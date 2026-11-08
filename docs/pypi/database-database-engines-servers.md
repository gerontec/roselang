# Database / Database Engines/Servers

[Index](README.md) · 17 packages in this topic, 25 more listed under another topic, by downloads.

### prisma

Prisma Client Python is an auto-generated and fully type-safe database client

`pip install prisma` · installs (wheel) · licence: Apache Software License · rank 4046 · last release 2024-08-16 · [PyPI](https://pypi.org/project/prisma/) · [docs](https://prisma-client-py.readthedocs.io) · [source](https://github.com/RobertCraigie/prisma-client-py)

<details><summary>README extract</summary>

Prisma Client Python is a next-generation ORM built on top of Prisma that has been designed from the ground up for ease of use and correctness.

Prisma is a TypeScript ORM with zero-cost type safety for your database, although don't worry, Prisma Client Python interfaces with Prisma using Rust, you don't need Node or TypeScript. ...

Features:
Unlike other Python ORMs, Prisma Client Python is fully type safe and offers native support for usage with and without `async`. All you have to do is specify the type of client you would like to use for your project in the Prisma schema file. ...

Example:
```python
users = await db.user.find_many()
```

...

</details>

### usearch

Smaller & Faster Single-File Vector Search Engine from Unum

`pip install usearch` · installs (wheel) · licence: Apache-2.0 · rank 4895 · last release 2026-10-25 · [PyPI](https://pypi.org/project/usearch/)

<details><summary>README extract</summary>

Similarity Search & Clustering Engine for Vectors & 🔜 Texts

Spatial • Binary • Probabilistic • User-Defined Metrics

C++11 •
Python 3 •
JavaScript •
Java •
Rust •
C99 •
Objective-C •
Swift •
C# •
Go •
Wolfram

Linux • macOS • Windows • iOS • Android • WebAssembly •
SQLite

- ✅ 10x faster HNSW implementation than FAISS. ...

Example:
```python
# pip install usearch

import numpy as np
from usearch.index import Index

index = Index(ndim=3)               # Default settings for 3D vectors
vector = np.array([0.2, 0.6, 0.4])  # Can be a matrix for batch operations
index.add(42, vector)               # Add one or many vectors in parallel
...
```

...

</details>

### pysqlite3-binary

DB-API 2.0 interface for Sqlite 3.x

`pip install pysqlite3-binary` · installs (wheel) · licence: zlib/libpng License · rank 4963 · last release 2025-12-03 · [PyPI](https://pypi.org/project/pysqlite3-binary/)

### pyoxigraph

Python bindings of Oxigraph, a SPARQL database and RDF toolkit

`pip install pyoxigraph` · installs (wheel) · licence: Apache Software License; MIT License · rank 5065 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pyoxigraph/) · [docs](https://pyoxigraph.readthedocs.io/) · [source](https://github.com/oxigraph/oxigraph/tree/main/python)

<details><summary>README extract</summary>

Pyoxigraph is a graph database library implementing the SPARQL standard.
It is a Python library written on top of Oxigraph.

Pyoxigraph offers two stores with SPARQL 1.1 capabilities.
One of the store is in-memory, and the other one is disk based. ...

Sections: Pyoxigraph (Oxigraph for Python), Help, Tests, Docs

</details>

### sqlean.py

sqlite3 with extensions

`pip install sqlean.py` · installs (wheel) · licence: zlib/libpng · rank 5134 · last release 2025-10-25 · [PyPI](https://pypi.org/project/sqlean.py/)

<details><summary>README extract</summary>

This package provides an SQLite Python wrapper bundled with sqlean extensions. It's a drop-in replacement for the standard library's sqlite3 module.

Example:
```python
import sqlean as sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.execute("select 'sql is awesome'")
print(cur.fetchone())
conn.close()
```

Sections: sqlean.py, Extensions, Usage, Building from source

</details>

### pybloom-live

Bloom filter: A Probabilistic data structure

`pip install pybloom-live` · installs from source (sdist only) · licence: MIT License · rank 7194 · last release 2022-10-15 · [PyPI](https://pypi.org/project/pybloom-live/)

<details><summary>README extract</summary>

This bloom filter is forked from pybloom, and its tightening ratio is changed to 0.9, and this ration is consistently used. Choosing r around 0.8 - 0.9 will result in better average space usage for wide range of growth, therefore the default value of model is set to LARGE_SET_GROWTH. ...

</details>

### collate-data-diff

Command-line tool and Python library to efficiently diff rows across two different databases.

`pip install collate-data-diff` · installs (wheel) · licence: MIT License · rank 7862 · last release 2026-10-06 · [PyPI](https://pypi.org/project/collate-data-diff/) · [source](https://github.com/datafold/data-diff)

<details><summary>README extract</summary>

Forked from the archived repository datafold/data-diff

To publish a new version of the package, follow these steps:

1. Bump the version number in the `pyproject.toml` file.
2. Trigger the publish action.

To publish to Test PyPI, set the "test" input to "true" when triggering the action. ...

</details>

### sqlcipher3-binary

DB-API 2.0 interface for SQLCipher 3.x

`pip install sqlcipher3-binary` · installs (wheel) · licence: MIT License · rank 8358 · last release 2025-12-31 · [PyPI](https://pypi.org/project/sqlcipher3-binary/)

### pymongo_inmemory

A mongo mocking library with an ephemeral MongoDB running in memory.

`pip install pymongo_inmemory` · installs (wheel) · licence: MIT License · rank 9037 · last release 2025-03-13 · [PyPI](https://pypi.org/project/pymongo_inmemory/) · [source](https://github.com/kaizendorks/pymongo_inmemory)

<details><summary>README extract</summary>

[PyPI ] [GitHub ] [BETA Docs]

A mongo mocking library with an ephemeral MongoDB running in memory.

Example:
```python
from pymongo_inmemory import MongoClient

client = MongoClient()  # No need to provide host
db = client['testdb']
collection = db['test-collection']
# etc., etc.
client.close()

# Also usable with context manager
with MongoClient() as client:
    # do stuff
```

Sections: pymongo_inmemory, What's new?, v0.5.0, v0.4.0, v0.3.1, Usage, Configure, Import and use, Configuration, Available MongoDB versions, How do we determine which MongoDB to download?, Operating System detection, Deciding MongoDB version, Adding a new MongoDB version

</details>

### jina

Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.

`pip install jina` · installs from source (sdist only) · licence: Apache Software License · rank 9083 · last release 2025-03-24 · [PyPI](https://pypi.org/project/jina/) · [docs](https://jina.ai/serve) · [source](https://github.com/jina-ai/jina/)

<details><summary>README extract</summary>

Jina-serve is a framework for building and deploying AI services that communicate via gRPC, HTTP and WebSockets. Scale your services from local development to production while focusing on your core logic.

Features:
- Native support for all major ML frameworks and data types
- High-performance service design with scaling, streaming, and dynamic batching
- LLM serving with streaming output
- Built-in Docker integration and Executor Hub ...

Example:
```python
from jina import Executor, requests
from docarray import DocList, BaseDoc
from transformers import pipeline

class Prompt(BaseDoc):
    text: str

class Generation(BaseDoc):
    prompt: str
    text: str

class StableLM(Executor):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.generator = pipeline(
...
```

...

</details>

### sqlcipher3-wheels

DB-API 2.0 interface for SQLCipher 3.x

`pip install sqlcipher3-wheels` · installs (wheel) · licence: zlib/libpng · rank 10101 · last release 2026-01-07 · [PyPI](https://pypi.org/project/sqlcipher3-wheels/)

<details><summary>README extract</summary>

*NOTICE*: This is a fork of sqlcipher3
which adds github action for creating wheels for Windows, MacOS and Linux.
The unofficial wheels from this fork are uploaded to `sqlcipher3-wheels` on pypi,
while the official wheels are `sqlcipher3-binary`.
To install openssl easily, conan is used. ...

Example:
```python
from sqlcipher3 import dbapi2 as sqlite
conn = sqlite.connect('test.db')
c = conn.cursor()
c.execute("PRAGMA key='password'")
c.execute("PRAGMA cipher_compatibility = 3")
c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
...
```

</details>

### arize-phoenix-sqlean

sqlite3 with extensions

`pip install arize-phoenix-sqlean` · installs (wheel) · licence: Zlib AND MIT AND BSD-2-Clause AND BSD-3-Clause AND PSF-2.0 · rank 10330 · last release 2026-10-19 · [PyPI](https://pypi.org/project/arize-phoenix-sqlean/)

<details><summary>README extract</summary>

This package provides an SQLite Python wrapper bundled with sqlean extensions. It's a drop-in replacement for the standard library's sqlite3 module.

> [!NOTE]
> This is a modified fork of nalgeon/sqlean.py,
> which was archived upstream in February 2026. ...

Example:
```python
import sqlean as sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.execute("select 'sql is awesome'")
print(cur.fetchone())
conn.close()
```

Sections: arize-phoenix-sqlean, Extensions, Usage, Building from source

</details>

### docarray

The data structure for multimodal data

`pip install docarray` · installs (wheel) · licence: Apache Software License; Other/Proprietary License · rank 12012 · last release 2025-03-21 · [PyPI](https://pypi.org/project/docarray/) · [docs](https://docs.docarray.org) · [source](https://github.com/docarray/docarray)

<details><summary>README extract</summary>

The data structure for multimodal data

> Note
> The README you're currently viewing is for DocArray>0.30, which introduces some significant changes from DocArray 0.21. If you wish to continue using the older DocArray <=0.21, ensure you install it via `pip install docarray==0.21`. ...

Example:
```python
from docarray import BaseDoc
from docarray.typing import TorchTensor, ImageUrl
import torch

# Define your data model
class MyDocument(BaseDoc):
    description: str
    image_url: ImageUrl  # could also be VideoUrl, AudioUrl, etc.
    image_tensor: TorchTensor[1704, 2272, 3]  # you can express tensor shapes!

...
```

...

</details>

### voyager

Easy-to-use, fast, simple multi-platform approximate nearest-neighbor search library.

`pip install voyager` · installs (wheel) · licence: Apache Software License · rank 12391 · last release 2026-11-02 · [PyPI](https://pypi.org/project/voyager/)

<details><summary>README extract</summary>

<!-- -->
<!-- -->
<!-- -->
<!-- -->

_Voyager_ is a library for performing fast approximate nearest-neighbor searches on an in-memory collection of vectors.

Voyager features bindings to both Python and Java, with feature parity and index compatibility between both languages. ...

Sections: Python, Java, Scala, Compatibility

</details>

### sqeleton

Python library for querying SQL databases

`pip install sqeleton` · installs (wheel) · licence: MIT License · rank 12864 · last release 2025-01-14 · [PyPI](https://pypi.org/project/sqeleton/) · [docs](https://sqeleton.readthedocs.io/en/latest/) · [source](https://github.com/erezsh/sqeleton)

<details><summary>README extract</summary>

Sqeleton is a Python library for querying SQL databases.

It consists of -

- A fast and concise query builder, designed from scratch, but inspired by PyPika and SQLAlchemy

- A modular database interface, with drivers for a long list of SQL databases (see below) ...

Features:
🏃‍♂️ High-performance: Sqeleton's API is designed to maximize performance using batch operations

- No ORM. Sqeleton takes the position that while ORMs feel easy and familiar, their granular operations are far too slow. ...

Example:
```python
from sqeleton import connect, table, this

# Create a new database connection
ddb = connect("duckdb://:memory:")

# Define a table with one int column
tbl = table('my_list', schema={'item': int})

# Make a bunch of queries
queries = [
    # Create table 'my_list'
...

</details>

### pysqlsync

Synchronize schema and large volumes of data

`pip install pysqlsync` · installs (wheel) · licence: MIT · rank 13513 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pysqlsync/) · [source](https://github.com/hunyadi/pysqlsync)

<details><summary>README extract</summary>

*pysqlsync* helps you synchronize your target database or data warehouse with a data source, making efficient use of Python language elements and database drivers (client libraries). ...

Example:
```python
class WorkflowState(enum.Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"

@dataclasses.dataclass
class UserTable:
    id: PrimaryKey[int]
    updated_at: datetime
    workflow_state: WorkflowState
    uuid: uuid.UUID
    name: str
    short_name: Annotated[str, MaxLength(255)]
    homepage_url: str | None = None
```

Sections: Use cases, Quick start, Structure and data synchronization, Formation, Enumerations, Data-classes, Lists, Modules, Python classes for database objects, Dialects

</details>

### cachekit

Backend-agnostic caching for Python — intent-based decorators with circuit breaker, distributed locking, Prometheus metrics, and optional zero-knowledge AES-256-GCM encryption, on a Rust-powered core. Zero-config L1 in-memory; scales to Redis, Memcached, File, or CachekitIO.

`pip install cachekit` · installs (wheel) · licence: MIT License · rank 14656 · last release 2026-10-30 · [PyPI](https://pypi.org/project/cachekit/) · [docs](https://github.com/cachekit-io/cachekit-py#readme) · [source](https://github.com/cachekit-io/cachekit-py.git)

<details><summary>README extract</summary>

> Python caching, batteries included

Backend-agnostic caching with intent-based decorators — circuit breaker, distributed locking, Prometheus metrics, and optional zero-knowledge encryption on a Rust-powered core. Zero config to start, any backend when you scale.

[][pypi-url]
[][pypi-url]
[][codecov-url]
[][license-url] ...

Features:
Simple to use, works out of the box.

That's it. You get:

| Feature | Description |

| Circuit breaker | Prevents cascading failures |
| Distributed locking | Multi-pod safety |
| Prometheus metrics | Built-in observability |
| MessagePack ...

Example:
```python
from cachekit import cache

@cache
def expensive_function():
    return fetch_data()
```

...

</details>

## Also in this topic

- [duckdb](database.md#duckdb) - DuckDB in-process database
- [pymssql](database.md#pymssql) - DB-API interface to Microsoft SQL Server for Python. (new Cython-based version)
- [sqlmodel](database.md#sqlmodel) - SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
- [mysqlclient](database.md#mysqlclient) - Python interface to MySQL
- [tinydb](database.md#tinydb) - TinyDB is a tiny, document oriented database optimized for your happiness :)
- [lmdb](database.md#lmdb) - Universal Python binding for the LMDB 'Lightning' Database
- [vertica-python](database.md#vertica-python) - Official native Python client for the Vertica database.
- [gdbmongo](database.md#gdbmongo) - GDB pretty printers and commands for debugging the MongoDB Server
- [advanced-alchemy](database.md#advanced-alchemy) - Ready-to-go SQLAlchemy concoctions.
- [sqlcipher3](database.md#sqlcipher3) - DB-API 2.0 interface for SQLCipher 4.x
- [plyvel](database.md#plyvel) - Plyvel, a fast and feature-rich Python interface to LevelDB
- [pgsanity](database.md#pgsanity) - Check syntax of sql for PostgreSQL
- [pymonetdb](database.md#pymonetdb) - Native MonetDB client Python API
- [py2neo-history](database.md#py2neo-history) - Python client library and toolkit for Neo4j
- [duckdb-cli](database.md#duckdb-cli) - The DuckDB CLI
- [sqlalchemy-views](database.md#sqlalchemy-views) - Adds CreateView and DropView constructs to SQLAlchemy
- [arcticdb](database.md#arcticdb) - ArcticDB DataFrame Database
- [pymongosql](database.md#pymongosql) - Python DB API 2.0 (PEP 249) client for MongoDB
- [surrealdb](database.md#surrealdb) - SurrealDB python client
- [sqlalchemy-monetdb](database.md#sqlalchemy-monetdb) - SQLAlchemy dialect for MonetDB
- [MySQL-python](database.md#mysql-python) - Python interface to MySQL
- [py2neo](database.md#py2neo) - Python client library and toolkit for Neo4j
- [sqlalchemy-file](database.md#sqlalchemy-file) - SQLAlchemy-file is a SQLAlchemy extension for attaching files to SQLAlchemy model and uploading them to various storage.
- [dbt-vertica](database.md#dbt-vertica) - Official vertica adapter plugin for dbt (data build tool)
- [pyturso](database.md#pyturso) - Turso is an in-process SQL database written in Rust, compatible with SQLite.
