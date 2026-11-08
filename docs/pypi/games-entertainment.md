# Games/Entertainment

[Index](README.md) · 19 packages in this topic, 1 more listed under another topic, by downloads.

### pygame

Python Game Development

`pip install pygame` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 2533 · last release 2024-09-29 · [PyPI](https://pypi.org/project/pygame/) · [docs](https://pygame.org/docs) · [source](https://github.com/pygame/pygame)

_README extract left out: share-alike licence._

### moderngl

ModernGL: High performance rendering for Python 3

`pip install moderngl` · installs (wheel) · licence: OSI Approved; MIT License · rank 4351 · last release 2026-10-07 · [PyPI](https://pypi.org/project/moderngl/) · [docs](https://moderngl.readthedocs.io/) · [source](https://github.com/moderngl/moderngl/)

<details><summary>README extract</summary>

ModernGL is a Python wrapper over OpenGL Core. ModernGL simplifies the creation of graphics applications like scientific simulations, games or user interfaces.
Usually, acquiring in-depth knowledge of OpenGL requires a steep learning curve. In contrast, ModernGL is easy to learn and use. ...

Features:
- GPU accelerated high quality graphics
- Rendering modern OpenGL scenes with less headache
- Simpler and faster than PyOpenGL
- Can render without a window
- 100% Pythonic

Example:
```python
>>> import moderngl
>>> ctx = moderngl.get_context()
>>> buf = ctx.buffer(b"Hello World!")  # allocated on the GPU
>>> buf.read()
b'Hello World!'
```

...

</details>

### glcontext

Portable Headless OpenGL Context

`pip install glcontext` · installs (wheel) · licence: MIT License · rank 4379 · last release 2026-10-07 · [PyPI](https://pypi.org/project/glcontext/)

<details><summary>README extract</summary>

glcontext is a library providing OpenGL implementation for ModernGL on multiple platforms.

* glcontext on github
* glcontext on pypi
* ModernGL

A glcontext backend is either an extension or a submodule of the glcontext package.
The package itself does not import any of the backends. ...

Example:
```python
def create_context(*args, **kwargs) -> GLContext:
    pass
```

Sections: glcontext, Backends, Structure, Current backends, wgl, x11, darwin, egl, Environment Variables, Running tests

</details>

### pygame-ce

Python Game Development

`pip install pygame-ce` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 4877 · last release 2026-08-09 · [PyPI](https://pypi.org/project/pygame-ce/) · [docs](https://pyga.me/docs) · [source](https://github.com/pygame-community/pygame-ce)

_README extract left out: share-alike licence._

### vimgolf

A vimgolf client written in Python

`pip install vimgolf` · installs (wheel) · licence: MIT License · rank 5416 · last release 2026-05-29 · [PyPI](https://pypi.org/project/vimgolf/)

<details><summary>README extract</summary>

This project contains a vimgolf client written in Python.

The user interface is similar to the official vimgolf client,
with a few additions inspired by vimgolf-finder, and an
optional way to specify keys to type when launching a challenge.

Installation

- Python 3.6 or greater

Sections: vimgolf, Requirements, Update, Launch, Commands, Demo

</details>

### UnityPy

A Unity extraction and patching package

`pip install UnityPy` · installs (wheel) · licence: MIT License · rank 5552 · last release 2026-10-03 · [PyPI](https://pypi.org/project/UnityPy/)

<details><summary>README extract</summary>

A Unity asset extractor for Python based on AssetStudio.

Next to extraction, UnityPy also supports editing Unity assets.
Via the typetree structure all object types can be edited in their native forms.

If you need advice or if you want to talk about (game) data-mining,
feel free to join the UnityPy Discord. ...

Example:
```python
import os
import UnityPy

def unpack_all_assets(source_folder: str, destination_folder: str):
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            # generate file_path
            file_path = os.path.join(root, file_name)
...
```

...

</details>

### fmod-toolkit

(no summary)

`pip install fmod-toolkit` · installs (wheel) · licence: MIT License · rank 6090 · last release 2026-04-07 · [PyPI](https://pypi.org/project/fmod-toolkit/)

<details><summary>README extract</summary>

`fmod_toolkit` is a lightweight Python package designed to extract and export audio from FMOD files to WAV format.
It includes pre-bundled FMOD libraries for Windows, macOS, and Linux, enabling seamless cross-platform usage without manual library installation. ...

Example:
```python
from fmod_toolkit import raw_to_wav

# fsb_data: bytes containing the FMOD sound bank (FSB) file
fsb_data: bytes = ...  # Load your FSB file data here
# fsb_basename: base name for output WAV files (e.g., "soundbank")
fsb_basename: str = "soundbank"
# channels: number of audio channels (e.g., 2 for stereo)
channels: int = 2
...
```

Sections: fmod_toolkit, usage

</details>

### pymunk

Pymunk is a easy-to-use pythonic 2D physics library

`pip install pymunk` · installs (wheel) · licence: MIT · rank 6956 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pymunk/) · [docs](https://www.pymunk.org) · [source](https://github.com/viblo/pymunk.git)

<details><summary>README extract</summary>

Pymunk is an easy-to-use pythonic 2D physics library that can be used whenever
you need 2D rigid body physics from Python. Perfect when you need 2D physics
in your game, demo or simulation! It is built on top of Munk2D, a fork of the
very capable 2D physics library Chipmunk2D. ...

Example:
```python
import pymunk               # Import pymunk..

space = pymunk.Space()      # Create a Space which contain the simulation
space.gravity = 0,-981      # Set its gravity

body = pymunk.Body()        # Create a Body
body.position = 50,100      # Set the position of the body

poly = pymunk.Poly.create_box(body) # Create a box shape and attach to body
...
```

Sections: Pymunk, Example, Documentation, The Pymunk Vision, Dependencies / Requirements, Older Pythons

</details>

### mcpforunityserver

MCP for Unity Server: A Unity package for Unity Editor integration via the Model Context Protocol (MCP).

`pip install mcpforunityserver` · installs (wheel) · licence: MIT · rank 7254 · last release 2026-10-04 · [PyPI](https://pypi.org/project/mcpforunityserver/) · [docs](https://coplaydev.github.io/unity-mcp/) · [source](https://github.com/CoplayDev/unity-mcp.git)

<details><summary>README extract</summary>

Model Context Protocol server for Unity Editor integration. Control Unity through natural language using AI assistants like Claude, Cursor, and more.

Maintained by Coplay - This project is not affiliated with Unity Technologies.

💬 Join our community: Discord Server ...

Sections: MCP for Unity Server, Option 1: PyPI, Option 2: From GitHub Source, Option 3: Docker, Configuration, CLI options, Environment variables, Examples, Remote-Hosted Mode, MCP Resources, Example Prompts, Documentation, Requirements

</details>

### moderngl-window

A cross platform helper library for ModernGL making window creation and resource loading simple

`pip install moderngl-window` · installs (wheel) · licence: MIT License · rank 7917 · last release 2025-01-19 · [PyPI](https://pypi.org/project/moderngl-window/) · [docs](https://moderngl-window.readthedocs.io) · [source](https://github.com/moderngl/moderngl_window)

<details><summary>README extract</summary>

A cross platform utility library for ModernGL making window
creation and resource loading simple. It can also be used with PyOpenGL for
rendering with the programmable pipeline.

* moderngl-window Documentation
* moderngl-window on PyPI
* moderngl-window on Github
* ModernGL
* ModernGL Discord Server ...

Features:
* Cross platform support. Tested on Windows 10, Linux and Mac OS X.
 This can save users a lot of time and is often more difficult than most people
 imagine it to be. ...

Example:
```python
# test.py
import moderngl_window as mglw

class Test(mglw.WindowConfig):
    gl_version = (3, 3)

    def on_render(self, time: float, frametime: float):
        self.ctx.clear(1.0, 0.0, 0.0, 0.0)

Test.run()
```

...

</details>

### Panda3D

Panda3D is a framework for 3D rendering and game development for Python and C++ programs.

`pip install Panda3D` · installs (wheel) · licence: BSD License · rank 8047 · last release 2025-12-25 · [PyPI](https://pypi.org/project/Panda3D/) · [docs](https://www.panda3d.org/manual/) · [source](https://github.com/panda3d/panda3d)

<details><summary>README extract</summary>

Panda3D is a powerful 3D engine written in C++, with a complete set of Python
bindings. Unlike other engines, these bindings are automatically generated,
meaning that they are always up-to-date and complete: all functions of the
engine can be controlled from Python. ...

</details>

### fortune

Python version of old BSD Unix fortune program

`pip install fortune` · installs (wheel) · licence: Apache Software License · rank 10674 · last release 2023-05-24 · [PyPI](https://pypi.org/project/fortune/)

<details><summary>README extract</summary>

`fortune` is a stripped-down implementation of the classic BSD Unix
`fortune` command. It combines the capabilities of the `strfile` command
(which produces the fortune index file) and the `fortune` command (which
displays a random fortune). It reads the traditional `fortune` program's
text file format.

Sections: Introduction, Usage, Fortune Cookie File Format, Generating a Random Fortune, Differences

</details>

### open-spiel

A Framework for Reinforcement Learning in Games

`pip install open-spiel` · installs (wheel) · licence: Apache-2.0 · rank 11880 · last release 2026-08-12 · [PyPI](https://pypi.org/project/open-spiel/) · [docs](https://openspiel.readthedocs.io/) · [source](https://github.com/deepmind/open_spiel.git)

<details><summary>README extract</summary>

OpenSpiel is a collection of environments and algorithms for research in general
reinforcement learning and search/planning in games. OpenSpiel supports n-player
(single- and multi- agent) zero-sum, cooperative and general-sum, one-shot and
sequential, strictly turn-taking and simultaneous-move, perfect and imperfect
information games, as well as ...

Sections: OpenSpiel: A Framework for Reinforcement Learning in Games, Index, Versioning

</details>

### python-a2s

Query Source and GoldSource servers for name, map, players and more.

`pip install python-a2s` · installs (wheel) · licence: MIT License · rank 12223 · last release 2026-06-15 · [PyPI](https://pypi.org/project/python-a2s/)

<details><summary>README extract</summary>

Library to query Source and GoldSource servers.
Implements Valve's Server Query Protocol.
Rewrite of the python-valve module.
Supports both synchronous and asyncronous applications.

Official demo application: Sourcequery

Python >=3.9, no external dependencies

Example:
```python
>>> import a2s
>>> address = ("chi-1.us.uncletopia.com", 27015)
>>> a2s.info(address)
SourceInfo(protocol=17, server_name='Uncletopia | Chicago | 1', map_name='pl_badwater',
folder='tf', game='Team Fortress', app_id=440, player_count=24, max_players=24, bot_count=0,
...
```

Sections: Python A2S, Requirements, API, Functions, Parameters, Return Values, Exceptions, Examples, Notes, Tested Games, Similar Projects

</details>

### mcstatus

A library to query Minecraft Servers for their status and capabilities.

`pip install mcstatus` · installs (wheel) · licence: Apache-2.0 · rank 12399 · last release 2026-09-02 · [PyPI](https://pypi.org/project/mcstatus/) · [docs](https://mcstatus.readthedocs.io) · [source](https://github.com/py-mine/mcstatus)

<details><summary>README extract</summary>

Example:
```python
from mcstatus import JavaServer

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use JavaServer("example.org", 1234)
server = JavaServer.lookup("example.org:1234")

...
```

Sections: Usage, Python API, Java Edition (1.7+), Java Edition (Beta 1.8-1.6), Bedrock Edition, Command Line Interface

</details>

### imgui

Cython-based Python bindings for dear imgui

`pip install imgui` · installs from source (sdist only) · licence: BSD License · rank 12453 · last release 2023-04-19 · [PyPI](https://pypi.org/project/imgui/)

<details><summary>README extract</summary>

Python bindings for the amazing
dear imgui C++ library - a Bloat-free
Immediate Mode Graphical User Interface.

Documentation: pyimgui.readthedocs.io

Sections: pyimgui, Project distribution

</details>

### godot-ai

Production-grade MCP server and AI tools for the Godot engine

`pip install godot-ai` · installs (wheel) · licence: not stated · rank 13013 · last release 2026-11-03 · [PyPI](https://pypi.org/project/godot-ai/) · [docs](https://github.com/hi-godot/godot-ai#readme) · [source](https://github.com/hi-godot/godot-ai)

<details><summary>README extract</summary>

**Godot AI connects Claude Code, Codex, Cursor, and other
MCP clients to a live Godot
editor.** Its 46 tools and 120+ operations build scenes, edit
nodes and scripts, wire signals, and configure UI, materials, animation,
particles, cameras, and environments. ...

Sections: Godot AI, Quick start, Try it, Privacy, Docs and help

</details>

### treys

treys is a pure Python poker hand evaluation library

`pip install treys` · installs (wheel) · licence: MIT License · rank 13115 · last release 2022-06-21 · [PyPI](https://pypi.org/project/treys/)

<details><summary>README extract</summary>

A pure Python poker hand evaluation library

Example:
```python
>>> from treys import Card
>>> card = Card.new('Qh')
```

Sections: Treys, Implementation notes, Usage

</details>

### crowdypy

Official Python SDK for Crowded Kingdoms: typed GraphQL clients and a native UDP replication core

`pip install crowdypy` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 13375 · last release 2026-11-04 · [PyPI](https://pypi.org/project/crowdypy/) · [docs](https://github.com/CrowdedKingdoms/CrowdyPy#readme) · [source](https://github.com/CrowdedKingdoms/CrowdyPy)

<details><summary>README extract</summary>

The official Python SDK for Crowded Kingdoms: typed clients for the platform's one
GraphQL API (identity, studio administration, world data, ck-exec) and a native UDP
replication core. ...

Example:
```python
import asyncio

import crowdypy

API = "

async def main() -> None:
    # The identity client: sign-in, account and studio calls, minting.
    async with crowdypy.AsyncCrowdyClient(http_url=API) as identity:
        await identity.auth.login("player@example.com", "correct-horse-battery")
        minted = await identity.portal.mint_app_token("42")

...
```

Sections: CrowdyPy, Quick start, Two tokens, two clients, Errors, Player safety, Replication, Voice, World Stores, Game Kit, Crowdy Studio, Performance

</details>

## Also in this topic

- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
