# Scientific/Engineering / Chemistry

[Index](README.md) · 18 packages in this topic, 42 more listed under another topic, by downloads.

### pymatgen

Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org).

`pip install pymatgen` · installs (wheel) · licence: MIT · rank 4721 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pymatgen/) · [docs](https://pymatgen.org) · [source](https://github.com/materialsproject/pymatgen)

<details><summary>README extract</summary>

Pymatgen (Python Materials Genomics) is a robust, open-source Python
library for materials analysis.

> [!IMPORTANT]
> The core data objects (`Element`, `Site`, `Molecule`, `Structure`, `Composition`, `Lattice`) and
> file I/O for major electronic structure codes now live in the lean [`pymatgen-core`] package. ...

Features:
1. It is (fairly) robust. Pymatgen is used by thousands of researchers and is the analysis code powering the
 [Materials Project]. The analysis it produces survives rigorous scrutiny every single day. Bugs tend to be found
 and corrected quickly. ...

Sections: Why use `pymatgen`?, Using pymatgen, Our Copyright Policy

</details>

### seekpath

A module to obtain and visualize k-vector coefficients and obtain band paths in the Brillouin zone of crystal structures

`pip install seekpath` · installs (wheel) · licence: MIT License · rank 5246 · last release 2026-09-25 · [PyPI](https://pypi.org/project/seekpath/)

<details><summary>README extract</summary>

Test status for default branch:

`SeeK-path` is a python module to obtain band paths in the Brillouin zone of crystal structures.

The definition of k-point labels follows crystallographic convention, as defined and discussed in the HPKOT paper. Moreover, the Bravais lattice is detected properly using the spacegroup symmetry. ...

Sections: SeeK-path, Online service/tool

</details>

### pymatgen-core

Python Materials Genomics is a robust materials analysis code that defines core object representations for structures and molecules with support for many electronic structure codes. It is currently the core analysis code powering the Materials Project (https://materialsproject.org). This repository is for pymatgen-core, which implements the core data structures and algorithms.

`pip install pymatgen-core` · installs (wheel) · licence: MIT · rank 5571 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pymatgen-core/) · [docs](https://pymatgen.org) · [source](https://github.com/materialsproject/pymatgen-core)

<details><summary>README extract</summary>

`pymatgen-core` is the foundational subset of Pymatgen (Python Materials Genomics), the robust open-source Python library for materials analysis. It contains the core data structures, symmetry/lattice operations, and the I/O layer for many DFT/MD codes, with minimal dependencies. ...

Features:
1. It is (fairly) robust. Pymatgen is used by thousands of researchers and is the analysis code powering the
 [Materials Project]. The analysis it produces survives rigorous scrutiny every single day. Bugs tend to be found
 and corrected quickly. ...

Sections: Why use `pymatgen-core`?, Using pymatgen, Our Copyright Policy

</details>

### janaf

Python wrapper for NIST-JANAF Thermochemical Tables

`pip install janaf` · installs (wheel) · licence: 0BSD · rank 5937 · last release 2026-11-06 · [PyPI](https://pypi.org/project/janaf/) · [source](https://github.com/n-takumasa/py-janaf)

<details><summary>README extract</summary>

Features:
* Search compounds
* Parse a table as `polars.DataFrame`
* Fix some data
 * Fix missing sign
 * Fix missing tab
 * Ignore comment-like lines

Example:
```python
>>> import polars as pl
>>> import janaf
>>> table = janaf.search(formula="CO2$")
>>> table.name
'Carbon Dioxide (CO2)'
>>> table.formula
'C1O2(g)'
>>> table.df
shape: (62, 9)
┌────────┬────────┬─────────┬──────────────┬───┬───────────┬───────────┬─────────┬──────┐
...
```

Sections: Features, Known issues, Usage, Credit

</details>

### nvalchemi-toolkit-ops

High-performance NVIDIA Warp primitives for GPU-enabled computational chemistry and atomistic simulation workflows.

`pip install nvalchemi-toolkit-ops` · installs (wheel) · licence: Apache-2.0 · rank 6329 · last release 2026-10-13 · [PyPI](https://pypi.org/project/nvalchemi-toolkit-ops/)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD033 MD007 -->

NVIDIA ALCHEMI Toolkit-Ops is a collection of GPU-optimized, batched
primitives for accelerating atomistic simulations. High performance compute
kernels are written in NVIDIA `warp-lang`.

Features:
- Neighbor lists
 - Naive, cell-list, and tiled cluster-pair methods
 - Matrix and COO formats
 - Automatic method selection and custom pair functions ...

Example:
```python
import torch
from nvalchemiops.torch.neighbors import neighbor_list

torch.set_default_dtype(torch.float32)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_default_device(device)

NUM_ATOMS = 50_000
# distribute positions inside the cell
positions = torch.rand((NUM_ATOMS, 3)) * 100.0
...
```

...

</details>

### MultiPyVu

Control MultiVu using Python

`pip install MultiPyVu` · installs (wheel) · licence: MIT · rank 6864 · last release 2026-10-30 · [PyPI](https://pypi.org/project/MultiPyVu/)

<details><summary>README extract</summary>

- Introduction
- Requirements
- Example Scripts
- Getting Started
- Using MultiPyVu.Server() and MultiPyVu.Client()
- Starting the Server Using the GUI
- Commands
 - set_temperature() / get_temperature()
 - set_field() / get_field()
 - set_chamber() / get_chamber()
 - wait_for()
 - is_steady()
 - get_aux_temperature()
 - resistivity option
 - ...

Example:
```python
import MultiPyVu as mpv

data = mpv.DataFile()
my_dataframe = data.parse_MVu_data_file('myMultiVuFile.dat')
```

Sections: MultiPyVu, Introduction, Module Requirements, Included Example Scripts, Getting Started, Using MultiPyVu.Server() and MultiPyVu.Client(), Starting the Server Using the GUI, Commands, Temperature, Field, Chamber, Wait For, Is Steady, OptiCool Auxiliary Thermometer

</details>

### ovito

A scientific data visualization and analysis software for particle-based simulations

`pip install ovito` · installs (wheel) · licence: MIT · rank 6985 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ovito/) · [docs](https://docs.ovito.org/python/)

<details><summary>README extract</summary>

OVITO (Open Visualization Tool) is a scientific visualization and analysis package for atomistic and
particle-based simulation data. Visit the official website for more information: ...

</details>

### pycalphad

CALPHAD tools for designing thermodynamic models, calculating phase diagrams and investigating phase equilibria.

`pip install pycalphad` · installs (wheel) · licence: MIT License · rank 7074 · last release 2026-06-05 · [PyPI](https://pypi.org/project/pycalphad/)

<details><summary>README extract</summary>

Note: Unsolicited pull requests are _happily_ accepted!

pycalphad is a free and open-source Python library for
designing thermodynamic models, calculating phase diagrams and
investigating phase equilibria within the CALPHAD method. ...

Sections: pycalphad, a library for the CALculation of PHAse Diagrams, Examples, Documentation, Getting Help, Citing

</details>

### shakenbreak

Package to generate and analyse distorted defect structures, in order to identify ground-state and metastable defect configurations.

`pip install shakenbreak` · installs (wheel) · licence: MIT License · rank 7210 · last release 2026-02-10 · [PyPI](https://pypi.org/project/shakenbreak/) · [docs](https://shakenbreak.readthedocs.io/en/latest/index.html) · [source](https://github.com/SMTG-Bham/shakenbreak)

<details><summary>README extract</summary>

`ShakeNBreak` is a defect structure-searching method employing chemically-guided bond distortions to locate ground-state
and metastable structures of point defects in solid materials.

- `ShakeNBreak` Documentation Site
- Questions Related to `ShakeNBreak` and Instructions ...

Sections: `ShakeNBreak` (`SnB`), Literature, Usage, Python API, Command line interface, Studies using `ShakeNBreak`, Code Compatibility, Bugs reports, feature requests and questions

</details>

### doped

Python package to setup, process and analyse solid-state defect calculations with VASP

`pip install doped` · installs (wheel) · licence: MIT License · rank 7211 · last release 2026-02-10 · [PyPI](https://pypi.org/project/doped/) · [docs](https://doped.readthedocs.io/en/latest/) · [source](https://github.com/SMTG-Bham/doped)

<details><summary>README extract</summary>

`doped` is a Python software for the generation, pre-/post-processing and analysis of defect supercell calculations, implementing the defect simulation workflow in an efficient, reproducible, user-friendly yet powerful and fully-customisable manner. ...

Features:
All features and functionality are fully-customisable:
- Supercell Generation: Generate an optimal supercell, maximising periodic image separation for the minimum number of atoms (computational cost). ...

Sections: Key Features, Performance and Example Outputs, Literature, `ShakeNBreak`, Studies using `doped`, so far, Open Science and Reproducibility

</details>

### ipi

A Python interface for ab initio path integral molecular dynamics simulations

`pip install ipi` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 7279 · last release 2026-10-17 · [PyPI](https://pypi.org/project/ipi/) · [docs](https://ipi-code.org/i-pi) · [source](https://github.com/i-pi/i-pi)

_README extract left out: share-alike licence._

### cantera

Cantera is an open-source suite of tools for problems involving chemical kinetics, thermodynamics, and transport processes.

`pip install cantera` · installs (wheel) · licence: BSD-3-Clause · rank 8705 · last release 2025-11-18 · [PyPI](https://pypi.org/project/cantera/) · [docs](https://cantera.org/stable/reference) · [source](https://github.com/Cantera/cantera)

<details><summary>README extract</summary>

Cantera is an open-source collection of object-oriented software tools for
problems involving chemical kinetics, thermodynamics, and transport processes.
Among other things, it can be used to: ...

Sections: What is Cantera?, Documentation, Users' Group, NumFOCUS

</details>

### epam-indigo

Indigo universal cheminformatics toolkit

`pip install epam-indigo` · installs (wheel) · licence: Apache Software License · rank 9232 · last release 2026-08-24 · [PyPI](https://pypi.org/project/epam-indigo/) · [docs](https://lifescience.opensource.epam.com/indigo/api/index.html) · [source](https://github.com/epam/indigo/)

<details><summary>README extract</summary>

Indigo is a universal molecular toolkit that can be used for molecular fingerprinting, substructure search, and molecular visualization. Also capable of performing a molecular similarity search, it is 100% open source and provides enhanced stereochemistry support for end users, as well as a documented API for developers.

</details>

### mendeleev

Pythonic periodic table of elements

`pip install mendeleev` · installs (wheel) · licence: MIT License · rank 9371 · last release 2026-09-10 · [PyPI](https://pypi.org/project/mendeleev/) · [docs](https://mendeleev.readthedocs.io) · [source](https://github.com/lmmentel/mendeleev)

<details><summary>README extract</summary>

A package with a convenient python API for accessing various properties
of elements, ions and isotopes in the periodic table of elements.

 Report Bug
 Request Feature
 Submit a Pull Request

> [!TIP]
> If you're looking for raw data behind ``mendeleev`` have a look at mendeleev-data repo. ...

Sections: Pythonic periodic table of elements, About the project, Interactive web app, Documentation, Data, Basic properties, Standardized colors schemes, Size related properties, Electronegativity scales, Descriptive properties, Physical properties, Computed properties, Other properties, Isotope properties

</details>

### periodictable

Extensible periodic table of the elements

`pip install periodictable` · installs (wheel) · licence: Public Domain · rank 9943 · last release 2026-02-28 · [PyPI](https://pypi.org/project/periodictable/) · [docs](https://periodictable.readthedocs.io) · [source](https://github.com/python-periodictable/periodictable)

<details><summary>README extract</summary>

This package provides a periodic table of the elements with
support for mass, density and xray/neutron scattering information.

Neutron scattering calculations use values collected by the
Atomic Institute of the Austrian Universities as they appear in the neutron
data booklet, with support for some energy dependent scattering
in rare earth ...

</details>

### custodian

A simple JIT job management framework in Python.

`pip install custodian` · installs (wheel) · licence: MIT License · rank 12119 · last release 2026-10-20 · [PyPI](https://pypi.org/project/custodian/) · [docs](https://materialsproject.github.io/custodian)

<details><summary>README extract</summary>

Custodian is a simple, robust and flexible just-in-time (JIT) job management
framework written in Python. Using custodian, you can create wrappers that
perform error checking, job management and error recovery. It has a simple
plugin framework that allows you to develop specific job management workflows
for different applications. ...

Sections: Getting custodian, Stable version, Requirements, Usage

</details>

### openfermion

Package to compile and analyze quantum algorithms for simulating fermionic systems.

`pip install openfermion` · installs (wheel) · licence: Apache Software License · rank 12147 · last release 2026-07-17 · [PyPI](https://pypi.org/project/openfermion/)

<details><summary>README extract</summary>

Electronic structure package for quantum computers.

Features –
Installation –
Plugins –
Documentation –
Contributing –
Citing –
Authors –
Contact

Features:
OpenFermion is an open-source Python package for compiling and analyzing quantum algorithms to
simulate fermionic systems, including quantum chemistry. ...

Sections: OpenFermion, Features, Plugins, High-performance simulators, Circuit compilation plugins, Electronic structure package plugins, Documentation, Citing OpenFermion, Contact, Disclaimer

</details>

### tblite

Light-weight tight-binding framework

`pip install tblite` · installs (wheel) · licence: LGPL-3.0-or-later · rank 14825 · last release 2026-10-29 · [PyPI](https://pypi.org/project/tblite/) · [docs](https://tblite.readthedocs.io) · [source](https://github.com/tblite/tblite)

_README extract left out: share-alike licence._

## Also in this topic

- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [simsimd](scientific-engineering-artificial-intelligence.md#simsimd) - Portable mixed-precision BLAS-like vector math library for x86 and ARM
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [gemmi](scientific-engineering-bio-informatics.md#gemmi) - library for structural biology
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [pymatgen-io-validation](scientific-engineering.md#pymatgen-io-validation) - A comprehensive I/O validator for electronic structure calculations
- [numkong](scientific-engineering-artificial-intelligence.md#numkong) - Portable mixed-precision math, linear-algebra, & retrieval library with 2000+ SIMD kernels for x86, Arm, RISC-V, LoongArch, Power, & WebAssembly
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [fluids](education.md#fluids) - Fluid dynamics component of Chemical Engineering Design Library (ChEDL)
- [pybaselines](scientific-engineering.md#pybaselines) - A library of algorithms for the baseline correction of experimental data.
- [pyteomics](education.md#pyteomics) - A framework for proteomics data analysis.
- [py3Dmol](scientific-engineering-bio-informatics.md#py3dmol) - An IPython interface for embedding 3Dmol.js views in Jupyter notebooks
- [chemicals](education.md#chemicals) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [mdtraj](scientific-engineering-bio-informatics.md#mdtraj) - MDTraj: A modern, open library for the analysis of molecular dynamics trajectories
- [thermo](education.md#thermo) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [iapws](scientific-engineering.md#iapws) - Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam
- [propka](scientific-engineering-bio-informatics.md#propka) - Heuristic pKa calculations with ligands
- [MDAnalysis](scientific-engineering.md#mdanalysis) - An object-oriented toolkit to analyze molecular dynamics trajectories.
- [pdbeccdutils](scientific-engineering-bio-informatics.md#pdbeccdutils) - Toolkit to parse and process small molecules in wwPDB
- [mmcif-pdbx](scientific-engineering-bio-informatics.md#mmcif-pdbx) - Python utilities for PDBx/mmCIF storage model
- [pdb2pqr](scientific-engineering-bio-informatics.md#pdb2pqr) - Automates many of the common tasks of preparing structures for continuum solvation calculations as well as many other types of biomolecular structure modeling, analysis, and simulation.
- [prolif](scientific-engineering-bio-informatics.md#prolif) - Interaction Fingerprints for protein-ligand complexes and more
- [pymzml](scientific-engineering-bio-informatics.md#pymzml) - high-throughput mzML parsing
- [openbabel-wheel](scientific-engineering-bio-informatics.md#openbabel-wheel) - An unofficial repository to distribute OpenBabel prebuilt wheels through Pypi..
- [pyopenms](scientific-engineering-bio-informatics.md#pyopenms) - Python wrapper for C++ LC-MS library OpenMS
- [networkit](scientific-engineering-bio-informatics.md#networkit) - NetworKit is a toolbox for high-performance network analysis
- [vesin](scientific-engineering.md#vesin) - Computing neighbor lists for atomistic system
- [alchemlyb](scientific-engineering-2.md#alchemlyb) - the simple alchemistry library
- [nglview](multimedia-graphics.md#nglview) - IPython widget to interactively view molecular structures and trajectories.
- [pdbfixer](scientific-engineering-bio-informatics.md#pdbfixer) - pdbfixer: Fixes problems in PDB files
- [pdb-tools](scientific-engineering-2.md#pdb-tools) - A swiss army knife for PDB files.
- [ViennaRNA](scientific-engineering-2.md#viennarna) - A library for the prediction and comparison of RNA secondary structures.
- [fabio](scientific-engineering-bio-informatics.md#fabio) - FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python
- [chematic](scientific-engineering-artificial-intelligence.md#chematic) - Pure-Rust cheminformatics — SMILES, fingerprints, 190+ descriptors, pKa, ADMET
- [ht](education.md#ht) - Heat transfer component of Chemical Engineering Design Library (ChEDL)
- [meeko](scientific-engineering-bio-informatics.md#meeko) - Python package for preparing small molecule for docking
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [SMACT](scientific-engineering-2.md#smact) - Semiconducting Materials by Analogy and Chemical Theory
- [molbloom](scientific-engineering-artificial-intelligence.md#molbloom) - Purchaseable SMILES filter
- [metatensor-core](scientific-engineering-2.md#metatensor-core) - Python bindings for metatensor
- [ProDy](scientific-engineering-bio-informatics.md#prody) - A Python Package for Protein Dynamics Analysis
- [exmol](scientific-engineering-artificial-intelligence.md#exmol) - Counterfactual generation with STONED SELFIES
