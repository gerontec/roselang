# Scientific/Engineering (part 1 of 2)

[Index](README.md) · 726 packages in this topic, 124 more listed under another topic, by downloads.

part 1 · [part 2](scientific-engineering-2.md)

### numpy

Fundamental package for array computing in Python

`pip install numpy` · installs (wheel) · licence: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 · rank 21 · last release 2026-10-10 · [PyPI](https://pypi.org/project/numpy/) · [docs](https://numpy.org/doc/) · [source](https://github.com/numpy/numpy)

<details><summary>README extract</summary>

NumPy is the fundamental package for scientific computing with Python.

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires `pytest` and `hypothesis`. ...

</details>

### pandas

Powerful data structures for data analysis, time series, and statistics

`pip install pandas` · installs (wheel) · licence: BSD-3-Clause · rank 38 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pandas/) · [docs](https://pandas.pydata.org/docs/) · [source](https://github.com/pandas-dev/pandas)

<details><summary>README extract</summary>

| | |

| Testing | |
| Package | |
| Meta | |

pandas is a Python package that provides fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, real-world data analysis in Python. ...

Sections: pandas: A Powerful Python Data Analysis Toolkit, What is it?, Main Features, Where to get it, Dependencies, Documentation, Background, Getting Help

</details>

### scipy

Fundamental algorithms for scientific computing in Python

`pip install scipy` · installs (wheel) · licence: BSD License · rank 95 · last release 2026-08-21 · [PyPI](https://pypi.org/project/scipy/) · [docs](https://docs.scipy.org/doc/scipy/) · [source](https://github.com/scipy/scipy)

<details><summary>README extract</summary>

SciPy (pronounced "Sigh Pie") is an open-source software for mathematics,
science, and engineering. It includes modules for statistics, optimization,
integration, linear algebra, Fourier transforms, signal and image processing,
ODE solvers, and more.

- Report a security vulnerability: via Tidelift, as explained in
 our docs on Security ...

</details>

### scikit-learn

A set of python modules for machine learning and data mining

`pip install scikit-learn` · installs (wheel) · licence: BSD-3-Clause · rank 155 · last release 2026-09-10 · [PyPI](https://pypi.org/project/scikit-learn/) · [source](https://github.com/scikit-learn/scikit-learn)

<details><summary>README extract</summary>

scikit-learn is a Python module for machine learning built on top of
SciPy and is distributed under the 3-Clause BSD license.

The project was started in 2007 by David Cournapeau as a Google Summer
of Code project, and since then many volunteers have contributed. See
the About us page
for a list of core contributors. ...

Sections: Dependencies, Important links, Source code, Submitting a Pull Request, Documentation, Communication, Main Channels, Social Media Platforms, Resources

</details>

### cloudpickle

Pickler class to extend the standard pickle.Pickler functionality

`pip install cloudpickle` · installs (wheel) · licence: BSD License · rank 158 · last release 2025-11-03 · [PyPI](https://pypi.org/project/cloudpickle/)

<details><summary>README extract</summary>

`cloudpickle` makes it possible to serialize Python constructs not supported
by the default `pickle` module from the Python standard library.

`cloudpickle` is especially useful for cluster computing where Python
code is shipped over the network to execute on remote hosts, possibly close
to the data. ...

Example:
```python
>>> import cloudpickle
>>> squared = lambda x: x ** 2
>>> pickled_lambda = cloudpickle.dumps(squared)

>>> import pickle
>>> new_squared = pickle.loads(pickled_lambda)
>>> new_squared(2)
4
```

</details>

### joblib

Lightweight pipelining with Python functions

`pip install joblib` · installs (wheel) · licence: BSD-3-Clause · rank 169 · last release 2026-08-31 · [PyPI](https://pypi.org/project/joblib/) · [source](https://github.com/joblib/joblib)

<details><summary>README extract</summary>

The homepage of joblib with user documentation is located on:

To get the latest code using git, simply type:
If you don't have git installed, you can download a zip
of the latest code:

Sections: Getting the latest code, Dependencies, Running the test suite, Building the docs, Making a source tarball

</details>

### dill

serialize all of Python

`pip install dill` · installs (wheel) · licence: BSD License · rank 200 · last release 2026-01-19 · [PyPI](https://pypi.org/project/dill/) · [docs](http://dill.rtfd.io) · [source](https://github.com/uqfoundation/dill)

<details><summary>README extract</summary>

`dill` extends Python's `pickle` module for serializing and de-serializing
Python objects to the majority of the built-in Python types. Serialization
is the process of converting an object to a byte stream, and the inverse
of which is converting a byte stream back to a Python object hierarchy. ...

Example:
```python
>>> import dill as pickle
```

Sections: dill: serialize all of Python, About Dill, Major Features, Requirements, Basic Usage, More Information

</details>

### sympy

Computer algebra system (CAS) in Python

`pip install sympy` · installs (wheel) · licence: BSD License · rank 218 · last release 2025-04-27 · [PyPI](https://pypi.org/project/sympy/) · [source](https://github.com/sympy/sympy)

<details><summary>README extract</summary>

See the AUTHORS file for the list of authors.

And many more people helped on the SymPy mailing list, reported bugs,
helped organize SymPy's participation in the Google Summer of Code, the
Google Highly Open Participation Contest, Google Code-In, wrote and
blogged about SymPy... ...

Example:
```python
>>> from sympy import Symbol, cos
>>> x = Symbol('x')
>>> e = 1/cos(x)
>>> print(e.series(x, 0, 10))
1 + x2/2 + 5*x4/24 + 61*x6/720 + 277*x8/8064 + O(x**10)
```

Sections: SymPy, Download, Documentation and Usage, Tests, Clean, Bugs

</details>

### onnxruntime

ONNX Runtime is a runtime accelerator for Machine Learning models

`pip install onnxruntime` · installs (wheel) · licence: MIT License · rank 285 · last release 2026-10-26 · [PyPI](https://pypi.org/project/onnxruntime/)

<details><summary>README extract</summary>

ONNX Runtime is a performance-focused scoring engine for Open Neural Network Exchange (ONNX) models.
For more information on ONNX Runtime, please see aka.ms/onnxruntime or the Github project.

Release Notes :

Sections: ONNX Runtime, Changes, 1.31.1, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.1, 1.23.0, 1.22.0, 1.21.0

</details>

### multiprocess

better multiprocessing and multithreading in Python

`pip install multiprocess` · installs (wheel) · licence: BSD License · rank 315 · last release 2026-01-19 · [PyPI](https://pypi.org/project/multiprocess/) · [docs](http://multiprocess.rtfd.io) · [source](https://github.com/uqfoundation/multiprocess)

<details><summary>README extract</summary>

`multiprocess` is a fork of `multiprocessing`. `multiprocess` extends `multiprocessing` to provide enhanced serialization, using `dill`. `multiprocess` leverages `multiprocessing` to support the spawning of processes using the API of the Python standard library's `threading` module. ...

Example:
```python
from multiprocess import Process, Queue

def f(q):
    q.put('hello world')

if name == 'main':
    q = Queue()
    p = Process(target=f, args=[q])
    p.start()
    print (q.get())
    p.join()
```

Sections: About Multiprocess, Major Features, Requirements, Basic Usage, More Information

</details>

### polars

Blazingly fast DataFrame library

`pip install polars` · installs (wheel) · licence: MIT License · rank 396 · last release 2026-10-25 · [PyPI](https://pypi.org/project/polars/) · [docs](https://docs.pola.rs/api/python/stable/reference/index.html) · [source](https://github.com/pola-rs/polars)

<details><summary>README extract</summary>

Documentation:
 Python

 Rust

 Node.js

 Agents:
 Skill

 MCP
 User guide
 Discord

Polars is an analytical query engine for DataFrames, written in Rust. It is designed to be fast,
easy to use and expressive. Key features are:

- Fast: written from the ground up in Rust with multi-threaded, vectorized (SIMD) execution ...

Example:
```python
import polars as pl

df = (
    pl.scan_parquet("orders.parquet")
    .filter(pl.col("status") == "shipped")
    .group_by("customer_id")
    .agg(
        pl.col("amount").sum().alias("total"),
        pl.len().alias("n_orders"),
    )
    .sort("total", descending=True)
    .collect()
)
```

Sections: Polars: Extremely fast Query Engine for DataFrames, Polars in action, Performance, Handles larger-than-RAM data, Python, Distributed Polars

</details>

### torch

Tensors and Dynamic neural networks in Python with strong GPU acceleration

`pip install torch` · installs (wheel) · licence: Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND BSD-3-Clause  · rank 397 · last release 2026-10-28 · [PyPI](https://pypi.org/project/torch/) · [docs](https://pytorch.org/docs) · [source](https://github.com/pytorch/pytorch)

<details><summary>README extract</summary>

PyTorch is a Python package that provides two high-level features:
- Tensor computation (like NumPy) with strong GPU acceleration
- Deep neural networks built on a tape-based autograd system

You can reuse your favorite Python packages such as NumPy, SciPy, and Cython to extend PyTorch when needed. ...

Sections: More About PyTorch, A GPU-Ready Tensor Library, Dynamic Neural Networks: Tape-Based Autograd, Python First, Imperative Experiences, Fast and Lean, Extensions Without Pain, Binaries, NVIDIA Jetson Platforms, From Source, Prerequisites, Get the PyTorch Source, Adjust Build Options (Optional), Docker Image

</details>

### polars-runtime-32

Blazingly fast DataFrame library

`pip install polars-runtime-32` · installs (wheel) · licence: MIT License · rank 425 · last release 2026-10-25 · [PyPI](https://pypi.org/project/polars-runtime-32/) · [docs](https://docs.pola.rs/api/python/stable/reference/index.html) · [source](https://github.com/pola-rs/polars)

<details><summary>README extract</summary>

Packages that contain the binary shared libraries that back the polars python package. Not meant for
general consumption and just meant as dependencies for the polars main package.

</details>

### opencv-python-headless

Wrapper package for OpenCV python bindings.

`pip install opencv-python-headless` · installs (wheel) · licence: Apache Software License · rank 449 · last release 2026-07-02 · [PyPI](https://pypi.org/project/opencv-python-headless/)

<details><summary>README extract</summary>

OpenCV is raising funds to keep the library free for everyone, and we need the support of the entire community to do it. Donate to OpenCV on Github to show your support.

- OpenCV on Wheels
 - Installation and Usage
- Frequently Asked Questions ...

Sections: Keep OpenCV Free, OpenCV on Wheels, Documentation for opencv-python, CI build process, Manual builds, Manual debug builds, Source distributions, Licensing, Versioning, Manylinux wheels, Backward compatibility

</details>

### nltk

Natural Language Toolkit

`pip install nltk` · installs (wheel) · licence: Apache Software License · rank 497 · last release 2026-10-21 · [PyPI](https://pypi.org/project/nltk/) · [docs](https://www.nltk.org/) · [source](https://github.com/nltk/nltk)

<details><summary>README extract</summary>

NLTK -- the Natural Language Toolkit -- is a suite of open source Python
modules, data sets, and tutorials supporting research and development in Natural
Language Processing. NLTK requires Python version from 3.10 up to the latest 3.14.

For documentation, please visit nltk.org.

Sections: Natural Language Toolkit (NLTK), Citing, Copyright, Redistributing

</details>

### opencv-python

Wrapper package for OpenCV python bindings.

`pip install opencv-python` · installs (wheel) · licence: Apache Software License · rank 595 · last release 2026-07-02 · [PyPI](https://pypi.org/project/opencv-python/)

<details><summary>README extract</summary>

OpenCV is raising funds to keep the library free for everyone, and we need the support of the entire community to do it. Donate to OpenCV on Github to show your support.

- OpenCV on Wheels
 - Installation and Usage
- Frequently Asked Questions ...

Sections: Keep OpenCV Free, OpenCV on Wheels, Documentation for opencv-python, CI build process, Manual builds, Manual debug builds, Source distributions, Licensing, Versioning, Manylinux wheels, Backward compatibility

</details>

### rfc3987-syntax

Helper functions to syntactically validate strings according to RFC 3987.

`pip install rfc3987-syntax` · installs (wheel) · licence: MIT · rank 596 · last release 2025-07-18 · [PyPI](https://pypi.org/project/rfc3987-syntax/) · [docs](https://github.com/willynilly/rfc3987-syntax#readme) · [source](https://github.com/willynilly/rfc3987-syntax)

<details><summary>README extract</summary>

Helper functions to parse and validate the syntax of terms defined in RFC 3987 — the IETF standard for Internationalized Resource Identifiers (IRIs).

The goal of `rfc3987-syntax` is to provide a lightweight, permissively licensed Python module for validating that strings conform to the ABNF grammar defined in RFC 3987. These helpers are: ...

Example:
```python
from rfc3987_syntax import is_valid_syntax

if is_valid_syntax(term='iri', value='
    print("✓ Valid IRI syntax")

if not is_valid_syntax(term='iri', value='bob'):
    print("✗ Invalid IRI syntax")

if not is_valid_syntax(term='iri_reference', value='bob'):
    print("✓ Valid IRI-reference syntax")
```

Sections: rfc3987-syntax, 🎯 Purpose, ⚠️ Limitations, 🛠 Usage, 📚 Sources, Rule-to-Source Mapping

</details>

### cuda-bindings

Python bindings for CUDA

`pip install cuda-bindings` · installs (wheel) · licence: Apache-2.0 · rank 597 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cuda-bindings/) · [docs](https://nvidia.github.io/cuda-python/) · [source](https://github.com/NVIDIA/cuda-python)

<details><summary>README extract</summary>

cuda.bindings is a standard set of low-level interfaces, providing full coverage of and 1:1 access to the CUDA host APIs from Python. Checkout the Overview for the workflow and performance results.

* Repository
* Documentation
* Examples
* Issue tracker

For the installation instruction, please refer to the Installation page.

</details>

### patsy

A Python package for describing statistical models and for building design matrices.

`pip install patsy` · installs (wheel) · licence: BSD License · rank 608 · last release 2026-08-29 · [PyPI](https://pypi.org/project/patsy/)

<details><summary>README extract</summary>

Notice: `patsy` is no longer under active development. As of August 2021,
Matthew Wardrop (@matthewwardrop) and Tomás Capretto (@tomicapretto) have taken
on responsibility from Nathaniel Smith (@njsmith) for keeping the lights on, but
no new feature development is planned. ...

Sections: Patsy, Dependencies

</details>

### dask

Parallel PyData with Task Scheduling

`pip install dask` · installs (wheel) · licence: BSD-3-Clause · rank 642 · last release 2026-08-24 · [PyPI](https://pypi.org/project/dask/)

<details><summary>README extract</summary>

Dask is a flexible parallel computing library for analytics. See
documentation for more information.

</details>

### nvidia-nccl-cu12

NVIDIA Collective Communication Library (NCCL) Runtime

`pip install nvidia-nccl-cu12` · installs (wheel) · licence: not stated · rank 646 · last release 2026-09-22 · [PyPI](https://pypi.org/project/nvidia-nccl-cu12/)

<details><summary>README extract</summary>

NCCL (pronounced "Nickel") is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, and reduce-scatter. It has been optimized to achieve high bandwidth on any platform using PCIe, NVLink, NVswitch, as well as networking using InfiniBand Verbs or TCP/IP sockets.

</details>

### nvidia-nccl-cu13

NVIDIA Collective Communication Library (NCCL) Runtime

`pip install nvidia-nccl-cu13` · installs (wheel) · licence: not stated · rank 654 · last release 2026-09-22 · [PyPI](https://pypi.org/project/nvidia-nccl-cu13/)

<details><summary>README extract</summary>

NCCL (pronounced "Nickel") is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, and reduce-scatter. It has been optimized to achieve high bandwidth on any platform using PCIe, NVLink, NVswitch, as well as networking using InfiniBand Verbs or TCP/IP sockets.

</details>

### nvidia-cudnn-cu13

cuDNN runtime libraries

`pip install nvidia-cudnn-cu13` · installs (wheel) · licence: not stated · rank 683 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nvidia-cudnn-cu13/)

<details><summary>README extract</summary>

cuDNN runtime libraries containing primitives for deep neural networks.

</details>

### scikit-image

Image processing in Python

`pip install scikit-image` · installs (wheel) · licence: BSD License · rank 692 · last release 2025-12-20 · [PyPI](https://pypi.org/project/scikit-image/) · [docs](https://scikit-image.org/docs/stable) · [source](https://github.com/scikit-image/scikit-image)

### nvidia-cublas

CUBLAS native runtime libraries

`pip install nvidia-cublas` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 693 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cublas/)

### nvidia-nvjitlink

Nvidia JIT LTO Library

`pip install nvidia-nvjitlink` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 707 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-nvjitlink/)

<details><summary>README extract</summary>

NVIDIA compiler library for JIT LTO functionality.

</details>

### nvidia-nvshmem-cu13

NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.

`pip install nvidia-nvshmem-cu13` · installs (wheel) · licence: not stated · rank 712 · last release 2026-09-22 · [PyPI](https://pypi.org/project/nvidia-nvshmem-cu13/)

<details><summary>README extract</summary>

NVSHMEM is a parallel programming interface based on OpenSHMEM that provides efficient and scalable communication for NVIDIA GPU clusters. NVSHMEM creates a global address space for data that spans the memory of multiple GPUs and can be accessed with fine-grained GPU-initiated operations, CPU-initiated operations, and operations on CUDA streams.

</details>

### nvidia-cuda-nvrtc

NVRTC native runtime libraries

`pip install nvidia-cuda-nvrtc` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 714 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-nvrtc/)

### nvidia-cufft

CUFFT native runtime libraries

`pip install nvidia-cufft` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 717 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cufft/)

### nvidia-cusparselt-cu13

NVIDIA cuSPARSELt

`pip install nvidia-cusparselt-cu13` · installs (wheel) · licence: NVIDIA Proprietary Software · rank 720 · last release 2026-09-30 · [PyPI](https://pypi.org/project/nvidia-cusparselt-cu13/)

<details><summary>README extract</summary>

NVIDIA cuSPARSELt is a high-performance CUDA library dedicated to general matrix-matrix operations in which at least one operand is a structured sparse matrix with 50\% sparsity ratio:

where op(A)/op(B) refers to in-place operations such as transpose/non-transpose, and alpha, beta are scalars or vectors. ...

Features:
* *NVIDIA Sparse MMA tensor core* support

 +--------------+----------------+-----------------+-------------+---------------------------------+--------------------+
 | Input A/B Output D Block scaled ...

Sections: Key Features, Documentation

</details>

### nvidia-cusolver

CUDA solver native runtime libraries

`pip install nvidia-cusolver` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 721 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cusolver/)

### nvidia-cusparse

CUSPARSE native runtime libraries

`pip install nvidia-cusparse` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 722 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cusparse/)

### nvidia-cuda-runtime

CUDA Runtime native Libraries

`pip install nvidia-cuda-runtime` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 724 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-runtime/)

### pyproj

Python interface to PROJ (cartographic projections and coordinate transformations library)

`pip install pyproj` · installs (wheel) · licence: MIT · rank 726 · last release 2026-09-05 · [PyPI](https://pypi.org/project/pyproj/) · [docs](https://pyproj4.github.io/pyproj/) · [source](https://github.com/pyproj4/pyproj)

<details><summary>README extract</summary>

Python interface to PROJ (cartographic projections and coordinate transformations library).

Sections: pyproj, Documentation, Bugs/Questions

</details>

### nvidia-cuda-cupti

CUDA profiling tools runtime libs.

`pip install nvidia-cuda-cupti` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 727 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-cupti/)

<details><summary>README extract</summary>

Provides libraries to enable third party tools using GPU profiling APIs.

</details>

### nvidia-cufile

cuFile GPUDirect libraries

`pip install nvidia-cufile` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 739 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cufile/)

### nvidia-nvtx

NVIDIA Tools Extension

`pip install nvidia-nvtx` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 741 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-nvtx/)

<details><summary>README extract</summary>

A C-based API for annotating events, code ranges, and resources in your applications. Applications which integrate NVTX can use the Visual Profiler to capture and visualize these events and ranges.

</details>

### catalogue

Super lightweight function registries for your library

`pip install catalogue` · installs (wheel) · licence: MIT License · rank 745 · last release 2023-09-25 · [PyPI](https://pypi.org/project/catalogue/)

<details><summary>README extract</summary>

`catalogue` is a tiny, zero-dependencies library that makes it easy to **add
function (or object) registries** to your code. Function registries are helpful
when you have objects that need to be both easily serializable and fully
customizable. ...

Example:
```python
# YOUR PACKAGE
import catalogue

loaders = catalogue.create("your_package", "loaders")
```

Sections: 👩‍💻 Usage, ❓ FAQ, 🎛 API, function `catalogue.create`, class `Registry`, method `Registry.init`, method `Registry.contains`, method `Registry.call`, method `Registry.register`, method `Registry.get`, method `Registry.get_all`, method `Registry.get_entry_points`, method `Registry.get_entry_point`, method `Registry.find`

</details>

### nvidia-curand

CURAND native runtime libraries

`pip install nvidia-curand` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 751 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-curand/)

### spacy

Industrial-strength Natural Language Processing (NLP) in Python

`pip install spacy` · installs (wheel) · licence: MIT License · rank 769 · last release 2026-10-26 · [PyPI](https://pypi.org/project/spacy/) · [source](https://github.com/explosion/spaCy)

<details><summary>README extract</summary>

spaCy is a library for advanced Natural Language Processing in Python and
Cython. It's built on the very latest research, and was designed from day one to
be used in real products.

spaCy comes with pretrained pipelines and currently
supports tokenization and training for 70+ languages. ...

Features:
- Support for 70+ languages
- Trained pipelines for different languages and tasks
- Multi-task learning with pretrained transformers like BERT
- Support for pretrained word vectors and embeddings
- State-of-the-art speed ...

Example:
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
```

...

</details>

### murmurhash

Cython bindings for MurmurHash

`pip install murmurhash` · installs (wheel) · licence: MIT License · rank 770 · last release 2026-10-24 · [PyPI](https://pypi.org/project/murmurhash/)

### thinc

A refreshing functional take on deep learning, compatible with your favorite libraries

`pip install thinc` · installs (wheel) · licence: MIT License · rank 773 · last release 2026-10-27 · [PyPI](https://pypi.org/project/thinc/)

<details><summary>README extract</summary>

Thinc is a lightweight deep learning library that offers
an elegant, type-checked, functional-programming API for composing models,
with support for layers defined in other frameworks such as **PyTorch,
TensorFlow and MXNet**. You can use Thinc as an interface layer, a standalone
toolkit or a flexible way to develop new models. ...

Sections: From the makers of spaCy and Prodigy, 🔥 Features, 🚀 Quickstart, 📓 Selected examples and notebooks, 📖 Documentation & usage guides, 🗺 What's where, 👷‍♀️ Building Thinc from source, 🚦 Running tests

</details>

### srsly

Modern high-performance serialization utilities for Python

`pip install srsly` · installs (wheel) · licence: MIT License · rank 774 · last release 2026-11-03 · [PyPI](https://pypi.org/project/srsly/)

<details><summary>README extract</summary>

This package bundles some of the best Python serialization libraries into one
convenience package, with a high-level API that makes it easy to write code
that's correct across platforms and Pythons. This allows us to provide all the
serialization utilities we need in a single binary wheel. ...

Example:
```python
data = {"foo": "bar", "baz": 123}
json_string = srsly.json_dumps(data)
```

Sections: Motivation, API, JSON, function `srsly.json_dumps`, function `srsly.json_loads`, function `srsly.write_json`, function `srsly.read_json`, function `srsly.write_gzip_json`, function `srsly.write_gzip_jsonl`, function `srsly.read_gzip_json`, function `srsly.read_gzip_jsonl`, function `srsly.write_jsonl`, function `srsly.read_jsonl`, function `srsly.is_json_serializable`

</details>

### blis

The Blis BLAS-like linear algebra library, as a self-contained C-extension.

`pip install blis` · installs (wheel) · licence: BSD License · rank 780 · last release 2026-10-25 · [PyPI](https://pypi.org/project/blis/)

<details><summary>README extract</summary>

This repository provides the
Blis linear algebra routines as a
self-contained Python C-extension.

It is safe to concurrently use Blis from multiple threads with immutable data. The
library is re-entrant, does not rely on global state, and is compatible with
free-threaded Python interpreters (e.g. 3.14t). ...

Example:
```python
cimport blis.cy
A = calloc(nN * nI, sizeof(float))
B = calloc(nO * nI, sizeof(float))
C = calloc(nr_b0 * nr_b1, sizeof(float))
blis.cy.gemm(blis.cy.NO_TRANSPOSE, blis.cy.NO_TRANSPOSE,
             nO, nI, nN,
             1.0, A, nI, 1, B, nO, 1,
             1.0, C, nO, 1)
```

Sections: Thread-safety, Compiler requirements, Building BLIS for alternative architectures, Usage, Updating the build files, Linux

</details>

### preshed

Cython hash table that trusts the keys are pre-hashed

`pip install preshed` · installs (wheel) · licence: MIT License · rank 784 · last release 2026-10-25 · [PyPI](https://pypi.org/project/preshed/)

<details><summary>README extract</summary>

Simple but high performance Cython hash table mapping pre-randomized keys to
`void*` values. Inspired by
Jeff Preshing.

All Python APIs provded by the `BloomFilter` and `PreshMap` classes are
thread-safe on both the GIL-enabled build and the free-threaded build of Python
3.14 and newer. ...

Example:
```python
from preshed.maps import PreshMap

map = PreshMap()                  # create with default size
map = PreshMap(initial_size=1024) # create with initial capacity (must be power of 2)

map[key] = value        # set a value
value = map[key]        # get a value (returns None if missing)
value = map.pop(key)    # remove and return a value
...
```

Sections: preshed: Cython Hash Table for Pre-Hashed Keys, Usage, PreshMap, BloomFilter, PreshCounter, Cython API

</details>

### cymem

Manage calls to calloc/free through Cython

`pip install cymem` · installs (wheel) · licence: MIT License · rank 786 · last release 2026-10-24 · [PyPI](https://pypi.org/project/cymem/)

<details><summary>README extract</summary>

cymem provides two small memory-management helpers for Cython. They make it easy
to tie memory to a Python object's life-cycle, so that the memory is freed when
the object is garbage collected.

Features:
The most useful is `cymem.Pool`, which acts as a thin wrapper around the calloc
function:

The `Pool` object saves the memory addresses internally, and frees them when the
object is garbage collected. ...

Example:
```python
"""Example without Cymem

To use an array of structs, we must carefully walk the data structure when
we deallocate it.
"""

from libc.stdlib cimport calloc, free

cdef struct SparseRow:
    size_t length
    size_t* indices
    double* values

cdef struct SparseMatrix:
    size_t length
    SparseRow* rows

cdef class MatrixArray:
...
```

...

</details>

### confection

The sweetest config system for Python

`pip install confection` · installs (wheel) · licence: MIT License · rank 806 · last release 2026-10-26 · [PyPI](https://pypi.org/project/confection/)

<details><summary>README extract</summary>

`confection` :candy: is a lightweight library that offers a **configuration
system** letting you conveniently describe arbitrary trees of objects.

Configuration is a huge challenge for machine-learning code because you may want
to expose almost any detail of any function as a hyperparameter. ...

Example:
```python
import dataclasses
from typing import Union, Iterable
import catalogue
from confection import registry, Config

# Create a new registry.
registry.optimizers = catalogue.create("confection", "optimizers", entry_points=False)

# Define a dummy optimizer class.
@dataclasses.dataclass
class MyCoolOptimizer:
    learn_rate: float
    gamma: float

...
```

...

</details>

### spacy-legacy

Legacy registered functions for spaCy backwards compatibility

`pip install spacy-legacy` · installs (wheel) · licence: MIT License · rank 812 · last release 2023-01-23 · [PyPI](https://pypi.org/project/spacy-legacy/)

<details><summary>README extract</summary>

This package includes outdated registered functions for spaCy v3.x, for example model architectures, pipeline components and utilities. It's installed automatically as a dependency of spaCy, and allows us to provide backwards compatibility, while keeping the core library tidy and up to date. ...

</details>

### pandas-stubs

Type annotations for pandas

`pip install pandas-stubs` · installs (wheel) · licence: BSD-3-Clause · rank 813 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pandas-stubs/) · [docs](https://pandas.pydata.org/pandas-docs/stable) · [source](https://github.com/pandas-dev/pandas-stubs)

<details><summary>README extract</summary>

These are public type stubs for pandas, following the
convention of providing stubs in a separate package, as specified in PEP 561. The stubs cover the most typical use cases of
pandas. In general, these stubs are narrower than what is possibly allowed by pandas,
but follow a convention of suggesting best recommended practices for using pandas. ...

Example:
```python
import pandas as pd

decimals = pd.DataFrame({'TSLA': 2, 'AMZN': 1})
prices = pd.DataFrame(data={'date': ['2021-08-13', '2021-08-07', '2021-08-21'],
                            'TSLA': [720.13, 716.22, 731.22], 'AMZN': [3316.50, 3200.50, 3100.23]})
rounded_prices = prices.round(decimals=decimals)
```

...

</details>

### weasel

Weasel: A small and easy workflow system

`pip install weasel` · installs (wheel) · licence: MIT License · rank 821 · last release 2026-10-26 · [PyPI](https://pypi.org/project/weasel/) · [source](https://github.com/explosion/weasel/)

<details><summary>README extract</summary>

Weasel lets you manage and share end-to-end workflows for
different use cases and domains, and orchestrate training, packaging and
serving your custom pipelines. You can start off by cloning a pre-defined
project template, adjust it to fit your needs, load in your data, train a
pipeline, export it as a Python package, upload your outputs to a ...

Sections: Weasel: A small and easy workflow system, 💡 Example: Get started with a project template, 📕 Documentation, Migrating from spaCy Projects

</details>

### great-expectations

Always know what to expect from your data.

`pip install great-expectations` · installs (wheel) · licence: Apache Software License · rank 841 · last release 2026-10-22 · [PyPI](https://pypi.org/project/great-expectations/) · [docs](https://docs.greatexpectations.io) · [source](https://github.com/fivetran/great_expectations)

<details><summary>README extract</summary>

Always know what to expect from your data. (See for full description).

</details>

### nvidia-cudnn-cu12

cuDNN runtime libraries

`pip install nvidia-cudnn-cu12` · installs (wheel) · licence: not stated · rank 844 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nvidia-cudnn-cu12/)

<details><summary>README extract</summary>

cuDNN runtime libraries containing primitives for deep neural networks.

</details>

### nvidia-cublas-cu12

CUBLAS native runtime libraries

`pip install nvidia-cublas-cu12` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 852 · last release 2026-10-30 · [PyPI](https://pypi.org/project/nvidia-cublas-cu12/)

### dask-expr

High Level Expressions for Dask

`pip install dask-expr` · installs (wheel) · licence: BSD License · rank 857 · last release 2025-01-21 · [PyPI](https://pypi.org/project/dask-expr/) · [source](https://github.com/dask-contrib/dask-expr/)

<details><summary>README extract</summary>

Dask DataFrames with query optimization.

This is a rewrite of Dask DataFrame that includes query
optimization and generally improved organization.

More in our blog posts:
- Dask Expressions overview
- TPC-H benchmark results vs. Dask DataFrame

Example

Query Representation

Dask-expr encodes user code in an expression tree: ...

Example:
```python
import dask_expr as dx

df = dx.datasets.timeseries()
df.head()

df.groupby("name").x.mean().compute()
```

</details>

### nvidia-cuda-nvrtc-cu12

NVRTC native runtime libraries

`pip install nvidia-cuda-nvrtc-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 887 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cuda-nvrtc-cu12/)

### pydata-google-auth

PyData helpers for authenticating to Google APIs

`pip install pydata-google-auth` · installs (wheel) · licence: BSD License · rank 891 · last release 2025-01-23 · [PyPI](https://pypi.org/project/pydata-google-auth/)

<details><summary>README extract</summary>

pydata-google-auth is a package providing helpers for authenticating to Google APIs.

Example:
```python
import pydata_google_auth
credentials = pydata_google_auth.get_user_credentials(
    ['
)

# Use the credentials in other libraries, such as the Google BigQuery
# client library.
from google.cloud import bigquery
client = bigquery.Client(project='YOUR-PROJECT-ID', credentials=credentials)
```

Sections: pydata-google-auth, Usage

</details>

### nvidia-cufft-cu12

CUFFT native runtime libraries

`pip install nvidia-cufft-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 895 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cufft-cu12/)

### nvidia-cusparse-cu12

CUSPARSE native runtime libraries

`pip install nvidia-cusparse-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 897 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cusparse-cu12/)

### nvidia-cusolver-cu12

CUDA solver native runtime libraries

`pip install nvidia-cusolver-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 899 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cusolver-cu12/)

### pooch

A friend to fetch your data files

`pip install pooch` · installs (wheel) · licence: BSD-3-Clause · rank 902 · last release 2026-01-30 · [PyPI](https://pypi.org/project/pooch/) · [docs](https://www.fatiando.org/pooch) · [source](https://github.com/fatiando/pooch)

<details><summary>README extract</summary>

Documentation (latest) •
Documentation (main branch) •
Contributing •
Contact •
Ask a question

Part of the Fatiando a Terra project

> Just want to download a file without messing with `requests` and `urllib`?
> Trying to add sample datasets to your Python package?
> Pooch is here to help! ...

Example:
```python
import pooch
import pandas as pd

# Download a file and save it locally, returning the path to it.
# Running this again will not cause a download. Pooch will check the hash
# (checksum) of the downloaded file against the given value to make sure
# it's the right file (not corrupted or outdated).
fname_bathymetry = pooch.retrieve(
    url="
...
```

Sections: About, Projects using Pooch, Example, Getting involved

</details>

### nvidia-nvjitlink-cu12

Nvidia JIT LTO Library

`pip install nvidia-nvjitlink-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 906 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-nvjitlink-cu12/)

<details><summary>README extract</summary>

NVIDIA compiler library for JIT LTO functionality.

</details>

### nvidia-cuda-runtime-cu12

CUDA Runtime native Libraries

`pip install nvidia-cuda-runtime-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 910 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cuda-runtime-cu12/)

### nvidia-curand-cu12

CURAND native runtime libraries

`pip install nvidia-curand-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 915 · last release 2025-05-01 · [PyPI](https://pypi.org/project/nvidia-curand-cu12/)

### nvidia-cuda-cupti-cu12

CUDA profiling tools runtime libs.

`pip install nvidia-cuda-cupti-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 930 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cuda-cupti-cu12/)

<details><summary>README extract</summary>

Provides libraries to enable third party tools using GPU profiling APIs.

</details>

### nvidia-nvtx-cu12

NVIDIA Tools Extension

`pip install nvidia-nvtx-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 965 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-nvtx-cu12/)

<details><summary>README extract</summary>

A C-based API for annotating events, code ranges, and resources in your applications. Applications which integrate NVTX can use the Visual Profiler to capture and visualize these events and ranges.

</details>

### jpype1

A Python to Java bridge

`pip install jpype1` · installs (wheel) · licence: Apache-2.0 · rank 1031 · last release 2026-05-28 · [PyPI](https://pypi.org/project/jpype1/)

<details><summary>README extract</summary>

JPype is a Python module to provide full access to Java from
within Python. It allows Python to make use of Java only libraries,
exploring and visualization of Java structures, development and testing
of Java libraries, scientific computing, and much more. ...

</details>

### nvidia-cusparselt-cu12

NVIDIA cuSPARSELt

`pip install nvidia-cusparselt-cu12` · installs (wheel) · licence: NVIDIA Proprietary Software · rank 1032 · last release 2025-09-05 · [PyPI](https://pypi.org/project/nvidia-cusparselt-cu12/)

<details><summary>README extract</summary>

NVIDIA cuSPARSELt is a high-performance CUDA library dedicated to general matrix-matrix operations in which at least one operand is a structured sparse matrix with 50\% sparsity ratio:

where op(A)/op(B) refers to in-place operations such as transpose/non-transpose, and alpha, beta are scalars or vectors. ...

Features:
* *NVIDIA Sparse MMA tensor core* support

 +--------------+----------------+-----------------+-------------+---------------------------------+--------------------+
 | Input A/B Output D Block scaled ...

Sections: Key Features, Documentation

</details>

### optuna

A hyperparameter optimization framework

`pip install optuna` · installs (wheel) · licence: MIT License · rank 1035 · last release 2026-09-07 · [PyPI](https://pypi.org/project/optuna/) · [docs](https://optuna.readthedocs.io) · [source](https://github.com/optuna/optuna)

<details><summary>README extract</summary>

:link: Website
| :page_with_curl: Docs
| :gear: Install Guide
| :pencil: Tutorial
| :bulb: Examples
| Twitter
| LinkedIn
| Medium

*Optuna* is an automatic hyperparameter optimization software framework, particularly designed
for machine learning. It features an imperative, *define-by-run* style user API. ...

Example:
```python
import optuna
import sklearn

# Define an objective function to be minimized.
def objective(trial):

    # Invoke suggest methods of a Trial object to generate hyperparameters.
    regressor_name = trial.suggest_categorical("regressor", ["SVR", "RandomForest"])
    if regressor_name == "SVR":
...
```

...

</details>

### tensorflow

TensorFlow is an open source machine learning framework for everyone.

`pip install tensorflow` · does not install on CPython 3.14 · licence: Apache Software License · rank 1040 · last release 2026-03-06 · [PyPI](https://pypi.org/project/tensorflow/)

<details><summary>README extract</summary>

TensorFlow is an open source software library for high performance numerical
computation. Its flexible architecture allows easy deployment of computation
across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters
of servers to mobile and edge devices. ...

</details>

### skops

A set of tools, related to machine learning in production.

`pip install skops` · installs (wheel) · licence: OSI Approved · rank 1048 · last release 2026-09-24 · [PyPI](https://pypi.org/project/skops/) · [docs](https://skops.readthedocs.io/en/stable/) · [source](http://github.com/skops-dev/skops)

<details><summary>README extract</summary>

`skops` is a Python library helping you share your scikit-learn based models and put them in production.
At the moment, it includes `skops.io` to securely persist sklearn estimators and
more, without using `pickle`. It also includes `skops.card` to create a model
card explaining what the model does and how it should be used. ...

Sections: SKOPS, Bug Reports and Questions

</details>

### xarray

N-D labeled arrays and datasets in Python

`pip install xarray` · installs (wheel) · licence: Apache-2.0 · rank 1095 · last release 2026-09-29 · [PyPI](https://pypi.org/project/xarray/) · [docs](https://docs.xarray.dev)

<details><summary>README extract</summary>

xarray (pronounced "ex-array", formerly known as xray) is an open source project and Python
package that makes working with labelled multi-dimensional arrays
simple, efficient, and fun! ...

Features:
Multi-dimensional (a.k.a. N-dimensional, ND) arrays (sometimes called
"tensors") are an essential part of computational science. ...

Sections: xarray: N-D labeled arrays and datasets, Why xarray?, Documentation, Get in touch, NumFOCUS

</details>

### keras

Multi-backend Keras

`pip install keras` · installs (wheel) · licence: Apache License 2.0 · rank 1113 · last release 2026-07-29 · [PyPI](https://pypi.org/project/keras/) · [source](https://github.com/keras-team/keras)

<details><summary>README extract</summary>

Keras 3 is a multi-backend deep learning framework, with support for JAX, TensorFlow, PyTorch, and OpenVINO (for inference-only).
Effortlessly build and train models for computer vision, natural language processing, audio processing,
timeseries forecasting, recommender systems, etc. ...

Features:
- Run your high-level Keras workflows on top of any framework -- benefiting at will from the advantages of each framework,
e.g. the scalability and performance of JAX or the production ecosystem options of TensorFlow.
- Write custom components (e.g. ...

Example:
```python
import os
os.environ["KERAS_BACKEND"] = "jax"

import keras
```

Sections: Keras 3: Deep Learning for Humans, Backend Compatibility Table, Configuring your backend, Backwards compatibility, Why use Keras 3?

</details>

### pathos

parallel graph management and execution in heterogeneous computing

`pip install pathos` · installs (wheel) · licence: BSD License · rank 1134 · last release 2026-01-20 · [PyPI](https://pypi.org/project/pathos/) · [docs](http://pathos.rtfd.io) · [source](https://github.com/uqfoundation/pathos)

<details><summary>README extract</summary>

`pathos` is a framework for heterogeneous computing. It provides a consistent
high-level interface for configuring and launching parallel computations
across heterogeneous resources. ...

Sections: About the Pathos Framework, About Pathos, Major Features, Requirements, More Information

</details>

### pox

utilities for filesystem exploration and automated builds

`pip install pox` · installs (wheel) · licence: BSD License · rank 1136 · last release 2026-01-19 · [PyPI](https://pypi.org/project/pox/) · [docs](http://pox.rtfd.io) · [source](https://github.com/uqfoundation/pox)

<details><summary>README extract</summary>

`pox` provides a collection of utilities for navigating and manipulating
filesystems. This module is designed to facilitate some of the low level
operating system interactions that are useful when exploring a filesystem
on a remote host, where queries such as *"what is the root of the filesystem?"*,
*"what is the user's name?"*, and *"what login ...

Example:
```python
>>> import pox
>>> pox.homedir()
'/Users/mmckerns'
>>> pox.rootdir()
'/'
```

Sections: About Pox, Major Features, Requirements, Basic Usage, More Information

</details>

### ppft

distributed and parallel Python

`pip install ppft` · installs (wheel) · licence: BSD License · rank 1141 · last release 2026-01-19 · [PyPI](https://pypi.org/project/ppft/) · [docs](http://ppft.rtfd.io) · [source](https://github.com/uqfoundation/ppft)

<details><summary>README extract</summary>

`ppft` is a friendly fork of Parallel Python (`pp`). `ppft` extends Parallel Python to provide packaging and distribution with `pip` and `setuptools`, support for Python 3, and enhanced serialization using `dill.source`. ...

Example:
```python
>>> import ppft as pp
>>> job_server = pp.Server()
```

Sections: ppft: distributed and parallel Python, About Ppft, Major Features, Requirements, Basic Usage, More Information

</details>

### kfp

Kubeflow Pipelines SDK

`pip install kfp` · installs (wheel) · licence: Apache Software License · rank 1150 · last release 2026-10-28 · [PyPI](https://pypi.org/project/kfp/) · [docs](https://kubeflow-pipelines.readthedocs.io/en/stable/) · [source](https://github.com/kubeflow/pipelines/tree/master/sdk)

<details><summary>README extract</summary>

Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers within the Kubeflow project.

Use Kubeflow Pipelines to compose a multi-step workflow (pipeline) as a graph of containerized tasks using Python code and/or YAML. ...

Example:
```python
from kfp import dsl
import kfp

@dsl.component
def add(a: float, b: float) -> float:
    '''Calculates sum of two arguments'''
    return a + b

@dsl.pipeline(
    name='Addition pipeline',
    description='An example pipeline that performs addition calculations.')
def add_pipeline(
    a: float = 1.0,
    b: float = 7.0,
):
...
```

Sections: Preview pipelines locally, Getting started

</details>

### timm

PyTorch Image Models

`pip install timm` · installs (wheel) · licence: Apache Software License · rank 1156 · last release 2026-11-03 · [PyPI](https://pypi.org/project/timm/) · [docs](https://huggingface.co/docs/timm/en/index) · [source](https://github.com/huggingface/pytorch-image-models)

<details><summary>README extract</summary>

- What's New
- Introduction
- Models
- Features
- Results
- Getting Started (Documentation)
- Train, Validation, Inference Scripts
- Awesome PyTorch Resources
- Licenses
- Citing ...

Sections: PyTorch Image Models, What's New, November 3, 2026, October 24, 2026, October 13, 2026, October 9, 2026, September 25, 2026, September 22, 2026, September 10-11, 2026, August 27, 2026, August 11, 2026, July 10, 2026, May 27, 2026, May 8, 2026

</details>

### cytoolz

Cython implementation of Toolz: High performance functional utilities

`pip install cytoolz` · installs (wheel) · licence: BSD-3-Clause · rank 1224 · last release 2026-10-08 · [PyPI](https://pypi.org/project/cytoolz/) · [docs](https://toolz.readthedocs.io/en/latest/) · [source](https://github.com/pytoolz/cytoolz)

<details><summary>README extract</summary>

Cython implementation of the
 package, which
provides high performance utility functions for iterables, functions,
and dictionaries.

`toolz` is a pure Python package that borrows heavily from contemporary
functional languages. ...

Sections: CyToolz, Dependencies

</details>

### shap

A unified approach to explain the output of any machine learning model.

`pip install shap` · installs (wheel) · licence: MIT License · rank 1271 · last release 2026-10-16 · [PyPI](https://pypi.org/project/shap/) · [docs](https://shap.readthedocs.io/en/latest/index.html) · [source](http://github.com/shap/shap)

<details><summary>README extract</summary>

SHAP (SHapley Additive exPlanations) is a game theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from game theory and their related extensions (see papers for details and citations).

Example:
```python
import xgboost
import shap

# train an XGBoost model
X, y = shap.datasets.california()
model = xgboost.XGBRegressor().fit(X, y)

# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn, transformers, Spark, etc.)
explainer = shap.Explainer(model)
shap_values = explainer(X)

...
```

...

</details>

### pandera

A light-weight and flexible data validation and testing tool for statistical data objects.

`pip install pandera` · installs (wheel) · licence: MIT License · rank 1281 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pandera/) · [docs](https://pandera.readthedocs.io)

<details><summary>README extract</summary>

📊 🔎 ✅

 Data validation for scientists, engineers, and analysts seeking correctness.

Pandera is a Union.ai open
source project that provides a flexible and expressive API for performing data
validation on dataframe-like objects. The goal of Pandera is to make data
processing pipelines more readable and robust with statistically typed
dataframes.

Example:
```python
import pandas as pd
import pandera.pandas as pa

# data to validate
df = pd.DataFrame({
    "column1": [1, 2, 3],
    "column2": [1.1, 1.2, 1.3],
    "column3": ["a", "b", "c"],
})
```

Sections: The Open-source Framework for Dataset Validation, Get started, Next steps

</details>

### tritonclient

Python client library and utilities for communicating with Triton Inference Server

`pip install tritonclient` · installs (wheel) · licence: BSD-3-Clause · rank 1299 · last release 2026-11-02 · [PyPI](https://pypi.org/project/tritonclient/)

<details><summary>README extract</summary>

See download-using-python-package-installer-pip for package details.

The client examples demonstrate how to use the package to issue request to triton inference server.

</details>

### scikit-build-core

Build backend for CMake based projects

`pip install scikit-build-core` · installs (wheel) · licence: Apache-2.0 · rank 1328 · last release 2026-11-03 · [PyPI](https://pypi.org/project/scikit-build-core/) · [docs](https://scikit-build-core.readthedocs.io)

<details><summary>README extract</summary>

[][rtd-link]
[][github-discussions-link]
[][discord-link]

[][actions-link]
[][codecov-link]

[][pypi-link]
[][conda-link]
[][pypi-link]
[][download-link]

> [!NOTE]
> We have a public Scikit-build community meeting every month!
> Join us on Google Meet on the third
> Friday of every month at 12:00 PM ET. ...

Sections: scikit-build-core, Example, Configuration, Top-level, `cmake`, `ninja`, `logging`, `sdist`, `wheel`, `backport`, `editable`, `build`, `generate[]`, `messages`

</details>

### nvidia-cufile-cu12

cuFile GPUDirect libraries

`pip install nvidia-cufile-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 1348 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cufile-cu12/)

### opencv-contrib-python

Wrapper package for OpenCV python bindings.

`pip install opencv-contrib-python` · installs (wheel) · licence: Apache Software License · rank 1364 · last release 2026-07-02 · [PyPI](https://pypi.org/project/opencv-contrib-python/)

<details><summary>README extract</summary>

OpenCV is raising funds to keep the library free for everyone, and we need the support of the entire community to do it. Donate to OpenCV on Github to show your support.

- OpenCV on Wheels
 - Installation and Usage
- Frequently Asked Questions ...

Sections: Keep OpenCV Free, OpenCV on Wheels, Documentation for opencv-python, CI build process, Manual builds, Manual debug builds, Source distributions, Licensing, Versioning, Manylinux wheels, Backward compatibility

</details>

### Bottleneck

Fast NumPy array functions written in C

`pip install Bottleneck` · installs (wheel) · licence: Simplified BSD · rank 1386 · last release 2025-09-08 · [PyPI](https://pypi.org/project/Bottleneck/)

<details><summary>README extract</summary>

Bottleneck is a collection of fast NumPy array functions written in C.

Let's give it a try. Create a NumPy array:

Find the nanmean:

Moving window mean:

Example:
```python
>>> import numpy as np
>>> a = np.array([1, 2, np.nan, 4, 5])
```

Sections: Benchmark, Where, Unit tests

</details>

### lancedb

lancedb

`pip install lancedb` · installs (wheel) · licence: Apache Software License · rank 1438 · last release 2026-10-29 · [PyPI](https://pypi.org/project/lancedb/) · [source](https://github.com/lancedb/lancedb)

<details><summary>README extract</summary>

A Python library for LanceDB.

Example:
```python
import lancedb
db = lancedb.connect('<PATH_TO_LANCEDB_DATASET>')
table = db.open_table('my_table')
results = table.search([0.1, 0.3]).limit(20).to_list()
print(results)
```

Sections: LanceDB Python SDK, Pre-Haswell x86_64 hosts: `lancedb-compat`, Threading in CPU-limited containers, Usage, Basic Example, Opening SQL blob descriptors

</details>

### pylatexenc

Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion

`pip install pylatexenc` · installs (wheel) · licence: MIT License · rank 1440 · last release 2026-07-25 · [PyPI](https://pypi.org/project/pylatexenc/)

<details><summary>README extract</summary>

Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion

The `pylatexenc.latexencode` module provides a function `unicode_to_latex()`
which converts a unicode string into LaTeX text and escape sequences. It should
recognize accented characters and most math symbols. ...

Sections: pylatexenc, Unicode Text to LaTeX code, Parsing LaTeX code & converting to plain text (unicode), Documentation

</details>

### Pint

Physical quantities module

`pip install Pint` · installs (wheel) · licence: BSD-3-Clause · rank 1487 · last release 2026-10-19 · [PyPI](https://pypi.org/project/Pint/) · [docs](https://pint.readthedocs.io/)

<details><summary>README extract</summary>

Pint is a Python package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. ...

Example:
```python
>>> import pint
>>> ureg = pint.UnitRegistry()
>>> 3 * ureg.meter + 4 * ureg.cm
Quantity(3.04, "meter")
```

Sections: Pint: makes units easy, Documentation, Command-line converter, Design principles

</details>

### python-crfsuite

Python binding for CRFsuite

`pip install python-crfsuite` · installs (wheel) · licence: MIT License · rank 1494 · last release 2025-12-23 · [PyPI](https://pypi.org/project/python-crfsuite/)

<details><summary>README extract</summary>

python-crfsuite is a python binding to CRFsuite.

Sections: python-crfsuite, Usage, See Also, Alternatives

</details>

### pynndescent

Nearest Neighbor Descent

`pip install pynndescent` · installs (wheel) · licence: BSD-2-Clause · rank 1515 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pynndescent/)

<details><summary>README extract</summary>

PyNNDescent is a Python nearest neighbor descent for approximate nearest neighbors.
It provides a python implementation of Nearest Neighbor
Descent for k-neighbor-graph construction and approximate nearest neighbor
search, as per the paper:

Dong, Wei, Charikar Moses, and Kai Li. ...

Features:
PyNNDescent provides fast approximate nearest neighbor queries. The
ann-benchmarks system puts it
solidly in the mix of top performing ANN libraries:

SIFT-128 Euclidean

NYTimes-256 Angular ...

Example:
```python
from pynndescent import NNDescent
index = NNDescent(data)
```

Sections: PyNNDescent, Why use PyNNDescent?, How to use PyNNDescent

</details>

### umap-learn

Uniform Manifold Approximation and Projection

`pip install umap-learn` · installs (wheel) · licence: OSI Approved · rank 1554 · last release 2026-04-08 · [PyPI](https://pypi.org/project/umap-learn/) · [source](http://github.com/lmcinnes/umap)

<details><summary>README extract</summary>

Uniform Manifold Approximation and Projection (UMAP) is a dimension reduction
technique that can be used for visualisation similarly to t-SNE, but also for
general non-linear dimension reduction. The algorithm is founded on three
assumptions about the data:

1. The data is uniformly distributed on a Riemannian manifold;
2. ...

Example:
```python
import umap
from sklearn.datasets import load_digits

digits = load_digits()

embedding = umap.UMAP().fit_transform(digits.data)
```

Sections: UMAP, How to use UMAP, Benefits of UMAP, Performance and Examples, Plotting, Parametric UMAP, densMAP, GPU-Accelerated UMAP with torchdr

</details>

### tensorflow-estimator

TensorFlow Estimator.

`pip install tensorflow-estimator` · installs (wheel) · licence: Apache Software License · rank 1576 · last release 2023-11-07 · [PyPI](https://pypi.org/project/tensorflow-estimator/)

<details><summary>README extract</summary>

TensorFlow Estimator is a high-level API that encapsulates model training,
evaluation, prediction, and exporting.

</details>

### probableparsing

Common methods for propbable parsers

`pip install probableparsing` · installs (wheel) · licence: MIT License · rank 1616 · last release 2016-12-19 · [PyPI](https://pypi.org/project/probableparsing/)

### usaddress

Parse US addresses using conditional random fields

`pip install usaddress` · installs (wheel) · licence: MIT License · rank 1627 · last release 2025-08-07 · [PyPI](https://pypi.org/project/usaddress/)

<details><summary>README extract</summary>

usaddress is a Python library for parsing unstructured United States address strings into address components, using advanced NLP methods.

What this can do: Using a probabilistic model, it makes (very educated) guesses in identifying address components, even in tricky cases where rule-based parsers typically break down. ...

Example:
```python
import usaddress
addr='123 Main St. Suite 100 Chicago, IL'

# The parse method will split your address string into components, and label each component.
...
```

Sections: usaddress, Tools built with usaddress, Parserator API, Parserator Google Sheets App, How to use the usaddress python library, Adding new training data, Important links, Team, Bad Parses / Bugs, Note on Patches/Pull Requests, Copyright

</details>

### exchange_calendars

Calendars for securities exchanges

`pip install exchange_calendars` · installs (wheel) · licence: Apache-2.0 · rank 1631 · last release 2026-03-10 · [PyPI](https://pypi.org/project/exchange_calendars/) · [docs](https://github.com/gerrymanoim/exchange_calendars/tree/master/docs) · [source](https://github.com/gerrymanoim/exchange_calendars)

<details><summary>README extract</summary>

A Python library for defining and querying calendars for security exchanges.

Calendars for more than 50 exchanges available out-the-box! If you still can't find the calendar you're looking for, create a new one!

Example:
```python
import exchange_calendars as xcals
```

Sections: exchange_calendars, Quick Start, Working with sessions, Working with minutes, Tutorials, Command Line Usage, Frequently Asked Questions, How can I create a new calendar?, What times are considered open and closed?, Calendars, market-prices, Deprecations and Renaming, Methods renamed in version 4.0.3 and removed in 4.3, Methods deprecated in 4.0 and removed in 4.3

</details>

### gradio

Python library for easily interacting with trained machine learning models

`pip install gradio` · installs (wheel) · licence: Apache-2.0 · rank 1634 · last release 2026-10-28 · [PyPI](https://pypi.org/project/gradio/)

<details><summary>README extract</summary>

Website
| Documentation
| Guides
| Getting Started
| Examples

Gradio is an open-source Python package that allows you to quickly build a demo or web application for your machine learning model, API, or any arbitrary Python function. ...

Example:
```python
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()
```

Sections: Gradio: Build Machine Learning Web Apps — in Python, Building Your First Demo, Sharing Your Demo, An Overview of Gradio, Custom Demos with `gr.Blocks`, Chatbots with `gr.ChatInterface`, The Gradio Python & JavaScript Ecosystem, What's Next?, AI Coding Skills, Questions?, Open Source Stack

</details>

### gradio-client

Python library for easily interacting with trained machine learning models

`pip install gradio-client` · installs (wheel) · licence: Apache-2.0 · rank 1643 · last release 2026-10-02 · [PyPI](https://pypi.org/project/gradio-client/)

<details><summary>README extract</summary>

This directory contains the source code for `gradio_client`, a lightweight Python library that makes it very easy to use any Gradio app as an API.

As an example, consider this Hugging Face Space that transcribes audio files that are recorded from the microphone. ...

Example:
```python
from gradio_client import Client

client = Client("abidlabs/whisper")
client.predict("audio_sample.wav")

>> "This is a test of the whisper speech recognition model."
```

Sections: Basic Usage, Connecting to a Space or a Gradio app, Inspecting the API endpoints, Making a prediction, Advanced Usage

</details>

### imbalanced-learn

Toolbox for imbalanced dataset in machine learning

`pip install imbalanced-learn` · installs (wheel) · licence: MIT License · rank 1662 · last release 2026-06-07 · [PyPI](https://pypi.org/project/imbalanced-learn/) · [source](https://github.com/scikit-learn-contrib/imbalanced-learn)

<details><summary>README extract</summary>

imbalanced-learn is a python package offering a number of re-sampling techniques
commonly used in datasets showing strong between-class imbalance.
It is compatible with scikit-learn and is part of scikit-learn-contrib
projects.

Installation documentation, API documentation, and examples can be found on the
documentation.

Sections: imbalanced-learn, Documentation, Dependencies, Endorsement of the Scientific Python Specification, About

</details>

### biopython

Freely available tools for computational molecular biology.

`pip install biopython` · installs (wheel) · licence: LicenseRef-Biopython-License-Agreement · rank 1664 · last release 2026-08-12 · [PyPI](https://pypi.org/project/biopython/) · [docs](https://biopython.org/wiki/Documentation) · [source](https://github.com/biopython/biopython/)

<details><summary>README extract</summary>

The Biopython Project is an international association of developers of freely
available Python tools for computational molecular biology.

This README file is intended primarily for people interested in working
with the Biopython source code, either one of the releases from the
 website, or from our repository on GitHub ...

Sections: Biopython README file, For the impatient, Python Requirements, Optional Dependencies, Experimental code, Bugs, Distribution Structure

</details>

### arxiv

Python wrapper for the arXiv API

`pip install arxiv` · installs (wheel) · licence: MIT · rank 1751 · last release 2026-10-26 · [PyPI](https://pypi.org/project/arxiv/) · [docs](https://lukasschwab.me/arxiv.py/) · [source](https://github.com/lukasschwab/arxiv.py)

<details><summary>README extract</summary>

Python wrapper for the arXiv API.

arXiv is a project by the Cornell University Library that provides open access to 1,000,000+ articles in Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, and Statistics.

Example:
```python
import arxiv
```

Sections: arxiv.py, Usage, Examples, Fetching results, Fetching results with a custom client, Downloading a paper, Logging, Types, Client, Search, Result

</details>

### mujoco

MuJoCo Physics Simulator

`pip install mujoco` · installs (wheel) · licence: Apache-2.0 · rank 1785 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mujoco/) · [docs](https://mujoco.readthedocs.io/en/4.0.0) · [source](https://github.com/google-deepmind/mujoco)

<details><summary>README extract</summary>

[][pypi]
[][pypi]

This package is the canonical Python distribution for the
MuJoCo physics engine.
These bindings are developed and maintained by Google DeepMind, and are kept
up-to-date with the latest developments in MuJoCo itself.

Installing `mujoco` installs: ...

Example:
```python
Eigen is primarily MPL2 licensed. See COPYING.MPL2 and these links:

Some files contain third-party code under BSD or LGPL licenses, whence the other
COPYING.* files here.

All the LGPL code is either LGPL 2.1-only, or LGPL 2.1-or-later.
For this reason, the COPYING.LGPL file contains the LGPL 2.1 text.

...
```

Sections: MuJoCo Python Bindings, Usage, Versioning, Abseil C++ Common Libraries, cereal, Collisions, Eigen, {fmt}, GLAD, GLFW, libccd, LodePNG, MarchingCubeCpp, OpenGL Mathematics

</details>

### nvidia-nvshmem-cu12

NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.

`pip install nvidia-nvshmem-cu12` · installs (wheel) · licence: not stated · rank 1827 · last release 2026-09-22 · [PyPI](https://pypi.org/project/nvidia-nvshmem-cu12/)

<details><summary>README extract</summary>

NVSHMEM is a parallel programming interface based on OpenSHMEM that provides efficient and scalable communication for NVIDIA GPU clusters. NVSHMEM creates a global address space for data that spans the memory of multiple GPUs and can be accessed with fine-grained GPU-initiated operations, CPU-initiated operations, and operations on CUDA streams.

</details>

### donfig

Python package for configuring a python package

`pip install donfig` · installs (wheel) · licence: MIT License · rank 1836 · last release 2024-05-23 · [PyPI](https://pypi.org/project/donfig/)

<details><summary>README extract</summary>

Donfig is a python library meant to make configuration easier for other
python packages. Donfig can be configured programmatically, by
environment variables, or from YAML files in standard locations. The
below examples show the basics of using donfig. For more details see the
official documentation.

Example:
```python
# mypkg/init.py
from donfig import Config
config = Config('mypkg')
```

Sections: Donfig, Using Donfig, Set configuration in Python, Configure from environment variables, Configure from YAML file

</details>

### distributed

Distributed scheduler for Dask

`pip install distributed` · installs (wheel) · licence: BSD-3-Clause · rank 1865 · last release 2026-08-24 · [PyPI](https://pypi.org/project/distributed/) · [source](https://github.com/dask/distributed)

<details><summary>README extract</summary>

|Longitudinal Report (full)Longitudinal Report (short)CoverageDoc StatusDiscourseVersion StatusNumFOCUS|

A library for distributed computation. See documentation for more details.

</details>

### ultralytics

Ultralytics YOLO 🚀 for SOTA object detection, instance segmentation, semantic segmentation, depth estimation, classification, pose estimation, oriented object detection, and multi-object tracking.

`pip install ultralytics` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 1876 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ultralytics/) · [docs](https://docs.ultralytics.com) · [source](https://github.com/ultralytics/ultralytics)

_README extract left out: share-alike licence._

### ultralytics-thop

Ultralytics THOP package for fast computation of PyTorch model FLOPs and parameters.

`pip install ultralytics-thop` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 1939 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ultralytics-thop/) · [docs](https://docs.ultralytics.com) · [source](https://github.com/ultralytics/thop)

_README extract left out: share-alike licence._

### cftime

Time-handling functionality from netcdf4-python

`pip install cftime` · installs (wheel) · licence: MIT · rank 1952 · last release 2026-10-14 · [PyPI](https://pypi.org/project/cftime/)

<details><summary>README extract</summary>

Time-handling functionality from netcdf4-python

For details on the latest updates, see the Changelog.

10/15/2026: Version 1.6.6.1 release. Includes free-threaded wheels.

9/15/2026: Version 1.6.6 release. Limited API compliant wheels (should work with python 3.15). New cftime calendar "tai".

10/13/2025: Version 1.6.5 release. ...

Sections: cftime, News, Quick Start, Documentation

</details>

### tensorflow-text

TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.

`pip install tensorflow-text` · does not install on CPython 3.14 · licence: Apache Software License · rank 1971 · last release 2026-09-08 · [PyPI](https://pypi.org/project/tensorflow-text/)

<details><summary>README extract</summary>

TF.Text is a TensorFlow library of text related ops, modules, and subgraphs. The
library can perform the preprocessing regularly required by text-based models,
and includes other features useful for sequence modeling not provided by core
TensorFlow.

See the README on GitHub for further documentation.

</details>

### pylance

python wrapper for Lance columnar format

`pip install pylance` · installs (wheel) · licence: Apache Software License · rank 1972 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pylance/)

<details><summary>README extract</summary>

Please read the contribution guide at the CONTRIBUTING.md page

</details>

### tensorflow-serving-api

TensorFlow Serving Python API.

`pip install tensorflow-serving-api` · installs (wheel) · licence: Apache Software License · rank 1980 · last release 2026-09-29 · [PyPI](https://pypi.org/project/tensorflow-serving-api/)

<details><summary>README extract</summary>

TensorFlow Serving is a flexible, high-performance serving system for machine
learning models, designed for production environments.TensorFlow Serving makes
it easy to deploy new algorithms and experiments, while keeping the same server
architecture and APIs. ...

</details>

### pysbd

pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.

`pip install pysbd` · installs (wheel) · licence: MIT License · rank 1994 · last release 2021-02-11 · [PyPI](https://pypi.org/project/pysbd/)

<details><summary>README extract</summary>

pySBD - python Sentence Boundary Disambiguation (SBD) - is a rule-based sentence boundary detection module that works out-of-the-box.

This project is a direct port of ruby gem - Pragmatic Segmenter which provides rule-based sentence boundary detection.

Features:
'PySBD: Pragmatic Sentence Boundary Disambiguation' a short research paper got accepted into 2nd Workshop for Natural Language Processing Open Source Software (NLP-OSS) at EMNLP 2020. </br>

Research Paper:</br>

Recorded Talk:</br>

</br> ...

Example:
```python
import pysbd
text = "My name is Jonas E. Smith. Please turn to p. 55."
seg = pysbd.Segmenter(language="en", clean=False)
print(seg.segment(text))
# ['My name is Jonas E. Smith.', 'Please turn to p. 55.']
```

...

</details>

### nvidia-cuda-cccl

CUDA CCCL

`pip install nvidia-cuda-cccl` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 2014 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-cccl/)

### optype

Building Blocks for Precise & Flexible Type Hints

`pip install optype` · installs (wheel) · licence: BSD-3-Clause · rank 2089 · last release 2026-10-02 · [PyPI](https://pypi.org/project/optype/) · [docs](https://jorenham.github.io/optype/) · [source](https://github.com/jorenham/optype/)

<details><summary>README extract</summary>

Building blocks for precise type hints

 GitHub
 Installation
 Getting Started
 API Reference
 Type Inference
 Changelog

 Stop fighting your type checker. Work with it.

 optype gives you single-method protocols for every dunder,
 exact types that reject sneaky subtypes, and typed operators that actually
 make sense, so you can express what your ...

</details>

### sacrebleu

Hassle-free computation of shareable, comparable, and reproducible BLEU, chrF, and TER scores

`pip install sacrebleu` · installs (wheel) · licence: Apache-2.0 · rank 2094 · last release 2026-01-12 · [PyPI](https://pypi.org/project/sacrebleu/) · [source](https://github.com/mjpost/sacrebleu)

<details><summary>README extract</summary>

SacreBLEU (Post, 2018) provides hassle-free computation of shareable, comparable, and reproducible BLEU scores.
Inspired by Rico Sennrich's `multi-bleu-detok.perl`, it produces the official WMT scores but works with plain text.
It also knows all the standard test sets and handles downloading, processing, and tokenization for you. ...

Features:
- It automatically downloads common WMT test sets and processes them to plain text
- It produces a short version string that facilitates cross-paper comparisons ...

Example:
```python
In [1]: from sacrebleu.metrics import BLEU, CHRF, TER
   ...:
   ...: refs = [ # First set of references
   ...:          ['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.'],
   ...:          # Second set of references
...

</details>

### hijridate

Accurate Hijri-Gregorian dates converter based on Umm al-Qura calendar

`pip install hijridate` · installs (wheel) · licence: MIT · rank 2137 · last release 2026-01-06 · [PyPI](https://pypi.org/project/hijridate/) · [source](https://github.com/dralshehri/hijridate)

<details><summary>README extract</summary>

> formerly `hijri-converter`

A Python package for accurate Hijri-Gregorian date conversion using the Umm al-Qura calendar.

HijriDate provides reliable date conversion based on official sources, including archived Umm al-Qura newspaper publications and comparative calendar data from King Abdulaziz City for Science and Technology (KACST). ...

Example:
```python
from hijridate import Hijri, Gregorian

# Convert a Hijri date to Gregorian
hijri_date = Hijri(1445, 6, 15)
gregorian_date = hijri_date.to_gregorian()
print(gregorian_date)  # 2023-12-28

# Convert a Gregorian date to Hijri
gregorian_date = Gregorian(2023, 12, 28)
hijri_date = gregorian_date.to_hijri()
print(hijri_date)  # 1445-06-15
```

Sections: HijriDate, ✨ Features, ⚠️ Limitations, 🚀 Basic Usage, 📚 Documentation

</details>

### formulas

Parse and compile Excel formulas and workbooks in python code.

`pip install formulas` · installs (wheel) · licence: European Union Public Licence 1.1 (EUPL 1.1) · rank 2154 · last release 2026-03-11 · [PyPI](https://pypi.org/project/formulas/) · [docs](http://formulas.readthedocs.io)

_README extract left out: share-alike licence._

### schedula

Produce a plan that dispatches calls based on a graph of functions, satisfying data dependencies.

`pip install schedula` · installs (wheel) · licence: European Union Public Licence 1.1 (EUPL 1.1) · rank 2156 · last release 2026-03-04 · [PyPI](https://pypi.org/project/schedula/) · [docs](https://schedula.readthedocs.io)

_README extract left out: share-alike licence._

### rembg

Remove image background

`pip install rembg` · installs (wheel) · licence: MIT License · rank 2168 · last release 2026-11-06 · [PyPI](https://pypi.org/project/rembg/) · [source](https://github.com/danielgatis/rembg)

<details><summary>README extract</summary>

Rembg is a tool to remove image backgrounds. It can be used as a CLI, Python library, HTTP server, or Docker container.

Example:
```python
from rembg import remove

with open('input.png', 'rb') as i:
    with open('output.png', 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
```

Sections: Requirements, Usage as a CLI, rembg `i`, rembg `p`, rembg `s`, rembg `b`, Usage as a Library, Choosing an edge mode, Which model to pair it with, Color decontamination, Usage with Docker, CPU Only, NVIDIA CUDA GPU Acceleration, Models

</details>

### igraph

High performance graph data structures and algorithms

`pip install igraph` · installs (wheel) · licence: GNU General Public License (GPL) · rank 2170 · last release 2025-10-23 · [PyPI](https://pypi.org/project/igraph/) · [docs](https://python.igraph.org) · [source](https://github.com/igraph/python-igraph)

_README extract left out: share-alike licence._

### autograd

Efficiently computes derivatives of NumPy code.

`pip install autograd` · installs (wheel) · licence: MIT · rank 2180 · last release 2026-07-02 · [PyPI](https://pypi.org/project/autograd/) · [source](https://github.com/HIPS/autograd)

<details><summary>README extract</summary>

Autograd can automatically differentiate native Python and Numpy code. It can
handle a large subset of Python's features, including loops, ifs, recursion and
closures, and it can even take derivatives of derivatives of derivatives. It
supports reverse-mode differentiation (a.k.a. ...

Example:
```python
>>> import autograd.numpy as np  # Thinly-wrapped numpy
>>> from autograd import grad    # The only autograd function you may ever need
>>>
>>> def tanh(x):                 # Define a function
...     return (1.0 - np.exp((-2 * x))) / (1.0 + np.exp(-(2 * x)))
...
>>> grad_tanh = grad(tanh)       # Obtain its gradient function
...
```

Sections: Autograd [][checks-url] [][tests-url] [][publish-url] [](#), Documentation, End-to-end examples

</details>

### tensorflow-io-gcs-filesystem

TensorFlow IO

`pip install tensorflow-io-gcs-filesystem` · does not install on CPython 3.14 · licence: Apache Software License · rank 2259 · last release 2024-07-01 · [PyPI](https://pypi.org/project/tensorflow-io-gcs-filesystem/) · [docs](https://tensorflow.org/io) · [source](https://github.com/tensorflow/io)

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

### casadi

CasADi -- framework for algorithmic differentiation and numeric optimization

`pip install casadi` · installs (wheel) · licence: OSI Approved · rank 2344 · last release 2026-10-27 · [PyPI](https://pypi.org/project/casadi/) · [docs](http://docs.casadi.org) · [source](https://github.com/casadi/casadi)

<details><summary>README extract</summary>

CasADi is a symbolic framework for numeric optimization implementing automatic differentiation in forward and reverse modes on sparse matrix-valued computational graphs. It supports self-contained C-code generation and interfaces state-of-the-art codes such as SUNDIALS, IPOPT etc. It can be used from C++, Python or Matlab/Octave. ...

</details>

### h5netcdf

netCDF4 via h5py

`pip install h5netcdf` · installs (wheel) · licence: BSD License · rank 2398 · last release 2026-10-27 · [PyPI](https://pypi.org/project/h5netcdf/) · [docs](https://h5netcdf.org) · [source](https://github.com/h5netcdf/h5netcdf)

<details><summary>README extract</summary>

h5netcdf is an open source project and Python package that provides an
interface for the netCDF4 file-format that reads and writes local or
remote HDF5 files directly via h5py or h5pyd, without relying on the Unidata
netCDF library. See Pyfive support for a pure Python HDF5 reading chain.

Features:
- It has one less binary dependency (netCDF C). If you already have h5py
 installed, reading netCDF4 with h5netcdf may be much easier than installing
 netCDF4-Python. ...

Example:
```python
import h5netcdf
import numpy as np

with h5netcdf.File("mydata.nc", "w") as f:
    # set dimensions with a dictionary
    f.dimensions = {"x": 5}
    # and update them with a dict-like interface
    # f.dimensions['x'] = 5
    # f.dimensions.update({'x': 5})

...

</details>

### oras

OCI Registry as Storage Python SDK

`pip install oras` · installs (wheel) · licence: Apache Software License · rank 2469 · last release 2026-08-08 · [PyPI](https://pypi.org/project/oras/)

<details><summary>README extract</summary>

OCI Registry as Storage enables libraries to push OCI Artifacts to OCI Conformant registries. This is a Python SDK for Python developers to empower them to do this in their applications.

See our ⭐️ Documentation ⭐️ to get started.

</details>

### nvidia-nvvm

NVVM Libraries

`pip install nvidia-nvvm` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 2480 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-nvvm/)

### nvidia-cuda-nvcc

CUDA nvcc

`pip install nvidia-cuda-nvcc` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 2489 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-nvcc/)

### nvidia-cuda-crt

CUDA C Runtime

`pip install nvidia-cuda-crt` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 2493 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-crt/)

### azure-cognitiveservices-speech

Microsoft Cognitive Services Speech SDK for Python

`pip install azure-cognitiveservices-speech` · installs (wheel) · licence: Other/Proprietary License · rank 2557 · last release 2026-10-21 · [PyPI](https://pypi.org/project/azure-cognitiveservices-speech/)

<details><summary>README extract</summary>

For an introduction to this package, have a look at `the quickstart
article <

For information about the Speech Service, please refer to `its
website <

Documentation

API documentation for this package can be found `here <

License information

- `Microsoft Software License Terms for the Speech SDK <
- `Third party notices <

</details>

### loky

A robust implementation of concurrent.futures.ProcessPoolExecutor

`pip install loky` · installs (wheel) · licence: BSD License · rank 2572 · last release 2026-09-29 · [PyPI](https://pypi.org/project/loky/) · [source](https://github.com/joblib/loky)

<details><summary>README extract</summary>

The aim of this project is to provide a robust, cross-platform and
cross-version implementation of the `ProcessPoolExecutor` class of
`concurrent.futures`. It notably features:

 * Consistent and robust spawn behavior: All processes are started
 using fork + exec on POSIX systems. This ensures safer interactions with
 third party libraries. ...

Features:
While developing `loky`, we had some bad experiences trying to debug deadlocks
when using `multiprocessing.Pool` and `concurrent.futures.ProcessPoolExecutor`,
especially when calling functions with non-picklable arguments or returned
values at the ...

Example:
```python
import os
from time import sleep
from loky import get_reusable_executor

def say_hello(k):
    pid = os.getpid()
    print(f"Hello from {pid} with arg {k}")
...

</details>

### nlopt

Library for nonlinear optimization, wrapping many algorithms for global and local, constrained or unconstrained, optimization

`pip install nlopt` · installs (wheel) · licence: MIT License · rank 2589 · last release 2026-07-17 · [PyPI](https://pypi.org/project/nlopt/) · [docs](https://nlopt.readthedocs.io/en/latest/) · [source](https://github.com/DanielBok/nlopt-python)

<details><summary>README extract</summary>

This project builds Python wheels for the NLopt library. NLopt contains various routines for non-linear optimization.

Sections: NLopt Python, Documentation

</details>

### mediapipe

MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web. See the privacy notice at https://goo.gle/mediapipe-privacy.

`pip install mediapipe` · installs (wheel) · licence: Apache Software License · rank 2623 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mediapipe/)

<details><summary>README extract</summary>

layout: forward
target:
title: Home
nav_order: 1

Attention: *See
for the primary developer documentation site for MediaPipe.*

On-device machine learning for everyone

Delight your customers with innovative machine learning features. ...

Sections: Get started, Solutions, Framework, Privacy Notice, Publications

</details>

### albumentations

Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.

`pip install albumentations` · installs (wheel) · licence: MIT License · rank 2632 · last release 2025-05-27 · [PyPI](https://pypi.org/project/albumentations/)

<details><summary>README extract</summary>

> 📣 Stay updated! Subscribe to our newsletter for the latest releases, tutorials, and tips directly from the Albumentations team.

Docs | Discord | Twitter | LinkedIn

Albumentations is a Python library for image augmentation. Image augmentation is used in deep learning and computer vision tasks to increase the quality of trained models. ...

Features:
- Complete Computer Vision Support: Works with all major CV tasks including classification, segmentation (semantic & instance), object detection, and pose estimation. ...

Example:
```python
import albumentations as A
import cv2

# Declare an augmentation pipeline
transform = A.Compose([
    A.RandomCrop(width=256, height=256),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])

...

</details>

### onnxruntime-gpu

ONNX Runtime is a runtime accelerator for Machine Learning models

`pip install onnxruntime-gpu` · installs (wheel) · licence: MIT License · rank 2634 · last release 2026-10-26 · [PyPI](https://pypi.org/project/onnxruntime-gpu/)

<details><summary>README extract</summary>

ONNX Runtime is a performance-focused scoring engine for Open Neural Network Exchange (ONNX) models.
For more information on ONNX Runtime, please see aka.ms/onnxruntime or the Github project.

Release Notes :

Sections: ONNX Runtime, Changes, 1.31.1, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.1, 1.23.0, 1.22.0, 1.21.0

</details>

### wslink

Python/JavaScript library for communicating over WebSocket

`pip install wslink` · installs (wheel) · licence: BSD License · rank 2668 · last release 2026-10-08 · [PyPI](https://pypi.org/project/wslink/)

<details><summary>README extract</summary>

Wslink allows easy, bi-directional communication between a python server and a
javascript or C++ client over a [websocket]. The client can make remote
procedure calls (RPC) to the server, and the server can publish messages to
topics that the client can subscribe to. ...

Sections: Usage for RPC and publish/subscribe, Examples, Commit message convention

</details>

### trame-common

Dependency less classes and functions for trame

`pip install trame-common` · installs (wheel) · licence: Apache Software License · rank 2674 · last release 2026-10-08 · [PyPI](https://pypi.org/project/trame-common/)

<details><summary>README extract</summary>

Trame is rapidly evolving and having a dependency-less package to provide helper
functions and classes across trame's eco-system is important for its future
health. Initially some of those classes were created inside trame-client,
trame-server or even trame, but we reached a point where some of those
should become even more mainstream so they ...

Sections: trame-common: common code for any trame package, Content

</details>

### hdbscan

Clustering based on density with variable density clusters

`pip install hdbscan` · installs (wheel) · licence: OSI Approved · rank 2709 · last release 2026-06-01 · [PyPI](https://pypi.org/project/hdbscan/)

<details><summary>README extract</summary>

HDBSCAN - Hierarchical Density-Based Spatial Clustering of Applications
with Noise. Performs DBSCAN over varying epsilon values and integrates
the result to find a clustering that gives the best stability over epsilon.
This allows HDBSCAN to find clusters of varying densities (unlike DBSCAN),
and be more robust to parameter selection. ...

Example:
```python
import hdbscan
from sklearn.datasets import make_blobs

data, _ = make_blobs(1000)

clusterer = hdbscan.HDBSCAN(min_cluster_size=10)
cluster_labels = clusterer.fit_predict(data)
```

Sections: HDBSCAN, How to use HDBSCAN, Performance, Additional functionality, Outlier Detection, Robust single linkage, Branch detection, Running the Tests, Python Version, Citing, Licensing

</details>

### CoolProp

Open-source thermodynamic and transport properties database

`pip install CoolProp` · installs (wheel) · licence: MIT License · rank 2744 · last release 2026-06-27 · [PyPI](https://pypi.org/project/CoolProp/) · [docs](http://www.coolprop.org) · [source](https://github.com/CoolProp/CoolProp)

<details><summary>README extract</summary>

CoolProp is a thermophysical property database and wrappers for a selection of programming environments.
It offers similar functionality to REFPROP, but CoolProp is open-source and free.
It was originally developed by Ian Bell, at the time a post-doc at the University of Liege, in Liege, Belgium. ...

</details>

### nvidia-cuda-nvdisasm

CUDA nvdisasm

`pip install nvidia-cuda-nvdisasm` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 2747 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-nvdisasm/)

<details><summary>README extract</summary>

nvdisasm extracts information from standalone cubin files and presents them in human readable format. It accepts cubin files as input and outputs CUDA assembly code.

</details>

### kornia-rs

Low level implementations for computer vision in Rust

`pip install kornia-rs` · installs (wheel) · licence: Apache Software License · rank 2748 · last release 2026-09-26 · [PyPI](https://pypi.org/project/kornia-rs/) · [docs](https://kornia.readthedocs.io) · [source](https://github.com/kornia/kornia-rs)

<details><summary>README extract</summary>

English | 简体中文

The `kornia` crate is a low-level computer vision library for Rust 🦀

Fast, thread-safe image I/O and processing with a single API that runs on the CPU or an NVIDIA GPU — the same `Image` and operators dispatch on where the data lives. ...

Features:
- 🦀 Written in Rust: memory- and thread-safe, no GIL — usable from the free-threaded Python build.
- ⚡ Fast image I/O and processing: libjpeg-turbo decoding and SIMD (NEON/AVX2) kernels. ...

Example:
```python
import kornia_rs as K
import numpy as np
import torch

# load a JPEG with libjpeg-turbo
img: np.ndarray = K.io.read_image_jpeg("dog.jpeg", "rgb")

# or read any supported format
# img: np.ndarray = K.io.read_image("dog.png")

assert img.shape == (195, 258, 3)

# convert to dlpack to import to torch
...

</details>

### ml-collections

ML Collections is a library of Python collections designed for ML usecases.

`pip install ml-collections` · installs (wheel) · licence: Apache Software License · rank 2767 · last release 2025-04-17 · [PyPI](https://pypi.org/project/ml-collections/) · [docs](https://ml-collections.readthedocs.io) · [source](https://github.com/google/ml_collections)

<details><summary>README extract</summary>

ML Collections is a library of Python Collections designed for ML use cases.

The two classes called `ConfigDict` and `FrozenConfigDict` are "dict-like" data
structures with dot access to nested elements. Together, they are supposed to be
used as a main way of expressing configurations of experiments and models. ...

Features:
* Dot-based access to fields.
* Locking mechanism to prevent spelling mistakes.
* Lazy computation.
* FrozenConfigDict() class which is immutable and hashable.
* Type safety.
* "Did you mean" functionality. ...

Example:
```python
from ml_collections import config_dict

cfg = config_dict.ConfigDict()
cfg.float_field = 12.6
cfg.integer_field = 123
cfg.another_integer_field = 234
cfg.nested = config_dict.ConfigDict()
cfg.nested.string_field = 'tom'

...

</details>

### silero-vad

Voice Activity Detector (VAD) by Silero

`pip install silero-vad` · installs (wheel) · licence: MIT License · rank 2826 · last release 2026-09-23 · [PyPI](https://pypi.org/project/silero-vad/)

<details><summary>README extract</summary>

Silero VAD - pre-trained enterprise-grade Voice Activity Detector (also see our STT models).

Real Time Example

Please note, that video loads only if you are logged in your GitHub account.

Dependencies

 System requirements to run python examples on `x86-64` systems: ...

Features:
- Stellar accuracy

 Silero VAD has excellent results on speech detection tasks.

- Fast

 One audio chunk (30+ ms) takes less than 1ms to be processed on a single CPU thread. Using batching or GPU can also improve performance considerably. ...

Example:
```python
from silero_vad import load_silero_vad, read_audio, get_speech_timestamps
model = load_silero_vad()
wav = read_audio('path_to_audio_file')
speech_timestamps = get_speech_timestamps(
  wav,
  model,
...

</details>

### filterpy

Kalman filtering and optimal estimation library

`pip install filterpy` · installs (wheel) · licence: MIT License · rank 2839 · last release 2026-10-26 · [PyPI](https://pypi.org/project/filterpy/)

<details><summary>README extract</summary>

NOTE: Imminent drop of support of Python 2.7, 3.4. See section below for details.

This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. ...

Example:
```python
import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
```

Sections: Basic use, Requirements, References

</details>

### fasttext

fasttext Python bindings

`pip install fasttext` · installs from source (sdist only) · licence: MIT License · rank 2849 · last release 2024-06-12 · [PyPI](https://pypi.org/project/fasttext/)

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

### open-clip-torch

Open reproduction of contrastive language-image pretraining (CLIP) and related.

`pip install open-clip-torch` · installs (wheel) · licence: MIT License · rank 2942 · last release 2026-11-06 · [PyPI](https://pypi.org/project/open-clip-torch/) · [source](https://github.com/mlfoundations/open_clip)

<details><summary>README extract</summary>

[[Paper]]( [[Citations]](#citing) [[Clip Colab]]( [[Coca Colab]](

> Versions
> - 4.x is the current release line, developed on `main`. 4.2.1 is the first 4.x release on PyPI; earlier 4.x version numbers were development versions only.
> - 3.x remains available on the `v3` branch. To stay on it, run `pip install 'open_clip_torch<4'`. ...

Example:
```python
import torch
from PIL import Image
import open_clip

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
model.eval()  # model in train mode by default, impacts some models with BatchNorm or stochastic depth active
tokenizer = open_clip.get_tokenizer('ViT-B-32')

...
```

...

</details>

### opencv-contrib-python-headless

Wrapper package for OpenCV python bindings.

`pip install opencv-contrib-python-headless` · installs (wheel) · licence: Apache Software License · rank 2965 · last release 2026-07-02 · [PyPI](https://pypi.org/project/opencv-contrib-python-headless/)

<details><summary>README extract</summary>

OpenCV is raising funds to keep the library free for everyone, and we need the support of the entire community to do it. Donate to OpenCV on Github to show your support.

- OpenCV on Wheels
 - Installation and Usage
- Frequently Asked Questions ...

Sections: Keep OpenCV Free, OpenCV on Wheels, Documentation for opencv-python, CI build process, Manual builds, Manual debug builds, Source distributions, Licensing, Versioning, Manylinux wheels, Backward compatibility

</details>

### fasttext-wheel

fasttext Python bindings

`pip install fasttext-wheel` · installs from source (sdist only) · licence: MIT License · rank 3047 · last release 2024-02-17 · [PyPI](https://pypi.org/project/fasttext-wheel/)

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

### tf-keras

Deep learning for humans.

`pip install tf-keras` · installs (wheel) · licence: Apache Software License · rank 3063 · last release 2026-03-18 · [PyPI](https://pypi.org/project/tf-keras/)

<details><summary>README extract</summary>

TF-Keras is a deep learning API written in Python,
running on top of the machine learning platform TensorFlow.

It was developed with a focus on enabling fast experimentation and
providing a delightful developer experience.
The purpose of TF-Keras is to give an *unfair advantage* to any developer
looking to ship ML-powered apps.

</details>

### portion

Python data structure and operations for intervals

`pip install portion` · installs (wheel) · licence: LGPL-3.0-or-later · rank 3143 · last release 2026-09-29 · [PyPI](https://pypi.org/project/portion/) · [docs](https://github.com/AlexandreDecan/portion/blob/master/README.md) · [source](https://github.com/AlexandreDecan/portion)

_README extract left out: share-alike licence._

### lifelines

Survival analysis in Python, including Kaplan Meier, Nelson Aalen and regression

`pip install lifelines` · installs (wheel) · licence: MIT License · rank 3144 · last release 2026-03-05 · [PyPI](https://pypi.org/project/lifelines/)

<details><summary>README extract</summary>

What is survival analysis and why should I learn it?
 Survival analysis was originally developed and applied heavily by the actuarial and medical community. Its purpose was to answer *why do events occur now versus later* under uncertainty (where *events* might refer to deaths, disease remission, etc.). ...

Sections: Documentation and intro to survival analysis, Contact

</details>

### autograd-gamma

Autograd compatible approximations to the gamma family of functions

`pip install autograd-gamma` · installs from source (sdist only) · licence: MIT License · rank 3177 · last release 2020-10-15 · [PyPI](https://pypi.org/project/autograd-gamma/)

<details><summary>README extract</summary>

autograd compatible approximations to the derivatives of the Gamma-family of functions.

Example:
```python
from autograd import grad
from autograd_gamma import gammainc, gammaincc, gammaincln, gammainccln

grad(gammainc, argnum=0)(1., 2.)
grad(gammaincc, argnum=0)(1., 2.)

# logarithmic functions too.
grad(gammaincln, argnum=0)(1., 2.)
grad(gammainccln, argnum=0)(1., 2.)

from autograd_gamma import betainc, betaincln

...
```

Sections: autograd-gamma, Tutorial, Long-term goal

</details>

### warp-lang

A Python framework for high-performance simulation and graphics programming

`pip install warp-lang` · installs (wheel) · licence: Apache-2.0 · rank 3187 · last release 2026-11-02 · [PyPI](https://pypi.org/project/warp-lang/) · [docs](https://nvidia.github.io/warp/stable/) · [source](https://github.com/NVIDIA/warp)

<details><summary>README extract</summary>

Documentation | Changelog

Warp is a Python framework for GPU-accelerated simulation, robotics, and machine learning. Warp takes
regular Python functions and JIT compiles them to efficient kernel code that can run on the CPU or GPU.

Warp comes with a rich set of primitives for physics simulation, robotics, geometry processing,
and more. ...

Example:
```python
import warp as wp
import numpy as np

num_particles = 1_000_000
dt = 0.01

@wp.kernel
def gravity_step(pos: wp.array[wp.vec3], vel: wp.array[wp.vec3]):
    i = wp.tid()
    position = pos[i]
    dist_sq = wp.length_sq(position) + 0.01  # softened distance
    acc = -1000.0 / dist_sq * wp.normalize(position)  # gravitational pull toward origin
...
```

...

</details>

### nibabel

Access a multitude of neuroimaging data formats

`pip install nibabel` · installs (wheel) · licence: MIT · rank 3222 · last release 2026-03-11 · [PyPI](https://pypi.org/project/nibabel/)

<details><summary>README extract</summary>

Read and write access to common neuroimaging file formats, including:
ANALYZE (plain, SPM99, SPM2 and later), GIFTI, NIfTI1, NIfTI2, CIFTI-2,
MINC1, MINC2, AFNI BRIK/HEAD, ECAT and Philips PAR/REC.
In addition, NiBabel also supports FreeSurfer's MGH, geometry, annotation and
morphometry files, and provides some limited support for DICOM. ...

</details>

### meshio

I/O for many mesh formats

`pip install meshio` · installs (wheel) · licence: MIT License · rank 3279 · last release 2024-01-31 · [PyPI](https://pypi.org/project/meshio/) · [source](https://github.com/nschloe/meshio)

<details><summary>README extract</summary>

I/O for mesh files.

There are various mesh formats available for representing unstructured meshes.
meshio can read and write all of the following and smoothly converts between them: ...

Example:
```python
import meshio

mesh = meshio.read(
    filename,  # string, os.PathLike, or a buffer/open file
    # file_format="stl",  # optional if filename is a path; inferred from extension
    # see meshio-convert -h for all possible formats
)
# mesh.points, mesh.cells, mesh.cells_dict, ...

# mesh.vtk.read() is also possible
```

Sections: Time series, ParaView plugin, Performance comparison, File sizes, I/O speed, Maximum memory usage

</details>

### hyperopt

Distributed Asynchronous Hyperparameter Optimization

`pip install hyperopt` · installs (wheel) · licence: BSD-3-Clause · rank 3280 · last release 2026-07-24 · [PyPI](https://pypi.org/project/hyperopt/) · [source](https://github.com/hyperopt/hyperopt)

<details><summary>README extract</summary>

Hyperopt is a Python library for serial and parallel optimization over awkward
search spaces, which may include real-valued, discrete, and conditional
dimensions.

Example:
```python
# define an objective function
def objective(args):
    case, val = args
    if case == 'case 1':
        return val
    else:
        return val ** 2

# define a search space
from hyperopt import hp
space = hp.choice('a',
    [
        ('case 1', 1 + hp.lognormal('c1', 0, 1)),
        ('case 2', hp.uniform('c2', -10, 10))
    ])

...
```

Sections: Hyperopt: Distributed Hyperparameter Optimization, Getting started, Setup (based on this), Algorithms, Documentation, Related Projects, Examples, Announcements mailing list, Discussion mailing list, Thanks

</details>

### alphashape

Toolbox for generating alpha shapes.

`pip install alphashape` · installs (wheel) · licence: MIT License · rank 3288 · last release 2021-04-16 · [PyPI](https://pypi.org/project/alphashape/)

<details><summary>README extract</summary>

Toolbox for generating n-dimensional alpha shapes.

Alpha shapes are often used to generalize bounding polygons containing sets of points. The alpha parameter is defined as the value `a`, such that an edge of a disk of radius 1/`a` can be drawn between any two edge members of a set of points and still contain all the points. ...

Example:
```python
import os
import sys
import pandas as pd
import numpy as np
from descartes import PolygonPatch
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.getcwd()))
import alphashape
```

...

</details>

### cma

CMA-ES, Covariance Matrix Adaptation Evolution Strategy for non-linear numerical optimization in Python

`pip install cma` · installs (wheel) · licence: BSD-3-Clause · rank 3294 · last release 2026-09-13 · [PyPI](https://pypi.org/project/cma/) · [source](https://github.com/CMA-ES/pycma.git)

<details><summary>README extract</summary>

The CMA-ES is a randomized derivative-free numerical optimization algorithm for
difficult (non-convex, ill-conditioned, multi-modal, rugged, noisy) optimization
problems in continuous or mixed-integer search spaces, implemented in Python.

The typical domain of application are objective functions with: ...

Example:
```python
>>> import cma
>>> help(cma)
    <output omitted>
>>> es = cma.CMAEvolutionStrategy(8 * [0], 0.5)
(5_w,10)-aCMA-ES (mu_w=3.2,w_1=45%) in dimension 8 (seed=468976, Tue May  6 19:14:06 2014)
>>> help(es)  # the same as help(cma.CMAEvolutionStrategy)
    <output omitted>
>>> es.optimize(cma.ff.rosen)
...
```

Sections: CMA-ES Covariance Matrix Adaptation Evolution Strategy, Usage Example, Documentations, Dependencies

</details>

### wbdata

A library to access World Bank data

`pip install wbdata` · installs (wheel) · licence: GPL-2.0+ · rank 3343 · last release 2025-10-05 · [PyPI](https://pypi.org/project/wbdata/) · [docs](https://wbdata.readthedocs.io/) · [source](https://github.com/OliverSherouse/wbdata)

_README extract left out: share-alike licence._

### fasttext-predict

fasttext with wheels and no external dependency, but only the predict method (<1MB)

`pip install fasttext-predict` · installs from source (sdist only) · licence: MIT License · rank 3360 · last release 2024-11-23 · [PyPI](https://pypi.org/project/fasttext-predict/)

<details><summary>README extract</summary>

Python package for
fasttext:

- keep only the `predict` method, all other features are removed
- standalone package without external dependency (numpy is not a
 dependency)
- wheels for various architectures using GitHub workflows. The script
 is inspired by lxml build scripts.

Example:
```python
import fasttext
model = fasttext.load_model('lid.176.ftz')
result = model.predict('Fondant au chocolat et tarte aux myrtilles')
```

Sections: fasttext-predict, Usage

</details>

### pyreadstat

Reads and Writes SAS, SPSS and Stata files into/from pandas and polars data frames.

`pip install pyreadstat` · installs (wheel) · licence: Apache-2.0 · rank 3367 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pyreadstat/)

<details><summary>README extract</summary>

A Python package to read and write SAS
(sas7bdat, sas7bcat, xport/xpt), SPSS (sav, zsav, por) and Stata (dta) files into/from pandas and polars data frames. It is a wrapper
around the C library readstat.

Please visit out project home page for more information:

</details>

### pmdarima

Python's forecast::auto.arima equivalent

`pip install pmdarima` · installs (wheel) · licence: MIT · rank 3368 · last release 2025-11-17 · [PyPI](https://pypi.org/project/pmdarima/) · [docs](http://alkaline-ml.com/pmdarima) · [source](https://github.com/alkaline-ml/pmdarima)

<details><summary>README extract</summary>

Pmdarima (originally `pyramid-arima`, for the anagram of 'py' + 'arima') is a statistical
library designed to fill the void in Python's time series analysis capabilities. This includes: ...

Example:
```python
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Load/split your data
y = pm.datasets.load_wineind()
train, test = train_test_split(y, train_size=150)

# Fit your model
model = pm.auto_arima(train, seasonal=True, m=12)

# make your forecasts
...
```

Sections: pmdarima, pip, conda, Quickstart Examples, Availability, Documentation

</details>

### graphframes

GraphFrames: DataFrame-based Graphs

`pip install graphframes` · installs (wheel) · licence: MIT License · rank 3407 · last release 2018-12-05 · [PyPI](https://pypi.org/project/graphframes/)

<details><summary>README extract</summary>

This is a package for DataFrame-based graphs on top of Apache Spark. Users can write highly expressive queries by leveraging the DataFrame API, combined with a new API for motif finding. The user also benefits from DataFrame performance optimizations within the Spark SQL engine.

</details>

### pvlib

A set of functions and classes for simulating the performance of photovoltaic energy systems.

`pip install pvlib` · installs (wheel) · licence: BSD-3-Clause · rank 3410 · last release 2026-09-26 · [PyPI](https://pypi.org/project/pvlib/) · [docs](https://pvlib-python.readthedocs.io/) · [source](https://github.com/pvlib/pvlib-python)

<details><summary>README extract</summary>

pvlib python is a community developed toolbox that provides a set of
functions and classes for simulating the performance of photovoltaic
energy systems and accomplishing related tasks. The core mission of pvlib
python is to provide open, reliable, interoperable, and benchmark
implementations of PV system models. ...

</details>

### crccheck

Calculation library for CRCs and checksums

`pip install crccheck` · installs (wheel) · licence: MIT License · rank 3465 · last release 2025-07-10 · [PyPI](https://pypi.org/project/crccheck/)

<details><summary>README extract</summary>

The `crccheck.crc` module implements all CRCs listed in the
Catalogue of parametrised CRC algorithms:

 CRC-3/GSM, CRC-3/ROHC, CRC-4/G-704, CRC-4/INTERLAKEN, CRC-5/EPC-C1G2, CRC-5/G-704, CRC-5/USB, CRC-6/CDMA2000-A,
 CRC-6/CDMA2000-B, CRC-6/DARC, CRC-6/G-704, CRC-6/GSM, CRC-7/MMC, CRC-7/ROHC, CRC-7/UMTS, CRC-8/AUTOSAR,
 CRC-8/BLUETOOTH, ...

Example:
```python
from crccheck.crc import Crc32, CrcXmodem
from crccheck.checksum import Checksum32

# Quick calculation
data = bytearray.fromhex("DEADBEEF")
crc = Crc32.calc(data)
checksum = Checksum32.calc(data)

# Procsss multiple data buffers
data1 = b"Binary string"  # or use .encode(..) on normal sring - Python 3 only
...
```

</details>

### pysam

Package for reading, manipulating, and writing genomic data

`pip install pysam` · installs (wheel) · licence: MIT License · rank 3475 · last release 2026-09-07 · [PyPI](https://pypi.org/project/pysam/) · [docs](https://pysam.readthedocs.io/)

<details><summary>README extract</summary>

pysam --- a Python package for reading, manipulating, and writing
genomic data sets.

pysam is a lightweight wrapper of the HTSlib API and provides facilities
to read and write SAM/BAM/CRAM/VCF/BCF/BED/GFF/GTF/FASTA/FASTQ files
as well as access to the command-line functionality of samtools and bcftools. ...

</details>

### tensorflow-cpu

TensorFlow is an open source machine learning framework for everyone.

`pip install tensorflow-cpu` · does not install on CPython 3.14 · licence: Apache Software License · rank 3496 · last release 2026-03-06 · [PyPI](https://pypi.org/project/tensorflow-cpu/)

<details><summary>README extract</summary>

TensorFlow is an open source software library for high performance numerical
computation. Its flexible architecture allows easy deployment of computation
across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters
of servers to mobile and edge devices. ...

</details>

### awkward-cpp

CPU kernels and compiled extensions for Awkward Array

`pip install awkward-cpp` · installs (wheel) · licence: BSD-3-Clause AND MIT · rank 3522 · last release 2026-09-17 · [PyPI](https://pypi.org/project/awkward-cpp/) · [docs](https://awkward-array.org) · [source](https://github.com/scikit-hep/awkward-1.0)

<details><summary>README extract</summary>

`awkward-cpp` provides precompiled routines for the `awkward` package. It is not useful on its own, only as a dependency for `awkward `.

</details>

### awkward

Manipulate JSON-like data with NumPy-like idioms.

`pip install awkward` · installs (wheel) · licence: BSD-3-Clause · rank 3529 · last release 2026-09-17 · [PyPI](https://pypi.org/project/awkward/) · [docs](https://awkward-array.org) · [source](https://github.com/scikit-hep/awkward-1.0)

<details><summary>README extract</summary>

Awkward Array is a library for nested, variable-sized data, including arbitrary-length lists, records, mixed types, and missing data, using NumPy-like idioms.

Arrays are dynamically typed, but operations on them are compiled and fast. Their behavior coincides with NumPy when array dimensions are regular and generalizes when they're not.

Example:
```python
import awkward as ak

array = ak.Array([
    [{"x": 1.1, "y": [1]}, {"x": 2.2, "y": [1, 2]}, {"x": 3.3, "y": [1, 2, 3]}],
    [],
    [{"x": 4.4, "y": [1, 2, 3, 4]}, {"x": 5.5, "y": [1, 2, 3, 4, 5]}]
])
```

Sections: Motivating example, Getting help

</details>

### nvidia-cublas-cu11

CUBLAS native runtime libraries

`pip install nvidia-cublas-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 3539 · last release 2024-08-17 · [PyPI](https://pypi.org/project/nvidia-cublas-cu11/)

### cupy-cuda12x

CuPy: NumPy & SciPy for GPU

`pip install cupy-cuda12x` · installs (wheel) · licence: MIT · rank 3559 · last release 2026-08-20 · [PyPI](https://pypi.org/project/cupy-cuda12x/) · [docs](https://docs.cupy.dev/) · [source](https://github.com/cupy/cupy)

<details><summary>README extract</summary>

CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated computing with Python.

This is a CuPy wheel (precompiled binary) package for CUDA 12.x.
You need to install CUDA Toolkit 12.x locally to use these packages. ...

</details>

### param

Declarative parameters for robust Python classes and a rich API for reactive programming

`pip install param` · installs (wheel) · licence: BSD License · rank 3577 · last release 2026-09-03 · [PyPI](https://pypi.org/project/param/) · [source](https://github.com/holoviz/param)

<details><summary>README extract</summary>

Param is a zero-dependency Python library that provides two main features:

- Easily create classes with rich, declarative attributes - `Parameter` objects - that include extended metadata for various purposes such as runtime type and range validation, documentation strings, default values or factories, nullability, etc. ...

Example:
```python
import param

class UserForm(param.Parameterized):
    age = param.Integer(bounds=(0, None), doc='User age')
    name = param.String(doc='User name')
    submit = param.Event()

    @param.depends('submit', watch=True)
    def save_user_to_db(self):
        print(f'Saving user to db: name={self.name}, age={self.age}')
        ...

...
```

Sections: Param, Rich class attributes for runtime validation and more, Reactive Programming

</details>

### nvidia-cudnn-cu11

cuDNN runtime libraries

`pip install nvidia-cudnn-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 3599 · last release 2025-06-06 · [PyPI](https://pypi.org/project/nvidia-cudnn-cu11/)

<details><summary>README extract</summary>

cuDNN runtime libraries containing primitives for deep neural networks.

</details>

### measurement

Easily use and manipulate unit-aware measurements in Python.

`pip install measurement` · installs (wheel) · licence: MIT License · rank 3628 · last release 2023-01-10 · [PyPI](https://pypi.org/project/measurement/)

<details><summary>README extract</summary>

Easily use and manipulate unit-aware measurement objects in Python.

django.contrib.gis.measure
has these wonderful 'Distance' objects that can be used not only for storing a
unit-aware distance measurement, but also for converting between different
units and adding/subtracting these objects from one another. ...

Example:
```python
>>> from measurement.measures import Weight
>>> weight_1 = Weight(lb=125)
>>> weight_2 = Weight(kg=40)
>>> added_together = weight_1 + weight_2
>>> added_together
Weight(lb=213.184976807)
>>> added_together.kg  # Maybe I actually need this value in kg?
96.699
```

</details>

### scikit-base

Base classes for sklearn-like parametric objects

`pip install scikit-base` · installs (wheel) · licence: BSD License · rank 3631 · last release 2026-09-23 · [PyPI](https://pypi.org/project/scikit-base/) · [docs](https://github.com/sktime/skbase) · [source](https://github.com/sktime/skbase)

<details><summary>README extract</summary>

> A framework factory for scikit-learn-like and sktime-like parametric objects

`skbase` provides base classes for creating scikit-learn-like parametric objects,
along with tools to make it easier to build your own packages that follow these design patterns.

:rocket: Version 1.2.0 is now available. Check out our
release notes.

| Overview | | ...

Sections: Welcome to skbase, Documentation and Tutorials, pip

</details>

### nvidia-cuda-nvcc-cu12

CUDA nvcc

`pip install nvidia-cuda-nvcc-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 3674 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-cuda-nvcc-cu12/)

### coremltools

Community Tools for Core ML

`pip install coremltools` · installs from source (sdist only) · licence: BSD · rank 3679 · last release 2025-11-10 · [PyPI](https://pypi.org/project/coremltools/)

<details><summary>README extract</summary>

Core ML
is an Apple framework that allows developers to easily integrate
machine learning (ML) models into apps. Core ML is available on iOS, iPadOS,
watchOS, macOS, and tvOS. Core ML introduces a public file format (.mlmodel)
for a broad set of ML methods including deep neural networks (convolutional
and recurrent), tree ensembles (boosted trees, ...

Sections: coremltools, More Information

</details>

### country-converter

The country converter (coco) - a Python package for converting country names between different classifications schemes

`pip install country-converter` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 3747 · last release 2025-10-22 · [PyPI](https://pypi.org/project/country-converter/) · [source](https://github.com/IndEcol/country_converter)

_README extract left out: share-alike licence._

### pyvista-validation

Validate and standardize array-like input.

`pip install pyvista-validation` · installs (wheel) · licence: MIT · rank 3759 · last release 2026-09-27 · [PyPI](https://pypi.org/project/pyvista-validation/) · [docs](https://validation.pyvista.org/)

<details><summary>README extract</summary>

Validate and standardize array-like input.

These are the input validation functions developed for
PyVista, extracted into a standalone package so any
project can use them. NumPy is the only required dependency: PyVista is not needed, and
VTK and SciPy are optional. ...

Example:
```python
>>> import numpy as np
>>> from pyvista_validation import validate_array3
>>> from pyvista_validation import validate_arrayNx3
>>> from pyvista_validation import validate_data_range

>>> validate_array3([1, 2, 3])
array([1, 2, 3])

>>> validate_arrayNx3([[1, 2, 3], [4, 5, 6]])
array([[1, 2, 3],
       [4, 5, 6]])

>>> validate_data_range([0, 1])
...
```

...

</details>

### instanttensor

An ultra-fast, distributed Safetensors loader

`pip install instanttensor` · installs (wheel) · licence: not stated · rank 3787 · last release 2026-10-13 · [PyPI](https://pypi.org/project/instanttensor/)

<details><summary>README extract</summary>

InstantTensor is an ultra-fast, distributed Safetensors loader designed to maximize I/O throughput when moving model weights from Safetensors files to GPU memory.

| Model | GPU | Backend | Load Time (s) | Throughput (GB/s) | Speedup | ...

Features:
- Fast: Pipeline I/O, GPU transfers, and prefetching.
- Distributed: Coordinate reads across GPUs with NCCL.
- Selective: Load only the tensors you need.
- Flexible: Support Direct I/O, Buffered I/O, MMAP, and GPUDirect Storage. ...

Example:
```python
from instanttensor import safe_open

tensors = {}
with safe_open("model.safetensors", framework="pt", device=0) as f:
    for name, tensor in f.tensors():
        tensors[name] = tensor
```

...

</details>

### pymc

Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with PyTensor

`pip install pymc` · installs (wheel) · licence: Apache-2.0 · rank 3822 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pymc/) · [source](http://github.com/pymc-devs/pymc)

<details><summary>README extract</summary>

PyMC (formerly PyMC3) is a Python package for Bayesian statistical modeling
focusing on advanced Markov chain Monte Carlo (MCMC) and variational inference (VI)
algorithms. Its flexibility and extensibility make it applicable to a
large suite of problems. ...

Features:
- Intuitive model specification syntax, for example, `x ~ N(0,1)`
 translates to `x = Normal('x',0,1)`
- Powerful sampling algorithms, such as the No U-Turn
 Sampler, allow complex models
 with thousands of parameters with little specialized ...

Example:
```python
import pymc as pm

# Taking draws from a normal distribution
seed = 42
x_dist = pm.Normal.dist(shape=(100, 3))
x_data = pm.draw(x_dist, random_seed=seed)

# Independent Variables:
# Sunlight Hours: Number of hours the plant is exposed to sunlight daily.
...

</details>

### plyfile

PLY file reader/writer

`pip install plyfile` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 3833 · last release 2026-07-28 · [PyPI](https://pypi.org/project/plyfile/) · [docs](https://python-plyfile.readthedocs.io) · [source](https://github.com/dranjan/python-plyfile)

_README extract left out: share-alike licence._

### OpenCC

Conversion between Traditional and Simplified Chinese

`pip install OpenCC` · installs (wheel) · licence: Apache Software License · rank 3837 · last release 2026-08-22 · [PyPI](https://pypi.org/project/OpenCC/)

<details><summary>README extract</summary>

Open Chinese Convert (OpenCC, 開放中文轉換) is an open source project for high-quality conversion between Traditional Chinese, Simplified Chinese, Japanese Shinjitai, and regional wording across Mainland China, Taiwan, and Hong Kong. It provides dictionaries, a reusable library, conversion tools, and dictionary generation tools. ...

Features:
* 基於詞庫的確定性轉換，不使用大語言模型，結果穩定可預期，可離線快速運行。
 Deterministic, dictionary-based conversion without large language models (LLMs): results are stable and predictable, and conversion runs fast and fully offline. ...

Example:
```python
import opencc
converter = opencc.OpenCC('s2t.json')
converter.convert('汉字')  # 漢字
```

...

</details>

### nvidia-cuda-runtime-cu11

CUDA Runtime native Libraries

`pip install nvidia-cuda-runtime-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 3880 · last release 2024-08-16 · [PyPI](https://pypi.org/project/nvidia-cuda-runtime-cu11/)

### hera

Hera makes Python code easy to orchestrate on Argo Workflows through native Python integrations. It lets you construct and submit your Workflows entirely in Python.

`pip install hera` · installs (wheel) · licence: Apache Software License · rank 3923 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hera/) · [docs](https://hera.readthedocs.io/en/stable/) · [source](https://github.com/argoproj-labs/hera)

<details><summary>README extract</summary>

| | Hera is the go-to Python SDK to make Argo Workflows simple and intuitive. Easily turn Python functions into containerised templates that run on Kubernetes, with full access to its capabilities. |

See the Quick Start guide to start using Hera to
orchestrate your Argo Workflows!

Example:
```python
from hera.workflows import DAG, Workflow, script

# Turn a function into a reusable "Script template"
# using the script decorator
@script()
def echo(message: str):
    print(message)

# Orchestration logic lives *outside* of business logic
with Workflow(
    generate_name="dag-diamond-",
    entrypoint="diamond",
) as w:
...
```

...

</details>

### nvidia-cuda-nvrtc-cu11

NVRTC native runtime libraries

`pip install nvidia-cuda-nvrtc-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 3926 · last release 2024-08-16 · [PyPI](https://pypi.org/project/nvidia-cuda-nvrtc-cu11/)

### lmfit

Least-Squares Minimization with Bounds and Constraints

`pip install lmfit` · installs (wheel) · licence: BSD-3-Clause · rank 4036 · last release 2025-07-19 · [PyPI](https://pypi.org/project/lmfit/) · [docs](https://lmfit.github.io/lmfit-py/)

<details><summary>README extract</summary>

Features:
The `lmfit` Python library provides tools for non-linear least-squares
minimization and curve fitting. The goal is to make these optimization
algorithms more flexible, more comprehensible, and easier to use, with the
key feature of casting variables ...

Example:
```python
import lmfit
fit_params = lmfit.Parameters()
fit_params['amp'] = lmfit.Parameter(value=1.2)
fit_params['cen'] = lmfit.Parameter(value=40.0, vary=False)
fit_params['wid'] = lmfit.Parameter(value=4, min=0)
fit_params['fwhm'] = lmfit.Parameter(expr='wid*2.355')
```

Sections: LMfit-py, Overview, Parameters and Minimization, Curve-Fitting with lmfit.Model, Exploration of Confidence Intervals

</details>

### pyrender

Easy-to-use Python renderer for 3D visualization

`pip install pyrender` · installs (wheel) · licence: MIT License · rank 4055 · last release 2021-02-18 · [PyPI](https://pypi.org/project/pyrender/)

<details><summary>README extract</summary>

A simple implementation of Physically-Based Rendering (PBR) in Python. Compliant with the glTF 2.0 standard.

</details>

### arch

ARCH for Python

`pip install arch` · installs (wheel) · licence: NCSA · rank 4061 · last release 2025-10-21 · [PyPI](https://pypi.org/project/arch/) · [docs](https://bashtage.github.io/arch/) · [source](https://github.com/bashtage/arch)

<details><summary>README extract</summary>

Autoregressive Conditional Heteroskedasticity (ARCH) and other tools for
financial econometrics, written in Python (with Cython and/or Numba used
to improve performance)

| Metric | |

| Latest Release | |
| | |
| Continuous Integration | |
| Coverage | |
| Code Quality | |
| Citation | |
| Documentation | |

Example:
```python
import datetime as dt
import pandas_datareader.data as web
st = dt.datetime(1990,1,1)
en = dt.datetime(2014,1,1)
data = web.get_data_yahoo('^FTSE', start=st, end=en)
returns = 100 * data['Adj Close'].pct_change().dropna()

from arch import arch_model
am = arch_model(returns)
res = am.fit()
```

...

</details>

### tensorflow-hub

TensorFlow Hub is a library to foster the publication, discovery, and consumption of reusable parts of machine learning models.

`pip install tensorflow-hub` · installs (wheel) · licence: Apache Software License · rank 4167 · last release 2024-01-30 · [PyPI](https://pypi.org/project/tensorflow-hub/)

### fasttext-numpy2

fasttext Python bindings, fixed numpy 2 compatibiliy

`pip install fasttext-numpy2` · installs from source (sdist only) · licence: MIT License · rank 4170 · last release 2024-11-09 · [PyPI](https://pypi.org/project/fasttext-numpy2/)

<details><summary>README extract</summary>

fasttext with one line changed to support numpy 2.

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

Sections: fasttext-numpy2, build, build for pypi, notes, fastText, Requirements, Usage overview, Word representation model, Saving and loading a model object, Text classification model, Compress model files with quantization, IMPORTANT: Preprocessing data / encoding conventions, More examples, API

</details>

### s5cmd

This project provides the infrastructure to build s5cmd Python wheels.

`pip install s5cmd` · installs (wheel) · licence: MIT License · rank 4172 · last release 2025-09-09 · [PyPI](https://pypi.org/project/s5cmd/)

<details><summary>README extract</summary>

[][actions-link]

[][pypi-link]
[][pypi-link]

Features:
`s5cmd` is a very fast S3 and local filesystem execution tool. It comes with
support for a multitude of operations including tab completion and wildcard
support for files, which can be very handy for your object storage workflow
while working with ...

Sections: s5cmd Python Distributions, Overview, Platforms

</details>

### curated-tokenizers

Lightweight piece tokenization library

`pip install curated-tokenizers` · installs (wheel) · licence: MIT License · rank 4174 · last release 2026-08-24 · [PyPI](https://pypi.org/project/curated-tokenizers/)

<details><summary>README extract</summary>

This Python library provides word-/sentencepiece tokenizers. The following
types of tokenizers are currenty supported:

| Tokenizer | Binding | Example model |

| BPE | sentencepiece | |
| Byte BPE | Native | RoBERTa/GPT-2 |
| Unigram | sentencepiece | XLM-RoBERTa |
| Wordpiece | Native | BERT | ...

Sections: 🥢 Curated Tokenizers, ⚠️ Warning: experimental package, 🚀 Quickstart

</details>

### pyviz-comms

A JupyterLab extension for rendering HoloViz content.

`pip install pyviz-comms` · installs (wheel) · licence: BSD License · rank 4195 · last release 2025-06-20 · [PyPI](https://pypi.org/project/pyviz-comms/) · [source](https://github.com/holoviz/pyviz_comms.git)

<details><summary>README extract</summary>

Offers a simple bidirectional communication architecture between Python and JavaScript,
with support for Jupyter comms in both the classic notebook and Jupyterlab.
Available for use by any PyViz tool, but currently primarily used by
HoloViz tools. ...

Sections: pyviz_comms, Compatibility, Compatible JupyterLab and jupyterlab_pyviz versions

</details>

### gmsh

Gmsh is a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities.

`pip install gmsh` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 4232 · last release 2026-03-24 · [PyPI](https://pypi.org/project/gmsh/)

_README extract left out: share-alike licence._

### cvxopt

Convex optimization package

`pip install cvxopt` · installs (wheel) · licence: not stated · rank 4236 · last release 2026-02-10 · [PyPI](https://pypi.org/project/cvxopt/) · [source](https://github.com/cvxopt/cvxopt)

<details><summary>README extract</summary>

Python Software for Convex Optimization

* Website
* Documentation
* Google Groups forum

Release info

Related projects

* CVXOPT wheels
* CVXOPT conda-forge package
* Julia interface to CVXOPT
* MATLAB interface to CVXOPT

Build status

</details>

### paddlex

Low-code development tool based on PaddlePaddle.

`pip install paddlex` · installs (wheel) · licence: Apache-2.0 · rank 4252 · last release 2026-06-25 · [PyPI](https://pypi.org/project/paddlex/)

<details><summary>README extract</summary>

PaddleX 3.0 是基于飞桨框架构建的低代码开发工具，它集成了众多开箱即用的预训练模型，可以实现模型从训练到推理的全流程开发，支持国内外多款主流硬件，助力AI 开发者进行产业实践。

Example:
```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline=[产线名称])
output = pipeline.predict([输入图片名称])
for res in output:
    res.print()
    res.save_to_img("./output/")
    res.save_to_json("./output/")
```

Sections: 🌟 特性 | 🌐 在线体验｜🚀 快速开始 | 📖 文档 | 🔥能力支持 | 📋 模型列表, 🇨🇳 简体中文 | 🇬🇧 English, 🔍 简介, 🌟 特性, 📣 近期更新, ⏭️ 快速开始, 🛠️ 安装, 💻 命令行使用, 📝 Python 脚本使用, 📖 文档, 🤔 FAQ, 💬 Discussion, 📄 许可证书

</details>

### msgpack-numpy

Numpy data serialization using msgpack

`pip install msgpack-numpy` · installs (wheel) · licence: BSD License · rank 4253 · last release 2022-06-09 · [PyPI](https://pypi.org/project/msgpack-numpy/)

<details><summary>README extract</summary>

Package Description

This package provides encoding and decoding routines that enable the
serialization and deserialization of numerical and array data types provided by
numpy using the highly efficient
msgpack format. Serialization of Python's
native complex data types is also supported.

Installation ...

</details>

### Cartopy

A Python library for cartographic visualizations with Matplotlib

`pip install Cartopy` · installs (wheel) · licence: BSD-3-Clause · rank 4264 · last release 2026-09-17 · [PyPI](https://pypi.org/project/Cartopy/) · [docs](https://cartopy.readthedocs.io/stable/)

<details><summary>README extract</summary>

data analysis and visualisation easy.

Features:
Cartopy is a Python package designed to make drawing maps for data
analysis and visualisation easy.

It features:

- object oriented projection definitions
- point, line, polygon and image transformations between projections ...

Sections: Overview, Get in touch

</details>

### boost-histogram

The Boost::Histogram Python wrapper.

`pip install boost-histogram` · installs (wheel) · licence: BSD-3-Clause AND BSL-1.0 · rank 4270 · last release 2026-09-04 · [PyPI](https://pypi.org/project/boost-histogram/) · [docs](https://boost-histogram.readthedocs.io/)

<details><summary>README extract</summary>

[][actions-link]
[][rtd-link]

[][pypi-link]
[][conda-link]
[][pypi-link]

[][github-discussions-link]
[][gitter-link]
[](
[][spec4-link]

Python bindings for Boost::Histogram (source), a C++14 library. This is one of the fastest libraries for
histogramming, while still providing the power of a full histogram object. See
what's new. ...

Example:
```python
import boost_histogram as bh

# Compose axis however you like; this is a 2D histogram
hist = bh.Histogram(
    bh.axis.Regular(2, 0, 1),
    bh.axis.Regular(4, 0.0, 1.0),
)

# Filling can be done with arrays, one per dimension
hist.fill(
    [0.3, 0.5, 0.2],
    [0.1, 0.4, 0.9],
)

# NumPy array view into histogram counts, no overflow bins
...
```

...

</details>

### hl7apy

HL7apy: a lightweight Python library to parse, create and handle HL7 v2.x messages

`pip install hl7apy` · installs (wheel) · licence: MIT License · rank 4327 · last release 2024-03-13 · [PyPI](https://pypi.org/project/hl7apy/)

<details><summary>README extract</summary>

HL7apy: a lightweight Python library to parse, create and handle HL7 v2.x messages

HL7apy is a lightweight Python package to intuitively handle `HL7 < v2 messages according to HL7 specifications. ...

</details>

### stanza

A Python NLP Library for Many Human Languages, by the Stanford NLP Group

`pip install stanza` · installs (wheel) · licence: Apache License 2.0 · rank 4334 · last release 2026-10-01 · [PyPI](https://pypi.org/project/stanza/)

<details><summary>README extract</summary>

The Stanford NLP Group's official Python NLP library. It contains support for running various accurate natural language processing tools on 60+ languages and for accessing the Java Stanford CoreNLP software from Python. For detailed information please visit our official website. ...

Example:
```python
>>> import stanza
>>> stanza.download('en')       # Optional: pre-download English models (Pipeline can auto-download if needed)
>>> nlp = stanza.Pipeline('en') # This sets up a default neural pipeline in English
>>> doc = nlp("Barack Obama was born in Hawaii. He was elected president in 2008.")
>>> doc.sentences[0].print_dependencies()
```

...

</details>

### simpleitk

SimpleITK is a simplified interface to the Insight Toolkit (ITK) for image registration and segmentation

`pip install simpleitk` · installs (wheel) · licence: Apache Software License · rank 4347 · last release 2026-10-30 · [PyPI](https://pypi.org/project/simpleitk/) · [docs](https://simpleitk.readthedocs.io/en/release/) · [source](https://github.com/SimpleITK/SimpleITK)

<details><summary>README extract</summary>

| | GithubActions | ReadTheDocs |

| release | | |
| master | | |

SimpleITK is an image analysis toolkit with a large number of components supporting general filtering operations, image segmentation and registration. ...

</details>

### uproot

ROOT I/O in pure Python and NumPy.

`pip install uproot` · installs (wheel) · licence: BSD-3-Clause · rank 4369 · last release 2026-10-06 · [PyPI](https://pypi.org/project/uproot/)

<details><summary>README extract</summary>

Uproot is a library for reading and writing ROOT files in pure Python and NumPy.

Unlike the standard C++ ROOT implementation, Uproot is only an I/O library, primarily intended to stream data into machine learning libraries in Python. Unlike PyROOT and root_numpy, Uproot does not depend on C++ ROOT. ...

Sections: Getting help, Dependencies

</details>

### tensorflow-probability

Probabilistic modeling and statistical inference in TensorFlow

`pip install tensorflow-probability` · installs (wheel) · licence: Apache Software License · rank 4394 · last release 2024-11-08 · [PyPI](https://pypi.org/project/tensorflow-probability/)

<details><summary>README extract</summary>

TensorFlow Probability is a library for probabilistic reasoning and statistical
analysis in TensorFlow. As part of the TensorFlow ecosystem, TensorFlow
Probability provides integration of probabilistic methods with deep networks,
gradient-based inference via automatic differentiation, and scalability to
large datasets and models via hardware ...

Sections: TensorFlow Probability, Examples, Stable Builds, Nightly Builds, References

</details>

### nccl-extensions

Python bindings for the nccl-extensions communication libraries (nccl_ep, nccl_m2n)

`pip install nccl-extensions` · installs (wheel) · licence: Apache-2.0 · rank 4446 · last release 2026-09-02 · [PyPI](https://pypi.org/project/nccl-extensions/) · [source](https://github.com/NVIDIA/nccl-extensions)

<details><summary>README extract</summary>

Python bindings for the nccl-extensions communication
libraries.

This package installs into the `nccl` namespace, so the import paths are
`nccl.ep` and `nccl.m2n`:

It contributes exactly three directories to that namespace, and no
`nccl/init.py`:

| path | contents | ...

Example:
```python
import nccl.ep as ep
import nccl.m2n as m2n
```

Sections: nccl-extensions (Python), Package layout, Regenerating the bindings

</details>

### rosbags

Pure Python library to read, modify, convert, and write rosbag files.

`pip install rosbags` · installs (wheel) · licence: Apache-2.0 · rank 4458 · last release 2026-10-20 · [PyPI](https://pypi.org/project/rosbags/) · [docs](https://ternaris.gitlab.io/rosbags) · [source](https://gitlab.com/ternaris/rosbags)

<details><summary>README extract</summary>

Rosbags is the pure python library for everything rosbag. It contains:

- highlevel easy-to-use interfaces,
- rosbag2 reader and writer,
- rosbag1 reader and writer,
- extensible type system with serializers and deserializers,
- efficient converter between rosbag1 and rosbag2,
- and more. ...

Example:
```python
from pathlib import Path

from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore

bagpath = Path('/home/ros/rosbag_2020_03_24')

# Create a type store to use if the bag has no message definitions.
typestore = get_typestore(Stores.ROS2_FOXY)

# Create reader instance and open for reading.
...
```

Sections: Rosbags, Getting started, Documentation

</details>

### hist

Hist classes and utilities

`pip install hist` · installs (wheel) · licence: BSD-3-Clause · rank 4488 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hist/) · [docs](https://hist.readthedocs.io/)

<details><summary>README extract</summary>

[][actions-link]
[][rtd-link]
[][pre-commit-link]

[][pypi-link]
[][conda-link]
[][pypi-link]
[][doi-link]
[][license-link]

[][github-discussions-link]
[][binder-link]
[][sk-link]
[][spec4-link]

Hist is an analyst-friendly front-end for
boost-histogram, designed for
Python 3.10+ (3.6-3.9 users get older versions). See what's new.

Features:
Hist currently provides everything boost-histogram provides, and the following enhancements:

 - `name=` is a unique label describing each axis.
 - `label=` is an optional string that is used in plotting (defaults to `name`
 if not provided). ...

Example:
```python
from hist import Hist

# Quick construction, no other imports needed:
h = (
    Hist.new.Reg(10, 0, 1, name="x", label="x-axis")
    .Var(range(10), name="y", label="y-axis")
    .Int64()
...

</details>

### uhi

Unified Histogram Interface: tools to help library authors work with histograms

`pip install uhi` · installs (wheel) · licence: BSD-3-Clause · rank 4514 · last release 2026-10-07 · [PyPI](https://pypi.org/project/uhi/) · [docs](https://uhi.readthedocs.io/en/latest/) · [source](https://github.com/Scikit-HEP/uhi)

<details><summary>README extract</summary>

[][actions-link]
[][rtd-link]
[][pre-commit-link]
[][black-link]

[][pypi-link]
[][conda-link]
[][pypi-link]

[][github-discussions-link]
[][gitter-link]
[][zenodo-link]
[](
[][spec4-link]

This is a package meant primarily for documenting histogram
indexing and the PlottableHistogram Protocol and any future cross-library
standards. ...

</details>

### histoprint

Pretty print of NumPy (and other) histograms to the console

`pip install histoprint` · installs (wheel) · licence: MIT · rank 4534 · last release 2026-08-17 · [PyPI](https://pypi.org/project/histoprint/)

<details><summary>README extract</summary>

`Histoprint` uses a mix of terminal color codes and Unicode trickery (i.e.
combining characters) to plot overlaying histograms. Some terminals are not
able to display Unicode combining characters correctly. `Histoprint` can still be
used in those terminals, but the character set needs to be constrained to the
non-combining ones (see below).

Example:
```python
import numpy as np
from histoprint import text_hist, print_hist

A = np.random.randn(1000) - 2
B = np.random.randn(1000)
C = np.random.randn(1000) + 2
D = np.random.randn(500) * 2

# text_hist is a thin wrapper for numpy.histogram
text_hist(
    B, bins=[-5, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 5], title="Variable bin widths"
)

...
```

...

</details>

### flyteidl

IDL for Flyte Platform

`pip install flyteidl` · does not install on CPython 3.14 · licence: Apache Software License · rank 4566 · last release 2026-07-09 · [PyPI](https://pypi.org/project/flyteidl/)

<details><summary>README extract</summary>

This is one of the core components of Flyte. It contains the Specification of the Flyte Language using protobuf messages, the Backend API specification in gRPC, and Swagger REST. The repo contains the generated clients and protocol message structures in multiple languages. ...

</details>

### nvidia-mathdx

MathDx Device libraries

`pip install nvidia-mathdx` · installs (wheel) · licence: Other/Proprietary License · rank 4573 · last release 2025-11-13 · [PyPI](https://pypi.org/project/nvidia-mathdx/) · [docs](https://docs.nvidia.com/cuda/cufftdx/index.html)

<details><summary>README extract</summary>

Nvidia MathDX APIs are device side API extensions for performing mathematical calculations inside your CUDA kernel.
Fusing numerical operations can decrease the latency and improve the performance of your application.

- MathDx Documentation
- MathDx Downloads

</details>

### pymoo

Multi-Objective Optimization in Python

`pip install pymoo` · installs (wheel) · licence: Apache-2.0 · rank 4574 · last release 2026-06-28 · [PyPI](https://pypi.org/project/pymoo/)

<details><summary>README extract</summary>

Documentation / Paper / Installation / Usage / Citation / Contact

Our open-source framework pymoo offers state of the art single- and multi-objective algorithms and many more features
related to multi-objective optimization such as visualization and decision making.

Example:
```python
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

problem = get_problem("zdt1")

algorithm = NSGA2(pop_size=100)

res = minimize(problem,
               algorithm,
               ('n_gen', 200),
               seed=1,
...
```

Sections: pymoo: Multi-objective Optimization in Python, Usage, Contact

</details>

### pymavlink

Python MAVLink code

`pip install pymavlink` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 4575 · last release 2026-09-24 · [PyPI](https://pypi.org/project/pymavlink/)

_README extract left out: share-alike licence._

### optuna-integration

Integration libraries of Optuna.

`pip install optuna-integration` · installs (wheel) · licence: MIT License · rank 4648 · last release 2026-09-07 · [PyPI](https://pypi.org/project/optuna-integration/) · [source](https://github.com/optuna/optuna-integration)

<details><summary>README extract</summary>

This package is an integration module of Optuna, an automatic Hyperparameter optimization software framework.
The modules in this package provide users with extended functionalities for Optuna in combination with third-party libraries such as PyTorch, sklearn, and TensorFlow. ...

Sections: Optuna-Integration, Integration Modules, Communication, Reference

</details>

### transforms3d

Functions for 3D coordinate transformations

`pip install transforms3d` · installs (wheel) · licence: BSD License · rank 4660 · last release 2024-06-20 · [PyPI](https://pypi.org/project/transforms3d/)

<details><summary>README extract</summary>

Code to convert between various geometric transformations.

* Composing rotations / zooms / shears / translations into affine matrix;
* Decomposing affine matrix into rotations / zooms / shears / translations;
* Conversions between different representations of rotations, including:

 * 3x3 Rotation matrices;
 * Euler angles;
 * quaternions. ...

Sections: Transforms3d, Documentation, Code

</details>

### DracoPy

Python wrapper for Google's Draco Mesh Compression Library

`pip install DracoPy` · installs (wheel) · licence: Apache-2.0 · rank 4671 · last release 2026-10-07 · [PyPI](https://pypi.org/project/DracoPy/)

<details><summary>README extract</summary>

DracoPy is a Python wrapper for Google's Draco mesh compression library.

Example:
```python
import os
import DracoPy

with open('bunny.drc', 'rb') as draco_file:
  mesh = DracoPy.decode(draco_file.read())

print(f"number of points: {len(mesh.points)}")
print(f"number of faces: {len(mesh.faces)}")
print(f"number of normals: {len(mesh.normals)}")

# Note: If mesh.points is an integer numpy array,
...
```

</details>

### causallib

A Python package for flexible and modular causal inference modeling

`pip install causallib` · installs (wheel) · licence: Apache Software License · rank 4672 · last release 2025-04-06 · [PyPI](https://pypi.org/project/causallib/) · [docs](https://causallib.readthedocs.io/en/latest/) · [source](https://github.com/BiomedSciAI/causallib)

<details><summary>README extract</summary>

A Python package for inferring causal effects from observational data.

Causal inference analysis enables estimating the causal effect of
an intervention on some outcome from real-world non-experimental observational data.

This package provides a suite of causal methods,
under a unified scikit-learn-inspired API. ...

Example:
```python
from sklearn.linear_model import LogisticRegression
from causallib.estimation import IPW
from causallib.datasets import load_nhefs

data = load_nhefs()
ipw = IPW(LogisticRegression())
ipw.fit(data.X, data.a)
potential_outcomes = ipw.estimate_population_outcome(data.X, data.a, data.y)
...
```

...

</details>

### holoviews

A high-level plotting API for the PyData ecosystem built on HoloViews.

`pip install holoviews` · installs (wheel) · licence: BSD-3-Clause · rank 4712 · last release 2026-08-24 · [PyPI](https://pypi.org/project/holoviews/) · [docs](https://holoviews.org/) · [source](https://github.com/holoviz/holoviews)

<details><summary>README extract</summary>

**Stop plotting your data - annotate your data and let it visualize
itself.**

| | |

| Downloads |
| Build Status | |
| Coverage | |
| Latest dev release | |
| Latest release | |
| Python | |
| Docs | |
| Support | |

HoloViews is an open-source
Python library designed to make data analysis and visualization seamless
and simple. ...

</details>

### hmmlearn

Hidden Markov Models in Python with scikit-learn like API

`pip install hmmlearn` · installs from source (sdist only) · licence: BSD License · rank 4755 · last release 2024-10-31 · [PyPI](https://pypi.org/project/hmmlearn/) · [source](https://github.com/hmmlearn/hmmlearn)

<details><summary>README extract</summary>

GitHubPyPI|
Read the DocsBuildCodeCov|

hmmlearn is a set of algorithms for unsupervised learning and inference
of Hidden Markov Models. For supervised learning learning of HMMs and similar
models see seqlearn.

Note: This package is under limited-maintenance mode.

The required dependencies to use hmmlearn are ...

Sections: hmmlearn, Important links, Dependencies

</details>

### panel-material-ui

An extension to bring MaterialUI components to Panel.

`pip install panel-material-ui` · installs (wheel) · licence: BSD License · rank 4780 · last release 2026-11-02 · [PyPI](https://pypi.org/project/panel-material-ui/) · [source](https://github.com/panel-extensions/panel-material-ui)

<details><summary>README extract</summary>

Downloads

Build Status

Coverage

Latest dev release

Latest release

Docs

Support

Welcome to Panel Material UI – a library that brings the sleek design and comprehensive component set of Material UI into the world of Panel.

Features:
- Consistent Look & Feel
 Panel Material UI leverages Material UI’s design principles to give your Panel dashboards and applications a modern, cohesive style.

- Easy Theming & Styling
 Take control of your UI using Material UI’s theming concepts. ...

Sections: ✨ Welcome to panel-material-ui, Why Panel Material UI?, Documentation

</details>

### mlxtend

Machine Learning Library Extensions

`pip install mlxtend` · installs (wheel) · licence: BSD License · rank 4783 · last release 2026-06-06 · [PyPI](https://pypi.org/project/mlxtend/) · [docs](https://rasbt.github.io/mlxtend) · [source](https://github.com/rasbt/mlxtend)

<details><summary>README extract</summary>

Mlxtend (machine learning extensions) is a Python library of useful tools for the day-to-day data science tasks.
It is primarily used for:
- Ensemble methods such as stacking and voting classifiers
- Feature selection and feature extraction techniques
- Visualization utilities (e.g., decision regions, confusion matrices) ...

Example:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import itertools
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import EnsembleVoteClassifier
from mlxtend.data import iris_data
...
```

Sections: Links, Using uv, Dev Version, Examples, Contact

</details>

### spython

Command line python tool for working with singularity.

`pip install spython` · installs (wheel) · licence: LICENSE · rank 4800 · last release 2024-09-15 · [PyPI](https://pypi.org/project/spython/)

<details><summary>README extract</summary>

Singularity Python (spython) is the Python API for working with Singularity containers. See
the documentation for installation and usage, and
the install instructions for a quick start.

This library does not support Singularity 2.x! It won't work and we no longer support it. ...

</details>

### spark-nlp

John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.

`pip install spark-nlp` · installs (wheel) · licence: Apache Software License · rank 4807 · last release 2026-09-23 · [PyPI](https://pypi.org/project/spark-nlp/)

<details><summary>README extract</summary>

Spark NLP is a state-of-the-art Natural Language Processing library built on top of Apache Spark. It provides simple, performant & accurate NLP annotations for machine learning pipelines that scale easily in a distributed environment.

Spark NLP comes with 100000+ pretrained pipelines and models in more than 200+ languages. ...

Features:
- Text Preprocessing
- Parsing and Analysis
- Sentiment and Classification
- Embeddings
- Classification and Question Answering
- Machine Translation and Generation
- Image and Speech
- Integration and Interoperability (ONNX, OpenVINO) ...

Example:
```python
# Import Spark NLP
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.pretrained import PretrainedPipeline
import sparknlp

# Start SparkSession with Spark NLP
...

</details>

### nvidia-cusparse-cu11

CUSPARSE native runtime libraries

`pip install nvidia-cusparse-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 4882 · last release 2024-08-17 · [PyPI](https://pypi.org/project/nvidia-cusparse-cu11/)

### nvidia-cufft-cu11

CUFFT native runtime libraries

`pip install nvidia-cufft-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 4888 · last release 2024-08-17 · [PyPI](https://pypi.org/project/nvidia-cufft-cu11/)

### sktime

A unified framework for machine learning with time series

`pip install sktime` · installs (wheel) · licence: BSD License · rank 4898 · last release 2026-09-22 · [PyPI](https://pypi.org/project/sktime/) · [docs](https://www.sktime.net) · [source](https://github.com/sktime/sktime)

<details><summary>README extract</summary>

> A unified interface for machine learning with time series

:rocket: Version 1.2.0 out now! Check out the release notes here.

sktime is a library for time series analysis in Python. It provides a unified interface for multiple time series learning tasks. ...

Example:
```python
from sktime.datasets import load_airline
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.theta import ThetaForecaster
from sktime.split import temporal_train_test_split
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error

y = load_airline()
y_train, y_test = temporal_train_test_split(y)
...
```

...

</details>

### nvidia-cusolver-cu11

CUDA solver native runtime libraries

`pip install nvidia-cusolver-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 4911 · last release 2024-08-17 · [PyPI](https://pypi.org/project/nvidia-cusolver-cu11/)

### unitycatalog-client

Official Python SDK for Unity Catalog

`pip install unitycatalog-client` · installs (wheel) · licence: Apache Software License · rank 4912 · last release 2026-10-11 · [PyPI](https://pypi.org/project/unitycatalog-client/) · [source](https://github.com/unitycatalog/unitycatalog)

<details><summary>README extract</summary>

Welcome to the official Python Client SDK for Unity Catalog!

Unity Catalog is the industry's only universal catalog for data and AI.

- Multimodal interface supports any format, engine, and asset
 - Multi-format support: It is extensible and supports Delta Lake, Apache Iceberg and Apache Hudi via UniForm, Apache Parquet, JSON, CSV, and many ...

Example:
```python
from unitycatalog.client import Configuration

config = Configuration()
config.host = "
```

Sections: Unity Catalog Python Client SDK, Python Client SDK, Usage, Feedback

</details>

### nvidia-curand-cu11

CURAND native runtime libraries

`pip install nvidia-curand-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 4937 · last release 2024-08-17 · [PyPI](https://pypi.org/project/nvidia-curand-cu11/)

### airbyte-cdk

A framework for writing Airbyte Connectors.

`pip install airbyte-cdk` · installs (wheel) · licence: MIT License · rank 4949 · last release 2026-11-06 · [PyPI](https://pypi.org/project/airbyte-cdk/) · [docs](https://docs.airbyte.io/) · [source](https://github.com/airbytehq/airbyte-python-cdk)

<details><summary>README extract</summary>

Airbyte Python CDK is a framework for building Airbyte API Source Connectors. It provides a set of
classes and helpers that make it easy to build a connector against an HTTP API (REST, GraphQL, etc),
or a generic Python source connector.

If you're looking to build a connector, we highly recommend that you first
start with the Connector Builder. ...

Sections: Airbyte Python CDK and Low-Code CDK, Building Connectors with the CDK, Python CDK Overview

</details>

### nvidia-cuda-cupti-cu11

CUDA profiling tools runtime libs.

`pip install nvidia-cuda-cupti-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 4974 · last release 2024-08-16 · [PyPI](https://pypi.org/project/nvidia-cuda-cupti-cu11/)

<details><summary>README extract</summary>

Provides libraries to enable third party tools using GPU profiling APIs.

</details>

### nvidia-nvtx-cu11

NVIDIA Tools Extension

`pip install nvidia-nvtx-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 5013 · last release 2024-08-16 · [PyPI](https://pypi.org/project/nvidia-nvtx-cu11/)

<details><summary>README extract</summary>

A C-based API for annotating events, code ranges, and resources in your applications. Applications which integrate NVTX can use the Visual Profiler to capture and visualize these events and ranges.

</details>

### python-gdcm

Grassroots DICOM runtime libraries

`pip install python-gdcm` · installs (wheel) · licence: Apache-2.0 · rank 5015 · last release 2026-05-11 · [PyPI](https://pypi.org/project/python-gdcm/)

<details><summary>README extract</summary>

Unofficial GDCM packages for Python 3 on Linux, Windows and MacOS (both Intel and Apple Silicon).

Grassroots DiCoM is a C++ library for DICOM medical files that can be wrapped for Python using SWIG. It supports datasets encoded using native, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntaxes. ...

Example:
```python
import gdcm
reader = gdcm.ImageReader()
reader.SetFileName("dicom_image_file.dcm")
ret = reader.Read()
if not ret:
    print("It was not possible to read your DICOM file")
```

Sections: Python-GDCM, Using pip, From source, Setup environment, Clone source, Usage, Reading a DICOM image file, Other Examples

</details>

### nvidia-nccl-cu11

NVIDIA Collective Communication Library (NCCL) Runtime

`pip install nvidia-nccl-cu11` · installs (wheel) · licence: Other/Proprietary License · rank 5024 · last release 2024-04-03 · [PyPI](https://pypi.org/project/nvidia-nccl-cu11/)

<details><summary>README extract</summary>

NCCL (pronounced "Nickel") is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, and reduce-scatter. It has been optimized to achieve high bandwidth on any platform using PCIe, NVLink, NVswitch, as well as networking using InfiniBand Verbs or TCP/IP sockets.

</details>

### pdbp

pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.

`pip install pdbp` · installs (wheel) · licence: PSF · rank 5044 · last release 2026-09-16 · [PyPI](https://pypi.org/project/pdbp/) · [source](https://github.com/mdmintz/pdbp)

<details><summary>README extract</summary>

pdbp (Pdb+) is an advanced console debugger for Python. It can be used as a drop-in replacement for pdb and pdbpp.

pdbp (Pdb+) makes Python debugging a lot easier (and more fun!)

Example:
```python
import pdb
import pdbp
for key in pdbp.dict.keys():
    pdb.dict[key] = pdbp.dict[key]
```

Sections: pdbp (Pdb+), Usage, pdbp (Pdb+) commands, Post Mortem Debug Mode, Sticky Mode vs Non-Sticky Mode, Tab completion, Multi-layer highlighting in the same stack, More examples

</details>

### mujoco-warp

MuJoCo Warp (MJWarp)

`pip install mujoco-warp` · installs (wheel) · licence: Apache-2.0 · rank 5053 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mujoco-warp/) · [docs](https://mujoco.readthedocs.io) · [source](https://github.com/google-deepmind/mujoco_warp)

<details><summary>README extract</summary>

MJWarp is a GPU-accelerated version of the MuJoCo physics simulator, designed for NVIDIA hardware. MJWarp delivers high-throughput, accurate simulation for robotics research.

MJWarp is maintained by Google DeepMind and NVIDIA as part of the Newton project.

Sections: MuJoCo Warp (MJWarp), Getting started, Examples, Integrating MuJoCo Warp, MuJoCo API Compatibility, Batch Rendering

</details>

### openqasm3

Reference OpenQASM AST in Python

`pip install openqasm3` · installs (wheel) · licence: Apache Software License · rank 5063 · last release 2025-02-19 · [PyPI](https://pypi.org/project/openqasm3/)

<details><summary>README extract</summary>

<!-- long-description-skip-begin --><!-- long-description-skip-end -->

The `openqasm3` package contains the reference abstract syntax tree (AST) for representing OpenQASM 3 programs, tools to parse text into this AST, and tools to manipulate the AST.

The AST is intended to help with writing compiler passes for OpenQASM 3 in Python. ...

Sections: OpenQASM 3 Python Reference, Setting up ANTLR, Deployment procedure

</details>

### fsspec-xrootd

xrootd implementation for fsspec

`pip install fsspec-xrootd` · installs (wheel) · licence: BSD-3-Clause · rank 5081 · last release 2026-06-01 · [PyPI](https://pypi.org/project/fsspec-xrootd/) · [docs](https://fsspec_xrootd.readthedocs.io/)

<details><summary>README extract</summary>

An XRootD implementation for fsspec.

Sections: fsspec-xrootd, Purpose, Documentation

</details>

### tabcompleter

tabcompleter --- Autocompletion in the Python console.

`pip install tabcompleter` · installs (wheel) · licence: BSD License · rank 5083 · last release 2026-04-28 · [PyPI](https://pypi.org/project/tabcompleter/) · [source](https://github.com/mdmintz/tabcompleter)

<details><summary>README extract</summary>

tabcompleter is a friendly fork of the (unmaintained) fancycompleter package.

``tabcompleter`` lets you use the Tab key to expand and autocomplete options in the Python console.

Example:
```python
import tabcompleter
tabcompleter.interact(persist_history=True)

# Now use the Tab key in the Python console
```

Sections: tabcompleter (📃), Usage, More examples

</details>

### ydata-profiling

Generate profile report for pandas DataFrame

`pip install ydata-profiling` · does not install on CPython 3.14 · licence: MIT License · rank 5118 · last release 2026-04-22 · [PyPI](https://pypi.org/project/ydata-profiling/) · [source](https://github.com/ydataai/ydata-profiling)

<details><summary>README extract</summary>

> `ydata-profiling` is now `fg-data-profiling`. This package has been renamed to `fg-data-profiling`. Please follow the Migration Guide as soon as possible — the old package will no longer receive updates or bug fixes.

 Documentation
 Discord
 Stack Overflow
 Latest changelog

 Do you like this project? Show us your love and give feedback! ...

Example:
```python
# Before
import ydata_profiling
from ydata_profiling import ProfileReport

# After
import data_profiling
from data_profiling import ProfileReport
```

Sections: ydata-profiling, Migration Guide, 3. Update your imports, ▶️ Quickstart, Start profiling, 📊 Key features, 🎁 Latest features, ✨ Spark, 📝 Use cases, Using inside Jupyter Notebooks, Exporting the report to a file, Using in the command line, 👀 Examples, Using pip

</details>

### feu

A lightweight Python library for managing packages and versions across different Python environments

`pip install feu` · installs (wheel) · licence: BSD-3-Clause · rank 5119 · last release 2026-10-05 · [PyPI](https://pypi.org/project/feu/) · [docs](https://durandtibo.github.io/feu/) · [source](https://github.com/durandtibo/feu)

<details><summary>README extract</summary>

Features:
`feu` (French word for "fire" 🔥) is a lightweight Python library designed to help manage Python
packages and their versions across different Python environments.

Example:
```python
from feu.imports import is_package_available
from feu.compat import Target, find_closest_version
from feu.version import get_package_version

# Check if a package is available
if is_package_available("numpy"):
    version = get_package_version("numpy")
    print(f"NumPy {version} is installed!")

...
```

Sections: feu :fire, Overview, Key Features, Quick Example, Why feu?, Documentation, Quick Links, Suggestions and Communication, API stability

</details>

### canopen

CANopen stack implementation

`pip install canopen` · installs (wheel) · licence: MIT License · rank 5128 · last release 2025-08-05 · [PyPI](https://pypi.org/project/canopen/) · [docs](https://canopen.readthedocs.io/en/stable/) · [source](https://github.com/canopen-python/canopen)

<details><summary>README extract</summary>

A Python implementation of the CANopen standard.
The aim of the project is to support the most common parts of the CiA 301
standard in a simple Pythonic interface. It is mainly targeted for testing and
automation tasks rather than a standard compliant master implementation.

The library supports Python 3.8 or newer.

Features:
The library is mainly meant to be used as a master.

* NMT master
* SDO client
* PDO producer/consumer
* SYNC producer
* EMCY consumer
* TIME producer
* LSS master
* Object Dictionary from EDS
* 402 profile support ...

Example:
```python
import canopen

# Start with creating a network representing one CAN bus
network = canopen.Network()

# Add some nodes with corresponding Object Dictionaries
node = canopen.RemoteNode(6, '/path/to/object_dictionary.eds')
...

</details>

### spacy-pkuseg

Chinese word segmentation toolkit for spaCy (fork of pkuseg-python)

`pip install spacy-pkuseg` · installs (wheel) · licence: MIT License · rank 5169 · last release 2026-10-26 · [PyPI](https://pypi.org/project/spacy-pkuseg/)

<details><summary>README extract</summary>

This package is a fork of
`pkuseg-python` that simplifies
installation and serialization for use with spaCy. The
underlying segmentation tools remain unmodified.

pkuseg 是基于论文[Luo et. al, 2019]的工具包。其简单易用，支持细分领域分词，有效提升了分词准确度。

* 主要亮点
* 编译和安装
* 各类分词工具包的性能对比
* 使用方式
* 论文引用
* 常见问题及解答

Example:
```python
import pkuseg

seg = pkuseg.pkuseg()           # 以默认配置加载模型
text = seg.cut('我爱北京天安门')  # 进行分词
print(text)
```

Sections: spacy-pkuseg: Chinese word segmentation toolkit for spaCy, pkuseg：一个多领域中文分词工具包 (English Version), 目录, 主要亮点, 编译和安装, 各类分词工具包的性能对比, 细领域训练及测试结果, 默认模型在不同领域的测试效果, 使用方式, 代码示例, 参数说明, 多进程分词, 预训练模型, 版本历史

</details>

### pymatgen-io-validation

A comprehensive I/O validator for electronic structure calculations

`pip install pymatgen-io-validation` · installs (wheel) · licence: BSD-3-Clause-LBNL · rank 5182 · last release 2026-08-14 · [PyPI](https://pypi.org/project/pymatgen-io-validation/) · [source](https://github.com/materialsproject/pymatgen-io-validation)

<details><summary>README extract</summary>

This package is an extension to `pymatgen` for performing I/O validation. Specifically, this package checks for discrepancies between a specific calculation and a provided input set; it also checks for known bugs when certain input parameters are used in combination, alongside several other small checks. ...

Example:
```python
from pymatgen.io.validation import VaspValidator
validation_doc = VaspValidator.from_directory(path_to_vasp_calculation_directory)
```

Sections: pymatgen-io-validation, Usage, Rationale

</details>

### praat-parselmouth

Praat in Python, the Pythonic way

`pip install praat-parselmouth` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 5199 · last release 2025-11-27 · [PyPI](https://pypi.org/project/praat-parselmouth/) · [docs](https://parselmouth.readthedocs.io/) · [source](https://github.com/YannickJadoul/Parselmouth)

_README extract left out: share-alike licence._

### polars-lts-cpu

Blazingly fast DataFrame library

`pip install polars-lts-cpu` · installs (wheel) · licence: MIT License · rank 5213 · last release 2025-09-09 · [PyPI](https://pypi.org/project/polars-lts-cpu/) · [docs](https://docs.pola.rs/api/python/stable/reference/index.html) · [source](https://github.com/pola-rs/polars)

<details><summary>README extract</summary>

Documentation:
 Python

 Rust

 Node.js

 StackOverflow:
 Python

 Rust

 Node.js

 User guide
 Discord

Polars is a DataFrame interface on top of an OLAP Query Engine implemented in Rust using
Apache Arrow Columnar Format as the memory
model.

- Lazy | eager execution
- Multi-threaded
- SIMD
- Query optimization
- Powerful expression API ...

Example:
```python
>>> import polars as pl
>>> df = pl.DataFrame(
...     {
...         "A": [1, 2, 3, 4, 5],
...         "fruits": ["banana", "banana", "apple", "apple", "banana"],
...         "B": [5, 4, 3, 2, 1],
...         "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
...     }
... )

...
```

...

</details>

### pyhf

pure-Python HistFactory implementation with tensors and autodiff

`pip install pyhf` · installs (wheel) · licence: Apache Software License · rank 5216 · last release 2024-01-05 · [PyPI](https://pypi.org/project/pyhf/) · [docs](https://pyhf.readthedocs.io/) · [source](https://github.com/scikit-hep/pyhf)

<details><summary>README extract</summary>

|pre-commit.ci StatusCode style: black|

|GitHub Actions Status: CIGitHub Actions Status: DocsGitHub Actions Status: Publish|
|GitHub Actions Status: Docker|

The HistFactory p.d.f. ...

Example:
```python
>>> import pyhf
>>> pyhf.set_backend("numpy")
>>> model = pyhf.simplemodels.uncorrelated_background(
...     signal=[12.0, 11.0], bkg=[50.0, 52.0], bkg_uncertainty=[3.0, 7.0]
... )
>>> data = [51, 48] + model.config.auxdata
>>> test_mu = 1.0
>>> CLs_obs, CLs_exp = pyhf.infer.hypotest(
...
```

Sections: User Guide, Hello World

</details>

### google-cloud-pipeline-components

This SDK enables a set of First Party (Google owned) pipeline components that allow users to take their experience from Vertex AI SDK and other Google Cloud services and create a corresponding pipeline using KFP or Managed Pipelines.

`pip install google-cloud-pipeline-components` · installs (wheel) · licence: Apache Software License · rank 5231 · last release 2025-11-10 · [PyPI](https://pypi.org/project/google-cloud-pipeline-components/) · [source](https://github.com/kubeflow/pipelines/tree/master/components/google-cloud)

<details><summary>README extract</summary>

Google Cloud Pipeline Components (GCPC) provides predefined KFP components that can be run on Google Cloud Vertex AI Pipelines and other KFP-conformant pipeline execution backends. You can compose the components together into pipelines using the Kubeflow Pipelines SDK.

Please see the Google Cloud Pipeline Components user guide.

Sections: Google Cloud Pipeline Components, Documentation, User documentation, API documentation, Examples, Requirements

</details>

### mpi4py

Python bindings for MPI

`pip install mpi4py` · installs (wheel) · licence: BSD-3-Clause · rank 5243 · last release 2026-05-16 · [PyPI](https://pypi.org/project/mpi4py/) · [docs](https://mpi4py.readthedocs.io/en/stable/) · [source](https://github.com/mpi4py/mpi4py)

<details><summary>README extract</summary>

This package provides Python bindings for the *Message Passing
Interface* (MPI) standard. It is implemented on top of the MPI
specification and exposes an API which grounds on the standard MPI-2
C++ bindings.

Features:
This package supports:

* Convenient communication of any *picklable* Python object

 + point-to-point (send & receive)
 + collective (broadcast, scatter & gather, reductions) ...

Sections: MPI for Python, Features, Wheel packages, Linux, Fedora/RHEL, Debian/Ubuntu, HPE Cray OS, macOS, Windows, Conda packages, System packages, Building from sources

</details>

### flytekit

Flyte SDK for Python

`pip install flytekit` · installs (wheel) · licence: Apache Software License · rank 5253 · last release 2026-11-03 · [PyPI](https://pypi.org/project/flytekit/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> ## Looking for Flyte 2?
> - ⭐️ Flyte 2 is now generally available! Read more in the announcement here.
> - Want to try Flyte 2 locally? Run the Devbox with the new Python SDK for Flyte 2.
> - Want to contribute to the Flyte 2 distributed backend? See the `main` branch of this repo.
> The README below is for Flyte 1.x. ...

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

...

</details>

### doit

doit - Automation Tool

`pip install doit` · installs (wheel) · licence: MIT License · rank 5284 · last release 2026-02-09 · [PyPI](https://pypi.org/project/doit/) · [docs](https://pydoit.org/) · [source](https://github.com/pydoit/doit/)

<details><summary>README extract</summary>

Define tasks in Python. Run only what changed.

*doit* is a task management & automation tool like `make`, but in pure Python.
It tracks file dependencies, caches results, and skips tasks that are already
up-to-date. No DSL, no YAML - just Python functions.

Features:
- Incremental builds - tracks file dependencies and targets,
 re-runs only what changed
- DAG execution - tasks run in correct dependency order
- Python-native - tasks are plain Python dicts and functions,
 use any library ...

Example:
```python
def task_hello():
    """create a greeting file"""
    return {
        'actions': ['echo "Hello from doit" > hello.txt'],
        'targets': ['hello.txt'],
        'clean': True,
    }

def task_shout():
    """convert greeting to uppercase"""
    return {
...

</details>

### monai

AI Toolkit for Healthcare Imaging

`pip install monai` · installs (wheel) · licence: Apache License 2.0 · rank 5300 · last release 2026-09-27 · [PyPI](https://pypi.org/project/monai/) · [docs](https://monai.readthedocs.io/) · [source](https://github.com/Project-MONAI/MONAI)

<details><summary>README extract</summary>

Medical Open Network for AI

MONAI is a PyTorch-based, open-source framework for deep learning in healthcare imaging, part of the PyTorch Ecosystem.
Its ambitions are as follows:

- Developing a community of academic, industrial and clinical researchers collaborating on a common foundation; ...

Features:
> _Please see the technical highlights and What's New of the milestone releases._

- flexible pre-processing for multi-dimensional medical imaging data;
- compositional & portable APIs for ease of integration in existing workflows; ...

Sections: Features, Requirements, Getting Started, Docker, Model Zoo, Links

</details>

### jacobi

Compute numerical derivatives

`pip install jacobi` · installs (wheel) · licence: MIT License · rank 5309 · last release 2023-08-16 · [PyPI](https://pypi.org/project/jacobi/) · [docs](https://hdembinski.github.io/jacobi/) · [source](https://github.com/hdembinski/jacobi)

<details><summary>README extract</summary>

Fast numerical derivatives for analytic functions with arbitrary round-off error and error propagation.

Click here for full documentation.

Features:
- Robustly compute the generalised Jacobi matrix for an arbitrary real analytic mapping ℝⁿ → ℝⁱ¹ × ... × ℝⁱⁿ
- Derivative is either computed to specified accuracy (to save computing time) or until maximum precision of function is reached ...

Example:
```python
from matplotlib import pyplot as plt
import numpy as np
from jacobi import jacobi

# function of one variable with auxiliary argument; returns a vector
def f(x):
    return np.sin(x) / x

x = np.linspace(-10, 10, 200)
fx = f(x)

# f(x) is a simple vectorized function, jacobian is diagonal
fdx, fdxe = jacobi(f, x, diagonal=True)
...
```

...

</details>

### cabinetry

design and steer profile likelihood fits

`pip install cabinetry` · installs (wheel) · licence: BSD License · rank 5315 · last release 2023-09-19 · [PyPI](https://pypi.org/project/cabinetry/)

<details><summary>README extract</summary>

`cabinetry` is a Python library for building and steering binned template fits.
It is written with applications in High Energy Physics in mind.
`cabinetry` interfaces many other powerful libraries to make it easy for an analyzer to run their statistical inference pipeline. ...

Example:
```python
import cabinetry

config = cabinetry.configuration.load("config_example.yml")

# create template histograms
cabinetry.templates.build(config)

# perform histogram post-processing
cabinetry.templates.postprocess(config)

# build a workspace
ws = cabinetry.workspace.build(config)

# run a fit
model, data = cabinetry.model_utils.model_and_data(ws)
...
```

Sections: Hello world, Documentation

</details>

### scikit-optimize

Sequential model-based optimization toolbox.

`pip install scikit-optimize` · installs (wheel) · licence: BSD License · rank 5316 · last release 2024-06-04 · [PyPI](https://pypi.org/project/scikit-optimize/) · [source](https://github.com/holgern/scikit-optimize)

<details><summary>README extract</summary>

Scikit-Optimize, or `skopt`, is a simple and efficient library for
optimizing (very) expensive and noisy black-box functions. It implements
several methods for sequential model-based optimization. `skopt` aims
to be accessible and easy to use in many contexts.

The library is built on top of NumPy, SciPy, and Scikit-Learn. ...

Sections: Scikit-Optimize, Maintaining the codebase, Important links, Getting started, Pre-commit-config, Using homebrew, Run against all the files, Update package rev in pre-commit yaml, Made possible by

</details>

### botorch

Bayesian Optimization in PyTorch

`pip install botorch` · installs (wheel) · licence: MIT · rank 5319 · last release 2026-06-08 · [PyPI](https://pypi.org/project/botorch/) · [docs](https://botorch.org) · [source](https://github.com/meta-pytorch/botorch)

<details><summary>README extract</summary>

BoTorch is a library for Bayesian Optimization built on PyTorch.

*BoTorch is currently in beta and under active development!*

Features:
BoTorch
* Provides a modular and easily extensible interface for composing Bayesian
 optimization primitives, including probabilistic models, acquisition functions,
 and optimizers. ...

Example:
```python
import torch
from botorch.models import SingleTaskGP
from botorch.models.transforms import Normalize
from botorch.fit import fit_gpytorch_mll
from gpytorch.mlls import ExactMarginalLogLikelihood

# Double precision is highly recommended for GPs.
# See
train_X = torch.rand(10, 2, dtype=torch.double) * 2
...
```

Sections: Why BoTorch ?, Target Audience, Getting Started, Citing BoTorch

</details>

### unitycatalog-ai

Official Python library for Unity Catalog AI support

`pip install unitycatalog-ai` · installs (wheel) · licence: Apache Software License · rank 5320 · last release 2026-10-27 · [PyPI](https://pypi.org/project/unitycatalog-ai/) · [source](https://github.com/unitycatalog/unitycatalog)

<details><summary>README extract</summary>

The Unity Catalog AI Core library provides convenient APIs to interact with Unity Catalog functions, including the creation, retrieval and execution of functions.
The library includes clients for interacting with both Unity Catalog servers and Databricks-managed Unity Catalog services, in support of UC functions as tools in agents.

Features:
- Asynchronous and Synchronous Operations: Flexibly choose between async and sync methods based on your application's concurrency requirements.
- Comprehensive Function Management: Easily create, retrieve, list, execute, and delete UC functions. ...

Example:
```python
import asyncio
from unitycatalog.ai.core.client import UnitycatalogFunctionClient
from unitycatalog.client import ApiClient, Configuration

# Configure the Unity Catalog API client
...

</details>

### symengine

Python library providing wrappers to SymEngine

`pip install symengine` · installs (wheel) · licence: MIT · rank 5403 · last release 2026-10-31 · [PyPI](https://pypi.org/project/symengine/) · [docs](https://symengine.org/symengine.py) · [source](https://github.com/symengine/symengine.py)

<details><summary>README extract</summary>

Python wrappers to the C++ library SymEngine,
a fast C++ symbolic manipulation library.

Example:
```python
from symengine import var
x, y, z = var('x y z')
e = (x + y + z)**2
expanded_e = e.expand()
print(expanded_e)
```

Sections: SymEngine Python Wrappers, Pip, Conda package manager, Build from source, Notes on Dependencies, Verification

</details>

### great-expectations-experimental

Always know what to expect from your data.

`pip install great-expectations-experimental` · installs (wheel) · licence: Apache Software License · rank 5415 · last release 2024-09-17 · [PyPI](https://pypi.org/project/great-expectations-experimental/)

<details><summary>README extract</summary>

Great Expectations community contributions package. (See for full description).

</details>

### python-igraph

High performance graph data structures and algorithms (legacy package)

`pip install python-igraph` · installs (wheel) · licence: GNU General Public License (GPL) · rank 5450 · last release 2025-10-23 · [PyPI](https://pypi.org/project/python-igraph/) · [docs](https://igraph.org/python/doc) · [source](https://github.com/igraph/python-igraph)

_README extract left out: share-alike licence._

### hatchling-autoextras-hook

Hatchling metadata hook to generate all extras

`pip install hatchling-autoextras-hook` · installs (wheel) · licence: BSD-3-Clause · rank 5466 · last release 2025-12-26 · [PyPI](https://pypi.org/project/hatchling-autoextras-hook/) · [source](https://github.com/durandtibo/hatchling-autoextras-hook)

<details><summary>README extract</summary>

Hatchling metadata hook to automatically generate an `all` extra that combines all optional
dependencies.

Features:
This package provides a Hatchling metadata hook that
automatically creates an `all` extra in your project's optional dependencies. ...

Sections: hatchling-autoextras-hook, Overview, Usage, Example, Features, Configuration, Advanced Usage, Excluding the Hook from Certain Extras, Using with Other Metadata Hooks, Troubleshooting, Hook Not Triggering, `all` Extra Missing Dependencies, Build Failures, FAQ

</details>

### asammdf

ASAM MDF measurement data file parser

`pip install asammdf` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5510 · last release 2026-11-03 · [PyPI](https://pypi.org/project/asammdf/) · [docs](https://asammdf.readthedocs.io/en/master) · [source](https://github.com/danielhrisca/asammdf)

_README extract left out: share-alike licence._

### qiskit-aer

Aer - High performance simulators for Qiskit

`pip install qiskit-aer` · installs (wheel) · licence: Apache Software License · rank 5522 · last release 2026-10-26 · [PyPI](https://pypi.org/project/qiskit-aer/)

<details><summary>README extract</summary>

Aer is a high performance simulator for quantum circuits written in Qiskit, that includes realistic noise models.

| :exclamation: Reduced Maintenance Mode |

| Aer is currently operating under reduced maintenance. The maintainers are only able to address critical bug fixes. ...

Example:
```python
from qiskit import transpile
from qiskit.circuit.library import RealAmplitudes
from qiskit.quantum_info import SparsePauliOp
from qiskit_aer import AerSimulator

sim = AerSimulator()
# --------------------------
# Simulating using estimator
# ---------------------------
from qiskit_aer.primitives import EstimatorV2

...
```

Sections: Simulating your first Qiskit circuit with Aer, Next Steps

</details>

### fiddle

Fiddle: A Python-first configuration library

`pip install fiddle` · installs (wheel) · licence: Apache Software License · rank 5545 · last release 2026-10-22 · [PyPI](https://pypi.org/project/fiddle/) · [docs](https://github.com/google/fiddle/docs) · [source](https://github.com/google/fiddle)

<details><summary>README extract</summary>

Fiddle is a Python-first configuration library particularly well suited to ML
applications. Fiddle enables deep configurability of parameters in a program,
while allowing configuration to be expressed in readable and maintainable
Python code.

Authors: Dan Holtmann-Rice, Brennan Saeta, Sergio Guadarrama

</details>

### ecmwf-datastores-client

ECMWF Data Stores Service (DSS) API Python client

`pip install ecmwf-datastores-client` · installs (wheel) · licence: Apache-2.0 · rank 5550 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ecmwf-datastores-client/)

<details><summary>README extract</summary>

Quick Start
 Installation
 Documentation

ECMWF Data Stores Service (DSS) API Python client.

> [!IMPORTANT]
> This software is Graduated and subject to ECMWF's guidelines on Software Maturity.

Technical documentation:

Example:
```python
>>> import logging
>>> logging.basicConfig(level="INFO")
```

Sections: ecmwf-datastores-client, Configuration, Quick Start, 1. Set Up the Environment, 2. Run Quality Assurance, 3. Commit and Push, Using the Makefile

</details>

### traits

Observable typed attributes for Python classes

`pip install traits` · installs (wheel) · licence: BSD License · rank 5555 · last release 2026-10-27 · [PyPI](https://pypi.org/project/traits/) · [docs](https://docs.enthought.com/traits) · [source](https://github.com/enthought/traits)

<details><summary>README extract</summary>

The Traits project is at the center of all Enthought Tool Suite development
and has changed the mental model used at Enthought for programming in the
already extremely efficient Python programming language. We encourage everyone
to join us in enjoying the productivity gains from using such a powerful
approach. ...

Sections: Traits: observable typed attributes for Python classes, Dependencies

</details>

### mp-api

API Client for the Materials Project

`pip install mp-api` · installs (wheel) · licence: BSD-3-Clause-LBNL · rank 5577 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mp-api/)

### pytorch-tokenizers

A package with common tokenizers in Python and C++

`pip install pytorch-tokenizers` · installs (wheel) · licence: BSD License · rank 5639 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pytorch-tokenizers/) · [source](https://github.com/pytorch/executorch)

<details><summary>README extract</summary>

C++ implementations for various tokenizers (sentencepiece, tiktoken etc). Useful for other PyTorch repos such as torchchat, ExecuTorch to build LLM runners using ExecuTorch stack or AOT Inductor stack.

Sections: tokenizers, SentencePiece tokenizer, Tiktoken tokenizer, Huggingface tokenizer, Llama2.c tokenizer, Tekken tokenizer

</details>

### pandarallel

An easy to use library to speed up computation (by parallelizing on multi CPUs) with pandas.

`pip install pandarallel` · installs from source (sdist only) · licence: BSD License · rank 5651 · last release 2023-05-02 · [PyPI](https://pypi.org/project/pandarallel/)

<details><summary>README extract</summary>

| Without parallelization | |

| With parallelization | |

Pandaral.lel provides a simple way to parallelize your pandas operations on all your
CPUs by changing only one line of code. It also displays progress bars.

Example:
```python
from pandarallel import pandarallel

pandarallel.initialize(progress_bar=True)

# df.apply(func)
df.parallel_apply(func)
```

Sections: Pandaral·lel, Quickstart, Usage, Examples

</details>

### cupy-cuda13x

CuPy: NumPy & SciPy for GPU

`pip install cupy-cuda13x` · installs (wheel) · licence: MIT · rank 5659 · last release 2026-09-01 · [PyPI](https://pypi.org/project/cupy-cuda13x/) · [docs](https://docs.cupy.dev/) · [source](https://github.com/cupy/cupy)

<details><summary>README extract</summary>

CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated computing with Python.

This is a CuPy wheel (precompiled binary) package for CUDA 13.x.
You need to install CUDA Toolkit 13.x locally to use these packages. ...

</details>

### simpy

Event discrete, process based simulation for Python.

`pip install simpy` · installs (wheel) · licence: MIT License · rank 5660 · last release 2026-05-24 · [PyPI](https://pypi.org/project/simpy/) · [docs](https://simpy.readthedocs.io) · [source](https://gitlab.com/team-simpy/simpy/)

<details><summary>README extract</summary>

SimPy is a process-based discrete-event simulation framework based on standard
Python. Processes in SimPy are defined by Python generator functions and
can, for example, be used to model active components like customers, vehicles or
agents. ...

Example:
```python
>>> import simpy
>>>
>>> def clock(env, name, tick):
...     while True:
...         print(name, env.now)
...         yield env.timeout(tick)
...
>>> env = simpy.Environment()
>>> env.process(clock(env, 'fast', 0.5))
<Process(clock) object at 0x...>
>>> env.process(clock(env, 'slow', 1))
<Process(clock) object at 0x...>
>>> env.run(until=2)
fast 0
...
```

Sections: SimPy, A Simple Example, Getting started, Documentation and Help, Ports and comparable libraries

</details>

### pandas-datareader

Pandas-compatible data readers. Formerly a component of pandas.

`pip install pandas-datareader` · installs (wheel) · licence: BSD-3-Clause · rank 5689 · last release 2026-06-24 · [PyPI](https://pypi.org/project/pandas-datareader/) · [docs](https://pandas-datareader.readthedocs.io/en/latest/) · [source](https://github.com/pydata/pandas-datareader.git)

<details><summary>README extract</summary>

Macroeconomic and factor-oriented remote data access for pandas.

Example:
```python
import pandas_datareader as pdr
pdr.get_data_fred('GS10')
```

Sections: pandas-datareader, Usage, Documentation, Requirements

</details>

### onnxsim

Simplify your ONNX model

`pip install onnxsim` · installs (wheel) · licence: MIT AND (Apache-2.0 OR BSD-2-Clause) · rank 5725 · last release 2026-10-09 · [PyPI](https://pypi.org/project/onnxsim/)

<details><summary>README extract</summary>

_ONNX is great, but sometimes too complicated._

One day I wanted to export the following simple reshape operation to ONNX:

The input shape in this model is static, so what I expected is

However, I got the following complicated model instead:

Features:
At its core onnxsim runs a fixed point of shape inference, graph optimization and
constant folding until the model stops changing. Around that it offers:

- Constant folding. ...

Example:
```python
import torch

class JustReshape(torch.nn.Module):
    def init(self):
        super(JustReshape, self).init()

    def forward(self, x):
        return x.view((x.shape[0], x.shape[1], x.shape[3], x.shape[2]))

net = JustReshape()
model_name = 'just_reshape.onnx'
dummy_input = torch.randn(2, 3, 4, 5)
...
```

...

</details>

### keras-hub

Pretrained models for Keras.

`pip install keras-hub` · installs (wheel) · licence: Apache-2.0 · rank 5745 · last release 2026-11-03 · [PyPI](https://pypi.org/project/keras-hub/) · [source](https://github.com/keras-team/keras/keras_hub)

<details><summary>README extract</summary>

> [!IMPORTANT]
> 📢 KerasNLP is now KerasHub! 📢 Read
> the announcement.

KerasHub is a pretrained modeling library that aims to be simple, flexible,
and fast. The library provides Keras 3
implementations of popular model architectures, paired with a collection of
pretrained checkpoints available on Kaggle Models. ...

Example:
```python
import os
os.environ["KERAS_BACKEND"] = "jax"  # Or "tensorflow" or "torch"!
```

Sections: KerasHub: Multi-framework Pretrained Models, Quick Links, For everyone, Quickstart, Configuring your backend, Compatibility, Disclaimer, Citing KerasHub

</details>

### pin-pink

Inverse kinematics for articulated robot models, based on Pinocchio.

`pip install pin-pink` · installs (wheel) · licence: Apache Software License · rank 5784 · last release 2026-09-09 · [PyPI](https://pypi.org/project/pin-pink/) · [docs](https://stephane-caron.github.io/pink/) · [source](https://github.com/stephane-caron/pink)

<details><summary>README extract</summary>

Python inverse kinematics for articulated robot models, based on Pinocchio.

Example:
```python
from pink.tasks import FrameTask, PostureTask

tasks = {
    "base": FrameTask(
        "base",
        position_cost=1.0,              # [cost] / [m]
        orientation_cost=1.0,           # [cost] / [rad]
    ),
    "left_contact": FrameTask(
        "left_contact",
        position_cost=[0.1, 0.0, 0.1],  # [cost] / [m]
...
```

Sections: Pink, Usage, Task costs, Task targets, Differential inverse kinematics, Floating-base velocity limits, Examples, Frequently Asked Questions, Global inverse kinematics, How can I help?, See also

</details>

### openshell

OpenShell is the safe, private runtime for autonomous AI agents.

`pip install openshell` · installs (wheel) · licence: Apache-2.0 · rank 5797 · last release 2026-11-03 · [PyPI](https://pypi.org/project/openshell/) · [docs](https://docs.nvidia.com/openshell/latest/) · [source](https://github.com/NVIDIA/OpenShell)

<details><summary>README extract</summary>

> [!IMPORTANT]
> New in OpenShell 0.1.x: a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs. Read the 0.1.0 upgrade guide.

OpenShell is the safe, private runtime for fleets of autonomous AI agents. Agents are most useful when they can read files, install packages, call APIs, and use credentials. ...

Sections: How It Works, Quickstart, Explore Further, Agent Skills, SDKs, Telemetry, Notice and Disclaimer

</details>

### nemo-toolkit

NeMo - a toolkit for Conversational AI

`pip install nemo-toolkit` · installs (wheel) · licence: Apache Software License · rank 5804 · last release 2026-08-07 · [PyPI](https://pypi.org/project/nemo-toolkit/)

<details><summary>README extract</summary>

Checkout our HuggingFace🤗 collection for the latest open
weight checkpoints and demos!

> The first release of NeMo Speech after NeMo repository split is scheduled for June 2026, as the repo undergoes transformation.
> For the latest stable released version, please use the 26.02 NGC container. ...

Sections: NVIDIA NeMo Speech, Updates, Introduction, Requirements, From source with uv (recommended), From PyPI with pip (fallback — bring your own versions)

</details>

### nvidia-cuda-tileiras

TileIR Assembler Package

`pip install nvidia-cuda-tileiras` · installs (wheel) · licence: LicenseRef-NVIDIA-Proprietary · rank 5827 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cuda-tileiras/)

<details><summary>README extract</summary>

TileIR is a portable and language agnostic intermediate representation for CUDA kernels.

</details>

### qiskit-ibm-runtime

IBM Quantum client for IBM Quantum Compute (formerly Qiskit Runtime).

`pip install qiskit-ibm-runtime` · installs (wheel) · licence: Apache Software License · rank 5843 · last release 2026-10-22 · [PyPI](https://pypi.org/project/qiskit-ibm-runtime/) · [docs](https://quantum.cloud.ibm.com/docs/) · [source](https://github.com/Qiskit/qiskit-ibm-runtime)

<details><summary>README extract</summary>

Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.

IBM Quantum Compute (formerly Qiskit Runtime) is a new environment offered by IBM Quantum that streamlines quantum computations and provides optimal
implementations of the Qiskit primitives `sampler` and ...

Example:
```python
from qiskit_ibm_runtime import QiskitRuntimeService

# Save an IBM Cloud account.
QiskitRuntimeService.save_account(channel="ibm_cloud", token="MY_IBM_CLOUD_API_KEY", instance="MY_IBM_CLOUD_CRN")

# 'ibm_quantum_platform' and 'ibm_cloud' point to the same channel so they can be used interchangeably
...
```

...

</details>

### tfp-nightly

Probabilistic modeling and statistical inference in TensorFlow

`pip install tfp-nightly` · installs (wheel) · licence: Apache Software License · rank 5862 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tfp-nightly/)

<details><summary>README extract</summary>

TensorFlow Probability is a library for probabilistic reasoning and statistical
analysis in TensorFlow. As part of the TensorFlow ecosystem, TensorFlow
Probability provides integration of probabilistic methods with deep networks,
gradient-based inference via automatic differentiation, and scalability to
large datasets and models via hardware ...

Sections: TensorFlow Probability, Examples, Stable Builds, Nightly Builds, References

</details>

### megatron-core

Megatron Core - a library for efficient and scalable training of transformer based models

`pip install megatron-core` · installs from source (sdist only) · licence: BSD License · rank 5873 · last release 2026-10-29 · [PyPI](https://pypi.org/project/megatron-core/)

<details><summary>README extract</summary>

This repository contains two components: Megatron-LM and Megatron Core.

Megatron-LM is a reference example that includes Megatron Core plus pre-configured training scripts, ideal for research teams, learning distributed training, and quick experimentation. ...

Sections: Megatron-LM and Megatron Core, About, Getting Started, Latest News, Project Structure, Performance Benchmarking, Weak Scaling Results, Strong Scaling Results, Roadmaps, Resources, Getting Help

</details>

### awkward-pandas

Awkward Array Pandas Extension

`pip install awkward-pandas` · installs (wheel) · licence: BSD License · rank 5891 · last release 2023-08-08 · [PyPI](https://pypi.org/project/awkward-pandas/)

<details><summary>README extract</summary>

> Awkward Array extension for use in pandas.

See the quick
start
in the documentation for an introduction to awkward-pandas.

</details>

### ai-edge-litert

LiteRT is for mobile and embedded devices.

`pip install ai-edge-litert` · installs (wheel) · licence: Apache Software License · rank 5894 · last release 2026-10-06 · [PyPI](https://pypi.org/project/ai-edge-litert/)

<details><summary>README extract</summary>

LiteRT is the official solution for running machine learning models on mobile
and embedded devices. It enables on-device machine learning inference with low
latency and a small binary size on Android, iOS, and other operating systems.

</details>

### gin-config

Gin-Config: A lightweight configuration library for Python

`pip install gin-config` · installs (wheel) · licence: Apache Software License · rank 5967 · last release 2021-11-03 · [PyPI](https://pypi.org/project/gin-config/) · [docs](https://github.com/google/gin-config/docs) · [source](https://github.com/google/gin-config)

<details><summary>README extract</summary>

Gin provides a lightweight configuration framework for Python, based on
dependency injection. Functions or classes can be decorated with
`@gin.configurable`, allowing default parameter values to be supplied from a
config file (or passed via the command line) using a simple but powerful syntax. ...

</details>

### pyhdfe

High dimensional fixed effect absorption with Python 3

`pip install pyhdfe` · installs (wheel) · licence: MIT License · rank 5976 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pyhdfe/) · [docs](http://pyhdfe.readthedocs.io/en/latest)

<details><summary>README extract</summary>

An overview of the package, examples, and other documentation can be found on Read the Docs.

PyHDFE is a Python 3 implementation of algorithms for absorbing high dimensional fixed effects. This package was created by Jeff Gortmaker in collaboration with Anya Tarascina. ...

</details>

### mink

Python inverse kinematics based on MuJoCo

`pip install mink` · installs (wheel) · licence: Apache-2.0 · rank 5997 · last release 2026-11-01 · [PyPI](https://pypi.org/project/mink/) · [docs](https://kevinzakka.github.io/mink/) · [source](https://github.com/kevinzakka/mink)

<details><summary>README extract</summary>

mink is a library for differential inverse kinematics in Python, based on the MuJoCo physics engine.

Features include:

* Task specification in configuration or operational space;
* Limits on joint positions and velocities;
* Collision avoidance between any geom pair;
* Support for closed-chain kinematics (loop closures) via equality ...

Sections: mink, Examples, How can I help?, References

</details>

### nvidia-cuda-cccl-cu12

CUDA CCCL

`pip install nvidia-cuda-cccl-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 6006 · last release 2025-05-01 · [PyPI](https://pypi.org/project/nvidia-cuda-cccl-cu12/)

### pygam

Generalized Additive Models in Python.

`pip install pygam` · installs (wheel) · licence: Apache Software License · rank 6009 · last release 2025-12-18 · [PyPI](https://pypi.org/project/pygam/)

<details><summary>README extract</summary>

Generalized Additive Models in Python.

:rocket: Version 0.12.0 out now! See release notes here.

`pyGAM` is a package for building Generalized Additive Models in Python, with an emphasis on modularity and performance.

The API is designed for users of `scikit-learn` or `scipy`.

| | Documentation · Tutorials · Medium article | ...

Sections: pyGAM, Documentation, About, Citing pyGAM, References

</details>

### planarity

Python Wrapper for the Edge Addition Planarity Suite and Graph Library

`pip install planarity` · installs from source (sdist only) · licence: BSD-3-Clause · rank 6016 · last release 2026-06-29 · [PyPI](https://pypi.org/project/planarity/) · [docs](https://github.com/graph-algorithms/planarity/wiki) · [source](https://github.com/graph-algorithms/planarity.git)

<details><summary>README extract</summary>

The `planarity` repository provides the source code for the `planarity` Python package. The `planarity` package was originally developed to provide Python and NetworkX developers with a Python API to access planar graph testing, embedding, drawing, and forbidden subgraph isolation algorithms from the Edge Addition Planarity Suite (EAPS). ...

Example:
```python
In [1]: # Example of the complete graph of 5 nodes, K5

In [2]: # K5 is not planar

In [3]: import planarity

In [4]: edgelist = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
   ...:             ('b', 'c'),('b', 'd'),('b', 'e'),
   ...:             ('c', 'd'), ('c', 'e'),
   ...:             ('d', 'e')]

...
```

Sections: Planarity, Example

</details>

### fastdtw

Dynamic Time Warping (DTW) algorithm with an O(N) time and memory complexity.

`pip install fastdtw` · installs from source (sdist only) · licence: MIT License · rank 6029 · last release 2019-10-07 · [PyPI](https://pypi.org/project/fastdtw/)

<details><summary>README extract</summary>

fastdtw

Python implementation of `FastDTW
< [1]_, which is an approximate Dynamic Time Warping (DTW) algorithm that provides optimal or near-optimal alignments with an O(N) time and memory complexity.

Install


 pip install fastdtw

Example


 import numpy as np
 from scipy.spatial.distance import euclidean

 from fastdtw import fastdtw ...

</details>

### coola

Library to check equality between two complex/nested objects

`pip install coola` · installs (wheel) · licence: BSD-3-Clause · rank 6056 · last release 2026-07-30 · [PyPI](https://pypi.org/project/coola/) · [docs](https://durandtibo.github.io/coola/) · [source](https://github.com/durandtibo/coola)

<details><summary>README extract</summary>

Features:
`coola` is a lightweight Python library that makes it easy to compare complex and nested data
structures.
It provides simple, extensible functions to check equality between objects containing
PyTorch tensors,
NumPy arrays,
pandas/polars DataFrames, ...

Example:
```python
>>> import numpy as np
>>> import torch
>>> from coola.equality import objects_are_equal
>>> data1 = {"torch": torch.ones(2, 3), "numpy": np.zeros((2, 3))}
>>> data2 = {"torch": torch.ones(2, 3), "numpy": np.zeros((2, 3))}
>>> objects_are_equal(data1, data2)
True
```

Sections: coola, Overview, Why coola?, Features, 🔍 Equality Comparison, 📊 Data Summarization, 🔄 Data Conversion, 🗂️ Mapping Utilities, 🔁 Iteration, 📈 Reduction, Using uv (recommended), Using pip, Requirements, Compatibility Matrix

</details>

### airbyte-protocol-models-dataclasses

Declares the Airbyte Protocol using Python Dataclasses. Dataclasses in Python have less performance overhead compared to Pydantic models, making them a more efficient choice for scenarios where speed and memory usage are critical

`pip install airbyte-protocol-models-dataclasses` · installs (wheel) · licence: MIT License · rank 6067 · last release 2025-06-27 · [PyPI](https://pypi.org/project/airbyte-protocol-models-dataclasses/) · [docs](https://docs.airbyte.io/) · [source](https://github.com/airbytehq/airbyte-protocol)

### s3tokenizer

Reverse Engineering of Supervised Semantic Speech Tokenizer (S3Tokenizer) proposed in CosyVoice

`pip install s3tokenizer` · installs (wheel) · licence: Apache2.0 · rank 6078 · last release 2025-12-22 · [PyPI](https://pypi.org/project/s3tokenizer/)

<details><summary>README extract</summary>

Supervised Semantic Speech Tokenizer (S3Tokenizer)

S3Tokenizer was initially introduced in CosyVoice [[Paper]]( [[Repo]]( it is a Supervised Semantic Speech Tokenizer based on the pre-trained SenseVoice-Large model, which enhances the semantic relationship of extracted tokens to textual and paralinguistic information, is robust to data noise, and ...

Example:
```python
import s3tokenizer

tokenizer = s3tokenizer.load_model("speech_tokenizer_v1").cuda()  # or "speech_tokenizer_v1_25hz speech_tokenizer_v2_25hz speech_tokenizer_v3_25hz"

mels = []
wav_paths = ["s3tokenizer/assets/BAC009S0764W0121.wav", "s3tokenizer/assets/BAC009S0764W0122.wav"]
for wav_path in wav_paths:
    audio = s3tokenizer.load_audio(wav_path)
...
```

...

</details>

### mne

MNE-Python is an open-source Python package for exploring, visualizing, and analyzing human neurophysiological data. It provides methods for data input/output, preprocessing, visualization, source estimation, time-frequency analysis, machine learning, and statistics.

`pip install mne` · installs (wheel) · licence: BSD-3-Clause · rank 6091 · last release 2026-09-11 · [PyPI](https://pypi.org/project/mne/) · [docs](https://mne.tools/) · [source](https://github.com/mne-tools/mne-python/)

<details><summary>README extract</summary>

MNE-Python is an open-source Python package for exploring,
visualizing, and analyzing human neurophysiological data such as MEG, EEG, sEEG,
ECoG, and more. It includes modules for data input/output, preprocessing,
visualization, source estimation, time-frequency analysis, connectivity analysis,
machine learning, statistics, and more. ...

Sections: MNE-Python, Documentation, Forum, Dependencies, About

</details>

### datashader

Data visualization toolchain based on aggregating into a grid

`pip install datashader` · installs (wheel) · licence: BSD-3-Clause · rank 6102 · last release 2026-05-19 · [PyPI](https://pypi.org/project/datashader/) · [docs](https://datashader.org) · [source](https://github.com/holoviz/datashader)

<details><summary>README extract</summary>

| | |

| Downloads |
| Build Status | |
| Coverage | |
| Latest dev release | |
| Latest release | |
| Python |
| Docs | |
| Support | |

Datashader is a data rasterization pipeline for automating the process of
creating meaningful representations of large amounts of data. Datashader
breaks the creation of images of data into 3 main steps:

1. ...

Sections: Turn even the largest data into images, accurately, What is it?, Fetching Examples, Learning more, Some Examples

</details>

### littlefs-python

A python wrapper for littlefs

`pip install littlefs-python` · installs (wheel) · licence: not stated · rank 6121 · last release 2026-08-17 · [PyPI](https://pypi.org/project/littlefs-python/)

<details><summary>README extract</summary>

littlefs-python provides a thin wrapper around littlefs, a filesystem targeted for
small embedded systems.
The wrapper provides a pythonic interface to the filesystem and allows the creation,
inspection and modification of the filesystem or individual files. ...

Example:
```python
from littlefs import LittleFS

# Initialize the File System according to your specifications
fs = LittleFS(block_size=512, block_count=256)

# Open a file and write some content
with fs.open('first-file.txt', 'w') as fh:
    fh.write('Some text to begin with\n')

# Dump the filesystem content to a file
with open('FlashMemory.bin', 'wb') as fh:
...
```

Sections: littlefs for Python, Quick Examples, CLI

</details>

### jenkspy

Compute Natural Breaks (Fisher-Jenks algorithm)

`pip install jenkspy` · installs (wheel) · licence: MIT License · rank 6154 · last release 2026-02-13 · [PyPI](https://pypi.org/project/jenkspy/) · [source](https://github.com/mthh/jenkspy.git)

<details><summary>README extract</summary>

Compute "natural breaks" (*Fisher-Jenks algorithm*) on list / tuple / array / numpy.ndarray of integers/floats.

The algorithm implemented by this library is also sometimes referred to as *Fisher-Jenks algorithm*, *Jenks Optimisation Method* or *Fisher exact optimization method*. ...

Example:
```python
>>> import jenkspy
>>> import json

>>> with open('tests/test.json', 'r') as f:
...     # Read some data from a JSON file
...     data = json.loads(f.read())
...
>>> jenkspy.jenks_breaks(data, n_classes=5) # Asking for 5 classes
[0.0028109620325267315, 2.0935479691252112, 4.205495140049607, 6.178148351609707, 8.09175917180255, 9.997982932254672]
...
```

Sections: Jenkspy: Fast Fisher-Jenks breaks for Python, Usage, Requirements, Motivation

</details>

### linearmodels

Linear Panel, Instrumental Variable, Asset Pricing, and System Regression models for Python

`pip install linearmodels` · installs (wheel) · licence: NCSA · rank 6190 · last release 2026-10-16 · [PyPI](https://pypi.org/project/linearmodels/) · [docs](https://bashtage.github.io/linearmodels/) · [source](https://github.com/bashtage/linearmodels)

<details><summary>README extract</summary>

| Metric | |

| Latest Release | |
| Continuous Integration | |
| Coverage | |
| Code Quality | |
| Citation | |

Linear (regression) models for Python. Extends
statsmodels with Panel regression,
instrumental variable estimators, system estimators and models for
estimating asset prices: ...

Example:
```python
import numpy as np
from statsmodels.datasets import grunfeld
data = grunfeld.load_pandas().data
data.year = data.year.astype(np.int64)
# MultiIndex, entity - time
data = data.set_index(['firm','year'])
from linearmodels import PanelOLS
mod = PanelOLS(data.invest, data[['value','capital']], entity_effects=True)
...
```

Sections: Linear Models, Panel models, Instrumental Variable Models, Documentation, Requirements, Running, Building from source

</details>

### nevergrad

A Python toolbox for performing gradient-free optimization

`pip install nevergrad` · installs (wheel) · licence: MIT License · rank 6214 · last release 2025-04-23 · [PyPI](https://pypi.org/project/nevergrad/)

<details><summary>README extract</summary>

`nevergrad` is a Python 3.8+ library. It can be installed with:

More installation options, including windows installation, and complete instructions are available in the "Getting started" section of the documentation.

You can join Nevergrad users Facebook group here.

Minimizing a function using an optimizer (here `NGOpt`) is straightforward: ...

Example:
```python
import nevergrad as ng

def square(x):
    return sum((x - .5)**2)

optimizer = ng.optimizers.NGOpt(parametrization=2, budget=100)
recommendation = optimizer.minimize(square)
print(recommendation.value)  # recommended value
>>> [0.49971112 0.5002944]
```

Sections: Nevergrad - A gradient-free optimization platform, Documentation, Citing

</details>

### effdet

EfficientDet for PyTorch

`pip install effdet` · installs (wheel) · licence: Apache Software License · rank 6225 · last release 2023-05-21 · [PyPI](https://pypi.org/project/effdet/)

<details><summary>README extract</summary>

A PyTorch implementation of EfficientDet.

It is based on the
* official Tensorflow implementation by Mingxing Tan and the Google Brain team
* paper by Mingxing Tan, Ruoming Pang, Quoc V. Le EfficientDet: Scalable and Efficient Object Detection

There are other PyTorch implementations. ...

Sections: EfficientDet (PyTorch), Updates, 2023-05-21, 2023-02-09, 2022-01-06, 2021-11-30, 2021-11-16, 2021-07-28, 2021-04-30, 2021-02-18, 2020-12-07, 2020-11-12, 2020-11-09, 2020-10-30

</details>

### hvplot

A high-level plotting API for the PyData ecosystem built on HoloViews.

`pip install hvplot` · installs (wheel) · licence: BSD License · rank 6235 · last release 2025-12-18 · [PyPI](https://pypi.org/project/hvplot/) · [source](http://github.com/holoviz/hvplot)

<details><summary>README extract</summary>

hvPlot makes data analysis and visualization simple

| | |

| Downloads |
| Build Status | |
| Coverage | |
| Latest dev release | |
| Latest release | |
| Python | |
| Docs | |
| Binder | |
| Support | |

Home | Installation instructions | Getting Started Guide | Gallery | Reference | Examples | License | Support ...

Example:
```python
import numpy as np
import pandas as pd

idx = pd.date_range('1/1/2000', periods=1000)
df  = pd.DataFrame(np.random.randn(1000, 4), index=idx, columns=list('ABCD')).cumsum()
```

Sections: hvPlot works with the tools you know and love, hvPlot can be used for exploration, reporting and data apps, Mini getting-started, Plotting data, Interactive data apps, How to find documentation from your notebook or editor

</details>

### autoray

Abstract your array operations.

`pip install autoray` · installs (wheel) · licence: Apache-2.0 · rank 6238 · last release 2026-08-22 · [PyPI](https://pypi.org/project/autoray/) · [docs](https://autoray.readthedocs.io/) · [source](https://github.com/jcmgray/autoray/)

<details><summary>README extract</summary>

`autoray` is a lightweight python AUTOmatic-arRAY library for
abstracting your tensor operations. Primarily it provides an
*automatic* dispatch mechanism
that means you can write backend agnostic code that works for:

* numpy
* pytorch
* jax
* cupy
* mlx
* dask
* autograd
* tensorflow
* sparse
* paddle
* ... ...

Example:
```python
import autoray as ar

def noised_svd(x):
    # automatic dispatch based on supplied array
    U, s, VH = ar.do("linalg.svd", x)

    # automatic dispatch based on different array
    sn = s + 0.1 * ar.do("random.normal", size=ar.shape(s), like=s)

    # automatic dispatch for multiple arrays for certain functions
...
```

</details>

### phidget22

Phidget22 Python Library

`pip install phidget22` · installs (wheel) · licence: BSD License · rank 6263 · last release 2026-08-21 · [PyPI](https://pypi.org/project/phidget22/)

<details><summary>README extract</summary>

phidget22 is the official Python library for working with Phidgets in Python applications. It provides lightweight bindings to the native phidget22 library.

Sections: phidget22, pip Package, macOS Notes, Resources

</details>

### colour-science

Colour Science for Python

`pip install colour-science` · installs (wheel) · licence: OSI Approved · rank 6265 · last release 2025-12-06 · [PyPI](https://pypi.org/project/colour-science/) · [docs](https://colour.readthedocs.org) · [source](https://github.com/colour-science/colour)

<details><summary>README extract</summary>

Colour is an open-source
Python package providing a comprehensive number
of algorithms and datasets for colour science.

It is freely available under the
BSD-3-Clause terms.

Colour is an affiliated project of NumFOCUS, a
501(c)(3) nonprofit in the United States.

Features:
Most of the objects are available from the `colour` namespace:

Example:
```python
import colour
```

Sections: Features, Automatic Colour Conversion Graph - `colour.graph`, ```text, Colour Notation Systems - `colour.notation`, Munsell Value, Munsell Colour, Optical Phenomena - `colour.phenomena`, Rayleigh Scattering, Thin Film Interference, Light Quality - `colour.quality`, Colour Fidelity Index, Colour Quality Scale, Colour Rendering Index

</details>

### entsoe-py

A python API wrapper for ENTSO-E

`pip install entsoe-py` · installs (wheel) · licence: MIT License · rank 6278 · last release 2026-09-04 · [PyPI](https://pypi.org/project/entsoe-py/)

<details><summary>README extract</summary>

Python client for the ENTSO-E API (european network of transmission system operators for electricity)

Documentation of the API found on

Example:
```python
from entsoe import EntsoeRawClient
import pandas as pd

client = EntsoeRawClient(api_key=)

start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180101', tz='Europe/Brussels')
country_code = 'BE'  # Belgium
country_code_from = 'FR'  # France
country_code_to = 'DE_LU' # Germany-Luxembourg
type_marketagreement_type = 'A01'
...
```

Sections: entsoe-py, Usage, EntsoeRawClient, Dump result to file, Making another request, EntsoePandasClient, Download from ENTSOE File Library, Mappings, Environment variables

</details>

### pymannkendall

A python package for non-parametric Mann-Kendall family of trend tests.

`pip install pymannkendall` · installs (wheel) · licence: MIT License · rank 6288 · last release 2023-01-14 · [PyPI](https://pypi.org/project/pymannkendall/)

<details><summary>README extract</summary>

The Mann-Kendall Trend Test (sometimes called the MK test) is used to analyze time series data for consistently increasing or decreasing trends (monotonic trends). It is a non-parametric test, which means it works for all distributions (i.e. data doesn't have to meet the assumption of normality), but data should have no serial correlation. ...

Example:
```python
import numpy as np
import pymannkendall as mk

# Data generation for analysis
data = np.random.rand(360,1)

result = mk.original_test(data)
print(result)
```

Sections: pyMannKendall, What is the Mann-Kendall Test ?, Function details, Dependencies, Tests, Usage, References

</details>

### directsearch

A derivative-free solver for unconstrained minimization

`pip install directsearch` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6303 · last release 2026-06-04 · [PyPI](https://pypi.org/project/directsearch/) · [docs](https://github.com/lindonroberts/directsearch) · [source](https://github.com/lindonroberts/directsearch)

_README extract left out: share-alike licence._

### keybert

KeyBERT performs keyword extraction with state-of-the-art transformer models.

`pip install keybert` · installs (wheel) · licence: MIT License · rank 6325 · last release 2025-02-07 · [PyPI](https://pypi.org/project/keybert/) · [docs](https://maartengr.github.io/KeyBERT/) · [source](https://github.com/MaartenGr/KeyBERT.git)

<details><summary>README extract</summary>

KeyBERT is a minimal and easy-to-use keyword extraction technique that leverages BERT embeddings to
create keywords and keyphrases that are most similar to a document.

Corresponding medium post can be found here.

Example:
```python
from keybert import KeyBERT

doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
...
```

Sections: KeyBERT, 1. About the Project, 2. Getting Started, 2.2. Usage, 2.3. Max Sum Distance, 2.4. Maximal Marginal Relevance, 2.5. Embedding Models, 3. Large Language Models, References

</details>

### pyscf

PySCF: Python-based Simulations of Chemistry Framework

`pip install pyscf` · installs (wheel) · licence: Apache Software License · rank 6345 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pyscf/) · [docs](http://www.pyscf.org) · [source](https://github.com/pyscf/pyscf)

<details><summary>README extract</summary>

Python-based Simulations of Chemistry Framework

2026-11-05

* Stable release 2.15.0
* Changelog
* Documentation
* Installation
* Features
* News: 3rd PySCF Developers Meeting!

Sections: Citing PySCF, Base PySCF, Density functional calculations, Bug reports and feature requests

</details>

### pytools

A collection of tools for Python

`pip install pytools` · installs (wheel) · licence: MIT · rank 6394 · last release 2026-06-03 · [PyPI](https://pypi.org/project/pytools/) · [docs](https://documen.tician.de/pytools/)

<details><summary>README extract</summary>

Pytools is a big bag of things that are "missing" from the Python standard
library. This is mainly a dependency of my other software packages, and is
probably of little interest to you unless you use those. If you're curious
nonetheless, here's what's on offer: ...

</details>

### keras-nightly

Multi-backend Keras

`pip install keras-nightly` · installs (wheel) · licence: Apache License 2.0 · rank 6408 · last release 2026-11-08 · [PyPI](https://pypi.org/project/keras-nightly/) · [source](https://github.com/keras-team/keras)

<details><summary>README extract</summary>

Keras 3 is a multi-backend deep learning framework, with support for JAX, TensorFlow, PyTorch, and OpenVINO (for inference-only).
Effortlessly build and train models for computer vision, natural language processing, audio processing,
timeseries forecasting, recommender systems, etc. ...

Features:
- Run your high-level Keras workflows on top of any framework -- benefiting at will from the advantages of each framework,
e.g. the scalability and performance of JAX or the production ecosystem options of TensorFlow.
- Write custom components (e.g. ...

Example:
```python
import os

os.environ["KERAS_BACKEND"] = "jax"

import keras
```

Sections: Keras 3: Deep Learning for Humans, Backend Compatibility Table, Configuring your backend, Backwards compatibility, Why use Keras 3?

</details>

### pyreadr

Reads/writes R RData and Rds files into/from pandas or polars data frames.

`pip install pyreadr` · installs (wheel) · licence: AGPL-3.0-or-later · rank 6448 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pyreadr/)

_README extract left out: share-alike licence._

### captum

Model Interpretability for PyTorch

`pip install captum` · installs (wheel) · licence: BSD-3-Clause · rank 6481 · last release 2026-04-17 · [PyPI](https://pypi.org/project/captum/) · [docs](https://captum.ai) · [source](https://github.com/pytorch/captum)

<details><summary>README extract</summary>

<hr/>

<!--- BADGES: START --->
[][#github-license]

[][#pypi-package]
[][#conda-forge-package]
[][#conda-forge-package]
[][#conda-forge-feedstock]
[][#docs-package]

<!--- BADGES: END --->

Captum is a model interpretability and understanding library for PyTorch. ...

Example:
```python
import numpy as np

import torch
import torch.nn as nn

from captum.attr import (
    GradientShap,
    DeepLift,
    DeepLiftShap,
    IntegratedGradients,
    LayerConductance,
    NeuronConductance,
    NoiseTunnel,
)

class ToyModel(nn.Module):
    def init(self):
        super().init()
        self.lin1 = nn.Linear(3, 3)
...
```

Sections: About Captum, Target Audience, Getting Started, Captum Insights (Retired), FAQ, Talks and Papers, References of Algorithms

</details>

### bertopic

BERTopic performs topic Modeling with state-of-the-art transformer models.

`pip install bertopic` · installs (wheel) · licence: MIT License · rank 6484 · last release 2025-12-03 · [PyPI](https://pypi.org/project/bertopic/) · [docs](https://maartengr.github.io/BERTopic/) · [source](https://github.com/MaartenGr/BERTopic.git)

<details><summary>README extract</summary>

BERTopic is a topic modeling technique that leverages 🤗 transformers and c-TF-IDF to create dense clusters
allowing for easily interpretable topics whilst keeping important words in the topic descriptions.

BERTopic supports all kinds of topic modeling techniques:

 Guided
 Supervised
 Semi-supervised ...

Example:
```python
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)
```

Sections: BERTopic, Getting Started, Quick Start, Fine-tune Topic Representations, Visualizations, Modularity, Functionality, Common, Attributes, Variations

</details>

### deap

Distributed Evolutionary Algorithms in Python

`pip install deap` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6491 · last release 2026-04-17 · [PyPI](https://pypi.org/project/deap/)

_README extract left out: share-alike licence._

### flyteidl2

IDL for Flyte

`pip install flyteidl2` · installs (wheel) · licence: Apache Software License · rank 6498 · last release 2026-11-03 · [PyPI](https://pypi.org/project/flyteidl2/)

### gluonts

Probabilistic time series modeling in Python.

`pip install gluonts` · installs (wheel) · licence: Apache Software License · rank 6547 · last release 2026-07-31 · [PyPI](https://pypi.org/project/gluonts/) · [docs](https://ts.gluon.ai/stable/) · [source](https://github.com/awslabs/gluonts/)

<details><summary>README extract</summary>

📢 BREAKING NEWS: We released Chronos, a suite of pretrained models for zero-shot time series forecasting. Chronos can generate accurate probabilistic predictions for new time series not seen during training. Check it out here! ...

Example:
```python
import pandas as pd
import matplotlib.pyplot as plt

from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split
from gluonts.torch import DeepAREstimator

# Load data from a CSV file into a PandasDataset
df = pd.read_csv(
    "
    "TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv",
    index_col=0,
...
```

Sections: GluonTS - Probabilistic Time Series Modeling in Python, Simple Example, Citing, Links, Documentation, References, Tutorials and Workshops

</details>

### pybaselines

A library of algorithms for the baseline correction of experimental data.

`pip install pybaselines` · installs (wheel) · licence: BSD-3-Clause · rank 6580 · last release 2025-08-10 · [PyPI](https://pypi.org/project/pybaselines/) · [docs](https://pybaselines.readthedocs.io)

<details><summary>README extract</summary>

pybaselines is a library of algorithms for the baseline correction of experimental data.

* For Python 3.9 or later
* Open Source: BSD 3-Clause License

pybaselines is a Python library that provides many different algorithms for
performing baseline correction on data from experimental techniques such as
Raman, FTIR, NMR, XRD, XRF, PIXE, MALDI-TOF, ...

Example:
```python
import matplotlib.pyplot as plt
import numpy as np
from pybaselines import Baseline, utils

x = np.linspace(1, 1000, 1000)
# a measured signal containing several Gaussian peaks
signal = (
    utils.gaussian(x, 4, 120, 5)
    + utils.gaussian(x, 5, 220, 12)
    + utils.gaussian(x, 5, 350, 10)
    + utils.gaussian(x, 7, 400, 8)
...
```

Sections: pybaselines, Introduction, Dependencies, Quick Start, Citing

</details>

### kmodes

Python implementations of the k-modes and k-prototypes clustering algorithms for clustering categorical data.

`pip install kmodes` · installs (wheel) · licence: MIT License · rank 6609 · last release 2022-09-06 · [PyPI](https://pypi.org/project/kmodes/)

<details><summary>README extract</summary>

Python implementations of the k-modes and k-prototypes clustering
algorithms. Relies on numpy for a lot of the heavy lifting.

k-modes is used for clustering categorical variables. It defines clusters
based on the number of matching categories between data points. ...

Example:
```python
import numpy as np
from kmodes.kmodes import KModes

# random categorical data
data = np.random.choice(20, (100, 10))

km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)

clusters = km.fit_predict(data)

# Print the cluster centroids
print(km.cluster_centroids)
```

Sections: kmodes, Description, Usage, Parallel execution, FAQ, References

</details>

### numbagg

Fast N-dimensional aggregation functions with Numba

`pip install numbagg` · installs (wheel) · licence: not stated · rank 6752 · last release 2026-09-25 · [PyPI](https://pypi.org/project/numbagg/)

<details><summary>README extract</summary>

Fast, flexible N-dimensional array functions written with
Numba and NumPy's generalized
ufuncs.

Example:
```python
import numpy as np
from numba import float32, float64, int32, int64

from numbagg.decorators import ndaggregate

@ndaggregate.wrap(
    signature=[
        (int32[:], int32[:]),
        (int64[:], int64[:]),
        (float32[:], float32[:]),
        (float64[:], float64[:]),
    ]
)
def nansum(a, out):
    asum = a.dtype.type(0)
    for ai in a:
...
```

Sections: Why use numbagg?, Performance, Versatility, Functions & benchmarks, Summary benchmark, Full benchmarks, Axis parameter behavior, Aggregation functions, Moving window functions, Grouped functions, Matrix functions, Example implementation, Implementation details

</details>

### pygmsh

Python frontend for Gmsh

`pip install pygmsh` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6771 · last release 2022-01-28 · [PyPI](https://pypi.org/project/pygmsh/) · [docs](https://pygmsh.readthedocs.io/en/latest) · [source](https://github.com/nschloe/pygmsh)

_README extract left out: share-alike licence._

### pgmpy

Python Toolkit for Causal and Probabilistic Reasoning

`pip install pgmpy` · installs (wheel) · licence: not stated · rank 6805 · last release 2026-04-30 · [PyPI](https://pypi.org/project/pgmpy/) · [docs](https://www.pgmpy.org) · [source](https://github.com/pgmpy/pgmpy)

<details><summary>README extract</summary>

pgmpy provides the building blocks for causal and probabilistic reasoning using graphical models. It implements data structures for a range of causal and graphical models such as DAGs, PDAGs, MAGs, PAGs, Bayesian Networks, Dynamic Bayesian Networks, and Structural Equation Models, along with algorithms for various tasks such as causal discovery, ...

Features:
| Feature | Description |

| Causal Discovery / Structure Learning | Learn the model structure from data, with optional integration of expert knowledge. |
| Causal Validation | Assess how compatible the causal structure is with the data. ...

Example:
```python
from pgmpy.example_models import load_model

# Load a Discrete Bayesian Network and simulate data.
discrete_bn = load_model("bnlearn/alarm")
...

</details>

### lasio

Read/write well data from Log ASCII Standard (LAS) files

`pip install lasio` · installs (wheel) · licence: MIT License · rank 6820 · last release 2025-08-01 · [PyPI](https://pypi.org/project/lasio/)

<details><summary>README extract</summary>

Documentation (stable) •
Documentation (main branch)

Read and write Log ASCII Standard files with Python.

This is a Python 3.7+ package to read and write Log ASCII Standard
(LAS) files, used for borehole data such as geophysical, geological, or
petrophysical logs. ...

Example:
```python
>>> import lasio
```

Sections: lasio, Quick start

</details>

### obspy

ObsPy - a Python framework for seismological observatories.

`pip install obspy` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6833 · last release 2026-08-28 · [PyPI](https://pypi.org/project/obspy/) · [docs](https://docs.obspy.org/) · [source](https://github.com/obspy/obspy)

_README extract left out: share-alike licence._

### octave-kernel

'A Jupyter kernel for Octave.'

`pip install octave-kernel` · installs (wheel) · licence: BSD-3-Clause · rank 6858 · last release 2026-08-17 · [PyPI](https://pypi.org/project/octave-kernel/)

<details><summary>README extract</summary>

Jupyter Notebook and GNU Octave.

Sections: An Octave kernel for Jupyter, Prerequisites, Usage, Configuration, Managing the Octave Executable, Troubleshooting, Debugging the Kernel, Kernel Times Out While Starting, Kernel is Not Listed, Qt Backend Availability, Blank Plot

</details>

### oct2py

'Python to GNU Octave bridge --> run m-files from python.'

`pip install oct2py` · installs (wheel) · licence: MIT License · rank 6894 · last release 2026-08-23 · [PyPI](https://pypi.org/project/oct2py/) · [docs](https://blink1073.github.io/oct2py)

<details><summary>README extract</summary>

Oct2Py allows you to seamlessly call M-files and Octave functions from Python.
It manages the Octave session for you, sharing data behind the scenes using
MAT files. Usage is as simple as:

To run .m function, you need to explicitly add the path to .m file using:

To get the output of .m file after setting the path, use: ...

Features:
- Supports all Octave datatypes and most Python datatypes and Numpy dtypes.
- Provides OctaveMagic for IPython, including inline plotting in notebooks.
- Supports cell arrays and structs/struct arrays with arbitrary nesting. ...

Example:
```python
>>> import oct2py
>>> oc = oct2py.Oct2Py()
>>> x = oc.zeros(3, 3)
>>> print(x, x.dtype)
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]] float64
```

Sections: Oct2Py: Python to GNU Octave Bridge, Features, Documentation

</details>

### newton

A GPU-accelerated physics engine for robotics simulation

`pip install newton` · installs (wheel) · licence: Apache-2.0 · rank 6913 · last release 2026-10-14 · [PyPI](https://pypi.org/project/newton/)

<details><summary>README extract</summary>

Newton is a GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.

Newton extends and generalizes Warp's (deprecated) `warp.sim` module, and integrates
MuJoCo Warp as its primary backend. ...

Sections: Newton, Requirements, Quickstart, Examples, Basic Examples, Robot Examples, Controller Examples, Cable Examples, Cloth Examples, Inverse Kinematics Examples, MPM Examples, Sensor Examples, Selection Examples, DiffSim Examples

</details>

### dscribe

A Python package for creating feature transformations in applications of machine learning to materials science.

`pip install dscribe` · installs (wheel) · licence: Apache Software License · rank 6924 · last release 2025-09-27 · [PyPI](https://pypi.org/project/dscribe/) · [docs](https://singroup.github.io/dscribe/latest/) · [source](https://singroup.github.io/dscribe)

<details><summary>README extract</summary>

DScribe is a Python package for transforming atomic structures into fixed-size
numerical fingerprints. These fingerprints are often called "descriptors" and
they can be used in various tasks, including machine learning, visualization,
similarity analysis, etc.

For more details and tutorials, visit our documentation at: ...

Example:
```python
import numpy as np
from ase.build import molecule
from dscribe.descriptors import SOAP
from dscribe.descriptors import CoulombMatrix

# Define atomic structures
samples = [molecule("H2O"), molecule("NO2"), molecule("CO2")]

# Setup descriptors
cm_desc = CoulombMatrix(n_atoms_max=3, permutation="sorted_l2")
...
```

Sections: Documentation, Quick Example, Currently implemented descriptors, pip, conda, From source

</details>

### lalsuite

LVK Algorithm Library Suite - LALSuite

`pip install lalsuite` · installs (wheel) · licence: GPL-2.0-or-later · rank 6931 · last release 2026-10-31 · [PyPI](https://pypi.org/project/lalsuite/) · [docs](https://lscsoft.docs.ligo.org/lalsuite/8.0/) · [source](https://git.ligo.org/lscsoft/lalsuite)

_README extract left out: share-alike licence._

### rfdetr

RF-DETR

`pip install rfdetr` · installs (wheel) · licence: Apache Software License · rank 6949 · last release 2026-11-06 · [PyPI](https://pypi.org/project/rfdetr/)

<details><summary>README extract</summary>

RF-DETR is a real-time transformer architecture for object detection, instance segmentation, and keypoint detection (preview) developed by Roboflow. Built on a DINOv2 vision transformer backbone (a PE-Core-T backbone for Atto, Femto and Pico), RF-DETR delivers state-of-the-art accuracy and latency trade-offs on Microsoft COCO and RF100-VL. ...

Example:
```python
import supervision as sv
from rfdetr import RFDETRMedium
from rfdetr.assets.coco_classes import COCO_CLASSES

model = RFDETRMedium()

detections = model.predict(" threshold=0.5)

labels = [f"{COCO_CLASSES[class_id]}" for class_id in detections.class_id]

annotated_image = sv.BoxAnnotator().annotate(detections.metadata["source_image"], detections)
...
```

...

</details>

### control

Python Control Systems Library

`pip install control` · installs (wheel) · licence: BSD-3-Clause · rank 6963 · last release 2025-07-05 · [PyPI](https://pypi.org/project/control/) · [source](https://github.com/python-control/python-control)

<details><summary>README extract</summary>

The Python Control Systems Library is a Python module that implements basic
operations for analysis and design of feedback control systems.

Try out the examples in the examples folder using the binder service.

The package can also be installed on Google Colab using the commands:

Features:
- Linear input/output systems in state-space and frequency domain
- Block diagram algebra: serial, parallel, feedback, and other interconnections
- Time response: initial, step, impulse
- Frequency response: Bode, Nyquist, and Nichols plots ...

Example:
```python
%pip install control
import control as ct
```

Sections: Python Control Systems Library, Have a go now!, Features, Links, Dependencies, Conda and conda-forge, Pip, Code

</details>

### tflite-runtime

TensorFlow Lite is for mobile and embedded devices.

`pip install tflite-runtime` · does not install on CPython 3.14 · licence: Apache Software License · rank 6986 · last release 2023-10-03 · [PyPI](https://pypi.org/project/tflite-runtime/)

<details><summary>README extract</summary>

TensorFlow Lite is the official solution for running machine learning models on
mobile and embedded devices. It enables on-device machine learning inference
with low latency and a small binary size on Android, iOS, and other operating
systems.

</details>

### pydoe

Design of Experiments for Python

`pip install pydoe` · installs (wheel) · licence: BSD-3-Clause · rank 6990 · last release 2026-10-21 · [PyPI](https://pypi.org/project/pydoe/) · [docs](https://pydoe.github.io/pydoe/) · [source](https://github.com/pydoe/pydoe)

<details><summary>README extract</summary>

PyDOE is a Python package for design of experiments (DOE), enabling scientists, engineers, and statisticians to efficiently construct experimental designs.

Overview

The package provides extensive support for design-of-experiments (DOE) methods and is capable of creating designs for any number of factors.

It provides: ...

</details>

### polars-runtime-compat

Blazingly fast DataFrame library

`pip install polars-runtime-compat` · installs (wheel) · licence: MIT License · rank 7010 · last release 2026-10-25 · [PyPI](https://pypi.org/project/polars-runtime-compat/) · [docs](https://docs.pola.rs/api/python/stable/reference/index.html) · [source](https://github.com/pola-rs/polars)

<details><summary>README extract</summary>

Packages that contain the binary shared libraries that back the polars python package. Not meant for
general consumption and just meant as dependencies for the polars main package.

</details>

### audioseal

Watermarking and detection for speech audios

`pip install audioseal` · installs (wheel) · licence: MIT License · rank 7016 · last release 2026-11-03 · [PyPI](https://pypi.org/project/audioseal/) · [source](https://github.com/facebookresearch/audioseal)

<details><summary>README extract</summary>

This repo contains the official implementation for AudioSeal, a method for efficient audio watermarking, with state-of-the-art robustness and detector speed.

[`arXiv`]
[🤗`Hugging Face`]
[`Colab Notebook`]
[`Webpage`]
[`Blog`]
[`Press`]

- 2024-12-12: AudioSeal 0.2 is out, with streaming support and other improvement ...

Example:
```python
from audioseal import AudioSeal

# model name corresponds to the YAML card file name found in audioseal/cards
model = AudioSeal.load_generator("audioseal_wm_16bits")
model.eval()

# Other way is to load directly from the checkpoint
# model =  Watermarker.from_pretrained(checkpoint_path, device = wav.device)

...
```

...

</details>

### ruckig

Instantaneous Motion Generation for Robots and Machines.

`pip install ruckig` · installs (wheel) · licence: MIT License · rank 7057 · last release 2026-07-15 · [PyPI](https://pypi.org/project/ruckig/) · [docs](https://docs.ruckig.com) · [source](https://github.com/pantor/ruckig.git)

<details><summary>README extract</summary>

Ruckig generates trajectories on-the-fly, allowing robots and machines to react instantaneously to sensor input. Ruckig calculates a trajectory to a *target* waypoint (with position, velocity, and acceleration) starting from *any* initial state limited by velocity, acceleration, and jerk constraints. ...

Example:
```python
Abs(acceleration) <= Sqrt(2 * max_jerk * (max_velocity - Abs(velocity))).
```

Sections: Ruckig, Instantaneous Motion Generation for Robots and Machines., Tutorial, Waypoint-based Trajectory Generation, Intermediate Waypoints, Input Parameter, Input Validation, Result Type, Output Parameter, Offline Calculation, Tracking Interface, Dynamic Number of Degrees of Freedom, Custom Vector Types, Tests and Numerical Stability

</details>

### pyiqa

PyTorch Toolbox for Image Quality Assessment

`pip install pyiqa` · installs (wheel) · licence: PolyForm-Noncommercial-1.0.0 · rank 7070 · last release 2026-07-08 · [PyPI](https://pypi.org/project/pyiqa/) · [source](https://github.com/chaofengc/IQA-PyTorch)

<details><summary>README extract</summary>

🚀 Install with `pip install pyiqa`

This is a comprehensive image quality assessment (IQA) toolbox built with pure Python and PyTorch. We provide reimplementation of many widely used full reference (FR) and no reference (NR) metrics, with results calibrated against official MATLAB scripts when available. ...

Example:
```python
import pyiqa
import torch

# list all available metrics
print(pyiqa.list_models())

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

# create metric with default setting
iqa_metric = pyiqa.create_metric('lpips', device=device)

# check if lower better or higher better
print(iqa_metric.lower_better)

...
```

...

</details>

### numpy-groupies

Optimised tools for group-indexing operations: aggregated sum and more.

`pip install numpy-groupies` · installs (wheel) · licence: BSD-2-Clause · rank 7134 · last release 2026-11-05 · [PyPI](https://pypi.org/project/numpy-groupies/) · [source](https://github.com/ml31415/numpy-groupies)

<details><summary>README extract</summary>

Fast group-by aggregation on plain NumPy arrays.
Give it values and a group label for each value, get back one result per group — sum, mean, std, median, min/max, argmax, cumulative sums, custom functions and more. No DataFrame required, with an optional Numba backend for speed. ...

Features:
- Fast. With Numba installed, `aggregate` is the fastest group-by aggregation for plain NumPy arrays. See Performance.
- One call, many functions. ...

Example:
```python
npg.aggregate(group_idx, 1)  # items per group
npg.aggregate(group_idx, a, func="mean")  # nan for the empty group 2
npg.aggregate(group_idx, a, func="mean", fill_value=-1)
```

...

</details>

### sfepy

SfePy: Simple finite elements in Python

`pip install sfepy` · installs from source (sdist only) · licence: BSD License · rank 7149 · last release 2026-09-29 · [PyPI](https://pypi.org/project/sfepy/)

<details><summary>README extract</summary>

SfePy (simple finite elements in Python) is a software, distributed
under the BSD license, for solving systems of coupled partial
differential equations by the finite element method. The code is based
on NumPy and SciPy packages.

</details>

### airbyte-protocol-models-pdv2

Declares the Airbyte Protocol.

`pip install airbyte-protocol-models-pdv2` · installs (wheel) · licence: MIT License · rank 7155 · last release 2025-06-27 · [PyPI](https://pypi.org/project/airbyte-protocol-models-pdv2/) · [docs](https://docs.airbyte.io/) · [source](https://github.com/airbytehq/airbyte-protocol)

### DoubleMetaphone

Python wrapper for C++ Double Metaphone

`pip install DoubleMetaphone` · installs from source (sdist only) · licence: Artistic License · rank 7160 · last release 2025-05-11 · [PyPI](https://pypi.org/project/DoubleMetaphone/)

### stumpy

A powerful and scalable library that can be used for a variety of time series data mining tasks

`pip install stumpy` · installs (wheel) · licence: BSD-3-Clause · rank 7162 · last release 2026-02-08 · [PyPI](https://pypi.org/project/stumpy/) · [docs](https://stumpy.readthedocs.io/en/latest/) · [source](https://github.com/stumpy-dev/stumpy)

<details><summary>README extract</summary>

STUMPY is a powerful and scalable Python library that efficiently computes something called the matrix profile, which is just an academic way of saying "for every (green) subsequence within your time series, automatically identify its corresponding nearest-neighbor (grey)": ...

Example:
```python
import stumpy
import numpy as np

if name == "main":
    your_time_series = np.random.rand(10000)
    window_size = 50  # Approximately, how many data points might be found in a pattern

    matrix_profile = stumpy.stump(your_time_series, m=window_size)
```

Sections: STUMPY, How to use STUMPY, Dependencies, Where to get it, Documentation, Performance, Hardware Resources, Running Tests, Python Version, Getting Help, Citing, References

</details>

### ConfigSpace

Creation and manipulation of parameter configuration spaces for automated algorithm configuration and hyperparameter tuning.

`pip install ConfigSpace` · installs (wheel) · licence: BSD License · rank 7218 · last release 2025-12-19 · [PyPI](https://pypi.org/project/ConfigSpace/) · [docs](https://automl.github.io/ConfigSpace/main/)

<details><summary>README extract</summary>

A simple Python module implementing a domain specific language to manage
configuration spaces for algorithm configuration and hyperparameter optimization tasks.
Distributed under BSD 3-clause, see LICENSE except all files in the directory
ConfigSpace.nx, which are copied from the networkx package and licensed
under a BSD license. ...

Example:
```python
from ConfigSpace import ConfigurationSpace

cs = ConfigurationSpace(
    name="myspace",
    space={
        "a": (0.1, 1.5),  # UniformFloat
        "b": (2, 10),  # UniformInt
        "c": ["mouse", "cat", "dog"],  # Categorical
    },
)

configs = cs.sample_configuration(2)
```

Sections: ConfigSpace, Minimum Example, Citing the ConfigSpace

</details>

### libcuml-cu12

cuML - RAPIDS ML Algorithms (C++)

`pip install libcuml-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7223 · last release 2026-10-08 · [PyPI](https://pypi.org/project/libcuml-cu12/)

<details><summary>README extract</summary>

NVIDIA cuML is an open-source CUDA-X Data Science library for
GPU-accelerated machine learning. It provides two ways to run machine learning
workloads on NVIDIA GPUs:

- The `cuml` Python API provides GPU-native estimators with familiar
 scikit-learn-style APIs and direct control over machine learning workflows. ...

Example:
```python
from cuml.datasets import make_blobs
from cuml.cluster import DBSCAN

# Create sample data
X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)

# Fit clustering model
dbscan = DBSCAN(eps=1.0, min_samples=5)
dbscan.fit(X)
print(dbscan.labels)
```

Sections: NVIDIA cuML: GPU-Accelerated Machine Learning, Use the GPU-native `cuml` API, Accelerate existing code with `cuml.accel`, Scale beyond one GPU, Scikit-learn compatibility

</details>

### azureml-dataprep

Azure ML Data Preparation SDK is used to load, transform, and write data for machine learning workflows

`pip install azureml-dataprep` · installs (wheel) · licence: Other/Proprietary License · rank 7281 · last release 2026-07-27 · [PyPI](https://pypi.org/project/azureml-dataprep/)

<details><summary>README extract</summary>

The Azure Machine Learning Data Prep SDK is used to load, transform, and write data for machine learning workflows.

This package is internal, and is not intended to be used directly.

</details>

### qutip

QuTiP: The Quantum Toolbox in Python

`pip install qutip` · installs (wheel) · licence: BSD-3-Clause · rank 7317 · last release 2026-08-04 · [PyPI](https://pypi.org/project/qutip/) · [docs](https://qutip.readthedocs.io/en/stable/) · [source](https://github.com/qutip/qutip)

<details><summary>README extract</summary>

A. Pitchford,
C. Granade,
A. Grimsmo,
N. Shammah,
S. Ahmed,
N. Lambert,
E. Giguère,
B. Li,
J. Lishman,
S. Cross,
A. Galicia,
P. Menczel,
P. Hopf,
P. D. Nation,
and J. R. Johansson

QuTiP is open-source software for simulating the dynamics of closed and open quantum systems. ...

</details>

### tabpfn

TabPFN: Foundation model for tabular data

`pip install tabpfn` · installs (wheel) · licence: Apache-2.0 · rank 7332 · last release 2026-10-12 · [PyPI](https://pypi.org/project/tabpfn/) · [docs](https://priorlabs.ai/docs) · [source](https://github.com/priorlabs/tabpfn)

<details><summary>README extract</summary>

Example:
```python
from tabpfn import TabPFNClassifier, TabPFNRegressor

clf = TabPFNClassifier()
clf.fit(X_train, y_train)  # downloads checkpoint on first use
predictions = clf.predict(X_test)

reg = TabPFNRegressor()
reg.fit(X_train, y_train)  # downloads checkpoint on first use
predictions = reg.predict(X_test)
```

Sections: TabPFN, Quick Start, Interactive Notebook Tutorial, Basic Usage, TabPFN Ecosystem, Enterprise & Production, Usage Tips, ❓ FAQ, Usage & Compatibility, Performance & Limitations

</details>

### nvidia-npp-cu12

NPP native runtime libraries

`pip install nvidia-npp-cu12` · installs (wheel) · licence: Other/Proprietary License · rank 7389 · last release 2025-06-05 · [PyPI](https://pypi.org/project/nvidia-npp-cu12/)

### fatfs-ng

Enhanced Python wrapper around ChaN's FatFS library - Fork of fatfs-python with extended features.

`pip install fatfs-ng` · installs (wheel) · licence: MIT License · rank 7432 · last release 2026-10-19 · [PyPI](https://pypi.org/project/fatfs-ng/) · [docs](https://github.com/Jason2866/pyfatfs)

<details><summary>README extract</summary>

Enhanced Python wrapper around ChaN's FatFS library with extended features and ESP32 support.

This is a fork of fatfs-python by Ladislav Laska, with significant improvements and extended functionality.

- ✅ Complete Directory Traversal: `walk()`, `listdir()`, `stat()`
- ✅ Path Operations: `exists()`, `isfile()`, `isdir()` ...

Example:
```python
from fatfs import RamDisk, create_extended_partition

# Create and format filesystem
storage = bytearray(1024 * 1024)  # 1MB
disk = RamDisk(storage, sector_size=512)
partition = create_extended_partition(disk)
partition.mkfs()
partition.mount()

# Use extended features
partition.makedirs("/test/dir", exist_ok=True)
...
```

...

</details>

### npTDMS

Cross-platform, NumPy based module for reading TDMS files produced by LabView

`pip install npTDMS` · installs (wheel) · licence: LGPL-3.0-only · rank 7436 · last release 2026-11-07 · [PyPI](https://pypi.org/project/npTDMS/) · [docs](https://npTDMS.readthedocs.io) · [source](https://github.com/adamreeve/npTDMS)

_README extract left out: share-alike licence._

### vector

Vector classes and utilities

`pip install vector` · installs (wheel) · licence: BSD-3-Clause · rank 7449 · last release 2026-09-20 · [PyPI](https://pypi.org/project/vector/) · [docs](https://vector.readthedocs.io/)

<details><summary>README extract</summary>

[][zenodo-link]
[][joss-link]
[][sk-link]

[][actions-link]
[][actions-link]
[][rtd-link]
[][pre-commit-link]
[][codecov-link]

[][pypi-link]
[][pypi-link]
[][conda-link]

[][license-link]
[][github-discussions-link]
[][gitter-link]

Sections: Vector: arrays of 2D, 3D, and Lorentz vectors, Introduction, Coordinate systems, Backends, Integrations, Geometric versus momentum, Familiar conventions, Getting help, Citing Vector, Documentation, Tutorials, Vector constructors, Vector functions

</details>

### sax

Autograd and XLA for S-parameters

`pip install sax` · installs (wheel) · licence: Apache Software License · rank 7491 · last release 2026-06-09 · [PyPI](https://pypi.org/project/sax/)

<details><summary>README extract</summary>

> 0.18.2

SAX: S-Matrices with Autograd and XLA - a scatter parameter circuit simulator and
optimizer for the frequency domain based on JAX.

The simulator was developed for simulating Photonic Integrated Circuits but in fact is
able to perform any S-parameter based circuit simulation. ...

Example:
```python
import sax
import jax
import jax.numpy as jnp
```

Sections: SAX, Quick Start

</details>

### scikit-survival

Survival analysis built on top of scikit-learn

`pip install scikit-survival` · installs (wheel) · licence: GPL-3.0-or-later · rank 7547 · last release 2026-07-05 · [PyPI](https://pypi.org/project/scikit-survival/) · [docs](https://scikit-survival.readthedocs.io) · [source](https://github.com/sebp/scikit-survival)

_README extract left out: share-alike licence._

### openpulse

Reference OpenPulse AST in Python

`pip install openpulse` · installs (wheel) · licence: Apache Software License · rank 7611 · last release 2024-10-01 · [PyPI](https://pypi.org/project/openpulse/)

<details><summary>README extract</summary>

<!-- long-description-skip-begin --><!-- long-description-skip-end -->

OpenPulse is a concrete implementation of pulse grammar for `cal` and `defcal` body.
It reuses the classical types and statements from openqasm3.

The package is structured similarly to `openqasm3` with the modules:

* `openpulse.ast`: The AST nodes. ...

</details>

### pylibftdi

Pythonic interface to FTDI devices using libftdi.

`pip install pylibftdi` · installs (wheel) · licence: MIT · rank 7632 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pylibftdi/) · [docs](https://pylibftdi.readthedocs.io/en/latest/) · [source](https://github.com/codedstructure/pylibftdi)

<details><summary>README extract</summary>

pylibftdi is a minimal Pythonic interface to FTDI devices using libftdi.

:Features:

 - No dependencies beyond standard library and a `libftdi` install.
 - Supports parallel and serial devices
 - Support for multiple devices
 - File-like interface wherever appropriate
 - Cross-platform

Example:
```python
>>> from pylibftdi import Device
>>>
>>> with Device(mode='t') as dev:
...     dev.baudrate = 115200
...     dev.write('Hello World')
```

Sections: pylibftdi, Usage, Examples, Plans

</details>

### mxnet

Apache MXNet is an ultra-scalable deep learning framework. This version uses openblas and MKLDNN.

`pip install mxnet` · installs (wheel) · licence: Apache Software License · rank 7652 · last release 2022-05-17 · [PyPI](https://pypi.org/project/mxnet/)

<details><summary>README extract</summary>

Apache MXNet is a deep learning framework designed for both *efficiency* and *flexibility*.
It allows you to mix the flavours of deep learning programs together to maximize the efficiency and your productivity.

For feature requests on the PyPI package, suggestions, and issue reports, create an issue by clicking here.
Prerequisites ...

</details>

### pylibmagic

scikit-build project with CMake for compiling libmagic

`pip install pylibmagic` · installs (wheel) · licence: BSD License · rank 7668 · last release 2023-10-19 · [PyPI](https://pypi.org/project/pylibmagic/) · [docs](https://pylibmagic.readthedocs.io/)

<details><summary>README extract</summary>

A lightweight, minimal python package that ships `magic` libraries
using automake, CMake, scikit-build, and cibuildwheel.

 |Code style: black|

Features:
If you use python-magic, you typically get an error like this

which is frustrating because they don’t ship shared lib with their
python distribution. ...

Example:
```python
>>> import magic
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kratsg/.pyenv/versions/venv/lib/python3.7/site-packages/magic/init.py", line 209, in <module>
    libmagic = loader.load_lib()
  File "/Users/kratsg/.pyenv/versions/venv/lib/python3.7/site-packages/magic/loader.py", line 49, in load_lib
...
```

Sections: pylibmagic v0.5.0, Why?, Compiling, Releasing

</details>

### aistore

Client-side APIs to access and utilize clusters, buckets, and objects on AIStore.

`pip install aistore` · installs (wheel) · licence: MIT · rank 7689 · last release 2026-10-28 · [PyPI](https://pypi.org/project/aistore/) · [docs](https://aistore.nvidia.com/docs/python-sdk) · [source](https://github.com/NVIDIA/aistore/tree/main/python/aistore/sdk)

<details><summary>README extract</summary>

This package contains the AIStore Python SDK, PyTorch integration, and Botocore patch.
See the README files in each module for usage details:

- SDK
- PyTorch
- Botocore

* AIStore GitHub
* Documentation
* AIStore pip package
* KubeCon 2024 presentation

Sections: AIS Python Components, References

</details>

### spsdk

Open Source Secure Provisioning SDK for NXP MCU/MPU

`pip install spsdk` · installs (wheel) · licence: BSD-3-Clause · rank 7692 · last release 2026-11-03 · [PyPI](https://pypi.org/project/spsdk/) · [docs](https://spsdk.readthedocs.io) · [source](https://github.com/NXPmicro/spsdk)

<details><summary>README extract</summary>

Secure Provisioning SDK (SPSDK) enables connection and communication with target devices for purposes of secure provisioning and programming. Delivered as python library with command-line applications for direct utilization.

* GitHub
* PyPi
* Documentation
* Project page

Sections: NXP Secure Provisioning SDK, Links, Usage, Dependencies

</details>

### azureml-dataprep-rslex

Azure ML Data Preparation RustLex

`pip install azureml-dataprep-rslex` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 7714 · last release 2026-09-18 · [PyPI](https://pypi.org/project/azureml-dataprep-rslex/)

<details><summary>README extract</summary>

Azure Machine Learning Data Prep RsLex is a Rust implementation of Data Prep's capabilities to load, transform, and write data for machine learning workflows.
You can interact with RsLex via the Data Prep SDK, `azureml-dataprep`, by calling `use_rust_execution(True)` before using the SDK.

</details>

### connected-components-3d

Connected components on discrete and continuous multilabel 3D and 2D images. Handles 26, 18, and 6 connected variants; periodic boundaries (4, 8, & 6).

`pip install connected-components-3d` · installs (wheel) · licence: LGPL-3.0-or-later · rank 7756 · last release 2026-10-24 · [PyPI](https://pypi.org/project/connected-components-3d/)

_README extract left out: share-alike licence._

### MAPIE

A scikit-learn-compatible module for estimating prediction intervals.

`pip install MAPIE` · installs (wheel) · licence: BSD-3-Clause · rank 7782 · last release 2026-10-19 · [PyPI](https://pypi.org/project/MAPIE/) · [docs](https://mapie.readthedocs.io/en/latest/) · [source](https://github.com/scikit-learn-contrib/MAPIE)

<details><summary>README extract</summary>

An open-source Python library for quantifying uncertainties and controlling the risks of machine learning models.

🚀 MAPIE in 2026 🚀 New features have been implemented, starting with the application of risk control to emerging use cases such as LLM-as-Judge and image segmentation. ...

Sections: MAPIE - Model Agnostic Prediction Interval Estimator, ⚡ Quickstart and documentation, 🔍 References, 🤝 Affiliations

</details>

### hydra-zen

Configurable, reproducible, and scalable workflows in Python, via Hydra

`pip install hydra-zen` · installs (wheel) · licence: MIT License · rank 7807 · last release 2026-10-21 · [PyPI](https://pypi.org/project/hydra-zen/) · [source](https://github.com/mit-ll-responsible-ai/hydra-zen)

<details><summary>README extract</summary>

A library that facilitates configurable, reproducible, and scalable workflows, using Hydra.

 Check out our documentation for more information.

 Interested in machine learning? Check out our guide for using PyTorch Lightning with hydra-zen.⚡ ...

Sections: hydra-zen, Join the Discussion, Disclaimer

</details>

### dtw-python

A comprehensive implementation of dynamic time warping (DTW) algorithms.

`pip install dtw-python` · installs (wheel) · licence: GPL-3.0-or-later · rank 7814 · last release 2026-10-08 · [PyPI](https://pypi.org/project/dtw-python/) · [docs](https://dynamictimewarping.github.io/python/) · [source](https://github.com/DynamicTimeWarping/dtw-python)

_README extract left out: share-alike licence._

### azureml-dataprep-native

Contains package for AzureML DataPrep specific native extensions.

`pip install azureml-dataprep-native` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 7816 · last release 2026-07-27 · [PyPI](https://pypi.org/project/azureml-dataprep-native/)

<details><summary>README extract</summary>

Specific native code extensions for package azureml-dataprep

</details>

### iapws

Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam

`pip install iapws` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7854 · last release 2026-03-27 · [PyPI](https://pypi.org/project/iapws/)

_README extract left out: share-alike licence._

### correctionlib

A generic correction library

`pip install correctionlib` · installs (wheel) · licence: BSD License · rank 7865 · last release 2026-06-16 · [PyPI](https://pypi.org/project/correctionlib/)

<details><summary>README extract</summary>

[][actions-link]
[][rtd-link]
[][black-link]

[][conda-link]
[][pypi-link]
[][pypi-link]

[][github-discussions-link]

The purpose of this library is to provide a well-structured JSON data format for
a wide variety of ad-hoc correction factors encountered in a typical HEP
analysis and a companion evaluation tool suitable for use in C++ and ...

Example:
```python
def f(*args: str | int | float) -> float:
    return ...
```

Sections: correctionlib, Introduction, Creating new corrections, Compatibility

</details>

### depthai

DepthAI Python Library

`pip install depthai` · installs (wheel) · licence: MIT · rank 7883 · last release 2026-11-03 · [PyPI](https://pypi.org/project/depthai/)

<details><summary>README extract</summary>

Python bindings for C++ depthai-core library

Documentation is available over at Luxonis DepthAI API

Example:
```python
export PYTHONPATH=$(pwd)/build/bindings/python
# Confirm that the right shared library is loaded
python3 -c "import depthai as dai; print(dai.file)"
# It should print the path to the shared library, something like /path/to/depthai-core/build/bindings/python/depthai.cpython-38-x86_64-linux-gnu.so
```

Sections: DepthAI Python Library, Documentation, Building from source, Dependencies, Building, Local build with pip, Wheel with pip, Shared library, Common issues, Running tests, Checking new Python bindings without a build, Running the compiled tests, Tested platforms, Building documentation

</details>

### tdigest

T-Digest data structure

`pip install tdigest` · installs (wheel) · licence: MIT License · rank 7884 · last release 2019-05-07 · [PyPI](https://pypi.org/project/tdigest/)

<details><summary>README extract</summary>

This is a Python implementation of Ted Dunning's t-digest data structure. The t-digest data structure is designed around computing accurate estimates from either streaming data, or distributed data. These estimates are percentiles, quantiles, trimmed means, etc. ...

Example:
```python
from tdigest import TDigest
from numpy.random import random

digest = TDigest()
for x in range(5000):
    digest.update(random())

print(digest.percentile(15))  # about 0.15, as 0.15 is the 15th percentile of the Uniform(0,1) distribution
```

Sections: tdigest, Usage, Update the digest sequentially, Update the digest in batches, Sum two digests to create a new digest, To dict or serializing a digest with JSON, API

</details>

### libusbsio

Python wrapper around NXP LIBUSBSIO library

`pip install libusbsio` · installs (wheel) · licence: BSD-3-Clause · rank 7935 · last release 2026-06-25 · [PyPI](https://pypi.org/project/libusbsio/)

<details><summary>README extract</summary>

The NXP libusbsio
is a binary library for Win/Linux/MacOS systems used to exercise SPI, I2C bus and GPIO pins over USBSIO interface of NXP
LPCLink2
and MCUlink Pro
devices.

This Python component provides a wrapper object which encapsulates the binary library
and exposes its API to Python applications.

Author: michal.hanak@nxp.com ( ...

Example:
```python
from libusbsio import *
sio = LIBUSBSIO()
```

Sections: Python wrapper for NXP libusbsio binary library, Dependencies, pypi.org, Local, Running example code, Running test code, v2.2.1 - June 2026, v2.2.0 - October 2025, v2.1.13 - October 2024, v2.1.12 - January 2023, v2.1.11 - February 2022, v2.1.10 - February 2022, v2.1.8 - November 2021, v2.1.5 - August 2021

</details>

### mujoco-mjx

MuJoCo XLA (MJX)

`pip install mujoco-mjx` · installs (wheel) · licence: Apache-2.0 · rank 7940 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mujoco-mjx/) · [docs](https://mujoco.readthedocs.io/en/4.0.0) · [source](https://github.com/google-deepmind/mujoco/tree/main/mjx)

<details><summary>README extract</summary>

[][pypi]
[][pypi]

This package is a re-implementation of the
MuJoCo physics engine in
JAX. This library is developed and maintained
by Google DeepMind, and is kept up-to-date with the latest developments in
MuJoCo itself.

The `mujoco-mjx` package is API-compatible with MuJoCo, but is missing some
features found in MuJoCo. ...

Sections: MuJoCo XLA (MJX), Usage, Versioning

</details>

### hera-workflows

Hera makes Python code easy to orchestrate on Argo Workflows through native Python integrations. It lets you construct and submit your Workflows entirely in Python.

`pip install hera-workflows` · installs (wheel) · licence: Apache Software License · rank 7947 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hera-workflows/) · [docs](https://hera.readthedocs.io/en/stable/) · [source](https://github.com/argoproj-labs/hera)

<details><summary>README extract</summary>

| | Hera is the go-to Python SDK to make Argo Workflows simple and intuitive. Easily turn Python functions into containerised templates that run on Kubernetes, with full access to its capabilities. |

See the Quick Start guide to start using Hera to
orchestrate your Argo Workflows!

Example:
```python
from hera.workflows import DAG, Workflow, script

# Turn a function into a reusable "Script template"
# using the script decorator
@script()
def echo(message: str):
    print(message)

# Orchestration logic lives *outside* of business logic
with Workflow(
    generate_name="dag-diamond-",
    entrypoint="diamond",
) as w:
...
```

...

</details>

### onnxruntime-openvino

ONNX Runtime is a runtime accelerator for Machine Learning models

`pip install onnxruntime-openvino` · does not install on CPython 3.14 · licence: MIT License · rank 7965 · last release 2026-02-26 · [PyPI](https://pypi.org/project/onnxruntime-openvino/)

<details><summary>README extract</summary>

OpenVINO™ Execution Provider for ONNX Runtime is a product designed for ONNX Runtime developers who want to get started with OpenVINO™ in their inferencing applications. This product delivers OpenVINO™ inline optimizations which enhance inferencing performance with minimal code modifications. ...

Sections: OpenVINO™ Execution Provider for ONNX Runtime, Requirements, Usage, Samples

</details>

### poutyne

A simplified framework and utilities for PyTorch.

`pip install poutyne` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 7972 · last release 2026-06-07 · [PyPI](https://pypi.org/project/poutyne/) · [source](https://github.com/freud14/poutyne)

_README extract left out: share-alike licence._

### scikit-learn-intelex

Intel® Extension for Scikit-learn is a seamless way to speed up your Scikit-learn application.

`pip install scikit-learn-intelex` · installs (wheel) · licence: Apache-2.0 · rank 7978 · last release 2026-10-16 · [PyPI](https://pypi.org/project/scikit-learn-intelex/) · [docs](https://uxlfoundation.github.io/scikit-learn-intelex/) · [source](https://github.com/uxlfoundation/scikit-learn-intelex)

<details><summary>README extract</summary>

Extension for Scikit-learn is a free software AI accelerator designed to deliver over 10-100X acceleration to your existing scikit-learn code.
The software acceleration is achieved with vector instructions, AI hardware-specific memory optimizations, threading, and optimizations.

With Extension for Scikit-learn, you can: ...

Example:
```python
import numpy as np
from sklearnex.cluster import DBSCAN

X = np.array([[1., 2.], [2., 2.], [2., 3.],
              [8., 7.], [8., 8.], [25., 80.]], dtype=np.float32)
clustering = DBSCAN(eps=3, min_samples=2).fit(X)
```

Sections: Intel(R) Extension for Scikit-learn, ⚡️ Get Started, Usage without patching, 🚀 Scikit-learn patching, 👀 Follow us on Medium, 🔗 Important links

</details>

### pyrnnoise

PyRnNoise

`pip install pyrnnoise` · installs (wheel) · licence: not stated · rank 7997 · last release 2026-09-23 · [PyPI](https://pypi.org/project/pyrnnoise/)

<details><summary>README extract</summary>

Python bindings for RNNoise, a recurrent neural network for audio noise reduction.

Features:
- Real-time noise suppression for speech audio
- Command-line interface for processing audio files
- Supports mono and stereo audio files
- Visualize voice activity detection probabilities

Example:
```python
import numpy as np
from pyrnnoise import RNNoise

# Create denoiser instance
denoiser = RNNoise(sample_rate=48000)

# Generate or load some audio data (stereo in this example)
audio_data = np.random.randint(-32768, 32767, (2, 48000), dtype=np.int16)

# Process audio chunk
for speech_prob, denoised_audio in denoiser.denoise_chunk(audio_data):
...
```

Sections: pyrnnoise, Features, Usage, Command-line interface, Python API, Advanced Usage, Build from source

</details>

### mplhep-data

Font (Data) sub-package for mplhep

`pip install mplhep-data` · installs (wheel) · licence: MIT · rank 8017 · last release 2026-06-04 · [PyPI](https://pypi.org/project/mplhep-data/)

<details><summary>README extract</summary>

[][actions-link]
[][pypi-link]
[][conda-link]
[](

Sub-package to hold data (fonts) for mplhep.

Fonts distributed in this package have open licenses and can be redistributed. While it
would be preferable to download the files from their original repositories, there is no
convenient way to do that due to varying repo structures. ...

Sections: mplhep_data, Fonts, Tex Gyre Heros, Tex Gyre Termes, Fira Sans, Fira Math

</details>

### deepparse

A library for parsing multinational street addresses using deep learning.

`pip install deepparse` · installs (wheel) · licence: MIT License · rank 8027 · last release 2026-11-02 · [PyPI](https://pypi.org/project/deepparse/)

<details><summary>README extract</summary>

Deepparse is a state-of-the-art library for parsing multinational street addresses using deep learning.

Use deepparse to

- parse multinational address using one of our pretrained models with or without attention mechanism,
- parse addresses directly from the command line without code to write, ...

Example:
```python
from deepparse.parser import AddressParser
from deepparse.dataset_container import CSVDatasetContainer

address_parser = AddressParser(model_type="bpemb", device=0)

# you can parse one address
parsed_address = address_parser("350 rue des Lilas Ouest Québec Québec G1L 1B6")

# or multiple addresses
parsed_address = address_parser(
    [
...
```

...

</details>

### tf-keras-nightly

Deep learning for humans.

`pip install tf-keras-nightly` · installs (wheel) · licence: Apache Software License · rank 8062 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tf-keras-nightly/)

<details><summary>README extract</summary>

TF-Keras is a deep learning API written in Python,
running on top of the machine learning platform TensorFlow.

It was developed with a focus on enabling fast experimentation and
providing a delightful developer experience.
The purpose of TF-Keras is to give an *unfair advantage* to any developer
looking to ship ML-powered apps.

</details>

### empyrical-reloaded

empyrical computes performance and risk statistics commonly used in quantitative finance

`pip install empyrical-reloaded` · installs (wheel) · licence: Apache-2.0 · rank 8079 · last release 2026-11-02 · [PyPI](https://pypi.org/project/empyrical-reloaded/) · [docs](https://empyrical.ml4trading.io) · [source](https://github.com/stefan-jansen/empyrical-reloaded)

<details><summary>README extract</summary>

Common financial return and risk metrics in Python.

We continue to maintain Empyrical Reloaded for bug, security, and compatibility fixes.
Our new feature development focuses on ML4T Diagnostic,
part of the ML4T libraries.
For new projects, start with Diagnostic's maintained
Empyrical migration guide
and published documentation. ...

Example:
```python
import numpy as np
from empyrical import max_drawdown, alpha_beta

returns = np.array([.01, .02, .03, -.4, -.06, -.02])
benchmark_returns = np.array([.02, .02, .03, -.35, -.05, -.01])

# calculate the max drawdown
max_drawdown(returns)

# calculate alpha and beta
alpha, beta = alpha_beta(returns, benchmark_returns)
```

...

</details>

### torch-tb-profiler

PyTorch Profiler TensorBoard Plugin

`pip install torch-tb-profiler` · installs (wheel) · licence: BSD License · rank 8095 · last release 2023-10-06 · [PyPI](https://pypi.org/project/torch-tb-profiler/)

### coffea

Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.

`pip install coffea` · installs (wheel) · licence: BSD License · rank 8118 · last release 2026-09-13 · [PyPI](https://pypi.org/project/coffea/)

<details><summary>README extract</summary>

Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.

coffea is a prototype package for pulling together all the typical needs
of a high-energy collider physics (HEP) experiment analysis using the scientific
Python ecosystem. ...

Sections: Columnar Object Framework For Effective Analysis, Strict dependencies, Documentation

</details>

### plotly-stubs

Type stubs for plotly.

`pip install plotly-stubs` · installs (wheel) · licence: MIT License · rank 8146 · last release 2026-08-24 · [PyPI](https://pypi.org/project/plotly-stubs/) · [docs](https://ClaasRostock.github.io/plotly-stubs/README.html) · [source](https://github.com/ClaasRostock/plotly-stubs.git)

<details><summary>README extract</summary>

[][plotly_stubs_docs]

plotly-stubs is a stub-only package containing static type annotations for plotly.

Sections: plotly-stubs, Usage, 2. Clone the repository, 4. (Optional) Activate the virtual environment, Meta

</details>

### ibis-substrait

Subtrait compiler for ibis

`pip install ibis-substrait` · installs (wheel) · licence: Apache Software License · rank 8168 · last release 2024-07-29 · [PyPI](https://pypi.org/project/ibis-substrait/) · [source](https://github.com/ibis-project/ibis-substrait)

<details><summary>README extract</summary>

This repo houses the Substrait compiler for ibis.

We're just getting started here, so stay tuned!

Example:
```python
>>> import ibis

>>> t = ibis.table(
    [("a", "string"), ("b", "float"), ("c", "int32"), ("d", "int64"), ("e", "int64")],
    "t",
)

>>> expr = t.group_by(["a", "b"]).aggregate([t.c.sum().name("sum")]).select("b", "sum")
>>> expr
r0 := UnboundTable: t
  a string
  b float64
  c int32
  d int64
  e int64

r1 := Aggregation[r0]
  metrics:
...
```

Sections: Ibis + Substrait, Usage

</details>

### probablepeople

Parse romanized names & companies using advanced NLP methods

`pip install probablepeople` · installs (wheel) · licence: MIT License · rank 8171 · last release 2024-10-29 · [PyPI](https://pypi.org/project/probablepeople/)

<details><summary>README extract</summary>

probablepeople is a python library for parsing unstructured romanized name or company strings into components, using advanced NLP methods. This is based off usaddress, a python library for parsing addresses.

Try it out on our web interface! For those who aren't python developers, we also have an API. ...

Example:
```python
import probablepeople as pp
name_str='Mr George "Gob" Bluth II'
corp_str='Sitwell Housing Inc'

# The parse method will split your string into components, and label each component.
pp.parse(name_str) # expected output: [('Mr', 'PrefixMarital'), ('George', 'GivenName'), ('"Gob"', 'Nickname'), ('Bluth', 'Surname'), ('II', 'SuffixGenerational')]
...
```

...

</details>

### polars-runtime-64

Blazingly fast DataFrame library

`pip install polars-runtime-64` · installs (wheel) · licence: MIT License · rank 8219 · last release 2026-10-25 · [PyPI](https://pypi.org/project/polars-runtime-64/) · [docs](https://docs.pola.rs/api/python/stable/reference/index.html) · [source](https://github.com/pola-rs/polars)

<details><summary>README extract</summary>

Packages that contain the binary shared libraries that back the polars python package. Not meant for
general consumption and just meant as dependencies for the polars main package.

</details>

### DIRAC

DIRAC is an interware, meaning a software framework for distributed computing.

`pip install DIRAC` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8252 · last release 2026-11-02 · [PyPI](https://pypi.org/project/DIRAC/)

_README extract left out: share-alike licence._

### MDAnalysis

An object-oriented toolkit to analyze molecular dynamics trajectories.

`pip install MDAnalysis` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 8253 · last release 2026-10-21 · [PyPI](https://pypi.org/project/MDAnalysis/) · [docs](https://docs.mdanalysis.org/) · [source](https://github.com/mdanalysis/mdanalysis)

_README extract left out: share-alike licence._

### pm4py

Process mining for Python

`pip install pm4py` · installs (wheel) · licence: AGPL-3.0-or-later · rank 8260 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pm4py/) · [docs](https://processintelligence.solutions/pm4py/) · [source](https://github.com/process-intelligence-solutions/pm4py)

_README extract left out: share-alike licence._

### cassio

A framework-agnostic Python library to seamlessly integrate Apache Cassandra(R) with ML/LLM/genAI workloads.

`pip install cassio` · installs (wheel) · licence: Apache Software License · rank 8279 · last release 2024-10-03 · [PyPI](https://pypi.org/project/cassio/) · [source](https://github.com/CassioML/cassio)

<details><summary>README extract</summary>

A framework-agnostic Python library to seamlessly integrate Apache Cassandra with ML/LLM/genAI workloads.

Note: this is currently an alpha release.

Installation is as simple as:

For example usages and integration with higher-level LLM frameworks
such as LangChain, please visit cassio.org.

Sections: cassIO, Users, Setup, Use cassio current code in other Poetry base projects, Versioning, Style and typing, Python version coverage, Publishing, Integration with the DB

</details>

### skrub

Machine learning with dataframes

`pip install skrub` · installs (wheel) · licence: BSD-3-Clause · rank 8293 · last release 2026-10-01 · [PyPI](https://pypi.org/project/skrub/) · [source](https://github.com/skrub-data/skrub)

<details><summary>README extract</summary>

skrub is a Python library that facilitates machine learning with dataframes.

If you like the package, spread the word and ⭐ this repository!
You can also join the Discord server.

Website:

See our examples, or check out
the learning materials.

Documentation and examples are bundled with the package itself, in
`skrub/_docs`. ...

Example:
```python
import skrub
print(skrub.docs_dir)
```

Sections: skrub, Citing skrub

</details>

### adtk

A package for unsupervised time series anomaly detection

`pip install adtk` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 8320 · last release 2020-04-17 · [PyPI](https://pypi.org/project/adtk/)

<details><summary>README extract</summary>

Anomaly Detection Toolkit (ADTK) is a Python package for unsupervised /
rule-based time series anomaly detection.

As the nature of anomaly varies over different cases, a model may not work
universally for all anomaly detection problems. ...

Sections: Anomaly Detection Toolkit (ADTK), Examples

</details>

### gradio-rangeslider

🛝 Slider component for selecting a range of values

`pip install gradio-rangeslider` · installs (wheel) · licence: not stated · rank 8353 · last release 2024-10-09 · [PyPI](https://pypi.org/project/gradio-rangeslider/) · [source](https://github.com/freddyaboulton/gradio-range-slider)

<details><summary>README extract</summary>

tags: [gradio-custom-component, Slider, leaderboards, forms, filtering, slider]
title: gradio_rangeslider
short_description: 🛝 Slider component for selecting a range of values
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: app.py

🛝 Slider component for selecting a range of values

Example:
```python
import gradio as gr
from gradio_rangeslider import RangeSlider
from pathlib import Path

text = "## The range is: {min} to {max}"

docs = Path(file).parent / "docs.md"

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.Tab("Demo"):
            gr.Markdown("""## 🛝 RangeSlider

...
```

Sections: `gradio_rangeslider`, Usage, `RangeSlider`, Initialization, Events, User function

</details>

### drake

Model-based design and verification for robotics

`pip install drake` · installs (wheel) · licence: BSD License; Other/Proprietary License · rank 8389 · last release 2026-10-15 · [PyPI](https://pypi.org/project/drake/)

<details><summary>README extract</summary>

Drake ("dragon" in Middle English) is a toolbox started by the Robot Locomotion
Group at the MIT Computer Science and Artificial Intelligence Lab (CSAIL).
The development team has now grown significantly, with core development led by
the Toyota Research Institute. ...

</details>

### snakemake

Workflow management system to create reproducible and scalable data analyses

`pip install snakemake` · installs (wheel) · licence: MIT · rank 8396 · last release 2026-10-21 · [PyPI](https://pypi.org/project/snakemake/) · [docs](https://snakemake.readthedocs.io) · [source](https://github.com/snakemake/snakemake)

<details><summary>README extract</summary>

Snakemake is a workflow management system that aims to reduce the
 complexity of creating workflows by providing a fast and comfortable
 execution environment, together with a clean and modern specification
 language in python style. Snakemake workflows are essentially Python
 scripts extended by declarative code to define rules. ...

</details>

### evo

Python package for the evaluation of odometry and SLAM

`pip install evo` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8398 · last release 2026-10-21 · [PyPI](https://pypi.org/project/evo/)

_README extract left out: share-alike licence._

### oqpy

Generating OpenQASM 3 + OpenPulse in Python

`pip install oqpy` · installs (wheel) · licence: Apache Software License · rank 8405 · last release 2026-10-07 · [PyPI](https://pypi.org/project/oqpy/) · [source](https://github.com/openqasm/oqpy)

<details><summary>README extract</summary>

The goal of `oqpy` ("ock-pie") is to make it easy to generate OpenQASM 3 + OpenPulse in Python. The
`oqpy` library builds off of the `openqasm3` and `openpulse` packages,
which serve as Python reference implementations of the _abstract syntax tree (AST) for the
OpenQASM 3 and OpenPulse grammars. ...

Example:
```python
import oqpy
prog = oqpy.Program()  # create a new oqpy program

# Declare frames: transmon driving frame and readout receive/transmit frames
xy_frame = oqpy.FrameVar(oqpy.PortVar("dac0"), 6.431e9, name="xy_frame")
rx_frame = oqpy.FrameVar(oqpy.PortVar("adc0"), 5.752e9, name="rx_frame")
...
```

Sections: OQpy: Generating OpenQASM 3 + OpenPulse in Python, What are OpenQASM 3 and OpenPulse?, Example: Ramsey Interferometry

</details>

### Morfessor

Morfessor

`pip install Morfessor` · installs (wheel) · licence: BSD License · rank 8423 · last release 2019-07-31 · [PyPI](https://pypi.org/project/Morfessor/)

### GridDataFormats

Reading and writing of data on regular grids in Python

`pip install GridDataFormats` · installs (wheel) · licence: LGPL-3.0-or-later · rank 8435 · last release 2026-05-23 · [PyPI](https://pypi.org/project/GridDataFormats/) · [docs](https://www.mdanalysis.org/GridDataFormats/) · [source](https://github.com/MDAnalysis/GridDataFormats)

_README extract left out: share-alike licence._

### tf-nightly

TensorFlow is an open source machine learning framework for everyone.

`pip install tf-nightly` · installs (wheel) · licence: Apache Software License · rank 8449 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tf-nightly/)

<details><summary>README extract</summary>

TensorFlow is an open source software library for high performance numerical
computation. Its flexible architecture allows easy deployment of computation
across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters
of servers to mobile and edge devices. ...

</details>

### pyjanitor

Tools for cleaning pandas DataFrames

`pip install pyjanitor` · installs (wheel) · licence: MIT License · rank 8466 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyjanitor/) · [docs](https://pyjanitor-devs.github.io/pyjanitor) · [source](https://github.com/pyjanitor-devs/pyjanitor)

<details><summary>README extract</summary>

`pyjanitor` is a Python implementation of the R package `janitor`.
It provides a clean user-friendly API for extending pandas
with powerful and readable data-cleaning functions.

Features:
Originally a port of the R package,
`pyjanitor` has evolved from a set of convenient data cleaning routines
into an experiment with the `method chaining` paradigm. ...

Example:
```python
# Libraries
import numpy as np
import pandas as pd
import janitor

# Sample Data curated for this example
company_sales = {
    'Sales Month': ['Jan', 'Feb', 'Mar', 'April'],
    'Company 1': [150.0, 200.0, 300.0, 400.0],
    'Company 2': [180.0, 250.0, np.nan, 500.0],
    'Company 3': [400.0, 500.0, 600.0, 675.0],
...
```

...

</details>

### MetPy

Collection of tools for reading, visualizing and performing calculations with weather data.

`pip install MetPy` · installs (wheel) · licence: BSD License · rank 8560 · last release 2025-08-29 · [PyPI](https://pypi.org/project/MetPy/) · [docs](https://unidata.github.io/MetPy/) · [source](https://github.com/Unidata/MetPy)

<details><summary>README extract</summary>

MetPy is a collection of tools in Python for reading, visualizing and
performing calculations with weather data.

MetPy follows semantic versioning in its version number. This means
that any MetPy ``1.x`` release will be backwards compatible with an earlier ``1.y`` release. ...

</details>

### joblibspark

Joblib Apache Spark Backend

`pip install joblibspark` · installs (wheel) · licence: Apache Software License · rank 8582 · last release 2025-04-07 · [PyPI](https://pypi.org/project/joblibspark/)

<details><summary>README extract</summary>

Joblib spark backend is a extension for joblib, which make joblib running on spark parallelly.

</details>

### tf2onnx

Tensorflow to ONNX converter

`pip install tf2onnx` · installs (wheel) · licence: Apache-2.0 · rank 8620 · last release 2026-03-04 · [PyPI](https://pypi.org/project/tf2onnx/)

<details><summary>README extract</summary>

tf2onnx converts TensorFlow (tf-2.x), keras, tensorflow.js and tflite models to ONNX via command
line or python api.

Example:
```python
import tf2onnx

model_proto, external_tensor_storage = tf2onnx.convert.from_keras(model,
                input_signature=None, opset=None, custom_ops=None,
                custom_op_handlers=None, custom_rewriter=None,
                inputs_as_nchw=None, outputs_as_nchw=None, extra_opset=None,
...
```

Sections: ONNX, TensorFlow, Python, Prerequisites, Getting started, Tool to save pre-trained model, Python API Reference, from_keras (tf-2.0 and newer), from_function (tf-2.0 and newer), from_graph_def, from_tflite, Creating custom op mappings from python, How tf2onnx works, Step 1 - start with a frozen graph

</details>

### foundry-local-sdk

Foundry Local Python SDK (v2): in-process Python bindings for the Foundry Local native runtime.

`pip install foundry-local-sdk` · installs (wheel) · licence: MIT · rank 8641 · last release 2026-11-02 · [PyPI](https://pypi.org/project/foundry-local-sdk/) · [source](https://github.com/microsoft/Foundry-Local)

<details><summary>README extract</summary>

The Foundry Local Python SDK is a native Python binding for the Foundry Local C++ SDK. It lets you discover, download, load, and run inference against local AI models — chat completions (streaming and non-streaming), tool calling, embeddings, and audio transcription — directly in-process via a cffi binding to the Foundry Local native library. ...

Features:
- Model Catalog and BYOM – browse the public catalog or register existing local model assets without copying them
- Model Management – download, cache, load, and unload models ...

Example:
```python
from foundry_local_sdk import (
    ChatSession,
    Configuration,
    FoundryLocalManager,
    MessageItem,
    Request,
    RequestOptions,
    SearchOptions,
    TextItem,
)

# 1. Initialize
config = Configuration(app_name="MyApp")
...

</details>

### pykdtree

Fast kd-tree implementation with OpenMP-enabled queries

`pip install pykdtree` · installs (wheel) · licence: LGPL-3.0-or-later · rank 8658 · last release 2025-08-06 · [PyPI](https://pypi.org/project/pykdtree/)

_README extract left out: share-alike licence._

### quantulum3

Extract quantities from unstructured text.

`pip install quantulum3` · installs (wheel) · licence: MIT · rank 8674 · last release 2026-03-09 · [PyPI](https://pypi.org/project/quantulum3/) · [source](https://github.com/nielstron/quantulum3)

<details><summary>README extract</summary>

Python library for information extraction of quantities, measurements
and their units from unstructured text. It is able to disambiguate between similar
looking units based on their *k-nearest neighbours* in their GloVe vector representation
and their Wikipedia page. ...

Example:
```python
>>> from quantulum3 import parser
>>> quants = parser.parse('I want 2 liters of wine')
>>> quants
[Quantity(2, 'litre')]
```

Sections: quantulum3, User Guide, Usage, Units and entities, Export/Import, Disambiguation, Spoken version, Manipulation, Extension, Training the classifier, Additional units, Custom Units and Entities, Adding Units and Entities

</details>

### cyksuid

Cython implementation of ksuid

`pip install cyksuid` · installs from source (sdist only) · licence: BSD License · rank 8686 · last release 2024-09-25 · [PyPI](https://pypi.org/project/cyksuid/)

<details><summary>README extract</summary>

A high performance Cython implementation of
KSUID (K-Sortable Globally Unique
IDs).

Example:
```python
from cyksuid import ksuid, parse

uid = ksuid.ksuid()

uid.bytes       # b'\x0f\xd4oB\x81I\xe5\x8d\x95\xb5\xeb\xbc"\xa0\xcd\xfe)N\xe0I'
uid.hex         # '0fd46f428149e58d95b5ebbc22a0cdfe294ee049'
uid.datetime    # datetime.datetime(2022, 10, 12, 13, 12, 34)
uid.timestamp   # 1665580354
uid.encoded     # b'2G2IfS6177qFICE3w10eMjgYu89'

...
```

Sections: CyKSUID, Dependencies, Sample Usage, v1 API, v2 API, Benchmark

</details>

### keras-nlp

Pretrained models for Keras.

`pip install keras-nlp` · installs (wheel) · licence: Apache-2.0 · rank 8688 · last release 2026-11-03 · [PyPI](https://pypi.org/project/keras-nlp/) · [source](https://github.com/keras-team/keras/keras_hub)

<details><summary>README extract</summary>

KerasNLP has renamed to KerasHub! Read the announcement
here.

This contains a shim package for `keras-nlp` so that the old style
`pip install keras-nlp` and `import keras_nlp` continue to work.

</details>

### gsw

Gibbs Seawater Oceanographic Package of TEOS-10

`pip install gsw` · installs (wheel) · licence: BSD-3-Clause · rank 8730 · last release 2026-06-21 · [PyPI](https://pypi.org/project/gsw/) · [docs](https://teos-10.github.io/GSW-Python/) · [source](https://github.com/TEOS-10/GSW-python)

<details><summary>README extract</summary>

This Python implementation of the Thermodynamic Equation of Seawater 2010 (TEOS-10) is based primarily on numpy ufunc wrappers of the GSW-C implementation.
This library replaces the original python-gsw pure-python implementation. ...

Sections: GSW-Python, Note for xarray users, Note on generating the docstrings, Scripts, Modules, Notes

</details>

### iLCDirac

iLCDirac is the iLC/CLIC/FCC extension of DIRAC

`pip install iLCDirac` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8737 · last release 2026-09-18 · [PyPI](https://pypi.org/project/iLCDirac/) · [docs](https://ilcdirac-doc.web.cern.ch/)

_README extract left out: share-alike licence._

### tsfresh

tsfresh extracts relevant characteristics from time series

`pip install tsfresh` · installs (wheel) · licence: MIT · rank 8752 · last release 2026-05-31 · [PyPI](https://pypi.org/project/tsfresh/)

### better-optimize

A drop-in replacement for scipy optimize functions with quality of life improvements

`pip install better-optimize` · installs (wheel) · licence: MIT License · rank 8753 · last release 2026-10-18 · [PyPI](https://pypi.org/project/better-optimize/) · [source](https://github.com/jessegrabowski/better_optimize.git)

<details><summary>README extract</summary>

`better_optimize` is a friendlier front-end to scipy's `optimize.minimize` and `optimize.root` functions. Features
include:

- Progress bar!
- Early stopping!
- Better propagation of common arguments (`maxiters`, `tol`)!
- A typed, documented configuration object for every method, so swapping optimizers is a one-argument change!

Example:
```python
import numpy as np
from better_optimize import minimize
from better_optimize.configuration import LBFGSBConfig

def rosenbrock(x):
    return sum(100.0*(x[1:] - x[:-1]2.0)2.0 + (1 - x[:-1])**2.0)

result = minimize(
    rosenbrock,
    x0=np.array([-1.0, 2.0]),
    method=LBFGSBConfig(tol=1e-6, maxiter=1000),
...
```

...

</details>

### sdmx1

Statistical Data and Metadata eXchange (SDMX)

`pip install sdmx1` · installs (wheel) · licence: Apache Software License · rank 8757 · last release 2026-10-18 · [PyPI](https://pypi.org/project/sdmx1/) · [docs](https://sdmx1.readthedocs.io/en/latest) · [source](https://github.com/khaeru/sdmx)

<details><summary>README extract</summary>

Source code @ Github —
Authors

`sdmx` (‘sdmx1’ on PyPI) is a Python implementation
of the SDMX 2.1 (ISO 17369:2013) and 3.0 standards
for statistical data and metadata exchange.
The SDMX standards are developed and used by national statistical agencies, central banks, and international organisations.

`sdmx` can be used to: ...

Sections: sdmx: Statistical data and metadata exchange, Documentation

</details>

### pypcd4

Read and write PCL .pcd files in python

`pip install pypcd4` · installs (wheel) · licence: BSD License · rank 8777 · last release 2026-10-05 · [PyPI](https://pypi.org/project/pypcd4/) · [source](https://github.com/MapIV/pypcd4)

<details><summary>README extract</summary>

Example:
```python
from pypcd4 import PointCloud
```

Sections: pypcd4, Description, Usage, Getting Started, Working with .pcd Files, Converting Between PointCloud and NumPy Array, Creating Custom Conversion Methods, Working with ROS PointCloud2 Messages, Concatenating PointClouds, Filtering a PointCloud, Using a Slice, Using a Boolean Mask, Using Field Names, Saving Your Work

</details>

### objectory

A light library for general purpose object factories

`pip install objectory` · installs (wheel) · licence: BSD-3-Clause · rank 8794 · last release 2025-12-19 · [PyPI](https://pypi.org/project/objectory/) · [docs](https://durandtibo.github.io/objectory/) · [source](https://github.com/durandtibo/objectory)

<details><summary>README extract</summary>

Features:
A Python library for general purpose object factories.
In particular, it focuses on dynamic object factory implementations where objects can be registered
dynamically without changing the code of the factory. ...

Example:
```python
>>> from objectory import factory
>>> obj = factory("builtins.list")
>>> print(obj)
[]
>>> obj = factory("builtins.list", [4, 2])
>>> print(obj)
[4, 2]
```

Sections: objectory = object + factory, Overview, API stability

</details>

### cwltool

Common workflow language reference implementation

`pip install cwltool` · installs (wheel) · licence: Apache Software License · rank 8815 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cwltool/)

<details><summary>README extract</summary>

PyPI:

Conda:

Debian:

Quay.io (Docker): |Quay.io Container|

This is the reference implementation of the Common Workflow Language open
standards. It is intended to be feature complete
and provide comprehensive validation of CWL
files as well as provide other tools related to working with CWL. ...

Example:
```python
import cwltool
```

...

</details>

### accumulation-tree

Red/black tree with support for fast accumulation of values in a key range

`pip install accumulation-tree` · installs from source (sdist only) · licence: MIT License · rank 8825 · last release 2024-09-26 · [PyPI](https://pypi.org/project/accumulation-tree/)

### darts

A python library for easy manipulation and forecasting of time series.

`pip install darts` · installs (wheel) · licence: Apache-2.0 · rank 8827 · last release 2026-10-16 · [PyPI](https://pypi.org/project/darts/) · [docs](https://unit8co.github.io/darts/) · [source](https://github.com/unit8co/darts)

<details><summary>README extract</summary>

Darts is a Python library for user-friendly forecasting and anomaly detection
on time series. It contains a variety of models, from classics such as ARIMA to
deep neural networks. The forecasting models can all be used in the same way,
using `fit()` and `predict()` functions, similar to scikit-learn. ...

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
...

</details>

### pymc-extras

A home for new additions to PyMC, which may include unusual probability distribitions, advanced model fitting algorithms, or any code that may be inappropriate to include in the pymc repository, but may want to be made available to users.

`pip install pymc-extras` · installs (wheel) · licence: Apache Software License · rank 8828 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pymc-extras/) · [docs](https://pymc-extras.readthedocs.io/) · [source](https://github.com/pymc-devs/pymc-extras.git)

<details><summary>README extract</summary>

PyMC Extras extends PyMC with additional distributions, inference methods, and model transformations.
It is maintained by the PyMC team and hosts functionality that is too specialized for the core library, but useful enough that you shouldn't have to write it yourself.

Highlights include: ...

Example:
```python
import pymc as pm
import pymc_extras as pmx

with pm.Model():
    xi = pm.HalfNormal("xi", 0.2)
    pmx.GenExtreme("llik", mu=1, sigma=0.5, xi=xi, observed=data)
```

Sections: Welcome to `pymc-extras`, Questions, What belongs in `pymc-extras`?, What does not belong in `pymc-extras`?

</details>

### tensorflow-io

TensorFlow IO

`pip install tensorflow-io` · does not install on CPython 3.14 · licence: Apache Software License · rank 8842 · last release 2024-07-01 · [PyPI](https://pypi.org/project/tensorflow-io/) · [docs](https://tensorflow.org/io) · [source](https://github.com/tensorflow/io)

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

### ale-py

The Arcade Learning Environment (ALE) - a platform for AI research.

`pip install ale-py` · installs (wheel) · licence: GPL-2.0-only · rank 8913 · last release 2026-08-16 · [PyPI](https://pypi.org/project/ale-py/) · [docs](https://ale.farama.org)

_README extract left out: share-alike licence._

### dlib

A toolkit for making real world machine learning and data analysis applications

`pip install dlib` · installs from source (sdist only) · licence: Boost Software License · rank 8960 · last release 2026-03-29 · [PyPI](https://pypi.org/project/dlib/)

### pytorch-forecasting

Forecasting timeseries with PyTorch - dataloaders, normalizers, metrics and models

`pip install pytorch-forecasting` · installs (wheel) · licence: MIT License · rank 8973 · last release 2026-06-24 · [PyPI](https://pypi.org/project/pytorch-forecasting/)

<details><summary>README extract</summary>

_PyTorch Forecasting is a PyTorch-based package for forecasting with state-of-the-art deep learning architectures. It provides a high-level API and uses PyTorch Lightning to scale training on GPU or CPU, with automatic logging.

| | Documentation · Tutorials · Release Notes | ...

Example:
```python
# imports for training
import lightning.pytorch as pl
from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.callbacks import EarlyStopping, LearningRateMonitor
# import dataset, network to train and metric to optimize
from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer, QuantileLoss
...
```

Sections: Documentation, Available models, Usage example

</details>

### dynesty

A dynamic nested sampling package for computing Bayesian posteriors and evidences.

`pip install dynesty` · installs (wheel) · licence: not stated · rank 9050 · last release 2026-07-17 · [PyPI](https://pypi.org/project/dynesty/)

<details><summary>README extract</summary>

A Dynamic Nested Sampling package for computing Bayesian posteriors and
evidences. Pure Python. MIT license.

Documentation can be found here.

Sections: dynesty, Documentation, Demos, Attribution, Reporting issues

</details>

### spiceypy

A Python Wrapper for the NAIF CSPICE Toolkit

`pip install spiceypy` · installs (wheel) · licence: MIT · rank 9111 · last release 2026-10-11 · [PyPI](https://pypi.org/project/spiceypy/) · [docs](https://spiceypy.readthedocs.io) · [source](https://github.com/AndrewAnnex/SpiceyPy)

<details><summary>README extract</summary>

SpiceyPy is a Python wrapper for the NAIF C SPICE Toolkit, written using ctypes and Cython.

+------------------------+-------------------+--------+------------+--------------+
 Code Coverage Citation
+========================+===================+========+============+==============+
Github Build Status Docs ...

Sections: SpiceyPy, Introduction, Citing SpiceyPy, Documentation, How to Help, Known Working Environments

</details>

### pint-xarray

Physical units interface to xarray using Pint

`pip install pint-xarray` · installs (wheel) · licence: Apache-2.0 · rank 9191 · last release 2026-03-23 · [PyPI](https://pypi.org/project/pint-xarray/) · [docs](https://pint-xarray.readthedocs.io/en/stable)

<details><summary>README extract</summary>

A convenience wrapper for using pint with
xarray.

Example:
```python
In [1]: import pint_xarray
   ...: import xarray as xr

In [2]: ds = xr.Dataset({"a": ("x", [0, 1, 2]), "b": ("y", [-3, 5, 1], {"units": "m"})})
   ...: ds
Out[2]:
<xarray.Dataset>
Dimensions:  (x: 3, y: 3)
Dimensions without coordinates: x, y
Data variables:
    a        (x) int64 0 1 2
    b        (y) int64 -3 5 1

...
```

Sections: pint-xarray, Usage

</details>

### openTSNE

Extensible, parallel implementations of t-SNE

`pip install openTSNE` · installs (wheel) · licence: OSI Approved · rank 9245 · last release 2025-10-27 · [PyPI](https://pypi.org/project/openTSNE/) · [docs](https://opentsne.readthedocs.io/) · [source](https://github.com/pavlin-policar/openTSNE)

<details><summary>README extract</summary>

openTSNE is a modular Python implementation of t-Distributed Stochasitc Neighbor Embedding (t-SNE) [1]_, a popular dimensionality-reduction algorithm for visualizing high-dimensional data sets. ...

Example:
```python
from sklearn import datasets

iris = datasets.load_iris()
x, y = iris["data"], iris["target"]
```

Sections: openTSNE, Conda, PyPi, A hello world example, References

</details>

### spacy-transformers

spaCy pipelines for pre-trained BERT and other transformers

`pip install spacy-transformers` · installs (wheel) · licence: MIT License · rank 9260 · last release 2026-11-03 · [PyPI](https://pypi.org/project/spacy-transformers/)

<details><summary>README extract</summary>

This package provides spaCy components and
architectures to use transformer models via
Hugging Face's `transformers` in
spaCy. The result is convenient access to state-of-the-art transformer
architectures, such as BERT, GPT-2, XLNet, etc.

> This release requires spaCy v3. For the
> previous version of this library, see the
> `v0.6.x` branch.

Features:
- Use pretrained transformer models like BERT, RoBERTa and XLNet to
 power your spaCy pipeline.
- Easy multi-task learning: backprop to one transformer model from several
 pipeline components. ...

Sections: Features, 📖 Documentation, Applying pretrained text and token classification models, Bug reports and other issues

</details>

### openmdao

OpenMDAO framework infrastructure

`pip install openmdao` · installs (wheel) · licence: Apache-2.0 · rank 9276 · last release 2026-10-27 · [PyPI](https://pypi.org/project/openmdao/)

<details><summary>README extract</summary>

[][18]
[][14]
[][11]
[][11]

OpenMDAO is an open-source high-performance computing platform for
systems analysis and multidisciplinary optimization, written in Python.
It enables you to decompose your models, making them easier to build and
maintain, while still solving them in a tightly coupled manner with
efficient parallel numerical methods. ...

Sections: OpenMDAO, Documentation, Important Notice, Using Pixi for reproducable environments, OpenMDAO Versions, Test OpenMDAO, Build the Documentation for OpenMDAO

</details>

### tfx-bsl

tfx_bsl (TFX Basic Shared Libraries) contains libraries shared by many TFX (TensorFlow eXtended) libraries and components.

`pip install tfx-bsl` · does not install on CPython 3.14 · licence: Apache Software License · rank 9341 · last release 2026-06-10 · [PyPI](https://pypi.org/project/tfx-bsl/)

<details><summary>README extract</summary>

TFX Basic Shared Libraries (`tfx_bsl`) contains libraries shared by many
TensorFlow eXtended (TFX) components.

__Only symbols exported by sub-modules under `tfx_bsl/public` are intended for
direct use by TFX users_, including by standalone TFX library (e.g. TFDV, TFMA,
TFT) users, TFX pipeline authors and TFX component authors. ...

Sections: TFX Basic Shared Libraries, Nightly Packages, Build from source, 1. Prerequisites, 2. Clone the `tfx_bsl` repository, 3. Build the pip package, Compatible versions

</details>

### truthound

Zero-Configuration Data Quality Framework Powered by Polars

`pip install truthound` · installs (wheel) · licence: Apache-2.0 · rank 9344 · last release 2026-11-05 · [PyPI](https://pypi.org/project/truthound/) · [docs](https://www.truthound-docs.tech/) · [source](https://github.com/seadonggyun4/Truthound)

<details><summary>README extract</summary>

Polars 기반 제로 설정 데이터 품질 프레임워크

 Zero-Configuration Data Quality Framework Powered by Polars

 Sniffs out bad data.

Codex CLI·Claude Code 플러그인과 별도 Claude Desktop 확장 모두 Styxis Plugins에서 설치를 시작합니다. 런타임과 MCP 설정은 플러그인이 관리하며, 설치 후 사용할 데이터 폴더를 별도로 승인합니다.

| Truthound Local | Truthound Core |

| | |

| 플러그인 | Codex CLI | Claude Code | ...

Example:
```python
import truthound as th
from truthound.datadocs import generate_validation_report
from truthound.reporters import get_reporter
from truthound.drift import compare

run = th.check(
    {"customer_id": [1, 2, 2], "email": ["a@example.com", None, "c@example.com"]},
)

print(run.execution_mode)
print([check.name for check in run.checks])
...
```

...

</details>

### Lifetimes

Measure customer lifetime value in Python

`pip install Lifetimes` · installs (wheel) · licence: MIT License · rank 9386 · last release 2020-07-06 · [PyPI](https://pypi.org/project/Lifetimes/)

<details><summary>README extract</summary>

Lifetimes can be used to analyze your users based on a few assumption:

1. Users interact with you when they are "alive".
2. Users under study may "die" after some period of time. ...

Sections: Measuring users is hard. Lifetimes makes it easy., Introduction, Applications, Specific Application: Customer Lifetime Value, Documentation and tutorials, Questions? Comments? Requests?, Main Articles, More Information

</details>

### ovstage

NVIDIA OVStage Data Plane Python API

`pip install ovstage` · installs (wheel) · licence: LicenseRef-NvidiaProprietary · rank 9427 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ovstage/) · [docs](https://nvidia-omniverse.github.io/ovstage/) · [source](https://github.com/NVIDIA-Omniverse/ovstage)

<details><summary>README extract</summary>

ovstage is a C and Python library providing a shared, high-performance, vectorized, GPU-capable scene data substrate for OpenUSD scene data, for use in Omniverse Libraries spanning physics, rendering, sensors, animation, and more. ...

Sections: NVIDIA ovstage, Documentation

</details>

### mwxml

A set of utilities for processing MediaWiki XML dump data.

`pip install mwxml` · installs (wheel) · licence: MIT License · rank 9526 · last release 2026-04-08 · [PyPI](https://pypi.org/project/mwxml/)

<details><summary>README extract</summary>

This library contains a collection of utilities for efficiently
processing MediaWiki’s XML database dumps. There are two
important concerns that this module intends to address:
complexity and performance of streaming XML parsing. This library
enables memory efficent stream processing of XML dumps with
a simple `iterator`
strategy. ...

Sections: MediaWiki XML, Example, See also

</details>

### mwtypes

A set of types for processing MediaWiki data.

`pip install mwtypes` · installs (wheel) · licence: MIT License · rank 9543 · last release 2024-07-09 · [PyPI](https://pypi.org/project/mwtypes/)

<details><summary>README extract</summary>

This library provides a set of classes for working with MediaWiki data types.
The point of this library is to help standardize different schemes and naming
patterns between the database, XML dumps and API responses.

* Installation: ``pip install mwtypes``

* License: MIT

</details>

### para

a set utilities that ake advantage of python's 'multiprocessing' module to distribute CPU-intensive tasks

`pip install para` · installs (wheel) · licence: MIT License · rank 9568 · last release 2020-01-17 · [PyPI](https://pypi.org/project/para/)

<details><summary>README extract</summary>

This library implements a simple set of parallel processing utilities that
take advantage of python's `multiprocessing` module to distribute processing
over multiple CPUs on a single machine. ...

Sections: Para(llel) processing utilities, Basic usage

</details>

### mwcli

Utilities for processing MediaWiki on the command line.

`pip install mwcli` · installs (wheel) · licence: MIT License · rank 9579 · last release 2020-01-14 · [PyPI](https://pypi.org/project/mwcli/)

<details><summary>README extract</summary>

A set of helper functions and classes for mediawiki-utilities command-line
utilities.

* Installation: ``pip install mwcli``

* License: MIT

</details>

### segyio

Simple & fast IO for SEG-Y files

`pip install segyio` · installs (wheel) · licence: LGPL-3.0-or-later · rank 9686 · last release 2026-10-29 · [PyPI](https://pypi.org/project/segyio/)

_README extract left out: share-alike licence._

### xpress

FICO Xpress Optimizer Python interface

`pip install xpress` · installs (wheel) · licence: LicenseRef-FICO-Shrinkwrap-License · rank 9703 · last release 2026-10-29 · [PyPI](https://pypi.org/project/xpress/)

<details><summary>README extract</summary>

Create and solve Mathematical Optimization problems like the following:
with just a few lines of code:
With the `xpress` module, one can create and solve optimization problems using the Python&#174; programming language and the FICO Xpress Optimizer library. The module allows for ...

Example:
```python
import xpress as xp
p = xp.problem(name='myexample')  # problem name (optional)
x1 = p.addVariable(vartype=xp.integer, name='x1', lb=-10, ub=10)
x2 = p.addVariable(name='x2')
p.setObjective(x1**2 + 2*x2)      # objective function
p.addConstraint(x1 + 3*x2 >= 4)   # one or more constraints
p.optimize()
...
```

</details>

### tabicl

TabICL: An open tabular foundation model

`pip install tabicl` · installs (wheel) · licence: not stated · rank 9794 · last release 2026-09-02 · [PyPI](https://pypi.org/project/tabicl/)

<details><summary>README extract</summary>

This repository is the official implementation of TabICLv2 (ICML 2026)
and TabICL (ICML 2025).

Strong performance without hyperparameter tuning:
TabICLv2 is a competitive model for tabular classification and regression
on the TabArena and TALENT benchmarks. ...

Example:
```python
from tabicl import TabICLClassifier, TabICLRegressor

clf = TabICLClassifier()
clf.fit(X_train, y_train)  # downloads checkpoint on first use, otherwise cheap
clf.predict(X_test)  # in-context learning happens here

reg = TabICLRegressor()
reg.fit(X_train, y_train)
reg.predict(X_test)
```

...

</details>

### pyopencl

Python wrapper for OpenCL

`pip install pyopencl` · installs (wheel) · licence: MIT · rank 9818 · last release 2026-08-25 · [PyPI](https://pypi.org/project/pyopencl/) · [docs](https://documen.tician.de/pyopencl) · [source](https://github.com/inducer/pyopencl)

<details><summary>README extract</summary>

PyOpenCL lets you access GPUs and other massively parallel compute
devices from Python. It tries to offer computing goodness in the
spirit of its sister project PyCUDA:

* Object cleanup tied to lifetime of objects. This idiom, often
 called RAII
 in C++, makes it much easier to write correct, leak- and
 crash-free code.

* Completeness. ...

</details>

### nilearn

Statistical learning for neuroimaging in Python

`pip install nilearn` · installs (wheel) · licence: BSD-3-Clause · rank 9820 · last release 2026-09-04 · [PyPI](https://pypi.org/project/nilearn/)

<details><summary>README extract</summary>

Nilearn enables approachable and versatile analyses of brain volumes and surfaces.
It provides statistical and machine-learning tools, with instructive documentation & friendly community. ...

Sections: nilearn, Important links, Drop-in Hours, Dependencies

</details>

### pymc-marketing

Marketing Statistical Models in PyMC

`pip install pymc-marketing` · installs (wheel) · licence: Apache Software License · rank 9839 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pymc-marketing/) · [source](https://github.com/pymc-labs/pymc-marketing)

<details><summary>README extract</summary>

Unlock the power of Marketing Mix Modeling (MMM), Customer Lifetime Value (CLV), Customer Choice (discrete choice, MaxDiff, Bayesian BLP), Bass Diffusion, and Predicted Incrementality by Experimentation (PIE) analytics with PyMC-Marketing. ...

Features:
PyMC-Marketing is and will always be free for commercial use, licensed under Apache 2.0. Developed by core developers behind the popular PyMC package and marketing experts, it provides state-of-the-art measurements and analytics for marketing teams. ...

Example:
```python
import pandas as pd
from pymc_marketing.mmm import (
    MMM,
    GeometricAdstock,
    LogisticSaturation,
)
from pymc_marketing.paths import data_dir

file_path = data_dir / "mmm_example.csv"
data = pd.read_csv(file_path, parse_dates=["date_week"])

mmm = MMM(
...

</details>

### cachey

Caching mindful of computation/storage costs

`pip install cachey` · installs (wheel) · licence: BSD License · rank 9842 · last release 2020-03-11 · [PyPI](https://pypi.org/project/cachey/)

<details><summary>README extract</summary>

Caching for Analytic Computations

Humans repeat stuff. Caching helps.

Normal caching policies like LRU aren't well suited for analytic computations
where both the cost of recomputation and the cost of storage routinely vary by
one million or more. Consider the following computations ...

Example:
```python
# Want this
np.std(x)        # tiny result, costly to recompute

# Don't want this
np.transpose(x)  # huge result, cheap to recompute
```

</details>

### pymc3

Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Theano

`pip install pymc3` · installs (wheel) · licence: Apache Software License · rank 9917 · last release 2024-05-31 · [PyPI](https://pypi.org/project/pymc3/)

<details><summary>README extract</summary>

PyMC3 is a Python package for Bayesian statistical modeling and Probabilistic Machine Learning
focusing on advanced Markov chain Monte Carlo (MCMC) and variational inference (VI)
algorithms. Its flexibility and extensibility make it applicable to a
large suite of problems. ...

Features:
- Intuitive model specification syntax, for example, `x ~ N(0,1)`
 translates to `x = Normal('x',0,1)`
- Powerful sampling algorithms, such as the No U-Turn
 Sampler, allow complex models
 with thousands of parameters with little specialized ...

...

</details>

### iterative-stratification

Package that provides scikit-learn compatible cross validators with stratification for multilabel data

`pip install iterative-stratification` · installs (wheel) · licence: BSD 3 · rank 9935 · last release 2024-10-12 · [PyPI](https://pypi.org/project/iterative-stratification/)

<details><summary>README extract</summary>

This iterative-stratification project offers implementations of MultilabelStratifiedKFold, MultilabelRepeatedStratifiedKFold, and MultilabelStratifiedShuffleSplit with a base algorithm for stratifying multilabel data described in the following paper: Sechidis K., Tsoumakas G., Vlahavas I. (2011) On the Stratification of Multi-Label Data. ...

</details>

### scikit-misc

Miscellaneous tools for scientific computing.

`pip install scikit-misc` · installs (wheel) · licence: BSD License · rank 9940 · last release 2026-10-15 · [PyPI](https://pypi.org/project/scikit-misc/) · [docs](https://has2k1.github.io/scikit-misc/stable) · [source](https://github.com/has2k1/scikit-misc)

<details><summary>README extract</summary>

================= =================
Latest Release
License
Build Status
Coverage
Documentation Documentation
================= =================

Miscellaneous tools for data analysis and scientific computing.

</details>

### pysplashsurf

Python bindings for splashsurf, a surface reconstruction library for SPH simulations.

`pip install pysplashsurf` · installs (wheel) · licence: MIT · rank 9961 · last release 2026-03-21 · [PyPI](https://pypi.org/project/pysplashsurf/) · [docs](https://pysplashsurf.readthedocs.io/) · [source](https://github.com/InteractiveComputerGraphics/splashsurf.git)

<details><summary>README extract</summary>

pySplashsurf provides Python bindings for `splashsurf`, an open source surface reconstruction library for particle data from SPH simulations.
Detailed information on the surface reconstruction and library itself and its API can be found on the project website (splashsurf.physics-simulation.org) or the main repository.

Example:
```python
import meshio
import numpy as np
import pysplashsurf

# Load particles from mesh file
mesh = meshio.read("input.vtk")
particles = np.array(mesh.points, dtype=np.float64)

# Reconstruct the points/particles with some post-processing
mesh_with_data, reconstruction = pysplashsurf.reconstruction_pipeline(
    particles,
    particle_radius=0.025,
...
```

Sections: pySplashsurf, Usage, CLI, Library, Build instructions

</details>

### tensorflowjs

(no summary)

`pip install tensorflowjs` · installs (wheel) · licence: Apache Software License · rank 9984 · last release 2024-10-21 · [PyPI](https://pypi.org/project/tensorflowjs/)

<details><summary>README extract</summary>

The tensorflowjs pip package contains libraries and tools for
TensorFlow.js.

Use following command to install the library with support of interactive CLI:

Then, run the following to see a list of CLI options

or, use the wizard

Alternatively, run the converter via its Bazel target. This must be run from withing the tfjs repo:

</details>

### autoware-carla-scenario

CARLA scenario testing framework for Autoware

`pip install autoware-carla-scenario` · installs (wheel) · licence: Apache-2.0 · rank 10010 · last release 2026-11-08 · [PyPI](https://pypi.org/project/autoware-carla-scenario/) · [docs](https://autowarefoundation.github.io/autoware_carla_scenario/) · [source](https://github.com/autowarefoundation/autoware_carla_scenario)

<details><summary>README extract</summary>

A CARLA scenario testing framework for Autoware. Drives an Autoware ego vehicle through configurable scenarios in the CARLA simulator, evaluates pass/fail conditions tick-by-tick, and produces JSON results plus a trajectory log of the run. ...

Features:
- Automated scenario execution against CARLA UE5 (`0.10.0` and `ue5-dev`), through the statically typed typesafe_carla client.
- Hydra-composed configurations for map, server, ego, entities, and scenario. ...

Sections: Autoware CARLA Scenario, Features, Quick usage, Run a scenario, Detect missing 3D models, Documentation

</details>

### pybit7z

A wrapper based on bit7z.

`pip install pybit7z` · installs (wheel) · licence: Apache Software License · rank 10047 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pybit7z/)

<details><summary>README extract</summary>

<!-- SPHINX-START -->

A Python wrapper around bit7z for creating and extracting 7-zip archives, with bundled external codec and format plugins.

Features:
- Compression & extraction of 7z, zip, tar, gzip, bzip2, xz, wim archives (writing); reading support for 60+ formats (rar, iso, cab, chm, nsis, vmdk, vhdx, squashfs, and more). ...

Example:
```python
import pybit7z

with pybit7z.lib7zip_context() as lib:
    ...
```

Sections: pybit7z, Features, Quick Start, Loading External Plugins, Extract Files from an Archive, Compress Files into an Archive, Read Archive Metadata, Command-Line Interface, Writable formats, Readable formats (60+), Bundled external codecs & formats, Building from Source, Prerequisites, Build

</details>

### albumentationsx

Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.

`pip install albumentationsx` · installs (wheel) · licence: AGPL-3.0-only · rank 10055 · last release 2026-11-05 · [PyPI](https://pypi.org/project/albumentationsx/) · [docs](https://albumentations.ai/docs/) · [source](https://github.com/albumentations-team/AlbumentationsX)

_README extract left out: share-alike licence._

### quimb

Quantum information and many-body library.

`pip install quimb` · installs (wheel) · licence: Apache-2.0 · rank 10078 · last release 2026-08-10 · [PyPI](https://pypi.org/project/quimb/) · [docs](https://quimb.readthedocs.io/) · [source](https://github.com/jcmgray/quimb/)

<details><summary>README extract</summary>

`quimb` is an easy but fast python library for *'quantum information many-body'* calculations, focusing primarily on tensor networks. The code is hosted on github, and docs are hosted on readthedocs. Functionality is split in two:

The `quimb.tensor` module contains tools for working with tensors and tensor networks. ...

</details>

### bittensor-wallet

(no summary)

`pip install bittensor-wallet` · installs (wheel) · licence: MIT License · rank 10146 · last release 2026-07-12 · [PyPI](https://pypi.org/project/bittensor-wallet/) · [docs](https://bittensor.com/docs) · [source](https://github.com/opentensor/btwallet)

<details><summary>README extract</summary>

`bittensor-wallet` is superseded by the `bittensor` package (Bittensor 11), where the wallet ships as `bittensor.wallet`. New projects should `pip install bittensor` instead. Development happens in the subtensor monorepo, and documentation lives at bittensor.com/docs.

The on-disk keyfile format is unchanged — existing wallets work as-is. ...

Example:
```python
from bittensor_wallet import Wallet

# creates wallet with name `default`
wallet = Wallet()
wallet.create()
```

Sections: ⚠️ This package is superseded, Bittensor Wallet, Internet-scale Neural Networks, Signed Commits, Documentation, Before you proceed, From PyPI, From source, Usage examples, Rust crate

</details>

### swanlab

Python library for streamlined tracking and management of AI training processes.

`pip install swanlab` · installs (wheel) · licence: Apache-2.0 · rank 10156 · last release 2026-11-04 · [PyPI](https://pypi.org/project/swanlab/) · [docs](https://docs.swanlab.cn/zh/guide_cloud/general/what-is-swanlab.html) · [source](https://github.com/SwanHubX/SwanLab)

<details><summary>README extract</summary>

一个专业、现代化设计的AI训练分析平台
面向模型训练团队，与50+主流框架集成，与你的实验代码轻松结合

🔥SwanLab 在线版 · 📃 文档 · 报告问题 · 建议反馈 · 更新日志 · 基线社区 · ...

Example:
```python
import swanlab

# 初始化一个新的swanlab实验
swanlab.init(
    project="my-first-ml",
    config={"learning-rate": 0.003},
)

# 记录指标
for i in range(10):
    swanlab.log({"loss": i, "acc": i})
```

Sections: 目录, 🌟 最近更新, 👋🏻 什么是SwanLab, 📃 在线演示, 🏁 快速开始, 1.安装, 2.登录并获取 API Key, 3.将 SwanLab 与你的代码集成, 💻 自托管, 🔥 实战案例, 🎮 硬件记录, 🚗 框架集成, 🔌 插件与API, 🆚 与熟悉的工具的比较

</details>

### pytket

Quantum computing toolkit and interface to the TKET compiler

`pip install pytket` · installs (wheel) · licence: Apache Software License · rank 10168 · last release 2026-10-08 · [PyPI](https://pypi.org/project/pytket/) · [docs](https://docs.quantinuum.com/tket/api-docs/) · [source](https://github.com/quantinuum/tket)

<details><summary>README extract</summary>

Pytket is a python module for interfacing with TKET, a quantum computing toolkit and optimising compiler developed by Quantinuum. In addition to pytket there are several pytket extension modules for accessing a range of quantum hardware and classical simulators. ...

</details>

### uniplot

Lightweight plotting to the terminal. 4x resolution via Unicode.

`pip install uniplot` · installs (wheel) · licence: MIT License · rank 10340 · last release 2026-10-29 · [PyPI](https://pypi.org/project/uniplot/) · [source](https://github.com/olavolav/uniplot)

<details><summary>README extract</summary>

Lightweight plotting to the terminal. 4x resolution via Unicode.

When working with production data science code it can be handy to have a
plotting tool that does not rely on graphics dependencies or works only in a
Jupyter notebook.

There are two main use cases:

1. ...

Features:
* Unicode drawing, so 4x the resolution (pixels) of usual ASCII plots, or even
 8x when using Braille characters
* Super simple API
* Interactive mode (pass `interactive=True`)
* Color mode (pass `color=True`) useful in particular when plotting ...

Example:
```python
import math

x = [math.sin(i / 20) + i / 300 for i in range(600)]
from uniplot import plot

plot(x, title="Sine wave")
```

...

</details>

### nemo-text-processing

NeMo text processing for ASR and TTS

`pip install nemo-text-processing` · installs (wheel) · licence: Apache Software License · rank 10354 · last release 2026-06-05 · [PyPI](https://pypi.org/project/nemo-text-processing/)

<details><summary>README extract</summary>

Introduction

`nemo-text-processing` is a Python package for text normalization and inverse text normalization.

Documentation

NeMo-text-processing (text normalization and inverse text normalization).

Tutorials

| Google Collab Notebook | Description | ...

Sections: NeMo Text Processing, Conda virtual environment, Pip, Pip from source, From source

</details>

### epiweeks

Epidemiological weeks calculation based on CDC and ISO week numbering systems

`pip install epiweeks` · installs (wheel) · licence: MIT · rank 10397 · last release 2026-01-07 · [PyPI](https://pypi.org/project/epiweeks/) · [source](https://github.com/dralshehri/epiweeks)

<details><summary>README extract</summary>

A Python package for accurate epidemiological weeks calculation using the US CDC (MMWR) and ISO week numbering systems.

EpiWeeks provides reliable week calculations validated against CDC reference data, essential for disease surveillance, public health reporting, and epidemiological research. ...

Example:
```python
from epiweeks import Week, Year

week = Week(2019, 1)
print(week.enddate())
# 2019-01-05

for week in Year(2019).iterweeks():
    print(week.enddate())
# 2019-01-05
# 2019-01-12
# ...
# 2019-12-21
# 2019-12-28
```

Sections: EpiWeeks, ✨ Features, 🚀 Basic Usage, 📚 Documentation

</details>

### openml

Python API for OpenML

`pip install openml` · installs (wheel) · licence: BSD License · rank 10409 · last release 2025-01-25 · [PyPI](https://pypi.org/project/openml/) · [docs](https://openml.github.io/openml-python/) · [source](https://github.com/openml/openml-python)

<details><summary>README extract</summary>

Installation | Documentation | Contribution guidelines

OpenML-Python provides an easy-to-use and straightforward Python interface for OpenML, an online platform for open science collaboration in machine learning.
It can download or upload data from OpenML, such as datasets and machine learning experiment results.

Example:
```python
import openml

dataset = openml.datasets.get_dataset("credit-g") # or by ID get_dataset(31)
X, y, categorical_indicator, attribute_names = dataset.get_data(target="class")
```

Sections: OpenML-Python, The Python API for a World of Data and More :dizzy, joystick: Minimal Example, page_facing_up: Citing OpenML-Python

</details>

### ai-edge-litert-nightly

LiteRT is for mobile and embedded devices.

`pip install ai-edge-litert-nightly` · installs (wheel) · licence: Apache Software License · rank 10445 · last release 2026-11-08 · [PyPI](https://pypi.org/project/ai-edge-litert-nightly/)

<details><summary>README extract</summary>

LiteRT is the official solution for running machine learning models on mobile
and embedded devices. It enables on-device machine learning inference with low
latency and a small binary size on Android, iOS, and other operating systems.

</details>

### onnxruntime-directml

ONNX Runtime is a runtime accelerator for Machine Learning models

`pip install onnxruntime-directml` · does not install on CPython 3.14 · licence: MIT License · rank 10463 · last release 2026-03-17 · [PyPI](https://pypi.org/project/onnxruntime-directml/)

<details><summary>README extract</summary>

ONNX Runtime is a performance-focused scoring engine for Open Neural Network Exchange (ONNX) models.
For more information on ONNX Runtime, please see aka.ms/onnxruntime or the Github project.

Release Notes :

Sections: ONNX Runtime, Changes, 1.24.4, 1.24.3, 1.24.2, 1.24.1, 1.23.0, 1.22.0, 1.21.0, 1.20.0, 1.19.0, 1.18.0, 1.17.0, 1.16.0

</details>

### qiskit-experiments

Software for developing quantum computing programs

`pip install qiskit-experiments` · installs (wheel) · licence: Apache-2.0 · rank 10468 · last release 2026-08-25 · [PyPI](https://pypi.org/project/qiskit-experiments/) · [docs](https://qiskit-community.github.io/qiskit-experiments) · [source](https://github.com/Qiskit-Community/qiskit-experiments)

<details><summary>README extract</summary>

Qiskit Experiments is a repository that builds tools for building, running,
and analyzing experiments on noisy quantum computers using Qiskit.

To learn more about the package, you can see the
most up-to-date documentation
corresponding to the main branch of this repository or the
documentation for the latest stable release.

</details>

### cotengra

Hyper optimized contraction trees for large tensor networks and einsums.

`pip install cotengra` · installs (wheel) · licence: Apache-2.0 · rank 10515 · last release 2026-10-21 · [PyPI](https://pypi.org/project/cotengra/) · [docs](https://cotengra.readthedocs.io/) · [source](https://github.com/jcmgray/cotengra/)

<details><summary>README extract</summary>

`cotengra` is a python library for contracting tensor networks or einsum
expressions involving large numbers of tensors - the main docs can be found
at cotengra.readthedocs.io.
Some of the key feautures of `cotengra` include: ...

</details>

### jupyter_bokeh

A Jupyter extension for rendering Bokeh content.

`pip install jupyter_bokeh` · installs (wheel) · licence: BSD License · rank 10577 · last release 2026-06-09 · [PyPI](https://pypi.org/project/jupyter_bokeh/) · [source](https://github.com/bokeh/jupyter_bokeh.git)

<details><summary>README extract</summary>

A Jupyter extension for rendering Bokeh content within Jupyter. See also the separate ipywidgets_bokeh library for support for using Jupyter widgets/ipywidgets objects within Bokeh applications.

Sections: jupyter_bokeh, Compatibility, Compatible JupyterLab and `jupyter_bokeh` versions

</details>

### fastdigest

A fast t-digest library for Python built on Rust.

`pip install fastdigest` · installs (wheel) · licence: MIT License · rank 10650 · last release 2026-03-15 · [PyPI](https://pypi.org/project/fastdigest/) · [source](https://github.com/moritzmucha/fastdigest)

<details><summary>README extract</summary>

*fastDigest* is a Rust-powered Python extension module that provides a lightning-fast implementation of the t-digest data structure and algorithm, offering a lightweight suite of online statistics for streaming and distributed data.

Features:
- Online statistics: Compute highly accurate estimates of quantiles, the CDF, the trimmed mean, MAD, and more.
- Updating: Update a t-digest incrementally with streaming data or batches of large datasets. ...

Example:
```python
from fastdigest import TDigest

digest = TDigest()
digest = TDigest.from_values([2.71, 3.14, 1.42])
```

Sections: fastDigest, Features, Usage, Initialization, Mathematical functions, Updating a TDigest, Merging TDigest objects, Dict conversion, Migration, Benchmarks

</details>

### torchax

torchax is a library for running Jax and PyTorch together

`pip install torchax` · installs (wheel) · licence: Apache Software License · rank 10664 · last release 2026-06-17 · [PyPI](https://pypi.org/project/torchax/)

<details><summary>README extract</summary>

Docs page:
Discord Discussion Channel:

torchax is a backend for PyTorch that allows users to run
PyTorch programs on Google Cloud TPUs. It also provides graph-level
interoperability between PyTorch and JAX.

With torchax, you can:
* Run PyTorch code on TPUs with minimal code changes.
* Call JAX functions from PyTorch, passing in `jax.Array`s. ...

Example:
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def init(self):
        super().init()
        self.fc1 = nn.Linear(28 * 28, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = F.relu(self.fc1(x))
...
```

...

</details>

### spacy-alignments

A spaCy package for the Rust tokenizations library

`pip install spacy-alignments` · installs (wheel) · licence: MIT · rank 10680 · last release 2026-10-26 · [PyPI](https://pypi.org/project/spacy-alignments/)

<details><summary>README extract</summary>

A spaCy package for Yohei Tamura's Rust
tokenizations library with Python
bindings.

Example:
```python
import spacy_alignments as tokenizations
a2b, b2a = tokenizations.get_alignments(["å", "BC"], ["abc"])
assert a2b == [[0], [0]]
assert b2a == [[0, 1]]
```

Sections: spacy-alignments vs. pytokenizations, Bug reports and other issues

</details>

### pandas-summary

An extension to pandas describe function.

`pip install pandas-summary` · installs (wheel) · licence: MIT · rank 10684 · last release 2021-11-25 · [PyPI](https://pypi.org/project/pandas-summary/)

### iden

simple library to manage a dataset of shards to train machine learning models

`pip install iden` · installs (wheel) · licence: BSD-3-Clause · rank 10686 · last release 2026-06-15 · [PyPI](https://pypi.org/project/iden/) · [docs](https://durandtibo.github.io/iden/) · [source](https://github.com/durandtibo/iden)

<details><summary>README extract</summary>

Features:
`iden` is a simple Python library to manage a dataset of shards when training a machine learning
model.
`iden` uses a lazy loading approach to load the shard's data, so it is easy to manage shards without
loading their data. ...

Example:
```python
import tempfile
from pathlib import Path
from iden.dataset import create_vanilla_dataset
from iden.shard import create_json_shard, create_shard_dict, create_shard_tuple

# Create a simple dataset
with tempfile.TemporaryDirectory() as tmpdir:
    # Create shards
    train_tuple = create_shard_tuple(
        [
            create_json_shard(
...
```

Sections: iden, Overview, Key Features, Quick Example, Documentation, Basic Usage, Working with Shards, Managing Datasets, Suggestions and Communication, API stability

</details>

### epicscorelibs

The EPICS Core libraries for use by python modules

`pip install epicscorelibs` · installs (wheel) · licence: EPICS · rank 10687 · last release 2026-09-25 · [PyPI](https://pypi.org/project/epicscorelibs/) · [source](https://github.com/mdavidsaver/epicscorelibs)

<details><summary>README extract</summary>

The EPICS (Experimental Physics and Industrial Control System) core libraries
for use by python modules. Either dynamically with ctypes or statically by compiled extension.

</details>

### napari-plugin-engine

napari plugin engine, fork of pluggy

`pip install napari-plugin-engine` · installs (wheel) · licence: MIT License · rank 10720 · last release 2026-02-10 · [PyPI](https://pypi.org/project/napari-plugin-engine/)

<details><summary>README extract</summary>

DEPRECATED:

This project is deprecated. Please use npe2 instead.

`napari-plugin-engine` is the first generation napari plugin engine. We
recommend:
- new plugins use the second generation npe2
- existing plugins migrate to npe2 using the Migration Guide in our docs.

`napari-plugin-engine` is a fork of pluggy,
modified by the napari team. ...

Sections: napari plugin engine, Usage

</details>

### napari

n-dimensional array viewer in Python

`pip install napari` · installs (wheel) · licence: BSD-3-Clause · rank 10740 · last release 2026-10-30 · [PyPI](https://pypi.org/project/napari/) · [docs](https://napari.org) · [source](https://github.com/napari/napari)

<details><summary>README extract</summary>

-green?labelColor=%23004811&color=%235CA038)

napari is a fast, interactive, multi-dimensional image viewer for Python. It's designed for browsing, annotating, and analyzing large multi-dimensional images. It's built on top of Qt (for the GUI), vispy (for performant GPU-based rendering), and the scientific Python stack (numpy, scipy). ...

Features:
Check out the scripts in our `examples` folder to see some of the functionality we're developing!

napari supports six main different layer types, `Image`, `Labels`, `Points`, `Vectors`, `Shapes`, and `Surface`, each corresponding to a different ...

Example:
```python
from skimage import data
import napari

viewer, layers = napari.imshow(data.cells3d(), channel_axis=1, ndisplay=3)
```

...

</details>

### krippendorff

Fast computation of the Krippendorff's alpha measure.

`pip install krippendorff` · installs (wheel) · licence: GPL-3.0-or-later · rank 10743 · last release 2026-10-07 · [PyPI](https://pypi.org/project/krippendorff/) · [docs](https://github.com/pln-fing-udelar/fast-krippendorff) · [source](https://github.com/pln-fing-udelar/fast-krippendorff)

_README extract left out: share-alike licence._

### pytorch_optimizer

optimizer & lr scheduler & objective function collections in PyTorch

`pip install pytorch_optimizer` · installs (wheel) · licence: Apache Software License · rank 10747 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pytorch_optimizer/)

<details><summary>README extract</summary>

`pytorch-optimizer` is a production-focused optimization toolkit for PyTorch with 100+ optimizers, 10+ learning rate schedulers, and 10+ loss functions behind a consistent API.

Use it when you want fast experimentation with modern training methods without rewriting optimizer boilerplate.

Highly inspired by jettify/pytorch-optimizer.

Features:
- Broad optimizer coverage, including many recent research variants.
- Consistent loader APIs for optimizers, schedulers, and losses.
- Practical features such as `foreach`, `Lookahead`, and `Gradient Centralization` integrations. ...

Example:
```python
from pytorch_optimizer import AdamP

model = YourModel()
optimizer = AdamP(model.parameters(), lr=1e-3)
```

...

</details>

### pyperplan

A lightweight STRIPS planner written in Python.

`pip install pyperplan` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 10748 · last release 2022-01-17 · [PyPI](https://pypi.org/project/pyperplan/)

_README extract left out: share-alike licence._

### robot_descriptions

Import open source robot description as Python modules.

`pip install robot_descriptions` · installs (wheel) · licence: Apache Software License · rank 10753 · last release 2026-10-12 · [PyPI](https://pypi.org/project/robot_descriptions/) · [source](https://github.com/robot-descriptions/robot_descriptions.py)

<details><summary>README extract</summary>

Import open source robot descriptions as Python modules.

Importing a description for the first time automatically downloads and caches files for future imports. Most Awesome Robot Descriptions are available. All of them load successfully in respectively MuJoCo (MJCF) or Pinocchio, iDynTree, PyBullet and yourdfpy (URDF).

Example:
```python
from robot_descriptions.loaders.pinocchio import load_robot_description

robot = load_robot_description("upkie_description")
```

Sections: Robot descriptions in Python, From conda-forge, From PyPI, Usage, Command line, Import as submodule, Examples, Descriptions, Arms, Bipeds, Dual arms, Drones, Educational, End effectors

</details>

### pyopenjtalk

A python wrapper for OpenJTalk

`pip install pyopenjtalk` · installs from source (sdist only) · licence: MIT License · rank 10756 · last release 2025-04-08 · [PyPI](https://pypi.org/project/pyopenjtalk/)

<details><summary>README extract</summary>

A python wrapper for OpenJTalk.

The package consists of two core components:

- Text processing frontend based on OpenJTalk
- Speech synthesis backend using HTSEngine

- The package is built with the modified version of OpenJTalk. ...

Example:
```python
In [1]: import pyopenjtalk

In [2]: from scipy.io import wavfile

In [3]: x, sr = pyopenjtalk.tts("おめでとうございます")

In [4]: wavfile.write("test.wav", sr, x.astype(np.int16))
```

Sections: pyopenjtalk, Notice, Build requirements, Quick demo, TTS, Run text processing frontend only, Grapheme-to-phoeneme (G2P), Create/Apply user dictionary, About `run_marine` option

</details>

### tensorflow-decision-forests

Collection of training and inference decision forest algorithms.

`pip install tensorflow-decision-forests` · does not install on CPython 3.14 · licence: Apache Software License · rank 10784 · last release 2025-03-13 · [PyPI](https://pypi.org/project/tensorflow-decision-forests/)

<details><summary>README extract</summary>

TensorFlow Decision Forests (TF-DF) is a library to train, run and
interpret decision forest
models (e.g., Random Forests, Gradient Boosted Trees) in TensorFlow. TF-DF
supports classification, regression and ranking.

TF-DF is powered by
Yggdrasil Decision Forest
(YDF, a library to train and use decision forests in C++, JavaScript, CLI,
and Go. ...

Example:
```python
import tensorflow_decision_forests as tfdf
import pandas as pd

# Load the dataset in a Pandas dataframe.
train_df = pd.read_csv("project/train.csv")
test_df = pd.read_csv("project/test.csv")

# Convert the dataset into a TensorFlow dataset.
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_df, label="my_label")
...
```

Sections: Usage example, Google I/O Presentation, Documentation & Resources, Contact

</details>

### pvxslibs

PVXS libraries packaged for python

`pip install pvxslibs` · installs (wheel) · licence: BSD · rank 10806 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pvxslibs/)

### vesin

Computing neighbor lists for atomistic system

`pip install vesin` · installs (wheel) · licence: BSD-3-Clause · rank 10823 · last release 2026-09-28 · [PyPI](https://pypi.org/project/vesin/) · [docs](https://luthaf.fr/vesin/) · [source](https://github.com/Luthaf/vesin/)

<details><summary>README extract</summary>

| English 🇺🇸⁠/⁠🇬🇧 | Occitan | Arpitan | French 🇫🇷 | Gallo‑Italic | Catalan | Spanish 🇪🇸 | Italian 🇮🇹 |

| neighbo(u)r | vesin | vesin | voisin | visin | veí | vecino | vicino |

Vesin is a fast and easy to use library computing neighbor lists for atomistic
system. We provide an interface for the following programing languages: ...

Example:
```python
import numpy as np
from vesin import NeighborList

# positions can be anything compatible with numpy's ndarray
positions = [
    (0, 0, 0),
    (0, 1.3, 1.3),
]
box = 3.2 * np.eye(3)

calculator = NeighborList(cutoff=4.2, full_list=True)
i, j, S, d = calculator.compute(
    points=positions,
    box=box,
    periodic=True,
    quantities="ijSd",
)
```

Sections: Vesin: fast neighbor lists for atomistic systems, Usage instruction, Benchmarks

</details>

