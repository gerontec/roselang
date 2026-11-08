# Multimedia / Graphics

[Index](README.md) · 131 packages in this topic, 28 more listed under another topic, by downloads.

### pillow

Python Imaging Library (fork)

`pip install pillow` · installs (wheel) · licence: MIT-CMU · rank 43 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pillow/) · [docs](https://pillow.readthedocs.io) · [source](https://github.com/python-pillow/Pillow)

<details><summary>README extract</summary>

Pillow is the friendly PIL fork by Jeffrey 'Alex' Clark and
contributors.
PIL is the Python Imaging Library by Fredrik Lundh and contributors.
Development is supported by:
- Tidelift (since 2018)
- Thanks.dev (since 2023)
- GitHub Sponsors (since 2026)

 docs

 tests

 package

 social

Features:
The Python Imaging Library adds image processing capabilities to your Python interpreter.

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. ...

Sections: Pillow, Python Imaging Library (Fork), Overview, More information, Report a vulnerability

</details>

### fonttools

Tools to manipulate font files

`pip install fonttools` · installs (wheel) · licence: MIT · rank 144 · last release 2026-10-27 · [PyPI](https://pypi.org/project/fonttools/)

<details><summary>README extract</summary>

| fontTools is a library for manipulating fonts, written in Python. The
 project includes the TTX tool, that can convert TrueType and OpenType
 fonts to and from an XML text format, which is also called TTX. It
 supports TrueType, OpenType, AFM and to an extent Type 1 and some
 Mac-specific formats. The project has an MIT open-source
 license. ...

Sections: What is this?, Optional Requirements, Copyrights

</details>

### pymupdf

A high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.

`pip install pymupdf` · installs (wheel) · licence: Dual Licensed - GNU AFFERO GPL 3.0 or Artifex Commercial License · rank 262 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pymupdf/) · [docs](https://pymupdf.readthedocs.io/) · [source](https://github.com/pymupdf/pymupdf)

_README extract left out: share-alike licence._

### matplotlib-inline

Inline Matplotlib backend for Jupyter

`pip install matplotlib-inline` · installs (wheel) · licence: BSD-3-Clause · rank 286 · last release 2026-05-08 · [PyPI](https://pypi.org/project/matplotlib-inline/)

<details><summary>README extract</summary>

This package provides support for matplotlib to display figures directly inline in the Jupyter notebook and related clients, as shown below.

Example:
```python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
```

Sections: Matplotlib Inline Back-end for IPython and Jupyter, Usage

</details>

### pypdfium2

Python bindings to PDFium

`pip install pypdfium2` · installs (wheel) · licence: BSD-3-Clause, Apache-2.0, dependency licenses · rank 314 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pypdfium2/) · [docs](https://pypdfium2.readthedocs.io) · [source](https://github.com/pypdfium2-team/pypdfium2)

<details><summary>README extract</summary>

pypdfium2 is an ABI-level Python 3 binding to PDFium, a powerful and liberal-licensed library for PDF rendering, inspection, manipulation and creation.

It is built with ctypesgen and external PDFium binaries.
The custom setup infrastructure provides a seamless packaging and installation process. ...

Example:
```python
  Note, with the PIL adapter, it might be advantageous to use `force_bitmap_format=pdfium_c.FPDFBitmap_BGRA, rev_byteorder=True` or perhaps `prefer_bgrx=True, maybe_alpha=True, rev_byteorder=True`, to achieve a pixel format supported natively by PIL, and avoid rendering with transparency to a non-alpha bitmap, which can slow down pdfium.

...
```

...

</details>

### qrcode

QR Code image generator

`pip install qrcode` · installs (wheel) · licence: BSD License; Other/Proprietary License · rank 590 · last release 2025-05-01 · [PyPI](https://pypi.org/project/qrcode/)

<details><summary>README extract</summary>

Generate QR codes.

A standard install uses pypng to generate PNG files and can also render QR
codes directly to the console. A standard install is just:
For more image functionality, install qrcode with the `pil` dependency so
that pillow is installed and can be used for generating images:

Example:
```python
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
```

Sections: Pure python QR Code generator, What is a QR Code?, Usage, Advanced Usage, Other image factories, SVG, Pure Python PNG, Styled Image, Examples, 8.2 (01 May 2025), 8.1 (02 April 2025), 8.0 (27 September 2024), 7.4.2 (6 February 2023), 7.4.1 (3 February 2023)

</details>

### seaborn

Statistical data visualization

`pip install seaborn` · installs (wheel) · licence: BSD License · rank 635 · last release 2024-01-25 · [PyPI](https://pypi.org/project/seaborn/) · [docs](http://seaborn.pydata.org) · [source](https://github.com/mwaskom/seaborn)

<details><summary>README extract</summary>

Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

Documentation

Online documentation is available at seaborn.pydata.org.

The docs include a tutorial, example gallery, API reference, FAQ, and other useful information. ...

</details>

### pillow-heif

Python interface for libheif library

`pip install pillow-heif` · installs (wheel) · licence: BSD-3-Clause · rank 651 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pillow-heif/) · [docs](https://pillow-heif.readthedocs.io) · [source](https://github.com/bigcat88/pillow_heif)

<details><summary>README extract</summary>

Python bindings to libheif for working with HEIF images and plugin for Pillow.

Features:
 * Decoding of `8`, `10`, `12` bit HEIC files.
 * Encoding of `8`, `10`, `12` bit HEIC files.
 * `EXIF`, `XMP`, `IPTC` read & write support.
 * Support of multiple images in one file and a `PrimaryImage` attribute.
 * Adding & removing `thumbnails`. ...

Example:
```python
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

im = Image.open("image.heic")  # do whatever need with a Pillow image
im = im.rotate(13)
im.save(f"rotated_image.heic", quality=90)
```

...

</details>

### leather

Python charting for 80% of humans.

`pip install leather` · installs (wheel) · licence: MIT License · rank 793 · last release 2025-12-15 · [PyPI](https://pypi.org/project/leather/)

<details><summary>README extract</summary>

Leather is the Python charting library for those who need charts *now* and don't care if they're perfect.

Leather isn't picky. It's rough. It gets dirty. It looks sexy just hanging on the back of a chair. Leather doesn't need your accessories. Leather is how Snake Plissken would make charts.

Get it?

Important links:

</details>

### pydeck

Widget for deck.gl maps

`pip install pydeck` · installs (wheel) · licence: Apache License 2.0 · rank 797 · last release 2026-07-02 · [PyPI](https://pypi.org/project/pydeck/)

<details><summary>README extract</summary>

The pydeck library is a set of Python bindings for making spatial visualizations with deck.gl,
optimized for a Jupyter environment. To get started, see the documentation.

To install pydeck, see the instructions here.

For interactive demos, click the binder logo below: ...

Example:
```python
import pydeck as pdk

# 2014 locations of car accidents in the UK
UK_ACCIDENTS_DATA = ('
                     'deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv')

# Define a layer to display on a map
layer = pdk.Layer(
    'HexagonLayer',
    UK_ACCIDENTS_DATA,
    get_position=['lng', 'lat'],
    auto_highlight=True,
...
```

</details>

### imagesize

Get image size from headers (BMP/PNG/JPEG/JPEG2000/GIF/TIFF/SVG/Netpbm/WebP/AVIF/HEIC/HEIF)

`pip install imagesize` · installs (wheel) · licence: MIT · rank 808 · last release 2026-08-24 · [PyPI](https://pypi.org/project/imagesize/) · [source](https://github.com/shibukawa/imagesize_py)

<details><summary>README extract</summary>

This module analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG/Netpbm/WebP/BMP/AVIF/HEIC/HEIF image headers and returns image size, DPI, and related metadata.

This module is a pure Python module. You can use file like object like file or something like `io.BytesIO`.

Supported Python versions: 3.10-3.15

Example:
```python
import imagesize

width, height = imagesize.get("test.png")
print(width, height)

xdpi, ydpi = imagesize.getDPI("test.png")
print(xdpi, ydpi)

info = imagesize.get_info("test.png")
print(info.width, info.height, info.rotation, info.xdpi, info.ydpi, info.colors, info.channels)
```

Sections: imagesize, Version 2.0 migration notes, API, Benchmark, Thanks

</details>

### fpdf2

Simple & fast PDF generation for Python

`pip install fpdf2` · installs (wheel) · licence: LGPL-3.0-only · rank 838 · last release 2026-10-29 · [PyPI](https://pypi.org/project/fpdf2/) · [docs](https://py-pdf.github.io/fpdf2/) · [source](https://github.com/py-pdf/fpdf2)

_README extract left out: share-alike licence._

### CairoSVG

A Simple SVG Converter based on Cairo

`pip install CairoSVG` · installs (wheel) · licence: LGPL-3.0-or-later · rank 868 · last release 2026-09-07 · [PyPI](https://pypi.org/project/CairoSVG/) · [docs](https://cairosvg.org/documentation/) · [source](https://github.com/Kozea/CairoSVG/)

_README extract left out: share-alike licence._

### cairocffi

cffi-based cairo bindings for Python

`pip install cairocffi` · installs (wheel) · licence: BSD License · rank 876 · last release 2024-06-18 · [PyPI](https://pypi.org/project/cairocffi/) · [docs](https://doc.courtbouillon.org/cairocffi/) · [source](https://github.com/Kozea/cairocffi/)

<details><summary>README extract</summary>

cairocffi is a CFFI-based drop-in replacement for Pycairo,
a set of Python bindings and object-oriented API for cairo.
Cairo is a 2D vector graphics library with support for multiple backends
including image buffers, PNG, PostScript, PDF, and SVG file output. ...

</details>

### trimesh

Import, export, process, analyze and view triangular meshes.

`pip install trimesh` · installs (wheel) · licence: MIT License · rank 1065 · last release 2026-10-24 · [PyPI](https://pypi.org/project/trimesh/) · [docs](https://trimesh.org)

<details><summary>README extract</summary>

Trimesh is a pure Python 3.10+ library for loading and using triangular meshes with an emphasis on watertight surfaces. The goal of the library is to provide a full featured and well tested Trimesh object which allows for easy manipulation and analysis, in the style of the Polygon object in the Shapely library. ...

Features:
* Import meshes from binary/ASCII STL, Wavefront OBJ, ASCII OFF, binary/ASCII PLY, GLTF/GLB 2.0, 3MF, XAML, 3DXML, etc.
* Export meshes as GLB/GLTF, binary STL, binary PLY, ASCII OFF, OBJ, COLLADA, etc. ...

Example:
```python
import numpy as np
import trimesh

# attach to logger so trimesh messages will be printed to console
trimesh.util.attach_to_log()

# mesh objects can be created from existing faces and vertex data
...

</details>

### pyclipper

Cython wrapper for the C++ translation of the Angus Johnson's Clipper library (ver. 6.4.2)

`pip install pyclipper` · installs (wheel) · licence: OSI Approved; MIT License · rank 1084 · last release 2025-12-01 · [PyPI](https://pypi.org/project/pyclipper/)

<details><summary>README extract</summary>

Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the Angus Johnson's Clipper library (ver.
6.4.2).

Source code is available on
GitHub. The package is published on
PyPI.

 Clipper - an open source freeware library for clipping and
 offsetting lines and polygons. ...

Example:
```python
import pyclipper

subj = (
    ((180, 200), (260, 200), (260, 150), (180, 150)),
    ((215, 160), (230, 190), (200, 190))
)
clip = ((190, 210), (240, 210), (240, 130), (190, 130))

pc = pyclipper.Pyclipper()
pc.AddPath(clip, pyclipper.PT_CLIP, True)
pc.AddPaths(subj, pyclipper.PT_SUBJECT, True)

...
```

...

</details>

### pikepdf

Read, write, repair, and transform PDFs in Python, powered by qpdf

`pip install pikepdf` · installs (wheel) · licence: MPL-2.0 · rank 1130 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pikepdf/) · [docs](https://pikepdf.readthedocs.io/) · [source](https://github.com/pikepdf/pikepdf)

<details><summary>README extract</summary>

<!-- SPDX-FileCopyrightText: 2022 James R. Barlow -->
<!-- SPDX-License-Identifier: MPL-2.0 -->

Read, write, repair, and transform PDFs in Python -- powered by qpdf.

pikepdf is based on qpdf, a mature, actively maintained C++ library for PDF manipulation and repair.

Python + qpdf = "py" + "qpdf" = "pyqpdf", which looks like a dyslexia test. ...

Features:
- Built on qpdf -- backed by a mature, battle-tested C++ PDF library
- Automatic PDF repair -- silently fixes many types of PDF damage on open
- PDF/A compliance -- modify PDFs without breaking PDF/A conformance ...

Example:
```python
import pikepdf

# Open a PDF -- pikepdf (via qpdf) automatically repairs structural damage
with pikepdf.Pdf.open('input.pdf') as pdf:
    num_pages = len(pdf.pages)
    del pdf.pages[-1]
...

</details>

### segno

QR Code and Micro QR Code generator for Python

`pip install segno` · installs (wheel) · licence: BSD License · rank 1335 · last release 2025-03-12 · [PyPI](https://pypi.org/project/segno/) · [docs](https://segno.readthedocs.io/)

<details><summary>README extract</summary>

Pure Python QR Code generator with no dependencies.

This package implements ISO/IEC 18004:2015(E) "QR Code bar code symbology
specification" and produces QR Codes and Micro QR Codes with nearly no effort.
It supports the Structured Append mode
which splits a message across several QR codes. ...

Example:
```python
import segno
qrcode = segno.make('Yellow Submarine')
qrcode.save('yellow-submarine.png')
```

Sections: QR Code encoder and Micro QR Code encoder, Unique features, conda-forge, Debian, Arch Linux, Usage, Command line, Library, Documentation, Trademark

</details>

### PyOpenGL

Standard OpenGL bindings for Python

`pip install PyOpenGL` · installs (wheel) · licence: BSD License · rank 1496 · last release 2025-08-18 · [PyPI](https://pypi.org/project/PyOpenGL/) · [docs](https://mcfletch.github.io/pyopengl/documentation/index.html) · [source](https://github.com/mcfletch/pyopengl)

<details><summary>README extract</summary>

PyOpenGL is normally distributed via PyPI using standard pip:
You can install this repository by branching/cloning and running
`pip`:
Note that to compile PyOpenGL_accelerate you will need to have
a functioning Python extension-compiling environment.

Sections: PyOpenGL and PyOpenGL_Accelerate, Learning PyOpenGL, Running Tests

</details>

### pypng

Pure Python library for saving and loading PNG images

`pip install pypng` · installs (wheel) · licence: MIT License · rank 1498 · last release 2022-07-15 · [PyPI](https://pypi.org/project/pypng/)

<details><summary>README extract</summary>

drj@pobox.com

PNG module for Python. PyPNG is written entirely in Python.

Sections: README for PyPNG, INTRODUCTION, QUICK START, MANIFEST, REFERENCES, END

</details>

### rasterio

Fast and direct raster I/O for use with NumPy

`pip install rasterio` · installs (wheel) · licence: BSD-3-Clause · rank 1581 · last release 2026-09-30 · [PyPI](https://pypi.org/project/rasterio/) · [docs](https://rasterio.readthedocs.io/) · [source](https://github.com/rasterio/rasterio)

<details><summary>README extract</summary>

Rasterio reads and writes geospatial raster data.

Geographic information systems use GeoTIFF and other formats to organize and
store gridded, or raster, datasets. Rasterio reads and writes these formats and
provides a Python API based on N-D arrays.

Rasterio 1.5+ works with Python >= 3.12, Numpy >= 2, and GDAL >= 3.8. ...

Example:
```python
import numpy as np
import rasterio

# Read raster bands directly to Numpy arrays.

with rasterio.open('tests/data/RGB.byte.tif') as src:
    r, g, b = src.read()

# Combine arrays in place. Expecting that the sum will
# temporarily exceed the 8-bit integer range, initialize it as
# a 64-bit float (the numpy default) array. Adding other
...
```

...

</details>

### affine

Matrices describing affine transformation of the plane

`pip install affine` · installs (wheel) · licence: BSD-3-Clause · rank 1619 · last release 2026-08-28 · [PyPI](https://pypi.org/project/affine/) · [source](https://github.com/rasterio/affine)

<details><summary>README extract</summary>

Matrices describing 2D affine transformation of the plane.

The Affine package is derived from Casey Duncan's Planar package. Please see
the copyright statement in src/affine.py.

Example:
```python
>>> from affine import Affine
>>> Affine.identity()
Affine(1.0, 0.0, 0.0,
       0.0, 1.0, 0.0)
>>> Affine.translation(1.0, 5.0)
Affine(1.0, 0.0, 1.0,
       0.0, 1.0, 5.0)
>>> Affine.scale(2.0)
Affine(2.0, 0.0, 0.0,
       0.0, 2.0, 0.0)
>>> Affine.shear(45.0, 45.0)  # decimal degrees
Affine(1.0, 0.9999999999999999, 0.0,
...
```

Sections: Affine, Usage, Usage with GIS data packages

</details>

### glfw

A ctypes-based wrapper for GLFW3.

`pip install glfw` · installs (wheel) · licence: MIT License · rank 1778 · last release 2026-10-16 · [PyPI](https://pypi.org/project/glfw/)

<details><summary>README extract</summary>

This module provides Python bindings for GLFW
(on GitHub: glfw/glfw). It is a
`ctypes` wrapper which keeps very close to the original GLFW API,
except for:

- function names use the pythonic `words_with_underscores` notation
 instead of `camelCase` ...

Example:
```python
import glfw

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
...
```

Sections: pyGLFW, Windows, macOS, Linux, Example Code

</details>

### vtk

VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization

`pip install vtk` · installs (wheel) · licence: BSD License · rank 1796 · last release 2026-11-05 · [PyPI](https://pypi.org/project/vtk/)

<details><summary>README extract</summary>

VTK is an open-source software system for image processing, 3D
graphics, volume rendering and visualization. VTK includes many
advanced algorithms (e.g., surface reconstruction, implicit modeling,
decimation) and rendering techniques (e.g., hardware-accelerated
volume rendering, LOD control). ...

Sections: Introduction, Learning Resources, Reporting Bugs, Requirements, Building

</details>

### pi-heif

Python interface for libheif library

`pip install pi-heif` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 1801 · last release 2026-06-10 · [PyPI](https://pypi.org/project/pi-heif/) · [docs](https://pillow-heif.readthedocs.io) · [source](https://github.com/bigcat88/pillow_heif)

_README extract left out: share-alike licence._

### zxing-cpp

Python bindings for the zxing-cpp barcode library

`pip install zxing-cpp` · installs (wheel) · licence: Apache-2.0 · rank 2079 · last release 2026-07-29 · [PyPI](https://pypi.org/project/zxing-cpp/) · [source](https://github.com/zxing-cpp/zxing-cpp.git)

<details><summary>README extract</summary>

The package uses scikit-build-core as its build backend and nanobind for the Python bindings.

Example:
```python
import cv2, zxingcpp

img = cv2.imread('test.png')
barcodes = zxingcpp.read_barcodes(img)
for barcode in barcodes:
    print('Found barcode:'
        f'\n Text:    "{barcode.text}"'
        f'\n Format:   {barcode.format}'
        f'\n Content:  {barcode.content_type}'
        f'\n Position: {barcode.position}')
if len(barcodes) == 0:
...
```

Sections: Python bindings for zxing-cpp, Usage, Reading barcodes, Writing barcodes

</details>

### freetype-py

Freetype python bindings

`pip install freetype-py` · installs (wheel) · licence: BSD License · rank 2103 · last release 2024-08-29 · [PyPI](https://pypi.org/project/freetype-py/)

<details><summary>README extract</summary>

Freetype Python provides bindings for the FreeType library. Only the
high-level API is bound.

Documentation available at:

Example:
```python
import freetype
face = freetype.Face("Vera.ttf")
face.set_char_size( 48*64 )
face.load_char('S')
bitmap = face.glyph.bitmap
print(bitmap.buffer)
```

Sections: FreeType (high-level Python API), Mac users, Linux users, Window users, Usage example, Screenshots, Freezing apps

</details>

### svgwrite

A Python library to create SVG drawings.

`pip install svgwrite` · installs (wheel) · licence: MIT License · rank 2128 · last release 2022-07-14 · [PyPI](https://pypi.org/project/svgwrite/)

<details><summary>README extract</summary>

This package is inactive! No new features will be added, there will
be no change of behavior, just bugfixes will be merged.

A Python library to create SVG drawings.

a simple example:
for more examples see: examples.py ...

Example:
```python
import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()
```

Sections: svgwrite, Abstract, Documentation, Contact, NEWS, Version 1.4.3 - 2022-07-14, Version 1.4.2 - 2022-03-23, Version 1.4.1 - 2021-01-15, Version 1.4 - 2020-03-28, Version 1.3.1 - 2019-06-28, Version 1.3.0 - 2019-06-23, Version 1.2.1 - 2018-11-16, Version 1.2.0 - 2018-10-27, Version 1.1.12 - 2017-12-27

</details>

### pdfrw

PDF file reader/writer library

`pip install pdfrw` · installs (wheel) · licence: MIT License · rank 2133 · last release 2017-09-18 · [PyPI](https://pypi.org/project/pdfrw/)

<details><summary>README extract</summary>

:Author: Patrick Maupin

pdfrw is a Python library and utility that reads and writes PDF files:

* Version 0.4 is tested and works on Python 2.6, 2.7, 3.3, 3.4, 3.5, and 3.6
* Operations include subsetting, merging, rotating, modifying metadata, etc. ...

Example:
```python
>>> from pdfrw import PdfReader
>>> x = PdfReader('source.pdf')
>>> x.keys()
['/Info', '/Size', '/Root']
>>> x.Info
{'/Producer': '(cairo 1.8.6 (
 '/Creator': '(cairo 1.8.6 (
>>> x.Root.keys()
['/Type', '/Pages']
```

Sections: pdfrw 0.4, Introduction, Examples, All examples, Notes on selected examples, Reorganizing pages and placing them two-up, Adding or modifying metadata, Rotating and doubling, Graphics stream parsing proof of concept, pdfrw philosophy, Core library, PDF files and Python

</details>

### manifold3d

Library for geometric robustness

`pip install manifold3d` · installs (wheel) · licence: Apache Software License · rank 2247 · last release 2026-09-29 · [PyPI](https://pypi.org/project/manifold3d/)

<details><summary>README extract</summary>

C++ Documentation | ManifoldCAD User Guide | JS/TS/WASM API | Algorithm Documentation | Blog Posts | Web Examples

Manifold is a geometry library dedicated to creating and operating on manifold triangle meshes. A manifold mesh is a mesh that represents a solid object, and so is very important in manufacturing, CAD, structural analysis, etc. ...

Example:
```python
>>> import manifold3d
>>> help(manifold3d)
```

Sections: About Manifold, Users, Bindings & Packages, Frontend Sandboxes, [ManifoldCAD.org], [Python Colab Example], Manifold Library, Dependencies, 3D Formats, Building, WASM, Python, Windows Shenanigans, Formatting

</details>

### mss

An ultra fast cross-platform multiple screenshots module in pure python using ctypes.

`pip install mss` · installs (wheel) · licence: MIT License · rank 2560 · last release 2026-04-23 · [PyPI](https://pypi.org/project/mss/) · [docs](https://python-mss.readthedocs.io) · [source](https://github.com/BoboTiG/python-mss)

<details><summary>README extract</summary>

> [!TIP]
> Become my boss to help me work on this awesome software, and make the world better:

An ultra-fast cross-platform multiple screenshots module in pure python using ctypes.

- Python 3.9+, PEP8 compliant, no dependency, thread-safe; ...

Example:
```python
from mss import MSS

# The simplest use, save a screenshot of the 1st monitor
with MSS() as sct:
    sct.shot()
```

</details>

### pillow-avif-plugin

A pillow plugin that adds avif support via libavif

`pip install pillow-avif-plugin` · installs (wheel) · licence: MIT License · rank 2658 · last release 2026-07-22 · [PyPI](https://pypi.org/project/pillow-avif-plugin/)

<details><summary>README extract</summary>

This is a plugin that adds support for AVIF files until official support has been added (see this pull request).

To register this plugin with pillow you will need to add `import pillow_avif` somewhere in your application.

</details>

### python-barcode

Create standard barcodes with Python. No external modules needed. (optional Pillow support included).

`pip install python-barcode` · installs (wheel) · licence: MIT License · rank 2678 · last release 2025-08-27 · [PyPI](https://pypi.org/project/python-barcode/) · [docs](https://python-barcode.readthedocs.io/) · [source](https://github.com/WhyNotHugo/python-barcode)

<details><summary>README extract</summary>

python-barcode provides a simple way to create barcodes in Python.

There are no external dependencies when generating SVG files.
Pillow is required for generating images (e.g.: PNGs).

Support Python 3.9 to 3.12.

Full documentation is published at

You can build the documentation locally using `make -C docs html`.

Sections: python-barcode, Documentation

</details>

### PyMuPDFb

MuPDF shared libraries for PyMuPDF.

`pip install PyMuPDFb` · installs (wheel) · licence: GNU AFFERO GPL 3.0 · rank 2988 · last release 2024-09-02 · [PyPI](https://pypi.org/project/PyMuPDFb/) · [docs](https://pymupdf.readthedocs.io/) · [source](https://github.com/pymupdf/pymupdf)

_README extract left out: share-alike licence._

### ipympl

Matplotlib Jupyter Extension

`pip install ipympl` · installs (wheel) · licence: BSD License · rank 3010 · last release 2026-01-21 · [PyPI](https://pypi.org/project/ipympl/) · [source](https://github.com/matplotlib/ipympl)

<details><summary>README extract</summary>

Leveraging the Jupyter interactive widgets framework, `ipympl` enables the interactive features of matplotlib in the Jupyter notebook and in JupyterLab.

Besides, the figure `canvas` element is a proper Jupyter interactive widget which can be positioned in interactive widget layouts.

Sections: ipympl, Usage, Documentation, Example, With conda, With pip, Use in JupyterLab, How to see your changes, Classic Jupyter Notebook

</details>

### python-nvd3

Python NVD3 - Chart Library for d3.js

`pip install python-nvd3` · installs from source (sdist only) · licence: MIT License · rank 3079 · last release 2024-04-22 · [PyPI](https://pypi.org/project/python-nvd3/)

<details><summary>README extract</summary>

:Description: Python-nvd3 is a wrapper for NVD3 graph library
:NVD3: NVD3
:D3: Data-Driven Documents
:Maintainers: Areski & Oz
:Contributors: list of contributors

NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js offers you. ...

Example:
```python
>>> from nvd3 import pieChart
>>> chart_name = 'pieChart'
>>> chart = pieChart(name=chart_name, color_category='category20c', height=450, width=450)
>>> xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
>>> ydata = [3, 4, 0, 1, 5, 7, 3]
>>> extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
...
```

...

</details>

### fpdf

Simple PDF generation for Python

`pip install fpdf` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 3108 · last release 2015-01-22 · [PyPI](https://pypi.org/project/fpdf/)

_README extract left out: share-alike licence._

### svgelements

Svg Elements Parsing

`pip install svgelements` · installs (wheel) · licence: MIT License · rank 3119 · last release 2023-08-17 · [PyPI](https://pypi.org/project/svgelements/)

<details><summary>README extract</summary>

`svgelements` does high fidelity SVG parsing and geometric rendering. The goal is to successfully and correctly process SVG for use with any scripts that may need or want to use SVG files as geometric data. ...

Features:
SVG is a huge spec and bleeds into a lot of areas. Many of these are supported some are not.

Example:
```python
def parse(source,
          reify=True,
          ppi=DEFAULT_PPI,
          width=1,
          height=1,
          color="black",
          transform=None,
          context=None):
```

Sections: svgelements, Requirements, Compatibility, Philosophy, Parsing, Writing, Overview, Point, Matrix, Path, Angle, Color, Length, Examples

</details>

### usd-core

Pixar's Universal Scene Description

`pip install usd-core` · installs (wheel) · licence: LicenseRef-TOST-1.0 · rank 3175 · last release 2026-10-21 · [PyPI](https://pypi.org/project/usd-core/) · [docs](https://openusd.org) · [source](https://github.com/PixarAnimationStudios/OpenUSD)

<details><summary>README extract</summary>

Universal Scene Description (USD) is a system that scalably encodes and
interchanges static and time-sampled 3D geometry, shading and lighting data
between Digital Content Creation applications. Domain-specific schema modules
define the geometry, shading, and lighting encoding atop USD's domain-agnostic
core. ...

</details>

### svgpathtools

A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.

`pip install svgpathtools` · installs (wheel) · licence: MIT License · rank 3342 · last release 2026-09-05 · [PyPI](https://pypi.org/project/svgpathtools/)

<details><summary>README extract</summary>

svgpathtools is a collection of tools for manipulating and analyzing SVG Path objects and Bézier curves.

Features:
svgpathtools contains functions designed to easily read, write and display SVG files as well as *a large selection of geometrically\-oriented tools* to transform and analyze path elements. ...

Example:
```python
from future import division, print_function
```

Sections: svgpathtools, Features, Prerequisites, Setup, Alternative Setup, Credit where credit's due, Basic Usage, Classes, Reading SVGSs, Writing SVGSs (and some geometric functions and methods), Bezier curves as NumPy polynomial objects, Numpy Array operations on Bézier path segments, Tangent vectors (and more on NumPy polynomials), Rotations and Translations

</details>

### Wand

Ctypes-based simple MagickWand API binding for Python

`pip install Wand` · installs (wheel) · licence: MIT · rank 3723 · last release 2026-06-25 · [PyPI](https://pypi.org/project/Wand/) · [docs](https://docs.wand-py.org/en/latest/index.html) · [source](https://github.com/emcconville/wand)

<details><summary>README extract</summary>

Wand is a `ctypes`-based simple ImageMagick binding for Python,
supporting 3.8+ and PyPy. All functionalities of MagickWand API are
implemented in Wand.

You can install the package from PyPI by using `pip`:

Or would you like to enjoy the bleeding edge? Check out the head
revision of the source code from the GitHub repository:


Sections: Wand, Docs

</details>

### svg.path

SVG path objects and parser

`pip install svg.path` · installs (wheel) · licence: MIT License · rank 3743 · last release 2026-07-07 · [PyPI](https://pypi.org/project/svg.path/)

<details><summary>README extract</summary>

svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.

Example:
```python
>>> from svg.path import Path, Move, Line, Arc, CubicBezier, QuadraticBezier, Close
```

Sections: svg.path, Usage, Future features, 7.1 (2026-07-07), 7.0 (2025-07-06), 6.4b1 (2025-02-27), 6.3 (2023-04-29), 6.2 (2022-06-17), 6.1 (2022-06-09), 6.0 (2022-04-14), 6.0b1 (2022-04-02), 5.1 (2022-03-23), 5.0.1 (2022-03-21), 5.0.0 (2022-03-21)

</details>

### supervision

A set of easy-to-use utils that will come in handy in any Computer Vision project

`pip install supervision` · installs (wheel) · licence: MIT · rank 3953 · last release 2026-11-05 · [PyPI](https://pypi.org/project/supervision/) · [docs](https://supervision.roboflow.com/latest/) · [source](https://github.com/roboflow/supervision)

<details><summary>README extract</summary>

notebooks | inference | autodistill | maestro

📑 Table of Contents

- 👋 Hello
- 💻 Install
- 🔥 Quickstart
 - Models
 - Annotators
 - Datasets
- 🎬 Tutorials
- 💜 Built with Supervision
- 📚 Documentation
- 🏆 Contribution

We are your essential toolkit for computer vision. ...

Example:
```python
import supervision as sv
from PIL import Image
from rfdetr import RFDETRSmall

image = Image.open("path/to/image.jpg")
model = RFDETRSmall()
detections = model.predict(image, threshold=0.5)

len(detections)
# 5
```

Sections: 👋 Hello, 🔥 Quickstart, Models, Annotators, Datasets, 🎬 Tutorials, 💜 Built with Supervision, 📚 Documentation

</details>

### pyvips

binding for the libvips image processing library

`pip install pyvips` · installs from source (sdist only) · licence: MIT License · rank 4049 · last release 2026-08-29 · [PyPI](https://pypi.org/project/pyvips/) · [docs](https://libvips.github.io/pyvips/) · [source](https://github.com/libvips/pyvips)

<details><summary>README extract</summary>

PyPI package:

conda package:

We have formatted docs online here:

This module wraps the libvips image processing library:

The libvips docs are also very useful:

If you have the development headers for libvips installed and have a working C
compiler, this module will use cffi API mode to try to build a libvips
binary extension for your Python. ...

Example:
```python
import pyvips

image = pyvips.Image.new_from_file('some-image.jpg', access='sequential')
image *= [1, 2, 1]
mask = pyvips.Image.new_from_array([
    [-1, -1, -1],
    [-1, 16, -1],
    [-1, -1, -1],
], scale=8)
image = image.conv(mask, precision='integer')
image.write_to_file('x.jpg')
```

Sections: README, How it works, Linux, macOS, Windows, Conda, Example, Notes

</details>

### psd-tools

Python package for working with Adobe Photoshop PSD files

`pip install psd-tools` · installs (wheel) · licence: MIT · rank 4180 · last release 2026-10-21 · [PyPI](https://pypi.org/project/psd-tools/)

<details><summary>README extract</summary>

`psd-tools` is a Python package for working with Adobe Photoshop PSD files
as described in specification.

Example:
```python
from psd_tools import PSDImage

psd = PSDImage.open('example.psd')
psd.composite().save('example.png')

for layer in psd:
    print(layer)
    layer_image = layer.composite()
    layer_image.save('%s.png' % layer.name)
```

Sections: psd-tools, Features, Getting started

</details>

### cascadio

Convert STEP files to GLB using OpenCASCADE

`pip install cascadio` · installs (wheel) · licence: not stated · rank 4479 · last release 2026-07-28 · [PyPI](https://pypi.org/project/cascadio/)

<details><summary>README extract</summary>

A Python library which uses OpenCASCADE to convert STEP files to a GLB file which can quickly be loaded by trimesh and other libraries.

The primary effort here is build and packaging using the wonderful work done recently on scikit-build-core and cibuildwheel. The goal is to produce wheels that don't require users to build OpenCASCADE themselves. ...

Sections: cascadio, warning: :warning: :warning: :warning, Motivation, Patching OCCT, Future Work

</details>

### mediapy

Read/write/show images and videos in an IPython notebook

`pip install mediapy` · installs (wheel) · licence: Apache Software License · rank 4484 · last release 2026-07-01 · [PyPI](https://pypi.org/project/mediapy/) · [source](https://github.com/google/mediapy)

<details><summary>README extract</summary>

[[GitHub source]]( &nbsp;
[[API docs]]( &nbsp;
[[Colab example]](

Example:
```python
!pip install -q mediapy
import mediapy as media
import numpy as np

image = media.read_image('
print(image.shape, image.dtype)  # It is a numpy array.
media.show_image(image)

checkerboard = np.kron([[0, 1] * 16, [1, 0] * 16] * 16, np.ones((4, 4)))
media.show_image(checkerboard)

...
```

Sections: Examples, Images, Videos, Setup

</details>

### bd-materials

Typical-values engineering materials for build123d -- with finishes and three.js PBR looks

`pip install bd-materials` · installs (wheel) · licence: not stated · rank 4988 · last release 2026-10-23 · [PyPI](https://pypi.org/project/bd-materials/) · [source](https://github.com/bernhard-42/bd_materials)

<details><summary>README extract</summary>

Typical-value engineering materials — give a part a named material, get its mass and mechanical/thermal properties, and resolve how it looks (finish + color → three.js PBR).

Example:
```python
from bd_materials import metals, finishes

part = metals.aluminum(metals.Alu.G7075_T6, finishes.anodize("champagne"))
part.material.mass(volume_mm3=8000)   # grams
part.material                         # print -> typical-value range table
part.pbr                              # three.js material for OCP VSCode
```

...

</details>

### rawpy

RAW image processing for Python, a wrapper for libraw

`pip install rawpy` · installs (wheel) · licence: MIT · rank 5027 · last release 2026-10-31 · [PyPI](https://pypi.org/project/rawpy/) · [docs](https://letmaik.github.io/rawpy/) · [source](https://github.com/letmaik/rawpy.git)

<details><summary>README extract</summary>

rawpy is an easy-to-use Python wrapper for the LibRaw library.
It also contains some extra functionality for finding and repairing hot/dead pixels.

API Documentation

Jupyter notebook tutorials

Load a RAW file and save the postprocessed image using default parameters:

Save as 16-bit linear image: ...

Example:
```python
import rawpy
import imageio.v3 as iio

path = 'image.nef'
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
iio.imwrite('default.tiff', rgb)
```

Sections: Sample code, Optional features, FAQ, I'm getting deadlocks when using multiprocessing on Linux

</details>

### potracer

Python Potrace

`pip install potracer` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 5068 · last release 2022-01-26 · [PyPI](https://pypi.org/project/potracer/)

_README extract left out: share-alike licence._

### Willow

A Python image library that sits on top of Pillow, Wand and OpenCV

`pip install Willow` · installs (wheel) · licence: BSD License · rank 5198 · last release 2025-10-26 · [PyPI](https://pypi.org/project/Willow/) · [docs](https://willow.wagtail.org/) · [source](https://github.com/wagtail/Willow)

<details><summary>README extract</summary>

A wrapper that combines the functionality of multiple Python image libraries into one API.

Documentation

Features:
Willow is a simple image library that combines the APIs of Pillow, Wand and OpenCV.
It converts the image between the libraries when necessary. ...

Example:
```python
from willow.image import Image

f = open('test.png', 'rb')
img = Image.open(f)

# Resize the image to 100x100 pixels
img = img.resize((100, 100))

# Save it
with open('test_thumbnail.png', 'wb') as out:
   img.save_as_png(out)
```

Sections: Willow image library, Overview, Examples, Resizing an image, Detecting faces, Available operations

</details>

### skia-pathops

Python access to operations on paths using the Skia library

`pip install skia-pathops` · installs (wheel) · licence: BSD License · rank 5215 · last release 2026-02-16 · [PyPI](https://pypi.org/project/skia-pathops/)

<details><summary>README extract</summary>

Python bindings for the Google Skia library's Path
Ops module, performing boolean
operations on paths (intersection, union, difference, xor).

</details>

### tesserocr

A simple, Pillow-friendly, Python wrapper around tesseract-ocr API using Cython

`pip install tesserocr` · installs (wheel) · licence: MIT · rank 5374 · last release 2026-10-22 · [PyPI](https://pypi.org/project/tesserocr/)

<details><summary>README extract</summary>

A simple, -friendly,
wrapper around the `tesseract-ocr` API for Optical Character Recognition
(OCR).

tesserocr integrates directly with Tesseract's C++ API using Cython
which allows for a simple Pythonic and easy-to-read source code. ...

Example:
```python
from tesserocr import PyTessBaseAPI

images = ['sample.jpg', 'sample2.jpg', 'sample3.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
...
```

...

</details>

### earthengine-api

Earth Engine Python API

`pip install earthengine-api` · installs (wheel) · licence: Apache Software License · rank 5404 · last release 2026-11-02 · [PyPI](https://pypi.org/project/earthengine-api/)

<details><summary>README extract</summary>

Visit the Google Earth Engine Python installation page
for setup instructions.

Note that some classes and algorithms are loaded dynamically and are not
included as part of the Python package or visible in the
source code.
For a complete listing of all Earth Engine client classes and methods, refer to
the API Reference.

</details>

### color-operations

Apply basic color-oriented image operations.

`pip install color-operations` · installs (wheel) · licence: MIT · rank 5474 · last release 2026-08-20 · [PyPI](https://pypi.org/project/color-operations/) · [source](https://github.com/vincentsarago/color-operations)

<details><summary>README extract</summary>

Apply basic color-oriented image operations.

Modified version of Mapbox's rio-color, removing rasterio dependency and with python>=3.10 compatibility.

Example:
```python
from color_operations import parse_operations

ops = "gamma b 1.85, gamma rg 1.95, sigmoidal rgb 35 0.13, saturation 1.15"

assert arr.shape[0] == 3
assert arr.min() >= 0
assert arr.max() <= 1

for func in parse_operations(ops):
    arr = func(arr)
```

Sections: color-operations (fork of rio-color ), Operations, Examples, Sigmoidal, Gamma, Saturation, Combinations of operations, Python API, `color_operations.operations`, `color_operations.colorspace`

</details>

### texture2ddecoder

a python wrapper for Perfare's Texture2DDecoder

`pip install texture2ddecoder` · installs (wheel) · licence: MIT License · rank 5824 · last release 2026-01-16 · [PyPI](https://pypi.org/project/texture2ddecoder/)

<details><summary>README extract</summary>

A python wrapper for Perfare's Texture2DDecoder

Some changes were made to the original code to make it cross-platform compatible.

1. Installation
2. Example
3. Functions

Example:
```python
import texture2ddecoder

# load sample data
data = open("astc_sample", "rb").read()

# decode data
width = 512
height = 512
block_width = block_height = 4

decoded_data= texture2ddecoder.decode_astc(data, width, height, block_width, block_height)

# load raw image data
...
```

Sections: texture2ddecoder, Example, Functions, decode_bc1, decode_bc3, decode_pvrtc, decode_etc1, decode_etc2, decode_etc2a1, decode_etc2a8, decode_eacr, decode_eacr_signed, decode_eacrg, decode_eacrg_signed

</details>

### nokap

Capture screenshots and PDFs from web pages using headless Chrome via CDP.

`pip install nokap` · installs (wheel) · licence: MIT License · rank 5848 · last release 2026-06-08 · [PyPI](https://pypi.org/project/nokap/) · [docs](https://posit-dev.github.io/nokap/) · [source](https://github.com/posit-dev/nokap)

<details><summary>README extract</summary>

_Screenshots and PDFs from web pages. Powered by headless Chrome._

nokap captures screenshots and PDFs from web pages (or local HTML) using headless Chrome via the Chrome DevTools Protocol. It doesn't need Selenium or Playwright. We use just one lightweight dependency (`websockets`).

Features:
| Feature | Details |

| Image formats | PNG, JPEG, WebP |
| PDF generation | Configurable page size, margins, orientation |
| CSS selectors | Capture specific elements (or union of multiple) |
| Zoom/scale | Produce retina-quality (2×, 3×) images ...

Example:
```python
import nokap

# Screenshot a URL
nokap.webshot(" "example.png")

# Save as PDF
nokap.webshot(" "example.pdf")

# Screenshot with a CSS selector (captures just that element)
nokap.webshot(" "header.png", selector="h1")

...

</details>

### pymupdfpro

Commercial extensions for PyMuPDF; enables Office document handling, including doc, docx, hwp, hwpx, ppt, pptx, xls, xls, and others. Supports text and table extraction, document conversion and more.

`pip install pymupdfpro` · installs (wheel) · licence: Other/Proprietary License · rank 5890 · last release 2026-08-06 · [PyPI](https://pypi.org/project/pymupdfpro/)

<details><summary>README extract</summary>

Features:
PyMuPDF Pro is a set of commercial extensions for PyMuPDF.

* Enables Office document handling, including doc, docx, hwp, hwpx, ppt, pptx, xls, xlsx, and others.

* Supports text and table extraction, document conversion and more. ...

Example:
```python
import pymupdf.pro
pymupdf.pro.unlock()

# PyMuPDF has now been extended with PyMuPDF Pro features, with some
# restrictions.
```

Sections: PyMuPDF Pro, Overview, Usage, Licensing

</details>

### etcpak

python wrapper for etcpak

`pip install etcpak` · installs (wheel) · licence: MIT License · rank 5922 · last release 2025-08-11 · [PyPI](https://pypi.org/project/etcpak/)

<details><summary>README extract</summary>

A python wrapper for wolfpld/etcpak
All relevant function and class documentation was taken from wolfpld/etcpak.

1. Installation
2. Example
3. Functions

Example:
```python
from PIL import Image
import etcpak

# load image
img = Image.open(file_path)

# get image data
img_data = img.convert("RGBA").tobytes()

# compress data
compressed = etcpak.compress_bc3(img_data, img.width, img.height)
```

Sections: etcpak, Example, Functions

</details>

### astc-encoder-py

a python wrapper for astc-encoder

`pip install astc-encoder-py` · installs (wheel) · licence: MIT License · rank 5948 · last release 2025-09-06 · [PyPI](https://pypi.org/project/astc-encoder-py/)

<details><summary>README extract</summary>

``astc-encoder-py`` is a Python binding of astc-encoder.
It can compress images into astc textures and decompress astc textures into images.

Example:
```python
# import following once to register the codec
import astc_encoder.pil_codec

# pass the relevant data to the decoder via the decoder args as below
profile: int = 1 # LDR_SRGB = 0, LDR = 1, HDR_RGB_LDR_A = 2, HDR = 3
block_width: int = 4
block_height: int = 4
...
```

Sections: astc-encoder-py, Examples, simple astc via PIL.Image, compressing and decompressing using astc_encoder, TODO

</details>

### pygal

A Python svg graph plotting library

`pip install pygal` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 6048 · last release 2026-06-18 · [PyPI](https://pypi.org/project/pygal/)

_README extract left out: share-alike licence._

### pyvips-binary

Binary distribution of libvips and dependencies for use with pyvips

`pip install pyvips-binary` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 6341 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pyvips-binary/) · [source](https://github.com/kleisauke/pyvips-binary)

_README extract left out: share-alike licence._

### vncdotool

Command line VNC client

`pip install vncdotool` · installs (wheel) · licence: MIT License · rank 6736 · last release 2026-09-06 · [PyPI](https://pypi.org/project/vncdotool/)

<details><summary>README extract</summary>

vncdotool is a command line VNC client.
It can be useful to automating interactions with virtual machines or
hardware devices that are otherwise difficult to control.

It's under active development and seems to be working, but please report any problems you have.

Sections: vncdotool, Quick Start, Feedback, 1.4.2 (2026-09-06), 1.4.1 (2026-08-19), 1.4.0 (2026-08-19), 1.3.0 (2026-04-03), 1.2.0 (2023-06-06), 1.1.0 (2023-04-01), 1.0.0 (2020-04-10), 0.13.0 (2019-11-21), 0.12.1 (2018-12-06), 0.12.0 (2018-04-07), 0.11.2 (2017-09-24)

</details>

### html2image

Package acting as a wrapper around the headless mode of existing web browsers to generate images from URLs and from HTML+CSS strings or files.

`pip install html2image` · installs (wheel) · licence: MIT License · rank 6848 · last release 2025-05-16 · [PyPI](https://pypi.org/project/html2image/) · [source](https://github.com/vgalin/html2image)

<details><summary>README extract</summary>

|PyPI Package|GitHub Repository|
|-|-|

A lightweight Python package acting as wrapper around the headless mode of existing web browsers, allowing image generation from HTML/CSS strings, files and URLs.

This package has been tested on Windows, Ubuntu (desktop and server) and MacOS. ...

Example:
```python
hti.screenshot(url=' save_as='python_org.png')
```

Sections: Principle, Usage, First, import the package and instantiate it, Then take a screenshot, A few examples, Change browser flags, Using the CLI, Hello, World, Hi, Using a Docker Container, FAQ, Running Tests, TODO List

</details>

### pyglm

OpenGL Mathematics library for Python

`pip install pyglm` · installs (wheel) · licence: zlib/libpng License · rank 6969 · last release 2025-11-26 · [PyPI](https://pypi.org/project/pyglm/) · [docs](https://github.com/Zuzu-Typ/PyGLM/wiki) · [source](https://github.com/Zuzu-Typ/PyGLM/)

<details><summary>README extract</summary>

GLSL \+ Optional features \+ Python = PyGLM
A mathematics library for graphics programming\.

PyGLM is a Python extension written in C\+\+\.
By using GLM by G\-Truc under the hood, it manages to bring glm's features to Python\.&nbsp;&nbsp;
Some features are unsupported \(such as most unstable extensions\)\. ...

Features:
Besides the obvious \- being mostly compatible with GLM \- PyGLM offers a variety of features for vector and matrix manipulation\.
It has a lot of possible use cases, including 3D\-Graphics \(OpenGL, DirectX, \.\.\.\), Physics and more\. ...

Example:
```python
glm.sizeof(<type>)
```

...

</details>

### pdfrw2

PDF file reader/writer library

`pip install pdfrw2` · installs (wheel) · licence: MIT License · rank 7019 · last release 2021-11-30 · [PyPI](https://pypi.org/project/pdfrw2/)

<details><summary>README extract</summary>

:Author: Patrick Maupin

:Forked Version by Sam Arnold which
fixes many of the bugs from pdfrw 0.4
including corrupted PDF forms.

pdfrw is a Python library and utility that reads and writes PDF files: ...

Example:
```python
>>> from pdfrw import PdfReader
>>> x = PdfReader('source.pdf')
>>> x.keys()
['/Info', '/Size', '/Root']
>>> x.Info
{'/Producer': '(cairo 1.8.6 (
 '/Creator': '(cairo 1.8.6 (
>>> x.Root.keys()
['/Type', '/Pages']
```

Sections: pdfrw2 0.5.0, Introduction, Examples, All examples, Notes on selected examples, Reorganizing pages and placing them two-up, Adding or modifying metadata, Rotating and doubling, Graphics stream parsing proof of concept, pdfrw philosophy, Core library, PDF files and Python

</details>

### aggdraw

High quality drawing interface for PIL.

`pip install aggdraw` · installs (wheel) · licence: Python (MIT style) · rank 7028 · last release 2025-12-03 · [PyPI](https://pypi.org/project/aggdraw/)

<details><summary>README extract</summary>

A high-quality graphics engine for PIL, based on Maxim Shemanarev's
Anti-Grain Geometry library (from
The aggdraw module implements the basic WCK 2D Drawing Interface on
top of the AGG library. This library provides high-quality drawing,
with anti-aliasing and alpha compositing, while being fully compatible
with the WCK renderer. ...

Sections: The aggdraw module, Build instructions (all platforms), Additional Patches

</details>

### pyvista-cad

PyVista accessor and reader-registry plugin for CAD formats (STEP, IGES, BREP, DXF, 3MF, IFC, FCStd) and bridges to build123d, cadquery, and OCP.

`pip install pyvista-cad` · installs (wheel) · licence: MIT · rank 7040 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pyvista-cad/) · [docs](https://pyvista.github.io/pyvista-cad/) · [source](https://github.com/pyvista/pyvista-cad)

<details><summary>README extract</summary>

CAD format reading, writing, and CAD-style plotting for PyVista.

Built and maintained by CoDimensional PBC.

`pyvista-cad` adds CAD-format support to PyVista: STEP, IGES, BREP, DXF, 3MF, IFC, FreeCAD `.fcstd`, OpenSCAD `.scad`, and glTF. ...

Example:
```python
import pyvista as pv
import pyvista_cad  # registers the .cad accessor and reader entries

mesh = pv.read('part.step')  # MultiBlock of parts with cad.color, cad.label
mesh.plot(show_edges=True)

floorplan = pv.read('floor.dxf')  # PolyData with Layer cell data
layers = floorplan.cad.split_by_layer()  # MultiBlock keyed on layer
```

Sections: pyvista-cad, Quick start, CAD-friendly plotting, Real-world workflow, Common tasks, Licensing, IGES backends, Speed, Trimmed surfaces, Fidelity and limitations

</details>

### skia-python

Skia python binding

`pip install skia-python` · installs (wheel) · licence: BSD License · rank 7112 · last release 2026-10-20 · [PyPI](https://pypi.org/project/skia-python/)

<details><summary>README extract</summary>

Python binding to Skia Graphics Library.

- Binding based on pybind11.

Sections: Skia python binding, Examples, Documentation

</details>

### PyOpenGL-accelerate

Cython-coded accelerators for PyOpenGL

`pip install PyOpenGL-accelerate` · installs (wheel) · licence: BSD License · rank 7145 · last release 2025-08-18 · [PyPI](https://pypi.org/project/PyOpenGL-accelerate/) · [docs](https://mcfletch.github.io/pyopengl/documentation/index.html) · [source](https://github.com/mcfletch/pyopengl)

<details><summary>README extract</summary>

This set of C (Cython) extensions provides acceleration of common operations
for slow points in PyOpenGL 3.x. It is not a requirement for using PyOpenGL
but performance without it will be poor.

Cython is updated frequently to support newer versions of Python. ...

Sections: Acceleration code for PyOpenGL, Build Process

</details>

### blurhash

Pure-Python implementation of the blurhash algorithm.

`pip install blurhash` · installs (wheel) · licence: MIT License · rank 7329 · last release 2025-08-17 · [PyPI](https://pypi.org/project/blurhash/)

<details><summary>README extract</summary>

Blurhash is an algorithm that lets you transform image data into a small text representation of a blurred version of the image. This is useful since this small textual representation can be included when sending objects that may have images attached around, which then can be used to quickly create a placeholder for images that are still loading or ...

Example:
```python
import blurhash
import PIL.Image
import numpy

PIL.Image.open("cool_cat_small.jpg")
# Result:
```

</details>

### OpenImageIO

Reading, writing, and processing images in a wide variety of file formats, using a format-agnostic API, aimed at VFX applications.

`pip install OpenImageIO` · installs (wheel) · licence: Apache Software License · rank 7774 · last release 2026-10-28 · [PyPI](https://pypi.org/project/OpenImageIO/) · [docs](https://docs.openimageio.org) · [source](https://github.com/AcademySoftwareFoundation/OpenImageIO)

<details><summary>README extract</summary>

Introduction

Mission statement: OpenImageIO is a toolset for reading, writing, and
manipulating image files of any image file format relevant to VFX / animation
via a format-agnostic API with a feature set, scalability, and robustness
needed for feature film production. ...

</details>

### ipyvue

Jupyter widgets base for Vue libraries

`pip install ipyvue` · installs (wheel) · licence: MIT · rank 7911 · last release 2026-10-06 · [PyPI](https://pypi.org/project/ipyvue/)

### ipyleaflet

A Jupyter widget for dynamic Leaflet maps

`pip install ipyleaflet` · installs (wheel) · licence: MIT License · rank 7933 · last release 2025-06-13 · [PyPI](https://pypi.org/project/ipyleaflet/)

<details><summary>README extract</summary>

A Jupyter / Leaflet bridge enabling interactive maps in the Jupyter notebook.

Sections: ipyleaflet, Usage, Selecting a basemap for a leaflet map, Loading a geojson map, Making use of leafletjs primitives, Using the splitmap control, Displaying velocity data on the top of a map, Choropleth layer, Widget control, Documentation, Related projects

</details>

### OpenTimelineIO

Editorial interchange format and API

`pip install OpenTimelineIO` · installs from source (sdist only) · licence: Apache Software License · rank 8107 · last release 2025-11-09 · [PyPI](https://pypi.org/project/OpenTimelineIO/) · [docs](https://opentimelineio.readthedocs.io/) · [source](https://github.com/AcademySoftwareFoundation/OpenTimelineIO)

<details><summary>README extract</summary>

OpenTimelineIO is an interchange format and API for
editorial cut information. OTIO is not a container format for media, rather it
contains information about the order and length of cuts and references to
external media.

OTIO includes both a file format and an API for manipulating that format. ...

</details>

### jupyter-leaflet

ipyleaflet extensions for JupyterLab and Jupyter Notebook

`pip install jupyter-leaflet` · installs (wheel) · licence: MIT License · rank 8123 · last release 2025-06-13 · [PyPI](https://pypi.org/project/jupyter-leaflet/)

<details><summary>README extract</summary>

Interactive leaflet widget for the Jupyter notebook

The reference Python backend, `ipyleaflet` is available
here, with examples.

</details>

### manim

Animation engine for explanatory math videos.

`pip install manim` · installs (wheel) · licence: MIT · rank 8262 · last release 2026-10-27 · [PyPI](https://pypi.org/project/manim/) · [docs](https://docs.manim.community/) · [source](https://github.com/manimcommunity/manim)

<details><summary>README extract</summary>

An animation engine for explanatory math videos

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically, as demonstrated in the videos of 3Blue1Brown.

> [!NOTE]
> The community edition of Manim (ManimCE) is a version maintained and developed by the community. ...

Example:
```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

Sections: Usage, Command line arguments, Documentation, Docker, Help with Manim

</details>

### ipyvuetify

Jupyter widgets based on vuetify UI components

`pip install ipyvuetify` · installs (wheel) · licence: MIT License · rank 8291 · last release 2026-10-06 · [PyPI](https://pypi.org/project/ipyvuetify/) · [source](https://github.com/widgetti/ipyvuetify)

<details><summary>README extract</summary>

Jupyter widgets based on vuetify UI components which implement Google's
Material Design Spec with the Vue.js framework.

A small selection of widgets:

Example:
```python
drawer = v.NavigationDrawer(rail=True, ...)

def update_rail(widget, event, data):
    drawer.rail = data

drawer.on_event('update:rail', update_rail)
```

Sections: ipyvuetify, Documentation, Usage, Advanced usage, v-model arguments, Vuetify, (scoped) slots, Icons, Alternate usage

</details>

### dxcam

A Python high-performance screenshot library for Windows using Desktop Duplication API

`pip install dxcam` · installs from source (sdist only) · licence: MIT · rank 8900 · last release 2026-03-12 · [PyPI](https://pypi.org/project/dxcam/) · [source](https://github.com/ra1nty/DXcam)

<details><summary>README extract</summary>

> *Fast Python Screen Capture for Windows - Updated 2026*

> Live API Docs:

DXcam is a high-performance python screenshot and capture library for Windows based on the Desktop Duplication API.
It is designed for low-latency, high-FPS capture pipelines (including full-screen Direct3D applications). ...

Example:
```python
import dxcam
camera = dxcam.create()  # primary output on device 0
```

Sections: DXcam, Introduction, From PyPI (pip), From source, Usage, Screenshot, Screen Capture, Consume the Screen Capture Data, Safely Releasing Resources, Advanced Usage and Remarks, Multiple monitors / GPUs, Output Format, Frame Buffer, Target FPS

</details>

### aspose-slides

Aspose.Slides for Python via .NET is a presentation file formats processing library for working with Microsoft PowerPoint files without using Microsoft PowerPoint.

`pip install aspose-slides` · installs (wheel) · licence: Free To Use But Restricted; Other/Proprietary License · rank 9061 · last release 2026-10-09 · [PyPI](https://pypi.org/project/aspose-slides/) · [docs](https://docs.aspose.com/slides/python-net/)

<details><summary>README extract</summary>

Product Page | Docs | Demos | API Reference | Blog | Search | Free Support | Release Notes | Temporary License

Aspose.Slides for Python via .NET is a powerful on-premise class library used for processing and working with presentations. ...

Example:
```python
import aspose.slides as slides

# Instantiate a Presentation object that represents a presentation file
with slides.Presentation() as presentation:
    slide = presentation.slides[0]
    slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)
    presentation.save("NewPresentation_out.pptx", slides.export.SaveFormat.PPTX)
```

...

</details>

### ipytree

A Tree Widget using jsTree

`pip install ipytree` · installs (wheel) · licence: MIT License · rank 9412 · last release 2022-08-23 · [PyPI](https://pypi.org/project/ipytree/)

### distinctipy

A lightweight package for generating visually distinct colours.

`pip install distinctipy` · installs (wheel) · licence: MIT License · rank 9751 · last release 2024-01-10 · [PyPI](https://pypi.org/project/distinctipy/) · [docs](https://distinctipy.readthedocs.io/)

<details><summary>README extract</summary>

_distinctipy_ is a lightweight python package providing functions to generate
colours that are visually distinct from one another.

Commonly available qualitative colormaps provided by the likes of matplotlib
generally have no more than 20 colours, but for some applications it is useful
to have many more colours that are clearly different from one ...

Example:
```python
import distinctipy

# number of colours to generate
N = 36

# generate N visually distinct colours
colors = distinctipy.get_colors(N)

# display the colours
distinctipy.color_swatch(colors)
```

Sections: Optional Dependencies, Usage and Examples, References, Citing distinctipy

</details>

### highdicom

High-level DICOM abstractions.

`pip install highdicom` · installs (wheel) · licence: MIT · rank 10043 · last release 2026-10-06 · [PyPI](https://pypi.org/project/highdicom/) · [docs](https://highdicom.readthedocs.io/) · [source](https://github.com/ImagingDataCommons/highdicom.git)

<details><summary>README extract</summary>

`highdicom` is a pure Python package built on top of `pydicom` to provide a higher-level application programming interface (API) for working with DICOM files. Its focus is on common operations required for machine learning, computer vision, and other similar computational analyses. Broadly speaking, the package helps with three types of task:

1. ...

Sections: Highdicom, Documentation

</details>

### pyaaf2

A python module for reading and writing advanced authoring format files

`pip install pyaaf2` · installs (wheel) · licence: MIT License · rank 10308 · last release 2023-09-17 · [PyPI](https://pypi.org/project/pyaaf2/) · [docs](http://pyaaf.readthedocs.io) · [source](https://github.com/markreidvfx/pyaaf2)

<details><summary>README extract</summary>

A python module for reading and writing Advanced Authoring Format (AAF) files.
pyaaf2 is a rewrite of pyaaf1 in pure python.

Features:
- Read/Write AAF files
- Modifying existing AAF files inplace
- Embedding DNxHD/DNxHR/WAV media
- Copying objects between files
- Low level read/write Compound File Binary access
- Lazy file reading
- Zero dependencies, does not use AAF SDK

Sections: pyaaf2, Features, Requirements, Documentation, TODO

</details>

### cu2qu

Cubic-to-quadratic bezier curve conversion

`pip install cu2qu` · installs (wheel) · licence: Apache Software License · rank 10428 · last release 2022-11-16 · [PyPI](https://pypi.org/project/cu2qu/)

<details><summary>README extract</summary>

This library provides functions which take in UFO objects (Defcon Fonts
or Robofab RFonts) and converts any cubic curves to quadratic. The most
useful function is probably `fonts_to_quadratic`.

This library is now maintained as part of

</details>

### pypylon

The official Python language binding for the Basler pylon C++ APIs.

`pip install pypylon` · installs (wheel) · licence: Other/Proprietary License · rank 10934 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pypylon/)

<details><summary>README extract</summary>

pypylon is the official Python language binding for the Basler pylon C++ APIs. It enables Python applications to control and acquire images from Basler machine vision products, e.g. cameras. Furthermore, the pylon Data Processing API allows you to perform image processing tasks.

> Note: This README was updated for pypylon 26.6. ...

Example:
```python
from pypylon import pylon

# Create an InstantCamera object with the camera device found first.
# The with statement creates, opens the camera and destroys it automatically.
with pylon.InstantCamera(pylon.FirstFound) as camera:
    print("Using device:", camera.DeviceInfo.ModelName)

...
```

...

</details>

### nglview

IPython widget to interactively view molecular structures and trajectories.

`pip install nglview` · installs from source (sdist only) · licence: MIT License · rank 11001 · last release 2026-02-02 · [PyPI](https://pypi.org/project/nglview/)

<details><summary>README extract</summary>

Citation | Installation | Example | Usage | Command line | API doc | Interface classes | Website | Acknowledgment

An IPython/Jupyter widget to interactively view molecular structures and trajectories. Utilizes the embeddable NGL Viewer for rendering. ...

Example:
```python
import nglview
view = nglview.show_pdbid("3pqr")  # load "3pqr" from RCSB PDB and display viewer widget
view
```

Sections: Notes, notebook user, Example, Showcase from users, Usage, API, API doc, Command line, FAQ, Website, Talks, Projects integrating NGLView

</details>

### puhu

A modern, high-performance image processing library for Python, powered by Rust.

`pip install puhu` · installs (wheel) · licence: MIT License · rank 11242 · last release 2026-05-25 · [PyPI](https://pypi.org/project/puhu/) · [docs](https://bgunebakan.github.io/puhu) · [source](https://github.com/bgunebakan/puhu)

<details><summary>README extract</summary>

A modern, high-performance image processing library for Python, powered by Rust. Puhu provides a Pillow-compatible API while delivering significantly better performance for common image operations.

Features:
- High Performance - Rust-powered for significantly faster operations
- Pillow Compatible - Drop-in replacement for most Pillow operations
- Memory Safe - Built with Rust's memory safety guarantees ...

Example:
```python
import puhu

# Open and process an image
img = puhu.open("photo.jpg")
img = img.resize((800, 600))
img = img.crop((100, 100, 500, 400))
img.save("output.png")

# Drop-in Pillow replacement
from puhu import Image
img = Image.open("photo.jpg")
img = img.resize((400, 300))
img.save("resized.jpg")
```

...

</details>

### gs-madrona

A fork from the official Madrona. The fork will be used for Genesis's own Madrona integration.

`pip install gs-madrona` · installs (wheel) · licence: MIT · rank 11472 · last release 2026-09-23 · [PyPI](https://pypi.org/project/gs-madrona/) · [source](https://github.com/Genesis-Embodied-AI/gs-madrona)

<details><summary>README extract</summary>

It started as a fork of Madrona for the core C++ implementation, created in 2025. Since the fork, substantial modifications have been made to adapt the codebase for Genesis simulator, including:
- Integrating Python interface based on Madrona-MJX and designed for Genesis.
- Adding new features to support the continuous development. ...

Features:
- Support for non-square resolutions
- Shadow rendering in the rasterizer pipeline
- Anti-aliasing support for rasterizer output
- Lighting support (rasterizer and ray tracer) using Genesis-defined light sources ...

Sections: gs-madrona — A Fork of Madrona and Madrona-MJX for Genesis, Scope and Objectives, Features Added Since Fork, Removed Features, Known Limitations, Roadmap / Future Plans, Performance, Pre-requisite, Build from source

</details>

### azureml-pipeline-core

Contains core functionality for Azure Machine Learning pipelines, which are configurable machine learning workflows.

`pip install azureml-pipeline-core` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 11783 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-pipeline-core/)

<details><summary>README extract</summary>

Core functionality to enable azureml-pipeline feature.

</details>

### streamlit-pdf

A Streamlit component for viewing PDF files

`pip install streamlit-pdf` · installs (wheel) · licence: Apache-2.0 · rank 11828 · last release 2026-09-28 · [PyPI](https://pypi.org/project/streamlit-pdf/) · [source](https://github.com/streamlit/streamlit-pdf)

<details><summary>README extract</summary>

A lightweight Streamlit feature that seamlessly displays PDF files in your apps, allowing for simple, responsive, and clean document viewing with minimal effort.

Example:
```python
import streamlit as st

# Display PDF from URL
st.pdf("

# Display with custom height
st.pdf("path/to/document.pdf", height=600)

# Display uploaded file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    st.pdf(uploaded_file)
```

Sections: streamlit-pdf, 💡 Usage, ⚙️ API Reference, `st.pdf(data, height=600)`, Parameters, 🖼️ Examples, Basic PDF Display, File Upload with PDF Display, Custom Height, Reading from Local File

</details>

### an

AI-driven structured animation in Python: scene.md to rendered video.

`pip install an` · installs (wheel) · licence: MIT · rank 12036 · last release 2026-11-03 · [PyPI](https://pypi.org/project/an/) · [docs](https://thorwhalen.github.io/an) · [source](https://github.com/thorwhalen/an)

<details><summary>README extract</summary>

AI-driven structured animation in Python. The user is the director; an AI agent (Claude Opus 4.7) is the assistant orchestrator; existing animation libraries (a custom 2D-cutout runtime, Manim, Remotion) are the executors.

Renamed from `anima` (PyPI conflict). Repo: < ...

Example:
```python
from an import sequence, parallel, tween, delay, flatten

action = sequence(
    tween("charlie/torso", "rotation", to=10.0, duration=1.0),
    delay(0.5),
    tween("charlie/torso", "rotation", to=0.0, duration=1.0),
)
flat = flatten(action)
# [FlatAction(start=0.0, end=1.0, ...), FlatAction(start=1.5, end=2.5, ...)]
```

...

</details>

### webp

Python bindings for WebP

`pip install webp` · installs (wheel) · licence: MIT License · rank 12142 · last release 2024-06-09 · [PyPI](https://pypi.org/project/webp/)

<details><summary>README extract</summary>

Features:
* Picture encoding/decoding
* Animation encoding/decoding
* Automatic memory management
* Simple API for working with `PIL.Image` objects

Example:
```python
import webp
```

Sections: WebP Python bindings, Requirements, Usage, Simple API, Advanced API, Features, Not implemented, Setting up, Running tests, Known issues

</details>

### blendmodes

Use this module to apply a number of blending modes to a background and foreground image

`pip install blendmodes` · installs (wheel) · licence: MIT · rank 12156 · last release 2025-02-20 · [PyPI](https://pypi.org/project/blendmodes/) · [docs](https://github.com/FHPythonUtils/BlendModes/blob/master/README.md) · [source](https://github.com/FHPythonUtils/BlendModes)

<details><summary>README extract</summary>

Use this module to apply a number of blending modes to a background and
foreground image.

Sections: BlendModes, Documentation, Language information, Built for, Chocolatey, Windows - Python.org, Apt, Dnf, Homebrew, MacOS - Python.org, How to run, Windows, Linux/ MacOS, Building

</details>

### django-versatileimagefield

A drop-in replacement for django's ImageField that provides a flexible, intuitive and easily-extensible interface for creating new images from the one assigned to the field.

`pip install django-versatileimagefield` · installs (wheel) · licence: MIT License · rank 12191 · last release 2024-01-21 · [PyPI](https://pypi.org/project/django-versatileimagefield/)

<details><summary>README extract</summary>

A drop-in replacement for django's `ImageField` that provides a flexible, intuitive and easily-extensible interface for creating new images from the one assigned to the field.

Click here for a quick overview of what it is, how it works and whether or not it's the right fit for your project.

 - 3.6
 - 3.7
 - 3.8
 - 3.9 ...

Sections: django-versatileimagefield, Compatibility, Documentation, Code, Running Tests

</details>

### gravis

Interactive graph visualizations with Python and HTML/CSS/JS.

`pip install gravis` · installs (wheel) · licence: Apache Software License · rank 12208 · last release 2021-12-08 · [PyPI](https://pypi.org/project/gravis/)

<details><summary>README extract</summary>

+----------------------+-----------------------------------------------------------------------------------+
 Website |
+----------------------+-----------------------------------------------------------------------------------+
 .. image:: |
 :target: |
 :alt: Hosted on GitHub Pages
 .. ...

</details>

### pyStrich

PyStrich is a fast pure-Python module to generate 1D and 2D barcodes: Code 39, Code 128 (including GS1-128), EAN-13, ITF-14, Data Matrix (including GS1 Data Matrix), QR Code, PDF417 and Aztec Code.

`pip install pyStrich` · installs (wheel) · licence: Apache-2.0 · rank 12460 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pyStrich/) · [docs](https://www.method-b.uk/pyStrich/docs/) · [source](https://github.com/mmulqueen/pyStrich)

<details><summary>README extract</summary>

pyStrich is a fast pure-Python module to generate 1D and 2D barcodes in PNG, SVG and other image formats. Currently it
supports:

 * Code 39 (`code39`)
 * Code 128 and GS1-128 (`code128`)
 * EAN-13 (`ean13`)
 * Interleaved 2 of 5 and ITF-14 (`itf`)
 * Data Matrix and GS1 Data Matrix (`datamatrix`)
 * QR Code (`qrcode`)
 * PDF417 (`pdf417`)
 * ...

</details>

### pykml

Python KML library

`pip install pykml` · installs (wheel) · licence: BSD License · rank 12509 · last release 2019-10-25 · [PyPI](https://pypi.org/project/pykml/)

<details><summary>README extract</summary>

pyKML is a Python package for parsing and authoring KML documents. It is based
on the lxml.objectify API ( which
provides Pythonic access to XML documents.

See the Package Documentation for information on installation and usage.

</details>

### azureml-train-core

Provides estimators for training models.

`pip install azureml-train-core` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 12559 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-train-core/)

<details><summary>README extract</summary>

The azureml-train-core package provides estimators for training models and includes the following:

- Base estimator classes and the generic estimator class in Azure Machine Learning.
- Estimators used in Deep Neural Network (DNN) training.
- Modules and classes supporting hyperparameter tuning.
- Estimator for training with Scikit-Learn. ...

</details>

### otio-fcp-adapter

OpenTimelineIO FCP XML Adapter

`pip install otio-fcp-adapter` · installs (wheel) · licence: Apache Software License · rank 12603 · last release 2023-07-07 · [PyPI](https://pypi.org/project/otio-fcp-adapter/)

<details><summary>README extract</summary>

The `fcp_xml` adapter is part of OpenTimelineIO's core adapter plugins.
It provides reading and writing of Final Cut Pro 7 formatted XML files.
For more information on the FCP XML format please check the links in the
reference section

The following features of OTIO are supported by the `fcp_xml` adapter:

|Feature | Support | ...

Sections: OpenTimelineIO FCP XML Adapter, Adapter Feature Matrix, FCP7 XML References, Contact

</details>

### ovrtx

Omniverse RTX

`pip install ovrtx` · installs from source (sdist only) · licence: LicenseRef-NvidiaProprietary · rank 12846 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ovrtx/) · [docs](https://nvidia-omniverse.github.io/ovrtx/) · [source](https://github.com/NVIDIA-Omniverse/ovrtx)

<details><summary>README extract</summary>

ovrtx is a C and Python library for embedding NVIDIA Omniverse RTX sensor simulation and visualization directly into applications.

It provides real-time, physically accurate camera, lidar, radar, and other sensor simulation for physical AI applications, including robotics learning, synthetic data generation, and industrial and design workflows. ...

Sections: NVIDIA ovrtx, Documentation

</details>

### glyphsLib

A bridge from Glyphs source files (.glyphs) to UFOs

`pip install glyphsLib` · installs (wheel) · licence: Apache Software License · rank 12849 · last release 2026-11-04 · [PyPI](https://pypi.org/project/glyphsLib/)

<details><summary>README extract</summary>

This Python library provides a bridge from Glyphs source files (.glyphs) to
UFOs and Designspace files via defcon and designspaceLib.

The main methods for conversion are found in `init.py`.
Intermediate data can be accessed without actually writing UFOs, if
needed.

The following code will write UFOs and a Designspace file to disk. ...

Example:
```python
import glyphsLib

master_dir = "master_ufos"
ufos, designspace_path = glyphsLib.build_masters("MyFont.glyphs", master_dir)
```

Sections: glyphsLib, Write and return UFOs, Load UFO objects without writing, Read and write Glyphs data as Python objects, Go back and forth between UFOs and Glyphs

</details>

### metafile-render

Render WMF and EMF files to SVG, PNG, JPEG, and WebP

`pip install metafile-render` · installs (wheel) · licence: MIT · rank 13087 · last release 2026-11-02 · [PyPI](https://pypi.org/project/metafile-render/) · [source](https://github.com/myhloli/metafile-render)

<details><summary>README extract</summary>

Windows metafiles, ready for the modern web.

English · 简体中文

Quick start · Usage · Reference

Features:
Metafile Render converts Windows Metafile (WMF) and Enhanced Metafile (EMF)
graphics into SVG, PNG, JPEG, and WebP. Use it to display legacy graphics in a
browser or process metafile images extracted from Office documents. ...

Example:
```python
from pathlib import Path
from metafile_render import render_metafile

result = render_metafile(
    Path("input.emf").read_bytes(),
    output_format="svg",
)
Path("output.svg").write_bytes(result.data)

print(result.width, result.height, result.media_type)
if result.partial:
    print("Partial rendering.")
for item in result.diagnostics:
...
```

Sections: Metafile Render, Overview, Quick start, Usage, Python, Command line, Rendering notes

</details>

### pythreejs

Interactive 3D graphics for the Jupyter Notebook and JupyterLab, using Three.js and Jupyter Widgets.

`pip install pythreejs` · installs (wheel) · licence: BSD License · rank 13112 · last release 2023-02-20 · [PyPI](https://pypi.org/project/pythreejs/)

<details><summary>README extract</summary>

[][binder]
[][pypi]
[][cf]
[][npm]
[][docs]
[][ci]

A Python / ThreeJS bridge for Jupyter Widgets.

![Screencast]

Sections: pythreejs, Troubleshooting, Jupyter Notebook Classic, JupyterLab, Jupyter Lab, Open Source

</details>

### mmdr

Fast native Mermaid diagram rendering (Rust-based, no browser required) with two backends: mermaid-rs-renderer and merman

`pip install mmdr` · installs (wheel) · licence: MIT License · rank 13160 · last release 2026-11-08 · [PyPI](https://pypi.org/project/mmdr/) · [docs](https://mohammadraziei.github.io/mmdr) · [source](https://github.com/mohammadraziei/mmdr)

<details><summary>README extract</summary>

Render Mermaid diagrams to SVG, PNG or raw pixels from Python or the command line.

No browser, no Node.js, no Chromium — `pip install mmdr` is all you need.

Documentation ·
Quick start ·
Benchmarks ·
Changelog

mmdr is a Python package with the Mermaid rendering engines written in Rust and compiled into the wheel. ...

Features:
- Nothing to install besides the wheel. The Rust engines are inside it; the only Python dependency is novasvg, which pip fetches for you.
- Two backends in one package. ...

Example:
```python
import mmdr

d = mmdr.render("flowchart LR; A-->B-->C")
d.save("diagram.svg")
d.save("diagram.png", width=1200, background="#ffffff")
```

Sections: mmdr, Highlights, Quick start, Python, Command line, How it works, Backends, Benchmarks, API and CLI essentials, Requirements

</details>

### meshoptimizer

Python wrapper for meshoptimizer library

`pip install meshoptimizer` · installs from source (sdist only) · licence: MIT License · rank 13243 · last release 2026-02-27 · [PyPI](https://pypi.org/project/meshoptimizer/)

<details><summary>README extract</summary>

Python bindings for the meshoptimizer library, which provides algorithms for optimizing 3D meshes for GPU rendering.

Features:
- Vertex cache optimization
- Overdraw optimization
- Vertex fetch optimization
- Mesh simplification
- Vertex/index buffer compression and decompression
- Zip file storage for encoded meshes
- Numpy array compression and storage
- And more...

Example:
```python
import numpy as np
from meshoptimizer import (
    optimize_vertex_cache,
    optimize_overdraw,
    optimize_vertex_fetch,
    simplify,
    encode_vertex_buffer,
    decode_vertex_buffer,
    encode_index_buffer,
    decode_index_buffer
)

# Create a simple mesh (a cube)
vertices = np.array([
    # positions
    [-0.5, -0.5, -0.5],
...
```

...

</details>

### defcon

A set of flexible objects for representing UFO data.

`pip install defcon` · installs (wheel) · licence: MIT License · rank 13251 · last release 2025-07-16 · [PyPI](https://pypi.org/project/defcon/)

<details><summary>README extract</summary>

Defcon is a set of UFO based objects optimized for use in font editing
applications. The objects are built to be lightweight, fast and
flexible. The objects are very bare-bones and they are not meant to be
end-all, be-all objects. ...

Sections: Defcon, Documentation, Copyrights

</details>

### ufo2ft

A bridge between UFOs and FontTools.

`pip install ufo2ft` · installs (wheel) · licence: MIT · rank 13263 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ufo2ft/)

<details><summary>README extract</summary>

ufo2ft ("UFO to FontTools") is a fork of
ufo2fdk whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

The library provides two functions, `compileOTF` and `compileTTF`,
which work exactly the same way: ...

Features:
If your font's features do not contain kerning/mark/mkmk features,
ufo2ft will create them based on your font's kerning/anchor data.

In addition to
Adobe OpenType feature files,
ufo2ft also supports the
MTI/Monotype format. ...

Example:
```python
from defcon import Font
from ufo2ft import compileOTF

ufo = Font("MyFont-Regular.ufo")
ufo.lib["com.github.googlei18n.ufo2ft.filters"] = [
    {"name": "propagateAnchors", "pre": True, "include": ["a", "b"]}
]
otf = compileOTF(ufo)
otf.save("MyFont-Regular.otf")
```

...

</details>

### exif

Read and modify image EXIF metadata using Python.

`pip install exif` · installs (wheel) · licence: MIT License · rank 13314 · last release 2024-12-10 · [PyPI](https://pypi.org/project/exif/)

<details><summary>README extract</summary>

Read and modify image EXIF metadata using Python without any third-party software
dependencies. For example, batch process image metadata using a Python script.

Example:
```python
>>> from exif import Image
>>> with open('grand_canyon.jpg', 'rb') as image_file:
...     my_image = Image(image_file)
...
>>> my_image.has_exif
True
```

Sections: [exif] Package, Quick Start

</details>

### pillow-simd

Python Imaging Library (fork)

`pip install pillow-simd` · installs from source (sdist only) · licence: MIT-CMU · rank 13324 · last release 2026-09-15 · [PyPI](https://pypi.org/project/pillow-simd/) · [docs](https://pillow.readthedocs.io) · [source](https://github.com/uploadcare/pillow-simd)

<details><summary>README extract</summary>

Pillow-SIMD repo and readme

Pillow-SIMD changelog

Pillow documentation

</details>

### quickchart.io

A client for quickchart.io, a service that generates static chart images

`pip install quickchart.io` · installs (wheel) · licence: MIT License · rank 13421 · last release 2026-06-30 · [PyPI](https://pypi.org/project/quickchart.io/) · [source](https://github.com/typpo/quickchart-python)

<details><summary>README extract</summary>

A Python client for the quickchart.io image charts web service.

Example:
```python
from quickchart import QuickChart

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.config = {
    "type": "bar",
    "data": {
        "labels": ["Hello world", "Test"],
        "datasets": [{
            "label": "Foo",
            "data": [1, 2]
        }]
    }
}
```

Sections: quickchart-python, Usage, Using Javascript functions in your chart, Customizing your chart, config: dict or str, width: int, height: int, format: str, background_color: str, device_pixel_ratio: float, version: str, scheme: str, host: str, key: str

</details>

### djvu-rs

Read, render, and extract text from DjVu files — Python bindings for the pure-Rust djvu-rs library

`pip install djvu-rs` · installs (wheel) · licence: MIT License · rank 13516 · last release 2026-10-16 · [PyPI](https://pypi.org/project/djvu-rs/) · [docs](https://github.com/matyushkin/djvu-rs/blob/main/djvu-py/README.md) · [source](https://github.com/matyushkin/djvu-rs)

<details><summary>README extract</summary>

Read, render, convert, and edit DjVu files from Python. Bindings for the
pure-Rust djvu-rs library: no
DjVuLibre, no GPL, no system dependencies. Rendering and conversion release
the GIL.

| Your task | How | ...

Example:
```python
import djvu_rs as djvu

doc = djvu.Document.open('scan.djvu')
print(f'{doc.page_count()} pages')

page = doc.page(0)
print(f'{page.width}x{page.height} @ {page.dpi} dpi')

page.render(dpi=150).to_pil().save('page.png')   # needs Pillow
text = page.text()                                # None if the page has no text layer

...
```

Sections: djvu-rs for Python, Quick start, Documentation

</details>

### opentype-sanitizer

Python wrapper for the OpenType Sanitizer

`pip install opentype-sanitizer` · installs (wheel) · licence: BSD License · rank 13660 · last release 2024-11-06 · [PyPI](https://pypi.org/project/opentype-sanitizer/)

### k3d

WebGL 3D plotting for Jupyter: meshes, isosurfaces, volumes, voxels and point clouds

`pip install k3d` · installs (wheel) · licence: MIT · rank 13697 · last release 2026-10-05 · [PyPI](https://pypi.org/project/k3d/) · [docs](https://k3d-jupyter.org) · [source](https://github.com/K3D-tools/K3D-jupyter)

<details><summary>README extract</summary>

K3D lets you create 3D plots backed by WebGL with high-level API (surfaces, isosurfaces, voxels,
mesh, point clouds, vtk objects, volume renderer, colormaps, etc). The primary aim of K3D-jupyter is
to be easy to use as a standalone package like matplotlib, but also to allow interoperation with
existing libraries as VTK. K3D can be run as: ...

Sections: K3D Jupyter, Showcase, YouTube, Try it Now!, PyPI, Conda/Anaconda, Google Colab, Source, Kudos

</details>

### ipywebrtc

WebRTC for Jupyter notebook/lab

`pip install ipywebrtc` · installs (wheel) · licence: MIT · rank 13720 · last release 2021-03-29 · [PyPI](https://pypi.org/project/ipywebrtc/)

### otio-cmx3600-adapter

OpenTimelineIO CMX 3600 EDL Adapter

`pip install otio-cmx3600-adapter` · installs (wheel) · licence: Apache Software License · rank 13800 · last release 2023-07-07 · [PyPI](https://pypi.org/project/otio-cmx3600-adapter/)

<details><summary>README extract</summary>

The `cmx_3600` adapter is part of OpenTimelineIO's core adapter plugins.
It provides reading and writing of CMX3600 formatted Edit Decision Lists (EDL).
For more information on the CMX3600 format please check the links in the
reference section

The following features of OTIO are supported by the `cmx_3600` adapter:

|Feature | Support | ...

Example:
```python
try:
    timeline = otio.adapters.read_from_string("mymovie.edl", rate=30)
except EDLParseError:
   print('Log a warning here')
   try:
       timeline = otio.adapters.read_from_string(
           "mymovie.edl",
           rate=30,
           ignore_timecode_mismatch=True)
   except EDLParseError:
       print('Log an error here')
```

...

</details>

### aspose-diagram-python

Aspose.Diagram for Python via .NET is a scalable and feature-rich API to process visio files using Python. API offers Visio file creation, manipulation, conversion and rendering. Developers can format pages to the most granular level, create and manipulate shape, render pages, shapes to PDF and images, and much more - all without any dependency on Microsoft Office or Visio application.

`pip install aspose-diagram-python` · does not install on CPython 3.14 · licence: Free To Use But Restricted; Other/Proprietary License · rank 13809 · last release 2026-10-14 · [PyPI](https://pypi.org/project/aspose-diagram-python/)

<details><summary>README extract</summary>

Product Page Demos Code Samples Temporary License | EULA

Try our free online apps demonstrating some of the most popular Aspose.diagram functionality.

Aspose.Diagram for Python via .Net is a scalable and feature-rich API to process visio files using Python. API offers Visio file creation, manipulation, conversion, rendering. ...

Example:
```python
from aspose.diagram import *
# For complete examples and data files, please go to
# Detect the format of a diagram file
fileFormatInfo = FileFormatUtil.detectFileFormat(test.vsdx")
# Display the file format
print("File Format: " + str(fileFormatInfo))
```

...

</details>

### blend-modes

Image processing blend modes

`pip install blend-modes` · installs (wheel) · licence: MIT License · rank 13818 · last release 2024-10-16 · [PyPI](https://pypi.org/project/blend-modes/)

<details><summary>README extract</summary>

This Python package implements blend modes for images.

The Blend Modes package enables blending different images, or image
layers, by means of blend modes. These modes are commonly found in
graphics programs like Adobe
Photoshop or
GIMP.

Blending through blend modes allows to mix images in a variety of ways. ...

Example:
```python
from PIL import Image
import numpy
from blend_modes import soft_light

# Import background image
background_img_raw = Image.open('background.png')  # RGBA image
background_img = numpy.array(background_img_raw)  # Inputs to blend_modes need to be numpy arrays.
...
```

Sections: Blend Modes, Description, Usage, Input and Output Formats, PIL/Pillow Example, OpenCV Example, Dependencies, See Also

</details>

### booleanOperations

Boolean operations on paths.

`pip install booleanOperations` · installs (wheel) · licence: MIT License · rank 13828 · last release 2026-01-15 · [PyPI](https://pypi.org/project/booleanOperations/)

<details><summary>README extract</summary>

Boolean operations on paths which uses a super fast polygon clipper
library by Angus Johnson.

You can download the latest version from PyPI:

Example:
```python
from booleanOperations import BooleanOperationManager

manager = BooleanOperationManager()
```

Sections: BooleanOperations, BooleanOperationManager, BooleanOperationManager(), manager.union(contours, pointPen), manager.difference(contours, clipContours, pointPen), manager.intersection(contours, clipContours, pointPen), manager.xor(contours, clipContours, pointPen), manager.getIntersections(contours), BooleanGlyph, BooleanGlyph(sourceGlyph), booleanGlyph.union(other), booleanGlyph.difference(other), booleanGlyph.intersection(other), booleanGlyph.xor(other)

</details>

### cffsubr

Standalone CFF subroutinizer based on the AFDKO tx tool

`pip install cffsubr` · installs (wheel) · licence: BSD License · rank 14174 · last release 2025-12-05 · [PyPI](https://pypi.org/project/cffsubr/)

<details><summary>README extract</summary>

Standalone CFF subroutinizer based on the AFDKO tx tool.

</details>

### plutoprint

Paged HTML rendering library

`pip install plutoprint` · installs (wheel) · licence: MIT License · rank 14275 · last release 2026-10-20 · [PyPI](https://pypi.org/project/plutoprint/) · [docs](https://plutoprint.readthedocs.io) · [source](https://github.com/plutoprint/plutoprint)

<details><summary>README extract</summary>

PlutoPrint is a lightweight and easy-to-use Python library for generating high-quality PDFs and images directly from HTML or XML content. It is based on PlutoBook’s robust rendering engine and provides a simple API to convert your HTML into crisp PDF documents or vibrant image files. This makes it ideal for reports, invoices, or visual snapshots.

Example:
```python
import plutoprint

book = plutoprint.Book(plutoprint.PAGE_SIZE_A4)
book.load_url("hello.html")

# Export the entire document to PDF
book.write_to_pdf("hello.pdf")

# Export pages 2 to 15 (inclusive) in order
book.write_to_pdf("hello-range.pdf", 2, 15, 1)

# Export pages 15 to 2 (inclusive) in reverse order
...
```

...

</details>

### fontMath

A set of objects for performing math operations on font data.

`pip install fontMath` · installs (wheel) · licence: MIT License · rank 14362 · last release 2026-02-03 · [PyPI](https://pypi.org/project/fontMath/)

### otio-fcpx-xml-adapter

OpenTimelineIO FCP X XML Adapter

`pip install otio-fcpx-xml-adapter` · installs (wheel) · licence: Apache Software License · rank 14372 · last release 2023-07-07 · [PyPI](https://pypi.org/project/otio-fcpx-xml-adapter/)

<details><summary>README extract</summary>

The `fcpx_xml` adapter is part of OpenTimelineIO's contrib adapter plugins.
It provides reading and writing of Final Cut Pro X formatted XML files.
For more information on the FCP X XML format please check the links in the
reference section

The following features of OTIO are supported by the `fcpx_xml` adapter:

|Feature | Support | ...

Sections: OpenTimelineIO FCP X XML Adapter, Adapter Feature Matrix, FCPX XML References, Contact

</details>

### PyMCubes

Marching cubes for Python

`pip install PyMCubes` · installs from source (sdist only) · licence: BSD License · rank 14467 · last release 2024-07-03 · [PyPI](https://pypi.org/project/PyMCubes/)

### fake-bpy-module-latest

Collection of the fake Blender Python API module for the code completion.

`pip install fake-bpy-module-latest` · installs (wheel) · licence: MIT License · rank 14609 · last release 2026-10-31 · [PyPI](https://pypi.org/project/fake-bpy-module-latest/) · [docs](https://github.com/nutti/fake-bpy-module/blob/main/README.md) · [source](https://github.com/nutti/fake-bpy-module)

<details><summary>README extract</summary>

fake-bpy-module is the collections of the fake Blender Python API modules for
the code completion in commonly used IDEs.

Note: The similar project for Blender Game Engine (BGE) is available on
fake-bge-module which targets
UPBGE. ...

Sections: Fake Blender Python API module collection: fake-bpy-module, Requirements, Generate Modules Manually, Bug report / Feature request / Disscussions, Owner, Reviewer

</details>

### pilgram

library for instagram filters

`pip install pilgram` · installs (wheel) · licence: Apache-2.0 · rank 14757 · last release 2025-11-23 · [PyPI](https://pypi.org/project/pilgram/) · [source](https://github.com/akiomik/pilgram)

<details><summary>README extract</summary>

A python library for instagram filters.

The filter implementations are inspired by CSSgram.

- Python >= 3.10
- Pillow or pillow-simd
- NumPy

Important: This library requires specific Pillow versions for optimal compatibility:

- Pillow >= 10.3.0: Use latest pilgram version for full feature support including `ImageMath.lambda_eval` ...

Example:
```python
from PIL import Image
import pilgram

im = Image.open('sample.jpg')
pilgram.aden(im).save('sample-aden.jpg')
```

Sections: pilgram, Requirements, Pillow Compatibility Notes, Version Selection Guide, Recommended (Latest Pillow), For Older Pillow Versions, Usage, Demo, Filter performance comparison with instagram-filters, Run commands

</details>

### pymetis

A graph partitioning package

`pip install pymetis` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 14887 · last release 2025-11-06 · [PyPI](https://pypi.org/project/pymetis/) · [docs](https://documen.tician.de/pymetis) · [source](https://github.com/inducer/pymetis)

<details><summary>README extract</summary>

PyMetis is a Python wrapper for the Metis graph partitioning software
by George Karypis, Vipin Kumar and others. It includes version 5.1.0 of Metis
and wraps it using the Pybind11
wrapper generator library. ...

Example:
```python
import numpy as np
import pymetis
adjacency_list = [np.array([4, 2, 1]),
                  np.array([0, 2, 3]),
                  np.array([4, 3, 1, 0]),
                  np.array([1, 2, 5, 6]),
                  np.array([0, 2, 5]),
                  np.array([4, 3, 6]),
                  np.array([5, 3])]
...
```

Sections: PyMetis: A Python Wrapper for METIS, Links, Quick Start

</details>

### vulkan

Ultimate Python binding for Vulkan API

`pip install vulkan` · installs (wheel) · licence: Apache Software License · rank 14916 · last release 2024-02-27 · [PyPI](https://pypi.org/project/vulkan/)

### dcc-mcp-core

Foundational library for the DCC Model Context Protocol (MCP) ecosystem

`pip install dcc-mcp-core` · installs (wheel) · licence: MIT License · rank 14924 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dcc-mcp-core/) · [docs](https://dcc-mcp.github.io/dcc-mcp-core/) · [source](https://github.com/dcc-mcp/dcc-mcp-core)

<details><summary>README extract</summary>

中文 | English

Website · Marketplace · Showcase · For Agents · Ecosystem

Skill-first, Rust-powered control plane for a growing creative-tool ecosystem.

dcc-mcp-core connects agents to desktop DCCs, game engines, 2D tools,
production systems, asset providers, profilers, and custom studio hosts through
discoverable MCP and REST capabilities. ...

Features:
- Bundled agent skill. Every checkout and every release ships
 `llms.txt` — a compact index — and
 `llms-full.txt`, the full API reference. ...

...

</details>

### svgutils

Python SVG editor

`pip install svgutils` · installs (wheel) · licence: MIT License · rank 14980 · last release 2021-02-10 · [PyPI](https://pypi.org/project/svgutils/)

<details><summary>README extract</summary>

This is an utility package that helps to edit and
concatenate SVG files. It is especially directed at scientists preparing
final figures for submission to journal. So far it supports arbitrary
placement and scaling of svg figures and
adding markers, such as labels.

</details>

### dcc-mcp-server

Standalone dcc-mcp-server CLI binary — gateway, sidecar, stdio bridge (Rust)

`pip install dcc-mcp-server` · installs (wheel) · licence: MIT License · rank 14986 · last release 2026-11-01 · [PyPI](https://pypi.org/project/dcc-mcp-server/) · [source](https://github.com/dcc-mcp/dcc-mcp-core)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.dcc-mcp/dcc-mcp-core -->

> Status: shipped — the wheel is built by the `build-binaries` job and
> published by `publish-server-pypi` in `.github/workflows/release.yml`. ...

Features:
`dcc-mcp-core` is a PyO3 wheel — its `_core.so` is loaded into the host
Python interpreter (mayapy / blender-python / hython). The sidecar binary,
by contrast, is meant to run as its own OS process; bundling it into
`dcc-mcp-core` would couple two ...

Example:
```python
# In a Maya plugin / Blender addon, after `pip install dcc-mcp-server`:
import os, subprocess
from dcc_mcp_server import binary_path

_proc = subprocess.Popen([
    str(binary_path()),
    "sidecar",
    "--dcc", "maya",
    "--host-rpc", "commandport://127.0.0.1:6000",
    "--watch-pid", str(os.getpid()),
])
```

...

</details>

## Also in this topic

- [weasyprint](internet-www-http.md#weasyprint) - The Awesome Document Factory
- [emoji](internet-www-http.md#emoji) - Emoji for Python
- [svglib](documentation.md#svglib) - A pure-Python library for reading and converting SVG
- [cloudinary](internet-www-http.md#cloudinary) - Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django.
- [pygame](games-entertainment.md#pygame) - Python Game Development
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [moderngl](games-entertainment.md#moderngl) - ModernGL: High performance rendering for Python 3
- [glcontext](games-entertainment.md#glcontext) - Portable Headless OpenGL Context
- [pygame-ce](games-entertainment.md#pygame-ce) - Python Game Development
- [UnityPy](games-entertainment.md#unitypy) - A Unity extraction and patching package
- [sorl-thumbnail](internet-www-http.md#sorl-thumbnail) - Thumbnails for Django, made in the template on first use with Pillow, libvips or ImageMagick, stored on any Django storage
- [borb](artistic-software.md#borb) - borb is a library for reading, creating and manipulating PDF files in python.
- [gallery-dl](internet-www-http.md#gallery-dl) - Command-line program to download image galleries and collections from several image hosting sites
- [gerbonara](artistic-software.md#gerbonara) - Tools to handle Gerber and Excellon files in Python
- [imgui-bundle](artistic-software.md#imgui-bundle) - Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.
- [instaloader](internet.md#instaloader) - Download pictures (or videos) along with their captions and other metadata from Instagram.
- [moderngl-window](games-entertainment.md#moderngl-window) - A cross platform helper library for ModernGL making window creation and resource loading simple
- [scour](internet.md#scour) - Scour SVG Optimizer
- [Panda3D](games-entertainment.md#panda3d) - Panda3D is a framework for 3D rendering and game development for Python and C++ programs.
- [django-markdownx](internet-www-http.md#django-markdownx) - A comprehensive Markdown editor built for Django.
- [taichi](games-entertainment-simulation.md#taichi) - The Taichi Programming Language
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [quadrants](games-entertainment-simulation.md#quadrants) - The Quadrants Programming Language
- [dicomweb-client](internet-www-http-2.md#dicomweb-client) - Client for DICOMweb RESTful services.
- [bithuman](multimedia.md#bithuman) - Real-time talking-avatar SDK: audio in, lip-synced frames out, on your own Mac, Linux or Windows machine.
- [endesive](communications-email.md#endesive) - Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [climage](artistic-software.md#climage) - Convert images to beautiful ANSI escape codes
