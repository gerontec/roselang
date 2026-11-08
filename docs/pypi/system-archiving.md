# System / Archiving

[Index](README.md) · 24 packages in this topic, 47 more listed under another topic, by downloads.

### wheel

Command line tool for manipulating wheel files

`pip install wheel` · installs (wheel) · licence: MIT · rank 90 · last release 2026-08-11 · [PyPI](https://pypi.org/project/wheel/) · [docs](https://wheel.readthedocs.io/) · [source](https://github.com/pypa/wheel)

<details><summary>README extract</summary>

This is a command line tool for manipulating Python wheel files, as defined in
PEP 427. It contains the following functionality:

* Convert `.egg` archives into `.whl`
* Unpack wheel archives
* Repack wheel archives
* Add or remove tags in existing wheel archives ...

Sections: wheel, Historical note, Documentation

</details>

### backports.zstd

Backport of compression.zstd

`pip install backports.zstd` · does not install on CPython 3.14 · licence: PSF-2.0 · rank 416 · last release 2026-10-10 · [PyPI](https://pypi.org/project/backports.zstd/) · [source](https://github.com/rogdham/backports.zstd)

<details><summary>README extract</summary>

Backport of PEP-784 “adding Zstandard to the standard library”

📖 PEP-784 | 📃 Changelog

Features:
This is on purpose. For Python
3.14 and later, use the `compression.zstd` module from the standard library.

If you want your code to be compatible with multiple Python versions, condition the
usage of this library based on the Python version: ...

Example:
```python
import sys

if sys.version_info >= (3, 14):
    from compression import zstd
else:
    from backports import zstd

# use the zstd module, for example:
zstd.compress(b"Hello, world!")
```

Sections: backports.zstd, Usage, zstd, tarfile, zipfile, shutil, FAQ, Who are you?, How is this backport constructed?, I found a bug

</details>

### zopfli

Zopfli module for python

`pip install zopfli` · installs (wheel) · licence: Apache Software License · rank 544 · last release 2026-06-10 · [PyPI](https://pypi.org/project/zopfli/)

<details><summary>README extract</summary>

cPython bindings for
zopfli.

It requires Python 3.10 or greater.

Example:
```python
from zopfli.zlib import compress
from zlib import decompress
s = 'Hello World'
print decompress(compress(s))
```

Sections: PYZOPFLI, USAGE, TODO

</details>

### compressed-rtf

Compressed Rich Text Format (RTF) compression and decompression package

`pip install compressed-rtf` · installs (wheel) · licence: MIT · rank 1283 · last release 2025-03-24 · [PyPI](https://pypi.org/project/compressed-rtf/)

<details><summary>README extract</summary>

Compressed Rich Text Format (RTF) compression worker in Python

Description:

Compressed RTF also known as "LZFu" compression format

Based on Rich Text Format (RTF) Compression Algorithm:

Usage example:

License:

Released under The MIT License.

Example:
```python
>>> from compressed_rtf import compress, decompress
>>>
>>> data = '{\\rtf1\\ansi\\ansicpg1252\\pard test}'
>>> comp = compress(data, compressed=True)  # compressed
>>> comp
'#\x00\x00\x00"\x00\x00\x00LZFu3\\\xe8t\x03\x00\n\x00rcpg125\x922\n\xf3 t\x07\x90t}\x0f\x10'
>>>
>>> raw = compress(data, compressed=False)  # raw/uncompressed
>>> raw
...
```

</details>

### pyzipper

AES encryption for zipfile.

`pip install pyzipper` · installs (wheel) · licence: MIT · rank 1435 · last release 2026-05-14 · [PyPI](https://pypi.org/project/pyzipper/)

<details><summary>README extract</summary>

A replacement for Python's `zipfile` that can read and write AES encrypted
zip files. Forked from Python 3.7's `zipfile` module, it features the same
`zipfile` API from that time (most notably, lacking support for
`pathlib`-compatible wrappers that were introduced in Python 3.8).

Example:
```python
import pyzipper

secret_password = b'lost art of keeping a secret'

with pyzipper.AESZipFile('new_test.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(secret_password)
...
```

Sections: pyzipper, Usage, CRC32 Values, AES Strength, Documentation

</details>

### pyzstd

Support for Zstandard (zstd) compression

`pip install pyzstd` · installs (wheel) · licence: BSD-3-Clause · rank 1540 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyzstd/) · [docs](https://pyzstd.readthedocs.io/) · [source](https://github.com/Rogdham/pyzstd)

<details><summary>README extract</summary>

Python bindings to Zstandard (zstd) compression library

📖 Documentation | 📃 Changelog

The `pyzstd` module provides Python support for Zstandard, using
an API style similar to the `bz2`, `lzma`, and `zlib` modules.

> [!WARNING]
> Zstandard is now natively supported in Python’s standard library via the
> `compression.zstd` module. ...

</details>

### zipfile-zstd

Monkey patch the standard zipfile module to enable Zstandard support

`pip install zipfile-zstd` · installs (wheel) · licence: MIT License · rank 2188 · last release 2021-12-08 · [PyPI](https://pypi.org/project/zipfile-zstd/)

<details><summary>README extract</summary>

Monkey patch the standard `zipfile` module to enable Zstandard support.

Based on `zipfile-deflate64`, which provides similar functionality but for the `deflate64` algorithm. Unlike `zipfile-deflate64`, this package supports both compression and decompression.

Requires `python-zstandard` for libzstd bindings.

Example:
```python
import zipfile_zstd  # This has the side effect of patching the zipfile module to support Zstandard
```

Sections: zipfile-zstd, Usage

</details>

### zlib-ng

Drop-in replacement for zlib and gzip modules using zlib-ng

`pip install zlib-ng` · installs (wheel) · licence: PSF-2.0 · rank 2414 · last release 2026-11-04 · [PyPI](https://pypi.org/project/zlib-ng/) · [docs](https://python-zlib-ng.readthedocs.io)

<details><summary>README extract</summary>

Faster zlib and gzip compatible compression and decompression
by providing Python bindings for the zlib-ng library.

This package provides Python bindings for the zlib-ng library.

`python-zlib-ng` provides the bindings by offering three modules: ...

Example:
```python
from zlib_ng import zlib_ng
from zlib_ng import gzip_ng
from zlib_ng import gzip_ng_threaded
```

Sections: python-zlib-ng, Quickstart, python-zlib-ng as a dependency in your project, Differences with zlib and gzip modules

</details>

### isal

Faster zlib and gzip compatible compression and decompression by providing python bindings for the ISA-L ibrary.

`pip install isal` · installs (wheel) · licence: PSF-2.0 · rank 2586 · last release 2026-11-03 · [PyPI](https://pypi.org/project/isal/) · [docs](https://python-isal.readthedocs.io)

<details><summary>README extract</summary>

Faster zlib and gzip compatible compression and decompression
by providing Python bindings for the ISA-L library.

This package provides Python bindings for the ISA-L library. The Intel(R) Intelligent Storage
Acceleration Library (ISA-L) implements several key algorithms in assembly
language. ...

Example:
```python
from isal import isal_zlib
from isal import igzip
from isal import igzip_lib
```

Sections: python-isal, Quickstart, python-isal as a dependency in your project, Differences with zlib and gzip modules

</details>

### zipfile-deflate64

Extract Deflate64 ZIP archives with Python's zipfile API.

`pip install zipfile-deflate64` · installs from source (sdist only) · licence: Apache Software License · rank 3329 · last release 2022-01-05 · [PyPI](https://pypi.org/project/zipfile-deflate64/) · [source](https://github.com/brianhelba/zipfile-deflate64)

<details><summary>README extract</summary>

Extract Deflate64 ZIP archives with Python's `zipfile` API.

Example:
```python
import zipfile_deflate64  # This has the side effect of patching the zipfile module to support Deflate64
```

Sections: zipfile-deflate64, Usage, Design Rationale, The Problem, A Solution

</details>

### zipfile36

Read and write ZIP files - backport of the zipfile module from Python 3.6

`pip install zipfile36` · installs (wheel) · licence: Python Software Foundation License · rank 3537 · last release 2016-10-16 · [PyPI](https://pypi.org/project/zipfile36/)

<details><summary>README extract</summary>

This is a backport of the zipfile module from Python 3.6, which contains some
improvements.

Installation:
Suggested usage:

Example:
```python
if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile
```

</details>

### s3cmd

Command line tool for managing Amazon S3 and CloudFront services

`pip install s3cmd` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 3928 · last release 2023-12-12 · [PyPI](https://pypi.org/project/s3cmd/)

_README extract left out: share-alike licence._

### patool

portable archive file manager

`pip install patool` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 4350 · last release 2026-09-04 · [PyPI](https://pypi.org/project/patool/) · [source](https://github.com/wummel/patool)

_README extract left out: share-alike licence._

### stream-inflate

Uncompress DEFLATE streams in pure Python (albeit compiled with Cython)

`pip install stream-inflate` · installs (wheel) · licence: MIT License · rank 4360 · last release 2026-03-04 · [PyPI](https://pypi.org/project/stream-inflate/) · [source](https://github.com/michalc/stream-inflate)

<details><summary>README extract</summary>

Uncompress Deflate and Deflate64 streams in pure Python (albeit compiled with Cython).

Example:
```python
from stream_inflate import stream_inflate
import httpx

def compressed_chunks():
    # Iterable that yields the bytes of a DEFLATE-compressed stream
    with httpx.stream('GET', ' as r:
        yield from r.iter_raw(chunk_size=65536)

for uncompressed_chunk in stream_inflate()0:
    print(uncompressed_chunk)
```

Sections: stream-inflate, Usage

</details>

### stream-unzip

Python function to stream unzip all the files in a ZIP archive, without loading the entire ZIP file into memory or any of its uncompressed files

`pip install stream-unzip` · installs (wheel) · licence: MIT License · rank 4390 · last release 2026-03-03 · [PyPI](https://pypi.org/project/stream-unzip/) · [docs](https://stream-unzip.docs.trade.gov.uk/) · [source](https://github.com/uktrade/stream-unzip)

<details><summary>README extract</summary>

<!-- --8<-- [start:intro] -->

Python function to stream unzip all the files in a ZIP archive, without loading the entire ZIP file into memory or any of its uncompressed files.
<!-- --8<-- [end:intro] -->

To create ZIP files on the fly try stream-zip.

<!-- --8<-- [start:features] -->

Features:
In addition to being memory efficient, stream-unzip supports:

- Deflate-compressed ZIPs. This is the historical standard for ZIP files.

- Deflate64-compressed ZIPs. These are created by certain versions of Windows Explorer in some circumstances. ...

Sections: stream-unzip, Features

</details>

### stream-zip

Python function to construct a ZIP archive with stream processing - without having to store the entire ZIP in memory or disk

`pip install stream-zip` · installs (wheel) · licence: MIT License · rank 4469 · last release 2026-02-04 · [PyPI](https://pypi.org/project/stream-zip/) · [docs](https://stream-zip.docs.trade.gov.uk/) · [source](https://github.com/uktrade/stream-zip)

<details><summary>README extract</summary>

<!-- --8<-- [start:intro] -->

Python function to construct a ZIP archive on the fly - without having to store the entire ZIP in memory or disk. This is useful in memory-constrained environments, or when you would like to start returning compressed data before you've even retrieved all the uncompressed data. ...

Features:
In addition to being memory efficient (with some limitations) stream-zip:

- Constructs ZIP files that can be stream unzipped, for example by stream-unzip

- Can construct Zip64 ZIP files. ...

Sections: stream-zip, Features

</details>

### unix-ar

AR file handling

`pip install unix-ar` · installs (wheel) · licence: BSD License · rank 4713 · last release 2019-06-12 · [PyPI](https://pypi.org/project/unix-ar/)

<details><summary>README extract</summary>

This packages allows the reading and writing of `AR archive files`.

It is inspired by the `tarfile` and `zipfile` that are part of Python's standard library (unfortunately the name ``arfile`` was taken on PyPI).

Features

The package provides a `ArFile` partially implementing the interface of
`tarfile.TarFile`

Credits ...

Example:
```python
>>> import unix_ar
>>> import tarfile
>>> ar_file = unix_ar.open('mypackage.deb')
>>> tarball = ar_file.open('data.tar.gz/')  # default interest location on .deb files
>>> tar_file = tarfile.open(fileobj=tarball)  # handles gz decompression internally
>>> tar_file.extractfile('usr/local/mypackage/bin/mybinarycontent.sh')
```

</details>

### unlzw3

Pure Python decompression module for .Z files compressed using Unix compress utility

`pip install unlzw3` · installs (wheel) · licence: MIT License · rank 6892 · last release 2024-12-20 · [PyPI](https://pypi.org/project/unlzw3/)

<details><summary>README extract</summary>

Pure Python decompression module for .Z files compressed using Unix compress utility.
Unlike the faster but Linux-specific
unlzw
using Python CFFI, `unlzw3` is slower but works on any platform that runs Python including Windows.

This is a purely Python adaptation of Mark Adler's
'unlzw' C function
on Stackoverflow. ...

Example:
```python
import unlzw3
from pathlib import Path

uncompressed_data = unlzw3.unlzw(Path('file.Z').read_bytes())

# or

uncompressed_data = unlzw3.unlzw(Path('file.Z'))
```

Sections: unlzw3, Usage

</details>

### python-neo-lzf

A fork of python-lzf with pre-built wheel files.

`pip install python-neo-lzf` · installs (wheel) · licence: BSD-3-Clause · rank 7830 · last release 2025-12-25 · [PyPI](https://pypi.org/project/python-neo-lzf/)

<details><summary>README extract</summary>

python-lzf: liblzf Python bindings

This package is a direct translation of the C API of liblzf into Python.
It provides two core functions: compress() and decompress().

- compress(data: bytes, max_length: Optional[int] = None) -> Optional[bytes]
 Compresses the given input bytes. Optionally, a maximum length for the output
 may be specified. ...

</details>

### zipstream-new

Zipfile generator that takes input files as well as streams

`pip install zipstream-new` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8746 · last release 2020-09-14 · [PyPI](https://pypi.org/project/zipstream-new/)

_README extract left out: share-alike licence._

### python-lzf

C Extension for liblzf

`pip install python-lzf` · installs from source (sdist only) · licence: BSD License · rank 10487 · last release 2024-06-13 · [PyPI](https://pypi.org/project/python-lzf/)

### indexed-gzip

Fast random access of gzip files in Python

`pip install indexed-gzip` · installs (wheel) · licence: Zlib · rank 10817 · last release 2025-12-08 · [PyPI](https://pypi.org/project/indexed-gzip/) · [source](https://github.com/pauldmccarthy/indexed_gzip)

<details><summary>README extract</summary>

*Fast random access of gzip files in Python*

 * Overview
 * Installation
 * Usage
 * Using with `nibabel`
 * Index import/export
 * Write support
 * Performance
 * Acknowledgements
 * License

Features:
The `indexed_gzip` project is a Python extension which aims to provide a
drop-in replacement for the built-in Python `gzip.GzipFile` class, the
`IndexedGzipFile`. ...

Example:
```python
import indexed_gzip as igzip

# You can create an IndexedGzipFile instance
# by specifying a file name, or an open file
# handle. For the latter use, the file handle
# must be opened in read-only binary mode.
# Write support is currently non-existent.
myfile = igzip.IndexedGzipFile('big_file.gz')

some_offset_into_uncompressed_data = 234195

...
```

...

</details>

### lhafile

LHA archive support for Python

`pip install lhafile` · installs from source (sdist only) · licence: BSD License · rank 12752 · last release 2025-02-24 · [PyPI](https://pypi.org/project/lhafile/)

<details><summary>README extract</summary>

A python package that handles .lha archives, with an interface similar to the
zipfile module found in the standard library.

</details>

### cabarchive

A pure-python library for creating and extracting cab files

`pip install cabarchive` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 12841 · last release 2026-02-10 · [PyPI](https://pypi.org/project/cabarchive/)

_README extract left out: share-alike licence._

## Also in this topic

- [setuptools](software-development-libraries.md#setuptools) - Most extensible Python build backend with support for C/C++ extension modules
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [brotli](software-development-libraries.md#brotli) - Python bindings for the Brotli compression library
- [python-snappy](internet.md#python-snappy) - Python library for the snappy compression library from Google
- [pex](software-development-build-tools.md#pex) - The PEX packaging toolchain.
- [netCDF4](software-development-libraries.md#netcdf4) - Provides an object-oriented python interface to the netCDF version 4 library
- [hatch-requirements-txt](software-development-libraries.md#hatch-requirements-txt) - Hatchling plugin to read project dependencies from requirements.txt
- [rarfile](software-development-libraries.md#rarfile) - RAR archive reader for Python
- [reedsolo](communications.md#reedsolo) - Pure-Python Reed Solomon encoder/decoder
- [cmeel](software-development-build-tools.md#cmeel) - Create Wheel from CMake projects
- [yarg](software-development-libraries-2.md#yarg) - A semi hard Cornish cheese, also queries PyPI (PyPI client)
- [extension-helpers](software-development-build-tools.md#extension-helpers) - Utilities for building and installing packages with compiled extensions
- [bindep](software-development-quality-assurance.md#bindep) - Binary dependency utility
- [ovh](software-development-libraries-2.md#ovh) - "Official module to perform HTTP requests to the OVHcloud APIs"
- [pyminizip](software-development-libraries-2.md#pyminizip) - A minizip wrapper - To create a password encrypted zip file in python.
- [xpress9](software-development-libraries-2.md#xpress9) - Python bindings for the Xpress9 compression library
- [indexed-zstd](software-development-libraries-2.md#indexed-zstd) - Fast random access to zstd files
- [rapidgzip](software-development-libraries-2.md#rapidgzip) - Parallel random access to gzip files
- [deflate](software-development-libraries-2.md#deflate) - Python wrapper for libdeflate.
- [xpress8](software-development-libraries-3.md#xpress8) - Python bindings for the Microsoft Xpress8 (ESE) compression library
- [blosc](software-development-libraries-3.md#blosc) - Blosc data compressor
- [bz2file](software-development-libraries-3.md#bz2file) - Read and write bzip2-compressed files.
- [arcp](internet.md#arcp) - arcp (Archive and Package) URI parser and generator
- [mda-xdrlib](software-development-libraries-3.md#mda-xdrlib) - Stand-alone XDRLIB module (from cpython 3.10.8)
- [rocrate](internet.md#rocrate) - RO-Crate metadata generator/parser
- [django-dbbackup](database.md#django-dbbackup) - Management commands to help backup and restore a project database and media.
- [venv-pack](software-development-build-tools.md#venv-pack) - Package virtual environments for redistribution
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [abx-dl](internet-www-http.md#abx-dl) - All-in-one CLI tool to download and extract content from URLs
- [dirsync](desktop-environment.md#dirsync) - Advanced directory tree synchronisation tool
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [conda-pack](software-development-build-tools.md#conda-pack) - Package conda environments for redistribution
- [indexed-bzip2](software-development-libraries-3.md#indexed-bzip2) - Fast random access to bzip2 files
- [setuptools-dso](software-development-libraries-4.md#setuptools-dso) - setuptools extension to build non-python shared libraries
- [redis-dump-load](database.md#redis-dump-load) - Dump and load redis databases
- [shippinglabel](software-development-libraries-4.md#shippinglabel) - Utilities for handling packages.
- [handy-archives](software-development-libraries-4.md#handy-archives) - Some handy archive helpers for Python.
- [dist-meta](software-development-libraries-4.md#dist-meta) - Parse and create Python distribution metadata.
- [rpm-vercmp](software-development-build-tools.md#rpm-vercmp) - Pure Python implementation of rpmvercmp
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
- [archivebox](internet-www-http-2.md#archivebox) - Self-hosted internet archiving solution.
- [mpyq](games-entertainment-real-time-strategy.md#mpyq) - A Python library for extracting MPQ (MoPaQ) files.
- [pyproject-parser](software-development-libraries-4.md#pyproject-parser) - Parser for 'pyproject.toml'
- [zipencrypt](software-development-libraries-5.md#zipencrypt) - Encryption for zipfile
- [borgbackup](security-cryptography.md#borgbackup) - Deduplicated, encrypted, authenticated and compressed backups
