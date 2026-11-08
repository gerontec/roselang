# Database / Front-Ends

[Index](README.md) · 54 packages in this topic, 40 more listed under another topic, by downloads.

### SQLAlchemy

Database Abstraction Library

`pip install SQLAlchemy` · installs (wheel) · licence: MIT · rank 86 · last release 2026-11-04 · [PyPI](https://pypi.org/project/SQLAlchemy/) · [docs](https://docs.sqlalchemy.org) · [source](https://github.com/sqlalchemy/sqlalchemy)

<details><summary>README extract</summary>

The Python SQL Toolkit and Object Relational Mapper

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper
that gives application developers the full power and
flexibility of SQL. ...

Sections: SQLAlchemy, Introduction, Documentation

</details>

### alembic

A database migration tool for SQLAlchemy.

`pip install alembic` · installs (wheel) · licence: MIT · rank 150 · last release 2026-10-22 · [PyPI](https://pypi.org/project/alembic/) · [docs](https://alembic.sqlalchemy.org/en/latest/) · [source](https://github.com/sqlalchemy/alembic/)

<details><summary>README extract</summary>

Alembic is a database migrations tool written by the author
of SQLAlchemy. A migrations tool
offers the following functionality:

* Can emit ALTER statements to a database in order to change
 the structure of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed;
 each script indicates a particular series ...

</details>

### asyncpg

An asyncio PostgreSQL driver

`pip install asyncpg` · installs (wheel) · licence: Apache-2.0 · rank 240 · last release 2026-10-06 · [PyPI](https://pypi.org/project/asyncpg/) · [source](https://github.com/MagicStack/asyncpg)

<details><summary>README extract</summary>

asyncpg is a database interface library designed specifically for
PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation
of PostgreSQL server binary protocol for use with Python's `asyncio`
framework. You can read more about asyncpg in an introductory
blog post. ...

Features:
asyncpg implements PostgreSQL server protocol natively and exposes its
features directly, as opposed to hiding them behind a generic facade
like DB-API.

This enables asyncpg to have easy-to-use support for: ...

Example:
```python
import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='user', password='password',
                                 database='database', host='127.0.0.1')
    values = await conn.fetch(
        'SELECT * FROM mytable WHERE id = $1',
...

</details>

### smart-open

Utils for streaming large files (S3, HDFS, GCS, SFTP, Azure Blob Storage, gzip, bz2, zst...)

`pip install smart-open` · installs (wheel) · licence: MIT License · rank 399 · last release 2026-11-03 · [PyPI](https://pypi.org/project/smart-open/) · [source](https://github.com/piskvorky/smart_open)

<details><summary>README extract</summary>

`smart_open` is a Python 3 library for efficient streaming of very large files from/to storages such as S3, GCS, Azure Blob Storage, HDFS, WebHDFS, HTTP, HTTPS, SFTP, or local filesystem. It supports transparent, on-the-fly (de-)compression for a variety of different formats. ...

Features:
Working with large remote files, for example using Amazon's boto3 Python library, is a pain.
`boto3`'s `Object.upload_fileobj()` and `Object.download_fileobj()` methods require gotcha-prone boilerplate to use successfully, such as constructing ...

Example:
```python
import os, boto3, botocore
from smart_open import open

# stream content *into* S3 (write mode) using a custom client
# this client is thread-safe ref
config = botocore.client.Config(
    max_pool_connections=64,
    tcp_keepalive=True,
...

</details>

### pg8000

PostgreSQL interface library

`pip install pg8000` · installs (wheel) · licence: BSD License · rank 471 · last release 2026-10-26 · [PyPI](https://pypi.org/project/pg8000/)

<details><summary>README extract</summary>

pg8000 is a pure-Python
PostgreSQL driver that complies with
DB-API 2.0. pg8000's name comes from the
belief that it is probably about the 8000th PostgreSQL interface for Python. pg8000 is
distributed under the BSD 3-clause license.

<!-- mtoc-start -->

- Installation ...

Example:
```python
>>> import pg8000.native
>>>
>>> # Connect to the database with user name postgres
>>>
>>> con = pg8000.native.Connection("postgres", password="cpsnow")
>>>
>>> # Create a temporary table
>>>
>>> con.run("CREATE TEMPORARY TABLE book (id SERIAL, title TEXT)")
>>>
>>> # Populate the table
>>>
>>> for title in ("Ender's Game", "The Magus"):
...
```

...

</details>

### redshift-connector

Redshift interface library

`pip install redshift-connector` · installs (wheel) · licence: BSD License · rank 475 · last release 2026-10-08 · [PyPI](https://pypi.org/project/redshift-connector/)

<details><summary>README extract</summary>

`redshift_connector` is the Amazon Redshift connector for
Python. Easy integration with pandas and numpy, as well as support for numerous Amazon Redshift specific features help you get the most out of your data

Supported Amazon Redshift features include:

- IAM authentication
- Identity provider (IdP) authentication ...

Example:
```python
import redshift_connector

# Connects to Redshift cluster using AWS credentials
conn = redshift_connector.connect(
    host='examplecluster.abc123xyz789.us-west-1.redshift.amazonaws.com',
    database='dev',
    user='awsuser',
    password='my_password'
 )

cursor: redshift_connector.Cursor = conn.cursor()
...
```

...

</details>

### db-dtypes

Pandas Data Types for SQL systems (BigQuery, Spanner)

`pip install db-dtypes` · installs (wheel) · licence: Apache Software License · rank 637 · last release 2026-10-23 · [PyPI](https://pypi.org/project/db-dtypes/)

<details><summary>README extract</summary>

Pandas extension data types for data from SQL systems such as BigQuery.

- Library Documentation

Sections: Pandas Data Types for SQL systems (BigQuery, Spanner), Mac/Linux, Windows

</details>

### streamlit

A faster way to build and share data apps

`pip install streamlit` · installs (wheel) · licence: Apache-2.0 · rank 759 · last release 2026-11-05 · [PyPI](https://pypi.org/project/streamlit/) · [docs](https://docs.streamlit.io/) · [source](https://github.com/streamlit/streamlit)

<details><summary>README extract</summary>

A faster way to build and share data apps.

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you’ve created an app, you can use our Community Cloud platform to deploy, manage, and share your app.

Features:
- Simple and Pythonic: Write beautiful, easy-to-read code.
- Fast, interactive prototyping: Let others interact with your data and provide feedback quickly.
- Live editing: See your app update instantly as you edit your script. ...

Example:
```python
import streamlit as st

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

...

</details>

### trino

Client for the Trino distributed SQL Engine

`pip install trino` · installs (wheel) · licence: Apache Software License · rank 967 · last release 2026-09-23 · [PyPI](https://pypi.org/project/trino/)

<details><summary>README extract</summary>

Client for Trino, a distributed SQL engine for interactive and batch big data processing.
Provides a low-level client and a DBAPI 2.0 implementation and a SQLAlchemy adapter.
It supports Python>=3.9 and PyPy.

Example:
```python
from trino.dbapi import connect

conn = connect(
    host="<host>",
    port=<port>,
    user="<username>",
    catalog="<catalog>",
    schema="<schema>",
)
cur = conn.cursor()
cur.execute("SELECT * FROM system.runtime.nodes")
rows = cur.fetchall()
```

Sections: Trino Python client, Usage, The Python Database API (DBAPI), SQLAlchemy, Authentication mechanisms, Basic authentication, JWT authentication, OAuth2 authentication, Certificate authentication, Kerberos authentication, GSSAPI authentication, User impersonation, Extra credentials, Roles

</details>

### sqlalchemy-bigquery

SQLAlchemy dialect for BigQuery

`pip install sqlalchemy-bigquery` · installs (wheel) · licence: MIT License · rank 1239 · last release 2026-10-02 · [PyPI](https://pypi.org/project/sqlalchemy-bigquery/)

<details><summary>README extract</summary>

SQLALchemy Dialects

- Dialect Documentation
- Product Documentation

Example:
```python
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
engine = create_engine('bigquery://project')
table = Table('dataset.table', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=table().scalar()))
```

Sections: SQLAlchemy Dialect for BigQuery, Quick Start, Mac/Linux, Windows, Usage, SQLAlchemy, Project, Authentication, Location, Table names, Batch size, Page size for dataset.list_tables, Adding a Default Dataset, Connection String Parameters

</details>

### dash

A Python framework for building reactive web-apps. Developed by Plotly.

`pip install dash` · installs (wheel) · licence: MIT License · rank 1434 · last release 2026-10-29 · [PyPI](https://pypi.org/project/dash/) · [docs](https://dash.plotly.com) · [source](https://github.com/plotly/dash)

<details><summary>README extract</summary>

Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical Python code. Read our tutorial (proudly crafted ❤️ with Dash itself).

- Docs: Create your first Dash app in under 5 minutes

- dash.gallery: Dash app gallery with Python & R code

Sections: Dash, Dash App Examples, Dash OSS & Dash Enterprise

</details>

### PyHive

Python interface to Hive

`pip install PyHive` · installs from source (sdist only) · licence: Apache Software License · rank 1682 · last release 2023-08-17 · [PyPI](https://pypi.org/project/PyHive/)

<details><summary>README extract</summary>

Example:
```python
from pyhive import presto  # or import hive or import trino
cursor = presto.connect('localhost').cursor()  # or use hive.connect or use trino.connect
cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
print cursor.fetchone()
print cursor.fetchall()
```

Sections: PyHive, Usage, DB-API, DB-API (asynchronous), SQLAlchemy, Passing session configuration, Requirements, Tips for test environment setup, Updating TCLIService

</details>

### teradatasql

Teradata SQL Driver for Python

`pip install teradatasql` · installs (wheel) · licence: Other/Proprietary License · rank 1835 · last release 2026-11-06 · [PyPI](https://pypi.org/project/teradatasql/)

<details><summary>README extract</summary>

This package enables Python applications to connect to the Teradata Database.

This package implements the PEP-249 Python Database API Specification 2.0.

This package requires 64-bit Python 3.7 or later and runs on the following operating systems and processor architectures. 32-bit Python is not supported. ...

Sections: Teradata SQL Driver for Python, Documentation

</details>

### ibis-framework

The portable Python dataframe library

`pip install ibis-framework` · installs (wheel) · licence: Apache Software License · rank 2261 · last release 2026-02-07 · [PyPI](https://pypi.org/project/ibis-framework/) · [docs](https://ibis-project.org) · [source](https://github.com/ibis-project/ibis)

<details><summary>README extract</summary>

Ibis is the portable Python dataframe library:

- Fast local dataframes (via DuckDB by default)
- Lazy dataframe expressions
- Interactive mode for iterative data exploration
- Compose Python dataframe and SQL code
- Use the same dataframe API for more than 20 backends
- Iterate locally and deploy remotely by changing a single line of code ...

Example:
```python
>>> import ibis
>>> ibis.options.interactive = True
>>> t = ibis.examples.penguins.fetch()
>>> t
┏━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃ species ┃ island    ┃ bill_length_mm ┃ bill_depth_mm ┃ flipper_length_mm ┃ body_mass_g ┃ sex    ┃ year  ┃
...
```

...

</details>

### ibm-db

Python DBI driver for DB2 (LUW, zOS, i5)

`pip install ibm-db` · installs (wheel) · licence: Apache Software License · rank 2488 · last release 2026-08-11 · [PyPI](https://pypi.org/project/ibm-db/)

<details><summary>README extract</summary>

Example:
```python
$ python
Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ibm_db
>>> #For connecting to local database named pydev for user db2inst1 and password secret, use below example
...
```

Sections: Components, API Documentation, Pre-requisites, For MacOS M1/M2/ Apple Silicon chip system, Linux/Unix, Windows, Docker Linux containers, Quick Example, Logging, Logging in ibm_db Module, Logging in ibm_db_dbi Module, Example of SSL Connection String, SQL0805N Error - Rebind packages, For z/OS and iSeries Connectivity and SQL1598N error

</details>

### apsw

Another Python SQLite Wrapper

`pip install apsw` · installs (wheel) · licence: any-OSI · rank 2859 · last release 2026-10-19 · [PyPI](https://pypi.org/project/apsw/) · [docs](https://rogerbinns.github.io/apsw/) · [source](https://github.com/rogerbinns/apsw)

<details><summary>README extract</summary>

APSW stands for A\ nother P\ ython S\ QLite W\ rapper. APSW
supports CPython 3.11 onwards.

APSW lets you get the most out of the SQLite
embedded relational database engine from Python, and the most out of
Python from SQLite. APSW glues together the complete SQLite C API and Python's C API, staying up to date
with both SQLite and Python. ...

Sections: About, Help/Documentation, Mailing lists/contacts, Bugs

</details>

### PubChemPy

A simple Python wrapper around the PubChem PUG REST API.

`pip install PubChemPy` · installs (wheel) · licence: MIT · rank 2888 · last release 2025-09-08 · [PyPI](https://pypi.org/project/PubChemPy/) · [docs](https://docs.pubchempy.org) · [source](https://github.com/mcs07/PubChemPy)

<details><summary>README extract</summary>

PubChemPy provides a way to interact with PubChem in Python. It allows chemical searches by name, substructure and similarity, chemical standardization, conversion between chemical file formats, depiction and retrieval of chemical properties.

Example:
```python
>>> import pubchempy as pcp
>>> comp = pcp.Compound.from_cid(1423)
>>> print(comp.smiles)
CCCCCCCNC1CCCC1CCCCCCC(=O)O
>>> print(comp.iupac_name)
7-[2-(heptylamino)cyclopentyl]heptanoic acid
```

Sections: PubChemPy, Example usage, Documentation

</details>

### presto-python-client

Client for the Presto distributed SQL Engine

`pip install presto-python-client` · installs (wheel) · licence: Apache Software License · rank 3232 · last release 2023-09-07 · [PyPI](https://pypi.org/project/presto-python-client/)

<details><summary>README extract</summary>

Client for Presto ( a distributed SQL engine for
interactive and batch big data processing. Provides a low-level client and
a DBAPI 2.0 implementation.

</details>

### sqlitedict

Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe.

`pip install sqlitedict` · installs from source (sdist only) · licence: Apache Software License · rank 3489 · last release 2022-12-03 · [PyPI](https://pypi.org/project/sqlitedict/)

<details><summary>README extract</summary>

A lightweight wrapper around Python's sqlite3 database with a simple, Pythonic
dict-like interface and support for multi-thread access:

Features:
* Values can be any picklable objects (uses `pickle` with the highest protocol).
* Support for multiple tables (=dicts) living in the same database file.
* Support for access from multiple threads to the same connection (needed by e.g. Pyro). ...

Example:
```python
>>> from sqlitedict import SqliteDict
>>> db = SqliteDict("example.sqlite")
>>>
>>> db["1"] = {"name": "first item"}
>>> db["2"] = {"name": "second item"}
>>> db["3"] = {"name": "yet another item"}
>>>
>>> # Commit to save the objects.
>>> db.commit()
>>>
>>> db["4"] = {"name": "yet another item"}
...
```

...

</details>

### teradatasqlalchemy

Teradata SQL Driver Dialect for SQLAlchemy

`pip install teradatasqlalchemy` · installs (wheel) · licence: Other/Proprietary License · rank 3864 · last release 2025-12-16 · [PyPI](https://pypi.org/project/teradatasqlalchemy/)

<details><summary>README extract</summary>

This package enables SQLAlchemy to connect to the Teradata Database.

This package requires 64-bit Python 3.4 or later, and runs on Windows, macOS, and Linux. 32-bit Python is not supported.

For community support, please visit the Teradata Community forums.

For Teradata customer support, please visit Teradata Access.

Copyright 2025 Teradata. ...

Sections: Teradata SQL Driver Dialect for SQLAlchemy, teradatasqlalchemy 20.0.0.9, teradatasqlalchemy 20.0.0.8, teradatasqlalchemy 20.0.0.7, teradatasqlalchemy 20.0.0.6, teradatasqlalchemy 20.0.0.5, teradatasqlalchemy 20.0.0.4, teradatasqlalchemy 20.0.0.3, teradatasqlalchemy 20.0.0.2, teradatasqlalchemy 20.0.0.1, teradatasqlalchemy 20.0.0.0, teradatasqlalchemy 17.20.0.0, teradatasqlalchemy 17.0.0.5, teradatasqlalchemy 17.0.0.4

</details>

### graphframes-py

GraphFrames: Graph Processing Framework for Apache Spark

`pip install graphframes-py` · installs (wheel) · licence: Apache Software License · rank 4088 · last release 2026-10-05 · [PyPI](https://pypi.org/project/graphframes-py/)

<details><summary>README extract</summary>

The is the officila graphframes-py PyPI package, which is a Python wrapper for the Scala GraphFrames library.
This package is maintained by the GraphFrames project and is available on PyPI.

- Installation
- Creating Graphs
- Basic Graph Manipulations
- Centrality Metrics
- Motif finding
- Traversals and Connectivity
- Community Detection ...

Sections: GraphFrames Python Package, Documentation, Tutorials, Spark-Connect Note

</details>

### weave

A toolkit for building composable interactive data driven applications.

`pip install weave` · installs (wheel) · licence: Apache Software License · rank 4697 · last release 2026-11-05 · [PyPI](https://pypi.org/project/weave/) · [docs](https://docs.wandb.ai) · [source](https://github.com/wandb/weave)

<details><summary>README extract</summary>

Weave is a toolkit for tracing and evaluating AI agents, built by Weights & Biases.

You can use Weave to:

- Trace agents. Conversations, turns, LLM calls, and tool calls show up in the Agents tab.
- Evaluate agents and LLM applications.
- Trace functions with `@weave.op` when you want the Calls tab, not the Agents tab. ...

Example:
```python
import asyncio
import requests
import weave
from agents import Agent, Runner, function_tool

weave.init("<your-team>/<your-project-name>")

@function_tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for a topic and return its title and intro paragraph."""
    r = requests.get(
        "
        params={
...
```

...

</details>

### pottery

Redis for Humans.

`pip install pottery` · installs (wheel) · licence: not stated · rank 4840 · last release 2025-03-21 · [PyPI](https://pypi.org/project/pottery/)

<details><summary>README extract</summary>

Redis is awesome, but Redis
commands are not always intuitive. Pottery is a
Pythonic way to access Redis. If you know how to use Python dicts, then you
already know how to use Pottery. Pottery is useful for accessing Redis more
easily, and also for implementing microservice resilience patterns; and it has
been battle tested in production at scale.

Example:
```python
>>> from redis import Redis
>>> redis = Redis.from_url('redis://localhost:6379/1')
>>>
```

Sections: Pottery: Redis for Humans 🌎🌍🌏, Usage, Dicts 📖, Sets 🛍️, Lists ⛓, Counters 🧮, Deques 🖇️, Queues 🚶‍♂️🚶‍♀️🚶‍♂️, Redlock 🔒, synchronize() 👯‍♀️, AIORedlock 🔒, NextID 🔢, redis_cache(), CachedOrderedDict

</details>

### sqlalchemy-drill

Apache Drill for SQLAlchemy

`pip install sqlalchemy-drill` · installs (wheel) · licence: MIT License · rank 5021 · last release 2026-02-05 · [PyPI](https://pypi.org/project/sqlalchemy-drill/)

<details><summary>README extract</summary>

The primary purpose of this is to have a working dialect for Apache Drill that can be used with Apache Superset.

Obviously, a working, robust dialect for Drill serves other purposes as well, but most of the iterative planning for this REPO will be based on working with Superset. ...

Example:
```python
jpype.startJVM("-ea", classpath="lib/*")
```

Sections: Apache Drill dialect for SQLAlchemy., Usage with REST, Trailing metadata, Drill < 1.19, Drill >= 1.19, Usage with JDBC, Usage with ODBC, Usage with Superset, Many thanks, Docker

</details>

### starrocks

Python SQLAlchemy Dialect for StarRocks with optional Alembic integration

`pip install starrocks` · installs (wheel) · licence: Apache-2.0 · rank 5313 · last release 2026-08-01 · [PyPI](https://pypi.org/project/starrocks/) · [docs](https://docs.starrocks.io) · [source](https://github.com/starrocks/starrocks.git)

<details><summary>README extract</summary>

A StarRocks client for the Python programming language, including a SQLAlchemy dialect and an Alembic extension.

StarRocks is a next-generation data platform designed for fast,real-time analytics. ...

Example:
```python
from sqlalchemy import create_engine, text

engine = create_engine('starrocks://root@localhost:9030/mydatabase')

# make sure you have created the table `mytable` in `mydatabase`.

with engine.connect() as connection:
    print("Connection successful!")
    rows = connection.execute(text("SELECT * FROM mytable LIMIT 2")).fetchall()
    print(rows)
...
```

...

</details>

### dash-cytoscape

A Component Library for Dash aimed at facilitating network visualization in Python, wrapped around Cytoscape.js

`pip install dash-cytoscape` · installs from source (sdist only) · licence: MIT License · rank 5397 · last release 2024-07-15 · [PyPI](https://pypi.org/project/dash-cytoscape/)

<details><summary>README extract</summary>

A Dash component library for creating interactive and customizable networks in Python, wrapped around Cytoscape.js.

- 🌟 Medium Article
- 📣 Community Announcement
- 💻 Github Repository
- 📚 User Guide
- 🗺 Component Reference
- 📺 Webinar Recording

Example:
```python
import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(name)
app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 50, 'y': 50}},
...
```

...

</details>

### maggma

Framework to develop datapipelines from files on disk to full dissemenation API

`pip install maggma` · installs (wheel) · licence: not stated · rank 5447 · last release 2026-10-27 · [PyPI](https://pypi.org/project/maggma/) · [docs](https://materialsproject.github.io/maggma/)

<details><summary>README extract</summary>

Maggma is a framework to build scientific data processing pipelines from data stored in
a variety of formats -- databases, Azure Blobs, files on disk, etc., all the way to a
REST API. The rest of this README contains a brief, high-level overview of what `maggma` can do.
For more, please refer to the documentation.

Example:
```python
>>> turtles = [{"name": "Leonardo", "color": "blue", "tool": "sword"},
               {"name": "Donatello","color": "purple", "tool": "staff"},
               {"name": "Michelangelo", "color": "orange", "tool": "nunchuks"},
               {"name":"Raphael", "color": "red", "tool": "sai"}
            ]
>>> store = MongoStore(database="my_db_name",
...
```

Sections: What is Maggma, Basic Concepts, Store, Builder

</details>

### jobflow

jobflow is a library for writing computational workflows

`pip install jobflow` · installs (wheel) · licence: modified BSD · rank 5539 · last release 2026-10-19 · [PyPI](https://pypi.org/project/jobflow/) · [docs](https://materialsproject.github.io/jobflow/) · [source](https://github.com/materialsproject/jobflow)

<details><summary>README extract</summary>

Documentation | PyPI | GitHub | Paper

Jobflow is a free, open-source library for writing and executing workflows. Complex
workflows can be defined using simple python functions and executed locally or on
arbitrary computing resources using the jobflow-remote or FireWorks
workflow managers. ...

Example:
```python
from jobflow import job, Flow

@job
def add(a, b):
    return a + b

add_first = add(1, 5)
add_second = add(add_first.output, 5)

flow = Flow([add_first, add_second])
flow.draw_graph().show()
```

Sections: Is jobflow for me, Workflow model, Quickstart and tutorials, Need help?, What’s new?

</details>

### sqlalchemy-pytds

A Microsoft SQL Server TDS connector for SQLAlchemy.

`pip install sqlalchemy-pytds` · installs (wheel) · licence: MIT · rank 6085 · last release 2026-10-20 · [PyPI](https://pypi.org/project/sqlalchemy-pytds/)

<details><summary>README extract</summary>

A Microsoft SQL Server TDS connector for SQLAlchemy.

</details>

### postgres

postgres is a high-value abstraction over psycopg2.

`pip install postgres` · installs (wheel) · licence: MIT License · rank 6218 · last release 2021-09-20 · [PyPI](https://pypi.org/project/postgres/)

<details><summary>README extract</summary>

postgres is a high-value abstraction over psycopg2

Read the Docs

</details>

### piccolo-admin

A powerful and modern admin interface / CMS, powered by Piccolo and ASGI.

`pip install piccolo-admin` · installs (wheel) · licence: MIT License · rank 6301 · last release 2026-06-19 · [PyPI](https://pypi.org/project/piccolo-admin/)

<details><summary>README extract</summary>

Piccolo Admin is a powerful admin interface / content management system for Python, built on top of Piccolo.

It was created at a design agency to serve the needs of customers who demand a high quality, beautiful admin interface for their websites. It's a modern alternative to tools like Wordpress and Django Admin. ...

Example:
```python
import uvicorn
from movies.endpoints import HomeEndpoint
from movies.tables import Director, Movie
from starlette.routing import Mount, Route, Router

from piccolo_admin.endpoints import create_admin

# The `allowed_hosts` argument is required when running under HTTPS. It's
# used for additional CSRF defence.
...
```

Sections: Piccolo Admin, Try it, Local Demo, ASGI, Full docs

</details>

### tika

Apache Tika Python library

`pip install tika` · installs (wheel) · licence: Apache-2.0 · rank 6344 · last release 2026-08-01 · [PyPI](https://pypi.org/project/tika/) · [docs](https://chrismattmann.github.io/tika-python) · [source](http://github.com/chrismattmann/tika-python.git)

<details><summary>README extract</summary>

A Python port of the Apache Tika
library that makes Tika available using the
Tika REST Server.

This makes Apache Tika available as a Python library,
installable via Setuptools, Pip and Easy Install.

To use this library, you need to have Java 11+ installed on your
system as tika-python starts up the Tika REST server in the
background. ...

Sections: tika-python, New Command Line Client Tool, Questions, comments?, Thanks

</details>

### ibm-db-sa

SQLAlchemy support for IBM Data Servers

`pip install ibm-db-sa` · installs (wheel) · licence: Apache-2.0 · rank 6411 · last release 2026-03-18 · [PyPI](https://pypi.org/project/ibm-db-sa/)

<details><summary>README extract</summary>

The IBM_DB_SA adapter provides the Python/SQLAlchemy interface to IBM Data Servers.

Version

0.4.4 (2026/03/18)

Prerequisites

1. Install Python 3.8 or newer versions or Jython 2.7.x .
2. SQLAlchemy version between 0.7.3 - 2.0.x.
3. IBM_DB driver and IBM_DB_DBI wrapper 1.0.1 or higher.

Example:
```python
from sqlalchemy import create_engine
engine = create_engine(
   "ibm_db_sa://userID:Password@host:port/database?ibmdbsa_log=C:\\Users\\Logs\\log_ibmdbsa.txt"
)
```

Sections: IBM_DB_SA, Logging in ibm_db_sa, Logging Configuration, Examples, 1. Enable Logging to a File (Current Directory), 2. Enable Logging to a File (Specific Directory), Windows example, Linux / macOS example, 3. Enable Console Logging, Using SQLAlchemy URL Object, Log to File, Log to Console, Notes, Typical Use Cases

</details>

### python-etcd

A python client for etcd

`pip install python-etcd` · installs from source (sdist only) · licence: MIT License · rank 6972 · last release 2017-03-02 · [PyPI](https://pypi.org/project/python-etcd/)

<details><summary>README extract</summary>

A python client for Etcd

Official documentation:

Example:
```python
import etcd

client = etcd.Client() # this will create a client against etcd server running on localhost on port 4001
client = etcd.Client(port=4002)
client = etcd.Client(host='127.0.0.1', port=4003)
client = etcd.Client(host=(('127.0.0.1', 4001), ('127.0.0.1', 4002), ('127.0.0.1', 4003)))
...
```

Sections: python-etcd documentation, Pre-requirements, From source, Usage, Create a client object, Write a key, Read a key, Delete a key, Atomic Compare and Swap, Watch a key, Refreshing key TTL, Locking module, Get machines in the cluster, Get leader of the cluster

</details>

### teradataml

Teradata Vantage Python package for Advanced Analytics

`pip install teradataml` · installs (wheel) · licence: Other/Proprietary License · rank 7066 · last release 2026-10-05 · [PyPI](https://pypi.org/project/teradataml/)

<details><summary>README extract</summary>

teradataml makes available to Python users a collection of analytic functions that reside on Teradata Vantage. This allows users to perform analytics on Teradata Vantage with no SQL coding. ...

Example:
```python
from teradataml import create_context

# Create two independent contexts to two different Vantage systems.
>>> ctx1 = create_context(host = 'hostname1', username = 'user1', password = 'password1')
>>> ctx2 = create_context(host = 'hostname2', username = 'user2', password = 'password2')

# Run teradataml operations using the first context
...
```

...

</details>

### pyathenajdbc

Amazon Athena JDBC driver wrapper for the Python DB API 2.0 (PEP 249)

`pip install pyathenajdbc` · installs (wheel) · licence: MIT License · rank 7482 · last release 2020-12-31 · [PyPI](https://pypi.org/project/pyathenajdbc/)

<details><summary>README extract</summary>

PyAthenaJDBC is an Amazon Athena JDBC driver wrapper for the Python DB API 2.0 (PEP 249).

* Python

 - CPython 3.6, 3.7, 3.8, 3.9

* Java

 - Java >= 8 (JDBC 4.2)

+---------------+---------------------+-------------------------------------------------------------------------------+
 JDBC driver ...

Example:
```python
from pyathenajdbc import connect

conn = connect(S3OutputLocation='s3://YOUR_S3_BUCKET/path/to/',
               AwsRegion='us-west-2')
try:
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM one_row
        """)
        print(cursor.description)
        print(cursor.fetchall())
finally:
    conn.close()
```

...

</details>

### questdb

QuestDB client library for Python

`pip install questdb` · installs (wheel) · licence: Apache-2.0 · rank 8522 · last release 2026-10-29 · [PyPI](https://pypi.org/project/questdb/) · [docs](https://py-questdb-client.readthedocs.io/en/latest/index.html) · [source](https://github.com/questdb/py-questdb-client/)

<details><summary>README extract</summary>

This is the official Python client library for QuestDB.

This client library implements the QuestDB Wire Protocol (QWP) over WebSocket
for pooled ingestion and queries — the deployment-level `questdb.connect()`
API. ...

Example:
```python
import numpy as np
import pandas as pd
import questdb

df = pd.DataFrame({
    'symbol': pd.Categorical(['ETH-USD', 'BTC-USD']),
    'side': pd.Categorical(['sell', 'sell']),
    'price': [2615.54, 39269.98],
    'amount': [0.00044, 0.001],

    # NumPy float64 arrays require QuestDB server >= 9.0.0.
    'ord_book_bids': [
...
```

Sections: QuestDB Client Library for Python, Quickstart, Links

</details>

### sqlalchemy-schemadisplay

Package for the generation of diagrams based on SQLAlchemy ORM models and or the database itself

`pip install sqlalchemy-schemadisplay` · installs (wheel) · licence: MIT License · rank 8559 · last release 2024-02-15 · [PyPI](https://pypi.org/project/sqlalchemy-schemadisplay/) · [docs](https://github.com/fschulze/sqlalchemy_schemadisplay/blob/master/README.rst) · [source](https://github.com/fschulze/sqlalchemy_schemadisplay)

<details><summary>README extract</summary>

Turn SQLAlchemy DB Model into a graph.

See SQLAlchemy wiki for the previous version of this doc.

Example:
```python
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

# create the pydot graph object by autoloading all tables via a bound metadata object
graph = create_schema_graph(metadata=MetaData('postgres://user:pwd@host/database'),
   show_datatypes=False, # The image would get nasty big if we'd show the datatypes
...
```

Sections: sqlalchemy_schemadisplay, Usage, 2.0 - 2024-02-15, 1.4 - 2024-02-15, 1.3 - 2016-01-27, 1.2 - 2014-03-02, 1.1 - 2011-10-12, 1.0 - 2011-01-07

</details>

### CouchDB

Python library for working with CouchDB

`pip install CouchDB` · installs (wheel) · licence: BSD License · rank 8572 · last release 2018-02-09 · [PyPI](https://pypi.org/project/CouchDB/)

<details><summary>README extract</summary>

This is a Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

</details>

### airium

Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.

`pip install airium` · installs (wheel) · licence: MIT · rank 8780 · last release 2026-09-20 · [PyPI](https://pypi.org/project/airium/)

<details><summary>README extract</summary>

Airium is the most natural, pure-Python HTML generator with no runtime
dependencies. It lets you describe an HTML document with ordinary Python
code, without introducing a template language or a separate template file. ...

Example:
```python
from airium import Airium

a = Airium()
with a.section(id="intro", **{"data-page": "home"}):
    a.h1(_t="Welcome")
    a("Text can also be written directly.")
```

Sections: Airium, Type checking, How it works, Generating `HTML` code in python using `airium`, Basic `HTML` page (hello world), Simple image in a div, Table, Chaining shortcut for elements with only one child, Options, Pretty or Minify, minify, indent style, indent level, line break character

</details>

### musicbrainzngs

Python bindings for the MusicBrainz NGS and the Cover Art Archive webservices

`pip install musicbrainzngs` · installs (wheel) · licence: BSD License; ISC License (ISCL) · rank 9987 · last release 2020-01-11 · [PyPI](https://pypi.org/project/musicbrainzngs/)

<details><summary>README extract</summary>

This library implements webservice bindings for the Musicbrainz NGS site, also known as /ws/2
and the Cover Art Archive.

For more information on the musicbrainz webservice see <

Example:
```python
# Import the module
import musicbrainzngs

# If you plan to submit data, authenticate
musicbrainzngs.auth("user", "password")

# Tell musicbrainz what your app is, and how to contact you
# (this step is required, as per the webservice access rules
# at  )
musicbrainzngs.set_useragent("Example music app", "0.1", "

...
```

Sections: Musicbrainz NGS bindings, Usage

</details>

### sqlalchemy-firebird

Firebird for SQLAlchemy

`pip install sqlalchemy-firebird` · installs (wheel) · licence: MIT License · rank 10369 · last release 2026-05-21 · [PyPI](https://pypi.org/project/sqlalchemy-firebird/) · [docs](https://github.com/fdcastel/sqlalchemy-firebird/wiki) · [source](https://github.com/fdcastel/sqlalchemy-firebird)

<details><summary>README extract</summary>

An external SQLAlchemy dialect for the Firebird database server.

This package targets SQLAlchemy 2.0+ and Firebird 3.0+, using the modern `firebird-driver` Python DB-API 2.0 driver.

Example:
```python
from sqlalchemy import create_engine

db_uri = "firebird+firebird://sysdba@/c:/databases/my_project.fdb?charset=UTF8&fb_client_library=c:/firebird/fbclient.dll"
engine = create_engine(db_uri, echo=True)

# Force the engine to connect, surfacing any URL or driver issues immediately.
with engine.begin():
    pass
```

Sections: sqlalchemy-firebird, Connection strings, Examples, Usage

</details>

### sqlalchemy-repr

Automatically generates pretty repr of a SQLAlchemy model.

`pip install sqlalchemy-repr` · installs from source (sdist only) · licence: not stated · rank 10425 · last release 2022-10-20 · [PyPI](https://pypi.org/project/sqlalchemy-repr/)

<details><summary>README extract</summary>

Automatically generates pretty `repr` of a SQLAlchemy model.

Example:
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

Base = declarative_base(cls=RepresentableBase)
```

Sections: sqlalchemy-repr, Usage, Example

</details>

### SQLAlchemy-Utc

SQLAlchemy type to store aware datetime values

`pip install SQLAlchemy-Utc` · installs (wheel) · licence: MIT License · rank 10453 · last release 2021-09-24 · [PyPI](https://pypi.org/project/SQLAlchemy-Utc/)

<details><summary>README extract</summary>

This package provides a drop-in replacement of SQLAlchemy's built-in DateTime
type with `timezone=True` option enabled. Although SQLAlchemy's built-in
`DateTime` type provides `timezone=True` option, since some vendors like
SQLite and MySQL don't provide `timestamptz` data type, the option doesn't
make any effect on these vendors. ...

Sections: SQLAlchemy-Utc, 0.14.0, 0.13.0, 0.12.0, 0.11.0, 0.10.0, 0.9.0

</details>

### ovs

Open vSwitch library

`pip install ovs` · installs from source (sdist only) · licence: Apache-2.0 · rank 10647 · last release 2026-08-17 · [PyPI](https://pypi.org/project/ovs/)

<details><summary>README extract</summary>

The `openvswitch` package provides the official Python language bindings
for Open vSwitch. They are developed in-tree as part of the Open vSwitch
Package.

Example:
```python
import json
import ovs.dirs

schema_path = f'{ovs.dirs.PKGDATADIR}/vswitch.ovsschema'

with open(schema_path) as fh:
    schema = json.load(fh)

print(schema)
```

Sections: Open vSwitch, Examples, Inspecting the database schema, Dumping tables, ports and interfaces, Documentation

</details>

### tigerbeetle

The TigerBeetle client for Python.

`pip install tigerbeetle` · installs (wheel) · licence: Apache Software License · rank 11209 · last release 2026-07-06 · [PyPI](https://pypi.org/project/tigerbeetle/)

<details><summary>README extract</summary>

<!-- This file is generated by /src/scripts/client_readmes.zig. -->

The TigerBeetle client for Python.

Linux >= 5.6 is the only production environment we
support. But for ease of development we also support macOS and Windows.
* Python (or PyPy, etc) >= `3.7`

Example:
```python
import os

import tigerbeetle as tb

print("Import OK!")

# To enable debug logging, via Python's built in logging module:
# logging.basicConfig(level=logging.DEBUG)
# tb.configure_logging(debug=True)
```

Sections: tigerbeetle-python, Prerequisites, Setup, Sample projects, Creating a Client, Creating Accounts, Account Flags, Response and Errors, Account Lookup, Create Transfers, Batching, Queues and Workers, Transfer Flags

</details>

### kaquel

Tools for handling ElasticSearch queries in various languages

`pip install kaquel` · installs (wheel) · licence: CeCILL-C Free Software License Agreement (CECILL-C) · rank 12009 · last release 2024-10-24 · [PyPI](https://pypi.org/project/kaquel/) · [source](https://gitlab.com/kaquel/kaquel)

<details><summary>README extract</summary>

Kaquel, pronounced */kækyɛl/*, is a toolset for parsing and rendering
query languages for ElasticSearch.

As described in Parsing queries, you can parse Kibana Query Language (KQL),
Apache Lucene and ElasticSearch queries, and render them using the
ElasticSearch Query DSL. For example, with KQL:

The project is present at the following locations: ...

Example:
```python
from kaquel.kql import parse_kql

query = parse_kql('identity: { first_name: "John" }')
print(query.render())
```

</details>

### st-theme

A component that returns the active theme of the Streamlit app.

`pip install st-theme` · installs (wheel) · licence: MIT License · rank 12414 · last release 2024-05-03 · [PyPI](https://pypi.org/project/st-theme/) · [docs](https://github.com/gabrieltempass/streamlit-theme) · [source](https://github.com/gabrieltempass/streamlit-theme)

<details><summary>README extract</summary>

A component that returns the active theme of the Streamlit app.

Example:
```python
import streamlit as st
from streamlit_theme import st_theme
theme = st_theme()
st.write(theme)
```

Sections: Streamlit Theme, Usage, Parameters, Returns, Notes, Examples, Requirements, References

</details>

### dash-auth

Dash Authorization Package.

`pip install dash-auth` · installs (wheel) · licence: MIT License · rank 12667 · last release 2024-03-19 · [PyPI](https://pypi.org/project/dash-auth/)

<details><summary>README extract</summary>

Example:
```python
from dash import Dash
from dash_auth import BasicAuth

app = Dash(name)
USER_PWD = {
    "username": "password",
    "user2": "useSomethingMoreSecurePlease",
}
BasicAuth(app, USER_PWD)
```

Sections: Usage, Basic Authentication, Public routes, OIDC Authentication, Multiple OIDC Providers, User-group-based permissions

</details>

### pydoris

Python interface to Doris

`pip install pydoris` · installs (wheel) · licence: Apache Software License · rank 12760 · last release 2026-03-17 · [PyPI](https://pypi.org/project/pydoris/) · [source](https://github.com/apache/doris)

<details><summary>README extract</summary>

A Apache Doris client for the Python programming language.

Apache Doris is a high-performance, real-time analytical database based on MPP architecture, known for its extreme speed and ease of use. ...

Example:
```python
from sqlalchemy import create_engine
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.sql.expression import select, text

engine = create_engine('doris://root:xxx@localhost:9030/hive_catalog.hive_db')
connection = engine.connect()

rows = connection.execute(text("SELECT * FROM hive_table")).fetchall()
```

Sections: Apache Doris Python Client, SQLAlchemy Usage, Example

</details>

### convex

Python client for the reactive backend-as-a-service Convex.

`pip install convex` · installs (wheel) · licence: not stated · rank 12886 · last release 2026-09-14 · [PyPI](https://pypi.org/project/convex/) · [docs](https://docs.convex.dev) · [source](https://github.com/get-convex/convex-py)

<details><summary>README extract</summary>

The official Python client for Convex.

Write and read data from a Convex backend with queries, mutations, and actions.
Get up and running at docs.convex.dev.

Installation:

 pip install convex

Basic usage: ...

Example:
```python
>>> from convex import ConvexClient
>>> client = ConvexClient('
>>> messages = client.query("messages:list")
>>> from pprint import pprint
>>> pprint(messages)
[{'_creationTime': 1668107495676.2854,
  '_id': '2sh2c7pn6nyvkexbdsfj66vd9h5q3hg',
  'author': 'Tom',
  'body': 'Have you tried Convex?'},
 {'_creationTime': 1668107497732.2295,
...
```

Sections: Convex, Convex types, Ints and Floats, Convex Errors, Pagination, Versioning

</details>

### keepa

Interfaces with keepa.com's API.

`pip install keepa` · installs (wheel) · licence: Apache Software License · rank 13546 · last release 2026-10-05 · [PyPI](https://pypi.org/project/keepa/) · [docs](https://keepaapi.readthedocs.io/en/latest/) · [source](https://github.com/akaszynski/keepa)

<details><summary>README extract</summary>

This Python library allows you to interface with the API at Keepa to query for Amazon product information and history. It
also contains a plotting module to allow for plotting of a product.

Sign up for Keepa Data Access.

Documentation can be found at Keepa Documentation.

This library is compatible with Python >= 3.10 and requires:

- `numpy` ...

Example:
```python
import keepa
accesskey = 'XXXXXXXXXXXXXXXX' # enter real access key here from
api = keepa.Keepa(accesskey)

# Single ASIN query
products = api.query('B0088PUEPK')  # returns list of product data

# Plot result (requires matplotlib)
keepa.plot_product(products[0])
```

Sections: Python keepa Client Library, Requirements, Brief Example, Brief Example Using Async, Detailed Examples, Buy Box Statistics

</details>

### sqlalchemy-ibmi

SQLAlchemy support for Db2 on IBM i

`pip install sqlalchemy-ibmi` · installs (wheel) · licence: Apache-2.0 · rank 14490 · last release 2026-07-09 · [PyPI](https://pypi.org/project/sqlalchemy-ibmi/) · [docs](https://sqlalchemy-ibmi.readthedocs.io) · [source](https://github.com/IBM/sqlalchemy-ibmi)

<details><summary>README extract</summary>

The IBM i SQLAlchemy adapter provides an SQLAlchemy
interface to Db2 for IBM i.

**Please note that this project is still under active development. Please
 report any bugs in the issue tracker** :rotating_light:

| SQLAlchemy Version | Supported | Notes |

| SQLAlchemy 2.0 | ✅ | Support added in 0.9.4. ...

Example:
```python
import sqlalchemy as sa
engine = sa.create_engine("ibmi://user:password@host.example.com")

cnxn = engine.connect()
metadata = sa.MetaData()
table = sa.Table('table_name', metadata, autoload=True, autoload_with=engine)

query = sa.select([table])

result = cnxn.execute(query)
result = result.fetchall()

# print first entry
print(result[0])
```

...

</details>

### aiotrino

Asyncio client for the Trino distributed SQL Engine

`pip install aiotrino` · installs (wheel) · licence: Apache Software License · rank 14801 · last release 2025-03-21 · [PyPI](https://pypi.org/project/aiotrino/)

<details><summary>README extract</summary>

This package provides a asyncio client interface to query Trino
a distributed SQL engine. It supports Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12.

Example:
```python
import aiotrino
conn = aiotrino.dbapi.connect(
    host='localhost',
    port=8080,
    user='the-user',
    catalog='the-catalog',
    schema='the-schema',
)
cur = await conn.cursor()
await cur.execute('SELECT * FROM system.runtime.nodes')
rows = await cur.fetchall()
await conn.close()
```

Sections: Introduction, Quick Start, Basic Authentication, JWT Token Authentication, Transactions, Code Style, Running Tests, Test setup, Releasing, Need Help?

</details>

## Also in this topic

- [psycopg2-binary](database.md#psycopg2-binary) - psycopg2 - Python-PostgreSQL Database Adapter
- [psycopg](database.md#psycopg) - PostgreSQL database adapter for Python
- [psycopg-binary](database.md#psycopg-binary) - PostgreSQL database adapter for Python -- C optimisation distribution
- [psycopg2](database.md#psycopg2) - psycopg2 - Python-PostgreSQL Database Adapter
- [psycopg-pool](database.md#psycopg-pool) - Connection Pool for Psycopg
- [peewee](database.md#peewee) - a little orm
- [PyAthena](database.md#pyathena) - Python DB API 2.0 (PEP 249) client for Amazon Athena
- [aiomysql](database.md#aiomysql) - MySQL driver for asyncio.
- [psycopg-c](database.md#psycopg-c) - PostgreSQL database adapter for Python -- C optimisation distribution
- [aioodbc](database.md#aioodbc) - ODBC driver for asyncio.
- [vertica-python](database.md#vertica-python) - Official native Python client for the Vertica database.
- [intersystems-irispython](database.md#intersystems-irispython) - InterSystems IRIS Python SDK Kit
- [upstash-redis](database.md#upstash-redis) - Serverless Redis SDK from Upstash
- [prisma](database-database-engines-servers.md#prisma) - Prisma Client Python is an auto-generated and fully type-safe database client
- [yoyo-migrations](database.md#yoyo-migrations) - Database migrations with SQL
- [aiopg](database.md#aiopg) - Postgres integration with asyncio.
- [sqlcipher3](database.md#sqlcipher3) - DB-API 2.0 interface for SQLCipher 4.x
- [sqlalchemy-hana](database.md#sqlalchemy-hana) - SQLAlchemy dialect for SAP HANA
- [qstash](database.md#qstash) - Python SDK for Upstash QStash
- [sqlalchemy-cloudflare-d1](database.md#sqlalchemy-cloudflare-d1) - A SQLAlchemy dialect for Cloudflare's D1 Serverless SQLite Database
- [pysqlite3](database.md#pysqlite3) - DB-API 2.0 interface for Sqlite 3.x
- [sqlalchemy-trino](database.md#sqlalchemy-trino) - Trino dialect for SQLAlchemy
- [PyGreSQL](database.md#pygresql) - Python PostgreSQL interfaces
- [django-fast-update](database.md#django-fast-update) - Faster db updates for Django using UPDATE FROM VALUES sql variants.
- [pgcli](database.md#pgcli) - CLI for Postgres Database. With auto-completion and syntax highlighting.
- [sqlalchemy-databricks](database.md#sqlalchemy-databricks) - SQLAlchemy Dialect for Databricks
- [sqlalchemy-filters](database.md#sqlalchemy-filters) - A library to filter SQLAlchemy queries.
- [ipython-sql](database.md#ipython-sql) - RDBMS access via IPython
- [surrealdb](database.md#surrealdb) - SurrealDB python client
- [jupysql](database.md#jupysql) - Better SQL in Jupyter
- [upstash-vector](database.md#upstash-vector) - Serverless Vector SDK from Upstash
- [sqlalchemy-monetdb](database.md#sqlalchemy-monetdb) - SQLAlchemy dialect for MonetDB
- [pylakekeeper](database.md#pylakekeeper) - Official Lakekeeper client — generic-tables API and OAuth2 auth (static token / client_credentials with refresh)
- [mycli](database.md#mycli) - Rich MySQL terminal client with autocompletion, syntax highlighting, and dataframes
- [pyhdb](database.md#pyhdb) - SAP HANA Database Client for Python
- [pymgclient](database.md#pymgclient) - Memgraph database adapter for Python language
- [dbt-vertica](database.md#dbt-vertica) - Official vertica adapter plugin for dbt (data build tool)
- [hopsworks-aiomysql](database.md#hopsworks-aiomysql) - MySQL driver for asyncio.
- [odmantic](database.md#odmantic) - ODMantic, an AsyncIO MongoDB Object Document Mapper for Python using type hints
- [foundationdb](database.md#foundationdb) - Python bindings for the FoundationDB Database
