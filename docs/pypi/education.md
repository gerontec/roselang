# Education

[Index](README.md) · 36 packages in this topic, 7 more listed under another topic, by downloads.

### cuda-python

CUDA Python: Performance meets Productivity

`pip install cuda-python` · installs (wheel) · licence: Apache-2.0 · rank 1800 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cuda-python/) · [docs](https://nvidia.github.io/cuda-python/) · [source](https://github.com/NVIDIA/cuda-python/)

<details><summary>README extract</summary>

CUDA Python is the home for accessing NVIDIA's CUDA platform from Python. It consists of multiple components:

* cuda.core: Pythonic access to CUDA Runtime and other core functionality
* cuda.bindings: Low-level Python bindings to CUDA C APIs
* cuda.pathfinder: Utilities for locating CUDA components installed in the user's Python environment
* ...

Sections: cuda-python as a metapackage, Subpackage: cuda.core, Subpackage: cuda.bindings

</details>

### cuda-core

cuda.core: pythonic CUDA module

`pip install cuda-core` · installs (wheel) · licence: Apache-2.0 · rank 1816 · last release 2026-10-16 · [PyPI](https://pypi.org/project/cuda-core/) · [docs](https://nvidia.github.io/cuda-python/cuda-core/) · [source](https://github.com/NVIDIA/cuda-python/tree/main/cuda_core)

<details><summary>README extract</summary>

cuda.core bridges Python's productivity with CUDA's performance through intuitive and pythonic APIs. The mission is to provide users full access to all of the core CUDA features in Python, such as runtime control, compiler and linker.

* Repository
* Documentation
* Examples
* Issue tracker

`cuda.core` is currently under active development. ...

</details>

### googletrans

An unofficial Google Translate API for Python

`pip install googletrans` · installs (wheel) · licence: MIT License · rank 2619 · last release 2025-01-01 · [PyPI](https://pypi.org/project/googletrans/)

<details><summary>README extract</summary>

Googletrans is a free and unlimited python library that
implemented Google Translate API. This uses the Google Translate Ajax
API to make calls to such methods as
detect and translate.

Compatible with Python 3.8+.

For details refer to the API
Documentation.

Features:
- Fast and reliable - it uses the same servers that
 translate.google.com uses
- Auto language detection
- Bulk translations
- Customizable service URL
- Async support
- HTTP/2 support
- Proxy support
- Complete type hints

Example:
```python
>>> import asyncio
>>> from googletrans import Translator
>>>
>>> async def translate_text():
...     async with Translator() as translator:
...         result = await translator.translate('안녕하세요.')
...

</details>

### uncertainties

calculations with values with uncertainties, error propagation

`pip install uncertainties` · installs (wheel) · licence: BSD License · rank 2676 · last release 2025-04-21 · [PyPI](https://pypi.org/project/uncertainties/) · [docs](https://uncertainties.readthedocs.io/) · [source](https://github.com/lmfit/uncertainties)

<details><summary>README extract</summary>

The `uncertainties` package allows calculations with values that have
uncertaintes, such as (2 +/- 0.1)*2 = 4 +/- 0.2. `uncertainties` takes the
pain and complexity out of error propagation and calculations of values with
uncertainties. For more information, see

Example:
```python
>>> from uncertainties import ufloat
>>> x = ufloat(2, 0.25)
>>> x
2.0+/-0.25

>>> square = x**2
>>> square
4.0+/-1.0
>>> square.nominal_value
4.0
>>> square.std_dev  # Standard deviation
1.0

>>> square - x*x
0.0  # Exactly 0: correlations taken into account

>>> from uncertainties.umath import sin, cos  # and many more.
>>> sin(1+x**2)
...
```

Sections: uncertainties, Basic examples, Main features, Git branches

</details>

### nccl4py

NCCL4Py: Python bindings for NCCL

`pip install nccl4py` · installs (wheel) · licence: Apache-2.0 · rank 2771 · last release 2026-09-23 · [PyPI](https://pypi.org/project/nccl4py/) · [docs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html) · [source](https://github.com/NVIDIA/nccl)

<details><summary>README extract</summary>

nccl4py bridges Python's simplicity with the performance of NVIDIA Collective Communications Library (NCCL), and provides a Pythonic interface to NCCL library's functionality. It enables Python applications to leverage NCCL's GPU-accelerated multi-GPU and multi-node communication capabilities for distributed computing workloads. ...

</details>

### open3d

Open3D: A Modern Library for 3D Data Processing.

`pip install open3d` · installs (wheel) · licence: MIT License · rank 2889 · last release 2026-09-16 · [PyPI](https://pypi.org/project/open3d/) · [docs](https://www.open3d.org/docs) · [source](https://github.com/isl-org/Open3D)

<details><summary>README extract</summary>

Open3D is an open-source library that supports rapid development of software
that deals with 3D data. The Open3D frontend exposes a set of carefully selected
data structures and algorithms in both C++ and Python. The backend is highly
optimized and is set up for parallelization. We welcome contributions from the
open-source community. ...

Sections: About This Project, Core features, Resources

</details>

### lap

Linear Assignment Problem solver (LAPJV/LAPMOD).

`pip install lap` · installs (wheel) · licence: BSD-2-Clause · rank 4048 · last release 2026-11-03 · [PyPI](https://pypi.org/project/lap/)

<details><summary>README extract</summary>

`lap` is a linear assignment
problem solver using
Jonker-Volgenant algorithm for dense LAPJV¹ or sparse LAPMOD² matrices. Both
algorithms are implemented from scratch based solely on the papers¹˒² and the
public domain Pascal implementation provided by A. Volgenant³. ...

Example:
```python
import lap
import numpy as np
print(lap.lapjv(np.random.rand(4, 5), extend_cost=True))
```

Sections: lap: Linear Assignment Problem Solver, 🧪 Usage, `cost, x, y = lap.lapjv(C)`

</details>

### sigfig

Python library for rounding numbers (with expected results)

`pip install sigfig` · installs (wheel) · licence: MIT · rank 4443 · last release 2026-09-18 · [PyPI](https://pypi.org/project/sigfig/) · [docs](https://sigfig.readthedocs.io/) · [source](https://github.com/drakegroup/sigfig.git)

<details><summary>README extract</summary>

This is the sigfig Python package used for rounding numbers (with expected results).

Key Features:

* round numbers by significant figures/digits
* round numbers by decimal places
* round numbers by uncertainty/error
* format numbers in a variety of common styles & notations

In-depth documentation can be found here: ...

Example:
```python
>>> round(0.25, 1)
0.2
>>> from sigfig import round
>>> round(0.25, decimals=1)
0.3
>>> round(3.14159, sigfigs=2)
3.1
>>> round(3.14159, uncertainty=0.003639)
'3.142 ± 0.004'
>>> round('3.141592653589793', '0.00000002567', format='Drake')
'3.141 592 654(26)'
```

</details>

### coacd

Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search

`pip install coacd` · installs (wheel) · licence: MIT License · rank 4616 · last release 2026-08-28 · [PyPI](https://pypi.org/project/coacd/)

### codetiming

A flexible, customizable timer for your Python code.

`pip install codetiming` · installs (wheel) · licence: MIT License · rank 5272 · last release 2022-11-08 · [PyPI](https://pypi.org/project/codetiming/) · [source](https://github.com/realpython/codetiming)

<details><summary>README extract</summary>

Install `codetiming` from PyPI:

The source code is available on GitHub.

For a complete tutorial on `codetiming`, see Python Timer Functions: Three Ways to Monitor Your Code on Real Python.

Example:
```python
t = Timer(name="class")
t.start()
# Do something
t.stop()
```

Sections: Basic Usage, Arguments, Capturing the Elapsed Time, Named Timers

</details>

### btsocket

Python library for BlueZ Bluetooth Management API

`pip install btsocket` · installs (wheel) · licence: MIT License · rank 5289 · last release 2024-06-10 · [PyPI](https://pypi.org/project/btsocket/)

<details><summary>README extract</summary>

A Python library to interact with Bluez Bluetooth Management API on Linux.
At this time it should be seen as a very early stage proof of concept.
If you are new to Bluetooth this might not be the best library to start with

Features:
This library aims to offer assistance to accessing the BlueZ Bluetooth
Management API
using Python.
With the `mgmt` API there are no commands for reading and writing data on a
connected device. ...

Example:
```python
from btsocket import btmgmt_sync
response = btmgmt_sync.send('SetPowered', 0, 1)
```

Sections: BlueZ Bluetooth Management API, Overview, Three Levels, Socket (How), Programming Paradigm (When), Commands, Callbacks on Events

</details>

### quantities

Support for physical quantities with units, based on numpy

`pip install quantities` · installs (wheel) · licence: not stated · rank 5907 · last release 2026-01-16 · [PyPI](https://pypi.org/project/quantities/) · [docs](http://python-quantities.readthedocs.io/) · [source](https://github.com/python-quantities/python-quantities)

<details><summary>README extract</summary>

Quantities is designed to handle arithmetic and
conversions of physical quantities, which have a magnitude, dimensionality
specified by various units, and possibly an uncertainty. See the tutorial
for examples. Quantities builds on the popular numpy library and is
designed to work with numpy ufuncs, many of which are already
supported. ...

Example:
```python
>>> import quantities as pq
>>> distance = 42*pq.metre
>>> time = 17*pq.second
>>> velocity = distance / time
>>> "%.3f %s" % (velocity.magnitude, velocity.dimensionality)
'2.471 m/s'
>>> velocity + 3
Traceback (most recent call last):
  ...
ValueError: Unable to convert between units of "dimensionless" and "m/s"
```

Sections: quantities, Download, Documentation and usage, Tests

</details>

### lapx

Linear assignment problem solvers, including single and batch solvers.

`pip install lapx` · installs (wheel) · licence: MIT · rank 6185 · last release 2026-10-29 · [PyPI](https://pypi.org/project/lapx/)

<details><summary>README extract</summary>

🆕 What's new

> - 2026/10/29: v0.13.0 improved performance on rectangular inputs for native R/H families.

> - 2026/10/27: v0.12.0 improved performance on congested rectangular inputs for native R/H families.

> - 2026/10/19: v0.11.0rc1 added the Rust and hybrid solvers: `lapjvr`, `lapjvh`, `lapjvr_batch`, and `lapjvh_batch`. ...

Example:
```python
import lap
import numpy as np

cost = np.random.rand(100, 150)
total, x, y = lap.lapjv(cost, extend_cost=True)
valid = x >= 0
pairs = np.column_stack((np.arange(len(x))[valid], x[valid]))
```

...

</details>

### translate

This is a simple, yet powerful command line translator with google translate behind it. You can also use it as a Python module in your code.

`pip install translate` · installs (wheel) · licence: MIT License · rank 6280 · last release 2026-07-06 · [PyPI](https://pypi.org/project/translate/)

<details><summary>README extract</summary>

Translate is a simple but powerful translation tool written in python with with support for
multiple translation providers. By now we offer integration with Microsoft Translation API,
Translated MyMemory API, LibreTranslate, DeepL's free and pro APIs, and Yandex Translate API

Features:
The biggest reason to use translate is to make translations in a simple way without the need of bigger
effort and can be used as a translation tool like command line

Example:
```python
In [1]: from translate import Translator
In [2]: translator = Translator(to_lang="zh")
In [3]: translation = translator.translate("This is a pen.")
Out [3]: 这是一支笔
```

...

</details>

### fluids

Fluid dynamics component of Chemical Engineering Design Library (ChEDL)

`pip install fluids` · installs (wheel) · licence: MIT · rank 6296 · last release 2026-06-23 · [PyPI](https://pypi.org/project/fluids/)

<details><summary>README extract</summary>

Fluids is open-source software for engineers and technicians working in the
fields of chemical, mechanical, or civil engineering. It includes modules
for piping, fittings, pumps, tanks, compressible flow, open-channel flow,
atmospheric properties, solar properties, particle size distributions,
two phase flow, friction factors, control valves, ...

Sections: fluids, What is Fluids?, Documentation, Latest source code, Bug reports

</details>

### noisereduce

Noise reduction using Spectral Gating in Python

`pip install noisereduce` · installs (wheel) · licence: BSD License · rank 6803 · last release 2024-10-06 · [PyPI](https://pypi.org/project/noisereduce/)

<details><summary>README extract</summary>

Noisereduce is a noise reduction algorithm in python that reduces noise in time-domain signals like speech, bioacoustics, and physiological signals. It relies on a method called "spectral gating" which is a form of Noise Gate. ...

Example:
```python
from scipy.io import wavfile
import noisereduce as nr
# load data
rate, data = wavfile.read("mywav.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)
```

...

</details>

### gpiozero

A simple interface to GPIO devices with Raspberry Pi

`pip install gpiozero` · installs (wheel) · licence: BSD-3-Clause · rank 7076 · last release 2026-07-27 · [PyPI](https://pypi.org/project/gpiozero/) · [docs](https://gpiozero.readthedocs.io/) · [source](https://github.com/gpiozero/gpiozero)

<details><summary>README extract</summary>

A simple interface to GPIO devices with Raspberry Pi, developed and
maintained by Ben Nuttall and Dave Jones.

Component interfaces are provided to allow a frictionless way to get started
with physical computing:

With very little code, you can quickly get going connecting your components
together: ...

Example:
```python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Sections: gpiozero, About, Pin factories, Documentation, Issues and questions

</details>

### pyteomics

A framework for proteomics data analysis.

`pip install pyteomics` · installs (wheel) · licence: Apache-2.0 · rank 7100 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pyteomics/) · [docs](http://pyteomics.readthedocs.io) · [source](https://github.com/levitsky/pyteomics)

<details><summary>README extract</summary>

Pyteomics is a collection of lightweight and handy tools for Python that help
to handle various sorts of proteomics data. Pyteomics provides a growing set of
modules to facilitate the most common tasks in proteomics data analysis, such as:

* calculation of basic physico-chemical properties of polypeptides: ...

</details>

### colorzero

Yet another Python color library

`pip install colorzero` · installs (wheel) · licence: BSD License · rank 7101 · last release 2021-03-15 · [PyPI](https://pypi.org/project/colorzero/) · [docs](https://colorzero.readthedocs.io/) · [source](https://github.com/waveform80/colorzero/)

<details><summary>README extract</summary>

colorzero is a color manipulation library for Python (yes, *another* one) which
aims to be reasonably simple to use and "pythonic" in nature.

It does *not* aim to be as comprehensive, powerful, or that matter as *correct*
as, say, colormath. ...

Example:
```python
>>> Color('red') + Color('blue')
<Color html='#ff00ff' rgb=(1, 0, 1)>
>>> Color('magenta') - Color('red')
<Color html='#0000ff' rgb=(0, 0, 1)>
>>> Color('red') - Red(0.5)
<Color html='#800000' rgb=(0.5, 0, 0)>
>>> Color('green') + Color('grey').red
<Color html='#808000' rgb=(0.501961, 0.501961, 0)>
>>> Color.from_hls(0.5, 0.5, 1.0)
...
```

Sections: colorzero, Links

</details>

### chemicals

Chemical properties component of Chemical Engineering Design Library (ChEDL)

`pip install chemicals` · installs (wheel) · licence: MIT License · rank 7528 · last release 2026-06-07 · [PyPI](https://pypi.org/project/chemicals/)

<details><summary>README extract</summary>

Features:
The chemicals library features an extensive compilation of pure component
chemical data that can serve engineers, scientists, technicians, and anyone
working with chemicals. The chemicals library facilitates the retrieval and
calculation of: ...

Example:
```python
>>> from chemicals import CAS_from_any, MW, Tb, Tm, Tc, Pc, Vc, Hfus, Hfs, Hfl, Hfg, S0s, S0l, S0g
>>> # Search for CASRN by a common name or a unique identifier such as the IchI key
>>> CAS_water = CAS_from_any('Water')
>>> MW(CAS_water)   # Molecular weight [g/mol]
18.01528
>>> Tb(CAS_water)   # Normal boiling point [K]
373.124
...
```

Sections: Chemicals, Key Features & Capabilities, Documentation, Getting Started, Roadmap, Latest source code, Bug reports

</details>

### thermo

Chemical properties component of Chemical Engineering Design Library (ChEDL)

`pip install thermo` · installs (wheel) · licence: MIT License · rank 7808 · last release 2026-07-13 · [PyPI](https://pypi.org/project/thermo/)

<details><summary>README extract</summary>

Thermo is open-source software for engineers, scientists, technicians and
anyone trying to understand the universe in more detail. It facilitates
the retrieval of constants of chemicals, the calculation of temperature
and pressure dependent chemical properties (both thermodynamic and
transport), and the calculation of the same for chemical ...

Example:
```python
>>> from thermo import ChemicalConstantsPackage, PRMIX, CEOSLiquid, CEOSGas, FlashPureVLS
>>> # Load the constant properties and correlation properties
>>> constants, correlations = ChemicalConstantsPackage.from_IDs(['decane'])
>>> # Configure the liquid and gas phase objects
...
```

...

</details>

### latex2sympy2

Convert latex to sympy with ANTLR and support Matrix, Linear Algebra and CAS functions.

`pip install latex2sympy2` · installs (wheel) · licence: MIT License · rank 8088 · last release 2023-04-23 · [PyPI](https://pypi.org/project/latex2sympy2/)

<details><summary>README extract</summary>

`latex2sympy2` parses LaTeX math expressions and converts it into the equivalent SymPy form. The latex2sympy2 is adapted from augustt198/latex2sympy and purdue-tlt / latex2sympy.

This project is a part of a VS Code extension called Latex Sympy Calculator. ...

Features:
* Arithmetic: Add (+), Sub (-), Dot Mul (·), Cross Mul (×), Frac (/), Power (^), Abs (|x|), Sqrt (√), etc...
* Alphabet: a - z, A - Z, α - ω, Subscript (x_1), Accent Bar(ā), etc... ...

Example:
```python
from latex2sympy2 import latex2sympy, latex2latex

tex = r"\frac{d}{dx}(x^{2}+x)"
# Or you can use '\mathrm{d}' to replace 'd'
latex2sympy(tex)
# => "Derivative(x**2 + x, x)"
latex2latex(tex)
# => "2 x + 1"
```

...

</details>

### pyamg

PyAMG: Algebraic Multigrid Solvers in Python

`pip install pyamg` · installs (wheel) · licence: MIT License · rank 8434 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyamg/) · [docs](https://pyamg.readthedocs.io) · [source](https://github.com/pyamg/pyamg.git)

<details><summary>README extract</summary>

Example:
```python
import pyamg
pyamg.test()
```

Sections: Introduction, Citing, Getting Help, What is AMG?, PyAMG Features, Example Usage, Conda

</details>

### torchreid

Torchreid-Pip: Deep learning person re-identification in PyTorch.

`pip install torchreid` · installs from source (sdist only) · licence: MIT · rank 9783 · last release 2022-10-16 · [PyPI](https://pypi.org/project/torchreid/)

<details><summary>README extract</summary>

This repo is a packaged version of the Torchreid algorithm.

Example:
```python
import torchreid
```

Sections: Torchreid-Pip: Packaged version of Torchreid, Overview, 1. Import ``torchreid``, 2. Load data manager, 3 Build model, optimizer and lr_scheduler, 4. Build engine, 5. Run training and test

</details>

### clip-interrogator

Generate a prompt from an image

`pip install clip-interrogator` · installs (wheel) · licence: MIT License · rank 10309 · last release 2023-03-20 · [PyPI](https://pypi.org/project/clip-interrogator/)

<details><summary>README extract</summary>

*Want to figure out what a good prompt might be to create new images like an existing one? The CLIP Interrogator is here to get you answers!*

🆕 Now available as a Stable Diffusion Web UI Extension! 🆕

Run Version 2 on Colab, HuggingFace, and Replicate!

Version 1 still available in Colab for comparing different CLIP models ...

Example:
```python
from PIL import Image
from clip_interrogator import Config, Interrogator
image = Image.open(image_path).convert('RGB')
ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
print(ci.interrogate(image))
```

Sections: clip-interrogator, Run it!, About, Using as a library, Configuration, Ranking against your own list of terms

</details>

### sapien

['SAPIEN: A SimulAted Parted based Interactive ENvironment']

`pip install sapien` · installs (wheel) · licence: MIT License · rank 10552 · last release 2026-03-10 · [PyPI](https://pypi.org/project/sapien/) · [docs](https://sapien.ucsd.edu/docs)

<details><summary>README extract</summary>

SAPIEN is a realistic and physics-rich simulated environment that hosts a
large-scale set for articulated objects. It enables various robotic vision and
interaction tasks that require detailed part-level understanding. SAPIEN is a
collaborative effort between researchers at UCSD, Stanford and SFU. ...

Sections: SAPIEN, Getting Started, Offscreen rendering on a server, Virtual desktop on a server, Website and Documentation, Build from source, Before build, Build with Docker, Build without Docker

</details>

### blackjax

Flexible and fast sampling in Python

`pip install blackjax` · installs (wheel) · licence: Apache Software License · rank 10873 · last release 2026-10-02 · [PyPI](https://pypi.org/project/blackjax/) · [docs](https://blackjax-devs.github.io/blackjax/) · [source](https://github.com/blackjax-devs/blackjax)

<details><summary>README extract</summary>

BlackJAX is a library of samplers for JAX that
works on CPU as well as GPU.

It is *not* a probabilistic programming library. However it integrates really
well with PPLs as long as they can provide a (potentially unnormalized)
log-probability density function compatible with JAX.

BlackJAX should appeal to those who: ...

Features:
Sampling algorithms are too often integrated into PPLs and not decoupled from
the rest of the framework, making them hard to use for people who do not need
the modeling language to build their logpdf. ...

Example:
```python
import jax
import jax.numpy as jnp
import jax.scipy.stats as stats
import numpy as np

import blackjax

observed = np.random.normal(10, 20, size=1_000)
def logdensity_fn(x):
    logpdf = stats.norm.logpdf(observed, x["loc"], x["scale"])
...

</details>

### sumy

Module for automatic summarization of text documents and HTML pages.

`pip install sumy` · installs (wheel) · licence: Apache Software License · rank 10901 · last release 2026-08-12 · [PyPI](https://pypi.org/project/sumy/) · [source](https://github.com/miso-belica/sumy)

<details><summary>README extract</summary>

Simple library and command line utility for extracting summary from HTML
pages or plain texts. The package also contains simple evaluation
framework for text summaries. Implemented summarization methods are described in the documentation. I also maintain a list of alternative implementations of the summarizers in various programming languages.

Example:
```python
# -*- coding: utf-8 -*-

from future import absolute_import
from future import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
...
```

...

</details>

### rubric

rubric

`pip install rubric` · installs (wheel) · licence: MIT · rank 11629 · last release 2026-01-21 · [PyPI](https://pypi.org/project/rubric/) · [source](https://github.com/The-LLM-Data-Company/rubric)

<details><summary>README extract</summary>

Example:
```python
import asyncio
from rubric import Rubric, default_per_criterion_generate_fn
from rubric.autograders import PerCriterionGrader

async def main():
    rubric = Rubric.from_dict([
        {"weight": 10.0, "requirement": "Response mentions Paris"},
        {"weight": 5.0, "requirement": "Response is concise"}
    ])

...
```

Sections: Usage, Quick Start with Default Generate Functions, Custom Generate Function with OpenAI, Autograder Strategies, PerCriterionGrader, PerCriterionOneShotGrader, RubricAsJudgeGrader, Default System Prompts, Customization, Error Handling, Score Fields, The `normalize` Parameter, Loading Rubrics, JSON Format

</details>

### nbtoolbelt

Tools to work with Jupyter notebooks

`pip install nbtoolbelt` · does not install on CPython 3.14 · licence: MIT License · rank 11937 · last release 2026-05-01 · [PyPI](https://pypi.org/project/nbtoolbelt/) · [docs](https://nbtoolbelt.readthedocs.io/) · [source](https://gitlab.tue.nl/jupyter-projects/nbtoolbelt/)

<details><summary>README extract</summary>

* `validate`: validate notebooks
* `head`: show head or tail of notebooks
* `dump`: dump notebook info and source on terminal
* `stats`: summarize notebooks with statistics
* `view`: view notebook, including all embedded images, LaTeX, and HTML in a browser
* `cat`: concatenate multiple notebooks
* `clean`: clean notebooks by removing specified ...

Sections: nbtoolbelt - Tools to Work with Jupyter Notebooks, Documentation, Usage, Resources

</details>

### pyDOE3

Design of experiments for Python

`pip install pyDOE3` · installs (wheel) · licence: BSD-3-Clause · rank 12296 · last release 2026-01-12 · [PyPI](https://pypi.org/project/pyDOE3/) · [source](https://github.com/relf/pyDOE3)

<details><summary>README extract</summary>

This package is designed to help the scientist, engineer, statistician, etc., to
construct appropriate experimental designs.

Capabilities

The package currently includes functions for creating designs for any
number of factors: ...

</details>

### googletrans-py

Free Google Translate API for Python. Translates totally free of charge.

`pip install googletrans-py` · installs from source (sdist only) · licence: Freeware · rank 12369 · last release 2022-04-13 · [PyPI](https://pypi.org/project/googletrans-py/)

<details><summary>README extract</summary>

This is a fork of the googletrans which makes the original package compatible with the latest versions of `httpx`, `httpcore` and their dependencies. This compatibility makes it possible to use `httpx`'s newer versions than `0.13.3`.

The base is taken from the feature/rpc branch of googletrans which was the last version, including pre-releases. ...

Sections: googletrans-py, PyPI, Repository

</details>

### ht

Heat transfer component of Chemical Engineering Design Library (ChEDL)

`pip install ht` · installs (wheel) · licence: MIT · rank 12755 · last release 2025-10-26 · [PyPI](https://pypi.org/project/ht/)

<details><summary>README extract</summary>

ht is open-source software for engineers and technicians working in the
fields of chemical or mechanical engineering. It includes modules
for various heat transfer functions.

Among the tasks this library can be used for are: ...

Sections: Heat Transfer (ht), What is ht?, Documentation, Latest source code, Bug reports

</details>

### mplib

A lightweight motion planning library

`pip install mplib` · installs from source (sdist only) · licence: MIT License · rank 13232 · last release 2024-08-17 · [PyPI](https://pypi.org/project/mplib/)

<details><summary>README extract</summary>

MPlib is a lightweight python package for motion planning,
which is decoupled from ROS and is easy to set up.
With a few lines of python code, one can achieve most of the motion planning
functionalities in robot manipulation.

Sections: MPlib: a Lightweight Motion Planning Library, Usage

</details>

### pybboxes

Light Weight Toolkit for Bounding Boxes

`pip install pybboxes` · installs (wheel) · licence: MIT · rank 13616 · last release 2024-10-07 · [PyPI](https://pypi.org/project/pybboxes/)

<details><summary>README extract</summary>

Light weight toolkit for bounding boxes providing conversion between bounding box types and simple computations. Supported bounding box types (italicized text indicates normalized values):

- albumentations : Albumentations Format
 - _[x-tl, y-tl, x-br, y-br]_ (Normalized VOC Format) Top-left coordinates & Bottom-right coordinates ...

Example:
```python
from pybboxes import BoundingBox

my_coco_box = [98, 345, 322, 117]
coco_bbox = BoundingBox.from_coco(*my_coco_box)  # <[98 345 322 117] (322x117) | Image: (?x?)>
# or alternatively
# coco_bbox = BoundingBox.from_array(my_coco_box)
```

...

</details>

### open3d-cpu

Open3D: A Modern Library for 3D Data Processing.

`pip install open3d-cpu` · installs (wheel) · licence: MIT License · rank 14691 · last release 2026-09-28 · [PyPI](https://pypi.org/project/open3d-cpu/) · [docs](https://www.open3d.org/docs) · [source](https://github.com/isl-org/Open3D)

<details><summary>README extract</summary>

Open3D is an open-source library that supports rapid development of software
that deals with 3D data. The Open3D frontend exposes a set of carefully selected
data structures and algorithms in both C++ and Python. The backend is highly
optimized and is set up for parallelization. We welcome contributions from the
open-source community. ...

Sections: About This Project, Core features, Resources

</details>

## Also in this topic

- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [deep-translator](communications.md#deep-translator) - A flexible free and unlimited python tool to translate between different languages in a simple way using multiple translators
- [imgui-bundle](artistic-software.md#imgui-bundle) - Dear ImGui for Python and C++, batteries included: real-time GUIs, plots and live data, on the desktop and in the browser, with no server.
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [stftpitchshift](artistic-software.md#stftpitchshift) - STFT based pitch and timbre shifting
