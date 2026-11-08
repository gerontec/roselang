# Terminals / Terminal Emulators/X Terminals

[Index](README.md) · 3 packages in this topic, 4 more listed under another topic, by downloads.

### terminado

Tornado websocket backend for the Xterm.js Javascript terminal emulator library.

`pip install terminado` · installs (wheel) · licence: BSD License · rank 592 · last release 2024-03-12 · [PyPI](https://pypi.org/project/terminado/)

<details><summary>README extract</summary>

This is a Tornado websocket backend for the
Xterm.js Javascript terminal emulator library.

It evolved out of pyxterm, which
was part of GraphTerm (as
lineterm.py), v0.57.0 (2014-07-18), and ultimately derived from the
public-domain Ajaxterm
code, v0.11 (2008-11-13) (also on Github as part of
QWeb).

Modules: ...

Example:
```python
import os.path
import tornado.web
import tornado.ioloop

# This demo requires tornado_xstatic and XStatic-term.js
import tornado_xstatic

import terminado

STATIC_DIR = os.path.join(os.path.dirname(terminado.file), "_static")

class TerminalPageHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render(
...
```

</details>

### pyte

Simple VTXXX-compatible terminal emulator.

`pip install pyte` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 2257 · last release 2023-11-12 · [PyPI](https://pypi.org/project/pyte/)

_README extract left out: share-alike licence._

### clint

Python Command Line Interface Tools

`pip install clint` · installs from source (sdist only) · licence: ISC License (ISCL) · rank 6860 · last release 2015-08-25 · [PyPI](https://pypi.org/project/clint/)

<details><summary>README extract</summary>

Clint is a module filled with a set of awesome tools for developing
commandline applications.

C ommand
L ine
IN terface
T ools

Clint is awesome. Crazy awesome. It supports colors, but detects if the session is a TTY, so doesn't render the colors if you're piping stuff around. Automagically.

Awesome nest-able indentation context manager. ...

Example:
```python
>>> from clint.textui import puts, indent

>>> puts('not indented text')
>>> with indent(4):
>>>     puts('indented text')
not indented text
    indented text
```

Sections: Clint: Python Command-line Application Tools, Current Features, Future Features, Example, Roadmap, 0.5.1, 0.5.0, 0.4.1, 0.4.0, 0.3.7, 0.3.6, 0.3.5, 0.3.4, 0.3.3

</details>

## Also in this topic

- [pywinpty](terminals.md#pywinpty) - Pseudo terminal support for Windows from Python.
- [cli-helpers](software-development.md#cli-helpers) - Helpers for building command-line apps
- [dockerpty](software-development-libraries-3.md#dockerpty) - Python library to use the pseudo-tty of a docker container
- [pansi](software-development.md#pansi) - Text mode rendering library
