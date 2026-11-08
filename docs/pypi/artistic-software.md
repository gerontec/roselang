# Artistic Software

[Index](README.md) · 10 packages in this topic, by downloads.

### music21

A Toolkit for Computer-Aided Musical Analysis and Computational Musicology.

`pip install music21` · installs (wheel) · licence: BSD-3-Clause · rank 4726 · last release 2026-10-28 · [PyPI](https://pypi.org/project/music21/) · [docs](https://www.music21.org/music21docs/)

<details><summary>README extract</summary>

`music21` -- A Toolkit for Computer-Aided Musical Analysis and
Computational Musicology

Copyright © 2006-2026 Michael Scott Asato Cuthbert

Released under the BSD (3-clause) license. See LICENSE and below.

For more information, visit:

To try it out, visit:
 (run all to set up an environment for the latest release)

And to install, see: ...

Sections: music21, Documentation, Mailing list

</details>

### descript-audiotools

Utilities for handling audio.

`pip install descript-audiotools` · installs (wheel) · licence: MIT · rank 4831 · last release 2023-07-19 · [PyPI](https://pypi.org/project/descript-audiotools/)

<details><summary>README extract</summary>

Object-oriented handling of audio signals, with fast augmentation routines, batching, padding, and more.

Example:
```python
import audiotools
from audiotools import AudioSignal

signal = AudioSignal("tests/audio/spk/f10_script4_produced.wav", offset=5, duration=5)
signal.play() # Play back the signal in your terminal using ffplay

signal.low_pass(8000) # Low-pass the signal
signal.play() # Play back the low-passed version of the signal
```

Sections: AudioTools, Documentation, Deploying documentation, Quickstart

</details>

### descript-audio-codec

A high-quality general neural audio codec.

`pip install descript-audio-codec` · installs (wheel) · licence: MIT · rank 5636 · last release 2023-07-20 · [PyPI](https://pypi.org/project/descript-audio-codec/)

<details><summary>README extract</summary>

This repository contains training and inference scripts
for the Descript Audio Codec (.dac), a high fidelity general
neural audio codec, introduced in the paper titled High-Fidelity Audio Compression with Improved RVQGAN.

 arXiv Paper: High-Fidelity Audio Compression with Improved RVQGAN

📈 Demo Site

⚙ Model Weights ...

Example:
```python
import dac
from audiotools import AudioSignal

# Download a model
model_path = dac.utils.download(model_type="44khz")
model = dac.DAC.load(model_path)

model.to('cuda')

# Load audio signal file
signal = AudioSignal('input.wav')

# Encode audio signal as one long file
# (may run out of GPU memory on long files)
signal.to(model.device)

...
```

...

</details>

### borb

borb is a library for reading, creating and manipulating PDF files in python.

`pip install borb` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 6022 · last release 2026-08-03 · [PyPI](https://pypi.org/project/borb/) · [source](https://github.com/borb-pdf/borb)

_README extract left out: share-alike licence._

### gerbonara

Tools to handle Gerber and Excellon files in Python

`pip install gerbonara` · installs (wheel) · licence: Apache-2.0 · rank 6483 · last release 2026-04-25 · [PyPI](https://pypi.org/project/gerbonara/) · [docs](https://gerbolyze.gitlab.io/gerbonara/) · [source](https://git.jaseg.de/gerbonara.git)

<details><summary>README extract</summary>

Tools to handle Gerber and Excellon files in Python.

This repository is a friendly fork of phsilva's pcb-tools with
extensions from opiopan integrated. We decided to fork pcb-tools since
we need it as a dependency for gerbolyze and pcb-tools was sometimes very
behind on bug fixes.

Sections: gerbonara, Documentation and Examples, Issues

</details>

### imgui-bundle

Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.

`pip install imgui-bundle` · installs (wheel) · licence: MIT License · rank 7347 · last release 2026-10-21 · [PyPI](https://pypi.org/project/imgui-bundle/) · [docs](https://imgui-bundle.pages.dev/doc/) · [source](https://github.com/pthom/imgui_bundle)

<details><summary>README extract</summary>

> “Dear ImGui Bundle: easily create applications in Python and C++. Batteries included! With very few lines of code, you can build a responsive GUI, and deploy it to desktop or directly in the browser.”

Dear ImGui Bundle is a collection of libraries around Dear ImGui, for both C++ and Python.

What for? ...

Features:
- Cross‑platform: Windows, macOS, Linux, iOS, Android, and WebAssembly.
- C++ and Python: APIs with very similar structure.

 - Dear ImGui (core widgets)
 - ImPlot / ImPlot3D (2D and 3D plotting)
 - ImmVision (image inspection)
 - ImAnim ...

Sections: Dear ImGui Bundle, Key features, Links

</details>

### Kivy

An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.

`pip install Kivy` · installs from source (sdist only) · licence: MIT License · rank 9005 · last release 2024-12-26 · [PyPI](https://pypi.org/project/Kivy/) · [docs](https://kivy.org/doc/stable/) · [source](https://github.com/kivy/kivy)

<details><summary>README extract</summary>

Kivy

====

Kivy is an open-source Python framework

for developing GUI apps that work cross-platform, including desktop, mobile and

embedded platforms.

The aim is to allow for quick and easy interaction design and rapid prototyping

whilst making your code reusable and deployable: Innovative user interfaces made

easy. ...

</details>

### pronouncing

A simple interface for the CMU pronouncing dictionary

`pip install pronouncing` · installs (wheel) · licence: MIT · rank 9573 · last release 2026-04-17 · [PyPI](https://pypi.org/project/pronouncing/)

<details><summary>README extract</summary>

Pronouncing is a simple interface for the CMU Pronouncing Dictionary. It's easy
to use and has no external dependencies. For example, here's how to find rhymes
for a given word:
Read the documentation here: ...

Example:
```python
>>> import pronouncing
>>> pronouncing.rhymes("climbing")
['diming', 'liming', 'priming', 'rhyming', 'timing']
```

</details>

### stftpitchshift

STFT based pitch and timbre shifting

`pip install stftpitchshift` · installs (wheel) · licence: MIT License · rank 14409 · last release 2023-12-12 · [PyPI](https://pypi.org/project/stftpitchshift/)

<details><summary>README extract</summary>

*stftPitchShift* is a Short-Time Fourier Transform (STFT) based pitch and timbre shifting algorithm implementation, originally inspired by the Stephan M. Bernsee's smbPitchShift.cpp.

This repository features two analogical algorithm implementations, C++ and Python. ...

Example:
```python
from stftpitchshift import StftPitchShift

pitchshifter = StftPitchShift(1024, 256, 44100)

x = [0] * 44100
y = pitchshifter.shiftpitch(x, 1)
```

Sections: stftPitchShift, Modules, Pitch shifting, Mono pitch shifting, Poly pitch shifting, Formant preservation, Build, C++, Python, Usage, Further reading, Instantaneous frequency estimation, Cepstrum analysis and formant changing, Asymmetric windows

</details>

### climage

Convert images to beautiful ANSI escape codes

`pip install climage` · installs (wheel) · licence: MIT License · rank 14737 · last release 2024-09-29 · [PyPI](https://pypi.org/project/climage/) · [docs](http://github.com/pnappa/CLImage) · [source](http://github.com/pnappa/CLImage)

<details><summary>README extract</summary>

Convert images to beautiful ANSI escape codes for display in command line interfaces.

Available as both a CLI application and a Python library.

Features:
- Custom sized images
 - ASCII or Unicode support
 - Unicode enables 4x more detail
 - 8/16/256/Truecolor support, for a wider gamut of colors
 - Selectable system palettes to adjust for user terminal themes
 - Fast color lookup with KDTrees & ...

Example:
```python
import climage

# Convert an image to a 50 character wide image.
output = climage.convert('image.png', is_unicode=True, width=50)
print(output)

# Convert an image using 8 color mode 100 columns wide, and write to file.
climage.to_file('image.png', 'out.txt', is_8color=True, width=100)
```

...

</details>

