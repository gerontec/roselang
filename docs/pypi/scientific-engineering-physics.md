# Scientific/Engineering / Physics

[Index](README.md) · 20 packages in this topic, 100 more listed under another topic, by downloads.

### ase

Atomic Simulation Environment

`pip install ase` · installs (wheel) · licence: LGPL-2.1-or-later · rank 3428 · last release 2026-06-21 · [PyPI](https://pypi.org/project/ase/) · [source](https://gitlab.com/ase/ase.git)

_README extract left out: share-alike licence._

### sklearn-compat

Ease support for compatible scikit-learn estimators across versions

`pip install sklearn-compat` · installs (wheel) · licence: BSD License · rank 3584 · last release 2026-06-07 · [PyPI](https://pypi.org/project/sklearn-compat/) · [source](https://github.com/sklearn-compat/sklearn-compat)

<details><summary>README extract</summary>

Example:
```python
from sklearn_compat.any_submodule import any_function
```

Sections: How to adapt your scikit-learn code, Upgrading to scikit-learn 1.9, `is_pandas_df` function, Upgrading to scikit-learn 1.8, DataFrame related utility functions, `_check_targets` function, Upgrading to scikit-learn 1.7, Upgrading to scikit-learn 1.6, `is_clusterer` function, `validate_data` function, `check_array` and `check_X_y` functions, `_check_n_features` and `_check_feature_names` functions, `Tags`, `sklearn_tags` and estimator tags, `check_estimator` and `parametrize_with_checks` functions

</details>

### spglib

This is the spglib module.

`pip install spglib` · installs (wheel) · licence: BSD-3-Clause · rank 3618 · last release 2026-10-10 · [PyPI](https://pypi.org/project/spglib/) · [docs](https://spglib.readthedocs.io/) · [source](https://github.com/spglib/spglib)

<details><summary>README extract</summary>

Python bindings for C library for finding and handling crystal
symmetries

Sections: spglib, Using package distribution service, Building from source, Running tests

</details>

### zfit

scalable pythonic model fitting for high energy physics

`pip install zfit` · does not install on CPython 3.14 · licence: BSD-3-Clause · rank 5301 · last release 2025-11-18 · [PyPI](https://pypi.org/project/zfit/)

<details><summary>README extract</summary>

zfit is a highly scalable and customizable model manipulation and likelihood fitting library. It uses the same computational backend as
TensorFlow and is optimised for simple and direct manipulation of probability density functions. The project is affiliated with
and well integrated into Scikit-HEP, the HEP Python ecosystem. ...

Features:
The basic idea behind zfit is to offer a Python oriented alternative to the very successful RooFit library
from the ROOT data analysis package that can integrate with the other packages
that are part if the scientific Python ecosystem. ...

Example:
```python
obs = zfit.Space('x', -10, 10)

# create the model
mu    = zfit.Parameter("mu"   , 2.4, -1, 5)
sigma = zfit.Parameter("sigma", 1.3,  0, 5)
gauss = zfit.pdf.Gauss(obs=obs, mu=mu, sigma=sigma)

...

</details>

### zfit-interface

zfit model fitting interface for HEP

`pip install zfit-interface` · installs (wheel) · licence: BSD License · rank 5332 · last release 2021-12-01 · [PyPI](https://pypi.org/project/zfit-interface/) · [docs](https://zfit-interface.readthedocs.io/)

<details><summary>README extract</summary>

Features:
zfit model fitting interface for HEP

* Free software: BSD 3-Clause License

Sections: Overview, Documentation

</details>

### trainstation

Convenient training of linear models

`pip install trainstation` · installs (wheel) · licence: not stated · rank 6932 · last release 2025-07-30 · [PyPI](https://pypi.org/project/trainstation/) · [docs](https://trainstation.materialsmodeling.org) · [source](https://gitlab.com/materials-modeling/trainstation/)

<details><summary>README extract</summary>

trainstation is a tool that allows the efficient construction of linear models.
It provides supplementary functionality for handling data and model metrics and relies on the scikit-learn library for the actual training.
Many examples for the application of trainstation can be found in the documentation of hiphive and icet. ...

</details>

### pennylane-lightning

PennyLane-Lightning plugin

`pip install pennylane-lightning` · installs (wheel) · licence: Apache-2.0 · rank 7283 · last release 2026-05-12 · [PyPI](https://pypi.org/project/pennylane-lightning/)

<details><summary>README extract</summary>

The Lightning plugin ecosystem provides fast state-vector and tensor-network simulators written in C++.

PennyLane is a cross-platform Python library for quantum machine
learning, automatic differentiation, and optimization of hybrid quantum-classical computations.
PennyLane supports Python 3.11 and above. ...

Sections: Backends, Black & Pylint

</details>

### mplhep

Matplotlib styles for HEP

`pip install mplhep` · installs (wheel) · licence: MIT · rank 7953 · last release 2026-08-15 · [PyPI](https://pypi.org/project/mplhep/)

<details><summary>README extract</summary>

[](

[][actions-link]

A set of helpers for `matplotlib` to more easily produce plots typically
needed in HEP as well as style them in way that's compatible with current
collaboration requirements (ROOT-like plots for CMS, ATLAS, LHCb, ALICE).

Sections: Documentation and Getting Started, Notes, Use in publications

</details>

### qiskit-mitigation

Tools for handling errors during quantum computation.

`pip install qiskit-mitigation` · installs (wheel) · licence: Apache Software License · rank 8007 · last release 2026-11-05 · [PyPI](https://pypi.org/project/qiskit-mitigation/)

<details><summary>README extract</summary>

Qiskit Mitigation is a package for handling noise in quantum computations. It contains a set of techniques that can be used to build advanced or customized error mitigation pipelines directly with samplomatic. Specifically, it contains:

1. ...

Sections: Qiskit Mitigation, Documentation, Citing this package, Deprecation Policy, References

</details>

### pennylane

PennyLane is a cross-platform Python library for quantum computing, quantum machine learning, and quantum chemistry. Train a quantum computer the same way as a neural network.

`pip install pennylane` · installs (wheel) · licence: Apache-2.0 · rank 8926 · last release 2026-06-26 · [PyPI](https://pypi.org/project/pennylane/) · [source](https://github.com/PennyLaneAI/pennylane)

<details><summary>README extract</summary>

PennyLane is an open-source quantum software platform for
quantum computing,
 quantum machine learning,
 and
 quantum chemistry.

 Create meaningful quantum algorithms, from inspiration to implementation.

Features:
- *Inspiration to implementation, quickly.*

 Quantum computing can be complex — PennyLane makes it natural. Leverage the world’s largest library of research demos, interactive tutorials, and state-of-the-art components to build algorithms in ...

Sections: Key Features, Getting started, Key Resources, Demos

</details>

### power-grid-model

Python/C++ library for distribution power system analysis

`pip install power-grid-model` · installs (wheel) · licence: MPL-2.0 · rank 9254 · last release 2026-11-03 · [PyPI](https://pypi.org/project/power-grid-model/) · [docs](https://power-grid-model.readthedocs.io/en/stable/) · [source](https://github.com/PowerGridModel/power-grid-model)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>

SPDX-License-Identifier: MPL-2.0

`power-grid-model` is a library for steady-state distribution power system analysis distributed for Python and C.
The core of the library is written in C++.
Currently, it supports the following calculations: ...

Sections: Power Grid Model, Examples, Contact

</details>

### AeroSandbox

AeroSandbox is a Python package that helps you design and optimize aircraft and other engineered systems.

`pip install AeroSandbox` · installs (wheel) · licence: MIT License · rank 11017 · last release 2026-07-05 · [PyPI](https://pypi.org/project/AeroSandbox/) · [source](https://github.com/peterdsharpe/AeroSandbox)

<details><summary>README extract</summary>

by Peter Sharpe ()

AeroSandbox is a Python package that helps you design and optimize aircraft and other engineered systems.

At its heart, AeroSandbox is an optimization suite that combines the ease-of-use of familiar NumPy syntax with the power of modern automatic differentiation. ...

Sections: AeroSandbox :airplane, What can I do with AeroSandbox?, Getting Started, Tutorials, Examples, and Documentation, Usage Details, Units, Project Details, Bugs, Versioning, Stargazers over time

</details>

### phonors

Rust kernels for phonopy and phono3py

`pip install phonors` · installs (wheel) · licence: BSD-3-Clause · rank 11145 · last release 2026-11-04 · [PyPI](https://pypi.org/project/phonors/) · [source](https://github.com/phonopy/phonors)

<details><summary>README extract</summary>

Rust kernels for phonopy and phono3py.

`phonors` is a Rust extension module providing the heavy numerical
kernels used by phono3py
(via the `phono3py[rust]` extra) and intended to also back
phonopy as its C kernels are
ported. It is built with maturin and
PyO3, distributed as `abi3-py310` wheels
(Python 3.10+).

Sections: phonors, From PyPI, From conda-forge, Optional: native CPU tuning

</details>

### sunpy

SunPy core package: Python for Solar Physics

`pip install sunpy` · installs (wheel) · licence: BSD-3-Clause · rank 11435 · last release 2026-10-08 · [PyPI](https://pypi.org/project/sunpy/) · [docs](https://docs.sunpy.org) · [source](https://github.com/sunpy/sunpy)

<details><summary>README extract</summary>

SunPy core package: Python for Solar Physics

+-----------------------------------+-----------------------------------+-----------------------------------+
 Development
+===================================+===================================+===================================+
Latest PyPi Version Matrix Chat ...

Sections: `sunpy`, Usage, Changes, Getting Help, Usage of Generative AI

</details>

### tiled

Structured Scientific Data Access Service

`pip install tiled` · installs (wheel) · licence: BSD License · rank 11672 · last release 2026-11-02 · [PyPI](https://pypi.org/project/tiled/) · [docs](https://blueskyproject.io/tiled)

<details><summary>README extract</summary>

Tiled is a service that enables secure, structured access to **scientific
data. It supports search, remote slicing, format** conversion, and
live streaming.

Tiled helps scientists to store, find, and access scientific data at scale. ...

Sections: Tiled, First Steps

</details>

### NeuralFoil

NeuralFoil is an airfoil aerodynamics analysis tool using physics-informed machine learning, in pure Python/NumPy.

`pip install NeuralFoil` · installs (wheel) · licence: MIT License · rank 11841 · last release 2026-07-11 · [PyPI](https://pypi.org/project/NeuralFoil/) · [source](https://github.com/peterdsharpe/NeuralFoil)

<details><summary>README extract</summary>

by Peter Sharpe ()

NeuralFoil is a tool for rapid aerodynamics analysis of airfoils, similar to XFoil. NeuralFoil is a hybrid of physics-informed machine learning techniques and analytical models, leveraging domain knowledge. Its learned core is trained on nearly 8 million XFoil runs. ...

Features:
NeuralFoil comes with 8 different neural network models, with increasing levels of complexity:

 "xxsmall"
 "xsmall"
 "small"
 "medium"
 "large"
 "xlarge"
 "xxlarge"
 "xxxlarge" ...

Example:
```python
import neuralfoil as nf  # `pip install neuralfoil`
import numpy as np

aero = nf.get_aero_from_dat_file(  # You can use a .dat file as an entry point
    filename="/path/to/my_airfoil_file.dat",
    alpha=5,  # Angle of attack [deg]
    Re=5e6,  # Reynolds number [-]
...

</details>

### accelerator-toolbox

Accelerator Toolbox

`pip install accelerator-toolbox` · installs (wheel) · licence: Apache-2.0 · rank 12269 · last release 2026-10-15 · [PyPI](https://pypi.org/project/accelerator-toolbox/) · [source](https://github.com/atcollab/at.git)

<details><summary>README extract</summary>

Accelerator Toolbox is a code used for simulating particle accelerators, used
particularly for synchrotron light sources. It is hosted on Github. Its original implementation is in Matlab.

pyAT is a Python interface to the Accelerator Toolbox. ...

Example:
```python
>>> import at
>>> ring = at.Lattice.load('machine_data/hmba.mat')
>>> print(at.radiation_parameters(ring))
          Frac. tunes: [0.2099983  0.34001317 0.00349013]
                Tunes: [76.2099983  27.34001317]
       Chromaticities: [5.73409894 3.91761206]
Momentum compact. factor: 8.506669e-05
          Slip factor: -8.505944e-05
...
```

Sections: pyAT, Introduction, Usage

</details>

### silx

Silx tool-kit: collection of Python packages to support the development of data assessment, reduction and analysis applications at synchrotron radiation facilities

`pip install silx` · installs (wheel) · licence: MIT License · rank 12500 · last release 2026-10-06 · [PyPI](https://pypi.org/project/silx/) · [docs](https://silx.readthedocs.io/en/latest/) · [source](https://github.com/silx-kit/silx)

<details><summary>README extract</summary>

The purpose of the *silx* project is to provide a collection of Python packages to support the
development of data assessment, reduction and analysis applications at synchrotron
radiation facilities. ...

Sections: silx toolkit, Documentation, Examples

</details>

### simsopt

Framework for optimizing stellarators

`pip install simsopt` · installs from source (sdist only) · licence: MIT License · rank 13634 · last release 2026-08-25 · [PyPI](https://pypi.org/project/simsopt/) · [docs](https://simsopt.readthedocs.io) · [source](https://github.com/hiddenSymmetries/simsopt)

<details><summary>README extract</summary>

`simsopt` is a framework for optimizing
stellarators.
The high-level routines of `simsopt` are in python, with calls to C++
or fortran where needed for performance. Several types of components
are included:

- Interfaces to physics codes, e.g. for MHD equilibrium.
- Tools for defining objective functions and parameter spaces for
 optimization. ...

</details>

### tensorcircuit-nightly

High performance unified quantum computing framework for the NISQ era

`pip install tensorcircuit-nightly` · installs (wheel) · licence: Apache-2.0 · rank 14938 · last release 2026-11-07 · [PyPI](https://pypi.org/project/tensorcircuit-nightly/) · [docs](https://tensorcircuit-ng.readthedocs.io/) · [source](https://github.com/tensorcircuit/tensorcircuit-ng)

<details><summary>README extract</summary>

English | 简体中文

TensorCircuit-NG is the next-generation open-source high-performance quantum software framework and an AI-native quantum research runtime for turning research questions into executable, optimized, and validated quantum experiments. ...

Example:
```python
import tensorcircuit as tc
c = tc.Circuit(2)
c.H(0)
c.CNOT(0,1)
c.rx(1, theta=0.2)
print(c.wavefunction())
print(c.expectation_ps(z=[0, 1]))
print(c.sample(allow_state=True, batch=1024, format="count_dict_bin"))
```

Sections: Getting Started, Agentic Quantum Research (Recommended), Quick Demos, Advantages, Guidelines, Executable Research Hub, Research and Applications, DQAS, VQNHE, VQEX-MBL, Stark-DTC, RA-Training, TenCirChem, TenCirPauli

</details>

## Also in this topic

- [networkx](scientific-engineering-bio-informatics.md#networkx) - Python package for creating and manipulating graphs and networks
- [sympy](scientific-engineering.md#sympy) - Computer algebra system (CAS) in Python
- [pydicom](scientific-engineering-medical-science-apps.md#pydicom) - A pure Python package for reading and writing DICOM data
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [igraph](scientific-engineering.md#igraph) - High performance graph data structures and algorithms
- [astropy](scientific-engineering-astronomy.md#astropy) - Astronomy and astrophysics core library
- [pyerfa](scientific-engineering-astronomy.md#pyerfa) - Python bindings for ERFA
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [uncertainties](education.md#uncertainties) - calculations with values with uncertainties, error propagation
- [CoolProp](scientific-engineering.md#coolprop) - Open-source thermodynamic and transport properties database
- [filterpy](scientific-engineering.md#filterpy) - Kalman filtering and optimal estimation library
- [pyquaternion](scientific-engineering-mathematics.md#pyquaternion) - A fully featured, pythonic library for representing and using quaternions.
- [awkward-cpp](scientific-engineering.md#awkward-cpp) - CPU kernels and compiled extensions for Awkward Array
- [awkward](scientific-engineering.md#awkward) - Manipulate JSON-like data with NumPy-like idioms.
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [boost-histogram](scientific-engineering.md#boost-histogram) - The Boost::Histogram Python wrapper.
- [uproot](scientific-engineering.md#uproot) - ROOT I/O in pure Python and NumPy.
- [sigfig](education.md#sigfig) - Python library for rounding numbers (with expected results)
- [hist](scientific-engineering.md#hist) - Hist classes and utilities
- [numpy-quaternion](scientific-engineering-astronomy.md#numpy-quaternion) - Add a quaternion dtype to NumPy
- [pymatgen](scientific-engineering-chemistry.md#pymatgen) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org).
- [pymatgen-io-validation](scientific-engineering.md#pymatgen-io-validation) - A comprehensive I/O validator for electronic structure calculations
- [pyhf](scientific-engineering.md#pyhf) - pure-Python HistFactory implementation with tensors and autodiff
- [seekpath](scientific-engineering-chemistry.md#seekpath) - A module to obtain and visualize k-vector coefficients and obtain band paths in the Brillouin zone of crystal structures
- [cabinetry](scientific-engineering.md#cabinetry) - design and steer profile likelihood fits
- [symengine](scientific-engineering.md#symengine) - Python library providing wrappers to SymEngine
- [python-igraph](scientific-engineering.md#python-igraph) - High performance graph data structures and algorithms (legacy package)
- [moyopy](scientific-engineering-mathematics.md#moyopy) - Python binding of Moyo
- [pymatgen-core](scientific-engineering-chemistry.md#pymatgen-core) - Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org). This repository is for pymatgen-core, which implements the core data structures and algorithms.
- [osmnx](scientific-engineering-gis.md#osmnx) - Download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap
- [janaf](scientific-engineering-chemistry.md#janaf) - Python wrapper for NIST-JANAF Thermochemical Tables
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [fluids](education.md#fluids) - Fluid dynamics component of Chemical Engineering Design Library (ChEDL)
- [nvalchemi-toolkit-ops](scientific-engineering-chemistry.md#nvalchemi-toolkit-ops) - High-performance NVIDIA Warp primitives for GPU-enabled computational chemistry and atomistic simulation workflows.
- [pybaselines](scientific-engineering.md#pybaselines) - A library of algorithms for the baseline correction of experimental data.
- [obspy](scientific-engineering.md#obspy) - ObsPy - a Python framework for seismological observatories.
- [vedo](scientific-engineering-medical-science-apps.md#vedo) - A python module for scientific visualization, analysis of 3D objects and point clouds.
- [MultiPyVu](scientific-engineering-chemistry.md#multipyvu) - Control MultiVu using Python
- [dscribe](scientific-engineering.md#dscribe) - A Python package for creating feature transformations in applications of machine learning to materials science.
- [lalsuite](scientific-engineering.md#lalsuite) - LVK Algorithm Library Suite - LALSuite
- [pymunk](games-entertainment.md#pymunk) - Pymunk is a easy-to-use pythonic 2D physics library
- [pyglm](multimedia-graphics.md#pyglm) - OpenGL Mathematics library for Python
- [ovito](scientific-engineering-chemistry.md#ovito) - A scientific data visualization and analysis software for particle-based simulations
- [pycalphad](scientific-engineering-chemistry.md#pycalphad) - CALPHAD tools for designing thermodynamic models, calculating phase diagrams and investigating phase equilibria.
- [pyteomics](education.md#pyteomics) - A framework for proteomics data analysis.
- [shakenbreak](scientific-engineering-chemistry.md#shakenbreak) - Package to generate and analyse distorted defect structures, in order to identify ground-state and metastable defect configurations.
- [doped](scientific-engineering-chemistry.md#doped) - Python package to setup, process and analyse solid-state defect calculations with VASP
- [ipi](scientific-engineering-chemistry.md#ipi) - A Python interface for ab initio path integral molecular dynamics simulations
- [vector](scientific-engineering.md#vector) - Vector classes and utilities
- [sax](scientific-engineering.md#sax) - Autograd and XLA for S-parameters
- [chemicals](education.md#chemicals) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [thermo](education.md#thermo) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [iapws](scientific-engineering.md#iapws) - Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam
- [astropy-healpix](scientific-engineering-astronomy.md#astropy-healpix) - BSD-licensed HEALPix for Astropy
- [pyroomacoustics](multimedia-sound-audio.md#pyroomacoustics) - A simple framework for room acoustics and audio processing in Python.
- [coffea](scientific-engineering.md#coffea) - Basic tools and wrappers for enabling not-too-alien syntax when running columnar Collider HEP analysis.
- [pyulog](scientific-engineering-artificial-intelligence.md#pyulog) - Python log parser for ULog
- [pyFFTW](multimedia-sound-audio.md#pyfftw) - A pythonic wrapper around FFTW, the FFT library, presenting a unified interface for all the supported transforms.
- [cantera](scientific-engineering-chemistry.md#cantera) - Cantera is an open-source suite of tools for problems involving chemical kinetics, thermodynamics, and transport processes.
- [iminuit](scientific-engineering-mathematics.md#iminuit) - Jupyter-friendly Python frontend for MINUIT2 in C++
- [mendeleev](scientific-engineering-chemistry.md#mendeleev) - Pythonic periodic table of elements
- [arxyne](scientific-engineering-artificial-intelligence.md#arxyne) - Run any engineering simulation from one command.
- [segyio](scientific-engineering.md#segyio) - Simple & fast IO for SEG-Y files
- [pyopencl](scientific-engineering.md#pyopencl) - Python wrapper for OpenCL
- [periodictable](scientific-engineering-chemistry.md#periodictable) - Extensible periodic table of the elements
- [pysplashsurf](scientific-engineering.md#pysplashsurf) - Python bindings for splashsurf, a surface reconstruction library for SPH simulations.
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [quimb](scientific-engineering.md#quimb) - Quantum information and many-body library.
- [cotengra](scientific-engineering.md#cotengra) - Hyper optimized contraction trees for large tensor networks and einsums.
- [vesin](scientific-engineering.md#vesin) - Computing neighbor lists for atomistic system
- [igwn-segments](scientific-engineering-2.md#igwn-segments) - Representations of semi-open intervals
- [pycuda](scientific-engineering-2.md#pycuda) - Python wrapper for Nvidia CUDA
- [fxpmath](scientific-engineering-2.md#fxpmath) - A python library for fractional fixed-point (base 2) arithmetic and binary manipulation with Numpy compatibility.
- [islpy](scientific-engineering-2.md#islpy) - Wrapper around isl, an integer set library
- [igwn-ligolw](scientific-engineering-2.md#igwn-ligolw) - Python LIGO Light-Weight XML I/O Library
- [gs-madrona](multimedia-graphics.md#gs-madrona) - A fork from the official Madrona. The fork will be used for Genesis's own Madrona integration.
- [fabio](scientific-engineering-bio-informatics.md#fabio) - FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python
- [lscsoft-glue](scientific-engineering-astronomy.md#lscsoft-glue) - LSCSoft-GLUE is a collection of utilities for running data analysis pipelines for online and offline analysis as well as accessing various grid utilities.
- [igwn-auth-utils](scientific-engineering-2.md#igwn-auth-utils) - Authorisation utilities for IGWN
- [custodian](scientific-engineering-chemistry.md#custodian) - A simple JIT job management framework in Python.
- [pyDOE3](education.md#pydoe3) - Design of experiments for Python
- [ht](education.md#ht) - Heat transfer component of Chemical Engineering Design Library (ChEDL)
- [anastruct](scientific-engineering-2.md#anastruct) - Finite element analysis of 2D structures
- [ovphysx](scientific-engineering-artificial-intelligence.md#ovphysx) - PhysX simulation library for ovstage-populated scenes with Warp array interoperability. x86_64 wheels require a CPU with AVX.
- [gwdatafind](scientific-engineering-2.md#gwdatafind) - The GWDataFind data discovery client
- [xtgeo](scientific-engineering-2.md#xtgeo) - XTGeo is a Python library for 3D grids, surfaces, wells, etc
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [gstools](scientific-engineering-2.md#gstools) - GSTools: A geostatistical toolbox.
- [qctrl-client](internet-www-http-2.md#qctrl-client) - Q-CTRL Client
- [spgrep](scientific-engineering-mathematics.md#spgrep) - On-the-fly generator of space-group irreducible representations
- [SeismoStats](scientific-engineering-2.md#seismostats) - A Python Package for Statistical Seismology.
- [doroutes](scientific-engineering-2.md#doroutes) - Advanced Routing for GDSFactory
- [CyRK](scientific-engineering-2.md#cyrk) - Runge-Kutta ODE Integrator Implemented in Cython and Numba.
- [gstools-cython](scientific-engineering-2.md#gstools-cython) - Cython backend for GSTools.
- [PyKrige](scientific-engineering-2.md#pykrige) - Kriging Toolkit for Python.
- [ert](scientific-engineering-2.md#ert) - Ensemble based Reservoir Tool (ERT)
- [ligo.skymap](scientific-engineering-astronomy.md#ligoskymap) - Tools for reading, writing, manipulating, and making LIGO/Virgo/KAGRA sky maps
- [rapid-pe](scientific-engineering-2.md#rapid-pe) - RapidPE: The original low-latency gravitational wave parameter estimation code.
- [metatensor-core](scientific-engineering-2.md#metatensor-core) - Python bindings for metatensor
- [tblite](scientific-engineering-chemistry.md#tblite) - Light-weight tight-binding framework
