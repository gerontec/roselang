# Software Development / Version Control

[Index](README.md) · 20 packages in this topic, 17 more listed under another topic, by downloads.

### dulwich

Python Git Library

`pip install dulwich` · installs (wheel) · licence: Apache-2.0 OR GPL-2.0-or-later · rank 432 · last release 2026-11-05 · [PyPI](https://pypi.org/project/dulwich/) · [source](https://github.com/dulwich/dulwich)

_README extract left out: share-alike licence._

### setuptools-rust

Setuptools Rust extension plugin

`pip install setuptools-rust` · installs (wheel) · licence: MIT License · rank 1828 · last release 2026-06-27 · [PyPI](https://pypi.org/project/setuptools-rust/) · [docs](https://setuptools-rust.readthedocs.io) · [source](https://github.com/PyO3/setuptools-rust)

<details><summary>README extract</summary>

`setuptools-rust` is a plugin for `setuptools` to build Rust Python extensions implemented with PyO3 or rust-cpython.

Compile and distribute Python extensions written in Rust as easily as if
they were written in C.

Sections: Setuptools plugin for Rust extensions, Quickstart, Environment variables for configuration, Next steps and final remarks

</details>

### pygit2

Python bindings for libgit2.

`pip install pygit2` · installs (wheel) · licence: GPLv2 with linking exception · rank 1853 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pygit2/) · [docs](https://www.pygit2.org/)

_README extract left out: share-alike licence._

### nbstripout

Strips outputs from Jupyter and IPython notebooks

`pip install nbstripout` · installs (wheel) · licence: MIT · rank 3087 · last release 2026-02-21 · [PyPI](https://pypi.org/project/nbstripout/) · [source](https://github.com/kynan/nbstripout)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD030 -->
<!-- markdownlint-disable MD041 -->
<!-- markdownlint-disable MD046 -->

Reads a notebook from a file or stdin, strips output and some metadata, and
writes the "cleaned" version of the notebook to the original file or stdout. ...

Sections: nbstripout: strip output from Jupyter and IPython notebooks, Python 3 only, Screencast, Usage, Using as a Git filter, Configuration files, Apply retroactively, Removing empty cells, Removing [init]{.title-ref} cells, Removing entire cells, Forcing UNIX newlines, Keeping some output, Output Types, Cell IDs

</details>

### poetry-dynamic-versioning

Plugin for Poetry to enable dynamic versioning based on VCS tags

`pip install poetry-dynamic-versioning` · installs (wheel) · licence: MIT License · rank 3184 · last release 2026-10-14 · [PyPI](https://pypi.org/project/poetry-dynamic-versioning/) · [source](https://github.com/mtkennerly/poetry-dynamic-versioning)

<details><summary>README extract</summary>

This is a Python 3.7+ plugin for Poetry 1.2.0+
and Poetry Core 1.0.0+
to enable dynamic versioning based on tags in your version control system,
powered by Dunamai.
Many different version control systems are supported, including Git and Mercurial;
please refer to the Dunamai page for the full list
(and minimum supported version where applicable). ...

Example:
```python
poetry run python -c "import dunamai; print(dunamai.Pattern.Default.regex())"
```

Sections: Dynamic versioning plugin for Poetry, Configuration, Environment variables, Command line mode, VCS archives, Caveats

</details>

### pullapprove

CLI for PullApprove5

`pip install pullapprove` · installs (wheel) · licence: not stated · rank 4790 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pullapprove/) · [docs](https://5.pullapprove.com/docs/?ref=pypi)

<details><summary>README extract</summary>

A CLI for validating and testing PullApprove code review configurations.

Sections: PullApprove, Usage, Documentation

</details>

### pre-commit-uv

Run pre-commit with uv

`pip install pre-commit-uv` · installs (wheel) · licence: MIT · rank 4979 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pre-commit-uv/) · [docs](https://github.com/tox-dev/pre-commit-uv/) · [source](https://github.com/tox-dev/pre-commit-uv)

<details><summary>README extract</summary>

Use `uv` to create virtual environments and install packages for `pre-commit`.

Changelog

Contributing

Features:
`pre-commit-uv` uses uv to create and seed hook environments. Caching the pre-commit directory avoids this work on later
runs, but the first install still needs it. This benchmark used this project's hooks with a warm uv cache:

Sections: pre-commit-uv, Why?, Configuration

</details>

### lefthook

Git hooks manager. Fast, powerful, simple.

`pip install lefthook` · installs (wheel) · licence: MIT · rank 4985 · last release 2026-10-13 · [PyPI](https://pypi.org/project/lefthook/)

<details><summary>README extract</summary>

> The fastest polyglot Git hooks manager out there

A Git hooks manager for Node.js, Ruby and many other types of projects.

* Fast. It is written in Go. Can run commands in parallel.
* Powerful. It allows to control execution and files you pass to your commands.
* Simple. It is single dependency-free binary which can work in any environment. ...

Sections: Lefthook, Usage, TL;DR, More details

</details>

### vcversioner

Use version control tags to discover version numbers

`pip install vcversioner` · installs from source (sdist only) · licence: ISC License (ISCL) · rank 5770 · last release 2016-04-12 · [PyPI](https://pypi.org/project/vcversioner/)

<details><summary>README extract</summary>

Elevator pitch: you can write a `setup.py` with no version information
specified, and vcversioner will find a recent, properly-formatted VCS tag and
extract a version from it.

It's much more convenient to be able to use your version control system's
tagging mechanism to derive a version number than to have to duplicate that
information all over ...

Example:
```python
from setuptools import setup

setup(
    # [...]
    setup_requires=['vcversioner'],
    vcversioner={},
)
```

Sections: vcversioner, Basic usage, Non-hook usage, Version modules, Customizing VCS commands, Project roots, Substitutions, Sphinx documentation, Read the Docs

</details>

### setuptools-git

Setuptools revision control system plugin for Git

`pip install setuptools-git` · installs (wheel) · licence: BSD License · rank 6375 · last release 2017-02-18 · [PyPI](https://pypi.org/project/setuptools-git/)

<details><summary>README extract</summary>

About

This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with ``MANIFEST.in``. ...

</details>

### git-remote-s3

A git remote helper for Amazon S3

`pip install git-remote-s3` · installs (wheel) · licence: Apache-2.0 · rank 6489 · last release 2026-08-20 · [PyPI](https://pypi.org/project/git-remote-s3/)

<details><summary>README extract</summary>

This library enables to use Amazon S3 as a git remote and LFS server.

It provides an implementation of a git remote helper to use S3 as a serverless Git server.

It also provide an implementation of the git-lfs custom transfer to enable pushing LFS managed files to the same S3 bucket used as remote.

Sections: git-remote-s3, Prerequisites, Data encryption, Access control, Use S3 remotes, Create a new repo, Clone a repo, Branches, etc., Using S3 remotes for submodules, Repo as S3 Source for AWS CodePipeline, Archive file location, Example AWS CodePipeline source action config, LFS, Creating the repo and pushing

</details>

### git-me-the-url

Generate sharable links to your Git source

`pip install git-me-the-url` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6495 · last release 2025-11-21 · [PyPI](https://pypi.org/project/git-me-the-url/) · [source](https://github.com/amykyta3/git-me-the-url)

_README extract left out: share-alike licence._

### requests-ntlm3

The HTTP NTLM proxy and/or server authentication library.

`pip install requests-ntlm3` · installs (wheel) · licence: ISC License (ISCL) · rank 7543 · last release 2020-02-19 · [PyPI](https://pypi.org/project/requests-ntlm3/)

<details><summary>README extract</summary>

requests-ntlm3, which is based on requests-ntlm, allows for HTTP NTLM authentication using the requests library.

Example:
```python
import requests
from requests_ntlm3 import HttpNtlmAuth

auth=HttpNtlmAuth('domain\\username','password')
requests.get(" auth=auth)
```

Sections: requests-ntlm3, Usage, Basic Usage, Changing NTLM compatibility level, Using with Requests Session, HTTP CONNECT Usage, Requirements

</details>

### mergify-cli

Mergify CLI is a tool that automates the creation and management of stacked pull requests on GitHub and handles CI results upload

`pip install mergify-cli` · installs (wheel) · licence: LicenseRef-Mergify-Proprietary · rank 7567 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mergify-cli/) · [docs](https://docs.mergify.com) · [source](https://github.com/Mergifyio/mergify-cli)

<details><summary>README extract</summary>

Drive Mergify from your terminal and CI pipelines:
stacked pull requests, the merge queue, Test Engine, scheduled freezes, and
configuration — all from a single self-contained binary that reuses your
existing GitHub (`gh`) login.

- One static binary. No runtime, no dependencies — drop it on a developer
 laptop or a CI runner and go. ...

Sections: Mergify CLI, Homebrew (recommended for macOS), Manual download (Windows, or to bypass the script), Authentication, Quick start, Commands, Shell completions, Global options, Environment variables, Exit codes, AI Agent Skills, Documentation

</details>

### mercurial

Fast scalable distributed SCM (revision control, version control) system

`pip install mercurial` · installs (wheel) · licence: GPL-2.0-or-later · rank 7643 · last release 2026-08-11 · [PyPI](https://pypi.org/project/mercurial/)

_README extract left out: share-alike licence._

### snapper-fmt

Semantic line break formatter for Org, LaTeX, Markdown, and plaintext

`pip install snapper-fmt` · installs (wheel) · licence: MIT License · rank 10456 · last release 2026-10-11 · [PyPI](https://pypi.org/project/snapper-fmt/) · [docs](https://snapper.turtletech.us/docs/) · [source](https://github.com/TurtleTech-ehf/snapper)

<details><summary>README extract</summary>

Features:
When multiple authors collaborate on a paper using Git, traditional line wrapping at a fixed column width causes problems.
A single word change can trigger a diff that spans an entire paragraph. ...

Sections: About, Why?, Design, Usage, MCP server (AI assistants), Pre-commit hook, Emacs (Apheleia), VS Code, Neovim, Vim, Obsidian, Microsoft Word, Git smudge/clean filter, Vale integration

</details>

### requests-ntlm2

The HTTP NTLM proxy and/or server authentication library.

`pip install requests-ntlm2` · installs (wheel) · licence: ISC License (ISCL) · rank 10582 · last release 2025-05-28 · [PyPI](https://pypi.org/project/requests-ntlm2/) · [docs](https://dopstar.github.io/requests-ntlm2) · [source](https://github.com/dopstar/requests-ntlm2)

<details><summary>README extract</summary>

NTLM authentication plugin for Requests

requests-ntlm2, which is based on requests-ntlm, allows for HTTP NTLM authentication using the requests library.

Example:
```python
import requests
from requests_ntlm2 import HttpNtlmAuth

auth=HttpNtlmAuth('domain\\username','password')
requests.get(" auth=auth)
```

Sections: requests-ntlm2, Usage, Basic Usage, Changing NTLM compatibility level, Using with Requests Session, HTTP CONNECT Usage, Requirements

</details>

### setuptools-protobuf

Setuptools protobuf extension plugin

`pip install setuptools-protobuf` · installs (wheel) · licence: Apache Software License · rank 13287 · last release 2026-11-01 · [PyPI](https://pypi.org/project/setuptools-protobuf/)

<details><summary>README extract</summary>

Example:
```python
from setuptools_protobuf import Protobuf

setup(
...
    setup_requires=['setuptools-protobuf'],
    protobufs=[Protobuf('example/foo.proto')],
)
```

Sections: Dependencies, Usage, setup.py, setup.cfg, pyproject.toml, GitHub actions

</details>

### vcstool

vcstool provides a command line tool to invoke vcs commands on multiple repositories.

`pip install vcstool` · installs (wheel) · licence: Apache Software License · rank 13364 · last release 2021-08-09 · [PyPI](https://pypi.org/project/vcstool/)

<details><summary>README extract</summary>

vcstool enables batch commands on multiple different vcs repositories. Currently it supports git, hg, svn and bzr.

</details>

### gitmatch

Gitignore-style path matching

`pip install gitmatch` · installs (wheel) · licence: MIT · rank 14538 · last release 2025-12-05 · [PyPI](https://pypi.org/project/gitmatch/) · [docs](https://gitmatch.readthedocs.io) · [source](https://github.com/jwodder/gitmatch)

<details><summary>README extract</summary>

GitHub
| PyPI
| Documentation
| Issues
| Changelog

`gitmatch` provides `gitignore`-style pattern matching of file paths.
Simply pass in a sequence of `gitignore` patterns and you'll get back an
object for testing whether a given relative path matches the patterns.

Example:
```python
>>> import gitmatch
>>> gi = gitmatch.compile(["foo", "!bar", "*.dir/"])
>>> bool(gi.match("foo"))
True
>>> bool(gi.match("bar"))
False
>>> bool(gi.match("quux"))
False
>>> bool(gi.match("foo/quux"))
True
>>> bool(gi.match("foo/bar"))
True
>>> bool(gi.match("bar/foo"))
True
>>> bool(gi.match("bar/quux"))
False
>>> bool(gi.match("foo.dir"))
False
...
```

</details>

## Also in this topic

- [setuptools-scm](software-development-libraries.md#setuptools-scm) - the blessed package to manage your versions by scm tags
- [word2number](documentation-sphinx.md#word2number) - Convert number words eg. three hundred and forty two to numbers (342).
- [whatthepatch](software-development.md#whatthepatch) - A patch parsing and application library.
- [versioningit](software-development-build-tools.md#versioningit) - Versioning It with your Version In Git
- [bump-my-version](software-development-build-tools.md#bump-my-version) - Version bump your Python project
- [yoyo-migrations](database.md#yoyo-migrations) - Database migrations with SQL
- [alembic-git-revisions](database.md#alembic-git-revisions) - Automatic Alembic migration chaining based on git commit history
- [clearml](scientific-engineering-artificial-intelligence.md#clearml) - ClearML - Auto-Magical Experiment Manager, Version Control, and MLOps for AI
- [lakefs](software-development-libraries-2.md#lakefs) - lakeFS Python SDK Wrapper
- [p4python](software-development.md#p4python) - P4Python - Python interface to Perforce API
- [gitman](software-development.md#gitman) - A language-agnostic dependency manager using Git.
- [YORM](database.md#yorm) - Automatic object-YAML mapping for Python.
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [version-utils](software-development-libraries-3.md#version-utils) - Library for parsing system package strings and comparing package versions
- [setupmeta](software-development-build-tools.md#setupmeta) - Simplify your setup.py
- [gitignorefile](software-development-libraries-4.md#gitignorefile) - A spec-compliant `.gitignore` parser for Python
- [gitchangelog](software-development.md#gitchangelog) - gitchangelog generates a changelog thanks to git log.
