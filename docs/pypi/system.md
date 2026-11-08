# System

[Index](README.md) · 4 packages in this topic, 19 more listed under another topic, by downloads.

### filetype

Infer file type and MIME type of any file/buffer. No external dependencies.

`pip install filetype` · installs (wheel) · licence: MIT License · rank 518 · last release 2022-11-02 · [PyPI](https://pypi.org/project/filetype/)

<details><summary>README extract</summary>

Small and dependency free Python package to infer file type and MIME
type checking the magic numbers signature of a file or buffer.

This is a Python port from filetype Go package.

Features:
- Simple and friendly API
- Supports a wide range of file types
- Provides file extension and MIME type inference
- File discovery by extension or MIME type
- File discovery by kind (image, video, audio…)
- Pluggable: add new custom type matchers ...

Example:
```python
import filetype

def main():
    kind = filetype.guess('tests/fixtures/sample.jpg')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if name == 'main':
    main()
```

...

</details>

### uptime

Cross-platform uptime library

`pip install uptime` · installs from source (sdist only) · licence: BSD License · rank 7602 · last release 2013-10-07 · [PyPI](https://pypi.org/project/uptime/)

<details><summary>README extract</summary>

This module provides a cross-platform way to retrieve system uptime and boot time.
See documentation for a full list of supported platforms (yours is likely one of them).

</details>

### dllist

List the shared libraries loaded by the current process.

`pip install dllist` · installs (wheel) · licence: BSD License · rank 7979 · last release 2025-02-10 · [PyPI](https://pypi.org/project/dllist/)

<details><summary>README extract</summary>

> [!NOTE]
> This functionality is available in the standard library starting in Python 3.14

A very small Python library to list the DLLs loaded by the current process.
This is equivalent to the `dllist` function in Julia.

*Note*: This library is tested on macOS, Linux, and Windows.
Some platforms which provide the same API as Linux (e.g. ...

Example:
```python
import dllist
print(dllist.dllist())
# ['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libpthread.so.0', '/lib/x86_64-linux-gnu/libdl.so.2', ... ]
```

Sections: dllist, Usage

</details>

### hanziconv

Hanzi Converter for Traditional and Simplified Chinese

`pip install hanziconv` · installs from source (sdist only) · licence: Apache Software License · rank 11905 · last release 2016-09-01 · [PyPI](https://pypi.org/project/hanziconv/)

<details><summary>README extract</summary>

This tool converts between simplified and traditional Chinese Characters.
It consists of two parts:

 - a command line tool: `hanzi-convert`
 - a python library: `hanziconv`

This module supports both Python 2 and 3

Example:
```python
>>> from hanziconv import HanziConv
>>> print(HanziConv.toSimplified('繁簡轉換器'))
繁简转换器
>>> print(HanziConv.toTraditional('繁简转换器'))
繁簡轉換器
>>> HanziConv.same('繁簡轉換器', '繁简转换器')
True
```

Sections: Hanzi Converter 繁簡轉換器 | 繁简转换器, Command Line Tool, Synopsis, Example, Python API

</details>

## Also in this topic

- [filelock](software-development-libraries.md#filelock) - A platform independent file lock.
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [aiofile](software-development-libraries.md#aiofile) - Asynchronous file operations.
- [portalocker](software-development-libraries.md#portalocker) - Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [tox-uv-bare](software-development-libraries.md#tox-uv-bare) - Integration of uv with tox (bare package, bring your own uv).
- [cysignals](software-development-debuggers.md#cysignals) - Interrupt and signal handling for Cython
- [verboselogs](software-development.md#verboselogs) - Verbose logging level for Python's logging module
- [toml-fmt-common](internet.md#toml-fmt-common) - Common logic to the TOML formatter.
- [pyClamd](security.md#pyclamd) - pyClamd is a python interface to Clamd (Clamav daemon).
- [scikit-learn-intelex](scientific-engineering.md#scikit-learn-intelex) - Intel® Extension for Scikit-learn is a seamless way to speed up your Scikit-learn application.
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [docplex](other-nonlisted-topic.md#docplex) - The IBM Decision Optimization CPLEX Modeling for Python
- [status](internet.md#status) - HTTP status code reporting for GET and POST requests
- [daal4py](scientific-engineering-2.md#daal4py) - daal4py is a Convenient Python API to the Intel® oneAPI Data Analytics Library (oneDAL)
- [cosmpy](software-development.md#cosmpy) - A library for interacting with the cosmos networks
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
