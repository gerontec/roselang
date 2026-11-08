# System / Filesystems

[Index](README.md) · 10 packages in this topic, 37 more listed under another topic, by downloads.

### scandir

scandir, a better directory iterator and faster os.walk()

`pip install scandir` · installs from source (sdist only) · licence: BSD License · rank 2837 · last release 2019-03-09 · [PyPI](https://pypi.org/project/scandir/)

<details><summary>README extract</summary>

`scandir()` is a directory iteration function like `os.listdir()`,
except that instead of returning a list of bare filenames, it yields
`DirEntry` objects that include file type and stat information along
with the name. ...

Example:
```python
# Use the built-in version of scandir/walk if possible, otherwise
# use the scandir module version
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk
```

Sections: scandir, a better directory iterator and faster os.walk(), Now included in a Python near you!, Background, Benchmarks, The API, walk(), scandir(), Further reading, Flames, comments, bug reports

</details>

### win32-setctime

A small Python utility to set file creation time on Windows

`pip install win32-setctime` · installs (wheel) · licence: MIT License · rank 2852 · last release 2026-10-25 · [PyPI](https://pypi.org/project/win32-setctime/)

<details><summary>README extract</summary>

A small Python utility to set file creation time on Windows.

Example:
```python
from win32_setctime import setctime

setctime("my_file.txt", 1561675987.509, follow_symlinks=True)
```

Sections: win32-setctime, Usage

</details>

### gsutil

A command line tool for interacting with cloud storage services.

`pip install gsutil` · installs from source (sdist only) · licence: Apache Software License · rank 3041 · last release 2026-10-21 · [PyPI](https://pypi.org/project/gsutil/)

<details><summary>README extract</summary>

gsutil is a Python application that lets you access Google Cloud Storage from
the command line. You can use gsutil to do a wide range of bucket and object
management tasks, including:
 * Creating and deleting buckets.
 * Uploading, downloading, and deleting objects.
 * Listing buckets and objects.
 * Moving, copying, and renaming objects. ...

</details>

### fs

Python's filesystem abstraction layer

`pip install fs` · installs (wheel) · licence: MIT License · rank 3973 · last release 2022-05-02 · [PyPI](https://pypi.org/project/fs/) · [docs](https://pyfilesystem2.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Python's Filesystem abstraction layer.

- Wiki
- API Documentation
- GitHub Repository
- Blog

Think of PyFilesystem's `FS` objects as the next logical step to
Python's `file` objects. In the same way that file objects abstract a
single file, FS objects abstract an entire filesystem.

Let's look at a simple piece of code as an example. ...

Example:
```python
def count_python_loc(fs):
    """Count non-blank lines of Python code."""
    count = 0
    for path in fs.walk.files(filter=['*.py']):
        with fs.open(path) as python_file:
            count += sum(1 for line in python_file if line.strip())
    return count
```

Sections: PyFilesystem2, Documentation, Introduction

</details>

### pywatchman

Watchman client for Python

`pip install pywatchman` · installs from source (sdist only) · licence: MIT License · rank 5183 · last release 2026-06-12 · [PyPI](https://pypi.org/project/pywatchman/)

<details><summary>README extract</summary>

This directory contains the Watchman client for Python.

Sections: Watchman client for Python, Build

</details>

### fusepy

Simple ctypes bindings for FUSE

`pip install fusepy` · installs from source (sdist only) · licence: ISC License (ISCL) · rank 5989 · last release 2018-09-17 · [PyPI](https://pypi.org/project/fusepy/)

<details><summary>README extract</summary>

NOTE: *This project has moved to be under a GitHub organization and can
 be found at The project has new
 maintainers and will be looking to incorporate pull requests in a more
 timely manner. ...

Sections: fusepy, examples

</details>

### appdata

Utils to manage application data folder.

`pip install appdata` · installs (wheel) · licence: MIT · rank 7671 · last release 2023-12-26 · [PyPI](https://pypi.org/project/appdata/)

<details><summary>README extract</summary>

Example:
```python
from appdata import AppDataPaths

app_paths = AppDataPaths('myapp')  # Name is optional. By default CWD folder name is used.
```

Sections: appdata | Application Data Management, Documentation, Usage

</details>

### oschmod

Consistent chmod-style file permissions on Windows, macOS, and Linux

`pip install oschmod` · installs (wheel) · licence: Apache-2.0 · rank 9103 · last release 2026-10-29 · [PyPI](https://pypi.org/project/oschmod/)

<details><summary>README extract</summary>

*oschmod* sets consistent file permissions across Windows, Linux and macOS.

*oschmod* brings `chmod` functionality to Windows, macOS, and Linux! If you're not familiar, `chmod` is a handy macOS and Linux-only tool for setting file permissions.

Prior to *oschmod*, Windows file permissions couldn't be set in the familiar `chmod` way. ...

Example:
```python
import oschmod

oschmod.set_mode("myfile", "a+rwx,g-w,o-x")
```

Sections: oschmod, oschmod TL;DR, GNU Documentation, Command line interface, Command line examples, Symbolic representation examples, Octal representation examples, Verbose output, Recursion and symlinks, Python usage, Creating private files, Windows notes

</details>

### mfusepy

Ctypes bindings for the high-level API in libfuse 2 and 3

`pip install mfusepy` · installs (wheel) · licence: ISC · rank 10104 · last release 2026-03-13 · [PyPI](https://pypi.org/project/mfusepy/)

<details><summary>README extract</summary>

`mfusepy` is a Python module that provides a simple interface to FUSE and macFUSE.
It's just one file and is implemented using `ctypes` to use libfuse.

Sections: mfusepy, Versioning, About this fork, Comparison with other libraries, Examples, Platforms, Known Dependents

</details>

### fs-s3fs

Amazon S3 filesystem for PyFilesystem2

`pip install fs-s3fs` · installs (wheel) · licence: MIT License · rank 11005 · last release 2019-08-14 · [PyPI](https://pypi.org/project/fs-s3fs/)

<details><summary>README extract</summary>

S3FS is a PyFilesystem interface to
Amazon S3 cloud storage.

As a PyFilesystem concrete class,
S3FS allows you to work
with S3 in the same way as any other supported filesystem.

Example:
```python
from fs_s3fs import S3FS
s3fs = S3FS('mybucket')
```

Sections: S3FS, Opening a S3FS, Downloading Files, Uploading Files, ExtraArgs, S3 URLs, Documentation

</details>

## Also in this topic

- [watchfiles](software-development-libraries.md#watchfiles) - Simple, modern and high performance file watching and code reload in python.
- [watchdog](software-development-libraries.md#watchdog) - Filesystem events monitoring
- [portalocker](software-development-libraries.md#portalocker) - Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks
- [filetype](system.md#filetype) - Infer file type and MIME type of any file/buffer. No external dependencies.
- [pathvalidate](software-development-libraries.md#pathvalidate) - pathvalidate is a Python library to sanitize/validate a string such as filenames/file-paths/etc.
- [flexparser](software-development-libraries.md#flexparser) - Parsing made fun ... using typing.
- [flexcache](software-development-libraries.md#flexcache) - Saves and loads to the cache a transformed versions of a source object.
- [pathlib](software-development-libraries.md#pathlib) - Object-oriented filesystem paths
- [pathlib2](software-development-libraries.md#pathlib2) - Object-oriented filesystem paths
- [pyfakefs](software-development-libraries.md#pyfakefs) - Implements a fake file system that mocks the Python file system modules.
- [fcache](software-development-libraries.md#fcache) - a dictionary-like, file-based cache module for Python
- [dohq-artifactory](software-development-libraries-2.md#dohq-artifactory) - A Python interface to Artifactory
- [pyinotify](software-development-libraries-2.md#pyinotify) - Linux filesystem events monitoring
- [pyftpdlib](internet-file-transfer-protocol-ftp.md#pyftpdlib) - Very fast asynchronous FTP server library
- [python-fsutil](desktop-environment-file-managers.md#python-fsutil) - high-level file-system operations for lazy devs.
- [python-benedict](education-testing.md#python-benedict) - python-benedict is a dict subclass with keylist/keypath/keyattr support, normalized I/O operations (base64, csv, ini, json, pickle, plist, query-string, toml, xls, xml, yaml) and many utilities... for humans, obviously.
- [ftputil](internet-file-transfer-protocol-ftp.md#ftputil) - High-level FTP client library (virtual file system and more)
- [littlefs-python](scientific-engineering.md#littlefs-python) - A python wrapper for littlefs
- [lasio](scientific-engineering.md#lasio) - Read/write well data from Log ASCII Standard (LAS) files
- [watchgod](software-development-libraries-3.md#watchgod) - Simple, modern file watching and code reload in python.
- [pathtools](software-development-libraries-3.md#pathtools) - File system general utilities
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [fatfs-ng](scientific-engineering.md#fatfs-ng) - Enhanced Python wrapper around ChaN's FatFS library - Fork of fatfs-python with extended features.
- [hachoir](multimedia.md#hachoir) - Package of Hachoir parsers used to open binary files
- [PyArtifactory](software-development-libraries-3.md#pyartifactory) - Typed interactions with the Jfrog Artifactory REST API
- [bagit](communications-file-sharing.md#bagit) - Create and validate BagIt packages
- [ipfshttpclient](internet.md#ipfshttpclient) - Python IPFS HTTP CLIENT library
- [universal-startfile](desktop-environment-file-managers.md#universal-startfile) - A cross-platform version of 'os.startfile' from the standard library.
- [artifactory](software-development-libraries-3.md#artifactory) - A Python to Artifactory interface
- [YORM](database.md#yorm) - Automatic object-YAML mapping for Python.
- [ayafileio](software-development-libraries-3.md#ayafileio) - Cross-platform async file API for Python. Blazing fast like Shameimaru Aya.
- [rleveldb](database.md#rleveldb) - LevelDB reader for Python — Rust core with PyO3 bindings
- [fspath](software-development-libraries-4.md#fspath) - semantic path names and more
- [bagit-profile](communications-file-sharing.md#bagit-profile) - This module can be used to validate BagitProfiles.
- [pyfatfs](software-development-libraries-4.md#pyfatfs) - FAT12/FAT16/FAT32 implementation with VFAT support
- [PySmbClient](software-development-libraries-4.md#pysmbclient) - A convenient smbclient wrapper
- [PySquashfsImage](software-development-libraries-5.md#pysquashfsimage) - Squashfs image parser
