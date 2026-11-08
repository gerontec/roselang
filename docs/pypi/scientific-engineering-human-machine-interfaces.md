# Scientific/Engineering / Human Machine Interfaces

[Index](README.md) · 2 packages in this topic, 15 more listed under another topic, by downloads.

### textdistance

Compute distance between the two texts.

`pip install textdistance` · installs (wheel) · licence: MIT License · rank 2809 · last release 2024-07-16 · [PyPI](https://pypi.org/project/textdistance/)

<details><summary>README extract</summary>

TextDistance -- python library for comparing distance between two or more sequences by many algorithms.

Features:

- 30+ algorithms
- Pure python implementation
- Simple usage
- More than two sequences comparing
- Some algorithms have more than one implementation in one class.
- Optional numpy usage for maximum speed. ...

Example:
```python
import textdistance

textdistance.hamming('test', 'text')
# 1

textdistance.hamming.distance('test', 'text')
# 1

textdistance.hamming.similarity('test', 'text')
# 3

textdistance.hamming.normalized_distance('test', 'text')
# 0.25

textdistance.hamming.normalized_similarity('test', 'text')
# 0.75

...
```

...

</details>

### pycomm3

A Python Ethernet/IP library for communicating with Allen-Bradley PLCs.

`pip install pycomm3` · installs (wheel) · licence: MIT License · rank 10779 · last release 2025-12-22 · [PyPI](https://pypi.org/project/pycomm3/)

<details><summary>README extract</summary>

⚠️ NOTE: `pycomm3` is no longer actively developed

`pycomm3` started as a Python 3 fork of pycomm, which is a Python 2 library for
communicating with Allen-Bradley PLCs using Ethernet/IP. The initial Python 3 port was done
in this fork and was used as the base for `pycomm3`. ...

Example:
```python
from pycomm3 import LogixDriver

with LogixDriver('10.20.30.100/1') as plc:
    print(plc)
    # OUTPUT:
    # Program Name: PLCA, Device: 1756-L83E/B, Revision: 28.13

    print(plc.info)
    # OUTPUT:
    # {'vendor': 'Rockwell Automation/Allen-Bradley', 'product_type': 'Programmable Logic Controller',
...
```

Sections: pycomm3, Introduction, Drivers, Disclaimer, Setup, Documentation, Highlighted Features, LogixDriver, LogixDriver Overview, Reading/Writing Tags, User Tests

</details>

## Also in this topic

- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [webrtcvad-wheels](scientific-engineering-artificial-intelligence.md#webrtcvad-wheels) - Python interface to the Google WebRTC Voice Activity Detector (VAD) [released with binary wheels!]
- [webrtcvad](scientific-engineering-artificial-intelligence.md#webrtcvad) - Python interface to the Google WebRTC Voice Activity Detector (VAD)
- [phidget22](scientific-engineering.md#phidget22) - Phidget22 Python Library
- [pyglove](scientific-engineering-artificial-intelligence.md#pyglove) - PyGlove: A library for manipulating Python objects.
- [pyrealsense2](multimedia-video.md#pyrealsense2) - Python Wrapper for Realsense SDK 2.0.
- [Kivy](artistic-software.md#kivy) - An open-source Python framework for developing GUI apps that work cross-platform, including desktop, mobile and embedded platforms.
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [nemo-safe-synthesizer](scientific-engineering-artificial-intelligence.md#nemo-safe-synthesizer) - Safe synthesizer
- [langfun](scientific-engineering-artificial-intelligence.md#langfun) - Langfun: Language as Functions.
- [pytextrank](scientific-engineering-artificial-intelligence.md#pytextrank) - Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
