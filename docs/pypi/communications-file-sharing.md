# Communications / File Sharing

[Index](README.md) · 10 packages in this topic, by downloads.

### pysmb

pysmb is an experimental SMB/CIFS library written in Python to support file sharing between Windows and Linux machines

`pip install pysmb` · installs (wheel) · licence: zlib/libpng License · rank 2198 · last release 2026-08-08 · [PyPI](https://pypi.org/project/pysmb/)

<details><summary>README extract</summary>

pysmb is an experimental SMB/CIFS library written in Python. It implements the client-side SMB/CIFS protocol which allows your Python application to access and transfer files to/from SMB/CIFS shared folders like your Windows file sharing and Samba folders.

</details>

### tuspy

A Python client for the tus resumable upload protocol -> http://tus.io

`pip install tuspy` · installs (wheel) · licence: MIT License · rank 2437 · last release 2024-11-29 · [PyPI](https://pypi.org/project/tuspy/)

<details><summary>README extract</summary>

> tus is a protocol based on HTTP for _resumable file uploads. Resumable
> means that an upload can be interrupted at any moment and can be resumed without
> re-uploading the previous data again. An interruption may happen willingly, if
> the user wants to pause, or by accident in case of a network issue or server
> outage. ...

Example:
```python
from tusclient import client

# Set Authorization headers if it is required
# by the tus server.
my_client = client.TusClient('
                              headers={'Authorization': 'Basic xxyyZZAAbbCC='})

# Set more headers.
my_client.set_headers({'HEADER_NAME': 'HEADER_VALUE'})

...
```

Sections: tus-py-client, Documentation, Get started

</details>

### bitmath

Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)

`pip install bitmath` · installs (wheel) · licence: MIT License · rank 7178 · last release 2026-05-25 · [PyPI](https://pypi.org/project/bitmath/)

<details><summary>README extract</summary>

* Free software: MIT License

bitmath simplifies many
facets of interacting with file sizes in various units. Originally
focusing on file size unit conversion, functionality now includes: ...

Example:
```python
>>> import bitmath
>>> log_size = bitmath.kB(137.4)
>>> log_zipped_size = bitmath.Byte(987)
>>> print("Compression saved %s space" % (log_size - log_zipped_size))
Compression saved 136.413kB space
>>> thumb_drive = bitmath.GiB(12)
>>> song_size = bitmath.MiB(5)
>>> songs_per_drive = thumb_drive / song_size
>>> print(songs_per_drive)
2457.6
```

Sections: bitmath, Documentation, Examples, Arithmetic, Capacity Planning, Convert Units, Select a human-readable unit, Rich Comparison, Sorting, Custom Formatting, Utility Functions, Formatting, `argparse` Integration

</details>

### bagit

Create and validate BagIt packages

`pip install bagit` · installs from source (sdist only) · licence: Public Domain · rank 8500 · last release 2025-06-13 · [PyPI](https://pypi.org/project/bagit/)

<details><summary>README extract</summary>

bagit is a Python library and command line utility for working with
BagIt style packages.

Example:
```python
bag = bagit.make_bag('mydir', {'Contact-Name': 'John Kunze'})
```

Sections: bagit-python, Command Line Usage, Finding Bagit on your system, Configuring BagIt, Using BagIt in your programs, Create, Update Bag Metadata, Update Bag Manifests, Validation, Running the tests, Benchmarks

</details>

### servestatic

Production-grade static file server for Python WSGI & ASGI.

`pip install servestatic` · installs (wheel) · licence: MIT · rank 8919 · last release 2026-10-02 · [PyPI](https://pypi.org/project/servestatic/) · [docs](https://archmonger.github.io/ServeStatic/) · [source](https://github.com/Archmonger/ServeStatic)

<details><summary>README extract</summary>

`ServeStatic` simplifies static file serving with minimal lines of configuration. It enables you to create a self-contained unit without requiring external services like Nginx or Amazon S3. This can simplify any production deployment, but is especially useful for platforms like Heroku, OpenShift, and other PaaS providers. ...

Example:
```python
# filename: my_project.py
from servestatic import ServeStaticASGI

asgi_app = ServeStaticASGI(
    application=None,  # `application=None` will run ServeStatic in standalone mode.
    root="/path/to/static/files",
)
```

Sections: ServeStatic, Quick Start, Frequently Asked Questions

</details>

### qbittorrent-api

Python client for qBittorrent v4.1+ Web API.

`pip install qbittorrent-api` · installs (wheel) · licence: MIT · rank 9726 · last release 2026-10-21 · [PyPI](https://pypi.org/project/qbittorrent-api/) · [docs](https://qbittorrent-api.readthedocs.io/) · [source](https://github.com/rmartin16/qbittorrent-api)

<details><summary>README extract</summary>

Python client implementation for qBittorrent Web API

Currently supports qBittorrent v5.3.0 (Web API v2.16.2) released on October 20, 2026.

User Guide and API Reference available on Read the Docs.

Features

* The entire qBittorrent Web API is implemented. ...

Example:
```python
import qbittorrentapi

# instantiate a Client using the appropriate WebUI configuration
conn_info = dict(
    host="localhost",
    port=8080,
    username="admin",
    password="adminadmin",
)
qbt_client = qbittorrentapi.Client(**conn_info)

# the Client will automatically acquire/maintain a logged-in state
...
```

...

</details>

### bagit-profile

This module can be used to validate BagitProfiles.

`pip install bagit-profile` · installs (wheel) · licence: Public Domain · rank 12351 · last release 2020-03-24 · [PyPI](https://pypi.org/project/bagit-profile/)

<details><summary>README extract</summary>

A simple Python module for validating BagIt profiles. See the BagIt
Profiles Specification
for more information.

This module is intended for use with
bagit-python but does not extend it.

Example:
```python
import bagit
import bagit_profile
```

Sections: Bagit Profile (validator), Description, Usage, Test suite

</details>

### py3-wget

A tool to download files. It supports progress bar, cksum, timeout, retry failed download.

`pip install py3-wget` · installs (wheel) · licence: MIT License · rank 12818 · last release 2025-07-26 · [PyPI](https://pypi.org/project/py3-wget/) · [source](https://github.com/gmberton/py3-wget)

<details><summary>README extract</summary>

A Python library for downloading files of any size, especially optimized for large file downloads, with support for progress bars, checksum verification, timeout handling, and automatic retry on failed downloads.

Features:
- 🚀 Optimized for large file downloads
- 📊 Progress bar visualization (optional)
- 🔄 Automatic retry on failed downloads
- 🔍 Optional integrity checks (cksum, MD5, SHA256)
- ⏱️ Configurable timeout and retry settings ...

Example:
```python
from py3_wget import download_file

# Simple download with progress bar
download_file("
```

Sections: py3-wget, Features, Quick Start, Basic Download, Advanced Usage, Retry on Failure, Checksum Verification, File Overwrite Control, API Reference, `download_file`, Parameters

</details>

### transferit-py

Pure-Python client for transfer.it — upload and download files via the MEGA backend, no browser required.

`pip install transferit-py` · installs (wheel) · licence: MIT License · rank 13811 · last release 2026-04-20 · [PyPI](https://pypi.org/project/transferit-py/) · [docs](https://github.com/viperadnan-git/transferit-py#readme) · [source](https://github.com/viperadnan-git/transferit-py)

<details><summary>README extract</summary>

Upload and download files on transfer.it from Python or your terminal — no browser, no MEGA account, no external CLI tools.

- End-to-end encrypted — AES-128-CTR + CBC-MAC, identical scheme to the official web client.
- Concurrent WebSocket uploads — up to 8 connections per file, matching MEGA's `ulDefConcurrency`. ...

Example:
```python
from transferit import Transferit

with Transferit() as tx:
    url = tx.upload("report.pdf").url     # →
```

Sections: transferit, CLI, Library, Typed returns, Progress hooks, Defaults, Low-level, How it works, Disclaimer

</details>

### py3createtorrent

Create torrents via command line!

`pip install py3createtorrent` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 14940 · last release 2024-06-08 · [PyPI](https://pypi.org/project/py3createtorrent/) · [source](https://github.com/rsnitsch/py3createtorrent)

_README extract left out: share-alike licence._

