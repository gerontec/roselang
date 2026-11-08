# Internet / File Transfer Protocol (FTP)

[Index](README.md) · 5 packages in this topic, 3 more listed under another topic, by downloads.

### pycurl

PycURL -- A Python Interface To The cURL library

`pip install pycurl` · installs (wheel) · licence: LGPL-2.1-only OR MIT · rank 1846 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pycurl/) · [docs](https://pycurl.github.io/docs/latest/) · [source](https://github.com/pycurl/pycurl)

_README extract left out: share-alike licence._

### pyftpdlib

Very fast asynchronous FTP server library

`pip install pyftpdlib` · installs from source (sdist only) · licence: not stated · rank 4275 · last release 2026-02-07 · [PyPI](https://pypi.org/project/pyftpdlib/)

<details><summary>README extract</summary>

downloadsstarsforkscontributors|
versionpackageslicense|
github-actionsdoctwitter|

- Home
- Documentation
- Download
- Mailing list
- What's new

Python FTP server library provides a high-level portable interface to easily
write very efficient, scalable and asynchronous FTP servers with Python. ...

Features:
- Extremely lightweight, fast and scalable (see
 why and
 benchmarks).
- Uses sendfile(2) (see pysendfile)
 system call for uploads (Linux only).
- Uses `epoll()` / `kqueue()` / `select()` to handle concurrency
 asynchronously. ...

Example:
```python
>>> from pyftpdlib.authorizers import DummyAuthorizer
>>> from pyftpdlib.handlers import FTPHandler
>>> from pyftpdlib.servers import FTPServer
>>>
>>> authorizer = DummyAuthorizer()
...

</details>

### ftputil

High-level FTP client library (virtual file system and more)

`pip install ftputil` · installs (wheel) · licence: BSD-3-Clause · rank 5844 · last release 2026-04-25 · [PyPI](https://pypi.org/project/ftputil/)

<details><summary>README extract</summary>

ftputil is a high-level FTP client library for the Python programming
language. ftputil implements a virtual file system for accessing FTP servers,
that is, it can generate file-like objects for remote files. The library
supports many functions similar to those in the os, os.path and
shutil modules. ...

</details>

### aioftp

ftp client/server for asyncio

`pip install aioftp` · installs (wheel) · licence: not stated · rank 7023 · last release 2026-09-19 · [PyPI](https://pypi.org/project/aioftp/) · [docs](https://aioftp.rtfd.io) · [source](https://github.com/aio-libs/aioftp)

<details><summary>README extract</summary>

ftp client/server for asyncio (

Features:
- Simple.
- Extensible.
- Client socks proxy via siosocks
 (`pip install aioftp[socks]`).

Example:
```python
import asyncio
import aioftp

async def get_mp3(host, port, login, password):
    async with aioftp.Client.context(host, port, login, password) as client:
        for path, info in (await client.list(recursive=True)):
            if info["type"] == "file" and path.suffix == ".mp3":
                await client.download(path)

async def main():
...
```

Sections: aioftp, Features, Goals, Server benchmark, Dependencies, Getting started

</details>

### sftpserver

sftpserver - a simple single-threaded sftp server

`pip install sftpserver` · installs (wheel) · licence: MIT License · rank 7152 · last release 2017-04-09 · [PyPI](https://pypi.org/project/sftpserver/)

<details><summary>README extract</summary>

`sftpserver` is a simple single-threaded SFTP server based on
Paramiko's SFTPServer.

I needed a simple server that could be used as a stub for testing
Python SFTP clients so I whipped out one.

Sections: sftpserver, Examples

</details>

## Also in this topic

- [tuspy](communications-file-sharing.md#tuspy) - A Python client for the tus resumable upload protocol -> http://tus.io
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
