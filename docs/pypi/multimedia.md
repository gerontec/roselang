# Multimedia

[Index](README.md) · 14 packages in this topic, 7 more listed under another topic, by downloads.

### moviepy

Video editing with Python

`pip install moviepy` · installs (wheel) · licence: MIT License · rank 1731 · last release 2025-05-21 · [PyPI](https://pypi.org/project/moviepy/)

<details><summary>README extract</summary>

> [!NOTE]
> MoviePy recently upgraded to v2.0, introducing major breaking changes. You can consult the last v1 docs here but beware that v1 is no longer maintained. For more info on how to update your code from v1 to v2, see this guide. ...

Example:
```python
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

clip = (
    VideoFileClip("long_examples/example2.mp4")
    .subclipped(10, 20)
    .with_volume_scaled(0.8)
)

...
```

Sections: MoviePy, Example, How MoviePy works, Documentation

</details>

### ffmpy

A simple Python wrapper for FFmpeg

`pip install ffmpy` · installs (wheel) · licence: MIT · rank 2467 · last release 2025-11-11 · [PyPI](https://pypi.org/project/ffmpy/)

<details><summary>README extract</summary>

*ffmpy* is a simple FFmpeg command line wrapper. It implements a Pythonic interface for FFmpeg command line compilation and uses Python's subprocess to execute the compiled command line.

*ffmpy* requires Python 3.9 or greater.

Example:
```python
from ffmpy import FFmpeg
ff = FFmpeg(
    inputs={'input.mp4': None},
    outputs={'output.avi': None}
)
ff.run()
```

Sections: ffmpy, Quick example, Documentation

</details>

### piexif

To simplify exif manipulations with python. Writing, reading, and more...

`pip install piexif` · installs (wheel) · licence: MIT License · rank 2564 · last release 2019-07-01 · [PyPI](https://pypi.org/project/piexif/)

<details><summary>README extract</summary>

To simplify exif manipulations with Python. Writing, reading, and more... Piexif is pure Python. To everywhere with Python.

Document:

Online demo:

Features:
- Pure Python. So, it runs everywhere where Python runs.
- Easy exif manipulations. Read, write, remove...
- Documented.

Example:
```python
exif_dict = piexif.load("foo1.jpg")
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGSifd["name"], exif_dictifd)
```

Sections: Piexif, Why Choose Piexif, How to Use, Example, With PIL(Pillow), Environment

</details>

### torch-audiomentations

A Pytorch library for audio data augmentation. Inspired by audiomentations. Useful for deep learning.

`pip install torch-audiomentations` · installs (wheel) · licence: MIT License · rank 3620 · last release 2025-01-15 · [PyPI](https://pypi.org/project/torch-audiomentations/)

<details><summary>README extract</summary>

Audio data augmentation in PyTorch. Inspired by audiomentations.

* Supports CPU and GPU (CUDA) - speed is a priority
* Supports batches of multichannel (or mono) audio
* Transforms extend `nn.Module`, so they can be integrated as a part of a pytorch neural network model
* Most transforms are differentiable
* Three modes: `per_batch`, ...

Example:
```python
import torch
from torch_audiomentations import Compose, Gain, PolarityInversion

# Initialize augmentation callable
apply_augmentation = Compose(
    transforms=[
        Gain(
            min_gain_in_db=-15.0,
            max_gain_in_db=5.0,
            p=0.5,
        ),
        PolarityInversion(p=0.5)
    ]
)

...
```

...

</details>

### art

ASCII Art Library For Python

`pip install art` · installs (wheel) · licence: MIT License · rank 4380 · last release 2025-04-12 · [PyPI](https://pypi.org/project/art/) · [source](https://github.com/sepandhaghighi/art)

<details><summary>README extract</summary>

Features:
ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or
letters to make a visual shape that is spread over multiple lines of text.

ART is a Python lib for text converting to ASCII art fancy. ...

Example:
```python
>>> from art import *
>>> art_1=art("coffee") # return art as str in normal mode
>>> print(art_1)
c[_]
>>> art_2=art("woman",number=2) # return multiple art as str
>>> print(art_2)
▓⚗_⚗▓ ▓⚗_⚗▓
>>> art("coffee", number=3, space=5)
'c[_]     c[_]     c[_]'
>>> art("random") # random 1-line art mode
'(っ◕‿◕)っ '
...
```

Sections: Overview, Usage, 1-Line art, 1. art, 2. aprint, 3. randart, ASCII text, 1. text2art, 2. tprint, 3. tsave, Line, 1. lprint, 2. line, Decoration

</details>

### audiomentations

A Python library for audio data augmentation. Inspired by albumentations. Useful for machine learning.

`pip install audiomentations` · installs (wheel) · licence: MIT · rank 6557 · last release 2025-09-13 · [PyPI](https://pypi.org/project/audiomentations/) · [docs](https://iver56.github.io/audiomentations/)

<details><summary>README extract</summary>

Audiomentations is a Python library for audio data augmentation, built to be fast and easy to use - its API is inspired by
albumentations. It's useful for making audio deep learning models work well in the real world, not just in the lab. ...

Example:
```python
from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, Shift
import numpy as np

augment = Compose([
    AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015, p=0.5),
    TimeStretch(min_rate=0.8, max_rate=1.25, p=0.5),
    PitchShift(min_semitones=-4, max_semitones=4, p=0.5),
    Shift(p=0.5),
])

...
```

Sections: Audiomentations, Setup, Usage example, Documentation, Transforms, [0.43.1] - 2025-09-13, Fixed

</details>

### PyExifTool

Python wrapper for exiftool

`pip install PyExifTool` · installs (wheel) · licence: BSD License; GNU General Public License v3 or later (GPLv3+) · rank 7713 · last release 2023-10-22 · [PyPI](https://pypi.org/project/PyExifTool/) · [docs](https://sylikc.github.io/pyexiftool/) · [source](https://github.com/sylikc/pyexiftool)

_README extract left out: share-alike licence._

### hachoir

Package of Hachoir parsers used to open binary files

`pip install hachoir` · installs (wheel) · licence: GNU General Public License (GPL) · rank 7885 · last release 2026-09-13 · [PyPI](https://pypi.org/project/hachoir/) · [source](https://github.com/vstinner/hachoir)

_README extract left out: share-alike licence._

### coqui-tts

Deep learning for Text to Speech.

`pip install coqui-tts` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11625 · last release 2026-10-19 · [PyPI](https://pypi.org/project/coqui-tts/) · [docs](https://coqui-tts.readthedocs.io) · [source](https://github.com/idiap/coqui-ai-TTS)

<details><summary>README extract</summary>

🐸 Coqui TTS is a library for advanced Text-to-Speech generation.

🚀 Pretrained models in +1100 languages.

🛠️ Tools for training new models and fine-tuning existing models in any language.

📚 Utilities for dataset analysis and curation.

- Fork of the original, unmaintained repository. New PyPI package: coqui-tts ...

Features:
- High-performance text-to-speech and voice conversion models, see list below.
- Fast and efficient model training with detailed training logs on the terminal and Tensorboard.
- Support for multi-speaker and multilingual TTS. ...

Example:
```python
import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Initialize TTS
...

</details>

### pulsectl

Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)

`pip install pulsectl` · installs (wheel) · licence: MIT License · rank 11754 · last release 2024-12-26 · [PyPI](https://pypi.org/project/pulsectl/)

<details><summary>README extract</summary>

Python (3.x and 2.x) blocking high-level interface and ctypes-based bindings
for PulseAudio (libpulse), to use in a simple synchronous code.

Wrappers are mostly for mixer-like controls and introspection-related operations,
as opposed to e.g. submitting sound samples to play and player-like client. ...

Example:
```python
import pulsectl

with pulsectl.Pulse('volume-increaser') as pulse:
  for sink in pulse.sink_list():
    # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
    pulse.volume_change_all_chans(sink, 0.1)
```

Sections: python-pulse-control (pulsectl module), Usage, Notes, Things not yet wrapped/exposed in python, Volume, String values, Enumerated/named values (enums), Event-handling code, threads, Tests, Links

</details>

### guessit

GuessIt - a library for guessing information from video filenames.

`pip install guessit` · installs (wheel) · licence: LGPL-3.0-or-later · rank 11956 · last release 2026-07-31 · [PyPI](https://pypi.org/project/guessit/) · [docs](https://guessit-io.github.io/guessit) · [source](https://github.com/guessit-io/guessit)

_README extract left out: share-alike licence._

### python-xmp-toolkit

XMP I/O wrapping Exempi

`pip install python-xmp-toolkit` · installs (wheel) · licence: BSD License · rank 12736 · last release 2025-11-26 · [PyPI](https://pypi.org/project/python-xmp-toolkit/)

<details><summary>README extract</summary>

Python XMP Toolkit is a library for working with XMP metadata, as well as
reading/writing XMP metadata stored in many different file formats.

Python XMP Toolkit is wrapping Exempi
(using ctypes), a C/C++ XMP library based on Adobe XMP Toolkit, ensuring that future
updates to the XMP standard are easily incorporated into the library with a ...

Sections: Python XMP Toolkit, Documentation

</details>

### python-vlc

VLC bindings for python.

`pip install python-vlc` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 12947 · last release 2024-10-07 · [PyPI](https://pypi.org/project/python-vlc/) · [docs](https://www.olivieraubert.net/vlc/python-ctypes/doc/) · [source](https://github.com/oaubert/python-vlc.git)

_README extract left out: share-alike licence._

### bithuman

Real-time talking-avatar SDK: audio in, lip-synced frames out, on your own Mac, Linux or Windows machine.

`pip install bithuman` · does not install on CPython 3.14 · licence: Commercial: see https://www.bithuman.ai/legal/terms · rank 13684 · last release 2026-11-05 · [PyPI](https://pypi.org/project/bithuman/) · [docs](https://docs.bithuman.ai)

<details><summary>README extract</summary>

Run a bitHuman avatar on your own machine, in your own process.

Two arguments — an avatar and some audio — and a video you can play (with
your API secret in `BITHUMAN_API_SECRET`; see the key). ...

Example:
```python
import bithuman, os

speech = os.path.join(os.path.dirname(bithuman.file),
                      "assets", "demo_sample.wav")   # 15 s, ships in the wheel
avatar_file = os.path.expanduser("~/.cache/bithuman/showcase/sofia-ramirez.imx")

avatar = bithuman.open(avatar_file)
frames = 0
...
```

...

</details>

## Also in this topic

- [tinytag](internet-www-http.md#tinytag) - Read audio file metadata
- [xhtml2pdf](documentation.md#xhtml2pdf) - PDF generator using HTML and CSS
- [open-webui](communications-chat.md#open-webui) - Open WebUI
- [descript-audiotools](artistic-software.md#descript-audiotools) - Utilities for handling audio.
- [descript-audio-codec](artistic-software.md#descript-audio-codec) - A high-quality general neural audio codec.
- [borb](artistic-software.md#borb) - borb is a library for reading, creating and manipulating PDF files in python.
- [Panda3D](games-entertainment.md#panda3d) - Panda3D is a framework for 3D rendering and game development for Python and C++ programs.
