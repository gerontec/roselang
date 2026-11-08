# Internet / Log Analysis

[Index](README.md) · 11 packages in this topic, 3 more listed under another topic, by downloads.

### jsonlines

Library with helpers for the jsonlines file format

`pip install jsonlines` · installs (wheel) · licence: BSD License · rank 971 · last release 2023-09-01 · [PyPI](https://pypi.org/project/jsonlines/)

<details><summary>README extract</summary>

`jsonlines` is a Python library to simplify working with jsonlines
and ndjson data.

</details>

### django-axes

Keep track of failed login attempts in Django-powered sites.

`pip install django-axes` · installs (wheel) · licence: MIT License · rank 2049 · last release 2026-10-30 · [PyPI](https://pypi.org/project/django-axes/) · [docs](https://django-axes.readthedocs.io/) · [source](https://github.com/django-commons/django-axes)

<details><summary>README extract</summary>

Axes is a Django plugin for keeping track of suspicious
login attempts for your Django based website
and implementing simple brute-force attack blocking.

The name is sort of a geeky pun, since it can be interpreted as:

* `access`, as in monitoring access attempts, or
* `axes`, as in tools you can use to hack (generally on wood). ...

Features:
- Truncate usernames to the model field's maximum length before lockout lookups
 and failed-login logging to avoid database errors for oversized usernames. ...

Sections: django-axes, Functionality, Documentation, Issues, Changes, 9.0.0 (2026-10-30), Breaking changes and upgrading, Features and fixes, Project and packaging, 8.3.2 (2026-08-30), 8.3.1 (2026-02-11), 8.3.0 (2026-02-09), 8.2.0 (2026-02-06), 8.1.0 (2025-12-19)

</details>

### coralogix-logger

Coralogix Python SDK

`pip install coralogix-logger` · installs (wheel) · licence: Apache Software License · rank 5744 · last release 2025-12-10 · [PyPI](https://pypi.org/project/coralogix-logger/)

<details><summary>README extract</summary>

This package provides logging suites integrated with `Coralogix` logs analytics platform.
To see how to use it, please read Coralogix Python SDK Docs.

The SDK requires a Coralogix region to be specified. You can specify the region in two ways:

1. ...

Example:
```python
from coralogix.handlers import CoralogixLogger

# Using region parameter
logger = CoralogixLogger(
    private_key="YOUR_PRIVATE_KEY",
    app_name="MyApp",
    subsystem="backend",
    region="EU1"
)

# Or set via environment variable
# export CORALOGIX_REGION=EU1
```

Sections: Coralogix Python SDK, Region Selection

</details>

### dissect.cstruct

A Dissect module implementing a parser for C-like structures: structure parsing in Python made easy

`pip install dissect.cstruct` · installs (wheel) · licence: Apache-2.0 · rank 5973 · last release 2025-11-20 · [PyPI](https://pypi.org/project/dissect.cstruct/) · [docs](https://docs.dissect.tools/en/latest/projects/dissect.cstruct) · [source](https://github.com/fox-it/dissect.cstruct)

<details><summary>README extract</summary>

A Dissect module implementing a parser for C-like structures. Structure parsing in Python made easy. With cstruct, you
can write C-like structures and use them to parse binary data, either as file-like objects or bytestrings.

Parsing binary data with cstruct feels familiar and easy. ...

Example:
```python
from dissect.cstruct import cstruct

# Default endianness is LE, but can be configured using a kwarg or setting the 'endian' attribute
# e.g. cstruct(endian='>') or c_parser.endian = '>'
parser_def = """
# define SOME_CONSTANT   5

enum Example : uint16 {
    A, B = 0x5, C
};

struct some_struct {
    uint8   field_1;
...
```

...

</details>

### dissect.util

A Dissect module implementing various utility functions for the other Dissect modules

`pip install dissect.util` · installs (wheel) · licence: Apache-2.0 · rank 7182 · last release 2026-02-24 · [PyPI](https://pypi.org/project/dissect.util/) · [docs](https://docs.dissect.tools/en/latest/projects/dissect.util) · [source](https://github.com/fox-it/dissect.util)

<details><summary>README extract</summary>

A Dissect module implementing various utility functions for the other Dissect modules. For more information, please see
the documentation.

This project is part of the Dissect framework and requires Python.

Information on the supported Python versions can be found in the Getting Started section of the documentation.

Sections: dissect.util, Requirements, Build and test instructions

</details>

### pytricia

An efficient IP address storage and lookup module for Python.

`pip install pytricia` · installs from source (sdist only) · licence: not stated · rank 8767 · last release 2025-09-15 · [PyPI](https://pypi.org/project/pytricia/)

<details><summary>README extract</summary>

Pytricia is a Python module to store IP prefixes in a
patricia tree. It's based on Dave Plonka's modified patricia tree
code, and has three things to recommend it over related modules
(including py-radix and SubnetTree):

 * it's faster,

 * it works nicely in Python 3, and

 * there are a few nicer library features for manipulating the structure. ...

</details>

### dissect.ntfs

A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system

`pip install dissect.ntfs` · installs (wheel) · licence: AGPL-3.0-or-later · rank 9132 · last release 2026-02-24 · [PyPI](https://pypi.org/project/dissect.ntfs/) · [docs](https://docs.dissect.tools/en/latest/projects/dissect.ntfs) · [source](https://github.com/fox-it/dissect.ntfs)

_README extract left out: share-alike licence._

### dissect.esedb

Superseded by dissect.database. A Dissect module implementing a parser for Microsofts Extensible Storage Engine Database (ESEDB), used for example in Active Directory, Exchange and Windows Update

`pip install dissect.esedb` · installs (wheel) · licence: Apache-2.0 · rank 10140 · last release 2025-11-20 · [PyPI](https://pypi.org/project/dissect.esedb/) · [docs](https://docs.dissect.tools/en/latest/projects/dissect.esedb) · [source](https://github.com/fox-it/dissect.esedb)

<details><summary>README extract</summary>

A Dissect module implementing a parser for Microsofts Extensible Storage Engine Database (ESEDB), used for example in
Active Directory, Exchange and Windows Update. For more information, please see the
documentation.

This project has been superseded by `dissect.database`, which provides the same functionality along with broader database support.

Sections: dissect.esedb, Supersession notice, Requirements, Tools, Impacket compatibility shim for secretsdump.py, Build and test instructions

</details>

### CMRESHandler

Elasticsearch Log handler for the logging library

`pip install CMRESHandler` · installs (wheel) · licence: Apache Software License · rank 11267 · last release 2017-10-08 · [PyPI](https://pypi.org/project/CMRESHandler/)

<details><summary>README extract</summary>

licenseversionsstatusdownloads|
ci_statuscodecovgitter|

This library provides an Elasticsearch logging appender compatible with the
python standard logging library.

The code source is in github at

Features:
In some cases is quite useful to provide all the information available within the LogRecords as it contains
things such as exception information, the method, file, log line where the log was generated. ...

Example:
```python
from cmreslogging.handlers import CMRESHandler
handler = CMRESHandler(hosts=[{'host': 'localhost', 'port': 9200}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="my_python_index")
log = logging.getLogger("PythonTest")
log.setLevel(logging.INFO)
log.addHandler(handler)
```

...

</details>

### opensearch-logger

OpenSearch logging handler

`pip install opensearch-logger` · installs (wheel) · licence: Apache Software License · rank 11537 · last release 2025-08-13 · [PyPI](https://pypi.org/project/opensearch-logger/) · [docs](https://github.com/vduseev/opensearch-logger) · [source](https://github.com/vduseev/opensearch-logger)

<details><summary>README extract</summary>

This library provides a standard Python logging handler compatible with OpenSearch suite.

The goals of this project are

* to provide a simple and direct logging from Python to OpenSearch without *fluentd*, *logstash* or other middleware;
* keep it up to date with the growing difference between OpenSearch and Elasticsearch projects;
* keep the ...

Example:
```python
import logging
from opensearch_logger import OpenSearchHandler

handler = OpenSearchHandler(
    index_name="my-logs",
    hosts=["
    http_auth=("admin", "admin"),
    http_compress=True,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

logger = logging.getLogger(name)
...
```

...

</details>

### dissect.target

This module ties all other Dissect modules together, it provides a programming API and command line tools which allow easy access to various data sources inside disk images or file collections (a.k.a. targets)

`pip install dissect.target` · installs (wheel) · licence: AGPL-3.0-or-later · rank 14183 · last release 2026-02-25 · [PyPI](https://pypi.org/project/dissect.target/) · [docs](https://docs.dissect.tools/en/latest/projects/dissect.target) · [source](https://github.com/fox-it/dissect.target)

_README extract left out: share-alike licence._

## Also in this topic

- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [stringzilla](file-formats.md#stringzilla) - Search, hash, sort, and process strings faster via SWAR and SIMD
- [eql](database.md#eql) - Event Query Language
