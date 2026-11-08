# Scientific/Engineering / Visualization

[Index](README.md) · 36 packages in this topic, 92 more listed under another topic, by downloads.

### matplotlib

Python plotting package

`pip install matplotlib` · installs (wheel) · licence: Python Software Foundation License · rank 172 · last release 2026-09-11 · [PyPI](https://pypi.org/project/matplotlib/) · [docs](https://matplotlib.org) · [source](https://github.com/matplotlib/matplotlib)

<details><summary>README extract</summary>

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in Python.

Check out our home page for more information.

Matplotlib produces publication-quality figures in a variety of hardcopy
formats and interactive environments across platforms. ...

Sections: Contact, Citing Matplotlib

</details>

### plotly

An open-source interactive data visualization library for Python

`pip install plotly` · installs (wheel) · licence: MIT · rank 413 · last release 2026-09-15 · [PyPI](https://pypi.org/project/plotly/) · [docs](https://plotly.com/python/) · [source](https://github.com/plotly/plotly.py)

<details><summary>README extract</summary>

Latest Release

 User forum

 PyPI Downloads

 License

Features:
plotly.py is an interactive, open-source, and browser-based graphing library for Python :sparkles:

Built on top of plotly.js, `plotly.py` is a high-level, declarative charting library. ...

Example:
```python
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()
```

Sections: plotly.py, Quickstart, Overview, Static Image Export

</details>

### graphviz

Simple Python interface for Graphviz

`pip install graphviz` · installs (wheel) · licence: MIT · rank 571 · last release 2025-06-15 · [PyPI](https://pypi.org/project/graphviz/) · [docs](https://graphviz.readthedocs.io)

<details><summary>README extract</summary>

This package facilitates the creation and rendering of graph descriptions in
the DOT language of the Graphviz graph drawing software (upstream repo)
from Python.

Create a graph object, assemble the graph by adding nodes and edges, and
retrieve its DOT source code string. ...

Example:
```python
>>> import graphviz  # doctest: +NO_EXE
>>> dot = graphviz.Digraph(comment='The Round Table')
>>> dot  #doctest: +ELLIPSIS
<graphviz.graphs.Digraph object at 0x...>
```

Sections: Graphviz, Links, Quickstart, See also

</details>

### pydot

Python interface to Graphviz's Dot

`pip install pydot` · installs (wheel) · licence: MIT · rank 854 · last release 2025-06-17 · [PyPI](https://pypi.org/project/pydot/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: 2024 pydot contributors

SPDX-License-Identifier: MIT

`pydot` is a Python interface to Graphviz and its DOT language. You can use `pydot` to create, read, edit, and visualize graphs.

- It's made in pure Python, with only one dependency – pyparsing – other than Graphviz itself. ...

Example:
```python
import pydot

graphs = pydot.graph_from_dot_file("example.dot")
graph = graphs[0]
```

Sections: Pydot, Dependencies, Quickstart, 1. Input, Import a graph from an existing DOT file, Parse a graph from an existing DOT string, Create a graph from scratch using pydot objects, Convert a NetworkX graph to a pydot graph, 2. Edit, 3. Output, Generate an image, Retrieve the DOT string, Convert to a NetworkX graph, More help

</details>

### mizani

Scales for Python

`pip install mizani` · installs (wheel) · licence: BSD License · rank 2801 · last release 2026-09-07 · [PyPI](https://pypi.org/project/mizani/) · [source](https://github.com/has2k1/mizani)

<details><summary>README extract</summary>

Mizani is a scales package for graphics. It is written in Python and is
based on Hadley Wickham's Scales.
See the documentation
for how to use it in a graphics system.

</details>

### plotnine

A Grammar of Graphics for Python

`pip install plotnine` · installs (wheel) · licence: MIT License · rank 2816 · last release 2026-11-03 · [PyPI](https://pypi.org/project/plotnine/) · [source](https://github.com/has2k1/plotnine)

<details><summary>README extract</summary>

plotnine is an implementation of a *grammar of graphics* in Python
based on ggplot2.
The grammar allows you to compose plots by explicitly mapping variables in a
dataframe to the visual characteristics (position, color, size etc.) of objects that make up the plot.

Plotting with a *grammar of graphics* is powerful. ...

Example:
```python
from plotnine import *
from plotnine.data import mtcars
```

Sections: plotnine, Example

</details>

### plotext

plotext plots directly on terminal

`pip install plotext` · installs (wheel) · licence: MIT License · rank 3082 · last release 2026-09-07 · [PyPI](https://pypi.org/project/plotext/)

<details><summary>README extract</summary>

Main features

- `plotext` draws its plots inside the terminal, as colored text, and its installation needs nothing beside itself; only pictures and videos ask for the optional extras.
- Basic plots: scatter, line and stem, each returning a signal you configure and then draw. ...

</details>

### palettable

Color palettes for Python

`pip install palettable` · installs (wheel) · licence: MIT License · rank 3655 · last release 2023-04-19 · [PyPI](https://pypi.org/project/palettable/) · [source](https://github.com/jiffyclub/palettable.git)

<details><summary>README extract</summary>

Palettable (formerly brewer2mpl) is a library of color palettes for Python.
It's written in pure Python with no dependencies, but it can supply color maps
for matplotlib. You can use Palettable to customize matplotlib plots or supply
colors for a web application.

For more information see the
documentation.

Sections: Palettable, Color Palettes for Python

</details>

### adjustText

Iteratively adjust text position in matplotlib plots to minimize overlaps

`pip install adjustText` · installs (wheel) · licence: MIT · rank 3925 · last release 2026-06-08 · [PyPI](https://pypi.org/project/adjustText/) · [docs](https://adjusttext.readthedocs.io/)

<details><summary>README extract</summary>

Inspired by ggrepel package for R/ggplot2 (

Alternative: textalloc

The idea is that often when we want to label multiple points on a graph the text will start heavily overlapping with both other labels and data points. This can be a major problem requiring manual solution. ...

Sections: adjustText - automatic label placement for `matplotlib`, Brief description, Getting started, Documentation, Citing adjustText

</details>

### pyqtgraph

Scientific Graphics and GUI Library for Python

`pip install pyqtgraph` · installs (wheel) · licence: MIT · rank 4384 · last release 2025-11-16 · [PyPI](https://pypi.org/project/pyqtgraph/) · [docs](https://pyqtgraph.readthedocs.io) · [source](https://github.com/pyqtgraph/pyqtgraph)

<details><summary>README extract</summary>

PyQtGraph is a pure-python graphics and GUI library built on PyQt5/PySide2 and
numpy.

It is intended for use in mathematics / scientific / engineering applications.
Despite being written entirely in python, the library is very fast due to its
heavy leverage of numpy for number crunching, Qt's GraphicsView framework for
2D display, and OpenGL for ...

</details>

### plotly-express

Plotly Express - a high level wrapper for Plotly.py

`pip install plotly-express` · installs (wheel) · licence: MIT License · rank 4499 · last release 2019-08-07 · [PyPI](https://pypi.org/project/plotly-express/) · [source](https://github.com/plotly/plotly_express/)

<details><summary>README extract</summary>

Plotly Express is now part of Plotly.py version 4 and so the `plotly_express` module now just re-exports the contents of `plotly.express`

Sections: Plotly Express, Via `pip`, Via `conda`, Getting Help

</details>

### vispy

Interactive visualization in Python

`pip install vispy` · installs (wheel) · licence: BSD-3-Clause · rank 5132 · last release 2026-09-08 · [PyPI](https://pypi.org/project/vispy/)

<details><summary>README extract</summary>

Main website:

VisPy is a **high-performance interactive 2D/3D data visualization
library. VisPy leverages the computational power of modern Graphics
Processing Units (GPUs) through the OpenGL** library to display very
large datasets. Applications of VisPy include:

- High-quality interactive scientific plots with millions of points. ...

Sections: VisPy: interactive scientific visualization in Python, Announcements, Using VisPy, Structure of VisPy, Governance, Genesis, External links

</details>

### matplotlib-venn

Functions for plotting area-proportional two- and three-way Venn diagrams in matplotlib.

`pip install matplotlib-venn` · installs from source (sdist only) · licence: MIT License · rank 5795 · last release 2025-02-25 · [PyPI](https://pypi.org/project/matplotlib-venn/)

<details><summary>README extract</summary>

Routines for plotting area-weighted two- and three-circle venn diagrams.

Example:
```python
venn2(subsets = (3, 2, 1))
```

Sections: Venn diagram plotting routines for Python/Matplotlib, Dependencies, Usage, Tuning the diagram layout, Questions, See also

</details>

### pydotplus

Python interface to Graphviz's Dot language

`pip install pydotplus` · installs from source (sdist only) · licence: MIT License · rank 5814 · last release 2014-12-09 · [PyPI](https://pypi.org/project/pydotplus/)

<details><summary>README extract</summary>

PyDotPlus is an improved version of the old pydot project that provides a
Python Interface to Graphviz's Dot language.

Differences with pydot:

- Compatible with PyParsing 2.0+.
- Python 2.7 - Python 3 compatible.
- Well documented.
- CI Tested.

Sections: PyDotPlus - Python interface to Graphviz's Dot language, About, Documentation, Requirements

</details>

### vegafusion

Core tools for using VegaFusion from Python

`pip install vegafusion` · installs (wheel) · licence: BSD License · rank 6020 · last release 2025-09-29 · [PyPI](https://pypi.org/project/vegafusion/) · [docs](https://vegafusion.io) · [source](https://github.com/hex-inc/vegafusion)

<details><summary>README extract</summary>

This crate contains the Python library that embeds the VegaFusion Runtime and select Connection. This crate uses PyO3 to expose the Rust logic to CPython.

</details>

### yellowbrick

A suite of visual analysis and diagnostic tools for machine learning.

`pip install yellowbrick` · installs (wheel) · licence: Apache Software License · rank 6929 · last release 2022-08-21 · [PyPI](https://pypi.org/project/yellowbrick/) · [docs](http://scikit-yb.org/) · [source](https://github.com/DistrictDataLabs/yellowbrick)

<details><summary>README extract</summary>

Yellowbrick is a suite of visual analysis and diagnostic tools designed to facilitate machine learning with scikit-learn. The library implements a new core API object, the `Visualizer` that is an scikit-learn estimator &mdash; an object that learns from data. ...

Features:
- Manifold Visualization: high-dimensional visualization with manifold learning
- Parallel Coordinates: horizontal visualization of instances
- PCA Projection: projection of instances based on principal components ...

Sections: Yellowbrick, Visualizers, Classification Visualization, Clustering Visualization, Feature Visualization, Model Selection Visualization, Regression Visualization, Target Visualization, Text Visualization, Affiliations

</details>

### pytest-mpl

pytest plugin to help with testing figures output from Matplotlib

`pip install pytest-mpl` · installs (wheel) · licence: BSD-2-Clause · rank 7122 · last release 2026-03-25 · [PyPI](https://pypi.org/project/pytest-mpl/)

<details><summary>README extract</summary>

`pytest-mpl` is a pytest plugin to facilitate image comparison for Matplotlib figures.

For each figure to test, an image is generated and then subtracted from an existing reference image.
If the RMS of the residual is larger than a user-specified tolerance, the test will fail. ...

Example:
```python
import matplotlib.pyplot as plt
import pytest

@pytest.mark.mpl_image_compare
def test_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2])
    return fig
```

Sections: `pytest-mpl`, Usage

</details>

### scikit-plot

An intuitive library to add plotting functionality to scikit-learn objects.

`pip install scikit-plot` · installs (wheel) · licence: MIT License · rank 7418 · last release 2018-08-19 · [PyPI](https://pypi.org/project/scikit-plot/)

<details><summary>README extract</summary>

Example:
```python
# The usual train-test split mumbo-jumbo
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
nb = GaussianNB()
nb.fit(X_train, y_train)
...
```

Sections: Welcome to Scikit-plot, Single line functions for detailed visualizations, The quickest and easiest way to go from analysis..., ...to this., Okay then, prove it. Show us an example., Documentation and Examples, Citing Scikit-plot, APA, IEEE, ACM

</details>

### mjviser

Web-based MuJoCo viewer powered by viser.

`pip install mjviser` · installs (wheel) · licence: Apache-2.0 · rank 8019 · last release 2026-10-31 · [PyPI](https://pypi.org/project/mjviser/) · [source](https://github.com/mujocolab/mjviser)

<details><summary>README extract</summary>

A web-based MuJoCo viewer built on Viser.

Example:
```python
import mujoco
from mjviser import Viewer

model = mujoco.MjModel.from_xml_path("robot.xml")
data = mujoco.MjData(model)
Viewer(model, data).run()
```

Sections: mjviser, Quick start, Python API, Extension points, Mouse and keyboard, Examples

</details>

### textual-plotext

A Textual widget wrapper for the Plotext plotting library

`pip install textual-plotext` · installs (wheel) · licence: MIT License · rank 8547 · last release 2024-11-30 · [PyPI](https://pypi.org/project/textual-plotext/) · [source](https://github.com/Textualize/textual-plotext)

<details><summary>README extract</summary>

A Textual widget wrapper for the Plotext plotting
library.

The library makes one widget available: `PlotextPlot`. This widget provides
a `plt` property, which should be used where you would normally use `plt` as
seen in the Plotext documentation.

Let's take the first
example
from the Plotext README: ...

Example:
```python
import plotext as plt
y = plt.sin() # sinusoidal test signal
plt.scatter(y)
plt.title("Scatter Plot") # to apply a title
plt.show() # to finally plot
```

Sections: textual-plotext, Introduction, Longer example, What functions are no-ops?, Themes, Known issues, Need more help?

</details>

### matplotlib-fontja

matplotlibを日本語表示に対応させます。

`pip install matplotlib-fontja` · installs (wheel) · licence: MIT AND IPA · rank 8656 · last release 2025-04-24 · [PyPI](https://pypi.org/project/matplotlib-fontja/) · [source](https://github.com/ciffelia/matplotlib-fontja.git)

<details><summary>README extract</summary>

matplotlibを日本語表示に対応させます。

uehara1414さんのjapanize-matplotlibをフォークし、Python 3.12以降でも動作するよう修正したものです。変更点の詳細についてはCHANGELOGをお読みください。

matplotlibをimportした後、matplotlib_fontjaをimportします。

Example:
```python
import matplotlib.pyplot as plt
import matplotlib_fontja

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()
```

Sections: matplotlib-fontja, 利用方法, インストール, 動作確認環境, 利用フォント, FAQ, `import matplotlib_fontja`したのに日本語が表示されません, IPAexゴシック以外のフォントを使いたいです

</details>

### matplotlib-scalebar

Artist for matplotlib to display a scale bar

`pip install matplotlib-scalebar` · installs (wheel) · licence: BSD License · rank 9324 · last release 2025-01-17 · [PyPI](https://pypi.org/project/matplotlib-scalebar/) · [source](https://github.com/ppinard/matplotlib-scalebar)

<details><summary>README extract</summary>

Documentation: See below

Source Code:

Cheat sheet:

Provides a new artist for matplotlib to display a scale bar, aka micron bar.
It is particularly useful when displaying calibrated images plotted using
`plt.imshow(...)`.

The artist supports customization either directly from the ScaleBar object or from the matplotlibrc.

Example:
```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar

# Load image
with cbook.get_sample_data("s1045.ima.gz") as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))

# Create subplot
fig, ax = plt.subplots()
ax.axis("off")

# Plot image
...
```

...

</details>

### plotille

Plot in the terminal using braille dots.

`pip install plotille` · installs (wheel) · licence: MIT · rank 10226 · last release 2026-02-17 · [PyPI](https://pypi.org/project/plotille/) · [source](https://github.com/tammoippen/plotille)

<details><summary>README extract</summary>

Plots, scatter plots, histograms and heatmaps in the terminal using braille dots, and foreground and background colors - with no dependencies. Make complex figures using the Figure class or make fast and simple plots using graphing function - similar to a very small sibling to matplotlib. Or use the canvas to plot dots, lines and images yourself. ...

Example:
```python
In [1]: import plotille
In [2]: import numpy as np
In [3]: X = np.sort(np.random.normal(size=1000))
```

...

</details>

### SciencePlots

Format Matplotlib for scientific plotting

`pip install SciencePlots` · installs (wheel) · licence: MIT · rank 10514 · last release 2026-06-23 · [PyPI](https://pypi.org/project/SciencePlots/) · [docs](https://github.com/garrettj403/SciencePlots/wiki) · [source](https://github.com/garrettj403/SciencePlots)

<details><summary>README extract</summary>

PyPI version

 conda-forge version

 DOI

> Warning
> : As of version 2.0.0, you need to add `import scienceplots` before setting the style (`plt.style.use('science')`).

*Matplotlib styles for scientific figures*

This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses. ...

Example:
```python
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')
```

</details>

### UpSetPlot

Draw Lex et al.'s UpSet plots with Pandas and Matplotlib

`pip install UpSetPlot` · installs from source (sdist only) · licence: BSD License · rank 11471 · last release 2023-12-31 · [PyPI](https://pypi.org/project/UpSetPlot/)

<details><summary>README extract</summary>

This is another Python implementation of UpSet plots by Lex et al. [Lex2014]_.
UpSet plots are used to visualise set overlaps; like Venn diagrams but
more readable. Documentation is at

This `upsetplot` library tries to provide a simple interface backed by an
extensible, object-oriented design. ...

Features:
Probably for petty reasons. It appeared py-upset was not being maintained. Its
input format was undocumented, inefficient and, IMO, inappropriate. ...

Example:
```python
>>> from upsetplot import generate_counts
>>> example = generate_counts()
>>> example
cat0   cat1   cat2
False  False  False      56
              True      283
       True   False    1279
              True     5882
True   False  False      24
              True       90
       True   False     429
...

</details>

### trame-pyvista

Trame interface for PyVista

`pip install trame-pyvista` · installs (wheel) · licence: MIT · rank 11559 · last release 2026-11-03 · [PyPI](https://pypi.org/project/trame-pyvista/) · [source](https://github.com/pyvista/trame-pyvista)

<details><summary>README extract</summary>

Trame interface for PyVista. Provides web-based 3D
viewers, Jupyter backends, scene exporters, and a Sphinx directive for
embedding interactive plots in docs.

This package was extracted from the `pyvista.trame` subpackage so the
trame stack can release on its own cadence. ...

Example:
```python
import pyvista as pv

pv.set_jupyter_backend('trame')
pl = pv.Plotter()
pl.add_mesh(pv.Wavelet())
pl.show()
```

Sections: trame-pyvista, What you get, Usage

</details>

### basemap-data

Data assets for matplotlib basemap

`pip install basemap-data` · installs (wheel) · licence: LGPL-3.0-or-later · rank 12442 · last release 2025-06-13 · [PyPI](https://pypi.org/project/basemap-data/) · [docs](https://matplotlib.org/basemap) · [source](https://github.com/matplotlib/basemap.git)

_README extract left out: share-alike licence._

### pydot-ng

Python interface to Graphviz's Dot

`pip install pydot-ng` · installs (wheel) · licence: MIT License · rank 12540 · last release 2018-10-16 · [PyPI](https://pypi.org/project/pydot-ng/)

<details><summary>README extract</summary>

Ero Carrera (c) 2004-2007

ero@dkbza.org

This code is distributed under the MIT license.

pyparsing: pydot requires the pyparsing module in order to be
 able to load DOT files.

GraphViz: is needed in order to render the graphs into any of
 the plethora of output formats supported.

Sections: pydot - Python interface to Graphviz's Dot language, Requirements

</details>

### basemap

Plot data on map projections with matplotlib

`pip install basemap` · does not install on CPython 3.14 · licence: MIT · rank 12699 · last release 2025-06-13 · [PyPI](https://pypi.org/project/basemap/) · [docs](https://matplotlib.org/basemap) · [source](https://github.com/matplotlib/basemap.git)

<details><summary>README extract</summary>

Plot on map projections (with coastlines and political boundaries) using
[`matplotlib`].

Sections: basemap, Requirements, Documentation, Contact, Thanks, Known bugs

</details>

### streamlit-drawable-canvas

A Streamlit custom component for a free drawing canvas using Fabric.js.

`pip install streamlit-drawable-canvas` · installs (wheel) · licence: MIT · rank 12770 · last release 2026-09-04 · [PyPI](https://pypi.org/project/streamlit-drawable-canvas/) · [source](https://github.com/andfanilo/streamlit-drawable-canvas)

<details><summary>README extract</summary>

This project is best effort. Every now and then I'll add something I need myself and let a coding agent do most of the typing, but I don't have the time to go through bigger issues or pull requests. If there's a larger feature you want, fork away! ...

Features:
- Draw freely, lines, circles, boxes and polygons on the canvas, with options on stroke & fill
- Rotate, skew, scale, move any object of the canvas on demand
- Select a background color or image to draw on ...

Example:
```python
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "polygon", "text")
)

...

</details>

### sweetviz

A pandas-based library to visualize and compare datasets.

`pip install sweetviz` · installs (wheel) · licence: MIT · rank 13542 · last release 2026-04-11 · [PyPI](https://pypi.org/project/sweetviz/)

<details><summary>README extract</summary>

_In-depth EDA (target analysis, comparison, feature analysis, correlation) in two lines of code!_

Sweetviz is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA (Exploratory Data Analysis) with just two lines of code. Output is a fully self-contained HTML application. ...

Features:
- Target analysis
 - Shows how a target value (e.g. "Survived" in the Titanic dataset) relates to other features
- Visualize and compare
 - Distinct datasets (e.g. training vs test data)
 - Intra-set characteristics (e.g. male versus female) ...

Example:
```python
import sweetviz as sv

my_report = sv.analyze(my_dataframe)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"
```

...

</details>

### brewer2mpl

Connect colorbrewer2.org color maps to Python and matplotlib

`pip install brewer2mpl` · installs (wheel) · licence: MIT License · rank 13588 · last release 2014-09-19 · [PyPI](https://pypi.org/project/brewer2mpl/)

<details><summary>README extract</summary>

brewer2mpl is now Palettable!
brewer2mpl will no longer be updated, but will stay available here
for the foreseeable future.

brewer2mpl is a pure Python package for accessing
colorbrewer2.org color maps from Python.
With brewer2mpl you can get the raw RGB colors of all 165
colorbrewer2.org color maps. ...

Example:
```python
brewer2mpl.print_maps()
```

Sections: brewer2mpl, NOTICE, Color Maps, Examples, Listing Color Maps, Get a Color Map, `BrewerMap` Objects, Direct Access

</details>

### dash-bootstrap-templates

A collection of Plotly figure templates with a Bootstrap theme

`pip install dash-bootstrap-templates` · installs (wheel) · licence: MIT License · rank 14067 · last release 2026-09-30 · [PyPI](https://pypi.org/project/dash-bootstrap-templates/)

<details><summary>README extract</summary>

`dash-bootstrap-templates` library provides:

- 54 Bootstrap themed Plotly figure templates
 - You will find Plotly templates in light and dark mode for each of the 26 Bootstrap/Bootswatch themes available in the Dash Bootstrap Components Library.
 - As of 2.1.0, there are also figure templates based on the Vizro theme. ...

Example:
```python
"""
A sample of 8 of the 26 Bootstrap themed Plotly figure templates available
in the dash-bootstrap-template library

"""
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px

df = px.data.gapminder()

templates = [
    "bootstrap",
...
```

...

</details>

### dclab

Library for real-time deformability cytometry (RT-DC)

`pip install dclab` · installs (wheel) · licence: GPL-2.0-or-later · rank 14113 · last release 2026-11-06 · [PyPI](https://pypi.org/project/dclab/) · [docs](https://dclab.readthedocs.io/en/stable/) · [source](https://github.com/DC-Analysis/dclab)

_README extract left out: share-alike licence._

### textcharts

Beautiful ASCII charts for your terminal — bar, histogram, heatmap, box plot, and 11 more chart types with zero dependencies

`pip install textcharts` · installs (wheel) · licence: MIT · rank 14302 · last release 2026-09-17 · [PyPI](https://pypi.org/project/textcharts/) · [docs](https://joeharris76.github.io/textcharts/) · [source](https://github.com/joeharris76/textcharts)

<details><summary>README extract</summary>

Beautiful text based charts for your terminal — zero dependencies.

15 chart types with Unicode box-drawing, ANSI colors, and automatic terminal
width detection. Pure Python, no external dependencies, Python 3.10+.

`textcharts` was extracted from the
BenchBox project so the terminal
charting layer could be used as a standalone library. ...

Features:
- Zero dependencies — pure Python, stdlib only
- 15 chart types — from simple bars to heatmaps and CDF curves
- Terminal-aware — auto-detects width, color support, and Unicode capability ...

Example:
```python
from textcharts import BoxPlot, BoxPlotSeries

downtown = [1825, 1900, 1980, 2100, 2250, 2400, 2550, 2710, 2980]
riverside = [1450, 1525, 1600, 1680, 1750, 1820, 1950, 2080, 2220]
...

</details>

### lets-plot

An open source library for statistical plotting

`pip install lets-plot` · installs (wheel) · licence: MIT · rank 14685 · last release 2026-06-30 · [PyPI](https://pypi.org/project/lets-plot/) · [docs](https://lets-plot.org) · [source](https://github.com/JetBrains/lets-plot)

<details><summary>README extract</summary>

Lets-Plot is a multiplatform plotting library built on the principles of the Grammar of Graphics.

The library design is heavily influenced by Leland Wilkinson's work The Grammar of Graphics describing the deep features that underlie all statistical graphics. ...

Sections: Lets-Plot, Grammar of Graphics for Python, Grammar of Graphics for Kotlin, Notebooks, Compose Multiplatform, JVM and Kotlin/JS, Documentation, "Lets-Plot in SciView" plugin, Recent Updates in the Gallery

</details>

## Also in this topic

- [contourpy](scientific-engineering-information-analysis.md#contourpy) - Python library for calculating contours of 2D quadrilateral grids
- [seaborn](multimedia-graphics.md#seaborn) - Statistical data visualization
- [streamlit](database-front-ends.md#streamlit) - A faster way to build and share data apps
- [leather](multimedia-graphics.md#leather) - Python charting for 80% of humans.
- [altgraph](scientific-engineering-mathematics.md#altgraph) - Python graph (network) package
- [dash](database-front-ends.md#dash) - A Python framework for building reactive web-apps. Developed by Plotly.
- [bokeh](office-business.md#bokeh) - Interactive plots and applications in the browser from Python
- [gradio](scientific-engineering.md#gradio) - Python library for easily interacting with trained machine learning models
- [glfw](multimedia-graphics.md#glfw) - A ctypes-based wrapper for GLFW3.
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [folium](scientific-engineering-gis.md#folium) - Make beautiful maps with Leaflet.js & Python
- [open3d](education.md#open3d) - Open3D: A Modern Library for 3D Data Processing.
- [pyquaternion](scientific-engineering-mathematics.md#pyquaternion) - A fully featured, pythonic library for representing and using quaternions.
- [anndata](scientific-engineering-bio-informatics.md#anndata) - Annotated data.
- [rerun-sdk](scientific-engineering-artificial-intelligence.md#rerun-sdk) - The Rerun Logging SDK
- [svgpathtools](multimedia-graphics.md#svgpathtools) - A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves.
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [panel](office-business.md#panel) - The powerful data exploration & web app framework for Python.
- [scanpy](scientific-engineering-bio-informatics.md#scanpy) - Single-Cell Analysis in Python.
- [Cartopy](scientific-engineering.md#cartopy) - A Python library for cartographic visualizations with Matplotlib
- [moderngl](games-entertainment.md#moderngl) - ModernGL: High performance rendering for Python 3
- [glcontext](games-entertainment.md#glcontext) - Portable Headless OpenGL Context
- [weave](database-front-ends.md#weave) - A toolkit for building composable interactive data driven applications.
- [great-tables](internet-www-http.md#great-tables) - Easily generate information-rich, publication-quality tables from Python.
- [pygraphviz](scientific-engineering-information-analysis.md#pygraphviz) - Python interface to Graphviz
- [dash-cytoscape](database-front-ends.md#dash-cytoscape) - A Component Library for Dash aimed at facilitating network visualization in Python, wrapped around Cytoscape.js
- [earthengine-api](multimedia-graphics.md#earthengine-api) - Earth Engine Python API
- [osmnx](scientific-engineering-gis.md#osmnx) - Download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [datashader](scientific-engineering.md#datashader) - Data visualization toolchain based on aggregating into a grid
- [mplfinance](office-business-financial.md#mplfinance) - Utilities for the visualization, and visual analysis, of financial data
- [pytools](scientific-engineering.md#pytools) - A collection of tools for Python
- [pbixray](scientific-engineering-information-analysis.md#pbixray) - A Python library to parse and analyze PBIX files used with Microsoft Power BI and Excel PowerPivot.
- [eralchemy](database.md#eralchemy) - Simple entity relation (ER) diagrams generation
- [vedo](scientific-engineering-medical-science-apps.md#vedo) - A python module for scientific visualization, analysis of 3D objects and point clouds.
- [ovito](scientific-engineering-chemistry.md#ovito) - A scientific data visualization and analysis software for particle-based simulations
- [pyvista-cad](multimedia-graphics.md#pyvista-cad) - PyVista accessor and reader-registry plugin for CAD formats (STEP, IGES, BREP, DXF, 3MF, IFC, FCStd) and bridges to build123d, cadquery, and OCP.
- [skia-python](multimedia-graphics.md#skia-python) - Skia python binding
- [py3Dmol](scientific-engineering-bio-informatics.md#py3dmol) - An IPython interface for embedding 3Dmol.js views in Jupyter notebooks
- [healpy](scientific-engineering-astronomy.md#healpy) - Healpix tools package for Python
- [imgui-bundle](artistic-software.md#imgui-bundle) - Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.
- [pytransform3d](scientific-engineering-mathematics.md#pytransform3d) - 3D transformations for Python
- [moderngl-window](games-entertainment.md#moderngl-window) - A cross platform helper library for ModernGL making window creation and resource loading simple
- [backtesting](office-business-financial.md#backtesting) - Backtest trading strategies in Python
- [fiftyone-brain](scientific-engineering-artificial-intelligence.md#fiftyone-brain) - FiftyOne Brain
- [gradio-rangeslider](scientific-engineering.md#gradio-rangeslider) - 🛝 Slider component for selecting a range of values
- [fiftyone-db](scientific-engineering-artificial-intelligence.md#fiftyone-db) - FiftyOne DB
- [voxel51-eta](scientific-engineering-artificial-intelligence.md#voxel51-eta) - Extensible Toolkit for Analytics
- [airium](database-front-ends.md#airium) - Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [openTSNE](scientific-engineering.md#opentsne) - Extensible, parallel implementations of t-SNE
- [apache-superset-core](database.md#apache-superset-core) - Core Python package for building Apache Superset backend extensions and integrations
- [fiftyone](scientific-engineering-artificial-intelligence.md#fiftyone) - FiftyOne: the open-source tool for building high-quality datasets and computer vision models
- [distinctipy](multimedia-graphics.md#distinctipy) - A lightweight package for generating visually distinct colours.
- [h2o-wave](communications-chat.md#h2o-wave) - Python driver for H2O Wave Realtime Apps
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [pysplashsurf](scientific-engineering.md#pysplashsurf) - Python bindings for splashsurf, a surface reconstruction library for SPH simulations.
- [ete3](scientific-engineering-bio-informatics.md#ete3) - A Python Environment for (phylogenetic) Tree Exploration
- [arcgis](internet-www-http.md#arcgis) - ArcGIS API for Python
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [geomdl](scientific-engineering-mathematics.md#geomdl) - Object-oriented B-Spline and NURBS evaluation library
- [swanlab](scientific-engineering.md#swanlab) - Python library for streamlined tracking and management of AI training processes.
- [uniplot](scientific-engineering.md#uniplot) - Lightweight plotting to the terminal. 4x resolution via Unicode.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [napari](scientific-engineering.md#napari) - n-dimensional array viewer in Python
- [networkit](scientific-engineering-bio-informatics.md#networkit) - NetworKit is a toolbox for high-performance network analysis
- [pycuda](scientific-engineering-2.md#pycuda) - Python wrapper for Nvidia CUDA
- [nglview](multimedia-graphics.md#nglview) - IPython widget to interactively view molecular structures and trajectories.
- [quadrilateral-fitter](scientific-engineering-artificial-intelligence.md#quadrilateral-fitter) - QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.
- [islpy](scientific-engineering-2.md#islpy) - Wrapper around isl, an integer set library
- [kerykeion](religion.md#kerykeion) - A Python library for astrological calculations, including natal charts, houses, planetary aspects, and SVG chart generation.
- [fabio](scientific-engineering-bio-informatics.md#fabio) - FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python
- [gravis](multimedia-graphics.md#gravis) - Interactive graph visualizations with Python and HTML/CSS/JS.
- [ridgeplot](scientific-engineering-2.md#ridgeplot) - Beautiful ridgeline plots in python
- [st-theme](database-front-ends.md#st-theme) - A component that returns the active theme of the Streamlit app.
- [pykml](multimedia-graphics.md#pykml) - Python KML library
- [netron](scientific-engineering-2.md#netron) - Viewer for neural network, deep learning and machine learning models.
- [dash-auth](database-front-ends.md#dash-auth) - Dash Authorization Package.
- [highcharts-core](internet-www-http-2.md#highcharts-core) - High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).
- [lttb](office-business-financial.md#lttb) - Largest-Triangle-Three-Buckets algorithm for downsampling time series-like data
- [ipymarkup](scientific-engineering-artificial-intelligence.md#ipymarkup) - NER, syntax tree markup visualisations for Jupyter Notebook
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [squidpy](scientific-engineering-bio-informatics.md#squidpy) - Spatial Single Cell Analysis in Python
- [k3d](multimedia-graphics.md#k3d) - WebGL 3D plotting for Jupyter: meshes, isosurfaces, volumes, voxels and point clouds
- [qctrl-client](internet-www-http-2.md#qctrl-client) - Q-CTRL Client
- [milsymbol](scientific-engineering-gis.md#milsymbol) - Military symbols (MIL-STD-2525 / STANAG APP-6) in Python — port of milsymbol.js
- [dimos-viewer](scientific-engineering-2.md#dimos-viewer) - Interactive Rerun viewer for DimOS with click-to-navigate support
- [gradio-pdf](scientific-engineering-2.md#gradio-pdf) - Easily display PDFs in Gradio
- [open3d-cpu](education.md#open3d-cpu) - Open3D: A Modern Library for 3D Data Processing.
- [pymetis](multimedia-graphics.md#pymetis) - A graph partitioning package
- [svgutils](multimedia-graphics.md#svgutils) - Python SVG editor
