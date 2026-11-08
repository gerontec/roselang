# Multimedia / Video

[Index](README.md) · 17 packages in this topic, 51 more listed under another topic, by downloads.

### yt-dlp

A feature-rich command-line audio/video downloader

`pip install yt-dlp` · installs (wheel) · licence: Unlicense · rank 862 · last release 2026-10-26 · [PyPI](https://pypi.org/project/yt-dlp/) · [docs](https://github.com/yt-dlp/yt-dlp#readme) · [source](https://github.com/yt-dlp/yt-dlp)

<details><summary>README extract</summary>

Official repository:

PS: Some links in this document will not work since this is a copy of the README.md from Github

yt-dlp is a feature-rich command-line audio/video downloader with support for thousands of sites. The project is a fork of youtube-dl based on the now inactive youtube-dlc. ...

Example:
```python
curl -L  | gpg --import
gpg --verify SHA2-256SUMS.sig SHA2-256SUMS
gpg --verify SHA2-512SUMS.sig SHA2-512SUMS
```

Sections: Recommended, Alternatives, Misc, Licensing, UPDATE, DEPENDENCIES, Strongly recommended, Networking, Impersonation, Metadata, Deprecated, COMPILE, Platform-independent Binary (UNIX)

</details>

### scenedetect

Video scene cut/shot detection program and Python library (bundles the opencv-python OpenCV variant and the scenedetect CLI).

`pip install scenedetect` · installs (wheel) · licence: BSD-3-Clause · rank 3580 · last release 2026-10-12 · [PyPI](https://pypi.org/project/scenedetect/) · [docs](https://www.scenedetect.com/docs/) · [source](https://github.com/Breakthrough/PySceneDetect)

<details><summary>README extract</summary>

Documentation:

Github Repo:

Install: `pip install --upgrade scenedetect` (or `scenedetect-headless` for servers)

Packages: scenedetect (CLI + `opencv-python`) and scenedetect-headless (CLI + `opencv-python-headless`). Both provide the same `scenedetect` module -- install only one. ...

Example:
```python
from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
scene_list = detect('my_video.mp4', AdaptiveDetector())
split_video_ffmpeg('my_video.mp4', scene_list)
```

Sections: PySceneDetect, Video Scene Cut Detection and Analysis Tool

</details>

### srt

A tiny library for parsing, modifying, and composing SRT files.

`pip install srt` · installs from source (sdist only) · licence: MIT License · rank 3592 · last release 2023-03-28 · [PyPI](https://pypi.org/project/srt/)

<details><summary>README extract</summary>

srt is a tiny but featureful Python library for parsing, modifying, and
composing SRT files. Take a look at the quickstart for a basic overview of
the library. Detailed API documentation is also available.

Want to see some examples of its use? Take a look at the tools shipped with
the library. ...

Features:
- Can parse many broken SRT files which other SRT libraries cannot, and fix them
- Extremely lightweight, ~200 lines of code excluding docstrings
- Simple, intuitive API
- High quality test suite using Hypothesis ...

Example:
```python
>>> data = '''\
1
00:00:33,843 --> 00:00:38,097
地球上只有3%的水是淡水

2
00:00:40,641 --> 00:00:44,687
可是这些珍贵的淡水中却充满了惊奇

3
00:00:57,908 --> 00:01:03,414
所有陆地生命归根结底都依赖於淡水

'''
>>> for sub in srt.parse(data):
...     print(sub)
...
```

...

</details>

### pysubs2

A library for editing subtitle files

`pip install pysubs2` · installs (wheel) · licence: MIT · rank 7285 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pysubs2/) · [docs](https://pysubs2.readthedocs.io)

<details><summary>README extract</summary>

pysubs2 is a Python library for editing subtitle files. It’s based on *SubStation Alpha*,
the native format of Aegisub; it also supports *SubRip (SRT)*,
*MicroDVD*, *MPL2*, *TMP*, *WebVTT*, *TTML* and *SAMI* formats and *OpenAI Whisper* captions. ...

Example:
```python
import pysubs2
subs = pysubs2.load("my_subtitles.ass", encoding="utf-8")
subs.shift(s=2.5)
for line in subs:
    line.text = "{\\be1}" + line.text
subs.save("my_subtitles_edited.ass")
```

Sections: pysubs2, Usage

</details>

### pyrealsense2

Python Wrapper for Realsense SDK 2.0.

`pip install pyrealsense2` · installs (wheel) · licence: Apache Software License · rank 7588 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyrealsense2/)

<details><summary>README extract</summary>

The Python wrapper for RealSense SDK 2.0 provides the C++ to Python binding required to access the SDK.

Example:
```python
import pyrealsense2 as rs
pipe = rs.pipeline()
profile = pipe.start()
try:
  for i in range(0, 100):
    frames = pipe.wait_for_frames()
    for f in frames:
      print(f.profile)
finally:
    pipe.stop()
```

Sections: Python Wrapper for RealSense SDK 2.0, Quick start

</details>

### pysrt

SubRip (.srt) subtitle parser and writer

`pip install pysrt` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 7737 · last release 2020-01-20 · [PyPI](https://pypi.org/project/pysrt/)

_README extract left out: share-alike licence._

### youtube_dl

YouTube video downloader

`pip install youtube_dl` · installs (wheel) · licence: Public Domain · rank 9905 · last release 2021-12-16 · [PyPI](https://pypi.org/project/youtube_dl/)

<details><summary>README extract</summary>

Command-line program to download videos from YouTube.com and other video sites

</details>

### ffprobe-python

A wrapper around ffprobe command to extract metadata from media files.

`pip install ffprobe-python` · installs (wheel) · licence: MIT License · rank 10713 · last release 2019-11-05 · [PyPI](https://pypi.org/project/ffprobe-python/)

<details><summary>README extract</summary>

A wrapper around the ffprobe command to extract metadata from media files.

Usage::

This software is now maintained by Mark Ma <519329064@qq.com>.

(The MIT License)

Copyright 2013 Simon Hargreaves <simon@simon-hargreaves.com>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated ...

Example:
```python
# !/usr/bin/env python

from ffprobe import FFProbe

metadata=FFProbe('test-media-file.mov')

for stream in metadata.streams:
    if stream.is_video():
        print('Stream contains {} frames.'.format(stream.frames()))
```

</details>

### scikit-video

Video Processing in Python

`pip install scikit-video` · installs (wheel) · licence: BSD License · rank 11792 · last release 2018-09-20 · [PyPI](https://pypi.org/project/scikit-video/)

<details><summary>README extract</summary>

This library provides easy access to common as well as
state-of-the-art video processing routines. Check out the
website for more details.

</details>

### scenedetect-headless

Video scene cut/shot detection program and Python library (bundles the opencv-python-headless OpenCV variant and the scenedetect CLI; for servers without GUI libraries).

`pip install scenedetect-headless` · installs (wheel) · licence: BSD-3-Clause · rank 13320 · last release 2026-10-12 · [PyPI](https://pypi.org/project/scenedetect-headless/) · [docs](https://www.scenedetect.com/docs/) · [source](https://github.com/Breakthrough/PySceneDetect)

<details><summary>README extract</summary>

Documentation:

Github Repo:

Install: `pip install --upgrade scenedetect` (or `scenedetect-headless` for servers)

Packages: scenedetect (CLI + `opencv-python`) and scenedetect-headless (CLI + `opencv-python-headless`). Both provide the same `scenedetect` module -- install only one. ...

Example:
```python
from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
scene_list = detect('my_video.mp4', AdaptiveDetector())
split_video_ffmpeg('my_video.mp4', scene_list)
```

Sections: PySceneDetect, Video Scene Cut Detection and Analysis Tool

</details>

### nvidia-vfx

Python bindings for NVIDIA Video Effects SDK

`pip install nvidia-vfx` · installs from source (sdist only) · licence: Other/Proprietary License · rank 13716 · last release 2026-09-30 · [PyPI](https://pypi.org/project/nvidia-vfx/)

<details><summary>README extract</summary>

`nvidia-vfx` provides Python bindings for the NVIDIA VFX SDK. It includes the VideoSuperRes, VideoFrameGeneration, and TrueHDR effects for GPU-accelerated video enhancement, frame interpolation, and SDR-to-HDR10 conversion from Python.

Features:
- Video Frame Generation – generate intermediate frames between consecutive frames for smoother playback or slow motion.
- Video Super Resolution – upscale and enhance SDR video up to 4x while reducing compression artifacts. ...

Example:
```python
import torch
from nvvfx import VideoSuperRes

# Example input: 1080p RGB frame on CUDA in [0, 1] range
frame = torch.rand(3, 1080, 1920, device="cuda", dtype=torch.float32)

# Create effect with standard HIGH quality (default)
vsr = VideoSuperRes(quality=VideoSuperRes.QualityLevel.HIGH)
...

</details>

### pywidevine

Widevine CDM (Content Decryption Module) implementation in Python.

`pip install pywidevine` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14126 · last release 2025-10-27 · [PyPI](https://pypi.org/project/pywidevine/) · [source](https://github.com/devine-dl/pywidevine)

_README extract left out: share-alike licence._

### otio-aaf-adapter

OpenTimelineIO AAF Adapter

`pip install otio-aaf-adapter` · installs (wheel) · licence: Apache Software License · rank 14329 · last release 2025-11-21 · [PyPI](https://pypi.org/project/otio-aaf-adapter/)

<details><summary>README extract</summary>

Features:
This project is a OpenTimelineIO adapter for reading and writing Advanced Authoring Format (AAF) files.
This adapter was originally included with OpenTimelineIO as a contrib adapter. ...

Sections: Overview, Feature Matrix, Requirements, Licensing

</details>

### pyjianyingdraft

轻量、灵活、易上手的Python剪映草稿生成及导出工具，构建全自动化视频剪辑/混剪流水线

`pip install pyjianyingdraft` · installs (wheel) · licence: not stated · rank 14335 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pyjianyingdraft/)

<details><summary>README extract</summary>

> 🧪 本项目的CapCut版本正在开发中，欢迎关注CapCut版本仓库

> 📢 欢迎加入Discord服务器进行用法或新功能的讨论

Sections: pyJianYingDraft, 轻量、灵活、易上手的Python剪映草稿生成及导出工具，构建全自动视频剪辑/混剪流水线！, 使用思路, 功能清单, 视频与图片, 贴纸, 音频, 轨道, 特效、滤镜和转场, 文本及字幕, 模板模式, 批量导出, 安装, 跨平台兼容性

</details>

### transnetv2-pytorch

TransNetV2 PyTorch implementation for video scene detection

`pip install transnetv2-pytorch` · installs (wheel) · licence: MIT · rank 14377 · last release 2025-06-01 · [PyPI](https://pypi.org/project/transnetv2-pytorch/) · [source](https://github.com/allenday/transnetv2_pytorch)

<details><summary>README extract</summary>

This repository contains a PyTorch implementation of TransNet V2: An effective deep network architecture for fast shot transition detection.

This is a PyTorch reimplementation of the TransNetV2 model that produces identical results as the original TensorFlow version. The code is for inference only. ...

Example:
```python
import torch
from transnetv2_pytorch import TransNetV2

# Initialize model
model = TransNetV2(device='auto')
model.eval()

# Load weights
state_dict = torch.load("transnetv2-pytorch-weights.pth", map_location=model.device)
model.load_state_dict(state_dict)

with torch.no_grad():
    # Primary method: Scene detection
...
```

...

</details>

### pyvirtualcam

Send frames to a virtual camera

`pip install pyvirtualcam` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 14890 · last release 2026-01-24 · [PyPI](https://pypi.org/project/pyvirtualcam/)

_README extract left out: share-alike licence._

### enzyme

Video metadata parser

`pip install enzyme` · installs (wheel) · licence: MIT License · rank 14941 · last release 2024-06-25 · [PyPI](https://pypi.org/project/enzyme/) · [docs](https://enzyme.readthedocs.org) · [source](https://github.com/Diaoul/enzyme)

<details><summary>README extract</summary>

Enzyme is a Python module to parse video metadata.

Example:
```python
>>> import enzyme
>>> with open('example.mkv', 'rb') as f:
...     mkv = enzyme.MKV(f)
...
>>> mkv.info
<Info [title=None, duration=0:00:01.440000, date=2015-03-14 08:40:16]>
>>> mkv.video_tracks
[<VideoTrack [2, 720x576, V_DIRAC, name=u'Video\x00', language=None]>]
>>> mkv.audio_tracks
...
```

Sections: Enzyme, Usage

</details>

## Also in this topic

- [av](multimedia-sound-audio.md#av) - Pythonic bindings for FFmpeg's libraries.
- [livekit-api](multimedia-sound-audio.md#livekit-api) - Python Server API for LiveKit
- [livekit](multimedia-sound-audio.md#livekit) - Python Real-time SDK for LiveKit
- [moviepy](multimedia.md#moviepy) - Video editing with Python
- [livekit-agents](multimedia-sound-audio.md#livekit-agents) - A powerful framework for building realtime voice AI agents
- [livekit-plugins-silero](multimedia-sound-audio.md#livekit-plugins-silero) - Agent Framework Plugin for Silero
- [ffmpy](multimedia.md#ffmpy) - A simple Python wrapper for FFmpeg
- [cloudinary](internet-www-http.md#cloudinary) - Upload, transform, optimize, and manage images and videos with Cloudinary from Python or Django.
- [livekit-plugins-openai](multimedia-sound-audio.md#livekit-plugins-openai) - Agent Framework plugin for services from OpenAI
- [livekit-plugins-elevenlabs](multimedia-sound-audio.md#livekit-plugins-elevenlabs) - Agent Framework plugin for voice synthesis with ElevenLabs' API.
- [pytube](internet.md#pytube) - Python 3 library for downloading YouTube Videos.
- [livekit-plugins-deepgram](multimedia-sound-audio.md#livekit-plugins-deepgram) - Agent Framework plugin for services using Deepgram's API.
- [livekit-plugins-cartesia](multimedia-sound-audio.md#livekit-plugins-cartesia) - LiveKit Agents Plugin for Cartesia
- [pipecat-ai](communications-conferencing.md#pipecat-ai) - An open source framework for voice (and multimodal) assistants
- [livekit-plugins-turn-detector](multimedia-sound-audio.md#livekit-plugins-turn-detector) - End of utterance detection for LiveKit Agents
- [livekit-plugins-google](multimedia-sound-audio.md#livekit-plugins-google) - Agent Framework plugin for services from Google Cloud
- [pymp4](multimedia-sound-audio.md#pymp4) - Python parser for MP4 boxes
- [livekit-plugins-assemblyai](multimedia-sound-audio.md#livekit-plugins-assemblyai) - Agent Framework plugin for AssemblyAI
- [supervision](multimedia-graphics.md#supervision) - A set of easy-to-use utils that will come in handy in any Computer Vision project
- [mediapy](multimedia-graphics.md#mediapy) - Read/write/show images and videos in an IPython notebook
- [livekit-plugins-anthropic](multimedia-sound-audio.md#livekit-plugins-anthropic) - Agent Framework plugin for services from Anthropic
- [livekit-plugins-xai](multimedia-sound-audio.md#livekit-plugins-xai) - Agent Framework plugin for xAI
- [daily-python](communications-conferencing.md#daily-python) - Daily Client SDK for Python
- [livekit-plugins-azure](multimedia-sound-audio.md#livekit-plugins-azure) - Agent Framework plugin for services from Azure
- [pytubefix](internet.md#pytubefix) - Python3 library for downloading YouTube Videos.
- [OpenImageIO](multimedia-graphics.md#openimageio) - Reading, writing, and processing images in a wide variety of file formats, using a format-agnostic API, aimed at VFX applications.
- [livekit-plugins-aws](multimedia-sound-audio.md#livekit-plugins-aws) - LiveKit Agents Plugin for services from AWS
- [OpenTimelineIO](multimedia-graphics.md#opentimelineio) - Editorial interchange format and API
- [manim](multimedia-graphics.md#manim) - Animation engine for explanatory math videos.
- [pipecat-ai-prebuilt](communications-conferencing.md#pipecat-ai-prebuilt) - A simple, ready-to-use prebuilt client supporting all Pipecat transports.
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [streamlink](internet-www-http.md#streamlink) - Streamlink is a command-line utility that extracts streams from various services and pipes them into a video player of choice.
- [pyaaf2](multimedia-graphics.md#pyaaf2) - A python module for reading and writing advanced authoring format files
- [livekit-plugins-speechmatics](multimedia-sound-audio.md#livekit-plugins-speechmatics) - Agent Framework plugin for Speechmatics
- [pypylon](multimedia-graphics.md#pypylon) - The official Python language binding for the Basler pylon C++ APIs.
- [livekit-plugins-inworld](multimedia-sound-audio.md#livekit-plugins-inworld) - Agent Framework plugin for voice synthesis and speech-to-text with Inworld's API.
- [livekit-plugins-gladia](multimedia-sound-audio.md#livekit-plugins-gladia) - Agent Framework plugin for services using Gladia's API.
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [livekit-plugins-fishaudio](multimedia-sound-audio.md#livekit-plugins-fishaudio) - Agent Framework plugin for voice synthesis and speech recognition with Fish Audio's API.
- [pipecat-ai-whisker](communications-conferencing.md#pipecat-ai-whisker) - A real-time debugger for Pipecat
- [otio-fcp-adapter](multimedia-graphics.md#otio-fcp-adapter) - OpenTimelineIO FCP XML Adapter
- [livekit-plugins-anam](multimedia-sound-audio.md#livekit-plugins-anam) - Agent Framework plugin for anam
- [python-vlc](multimedia.md#python-vlc) - VLC bindings for python.
- [typed-ffmpeg](multimedia-sound-audio.md#typed-ffmpeg) - Modern Python & TypeScript FFmpeg wrappers with comprehensive typing (latest version)
- [TikTokLive](communications-chat.md#tiktoklive) - Unofficial TikTok LIVE API for Python: real-time chat, gift, like, follow and viewer events from any TikTok livestream.
- [bithuman](multimedia.md#bithuman) - Real-time talking-avatar SDK: audio in, lip-synced frames out, on your own Mac, Linux or Windows machine.
- [otio-cmx3600-adapter](multimedia-graphics.md#otio-cmx3600-adapter) - OpenTimelineIO CMX 3600 EDL Adapter
- [livekit-plugins-sarvam](multimedia-sound-audio.md#livekit-plugins-sarvam) - Agent Framework plugin for services using Sarvam.ai's API.
- [pipecat-ai-small-webrtc-prebuilt](communications-conferencing.md#pipecat-ai-small-webrtc-prebuilt) - A simple, ready-to-use client for testing the SmallWebRTCTransport.
- [otio-fcpx-xml-adapter](multimedia-graphics.md#otio-fcpx-xml-adapter) - OpenTimelineIO FCP X XML Adapter
