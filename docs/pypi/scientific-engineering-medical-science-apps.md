# Scientific/Engineering / Medical Science Apps.

[Index](README.md) · 11 packages in this topic, 27 more listed under another topic, by downloads.

### pydicom

A pure Python package for reading and writing DICOM data

`pip install pydicom` · installs (wheel) · licence: MIT License · rank 1690 · last release 2026-03-19 · [PyPI](https://pypi.org/project/pydicom/) · [docs](https://pydicom.github.io/pydicom) · [source](https://github.com/pydicom/pydicom)

<details><summary>README extract</summary>

*pydicom* is a pure Python package for working with DICOM files.
It lets you read, modify and write DICOM data in an easy "pythonic" way. As a pure Python package,
*pydicom* can run anywhere Python runs without any other requirements, although if you're working
with *Pixel Data* then we recommend you also install NumPy. ...

Example:
```python
from pydicom import dcmread

ds = dcmread("/path/to/file.dcm")
# Edit the (0010,0020) 'Patient ID' element
ds.PatientID = "12345678"
ds.save_as("/path/to/file_updated.dcm")
```

Sections: pydicom, Documentation, Pixel Data, Decompressing *Pixel Data, JPEG, JPEG-LS and JPEG 2000, RLE, Compressing *Pixel Data, JPEG-LS, JPEG 2000, Examples

</details>

### pylibjpeg

A Python framework for decoding JPEG and decoding/encoding DICOM RLE data, with a focus on supporting pydicom

`pip install pylibjpeg` · installs (wheel) · licence: MIT License · rank 3800 · last release 2025-09-01 · [PyPI](https://pypi.org/project/pylibjpeg/) · [source](https://github.com/pydicom/pylibjpeg)

<details><summary>README extract</summary>

A Python framework for decoding JPEG and JPEG-LS and decoding/encoding JPEG 2000 and RLE, with a focus on providing support for pydicom.

Example:
```python
from pydicom import dcmread
from pydicom.data import get_testdata_file

# With the pylibjpeg-libjpeg plugin
ds = dcmread(get_testdata_file('JPEG-LL.dcm'))
jpg_arr = ds.pixel_array

# With the pylibjpeg-openjpeg plugin
ds = dcmread(get_testdata_file('JPEG2000.dcm'))
j2k_arr = ds.pixel_array

# With the pylibjpeg-rle plugin and pydicom v2.2+
...
```

Sections: pylibjpeg, Plugins, Usage, Decoding, With pydicom, Standalone JPEG decoding, Encoding

</details>

### pylibjpeg-openjpeg

A Python wrapper for openjpeg, with a focus on use as a plugin for for pylibjpeg

`pip install pylibjpeg-openjpeg` · installs (wheel) · licence: MIT License · rank 3840 · last release 2026-09-23 · [PyPI](https://pypi.org/project/pylibjpeg-openjpeg/)

<details><summary>README extract</summary>

A Python wrapper for
openjpeg, with a focus on use as a plugin for pylibjpeg.

Linux, OSX and Windows are all supported.

Example:
```python
from pydicom import dcmread
from pydicom.data import get_testdata_file

ds = dcmread(get_testdata_file('JPEG2000.dcm'))
arr = ds.pixel_array
```

Sections: pylibjpeg-openjpeg, Dependencies, Decoding, Encoding, Transfer Syntaxes, Usage, With pylibjpeg and pydicom, Standalone JPEG decoding, Standalone JPEG encoding

</details>

### pylibjpeg-libjpeg

A Python wrapper for libjpeg, with a focus on use as a plugin for for pylibjpeg

`pip install pylibjpeg-libjpeg` · installs (wheel) · licence: GNU General Public License v3 (GPLv3); Other/Proprietary License · rank 4011 · last release 2026-10-24 · [PyPI](https://pypi.org/project/pylibjpeg-libjpeg/)

_README extract left out: share-alike licence._

### pylibjpeg-rle

Python bindings for a fast RLE decoder/encoder, with a focus on use as a plugin for pylibjpeg

`pip install pylibjpeg-rle` · installs (wheel) · licence: MIT · rank 4505 · last release 2025-09-07 · [PyPI](https://pypi.org/project/pylibjpeg-rle/)

<details><summary>README extract</summary>

A fast DICOM (PackBits) RLE plugin for pylibjpeg, written in Rust with a Python wrapper.

Linux, MacOS and Windows are all supported.

Example:
```python
from pydicom import dcmread
from pydicom.data import get_testdata_file

ds = dcmread(get_testdata_file("OBXXXX1A_rle.dcm"))
arr = ds.pixel_array
```

Sections: pylibjpeg-rle, Usage, Decoding, With pylibjpeg, Standalone with pydicom, Encoding, Benchmarks

</details>

### pynetdicom

A Python implementation of the DICOM networking protocol

`pip install pynetdicom` · installs (wheel) · licence: MIT License · rank 6221 · last release 2025-08-02 · [PyPI](https://pypi.org/project/pynetdicom/) · [docs](https://pydicom.github.io/pynetdicom)

<details><summary>README extract</summary>

A Python implementation of the DICOM networking
protocol, originally based on (legacy)
pynetdicom.

DICOM is the international standard for medical
images and related information. It defines the formats and communication protocols for
media exchange in radiology, cardiology, radiotherapy and other medical domains. ...

Example:
```python
from pynetdicom import AE

ae = AE(ae_title='MY_ECHO_SCU')
# Verification SOP Class has a UID of 1.2.840.10008.1.1
# we can use the UID str directly when adding the requested
# presentation context
ae.add_requested_context('1.2.840.10008.1.1')

# Associate with a peer AE
assoc = ae.associate(addr, port)

if assoc.is_established:
...
```

...

</details>

### dicom2nifti

package for converting dicom files to nifti

`pip install dicom2nifti` · installs (wheel) · licence: MIT · rank 6565 · last release 2025-06-23 · [PyPI](https://pypi.org/project/dicom2nifti/)

<details><summary>README extract</summary>

With this package you can convert dicom images to nifti files.
There is support for most anatomical CT and MR data.
For MR specifically there is support for most 4D data (like DTI and fMRI)

</details>

### vedo

A python module for scientific visualization, analysis of 3D objects and point clouds.

`pip install vedo` · installs (wheel) · licence: MIT License · rank 6843 · last release 2026-10-25 · [PyPI](https://pypi.org/project/vedo/) · [docs](https://vedo.embl.es) · [source](https://github.com/marcomusy/vedo)

<details><summary>README extract</summary>

Your friendly python module
for scientific analysis and visualization of 3d objects.

Example:
```python
from vedo import Sphere, show

sphere = Sphere().c("tomato")
show(sphere, axes=1).close()
```

Sections: 🚀 Quick Start, 📙 Documentation, 🎨 Features, ⌨ Command Line Interface, 🐾 Gallery, 📜 References

</details>

### hdmf

A hierarchical data modeling framework for modern science data standards

`pip install hdmf` · installs (wheel) · licence: BSD-3-Clause · rank 8876 · last release 2026-08-19 · [PyPI](https://pypi.org/project/hdmf/)

<details><summary>README extract</summary>

The Hierarchical Data Modeling Framework, or *HDMF*, is a Python package for working with hierarchical data.
It provides APIs for specifying data models, reading and writing data to different storage backends, and
representing data with Python objects.

Documentation of HDMF can be found at

Sections: The Hierarchical Data Modeling Framework, Overall Health, Citing HDMF, COPYRIGHT

</details>

### pynwb

Package for working with Neurodata stored in the NWB format.

`pip install pynwb` · installs (wheel) · licence: BSD License · rank 9404 · last release 2026-09-02 · [PyPI](https://pypi.org/project/pynwb/)

<details><summary>README extract</summary>

PyNWB is a Python package for working with NWB files. The PyNWB
documentation can be found at

Sections: Overall Health, NWB Format API, Citing NWB, COPYRIGHT

</details>

### pypulseqpp

Fast drop-in PyPulseq replacement over a C++ sequence core, with hardware safety checks.

`pip install pypulseqpp` · installs (wheel) · licence: MIT · rank 13041 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pypulseqpp/) · [docs](https://pulserver.github.io/pypulseqpp/) · [source](https://github.com/pulserver/pypulseqpp)

<details><summary>README extract</summary>

pypulseqpp is a fast drop-in replacement for PyPulseq, written in Python with
a C++ backend. You write MR pulse sequences exactly as you write them in
PyPulseq, and get back a sequence that is fast to build, check and write,
however long it is. Change one line of your script, ...

Example:
```python
import pypulseqpp as pp  # in place of: import pypulseq as pp
```

Sections: How it works, Sequences as functions, Learn more

</details>

## Also in this topic

- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [vtk](multimedia-graphics.md#vtk) - VTK is an open-source toolkit for 3D computer graphics, image processing, and visualization
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [simpleitk](scientific-engineering.md#simpleitk) - SimpleITK is a simplified interface to the Insight Toolkit (ITK) for image registration and segmentation
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [hl7](communications.md#hl7) - Python library parsing HL7 v2.x messages
- [monai](scientific-engineering.md#monai) - AI Toolkit for Healthcare Imaging
- [fastobo](scientific-engineering-bio-informatics.md#fastobo) - Faultless AST for Open Biomedical Ontologies in Python.
- [nnunetv2](scientific-engineering-artificial-intelligence.md#nnunetv2) - nnU-Net is a framework for out-of-the box image segmentation.
- [pronto](scientific-engineering-bio-informatics.md#pronto) - Python frontend to ontologies.
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [pyhmmer](scientific-engineering-bio-informatics.md#pyhmmer) - Cython bindings and Python interface to HMMER3.
- [pymzml](scientific-engineering-bio-informatics.md#pymzml) - high-throughput mzML parsing
- [eutils](scientific-engineering-bio-informatics.md#eutils) - Python interface to NCBI's eutilities API
- [ndex2](scientific-engineering-bio-informatics.md#ndex2) - Nice CX Python includes a client and a data model.
- [batchgeneratorsv2](scientific-engineering-artificial-intelligence.md#batchgeneratorsv2) - Batchgenerators but better
- [itk-core](scientific-engineering-2.md#itk-core) - ITK is an open-source toolkit for multidimensional image analysis
- [datamol](scientific-engineering-artificial-intelligence.md#datamol) - A python library to work with molecules. Built on top of RDKit.
- [itk-filtering](scientific-engineering-2.md#itk-filtering) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-numerics](scientific-engineering-2.md#itk-numerics) - ITK is an open-source toolkit for multidimensional image analysis
- [pyfamsa](scientific-engineering-bio-informatics.md#pyfamsa) - Cython bindings and Python interface to FAMSA, an algorithm for ultra-scale multiple sequence alignments.
- [itk](scientific-engineering-2.md#itk) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-io](scientific-engineering-2.md#itk-io) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-segmentation](scientific-engineering-2.md#itk-segmentation) - ITK is an open-source toolkit for multidimensional image analysis
- [itk-registration](scientific-engineering-2.md#itk-registration) - ITK is an open-source toolkit for multidimensional image analysis
- [hgvs](scientific-engineering-bio-informatics.md#hgvs) - HGVS Parser, Formatter, Mapper, Validator
- [torchio](scientific-engineering-2.md#torchio) - Tools for medical image processing with PyTorch
