# Desktop Environment / K Desktop Environment (KDE)

[Index](README.md) · 1 packages in this topic, 1 more listed under another topic, by downloads.

### pyprof2calltree

Help visualize profiling data from cProfile with kcachegrind and qcachegrind

`pip install pyprof2calltree` · installs from source (sdist only) · licence: MIT License · rank 11578 · last release 2020-04-19 · [PyPI](https://pypi.org/project/pyprof2calltree/)

<details><summary>README extract</summary>

Features:
Script to help visualize profiling data collected with the cProfile
Python module with the kcachegrind (screenshots) graphical calltree
analyser.

This is a rebranding of the venerable
 script by David Allouche
et Al. ...

Example:
```python
>>> from xml.etree import ElementTree
>>> from cProfile import Profile
>>> xml_content = '\n' + '\ttext\n' * 100 + ''
>>> profiler = Profile()
>>> profiler.runctx(
...     "ElementTree.fromstring(xml_content)",
...     locals(), globals())

>>> from pyprof2calltree import convert, visualize
...
```

Sections: Overview, Command line usage, Python shell usage

</details>

## Also in this topic

- [desktop-notifier](communications.md#desktop-notifier) - Python library for cross-platform desktop notifications
