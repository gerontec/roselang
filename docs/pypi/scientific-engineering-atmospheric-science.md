# Scientific/Engineering / Atmospheric Science

[Index](README.md) · 3 packages in this topic, 13 more listed under another topic, by downloads.

### xee

A Google Earth Engine extension for Xarray.

`pip install xee` · installs (wheel) · licence: Apache Software License · rank 10320 · last release 2026-07-14 · [PyPI](https://pypi.org/project/xee/)

<details><summary>README extract</summary>

> ⚠️ Breaking Change in v0.1.0
> v0.1.0 includes a major refactor with breaking API changes.
> - Migration steps:
> docs/migration-guide-v0.1.0.md
> - Canonical install options (prerelease vs stable):
> docs/installation.md

Xee is an Xarray backend for Google Earth Engine. ...

Features:
- Lazy, parallel pixel retrieval through Earth Engine
- Flexible output grid definition (fixed resolution or fixed shape)
- CF-friendly dimension order: `[time, y, x]`
- Plays nicely with Xarray, Dask, and friends

Example:
```python
import ee
import xarray as xr
from xee import helpers

# Authenticate once (on a persistent machine):
# earthengine authenticate

project = 'PROJECT-ID'  # Set your Earth Engine registered Google Cloud project ID
...

</details>

### herbie-data

Download numerical weather prediction GRIB2 model data.

`pip install herbie-data` · installs (wheel) · licence: MIT License · rank 10455 · last release 2026-10-27 · [PyPI](https://pypi.org/project/herbie-data/) · [docs](https://herbie.readthedocs.io/) · [source](https://github.com/blaylockbk/Herbie)

<details><summary>README extract</summary>

Access HRRR, GFS, RAP, GEFS, IFS and more!

See also the DeepWiki generated docs.

Herbie is a Python package that makes downloading and working with numerical weather prediction (NWP) model data simple and fast. ...

Example:
```python
from herbie import Herbie

# Create a Herbie object for HRRR model data
H = Herbie(
    '2021-01-01 12:00',  # Date and time
    model='hrrr',         # Model name
    product='sfc',        # Product type
    fxx=6                 # Forecast hour
)

# Show file contents
H.inventory()

# Download and read 2-meter temperature
...
```

...

</details>

### ha-ffmpeg

A library that handling with ffmpeg for home-assistant

`pip install ha-ffmpeg` · installs (wheel) · licence: BSD License · rank 12256 · last release 2024-11-08 · [PyPI](https://pypi.org/project/ha-ffmpeg/)

<details><summary>README extract</summary>

A Python library to control ffmepg from asyncio for Home Assistant.

- Emulate webcam from any video input source for HA
- Analyse a video/audio stream for noise or motion detection
- Grab image from a stream

Take care to protect function calls to this library with `asyncio.shield`.

</details>

## Also in this topic

- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [fluids](education.md#fluids) - Fluid dynamics component of Chemical Engineering Design Library (ChEDL)
- [chemicals](education.md#chemicals) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [thermo](education.md#thermo) - Chemical properties component of Chemical Engineering Design Library (ChEDL)
- [MetPy](scientific-engineering.md#metpy) - Collection of tools for reading, visualizing and performing calculations with weather data.
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [ht](education.md#ht) - Heat transfer component of Chemical Engineering Design Library (ChEDL)
- [xradar](scientific-engineering-2.md#xradar) - Xradar includes all the tools to get your weather radar into the xarray data model.
- [cf-units](scientific-engineering-2.md#cf-units) - Units of measure as required by the Climate and Forecast (CF) metadata conventions
- [regionmask](scientific-engineering-2.md#regionmask) - create masks of geospatial regions for arbitrary grids
- [arm-pyart](scientific-engineering-2.md#arm-pyart) - Py-ART: Python ARM Radar Toolkit
