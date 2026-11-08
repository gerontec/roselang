# Software Development / Debuggers

[Index](README.md) · 36 packages in this topic, 18 more listed under another topic, by downloads.

### stack-data

Extract data from python stack frames and tracebacks for informative displays

`pip install stack-data` · installs (wheel) · licence: MIT License · rank 292 · last release 2023-09-30 · [PyPI](https://pypi.org/project/stack-data/)

<details><summary>README extract</summary>

This is a library that extracts data from stack frames and tracebacks, particularly to display more useful tracebacks than the default. It powers the tracebacks in IPython and futurecoder:

You can install it from PyPI:

 pip install stack_data

Example:
```python
def foo():
    result = []
    for i in range(5):
        row = []
        result.append(row)
        print_stack()
        for j in range(5):
            row.append(i * j)
    return result
```

Sections: stack_data, Basic usage, Variables, Rendering lines with ranges and markers, Syntax highlighting with Pygments, Getting the full stack

</details>

### debugpy

An implementation of the Debug Adapter Protocol for Python

`pip install debugpy` · installs (wheel) · licence: MIT License · rank 305 · last release 2026-09-15 · [PyPI](https://pypi.org/project/debugpy/) · [source](https://github.com/microsoft/debugpy)

<details><summary>README extract</summary>

debugpy is an implementation of the Debug Adapter Protocol for Python.

The source code and the issue tracker is hosted on GitHub.

</details>

### pylint

python code static checker

`pip install pylint` · installs (wheel) · licence: GPL-2.0-or-later · rank 534 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pylint/) · [source](https://github.com/pylint-dev/pylint)

_README extract left out: share-alike licence._

### ipdb

IPython-enabled pdb

`pip install ipdb` · installs (wheel) · licence: BSD License · rank 1068 · last release 2023-03-09 · [PyPI](https://pypi.org/project/ipdb/)

<details><summary>README extract</summary>

ipdb exports functions to access the IPython debugger, which features
tab completion, syntax highlighting, better tracebacks, better introspection
with the same interface as the `pdb` module.

Example usage:

Example:
```python
import ipdb
ipdb.set_trace()
ipdb.set_trace(context=5)  # will show five lines of code
                           # instead of the default three lines
                           # or you can set it via IPDB_CONTEXT_SIZE env variable
                           # or setup.cfg file
ipdb.pm()
ipdb.run('x[0] = 3')
...
```

...

</details>

### memray

A memory profiler for Python applications

`pip install memray` · installs (wheel) · licence: Apache Software License · rank 1168 · last release 2026-08-07 · [PyPI](https://pypi.org/project/memray/)

<details><summary>README extract</summary>

Memray is a memory profiler for Python. It can track memory allocations in Python code, in native extension
modules, and in the Python interpreter itself. It can generate several different types of reports to help you
analyze the captured memory usage data. ...

Example:
```python
@pytest.mark.limit_memory("24 MB")
def test_foobar():
    # do some stuff that allocates memory
```

Sections: Help us improve Memray!, Building from source, Documentation, Usage, Pytest plugin, Native mode, Live mode, Sorting results, Viewing different threads, API, Steps

</details>

### pyinstrument

Call stack profiler for Python. Shows you why your code is slow!

`pip install pyinstrument` · installs (wheel) · licence: BSD License · rank 1334 · last release 2026-07-29 · [PyPI](https://pypi.org/project/pyinstrument/)

<details><summary>README extract</summary>

Documentation

<!-- MARK intro start -->

Pyinstrument is a Python profiler. A profiler is a tool to help you optimize
your code - make it faster. To get the biggest speed increase you should
focus on the slowest part of your program.
Pyinstrument helps you find it!

> ☕️ Not sure where to start? Check out this video tutorial from calmcode.io! ...

Example:
```python
import asyncio
from pyinstrument import Profiler

async def main():
    p = Profiler(async_mode='disabled')

    with p:
        print('Hello ...')
        await asyncio.sleep(1)
        print('... World!')

    p.print()

asyncio.run(main())
```

Sections: pyinstrument, v5.1.3, v5.1.2, v5.1.1, v5.1.0, v5.0.3, v5.0.2, v5.0.1, v5.0.0, v4.7.3, v4.7.2, v4.7.1, v4.7.0, v4.6.2

</details>

### pytest-memray

A simple plugin to use with pytest

`pip install pytest-memray` · installs (wheel) · licence: Apache-2.0 · rank 2776 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pytest-memray/) · [docs](https://pytest-memray.readthedocs.io) · [source](https://github.com/bloomberg/pytest-memray)

<details><summary>README extract</summary>

pytest-memray is a pytest plugin for easy integration of
memray.

Sections: pytest-memray, Documentation, Quick introduction, Configuration - CLI flags, Configuration - INI, Steps

</details>

### circular-dict

CircularDict is a high-performance Python data structure that blends the functionality of dictionaries and circular buffers. Inheriting the usage of traditional dictionaries, it allows you to define constraints on size and memory usage. This way, the CircularDict will be always up-to-date with the last N added elements, ensuring that neither the maximum length nor the memory usage limit is exceeded. It is ideal for caching large data structures while maintaining control over memory footprint.

`pip install circular-dict` · installs (wheel) · licence: MIT License · rank 3436 · last release 2024-05-12 · [PyPI](https://pypi.org/project/circular-dict/)

<details><summary>README extract</summary>

CircularDict is a Python `dict` that acts as a Circular Buffer. This dictionary maintains a controlled size, limited either by a specified number of items (_maxlen_) or total size in bytes (_maxsize_bytes_). Upon reaching the defined limit, CircularDict automatically removes the oldest entries, maintaining memory usage under control. ...

Example:
```python
from circular_dict import CircularDict
# Initialize a CircularDict with a maximum length of 3 items and a storage limit of 4Mb
my_dict = CircularDict(maxlen=3, maxsize_bytes=4*1024*1024)
```

Sections: CircularDict, Usage, Example with `maxlen`, Example with `maxsize_bytes`

</details>

### pydevd

PyDev.Debugger (used in PyDev, PyCharm and VSCode Python)

`pip install pydevd` · installs from source (sdist only) · licence: Eclipse Public License 1.0 (EPL-1.0) · rank 3506 · last release 2026-04-02 · [PyPI](https://pypi.org/project/pydevd/)

<details><summary>README extract</summary>

Latest `3.x` version: the PyDev debugger now supports `sys.monitoring` which enables
really fast tracing on `Python 3.12` (so, if speed is an issue, make sure you upgrade).

 is the main repository
for `pydevd` and the latest versions can always be used directly in:

- PyDev for Eclipse: Enables the usage of `pydevd` in Eclipse (Open Source). ...

Sections: PyDev.Debugger, New, Important, Source code / using

</details>

### pdbpp

pdb++, a drop-in replacement for pdb

`pip install pdbpp` · installs (wheel) · licence: BSD-3-Clause · rank 3684 · last release 2026-02-23 · [PyPI](https://pypi.org/project/pdbpp/) · [source](https://github.com/bretello/pdbpp)

<details><summary>README extract</summary>

This module is an extension of the pdb module of the standard library. It is
meant to be fully compatible with its predecessor, yet it introduces a number
of new features to make your debugging experience as nice as possible.

`pdb++` features include:

 - colorful TAB completion of Python expressions (through fancycompleter) ...

Example:
```python
(Pdb) list
  1
  2     def fn():
  3         c = 42
  4         import pdb;pdb.set_trace()
  5  ->     return c
(Pdb) c
```

Sections: pdb++, a drop-in replacement for pdb, What is it?, Usage, New interactive commands, Smart command parsing, Additional functions in the `pdb` module, Configuration and customization, Notes on color options, Coding guidelines

</details>

### traceback-with-variables

Adds variables to python traceback. Simple, lightweight, controllable. Debug reasons of exceptions by logging or pretty printing colorful variable contexts for each frame in a stacktrace, showing every value. Dump locals environments after errors to console, files, and loggers. Works with Jupyter and IPython.

`pip install traceback-with-variables` · installs (wheel) · licence: MIT License · rank 4308 · last release 2025-10-24 · [PyPI](https://pypi.org/project/traceback-with-variables/)

<details><summary>README extract</summary>

Very simple to use and fast, but versatile when needed. Try for debug and keep for small-scale production.

> “It is useless work that darkens the heart.”
> – Ursula K. Le Guin

Tired of useless job of putting all your variables into debug exception messages? Just stop it.
Automate it and clean your code. Once and for all. ...

Example:
```python
from traceback_with_variables import activate_by_import
```

Sections: Python Traceback (Error Message) Printing Variables, 🚀 Quick Start, Colors, How does it save my time?, Examples and recipes, Reference, `activate_by_import`, `activate_in_ipython_by_import`, `global_print_exc`, `global_print_exc_in_ipython`, `print_exc`, `print_cur_tb`, `prints_exc`, `printing_exc`

</details>

### frida

Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers

`pip install frida` · installs (wheel) · licence: OSI Approved · rank 4787 · last release 2026-11-07 · [PyPI](https://pypi.org/project/frida/)

### tracerite

Human-readable HTML tracebacks for Python exceptions

`pip install tracerite` · installs (wheel) · licence: MIT License; Public Domain · rank 4886 · last release 2026-08-18 · [PyPI](https://pypi.org/project/tracerite/) · [source](https://github.com/sanic-org/tracerite)

<details><summary>README extract</summary>

Fixing bugs is easier with well formatted error messages. Console, HTML and JSON.

*TraceRite formats Python errors in Jupyter notebooks, in plain HTML, and in the terminal: rich variable inspection (left), plus syntax-error highlighting and compact terminal tracebacks (right).*

Features:
- Chronological order - Single timeline with the program entry point is at top, and the finally uncaught exception bottom.
- Minimalistic output - Smart pruning to show only relevant pieces of information, excluding library internals where not ...

Example:
```python
import tracerite; tracerite.load()
```

...

</details>

### pydevd-pycharm

PyCharm Debugger (used in PyCharm and PyDev)

`pip install pydevd-pycharm` · installs from source (sdist only) · licence: Apache 2.0 · rank 5034 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pydevd-pycharm/)

<details><summary>README extract</summary>

PyCharms' fork of PyDev.Debugger.

Sections: PyDev.Debugger, Compatibility, Dependencies, Tests

</details>

### cysignals

Interrupt and signal handling for Cython

`pip install cysignals` · installs (wheel) · licence: LGPL-3.0-or-later · rank 5601 · last release 2026-10-02 · [PyPI](https://pypi.org/project/cysignals/)

_README extract left out: share-alike licence._

### frida-tools

Frida CLI tools

`pip install frida-tools` · installs (wheel) · licence: LGPL-2.0-or-later WITH WxWindows-exception-3.1 · rank 5896 · last release 2026-11-06 · [PyPI](https://pypi.org/project/frida-tools/) · [source](https://github.com/frida/frida-tools)

_README extract left out: share-alike licence._

### PySnooper

A poor man's debugger for Python.

`pip install PySnooper` · installs (wheel) · licence: MIT License · rank 6141 · last release 2025-05-31 · [PyPI](https://pypi.org/project/PySnooper/)

<details><summary>README extract</summary>

PySnooper is a poor man's debugger. If you've used Bash, it's like `set -x` for Python, except it's fancier.

Your story: You're trying to figure out why your Python code isn't doing what you think it should be doing. You'd love to use a full-fledged debugger with breakpoints and watches, but you can't be bothered to set one up right now. ...

Features:
If stderr is not easily accessible for you, you can redirect the output to a file:

You can also pass a stream or a callable instead, and they'll be used.

See values of some expressions that aren't local variables: ...

Example:
```python
import pysnooper

@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
...

</details>

### xdis

Python cross-version byte-code disassembler and marshal routines

`pip install xdis` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 6620 · last release 2026-03-30 · [PyPI](https://pypi.org/project/xdis/)

_README extract left out: share-alike licence._

### lauterbach-trace32-rcl

Lauterbach TRACE32 Python Remote Control Library

`pip install lauterbach-trace32-rcl` · installs (wheel) · licence: MIT License · rank 6776 · last release 2026-07-02 · [PyPI](https://pypi.org/project/lauterbach-trace32-rcl/) · [docs](https://pyrcl.readthedocs.io) · [source](https://gitlab.com/lauterbach/pyrcl)

<details><summary>README extract</summary>

Sections: pyrcl, v1.1.6, v1.1.5, v1.1.4, v1.1.3, v1.1.2, v1.1.1, v1.1.0, v1.0.10, v1.0.9, v1.0.8, v1.0.7, v1.0.6, v1.0.5

</details>

### ptvsd

Remote debugging server for Python support in Visual Studio and Visual Studio Code

`pip install ptvsd` · installs (wheel) · licence: Eclipse Public License 2.0 (EPL-2.0); MIT License · rank 6792 · last release 2019-08-13 · [PyPI](https://pypi.org/project/ptvsd/)

<details><summary>README extract</summary>

The Python Visual Studio Debugger engine implements the Visual Studio Code debug protocol and is used as the debug engine in Visual Studio and Visual Studio Code.

The source code and the issue tracker is hosted on GitHub.

</details>

### guppy3

Guppy 3 -- Guppy-PE ported to Python 3

`pip install guppy3` · installs (wheel) · licence: MIT · rank 6976 · last release 2026-11-06 · [PyPI](https://pypi.org/project/guppy3/)

<details><summary>README extract</summary>

A Python Programming Environment & Heap analysis toolset.

This package contains the following subpackages:
* etc - Support modules. Contains especially the Glue protocol module.
* gsl - The Guppy Specification Language implementation. This can be used
 to create documents and tests from a common source.
* heapy - The heap analysis toolset. ...

Example:
```python
>>> from guppy import hpy; h=hpy()
>>> h.heap()
Partition of a set of 30976 objects. Total size = 3544220 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0   8292  27   739022  21    739022  21 str
     1   7834  25   625624  18   1364646  39 tuple
     2   2079   7   300624   8   1665270  47 types.CodeType
...
```

Sections: Guppy 3, Requirements, Freethreading, Usage

</details>

### pystack

Analysis of the stack of remote python processes

`pip install pystack` · installs (wheel) · licence: Apache Software License · rank 7820 · last release 2026-09-24 · [PyPI](https://pypi.org/project/pystack/)

<details><summary>README extract</summary>

______________

> Print the stack trace of a running Python process, or of a Python core dump.

PyStack is a tool that uses forbidden magic to let you inspect the stack frames of a running Python
process or a Python core dump, helping you quickly and easily learn what it's doing (or what it was
doing when it crashed) without having to interpret ...

Sections: PyStack, What PyStack can do, Building from source, Documentation, Usage, Analyzing running processes, Analyzing core dumps, Steps

</details>

### pyvalid

The module, which allows easily validate function's input/output values.

`pip install pyvalid` · installs (wheel) · licence: MIT License · rank 7925 · last release 2020-10-13 · [PyPI](https://pypi.org/project/pyvalid/)

<details><summary>README extract</summary>

pyvalid is a Python data validation tool.

Documentation: uzumaxy.github.io/pyvalid.

</details>

### aiocop

Non-intrusive monitoring for Python asyncio and uvloop. Detects, pinpoints, and logs blocking IO and CPU calls that freeze your event loop.

`pip install aiocop` · installs (wheel) · licence: MIT License · rank 8237 · last release 2026-10-15 · [PyPI](https://pypi.org/project/aiocop/)

<details><summary>README extract</summary>

Non-intrusive monitoring for Python asyncio.

 Detects, pinpoints, and logs blocking IO and CPU calls that freeze your event loop.

Features:
* Production-Safe & Low Overhead: Leverages Python's `sys.audit` hooks for minimal runtime overhead, making it safe for production use
* Works with asyncio and uvloop: Compatible with both standard asyncio and uvloop event loops out of the box
* ...

Example:
```python
# test_aiocop.py
import asyncio
import aiocop

def on_slow_task(event):
    print(f"SLOW TASK DETECTED: {event.elapsed_ms:.1f}ms")
    print(f"  Severity: {event.severity_level}")
    for evt in event.blocking_events:
        print(f"  - {evt['event']} at {evt['entry_point']}")

async def blocking_task():
...
```

...

</details>

### pylint-odoo

Pylint plugin for Odoo

`pip install pylint-odoo` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 8841 · last release 2026-10-05 · [PyPI](https://pypi.org/project/pylint-odoo/)

_README extract left out: share-alike licence._

### uncompyle6

Python cross-version byte-code decompiler

`pip install uncompyle6` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 8916 · last release 2025-09-29 · [PyPI](https://pypi.org/project/uncompyle6/)

_README extract left out: share-alike licence._

### manhole

Manhole is in-process service that will accept unix domain socket connections and present thestacktraces for all threads and an interactive prompt.

`pip install manhole` · installs (wheel) · licence: BSD License · rank 9327 · last release 2024-07-04 · [PyPI](https://pypi.org/project/manhole/) · [docs](https://python-manhole.readthedocs.io/)

<details><summary>README extract</summary>

Example:
```python
manhole.install(
    verbose=True,
    verbose_destination=2,
    patch_fork=True,
    activate_on=None,
    oneshot_on=None,
    sigmask=manhole.ALL_SIGNALS,
    socket_path=None,
    reinstall_delay=0.5,
    locals=None,
    strict=True,
)
```

Sections: Overview, Features, Options, What happens when you actually connect to the socket, Known issues, SIGTERM and socket cleanup, Using Manhole with uWSGI, Requirements, Similar projects, 1.8.1 (2024-07-24), 1.8.0 (2021-04-08), 1.7.0 (2021-03-22), 1.6.0 (2019-01-19), 1.5.0 (2017-08-31)

</details>

### hunter

Hunter is a flexible code tracing toolkit.

`pip install hunter` · installs (wheel) · licence: BSD-2-Clause · rank 9889 · last release 2025-08-22 · [PyPI](https://pypi.org/project/hunter/) · [docs](https://python-hunter.readthedocs.io/)

<details><summary>README extract</summary>

Features:
Hunter is a flexible code tracing toolkit, not for measuring coverage, but for debugging, logging, inspection and other
nefarious purposes. It has a simple Python API,
a convenient terminal API and
a CLI tool to attach to processes. ...

Example:
```python
import hunter
hunter.trace(module='posixpath', action=hunter.CallPrinter)

import os
os.path.join('a', 'b')
```

Sections: Overview, Documentation, Getting started, Actions, Tracing processes, Environment variable activation, Environment variable configuration, Filtering DSL, Design notes, FAQ, Why not Smiley?, Why not pytrace?, Why not PySnooper or snoop?, Why not coverage?

</details>

### web-pdb

Web interface for Python's built-in PDB debugger

`pip install web-pdb` · installs (wheel) · licence: MIT License · rank 10313 · last release 2026-05-21 · [PyPI](https://pypi.org/project/web-pdb/)

<details><summary>README extract</summary>

Web-PDB is a web-interface for Python's built-in PDB debugger.
It allows to debug Python scripts remotely in a web-browser.

Currently this project is in a minimum maintenance mode.
It means that I will try to maintain compatibility with new Python versions and address
critical issues, if any arise. ...

Features:
- Responsive design based on Bootstrap with light and dark modes.
- Python syntax highlighting with Prism (the default and "Okaida" themes).
- Supports all PDB features. ...

Example:
```python
import web_pdb; web_pdb.set_trace()
```

Sections: Web-PDB, Important Notice, Features, Usage, The `inspect` Command, Multithreading, Multiprocessing, Compatibility, Implementation Details

</details>

### niche-elf

A small library that optimizes some niche operations commonly used by debugger extensions.

`pip install niche-elf` · installs (wheel) · licence: GPLv3 · rank 10643 · last release 2026-09-21 · [PyPI](https://pypi.org/project/niche-elf/)

_README extract left out: share-alike licence._

### snoop

Powerful debugging tools for Python

`pip install snoop` · installs (wheel) · licence: MIT License · rank 10969 · last release 2026-07-18 · [PyPI](https://pypi.org/project/snoop/)

<details><summary>README extract</summary>

snoop is a powerful set of Python debugging tools. It's primarily meant to be a more featureful and refined version of PySnooper. It also includes its own version of icecream and some other nifty stuff.

You're trying to figure out why your Python code isn't doing what you think it should be doing. ...

Example:
```python
import snoop

@snoop
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

number_to_bits(6)
```

...

</details>

### decompyle3

Python cross-version byte-code decompiler

`pip install decompyle3` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11994 · last release 2025-10-01 · [PyPI](https://pypi.org/project/decompyle3/)

_README extract left out: share-alike licence._

### robotcode

Command line interface for RobotCode

`pip install robotcode` · installs (wheel) · licence: Apache Software License · rank 12660 · last release 2026-10-26 · [PyPI](https://pypi.org/project/robotcode/) · [docs](https://github.com/robotcodedev/robotcode#readme) · [source](https://github.com/robotcodedev/robotcode)

<details><summary>README extract</summary>

RobotCode is a complete Robot Framework toolkit: a language server, IDE extensions for VS Code and the JetBrains platform, a powerful command-line interface, and a unified `robot.toml`-based configuration model. It is designed for everyday Robot Framework work — from your first keyword to scaling multi-team test suites in CI. ...

Sections: RobotCode - The Ultimate Robot Framework Toolset, What is RobotCode?, Key Features, Editor / IDE, Configuration, Command line, Requirements, Getting Started, Visual Studio Code, IntelliJ IDEA or PyCharm, Command Line and Other Editors, Documentation, Get Involved, Powered by

</details>

### interruptingcow

A watchdog that interrupts long running code.

`pip install interruptingcow` · installs from source (sdist only) · licence: MIT License · rank 12803 · last release 2018-02-27 · [PyPI](https://pypi.org/project/interruptingcow/)

<details><summary>README extract</summary>

Interruptingcow is a generic utility that can relatively gracefully interrupt
your Python code when it doesn't execute within a specific number of seconds:
Timeouts are specified in seconds (as floats with theoretical microsecond
precision).

Example:
```python
from interruptingcow import timeout

try:
    with timeout(5, exception=RuntimeError):
        # perform a potentially very slow operation
        pass
except RuntimeError:
    print "didn't finish within 5 seconds"
```

Sections: Interrupting Cow, Reentrant, Function Decorators, Quotas, Caveats

</details>

### isystem.connect

isystem.connect for Python

`pip install isystem.connect` · installs (wheel) · licence: Other/Proprietary License · rank 12807 · last release 2026-11-06 · [PyPI](https://pypi.org/project/isystem.connect/)

<details><summary>README extract</summary>

This package enables control of winIDEA and embedded targets from Python.
Please find the detailed documentation with examples at

(c) TASKING Germany GmbH, 2023

</details>

### django-debug-toolbar-template-timings

A django-debug-toolbar panel that shows you template rendering times for Django

`pip install django-debug-toolbar-template-timings` · installs (wheel) · licence: not stated · rank 13047 · last release 2018-02-24 · [PyPI](https://pypi.org/project/django-debug-toolbar-template-timings/)

<details><summary>README extract</summary>

Template-timings is a panel for Django Debug Toolbar that gives an in-dept breakdown of the time it takes to render your Django templates (including templates included via `{% extends %}` and `{% include %}`).

Template-timings supports Django 1.8 and below, Django 1.9 and above do not work at the moment.

Sections: Template-Timings, Screenshot, Frequently asked questions, Configuration

</details>

## Also in this topic

- [yamllint](software-development.md#yamllint) - A linter for YAML files.
- [pyroscope-io](software-development.md#pyroscope-io) - Pyroscope Python integration
- [pyelftools](file-formats.md#pyelftools) - Library for analyzing ELF files and DWARF debugging information
- [gdbmongo](database.md#gdbmongo) - GDB pretty printers and commands for debugging the MongoDB Server
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [pwntools](security.md#pwntools) - Pwntools CTF framework and exploit development library.
- [pyocd](software-development.md#pyocd) - Cortex-M debugger for Python
- [cmsis-pack-manager](software-development.md#cmsis-pack-manager) - Python manager for CMSIS-Pack index and cache with fast Rust backend
- [pdbp](scientific-engineering.md#pdbp) - pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.
- [tabcompleter](scientific-engineering.md#tabcompleter) - tabcompleter --- Autocompletion in the Python console.
- [pudb](software-development.md#pudb) - A full-screen, console-based Python debugger
- [livereload](software-development-build-tools.md#livereload) - Python LiveReload is an awesome tool for web developers
- [scalene](software-development.md#scalene) - Scalene: A high-resolution, low-overhead CPU, GPU, and memory profiler for Python with AI-powered optimization suggestions
- [fastapi-debug-toolbar](internet.md#fastapi-debug-toolbar) - A debug toolbar for FastAPI.
- [yagmail](communications-email.md#yagmail) - Yet Another GMAIL client
- [django-graphiql-debug-toolbar](internet.md#django-graphiql-debug-toolbar) - Django Debug Toolbar for GraphiQL IDE.
- [kolo](software-development.md#kolo) - Kolo is a text-based Python debugger for AI agents. Capture every executed function call, return value, local variable, HTTP request, and more in greppable trace files.
- [pyocd-pemicro](scientific-engineering-2.md#pyocd-pemicro) - PyOCD debug probe plugin for PEMicro debug probes
