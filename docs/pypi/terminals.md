# Terminals

[Index](README.md) · 15 packages in this topic, 40 more listed under another topic, by downloads.

### colorama

Cross-platform colored terminal text.

`pip install colorama` · installs (wheel) · licence: BSD License · rank 118 · last release 2022-10-25 · [PyPI](https://pypi.org/project/colorama/)

<details><summary>README extract</summary>

Makes ANSI escape character sequences (for producing colored terminal text and
cursor positioning) work under MS Windows.

PyPI for releases |
Github for source |
Colorama for enterprise on Tidelift

If you find Colorama useful, please to the authors. Thank you!

Example:
```python
from colorama import just_fix_windows_console
just_fix_windows_console()
```

Sections: Colorama, Description, Usage, Thanks

</details>

### ptyprocess

Run a subprocess in a pseudo terminal

`pip install ptyprocess` · installs (wheel) · licence: ISC License (ISCL) · rank 234 · last release 2020-12-28 · [PyPI](https://pypi.org/project/ptyprocess/)

<details><summary>README extract</summary>

Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a password
prompt that doesn't read from stdin, output that changes when it's going to a
pipe rather than a terminal, or curses-style interfaces that rely on a terminal. ...

Example:
```python
p = PtyProcessUnicode.spawn(['python'])
p.read(20)
p.write('6+6\n')
p.read(20)
```

</details>

### termcolor

ANSI color formatting for output in terminal

`pip install termcolor` · installs (wheel) · licence: MIT · rank 336 · last release 2025-12-29 · [PyPI](https://pypi.org/project/termcolor/) · [source](https://github.com/termcolor/termcolor)

<details><summary>README extract</summary>

Example:
```python
import sys

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
...
```

Sections: termcolor, From PyPI, From source, Demo, Example, Text properties, Terminal properties, Overrides

</details>

### colorlog

Add colours to the output of Python's logging module.

`pip install colorlog` · installs (wheel) · licence: MIT License · rank 485 · last release 2026-07-23 · [PyPI](https://pypi.org/project/colorlog/)

<details><summary>README extract</summary>

Add colours to the output of Python's `logging` module.

- Source on GitHub
- Package on PyPI

Example:
```python
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())

logger = colorlog.getLogger('example')
logger.addHandler(handler)
```

Sections: Log formatting with colors!, Usage, Arguments, Color escape codes, Examples, Using `secondary_log_colors`, With `dictConfig`, With `fileConfig`, With custom log levels, Tests, Alternatives, Projects using colorlog

</details>

### jinxed

Jinxed Terminal Library

`pip install jinxed` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 1658 · last release 2026-07-03 · [PyPI](https://pypi.org/project/jinxed/)

<details><summary>README extract</summary>

docsgh_actionscodecov|
pypisupported-versionssupported-implementations|
linuxwindowsmacbsd|

Jinxed is a pure-Python implementation of a subset of the Python curses library.

It provides jinxed.tigetstr(), jinxed.tparm(), and related terminfo
functions on all platforms with a virtual terminfo(5) database. ...

Sections: Introduction, Source, Issues

</details>

### pywinpty

Pseudo terminal support for Windows from Python.

`pip install pywinpty` · installs from source (sdist only) · licence: MIT License · rank 2779 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pywinpty/) · [source](https://github.com/andfoy/pywinpty)

<details><summary>README extract</summary>

*Copyright © 2017–2022 Spyder Project Contributors*
*Copyright © 2022– Edgar Andrés Margffoy Tuay*

Features:
PyWinpty allows creating and communicating with Windows processes that receive input and print outputs via console input and output pipes. PyWinpty supports both the native ConPTY interface and the previous, fallback winpty library.

Example:
```python
# High level usage using `spawn`
from winpty import PtyProcess

proc = PtyProcess.spawn('python')
proc.write('print("hello, world!")\r\n')
proc.write('exit()\r\n')
while proc.isalive():
    print(proc.readline())

# Low level usage using the raw `PTY` object
from winpty import PTY

# Start a new winpty-agent process of size (cols, rows)
...
```

...

</details>

### colored

Simple python library for color and formatting to terminal

`pip install colored` · installs (wheel) · licence: MIT License · rank 3398 · last release 2026-03-28 · [PyPI](https://pypi.org/project/colored/)

<details><summary>README extract</summary>

Colored, it's a simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups.
Colored now supports RGB color mode. As "true color" graphic cards with 16 to 24 bits of color became common,
applications began to support 24-bit colors. ...

Sections: About, Usage

</details>

### iterfzf

Pythonic interface to fzf

`pip install iterfzf` · installs (wheel) · licence: GPL-3.0-or-later · rank 3467 · last release 2026-01-25 · [PyPI](https://pypi.org/project/iterfzf/) · [source](https://github.com/dahlia/iterfzf)

_README extract left out: share-alike licence._

### simple-term-menu

A Python package which creates simple interactive menus on the command line.

`pip install simple-term-menu` · installs (wheel) · licence: MIT License · rank 3640 · last release 2024-12-02 · [PyPI](https://pypi.org/project/simple-term-menu/)

<details><summary>README extract</summary>

Features:
`simple-term-menu` creates simple menus for interactive command line programs. It can be used to offer a choice of
different options to the user. Menu entries can be selected with the arrow, j/k, or emacs (C-n/C-p) keys. ...

Example:
```python
# !/usr/bin/env python3

import os
from simple_term_menu import TerminalMenu

def main():
    fruits = ["[a] apple", "[b] banana", "[o] orange"]
    terminal_menu = TerminalMenu(fruits, title="Fruits")
    menu_entry_index = terminal_menu.show()

if name == "main":
    main()
```

...

</details>

### prefixed

Prefixed alternative numeric library

`pip install prefixed` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5074 · last release 2024-09-02 · [PyPI](https://pypi.org/project/prefixed/) · [docs](https://prefixed.readthedocs.io)

<details><summary>README extract</summary>

docsgh_actionscodecov|
pypisupported-versionssupported-implementations|

Features:
Prefixed provides an alternative implementation of the built-in float which supports
formatted output with SI (decimal) and IEC (binary) prefixes.

Because prefixed.Float inherits from the built-in float, it behaves
exactly the same in most cases. ...

Example:
```python
>>> from prefixed import Float

>>> f'{Float(3250):.2h}'
'3.25k'

>>> '{:.2h}s'.format(Float(.00001534))
'15.34μs'

>>> '{:.2k}B'.format(Float(42467328))
'40.50MiB'

>>> f'{Float(2048):.2m}B'
'2.00KB'
```

Sections: Overview, Presentation Types, String Initialization, Additional Flags, Significant Digits, Adjustable Thresholds, SI (Decimal) Prefixes, IEC (Binary) Prefixes

</details>

### ripgrep-bin

ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern while respecting gitignore rules.

`pip install ripgrep-bin` · installs (wheel) · licence: Unlicense OR MIT · rank 6112 · last release 2026-07-16 · [PyPI](https://pypi.org/project/ripgrep-bin/) · [source](https://github.com/Bing-su/pip-binary-factory)

<details><summary>README extract</summary>

`ripgrep` is a line-oriented search tool that recursively searches the current directory for a regex pattern.

</details>

### termflow-md

A streaming markdown renderer for modern terminals

`pip install termflow-md` · installs (wheel) · licence: MIT · rank 6645 · last release 2026-10-02 · [PyPI](https://pypi.org/project/termflow-md/) · [docs](https://github.com/mpfaffenberger/termflow#readme) · [source](https://github.com/mpfaffenberger/termflow)

<details><summary>README extract</summary>

A streaming markdown renderer and terminal UI toolkit for modern terminals.

termflow renders markdown to ANSI as it arrives, line by line, which makes it
a natural fit for LLM output. ...

Features:
- Streaming rendering — parse and render markdown incrementally, line by
 line, without waiting for the full document
- Syntax highlighting — fenced code blocks highlighted via Pygments, with
 language detection ...

Example:
```python
from termflow import render_markdown

render_markdown("# Hello World")
```

Sections: termflow, Features, CLI, Rendering markdown, Smooth streaming output, Terminal theming, Interactive menus, Resizing, Swappable agent histories, Live mode, The real DOOM, Configuration, Origin

</details>

### pyfzf

Python wrapper for junegunn's fuzzyfinder (fzf)

`pip install pyfzf` · installs (wheel) · licence: MIT License · rank 8459 · last release 2022-03-01 · [PyPI](https://pypi.org/project/pyfzf/)

<details><summary>README extract</summary>

* Python 3.6+
* fzf

*Note*: fzf must be installed and available on PATH.

Sections: pyfzf, A python wrapper for *junegunn*'s awesome fzf., Requirements, Usage, Thanks, CHANGES

</details>

### ansi2txt

ansi to plain text converter

`pip install ansi2txt` · installs (wheel) · licence: GNU Affero General Public License v3; MIT License · rank 13886 · last release 2023-02-23 · [PyPI](https://pypi.org/project/ansi2txt/)

_README extract left out: share-alike licence._

### beaupy

A library of elements for interactive TUIs in Python

`pip install beaupy` · installs (wheel) · licence: MIT · rank 14979 · last release 2026-10-15 · [PyPI](https://pypi.org/project/beaupy/) · [source](https://github.com/petereon/beaupy)

<details><summary>README extract</summary>

> A Python library of interactive CLI elements you have been looking for

For documentation but more and prettier see here

Features:
BeauPy implements a number of common interactive elements:

| Function | Functionality |

| `select` | Prompt to pick a choice from a list |
| `select_multiple` | Prompt to select one or multiple choices from a list |
| `confirm` | Prompt with a ...

Example:
```python
import time
from beaupy import confirm, prompt, select, select_multiple
from beaupy.spinners import *
from rich.console import Console

console = Console()

# Confirm a dialog
if confirm("Will you take the ring to Mordor?"):
    names = [
        "Frodo Baggins",
        "Samwise Gamgee",
        "Legolas",
        "Aragorn",
...
```

...

</details>

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [wcwidth](software-development-internationalization.md#wcwidth) - Measures the displayed width of unicode strings in a terminal
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [argcomplete](software-development.md#argcomplete) - Bash tab completion for argparse
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [colorclass](software-development-libraries.md#colorclass) - Colorful worry-free console applications for Linux, Mac OS X, and Windows.
- [blessed](software-development-libraries.md#blessed) - Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.
- [yaspin](software-development.md#yaspin) - Yet Another Terminal Spinner
- [terminaltables](software-development-libraries.md#terminaltables) - Generate simple tables in terminals from a nested list of strings.
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [asciinema](system-shells.md#asciinema) - Terminal session recorder
- [pytube](internet.md#pytube) - Python 3 library for downloading YouTube Videos.
- [tcolorpy](software-development-libraries.md#tcolorpy) - tcolopy is a Python library to apply true color for terminal text.
- [plotext](scientific-engineering-visualization.md#plotext) - plotext plots directly on terminal
- [autopage](software-development-libraries-2.md#autopage) - A library to provide automatic paging for console output
- [blessings](software-development-libraries-2.md#blessings) - A thin, practical wrapper around terminal coloring, styling, and positioning
- [httpie](internet-www-http.md#httpie) - HTTPie: modern, user-friendly command-line HTTP client for the API era.
- [pudb](software-development.md#pudb) - A full-screen, console-based Python debugger
- [progressbar](software-development-libraries-2.md#progressbar) - Text progress bar library for Python.
- [verboselogs](software-development.md#verboselogs) - Verbose logging level for Python's logging module
- [common](software-development-libraries-2.md#common) - Common tools and data structures implemented in pure python.
- [dockerpty](software-development-libraries-3.md#dockerpty) - Python library to use the pseudo-tty of a docker container
- [pytubefix](internet.md#pytubefix) - Python3 library for downloading YouTube Videos.
- [to-requirements.txt](software-development.md#to-requirementstxt) - Automatically add and delete modules to requirements.txt installing them using pip.
- [progressbar33](software-development-libraries-3.md#progressbar33) - Text progress bar library for Python.
- [ascii-colors](software-development-libraries-3.md#ascii-colors) - A Python library for rich terminal output with advanced logging features.
- [sty](printing.md#sty) - String styling for your terminal
- [plotille](scientific-engineering-visualization.md#plotille) - Plot in the terminal using braille dots.
- [uniplot](scientific-engineering.md#uniplot) - Lightweight plotting to the terminal. 4x resolution via Unicode.
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [terminaltables3](software-development-libraries-4.md#terminaltables3) - Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [pansi](software-development.md#pansi) - Text mode rendering library
- [asciimatics](software-development-user-interfaces.md#asciimatics) - A cross-platform package to replace curses (mouse/keyboard input & text colours/positioning) and create ASCII animations
- [tabula](software-development-libraries-4.md#tabula) - Ascii table
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
- [prompt](software-development-libraries-5.md#prompt) - Library for prompting input on the command line.
- [textual-fspicker](software-development-libraries-5.md#textual-fspicker) - A simple Textual filesystem picker dialog library.
