# Scientific/Engineering / Astronomy

[Index](README.md) · 23 packages in this topic, 19 more listed under another topic, by downloads.

### jdcal

Julian dates from proleptic Gregorian and Julian calendars.

`pip install jdcal` · installs (wheel) · licence: BSD License · rank 2219 · last release 2019-04-24 · [PyPI](https://pypi.org/project/jdcal/)

<details><summary>README extract</summary>

This module contains functions for converting between Julian dates and
calendar dates.

A function for converting Gregorian calendar dates to Julian dates, and
another function for converting Julian calendar dates to Julian dates
are defined. Two functions for the reverse calculations are also
defined. ...

Example:
```python
>>> from jdcal import gcal2jd, jd2gcal
>>> gcal2jd(2000,1,1)
(2400000.5, 51544.0)
>>> 2400000.5 + 51544.0 + 0.5
2451545.0

>>> gcal2jd(2000,2,30)
(2400000.5, 51604.0)
>>> gcal2jd(2000,3,1)
(2400000.5, 51604.0)
>>> gcal2jd(2001,2,30)
(2400000.5, 51970.0)
>>> gcal2jd(2001,3,2)
(2400000.5, 51970.0)

>>> jd2gcal(*gcal2jd(2000,1,1))
(2000, 1, 1, 0.0)
...
```

Sections: jdcal, Examples

</details>

### astropy

Astronomy and astrophysics core library

`pip install astropy` · installs (wheel) · licence: BSD-3-Clause · rank 2273 · last release 2026-10-15 · [PyPI](https://pypi.org/project/astropy/) · [docs](https://docs.astropy.org) · [source](https://github.com/astropy/astropy)

<details><summary>README extract</summary>

:Versions:
:Status:
:Tools:
:Community:

The Astropy Project is a community effort to develop a
single core package for astronomy in Python and foster interoperability between
packages used in the field. This repository contains the core library. ...

</details>

### PyMeeus

Python implementation of Jean Meeus astronomical routines

`pip install PyMeeus` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 2317 · last release 2022-12-11 · [PyPI](https://pypi.org/project/PyMeeus/)

_README extract left out: share-alike licence._

### pyerfa

Python bindings for ERFA

`pip install pyerfa` · installs (wheel) · licence: BSD License · rank 2349 · last release 2024-11-11 · [PyPI](https://pypi.org/project/pyerfa/)

<details><summary>README extract</summary>

PyERFA is the Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU). ...

Example:
```python
>>> import erfa
>>> erfa.jd2cal(2460000., [0, 1, 2, 3])
(array([2023, 2023, 2023, 2023], dtype=int32),
 array([2, 2, 2, 2], dtype=int32),
 array([24, 25, 26, 27], dtype=int32),
 array([0.5, 0.5, 0.5, 0.5]))
>>> erfa.plan94(2460000., [0, 1, 2, 3], 1)
array([([ 0.09083713, -0.39041392, -0.21797389], [0.02192341, 0.00705449, 0.00149618]),
...
```

Sections: PyERFA, Usage

</details>

### ephem

Compute positions of the planets and stars

`pip install ephem` · installs (wheel) · licence: MIT License · rank 3238 · last release 2026-02-28 · [PyPI](https://pypi.org/project/ephem/) · [source](https://github.com/brandon-rhodes/pyephem)

<details><summary>README extract</summary>

PyEphem provides an `ephem` Python package
for performing high-precision astronomy computations.
The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy application,
whose author, Elwood Charles Downey,
generously gave permission for their use in PyEphem. ...

Example:
```python
>>> import ephem
>>> mars = ephem.Mars()
>>> mars.compute('2008/1/1')
>>> print(mars.ra)
5:59:27.35
>>> print(mars.dec)
26:56:27.4
```

</details>

### sgp4

The C++ SGP4 routine that, given an Earth satellite TLE, computes its position.

`pip install sgp4` · installs (wheel) · licence: MIT · rank 3962 · last release 2026-07-12 · [PyPI](https://pypi.org/project/sgp4/)

<details><summary>README extract</summary>

This package compiles the official C++ code from Revisiting Spacetrack
Report #3 (AIAA 2006-6753) — specifically, the 2023 May 09 release
from David Vallado’s Fundamentals of Astrodynamics and Applications
webpage — and uses it to compute the positions of satellites in Earth
orbit. ...

Sections: Usage, Double-checking your TLE lines, Using OMM elements instead of TLE, Epoch, Array Acceleration, Export, Gravity, Providing your own elements, Attributes, Legacy API

</details>

### numpy-quaternion

Add a quaternion dtype to NumPy

`pip install numpy-quaternion` · installs (wheel) · licence: MIT · rank 4606 · last release 2025-11-24 · [PyPI](https://pypi.org/project/numpy-quaternion/) · [docs](https://quaternion.readthedocs.io/en/latest)

<details><summary>README extract</summary>

This Python module adds a quaternion dtype to NumPy.

The code was originally based on code by Martin
Ling (which he wrote
with help from Mark Wiebe), but was rewritten with ideas from
rational
to work with newer python versions (and to fix a few bugs), and
*greatly* expands the applications of quaternions. ...

Example:
```python
>>> import numpy as np
>>> import quaternion
>>> np.quaternion(1,0,0,0)
quaternion(1, 0, 0, 0)
>>> q1 = np.quaternion(1,2,3,4)
>>> q2 = np.quaternion(5,6,7,8)
>>> q1 * q2
quaternion(-60, 12, 30, 24)
>>> a = np.array([q1, q2])
>>> a
array([quaternion(1, 2, 3, 4), quaternion(5, 6, 7, 8)], dtype=quaternion)
>>> np.exp(a)
...
```

Sections: Quaternions in numpy, Quickstart, Basic usage, Dependencies, Bug reports and feature requests, 1 Euler angles are awful

</details>

### jplephem

Use a JPL ephemeris to predict planet positions.

`pip install jplephem` · installs (wheel) · licence: MIT · rank 4747 · last release 2026-01-23 · [PyPI](https://pypi.org/project/jplephem/)

<details><summary>README extract</summary>

Cite as: `Astrophysics Source Code Library, record ascl:1112.014

This package can load and use a Jet Propulsion Laboratory (JPL)
ephemeris for predicting the position and velocity of a planet or other
Solar System body. ...

</details>

### skyfield

Elegant astronomy for Python

`pip install skyfield` · installs (wheel) · licence: MIT License · rank 5080 · last release 2026-08-07 · [PyPI](https://pypi.org/project/skyfield/)

<details><summary>README extract</summary>

Skyfield is a pure-Python astronomy package
that is compatible with both Python 2 and 3
and makes it easy to generate high precision research-grade
positions for planets and Earth satellites.

The result:

Skyfield’s only binary dependency is NumPy. ...

Example:
```python
from skyfield.api import load

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

ts = load.timescale()
t = ts.now()
position = earth.at(t).observe(mars)
ra, dec, distance = position.radec()

print(ra)
print(dec)
print(distance)
```

</details>

### healpy

Healpix tools package for Python

`pip install healpy` · installs (wheel) · licence: GPL-2.0-only · rank 7275 · last release 2026-10-03 · [PyPI](https://pypi.org/project/healpy/) · [docs](https://healpy.readthedocs.io) · [source](https://github.com/healpy/healpy)

_README extract left out: share-alike licence._

### astropy-healpix

BSD-licensed HEALPix for Astropy

`pip install astropy-healpix` · installs (wheel) · licence: BSD 3-Clause · rank 7907 · last release 2026-07-20 · [PyPI](https://pypi.org/project/astropy-healpix/)

<details><summary>README extract</summary>

This is a BSD-licensed HEALPix package developed by the Astropy project
and based on C code written by Dustin Lang in astrometry.net. See the
Documentation for
information about installing and using this package.

</details>

### photutils

An Astropy package for source detection and photometry

`pip install photutils` · installs (wheel) · licence: BSD-3-Clause · rank 8476 · last release 2026-10-16 · [PyPI](https://pypi.org/project/photutils/) · [docs](https://photutils.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Photutils is a Python library that provides commonly-used tools
and key functionality for detecting and performing photometry of
astronomical sources. Tools are provided for background estimation,
star finding, source detection and extraction, aperture photometry,
PSF photometry, image segmentation, centroids, radial profiles,
and elliptical ...

Sections: Photutils, Citing Photutils

</details>

### asdf-coordinates-schemas

ASDF schemas for coordinates

`pip install asdf-coordinates-schemas` · installs (wheel) · licence: not stated · rank 9393 · last release 2026-02-05 · [PyPI](https://pypi.org/project/asdf-coordinates-schemas/) · [docs](https://www.asdf-format.org/projects/asdf-coordinates-schemas/en/latest/) · [source](https://github.com/asdf-format/asdf-coordinates-schemas)

<details><summary>README extract</summary>

This package provides ASDF schemas for validating coordinates tags. Users should not
need to install this directly; instead, install an implementation package such
as asdf-astropy, which includes asdf-coordinates-schemas as a dependency.

</details>

### lscsoft-glue

LSCSoft-GLUE is a collection of utilities for running data analysis pipelines for online and offline analysis as well as accessing various grid utilities.

`pip install lscsoft-glue` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 11970 · last release 2025-07-18 · [PyPI](https://pypi.org/project/lscsoft-glue/) · [docs](https://lscsoft.docs.ligo.org/glue/) · [source](https://git.ligo.org/lscsoft/glue.git)

_README extract left out: share-alike licence._

### camb

Code for Anisotropies in the Microwave Background

`pip install camb` · installs (wheel) · licence: LicenseRef-LGPLv3-arxiv · rank 12542 · last release 2026-10-14 · [PyPI](https://pypi.org/project/camb/) · [docs](https://camb.readthedocs.io) · [source](https://github.com/cmbant/camb)

_README extract left out: share-alike licence._

### rebound

An open-source multi-purpose N-body code

`pip install rebound` · installs (wheel) · licence: GPL-3.0-only · rank 12661 · last release 2026-10-05 · [PyPI](https://pypi.org/project/rebound/)

_README extract left out: share-alike licence._

### PyJHora

Complete Vedic Astrology Python package and SarvaJyotish Web Service.

`pip install PyJHora` · installs (wheel) · licence: AGPL-3.0-or-later · rank 13111 · last release 2026-11-08 · [PyPI](https://pypi.org/project/PyJHora/) · [source](https://github.com/naturalstupid/pyjhora)

_README extract left out: share-alike licence._

### regions

An Astropy coordinated package for region handling

`pip install regions` · installs (wheel) · licence: BSD-3-Clause · rank 13354 · last release 2026-10-17 · [PyPI](https://pypi.org/project/regions/) · [docs](https://astropy-regions.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Regions is an Astropy package for region handling.

Please see the online documentation for installation
instructions
and usage information.

If you use Regions for a project that leads to a publication, whether
directly or as a dependency of another package, please include the
following acknowledgment:
where (Bradley et al. ...

Sections: Regions, Citing Regions

</details>

### sep

Astronomical source extraction and photometry library

`pip install sep` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 13996 · last release 2025-02-18 · [PyPI](https://pypi.org/project/sep/) · [docs](http://sep-pjw.readthedocs.org)

_README extract left out: share-alike licence._

### casacure

A Rust replacement for the casacore table system, pip installable on any machine

`pip install casacure` · installs (wheel) · licence: LGPL-3.0-or-later · rank 14086 · last release 2026-11-07 · [PyPI](https://pypi.org/project/casacure/) · [source](https://github.com/tmolteno/casacure)

_README extract left out: share-alike licence._

### mocpy

MOCPy allows to create and manipulate MOCs (Multi-Order Coverage maps)

`pip install mocpy` · installs (wheel) · licence: BSD License · rank 14496 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mocpy/) · [docs](https://cds-astro.github.io/mocpy/) · [source](https://github.com/cds-astro/mocpy)

<details><summary>README extract</summary>

MOCPy is a Python library allowing easy creation and manipulation of MOCs (Multi-Order Coverage maps).

MOC is an IVOA standard enabling
description of arbitrary sky, time, (or frequency) coverages.

| | Space | Time | Frequency | ...

Example:
```python
from mocpy import MOC
import astropy.units as u

# Create a MOC from a cone
field_of_view = MOC.from_cone(lon=0*u.deg, lat=0*u.deg, radius=10*u.deg, max_depth=7)

# Check if a position is covered
field_of_view.contains_lonlat(0*u.deg, 0*u.deg)  # True

# Combine MOCs with set operations
...
```

Sections: MOCPy, What's in MOCpy?, Quick example, Other resources, Latest stable version, To run the notebooks, For use in pyodide, Other python packages for MOCs

</details>

### ligo.skymap

Tools for reading, writing, manipulating, and making LIGO/Virgo/KAGRA sky maps

`pip install ligo.skymap` · installs (wheel) · licence: GPL-3.0-or-later · rank 14621 · last release 2026-06-06 · [PyPI](https://pypi.org/project/ligo.skymap/) · [docs](https://lscsoft.docs.ligo.org/ligo.skymap) · [source](https://github.com/lpsinger/ligo.skymap)

_README extract left out: share-alike licence._

### specutils

Package for spectroscopic astronomical data

`pip install specutils` · installs (wheel) · licence: BSD 3-Clause · rank 14694 · last release 2026-06-01 · [PyPI](https://pypi.org/project/specutils/) · [docs](https://specutils.readthedocs.io) · [source](https://github.com/astropy/specutils)

<details><summary>README extract</summary>

Specutils is an Astropy affiliated package
with the goal of providing a shared set of Python representations of
astronomical spectra and basic tools to operate on these spectra. ...

Sections: Specutils, Getting Started with Specutils, Migrating from Specutils 1.x to 2.x, If you locally cloned this repo before 22 Mar 2021

</details>

## Also in this topic

- [convertdate](religion.md#convertdate) - Converts between Gregorian dates and other calendar systems
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [pyswisseph](religion.md#pyswisseph) - Python extension to the Swiss Ephemeris
- [pyvo](database.md#pyvo) - Astropy affiliated package for accessing Virtual Observatory data and services
- [lalsuite](scientific-engineering.md#lalsuite) - LVK Algorithm Library Suite - LALSuite
- [astroquery](database.md#astroquery) - Functions and classes to access online astronomical data resources
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [spiceypy](scientific-engineering.md#spiceypy) - A Python Wrapper for the NAIF CSPICE Toolkit
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [igwn-segments](scientific-engineering-2.md#igwn-segments) - Representations of semi-open intervals
- [igwn-ligolw](scientific-engineering-2.md#igwn-ligolw) - Python LIGO Light-Weight XML I/O Library
- [kerykeion](religion.md#kerykeion) - A Python library for astrological calculations, including natal charts, houses, planetary aspects, and SVG chart generation.
- [igwn-auth-utils](scientific-engineering-2.md#igwn-auth-utils) - Authorisation utilities for IGWN
- [tesseract](scientific-engineering-2.md#tesseract) - Tesselation based Recovery of Amorphous halo Concentrations
- [pyorbital](scientific-engineering-2.md#pyorbital) - Scheduling satellite passes in Python
- [gwdatafind](scientific-engineering-2.md#gwdatafind) - The GWDataFind data discovery client
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [rapid-pe](scientific-engineering-2.md#rapid-pe) - RapidPE: The original low-latency gravitational wave parameter estimation code.
