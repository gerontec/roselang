# Software Development / Quality Assurance

[Index](README.md) · 122 packages in this topic, 140 more listed under another topic, by downloads.

### coverage

Code coverage measurement for Python

`pip install coverage` · installs (wheel) · licence: Apache-2.0 · rank 108 · last release 2026-11-04 · [PyPI](https://pypi.org/project/coverage/) · [docs](https://coverage.readthedocs.io/en/7.17.2)

<details><summary>README extract</summary>

Code coverage measurement for Python.

kitlicenseversions|
test-statusquality-statusdocsmetacov|
tideliftsponsorstarsmastodon-coveragepymastodon-nedbat|

Coverage.py measures code coverage, typically during test execution. ...

Sections: Coverage.py, For Enterprise, Getting Started

</details>

### pytest-xdist

pytest xdist plugin for distributed testing, most importantly across multiple CPUs

`pip install pytest-xdist` · installs (wheel) · licence: MIT · rank 176 · last release 2025-07-01 · [PyPI](https://pypi.org/project/pytest-xdist/) · [docs](https://pytest-xdist.readthedocs.io/en/latest) · [source](https://github.com/pytest-dev/pytest-xdist)

<details><summary>README extract</summary>

The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing
tests across multiple CPUs to speed up test execution:
With this call, pytest will spawn a number of workers processes equal to the number of available CPUs, and distribute
the tests randomly across them. ...

Sections: pytest-xdist, Documentation

</details>

### pytest-rerunfailures

pytest plugin to re-run tests to eliminate flaky failures

`pip install pytest-rerunfailures` · installs (wheel) · licence: MPL-2.0 · rank 526 · last release 2026-09-17 · [PyPI](https://pypi.org/project/pytest-rerunfailures/)

<details><summary>README extract</summary>

pytest-rerunfailures is a plugin for pytest that
re-runs tests to eliminate intermittent failures.

You will need the following prerequisites in order to use pytest-rerunfailures:

- Python 3.10+ or PyPy3
- pytest 8.2 or newer

This plugin can recover from a hard crash with the following optional
prerequisites:

- pytest-xdist 2.3.0 or newer ...

Features:
- Allow configuring `only_rerun` regular expressions in `pytest.ini` files.
 (#165)
- Show each rerun attempt and its final outcome in the rerun test summary info
 section. (#191) ...

Example:
```python
@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True, False])
```

...

</details>

### diff_cover

Run coverage and linting reports on diffs

`pip install diff_cover` · installs (wheel) · licence: Apache-2.0 · rank 709 · last release 2026-11-04 · [PyPI](https://pypi.org/project/diff_cover/) · [source](https://github.com/Bachmann1234/diff-cover)

<details><summary>README extract</summary>

Automatically find diff lines that need test coverage.
Also finds diff lines that have violations (according to tools such
as pycodestyle, pyflakes, flake8, or pylint).
This is used as a code quality metric during code reviews.

Features:
Diff coverage is the percentage of new or modified
lines that are covered by tests. This provides a clear
and achievable standard for code review: If you touch a line
of code, that line should be covered. ...

Sections: diff-cover, Overview, Getting Started, Multiple XML Coverage Reports, Quality Coverage, Compare Branch, Diff File, Total Percent Formatting, Fail Under, Exclude/Include paths, . check if any include pattern was specified, . check if the file is part of any exclude pattern, Quiet mode, Showing Covered and Uncovered Lines

</details>

### pytest-metadata

pytest plugin for test session metadata

`pip install pytest-metadata` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 754 · last release 2024-02-12 · [PyPI](https://pypi.org/project/pytest-metadata/) · [source](https://github.com/pytest-dev/pytest-metadata)

<details><summary>README extract</summary>

pytest-metadata is a plugin for pytest that provides
access to test session metadata.

You will need the following in order to use pytest-metadata:

- Python 3.8+ or PyPy3

Example:
```python
import pytest

pytestmark = pytest.mark.usefixtures('include_metadata_in_junit_xml')

def test():
    pass
```

Sections: pytest-metadata, Requirements, Available metadata, Additional metadata, Continuous integration, Viewing metadata, Including metadata in Junit XML, Accessing metadata, Plugin integrations, Resources

</details>

### vulture

Find dead code

`pip install vulture` · installs (wheel) · licence: MIT License · rank 945 · last release 2026-03-25 · [PyPI](https://pypi.org/project/vulture/) · [source](https://github.com/jendrikseipp/vulture)

<details><summary>README extract</summary>

Vulture finds unused code in Python programs. This is useful for
cleaning up and finding errors in large code bases. If you run Vulture
on both your library and test suite you can find untested code.

Due to Python's dynamic nature, static code analyzers like Vulture are
likely to miss some dead code. ...

Features:
* fast: uses static code analysis
* tested: tests itself and has complete test coverage
* complements pyflakes and has the same output syntax
* sorts unused classes and functions by size with `--sort-by-size`

Example:
```python
import os

class Greeter:
    def greet(self):
        print("Hi")

def hello_world():
    message = "Hello, world!"
    greeter = Greeter()
    func_name = "greet"
    greet_func = getattr(greeter, func_name)
    greet_func()

if name == "main":
...

</details>

### prek

A fast Git hook manager written in Rust, designed as a drop-in alternative to pre-commit, reimagined.

`pip install prek` · installs (wheel) · licence: MIT · rank 955 · last release 2026-11-04 · [PyPI](https://pypi.org/project/prek/) · [source](https://github.com/j178/prek)

<details><summary>README extract</summary>

Installation • Quick start • Documentation

prek is a framework for running hooks on your code. It runs them before you commit changes, on demand, or in CI.
These hooks can format files, catch lint errors, detect secrets, or run any other command your project defines.
prek also installs and manages the tools and dependencies they need. ...

Features:
- A single binary with no dependencies, does not require Python or any other runtime.
- Faster than `pre-commit` and more efficient in disk space usage.
- Fully compatible with the original pre-commit configurations and hooks. ...

Sections: About, Features, Quick start, Why prek?, prek is faster, prek is easier to work with, Who is using prek?

</details>

### pytest-html

pytest plugin for generating HTML reports

`pip install pytest-html` · installs (wheel) · licence: MPL-2.0 · rank 973 · last release 2026-01-19 · [PyPI](https://pypi.org/project/pytest-html/) · [source](https://github.com/pytest-dev/pytest-html)

<details><summary>README extract</summary>

pytest-html is a plugin for pytest that generates a HTML report for test results.

- Documentation
- Release Notes
- Issue Tracker
- Code

Sections: pytest-html, Resources, Screenshots

</details>

### pytest-repeat

pytest plugin for repeating tests

`pip install pytest-repeat` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 1037 · last release 2025-04-07 · [PyPI](https://pypi.org/project/pytest-repeat/)

<details><summary>README extract</summary>

pytest-repeat is a plugin for pytest that makes it
easy to repeat a single test, or multiple tests, a specific number of times.

You will need the following prerequisites in order to use pytest-repeat:

- Python 3.9+ or PyPy3
- pytest 5 or newer

Example:
```python
import pytest

@pytest.mark.repeat(3)
def test_repeat_decorator():
    pass
```

Sections: pytest-repeat, Requirements, Repeating a test, Repeating a test until failure, UnitTest Style Tests, Resources

</details>

### pip-tools

pip-tools keeps your pinned dependencies fresh.

`pip install pip-tools` · installs (wheel) · licence: BSD-3-Clause · rank 1038 · last release 2026-10-07 · [PyPI](https://pypi.org/project/pip-tools/) · [docs](https://pip-tools.readthedocs.io/en/latest/) · [source](https://github.com/jazzband/pip-tools)

<details><summary>README extract</summary>

<!-- pyml disable-next-line first-line-heading -->
[![jazzband-image]][jazzband]
[][pypi]
[][pyversions]
[][pre-commit]
[][buildstatus-gha]
[][codecov]
[![Matrix Room Badge]][Matrix Room]
[![Matrix Space Badge]][Matrix Space]
[![discord-chat-image]][discord-chat] ...

Sections: pip-tools = pip-compile + pip-sync, Example usage for `pip-compile`, Requirements from `pyproject.toml`, Requirements from `setup.py` and `setup.cfg`, Requirements from `requirements.in`, Updating requirements, Understanding output file behavior, Using hashes, Output File, Forwarding options to `pip`, Workflow for layered requirements, Version control integration, Example usage for `pip-sync`, Maximizing reproducibility

</details>

### sqlfluff

The SQL Linter for Humans

`pip install sqlfluff` · installs (wheel) · licence: MIT License · rank 1178 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sqlfluff/) · [docs](https://docs.sqlfluff.com) · [source](https://github.com/sqlfluff/sqlfluff)

<details><summary>README extract</summary>

SQLFluff is a dialect-flexible and configurable SQL linter. Designed
with ELT applications in mind, SQLFluff also works with Jinja templating
and dbt. SQLFluff will auto-fix most linting errors, allowing you to focus
your time on what matters.

Sections: The SQL Linter for Humans, VS Code Extension, Getting Started, Documentation, SQLFluff on Slack, SQLFluff on Twitter

</details>

### pytest-base-url

pytest plugin for URL based testing

`pip install pytest-base-url` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 1248 · last release 2024-01-31 · [PyPI](https://pypi.org/project/pytest-base-url/) · [source](https://github.com/pytest-dev/pytest-base-url)

<details><summary>README extract</summary>

pytest-base-url is a simple plugin for pytest that provides an optional base
URL via the command line or configuration file.

You will need the following prerequisites in order to use pytest-base-url:

- Python 3.8+ or PyPy3

Example:
```python
import urllib2

def test_example(base_url):
    assert 200 == urllib2.urlopen(base_url).getcode()
```

Sections: pytest-base-url, Requirements, Specifying a Base URL, Using the Command Line, Using a Configuration File, Using an Environment Variable, Using a Fixture, Available Live Servers, Verifying the Base URL, Skipping Base URLs, Resources

</details>

### allure-python-commons

Contains the API for end users as well as helper functions and classes to build Allure adapters for Python test frameworks

`pip install allure-python-commons` · installs (wheel) · licence: Apache Software License · rank 1570 · last release 2026-09-29 · [PyPI](https://pypi.org/project/allure-python-commons/) · [source](https://github.com/allure-framework/allure-python)

<details><summary>README extract</summary>

> The package contains classes and functions for users of Allure Report. It can
> be used to enhance reports using an existing Allure adapter or to create new
> adapters.

[]( "Allure Report")

- Learn more about Allure Report at
- 📚 Documentation – discover official documentation for Allure Report ...

Example:
```python
import allure

@allure.title("My test")
def test_fn():
    pass
```

Sections: Allure Common API, User's API, Decorators API, Runtime API, Adapter API

</details>

### allure-pytest

Allure pytest integration

`pip install allure-pytest` · installs (wheel) · licence: Apache Software License · rank 1691 · last release 2026-09-29 · [PyPI](https://pypi.org/project/allure-pytest/) · [docs](https://allurereport.org/docs/pytest/) · [source](https://github.com/allure-framework/allure-python)

<details><summary>README extract</summary>

> An Allure adapter for pytest.

[]( "Allure Report")

- Learn more about Allure Report at
- 📚 Documentation – discover official documentation for Allure Report
- ❓ Questions and Support – get help from the team and community
- 📢 Official announcements – stay updated with our latest news and updates ...

Sections: Allure Pytest Plugin, Quick start, Further readings

</details>

### pytest-order

pytest plugin to run tests in a specific order

`pip install pytest-order` · installs (wheel) · licence: MIT · rank 1824 · last release 2026-06-13 · [PyPI](https://pypi.org/project/pytest-order/) · [docs](https://pytest-order.readthedocs.io/) · [source](https://github.com/pytest-dev/pytest-order)

<details><summary>README extract</summary>

`pytest-order` is a pytest plugin that allows you to customize the order in which
your tests are run. It uses the marker `order` that defines when a specific
test shall run, either by using an ordinal number, or by specifying the
relationship to other tests. ...

</details>

### pytest-forked

run tests in isolated forked subprocesses

`pip install pytest-forked` · installs (wheel) · licence: MIT License · rank 1858 · last release 2026-08-08 · [PyPI](https://pypi.org/project/pytest-forked/)

<details><summary>README extract</summary>

This plugin does not work on Windows because there's no `fork` support.

* `--forked`: run each test in a forked
 subprocess to survive `SEGFAULTS` or otherwise dying processes.

Example:
```python
@pytest.mark.forked
def test_with_leaky_state():
    run_some_monkey_patches()
```

Sections: pytest-forked: run each test in a forked subprocess, Usage examples

</details>

### autoflake

Removes unused imports and unused variables

`pip install autoflake` · installs (wheel) · licence: MIT · rank 1950 · last release 2026-08-22 · [PyPI](https://pypi.org/project/autoflake/)

<details><summary>README extract</summary>

_autoflake_ removes unused imports and unused variables from Python code. It
makes use of pyflakes to do this.

By default, autoflake only removes unused imports for modules that are part of
the standard library. ...

Example:
```python
import math
import re
import os
import random
import multiprocessing
import grp, pwd, platform
import subprocess, sys

def foo():
    from abc import ABCMeta, WeakSet
    try:
        import multiprocessing
        print(multiprocessing.cpu_count())
    except ImportError as exception:
        print(sys.version)
    return math.pi
```

Sections: autoflake, Introduction, Example, Advanced usage, Configuration, Tests, Excluding specific lines, Using pre-commit hooks

</details>

### ansible-lint

Checks playbooks for practices and behavior that could potentially be improved

`pip install ansible-lint` · installs (wheel) · licence: GPL-3.0-or-later · rank 1978 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ansible-lint/) · [docs](https://docs.ansible.com/projects/lint/) · [source](https://github.com/ansible/ansible-lint)

_README extract left out: share-alike licence._

### djlint

HTML template linter and formatter (Django, Jinja, Twig, Nunjucks, Handlebars, Mustache, Liquid, Go templates, Angular, Tera, Askama, Mako)

`pip install djlint` · installs (wheel) · licence: GPL-3.0-or-later · rank 2008 · last release 2026-11-07 · [PyPI](https://pypi.org/project/djlint/) · [docs](https://djlint.com) · [source](https://github.com/djlint/djLint)

_README extract left out: share-alike licence._

### clang-format

Clang-Format is an LLVM-based code formatting tool

`pip install clang-format` · installs (wheel) · licence: Apache Software License · rank 2025 · last release 2026-11-04 · [PyPI](https://pypi.org/project/clang-format/) · [docs](https://clang.llvm.org/docs/ClangFormat.html) · [source](https://github.com/ssciwr/clang-format-wheel)

<details><summary>README extract</summary>

This project packages the `clang-format` utility as a Python package. It allows you to install `clang-format` directly from PyPI:

This projects intends to release a new PyPI package for each major and minor release of `clang-format`.

You can use `pipx` to run clang-format, as well. ...

Sections: clang-format Python distribution, Use with pipx, Use from pre-commit

</details>

### django-health-check

Monitor the health of your Django app and its connected services.

`pip install django-health-check` · installs (wheel) · licence: MIT License · rank 2121 · last release 2026-11-02 · [PyPI](https://pypi.org/project/django-health-check/) · [docs](https://codingjoe.dev/django-health-check/) · [source](https://github.com/codingjoe/django-health-check)

<details><summary>README extract</summary>

Documentation |
 Issues |
 Changelog |
 Funding 💚

_Pluggable health checks for Django applications

</details>

### pylint-plugin-utils

Utilities and helpers for writing Pylint plugins

`pip install pylint-plugin-utils` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 2208 · last release 2025-06-24 · [PyPI](https://pypi.org/project/pylint-plugin-utils/) · [source](https://github.com/PyCQA/pylint-plugin-utils)

_README extract left out: share-alike licence._

### pytest-github-actions-annotate-failures

pytest plugin to annotate failed tests with a workflow command for GitHub Actions

`pip install pytest-github-actions-annotate-failures` · installs (wheel) · licence: MIT · rank 2276 · last release 2026-06-19 · [PyPI](https://pypi.org/project/pytest-github-actions-annotate-failures/) · [source](https://github.com/pytest-dev/pytest-github-actions-annotate-failures)

<details><summary>README extract</summary>

Pytest plugin to annotate failed tests with a workflow command for GitHub Actions

Sections: pytest-github-actions-annotate-failures, Usage, Warning annotations, Screenshot

</details>

### sqlfluff-templater-dbt

Lint your dbt project SQL

`pip install sqlfluff-templater-dbt` · installs (wheel) · licence: MIT License · rank 2452 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sqlfluff-templater-dbt/) · [docs](https://docs.sqlfluff.com) · [source](https://github.com/sqlfluff/sqlfluff)

<details><summary>README extract</summary>

This plugin works with SQLFluff, the
SQL linter for humans, to correctly parse and compile SQL projects using
dbt.

For more details on how to use this plugin,
see the documentation.

</details>

### Flake8-pyproject

Flake8 plug-in loading the configuration from pyproject.toml

`pip install Flake8-pyproject` · installs (wheel) · licence: MIT License · rank 2582 · last release 2025-11-28 · [PyPI](https://pypi.org/project/Flake8-pyproject/) · [source](https://github.com/john-hen/Flake8-pyproject)

<details><summary>README extract</summary>

﻿# Flake8-pyproject
*Flake8 plug-in loading the configuration from `pyproject.toml`*

[Flake8] cannot be configured via `pyproject.toml`, even though
virtually all other Python dev tools have adopted it as the central
location for project configuration. ...

</details>

### pylint-django

A Pylint plugin to help Pylint understand the Django web framework

`pip install pylint-django` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 2836 · last release 2026-07-11 · [PyPI](https://pypi.org/project/pylint-django/) · [source](https://github.com/pylint-dev/pylint-django)

_README extract left out: share-alike licence._

### import-deps

find python module imports

`pip install import-deps` · installs (wheel) · licence: MIT License · rank 2975 · last release 2026-01-09 · [PyPI](https://pypi.org/project/import-deps/) · [source](https://github.com/schettino72/import-deps)

<details><summary>README extract</summary>

Find python module's import dependencies.

`import_deps` is based on ast module from standard library,
so the modules being analysed are *not* executed.

Example:
```python
from . import foo_b
from .foo_c import obj_c
```

Sections: import_deps, Usage, Usage (CLI), Analyze a single file, Analyze a package directory, JSON output, Transitive imports, DOT output for visualization, Checks, Check for circular dependencies, Check for re-imports, Check for inner imports, Topological sort, Handling circular dependencies

</details>

### pytest-datadir

pytest plugin for test data directories and files

`pip install pytest-datadir` · installs (wheel) · licence: MIT License · rank 3098 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pytest-datadir/)

<details><summary>README extract</summary>

pytest plugin for manipulating test data directories and files.

Example:
```python
def test_read_global(shared_datadir):
    contents = (shared_datadir / "hello.txt").read_text()
    assert contents == "Hello World!\n"

def test_read_module(datadir):
    contents = (datadir / "spam.txt").read_text()
    assert contents == "eggs\n"
```

Sections: pytest-datadir, Usage, lazy_datadir, lazy_shared_datadir

</details>

### pytest-ordering

pytest plugin to run your tests in a specific order

`pip install pytest-ordering` · installs (wheel) · licence: MIT License · rank 3170 · last release 2018-11-14 · [PyPI](https://pypi.org/project/pytest-ordering/)

### lizard

A code analyzer without caring the C/C++ header files. It works with Java, C/C++, JavaScript, Python, Ruby, Swift, Objective C. Metrics includes cyclomatic complexity number etc.

`pip install lizard` · installs (wheel) · licence: Freeware · rank 3366 · last release 2026-11-07 · [PyPI](https://pypi.org/project/lizard/) · [source](https://github.com/terryyin/lizard)

<details><summary>README extract</summary>

Lizard is an extensible Cyclomatic Complexity Analyzer for many programming languages
including C/C++ (doesn't require all the header files or Java imports). It also does
copy-paste detection (code clone detection/code duplicate detection) and many other forms of static
code analysis.

A list of supported languages:

- C# (C Sharp) ...

Example:
```python
>>> import lizard
>>> i = lizard.analyze_file("../cpputest/tests/AllTests.cpp")
>>> print(i.dict)
{'nloc': 9, 'function_list': [<lizard.FunctionInfo object at 0x10bf7af10>], 'filename': '../cpputest/tests/AllTests.cpp'}
>>> print(i.function_list[0].dict)
...
```

...

</details>

### ansi2html

Convert text with ANSI color codes to HTML or to LaTeX

`pip install ansi2html` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 3516 · last release 2026-09-06 · [PyPI](https://pypi.org/project/ansi2html/) · [docs](https://ansi2html.readthedocs.io/) · [source](https://github.com/pycontribs/ansi2html)

_README extract left out: share-alike licence._

### skillsaw

A configurable linter for agent skills, plugins, and AI coding assistant context

`pip install skillsaw` · installs (wheel) · licence: Apache Software License · rank 3875 · last release 2026-11-07 · [PyPI](https://pypi.org/project/skillsaw/) · [docs](https://github.com/stbenjam/skillsaw#readme) · [source](https://github.com/stbenjam/skillsaw)

<details><summary>README extract</summary>

Keep your skills sharp.

A linter for the files that steer AI coding agents.

Agent instructions behave like code, but most teams still review them like
prose. skillsaw gives them a linter. ...

Sections: skillsaw, See it work, Try it, What it catches, Built for real workflows, Measure the result

</details>

### pylint-pydantic

A Pylint plugin to help Pylint understand the Pydantic

`pip install pylint-pydantic` · installs (wheel) · licence: GPLv3 · rank 4134 · last release 2025-10-27 · [PyPI](https://pypi.org/project/pylint-pydantic/)

_README extract left out: share-alike licence._

### shandy-sqlfmt

sqlfmt formats your dbt SQL files so you don't have to.

`pip install shandy-sqlfmt` · installs (wheel) · licence: Apache-2.0 · rank 4140 · last release 2026-08-10 · [PyPI](https://pypi.org/project/shandy-sqlfmt/) · [docs](https://docs.sqlfmt.com) · [source](https://github.com/tconbeer/sqlfmt)

<details><summary>README extract</summary>

sqlfmt formats your dbt SQL files so you don't have to. It is similar in nature to black, gofmt,
and rustfmt (but for SQL).

1. sqlfmt promotes collaboration. An auto-formatter makes it easier to collaborate with your team and solicit contributions from new people. You will never have to mention (or argue about) code style in code reviews again. ...

Features:
Because SQL is code! But there are other good reasons too.

Sections: sqlfmt, Documentation, Try it first, Using sqlfmt, Configuring sqlfmt using pyproject.toml, The jinjafmt extra, Using sqlfmt with different SQL dialects, Integrations, dbt, Other Integrations, The sqlfmt style, Why lowercase?, Why trailing commas?, Providing Feedback

</details>

### lintrunner-adapters

Adapters and tools for lintrunner

`pip install lintrunner-adapters` · installs (wheel) · licence: MIT · rank 4515 · last release 2026-07-13 · [PyPI](https://pypi.org/project/lintrunner-adapters/) · [source](https://github.com/justinchuby/lintrunner-adapters)

<details><summary>README extract</summary>

Adapters and tools for lintrunner.

`lintrunner-adapters` currently supports popular Python / Rust / C++ linters and formatters like `flake8`, `pylint`, `mypy`, `black`, `ruff`(with auto-fix support), `rustfmt`, `clippy`, `clang-format` and many more - and the list is growing. Contributions welcome! ...

Sections: lintrunner-adapters, Usage, GitHub action, How to, Use `lintrunner_adapters` with `lintrunner` in your project, Write lint config in `.lintrunner.toml`, Create a new adapter, Option 1, Option 2

</details>

### django-coverage-plugin

Django template coverage.py plugin

`pip install django-coverage-plugin` · installs (wheel) · licence: Apache-2.0 · rank 4528 · last release 2026-04-04 · [PyPI](https://pypi.org/project/django-coverage-plugin/) · [source](https://github.com/coveragepy/django_coverage_plugin)

<details><summary>README extract</summary>

A coverage.py plugin to measure test coverage of Django templates.

statuskitlicense|
versionsdjversions|
sponsorbluesky-nedbatmastodon-nedbat|

Supported on:

- Python: 3.10 through 3.14.

- Django: 5.2 through 6.0.

- Coverage.py: 6.x or higher. ...

Sections: Django Template Coverage.py Plugin, Configuration, Caveats, What the? How?, Tests, v3.2.2 — 2026-04-04, v3.2.0 — 2025-10-05, v3.1.1 — 2025-06-15, v3.1.0 — 2023-07-10, v3.0.0 — 2022-12-06, v2.0.4 — 2022-10-31, v2.0.3 — 2022-05-04, v2.0.2 — 2021-11-11, v2.0.1 — 2021-10-06

</details>

### pyproject-fmt

Format pyproject.toml files

`pip install pyproject-fmt` · installs (wheel) · licence: MIT · rank 4545 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyproject-fmt/) · [docs](https://pyproject-fmt.readthedocs.io/en/latest/) · [source](https://github.com/tox-dev/toml-fmt/tree/main/pyproject-fmt)

<details><summary>README extract</summary>

`pyproject-fmt` formats `pyproject.toml` files without discarding comments. It uses a small configuration surface
to keep results stable across projects. See the
release history for version changes.

Example:
```python
from pyproject_fmt import run

exit_code = run(["path/to/pyproject.toml"])
```

Sections: pyproject-fmt, Pre-commit, Python API, Project settings, Shared settings, Command-line interface, Python classifiers, Table shape, Spacing, String wrapping, General Formatting, Table Ordering, String Quotes, Key Quotes

</details>

### gitlint-core

Git commit message linter written in python, checks your commit messages for style.

`pip install gitlint-core` · installs (wheel) · licence: MIT License · rank 4695 · last release 2023-03-10 · [PyPI](https://pypi.org/project/gitlint-core/) · [docs](https://jorisroovers.github.io/gitlint) · [source](https://github.com/jorisroovers/gitlint/tree/main/gitlint-core)

<details><summary>README extract</summary>

Git commit message linter written in python, checks your commit messages for style.

See jorisroovers.github.io/gitlint for full documentation.

Sections: Gitlint-core, gitlint: jorisroovers.github.io/gitlint

</details>

### validate-pyproject

Validation library and CLI tool for checking on 'pyproject.toml' files using JSON Schema

`pip install validate-pyproject` · installs (wheel) · licence: MPL-2.0 and MIT and BSD-3-Clause · rank 4761 · last release 2026-10-22 · [PyPI](https://pypi.org/project/validate-pyproject/) · [docs](https://validate-pyproject.readthedocs.io/) · [source](https://github.com/abravalheri/validate-pyproject)

<details><summary>README extract</summary>

Automated checks on `pyproject.toml` powered by JSON Schema definitions

With the approval of PEP 517 and PEP 518, the Python community shifted
towards a strong focus on standardisation for packaging software, which allows
more freedom when choosing tools during development and make sure packages
created using different technologies can ...

Example:
```python
# in your python code
from validate_pyproject import api, errors

# let's assume that you have access to a `loads` function
# responsible for parsing a string representing the TOML file
# (you can check the `toml` or `tomli` projects for that)
pyproject_as_dict = loads(pyproject_toml_str)

# now we can use validate-pyproject
...
```

Sections: validate-pyproject, Description, Usage, Plugins, pre-commit / prek, Note

</details>

### cpplint

Check C++ files configurably against Google's style guide

`pip install cpplint` · installs (wheel) · licence: Freely Distributable; BSD License · rank 4797 · last release 2025-04-08 · [PyPI](https://pypi.org/project/cpplint/)

<details><summary>README extract</summary>

Cpplint is a command-line tool to check C/C++ files for style issues according to Google's C++ style guide.

Cpplint used to be developed and maintained by Google Inc. at google/styleguide. ...

Sections: cpplint - static code checker for C++, Usage, Changes, Former

</details>

### nbqa

Run any standard Python code quality tool on a Jupyter Notebook

`pip install nbqa` · installs (wheel) · licence: MIT · rank 4802 · last release 2026-11-07 · [PyPI](https://pypi.org/project/nbqa/) · [docs](https://nbQA.readthedocs.io/en/latest/) · [source](https://github.com/nbQA-dev/nbQA)

<details><summary>README extract</summary>

- ✅ handles IPython magics robustly
- ✅ respects your config files
- ✅ preserves "quiet mode" trailing semicolons
- ✅ lints both code and markdown cells

Sections: 🚀 Examples, Command-line, Pre-commit, 🥳 Used by, 💬 Testimonials

</details>

### clang-tidy

Clang-tidy is an LLVM-based code analyser tool

`pip install clang-tidy` · installs (wheel) · licence: Apache Software License · rank 4866 · last release 2026-10-26 · [PyPI](https://pypi.org/project/clang-tidy/) · [docs](https://clang.llvm.org/extra/clang-tidy/index.html#clang-tidy) · [source](https://github.com/ssciwr/clang-tidy-wheel)

<details><summary>README extract</summary>

This project packages the `clang-tidy` utility and related tools as a Python package. It allows you to install `clang-tidy` directly from PyPI:

The tools provided are:
- `clang-tidy`: lints C++ source code using configurable rules
- `clang-apply-replacements`: applies "fixes" that have been exported by `clang-tidy` in YAML format ...

Sections: clang-tidy Python distribution, Use with pipx, Troubleshooting

</details>

### eradicate

Removes commented-out code.

`pip install eradicate` · installs (wheel) · licence: MIT License · rank 4945 · last release 2025-10-27 · [PyPI](https://pypi.org/project/eradicate/)

<details><summary>README extract</summary>

`eradicate` removes commented-out code from Python files.

With modern revision control available, there is no reason to save
commented-out code to your repository. `eradicate` helps cleans up
existing junk comments. It does this by detecting block comments that
contain valid Python syntax that are likely to be commented out code. ...

Example:
```python
# import os
# from foo import junk
# a = 3
a = 4
# foo(1, 2, 3)

def foo(x, y, z):
    # print('hello')
    print(x, y, z)

    # This is a real comment.
    #return True
    return False
```

Sections: eradicate, Introduction, Example, Whitelisting, Related

</details>

### bindep

Binary dependency utility

`pip install bindep` · installs (wheel) · licence: Apache Software License · rank 5056 · last release 2026-03-19 · [PyPI](https://pypi.org/project/bindep/) · [docs](https://docs.opendev.org/opendev/bindep)

<details><summary>README extract</summary>

Bindep is a tool for checking the presence of binary packages needed to
use an application / library. It started life as a way to make it easier to set
up a development environment for OpenStack projects. ...

Sections: Introduction, Basics, Profiles, Writing Requirements Files, CLI Exit Codes, Examples

</details>

### pytest-variables

pytest plugin for providing variables to tests/fixtures

`pip install pytest-variables` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5066 · last release 2024-02-01 · [PyPI](https://pypi.org/project/pytest-variables/) · [source](https://github.com/pytest-dev/pytest-variables)

<details><summary>README extract</summary>

pytest-variables is a plugin for pytest that provides variables to
tests/fixtures as a dictionary via a file specified on the command line.

You will need the following prerequisites in order to use pytest-variables:

- Python 3.8+ or PyPy3

Example:
```python
def test_foo(self, variables):
    assert variables['foo'] == 'bar'
    assert variables.get('bar') == 'foo'
    assert variables.get('missing') is None
```

Sections: pytest-variables, Requirements, Additional formats, Human JSON, YAML, YAML Loader, TOML, Specifying variables, Accessing variables, Resources

</details>

### robotframework-robocop

Static code analysis tool (linter) and code formatter for Robot Framework

`pip install robotframework-robocop` · installs (wheel) · licence: Apache Software License · rank 5090 · last release 2026-11-07 · [PyPI](https://pypi.org/project/robotframework-robocop/) · [docs](https://robocop.dev/) · [source](https://github.com/MarketSquare/robotframework-robocop)

<details><summary>README extract</summary>

- Introduction
- Documentation
- Requirements
- Installation
- Usage
- Example Output
- MCP Server
- Values
- FAQ

Robocop is a tool that performs static code analysis and formatting of Robot Framework code. ...

Sections: Robocop, Introduction, Documentation, Requirements, Usage, Example Output, MCP Server, Values, FAQ

</details>

### crosshair-tool

Analyze Python code for correctness using symbolic execution.

`pip install crosshair-tool` · installs (wheel) · licence: MIT · rank 5114 · last release 2026-11-05 · [PyPI](https://pypi.org/project/crosshair-tool/)

<details><summary>README extract</summary>

An analysis tool for Python that blurs the line between testing and
type systems.

> _THE LATEST NEWS:_
Python's most popular property-based testing tool,
Hypothesis,
now supports running CrossHair as an
optional backend! ...

Sections: CrossHair, Documentation

</details>

### dodgy

Dodgy: Searches for dodgy looking lines in Python code

`pip install dodgy` · installs (wheel) · licence: MIT License · rank 5290 · last release 2019-12-31 · [PyPI](https://pypi.org/project/dodgy/)

### pylint-per-file-ignores

A pylint plugin to ignore error codes per file.

`pip install pylint-per-file-ignores` · installs (wheel) · licence: MIT · rank 5391 · last release 2026-09-28 · [PyPI](https://pypi.org/project/pylint-per-file-ignores/)

<details><summary>README extract</summary>

This pylint plugin will enable per-file-ignores in your project!

The project was initially created by christopherpickering.

Sections: Pylint Per File Ignores, Add to Pylint Settings, Usage, Build and Publish, Licensing

</details>

### lcov-cobertura

LCOV to Cobertura XML converter

`pip install lcov-cobertura` · installs (wheel) · licence: Apache Software License · rank 5454 · last release 2025-02-22 · [PyPI](https://pypi.org/project/lcov-cobertura/)

<details><summary>README extract</summary>

This project does as the name implies: it converts code coverage report files in lcov format to Cobertura's XML report format so that CI servers like Jenkins can aggregate results and determine build stability etc.

Coverage metrics supported: ...

Example:
```python
from lcov_cobertura import LcovCobertura

LCOV_INPUT = 'SF:foo/file.ext\nDA:1,1\nDA:2,0\nend_of_record\n'
converter = LcovCobertura(LCOV_INPUT)
cobertura_xml = converter.convert()
print(cobertura_xml)
```

Sections: lcov to cobertura XML converter, Quick usage, With pip, Command-line usage, Usage as a Python module

</details>

### shfmt-py

Installs the shfmt shell script formatter binary, plus a ready-made pre-commit hook

`pip install shfmt-py` · installs (wheel) · licence: MIT AND BSD-3-Clause · rank 5469 · last release 2026-09-07 · [PyPI](https://pypi.org/project/shfmt-py/)

<details><summary>README extract</summary>

`pip install shfmt-py` puts [shfmt], the shell script formatter, on the `PATH` of your Python
environment and gives you a ready-made [pre-commit] hook.

This is packaging only — no patches, no Python API, nothing to `import`, no `python -m shfmt`. ...

Sections: shfmt-py, Pre-commit hook, Overriding args, EditorConfig, Command line, Versioning, FAQ, Issues

</details>

### gitlint

Git commit message linter written in python, checks your commit messages for style.

`pip install gitlint` · installs (wheel) · licence: MIT License · rank 5484 · last release 2023-03-10 · [PyPI](https://pypi.org/project/gitlint/) · [docs](https://jorisroovers.github.io/gitlint) · [source](https://github.com/jorisroovers/gitlint)

<details><summary>README extract</summary>

Git commit message linter written in python, checks your commit messages for style.

See jorisroovers.github.io/gitlint for full documentation.

</details>

### pytest-selenium

pytest plugin for Selenium

`pip install pytest-selenium` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5540 · last release 2024-02-01 · [PyPI](https://pypi.org/project/pytest-selenium/) · [source](https://github.com/pytest-dev/pytest-selenium)

<details><summary>README extract</summary>

pytest-selenium is a plugin for pytest that provides
support for running Selenium based tests.

- Documentation
- Issue Tracker
- Code

Sections: pytest-selenium, Resources

</details>

### taplo

A CLI for Taplo TOML toolkit

`pip install taplo` · installs (wheel) · licence: MIT License · rank 5740 · last release 2024-08-19 · [PyPI](https://pypi.org/project/taplo/) · [source](https://github.com/tamasfe/taplo)

<details><summary>README extract</summary>

A command line tool for linting and formatting TOML files.

More information on the website

</details>

### pytest-ansible

Plugin for pytest to simplify calling ansible modules from tests or fixtures

`pip install pytest-ansible` · installs (wheel) · licence: MIT License · rank 5799 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pytest-ansible/) · [docs](https://github.com/ansible/pytest-ansible) · [source](https://github.com/ansible/pytest-ansible)

<details><summary>README extract</summary>

I've made the difficult decision to deprecate myself.

My first commit was 25 July 2014 — a small pytest plugin so you could aim
Ansible at inventory from inside a test function and get something friendlier
than shell soup. ...

Features:
pytest-ansible runs each scenario as a separate `molecule test -s <scenario>`
subprocess. That only works for standalone scenarios. ...

Example:
```python
# tests/conftest.py — copy into your repo
from future import annotations

import json
import subprocess

def inventory_hosts(inventory: str = "inventory") -> list[str]:
    data = json.loads(
        subprocess.check_output(
            ["ansible-inventory", "-i", inventory, "--list"],
            text=True,
        )
    )
...
```

...

</details>

### allure-behave

Allure behave integration

`pip install allure-behave` · installs (wheel) · licence: Apache Software License · rank 5834 · last release 2026-09-29 · [PyPI](https://pypi.org/project/allure-behave/) · [docs](https://allurereport.org/docs/behave/) · [source](https://github.com/allure-framework/allure-python)

<details><summary>README extract</summary>

> An Allure adapter for Behave.

[]( "Allure Report")

- Learn more about Allure Report at
- 📚 Documentation – discover official documentation for Allure Report
- ❓ Questions and Support – get help from the team and community
- 📢 Official announcements – stay updated with our latest news and updates ...

Sections: Allure Behave Formatter, Quick start, Further readings

</details>

### fixtures

Fixtures, reusable state for writing clean tests and more.

`pip install fixtures` · installs (wheel) · licence: Apache Software License; BSD License · rank 5912 · last release 2026-03-25 · [PyPI](https://pypi.org/project/fixtures/) · [source](https://github.com/testing-cabal/fixtures)

<details><summary>README extract</summary>

Features:
Standard Python `unittest` provides no obvious method for making and reusing
state needed in a test case other than by adding a method on the test class. ...

Example:
```python
>>> import unittest
>>> import fixtures
>>> class NoddyFixture(fixtures.Fixture):
...     def _setUp(self):
...         self.frobnozzle = 42
...         self.addCleanup(delattr, self, 'frobnozzle')
```

Sections: Dependencies, Why Fixtures, About Fixtures, Creating Fixtures, The Fixture API, Errors in setUp, Shared Dependencies, `ByteStream`, `EnvironmentVariable`, `FakeLogger`, `FakePopen`, `LogHandler`, `MockPatchObject`, `MockPatch`

</details>

### pytest-parallel

a pytest plugin for parallel and concurrent testing

`pip install pytest-parallel` · installs (wheel) · licence: MIT License · rank 6100 · last release 2021-10-10 · [PyPI](https://pypi.org/project/pytest-parallel/)

<details><summary>README extract</summary>

a pytest plugin for parallel and concurrent testing

This plugin makes it possible to run tests quickly using multiprocessing (parallelism) and multithreading (concurrency).

Features:
`pytest-xdist` is great to run tests that:
 1. aren't threadsafe
 2. perform poorly when multithreaded
 3. need state isolation

`pytest-parallel` is better for some use cases (like Selenium tests) that:
 1. can be threadsafe
 2. ...

Sections: pytest-parallel, What?, Why?, Requirements, Options, Examples, Notice

</details>

### pytest-md-report

A pytest plugin to generate test outcomes reports with markdown table format.

`pip install pytest-md-report` · installs (wheel) · licence: MIT License · rank 6194 · last release 2026-05-04 · [PyPI](https://pypi.org/project/pytest-md-report/) · [source](https://github.com/thombashi/pytest-md-report)

<details><summary>README extract</summary>

A pytest plugin to generate test outcomes reports with markdown table format.

Example:
```python
import pytest

@pytest.mark.id("TC-001")
@pytest.mark.priority("high")
def test_alpha():
    assert True

@pytest.mark.id("TC-002")
@pytest.mark.priority("low")
def test_beta():
    assert True
```

Sections: Summary, Usage, Other examples, Config file examples, Add report to pull requests, Add report to pull requests: only failed tests, Options, Command options, ini-options, Dependencies

</details>

### rstcheck

Checks syntax of reStructuredText and code blocks nested within it

`pip install rstcheck` · installs (wheel) · licence: MIT · rank 6322 · last release 2026-07-28 · [PyPI](https://pypi.org/project/rstcheck/) · [docs](https://rstcheck.readthedocs.io/en/latest/) · [source](https://github.com/rstcheck/rstcheck)

<details><summary>README extract</summary>

+-------------------+---------------------------------------------------------------------------------------------+
| General maintenance_ylicensesemver
| ...

Example:
```python
With bad C++ syntax:

# ```rst
# Test
.. code:: cpp

    int main()
    {
        return x;
    }
```

Sections: rstcheck, Pre-commit Hook with Extras, Examples, ```rst, Test

</details>

### pylint-pytest

A Pylint plugin to suppress pytest-related false positives.

`pip install pylint-pytest` · installs (wheel) · licence: MIT License · rank 6334 · last release 2026-09-29 · [PyPI](https://pypi.org/project/pylint-pytest/) · [docs](https://github.com/pylint-dev/pylint-pytest#readme) · [source](https://github.com/pylint-dev/pylint-pytest)

<details><summary>README extract</summary>

A Pylint plugin to suppress pytest-related false positives.

Example:
```python
def test_something(conftest_fixture):  # <- Unused argument 'conftest_fixture'
    assert True
```

Sections: pylint-pytest, Usage, Suppressed Pylint Warnings, `unused-argument`, `unused-import`, `redefined-outer-name`, `no-member`, Raise new warning(s), W6401 `deprecated-pytest-yield-fixture`, W6402 `useless-pytest-mark-decorator`, W6403 `deprecated-positional-argument-for-pytest-fixture`, F6401 `cannot-enumerate-pytest-fixtures`

</details>

### pytest-pytestrail

Pytest plugin for interaction with TestRail

`pip install pytest-pytestrail` · installs (wheel) · licence: MIT License · rank 6468 · last release 2020-08-27 · [PyPI](https://pypi.org/project/pytest-pytestrail/)

<details><summary>README extract</summary>

Pytest plugin for interaction with TestRail

Example:
```python
from pytest_pytestrail import pytestrail

@pytestrail.case('C32')
def test_one():
    assert True

@pytestrail.case('C12')
def test_two():
    assert True
```

Sections: pytest-pytestrail, Example, Steps, Steps parametrize, Configuration, Config file, Command line options

</details>

### pysonar

Sonar Scanner for the Python Ecosystem

`pip install pysonar` · installs (wheel) · licence: LGPL-3.0-only · rank 6501 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pysonar/) · [source](https://github.com/SonarSource/sonar-scanner-python)

_README extract left out: share-alike licence._

### testresources

Testresources, a pyunit extension for managing expensive test resources

`pip install testresources` · installs (wheel) · licence: Apache Software License; BSD License · rank 6647 · last release 2026-04-21 · [PyPI](https://pypi.org/project/testresources/) · [source](https://github.com/testing-cabal/testresources)

<details><summary>README extract</summary>

testresources extends `unittest` with a clean and simple API to provide test
optimisation where expensive common resources are needed for test cases - for
example sample working trees for VCS systems, reference databases for
enterprise applications, or web servers ... let your imagination run wild.

Example:
```python
import shutil
import tempfile
import testresources

class TemporaryDirectoryResource(testresources.TestResourceManager):

    def make(self, dependency_resources):
        return tempfile.mkdtemp()

    def clean(self, resource):
        shutil.rmtree(resource)

    def isDirty(self, resource):
...
```

...

</details>

### tox-ansible

A radical approach to testing ansible content

`pip install tox-ansible` · installs (wheel) · licence: MIT · rank 6676 · last release 2026-11-05 · [PyPI](https://pypi.org/project/tox-ansible/) · [docs](https://ansible.readthedocs.io/projects/tox-ansible/) · [source](https://github.com/ansible/tox-ansible)

<details><summary>README extract</summary>

`tox-ansible` is a utility designed to simplify the testing of Ansible content collections.

Implemented as a `tox` plugin, `tox-ansible` provides a simple way to test Ansible content collections across multiple Python interpreters and Ansible versions.

`tox-ansible` uses familiar python testing tools to perform the actual testing. ...

Sections: tox-ansible, Introduction, Talk to us, Usage, Configuration, Note to version 1.x users

</details>

### testscenarios

Testscenarios, a unittest extension for dependency injection

`pip install testscenarios` · installs (wheel) · licence: Apache Software License; BSD License · rank 6879 · last release 2026-08-28 · [PyPI](https://pypi.org/project/testscenarios/) · [source](https://github.com/testing-cabal/testscenarios)

<details><summary>README extract</summary>

testscenarios provides clean dependency injection for python unittest style
tests. This can be used for interface testing (testing many implementations via
a single test suite) or for classic dependency injection (provide tests with
dependencies externally to the test code itself, allowing easy testing in
different situations).

Features:
`unittest` provides on obvious method for running a single `test_foo`
method with two (or more) scenarios: by creating a mix-in that
provides the functions, objects or settings that make up the scenario. This is
however limited and unsatisfying. ...

Example:
```python
>>> import unittest
>>> from io import StringIO
>>> from testscenarios.scenarios import generate_scenarios
```

...

</details>

### requirements-detector

Python tool to find and list requirements of a Python project

`pip install requirements-detector` · installs (wheel) · licence: MIT License · rank 6886 · last release 2026-08-11 · [PyPI](https://pypi.org/project/requirements-detector/)

<details><summary>README extract</summary>

Example:
```python
>>> import os
>>> from requirements_detector import find_requirements
>>> find_requirements(os.getcwd())
[DetectedRequirement:Django==1.5.2, DetectedRequirement:South>=0.8, ...]
```

Sections: Requirements Detector, About, Usage, Output, Usage From Python

</details>

### rstcheck-core

Checks syntax of reStructuredText and code blocks nested within it

`pip install rstcheck-core` · installs (wheel) · licence: MIT · rank 7013 · last release 2026-08-23 · [PyPI](https://pypi.org/project/rstcheck-core/) · [docs](https://rstcheck-core.readthedocs.io/en/latest/) · [source](https://github.com/rstcheck/rstcheck-core)

### pytest-loop

pytest plugin for looping tests

`pip install pytest-loop` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7045 · last release 2024-10-17 · [PyPI](https://pypi.org/project/pytest-loop/) · [source](https://github.com/anogowski/pytest-loop.git)

<details><summary>README extract</summary>

pytest-loop is a plugin for pytest that makes it
easy to loop a single test, or multiple tests, a specific number of times or for a certain duration of time.
This plugin merges pytest-repeat and pytest-stress with a fix for test results.

You will need the following prerequisites in order to use pytest-loop:
- Python 3.7+ or PyPy ...

Example:
```python
import pytest

@pytest.mark.loop(3)
def test_loop_decorator():
    pass
```

Sections: pytest-loop, Requirements, Usage, Iterative Loop, Time based loop, looping a test until failure, UnitTest Style Tests, Resources

</details>

### code-review-graph

Local-first knowledge graph for token-efficient code review through MCP and CLI

`pip install code-review-graph` · installs (wheel) · licence: MIT · rank 7165 · last release 2026-09-18 · [PyPI](https://pypi.org/project/code-review-graph/) · [docs](https://github.com/tirth8205/code-review-graph/blob/main/docs/INDEX.md) · [source](https://github.com/tirth8205/code-review-graph)

<details><summary>README extract</summary>

A local code knowledge graph that gives AI coding tools precise review context over MCP.

 English |
 简体中文 |
 日本語 |
 한국어 |
 हिन्दी

 Usage ·
 Commands ·
 FAQ ·
 Troubleshooting ·
 GitHub Action ·
 Reproducing the benchmarks ·
 Roadmap

AI coding tools often re-read large parts of a codebase to review a change. ...

Features:
| Feature | Details |

| Incremental updates | Re-parses only files whose hash changed. On a ~3,000-file repo a two-file edit takes ~2.5 s on the hook path (measured). |
| Language and notebook support | See Language coverage above. ...

...

</details>

### prospector

Prospector is a tool to analyse Python code by aggregating the result of other tools.

`pip install prospector` · installs (wheel) · licence: GPL-2.0-or-later · rank 7166 · last release 2026-10-26 · [PyPI](https://pypi.org/project/prospector/) · [source](https://github.com/prospector-dev/prospector)

_README extract left out: share-alike licence._

### bzt

Taurus Tool for Continuous Testing

`pip install bzt` · installs (wheel) · licence: Apache Software License · rank 7241 · last release 2026-10-26 · [PyPI](https://pypi.org/project/bzt/)

<details><summary>README extract</summary>

Quick links: Taurus Documentation | Knowledge Base | GitHub Issues

Hides the complexity of performance and functional tests with an automation-friendly convenience wrapper. Taurus relies on JMeter, Gatling, Locust.io, and Selenium WebDriver as its underlying tools. Free and open source under Apache 2.0 License.

Sections: Taurus, Purpose, Getting Started

</details>

### eyes-selenium

Applitools Python SDK. Selenium package

`pip install eyes-selenium` · installs (wheel) · licence: LicenseRef-Proprietary · rank 7302 · last release 2026-11-05 · [PyPI](https://pypi.org/project/eyes-selenium/)

<details><summary>README extract</summary>

Applitools Eyes SDK For Images and Selenium/Appium WebDrivers
Proxy package that additionally installs `selenium` and `Appium-Python-Client` packages.

Change log.

Sections: Applitools Eyes Python SDK, Usage

</details>

### ansible-navigator

A text-based user interface (TUI) for the Red Hat Ansible Automation Platform

`pip install ansible-navigator` · installs (wheel) · licence: Apache Software License · rank 7341 · last release 2026-11-05 · [PyPI](https://pypi.org/project/ansible-navigator/) · [docs](https://ansible-navigator.readthedocs.io/en/latest/) · [source](https://github.com/ansible/ansible-navigator)

<details><summary>README extract</summary>

A text-based user interface (TUI) for Ansible.

A demo of the interface can be found on YouTube.

Refer to the
Talk to us
section of the Contributing guide to find out how to get in touch with us.

You can also find more information in the
Ansible communication guide.

Sections: ansible-navigator, Communication, Quick start, Welcome, Output modes, Example commands, Configuring ansible-navigator, Frequently Asked Questions (FAQ)

</details>

### eyes-common

Applitools Python SDK. Common code package

`pip install eyes-common` · installs (wheel) · licence: LicenseRef-Proprietary · rank 7342 · last release 2026-11-05 · [PyPI](https://pypi.org/project/eyes-common/)

<details><summary>README extract</summary>

Applitools Eyes SDK For Images and Playwright
Proxy package that additionally installs `playwright` package.

Change log.

Sections: Applitools Eyes Python SDK, Usage

</details>

### core-universal

Applitools Eyes Core SDK Server

`pip install core-universal` · does not install on CPython 3.14 · licence: Applitools SDK License · rank 7701 · last release 2024-06-17 · [PyPI](https://pypi.org/project/core-universal/) · [source](https://github.com/applitools/eyes.sdk.javascript1/tree/master/js/packages/core)

<details><summary>README extract</summary>

This package contains Applitools Eyes Core SDK Server binary.

Check project repository and Core Changelog for more information.

</details>

### ansible-sign

Ansible content validation library and CLI

`pip install ansible-sign` · installs (wheel) · licence: MIT · rank 7725 · last release 2026-06-30 · [PyPI](https://pypi.org/project/ansible-sign/) · [docs](https://ansible.readthedocs.io/projects/sign/) · [source](https://github.com/ansible/ansible-sign)

<details><summary>README extract</summary>

This is a library and auxiliary CLI tool for dealing with Ansible content
verification.

It does the following:

- checksum manifest generation and validation (sha256sum)
- GPG detached signature generation and validation (using python-gnupg) for
 content ...

</details>

### collate-sqlfluff

The SQL Linter for Humans

`pip install collate-sqlfluff` · installs (wheel) · licence: MIT License · rank 7891 · last release 2026-05-28 · [PyPI](https://pypi.org/project/collate-sqlfluff/) · [docs](https://docs.sqlfluff.com) · [source](https://github.com/open-metadata/collate-sqlfluff)

<details><summary>README extract</summary>

SQLFluff is a dialect-flexible and configurable SQL linter. Designed
with ELT applications in mind, SQLFluff also works with Jinja templating
and dbt. SQLFluff will auto-fix most linting errors, allowing you to focus
your time on what matters.

Sections: The SQL Linter for Humans, VS Code Extension, Getting Started, Documentation, SQLFluff on Slack, SQLFluff on Twitter

</details>

### pytest-gremlins

Fast-first mutation testing for pytest. Let the gremlins loose, see which ones survive.

`pip install pytest-gremlins` · installs (wheel) · licence: MIT License · rank 8233 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pytest-gremlins/) · [docs](https://pytest-gremlins.readthedocs.io) · [source](https://github.com/mikelane/pytest-gremlins)

<details><summary>README extract</summary>

Fast-first mutation testing for pytest. Speed that makes mutation testing practical for everyday TDD.

> *Let the gremlins loose. See which ones survive.*

Features:
- Speed-First Architecture - Mutation switching eliminates file I/O and module reloads. Run
 gremlins in seconds, not hours.
- Native pytest Integration - Zero configuration to start. Just add `--gremlins` to your pytest
 command. ...

Sections: pytest-gremlins, Key Features, Quick Start, Why pytest-gremlins?, The Problem with Existing Tools, Our Solution: Speed Through Architecture, Performance, Example Output, Configuration, The Gremlins Theme, Documentation, Related Projects

</details>

### code-standards

One deterministic quality gate for Sarj Python, TypeScript, Swift, Kotlin, shell, SQL, IaC, and repository policy.

`pip install code-standards` · installs (wheel) · licence: MIT · rank 8441 · last release 2026-11-08 · [PyPI](https://pypi.org/project/code-standards/) · [docs](https://code-standards.sarj.ai/cli/) · [source](https://github.com/sarj-ai/code-standards)

<details><summary>README extract</summary>

<!-- Generated by `code-standards maintain docs sync`; do not edit. -->

One deterministic quality gate for Sarj Python, TypeScript, Swift, Kotlin, shell, SQL, IaC, and repository policy.

Adopt the repository once with `code-standards setup`. ...

</details>

### pytest-cpp

Use pytest's runner to discover and execute C++ tests

`pip install pytest-cpp` · installs (wheel) · licence: MIT License · rank 8669 · last release 2024-09-18 · [PyPI](https://pypi.org/project/pytest-cpp/)

<details><summary>README extract</summary>

Use pytest runner to discover and execute C++ tests.

Supports Google Test,
Boost.Test,
and Catch2:

This brings several benefits:

* Allows you to run all your tests in multi-language projects with a single
 command;
* Execute C++ tests in parallel using
 pytest-xdist plugin;
* Use `--junitxml` option to produce a single and uniform xml file with ...

Sections: pytest-cpp, Usage, Configuration Options, cpp_files, cpp_arguments, cpp_ignore_py_files, cpp_harness, cpp_harness_collect

</details>

### robotframework-appiumlibrary

Robot Framework Mobile app testing library for Appium Client Android & iOS & Web

`pip install robotframework-appiumlibrary` · installs (wheel) · licence: Apache-2.0 · rank 8678 · last release 2025-12-15 · [PyPI](https://pypi.org/project/robotframework-appiumlibrary/) · [docs](https://github.com/serhatbolsu/robotframework-appiumlibrary?tab=readme-ov-file#appium-library-for-robotframework)

<details><summary>README extract</summary>

AppiumLibrary is an appium testing library for Robot Framework. Library can be downloaded from PyPI.

It uses Appium to communicate with Android and iOS application
similar to how *Selenium WebDriver* talks to web browser.

It is supporting Python 3.9+ and Appium Python Client 5.1.1+ ...

Sections: Appium library for RobotFramework, Introduction, Keyword Documentation, Device Setup, Usage

</details>

### pyscn

An intelligent Python code quality analyzer with architectural guidance

`pip install pyscn` · installs (wheel) · licence: MIT License · rank 8764 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pyscn/)

<details><summary>README extract</summary>

English | 日本語 | 简体中文 | Français

Code quality analysis for Python in the age of AI coding.

Building with Cursor, Claude, or ChatGPT? pyscn keeps AI-generated code maintainable with structural analysis.

Features:
One command scores your whole codebase (0-100 with an A-F grade) and generates an HTML report that shows what to fix first.

pyscn looks at your code from five angles:

- 🧹 Dead code - unreachable code you can safely delete ...

Sections: Quick Start, Demo, Features, Other Languages, Polyscan for GitHub, AI Agent Integration, Agent Skills (Recommended), MCP Server (Optional), Build from source, Common Commands, `pyscn analyze`, `pyscn check`, `pyscn init`, Configuration

</details>

### robotframework-tidy

Code autoformatter for Robot Framework

`pip install robotframework-tidy` · installs (wheel) · licence: Apache Software License · rank 8986 · last release 2025-07-03 · [PyPI](https://pypi.org/project/robotframework-tidy/)

<details><summary>README extract</summary>

- Introduction
- Documentation
- Requirements
- Installation
- Usage
- Example

DEPRECATION NOTICE

Starting from Robocop 6.0, Robotidy is part of Robocop as formatter.

If you are new users, please use instead.

Introduction

Robotidy is a tool for autoformatting Robot Framework code. ...

</details>

### qase-python-commons

A library for Qase TestOps and Qase Report

`pip install qase-python-commons` · installs (wheel) · licence: Apache Software License · rank 9112 · last release 2026-10-30 · [PyPI](https://pypi.org/project/qase-python-commons/)

<details><summary>README extract</summary>

Core library for all Qase Python reporters. Contains the complete configuration reference.

Sections: Qase Python Commons, About, Reporters, Configuration, Configuration Priority, Reporter Modes, Common Options, TestOps Options (Single Project), TestOps Multi Options (Multiple Projects), Local Report Options, Logging Options, Framework-Specific Options, Pytest, Behave, Robot Framework, Tavern

</details>

### slotscheck

Ensure your __slots__ are working properly.

`pip install slotscheck` · installs (wheel) · licence: MIT · rank 9275 · last release 2026-09-06 · [PyPI](https://pypi.org/project/slotscheck/) · [source](https://github.com/ariebovenberg/slotscheck)

<details><summary>README extract</summary>

Adding `slots` to a class in Python is a great way to improve performance.
But to work properly, all base classes need to implement it — without overlap!
It's easy to get wrong, and what's worse: there is nothing warning you that you messed up.

✨ *Until now!* ✨

`slotscheck` helps you validate your slots are working properly. ...

Features:
- Detect broken slots inheritance
- Detect overlapping slots
- Detect duplicate slots
- Pre-commit hook
- (Optionally) enforce the use of slots

See the documentation for more details
and configuration options.

Sections: 🎰 Slotscheck, Quickstart, Features, Why not a flake8 plugin?, Why not pylint or ruff?, Notes

</details>

### robotframework-faker

Robot Framework wrapper for faker, a fake test data generator

`pip install robotframework-faker` · installs (wheel) · licence: MIT License · rank 9355 · last release 2025-07-18 · [PyPI](https://pypi.org/project/robotframework-faker/)

<details><summary>README extract</summary>

Robot Framework keyword library wrapper for
Faker.

This module allows easy use of Faker's random test data generation in
Robot Framework. I hate using static test data, because inevitably the
system under test evolves to pass the tests without necessarily solving
the root cause of bugs. ...

Sections: robotframework-faker, Faker package dependency, Usage

</details>

### pylint-flask

pylint-flask is a Pylint plugin to aid Pylint in recognizing and understanding errors caused when using Flask

`pip install pylint-flask` · installs from source (sdist only) · licence: GPLv2 · rank 9374 · last release 2019-01-30 · [PyPI](https://pypi.org/project/pylint-flask/)

_README extract left out: share-alike licence._

### pydocstringformatter

A tool to automatically format Python docstrings that tries to follow recommendations from PEP 8 and PEP 257.

`pip install pydocstringformatter` · installs (wheel) · licence: MIT License · rank 9652 · last release 2026-07-04 · [PyPI](https://pypi.org/project/pydocstringformatter/) · [source](https://github.com/DanielNoord/pydocstringformatter)

<details><summary>README extract</summary>

A tool to automatically format Python docstrings to follow recommendations from
`PEP 8` and
`PEP 257` (or other supported style
guides.)

See What it does for currently supported auto-formatting.

Rationale

This project is heavily inspired by
`docformatter`. ...

Features:
The following examples show some of the changes pydocstringformatter will apply. For a
full overview of all potential changes you can check out the
`Usage` page which
shows an up to date list of all formatters and their description.

Sections: Pydocstringformatter, Usage, Configuration, Style, Pre-commit, What it does

</details>

### qase-pytest

Qase Pytest Plugin for Qase TestOps and Qase Report

`pip install qase-pytest` · installs (wheel) · licence: Apache Software License · rank 9663 · last release 2026-10-30 · [PyPI](https://pypi.org/project/qase-pytest/) · [docs](https://developers.qase.io) · [source](https://github.com/qase-tms/qase-python/tree/main/qase-pytest)

<details><summary>README extract</summary>

Qase Pytest Reporter enables seamless integration between your Pytest tests and Qase TestOps, providing automatic test result reporting, test case management, and comprehensive test analytics.

Features:
- Link automated tests to Qase test cases by ID
- Auto-create test cases from your test code
- Report test results with rich metadata (fields, attachments, steps)
- Support for parameterized tests
- Multi-project reporting support ...

Example:
```python
from qase.pytest import qase

@qase.id(1)
def test_example():
    assert True
```

Sections: Qase TestOps Pytest Reporter, Features, Quick Start, Upgrading, Configuration, Minimal Configuration, Example `qase.config.json`, Usage, Link Tests with Test Cases, Add Metadata, Ignore Tests, Attachments, Test Steps, Running Tests

</details>

### enola-cli

Architectural regression testing for AI-assisted development

`pip install enola-cli` · installs (wheel) · licence: Apache-2.0 · rank 9768 · last release 2026-11-06 · [PyPI](https://pypi.org/project/enola-cli/) · [docs](https://github.com/enola-labs/enola/blob/main/docs/README.md) · [source](https://github.com/enola-labs/enola)

<details><summary>README extract</summary>

Architectural regression testing for AI-assisted development.

Catch structural regressions that builds and tests cannot see: new dependency
cycles, violated layer boundaries, undeclared service dependencies, and changes
that spread beyond their intended scope.

Enola maps your codebase before a change and compares it with the structure
afterward. ...

Sections: enola, Try it read-only, Documentation

</details>

### tox-toml-fmt

Format tox.toml files

`pip install tox-toml-fmt` · installs (wheel) · licence: MIT · rank 10042 · last release 2026-11-04 · [PyPI](https://pypi.org/project/tox-toml-fmt/) · [docs](https://tox-toml-fmt.readthedocs.io/en/latest/) · [source](https://github.com/tox-dev/toml-fmt/tree/main/tox-toml-fmt)

<details><summary>README extract</summary>

`tox-toml-fmt` formats `tox.toml` files without discarding comments. It uses a small configuration surface to keep
results stable across projects. See the
release history for version changes.

Example:
```python
from tox_toml_fmt import run

exit_code = run(["path/to/tox.toml"])
```

Sections: tox-toml-fmt, Pre-commit, Python API, Project settings, Shared settings, Spacing, String wrapping, Command-line interface, General Formatting, String Quotes, Key Quotes, Array Formatting, String Wrapping, Table Formatting

</details>

### stestr

A parallel Python test runner built around subunit

`pip install stestr` · installs (wheel) · licence: Apache-2.0 · rank 10164 · last release 2026-02-20 · [PyPI](https://pypi.org/project/stestr/) · [docs](https://stestr.readthedocs.io) · [source](https://github.com/mtreinish/stestr)

<details><summary>README extract</summary>

* Read this in other languages: English, 日本語

Features:
stestr is parallel Python test runner designed to execute unittest test
suites using multiple processes to split up execution of a test suite. ...

Sections: stestr, Overview, Using stestr, Migrating from testrepository, Building a manpage, stestr on OFTC

</details>

### capt-hook

Stop repeating yourself to Claude.

`pip install capt-hook` · installs (wheel) · licence: PolyForm-Noncommercial-1.0.0 · rank 10191 · last release 2026-11-07 · [PyPI](https://pypi.org/project/capt-hook/) · [docs](https://yasyf.github.io/captain-hook/) · [source](https://github.com/yasyf/captain-hook)

<details><summary>README extract</summary>

Stop repeating yourself to Claude. captain-hook mines your transcripts for the corrections you keep giving and opens PRs that turn each one into a typed, tested Python hook.

The formula fills the Cellar and `helper install` deploys the fixed, signed host at
`~/Applications/Captain Hook.app`; `init` scaffolds
`.claude/hooks/`, wires Claude Code's ...

Example:
```python
# .claude/hooks/safety.py
from captain_hook import Allow, Block, Input, block_command

block_command(
    ["git", "push", "--force"],
    reason="Force-pushing rewrites shared history",
    hint="Use `git push --force-with-lease` instead",
    tests={
        Input(command="git push --force"): Block(),
...
```

...

</details>

### strict-kwargs

Enforce using keyword arguments where possible.

`pip install strict-kwargs` · installs (wheel) · licence: MIT License · rank 10198 · last release 2026-10-09 · [PyPI](https://pypi.org/project/strict-kwargs/) · [source](https://github.com/adamtheturtle/strict-kwargs)

<details><summary>README extract</summary>

Enforce using keyword arguments where possible.

`strict-kwargs` is a standalone CLI implemented in Rust.

For example, if we have a function which takes two regular arguments, there are three ways to call it.
With this tool, only the form where keyword arguments are used is accepted.

Features:
- Like a formatter, such as `black` or `ruff format`, this lets you stop discussing whether a particular function call should use keyword arguments.
- Positional arguments can be fine at first. ...

Example:
```python
"""Showcase errors when calling a function without naming the arguments."""

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

add(a=1, b=2)  # OK
add(1, 2)  # strict-kwargs reports this; strict-kwargs check --fix can rewrite it
...

</details>

### no-defaults

A fast Python linter that forbids function and dataclass defaults.

`pip install no-defaults` · installs (wheel) · licence: MIT · rank 10250 · last release 2026-09-01 · [PyPI](https://pypi.org/project/no-defaults/) · [source](https://github.com/adamtheturtle/no-defaults)

<details><summary>README extract</summary>

A fast, standalone Python linter that forbids defaults in function signatures, dataclasses, and pydantic models — and removes them for you, updating the call sites in the files you checked so the code still runs. It is implemented in Rust and parses Python with Ruff's parser.

Example:
```python
from dataclasses import dataclass, field
from pydantic import BaseModel, Field

def connect(timeout=30):  # NOD001
    pass

@dataclass
class Job:
    retries: int = 3  # NOD001
    tags: list[str] = field(default_factory=list)  # NOD001

class Request(BaseModel):
    method: str = "GET"  # NOD001
...
```

Sections: no-defaults, Usage, `--fix`, Suppressing, Configuration, pre-commit

</details>

### pylint-json2html

Pylint JSON report to HTML

`pip install pylint-json2html` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10341 · last release 2023-11-11 · [PyPI](https://pypi.org/project/pylint-json2html/)

<details><summary>README extract</summary>

A pylint JSON report file to HTML: pylint is used to generate a JSON report,
and this tool will transform this report into an HTML document:

 usage: pylint-json2html [-h] [-o FILENAME] [-e OUTPUT_ENCODING]
 [-t FILENAME] [-f FORMAT] [FILENAME]

 Transform Pylint JSON report to HTML ...

Features:
Since its 1.7 version,
Pylint does not provide an HTML output format. The release notes say that:

> It was lately a second class citizen in Pylint, being mostly neglected. ...

Sections: pylint-json2html, Why?, Usage, Extended Report, Custom Template, Report, Metrics, Encoding

</details>

### pytest-grpc

pytest plugin for grpc

`pip install pytest-grpc` · installs (wheel) · licence: MIT License · rank 10415 · last release 2020-05-01 · [PyPI](https://pypi.org/project/pytest-grpc/)

<details><summary>README extract</summary>

Write test for gRPC with pytest.

Example:
```python
from stub.test_pb2 import EchoRequest, EchoResponse
from stub.test_pb2_grpc import EchoServiceServicer

class Servicer(EchoServiceServicer):
    def handler(self, request: EchoRequest, context) -> EchoResponse:
        return EchoResponse(name=f'test-{request.name}')

    def error_handler(self, request: EchoRequest, context) -> EchoResponse:
...
```

Sections: pytest-grpc, Example, Usage, Run tests against real gRPC server, Run tests directly to python code, Run the servicer on multiple threads

</details>

### sqlfluffrs

The SQL Linter for Humans

`pip install sqlfluffrs` · installs (wheel) · licence: MIT License · rank 10539 · last release 2026-10-30 · [PyPI](https://pypi.org/project/sqlfluffrs/) · [docs](https://docs.sqlfluff.com) · [source](https://github.com/sqlfluff/sqlfluff)

<details><summary>README extract</summary>

This package is an optional installation for SQLFluff and is not intended to be used as a standalone linting solution.

SQLFluff-rs serves as a Rust-based component that can be integrated with the main SQLFluff package. It is currently in development and should be considered experimental.

Sections: SQLFluff-rs, Purpose

</details>

### flake8-pytest-style

A flake8 plugin checking common style issues or inconsistencies with pytest-based tests.

`pip install flake8-pytest-style` · installs (wheel) · licence: not stated · rank 10661 · last release 2025-10-20 · [PyPI](https://pypi.org/project/flake8-pytest-style/) · [source](https://github.com/m-burst/flake8-pytest-style)

<details><summary>README extract</summary>

A `flake8` plugin checking common style issues or inconsistencies with `pytest`-based tests.

Currently the following errors are reported:

| Code | Description |

| [PT001] | use @pytest.fixture over @pytest.fixture()
 (configurable by `pytest-fixture-no-parentheses`) |
| [PT002] | configuration for fixture '{name}' specified via positional args, ...

Sections: flake8-pytest-style, Description, Configuration, Run linters, autoformat, tests etc., Bump new version

</details>

### sarj-python-lint

Custom Python lint rules — AST-based, pre-commit-friendly, hypermodern defaults

`pip install sarj-python-lint` · installs (wheel) · licence: MIT · rank 10711 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sarj-python-lint/) · [docs](https://code-standards.sarj.ai/rules/python/) · [source](https://github.com/sarj-ai/code-standards)

<details><summary>README extract</summary>

<!-- Generated by `code-standards maintain docs sync`; do not edit. -->

Custom Python lint rules — AST-based, pre-commit-friendly, hypermodern defaults

Documentation · Source

</details>

### allure-robotframework

Allure Robot Framework integration

`pip install allure-robotframework` · installs (wheel) · licence: Apache Software License · rank 10927 · last release 2026-09-29 · [PyPI](https://pypi.org/project/allure-robotframework/) · [source](https://github.com/allure-framework/allure-python)

<details><summary>README extract</summary>

> An Allure adapter for Robot Framework.

[]( "Allure Report")

- Learn more about Allure Report at
- 📚 Documentation – discover official documentation for Allure Report
- ❓ Questions and Support – get help from the team and community
- 📢 Official announcements – stay updated with our latest news and updates ...

Sections: Allure Robot Framework Listener, Usage examples

</details>

### flake8-fixme

Check for FIXME, TODO and other temporary developer notes. Plugin for flake8.

`pip install flake8-fixme` · installs (wheel) · licence: Apache Software License · rank 10982 · last release 2019-05-06 · [PyPI](https://pypi.org/project/flake8-fixme/)

<details><summary>README extract</summary>

Check for FIXME, TODO and other temporary developer notes.

This module provides a plugin for `flake8`, the Python code checker.

> This module was inspired by flake8-todo

Example:
```python
def my_function():
    # FIXME actual implementation here!
    pass
```

Sections: flake8-fixme, Usage, 1.0.2, Enhancements, 1.0.1, Bugfixes, 1.0.0, Breaking changes

</details>

### pytest-testrail

A pytest plugin for creating TestRail runs and adding results

`pip install pytest-testrail` · installs (wheel) · licence: MIT · rank 11114 · last release 2026-01-25 · [PyPI](https://pypi.org/project/pytest-testrail/) · [docs](https://github.com/allankp/pytest-testrail#readme) · [source](https://github.com/allankp/pytest-testrail)

<details><summary>README extract</summary>

This is a pytest plugin for creating/editing testplans or testruns based
on pytest markers. The results of the collected tests will be updated
against the testplan/testrun in TestRail.

Version 3.0 brings major modernization:

- Python 3.10+ required (Python 2 support dropped)
- Full type hints throughout the codebase ...

Example:
```python
from pytest_testrail import APIClient, TestRailError

# Create client
client = APIClient(
    base_url="
    user="user@example.com",
    password="your-api-key"  # Can be API key or password
)

# Use context manager for automatic cleanup
with client:
    # Get a test case
    case = client.send_get("get_case/1")

    # Add a result
...
```

...

</details>

### pytest-jira

py.test JIRA integration plugin, using markers

`pip install pytest-jira` · installs (wheel) · licence: GPL-2.0-only · rank 11273 · last release 2026-07-13 · [PyPI](https://pypi.org/project/pytest-jira/)

_README extract left out: share-alike licence._

### allure-pytest-bdd

Allure pytest-bdd integration

`pip install allure-pytest-bdd` · installs (wheel) · licence: Apache Software License · rank 11355 · last release 2026-09-29 · [PyPI](https://pypi.org/project/allure-pytest-bdd/) · [source](https://github.com/allure-framework/allure-python)

<details><summary>README extract</summary>

> An Allure adapter for Pytest-BDD.

[]( "Allure Report")

- Learn more about Allure Report at
- 📚 Documentation – discover official documentation for Allure Report
- ❓ Questions and Support – get help from the team and community
- 📢 Official announcements – stay updated with our latest news and updates ...

Sections: Allure Pytest-BDD, Quick start

</details>

### cppclean

Find problems in C++ source that slow development of large code bases.

`pip install cppclean` · installs from source (sdist only) · licence: Apache license · rank 11481 · last release 2019-07-30 · [PyPI](https://pypi.org/project/cppclean/)

<details><summary>README extract</summary>

cppclean attempts to find problems in C++ source that slow development
in large code bases, for example various forms of unused code.
Unused code can be unused functions, methods, data members, types, etc
to unnecessary #include directives. Unnecessary #includes can cause
considerable extra compiles increasing the edit-compile-run cycle. ...

Features:
cppclean finds the following:

- Classes with virtual methods, no virtual destructor, and no bases
- Global/static data that are potential problems when using threads
- Functions that are declared but not defined ...

Sections: cppclean, Goal, Features, Run, Non-goals, Links

</details>

### pylama

Code audit tool for python

`pip install pylama` · installs (wheel) · licence: MIT License · rank 12136 · last release 2022-08-08 · [PyPI](https://pypi.org/project/pylama/) · [docs](https://klen.github.io/pylama) · [source](https://github.com/klen/pylama)

<details><summary>README extract</summary>

Code audit tool for Python. Pylama wraps these tools:

* pycodestyle (formerly pep8) © 2012-2013, Florent Xicluna;
* pydocstyle (formerly pep257 by Vladimir Keleshev) © 2014, Amir Rachum;
* PyFlakes © 2005-2013, Kevin Watters;
* Mccabe © Ned Batchelder;
* Pylint © 2013, Logilab;
* Radon © Michele Lacchia
* eradicate © Steven Myint;
* Mypy © Jukka ...

Example:
```python
setup(
    name='pylama_wow',
    install_requires=[ 'setuptools' ],
    entry_points={
        'pylama.linter': ['wow = pylama_wow.main:Linter'],
    }
    # ...
)
```

...

</details>

### clangd-tidy

A faster alternative to clang-tidy

`pip install clangd-tidy` · installs (wheel) · licence: MIT License · rank 12187 · last release 2026-02-09 · [PyPI](https://pypi.org/project/clangd-tidy/)

<details><summary>README extract</summary>

clang-tidy is a powerful tool for static analysis of C++ code. However, it's widely acknowledged that clang-tidy takes a significant amount of time to run on large codebases, particularly when enabling numerous checks. This often leads to the dilemma of disabling valuable checks to expedite clang-tidy execution. ...

Sections: clangd-tidy: A Faster Alternative to clang-tidy, Motivation, Comparison with clang-tidy, Prerequisites, Usage, clang-tidy, clangd-tidy-diff

</details>

### validate-pyproject-schema-store

A plugin set for validate-pyproject and schema-store.

`pip install validate-pyproject-schema-store` · installs (wheel) · licence: Apache-2.0 · rank 12479 · last release 2026-11-07 · [PyPI](https://pypi.org/project/validate-pyproject-schema-store/)

<details><summary>README extract</summary>

[][actions-link]

[][pypi-link]
[][pypi-link]

<!-- SPHINX-START -->

This provides a versioned copy of SchemaStore for validate-pyproject.
You can pin this to get a stable set of schema files.

Nested schemas are not supported yet. Support will require updates to
validate-pyproject. For now, they are replaced with `"type": "object"`.

Sections: validate-pyproject-schema-store, Usage, Direct usage

</details>

### ops-scenario

Python library providing a state-transition testing API for Operator Framework charms.

`pip install ops-scenario` · installs (wheel) · licence: Apache-2.0 · rank 12490 · last release 2026-10-08 · [PyPI](https://pypi.org/project/ops-scenario/)

<details><summary>README extract</summary>

Example:
```python
from ops import testing

# 'src/charm.py' typically contains the charm class.
from charm import MyCharm

def test_start():
    ctx = testing.Context(MyCharm)
    state_in = testing.State()
    state_out = ctx.run(ctx.on.start(), state_in)
    assert state_out.unit_status == testing.ActiveStatus()
```

Sections: Writing tests, Documentation

</details>

### curlylint

{{ 🎀}} Experimental HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid

`pip install curlylint` · installs (wheel) · licence: MIT License · rank 12719 · last release 2022-03-30 · [PyPI](https://pypi.org/project/curlylint/)

<details><summary>README extract</summary>

> {{ 🎀}} Experimental HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid.
> Forked from jinjalint.

Features:
Curlylint is an HTML linter for “curly braces” templates, and their HTML. It focuses on rules to check for common accessibility issues.

On the roadmap:

- More checks for common accessibility issues in HTML. ...

Sections: curlylint [](, Features, Usage

</details>

### clawmetry

ClawMetry - Real-time observability for 32 AI agent runtimes (OpenClaw, NVIDIA NemoClaw, Claude Code, Codex & more)

`pip install clawmetry` · installs (wheel) · licence: MIT License · rank 12906 · last release 2026-11-07 · [PyPI](https://pypi.org/project/clawmetry/) · [source](https://github.com/vivekchand/clawmetry)

<details><summary>README extract</summary>

An agent can make a hundred tool calls without making progress. ClawMetry
reads the session files your coding agents already write, and puts the timeline,
the tool calls and whatever token and cost data the runtime exposes into one
view — so you can tell a long run that is working from one that is stuck. ...

Sections: ClawMetry, Works with 32 agent runtimes, What you get, Context blowout, and what watching costs, Pricing, Your data stays on your machine, Docs, Screenshots, Recognition

</details>

### pytest-container

Pytest fixtures for writing container based tests

`pip install pytest-container` · installs (wheel) · licence: OSI Approved; GNU Lesser General Public License v2 or later (LGPLv2+) · rank 13272 · last release 2025-06-30 · [PyPI](https://pypi.org/project/pytest-container/) · [source](https://github.com/dcermak/pytest_container/)

_README extract left out: share-alike licence._

### flake8-type-checking

A flake8 plugin for managing type-checking imports & forward references

`pip install flake8-type-checking` · installs (wheel) · licence: BSD License · rank 13358 · last release 2026-11-04 · [PyPI](https://pypi.org/project/flake8-type-checking/) · [source](https://github.com/snok/flake8-type-checking)

<details><summary>README extract</summary>

Lets you know which imports to move in or out of
type-checking blocks.

The plugin assumes that the imports you only use for type hinting
*are not* required at runtime. When imports aren't strictly required at runtime, it means we can guard them (or with Python
3.15+ we can make them lazy).

Guarding imports provides 3 major benefits: ...

Example:
```python
import pandas

def dataframe_length(df: pandas.DataFrame) -> int:
    return len(df)
```

Sections: flake8-type-checking, Primary features, Error codes, Choosing how to handle forward references, Enabling error ranges, Lazy imports, Configuration, Python 3.14+, Python 3.15+, Typing modules, Exempt modules, Strict, Report typing-only uses of `lazy_modules`, Force `from future import annotations` import

</details>

### ascii-guard

A minimal-dependency Python linter for detecting and fixing misaligned ASCII art boxes in documentation

`pip install ascii-guard` · installs (wheel) · licence: Apache-2.0 · rank 13370 · last release 2026-02-12 · [PyPI](https://pypi.org/project/ascii-guard/) · [source](https://github.com/fxstein/ascii-guard)

<details><summary>README extract</summary>

Zero-dependency Python linter for detecting and fixing misaligned ASCII art boxes in documentation.

AI-generated ASCII flowcharts and diagrams often have subtle formatting errors where box borders are misaligned by 1-2 characters. This breaks visual integrity and makes documentation harder to read. ...

Example:
```python
from ascii_guard import lint_file, fix_file, detect_boxes

# Lint a file for issues
result = lint_file("README.md")
if result.has_errors:
    print(f"Found {len(result.errors)} alignment errors")
    for error in result.errors:
        print(f"  Line {error.line + 1}: {error.message}")

# Auto-fix alignment issues
...
```

...

</details>

### vsg

VHDL Style Guide

`pip install vsg` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13954 · last release 2025-09-07 · [PyPI](https://pypi.org/project/vsg/)

_README extract left out: share-alike licence._

### valgebra

Fast runtime validation via a closed Boolean algebra of schemas on a compiled Rust core.

`pip install valgebra` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 14203 · last release 2026-11-06 · [PyPI](https://pypi.org/project/valgebra/) · [docs](https://ppigazzini.github.io/valgebra/)

<details><summary>README extract</summary>

A closed, minimal Boolean algebra of schemas for Python. A schema denotes
a *set of Python values*, and validating asks whether a value you already hold is
a member — no copy, no coercion. ...

Features:
- Schemas are sets; validation is membership. Subtyping is set inclusion and
 equivalence is mutual inclusion — sound, deciding a wide fragment and staying
 deliberately conservative beyond it (foundations,
 decidability, soundness argument). ...

Example:
```python
from typing import TypedDict

from valgebra import ValidationError, Validator

class User(TypedDict):
    name: str
    age: int

is_user = Validator(User)

assert is_user.is_valid({"name": "Ada", "age": 36})
assert not is_user.is_valid({"name": "Ada", "age": "unknown"})

...

</details>

### sarj-sql-lint

Deterministic PostgreSQL migration rules for safe, repeatable schema changes.

`pip install sarj-sql-lint` · installs (wheel) · licence: MIT · rank 14361 · last release 2026-11-07 · [PyPI](https://pypi.org/project/sarj-sql-lint/) · [docs](https://code-standards.sarj.ai/rules/sql/) · [source](https://github.com/sarj-ai/code-standards)

<details><summary>README extract</summary>

<!-- Generated by `code-standards maintain docs sync`; do not edit. -->

Deterministic PostgreSQL migration rules for safe, repeatable schema changes.

Documentation · Source

</details>

### marionette-driver

Marionette Driver

`pip install marionette-driver` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14406 · last release 2026-07-20 · [PyPI](https://pypi.org/project/marionette-driver/)

<details><summary>README extract</summary>

Note marionette_driver is no longer supported.

For more information see

</details>

### sarj-iac-lint

Custom Terraform / IaC lint rules, pre-commit-friendly.

`pip install sarj-iac-lint` · installs (wheel) · licence: MIT · rank 14727 · last release 2026-11-08 · [PyPI](https://pypi.org/project/sarj-iac-lint/) · [docs](https://code-standards.sarj.ai/rules/iac/) · [source](https://github.com/sarj-ai/code-standards)

<details><summary>README extract</summary>

<!-- Generated by `code-standards maintain docs sync`; do not edit. -->

Custom Terraform / IaC lint rules, pre-commit-friendly.

Documentation · Source

</details>

### reformat-gherkin

Formatter for Gherkin language

`pip install reformat-gherkin` · installs (wheel) · licence: MIT License · rank 14845 · last release 2022-10-04 · [PyPI](https://pypi.org/project/reformat-gherkin/)

<details><summary>README extract</summary>

&nbsp;

&nbsp;

&nbsp;
&nbsp;

Sections: Reformat-gherkin, About, Usage, Command-line options, Config file, Version control integration

</details>

## Also in this topic

- [ruff](software-development-libraries.md#ruff) - An extremely fast Python linter and code formatter, written in Rust.
- [uv](software-development-libraries.md#uv) - An extremely fast Python package and project manager, written in Rust.
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [black](software-development-libraries.md#black) - The uncompromising code formatter.
- [beartype](software-development-code-generators.md#beartype) - Unbearably fast near-real-time pure-Python runtime-static type-checker.
- [mccabe](software-development-libraries.md#mccabe) - McCabe checker, plugin for flake8
- [ty](software-development-libraries.md#ty) - An extremely fast Python type checker, written in Rust.
- [flake8](software-development-libraries.md#flake8) - the modular source code checker: pep8 pyflakes and co
- [astroid](software-development-libraries.md#astroid) - An abstract syntax tree for Python with inference support.
- [pylint](software-development-debuggers.md#pylint) - python code static checker
- [yamllint](software-development.md#yamllint) - A linter for YAML files.
- [semgrep](security.md#semgrep) - Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.
- [uv-build](software-development-libraries.md#uv-build) - The uv build backend
- [deptry](software-development-libraries.md#deptry) - A command line utility to check for unused, missing and transitive dependencies in a Python project.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [autopep8](software-development-libraries.md#autopep8) - A tool that automatically formats Python code to conform to the PEP 8 style guide
- [poethepoet](software-development-build-tools.md#poethepoet) - A task runner that works well with poetry and uv.
- [radon](software-development.md#radon) - Code Metrics in Python
- [tach](software-development-libraries.md#tach) - A Python tool to maintain a modular package architecture.
- [yapf](software-development-libraries.md#yapf) - A formatter for Python code
- [ansible-compat](software-development-bug-tracking.md#ansible-compat) - Ansible compatibility goodies
- [ast-grep-cli](security.md#ast-grep-cli) - Structural Search and Rewrite code at large scale using precise AST pattern.
- [pytest-unordered](software-development-libraries.md#pytest-unordered) - Test equality of unordered collections in pytest
- [gcovr](software-development.md#gcovr) - Generate C/C++ code coverage reports with gcov
- [flake8-bugbear](software-development-libraries.md#flake8-bugbear) - A plugin for flake8 finding likely bugs and design problems in your program. Contains warnings that don't belong in pyflakes and pycodestyle.
- [PyHamcrest](software-development.md#pyhamcrest) - Hamcrest framework for matcher objects
- [runtype](software-development-libraries.md#runtype) - Type dispatch and validation for run-time Python
- [chispa](software-development-libraries.md#chispa) - Pyspark test helper library
- [ast-grep-py](security.md#ast-grep-py) - Structural Search and Rewrite code at large scale using precise AST pattern.
- [pep8-naming](software-development-libraries-2.md#pep8-naming) - Check PEP-8 naming conventions, plugin for flake8
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [molecule](software-development-bug-tracking.md#molecule) - Molecule aids in the development and testing of Ansible roles
- [interrogate](software-development-documentation.md#interrogate) - Interrogate a codebase for docstring coverage.
- [complexipy](software-development-libraries-2.md#complexipy) - An extremely fast Python library to calculate the cognitive complexity of Python files, written in Rust.
- [viztracer](software-development-bug-tracking.md#viztracer) - A debugging and profiling tool that can trace and visualize python code execution
- [salt-lint](software-development-bug-tracking.md#salt-lint) - A command-line utility that checks for best practices in SaltStack.
- [xenon](internet-www-http.md#xenon) - Monitor code metrics for Python on your CI server
- [flake8-import-order](software-development-libraries-2.md#flake8-import-order) - Flake8 and pylama plugin that checks the ordering of import statements.
- [pytest-qt](desktop-environment-window-managers.md#pytest-qt) - pytest support for PyQt and PySide applications
- [datacontract-cli](database.md#datacontract-cli) - The datacontract CLI is an open source command-line tool for working with Data Contracts. It uses data contract YAML files to lint the data contract, connect to data sources and execute schema and quality tests, detect breaking changes, and export to different formats. The tool is written in Python. It can be used as a standalone CLI tool, in a CI/CD pipeline, or directly as a Python library.
- [flake8-quotes](software-development-libraries-2.md#flake8-quotes) - Flake8 lint for quotes.
- [flake8-isort](software-development.md#flake8-isort) - flake8 plugin that integrates isort
- [molecule-plugins](software-development-bug-tracking.md#molecule-plugins) - Molecule Plugins
- [pyDeprecate](software-development-libraries-2.md#pydeprecate) - Python deprecation decorator: call forwarding, argument mapping, class proxying, CI audit. Zero deps.
- [rollbar](internet-www-http.md#rollbar) - Easy and powerful exception tracking with Rollbar. Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.
- [flake8-print](software-development-libraries-2.md#flake8-print) - print statement checker plugin for flake8
- [pywinauto](software-development-libraries-2.md#pywinauto) - A set of Python modules to automate the Microsoft Windows GUI
- [rumdl](software-development-libraries-2.md#rumdl) - A fast Markdown linter and formatter written in Rust
- [Nuitka](software-development-build-tools.md#nuitka) - Python compiler with full language support and CPython compatibility
- [chalk-viztracer](software-development-bug-tracking.md#chalk-viztracer) - A debugging and profiling tool that can trace and visualize python code execution (Chalk fork)
- [darglint](software-development-documentation.md#darglint) - A utility for ensuring Google-style docstrings stay up to date with the source code.
- [pdbp](scientific-engineering.md#pdbp) - pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.
- [axe-playwright-python](adaptive-technologies.md#axe-playwright-python) - Automated web accessibility testing using axe-core engine and Playwright.
- [tabcompleter](scientific-engineering.md#tabcompleter) - tabcompleter --- Autocompletion in the Python console.
- [flake8-builtins](software-development.md#flake8-builtins) - Check for python builtins being used as variables or parameters
- [pyink](software-development-libraries-2.md#pyink) - Pyink is a python formatter, forked from Black with slightly different behavior.
- [doit](scientific-engineering.md#doit) - doit - Automation Tool
- [fixit](software-development-libraries-2.md#fixit) - A lint framework that writes better Python code for you.
- [pudb](software-development.md#pudb) - A full-screen, console-based Python debugger
- [pylint-actions](software-development-libraries-2.md#pylint-actions) - Pylint plugin for GitHub Actions
- [sbvirtualdisplay](internet.md#sbvirtualdisplay) - A customized pyvirtualdisplay for SeleniumBase.
- [flake8-polyfill](software-development-libraries-2.md#flake8-polyfill) - Polyfill package for Flake8 plugins
- [deal](software-development.md#deal) - **Deal** is a Python library for [design by contract][wiki] (DbC) programming.
- [flake8-annotations](software-development-libraries-2.md#flake8-annotations) - Flake8 Type Annotation Checks
- [selenium-stealth](internet.md#selenium-stealth) - Trying to make python selenium more stealthy.
- [flake8-eradicate](software-development-libraries-2.md#flake8-eradicate) - Flake8 plugin to find commented out code
- [flake8-bandit](security.md#flake8-bandit) - Automated security testing with bandit and flake8.
- [cognitive-complexity](software-development-documentation.md#cognitive-complexity) - Library to calculate Python functions cognitive complexity via code
- [cisco-ai-skill-scanner](security.md#cisco-ai-skill-scanner) - Security scanner for Agent Skills packages - Detects prompt injection, data exfiltration, and malicious code
- [wiremock](internet-www-http.md#wiremock) - Wiremock Admin API Client
- [flake8-black](software-development-libraries-2.md#flake8-black) - flake8 plugin to call black as a code style validator
- [flake8-broken-line](software-development-libraries-2.md#flake8-broken-line) - Flake8 plugin to forbid backslashes for line breaks
- [check-wheel-contents](software-development-build-tools.md#check-wheel-contents) - Check your wheels have the right contents
- [flake8-use-fstring](software-development-libraries-3.md#flake8-use-fstring) - Flake8 plugin for string formatting style.
- [pgsanity](database.md#pgsanity) - Check syntax of sql for PostgreSQL
- [fno](software-development-build-tools.md#fno) - Run your coding agents as one team: one backlog they all work from, and a chat where they message each other and you, across harnesses and machines.
- [verlib2](software-development-build-tools.md#verlib2) - A standalone bundle of "distutils.version" and "packaging.version", without anything else.
- [flake8-cognitive-complexity](software-development-documentation.md#flake8-cognitive-complexity) - An extension for flake8 that validates cognitive functions complexity
- [pytest-flake8](software-development.md#pytest-flake8) - pytest plugin to check FLAKE8 requirements
- [flake8-commas](software-development-libraries-3.md#flake8-commas) - Flake8 lint for trailing commas.
- [wemake-python-styleguide](software-development-libraries-3.md#wemake-python-styleguide) - The strictest and most opinionated python linter ever
- [zuban](software-development-libraries-3.md#zuban) - Zuban - The Zuban Language Server
- [libsast](security.md#libsast) - A generic SAST library built on top of semgrep and regex
- [flake8-variables-names](software-development-documentation.md#flake8-variables-names) - A flake8 extension that helps to make more readable variables names
- [django-eagle](software-development-libraries-3.md#django-eagle) - Prevent Django ORM Unused Eager Loads
- [fawltydeps](software-development-libraries-3.md#fawltydeps) - Find undeclared and unused 3rd-party dependencies in your Python project.
- [beautysh](software-development-libraries-3.md#beautysh) - A Bash beautifier for the masses.
- [aiocop](software-development-debuggers.md#aiocop) - Non-intrusive monitoring for Python asyncio and uvloop. Detects, pinpoints, and logs blocking IO and CPU calls that freeze your event loop.
- [docstr-coverage](documentation.md#docstr-coverage) - Utility for examining python source files to ensure proper documentation. Lists missing docstrings, and calculates overall docstring coverage percentage rating.
- [flake8-debugger](software-development-libraries-3.md#flake8-debugger) - ipdb/pdb statement checker plugin for flake8
- [openunmix](software-development-libraries-3.md#openunmix) - PyTorch-based music source separation toolkit
- [config-formatter](software-development-libraries-3.md#config-formatter) - An automatic formatter for .ini and .cfg configuration files
- [flake8-noqa](software-development-libraries-3.md#flake8-noqa) - Flake8 noqa comment validation
- [flawfinder](security.md#flawfinder) - a program that examines source code looking for security weaknesses
- [pylint-odoo](software-development-debuggers.md#pylint-odoo) - Pylint plugin for Odoo
- [flake8-functions](software-development-documentation.md#flake8-functions) - A flake8 extension that checks functions
- [plugin-scanner](security.md#plugin-scanner) - Lint, verify, and gate plugin ecosystems for maintainers, CI, and publish workflows.
- [gersemi](software-development-libraries-3.md#gersemi) - A formatter to make your CMake code the real treasure
- [flake8-class-attributes-order](software-development-documentation.md#flake8-class-attributes-order) - A flake8 extension that checks classes attributes order
- [flake8-requirements](software-development-libraries-3.md#flake8-requirements) - Package requirements checker, plugin for flake8
- [openrewrite](software-development-code-generators.md#openrewrite) - OpenRewrite automated refactoring for Python.
- [uv-secure](software-development-libraries-3.md#uv-secure) - Deprecated dependency scanner for uv projects; use uv audit instead
- [leakguard](security.md#leakguard) - leakguard — fast secret scanner for your codebase
- [flake8-expression-complexity](software-development-documentation.md#flake8-expression-complexity) - A flake8 extension that checks expressions complexity
- [tower](software-development-libraries-3.md#tower) - Tower CLI and runtime environment for Tower.
- [flake8-pyi](software-development-libraries-3.md#flake8-pyi) - A plugin for flake8 to enable linting .pyi stub files.
- [flake8-annotations-complexity](software-development-documentation.md#flake8-annotations-complexity) - A flake8 extension that checks for type annotations complexity
- [flake8-rst-docstrings](software-development-libraries-3.md#flake8-rst-docstrings) - Python docstring reStructuredText (RST) validator for flake8
- [flake8-no-implicit-concat](software-development-libraries-3.md#flake8-no-implicit-concat) - Flake8 plugin that forbids implicit str/bytes literal concatenations
- [pytest-beartype](software-development-code-generators.md#pytest-beartype) - Pytest plugin type-checking tests, fixtures, and/or your codebase with beartype: the unbearably fast near-real-time pure-Python runtime-static type-checker.
- [flake8-literal](software-development-libraries-3.md#flake8-literal) - Flake8 string literal validation
- [flake8-import-rules](software-development-libraries-3.md#flake8-import-rules) - 
- [scan-build](software-development-compilers.md#scan-build) - Run the Clang static analyzer on projects with a compilation database.
- [jcodemunch-mcp](software-development.md#jcodemunch-mcp) - MCP server that gives AI coding agents the exact function or class they asked for, not the whole file. Runs on your machine, 70+ languages. Free for non-commercial use; commercial use needs a one-time license.
- [bernstein](software-development.md#bernstein) - The open-source governance layer for AI agents. No model in the coordination loop, so replaying a plan reproduces its task graph byte-identically, and run receipts are byte-identical across independent builds. Signed lineage plus an opt-in HMAC audit chain a reviewer checks offline, without rerunning it. Runs Claude Code, Codex, Gemini CLI, and 50+ CLI agents; governs any deliverable from code to research to audit evidence packs. Cluster mode, air-gap deploy.
- [flake8-picky-parentheses](software-development-libraries-3.md#flake8-picky-parentheses) - flake8 plugin to nitpick about parenthesis, brackets, and braces
- [ruff-lsp](software-development-libraries-3.md#ruff-lsp) - A Language Server Protocol implementation for Ruff.
- [hol-guard](security.md#hol-guard) - Open-source antivirus and runtime protection for AI agents, tools, MCP servers, plugins, skills, and package installs.
- [flake8-string-format](software-development-libraries-4.md#flake8-string-format) - string format checker, plugin for flake8
- [dotenv-linter](software-development-libraries-4.md#dotenv-linter) - Linting dotenv files like a charm!
- [flake8-unused-arguments](software-development-libraries-4.md#flake8-unused-arguments) - flake8 extension to warn on unused function arguments
- [pylint-junit](software-development-libraries-4.md#pylint-junit) - pylint reporter for junit format.
- [pyprof2calltree](desktop-environment-k-desktop-environment-kde.md#pyprof2calltree) - Help visualize profiling data from cProfile with kcachegrind and qcachegrind
- [pysphere](software-development-libraries-4.md#pysphere) - Python API for interacting with the vSphere Web Services SDK
- [pyrig](software-development-build-tools.md#pyrig) - A Python project setup and management tool built on infrastructure as code and convention over configuration.
- [flake8-formatter-junit-xml](software-development-libraries-4.md#flake8-formatter-junit-xml) - JUnit XML Formatter for flake8
- [skylos](security.md#skylos) - Python dead code, security and secrets scanner with a pull-request gate; narrower checks for TypeScript, Java and more.
- [mailosaur](software-development-libraries-4.md#mailosaur) - The Mailosaur Python library lets you integrate email and SMS testing into your continuous integration process.
- [roc-validator](scientific-engineering-2.md#roc-validator) - A Python package to validate RO-Crates
- [robotcode](software-development-debuggers.md#robotcode) - Command line interface for RobotCode
- [privata](software-development-libraries-4.md#privata) - A Python module privacy checker for keeping public interfaces intentional.
- [flake8-executable](software-development-libraries-4.md#flake8-executable) - A Flake8 plugin for checking executable permissions and shebangs.
- [dlint](security.md#dlint) - Dlint is a tool for encouraging best coding practices and helping ensure Python code is secure.
- [ca9](security.md#ca9) - Open source Python package security and evidence-backed SCA triage
- [pytest-progress](software-development-libraries-4.md#pytest-progress) - pytest plugin for instant test progress status
- [codechecker](software-development-bug-tracking.md#codechecker) - CodeChecker is an analyzer tooling, defect database and viewer extension
- [python-dbusmock](software-development-libraries-5.md#python-dbusmock) - Mock D-Bus objects
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
- [flake8-django](software-development-libraries-5.md#flake8-django) - Plugin to catch bad style specific to Django Projects.
- [miss-hit-core](scientific-engineering-2.md#miss-hit-core) - Code formatting and code metrics for programs written in the MATLAB/Simulink and Octave languages.
