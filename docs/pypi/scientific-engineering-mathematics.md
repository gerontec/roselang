# Scientific/Engineering / Mathematics

[Index](README.md) · 98 packages in this topic, 209 more listed under another topic, by downloads.

### mpmath

Python library for arbitrary-precision floating-point arithmetic

`pip install mpmath` · installs (wheel) · licence: BSD-3-Clause · rank 221 · last release 2026-03-15 · [PyPI](https://pypi.org/project/mpmath/) · [docs](http://mpmath.org/doc/current/) · [source](https://github.com/mpmath/mpmath)

<details><summary>README extract</summary>

A Python library for arbitrary-precision floating-point arithmetic.

Website:
Main author: Fredrik Johansson <fredrik.johansson@gmail.com>

Mpmath is free software released under the New BSD License (see the
LICENSE file for details).

Sections: mpmath, 2. Documentation, 3. Running tests, 4. Known problems, 5. Help and bug reports

</details>

### boolean.py

Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.

`pip install boolean.py` · installs (wheel) · licence: BSD-2-Clause · rank 487 · last release 2025-04-03 · [PyPI](https://pypi.org/project/boolean.py/)

<details><summary>README extract</summary>

This library helps you deal with boolean expressions and algebra with variables
and the boolean functions AND, OR, NOT.

You can parse expressions from strings and simplify and compare expressions.
You can also easily create your custom algreba and mini DSL and create custom
tokenizers to handle custom expressions. ...

</details>

### tensorboard

TensorBoard lets you watch Tensors Flow

`pip install tensorboard` · installs (wheel) · licence: Apache Software License · rank 871 · last release 2026-06-29 · [PyPI](https://pypi.org/project/tensorboard/)

<details><summary>README extract</summary>

TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

Releases prior to 1.6.0 were published under the ``tensorflow-tensorboard`` name
and may be found at

</details>

### formulaic

An implementation of Wilkinson formulas.

`pip install formulaic` · installs (wheel) · licence: MIT · rank 1043 · last release 2026-06-02 · [PyPI](https://pypi.org/project/formulaic/) · [docs](https://matthewwardrop.github.io/formulaic) · [source](https://github.com/matthewwardrop/formulaic)

<details><summary>README extract</summary>

Formulaic is a high-performance implementation of Wilkinson formulas for Python.

It provides:

- high-performance dataframe to model-matrix conversions.
- support for reusing the encoding choices made during conversion of one data-set on other datasets.
- extensible formula parsing. ...

Example:
```python
import pandas
from formulaic import Formula

df = pandas.DataFrame({
    'y': [0, 1, 2],
    'x': ['A', 'B', 'C'],
    'z': [0.3, 0.1, 0.2],
})

y, X = Formula('y ~ x + z').get_model_matrix(df)
```

Sections: Example code, Benchmarks, Related projects and prior art, Used by

</details>

### tensorboard-data-server

Fast data loading for TensorBoard

`pip install tensorboard-data-server` · installs (wheel) · licence: Apache Software License · rank 1064 · last release 2023-10-23 · [PyPI](https://pypi.org/project/tensorboard-data-server/)

### altgraph

Python graph (network) package

`pip install altgraph` · installs (wheel) · licence: MIT License · rank 1217 · last release 2025-11-21 · [PyPI](https://pypi.org/project/altgraph/) · [docs](https://altgraph.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/altgraph)

<details><summary>README extract</summary>

altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

altgraph includes some additional usage of Python 2.6+ features and
enhancements related to modulegraph and macholib.

* Documentation

* Issue Tracker

* Repository

Sections: Project links, 0.17.5, 0.17.4, 0.17.3, 0.17.2, 0.17.1, 0.17, 0.16.1, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11

</details>

### latex2mathml

Pure Python library for LaTeX to MathML conversion

`pip install latex2mathml` · installs (wheel) · licence: MIT · rank 1612 · last release 2026-09-07 · [PyPI](https://pypi.org/project/latex2mathml/) · [source](https://github.com/roniemartinez/latex2mathml)

<details><summary>README extract</summary>

License

 Version

 Github Actions

 Coverage

 Supported versions

 Wheel

 Status

 Downloads

 All Contributors

Pure Python library for LaTeX to MathML conversion

Example:
```python
import latex2mathml.converter

latex_input = ""
mathml_output = latex2mathml.converter.convert(latex_input)
```

Sections: latex2mathml, Usage, Python, Command-line, References, LaTeX, MathML

</details>

### PuLP

PuLP is an LP modeler written in python. PuLP can generate MPS or LP files and call GLPK, COIN CLP/CBC, CPLEX, and GUROBI to solve linear problems.

`pip install PuLP` · installs (wheel) · licence: MIT · rank 1614 · last release 2026-10-22 · [PyPI](https://pypi.org/project/PuLP/) · [source](https://github.com/coin-or/pulp)

<details><summary>README extract</summary>

PuLP is an linear and mixed integer programming modeler written in Python. With PuLP, it is simple to create MILP optimisation problems and solve them with the latest open-source (or proprietary) solvers. ...

Example:
```python
from pulp import *
prob = LpProblem("myProblem", LpMinimize)
x = prob.add_variable("x", 0, 3)
```

Sections: pulp, Quickstart, Essential Classes, Useful Functions, More Examples, Building from source, Building the documentation

</details>

### dm-tree

Tree is a library for working with nested data structures.

`pip install dm-tree` · installs (wheel) · licence: Apache Software License · rank 2174 · last release 2026-03-31 · [PyPI](https://pypi.org/project/dm-tree/)

<details><summary>README extract</summary>

`tree` is a library for working with nested data structures. In a way, `tree`
generalizes the builtin `map` function which only supports flat sequences,
and allows to apply a function to each "leaf" preserving the overall
structure. ...

Example:
```python
>>> import tree
>>> structure = [[1], [[[2, 3]]], [4]]
>>> tree.flatten(structure)
[1, 2, 3, 4]
>>> tree.map_structure(lambda v: v**2, structure)
[[1], [[[4, 9]]], [16]]
```

</details>

### pyquaternion

A fully featured, pythonic library for representing and using quaternions.

`pip install pyquaternion` · installs (wheel) · licence: MIT License · rank 3197 · last release 2020-10-05 · [PyPI](https://pypi.org/project/pyquaternion/)

<details><summary>README extract</summary>

A fully featured, pythonic library for quaternion representation, manipulation, 3D animation and geometry.

</details>

### pytensor

Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.

`pip install pytensor` · installs (wheel) · licence: BSD-3-Clause · rank 3733 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pytensor/) · [docs](https://pytensor.readthedocs.io/en/latest/) · [source](https://github.com/pymc-devs/pytensor)

<details><summary>README extract</summary>

is a Python library that allows one to define, optimize, and
efficiently evaluate mathematical expressions involving multi-dimensional arrays.
It provides the computational backend for PyMC.

Features:
- A hackable, pure-Python codebase
- Extensible graph framework suitable for rapid development of custom operators and symbolic optimizations ...

Example:
```python
import pytensor
from pytensor import tensor as pt

# Declare two symbolic floating-point scalars
a = pt.dscalar("a")
b = pt.dscalar("b")

# Create a simple example expression
c = a + b

# Convert the expression into a callable object that takes `(a, b)`
# values as input and computes the value of `c`.
f_c = pytensor.function([a, b], c)

...
```

Sections: Features, Getting started, Background

</details>

### ruptures

Change point detection for signals in Python.

`pip install ruptures` · does not install on CPython 3.14 · licence: BSD License · rank 3782 · last release 2025-09-10 · [PyPI](https://pypi.org/project/ruptures/) · [docs](https://centre-borelli.github.io/ruptures-docs/) · [source](https://github.com/deepcharles/ruptures/)

<details><summary>README extract</summary>

`ruptures` is a Python library for off-line change point detection.
This package provides methods for the analysis and segmentation of non-stationary signals. Implemented algorithms include exact and approximate detection for various parametric and non-parametric models. ...

Example:
```python
import matplotlib.pyplot as plt
import ruptures as rpt

# generate signal
n_samples, dim, sigma = 1000, 3, 4
n_bkps = 4  # number of breakpoints
signal, bkps = rpt.pw_constant(n_samples, dim, n_bkps, noise_std=sigma)

# detection
algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

# display
rpt.display(signal, bkps, result)
...
```

Sections: Welcome to ruptures, Latest news, Basic usage, General information, Contact, Important links

</details>

### qpsolvers

Quadratic programming solvers in Python with a unified API.

`pip install qpsolvers` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 3836 · last release 2026-07-19 · [PyPI](https://pypi.org/project/qpsolvers/) · [docs](https://qpsolvers.github.io/qpsolvers/) · [source](https://github.com/qpsolvers/qpsolvers)

_README extract left out: share-alike licence._

### ocp-gordon

A Python library for Gordon Surface interpolation using B-splines.

`pip install ocp-gordon` · installs (wheel) · licence: Apache-2.0 · rank 3916 · last release 2026-09-09 · [PyPI](https://pypi.org/project/ocp-gordon/)

<details><summary>README extract</summary>

This library provides a Python implementation for creating Gordon surfaces, a method for interpolating a network of curves to generate a smooth surface. It is designed to be compatible with CadQuery's OCP and leverages B-spline mathematics.

The implementation is written entirely in Python and is adapted from the original C++ code in `occ_gordon` ...

Features:
- Gordon surface interpolation from profile and guide curves.
- Compatibility with B-spline representations.
- Integration with CadQuery's OCP (OpenCASCADE Python) for geometric primitives.

Example:
```python
# Assume you have profile_curves and guide_curves defined as lists of B-spline objects
# profile_curves = [...] # List of Geom_BSplineCurve objects
# guide_curves = [...]   # List of Geom_BSplineCurve objects

...

</details>

### trianglesolver

Find all the sides and angles of a triangle, if you know some of the sides and/or angles. (Uses the Law of Sines and Law of Cosines.)

`pip install trianglesolver` · installs (wheel) · licence: MIT License · rank 3922 · last release 2020-04-10 · [PyPI](https://pypi.org/project/trianglesolver/)

<details><summary>README extract</summary>

Written by Steven Byrnes,

Download:
Source code repository:

This little package applies the law of sines or cosines to find all the
sides and angles of a triangle, if you know some of the sides and/or
angles.

The main function defined by this package is solve(...). Simple example:: ...

</details>

### pyomo

The Pyomo optimization modeling framework

`pip install pyomo` · installs (wheel) · licence: BSD-3-Clause · rank 4064 · last release 2026-06-04 · [PyPI](https://pypi.org/project/pyomo/) · [docs](https://pyomo.readthedocs.io/en/stable/) · [source](https://github.com/Pyomo/pyomo)

<details><summary>README extract</summary>

Pyomo is a Python-based open-source software package that supports a
diverse set of optimization capabilities for formulating and analyzing
optimization models. Pyomo can be used to define symbolic problems,
create concrete problem instances, and solve these instances with
standard solvers. Pyomo supports a wide range of problem types,
including: ...

Sections: Pyomo Overview, PyPI &emsp;, Anaconda &emsp;, Tutorials and Examples, Getting Help, Related Packages

</details>

### tensorflow-addons

TensorFlow Addons.

`pip install tensorflow-addons` · does not install on CPython 3.14 · licence: Apache Software License · rank 4257 · last release 2023-11-28 · [PyPI](https://pypi.org/project/tensorflow-addons/)

<details><summary>README extract</summary>

TensorFlow Addons is a repository of contributions that conform to well-
established API patterns, but implement new functionality not available
in core TensorFlow. TensorFlow natively supports a large number of
operators, layers, metrics, losses, and optimizers. ...

</details>

### numdifftools

Solves automatic numerical differentiation problems in one or more variables.

`pip install numdifftools` · installs (wheel) · licence: not stated · rank 4364 · last release 2026-10-25 · [PyPI](https://pypi.org/project/numdifftools/) · [docs](https://numdifftools.readthedocs.io/en/latest/) · [source](https://github.com/pbrod/numdifftools/)

<details><summary>README extract</summary>

The numdifftools library is a suite of tools written in _Python
to solve automatic numerical differentiation problems in one or more variables.
Finite differences are used in an adaptive manner, coupled with a Richardson
extrapolation methodology to provide a maximally accurate result. ...

Example:
```python
>>> fd = nd.Derivative(np.exp)        # 1'st derivative
>>> fdd = nd.Derivative(np.exp, n=2)  # 2'nd derivative
>>> np.allclose(fd(1), 2.7182818284590424)
True
>>> np.allclose(fdd(1), 2.7182818284590424)
True
```

Sections: numdifftools, Getting Started, See also, Documentation and code, Unit tests, References

</details>

### quadprog

Quadratic Programming Solver

`pip install quadprog` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 4746 · last release 2026-10-19 · [PyPI](https://pypi.org/project/quadprog/)

_README extract left out: share-alike licence._

### tensorboard-plugin-profile

XProf Profiler Plugin

`pip install tensorboard-plugin-profile` · installs (wheel) · licence: Apache Software License · rank 4876 · last release 2026-10-29 · [PyPI](https://pypi.org/project/tensorboard-plugin-profile/)

<details><summary>README extract</summary>

An open, scalable, and extensible profiler for the modern ML stack.

About
Installation
Usage
Resources
Citing

XProf offers a number of tools to analyse and visualize the performance of your
model across multiple devices. Some of the tools include:

Features:
A high-level overview of the performance of your model. This
 is an aggregated overview for your host and all devices. It includes:

- Performance summary and breakdown of step times.

- A graph of individual step times. ...

Sections: XProf (+ Tensorboard Profiler Plugin), About, Overview Page, Trace Viewer, Memory Profile, Graph Viewer, Usage, Standalone, With TensorBoard, Command-Line Arguments, Log Directory Structure, Distributed Profiling, Resources, Citing XProf

</details>

### cpsat-logutils

Parse CP-SAT (OR-Tools) solver logs into line-anchored, JSON-serializable pydantic models.

`pip install cpsat-logutils` · installs (wheel) · licence: MIT · rank 4944 · last release 2026-09-06 · [PyPI](https://pypi.org/project/cpsat-logutils/) · [source](https://github.com/d-krupke/cpsat-logutils)

<details><summary>README extract</summary>

Parse CP-SAT
(OR-Tools) solver logs into **line-anchored, JSON-serializable pydantic
models**.

Sections that do not occur in a log are simply `None`. Nothing raises on a log
the parser does not fully understand: unknown sections are kept verbatim in
`log.unparsed`.

Features:
Log analyzers want to show the raw text next to the parsed data. Every scalar is
a `Loc[T]` (`value` + `line`), table rows carry their `line`, every section has
a `span`, and `CpSatLog.blocks` is an ordered index (`kind`, `span`, JSON
pointer ...

Example:
```python
from cpsat_logutils import parse_log

log = parse_log(open("solver.log").read())

log.solver.version.value  # "9.15.6755"
log.solver.parameters.value  # {"max_time_in_seconds": 5, "num_workers": 8, ...}
log.response.status.value  # "OPTIMAL"
...

</details>

### xprof

XProf Profiler Plugin

`pip install xprof` · installs (wheel) · licence: Apache Software License · rank 5004 · last release 2026-10-29 · [PyPI](https://pypi.org/project/xprof/)

<details><summary>README extract</summary>

An open, scalable, and extensible profiler for the modern ML stack.

About
Installation
Usage
Resources
Citing

XProf offers a number of tools to analyse and visualize the performance of your
model across multiple devices. Some of the tools include:

Features:
A high-level overview of the performance of your model. This
 is an aggregated overview for your host and all devices. It includes:

- Performance summary and breakdown of step times.

- A graph of individual step times. ...

Sections: XProf (+ Tensorboard Profiler Plugin), About, Overview Page, Trace Viewer, Memory Profile, Graph Viewer, Usage, Standalone, With TensorBoard, Command-Line Arguments, Log Directory Structure, Distributed Profiling, Resources, Citing XProf

</details>

### PySCIPOpt

Python interface and modeling environment for SCIP

`pip install PySCIPOpt` · installs (wheel) · licence: MIT · rank 5383 · last release 2026-10-11 · [PyPI](https://pypi.org/project/PySCIPOpt/)

<details><summary>README extract</summary>

This project provides an interface from Python to the SCIP Optimization Suite. Starting from v8.0.3, SCIP uses the Apache2.0 license. If you plan to use an earlier version of SCIP, please review SCIP's license restrictions.

Documentation ...

Example:
```python
from pyscipopt import Model
```

</details>

### gmpy2

gmpy2 interface to GMP, MPFR, and MPC for Python

`pip install gmpy2` · installs (wheel) · licence: LGPL-3.0-or-later · rank 5426 · last release 2026-10-04 · [PyPI](https://pypi.org/project/gmpy2/)

_README extract left out: share-alike licence._

### munkres

The Munkres (Hungarian) algorithm for the assignment problem: fast, typed, dependency-free.

`pip install munkres` · installs (wheel) · licence: Apache-2.0 · rank 5486 · last release 2026-10-18 · [PyPI](https://pypi.org/project/munkres/) · [docs](https://github.com/iameishit/Paldita-munkres#readme)

<details><summary>README extract</summary>

The Munkres (Hungarian) algorithm for the *assignment problem*: given a cost
for every (worker, job) pair, find the one-to-one assignment with the lowest
total cost. Pure Python, no dependencies, fully typed, thread-safe.

Example:
```python
from munkres import Munkres

cost = [[4, 1, 3],
        [2, 0, 5],
        [3, 2, 2]]

pairs = Munkres().compute(cost)
print(pairs)                                   # [(0, 1), (1, 0), (2, 2)]
print(sum(costr for r, c in pairs))       # 5
```

...

</details>

### pingouin

Pingouin: statistical package for Python

`pip install pingouin` · installs (wheel) · licence: GPL-3.0 · rank 5523 · last release 2026-09-26 · [PyPI](https://pypi.org/project/pingouin/)

_README extract left out: share-alike licence._

### moyopy

Python binding of Moyo

`pip install moyopy` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 5553 · last release 2026-10-30 · [PyPI](https://pypi.org/project/moyopy/)

<details><summary>README extract</summary>

Python interface of moyo, a fast and robust crystal symmetry finder.

- Document: <
- PyPI: <

</details>

### loop-rate-limiters

Loop rate limiters.

`pip install loop-rate-limiters` · installs (wheel) · licence: Apache Software License · rank 5671 · last release 2025-08-13 · [PyPI](https://pypi.org/project/loop-rate-limiters/) · [source](https://github.com/stephane-caron/loop-rate-limiters)

<details><summary>README extract</summary>

Simple loop frequency regulators in Python with an API similar to ``rospy.Rate``:

A similar ``AsyncRateLimiter`` class is available for asynchronous code.

Example:
```python
import asyncio
from loop_rate_limiters import AsyncRateLimiter

async def main():
    rate = AsyncRateLimiter(frequency=400.0)
    while True:
        loop_time = asyncio.get_event_loop().time()
        print(f"Hello from loop at {loop_time:.3f} s")
        await rate.sleep()

asyncio.run(main())
```

Sections: Loop rate limiters, From conda-forge, From PyPI, Usage, See also

</details>

### python-markdown-math

Math extension for Python-Markdown

`pip install python-markdown-math` · installs (wheel) · licence: BSD-3-Clause · rank 5752 · last release 2025-04-10 · [PyPI](https://pypi.org/project/python-markdown-math/)

<details><summary>README extract</summary>

[][Actions]

This extension adds math formulas support to [Python-Markdown].

Installation

</details>

### python-flint

Bindings for FLINT

`pip install python-flint` · installs (wheel) · licence: MIT AND LGPL-3.0-or-later · rank 6543 · last release 2026-07-03 · [PyPI](https://pypi.org/project/python-flint/) · [docs](https://python-flint.readthedocs.io/en/latest/) · [source](https://github.com/flintlib/python-flint)

_README extract left out: share-alike licence._

### empirical-calibration

Package for empirical calibration

`pip install empirical-calibration` · installs from source (sdist only) · licence: Apache Software License · rank 6600 · last release 2024-05-05 · [PyPI](https://pypi.org/project/empirical-calibration/)

### jmp

JMP is a Mixed Precision library for JAX.

`pip install jmp` · installs (wheel) · licence: Apache Software License · rank 6610 · last release 2023-01-30 · [PyPI](https://pypi.org/project/jmp/)

<details><summary>README extract</summary>

Installation
| Examples
| Policies
| Loss scaling
| Citing JMP
| References

Mixed precision training [[0]] is a technique that mixes the use of full and
half precision floating point numbers during training to reduce the memory
bandwidth requirements and improve the computational efficiency of a given
model. ...

Example:
```python
import jax
import jax.numpy as jnp
import jmp

half = jnp.float16  # On TPU this should be jnp.bfloat16.
full = jnp.float32
```

Sections: Mixed precision training in [JAX], Examples, Policies, Loss scaling, Citing JMP, References

</details>

### tb-nightly

TensorBoard lets you watch Tensors Flow

`pip install tb-nightly` · installs (wheel) · licence: Apache Software License · rank 7109 · last release 2025-10-23 · [PyPI](https://pypi.org/project/tb-nightly/)

<details><summary>README extract</summary>

TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

Releases prior to 1.6.0 were published under the ``tensorflow-tensorboard`` name
and may be found at

</details>

### klujax

a KLU solver for JAX

`pip install klujax` · installs (wheel) · licence: LGPL-2.0-only · rank 7268 · last release 2026-11-06 · [PyPI](https://pypi.org/project/klujax/)

_README extract left out: share-alike licence._

### pytransform3d

3D transformations for Python

`pip install pytransform3d` · installs (wheel) · licence: BSD License · rank 7558 · last release 2026-10-06 · [PyPI](https://pypi.org/project/pytransform3d/)

<details><summary>README extract</summary>

A Python library for transformations in three dimensions.

pytransform3d offers...

* operations like concatenation and inversion for most common representations
 of rotation (orientation) and translation (position)
* conversions between those representations
* clear documentation of transformation conventions
* tight coupling with matplotlib to ...

Example:
```python
import numpy as np
import matplotlib.pyplot as plt
from pytransform3d import rotations as pr
from pytransform3d import transformations as pt
from pytransform3d.transform_manager import TransformManager

rng = np.random.default_rng(0)

ee2robot = pt.transform_from_pq(
    np.hstack((np.array([0.4, -0.3, 0.5]),
...
```

Sections: pytransform3d, Gallery, Example, Documentation, Tests

</details>

### ropwr

RoPWR: Robust Piecewise Regression

`pip install ropwr` · installs (wheel) · licence: Apache Software License · rank 8414 · last release 2026-01-23 · [PyPI](https://pypi.org/project/ropwr/)

<details><summary>README extract</summary>

RoPWR is a library written in Python implementing several mathematical
programming formulations to compute the optimal continuous/discontinuous
piecewise polynomial regression given a list of split points.

Read the documentation at:

RoPWR is distributed under the Apache Software License (Apache 2.0).

</details>

### optbinning

OptBinning: The Python Optimal Binning library

`pip install optbinning` · installs (wheel) · licence: Apache-2.0 · rank 8447 · last release 2026-09-12 · [PyPI](https://pypi.org/project/optbinning/) · [docs](http://gnpalencia.org/optbinning/)

<details><summary>README extract</summary>

OptBinning is a library written in Python implementing a rigorous and flexible mathematical programming formulation to solve the optimal binning problem for a binary, continuous and multiclass target type, incorporating constraints not previously addressed.

 * Optimal binning: mathematical programming formulation. ...

Example:
```python
import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

variable = "mean radius"
x = df[variable].values
y = data.target
```

Sections: OptBinning, Dependencies, Getting started, Tutorials, Example: Optimal binning with binary target, Example: Optimal binning 2D with binary target, Example: Scorecard with continuous target, Benchmarks, Who uses OptBinning?

</details>

### mip

Python tools for Modeling and Solving Mixed-Integer Linear Programs (MIPs)

`pip install mip` · installs (wheel) · licence: Eclipse Public License 2.0 (EPL-2.0) · rank 8724 · last release 2026-11-07 · [PyPI](https://pypi.org/project/mip/) · [source](https://github.com/coin-or/python-mip)

<details><summary>README extract</summary>

Package website:

Python MIP is a collection of Python tools for the modeling and solution
of Mixed-Integer Linear programs (MIPs). MIP syntax was inspired by
Pulp. Just like
CyLP it also provides access to
advanced solver features like cut generation, lazy constraints, MIPstarts
and solution Pools. ...

Sections: Python MIP (Mixed-Integer Linear Programming) Tools, Examples, Documentation, Mailing list

</details>

### colormath

Color math and conversion library.

`pip install colormath` · installs from source (sdist only) · licence: BSD License · rank 8731 · last release 2017-12-27 · [PyPI](https://pypi.org/project/colormath/)

<details><summary>README extract</summary>

This module implements a large number of different color operations such as
color space conversions, Delta E, and density to spectral.

* numpy
* NetworkX 2.0+
* Python 2.7 or Python 3.5+

Sections: Python Color Math Module (colormath), Requirements, Documentation, Legal Mumbo Jumbo

</details>

### graspologic-native

(no summary)

`pip install graspologic-native` · installs (wheel) · licence: MIT License · rank 8747 · last release 2026-06-14 · [PyPI](https://pypi.org/project/graspologic-native/) · [source](https://github.com/graspologic-org/graspologic-native)

### ziamath

Render MathML and LaTeX Math to SVG in pure Python without Latex installation

`pip install ziamath` · installs (wheel) · licence: MIT License · rank 8962 · last release 2026-02-06 · [PyPI](https://pypi.org/project/ziamath/) · [docs](https://ziamath.readthedocs.io) · [source](https://github.com/cdelker/ziamath)

<details><summary>README extract</summary>

Render MathML or LaTeX Math expressions as SVG using pure Python. Does not require a Latex installation, nor a network connection.

Ziamath comes with the STIXTwoMath-Regular font installed for use by default.
Other Math-enabled Open Type fonts (TTF or OTF files) may also be used.

Documentation is available at readthedocs. ...

</details>

### iminuit

Jupyter-friendly Python frontend for MINUIT2 in C++

`pip install iminuit` · installs (wheel) · licence: MIT AND LGPL-2.1-or-later · rank 9301 · last release 2026-09-17 · [PyPI](https://pypi.org/project/iminuit/) · [docs](https://scikit-hep.org/iminuit) · [source](https://github.com/scikit-hep/iminuit)

_README extract left out: share-alike licence._

### cbcbox

Binary distribution of the CBC MILP solver (COIN-OR Branch and Cut)

`pip install cbcbox` · installs (wheel) · licence: Eclipse Public License 2.0 (EPL-2.0) · rank 9306 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cbcbox/)

<details><summary>README extract</summary>

cbcbox is a high-performance, self-contained Python distribution of the
CBC MILP solver (COIN-OR Branch and Cut),
built from the latest COIN-OR `master` branch.

On x86_64 (Linux, macOS, Windows) the wheel ships both a Haswell-optimised binary
(AVX2/FMA) for maximum speed and a generic build with
runtime CPU dispatch for compatibility with any ...

Features:
- Haswell-optimised & generic builds — on x86_64 Linux, macOS, and Windows the wheel
 ships two complete solver stacks: a *Haswell* build (OpenBLAS AVX2/FMA kernel) for
 maximum throughput, and a *generic* build (`DYNAMIC_ARCH` runtime dispatch) ...

Example:
```python
import cbcbox
import subprocess

# Path to the cbc binary (cbc.exe on Windows).
cbcbox.cbc_bin_path()
...

</details>

### google-vizier

Open Source Vizier: Distributed service framework for blackbox optimization and research.

`pip install google-vizier` · installs (wheel) · licence: Apache Software License · rank 9746 · last release 2025-02-01 · [PyPI](https://pypi.org/project/google-vizier/)

<details><summary>README extract</summary>

Google AI Blog
| Getting Started
| Documentation
| Installation
| Citing and Highlights

OSS Vizier is a Python-based service for black-box optimization and research, based on Google Vizier, one of the first hyperparameter tuning services designed to work at scale.

 OSS Vizier's distributed client-server system. Animation by Tom Small.

Example:
```python
from vizier.service import clients
from vizier.service import pyvizier as vz

# Objective function to maximize.
def evaluate(w: float, x: int, y: float, z: str) -> float:
  return w2 - y2 + x * ord(z)

# Algorithm, search space, and metrics.
study_config = vz.StudyConfig(algorithm='DEFAULT')
...
```

Sections: What is Open Source (OSS) Vizier?, Getting Started, Documentation, Citing and Highlights

</details>

### galois

A performant NumPy extension for Galois fields and their applications

`pip install galois` · installs (wheel) · licence: MIT License · rank 9846 · last release 2026-05-02 · [PyPI](https://pypi.org/project/galois/) · [docs](https://mhostetter.github.io/galois/latest/) · [source](https://github.com/mhostetter/galois)

<details><summary>README extract</summary>

The `galois` library is a Python 3 package that extends NumPy arrays to operate over finite fields.

> Enjoying the library? Give us a :star: on GitHub!

The user creates a `FieldArray` subclass using `GF = galois.GF(p**m)`.
`GF` is a subclass of `np.ndarray` and its constructor `x = GF(array_like)` mimics the signature of `np.array()`. ...

Features:
- Supports all Galois fields $\mathrm{GF}(p^m)$, including arbitrarily large fields.
- Faster than native NumPy. `GF(x) * GF(y)` is often faster than `(x * y) % p` for $\mathrm{GF}(p)$. ...

Example:
```python
In [3]: GF = galois.GF(3**5)

In [4]: print(GF.properties)
Galois Field:
  name: GF(3^5)
  characteristic: 3
  degree: 5
  order: 243
  irreducible_poly: x^5 + 2x + 1
  is_primitive_poly: True
  primitive_element: x
```

...

</details>

### geomdl

Object-oriented B-Spline and NURBS evaluation library

`pip install geomdl` · installs (wheel) · licence: MIT · rank 10087 · last release 2025-05-23 · [PyPI](https://pypi.org/project/geomdl/) · [docs](http://nurbs-python.readthedocs.io/) · [source](https://github.com/orbingol/NURBS-Python.git)

<details><summary>README extract</summary>

NURBS-Python (geomdl) is a pure Python, self-contained, object-oriented B-Spline and NURBS spline library.

Features:
NURBS-Python (geomdl) provides convenient data structures and highly customizable API for rational and non-rational
splines along with the efficient and extensible implementations of the following algorithms: ...

Sections: NURBS-Python (geomdl), Introduction, Features, Further reading, Citing

</details>

### pyfixest

Fast high dimensional fixed effect estimation following syntax of the fixest R package.

`pip install pyfixest` · installs (wheel) · licence: MIT License · rank 10102 · last release 2026-06-11 · [PyPI](https://pypi.org/project/pyfixest/) · [docs](https://pyfixest.com) · [source](https://github.com/py-econometrics/pyfixest)

<details><summary>README extract</summary>

[][chat-url]

Docs · Quickstart · Function & API Reference · DeepWiki · Benchmarks · Contributing · Changelog

`PyFixest` is a Python package for fast high-dimensional fixed effects regression.

The package aims to mimic the syntax and functionality of Laurent Bergé's formidable fixest package as closely as Python allows. ...

Features:
- Estimation
 - OLS, WLS, IV, and GLMs (Poisson, logit, probit, gaussian) with high-dimensional fixed effects
 - Different demeaning backends (MAP, within LSMR, torch LSMR) on CPU and GPU
 - Fast quantile regression via an interior-point solver
 - ...

Example:
```python
import pyfixest as pf

data = pf.get_data()
pf.feols("Y ~ X1 | f1 + f2", data=data).summary()
```

Sections: Features, Quickstart, Benchmarks, Learn More

</details>

### dm-haiku

Haiku is a library for building neural networks in JAX.

`pip install dm-haiku` · installs (wheel) · licence: Apache Software License · rank 10483 · last release 2026-07-27 · [PyPI](https://pypi.org/project/dm-haiku/)

<details><summary>README extract</summary>

Overview
| Why Haiku?
| Quickstart
| Installation
| Examples
| User manual
| Documentation
| Citing Haiku

> [!IMPORTANT]
> 📣 **As of July 2023 [Google DeepMind] recommends that new projects adopt
> [Flax] instead of Haiku. ...

Features:
[JAX] is a numerical computing library that combines NumPy, automatic
differentiation, and first-class GPU/TPU support.

Haiku is a simple neural network library for JAX that enables users to use
familiar object-oriented programming models while ...

Example:
```python
import haiku as hk
import jax.numpy as jnp

def softmax_cross_entropy(logits, labels):
  one_hot = jax.nn.one_hot(labels, logits.shape[-1])
  return -jnp.sum(jax.nn.log_softmax(logits) * one_hot, axis=-1)

def loss_fn(images, labels):
  mlp = hk.Sequential([
...

</details>

### Theano-PyMC

Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.

`pip install Theano-PyMC` · installs from source (sdist only) · licence: BSD License · rank 10591 · last release 2021-01-22 · [PyPI](https://pypi.org/project/Theano-PyMC/)

<details><summary>README extract</summary>

Theano is a Python library that allows you to define, optimize, and efficiently evaluate mathematical expressions involving multi-dimensional arrays. It is built on top of NumPy. Theano features:

 * tight integration with NumPy: a similar interface to NumPy's. numpy.ndarrays are also used internally in Theano-compiled functions. ...

</details>

### aimmspy

Python bindings for the AIMMS optimization platform, built with pybind11 for seamless C++ integration. Enables efficient data exchange and interaction with AIMMS projects using pandas, polars, and pyarrow. Ideal for advanced optimization workflows requiring high-performance native code.

`pip install aimmspy` · installs (wheel) · licence: MIT License · rank 10595 · last release 2026-09-23 · [PyPI](https://pypi.org/project/aimmspy/)

<details><summary>README extract</summary>

With this library it is possible to interact with AIMMS models from Python, enabling high-performance, headless interaction with AIMMS models from within Python scripts.

Features:
`aimmspy` is a Python module built on pybind11 for tight C++ integration, enabling efficient interaction with AIMMS models. With `aimmspy`, you can: ...

Example:
```python
from aimmspy.project.project import Project, Model
from aimmspy.utils import find_aimms_path

# Initialize connection to AIMMS project
project = Project(
    # path to the AIMMS bin folder (or Lib on Linux)
    aimms_path=find_aimms_path("25.5.4.3"),
    # path to AIMMS project
    aimms_project_file="path/to/your/project.aimms",
    # license url
...
```

...

</details>

### solidpython2

Python interface to the OpenSCAD declarative geometry language

`pip install solidpython2` · installs (wheel) · licence: OSI Approved; GNU Lesser General Public License v2 or later (LGPLv2+) · rank 10759 · last release 2025-08-16 · [PyPI](https://pypi.org/project/solidpython2/) · [source](https://github.com/jeff-dh/SolidPython)

_README extract left out: share-alike licence._

### passagemath-homfly

passagemath: Homfly polynomials of knots/links with libhomfly

`pip install passagemath-homfly` · installs (wheel) · licence: GPL-2.0-or-later · rank 10801 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-homfly/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### glpk

PyGLPK, a Python module encapsulating GLPK.

`pip install glpk` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 11551 · last release 2024-10-07 · [PyPI](https://pypi.org/project/glpk/)

_README extract left out: share-alike licence._

### quantile-python

Python Implementation of Graham Cormode and S. Muthukrishnan's Effective Computation of Biased Quantiles over Data Streams in ICDE'05

`pip install quantile-python` · installs from source (sdist only) · licence: Apache Software License · rank 11681 · last release 2015-02-11 · [PyPI](https://pypi.org/project/quantile-python/)

### packingsolver

A solver for geometrical packing and cutting-stock problems

`pip install packingsolver` · installs (wheel) · licence: MIT · rank 11687 · last release 2026-11-08 · [PyPI](https://pypi.org/project/packingsolver/)

<details><summary>README extract</summary>

A state-of-the-art solver for cutting and packing problems

 Nesting, cutting optimization, load planning etc

 Online solver ·
 Documentation ·
 Ask a question

PackingSolver computes cutting and loading plans. ...

Features:
| Problem type | Example |
|:--|:--|
| Rectangles, guillotine cuts `rectangleguillotine`
Two-dimensional rectangles cut with edge-to-edge (guillotine) cuts ...

Example:
```python
import packingsolver.rectangleguillotine as psg

instance_builder = psg.InstanceBuilder()
instance_builder.set_objective(psg.Objective.BinPackingWithLeftovers)
instance_builder.add_bin_type(1000, 700, copies=5)
instance_builder.add_item_type(250, 200, copies=2)
instance_builder.add_item_type(150, 300, copies=2)
...
```

...

</details>

### antropy

AntroPy: entropy and complexity of time-series in Python

`pip install antropy` · installs (wheel) · licence: BSD (3-clause) · rank 12298 · last release 2026-10-17 · [PyPI](https://pypi.org/project/antropy/)

<details><summary>README extract</summary>

AntroPy is a Python package for computing entropy and fractal dimension measures of
time-series. It is designed for speed (Numba JIT compilation) and ease of use, and works on
both 1-D and N-D arrays. Typical use cases include feature extraction from physiological signals
(e.g. EEG, ECG, EMG), and signal processing research.

- Documentation ...

Example:
```python
import numpy as np
import antropy as ant

np.random.seed(1234567)
x = np.random.normal(size=3000)

print(ant.perm_entropy(x, normalize=True))
print(ant.spectral_entropy(x, sf=100, method='welch', normalize=True))
print(ant.svd_entropy(x, normalize=True))
print(ant.app_entropy(x))
print(ant.sample_entropy(x))
...
```

Sections: Functions, Entropy, Fractal dimension, Quick start, Entropy measures, N-D arrays, Performance

</details>

### powerlaw

Toolbox for testing if a probability distribution fits a power law

`pip install powerlaw` · installs (wheel) · licence: MIT License · rank 12446 · last release 2026-01-02 · [PyPI](https://pypi.org/project/powerlaw/)

<details><summary>README extract</summary>

`powerlaw` is a toolbox implementing the statistical methods developed in
Clauset et al. 2007 and
Klaus et al. 2011
to fit heavy-tailed distributions like power laws. Academics, please cite as:

Jeff Alstott, Ed Bullmore, Dietmar Plenz. (2014). powerlaw: a Python package
for analysis of heavy-tailed distributions.
PLoS ONE 9(1): e85777 ...

Example:
```python
import powerlaw
import numpy as np

data = np.array([1.7, 3.2, 5.4, 2.1, 1.5, 2.8]) # data can be a list or a numpy array
fit = powerlaw.Fit(data)

print(fit.power_law.alpha)
print(fit.power_law.xmin)

R, p = fit.distribution_compare('power_law', 'lognormal')
```

Sections: Basic Usage, Quick Links, Mailing List

</details>

### passagemath-glpk

passagemath: Linear and mixed integer linear optimization backend using GLPK

`pip install passagemath-glpk` · installs (wheel) · licence: GPL-2.0-or-later · rank 12546 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-glpk/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-libecm

passagemath: Elliptic curve method for integer factorization using GMP-ECM

`pip install passagemath-libecm` · installs (wheel) · licence: GPL-2.0-or-later · rank 12600 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-libecm/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-meataxe

passagemath: Matrices over small finite fields with meataxe

`pip install passagemath-meataxe` · installs (wheel) · licence: GPL-2.0-or-later · rank 12606 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-meataxe/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### Theano

Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.

`pip install Theano` · installs from source (sdist only) · licence: BSD License · rank 12638 · last release 2020-07-27 · [PyPI](https://pypi.org/project/Theano/)

<details><summary>README extract</summary>

Theano is a Python library that allows you to define, optimize, and efficiently evaluate mathematical expressions involving multi-dimensional arrays. It is built on top of NumPy. Theano features:

 * tight integration with NumPy: a similar interface to NumPy's. numpy.ndarrays are also used internally in Theano-compiled functions. ...

</details>

### passagemath-planarity

passagemath: Graph planarity with the edge addition planarity suite

`pip install passagemath-planarity` · installs (wheel) · licence: GPL-2.0-or-later · rank 12676 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-planarity/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-sirocco

passagemath: Certified root continuation with sirocco

`pip install passagemath-sirocco` · installs (wheel) · licence: GPL-2.0-or-later · rank 12758 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-sirocco/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### causalmodels

Causal models in Python

`pip install causalmodels` · installs (wheel) · licence: MIT License · rank 12793 · last release 2016-07-20 · [PyPI](https://pypi.org/project/causalmodels/)

<details><summary>README extract</summary>

causalmodels in Python.

Example:
```python
>>> import numpy as np
>>> import pandas as pd
>>> import causalmodels as cm
>>> a = np.random.laplace(size=500)
>>> b = np.random.laplace(size=500) + a
>>> c = np.random.laplace(size=500) + a + b
>>> data = pd.DataFrame({'a': a, 'b': b, 'c': c})
>>> model = cm.DirectLiNGAM(data.values, data.columns)
>>> results = model.fit()
>>> results.order
...
```

Sections: causalmodels, instalation, usage

</details>

### passagemath-rankwidth

passagemath: Rankwidth and rank decompositions of graphs with rw

`pip install passagemath-rankwidth` · installs (wheel) · licence: GPL-2.0-or-later · rank 12994 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-rankwidth/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-coxeter3

passagemath: Coxeter groups, Bruhat ordering, Kazhdan-Lusztig polynomials with coxeter3

`pip install passagemath-coxeter3` · installs (wheel) · licence: GPL-2.0-or-later · rank 13004 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-coxeter3/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### hyppo

A comprehensive independence testing package

`pip install hyppo` · installs (wheel) · licence: MIT License · rank 13116 · last release 2025-05-24 · [PyPI](https://pypi.org/project/hyppo/)

<details><summary>README extract</summary>

hyppo (HYPothesis Testing in PythOn, pronounced "Hippo") is an open-source
software package for multivariate hypothesis testing. We decided to develop hyppo for
the following reasons: ...

</details>

### graspologic

A set of Python modules for graph statistics

`pip install graspologic` · does not install on CPython 3.14 · licence: MIT License · rank 13196 · last release 2025-09-08 · [PyPI](https://pypi.org/project/graspologic/) · [source](https://github.com/graspologic-org/graspologic)

<details><summary>README extract</summary>

<!-- omit in toc -->

<!-- no toc -->
- Overview
- Documentation
- System Requirements
- Installation Guide
- Contributing
- License
- Issues
- Citing `graspologic`

Features:
A graph, or network, provides a mathematically intuitive representation of data with some sort of relationship between items. For example, a social network can be represented as a graph by considering all participants in the social network as nodes, ...

Sections: graspologic, Overview, Documentation, System Requirements, Hardware requirements, Software requirements, OS Requirements, Issues, Citing `graspologic`

</details>

### automata-lib

A Python library for simulating finite automata, pushdown automata, and Turing machines

`pip install automata-lib` · installs (wheel) · licence: MIT · rank 13238 · last release 2026-01-02 · [PyPI](https://pypi.org/project/automata-lib/) · [docs](https://caleb531.github.io/automata/) · [source](https://github.com/caleb531/automata)

<details><summary>README extract</summary>

*Copyright 2016-2026 Caleb Evans*
*Released under the MIT license*

Links:
- Documentation
- Examples
- Example Notebooks
- Migration Guide
- API

Automata is a Python 3 library implementing structures and algorithms for manipulating finite automata,
pushdown automata, and Turing machines. ...

</details>

### scann

Scalable Nearest Neighbor search library

`pip install scann` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 13377 · last release 2025-08-29 · [PyPI](https://pypi.org/project/scann/)

<details><summary>README extract</summary>

ScaNN (Scalable Nearest Neighbors) is a method for efficient vector similarity
search at scale. This code implements [1, 2], which includes search space
pruning and quantization for Maximum Inner Product Search and also supports
other distance functions such as Euclidean distance. ...

Sections: ScaNN, Using ScaNN with TensorFlow, Integration with TensorFlow Serving, Usage, Building from source

</details>

### passagemath-libbraiding

passagemath: Braid computations with libbraiding

`pip install passagemath-libbraiding` · installs (wheel) · licence: GPL-2.0-or-later · rank 13379 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-libbraiding/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-mcqd

passagemath: Finding maximum cliques with mcqd

`pip install passagemath-mcqd` · installs (wheel) · licence: GPL-2.0-or-later · rank 13488 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-mcqd/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### openturns

Uncertainty treatment library

`pip install openturns` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 13609 · last release 2026-06-19 · [PyPI](https://pypi.org/project/openturns/)

_README extract left out: share-alike licence._

### passagemath-groups

passagemath: Groups and Invariant Theory

`pip install passagemath-groups` · installs (wheel) · licence: GPL-2.0-or-later · rank 13727 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-groups/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-bliss

passagemath: Graph (iso/auto)morphisms with bliss

`pip install passagemath-bliss` · installs (wheel) · licence: GPL-2.0-or-later · rank 13845 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-bliss/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-rubiks

passagemath: Algorithms for Rubik's cube

`pip install passagemath-rubiks` · installs (wheel) · licence: GPL-2.0-or-later · rank 13851 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-rubiks/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-tdlib

passagemath: Tree decompositions with tdlib

`pip install passagemath-tdlib` · installs (wheel) · licence: GPL-2.0-or-later · rank 13879 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-tdlib/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-plantri

passagemath: Generating planar graphs with plantri and fullgen

`pip install passagemath-plantri` · installs (wheel) · licence: GPL-2.0-or-later · rank 13887 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-plantri/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-kissat

passagemath: Interface to the SAT solver kissat

`pip install passagemath-kissat` · installs (wheel) · licence: GPL-2.0-or-later · rank 13939 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-kissat/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### spgrep

On-the-fly generator of space-group irreducible representations

`pip install spgrep` · installs (wheel) · licence: BSD License · rank 13976 · last release 2026-10-12 · [PyPI](https://pypi.org/project/spgrep/)

<details><summary>README extract</summary>

Spgrep is a Python package of on-the-fly generator of space-group irreducible representations.

- GitHub: <
- Document: <
- PyPI: <

Features:
- Enumerate the following irreducible representations (irreps) of space groups from spglib's cell and kpoints:
 - Linear irreps
 - Physically irreps (irreps over real numbers)
 - Projective irreps for spnior
 - Projective irreducible ...

Example:
```python
from spgrep import get_spacegroup_irreps
from spgrep.representation import get_character

# Rutile structure (
# P4_2/mnm (No. 136)
a = 4.603
c = 2.969
x_4f = 0.3046
lattice = [
    [a, 0, 0],
    [0, a, 0],
    [0, 0, c],
]
positions = [
    [0, 0, 0],  # Ti(2a)
    [0.5, 0.5, 0.5],  # Ti(2a)
    [x_4f, x_4f, 0],  # O(4f)
...
```

Sections: Spgrep, Features, Usage

</details>

### hsnf

Computing Hermite normal form and Smith normal form.

`pip install hsnf` · installs (wheel) · licence: MIT · rank 14091 · last release 2026-03-31 · [PyPI](https://pypi.org/project/hsnf/) · [docs](https://hsnf.readthedocs.io/en/latest/) · [source](https://github.com/lan496/hsnf)

<details><summary>README extract</summary>

<!-- -->

Computing Hermite normal form and Smith normal form with transformation matrices.

- Document: <
- Document(develop): <
- Github: <
- PyPI: <

Example:
```python
import numpy as np
from hsnf import column_style_hermite_normal_form, row_style_hermite_normal_form, smith_normal_form

# Integer matrix to be decomposed
M = np.array(
    [
        [-6, 111, -36, 6],
        [5, -672, 210, 74],
        [0, -255, 81, 24],
    ]
)

# Smith normal form
D, L, R = smith_normal_form(M)
"""
D = array([
...
```

Sections: hsnf, Usage, References

</details>

### passagemath-lrslib

passagemath: Reverse search for vertex enumeration and convex hulls with lrslib

`pip install passagemath-lrslib` · installs (wheel) · licence: GPL-2.0-or-later · rank 14095 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-lrslib/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-glucose

passagemath: Interface to the SAT solver glucose

`pip install passagemath-glucose` · installs (wheel) · licence: GPL-2.0-or-later · rank 14142 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-glucose/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-m4ri-m4rie

passagemath: Linear Algebra with m4ri and m4rie

`pip install passagemath-m4ri-m4rie` · installs (wheel) · licence: GPL-2.0-or-later · rank 14230 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-m4ri-m4rie/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-buckygen

passagemath: Generation of nonisomorphic fullerenes with buckygen

`pip install passagemath-buckygen` · installs (wheel) · licence: GPL-2.0-or-later · rank 14246 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-buckygen/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-categories

passagemath: Sage categories and basic rings

`pip install passagemath-categories` · installs (wheel) · licence: GPL-2.0-or-later · rank 14248 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-categories/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### optlang

Formulate optimization problems using sympy expressions and solve them using interfaces to third-party optimization software (e.g. GLPK).

`pip install optlang` · installs (wheel) · licence: Apache Software License · rank 14270 · last release 2026-06-02 · [PyPI](https://pypi.org/project/optlang/) · [docs](https://optlang.readthedocs.io) · [source](https://github.com/opencobra/optlang)

<details><summary>README extract</summary>

*Sympy based mathematical programming language*

Optlang is a Python package for solving mathematical optimization
problems, i.e. maximizing or minimizing an objective function over a set
of variables subject to a number of constraints. ...

Example:
```python
from optlang import Model, Variable, Constraint, Objective

# All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.
x1 = Variable('x1', lb=0)
x2 = Variable('x2', lb=0)
x3 = Variable('x3', lb=0)

# A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).
...
```

Sections: optlang, Dependencies, Example, Using a particular solver, Documentation, Future outlook

</details>

### passagemath-benzene

passagemath: Generate fusene and benzenoid graphs with benzene

`pip install passagemath-benzene` · installs (wheel) · licence: GPL-2.0-or-later · rank 14321 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-benzene/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### passagemath-objects

passagemath: Sage objects, elements, parents, categories, coercion, metaclasses

`pip install passagemath-objects` · installs (wheel) · licence: GPL-2.0-or-later · rank 14338 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-objects/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### pypardiso

Python interface to the Intel MKL Pardiso library to solve large sparse linear systems of equations

`pip install pypardiso` · installs (wheel) · licence: BSD-3-Clause · rank 14456 · last release 2025-11-02 · [PyPI](https://pypi.org/project/pypardiso/) · [source](https://github.com/haasad/PyPardiso.git)

<details><summary>README extract</summary>

PyPardiso is a python package to solve large sparse linear systems of equations with the Intel oneAPI Math Kernel Library PARDISO solver, a shared-memory multiprocessing parallel direct sparse solver.

PyPardiso provides the same functionality as SciPy's scipy.sparse.linalg.spsolve for solving the sparse linear system `Ax=b`. ...

Example:
```python
In [1]: import pypardiso

In [2]: import numpy as np

In [3]: import scipy.sparse as sp

In [4]: A = sp.rand(10, 10, density=0.5, format='csr')

In [5]: A
Out[5]:
<10x10 sparse matrix of type '<class 'numpy.float64'>'
    with 50 stored elements in Compressed Sparse Row format>

In [6]: b = np.random.rand(10)

In [7]: x = pypardiso.spsolve(A, b)

...
```

Sections: PyPardiso, Basic usage

</details>

### passagemath-cddlib

passagemath: Polyhedral computation with cddlib

`pip install passagemath-cddlib` · installs (wheel) · licence: GPL-2.0-or-later · rank 14468 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-cddlib/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### findiff

A Python package for finite difference derivatives in any number of dimensions.

`pip install findiff` · installs (wheel) · licence: MIT License · rank 14524 · last release 2026-10-22 · [PyPI](https://pypi.org/project/findiff/) · [source](https://github.com/maroba/findiff)

<details><summary>README extract</summary>

A Python package for finite difference numerical derivatives and partial differential equations in
any number of dimensions.

* Differentiate arrays of any number of dimensions along any axis with any desired accuracy order
* Accurate treatment of grid boundary
* Can handle uniform and non-uniform grids
* Can handle arbitrary linear combinations ...

Example:
```python
from findiff import Diff, Id, PDE

shape = (300, )
t = numpy.linspace(0, 10, shape[0])
dt = t[1]-t[0]

L = Diff(0, dt)**2 - Diff(0, dt) + 5 * Id()
f = numpy.cos(2*t)

bc = BoundaryConditions(shape)
bc[0] = 0
bc[-1] = 1

pde = PDE(L, f, bc)
u = pde.solve()
```

...

</details>

### pyvcg

Verification Condition Generator

`pip install pyvcg` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14622 · last release 2026-07-12 · [PyPI](https://pypi.org/project/pyvcg/) · [docs](https://github.com/pages/florianschanda/PyVCG/) · [source](https://github.com/florianschanda/PyVCG)

_README extract left out: share-alike licence._

### dcor

dcor: distance correlation and energy statistics in Python.

`pip install dcor` · installs (wheel) · licence: MIT License · rank 14750 · last release 2026-01-17 · [PyPI](https://pypi.org/project/dcor/) · [docs](https://dcor.readthedocs.io) · [source](https://github.com/vnmabus/dcor)

<details><summary>README extract</summary>

dcor: distance correlation and energy statistics in Python.

E-statistics are functions of distances between statistical observations
in metric spaces.

Distance covariance and distance correlation are
dependency measures between random vectors introduced in [SRB07]_ with
a simple E-statistic estimator. ...

Sections: dcor, Requirements, Citing dcor, Documentation, References

</details>

### passagemath-cmr

passagemath: Combinatorial matrix recognition

`pip install passagemath-cmr` · installs (wheel) · licence: GPL-2.0-or-later · rank 14790 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-cmr/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### opensimplex

OpenSimplex is a noise generation function like Perlin or Simplex noise, but better.

`pip install opensimplex` · installs (wheel) · licence: MIT License · rank 14819 · last release 2024-05-01 · [PyPI](https://pypi.org/project/opensimplex/)

<details><summary>README extract</summary>

[OpenSimplex] is a noise generation function like [Perlin] or [Simplex] noise, but better.

 OpenSimplex noise is an n-dimensional gradient noise function that was
 developed in order to overcome the patent-related issues surrounding
 Simplex noise, while continuing to also avoid the visually-significant
 directional artifacts characteristic of ...

Sections: OpenSimplex Noise, Usage, API, FAQ, Example Output

</details>

### passagemath-standard-no-symbolics

passagemath: Sage library without the symbolics subsystem

`pip install passagemath-standard-no-symbolics` · installs (wheel) · licence: GPL-2.0-or-later · rank 14839 · last release 2026-10-12 · [PyPI](https://pypi.org/project/passagemath-standard-no-symbolics/) · [docs](https://passagemath.org/docs/latest)

_README extract left out: share-alike licence._

### Tree

A package for creating and drawing trees

`pip install Tree` · installs from source (sdist only) · licence: MIT License · rank 14881 · last release 2018-07-03 · [PyPI](https://pypi.org/project/Tree/)

<details><summary>README extract</summary>

Python package, which you can use to generate and drawing trees, realistic or fractal ones.

Example:
```python
from math import pi, radians as rad
from Tree.core import Tree
from PIL import Image

branches = (
    (.5, rad(-30)),
    (.6, rad(30)),
    (.4, rad(60))
)

def main():
    tree = Tree(
        pos=(0, 0, 0, -500),
        branches=branches
    )

    # Let the tree grow
    tree.grow(10)

...
```

Sections: PyTree, Usage, Documentation

</details>

## Also in this topic

- [networkx](scientific-engineering-bio-informatics.md#networkx) - Python package for creating and manipulating graphs and networks
- [contourpy](scientific-engineering-information-analysis.md#contourpy) - Python library for calculating contours of 2D quadrilateral grids
- [sympy](scientific-engineering.md#sympy) - Computer algebra system (CAS) in Python
- [onnxruntime](scientific-engineering.md#onnxruntime) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [torch](scientific-engineering.md#torch) - Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [nvidia-nccl-cu12](scientific-engineering.md#nvidia-nccl-cu12) - NVIDIA Collective Communication Library (NCCL) Runtime
- [nvidia-nccl-cu13](scientific-engineering.md#nvidia-nccl-cu13) - NVIDIA Collective Communication Library (NCCL) Runtime
- [nvidia-cudnn-cu13](scientific-engineering.md#nvidia-cudnn-cu13) - cuDNN runtime libraries
- [nvidia-cublas](scientific-engineering.md#nvidia-cublas) - CUBLAS native runtime libraries
- [nvidia-nvjitlink](scientific-engineering.md#nvidia-nvjitlink) - Nvidia JIT LTO Library
- [nvidia-nvshmem-cu13](scientific-engineering.md#nvidia-nvshmem-cu13) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [nvidia-cuda-nvrtc](scientific-engineering.md#nvidia-cuda-nvrtc) - NVRTC native runtime libraries
- [nvidia-cufft](scientific-engineering.md#nvidia-cufft) - CUFFT native runtime libraries
- [nvidia-cusolver](scientific-engineering.md#nvidia-cusolver) - CUDA solver native runtime libraries
- [nvidia-cusparse](scientific-engineering.md#nvidia-cusparse) - CUSPARSE native runtime libraries
- [nvidia-cuda-runtime](scientific-engineering.md#nvidia-cuda-runtime) - CUDA Runtime native Libraries
- [pyproj](scientific-engineering.md#pyproj) - Python interface to PROJ (cartographic projections and coordinate transformations library)
- [nvidia-cuda-cupti](scientific-engineering.md#nvidia-cuda-cupti) - CUDA profiling tools runtime libs.
- [nvidia-cufile](scientific-engineering.md#nvidia-cufile) - cuFile GPUDirect libraries
- [nvidia-nvtx](scientific-engineering.md#nvidia-nvtx) - NVIDIA Tools Extension
- [nvidia-curand](scientific-engineering.md#nvidia-curand) - CURAND native runtime libraries
- [nvidia-cudnn-cu12](scientific-engineering.md#nvidia-cudnn-cu12) - cuDNN runtime libraries
- [nvidia-cublas-cu12](scientific-engineering.md#nvidia-cublas-cu12) - CUBLAS native runtime libraries
- [nvidia-cuda-nvrtc-cu12](scientific-engineering.md#nvidia-cuda-nvrtc-cu12) - NVRTC native runtime libraries
- [nvidia-cufft-cu12](scientific-engineering.md#nvidia-cufft-cu12) - CUFFT native runtime libraries
- [nvidia-cusparse-cu12](scientific-engineering.md#nvidia-cusparse-cu12) - CUSPARSE native runtime libraries
- [nvidia-cusolver-cu12](scientific-engineering.md#nvidia-cusolver-cu12) - CUDA solver native runtime libraries
- [nvidia-nvjitlink-cu12](scientific-engineering.md#nvidia-nvjitlink-cu12) - Nvidia JIT LTO Library
- [nvidia-cuda-runtime-cu12](scientific-engineering.md#nvidia-cuda-runtime-cu12) - CUDA Runtime native Libraries
- [nvidia-curand-cu12](scientific-engineering.md#nvidia-curand-cu12) - CURAND native runtime libraries
- [nvidia-cuda-cupti-cu12](scientific-engineering.md#nvidia-cuda-cupti-cu12) - CUDA profiling tools runtime libs.
- [nvidia-nvtx-cu12](scientific-engineering.md#nvidia-nvtx-cu12) - NVIDIA Tools Extension
- [optuna](scientific-engineering.md#optuna) - A hyperparameter optimization framework
- [tensorflow](scientific-engineering.md#tensorflow) - TensorFlow is an open source machine learning framework for everyone.
- [pyclipper](multimedia-graphics.md#pyclipper) - Cython wrapper for the C++ translation of the Angus Johnson's Clipper library (ver. 6.4.2)
- [PyPika](scientific-engineering-information-analysis.md#pypika) - A SQL query builder API for Python
- [nvidia-cufile-cu12](scientific-engineering.md#nvidia-cufile-cu12) - cuFile GPUDirect libraries
- [crcmod](communications.md#crcmod) - CRC Generator
- [ortools](office-business-scheduling.md#ortools) - Google OR-Tools python libraries and modules
- [tensorflow-estimator](scientific-engineering.md#tensorflow-estimator) - TensorFlow Estimator.
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [exchange_calendars](scientific-engineering.md#exchange_calendars) - Calendars for securities exchanges
- [jaxtyping](scientific-engineering-artificial-intelligence.md#jaxtyping) - Type annotations and runtime checking for shape and dtype of JAX/NumPy/PyTorch/etc. arrays.
- [nvidia-nvshmem-cu12](scientific-engineering.md#nvidia-nvshmem-cu12) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [crcmod-plus](communications.md#crcmod-plus) - CRC generator - modernized
- [tensorflow-serving-api](scientific-engineering.md#tensorflow-serving-api) - TensorFlow Serving Python API.
- [nvidia-cuda-cccl](scientific-engineering.md#nvidia-cuda-cccl) - CUDA CCCL
- [rembg](scientific-engineering.md#rembg) - Remove image background
- [igraph](scientific-engineering.md#igraph) - High performance graph data structures and algorithms
- [tensorflow-io-gcs-filesystem](scientific-engineering.md#tensorflow-io-gcs-filesystem) - TensorFlow IO
- [haversine](scientific-engineering-gis.md#haversine) - Calculate the distance between 2 points on Earth.
- [simsimd](scientific-engineering-artificial-intelligence.md#simsimd) - Portable mixed-precision BLAS-like vector math library for x86 and ARM
- [nvidia-nvvm](scientific-engineering.md#nvidia-nvvm) - NVVM Libraries
- [nvidia-cuda-nvcc](scientific-engineering.md#nvidia-cuda-nvcc) - CUDA nvcc
- [nvidia-cuda-crt](scientific-engineering.md#nvidia-cuda-crt) - CUDA C Runtime
- [onnxruntime-gpu](scientific-engineering.md#onnxruntime-gpu) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [uncertainties](education.md#uncertainties) - calculations with values with uncertainties, error propagation
- [nvidia-cuda-nvdisasm](scientific-engineering.md#nvidia-cuda-nvdisasm) - CUDA nvdisasm
- [filterpy](scientific-engineering.md#filterpy) - Kalman filtering and optimal estimation library
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [tf-keras](scientific-engineering.md#tf-keras) - Deep learning for humans.
- [reedsolo](communications.md#reedsolo) - Pure-Python Reed Solomon encoder/decoder
- [portion](scientific-engineering.md#portion) - Python data structure and operations for intervals
- [equinox](scientific-engineering-artificial-intelligence.md#equinox) - Elegant easy-to-use neural networks in JAX.
- [cma](scientific-engineering.md#cma) - CMA-ES, Covariance Matrix Adaptation Evolution Strategy for non-linear numerical optimization in Python
- [svgpathtools](multimedia-graphics.md#svgpathtools) - A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.
- [tensorflow-metadata](scientific-engineering-artificial-intelligence.md#tensorflow-metadata) - Library and standards for schema and statistics.
- [tensorflow-cpu](scientific-engineering.md#tensorflow-cpu) - TensorFlow is an open source machine learning framework for everyone.
- [awkward-cpp](scientific-engineering.md#awkward-cpp) - CPU kernels and compiled extensions for Awkward Array
- [awkward](scientific-engineering.md#awkward) - Manipulate JSON-like data with NumPy-like idioms.
- [nvidia-cublas-cu11](scientific-engineering.md#nvidia-cublas-cu11) - CUBLAS native runtime libraries
- [nvidia-cudnn-cu11](scientific-engineering.md#nvidia-cudnn-cu11) - cuDNN runtime libraries
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [nvidia-cuda-nvcc-cu12](scientific-engineering.md#nvidia-cuda-nvcc-cu12) - CUDA nvcc
- [leidenalg](scientific-engineering-information-analysis.md#leidenalg) - Leiden is a general algorithm for methods of community detection in large networks.
- [pymc](scientific-engineering.md#pymc) - Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with PyTensor
- [nvidia-cuda-runtime-cu11](scientific-engineering.md#nvidia-cuda-runtime-cu11) - CUDA Runtime native Libraries
- [nvidia-cuda-nvrtc-cu11](scientific-engineering.md#nvidia-cuda-nvrtc-cu11) - NVRTC native runtime libraries
- [lap](education.md#lap) - Linear Assignment Problem solver (LAPJV/LAPMOD).
- [tensorflow-hub](scientific-engineering.md#tensorflow-hub) - TensorFlow Hub is a library to foster the publication, discovery, and consumption of reusable parts of machine learning models.
- [paddlex](scientific-engineering.md#paddlex) - Low-code development tool based on PaddlePaddle.
- [boost-histogram](scientific-engineering.md#boost-histogram) - The Boost::Histogram Python wrapper.
- [uproot](scientific-engineering.md#uproot) - ROOT I/O in pure Python and NumPy.
- [tensorflow-probability](scientific-engineering.md#tensorflow-probability) - Probabilistic modeling and statistical inference in TensorFlow
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [hist](scientific-engineering.md#hist) - Hist classes and utilities
- [nvidia-mathdx](scientific-engineering.md#nvidia-mathdx) - MathDx Device libraries
- [pymoo](scientific-engineering.md#pymoo) - Multi-Objective Optimization in Python
- [optuna-integration](scientific-engineering.md#optuna-integration) - Integration libraries of Optuna.
- [nvidia-cusparse-cu11](scientific-engineering.md#nvidia-cusparse-cu11) - CUSPARSE native runtime libraries
- [nvidia-cufft-cu11](scientific-engineering.md#nvidia-cufft-cu11) - CUFFT native runtime libraries
- [nvidia-cusolver-cu11](scientific-engineering.md#nvidia-cusolver-cu11) - CUDA solver native runtime libraries
- [nvidia-curand-cu11](scientific-engineering.md#nvidia-curand-cu11) - CURAND native runtime libraries
- [nvidia-cuda-cupti-cu11](scientific-engineering.md#nvidia-cuda-cupti-cu11) - CUDA profiling tools runtime libs.
- [kaldialign](scientific-engineering-artificial-intelligence.md#kaldialign) - Kaldi alignment methods wrapped into Python
- [TA-Lib](office-business-financial.md#ta-lib) - Python wrapper for TA-Lib
- [nvidia-nvtx-cu11](scientific-engineering.md#nvidia-nvtx-cu11) - NVIDIA Tools Extension
- [nvidia-nccl-cu11](scientific-engineering.md#nvidia-nccl-cu11) - NVIDIA Collective Communication Library (NCCL) Runtime
- [pygraphviz](scientific-engineering-information-analysis.md#pygraphviz) - Python interface to Graphviz
- [mlx-lm](scientific-engineering-artificial-intelligence.md#mlx-lm) - LLMs with MLX and the Hugging Face Hub
- [symengine](scientific-engineering.md#symengine) - Python library providing wrappers to SymEngine
- [python-igraph](scientific-engineering.md#python-igraph) - High performance graph data structures and algorithms (legacy package)
- [fiddle](scientific-engineering.md#fiddle) - Fiddle: A Python-first configuration library
- [numkong](scientific-engineering-artificial-intelligence.md#numkong) - Portable mixed-precision math, linear-algebra, & retrieval library with 2000+ SIMD kernels for x86, Arm, RISC-V, LoongArch, Power, & WebAssembly
- [pytorch-tokenizers](scientific-engineering.md#pytorch-tokenizers) - A package with common tokenizers in Python and C++
- [lineax](scientific-engineering-artificial-intelligence.md#lineax) - Linear solvers in JAX and Equinox.
- [nemo-toolkit](scientific-engineering.md#nemo-toolkit) - NeMo - a toolkit for Conversational AI
- [nvidia-cuda-tileiras](scientific-engineering.md#nvidia-cuda-tileiras) - TileIR Assembler Package
- [osmnx](scientific-engineering-gis.md#osmnx) - Download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap
- [tfp-nightly](scientific-engineering.md#tfp-nightly) - Probabilistic modeling and statistical inference in TensorFlow
- [megatron-core](scientific-engineering.md#megatron-core) - Megatron Core - a library for efficient and scalable training of transformer based models
- [ai-edge-litert](scientific-engineering.md#ai-edge-litert) - LiteRT is for mobile and embedded devices.
- [gin-config](scientific-engineering.md#gin-config) - Gin-Config: A lightweight configuration library for Python
- [nvidia-cuda-cccl-cu12](scientific-engineering.md#nvidia-cuda-cccl-cu12) - CUDA CCCL
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [optimistix](scientific-engineering-artificial-intelligence.md#optimistix) - Nonlinear optimisation in JAX and Equinox.
- [lapx](education.md#lapx) - Linear assignment problem solvers, including single and batch solvers.
- [directsearch](scientific-engineering.md#directsearch) - A derivative-free solver for unconstrained minimization
- [pytools](scientific-engineering.md#pytools) - A collection of tools for Python
- [POT](scientific-engineering-artificial-intelligence.md#pot) - Python Optimal Transport Library
- [quantstats](office-business-financial.md#quantstats) - Portfolio analytics for quants
- [diffrax](scientific-engineering-artificial-intelligence.md#diffrax) - GPU+autodiff-capable ODE/SDE/CDE solvers written in JAX.
- [pygmsh](scientific-engineering.md#pygmsh) - Python frontend for Gmsh
- [tflite-runtime](scientific-engineering.md#tflite-runtime) - TensorFlow Lite is for mobile and embedded devices.
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [nvidia-npp-cu12](scientific-engineering.md#nvidia-npp-cu12) - NPP native runtime libraries
- [vector](scientific-engineering.md#vector) - Vector classes and utilities
- [pyAgrum-nightly](scientific-engineering-artificial-intelligence.md#pyagrum-nightly) - Bayesian networks and other Probabilistic Graphical Models.
- [mxnet](scientific-engineering.md#mxnet) - Apache MXNet is an ultra-scalable deep learning framework. This version uses openblas and MKLDNN.
- [rdata](file-formats.md#rdata) - Read R datasets from Python.
- [onnxruntime-openvino](scientific-engineering.md#onnxruntime-openvino) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [tf-keras-nightly](scientific-engineering.md#tf-keras-nightly) - Deep learning for humans.
- [empyrical-reloaded](scientific-engineering.md#empyrical-reloaded) - empyrical computes performance and risk statistics commonly used in quantitative finance
- [pynini](scientific-engineering-artificial-intelligence.md#pynini) - Finite-state grammar compilation
- [latex2sympy2](education.md#latex2sympy2) - Convert latex to sympy with ANTLR and support Matrix, Linear Algebra and CAS functions.
- [torch-tb-profiler](scientific-engineering.md#torch-tb-profiler) - PyTorch Profiler TensorBoard Plugin
- [coffea](scientific-engineering.md#coffea) - Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.
- [pyulog](scientific-engineering-artificial-intelligence.md#pyulog) - Python log parser for ULog
- [pyFFTW](multimedia-sound-audio.md#pyfftw) - A pythonic wrapper around FFTW, the FFT library, presenting a unified interface for all the supported transforms.
- [pyamg](education.md#pyamg) - PyAMG: Algebraic Multigrid Solvers in Python
- [tf-nightly](scientific-engineering.md#tf-nightly) - TensorFlow is an open source machine learning framework for everyone.
- [tf2onnx](scientific-engineering.md#tf2onnx) - Tensorflow to ONNX converter
- [better-optimize](scientific-engineering.md#better-optimize) - A drop-in replacement for scipy optimize functions with quality of life improvements
- [pymc-extras](scientific-engineering.md#pymc-extras) - A home for new additions to PyMC, which may include unusual probability distribitions, advanced model fitting algorithms, or any code that may be inappropriate to include in the pymc repository, but may want to be made available to users.
- [tensorflow-io](scientific-engineering.md#tensorflow-io) - TensorFlow IO
- [pytorch-forecasting](scientific-engineering.md#pytorch-forecasting) - Forecasting timeseries with PyTorch - dataloaders, normalizers, metrics and models
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [skfolio](office-business-financial.md#skfolio) - Portfolio optimization, factor model construction, and risk management built on top of scikit-learn
- [tfx-bsl](scientific-engineering.md#tfx-bsl) - tfx_bsl (TFX Basic Shared Libraries) contains libraries shared by many TFX (TensorFlow eXtended) libraries and components.
- [PyMaxflow](scientific-engineering-artificial-intelligence.md#pymaxflow) - A mincut/maxflow package for Python
- [pyopencl](scientific-engineering.md#pyopencl) - Python wrapper for OpenCL
- [pymc-marketing](scientific-engineering.md#pymc-marketing) - Marketing Statistical Models in PyMC
- [pymc3](scientific-engineering.md#pymc3) - Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Theano
- [tensorflowjs](scientific-engineering.md#tensorflowjs) - 
- [bittensor-wallet](scientific-engineering.md#bittensor-wallet) - 
- [nemo-text-processing](scientific-engineering.md#nemo-text-processing) - NeMo text processing for ASR and TTS
- [cu2qu](multimedia-graphics.md#cu2qu) - Cubic-to-quadratic bezier curve conversion
- [ai-edge-litert-nightly](scientific-engineering.md#ai-edge-litert-nightly) - LiteRT is for mobile and embedded devices.
- [onnxruntime-directml](scientific-engineering.md#onnxruntime-directml) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [py-vollib-vectorized](office-business-financial.md#py-vollib-vectorized) - A fast, vectorized approach to calculating Implied Volatility and Greeks using the Black, Black-Scholes and Black-Scholes-Merton pricing.
- [fastdigest](scientific-engineering.md#fastdigest) - A fast t-digest library for Python built on Rust.
- [torchax](scientific-engineering.md#torchax) - torchax is a library for running Jax and PyTorch together
- [networkit](scientific-engineering-bio-informatics.md#networkit) - NetworKit is a toolbox for high-performance network analysis
- [tensorflow-decision-forests](scientific-engineering.md#tensorflow-decision-forests) - Collection of training and inference decision forest algorithms.
- [blackjax](education.md#blackjax) - Flexible and fast sampling in Python
- [pycuda](scientific-engineering-2.md#pycuda) - Python wrapper for Nvidia CUDA
- [fxpmath](scientific-engineering-2.md#fxpmath) - A python library for fractional fixed-point (base 2) arithmetic and binary manipulation with Numpy compatibility.
- [litert-converter](scientific-engineering-2.md#litert-converter) - LiteRT is for mobile and embedded devices.
- [quadrilateral-fitter](scientific-engineering-artificial-intelligence.md#quadrilateral-fitter) - QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.
- [islpy](scientific-engineering-2.md#islpy) - Wrapper around isl, an integer set library
- [fastcluster](scientific-engineering-artificial-intelligence.md#fastcluster) - Fast hierarchical clustering routines for R and Python.
- [tensorflow-data-validation](scientific-engineering-2.md#tensorflow-data-validation) - A library for exploring and validating machine learning data.
- [bittensor-drand](scientific-engineering-2.md#bittensor-drand) - Rust-backed Python library for generating timelock-encrypted weight commitments for Bittensor's commit-reveal mechanism using drand randomness.
- [scikit-posthocs](scientific-engineering-information-analysis.md#scikit-posthocs) - Statistical post-hoc analysis and outlier detection algorithms
- [lightly](scientific-engineering-2.md#lightly) - A deep learning package for self-supervised learning and world models
- [docplex](other-nonlisted-topic.md#docplex) - The IBM Decision Optimization CPLEX Modeling for Python
- [tensorflow-intel](scientific-engineering-2.md#tensorflow-intel) - TensorFlow is an open source machine learning framework for everyone.
- [ydf](scientific-engineering-2.md#ydf) - YDF (short for Yggdrasil Decision Forests) is a library for training, serving, evaluating and analyzing decision forest models such as Random Forest and Gradient Boosted Trees.
- [nvidia-matmul-heuristics](scientific-engineering-2.md#nvidia-matmul-heuristics) - NVIDIA Matmul Heuristics
- [suitesparse-graphblas](scientific-engineering-2.md#suitesparse-graphblas) - SuiteSparse:GraphBLAS Python bindings.
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [lightly-utils](scientific-engineering-2.md#lightly-utils) - A utility package for lightly
- [nvidia-nvfatbin-cu12](scientific-engineering-2.md#nvidia-nvfatbin-cu12) - NVIDIA compiler library for fatbin interaction
- [tensorflow-recommenders](scientific-engineering-2.md#tensorflow-recommenders) - Tensorflow Recommenders, a TensorFlow library for recommender systems.
- [pyroots](scientific-engineering-2.md#pyroots) - Pure python single variable function solvers
- [pyDOE3](education.md#pydoe3) - Design of experiments for Python
- [tensorflow-cpu-aws](scientific-engineering-2.md#tensorflow-cpu-aws) - TensorFlow is an open source machine learning framework for everyone.
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [netron](scientific-engineering-2.md#netron) - Viewer for neural network, deep learning and machine learning models.
- [torch-npu](scientific-engineering-2.md#torch-npu) - NPU bridge for PyTorch
- [minizinc](scientific-engineering-artificial-intelligence.md#minizinc) - Access MiniZinc directly from Python
- [tensorflow-transform](scientific-engineering-2.md#tensorflow-transform) - A library for data preprocessing with TensorFlow
- [jixia](file-formats-json.md#jixia) - Python binding for jixia
- [riskfolio-lib](office-business-financial.md#riskfolio-lib) - Portfolio Optimization in Python
- [nemo-gym](scientific-engineering-2.md#nemo-gym) - NeMo Gym is a library for building reinforcement learning environments
- [flwr](scientific-engineering-2.md#flwr) - Flower: A Friendly Federated AI Framework
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [tensorflow-gpu](scientific-engineering-2.md#tensorflow-gpu) - Removed: please install "tensorflow" instead.
- [gstools](scientific-engineering-2.md#gstools) - GSTools: A geostatistical toolbox.
- [executorch](scientific-engineering-2.md#executorch) - On-device AI across mobile, embedded and edge for PyTorch
- [interpax](scientific-engineering-2.md#interpax) - Interpolation and function approximation with JAX
- [CyRK](scientific-engineering-2.md#cyrk) - Runge-Kutta ODE Integrator Implemented in Cython and Numba.
- [gstools-cython](scientific-engineering-2.md#gstools-cython) - Cython backend for GSTools.
- [PyKrige](scientific-engineering-2.md#pykrige) - Kriging Toolkit for Python.
- [torchtyping](scientific-engineering-artificial-intelligence.md#torchtyping) - Runtime type annotations for the shape, dtype etc. of PyTorch Tensors.
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [pymetis](multimedia-graphics.md#pymetis) - A graph partitioning package
- [tensorflow-io-nightly](scientific-engineering-2.md#tensorflow-io-nightly) - TensorFlow IO
- [mnn](scientific-engineering-2.md#mnn) - C methods for MNN Package
