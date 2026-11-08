# Scientific/Engineering / GIS

[Index](README.md) · 71 packages in this topic, 19 more listed under another topic, by downloads.

### shapely

Manipulation and analysis of geometric objects

`pip install shapely` · installs (wheel) · licence: BSD-3-Clause · rank 352 · last release 2026-10-07 · [PyPI](https://pypi.org/project/shapely/) · [docs](https://shapely.readthedocs.io/) · [source](https://github.com/shapely/shapely)

<details><summary>README extract</summary>

Manipulation and analysis of geometric objects in the Cartesian plane.

Shapely is a BSD-licensed Python package for manipulation and analysis of
planar geometric objects. It is using the widely deployed open-source
geometry library GEOS (the engine of PostGIS, and a port of JTS). ...

Example:
```python
>>> from shapely import Point
>>> patch = Point(0.0, 0.0).buffer(10.0)
>>> patch
<POLYGON ((10 0, 9.952 -0.98, 9.808 -1.951, 9.569 -2.903, 9.239 -3.827, 8.81...>
>>> patch.area
313.6548490545941
```

Sections: Shapely, What is a ufunc?, Multithreading, Usage, Requirements, Integration

</details>

### geopandas

Geographic pandas extensions

`pip install geopandas` · installs (wheel) · licence: BSD-3-Clause · rank 976 · last release 2026-09-28 · [PyPI](https://pypi.org/project/geopandas/) · [source](https://github.com/geopandas/geopandas)

<details><summary>README extract</summary>

GeoPandas is a project to add support for geographic data to
pandas objects.

The goal of GeoPandas is to make working with geospatial data in
python easier. It combines the capabilities of pandas and shapely,
providing geospatial operations in pandas and a high-level interface
to multiple geometries to shapely. ...

</details>

### h3

Uber's hierarchical hexagonal geospatial indexing system

`pip install h3` · installs (wheel) · licence: Apache Software License · rank 981 · last release 2026-05-30 · [PyPI](https://pypi.org/project/h3/) · [docs](https://uber.github.io/h3-py/)

<details><summary>README extract</summary>

Python bindings for the H3 core library.

- Documentation: uber.github.io/h3-py
- GitHub repo: github.com/uber/h3-py

Example:
```python
>>> import h3
>>> lat, lng = 37.769377, -122.388903
>>> resolution = 9
>>> h3.latlng_to_cell(lat, lng, resolution)
'89283082e73ffff'
```

Sections: Usage, APIs, Example gallery, Versioning

</details>

### pyogrio

Vectorized spatial vector file format I/O using GDAL/OGR

`pip install pyogrio` · installs (wheel) · licence: MIT License · rank 1021 · last release 2026-06-26 · [PyPI](https://pypi.org/project/pyogrio/) · [source](https://github.com/geopandas/pyogrio)

<details><summary>README extract</summary>

Pyogrio provides fast, bulk-oriented read and write access to
GDAL/OGR vector data
sources, such as ESRI Shapefile, GeoPackage, GeoJSON, and several others.
Vector data sources typically have geometries, such as points, lines, or
polygons, and associated records with potentially many columns worth of data. ...

Sections: Requirements, Getting started

</details>

### geographiclib

The geodesic routines from GeographicLib

`pip install geographiclib` · installs (wheel) · licence: MIT · rank 1108 · last release 2025-08-21 · [PyPI](https://pypi.org/project/geographiclib/) · [docs](https://geographiclib.sourceforge.io/Python/doc/) · [source](https://github.com/geographiclib/geographiclib-python)

<details><summary>README extract</summary>

This is a library to solve geodesic problems on an ellipsoid model of
the earth.

Licensed under the MIT/X11 License; see
LICENSE.txt.

The algorithms are documented in

* C. F. F. Karney,
 Algorithms for geodesics,
 J. Geodesy 87(1), 43–55 (2013);
 Addenda.

The documentation for this package is in

</details>

### geopy

Python Geocoding Toolbox

`pip install geopy` · installs (wheel) · licence: MIT License · rank 1112 · last release 2026-07-12 · [PyPI](https://pypi.org/project/geopy/) · [docs](https://geopy.readthedocs.io) · [source](https://github.com/geopy/geopy)

<details><summary>README extract</summary>

geopy is a Python client for several popular geocoding web
services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources. ...

Example:
```python
>>> from geopy.geocoders import Nominatim
>>> geolocator = Nominatim(user_agent="specify_your_app_name_here")
>>> location = geolocator.geocode("175 5th Avenue NYC")
>>> print(location.address)
Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
>>> print((location.latitude, location.longitude))
...
```

Sections: geopy, Geocoding, Measuring Distance, Documentation

</details>

### pyshp

Pure Python read/write support for ESRI Shapefile format

`pip install pyshp` · installs (wheel) · licence: MIT · rank 1768 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pyshp/) · [source](https://github.com/GeospatialPython/pyshp)

<details><summary>README extract</summary>

The Python Shapefile Library (PyShp) reads and writes ESRI Shapefiles in pure Python.

- Author: Joel Lawhead
- Maintainers: James Parrott & Karim Bahgat
- Version: 3.1.7
- Date: 7th Nov 2026
- License: MIT

Features:
The Python Shapefile Library (PyShp) provides read and write support for the
Esri Shapefile format. The Shapefile format is a popular Geographic
Information System vector data format created by Esri. ...

Example:
```python
with open("{}.prj".format(filename), "w") as prj:
    wkt = 'GEOGCS["WGS 84",'
    wkt += 'DATUM["WGS_1984",'
    wkt += 'SPHEROID["WGS 84",6378137,298.257223563]]'
    wkt += ',PRIMEM["Greenwich",0],'
    wkt += 'UNIT["degree",0.0174532925199433]]'
    prj.write(wkt)
```

...

</details>

### GeoAlchemy2

Using SQLAlchemy with Spatial Databases

`pip install GeoAlchemy2` · installs (wheel) · licence: MIT · rank 1791 · last release 2026-11-04 · [PyPI](https://pypi.org/project/GeoAlchemy2/) · [source](https://github.com/geoalchemy/geoalchemy2)

<details><summary>README extract</summary>

GeoAlchemy 2 is a Python toolkit for working with spatial databases. It is
based on the gorgeous SQLAlchemy.

Documentation is on Read the Docs:

</details>

### geomet

Pure Python conversion library for common geospatial data formats

`pip install geomet` · installs (wheel) · licence: Apache Software License · rank 1921 · last release 2023-11-14 · [PyPI](https://pypi.org/project/geomet/) · [source](https://github.com/geomet/geomet)

<details><summary>README extract</summary>

Pure-Python conversion library for common geospatial data formats.
Supported formats include:
- GeoJSON
- WKT/WKB (Well-Known Text/Binary)
- Extended WKB/WKT
- GeoPackage Binary

Sections: GeoMet, Functionality, Example usage, Limitations, See also

</details>

### fiona

Fiona reads and writes spatial data files

`pip install fiona` · installs from source (sdist only) · licence: BSD License · rank 2304 · last release 2024-09-16 · [PyPI](https://pypi.org/project/fiona/) · [docs](https://fiona.readthedocs.io/) · [source](https://github.com/Toblerity/Fiona)

<details><summary>README extract</summary>

Fiona streams simple feature data to and from GIS formats like GeoPackage and
Shapefile.

Fiona can read and write real-world data using multi-layered GIS formats,
zipped and in-memory virtual file systems, from files on your hard drive or in
cloud storage. This project includes Python modules and a command line
interface (CLI). ...

Example:
```python
import fiona
from fiona import Feature, Geometry
from shapely.geometry import mapping, shape

# Open a file for reading. We'll call this the source.
with fiona.open(
    "zip+
) as src:

    # The file we'll write to must be initialized with a coordinate
    # system, a format driver name, and a record schema. We can get
...
```

...

</details>

### tzfpy

Probably the fastest Python package to convert longitude/latitude to timezone name

`pip install tzfpy` · installs (wheel) · licence: MIT · rank 2378 · last release 2026-11-01 · [PyPI](https://pypi.org/project/tzfpy/) · [docs](https://github.com/ringsaturn/tzfpy) · [source](https://github.com/ringsaturn/tzfpy)

<details><summary>README extract</summary>

> [!NOTE]
> 0. It's probably the fastest Python package to convert longitude/latitude to
> timezone name.
> 1. This package uses simplified polygon data. The error around borders is
> small and bounded: every simplified boundary stays within about 111 m of
> the full-precision border. See Accuracy for measured numbers.
> 2. ...

Example:
```python
>>> from tzfpy import get_tz, get_tzs
>>> get_tz(116.3883, 39.9289)  # in (longitude, latitude) order.
'Asia/Shanghai'
>>> get_tzs(87.4160, 44.0400)  # in (longitude, latitude) order.
['Asia/Shanghai', 'Asia/Urumqi']
```

Sections: tzfpy, -, Changes in 2.0, Breaking changes, Usage, Export to GeoJSON, Best practices, Accuracy, Full-precision wheels, Performance, Memory, Background, Compare with other packages

</details>

### geojson

Python bindings and utilities for GeoJSON

`pip install geojson` · installs (wheel) · licence: BSD License · rank 2388 · last release 2026-05-28 · [PyPI](https://pypi.org/project/geojson/)

<details><summary>README extract</summary>

This Python library contains:

- Functions for encoding and decoding GeoJSON formatted data
- Classes for all GeoJSON Objects
- An implementation of the Python geo_interface Specification

Table of Contents

Features:
Visualize the results of the examples above here. General information about Feature can be found in Section 3.2 within The GeoJSON Format Specification.

Example:
```python
>>> from geojson import Point

>>> Point((-115.81, 37.24))  # doctest: +ELLIPSIS
{"coordinates": [-115.8..., 37.2...], "type": "Point"}
```

Sections: geojson, GeoJSON Objects, Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection, Feature, FeatureCollection, GeoJSON encoding/decoding, Custom classes, Default and custom precision

</details>

### haversine

Calculate the distance between 2 points on Earth.

`pip install haversine` · installs (wheel) · licence: MIT License · rank 2453 · last release 2024-11-28 · [PyPI](https://pypi.org/project/haversine/)

<details><summary>README extract</summary>

Calculate the distance (in various units) between two points on Earth using their latitude and longitude.

Example:
```python
from haversine import inverse_haversine, Direction
from math import pi
paris = (48.8567, 2.3508) # (lat, lon)
# Finding 32 km west of Paris
inverse_haversine(paris, 32, Direction.WEST)
# returns tuple (48.85587279023947, 1.9134085092836945)
# Finding 32 km southwest of Paris
inverse_haversine(paris, 32, pi * 1.25)
...
```

Sections: Haversine, Usage, Calculate the distance between Lyon and Paris, Note for radians and degrees, Inverse Haversine Formula, Example: Finding arbitary point from Paris, Combine matrix

</details>

### folium

Make beautiful maps with Leaflet.js & Python

`pip install folium` · installs (wheel) · licence: MIT License · rank 2715 · last release 2025-06-16 · [PyPI](https://pypi.org/project/folium/)

<details><summary>README extract</summary>

`folium` builds on the data wrangling strengths of the Python ecosystem and the
mapping strengths of the Leaflet.js library. Manipulate your data in Python,
then visualize it in a Leaflet map via `folium`.

Sections: folium, Python Data, Leaflet.js Maps, Documentation, Packages and plugins

</details>

### laspy

Native Python ASPRS LAS read/write library

`pip install laspy` · installs (wheel) · licence: BSD-2-Clause · rank 3233 · last release 2026-01-14 · [PyPI](https://pypi.org/project/laspy/)

<details><summary>README extract</summary>

Laspy is a python library for reading, modifying and creating LAS LiDAR
files.

Laspy is compatible with Python 3.8+.

Features:
- LAS support.
- LAZ support via `lazrs` or `laszip` backend.
- LAS/LAZ streamed/chunked reading/writting.
- [COPC] support over files.
- [COPC] support over https with `requests` package.
- CRS support via `pyproj` package.

Example:
```python
import laspy

las = laspy.read('filename.las')
las.points = las.points[las.classification == 2]
las.write('ground.laz')
```

Sections: Laspy, Features, Examples

</details>

### mercantile

Web mercator XYZ tile utilities

`pip install mercantile` · installs (wheel) · licence: BSD License · rank 3590 · last release 2021-04-21 · [PyPI](https://pypi.org/project/mercantile/)

<details><summary>README extract</summary>

Spherical mercator coordinate and tile utilities

Documentation:

The mercantile module provides `ul(xtile, ytile, zoom)` and `bounds(xtile,
ytile, zoom)` functions that respectively return the upper left corner and
bounding longitudes and latitudes for XYZ tiles, a `xy(lng, lat)` function
that returns spherical mercator x and y coordinates, a ...

Example:
```python
>>> import mercantile
>>> mercantile.ul(486, 332, 10)
LngLat(lng=-9.140625, lat=53.33087298301705)
>>> mercantile.bounds(486, 332, 10)
LngLatBbox(west=-9.140625, south=53.12040528310657, east=-8.7890625, north=53.33087298301705)
>>> mercantile.xy(*mercantile.ul(486, 332, 10))
(-1017529.7205322663, 7044436.526761846)
...
```

Sections: Mercantile, Mercantile CLI, See Also

</details>

### geojson-pydantic

Pydantic data models for the GeoJSON spec.

`pip install geojson-pydantic` · installs (wheel) · licence: MIT License · rank 3707 · last release 2026-09-21 · [PyPI](https://pypi.org/project/geojson-pydantic/) · [source](https://github.com/developmentseed/geojson-pydantic)

<details><summary>README extract</summary>

Pydantic models for GeoJSON.

Documentation:

Source Code:

`geojson_pydantic` provides a suite of Pydantic models matching the GeoJSON specification rfc7946. Those models can be used for creating or validating geojson data.

Sections: geojson-pydantic, Description, Changes

</details>

### morecantile

Construct and use map tile grids (a.k.a TileMatrixSet / TMS).

`pip install morecantile` · installs (wheel) · licence: MIT License · rank 4303 · last release 2026-09-16 · [PyPI](https://pypi.org/project/morecantile/) · [docs](https://developmentseed.org/morecantile/) · [source](https://github.com/developmentseed/morecantile)

<details><summary>README extract</summary>

Construct and use map tile grids (a.k.a TileMatrixSet / TMS).

Documentation:

Source Code:

Morecantile is like mercantile (the best tool to work with Web Mercator tile indexes), but with support for other TileMatrixSet grids.

Morecantile follows the OGC Two Dimensional Tile Matrix Set specification 2.0 found in ...

Example:
```python
import morecantile

tms = morecantile.tms.get("WebMercatorQuad")

# Get TMS bounding box
print(tms.xy_bbox)
>>> BoundingBox(
    left=-20037508.342789244,
    bottom=-20037508.34278919,
    right=20037508.34278919,
    top=20037508.342789244,
)

# Get the bounds for tile Z=4, X=10, Y=10 in the TMS's CRS (e.g epsg:3857)
...
```

Sections: Morecantile, Usage, Defaults Grids, Implementations, Changes

</details>

### utm

Bidirectional UTM-WGS84 converter for python

`pip install utm` · installs (wheel) · licence: MIT License · rank 4348 · last release 2026-07-27 · [PyPI](https://pypi.org/project/utm/)

<details><summary>README extract</summary>

Bidirectional UTM-WGS84 converter for python

Example:
```python
>>> import utm
```

Sections: utm, Usage, Latitude/Longitude to UTM, UTM to Latitude/Longitude, Speed

</details>

### countryinfo

A Python module for returning data about countries, ISO info, and states/provinces within them.

`pip install countryinfo` · installs (wheel) · licence: MIT License · rank 4383 · last release 2026-03-07 · [PyPI](https://pypi.org/project/countryinfo/) · [source](https://github.com/porimol/countryinfo)

<details><summary>README extract</summary>

A lightweight Python library for accessing comprehensive country data — including ISO codes, states/provinces, capital cities, currencies, languages, and other geographic information.

Example:
```python
from countryinfo import CountryInfo

country = CountryInfo("Singapore")
print(country.capital())      # Singapore
print(country.iso(2))         # SG
print(country.population())   # 5469700
print(country.neighbors())    # [] — island, no land borders
```

Sections: Countryinfo, Quick Start, Constructor, API Reference, Country lookup, .info(), .name(), .iso(), .alt_spellings(), .area(), .borders(), .neighbors(), .calling_codes(), .capital()

</details>

### pymap3d

pure Python (no prereqs) coordinate conversions, following convention of several popular Matlab routines.

`pip install pymap3d` · installs (wheel) · licence: BSD License · rank 4418 · last release 2025-07-08 · [PyPI](https://pypi.org/project/pymap3d/)

<details><summary>README extract</summary>

Pure Python (no prerequistes beyond Python itself) 3-D geographic coordinate conversions and geodesy.
Function syntax is roughly similar to Matlab Mapping Toolbox.
PyMap3D is intended for non-interactive use on massively parallel (HPC) and embedded systems.

API docs

Thanks to our contributors.

* Matlab, GNU Octave
* Fortran
* Rust
* C++ ...

Example:
```python
import pymap3d as pm

x,y,z = pm.geodetic2ecef(lat,lon,alt)

az,el,range = pm.geodetic2aer(lat, lon, alt, observer_lat, observer_lon, 0)
```

Sections: Python 3-D coordinate conversions, Similar toolboxes in other code languages, Prerequisites, Usage, Functions, Ellipsoid, array vs scalar, Caveats, Compare to Matlab Mapping and Aerospace Toolbox, Notes, AstroPy.Units.Quantity

</details>

### mgrs

MGRS coordinate conversion for Python

`pip install mgrs` · installs (wheel) · licence: BSD License · rank 4429 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mgrs/) · [source](https://github.com/hobuinc/mgrs/)

<details><summary>README extract</summary>

This package exposes scalar and batch GeoTrans conversions through
a pybind11 extension. The Rust translation of GEOTRANS 3.10 is linked
statically into that extension; no separate libmgrs shared library or runtime
Python dependencies are needed. The C++ binding preserves the Python API;
all coordinate conversion runs in Rust. ...

Example:
```python
>>> import mgrs

>>> latitude = 42.0
>>> longitude = -93.0

>>> m = mgrs.MGRS()
>>> c = m.toMGRS(latitude, longitude)
>>> c
'15TWG0000049776'

>>> lat, lon = m.toLatLon(c)
>>> '%.5f, %.5f' % (lat, lon)
'42.00000, -92.99999'

>>> y = '321942.29N'
>>> yd = m.dmstodd(y)
>>> '%.5f' % yd
'32.32841'

>>> d, m, s = m.ddtodms(32.328414)
...
```

...

</details>

### rioxarray

geospatial xarray extension powered by rasterio

`pip install rioxarray` · installs (wheel) · licence: Apache-2.0 · rank 4439 · last release 2026-10-29 · [PyPI](https://pypi.org/project/rioxarray/) · [docs](https://vylor.github.io/rioxarray/) · [source](https://github.com/vylor/rioxarray)

<details><summary>README extract</summary>

rasterio xarray extension.

Sections: rioxarray README, Documentation, Bugs/Questions

</details>

### osmium

Python bindings for libosmium, the data processing library for OSM data

`pip install osmium` · installs (wheel) · licence: BSD License · rank 4642 · last release 2026-10-18 · [PyPI](https://pypi.org/project/osmium/) · [docs](https://docs.osmcode.org/pyosmium/latest/) · [source](https://github.com/osmcode/pyosmium)

<details><summary>README extract</summary>

This library provides Python bindings for the Libosmium C++
library, a library for working with OpenStreetMap data in a fast and flexible
manner.

Sections: pyosmium, Documentation, Examples, Fineprint

</details>

### opencage

Wrapper module for the OpenCage Geocoder API

`pip install opencage` · installs (wheel) · licence: BSD-3-Clause · rank 4732 · last release 2026-10-28 · [PyPI](https://pypi.org/project/opencage/) · [source](https://github.com/OpenCageData/python-opencage-geocoder)

<details><summary>README extract</summary>

A Python module to access the OpenCage Geocoding API.

Example:
```python
from opencage.geocoder import OpenCageGeocode
```

Sections: OpenCage Geocoding Module for Python, Tutorials, Working with AI / Agent Skill, Usage, Reverse geocoding, Sessions, Asyncronous requests, Non-SSL API use, Exceptions, Command-line batch geocoding, Who is OpenCage GmbH?

</details>

### simplekml

A Simple KML creator

`pip install simplekml` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5173 · last release 2021-09-16 · [PyPI](https://pypi.org/project/simplekml/)

_README extract left out: share-alike licence._

### pystac-client

Python library for searching SpatioTemporal Asset Catalog (STAC) APIs.

`pip install pystac-client` · installs (wheel) · licence: Apache Software License · rank 5407 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pystac-client/) · [docs](https://pystac-client.readthedocs.io) · [source](https://github.com/stac-utils/pystac-client.git)

<details><summary>README extract</summary>

A Python client for working with STAC APIs.

Sections: pystac-client, Documentation

</details>

### rio-tiler

User friendly Rasterio plugin to read raster datasets.

`pip install rio-tiler` · installs (wheel) · licence: BSD License · rank 5418 · last release 2026-11-02 · [PyPI](https://pypi.org/project/rio-tiler/) · [docs](https://cogeotiff.github.io/rio-tiler/) · [source](https://github.com/cogeotiff/rio-tiler)

<details><summary>README extract</summary>

User friendly Rasterio plugin to read raster datasets.

Documentation:

Source Code:

`rio-tiler` was initially designed to create slippy map
tiles from large raster data
sources and render these tiles dynamically on a web map. ...

Features:
- Read any dataset supported by GDAL/Rasterio

- User friendly `tile`, `part`, `feature`, `point` reading methods

- Enable property assignment (e.g nodata) on data reading

- STAC support

- Xarray support (>=4.0) ...

Example:
```python
from rio_tiler.io import Reader

with Reader("my.tif") as image:
    print(image.dataset)  # rasterio opened dataset
    img = image.read()    # similar to rasterio.open("my.tif").read() but returns a rio_tiler.models.ImageData object
```

...

</details>

### mapclassify

Classification Schemes for Choropleth Maps.

`pip install mapclassify` · installs (wheel) · licence: BSD License · rank 5746 · last release 2026-08-11 · [PyPI](https://pypi.org/project/mapclassify/) · [source](https://github.com/pysal/mapclassify)

<details><summary>README extract</summary>

`mapclassify` implements a family of classification schemes for choropleth maps.
Its focus is on the determination of the number of classes, and the assignment
of observations to those classes. It is intended for use with upstream mapping
and geovisualization packages (see geopandas and geoplot)
that handle the rendering of the maps. ...

</details>

### osmnx

Download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap

`pip install osmnx` · installs (wheel) · licence: MIT · rank 5858 · last release 2026-07-21 · [PyPI](https://pypi.org/project/osmnx/) · [docs](https://osmnx.readthedocs.io)

<details><summary>README extract</summary>

OSMnx is a Python package to easily download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap. You can download and model walking, driving, or biking networks with a single line of code then analyze and visualize them. ...

Sections: OSMnx, Getting Started

</details>

### pygeodesy

Pure Python geodesy tools

`pip install pygeodesy` · installs (wheel) · licence: MIT License · rank 6148 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pygeodesy/)

<details><summary>README extract</summary>

A pure Python implementation of `geodesy` tools for various ellipsoidal and spherical earth models using precision exact, elliptic, trigonometric, vector-based, iterative and approximate methods for geodetic (lat-/longitude), geocentric (ECEF cartesian), local (LTP) and certain triaxial ellipsoidal coordinates. ...

Sections: PyGeodesy, Dependencies, Documentation, Tests, Notes

</details>

### descartes

Use geometric objects as matplotlib paths and patches

`pip install descartes` · installs (wheel) · licence: BSD License · rank 6175 · last release 2017-01-17 · [PyPI](https://pypi.org/project/descartes/)

<details><summary>README extract</summary>

Use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches

Requires: matplotlib, numpy, and optionally Shapely 1.2+.

Example:
See also: examples/patches.py.

Descartes is not associated with the identically named and apparently defunct
project at

Example:
```python
from matplotlib import pyplot
from shapely.geometry import LineString
from descartes import PolygonPatch

BLUE = '#6699cc'
GRAY = '#999999'

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)

line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

...
```

</details>

### rio-cogeo

Cloud Optimized GeoTIFF (COGEO) creation plugin for rasterio

`pip install rio-cogeo` · installs (wheel) · licence: BSD License · rank 6473 · last release 2026-10-09 · [PyPI](https://pypi.org/project/rio-cogeo/) · [docs](https://cogeotiff.github.io/rio-cogeo/) · [source](https://github.com/cogeotiff/rio-cogeo)

<details><summary>README extract</summary>

Cloud Optimized GeoTIFF (COG) creation and validation plugin for Rasterio.

Documentation:

Source Code:

This plugin aims to facilitate the creation and validation of Cloud Optimized
GeoTIFF (COG or COGEO). While it respects the
COG specifications, this plugin also
enforces several features: ...

Sections: rio-cogeo, Cloud Optimized GeoTIFF, GDAL Version, More, Changes

</details>

### libpysal

Core components of PySAL - A library of spatial analysis functions

`pip install libpysal` · installs (wheel) · licence: BSD License · rank 6509 · last release 2026-10-22 · [PyPI](https://pypi.org/project/libpysal/) · [source](https://github.com/pysal/libpysal)

<details><summary>README extract</summary>

libpysal offers five modules that form the building blocks in many upstream packages
in the PySAL family:

- `libpysal.cg` – Computational geometry
- `libpysal.examples` – Built-in example datasets
- `libpysal.graph` – Graph class encoding spatial weights matrices
- `libpysal.io` – Input and output
- `libpysal.weights` – Spatial weights (legacy)

Sections: libpysal: Python Spatial Analysis Library Core, Introduction, Documentation, Citing libpysal

</details>

### simplification

Fast linestring simplification using RDP or Visvalingam-Whyatt

`pip install simplification` · installs (wheel) · licence: BlueOak-1.0.0 · rank 6582 · last release 2026-10-11 · [PyPI](https://pypi.org/project/simplification/) · [docs](https://github.com/urschrei/simplification#readme) · [source](https://github.com/urschrei/simplification)

<details><summary>README extract</summary>

Simplify a LineString using the Ramer–Douglas–Peucker or Visvalingam-Whyatt algorithms

Example:
```python
from simplification.cutil import (
    simplify_coords,
    simplify_coords_idx,
    simplify_coords_vw,
    simplify_coords_vw_idx,
    simplify_coords_vwp,
)

# Using Ramer–Douglas–Peucker
coords = [
    [0.0, 0.0],
    [5.0, 4.0],
    [11.0, 5.5],
    [17.3, 3.2],
    [27.8, 0.1]
]

...
```

Sections: Simplification, Building SDist and Wheels, Usage, But I only want the simplified Indices, But I Want to Simplify Polylines, How it Works, Is It Fast, What does that mean, Disclaimer, Citing `Simplification`

</details>

### titiler-core

A modern dynamic tile server built on top of FastAPI and Rasterio/GDAL.

`pip install titiler-core` · installs (wheel) · licence: MIT License · rank 6721 · last release 2026-09-21 · [PyPI](https://pypi.org/project/titiler-core/) · [docs](https://developmentseed.org/titiler/) · [source](https://github.com/developmentseed/titiler)

<details><summary>README extract</summary>

Core of Titiler's application. Contains blocks to create dynamic tile servers.

Example:
```python
from fastapi import FastAPI
from titiler.core.factory import TilerFactory

# Create a FastAPI application
app = FastAPI(
    description="A lightweight Cloud Optimized GeoTIFF tile server",
)

# Create a set of COG endpoints
cog = TilerFactory()

# Register the COG endpoints to the application
...
```

Sections: titiler.core, How To, Package structure

</details>

### pygeoif

A basic implementation of the __geo_interface__

`pip install pygeoif` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6763 · last release 2025-10-01 · [PyPI](https://pypi.org/project/pygeoif/) · [docs](https://pygeoif.readthedocs.io/)

_README extract left out: share-alike licence._

### GDAL

GDAL: Geospatial Data Abstraction Library

`pip install GDAL` · installs from source (sdist only) · licence: MIT · rank 6793 · last release 2026-08-18 · [PyPI](https://pypi.org/project/GDAL/) · [docs](https://gdal.org) · [source](https://github.com/OSGeo/GDAL.git)

<details><summary>README extract</summary>

This Python package and extensions are a number of tools for programming and
manipulating the GDAL Geospatial Data Abstraction Library.
Generally speaking the classes and methods mostly
match those of the GDAL and OGR C++ classes.

A basic starting point is the Vector API Tutorial.
For full documentation, see the GDAL Python API. ...

Example:
```python
python3 -c 'from osgeo import gdal_array'
```

Sections: GDAL/OGR in Python, Building from source, Dependencies, Building when building the rest of GDAL, Building just the bindings, from the full tree, Building from the PyPi module file, General, pip, Conda, Usage, Imports, API, Numpy, Tutorials

</details>

### pynmeagps

NMEA protocol parser and generator

`pip install pynmeagps` · installs (wheel) · licence: BSD-3-Clause · rank 7539 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pynmeagps/) · [docs](https://www.semuconsulting.com/pynmeagps/) · [source](https://github.com/semuconsulting/pynmeagps)

<details><summary>README extract</summary>

Current Status |
Installation |
Reading |
Parsing |
Generating |
Serializing |
Utilities |
Examples |
Extensibility |
Command Line Utility |
Graphical Client |
Author & License

`pynmeagps` is an original Python 3 parser aimed *primarily* at the subset of the NMEA 0183 © v4 protocol relevant to GNSS/GPS receivers. ...

Example:
```python
class pynmeagps.nmeareader.NMEAReader(stream, **kwargs)
```

Sections: pynmeagps, Reading (Streaming), Parsing, Generating, Serializing, Utility Methods, Examples, Extensibility, Command Line Utility, Graphical Client

</details>

### owslib

OGC Web Service utility library

`pip install owslib` · installs (wheel) · licence: BSD-3-Clause · rank 7568 · last release 2026-06-04 · [PyPI](https://pypi.org/project/owslib/) · [docs](https://geopython.github.io/OWSLib) · [source](https://github.com/geopython/OWSLib)

<details><summary>README extract</summary>

Features:
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their
related content models.

Full documentation is available at ...

Example:
```python
>>> from owslib.wms import WebMapService
>>> wms = WebMapService(' version='1.1.1')
>>> wms.identification.type
'OGC:WMS'
>>> wms.identification.version
'1.1.1'
>>> wms.identification.title
'JPL Global Imagery Service'
>>> wms.identification.abstract
'WMS Server maintained by JPL, worldwide satellite imagery.'

Available layers::

...
```

Sections: OWSLib, Overview, Requirements, Dependencies, Running

</details>

### rasterstats

Summarize geospatial raster datasets based on vector geometries

`pip install rasterstats` · installs (wheel) · licence: BSD License · rank 7794 · last release 2026-05-23 · [PyPI](https://pypi.org/project/rasterstats/) · [docs](https://pythonhosted.org/rasterstats/) · [source](https://github.com/perrygeo/python-rasterstats)

<details><summary>README extract</summary>

`rasterstats` is a Python module for summarizing geospatial raster datasets based on vector geometries.
It includes functions for zonal statistics and interpolated point queries. The command-line interface allows for
easy interoperability with other GeoJSON tools.

For details on installation and usage, visit the documentation at ...

Example:
```python
>>> from rasterstats import zonal_stats
>>> stats = zonal_stats("tests/data/polygons.shp", "tests/data/slope.tif")
>>> stats[0].keys()
dict_keys(['min', 'max', 'mean', 'count'])
>>> [f['mean'] for f in stats]
[14.660084635416666, 56.60576171875]
```

Sections: rasterstats, Documentation, What does it do?, Command Line Quick Start, Python Quick Start, Issues

</details>

### fastkml

Fast KML processing in python

`pip install fastkml` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 7853 · last release 2025-11-04 · [PyPI](https://pypi.org/project/fastkml/) · [docs](https://fastkml.readthedocs.org/)

_README extract left out: share-alike licence._

### odc-geo

Geometry Classes and Operations (opendatacube)

`pip install odc-geo` · installs (wheel) · licence: Apache Software License · rank 8008 · last release 2026-11-02 · [PyPI](https://pypi.org/project/odc-geo/) · [docs](https://odc-geo.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

This library combines geometry shape classes from shapely with CRS from pyproj to provide
projection aware `Geometry`. It exposes all the functionality provided by `shapely` modules, but
will refuse operations between geometries defined in different projections. Geometries can be
brought into a common projection with `Geometry.to_crs` method. ...

Sections: odc.geo, Origins

</details>

### esda

Exploratory Spatial Data Analysis in PySAL

`pip install esda` · installs (wheel) · licence: BSD License · rank 8628 · last release 2026-06-19 · [PyPI](https://pypi.org/project/esda/) · [source](https://github.com/pysal/esda)

### pynmea2

Python library for the NMEA 0183 protcol

`pip install pynmea2` · installs (wheel) · licence: MIT License · rank 10135 · last release 2023-01-19 · [PyPI](https://pypi.org/project/pynmea2/)

### quantized-mesh-tile

Quantized-Mesh format reader and writer

`pip install quantized-mesh-tile` · installs (wheel) · licence: MIT License · rank 10136 · last release 2026-02-05 · [PyPI](https://pypi.org/project/quantized-mesh-tile/)

<details><summary>README extract</summary>

Quantized-mesh-tile is a Python encoder/decoder and topology builder for terrain tiles.

Doc is hosted on Readthedocs:

Sections: quantized-mesh-tile, Test Doc Locally

</details>

### odc-stac

Tooling for converting STAC metadata to ODC data model

`pip install odc-stac` · installs (wheel) · licence: not stated · rank 10529 · last release 2026-07-30 · [PyPI](https://pypi.org/project/odc-stac/) · [docs](https://odc-stac.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Load STAC items into `xarray` Datasets. Process locally or distribute data
loading and computation with Dask.

Example:
```python
catalog = pystac_client.Client.open(...)
query = catalog.search(...)
xx = odc.stac.load(
    query.items(),
    bands=["red", "green", "blue"],
)
xx.red.plot.imshow(col="time")
```

Sections: odc.stac, Usage, odc.stac.load, Using pip, Using Conda

</details>

### shapely-polyskel

Implementation of the straight skeleton algorithm as described by Felkel and Obdržálek in their 1998 conference paper Straight skeleton implementation.

`pip install shapely-polyskel` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 10594 · last release 2025-01-05 · [PyPI](https://pypi.org/project/shapely-polyskel/) · [source](https://github.com/vec2pt/shapely-polyskel.git)

_README extract left out: share-alike licence._

### osm2geojson

Parse OSM and Overpass JSON

`pip install osm2geojson` · installs (wheel) · licence: MIT · rank 10695 · last release 2026-03-04 · [PyPI](https://pypi.org/project/osm2geojson/) · [source](https://github.com/aspectumapp/osm2geojson)

<details><summary>README extract</summary>

<!-- -->

Parse OSM and Overpass JSON/XML to GeoJSON with Python.

This library is under development!

Example:
```python
import osm2geojson

# From Overpass JSON
geojson = osm2geojson.json2geojson(overpass_json)

# From OSM/Overpass XML
geojson = osm2geojson.xml2geojson(osm_xml)

# To Shape objects (Shapely geometries + properties)
shapes = osm2geojson.json2shapes(overpass_json)
shapes = osm2geojson.xml2shapes(osm_xml)
```

Sections: osm2geojson, Usage, Python API, Command-Line Interface, API Reference, Main Functions, `json2geojson(data, **options)`, `xml2geojson(xml_str, **options)`, `json2shapes(data, **options)`, `xml2shapes(xml_str, **options)`, Options, Helper Functions, `overpass_call(query)`, `shape_to_feature(shape_obj, properties)`

</details>

### lat-lon-parser

Simple parser for latitude-longitude strings

`pip install lat-lon-parser` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 11052 · last release 2024-11-13 · [PyPI](https://pypi.org/project/lat-lon-parser/)

<details><summary>README extract</summary>

Code for parsing lat-long coordinates in "various" formats, and for converting between lat-long formats (e.g. decimal degrees to degrees-minutes-seconds)

Note: perhaps it would be better to integrate this with a more full featured lib like: ...

Example:
```python
In [12]: from lat_lon_parser import parse

In [13]: parse("45° 12.6' W")
Out[13]: -45.21
```

Sections: lat_lon_parser, Parsing Latitude and Longitude strings, Usage, How it works, Conversion to Latitude Longitude Formats, Converting to numbers, Converting to strings, Usage with Pandas

</details>

### odc-loader

Tooling for constructing xarray objects from parsed metadata

`pip install odc-loader` · installs (wheel) · licence: Apache Software License · rank 11063 · last release 2026-10-10 · [PyPI](https://pypi.org/project/odc-loader/)

<details><summary>README extract</summary>

Tools for constructing xarray objects from parsed metadata.

</details>

### geodatasets

Spatial data examples

`pip install geodatasets` · installs (wheel) · licence: BSD License · rank 11203 · last release 2026-11-03 · [PyPI](https://pypi.org/project/geodatasets/) · [source](https://github.com/geopandas/geodatasets)

<details><summary>README extract</summary>

Fetch links or download and cache spatial data example files.

The `geodatasets` contains an API on top of a JSON with metadata of externally hosted
datasets containing geospatial information useful for illustrative and educational
purposes.

See the documentation at geodatasets.readthedocs.io/.

Example:
```python
In [1]: import geodatasets

In [2]: geodatasets.data
Out[2]:
{'geoda': {'airbnb': {'url': '
   'license': 'NA',
   'attribution': 'Center for Spatial Data Science, University of Chicago',
   'name': 'geoda.airbnb',
   'description': 'Airbnb rentals, socioeconomics, and crime in Chicago',
   'geometry_type': 'Polygon',
   'nrows': 77,
...
```

Sections: geodatasets, How to use

</details>

### xproj

Xarray extension for projections and coordinate reference systems

`pip install xproj` · installs (wheel) · licence: Apache Software License · rank 11849 · last release 2025-07-07 · [PyPI](https://pypi.org/project/xproj/) · [docs](https://xproj.readthedocs.io) · [source](https://github.com/xarray-contrib/xproj)

<details><summary>README extract</summary>

A lightweight Xarray extension for managing geospatial coordinate reference
systems (CRS) using PROJ/Pyproj.

*Current development status: experimental, proof-of-concept.*

Sections: XProj, Usage, Goals, Non-Goals

</details>

### pypolyline

Fast Google Polyline encoding and decoding using Rust

`pip install pypolyline` · installs (wheel) · licence: BlueOak-1.0.0 · rank 12051 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pypolyline/) · [source](https://github.com/urschrei/pypolyline)

<details><summary>README extract</summary>

Example:
```python
from pypolyline.cutil import encode_coordinates, decode_polyline

coords = [
            [52.64125, 23.70162],
            [52.64938, 23.70154],
            [52.64957, 23.68546],
            [52.64122, 23.68549],
            [52.64125, 23.70162]
         ]

# precision is 5 for Google Polyline, 6 for OSRM / Valhalla
...
```

Sections: Fast Google Polyline Encoding and Decoding, Usage, Error Handling, How it Works, Is It Fast, Citing `Pypolyline`

</details>

### pyOrthomosaic

Native (Cython + optional CUDA) orthomosaic generator for nadir drone imagery

`pip install pyOrthomosaic` · installs from source (sdist only) · licence: MIT · rank 12218 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pyOrthomosaic/)

<details><summary>README extract</summary>

Orthomosaics, DSM/DTM, dense point clouds and 3D meshes from drone photos — natively in Python.
No Docker, no VM, no OpenCV, GDAL or PROJ. The heavy lifting runs in Cython-compiled C that uses
every CPU core; NVIDIA (CUDA) and Apple-silicon (Metal) GPUs are used when available.

Two pipelines:

| | Command | Output | ...

Example:
```python
from orthomosaic import build_3d, Options3D

opt = Options3D(gps_sigma=0.05,          # RTK-fixed positions (m)
                gcp="gcps.txt",          # WebODM / Pix4D GCP list
                gcp_sigma=0.02)          # surveyed accuracy (m)
build_3d("images/", "recon/", opt)
```

...

</details>

### pyrtcm

RTCM3 protocol parser

`pip install pyrtcm` · installs (wheel) · licence: BSD-3-Clause · rank 12476 · last release 2026-10-19 · [PyPI](https://pypi.org/project/pyrtcm/) · [docs](https://www.semuconsulting.com/pyrtcm/) · [source](https://github.com/semuconsulting/pyrtcm)

<details><summary>README extract</summary>

Current Status |
Installation |
Reading |
Parsing |
Generating |
Serializing |
Utilities |
Examples |
Extensibility |
Command Line Utility |
Graphical Client |
Author & License

`pyrtcm` is an original Python 3 parser for the RTCM3 © GPS/GNSS protocol. ...

Example:
```python
class pyrtcm.rtcmreader.RTCMReader(stream, **kwargs)
```

Sections: pyrtcm, Reading (Streaming), Parsing, Iterating Through Group Attributes, Generating, Serializing, Utility Methods, Examples, Extensibility, Command Line Utility, Graphical Client

</details>

### convertbng

Fast lon, lat to and from ETRS89 and BNG (OSGB36) using the OS OSTN15 transform

`pip install convertbng` · installs (wheel) · licence: BlueOak-1.0.0 · rank 12550 · last release 2026-10-11 · [PyPI](https://pypi.org/project/convertbng/) · [source](https://github.com/urschrei/convertbng)

<details><summary>README extract</summary>

A utility library for converting decimal WGS84 longitude and latitude coordinates into ETRS89 (EPSG:25830) and/or British National Grid (More correctly: OSGB36, or EPSG:27700) Eastings and Northings, and vice versa.

Conversion is handled by the Rust `lonlat_bng` crate, and is quite fast. Some benchmarks can be found here.

Example:
```python
from convertbng.cutil import convert_bng, convert_lonlat

# convert a single value
res = convert_bng(lon, lat)

# convert longitude and latitude to OSGB36 Eastings and Northings using OSTN15 corrections
lons = [lon1, lon2, lon3]
lats = [lat1, lat2, lat3]
res_list = convert_bng(lons, lats)

...
```

...

</details>

### geolib

A library for geohash encoding, decoding and associated functions

`pip install geolib` · installs (wheel) · licence: MIT License · rank 12665 · last release 2019-05-04 · [PyPI](https://pypi.org/project/geolib/)

<details><summary>README extract</summary>

A python library for geohash encoding, decoding and finding neighbour cells. This is a python port of Chris Veness' javascript implementation.

Wikipedia reference

Sections: Geolib, Usage, Documentation

</details>

### tobler

Tobler is a Python library for areal interpolation.

`pip install tobler` · installs (wheel) · licence: BSD License · rank 13260 · last release 2026-04-10 · [PyPI](https://pypi.org/project/tobler/) · [source](https://github.com/pysal/tobler)

<details><summary>README extract</summary>

Spatial interpolation, Dasymetric Mapping, & Change of Support"

</details>

### pygeofilter

pygeofilter is a pure Python parser implementation of OGC filtering standards

`pip install pygeofilter` · installs (wheel) · licence: MIT License · rank 13387 · last release 2026-06-08 · [PyPI](https://pypi.org/project/pygeofilter/)

<details><summary>README extract</summary>

pygeofilter is a pure Python parser implementation of OGC filtering standards

Features:
* Parsing of several filter encoding standards
 * CQL as defined in CSW 2.0
 * CQL JSON as defined in OGC API - Features - Part 3: Filtering and the Common Query Language (CQL)
 * JSON Filter Expressions (JFE) ...

Example:
```python
>>> from pygeofilter.parsers.ecql import parse as parse_ecql
>>> filters = parse_ecql(filter_expression)
>>> from pygeofilter.parsers.cql_json import parse as parse_json
>>> filters = parse_json(filter_expression)
```

Sections: pygeofilter, Features, Usage, Inspection, Evaluation, Command line utility, Releasing, Docker, Backends, Django, SQL, Optimization

</details>

### pydantic-geojson

Pydantic validation for GeoJson

`pip install pydantic-geojson` · installs (wheel) · licence: MIT License · rank 13410 · last release 2026-03-01 · [PyPI](https://pypi.org/project/pydantic-geojson/) · [docs](https://github.com/gb-libs/pydantic-geojson) · [source](https://github.com/gb-libs/pydantic-geojson)

<details><summary>README extract</summary>

A type-safe, Pydantic-based library for validating and working with GeoJSON data according to RFC 7946 specification.

Example:
```python
from pydantic_geojson import PointModel

# Create a point
point = PointModel(
    type="Point",
    coordinates=[-105.01621, 39.57422]
)

print(point)
# type='Point' coordinates=Coordinates(lon=-105.01621, lat=39.57422)
```

Sections: pydantic-geojson 🌍, Quick Start, GeoJSON Types with Visualizations, Features and FeatureCollections, Feature, FeatureCollection, Custom Properties Models, Validation, Example: Invalid Coordinates, FastAPI Integration, Basic Example, Working with Different Geometry Types, Custom Properties with FastAPI, OpenAPI Schema Generation

</details>

### spreg

PySAL Spatial Econometric Regression in Python

`pip install spreg` · installs (wheel) · licence: BSD License · rank 13443 · last release 2026-07-27 · [PyPI](https://pypi.org/project/spreg/) · [source](https://github.com/pysal/spreg)

### momepy

Urban Morphology Measuring Toolkit

`pip install momepy` · installs (wheel) · licence: BSD License · rank 13539 · last release 2026-07-02 · [PyPI](https://pypi.org/project/momepy/) · [source](https://github.com/pysal/momepy)

<details><summary>README extract</summary>

Momepy (Morphological Measuring in Python) is a library for
quantitative analysis of urban form - urban morphometrics. It is
part of PySAL (Python Spatial Analysis Library) and is built on top
of GeoPandas, other PySAL modules, and
networkX.

</details>

### pyubx2

UBX protocol parser and generator

`pip install pyubx2` · installs (wheel) · licence: BSD-3-Clause · rank 13700 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyubx2/) · [docs](https://www.semuconsulting.com/pyubx2/) · [source](https://github.com/semuconsulting/pyubx2)

<details><summary>README extract</summary>

Current Status |
Installation |
Message Categories |
Reading |
Parsing |
Generating |
Serializing |
Configuration Interface |
Utilities |
Examples |
Extensibility |
Troubleshooting |
Command Line Utility |
Graphical Client |
Author & License

`pyubx2` is an original Python 3 parser for the UBX © protocol. ...

Example:
```python
class pyubx2.ubxreader.UBXReader(stream, *args, **kwargs)
```

Sections: pyubx2, UBX Message Categories - GET, SET, POLL, Reading (Streaming), Parsing, Generating, Serializing, Configuration Interface, Utility Methods, Examples, Extensibility, Troubleshooting, 2. `Serial Permission` errors., 3. `UnicodeDecode` errors., Command Line Utility

</details>

### milsymbol

Military symbols (MIL-STD-2525 / STANAG APP-6) in Python — port of milsymbol.js

`pip install milsymbol` · installs (wheel) · licence: MIT License · rank 13747 · last release 2026-03-21 · [PyPI](https://pypi.org/project/milsymbol/)

<details><summary>README extract</summary>

A reference implementation and test harness for porting
milsymbol (JavaScript)
to Python — with a usable frozen renderer as a side effect.

Generates SVG military symbols per MIL-STD-2525 (B/C/D/E) and
STANAG APP-6 (B/D/E).

Example:
```python
from milsymbol import Symbol

sym = Symbol("10031000001211000000", size=80)   # friendly infantry
svg = sym.as_svg()                               # → SVG string

sym = Symbol("SHG-UCI----", size=80)             # hostile infantry
svg = sym.as_svg()
```

Sections: milsymbol-py, The porting problem, Our approach: extraction, not translation, What Phase 1 actually is, Analogy, A note on process, API, `Symbol(sidc, **kwargs)`, Methods, Affiliations, Playground, Coverage, Can I use this in production?, Upstream version

</details>

### giddy

PySAL-giddy for exploratory spatiotemporal data analysis

`pip install giddy` · installs (wheel) · licence: BSD License · rank 13797 · last release 2026-07-26 · [PyPI](https://pypi.org/project/giddy/) · [source](https://github.com/pysal/giddy)

<details><summary>README extract</summary>

Giddy is an open-source python library for exploratory spatiotemporal data analysis and the analysis of geospatial distribution dynamics. It is under active development for the inclusion of newly proposed analytics that consider the role of space in the evolution of distributions over time.

*Below are six choropleth maps of U.S. ...

Sections: PySAL-giddy for exploratory spatiotemporal data analysis, Requirements

</details>

### xvec

Vector data cubes for Xarray

`pip install xvec` · installs (wheel) · licence: MIT License · rank 13918 · last release 2025-11-22 · [PyPI](https://pypi.org/project/xvec/) · [source](https://github.com/xarray-contrib/xvec)

<details><summary>README extract</summary>

In geospatial analysis, data cubes can be of two sorts. The first is a raster data cube, typically represented by an Xarray DataArray indexed either by `x` or `y` dimensions or `latitude` and `longitude`. ...

</details>

### stac-valid

A package to validate STAC files

`pip install stac-valid` · installs (wheel) · licence: Apache Software License · rank 14491 · last release 2026-09-04 · [PyPI](https://pypi.org/project/stac-valid/) · [source](https://github.com/stac-utils/stac-validator)

<details><summary>README extract</summary>

> ⚠️ IMPORTANT NOTICE: PyPI Package Renamed ⚠️
> Due to an administrative transition, the PyPI package name for this project has changed. The `stac-validator` package on PyPI is no longer maintained.
> To get the latest updates, bug fixes, and features (v4.2.0 and beyond), you must now install `stac-valid`. ...

Features:
STAC Validator is a tool to validate STAC (SpatioTemporal Asset Catalog) json files against the official STAC specification. It provides both a command-line interface and a Python API for validating STAC objects.

Example:
```python
from stac_validator.batch_validator import validate_concurrently

# Validate files
results = validate_concurrently(
    ["item1.json", "item2.json", "item3.json"],
    max_workers=None,  # Auto-detect cores
    show_progress=True
)

...

</details>

### zeit-cdts

Change detection and time series analysis of Earth observation data cubes: LandTrendr, CCDC, BFAST, TWDTW, phenology, accuracy assessment, embeddings and deep learning

`pip install zeit-cdts` · installs (wheel) · licence: GPL-3.0-or-later · rank 14620 · last release 2026-11-08 · [PyPI](https://pypi.org/project/zeit-cdts/) · [docs](https://sacridini.github.io/zeit-cdts/)

_README extract left out: share-alike licence._

### pointpats

Methods and Functions for planar point pattern analysis

`pip install pointpats` · installs (wheel) · licence: BSD License · rank 14908 · last release 2026-06-23 · [PyPI](https://pypi.org/project/pointpats/) · [source](https://github.com/pysal/pointpats)

<details><summary>README extract</summary>

Statistical analysis of planar point patterns.

This package is part of PySAL: The Python Spatial Analysis Library.

This pointpats package is intended to support the statistical analysis of planar point patterns.

It currently works on cartesian coordinates. ...

Sections: pointpats: Point Pattern Analysis in PySAL, Introduction, Documentation, Bug reports

</details>

### pygdal

Virtualenv and setuptools friendly version of standard GDAL python bindings

`pip install pygdal` · installs from source (sdist only) · licence: MIT License · rank 14913 · last release 2023-05-18 · [PyPI](https://pypi.org/project/pygdal/)

<details><summary>README extract</summary>

b'pygdal\n======\n\nVirtualenv and setuptools friendly version of standard GDAL python bindings.\n\nThis package is for you if you had problems installing GDAL in your virtualenv. You can install GDAL into your virtualenv using this package but you still need to install GDAL library and its header files on your system. ...

</details>

## Also in this topic

- [pyproj](scientific-engineering.md#pyproj) - Python interface to PROJ (cartographic projections and coordinate transformations library)
- [rtree](database.md#rtree) - R-Tree spatial index for Python GIS
- [rasterio](multimedia-graphics.md#rasterio) - Fast and direct raster I/O for use with NumPy
- [affine](multimedia-graphics.md#affine) - Matrices describing affine transformation of the plane
- [geocoder](internet.md#geocoder) - Geocoder is a simple and consistent geocoding library.
- [measurement](scientific-engineering.md#measurement) - Easily use and manipulate unit-aware measurements in Python.
- [Cartopy](scientific-engineering.md#cartopy) - A Python library for cartographic visualizations with Matplotlib
- [earthengine-api](multimedia-graphics.md#earthengine-api) - Earth Engine Python API
- [color-operations](multimedia-graphics.md#color-operations) - Apply basic color-oriented image operations.
- [arcgis](internet-www-http.md#arcgis) - ArcGIS API for Python
- [tippecanoe](scientific-engineering-2.md#tippecanoe) - Builds vector tilesets from large (or small) collections of GeoJSON, FlatGeobuf, or CSV features
- [pykml](multimedia-graphics.md#pykml) - Python KML library
- [plpygis](database.md#plpygis) - Python tools for PostGIS
- [gstools](scientific-engineering-2.md#gstools) - GSTools: A geostatistical toolbox.
- [postal](internet-www-http-2.md#postal) - Python bindings to libpostal for fast international address parsing/normalization
- [gstools-cython](scientific-engineering-2.md#gstools-cython) - Cython backend for GSTools.
- [PyKrige](scientific-engineering-2.md#pykrige) - Kriging Toolkit for Python.
- [regionmask](scientific-engineering-2.md#regionmask) - create masks of geospatial regions for arbitrary grids
- [dask-geopandas](scientific-engineering-2.md#dask-geopandas) - Parallel GeoPandas with Dask
