# Desktop Environment

[Index](README.md) · 16 packages in this topic, 1 more listed under another topic, by downloads.

### tqdm

Fast, Extensible Progress Meter

`pip install tqdm` · installs (wheel) · licence: MPL-2.0 AND MIT · rank 69 · last release 2026-09-11 · [PyPI](https://pypi.org/project/tqdm/) · [source](https://github.com/tqdm/tqdm)

<details><summary>README extract</summary>

`tqdm` derives from the Arabic word *taqaddum* (تقدّم) which can mean "progress,"
and is an abbreviation for "I love you so much" in Spanish (*te quiero demasiado*).

Instantly make your loops show a smart progress meter - just wrap any
iterable with `tqdm(iterable)`, and you're done! ...

Example:
```python
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
```

Sections: tqdm, Documentation, Parameters, Extra CLI Options, Returns, Convenience Functions, Submodules, `contrib`, Examples and Advanced Usage, Description and additional stats, `asyncio`, Pandas Integration, Keras Integration, Dask Integration

</details>

### jeepney

Low-level, pure Python DBus protocol wrapper.

`pip install jeepney` · installs (wheel) · licence: MIT · rank 219 · last release 2025-02-27 · [PyPI](https://pypi.org/project/jeepney/) · [docs](https://jeepney.readthedocs.io/en/latest/) · [source](https://gitlab.com/takluyver/jeepney)

<details><summary>README extract</summary>

Jeepney is a pure Python implementation of D-Bus messaging. It has an I/O-free core, and integration modules for different
event loops.

D-Bus is an inter-process communication system, mainly used in Linux.

To install Jeepney:
Jeepney docs on Readthedocs

</details>

### progressbar2

A Python Progressbar library to provide visual (yet text based) progress to long running operations.

`pip install progressbar2` · installs (wheel) · licence: BSD License · rank 877 · last release 2026-11-05 · [PyPI](https://pypi.org/project/progressbar2/) · [docs](https://progressbar-2.readthedocs.io/en/latest/) · [source](https://github.com/wolph/python-progressbar/)

<details><summary>README extract</summary>

The fastest progress bar in Python, maintained since 2012.

Wrapping a fast loop in a progress bar can cost more than the loop
itself, so the overhead per iteration is the number that matters. This
race replays the measured wall-clock times of the same
1,000,000-iteration loop, wrapped with each library's default settings: ...

Example:
```python
import time
import progressbar

for item in progressbar.progressbar(range(100), desc='Loading'):
    time.sleep(0.02)
```

Sections: progressbar2, Quick start, Colors, gradients and animated markers, Logs above a live bar, Many bars at once, Parallel execution, Replace pv on the command line, Unknown length and animated bars, Boring where it counts, Known terminal caveats, Links

</details>

### screeninfo

Fetch location and size of physical screens.

`pip install screeninfo` · installs (wheel) · licence: MIT License · rank 1412 · last release 2022-09-09 · [PyPI](https://pypi.org/project/screeninfo/) · [source](https://github.com/rr-/screeninfo)

<details><summary>README extract</summary>

screeninfo

Fetch location and size of physical screens.

Example:
```python
from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))
```

Sections: Usage, Forcing environment

</details>

### shtab

Automagic shell tab completion for Python CLI applications

`pip install shtab` · installs (wheel) · licence: MPL-2.0 · rank 2161 · last release 2026-10-21 · [PyPI](https://pypi.org/project/shtab/) · [docs](https://tqdm.github.io/shtab) · [source](https://github.com/tqdm/shtab)

<details><summary>README extract</summary>

- What: Automatically generate shell tab completion scripts for Python CLI apps
- Why: Speed & correctness. Alternatives like
 argcomplete and
 pyzshcomplete are slow and have
 side-effects
- How: `shtab` processes an `argparse.ArgumentParser` object to generate a
 tab completion script for your shell

Features:
- Outputs tab completion scripts for multiple shells

 - `bash`, `zsh`, `fish`, `tcsh`, `powershell`

- Supports

 - argparse
 - docopt (via argopt)
 - click

- `<arguments>`, `--options` and `sub commands`
- Choices (`--say={hello,goodbye}`) ...

Sections: shtab, Features, Usage, Examples, FAQs, Alternatives

</details>

### pyxdg

PyXDG contains implementations of freedesktop.org standards in python.

`pip install pyxdg` · installs (wheel) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 4291 · last release 2022-06-05 · [PyPI](https://pypi.org/project/pyxdg/)

_README extract left out: share-alike licence._

### urwid-readline

A textbox edit widget for urwid that supports readline shortcuts

`pip install urwid-readline` · installs from source (sdist only) · licence: MIT License · rank 5599 · last release 2024-09-22 · [PyPI](https://pypi.org/project/urwid-readline/)

### superqt

Missing widgets and components for PyQt/PySide

`pip install superqt` · installs (wheel) · licence: BSD License · rank 7831 · last release 2026-10-30 · [PyPI](https://pypi.org/project/superqt/) · [docs](https://pyapp-kit.github.io/superqt/) · [source](https://github.com/pyapp-kit/superqt)

<details><summary>README extract</summary>

This repository aims to provide high-quality community-contributed Qt widgets and components for PyQt & PySide
that are not provided in the native QtWidgets module.

Components are tested on:

- macOS, Windows, & Linux
- Python 3.11 and above
- PyQt5 (5.11 and above) & PyQt6
- PySide6

Documentation is available at

Sections: superqt!, "missing" widgets and components for PyQt/PySide, Documentation, Widgets, Utilities

</details>

### mac-alias

Generate/parse macOS Alias records from Python

`pip install mac-alias` · installs (wheel) · licence: MIT · rank 8438 · last release 2025-12-04 · [PyPI](https://pypi.org/project/mac-alias/) · [docs](https://mac-alias.readthedocs.io/en/latest/) · [source](https://github.com/dmgbuild/mac_alias)

<details><summary>README extract</summary>

`mac_alias` lets you generate or read binary Alias and Bookmark records
from Python code.

While it is written in pure Python, some OS X specific code is required to
generate a proper Alias or Bookmark record for a given file, so this module
currently is not portable to other platforms. ...

Sections: mac_alias, What is this?

</details>

### ds-store

Manipulate Finder .DS_Store files from Python

`pip install ds-store` · installs (wheel) · licence: MIT · rank 8489 · last release 2026-06-23 · [PyPI](https://pypi.org/project/ds-store/) · [docs](https://ds-store.readthedocs.io/en/latest/) · [source](https://github.com/dmgbuild/ds_store)

<details><summary>README extract</summary>

`ds_store` lets you examine and modify `.DS_Store` files from Python
code; since it is written in pure Python, it is portable and will run on any
platform, not just Mac OS X.

Credit is due to Wim Lewis, Mark Mentovai and Yvan Barthélemy for
reverse-engineering the .DS_Store file format. ...

Sections: ds_store, What is this?

</details>

### dmgbuild

macOS command line utility to build disk images

`pip install dmgbuild` · installs (wheel) · licence: MIT · rank 9277 · last release 2026-01-15 · [PyPI](https://pypi.org/project/dmgbuild/) · [docs](https://dmgbuild.readthedocs.io/en/latest/) · [source](https://github.com/dmgbuild/dmgbuild)

<details><summary>README extract</summary>

`dmgbuild` is a command line tool to create macOS disk images (aka
`.dmg` files). While it is possible to create disk images easily enough
from the command line using the `hdiutil` program that ships with macOS,
there is no easy way to configure the appearance of the resulting disk image
when the user opens it. ...

Sections: dmgbuild, What is this?

</details>

### dirsync

Advanced directory tree synchronisation tool

`pip install dirsync` · installs (wheel) · licence: MIT License · rank 9672 · last release 2025-05-24 · [PyPI](https://pypi.org/project/dirsync/)

<details><summary>README extract</summary>

2014+ Thomas Khyn
 2003-2015 Anand B Pillai

Advanced directory tree synchronisation tool

based on Python robocopier by Anand B Pillai

If you like dirsync and find it useful, you may want to thank me and
encourage future development by sending a few mBTC / mBCH / mBSV at this address:
`1EwENyR8RV6tMc1hsLTkPURtn5wJgaBfG9`.

Example:
```python
from dirsync import sync
sync(sourcedir, targetdir, action, **options)
```

Sections: dirsync, Usage, Main Options, Additional Options, Configuration file, Custom logger

</details>

### magicgui

build GUIs from python types

`pip install magicgui` · installs (wheel) · licence: MIT License · rank 10068 · last release 2026-04-10 · [PyPI](https://pypi.org/project/magicgui/) · [docs](https://pyapp-kit.github.io/magicgui/) · [source](https://github.com/pyapp-kit/magicgui)

<details><summary>README extract</summary>

build GUIs from type annotations, using magic.

Example:
```python
from magicgui import magicgui
from enum import Enum

class Medium(Enum):
    Glass = 1.520
    Oil = 1.515
    Water = 1.333
    Air = 1.0003

# decorate your function with the @magicgui decorator
@magicgui(call_button="calculate", result_widget=True)
def snells_law(aoi=30.0, n1=Medium.Glass, n2=Medium.Water, degrees=True):
    import math

...
```

Sections: 📖 Docs, Basic usage

</details>

### app-model

Generic application schema implemented in python

`pip install app-model` · installs (wheel) · licence: BSD License · rank 10570 · last release 2025-11-09 · [PyPI](https://pypi.org/project/app-model/) · [source](https://github.com/pyapp-kit/app-model)

<details><summary>README extract</summary>

Generic application schema implemented in python.

This is a schema for declarative organization of application data, such as
menus, keybindings, actions/commands, etc...

Inspired by the VS-Code application model

docs at

</details>

### notify2

Python interface to DBus notifications

`pip install notify2` · installs (wheel) · licence: BSD License · rank 11855 · last release 2017-04-28 · [PyPI](https://pypi.org/project/notify2/)

<details><summary>README extract</summary>

This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly. It's compatible with
Python 2 and 3, and its callbacks can work with Gtk 3 or Qt 4 applications.

To use it, first call ``notify2.init('app name')``, then create and show notifications:: ...

</details>

### windows-mcp

Lightweight MCP Server for interacting with Windows Operating System.

`pip install windows-mcp` · installs (wheel) · licence: MIT License · rank 12968 · last release 2026-10-10 · [PyPI](https://pypi.org/project/windows-mcp/) · [source](https://github.com/CursorTouch/Windows-MCP)

<details><summary>README extract</summary>

Windows-MCP is a lightweight, open-source project that enables seamless integration between AI agents and the Windows operating system. Acting as an MCP server bridges the gap between LLMs and the Windows operating system, allowing agents to perform tasks such as file navigation, application control, UI interaction, QA testing, and more. ...

Sections: 🪟 Windows-MCP, Updates, 🎥 Demos, ✨ Key Features, Prerequisites, Run at Login, 🖥️ Running Windows-MCP, Transport Options, Authentication, IP Allowlist, CORS Origins, Tool Selection, TLS/HTTPS, OAuth 2.0 + PKCE

</details>

## Also in this topic

- [desktop-notifier](communications.md#desktop-notifier) - Python library for cross-platform desktop notifications
