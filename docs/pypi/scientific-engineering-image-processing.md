# Scientific/Engineering / Image Processing

[Index](README.md) · 2 packages in this topic, 21 more listed under another topic, by downloads.

### qoi

A simple, fast wrapper around qoi (https://qoiformat.org), the 'Quite OK Image' format

`pip install qoi` · installs (wheel) · licence: MIT License · rank 10931 · last release 2026-10-02 · [PyPI](https://pypi.org/project/qoi/)

<details><summary>README extract</summary>

A simple Python wrapper around QOI, the "Quite OK Image" image format (via the `qoi` Rust crate). It's

- Lossless with comparable compression to PNG, but fast! It encodes 4x+ faster and decodes 3x+ faster than PNG in OpenCV or PIL. ...

Example:
```python
import numpy as np
import qoi

# Get your image as a numpy array (OpenCV, Pillow, etc. but here we just create a bunch of noise). Note: HWC ordering
rgb = np.random.randint(low=0, high=255, size=(224, 244, 3)).astype(np.uint8)

# Write it:
_ = qoi.write("/tmp/img.qoi", rgb)

# Read it and check it matches (it should, as we're lossless)
...
```

Sections: QOI, Example, (Single-threaded) Benchmarks, Publishing, TODO, Discussion, Wrap or rewrite?, On the name, What's up with `./src`?

</details>

### pylibCZIrw

A python wrapper around the libCZI C++ library with reading and writing functionality.

`pip install pylibCZIrw` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 13847 · last release 2026-07-06 · [PyPI](https://pypi.org/project/pylibCZIrw/)

_README extract left out: share-alike licence._

## Also in this topic

- [kornia](scientific-engineering-artificial-intelligence.md#kornia) - Open Source Differentiable Computer Vision Library for PyTorch
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [kornia-rs](scientific-engineering.md#kornia-rs) - Low level implementations for computer vision in Rust
- [albucore](scientific-engineering-artificial-intelligence.md#albucore) - High-performance image processing functions for deep learning and computer vision.
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [pyjpegls](file-formats.md#pyjpegls) - JPEG-LS for Python via CharLS C++ Library
- [earthengine-api](multimedia-graphics.md#earthengine-api) - Earth Engine Python API
- [gerbonara](artistic-software.md#gerbonara) - Tools to handle Gerber and Excellon files in Python
- [pyiqa](scientific-engineering.md#pyiqa) - PyTorch Toolbox for Image Quality Assessment
- [fiftyone-brain](scientific-engineering-artificial-intelligence.md#fiftyone-brain) - FiftyOne Brain
- [pyFFTW](multimedia-sound-audio.md#pyfftw) - A pythonic wrapper around FFTW, the FFT library, presenting a unified interface for all the supported transforms.
- [fiftyone-db](scientific-engineering-artificial-intelligence.md#fiftyone-db) - FiftyOne DB
- [voxel51-eta](scientific-engineering-artificial-intelligence.md#voxel51-eta) - Extensible Toolkit for Analytics
- [fiftyone](scientific-engineering-artificial-intelligence.md#fiftyone) - FiftyOne: the open-source tool for building high-quality datasets and computer vision models
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [lightly](scientific-engineering-2.md#lightly) - A deep learning package for self-supervised learning and world models
- [ouster-sdk](scientific-engineering-2.md#ouster-sdk) - Ouster Sensor SDK
- [pyOrthomosaic](scientific-engineering-gis.md#pyorthomosaic) - Native (Cython + optional CUDA) orthomosaic generator for nadir drone imagery
- [torchio](scientific-engineering-2.md#torchio) - Tools for medical image processing with PyTorch
- [boxmot](scientific-engineering-2.md#boxmot) - BoxMOT: pluggable SOTA tracking modules for segmentation, object detection and pose estimation models
- [zeit-cdts](scientific-engineering-gis.md#zeit-cdts) - Change detection and time series analysis of Earth observation data cubes: LandTrendr, CCDC, BFAST, TWDTW, phenology, accuracy assessment, embeddings and deep learning
