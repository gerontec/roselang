# Software Development / Testing

[Index](README.md) · 206 packages in this topic, 290 more listed under another topic, by downloads.

### pytest-asyncio

Pytest support for asyncio

`pip install pytest-asyncio` · installs (wheel) · licence: Apache-2.0 · rank 126 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pytest-asyncio/) · [docs](https://pytest-asyncio.readthedocs.io) · [source](https://github.com/pytest-dev/pytest-asyncio)

<details><summary>README extract</summary>

pytest-asyncio is a pytest plugin. It facilitates testing of code that uses the asyncio library.

Specifically, pytest-asyncio provides support for coroutines as test functions. This allows users to *await* code inside their tests. For example, the following code is executed as a test item by pytest: ...

Example:
```python
@pytest.mark.asyncio
async def test_some_asyncio_code():
    res = await library.do_something()
    assert b"expected result" == res
```

</details>

### pytest-cov

Pytest plugin for measuring coverage.

`pip install pytest-cov` · installs (wheel) · licence: MIT · rank 139 · last release 2026-03-21 · [PyPI](https://pypi.org/project/pytest-cov/) · [docs](https://pytest-cov.readthedocs.io/)

<details><summary>README extract</summary>

Features:
This plugin provides coverage functionality as a pytest plugin. Compared to just using `coverage run` this plugin does some extras:

* Automatic erasing and combination of .coverage files and default reporting. ...

Sections: Overview, Upgrading from pytest-cov 6.3, Usage, Documentation, Coverage Data File, Limitations, 7.1.0 (2026-03-21), 6.0.0 (2024-10-29), 5.0.0 (2024-03-24), 4.1.0 (2023-05-24), 4.0.0 (2022-09-28), 3.0.0 (2021-10-04), 2.12.1 (2021-06-01), 2.12.0 (2021-05-14)

</details>

### pytest-timeout

pytest plugin to abort hanging tests

`pip install pytest-timeout` · installs (wheel) · licence: DFSG approved; MIT License · rank 282 · last release 2025-05-05 · [PyPI](https://pypi.org/project/pytest-timeout/)

<details><summary>README extract</summary>

This plugin will time each test and terminate it when it takes too
long. Termination may or may not be graceful, please see below, but
when aborting it will show a stack dump of all thread running at the
time. This is useful when running tests under a continuous
integration server or simply if you don't know why the test suite
hangs. ...

Example:
```python
@pytest.mark.timeout(60)
def test_foo():
    pass
```

Sections: pytest-timeout, Usage, Timeout Methods, thread, signal, Specifying the Timeout Method, The `timeout` Marker API, Timeouts in Fixture Teardown, Avoiding timeouts in Fixtures, Debugger Detection, Extending pytest-timeout with plugins, `pytest_timeout_set_timer`, `Settings`, `pytest_timeout_cancel_timer`

</details>

### pytest-mock

Thin-wrapper around the mock package for easier use with pytest

`pip install pytest-mock` · installs (wheel) · licence: MIT License · rank 304 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pytest-mock/) · [docs](https://pytest-mock.readthedocs.io/en/latest/) · [source](https://github.com/pytest-dev/pytest-mock/)

<details><summary>README extract</summary>

This plugin provides a `mocker` fixture which is a thin-wrapper around the patching API
provided by the mock package:

Besides undoing the mocking automatically after the end of the test, it also provides other
nice utilities such as `spy` and `stub`, and uses pytest introspection when
comparing calls. ...

Example:
```python
import os

class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
```

Sections: pytest-mock, Documentation

</details>

### moto

A library that allows you to easily mock out tests based on AWS infrastructure

`pip install moto` · installs (wheel) · licence: Apache-2.0 · rank 482 · last release 2026-10-27 · [PyPI](https://pypi.org/project/moto/) · [docs](http://docs.getmoto.org/en/latest/)

<details><summary>README extract</summary>

Example:
```python
import boto3

class MyModel:
    def init(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.put_object(Bucket="mybucket", Key=self.name, Body=self.value)
```

Sections: Moto - Mock AWS Services, In a nutshell, Documentation

</details>

### pytest-django

A Django plugin for pytest.

`pip install pytest-django` · installs (wheel) · licence: BSD License · rank 738 · last release 2026-08-10 · [PyPI](https://pypi.org/project/pytest-django/) · [docs](https://pytest-django.readthedocs.io/) · [source](https://github.com/pytest-dev/pytest-django)

<details><summary>README extract</summary>

pytest-django allows you to test your Django project/applications with the
pytest testing tool.

* Quick start / tutorial
* Changelog

* Contribution docs

 * Django: 5.2, 6.0 and latest main branch (compatible at the time
 of each release)
 * Python: CPython>=3.10 or PyPy 3
 * pytest: >=7.0 ...

Features:
Running your test suite with pytest-django allows you to tap into the features
that are already present in pytest. Here are some advantages:

* Manage test dependencies with pytest fixtures. ...

</details>

### requests-mock

Mock out responses from the requests package

`pip install requests-mock` · installs (wheel) · licence: Apache Software License · rank 829 · last release 2024-03-29 · [PyPI](https://pypi.org/project/requests-mock/) · [source](https://github.com/jamielennox/requests-mock)

<details><summary>README extract</summary>

`requests-mock` provides a building block to stub out the HTTP requests portions of your testing code.
You should checkout the docs for more information.

Everything in requests eventually goes through an adapter to do the transport work. ...

Example:
```python
>>> import requests
>>> import requests_mock

>>> session = requests.Session()
>>> adapter = requests_mock.Adapter()
>>> session.mount('mock://', adapter)

>>> adapter.register_uri('GET', 'mock://test.com', text='data')
>>> resp = session.get('mock://test.com')
>>> resp.status_code, resp.text
(200, 'data')
```

Sections: requests-mock, Intro, The Basics, Reporting Bugs, Questions

</details>

### pytest-socket

Pytest Plugin to disable socket calls during tests

`pip install pytest-socket` · installs (wheel) · licence: MIT · rank 1199 · last release 2026-08-19 · [PyPI](https://pypi.org/project/pytest-socket/) · [source](https://github.com/miketheman/pytest-socket)

<details><summary>README extract</summary>

A plugin to use with Pytest to disable or restrict `socket` calls during
tests to ensure network calls are prevented.

Features:
- Disables all network calls flowing through Python's `socket` interface,
 including DNS resolution.
- Restricts connections to an allow-list of hosts, IP addresses, or CIDR
 network ranges. ...

Example:
```python
from pytest_socket import disable_socket

def pytest_runtest_setup():
    disable_socket()
```

Sections: pytest-socket, Features, Requirements, Usage, Frequently Asked Questions, Issues, References

</details>

### locust

Developer-friendly load testing framework

`pip install locust` · installs (wheel) · licence: MIT License · rank 1221 · last release 2026-10-21 · [PyPI](https://pypi.org/project/locust/) · [docs](https://docs.locust.io/) · [source](https://github.com/locustio/locust)

<details><summary>README extract</summary>

Locust is an open source performance/load testing tool for HTTP and other protocols. Its developer-friendly approach lets you define your tests in regular Python code.

Locust tests can be run from command line or using its web-based UI. Throughput, response times and errors can be viewed in real time and/or exported for later analysis. ...

Example:
```python
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
...
```

...

</details>

### asynctest

Enhance the standard unittest package with features for testing asyncio libraries

`pip install asynctest` · installs (wheel) · licence: Apache Software License · rank 1564 · last release 2019-05-14 · [PyPI](https://pypi.org/project/asynctest/)

<details><summary>README extract</summary>

The package asynctest is built on top of the standard unittest module and
cuts down boilerplate code when testing libraries for asyncio.

Currently, asynctest targets the "selector" model, hence, some features
will not (yet?) work with Windows' proactor.

Sections: asynctest, Documentation, Features, TestCases, Mock and CoroutineMock, Selectors, Helpers, Roadmap, Tests

</details>

### harbor-rewardkit

Lightweight grading toolkit for environment-based tasks.

`pip install harbor-rewardkit` · installs (wheel) · licence: Apache-2.0 · rank 1623 · last release 2026-11-01 · [PyPI](https://pypi.org/project/harbor-rewardkit/) · [source](https://github.com/harbor-framework/harbor)

<details><summary>README extract</summary>

Rewardkit is a lightweight verifier package for Harbor tasks or standalone use.

Example:
```python
# tests/checks.py
from rewardkit import criteria

criteria.file_exists("output.txt")
criteria.file_contains("output.txt", "hello")
```

Sections: Harbor Rewardkit, Programmatic verifier, Configure scoring, Judge verifier, Multi-reward verifier

</details>

### Appium-Python-Client

Python client for Appium

`pip install Appium-Python-Client` · installs (wheel) · licence: Apache-2.0 · rank 1655 · last release 2026-11-06 · [PyPI](https://pypi.org/project/Appium-Python-Client/) · [source](https://github.com/appium/python-client)

<details><summary>README extract</summary>

An extension library for adding WebDriver Protocol and Appium commands to the Selenium Python language binding for use with the mobile testing framework Appium.

There are three ways to install and use the Appium Python client.

1. Install from PyPi, as
'Appium-Python-Client'.

 You can see the history from here

2. Install from source, via PyPi. ...

Example:
```python
from appium import webdriver
```

Sections: Appium Python Client, Getting the Appium Python client, Compatibility Matrix, Quick migration guide from v4 to v5, Quick migration guide from v3 to v4, Quick migration guide from v2 to v3, Quick migration guide from v1 to v2, Usage, Available `options`, Direct Connect URLs, Relax SSL validation, Set custom `AppiumConnection`, Relaxing HTTP request read timeout, Documentation

</details>

### nose

nose extends unittest to make testing easier

`pip install nose` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 1735 · last release 2015-06-02 · [PyPI](https://pypi.org/project/nose/)

_README extract left out: share-alike licence._

### pytest-recording

A pytest plugin powered by VCR.py to record and replay HTTP traffic

`pip install pytest-recording` · installs (wheel) · licence: MIT · rank 1787 · last release 2026-11-02 · [PyPI](https://pypi.org/project/pytest-recording/) · [docs](https://github.com/kiwicom/pytest-recording) · [source](https://github.com/kiwicom/pytest-recording)

<details><summary>README extract</summary>

A pytest plugin powered by VCR.py to record and replay HTTP traffic.

Features:
- Straightforward `pytest.mark.vcr`, that reflects `VCR.use_cassettes` API;
- Combining multiple VCR cassettes;
- Network access blocking;
- The `rewrite` recording mode that rewrites cassettes from scratch.

Example:
```python
import pytest
import requests

# cassettes/{module_name}/test_single.yaml will be used
@pytest.mark.vcr
def test_single():
    assert requests.get(" == '{"get": true}'

# cassettes/{module_name}/example.yaml will be used
@pytest.mark.default_cassette("example.yaml")
@pytest.mark.vcr
def test_default():
    assert requests.get(" == '{"get": true}'

...
```

...

</details>

### pytest-aiohttp

Pytest plugin for aiohttp support

`pip install pytest-aiohttp` · installs (wheel) · licence: Apache Software License · rank 1857 · last release 2026-06-07 · [PyPI](https://pypi.org/project/pytest-aiohttp/) · [source](https://github.com/aio-libs/pytest-aiohttp)

<details><summary>README extract</summary>

pytest plugin for aiohttp support

The library provides useful fixtures for creation test aiohttp server and client.

Example:
```python
from aiohttp import web

async def hello(request):
    return web.Response(body=b"Hello, world")

def create_app():
    app = web.Application()
    app.router.add_route("GET", "/", hello)
    return app

async def test_hello(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/")
...
```

Sections: pytest-aiohttp, Usage

</details>

### schemathesis

Adaptive API testing for OpenAPI, GraphQL, and gRPC

`pip install schemathesis` · installs (wheel) · licence: MIT · rank 1896 · last release 2026-11-04 · [PyPI](https://pypi.org/project/schemathesis/) · [docs](https://schemathesis.readthedocs.io/en/stable/) · [source](https://github.com/schemathesis/schemathesis)

<details><summary>README extract</summary>

> Catch API bugs before your users do.

Schemathesis tests OpenAPI, GraphQL, and gRPC APIs by generating inputs from your schema, adapting to server responses, and chaining operations into realistic workflows.

 Finding bugs that manual testing missed

 Verdict, timeline and every failure in one offline page: --report html ...

Sections: Schemathesis, Try it now, What problems does it solve?, What can it do?, Who uses it, See it in action, Documentation, Get Help

</details>

### pytest-icdiff

use icdiff for better error messages in pytest assertions

`pip install pytest-icdiff` · installs (wheel) · licence: Public Domain · rank 1900 · last release 2023-12-05 · [PyPI](https://pypi.org/project/pytest-icdiff/)

<details><summary>README extract</summary>

Better diffs in pytest assertion error messages using ICDiff.

Sections: pytest-icdiff, Usage, 0.3 (2020-01-28), 0.2 (2019-03-28), 0.0.4 (2018-08-26), 0.0.3 (2018-08-10), 0.0.2 (2018-08-08), 0.0.1 (2018-08-08)

</details>

### hypothesis-graphql

Hypothesis strategies for GraphQL queries

`pip install hypothesis-graphql` · installs (wheel) · licence: MIT · rank 1907 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hypothesis-graphql/) · [source](https://github.com/Stranger6667/hypothesis-graphql)

<details><summary>README extract</summary>

`hypothesis-graphql` gives you Hypothesis strategies that build queries and mutations from a GraphQL schema.
Each generated operation selects a random subset of fields at random depth and fills arguments with random values.

For a ready-made tool, try Schemathesis: it runs on top of this library and reports server crashes without any test code.

Example:
```python
from hypothesis import given
from hypothesis_graphql import from_schema
import requests

# A schema string or a `graphql.GraphQLSchema` instance
SCHEMA = """
type Book {
  title: String
  author: Author
}

type Author {
  name: String
  books: [Book]
}

type Query {
  getBooks: [Book]
  getAuthors: [Author]
}

type Mutation {
...
```

Sections: hypothesis-graphql, Usage, Customization

</details>

### harfile

Writer for HTTP Archive (HAR) files

`pip install harfile` · installs (wheel) · licence: MIT · rank 1941 · last release 2026-10-21 · [PyPI](https://pypi.org/project/harfile/) · [source](https://github.com/schemathesis/harfile)

<details><summary>README extract</summary>

This package provides a zero-dependency writer for building HAR (HTTP Archive) files in Python.

NOTES:

- The writer assumes a single-threaded environment.
- Pages are not supported.

Example:
```python
import datetime
import io

import harfile

# Write to a file
with harfile.open("filename.har") as har:
    har.add_entry(
        startedDateTime=datetime.datetime.now(datetime.timezone.utc),
        time=42,
        request=harfile.Request(
            method="GET",
            url="
            httpVersion="HTTP/1.1",
        ),
...
```

Sections: harfile, Usage

</details>

### nox

Flexible test automation.

`pip install nox` · installs (wheel) · licence: Apache-2.0 · rank 1969 · last release 2026-10-20 · [PyPI](https://pypi.org/project/nox/) · [docs](https://nox.thea.codes) · [source](https://github.com/wntrblm/nox)

<details><summary>README extract</summary>

*Flexible test automation with Python*

Features:
`nox` is a command-line tool that automates testing in multiple Python environments, similar to tox. Unlike tox, Nox uses a standard Python file for configuration:

Example:
```python
import nox

@nox.session
def tests(session: nox.Session) -> None:
    session.install("pytest")
    session.run("pytest")

@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8")
    session.run("flake8", "--import-order-style", "google")
```

Sections: Nox, Overview, Usage, List all sessions, Get help on a particular session (if it has a docstring), Run all sessions, Run a particular session

</details>

### pytest-subtests

unittest subTest() support and subtests fixture

`pip install pytest-subtests` · installs (wheel) · licence: MIT License · rank 2053 · last release 2025-10-20 · [PyPI](https://pypi.org/project/pytest-subtests/)

<details><summary>README extract</summary>

unittest `subTest()` support and `subtests` fixture.

This pytest plugin was generated with Cookiecutter along with @hackebrot's cookiecutter-pytest-plugin template.

Features:
* Adds support for TestCase.subTest.

* New `subtests` fixture, providing similar functionality for pure pytest tests.

Example:
```python
import unittest

class T(unittest.TestCase):
    def test_foo(self):
        for i in range(5):
            with self.subTest("custom message", i=i):
                self.assertEqual(i % 2, 0)

if name == "main":
    unittest.main()
```

Sections: pytest-subtests, Features, Usage, unittest subTest() example, `subtests` fixture example, Issues

</details>

### behave

behave is behaviour-driven development, Python style

`pip install behave` · installs (wheel) · licence: BSD-2-Clause · rank 2150 · last release 2025-09-04 · [PyPI](https://pypi.org/project/behave/) · [docs](https://behave.readthedocs.io/en/latest/) · [source](https://github.com/behave/behave)

<details><summary>README extract</summary>

|badge.latest_versionbadge.licensebadge.CI_statusbadge.docs_statusbadge.discussionsbadge.gitterbadge.gurubase|

behave is behavior-driven development, Python style.

Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a ...

Example:
```python
# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

...
```

Sections: behave, More Information

</details>

### robotframework

Generic automation framework for acceptance testing and robotic process automation (RPA)

`pip install robotframework` · installs (wheel) · licence: Apache Software License · rank 2264 · last release 2026-11-02 · [PyPI](https://pypi.org/project/robotframework/) · [docs](https://robotframework.org/robotframework) · [source](https://github.com/robotframework/robotframework)

<details><summary>README extract</summary>

Robot Framework is a generic open source
automation framework for acceptance testing, acceptance test driven
development (ATDD), and robotic process automation (RPA). It has simple plain
text syntax and it can be extended easily with generic and custom libraries.

Robot Framework is operating system and application independent. ...

Sections: Robot Framework, Introduction, Example, Usage, Documentation

</details>

### pytest-check

A pytest plugin that allows multiple failures per test.

`pip install pytest-check` · installs (wheel) · licence: not stated · rank 2287 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pytest-check/)

<details><summary>README extract</summary>

A pytest plugin that allows multiple failures per test.

Normally, a test function will fail and stop running with the first failed `assert`.
That's totally fine for tons of kinds of software tests. ...

Example:
```python
import httpx
from pytest_check import check

def test_httpx_get():
    r = httpx.get('
    # bail if bad status code
    assert r.status_code == 200
    # but if we get to here
    # then check everything else without stopping
    with check:
        assert r.is_redirect is False
    with check:
        assert r.encoding == 'utf-8'
    with check:
...
```

...

</details>

### flaky

Plugin for pytest that automatically reruns flaky tests.

`pip install flaky` · installs (wheel) · licence: Apache Software License · rank 2353 · last release 2024-03-12 · [PyPI](https://pypi.org/project/flaky/)

<details><summary>README extract</summary>

Flaky is a plugin for pytest that automatically reruns flaky tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must rely on components that aren't 100%
reliable. With flaky, instead of removing those tests or marking them to @skip, they can be automatically
retried.

For more information about flaky, see this presentation.

Example:
```python
from flaky import flaky
```

Sections: flaky, About, Marking tests flaky, Marking a class flaky, Pytest marker, Don't rerun certain types of failures, Activating the plugin, Command line arguments, No Flaky Report, Shorter Flaky Report, Force Flaky, Compatibility, Setup

</details>

### pytest-random-order

Randomise the order in which pytest tests are run with some control over the randomness

`pip install pytest-random-order` · installs (wheel) · licence: MIT License · rank 2424 · last release 2025-06-22 · [PyPI](https://pypi.org/project/pytest-random-order/)

<details><summary>README extract</summary>

pytest-random-order is a pytest plugin that randomises the order of tests.
This can be useful to detect a test that passes just because it happens to run after an unrelated test that
leaves the system in a *favourable* state. ...

Example:
```python
pytestmark = pytest.mark.random_order(disabled=True)
```

Sections: pytest-random-order, Quick Start, Design, Usage and Tips, Bucket Type Choice, Disable Shuffling in Module or Class, Rerun Tests in the Same Order (Same Seed), Run Last Failed Tests First, Disable the Plugin

</details>

### rstr

Generate random strings in Python

`pip install rstr` · installs (wheel) · licence: BSD License · rank 2498 · last release 2023-10-11 · [PyPI](https://pypi.org/project/rstr/)

<details><summary>README extract</summary>

rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications.

It has no dependencies outside the standard library.

By default, rstr uses the Python `random` module to generate pseudorandom text. ...

Example:
```python
'{0}@{1}.{2}'.format(rstr.nonwhitespace(exclude='@'),
                     rstr.domainsafe(),
                     rstr.letters(3))
```

Sections: rstr = Random Strings in Python, A Word of Caution, Use, Other methods, Xeger, Custom Alphabets, Examples

</details>

### pytest-codspeed

Pytest plugin to create CodSpeed benchmarks

`pip install pytest-codspeed` · installs (wheel) · licence: MIT License · rank 2521 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pytest-codspeed/) · [docs](https://codspeed.io/docs/reference/pytest-codspeed) · [source](https://github.com/CodSpeedHQ/pytest-codspeed)

<details><summary>README extract</summary>

Pytest plugin to create CodSpeed benchmarks

Documentation:

Example:
```python
import pytest
from statistics import median

@pytest.mark.benchmark
def test_median_performance():
    input = [1, 2, 3, 4, 5]
    output = sum(i**2 for i in input)
    assert output == 55
```

Sections: pytest-codspeed, Usage, Creating benchmarks, Running the benchmarks in your CI

</details>

### pytest-custom-exit-code

Exit pytest test session with custom exit code in different scenarios

`pip install pytest-custom-exit-code` · installs (wheel) · licence: MIT License · rank 2541 · last release 2019-08-07 · [PyPI](https://pypi.org/project/pytest-custom-exit-code/)

<details><summary>README extract</summary>

Exit pytest test session with custom exit code in different scenarios

Features:
* TODO

Sections: pytest-custom_exit_code, Features, Requirements, Usage, Issues, Acknowledegements

</details>

### pytest-celery

Pytest plugin for Celery

`pip install pytest-celery` · installs (wheel) · licence: BSD License · rank 2616 · last release 2026-03-02 · [PyPI](https://pypi.org/project/pytest-celery/)

<details><summary>README extract</summary>

:Version: 1.3.0
:Web:
:Download:
:Source:
:DeepWiki:

Welcome to pytest-celery, the official pytest plugin for Celery.

The pytest-celery plugin introduces significant enhancements with the introduction of
version >= 1.0.0, shifting towards a Docker-based approach for smoke and production-like testing. ...

Sections: Official pytest plugin for Celery, Getting Started

</details>

### inline-snapshot

golden master/snapshot/approval testing library which puts the values right into your source code

`pip install inline-snapshot` · installs (wheel) · licence: MIT License · rank 2627 · last release 2026-10-12 · [PyPI](https://pypi.org/project/inline-snapshot/) · [docs](https://15r10nk.github.io/inline-snapshot/latest) · [source](https://github.com/15r10nk/inline-snapshot/)

<details><summary>README extract</summary>

Features:
- support for normal assertions: inline-snapshot can now also fix normal assertions which do not use `snapshot()` like:

 You can learn here more about this feature.

- Intuitive Semantics: `snapshot(x)` mirrors `x` for easy understanding. ...

Example:
```python
from inline_snapshot import snapshot

def test_something():
    assert 1548 * 18489 == snapshot()
```

Sections: Key Features, Usage, Feedback, Issues

</details>

### pytest-dependency

Manage dependencies of tests

`pip install pytest-dependency` · installs from source (sdist only) · licence: Apache Software License · rank 2630 · last release 2026-02-15 · [PyPI](https://pypi.org/project/pytest-dependency/) · [docs](https://pytest-dependency.readthedocs.io/) · [source](https://github.com/RKrahl/pytest-dependency)

<details><summary>README extract</summary>

This module is a plugin for the popular Python testing framework
pytest. It manages dependencies of tests: you may mark some tests
as dependent from other tests. These tests will then be skipped if
any of the dependencies did fail or has been skipped.

See the online documentation. ...

Sections: pytest-dependency – Manage dependencies of tests, Documentation

</details>

### pytest-vcr

Plugin for managing VCR.py cassettes

`pip install pytest-vcr` · installs (wheel) · licence: MIT License · rank 2677 · last release 2019-04-26 · [PyPI](https://pypi.org/project/pytest-vcr/)

<details><summary>README extract</summary>

Py.test plugin for managing VCR.py cassettes.

Example:
```python
@pytest.mark.vcr()
def test_iana():
    response = urlopen('
    assert b'Example domains' in response
```

Sections: pytest-vcr, Quick Start

</details>

### pytest-docker-tools

Docker integration tests for pytest

`pip install pytest-docker-tools` · installs (wheel) · licence: Apache Software License · rank 2756 · last release 2026-07-21 · [PyPI](https://pypi.org/project/pytest-docker-tools/)

<details><summary>README extract</summary>

You have written a software application (in any language) and have packaged it as a Docker image. Now you want to smoke test the built image or do some integration testing with other containers before releasing it. You: ...

Example:
```python
# conftest.py

from http.client import HTTPConnection

import pytest
from pytest_docker_tools import build, container

fakedns_image = build(
    path='examples/resolver-service/dns',
)

fakedns = container(
    image='{fakedns_image.id}',
    environment={
        'DNS_EXAMPLE_COM__A': '127.0.0.1',
    }
)

apiserver_image = build(
...
```

Sections: pytest-docker-tools, Scope, Parallelism, Factories Reference, Containers, Ip Addresses, Ports, Logs, Images, Caching, Networks, Volumes, Fixtures, docker_client

</details>

### pytest-shard

(no summary)

`pip install pytest-shard` · installs (wheel) · licence: MIT License · rank 2772 · last release 2020-12-11 · [PyPI](https://pypi.org/project/pytest-shard/)

<details><summary>README extract</summary>

Shards tests based on a hash of their test name enabling easy parallelism across machines, suitable for a wide variety of continuous integration services. Tests are split at the finest level of granularity, individual test cases, enabling parallelism even if all of your tests are in a single file (or even single parameterized test method).

Features:
`pytest-shard` aims for simplicity. When installed, simply run:

where `I` is the index of this shard and `N` the total number of shards. For example, to split tests across two machines: ...

Sections: pytest-shard, Features, Alternatives

</details>

### pytest-durations

Pytest plugin reporting fixtures and test functions execution time.

`pip install pytest-durations` · installs (wheel) · licence: MIT License · rank 2993 · last release 2026-10-24 · [PyPI](https://pypi.org/project/pytest-durations/) · [source](https://github.com/blake-r/pytest-durations)

<details><summary>README extract</summary>

Pytest plugin to measure fixture and test durations.

In order to get the pure test setup/teardown durations, the plugin subtracts time taken by fixtures whose scope
is larger than "function". ...

Sections: Introduction, Plugin options, Example of report, JSON Export Example, 1.10.0 (Oct 25, 2026), 1.9.0 (Aug 14, 2026), 1.8.0 (Aug 07, 2026), 1.7.1 (Aug 06, 2026), 1.7.0 (Jul 08, 2026), 1.6.3 (Jun 28, 2026) [YANKED], 1.6.2 (Mar 13, 2026), 1.6.1 (Aug 29, 2025), 1.6.0 (Aug 27, 2025), 1.5.2 (Apr 29, 2025)

</details>

### pytest-snapshot

A plugin for snapshot testing with pytest.

`pip install pytest-snapshot` · installs (wheel) · licence: MIT License · rank 3085 · last release 2022-04-23 · [PyPI](https://pypi.org/project/pytest-snapshot/)

<details><summary>README extract</summary>

A plugin for snapshot testing with pytest.

This library was inspired by jest's snapshot testing.
Snapshot testing can be used to test that the value of an expression does not change unexpectedly.
The added benefits of snapshot testing are that

* They are easy to create.
* They are easy to update when the expected value of a test changes. ...

Features:
* snapshot testing of strings and bytes
* snapshot testing of (optionally nested) collections of strings and bytes
* complete control of the snapshot file path and content

Example:
```python
def test_function_output():
    assert foo('function input') == 'expected result'
```

Sections: pytest-snapshot, Features, Requirements, Usage, assert_match, assert_match_dir, Common use case, Similar Packages, Issues, Links

</details>

### anys

Matchers for pytest

`pip install anys` · installs (wheel) · licence: MIT License · rank 3092 · last release 2024-12-01 · [PyPI](https://pypi.org/project/anys/) · [source](https://github.com/jwodder/anys)

<details><summary>README extract</summary>

GitHub
| PyPI
| Issues
| Changelog

`anys` provides matchers for pytest-style assertions. What's a "matcher,"
you say? Well, say you're writing a unit test and you want to assert that a
given object contains the correct values. Normally, you'd just write: ...

Example:
```python
from anys import ANY_DATETIME_STR

assert foo == {
    "widgets": 42,
    "name": "Alice",
    "subfoo": {
        "created_at": ANY_DATETIME_STR,
        "name": "Bob",
        "widgets": 23,
    }
}
```

Sections: API, Classes, Constants, Caveat: Custom Classes

</details>

### lit

A Software Testing Tool

`pip install lit` · installs (wheel) · licence: Apache Software License · rank 3163 · last release 2026-11-03 · [PyPI](https://pypi.org/project/lit/)

<details><summary>README extract</summary>

Features:
* Portable!
 * Flexible test discovery.
 * Parallel test execution.
 * Support for multiple test formats and test suite designs.

Sections: About, Features, Documentation, Source

</details>

### pytest-watcher

Automatically rerun your tests on file modifications

`pip install pytest-watcher` · installs (wheel) · licence: MIT · rank 3300 · last release 2026-01-10 · [PyPI](https://pypi.org/project/pytest-watcher/)

<details><summary>README extract</summary>

Features:
pytest-watcher is a tool to automatically rerun tests (using `pytest` by default) whenever your code changes.

Works on Unix (Linux, MacOS, BSD) and Windows.

Example:

Sections: Welcome to pytest-watcher, Overview, Motivation, Why not general tools, What about pytest-watch, File events, Usage, Available options, Debug logging, Using a different test runner, Watching different patterns, Delay, Screen clearing, Enable BEL notification

</details>

### pytest-sftpserver

py.test plugin to locally test sftp server connections.

`pip install pytest-sftpserver` · installs (wheel) · licence: MIT License · rank 3330 · last release 2019-09-16 · [PyPI](https://pypi.org/project/pytest-sftpserver/)

<details><summary>README extract</summary>

pytest-sftpserver is a plugin for pytest that provides a local SFTP-Server
fixture.

The SFTP-Server provided by this fixture serves content not from files but
directly from Python objects.

Example:
```python
from contextlib import closing
import paramiko
def get_sftp_file(host, port, username, password, path):
    with closing(paramiko.Transport((host, port))) as transport:
        transport.connect(username=username, password=password)
        with closing(paramiko.SFTPClient.from_transport(transport)) as sftpclient:
...
```

Sections: pytest-sftpserver, Quickstart, TODO, 1.3.0 - 2019-09-16, 1.2.0 - 2018-03-28, 1.1.2 - 2015-06-01, 1.1.1 - 2015-04-04, 1.1.0 - 2014-10-15, 1.0.2 - 2014-07-27, 1.0.1 - 2014-07-27, 1.0.0 - 2014-07-18, Inspiration

</details>

### pytest-circleci-coverage

Pytest plugin that works with pytest-cov to generate coverage data for CircleCI's Smarter Testing

`pip install pytest-circleci-coverage` · installs (wheel) · licence: MIT · rank 3332 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pytest-circleci-coverage/)

<details><summary>README extract</summary>

A pytest plugin that works with pytest-cov to generate coverage data for CircleCI's Smarter Testing.

Sections: pytest-circleci-coverage, Usage, Running tests

</details>

### testpath

Test utilities for code working with files and commands

`pip install testpath` · installs (wheel) · licence: BSD License · rank 3495 · last release 2022-02-23 · [PyPI](https://pypi.org/project/testpath/) · [docs](https://testpath.readthedocs.io/en/latest/) · [source](https://github.com/jupyter/testpath)

<details><summary>README extract</summary>

Testpath is a collection of utilities for Python code working with files and commands.

It contains functions to check things on the filesystem, and tools for mocking
system commands and recording calls to those.

Documentation on ReadTheDocs

e.g.:

Example:
```python
import testpath
testpath.assert_isfile(path)

with testpath.assert_calls('git', ['add', path]):
    function_under_test()
```

</details>

### pytest-timeouts

Linux-only Pytest plugin to control durations of various test case execution phases

`pip install pytest-timeouts` · installs from source (sdist only) · licence: MIT License · rank 3528 · last release 2019-09-21 · [PyPI](https://pypi.org/project/pytest-timeouts/) · [docs](https://pytest-timeouts.readthedocs.io) · [source](https://github.com/Scony/pytest-timeouts)

<details><summary>README extract</summary>

Linux-only Pytest plugin to control durations of various test case execution phases.

For documentation visit pytest-timeouts.readthedocs.io.

This plugin has been designed for specific use cases which are out of the scope of famous `pytest-timeout` plugin.
It uses a `SIGALRM` signal to schedule a timer which breaks the test case.

Features:
* `setup`, `execution` and `teardown` phase timeouts controllable by:
 * opts: `--setup-timeout`, `--execution-timeout` and `--teardown-timeout`
 * ini: `setup_timeout`, `execution_timeout` and `teardown_timeout`
 * mark: `setup_timeout`, ...

Example:
```python
import time

import pytest

@pytest.mark.setup_timeout(0.3)
@pytest.mark.execution_timeout(0.5)
@pytest.mark.teardown_timeout(0.4)
def test_timeout():
    time.sleep(1)
```

...

</details>

### pytest-flakefinder

Runs tests multiple times to expose flakiness.

`pip install pytest-flakefinder` · installs (wheel) · licence: Apache Software License · rank 3634 · last release 2022-10-26 · [PyPI](https://pypi.org/project/pytest-flakefinder/)

<details><summary>README extract</summary>

Runs tests multiple times to expose flakiness.

This Pytest plugin was generated with Cookiecutter along with @hackebrot's Cookiecutter-pytest-plugin template.

Features:
* When enabled it will 'multiply' your tests so that they get run multiple times without having to restart pytest. This helps you find flakiness in your tests.
* You can limit your flake runs to a particular timeout value.

Sections: pytest-flakefinder, Features, Usage, Flake Finding, Timing Out, Issues

</details>

### pact-python

Tool for creating and verifying consumer-driven contracts using the Pact framework.

`pip install pact-python` · installs (wheel) · licence: MIT License · rank 3779 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pact-python/) · [docs](https://pact-foundation.github.io/pact-python/) · [source](https://github.com/pact-foundation/pact-python)

<details><summary>README extract</summary>

Fast, easy and reliable testing for your APIs and microservices.

 Package

 CI/CD

 Meta

 Community

Pact is the de-facto API contract testing tool. Replace expensive and brittle end-to-end integration tests with fast, reliable and easy to debug unit tests.

- ⚡ Lightning fast ...

Sections: Pact Python, Documentation, Need Help, Requirements, Telemetry

</details>

### robotframework-pythonlibcore

Tools to ease creating larger test libraries for Robot Framework using Python.

`pip install robotframework-pythonlibcore` · installs (wheel) · licence: Apache-2.0 · rank 3788 · last release 2026-05-14 · [PyPI](https://pypi.org/project/robotframework-pythonlibcore/)

<details><summary>README extract</summary>

Tools to ease creating larger test libraries for Robot
Framework using Python. The Robot Framework
hybrid
and dynamic library
API
gives more flexibility for library than the static library API, but they
also sets requirements for libraries which needs to be implemented in
the library side. ...

Example:
```python
"""Main library."""

from robotlibcore import DynamicCore

from mystuff import Library1, Library2

class MyLibrary(DynamicCore):
    """General library documentation."""

    def init(self):
        libraries = [Library1(), Library2()]
        DynamicCore.init(self, libraries)

    @keyword
    def keyword_in_main(self):
        pass
```

Sections: Python Library Core, Usage, Example, Plugin API, Translation, Provide Translation As File, Provide Translation As Dictionary

</details>

### pact-python-ffi

Python bindings for the Pact FFI library

`pip install pact-python-ffi` · installs (wheel) · licence: MIT · rank 3930 · last release 2026-10-23 · [PyPI](https://pypi.org/project/pact-python-ffi/) · [docs](https://docs.pact.io) · [source](https://github.com/pact-foundation/pact-python)

<details><summary>README extract</summary>

> [!NOTE]
> This package provides direct access to the Pact Foreign Function Interface (FFI) with minimal abstraction. It is intended for advanced users who need low-level control over Pact operations in Python.

 Package

 CI/CD

 Meta

 Community ...

Features:
- The module provides a thin Python wrapper around the Pact FFI (C API).
- Most classes correspond directly to structs from the FFI, and are designed to wrap the underlying C pointers. ...

Sections: Pact Python FFI, Overview, Usage

</details>

### pytest-race

Race conditions tester for pytest

`pip install pytest-race` · installs (wheel) · licence: BSD License · rank 3976 · last release 2022-06-07 · [PyPI](https://pypi.org/project/pytest-race/)

<details><summary>README extract</summary>

*Race conditions tester for pytest*

Introduces start_race fixture to run race condition tests.

* Python 3.7+
* pytest 2.9.0+

Example:
```python
from time import sleep

ACCUMULATOR = 0  # This global var is race conditions prone.

def test_race(start_race):
    from random import randint

    def actual_test():
        global ACCUMULATOR

        increment = randint(1, 10000)

        accumulator = ACCUMULATOR
        sleep(1)  # Simulate some lag.
        ACCUMULATOR += increment

...
```

Sections: pytest-race, Description, Requirements, Usage

</details>

### robotframework-requests

Robot Framework keyword library wrapper around requests

`pip install robotframework-requests` · installs (wheel) · licence: MIT License · rank 3993 · last release 2024-04-07 · [PyPI](https://pypi.org/project/robotframework-requests/)

<details><summary>README extract</summary>

🏠 ``RequestsLibrary`` is a Robot Framework library
aimed to provide HTTP api testing functionalities by wrapping the well known Python Requests Library.

Sections: 🤖 Quick start, What's new in 0.9, What's new in 0.8, 🤖 More examples, 📖 Keywords documentation, 🔬 Test examples

</details>

### localstack-client

A lightweight Python client for LocalStack.

`pip install localstack-client` · installs from source (sdist only) · licence: Apache Software License · rank 4000 · last release 2026-07-21 · [PyPI](https://pypi.org/project/localstack-client/)

### robotframework-seleniumlibrary

Web testing library for Robot Framework

`pip install robotframework-seleniumlibrary` · installs (wheel) · licence: Apache Software License · rank 4033 · last release 2026-05-17 · [PyPI](https://pypi.org/project/robotframework-seleniumlibrary/)

<details><summary>README extract</summary>

SeleniumLibrary is a web testing library for Robot Framework that
utilizes the Selenium tool internally. The project is hosted on GitHub
and downloads can be found from PyPI.

SeleniumLibrary currently works with Selenium 4. It supports Python 3.10 through 3.13.
In addition to the normal Python interpreter, it works also
with PyPy. ...

Sections: SeleniumLibrary, Introduction, Keyword Documentation, Browser drivers, Usage, Extending SeleniumLibrary

</details>

### pytest-picked

Run the tests related to the changed files

`pip install pytest-picked` · installs (wheel) · licence: MIT License · rank 4087 · last release 2024-11-06 · [PyPI](https://pypi.org/project/pytest-picked/)

<details><summary>README extract</summary>

Run the tests related to the unstaged files or the current branch
(according to Git)

Let's say you have the following output from `git status`:

 $ git status

 On branch main
 Your branch is ahead of 'origin/main' by 1 commit.
 (use "git push" to publish your local commits) ...

Features:
Using `git status`, this plugin allows you to:

- Run only tests from modified test files
- Run tests from modified test files first, followed by all unmodified tests

Sections: pytest-picked, Usage, Features, Issues

</details>

### pytest-regressions

Easy to use fixtures to write regression tests.

`pip install pytest-regressions` · installs (wheel) · licence: MIT License · rank 4137 · last release 2026-05-25 · [PyPI](https://pypi.org/project/pytest-regressions/)

<details><summary>README extract</summary>

Fixtures to write regression tests.

Features:
This plugin makes it simple to test general data, images, files, and numeric tables by saving *expected*
data in a *data directory* (courtesy of pytest-datadir) that
can be used to verify that future runs produce the same data. ...

Sections: pytest-regressions, Features, Issues

</details>

### ddt

Data-Driven/Decorated Tests

`pip install ddt` · installs (wheel) · licence: MIT License · rank 4155 · last release 2024-02-26 · [PyPI](https://pypi.org/project/ddt/)

### pytest-testinfra

Test infrastructures

`pip install pytest-testinfra` · installs (wheel) · licence: Apache Software License · rank 4255 · last release 2025-03-30 · [PyPI](https://pypi.org/project/pytest-testinfra/)

<details><summary>README extract</summary>

Latest documentation:

With Testinfra you can write unit tests in Python to test *actual state* of
your servers configured by management tools like Salt, Ansible, Puppet,
Chef and so on.

Testinfra aims to be a Serverspec equivalent in python and is written as
a plugin to the powerful Pytest test engine

Example:
```python
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.2")

...
```

Sections: Testinfra test your infrastructure, About, Quick start

</details>

### pytest-reportlog

Replacement for the --resultlog option, focused in simplicity and extensibility

`pip install pytest-reportlog` · installs (wheel) · licence: MIT · rank 4310 · last release 2025-11-11 · [PyPI](https://pypi.org/project/pytest-reportlog/)

<details><summary>README extract</summary>

Replacement for the `--resultlog` option, focused in simplicity and extensibility.

Example:
```python
# content of test_report_example.py

def test_ok():
    assert 5 + 5 == 10

def test_fail():
    assert 4 + 4 == 1
```

Sections: pytest-reportlog, Usage, Compression, Example, record_property

</details>

### coveralls

Show coverage stats online via coveralls.io

`pip install coveralls` · installs (wheel) · licence: MIT License · rank 4375 · last release 2026-02-28 · [PyPI](https://pypi.org/project/coveralls/) · [docs](https://coveralls-python.rtfd.io/) · [source](https://github.com/TheKevJames/coveralls-python)

<details><summary>README extract</summary>

:Test Status:

 .. image::
 :target:
 .. image::
 :target:
 .. image::
 :target:
 .. image::
 :target:

:Version Info:

 .. image::
 :target:
 .. image::
 :target:
 .. image::
 :target:
 .. image::
 :target:

:Compatibility:

 .. image::
 :target:
 .. image::
 :target:

:Downloads:

 .. image::
 :target:
 .. image::
 :target:
 .. ...

Sections: Coveralls for Python, Version Compatibility

</details>

### arsenic

Asynchronous WebDriver client

`pip install arsenic` · installs (wheel) · licence: Apache Software License · rank 4466 · last release 2021-08-23 · [PyPI](https://pypi.org/project/arsenic/) · [docs](https://arsenic.readthedocs.io/en/latest/) · [source](https://github.com/HDE/arsenic)

<details><summary>README extract</summary>

Asynchronous webdriver client built on asyncio.

Example:
```python
from arsenic import get_session
from arsenic.browsers import Firefox
from arsenic.services import Geckodriver

async def example():
    # Runs geckodriver and starts a firefox session
    async with get_session(Geckodriver(), Firefox()) as session:
          # go to example.com
          await session.get('
...
```

Sections: Async Webdriver, Quickstart

</details>

### pytest-deadfixtures

A simple plugin to list unused fixtures in pytest

`pip install pytest-deadfixtures` · installs (wheel) · licence: MIT · rank 4500 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pytest-deadfixtures/) · [source](https://github.com/jllorencetti/pytest-deadfixtures)

<details><summary>README extract</summary>

A simple plugin to list unused or duplicated fixtures in a pytest suite.

Features:
- List unused fixtures in your tests
- List duplicated fixtures
- Ignore specific fixtures from analysis with `@deadfixtures_ignore`

Example:
```python
import pytest

from pytest_deadfixtures import deadfixtures_ignore

@pytest.fixture
@deadfixtures_ignore
def intentionally_unused_fixture():
    """This fixture won't be reported as unused."""
    return "something"
```

Sections: pytest-deadfixtures, Features, Usage, Important, Listing unused fixtures, Listing repeated fixtures, Ignoring specific fixtures, Projects using it, Issues

</details>

### pytest-clarity

A plugin providing an alternative, colourful diff output for failing assertions.

`pip install pytest-clarity` · installs from source (sdist only) · licence: MIT License · rank 4522 · last release 2021-06-11 · [PyPI](https://pypi.org/project/pytest-clarity/)

<details><summary>README extract</summary>

A pytest plugin which brings the coloured diff output from the Ward test framework to pytest.

Sections: pytest-clarity, Before, After, Requirements, Usage

</details>

### awscli-local

Thin wrapper around the "aws" command line interface for use with LocalStack

`pip install awscli-local` · installs (wheel) · licence: Apache Software License · rank 4554 · last release 2026-10-21 · [PyPI](https://pypi.org/project/awscli-local/)

<details><summary>README extract</summary>

[][pypi]

> [!WARNING]
> `awslocal` is deprecated. Use `lstk aws` instead.
> `awslocal` no longer receives updates.
> - Get started with `lstk`, the new LocalStack CLI: docs.localstack.cloud/.../lstk
> - Switch your scripts and CI workflows to `lstk aws`: docs.localstack.cloud/.../lstk/migration
> `lstk aws` does not install the AWS CLI for you. ...

Sections: LocalStack AWS CLI, Usage, Example, Configurations, Completion, Usage instructions, Configuration, Limitations, Alternative

</details>

### pytest-freezegun

Wrap tests with fixtures in freeze_time

`pip install pytest-freezegun` · installs (wheel) · licence: MIT License · rank 4563 · last release 2020-07-19 · [PyPI](https://pypi.org/project/pytest-freezegun/)

<details><summary>README extract</summary>

Wrap tests with fixtures in freeze_time

Features:
* Freeze time in both the test and fixtures
* Access the freezer when you need it

Example:
```python
def test_frozen_date(freezer):
    now = datetime.now()
    time.sleep(1)
    later = datetime.now()
    assert now == later
```

Sections: pytest-freezegun, Features, Usage, Issues

</details>

### pynose

pynose fixes nose to extend unittest and make testing easier

`pip install pynose` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 4634 · last release 2025-09-08 · [PyPI](https://pypi.org/project/pynose/) · [docs](https://github.com/mdmintz/pynose) · [source](https://github.com/mdmintz/pynose)

_README extract left out: share-alike licence._

### python-subunit

Python implementation of subunit test streaming protocol

`pip install python-subunit` · installs (wheel) · licence: Apache-2.0 or BSD · rank 4789 · last release 2026-05-04 · [PyPI](https://pypi.org/project/python-subunit/) · [source](https://github.com/testing-cabal/subunit/)

<details><summary>README extract</summary>

subunit: A streaming protocol for test results
 Copyright (C) 2005-2013 Robert Collins <robertc@robertcollins.net>

 Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
 license at the users choice. A copy of both licenses are available in the
 project source as Apache-2.0 and BSD. ...

Sections: Subunit, Integration with other tools, Python, Rust, C, C++, shell, perl, Filter recipes, The xUnit test model, Version 2, Example packets, Version 1 (and 1.1), Hacking on subunit

</details>

### pytest-test-groups

A Pytest plugin for running a subset of your tests by splitting them in to equally sized groups.

`pip install pytest-test-groups` · installs (wheel) · licence: MIT License · rank 4883 · last release 2025-05-08 · [PyPI](https://pypi.org/project/pytest-test-groups/) · [docs](https://github.com/mark-adams/pytest-test-groups) · [source](https://github.com/mark-adams/pytest-test-groups)

<details><summary>README extract</summary>

pytest-test-groups allows you to split your test runs into groups of a specific
size to make it easier to split up your test runs.

Features:
Sometimes you may have some long running test jobs that take a
while to complete. This can be a major headache when trying to
run tests quickly. ...

Sections: Welcome to pytest-test-groups!, Usage, Why would I use this?

</details>

### pytest-logging

Configures logging and allows tweaking the log level with a py.test flag

`pip install pytest-logging` · installs from source (sdist only) · licence: Apache Software License · rank 4909 · last release 2015-11-04 · [PyPI](https://pypi.org/project/pytest-logging/)

<details><summary>README extract</summary>

Configures logging and allows tweaking the log level with a py.test flag

This Pytest plugin was generated with Cookiecutter along with @hackebrot's Cookiecutter-pytest-plugin template.

Features:
* Configures python's logging to output log messages to the console(You need to tell PyTest not to capture output).
* Increases the logging verbosity by lowering the log level by passing `-v` to PyTest

Sections: pytest-logging, Features, Requirements, Usage, Issues

</details>

### robotframework-browser

Robot Framework Browser library powered by Playwright. Aiming for speed, reliability and visibility.

`pip install robotframework-browser` · installs (wheel) · licence: Apache-2.0 · rank 4948 · last release 2026-11-01 · [PyPI](https://pypi.org/project/robotframework-browser/) · [docs](https://marketsquare.github.io/robotframework-browser/Browser.html) · [source](https://github.com/MarketSquare/robotframework-browser)

<details><summary>README extract</summary>

Robot Framework Browser library powered by
Playwright. Propelling browser automation into the future!

Aiming for :rocket: speed, :white_check_mark: reliability and :microscope: visibility.

See keyword documentation and
web page for more details.

Sections: robotframework-browser, Update instructions without NodeJS, Update instructions with NodeJS, Nightly builds, Examples, and extending with JavaScript, Evaluate in browser page, Asynchronously waiting for HTTP requests and responses, Device Descriptors, Sending HTTP requests and parsing their responses, Parallel test execution using Pabot, Re-using authentication credentials, Plugins, Core team

</details>

### codecov

Hosted coverage reports for GitHub, Bitbucket and Gitlab

`pip install codecov` · installs (wheel) · licence: Apache Software License · rank 5084 · last release 2023-04-17 · [PyPI](https://pypi.org/project/codecov/)

### cassetter

Rust-powered HTTP cassette recorder for Python tests. Safe by default.

`pip install cassetter` · installs (wheel) · licence: MIT · rank 5089 · last release 2026-10-29 · [PyPI](https://pypi.org/project/cassetter/) · [source](https://github.com/Kludex/cassetter)

<details><summary>README extract</summary>

Rust-powered HTTP cassette recorder. Safe by default.

Available for Python (this README), Node/TypeScript (`ts/`),
Go (`go/`), and Rust (`crates/cassetter/`).
Every SDK uses the same cassette format.

Features:
VCR.py works, but has fundamental problems:

- Unsafe by default - doesn't filter sensitive headers, tokens, or API keys
- Unsafe YAML - uses `yaml.load()` with an unsafe loader that can execute arbitrary Python code from cassette files ...

Example:
```python
import httpx
import pytest

@pytest.mark.vcr
async def test_api_call():
    async with httpx.AsyncClient() as client:
        response = await client.get("
    assert response.status_code == 200
```

...

</details>

### pytest-nunit

A pytest plugin for generating NUnit3 test result XML output

`pip install pytest-nunit` · installs from source (sdist only) · licence: MIT License · rank 5135 · last release 2024-02-26 · [PyPI](https://pypi.org/project/pytest-nunit/)

<details><summary>README extract</summary>

A pytest plugin for generating NUnit3 test result XML output

Requires:
- Pytest 5.1.0+
- Python 3.7+

A string value to set the file name of the generated XML file.

Argument takes a path to the output file, either relative, or absolute.

Example:
```python
def test_basic(record_nunit_property):
    record_nunit_property("test", "value")
    assert 1 == 1
```

Sections: pytest-nunit, Command-line options, `--nunit-xml`, `--nunit-prefix`, INI Options, `nunit_show_username`, `nunit_show_user_domain`, `nunit_suite_name`, `nunit_attach_on`, Fixtures, `record_nunit_property`, `add_nunit_attachment`, Usage with Azure Pipelines, Skipped Tests

</details>

### allure-combine

Generate single HTML file from allure report.

`pip install allure-combine` · installs (wheel) · licence: MIT License · rank 5219 · last release 2023-06-30 · [PyPI](https://pypi.org/project/allure-combine/)

<details><summary>README extract</summary>

Tool to build allure generated folder into a single html file

After run by console command, or by call from python code, it:

1. Reads contents of allure-generated folder
2. Creates server.js file, which has all the data files inside and code to start fake XHR server
3. ...

Example:
```python
from allure_combine import combine_allure

# 1) Create complete.html in allure-generated folder
combine_allure("./some/path/to/allure/generated/folder")

# 2) Create complete.html in specified folder
combine_allure("./some/path/to/allure/generated/folder", dest_folder="/tmp")

# 3) Make sure that dest folder exists, create if not
combine_allure(
...
```

...

</details>

### robotframework-pabot

Parallel test runner for Robot Framework

`pip install robotframework-pabot` · installs (wheel) · licence: Apache License, Version 2.0 · rank 5254 · last release 2026-02-18 · [PyPI](https://pypi.org/project/robotframework-pabot/) · [source](https://github.com/mkorpela/pabot)

<details><summary>README extract</summary>

中文版

A parallel executor for Robot Framework tests. With Pabot you can split one execution into multiple and save test execution time.

Example:
```python
import sys
from pabot.pabot import main_program

def amazing_new_program():
    print("Before calling pabot")
    exit_code = main_program(['tests'])
    print(f"After calling pabot (return code {exit_code})")
    sys.exit(exit_code)
```

Sections: Pabot, From PyPI, Note, Basic use, Contact, Command-line options, PabotLib, PabotLib example, Controlling execution order, mode, and level of parallelism, Controlling execution order, Programmatic use, Global variables, Output Files Generated by Pabot, Internal File: `.pabotsuitenames`

</details>

### robotframework-jsonlibrary

robotframework-jsonlibrary is a Robot Framework test library for manipulating JSON Object. You can manipulate your JSON object using JSONPath

`pip install robotframework-jsonlibrary` · installs from source (sdist only) · licence: Public Domain · rank 5275 · last release 2022-08-08 · [PyPI](https://pypi.org/project/robotframework-jsonlibrary/)

### teamcity-messages

Send test results to TeamCity continuous integration server from unittest, nose, py.test, twisted trial, behave (Python 2.6+)

`pip install teamcity-messages` · installs (wheel) · licence: Apache Software License · rank 5370 · last release 2025-01-30 · [PyPI](https://pypi.org/project/teamcity-messages/)

<details><summary>README extract</summary>

jb_projectlicensepypi_version|
versionsteamcity_ci|

This package integrates Python with the
TeamCity Continuous Integration
(CI) server. It allows sending "service
messages"
from Python code. Additionally, it provides integration with the
following testing frameworks and tools:

- py.test
- nose
- Django
- unittest (Python standard
 library) ...

Example:
```python
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class Test(unittest.TestCase):
    ...

if name == 'main':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
```

...

</details>

### pytest-homeassistant-custom-component

Experimental package to automatically extract test plugins for Home Assistant custom components

`pip install pytest-homeassistant-custom-component` · installs (wheel) · licence: MIT License · rank 5441 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pytest-homeassistant-custom-component/)

<details><summary>README extract</summary>

Package to automatically extract testing plugins from Home Assistant for custom component testing.
The goal is to provide the same functionality as the tests in home-assistant/core.
pytest-homeassistant-custom-component is updated daily according to the latest homeassistant release including beta.

Example:
```python
from pytest_homeassistant_custom_component.syrupy import HomeAssistantSnapshotExtension
from syrupy.assertion import SnapshotAssertion

@pytest.fixture
def snapshot(snapshot: SnapshotAssertion) -> SnapshotAssertion:
    """Return snapshot assertion fixture with the Home Assistant extension."""
...
```

Sections: pytest-homeassistant-custom-component, Usage, Examples, More Info, Version Strategy

</details>

### pytest-azurepipelines

Formatting PyTest output for Azure Pipelines UI

`pip install pytest-azurepipelines` · installs (wheel) · licence: MIT License · rank 5483 · last release 2023-10-06 · [PyPI](https://pypi.org/project/pytest-azurepipelines/)

<details><summary>README extract</summary>

Making Pytest easier to use with Microsoft Azure Pipelines.

Just run pytest with this plugin and see your test results in the Azure Pipelines UI!

Features:

* Formats the PyTest output to show test docstrings and module names instead of just test case names in the Azure Pipelines UI. ...

Example:
```python
def test_basic(record_pipelines_property):
    record_pipelines_property("test", "value")
    assert 1 == 1
```

Sections: pytest-azurepipelines, Usage, Fixtures, `record_pipelines_property`, `add_pipelines_attachment`, Using the automatic code coverage upload, Running in Docker, Issues

</details>

### rtest-forked-constants

Temporary PyPI fork of rtest 0.0.47 with constructor-call parametrize IDs, pytest-version-aware duplicate IDs, broader static argvalue evaluation, get_args/constructor/factory-call resolution, pytest-compatible IDs for runtime-only expressions, configurable parametrize wrappers, dict .items() expansion, literal-values helpers, star imports, and record attribute IDs. Import and CLI remain `rtest`.

`pip install rtest-forked-constants` · installs (wheel) · licence: MIT License · rank 5547 · last release 2026-10-29 · [PyPI](https://pypi.org/project/rtest-forked-constants/) · [source](https://github.com/ronald-braunstein/rtest.git)

<details><summary>README extract</summary>

A Python test runner built with Rust, featuring high-performance test collection and parallel test execution.

> ⚠️ Development Status: This project is in early development (v0.0.x). Expect bugs, breaking changes, and evolving
> features as we work toward stability. ...

Example:
```python
import rtest

@rtest.mark.cases("value", [1, 2, 3])
def test_example(value):
    assert value > 0

@rtest.mark.skip(reason="Not implemented yet")
def test_skipped():
    pass
```

Sections: rtest, Performance, Quick Start, Basic Usage, Native Runner, Roadmap, Known Limitations, Parametrized Test Discovery, Project-specific parametrize decorators, Literal-values helpers, Pass-through helpers, Functions, comprehensions and types, Records and IDs, Path Separator Handling

</details>

### httmock

A mocking library for requests.

`pip install httmock` · installs (wheel) · licence: Apache Software License · rank 5610 · last release 2020-10-28 · [PyPI](https://pypi.org/project/httmock/)

<details><summary>README extract</summary>

A mocking library for `requests` for Python 2.7 and 3.4+.

Installation

 pip install httmock

Or, if you are a Gentoo user:

 emerge dev-python/httmock

Usage

You can use it to mock third-party APIs and test libraries that use `requests` internally, conditionally using mocked replies with the `urlmatch` decorator: ...

Example:
```python
from httmock import urlmatch, HTTMock
import requests

@urlmatch(netloc=r'(.*\.)?google\.com$')
def google_mock(url, request):
    return 'Feeling lucky, punk?'

with HTTMock(google_mock):
    r = requests.get('
print r.content  # 'Feeling lucky, punk?'
```

</details>

### pytest-cover

Pytest plugin for measuring coverage. Forked from `pytest-cov`.

`pip install pytest-cover` · installs (wheel) · licence: BSD License · rank 5643 · last release 2015-08-01 · [PyPI](https://pypi.org/project/pytest-cover/)

<details><summary>README extract</summary>

`pytest-cover` has been merged back into pytest-cov 2.0.

Sections: pytest-cover, 2.0.2 (2015-07-08), 2.0.1 (2015-07-06), 2.0.0 (2015-06-29), 1.0.0 (2015-06-05)

</details>

### pytest-mergify

Pytest plugin for Mergify

`pip install pytest-mergify` · installs (wheel) · licence: LicenseRef-Mergify-Proprietary · rank 5887 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pytest-mergify/)

<details><summary>README extract</summary>

Find the pytest tests that pass and fail on the same code, and quarantine them so they stop failing your CI. Requires a Mergify account (set `MERGIFY_TOKEN` in CI); free for open source. Why tests go flaky in pytest, and how to fix them: mergify.com/learn/flaky-tests/pytest.

Pytest plugin for Mergify Test Engine.

More information at

Features:
- Test tracing — Sends OpenTelemetry traces for every test to Mergify's API
- Flaky test detection — Intelligently reruns tests to detect flakiness with budget constraints
- Test quarantine — Quarantines failing tests so they don't block CI ...

Sections: pytest-mergify, Features, Configuration, Environment Variables, Bisection steps: failures first, Prerequisites, Setup, Running Tests, Linting

</details>

### pytest-doctestplus

Pytest plugin with advanced doctest features.

`pip install pytest-doctestplus` · installs (wheel) · licence: BSD License · rank 6089 · last release 2026-01-26 · [PyPI](https://pypi.org/project/pytest-doctestplus/)

<details><summary>README extract</summary>

This package contains a plugin for the pytest framework that provides
advanced doctest support and enables the testing of various text files, such
as reStructuredText (".rst"), markdown (".md"), and TeX (".tex"). ...

Example:
```python
``pycon
>>> 1 + 2
2

``
```

Sections: pytest-doctestplus, Motivation, Usage, Setup and Configuration, Running Tests in Markdown Files, Doctest Directives, Sphinx Doctest Directives, Floating Point Comparison, Ignoring warnings, Showing warnings, Skipping Tests, Skipping All the Tests, Skip Unconditionally, Doctest Dependencies

</details>

### pytest-mypy

A Pytest Plugin for Mypy

`pip install pytest-mypy` · installs (wheel) · licence: MIT License · rank 6161 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pytest-mypy/)

<details><summary>README extract</summary>

Mypy static type checker plugin for pytest

Features:
* Runs the mypy static type checker on your source files as part of your pytest test runs.
* Does for mypy what the pytest-flake8 plugin does for flake8.
* This is a work in progress – pull requests appreciated.

Example:
```python
def pytest_configure(config):
    plugin = config.pluginmanager.getplugin('mypy')
    plugin.mypy_argv.append('--check-untyped-defs')
```

Sections: pytest-mypy, Features, Usage, Issues, Meta

</details>

### jenkinsapi

A Python API for accessing resources on a Jenkins continuous-integration server.

`pip install jenkinsapi` · installs (wheel) · licence: MIT License · rank 6165 · last release 2026-04-21 · [PyPI](https://pypi.org/project/jenkinsapi/)

<details><summary>README extract</summary>

Example:
```python
from jenkinsapi.utils.logging import configure_logging

configure_logging("INFO")
```

Sections: Jenkinsapi, Logging, Important Links, About this library, Get details of jobs running on Jenkins server, Disable/Enable a Jenkins Job, Creating jobs in folders, Known issues, Python versions, Jenkins versions

</details>

### robotframework-retryfailed

A listener to automatically retry tests or tasks based on flags.

`pip install robotframework-retryfailed` · installs (wheel) · licence: Apache Software License · rank 6193 · last release 2022-10-09 · [PyPI](https://pypi.org/project/robotframework-retryfailed/)

<details><summary>README extract</summary>

A listener to automatically retry tests or tasks based on tags.

Sections: robotframework-retryfailed, Usage, Attaching Listener, Tagging Tests

</details>

### pytest-assume

A pytest plugin that allows multiple failures per test

`pip install pytest-assume` · installs (wheel) · licence: MIT · rank 6251 · last release 2021-06-24 · [PyPI](https://pypi.org/project/pytest-assume/)

### pytest-unused-fixtures

A pytest plugin to list unused fixtures after a test run.

`pip install pytest-unused-fixtures` · installs (wheel) · licence: MIT License · rank 6350 · last release 2025-12-23 · [PyPI](https://pypi.org/project/pytest-unused-fixtures/) · [source](https://github.com/mikicz/pytest-unused-fixtures)

<details><summary>README extract</summary>

A pytest plugin to list unused fixtures after a test run.

The plugin watches all fixtures which are used in a test run, and then compares it to all the fixtures available in the same test collection. It then prints out all the fixtures which were not used, groupped by where they were defined. ...

Example:
```python
import pytest
from pytest_unused_fixtures import ignore_unused_fixture

@pytest.fixture
@ignore_unused_fixture
def ignored_fixture():
    pass
```

Sections: pytest-unused-fixtures, Options, Usage, Ignoring specific fixtures from report, Thanks, 0.3.1 (Dec 23, 2025), 0.3.0 (Dec 2, 2025), 0.2.1 (Nov 10, 2025), 0.2.0 (Mar 15, 2025), 0.1.5 (Apr 8, 2024), 0.1.4 (Aug 8, 2023), 0.1.3 (Jun 30, 2023), 0.1.2 (Jun 15, 2023), 0.1.1 (Jun 14, 2023)

</details>

### pytest-tornasync

py.test plugin for testing Python 3.5+ Tornado code

`pip install pytest-tornasync` · installs (wheel) · licence: MIT License · rank 6428 · last release 2019-07-15 · [PyPI](https://pypi.org/project/pytest-tornasync/)

<details><summary>README extract</summary>

A simple pytest plugin that provides some helpful fixtures for testing
Tornado (version 5.0 or newer) apps and easy handling of plain
(undecoratored) native coroutine tests (Python 3.5+). ...

Example:
```python
import pytest

@pytest.fixture
def app():
    import yourapp
    return yourapp.make_app()  # a tornado.web.Application
```

Sections: pytest-tornasync, Usage, Fixtures, Examples, Changes, 0.6.0 (2018-11-19), 0.5.0 (2018-05-28)

</details>

### nbval

A py.test plugin to validate Jupyter notebooks

`pip install nbval` · installs (wheel) · licence: BSD License · rank 6461 · last release 2024-03-04 · [PyPI](https://pypi.org/project/nbval/)

<details><summary>README extract</summary>

The plugin adds functionality to py.test to recognise and collect Jupyter
notebooks. The intended purpose of the tests is to determine whether execution
of the stored inputs match the stored outputs of the `.ipynb` file. Whilst also
ensuring that the notebooks are running without errors. ...

Sections: Py.test plugin for validating Jupyter notebooks, How it works, Execution, Coverage, Parallel execution, Documentation, Help

</details>

### pytest-subprocess

A plugin to fake subprocess for pytest

`pip install pytest-subprocess` · installs (wheel) · licence: MIT License · rank 6474 · last release 2026-05-10 · [PyPI](https://pypi.org/project/pytest-subprocess/) · [docs](https://pytest-subprocess.readthedocs.io) · [source](https://github.com/aklajnert/pytest-subprocess)

<details><summary>README extract</summary>

Pytest plugin to fake subprocess.

Features:
* #206: Add fp.regex() for regex-based command argument matching.

Example:
```python
def test_echo_null_byte(fp):
    fp.register(["echo", "-ne", "\x00"], stdout=bytes.fromhex("00"))

    process = subprocess.Popen(
        ["echo", "-ne", "\x00"],
        stdout=subprocess.PIPE,
    )
    out, _ = process.communicate()

    assert process.returncode == 0
    assert out == b"\x00"
```

Sections: pytest-subprocess, Usage, Basic usage, Passing input, Unregistered commands, Differing results, Using callbacks, As a context manager, Non-exact command matching, Regex argument matching, Check if process was called, Check Popen arguments, Handling signals, Documentation

</details>

### pytest-textual-snapshot

Snapshot testing for Textual apps

`pip install pytest-textual-snapshot` · installs (wheel) · licence: MIT License · rank 6500 · last release 2025-01-23 · [PyPI](https://pypi.org/project/pytest-textual-snapshot/)

<details><summary>README extract</summary>

A pytest plugin for snapshot testing Textual applications.

Example:
```python
def test_my_app(snap_compare):
    app = MyTextualApp()  # a *non-running* Textual `App` instance
    assert snap_compare(app)
```

Sections: `pytest-textual-snapshot`, About, Usage, Running tests, My snapshot test failed, what do I do?, Writing tests, Basic usage, Pressing keys, Run code before screenshot, Customizing the size of the terminal, Quickly opening paths in your editor

</details>

### locust-plugins

Useful plugins/extensions for Locust

`pip install locust-plugins` · installs (wheel) · licence: Apache Software License · rank 6561 · last release 2026-06-12 · [PyPI](https://pypi.org/project/locust-plugins/)

### pytest-lazy-fixture

It helps to use fixtures in pytest.mark.parametrize

`pip install pytest-lazy-fixture` · installs (wheel) · licence: MIT License · rank 6573 · last release 2020-02-01 · [PyPI](https://pypi.org/project/pytest-lazy-fixture/)

<details><summary>README extract</summary>

Use your fixtures in `@pytest.mark.parametrize`.

Example:
```python
import pytest

@pytest.fixture(params=[1, 2])
def one(request):
    return request.param

@pytest.mark.parametrize('arg1,arg2', [
    ('val1', pytest.lazy_fixture('one')),
])
def test_func(arg1, arg2):
    assert arg2 in [1, 2]
```

Sections: pytest-lazy-fixture, Usage, Issues

</details>

### pytest-md

Plugin for generating Markdown reports for pytest results

`pip install pytest-md` · installs (wheel) · licence: MIT License · rank 6598 · last release 2019-07-11 · [PyPI](https://pypi.org/project/pytest-md/)

<details><summary>README extract</summary>

Plugin for generating Markdown reports for [pytest] results 📝

Example:
```python
import random
import pytest

def test_failed():
    assert "emoji" == "hello world"

@pytest.mark.xfail
def test_xfailed():
    assert random.random() == 1.0

@pytest.mark.xfail
def test_xpassed():
    assert 0.0 < random.random() < 1.0

@pytest.mark.skip(reason="don't run this test")
def test_skipped():
    assert "pytest-emoji" != ""

...
```

Sections: pytest-md, Usage, pytest-emoji

</details>

### rtfparse

Tool to parse Microsoft Rich Text Format (RTF)

`pip install rtfparse` · installs (wheel) · licence: MIT · rank 6825 · last release 2025-07-08 · [PyPI](https://pypi.org/project/rtfparse/) · [docs](https://github.com/fleetingbytes/rtfparse#readme) · [source](https://github.com/fleetingbytes/rtfparse)

<details><summary>README extract</summary>

Parses Microsoft's Rich Text Format (RTF) documents. It creates an in-memory object which represents the tree structure of the RTF document. This object can in turn be rendered by using one of the renderers.
So far, rtfparse provides only one renderer (`HTML_Decapsulator`) which liberates the HTML code encapsulated in RTF. ...

Example:
```python
from pathlib import Path
from rtfparse.parser import Rtf_Parser
from rtfparse.renderers.html_decapsulator import HTML_Decapsulator

source_path = Path(r"path/to/your/rtf/document.rtf")
target_path = Path(r"path/to/your/html/decapsulated.html")
# Create parent directory of `target_path` if it does not already exist:
...
```

...

</details>

### provide-dir

Provides a directory with all its parent directories, if it does not yet exist

`pip install provide-dir` · installs (wheel) · licence: MIT License · rank 6832 · last release 2022-04-13 · [PyPI](https://pypi.org/project/provide-dir/)

<details><summary>README extract</summary>

Function to create the given path, including potential parent directories. Writes to the provided sink (e.g. `print`) whether the directory was created or whether it already existed.

None

Example:
```python
from pathlib import Path
from provide_dir import provide_dir

needed_path = Path("/path/to/directory/with/subdirectories")
provide_dir(needed_path, print)
```

Sections: provide_directory, Dependencies, Usage, Pip, Test dependencies

</details>

### asv

Airspeed Velocity: A simple Python history benchmarking tool

`pip install asv` · installs (wheel) · licence: BSD-3-Clause · rank 7089 · last release 2026-06-27 · [PyPI](https://pypi.org/project/asv/) · [docs](https://asv.readthedocs.io/en/stable/) · [source](https://github.com/airspeed-velocity/asv)

<details><summary>README extract</summary>

airspeed velocity (`asv`) is a tool for benchmarking Python
packages over their lifetime.

It is primarily designed to benchmark a single project over its
lifetime using a given suite of benchmarks. The results are displayed
in an interactive web frontend that requires only a basic static
webserver to host.

See an example airspeed velocity site. ...

</details>

### robotframework-sshlibrary

Robot Framework test library for SSH and SFTP

`pip install robotframework-sshlibrary` · installs from source (sdist only) · licence: Apache Software License · rank 7164 · last release 2021-11-18 · [PyPI](https://pypi.org/project/robotframework-sshlibrary/)

<details><summary>README extract</summary>

SSHLibrary is a Robot Framework test
library for SSH and SFTP. The project is hosted on GitHub
and downloads can be found from PyPI.

SSHLibrary is operating system independent and supports Python 2.7 as well
as Python 3.4 or newer. In addition to the normal Python interpreter,
it also works with Jython 2.7. ...

Sections: SSHLibrary, Introduction, Documentation, Docker, Usage

</details>

### pytest-trio

Pytest plugin for trio

`pip install pytest-trio` · installs (wheel) · licence: Apache Software License; MIT License · rank 7396 · last release 2022-11-01 · [PyPI](https://pypi.org/project/pytest-trio/)

<details><summary>README extract</summary>

This is a pytest plugin to help you test projects that use Trio, a friendly library for concurrency
and async I/O in Python. For an overview of features, see our manual, or jump straight to the
quickstart guide.

Documentation:

Bug tracker and source code:

License: MIT or Apache 2, your choice. ...

Sections: pytest-trio, Vital statistics

</details>

### robotframework-stacktrace

A listener that prints a Stack Trace to console to faster find the code section where the failure appears.

`pip install robotframework-stacktrace` · installs (wheel) · licence: Apache Software License · rank 7465 · last release 2021-07-12 · [PyPI](https://pypi.org/project/robotframework-stacktrace/)

<details><summary>README extract</summary>

A listener for RF >= 4.0 that prints a Stack Trace to console to faster find the code section where the failure appears.

Sections: robotframework-stacktrace, Usage, Example

</details>

### robotframework-datadriver

A library for Data-Driven Testing.

`pip install robotframework-datadriver` · installs (wheel) · licence: Apache Software License · rank 7478 · last release 2024-06-08 · [PyPI](https://pypi.org/project/robotframework-datadriver/)

<details><summary>README extract</summary>

DataDriver is a Data-Driven extension for Robot Framework®.
This document explains how to use the DataDriver library listener. For
information about installation, support, and more, please visit the
project page

For more information about Robot Framework®, see ...

Sections: DataDriver for Robot Framework®, Python 2, What DataDriver Does, RoboCon 2020 Talk, Alternative approach, How DataDriver Works, Usage, Structure of Test Suite, Requirements, Example Test Suite, Structure of data file, min. required columns, optional columns, Example Data file

</details>

### pytest-remotedata

Pytest plugin for controlling remote data access.

`pip install pytest-remotedata` · installs (wheel) · licence: BSD-3-Clause · rank 7516 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pytest-remotedata/)

<details><summary>README extract</summary>

This package provides a plugin for the pytest framework that allows
developers to control unit tests that require access to data from the internet.
It was originally part of the astropy core package, but has been moved to a
separate package in order to be of more general use. ...

Example:
```python
import pytest
from urllib.request import urlopen

@pytest.mark.remote_data
def test_remote_data():
    urlopen('
```

Sections: pytest-remotedata, Motivation, Usage

</details>

### pytest-xdist-worker-stats

A pytest plugin to list worker statistics after a xdist run.

`pip install pytest-xdist-worker-stats` · installs (wheel) · licence: MIT License · rank 7576 · last release 2026-02-16 · [PyPI](https://pypi.org/project/pytest-xdist-worker-stats/) · [source](https://github.com/mikicz/pytest-xdist-worker-stats)

<details><summary>README extract</summary>

A pytest plugin to list worker statistics after a xdist run.

Sections: pytest-xdist-worker-stats, Usage, Default mode, Summary mode, Breakdown mode, Thanks, 0.4.0 (November 10, 2025), 0.3.1 (November 10, 2025), 0.3.0 (March 15, 2025), 0.2.0 (Apr 16, 2024), 0.1.4 (Aug 8, 2023), 0.1.3 (Aug 8, 2023), 0.1.2 (Jun 19, 2023), 0.1.1 (Jun 15, 2023)

</details>

### PyTestArch

Test framework for software architecture based on imports between modules

`pip install PyTestArch` · installs (wheel) · licence: Apache-2.0 · rank 7578 · last release 2026-10-24 · [PyPI](https://pypi.org/project/PyTestArch/) · [docs](https://zyskarch.github.io/pytestarch/latest) · [source](https://github.com/zyskarch/pytestarch)

<details><summary>README extract</summary>

PyTestArch is an open source library that allows users to define architectural rules and test their code against them. It is
generally inspired by ArchUnit.

Example:
```python
from pytestarch import get_evaluable_architecture

evaluable = get_evaluable_architecture("/home/dummy/project", "/home/dummy/project/src")
```

Sections: Welcome to PyTestArch, Usage Guide, Real-World Example, Further Resources

</details>

### testmuai-selenium-bindings

Testmu binding for Selenium Python — thin test runtime for LambdaTest exports

`pip install testmuai-selenium-bindings` · installs (wheel) · licence: LicenseRef-Proprietary · rank 7597 · last release 2026-10-23 · [PyPI](https://pypi.org/project/testmuai-selenium-bindings/)

<details><summary>README extract</summary>

Python runtime bindings for Selenium-based generated tests.

Example:
```python
import testmu_selenium

testmu_selenium.configure(build="my-build", name="my-test")

@testmu_selenium.test
def my_test(driver):
    driver.get("
    el = testmu_selenium.findElement(driver, [{"selector": "h1", "isXPath": False}])
    assert el is not None

if name == "main":
    testmu_selenium.run(my_test)
```

Sections: testmuai-selenium-bindings, Usage

</details>

### robotframework-seleniumtestability

SeleniumTestability library that helps speed up tests withasyncronous evens

`pip install robotframework-seleniumtestability` · installs (wheel) · licence: Apache Software License · rank 7731 · last release 2023-02-14 · [PyPI](https://pypi.org/project/robotframework-seleniumtestability/)

<details><summary>README extract</summary>

SeleniumTestability is a plugin to Robot Framework's SeleniumLibrary that adds
functionality to it doesn't fit into its mission. These new features are archived
by SL's plugin api that then automatically instrumentents the web application via
javascript calls and provides keywords to bridge those into Robot Framework. ...

Sections: robotframework-seleniumtestability, Usage, Initialize library, Example, Other functionality., Keyword Documentation

</details>

### robotframework-excellib

Robot Framework library for working with Excel documents

`pip install robotframework-excellib` · installs (wheel) · licence: Apache Software License · rank 7778 · last release 2020-06-18 · [PyPI](https://pypi.org/project/robotframework-excellib/)

<details><summary>README extract</summary>

Robot Framework library for working with Excel documents, based on openpyxl.

Sections: Robot Framework Excel Library, Short Description, Documentation, Example

</details>

### django-mock-queries

A django library for mocking queryset functions in memory for testing

`pip install django-mock-queries` · installs (wheel) · licence: MIT · rank 7788 · last release 2026-09-30 · [PyPI](https://pypi.org/project/django-mock-queries/)

<details><summary>README extract</summary>

A library for mocking Django queryset functions in memory for testing

Features:
* QuerySet style support for method chaining
* Filtering with Q objects
* Aggregates generation
* CRUD functions
* Field lookups
* django-rest-framework serializer asserts

Example:
```python
from django.db.models import Avg, Q
from django_mock_queries.query import MockSet, MockModel

qs = MockSet(
    MockModel(mock_name='john', email='john@gmail.com'),
    MockModel(mock_name='jeff', email='jeff@hotmail.com'),
    MockModel(mock_name='bill', email='bill@gmail.com'),
)

...
```

Sections: Django Mock Queries, Features, Examples, Test function that uses Django QuerySet, Test django-rest-framework model serializer, Full Example, TODO

</details>

### mock-ssh-server

Mock SSH server for testing purposes

`pip install mock-ssh-server` · installs (wheel) · licence: MIT License · rank 7842 · last release 2021-09-13 · [PyPI](https://pypi.org/project/mock-ssh-server/)

<details><summary>README extract</summary>

Example:
```python
import os

from pytest import yield_fixture

import mockssh

@yield_fixture()
def server():
    users = {
        "sample-user": "/path/to/user-private-key",
    }
    with mockssh.Server(users) as s:
        yield s

def test_ssh_session(server):
    for uid in server.users:
        with server.client(uid) as c:
...
```

</details>

### laboratory

Sure-footed refactoring achieved through experimenting

`pip install laboratory` · installs (wheel) · licence: MIT License · rank 7889 · last release 2019-05-05 · [PyPI](https://pypi.org/project/laboratory/)

<details><summary>README extract</summary>

A Python library for carefully refactoring critical paths by testing in
production (inspired by GitHub's Scientist) with support for Python 2.7, 3.3+

Features:
Some blocks of code are more critical than the rest. Laboratory helps us refactor important
code paths by running experiments in production and verifying the results. ...

Example:
```python
import laboratory

# set up the experiment and define control and candidate functions
experiment = laboratory.Experiment()
experiment.control(authorise_control, args=[user], kwargs={'action': action})
experiment.candidate(authorise_candidate, args=[user], kwargs={'action': action})

# conduct the experiment and return the control value
...
```

...

</details>

### pytest-fail-slow

Fail tests that take too long to run

`pip install pytest-fail-slow` · installs (wheel) · licence: MIT License · rank 7921 · last release 2024-06-01 · [PyPI](https://pypi.org/project/pytest-fail-slow/) · [source](https://github.com/jwodder/pytest-fail-slow)

<details><summary>README extract</summary>

GitHub
| PyPI
| Issues
| Changelog

`pytest-fail-slow` is a pytest plugin for treating tests as failed if they
took too long to run. It adds markers for failing tests if they or their setup
stages run for longer than a given duration, along with command-line options
for applying the same cutoff to all tests. ...

Example:
```python
import pytest

@pytest.mark.fail_slow("5s")
def test_something_sluggish():
    ...
```

Sections: Usage, Failing Slow Tests, Failing Slow Setups, Specifying Durations

</details>

### behavex

Production-grade test orchestration for Python BDD.

`pip install behavex` · installs (wheel) · licence: not stated · rank 7962 · last release 2026-10-21 · [PyPI](https://pypi.org/project/behavex/)

<details><summary>README extract</summary>

> Production-grade test orchestration for Python BDD.

BehaveX extends Behave with parallel execution, enterprise-grade reporting, and the operational controls needed to run test suites at scale. Downloaded 121,000+ times per month. ...

Sections: BehaveX, ✨ Latest Features, Quick Start, BehaveX vs Behave, Who Uses BehaveX, Documentation, Get Involved

</details>

### pulumi-local

Thin wrapper script to use Pulumi with LocalStack

`pip install pulumi-local` · installs from source (sdist only) · licence: Apache Software License · rank 8036 · last release 2024-09-30 · [PyPI](https://pypi.org/project/pulumi-local/)

<details><summary>README extract</summary>

<u>DISCLAIMER</u>: pulumi-local currently does not support the _aws-native package. (pulumi/pulumi-aws-native #108)

This package provides the `pulumilocal` command, which is a thin wrapper around the `pulumi`
command line interface to use `Pulumi` with LocalStack.

Sections: Pulumi CLI for LocalStack, Prerequisites, Usage, Create a new Pulumi project with stack name lsdev, Select and create the lsdev Pulumi stack, Deploy the stack to LocalStack, How it works, Configurations, Deploying to AWS

</details>

### tap.py

Test Anything Protocol (TAP) tools

`pip install tap.py` · installs (wheel) · licence: BSD License · rank 8076 · last release 2025-01-26 · [PyPI](https://pypi.org/project/tap.py/)

<details><summary>README extract</summary>

tappy is a set of tools for working with the Test Anything Protocol (TAP), a line based test protocol for recording test
data in a standard way.

Follow tappy development on GitHub.
Developer documentation is on
Read the Docs.

</details>

### pytest-filter-subpackage

Pytest plugin for filtering based on sub-packages

`pip install pytest-filter-subpackage` · installs (wheel) · licence: BSD License · rank 8127 · last release 2024-03-04 · [PyPI](https://pypi.org/project/pytest-filter-subpackage/)

<details><summary>README extract</summary>

This package contains a simple plugin for the pytest framework that provides a
shortcut to testing all code and documentation for a given sub-package.

Sections: pytest-filter-subpackage, Usage

</details>

### pytest-localserver

pytest plugin to test server connections locally.

`pip install pytest-localserver` · installs (wheel) · licence: MIT · rank 8307 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pytest-localserver/)

<details><summary>README extract</summary>

pytest-localserver is a plugin for the pytest testing framework which enables
you to test server connections locally.

Sometimes monkeypatching `urllib2.urlopen()` just does not cut it, for
instance if you work with `urllib2.Request`, define your own openers/handlers
or work with `httplib`. ...

Example:
```python
import requests

def make_request(url):
    """A function that makes a web request."""
    rsp = requests.get(url)
    return rsp.text
```

Sections: pytest-localserver, Quickstart, How-To, Fixtures, Using your a WSGI application as test server

</details>

### pytest-pythonpath

pytest plugin for adding to the PYTHONPATH from command line or configs.

`pip install pytest-pythonpath` · installs (wheel) · licence: MIT License · rank 8323 · last release 2022-02-10 · [PyPI](https://pypi.org/project/pytest-pythonpath/)

<details><summary>README extract</summary>

NOTE: This plugin is obsolete as of pytest 7.0.0. Thanks to this PR from Brian Okken, you can now modify the PYTHONPATH using the `pythonpath` configuration option. See documentation here:

This is a py.test plugin for adding to the PYTHONPATH from the pytests.ini file before tests run.

Installation

Install with pip:: ...

</details>

### pytest-twisted

A twisted plugin for pytest.

`pip install pytest-twisted` · installs (wheel) · licence: BSD License · rank 8336 · last release 2024-09-10 · [PyPI](https://pypi.org/project/pytest-twisted/)

<details><summary>README extract</summary>

:Authors: Ralf Schmitt, Kyle Altendorf, Victor Titor
:Version: 1.14.3
:Date: 2024-08-21
:Download:
:Code:

pytest-twisted is a plugin for pytest, which allows to test code,
which uses the twisted framework. test functions can return Deferred
objects and pytest will wait for their completion with this plugin.

Example:
```python
@pytest_twisted.inlineCallbacks
def test_some_stuff(tmpdir):
    res = yield threads.deferToThread(os.listdir, tmpdir.strpath)
    assert res == []
```

Sections: pytest-twisted - test twisted code with pytest, Using the plugin, inlineCallbacks, ensureDeferred, Waiting for deferreds in fixtures, async/await fixtures, Hypothesis, The twisted greenlet, Deprecations, v1.9

</details>

### coverage-badge

Generate coverage badges for Coverage.py.

`pip install coverage-badge` · installs (wheel) · licence: MIT License · rank 8363 · last release 2024-08-02 · [PyPI](https://pypi.org/project/coverage-badge/)

### pytest-tap

Test Anything Protocol (TAP) reporting plugin for pytest

`pip install pytest-tap` · installs (wheel) · licence: BSD License · rank 8450 · last release 2025-01-30 · [PyPI](https://pypi.org/project/pytest-tap/)

<details><summary>README extract</summary>

pytest-tap is a reporting plugin for pytest that outputs
Test Anything Protocol (TAP) data.
TAP is a line based test protocol for recording test data in a standard way.

Use `pytest --tap` after installing to get started.

Follow GitHub
for more information or to follow this plugin's development. ...

Sections: Version 3.5, January 30, 2025, Version 3.4, July 15, 2023, Version 3.3, October 27, 2021, Version 3.2, November 7, 2020

</details>

### callee

Argument matchers for unittest.mock

`pip install callee` · installs from source (sdist only) · licence: BSD License · rank 8451 · last release 2019-12-24 · [PyPI](https://pypi.org/project/callee/)

### terraform-local

Thin wrapper script to run Terraform against LocalStack

`pip install terraform-local` · installs (wheel) · licence: Apache Software License · rank 8469 · last release 2026-10-21 · [PyPI](https://pypi.org/project/terraform-local/)

<details><summary>README extract</summary>

> [!WARNING]
> `tflocal` is deprecated. Use `lstk terraform` instead.
> `tflocal` no longer receives updates.
> - Get started with `lstk`, the new LocalStack CLI: docs.localstack.cloud/.../lstk
> - Switch your scripts and CI workflows to `lstk terraform`: docs.localstack.cloud/.../lstk/migration ...

Sections: `tflocal` - Terraform with LocalStack, Prerequisites, How it works, 1) Recommended: Using pipx, 2) Alternative: Using a Virtual Environment, Activate it, Configurations, Usage, Validation errors when using local terraform modules

</details>

### robotframework-selenium2library

Web testing library for Robot Framework

`pip install robotframework-selenium2library` · installs (wheel) · licence: Apache Software License · rank 8493 · last release 2017-12-04 · [PyPI](https://pypi.org/project/robotframework-selenium2library/)

<details><summary>README extract</summary>

Selenium2Library is a web testing library for Robot Framework
that uses the Selenium tool internally. The project is hosted on
GitHub and downloads can be found from PyPI.

Starting from version 3.0, Selenium2Library is renamed to SeleniumLibrary
and this project exists mainly to help with transitioning. ...

Sections: Selenium2Library, Versions, Keyword documentation, Migrating to SeleniumLibrary

</details>

### pytest-arraydiff

pytest plugin to help with comparing array output from tests

`pip install pytest-arraydiff` · installs (wheel) · licence: BSD-3-Clause · rank 8571 · last release 2026-06-02 · [PyPI](https://pypi.org/project/pytest-arraydiff/)

<details><summary>README extract</summary>

This is a py.test plugin to facilitate the
generation and comparison of data arrays produced during tests, in particular
in cases where the arrays are too large to conveniently hard-code them
in the tests (e.g. `np.testing.assert_allclose(x, [1, 2, 3])`). ...

Example:
```python
E               AssertionError:
E
E               a: /var/folders/zy/t1l3sx310d3d6p0kyxqzlrnr0000gr/T/tmpbvjkzt_q/test_to_mask_rect-mode_subpixels-subpixels_18.txt
E               b: /var/folders/zy/t1l3sx310d3d6p0kyxqzlrnr0000gr/T/tmpbvjkzt_q/reference-test_to_mask_rect-mode_subpixels-subpixels_18.txt
E
...
```

Sections: About, Using, Options, Test failure example, Running the tests for pytest-arraydiff

</details>

### tavern

Simple testing of RESTful APIs

`pip install tavern` · installs (wheel) · licence: MIT License · rank 8653 · last release 2026-10-28 · [PyPI](https://pypi.org/project/tavern/) · [docs](https://tavern.readthedocs.io/en/latest/) · [source](https://github.com/taverntesting/tavern)

<details><summary>README extract</summary>

Features:
Choosing an API testing framework can be tough. Tavern was started in 2017 to address some of our concerns with other
testing frameworks.

In short, we think the best things about Tavern are:

Sections: Why Tavern, It's Lightweight., Easy to Write, Easy to Read and Understand., Test Anything, Extensible, Growing Ecosystem, Quickstart, Why not Postman, Insomnia or pyresttest etc?, Hacking on Tavern, Maintenance

</details>

### pytest-astropy

Meta-package containing dependencies for testing

`pip install pytest-astropy` · installs (wheel) · licence: BSD License · rank 8735 · last release 2026-08-03 · [PyPI](https://pypi.org/project/pytest-astropy/)

<details><summary>README extract</summary>

This is a meta-package that pulls in the dependencies that are used by
astropy and some affiliated packages for testing. It can also be used for
testing packages that are not affiliated with the Astropy project.

The package also provides the short option `-R` for `--remote-data`.

The following dependencies are installed by this package: ...

Sections: pytest-astropy, Dependencies

</details>

### aiointercept

aiohttp mock library that routes requests through a real test server

`pip install aiointercept` · installs (wheel) · licence: MIT · rank 8813 · last release 2026-10-12 · [PyPI](https://pypi.org/project/aiointercept/) · [source](https://github.com/Polandia94/aiointercept)

<details><summary>README extract</summary>

Mock `aiohttp` HTTP requests by routing them through a real `aiohttp.web` test server. Inspired by `aioresponses`, with a largely compatible API.

Features:
Testing code that makes HTTP requests usually means either hitting a real server (slow, fragile, requires network) or replacing the HTTP layer with fake objects (fast, but disconnected from reality). ...

Example:
```python
import aiohttp
from aiointercept import aiointercept

async with aiointercept() as m:
    m.get(f"{m.server_url}/users", payload=[{"id": 1}])

    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"{m.server_url}/users")
        assert await resp.json() == [{"id": 1}]
```

...

</details>

### sure

utility belt for automated testing in python for python

`pip install sure` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 8845 · last release 2023-02-06 · [PyPI](https://pypi.org/project/sure/)

_README extract left out: share-alike licence._

### pytest-incremental

an incremental test runner (pytest plugin)

`pip install pytest-incremental` · installs from source (sdist only) · licence: MIT License · rank 8850 · last release 2021-04-24 · [PyPI](https://pypi.org/project/pytest-incremental/)

<details><summary>README extract</summary>

an incremental test runner (pytest plug-in)

*pytest-incremental* analyses your project structure and file
modifications between test-runs
to modify the order tests are executed and de-select tests.
This allows a much faster feedback for interactive test execution. ...

Sections: pytest-incremental, Project Details

</details>

### fest-mutate

An extremely fast mutation testing tool for Python

`pip install fest-mutate` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 8851 · last release 2026-03-14 · [PyPI](https://pypi.org/project/fest-mutate/) · [source](https://github.com/sakost/fest)

<details><summary>README extract</summary>

An extremely fast mutation testing tool for Python.

fest generates small changes (_mutants_) to your Python source code and checks whether your test
suite catches them. Surviving mutants reveal gaps that line coverage alone cannot find.

Built in Rust with ruff's Python parser. ~25× faster than
cosmic-ray on real-world projects
(benchmark).

Features:
- 🔥 Parallel execution — runs mutants across all CPU cores simultaneously
- 🎯 Coverage-guided — only runs tests that cover the mutated line, via per-test `pytest-cov` context ...

Sections: fest, Highlights, From PyPI (recommended), From source, Quick start, Configuration, CLI, Mutation operators, Backends, Performance

</details>

### pytest-run-parallel

A simple pytest plugin to run tests concurrently

`pip install pytest-run-parallel` · installs (wheel) · licence: MIT · rank 8878 · last release 2026-08-04 · [PyPI](https://pypi.org/project/pytest-run-parallel/) · [source](https://github.com/Quansight-Labs/pytest-run-parallel)

<details><summary>README extract</summary>

A simple pytest plugin to run tests concurrently

This pytest plugin takes a set
of tests that would be normally be run serially and execute them in
parallel.

The main goal of `pytest-run-parallel` is to discover thread-safety
issues that could exist when using C libraries, this is of vital
importance after PEP703, which
provides a path for a ...

Features:
- `--parallel-threads` to run a test suite in parallel
 - `--iterations` to run multiple times in each thread
 - `--skip-thread-unsafe` to skip running tests marked as or
 detected to be thread-unsafe. ...

Example:
```python
# test_file.py
import pytest

@pytest.fixture
def my_fixture():
    ...

@pytest.mark.force_parallel_threads(2)
@pytest.mark.iterations(10)
def test_something_1():
...

</details>

### pytest-timer

A timer plugin for pytest

`pip install pytest-timer` · installs (wheel) · licence: MIT License · rank 8988 · last release 2023-12-26 · [PyPI](https://pypi.org/project/pytest-timer/)

<details><summary>README extract</summary>

Porting of nose-timer plugin for pytest. A timer plugin for pytest (how much time does every test take?).

Sections: pytest-timer, Usage, How do I show only the `n` slowest tests?, How do I turn off pretty colors?, How do I filter results by colors?

</details>

### pytest-console-scripts

Pytest plugin for testing console scripts

`pip install pytest-console-scripts` · installs (wheel) · licence: MIT License · rank 9078 · last release 2023-05-31 · [PyPI](https://pypi.org/project/pytest-console-scripts/)

<details><summary>README extract</summary>

Pytest-console-scripts is a pytest plugin for running python scripts from
within tests. It's quite similar to `subprocess.run()`, but it also has an
in-process mode, where the scripts are executed by the interpreter that's
running `pytest` (using some amount of sandboxing). ...

Example:
```python
setup(
    name='foo',
    version='0.0.1',
    py_modules=['foo'],
    entry_points={
        'console_scripts': ['foobar=foo:bar']
    },
)
```

</details>

### pretend

A library for stubbing in Python

`pip install pretend` · installs (wheel) · licence: BSD License · rank 9088 · last release 2018-04-14 · [PyPI](https://pypi.org/project/pretend/)

<details><summary>README extract</summary>

Pretend is a library to make stubbing with Python easier.

Stubbing is a technique for writing tests. You may hear the term mixed up with
mocks, fakes, or doubles. Basically a stub is an object that returns pre-canned
responses, rather than doing any computation.

Martin Fowler does a good job explaining the terms in his Mocks Aren't Stubs
article.

Features:
Ideally stubbing tests how your system responds to a particular input, rather
than which API is used. Stubbing still requires you to write tests that check
the results of a computation, rather than looking for side effects. ...

Example:
```python
>>> from pretend import stub
>>> x = stub(country_code="US")
>>> some_function(x)
```

...

</details>

### pytest-json

Generate JSON test reports

`pip install pytest-json` · installs from source (sdist only) · licence: MIT License · rank 9188 · last release 2016-01-18 · [PyPI](https://pypi.org/project/pytest-json/)

<details><summary>README extract</summary>

pytest-json is a plugin for py.test that generates JSON
reports for test results

This Pytest plugin was generated with Cookiecutter along with
@hackebrot's Cookiecutter-pytest-plugin template.

- Python 2.7, 3.3, 3.4, 3.5
- py.test 2.7 or newer

Example:
```python
@pytest.fixture(scope='session', autouse=True):
def extra_json_environment(request):
    request.config._json_environment.append(('herp', 'derp'))
```

Sections: pytest-json, Requirements, Usage, Adding to environment, Adding metadata per test stage, Addint metadata per test, Compatibility with pytest-html, Example json, Issues

</details>

### pytest-xvfb

A pytest plugin to run Xvfb (or Xephyr/Xvnc) for tests.

`pip install pytest-xvfb` · installs (wheel) · licence: MIT License · rank 9203 · last release 2025-03-12 · [PyPI](https://pypi.org/project/pytest-xvfb/)

<details><summary>README extract</summary>

A pytest plugin to run Xvfb (or Xephyr/Xvnc) for tests.

Features:
You can pass `--no-xvfb` to explicitly turn off Xvfb (e.g. to visually
inspect a failure).

With `--xvfb-backend xephyr` or `--xvfb-backend xvnc`, you can use Xephyr
or Xvnc in place of Xvfb, e.g. to visually inspect failures. ...

Sections: pytest-xvfb, Usage, Features, Thanks, Issues

</details>

### moto-ext

A library that allows you to easily mock out tests based on AWS infrastructure

`pip install moto-ext` · installs (wheel) · licence: Apache-2.0 · rank 9231 · last release 2026-11-02 · [PyPI](https://pypi.org/project/moto-ext/)

<details><summary>README extract</summary>

Fork of Moto with patches and fixes for LocalStack for AWS.

</details>

### django-nose

Makes your Django tests simple and snappy

`pip install django-nose` · installs (wheel) · licence: BSD License · rank 9248 · last release 2020-08-20 · [PyPI](https://pypi.org/project/django-nose/)

<details><summary>README extract</summary>

django-nose provides all the goodness of nose in your Django tests, like:

* Testing just your apps by default, not all the standard ones that happen to
 be in `INSTALLED_APPS`
* Running the tests in one or more specific modules (or apps, or classes, or
 folders, or just running a specific test)
* Obviating the need to import all your tests into ...

Sections: django-nose, Note to users, 1.4.7 (2020-08-19), 1.4.6 (2018-10-03), 1.4.5 (2017-08-22), 1.4.4 (2016-06-27), 1.4.3 (2015-12-28), 1.4.2 (2015-10-07), 1.4.1 (2015-06-29), 1.4 (2015-04-23), 1.3 (2014-12-05), 1.2 (2013-07-23), 1.1 (2012-05-19), 1.0 (2012-03-12)

</details>

### dbldatagen

Databricks Labs - PySpark Synthetic Data Generator

`pip install dbldatagen` · installs (wheel) · licence: Databricks License · rank 9314 · last release 2024-07-26 · [PyPI](https://pypi.org/project/dbldatagen/) · [docs](https://databrickslabs.github.io/dbldatagen/public_docs/index.html)

<details><summary>README extract</summary>

<!-- Top bar will be removed from PyPi packaged versions -->


<!--


The `dbldatagen` Databricks Labs project is a Python library for generating synthetic data within the Databricks
environment using Spark. The generated data may be used for testing, benchmarking, demos, and many
other uses. ...

Features:
It supports:
* Generating synthetic data at scale up to billions of rows within minutes using appropriately sized clusters
* Generating repeatable, predictable data supporting the need for producing multiple tables, Change Data Capture,
merge and ...

Sections: Databricks Labs Data Generator (`dbldatagen`), Project Description, Feature Summary, Documentation, Compatibility, Using the Data Generator, Spark and Databricks Runtime Compatibility, Feedback

</details>

### nox-uv

Facilitate nox integration with uv for Python projects

`pip install nox-uv` · installs (wheel) · licence: MIT · rank 9383 · last release 2026-05-12 · [PyPI](https://pypi.org/project/nox-uv/) · [source](https://github.com/dantebben/nox-uv)

<details><summary>README extract</summary>

[](
[](
[](
[](
[](
[](
[](
[](

`nox-uv` is a simple drop-in replacement for nox's `@nox.session` that
installs dependencies constrained by uv's lockfile.

Example:
```python
from nox import Session, options
from nox_uv import session

options.default_venv_backend = "uv"

@session(
    python=["3.10", "3.11", "3.12", "3.13", "3.14"],
    uv_groups=["test"],
)
def test(s: Session) -> None:
    s.run("python", "-m", "pytest")

@session(uv_groups=["type_check"])
def type_check(s: Session) -> None:
    s.run("mypy", "src")
...
```

Sections: Intro, Usage, Added parameters, Inspiration

</details>

### yang.connector

YANG defined interface API protocol connector

`pip install yang.connector` · installs (wheel) · licence: Apache Software License · rank 9472 · last release 2026-11-03 · [PyPI](https://pypi.org/project/yang.connector/)

### bluezoo

A mock for the BlueZ D-Bus API

`pip install bluezoo` · installs (wheel) · licence: GPL-2.0-only · rank 9734 · last release 2025-09-15 · [PyPI](https://pypi.org/project/bluezoo/)

_README extract left out: share-alike licence._

### aiohttp-asgi-connector

AIOHTTP Connector for running ASGI applications

`pip install aiohttp-asgi-connector` · installs (wheel) · licence: BSD-3-Clause-Clear · rank 9762 · last release 2026-09-24 · [PyPI](https://pypi.org/project/aiohttp-asgi-connector/)

<details><summary>README extract</summary>

An AIOHTTP `ClientSession` connector for interacting with ASGI applications.

This library intends to increase the parity between AIOHTTP and HTTPX, specifically with HTTPX's `AsyncClient`. ...

Example:
```python
import asyncio
from typing import Annotated  # or from typing_extensions

from aiohttp_asgi_connector import ASGIApplicationConnector
from aiohttp import ClientSession
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/ping")
async def pong(message: Annotated[str, Body(embed=True)]):
...
```

Sections: aiohttp-asgi-connector, Usage

</details>

### pytest-circleci-parallelized

Parallelize pytest across CircleCI workers.

`pip install pytest-circleci-parallelized` · installs from source (sdist only) · licence: MIT License · rank 9855 · last release 2022-10-20 · [PyPI](https://pypi.org/project/pytest-circleci-parallelized/)

<details><summary>README extract</summary>

Parallelize pytest across CircleCI workers.

Features:
Leverage the builtin parallelism of CircleCI to run your test suites. Call `pytest` with the `--circleci-parallelize` flag to automatically split tests amongst nodes using the `circleci tests split` utility. ...

Sections: pytest-circleci-parallelized, Features, Issues

</details>

### TestSlide

A test framework for Python that makes mocking and iterating over code with tests a breeze

`pip install TestSlide` · installs from source (sdist only) · licence: MIT License · rank 9862 · last release 2023-03-16 · [PyPI](https://pypi.org/project/TestSlide/)

<details><summary>README extract</summary>

A test framework for Python that enable unit testing / TDD / BDD to be productive and enjoyable.

Its well behaved mocks with thorough API validations catches bugs both when code is first written or long in the future when it is changed. ...

Example:
```python
class Backup:
  def delete(self, path):
    pass
```

Sections: Quickstart, Full documentation, Requirements, Terms of Use, Privacy Policy, Copyright

</details>

### postgresql-proxy

Postgresql Proxy

`pip install postgresql-proxy` · installs from source (sdist only) · licence: Apache Software License · rank 10177 · last release 2026-05-27 · [PyPI](https://pypi.org/project/postgresql-proxy/)

### testmuai-playwright-bindings

TestMu binding for Playwright Python — thin test runtime for TestMu-exported tests on the LambdaTest grid

`pip install testmuai-playwright-bindings` · installs (wheel) · licence: MIT · rank 10206 · last release 2026-11-06 · [PyPI](https://pypi.org/project/testmuai-playwright-bindings/) · [source](https://github.com/LambdaTest/testmuai-bindings)

<details><summary>README extract</summary>

TestMu binding for Playwright Python — a thin test runtime for running TestMu-exported tests locally or on the LambdaTest grid.

Features:
- `@testmu.test` — decorator that wraps async Playwright tests with session lifecycle management
- `testmu.step(...)` — context manager for structured test steps ...

Example:
```python
import testmu

@testmu.test
async def my_test(page):
    async with testmu.step("Open site"):
        await page.goto("

    async with testmu.step("Verify title"):
        await testmu.expect(page).to_have_title("Example Domain")

testmu.run(my_test)
```

Sections: testmuai-playwright-bindings, Quick Start, Configuration, Runtime modes (`kane_version`), Features, Requirements, Links

</details>

### pure-python-adb

Pure python implementation of the adb client

`pip install pure-python-adb` · installs from source (sdist only) · licence: MIT License · rank 10331 · last release 2020-08-05 · [PyPI](https://pypi.org/project/pure-python-adb/)

<details><summary>README extract</summary>

From version v0.2.1-dev, the package name has been renamed from 'adb' to 'ppadb' to avoid conflit with Google google/python-adb

This is pure-python implementation of the ADB client.

You can use it to communicate with adb server (not the adb daemon on the device/emulator).

When you use `adb` command ...

Example:
```python
from ppadb.client import Client as AdbClient
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
print(client.version())

>>> 39
```

Sections: The package name has been renamed from 'adb' to 'ppadb', Introduction, Requirements, Examples, Connect to adb server and get the version, Connect to a device, adb shell, Screenshot, Push file or folder, Pull, Connect to device, Enable debug logger, Async Client, How to run test cases

</details>

### pytest-reporter

Generate Pytest reports with templates

`pip install pytest-reporter` · installs (wheel) · licence: MIT License · rank 10516 · last release 2024-02-28 · [PyPI](https://pypi.org/project/pytest-reporter/)

<details><summary>README extract</summary>

Generate Pytest reports from templates. You may use one of the available
templates on PyPI (like the reference template pytest-reporter-html1),
inherit them in your own template to tweak their content and appearence or
make your own from scratch.

Anything text based can be generated like HTML, LaTeX, CSV et.c.

Example:
```python
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

def pytest_reporter_render(template_name, dirs, context):
    env = Environment(loader=FileSystemLoader(dirs))
    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        # Don't know about this name, may be provided by some other template
...
```

Sections: pytest-reporter, Usage, Writing templates, The template context, Hooks, Issues

</details>

### napari-svg

A plugin for writing svg files with napari

`pip install napari-svg` · installs (wheel) · licence: BSD License · rank 10532 · last release 2025-01-14 · [PyPI](https://pypi.org/project/napari-svg/) · [source](https://github.com/napari/napari-svg)

<details><summary>README extract</summary>

A plugin for writing svg files with napari

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:

and review the napari docs for plugin developers:


Sections: napari-svg, Issues

</details>

### tempdir

Tempdirs are temporary directories, based on tempfile.mkdtemp

`pip install tempdir` · installs from source (sdist only) · licence: MIT License · rank 10575 · last release 2016-03-02 · [PyPI](https://pypi.org/project/tempdir/)

<details><summary>README extract</summary>

Having to manually manage temporary directories is annoying.
So this class encapsulates temporary directories which just disappear after use,
including contained directories and files.
Temporary directories are created with tempfile.mkdtemp and thus save from race conditions.
Cleanup might not work on windows if files are still opened.

</details>

### napari-console

A plugin that adds a console to napari

`pip install napari-console` · installs (wheel) · licence: BSD License · rank 10729 · last release 2026-10-22 · [PyPI](https://pypi.org/project/napari-console/) · [source](https://github.com/napari/napari-console)

<details><summary>README extract</summary>

A plugin that adds a console to [napari]. This plugin is maintained by the [@napari] team.

`napari-console` adds an interactive console based on IPython to `napari`. The napari UI contains a
console button to display the
console. This button is enabled if you launch napari from the command line, a script, or use the
napari bundled app.

Example:
```python
import napari
import numpy as np
from scipy import ndimage as ndi

image = np.random.random((500, 500))
labels = ndi.label(image > 0.7)[0]

viewer, image_layer = napari.imshow(image)
labels_layer = viewer.add_labels(labels)

napari.run()
```

Sections: napari-console, Issues, Local variables and napari-console

</details>

### robotframework-extendedselenium2library

Extended Selenium2 web testing library for Robot Framework with AngularJS support

`pip install robotframework-extendedselenium2library` · installs from source (sdist only) · licence: GNU Affero General Public License v3 · rank 10794 · last release 2018-04-09 · [PyPI](https://pypi.org/project/robotframework-extendedselenium2library/)

_README extract left out: share-alike licence._

### snappi

The Snappi Open Traffic Generator Python Package

`pip install snappi` · installs (wheel) · licence: MIT · rank 10861 · last release 2026-10-12 · [PyPI](https://pypi.org/project/snappi/) · [source](https://github.com/open-traffic-generator/snappi)

<details><summary>README extract</summary>

Test scripts written in `snappi`, an auto-generated python SDK, can be executed against any traffic generator conforming to Open Traffic Generator API.

Ixia-c is one such reference implementation of Open Traffic Generator API.

> The repository is under active development and is subject to updates. ...

</details>

### behave-html-formatter

HTML formatter for Behave

`pip install behave-html-formatter` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10922 · last release 2022-06-30 · [PyPI](https://pypi.org/project/behave-html-formatter/)

_README extract left out: share-alike licence._

### pytest-manual-marker

pytest marker for marking manual tests

`pip install pytest-manual-marker` · installs (wheel) · licence: MIT · rank 10944 · last release 2026-10-13 · [PyPI](https://pypi.org/project/pytest-manual-marker/)

<details><summary>README extract</summary>

Pytest marker for tests that need a person to execute them.

Tests marked `manual` are not run; they are reported with their own
`manual` outcome (`M` in the progress line) instead of passing or failing.

Example:
```python
# content of test_manual.py
import pytest

@pytest.mark.manual
def test_manual():
    """this needs a person to run it and reports MANUAL as its outcome"""

def test_automated():
    """an empty automated test, for show"""
```

Sections: pytest-manual-marker, Usage, run everything, reporting manual tests, only manual tests, only automated tests

</details>

### behavex-images

BehaveX extension library to attach images to the test execution report.

`pip install behavex-images` · installs (wheel) · licence: MIT License · rank 11112 · last release 2025-08-15 · [PyPI](https://pypi.org/project/behavex-images/) · [source](https://github.com/abmercado19/behavex-images)

<details><summary>README extract</summary>

An extension for the BehaveX library that enables attaching images to the generated HTML report.

Features:
- Attach images to BehaveX HTML reports
- Support for both binary image data and image files
- Flexible attachment conditions (always, only on failure, or never)
- Easy integration with existing BehaveX projects

Example:
```python
from behavex_images import image_attachments

image_attachments.attach_image_binary(context, image_binary)
```

Sections: behavex-images, Features, Usage, 1. Attach Image from Binary Data, 2. Attach Image from File, 3. Set Attachment Condition, 4. Clean All Attached Images, Examples, Attaching an Image in a Step Definition, Using Hooks in environment.py, Sample Report Output

</details>

### pytest-replay

Saves previous test runs and allow re-execute previous pytest runs to reproduce crashes or flaky tests

`pip install pytest-replay` · installs (wheel) · licence: MIT License · rank 11619 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pytest-replay/)

<details><summary>README extract</summary>

Saves previous test runs and allow re-execute previous pytest runs to reproduce crashes or flaky tests

This pytest plugin was generated with Cookiecutter along with @hackebrot's Cookiecutter-pytest-plugin template.

Features:
This plugin helps to reproduce random or flaky behavior when running tests with xdist. `pytest-xdist` executes tests
in a non-predictable order, making it hard to reproduce a behavior seen in CI locally because there's no convenient way
to track ...

Example:
```python
import pytest
import numpy as np
import random

@pytest.fixture
def rng(replay_metadata):
    seed = replay_metadata.metadata.setdefault("seed", random.randint(0, 100))
    return np.random.default_rng(seed=seed)

def test_random(rng):
    data = rng.standard_normal((100, 100))
...

</details>

### pytest-reporter-html1

A basic HTML report template for Pytest

`pip install pytest-reporter-html1` · installs (wheel) · licence: MIT · rank 11680 · last release 2025-10-10 · [PyPI](https://pypi.org/project/pytest-reporter-html1/) · [source](https://github.com/christiansandberg/pytest-reporter-html1.git)

<details><summary>README extract</summary>

A basic HTML report for pytest using Jinja2 template engine.
Based on pytest-reporter which provides the data to the template.

Features:
* Overview of files, tests, and phases with expandable sections
* Includes information about tests such as documentation, markers, and fixtures
* Fairly mobile friendly
* Complies with Jenkins default CSP policy (with `--split-report`)
* Support for ...

Sections: pytest-reporter-html1, Features, Usage, Customization, Issues

</details>

### pytest-depends

Tests that depend on other tests

`pip install pytest-depends` · installs (wheel) · licence: MIT License · rank 11706 · last release 2020-04-05 · [PyPI](https://pypi.org/project/pytest-depends/)

<details><summary>README extract</summary>

This pytest plugin allows you to declare dependencies between pytest tests, where dependent tests will not run if the
tests they depend on did not succeed.

Of course, tests should be self contained whenever possible, but that doesn't mean this doesn't have good uses. ...

Example:
```python
BUILD_PATH = 'build'

def test_build_exists():
    assert os.path.exists(BUILD_PATH)

@pytest.mark.depends(on=['test_build_exists'])
def test_build_version():
    result = subprocess.run([BUILD_PATH, '--version'], stdout=subprocess.PIPE)
    assert result.returncode == 0
    assert '1.2.3' in result.stdout
```

Sections: pytest-depends, Usage, Order, Naming

</details>

### pytest-threadleak

Detects thread leaks

`pip install pytest-threadleak` · installs (wheel) · licence: MIT License · rank 11953 · last release 2022-07-03 · [PyPI](https://pypi.org/project/pytest-threadleak/)

<details><summary>README extract</summary>

Example:
```python
$ cat leak_test.py
import threading
import time

def test_leak():
    threading.Thread(target=time.sleep, args=(1,)).start()
```

Sections: pytest-threadleak, Detects tests leaking threads, Usage

</details>

### pytest-stub

Stub packages, modules and attributes.

`pip install pytest-stub` · installs (wheel) · licence: BSD License · rank 11967 · last release 2020-04-28 · [PyPI](https://pypi.org/project/pytest-stub/)

<details><summary>README extract</summary>

*Stub packages, modules and attributes.*

This pytest plugin allows you to replace dependencies with stubs.

It can be useful if you want to test some code using a dependency without actually having this dependency,
for example if you're testing your library, which uses some parts of another library.

* Python 3.6+
* pytest >= 2.9.0

Example:
```python
def test_django_related(stub):

    stub.apply({
        # Replace `call_command` with a generated function.
        'django.core.management.call_command': '[func]',

        # Replace `BaseCommand` with a generated class.
        'django.core.management.base.BaseCommand': '[cls]',

        # Replace `dummy` with generated MagicMock.
...
```

Sections: pytest-stub, Description, Requirements, How to use

</details>

### pytest-black

A pytest plugin to enable format checking with black

`pip install pytest-black` · installs (wheel) · licence: MIT License · rank 12052 · last release 2024-12-15 · [PyPI](https://pypi.org/project/pytest-black/)

<details><summary>README extract</summary>

A pytest plugin to enable format checking with black.

Requirements

* pytest
* black

There is a minimum requirement of black 19.3b0 or later.

Installation

Usage

To run pytest with formatting checks provided by black:

The plugin will output a diff of suggested formatting changes (if any exist). Changes will _not_ be applied automatically. ...

</details>

### colour-runner

Colour formatting for unittest tests

`pip install colour-runner` · installs (wheel) · licence: MIT License · rank 12059 · last release 2018-10-05 · [PyPI](https://pypi.org/project/colour-runner/)

### flexmock

flexmock is a testing library for Python that makes it easy to create mocks, stubs and fakes.

`pip install flexmock` · installs (wheel) · licence: BSD License · rank 12115 · last release 2026-01-10 · [PyPI](https://pypi.org/project/flexmock/) · [docs](https://flexmock.readthedocs.io) · [source](https://github.com/flexmock/flexmock)

<details><summary>README extract</summary>

flexmock - Mock, stub, and spy library for Python.

Flexmock is a testing library for Python that makes it easy to create mocks, stubs, and fakes.

Features:
- Mock: Easily create mock objects and make assertions about which methods or attributes were used and arguments they were called with. ...

Example:
```python
from flexmock import flexmock
```

Sections: Features, Examples, Mocks, Spies, Documentation

</details>

### xunitparser

Read JUnit/XUnit XML files and map them to Python objects

`pip install xunitparser` · installs (wheel) · licence: MIT License · rank 12145 · last release 2022-02-23 · [PyPI](https://pypi.org/project/xunitparser/)

<details><summary>README extract</summary>

xunitparser reads a JUnit/XUnit XML file and maps it to Python objects.
It tries to use the objects available in the standard `unittest` module.

Example:
```python
import xunitparser
ts, tr = xunitparser.parse(open('/path/to/unit.xml'))
```

Sections: xunitparser, Description, Usage, Changes

</details>

### pytest-asyncio-concurrent

Pytest plugin to execute python async tests concurrently.

`pip install pytest-asyncio-concurrent` · installs (wheel) · licence: MIT License · rank 12150 · last release 2026-04-09 · [PyPI](https://pypi.org/project/pytest-asyncio-concurrent/) · [source](https://github.com/czl9707/pytest-asyncio-concurrent)

<details><summary>README extract</summary>

System/Integration tests can take a really long time.

And `pytest-asyncio-concurrent` A pytest plugin aiming to solve this by running asynchronous tests in true parallel, enabling faster execution for high I/O or network-bound test suites. ...

Features:
* Giving the capability to run pytest async functions.
* Providing granular control over Concurrency -- See Async Group for details

 * Specifying Async Group to control tests that can run together. ...

Example:
```python
@pytest.mark.asyncio_concurrent
async def async_test_A():
    res = await wait_for_something_async()
    assert result.is_valid()

@pytest.mark.asyncio_concurrent
async def async_test_B():
    res = await wait_for_something_async()
    assert result.is_valid()
```

...

</details>

### testinfra

Test infrastructures

`pip install testinfra` · installs (wheel) · licence: Apache Software License · rank 12185 · last release 2020-11-12 · [PyPI](https://pypi.org/project/testinfra/)

<details><summary>README extract</summary>

This package is just a transitional package for you should install pytest-testinfra instead.

</details>

### refurb

A tool for refurbishing and modernizing Python codebases

`pip install refurb` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12196 · last release 2026-04-03 · [PyPI](https://pypi.org/project/refurb/) · [source](https://github.com/dosisod/refurb)

_README extract left out: share-alike licence._

### pytest-click

Pytest plugin for Click

`pip install pytest-click` · installs (wheel) · licence: MIT License · rank 12205 · last release 2022-02-11 · [PyPI](https://pypi.org/project/pytest-click/)

<details><summary>README extract</summary>

pytest plugin for Click.

Example:
```python
import click

def test_cli(cli_runner):
    @click.command()
    @click.argument("name")
    def hello(name):
        click.echo("Hello %s!" % name)

    result = cli_runner.invoke(hello, ["Peter"])
    assert result.exit_code == 0
    assert result.output == "Hello Peter!\n"
```

Sections: pytest-click, Usage

</details>

### pytest-fastest

Use SCM and coverage to run only needed tests

`pip install pytest-fastest` · installs (wheel) · licence: MIT License · rank 12245 · last release 2023-10-04 · [PyPI](https://pypi.org/project/pytest-fastest/) · [docs](http://pytest-fastest.readthedocs.io/en/latest/) · [source](https://github.com/kstrauser/pytest-fastest)

<details><summary>README extract</summary>

Use SCM and coverage to run only needed tests

This pytest plugin was generated with Cookiecutter along with @hackebrot's cookiecutter-pytest-plugin template.

Features:
* Gathers coverage data from tests to track which tests call functions from which modules.
* Uses Git to track changes from a given commit to find the minimum set of tests that need to run to test new changes, then skips everything else.

Sections: pytest-fastest, Features, Requirements, Usage, Issues

</details>

### tag-expressions

Built-in functions, types, exceptions, and other objects.

`pip install tag-expressions` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 12286 · last release 2024-11-23 · [PyPI](https://pypi.org/project/tag-expressions/)

_README extract left out: share-alike licence._

### softest

Supports lightweight soft assertions by extending the unittest.TestCase class

`pip install softest` · installs (wheel) · licence: Freeware · rank 12411 · last release 2018-07-26 · [PyPI](https://pypi.org/project/softest/)

<details><summary>README extract</summary>

Supports the soft assert style of testing,
where multiple assertions can fail within the same method,
while collecting and formatting those failures' stack traces
for reporting by a final `assert_all` call.

Such stack traces are enhanced
to include the call hierarchy
from within the test class.

Example:
```python
import softest

class ExampleTest(softest.TestCase):

    def test_example(self):
        self.soft_assert(self.assertEqual, 'Worf', 'wharf', 'Klingon is not ship receptacle')
        self.soft_assert(self.assertTrue, True)
        self.soft_assert(self.assertTrue, False)

        self.assert_all()

...
```

Sections: softest - Soft Assertions, Usage, Error Console Output, ```

</details>

### unittest-parallel

Parallel unit test runner with coverage support

`pip install unittest-parallel` · installs (wheel) · licence: MIT · rank 12744 · last release 2026-08-22 · [PyPI](https://pypi.org/project/unittest-parallel/)

<details><summary>README extract</summary>

unittest-parallel is a parallel unit test runner for Python with coverage support.

Install unittest-parallel from PyPI:

~~~
pip install unittest-parallel
~~~

unittest-parallel discovers tests like `python -m unittest discover`. Specify the directory
containing your tests with `-s` and the project's top-level directory with `-t`: ...

Sections: unittest-parallel, Run Tests in Parallel, Test Coverage, Parallelism Level, Process and Thread Pools, Custom Runner and Result, Speedup Potential, I/O-Bound Tests, Real-World Speedups, Usage

</details>

### pytest-emoji

A pytest plugin that adds emojis to your test result report

`pip install pytest-emoji` · installs (wheel) · licence: MIT License · rank 12824 · last release 2019-02-19 · [PyPI](https://pypi.org/project/pytest-emoji/)

<details><summary>README extract</summary>

A pytest plugin that adds emojis to your test result report 😍

pytest is a mature testing framework for Python that is developed by a
thriving community of volunteers. It uses plain assert statements and regular
Python comparisons. ...

Features:
This plugin adds a ``--emoji`` CLI flag to pytest, which replaces the test
result indicator to emojis, both for *normal* and *verbose* mode.

- ``😃 / PASSED 😃`` for passed tests
- ``😰 / FAILED 😰`` for failed tests ...

Example:
```python
def pytest_emoji_passed(config):
    return "🍪 ", "PASSED 🍪 "

def pytest_emoji_failed(config):
    return "😿 ", "FAILED 😿 "

def pytest_emoji_skipped(config):
    return "🙈 ", "SKIPPED 🙈 "

def pytest_emoji_error(config):
    return "💩 ", "ERROR 💩 "

def pytest_emoji_xfailed(config):
    return "🤓 ", "XFAIL 🤓 "

...

</details>

### pytest-error-for-skips

Pytest plugin to treat skipped tests a test failure

`pip install pytest-error-for-skips` · installs (wheel) · licence: MIT License · rank 13069 · last release 2019-12-19 · [PyPI](https://pypi.org/project/pytest-error-for-skips/)

<details><summary>README extract</summary>

Pytest plugin to treat skipped tests a test failures.

This is nice if you want to ensure that your CI tests really run all
tests and don\'t skip tests because of missing dependencies.

Usage

Simply execute your tests via `pytest --error-for-skips ...` and all
skipped tests become test failures.

Requirements

- pytest

Installation ...

</details>

### cov-core

plugin core for use by pytest-cov, nose-cov and nose2-cov

`pip install cov-core` · installs from source (sdist only) · licence: MIT License · rank 13080 · last release 2014-11-22 · [PyPI](https://pypi.org/project/cov-core/)

<details><summary>README extract</summary>

This is a lib package for use by pytest-cov, nose-cov and nose2-cov. Unless you're developing a
coverage plugin for a test framework, you probably want one of those.

</details>

### pytest-localftpserver

A PyTest plugin which provides an FTP fixture for your tests

`pip install pytest-localftpserver` · installs (wheel) · licence: MIT License · rank 13086 · last release 2026-08-11 · [PyPI](https://pypi.org/project/pytest-localftpserver/)

<details><summary>README extract</summary>

A PyTest plugin which provides an FTP fixture for your tests

* Free software: MIT license

As of version `1.0.0` the support for python 2.7 and 3.4 was dropped.
If you need to support those versions you should pin the version to `0.6.0`,
i.e. add the following lines to your "requirements_dev.txt":

Sections: PyTest FTP Server, Attention!, Usage Quickstart

</details>

### pytest-aio

Pytest plugin for testing async python code

`pip install pytest-aio` · installs (wheel) · licence: MIT · rank 13131 · last release 2026-02-12 · [PyPI](https://pypi.org/project/pytest-aio/) · [source](https://github.com/klen/pytest-aio)

<details><summary>README extract</summary>

pytest-aio -- Is a simple pytest plugin for testing any async python code

Features:
- Supports all most popular async python libraries: Asyncio, Trio and Curio
- Automatically run your async tests
- Works with `contextvars` correctly (supports it for async/sync fixtures)
- Supports trio-asyncio

Example:
```python
async def test_async():
    assert True
```

Sections: pytest-aio, Features, Requirements, Usage, Async fixtures for sync tests, Customize async libraries, Helpers, Bug tracker

</details>

### shellsim

In-process BusyBox-like environment for RL rollouts and agent tests

`pip install shellsim` · installs (wheel) · licence: Apache-2.0 · rank 13149 · last release 2026-10-23 · [PyPI](https://pypi.org/project/shellsim/) · [source](https://github.com/rjpower/shellsim)

<details><summary>README extract</summary>

Shellsim is a BusyBox for containers: one small, deterministic process that provides a useful
Unix-shaped environment without starting a VM, container runtime, or host subprocess. ...

Sections: shellsim, Compatibility, Clock modes, Experimental Wasm executables, Agent harness, Resource model

</details>

### pytest-extra-durations

A pytest plugin to get durations on a per-function basis and per module basis.

`pip install pytest-extra-durations` · installs (wheel) · licence: MIT License · rank 13211 · last release 2020-04-21 · [PyPI](https://pypi.org/project/pytest-extra-durations/)

<details><summary>README extract</summary>

Get more info about the speed of your test suite.

It works with pytest-xdist too.

Sections: pytest-extra-durations, Usage, The sum of all tests/setup/teardown durations, The sum of all the tests durations of a module, The sum of all the tests durations of a test function, TODO

</details>

### labgrid

embedded systems control library for development, testing and installation

`pip install labgrid` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 13254 · last release 2026-10-14 · [PyPI](https://pypi.org/project/labgrid/)

_README extract left out: share-alike licence._

### pytest-regex

Select pytest tests with regular expressions

`pip install pytest-regex` · installs (wheel) · licence: MIT License · rank 13265 · last release 2023-05-29 · [PyPI](https://pypi.org/project/pytest-regex/)

<details><summary>README extract</summary>

pytest-regex

Use Python Standard Library Regular Expressions to Specify Tests to Run

After installing locally with i.e., `python -m pip install .` you can
compare it with more conventional test selection techniques as follows.

Consider working with SciPy development. ...

</details>

### pytest-monitor

Pytest plugin for analyzing resource usage.

`pip install pytest-monitor` · installs (wheel) · licence: MIT License · rank 13342 · last release 2023-06-25 · [PyPI](https://pypi.org/project/pytest-monitor/) · [source](https://github.com/CFMTech/pytest-monitor)

<details><summary>README extract</summary>

Pytest-monitor is a pytest plugin designed for analyzing resource usage.

Features:
* memory consumption
 * time duration
 * CPU usage
- Keep a history of your resource consumption measurements.
- Compare how your code behaves between different environments.

Sections: pytest-monitor, Features, Usage, Documentation, Requirements, Storage backends, Issues

</details>

### pytest-shm

Put pytest's temporary files on the /dev/shm tmpfs so fsync-heavy suites stop waiting on the disk

`pip install pytest-shm` · installs (wheel) · licence: MIT · rank 13463 · last release 2026-10-25 · [PyPI](https://pypi.org/project/pytest-shm/) · [docs](https://pytest-shm.nijho.lt) · [source](https://github.com/basnijholt/pytest-shm)

<details><summary>README extract</summary>

Faster tests for code that saves files, by keeping pytest's temporary files in memory instead of on disk.

Install it and run pytest as usual.
There is nothing to configure, and most test suites need no changes.

Example:
```python
# conftest.py at the repository root (tiktoken shown as an example)
import os
import tempfile
from pathlib import Path

if "TIKTOKEN_CACHE_DIR" not in os.environ and "DATA_GYM_CACHE_DIR" not in os.environ:
    os.environ["TIKTOKEN_CACHE_DIR"] = str(Path(tempfile.gettempdir()) / "data-gym-cache")
```

Sections: pytest-shm, The problem: waiting on the disk, The fix: a folder that lives in memory, Does it help?, How it works, When it stays off, Configuration, Caveats

</details>

### testmuai-appium-bindings

Testmu binding for Appium Python — thin mobile test runtime for LambdaTest exports

`pip install testmuai-appium-bindings` · installs (wheel) · licence: LicenseRef-Proprietary · rank 13512 · last release 2026-11-05 · [PyPI](https://pypi.org/project/testmuai-appium-bindings/)

<details><summary>README extract</summary>

Appium runtime bindings for KaneAI v4 mobile exports.

> Distribution name vs import name
> Install `testmuai-appium-bindings`; import `testmu_appium`.

Example:
```python
import testmu_appium
from testmu_appium import var, set_var

testmu_appium.configure(kane_run_v4=True, app_id="com.google.android.gm", platform="android")

@testmu_appium.test
def test(driver):
    with testmu_appium.step("Tap the Compose button"):
        testmu_appium.click(
            driver,
            selectors=[
...
```

...

</details>

### snappi-ixnetwork

The Snappi IxNetwork Open Traffic Generator Python Package

`pip install snappi-ixnetwork` · installs (wheel) · licence: MIT · rank 13617 · last release 2026-10-30 · [PyPI](https://pypi.org/project/snappi-ixnetwork/) · [source](https://github.com/open-traffic-generator/snappi-ixnetwork)

<details><summary>README extract</summary>

This extension allows executing test scripts written using snappi against
IxNetwork, (one of) Keysight's implementation of Open Traffic Generator.

> The repository is under active development.

To start contributing, please see contributing.md.

Example:
```python
"""
Configure a raw TCP flow with,
- tx port as source to rx port as destination
- frame count 10000, each of size 128 bytes
- transmit rate of 1000 packets per second
Validate,
- frames transmitted and received for configured flow is as expected
"""

import snappi
# host is IxNetwork API Server
api = snappi.api(location=' ext='ixnetwork')
...
```

Sections: snappi Extension for IxNetwork, Start scripting

</details>

### pytest-rich

Leverage rich for richer test session output

`pip install pytest-rich` · installs (wheel) · licence: MIT License · rank 13633 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pytest-rich/)

<details><summary>README extract</summary>

Leverage rich for richer test session output.

Sections: pytest-rich, Usage, IMPORTANT: Proof-of-concept

</details>

### datacurve-pier

A framework for running coding agents in sandboxed environments and keeping full trajectories for analysis.

`pip install datacurve-pier` · installs (wheel) · licence: Apache-2.0 · rank 13730 · last release 2026-08-11 · [PyPI](https://pypi.org/project/datacurve-pier/)

<details><summary>README extract</summary>

Pier is a Harbor-compatible framework for evaluating coding agents in sandboxed environments. It reads Harbor's task format and runs trials against it.

Features:
Pier is a fork. We wanted a smaller, more opinionated base to build on. On top of Harbor, Pier adds:

- Installed agents in air-gapped tasks (`allow_internet = false`). ...

Sections: pier, Why pier, What works today, Run, Agent runtime configuration

</details>

### tox-docker

Manage lifecycle of docker containers during Tox test runs

`pip install tox-docker` · installs (wheel) · licence: BSD License · rank 13780 · last release 2024-05-25 · [PyPI](https://pypi.org/project/tox-docker/)

<details><summary>README extract</summary>

A tox plugin which runs one or
more Docker containers during the test run.

Links: Source Code |
Documentation

Sections: tox-docker, Configuration, Command-Line Arguments, Container Naming & Parallel Runs, Example, Environment Variables, Version Compatibility, Upgrading, Code Style

</details>

### pytest-schema

👍 Validate return values against a schema-like object in testing

`pip install pytest-schema` · installs (wheel) · licence: MIT License · rank 13896 · last release 2024-02-16 · [PyPI](https://pypi.org/project/pytest-schema/)

<details><summary>README extract</summary>

👍 Validate return values against a schema-like object in testing

`keleshev/schema` is a library for validating Python data structures, such as
those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to Python data-types.

Example:
```python
from pytest_schema import schema, exact_schema, like_schema

article_v1 = {
    "id": int,
    "title": str,
    "completed": bool,
    "engagement": {
        "viewer": list,
        "rating": float,
    },
    "metadata": dict
}

def test_article_v1_endpoint(test_client):
    """
    Test calling v1 endpoint and validating the response
...
```

Sections: pytest-schema, Basic Example, Full Example

</details>

### pytest-datafiles

py.test plugin to create a 'tmp_path' containing predefined files/directories.

`pip install pytest-datafiles` · installs (wheel) · licence: MIT · rank 13937 · last release 2026-01-04 · [PyPI](https://pypi.org/project/pytest-datafiles/) · [source](https://github.com/omarkohl/pytest-datafiles)

<details><summary>README extract</summary>

pytest plugin to create a tmp_path containing a preconfigured set of files and/or directories.

Note about maintenance: This project is maintained and bug reports or pull requests will be addressed. There is little activity because it simply works and no changes are required.

Features:
This plugin allows you to specify one or several files/directories that are copied to a temporary directory (tmp_path) before the execution of the test. ...

Example:
```python
# more details in `examples/example_1.py`

@pytest.mark.datafiles('/opt/big_files/film1.mp4')
def test_fast_forward(datafiles):
    # ...
```

Sections: pytest-datafiles, Features, Options, Upgrade to 3.0, Usage, Example 1, Example 2, Example 3, Example 4, Example 5, Releasing, Issues

</details>

### pytest-embedded-idf

Make pytest-embedded plugin work with ESP-IDF.

`pip install pytest-embedded-idf` · installs (wheel) · licence: MIT License · rank 13947 · last release 2026-08-31 · [PyPI](https://pypi.org/project/pytest-embedded-idf/) · [docs](https://docs.espressif.com/projects/pytest-embedded/en/latest/) · [source](https://github.com/espressif/pytest-embedded)

<details><summary>README extract</summary>

pytest embedded service for esp-idf project

Extra Functionalities:

</details>

### pytest-embedded-serial-esp

Make pytest-embedded plugin work with Espressif target boards.

`pip install pytest-embedded-serial-esp` · installs (wheel) · licence: MIT License · rank 14050 · last release 2026-08-31 · [PyPI](https://pypi.org/project/pytest-embedded-serial-esp/) · [docs](https://docs.espressif.com/projects/pytest-embedded/en/latest/) · [source](https://github.com/espressif/pytest-embedded)

<details><summary>README extract</summary>

pytest embedded service for testing espressif boards via serial ports

Extra Functionalities:

- `serial`: detect and confirm target and port by `esptool` automatically.

</details>

### pytest-embedded-qemu

Make pytest-embedded plugin work with QEMU.

`pip install pytest-embedded-qemu` · installs (wheel) · licence: MIT License · rank 14131 · last release 2026-08-31 · [PyPI](https://pypi.org/project/pytest-embedded-qemu/) · [docs](https://docs.espressif.com/projects/pytest-embedded/en/latest/) · [source](https://github.com/espressif/pytest-embedded)

<details><summary>README extract</summary>

pytest embedded service for running tests on QEMU instead of the real target.

Extra Functionalities:

</details>

### pyucis

PyUCIS provides a Python API for manipulating UCIS coverage data.

`pip install pyucis` · installs (wheel) · licence: Apache Software License · rank 14177 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pyucis/) · [source](https://github.com/fvutils/pyucis)

<details><summary>README extract</summary>

Python API to Unified Coverage Interoperability Standard (UCIS) Data Model

Features:
- Python API for manipulating UCIS coverage databases
- CLI Tools for database conversion, merging, and reporting
- Coverage Import - Import from Verilator, cocotb-coverage, and AVL frameworks ...

Example:
```python
from ucis import UCIS

# Open a database
db = UCIS("coverage.xml")

# Access coverage data
for scope in db.scopes():
    print(f"Scope: {scope.name}")
    for coveritem in scope.coveritems():
        print(f"  {coveritem.name}: {coveritem.count} hits")
```

...

</details>

### robotframework-archivelibrary

Robot Framework keyword library for handling ZIP files

`pip install robotframework-archivelibrary` · installs (wheel) · licence: Public Domain · rank 14211 · last release 2024-10-26 · [PyPI](https://pypi.org/project/robotframework-archivelibrary/)

<details><summary>README extract</summary>

Robot Framework keyword library for handling ZIP files.

</details>

### pytest-logger

Plugin configuring handlers for loggers from Python logging module.

`pip install pytest-logger` · installs (wheel) · licence: MIT License · rank 14217 · last release 2024-03-10 · [PyPI](https://pypi.org/project/pytest-logger/)

<details><summary>README extract</summary>

Pytest-logger is a pytest plugin configuring handlers for loggers from Python logging module.

You can install pytest-logger via `pip` from `PyPI`:
Plugin puts logs on per-logger basis to:

- standard output,
- files within log-specific directory under pytest's `tmpdir_factory` session directory. ...

Example:
```python
# conftest.py
import os

def pytest_logger_config(logger_config):
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='info')
    logger_config.set_log_option_default('foo,bar')

def pytest_logger_logdirlink(config):
    return os.path.join(os.path.dirname(file), 'mylogs')
```

</details>

### ipytest

Unit tests in IPython notebooks

`pip install ipytest` · installs (wheel) · licence: MIT License · rank 14227 · last release 2024-04-21 · [PyPI](https://pypi.org/project/ipytest/)

<details><summary>README extract</summary>

PyPI
| Usage
| Global state
| How does it work?
| Changes
| Reference
| Development
| Related packages
| License

`ipytest` allows you to run Pytest in Jupyter notebooks.
`ipytest` aims to give access to the full `pytest` experience and to make it
easy to transfer tests out of notebooks into separate test files.

Example:
```python
import ipytest
ipytest.autoconfig()
```

Sections: ipytest - Pytest in Jupyter notebooks, Usage, Global state, How does it work?, Reference, `%%ipytest ...`, `ipytest.exit_code`, `ipytest.clean(pattern=<default>, *, module=None)`, `ipytest.Error(exit_code)`, `ipytest.cov`, `ipytest.cov.translate_cell_filenames(enabled=True)`, Related packages

</details>

### pytest-pycodestyle

pytest plugin to run pycodestyle

`pip install pytest-pycodestyle` · installs from source (sdist only) · licence: MIT · rank 14247 · last release 2025-07-20 · [PyPI](https://pypi.org/project/pytest-pycodestyle/)

<details><summary>README extract</summary>

pytest plugin to run pycodestyle

Sections: pytest-pycodestyle, Usage, Configuration

</details>

### pytest-cython

A plugin for testing Cython extension modules.

`pip install pytest-cython` · installs (wheel) · licence: not stated · rank 14392 · last release 2026-03-11 · [PyPI](https://pypi.org/project/pytest-cython/) · [docs](https://github.com/lgpage/pytest-cython/tree/main#readme) · [source](https://github.com/lgpage/pytest-cython)

<details><summary>README extract</summary>

Features:
This pytest plugin allows for the doctesting of C/C++ extension modules for
Python created through cython.

Sections: Overview, Usage, Notes, Compatibility, Issues

</details>

### pytest-slow-first

Prioritize running the slowest tests first.

`pip install pytest-slow-first` · installs (wheel) · licence: MIT License · rank 14401 · last release 2024-01-30 · [PyPI](https://pypi.org/project/pytest-slow-first/)

<details><summary>README extract</summary>

Features:
`pytest-slow-first` is a pytest plugin that optimizes test suite execution by sorting tests based on their duration from the last run. ...

Sections: pytest-slow-first, Overview, How It Works, Example, Usage, Multiple runs, Custom File Location

</details>

### pytest-cookies

The pytest plugin for your Cookiecutter templates. 🍪

`pip install pytest-cookies` · installs (wheel) · licence: MIT License · rank 14616 · last release 2023-03-22 · [PyPI](https://pypi.org/project/pytest-cookies/) · [source](https://github.com/hackebrot/pytest-cookies)

<details><summary>README extract</summary>

pytest is a mature testing framework for Python that is developed
by a thriving and ever-growing community of volunteers. It uses plain assert
statements and regular Python comparisons. At the core of the pytest test
framework is a powerful hook-based plugin system. ...

Example:
```python
def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repo_name": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
...
```

Sections: pytest-cookies, Usage, Generate a new project, Specify the template directory, Keep output directories for debugging

</details>

### pytest-isort

py.test plugin to check import ordering using isort

`pip install pytest-isort` · installs (wheel) · licence: MIT License · rank 14872 · last release 2024-03-05 · [PyPI](https://pypi.org/project/pytest-isort/) · [source](https://github.com/stephrdev/pytest-isort)

<details><summary>README extract</summary>

Example:
```python
# content of file1.py

import os
import sys
import random

# content of file2.py

import json
import sys
import os
```

Sections: py.test plugin to check import ordering using isort, Usage, Example, Configuration, Notes

</details>

### pytest-kubernetes

A lightweight pytest plugin for managing local Kubernetes clusters (minikube, k3d, kind)

`pip install pytest-kubernetes` · installs (wheel) · licence: not stated · rank 14902 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pytest-kubernetes/) · [source](https://github.com/Blueshoe/pytest-kubernetes)

<details><summary>README extract</summary>

> Stop mocking Kubernetes. Mocks don't have crash loops, OOM kills, DNS gremlins, or angry admission webhooks. Test against the real thing.

`pytest-kubernetes` is a lightweight pytest plugin that makes orchestrating local Kubernetes clusters in your tests an absolute breeze. ...

Example:
```python
from pathlib import Path
from pytest_kubernetes.providers import AClusterManager

def test_my_kubernetes_app(k8s: AClusterManager):
    # 1. Spin up the cluster (auto-detected provider: k3d, kind, or minikube)
    k8s.create()

    # 2. Apply a manifest from a Python dictionary (no disk I/O required!)
    k8s.apply(
        {
...
```

...

</details>

### pytest-github-report

Generate a GitHub report using pytest in GitHub Workflows

`pip install pytest-github-report` · installs from source (sdist only) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14937 · last release 2022-06-03 · [PyPI](https://pypi.org/project/pytest-github-report/)

<details><summary>README extract</summary>

This is an example of how we can use GitHub reports with pytest to
generate a nice markdown matrix of results. The tests here are from the pytest-md-report
repository.

Sections: Pytest GitHub Report, Usage, Local, GitHub Actions, Configuration, Enable, Title, Zeros, Blanks, Detail, Emojis, Thanks!

</details>

## Also in this topic

- [pluggy](software-development-libraries.md#pluggy) - plugin and hook calling mechanisms for python
- [pytest](software-development-libraries.md#pytest) - pytest: simple powerful testing with Python
- [coverage](software-development-quality-assurance.md#coverage) - Code coverage measurement for Python
- [virtualenv](software-development-libraries.md#virtualenv) - Virtual Python Environment builder
- [pytest-xdist](software-development-quality-assurance.md#pytest-xdist) - pytest xdist plugin for distributed testing, most importantly across multiple CPUs
- [uv](software-development-libraries.md#uv) - An extremely fast Python package and project manager, written in Rust.
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [playwright](internet-www-http.md#playwright) - A high-level API to automate web browsers
- [Faker](software-development-libraries.md#faker) - Faker is a Python package that generates fake data for you.
- [hypothesis](education-testing.md#hypothesis) - The property-based testing library for Python
- [ty](software-development-libraries.md#ty) - An extremely fast Python type checker, written in Rust.
- [py](software-development-libraries.md#py) - library with cross-python path, ini-parsing, io, code, log facilities
- [astroid](software-development-libraries.md#astroid) - An abstract syntax tree for Python with inference support.
- [pytest-rerunfailures](software-development-quality-assurance.md#pytest-rerunfailures) - pytest plugin to re-run tests to eliminate flaky failures
- [pylint](software-development-debuggers.md#pylint) - python code static checker
- [selenium](software-development-libraries.md#selenium) - Official Python bindings for Selenium WebDriver
- [yamllint](software-development.md#yamllint) - A linter for YAML files.
- [diff_cover](software-development-quality-assurance.md#diff_cover) - Run coverage and linting reports on diffs
- [pytest-metadata](software-development-quality-assurance.md#pytest-metadata) - pytest plugin for test session metadata
- [factory-boy](software-development-libraries.md#factory-boy) - A versatile test fixtures replacement based on thoughtbot's factory_bot for Ruby.
- [pytest-env](software-development-libraries.md#pytest-env) - Set environment variables for pytest sessions.
- [mock](software-development-libraries.md#mock) - Rolling backport of unittest.mock for all Pythons
- [vcrpy](internet-www-http.md#vcrpy) - Automatically mock your HTTP interactions to simplify and speed up testing
- [great-expectations](scientific-engineering.md#great-expectations) - Always know what to expect from your data.
- [uv-build](software-development-libraries.md#uv-build) - The uv build backend
- [tox](software-development-libraries.md#tox) - tox is a generic virtualenv management and test command line tool
- [pytest-html](software-development-quality-assurance.md#pytest-html) - pytest plugin for generating HTML reports
- [pytest-repeat](software-development-quality-assurance.md#pytest-repeat) - pytest plugin for repeating tests
- [pip-tools](software-development-quality-assurance.md#pip-tools) - pip-tools keeps your pinned dependencies fresh.
- [polyfactory](software-development.md#polyfactory) - Mock data generation factories
- [syrupy](software-development-libraries.md#syrupy) - Pytest Snapshot Test Utility
- [junit-xml](software-development-build-tools.md#junit-xml) - Creates JUnit XML test result documents that can be read by tools such as Jenkins
- [pytest-base-url](software-development-quality-assurance.md#pytest-base-url) - pytest plugin for URL based testing
- [browser-harness](internet-www-http.md#browser-harness) - The simplest, thinnest, and most powerful harness to control your real browser with your agent.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [pyinstrument](software-development-debuggers.md#pyinstrument) - Call stack profiler for Python. Shows you why your code is slow!
- [pytest-sugar](software-development-libraries.md#pytest-sugar) - pytest-sugar is a plugin for pytest that changes the default look and feel of pytest (e.g. progressbar, show tests that fail instantly).
- [poethepoet](software-development-build-tools.md#poethepoet) - A task runner that works well with poetry and uv.
- [pytest-testmon](software-development-libraries.md#pytest-testmon) - selects tests affected by changed files and methods
- [allure-python-commons](software-development-quality-assurance.md#allure-python-commons) - Contains the API for end users as well as helper functions and classes to build Allure adapters for Python test frameworks
- [allure-pytest](software-development-quality-assurance.md#allure-pytest) - Allure pytest integration
- [aioresponses](internet-www-http.md#aioresponses) - Mock out requests made by ClientSession from aiohttp package
- [unittest-xml-reporting](software-development-libraries.md#unittest-xml-reporting) - unittest-based test runner with Ant/JUnit like XML reporting.
- [ansible-compat](software-development-bug-tracking.md#ansible-compat) - Ansible compatibility goodies
- [pytest-order](software-development-quality-assurance.md#pytest-order) - pytest plugin to run tests in a specific order
- [pytest-forked](software-development-quality-assurance.md#pytest-forked) - run tests in isolated forked subprocesses
- [mitmproxy](internet-proxy-servers.md#mitmproxy) - An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.
- [patchright](internet-www-http.md#patchright) - Undetected Python version of the Playwright testing and automation library.
- [ansible-lint](software-development-quality-assurance.md#ansible-lint) - Checks playbooks for practices and behavior that could potentially be improved
- [pytest-postgresql](software-development-libraries.md#pytest-postgresql) - Postgresql fixtures and fixture factories for Pytest.
- [pytest-github-actions-annotate-failures](software-development-quality-assurance.md#pytest-github-actions-annotate-failures) - pytest plugin to annotate failed tests with a workflow command for GitHub Actions
- [pytest-bdd](software-development-libraries.md#pytest-bdd) - BDD for pytest
- [pytest-unordered](software-development-libraries.md#pytest-unordered) - Test equality of unordered collections in pytest
- [pytest-factoryboy](software-development-libraries.md#pytest-factoryboy) - Factory Boy support for pytest.
- [gcovr](software-development.md#gcovr) - Generate C/C++ code coverage reports with gcov
- [pyfakefs](software-development-libraries.md#pyfakefs) - Implements a fake file system that mocks the Python file system modules.
- [pytest-instafail](software-development-libraries.md#pytest-instafail) - pytest plugin to show failures instantly
- [kgb](software-development.md#kgb) - Utilities for spying on function calls in unit tests.
- [PyHamcrest](software-development.md#pyhamcrest) - Hamcrest framework for matcher objects
- [hypothesis-jsonschema](education-testing.md#hypothesis-jsonschema) - Generate test data from JSON schemata with Hypothesis
- [cucumber-tag-expressions](software-development-libraries.md#cucumber-tag-expressions) - Provides a tag-expression parser and evaluation logic for cucumber/behave
- [mimesis](software-development.md#mimesis) - Mimesis: Fake Data Generator.
- [chispa](software-development-libraries.md#chispa) - Pyspark test helper library
- [cucumber-expressions](software-development-libraries-2.md#cucumber-expressions) - Cucumber Expressions - a simpler alternative to Regular Expressions
- [pytest-datadir](software-development-quality-assurance.md#pytest-datadir) - pytest plugin for test data directories and files
- [stagehand](internet-www-http.md#stagehand) - Browserbase's SDK for building browser agents
- [pytest-profiling](software-development-libraries-2.md#pytest-profiling) - Profiling plugin for py.test
- [pytest-ordering](software-development-quality-assurance.md#pytest-ordering) - pytest plugin to run your tests in a specific order
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [circular-dict](software-development-debuggers.md#circular-dict) - CircularDict is a high-performance Python data structure that blends the functionality of dictionaries and circular buffers. Inheriting the usage of traditional dictionaries, it allows you to define constraints on size and memory usage. This way, the CircularDict will be always up-to-date with the last N added elements, ensuring that neither the maximum length nor the memory usage limit is exceeded. It is ideal for caching large data structures while maintaining control over memory footprint.
- [molecule](software-development-bug-tracking.md#molecule) - Molecule aids in the development and testing of Ansible roles
- [ansi2html](software-development-quality-assurance.md#ansi2html) - Convert text with ANSI color codes to HTML or to LaTeX
- [complexipy](software-development-libraries-2.md#complexipy) - An extremely fast Python library to calculate the cognitive complexity of Python files, written in Rust.
- [rpyc](internet.md#rpyc) - Remote Python Call (RPyC) is a transparent and symmetric distributed computing library
- [pytest-flask](software-development-libraries-2.md#pytest-flask) - A set of py.test fixtures to test Flask applications.
- [salt-lint](software-development-bug-tracking.md#salt-lint) - A command-line utility that checks for best practices in SaltStack.
- [langchain-tests](software-development-libraries-2.md#langchain-tests) - Standard tests for LangChain implementations
- [jsoncomparison](software-development-libraries-2.md#jsoncomparison) - json compare utility
- [pyngrok](internet-proxy-servers.md#pyngrok) - The complete ngrok agent for Python: programmatic tunnels for ingress, inspection, webhooks, demos, and APIs
- [skillsaw](software-development-quality-assurance.md#skillsaw) - A configurable linter for agent skills, plugins, and AI coding assistant context
- [testing.common.database](database.md#testingcommondatabase) - utilities for testing.* packages
- [pytest-qt](desktop-environment-window-managers.md#pytest-qt) - pytest support for PyQt and PySide applications
- [datacontract-cli](database.md#datacontract-cli) - The datacontract CLI is an open source command-line tool for working with Data Contracts. It uses data contract YAML files to lint the data contract, connect to data sources and execute schema and quality tests, detect breaking changes, and export to different formats. The tool is written in Python. It can be used as a standalone CLI tool, in a CI/CD pipeline, or directly as a Python library.
- [testtools](software-development-libraries-2.md#testtools) - Extensions to the Python standard library unit testing framework
- [geckodriver-autoinstaller](software-development-libraries-2.md#geckodriver-autoinstaller) - Automatically install geckodriver that supports the currently installed version of chrome.
- [trustme](security-cryptography.md#trustme) - #1 quality TLS certs while you wait, for the discerning tester
- [testing.postgresql](database.md#testingpostgresql) - automatically setups a postgresql instance in a temporary directory, and destroys it after testing
- [xdoctest](software-development-libraries-2.md#xdoctest) - A rewrite of the builtin doctest module
- [molecule-plugins](software-development-bug-tracking.md#molecule-plugins) - Molecule Plugins
- [assertpy](software-development.md#assertpy) - Fluent, fully typed assertion library for Python: your type checker sees only the assertions that fit the value, and every failure carries a structured diff. Soft assertions, polling, inline snapshots, OpenAPI contracts.
- [pytest-cases](software-development-libraries-2.md#pytest-cases) - Separate test code from test cases in pytest.
- [rollbar](internet-www-http.md#rollbar) - Easy and powerful exception tracking with Rollbar. Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.
- [lintrunner-adapters](software-development-quality-assurance.md#lintrunner-adapters) - Adapters and tools for lintrunner
- [pywinauto](software-development-libraries-2.md#pywinauto) - A set of Python modules to automate the Microsoft Windows GUI
- [django-coverage-plugin](software-development-quality-assurance.md#django-coverage-plugin) - Django template coverage.py plugin
- [adbutils](software-development-libraries-2.md#adbutils) - Pure Python Adb Library
- [fickling](security.md#fickling) - A static analyzer and interpreter for Python pickle data
- [gitlint-core](software-development-quality-assurance.md#gitlint-core) - Git commit message linter written in python, checks your commit messages for style.
- [polyfile-weave](security.md#polyfile-weave) - A utility to recursively map the structure of a file.
- [browsermob-proxy](software-development-libraries-2.md#browsermob-proxy) - A library for interacting with the Browsermob Proxy
- [cosmic-ray](software-development-libraries-2.md#cosmic-ray) - Mutation testing
- [unittest2](software-development-libraries-2.md#unittest2) - The new features in unittest backported to Python 2.4+.
- [pyocd](software-development.md#pyocd) - Cortex-M debugger for Python
- [httpretty](internet-www-http.md#httpretty) - HTTP client mock for Python
- [pdbp](scientific-engineering.md#pdbp) - pdbp (Pdb+): A drop-in replacement for pdb and pdbpp.
- [axe-playwright-python](adaptive-technologies.md#axe-playwright-python) - Automated web accessibility testing using axe-core engine and Playwright.
- [bindep](software-development-quality-assurance.md#bindep) - Binary dependency utility
- [pytest-variables](software-development-quality-assurance.md#pytest-variables) - pytest plugin for providing variables to tests/fixtures
- [tabcompleter](scientific-engineering.md#tabcompleter) - tabcompleter --- Autocompletion in the Python console.
- [robotframework-robocop](software-development-quality-assurance.md#robotframework-robocop) - Static code analysis tool (linter) and code formatter for Robot Framework
- [crosshair-tool](software-development-quality-assurance.md#crosshair-tool) - Analyze Python code for correctness using symbolic execution.
- [pytest-describe](software-development-libraries-2.md#pytest-describe) - Describe-style plugin for pytest
- [pytest-cache](software-development-libraries-2.md#pytest-cache) - pytest plugin with mechanisms for caching across test runs
- [doit](scientific-engineering.md#doit) - doit - Automation Tool
- [great-expectations-experimental](scientific-engineering.md#great-expectations-experimental) - Always know what to expect from your data.
- [pylint-actions](software-development-libraries-2.md#pylint-actions) - Pylint plugin for GitHub Actions
- [lcov-cobertura](software-development-quality-assurance.md#lcov-cobertura) - LCOV to Cobertura XML converter
- [sbvirtualdisplay](internet.md#sbvirtualdisplay) - A customized pyvirtualdisplay for SeleniumBase.
- [gitlint](software-development-quality-assurance.md#gitlint) - Git commit message linter written in python, checks your commit messages for style.
- [nose2](software-development-libraries-2.md#nose2) - unittest with plugins
- [pytest-selenium](software-development-quality-assurance.md#pytest-selenium) - pytest plugin for Selenium
- [cloakbrowser](internet-www-http.md#cloakbrowser) - Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches.
- [mock-open](software-development.md#mock-open) - A better mock for file I/O
- [pytest-harvest](software-development-libraries-2.md#pytest-harvest) - Store data created during your pytest tests execution, and retrieve it at the end of the session, e.g. for applicative benchmarking purposes.
- [pytest-ansible](software-development-quality-assurance.md#pytest-ansible) - Plugin for pytest to simplify calling ansible modules from tests or fixtures
- [selenium-stealth](internet.md#selenium-stealth) - Trying to make python selenium more stealthy.
- [allure-behave](software-development-quality-assurance.md#allure-behave) - Allure behave integration
- [fixtures](software-development-quality-assurance.md#fixtures) - Fixtures, reusable state for writing clean tests and more.
- [coola](scientific-engineering.md#coola) - Library to check equality between two complex/nested objects
- [pytest-parallel](software-development-quality-assurance.md#pytest-parallel) - a pytest plugin for parallel and concurrent testing
- [install-playwright](software-development-libraries-2.md#install-playwright) - Execute `playwright install` from Python
- [pytest-md-report](software-development-quality-assurance.md#pytest-md-report) - A pytest plugin to generate test outcomes reports with markdown table format.
- [cisco-ai-skill-scanner](security.md#cisco-ai-skill-scanner) - Security scanner for Agent Skills packages - Detects prompt injection, data exfiltration, and malicious code
- [localstack](internet.md#localstack) - The LocalStack Command Line Interface
- [pylint-pytest](software-development-quality-assurance.md#pylint-pytest) - A Pylint plugin to suppress pytest-related false positives.
- [wiremock](internet-www-http.md#wiremock) - Wiremock Admin API Client
- [pytest-pytestrail](software-development-quality-assurance.md#pytest-pytestrail) - Pytest plugin for interaction with TestRail
- [async-factory-boy](software-development-libraries-2.md#async-factory-boy) - factory_boy extension with asynchronous ORM support
- [allpairspy](software-development-libraries-2.md#allpairspy) - Pairwise test combinations generator
- [testresources](software-development-quality-assurance.md#testresources) - Testresources, a pyunit extension for managing expensive test resources
- [tox-gh-actions](software-development-libraries-2.md#tox-gh-actions) - Seamless integration of tox into GitHub Actions
- [tox-ansible](software-development-quality-assurance.md#tox-ansible) - A radical approach to testing ansible content
- [vncdotool](multimedia-graphics.md#vncdotool) - Command line VNC client
- [pytest-spark](software-development-libraries-3.md#pytest-spark) - pytest plugin to run the tests with support of pyspark.
- [testscenarios](software-development-quality-assurance.md#testscenarios) - Testscenarios, a unittest extension for dependency injection
- [pgsanity](database.md#pgsanity) - Check syntax of sql for PostgreSQL
- [pytest-spec](software-development-libraries-3.md#pytest-spec) - Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.
- [pytest-loop](software-development-quality-assurance.md#pytest-loop) - pytest plugin for looping tests
- [concurrencytest](software-development-libraries-3.md#concurrencytest) - Run unittest test suites concurrently
- [pytest-mpl](scientific-engineering-visualization.md#pytest-mpl) - pytest plugin to help with testing figures output from Matplotlib
- [sql-compare](database.md#sql-compare) - Compare SQL schemas
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [verlib2](software-development-build-tools.md#verlib2) - A standalone bundle of "distutils.version" and "packaging.version", without anything else.
- [bzt](software-development-quality-assurance.md#bzt) - Taurus Tool for Continuous Testing
- [eyes-selenium](software-development-quality-assurance.md#eyes-selenium) - Applitools Python SDK. Selenium package
- [chromedriver-autoinstaller](software-development-libraries-3.md#chromedriver-autoinstaller) - Automatically install chromedriver that supports the currently installed version of chrome.
- [ansible-navigator](software-development-quality-assurance.md#ansible-navigator) - A text-based user interface (TUI) for the Red Hat Ansible Automation Platform
- [eyes-common](software-development-quality-assurance.md#eyes-common) - Applitools Python SDK. Common code package
- [pytest-xprocess](software-development-libraries-3.md#pytest-xprocess) - A pytest plugin for managing processes across test runs.
- [xmlrunner](software-development-libraries-3.md#xmlrunner) - PyUnit-based test runner with JUnit like XML reporting.
- [pytest-flake8](software-development.md#pytest-flake8) - pytest plugin to check FLAKE8 requirements
- [otel-extensions](software-development-libraries-3.md#otel-extensions) - Python extensions for OpenTelemetry
- [core-universal](software-development-quality-assurance.md#core-universal) - Applitools Eyes Core SDK Server
- [ansible-sign](software-development-quality-assurance.md#ansible-sign) - Ansible content validation library and CLI
- [pytest-redis](software-development-libraries-3.md#pytest-redis) - Redis fixtures and fixture factories for Pytest.
- [pyvalid](software-development-debuggers.md#pyvalid) - The module, which allows easily validate function's input/output values.
- [mocket](software-development.md#mocket) - Socket Mock Framework - for all kinds of socket animals, web-clients included - with gevent/asyncio/SSL support
- [unicon](software-development-build-tools.md#unicon) - Unicon Connection Library
- [looptime](software-development-libraries-3.md#looptime) - Fast-forward asyncio event loop time (in tests)
- [pytest-gremlins](software-development-quality-assurance.md#pytest-gremlins) - Fast-first mutation testing for pytest. Let the gremlins loose, see which ones survive.
- [localstack-ext](internet.md#localstack-ext) - Extensions for LocalStack
- [unicon.plugins](software-development-build-tools.md#uniconplugins) - Unicon Connection Library Plugins
- [mixer](software-development-libraries-3.md#mixer) - Mixer -- Is a fixtures replacement. Supported Django ORM, SqlAlchemy ORM, Mongoengine ODM and custom python objects.
- [pyats](software-development-build-tools.md#pyats) - pyATS - Python Automation Test System
- [django-webtest](software-development-libraries-3.md#django-webtest) - Instant integration of Ian Bicking's WebTest (http://docs.pylonsproject.org/projects/webtest/) with Django's testing framework.
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [pyats.datastructures](software-development-build-tools.md#pyatsdatastructures) - pyATS Datastructures: Extended Datastructures for Grownups
- [pyats.easypy](software-development-build-tools.md#pyatseasypy) - pyATS Easypy: launcher and runtime environment
- [pyats.topology](software-development-build-tools.md#pyatstopology) - pyATS Topology: Topology Objects and Testbed YAMLs
- [pyats.aetest](software-development-build-tools.md#pyatsaetest) - pyATS AEtest: Testscript Engine
- [pyats.utils](software-development-build-tools.md#pyatsutils) - pyATS Utils: Utilities Module
- [pyats.reporter](software-development-build-tools.md#pyatsreporter) - pyATS Reporter: Result Collection and Reporting
- [pyats.connections](software-development-build-tools.md#pyatsconnections) - pyATS Connection: Device Connection Handling & Base Classes
- [pyats.aereport](software-development-build-tools.md#pyatsaereport) - pyATS AEreport: Result Collection and Reporting
- [pyats.tcl](software-development-build-tools.md#pyatstcl) - pyATS Tcl: Tcl Integration and Objects
- [pyats.log](software-development-build-tools.md#pyatslog) - pyATS Log: Logging Format and Utilities
- [pyats.kleenex](software-development-build-tools.md#pyatskleenex) - pyATS Kleenex: Testbed Preparation, Clean & Finalization
- [pytest-cpp](software-development-quality-assurance.md#pytest-cpp) - Use pytest's runner to discover and execute C++ tests
- [robotframework-appiumlibrary](software-development-quality-assurance.md#robotframework-appiumlibrary) - Robot Framework Mobile app testing library for Appium Client Android & iOS & Web
- [pyats.results](software-development-build-tools.md#pyatsresults) - pyATS Results: Representing Results using Objects
- [pyats.async](software-development-build-tools.md#pyatsasync) - pyATS Async: Asynchronous Execution of Codes
- [flawfinder](security.md#flawfinder) - a program that examines source code looking for security weaknesses
- [localstack-core](internet.md#localstack-core) - The core library and runtime of LocalStack
- [pylint-odoo](software-development-debuggers.md#pylint-odoo) - Pylint plugin for Odoo
- [behave-django](internet-www-http.md#behave-django) - Behave BDD integration for Django
- [genie](software-development-build-tools.md#genie) - Genie: THE standard pyATS Library System
- [robotframework-tidy](software-development-quality-assurance.md#robotframework-tidy) - Code autoformatter for Robot Framework
- [pymongo_inmemory](database-database-engines-servers.md#pymongo_inmemory) - A mongo mocking library with an ephemeral MongoDB running in memory.
- [qase-python-commons](software-development-quality-assurance.md#qase-python-commons) - A library for Qase TestOps and Qase Report
- [prophy](scientific-engineering-interface-engine-protocol-translator.md#prophy) - prophy: fast serialization protocol
- [pytest-mysql](software-development-libraries-3.md#pytest-mysql) - MySQL process and client fixtures for pytest
- [robotframework-faker](software-development-quality-assurance.md#robotframework-faker) - Robot Framework wrapper for faker, a fake test data generator
- [genie.libs.parser](software-development-build-tools.md#genielibsparser) - Genie libs Parser: Genie Parser Libraries
- [uv-secure](software-development-libraries-3.md#uv-secure) - Deprecated dependency scanner for uv projects; use uv audit instead
- [genie.libs.sdk](software-development-build-tools.md#genielibssdk) - Genie libs sdk: Libraries containing all Triggers and Verifications
- [pytest-print](software-development-libraries-3.md#pytest-print) - pytest-print adds the printer fixture you can use to print messages to the user (directly to the pytest runner, not stdout)
- [genie.libs.ops](software-development-build-tools.md#genielibsops) - Genie libs Ops: Libraries to retrieve operational state of the topology
- [genie.libs.clean](software-development-build-tools.md#genielibsclean) - Genie Library for device clean support
- [genie.libs.conf](software-development-build-tools.md#genielibsconf) - Genie libs Conf: Libraries to configures topology through Python object attributes
- [approvaltests](software-development-libraries-3.md#approvaltests) - Assertion/verification library to aid testing
- [genie.libs.filetransferutils](software-development-build-tools.md#genielibsfiletransferutils) - Genie libs FileTransferUtils: Genie FileTransferUtils Libraries
- [genie.libs.health](software-development-build-tools.md#genielibshealth) - pyATS Health Check for monitoring device health status
- [rest.connector](software-development-build-tools.md#restconnector) - pyATS REST connection package
- [pytest-tornado](software-development.md#pytest-tornado) - A py.test plugin providing fixtures and markers to simplify testing of asynchronous tornado applications.
- [pytest-faker](software-development-libraries-3.md#pytest-faker) - Faker integration with the pytest framework.
- [qase-pytest](software-development-quality-assurance.md#qase-pytest) - Qase Pytest Plugin for Qase TestOps and Qase Report
- [spider-browser](internet-www-http.md#spider-browser) - Browser automation client for Spider's pre-warmed browser fleet with smart retry and browser switching
- [enola-cli](software-development-quality-assurance.md#enola-cli) - Architectural regression testing for AI-assisted development
- [pytest-shutil](software-development-libraries-3.md#pytest-shutil) - A goodie-bag of unix shell and environment tools for py.test
- [aiomoto](software-development-libraries-3.md#aiomoto) - Moto-style AWS service mocks for aiobotocore
- [zope.testing](software-development-libraries-3.md#zopetesting) - Zope testing helpers
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [stestr](software-development-quality-assurance.md#stestr) - A parallel Python test runner built around subunit
- [capt-hook](software-development-quality-assurance.md#capt-hook) - Stop repeating yourself to Claude.
- [py-pglite](database.md#py-pglite) - Python testing library for PGlite - in-memory PostgreSQL for tests
- [pytest-grpc](software-development-quality-assurance.md#pytest-grpc) - pytest plugin for grpc
- [flake8-pytest-style](software-development-quality-assurance.md#flake8-pytest-style) - A flake8 plugin checking common style issues or inconsistencies with pytest-based tests.
- [ruff-lsp](software-development-libraries-3.md#ruff-lsp) - A Language Server Protocol implementation for Ruff.
- [napari-plugin-engine](scientific-engineering.md#napari-plugin-engine) - napari plugin engine, fork of pluggy
- [kolo](software-development.md#kolo) - Kolo is a text-based Python debugger for AI agents. Capture every executed function call, return value, local variable, HTTP request, and more in greppable trace files.
- [allure-robotframework](software-development-quality-assurance.md#allure-robotframework) - Allure Robot Framework integration
- [faker-vehicle](software-development-libraries-4.md#faker-vehicle) - Vehicle related Provider for the Faker Python package.
- [django-slowtests](internet-www-http.md#django-slowtests) - locate your slowest tests
- [pytest-testrail](software-development-quality-assurance.md#pytest-testrail) - A pytest plugin for creating TestRail runs and adding results
- [gxformat2](software-development.md#gxformat2) - Galaxy Workflow Format 2 Descriptions
- [pytest-jira](software-development-quality-assurance.md#pytest-jira) - py.test JIRA integration plugin, using markers
- [allure-pytest-bdd](software-development-quality-assurance.md#allure-pytest-bdd) - Allure pytest-bdd integration
- [pytest-httpbin](software-development-libraries-4.md#pytest-httpbin) - Easily test your HTTP library against a local copy of httpbin
- [genie.telemetry](software-development-build-tools.md#genietelemetry) - Genie libs Telemetry: Genie Telemetry Libraries
- [pylint-junit](software-development-libraries-4.md#pylint-junit) - pylint reporter for junit format.
- [junit-xml-2](software-development-build-tools.md#junit-xml-2) - Fork of https://github.com/kyrus/python-junit-xml that has tarball published to pypi
- [genie.libs.robot](software-development-build-tools.md#genielibsrobot) - Genie libs Robot: RobotFramework libraries to interact with Genie
- [genie.trafficgen](software-development-build-tools.md#genietrafficgen) - Genie Library for traffic generator connection support
- [pyats.contrib](software-development-build-tools.md#pyatscontrib) - Open source package for pyATS framework extensions.
- [pyats.robot](software-development-build-tools.md#pyatsrobot) - pyATS Robot: Robot Module
- [chromedriver-binary](software-development-libraries-4.md#chromedriver-binary) - Installer for chromedriver.
- [rebrowser-playwright](internet-www-http-2.md#rebrowser-playwright) - A high-level API to automate web browsers
- [pysphere](software-development-libraries-4.md#pysphere) - Python API for interacting with the vSphere Web Services SDK
- [pyrig](software-development-build-tools.md#pyrig) - A Python project setup and management tool built on infrastructure as code and convention over configuration.
- [pylama](software-development-quality-assurance.md#pylama) - Code audit tool for python
- [skylos](security.md#skylos) - Python dead code, security and secrets scanner with a pull-request gate; narrower checks for TypeScript, Java and more.
- [radish-bdd](education-testing.md#radish-bdd) - Behaviour-Driven-Development tool for Python
- [pydantic-factories](software-development.md#pydantic-factories) - Mock data generation for pydantic based models and python dataclasses
- [pyjoulescope-driver](scientific-engineering-2.md#pyjoulescope-driver) - Joulescope™ driver
- [xlcalculator](office-business-financial.md#xlcalculator) - Converts MS Excel formulas to Python and evaluates them.
- [ops-scenario](software-development-quality-assurance.md#ops-scenario) - Python library providing a state-transition testing API for Operator Framework charms.
- [mailosaur](software-development-libraries-4.md#mailosaur) - The Mailosaur Python library lets you integrate email and SMS testing into your continuous integration process.
- [roc-validator](scientific-engineering-2.md#roc-validator) - A Python package to validate RO-Crates
- [faker-e164](software-development-libraries-4.md#faker-e164) - Faker Provider to generate phone numbers in E164 format.
- [robotcode](software-development-debuggers.md#robotcode) - Command line interface for RobotCode
- [oidc-provider-mock](internet-www-http-2.md#oidc-provider-mock) - OpenID Connect provider server for testing authentication
- [edam-ontology](software-development.md#edam-ontology) - Versioned, Python packaged EDAM ontology (http://edamontology.org/) data.
- [isystem.connect](software-development-debuggers.md#isystemconnect) - isystem.connect for Python
- [facebook-wda](software-development-libraries-4.md#facebook-wda) - Python Client for Facebook WebDriverAgent
- [zope.testbrowser](internet-www-http-2.md#zopetestbrowser) - Programmable browser for functional black-box tests
- [attrs-strict](software-development-libraries-4.md#attrs-strict) - Runtime validators for attrs
- [pytest-container](software-development-quality-assurance.md#pytest-container) - Pytest fixtures for writing container based tests
- [nemo-evaluator](scientific-engineering-artificial-intelligence.md#nemo-evaluator) - NeMo Evaluator — benchmark environments, pluggable solvers, interceptor proxy, and decision-grade scoring for LLMs
- [fuzzfetch](security.md#fuzzfetch) - Downloader for firefox/jsshell builds.
- [random-address](software-development-libraries-4.md#random-address) - Retrieve real random US addresses, with coordinates, for tests and fixtures
- [faker-enum](software-development-libraries-4.md#faker-enum) - Enum provider for the Faker Python package.
- [zope.testrunner](software-development-libraries-4.md#zopetestrunner) - Zope testrunner script.
- [pytest-mongo](software-development-libraries-4.md#pytest-mongo) - MongoDB process and client fixtures plugin for Pytest.
- [mongomock-ng](database.md#mongomock-ng) - Replacement fake pymongo stub for testing simple MongoDB-dependent code
- [pytest-progress](software-development-libraries-4.md#pytest-progress) - pytest plugin for instant test progress status
- [anta](software-development-libraries-4.md#anta) - Arista Network Test Automation (ANTA) Framework
- [galaxy-release-util](software-development.md#galaxy-release-util) - Utlity for various tasks around creating Galaxy releases
- [markdown-it-reporter](software-development.md#markdown-it-reporter) - Galaxy Workflow Format 2 Descriptions
- [jsonsubschema](software-development-libraries-5.md#jsonsubschema) - A tool to check whether a JSON schema is subset/subschema of another JSON schema
- [Flask-Injector](software-development-libraries-5.md#flask-injector) - Adds Injector, a Dependency Injection framework, support to Flask.
- [python-dbusmock](software-development-libraries-5.md#python-dbusmock) - Mock D-Bus objects
- [marionette-driver](software-development-quality-assurance.md#marionette-driver) - Marionette Driver
- [pytest-flask-sqlalchemy](software-development-libraries-5.md#pytest-flask-sqlalchemy) - A pytest plugin for preserving test isolation in Flask-SQlAlchemy using database transactions.
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
- [aioresponses-ng](internet-www-http-2.md#aioresponses-ng) - Maintained fork of aioresponses with aiohttp compatibility fixes
- [ministack](internet.md#ministack) - Free, open-source local AWS emulator — drop-in LocalStack replacement
- [invisible-core](internet-www-http-2.md#invisible-core) - Pure config for a stealth Firefox profile: seed -> fingerprint -> prefs, engine download, proxy, geo, and the Juggler client the wrappers drive it with. Zero Playwright.
- [pytest-splinter](software-development-libraries-5.md#pytest-splinter) - Splinter plugin for pytest testing framework
- [pytest-rabbitmq](software-development-libraries-5.md#pytest-rabbitmq) - RabbitMQ process and client fixtures for pytest
- [vunit-hdl](scientific-engineering-electronic-design-automation-eda.md#vunit-hdl) - VUnit is an open source unit testing framework for VHDL/SystemVerilog.
