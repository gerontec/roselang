# Software Development / User Interfaces

[Index](README.md) · 10 packages in this topic, 213 more listed under another topic, by downloads.

### rich-argparse

Rich help formatters for argparse and optparse

`pip install rich-argparse` · installs (wheel) · licence: MIT · rank 1018 · last release 2026-05-01 · [PyPI](https://pypi.org/project/rich-argparse/) · [docs](https://github.com/hamdanal/rich-argparse#rich-argparse)

<details><summary>README extract</summary>

Format argparse and optparse help using rich.

*rich-argparse* improves the look and readability of argparse's help while requiring minimal
changes to the code.

Example:
```python
import argparse
from rich_argparse import RichHelpFormatter

parser = argparse.ArgumentParser(..., formatter_class=RichHelpFormatter)
...
```

Sections: rich-argparse, Usage, Output styles, Customize the colors, Customize the group name format, Special text highlighting, Colors in the `usage`, Disable console markup, Colors in `--version`, Rich descriptions and epilog, Working with subparsers, Generate help preview, Additional formatters

</details>

### easygui

EasyGUI is a module for very simple, very easy GUI programming in Python. EasyGUI is different from other GUI generators in that EasyGUI is NOT event-driven. Instead, all GUI interactions are invoked by simple function calls.

`pip install easygui` · installs (wheel) · licence: BSD License · rank 1203 · last release 2022-04-01 · [PyPI](https://pypi.org/project/easygui/)

<details><summary>README extract</summary>

Hi everyone. There hasn't been much activity but thankfully we have a new revision. Thank you contributors and thank you Stephen Ferg for creating EasyGui.

You might also consider the following alternatives:

For those who wish to contribute you are welcome to fork this respository. Or, take a look at the alternatives and contribute there. ...

Sections: Project in Maintainance, EasyGUI, 0.98.3, 0.98.2, 0.98.0, 0.97.4, 0.97.3

</details>

### about-time

Easily measure timing and throughput of code blocks, with beautiful human friendly representations.

`pip install about-time` · installs (wheel) · licence: MIT · rank 2520 · last release 2025-07-23 · [PyPI](https://pypi.org/project/about-time/) · [source](https://github.com/rsalmei/about-time)

<details><summary>README extract</summary>

[](
[](

Features:
According to the SI standard, there are 1000 bytes in a `kilobyte`.

There is another standard called IEC that has 1024 bytes in a `kibibyte`, but this is only useful when measuring things that are naturally a power of two, e.g. a stick of RAM. ...

Example:
```python
from about_time import about_time

def some_func():
    import time
    time.sleep(85e-3)
    return True

def main():
    with about_time() as t1:  # <-- use it like a context manager!

        t2 = about_time(some_func)  # <-- use it with any callable!!

...
```

Sections: about-time, What does it do?, Get it, Use it, 1. Use it like a context manager, 2. Use it with any callable, 3. Use it with any iterable or generator, Features, The human duration magic, The human throughput magic, Accuracy

</details>

### QtAwesome

FontAwesome icons in PyQt and PySide applications

`pip install QtAwesome` · installs (wheel) · licence: MIT License · rank 8631 · last release 2026-04-10 · [PyPI](https://pypi.org/project/QtAwesome/)

<details><summary>README extract</summary>

*Copyright © 2015- Spyder Project Contributors*

QtAwesome enables iconic fonts such as Font Awesome and Elusive Icons
in PyQt and PySide applications.

It started as a Python port of the QtAwesome
C++ library by Rick Blommers.

Example:
```python
import qtawesome as qta
```

Sections: QtAwesome, Description, Usage, Examples, Other features, Icon Browser

</details>

### wxPython

Cross platform GUI toolkit for Python, "Phoenix" version

`pip install wxPython` · installs from source (sdist only) · licence: LGPL-2.0-or-later WITH WxWindows-exception-3.1 · rank 9269 · last release 2026-10-16 · [PyPI](https://pypi.org/project/wxPython/) · [docs](https://docs.wxpython.org/) · [source](https://github.com/wxWidgets/Phoenix.git)

_README extract left out: share-alike licence._

### tuna

Visualize Python performance profiles

`pip install tuna` · installs (wheel) · licence: GPL-3.0-or-later · rank 11270 · last release 2026-05-19 · [PyPI](https://pypi.org/project/tuna/) · [source](https://github.com/nschloe/tuna)

_README extract left out: share-alike licence._

### asciimatics

A cross-platform package to replace curses (mouse/keyboard input & text colours/positioning) and create ASCII animations

`pip install asciimatics` · installs (wheel) · licence: Apache Software License · rank 12593 · last release 2023-10-25 · [PyPI](https://pypi.org/project/asciimatics/)

<details><summary>README extract</summary>

Asciimatics is a package to help people create full-screen text UIs (from interactive forms to
ASCII animations) on any platform. It is licensed under the Apache Software Foundation License 2.0.

Features:
Why not? It brings a little joy to anyone who was programming in the 80s... Oh and it provides a
single cross-platform Python class to do all the low-level console function you could ask for,
including: ...

Example:
```python
from random import randint
from asciimatics.screen import Screen

def demo(screen):
    while True:
        screen.print_at('Hello world!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
...
```

...

</details>

### reacton

(no summary)

`pip install reacton` · installs (wheel) · licence: MIT License · rank 12688 · last release 2026-11-07 · [PyPI](https://pypi.org/project/reacton/) · [docs](https://reacton.solara.dev) · [source](https://www.github.com/widgetti/reacton)

### ttkbootstrap

Modern themes for Tkinter. Sleek, responsive styles inspired by Bootstrap. Includes ready-to-use widgets, 30+ themes, and tools for building beautiful, cross-platform desktop apps with ease.

`pip install ttkbootstrap` · installs (wheel) · licence: MIT AND (Apache-2.0 OR BSD-2-Clause) · rank 12723 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ttkbootstrap/) · [docs](https://www.ttkbootstrap.org/en/latest/)

<details><summary>README extract</summary>

Modern, themed tkinter — style any ttk widget with one keyword.

ttkbootstrap is a theming extension for tkinter. It generates flat,
Bootstrap-inspired light and dark themes on demand and adds a single ``bootstyle``
keyword to every ttk widget, so you describe *intent* — ``"primary"``,
``"success"``, ``"outline"`` — instead of hand-tuning colors ...

Features:
- 🎨 30 curated themes — fifteen families, each in a coordinated light and dark variant, that switch at runtime.
- ⌨️ One-keyword styling — `bootstyle="success"`, `bootstyle="info outline"`, `bootstyle="round toggle"`. ...

Example:
```python
import ttkbootstrap as ttk

app = ttk.App(title="Hello")

ttk.Label(app, text="Hello from ttkbootstrap!").pack(padx=16, pady=(16, 8))
...

</details>

### click-shell

An extension to click that easily turns your click app into a shell utility

`pip install click-shell` · installs (wheel) · licence: BSD License · rank 14664 · last release 2021-06-27 · [PyPI](https://pypi.org/project/click-shell/)

<details><summary>README extract</summary>

click-shell is an extension to click that easily turns your click app into a shell utility.
It is built on top of the built in python cmd module, with modifications to make it work with click.

Features:
* Adds a "shell" mode with command completion to any click app
* Just a one line change for most click apps

Example:
```python
from click_shell import shell

# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    pass

@my_app.command()
def testcommand():
    print('testcommand is running')

# more commands

if name == 'main':
    my_app()
```

Sections: click-shell, Features, Usage

</details>

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [inquirerpy](software-development.md#inquirerpy) - Python port of Inquirer.js (A collection of common interactive command-line user interfaces)
- [readchar](software-development.md#readchar) - Library to easily read single chars and key strokes
- [blessed](software-development-libraries.md#blessed) - Easy, practical library for making terminal apps, by providing an elegant, well-documented interface for Terminals.
- [gradio-client](scientific-engineering.md#gradio-client) - Python library for easily interacting with trained machine learning models
- [urwid](software-development-libraries.md#urwid) - A full-featured console (xterm et al.) user interface library
- [PySide6-Essentials](database.md#pyside6-essentials) - Python bindings for the Qt cross-platform application and UI framework (Essentials)
- [shiboken6](database.md#shiboken6) - Python/C++ bindings helper module
- [yaspin](software-development.md#yaspin) - Yet Another Terminal Spinner
- [PySide6-Addons](database.md#pyside6-addons) - Python bindings for the Qt cross-platform application and UI framework (Addons)
- [PySide6](database.md#pyside6) - Python bindings for the Qt cross-platform application and UI framework
- [inquirer](software-development-libraries.md#inquirer) - Collection of common interactive command line user interfaces, based on Inquirer.js
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [ibis-framework](database-front-ends.md#ibis-framework) - The portable Python dataframe library
- [python-xlib](software-development-libraries.md#python-xlib) - Python X Library
- [QtPy](software-development-libraries.md#qtpy) - Provides an abstraction layer on top of the various Qt bindings (PyQt5/6 and PySide2/6).
- [pywebview](software-development-libraries-2.md#pywebview) - Build GUI for your Python program with JavaScript, HTML, and CSS
- [PySide6-WebEngine](database.md#pyside6-webengine) - Python bindings for the Qt cross-platform application and UI framework (WebEngine)
- [PySide6-Pdf](database.md#pyside6-pdf) - Python bindings for the Qt cross-platform application and UI framework (Pdf)
- [pyobjc-core](software-development-libraries-2.md#pyobjc-core) - Python<->ObjC Interoperability Module
- [pyobjc-framework-Cocoa](software-development-libraries-2.md#pyobjc-framework-cocoa) - Wrappers for the Cocoa frameworks on macOS
- [ct3](internet-www-http.md#ct3) - Cheetah is a template engine and code generation tool
- [argh](software-development-libraries-2.md#argh) - Plain Python functions as CLI commands without boilerplate
- [nicegui](internet-www-http.md#nicegui) - Create web-based user interfaces with Python. The nice way.
- [pyobjc-framework-Quartz](software-development-libraries-2.md#pyobjc-framework-quartz) - Wrappers for the Quartz frameworks on macOS
- [pytest-qt](desktop-environment-window-managers.md#pytest-qt) - pytest support for PyQt and PySide applications
- [pyqtgraph](scientific-engineering-visualization.md#pyqtgraph) - Scientific Graphics and GUI Library for Python
- [pywinauto](software-development-libraries-2.md#pywinauto) - A set of Python modules to automate the Microsoft Windows GUI
- [frappe-bench](software-development-build-tools.md#frappe-bench) - CLI to manage Multi-tenant deployments for Frappe apps
- [unitycatalog-client](scientific-engineering.md#unitycatalog-client) - Official Python SDK for Unity Catalog
- [blessings](software-development-libraries-2.md#blessings) - A thin, practical wrapper around terminal coloring, styling, and positioning
- [unitycatalog-ai](scientific-engineering.md#unitycatalog-ai) - Official Python library for Unity Catalog AI support
- [progressbar](software-development-libraries-2.md#progressbar) - Text progress bar library for Python.
- [textual-image](software-development-libraries-2.md#textual-image) - Render images via Kitty's Terminal Graphics Protocol with Rich and Textual
- [pyobjc-framework-ApplicationServices](software-development-libraries-2.md#pyobjc-framework-applicationservices) - Wrappers for the framework ApplicationServices on macOS
- [pyobjc-framework-CoreText](software-development-libraries-2.md#pyobjc-framework-coretext) - Wrappers for the framework CoreText on macOS
- [traits](scientific-engineering.md#traits) - Observable typed attributes for Python classes
- [chainlit](communications-chat.md#chainlit) - Build Conversational AI.
- [pyobjc-framework-CoreML](software-development-libraries-2.md#pyobjc-framework-coreml) - Wrappers for the framework CoreML on macOS
- [pyobjc-framework-Vision](software-development-libraries-2.md#pyobjc-framework-vision) - Wrappers for the framework Vision on macOS
- [pyobjc-framework-WebKit](software-development-libraries-2.md#pyobjc-framework-webkit) - Wrappers for the framework WebKit on macOS
- [pyobjc-framework-Security](software-development-libraries-2.md#pyobjc-framework-security) - Wrappers for the framework Security on macOS
- [pyobjc-framework-UniformTypeIdentifiers](software-development-libraries-2.md#pyobjc-framework-uniformtypeidentifiers) - Wrappers for the framework UniformTypeIdentifiers on macOS
- [html2image](multimedia-graphics.md#html2image) - Package acting as a wrapper around the headless mode of existing web browsers to generate images from URLs and from HTML+CSS strings or files.
- [imgui-bundle](artistic-software.md#imgui-bundle) - Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.
- [Cheetah3](internet-www-http.md#cheetah3) - Cheetah is a template engine and code generation tool
- [inquirer3](software-development-libraries-3.md#inquirer3) - Collection of common interactive command line user interfaces, based on Inquirer.js
- [superqt](desktop-environment.md#superqt) - Missing widgets and components for PyQt/PySide
- [pyobjc-framework-CoreAudio](software-development-libraries-3.md#pyobjc-framework-coreaudio) - Wrappers for the framework CoreAudio on macOS
- [dearpygui](software-development-libraries-3.md#dearpygui) - DearPyGui: A simple Python GUI Toolkit
- [pyobjc-framework-CoreBluetooth](software-development-libraries-3.md#pyobjc-framework-corebluetooth) - Wrappers for the framework CoreBluetooth on macOS
- [pyobjc-framework-libdispatch](software-development-libraries-3.md#pyobjc-framework-libdispatch) - Wrappers for libdispatch on macOS
- [pyobjc-framework-CoreMedia](software-development-libraries-3.md#pyobjc-framework-coremedia) - Wrappers for the framework CoreMedia on macOS
- [pyobjc-framework-FSEvents](software-development-libraries-3.md#pyobjc-framework-fsevents) - Wrappers for the framework FSEvents on macOS
- [progressbar33](software-development-libraries-3.md#progressbar33) - Text progress bar library for Python.
- [pyobjc-framework-AVFoundation](software-development-libraries-3.md#pyobjc-framework-avfoundation) - Wrappers for the framework AVFoundation on macOS
- [pyobjc-framework-CoreServices](software-development-libraries-3.md#pyobjc-framework-coreservices) - Wrappers for the framework CoreServices on macOS
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [magicgui](desktop-environment.md#magicgui) - build GUIs from python types
- [pyobjc-framework-CoreLocation](software-development-libraries-3.md#pyobjc-framework-corelocation) - Wrappers for the framework CoreLocation on macOS
- [pyobjc-framework-Contacts](software-development-libraries-3.md#pyobjc-framework-contacts) - Wrappers for the framework Contacts on macOS
- [pyobjc-framework-SystemConfiguration](software-development-libraries-3.md#pyobjc-framework-systemconfiguration) - Wrappers for the framework SystemConfiguration on macOS
- [pyobjc-framework-Metal](software-development-libraries-3.md#pyobjc-framework-metal) - Wrappers for the framework Metal on macOS
- [app-model](desktop-environment.md#app-model) - Generic application schema implemented in python
- [pyobjc-framework-AppleScriptKit](software-development-libraries-3.md#pyobjc-framework-applescriptkit) - Wrappers for the framework AppleScriptKit on macOS
- [pyobjc-framework-Photos](software-development-libraries-3.md#pyobjc-framework-photos) - Wrappers for the framework Photos on macOS
- [pyobjc-framework-EventKit](software-development-libraries-3.md#pyobjc-framework-eventkit) - Wrappers for the framework Accounts on macOS
- [pyobjc-framework-AppleScriptObjC](software-development-libraries-4.md#pyobjc-framework-applescriptobjc) - Wrappers for the framework AppleScriptObjC on macOS
- [pyobjc](software-development-libraries-4.md#pyobjc) - Python<->ObjC Interoperability Module
- [pyobjc-framework-ScreenSaver](software-development-libraries-4.md#pyobjc-framework-screensaver) - Wrappers for the framework ScreenSaver on macOS
- [pyobjc-framework-ScreenCaptureKit](software-development-libraries-4.md#pyobjc-framework-screencapturekit) - Wrappers for the framework ScreenCaptureKit on macOS
- [PySide2](database.md#pyside2) - Python bindings for the Qt cross-platform application and UI framework
- [pyobjc-framework-CFNetwork](software-development-libraries-4.md#pyobjc-framework-cfnetwork) - Wrappers for the framework CFNetwork on macOS
- [pyobjc-framework-SyncServices](software-development-libraries-4.md#pyobjc-framework-syncservices) - Wrappers for the framework SyncServices on macOS
- [pyobjc-framework-AddressBook](software-development-libraries-4.md#pyobjc-framework-addressbook) - Wrappers for the framework AddressBook on macOS
- [pyobjc-framework-ScriptingBridge](software-development-libraries-4.md#pyobjc-framework-scriptingbridge) - Wrappers for the framework ScriptingBridge on macOS
- [snowflake-id](software-development.md#snowflake-id) - The Snowflake generator done right
- [pyobjc-framework-CoreData](software-development-libraries-4.md#pyobjc-framework-coredata) - Wrappers for the framework CoreData on macOS
- [pyobjc-framework-Automator](software-development-libraries-4.md#pyobjc-framework-automator) - Wrappers for the framework Automator on macOS
- [pyobjc-framework-SecurityInterface](software-development-libraries-4.md#pyobjc-framework-securityinterface) - Wrappers for the framework SecurityInterface on macOS
- [pyobjc-framework-DiscRecording](software-development-libraries-4.md#pyobjc-framework-discrecording) - Wrappers for the framework DiscRecording on macOS
- [pyobjc-framework-CoreAudioKit](software-development-libraries-4.md#pyobjc-framework-coreaudiokit) - Wrappers for the framework CoreAudioKit on macOS
- [pyobjc-framework-IOBluetooth](software-development-libraries-4.md#pyobjc-framework-iobluetooth) - Wrappers for the framework IOBluetooth on macOS
- [pyobjc-framework-LaunchServices](software-development-libraries-4.md#pyobjc-framework-launchservices) - Wrappers for the framework LaunchServices on macOS
- [pyobjc-framework-CoreMIDI](software-development-libraries-4.md#pyobjc-framework-coremidi) - Wrappers for the framework CoreMIDI on macOS
- [pyobjc-framework-ExceptionHandling](software-development-libraries-4.md#pyobjc-framework-exceptionhandling) - Wrappers for the framework ExceptionHandling on macOS
- [pyobjc-framework-OSAKit](software-development-libraries-4.md#pyobjc-framework-osakit) - Wrappers for the framework OSAKit on macOS
- [pyobjc-framework-LatentSemanticMapping](software-development-libraries-4.md#pyobjc-framework-latentsemanticmapping) - Wrappers for the framework LatentSemanticMapping on macOS
- [pyobjc-framework-InstallerPlugins](software-development-libraries-4.md#pyobjc-framework-installerplugins) - Wrappers for the framework InstallerPlugins on macOS
- [pyobjc-framework-SearchKit](software-development-libraries-4.md#pyobjc-framework-searchkit) - Wrappers for the framework SearchKit on macOS
- [pyobjc-framework-PreferencePanes](software-development-libraries-4.md#pyobjc-framework-preferencepanes) - Wrappers for the framework PreferencePanes on macOS
- [pyobjc-framework-DiskArbitration](software-development-libraries-4.md#pyobjc-framework-diskarbitration) - Wrappers for the framework DiskArbitration on macOS
- [pyobjc-framework-SecurityFoundation](software-development-libraries-4.md#pyobjc-framework-securityfoundation) - Wrappers for the framework SecurityFoundation on macOS
- [pyobjc-framework-DVDPlayback](software-development-libraries-4.md#pyobjc-framework-dvdplayback) - Wrappers for the framework DVDPlayback on macOS
- [pyobjc-framework-DiscRecordingUI](software-development-libraries-4.md#pyobjc-framework-discrecordingui) - Wrappers for the framework DiscRecordingUI on macOS
- [pyobjc-framework-LocalAuthentication](software-development-libraries-4.md#pyobjc-framework-localauthentication) - Wrappers for the framework LocalAuthentication on macOS
- [pyobjc-framework-UserNotifications](software-development-libraries-4.md#pyobjc-framework-usernotifications) - Wrappers for the framework UserNotifications on macOS
- [pyobjc-framework-Speech](software-development-libraries-4.md#pyobjc-framework-speech) - Wrappers for the framework Speech on macOS
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [pyobjc-framework-IOBluetoothUI](software-development-libraries-4.md#pyobjc-framework-iobluetoothui) - Wrappers for the framework IOBluetoothUI on macOS
- [pyobjc-framework-CoreWLAN](software-development-libraries-4.md#pyobjc-framework-corewlan) - Wrappers for the framework CoreWLAN on macOS
- [pyobjc-framework-ServiceManagement](software-development-libraries-4.md#pyobjc-framework-servicemanagement) - Wrappers for the framework ServiceManagement on macOS
- [pyobjc-framework-ImageCaptureCore](software-development-libraries-4.md#pyobjc-framework-imagecapturecore) - Wrappers for the framework ImageCaptureCore on macOS
- [pyobjc-framework-Accessibility](software-development-libraries-4.md#pyobjc-framework-accessibility) - Wrappers for the framework Accessibility on macOS
- [pyobjc-framework-Intents](software-development-libraries-4.md#pyobjc-framework-intents) - Wrappers for the framework Intents on macOS
- [pyobjc-framework-AVKit](software-development-libraries-4.md#pyobjc-framework-avkit) - Wrappers for the framework AVKit on macOS
- [pyobjc-framework-MapKit](software-development-libraries-4.md#pyobjc-framework-mapkit) - Wrappers for the framework MapKit on macOS
- [pyobjc-framework-SpriteKit](software-development-libraries-4.md#pyobjc-framework-spritekit) - Wrappers for the framework SpriteKit on macOS
- [pyobjc-framework-CryptoTokenKit](software-development-libraries-4.md#pyobjc-framework-cryptotokenkit) - Wrappers for the framework CryptoTokenKit on macOS
- [pyobjc-framework-CoreSpotlight](software-development-libraries-4.md#pyobjc-framework-corespotlight) - Wrappers for the framework CoreSpotlight on macOS
- [pyobjc-framework-StoreKit](software-development-libraries-4.md#pyobjc-framework-storekit) - Wrappers for the framework StoreKit on macOS
- [pyobjc-framework-ContactsUI](software-development-libraries-4.md#pyobjc-framework-contactsui) - Wrappers for the framework ContactsUI on macOS
- [pyobjc-framework-GameCenter](software-development-libraries-4.md#pyobjc-framework-gamecenter) - Wrappers for the framework GameCenter on macOS
- [pyobjc-framework-MultipeerConnectivity](software-development-libraries-4.md#pyobjc-framework-multipeerconnectivity) - Wrappers for the framework MultipeerConnectivity on macOS
- [pyobjc-framework-SceneKit](software-development-libraries-4.md#pyobjc-framework-scenekit) - Wrappers for the framework SceneKit on macOS
- [pyobjc-framework-GameController](software-development-libraries-4.md#pyobjc-framework-gamecontroller) - Wrappers for the framework GameController on macOS
- [pyobjc-framework-ModelIO](software-development-libraries-4.md#pyobjc-framework-modelio) - Wrappers for the framework ModelIO on macOS
- [pyobjc-framework-SafariServices](software-development-libraries-4.md#pyobjc-framework-safariservices) - Wrappers for the framework SafariServices on macOS
- [pyobjc-framework-CoreMediaIO](software-development-libraries-4.md#pyobjc-framework-coremediaio) - Wrappers for the framework CoreMediaIO on macOS
- [pyobjc-framework-Network](software-development-libraries-4.md#pyobjc-framework-network) - Wrappers for the framework Network on macOS
- [pyobjc-framework-NetworkExtension](software-development-libraries-4.md#pyobjc-framework-networkextension) - Wrappers for the framework NetworkExtension on macOS
- [pyobjc-framework-FileProvider](software-development-libraries-4.md#pyobjc-framework-fileprovider) - Wrappers for the framework FileProvider on macOS
- [pyobjc-framework-NotificationCenter](software-development-libraries-4.md#pyobjc-framework-notificationcenter) - Wrappers for the framework NotificationCenter on macOS
- [pyobjc-framework-MetalPerformanceShaders](software-development-libraries-4.md#pyobjc-framework-metalperformanceshaders) - Wrappers for the framework MetalPerformanceShaders on macOS
- [pyobjc-framework-PhotosUI](software-development-libraries-4.md#pyobjc-framework-photosui) - Wrappers for the framework PhotosUI on macOS
- [pyobjc-framework-ExternalAccessory](software-development-libraries-4.md#pyobjc-framework-externalaccessory) - Wrappers for the framework ExternalAccessory on macOS
- [pyobjc-framework-GameplayKit](software-development-libraries-4.md#pyobjc-framework-gameplaykit) - Wrappers for the framework GameplayKit on macOS
- [pyobjc-framework-VideoToolbox](software-development-libraries-4.md#pyobjc-framework-videotoolbox) - Wrappers for the framework VideoToolbox on macOS
- [pyobjc-framework-MetalKit](software-development-libraries-4.md#pyobjc-framework-metalkit) - Wrappers for the framework MetalKit on macOS
- [pyobjc-framework-GameKit](software-development-libraries-4.md#pyobjc-framework-gamekit) - Wrappers for the framework GameKit on macOS
- [pyobjc-framework-AuthenticationServices](software-development-libraries-4.md#pyobjc-framework-authenticationservices) - Wrappers for the framework AuthenticationServices on macOS
- [pyobjc-framework-MediaToolbox](software-development-libraries-4.md#pyobjc-framework-mediatoolbox) - Wrappers for the framework MediaToolbox on macOS
- [pyobjc-framework-CoreMotion](software-development-libraries-4.md#pyobjc-framework-coremotion) - Wrappers for the framework CoreMotion on macOS
- [pyobjc-framework-AutomaticAssessmentConfiguration](software-development-libraries-4.md#pyobjc-framework-automaticassessmentconfiguration) - Wrappers for the framework AutomaticAssessmentConfiguration on macOS
- [pyobjc-framework-PushKit](software-development-libraries-4.md#pyobjc-framework-pushkit) - Wrappers for the framework PushKit on macOS
- [pyobjc-framework-OSLog](software-development-libraries-4.md#pyobjc-framework-oslog) - Wrappers for the framework OSLog on macOS
- [pyobjc-framework-SystemExtensions](software-development-libraries-4.md#pyobjc-framework-systemextensions) - Wrappers for the framework SystemExtensions on macOS
- [pyobjc-framework-AudioVideoBridging](software-development-libraries-4.md#pyobjc-framework-audiovideobridging) - Wrappers for the framework AudioVideoBridging on macOS
- [pyobjc-framework-Virtualization](software-development-libraries-4.md#pyobjc-framework-virtualization) - Wrappers for the framework Virtualization on macOS
- [pyobjc-framework-PassKit](software-development-libraries-4.md#pyobjc-framework-passkit) - Wrappers for the framework PassKit on macOS
- [pyobjc-framework-IntentsUI](software-development-libraries-4.md#pyobjc-framework-intentsui) - Wrappers for the framework Intents on macOS
- [pyobjc-framework-ReplayKit](software-development-libraries-4.md#pyobjc-framework-replaykit) - Wrappers for the framework ReplayKit on macOS
- [pyobjc-framework-CallKit](software-development-libraries-4.md#pyobjc-framework-callkit) - Wrappers for the framework CallKit on macOS
- [pyobjc-framework-ClassKit](software-development-libraries-4.md#pyobjc-framework-classkit) - Wrappers for the framework ClassKit on macOS
- [pyobjc-framework-ShazamKit](software-development-libraries-4.md#pyobjc-framework-shazamkit) - Wrappers for the framework ShazamKit on macOS
- [pyobjc-framework-MetricKit](software-development-libraries-4.md#pyobjc-framework-metrickit) - Wrappers for the framework MetricKit on macOS
- [pyobjc-framework-libxpc](software-development-libraries-4.md#pyobjc-framework-libxpc) - Wrappers for xpc on macOS
- [pyobjc-framework-MediaPlayer](software-development-libraries-4.md#pyobjc-framework-mediaplayer) - Wrappers for the framework MediaPlayer on macOS
- [pyobjc-framework-OpenDirectory](software-development-libraries-4.md#pyobjc-framework-opendirectory) - Wrappers for the framework OpenDirectory on macOS
- [pyobjc-framework-MetalFX](software-development-libraries-4.md#pyobjc-framework-metalfx) - Wrappers for the framework MetalFX on macOS
- [pyobjc-framework-HealthKit](software-development-libraries-4.md#pyobjc-framework-healthkit) - Wrappers for the framework HealthKit on macOS
- [pyobjc-framework-AVRouting](software-development-libraries-4.md#pyobjc-framework-avrouting) - Wrappers for the framework AVRouting on macOS
- [pyobjc-framework-SharedWithYou](software-development-libraries-4.md#pyobjc-framework-sharedwithyou) - Wrappers for the framework SharedWithYou on macOS
- [pyobjc-framework-BackgroundAssets](software-development-libraries-4.md#pyobjc-framework-backgroundassets) - Wrappers for the framework BackgroundAssets on macOS
- [pyobjc-framework-Accounts](software-development-libraries-4.md#pyobjc-framework-accounts) - Wrappers for the framework Accounts on macOS
- [pyobjc-framework-SharedWithYouCore](software-development-libraries-4.md#pyobjc-framework-sharedwithyoucore) - Wrappers for the framework SharedWithYouCore on macOS
- [pyobjc-framework-ExtensionKit](software-development-libraries-4.md#pyobjc-framework-extensionkit) - Wrappers for the framework ExtensionKit on macOS
- [pyobjc-framework-SafetyKit](software-development-libraries-4.md#pyobjc-framework-safetykit) - Wrappers for the framework SafetyKit on macOS
- [pyobjc-framework-Social](software-development-libraries-4.md#pyobjc-framework-social) - Wrappers for the framework Social on macOS
- [pyobjc-framework-NaturalLanguage](software-development-libraries-4.md#pyobjc-framework-naturallanguage) - Wrappers for the framework NaturalLanguage on macOS
- [pyobjc-framework-CloudKit](software-development-libraries-4.md#pyobjc-framework-cloudkit) - Wrappers for the framework CloudKit on macOS
- [pyobjc-framework-ColorSync](software-development-libraries-4.md#pyobjc-framework-colorsync) - Wrappers for the framework ColorSync on Mac OS X
- [pyobjc-framework-iTunesLibrary](software-development-libraries-4.md#pyobjc-framework-ituneslibrary) - Wrappers for the framework iTunesLibrary on macOS
- [pyobjc-framework-IOSurface](software-development-libraries-4.md#pyobjc-framework-iosurface) - Wrappers for the framework IOSurface on macOS
- [pyobjc-framework-NetFS](software-development-libraries-4.md#pyobjc-framework-netfs) - Wrappers for the framework NetFS on macOS
- [pyobjc-framework-BusinessChat](software-development-libraries-4.md#pyobjc-framework-businesschat) - Wrappers for the framework BusinessChat on macOS
- [pyobjc-framework-FinderSync](software-development-libraries-4.md#pyobjc-framework-findersync) - Wrappers for the framework FinderSync on macOS
- [pyobjc-framework-MediaLibrary](software-development-libraries-4.md#pyobjc-framework-medialibrary) - Wrappers for the framework MediaLibrary on macOS
- [pyobjc-framework-MediaAccessibility](software-development-libraries-4.md#pyobjc-framework-mediaaccessibility) - Wrappers for the framework MediaAccessibility on macOS
- [pyobjc-framework-AdSupport](software-development-libraries-4.md#pyobjc-framework-adsupport) - Wrappers for the framework AdSupport on macOS
- [pyobjc-framework-BrowserEngineKit](software-development-libraries-4.md#pyobjc-framework-browserenginekit) - Wrappers for the framework BrowserEngineKit on macOS
- [pyobjc-framework-VideoSubscriberAccount](software-development-libraries-4.md#pyobjc-framework-videosubscriberaccount) - Wrappers for the framework VideoSubscriberAccount on macOS
- [pyobjc-framework-SoundAnalysis](software-development-libraries-4.md#pyobjc-framework-soundanalysis) - Wrappers for the framework SoundAnalysis on macOS
- [pyobjc-framework-MetalPerformanceShadersGraph](software-development-libraries-4.md#pyobjc-framework-metalperformanceshadersgraph) - Wrappers for the framework MetalPerformanceShadersGraph on macOS
- [pyobjc-framework-FileProviderUI](software-development-libraries-4.md#pyobjc-framework-fileproviderui) - Wrappers for the framework FileProviderUI on macOS
- [pyobjc-framework-CoreHaptics](software-development-libraries-4.md#pyobjc-framework-corehaptics) - Wrappers for the framework CoreHaptics on macOS
- [pyobjc-framework-DeviceCheck](software-development-libraries-4.md#pyobjc-framework-devicecheck) - Wrappers for the framework DeviceCheck on macOS
- [pyobjc-framework-PencilKit](software-development-libraries-4.md#pyobjc-framework-pencilkit) - Wrappers for the framework PencilKit on macOS
- [pyobjc-framework-ExecutionPolicy](software-development-libraries-4.md#pyobjc-framework-executionpolicy) - Wrappers for the framework ExecutionPolicy on macOS
- [pyobjc-framework-QuickLookThumbnailing](software-development-libraries-4.md#pyobjc-framework-quicklookthumbnailing) - Wrappers for the framework QuickLookThumbnailing on macOS
- [pyobjc-framework-LinkPresentation](software-development-libraries-4.md#pyobjc-framework-linkpresentation) - Wrappers for the framework LinkPresentation on macOS
- [django-ajax-selects](software-development-libraries-4.md#django-ajax-selects) - Edit ForeignKey, ManyToManyField and CharField in Django Admin using jQuery UI AutoComplete.
- [pyobjc-framework-AppTrackingTransparency](software-development-libraries-4.md#pyobjc-framework-apptrackingtransparency) - Wrappers for the framework AppTrackingTransparency on macOS
- [pyobjc-framework-MLCompute](software-development-libraries-4.md#pyobjc-framework-mlcompute) - Wrappers for the framework MLCompute on macOS
- [pyobjc-framework-AdServices](software-development-libraries-4.md#pyobjc-framework-adservices) - Wrappers for the framework AdServices on macOS
- [pyobjc-framework-KernelManagement](software-development-libraries-4.md#pyobjc-framework-kernelmanagement) - Wrappers for the framework KernelManagement on macOS
- [pyobjc-framework-UserNotificationsUI](software-development-libraries-4.md#pyobjc-framework-usernotificationsui) - Wrappers for the framework UserNotificationsUI on macOS
- [pyobjc-framework-ScreenTime](software-development-libraries-4.md#pyobjc-framework-screentime) - Wrappers for the framework ScreenTime on macOS
- [pyobjc-framework-DataDetection](software-development-libraries-4.md#pyobjc-framework-datadetection) - Wrappers for the framework DataDetection on macOS
- [pyobjc-framework-LocalAuthenticationEmbeddedUI](software-development-libraries-4.md#pyobjc-framework-localauthenticationembeddedui) - Wrappers for the framework LocalAuthenticationEmbeddedUI on macOS
- [pyobjc-framework-MailKit](software-development-libraries-4.md#pyobjc-framework-mailkit) - Wrappers for the framework MailKit on macOS
- [pyobjc-framework-PHASE](software-development-libraries-4.md#pyobjc-framework-phase) - Wrappers for the framework PHASE on macOS
- [pyobjc-framework-ThreadNetwork](software-development-libraries-4.md#pyobjc-framework-threadnetwork) - Wrappers for the framework ThreadNetwork on macOS
- [pyobjc-framework-Cinematic](software-development-libraries-4.md#pyobjc-framework-cinematic) - Wrappers for the framework Cinematic on macOS
- [pyobjc-framework-Symbols](software-development-libraries-4.md#pyobjc-framework-symbols) - Wrappers for the framework Symbols on macOS
- [pyobjc-framework-SensitiveContentAnalysis](software-development-libraries-4.md#pyobjc-framework-sensitivecontentanalysis) - Wrappers for the framework SensitiveContentAnalysis on macOS
- [pyobjc-framework-Carbon](software-development-libraries-4.md#pyobjc-framework-carbon) - Wrappers for the framework Carbon on macOS
- [pyobjc-framework-InputMethodKit](software-development-libraries-4.md#pyobjc-framework-inputmethodkit) - Wrappers for the framework InputMethodKit on macOS
- [pyobjc-framework-MediaExtension](software-development-libraries-4.md#pyobjc-framework-mediaextension) - Wrappers for the framework MediaExtension on macOS
- [pyobjc-framework-Collaboration](software-development-libraries-4.md#pyobjc-framework-collaboration) - Wrappers for the framework Collaboration on macOS
- [pyobjc-framework-DictionaryServices](software-development-libraries-4.md#pyobjc-framework-dictionaryservices) - Wrappers for the framework DictionaryServices on macOS
- [pyobjc-framework-InstantMessage](software-development-libraries-4.md#pyobjc-framework-instantmessage) - Wrappers for the framework InstantMessage on macOS
- [pyobjc-framework-CalendarStore](software-development-libraries-4.md#pyobjc-framework-calendarstore) - Wrappers for the framework CalendarStore on macOS
- [pyobjc-framework-DeviceDiscoveryExtension](software-development-libraries-4.md#pyobjc-framework-devicediscoveryextension) - Wrappers for the framework DeviceDiscoveryExtension on macOS
- [pyobjc-framework-FSKit](software-development-libraries-4.md#pyobjc-framework-fskit) - Wrappers for the framework FSKit on macOS
- [pyobjc-framework-SecurityUI](software-development-libraries-4.md#pyobjc-framework-securityui) - Wrappers for the framework SecurityUI on macOS
- [clize](software-development.md#clize) - Turn functions into command-line interfaces
- [tabula](software-development-libraries-4.md#tabula) - Ascii table
- [shiboken2](database.md#shiboken2) - Python / C++ bindings helper module
- [xlib](software-development-libraries-5.md#xlib) - Python X Library
