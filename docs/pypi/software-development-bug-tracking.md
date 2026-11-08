# Software Development / Bug Tracking

[Index](README.md) · 8 packages in this topic, 2 more listed under another topic, by downloads.

### Pympler

A development tool to measure, monitor and analyze the memory behavior of Python objects.

`pip install Pympler` · installs (wheel) · licence: Apache Software License · rank 1782 · last release 2024-06-28 · [PyPI](https://pypi.org/project/Pympler/)

<details><summary>README extract</summary>

Pympler is a development tool to measure, monitor and analyze the memory
behavior of Python objects in a running Python application.

By pympling a Python application, detailed insight in the size and the lifetime
of Python objects can be obtained. ...

</details>

### ansible-compat

Ansible compatibility goodies

`pip install ansible-compat` · installs (wheel) · licence: MIT · rank 1818 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ansible-compat/) · [docs](https://ansible.readthedocs.io/projects/compat/) · [source](https://github.com/ansible/ansible-compat)

<details><summary>README extract</summary>

A python package contains functions that facilitate working with various
versions of Ansible.

Documentation is available at
ansible.readthedocs.io/projects/compat/.

Join the Ansible forum to ask questions, get help, and interact with the
community.

- Get Help: get help or help others.
 Please add appropriate tags if you start new discussions. ...

Sections: ansible-compat, Documentation, Communication

</details>

### molecule

Molecule aids in the development and testing of Ansible roles

`pip install molecule` · installs (wheel) · licence: MIT · rank 3498 · last release 2026-11-05 · [PyPI](https://pypi.org/project/molecule/) · [docs](https://docs.ansible.com/projects/molecule/) · [source](https://github.com/ansible/molecule)

<details><summary>README extract</summary>

Molecule is an Ansible testing framework designed for developing and testing
Ansible collections, playbooks, and roles.

Molecule leverages standard Ansible features including inventory, playbooks,
and collections to provide flexible testing workflows. ...

Sections: About Ansible Molecule, Documentation, Get Involved

</details>

### viztracer

A debugging and profiling tool that can trace and visualize python code execution

`pip install viztracer` · installs (wheel) · licence: Apache-2.0 · rank 3695 · last release 2025-11-11 · [PyPI](https://pypi.org/project/viztracer/) · [docs](https://viztracer.readthedocs.io)

<details><summary>README extract</summary>

VizTracer is a low-overhead logging/debugging/profiling tool that can trace and visualize your python code execution.

The front-end UI is powered by Perfetto. Use "AWSD" to zoom/navigate.
More help can be found in "Support - Controls".

Features:
* Detailed function entry/exit information on timeline with source code
* Super easy to use, no source code change for most features, no package dependency
* Low overhead, probably the fastest tracer in the market
* Supports threading, ...

Example:
```python
from viztracer import VizTracer

tracer = VizTracer()
tracer.start()
# Something happens here
tracer.stop()
tracer.save() # also takes output_file as an optional argument
```

...

</details>

### salt-lint

A command-line utility that checks for best practices in SaltStack.

`pip install salt-lint` · installs (wheel) · licence: MIT License · rank 3735 · last release 2023-02-09 · [PyPI](https://pypi.org/project/salt-lint/)

<details><summary>README extract</summary>

salt-lint checks Salt State files (SLS) for best practices and behavior that could potentially be improved.

 Explore the docs »

 Check the Linting Rules
 Report Bug
 Request Feature

Sections: salt-lint, Demo, [0.9.2] (2023-02-09), Fixed, [0.9.1] (2023-01-16), [0.9.0] (2023-01-13), Added, [0.8.0] (2021-11-09), [0.7.0] (2021-11-01), [0.6.1] (2021-06-01)

</details>

### molecule-plugins

Molecule Plugins

`pip install molecule-plugins` · installs (wheel) · licence: MIT · rank 4306 · last release 2026-11-02 · [PyPI](https://pypi.org/project/molecule-plugins/) · [docs](https://docs.ansible.com/projects/molecule/) · [source](https://github.com/ansible-community/molecule-plugins)

<details><summary>README extract</summary>

This repository contains the following molecule plugins:

- azure
- containers
- docker
- ec2
- gce
- openstack
- podman
- vagrant

Installing `molecule-plugins` does not install dependencies specific to each,
plugin. To install these you need to install the extras for each plugin, like
`pip3 install 'molecule-plugins[azure]'`. ...

</details>

### chalk-viztracer

A debugging and profiling tool that can trace and visualize python code execution (Chalk fork)

`pip install chalk-viztracer` · installs (wheel) · licence: Apache-2.0 · rank 4869 · last release 2026-08-14 · [PyPI](https://pypi.org/project/chalk-viztracer/) · [docs](https://viztracer.readthedocs.io)

<details><summary>README extract</summary>

This repository publishes the Chalk-maintained `chalk-viztracer` distribution.
It preserves VizTracer's `viztracer` Python package and command-line interfaces
while carrying patches that have not yet shipped in an upstream release. ...

Features:
* Detailed function entry/exit information on timeline with source code
* Super easy to use, no source code change for most features, no package dependency
* Low overhead, probably the fastest tracer in the market
* Supports threading, ...

Example:
```python
from viztracer import VizTracer

tracer = VizTracer()
tracer.start()
# Something happens here
tracer.stop()
tracer.save()  # also takes output_file as an optional argument
```

...

</details>

### codechecker

CodeChecker is an analyzer tooling, defect database and viewer extension

`pip install codechecker` · installs from source (sdist only) · licence: Apache Software License · rank 14327 · last release 2026-11-05 · [PyPI](https://pypi.org/project/codechecker/) · [docs](http://codechecker.readthedocs.io)

<details><summary>README extract</summary>

CodeChecker

CodeChecker is a static analysis infrastructure built on the LLVM/Clang
Static Analyzer toolchain, replacing
`scan-build` in a Linux or
macOS (OS X) development environment.

Check out our DEMO showing some analysis results of open-source projects! ...

Sections: Main features, Command line C/C++ Analysis, Web-based report storage, Command line features, Usage flow, User documentation, C/C++ Analysis, Web based report management, Storage of reports from analyzer tools, Common Tools, Helper Scripts, Linux: Build from source, Minimum Recommended package versions, Upgrading environment after system or Python upgrade

</details>

## Also in this topic

- [rollbar](internet-www-http.md#rollbar) - Easy and powerful exception tracking with Rollbar. Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.
- [yandex-cli](office-business.md#yandex-cli) - Interact with Yandex 360 services (Wiki, Tracker, Forms, …) from a CLI, an MCP server, or a Python SDK.
