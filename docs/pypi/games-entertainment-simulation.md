# Games/Entertainment / Simulation

[Index](README.md) · 3 packages in this topic, 1 more listed under another topic, by downloads.

### pybullet

Official Python Interface for the Bullet Physics SDK specialized for Robotics Simulation and Reinforcement Learning

`pip install pybullet` · installs from source (sdist only) · licence: zlib/libpng License · rank 6887 · last release 2025-01-30 · [PyPI](https://pypi.org/project/pybullet/)

<details><summary>README extract</summary>

pybullet is an easy to use Python module for physics simulation, robotics and deep reinforcement learning based on the Bullet Physics SDK. With pybullet you can load articulated bodies from URDF, SDF and other file formats. ...

</details>

### taichi

The Taichi Programming Language

`pip install taichi` · does not install on CPython 3.14 · licence: Apache Software License · rank 8978 · last release 2025-07-31 · [PyPI](https://pypi.org/project/taichi/)

<details><summary>README extract</summary>

Taichi Lang is an open-source, imperative, parallel programming language for high-performance numerical computation. It is embedded in Python and uses just-in-time (JIT) compiler frameworks, for example LLVM, to offload the compute-intensive Python code to the native GPU or CPU instructions. ...

Features:
- Built around Python: Taichi Lang shares almost the same syntax with Python, allowing you to write algorithms with minimal language barrier. It is also well integrated into the Python ecosystem, including NumPy and PyTorch. ...

Example:
```python
# python/taichi/examples/simulation/fractal.py

import taichi as ti

ti.init(arch=ti.gpu)

n = 320
pixels = ti.field(dtype=float, shape=(n * 2, n))

@ti.func
def complex_sqr(z):
    return ti.Vector([z[0]2 - z[1]2, z[1] * z[0] * 2])

...

</details>

### quadrants

The Quadrants Programming Language

`pip install quadrants` · installs (wheel) · licence: Apache-2.0 · rank 9309 · last release 2026-11-04 · [PyPI](https://pypi.org/project/quadrants/)

<details><summary>README extract</summary>

Quadrants is a high-performance multi-platform compiler for physics simulation being continuously developed by Genesis AI.

It is designed for large-scale physics simulation and robotics workloads. It compiles Python code into highly optimized parallel kernels that run on: ...

Sections: What is Quadrants?, The origin, How Quadrants differs from upstream Taichi, CI, Structural improvements, Removed components, Performance, SIMT primitives, Autodiff, Prerequisites, Procedure, Documentation, Something is broken!

</details>

## Also in this topic

- [sapien](education.md#sapien) - ['SAPIEN: A SimulAted Parted based Interactive ENvironment']
