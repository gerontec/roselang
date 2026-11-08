# Unclassified / J

[Index](README.md) · 152 packages in this topic, by downloads.

### jmespath

JSON Matching Expressions

`pip install jmespath` · installs (wheel) · licence: MIT License · rank 50 · last release 2026-01-22 · [PyPI](https://pypi.org/project/jmespath/)

<details><summary>README extract</summary>

JMESPath (pronounced "james path") allows you to declaratively specify how to
extract elements from a JSON document.

For example, given this document:
The jmespath expression `foo.bar` will return "baz".

JMESPath also supports:

Referencing elements in a list. Given the data:
The expression: `foo.bar[0]` will return "one". ...

Example:
```python
>>> import jmespath
>>> path = jmespath.search('foo.bar', {'foo': {'bar': 'baz'}})
'baz'
```

Sections: JMESPath, API, Options, Custom Functions, Specification, Discuss

</details>

### jaraco.classes

Utility functions for Python class constructs

`pip install jaraco.classes` · installs (wheel) · licence: MIT License · rank 212 · last release 2024-03-31 · [PyPI](https://pypi.org/project/jaraco.classes/)

<details><summary>README extract</summary>

Available as part of the Tidelift Subscription.

This project and the maintainers of thousands of other packages are working with Tidelift to deliver one enterprise subscription that covers all of the open source you use.

Learn more.

</details>

### jaraco.functools

Functools like those found in stdlib

`pip install jaraco.functools` · installs (wheel) · licence: MIT · rank 214 · last release 2026-07-14 · [PyPI](https://pypi.org/project/jaraco.functools/) · [source](https://github.com/jaraco/jaraco.functools)

<details><summary>README extract</summary>

Additional functools in the spirit of stdlib's functools.

Available as part of the Tidelift Subscription.

This project and the maintainers of thousands of other packages are working with Tidelift to deliver one enterprise subscription that covers all of the open source you use.

Learn more.

</details>

### jaraco.context

Useful decorators and context managers

`pip install jaraco.context` · installs (wheel) · licence: MIT · rank 223 · last release 2026-03-20 · [PyPI](https://pypi.org/project/jaraco.context/) · [source](https://github.com/jaraco/jaraco.context)

<details><summary>README extract</summary>

Features:
See the docs linked from the badge above for the full details, but here are some features that may be of interest.

- `ExceptionTrap` provides a general-purpose wrapper for trapping exceptions and then acting on the outcome. ...

Sections: Highlights, For Enterprise

</details>

### jupyter-core

Jupyter core package. A base package on which Jupyter projects rely.

`pip install jupyter-core` · installs (wheel) · licence: BSD-3-Clause · rank 300 · last release 2025-10-16 · [PyPI](https://pypi.org/project/jupyter-core/) · [docs](https://jupyter-core.readthedocs.io/) · [source](https://github.com/jupyter/jupyter_core)

<details><summary>README extract</summary>

Jupyter core package. A base package on which Jupyter projects rely.

</details>

### jupyter-client

Jupyter protocol implementation and client libraries

`pip install jupyter-client` · installs (wheel) · licence: BSD License · rank 323 · last release 2026-08-28 · [PyPI](https://pypi.org/project/jupyter-client/) · [docs](https://jupyter-client.readthedocs.io/) · [source](https://github.com/jupyter/jupyter_client)

<details><summary>README extract</summary>

`jupyter_client` contains the reference implementation of the [Jupyter protocol].
It also provides client and kernel management APIs for working with kernels.

It also provides the `jupyter kernelspec` entrypoint
for installing kernelspecs for use with Jupyter frontends.

Sections: Jupyter Client, Coding, Documentation, Our Copyright Policy

</details>

### jsonref

jsonref is a library for automatic dereferencing of JSON Reference objects for Python.

`pip install jsonref` · installs (wheel) · licence: MIT · rank 338 · last release 2023-01-16 · [PyPI](https://pypi.org/project/jsonref/) · [docs](https://jsonref.readthedocs.io/en/latest/) · [source](https://github.com/gazpachoking/jsonref)

<details><summary>README extract</summary>

`jsonref` is a library for automatic dereferencing of JSON
Reference
objects for Python (supporting Python 3.7+).

This library lets you use a data structure with JSON reference objects,
as if the references had been replaced with the referent data.

Features:
- References are evaluated lazily. Nothing is dereferenced until it is
 used.
- Recursive references are supported, and create recursive python data
 structures. ...

Sections: jsonref, Features

</details>

### jsonpath-ng

A final implementation of JSONPath for Python that aims to be standard compliant, including arithmetic and binary comparison operators and providing clear AST for metaprogramming.

`pip install jsonpath-ng` · installs (wheel) · licence: Apache-2.0 · rank 414 · last release 2026-11-04 · [PyPI](https://pypi.org/project/jsonpath-ng/) · [docs](https://jsonpath-ng.readthedocs.io/en/latest/) · [source](https://github.com/jsonpath-ng/jsonpath-ng)

<details><summary>README extract</summary>

An implementation of JSONPath for Python that aims to be standards compliant,
as defined in RFC 9535.

This packages merges both jsonpath-rw and jsonpath-rw-ext and
provides several AST API enhancements, such as the ability to update or remove nodes in the tree. ...

Example:
```python
>>> from jsonpath_ng import jsonpath, parse

# A robust parser, not just a regex. (Makes powerful extensions possible; see below)
>>> jsonpath_expr = parse('foo[*].baz')

# Extracting values is easy
>>> [match.value for match in jsonpath_expr.find({'foo': [{'baz': 1}, {'baz': 2}]})]
[1, 2]

# Matches remember where they came from
...
```

...

</details>

### jupyterlab-pygments

Pygments theme using JupyterLab CSS variables

`pip install jupyterlab-pygments` · installs (wheel) · licence: BSD License · rank 419 · last release 2023-11-23 · [PyPI](https://pypi.org/project/jupyterlab-pygments/) · [source](https://github.com/jupyterlab/jupyterlab_pygments.git)

<details><summary>README extract</summary>

This package contains a syntax coloring theme for pygments making use of
the JupyterLab CSS variables.

The goal is to enable the use of JupyterLab's themes with pygments-generated HTML.

In the following screencast, we demonstrate how Pygments-highlighted code can make use of the JupyterLab theme.

Sections: JupyterLab Pygments Theme, Screencast, Dependencies, Limitations

</details>

### json5

A Python implementation of the JSON5 data format.

`pip install json5` · installs (wheel) · licence: Apache-2.0 · rank 465 · last release 2026-10-09 · [PyPI](https://pypi.org/project/json5/) · [source](https://github.com/dpranke/pyjson5)

<details><summary>README extract</summary>

A Python implementation of the JSON5 data format.

JSON5 extends the
JSON data interchange format to make it
slightly more usable as a configuration language:

* JavaScript-style comments (both single and multi-line) are legal.

* Object keys may be unquoted if they are legal ECMAScript identifiers ...

Sections: pyjson5, Known issues, On Mac, On other platforms, Creating a venv, Run tests and other checks, Releasing a new version

</details>

### jupyter-server

The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.

`pip install jupyter-server` · installs (wheel) · licence: BSD License · rank 558 · last release 2026-09-15 · [PyPI](https://pypi.org/project/jupyter-server/) · [docs](https://jupyter-server.readthedocs.io) · [source](https://github.com/jupyter-server/jupyter_server)

<details><summary>README extract</summary>

The Jupyter Server provides the backend (i.e. the core services, APIs, and REST endpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, and Voilà.

For more information, read our documentation here.

Sections: Jupyter Server, Versioning and Branches, Usage - Running Jupyter Server, Team Meetings and Roadmap, Our Copyright Policy

</details>

### json-repair

A package to repair broken json strings

`pip install json-repair` · installs (wheel) · licence: MIT · rank 560 · last release 2026-11-06 · [PyPI](https://pypi.org/project/json-repair/)

<details><summary>README extract</summary>

English | 中文

Repair malformed JSON from LLMs, APIs, logs, and user input in Python.

- Fix missing quotes, commas, brackets, comments, stray prose, and truncated values.
- Use it as a drop-in fallback for `json.loads()` or as a schema-guided repair step.
- Install with `pip install json-repair` or try the live demo.

Example:
```python
import json_repair

bad_json = '{"users":[{"name":"Ada","role":"admin",}],"ok":true'
decoded_object = json_repair.loads(bad_json)

# {'users': [{'name': 'Ada', 'role': 'admin'}], 'ok': True}
```

...

</details>

### jupyterlab-widgets

Jupyter interactive widgets for JupyterLab

`pip install jupyterlab-widgets` · installs (wheel) · licence: BSD License · rank 566 · last release 2026-08-18 · [PyPI](https://pypi.org/project/jupyterlab-widgets/)

<details><summary>README extract</summary>

A JupyterLab extension for Jupyter/IPython widgets.

Sections: Jupyter Widgets JupyterLab Extension, Version compatibility

</details>

### jupyterlab

JupyterLab computational environment

`pip install jupyterlab` · installs (wheel) · licence: BSD License · rank 602 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jupyterlab/) · [docs](https://jupyterlab.readthedocs.io) · [source](https://github.com/jupyterlab/jupyterlab)

<details><summary>README extract</summary>

Installation |
Documentation |
Contributing |
License |
Team |
Getting help |

An extensible environment for interactive and reproducible computing, based on the
Jupyter Notebook and Architecture. ...

Features:
We also welcome suggestions for new features as they help make the project more useful for everyone. To request a feature please use the feature request template.

Sections: JupyterLab, Getting started, Running, Getting help, Bug report, Feature request, Extending JupyterLab, Team, Weekly Dev Meeting

</details>

### jupyter-events

Jupyter Event System library

`pip install jupyter-events` · installs (wheel) · licence: BSD License · rank 604 · last release 2026-04-20 · [PyPI](https://pypi.org/project/jupyter-events/) · [docs](https://jupyter-events.readthedocs.io/) · [source](https://github.com/jupyter/jupyter_events.git)

<details><summary>README extract</summary>

_An event system for Jupyter Applications and extensions._

Jupyter Events enables Jupyter Python Applications (e.g. Jupyter Server, JupyterLab Server, JupyterHub, etc.) to emit events—structured data describing things happening inside the application. Other software (e.g. ...

Sections: Jupyter Events, Documentation, Our Copyright Policy

</details>

### jupyter-server-terminals

A Jupyter Server Extension Providing Terminals.

`pip install jupyter-server-terminals` · installs (wheel) · licence: BSD License · rank 609 · last release 2026-01-14 · [PyPI](https://pypi.org/project/jupyter-server-terminals/) · [docs](https://jupyter-server-terminals.readthedocs.io) · [source](https://github.com/jupyter-server/jupyter_server_terminals)

<details><summary>README extract</summary>

Jupyter Server Terminals is a Jupyter Server Extension providing support for terminals.

Sections: Jupyter Server Terminals, Our Copyright Policy

</details>

### jupyterlab-server

A set of server components for JupyterLab and JupyterLab like applications.

`pip install jupyterlab-server` · installs (wheel) · licence: BSD License · rank 624 · last release 2026-09-15 · [PyPI](https://pypi.org/project/jupyterlab-server/) · [docs](https://jupyterlab-server.readthedocs.io) · [source](https://github.com/jupyterlab/jupyterlab_server)

<details><summary>README extract</summary>

JupyterLab Server sits between JupyterLab and Jupyter Server, and provides a
set of REST API handlers and utilities that are used by JupyterLab. It is a separate project in order to
accommodate creating JupyterLab-like applications from a more limited scope.

Sections: jupyterlab server, Motivation, Usage, Extending the Application

</details>

### jupyter-lsp

Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server

`pip install jupyter-lsp` · installs (wheel) · licence: BSD License · rank 645 · last release 2026-04-02 · [PyPI](https://pypi.org/project/jupyter-lsp/) · [docs](https://jupyterlab-lsp.readthedocs.io/) · [source](https://github.com/jupyter-lsp/jupyterlab-lsp)

<details><summary>README extract</summary>

Multi-Language Server WebSocket proxy for your Jupyter
`notebook` or `lab` server. For Python 3.6+.

> See the parent of this repository,
> jupyterlab-lsp for the
> reference client implementation for JupyterLab.

`jupyter-lsp` does not come with any Language Servers! Learn more about installing
and configuring language servers

Sections: jupyter-lsp, Language Servers

</details>

### jupyter-builder

JupyterLab build tools

`pip install jupyter-builder` · installs (wheel) · licence: Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT · rank 800 · last release 2026-10-27 · [PyPI](https://pypi.org/project/jupyter-builder/) · [source](https://github.com/jupyterlab/jupyter-builder)

<details><summary>README extract</summary>

Build tools for JupyterLab extensions — extracted from the core JupyterLab codebase to be maintained and used independently.

Example:
```python
from jupyter_builder.federated_extensions import (
    build_labextension,
    develop_labextension_py,
    watch_labextension,
)

build_labextension(
    "/path/to/extension",
    development=False,
    source_map=False,
    static_url=None,
    core_version=None,
    core_package_file=None,
)

develop_labextension_py(
    "/path/to/extension",
...
```

Sections: Jupyter Builder, CLI, `build`, `watch`, `jlpm`, Advanced, CLI flags, Python API, Environment variables

</details>

### jsonpickle

jsonpickle encodes/decodes any Python object to/from JSON

`pip install jsonpickle` · installs (wheel) · licence: BSD-3-Clause · rank 986 · last release 2026-10-15 · [PyPI](https://pypi.org/project/jsonpickle/) · [docs](https://jsonpickle.readthedocs.io/) · [source](https://github.com/jsonpickle/jsonpickle)

<details><summary>README extract</summary>

jsonpickle is a library for the two-way conversion of complex Python objects
and JSON. jsonpickle builds upon existing JSON
encoders, such as simplejson, json, and ujson.

For complete documentation, please visit the
jsonpickle documentation.

Bug reports and merge requests are encouraged at the
jsonpickle repository on github.

Features:
Data serialized with python's pickle (or cPickle or dill) is not easily readable outside of python. Using the json format, jsonpickle allows simple data types to be stored in a human-readable format, and more complex data types such as numpy arrays ...

Example:
```python
import jsonpickle
from dataclasses import dataclass

@dataclass
class Example:
    data: str

ex = Example("value1")
encoded_instance = jsonpickle.encode(ex)
...

</details>

### jupyter-console

Jupyter terminal console

`pip install jupyter-console` · installs (wheel) · licence: BSD License · rank 1003 · last release 2023-03-06 · [PyPI](https://pypi.org/project/jupyter-console/)

<details><summary>README extract</summary>

A terminal-based console frontend for Jupyter kernels.
This code is based on the single-process IPython terminal.

Install with pip:

 pip install jupyter-console

Install with conda:

 conda install -c conda-forge jupyter_console

Start:

 jupyter console

Help:

 jupyter console -h ...

Sections: Jupyter Console, Resources, Our Copyright Policy

</details>

### jupyter

Jupyter metapackage. Install all the Jupyter components in one go.

`pip install jupyter` · installs (wheel) · licence: BSD License · rank 1016 · last release 2024-08-30 · [PyPI](https://pypi.org/project/jupyter/)

### jax

Differentiate, compile, and transform Numpy code.

`pip install jax` · installs (wheel) · licence: Apache-2.0 · rank 1153 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jax/)

<details><summary>README extract</summary>

Transformations
| Scaling
| Install guide
| Change logs
| Reference docs

JAX is a Python library for accelerator-oriented array computation and program transformation,
designed for high-performance numerical computing and large-scale machine learning.

JAX can automatically differentiate native
Python and NumPy functions. ...

Example:
```python
import jax
import jax.numpy as jnp

def predict(params, inputs):
  for W, b in params:
    outputs = jnp.dot(inputs, W) + b
    inputs = jnp.tanh(outputs)  # inputs to the next layer
  return outputs                # no activation on last layer

def loss(params, inputs, targets):
  preds = predict(params, inputs)
...
```

...

</details>

### jaxlib

XLA library for JAX

`pip install jaxlib` · installs (wheel) · licence: Apache-2.0 · rank 1171 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jaxlib/)

### jellyfish

(no summary)

`pip install jellyfish` · installs (wheel) · licence: MIT License · rank 1184 · last release 2026-10-16 · [PyPI](https://pypi.org/project/jellyfish/) · [docs](https://jpt.sh/projects/jellyfish/) · [source](https://codeberg.org/jpt/jellyfish/)

### jsondiff

Diff JSON and JSON-like structures in Python

`pip install jsondiff` · installs (wheel) · licence: MIT License · rank 1560 · last release 2024-08-29 · [PyPI](https://pypi.org/project/jsondiff/)

<details><summary>README extract</summary>

Diff JSON and JSON-like structures in Python.

Example:
```python
>>> import jsondiff as jd
>>> from jsondiff import diff

>>> diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
{'c': 4, 'b': 3, delete: ['a']}

>>> diff(['a', 'b', 'c'], ['a', 'b', 'c', 'd'])
{insert: [(3, 'd')]}

>>> diff(['a', 'b', 'c'], ['a', 'c'])
{delete: [1]}

# Typical diff looks like what you'd expect...
...
```

Sections: jsondiff, Quickstart, Command Line Client

</details>

### jsbeautifier

JavaScript unobfuscator and beautifier.

`pip install jsbeautifier` · installs (wheel) · licence: MIT · rank 1600 · last release 2026-06-30 · [PyPI](https://pypi.org/project/jsbeautifier/)

<details><summary>README extract</summary>

Beautify, unpack or deobfuscate JavaScript. Handles popular online obfuscators.

</details>

### jinja2-humanize-extension

a jinja2 extension to use humanize library inside jinja2 templates

`pip install jinja2-humanize-extension` · installs (wheel) · licence: BSD License · rank 1603 · last release 2023-09-01 · [PyPI](https://pypi.org/project/jinja2-humanize-extension/)

<details><summary>README extract</summary>

Status (master branch)

This is a jinja2 extension to use humanize library inside jinja2 templates.

The generic syntax is `{{ 'VALUE'|humanize{humanize_fn}([humanize_fn_args]) }}`.

Following humanize functions are currently mapped:

- `naturalsize`
- `abs_timedelta` (deprecated with humanize >= 4.0, we keep it for compatibility) ...

Example:
```python
from jinja2 import Template, Environment

# We load the extension in a jinja2 Environment
env = Environment(extensions=["jinja2_humanize_extension.HumanizeExtension"])

template = env.from_string("The file size is : {{ 30000000|humanize_naturalsize() }}")
result = template.render()

# [...]
```

Sections: jinja2_humanize_extension, What is it ?, Syntax, Full example

</details>

### jq

jq is a lightweight and flexible JSON processor.

`pip install jq` · installs (wheel) · licence: BSD-2-Clause · rank 1650 · last release 2026-10-18 · [PyPI](https://pypi.org/project/jq/)

<details><summary>README extract</summary>

This project contains Python bindings for
jq 1.8.2.

Example:
```python
import jq

assert jq.compile(".+5").input_value(42).first() == 47
```

Sections: jq.py: a lightweight and flexible JSON processor, Debian, Ubuntu or relatives, Red Hat, Fedora, CentOS or relatives, Mac OS X, Usage, . Call `jq.compile()` to compile a jq program., Input methods, Output methods, Arguments, Convenience functions, Original program string

</details>

### json-merge-patch

JSON Merge Patch library (https://tools.ietf.org/html/rfc7386)

`pip install json-merge-patch` · installs (wheel) · licence: BSD · rank 2067 · last release 2025-03-25 · [PyPI](https://pypi.org/project/json-merge-patch/)

### jiwer

Evaluate your speech-to-text system with similarity measures such as word error rate (WER)

`pip install jiwer` · installs (wheel) · licence: Apache-2.0 · rank 2221 · last release 2025-06-19 · [PyPI](https://pypi.org/project/jiwer/)

<details><summary>README extract</summary>

JiWER is a simple and fast python package to evaluate an automatic speech recognition system.
It supports the following measures:

1. word error rate (WER)
2. match error rate (MER)
3. word information lost (WIL)
4. word information preserved (WIP)
5. character error rate (CER) ...

Example:
```python
from jiwer import wer

reference = "hello world"
hypothesis = "hello duck"

error = wer(reference, hypothesis)
```

Sections: JiWER, Documentation, Usage, A note on empty references, Reference

</details>

### jinja2-ansible-filters

A port of Ansible's jinja2 filters without requiring ansible core.

`pip install jinja2-ansible-filters` · installs (wheel) · licence: GPL3 · rank 2998 · last release 2022-06-30 · [PyPI](https://pypi.org/project/jinja2-ansible-filters/)

_README extract left out: share-alike licence._

### jcs

JCS - JSON Canonicalization

`pip install jcs` · installs (wheel) · licence: Apache-2.0 · rank 3127 · last release 2026-11-06 · [PyPI](https://pypi.org/project/jcs/) · [source](https://github.com/titusz/jcs)

<details><summary>README extract</summary>

This is a Python 3 package for a JCS (RFC 8785)
compliant JSON canonicalization.

The main author of this code is Anders Rundgren. The original
source code is at
cyberphone/json-canonicalization
including comprehensive test data.

Example:
```python
import jcs
data = jcs.canonicalize({"tag": 4})
```

Sections: JCS - JSON Canonicalization for Python 3, Using JCS, Numbers, Releasing

</details>

### jaraco.text

Module for text manipulation

`pip install jaraco.text` · installs (wheel) · licence: MIT · rank 3151 · last release 2026-07-12 · [PyPI](https://pypi.org/project/jaraco.text/) · [source](https://github.com/jaraco/jaraco.text)

<details><summary>README extract</summary>

This package provides handy routines for dealing with text, such as
wrapping, substitution, trimming, stripping, prefix and suffix removal,
line continuation, indentation, comment processing, identifier processing,
values parsing, case insensitive comparison, and more. ...

Sections: Layouts, Newline Reporting, For Enterprise

</details>

### jsonargparse

Minimal effort CLIs derived from type hints and parse from command line, config files and environment variables.

`pip install jsonargparse` · installs (wheel) · licence: MIT · rank 3277 · last release 2026-10-23 · [PyPI](https://pypi.org/project/jsonargparse/) · [source](https://github.com/mauvilsa/jsonargparse)

<details><summary>README extract</summary>

`jsonargparse` is a library for creating command-line interfaces (CLIs) and
making Python apps easily configurable. It is a well-maintained project with
frequent releases, adhering to high standards of development: semantic
versioning, deprecation periods, changelog, automated testing, and full test
coverage. ...

Features:
`jsonargparse` is user-friendly and encourages the development of **clean,
high-quality code**. It encompasses numerous powerful features, some unique to
`jsonargparse`, while also combining advantages found in similar packages: ...

Example:
```python
from jsonargparse import auto_cli

def main_function(...):  # your main parameters with type hints here
    ...  # your main code here

if name == "main":
...

</details>

### jsonalias

A microlibrary that defines a Json type alias for Python.

`pip install jsonalias` · installs (wheel) · licence: MIT License · rank 3362 · last release 2022-10-30 · [PyPI](https://pypi.org/project/jsonalias/)

<details><summary>README extract</summary>

A microlibrary that defines a `Json` type alias for Python.

Seriously, this is all the code:

If we only supported Python >= 3.10, it would fit on one line:

Example:
```python
from jsonalias import Json

d: Json = {"foo": ["bar", {"x": "y"}]}
```

Sections: jsonalias, This README is longer than the library, Then why make a library out of it?, Example, It's not working please help???, Special Thanks

</details>

### jsonpath-rw

A robust and significantly extended implementation of JSONPath for Python, with a clear AST for metaprogramming.

`pip install jsonpath-rw` · installs from source (sdist only) · licence: Apache Software License · rank 3642 · last release 2015-04-19 · [PyPI](https://pypi.org/project/jsonpath-rw/)

<details><summary>README extract</summary>

This library provides a robust and significantly extended implementation
of JSONPath for Python. It is tested with Python 2.6, 2.7, 3.2, 3.3.
*(On travis-ci there is a segfault when running the tests with pypy; I don't think the problem lies with this library)*. ...

Example:
```python
$ python

>>> from jsonpath_rw import jsonpath, parse

# A robust parser, not just a regex. (Makes powerful extensions possible; see below)
>>> jsonpath_expr = parse('foo[*].baz')

# Extracting values is easy
>>> [match.value for match in jsonpath_expr.find({'foo': [{'baz': 1}, {'baz': 2}]})]
[1, 2]

# Matches remember where they came from
...
```

Sections: Python JSONPath RW, Quick Start, JSONPath Syntax, Programmatic JSONPath, Extensions, More to explore, Special note about PLY and docstrings

</details>

### jsonata-python

Pure Python implementation of JSONata

`pip install jsonata-python` · installs (wheel) · licence: Apache Software License · rank 3815 · last release 2026-10-10 · [PyPI](https://pypi.org/project/jsonata-python/)

<details><summary>README extract</summary>

[][github-actions-link]

Pure Python implementation of JSONata.

This is a Python port of the JSONata reference implementation,
and also borrows from the Dashjoin Java port.

This implementation supports 100% of the language features of JSONata, with no external dependencies.
The JSONata documentation can be found here.

Example:
```python
>>> import jsonata
>>> data = {"example": [{"value": 4}, {"value": 7}, {"value": 13}]}
>>> expr = jsonata.Jsonata("$sum(example.value)")
>>> result = expr.evaluate(data)
>>> result
24
```

Sections: jsonata-python, Getting Started, Command Line Interface, Examples, Guardrails, Running Tests, Notes

</details>

### json-stream-rs-tokenizer

A faster tokenizer for the json-stream Python library

`pip install json-stream-rs-tokenizer` · installs (wheel) · licence: not stated · rank 3852 · last release 2026-10-20 · [PyPI](https://pypi.org/project/json-stream-rs-tokenizer/) · [source](https://github.com/smheidrich/py-json-stream-rs-tokenizer)

<details><summary>README extract</summary>

> NOTE: `json-stream-rs-tokenizer` is now automatically used by
> `json-stream`, so unless you find a bug, you can ignore this package's
> existence!

A faster tokenizer for the json-stream
Python library. ...

Example:
```python
from io import StringIO
from json_stream import load
from json_stream_rs_tokenizer import RustTokenizer

json_buf = StringIO('{ "a": [1,2,3,4], "b": [5,6,7] }')

# uses the Rust tokenizer to load JSON:
d = load(json_buf, tokenizer=RustTokenizer)

for k, l in d.items():
  print(f"{k}: {' '.join(str(n) for n in l)}")
```

Sections: json-stream-rs-tokenizer, Implicit, Explicit, Usage, Limitations, Benchmarks, Tests

</details>

### johnnydep

Display dependency tree of Python distribution

`pip install johnnydep` · installs (wheel) · licence: MIT · rank 3867 · last release 2026-10-20 · [PyPI](https://pypi.org/project/johnnydep/)

<details><summary>README extract</summary>

Pretty-print a dependency tree for a Python distribution. A simple example:

 $ johnnydep requests
 name summary
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 requests Python HTTP for Humans. ...

</details>

### jsonnet

Python bindings for Jsonnet - The data templating language

`pip install jsonnet` · installs (wheel) · licence: Apache-2.0 · rank 3987 · last release 2026-03-24 · [PyPI](https://pypi.org/project/jsonnet/) · [source](https://github.com/google/jsonnet)

<details><summary>README extract</summary>

For an introduction to Jsonnet and documentation,
visit our website.

This is the Python module for the original C++ implementation of Jsonnet.

Security notes: The C++ implementation is not suitable for processing *untrusted inputs* without significant external effort to sandbox it. It is not hardened and may have unknown exploitable bugs. ...

Example:
```python
import _jsonnet

FILES = {
    "the_message.txt": b"hello, world",
}

def import_callback_memfile(dir, rel):
    """Custom import function which only returns files from some in-memory storage.

    Args:
      dir: The directory part of the file in which the `import` occurred.
      rel: The path string passed to the `import` expression.
    """
...
```

...

</details>

### jinja_partials

Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks.

`pip install jinja_partials` · installs (wheel) · licence: MIT · rank 4005 · last release 2026-11-07 · [PyPI](https://pypi.org/project/jinja_partials/) · [docs](https://mkennedy.codes/docs/jinja-partials/) · [source](https://github.com/mikeckennedy/jinja_partials)

<details><summary>README extract</summary>

Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks.
(There is also a Pyramid/Chameleon version here.)

Features:
Every Jinja2 app of a certain age has a fragment that got copied. A video card, a badge, a table row. It started life on one page, got pasted onto a second, then a third, and by the time the designer asks for a small refresh there are fourteen of ...

Example:
```python
import flask
import jinja_partials

app = flask.Flask(name)
jinja_partials.register_extensions(app)
```

Sections: Jinja Partials, Overview, Documentation, Examples, Usage, Flask, FastAPI, Starlette, Quart, One rule for async apps, Direct Jinja2 Environment, Using the Jinja2 Extension (Declarative), For Flask Applications, For Standalone Jinja2 Environments

</details>

### json2html

JSON to HTML Table Representation

`pip install json2html` · installs from source (sdist only) · licence: MIT · rank 4178 · last release 2019-07-03 · [PyPI](https://pypi.org/project/json2html/)

<details><summary>README extract</summary>

Python wrapper to convert `JSON` into a human readable `HTML Table` representation.

Features:
* User friendly tablular fomat, easy to read and share.
* If value of the key is array of objects and all the keys are same(value of the key is a dict of list), the module will club by default. Eg. ...

Example:
```python
from json2html import *
input = {
    "name": "json2html",
    "description": "Converts JSON to HTML tabular representation"
}
json2html.convert(json = input)
```

Sections: json2html, Features, Live Demo, List of valid arguments, Example Usage, Tests

</details>

### junit2html

Generate HTML reports from Junit results

`pip install junit2html` · installs (wheel) · licence: License :: OSI Approved :: MIT License · rank 4182 · last release 2026-06-11 · [PyPI](https://pypi.org/project/junit2html/)

<details><summary>README extract</summary>

Generate a single file HTML report from a Junit or XUnit XML results file

</details>

### jstyleson

Library to parse JSON with js-style comments.

`pip install jstyleson` · installs from source (sdist only) · licence: MIT License · rank 4261 · last release 2016-06-21 · [PyPI](https://pypi.org/project/jstyleson/)

### jinja2-cli

The CLI for Jinja2

`pip install jinja2-cli` · installs (wheel) · licence: BSD License · rank 4274 · last release 2026-04-05 · [PyPI](https://pypi.org/project/jinja2-cli/)

<details><summary>README extract</summary>

The CLI for Jinja2.

Features:
- Read data from files or stdin
- Define variables inline with `-D key=value`
- Custom Jinja2 extensions
- Import custom filters - see Custom Filters below
- Full control over Jinja2 environment options ...

Example:
```python
# myfilters.py
def reverse(s):
    return s[::-1]

def shout(s):
    return s.upper() + "!"
```

Sections: $ jinja2, Formats, Features, Custom Filters, Used by, Available in, Learn more

</details>

### jupyter-ydoc

Document structures for collaborative editing using Ypy

`pip install jupyter-ydoc` · installs (wheel) · licence: BSD 3-Clause License · rank 4480 · last release 2026-11-02 · [PyPI](https://pypi.org/project/jupyter-ydoc/) · [source](https://github.com/jupyter-server/jupyter_ydoc)

<details><summary>README extract</summary>

`jupyter_ydoc` provides pycrdt-based data structures for various
documents used in the Jupyter ecosystem. Built-in documents include:
- `YBlob`: a generic immutable binary document.
- `YUnicode`: a generic UTF8-encoded text document (`YFile` is an alias to `YUnicode`).
- `YNotebook`: a Jupyter notebook document. ...

Example:
```python
from jupyter_ydoc import ydocs

print(ydocs)
# {
# 'blob': <class 'jupyter_ydoc.yblob.YBlob'>,
# 'file': <class 'jupyter_ydoc.yfile.YFile'>,
# 'notebook': <class 'jupyter_ydoc.ynotebook.YNotebook'>,
# 'unicode': <class 'jupyter_ydoc.yunicode.YUnicode'>
# }
```

</details>

### jsonpath-rfc9535

RFC 9535 - JSONPath: Query Expressions for JSON in Python

`pip install jsonpath-rfc9535` · installs (wheel) · licence: MIT · rank 4553 · last release 2026-10-10 · [PyPI](https://pypi.org/project/jsonpath-rfc9535/) · [docs](https://jg-rp.github.io/python-jsonpath-rfc9535/) · [source](https://github.com/jg-rp/python-jsonpath-rfc9535)

<details><summary>README extract</summary>

We follow RFC 9535 strictly and test against the JSONPath Compliance Test Suite.

Table of Contents

- Install
- Links
- Example
- Related projects
- License

Example:
```python
import jsonpath_rfc9535 as jsonpath

expr = "$.users[?@.status == 'pending'].name"

data: dict[str, object] = {
    "users": [
        {"id": "usr_101", "name": "Alice", "status": "pending"},
        {"id": "usr_102", "name": "Bob", "status": "active"},
        {"id": "usr_103", "name": "Charlie", "status": "pending"},
    ],
}

...
```

Sections: RFC 9535 JSONPath: Query Expressions for JSON in Python, Links, Example, Related projects

</details>

### jupyter-server-fileid

Jupyter Server extension providing an implementation of the File ID service.

`pip install jupyter-server-fileid` · installs (wheel) · licence: BSD License · rank 4640 · last release 2026-10-13 · [PyPI](https://pypi.org/project/jupyter-server-fileid/)

<details><summary>README extract</summary>

A Jupyter Server extension providing an implementation of the File ID service.

- Jupyter Server

Sections: jupyter_server_fileid, Requirements, Troubleshoot, Running Tests, Packaging the extension

</details>

### jsonfield

A reusable Django field that allows you to store validated JSON in your model.

`pip install jsonfield` · installs (wheel) · licence: MIT · rank 4649 · last release 2025-07-04 · [PyPI](https://pypi.org/project/jsonfield/) · [source](https://github.com/rpkilby/jsonfield)

<details><summary>README extract</summary>

jsonfield is a reusable model field that allows you to store validated JSON, automatically handling
serialization to and from the database. To use, add `jsonfield.JSONField` to one of your models.

Django 3.1 introduced a native `JSONField` that supports all database backends. ...

Example:
```python
from django.db import models
from jsonfield import JSONField

class MyModel(models.Model):
    json = JSONField()
```

Sections: jsonfield, Deprecation & Migration to Django's native `JSONField`, Usage, Querying, Handling null values, Advanced Usage, Other Fields, Running the tests, Changes

</details>

### jsonmerge

Merge a series of JSON documents.

`pip install jsonmerge` · installs (wheel) · licence: MIT License · rank 4679 · last release 2023-07-19 · [PyPI](https://pypi.org/project/jsonmerge/)

<details><summary>README extract</summary>

This Python module allows you to merge a series of JSON documents into a
single one.

This problem often occurs for example when different authors fill in
different parts of a common document and you need to construct a document
that includes contributions from all the authors. ...

Example:
```python
>>> base = {
...         "foo": 1,
...         "bar": [ "one" ],
...      }

>>> head = {
...         "bar": [ "two" ],
...         "baz": "Hello, world!"
...     }
```

Sections: Merge a series of JSON documents, Merge strategies, The Merger Class, Requirements, Source, Troubleshooting

</details>

### jupyter-server-ydoc

jupyter-server extension integrating collaborative shared models.

`pip install jupyter-server-ydoc` · installs (wheel) · licence: BSD License · rank 4680 · last release 2026-09-20 · [PyPI](https://pypi.org/project/jupyter-server-ydoc/) · [docs](https://jupyterlab-realtime-collaboration.readthedocs.io/) · [source](https://github.com/jupyterlab/jupyter-collaboration)

<details><summary>README extract</summary>

jupyter-server extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

</details>

### json-e

A data-structure parameterization system written for embedding context in JSON objects

`pip install json-e` · installs (wheel) · licence: MPL2 · rank 4798 · last release 2026-08-20 · [PyPI](https://pypi.org/project/json-e/)

<details><summary>README extract</summary>

A data-structure parameterization system written for embedding context in JSON objects.

See for usage information.

</details>

### jinja2-time

Jinja2 Extension for Dates and Times

`pip install jinja2-time` · installs (wheel) · licence: MIT License · rank 4829 · last release 2016-06-08 · [PyPI](https://pypi.org/project/jinja2-time/)

<details><summary>README extract</summary>

Jinja2 Extension for Dates and Times

Example:
```python
from jinja2 import Environment

env = Environment(extensions=['jinja2_time.TimeExtension'])

# Timezone 'local', default format -> "2015-12-10"
template = env.from_string("{% now 'local' %}")

# Timezone 'utc', explicit format -> "Thu, 10 Dec 2015 15:49:01"
template = env.from_string("{% now 'utc', '%a, %d %b %Y %H:%M:%S' %}")

...
```

Sections: Jinja2 Time, Usage, Now Tag, Default Datetime Format, Time Offset, Issues

</details>

### jaraco.collections

Collection objects similar to those in stdlib by jaraco

`pip install jaraco.collections` · installs (wheel) · licence: MIT · rank 4835 · last release 2025-06-21 · [PyPI](https://pypi.org/project/jaraco.collections/) · [source](https://github.com/jaraco/jaraco.collections)

<details><summary>README extract</summary>

Models and classes to supplement the stdlib 'collections' module.

See the docs, linked above, for descriptions and usage examples.

Highlights include:

- RangeMap: A mapping that accepts a range of values for keys.
- Projection: A subset over an existing mapping.
- KeyTransformingDict: Generalized mapping with keys transformed by a function. ...

</details>

### jupyter-server-proxy

A Jupyter server extension to run additional processes and proxy to them that comes bundled JupyterLab extension to launch pre-defined processes.

`pip install jupyter-server-proxy` · installs (wheel) · licence: BSD-3-Clause · rank 4894 · last release 2026-09-21 · [PyPI](https://pypi.org/project/jupyter-server-proxy/) · [docs](https://jupyter-server-proxy.readthedocs.io) · [source](https://github.com/jupyterhub/jupyter-server-proxy)

<details><summary>README extract</summary>

Jupyter Server Proxy lets you run arbitrary external processes (such as
RStudio, Shiny Server, Syncthing, PostgreSQL, Code Server, etc)
alongside your notebook server and provide authenticated web access to
them using a path like `/rstudio` next to others like `/lab`. ...

Sections: Jupyter Server Proxy, Python package, `pip`, `conda`, Jupyter Client Extensions, Client compatibility, Disable, Server extension, Notebook Classic extension, JupyterLab extension

</details>

### jupyter-kernel-gateway

A web server for spawning and communicating with Jupyter kernels

`pip install jupyter-kernel-gateway` · installs (wheel) · licence: BSD License · rank 4997 · last release 2024-03-12 · [PyPI](https://pypi.org/project/jupyter-kernel-gateway/)

<details><summary>README extract</summary>

Features:
Jupyter Kernel Gateway is a web server that provides headless access to
Jupyter kernels. Your application communicates with the kernels remotely,
through REST calls and Websockets rather than ZeroMQ messages. ...

Sections: Jupyter Kernel Gateway, Overview, Example Uses of Kernel Gateway, Features

</details>

### jsons

For serializing Python objects to JSON (dicts) and back

`pip install jsons` · installs (wheel) · licence: MIT License · rank 5036 · last release 2022-06-09 · [PyPI](https://pypi.org/project/jsons/)

<details><summary>README extract</summary>

- *Turn Python objects into dicts or (json)strings and back*
 - *No changes required to your objects*
 - *Easily customizable and extendable*
 - *Works with dataclasses, attrs and POPOs*

ðŸ’— this lib? Leave a â˜… and tell your colleagues!

Example of a model to serialize:

Example of using jsons to serialize: ...

Example:
```python
import jsons

some_instance = jsons.load(some_dict, SomeClass)  # Deserialization
some_dict = jsons.dump(some_instance)  # Serialization
```

Sections: Usage, Documentation, Meta, Recent updates, 1.6.3, 1.6.2, 1.6.1, 1.6.0, 1.5.1, 1.5.0, 1.4.2, 1.4.1, 1.4.0, 1.3.1

</details>

### jinjanator

Command-line interface to Jinja2 for templating in shell scripts.

`pip install jinjanator` · installs (wheel) · licence: Apache-2.0 · rank 5110 · last release 2026-10-27 · [PyPI](https://pypi.org/project/jinjanator/)

<details><summary>README extract</summary>

Features:

* Jinja2 templating
* INI, YAML, JSON data sources supported
* Environment variables can be used with or without data files
* Plugins can provide additional formats, filters, tests, extensions and global
 functions (see
 jinjanator-plugins
 for details)

Example:
```python
# Simple filters file

def parentheses(message):
    """Put message in parenthesis"""
    return f"({message})"
```

Sections: jinjanator*: CLI tool for rendering Jinja2 templates, Available Plugins, Tutorial, Tutorial with environment variables, Using environment variables, CLI Reference, Options, Customization Options, Usage Examples, Data Formats, dotenv, Usage, INI

</details>

### jinjanator-plugins

Package which provides the plugin API for the jinjanator tool

`pip install jinjanator-plugins` · installs (wheel) · licence: Apache-2.0 · rank 5142 · last release 2026-10-12 · [PyPI](https://pypi.org/project/jinjanator-plugins/)

<details><summary>README extract</summary>

jinjanator can be extended through the use of plugins; these are
Python packages installed into the same environment as the tool
itself, which use special markers to 'hook' into various
features. There is a minimal example in the
plugin_example directory which demonstrates three of
the four possible hooks. ...

Example:
```python
import codecs

from jinjanator_plugins import (
    FormatOptionUnknownError,
    FormatOptionUnsupportedError,
    FormatOptionValueError,
    plugin_filters_hook,
    plugin_formats_hook,
    plugin_identity_hook,
    plugin_tests_hook,
    plugin_extensions_hook,
)

def rot13_filter(value):
    return codecs.encode(value, "rot13")

...
```

...

</details>

### jax-cuda12-pjrt

JAX XLA PJRT Plugin for NVIDIA GPUs

`pip install jax-cuda12-pjrt` · installs (wheel) · licence: Apache-2.0 · rank 5417 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jax-cuda12-pjrt/)

### jax-cuda12-plugin

JAX Plugin for NVIDIA GPUs

`pip install jax-cuda12-plugin` · installs (wheel) · licence: Apache-2.0 · rank 5456 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jax-cuda12-plugin/)

### json-ref-dict

Python dict-like object which abstracts resolution of JSONSchema references

`pip install json-ref-dict` · installs (wheel) · licence: MIT · rank 5531 · last release 2023-08-06 · [PyPI](https://pypi.org/project/json-ref-dict/)

<details><summary>README extract</summary>

Python dict-like object which abstracts resolution of JSONSchema references.

Nested items containing `"$ref"` will be resolved lazily when accessed,
meaning the dictionary can be treating as a single, continuous (and
possibly infinite) document.

Remote references are supported, and will be resolved relative to the current
document. ...

Example:
```python
from json_ref_dict import RefDict

schema = RefDict("
```

Sections: JSONSchema Ref Dict, Example, _master.yaml, _other.yaml, Materializing documents, Requirements

</details>

### jupyter-packaging

Jupyter Packaging Utilities.

`pip install jupyter-packaging` · installs (wheel) · licence: BSD License · rank 5597 · last release 2022-08-25 · [PyPI](https://pypi.org/project/jupyter-packaging/) · [source](https://github.com/jupyter/jupyter-packaging/)

<details><summary>README extract</summary>

Tools to help build and install Jupyter Python packages that require a pre-build step that may include JavaScript build steps.

Example:
```python
from setuptools import setup

try:
    from jupyter_packaging import wrap_installers, npm_builder
    builder = npm_builder()
    cmdclass = wrap_installers(pre_develop=builder, pre_dist=builder)
except ImportError:
    cmdclass = {}

setup(cmdclass=cmdclass))
```

Sections: Jupyter Packaging, Usage, As a Build Requirement, As a Build Backend, As a Vendored File, Usage Notes

</details>

### json-delta

A diff/patch pair for JSON-serialized data structures.

`pip install json-delta` · installs (wheel) · licence: BSD License · rank 5628 · last release 2020-10-18 · [PyPI](https://pypi.org/project/json-delta/)

<details><summary>README extract</summary>

json-delta: A diff/patch pair and library for JSON data
structures. (

JSON-delta is a multi-language software suite for computing deltas
between JSON-serialized data structures, and applying those deltas as
patches. It enables separate programs at either end of a
communications channel (e.g. ...

</details>

### jamo

A Hangul syllable and jamo analyzer.

`pip install jamo` · installs (wheel) · licence: Apache Software License · rank 5631 · last release 2017-11-06 · [PyPI](https://pypi.org/project/jamo/)

<details><summary>README extract</summary>

Python-jamo is a Python Hangul syllable decomposition and synthesis library
for working with Hangul characters and jamo.

Currently in beta release, function names are subject to change, but there is
coverage for nearly all Hangul-related codepoints under Unicode 7.0. ...

Sections: Jamo: Hangul Character Analysis, Documentation

</details>

### jinjasql

Generate SQL Queries and Corresponding Bind Parameters using a Jinja2 Template

`pip install jinjasql` · installs (wheel) · licence: MIT License · rank 5638 · last release 2020-05-27 · [PyPI](https://pypi.org/project/jinjasql/)

<details><summary>README extract</summary>

Generate SQL Queries using a Jinja Template, without worrying about SQL Injection

JinjaSQL automatically binds parameters that are inserted into the template.
After JinjaSQL evaluates the template, you get 1) Query with placeholders
for parameters, and 2) List of values that need to be bound to the query. ...

</details>

### jax-cuda13-pjrt

JAX XLA PJRT Plugin for NVIDIA GPUs

`pip install jax-cuda13-pjrt` · installs (wheel) · licence: Apache-2.0 · rank 5713 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jax-cuda13-pjrt/)

### jax-cuda13-plugin

JAX Plugin for NVIDIA GPUs

`pip install jax-cuda13-plugin` · installs (wheel) · licence: Apache-2.0 · rank 5732 · last release 2026-10-21 · [PyPI](https://pypi.org/project/jax-cuda13-plugin/)

### Js2Py

JavaScript to Python Translator & JavaScript interpreter written in 100% pure Python.

`pip install Js2Py` · installs (wheel) · licence: MIT · rank 5773 · last release 2022-11-06 · [PyPI](https://pypi.org/project/Js2Py/)

<details><summary>README extract</summary>

Translates JavaScript to Python code. Js2Py is able to translate and execute virtually any JavaScript code.

Js2Py is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python.

 import js2py

 f = js2py.eval_js( "function $(name) {return name.length}" )

 f("Hello world") ...

</details>

### jupyter-dash

Dash support for the Jupyter notebook interface

`pip install jupyter-dash` · installs (wheel) · licence: MIT · rank 5792 · last release 2022-04-01 · [PyPI](https://pypi.org/project/jupyter-dash/) · [source](https://github.com/plotly/jupyter-dash)

<details><summary>README extract</summary>

This library makes it easy to develop Plotly Dash apps interactively from within Jupyter environments (e.g. classic Notebook, JupyterLab, Visual Studio Code notebooks, nteract, PyCharm notebooks, etc.).

See the notebooks/getting_started.ipynb for more information and example usage.

Features:
To learn more about the features of JupyterDash, check out the announcement post.

Sections: Jupyter Dash, Features

</details>

### jinja2-strcase

A python package for converting string case in jinja2 templates

`pip install jinja2-strcase` · installs (wheel) · licence: MIT License · rank 5915 · last release 2020-06-21 · [PyPI](https://pypi.org/project/jinja2-strcase/)

<details><summary>README extract</summary>

A python package for converting string case in jinja2 templates (including cookiecutter).

It is a port of the go package strcase

Example:
```python
from jinja2 import Environment

env = Environment(extensions=['jinja2_strcase.StrcaseExtension'])

# This will convert 'Any kind of string' -> 'any_kind_of_string'
template = env.from_string("{% 'Any kind of string' |  to_snake }")

template.render()
```

Sections: jinja2-strcase, Example

</details>

### jieba3k

Chinese Words Segementation Utilities

`pip install jieba3k` · installs from source (sdist only) · licence: UNKNOWN · rank 5930 · last release 2014-11-15 · [PyPI](https://pypi.org/project/jieba3k/)

### jsf

Creates fake JSON files from a JSON schema

`pip install jsf` · installs (wheel) · licence: MIT License · rank 6030 · last release 2024-03-26 · [PyPI](https://pypi.org/project/jsf/)

<details><summary>README extract</summary>

Use jsf along with fake data generators to provide consistent and meaningful fake data for your system.

- Provides out of the box data generation from any JSON schema 📦
- Extendable custom data providers using any lambda functions 🔗
- Multi level state for dependant data (eg multiple objects sharing value, such as children with same surname) 🤓 ...

Example:
```python
from jsf import JSF

faker = JSF(
    {
        "type": "object",
        "properties": {
            "name": {"type": "string", "$provider": "faker.name"},
            "email": {"type": "string", "$provider": "faker.email"},
        },
        "required": ["name", "email"],
    }
)

fake_json = faker.generate()
```

Sections: jsf, Main Features, Usage, Basic 😊, From JSON file 📁, Docker, FastAPI Integration 🚀

</details>

### jarowinkler

library for fast approximate string matching using Jaro and Jaro-Winkler similarity

`pip install jarowinkler` · installs (wheel) · licence: MIT License · rank 6211 · last release 2023-11-03 · [PyPI](https://pypi.org/project/jarowinkler/)

<details><summary>README extract</summary>

Example:
```python
>>> from jarowinkler import *

>>> jaro_similarity("Johnathan", "Jonathan")
0.8796296296296297

>>> jarowinkler_similarity("Johnathan", "Jonathan")
0.9037037037037037
```

Sections: JaroWinkler, zap: Quickstart, 🚀 Benchmarks, Source builds, 📖 Usage

</details>

### jdk4py

A JDK shipped in a Python package

`pip install jdk4py` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 6219 · last release 2026-04-23 · [PyPI](https://pypi.org/project/jdk4py/) · [source](https://github.com/activeviam/jdk4py)

_README extract left out: share-alike licence._

### jupyter_highlight_selected_word

Jupyter notebook extension that enables highlighting every instance of the current word in the notebook.

`pip install jupyter_highlight_selected_word` · installs (wheel) · licence: BSD · rank 6226 · last release 2018-04-07 · [PyPI](https://pypi.org/project/jupyter_highlight_selected_word/)

<details><summary>README extract</summary>

Jupyter notebook extension that enables highlighting of all instances of the
currently-selected or cursor-adjecent word in either the current cell's editor,
or in the whole notebook.
Based on the CodeMirror addon
`Match Highlighter <
extended to work across multiple editors.

</details>

### jurigged

Live update of Python functions

`pip install jurigged` · installs (wheel) · licence: MIT · rank 6290 · last release 2025-05-13 · [PyPI](https://pypi.org/project/jurigged/) · [source](https://github.com/breuleux/jurigged)

<details><summary>README extract</summary>

Jurigged lets you update your code while it runs. Using it is trivial:

1. `jurigged your_script.py`
2. Change some function or method with your favorite editor and save the file
3. Jurigged will hot patch the new function into the running script ...

Example:
```python
import jurigged
jurigged.watch()
```

Sections: jurigged, Command line, Develoop, Using with stdin, Troubleshooting, API, Recoders, Caveats, Customizing behavior, How it works, Comparison

</details>

### json-flatten

Python functions for flattening a JSON object to a single dictionary of pairs, and unflattening that dictionary back to a JSON object

`pip install json-flatten` · installs (wheel) · licence: Apache License, Version 2.0 · rank 6314 · last release 2024-09-07 · [PyPI](https://pypi.org/project/json-flatten/)

<details><summary>README extract</summary>

Python functions for flattening a JSON object to a single dictionary of pairs, and unflattening that dictionary back to a JSON object.

This can be useful if you need to represent a JSON object using a regular HTML form or transmit it as a set of query string parameters.

For example: ...

Example:
```python
>>> import json_flatten
>>> json_flatten.flatten({"foo": {"bar": [1, True, None]}})
{'foo.bar.[0]$int': '1', 'foo.bar.[1]$bool': 'True', 'foo.bar.[2]$none': 'None'}
>>> json_flatten.unflatten(_)
{'foo': {'bar': [1, True, None]}}
```

Sections: json-flatten, JSON flattening format, Basic principles, Nested objects, Lists, Nested lists, Type preservation, Example

</details>

### jupyterlab-nvdashboard

A JupyterLab extension for displaying GPU usage dashboards

`pip install jupyterlab-nvdashboard` · installs (wheel) · licence: BSD-3-Clause · rank 6683 · last release 2026-06-25 · [PyPI](https://pypi.org/project/jupyterlab-nvdashboard/) · [source](https://github.com/rapidsai/jupyterlab-nvdashboard.git)

<details><summary>README extract</summary>

NVDashboard is a JupyterLab extension for displaying GPU usage dashboards. It enables JupyterLab users to visualize system hardware metrics within the same interactive environment they use for development. Supported metrics include:

- GPU-compute utilization
- GPU-memory consumption
- PCIe throughput
- NVLink throughput

Sections: JupyterLab NVdashboard, Demo, New Features, Brush for Time Series Charts, Synced Tooltips, Theme Compatibility, Light Theme, Dark Theme, GPU Accelerators, Version Compatibility, Conda, PyPI, Troubleshoot

</details>

### jsonpath-rw-ext

Extensions for JSONPath RW

`pip install jsonpath-rw-ext` · installs (wheel) · licence: Apache Software License · rank 6743 · last release 2019-07-12 · [PyPI](https://pypi.org/project/jsonpath-rw-ext/)

<details><summary>README extract</summary>

Extensions for JSONPath RW

jsonpath-rw-ext extends json-path-rw capabilities by adding multiple extensions.
'len' that allows one to get the length of a list. 'sorted' that returns a sorted version
of a list, 'arithmetic' that permits one to make math operation between elements and
'filter' to select only certain elements of a list. ...

Example:
```python
import jsonpath_rw_ext
jsonpath_rw_ext.parse("$.foo").find(...)
```

Sections: python-jsonpath-rw-ext, Quick Start, Extensions, About arithmetic and string, About arithmetic and list

</details>

### jupyterhub

JupyterHub: A multi-user server for Jupyter notebooks

`pip install jupyterhub` · installs (wheel) · licence: BSD-3-Clause · rank 6768 · last release 2026-11-05 · [PyPI](https://pypi.org/project/jupyterhub/) · [docs](https://jupyterhub.readthedocs.io) · [source](https://github.com/jupyterhub/jupyterhub)

<details><summary>README extract</summary>

Technical Overview |
Installation |
Configuration |
Docker |
Contributing |
License |
Help and Resources

With JupyterHub you can create a
multi-user Hub that spawns, manages, and proxies multiple instances of the
single-user Jupyter notebook
server.

Project Jupyter created JupyterHub to support many
users. ...

Sections: JupyterHub, Technical overview, Check prerequisites, Using `conda`, Using `pip`, Run the Hub server, Configuration, Create a configuration file, Start the Hub, Authenticators, Spawners, Docker, Help and resources

</details>

### jsonseq

Python support for RFC 7464 JSON text sequences

`pip install jsonseq` · installs (wheel) · licence: MIT License · rank 6781 · last release 2019-07-31 · [PyPI](https://pypi.org/project/jsonseq/)

<details><summary>README extract</summary>

RFC 7464 JSON Text Sequences encoding and decoding for Python.

Example:
```python
>>> from jsonseq.encode import JSONSeqEncoder
>>> for chunk in JSONSeqEncoder().encode(({"a": i, "b": i} for i in range(3))):
...     print(repr(chunk))
...
'{"a": 0, "b": 0}\n'
'{"a": 1, "b": 1}\n'
'{"a": 2, "b": 2}\n'
```

Sections: jsonseq, Usage

</details>

### jalali-core

a Gregorian to Jalali and inverse date convertor

`pip install jalali-core` · installs (wheel) · licence: LGPL · rank 6944 · last release 2024-03-25 · [PyPI](https://pypi.org/project/jalali-core/)

_README extract left out: share-alike licence._

### jsoncompat

JSON Schema compatibility checker for evolving schemas

`pip install jsoncompat` · installs (wheel) · licence: not stated · rank 7216 · last release 2026-10-10 · [PyPI](https://pypi.org/project/jsoncompat/)

<details><summary>README extract</summary>

Python bindings for checking compatibility of evolving JSON Schemas and generating example values.

Example:
```python
import jsoncompat as jsc

old_schema = '{"type": "string"}'
new_schema = '{"type": "number"}'

is_compatible = jsc.check_compat(old_schema, new_schema, jsc.Role.BOTH)
print(is_compatible)

# Generate example values for a schema
generator = jsc.generator_for(old_schema)
example = generator.generate_value(depth=5)
print(example)
```

Sections: jsoncompat, Quick start, API, Generated model artifacts, OpenAPI model packages, Offline resources and format policy, More detail, Benchmarks

</details>

### japanize-matplotlib

matplotlibのフォント設定を自動で日本語化する

`pip install japanize-matplotlib` · installs from source (sdist only) · licence: MIT License · rank 7219 · last release 2020-10-21 · [PyPI](https://pypi.org/project/japanize-matplotlib/)

<details><summary>README extract</summary>

matplotlib を日本語表示に対応させます

matplotlibをimportした後、japanize_matplotlibをimportします。

Example:
```python
import matplotlib.pyplot as plt
import japanize_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()
```

Sections: japanize-matplotlib, 利用方法, インストール, 利用フォント, FAQ, import japanize_matplotlib したのに日本語表示になりません #1, import のみして利用されないコードなのでフォーマッターに消されてしまいます

</details>

### jsonslicer

Stream JSON parser with iterator interface

`pip install jsonslicer` · installs from source (sdist only) · licence: MIT License · rank 7337 · last release 2022-10-25 · [PyPI](https://pypi.org/project/jsonslicer/)

<details><summary>README extract</summary>

Features:
JsonSlicer performs a stream or iterative, pull JSON
parsing, which means it does not load whole JSON into memory
and is able to parse very large JSON files or streams. ...

Example:
```python
from jsonslicer import JsonSlicer

# Extract specific elements:
with open('people.json') as data:
    ivans_age = next(JsonSlicer(data, ('friends', 1, 'age')))
    # 26

with open('people.json') as data:
    managers_name = next(JsonSlicer(data, ('colleagues', 'manager', 'name')))
    # 'Jack'

...
```

Sections: jsonslicer - stream JSON parser, Overview, Example, API, Performance/competitors, Requirements

</details>

### janome

Janome is a Japanese morphological analysis engine written in pure Python.

`pip install janome` · installs (wheel) · licence: Apache-2.0 · rank 7447 · last release 2026-11-07 · [PyPI](https://pypi.org/project/janome/) · [docs](https://janome.mocobeta.dev/en/) · [source](https://github.com/mocobeta/janome)

<details><summary>README extract</summary>

Janome is a Japanese morphological analysis engine written in pure Python.

General documentation:

 (English)

 (Japanese)

Python 3.11+ is required.

Sections: Janome, Requirements, Run, Copyright

</details>

### json5kit

A Roundtrip parser and CST for JSON, JSONC and JSON5.

`pip install json5kit` · installs (wheel) · licence: MIT License · rank 7460 · last release 2023-05-16 · [PyPI](https://pypi.org/project/json5kit/)

<details><summary>README extract</summary>

A Roundtrip parser and CST for JSON, JSONC and JSON5.

JSON5 is a superset of JSON, that allows trailing commas,
comments, unquoted and single-quoted object keys, and a lot more.

Currently supports parsing most JSON5 syntax, and converting it back to source.
Also supports single line `// comments`.

Example:
```python
>>> source = """
... {
...   items: [1, 2, 4],  // change this to 3
... }
... """
>>> import json5kit
>>> tree = json5kit.parse(source)
>>> print(tree.to_source())

{
  items: [1, 2, 4],  // change this to 3
}

>>> print(tree.to_json())
{"items":[1,2,4]}

>>> # Let's replace the `4` with `3` now:
...
```

Sections: json5kit, Usage

</details>

### jupyter-collaboration-ui

JupyterLab/Jupyter Notebook 7+ extension providing user interface integration for real time collaboration

`pip install jupyter-collaboration-ui` · installs (wheel) · licence: BSD License · rank 7514 · last release 2026-09-20 · [PyPI](https://pypi.org/project/jupyter-collaboration-ui/) · [docs](https://jupyterlab-realtime-collaboration.readthedocs.io/) · [source](https://github.com/jupyterlab/jupyter-collaboration)

<details><summary>README extract</summary>

JupyterLab/Jupyter Notebook 7+ extension providing user interface integration for real time collaboration.

</details>

### jupyter-docprovider

JupyterLab/Jupyter Notebook 7+ extension integrating collaborative shared models.

`pip install jupyter-docprovider` · installs (wheel) · licence: BSD License · rank 7562 · last release 2026-09-20 · [PyPI](https://pypi.org/project/jupyter-docprovider/) · [docs](https://jupyterlab-realtime-collaboration.readthedocs.io/) · [source](https://github.com/jupyterlab/jupyter-collaboration)

<details><summary>README extract</summary>

JupyterLab/Jupyter Notebook 7+ extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

</details>

### jupyter-collaboration

JupyterLab/Jupyter Notebook 7+ Real Time Collaboration extension (metapackage)

`pip install jupyter-collaboration` · installs (wheel) · licence: BSD License · rank 7728 · last release 2026-09-20 · [PyPI](https://pypi.org/project/jupyter-collaboration/) · [docs](https://jupyterlab-realtime-collaboration.readthedocs.io/) · [source](https://github.com/jupyterlab/jupyter-collaboration)

<details><summary>README extract</summary>

A meta-package for:
- jupyter-collaboration-ui
- jupyter-docprovider
- jupyter-server-ydoc

</details>

### json-spec

Implements JSON Schema, JSON Pointer and JSON Reference.

`pip install json-spec` · installs (wheel) · licence: Apache Software License; BSD License · rank 7886 · last release 2024-04-29 · [PyPI](https://pypi.org/project/json-spec/) · [docs](https://json-spec.readthedocs.org) · [source](https://github.com/johnnoone/json-spec)

<details><summary>README extract</summary>

This library implements several JSON specs, like JSON Schema,
JSON Reference and JSON Pointer:

* It works on python 3.6 and above
* It is release under the BSD license

Example:
```python
from jsonspec.pointer import extract

obj = {
    'foo': ['bar', 'baz', 'quux']
}
assert 'baz' == extract(obj, '/foo/1')
```

Sections: Json Spec, CLI Usage, Library usage

</details>

### judgeval

The open source post-building layer for Agent Behavior Monitoring.

`pip install judgeval` · installs (wheel) · licence: Apache-2.0 · rank 7905 · last release 2026-10-27 · [PyPI](https://pypi.org/project/judgeval/)

<details><summary>README extract</summary>

Detect failures, triage root causes, and ship fixes backed by production data.

Features:
Judgeval is an open-source Python SDK for agent improvement. It provides tracing and Agent judge evaluation for LLM-powered applications — so you can detect failures, understand what went wrong, and validate fixes against real production cases ...

Example:
```python
from judgeval import Tracer, wrap
from openai import OpenAI

Tracer.init(project_name="my-project")
client = wrap(OpenAI())

@Tracer.observe(span_type="tool")
def search(query: str) -> str:
    results = vector_db.search(query)
    return results

@Tracer.observe(span_type="agent")
def run_agent(question: str) -> str:
...
```

...

</details>

### jambo

Jambo - JSON Schema to Pydantic Converter

`pip install jambo` · installs (wheel) · licence: MIT · rank 7924 · last release 2026-09-22 · [PyPI](https://pypi.org/project/jambo/) · [source](https://github.com/HideyoshiNakazone/jambo.git)

<details><summary>README extract</summary>

Jambo is a Python package that automatically converts JSON Schema definitions into Pydantic models.
It's designed to streamline schema validation and enforce type safety using Pydantic's validation features.

Created to simplify the process of dynamically generating Pydantic models for AI frameworks like LangChain, CrewAI, and others.

Example:
```python
from jambo import SchemaConverter

schema = {
    "title": "Person",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name"],
}

# Old-style convenience API (kept for compatibility)
Person = SchemaConverter.build(schema)

obj = Person(name="Alice", age=30)
...
```

...

</details>

### justhtml

A pure Python HTML5 parser that just works.

`pip install justhtml` · installs (wheel) · licence: MIT License · rank 7991 · last release 2026-10-26 · [PyPI](https://pypi.org/project/justhtml/)

<details><summary>README extract</summary>

HTML from the real web is messy. It is often malformed, user supplied, scraped from unknown pages, or headed for a browser where small parsing differences can become security bugs.

JustHTML gives Python projects one small dependency for the common HTML jobs:

- parse HTML like a browser, including broken markup ...

Features:
Most Python HTML libraries optimize for one part of the problem.

`html.parser` is built in, but not HTML5-correct. BeautifulSoup is convenient, but depends heavily on the parser underneath. ...

Example:
```python
from justhtml import JustHTML

doc = JustHTML(
    "Helloalert(1) "
    "bad "
    "ok
",
    fragment=True,
)

print(doc.to_html(pretty=False))
# => Hello bad ok
```

...

</details>

### juju

Python library for Juju

`pip install juju` · installs (wheel) · licence: Apache Software License · rank 8069 · last release 2025-07-11 · [PyPI](https://pypi.org/project/juju/) · [docs](https://pythonlibjuju.readthedocs.io/en/latest/) · [source](https://github.com/juju/python-libjuju)

<details><summary>README extract</summary>

Source code:

Bug reports:

Documentation:

Supported Python versions: 3.8 through 3.13
Supported Juju versions: 3.1 through 3.6

* Asynchronous - Uses asyncio and async/await features of Python
* Websocket-level bindings are programmatically generated (indirectly) from the
 Juju golang code, ensuring full api coverage
* Provides an OO layer which ...

Example:
```python
# !/usr/bin/python3

import asyncio
import logging
import sys

from juju.model import Model

async def deploy():
    # Create a Model instance. We need to connect our Model to a Juju api
    # server before we can use it.
    model = Model()

    # Connect to the currently active Juju model
    await model.connect()

    try:
...
```

Sections: A Python library for Juju, Design Notes, Quickstart, REPL, Versioning

</details>

### java-access-bridge-wrapper

Python wrapper for the Windows Java Access Bridge

`pip install java-access-bridge-wrapper` · installs (wheel) · licence: Apache Software License · rank 8082 · last release 2025-11-23 · [PyPI](https://pypi.org/project/java-access-bridge-wrapper/) · [source](https://github.com/robocorp/java-access-bridge-wrapper.git)

<details><summary>README extract</summary>

Python wrapper around the Java Access Bridge / Windows Access Bridge.

* 64-bit Windows
* Java >= 8 (
 * If you are doing development install JDK, otherwise JRE is enough
* Python >= 3.9 (

Enable the Java Access Bridge in windows

 C:\path\to\java\bin\jabswitch -enable

Sections: Introduction, Requirements, How to use, Prerequisites, Packaging, TODO

</details>

### jsonc-parser

A lightweight, native tool for parsing .jsonc files

`pip install jsonc-parser` · installs (wheel) · licence: MIT License · rank 8156 · last release 2021-05-23 · [PyPI](https://pypi.org/project/jsonc-parser/)

<details><summary>README extract</summary>

This package is a lightweight, zero-dependency module for parsing files with .jsonc extension. (a.k.a. JSON with comments)

Sections: jsonc-parser, Usage, Functions, Exceptions

</details>

### jinja2_pluralize

Jinja2 pluralize filters.

`pip install jinja2_pluralize` · installs (wheel) · licence: BSD License · rank 8174 · last release 2015-10-09 · [PyPI](https://pypi.org/project/jinja2_pluralize/)

<details><summary>README extract</summary>

Jinja2 pluralize filters.

* Free software: BSD license

Features:
1. Simple pluralize filter based on inflect.py. For example, this renders as `geese`:

2. Django-style pluralize filter. Works as described in the Django docs. For example, this renders as `votes`:

Example:
```python
from jinja2 import Environment
from jinja2_pluralize import pluralize_dj

env = Environment()
env.filters['pluralize'] = pluralize_dj
tmpl = env.from_string('vote{{ 0|pluralize }}')
assert tmpl.render() == 'votes'
```

Sections: Jinja2 Pluralize, Features, Usage, 0.3.0 (2015-10-09), 0.2.1 (2014-07-09), 0.2.0 (2014-07-02), 0.1.0 (2014-04-25)

</details>

### jsonobject

A library for dealing with JSON as python objects

`pip install jsonobject` · installs from source (sdist only) · licence: BSD License · rank 8225 · last release 2025-02-27 · [PyPI](https://pypi.org/project/jsonobject/)

<details><summary>README extract</summary>

jsonobject is a python library for handling deeply nested JSON objects
as well-schema'd python objects.

jsonobject is made by Dimagi, where we build, use, and contribute to OSS in our mission to reduce inequity in the world.

jsonobject is inspired by and largely API compatible with
the `Document`/`DocumentSchema` portion of `couchdbkit`. ...

Example:
```python
from jsonobject import *

class User(JsonObject):
    username = StringProperty()
    name = StringProperty()
    active = BooleanProperty(default=False)
    date_joined = DateTimeProperty()
    tags = ListProperty(unicode)
```

...

</details>

### jubilant

Juju CLI wrapper, primarily for charm integration testing

`pip install jubilant` · installs (wheel) · licence: Apache Software License · rank 8226 · last release 2026-09-29 · [PyPI](https://pypi.org/project/jubilant/) · [docs](https://canonical.com/juju/docs/jubilant/) · [source](https://github.com/canonical/jubilant)

<details><summary>README extract</summary>

Jubilant is a Python library that wraps the Juju CLI, primarily for use in charm integration tests. It provides methods that map 1:1 to Juju CLI commands, but with a type-annotated, Pythonic interface.

You should consider switching to Jubilant if your integration tests currently use pytest-operator (and they probably do). ...

Example:
```python
import jubilant

juju = jubilant.Juju()
juju.deploy('snappass-test')
juju.wait(jubilant.all_active)

# Or only wait for specific applications:
juju.wait(lambda status: jubilant.all_active(status, 'snappass-test', 'another-app'))
```

Sections: Jubilant, the joyful library for driving Juju, Using Jubilant

</details>

### jupyterlab-rise

RISE: "Live" Reveal.js JupyterLab Slideshow extension.

`pip install jupyterlab-rise` · installs (wheel) · licence: BSD License · rank 8564 · last release 2024-12-31 · [PyPI](https://pypi.org/project/jupyterlab-rise/) · [source](https://github.com/jupyterlab-contrib/rise.git)

<details><summary>README extract</summary>

RISE: "Live" Reveal.js JupyterLab Slideshow extension.

- JupyterLab >= 4.1.2

Sections: jupyterlab_rise, Requirements, Usage, Troubleshoot, Integration tests, Packaging the extension

</details>

### jupyterlab-mathjax3

MathJax 3 math renderer for JupyterLab

`pip install jupyterlab-mathjax3` · installs (wheel) · licence: BSD License · rank 8578 · last release 2022-01-17 · [PyPI](https://pypi.org/project/jupyterlab-mathjax3/)

<details><summary>README extract</summary>

A JupyterLab extension for rendering math with MathJax 3.

The default LaTeX renderer in JupyterLab uses MathJax 2.
This extension substitutes the MathJax 2 renderer with the MathJax 3 renderer.

- JupyterLab >= 3.0

Sections: jupyterlab-mathjax3, Requirements

</details>

### jupyter-ui-poll

Block jupyter cell execution while interacting with widgets

`pip install jupyter-ui-poll` · installs (wheel) · licence: MIT License · rank 8758 · last release 2025-10-31 · [PyPI](https://pypi.org/project/jupyter-ui-poll/) · [docs](https://jupyter-ui-poll.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Block Jupyter cell execution while interacting with widgets.

This library is for people familiar with `ipywidgets` who want to solve the
following problem:

1. Display User Interface in Jupyter [#]_ using `ipywidgets` [#]_ or similar
2. Wait for data to be entered (this step is surprisingly non-trivial to implement)
3. ...

Example:
```python
# cell 1
ui = make_ui()
display(ui)
data = ui.wait_for_data()

# cell 2
do_things_with(data)

# cell 3.
do_more_tings()
```

Sections: jupyter-ui-poll, Technical Details

</details>

### java-manifest

Encode/decode Java's META-INF/MANIFEST.MF in Python

`pip install java-manifest` · installs (wheel) · licence: not stated · rank 8772 · last release 2020-07-22 · [PyPI](https://pypi.org/project/java-manifest/)

<details><summary>README extract</summary>

Encode/decode Java's `META-INF/MANIFEST.MF` in Python.

Example:
```python
>>> import java_manifest
>>> manifest_str = """
... Name: README-Example-1
... Long-Line: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
...  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
...
... Name: README-Example-2
... Foo: Bar
... """
>>> manifest = java_manifest.loads(manifest_str)
>>> print(manifest)
...
```

Sections: java-manifest-py, Usage, Custom Encoders/Decoders

</details>

### Js2Py-3.13

JavaScript to Python Translator & JavaScript interpreter written in 100% pure Python.

`pip install Js2Py-3.13` · installs (wheel) · licence: MIT · rank 8808 · last release 2025-02-07 · [PyPI](https://pypi.org/project/Js2Py-3.13/)

<details><summary>README extract</summary>

Translates JavaScript to Python code. Js2Py is able to translate and execute virtually any JavaScript code.

Js2Py is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python.

 import js2py

 f = js2py.eval_js( "function $(name) {return name.length}" )

 f("Hello world") ...

</details>

### janitor-rs

(no summary)

`pip install janitor-rs` · installs (wheel) · licence: MIT · rank 8889 · last release 2026-11-01 · [PyPI](https://pypi.org/project/janitor-rs/)

<details><summary>README extract</summary>

`janitor-rs` provides the Rust/PyO3 extension kernels used by
pyjanitor. It is not a
standalone command-line tool.

Sections: janitor-rs, Building, Repository layout, Further reading

</details>

### jfx-bridge

RPC bridge to/from Python2/Python3/Jython/etc

`pip install jfx-bridge` · installs (wheel) · licence: MIT License · rank 9183 · last release 2023-01-30 · [PyPI](https://pypi.org/project/jfx-bridge/)

<details><summary>README extract</summary>

Originally developed as part of

jfx_bridge is a simple, single file Python RPC bridge, designed to allow interacting from modern python3 to python2. It was built to operate in constrained interpreters, like the Jython interpreters built into more than one reverse-engineering tool, to allow you to access and interact with the data in the tool, and ...

Example:
```python
import ghidra_bridge
b = ghidra_bridge.GhidraBridge(namespace=globals())
name_list = b.remote_eval("[ f.getName() for f in currentProgram.getFunctionManager().getFunctions(True)]")
```

Sections: jfx(justfoxing) bridge, How to use, Remote eval, Remoteify and remote exec, Long-running commands, Remote imports, Optimising for performance, How it works, Design principles, Tested, TODO

</details>

### json-five

A JSON5 parser that, among other features, supports round-trip preservation of comments

`pip install json-five` · installs (wheel) · licence: Apache Software License · rank 9199 · last release 2024-06-11 · [PyPI](https://pypi.org/project/json-five/)

<details><summary>README extract</summary>

JSON5 for Python

Features:
- Supports the JSON5 spec
- Supports similar interfaces to stdlib `json` module
- Provides an API for working with abstract model representations of JSON5 documents. ...

Example:
```python
import json5
json_text = """{ // This is a JSON5 comment
"foo": "bar", /* this is a JSON5 block
comment that can span lines */
bacon: "eggs"  // unquoted Identifiers also work
}
"""
print(json5.loads(json_text))
# {"foo": "bar", "bacon": "eggs"}

with open('myfile.json5') as f:
    data = json5.load(f)
```

Sections: json-five, Key features, Usage, Custom loaders; Abstract JSON5 Models, Tokenization

</details>

### jsonquerylang

A lightweight, flexible, and expandable JSON query language

`pip install jsonquerylang` · installs (wheel) · licence: ISC License (ISCL) · rank 9218 · last release 2025-12-09 · [PyPI](https://pypi.org/project/jsonquerylang/)

<details><summary>README extract</summary>

This is a Python implementation of JSON Query, a small, flexible, and expandable JSON query language.

Try it out on the online playground: <

Example:
```python
from jsonquerylang import jsonquery
from pprint import pprint

data = {
    "friends": [
        {"name": "Chris", "age": 23, "city": "New York"},
        {"name": "Emily", "age": 19, "city": "Atlanta"},
        {"name": "Joe", "age": 32, "city": "New York"},
        {"name": "Kevin", "age": 19, "city": "Atlanta"},
...
```

Sections: jsonquery-python, Use, Syntax, API, jsonquery, compile, parse, stringify, Custom functions, Custom operators

</details>

### juliapkg

Julia version manager and package manager

`pip install juliapkg` · installs (wheel) · licence: MIT License · rank 9434 · last release 2026-10-24 · [PyPI](https://pypi.org/project/juliapkg/) · [source](http://github.com/JuliaPy/pyjuliapkg.git)

<details><summary>README extract</summary>

Do you want to use Julia in your Python script/project/package?
No problem! JuliaPkg will help you out!
- Declare the version of Julia you require in a `juliapkg.json` file.
- Add any packages you need too.
- Call `juliapkg.resolve()` et voila, your dependencies are there. ...

Sections: JuliaPkg, Declare dependencies, Functional interface, juliapkg.json, Command line interface, Using Julia, Details, Configuration, Which Julia gets used?, Adding Julia dependencies to Python packages, Offline mode, Zstandard-compressed Julia registries

</details>

### juliacall

Julia and Python in seamless harmony

`pip install juliacall` · installs (wheel) · licence: MIT License · rank 9497 · last release 2026-10-19 · [PyPI](https://pypi.org/project/juliacall/)

<details><summary>README extract</summary>

PythonCall & JuliaCall

Bringing Python® and Julia together in seamless harmony:
- Call Python code from Julia and Julia code from Python via a symmetric interface.
- Simple syntax, so the Python code looks like Python and the Julia code looks like Julia. ...

Sections: Example 1: Calling Python from Julia, Example 2: Calling Julia from Python, What about PyCall?

</details>

### jsonstreams

A JSON streaming writer

`pip install jsonstreams` · installs (wheel) · licence: MIT License · rank 9562 · last release 2021-03-16 · [PyPI](https://pypi.org/project/jsonstreams/)

<details><summary>README extract</summary>

Source code is available at github.

The code is licensed MIT. See the included LICENSE file for the exact terms.

JSONstreams is a package that attempts to making writing JSON in a streaming
format easier. ...

Example:
```python
import jsonstreams

with jsonstreams.Stream(jsonstreams.Type.OBJECT, filename='foo') as s:
    s.write('foo', 'bar')
    with s.subobject('a') as a:
        a.write('foo', 1)
        a.write('bar', 2)
    s.write('bar', 'foo')
```

Sections: JSONStreams, Description, Basic Usage

</details>

### jaeger-client

Jaeger Python OpenTracing Tracer implementation

`pip install jaeger-client` · installs from source (sdist only) · licence: Apache Software License · rank 9986 · last release 2021-09-14 · [PyPI](https://pypi.org/project/jaeger-client/)

### jax-dataclasses

Dataclasses + JAX

`pip install jax-dataclasses` · installs (wheel) · licence: MIT License · rank 10124 · last release 2025-12-19 · [PyPI](https://pypi.org/project/jax-dataclasses/)

<details><summary>README extract</summary>

<!-- vim-markdown-toc GFM -->

- Overview
- Installation
- Core interface
- Static fields
- Mutations
- Alternatives
- Misc

<!-- vim-markdown-toc -->

Features:
`jax_dataclasses` provides a simple wrapper around `dataclasses.dataclass` for use in
JAX, which enables automatic support for:

- Pytree registration. This
 allows dataclasses to be used at API boundaries in JAX. ...

Example:
```python
@jdc.jit
def f(a: jax.Array, b: jdc.Static[bool]) -> jax.Array:
  ...
```

Sections: jax_dataclasses, Overview, Core interface, Static fields, Mutations, Alternatives, Misc

</details>

### jsonata-rs

JSONata for Python — Rust port of the jsonata-java reference implementation

`pip install jsonata-rs` · installs (wheel) · licence: Apache-2.0 · rank 10183 · last release 2026-07-06 · [PyPI](https://pypi.org/project/jsonata-rs/)

<details><summary>README extract</summary>

Python bindings for the Rust port of jsonata-java.

* PyPI distribution name: `jsonata-rs` — `pip install jsonata-rs`
* Import name: `jsonata` — `import jsonata`
* Requires Python ≥ 3.11; published as a single `abi3` wheel per platform
 (Linux amd64 + arm64, macOS arm64).

Errors raise `jsonata.JsonataError` with `.code` (e.g. ...

Example:
```python
import jsonata

expr = jsonata.Jsonata("Account.Order.Product.(Price * Quantity) ~> $sum()")
expr.evaluate(data)            # evaluate against a dict / list / scalar

# variable bindings
jsonata.Jsonata("$x + 1").evaluate(None, {"x": 41})   # -> 42

# one-shot convenience
jsonata.evaluate("a + b", {"a": 2, "b": 3})           # -> 5

...
```

Sections: jsonata-rs, Type checking, Value mapping, Building

</details>

### jupyterlab-code-formatter

A JupyterLab plugin to facilitate invocation of code formatters.

`pip install jupyterlab-code-formatter` · installs (wheel) · licence: BSD License · rank 10286 · last release 2026-08-06 · [PyPI](https://pypi.org/project/jupyterlab-code-formatter/) · [source](https://github.com/jupyterlab-contrib/jupyterlab_code_formatter.git)

<details><summary>README extract</summary>

_A JupyterLab plugin to facilitate invocation of code formatters._

Documentation: Hosted on ReadTheDocs

Sections: Demo, Quick Start, Troubleshoot, Getting help

</details>

### jigsawstack

JigsawStack - The AI SDK for Python

`pip install jigsawstack` · installs (wheel) · licence: MIT License · rank 10300 · last release 2026-07-06 · [PyPI](https://pypi.org/project/jigsawstack/)

<details><summary>README extract</summary>

The JigsawStack AI SDK is a Python library that allows you to interact with powerful AI services to build AI-powered applications.

- 🧩 Powerful AI services all in one SDK
- ⌨️ Fully typed parameters and responses
- 📡 Built in Webhook support for long-running tasks
- 📦 Built in file system for easy file uploads
- 🍃 Lightweight and blazing fast ...

Example:
```python
params = {
 "url": "
 "element_prompts": ["prices"]
}
result = jigsaw.web.ai_scrape(params)
```

Sections: JigsawStack AI SDK, Learn more, All APIs, Setup, Usage, Related Projects

</details>

### jupysql-plugin

Jupyterlab extension for JupySQL

`pip install jupysql-plugin` · installs (wheel) · licence: BSD License · rank 10555 · last release 2024-09-05 · [PyPI](https://pypi.org/project/jupysql-plugin/) · [source](https://github.com/ploomber/jupysql-plugin.git.git)

<details><summary>README extract</summary>

> [!TIP]
> Deploy AI apps for free on Ploomber Cloud!

> [!NOTE]
> Code in the `main` branch is compatible with JupyterLab 4 (`0.4.x` or higher releases),
> the `jupyterlab3` branch contains code compatible with JupyterLab 3 (`0.3.x` releases). ...

Sections: jupysql-plugin, Troubleshooting setup, Adding dependencies, Releasing the extension, Configuration, Ploomber Cloud API Endpoint

</details>

### jaxlie

Matrix Lie groups in JAX

`pip install jaxlie` · installs (wheel) · licence: MIT License · rank 10637 · last release 2025-04-24 · [PyPI](https://pypi.org/project/jaxlie/)

<details><summary>README extract</summary>

[API reference ] **
[PyPI ]**

`jaxlie` is a library containing implementations of Lie groups commonly used for
rigid body transformations, targeted at computer vision &amp; robotics
applications written in JAX. Heavily inspired by the C++ library
Sophus.

We implement Lie groups as high-level (data)classes: ...

Sections: jaxlie, Misc

</details>

### jsonschema-pydantic

Convert JSON Schemas to Pydantic models

`pip install jsonschema-pydantic` · installs (wheel) · licence: not stated · rank 10719 · last release 2024-02-03 · [PyPI](https://pypi.org/project/jsonschema-pydantic/)

<details><summary>README extract</summary>

Simple transform of jsonschema to pydantic models.

Example:
```python
from jsonschema_pydantic import jsonschema_to_pydantic

jsonschema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name"],
}

pydantic_model = jsonschema_to_pydantic(jsonschema)
```

Sections: jsonschema-pydantic, Usage, Linting, Formatting, Documentation

</details>

### jupyter-archive

A JupyterLab extension to make, download and extract archive files.

`pip install jupyter-archive` · installs (wheel) · licence: BSD License · rank 10769 · last release 2026-07-30 · [PyPI](https://pypi.org/project/jupyter-archive/) · [source](https://github.com/jupyterlab-contrib/jupyter-archive.git)

<details><summary>README extract</summary>

A Jupyter extension to make, download and extract archive files.

Features:

- Download selected or current folder as an archive.
- Supported formats: 'zip', 'tar.gz', 'tar.bz2' and 'tar.xz'.
- Archiving and downloading are non-blocking for Jupyter. UI can still be used.
- Archive format can be set in the JLab settings. ...

Sections: jupyter-archive, Configuration, Requirements, Troubleshoot

</details>

### jupyter-kernel-client

(no summary)

`pip install jupyter-kernel-client` · installs (wheel) · licence: BSD License · rank 10979 · last release 2026-08-24 · [PyPI](https://pypi.org/project/jupyter-kernel-client/)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2023-2024 Datalayer, Inc.
 ~ BSD 3-Clause License

`Jupyter Kernel Client` allows you to connect to live Jupyter Kernels through HTTP and WebSocket.

A `Kernel` is the process responsible to execute the notebook code. ...

Example:
```python
import os

from platform import node
from jupyter_kernel_client import JupyterKernelClient

with JupyterKernelClient(server_url=" token="MY_TOKEN") as kernel:
    code = """import os
from platform import node
print(f"Hey {os.environ.get('USER', 'John Smith')} from {node()}.")
"""
    reply = kernel.execute(code)
    print(reply)
...
```

Sections: 🪐 > Jupyter Kernel Client, Jupyter Server Kernel, Jupyter Konsole, Running Tests, Packaging the library

</details>

### jaxellip

Some elliptic integrals in JAX

`pip install jaxellip` · installs (wheel) · licence: MIT · rank 11039 · last release 2026-07-01 · [PyPI](https://pypi.org/project/jaxellip/) · [source](https://github.com/sinaatalay/jaxellip)

<details><summary>README extract</summary>

Elliptic integrals are available in `scipy.special`, but are not implemented in `jax.scipy.special`, making them neither differentiable nor compatible with JAX’s JIT compilation. This package provides JAX-compatible implementations of several elliptic integrals from `scipy.special`: `ellipk`, `ellipkm1`, and `ellipe`. ...

Example:
```python
import jaxellip
import jax.numpy as jnp

input = jnp.linspace(-10, 10, 1000)

jaxellip.ellipk(input) # Complete elliptic integral of the first kind
jaxellip.ellipkm1(input) # Complete elliptic integral of the first kind around m = 1
jaxellip.ellipe(input) # Complete elliptic integral of the second kind
```

...

</details>

### jupyterlab-git

A JupyterLab extension for version control using git

`pip install jupyterlab-git` · installs (wheel) · licence: BSD License · rank 11181 · last release 2026-10-07 · [PyPI](https://pypi.org/project/jupyterlab-git/) · [source](https://github.com/jupyterlab/jupyterlab-git.git)

<details><summary>README extract</summary>

JupyterLab extension providing Git version control integration.

See the main repository for full documentation.

</details>

### jupyter-mimetypes

(no summary)

`pip install jupyter-mimetypes` · installs (wheel) · licence: BSD License · rank 11218 · last release 2025-08-10 · [PyPI](https://pypi.org/project/jupyter-mimetypes/)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2023-2024 Datalayer, Inc.
 ~ BSD 3-Clause License

A Python package that provides enhanced Jupyter representation capabilities through proxy objects, enabling efficient Apache Arrow-based serialization for pandas DataFrames/Series and pickle-based serialization for generic Python objects in Jupyter environments. ...

Features:
- Efficient Serialization: Apache Arrow format for pandas DataFrames and Series
- Universal Fallback: Pickle-based serialization for any Python object
- Jupyter Integration: Seamless MIME bundle support for Jupyter display system ...

Example:
```python
import pandas as pd
from jupyter_mimetypes import serialize_object, deserialize_object

# Create a pandas DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
...

</details>

### judoscale

Official Python package for the Judoscale autoscaler

`pip install judoscale` · installs (wheel) · licence: MIT License · rank 11225 · last release 2026-10-19 · [PyPI](https://pypi.org/project/judoscale/) · [source](https://github.com/judoscale/judoscale-python)

<details><summary>README extract</summary>

This is the official Python adapter for Judoscale. You can use Judoscale without it, but this gives you request queue time metrics and job queue time (for supported job processors).

It is recommended to install the specific web framework and/or background job library support as "extras" to the `judoscale` PyPI package. ...

Example:
```python
# app.py

from judoscale.flask import Judoscale

# If your app is a top-level global

app = Flask("MyFlaskApp")
app.config.from_object('...')  # or however you configure your app
judoscale = Judoscale(app)

# If your app uses the application factory pattern

judoscale = Judoscale()

def create_app():
    app = Flask("MyFlaskApp")
...
```

...

</details>

### jinjasql2

Generate SQL Queries and Corresponding Bind Parameters using a Jinja2 Template

`pip install jinjasql2` · installs (wheel) · licence: MIT License · rank 11337 · last release 2026-07-07 · [PyPI](https://pypi.org/project/jinjasql2/)

<details><summary>README extract</summary>

This is a forked version of jinjasql, maintained at pythonutilities/jinjasql and published on PyPI as jinjasql2.

JinjaSQL is a template language for SQL statements and scripts.
Since it's based in Jinja2,
you have all the power it offers - conditional statements, macros,
looping constructs, blocks, inheritance, and many more. ...

Example:
```python
from jinjasql import JinjaSql
j = JinjaSql()
```

Sections: When to use JinjaSQL, Basic Usage, Multiple Param Styles, Handling In Clauses, SQL Safe Strings, How does JinjaSQL work?, The bind filter, Pre-processing the Query Template, Autoescape and JinjaSQL, Copyright

</details>

### jsonify

A csv to json converter

`pip install jsonify` · installs from source (sdist only) · licence: MIT · rank 12072 · last release 2016-04-29 · [PyPI](https://pypi.org/project/jsonify/)

<details><summary>README extract</summary>

Jsonify is a python script that takes a .csv file as input and outputs a file with the same data in .json format. To use this program from the command line, enter the python shell and run the following commands:
The script will generate a json file for you in the same directory with the same name as the original csv.

Example:
```python
>> from jsonify import convert
>> convert.jsonify('<your csv filename here>')
```

</details>

### jupyter-black

A simple extension for Jupyter Notebook and Jupyter Lab to beautify Python code automatically using Black. Fork of dnanhkhoa/nb_black.

`pip install jupyter-black` · installs (wheel) · licence: MIT · rank 12114 · last release 2024-08-30 · [PyPI](https://pypi.org/project/jupyter-black/)

<details><summary>README extract</summary>

master:

dev:

A simple extension for Jupyter Notebook and Jupyter Lab to beautify Python code
automatically using Black. Fork of
dnanhkhoa/nb_black with a few minor
modifications:

Features:
Once loaded, automatically format syntactically correct `jupyter` cells with
`black` once they are run.

Enhancements compared to dnanhkhoa/nb_black: ...

Example:
```python
import jupyter_black

jupyter_black.load()
```

Sections: jupyter-black, Features, Introduction, Dependencies, Quickstart, Configurable (recommended), The other way, TODO, Troubleshooting / FAQ, Buy Me a Coffee, 0.4.0 :: 2024-08-30, 0.3.4 :: 2023-04-27, 0.3.2, 0.3.3 :: 2022-11-20, 0.3.1 :: 2022-03-08

</details>

### joblib-stubs

joblib stubs

`pip install joblib-stubs` · installs (wheel) · licence: MIT · rank 12244 · last release 2026-10-12 · [PyPI](https://pypi.org/project/joblib-stubs/) · [source](https://github.com/phi-friday/joblib-stubs)

<details><summary>README extract</summary>

Type stubs for the joblib library.

> [!NOTE]
> This package provides type hints only and contains no runtime code.
> For the actual runtime implementation, install `joblib`.

> [!WARNING]
> This package does not include type stubs for `joblib.externals` (bundled `cloudpickle` and `loky`).

Example:
```python
from math import sqrt
from typing import assert_type

from joblib import Parallel, delayed

# Your type checker will now understand joblib's types
results = Parallel(n_jobs=2)(delayed(sqrt)(i**2) for i in range(10))
assert_type(results, list[float])
```

Sections: joblib-stubs, Usage

</details>

### ja-sentence

Light-weight sentence tokenizer for Japanese.

`pip install ja-sentence` · installs (wheel) · licence: Apache Software License · rank 12272 · last release 2021-10-23 · [PyPI](https://pypi.org/project/ja-sentence/)

<details><summary>README extract</summary>

A light-weight sentence tokenizer for Japanese.

Sample Code:

from ja_sentence.tokenizer import tokenize

paragraph_str = "えー！？くれるの？本当にいいの…？嬉しい！！"

sentence_list = tokenize(paragraph_str)

for sentence in sentence_list:
 print(sentence)

</details>

### json2table

Convert JSON to an HTML table

`pip install json2table` · installs (wheel) · licence: MIT · rank 12658 · last release 2016-10-21 · [PyPI](https://pypi.org/project/json2table/)

<details><summary>README extract</summary>

This is a simple Python package that allows a JSON object to be converted to HTML. It provides a `convert` function that accepts a `dict` instance and returns a string of converted HTML. For example, the simple JSON object `{"key" : "value"}` can be converted to HTML via:

The resulting table will resemble ...

Example:
```python
>>> from json2table import convert
>>> json_object = {"key" : "value"}
>>> build_direction = "LEFT_TO_RIGHT"
>>> table_attributes = {"style" : "width:100%"}
>>> html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
>>> print(html)
'<table style="width:100%"><tr><th>key</th><td>value</td></tr></table>'
```

Sections: json2table, Details, Tests

</details>

### jupyter-ai

A set of extensions providing agentic AI in JupyterLab

`pip install jupyter-ai` · installs (wheel) · licence: BSD License · rank 12852 · last release 2026-09-03 · [PyPI](https://pypi.org/project/jupyter-ai/) · [docs](https://jupyter-ai.readthedocs.io/en/stable/) · [source](https://github.com/jupyterlab/jupyter-ai)

<details><summary>README extract</summary>

An open source extension that connects AI agents to computational notebooks in JupyterLab.

Jupyter AI brings agentic AI to JupyterLab. It provides a native chat UI where you can collaborate with frontier AI agents — including Claude, Codex, GitHub Copilot, Gemini, Goose, Kiro, Mistral Vibe, and OpenCode — all integrated through the Agent Client ...

Sections: Jupyter AI, Quick Links, Governance

</details>

### json-fix

allow custom class json behavior on builtin json object

`pip install json-fix` · installs (wheel) · licence: MIT · rank 12911 · last release 2025-10-23 · [PyPI](https://pypi.org/project/json-fix/)

<details><summary>README extract</summary>

A pip module that lets you define a `json` method, that works like `toJSON` from JavaScript.

(e.g. it magically gets called whenever someone does `json.dumps(your_object)`)

From a technical perspective, this module is a safe, backwards-compatible, reversable patch to the built-in python `json` object that allows classes to specify how they ...

Features:
Because sometimes someone eles's code (e.g. a pip module) tries to serialize your object, like
And you'd have to fork their code to make it not throw an error.

Example:
```python
import json
json.dumps(list_containing_your_object)
```

Sections: What is this?, Why?, How do I use this tool?, Override Table, Fallback Table

</details>

### jsql

(no summary)

`pip install jsql` · installs (wheel) · licence: BSD License · rank 13068 · last release 2026-02-04 · [PyPI](https://pypi.org/project/jsql/)

### jupyterlab-lsp

Coding assistance for JupyterLab with Language Server Protocol

`pip install jupyterlab-lsp` · installs (wheel) · licence: BSD License · rank 13104 · last release 2026-04-02 · [PyPI](https://pypi.org/project/jupyterlab-lsp/) · [docs](https://jupyterlab-lsp.readthedocs.io/) · [source](https://github.com/jupyter-lsp/jupyterlab-lsp)

<details><summary>README extract</summary>

Features:
> Examples show Python code, but most features also work in R, bash, typescript, and many other languages.

Sections: Features, Hover, Diagnostics, Jump to Definition and References, Highlight References, Automatic Completion and Continuous Hinting, Automatic Signature Suggestions, The runtime kernel suggestions are still there, Rename, Diagnostics panel, Prerequisites, Configuring the servers, Other configuration methods

</details>

### jobseek-crawler-setup

Workspace CLI for configuring jobseek-crawler companies

`pip install jobseek-crawler-setup` · installs (wheel) · licence: MIT · rank 13374 · last release 2026-11-04 · [PyPI](https://pypi.org/project/jobseek-crawler-setup/)

### just-bin

A thin wrapper to distribute https://github.com/casey/just via pip.

`pip install just-bin` · installs (wheel) · licence: CC0-1.0 · rank 13875 · last release 2026-10-21 · [PyPI](https://pypi.org/project/just-bin/) · [source](https://github.com/justin-yan/pybin)

<details><summary>README extract</summary>

This project is part of the pybin family of packages, which are generally
permissively-licensed binary tools that have been re-packaged to be distributable via python's PyPI infrastructure using
`pip install $TOOLNAME-bin`. ...

Sections: just-bin, Packaging Details

</details>

### jeap-pipeline

A collection of Python modules and libraries for CI/CD pipelines in the jEAP context.

`pip install jeap-pipeline` · installs (wheel) · licence: Apache-2.0 · rank 13912 · last release 2026-11-03 · [PyPI](https://pypi.org/project/jeap-pipeline/)

<details><summary>README extract</summary>

`jeap-python-pipeline-lib` is a collection of reusable Python modules that standardize CI/CD pipeline
operations in the jEAP context — ECS deployment checks on AWS, recording deployments in the jEAP
Deployment Log service, Pact Broker `can-i-deploy` checks, Message Contract Service operations,
business-process test runs, and GitHub / Remedy ...

Sections: jEAP Python Pipeline Library, Documentation, Note

</details>

### jericho

A python interface to text-based adventure games.

`pip install jericho` · installs from source (sdist only) · licence: GNU General Public License v2 or later (GPLv2+) · rank 14134 · last release 2025-11-11 · [PyPI](https://pypi.org/project/jericho/)

_README extract left out: share-alike licence._

### jnjrender

CLI tool to render Jinja2 templates with YAML variables, with auto-selection from template libraries

`pip install jnjrender` · installs (wheel) · licence: not stated · rank 14260 · last release 2026-05-12 · [PyPI](https://pypi.org/project/jnjrender/)

### julian

Simple library for converting between Julian calendar dates and datetime objects

`pip install julian` · installs from source (sdist only) · licence: UNKNOWN · rank 14264 · last release 2016-03-26 · [PyPI](https://pypi.org/project/julian/)

<details><summary>README extract</summary>

julian is a simple Python library for converting between Julian dates
and Python datetime objects.

Example:
```python
import julian
import datetime

mjd = 54372.78
dt = julian.from_jd(mjd, fmt='mjd')
print(dt)
```

Sections: julian, Examples

</details>

### jupyterlab-launcher

Jupyter Launcher

`pip install jupyterlab-launcher` · installs (wheel) · licence: BSD License · rank 14272 · last release 2018-08-11 · [PyPI](https://pypi.org/project/jupyterlab-launcher/)

<details><summary>README extract</summary>

This package is used to launch an application built using JupyterLab

</details>

### jupyter-server-mathjax

MathJax resources as a Jupyter Server Extension.

`pip install jupyter-server-mathjax` · installs (wheel) · licence: BSD License · rank 14669 · last release 2022-07-14 · [PyPI](https://pypi.org/project/jupyter-server-mathjax/)

<details><summary>README extract</summary>

Sections: MathJax resources endpoints for Jupyter Server, Basic Usage, Maintenance Notes

</details>

### jsonlogic-rs

JsonLogic implemented with a Rust backend

`pip install jsonlogic-rs` · installs from source (sdist only) · licence: MIT License · rank 14693 · last release 2024-12-13 · [PyPI](https://pypi.org/project/jsonlogic-rs/)

<details><summary>README extract</summary>

This is an implementation of the [JsonLogic] specification in Rust.

Example:
```python
import jsonlogic_rs

res = jsonlogic_rs.apply(
    {"===": [{"var": "a"}, 7]},
    {"a": 7}
)

assert res == True

# If You have serialized JsonLogic and data, the `apply_serialized` method can
# be used instead
res = jsonlogic_rs.apply_serialized(
    '{"===": [{"var": "a"}, 7]}',
    '{"a": 7}'
)
```

Sections: json-logic-rs, Rust, Node/Browser, Python, Usage, Javascript, Commandline, Building, Prerequisites, WebAssembly

</details>

### jupyterlab-git-core

A JupyterLab extension for version control using git

`pip install jupyterlab-git-core` · installs (wheel) · licence: BSD License · rank 14720 · last release 2026-10-07 · [PyPI](https://pypi.org/project/jupyterlab-git-core/) · [source](https://github.com/jupyterlab/jupyterlab-git.git)

<details><summary>README extract</summary>

Core Git operations library for the jupyterlab-git JupyterLab extension.

This package provides the pure Python Git logic without tornado/jupyter-server dependencies.
It is intended to be used as a dependency of `jupyterlab-git`.

See the main repository for full documentation.

</details>

### jupyter-sphinx

Jupyter Sphinx Extensions

`pip install jupyter-sphinx` · installs (wheel) · licence: not stated · rank 14764 · last release 2023-12-28 · [PyPI](https://pypi.org/project/jupyter-sphinx/) · [docs](https://jupyter-sphinx.readthedocs.io) · [source](https://github.com/jupyter/jupyter-sphinx/)

<details><summary>README extract</summary>

`jupyter-sphinx` enables running code embedded in Sphinx documentation and
embedding output of that code into the resulting document. It has support
for rich output such as images and even Jupyter interactive widgets.

Sections: Jupyter Sphinx Extensions, Usage

</details>

### jaraco.logging

Support for Python logging facility

`pip install jaraco.logging` · installs (wheel) · licence: MIT · rank 14843 · last release 2025-06-16 · [PyPI](https://pypi.org/project/jaraco.logging/) · [source](https://github.com/jaraco/jaraco.logging)

<details><summary>README extract</summary>

Quickly solicit log level info from command-line parameters:

Example:
```python
parser = argparse.ArgumentParser()
jaraco.logging.add_arguments(parser)
args = parser.parse_args()
jaraco.logging.setup(args)
```

</details>

### JSON-Datetime

Allows for proper decoding of datetime values contained in JSON streams

`pip install JSON-Datetime` · installs from source (sdist only) · licence: ISC License (ISCL) · rank 14905 · last release 2020-11-15 · [PyPI](https://pypi.org/project/JSON-Datetime/)

<details><summary>README extract</summary>

JSON-datetime allows for proper decoding of datetime values contained in JSON
streams.

The JSON standard RFC 4627 does not
support datetime types. These are usually represented as strings and Python
decoders end up decoding them as such. Consider the following example:

As you can see, in the resulting dictionary `born` is still a string.

Example:
```python
import simplejson as json

>>> test = '{"name": "John Doe", "born": "Thu, 1 Mar 2012 10:00:49 UTC"}'
>>> json.loads(test)
{'born': u'Thu, 1 Mar 2012 10:00:49 UTC', 'name': u'John Doe'}
```

Sections: JSON-datetime, The problem, The solution, Custom parsing

</details>

### jsonmodels

Models to make easier to deal with structures that are converted to, or read from JSON.

`pip install jsonmodels` · installs (wheel) · licence: BSD License · rank 14909 · last release 2026-10-25 · [PyPI](https://pypi.org/project/jsonmodels/)

<details><summary>README extract</summary>

`jsonmodels` is library to make it easier for you to deal with structures that
are converted to, or read from JSON.

* Free software: BSD license

Features:
* Fully tested with Python 3.8+.

 .. code-block:: python

 from jsonmodels import models, fields, errors, validators

 class Cat(models.Base): ...

Sections: JSON models, Features, More

</details>

