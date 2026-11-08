# Unclassified / Y

[Index](README.md) · 32 packages in this topic, by downloads.

### youtube-transcript-api

This is a python API which allows you to get the transcripts/subtitles for a given YouTube video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!

`pip install youtube-transcript-api` · installs (wheel) · licence: MIT License · rank 888 · last release 2026-11-05 · [PyPI](https://pypi.org/project/youtube-transcript-api/) · [source](https://github.com/jdepoix/youtube-transcript-api)

<details><summary>README extract</summary>

This is a python API which allows you to retrieve the transcript/subtitles for a given YouTube video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do! ...

Example:
```python
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

# retrieve the available transcripts
transcript_list = ytt_api.list('video_id')

# iterate over all available transcripts
for transcript in transcript_list:

    # the Transcript object provides metadata properties
    print(
        transcript.video_id,
...
```

...

</details>

### yt-dlp-ejs

External JavaScript for yt-dlp supporting many runtimes

`pip install yt-dlp-ejs` · installs (wheel) · licence: Unlicense AND MIT AND ISC · rank 1931 · last release 2026-03-17 · [PyPI](https://pypi.org/project/yt-dlp-ejs/) · [docs](https://github.com/yt-dlp/ejs#readme) · [source](https://github.com/yt-dlp/ejs)

<details><summary>README extract</summary>

External JavaScript for yt-dlp supporting many runtimes

Sections: yt-dlp-ejs, Build, Tests, Upgrading packages, Licensing

</details>

### yaml-config

Python client for reading yaml based config files

`pip install yaml-config` · installs (wheel) · licence: not stated · rank 2289 · last release 2020-06-22 · [PyPI](https://pypi.org/project/yaml-config/)

### yamale

A schema and validator for YAML.

`pip install yamale` · installs (wheel) · licence: MIT License · rank 2749 · last release 2025-11-20 · [PyPI](https://pypi.org/project/yamale/)

<details><summary>README extract</summary>

| :warning: Ensure that your schema definitions come from internal or trusted sources. Yamale does not protect against intentionally malicious schemas. |

A schema and validator for YAML.

What's YAML? See the current spec here and an introduction
to the syntax here.

Requirements

* Python 3.8+
* PyYAML
* ruamel.yaml (optional)

Install ...

Example:
```python
# Import Yamale and make a schema object:
import yamale
schema = yamale.make_schema('./schema.yaml')

# Create a Data object
data = yamale.make_data('./data.yaml')

# Validate data against the schema. Throws a ValueError if data is invalid.
yamale.validate(schema, data)
```

...

</details>

### ytsaurus-client

Python client for YTsaurus system and miscellaneous libraries.

`pip install ytsaurus-client` · installs (wheel) · licence: Apache 2.0 · rank 3134 · last release 2026-10-02 · [PyPI](https://pypi.org/project/ytsaurus-client/)

<details><summary>README extract</summary>

YTsaurus — is a platform for distributed storage and processing of large amounts of data with support of MapReduce, distributed file system and NoSQL key-value storage.

This library provides python client for YTsaurus, that provides python-friendly mechanism for running operations, reading/writing data to the cluster and most of the other ...

</details>

### yggdrasil-engine

Engine for evaluating Unleash feature flags

`pip install yggdrasil-engine` · installs (wheel) · licence: MIT License · rank 3173 · last release 2026-10-07 · [PyPI](https://pypi.org/project/yggdrasil-engine/)

<details><summary>README extract</summary>

Provides high level bindings to the Unleash Yggdrasil engine.

This project uses poetry.

Before you begin, you'll need to setup the native library. You'll need a Rust compiler. If you're on Windows, you'll need bash or just read the script and do the equivalent powershell steps.

To run tests:

Sections: Python Bindings to Yggdrasil, Build and test, Lint and format, Publish

</details>

### yara-python

Python interface for YARA

`pip install yara-python` · installs from source (sdist only) · licence: Apache Software License · rank 3210 · last release 2025-05-27 · [PyPI](https://pypi.org/project/yara-python/)

<details><summary>README extract</summary>

.. image::
 :target:

With this library you can use `YARA < from
your Python programs. It covers all YARA's features, from compiling, saving
and loading rules to scanning files, strings and processes.

Here it goes a little example:

.. code-block:: python ...

</details>

### ytsaurus-yson

C++ bindings for YSON.

`pip install ytsaurus-yson` · installs (wheel) · licence: Apache 2.0 · rank 4153 · last release 2025-03-06 · [PyPI](https://pypi.org/project/ytsaurus-yson/)

<details><summary>README extract</summary>

YTsaurus — is a platform for distributed storage and processing of large amounts of data with support of MapReduce, distributed file system and NoSQL key-value storage.

This library provides C++ bindings for YSON format.

</details>

### yourdfpy

A simpler and easier-to-use library for loading, manipulating, saving, and visualizing URDF files.

`pip install yourdfpy` · installs (wheel) · licence: MIT License · rank 4463 · last release 2026-01-23 · [PyPI](https://pypi.org/project/yourdfpy/) · [source](https://github.com/clemense/yourdfpy/)

<details><summary>README extract</summary>

Yet anOther URDF parser for Python. Yup, it's another one. Deal with it.

Yourdfpy is a simpler and easier-to-use library for loading, manipulating, validating, saving, and visualizing URDF files.

Example:
```python
robot_assets = ['robot-assets/urdfs/robots/barret_hand/bhand_model.URDF', 'robot-assets/urdfs/robots/robotiq_gripper/robotiq_arg85_description.URDF', 'robot-assets/urdfs/robots/anymal/anymal.urdf', 'robot-assets/urdfs/robots/franka_panda/panda.urdf', 'robot-assets/urdfs/robots/ginger_robot/gingerurdf.urdf', 'robot-assets/urdfs/robots/halodi/eve_r3.
...
```

Sections: yourdfpy, Visualization, But why another one?!?

</details>

### y-py

Python bindings for the Y-CRDT built from yrs (Rust)

`pip install y-py` · installs from source (sdist only) · licence: MIT License · rank 5151 · last release 2023-10-05 · [PyPI](https://pypi.org/project/y-py/) · [source](https://github.com/y-crdt/ypy)

<details><summary>README extract</summary>

Ypy is a Python binding for Y-CRDT. It provides distributed data types that enable real-time collaboration between devices. Ypy can sync data with any other platform that has a Y-CRDT binding, allowing for seamless cross-domain communication. The library is a thin wrapper around Yrs, taking advantage of the safety and performance of Rust. ...

Example:
```python
import y_py as Y

d1 = Y.YDoc()
# Create a new YText object in the YDoc
text = d1.get_text('test')
# Start a transaction in order to update the text
with d1.begin_transaction() as txn:
    # Add text contents
    text.extend(txn, "hello world!")

# Create another document
d2 = Y.YDoc()
# Share state with the original document
...
```

Sections: Ypy, Getting Started, Tests, Using Hatch, Build Ypy, Ypy in WASM (Pyodide)

</details>

### ypy-websocket

WebSocket connector for Ypy

`pip install ypy-websocket` · installs (wheel) · licence: MIT License · rank 5401 · last release 2023-10-04 · [PyPI](https://pypi.org/project/ypy-websocket/) · [source](https://github.com/y-crdt/ypy-websocket)

<details><summary>README extract</summary>

Ypy-websocket is an async WebSocket connector for Ypy.

Documentation:

Source Code:

Ypy-websocket is a Python library for building WebSocket servers and clients that connect and synchronize shared documents.
It can be used to create collaborative web applications.

The following diagram illustrates a typical architecture. ...

</details>

### ydb

YDB Python SDK

`pip install ydb` · installs (wheel) · licence: Apache 2.0 · rank 5573 · last release 2026-10-28 · [PyPI](https://pypi.org/project/ydb/)

<details><summary>README extract</summary>

YDB Python SDK

Officially supported Python client for YDB.

Documentation:

Sections: Quickstart, Prerequisites

</details>

### yandexcloud

The Yandex Cloud official SDK

`pip install yandexcloud` · installs (wheel) · licence: MIT · rank 5637 · last release 2026-11-02 · [PyPI](https://pypi.org/project/yandexcloud/)

<details><summary>README extract</summary>

[][pypi-url]
[][build-url]
[][license-url]

<!-- Badges -->

Need to automate your infrastructure or use services provided by Yandex.Cloud? We've got you covered.

Installation:

 pip install yandexcloud

Example:
```python
sdk = yandexcloud.SDK()
```

Sections: Yandex.Cloud SDK (Python), Getting started, Metadata Service, Service Account Keys, IAM tokens, Override service endpoint, Override in client, Override in sdk config, Switch SDK region, Retries, Dependencies, Adding new project dependency with uv, Adding new optional dependency with uv, Git hooks

</details>

### yara-x

Python bindings for YARA-X

`pip install yara-x` · installs (wheel) · licence: BSD License · rank 5704 · last release 2026-11-05 · [PyPI](https://pypi.org/project/yara-x/) · [source](https://github.com/VirusTotal/yara-x.git)

<details><summary>README extract</summary>

The official Python library for YARA-X.
Supports Python 3.9+ in Linux, MacOS and Windows.

For more information about how to use this library, please check
the documentation.

Example:
```python
import yara_x

rules = yara_x.compile('''
  rule test {
    strings:
      $a = "foobar"
    condition:
      $a
  }''')

results = rules.scan(b"foobar")

assert results.matching_rules[0].identifier == "test"
assert results.matching_rules[0].patterns[0].identifier == "$a"
assert results.matching_rules[0].patterns[0].matches[0].offset == 0
...
```

</details>

### ydb-dbapi

YDB Python DBAPI which complies with PEP 249

`pip install ydb-dbapi` · installs (wheel) · licence: not stated · rank 6391 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ydb-dbapi/) · [source](https://github.com/ydb-platform/ydb-python-dbapi/)

<details><summary>README extract</summary>

Python DBAPI to `YDB`, which provides both sync and async drivers and complies with PEP249.

Example:
```python
import ydb_dbapi

connection = ydb_dbapi.connect(
    host="localhost", port="2136", database="/local"
) # sync connection

async_connection = await ydb_dbapi.async_connect(
    host="localhost", port="2136", database="/local"
) # async connection
```

Sections: YDB Python DBAPI, Introduction, Usage, Query parameters, Standard mode (`pyformat=True`), Native YDB mode (default, deprecated)

</details>

### ytmusicapi

Unofficial API for YouTube Music

`pip install ytmusicapi` · installs (wheel) · licence: MIT · rank 7967 · last release 2026-09-16 · [PyPI](https://pypi.org/project/ytmusicapi/) · [docs](https://ytmusicapi.readthedocs.io) · [source](https://github.com/sigma67/ytmusicapi)

<details><summary>README extract</summary>

ytmusicapi is a Python 3 library to send requests to the YouTube Music API.
It emulates YouTube Music web client requests using the user's cookie data for authentication.

Features:
| Browsing:

* search (including all filters) and suggestions
* get artist information and releases (songs, videos, albums, singles, related artists)
* get user information (videos, playlists)
* get albums
* get song metadata
* get watch playlists ...

Example:
```python
from ytmusicapi import YTMusic

yt = YTMusic('oauth.json')
playlistId = yt.create_playlist('test', 'test description')
search_results = yt.search('Oasis Wonderwall')
yt.add_playlist_items(playlistId, search_results[0])
```

Sections: ytmusicapi: Unofficial API for YouTube Music, Features, Requirements, Setup, Usage

</details>

### yaql

YAQL - Yet Another Query Language

`pip install yaql` · installs (wheel) · licence: Apache Software License · rank 8061 · last release 2025-10-09 · [PyPI](https://pypi.org/project/yaql/) · [source](https://opendev.org/openstack/yaql/)

<details><summary>README extract</summary>

YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. ...

Sections: YAQL: Yet Another Query Language, Quickstart, Project Resources

</details>

### yandex-query-client

The Yandex Query official HTTP client

`pip install yandex-query-client` · installs (wheel) · licence: MIT License · rank 8430 · last release 2024-05-10 · [PyPI](https://pypi.org/project/yandex-query-client/)

<details><summary>README extract</summary>

Example:
```python
# IAM token to access YandexQuery service
IAM_TOKEN="...."

# Folder ID to work within
PROJECT="my_folder_id"

config = YQHttpClientConfig(IAM_TOKEN, PROJECT)
client = YQHttpClient(config)

# start new query
query_id = client.create_query(query_text="select 777", name="my sample query")

# wait query to succeed
...
```

</details>

### yte

A YAML template engine with Python expressions

`pip install yte` · installs (wheel) · licence: MIT · rank 8710 · last release 2025-11-27 · [PyPI](https://pypi.org/project/yte/) · [source](https://github.com/yte-template-engine/yte)

<details><summary>README extract</summary>

YTE is a template engine for YAML format that utilizes the YAML structure in combination with Python expressions for enabling to dynamically build YAML documents.

The key idea of YTE is to rely on the YAML structure to enable conditionals, loops and other arbitrary Python expressions to dynamically render YAML files. ...

Sections: YTE - A YAML template engine with Python expressions, Comparison with other engines

</details>

### yunchang

a package for long context attention

`pip install yunchang` · installs (wheel) · licence: Apache Software License · rank 9212 · last release 2026-01-13 · [PyPI](https://pypi.org/project/yunchang/)

<details><summary>README extract</summary>

[\[Tech Report\] USP: A Unified Sequence Parallelism Approach for Long Context Generative AI](

This repo provides a sequence parallel approach that synergizes the strengths of two popular distributed attentions, i.e. DeepSpeed-Ulysses-Attention and Ring-Attention, delivering a more general and stronger versatility and better performance. ...

Features:
- Ulysses is sensitive to the number of attention heads.
The parallelism degree in Ulysses cannot exceed the number of heads.
Consequently, it is not suitable for GQA (Grouped Query Attention) and MQA (Multi-Query Attention) scenarios. ...

Example:
```python
from yunchang import (
    AsyncLongContextAttention,
    LongContextAttention,
    set_seq_parallel_pg,
    EXTRACT_FUNC_DICT
)
from yunchang.kernels import AttnType

...

</details>

### yesqa

Automatically remove unnecessary `# noqa` comments.

`pip install yesqa` · installs (wheel) · licence: MIT License · rank 9233 · last release 2023-06-10 · [PyPI](https://pypi.org/project/yesqa/)

<details><summary>README extract</summary>

A tool (and pre-commit hook) to automatically remove unnecessary `# noqa`
comments, for example: a check that's no longer applicable (say you increased your
max line length), a mistake (`# noqa` added to a line that wasn't failing),
or other code in the file caused it to no longer need a `# noqa` (such as an unused import).

Sections: yesqa, As a pre-commit hook

</details>

### ydb-sqlalchemy

YDB Dialect for SQLAlchemy

`pip install ydb-sqlalchemy` · installs (wheel) · licence: Apache 2.0 · rank 10765 · last release 2026-09-14 · [PyPI](https://pypi.org/project/ydb-sqlalchemy/)

<details><summary>README extract</summary>

This repository contains YQL dialect for SqlAlchemy 2.0.

Documentation:

Note: Dialect also works with SqlAlchemy 1.4, but it is not fully tested.

Example:
```python
import sqlalchemy as sa

engine = sa.create_engine("yql+ydb://localhost:2136/local")

with engine.connect() as conn:
  rs = conn.execute(sa.text("SELECT 1 AS value"))
  print(rs.fetchone())
```

Sections: YDB Dialect for SQLAlchemy, Via PyPI, Getting started, Authentication, Static Credentials, Token Credentials, Service Account Credentials, Credentials from YDB SDK, Migrations, Run Tests, Additional Notes, Pandas

</details>

### yookassa

YooKassa API SDK Python Library

`pip install yookassa` · installs from source (sdist only) · licence: MIT License · rank 11438 · last release 2026-10-06 · [PyPI](https://pypi.org/project/yookassa/)

<details><summary>README extract</summary>

Russian | English

This product is used for managing payments under The YooKassa API
For usage by those who implemented YooKassa using the API method.

Features:
* Version 3.x supports Python >=3.7. To work on earlier versions of Python, use versions of yookassa 2.x
* Changing the directory/file structure affected some package imports. ...

Example:
```python
import yookassa
```

Sections: YooKassa API Python Client Library, Features, Requirements, Under console using pip, Commencing work

</details>

### youtube-search

Perform YouTube video searches without the API

`pip install youtube-search` · installs (wheel) · licence: MIT License · rank 11842 · last release 2025-12-06 · [PyPI](https://pypi.org/project/youtube-search/)

<details><summary>README extract</summary>

Python function for searching for youtube videos to avoid using their heavily rate-limited API

To avoid using the API, this uses the form on the youtube homepage and scrapes the resulting page.

Sections: youtube_search, Example Usage, returns a json string, #, returns a dictionary

</details>

### yowasp-yosys

Yosys Open SYnthesis Suite

`pip install yowasp-yosys` · installs (wheel) · licence: ISC · rank 11848 · last release 2026-10-13 · [PyPI](https://pypi.org/project/yowasp-yosys/) · [source](https://github.com/YoWASP/yosys)

<details><summary>README extract</summary>

This package provides Yosys binaries built for WebAssembly. See the overview of the YoWASP project for details.

Versioning

The version of this package is derived from the upstream Yosys package version in the `X.Y.Z` format, and is comprised of five or six parts in a `X.Y.Z.N.postM[.dev]` format, where the symbols are:

1. ...

</details>

### yamlcore

YAML 1.2 Support for PyYAML

`pip install yamlcore` · installs (wheel) · licence: MIT License · rank 12049 · last release 2024-10-09 · [PyPI](https://pypi.org/project/yamlcore/) · [docs](https://github.com/perlpunk/pyyaml-core) · [source](https://github.com/perlpunk/pyyaml-core)

<details><summary>README extract</summary>

Features:
At the time of this writing, there is a pending pull
request that adds YAML 1.2 Core
Schema Support for PyYAML.

It's blocked because there is a plan to redesign the API, and no new things
shall be added using the old API at this point. ...

Sections: Examples, Why?, Differences, Duplicate keys are not allowed

</details>

### yowasp-runtime

Common runtime for YoWASP packages

`pip install yowasp-runtime` · installs (wheel) · licence: ISC · rank 12085 · last release 2026-07-21 · [PyPI](https://pypi.org/project/yowasp-runtime/) · [source](https://github.com/YoWASP/runtime-py)

<details><summary>README extract</summary>

This package is an internal support package for the YoWASP project. It handles interfacing with the WebAssembly runtime and the supported operating systems. Do not depend on this package in your own code.

Configuration

The YoWASP runtime can be configured through environment variables: ...

Sections: YoWASP Python runtime, `YOWASP_CACHE_DIR`, `YOWASP_MOUNT`

</details>

### yahooquery

Python wrapper for an unofficial Yahoo Finance API

`pip install yahooquery` · installs (wheel) · licence: MIT · rank 12180 · last release 2025-05-15 · [PyPI](https://pypi.org/project/yahooquery/)

<details><summary>README extract</summary>

Python wrapper for an unofficial Yahoo Finance API

Documentation:

Interactive Demo:

Source Code:

Blog Post:

Features:
Yahooquery is a python interface to unofficial Yahoo Finance API endpoints. The package allows a user to retrieve nearly all the data visible via the Yahoo Finance front-end.

Some features of yahooquery: ...

Example:
```python
from yahooquery import Ticker

aapl = Ticker('aapl')

aapl.summary_detail
```

Sections: Overview, Requirements, Yahoo Finance Premium Subscribers, Example, Multiple Symbol Example

</details>

### yearfrac

Daycount methods to compute date differences in year units

`pip install yearfrac` · installs from source (sdist only) · licence: MIT · rank 12515 · last release 2023-02-06 · [PyPI](https://pypi.org/project/yearfrac/)

<details><summary>README extract</summary>

Sections: yearfrac, Usage, Appendix, Python Commands

</details>

### yargy

Rule-based facts extraction for Russian language

`pip install yargy` · installs (wheel) · licence: MIT License · rank 13121 · last release 2023-07-24 · [PyPI](https://pypi.org/project/yargy/)

<details><summary>README extract</summary>

Yargy uses rules and dictionaries to extract structured information from Russian texts. Yargy is similar to Tomita parser.

Example:
```python
from yargy import Parser, rule, and, not
from yargy.interpretation import fact
from yargy.predicates import gram
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

Name = fact(
    'Name',
    ['first', 'last'],
)
Person = fact(
    'Person',
    ['position', 'name']
)

LAST = and(
    gram('Surn'),
...
```

Sections: Usage, Documentation

</details>

### yawsso

Yet Another AWS SSO - sync up AWS CLI v2 SSO login session to legacy CLI v1 credentials

`pip install yawsso` · installs (wheel) · licence: MIT · rank 13140 · last release 2026-04-21 · [PyPI](https://pypi.org/project/yawsso/)

<details><summary>README extract</summary>

Yet Another AWS SSO - sync up AWS CLI v2 SSO login session to legacy CLI v1 credentials.

> See also Release v1.0.0 Notes

- Required `Python >= 3.7`
- Required AWS CLI v2
- Assume you have already setup AWS SSO for your organization

- Do your per normal SSO login and, have at least one active SSO session cache: ...

Sections: yawsso, Prerequisite, Main Use Case, Additional Use Cases, Rename Profile on Sync, Export Tokens, Login, Login then Export token, Auto Login then Sync, Set Default, Show Account ID, Set Region, Encryption

</details>

### youtube-search-python

Search for YouTube videos, channels & playlists & get video information using link WITHOUT YouTube Data API v3

`pip install youtube-search-python` · installs (wheel) · licence: MIT License · rank 13792 · last release 2022-06-23 · [PyPI](https://pypi.org/project/youtube-search-python/)

<details><summary>README extract</summary>

Example:
```python
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

print(videosSearch.result())
```

Sections: youtube-search-python, WITHOUT YouTube Data API v3., Sync, Search for only videos, Async, More Examples, Search for only channels, Search for only playlists, Search with a filter or sort, Search for everything, Advanced, Getting next page search results, Getting video information using video link or video ID

</details>

