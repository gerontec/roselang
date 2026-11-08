# Multimedia / Sound/Audio

[Index](README.md) · 99 packages in this topic, 26 more listed under another topic, by downloads.

### av

Pythonic bindings for FFmpeg's libraries.

`pip install av` · installs (wheel) · licence: BSD-3-Clause · rank 483 · last release 2026-10-21 · [PyPI](https://pypi.org/project/av/) · [source](https://github.com/PyAV-Org/PyAV)

<details><summary>README extract</summary>

PyAV is a Pythonic binding for the FFmpeg libraries. We aim to provide all the power and control of the underlying library, but manage the gritty details as much as possible.

[][github-tests] [][docs] [][pypi] [][conda]

PyAV is for direct and precise access to your media via containers, streams, packets, codecs, and frames. ...

</details>

### soundfile

An audio library based on libsndfile, CFFI and NumPy

`pip install soundfile` · installs (wheel) · licence: BSD License · rank 617 · last release 2026-06-06 · [PyPI](https://pypi.org/project/soundfile/)

<details><summary>README extract</summary>

The soundfile module is an audio
library based on libsndfile, CFFI and NumPy. Full documentation is
available on

The `soundfile` module can read and write sound files. File reading/writing is
supported through libsndfile,
which is a free, cross-platform, open-source (LGPL) library for reading
and writing many different sampled sound file formats ...

Example:
```python
import soundfile as sf

data, samplerate = sf.read('existing_file.wav')
sf.write('new_file.flac', data, samplerate)
```

Sections: python-soundfile, Breaking Changes, Building, Error Reporting, Read/Write Functions, Block Processing, `SoundFile` Objects

</details>

### pydub

Manipulate audio with an simple and easy high level interface

`pip install pydub` · installs (wheel) · licence: MIT License · rank 893 · last release 2021-03-10 · [PyPI](https://pypi.org/project/pydub/)

<details><summary>README extract</summary>

Manipulate audio with an simple and easy high level interface.

See the README file for details, usage info, and a list of gotchas.

</details>

### sounddevice

Play and Record Sound with Python

`pip install sounddevice` · installs (wheel) · licence: MIT · rank 1026 · last release 2026-08-17 · [PyPI](https://pypi.org/project/sounddevice/) · [docs](https://python-sounddevice.readthedocs.io/) · [source](https://github.com/spatialaudio/python-sounddevice/)

<details><summary>README extract</summary>

This Python module provides bindings for the PortAudio library and a few
convenience functions to play and record NumPy arrays containing audio signals.

The `sounddevice` module is available for Linux, macOS and Windows.

Documentation:

Source code repository and issue tracker:

License:
 MIT -- see the file `LICENSE` for details.

</details>

### soxr

High quality, one-dimensional sample-rate conversion library

`pip install soxr` · installs (wheel) · licence: LGPL-2.1-or-later · rank 1066 · last release 2026-05-03 · [PyPI](https://pypi.org/project/soxr/) · [docs](https://python-soxr.readthedocs.io) · [source](https://github.com/dofuuz/python-soxr)

_README extract left out: share-alike licence._

### librosa

Python module for audio and music processing

`pip install librosa` · installs (wheel) · licence: ISC License (ISCL) · rank 1185 · last release 2026-08-11 · [PyPI](https://pypi.org/project/librosa/) · [docs](https://librosa.org/doc) · [source](https://github.com/librosa/librosa)

<details><summary>README extract</summary>

`librosa` is a Python library for audio and music signal processing. It provides the foundational algorithms and tools required for building music information retrieval (MIR) systems.

Full documentation is available at:

If you're new to librosa, we recommend starting with the
tutorials. ...

Example:
```python
import librosa
librosa.cite()
```

Sections: librosa, Documentation, Using PyPI, Using conda, Citing, Citing for use, Citing for design

</details>

### mutagen

read and write audio tags for many formats

`pip install mutagen` · installs (wheel) · licence: GPL-2.0-or-later · rank 1319 · last release 2026-06-25 · [PyPI](https://pypi.org/project/mutagen/) · [source](https://github.com/quodlibet/mutagen)

_README extract left out: share-alike licence._

### SpeechRecognition

Library for performing speech recognition, with support for several engines and APIs, online and offline.

`pip install SpeechRecognition` · installs (wheel) · licence: BSD-3-Clause · rank 1423 · last release 2026-06-17 · [PyPI](https://pypi.org/project/SpeechRecognition/)

<details><summary>README extract</summary>

Library for performing speech recognition, with support for several engines and APIs, online and offline.

If you’re working with speech detection or transcription for meetings, consider checking out Recall.ai, an API that works with Zoom, Google Meet, Microsoft Teams, and more. ...

Example:
```python
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
```

...

</details>

### livekit-api

Python Server API for LiveKit

`pip install livekit-api` · installs (wheel) · licence: Apache-2.0 · rank 1452 · last release 2026-10-16 · [PyPI](https://pypi.org/project/livekit-api/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/python-sdks/)

<details><summary>README extract</summary>

Access LiveKit server APIs and generate access tokens.

See for more information.

Every request to the server APIs is authenticated. `LiveKitAPI` supports two modes:

- API key & secret — recommended for backend use. The SDK signs a short-lived token per request from your key and secret. ...

Example:
```python
from livekit import api

# API key & secret: set LIVEKIT_URL, LIVEKIT_API_KEY, and LIVEKIT_API_SECRET,
# then construct with no arguments...
lkapi = api.LiveKitAPI()

# ...or pass any of them explicitly to override the corresponding env var:
lkapi = api.LiveKitAPI(" api_key="api-key", api_secret="api-secret")

...
```

Sections: LiveKit Server APIs, Authentication

</details>

### audioread

Multi-library, cross-platform audio decoding.

`pip install audioread` · installs (wheel) · licence: MIT · rank 1455 · last release 2025-10-26 · [PyPI](https://pypi.org/project/audioread/) · [source](https://github.com/beetbox/audioread)

<details><summary>README extract</summary>

Decode audio files using whichever backend is available. The library
currently supports:

- Gstreamer via PyGObject.
- Core Audio on Mac OS X via ctypes. (PyObjC not required.)
- MAD via the pymad bindings.
- FFmpeg or Libav via its command-line interface.
- The standard library wave, aifc, and sunau modules (for
 uncompressed audio formats). ...

Example:
```python
with audioread.audio_open(filename) as f:
    print(f.channels, f.samplerate, f.duration)
    for buf in f:
        do_something(buf)
```

Sections: audioread, Example, Troubleshooting, Et Cetera

</details>

### livekit

Python Real-time SDK for LiveKit

`pip install livekit` · installs (wheel) · licence: Apache-2.0 · rank 1571 · last release 2026-11-06 · [PyPI](https://pypi.org/project/livekit/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/python-sdks/)

<details><summary>README extract</summary>

Python SDK to integrate LiveKit's real-time video, audio, and data capabilities into your Python applications using WebRTC. Designed for use with LiveKit Agents to build powerful voice AI apps.

See for more information.

Use `EncodedVideoSource` when an upstream encoder already provides compressed
frames. ...

Example:
```python
from livekit import rtc

source = rtc.EncodedVideoSource(width=640, height=360)
track = rtc.LocalVideoTrack.create_video_track("camera", source)
await room.local_participant.publish_track(
    track,
    rtc.TrackPublishOptions(
        video_codec=rtc.VideoCodec.VP9,
        video_encoder=rtc.VideoEncoderBackend.ENCODER_BACKEND_PRE_ENCODED,
...
```

Sections: LiveKit SDK for Python, Publishing pre-encoded video

</details>

### torchaudio

An audio package for PyTorch

`pip install torchaudio` · installs (wheel) · licence: BSD License · rank 1761 · last release 2026-10-28 · [PyPI](https://pypi.org/project/torchaudio/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> **TorchAudio 2.11 works with `torch` 2.11 and with every future `torch`
> release (2.12, 2.13, etc.).** It is the latest release, and it is the only
> one you need: there is nothing to upgrade in TorchAudio when you upgrade
> `torch`, and installing TorchAudio does not pin `torch` to a specific
> version. ...

</details>

### livekit-agents

A powerful framework for building realtime voice AI agents

`pip install livekit-agents` · installs (wheel) · licence: Apache-2.0 · rank 1945 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-agents/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Realtime framework for production-grade multimodal and voice AI agents.

See for quickstarts, documentation, and examples.

Example:
```python
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import openai

load_dotenv()

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="coral"
...
```

</details>

### livekit-blingfire

BlingFire bindings for livekit-agents

`pip install livekit-blingfire` · installs (wheel) · licence: Apache Software License · rank 1961 · last release 2026-10-13 · [PyPI](https://pypi.org/project/livekit-blingfire/) · [docs](https://docs.livekit.io)

### livekit-local-inference

LiveKit on-device inference (end-of-turn detector + streaming VAD)

`pip install livekit-local-inference` · installs (wheel) · licence: Apache Software License; Other/Proprietary License · rank 2173 · last release 2026-08-18 · [PyPI](https://pypi.org/project/livekit-local-inference/)

### livekit-plugins-silero

Agent Framework Plugin for Silero

`pip install livekit-plugins-silero` · installs (wheel) · licence: Apache-2.0 · rank 2274 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-silero/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for VAD-based turn detection.

See for more information.

</details>

### resampy

Efficient signal resampling

`pip install resampy` · installs (wheel) · licence: ISC License (ISCL) · rank 2295 · last release 2024-03-05 · [PyPI](https://pypi.org/project/resampy/)

<details><summary>README extract</summary>

Efficient sample rate conversion in Python.

This package implements the band-limited sinc interpolation method for sampling rate conversion as described by:
> Smith, Julius O. Digital Audio Resampling Home Page
> Center for Computer Research in Music and Acoustics (CCRMA),
> Stanford University, 2015-02-23.
> Web published at

</details>

### pyloudnorm

Implementation of ITU-R BS.1770-4 loudness algorithm in Python.

`pip install pyloudnorm` · installs (wheel) · licence: MIT · rank 2410 · last release 2026-01-04 · [PyPI](https://pypi.org/project/pyloudnorm/) · [source](https://github.com/csteinmetz1/pyloudnorm)

<details><summary>README extract</summary>

Flexible audio loudness meter in Python.

Implementation of ITU-R BS.1770-4.

Allows control over gating block size and frequency weighting filters for additional control.

For full details on the implementation see our paper with a summary in our AES presentation video.

Example:
```python
import soundfile as sf
import pyloudnorm as pyln

data, rate = sf.read("test.wav") # load audio (with shape (samples, channels))
meter = pyln.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data) # measure loudness
```

Sections: pyloudnorm, Usage, Find the loudness of an audio file, Loudness normalize and peak normalize audio files, Loudness range, Advanced operation, Dependencies, References, Tensorized/Differentiable Implementations

</details>

### julius

Nice DSP sweets: resampling, FFT Convolutions. All with PyTorch, differentiable and with CUDA support.

`pip install julius` · installs (wheel) · licence: MIT License · rank 2446 · last release 2026-06-03 · [PyPI](https://pypi.org/project/julius/)

<details><summary>README extract</summary>

Julius contains different Digital Signal Processing algorithms implemented
with PyTorch, so that they are differentiable and available on CUDA.
Note that all the modules implemented here can be used with TorchScript.

For now, I have implemented:

- julius.resample: fast sinc resampling.
- julius.fftconv: FFT based convolutions. ...

Example:
```python
import julius
import torch

signal = torch.randn(6, 4, 1024)
# Resample from a sample rate of 100 to 70. The old and new sample rate must be integers,
# and resampling will be fast if they form an irreductible fraction with small numerator
# and denominator (here 10 and 7). Any shape is supported, last dim is time.
...
```

...

</details>

### livekit-plugins-openai

Agent Framework plugin for services from OpenAI

`pip install livekit-plugins-openai` · installs (wheel) · licence: Apache-2.0 · rank 2578 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-openai/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for OpenAI Realtime API, Responses API, Decisions API, LLM, TTS, and STT APIs.

Also includes support for a large number of OpenAI-compatible APIs including Azure OpenAI, Cerebras, Fireworks, Perplexity, Telnyx, xAI, Ollama, DeepSeek, and SambaNova.

See for more information.

Sections: OpenAI plugin for LiveKit Agents, Pre-requisites

</details>

### piper-tts

Fast and local neural text-to-speech engine

`pip install piper-tts` · installs (wheel) · licence: GPL-3.0-or-later · rank 2832 · last release 2026-09-04 · [PyPI](https://pypi.org/project/piper-tts/)

_README extract left out: share-alike licence._

### livekit-plugins-elevenlabs

Agent Framework plugin for voice synthesis with ElevenLabs' API.

`pip install livekit-plugins-elevenlabs` · installs (wheel) · licence: Apache-2.0 · rank 2862 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-elevenlabs/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for voice synthesis with ElevenLabs.

See for more information.

Example:
```python
from livekit.plugins import elevenlabs

stt = elevenlabs.STT(
    model="scribe_v2_realtime",
    audio_chunk_duration_ms=100,
)
```

Sections: ElevenLabs plugin for LiveKit Agents, Pre-requisites, Realtime speech-to-text audio chunks

</details>

### livekit-plugins-deepgram

Agent Framework plugin for services using Deepgram's API.

`pip install livekit-plugins-deepgram` · installs (wheel) · licence: Apache-2.0 · rank 2960 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-deepgram/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Deepgram's voice AI services in LiveKit Agents.

More information is available in the docs for the STT and TTS integrations.

Sections: Deepgram plugin for LiveKit Agents, Pre-requisites

</details>

### livekit-plugins-cartesia

LiveKit Agents Plugin for Cartesia

`pip install livekit-plugins-cartesia` · installs (wheel) · licence: Apache-2.0 · rank 3033 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-cartesia/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Cartesia's voice AI services in LiveKit Agents.

More information is available in the docs for the STT and TTS integrations.

Sections: Cartesia plugin for LiveKit Agents, Pre-requisites

</details>

### lameenc

LAME encoding bindings

`pip install lameenc` · installs (wheel) · licence: LGPL-3.0-or-later · rank 3168 · last release 2026-10-15 · [PyPI](https://pypi.org/project/lameenc/) · [source](https://github.com/chrisstaite/lameenc)

_README extract left out: share-alike licence._

### mido

MIDI Objects for Python

`pip install mido` · installs (wheel) · licence: MIT License · rank 3460 · last release 2024-10-25 · [PyPI](https://pypi.org/project/mido/) · [docs](https://mido.readthedocs.io) · [source](https://github.com/mido/mido)

<details><summary>README extract</summary>

Mido is a library for working with MIDI messages and ports:

Full documentation at

Example:
```python
>>> import mido
>>> msg = mido.Message('note_on', note=60)
>>> msg.type
'note_on'
>>> msg.note
60
>>> msg.bytes()
[144, 60, 64]
>>> msg.copy(channel=2)
Message('note_on', channel=2, note=60, velocity=64, time=0)
```

Sections: Mido - MIDI Objects for Python, Main Features, Requirements, Source Code, Questions and suggestions

</details>

### gTTS

gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate text-to-speech API

`pip install gTTS` · installs (wheel) · licence: MIT License · rank 3647 · last release 2024-11-10 · [PyPI](https://pypi.org/project/gTTS/) · [docs](https://gtts.readthedocs.io) · [source](https://github.com/pndurette/gTTS)

<details><summary>README extract</summary>

gTTS (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
Write spoken `mp3` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout`.

Features:
- Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more; ...

Sections: gTTS, Features, Quickstart, Disclaimer, Project

</details>

### livekit-plugins-turn-detector

End of utterance detection for LiveKit Agents

`pip install livekit-plugins-turn-detector` · installs (wheel) · licence: Apache-2.0 · rank 3727 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-turn-detector/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

> ⚠️ Deprecated. This plugin is deprecated and will be removed in a future release. Use `livekit.agents.inference.TurnDetector` instead — it ships with `livekit-agents`, requires no additional install, and replaces both the English and Multilingual text-based models with a unified audio end-of-turn detector. ...

Example:
```python
from livekit.agents.inference import TurnDetector

session = AgentSession(
    ...
    turn_detection=TurnDetector(),
)
```

Sections: Turn detector plugin for LiveKit Agents, Usage, Usage with RealtimeModel, Running your agent, Downloaded model files, Model system requirements

</details>

### livekit-plugins-google

Agent Framework plugin for services from Google Cloud

`pip install livekit-plugins-google` · installs (wheel) · licence: Apache-2.0 · rank 3798 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-google/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Gemini, Gemini Live, Cloud Speech-to-Text, and Cloud Text-to-Speech.

See for more information.

Sections: Google AI plugin for LiveKit Agents, Pre-requisites

</details>

### pymp4

Python parser for MP4 boxes

`pip install pymp4` · installs (wheel) · licence: Apache Software License · rank 3810 · last release 2023-05-07 · [PyPI](https://pypi.org/project/pymp4/) · [source](https://github.com/beardypig/pymp4)

<details><summary>README extract</summary>

Python MP4 box parser and toolkit based on the construct library.

Example:
```python
>>> from pymp4.parser import Box
>>> from io import BytesIO

>>> Box.build(dict(
    type=b"ftyp",
    major_brand="iso5",
    minor_version=1,
    compatible_brands=["iso5", "avc1"]))
b'\x00\x00\x00\x18ftypiso5\x00\x00\x00\x01iso5avc1'

>>> ftyp = Box.parse(b'\x00\x00\x00\x18ftypiso5\x00\x00\x00\x01iso5avc1')
>>> print(ftyp)
Container:
...
```

Sections: pymp4, Usage

</details>

### PyAudio

Cross-platform audio I/O with PortAudio

`pip install PyAudio` · installs from source (sdist only) · licence: MIT License · rank 3830 · last release 2024-11-20 · [PyPI](https://pypi.org/project/PyAudio/)

<details><summary>README extract</summary>

PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms, such as GNU/Linux, Microsoft Windows, and Apple macOS.

PyAudio is distributed under the MIT License.

* Homepage
* API Documentation
* PyPi

Sections: PyAudio, Windows, macOS, GNU/Linux, Building from source, Documentation & Usage Examples

</details>

### livekit-plugins-assemblyai

Agent Framework plugin for AssemblyAI

`pip install livekit-plugins-assemblyai` · installs (wheel) · licence: Apache-2.0 · rank 3951 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-assemblyai/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Streaming Speech-to-Text and Streaming Text-to-Speech from AssemblyAI.

More information is available in the docs for the STT integration and for AssemblyAI's Streaming TTS.

Example:
```python
from livekit.agents import AgentSession, TurnHandlingOptions
from livekit.plugins import assemblyai

session = AgentSession(
    stt=assemblyai.STT(model="universal-3-6-pro", mode="balanced"),
    tts=assemblyai.TTS(
        model="assemblyai-tts-1",
        voice="49c443a4-8a1d-5f7e-b70b-98bdbd9823c3",  # Audrey
    ),
...
```

Sections: AssemblyAI plugin for LiveKit Agents, Pre-requisites, Usage, Speech-to-text, Text-to-speech

</details>

### miniaudio

python bindings for the miniaudio library and its decoders (mp3, flac, ogg vorbis, wav)

`pip install miniaudio` · installs (wheel) · licence: MIT · rank 3997 · last release 2026-11-07 · [PyPI](https://pypi.org/project/miniaudio/)

<details><summary>README extract</summary>

Multiplatform audio playback, recording, decoding and sample format conversion for
Linux (including Raspberry Pi), Windows, Mac and others.

Installation for most users: via Pypi, Raspberry Pi builds via PiWheels.

This is a Pythonic interface to the cross-platform miniaudio C library:

- audio operations run in the background ...

Example:
```python
import miniaudio

# Get file info
info = miniaudio.get_file_info("samples/music.mp3")
print(f"Playing: {info.nchannels} channels, {info.sample_rate} Hz, {info.duration:.1f}s")

# Stream and play
stream = miniaudio.stream_file("samples/music.mp3")
with miniaudio.PlaybackDevice() as device:
    device.start(stream)
...
```

...

</details>

### pedalboard

A Python library for adding effects to audio.

`pip install pedalboard` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 4026 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pedalboard/)

_README extract left out: share-alike licence._

### pretty-midi

Functions and classes for handling MIDI data conveniently.

`pip install pretty-midi` · installs (wheel) · licence: MIT License · rank 4259 · last release 2026-07-28 · [PyPI](https://pypi.org/project/pretty-midi/)

<details><summary>README extract</summary>

`pretty_midi` contains utility function/classes for handling MIDI data, so that it's in a format which is easy to modify and extract information from.

Documentation is available here. You can also find a Jupyter notebook tutorial here (click here to load in Colab).

`pretty_midi` is available via pip or via the setup.py script. ...

Example:
```python
import pretty_midi
# Load MIDI file into PrettyMIDI object
midi_data = pretty_midi.PrettyMIDI('example.mid')
# Print an empirical estimate of its global tempo
print(midi_data.estimate_tempo())
# Compute the relative amount of each semitone across the entire song, a proxy for key
total_velocity = sum(sum(midi_data.get_chroma()))
...
```

</details>

### demucs

Music source separation in the waveform domain.

`pip install demucs` · installs (wheel) · licence: MIT License · rank 4301 · last release 2026-07-11 · [PyPI](https://pypi.org/project/demucs/)

<details><summary>README extract</summary>

This is the officially maintained Demucs now that I (Alexandre Défossez) have left Meta to join Kyutai.
Note that I'm not actively working on Demucs anymore, so expect slow replies and no new feature for now.

This is the 4th release of Demucs (v4), featuring Hybrid Transformer based source separation. ...

Example:
```python
# Assume that your command is `demucs --mp3 --two-stems vocals -n mdx_extra "track with space.mp3"`
# The following codes are same as the command above:
import demucs.separate
demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", "track with space.mp3"])

# Or like this
import demucs.separate
import shlex
...
```

...

</details>

### pocketsphinx

Official Python bindings for PocketSphinx

`pip install pocketsphinx` · installs from source (sdist only) · licence: BSD License · rank 4652 · last release 2026-06-06 · [PyPI](https://pypi.org/project/pocketsphinx/) · [docs](https://pocketsphinx.readthedocs.io/en/latest/) · [source](https://github.com/cmusphinx/pocketsphinx.git)

<details><summary>README extract</summary>

This is PocketSphinx, one of Carnegie Mellon University's open source large
vocabulary, speaker-independent continuous speech recognition engines.

Although this was at one point a research system, active development
has largely ceased and it has become very, very far from the state of
the art. ...

Example:
```python
from pocketsphinx import LiveSpeech
for phrase in LiveSpeech(): print(phrase)
```

Sections: PocketSphinx 5.1.1, LiveSpeech, AudioFile

</details>

### livekit-plugins-anthropic

Agent Framework plugin for services from Anthropic

`pip install livekit-plugins-anthropic` · installs (wheel) · licence: Apache-2.0 · rank 4931 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-anthropic/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for the Claude family of LLMs from Anthropic.

See for more information.

Sections: Anthropic plugin for LiveKit Agents, Pre-requisites

</details>

### livekit-plugins-krisp

Krisp VIVA noise reduction plugin for LiveKit Agents

`pip install livekit-plugins-krisp` · installs (wheel) · licence: Apache-2.0 · rank 5061 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-krisp/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Real-time noise reduction for LiveKit voice agents using Krisp's VIVA SDK.

Features:
- `voice_isolation()`: Real-time voice isolation and noise reduction `FrameProcessor`
- `voice_isolation_telephony()`: Voice isolation tuned for telephony audio (for example, SIP participants)

Example:
```python
from livekit.agents import AgentSession, Agent, JobContext, inference, room_io
from livekit.plugins import krisp, openai

@server.rtc_session()
async def entrypoint(ctx: JobContext):
    # Default: LiveKit Cloud auth + bundled model. No keys or model files.
    noise_cancellation = krisp.voice_isolation(
...
```

...

</details>

### mir-eval

Common metrics for common audio/music processing tasks.

`pip install mir-eval` · installs (wheel) · licence: MIT License · rank 5582 · last release 2025-02-25 · [PyPI](https://pypi.org/project/mir-eval/)

<details><summary>README extract</summary>

Python library for computing common heuristic accuracy scores for various music/audio information retrieval/signal processing tasks.

Documentation, including installation and usage information:

Dependencies:

* Scipy/Numpy
* decorator

If you use mir_eval in a research project, please cite the following paper:

Colin Raffel, Brian McFee, Eric J. ...

</details>

### kaldiio

Kaldi-ark loading and writing module

`pip install kaldiio` · installs (wheel) · licence: not stated · rank 5881 · last release 2025-03-06 · [PyPI](https://pypi.org/project/kaldiio/)

<details><summary>README extract</summary>

A pure python module for reading and writing kaldi ark files

- Introduction
 - What is this? What are `ark` and `scp`?
 - Features
 - Similar projects
- Install
- Usage
 - ReadHelper
 - WriteHelper
- More low level API ...

Features:
Kaldiio supports:

- Read/Write for archive formats: ark, scp
 - Binary/Text - Float/Double Matrix: DM, FM
 - Binary/Text - Float/Double Vector: DV, FV
 - Compressed Matrix for loading: CM, CM2, CM3
 - Compressed Matrix for writing: All ...

Example:
```python
from kaldiio import ReadHelper
with ReadHelper('scp:file.scp') as reader:
    for key, numpy_array in reader:
        ...
```

...

</details>

### encodec

High fidelity neural audio codec

`pip install encodec` · installs from source (sdist only) · licence: Creative Commons Attribution-NonCommercial 4.0 International · rank 5983 · last release 2022-10-25 · [PyPI](https://pypi.org/project/encodec/)

<details><summary>README extract</summary>

This is the code for the EnCodec neural codec presented in the High Fidelity Neural Audio Compression [[abs]](
paper. We provide our two multi-bandwidth models:
* A causal model operating at 24 kHz on monophonic audio trained on a variety of audio data.
* A non-causal model operationg at 48 kHz on stereophonic audio trained on music-only data. ...

Example:
```python
from encodec import EncodecModel
from encodec.utils import convert_audio

import torchaudio
import torch

# Instantiate a pretrained EnCodec model
model = EncodecModel.encodec_model_24khz()
model.set_target_bandwidth(6.0)

# Load and pre-process the audio waveform
wav, sr = torchaudio.load("")
wav = wav.unsqueeze(0)
...
```

...

</details>

### aic-sdk

Python bindings for ai-coustics SDK

`pip install aic-sdk` · installs (wheel) · licence: Apache Software License · rank 5985 · last release 2026-11-05 · [PyPI](https://pypi.org/project/aic-sdk/)

<details><summary>README extract</summary>

Python wrapper for the ai-coustics audio enhancement, voice activity detection, and analysis SDK.

For comprehensive documentation, visit docs.ai-coustics.com.

> [!NOTE]
> This SDK requires a license key. Generate your key at developers.ai-coustics.com.

Example:
```python
import aic_sdk as aic
import numpy as np
import os

# Get your license key from the environment variable
license_key = os.environ["AIC_SDK_LICENSE"]

# Download and load a model (or download manually at
model_path = aic.Model.download("quail-vf-2.3-l-16khz", "./models")
model = aic.Model.from_file(model_path)

# Get optimal configuration
...
```

...

</details>

### livekit-plugins-soniox

Agent Framework plugin for services using Soniox's API.

`pip install livekit-plugins-soniox` · installs (wheel) · licence: Apache-2.0 · rank 6418 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-soniox/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Soniox Speech-to-Text and Text-to-Speech APIs, using WebSocket streaming interfaces.

See STT documentation and TTS documentation for more information.

Example:
```python
from livekit.plugins import soniox

session = AgentSession(
    stt=soniox.STT(),
    # ... llm, tts, etc.
)
```

Sections: Soniox plugin for LiveKit Agents, Pre-requisites, Usage, Speech-to-Text (STT), Text-to-Speech (TTS), More information and reference

</details>

### pvporcupine

Porcupine wake word engine.

`pip install pvporcupine` · installs (wheel) · licence: Apache Software License · rank 6482 · last release 2026-06-25 · [PyPI](https://pypi.org/project/pvporcupine/)

<details><summary>README extract</summary>

Made in Vancouver, Canada by Picovoice

Porcupine is a highly-accurate and lightweight wake word engine. It enables building always-listening voice-enabled
applications. It is

- using deep neural networks trained in real-world environments.
- compact and computationally-efficient. It is perfect for IoT. ...

Example:
```python
import pvporcupine

access_key = "${ACCESS_KEY}" # AccessKey obtained from Picovoice Console (

handle = pvporcupine.create(access_key=access_key, keywords=['picovoice'])
```

Sections: Porcupine Wake Word Engine, Compatibility, AccessKey, Usage, Non-English Wake Words, Non-English Contexts, Train Models over API, Demos

</details>

### funasr

OpenAI-compatible speech recognition toolkit with WebSocket streaming, vLLM acceleration, and llama.cpp/GGUF edge runtime.

`pip install funasr` · installs (wheel) · licence: MIT License · rank 6538 · last release 2026-11-08 · [PyPI](https://pypi.org/project/funasr/) · [docs](https://modelscope.github.io/FunASR/)

<details><summary>README extract</summary>

(简体中文|English|日本語|한국어)

 Industrial speech recognition toolkit for offline, streaming, and edge deployment.

 ASR · VAD · punctuation · speaker pipelines · emotion and audio-event models · OpenAI-compatible serving

 Quick Start · Model selection · Models · Deployment matrix · Deployment hub · Docs · Benchmark · Contribute

Features:
FunASR is a toolkit: choose the task, checkpoint, and runtime separately.
Support in one model or adapter does not imply support in every serving backend.

| Task | Checkpoint or pipeline | Runtime entrypoint | Important limitation | ...

Example:
```python
from funasr import AutoModel

# Chinese production (VAD + ASR + punctuation + speaker)
...

</details>

### lhotse

Data preparation for speech processing models training.

`pip install lhotse` · installs (wheel) · licence: Apache Software License · rank 6617 · last release 2026-04-20 · [PyPI](https://pypi.org/project/lhotse/)

<details><summary>README extract</summary>

Lhotse is a Python library aiming to make multimodal (speech, audio, video, image, text) data preparation flexible and accessible to a wider community.
Alongside k2, it is a part of the next generation Kaldi speech processing library.

Example:
```python
from torch.utils.data import DataLoader
from lhotse import CutSet, Fbank
from lhotse.dataset import VadDataset, SimpleCutSampler
from lhotse.recipes import prepare_switchboard

# Prepare data manifests from a raw corpus distribution.
# The RecordingSet describes the metadata about audio recordings;
...
```

Sections: Lhotse, Tutorial presentations and materials, About, Main goals (updated for 2025), Tutorials, Examples of use, Main ideas, Pip, Environment variables, Optional dependencies, Examples

</details>

### livekit-plugins-xai

Agent Framework plugin for xAI

`pip install livekit-plugins-xai` · installs (wheel) · licence: Apache-2.0 · rank 6646 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-xai/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for xAI's Grok LLM, STT, TTS, and Grok Voice Agent API.

See the xAI integration docs for more information.

Sections: xAI plugin for LiveKit Agents, Pre-requisites

</details>

### numpy-rms

A fast python library for calculating the RMS of a NumPy array

`pip install numpy-rms` · installs (wheel) · licence: MIT License · rank 6703 · last release 2026-06-26 · [PyPI](https://pypi.org/project/numpy-rms/)

<details><summary>README extract</summary>

* Written in C and takes advantage of AVX (on x86-64) or NEON (on ARM) for speed
* The fast implementation is tailored for C-contiguous 1-dimensional and 2-dimensional float32 arrays

Example:
```python
import numpy_rms
import numpy as np

arr = np.arange(40, dtype=np.float32)
rms_series = numpy_rms.rms(arr, window_size=10)
print(rms_series.shape)  # (4,)
```

Sections: Usage, [0.7.0] - 2025-12-27, Added, Removed

</details>

### numpy-minmax

A fast python library for finding both min and max value in a NumPy array

`pip install numpy-minmax` · installs (wheel) · licence: MIT License · rank 6704 · last release 2026-06-26 · [PyPI](https://pypi.org/project/numpy-minmax/)

<details><summary>README extract</summary>

NumPy lacked an optimized minmax function, so we wrote our own. At Nomono, we use it for audio processing, but it can be applied any kind of float32 ndarray.

* Written in C and takes advantage of AVX/AVX512 for speed
* Roughly 2.3x speedup compared to the numpy amin+amax equivalent (tested on Intel CPU with numpy 1.24-1.26)
* The fast ...

Example:
```python
import numpy_minmax
import numpy as np

arr = np.arange(1337, dtype=np.float32)
min_val, max_val = numpy_minmax.minmax(arr)  # 0.0, 1336.0
```

Sections: Usage, [0.6.0] - 2025-12-27, Added, Removed, Running benchmarks

</details>

### python-stretch

Simple python library for pitch shifting and time stretching

`pip install python-stretch` · installs (wheel) · licence: MIT License · rank 6715 · last release 2025-02-14 · [PyPI](https://pypi.org/project/python-stretch/)

<details><summary>README extract</summary>

[][actions-pip-link]
[][actions-wheels-link]
<!-- -->
<!-- -->

A simple Python Wrapper of the Signalsmith Stretch C++ library for pitch and time stretching.

Features:
- Time stretching
- Pitch shifting
- Multichannel support: Works with mono and multichannel audio files.
- Seamless integration: Works natively with NumPy arrays for compatibility with libraries such as `librosa` and many others used in audio ...

Example:
```python
import numpy as np
import librosa
import python_stretch as ps

# Load an audio example from librosa (e.g., 'trumpet', 'brahms',...)
audio, sr = librosa.load(librosa.ex('trumpet'), sr=None)

# Assure that "audio" is a 2d array
if (audio.ndim == 1):
    audio = audio[np.newaxis, :]

# Create a Stretch object
stretch = ps.Signalsmith.Stretch()
...
```

...

</details>

### opuslib

Python bindings to the libopus, IETF low-delay audio codec

`pip install opuslib` · installs from source (sdist only) · licence: BSD License · rank 6761 · last release 2018-01-16 · [PyPI](https://pypi.org/project/opuslib/)

### samplerate

Monolithic python wrapper for libsamplerate based on pybind11 and NumPy

`pip install samplerate` · installs (wheel) · licence: MIT · rank 6997 · last release 2026-03-22 · [PyPI](https://pypi.org/project/samplerate/)

<details><summary>README extract</summary>

This is a wrapper around Erik de Castro Lopo's libsamplerate (aka Secret
Rabbit Code) for high-quality sample rate conversion.

It implements all three APIs available in
libsamplerate: ...

Example:
```python
import numpy as np
import samplerate

# Synthesize data
fs = 1000.
t = np.arange(fs * 2) / fs
input_data = np.sin(2 * np.pi * 5 * t)

# Simple API
ratio = 1.5
converter = 'sinc_best'  # or 'sinc_fastest', ...
output_data_simple = samplerate.resample(input_data, ratio, converter)

# Full API
resampler = samplerate.Resampler(converter, channels=1)
...
```

Sections: python-samplerate, Usage, See also

</details>

### onnx-asr

A lightweight Python package for Automatic Speech Recognition using ONNX models

`pip install onnx-asr` · installs (wheel) · licence: MIT · rank 7052 · last release 2026-07-15 · [PyPI](https://pypi.org/project/onnx-asr/) · [docs](https://istupakov.github.io/onnx-asr/) · [source](https://github.com/istupakov/onnx-asr)

<details><summary>README extract</summary>

onnx-asr is a Python package for Automatic Speech Recognition using ONNX models. It's a lightweight, fast, and easy-to-use pure Python package with minimal dependencies (no need for PyTorch, Transformers, or FFmpeg):

Key features of onnx-asr include: ...

Example:
```python
import onnx_asr

# Load the Parakeet TDT v3 model from Hugging Face (may take a few minutes)
model = onnx_asr.load_model("nemo-parakeet-tdt-0.6b-v3")

# Recognize speech and print the result
result = model.recognize("test.wav")
print(result)
```

Sections: ONNX ASR, Quick Start, Benchmarks, Troubleshooting and FAQ

</details>

### livekit-plugins-azure

Agent Framework plugin for services from Azure

`pip install livekit-plugins-azure` · installs (wheel) · licence: Apache-2.0 · rank 7064 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-azure/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Complete Azure AI integration for LiveKit Agents, including Azure Speech Services and Azure Voice Live Realtime API.

What's included:
- RealtimeModel - Azure Voice Live for speech-to-speech
- STT - Powered by Azure Speech Services
- TTS - Powered by Azure Speech Services with neural voices ...

Example:
```python
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession
from livekit.plugins import azure

class Assistant(Agent):
    def init(self):
        super().init(
            instructions="You are a helpful voice assistant powered by Azure."
        )

    async def on_enter(self):
...
```

...

</details>

### resemble-perth

Audio Watermarking and Detection Library

`pip install resemble-perth` · installs (wheel) · licence: MIT License · rank 7228 · last release 2025-05-23 · [PyPI](https://pypi.org/project/resemble-perth/) · [docs](https://github.com/resemble-ai/Perth/blob/main/README.md) · [source](https://github.com/resemble-ai/Perth)

<details><summary>README extract</summary>

Perth is a comprehensive Python library for audio watermarking and detection.

Features:
Perth enables you to embed imperceptible watermarks in audio files and later detect them, even after the audio has undergone various transformations or manipulations. ...

Example:
```python
import perth
import librosa
import soundfile as sf

# Load audio file
wav, sr = librosa.load("input.wav", sr=None)

# Initialize watermarker
watermarker = perth.PerthImplicitWatermarker()

# Apply watermark
watermarked_audio = watermarker.apply_watermark(wav, watermark=None, sample_rate=sr)

# Save watermarked audio
...
```

...

</details>

### speechmatics-rt

Speechmatics Real-Time API Client

`pip install speechmatics-rt` · installs (wheel) · licence: MIT · rank 7639 · last release 2026-11-06 · [PyPI](https://pypi.org/project/speechmatics-rt/) · [docs](https://docs.speechmatics.com/) · [source](https://github.com/speechmatics/speechmatics-python-sdk)

<details><summary>README extract</summary>

Async Python client for the Speechmatics Real-Time API.

Features:
- Async-first design with simpler interface
- Multi-channel transcription - Simultaneous processing of multiple audio sources
- Single-stream transcription - Optimized client for single audio source ...

Example:
```python
import asyncio
from speechmatics.rt import AsyncClient, ServerMessageType

async def main():
    # Create a client using environment variable SPEECHMATICS_API_KEY
    async with AsyncClient() as client:
        # Register event handlers
        @client.on(ServerMessageType.ADD_TRANSCRIPT)
        def handle_final_transcript(msg):
...
```

Sections: Speechmatics Real-Time API Client, Features, Quick Start, Multi-Channel Transcription, JWT Authentication, Logging, Environment Variables

</details>

### audio-separator

Easy to use audio stem separation, using various models from UVR trained primarily by @Anjok07

`pip install audio-separator` · installs (wheel) · licence: MIT License · rank 7657 · last release 2026-10-29 · [PyPI](https://pypi.org/project/audio-separator/) · [docs](https://github.com/karaokenerds/python-audio-separator/blob/main/README.md) · [source](https://github.com/karaokenerds/python-audio-separator)

<details><summary>README extract</summary>

Summary: Easy to use audio stem separation from the command line or as a dependency in your own Python project, using the amazing MDX-Net, VR Arch, Demucs and MDXC models available in UVR by @Anjok07 & @aufr33. ...

Features:
- Separate audio into multiple stems, e.g. instrumental and vocals.
- Supports all common audio formats (WAV, MP3, FLAC, M4A, etc.)
- Ability to inference using a pre-trained model in PTH or ONNX format. ...

Example:
```python
from audio_separator.separator import Separator

# Initialize the Separator class with custom parameters
separator = Separator(
    output_dir='output',
    ensemble_algorithm='avg_wave'
)

# List of models to ensemble
# Note: These models will be downloaded automatically if not present
models = [
    'UVR-MDX-NET-Inst_HQ_3.onnx',
...
```

...

</details>

### pyroomacoustics

A simple framework for room acoustics and audio processing in Python.

`pip install pyroomacoustics` · installs (wheel) · licence: not stated · rank 7934 · last release 2026-05-01 · [PyPI](https://pypi.org/project/pyroomacoustics/) · [docs](https://pyroomacoustics.readthedocs.io/en/pypi-release/) · [source](https://github.com/LCAV/pyroomacoustics.git)

<details><summary>README extract</summary>

Pyroomacoustics is a software package aimed at the rapid development
and testing of audio array processing algorithms. The content of the package
can be divided into three main components:

1. ...

Example:
```python
import numpy as np
import matplotlib.pyplot as plt
import pyroomacoustics as pra

# Create a 4 by 6 metres shoe box room
room = pra.ShoeBox([4,6])

# Add a source somewhere in the room
room.add_source([2.5, 4.5])

# Create a linear array beamformer with 4 microphones
# with angle 0 degrees and inter mic distance 10 cm
...
```

Sections: Summary, Room Acoustics Simulation, Reference Implementations, Datasets, Dependencies, Example, More examples, Academic publications

</details>

### livekit-plugins-aws

LiveKit Agents Plugin for services from AWS

`pip install livekit-plugins-aws` · installs (wheel) · licence: Apache-2.0 · rank 7995 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-aws/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Complete AWS AI integration for LiveKit Agents, including Bedrock, Polly, Transcribe, and realtime speech-to-speech support for Amazon Nova Sonic

What's included:
- RealtimeModel - Amazon Nova 2.5 Sonic, Nova 2 Sonic, and Nova Sonic 1.0 for speech-to-speech
- LLM - Powered by Amazon Bedrock, defaults to Nova 2 Lite ...

Example:
```python
from livekit import agents
from livekit.agents import Agent, AgentSession
from livekit.plugins import aws
from dotenv import load_dotenv

load_dotenv()

class Assistant(Agent):
    def init(self):
        super().init(
            instructions="You are a helpful voice assistant powered by Amazon Nova 2 Sonic."
        )

...
```

...

</details>

### SoundCard

Play and record audio without resorting to CPython extensions

`pip install SoundCard` · installs (wheel) · licence: BSD License · rank 8034 · last release 2026-04-12 · [PyPI](https://pypi.org/project/SoundCard/)

<details><summary>README extract</summary>

SoundCard is a library for playing and recording audio without resorting to a
CPython extension. Instead, it is implemented using the wonderful CFFI and the native audio libraries of
Linux, Windows and macOS.

The input and output data are scaled to 0dBFS (Full Scale). To avoid clipping
restrict all data between -1 and 1. ...

Example:
```python
import soundcard as sc

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()

...
```

Sections: SoundCard, Tutorial, Latency, Channel Maps, FAQ, Known Issues

</details>

### audiolab

Streaming audio I/O and high-level processing for NumPy

`pip install audiolab` · installs (wheel) · licence: Apache-2.0 · rank 8110 · last release 2026-08-27 · [PyPI](https://pypi.org/project/audiolab/) · [docs](https://github.com/pengzhendong/audiolab#readme)

<details><summary>README extract</summary>

`audiolab` is a compact Python toolkit for loading, transforming, streaming, inspecting, and saving audio. It accepts local files, URLs, encoded bytes, and file-like objects, and returns NumPy arrays with a consistent channels-first layout. ...

Features:
- Decode WAV, FLAC, MP3, AAC, M4A, WebM, and other formats supported by the installed audio libraries.
- Read from paths, URLs, `bytes`, and binary file-like objects. ...

Example:
```python
import numpy as np

from audiolab import load_audio

audio, sample_rate = load_audio(
    "speech.mp3",
    offset=7.0,
    duration=23.0,
    sample_rate=16_000,
    to_mono=True,
    dtype=np.float32,
)

print(audio.shape)  # (channels, samples); here channels == 1
print(sample_rate)  # 16000
```

...

</details>

### pyFFTW

A pythonic wrapper around FFTW, the FFT library, presenting a unified interface for all the supported transforms.

`pip install pyFFTW` · installs (wheel) · licence: BSD-3-Clause · rank 8234 · last release 2025-10-22 · [PyPI](https://pypi.org/project/pyFFTW/)

<details><summary>README extract</summary>

Sections: Conda-forge Info, PyFFTW, Requirements (i.e. what it was designed for), Optional Dependencies, Wheels, Building, Platform specific build info, Windows, Mac OSX, FreeBSD

</details>

### livekit-plugins-groq

Groq inference plugin for LiveKit Agents

`pip install livekit-plugins-groq` · installs (wheel) · licence: Apache-2.0 · rank 8314 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-groq/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for STT, TTS, and LLM with Groq fast inference.

See for more information.

Sections: Groq plugin for LiveKit Agents, Pre-requisites

</details>

### livekit-plugins-rime

LiveKit Agents Plugin for Rime

`pip install livekit-plugins-rime` · installs (wheel) · licence: Apache-2.0 · rank 8924 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-rime/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for voice synthesis and speech recognition with Rime.

See for more information.

Example:
```python
from livekit.agents import AgentSession
from livekit.plugins import rime, silero

session = AgentSession(
    vad=silero.VAD.load(),
    stt=rime.STT(
        language="en",
        mode="written",  # or "verbatim" for spoken forms
        context_terms=["LiveKit", "Rime"],
    ),
    # Configure your LLM and TTS as usual.
)
```

Sections: Rime plugin for LiveKit Agents, Pre-requisites, Speech recognition, Native streaming speech recognition, Streaming WebSocket v1 API, Prism realtime, LiveKit compatibility, Turns and interruption, Tools and settings, Response metrics, Events and limits

</details>

### pyacoustid

Bindings for Chromaprint acoustic fingerprinting and the Acoustid API

`pip install pyacoustid` · installs (wheel) · licence: MIT · rank 9180 · last release 2026-04-09 · [PyPI](https://pypi.org/project/pyacoustid/) · [source](https://github.com/beetbox/pyacoustid)

<details><summary>README extract</summary>

Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package provides
Python bindings for both the fingerprinting algorithm library, which is written
in C but portable, and the Web service, which provides fingerprint lookups.

Example:
```python
>>> import acoustid
>>> for score, recording_id, title, artist in acoustid.match(apikey, path):
>>>     ...
```

Sections: Chromaprint and Acoustid for Python, Running, Using in Your Code

</details>

### silk-python

silk encode and decode

`pip install silk-python` · installs (wheel) · licence: BSD License · rank 9222 · last release 2026-10-25 · [PyPI](https://pypi.org/project/silk-python/)

<details><summary>README extract</summary>

Example:
```python
import pysilk

with open("verybiginput.pcm", "rb") as pcm, open("output.silk", "wb") as silk:
    pysilk.encode(pcm, silk, 24000, 24000)
```

Sections: ✨ pysilk ✨, The python binding for silk-v3-decoder, 安装, 使用, 支持功能, 公开函数, 公开异常, ✨v0.2.0✨, 本机编译, 后端选择

</details>

### python-rtmidi

A Python binding for the RtMidi C++ library implemented using Cython.

`pip install python-rtmidi` · installs from source (sdist only) · licence: MIT License · rank 9356 · last release 2023-11-20 · [PyPI](https://pypi.org/project/python-rtmidi/) · [docs](https://spotlightkid.github.io/python-rtmidi/) · [source](https://gitlab.com/SpotlightKid/python-rtmidi/)

<details><summary>README extract</summary>

A Python binding for the RtMidi C++ library implemented using Cython.

Features:
[RtMidi] is a set of C++ classes which provides a concise and simple,
cross-platform API (Application Programming Interface) for realtime MIDI
input / output across Linux (ALSA & JACK), macOS / OS X (CoreMIDI & JACK), and
Windows (MultiMedia System) ...

Example:
```python
import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

with midiout:
    note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
...
```

Sections: Welcome to python-rtmidi!, Overview, Usage example

</details>

### fish-audio-sdk

The official Python library for the Fish Audio API

`pip install fish-audio-sdk` · installs (wheel) · licence: Apache Software License · rank 9444 · last release 2026-10-31 · [PyPI](https://pypi.org/project/fish-audio-sdk/) · [docs](https://docs.fish.audio) · [source](https://github.com/fishaudio/fish-audio-python)

<details><summary>README extract</summary>

The official Python library for the Fish Audio API

Documentation: Python SDK Guide | API Reference
> [!IMPORTANT]
> ## Changes to PyPI Versioning
> For existing users on Fish Audio Python SDK, please note that the starting version is now `1.0.0`. The last version before this was `2025.6.3`. ...

Example:
```python
from fishaudio import FishAudio
from fishaudio.utils import play, save

client = FishAudio()

# Generate audio
audio = client.tts.convert(text="Hello, world!")

# Play or save
play(audio)
save(audio, "output.mp3")
```

Sections: Fish Audio Python SDK, Authentication, Quick Start, Core Features, Text-to-Speech, Speech-to-Text, Real-time Streaming, Voice Cloning, Resource Clients, Error Handling, Resources

</details>

### speechmatics-voice

Speechmatics Voice Agent Python client for Real-Time API

`pip install speechmatics-voice` · installs (wheel) · licence: MIT · rank 9710 · last release 2026-01-26 · [PyPI](https://pypi.org/project/speechmatics-voice/) · [docs](https://docs.speechmatics.com/) · [source](https://github.com/speechmatics/speechmatics-python-sdk)

<details><summary>README extract</summary>

Python SDK for building voice-enabled applications using Speechmatics Real-Time API. Optimized for specific use cases: conversational AI, voice agents, transcription services, and real-time captioning.

Example:
```python
import asyncio
import os
from speechmatics.rt import Microphone
from speechmatics.voice import VoiceAgentClient, AgentServerMessageType

async def main():
    """Stream microphone audio to Speechmatics Voice Agent using 'scribe' preset"""

    # Audio configuration
    SAMPLE_RATE = 16000         # Hz
...
```

...

</details>

### omnivoice

OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models

`pip install omnivoice` · installs (wheel) · licence: Apache-2.0 · rank 9816 · last release 2026-07-16 · [PyPI](https://pypi.org/project/omnivoice/) · [source](https://github.com/k2-fsa/OmniVoice)

<details><summary>README extract</summary>

OmniVoice is a state-of-the-art massively multilingual zero-shot text-to-speech (TTS) model supporting over 600 languages. Built on a novel diffusion language model-style architecture, it generates high-quality speech with superior inference speed, supporting voice cloning and voice design. ...

Features:
- 600+ Languages Supported: The broadest language coverage among zero-shot TTS models (full list).
- Voice Cloning: State-of-the-art voice cloning quality. ...

Example:
```python
from omnivoice import OmniVoice
import soundfile as sf
import torch

model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cuda:0",
    dtype=torch.float16
)
# Apple Silicon users: use device_map="mps" instead
# Intel Arc GPU users: use device_map="xpu" instead

audio = model.generate(
...
...

</details>

### livekit-plugins-speechmatics

Agent Framework plugin for Speechmatics

`pip install livekit-plugins-speechmatics` · installs (wheel) · licence: Apache-2.0 · rank 10467 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-speechmatics/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Speechmatics STT.

See for more information.

Example:
```python
from livekit.agents import AgentSession
from livekit.plugins import speechmatics

agent = AgentSession(
    stt=speechmatics.STT(),
    turn_detection="stt",
    ...
)
```

Sections: Speechmatics STT plugin for LiveKit Agents, Model, Turn detection modes, Usage — service-side endpointing (`VAD`, default), Usage — caller-driven endpointing (`EXTERNAL`), Interim transcripts, Sentence segments, Sample rate, Diarization, Speaker identification, Pre-requisites

</details>

### speechmatics-agent-stt

Speechmatics Agent STT Python client for agent transcription

`pip install speechmatics-agent-stt` · installs (wheel) · licence: MIT · rank 10543 · last release 2026-10-19 · [PyPI](https://pypi.org/project/speechmatics-agent-stt/) · [docs](https://docs.speechmatics.com/) · [source](https://github.com/speechmatics/speechmatics-python-sdk)

<details><summary>README extract</summary>

Python client for the Speechmatics Agent STT service, built on
`speechmatics-rt`.

The Agent STT service works in segments rather than word groups, and reports the speech and
turn events a voice agent needs. This SDK runs no VAD and no turn detection of its own -
either the service's VAD closes turns, or your application's does.

Example:
```python
import asyncio
from speechmatics.agent_stt import AgentSttAsyncClient, ServerMessageType, TranscriptionConfig

async def main():
    # Uses SPEECHMATICS_API_KEY from the environment
    client = AgentSttAsyncClient(
        transcription_config=TranscriptionConfig(language="en", enable_partials=True)
    )

...
```

...

</details>

### audiostretchy

AudioStretchy is a Python library and CLI tool for high-quality time-stretching of audio files without changing pitch. Uses David Bryant's audio-stretch C library with Pedalboard for versatile audio I/O.

`pip install audiostretchy` · installs (wheel) · licence: BSD-3-Clause · rank 10856 · last release 2026-11-03 · [PyPI](https://pypi.org/project/audiostretchy/) · [source](https://github.com/twardoch/audiostretchy.git)

<details><summary>README extract</summary>

this_file: README.md

Change audio duration without changing pitch, using David Bryant's
audio-stretch TDHS engine.
Pedalboard reads and writes WAV, MP3, FLAC, OGG and AIFF; NumPy handles samples
and linear-interpolation resampling.

For a Python project, use `uv add audiostretchy`:

Run `audiostretchy --help` for all parameters. ...

Example:
```python
from audiostretchy import AudioStretch, stretch_audio

stretch_audio("input.wav", "output.wav", ratio=0.9)

processor = AudioStretch()
processor.open("input.wav")
processor.stretch(ratio=1.2)  # 20% longer
processor.resample(24000)
processor.save("output.wav")
```

</details>

### PyAudioWPatch

PortAudio fork with WASAPI loopback support

`pip install PyAudioWPatch` · does not install on CPython 3.14 · licence: Apache Software License · rank 11133 · last release 2026-10-06 · [PyPI](https://pypi.org/project/PyAudioWPatch/)

<details><summary>README extract</summary>

> If you’re looking for a hosted desktop recording API, consider checking out Recall.ai, an API that records Zoom, Google Meet, Microsoft Teams, in-person meetings, and more.

> ✨ This repo is sponsored by Recall.ai ✨

This fork will allow you to use the WASAPI device as loopback using PyAudio.

So you can *use speakers to record audio* ✨ ...

Example:
```python
import pyaudiowpatch as pyaudio

with pyaudio.PyAudio() as p:
    # Open PyA manager via context manager
    with p.open(...) as stream:
        # Open audio stream via context manager
        # Do some stuff
        ...
```

...

</details>

### livekit-plugins-inworld

Agent Framework plugin for voice synthesis and speech-to-text with Inworld's API.

`pip install livekit-plugins-inworld` · installs (wheel) · licence: Apache-2.0 · rank 11392 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-inworld/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for voice synthesis and speech-to-text with Inworld TTS and Inworld STT.

See Inworld TTS and Inworld STT for more information.

Example:
```python
"""Inworld STT + TTS voice agent example.

Demonstrates using Inworld for both speech-to-text and text-to-speech
in a LiveKit voice agent. Save this as ``inworld_agent.py`` and run:

    uv run inworld_agent.py console   # local console mode
    uv run inworld_agent.py dev       # LiveKit Cloud (requires LIVEKIT_URL,
...
```

Sections: Inworld plugin for LiveKit Agents, Authentication, Usage, TTS, TTS Streaming, STT, Example, Combined TTS + STT

</details>

### livekit-plugins-gladia

Agent Framework plugin for services using Gladia's API.

`pip install livekit-plugins-gladia` · installs (wheel) · licence: Apache-2.0 · rank 11409 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-gladia/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for speech-to-text with Gladia.

See for more information.

Features:
- Streaming speech-to-text
- Multi-language support
- Code-switching between languages
- Interim results (partial transcriptions)
- Voice activity detection with energy filtering
- Optional real-time translation ...

Example:
```python
from livekit.stt import STT
from livekit.plugins.gladia.stt import STT as GladiaSTT

# Basic initialization
stt = GladiaSTT(
    api_key="your-api-key-here",  # or use GLADIA_API_KEY env var
    interim_results=True
)

# With more options
stt = GladiaSTT(
    languages=["en", "fr"],                     # Specify languages or let Gladia auto-detect
...
```

Sections: Gladia plugin for LiveKit Agents, Pre-requisites, Features, Example Usage, Using with LiveKit Agents Framework

</details>

### python-osc

Open Sound Control server and client implementations in pure Python

`pip install python-osc` · installs (wheel) · licence: Freely Distributable · rank 11584 · last release 2026-04-02 · [PyPI](https://pypi.org/project/python-osc/) · [source](https://github.com/attwad/python-osc)

<details><summary>README extract</summary>

Open Sound Control server and client implementations in pure python.

Features:
* UDP and TCP blocking/threading/forking/asyncio server implementations
* UDP and TCP clients, including asyncio support
* TCP support for 1.0 and 1.1 protocol formats
* int, int64, float, string, double, MIDI, timestamps, blob, nil OSC arguments
* ...

Example:
```python
"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import udp_client

if name == "main":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
...
```

...

</details>

### monotonic-alignment-search

Monotonically align text and speech

`pip install monotonic-alignment-search` · installs (wheel) · licence: MIT · rank 11703 · last release 2026-10-29 · [PyPI](https://pypi.org/project/monotonic-alignment-search/) · [source](https://github.com/eginhard/monotonic_alignment_search)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Enno Hermann

SPDX-License-Identifier: MIT

Implementation of MAS from Glow-TTS
for easy reuse in other projects.

Example:
```python
from monotonic_alignment_search import maximum_path

# value (torch.Tensor): [batch_size, t_x, t_y]
# mask  (torch.Tensor): [batch_size, t_x, t_y]
path = maximum_path(value, mask, implementation="cython")
```

Sections: Monotonic Alignment Search (MAS), Usage, References

</details>

### eyeD3

Python audio data toolkit (ID3 and MP3)

`pip install eyeD3` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12040 · last release 2025-11-16 · [PyPI](https://pypi.org/project/eyeD3/) · [source](https://github.com/nicfit/eyeD3)

_README extract left out: share-alike licence._

### livekit-plugins-fishaudio

Agent Framework plugin for voice synthesis and speech recognition with Fish Audio's API.

`pip install livekit-plugins-fishaudio` · installs (wheel) · licence: Apache-2.0 · rank 12074 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-fishaudio/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for voice synthesis and realtime speech-to-text with Fish Audio.

- Docs: `

Example:
```python
from livekit.agents import AgentSession
from livekit.plugins import fishaudio

# Basic usage with env-based credentials
tts = fishaudio.TTS()

session = AgentSession(
    tts=tts,
    # ... stt, llm, etc.
)
```

Sections: Fish Audio plugin for LiveKit Agents, Prerequisites, Usage, Speech-to-text

</details>

### livekit-plugins-langchain

LangChain/LangGraph plugin for LiveKit agents

`pip install livekit-plugins-langchain` · installs (wheel) · licence: Apache-2.0 · rank 12320 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-langchain/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

This plugin integrates capabilites from LangChain within LiveKit Agents

Example:
```python
from langgraph.graph import StateGraph
from livekit.agents import Agent, AgentSession, JobContext
from livekit.plugins import langchain

...

def entrypoint(ctx: JobContext):
    graph = StateGraph(...).compile()

    session = AgentSession(
        vad=...,
        stt=...,
        tts=...,
    )

    await session.start(
...
```

Sections: LangChain plugin for LiveKit Agents, Usage, Using LangGraph workflows

</details>

### livekit-plugins-anam

Agent Framework plugin for anam

`pip install livekit-plugins-anam` · installs (wheel) · licence: Apache-2.0 · rank 12624 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-anam/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for the Anam virtual avatar.

See the Anam integration docs for more information.

Sections: Anam plugin for LiveKit Agents, Pre-requisites

</details>

### ko-speech-tools

Korean speech/NLP tools

`pip install ko-speech-tools` · installs (wheel) · licence: Apache-2.0 · rank 12733 · last release 2026-10-29 · [PyPI](https://pypi.org/project/ko-speech-tools/) · [source](https://github.com/eginhard/ko-speech-tools)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Enno Hermann

SPDX-License-Identifier: Apache-2.0

This package contains a variety of tools for Korean speech and language
processing, including:
- Hangul romanization.
- Jamo conversion.
- Grapheme-to-phoneme conversion (G2P). ...

Example:
```python
>>> from ko_speech_tools import hangul_romanize

>>> hangul_romanize("물엿")
'mul-yeos'
```

Sections: Korean Speech Tools, Usage

</details>

### essentia

Library for audio and music analysis, description and synthesis

`pip install essentia` · installs (wheel) · licence: AGPL-3.0-only · rank 12867 · last release 2026-05-19 · [PyPI](https://pypi.org/project/essentia/) · [docs](http://essentia.upf.edu) · [source](https://github.com/MTG/essentia)

_README extract left out: share-alike licence._

### deepfilternet

Noise supression using deep filtering

`pip install deepfilternet` · installs (wheel) · licence: MIT License · rank 13092 · last release 2023-08-31 · [PyPI](https://pypi.org/project/deepfilternet/) · [source](https://github.com/Rikorose/DeepFilterNet)

### mediafile

A simple, cross-format library for reading and writing media file metadata.

`pip install mediafile` · installs (wheel) · licence: MIT · rank 13143 · last release 2026-04-24 · [PyPI](https://pypi.org/project/mediafile/) · [docs](https://mediafile.readthedocs.io) · [source](https://github.com/beetbox/mediafile)

<details><summary>README extract</summary>

MediaFile is a simple interface to the metadata tags for many audio file
formats. It wraps Mutagen, a high-quality library for low-level tag
manipulation, with a high-level, format-independent interface for a common set
of tags.

MediaFile is available on PyPI. Install it by typing `pip install
mediafile`. It works on Python 3.10 or later. Then: ...

Example:
```python
from mediafile import MediaFile

f = MediaFile("Lucy.mp3")
f.title
"Lucy in the Sky with Diamonds"
f.artist = "The Beatles"
f.save()
```

Sections: MediaFile: read and write audio files' tags in Python, Synopsis, Documentation

</details>

### beat-this

Beat This! beat tracker

`pip install beat-this` · installs (wheel) · licence: MIT · rank 13303 · last release 2026-04-14 · [PyPI](https://pypi.org/project/beat-this/) · [source](https://github.com/CPJKU/beat_this)

<details><summary>README extract</summary>

Official implementation of the beat tracker from the ISMIR 2024 paper "Beat This! Accurate Beat Tracking Without DBN Postprocessing" by Francesco Foscarin, Jan Schlüter and Gerhard Widmer.

* Inference
* Available models
* Data
* Reproducing metrics from the paper
* Training
* Reusing the loss
* Reusing the model
* Citation ...

Example:
```python
from beat_this.inference import File2Beats
file2beats = File2Beats(checkpoint_path="final0", device="cuda", dbn=False)
```

Sections: Beat This!, Inference, Online demo, Requirements, Command line, Python class, Available models, Data, Annotations, Spectrograms, Recreating spectrograms, Reproducing metrics from the paper

</details>

### typed-ffmpeg

Modern Python & TypeScript FFmpeg wrappers with comprehensive typing (latest version)

`pip install typed-ffmpeg` · installs (wheel) · licence: MIT · rank 13336 · last release 2026-10-21 · [PyPI](https://pypi.org/project/typed-ffmpeg/)

<details><summary>README extract</summary>

Modern Python FFmpeg wrappers with comprehensive typing.

Features:
- Full type hints for all FFmpeg filters, codecs, and formats
- IDE autocomplete support
- Runtime validation
- Filter graph visualization
- JSON serialization

Example:
```python
import ffmpeg

# Input and output
input_file = ffmpeg.input("input.mp4")
output_file = input_file.hflip().output("output.mp4")
output_file.run()

# Complex filter graph
in_file = ffmpeg.input("input.mp4")
overlay_file = ffmpeg.input("overlay.png")

output = (
    ffmpeg.filters
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
...
```

Sections: typed-ffmpeg, Usage, Requirements, Features, Documentation

</details>

### speechmatics-batch

Speechmatics Batch API Client

`pip install speechmatics-batch` · installs (wheel) · licence: MIT · rank 13596 · last release 2026-11-06 · [PyPI](https://pypi.org/project/speechmatics-batch/) · [docs](https://docs.speechmatics.com/) · [source](https://github.com/speechmatics/speechmatics-python-sdk)

<details><summary>README extract</summary>

Python client for Speechmatics Batch API, with both async and blocking interfaces.

> Migrating from `speechmatics-python` (the legacy `BatchClient`)? See MIGRATION.md for a full guide, including a method-by-method mapping table.

Features:
- Async (`AsyncClient`) and blocking (`Client`) API clients with comprehensive error handling
- Synchronous transcription support: get a transcript in a single request, without polling
- Type hints throughout for better IDE support ...

Example:
```python
from speechmatics.batch import Client

# Create a client using environment variable SPEECHMATICS_API_KEY
with Client() as client:
    # Simple transcription
    result = client.transcribe("audio.wav")
    print(result.transcript_text)
```

...

</details>

### pyopen-wakeword

An open-source audio wake word (or phrase) detection framework with a focus on performance and simplicity.

`pip install pyopen-wakeword` · installs (wheel) · licence: Apache Software License · rank 13737 · last release 2025-10-28 · [PyPI](https://pypi.org/project/pyopen-wakeword/) · [source](https://github.com/rhasspy/pyopen-wakeword)

<details><summary>README extract</summary>

Alternative Python library for openWakeWord.

Uses a pre-compiled Tensorflow Lite library.

Example:
```python
from pyopen_wakeword import OpenWakeWord, OpenWakeWordFeatures, Model

oww = OpenWakeWord.from_builtin(Model.OKAY_NABU)
oww_features = OpenWakeWordFeatures()

# Audio must be 16-bit mono at 16Khz
while audio := get_10ms_of_audio():
    assert len(audio) == 160 * 2  # 160 samples
    for features in oww_features.process_streaming(audio):
...
```

Sections: Python openWakeWord, Usage, Command-Line, WAVE files, Live

</details>

### audiotsm

A real-time audio time-scale modification library

`pip install audiotsm` · installs (wheel) · licence: MIT License · rank 13769 · last release 2017-09-21 · [PyPI](https://pypi.org/project/audiotsm/)

<details><summary>README extract</summary>

AudioTSM is a python library for real-time audio time-scale modification
procedures, i.e. algorithms that change the speed of an audio signal without
changing its pitch.

Documentation:

Examples:

Source code repository and issue tracker:

Python Package Index:

License:
 MIT -- see the file `LICENSE` for details.

Example:
```python
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter

with WavReader(input_filename) as reader:
    with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
        tsm = phasevocoder(reader.channels, speed=0.5)
        tsm.run(reader, writer)
```

Sections: A real-time audio time-scale modification library, Basic usage, Thanks

</details>

### pilk

python silk voice library

`pip install pilk` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 13837 · last release 2023-05-26 · [PyPI](https://pypi.org/project/pilk/)

_README extract left out: share-alike licence._

### livekit-plugins-sarvam

Agent Framework plugin for services using Sarvam.ai's API.

`pip install livekit-plugins-sarvam` · installs (wheel) · licence: Apache-2.0 · rank 13897 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-plugins-sarvam/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/agents)

<details><summary>README extract</summary>

Support for Sarvam.ai's Indian-language voice AI services in LiveKit Agents.

Features:
- Speech-to-Text (STT): Convert audio to text using Sarvam's "Saaras" models. See the STT docs for more information.
- Text-to-Speech (TTS): Convert text to audio using Sarvam's "Bulbul" models. See the TTS docs for more information. ...

Example:
```python
from livekit.plugins import sarvam

llm = sarvam.LLM(
    model="sarvam-30b",  # or `sarvam-30b-16k`, `sarvam-105b`, `sarvam-105b-32k`
)
```

Sections: Sarvam.ai Plugin for LiveKit Agents, Features, Pre-requisites, LLM Usage

</details>

### supertonic

High-quality Text-to-Speech synthesis with ONNX Runtime

`pip install supertonic` · installs (wheel) · licence: MIT · rank 13914 · last release 2026-05-18 · [PyPI](https://pypi.org/project/supertonic/) · [docs](https://supertone-inc.github.io/supertonic-py) · [source](https://github.com/supertone-inc/supertonic-py)

<details><summary>README extract</summary>

> Supertonic-3: Multilingual synthesis across 31 languages, plus a `na` fallback for text whose language is unknown or outside the supported set.

Example:
```python
from supertonic import TTS

# Note: first run downloads the model (~400MB) into ~/.cache/supertonic3/
tts = TTS(auto_download=True)       # Initialize TTS engine

style = tts.get_voice_style(voice_name="M1")   # 10 built-in voices: M1–M5, F1–F5

wav, duration = tts.synthesize(
    text="Supertonic is a lightning fast, on-device TTS system.",
...
```

...

</details>

### playsound

Pure Python, cross platform, single function module with no dependencies for playing sounds.

`pip install playsound` · installs from source (sdist only) · licence: MIT License · rank 13999 · last release 2021-07-24 · [PyPI](https://pypi.org/project/playsound/)

<details><summary>README extract</summary>

*Pure Python, cross platform, single function module with no dependencies for playing sounds.*

Example:
```python
>>> from playsound import playsound
>>> playsound('/path/to/a/sound/file/you/want/to/play.mp3')
```

Sections: playsound, Quick Start, Documentation, Copyright

</details>

### pyalsaaudio

ALSA bindings

`pip install pyalsaaudio` · installs from source (sdist only) · licence: Python Software Foundation License · rank 14150 · last release 2024-05-30 · [PyPI](https://pypi.org/project/pyalsaaudio/)

<details><summary>README extract</summary>

This package contains wrappers for accessing the ALSA API from Python.
It is fairly complete for PCM devices and Mixer access.

</details>

### pymp3

Read and write MP3 files.

`pip install pymp3` · installs from source (sdist only) · licence: GNU General Public License v2 (GPLv2) · rank 14259 · last release 2024-03-06 · [PyPI](https://pypi.org/project/pymp3/)

_README extract left out: share-alike licence._

### livekit-plugins-dtln

DTLN noise suppression plugin for LiveKit Agents — self-hosted, in-process, no cloud API

`pip install livekit-plugins-dtln` · installs (wheel) · licence: MIT License · rank 14637 · last release 2026-09-11 · [PyPI](https://pypi.org/project/livekit-plugins-dtln/) · [source](https://github.com/aloware/livekit-plugins-dtln)

<details><summary>README extract</summary>

Python LiveKit plugin for DTLN (Dual-Signal Transformation LSTM Network) noise suppression — a fully self-hosted, open-source alternative to cloud-based noise cancellation services like Krisp or AI-coustics.

Runs entirely in-process using ONNX Runtime. No cloud API, no per-minute fees, no proprietary binaries. ...

Features:
| | DTLN (this plugin) | Krisp / AI-coustics |

| Hosting | Self-hosted, in-process | Cloud API required |
| Cost | Free (open weights) | Per-minute billing |
| LiveKit | Works with self-hosted | Requires LiveKit Cloud |
| Latency | ~8 ms (one block ...

Example:
```python
from livekit.agents import room_io
from livekit.plugins import dtln

await session.start(
    # ...,
    room_options=room_io.RoomOptions(
        audio_input=room_io.AudioInputOptions(
...

</details>

## Also in this topic

- [moviepy](multimedia.md#moviepy) - Video editing with Python
- [tinytag](internet-www-http.md#tinytag) - Read audio file metadata
- [ffmpy](multimedia.md#ffmpy) - A simple Python wrapper for FFmpeg
- [cloudinary](internet-www-http.md#cloudinary) - Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django.
- [pygame](games-entertainment.md#pygame) - Python Game Development
- [torch-audiomentations](multimedia.md#torch-audiomentations) - A Pytorch library for audio data augmentation. Inspired by audiomentations. Useful for deep learning.
- [pipecat-ai](communications-conferencing.md#pipecat-ai) - An open source framework for voice (and multimodal) assistants
- [music21](artistic-software.md#music21) - A Toolkit for Computer-Aided Musical Analysis and Computational Musicology.
- [descript-audiotools](artistic-software.md#descript-audiotools) - Utilities for handling audio.
- [pygame-ce](games-entertainment.md#pygame-ce) - Python Game Development
- [descript-audio-codec](artistic-software.md#descript-audio-codec) - A high-quality general neural audio codec.
- [symusic](file-formats.md#symusic) - A high performance MIDI file parser with comprehensible interface.
- [audiomentations](multimedia.md#audiomentations) - A Python library for audio data augmentation. Inspired by albumentations. Useful for machine learning.
- [daily-python](communications-conferencing.md#daily-python) - Daily Client SDK for Python
- [pipecat-ai-prebuilt](communications-conferencing.md#pipecat-ai-prebuilt) - A simple, ready-to-use prebuilt client supporting all Pipecat transports.
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [streamlink](internet-www-http.md#streamlink) - Streamlink is a command-line utility that extracts streams from various services and pipes them into a video player of choice.
- [coqui-tts](multimedia.md#coqui-tts) - Deep learning for Text to Speech.
- [pulsectl](multimedia.md#pulsectl) - Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)
- [soco](home-automation.md#soco) - SoCo (Sonos Controller) is a simple library to control Sonos speakers.
- [pipecat-ai-whisker](communications-conferencing.md#pipecat-ai-whisker) - A real-time debugger for Pipecat
- [pylast](internet.md#pylast) - A Python interface to Last.fm and Libre.fm
- [python-vlc](multimedia.md#python-vlc) - VLC bindings for python.
- [bithuman](multimedia.md#bithuman) - Real-time talking-avatar SDK: audio in, lip-synced frames out, on your own Mac, Linux or Windows machine.
- [pipecat-ai-small-webrtc-prebuilt](communications-conferencing.md#pipecat-ai-small-webrtc-prebuilt) - A simple, ready-to-use client for testing the SmallWebRTCTransport.
- [stftpitchshift](artistic-software.md#stftpitchshift) - STFT based pitch and timbre shifting
