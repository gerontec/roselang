# Database

[Index](README.md) · 234 packages in this topic, 2 more listed under another topic, by downloads.

### psycopg2-binary

psycopg2 - Python-PostgreSQL Database Adapter

`pip install psycopg2-binary` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 146 · last release 2026-09-10 · [PyPI](https://pypi.org/project/psycopg2-binary/) · [docs](https://www.psycopg.org/docs/) · [source](https://github.com/psycopg/psycopg2)

_README extract left out: share-alike licence._

### psycopg

PostgreSQL database adapter for Python

`pip install psycopg` · installs (wheel) · licence: LGPL-3.0-only · rank 170 · last release 2026-11-04 · [PyPI](https://pypi.org/project/psycopg/) · [docs](https://psycopg.org/psycopg3/docs/) · [source](https://github.com/psycopg/psycopg)

_README extract left out: share-alike licence._

### psycopg-binary

PostgreSQL database adapter for Python -- C optimisation distribution

`pip install psycopg-binary` · installs (wheel) · licence: LGPL-3.0-only · rank 181 · last release 2026-11-04 · [PyPI](https://pypi.org/project/psycopg-binary/) · [docs](https://psycopg.org/psycopg3/docs/) · [source](https://github.com/psycopg/psycopg)

_README extract left out: share-alike licence._

### sqlparse

A non-validating SQL parser.

`pip install sqlparse` · installs (wheel) · licence: BSD License · rank 257 · last release 2026-11-01 · [PyPI](https://pypi.org/project/sqlparse/) · [docs](https://sqlparse.readthedocs.io/) · [source](https://github.com/andialbrecht/sqlparse)

<details><summary>README extract</summary>

> [!IMPORTANT]
> Project Status: End of Maintenance
> sqlparse is no longer actively maintained. Version 0.6.1 was its final release.
> No further bug fixes, feature updates, or security fixes are planned. The repository and published packages will remain available, but users should not expect ongoing maintenance or security support. ...

Example:
```python
import sqlparse

sqlparse.split("select * from foo; select * from bar;")
# ['select * from foo;', 'select * from bar;']
```

Sections: sqlparse, Usage, Split a script into statements, Format a statement, Parse and inspect a statement, Command line, Pre-commit hook, Links

</details>

### snowflake-connector-python

Snowflake DB driver for Python

`pip install snowflake-connector-python` · installs (wheel) · licence: Apache Software License · rank 275 · last release 2026-11-04 · [PyPI](https://pypi.org/project/snowflake-connector-python/) · [docs](https://github.com/snowflakedb/drivers/blob/main/README.md) · [source](https://github.com/snowflakedb/drivers)

<details><summary>README extract</summary>

This package includes the Snowflake Connector for Python, which conforms to the Python DB API 2.0 specification.

The Snowflake Connector for Python provides an interface for developing Python
applications that can connect to Snowflake and perform all standard operations. ...

Sections: Snowflake Connector for Python, Prerequisites, Setup, Environment Variables, Hatch Environments, `test` Environment (for CI/CD pipelines), Environment Comparison, Other Environments, References

</details>

### PyMySQL

Pure Python MySQL Driver

`pip install PyMySQL` · installs (wheel) · licence: MIT · rank 331 · last release 2026-09-17 · [PyPI](https://pypi.org/project/PyMySQL/) · [docs](https://pymysql.readthedocs.io/)

<details><summary>README extract</summary>

This package contains a pure-Python MySQL and MariaDB client library, based on
PEP 249.

 - CPython : 3.9 and newer
 - PyPy : Latest 3.x version

 - MySQL LTS versions
 - MariaDB LTS versions

Example:
```python
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="user",
    password="passwd",
    database="db",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
...
```

Sections: PyMySQL, Requirements, Documentation, Example, Resources

</details>

### xlrd

Library for developers to extract data from Microsoft Excel (tm) .xls spreadsheet files

`pip install xlrd` · installs (wheel) · licence: BSD License · rank 339 · last release 2025-06-14 · [PyPI](https://pypi.org/project/xlrd/)

<details><summary>README extract</summary>

xlrd is a library for reading data and formatting information from Excel
files in the historical `.xls` format.

The following are also not supported but will safely and reliably be ignored:

* Charts, Macros, Pictures, any other embedded object, including embedded worksheets. ...

Example:
```python
import xlrd
book = xlrd.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
...
```

</details>

### pymongo

PyMongo - the Official MongoDB Python driver

`pip install pymongo` · installs (wheel) · licence: Apache-2.0 · rank 362 · last release 2026-10-14 · [PyPI](https://pypi.org/project/pymongo/) · [docs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) · [source](https://github.com/mongodb/mongo-python-driver)

<details><summary>README extract</summary>

The PyMongo distribution contains tools for interacting with MongoDB
database from Python. The `bson` package is an implementation of the
BSON format for Python. The `pymongo` package is
a native Python driver for MongoDB, offering both synchronous and asynchronous APIs. The `gridfs` package is a
gridfs
implementation on top of `pymongo`. ...

Example:
```python
>>> import pymongo
>>> client = pymongo.MongoClient("localhost", 27017)
>>> db = client.test
>>> db.name
'test'
>>> db.my_collection
Collection(Database(MongoClient('localhost', 27017), 'test'), 'my_collection')
>>> db.my_collection.insert_one({"x": 10}).inserted_id
ObjectId('4aba15ebe23f6b53b0000000')
...
```

...

</details>

### duckdb

DuckDB in-process database

`pip install duckdb` · installs (wheel) · licence: MIT License · rank 366 · last release 2026-10-21 · [PyPI](https://pypi.org/project/duckdb/) · [docs](https://duckdb.org/docs/stable/clients/python/overview) · [source](https://github.com/duckdb/duckdb-python)

<details><summary>README extract</summary>

DuckDB.org
 User Guide (Python)

 API Docs (Python)

* Simple: DuckDB is easy to install and deploy. It has zero external dependencies and runs in-process in its host application or as a single binary.
* Portable: DuckDB runs on Linux, macOS, Windows, Android, iOS and all popular hardware architectures. ...

</details>

### psycopg2

psycopg2 - Python-PostgreSQL Database Adapter

`pip install psycopg2` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 390 · last release 2026-09-09 · [PyPI](https://pypi.org/project/psycopg2/) · [docs](https://www.psycopg.org/docs/) · [source](https://github.com/psycopg/psycopg2)

_README extract left out: share-alike licence._

### psycopg-pool

Connection Pool for Psycopg

`pip install psycopg-pool` · installs (wheel) · licence: LGPL-3.0-only · rank 424 · last release 2026-09-22 · [PyPI](https://pypi.org/project/psycopg-pool/) · [docs](https://www.psycopg.org/psycopg3/docs/advanced/pool.html) · [source](https://github.com/psycopg/psycopg)

_README extract left out: share-alike licence._

### peewee

a little orm

`pip install peewee` · installs (wheel) · licence: not stated · rank 517 · last release 2026-10-07 · [PyPI](https://pypi.org/project/peewee/) · [docs](https://docs.peewee-orm.com/) · [source](https://github.com/coleifer/peewee)

<details><summary>README extract</summary>

Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.

Peewee is a single module with no required dependencies and has been running
production workloads of all sizes since 2010. ...

Example:
```python
from peewee import *
import datetime

db = SqliteDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
...
```

Sections: peewee, Examples, Asyncio, Learning more, Still want more info?

</details>

### pymssql

DB-API interface to Microsoft SQL Server for Python. (new Cython-based version)

`pip install pymssql` · installs (wheel) · licence: not stated · rank 550 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pymssql/) · [docs](http://pymssql.readthedocs.io) · [source](https://github.com/pymssql/pymssql)

<details><summary>README extract</summary>

A simple database interface for Python that builds on top of FreeTDS to
provide a Python DB-API (PEP-249) interface to Microsoft SQL Server.

Detailed information on pymssql is available on the website:

pymssql.readthedocs.io

New development is happening on GitHub at:

github.com/pymssql/pymssql

There is a Google Group for discussion at: ...

Example:
```python
conn = pymssql.connect(server, user, password, "tempdb")
cursor = conn.cursor(as_dict=True)

cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))

conn.close()
```

...

</details>

### snowballstemmer

This package provides 36 stemmers for 34 languages generated from Snowball algorithms.

`pip install snowballstemmer` · installs (wheel) · licence: BSD-3-Clause · rank 612 · last release 2026-06-03 · [PyPI](https://pypi.org/project/snowballstemmer/)

<details><summary>README extract</summary>

Python 3 (>= 3.3) is supported. We no longer support Python 2 as the Python
developers stopped supporting it at the start of 2020. Snowball 2.1.0 was the
last release to officially support Python 2; Snowball 3.0.1 was the last
release which had the code to support Python 2, but we were no longer testing
it. ...

Example:
```python
import snowballstemmer

stemmer = snowballstemmer.stemmer('english')
print(stemmer.stemWords("We are the world".split()))
```

Sections: Snowball stemming library collection for Python, What is Stemming?, How to use library, Automatic Acceleration, Benchmark, The TestApp example

</details>

### h5py

Read and write HDF5 files from Python

`pip install h5py` · installs (wheel) · licence: BSD-3-Clause · rank 614 · last release 2026-03-06 · [PyPI](https://pypi.org/project/h5py/) · [docs](https://docs.h5py.org/en/stable/) · [source](https://github.com/h5py/h5py)

<details><summary>README extract</summary>

The h5py package provides both a high- and low-level interface to the HDF5
library from Python. The low-level interface is intended to be a complete
wrapping of the HDF5 API, while the high-level component supports access to
HDF5 files, datasets and groups using established Python and NumPy concepts. ...

</details>

### pyodbc

DB API module for ODBC

`pip install pyodbc` · installs (wheel) · licence: MIT-0 · rank 657 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyodbc/)

<details><summary>README extract</summary>

pyodbc is an open source Python module that makes accessing ODBC databases simple. It
implements the DB API 2.0 specification but is packed with even more Pythonic convenience.

The easiest way to install pyodbc is to use pip:

 python -m pip install pyodbc ...

</details>

### mysql-connector-python

A self-contained Python driver for communicating with MySQL servers, using an API that is compliant with the Python Database API Specification v2.0 (PEP 249).

`pip install mysql-connector-python` · installs (wheel) · licence: GNU General Public License (GPL) · rank 675 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mysql-connector-python/) · [docs](https://dev.mysql.com/doc/connector-python/en/) · [source](https://github.com/mysql/mysql-connector-python)

_README extract left out: share-alike licence._

### sqlmodel

SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.

`pip install sqlmodel` · installs (wheel) · licence: MIT · rank 704 · last release 2026-10-06 · [PyPI](https://pypi.org/project/sqlmodel/) · [docs](https://sqlmodel.tiangolo.com) · [source](https://github.com/fastapi/sqlmodel)

<details><summary>README extract</summary>

SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.

Documentation:

Source Code:

SQLModel is a library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust. ...

Example:
```python
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
```

Sections: SQL Databases in FastAPI, Requirements, Example, A SQL Table, Create a SQLModel Model, Create Rows, Write to the Database, Select from the Database, SQLAlchemy and Pydantic

</details>

### snowflake-sqlalchemy

Snowflake SQLAlchemy Dialect

`pip install snowflake-sqlalchemy` · installs (wheel) · licence: Apache-2.0 · rank 749 · last release 2026-10-26 · [PyPI](https://pypi.org/project/snowflake-sqlalchemy/) · [docs](https://docs.snowflake.com/en/user-guide/sqlalchemy.html) · [source](https://github.com/snowflakedb/snowflake-sqlalchemy)

<details><summary>README extract</summary>

Snowflake SQLAlchemy runs on the top of the Snowflake Connector for Python as a dialect to bridge a Snowflake database and SQLAlchemy applications.

> v2.1.0 — Async is opt-in: SQLAlchemy 2.1 no longer installs `greenlet`, so the base install is sync-only. ...

Example:
```python
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user='<your_user_login_name>',
        password='<your_password>',
        account='<your_account_name>',
    )
)

async def main():
...
```

...

</details>

### oracledb

Python interface to Oracle Database

`pip install oracledb` · installs (wheel) · licence: UPL-1.0 OR Apache-2.0 · rank 839 · last release 2026-10-27 · [PyPI](https://pypi.org/project/oracledb/) · [docs](http://python-oracledb.readthedocs.io) · [source](https://github.com/oracle/python-oracledb)

<details><summary>README extract</summary>

The python-oracledb driver is the widely used, open-source Python
extension module allowing Python programs to connect directly to Oracle
Database with no extra libraries needed. The module is built with
Cython for safety and speed. It is lightweight and high-performance. It is
stable, well tested, and has comprehensive documentation. ...

Example:
```python
import oracledb
import getpass

un = "scott"                  # Sample database username
cs = "localhost/orclpdb"      # Sample database connection string
# cs = "localhost/freepdb1"   # For Oracle Database Free users
# cs = "localhost/orclpdb1"   # Some databases may have this service
pw = getpass.getpass(f"Enter password for {un}@{cs}: ")

...
```

...

</details>

### PyAthena

Python DB API 2.0 (PEP 249) client for Amazon Athena

`pip install PyAthena` · installs (wheel) · licence: MIT · rank 920 · last release 2026-10-23 · [PyPI](https://pypi.org/project/PyAthena/) · [docs](https://pyathena.dev/) · [source](https://github.com/pyathena-dev/PyAthena/)

<details><summary>README extract</summary>

PyAthena is a Python DB API 2.0 (PEP 249) client for Amazon Athena.

- Python

 - CPython 3.11, 3.12, 3.13, 3.14, 3.15

Example:
```python
from pyathena import connect

cursor = connect(s3_staging_dir="s3://YOUR_S3_BUCKET/path/to/",
                 region_name="us-west-2").cursor()
cursor.execute("SELECT * FROM one_row")
print(cursor.description)
print(cursor.fetchall())
```

Sections: PyAthena, Requirements, Usage, Links, Logo

</details>

### mysqlclient

Python interface to MySQL

`pip install mysqlclient` · installs from source (sdist only) · licence: GPL-2.0-or-later · rank 943 · last release 2026-09-14 · [PyPI](https://pypi.org/project/mysqlclient/) · [docs](https://mysqlclient.readthedocs.io/)

_README extract left out: share-alike licence._

### neo4j

Neo4j Bolt driver for Python

`pip install neo4j` · installs (wheel) · licence: Apache-2.0 AND Python-2.0 · rank 1042 · last release 2026-10-15 · [PyPI](https://pypi.org/project/neo4j/) · [source](https://github.com/neo4j/neo4j-python-driver)

<details><summary>README extract</summary>

This repository contains the official Neo4j driver for Python.

Driver upgrades within a major version will never contain breaking API changes.

For version compatibility with Neo4j server, please refer to:

+ Python 3.15 supported.
+ Python 3.14 supported.
+ Python 3.13 supported.
+ Python 3.12 supported.
+ Python 3.11 supported. ...

Example:
```python
from neo4j import GraphDatabase, RoutingControl

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")

def add_friend(driver, name, friend_name):
    driver.execute_query(
        "MERGE (a:Person {name: $name}) "
        "MERGE (friend:Person {name: $friend_name}) "
        "MERGE (a)-[:KNOWS]->(friend)",
...
```

Sections: Neo4j Bolt Driver for Python, Quick Example, Further Information

</details>

### snowflake-snowpark-python

Snowflake Snowpark for Python

`pip install snowflake-snowpark-python` · installs (wheel) · licence: Apache Software License · rank 1127 · last release 2026-10-30 · [PyPI](https://pypi.org/project/snowflake-snowpark-python/) · [docs](https://docs.snowflake.com/en/developer-guide/snowpark/python/index.html) · [source](https://github.com/snowflakedb/snowpark-python)

<details><summary>README extract</summary>

The Snowpark library provides intuitive APIs for querying and processing data in a data pipeline.
Using this library, you can build applications that process data in Snowflake without having to move data to the system where your application code runs. ...

Example:
```python
from snowflake.snowpark import Session

connection_parameters = {
  "account": "<your snowflake account>",
  "user": "<your snowflake user>",
  "password": "<your snowflake password>",
  "role": "<snowflake user role>",
  "warehouse": "<snowflake warehouse>",
  "database": "<snowflake database>",
  "schema": "<snowflake schema>"
}

...
```

...

</details>

### clickhouse-driver

Python driver with native interface for ClickHouse

`pip install clickhouse-driver` · installs (wheel) · licence: MIT License · rank 1135 · last release 2026-07-17 · [PyPI](https://pypi.org/project/clickhouse-driver/) · [docs](https://clickhouse-driver.readthedocs.io)

<details><summary>README extract</summary>

ClickHouse Python Driver with native (TCP) interface support.

Asynchronous wrapper is available here:

Features:
- External data for query processing.

- Query settings.

- Compression support.

- TLS support.

 * Float32/64
 * [U]Int8/16/32/64/128/256
 * Date/Date32/DateTime('timezone')/DateTime64('timezone')
 * String/FixedString(N)
 * Enum8/16
 * Array(T) ...

Sections: ClickHouse Python Driver, Features, Documentation, Usage

</details>

### aiomysql

MySQL driver for asyncio.

`pip install aiomysql` · installs (wheel) · licence: MIT · rank 1162 · last release 2025-10-22 · [PyPI](https://pypi.org/project/aiomysql/) · [docs](https://aiomysql.readthedocs.io/) · [source](https://github.com/aio-libs/aiomysql)

<details><summary>README extract</summary>

aiomysql is a "driver" for accessing a `MySQL` database
from the asyncio (PEP-3156/tulip) framework. It depends on and reuses most
parts of PyMySQL . *aiomysql* tries to be like awesome aiopg library and
preserve same api, look and feel. ...

Example:
```python
import asyncio
import aiomysql

async def test_example():
    async with aiomysql.create_pool(host='127.0.0.1', port=3306,
                                    user='root', password='',
                                    db='mysql') as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
...
```

Sections: aiomysql, Documentation, Basic Example, Example of SQLAlchemy optional integration, Requirements

</details>

### rtree

R-Tree spatial index for Python GIS

`pip install rtree` · installs (wheel) · licence: MIT · rank 1172 · last release 2025-08-13 · [PyPI](https://pypi.org/project/rtree/) · [docs](https://rtree.readthedocs.io) · [source](https://github.com/Toblerity/rtree)

<details><summary>README extract</summary>

Rtree is a ctypes Python wrapper of libspatialindex that provides a
number of advanced spatial indexing features for the spatially curious Python
user. These features include:

* Nearest neighbor search
* Intersection search
* Multi-dimensional indexes
* Clustered indexes (store Python pickles directly with index entries)
* Bulk loading
* ...

</details>

### JayDeBeApi

Use JDBC database drivers from Python 2/3 or Jython with a DB-API.

`pip install JayDeBeApi` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 1233 · last release 2020-06-12 · [PyPI](https://pypi.org/project/JayDeBeApi/)

_README extract left out: share-alike licence._

### pglast

PostgreSQL Languages AST and statements prettifier

`pip install pglast` · installs (wheel) · licence: GPL-3.0-or-later · rank 1238 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pglast/) · [source](https://github.com/lelit/pglast)

_README extract left out: share-alike licence._

### mongomock

Fake pymongo stub for testing simple MongoDB-dependent code

`pip install mongomock` · installs (wheel) · licence: ISC License (ISCL) · rank 1331 · last release 2024-11-16 · [PyPI](https://pypi.org/project/mongomock/)

<details><summary>README extract</summary>

Mongomock is a small library to help testing Python code that interacts with MongoDB via Pymongo.

To understand what it's useful for, we can take the following code:

The above code can be tested in several ways:

1. It can be tested against a real mongodb instance with pymongo.
2. It can receive a record-replay style mock as an argument. ...

Example:
```python
def increase_votes(collection):
    for document in collection.find():
        collection.update_one(document, {'$set': {'votes': document['votes'] + 1}})
```

Sections: What is this?, 2 in action - we might write our test like so, Upgrading to Pymongo v4, utcnow, Branching model, Releasing

</details>

### xlwt

Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.6, 2.7, 3.3+

`pip install xlwt` · installs (wheel) · licence: BSD License · rank 1433 · last release 2017-08-22 · [PyPI](https://pypi.org/project/xlwt/)

<details><summary>README extract</summary>

This is a library for developers to use to generate
spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or packages
outside the standard Python distribution.

Please read this before using this package:

Example:
```python
import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
...
```

Sections: xlwt, Quick start, Documentation, Problems?

</details>

### docling-core

A python library to define and validate data types in Docling.

`pip install docling-core` · installs (wheel) · licence: MIT · rank 1745 · last release 2026-11-04 · [PyPI](https://pypi.org/project/docling-core/) · [source](https://github.com/docling-project/docling-core)

<details><summary>README extract</summary>

Docling Core is a library that defines core data types and transformations in Docling.

Example:
```python
from docling_core.utils.settings import settings

settings.allow_image_file_uri = True
```

Sections: Docling Core, Main features, DoclingDocument, Serialization, Chunking, Profiling, Configuration, Local image files, References

</details>

### PySide6-Essentials

Python bindings for the Qt cross-platform application and UI framework (Essentials)

`pip install PySide6-Essentials` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 1765 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PySide6-Essentials/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### shiboken6

Python/C++ bindings helper module

`pip install shiboken6` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 1832 · last release 2026-10-08 · [PyPI](https://pypi.org/project/shiboken6/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### sqlparams

Convert between various DB API 2.0 parameter styles.

`pip install sqlparams` · installs (wheel) · licence: MIT License · rank 1855 · last release 2025-01-25 · [PyPI](https://pypi.org/project/sqlparams/) · [docs](https://python-sql-parameters.readthedocs.io/en/latest/index.html) · [source](https://github.com/cpburnz/python-sqlparams)

<details><summary>README extract</summary>

*sqlparams* is a utility package for converting between various SQL
parameter styles. This can simplify the use of SQL parameters in queries by
allowing the use of named parameters where only ordinal are supported. ...

Example:
```python
>>> import sqlparams
>>> query = sqlparams.SQLParams('named', 'qmark')
```

Sections: SQL Params, Tutorial, Source, Documentation, 6.2.0 (2024-01-25), 6.1.0 (2024-08-17), 6.0.1 (2023-12-09), 6.0.0 (2023-12-09), 5.1.0 (2023-03-14), 5.0.0 (2022-08-11), 4.0.0 (2022-06-06), 3.0.0 (2020-04-04), 2.0.0 (2020-02-26), 1.2.0 (2020-02-26)

</details>

### tinydb

TinyDB is a tiny, document oriented database optimized for your happiness :)

`pip install tinydb` · installs (wheel) · licence: MIT · rank 1879 · last release 2026-08-06 · [PyPI](https://pypi.org/project/tinydb/) · [docs](https://tinydb.readthedocs.org/)

<details><summary>README extract</summary>

- Example Code
- Supported Python Versions
- Documentation
- Changelog
- Extensions
- Contributing

TinyDB is a lightweight document oriented database optimized for your happiness :)
It's written in pure Python and has no external dependencies. The target are
small apps that would be blown away by a SQL-DB or an external database server. ...

Example:
```python
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('/path/to/db.json')
>>> db.insert({'int': 1, 'char': 'a'})
>>> db.insert({'int': 1, 'char': 'b'})
```

Sections: Quick Links, Introduction, Example Code, Query Language, Tables, Using Middlewares

</details>

### datasketch

Probabilistic data structures for processing and searching very large datasets

`pip install datasketch` · installs (wheel) · licence: MIT License · rank 2002 · last release 2026-07-05 · [PyPI](https://pypi.org/project/datasketch/) · [docs](https://ekzhu.github.io/datasketch) · [source](https://github.com/ekzhu/datasketch)

<details><summary>README extract</summary>

datasketch gives you probabilistic data structures that can process and
search very large amount of data super fast, with little loss of
accuracy.

This package contains the following data sketches: ...

Sections: datasketch: Big Data Looks Small, Guidelines

</details>

### PySide6-Addons

Python bindings for the Qt cross-platform application and UI framework (Addons)

`pip install PySide6-Addons` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 2009 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PySide6-Addons/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### pinecone

Pinecone Python SDK

`pip install pinecone` · installs (wheel) · licence: Apache-2.0 · rank 2031 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pinecone/) · [docs](https://sdk.pinecone.io/python/) · [source](https://github.com/pinecone-io/python-sdk)

<details><summary>README extract</summary>

The Pinecone Python SDK provides a client for the Pinecone vector database. Use it to create and manage indexes, upsert and query records, and run inference operations from Python.

Requires Python 3.10+. ...

Example:
```python
from pinecone import DenseVectorQuery, Pinecone

pc = Pinecone(api_key="your-api-key")  # or omit and set PINECONE_API_KEY

# Create an index. This blocks until the index is ready.
pc.indexes.create(
    name="movie-recommendations",
    schema={"fields": {"your_vector": {"type": "dense_vector", "dimension": 3, "metric": "cosine"}}},
...
```

Sections: Pinecone Python SDK, Quick start, Async usage, Configuration

</details>

### snowflake.core

Snowflake Python API for Resource Management

`pip install snowflake.core` · installs (wheel) · licence: Apache Software License · rank 2036 · last release 2026-10-22 · [PyPI](https://pypi.org/project/snowflake.core/)

<details><summary>README extract</summary>

`snowflake.core` is the subpackage providing Python access to Snowflake entity metadata.

You can use it to interact with Snowflake resources, creating, deleting, modifying them, and more.

Developer guide

API reference

</details>

### PySide6

Python bindings for the Qt cross-platform application and UI framework

`pip install PySide6` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 2093 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PySide6/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### dbos

Ultra-lightweight durable execution in Python

`pip install dbos` · installs (wheel) · licence: MIT License · rank 2125 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dbos/)

<details><summary>README extract</summary>

Features:
💾 Durable Workflows

Example:
```python
from dbos import DBOS

@DBOS.step()
def step_one():
    ...

@DBOS.step()
def step_two():
    ...

@DBOS.workflow()
def workflow()
    step_one()
    step_two()
```

Sections: DBOS Transact: Lightweight Durable Workflows, Documentation • Examples • Github • Discord, What is DBOS?, When Should I Use DBOS?, Features, #, Getting Started, Documentation, Examples

</details>

### chdb

chDB is an in-process OLAP SQL Engine powered by ClickHouse

`pip install chdb` · installs (wheel) · licence: Apache Software License · rank 2242 · last release 2026-09-11 · [PyPI](https://pypi.org/project/chdb/) · [docs](https://clickhouse.com/docs/chdb) · [source](https://github.com/chdb-io/chdb)

<details><summary>README extract</summary>

🎉 New: chDB-Wasm — the complete ClickHouse engine compiled to WebAssembly. Run SQL in your browser, no server, no install → wasm.chdb.io

 Contributing? See CONTRIBUTING.md — setup, the modify-then-test workflow, PR conventions, CI, and releases. AGENTS.md (kept short and stays in agent context) captures the chdb-ds design and testing principles.

Features:
* 🐼 Pandas-compatible DataStore API - Use familiar pandas syntax with ClickHouse performance
* 🌐 Runs in the browser via WebAssembly - chDB-Wasm compiles the full engine to WASM; try it live at wasm.chdb.io
* In-process SQL OLAP Engine, powered by ...

Example:
```python
import datastore as pd  # That's it! Use pandas API as usual

# Create a DataFrame - works exactly like pandas
df = pd.DataFrame({
...

</details>

### lmdb

Universal Python binding for the LMDB 'Lightning' Database

`pip install lmdb` · installs (wheel) · licence: OLDAP-2.8 · rank 2329 · last release 2026-10-02 · [PyPI](https://pypi.org/project/lmdb/)

<details><summary>README extract</summary>

Universal Python binding for the LMDB 'Lightning' Database

</details>

### influxdb-client

InfluxDB 2.0 Python client library

`pip install influxdb-client` · installs (wheel) · licence: MIT License · rank 2357 · last release 2026-01-23 · [PyPI](https://pypi.org/project/influxdb-client/)

<details><summary>README extract</summary>

<!-- marker-index-start -->

This repository contains the Python client library for use with InfluxDB 2.x and Flux. InfluxDB 3.x users should instead use the lightweight v3 client library.
InfluxDB 1.x users should use the v1 client library. ...

Example:
```python
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"

client = InfluxDBClient(url=" token="my-token", org="my-org")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

...
```

...

</details>

### python-ldap

Python modules for implementing LDAP clients

`pip install python-ldap` · installs from source (sdist only) · licence: Python Software Foundation License · rank 2379 · last release 2026-09-16 · [PyPI](https://pypi.org/project/python-ldap/) · [docs](https://python-ldap.readthedocs.io/) · [source](https://github.com/python-ldap/python-ldap)

<details><summary>README extract</summary>

python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP client libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

Not included: Direct BER support ...

Example:
```python
import ldap
l = ldap.initialize("ldap://my_ldap_server.my_domain")
l.simple_bind_s("","")
l.search_s("o=My Organisation, c=AU", ldap.SCOPE_SUBTREE, "objectclass=*")
```

Sections: python-ldap: LDAP client API for Python, What is python-ldap?, Quick usage example

</details>

### chdb-core

chDB is an in-process OLAP SQL Engine powered by ClickHouse

`pip install chdb-core` · installs (wheel) · licence: Apache Software License · rank 2387 · last release 2026-09-29 · [PyPI](https://pypi.org/project/chdb-core/) · [docs](https://chdb.readthedocs.io/en/latest/index.html) · [source](https://github.com/chdb-io/chdb-core)

<details><summary>README extract</summary>

> chdb-core is the foundational engine of the chDB ecosystem — an in-process SQL OLAP Engine powered by ClickHouse [^1]

Features:
* In-process SQL OLAP Engine, powered by ClickHouse
* No need to install ClickHouse
* Minimized data copy from C++ to Python with python memoryview
* Input & Output support Parquet, CSV, JSON, Arrow, ORC and 60+ more formats
* Session and Connection ...

Example:
```python
import chdb

result = chdb.query("SELECT version()", "Pretty")
print(result)
```

Sections: chdb-core, Packages & Distributions, Features, Architecture, Quick Start, API Reference, Query on Pandas DataFrame, Query on Arrow Table, Demos and Examples, Benchmark, Documentation, AI Coding Agent Skill, Events, Bindings

</details>

### pymongo-auth-aws

MONGODB-AWS authentication support for PyMongo

`pip install pymongo-auth-aws` · installs (wheel) · licence: Apache Software License · rank 2445 · last release 2024-09-11 · [PyPI](https://pypi.org/project/pymongo-auth-aws/)

<details><summary>README extract</summary>

:Info: MONGODB-AWS authentication support for PyMongo. See
 GitHub
 for the latest source.
:Author: Shane Harvey

MONGODB-AWS authentication support for PyMongo. pymongo-auth-aws uses
boto3, botocore, and requests.

Example:
```python
$ python -c "import sys; print(sys.version)"
```

Sections: pymongo-auth-aws, About, Bugs / Feature Requests, How To Ask For Help, Dependencies

</details>

### nvtx

Python NVTX - Python code annotation library

`pip install nvtx` · installs (wheel) · licence: Apache-2.0 WITH LLVM-exception · rank 2485 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvtx/) · [docs](https://nvidia.github.io/NVTX/python/) · [source](https://github.com/NVIDIA/NVTX)

<details><summary>README extract</summary>

Example:
```python
# demo.py

import time
import nvtx

@nvtx.annotate(color="blue")
def my_function():
    for i in range(5):
        with nvtx.annotate("my_loop", color="red"):
            time.sleep(i)

my_function()
```

Sections: nvtx Python package, Quick start, Documentation, 0.2.17, 0.2.16, 0.2.15, 0.2.14, 0.2.13, 0.2.12

</details>

### sqlacodegen

Automatic model code generator for SQLAlchemy

`pip install sqlacodegen` · installs (wheel) · licence: MIT · rank 2506 · last release 2026-06-19 · [PyPI](https://pypi.org/project/sqlacodegen/) · [source](https://github.com/agronholm/sqlacodegen)

<details><summary>README extract</summary>

This is a tool that reads the structure of an existing database and generates the
appropriate SQLAlchemy model code, using the declarative style if possible.

This tool was written as a replacement for sqlautocode, which was suffering from
several issues (including, but not limited to, incompatibility with Python 3 and the
latest SQLAlchemy ...

Features:
* Supports SQLAlchemy 2.x
* Produces declarative code that almost looks like it was hand written
* Produces PEP 8 compliant code
* Accurately determines relationships, including many-to-many, one-to-one
* Automatically detects joined table ...

...

</details>

### django-polymorphic

Seamless polymorphic inheritance for Django models.

`pip install django-polymorphic` · installs (wheel) · licence: BSD-3-Clause · rank 2525 · last release 2026-08-01 · [PyPI](https://pypi.org/project/django-polymorphic/) · [docs](https://django-polymorphic.readthedocs.io) · [source](https://github.com/django-commons/django-polymorphic)

<details><summary>README extract</summary>

django-polymorphic simplifies using inherited models in Django projects. When a query is made at the base model, the inherited model classes are returned.

When we store models that inherit from a ``Project`` model...

...and want to retrieve all our projects, the subclassed models are returned! ...

Features:
* Full admin integration.

 * support for ForeignKey, ManyToManyField, OneToOneField descriptors.
 * Filtering/ordering of inherited models (``ArtProject___artist``). ...

Example:
```python
>>> Project.objects.create(topic="Department Party")
>>> ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
>>> ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")
```

Sections: django-polymorphic, Polymorphic Models for Django, Features

</details>

### tables

Hierarchical datasets for Python

`pip install tables` · installs (wheel) · licence: BSD License · rank 2530 · last release 2026-03-01 · [PyPI](https://pypi.org/project/tables/) · [docs](http://www.pytables.org) · [source](https://github.com/PyTables/PyTables)

<details><summary>README extract</summary>

PyTables is a package for managing hierarchical datasets and
designed to efficiently cope with extremely large amounts of
data. PyTables is built on top of the HDF5 library and the
NumPy package and features an object-oriented interface
that, combined with C-code generated from Cython sources,
makes of it a fast, yet extremely easy to use tool ...

</details>

### pymemcache

A comprehensive, fast, pure Python memcached client

`pip install pymemcache` · installs (wheel) · licence: Apache Software License · rank 2550 · last release 2022-10-17 · [PyPI](https://pypi.org/project/pymemcache/)

<details><summary>README extract</summary>

A comprehensive, fast, pure-Python memcached client.

pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Connections using UNIX sockets, or TCP over IPv4 or IPv6.
* Configurable timeouts for socket connect and send/recv calls. ...

Sections: pymemcache, Usage, Django, Comparison with Other Libraries, pylibmc, python-memcached, memcache_client, External Links, We're Hiring!, New in version 4.0.0, New in version 3.5.2, New in version 3.5.1, New in version 3.5.0, New in version 3.4.4

</details>

### cx-Oracle

Python interface to Oracle

`pip install cx-Oracle` · installs from source (sdist only) · licence: BSD License · rank 2594 · last release 2021-11-04 · [PyPI](https://pypi.org/project/cx-Oracle/) · [docs](http://cx-oracle.readthedocs.io) · [source](https://github.com/oracle/python-cx_Oracle)

<details><summary>README extract</summary>

cx_Oracle is a Python extension module that enables access to Oracle
Database. It conforms to the Python database API 2.0
specification with a considerable number of additions and a couple
of exclusions. See the
homepage for a
feature list.

cx_Oracle 8.3 has been tested with Python versions 3.6 through 3.10. ...

Sections: cx_Oracle version 8.3, Documentation, Samples, Help, Tests

</details>

### sqlalchemy-json

JSON type with nested change tracking for SQLAlchemy

`pip install sqlalchemy-json` · installs (wheel) · licence: BSD License · rank 2642 · last release 2023-08-30 · [PyPI](https://pypi.org/project/sqlalchemy-json/)

<details><summary>README extract</summary>

SQLAlchemy-JSON provides mutation-tracked JSON types to SQLAlchemy:

* `MutableJson` is a straightforward implementation for keeping track of top-level changes to JSON objects;
* `NestedMutableJson` is an extension of this which tracks changes even when these happen in nested objects or arrays (Python `dicts` and `lists`).

Example:
```python
class Author(Base):
    name = Column(Text)
    handles = Column(MutableJson)
```

Sections: sqlalchemy-json, Examples, Basic change tracking, Nested change tracking, Non-native JSON / other serialization types, Dependencies, 0.7.0, 0.6.0, 0.5.0, 0.4.0, 0.3.0, 0.2.2, 0.2.1

</details>

### hdbcli

SAP HANA Python Client

`pip install hdbcli` · installs (wheel) · licence: Other/Proprietary License · rank 2654 · last release 2026-09-18 · [PyPI](https://pypi.org/project/hdbcli/) · [docs](https://help.sap.com/viewer/f1b440ded6144a54ada97ff95dac7adf/latest/en-US/f3b8fabf34324302b123297cdbe710f0.html)

<details><summary>README extract</summary>

The Python Database API Specification v2.0 (PEP 249) defines a set of methods that provides a consistent database interface independent of the actual database being used. The Python extension module for SAP HANA implements PEP 249. Once you install the module, you can access and change the information in SAP HANA databases from Python. ...

Example:
```python
from hdbcli import dbapi
conn = dbapi.connect(
    address="<hostname>",
    port=3<NN>MM,
    user="<username>",
    password="<password>"
)
cursor = conn.cursor()
```

Sections: SAP HANA Python Client, Introduction, Getting Started, Quick Start, Help, Limitations of 32-bit Windows driver

</details>

### clickhouse-sqlalchemy

Simple ClickHouse SQLAlchemy Dialect

`pip install clickhouse-sqlalchemy` · installs from source (sdist only) · licence: MIT License · rank 2769 · last release 2024-06-12 · [PyPI](https://pypi.org/project/clickhouse-sqlalchemy/) · [docs](https://clickhouse-sqlalchemy.readthedocs.io)

<details><summary>README extract</summary>

ClickHouse dialect for SQLAlchemy to ClickHouse database.

Documentation is available at

Sections: ClickHouse SQLAlchemy, Documentation, Usage

</details>

### asynch

An asyncio driver for ClickHouse with native TCP support

`pip install asynch` · installs (wheel) · licence: Apache Software License · rank 2791 · last release 2026-08-14 · [PyPI](https://pypi.org/project/asynch/) · [docs](https://github.com/long2ice/asynch) · [source](https://github.com/long2ice/asynch.git)

<details><summary>README extract</summary>

`asynch` is an asynchronous ClickHouse Python driver with native TCP interface support, complying with PEP 249.

- Fast: the protocol hot path (streams, column codecs, connection, cursors) is compiled with Cython — it matches or beats clickhouse-driver, the synchronous C-extension driver, while staying fully asynchronous (see Performance) ...

Example:
```python
from asynch import Connection

# connecting with a DSN string
async def connect_database():
    async with Connection(
        dsn = "clickhouse://ch_user:P%4055w0rD@127.0.0.1:9000/chdb",
    ) as conn:
        pass
```

Sections: asynch, Introduction, Usage, Streaming results, JSON columns, Cancelling a query, Connection Pool, Query statistics, Performance, ThanksTo

</details>

### snowflake.-legacy

You should switch to the snowflake-uuid package

`pip install snowflake.-legacy` · installs (wheel) · licence: Apache Software License · rank 2967 · last release 2026-10-22 · [PyPI](https://pypi.org/project/snowflake.-legacy/)

<details><summary>README extract</summary>

Historically, the `snowflake` package on PyPI was an unrelated package owned
by an independent developer not affiliated with
Snowflake. After friendly discussion in
2023, it was agreed to transfer the PyPI `snowflake` package name to
Snowflake. ...

</details>

### snowflake

Snowflake Python API

`pip install snowflake` · installs (wheel) · licence: Apache Software License · rank 2969 · last release 2026-10-22 · [PyPI](https://pypi.org/project/snowflake/)

<details><summary>README extract</summary>

The Snowflake Python API is the unified Python API across all Snowflake workloads, providing APIs for all Snowflake resources across data engineering, Snowpark, Snowpark ML, and client application workloads.

The `snowflake` package is the PEP 420 namespace parent package for the Snowflake Python API, including Snowpark. ...

</details>

### DBUtils

Database connections for multi-threaded environments.

`pip install DBUtils` · installs (wheel) · licence: MIT · rank 2985 · last release 2026-08-21 · [PyPI](https://pypi.org/project/DBUtils/) · [docs](https://webwareforpython.github.io/DBUtils/main.html) · [source](https://github.com/WebwareForPython/DBUtils)

<details><summary>README extract</summary>

DBUtils is a suite of tools providing solid, persistent and pooled connections
to a database that can be used in all kinds of multi-threaded environments.

The suite supports DB-API 2 compliant database interfaces
and the classic PyGreSQL interface.

The current version 3.2.0 of DBUtils supports Python versions 3.7 to 3.14. ...

</details>

### beanie

Asynchronous Python ODM for MongoDB

`pip install beanie` · does not install on CPython 3.14 · licence: Apache Software License · rank 3203 · last release 2026-08-07 · [PyPI](https://pypi.org/project/beanie/) · [source](https://github.com/BeanieODM/beanie)

<details><summary>README extract</summary>

Features:
Beanie - is an asynchronous Python object-document mapper (ODM) for MongoDB. Data models are based on Pydantic.

When using Beanie each database collection has a corresponding `Document` that
is used to interact with that collection. ...

Example:
```python
import asyncio
from typing import Optional

from pymongo import AsyncMongoClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie

class Category(BaseModel):
    name: str
    description: str

class Product(Document):
    name: str                          # You can use normal types just like in pydantic
...
```

Sections: Overview, PIP, Poetry, Example, Links, Documentation, Example Projects, Articles, Resources

</details>

### PySide6-WebEngine

Python bindings for the Qt cross-platform application and UI framework (WebEngine)

`pip install PySide6-WebEngine` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 3234 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PySide6-WebEngine/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### PySide6-Pdf

Python bindings for the Qt cross-platform application and UI framework (Pdf)

`pip install PySide6-Pdf` · installs (wheel) · licence: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only · rank 3290 · last release 2026-10-08 · [PyPI](https://pypi.org/project/PySide6-Pdf/) · [docs](https://doc.qt.io/qtforpython) · [source](https://code.qt.io/cgit/pyside/pyside-setup.git/)

_README extract left out: share-alike licence._

### PyStemmer

Snowball stemming algorithms, for information retrieval

`pip install PyStemmer` · installs (wheel) · licence: BSD License; MIT License · rank 3408 · last release 2026-05-22 · [PyPI](https://pypi.org/project/PyStemmer/)

<details><summary>README extract</summary>

Stemming algorithms

PyStemmer provides access to efficient algorithms for calculating a
"stemmed" form of a word. This is a form with most of the common
morphological endings removed; hopefully representing a common
linguistic base form. ...

</details>

### mongoengine

MongoEngine is a Python Object-Document Mapper for working with MongoDB.

`pip install mongoengine` · installs (wheel) · licence: MIT License · rank 3424 · last release 2026-03-10 · [PyPI](https://pypi.org/project/mongoengine/)

<details><summary>README extract</summary>

:Info: MongoEngine is an ORM-like layer on top of PyMongo.
:Repository:
:Author: Harry Marr (
:Maintainer: Bastien Gerard (

MongoEngine is a Python Object-Document Mapper for working with MongoDB.
Documentation is available at - there
is currently a tutorial,
a user guide, and
an API reference.

Sections: MongoEngine, About, Dependencies, Examples, Tests

</details>

### psycopg-c

PostgreSQL database adapter for Python -- C optimisation distribution

`pip install psycopg-c` · installs from source (sdist only) · licence: LGPL-3.0-only · rank 3476 · last release 2026-11-04 · [PyPI](https://pypi.org/project/psycopg-c/) · [docs](https://psycopg.org/psycopg3/docs/) · [source](https://github.com/psycopg/psycopg)

_README extract left out: share-alike licence._

### aioodbc

ODBC driver for asyncio.

`pip install aioodbc` · installs (wheel) · licence: Apache Software License · rank 3558 · last release 2023-10-28 · [PyPI](https://pypi.org/project/aioodbc/) · [docs](https://uddsketch.readthedocs.io)

<details><summary>README extract</summary>

aioodbc is a Python 3.7+ module that makes it possible to access ODBC databases
with asyncio. It relies on the awesome pyodbc library and preserves the same look and
feel. Internally *aioodbc* employs threads to avoid blocking the event loop,
threads are not that as bad as you think!. Other drivers like motor use the
same approach. ...

Example:
```python
import asyncio

import aioodbc

async def test_example():
    dsn = "Driver=SQLite;Database=sqlite.db"
    conn = await aioodbc.connect(dsn=dsn)

    cur = await conn.cursor()
    await cur.execute("SELECT 42 AS age;")
    rows = await cur.fetchall()
    print(rows)
    print(rows[0])
    print(rows[0].age)
    await cur.close()
...
```

...

</details>

### vertica-python

Official native Python client for the Vertica database.

`pip install vertica-python` · installs (wheel) · licence: Apache Software License · rank 3635 · last release 2024-07-22 · [PyPI](https://pypi.org/project/vertica-python/)

<details><summary>README extract</summary>

vertica-python is the official Vertica database client for the Python programming language. Please check the project homepage for the details.

</details>

### pinecone-client

Pinecone client (DEPRECATED)

`pip install pinecone-client` · installs (wheel) · licence: Apache Software License · rank 3669 · last release 2025-02-21 · [PyPI](https://pypi.org/project/pinecone-client/) · [docs](https://pinecone.io/docs)

<details><summary>README extract</summary>

The official Pinecone python package has been renamed from `pinecone-client` to `pinecone`. To upgrade, please
remove `pinecone-client` from your project dependencies and then add the `pinecone` package to get the
latest updates. ...

Sections: Pinecone Python Client (DEPRECATED), Upgrade steps, Links

</details>

### intersystems-irispython

InterSystems IRIS Python SDK Kit

`pip install intersystems-irispython` · installs (wheel) · licence: LicenseRef-InterSystems-External-Repository · rank 3710 · last release 2026-10-08 · [PyPI](https://pypi.org/project/intersystems-irispython/) · [docs](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=PAGE_python_native)

<details><summary>README extract</summary>

Example:
```python
import iris

# Open a connection to the server
args = {
    'hostname':'127.0.0.1',
    'port': 1972,
    'namespace':'USER',
    'username':'username',
    'password':'password'
}
conn = iris.connect(**args)

# Create an iris object
irispy = iris.createIRIS(conn)

# Create a global array in the USER namespace on the server
...
```

Sections: intersystems-irispython, Usage, Native Connections, Using DB-API, Documentation, Help, Version 5.4.1, Version 5.4.0, Version 5.3.2, Version 5.3.1, Version 5.3.0, Version 5.2.1, Version 5.2.0, Version 5.1.2

</details>

### psycogreen

psycopg2 integration with coroutine libraries

`pip install psycogreen` · installs from source (sdist only) · licence: BSD License · rank 3739 · last release 2020-02-22 · [PyPI](https://pypi.org/project/psycogreen/)

<details><summary>README extract</summary>

The psycogreen package enables psycopg2 to work with coroutine libraries,
using asynchronous calls internally but offering a blocking interface so that
regular code can run unmodified.

Psycopg offers coroutines support since release 2.2. Because the main
module is a C extension it cannot be monkey-patched to become
coroutine-friendly. ...

Sections: psycogreen -- psycopg2 integration with coroutine libraries, Module `psycogreen.eventlet`, Module `psycogreen.gevent`, uWSGI green threads

</details>

### valkey-glide

Valkey GLIDE Async client. Supports Valkey and Redis OSS.

`pip install valkey-glide` · installs (wheel) · licence: Apache Software License · rank 3748 · last release 2026-11-06 · [PyPI](https://pypi.org/project/valkey-glide/)

<details><summary>README extract</summary>

Valkey General Language Independent Driver for the Enterprise (GLIDE) is the official open-source Valkey client library, proudly part of the Valkey organization. Our mission is to make your experience with Valkey and Redis OSS seamless and enjoyable. ...

Features:
- Community and Open Source: Join our vibrant community and contribute to the project. We are always here to respond, and the client is for the community. ...

Example:
```python
import asyncio
from glide import GlideClusterClientConfiguration, NodeAddress, GlideClusterClient

async def test_cluster_client():
    addresses = [NodeAddress("address.example.com", 6379)]
    # It is recommended to set a timeout for your specific use case
...
```

...

</details>

### testing.common.database

utilities for testing.* packages

`pip install testing.common.database` · installs (wheel) · licence: Apache Software License · rank 3934 · last release 2017-10-23 · [PyPI](https://pypi.org/project/testing.common.database/)

<details><summary>README extract</summary>

`testing.common.database` is utilities for testing.* package.

Example:
```python
      def get_data_directory(self):
          return os.path.join(self.base_dir, 'data')

def initialize_database(self):

    Handler to initialize your database.

    Example::

      def initialize_database(self):
         if not os.path.exists(os.path.join(self.base_dir, 'data', 'PG_VERSION')):
...
```

Sections: About, Helpers, Requirements, 2.0.3 (2017-10-24), 2.0.2 (2017-10-08), 2.0.1 (2017-07-15), 2.0.0 (2016-08-20), 1.1.0 (2016-02-05), 1.0.0 (2016-02-01)

</details>

### upstash-redis

Serverless Redis SDK from Upstash

`pip install upstash-redis` · installs (wheel) · licence: MIT License · rank 3982 · last release 2026-11-02 · [PyPI](https://pypi.org/project/upstash-redis/) · [source](https://github.com/upstash/redis-python)

<details><summary>README extract</summary>

> [!NOTE]
> This project is in GA Stage.
> The Upstash Professional Support fully covers this project. It receives regular updates, and bug fixes. The Upstash team is committed to maintaining and improving its functionality. ...

Example:
```python
# for sync client
from upstash_redis import Redis

redis = Redis(url="UPSTASH_REDIS_REST_URL", token="UPSTASH_REDIS_REST_TOKEN")

# for async client
from upstash_redis.asyncio import Redis

redis = Redis(url="UPSTASH_REDIS_REST_URL", token="UPSTASH_REDIS_REST_TOKEN")
```

Sections: Upstash Redis Python SDK, Quick Start, PyPI, Usage, BITFIELD and BITFIELD_RO, Redis Streams, Vector indexes, Arrays, Custom commands, Pipelines & Transactions, Telemetry, Encoding, Retry mechanism, Preparing the environment

</details>

### pymongocrypt

Python bindings for libmongocrypt

`pip install pymongocrypt` · installs (wheel) · licence: Apache Software License · rank 4023 · last release 2026-10-15 · [PyPI](https://pypi.org/project/pymongocrypt/)

<details><summary>README extract</summary>

:Info: Python bindings for libmongocrypt. See
 GitHub
 for the latest source.
:Author: Shane Harvey

Python wrapper library for libmongocrypt that supports client side encryption
in drivers. PyMongoCrypt uses cffi and
cryptography.

PyMongoCrypt supports Python 3.11+.

Example:
```python
$ python -c "import sys; print(sys.version)"
```

Sections: PyMongoCrypt, About, Bugs / Feature Requests, How To Ask For Help, Dependencies

</details>

### datacontract-cli

The datacontract CLI is an open source command-line tool for working with Data Contracts. It uses data contract YAML files to lint the data contract, connect to data sources and execute schema and quality tests, detect breaking changes, and export to different formats. The tool is written in Python. It can be used as a standalone CLI tool, in a CI/CD pipeline, or directly as a Python library.

`pip install datacontract-cli` · installs (wheel) · licence: MIT · rank 4029 · last release 2026-10-30 · [PyPI](https://pypi.org/project/datacontract-cli/) · [docs](https://cli.datacontract.com) · [source](https://github.com/datacontract/datacontract-cli)

<details><summary>README extract</summary>

Turn your schemas into data contracts and test your data against them, on Snowflake, Databricks, BigQuery, Kafka, Postgres & 15 more. Open source, built on the Open Data Contract Standard.
The `datacontract` CLI is an open-source command-line tool for working with data contracts. ...

Example:
```python
from datacontract.data_contract import DataContract

data_contract = DataContract(data_contract_file="odcs.yaml")
run = data_contract.test()
if not run.has_passed():
    print("Data quality validation failed.")
    # Abort pipeline, alert, or take corrective actions...
```

Sections: Data Contract CLI, Getting started, Usage, Programmatic (Python), How to, uv, uvx, pip, pip with venv, pipx, Docker, Optional Dependencies (Extras), Documentation, Troubleshooting

</details>

### mysql-connector

MySQL driver written in Python

`pip install mysql-connector` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 4097 · last release 2019-04-01 · [PyPI](https://pypi.org/project/mysql-connector/)

_README extract left out: share-alike licence._

### rocksdict

Rocksdb Python Binding

`pip install rocksdict` · installs (wheel) · licence: MIT License · rank 4146 · last release 2025-12-01 · [PyPI](https://pypi.org/project/rocksdict/)

<details><summary>README extract</summary>

Key-value storage for Python & Wrapper of Rocksdb and Speedb

Example:
```python
from rocksdict import Rdict
import numpy as np
import pandas as pd

path = str("./test_dict")

# create a Rdict with default options at `path`
db = Rdict(path)
db[1.0] = 1
db["huge integer"] = 2343546543243564534233536434567543
db["good"] = True
db["bytes"] = b"bytes"
db["this is a list"] = [1, 2, 3]
db["store a dict"] = {0: 1}
...
```

Sections: RocksDict / SpeeDict, Introduction, Examples, A minimal example, An Example of Raw Mode, New Feature Since v0.3.3, Load Options and add A New ColumnFamily, Reopening RocksDB Reads DB Options Automatically, Limitations, Full Documentation

</details>

### sqlite-utils

CLI tool and Python library for manipulating SQLite databases

`pip install sqlite-utils` · installs (wheel) · licence: Apache-2.0 · rank 4168 · last release 2026-08-13 · [PyPI](https://pypi.org/project/sqlite-utils/) · [docs](https://sqlite-utils.datasette.io/en/stable/)

<details><summary>README extract</summary>

Python CLI utility and library for manipulating SQLite databases.

- Pipe JSON (or CSV or TSV) directly into a new SQLite database file, automatically creating a table with the appropriate schema
- Run in-memory SQL queries, including joins, directly against data in CSV, TSV or JSON files and view the results ...

Example:
```python
import sqlite_utils
db = sqlite_utils.Database("demo_database.db")
# This line creates a "dogs" table if one does not already exist:
db["dogs"].insert_all([
    {"id": 1, "age": 4, "name": "Cleo"},
    {"id": 2, "age": 2, "name": "Pancakes"}
], pk="id")
```

Sections: sqlite-utils, Some feature highlights, Using as a CLI tool, Using as a library, Related projects

</details>

### testing.postgresql

automatically setups a postgresql instance in a temporary directory, and destroys it after testing

`pip install testing.postgresql` · installs (wheel) · licence: Apache Software License · rank 4216 · last release 2016-02-04 · [PyPI](https://pypi.org/project/testing.postgresql/)

<details><summary>README extract</summary>

`testing.postgresql` automatically setups a postgresql instance in a temporary directory, and destroys it after testing.

Documentation

Issues

Download

Example:
```python
import testing.postgresql
from sqlalchemy import create_engine

# Lanuch new PostgreSQL server
with testing.postgresql.Postgresql() as postgresql:
    # connect to PostgreSQL
    engine = create_engine(postgresql.url())

    # if you use postgresql or other drivers:
    #   import psycopg2
    #   db = psycopg2.connect(**postgresql.dsn())

    #
...
```

Sections: About, Usage, To make your tests faster, Requirements, 1.3.0 (2016-02-03), 1.2.1 (2015-08-22), 1.2.0 (2015-05-17), 1.1.2 (2015-04-06), 1.1.1 (2015-01-18), 1.1.0 (2014-12-20), 1.0.6 (2014-07-19), 1.0.5 (2014-07-19), 1.0.4 (2014-06-19), 1.0.3 (2014-06-11)

</details>

### gdbmongo

GDB pretty printers and commands for debugging the MongoDB Server

`pip install gdbmongo` · installs (wheel) · licence: Apache Software License · rank 4238 · last release 2025-02-13 · [PyPI](https://pypi.org/project/gdbmongo/)

<details><summary>README extract</summary>

The *gdbmongo* package contains GDB pretty printers and commands for
debugging the MongoDB Server. Its primary target audience is MongoDB
employees.

The *gdbmongo* package is mostly born out of joy from tinkering with
low-level constructs while writing GDB pretty printers. There are some
explicit areas for what it aims to achieve:

1. ...

Example:
```python
(gdb) python lock_mgr = gdbmongo.LockManagerPrinter.from_global()
(gdb) python print(lock_mgr.val)
```

Sections: gdb-mongodb-server, About, Motivation, Usage, 0.16.0 (2025-02-13), 0.15.2 (2025-02-02), 0.15.1 (2024-05-19), 0.15.0 (2024-04-29), 0.14.0 (2023-09-30), 0.13.0 (2023-09-29), 0.12.0 (2023-09-22), 0.11.0 (2023-09-16), 0.10.0 (2023-09-03), 0.9.0 (2023-08-26)

</details>

### mssql-python-rs

Rust-based native runtime (TDS core and ODBC driver) consumed by the mssql-python driver.

`pip install mssql-python-rs` · installs (wheel) · licence: MIT License · rank 4316 · last release 2026-10-31 · [PyPI](https://pypi.org/project/mssql-python-rs/) · [source](https://github.com/microsoft/mssql-rs)

<details><summary>README extract</summary>

<!--
Published verbatim as the mssql-python-rs PyPI project description (see
`readme` in pyproject.toml); it is republished on the next release. Keep the
content user-facing and every link absolute: repo-relative links do not
resolve on PyPI.

Native runtime for the
`mssql-python` SQL Server and
Azure SQL driver. ...

Sections: mssql-python-rs, Bulk-copy datetime strings, Platforms, Native connection settings

</details>

### hmsclient

A package interact with the Hive metastore via the Thrift protocol

`pip install hmsclient` · installs (wheel) · licence: Apache Software License · rank 4317 · last release 2018-04-24 · [PyPI](https://pypi.org/project/hmsclient/)

<details><summary>README extract</summary>

This project aims to be an up to date Python client to interact with the Hive metastore
using the Thrift protocol.

Example:
```python
from hmsclient import hmsclient
client = hmsclient.HMSClient(host='localhost', port=9083)
with client as c:
    c.check_for_named_partition('db', 'table', 'date=20180101')
```

Sections: HMSClient, Usage, Regenerate the Python thrift library

</details>

### yoyo-migrations

Database migrations with SQL

`pip install yoyo-migrations` · installs (wheel) · licence: Apache Software License · rank 4342 · last release 2024-08-10 · [PyPI](https://pypi.org/project/yoyo-migrations/)

<details><summary>README extract</summary>

Yoyo-migrations is a database schema migration tool.
Database migrations can be written as SQL files or Python scripts.

As your database application evolves, changes to the database schema may be
required. Yoyo lets you write migration scripts in raw SQL or Python containing
SQL statements to migrate your database schema to a new version. ...

Example:
```python
# file: migrations/0001.create-foo.py
from yoyo import step
step(
    "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
    "DROP TABLE foo",
)
```

Sections: Yoyo database migrations, What does yoyo-migrations do?, Documentation and code

</details>

### sqlite-anyio

Asynchronous client for SQLite using AnyIO

`pip install sqlite-anyio` · installs (wheel) · licence: MIT License · rank 4410 · last release 2026-08-06 · [PyPI](https://pypi.org/project/sqlite-anyio/) · [source](https://github.com/davidbrochart/sqlite-anyio)

### milvus-lite

Lightweight version of Milvus for local development and testing

`pip install milvus-lite` · installs (wheel) · licence: Apache Software License · rank 4416 · last release 2026-10-13 · [PyPI](https://pypi.org/project/milvus-lite/) · [source](https://github.com/milvus-io/milvus-lite)

<details><summary>README extract</summary>

Features:
- Drop-in local usage with `MilvusClient("./demo.db")`.
- Pure Python implementation with inspectable code and Python stack traces.
- Dense vector search, exact sparse inner-product search, BM25 text search, and hybrid search. ...

Example:
```python
from pymilvus import MilvusClient

client = MilvusClient("./demo.db")

client.create_collection(
    collection_name="docs",
    dimension=4,
)

data = [
    {"id": 1, "vector": [0.1, 0.2, 0.3, 0.4], "text": "python tutorial", "category": "tech"},
    {"id": 2, "vector": [0.2, 0.1, 0.4, 0.3], "text": "machine learning", "category": "ai"},
...
```

...

</details>

### snowflake-cli

Snowflake CLI

`pip install snowflake-cli` · installs (wheel) · licence: Apache Software License · rank 4473 · last release 2026-11-02 · [PyPI](https://pypi.org/project/snowflake-cli/) · [source](https://github.com/snowflakedb/snowflake-cli)

<details><summary>README extract</summary>

<!--
 Copyright (c) 2024 Snowflake Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

Sections: Snowflake CLI, Customize the SQL REPL prompt, Default output format, Get involved

</details>

### alembic-git-revisions

Automatic Alembic migration chaining based on git commit history

`pip install alembic-git-revisions` · installs (wheel) · licence: Apache-2.0 · rank 4572 · last release 2026-09-24 · [PyPI](https://pypi.org/project/alembic-git-revisions/) · [source](https://github.com/Mergifyio/alembic-git-revisions)

<details><summary>README extract</summary>

Automatic Alembic migration chaining based on git commit history. No more `Multiple head revisions are present for given argument 'head'`.

You merged two branches and Alembic now refuses to run: ...

Sections: alembic-git-revisions, The problem, How it works, Setup, Environments without git (Docker, CI), How migrations are classified, API, `get_down_revision(revision, versions_dir=None)`, `generate_chain_file(versions_dir)`, `build_chain(versions_dir)`, `parse_versions_dir(versions_dir)`, `MigrationFile`, `CHAIN_FILENAME`

</details>

### valkey-glide-sync

Valkey GLIDE Sync client. Supports Valkey and Redis OSS.

`pip install valkey-glide-sync` · installs (wheel) · licence: Apache-2.0 · rank 4870 · last release 2026-11-06 · [PyPI](https://pypi.org/project/valkey-glide-sync/)

<details><summary>README extract</summary>

Valkey General Language Independent Driver for the Enterprise (GLIDE) is the official open-source Valkey client library, proudly part of the Valkey organization. Our mission is to make your experience with Valkey and Redis OSS seamless and enjoyable. ...

Features:
- Community and Open Source: Join our vibrant community and contribute to the project. We are always here to respond, and the client is for the community. ...

Example:
```python
import asyncio
from glide import GlideClusterClientConfiguration, NodeAddress, GlideClusterClient

async def test_cluster_client():
    addresses = [NodeAddress("address.example.com", 6379)]
    # It is recommended to set a timeout for your specific use case
...
```

...

</details>

### advanced-alchemy

Ready-to-go SQLAlchemy concoctions.

`pip install advanced-alchemy` · installs (wheel) · licence: MIT License · rank 5005 · last release 2026-10-19 · [PyPI](https://pypi.org/project/advanced-alchemy/) · [docs](https://advanced-alchemy.litestar.dev/latest/) · [source](https://github.com/litestar-org/advanced-alchemy)

<details><summary>README extract</summary>

| Project | Status |

| CI/CD | |
| Quality | |
| Package | |
| Community | |
| Meta | |

Check out the project documentation 📚 for more information.

A carefully crafted, thoroughly tested, optimized companion library for SQLAlchemy,
offering:

- Sync and async repositories, featuring common CRUD and highly optimized bulk operations ...

Example:
```python
from advanced_alchemy import base, repository, config
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, sessionmaker

class User(base.UUIDBase):
    # you can optionally override the generated table name by manually setting it.
    tablename = "user_account"  # type: ignore[assignment]
    email: Mapped[str]
...
```

...

</details>

### django-mysql

Django-MySQL extends Django's built-in MySQL and MariaDB support their specific features not available on other databases.

`pip install django-mysql` · installs (wheel) · licence: MIT · rank 5176 · last release 2025-09-18 · [PyPI](https://pypi.org/project/django-mysql/) · [docs](https://django-mysql.readthedocs.io/) · [source](https://github.com/adamchainz/django-mysql)

<details><summary>README extract</summary>

Django-MySQL extends Django's built-in MySQL and MariaDB support their specific
features not available on other databases.

Includes:

 * 'Smart' iteration - chunked pagination across a large queryset
 * `approx_count` for quick estimates of `count()`
 * Query hints
 * Quick `pt-visual-explain` of the underlying query ...

Sections: Django-MySQL, What kind of features?, Documentation

</details>

### pony

Pony Object-Relational Mapper

`pip install pony` · installs (wheel) · licence: Apache-2.0 · rank 5228 · last release 2026-08-09 · [PyPI](https://pypi.org/project/pony/) · [docs](https://docs.ponyorm.org) · [source](https://github.com/ponyorm/pony)

<details><summary>README extract</summary>

Pony is an advanced object-relational mapper. The most interesting feature of Pony is its ability to write queries to the database using Python generator expressions and lambdas. Pony analyzes the abstract syntax tree of the expression and translates it into a SQL query.

Here is an example query in Pony: ...

Example:
```python
select(p for p in Product if p.name.startswith('A') and p.cost <= 1000)
```

Sections: Downloads, Pony Object-Relational Mapper

</details>

### pyexasol

Exasol python driver with extra features

`pip install pyexasol` · installs (wheel) · licence: MIT · rank 5241 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pyexasol/) · [docs](https://github.com/exasol/pyexasol/) · [source](https://github.com/exasol/pyexasol)

<details><summary>README extract</summary>

PyExasol is the officially supported Python connector for Exasol. It helps to handle massive volumes of data commonly associated with this DBMS.

You may expect significant performance improvement over ODBC in a single process scenario involving pandas, parquet, or polars. ...

Sections: PyExasol, PyExasol Main Concepts, System Requirements, Getting Started

</details>

### tortoise-orm

Easy async ORM for python, built with relations in mind

`pip install tortoise-orm` · installs (wheel) · licence: Apache Software License · rank 5314 · last release 2026-10-14 · [PyPI](https://pypi.org/project/tortoise-orm/) · [docs](https://tortoise.github.io) · [source](https://github.com/tortoise/tortoise-orm.git)

<details><summary>README extract</summary>

Tortoise ORM is an easy-to-use `asyncio` ORM *(Object Relational Mapper)* inspired by Django.

You can find the docs at Documentation

Tortoise ORM supports CPython 3.10 and later for SQLite, MySQL, PostgreSQL, Microsoft SQL Server, and Oracle.

Features:
Tortoise ORM was built to provide a lightweight, async-native Object-Relational Mapper for Python with a familiar Django-like API.

Tortoise ORM performs well when compared to other Python ORMs. ...

Example:
```python
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=20)

class Event(Model):
    id = fields.BigIntField(primary_key=True)
    name = fields.TextField()
...
```

...

</details>

### cacheout

A caching library for Python

`pip install cacheout` · installs (wheel) · licence: MIT · rank 5396 · last release 2026-10-03 · [PyPI](https://pypi.org/project/cacheout/) · [docs](https://cacheout.readthedocs.org) · [source](https://github.com/dgilland/cacheout)

<details><summary>README extract</summary>

A caching library for Python.

Features:
- In-memory caching using dictionary backend
- Cache manager for easily accessing multiple cache objects
- Reconfigurable cache settings for runtime setup when using module-level cache objects
- Maximum cache size enforcement ...

Example:
```python
from cacheout import Cache

cache = Cache()
```

Sections: cacheout, Links, Features, Roadmap, Requirements, Quickstart

</details>

### pgqueuer

PostgreSQL-backed background job and task queue for Python.

`pip install pgqueuer` · installs (wheel) · licence: MIT License · rank 5408 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pgqueuer/) · [docs](https://janbjorge.github.io/pgqueuer/) · [source](https://github.com/janbjorge/pgqueuer/)

<details><summary>README extract</summary>

📚 Docs · 💻 Source · 💬 Discord

Your PostgreSQL database is already a job queue.

PgQueuer turns PostgreSQL into a fast, reliable background job processor. Jobs live in the same database as your application data. One stack, full ACID guarantees, and no separate message broker to run. ...

Features:
- 💡 Minimal footprint: one `pip install`; bring your existing PostgreSQL connection and start enqueueing
- 🔁 Transactional enqueue: commit a job in the same transaction as your data; no dual-write drift ...

Example:
```python
import asyncpg
from pgqueuer import PgQueuer
from pgqueuer.db import AsyncpgDriver
from pgqueuer.models import Job

async def main() -> PgQueuer:
    connection = await asyncpg.connect()
    pgq = PgQueuer(AsyncpgDriver(connection))

    @pgq.entrypoint("fetch")
...

</details>

### sqloxide

Python bindings for sqlparser-rs

`pip install sqloxide` · installs (wheel) · licence: MIT · rank 5554 · last release 2026-04-06 · [PyPI](https://pypi.org/project/sqloxide/) · [source](https://github.com/wseaton/sqloxide)

### piccolo

A fast, user friendly ORM and query builder which supports asyncio.

`pip install piccolo` · installs (wheel) · licence: MIT License · rank 5640 · last release 2026-10-28 · [PyPI](https://pypi.org/project/piccolo/) · [docs](https://piccolo-orm.readthedocs.io/en/latest/index.html) · [source](https://github.com/piccolo-orm/piccolo)

<details><summary>README extract</summary>

Piccolo is a fast, user friendly ORM and query builder which supports asyncio. Read the docs.

Features:
Some of it’s stand out features are:

- Support for sync and async.
- A builtin playground, which makes learning a breeze.
- Tab completion support - works great with iPython and VSCode. ...

Example:
```python
# Select:
await Band.select(
    Band.name
).where(
    Band.popularity > 100
)

# Join:
await Band.select(
    Band.name,
    Band.manager.name
)

# Delete:
await Band.delete().where(
    Band.popularity < 1000
)

# Update:
await Band.update({Band.popularity: 10000}).where(
    Band.name == 'Pythonistas'
)
```

Sections: Features, Syntax, Building a web app?, Piccolo ecosystem, Piccolo Admin, Piccolo API, Are you a Django user?, Documentation

</details>

### aiopg

Postgres integration with asyncio.

`pip install aiopg` · installs (wheel) · licence: BSD License · rank 5767 · last release 2022-10-26 · [PyPI](https://pypi.org/project/aiopg/)

<details><summary>README extract</summary>

aiopg is a library for accessing a PostgreSQL database
from the asyncio (PEP-3156/tulip) framework. It wraps
asynchronous features of the Psycopg database driver.

Example:
```python
import asyncio
import aiopg

dsn = 'dbname=aiopg user=aiopg password=passwd host=127.0.0.1'

async def go():
    pool = await aiopg.create_pool(dsn)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")
            ret = []
            async for row in cur:
...
```

...

</details>

### transaction

Transaction management for Python

`pip install transaction` · installs (wheel) · licence: ZPL-2.1 · rank 5796 · last release 2026-03-17 · [PyPI](https://pypi.org/project/transaction/) · [docs](https://transaction.readthedocs.io/) · [source](https://github.com/zopefoundation/transaction)

<details><summary>README extract</summary>

This package contains a generic transaction implementation for Python. It is
mainly used by the ZODB.

See for narrative documentation
on its usage.

- Move package metadata from setup.py to pyproject.toml.

- Add support for Python 3.14.

- Drop support for Python 3.8, 3.9.

Example:
```python
   for attempt in transaction.attempts(5):
       with attempt:
           ... do some things ..

If the work being done raises transient errors, the transaction will
be retried up to 5 times.

See transaction/tests/convenience.txt for more details.
```

...

</details>

### rapids-logger

Logging framework for RAPIDS built around spdlog

`pip install rapids-logger` · installs (wheel) · licence: Apache-2.0 · rank 5911 · last release 2026-08-04 · [PyPI](https://pypi.org/project/rapids-logger/)

<details><summary>README extract</summary>

The `rapids-logger` project defines an easy way to produce a project-specific logger using the excellent spdlog package.
This project has two primary goals:
1. Ensure that projects wishing to provide their own logger may do so easily without needing to reimplement their own custom wrappers around spdlog.
2. ...

Example:
```python
RAPIDS_LOG_DEBUG("Some message to be shown when the debug level is enabled");
```

</details>

### sqlcipher3

DB-API 2.0 interface for SQLCipher 4.x

`pip install sqlcipher3` · installs (wheel) · licence: not stated · rank 6052 · last release 2026-11-05 · [PyPI](https://pypi.org/project/sqlcipher3/) · [source](https://github.com/coleifer/sqlcipher3)

<details><summary>README extract</summary>

This library takes pysqlite3 and makes
some small modifications so it is suitable for use with
sqlcipher (sqlite with encryption).

Additional features:

* User-defined window functions (requires SQLite >= 3.25)
* Flags and VFS an be specified when opening connection
* Incremental BLOB I/O, bpo-24905
* Improved error messages, bpo-16379
* ...

</details>

### couchbase

Python Client for Couchbase

`pip install couchbase` · installs (wheel) · licence: Apache Software License · rank 6062 · last release 2026-10-28 · [PyPI](https://pypi.org/project/couchbase/)

<details><summary>README extract</summary>

Python client for Couchbase
>NOTE: This is the documentation for the 4.x version of the client. This is mostly compatible with the older 3.x version. Please refer to the *release32* branch for the older 3.x version.

Example:
```python
import logging
from couchbase import configure_logging

configure_logging('my_app', level=logging.DEBUG)
```

Sections: Couchbase Python Client, Prerequisites, Debian and Ubuntu, RHEL and CentOS, Mac OS, pyenv, Homebrew, Windows, Anaconda/Miniconda, Building

</details>

### mariadb

Python MariaDB extension

`pip install mariadb` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 6181 · last release 2025-10-07 · [PyPI](https://pypi.org/project/mariadb/) · [docs](https://mariadb-corporation.github.io/mariadb-connector-python/) · [source](https://www.github.com/mariadb-corporation/mariadb-connector-python)

_README extract left out: share-alike licence._

### plyvel

Plyvel, a fast and feature-rich Python interface to LevelDB

`pip install plyvel` · installs from source (sdist only) · licence: BSD License · rank 6184 · last release 2024-01-15 · [PyPI](https://pypi.org/project/plyvel/)

<details><summary>README extract</summary>

Plyvel is a fast and feature-rich Python interface to LevelDB.

Plyvel has a rich feature set, high performance, and a friendly Pythonic API.
See the documentation and project page for more information:

* Documentation
* Project page
* PyPI page

Note that using a released version is recommended over a checkout from version
control. ...

</details>

### vortex-data

Python bindings for Vortex, an Apache Arrow-compatible toolkit for working with compressed array data.

`pip install vortex-data` · installs (wheel) · licence: Apache Software License · rank 6255 · last release 2026-11-06 · [PyPI](https://pypi.org/project/vortex-data/) · [docs](https://docs.vortex.dev)

<details><summary>README extract</summary>

Join the community on Slack! | Documentation | Performance Benchmarks

If you are interested in closer collaboration, please email info@vortex.dev

Features:
Vortex is a next-generation columnar file format and toolkit designed for high-performance data processing.
It is the fastest and most extensible format for building data systems backed by object storage. It provides: ...

Sections: 🌪️ Vortex, Overview, Key Features, Core Capabilities, Technical Architecture, Logical vs Physical Design, Quick Start, Rust Crate, Python Package, Command Line UI (vx), Prerequisites (macOS), Benchmarking, Performance Optimization, Project Information

</details>

### queries

Simplified PostgreSQL client built upon Psycopg2

`pip install queries` · installs from source (sdist only) · licence: BSD License · rank 6270 · last release 2021-11-16 · [PyPI](https://pypi.org/project/queries/)

<details><summary>README extract</summary>

*Queries* is a BSD licensed opinionated wrapper of the psycopg2 library for
interacting with PostgreSQL.

The popular psycopg2 package is a full-featured python client. Unfortunately
as a developer, you're often repeating the same steps to get started with your
applications that use it. ...

Example:
```python
session = queries.Session("postgresql://postgres@localhost:5432/postgres")
```

Sections: Queries: PostgreSQL Simplified, Documentation, Usage, Environment Variables, Using the queries.Session class, Inspiration

</details>

### aerospike

Aerospike Client Library for Python

`pip install aerospike` · installs (wheel) · licence: Apache Software License · rank 6308 · last release 2026-09-25 · [PyPI](https://pypi.org/project/aerospike/)

<details><summary>README extract</summary>

The Python client for Aerospike works with Python 3.10 - 3.14 and supports the following OS'es:

* macOS 14, 15, 26
* RHEL 9 and 10
* Amazon Linux 2023
* Debian 12 and 13
* Ubuntu 22.04 and 24.04
* Windows (x64) ...

Sections: Aerospike Python Client, Compatibility, Troubleshooting, Troubleshooting macOS, Build, Documentation, Examples, Benchmarks

</details>

### sqlalchemy-hana

SQLAlchemy dialect for SAP HANA

`pip install sqlalchemy-hana` · installs (wheel) · licence: Apache-2.0 · rank 6380 · last release 2026-10-02 · [PyPI](https://pypi.org/project/sqlalchemy-hana/) · [source](https://github.com/SAP/sqlalchemy-hana)

<details><summary>README extract</summary>

This dialect allows you to use the SAP HANA database with SQLAlchemy.
It uses `hdbcli` to connect to SAP HANA.
Please notice that sqlalchemy-hana isn't an official SAP product and isn't covered by SAP support.

* Python 3.11+
* SQLAlchemy 2.x
* hdbcli

Example:
```python
from sqlalchemy import create_engine
engine = create_engine('hana://username:password@example.de:30015')
```

Sections: SQLAlchemy dialect for SAP HANA, Prerequisites, Versioning, Getting started, Usage, Special CREATE TABLE argument, Case Sensitivity, Reflection, Foreign Key Constraints, UNIQUE Constraints, Data types, Real Vector, Regex, Bound Parameter Styles

</details>

### qstash

Python SDK for Upstash QStash

`pip install qstash` · installs (wheel) · licence: MIT License · rank 6385 · last release 2026-03-18 · [PyPI](https://pypi.org/project/qstash/) · [source](https://github.com/upstash/qstash-py)

<details><summary>README extract</summary>

> [!NOTE]
> This project is in GA Stage.
> The Upstash Professional Support fully covers this project. It receives regular updates, and bug fixes.
> The Upstash team is committed to maintaining and improving its functionality.

QStash is an HTTP based messaging and scheduling solution for serverless and edge runtimes.

QStash Documentation

Example:
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")

res = client.message.publish_json(
    url="
    body={"hello": "world"},
    headers={
        "test-header": "test-value",
    },
)

print(res.message_id)
```

Sections: Upstash Python QStash SDK, Usage, Publish a JSON message, Create a scheduled message, Receiving messages, Publish a JSON message to LLM Using Custom Providers, Additional configuration

</details>

### sqlalchemy-cloudflare-d1

A SQLAlchemy dialect for Cloudflare's D1 Serverless SQLite Database

`pip install sqlalchemy-cloudflare-d1` · installs (wheel) · licence: MIT License · rank 6403 · last release 2026-10-02 · [PyPI](https://pypi.org/project/sqlalchemy-cloudflare-d1/) · [source](https://github.com/collierking/sqlalchemy-cloudflare-d1)

<details><summary>README extract</summary>

A SQLAlchemy dialect for Cloudflare's D1 Serverless SQLite Database supporting both the REST API and Python Workers.

Features:
- Full SQLAlchemy ORM and Core support
- Sync and async engines via D1 REST API (`create_engine` and `create_async_engine`)
- Python Workers support with direct D1 binding (`create_engine_from_binding`) ...

Example:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine(
    "cloudflare_d1://account_id:api_token@database_id"
)

# Create base and define model
Base = declarative_base()

class User(Base):
...
```

...

</details>

### pixeltable-pgserver

Embedded Postgres Server for Pixeltable

`pip install pixeltable-pgserver` · installs (wheel) · licence: Apache Software License · rank 6515 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pixeltable-pgserver/) · [docs](https://docs.pixeltable.com/) · [source](https://github.com/pixeltable/pixeltable-pgserver)

<details><summary>README extract</summary>

pixeltable-pgserver is an embedded Postgres server used internally by
Pixeltable. It is a fork of Oscar Moll's
pgserver, which is itself a fork of Michel Pelletier's
postgresql-wheel.

For Pixeltable documentation and installation instructions, visit the main
Pixeltable repository.

</details>

### pysqlite3

DB-API 2.0 interface for Sqlite 3.x

`pip install pysqlite3` · installs (wheel) · licence: not stated · rank 6524 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pysqlite3/) · [source](https://github.com/coleifer/pysqlite3)

<details><summary>README extract</summary>

Note: moving forward, cysqlite (docs)
is where all new development is happening for packaging a SQLite driver as a
self-contained package. End note

This library takes the SQLite module from Python 3 and packages it as a
separately-installable module. ...

</details>

### dag-factory

Dynamically build Apache Airflow DAGs from YAML files

`pip install dag-factory` · installs (wheel) · licence: Apache-2.0 · rank 6528 · last release 2026-05-07 · [PyPI](https://pypi.org/project/dag-factory/) · [source](https://github.com/astronomer/dag-factory)

<details><summary>README extract</summary>

Welcome to *dag-factory*! *dag-factory* is a library for Apache Airflow® to construct DAGs
declaratively via configuration files.

The minimum requirements for dag-factory are:

- Python 3.10.0+
- Apache Airflow® 2.9+

For a gentle introduction, please take a look at our Quickstart Guide. For more examples, please see the
examples folder. ...

Sections: dag-factory, Benefits, Privacy Notice

</details>

### eralchemy

Simple entity relation (ER) diagrams generation

`pip install eralchemy` · installs (wheel) · licence: Apache-2.0 · rank 6590 · last release 2026-05-05 · [PyPI](https://pypi.org/project/eralchemy/) · [source](https://github.com/eralchemy/eralchemy)

<details><summary>README extract</summary>

eralchemy generates Entity Relation (ER) diagram (like the one below) from databases or from SQLAlchemy models.

Example:
```python
from eralchemy import render_er
# Draw from SQLAlchemy base
render_er(Base, 'erd_from_sqlalchemy.png')

# Draw from database
render_er("sqlite:///relative/path/to/db.db", 'erd_from_sqlite.png')
```

Sections: Entity relation diagrams generator, Example, Quick Start, Graph library flavors, Usage from Command Line, From a database, From a markdown file., Specify Output Mode, Usage from Python, Adjustments to the rendering config, Architecture, Running tests, Notes

</details>

### sqlalchemy-trino

Trino dialect for SQLAlchemy

`pip install sqlalchemy-trino` · installs (wheel) · licence: Apache Software License · rank 6790 · last release 2022-05-05 · [PyPI](https://pypi.org/project/sqlalchemy-trino/)

<details><summary>README extract</summary>

`sqlalchemy-trino` was developed as _Trino (f.k.a PrestoSQL) dialect for SQLAlchemy._
Since trinodb/trino-python-client#81, all code of `sqlalchemy-trino` is donated and merged into upstream project.
So now, this project is no longer active and consider as deprecated.

Example:
```python
from sqlalchemy.engine import create_engine
from trino.auth import JWTAuthentication

# pass access token via connect_args
engine = create_engine(
  'trino://<username>@<host>:<port>/',
  connect_args={'auth': JWTAuthentication('a-jwt-token')},
)

# pass access token via the query string param accessToken
engine = create_engine(
...
```

Sections: sqlalchemy-trino, ⚠️ Deprecation and Archive Notice, Through Python Package Index, Latest from Source Code, Usage, JWT authentication, User impersonation

</details>

### pyvo

Astropy affiliated package for accessing Virtual Observatory data and services

`pip install pyvo` · installs (wheel) · licence: BSD-3-Clause · rank 6798 · last release 2026-11-04 · [PyPI](https://pypi.org/project/pyvo/) · [docs](https:/pyvo.readthedocs.io) · [source](https://github.com/astropy/pyvo)

<details><summary>README extract</summary>

PyVO is a package providing access to remote data and services of the
Virtual observatory (VO) using Python.

Its development was launched by the NSF/NASA-funded Virtual Astronomical
Observatory (VAO) project (formerly under the name VAOpy) as part of its
initiative to bring VO capabilities to desktop. ...

Sections: PyVO, Examples, Unit Tests

</details>

### PyGreSQL

Python PostgreSQL interfaces

`pip install PyGreSQL` · installs from source (sdist only) · licence: PostgreSQL · rank 6840 · last release 2026-01-25 · [PyPI](https://pypi.org/project/PyGreSQL/) · [docs](https://pygresql.github.io/contents/) · [source](https://github.com/PyGreSQL/PyGreSQL)

<details><summary>README extract</summary>

PyGreSQL is a Python module that interfaces to a PostgreSQL database.
It wraps the lower level C API library libpq to allow easy use of the
powerful PostgreSQL features from Python.

PyGreSQL should run on most platforms where PostgreSQL and Python is running.
It is based on the PyGres95 code written by Pascal Andre.
D'Arcy J. M. ...

Sections: PyGreSQL - Python interface for PostgreSQL, Documentation

</details>

### scrapy-ingest

One pipeline. Full crawl observability in SQL or Elasticsearch.

`pip install scrapy-ingest` · installs (wheel) · licence: MIT License · rank 6898 · last release 2026-11-02 · [PyPI](https://pypi.org/project/scrapy-ingest/) · [docs](https://scrapy-ingest.readthedocs.io/) · [source](https://github.com/fawadss1/scrapy-ingest)

<details><summary>README extract</summary>

One pipeline. Full crawl observability in SQL or Elasticsearch — plus an optional read-only web dashboard.

Set `DB_URL`, `SEARCH_URL`, or both — or use no DB settings and ingest writes to `ingest.db` (SQLite) in your project folder. Items, requests, logs, stats, parent URLs, and errors are captured automatically. ...

Sections: Scrapy Ingest, Minimal setup (settings.py), Choose your destination, Database configuration, Elasticsearch / OpenSearch configuration, What is stored, Relational database (Postgres / MySQL), Elasticsearch / OpenSearch, Ingest flow and connections, Crawl lifecycle, When data is flushed, CLI, `check-config`, `jobs show`

</details>

### libcudf-cu12

cuDF - GPU Dataframe (C++)

`pip install libcudf-cu12` · installs (wheel) · licence: Apache-2.0 · rank 6970 · last release 2026-10-22 · [PyPI](https://pypi.org/project/libcudf-cu12/)

<details><summary>README extract</summary>

NVIDIA cuDF (pronounced "KOO-dee-eff") is an Apache 2.0 licensed, GPU-accelerated DataFrame library
for tabular data processing. The cuDF library is one part of the NVIDIA
CUDA-X suite of GPU
Accelerated libraries.

cuDF is composed of multiple libraries including: ...

Example:
```python
import cudf

df = cudf.read_parquet("data.parquet")
df.dropna().groupby(["A", "B"]).mean()
```

Sections: About, System Requirements, pip, conda, source, Examples, cudf, cudf.pandas, cudf-polars, Questions and Discussion

</details>

### astroquery

Functions and classes to access online astronomical data resources

`pip install astroquery` · installs (wheel) · licence: BSD License · rank 6973 · last release 2025-09-20 · [PyPI](https://pypi.org/project/astroquery/) · [docs](https://astroquery.readthedocs.io) · [source](https://github.com/astropy/astroquery)

<details><summary>README extract</summary>

Documentation | View on Github | Download Development ZIP

Astroquery is an astropy affiliated package that
contains a collection of tools to access online Astronomical data. Each web
service has its own sub-package. For example, to interface with the SIMBAD
website, use the `simbad` sub-package:

Example:
```python
>>> from astroquery.simbad import Simbad
>>> theta1c = Simbad.query_object('tet01 Ori C')
>>> theta1c.pprint()
   main_id          ra           dec      ... coo_wavelength     coo_bibcode       matched_id
                   deg           deg      ...
------------- ------------- ------------- ... -------------- ------------------- -------------
...
```

Sections: Accessing Online Astronomical Data, Using astroquery, Citing Astroquery, Additional Links

</details>

### neo4j-rust-ext

Rust Extensions for a Faster Neo4j Bolt Driver for Python

`pip install neo4j-rust-ext` · installs (wheel) · licence: Apache-2.0 AND MIT · rank 6979 · last release 2026-10-15 · [PyPI](https://pypi.org/project/neo4j-rust-ext/) · [source](https://github.com/neo4j/neo4j-python-driver-rust-ext)

<details><summary>README extract</summary>

This project contains Rust extensions to speed up the official Python driver for Neo4j.

The exact speedup depends on the use-case but has been measured to be up to 10x faster.
Use-cases moving only few but big records out of the DBMS tend to benefit the most.

Sections: Rust Extensions for a Faster Neo4j Bolt Driver for Python, Requirements

</details>

### pgsanity

Check syntax of sql for PostgreSQL

`pip install pgsanity` · installs (wheel) · licence: MIT · rank 7000 · last release 2025-09-20 · [PyPI](https://pypi.org/project/pgsanity/) · [source](https://github.com/markdrago/pgsanity.git)

<details><summary>README extract</summary>

PgSanity checks the syntax of Postgresql SQL files.

It does this by leveraging the ecpg command which is traditionally
used for preparing C files with embedded SQL for compilation.
However, as part of that preparation, ecpg checks the embedded SQL
statements for syntax errors using the exact same parser that is
in PostgreSQL. ...

Sections: PgSanity, Dependencies, Getting PgSanity, Usage, Interpreting The Results, pre-commit, Reporting Problems

</details>

### dmpython

Python interface to Dameng

`pip install dmpython` · installs (wheel) · licence: Python Software Foundation License · rank 7033 · last release 2026-10-19 · [PyPI](https://pypi.org/project/dmpython/)

<details><summary>README extract</summary>

​ dmPython驱动是Python连接达梦数据库的原生驱动。允许Python程序直接连接到达梦数据库。模块由达梦数据库维护。

​ dmPython 是 DM 依据 Python DB API version 2.0 中 API 使用规定开发的数据库访问接口，Python 应用程序能够通过这些 API 对 DM 数据库进行访问。因 dmPython 通过调用 DM DPI 接口完成 Python 模块扩展，使用whl包安装时无需DPI，使用源码安装时需要配置DPI运行环境。

Example:
```python
import dmPython

conn = dmPython.connect('SYSDBA/Dmsys_123@localhost:5236/sch1')
cursor = conn.cursor()

cursor.execute("SELECT * FROM DUAL;")
result = cursor.fetchall()
for row in result:
    print(row)
```

Sections: dmPython, Samples, Help, Error Handling, Extensions

</details>

### sql-compare

Compare SQL schemas

`pip install sql-compare` · installs (wheel) · licence: Apache Software License · rank 7140 · last release 2026-09-03 · [PyPI](https://pypi.org/project/sql-compare/) · [source](https://github.com/Mergifyio/sql-compare)

<details><summary>README extract</summary>

Compare SQL schemas.

This package allows to compare two SQL files (or strings) to know whether their
statements are the same or not. The comparison doesn't care about the order of
the columns in a table or the order of the values in an enumerator. It also
excludes irrelevant data like comments. ...

Example:
```python
import sql_compare

assert sql_compare.compare(first_schema, second_schema)
```

Sections: SQL Compare, Usage, Dependencies

</details>

### singlestoredb

Interface to the SingleStoreDB database and workspace management APIs

`pip install singlestoredb` · installs (wheel) · licence: Apache-2.0 · rank 7183 · last release 2026-10-28 · [PyPI](https://pypi.org/project/singlestoredb/)

<details><summary>README extract</summary>

The SingleStoreDB Python SDK provides a DB-API 2.0
compatible interface to SingleStore, a high-performance
distributed SQL database designed for data-intensive applications including real-time
analytics and vector search.

Key Features: ...

Example:
```python
import singlestoredb as s2

# Connect using the default connector
conn = s2.connect('user:password@host:3306/db_name')

# Create a cursor
cur = conn.cursor()

# Execute SQL
cur.execute('select * from foo')

# Fetch the results
print(cur.description)
for item in cur:
    print(item)

# Close the connection
conn.close()
```

...

</details>

### librmm-cu12

Library for CUDA memory management

`pip install librmm-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7284 · last release 2026-10-08 · [PyPI](https://pypi.org/project/librmm-cu12/)

<details><summary>README extract</summary>

NOTE: For the latest stable README.md ensure you are on the `main` branch.

- RMM Reference Documentation: Python and C++ API references, tutorials, and topic guides.
- Installation: Instructions for installing RMM.
- GitHub Repository: Download the RMM source code.
- Issue Tracker: Report issues or request features.

Features:
Achieving optimal performance in GPU-centric workflows frequently requires customizing how host and
device memory are allocated. ...

Example:
```python
>>> import rmm
>>> buf = rmm.DeviceBuffer(size=100)
```

...

</details>

### cudf-cu12

cuDF - GPU Dataframe

`pip install cudf-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7296 · last release 2026-10-22 · [PyPI](https://pypi.org/project/cudf-cu12/) · [docs](https://docs.nvidia.com/cudf/)

<details><summary>README extract</summary>

NVIDIA cuDF (pronounced "KOO-dee-eff") is an Apache 2.0 licensed, GPU-accelerated DataFrame library
for tabular data processing. The cuDF library is one part of the NVIDIA
CUDA-X suite of GPU
Accelerated libraries.

cuDF is composed of multiple libraries including: ...

Example:
```python
import cudf

df = cudf.read_parquet("data.parquet")
df.dropna().groupby(["A", "B"]).mean()
```

Sections: About, System Requirements, pip, conda, source, Examples, cudf, cudf.pandas, cudf-polars, Questions and Discussion

</details>

### rmm-cu12

Library for CUDA memory management

`pip install rmm-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7297 · last release 2026-10-08 · [PyPI](https://pypi.org/project/rmm-cu12/)

<details><summary>README extract</summary>

NOTE: For the latest stable README.md ensure you are on the `main` branch.

- RMM Reference Documentation: Python and C++ API references, tutorials, and topic guides.
- Installation: Instructions for installing RMM.
- GitHub Repository: Download the RMM source code.
- Issue Tracker: Report issues or request features.

Features:
Achieving optimal performance in GPU-centric workflows frequently requires customizing how host and
device memory are allocated. ...

Example:
```python
>>> import rmm
>>> buf = rmm.DeviceBuffer(size=100)
```

...

</details>

### pylibcudf-cu12

pylibcudf - Python bindings for libcudf

`pip install pylibcudf-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7327 · last release 2026-10-22 · [PyPI](https://pypi.org/project/pylibcudf-cu12/) · [docs](https://docs.nvidia.com/cudf/)

<details><summary>README extract</summary>

NVIDIA cuDF (pronounced "KOO-dee-eff") is an Apache 2.0 licensed, GPU-accelerated DataFrame library
for tabular data processing. The cuDF library is one part of the NVIDIA
CUDA-X suite of GPU
Accelerated libraries.

cuDF is composed of multiple libraries including: ...

Example:
```python
import cudf

df = cudf.read_parquet("data.parquet")
df.dropna().groupby(["A", "B"]).mean()
```

Sections: About, System Requirements, pip, conda, source, Examples, cudf, cudf.pandas, cudf-polars, Questions and Discussion

</details>

### libkvikio-cu12

KvikIO - GPUDirect Storage (C++)

`pip install libkvikio-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7344 · last release 2026-10-08 · [PyPI](https://pypi.org/project/libkvikio-cu12/)

<details><summary>README extract</summary>

KvikIO (pronounced "kuh-VICK-eye-oh", see here for pronunciation of kvik) is a Python and C++ library for high performance file IO. It provides C++ and Python
bindings to cuFile,
which enables GPUDirect Storage (GDS).
KvikIO also works efficiently when GDS isn't available and can read/write both host and device data seamlessly.

Features:
* Object oriented API of cuFile with C++/Python exception handling.
* A Python Zarr backend for reading and writing GPU data to file seamlessly.
* Concurrent reads and writes using an internal thread pool.
* Non-blocking API. ...

Example:
```python
import cupy
import kvikio

def main(path):
    a = cupy.arange(100)
    f = kvikio.CuFile(path, "w")
    # Write whole array to file
    f.write(a)
    f.close()

    b = cupy.empty_like(a)
...

</details>

### aerich

A database migrations tool for Tortoise ORM.

`pip install aerich` · installs (wheel) · licence: Apache Software License · rank 7349 · last release 2026-08-24 · [PyPI](https://pypi.org/project/aerich/) · [docs](https://github.com/tortoise/aerich) · [source](https://github.com/tortoise/aerich.git)

<details><summary>README extract</summary>

> ⚠️ Warning
> For tortoise-orm>=1.0.0, you can use the built-in cli for migrating, e.g.: `python -m tortoise makemigrations`
> See more at:

English | Русский

Aerich is a database migrations tool for TortoiseORM, which is like alembic for SQLAlchemy,
or like Django ORM with it\'s own migration solution.

Example:
```python
from tortoise import Model, fields

class Test(Model):
    date = fields.DateField(null=True)
    datetime = fields.DatetimeField(auto_now=True)
    decimal = fields.DecimalField(max_digits=10, decimal_places=2)
    float = fields.FloatField(null=True)
    id = fields.IntField(primary_key=True)
...
```

...

</details>

### pymonetdb

Native MonetDB client Python API

`pip install pymonetdb` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7565 · last release 2026-07-09 · [PyPI](https://pypi.org/project/pymonetdb/)

<details><summary>README extract</summary>

pymonetdb is a native python client API for monetDB. This API is cross-platform,
and doesn't depend on any monetdb libraries. It has support for Python 3.7+
and PyPy. The driver is Python DBAPI 2.0 compatible.

Sections: Introduction, Documentation

</details>

### snowflake-telemetry-python

Snowflake Telemetry for Python

`pip install snowflake-telemetry-python` · installs (wheel) · licence: Apache Software License · rank 7579 · last release 2026-04-08 · [PyPI](https://pypi.org/project/snowflake-telemetry-python/) · [docs](https://docs.snowflake.com/en/developer-guide/logging-tracing/tracing-python) · [source](https://github.com/snowflakedb/snowflake-telemetry-python/)

<details><summary>README extract</summary>

This package provides a set of telemetry APIs for developers building on the Snowflake platform.

Documentation is available at:

Source code is also available at:

</details>

### django-fast-update

Faster db updates for Django using UPDATE FROM VALUES sql variants.

`pip install django-fast-update` · installs (wheel) · licence: MIT License · rank 7612 · last release 2025-08-04 · [PyPI](https://pypi.org/project/django-fast-update/)

<details><summary>README extract</summary>

Faster db updates using `UPDATE FROM VALUES` sql variants.

Sections: django-fast-update, Compatibility, copy_update, flat_update & merged_update, Performance

</details>

### pgcli

CLI for Postgres Database. With auto-completion and syntax highlighting.

`pip install pgcli` · installs (wheel) · licence: BSD-3-Clause · rank 7709 · last release 2026-09-20 · [PyPI](https://pypi.org/project/pgcli/) · [source](https://github.com/dbcli/pgcli/)

<details><summary>README extract</summary>

Ukrainian people are fighting for their country. A lot of civilians, women and children, are suffering. Hundreds were killed and injured, and thousands were displaced.

This is an image from my home town, Kharkiv. This place is right in the old city center.

Picture by @fomenko_ph (Telegram).

Please consider donating or volunteering. ...

Features:
The `pgcli` is written using prompt_toolkit.

* Auto-completes as you type for SQL keywords as well as tables and
 columns in the database.
* Syntax highlighting using Pygments. ...

Sections: We stand with Ukraine, A REPL for Postgres, Quick Start, Usage, Features, Config, macOS, Linux, Docker, IPython

</details>

### eql

Event Query Language

`pip install eql` · installs (wheel) · licence: AGPLv3 · rank 7876 · last release 2026-08-07 · [PyPI](https://pypi.org/project/eql/)

_README extract left out: share-alike licence._

### sqlalchemy-databricks

SQLAlchemy Dialect for Databricks

`pip install sqlalchemy-databricks` · installs (wheel) · licence: MIT License · rank 8028 · last release 2022-05-06 · [PyPI](https://pypi.org/project/sqlalchemy-databricks/) · [docs](https://github.com/crflynn/sqlalchemy-databricks) · [source](https://github.com/crflynn/sqlalchemy-databricks)

<details><summary>README extract</summary>

A SQLAlchemy Dialect for Databricks workspace and sql analytics clusters using the officially supported databricks-sql-connector dbapi.

Example:
```python
from sqlalchemy import *
from sqlalchemy.engine import create_engine

engine = create_engine(
    "databricks+connector://token:<databricks_token>@<databricks_host>:443/<database_or_schema_name>",
    connect_args={
        "http_path": "<cluster_http_path>",
    },
)

logs = Table("my_table", MetaData(bind=engine), autoload=True)
...
```

Sections: sqlalchemy-databricks, Usage

</details>

### snowflake-ml-python

The machine learning client library that is used for interacting with Snowflake to build machine learning solutions.

`pip install snowflake-ml-python` · installs (wheel) · licence: Apache Software License · rank 8044 · last release 2026-11-04 · [PyPI](https://pypi.org/project/snowflake-ml-python/) · [docs](https://docs.snowflake.com/developer-guide/snowpark-ml) · [source](https://github.com/snowflakedb/snowflake-ml-python)

<details><summary>README extract</summary>

`snowflake-ml-python` is the Python library for AI and machine learning on Snowflake. Use it to build and manage
features with the Snowflake Feature Store, train with the open-source frameworks you already use, and manage, serve,
and monitor models on Snowflake compute. ...

Features:
* `FeatureStore.generate_dataset` argument list has been changed to match the new
`snowflake.ml.dataset.Dataset` definition

 * `materialized_table` has been removed and replaced with `name` and `version`. ...

Example:
```python
from snowflake.ml.experiment import ExperimentTracking

exp = ExperimentTracking(session)
exp.set_experiment("MY_EXPERIMENT")
with exp.start_run(run_name="MY_RUN"):
    exp.log_model(model, model_name="MY_MODEL", sample_input_data=X)

...

</details>

### persistent

Translucent persistent objects

`pip install persistent` · installs (wheel) · licence: ZPL-2.1 · rank 8091 · last release 2026-10-27 · [PyPI](https://pypi.org/project/persistent/) · [docs](https://persistent.readthedocs.io) · [source](https://github.com/zopefoundation/persistent)

<details><summary>README extract</summary>

This package contains a generic persistence implementation for Python. It
forms the core protocol for making objects interact "transparently" with
a database such as the ZODB.

Please see the Sphinx documentation (`docs/index.rst`) for further
information, or view the documentation at Read The Docs, for either
the latest (` or stable
release (`

Example:
```python
  from persistent.timestamp import TimeStamp

which will yield the class from the extension module (if available),
falling back to the pure-Python reference implementation.
```

...

</details>

### tangled-up-in-unicode

Access to the Unicode Character Database (UCD)

`pip install tangled-up-in-unicode` · installs (wheel) · licence: BSD License · rank 8155 · last release 2021-09-27 · [PyPI](https://pypi.org/project/tangled-up-in-unicode/)

<details><summary>README extract</summary>

This module provides access to character properties for all Unicode characters, from the Unicode Character Database (UCD) .
This module provides an alternative to Python's standard library `unicodedata`.
`Tangled up in Unicode` provides four main benefits compared to the standard library:
- The latest version of the Unicode database is used. ...

Example:
```python
import tangled_up_in_unicode as unicodedata
```

Sections: Tangled up in Unicode, Example, Properties comparison, Usage, Performance

</details>

### airflow-provider-fivetran-async

A Fivetran async provider for Apache Airflow

`pip install airflow-provider-fivetran-async` · installs (wheel) · licence: Apache-2.0 · rank 8161 · last release 2026-04-17 · [PyPI](https://pypi.org/project/airflow-provider-fivetran-async/) · [source](https://github.com/astronomer/airflow-provider-fivetran-async)

<details><summary>README extract</summary>

This package provides an async operator, sensor and hook that integrates Fivetran into Apache Airflow.
`FivetranSensor` allows you to monitor a Fivetran sync job for completion before running downstream processes.
`FivetranOperator` submits a Fivetran sync job and polls for its status on the triggerer. ...

Example:
```python
from fivetran_provider_async.operators import FivetranOperator
```

Sections: Fivetran Async Provider for Apache Airflow, Configuration, Modules, Fivetran Operator Async, Fivetran Sensor Async, Examples, Issues

</details>

### pytd

Treasure Data Driver for Python

`pip install pytd` · installs (wheel) · licence: Apache-2.0 · rank 8180 · last release 2026-02-03 · [PyPI](https://pypi.org/project/pytd/) · [source](https://github.com/treasure-data/pytd)

<details><summary>README extract</summary>

pytd provides user-friendly interfaces to Treasure Data’s REST
APIs, Presto
query
engine,
and Plazma primary
storage.

The seamless connection allows your Python code to efficiently
read/write a large volume of data from/to Treasure Data. Eventually,
pytd makes your day-to-day data analytics work more productive.

Example:
```python
import pytd

client = pytd.Client(database='sample_datasets')
# or, hard-code your API key, endpoint, and/or query engine:
# >>> pytd.Client(apikey='1/XXX', endpoint=' database='sample_datasets', default_engine='presto')
```

Sections: pytd, Requirements, Usage, Query in Treasure Data, Write data to Treasure Data, Enabling Spark Writer, Comparison between pytd, td-client-python, and pandas-td, How to replace pandas-td

</details>

### odata-query

An OData query parser and transpiler.

`pip install odata-query` · installs (wheel) · licence: MIT · rank 8236 · last release 2026-11-01 · [PyPI](https://pypi.org/project/odata-query/)

<details><summary>README extract</summary>

`odata-query` is a library that parses OData v4 filter strings, and can
convert them to other forms such as Django Queries, SQLAlchemy Queries,
or just plain SQL.

Example:
```python
from odata_query.django import apply_odata_query

orm_query = MyModel.objects  # This can be a Manager or a QuerySet.
odata_query = "name eq 'test'"  # This will usually come from a query string parameter.

query = apply_odata_query(orm_query, odata_query)
results = query.all()
```

Sections: OData-Query, Quickstart, Advanced Usage, Contact

</details>

### django-multitenant

Django Library to Implement Multi-tenant databases

`pip install django-multitenant` · installs (wheel) · licence: MIT License · rank 8259 · last release 2023-12-18 · [PyPI](https://pypi.org/project/django-multitenant/)

<details><summary>README extract</summary>

Python/Django support for distributed multi-tenant databases like Postgres+Citus

Enables easy scale-out by adding the tenant context to your queries, enabling the database (e.g. Citus) to efficiently route queries to the right database node.

There are architecures for building multi-tenant databases viz. ...

Example:
```python
from django_multitenant.fields import *
from django_multitenant.models import *
```

Sections: django-multitenant, Usage, Changes in Models, Changes in Models using mixins, Automating composite foreign keys at db layer, Where to Set the Tenant?

</details>

### BTrees

Scalable persistent object containers

`pip install BTrees` · installs (wheel) · licence: ZPL-2.1 · rank 8273 · last release 2026-08-20 · [PyPI](https://pypi.org/project/BTrees/) · [docs](https://btrees.readthedocs.io) · [source](https://github.com/zopefoundation/BTrees)

<details><summary>README extract</summary>

This package contains a set of persistent object containers built around
a modified BTree data structure. The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit resolution
of conflicts detected by that mechanism.

Please see the Sphinx documentation for
further information.

Sections: `BTrees`: scalable persistent components, 6.5 (2026-08-20), 6.4 (2026-04-29), 6.3 (2025-11-16), 6.2 (2025-10-28), 6.1 (2024-09-17), 6.0 (2024-05-30), 5.2 (2024-02-07), 5.1 (2023-10-05), 5.0 (2023-02-10), 4.11.3 (2022-11-17), 4.11.2 (2022-11-16), 4.11.1 (2022-11-09), 4.11.0 (2022-11-03)

</details>

### firebird-driver

Firebird driver for Python

`pip install firebird-driver` · installs (wheel) · licence: MIT License · rank 8340 · last release 2026-10-31 · [PyPI](https://pypi.org/project/firebird-driver/) · [docs](https://firebird-driver.rtfd.io) · [source](https://github.com/FirebirdSQL/python3-driver)

<details><summary>README extract</summary>

This package provides official Python Database API 2.0-compliant driver for the open
source relational database Firebird®. In addition to the minimal feature set of
the standard Python DB API, this driver also exposes the new (interface-based)
client API introduced in Firebird 3, and number of additional extensions and
enhancements for convenient ...

Sections: firebird-driver, Firebird driver for Python, Agent skill, Documentation, Running tests

</details>

### py2neo-history

Python client library and toolkit for Neo4j

`pip install py2neo-history` · installs from source (sdist only) · licence: Apache Software License · rank 8368 · last release 2023-10-20 · [PyPI](https://pypi.org/project/py2neo-history/) · [docs](https://py2neo.org/2021.2/) · [source](https://github.com/technige/py2neo)

<details><summary>README extract</summary>

This is a copy of the py2neo package to restore the version history that got deleted.
It's not possible to re-upload a deleted version of a package to PyPI.
So if you rely on, for example, `py2neo ~= 4.1.0` in your project, you can simply switch to `py2neo-history ~= 4.1.0`. ...

Example:
```python
>>> from py2neo import Graph
>>> graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
>>> graph.run("UNWIND range(1, 3) AS n RETURN n, n * n as n_sq")
   n | n_sq

   1 |    1
   2 |    4
   3 |    9
```

Sections: Py2neo, Quick Example, More

</details>

### django-dbbackup

Management commands to help backup and restore a project database and media.

`pip install django-dbbackup` · installs (wheel) · licence: BSD-3-Clause · rank 8439 · last release 2026-10-24 · [PyPI](https://pypi.org/project/django-dbbackup/) · [docs](https://archmonger.github.io/django-dbbackup) · [source](https://github.com/Archmonger/django-dbbackup)

<details><summary>README extract</summary>

This Django application provides management commands to help backup and restore your project database and media files with various storages such as Amazon S3, Dropbox, local file storage, or any Django-supported storage.

The main features include:

- Secure your backup with GPG signature and encryption.
- Archive with compression. ...

Features:
DBBackup gives you a simple yet robust interface to backup, encrypt, transmit, and restore your database and media.

In a few words, it is a pipe between your Django project and your backups. ...

Sections: Django DBBackup, Why use DBBackup?

</details>

### datafusion-query-builder

Programmatic, injection-safe builder for DataFusion SQL.

`pip install datafusion-query-builder` · installs (wheel) · licence: MIT · rank 8480 · last release 2026-10-17 · [PyPI](https://pypi.org/project/datafusion-query-builder/) · [source](https://github.com/pydantic/datafusion-query-builder)

<details><summary>README extract</summary>

A programmatic, injection-safe builder for DataFusion SQL — a typed Rust core with a
pyo3-exposed Python API. It replaces hand-rolled f-string / template-literal SQL with a typed,
composable surface, while still emitting SQL text (so the SQL stays visible in logs/traces,
greppable, and cache-keyable). ...

Example:
```python
from datafusion_query_builder import col, lit, param, raw, when, and, table
from datafusion_query_builder import functions as f

q = (
    table("records")
    .filter((col("kind") == "span") & col("deployment_environment").is_in(["prod", "staging"]))
    .select(
        f.coalesce(col("service_name"), "(unknown)").alias("service"),
...
```

Sections: datafusion-query-builder, Quick start (Python), Architecture, How the tests are layered

</details>

### duckdb-cli

The DuckDB CLI

`pip install duckdb-cli` · installs (wheel) · licence: MIT License · rank 8591 · last release 2026-11-05 · [PyPI](https://pypi.org/project/duckdb-cli/) · [docs](https://duckdb.org/docs/) · [source](https://github.com/duckdb/duckdb)

<details><summary>README extract</summary>

This package distributes the DuckDB Command Line Interface as a Python package.

Sections: DuckDB CLI, Usage

</details>

### zope.sqlalchemy

Minimal Zope/SQLAlchemy transaction integration

`pip install zope.sqlalchemy` · installs (wheel) · licence: Zope Public License · rank 8683 · last release 2025-11-25 · [PyPI](https://pypi.org/project/zope.sqlalchemy/)

<details><summary>README extract</summary>

The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it seeks
only to provide a data manager and makes no attempt to define a `zopeish` way
to configure engines. ...

Example:
```python
from zope.sqlalchemy import register
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = sqlalchemy.create_engine("postgresql://scott:tiger@localhost/test")

DBSession = scoped_session(sessionmaker(bind=engine))
register(DBSession)
```

...

</details>

### speedict

Speedb Python Binding

`pip install speedict` · does not install on CPython 3.14 · licence: MIT License · rank 8734 · last release 2023-11-11 · [PyPI](https://pypi.org/project/speedict/)

<details><summary>README extract</summary>

Key-value storage supporting any python object

This library has two purposes.

1. As an on-disk key-value storage solution for Python.
2. As a SpeeDB interface.

These two purposes operate in different modes:

- Default mode, which allows storing `int`, `float`,
`bool`, `str`, `bytes`, and other python objects (with `Pickle`). ...

Example:
```python
from speedict import Rdict
import numpy as np
import pandas as pd

path = str("./test_dict")

# create a Rdict with default options at `path`
db = Rdict(path)
db[1.0] = 1
db["huge integer"] = 2343546543243564534233536434567543
db["good"] = True
db["bytes"] = b"bytes"
db["this is a list"] = [1, 2, 3]
db["store a dict"] = {0: 1}
...
```

...

</details>

### pgparse

Python wrapper for libpg_query

`pip install pgparse` · installs (wheel) · licence: BSD-3-Clause · rank 8756 · last release 2026-03-19 · [PyPI](https://pypi.org/project/pgparse/)

<details><summary>README extract</summary>

Python bindings for libpg_query, exposing PostgreSQL's internal parser to Python. Parse, normalize, and fingerprint SQL statements using the same parser that PostgreSQL itself uses.

| pgparse | libpg_query | PostgreSQL |

| 1.x | 17-latest | 17 |

Example:
```python
import pgparse

result = pgparse.parse("SELECT * FROM orders WHERE id = 1")
# [{'stmt': {'SelectStmt': {...}}}]
```

Sections: pgparse, PostgreSQL Compatibility, Usage, Parse, Normalize, Fingerprint, Parse PL/pgSQL, Error Handling, Documentation

</details>

### databend-driver

Databend Driver Python Binding

`pip install databend-driver` · installs (wheel) · licence: Apache Software License · rank 8779 · last release 2026-11-06 · [PyPI](https://pypi.org/project/databend-driver/) · [source](https://github.com/databendlabs/bendsql)

<details><summary>README extract</summary>

Databend Python Client

Example:
```python
from databend_driver import connect

# Persistent state stored under ./local-state
conn = connect("databend+local:///./local-state")
conn.exec("CREATE TABLE books(id INT, title STRING)")
conn.exec("INSERT INTO books VALUES (1, 'Databend')")

row = conn.query_row("SELECT title FROM books ORDER BY id LIMIT 1")
print(row.values())  # ('Databend',)

...
```

Sections: databend-driver, Usage, Local Embedded Connection, Relation API, Registering External Data, PEP 249 Cursor Object, Blocking Connection Object, Asyncio Connection Object, Parameter bindings, Query ID tracking and query management, Type Mapping, General Data Types, Semi-Structured Data Types, APIs

</details>

### datasette

An open source multi-tool for exploring and publishing data

`pip install datasette` · installs (wheel) · licence: Apache License, Version 2.0 · rank 9029 · last release 2026-09-17 · [PyPI](https://pypi.org/project/datasette/) · [docs](https://docs.datasette.io/en/stable/) · [source](https://github.com/simonw/datasette)

<details><summary>README extract</summary>

*An open source multi-tool for exploring and publishing data*

Datasette is a tool for exploring and publishing data. It helps people take data of any shape or size and publish that as an interactive, explorable website and accompanying API. ...

Sections: Basic usage, metadata.json, datasette publish, Datasette Lite

</details>

### sqlalchemy-filters

A library to filter SQLAlchemy queries.

`pip install sqlalchemy-filters` · installs (wheel) · licence: Apache Software License · rank 9122 · last release 2023-04-13 · [PyPI](https://pypi.org/project/sqlalchemy-filters/)

<details><summary>README extract</summary>

Assuming that we have a SQLAlchemy `query` object:

Then we can apply filters to that `query` object (multiple times):

It is also possible to filter queries that contain multiple models,
including joins:

`apply_filters` will attempt to automatically join models to `query`
if they're not already present and a model-specific filter is supplied. ...

Example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Base(object):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    count = Column(Integer, nullable=True)

    @hybrid_property
    def count_square(self):
        return self.count * self.count

...
```

...

</details>

### ipython-sql

RDBMS access via IPython

`pip install ipython-sql` · installs (wheel) · licence: MIT License · rank 9209 · last release 2023-02-27 · [PyPI](https://pypi.org/project/ipython-sql/) · [source](https://github.com/catherinedevlin/ipython-sql)

<details><summary>README extract</summary>

:Author: Catherine Devlin,

Introduces a %sql (or %%sql) magic.

Connect to a database, using SQLAlchemy URL connect strings, then issue SQL
commands within IPython or IPython Notebook.

Example:
```python
In [1]: %load_ext sql

In [2]: %%sql postgresql://will:longliveliz@localhost/shakes
   ...: select * from character
   ...: where abbrev = 'ALICE'
   ...:
Out[2]: [(u'Alice', u'Alice', u'ALICE', u'a lady attending on Princess Katherine', 22)]

In [3]: result = _

In [4]: print(result)
...
```

Sections: ipython-sql, Examples, Variable substitution, Assignment, Connecting, DSN connections, Configuration, Pandas, Graphing, Dumping, PostgreSQL features, Options, Caution, Comments

</details>

### sqlalchemy-views

Adds CreateView and DropView constructs to SQLAlchemy

`pip install sqlalchemy-views` · installs (wheel) · licence: MIT License · rank 9250 · last release 2023-02-18 · [PyPI](https://pypi.org/project/sqlalchemy-views/)

<details><summary>README extract</summary>

Adds `CreateView` and `DropView` constructs to SQLAlchemy.

Sections: View Manipulation for SQLAlchemy, Usage, Limitations

</details>

### pymongoarrow

Tools for using NumPy, Pandas, Polars, and PyArrow with MongoDB

`pip install pymongoarrow` · installs (wheel) · licence: Apache Software License · rank 9334 · last release 2026-10-28 · [PyPI](https://pypi.org/project/pymongoarrow/) · [docs](https://mongo-arrow.readthedocs.io) · [source](https://github.com/mongodb-labs/mongo-arrow/tree/main/bindings/python)

<details><summary>README extract</summary>

PyMongoArrow is a companion library to PyMongo that contains tools
for loading MongoDB query result sets as Apache Arrow tables, Pandas
DataFrames or NumPy arrays.

PyMongoArrow is the recommended way to materialize MongoDB query
result sets as contiguous-in-memory, typed arrays suited for in-memory
analytical processing applications.

Example:
```python
>>> from pymongoarrow.monkey import patch_all
... patch_all()
... from pymongoarrow.api import Schema
... schema = Schema({"_id": int, "qty": float})
... from pymongo import MongoClient
... client = MongoClient()
... client.db.data.insert_many(
...     [{"_id": 1, "qty": 25.4}, {"_id": 2, "qty": 16.9}, {"_id": 3, "qty": 2.3}]
... )
...
```

Sections: PyMongoArrow, Documentation

</details>

### apache-superset-core

Core Python package for building Apache Superset backend extensions and integrations

`pip install apache-superset-core` · installs (wheel) · licence: Apache-2.0 · rank 9461 · last release 2026-05-11 · [PyPI](https://pypi.org/project/apache-superset-core/) · [docs](https://superset.apache.org/docs/) · [source](https://github.com/apache/superset)

<details><summary>README extract</summary>

<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements. See the NOTICE file
distributed with this work for additional information
regarding copyright ownership. ...

Example:
```python
from flask_appbuilder.api import expose, permission_name, protect, safe
from superset_core.rest_api.api import RestApi
from superset_core.rest_api.decorators import api

@api(id="dataset_references", name="Dataset References API")
class DatasetReferencesAPI(RestApi):

    @expose("/metadata", methods=("POST",))
    @protect()
    @safe
...
```

Sections: apache-superset-core, 🏗️ Package Structure, 🚀 Quick Start, Basic Extension API, Background Tasks, MCP Tools, MCP Prompts, 🔗 Links

</details>

### crate

CrateDB Python Client

`pip install crate` · installs (wheel) · licence: Apache-2.0 · rank 9475 · last release 2026-11-02 · [PyPI](https://pypi.org/project/crate/)

<details><summary>README extract</summary>

A Python client library for CrateDB, implementing the Python DB API 2.0
specification.

The CrateDB dialect for SQLAlchemy is provided by the sqlalchemy-cratedb
package, see also sqlalchemy-cratedb documentation.

Sections: CrateDB Python Client, Migration Notes, Documentation and Help

</details>

### sqlalchemy-mixins

Active Record, Django-like queries, nested eager load and beauty __repr__ for SQLAlchemy

`pip install sqlalchemy-mixins` · installs (wheel) · licence: MIT License · rank 9505 · last release 2023-08-29 · [PyPI](https://pypi.org/project/sqlalchemy-mixins/)

### YORM

Automatic object-YAML mapping for Python.

`pip install YORM` · installs (wheel) · licence: MIT License · rank 9722 · last release 2019-03-23 · [PyPI](https://pypi.org/project/YORM/)

<details><summary>README extract</summary>

Build Status|
Coverage Status|
Scrutinizer Code Quality|
PyPI Version|

Features:
| YORM enables automatic, bidirectional, human-friendly mappings of
 object attributes to YAML files.
| Uses beyond typical object serialization and relational mapping
 include:

- bidirectional conversion between basic YAML and Python types ...

Example:
```python
class Student:
    def init(self, name, school, number, year=2009):
        self.name = name
        self.school = school
        self.number = number
        self.year = year
        self.gpa = 0.0
```

Sections: Overview, Requirements, Usage, 1.6.2 (2019-03-23), 1.6.1 (2019-03-22), 1.6 (2018-09-07), 1.5.1 (2018-03-07), 1.5 (2017-10-22), 1.4 (2017-04-02), 1.3 (2017-01-24), 1.2 (2017-01-06), 1.1 (2016-10-22), 1.0.1 (2016-09-23), 1.0 (2016-05-22)

</details>

### arcticdb

ArcticDB DataFrame Database

`pip install arcticdb` · installs (wheel) · licence: Business Source License 1.1 (See LICENSE.txt) · rank 9724 · last release 2026-11-02 · [PyPI](https://pypi.org/project/arcticdb/)

<details><summary>README extract</summary>

Three minute ArcticDB demo from PyQuantNews

 ArcticDB Website | 📘 ArcticDB Docs | 📰: ArcticDB Blog | Press Release | Press Release | Community

ArcticDB is a high performance, serverless DataFrame database built for the Python Data Science ecosystem.
Launched in March 2023, it is the successor to Arctic. ...

Sections: Quickstart, Prebuilt binary availability (for the current version), Storage compatibility, Documentation

</details>

### mysql-connector-python-rf

MySQL driver written in Python

`pip install mysql-connector-python-rf` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 9744 · last release 2017-02-04 · [PyPI](https://pypi.org/project/mysql-connector-python-rf/)

_README extract left out: share-alike licence._

### falkordblite

FalkorDB embedded in a Python package

`pip install falkordblite` · installs (wheel) · licence: BSD License · rank 9785 · last release 2026-10-19 · [PyPI](https://pypi.org/project/falkordblite/) · [docs](https://docs.falkordb.com/) · [source](https://github.com/FalkorDB/falkordblite)

<details><summary>README extract</summary>

FalkorDBLite is a self-contained Python interface to the FalkorDB graph database.

It provides enhanced versions of the Redis-Py Python bindings with FalkorDB graph database functionality. Key features include: ...

Example:
```python
from redislite.falkordb_client import FalkorDB

db = FalkorDB('/tmp/my.db')
g = db.select_graph('mygraph')
g.query('CREATE (n:Person {name: "Alice"}) RETURN n')
result = g.query('MATCH (n:Person) RETURN n.name')
print(result.result_set)  # [['Alice']]
```

Sections: FalkorDBLite, Description, Quick Start, Requirements, Runtime Requirements, macOS Runtime Requirements, Getting Started, Examples, Using FalkorDB Graph Database, Using Redis Key-Value Operations, Persistence, Compatibility, Running and using Multiple servers, FalkorDB-Specific Features

</details>

### mixpanel-headless

Python library for working with Mixpanel analytics data, designed for AI coding agents

`pip install mixpanel-headless` · installs (wheel) · licence: MIT · rank 9813 · last release 2026-10-05 · [PyPI](https://pypi.org/project/mixpanel-headless/) · [source](https://github.com/mixpanel/mixpanel-headless)

<details><summary>README extract</summary>

> ⚠️ Pre-release Software: This package is under active development. APIs may change between versions before 1.0.

A complete programmable interface to Mixpanel analytics—Python library and CLI for discovery, querying, streaming, and entity management.

Features:
Mixpanel's web UI is powerful for interactive exploration, but programmatic access requires navigating multiple REST endpoints with different conventions. ...

Example:
```python
import mixpanel_headless as mp

ws = mp.Workspace()

# Typed insights query (recommended)
result = ws.query("Purchase", math="unique", group_by="country", last=30)
print(result.df)
```

...

</details>

### zodbpickle

Fork of Python 3 pickle module

`pip install zodbpickle` · installs (wheel) · licence: ZPL-2.1 · rank 9896 · last release 2026-08-20 · [PyPI](https://pypi.org/project/zodbpickle/) · [source](https://github.com/zopefoundation/zodbpickle)

<details><summary>README extract</summary>

This package presents a uniform pickling interface for ZODB:

- Under Python2, this package forks both Python 2.7's `pickle` and
 `cPickle` modules, adding support for the `protocol 3` opcodes. ...

Example:
```python
import pickle
```

Sections: `zodbpickle` README, Caution, General Usage, Loading/Storing Python 2 Strings, 4.5 (2026-08-20), 4.4 (2026-05-04), 4.3 (2025-11-20), 4.2 (2025-02-12), 4.1.1 (2024-10-02), 4.1 (2024-09-17), 4.0 (2024-05-30), 3.3 (2024-04-16), 3.2 (2024-02-16), 3.1 (2023-10-05)

</details>

### pymongosql

Python DB API 2.0 (PEP 249) client for MongoDB

`pip install pymongosql` · installs (wheel) · licence: MIT License · rank 9977 · last release 2026-09-10 · [PyPI](https://pypi.org/project/pymongosql/) · [docs](https://github.com/passren/PyMongoSQL/wiki) · [source](https://github.com/passren/PyMongoSQL.git)

<details><summary>README extract</summary>

PyMongoSQL is a Python DB API 2.0 (PEP 249) client for MongoDB. It provides a familiar SQL interface to MongoDB, allowing developers to use SQL to interact with MongoDB collections.

PyMongoSQL implements the DB API 2.0 interfaces to provide SQL-like access to MongoDB, built on PartiQL syntax for querying semi-structured data. ...

Features:
- DB API 2.0 Compliant: Full compatibility with Python Database API 2.0 specification
- PartiQL-based SQL Syntax: Built on PartiQL (SQL for semi-structured data), enabling seamless SQL querying of nested and hierarchical MongoDB documents ...

Example:
```python
from pymongosql import connect

# Connect to MongoDB
connection = connect(
    host="mongodb://localhost:27017",
    database="database"
)

cursor = connection.cursor()
...

</details>

### snowpipe-streaming

Snowflake Streaming Ingest SDK

`pip install snowpipe-streaming` · installs (wheel) · licence: Apache Software License · rank 10066 · last release 2026-11-02 · [PyPI](https://pypi.org/project/snowpipe-streaming/) · [docs](https://docs.snowflake.com/) · [source](https://github.com/snowflake-eng/snowflake-ingest-sdk)

<details><summary>README extract</summary>

A high-performance Python SDK for streaming data ingestion into Snowflake, built with Rust for optimal performance and reliability.

Features:
The Snowflake Streaming Ingest Python SDK provides a Python interface for real-time data streaming into Snowflake tables. It leverages a Rust core for high performance while providing a familiar Python API for easy integration.

Example:
```python
from snowflake.ingest.streaming import StreamingIngestClient

# Create a client
client = StreamingIngestClient(
    client_name="my_client",
    db_name="my_database",
    schema_name="my_schema",
    pipe_name="my_pipe",
    properties={
        "account": "your_account",
        "user": "your_user",
        "private_key": "your_private_key",
...
```

...

</details>

### surrealdb

SurrealDB python client

`pip install surrealdb` · installs (wheel) · licence: Apache-2.0 · rank 10076 · last release 2026-11-04 · [PyPI](https://pypi.org/project/surrealdb/) · [docs](https://surrealdb.com/docs/sdk/python) · [source](https://github.com/surrealdb/surrealdb.py)

<details><summary>README extract</summary>

The official SurrealDB SDK for Python.

View the SDK documentation here.

Features:
- Automatic tracing: All database methods are instrumented automatically
- Smart parameter logging: Sensitive data (tokens, passwords) are automatically scrubbed ...

Example:
```python
import logfire
from surrealdb import AsyncSurreal

# Configure Logfire
logfire.configure()

# Instrument all SurrealDB operations
logfire.instrument_surrealdb()

# All database operations are now automatically traced
async with AsyncSurreal("ws://localhost:8000") as db:
    await db.signin({"username": "root", "password": "root"})
...
```

...

</details>

### redis-om

Object mappings, and more, for Redis.

`pip install redis-om` · installs (wheel) · licence: BSD License · rank 10123 · last release 2026-10-01 · [PyPI](https://pypi.org/project/redis-om/) · [source](https://github.com/redis/redis-om-python)

<details><summary>README extract</summary>

Object mapping, and more, for Redis and Python

[][package-url]
[][license-url]
[][ci-url]

Redis OM Python makes it easy to model Redis data in your Python applications.

📖 Read the Documentation | 🚀 Getting Started

Redis OM .NET | Redis OM Node.js | Redis OM Spring | Redis OM Python

 Table of contents

span

- 💡 Why Redis OM? ...

Example:
```python
import datetime
from typing import Optional

from pydantic import EmailStr

from redis_om import HashModel

class Customer(HashModel):
    first_name: str
    last_name: str
    email: EmailStr
    join_date: datetime.date
    age: int
    bio: Optional[str] = None
```

...

</details>

### jupysql

Better SQL in Jupyter

`pip install jupysql` · installs (wheel) · licence: Apache Software License · rank 10219 · last release 2025-03-25 · [PyPI](https://pypi.org/project/jupysql/) · [source](https://github.com/ploomber/jupysql)

<details><summary>README extract</summary>

Join our community
 Newsletter
 Contact us
 Docs
 Blog
 Website
 YouTube

> [!TIP]
> Deploy Streamlit and Dash apps for free on Ploomber Cloud!

Run SQL in Jupyter/IPython via a `%sql` and `%%sql` magics.

Features:
- Pandas integration
- SQL composition (no more hard-to-debug CTEs!)
- Plot massive datasets without blowing up memory
- DuckDB integration

Sections: JupySQL, Features, Documentation

</details>

### sqlalchemy-diff

A tool for comparing database schemas using SQLAlchemy

`pip install sqlalchemy-diff` · installs (wheel) · licence: Apache Software License · rank 10333 · last release 2026-11-04 · [PyPI](https://pypi.org/project/sqlalchemy-diff/)

<details><summary>README extract</summary>

A tool for comparing database schemas using SQLAlchemy.

- Python 3.10 or higher (supports 3.10, 3.11, 3.12, 3.13, 3.14, 3.15)
- SQLAlchemy >= 1.4

Example:
```python
from sqlalchemy import create_engine
from sqlalchemydiff.comparer import Comparer

# Create engines for the two databases you want to compare
engine_one = create_engine('postgresql://user:pass@host:port/db_one')
engine_two = create_engine('postgresql://user:pass@host:port/db_two')

# Create a comparer instance
...
```

Sections: SQLAlchemy Diff, Requirements, Usage, Quick Start, Aliases, Inspectors, Ignoring inspectors, Custom Inspectors, Creating a Custom Inspector, Example: A Custom Sequences Inspector

</details>

### dask-cuda

Utilities for Dask and CUDA interactions

`pip install dask-cuda` · installs (wheel) · licence: Apache-2.0 · rank 10364 · last release 2026-10-08 · [PyPI](https://pypi.org/project/dask-cuda/) · [docs](https://docs.rapids.ai/api/dask-cuda/stable/) · [source](https://github.com/rapidsai/dask-cuda)

<details><summary>README extract</summary>

Various utilities to improve deployment and management of Dask workers on
CUDA-enabled systems.

This library is experimental, and its API is subject to change at any time
without notice.

Example

Documentation is available here.

What this is not

This library does not automatically convert your Dask code to run on GPUs. ...

Example:
```python
from dask_cuda import LocalCUDACluster
from dask.distributed import Client

cluster = LocalCUDACluster()
client = Client(cluster)
```

</details>

### py-pglite

Python testing library for PGlite - in-memory PostgreSQL for tests

`pip install py-pglite` · installs (wheel) · licence: Apache-2.0 · rank 10385 · last release 2025-09-17 · [PyPI](https://pypi.org/project/py-pglite/) · [docs](https://github.com/wey-gu/py-pglite#readme) · [source](https://github.com/wey-gu/py-pglite)

<details><summary>README extract</summary>

A Pythonic interface for PGlite - the instant, zero-config PostgreSQL. ⚡️

`py-pglite` brings the magic of PGlite to Python with a high-level, developer-friendly API. Real PostgreSQL, instant testing.

`pip install py-pglite`

That's it. No Docker, no setup, no config files. Real PostgreSQL, instant testing.

Features:
The magic:

- 🎯 Zero config - No setup, no Docker, no servers
- ⚡ Instant - 2-3s startup vs 30-60s Docker
- 🔄 Isolated - Fresh database per test
- 🐘 Real PostgreSQL - JSON, arrays, window functions ...

Example:
```python
def test_users(pglite_session):
    user = User(name="Alice")
    pglite_session.add(user)
    pglite_session.commit()
    assert user.id == 1  # It's real PostgreSQL!
```

...

</details>

### upstash-vector

Serverless Vector SDK from Upstash

`pip install upstash-vector` · installs (wheel) · licence: MIT License · rank 10519 · last release 2025-02-27 · [PyPI](https://pypi.org/project/upstash-vector/) · [source](https://github.com/upstash/vector-py)

<details><summary>README extract</summary>

The Upstash Vector Python client

> [!NOTE]
> This project is in GA Stage.
> The Upstash Professional Support fully covers this project. It receives regular updates, and bug fixes.
> The Upstash team is committed to maintaining and improving its functionality.

Example:
```python
from upstash_vector import Index

index = Index(url=UPSTASH_VECTOR_REST_URL, token=UPSTASH_VECTOR_REST_TOKEN)
```

Sections: Upstash Vector Python SDK, Usage, Initializing the Index, Upsert Vectors, Query Vectors, Fetch Vectors, Range Over Vectors, Delete Vectors, Update a Vector, Reset the Namespace, Index Info, List Namespaces, Delete a Namespace, Preparing the environment

</details>

### aiosql

Simple SQL in Python

`pip install aiosql` · installs (wheel) · licence: BSD-2-Clause · rank 10533 · last release 2026-01-04 · [PyPI](https://pypi.org/project/aiosql/) · [docs](https://nackjicholson.github.io/aiosql/) · [source](https://github.com/nackjicholson/aiosql)

<details><summary>README extract</summary>

SQL is code.
Write it, version control it, comment it, and run it using files.
Writing your SQL code in Python programs as strings doesn't allow you to easily
reuse them in SQL GUIs or CLI tools like `psql`. ...

Features:
* You think SQL is pretty good, and writing SQL is an important part of your applications.
* You don't want to write your SQL in strings intermixed with your python code. ...

Example:
```python
import aiosql
import sqlite3

queries = aiosql.from_path("greetings.sql", "sqlite3")

with sqlite3.connect("greetings.db") as conn:
    user = queries.get_user_by_username(conn, username="willvaughn")
    # user: (1, "willvaughn", "William")

    for _, greeting in queries.get_all_greetings(conn):
...
```

...

</details>

### rleveldb

LevelDB reader for Python — Rust core with PyO3 bindings

`pip install rleveldb` · installs (wheel) · licence: MIT License · rank 10667 · last release 2026-04-10 · [PyPI](https://pypi.org/project/rleveldb/) · [source](https://github.com/DedInc/rleveldb)

<details><summary>README extract</summary>

A LevelDB reader for Python, implemented in Rust. Reads `.ldb` (SSTable), `.log` (write-ahead log), and `.sst` files without linking against the original C++ LevelDB library. Snappy decompression is handled internally.

The Python API follows the same shape as ccl_leveldb, so it can act as a drop-in for read workloads. ...

Example:
```python
import rleveldb

with rleveldb.RawLevelDb("/path/to/leveldb") as db:
    records = db.iterate_records_raw()

# Sort by sequence number to replay writes in order
records.sort(key=lambda r: r.seq)

state = {}
for rec in records:
    key = rec.user_key.decode("utf-8", errors="replace")
    if rec.state == rleveldb.KeyState.Live:
...
```

...

</details>

### ZODB

ZODB, a Python object-oriented database

`pip install ZODB` · installs (wheel) · licence: ZPL-2.1 · rank 10744 · last release 2026-10-12 · [PyPI](https://pypi.org/project/ZODB/) · [docs](http://zodb-docs.readthedocs.io) · [source](https://github.com/zopefoundation/ZODB)

<details><summary>README extract</summary>

ZODB provides an object-oriented database for Python that provides a
high-degree of transparency. ZODB runs on Python 3.10 and
above. It also runs on PyPy.

- no separate language for database operations

- very little impact on your code to make objects persistent

- no database mapper that partially hides the database. ...

Example:
```python
  conn.prefetch(obj, ...)

Where arguments can be objects, object ids, or iterables of objects
or object ids.

Added optional `prefetch` methods to the storage APIs. If a
storage doesn't support prefetch, then the connection prefetch
method is a noop.
```

...

</details>

### neomodel

An object mapper for the neo4j graph database.

`pip install neomodel` · installs (wheel) · licence: MIT License · rank 10760 · last release 2026-08-26 · [PyPI](https://pypi.org/project/neomodel/) · [docs](https://neomodel.readthedocs.io/en/latest/) · [source](http://github.com/neo4j-contrib/neomodel)

<details><summary>README extract</summary>

An Object Graph Mapper (OGM) for the neo4j graph
database, built on the awesome
neo4j_driver

If you need assistance with neomodel, please create an issue on the
GitHub repo found at <

- Familiar class based model definitions with proper inheritance.
- Powerful query API.
- Schema enforcement through cardinality restrictions. ...

Sections: Requirements, Documentation, New in 6.0.0, Breaking changes, Performance comparison, Running the test suite, Transpiling async -> sync, Specific async/sync code

</details>

### PySide2

Python bindings for the Qt cross-platform application and UI framework

`pip install PySide2` · does not install on CPython 3.14 · licence: GNU Library or Lesser General Public License (LGPL); Other/Proprietary License · rank 10897 · last release 2022-01-14 · [PyPI](https://pypi.org/project/PySide2/)

_README extract left out: share-alike licence._

### librmm-cu13

Library for CUDA memory management

`pip install librmm-cu13` · installs (wheel) · licence: Apache-2.0 · rank 11070 · last release 2026-10-08 · [PyPI](https://pypi.org/project/librmm-cu13/)

<details><summary>README extract</summary>

NOTE: For the latest stable README.md ensure you are on the `main` branch.

- RMM Reference Documentation: Python and C++ API references, tutorials, and topic guides.
- Installation: Instructions for installing RMM.
- GitHub Repository: Download the RMM source code.
- Issue Tracker: Report issues or request features.

Features:
Achieving optimal performance in GPU-centric workflows frequently requires customizing how host and
device memory are allocated. ...

Example:
```python
>>> import rmm
>>> buf = rmm.DeviceBuffer(size=100)
```

...

</details>

### sqlalchemy-monetdb

SQLAlchemy dialect for MonetDB

`pip install sqlalchemy-monetdb` · installs (wheel) · licence: MIT · rank 11131 · last release 2026-08-27 · [PyPI](https://pypi.org/project/sqlalchemy-monetdb/) · [source](https://github.com/MonetDB/sqlalchemy-monetdb)

<details><summary>README extract</summary>

This is the MonetDB dialect driver for SQLAlchemy 2.*. It has support for Python 3.8+ and PyPy. It supports
SQLalchemy 2.*.

Example:
```python
from sqlalchemy import create_engine
engine = create_engine('monetdb://monetdb:monetdb@localhost:50000/demo', echo=True)
```

Sections: MonetDB dialect for SQLAlchemy, Usage, More info

</details>

### sqltap

Profiling and introspection for applications using sqlalchemy

`pip install sqltap` · installs from source (sdist only) · licence: Apache Software License · rank 11134 · last release 2019-05-03 · [PyPI](https://pypi.org/project/sqltap/)

<details><summary>README extract</summary>

sqltap is a library that allows you to profile and introspect the
queries that your application makes using SQLAlchemy.

sqltap helps you quickly understand:

 * how many times a sql query is executed
 * how much time your sql queries take
 * where your application is issuing sql queries from ...

</details>

### redis-data-structures

Redis-backed data structures for building scalable and resilient applications

`pip install redis-data-structures` · installs (wheel) · licence: MIT License · rank 11164 · last release 2025-09-11 · [PyPI](https://pypi.org/project/redis-data-structures/) · [docs](https://github.com/vndee/redis-data-structures#readme) · [source](https://github.com/vndee/redis-data-structures)

<details><summary>README extract</summary>

A Python library providing high-level, Redis-backed data structures with a clean, Pythonic interface. Perfect for distributed systems, microservices, and any application requiring persistent, thread-safe data structures, especially in environments where multiple workers share the same data structure.

.png)

💡 Examples

Example:
```python
from redis_data_structures import Queue, Stack, Set, ConnectionManager

# Initialize connection
conn = ConnectionManager(host='localhost', port=6379, db=0)

# Create and use data structures
queue = Queue("tasks", connection_manager=conn)
queue.push({'id': 1, 'action': 'process'})

stack = Stack("commands", connection_manager=conn)
...
```

...

</details>

### ydb-sqlglot-plugin

YDB dialect plugin for sqlglot

`pip install ydb-sqlglot-plugin` · installs (wheel) · licence: Apache-2.0 · rank 11192 · last release 2026-06-02 · [PyPI](https://pypi.org/project/ydb-sqlglot-plugin/) · [source](https://github.com/ydb-platform/ydb-sqlglot-plugin)

<details><summary>README extract</summary>

YDB dialect plugin for sqlglot — bidirectional transpilation between YDB/YQL and any SQL dialect.

Example:
```python
import sqlglot

# Any dialect → YDB
result = sqlglot.transpile("SELECT * FROM users WHERE id = 1", read="mysql", write="ydb")[0]
# → SELECT * FROM `users` WHERE id = 1

# YDB → any dialect
result = sqlglot.transpile("$t = (SELECT id FROM users); SELECT * FROM $t AS t", read="ydb", write="postgres")[0]
...
```

Sections: ydb-sqlglot-plugin, Usage, What the plugin does, YDB syntax documentation conformance, Any SQL → YDB, Table names, CTEs → YDB variables, Subquery decorrelation, GROUP BY aliases, YDB → any SQL, CTEs reassembly, Column lineage, Function reference, Date / time

</details>

### rmm-cu13

Library for CUDA memory management

`pip install rmm-cu13` · installs (wheel) · licence: Apache-2.0 · rank 11197 · last release 2026-10-08 · [PyPI](https://pypi.org/project/rmm-cu13/)

<details><summary>README extract</summary>

NOTE: For the latest stable README.md ensure you are on the `main` branch.

- RMM Reference Documentation: Python and C++ API references, tutorials, and topic guides.
- Installation: Instructions for installing RMM.
- GitHub Repository: Download the RMM source code.
- Issue Tracker: Report issues or request features.

Features:
Achieving optimal performance in GPU-centric workflows frequently requires customizing how host and
device memory are allocated. ...

Example:
```python
>>> import rmm
>>> buf = rmm.DeviceBuffer(size=100)
```

...

</details>

### pgcopy

Fast db insert with postgresql binary copy

`pip install pgcopy` · installs (wheel) · licence: MIT License · rank 11217 · last release 2025-11-23 · [PyPI](https://pypi.org/project/pgcopy/)

<details><summary>README extract</summary>

Use pgcopy for fast data loading into
PostgreSQL with binary copy.

Features:
* Support for many data types
* Support for multi-dimensional array types
* Support for schema and schema search path
* Support for mixed-case table and column names
* Transparent string encoding
* Utility for replacing entire table

Example:
```python
from datetime import datetime
from pgcopy import CopyManager
import psycopg2
cols = ('id', 'timestamp', 'location', 'temperature')
now = datetime.now()
records = [
        (0, now, 'Jerusalem', 72.2),
        (1, now, 'New York', 75.6),
        (2, now, 'Moscow', 54.3),
    ]
conn = psycopg2.connect(database='weather_db')
...
```

Sections: pgcopy, Features, Quickstart, Documentation

</details>

### pylakekeeper

Official Lakekeeper client — generic-tables API and OAuth2 auth (static token / client_credentials with refresh)

`pip install pylakekeeper` · installs (wheel) · licence: Apache-2.0 · rank 11222 · last release 2026-09-21 · [PyPI](https://pypi.org/project/pylakekeeper/) · [docs](https://docs.lakekeeper.io/) · [source](https://github.com/lakekeeper/lakekeeper-clients)

<details><summary>README extract</summary>

Please visit for Documentation!

`pylakekeeper` is the official Python client for
Lakekeeper, an Apache-Licensed, secure,
fast and easy to use implementation of the
Apache Iceberg REST Catalog specification. ...

Example:
```python
from pylakekeeper import Client, StaticToken

lk = Client(
    base_url="
    warehouse="my-warehouse",
    auth=StaticToken("my-token"),
)

# Register a Lance dataset as a generic table
lk.generic_tables.create("ai.models", "embeddings", format="lance")

# Load it back with short-lived, vended S3 credentials
...
```

Sections: pylakekeeper — Lakekeeper Python Client, Quickstart, Scope and Features, Authentication Flows, Generic Table Operations, Storage Backends, Optional Extras, Examples, API Reference

</details>

### orchestra-sdk

Orchestra SDK for updating self-hosted Tasks.

`pip install orchestra-sdk` · installs (wheel) · licence: MIT License · rank 11390 · last release 2026-10-06 · [PyPI](https://pypi.org/project/orchestra-sdk/)

<details><summary>README extract</summary>

This is a lightweight SDK that allows Orchestra to interact with Self-hosted applications (Tasks).

The basic premise is that your self-hosted Task can send back status updates and logs to Orchestra once triggered asynchronously by Orchestra. This is done via HTTP requests.

Example:
```python
@orchestra.run()
def my_function(arg1, arg2=1):
    print("Running complex process")
```

Sections: Orchestra Python SDK, Task decorator, AWS Lambda, Updating Tasks manually, Sending logs, Setting outputs, Linked connections

</details>

### redis-dump-load

Dump and load redis databases

`pip install redis-dump-load` · installs from source (sdist only) · licence: BSD License · rank 11607 · last release 2016-09-10 · [PyPI](https://pypi.org/project/redis-dump-load/)

<details><summary>README extract</summary>

Dumps Redis data sets into a format suitable for long-term storage
(currently JSON) and loads data from such dump files back into Redis.

Features:
redis-dump-load:

- Supports all Redis data types;
- Dumps TTL and expiration times;
- Can load TTL OR original expiration time for expiring keys;
- Can create pretty/human-readable dumps (keys dumped in sorted order,
 output indented); ...

Example:
```python
import redisdl

json_text = redisdl.dumps()

with open('path/to/dump.json', 'w') as f:
    # streams data
    redisdl.dump(f)

json_text = '...'
redisdl.loads(json_text)

with open('path/to/dump.json') as f:
    # streams data if ijson or jsaone are installed
    redisdl.load(f)
```

...

</details>

### MySQL-python

Python interface to MySQL

`pip install MySQL-python` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 11776 · last release 2014-01-02 · [PyPI](https://pypi.org/project/MySQL-python/)

_README extract left out: share-alike licence._

### RLTest

Redis Modules Test Framework, allow to run tests on redis and modules on a variety of environments

`pip install RLTest` · installs (wheel) · licence: BSD License · rank 12031 · last release 2026-10-22 · [PyPI](https://pypi.org/project/RLTest/) · [source](https://github.com/RedisLabsModules/RLTest)

<details><summary>README extract</summary>

Redis Labs Test Framework, allow running tests on redis and modules on a variety of environments.

Supported Environment: oss, oss-cluster, enterprise, enterprise-cluster

The framework allow you to write a test without environment specification and then run the test on all supported environment.

Example:
```python
from RLTest import Env
import time

class testExample():
    '''
    run all tests on a single env without taking
    env down between tests
    '''
    def init(self):
        self.env = Env()

    def testExample(self):
        con = self.env.getConnection()
        con.set('x', 1)
        self.env.assertEqual(con.get('x'), '1')

...
```

Sections: RLTest, Usage, Sample usages, Multiple modules, Configuration File, Test Example, Shutdown grace period

</details>

### rust-store-py

Python binding (PyO3) for the rust-store multi-backend data engine: GQL parsing, permissions, computed columns and SQL dialect translation for MongoDB, MySQL, SQLite and PostgreSQL

`pip install rust-store-py` · installs (wheel) · licence: MIT · rank 12294 · last release 2026-11-08 · [PyPI](https://pypi.org/project/rust-store-py/) · [docs](https://coenddt.github.io/rust-store/) · [source](https://github.com/coenddt/rust-store)

<details><summary>README extract</summary>

`rust-store` 的 Python 绑定（PyO3）：把 Rust core 的 Command 契约暴露给 Python Host。

- 语言无关核心见 `../core`（GQL / 权限 / 计算列 / 命令规划 / SQL 方言翻译，纯逻辑无 IO）。
- 绑定层只做「dict in → dict out」的类型转换与转发，不持有数据库驱动，不执行任何 IO。
- Node 侧同构绑定见 `../core-node`（`rust-store-node`）。 ...

Example:
```python
from rust_store_py import Registry

reg = Registry()
reg.register({"name": "User", "collection": "users", "fields": {"name": {"type": "string"}}, "relations": {}})

plan = reg.plan_query("User{name}", {}, None)  # → Mongo 命令 JSON（dict）
```

Sections: rust-store-py, 安装, 使用, 命名规范与翻译摘要, Naming: freeform definitions, system-directed translation, 构建（开发）

</details>

### django-pgcrypto-fields

Encrypted fields for Django dealing with pgcrypto postgres extension.

`pip install django-pgcrypto-fields` · installs (wheel) · licence: BSD License · rank 12450 · last release 2021-01-06 · [PyPI](https://pypi.org/project/django-pgcrypto-fields/)

<details><summary>README extract</summary>

`django-pgcrypto-fields` is a `Django` extension which relies upon `pgcrypto` to
encrypt and decrypt data for fields.

 - postgres with `pgcrypto`
 - Supports Django 2.2.x, 3.0.x, 3.1.x and 3.2.x
 - Compatible with Python 3 only

 Last version of this library that supports `Django` 1.8.x, 1.9.x, 1.10.x
 was `django-pgcrypto-fields` 2.2.0. ...

Example:
```python
import os
BASEDIR = os.path.dirname(os.path.dirname(file))
PUBLIC_PGP_KEY_PATH = os.path.abspath(os.path.join(BASEDIR, 'public.key'))
PRIVATE_PGP_KEY_PATH = os.path.abspath(os.path.join(BASEDIR, 'private.key'))

# Used by PGPPublicKeyField used by default if not specified by the db
PUBLIC_PGP_KEY = open(PUBLIC_PGP_KEY_PATH).read()
...
```

...

</details>

### django-citext

PostgreSQL CIText integration for Django.

`pip install django-citext` · installs (wheel) · licence: BSD License · rank 12473 · last release 2025-12-01 · [PyPI](https://pypi.org/project/django-citext/)

<details><summary>README extract</summary>

Example:
```python
# myapp/models.py
from django.db import models
from citext import CITextField, CIEmailField

class MyModel(models.Model):
    name = CITextField()
    email = CIEmailField(unique=True)
```

Sections: Setup, Usage

</details>

### gooddata-sdk

GoodData Cloud Python SDK

`pip install gooddata-sdk` · installs (wheel) · licence: MIT · rank 12534 · last release 2026-11-04 · [PyPI](https://pypi.org/project/gooddata-sdk/) · [docs](https://www.gooddata.ai/docs/python-sdk/1.79.1) · [source](https://github.com/gooddata/gooddata-python-sdk)

<details><summary>README extract</summary>

The `gooddata-sdk` package provides a clean and convenient Python API to interact with GoodData.

At the moment the SDK provides services to inspect and interact with the Semantic Model and consume analytics:
* Catalog Workspaces Service
* Catalog Workspace Content Service
* Catalog Data Source Service
* Catalog User Service
* Catalog Permission ...

Example:
```python
import gooddata_sdk

# GoodData host in the form of uri
host = "
# GoodData user token
token = "some_user_token"
sdk = gooddata_sdk.GoodDataSdk.create(host, token)

workspace_id = "demo"
visualization_id = "customers_trend"
# reads visualization from workspace
visualization = sdk.visualizations.get_visualization(workspace_id, visualization_id)
...
```

Sections: GoodData Python SDK, Requirements, Example, Bugs & Requests

</details>

### mycli

Rich MySQL terminal client with autocompletion, syntax highlighting, and dataframes

`pip install mycli` · installs (wheel) · licence: BSD-3-Clause · rank 12549 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mycli/) · [docs](https://mycli.net/docs) · [source](https://github.com/dbcli/mycli)

<details><summary>README extract</summary>

Rich MySQL terminal client with auto-completion, syntax highlighting, and dataframes.

Homepage:

Documentation:

Mycli is known to be compatible with

 * MySQL
 * MariaDB
 * Percona
 * TiDB
 * Apache Doris

Postgres equivalent

 * pgcli

Features:
* Auto-completion as you type for SQL keywords as well as tables, views, columns, enums, and more!

 - `SELECT * FROM `tab will only show table names.
 - `SELECT * FROM users WHERE `tab will only show column names.
* Fuzzy history search using fzf. ...

Sections: mycli, Quick Start, Features, Usage, Shell Completions, Arch, Manjaro, Debian, Ubuntu, Fedora, Windows, Option 1: Native Windows, Option 2: WSL, Thanks, Compatibility, Configuration and Usage

</details>

### pyhdb

SAP HANA Database Client for Python

`pip install pyhdb` · installs from source (sdist only) · licence: Apache Software License · rank 12674 · last release 2018-02-16 · [PyPI](https://pypi.org/project/pyhdb/)

<details><summary>README extract</summary>

A pure Python client for the SAP HANA Database based on the SAP HANA Database SQL Command Network Protocol.

pyhdb supports Python 2.7, 3.3, 3.4, 3.5 and also PyPy on Linux, OSX and Windows. It implements a large part of the DBAPI Specification v2.0 (PEP 249). We plan to support Python 2.6 again in the future.

Example:
```python
>>> import pyhdb
>>> connection = pyhdb.connect(
    host="example.com",
    port=30015,
    user="user",
    password="secret"
)

>>> cursor = connection.cursor()
>>> cursor.execute("SELECT 'Hello Python World' FROM DUMMY")
>>> cursor.fetchone()
(u"Hello Python World",)

>>> connection.close()
```

...

</details>

### py2neo

Python client library and toolkit for Neo4j

`pip install py2neo` · installs (wheel) · licence: Apache Software License · rank 12827 · last release 2023-10-20 · [PyPI](https://pypi.org/project/py2neo/) · [docs](https://py2neo.org/2021.2/) · [source](https://github.com/technige/py2neo)

<details><summary>README extract</summary>

Please now consider this project to be EOL. There will be no more updates. It is recommended to use the official Neo4j drivers instead.

The version history of py2neo on PyPI got lost.
If you need an older version, you can install `py2neo-history` instead. ...

Example:
```python
>>> from py2neo import Graph
>>> graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
>>> graph.run("UNWIND range(1, 3) AS n RETURN n, n * n as n_sq")
   n | n_sq

   1 |    1
   2 |    4
   3 |    9
```

Sections: Py2neo, Quick Example, More

</details>

### plpygis

Python tools for PostGIS

`pip install plpygis` · installs (wheel) · licence: GPL-3.0-only · rank 12830 · last release 2025-09-30 · [PyPI](https://pypi.org/project/plpygis/) · [docs](https://plpygis.readthedocs.io/)

_README extract left out: share-alike licence._

### pgdb

PostgreSQL wrapper

`pip install pgdb` · installs from source (sdist only) · licence: Apache Software License · rank 12997 · last release 2021-07-29 · [PyPI](https://pypi.org/project/pgdb/)

### klepto

persistent caching to memory, disk, or database

`pip install klepto` · installs (wheel) · licence: BSD License · rank 13021 · last release 2026-01-19 · [PyPI](https://pypi.org/project/klepto/) · [docs](http://klepto.rtfd.io) · [source](https://github.com/uqfoundation/klepto)

<details><summary>README extract</summary>

`klepto` extends Python's `lru_cache` to utilize different keymaps and
alternate caching algorithms, such as `lfu_cache` and `mru_cache`.
While caching is meant for fast access to saved results, `klepto` also
has archiving capabilities, for longer-term storage. ...

Sections: klepto: persistent caching to memory, disk, or database, About Klepto, Major Features, Requirements, More Information

</details>

### bcpandas

High-level wrapper around BCP for high performance data transfers between pandas and SQL Server. No knowledge of BCP required!!

`pip install bcpandas` · does not install on CPython 3.14 · licence: MIT License · rank 13040 · last release 2024-12-16 · [PyPI](https://pypi.org/project/bcpandas/) · [source](https://github.com/yehoshuadimarsky/bcpandas)

<details><summary>README extract</summary>

High-level wrapper around BCP for high performance data transfers between pandas and SQL Server. No
knowledge of BCP required!! (pronounced _BEE-CEE-Pandas)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- Quickstart
- IMPORTANT - Read vs. ...

Features:
1. Because it is still much slower
2. Because you are forced to set the `chunksize` parameter to a very small number for it to work -
 generally a bit less then `2100/<number of columns>`. ...

Example:
```python
In [1]: import pandas as pd
   ...: import numpy as np
   ...:
   ...: from bcpandas import SqlCreds, to_sql

In [2]: creds = SqlCreds(
   ...:     'my_server',
   ...:     'my_db',
   ...:     'my_username',
...

</details>

### neo4j-driver

Neo4j Bolt driver for Python

`pip install neo4j-driver` · installs (wheel) · licence: Apache Software License · rank 13114 · last release 2026-10-15 · [PyPI](https://pypi.org/project/neo4j-driver/) · [source](https://github.com/neo4j/neo4j-python-driver)

<details><summary>README extract</summary>

This repository contains the official Neo4j driver for Python.

Starting with 5.0, the Neo4j Drivers will be moving to a monthly release
cadence. A minor version will be released on the last Friday of each month so
as to maintain versioning consistency with the core product (Neo4j DBMS) which
has also moved to a monthly cadence. ...

Example:
```python
from neo4j import GraphDatabase, RoutingControl

URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password")

def add_friend(driver, name, friend_name):
    driver.execute_query(
        "MERGE (a:Person {name: $name}) "
        "MERGE (friend:Person {name: $friend_name}) "
        "MERGE (a)-[:KNOWS]->(friend)",
...
```

Sections: Neo4j Bolt Driver for Python, Quick Example, Further Information

</details>

### sqlalchemy-file

SQLAlchemy-file is a SQLAlchemy extension for attaching files to SQLAlchemy model and uploading them to various storage.

`pip install sqlalchemy-file` · installs (wheel) · licence: MIT · rank 13291 · last release 2026-10-24 · [PyPI](https://pypi.org/project/sqlalchemy-file/) · [docs](https://jowilf.github.io/sqlalchemy-file) · [source](https://github.com/jowilf/sqlalchemy-file)

<details><summary>README extract</summary>

SQLAlchemy-file is a SQLAlchemy extension for attaching files to SQLAlchemy model and
uploading them to various storage such as Local Storage, Amazon S3, Rackspace CloudFiles, Google Storage and others
using Apache Libcloud.

The key features are:

* Multiple Storage : Use Object Storage API provided by Apache Libcloud to
 store files. ...

Example:
```python
import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy_file import File, FileField
from sqlalchemy_file.storage import StorageManager

Base = declarative_base()

...
```

...

</details>

### pyadomd

A pythonic approach to query SSAS data models

`pip install pyadomd` · installs from source (sdist only) · licence: Apache Software License · rank 13438 · last release 2022-01-22 · [PyPI](https://pypi.org/project/pyadomd/)

<details><summary>README extract</summary>

A pythonic approach to query SSAS data models.

Example:
```python
from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')

from pyadomd import Pyadomd

conn_str = 'Provider=MSOLAP;Data Source=localhost;Catalog=AdventureWorks;'
query = """EVALUATE Product"""

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        print(cur.fetchall())
```

Sections: pyadomd, Query SSAS Tabular model, Integrates easily with pandas, FAQ

</details>

### graphdatascience

A Python client for the Neo4j Graph Data Science (GDS) library

`pip install graphdatascience` · installs (wheel) · licence: Apache-2.0 · rank 13447 · last release 2026-10-29 · [PyPI](https://pypi.org/project/graphdatascience/) · [docs](https://neo4j.com/docs/graph-data-science-client/current/) · [source](https://github.com/neo4j/graph-data-science-client)

<details><summary>README extract</summary>

`graphdatascience` is a Python client for operating and working with the Neo4j Graph Data Science (GDS) library.
It enables users to write pure Python code to project graphs, run algorithms, as well as define and use machine learning pipelines in GDS.

The API is designed to mimic the GDS Cypher procedure API in Python code. ...

Example:
```python
from graphdatascience.session import AuraAPICredentials, DbmsConnectionInfo, GdsSessions, SessionMemory

sessions = GdsSessions(api_credentials=AuraAPICredentials("my-client-id", "my-client-secret"))

# Optional: estimate the session memory needed for your workload
...
```

Sections: Neo4j Graph Data Science Client, Getting started, GDS Sessions (Aura Graph Analytics), Self-managed Neo4j or GDS plugin, Documentation, Known limitations

</details>

### shiboken2

Python / C++ bindings helper module

`pip install shiboken2` · does not install on CPython 3.14 · licence: GNU Library or Lesser General Public License (LGPL); Other/Proprietary License · rank 13485 · last release 2022-01-14 · [PyPI](https://pypi.org/project/shiboken2/)

_README extract left out: share-alike licence._

### pymgclient

Memgraph database adapter for Python language

`pip install pymgclient` · installs (wheel) · licence: Apache-2.0 · rank 13663 · last release 2026-07-20 · [PyPI](https://pypi.org/project/pymgclient/) · [docs](https://memgraph.github.io/pymgclient) · [source](https://github.com/memgraph/pymgclient)

<details><summary>README extract</summary>

pymgclient is a Memgraph database adapter for Python
programming language compliant with the DB-API 2.0 specification described by
PEP 249.

mgclient module is the current implementation of the adapter. It is implemented
in C as a wrapper around mgclient, the
official Memgraph client library. ...

Example:
```python
>>> import mgclient

# Make a connection to the database
>>> conn = mgclient.connect(host='127.0.0.1', port=7687)

# Create a cursor for query execution
>>> cursor = conn.cursor()

# Execute a query
>>> cursor.execute("""
        CREATE (n:Person {name: 'John'})-[e:KNOWS]->
               (m:Person {name: 'Steve'})
        RETURN n, e, m
    """)

...
```

Sections: pymgclient - Memgraph database adapter for Python language, Documentation, Code sample

</details>

### dbt-vertica

Official vertica adapter plugin for dbt (data build tool)

`pip install dbt-vertica` · installs (wheel) · licence: Apache Software License · rank 13772 · last release 2026-09-22 · [PyPI](https://pypi.org/project/dbt-vertica/)

<details><summary>README extract</summary>

dbt adapter for Vertica. The adapter uses vertica-python to connect to your Vertica database.

For more information on using dbt with Vertica, consult the Vertica-Setup and Configuration pages. ...

Sections: dbt-vertica, dbt-vertica Versions Tested, dbt Core Features, dbt Fusion engine / ADBC, Sample Profile Configuration, Description of Profile Fields

</details>

### wren-core-py

Python bindings for Wren Engine semantic layer (wren-core)

`pip install wren-core-py` · installs (wheel) · licence: Apache Software License · rank 13779 · last release 2026-10-23 · [PyPI](https://pypi.org/project/wren-core-py/) · [source](https://github.com/Canner/WrenAI)

<details><summary>README extract</summary>

Python bindings for wren-core, the Rust semantic engine behind Wren Engine. Built with PyO3 and Maturin.

Wren Engine translates SQL queries through a semantic layer (MDL - Modeling Definition Language) and executes them against 22+ data sources (PostgreSQL, BigQuery, Snowflake, etc.).

Example:
```python
from wren_core import SessionContext

# Create a session context from a base64-encoded MDL JSON string
base64_mdl_json = "<your-base64-encoded-mdl-json>"
ctx = SessionContext(base64_mdl_json)

# Transform a SQL query through the semantic layer
planned_sql = ctx.transform_sql("SELECT * FROM my_model")
```

Sections: Wren Core Python Binding, Quick Start, Registering local files (Parquet/CSV), Concurrency, Environment Setup, Test and Build, Coding Style, Publishing

</details>

### mongomock-ng

Replacement fake pymongo stub for testing simple MongoDB-dependent code

`pip install mongomock-ng` · installs (wheel) · licence: ISC License (ISCL) · rank 13808 · last release 2026-07-24 · [PyPI](https://pypi.org/project/mongomock-ng/)

<details><summary>README extract</summary>

Example:
```python
import mongomock_ng as mongomock

client = mongomock.MongoClient()
db = client['test_db']
collection = db['test_collection']
collection.insert_one({'name': 'test', 'value': 42})
print(collection.find_one())
```

Sections: What is this?, 2 in action - we might write our test like so, Compatibility, Quick Start, Examples, Documentation, Code formatting, utcnow, Branching model, Releasing

</details>

### django-pgware

PostgreSQL utilities for Django: advisory locks, GUC management, and logging suppression

`pip install django-pgware` · installs (wheel) · licence: PostgreSQL · rank 13862 · last release 2026-06-21 · [PyPI](https://pypi.org/project/django-pgware/) · [source](https://github.com/Xof/django-pgware)

<details><summary>README extract</summary>

PostgreSQL utilities for Django: advisory locks, GUC management, and logging suppression.

Features:
A small, dependency-light toolkit of three independent PostgreSQL utilities for Django. Each is a context manager (and, where it makes sense, a decorator) that borrows Django's database connection, performs a session-scoped action, and reliably ...

Example:
```python
from django_pg_utils import advisory_lock

# Exclusive lock (blocks until acquired):
with advisory_lock("my-task") as acquired:
    assert acquired is True
    do_exclusive_work()

# Shared lock:
with advisory_lock("my-task", shared=True):
    do_shared_work()

# Non-blocking:
with advisory_lock("my-task", wait=False) as acquired:
    if acquired:
...
```

...

</details>

### fastapi-redis-sdk

The official Redis integration with FastAPI

`pip install fastapi-redis-sdk` · installs (wheel) · licence: MIT · rank 13902 · last release 2026-10-19 · [PyPI](https://pypi.org/project/fastapi-redis-sdk/) · [source](https://github.com/redis/fastapi-redis-sdk)

<details><summary>README extract</summary>

Idiomatic Redis integration for FastAPI - connection management and DI-based caching with automatic key consistency.

Features:
- Fluent setup — `FastAPIRedis(app).lifespan().caching()` configures pools and caching in one chain, attaching to the FastAPI lifespan events ...

Example:
```python
from fastapi import Depends, FastAPI
from redis_fastapi import FastAPIRedis, cache

app = FastAPI()
FastAPIRedis(app).lifespan().caching()

@app.get("/products/{product_id}", dependencies=[Depends(cache(ttl=300, eviction_group="products"))])
async def get_product(product_id: int):
    return await db.get_product(product_id)
```

Sections: Official FastAPI integration for Redis, Features, Requirements, Caching, Rate limiting, Sessions, Configuration

</details>

### hdf5storage

Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.

`pip install hdf5storage` · installs (wheel) · licence: BSD License · rank 13913 · last release 2025-09-30 · [PyPI](https://pypi.org/project/hdf5storage/)

<details><summary>README extract</summary>

Features:
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. ...

Sections: Overview, Dependencies, Running Tests

</details>

### ramp-packer

Packs for Redis modules into a distributable format

`pip install ramp-packer` · installs (wheel) · licence: BSD License · rank 13984 · last release 2026-06-04 · [PyPI](https://pypi.org/project/ramp-packer/)

<details><summary>README extract</summary>

Redis Automatic Module Packaging

Similar to `npm init`, this packer bundles Redis Modules for later distribution.

It gathers information from modules e.g.
module's name, command list, version and additional metadata.

Make sure redis-server is on your PATH. GitHub actions install this automatically.

Sections: RAMP, Prerequisites, Usage, Manifest mode, Command line mode, Full usage options, Packing, Module Capabilities, Output, Test

</details>

### generic-connection-pool

generic connection pool

`pip install generic-connection-pool` · installs (wheel) · licence: Unlicense · rank 14059 · last release 2026-06-07 · [PyPI](https://pypi.org/project/generic-connection-pool/)

<details><summary>README extract</summary>

`generic-connection-pool` is an extensible connection pool agnostic to the connection type it is managing.
It can be used for TCP, http, database or ssh connections.

Features:
- generic nature: can be used for any connection you desire (TCP, http, database, ssh, etc.)
- runtime agnostic: synchronous and asynchronous runtime supported
- flexibility: flexable connection retention and recycling policy ...

Example:
```python
import socket
import ssl
import urllib.parse
from http.client import HTTPResponse
from typing import Tuple

from generic_connection_pool.contrib.socket import SslSocketConnectionManager
from generic_connection_pool.threading import ConnectionPool

Hostname = str
Port = int
Endpoint = Tuple[Hostname, Port]
Connection = socket.socket

...
```

...

</details>

### fdb

Legacy Python driver for Firebird 2.5

`pip install fdb` · installs (wheel) · licence: BSD License · rank 14070 · last release 2025-07-22 · [PyPI](https://pypi.org/project/fdb/) · [docs](https://fdb.rtfd.io) · [source](https://github.com/FirebirdSQL/fdb)

<details><summary>README extract</summary>

This package provides LEGACY Python Database API 2.0-compliant driver for the open
source relational database Firebird version 2.5., with limited support for Firebird 3.0.
It does NOT support Firebird 4 and newer.

If you are using Firebird 3 or newer, please use the OFFICIAL Python driver for Firebird
called firebird-driver. ...

Sections: FDB - legacy Firebird driver for Python, Important, Documentation

</details>

### firebirdsql

Firebird RDBMS bindings for python.

`pip install firebirdsql` · installs from source (sdist only) · licence: not stated · rank 14125 · last release 2026-10-25 · [PyPI](https://pypi.org/project/firebirdsql/)

<details><summary>README extract</summary>

firebirdsql package is a set of Firebird RDBMS ( bindings for Python (Written in pure Python : no C compiler needed or fbclient library)

Sorry, it support Firebird 2.5+.

It works on Python 3.10+.

- TimeZone feature in Firebird 4.0+
- asyncio API

Example:
```python
import firebirdsql
conn = firebirdsql.connect(
    host='localhost',
    database='/foo/bar.fdb',
    port=3050,
    user='alice',
    password='secret'
)
cur = conn.cursor()
cur.execute("select * from baz")
for c in cur.fetchall():
    print(c)
conn.close()
```

Sections: PyfirebirdSQL, Example, Python Database API Specification v2.0, asyncio

</details>

### dbf

Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf files (including memos)

`pip install dbf` · installs (wheel) · licence: BSD License · rank 14204 · last release 2025-09-02 · [PyPI](https://pypi.org/project/dbf/)

<details><summary>README extract</summary>

Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is returned as unicode, and codepage settings in tables are honored. Memos and Null fields are supported. Documentation needs work, but author is very responsive to e-mails. ...

</details>

### hopsworks-aiomysql

MySQL driver for asyncio.

`pip install hopsworks-aiomysql` · installs (wheel) · licence: MIT License · rank 14410 · last release 2026-10-01 · [PyPI](https://pypi.org/project/hopsworks-aiomysql/)

<details><summary>README extract</summary>

aiomysql is a "driver" for accessing a `MySQL` database
from the asyncio (PEP-3156/tulip) framework. It depends on and reuses most
parts of PyMySQL . *aiomysql* tries to be like awesome aiopg library and
preserve same api, look and feel. ...

Example:
```python
import asyncio
import aiomysql

async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
...
```

...

</details>

### pyturso

Turso is an in-process SQL database written in Rust, compatible with SQLite.

`pip install pyturso` · installs (wheel) · licence: MIT License · rank 14428 · last release 2026-10-12 · [PyPI](https://pypi.org/project/pyturso/) · [source](https://github.com/tursodatabase/turso)

<details><summary>README extract</summary>

Turso Database runs in production today at multiple organizations. It has not yet reached 1.0, so as with any database we recommend keeping backups — see the FAQ for where the project stands.

Features:
- SQLite compatible: SQLite query language and file format support (status).
- In-process: No network overhead, runs directly in your Python process
- Cross-platform: Supports Linux, macOS, Windows ...

Example:
```python
import turso

# Standard DB-API usage
conn = turso.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
cur.execute("INSERT INTO users VALUES (1, 'alice'), (2, 'bob')")

cur.execute("SELECT * FROM users ORDER BY id")
rows = cur.fetchall()
print(rows)  # [(1, 'alice'), (2, 'bob')]

...
```

...

</details>

### morph-kgc

Powerful [R2]RML engine to create RDF knowledge graphs from heterogeneous data sources.

`pip install morph-kgc` · installs (wheel) · licence: Apache-2.0 · rank 14568 · last release 2026-01-20 · [PyPI](https://pypi.org/project/morph-kgc/) · [docs](https://morph-kgc.readthedocs.io) · [source](https://github.com/morph-kgc/morph-kgc)

<details><summary>README extract</summary>

Morph-KGC is an engine that constructs RDF knowledge graphs from heterogeneous data sources with the R2RML and RML mapping languages. Morph-KGC is built on top of pandas and it leverages *mapping partitions* to significantly reduce execution times and memory consumption for large data sources.

Features:
- User-friendly mappings with YARRRML.
- Transformation functions with RML-FNML, including Python UDFs.
- RDF-star generation with RML-star.
- RML views over tabular data sources and JSON files.
- Integration with RDFLib, Oxigraph and Kafka. ...

Example:
```python
import morph_kgc

# generate the triples and load them to an RDFLib graph
g_rdflib = morph_kgc.materialize('/path/to/config.ini')
# work with the RDFLib graph
...

</details>

### pymongoexplain

Explainable CRUD API for PyMongo

`pip install pymongoexplain` · installs (wheel) · licence: Apache Software License · rank 14592 · last release 2022-01-07 · [PyPI](https://pypi.org/project/pymongoexplain/)

<details><summary>README extract</summary>

:Info: Explain collections in PyMongo. See
 GitHub
 for the latest source.
:Author: Julius Park

This package provides an `ExplainableCollection` class that allows PyMongo's Collection methods to be explained

PyMongoExplain greatly simplifies the amount of effort needed to explain commands. ...

Example:
```python
from pymongoexplain import ExplainableCollection

collection = client.db.products
explain = ExplainableCollection(collection)
```

Sections: PyMongoExplain, About, Bugs / Feature Requests, How To Ask For Help, Dependencies, Tutorial, Explaining commands in a script, Limitations

</details>

### dj-anonymizer

dj_anonymizer is a utility designed to anonymize production databases with various types of mock data, specifically designed for use within Django projects.

`pip install dj-anonymizer` · installs (wheel) · licence: MIT License · rank 14745 · last release 2026-09-18 · [PyPI](https://pypi.org/project/dj-anonymizer/)

<details><summary>README extract</summary>

dj_anonymizer is a utility designed to anonymize production databases with various types of mock data, specifically designed for use within Django projects.

Project works with Django 4.2 or higher and Python 3.8 or higher.

Sections: dj_anonymizer, Documentation

</details>

### odmantic

ODMantic, an AsyncIO MongoDB Object Document Mapper for Python using type hints

`pip install odmantic` · installs (wheel) · licence: ISC License (ISCL) · rank 14754 · last release 2026-01-24 · [PyPI](https://pypi.org/project/odmantic/) · [docs](https://art049.github.io/odmantic) · [source](https://github.com/art049/odmantic)

<details><summary>README extract</summary>

Documentation:

Sync and Async ODM (Object Document Mapper) for MongoDB based on standard Python type hints. Built on top of Pydantic for model
definition and validation.

Core features:

- Simple: define your model by typing your fields using Python types, build queries
 using Python comparison operators ...

Example:
```python
from typing import Optional

from odmantic import Field, Model

class Publisher(Model):
    name: str
    founded: int = Field(ge=1440)
    location: Optional[str] = None
```

Sections: ODMantic, Requirements, Example, Define your first model, Create some instances, Populate the database with your instances, Find instances matching a criteria, Modify an instance, Next steps

</details>

### pydgraph

Official Dgraph client implementation for Python

`pip install pydgraph` · installs (wheel) · licence: Apache-2.0 · rank 14769 · last release 2026-02-25 · [PyPI](https://pypi.org/project/pydgraph/)

<details><summary>README extract</summary>

This is the official Dgraph database client implementation for Python (Python >= v3.9), using
gRPC.

Before using this client, we highly recommend that you read the the product documentation at

Example:
```python
import asyncio
import pydgraph

async def main():
    # Create async client
    client_stub = pydgraph.AsyncDgraphClientStub('localhost:9080')
    client = pydgraph.AsyncDgraphClient(client_stub)

    try:
        # Login
        await client.login("groot", "password")

        # Alter schema
        await client.alter(pydgraph.Operation(
...
```

...

</details>

### cognite-neat

Knowledge graph transformation

`pip install cognite-neat` · installs (wheel) · licence: Apache-2.0 · rank 14784 · last release 2026-09-09 · [PyPI](https://pypi.org/project/cognite-neat/) · [docs](https://cognite-neat.readthedocs-hosted.com/) · [source](https://github.com/cognitedata/neat)

<details><summary>README extract</summary>

There was no easy way to make knowledge graphs, especially data models, and onboard them to
Cognite Data Fusion, so we have built NEAT.

NEAT is great for data model development, validation and deployment. ...

Example:
```python
from cognite.neat import NeatSession, get_cognite_client

client = get_cognite_client(".env")

neat = NeatSession(client)

neat.physical_data_model.read.cdf("cdf_cdm", "CogniteCore", "v1")
```

Sections: kNowlEdge grAph Transformer (NEAT), Usage, Documentation

</details>

### foundationdb

Python bindings for the FoundationDB Database

`pip install foundationdb` · installs (wheel) · licence: Apache-2.0 · rank 14847 · last release 2026-10-02 · [PyPI](https://pypi.org/project/foundationdb/) · [source](https://github.com/apple/foundationdb)

<details><summary>README extract</summary>

Complete documentation of the FoundationDB Python API can be found at

These bindings require the FoundationDB client. The client can be obtained from

</details>

### firestore

An offline-available ORM-like wrapper for Google Firestore Database

`pip install firestore` · installs (wheel) · licence: MIT License · rank 14873 · last release 2019-08-26 · [PyPI](https://pypi.org/project/firestore/)

<details><summary>README extract</summary>

:Details: Firestore is an offline available ORM/ODM atop Google Firestore.
:Repository:
:Author: Workenvoy Inc (
:Maintainer: Raymond Ortserga (

Firestore is a Python Object-Document/Object-Collections Mapper for working with Google Firestore.
The Flexible, Extremely Scalable, realtime database by Google. ...

Sections: Firestore, Details, Dependencies, Examples

</details>

## Also in this topic

- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
