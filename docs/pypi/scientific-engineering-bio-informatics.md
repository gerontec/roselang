# Scientific/Engineering / Bio-Informatics

[Index](README.md) · 83 packages in this topic, 31 more listed under another topic, by downloads.

### networkx

Python package for creating and manipulating graphs and networks

`pip install networkx` · installs (wheel) · licence: BSD-3-Clause · rank 138 · last release 2026-09-21 · [PyPI](https://pypi.org/project/networkx/) · [docs](https://networkx.org/documentation/stable/) · [source](https://github.com/networkx/networkx)

<details><summary>README extract</summary>

NetworkX is a Python package for the creation, manipulation,
and study of the structure, dynamics, and functions
of complex networks.

Example:
```python
>>> import networkx as nx
>>> G = nx.Graph()
>>> G.add_edge("A", "B", weight=4)
>>> G.add_edge("B", "D", weight=2)
>>> G.add_edge("A", "C", weight=3)
>>> G.add_edge("C", "D", weight=4)
>>> nx.shortest_path(G, "A", "D", weight="weight")
['A', 'B', 'D']
```

Sections: NetworkX, Simple example, Bugs

</details>

### biotite

A comprehensive library for computational molecular biology

`pip install biotite` · installs (wheel) · licence: BSD-3-Clause · rank 3105 · last release 2026-10-18 · [PyPI](https://pypi.org/project/biotite/) · [docs](https://www.biotite-python.org) · [source](https://github.com/biotite-dev/biotite)

<details><summary>README extract</summary>

*Biotite* is your Swiss army knife for bioinformatics.
Whether you want to identify homologous sequence regions in a protein family
or you would like to find disulfide bonds in a protein structure: *Biotite*
has the right tool for you.
This package bundles popular tasks in computational molecular biology
into a uniform *Python* library. ...

Example:
```python
import biotite.sequence.align as align
import biotite.sequence.io.fasta as fasta
import biotite.database.entrez as entrez

# Download FASTA file for the sequences of avidin and streptavidin
file_name = entrez.fetch_single_file(
    uids=["CAC34569", "ACL82594"], file_name="sequences.fasta",
    db_name="protein", ret_type="fasta"
)

...
```

Sections: Biotite project, Usage

</details>

### anndata

Annotated data.

`pip install anndata` · installs (wheel) · licence: BSD-3-Clause · rank 3231 · last release 2026-09-18 · [PyPI](https://pypi.org/project/anndata/) · [docs](https://anndata.readthedocs.io/) · [source](https://github.com/scverse/anndata)

<details><summary>README extract</summary>

anndata is a Python package for handling annotated data matrices in memory and on disk, positioned between pandas and xarray. anndata offers a broad range of computationally efficient features including, among others, sparse data support, and lazy operations. ...

Sections: anndata - Annotated data, Public API

</details>

### gemmi

library for structural biology

`pip install gemmi` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 3322 · last release 2026-03-02 · [PyPI](https://pypi.org/project/gemmi/) · [source](https://github.com/project-gemmi/gemmi)

<details><summary>README extract</summary>

GEMMI can help if you work with:

* macromolecular models (from mmCIF, PDB and mmJSON files),
* refinement restraints (CIF files) and small molecule models,
* crystallographic reflections (from MTZ and SF-mmCIF files),
* electron and other density maps (MRC/CCP4 files),
* crystallographic symmetries,
* or if you just read and write CIF/STAR files ...

</details>

### scanpy

Single-Cell Analysis in Python.

`pip install scanpy` · installs (wheel) · licence: BSD-3-Clause · rank 4162 · last release 2026-10-29 · [PyPI](https://pypi.org/project/scanpy/) · [docs](https://scanpy.scverse.org/) · [source](https://github.com/scverse/scanpy)

<details><summary>README extract</summary>

Scanpy is a scalable toolkit for analyzing single-cell gene expression data built jointly with anndata.
It includes preprocessing, visualization, clustering, trajectory inference and differential expression testing.
The Python-based implementation efficiently deals with datasets of more than one million cells. ...

Sections: Scanpy – Single-Cell Analysis in Python, Public API

</details>

### prefixcommons

A python API for working with ID prefixes

`pip install prefixcommons` · installs (wheel) · licence: BSD License · rank 4536 · last release 2022-07-19 · [PyPI](https://pypi.org/project/prefixcommons/) · [source](https://github.com/prefixcommons/prefixcommons-py)

<details><summary>README extract</summary>

A python API for working with ID prefixes in the context of
prefixcommons

Current functionality: Uses JSON-LD contexts to expand and contract
CURIEs to URIs

E.g. GO:0008150 <=>

Example:
```python
>>> from prefixcommons import contract_uri
>>> print(contract_uri('
['GO:0008150']

>>> from prefixcommons import expand_uri
>>> print(expand_uri('GO:000850'))
```

Sections: prefixcommons, Example

</details>

### prefixmaps

A python library for retrieving semantic prefix maps

`pip install prefixmaps` · installs (wheel) · licence: Apache Software License · rank 4541 · last release 2024-10-17 · [PyPI](https://pypi.org/project/prefixmaps/) · [source](https://github.com/linkml/prefixmaps)

<details><summary>README extract</summary>

A Python library for retrieving semantic prefix maps.

A semantic prefix map will map a a prefix (e.g. `skos`) to a namespace (e.g `

This repository and the corresponding library is designed to satisfy the following requirements:

- generation of prefix maps in headers of RDF documents ...

Example:
```python
from prefixmaps import load_converter
from curies import Converter

converter: Converter = load_converter(["obo", "bioregistry.upper", "linked_data", "prefixcc"])

>>> converter.expand("CHEBI:1")
'
>>> converter.expand("GEO:1")
'
>>> converter.expand("owl:Class")
'
>>> converter.expand("FlyBase:FBgn123")
'
```

...

</details>

### json-flattener

Python library for denormalizing nested dicts or json objects to tables and back

`pip install json-flattener` · installs (wheel) · licence: BSD License · rank 4552 · last release 2022-02-26 · [PyPI](https://pypi.org/project/json-flattener/)

<details><summary>README extract</summary>

Python library for denormalizing/flattening lists of complex objects to tables/data frames, with roundtripping

Sections: json-flattener, Notebook Example, Description, Method, Command line usage (TODO), Usage from Python, use within LinkML, Comparison, Pandas json_normalize, Java json-flattener, Python, csvjson

</details>

### biotraj

Basic trajectory file format functionality for Biotite; forked from MDTraj

`pip install biotraj` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 5569 · last release 2024-11-02 · [PyPI](https://pypi.org/project/biotraj/) · [docs](https://www.biotite-python.org) · [source](https://github.com/biotite-dev/biotraj)

_README extract left out: share-alike licence._

### primer3-py

Simple primer design and analysis

`pip install primer3-py` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 5633 · last release 2026-10-21 · [PyPI](https://pypi.org/project/primer3-py/) · [docs](http://libnano.github.io/primer3-py)

_README extract left out: share-alike licence._

### pyfaidx

pyfaidx: efficient pythonic random access to fasta subsequences

`pip install pyfaidx` · installs (wheel) · licence: BSD-3-Clause · rank 5954 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyfaidx/)

<details><summary>README extract</summary>

Samtools provides a function "faidx" (FAsta InDeX), which creates a
small flat index file ".fai" allowing for fast random access to any
subsequence in the indexed FASTA file, while loading a minimal amount of the
file in to memory. ...

Example:
```python
>>> from pyfaidx import Fasta
>>> genes = Fasta('tests/data/genes.fasta')
>>> genes
Fasta("tests/data/genes.fasta")  # set strict_bounds=True for bounds checking
```

Sections: Description, Usage, cli script: faidx, Known issues

</details>

### mrcfile

MRC file I/O library

`pip install mrcfile` · installs (wheel) · licence: BSD License · rank 6316 · last release 2025-01-22 · [PyPI](https://pypi.org/project/mrcfile/)

<details><summary>README extract</summary>

`mrcfile` is a Python implementation of the MRC2014 file format, which
is used in structural biology to store image and volume data.

It allows MRC files to be created and opened easily using a very simple API,
which exposes the file's header and data as numpy arrays. The code runs in
Python 2 and 3 and is fully unit-tested. ...

Features:
* Clean, simple API for access to MRC files
* Easy to install and use
* Validation of files according to the MRC2014 format
* Seamless support for gzip and bzip2 files
* Memory-mapped file option for fast random access to very large files
* ...

Example:
```python
>>> import mrcfile
>>> with mrcfile.open('tests/test_data/EMD-3197.map') as mrc:
...     mrc.data[10,10]
...
array([ 2.58179283,  3.1406002 ,  3.64495397,  3.63812137,  3.61837363,
...

</details>

### gseapy

Gene Set Enrichment Analysis in Python

`pip install gseapy` · installs (wheel) · licence: BSD-3-Clause · rank 7157 · last release 2026-10-29 · [PyPI](https://pypi.org/project/gseapy/) · [docs](https://gseapy.readthedocs.io/en/latest/) · [source](https://github.com/zqfang/GSEApy)

<details><summary>README extract</summary>

Release notes :

Tutorial for general usage

* A faithful Rust port of fgsea's multilevel algorithm that resolves p-values far below `1/permutation_num`.

Features:
I would like to use Pandas to explore my data, but I did not find a convenient tool to
do gene set enrichment analysis in python. So, here are my reasons: ...

Example:
```python
import gseapy

# run GSEA.
gseapy.gsea(data='expression.txt', gene_sets='gene_sets.gmt', cls='test.cls', outdir='test')

# run prerank
gseapy.prerank(rnk='gsea_data.rnk', gene_sets='gene_sets.gmt', outdir='test')

# run prerank with the fgsea multilevel p-value method
...
```

...

</details>

### tmol

GPU-accelerated PyTorch reimplementation of the Rosetta energy function

`pip install tmol` · installs (wheel) · licence: Apache-2.0 · rank 7168 · last release 2026-10-20 · [PyPI](https://pypi.org/project/tmol/) · [docs](https://uw-ipd.github.io/tmol/) · [source](https://github.com/uw-ipd/tmol)

<details><summary>README extract</summary>

TMol provides all-atom scoring, packing, minimization, and
FastRelax in PyTorch. It batches proteins, nucleic acids, ligands, and complexes
on CPU or CUDA, with gradients through coordinate scoring.

Documentation ·
Tutorials ·
API reference

Example:
```python
import torch
import tmol

device = torch.device("cpu")
pose = tmol.pose_stack_from_file("input.pdb", device)

score_function = tmol.beta2016_score_function(device)
score = score_function.render_whole_pose_scoring_module(pose)
print(score(pose.coords))
```

</details>

### py3Dmol

An IPython interface for embedding 3Dmol.js views in Jupyter notebooks

`pip install py3Dmol` · installs (wheel) · licence: MIT License · rank 7238 · last release 2026-05-23 · [PyPI](https://pypi.org/project/py3Dmol/)

<details><summary>README extract</summary>

A simple IPython/Jupyter widget to
embed an interactive 3Dmol.js viewer in a notebook.

The widget is completely static, which means the viewer doesn't need a running
IPython kernel to be useful and web pages and presentations generated from
the notebook will work as expected. ...

Sections: py3Dmol, Usage

</details>

### mdtraj

MDTraj: A modern, open library for the analysis of molecular dynamics trajectories

`pip install mdtraj` · installs (wheel) · licence: LGPL-2.1-or-later · rank 7769 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mdtraj/) · [source](https://github.com/mdtraj/mdtraj)

_README extract left out: share-alike licence._

### propka

Heuristic pKa calculations with ligands

`pip install propka` · installs (wheel) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 7936 · last release 2024-01-02 · [PyPI](https://pypi.org/project/propka/)

_README extract left out: share-alike licence._

### biothings-client

Python Client for BioThings API services.

`pip install biothings-client` · installs (wheel) · licence: BSD License · rank 7942 · last release 2026-07-23 · [PyPI](https://pypi.org/project/biothings-client/) · [docs](https://biothings-clientpy.readthedocs.io) · [source](https://github.com/biothings/biothings_client.py)

<details><summary>README extract</summary>

*biothings_client* is an easy-to-use Python wrapper to access any Biothings.api
-based backend service. Currently, the following clients are available:

 * gene - The client for MyGene.Info, which provides access to gene objects.
 * variant - The client MyVariant.Info, which provides access to genetic variant objects. ...

Sections: Intro, Optional dependencies, Tutorial, Documentation, Usage, Contact

</details>

### openslide-python

Python interface to OpenSlide

`pip install openslide-python` · installs (wheel) · licence: LGPL-2.1-only AND BSD-3-Clause AND MIT AND LicenseRef-Public-Domain · rank 7980 · last release 2026-10-24 · [PyPI](https://pypi.org/project/openslide-python/) · [docs](https://openslide.org/api/python/) · [source](https://github.com/openslide/openslide-python)

_README extract left out: share-alike licence._

### harmonypy

Batch correction for single-cell data using the Harmony algorithm with a C++ Armadillo backend.

`pip install harmonypy` · installs (wheel) · licence: GPL-3.0-or-later · rank 8004 · last release 2026-10-06 · [PyPI](https://pypi.org/project/harmonypy/) · [source](https://github.com/slowkow/harmonypy)

_README extract left out: share-alike licence._

### mygene

Python Client for MyGene.Info services.

`pip install mygene` · installs (wheel) · licence: BSD License · rank 8113 · last release 2021-04-05 · [PyPI](https://pypi.org/project/mygene/)

<details><summary>README extract</summary>

MyGene.Info provides simple-to-use REST web services to query/retrieve gene annotation data.
It's designed with simplicity and performance emphasized. `mygene`, is an easy-to-use Python
wrapper to access MyGene.Info services. ...

Example:
```python
In [1]: import mygene

In [2]: mg = mygene.MyGeneInfo()

In [3]: mg.getgene(1017)
Out[3]:
{'_id': '1017',
 'entrezgene': 1017,
 'name': 'cyclin-dependent kinase 2',
 'symbol': 'CDK2',
 'taxid': 9606,
 ...
}

# use "fields" parameter to return a subset of fields
In [4]: mg.getgene(1017, fields='name,symbol,refseq')
Out[4]:
{'_id': '1017',
...
```

Sections: Intro, Requirements, Optional dependencies, Tutorial, Documentation, Usage, Contact

</details>

### fastobo

Faultless AST for Open Biomedical Ontologies in Python.

`pip install fastobo` · installs (wheel) · licence: MIT License · rank 8208 · last release 2026-10-21 · [PyPI](https://pypi.org/project/fastobo/) · [docs](https://fastobo.readthedocs.io/)

<details><summary>README extract</summary>

*Faultless AST for Open Biomedical Ontologies in Python.*

Features:
`fastobo` is a Rust library implementing a
reliable parser for the OBO file format 1.4. This extension module exports
idiomatic Python bindings that can be used to load, edit and serialize ontologies
in the OBO format.

Example:
```python
import fastobo
obodoc = fastobo.load("../data/ms.obo")
```

Sections: `fastobo-py`, Overview, Usage, Feedback, About

</details>

### pdbeccdutils

Toolkit to parse and process small molecules in wwPDB

`pip install pdbeccdutils` · installs (wheel) · licence: Apache Software License; Other/Proprietary License · rank 8482 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pdbeccdutils/) · [docs](https://pdbeurope.github.io/ccdutils/) · [source](https://github.com/PDBeurope/ccdutils)

<details><summary>README extract</summary>

An RDKit-based python toolkit for parsing and processing small molecule definitions in wwPDB Chemical Component Dictionary and wwPDB The Biologically Interesting Molecule Reference Dictionary.`pdbeccdutils` provides streamlined access to all metadata of small molecules in the PDB and offers a set of convenient methods to compute various properties ...

Features:
* `gemmi` CCD read/write.
* Generation of 2D depictions (`No image available` generated if the flattening cannot be done) along with the quality check.
* Generation of 3D conformations. ...

Sections: pdbeccdutils, Features, Dependencies, Documentation

</details>

### mmcif-pdbx

Python utilities for PDBx/mmCIF storage model

`pip install mmcif-pdbx` · installs (wheel) · licence: CC0-1.0 · rank 8675 · last release 2026-04-26 · [PyPI](https://pypi.org/project/mmcif-pdbx/) · [docs](https://mmcif-pdbx.readthedocs.io)

<details><summary>README extract</summary>

This is yet another PyPI package for
It emphasizes a simple and pure Python interface to basic mmCIF functionality.

The canonical mmCIF Python package can be found at
It is full-featured and includes C/C++ code to accelerate I/O functions. ...

Sections: PDBx/mmCIF Dictionary Resources, Origin of this software, Versions, More information about this software

</details>

### pronto

Python frontend to ontologies.

`pip install pronto` · installs (wheel) · licence: MIT License · rank 8700 · last release 2026-10-19 · [PyPI](https://pypi.org/project/pronto/) · [docs](https://pronto.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

*A Python frontend to ontologies.*

Example:
```python
>>> from pronto import Ontology
```

Sections: `pronto`, 🗺️ Overview, 💡 Examples, 🏷️ Get a term by accession, 🖊️ Create a new term from scratch, ✏️ Convert an OWL ontology to OBO format, 🌿 Find ontology terms without subclasses, 🤫 Silence warnings, 📖 API Reference

</details>

### pdb2pqr

Automates many of the common tasks of preparing structures for continuum solvation calculations as well as many other types of biomolecular structure modeling, analysis, and simulation.

`pip install pdb2pqr` · installs (wheel) · licence: BSD License · rank 8729 · last release 2026-10-24 · [PyPI](https://pypi.org/project/pdb2pqr/) · [docs](https://pdb2pqr.readthedocs.io/) · [source](https://github.com/Electrostatics/pdb2pqr)

<details><summary>README extract</summary>

This package contains the PDB2PQR software. For more information, please see

</details>

### prolif

Interaction Fingerprints for protein-ligand complexes and more

`pip install prolif` · installs (wheel) · licence: Apache-2.0 · rank 8770 · last release 2026-10-09 · [PyPI](https://pypi.org/project/prolif/) · [docs](https://prolif.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

ProLIF (*Protein-Ligand Interaction Fingerprints*) is a tool designed to generate
interaction fingerprints for complexes made of ligands, protein, DNA or RNA molecules
extracted from molecular dynamics trajectories, docking simulations and experimental
structures. ...

Sections: Description, Documentation, Issues, Discussion, Citing ProLIF, Logo

</details>

### ubiquerg

Various utility functions

`pip install ubiquerg` · installs (wheel) · licence: BSD-2-Clause · rank 9038 · last release 2026-04-02 · [PyPI](https://pypi.org/project/ubiquerg/)

<details><summary>README extract</summary>

Ubiquerg is a utility package with a collection of universally helpful functions. The name means work (erg) everywhere (ubique), indicating our intention for these to be low-level functions that can be used in lots of different places. Functions are divided into groups, including:

- collection
- environment
- files
- paths
- system
- web ...

</details>

### cyvcf2

fast vcf parsing with cython + htslib

`pip install cyvcf2` · installs (wheel) · licence: MIT · rank 9362 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cyvcf2/) · [docs](https://brentp.github.io/cyvcf2/)

<details><summary>README extract</summary>

Note: cyvcf2 versions < 0.20.0 require htslib < 1.10. cyvcf2 versions >= 0.20.0 require htslib >= 1.10

<!-- ghp-import -p docs/build/html/ -->
The latest documentation for cyvcf2 can be found here:

If you use cyvcf2, please cite the paper

Fast Python (3.9+) parsing of VCF and BCF including region-queries. ...

Example:
```python
from cyvcf2 import VCF

for variant in VCF('some.vcf.gz'): # or VCF('some.bcf')
    variant.REF, variant.ALT # e.g. REF='A', ALT=['C', 'T']

    variant.CHROM, variant.start, variant.end, variant.ID, \
                variant.FILTER, variant.QUAL

    # numpy arrays of specific things we pull from the sample fields.
...
```

...

</details>

### yacman

A YAML configuration manager

`pip install yacman` · installs (wheel) · licence: BSD-2-Clause · rank 9392 · last release 2026-03-06 · [PyPI](https://pypi.org/project/yacman/)

<details><summary>README extract</summary>

Yacman is a YAML configuration manager. It provides some convenience tools for dealing with YAML configuration files.

Please see this Python notebook for features and usage instructions and this document for API documentation.

How to upgrade to yacman v1.0.0.
Yacman v1 provides 2 feature upgrades:

1. ...

Example:
```python
from yacman import FutureYAMLConfigManager as YAMLConfigManager
```

Sections: Upgrading guide, Upgrading from v0.9.3 to v1.0.0, Locking caveats, From v0.9.3 (using future) to v1.X.X, Demos

</details>

### mudata

Multimodal data

`pip install mudata` · installs (wheel) · licence: BSD License · rank 9471 · last release 2026-08-17 · [PyPI](https://pypi.org/project/mudata/) · [docs](https://mudata.readthedocs.io/) · [source](https://github.com/scverse/mudata)

<details><summary>README extract</summary>

[][pypi]
[][tests]
[][codecov]
[][documentation]
[][scverse]
[][numfocus]

Documentation | Publication | Changelog

For using `MuData` in multimodal omics applications see muon. ...

Example:
```python
from mudata import MuData

mdata = MuData({'rna': adata_rna, 'atac': adata_atac})
```

Sections: MuData – multimodal data, Data structure, Overview, Input, I/O with `.h5mu` files

</details>

### pyhmmer

Cython bindings and Python interface to HMMER3.

`pip install pyhmmer` · installs (wheel) · licence: MIT AND BSD-3-Clause AND BSD-2-Clause · rank 9487 · last release 2026-08-19 · [PyPI](https://pypi.org/project/pyhmmer/) · [docs](https://pyhmmer.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

*Cython bindings and Python interface to HMMER3.*

%20times&replace=%241&style=flat-square&label=downloads&color=303f9f&cacheSeconds=86400)

%3C%2Fdiv%3E&replace=%241&style=flat-square&label=citations&cacheSeconds=3600)

HMMER is a biological sequence analysis tool that uses profile hidden Markov
models to search for sequence homologs. ...

Example:
```python
import pyhmmer

with pyhmmer.easel.SequenceFile("pyhmmer/tests/data/seqs/938293.PRJEB85.HG003687.faa", digital=True) as seq_file:
    sequences = seq_file.read_block()

with pyhmmer.plan7.HMMFile("pyhmmer/tests/data/hmms/txt/t2pks.hmm") as hmm_file:
    for hits in pyhmmer.hmmsearch(hmm_file, sequences, cpus=4):
...
```

...

</details>

### pybedtools

Wrapper around BEDTools for bioinformatics work

`pip install pybedtools` · installs (wheel) · licence: MIT License · rank 9520 · last release 2026-08-26 · [PyPI](https://pypi.org/project/pybedtools/)

<details><summary>README extract</summary>

Features:
The BEDTools suite of programs is widely
used for genomic interval manipulation or "genome algebra". `pybedtools` wraps
and extends BEDTools and offers feature-level manipulations from within
Python. ...

Example:
```python
from pybedtools import BedTool

snps = BedTool('snps.bed.gz')  # [1]
genes = BedTool('hg19.gff')    # [1]

intergenic_snps = snps.subtract(genes)                       # [2]
nearby = genes.closest(intergenic_snps, d=True, stream=True) # [2, 3]

for gene in nearby:             # [4]
    if int(gene[-1]) < 5000:    # [4]
...
```

Sections: Overview, Why `pybedtools`?

</details>

### pymzml

high-throughput mzML parsing

`pip install pymzml` · installs (wheel) · licence: MIT License · rank 9570 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pymzml/) · [source](https://github.com/pymzml/pymzML)

<details><summary>README extract</summary>

Module to parse mzML data in Python based on cElementTree

Copyright 2010-2026 by:

 | M. Kösters,
 | J. Leufken,
 | T. Bald,
 | A. Niehues,
 | S. Schulze,
 | K. Sugimoto,
 | R.P. Zahedi,
 | M. Hippler,
 | S.A. Leidel,
 | C. Fufezan,

Please refer to:

 | Dr. ...

Sections: Introduction, General information, Contact information, Summary, Implementation, Download

</details>

### refgenconf

A standardized configuration object for reference genome assemblies

`pip install refgenconf` · installs (wheel) · licence: BSD-2-Clause · rank 9732 · last release 2026-04-01 · [PyPI](https://pypi.org/project/refgenconf/)

<details><summary>README extract</summary>

Configuration object for refgenie *et al.*

Documentation for `refgenconf` can be found with the primary documentation for refgenie.

</details>

### DendroPy

A Python library for phylogenetics and phylogenetic computing: reading, writing, simulation, processing and manipulation of phylogenetic trees (phylogenies) and characters.

`pip install DendroPy` · installs (wheel) · licence: BSD License · rank 9960 · last release 2026-10-23 · [PyPI](https://pypi.org/project/DendroPy/) · [docs](https://jeetsukumaran.github.io/DendroPy/) · [source](https://github.com/jeetsukumaran/DendroPy)

<details><summary>README extract</summary>

| automated tests: | package version: | documentation: | test coverage: |

| | | | |

DendroPy is a Python library for phylogenetic computing.
It provides classes and functions for the simulation, processing, and
manipulation of phylogenetic trees and character matrices, and supports the
reading and writing of phylogenetic data in a range of ...

Sections: Documentation, Citing

</details>

### eutils

Python interface to NCBI's eutilities API

`pip install eutils` · installs (wheel) · licence: Apache-2.0 · rank 9964 · last release 2025-12-07 · [PyPI](https://pypi.org/project/eutils/) · [docs](https://biocommons.github.io/eutils/) · [source](https://github.com/biocommons/eutils/)

<details><summary>README extract</summary>

**eutils is a Python package to simplify searching, fetching, and parsing
records from NCBI using their
E-utilities interface**

Features:
* simple Pythonic interface for searching and fetching
* Support for NCBI API keys, and rate throttling when no key is available
* optional sqlite-based caching of compressed replies
* "façades" that facilitate access to essential attributes in XML ...

Sections: eutils -- simplified interface to NCBI E-Utilities, Features, Example Usage, MacOS or Linux Systems, Linux (Debian-based systems)

</details>

### openbabel-wheel

An unofficial repository to distribute OpenBabel prebuilt wheels through Pypi..

`pip install openbabel-wheel` · installs (wheel) · licence: GNU General Public License (GPL) · rank 9965 · last release 2026-03-06 · [PyPI](https://pypi.org/project/openbabel-wheel/) · [source](https://github.com/njzjz/openbabel-wheel)

_README extract left out: share-alike licence._

### ete3

A Python Environment for (phylogenetic) Tree Exploration

`pip install ete3` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 9995 · last release 2023-05-02 · [PyPI](https://pypi.org/project/ete3/) · [docs](http://etetoolkit.org/docs/latest/tutorial/index.html) · [source](https://github.com/etetoolkit/ete)

_README extract left out: share-alike licence._

### pyopenms

Python wrapper for C++ LC-MS library OpenMS

`pip install pyopenms` · installs (wheel) · licence: BSD-3-Clause · rank 10025 · last release 2026-09-30 · [PyPI](https://pypi.org/project/pyopenms/) · [docs](https://pyopenms.readthedocs.io) · [source](https://github.com/OpenMS/OpenMS/tree/develop/src/pyOpenMS)

<details><summary>README extract</summary>

This package contains Python bindings for a large part of the OpenMS library
for mass spectrometry based proteomics. It thus provides providing facile
access to a feature-rich, open-source algorithm library for mass-spectrometry
based proteomics analysis. ...

</details>

### ndex2

Nice CX Python includes a client and a data model.

`pip install ndex2` · installs (wheel) · licence: BSD License · rank 10129 · last release 2026-08-12 · [PyPI](https://pypi.org/project/ndex2/)

<details><summary>README extract</summary>

Features:
The NDEx2 Python Client provides methods to access NDEx via
the NDEx REST Server API. As well as methods for common operations on
networks via the NiceCXNetwork class.

Sections: NDEx2 Python Client, Overview, Dependencies, Compatibility, Resources, 3.12.0 (2025-08-12), 3.11.0 (2025-07-22), 3.10.0 (2025-01-14), 3.9.0 (2024-06-18), 3.8.0 (2024-02-07), 3.7.0 (2024-01-03), 3.6.0 (2023-11-14), 3.5.1 (2023-04-11), 3.5.0 (2022-06-28)

</details>

### gprofiler-official

Functional enrichment analysis and more via the g:Profiler toolkit

`pip install gprofiler-official` · installs (wheel) · licence: BSD License · rank 10244 · last release 2019-04-02 · [PyPI](https://pypi.org/project/gprofiler-official/)

<details><summary>README extract</summary>

The official Python 3 interface to the g:Profiler
toolkit for enrichment analysis of functional (GO and other) terms,
conversion between identifier namespaces and mapping orhologous genes in related organisms.

It has an optional dependency on pandas.

Example:
```python
from gprofiler import GProfiler
gp = GProfiler(
    user_agent='ExampleTool', #optional user agent
    return_dataframe=True, #return pandas dataframe or plain python structures
)
```

Sections: gprofiler, Project description, Legacy version, Tools, g:GOSt (profile), g:Convert (convert), g:Orth (orth), g:SNPense (snpense)

</details>

### bx-python

Tools for manipulating biological data, particularly multiple sequence alignments

`pip install bx-python` · installs (wheel) · licence: MIT · rank 10587 · last release 2026-10-29 · [PyPI](https://pypi.org/project/bx-python/) · [source](https://github.com/bxlab/bx-python)

<details><summary>README extract</summary>

The bx-python project is a Python library and associated set of scripts for rapid implementation of genome scale analyses. The library contains a variety of useful modules, but the particular strengths are: ...

Sections: bx-python, Requirements

</details>

### phylo-treetime

Maximum-likelihood phylodynamic inference

`pip install phylo-treetime` · installs (wheel) · licence: MIT License · rank 10636 · last release 2026-04-23 · [PyPI](https://pypi.org/project/phylo-treetime/)

<details><summary>README extract</summary>

Features:
TreeTime provides routines for ancestral sequence reconstruction and inference of molecular-clock phylogenies, i.e., a tree where all branches are scaled such that the positions of terminal nodes correspond to their sampling times and internal nodes ...

Sections: Overview, Features, Command-line usage, Timetrees, Rerooting and substitution rate estimation, Ancestral sequence reconstruction, Homoplasy analysis, Mugration analysis, Metadata and date format, Example scripts, Related tools, Projects using TreeTime, Building the documentation, Requirements

</details>

### networkit

NetworKit is a toolbox for high-performance network analysis

`pip install networkit` · installs (wheel) · licence: MIT License · rank 10750 · last release 2026-11-06 · [PyPI](https://pypi.org/project/networkit/) · [docs](https://networkit.github.io/dev-docs/index.html) · [source](https://github.com/networkit/networkit)

<details><summary>README extract</summary>

High-performance tools for large-scale network analysis

 Explore the docs »

 Try Demo
 Report Bug
 Request Feature

 Table of Contents

 About The Project

- Key Features

 Getting Started

- Prerequisites

- Installation

- Usage

- Building from Source

- Documentation

- Contributing

- License

- Contact

- Publications

Features:
- Scalable: Analyze networks with billions of edges
- Fast: Parallel algorithms utilizing multicore architectures
- Comprehensive: Wide range of network analysis algorithms
- Interactive: Python interface with Jupyter notebook support ...

Example:
```python
from networkit.generators import HyperbolicGenerator
from networkit.community import detectCommunities

# Generate a random hyperbolic graph
g = (
    HyperbolicGenerator(1e5)
    .generate()
)

...

</details>

### tiledbsoma

Python API for efficient storage and retrieval of single-cell data using TileDB

`pip install tiledbsoma` · installs from source (sdist only) · licence: MIT · rank 10954 · last release 2026-01-27 · [PyPI](https://pypi.org/project/tiledbsoma/)

<details><summary>README extract</summary>

Features:
This is a Python implementation of the SOMA API specification for interacting with the Unified Single-cell Data Model.

Sections: Overview, From source, `platform_config` format

</details>

### bioblend

Library for interacting with the Galaxy API

`pip install bioblend` · installs (wheel) · licence: MIT · rank 10985 · last release 2026-04-14 · [PyPI](https://pypi.org/project/bioblend/) · [docs](https://bioblend.readthedocs.io/) · [source](https://github.com/galaxyproject/bioblend)

<details><summary>README extract</summary>

BioBlend is a Python library for interacting with the Galaxy API.

BioBlend is supported and tested on:

- Python 3.10 - 3.14
- Galaxy release 19.05 and later.

Full docs are available at with a quick library
overview also available in ABOUT.rst.

</details>

### openslide-bin

Binary build of OpenSlide

`pip install openslide-bin` · installs (wheel) · licence: LGPL-2.1-only AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clau · rank 11061 · last release 2026-06-20 · [PyPI](https://pypi.org/project/openslide-bin/) · [source](https://github.com/openslide/openslide-bin)

_README extract left out: share-alike licence._

### pdbfixer

pdbfixer: Fixes problems in PDB files

`pip install pdbfixer` · installs from source (sdist only) · licence: MIT License · rank 11300 · last release 2026-02-06 · [PyPI](https://pypi.org/project/pdbfixer/)

<details><summary>README extract</summary>

Protein Data Bank (PDB) files often have a number of problems that must be
fixed before they can be used in a molecular dynamics simulation. The details
vary depending on how the file was generated. Here are some of the most common
ones:

- If the structure was generated by X-ray crystallography, most or all of the ...

</details>

### biom-format

Biological Observation Matrix (BIOM) format

`pip install biom-format` · installs (wheel) · licence: BSD License · rank 11420 · last release 2026-10-05 · [PyPI](https://pypi.org/project/biom-format/)

<details><summary>README extract</summary>

The BIOM file format (canonically pronounced *biome*) is designed to be a general-use format for representing counts of observations (e.g., OTUs, KO categories, lipid types) in one or more biological samples (e.g., microbiome samples, genomes, metagenomes).

Further details can be found at

Installation ...

</details>

### logomaker

Package for making Sequence Logos

`pip install logomaker` · installs (wheel) · licence: MIT License · rank 11477 · last release 2025-03-25 · [PyPI](https://pypi.org/project/logomaker/) · [docs](http://logomaker.readthedocs.io) · [source](https://github.com/jbkinney/logomaker)

<details><summary>README extract</summary>

Software for creating highly customized sequence logos

Sections: logomaker, Documentation

</details>

### pyfamsa

Cython bindings and Python interface to FAMSA, an algorithm for ultra-scale multiple sequence alignments.

`pip install pyfamsa` · installs (wheel) · licence: GPL-3.0-or-later · rank 11714 · last release 2026-03-24 · [PyPI](https://pypi.org/project/pyfamsa/) · [docs](https://pyfamsa.readthedocs.io/en/stable/)

_README extract left out: share-alike licence._

### smoldyn

Python package for the Smoldyn simulator

`pip install smoldyn` · installs (wheel) · licence: LGPL-3.0-or-later · rank 11893 · last release 2026-10-22 · [PyPI](https://pypi.org/project/smoldyn/)

_README extract left out: share-alike licence._

### fabio

FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python

`pip install fabio` · installs (wheel) · licence: MIT License · rank 11938 · last release 2026-06-19 · [PyPI](https://pypi.org/project/fabio/) · [docs](http://www.silx.org/doc/fabio/latest/) · [source](https://github.com/silx-kit/fabio)

<details><summary>README extract</summary>

Main websites:

 * (historical)

FabIO is an I/O library for images produced by 2D X-ray detectors and written in Python.
FabIO supports detector images from a dozen companies (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...),
for a total of 30 different file formats (like CBF, EDF, TIFF, ...) and offers a unified interface to their
headers ...

Sections: FabIO: Fable Input/Output library, Usage, Documentation, Transparent handling of compressed files, Design Specifications

</details>

### pephubclient

PEPhub command line interface.

`pip install pephubclient` · installs (wheel) · licence: BSD License · rank 12111 · last release 2026-08-05 · [PyPI](https://pypi.org/project/pephubclient/)

<details><summary>README extract</summary>

`PEPHubClient` is a tool to provide Python API and CLI for PEPhub.

Documentation:

Source Code:

Sections: PEPHubClient, `pephubclient` features

</details>

### logmuse

Logging setup

`pip install logmuse` · installs (wheel) · licence: BSD-2-Clause · rank 12207 · last release 2026-08-07 · [PyPI](https://pypi.org/project/logmuse/)

<details><summary>README extract</summary>

A small Python package that makes it easy to add CLI-controllable logging to your command-line tools. It provides a simple interface for standard logging arguments (`--verbosity`, `--silent`, `--logdev`) that can be passed directly to a logger.

Example:
```python
import argparse
import logmuse

parser = argparse.ArgumentParser()
# your arguments here...
parser = logmuse.add_logging_options(parser)
args = parser.parse_args()
logger = logmuse.logger_via_cli(args)

logger.info("Hello, world!")
```

Sections: logmuse, Quick start, Setup for a CLI package, 1. Add CLI args to your argparser, 2. Activate in your main function, For imported packages, Avoid calling `init_logger` at import time, Using logmuse interactively, Usage reference, CLI options, `init_logger` parameters, Verbosity levels

</details>

### eido

A project metadata validator

`pip install eido` · installs (wheel) · licence: BSD License · rank 12292 · last release 2026-07-23 · [PyPI](https://pypi.org/project/eido/)

<details><summary>README extract</summary>

PEP validation tool based on jsonschema. See documentation for usage.

</details>

### peppy

A python-based project metadata manager for portable encapsulated projects

`pip install peppy` · installs (wheel) · licence: BSD License · rank 12353 · last release 2025-10-20 · [PyPI](https://pypi.org/project/peppy/)

<details><summary>README extract</summary>

`peppy` is the official python package for reading Portable Encapsulated Projects or PEPs in Python.

Links to complete documentation:

* Complete documentation and API for the `peppy` python package is at peppy.databio.org.
* Reference documentation for standard PEP format is at pep.databio.org. ...

</details>

### hydride

Adding hydrogen atoms to molecular models

`pip install hydride` · installs from source (sdist only) · licence: BSD License · rank 12491 · last release 2024-11-04 · [PyPI](https://pypi.org/project/hydride/) · [docs](https://hydride.biotite-python.org) · [source](https://github.com/biotite-dev/hydride)

<details><summary>README extract</summary>

Many tasks in structural biology ranging from simulations and hydrogen
bond detection to mere visual analysis, require complete molecular
models.
However, most experimentally determined structures do not include
the position of hydrogen atoms, due to their small size and electron
density. ...

Example:
```python
atom_array, _ = hydride.add_hydrogen(atom_array)
atom_array.coord = hydride.relax_hydrogen(atom_array)
```

Sections: Hydride - Adding hydrogen atoms to molecular models, Usage, Python API

</details>

### dnaio

Read and write FASTA and FASTQ files efficiently

`pip install dnaio` · installs (wheel) · licence: MIT · rank 12526 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dnaio/) · [source](https://github.com/marcelm/dnaio/)

<details><summary>README extract</summary>

`dnaio` is a Python 3 library for very efficient parsing and writing of FASTQ and also FASTA files.
Since `dnaio` version 1.1.0, support for efficiently parsing uBAM files has been implemented.
This allows reading ONT files from the dorado
basecaller directly. ...

Features:
- FASTQ input and output
- FASTA input and output
- BAM input
- Compressed input and output (`.gz`, `.bz2`, `.xz` and `.zst` are detected automatically)
- Paired-end data in two files
- Interleaved paired-end data in a single file ...

Example:
```python
import dnaio

with dnaio.open("reads.fastq.gz") as f:
    bp = 0
    for record in f:
        bp += len(record)
print(f"The input file contains {bp/1E6:.1f} Mbp")
```

Sections: dnaio processes FASTQ, FASTA and uBAM files, Example usage, Limitations, Links

</details>

### cellxgene-census

API to facilitate the use of the CZ CELLxGENE Discover Census. For more information about the API and the project visit https://github.com/chanzuckerberg/cellxgene-census/

`pip install cellxgene-census` · installs (wheel) · licence: MIT License · rank 12543 · last release 2026-06-24 · [PyPI](https://pypi.org/project/cellxgene-census/) · [source](https://github.com/chanzuckerberg/cellxgene-census)

<details><summary>README extract</summary>

The `cellxgene_census` package provides an API to facilitate the use of the CZ CELLxGENE Discover Census. For more information about the API and the project visit the chanzuckerberg/cellxgene-census GitHub repo.

For more help, please file a issue on the repo, or contact us at <soma@chanzuckerberg.com>. ...

Sections: CZ CELLxGENE Discover Census, For More Help

</details>

### scoring-matrices

Dependency free, Cython-compatible scoring matrices to use with biological sequences.

`pip install scoring-matrices` · installs (wheel) · licence: MIT License · rank 12668 · last release 2026-10-01 · [PyPI](https://pypi.org/project/scoring-matrices/) · [docs](https://scoring-matrices.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

*Dependency free, Cython-compatible scoring matrices to use with biological sequences.*

*Scoring Matrices* are matrices used to score the matches and mismatches between
two characters are the same position in a sequence alignment. Some of these
matrices are derived from *substitution matrices*, which uses evolutionary
modeling. ...

Example:
```python
from scoring_matrices import ScoringMatrix
```

Sections: 🧬🔠 `scoring-matrices`, 🗺️ Overview, 💡 Usage, Python, Cython, 💭 Feedback, ⚠️ Issue Tracker

</details>

### omnipath

Python client for the OmniPath web service

`pip install omnipath` · installs (wheel) · licence: MIT · rank 12874 · last release 2025-06-26 · [PyPI](https://pypi.org/project/omnipath/) · [docs](https://omnipath.readthedocs.io/) · [source](https://github.com/saezlab/omnipath)

<details><summary>README extract</summary>

Sections: Python client for the OmniPath web service, The OmniPath database, The Python client, The Python package for OmniPath is pypath, isn't it?, Is there an R client?, Cytoscape

</details>

### pipestat

A pipeline results reporter

`pip install pipestat` · installs (wheel) · licence: BSD-2-Clause · rank 12933 · last release 2026-03-06 · [PyPI](https://pypi.org/project/pipestat/)

<details><summary>README extract</summary>

Pipestat is a Python package for managing pipeline results. It provides a standard API for reporting, storing, and retrieving outputs from any computational pipeline. Results are validated against a JSON Schema and stored in either a YAML file or a PostgreSQL database. ...

Example:
```python
import pipestat

psm = pipestat.PipestatManager(
    schema_path="output_schema.yaml",
    results_file_path="results.yaml",
    record_identifier="sample1",
)
psm.report(values={"accuracy": 0.95, "processing_time": 12.3})
psm.report(values={"output_file": {"path": "results/output.csv", "title": "Output CSV"}})
```

Sections: Quick Start, Schema, Generating a schema from existing results, Optional Dependencies, Database Backend Configuration for Tests

</details>

### isa-rwval

Metadata tracking tools help to manage an increasingly diverse set of life science, environmental and biomedical experiments

`pip install isa-rwval` · installs (wheel) · licence: CPAL-1.0 · rank 12964 · last release 2025-06-19 · [PyPI](https://pypi.org/project/isa-rwval/) · [docs](https://isa-tools.org/isa-api/) · [source](https://github.com/ISA-tools/isa-rwval)

<details><summary>README extract</summary>

This repo is forked originally from

The open source ISA metadata tracking tools help to manage an increasingly diverse set of life science, environmental and biomedical experiments that employing one or a combination of technologies. ...

</details>

### piper

A lightweight python toolkit for gluing together restartable, robust command line pipelines

`pip install piper` · installs (wheel) · licence: BSD-2-Clause · rank 13009 · last release 2026-03-06 · [PyPI](https://pypi.org/project/piper/)

<details><summary>README extract</summary>

A lightweight Python toolkit for gluing together restartable, robust shell pipelines. Pypiper manages shell command execution with automatic restartability, file integrity protection, resource monitoring, and detailed logging -- useful for any multi-step workflow that calls command-line tools. Learn more in the documentation.

</details>

### rcsb-api

Python package interface for RCSB.org API services

`pip install rcsb-api` · installs (wheel) · licence: MIT · rank 13179 · last release 2026-05-05 · [PyPI](https://pypi.org/project/rcsb-api/) · [docs](https://rcsbapi.readthedocs.io/) · [source](https://github.com/rcsb/py-rcsb-api)

<details><summary>README extract</summary>

*rcsb-api*: Python Toolkit for Accessing RCSB.org APIs
Python interface for RCSB Protein Data Bank API services at RCSB.org.

Features:
The _rcsb-api package provides a simple Pythonic interface to the suite of RCSB PDB APIs for querying and fetching data in the PDB. ...

Sections: Overview, Training Materials, Citing

</details>

### PyCifRW

CIF/STAR file support for Python

`pip install PyCifRW` · installs from source (sdist only) · licence: Python Software Foundation License · rank 13244 · last release 2025-03-24 · [PyPI](https://pypi.org/project/PyCifRW/)

<details><summary>README extract</summary>

PyCIFRW Readme

Introduction

PyCIFRW provides support for reading and writing CIF (Crystallographic
Information Format) files using Python. It was developed at the
Australian National Beamline Facility (ANBF), run by the Australian
Synchrotron Research Program (ASRP), as part of a larger project to
provide CIF input/output capabilities for data ...

</details>

### cutadapt

Adapter trimming and other preprocessing of high-throughput sequencing reads

`pip install cutadapt` · installs from source (sdist only) · licence: MIT · rank 13252 · last release 2025-10-23 · [PyPI](https://pypi.org/project/cutadapt/) · [source](https://github.com/marcelm/cutadapt/)

<details><summary>README extract</summary>

Cutadapt finds and removes adapter sequences, primers, poly-A tails and other
types of unwanted sequence from your high-throughput sequencing reads.

Cleaning your data in this way is often required: Reads from small-RNA
sequencing contain the 3’ sequencing adapter because the read is longer than
the molecule that is sequenced. ...

Sections: Cutadapt, Links

</details>

### scvi-tools

Deep probabilistic analysis of single-cell omics data.

`pip install scvi-tools` · installs (wheel) · licence: not stated · rank 13352 · last release 2026-10-28 · [PyPI](https://pypi.org/project/scvi-tools/) · [docs](https://docs.scvi-tools.org/) · [source](https://github.com/scverse/scvi-tools)

<details><summary>README extract</summary>

[][gh-stars-link]
[][pypi-link]
[][pepy-link]
[][conda-link]
[][docs-link]
[][tests-link]
[][build-link]
[][coverage-link]

[scvi-tools] (single-cell variational inference tools) is a package for probabilistic modeling and
analysis of single-cell omics data, built on top of [PyTorch] and [AnnData]. ...

Sections: Analysis of single-cell omics data, Resources, Reference

</details>

### squidpy

Spatial Single Cell Analysis in Python

`pip install squidpy` · installs (wheel) · licence: BSD-3-Clause · rank 13390 · last release 2026-10-29 · [PyPI](https://pypi.org/project/squidpy/) · [docs](https://squidpy.readthedocs.io) · [source](https://github.com/scverse/squidpy)

<details><summary>README extract</summary>

Squidpy is the scverse toolkit for scalable analysis and visualization of spatial molecular data.
It builds on scanpy and anndata, providing streamlined APIs for feature extraction, spatial statistics, and interactive exploration of tissue sections together with microscopy images. ...

Features:
- Build and analyze spatial neighbor graphs directly from Visium, Slide-seq, Xenium, and other spatial omics assays.
- Compute spatial statistics for cell types and genes, including neighborhood enrichment, co-occurrence, and Moran's I. ...

Sections: Squidpy - Spatial Single Cell Analysis in Python, Documentation, Interactive visualization, Key capabilities

</details>

### refgenie

Refgenie creates a standardized folder structure for reference genome files and indexes

`pip install refgenie` · installs (wheel) · licence: BSD-2-Clause · rank 13550 · last release 2026-02-25 · [PyPI](https://pypi.org/project/refgenie/)

<details><summary>README extract</summary>

A standardized reference genome resource manager. See the documentation.

</details>

### meeko

Python package for preparing small molecule for docking

`pip install meeko` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 13558 · last release 2026-08-27 · [PyPI](https://pypi.org/project/meeko/)

_README extract left out: share-alike licence._

### annsel

A Narwhals powered DataFrame-style selection, filtering and indexing operations on AnnData Objects.

`pip install annsel` · installs (wheel) · licence: MIT License · rank 13597 · last release 2026-06-22 · [PyPI](https://pypi.org/project/annsel/) · [docs](https://annsel.readthedocs.io/) · [source](https://github.com/srivarra/annsel)

<details><summary>README extract</summary>

| | |

| Status | [][link-build] [][link-test] [][link-docs] [][link-codecov] [][link-prek] |
| Meta | [][link-hatch] [][link-ruff] [][link-uv] [][link-license] |
| Package | [][link-pypi] [][link-pypi] |
| Ecosystem | [][link-scverse] |
| | |

Annsel is a user-friendly library that brings familiar dataframe-style operations to `AnnData` objects. ...

Example:
```python
import annsel as an

adata = an.datasets.leukemic_bone_marrow_dataset()
```

Sections: annsel, Getting started, Examples, Filter, Select, Group By, Pipe, Contact

</details>

### hgvs

HGVS Parser, Formatter, Mapper, Validator

`pip install hgvs` · installs (wheel) · licence: Apache Software License · rank 13920 · last release 2026-03-17 · [PyPI](https://pypi.org/project/hgvs/)

<details><summary>README extract</summary>

The *hgvs* package provides a Python library to parse, format, validate,
normalize, and map sequence variants according to Variation
Nomenclature (aka Human Genome Variation
Society) recommendations. ...

Features:
- Parsing is based on formal grammar.
- An easy-to-use object model that represents most variant types
 (SNVs, indels, dups, inversions, etc) and concepts (intronic
 offsets, uncertain positions, intervals) ...

Sections: Information, Features, Important Notes, Prerequisites, Examples and Usage, 551,, 760, and, 761. To load reliably, use, See Also

</details>

### pyxDamerauLevenshtein

pyxDamerauLevenshtein implements the Damerau-Levenshtein (DL) edit distance algorithm for Python in Cython for high performance.

`pip install pyxDamerauLevenshtein` · installs (wheel) · licence: BSD-3-Clause · rank 14119 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyxDamerauLevenshtein/)

<details><summary>README extract</summary>

Example:
```python
from pyxdameraulevenshtein import (
    damerau_levenshtein_distance,
    damerau_levenshtein_distance_seqs,
    normalized_damerau_levenshtein_distance,
    normalized_damerau_levenshtein_distance_seqs,
)

damerau_levenshtein_distance('smtih', 'smith')  # expected result: 1
...
```

Sections: pyxDamerauLevenshtein, ABOUT, REQUIREMENTS, USING THIS CODE, DIFFERENCES

</details>

### cobra

COBRApy is a package for constraint-based modeling of metabolic networks.

`pip install cobra` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+); GNU Lesser General Public Licen · rank 14308 · last release 2026-08-11 · [PyPI](https://pypi.org/project/cobra/) · [docs](https://cobrapy.readthedocs.io) · [source](https://github.com/opencobra/cobrapy)

_README extract left out: share-alike licence._

### pyliftover

Pure-python implementation of UCSC ``liftOver`` genome coordinate conversion.

`pip install pyliftover` · installs (wheel) · licence: MIT License · rank 14404 · last release 2024-02-08 · [PyPI](https://pypi.org/project/pyliftover/)

<details><summary>README extract</summary>

PyLiftover is a library for quick and easy conversion of genomic (point) coordinates between different assemblies.

It uses the same logic and coordinate conversion mappings as the UCSC liftOver tool. ...

Example:
```python
from pyliftover import LiftOver
lo = LiftOver('hg17', 'hg18')
lo.convert_coordinate('chr1', 1000000)
```

Sections: Usage, See also

</details>

### posebusters

PoseBusters: Plausibility checks for generated molecule poses.

`pip install posebusters` · installs (wheel) · licence: BSD License · rank 14440 · last release 2026-03-07 · [PyPI](https://pypi.org/project/posebusters/) · [docs](https://posebusters.readthedocs.io/en/latest/) · [source](https://github.com/maabuu/posebusters/)

<details><summary>README extract</summary>

PoseBusters: Plausibility checks for generated molecule poses.

Example:
```python
from dockbusters import DockBuster

# check re-docked ligand
DockBuster().bust(ligand_pred_file, ligand_crystal_file, protein_crystal_file)

# check docked ligand
DockBuster().bust(ligand_pred_file, protein_crystal_file)

# check molecule
DockBuster().bust(ligand_pred_file, protein_crystal_file)
```

Sections: Paper in Chemical Science and preprint on arXiv, Usage, Documentation, Feedback & Contact, Thanks

</details>

### easydev

Common utilities to ease development of Python packages

`pip install easydev` · installs (wheel) · licence: BSD-3-Clause · rank 14532 · last release 2026-10-12 · [PyPI](https://pypi.org/project/easydev/) · [docs](https://easydev.readthedocs.io) · [source](https://github.com/cokelaer/easydev)

<details><summary>README extract</summary>

:documentation:
:contributions: Please join
:source: Please use
:issues: Please use
:Python version supported: 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

Features:
The easydev package provides
miscellaneous utility functions and classes that are repeatedly useful during
the development of Python packages. ...

Example:
```python
from easydev import check_param_in_list, check_range

check_param_in_list("on", ["on", "off"])   # passes silently
check_range(0.5, 0, 1)                     # passes silently
```

Sections: easydev, Overview, Features, Quick Start, Moving away from easydev

</details>

### isovar

Determine mutant protein sequences from RNA using assembly around variants

`pip install isovar` · installs (wheel) · licence: Apache-2.0 · rank 14577 · last release 2026-11-07 · [PyPI](https://pypi.org/project/isovar/)

<details><summary>README extract</summary>

Isovar finds the mutant protein sequence that tumor RNA actually encodes around
each somatic mutation. Given variant calls (VCF) and aligned tumor RNA-seq reads
(BAM), it assembles the reads that carry each mutation into cDNA and translates
that cDNA in the reading frames of annotated transcripts. ...

Example:
```python
from isovar import run_isovar, isovar_results_to_dataframe

isovar_results = run_isovar(
    variants="cancer-mutations.vcf",
    alignment_file="tumor-rna.bam")

for isovar_result in isovar_results:
    # The protein preferred by the context/support policy, or None.
    protein = isovar_result.top_protein_sequence
    if protein is not None:
...
```

Sections: Isovar, Quick start, Command line, Documentation

</details>

### ProDy

A Python Package for Protein Dynamics Analysis

`pip install ProDy` · installs from source (sdist only) · licence: MIT License · rank 14785 · last release 2025-08-19 · [PyPI](https://pypi.org/project/ProDy/) · [docs](http://www.bahargroup.org/prody/tutorials.html) · [source](https://github.com/prody/ProDy)

### pyensembl

Python interface to Ensembl reference genome metadata

`pip install pyensembl` · installs (wheel) · licence: Apache-2.0 · rank 14835 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyensembl/)

<details><summary>README extract</summary>

PyEnsembl looks up genes, transcripts, exons and their protein and transcript
sequences in a pinned Ensembl release or in your
own GTF and FASTA files. It downloads and indexes an annotation once; after
that, queries run locally. ...

Example:
```python
from pyensembl import EnsemblRelease

with EnsemblRelease(93, species="human") as data:
    gene = data.gene_by_id("ENSG00000141510")
    print(gene.name, gene.contig, gene.start, gene.end, gene.strand)
    transcript = data.transcript_by_id("ENST00000269305")
    print(transcript.name, transcript.protein_sequence[:30])
```

Sections: PyEnsembl, Quick start, Command line, Documentation

</details>

## Also in this topic

- [biopython](scientific-engineering.md#biopython) - Freely available tools for computational molecular biology.
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [intervaltree](scientific-engineering-artificial-intelligence.md#intervaltree) - Editable interval tree data structure for Python 2 and 3
- [igraph](scientific-engineering.md#igraph) - High performance graph data structures and algorithms
- [simsimd](scientific-engineering-artificial-intelligence.md#simsimd) - Portable mixed-precision BLAS-like vector math library for x86 and ARM
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [python-igraph](scientific-engineering.md#python-igraph) - High performance graph data structures and algorithms (legacy package)
- [numkong](scientific-engineering-artificial-intelligence.md#numkong) - Portable mixed-precision math, linear-algebra, & retrieval library with 2000+ SIMD kernels for x86, Arm, RISC-V, LoongArch, Power, & WebAssembly
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [pgmpy](scientific-engineering.md#pgmpy) - Python Toolkit for Causal and Probabilistic Reasoning
- [pyteomics](education.md#pyteomics) - A framework for proteomics data analysis.
- [MDAnalysis](scientific-engineering.md#mdanalysis) - An object-oriented toolkit to analyze molecular dynamics trajectories.
- [cwltool](scientific-engineering.md#cwltool) - Common workflow language reference implementation
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [napari](scientific-engineering.md#napari) - n-dimensional array viewer in Python
- [vesin](scientific-engineering.md#vesin) - Computing neighbor lists for atomistic system
- [alchemlyb](scientific-engineering-2.md#alchemlyb) - the simple alchemistry library
- [nglview](multimedia-graphics.md#nglview) - IPython widget to interactively view molecular structures and trajectories.
- [datamol](scientific-engineering-artificial-intelligence.md#datamol) - A python library to work with molecules. Built on top of RDKit.
- [fastcluster](scientific-engineering-artificial-intelligence.md#fastcluster) - Fast hierarchical clustering routines for R and Python.
- [scikit-bio](scientific-engineering-2.md#scikit-bio) - Data structures, algorithms and educational resources for bioinformatics.
- [pdb-tools](scientific-engineering-2.md#pdb-tools) - A swiss army knife for PDB files.
- [ViennaRNA](scientific-engineering-2.md#viennarna) - A library for the prediction and comparison of RNA secondary structures.
- [latch](scientific-engineering-2.md#latch) - The Latch SDK
- [tskit](scientific-engineering-2.md#tskit) - The tree sequence toolkit.
- [medspacy-quickumls](scientific-engineering-artificial-intelligence.md#medspacy-quickumls) - QuickUMLS is a tool for fast, unsupervised biomedical concept extraction from medical text
- [metatensor-core](scientific-engineering-2.md#metatensor-core) - Python bindings for metatensor
- [pygad](scientific-engineering-2.md#pygad) - PyGAD: A Python Library for Building the Genetic Algorithm and Training Machine Learning Algoithms (Keras & PyTorch).
