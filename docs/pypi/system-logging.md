# System / Logging

[Index](README.md) · 17 packages in this topic, 44 more listed under another topic, by downloads.

### structlog

Structured Logging for Python

`pip install structlog` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 273 · last release 2026-06-06 · [PyPI](https://pypi.org/project/structlog/) · [docs](https://www.structlog.org/) · [source](https://github.com/hynek/structlog)

<details><summary>README extract</summary>

*structlog* is *the* production-ready logging solution for Python:

- Simple: Everything is about functions that take and return dictionaries – all hidden behind familiar APIs.
- Powerful: Functions and dictionaries aren’t just simple but also powerful.
 *structlog* leaves *you* in control.
- Fast: *structlog* is not hamstrung by designs of yore. ...

Sections: Introduction, Project Links, structlog* for Enterprise, Removed, Deprecated, Added, Changed, Fixed

</details>

### python-json-logger

JSON Log Formatter for the Python Logging Package

`pip install python-json-logger` · installs (wheel) · licence: BSD-2-Clause · rank 293 · last release 2026-08-15 · [PyPI](https://pypi.org/project/python-json-logger/) · [source](https://github.com/nhairs/python-json-logger)

<details><summary>README extract</summary>

Python JSON Logger enables you produce JSON logs when using Python's `logging` package.

JSON logs are machine readable allowing for much easier parsing and ingestion into log aggregation tools.

- Documentation
- Quickstart Guide
- Change Log
- Contributing

Sections: Python JSON Logger, Documentation

</details>

### loguru

Python logging made (stupidly) simple

`pip install loguru` · installs (wheel) · licence: MIT License · rank 337 · last release 2024-12-06 · [PyPI](https://pypi.org/project/loguru/) · [docs](https://loguru.readthedocs.io/en/stable/index.html)

<details><summary>README extract</summary>

______________

Loguru is a library which aims to bring enjoyable logging in Python.

Did you ever feel lazy about configuring a logger and used `print()` instead?... I did, yet logging is fundamental to every application and eases the process of debugging. ...

Features:
- Ready to use out of the box without boilerplate
- No Handler, no Formatter, no Filter: one function to rule them all
- Easier file logging with rotation / retention / compression
- Modern string formatting using braces style ...

Example:
```python
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")
```

...

</details>

### click-log

Logging integration for Click

`pip install click-log` · installs (wheel) · licence: MIT License · rank 1991 · last release 2022-03-13 · [PyPI](https://pypi.org/project/click-log/)

<details><summary>README extract</summary>

Integrates logging with click.

- Documentation
- Source code

</details>

### Logbook

A logging replacement for Python

`pip install Logbook` · installs (wheel) · licence: BSD-3-Clause · rank 2142 · last release 2026-08-05 · [PyPI](https://pypi.org/project/Logbook/) · [docs](https://logbook.readthedocs.io) · [source](https://github.com/getlogbook/logbook)

<details><summary>README extract</summary>

[][pypi]

[][gha]
[][pypi]

Logbook is a nice logging replacement.

It should be easy to setup, use and configure and support web applications :)

For more information:

</details>

### django-structlog

Structured Logging for Django

`pip install django-structlog` · installs (wheel) · licence: MIT License · rank 2256 · last release 2026-10-24 · [PyPI](https://pypi.org/project/django-structlog/) · [docs](https://django-structlog.readthedocs.io) · [source](https://github.com/jrobichaud/django-structlog)

<details><summary>README extract</summary>

pypiwheelsbuild-statusdocscoverageopen_issuespull_requests|
djangopythonlicenseblackruff|
django_packages|
watchersstarsforks|

django-structlog is a structured logging integration for Django project using structlog

Logging will then produce additional cohesive metadata on each logs that makes it easier to track events or incidents. ...

Example:
```python
>>> import logging
>>> logger = logging.get_logger(name)
>>> logger.info("An error occurred")
```

Sections: django-structlog, Additional Popular Integrations, Django REST framework, django-ninja, Celery, Django Tasks, Logging comparison, Standard logging, With django-structlog and flat_line, With django-structlog and json, Getting Started, Extending Request Log Metadata, Standard Loggers, Upgrading to 6.0+

</details>

### ecs-logging

Logging formatters for ECS (Elastic Common Schema) in Python

`pip install ecs-logging` · installs (wheel) · licence: Apache Software License · rank 2536 · last release 2026-01-19 · [PyPI](https://pypi.org/project/ecs-logging/) · [docs](https://github.com/elastic/ecs-logging-python) · [source](https://github.com/elastic/ecs-logging-python)

<details><summary>README extract</summary>

Check out the Elastic Common Schema (ECS) reference
for more information.

The library currently implements ECS 1.6.

Sections: ecs-logging-python, Documentation, Elastic APM Log Correlation

</details>

### splunk-handler

A Python logging handler that sends your logs to Splunk

`pip install splunk-handler` · installs (wheel) · licence: MIT License · rank 5097 · last release 2021-08-17 · [PyPI](https://pypi.org/project/splunk-handler/)

<details><summary>README extract</summary>

Splunk Handler is a Python Logger for sending logged events to an installation of Splunk Enterprise.

*This logger requires the destination Splunk Enterprise server to have enabled and configured the Splunk HTTP Event Collector.*

AWS Lambda has a custom implementation of Python Threading, and does not signal when the main thread exits. ...

Sections: Splunk Handler, A Note on Using with AWS Lambda, Usage, Logging Config, Splunk settings, Retry Logic

</details>

### json-logging

JSON Python Logging

`pip install json-logging` · installs (wheel) · licence: Apache Software License · rank 5123 · last release 2026-10-21 · [PyPI](https://pypi.org/project/json-logging/)

<details><summary>README extract</summary>

Python logging library to emit JSON log that can be easily indexed and
searchable by logging infrastructure such as
ELK.

Go here for full documentation:

</details>

### fluent-logger

A Python logging handler for Fluentd event collector

`pip install fluent-logger` · installs (wheel) · licence: not stated · rank 5130 · last release 2024-06-06 · [PyPI](https://pypi.org/project/fluent-logger/)

<details><summary>README extract</summary>

Many web/mobile applications generate huge amount of event logs (c,f.
login, logout, purchase, follow, etc). To analyze these event logs could
be really valuable for improving the service. However, the challenge is
collecting these logs easily and reliably. ...

Example:
```python
from fluent import sender

# for local fluent
logger = sender.FluentSender('app')

# for remote fluent
logger = sender.FluentSender('app', host='host', port=24224)
```

Sections: A Python structured logger for Fluentd/Fluent Bit, Requirements, Configuration, Usage, FluentSender Interface, Event-Based Interface, Handler for buffer overflow, Python logging.Handler interface, Asynchronous Communication, Circular queue mode

</details>

### axiom-py

Official bindings for the Axiom API

`pip install axiom-py` · installs (wheel) · licence: MIT License · rank 5666 · last release 2026-09-23 · [PyPI](https://pypi.org/project/axiom-py/) · [source](https://github.com/axiomhq/axiom-py.git)

<details><summary>README extract</summary>

> [!IMPORTANT]
> Version v0.15.0 removes the legacy result format, `query_legacy()` and the `QueryLegacy` types. APL queries return tabular results and you read them with `result.tables[0].events()`. Read MIGRATING.md.

Example:
```python
import axiom_py

client = axiom_py.Client()

client.ingest_events(dataset="DATASET_NAME", events=[{"foo": "bar"}, {"bar": "baz"}])
result = client.query(r"['DATASET_NAME'] | where foo == 'bar' | limit 100")
for row in result.tables[0].events():
    print(row)
```

Sections: axiom-py [][ci] [][pypi] [][pypi], Synchronous Client, Edge Ingestion, Metrics Queries (MPL), Asynchronous Client, Concurrent Operations, Documentation

</details>

### graypy

Python logging handlers that send messages in the Graylog Extended Log Format (GELF).

`pip install graypy` · installs (wheel) · licence: BSD License · rank 6935 · last release 2019-09-30 · [PyPI](https://pypi.org/project/graypy/)

<details><summary>README extract</summary>

Python logging handlers that send log messages in the
Graylog Extended Log Format (GELF).

graypy supports sending GELF logs to both Graylog2 and Graylog3 servers.

Example:
```python
import logging
import graypy

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)

my_logger.debug('Hello Graylog.')
```

Sections: graypy, Description, Using pip, Usage, UDP Logging, UDP GELF Chunkers, RabbitMQ Logging, Django Logging, Traceback Logging, Default Logging Fields, Adding Custom Logging Fields, Using LoggerAdapter, Using Filter

</details>

### logging-tree

Introspect and display the logger tree inside "logging"

`pip install logging-tree` · installs (wheel) · licence: BSD License · rank 7665 · last release 2024-05-03 · [PyPI](https://pypi.org/project/logging-tree/)

<details><summary>README extract</summary>

Introspection for the ``logging`` logger tree in the Standard Library.

You can install this package with the standard ``pip`` command::

 $ pip install logging_tree

The simplest way to use this package is to call ``printout()`` to see
the loggers, filters, and handlers that your application has configured: ...

</details>

### humiolib

Python SDK for connecting to Humio

`pip install humiolib` · installs (wheel) · licence: Apache Software License · rank 8979 · last release 2023-10-05 · [PyPI](https://pypi.org/project/humiolib/) · [docs](https://python-humio.readthedocs.io/)

<details><summary>README extract</summary>

The `humiolib` library is a wrapper for Humio's web API, supporting easy interaction with Humio directly from Python.
Full documentation for this repository can be found at

The vision for `humiolib` is to create an opinionated wrapper around the Humio web API, supporting log ingestion and log queries. ...

Example:
```python
from humiolib.HumioClient import HumioClient

# Creating the client
client = HumioClient(
     base_url= "
     repository= "sandbox",
     user_token="*")

# Using a streaming query
webStream = client.streaming_query("Login Attempt Failed", is_live=True)
for event in webStream:
    print(event)

# Using a queryjob
...
```

...

</details>

### mdc

Mapped Diagnostic Context (MDC) library for python

`pip install mdc` · installs from source (sdist only) · licence: not stated · rank 9801 · last release 2019-09-09 · [PyPI](https://pypi.org/project/mdc/)

<details><summary>README extract</summary>

This is thought to be an easy to use, import and go, library for Mapped Diagnostic Context style logging.

Logs should include all necessary fields collected by the python logging library.
Helper methods are provided to add context fields where required. ...

Example:
```python
>>> import logging
>>> from mdc import MDCHandler

>>> # use the MDCHandler only
>>> logging.basicConfig(level=logging.DEBUG, handlers=[MDCHandler()])

>>> # the MDC contextmanager
>>> with MDC(foo='bar'):
...     logging.warning('foobar')
{ ..., "mdc": { "foo": "bar" }, "extra": {}, ... }

>>> # the with_mdc decorator
>>> @with_mdc(test='123')
...
```

Sections: MDC, Usage

</details>

### splunk-hec-handler

A Python logging handler to sends logs to Splunk using HTTP event collector (HEC)

`pip install splunk-hec-handler` · installs (wheel) · licence: MIT License · rank 11888 · last release 2023-02-16 · [PyPI](https://pypi.org/project/splunk-hec-handler/)

<details><summary>README extract</summary>

Features:
1. Log messages to Splunk via HTTP Event Collector (HEC).
See Splunk HEC Documentation
2. All messages are logged as '_json' sourcetype by default.
3. ...

Example:
```python
import logging
from splunk_hec_handler import SplunkHecHandler
logger = logging.getLogger('SplunkHecHandlerExample')
logger.setLevel(logging.DEBUG)

# If using self-signed certificate, set ssl_verify to False
# If using http, set proto to http
splunk_handler = SplunkHecHandler('splunkfw.domain.tld',
...
```

Sections: Features, Examples, Basic, Advanced, Todo

</details>

### ansilogs

Colored, single-line log output for command-line tools: a dependency-free coloredlogs.install() replacement

`pip install ansilogs` · installs (wheel) · licence: MIT License · rank 13794 · last release 2026-10-19 · [PyPI](https://pypi.org/project/ansilogs/)

<details><summary>README extract</summary>

Colored, single-line log output for command-line tools. A small, dependency-free replacement
for `coloredlogs.install()`.

- One line per record: `<time> <host> <name>[<pid>] <LEVEL> <message>`; tracebacks follow
 uncolored. ...

Example:
```python
import logging

import ansilogs

ansilogs.install(logging.DEBUG)
logging.getLogger(name).warning("careful")
```

Sections: ansilogs, API, Migrating from coloredlogs

</details>

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [wandb](scientific-engineering-artificial-intelligence.md#wandb) - A CLI and library for interacting with the Weights & Biases API.
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [jsonlines](internet-log-analysis.md#jsonlines) - Library with helpers for the jsonlines file format
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [yaspin](software-development.md#yaspin) - Yet Another Terminal Spinner
- [django-axes](internet-log-analysis.md#django-axes) - Keep track of failed login attempts in Django-powered sites.
- [django-health-check](software-development-quality-assurance.md#django-health-check) - Monitor the health of your Django app and its connected services.
- [python-can](software-development-embedded-systems.md#python-can) - Controller Area Network interface module for Python
- [concurrent-log-handler](software-development-libraries.md#concurrent-log-handler) - RotatingFileHandler replacement with concurrency, gzip and Windows support. Size and time based rotation.
- [stringzilla](file-formats.md#stringzilla) - Search, hash, sort, and process strings faster via SWAR and SIMD
- [viztracer](software-development-bug-tracking.md#viztracer) - A debugging and profiling tool that can trace and visualize python code execution
- [rollbar](internet-www-http.md#rollbar) - Easy and powerful exception tracking with Rollbar. Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.
- [python-logging-loki](internet-www-http.md#python-logging-loki) - Python logging handler for Grafana Loki.
- [logfury](software-development-libraries-2.md#logfury) - ('Toolkit for responsible, low-boilerplate logging of library method calls',)
- [chalk-viztracer](software-development-bug-tracking.md#chalk-viztracer) - A debugging and profiling tool that can trace and visualize python code execution (Chalk fork)
- [systemd-python](software-development-libraries-2.md#systemd-python) - Python interface for libsystemd
- [python-logstash](internet-www-http.md#python-logstash) - Python logging handler for Logstash.
- [clearml](scientific-engineering-artificial-intelligence.md#clearml) - ClearML - Auto-Magical Experiment Manager, Version Control, and MLOps for AI
- [arize](scientific-engineering-artificial-intelligence.md#arize) - A helper library to interact with Arize AI APIs
- [coralogix-logger](internet-log-analysis.md#coralogix-logger) - Coralogix Python SDK
- [verboselogs](software-development.md#verboselogs) - Verbose logging level for Python's logging module
- [Autologging](software-development-libraries-2.md#autologging) - Autologging makes logging and tracing Python classes easy.
- [arize-otel](scientific-engineering-artificial-intelligence.md#arize-otel) - OpenTelemetry tracing helpers for Arize
- [pylogbeat](internet-www-http.md#pylogbeat) - Simple, incomplete implementation of the Beats protocol used by Elastic Beats and Logstash.
- [clearml-agent](scientific-engineering-artificial-intelligence.md#clearml-agent) - ClearML Agent - Auto-Magical DevOps for Deep Learning
- [python-logstash-async](internet-www-http.md#python-logstash-async) - Asynchronous Python logging handler for Logstash.
- [prov](scientific-engineering-information-analysis.md#prov) - A library for W3C Provenance Data Model supporting PROV-N, PROV-JSON, PROV-XML, PROV-O (RDF) and PROV-JSONLD
- [pygelf](software-development-libraries-3.md#pygelf) - Logging handlers with GELF support
- [tailer](software-development-libraries-3.md#tailer) - Python tail is a simple implementation of GNU tail and head.
- [minilog](software-development.md#minilog) - Minimalistic wrapper for Python logging.
- [ascii-colors](software-development-libraries-3.md#ascii-colors) - A Python library for rich terminal output with advanced logging features.
- [robocorp-log](software-development-libraries-3.md#robocorp-log) - Automatic trace logging for Python
- [safe-init](software-development-libraries-3.md#safe-init) - Safe Init is a Python library that enhances AWS Lambda functions with advanced error handling, logging, monitoring, and resilience features, providing comprehensive observability and reliability for serverless applications.
- [python-evtx](security.md#python-evtx) - Pure Python parser for Windows event log files (.evtx).
- [pygtail](software-development-libraries-3.md#pygtail) - Reads log file lines that have not been read.
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [CMRESHandler](internet-log-analysis.md#cmreshandler) - Elasticsearch Log handler for the logging library
- [click-extra](documentation-sphinx.md#click-extra) - 🌈 Drop-in replacement for Click to make user-friendly and colorful CLI
- [opensearch-logger](internet-log-analysis.md#opensearch-logger) - OpenSearch logging handler
- [pipestat](scientific-engineering-bio-informatics.md#pipestat) - A pipeline results reporter
- [glog](software-development-libraries-4.md#glog) - Simple Google-style logging wrapper for Python.
