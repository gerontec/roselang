# Unclassified / A (part 1 of 2)

[Index](README.md) · 752 packages in this topic, by downloads.

part 1 · [part 2](unclassified-a-2.md)

### anyio

High-level concurrency and networking framework on top of asyncio or Trio

`pip install anyio` · installs (wheel) · licence: MIT · rank 23 · last release 2026-11-01 · [PyPI](https://pypi.org/project/anyio/) · [docs](https://anyio.readthedocs.io/en/latest/) · [source](https://github.com/agronholm/anyio)

<details><summary>README extract</summary>

AnyIO is an asynchronous networking and concurrency library that works on top of either asyncio or
Trio. It implements Trio-like structured concurrency (SC) on top of asyncio and works in harmony
with the native SC of Trio itself.

Applications and libraries written against AnyIO's API will run unmodified on either asyncio or
Trio. ...

Features:
AnyIO offers the following functionality:

* Task groups (nurseries in trio terminology)
* High-level networking (TCP, UDP and UNIX sockets) ...

Sections: Documentation, Features

</details>

### attrs

Classes Without Boilerplate

`pip install attrs` · installs (wheel) · licence: MIT · rank 29 · last release 2026-03-19 · [PyPI](https://pypi.org/project/attrs/) · [docs](https://www.attrs.org/) · [source](https://github.com/python-attrs/attrs)

<details><summary>README extract</summary>

*attrs* is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods).
Trusted by NASA for Mars missions since 2020!

Its main goal is to help you to write concise and correct software without slowing down your code.

Example:
```python
>>> from attrs import asdict, define, make_class, Factory

>>> @define
... class SomeClass:
...     a_number: int = 42
...     list_of_numbers: list[int] = Factory(list)
...
...     def hard_math(self, another_number):
...         return self.a_number + sum(self.list_of_numbers) * another_number

>>> sc = SomeClass(1, [1, 2, 3])
>>> sc
...
```

...

</details>

### aiobotocore

Async client for aws services using botocore and aiohttp

`pip install aiobotocore` · installs (wheel) · licence: Apache-2.0 · rank 39 · last release 2026-10-23 · [PyPI](https://pypi.org/project/aiobotocore/) · [docs](https://aiobotocore.aio-libs.org) · [source](https://github.com/aio-libs/aiobotocore)

<details><summary>README extract</summary>

Example:
```python
import asyncio
from aiobotocore.session import get_session

AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"

async def go():
    bucket = 'dataintake'
    filename = 'dummy.bin'
    folder = 'aiobotocore'
    key = '{}/{}'.format(folder, filename)

    session = get_session()
...
```

Sections: Basic Example, Context Manager Examples, Enable type checking and code completion, Requirements, Changes, 3.10.0 (2026-10-23), 3.9.2 (2026-09-30), 3.9.1 (2026-08-20), 3.9.0 (2026-08-01), 3.8.0 (2026-07-17), 3.7.0 (2026-05-09), 3.6.0 (2026-04-30), 3.5.0 (2026-04-19), 3.4.0 (2026-04-07)

</details>

### aiosignal

aiosignal: a list of registered asynchronous callbacks

`pip install aiosignal` · installs (wheel) · licence: Apache Software License · rank 71 · last release 2025-07-03 · [PyPI](https://pypi.org/project/aiosignal/)

<details><summary>README extract</summary>

A project to manage callbacks in `asyncio` projects.

`Signal` is a list of registered asynchronous callbacks.

The signal's life-cycle has two stages: after creation its content
could be filled by using standard list operations: `sig.append()`
etc. ...

Sections: aiosignal, Introduction, Documentation, Source code

</details>

### azure-core

Microsoft Azure Core Library for Python

`pip install azure-core` · installs (wheel) · licence: not stated · rank 185 · last release 2026-05-07 · [PyPI](https://pypi.org/project/azure-core/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core)

<details><summary>README extract</summary>

Azure core provides shared exceptions and modules for Python SDK client libraries.
These libraries follow the Azure SDK Design Guidelines for Python .

If you are a client library developer, please reference client library developer reference for more information.

Source code
| Package (Pypi)
| Package (Conda)
| API reference documentation

Features:
- `AZURE_LOG_LEVEL` now accepts `VERBOSE` (case-insensitive) as an alias for `DEBUG`. #46668

Example:
```python
class AzureError(Exception):
    def init(self, message, *args, **kwargs):
        self.inner_exception = kwargs.get("error")
        self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
        self.exc_type = self.exc_type.name if self.exc_type else type(self.inner_exception)
...
```

...

</details>

### azure-identity

Microsoft Azure Identity Library for Python

`pip install azure-identity` · installs (wheel) · licence: MIT · rank 239 · last release 2026-10-26 · [PyPI](https://pypi.org/project/azure-identity/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

The Azure Identity library provides Microsoft Entra ID token-based authentication support across the Azure SDK. It provides a set of `TokenCredential`/`SupportsTokenInfo` implementations, which can be used to construct Azure SDK clients that support Microsoft Entra token authentication. ...

Features:
- Added support for `WorkloadIdentityCredential` identity binding mode in AKS environments. This feature uses an AKS proxy to handle FIC exchanges on behalf of pods, addressing Entra's limit on federated identity credentials per managed identity. ...

Example:
```python
from azure.identity.aio import DefaultAzureCredential

# call close when the credential is no longer needed
credential = DefaultAzureCredential()
...
await credential.close()

...

</details>

### aiofiles

File support for asyncio.

`pip install aiofiles` · installs (wheel) · licence: Apache Software License · rank 241 · last release 2025-10-09 · [PyPI](https://pypi.org/project/aiofiles/) · [source](https://github.com/Tinche/aiofiles)

<details><summary>README extract</summary>

Features:
- a file API very similar to Python's standard, blocking API
- support for buffered and unbuffered binary files, and buffered text files
- support for `async`/`await` (PEP 492) constructs
- async interface to tempfile module

Example:
```python
async with aiofiles.tempfile.NamedTemporaryFile('wb+') as f:
    await f.write(b'Line1\n Line2')
    await f.seek(0)
    async for line in f:
        print(line)

async with aiofiles.tempfile.TemporaryDirectory() as d:
    filename = os.path.join(d, "file.ext")
```

Sections: Features, Usage, Tempfile, Writing tests for aiofiles

</details>

### azure-storage-blob

Microsoft Azure Blob Storage Client Library for Python

`pip install azure-storage-blob` · installs (wheel) · licence: MIT License · rank 288 · last release 2026-10-29 · [PyPI](https://pypi.org/project/azure-storage-blob/)

<details><summary>README extract</summary>

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.

Blob storage is ideal for: ...

Example:
```python
from azure.storage.blob import BlobServiceClient

service = BlobServiceClient(account_url=" credential=credential)
```

Sections: Azure Storage Blobs client library for Python, Getting started, Prerequisites, Create a storage account, Create the client, Looking up the account URL, Types of credentials, Create a logger for the 'azure.storage.blob' SDK, Configure a console output

</details>

### awscli

Universal Command Line Environment for AWS.

`pip install awscli` · installs (wheel) · licence: Apache Software License · rank 310 · last release 2026-11-05 · [PyPI](https://pypi.org/project/awscli/) · [source](https://github.com/aws/aws-cli)

<details><summary>README extract</summary>

This package provides a unified command line interface to Amazon Web
Services.

Jump to:

- Getting Started
- Getting Help
- More Resources

The AWS CLI v1 entered maintenance mode on August 5, 2026 and will reach
end-of-support on July 15, 2027. During maintenance mode, AWS limits releases
to critical bug fixes and security issues only. ...

Sections: aws-cli, AWS CLI v1 is in Maintenance Mode, Getting Started, Requirements, Notices, Configuration, Basic Commands, Command Completion, Getting Help, More Resources

</details>

### awswrangler

Pandas on AWS.

`pip install awswrangler` · installs (wheel) · licence: Apache-2.0 · rank 320 · last release 2026-10-27 · [PyPI](https://pypi.org/project/awswrangler/) · [docs](https://aws-sdk-pandas.readthedocs.io/) · [source](https://github.com/aws/aws-sdk-pandas)

<details><summary>README extract</summary>

*Pandas on AWS*

Easy integration with Athena, Glue, Redshift, Timestream, OpenSearch, Neptune, QuickSight, Chime, CloudWatchLogs, DynamoDB, EMR, SecretManager, PostgreSQL, MySQL, SQLServer and S3 (Parquet, CSV, JSON and EXCEL).

> An AWS Professional Service open source initiative | aws-proserve-opensource@amazon.com ...

Sections: AWS SDK for pandas (awswrangler), Quick Start, At scale, Read The Docs, Getting Help, Logging

</details>

### antlr4-python3-runtime

ANTLR 4.13.2 runtime for Python 3

`pip install antlr4-python3-runtime` · installs (wheel) · licence: BSD · rank 421 · last release 2024-08-03 · [PyPI](https://pypi.org/project/antlr4-python3-runtime/)

### aiohttp-retry

Simple retry client for aiohttp

`pip install aiohttp-retry` · installs (wheel) · licence: MIT License · rank 444 · last release 2024-11-06 · [PyPI](https://pypi.org/project/aiohttp-retry/)

<details><summary>README extract</summary>

Python 3.7 or higher.

Install: `pip install aiohttp-retry`.

- Everything between [2.7.0 - 2.8.3) is yanked.
There is a bug with evaluate_response_callback, it led to infinite retries

- 2.8.0 is incorrect and yanked.

- Since 2.5.6 this is a new parameter in ```get_timeout``` func called "response". ...

Example:
```python
from aiohttp_retry import RetryClient, ExponentialRetry

async def main():
    retry_options = ExponentialRetry(attempts=1)
    retry_client = RetryClient(raise_for_status=False, retry_options=retry_options)
    async with retry_client.get(' as response:
        print(response.status)

    await retry_client.close()
```

...

</details>

### amqp

Low-level AMQP client for Python (fork of amqplib).

`pip install amqp` · installs (wheel) · licence: BSD License · rank 446 · last release 2026-11-02 · [PyPI](https://pypi.org/project/amqp/)

<details><summary>README extract</summary>

:Version: 5.4.2
:Web:
:Download:
:Source:
:DeepWiki:
:Keywords: amqp, rabbitmq

This is a fork of amqplib which was originally written by Barry Pederson.
It is maintained by the Celery project, and used by kombu as a pure python
alternative when librabbitmq is not available.

This library should be API compatible with librabbitmq. ...

Example:
```python
import amqp

with amqp.Connection('broker.example.com') as c:
    ch = c.channel()
    ch.basic_publish(amqp.Message('Hello World'), routing_key='test')
```

Sections: Python AMQP 0.9.1 client library, About, Differences from amqplib, Quick overview, Speedups, Further, py-amqp as part of the Tidelift Subscription

</details>

### APScheduler

In-process task scheduler with Cron-like capabilities

`pip install APScheduler` · installs (wheel) · licence: MIT License · rank 513 · last release 2026-06-28 · [PyPI](https://pypi.org/project/APScheduler/) · [docs](https://apscheduler.readthedocs.io/en/3.x/) · [source](https://github.com/agronholm/apscheduler)

<details><summary>README extract</summary>

Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code
to be executed later, either just once or periodically. You can add new jobs or remove old ones on
the fly as you please. If you store your jobs in a database, they will also survive scheduler
restarts and maintain their state. ...

Sections: Documentation, Source, Reporting bugs, Getting help

</details>

### altair

Vega-Altair: A declarative statistical visualization library for Python.

`pip install altair` · installs (wheel) · licence: BSD License · rank 519 · last release 2026-09-15 · [PyPI](https://pypi.org/project/altair/) · [docs](https://altair-viz.github.io) · [source](https://github.com/vega/altair)

<details><summary>README extract</summary>

Vega-Altair is a declarative statistical visualization library for Python. With Vega-Altair, you can spend more time understanding your data and its meaning. Vega-Altair's
API is simple, friendly and consistent and built on top of the powerful
Vega-Lite JSON specification. ...

Features:
- Carefully-designed, declarative Python API.
- Auto-generated internal Python API that guarantees visualizations are type-checked and
 in full conformance with the Vega-Lite
 specification. ...

Example:
```python
import altair as alt

# load a simple dataset as a pandas DataFrame
from altair.datasets import data

cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
)
```

...

</details>

### azure-keyvault-secrets

Microsoft Corporation Key Vault Secrets Client Library for Python

`pip install azure-keyvault-secrets` · installs (wheel) · licence: MIT License · rank 521 · last release 2026-10-28 · [PyPI](https://pypi.org/project/azure-keyvault-secrets/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk)

<details><summary>README extract</summary>

Azure Key Vault helps solve the following problems:

- Secrets management (this library) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets
- Cryptographic key management
(azure-keyvault-keys) -
create, store, and control access to the keys used to encrypt your data ...

Features:
- Added support for service API version `2025-07-01`
 - Added support for retrieving secrets with `out_content_type`
 - Added the `previous_version` property to `SecretProperties`

Example:
```python
VAULT_URL = os.environ["VAULT_URL"]
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)
```

...

</details>

### async-lru

Simple LRU cache for asyncio

`pip install async-lru` · installs (wheel) · licence: MIT License · rank 525 · last release 2026-10-12 · [PyPI](https://pypi.org/project/async-lru/)

<details><summary>README extract</summary>

:info: Simple lru cache for asyncio

Example:
```python
import asyncio

import aiohttp
from async_lru import alru_cache

@alru_cache(maxsize=32)
async def get_pep(num):
    resource = ' % num
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(resource) as s:
                return await s.read()
        except aiohttp.ClientError:
...
```

Sections: async-lru, Usage, Custom cache keys, Limitations, Benchmarks, Thanks

</details>

### azure-common

Microsoft Azure Client Library for Python (Common)

`pip install azure-common` · installs (wheel) · licence: MIT License · rank 564 · last release 2022-02-03 · [PyPI](https://pypi.org/project/azure-common/)

<details><summary>README extract</summary>

This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, refer to the main Github repository:

Sections: Microsoft Azure SDK for Python, 1.1.28 (2022-02-03), 1.1.27 (2021-03-23), 1.1.26 (2020-11-10), 1.1.25 (2020-03-09), 1.1.24 (2019-12-18), 1.1.23 (2019-06-24), 1.1.22 (2019-06-06), 1.1.21 (2019-05-21), 1.1.20 (2019-04-30), 1.1.19 (2019-04-18), 1.1.18 (2019-01-29), 1.1.17 (2019-01-15), 1.1.16 (2018-09-26)

</details>

### amazon-ion

Amazon Ion

`pip install amazon-ion` · installs from source (sdist only) · licence: not stated · rank 619 · last release 2026-09-11 · [PyPI](https://pypi.org/project/amazon-ion/) · [docs](https://ion-python.readthedocs.io/en/latest/?badge=latest)

<details><summary>README extract</summary>

An implementation of Amazon Ion
for Python.

This package is designed to work with Python 3.8+. Newer language features will be used as deemed valuable. Support may be dropped for versions more than six months past EOL.

Example:
```python
>>> import amazon.ion.simpleion as ion
>>> obj = ion.loads('{abc: 123}')
>>> obj['abc']
123
>>> ion.dumps(obj, binary=False)
'$ion_1_0 {abc:123}'
```

Sections: Amazon Ion Python, Getting Started, Git Setup, Tox Setup, TODO, Known Issues

</details>

### aioboto3

Async boto3 wrapper

`pip install aioboto3` · installs (wheel) · licence: Apache Software License · rank 628 · last release 2025-10-30 · [PyPI](https://pypi.org/project/aioboto3/) · [docs](https://readthedocs.org/projects/aioboto3/) · [source](https://github.com/terricain/aioboto3)

<details><summary>README extract</summary>

Breaking changes for v11: The S3Transfer config passed into upload/download_file etc.. has been updated to that it matches what boto3 uses

Breaking changes for v9: aioboto3.resource and aioboto3.client methods no longer exist, make a session then call session.client etc... ...

Features:
* Closely mimics the usage of boto3.

Example:
```python
import asyncio
import aioboto3
from boto3.dynamodb.conditions import Key

async def main():
    session = aioboto3.Session()
    async with session.resource('dynamodb', region_name='eu-central-1') as dynamo_resource:
        table = await dynamo_resource.Table('test_table')

        await table.put_item(
...
```

...

</details>

### azure-monitor-opentelemetry-exporter

Microsoft Azure Monitor Opentelemetry Exporter Client Library for Python

`pip install azure-monitor-opentelemetry-exporter` · installs (wheel) · licence: MIT License · rank 732 · last release 2026-11-05 · [PyPI](https://pypi.org/project/azure-monitor-opentelemetry-exporter/)

<details><summary>README extract</summary>

The exporter for Azure Monitor allows Python applications to export data from the OpenTelemetry SDK to Azure Monitor. The exporter is intended for users who require advanced configuration or have more complicated telemetry needs that require all of distributed tracing, logging and metrics. ...

Example:
```python
"""
An example to show an application using all instruments in the OpenTelemetry SDK. Metrics created
and recorded using the sdk are tracked and telemetry is exported to application insights with the
AzureMonitorMetricsExporter.
"""
import os
from typing import Iterable

from opentelemetry import metrics
...
```

...

</details>

### awscrt

A common runtime for AWS Python projects

`pip install awscrt` · installs (wheel) · licence: Apache-2.0 · rank 734 · last release 2026-11-04 · [PyPI](https://pypi.org/project/awscrt/) · [docs](https://awslabs.github.io/aws-crt-python) · [source](https://github.com/awslabs/aws-crt-python)

<details><summary>README extract</summary>

Python 3 bindings for the AWS Common Runtime.

* API documentation
* Development guide for contributors to aws-crt-python's source code.

Example:
```python
import logging
from awscrt.logging import init_logging, CRT_LOG_FORMAT

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(CRT_LOG_FORMAT))
logging.getLogger('awscrt').addHandler(handler)
init_logging(logging.DEBUG)
```

Sections: AWS CRT Python, Minimum Requirements, Fork and Multiprocessing, macOS TLS Configuration, Keychain Behavior, Logging, Option 1: Python logging integration (recommended), Option 2: Direct file/stdout logging, Which should I use?, Crash Handler, Advanced Build Options, OpenSSL and LibCrypto, AWS_CRT_BUILD_USE_SYSTEM_LIBS, AWS_EXTRA_LIB_DIR

</details>

### adal

Note: This library is already replaced by MSAL Python, available here: https://pypi.org/project/msal/ .ADAL Python remains available here as a legacy. The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.

`pip install adal` · installs (wheel) · licence: MIT License · rank 748 · last release 2021-04-05 · [PyPI](https://pypi.org/project/adal/)

<details><summary>README extract</summary>

This library, ADAL for Python, will no longer receive new feature improvements. Instead, use the new library
MSAL for Python.

* If you are starting a new project, you can get started with the
 MSAL Python docs
 for details about the scenarios, usage, and relevant concepts. ...

Sections: Samples and Documentation, Versions, Submit Feedback

</details>

### azure-mgmt-core

Microsoft Azure Management Core Library for Python

`pip install azure-mgmt-core` · installs (wheel) · licence: MIT License · rank 758 · last release 2025-07-03 · [PyPI](https://pypi.org/project/azure-mgmt-core/)

<details><summary>README extract</summary>

Azure management core library defines extensions to Azure Core that are specific to ARM (Azure Resource Management) needed when you use client libraries.

As an end user, you don't need to manually install azure-mgmt-core because it will be installed automatically when you install other SDKs. ...

Features:
- Added helper function `get_arm_endpoints` to get the ARM endpoint and credential scopes from the cloud setting.

Sections: Azure Management Core Library, 1.6.0 (2025-07-02), Other Changes, 1.5.0 (2024-10-31), Features Added, 1.4.0 (2023-04-06), Features, 1.3.2 (2022-08-11), 1.3.1 (2022-06-14), 1.3.0 (2021-07-01)

</details>

### azure-storage-queue

Microsoft Corporation Azure Storage Queue Client Library for Python

`pip install azure-storage-queue` · installs (wheel) · licence: MIT · rank 819 · last release 2026-10-29 · [PyPI](https://pypi.org/project/azure-storage-queue/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure Queue storage is a service for storing large numbers of messages that can be accessed from anywhere in the world via authenticated calls using HTTP or HTTPS. A single queue message can be up to 64 KiB in size, and a queue can contain millions of messages, up to the total capacity limit of a storage account. ...

Example:
```python
from azure.storage.queue import QueueServiceClient

service = QueueServiceClient(account_url=" credential=credential)
```

...

</details>

### azure-keyvault-keys

Microsoft Corporation Azure Key Vault Keys Client Library for Python

`pip install azure-keyvault-keys` · installs (wheel) · licence: MIT · rank 831 · last release 2026-10-02 · [PyPI](https://pypi.org/project/azure-keyvault-keys/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure Key Vault helps solve the following problems:
- Cryptographic key management (this library) - create, store, and control
access to the keys used to encrypt your data
- Secrets management
(azure-keyvault-secrets) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets ...

Features:
- Added support for service API version `2025-07-01` #46716

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient

VAULT_URL = os.environ["VAULT_URL"]
credential = DefaultAzureCredential()
client = KeyClient(vault_url=VAULT_URL, credential=credential)
```

...

</details>

### azure-storage-file-datalake

Microsoft Azure File DataLake Storage Client Library for Python

`pip install azure-storage-file-datalake` · installs (wheel) · licence: MIT License · rank 847 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-storage-file-datalake/)

<details><summary>README extract</summary>

Overview

This preview package for Python includes ADLS Gen2 specific API support made available in Storage SDK. This includes:
1. New directory level operations (Create, Rename, Delete) for hierarchical namespace enabled (HNS) storage account. For HNS enabled accounts, the rename/move operations are atomic.
2. ...

Example:
```python
from azure.storage.filedatalake import DataLakeServiceClient

service = DataLakeServiceClient(account_url=" credential=credential)
```

Sections: Azure DataLake service client library for Python, Getting started, Prerequisites, Create a storage account, Authenticate the client, Get credentials, Create client, Key concepts, Async Clients, Clients, Examples, Client creation with a connection string, Uploading a file, Downloading a file

</details>

### aws-requests-auth

AWS signature version 4 signing process for the python requests module

`pip install aws-requests-auth` · installs (wheel) · licence: BSD License · rank 884 · last release 2020-05-27 · [PyPI](https://pypi.org/project/aws-requests-auth/)

### azure-servicebus

Microsoft Azure Service Bus Client Library for Python

`pip install azure-servicebus` · installs (wheel) · licence: MIT · rank 934 · last release 2026-10-08 · [PyPI](https://pypi.org/project/azure-servicebus/) · [source](https://github.com/Azure/azure-sdk-for-python.git)

<details><summary>README extract</summary>

Azure Service Bus is a high performance cloud-managed messaging service for providing real-time and fault-tolerant communication between distributed senders and receivers.

Service Bus provides multiple mechanisms for asynchronous highly reliable communication, such as structured first-in-first-out messaging,
publish/subscribe capabilities, and ...

Features:
- Added an opt-in `try_timeout` client keyword that bounds a single attempt rather than the whole operation. Applies to sending, management operations (including management-link message settlement), and AMQP link acquisition, where the wait for the ...

Example:
```python
import threading
from concurrent.futures import ThreadPoolExecutor
from azure.servicebus import ServiceBusClient, ServiceBusMessage
...

</details>

### aiodns

Simple DNS resolver for asyncio

`pip install aiodns` · installs (wheel) · licence: MIT · rank 952 · last release 2026-05-20 · [PyPI](https://pypi.org/project/aiodns/) · [source](https://github.com/aio-libs/aiodns.git)

<details><summary>README extract</summary>

aiodns provides a simple way for doing asynchronous DNS resolutions using pycares.

Example:
```python
import asyncio
import aiodns

async def main():
    resolver = aiodns.DNSResolver()
    result = await resolver.query_dns('google.com', 'A')
    for record in result.answer:
        print(record.data.addr)

asyncio.run(main())
```

Sections: Simple DNS resolver for asyncio, Example, API, Migrating from aiodns 3.x, Future migration to aiodns 5.x, Note for Windows users, Running the test suite

</details>

### aws-xray-sdk

The AWS X-Ray SDK for Python (the SDK) enables Python developers to record and emit information from within their applications to the AWS X-Ray service.

`pip install aws-xray-sdk` · installs (wheel) · licence: Apache Software License · rank 958 · last release 2026-10-30 · [PyPI](https://pypi.org/project/aws-xray-sdk/)

<details><summary>README extract</summary>

The AWS X-Ray SDKs will enter maintenance mode on `February 25, 2026`. During maintenance mode, the X-Ray SDKs and Daemon will only receive critical bug fixes and security updates, and will not be updated to support new features. ...

Example:
```python
from aws_xray_sdk.core import xray_recorder

xray_recorder.configure(
    sampling=False,
    context_missing='LOG_ERROR',
    plugins=('EC2Plugin', 'ECSPlugin', 'ElasticBeanstalkPlugin'),
    daemon_address='127.0.0.1:3000',
    dynamic_naming='*mysite.com*'
)
```

...

</details>

### aws-lambda-powertools

Powertools for AWS Lambda (Python) is a developer toolkit to implement Serverless best practices and increase developer velocity.

`pip install aws-lambda-powertools` · installs (wheel) · licence: MIT License; MIT No Attribution License (MIT-0) · rank 977 · last release 2026-11-03 · [PyPI](https://pypi.org/project/aws-lambda-powertools/) · [docs](https://docs.powertools.aws.dev/lambda/python/) · [source](https://github.com/aws-powertools/powertools-lambda-python)

<details><summary>README extract</summary>

<!-- markdownlint-disable MD013 MD041 MD043 -->

Powertools for AWS Lambda (Python) is a developer toolkit for AWS Lambda: structured logging, tracing, metrics, event handlers for API Gateway, AppSync and Bedrock Agents, idempotency, batch processing, parameters, validation, and more. ...

Sections: Powertools for AWS Lambda (Python), Features, Core, Utilities, Lambda features, Tutorial and examples, Becoming a reference customer, Sharing your work, Using the Lambda layer, Connect

</details>

### Automat

Self-service finite-state machines for the programmer on the go.

`pip install Automat` · installs (wheel) · licence: MIT License · rank 1014 · last release 2025-04-16 · [PyPI](https://pypi.org/project/Automat/) · [docs](https://automat.readthedocs.io/) · [source](https://github.com/glyph/automat/)

<details><summary>README extract</summary>

Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

Read more here, or on Read the Docs, or watch the following videos for an overview and presentation

Features:
Sometimes you have to create an object whose behavior varies with its state,
but still wishes to present a consistent interface to its callers.

For example, let's say you're writing the software for a coffee machine. ...

Example:
```python
class CoffeeMachine(object):
    def brewButton(self) -> None:
        if self.hasWater and self.hasBeans and not self.isLidOpen:
            self.heatTheHeatingElement()
            # ...
```

Sections: Automat, Why use state machines?, What makes Automat different?

</details>

### azure-core-tracing-opentelemetry

Microsoft Azure Core OpenTelemetry plugin Library for Python

`pip install azure-core-tracing-opentelemetry` · installs (wheel) · licence: not stated · rank 1056 · last release 2026-05-01 · [PyPI](https://pypi.org/project/azure-core-tracing-opentelemetry/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry)

<details><summary>README extract</summary>

Features:
- If a span exits with an exception, the exception name is now recorded in the `error.type` attribute. (#34619)
- Added support for passing a schema version to fetch available attribute mappings and set the schema URL on the tracer's instrumentation ...

Example:
```python
# Enable Azure Monitor OpenTelemetry Distro
# It confiures Azure SDKs to use OpenTelemetry as well
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace

configure_azure_monitor(
   connection_string="<your-connection-string>"
)

# Use Azure SDKs as usual, here as an example with Storage SDKs
...
```

...

</details>

### azure-monitor-opentelemetry

Microsoft Azure Monitor Opentelemetry Distro Client Library for Python

`pip install azure-monitor-opentelemetry` · installs (wheel) · licence: MIT License · rank 1067 · last release 2026-11-06 · [PyPI](https://pypi.org/project/azure-monitor-opentelemetry/)

<details><summary>README extract</summary>

The Azure Monitor Distro of Opentelemetry Python is a "one-stop-shop" telemetry solution, requiring only one line of code to instrument your application. The distro captures telemetry via OpenTelemetry instrumentations and reports telemetry to Azure Monitor via the Azure Monitor exporters. ...

Example:
```python
...
configure_azure_monitor(
   connection_string="<your-connection-string>",
   disable_offline_storage=True,
)
...
```

Sections: Key concepts, Getting started, Prerequisites, Usage, Azure monitor OpenTelemetry Exporter configurations, Examples, Monitoring in Azure Functions, Trace correlation, Logging issues, Troubleshooting, Next steps, Additional documentation

</details>

### aiolimiter

asyncio rate limiter, a leaky bucket implementation

`pip install aiolimiter` · installs (wheel) · licence: MIT · rank 1076 · last release 2026-09-07 · [PyPI](https://pypi.org/project/aiolimiter/) · [docs](http://aiolimiter.readthedocs.org/en/stable/) · [source](https://github.com/mjpieters/aiolimiter)

<details><summary>README extract</summary>

[][checks_status]
[][codecov_status]
[][aiolimiter_release]
[][aiolimiter_docs]

An efficient implementation of a rate limiter for asyncio.

This project implements the Leaky bucket algorithm, giving you precise control over the rate a code section can be entered:

It was first developed as an answer on Stack Overflow.

Example:
```python
from aiolimiter import AsyncLimiter

# allow for 100 concurrent entries within a 30 second window
rate_limit = AsyncLimiter(100, 30)

async def some_coroutine():
    async with rate_limit:
        # this section is *at most* going to entered 100 times
        # in a 30 second period.
        await do_something()
```

Sections: aiolimiter, Introduction, Documentation, Requirements, Source code

</details>

### azure-cosmos

Microsoft Azure Cosmos Client Library for Python

`pip install azure-cosmos` · installs (wheel) · licence: MIT License · rank 1083 · last release 2026-09-16 · [PyPI](https://pypi.org/project/azure-cosmos/)

<details><summary>README extract</summary>

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Azure Cosmos DB is a globally distributed, multi-model database service that supports document, key-value, wide-column, and graph databases. ...

Features:
* Added the `enable_compact_utf8_item_writes` client option. Set it to `True` to reduce item write request sizes by
 serializing valid Unicode as compact UTF-8 for create, upsert, replace, patch, and transactional batch operations.
 See PR 48914.

Example:
```python
from azure.cosmos import CosmosClient

import os
URL = os.environ['ACCOUNT_URI']
KEY = os.environ['ACCOUNT_KEY']
client = CosmosClient(URL, credential=KEY)
```

...

</details>

### avro

Avro is a serialization and RPC framework.

`pip install avro` · installs (wheel) · licence: Apache Software License · rank 1085 · last release 2026-08-17 · [PyPI](https://pypi.org/project/avro/) · [docs](https://avro.apache.org/docs/1.12.0/api/py/html/) · [source](https://github.com/apache/avro.git)

<details><summary>README extract</summary>

Apache Avro™ is a data serialization system. To learn more, please visit our website.

Apache Avro documentation is maintained on our wiki.

Sections: Apache Avro™, Documentation

</details>

### azure-batch

Microsoft Corporation Azure Batch Client Library for Python

`pip install azure-batch` · installs (wheel) · licence: not stated · rank 1124 · last release 2026-05-01 · [PyPI](https://pypi.org/project/azure-batch/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Batch allows users to run large-scale parallel and high-performance computing (HPC) batch jobs efficiently in Azure. To learn more about Azure Batch, please see the Azure Batch Overview documentation.

Source code
| Batch package (PyPI)
| API reference documentation
| Product documentation ...

Features:
- Job level FIFO
 - Added `BatchJobDefaultOrder` types.
 - Extended `BatchTaskSchedulingPolicy` with a new `jobDefaultOrder` property to support job-level FIFO scheduling. ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.batch import BatchClient

credentials = DefaultAzureCredential()
client = BatchClient(
    endpoint=' account>.eastus.batch.azure.com',
    credential=credentials
)
```

...

</details>

### aliyun-trace

Aliyun Trace

`pip install aliyun-trace` · installs (wheel) · licence: Apache-2.0 · rank 1137 · last release 2025-06-20 · [PyPI](https://pypi.org/project/aliyun-trace/)

<details><summary>README extract</summary>

This library contains code for the Aliyun Trace that manually creates a trace for the LLM.

</details>

### aliyun-semantic-conventions

Aliyun Semantic Conventions

`pip install aliyun-semantic-conventions` · installs (wheel) · licence: Apache-2.0 · rank 1138 · last release 2025-03-13 · [PyPI](https://pypi.org/project/aliyun-semantic-conventions/)

<details><summary>README extract</summary>

This library contains code for the Aliyun Semantic Conventions defined by the Aliyun specification.

</details>

### aws-cdk.asset-awscli-v1

A library that contains the AWS CLI for use in Lambda Layers

`pip install aws-cdk.asset-awscli-v1` · installs (wheel) · licence: OSI Approved · rank 1140 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.asset-awscli-v1/) · [source](https://github.com/cdklabs/awscdk-asset-awscli.git)

### asgi-lifespan

Programmatic startup/shutdown of ASGI apps.

`pip install asgi-lifespan` · installs (wheel) · licence: MIT · rank 1142 · last release 2023-03-28 · [PyPI](https://pypi.org/project/asgi-lifespan/)

<details><summary>README extract</summary>

Programmatically send startup/shutdown lifespan events into ASGI applications. When used in combination with an ASGI-capable HTTP client such as HTTPX, this allows mocking or testing ASGI applications without having to spin up an ASGI server.

Features:
- Send lifespan events to an ASGI app using `LifespanManager`.
- Support for `asyncio` and `trio`.
- Fully type-annotated.
- 100% test coverage.

Example:
```python
# example.py
from contextlib import asynccontextmanager
from asgi_lifespan import LifespanManager
from starlette.applications import Starlette

# Example lifespan-capable ASGI app. Any ASGI app that supports
# the lifespan protocol will do, e.g. FastAPI, Quart, Responder, ...

@asynccontextmanager
async def lifespan(app):
    print("Starting up!")
...
```

...

</details>

### azure-mgmt-resource

Microsoft Azure Resource Management Client Library for Python

`pip install azure-mgmt-resource` · installs (wheel) · licence: MIT · rank 1158 · last release 2026-06-24 · [PyPI](https://pypi.org/project/azure-mgmt-resource/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ResourceManagementClient` added method `send_request`
 - Model `GenericResource` added property `system_data`
 - Model `GenericResourceExpanded` added property `system_data`
 - Model `Operation` added property `is_data_action`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### audioop-lts

LTS Port of Python audioop

`pip install audioop-lts` · installs (wheel) · licence: PSF-2.0 · rank 1201 · last release 2025-08-05 · [PyPI](https://pypi.org/project/audioop-lts/) · [source](https://github.com/AbstractUmbra/audioop)

<details><summary>README extract</summary>

An LTS port of the Python builtin module `audioop` which was deprecated since version 3.11 and removed in 3.13.

This project exists to maintain this module for future versions.

> [!WARNING]
This module only functions at Python versions of 3.13 or greater due to being removed in this version. ...

Sections: audioop, Using this project, pip-requirements, Poetry-pyproject, pdm-pyproject / uv-pyproject / hatch-pyproject, Pipenv-pipfile

</details>

### azure-ai-documentintelligence

Microsoft Azure AI Document Intelligence Client Library for Python

`pip install azure-ai-documentintelligence` · installs (wheel) · licence: MIT License · rank 1269 · last release 2025-03-27 · [PyPI](https://pypi.org/project/azure-ai-documentintelligence/)

<details><summary>README extract</summary>

Azure AI Document Intelligence (previously known as Form Recognizer) is a cloud service that uses machine learning to analyze text and structured data from your documents. It includes the following main features:

- Layout - Extract content and structure (ex. words, selection marks, tables) from documents. ...

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

endpoint = "
credential = AzureKeyCredential("<api_key>")
document_intelligence_client = DocumentIntelligenceClient(endpoint, credential)
```

...

</details>

### azure-storage-file-share

Microsoft Corporation Azure Storage File Share Client Library for Python

`pip install azure-storage-file-share` · installs (wheel) · licence: MIT · rank 1288 · last release 2026-10-29 · [PyPI](https://pypi.org/project/azure-storage-file-share/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure File Share storage offers fully managed file shares in the cloud that are accessible via the industry standard Server Message Block (SMB) protocol. Azure file shares can be mounted concurrently by cloud or on-premises deployments of Windows, Linux, and macOS. ...

Example:
```python
from azure.storage.fileshare import ShareServiceClient

service = ShareServiceClient(account_url=" credential=credential)
```

Sections: Azure Storage File Share client library for Python, Getting started, Prerequisites, Create a storage account, Create the client, Looking up the account URL, Types of credentials, Create a logger for the 'azure.storage.fileshare' SDK, Configure a console output

</details>

### azure-data-tables

Microsoft Azure Azure Data Tables Client Library for Python

`pip install azure-data-tables` · installs (wheel) · licence: MIT License · rank 1300 · last release 2025-05-06 · [PyPI](https://pypi.org/project/azure-data-tables/)

<details><summary>README extract</summary>

Azure Tables is a NoSQL data storage service that can be accessed from anywhere in the world via authenticated calls using HTTP or HTTPS.
Tables scales as needed to support the amount of data inserted, and allow for the storing of data with non-complex accessing.
The Azure Tables client can be used to access Azure Storage or Cosmos accounts. ...

Features:
* Added support for configuring custom audiences for `TokenCredential` authentication when initializing a `TableClient` or `TableServiceClient`. (#40487)

Example:
```python
from azure.data.tables import TableServiceClient
service = TableServiceClient(endpoint=" credential=credential)
```

...

</details>

### adlfs

Access Azure Blobs and Data Lake Storage (ADLS) Gen2 with fsspec and dask

`pip install adlfs` · installs (wheel) · licence: BSD License · rank 1302 · last release 2026-08-11 · [PyPI](https://pypi.org/project/adlfs/) · [docs](https://fsspec.github.io/adlfs/) · [source](https://github.com/fsspec/adlfs)

<details><summary>README extract</summary>

Filesystem interface to Azure Blob and Data Lake Storage (Gen2)

Quickstart

This package can be installed using:

`pip install adlfs`


`conda install -c conda-forge adlfs`

The `az://` and `abfs://` protocols are included in fsspec's known_implementations registry. ...

Example:
```python
import dask.dataframe as dd

storage_options={'account_name': ACCOUNT_NAME, 'account_key': ACCOUNT_KEY}

ddf = dd.read_csv('abfs://{CONTAINER}/{FOLDER}/*.csv', storage_options=storage_options)
ddf = dd.read_parquet('az://{CONTAINER}/folder.parquet', storage_options=storage_options)

Accepted protocol / uri formats include:
...
```

Sections: Setting credentials, Append Blob, Older versions

</details>

### azure-keyvault-certificates

Microsoft Corporation Key Vault Certificates Client Library for Python

`pip install azure-keyvault-certificates` · installs (wheel) · licence: MIT License · rank 1305 · last release 2026-10-28 · [PyPI](https://pypi.org/project/azure-keyvault-certificates/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk)

<details><summary>README extract</summary>

Azure Key Vault helps solve the following problems:
- Certificate management (this library) - create, manage, and deploy public and private SSL/TLS certificates
- Cryptographic key management
(azure-keyvault-keys) - create, store, and control access to the keys used to encrypt your data ...

Features:
- Added an experimental `PlatformManaged` property on `CertificatePolicy` for Azure Key Vault internal usage. Any calls using this property will fail and it is not recommended to be used at this point. ...

Example:
```python
VAULT_URL = os.environ["VAULT_URL"]
credential = DefaultAzureCredential()
client = CertificateClient(vault_url=VAULT_URL, credential=credential)
```

...

</details>

### ag-ui-protocol

(no summary)

`pip install ag-ui-protocol` · installs (wheel) · licence: MIT · rank 1318 · last release 2026-09-17 · [PyPI](https://pypi.org/project/ag-ui-protocol/)

<details><summary>README extract</summary>

Features:
- 🐍 Python-native – Idiomatic Python APIs with full type hints and validation
- 📋 Pydantic models – Runtime validation and automatic JSON serialization
- 🔄 Streaming events – 16 core event types for real-time agent communication ...

Example:
```python
from ag_ui.core import TextMessageContentEvent, EventType
from ag_ui.encoder import EventEncoder

# Create a streaming text event
event = TextMessageContentEvent(
    type=EventType.TEXT_MESSAGE_CONTENT,
    message_id="msg_123",
    delta="Hello from Python!"
)

# Encode for HTTP streaming
encoder = EventEncoder()
sse_data = encoder.encode(event)
...
```

Sections: Features, Quick example, Multimodal user message, Optional fields with no value are left out, Packages, Documentation

</details>

### azure-mgmt-compute

Microsoft Azure Compute Management Client Library for Python

`pip install azure-mgmt-compute` · installs (wheel) · licence: MIT · rank 1336 · last release 2026-10-23 · [PyPI](https://pypi.org/project/azure-mgmt-compute/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Compute Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `VirtualMachineNetworkInterfaceIPConfigurationProperties` added property `private_ip_address_prefix_length`
 - Model `VirtualMachineProperties` added property `flex_profile`
 - Model `VirtualMachineScaleSetIPConfigurationProperties` added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-storage

Microsoft Azure Storage Management Client Library for Python

`pip install azure-mgmt-storage` · installs (wheel) · licence: MIT · rank 1338 · last release 2026-10-16 · [PyPI](https://pypi.org/project/azure-mgmt-storage/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Storage Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `StorageManagementClient` added operation group `blob_access_point_configurations`
 - Client `StorageManagementClient` added operation group `blob_access_point_connection_tests`
 - Model `ContainerProperties` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### amplitude-analytics

The official Amplitude backend Python SDK for server-side instrumentation.

`pip install amplitude-analytics` · installs (wheel) · licence: MIT License · rank 1340 · last release 2026-10-15 · [PyPI](https://pypi.org/project/amplitude-analytics/) · [source](https://github.com/amplitude/Amplitude-Python)

<details><summary>README extract</summary>

The official Amplitude backend Python SDK for server-side instrumentation.

Sections: Amplitude Python SDK, Run Server Locally, Run Unit Tests Locally, Run Directly, Run with `tox`, Amplitude and Ampli Wrapper, Need Help?

</details>

### azure-eventhub

Microsoft Azure Event Hubs Client Library for Python

`pip install azure-eventhub` · installs (wheel) · licence: not stated · rank 1351 · last release 2025-10-30 · [PyPI](https://pypi.org/project/azure-eventhub/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk)

<details><summary>README extract</summary>

Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions of events per second and stream
them to multiple consumers. This lets you process and analyze the massive amounts of data produced by your connected
devices and applications. ...

Example:
```python
import threading
from concurrent.futures import ThreadPoolExecutor
from azure.eventhub import EventHubProducerClient, EventData
from azure.identity import DefaultAzureCredential

EVENTHUB_NAMESPACE = "<your-namespace>.servicebus.windows.net"
EVENTHUB_NAME = "<your-eventhub-name>"

# Create a global lock
producer_lock = threading.Lock()

...
```

...

</details>

### ansible

Radically simple IT automation

`pip install ansible` · installs (wheel) · licence: GPL-3.0-or-later · rank 1368 · last release 2026-11-04 · [PyPI](https://pypi.org/project/ansible/) · [docs](https://docs.ansible.com/projects/ansible)

_README extract left out: share-alike licence._

### azure-datalake-store

Azure Data Lake Store Filesystem Client Library for Python

`pip install azure-datalake-store` · installs (wheel) · licence: MIT License · rank 1369 · last release 2025-06-11 · [PyPI](https://pypi.org/project/azure-datalake-store/)

<details><summary>README extract</summary>

This project is the Python filesystem library for Azure Data Lake Store.

Example:
```python
from azure.datalake.store import core, lib, multithread
token = lib.auth(tenant_id, username, password)
adl = core.AzureDLFileSystem(token, store_name=store_name)

# typical operations
adl.ls('')
adl.ls('tmp/', detail=True)
adl.ls('tmp/', detail=True, invalidate_cache=True)
adl.cat('littlefile')
adl.head('gdelt20150827.csv')

# file-like object
...
```

Sections: Usage: Sample Code, Usage: Command Line Sample, Tests, Need Help?, 1.0.1 (2025-05-16), 1.0.0-alpha0 (2024-07-12), 0.0.53 (2023-04-11), 0.0.52 (2020-11-25), 0.0.51 (2020-10-15), 0.0.50 (2020-09-10), 0.0.49 (2020-08-05), 0.0.48 (2019-10-18), 0.0.47 (2019-08-14), 0.0.46 (2019-06-25)

</details>

### azure-monitor-query

Microsoft Corporation Azure Monitor Query Client Library for Python

`pip install azure-monitor-query` · installs (wheel) · licence: MIT License · rank 1398 · last release 2025-07-30 · [PyPI](https://pypi.org/project/azure-monitor-query/)

<details><summary>README extract</summary>

The Azure Monitor Query client library is used to execute read-only queries against Azure Monitor's Logs data platform.

- Logs - Collects and organizes log and performance data from monitored resources. ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

credential = DefaultAzureCredential()
logs_query_client = LogsQueryClient(credential)
```

Sections: Azure Monitor Query client library for Python, Getting started, Prerequisites, Create the client, Synchronous clients, Asynchronous clients, Configure client for Azure sovereign cloud, Execute the query, Key concepts, Logs query rate limits and throttling, Examples, Logs query, Resource-centric logs query, Specify timespan

</details>

### azure-kusto-data

Kusto Data Client

`pip install azure-kusto-data` · installs (wheel) · licence: MIT · rank 1442 · last release 2026-05-06 · [PyPI](https://pypi.org/project/azure-kusto-data/) · [source](https://github.com/Azure/azure-kusto-python)

<details><summary>README extract</summary>

Features:
*Kusto Python Client* Library provides the capability to query Kusto clusters using Python.
It is Python 3.x compatible and supports
all data types through familiar Python DB API interface. ...

Example:
```python
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

cluster = "<insert here your cluster name>"
client_id = "<insert here your AAD application id>"
client_secret = "<insert here your AAD application key>"
authority_id = "<insert here your AAD tenant id>"

...
```

Sections: Microsoft Azure Kusto Library for Python, Overview, Async Client, Links

</details>

### aws-cdk-lib

Version 2 of the AWS Cloud Development Kit library

`pip install aws-cdk-lib` · installs (wheel) · licence: OSI Approved · rank 1446 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk-lib/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

Example:
```python
from aws_cdk import Environment
# topic: sns.Topic

consumer = Stack(app, "Consumer",
    env=Environment(account="123456789012", region="us-east-1")
)
sns.Subscription(consumer, "Subscription",
    topic=sns.Topic.from_topic_arn(consumer, "Topic",
        Stack.consume_reference(topic.topic_arn, ReferenceStrength.WEAK)),
    endpoint="
...
```

Sections: Usage, Upgrade from CDK 1.x, Use in your code, Classic import, Barrel import, Stacks and Stages, Stack Synthesizers, STS Role Options, Session Tags, Nested Stacks, Accessing resources in a different stack, Reference strength, The deadly embrace, Controlling reference strength

</details>

### arro3-core

(no summary)

`pip install arro3-core` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 1475 · last release 2026-10-12 · [PyPI](https://pypi.org/project/arro3-core/)

### aiocache

multi backend asyncio cache

`pip install aiocache` · installs (wheel) · licence: not stated · rank 1491 · last release 2024-09-25 · [PyPI](https://pypi.org/project/aiocache/)

<details><summary>README extract</summary>

Asyncio cache supporting multiple backends (memory, redis and memcached).

This library aims for simplicity over specialization. All caches contain the same minimum interface which consists on the following functions:

- `add`: Only adds key/value if key does not exist.
- `get`: Retrieve value identified by key.
- `set`: Sets key/value. ...

Example:
```python
>>> import asyncio
>>> from aiocache import Cache
>>> cache = Cache(Cache.MEMORY) # Here you can also use Cache.REDIS and Cache.MEMCACHED, default is Cache.MEMORY
>>> with asyncio.Runner() as runner:
>>>     runner.run(cache.set('key', 'value'))
True
>>>     runner.run(cache.get('key'))
'value'
```

Sections: aiocache, Usage, How does it work, Amazing examples, Documentation

</details>

### aws-cdk.asset-node-proxy-agent-v6

@aws-cdk/asset-node-proxy-agent-v6

`pip install aws-cdk.asset-node-proxy-agent-v6` · installs (wheel) · licence: OSI Approved · rank 1499 · last release 2026-09-08 · [PyPI](https://pypi.org/project/aws-cdk.asset-node-proxy-agent-v6/) · [source](https://github.com/cdklabs/awscdk-asset-node-proxy-agent.git)

### aws-cdk.cloud-assembly-schema

Schema for the protocol between CDK framework and CDK CLI

`pip install aws-cdk.cloud-assembly-schema` · installs (wheel) · licence: OSI Approved · rank 1507 · last release 2026-11-05 · [PyPI](https://pypi.org/project/aws-cdk.cloud-assembly-schema/) · [source](https://github.com/aws/aws-cdk-cli)

<details><summary>README extract</summary>

This module is part of the AWS Cloud Development Kit project.

The *Cloud Assembly* is the output of the synthesis operation. It is produced as part of the
`cdk synth`
command, or the `app.synth()` method invocation.

Its essentially a set of files and directories, one of which is the `manifest.json` file. ...

Sections: Cloud Assembly Schema, Cloud Assembly, Schema, Versioning, How to consume

</details>

### azure-ai-projects

Microsoft Corporation Azure AI Projects Client Library for Python

`pip install azure-ai-projects` · installs (wheel) · licence: MIT · rank 1508 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-ai-projects/) · [source](https://aka.ms/azsdk/azure-ai-projects-v2/python/code)

<details><summary>README extract</summary>

The AI Projects client library is part of the Microsoft Foundry SDK, and provides easy access to
resources in your Microsoft Foundry Project. Use it to:

* Create and run Agents using methods on the `.agents` client property. ...

Features:
* Added optional `VoiceAgentDefinition.soundscape` for built-in background ambience and event cues in telephony calls, with `VoiceAgentSoundscapeConfig`, `VoiceAgentSoundscapeSourceConfig`, `VoiceAgentSoundscapeTrackConfig`, ...

Example:
```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        credential=credential
    ) as project_client,
):
```

...

</details>

### asteval

Safe, minimalistic evaluator of python expression using ast module

`pip install asteval` · installs (wheel) · licence: MIT · rank 1513 · last release 2026-08-21 · [PyPI](https://pypi.org/project/asteval/) · [docs](https://lmfit.github.io/asteval/)

### apache-tvm-ffi

tvm ffi

`pip install apache-tvm-ffi` · installs (wheel) · licence: Apache Software License · rank 1552 · last release 2026-10-29 · [PyPI](https://pypi.org/project/apache-tvm-ffi/) · [source](https://github.com/apache/tvm-ffi)

<details><summary>README extract</summary>

<!--- Licensed to the Apache Software Foundation (ASF) under one -->
<!--- or more contributor license agreements. See the NOTICE file -->
<!--- distributed with this work for additional information -->
<!--- regarding copyright ownership. ...

Features:
- Stable, minimal C ABI designed for kernels, DSLs, and runtime extensibility.
- Zero-copy interop across PyTorch, JAX, and CuPy using DLPack protocol. ...

Sections: TVM FFI: Open ABI and FFI for Machine Learning Systems, Features, Getting Started, Documentation, Get Started, Guides, Concepts, Packaging

</details>

### azure-keyvault

Microsoft Azure Key Vault Client Libraries for Python

`pip install azure-keyvault` · installs (wheel) · licence: MIT License · rank 1557 · last release 2022-03-29 · [PyPI](https://pypi.org/project/azure-keyvault/)

<details><summary>README extract</summary>

This is the Microsoft Azure Key Vault libraries bundle.

This package does not contain any code in itself. It installs a set
of packages that provide APIs for Key Vault operations:

- azure-keyvault-keys v4.x
- azure-keyvault-secrets v4.x
- azure-keyvault-certificates v4.x ...

Sections: Azure Key Vault client libraries for Python, _Disclaimer_, Documentation, 4.2.0 (2022-03-29), Other Changes, 4.1.0 (2020-04-10), 4.0.0 (2019-10-31), 1.1.0 (2018-08-07), 1.0.0 (2018-06-27), 1.0.0b1 (2018-04-10), 1.0.0a2 (2018-03-28), 1.0.0a1 (2018-01-25), 0.3.7 (2017-09-22), 0.3.6 (2017-08-16)

</details>

### avro-python3

Avro is a serialization and RPC framework.

`pip install avro-python3` · installs from source (sdist only) · licence: Apache Software License · rank 1589 · last release 2021-03-17 · [PyPI](https://pypi.org/project/avro-python3/)

<details><summary>README extract</summary>

avro-python3 is no longer maintained and is deprecated in favor of avro. Avro is maintained and has full support for recent versions of Python.

Apache Avro™ is a data serialization system. To learn more, please visit our website.

Apache Avro documentation is maintained on our wiki.

Sections: Deprecation Notice, Apache Avro™, Documentation

</details>

### aws-msk-iam-sasl-signer-python

Amazon MSK Library in Python for SASL/OAUTHBEARER Auth

`pip install aws-msk-iam-sasl-signer-python` · installs (wheel) · licence: Apache Software License · rank 1628 · last release 2025-03-05 · [PyPI](https://pypi.org/project/aws-msk-iam-sasl-signer-python/)

<details><summary>README extract</summary>

This is an Amazon MSK Library in Python. This library provides a function to generates a base 64 encoded signed url
to enable authentication/authorization with an MSK Cluster.
The signed url is generated by using your IAM credentials.

* Free software: Apache Software License 2.0

Features:
* Provides a function to generate auth token using IAM credentials from the AWS default credentials chain.
* Provides a function to generate auth token using IAM credentials from the AWS named profile. ...

Example:
```python
from kafka import KafkaProducer
from kafka.errors import KafkaError
import socket
import time
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

class MSKTokenProvider():
    def token(self):
        token, _ = MSKAuthTokenProvider.generate_auth_token('<my aws region>')
...

</details>

### azure-storage-common

Microsoft Azure Storage Common Client Library for Python

`pip install azure-storage-common` · installs (wheel) · licence: MIT License · rank 1638 · last release 2019-08-02 · [PyPI](https://pypi.org/project/azure-storage-common/)

<details><summary>README extract</summary>

This project provides a client library in Python that makes it easy to
consume Microsoft Azure Storage services. For documentation please see
the Microsoft Azure Python Developer Center and our API Reference (also available on readthedocs).

 If you are looking for the Service Bus or Azure Management
 libraries, please visit ...

Features:
- Blob

 - Create/Read/Update/Delete Containers
 - Create/Read/Update/Delete Blobs
 - Advanced Blob Operations

- Queue

 - Create/Delete Queues
 - Insert/Peek Queue Messages
 - Advanced Queue Operations

- Files ...

Example:
```python
# Basic configuration: configure the root logger, including 'azure.storage'
logging.basicConfig(format='%(asctime)s %(name)-20s %(levelname)-5s %(message)s', level=logging.INFO)
```

...

</details>

### azure-mgmt-authorization

Microsoft Azure Authorization Management Client Library for Python

`pip install azure-mgmt-authorization` · installs (wheel) · licence: MIT License · rank 1647 · last release 2023-07-25 · [PyPI](https://pypi.org/project/azure-mgmt-authorization/)

<details><summary>README extract</summary>

This is the Microsoft Azure Authorization Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation RoleAssignmentScheduleRequestsOperations.validate
 - Added operation RoleEligibilityScheduleRequestsOperations.validate
 - Model AlertConfiguration has a new parameter alert_definition
 - Model AlertConfigurationProperties has a ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-datafactory

Microsoft Azure Datafactory Management Client Library for Python

`pip install azure-mgmt-datafactory` · installs (wheel) · licence: MIT · rank 1648 · last release 2026-07-08 · [PyPI](https://pypi.org/project/azure-mgmt-datafactory/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Factory Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `DataFactoryManagementClient` added method `send_request`
 - Model `ChangeDataCaptureResource` added property `system_data`
 - Model `CredentialResource` added property `system_data`
 - Model `DataFlowResource` added property `system_data` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-cosmosdb

Microsoft Azure Cosmosdb Management Client Library for Python

`pip install azure-mgmt-cosmosdb` · installs (wheel) · licence: MIT · rank 1653 · last release 2026-07-03 · [PyPI](https://pypi.org/project/azure-mgmt-cosmosdb/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Cosmos DB Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `CosmosDBManagementClient` added method `send_request`
 - Client `CosmosDBManagementClient` added operation group `mongo_mi_resources`
 - Model `ARMResourceProperties` added property `identity`
 - Model `CassandraClusterDataCenterNodeItem` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdb import CosmosDBManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-containerregistry

Microsoft Azure Containerregistry Management Client Library for Python

`pip install azure-mgmt-containerregistry` · installs (wheel) · licence: not stated · rank 1679 · last release 2026-03-19 · [PyPI](https://pypi.org/project/azure-mgmt-containerregistry/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Container Registry Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `ContainerRegistryManagementClient` added parameter `cloud_setting` in method `init`
 - Client `ContainerRegistryManagementClient` added method `send_request`
 - Model `ConnectedRegistry` added property `properties`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### apispec

A pluggable API specification generator. Currently supports the OpenAPI Specification (f.k.a. the Swagger specification).

`pip install apispec` · installs (wheel) · licence: MIT · rank 1700 · last release 2026-11-04 · [PyPI](https://pypi.org/project/apispec/) · [source](https://github.com/marshmallow-code/apispec)

<details><summary>README extract</summary>

A pluggable API specification generator. Currently supports the OpenAPI Specification (f.k.a. the Swagger specification).

Features:
- Supports the OpenAPI Specification (versions 2 and 3)
- Framework-agnostic
- Built-in support for marshmallow
- Utilities for parsing docstrings

Example:
```python
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
...
```

Sections: apispec, Features, Example Application, Generated OpenAPI Spec, Documentation, Ecosystem, Project Links

</details>

### a2wsgi

Convert WSGI app to ASGI app or ASGI app to WSGI app.

`pip install a2wsgi` · installs (wheel) · licence: Apache-2.0 · rank 1716 · last release 2025-06-18 · [PyPI](https://pypi.org/project/a2wsgi/) · [source](https://github.com/abersheeran/a2wsgi)

<details><summary>README extract</summary>

Convert WSGI app to ASGI app or ASGI app to WSGI app.

Pure Python. Only depend on the standard library.

Compared with other converters, the advantage is that a2wsgi will not accumulate the requested content or response content in the memory, so you don't have to worry about the memory limit caused by a2wsgi. ...

Example:
```python
from a2wsgi import WSGIMiddleware

ASGI_APP = WSGIMiddleware(WSGI_APP)
```

Sections: a2wsgi, How to use, `WSGIMiddleware`, `ASGIMiddleware`, Access the original `Scope`/`Environ`, Benchmark, Why a2wsgi, Convert WSGI app to ASGI app, Convert ASGI app to WSGI app, Compatibility list

</details>

### azure-appconfiguration

Microsoft Corporation Azure App Configuration Data Client Library for Python

`pip install azure-appconfiguration` · installs (wheel) · licence: MIT · rank 1723 · last release 2026-10-09 · [PyPI](https://pypi.org/project/azure-appconfiguration/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure App Configuration is a managed service that helps developers centralize their application configurations simply and securely.

Modern programs, especially programs running in a cloud, generally have many components that are distributed in nature. ...

Features:
- Added `check_configuration_settings()` method to efficiently check for configuration changes using HEAD requests, returning only headers (ETags) without response bodies. ...

Example:
```python
ENDPOINT = os.environ["APPCONFIGURATION_ENDPOINT_STRING"]
credential = DefaultAzureCredential()
# Create app config client
client = AzureAppConfigurationClient(base_url=ENDPOINT, credential=credential)
```

...

</details>

### azure-mgmt-keyvault

Microsoft Azure Keyvault Management Client Library for Python

`pip install azure-mgmt-keyvault` · installs (wheel) · licence: MIT · rank 1726 · last release 2026-10-09 · [PyPI](https://pypi.org/project/azure-mgmt-keyvault/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Key Vault Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Enum `JsonWebKeyType` added member `OCT_HSM`
 - Enum `ManagedHsmSkuName` added member `STANDARD_B10_V2`
 - Enum `ManagedHsmSkuName` added member `STANDARD_B15_V2`
 - Enum `ManagedHsmSkuName` added member `STANDARD_B1_V2`
 - Enum ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### applicationinsights

This project extends the Application Insights API surface to support Python.

`pip install applicationinsights` · installs (wheel) · licence: MIT · rank 1729 · last release 2021-04-22 · [PyPI](https://pypi.org/project/applicationinsights/)

<details><summary>README extract</summary>

This SDK is no longer maintained or supported by Microsoft. Check out the `Python OpenCensus SDK < for Azure Monitor's latest Python investments. Azure Monitor only provides support when using the `supported SDKs < We’re constantly assessing opportunities to expand our support for other languages, so follow our `GitHub Announcements < page to ...

</details>

### azure-mgmt-network

Microsoft Azure Network Management Client Library for Python

`pip install azure-mgmt-network` · installs (wheel) · licence: MIT · rank 1748 · last release 2026-10-12 · [PyPI](https://pypi.org/project/azure-mgmt-network/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Network Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `NetworkManagementClient` added operation group `express_route_lag_authorizations`
 - Client `NetworkManagementClient` added operation group `virtual_network_appliance_capabilities`
 - Model `DdosCustomPolicyPropertiesFormat` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-containerservice

Microsoft Azure Containerservice Management Client Library for Python

`pip install azure-mgmt-containerservice` · installs (wheel) · licence: MIT · rank 1752 · last release 2026-10-19 · [PyPI](https://pypi.org/project/azure-mgmt-containerservice/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Container Service Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `GPUProfile` added property `nvidia`
 - Added enum `ManagementMode`
 - Added model `NvidiaGPUProfile`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = ContainerServiceClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-containerinstance

Microsoft Azure Container Instance Client Library for Python

`pip install azure-mgmt-containerinstance` · installs (wheel) · licence: MIT License · rank 1780 · last release 2023-04-21 · [PyPI](https://pypi.org/project/azure-mgmt-containerinstance/)

<details><summary>README extract</summary>

This is the Microsoft Azure Container Instance Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model Container has a new parameter security_context
 - Model ContainerGroup has a new parameter confidential_compute_properties
 - Model ContainerGroup has a new parameter extensions
 - Model ContainerGroup has a new parameter priority
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-monitor

Microsoft Azure Monitor Client Library for Python

`pip install azure-mgmt-monitor` · installs (wheel) · licence: MIT License · rank 1784 · last release 2025-07-28 · [PyPI](https://pypi.org/project/azure-mgmt-monitor/)

<details><summary>README extract</summary>

This is the Microsoft Azure Monitor Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `MonitorManagementClient` added operation group `action_groups`
 - Client `MonitorManagementClient` added operation group `activity_log_alerts`
 - Client `MonitorManagementClient` added operation group `activity_logs`
 - Client ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-web

Microsoft Azure Web Management Client Library for Python

`pip install azure-mgmt-web` · installs (wheel) · licence: MIT · rank 1817 · last release 2026-07-13 · [PyPI](https://pypi.org/project/azure-mgmt-web/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Web Apps Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Enum `TriggeredWebJobStatus` added member `ABORTED`
 - Enum `TriggeredWebJobStatus` added member `RUNNING`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = WebSiteManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-functions

Python library for Azure Functions.

`pip install azure-functions` · installs (wheel) · licence: MIT License · rank 1838 · last release 2026-08-28 · [PyPI](https://pypi.org/project/azure-functions/)

<details><summary>README extract</summary>

| Branch | CodeCov |

| master | |
| dev | |

Features:
Python support for Azure Functions is based on Python 3.10, 3.11, 3.12, and 3.13 serverless hosting on Linux, and the Functions 2.x (EOL), 3.x (EOL) and 4.0 runtime.

Here is the current status of Python in Azure Functions: ...

Sections: Azure Functions Python Library, Overview, Get Started, Give Feedback

</details>

### azure-search-documents

Microsoft Corporation Azure Search Documents Client Library for Python

`pip install azure-search-documents` · installs (wheel) · licence: not stated · rank 1848 · last release 2026-05-01 · [PyPI](https://pypi.org/project/azure-search-documents/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure AI Search (formerly known as "Azure Cognitive Search") is an AI-powered information retrieval platform that helps developers build rich search experiences and generative AI apps that combine large language models with enterprise data.

Azure AI Search is well suited for the following application scenarios: ...

Features:
- Below clients, models, and enum members are added for knowledge base support
 - `azure.search.documents.knowledgebases.KnowledgeBaseRetrievalClient`
 - `azure.search.documents.indexes.models.AzureBlobKnowledgeSource`
 - ...

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

service_endpoint = os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
index_name = os.environ["AZURE_SEARCH_INDEX_NAME"]
...

</details>

### azure-mgmt-redis

Microsoft Azure Redis Cache Management Client Library for Python

`pip install azure-mgmt-redis` · installs (wheel) · licence: MIT License · rank 1860 · last release 2025-01-20 · [PyPI](https://pypi.org/project/azure-mgmt-redis/)

<details><summary>README extract</summary>

This is the Microsoft Azure Redis Cache Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `RedisCommonProperties` added property `zonal_allocation_policy`
 - Model `RedisCreateParameters` added property `zonal_allocation_policy`
 - Model `RedisCreateProperties` added property `zonal_allocation_policy`
 - Model `RedisProperties` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.redis import RedisManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-msi

Microsoft Azure Msi Management Client Library for Python

`pip install azure-mgmt-msi` · installs (wheel) · licence: MIT License · rank 1872 · last release 2025-07-21 · [PyPI](https://pypi.org/project/azure-mgmt-msi/)

<details><summary>README extract</summary>

This is the Microsoft Azure Msi Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model Identity has a new parameter isolation_scope
 - Model IdentityUpdate has a new parameter isolation_scope

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.msi import ManagedServiceIdentityClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = ManagedServiceIdentityClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### autoevals

Universal library for evaluating AI models

`pip install autoevals` · installs (wheel) · licence: not stated · rank 1875 · last release 2026-10-21 · [PyPI](https://pypi.org/project/autoevals/)

<details><summary>README extract</summary>

Autoevals is a tool to quickly and easily evaluate AI model outputs.

It bundles together a variety of automatic evaluation methods including:

- LLM-as-a-judge
- Heuristic (e.g. Levenshtein distance)
- Statistical (e.g. BLEU)

Autoevals is developed by the team at Braintrust. ...

Features:
There is nothing particularly novel about the evaluation methods in this library. They are all well-known and well-documented. However, there are a few things that are particularly difficult when evaluating in practice: ...

Example:
```python
from autoevals.llm import *
import asyncio

# Create a new LLM-based evaluator
evaluator = Factuality()

# Synchronous evaluation
input = "Which country has the highest population?"
output = "People's Republic of China"
expected = "China"

...

</details>

### azure-mgmt-cognitiveservices

Microsoft Azure Cognitiveservices Management Client Library for Python

`pip install azure-mgmt-cognitiveservices` · installs (wheel) · licence: not stated · rank 1897 · last release 2025-10-24 · [PyPI](https://pypi.org/project/azure-mgmt-cognitiveservices/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Cognitive Services Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `CognitiveServicesManagementClient` added parameter `cloud_setting` in method `init`
 - Client `CognitiveServicesManagementClient` added operation group `rai_topics`
 - Client `CognitiveServicesManagementClient` added operation group ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-devops

Python wrapper around the Azure DevOps 7.x APIs

`pip install azure-devops` · installs (wheel) · licence: MIT License · rank 1908 · last release 2023-11-20 · [PyPI](https://pypi.org/project/azure-devops/)

### azure-eventgrid

Microsoft Azure Event Grid Client Library for Python

`pip install azure-eventgrid` · installs (wheel) · licence: MIT License · rank 1910 · last release 2026-07-29 · [PyPI](https://pypi.org/project/azure-eventgrid/)

<details><summary>README extract</summary>

Azure Event Grid is a fully-managed intelligent event routing service that allows for uniform event consumption using a publish-subscribe model.

Source code
| Package (PyPI)
| Package (Conda)
| API reference documentation
| Product documentation
| Samples
| Changelog ...

Example:
```python
# Event Grid Namespace client
client = EventGridPublisherClient(endpoint, credential, namespace_topic=YOUR_TOPIC_NAME)

# Event Grid Basic Client
client = EventGridPublisherClient(endpoint, credential)
```

...

</details>

### azure-mgmt-sql

Microsoft Azure Sql Management Client Library for Python

`pip install azure-mgmt-sql` · installs (wheel) · licence: MIT · rank 1912 · last release 2026-07-01 · [PyPI](https://pypi.org/project/azure-mgmt-sql/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure SQL Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `SqlManagementClient` added parameter `cloud_setting` in method `init`
 - Client `SqlManagementClient` added method `send_request`
 - Client `SqlManagementClient` added operation group `sql_vulnerability_assessment_baseline`
 - Client ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-loganalytics

Microsoft Azure Loganalytics Management Client Library for Python

`pip install azure-mgmt-loganalytics` · installs (wheel) · licence: MIT · rank 1918 · last release 2026-06-24 · [PyPI](https://pypi.org/project/azure-mgmt-loganalytics/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Log Analytics Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `LogAnalyticsManagementClient` added method `send_request`
 - Model `AzureEntityResource` added property `system_data`
 - Model `Cluster` added property `system_data`
 - Model `DataExport` added property `system_data`
 - Model `DataSource` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### asyncstdlib

The missing async toolbox

`pip install asyncstdlib` · installs (wheel) · licence: MIT License · rank 1923 · last release 2026-03-20 · [PyPI](https://pypi.org/project/asyncstdlib/) · [docs](https://asyncstdlib.readthedocs.io/en/latest/) · [source](https://github.com/maxfischer2781/asyncstdlib)

<details><summary>README extract</summary>

The `asyncstdlib` library re-implements functions and classes of the Python
standard library to make them compatible with `async` callables, iterables
and context managers.
It is fully agnostic to `async` event loops and seamlessly works with
`asyncio`, third-party libraries such as `trio`, as well as
any custom `async` event loop. ...

</details>

### azure-ai-agents

Microsoft Corporation Azure AI Agents Client Library for Python

`pip install azure-ai-agents` · installs (wheel) · licence: MIT License · rank 1926 · last release 2025-08-05 · [PyPI](https://pypi.org/project/azure-ai-agents/)

<details><summary>README extract</summary>

<!-- PIPY LONG DESCRIPTION BEGIN -->

Use the AI Agents client library to:

* Develop Agents using the Azure AI Agents Service, leveraging an extensive ecosystem of models, tools, and capabilities from OpenAI, Microsoft, and other LLM providers. The Azure AI Agents Service enables the building of Agents for a wide range of generative AI use cases. ...

Example:
```python
import os
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential

agents_client = AgentsClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
```

...

</details>

### alibabacloud-oss-v2

Alibaba Cloud OSS (Object Storage Service) SDK V2 for Python

`pip install alibabacloud-oss-v2` · installs (wheel) · licence: Apache Software License · rank 1948 · last release 2026-10-19 · [PyPI](https://pypi.org/project/alibabacloud-oss-v2/)

<details><summary>README extract</summary>

alibabacloud-oss-python-sdk-v2 is the v2 of the OSS SDK for the Python programming language

> - This Python SDK is based on the official APIs of Alibaba Cloud OSS.
> - Alibaba Cloud Object Storage Service (OSS) is a cloud storage service provided by Alibaba Cloud, featuring massive capacity, security, a low cost, and high reliability. ...

Example:
```python
import alibabacloud_oss_v2 as oss

def main():

    region = "cn-hangzhou"

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
...
```

...

</details>

### azure-mgmt-datalake-store

Microsoft Azure Data Lake Store Management Client Library for Python

`pip install azure-mgmt-datalake-store` · installs (wheel) · licence: MIT License · rank 1960 · last release 2018-06-14 · [PyPI](https://pypi.org/project/azure-mgmt-datalake-store/)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Lake Store Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6. ...

Sections: Microsoft Azure SDK for Python, Compatibility, Usage, Provide Feedback, 0.5.0 (2018-06-14), 0.4.0 (2018-02-12), 0.3.0 (2018-01-09), 0.2.0 (2017-08-17), 0.1.6 (2017-06-19), 0.1.5 (2017-06-07), 0.1.4 (2017-04-20), 0.1.3 (2017-02-13), 0.1.2 (2017-01-09), 0.1.1 (2016-12-12)

</details>

### azure-nspkg

Microsoft Azure Namespace Package [Internal]

`pip install azure-nspkg` · installs (wheel) · licence: MIT License · rank 1963 · last release 2018-10-02 · [PyPI](https://pypi.org/project/azure-nspkg/)

<details><summary>README extract</summary>

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use PEP420 as namespace package strategy. ...

</details>

### azure-kusto-ingest

Kusto Ingest Client

`pip install azure-kusto-ingest` · installs (wheel) · licence: MIT · rank 1976 · last release 2026-05-06 · [PyPI](https://pypi.org/project/azure-kusto-ingest/) · [source](https://github.com/Azure/azure-kusto-python)

<details><summary>README extract</summary>

Features:
*Kusto Python Ingest Client* Library provides the capability to ingest data into Kusto clusters using Python.
It is Python 3.x compatible and supports data types through familiar Python DB API interface. ...

Example:
```python
from azure.kusto.data import KustoConnectionStringBuilder, DataFormat
from azure.kusto.ingest import QueuedIngestClient, IngestionProperties, FileDescriptor, BlobDescriptor

ingestion_props = IngestionProperties(database="{database_name}", table="{table_name}", data_format=DataFormat.CSV)
...
```

Sections: Microsoft Azure Kusto Ingest Library for Python, Overview

</details>

### azure-mgmt-applicationinsights

Microsoft Azure Application Insights Management Client Library for Python

`pip install azure-mgmt-applicationinsights` · installs (wheel) · licence: MIT License · rank 1979 · last release 2025-03-06 · [PyPI](https://pypi.org/project/azure-mgmt-applicationinsights/)

<details><summary>README extract</summary>

This is the Microsoft Azure Application Insights Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation group DeletedWorkbooksOperations
 - Model Resource has a new parameter system_data
 - Model TrackedResource has a new parameter system_data

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.applicationinsights import ApplicationInsightsManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-rdbms

Microsoft Azure Rdbms Management Client Library for Python

`pip install azure-mgmt-rdbms` · installs (wheel) · licence: not stated · rank 2012 · last release 2025-11-25 · [PyPI](https://pypi.org/project/azure-mgmt-rdbms/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure RDBMS Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added model ServerDetachVNetParameter
 - Added model StorageRedundancyEnum

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.rdbms.mysql import MySQLManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = MySQLManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### atomicwrites

Atomic file writes.

`pip install atomicwrites` · installs from source (sdist only) · licence: MIT License · rank 2015 · last release 2022-07-08 · [PyPI](https://pypi.org/project/atomicwrites/)

<details><summary>README extract</summary>

Atomic file writes.

See API documentation for more
low-level interfaces.

Features that distinguish it from other similar libraries (see Alternatives and Credit):

- Race-free assertion that the target file doesn't yet exist. This can be
 controlled with the `overwrite` parameter.

- Windows support, although not well-tested. ...

Example:
```python
from atomicwrites import atomic_write

with atomic_write('foo.txt', overwrite=True) as f:
    f.write('Hello world.')
    # "foo.txt" doesn't exist yet.

# Now it does.
```

Sections: python-atomicwrites, How it works, fsync, Alternatives and Credit

</details>

### azure-mgmt-eventhub

Microsoft Azure Eventhub Management Client Library for Python

`pip install azure-mgmt-eventhub` · installs (wheel) · licence: MIT · rank 2020 · last release 2026-07-30 · [PyPI](https://pypi.org/project/azure-mgmt-eventhub/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Event Hub Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `EventHubManagementClient` added parameter `cloud_setting` in method `init`
 - Client `EventHubManagementClient` added method `send_request`
 - Model `NetworkSecurityPerimeterConfiguration` added property `system_data`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub import EventHubManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-recoveryservices

Microsoft Azure Recoveryservices Management Client Library for Python

`pip install azure-mgmt-recoveryservices` · installs (wheel) · licence: MIT · rank 2026 · last release 2026-11-03 · [PyPI](https://pypi.org/project/azure-mgmt-recoveryservices/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Recovery Services Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `VaultProperties` added property `region_of_choice_settings`
 - Added model `RegionOfChoiceSettings`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservices import RecoveryServicesClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = RecoveryServicesClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-recoveryservicesbackup

Microsoft Azure Recoveryservicesbackup Management Client Library for Python

`pip install azure-mgmt-recoveryservicesbackup` · installs (wheel) · licence: MIT · rank 2032 · last release 2026-10-16 · [PyPI](https://pypi.org/project/azure-mgmt-recoveryservicesbackup/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Recovery Services Backup Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `RecoveryServicesBackupClient` added operation group `protection_container_refresh_operation_statuses`
 - Model `AzureIaaSClassicComputeVMProtectedItem` added property `existing_basic_vm_protection`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicesbackup import RecoveryServicesBackupClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### asyncpg-stubs

asyncpg stubs

`pip install asyncpg-stubs` · installs (wheel) · licence: BSD-3-Clause · rank 2034 · last release 2026-10-06 · [PyPI](https://pypi.org/project/asyncpg-stubs/)

<details><summary>README extract</summary>

This package contains type stubs to provide more precise static types and type inference for asyncpg.

Sections: asyncpg-stubs, Version numbering scheme

</details>

### azure-mgmt-servicebus

Microsoft Azure Servicebus Management Client Library for Python

`pip install azure-mgmt-servicebus` · installs (wheel) · licence: MIT · rank 2039 · last release 2026-07-20 · [PyPI](https://pypi.org/project/azure-mgmt-servicebus/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Service Bus Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ServiceBusManagementClient` added parameter `cloud_setting` in method `init`
 - Client `ServiceBusManagementClient` added method `send_request`
 - Client `ServiceBusManagementClient` added operation group ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicebus import ServiceBusManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-cdn

Microsoft Azure Cdn Management Client Library for Python

`pip install azure-mgmt-cdn` · installs (wheel) · licence: MIT · rank 2047 · last release 2026-10-28 · [PyPI](https://pypi.org/project/azure-mgmt-cdn/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure CDN Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `AFDDomainHttpsParameters` added property `server_tls_group_policy`
 - Model `AFDDomainHttpsParameters` added property `server_tls_groups`
 - Model `AFDDomainProperties` added property `mtls_settings`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.cdn import CdnManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### aiostream

Generator-based operators for asynchronous iteration

`pip install aiostream` · installs (wheel) · licence: GPL-3.0-or-later · rank 2070 · last release 2026-09-16 · [PyPI](https://pypi.org/project/aiostream/)

_README extract left out: share-alike licence._

### azure-mgmt-eventgrid

Microsoft Azure Event Grid Management Client Library for Python

`pip install azure-mgmt-eventgrid` · installs (wheel) · licence: MIT License · rank 2074 · last release 2025-03-24 · [PyPI](https://pypi.org/project/azure-mgmt-eventgrid/)

<details><summary>README extract</summary>

This is the Microsoft Azure Event Grid Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `EventGridManagementClient` added operation group `ca_certificates`
 - Client `EventGridManagementClient` added operation group `client_groups`
 - Client `EventGridManagementClient` added operation group `clients`
 - Client ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.eventgrid import EventGridManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-search

Microsoft Azure Search Management Client Library for Python

`pip install azure-mgmt-search` · installs (wheel) · licence: MIT License · rank 2084 · last release 2025-07-21 · [PyPI](https://pypi.org/project/azure-mgmt-search/)

<details><summary>README extract</summary>

This is the Microsoft Azure Search Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `SearchManagementClient` added operation group `network_security_perimeter_configurations`
 - Model `Identity` added property `user_assigned_identities`
 - Enum `IdentityType` added member `SYSTEM_ASSIGNED_USER_ASSIGNED`
 - Enum ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.search import SearchManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-managementgroups

Microsoft Azure Managementgroups Management Client Library for Python

`pip install azure-mgmt-managementgroups` · installs (wheel) · licence: MIT · rank 2096 · last release 2026-06-29 · [PyPI](https://pypi.org/project/azure-mgmt-managementgroups/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Management Groups Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `HierarchySettings` added property `system_data`
 - Model `ManagementGroup` added property `system_data`
 - Enum `ManagementGroupChildType` added member `SUBSCRIPTIONS`
 - Model `Operation` added property `is_data_action`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.managementgroups import ManagementGroupsMgmtClient

client = ManagementGroupsMgmtClient(credential=DefaultAzureCredential())
```

...

</details>

### azure-mgmt-trafficmanager

Microsoft Azure Trafficmanager Management Client Library for Python

`pip install azure-mgmt-trafficmanager` · installs (wheel) · licence: MIT · rank 2108 · last release 2026-09-29 · [PyPI](https://pypi.org/project/azure-mgmt-trafficmanager/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Traffic Manager Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `TrafficManagerManagementClient` added parameter `cloud_setting` in method `init`
 - Client `TrafficManagerManagementClient` added method `send_request`
 - Model `Endpoint` added property `properties`
 - Model `HeatMapModel` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.trafficmanager import TrafficManagerManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-batch

Microsoft Azure Batch Management Client Library for Python

`pip install azure-mgmt-batch` · installs (wheel) · licence: not stated · rank 2117 · last release 2026-03-12 · [PyPI](https://pypi.org/project/azure-mgmt-batch/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Batch Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `BatchManagementClient` added parameter `cloud_setting` in method `init`
 - Client `BatchManagementClient` added method `send_request`
 - Model `Application` added property `system_data`
 - Model `ApplicationPackage` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.batch import BatchManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-iothub

Microsoft Azure IoT Hub Management Client Library for Python

`pip install azure-mgmt-iothub` · installs (wheel) · licence: MIT License · rank 2147 · last release 2025-04-09 · [PyPI](https://pypi.org/project/azure-mgmt-iothub/)

<details><summary>README extract</summary>

This is the Microsoft Azure IoT Hub Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model RoutingEndpoints has a new parameter cosmos_db_sql_containers

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.iothub import IotHubClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = IotHubClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-ai-inference

Microsoft Azure AI Inference Client Library for Python

`pip install azure-ai-inference` · installs (wheel) · licence: MIT License · rank 2155 · last release 2025-02-15 · [PyPI](https://pypi.org/project/azure-ai-inference/)

<details><summary>README extract</summary>

Use the Inference client library (in preview) to:

* Authenticate against the service
* Get information about the AI model
* Do chat completions
* Get text embeddings
* Get image embeddings

The Inference client library supports AI models deployed to the following services: ...

Example:
```python
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response = client.complete(
    messages=[
...
```

...

</details>

### azure-graphrbac

Microsoft Azure Graph RBAC Client Library for Python

`pip install azure-graphrbac` · installs (wheel) · licence: MIT License · rank 2175 · last release 2024-10-31 · [PyPI](https://pypi.org/project/azure-graphrbac/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 10-31-2024. This package will only receive security fixes until 10-31-2024. Refer to the samples in the MS Graph SDK for Python repo instead.

For additional support, open a new issue in the Issues section of the MS Graph SDK for Python repo.

Sections: Microsoft Azure SDK for Python, 0.61.2 (2024-10-31), Other Changes, 0.61.1 (2019-05-29), 0.61.0 (2019-03-20), 0.60.0 (2019-03-13), 0.53.0 (2018-11-27), 0.52.0 (2018-10-29), 0.51.1 (2018-10-16), 0.51.0 (2018-10-11), 0.50.0 (2018-10-10), 0.40.0 (2018-02-05), 0.33.0 (2017-11-01), 0.32.0 (2017-09-22)

</details>

### azure-mgmt-advisor

Microsoft Azure Advisor Management Client Library for Python

`pip install azure-mgmt-advisor` · installs (wheel) · licence: not stated · rank 2181 · last release 2026-05-13 · [PyPI](https://pypi.org/project/azure-mgmt-advisor/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Advisor Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model ResourceMetadata has a new parameter action
 - Model ResourceMetadata has a new parameter plural
 - Model ResourceMetadata has a new parameter singular
 - Model ResourceRecommendationBase has a new parameter actions
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.advisor import AdvisorManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-marketplaceordering

Microsoft Azure Marketplaceordering Management Client Library for Python

`pip install azure-mgmt-marketplaceordering` · installs (wheel) · licence: not stated · rank 2182 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-marketplaceordering/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Market Place Ordering Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model OperationDisplay has a new parameter description

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.marketplaceordering import MarketplaceOrderingAgreements
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = MarketplaceOrderingAgreements(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-servicefabric

Microsoft Azure Service Fabric Management Client Library for Python

`pip install azure-mgmt-servicefabric` · installs (wheel) · licence: MIT License · rank 2194 · last release 2023-12-18 · [PyPI](https://pypi.org/project/azure-mgmt-servicefabric/)

<details><summary>README extract</summary>

This is the Microsoft Azure Service Fabric Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added model ClusterVersionsEnvironment

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicefabric import ServiceFabricManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = ServiceFabricManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-policyinsights

Microsoft Azure Policyinsights Management Client Library for Python

`pip install azure-mgmt-policyinsights` · installs (wheel) · licence: not stated · rank 2196 · last release 2026-05-19 · [PyPI](https://pypi.org/project/azure-mgmt-policyinsights/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Policy Insights Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `CheckRestrictionsRequest` added property `include_audit_effect`
 - Model `FieldRestriction` added property `policy_effect`
 - Model `FieldRestriction` added property `reason`
 - Enum `FieldRestrictionResult` added member `AUDIT`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.policyinsights import PolicyInsightsClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-apimanagement

Microsoft Azure API Management Client Library for Python

`pip install azure-mgmt-apimanagement` · installs (wheel) · licence: MIT License · rank 2197 · last release 2025-04-22 · [PyPI](https://pypi.org/project/azure-mgmt-apimanagement/)

<details><summary>README extract</summary>

This is the Microsoft Azure API Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ApiManagementClient` added operation group `api_gateway`
 - Client `ApiManagementClient` added operation group `api_management_gateway_skus`
 - Client `ApiManagementClient` added operation group `all_policies`
 - Client ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-privatedns

Microsoft Azure Privatedns Management Client Library for Python

`pip install azure-mgmt-privatedns` · installs (wheel) · licence: MIT · rank 2206 · last release 2026-07-29 · [PyPI](https://pypi.org/project/azure-mgmt-privatedns/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure DNS Private Zones Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `PrivateDnsManagementClient` added parameter `cloud_setting` in method `init`
 - Client `PrivateDnsManagementClient` added method `send_request`
 - Model `PrivateZone` added property `system_data`
 - Model `ProxyResource` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.privatedns import PrivateDnsManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-signalr

Microsoft Azure SignalR Client Library for Python

`pip install azure-mgmt-signalr` · installs (wheel) · licence: MIT License · rank 2215 · last release 2023-03-20 · [PyPI](https://pypi.org/project/azure-mgmt-signalr/)

<details><summary>README extract</summary>

This is the Microsoft Azure SignalR Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model SignalRResource has a new parameter serverless

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.signalr import SignalRManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = SignalRManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-synapse-artifacts

Microsoft Azure Synapse Artifacts Client Library for Python

`pip install azure-synapse-artifacts` · installs (wheel) · licence: MIT License · rank 2217 · last release 2026-03-23 · [PyPI](https://pypi.org/project/azure-synapse-artifacts/)

<details><summary>README extract</summary>

This is the Microsoft Azure Synapse Artifacts Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model AzureDatabricksDeltaLakeLinkedService has a new parameter workspace_resource_id
- Model HDInsightOnDemandLinkedService has a new parameter cluster_resource_group_auth_type
- Model JiraObjectDataset has a new parameter table ...

Example:
```python
import os
from azure.identity import DefaultAzureCredential
from azure.synapse.artifacts import ArtifactsClient

endpoint = os.environ["SYNAPSE_ARTIFACTS_ENDPOINT"]
...

</details>

### azure-mgmt-datamigration

Microsoft Azure Data Migration Client Library for Python

`pip install azure-mgmt-datamigration` · installs (wheel) · licence: MIT License · rank 2235 · last release 2025-09-22 · [PyPI](https://pypi.org/project/azure-mgmt-datamigration/)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Migration Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `DataMigrationManagementClient` added operation group `database_migrations_mongo_to_cosmos_db_ru_mongo`
 - Client `DataMigrationManagementClient` added operation group `database_migrations_mongo_to_cosmos_dbv_core_mongo`
 - Client ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.datamigration import DataMigrationManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### awslambdaric

AWS Lambda Runtime Interface Client for Python

`pip install awslambdaric` · installs (wheel) · licence: Apache Software License · rank 2237 · last release 2026-10-27 · [PyPI](https://pypi.org/project/awslambdaric/)

<details><summary>README extract</summary>

We have open-sourced a set of software packages, Runtime Interface Clients (RIC), that implement the Lambda
 Runtime API, allowing you to seamlessly extend your preferred
 base images to be Lambda compatible. ...

Example:
```python
def handler(event, context):
    return "Hello World!"
```

Sections: AWS Lambda Python Runtime Interface Client, Requirements, Usage, Structured (JSON) logging, Building the package, Running tests, Troubleshooting

</details>

### azure-mgmt-billing

Microsoft Azure Billing Management Client Library for Python

`pip install azure-mgmt-billing` · installs (wheel) · licence: MIT · rank 2244 · last release 2026-06-24 · [PyPI](https://pypi.org/project/azure-mgmt-billing/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Billing Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `BillingManagementClient` added parameter `cloud_setting` in method `init`
 - Client `BillingManagementClient` added method `send_request`
 - Added model `ReservationPropertyUtilization`
 - Added model `PatchPropertiesRenewProperties`
 - ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.billing import BillingManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-media

Microsoft Azure Media Services Client Library for Python

`pip install azure-mgmt-media` · installs (wheel) · licence: MIT License · rank 2246 · last release 2025-06-03 · [PyPI](https://pypi.org/project/azure-mgmt-media/)

<details><summary>README extract</summary>

Please note, this package has been deprecated and will no longer be maintained after 06/30/2024.
Refer to Azure Media Services retirement guide for more retirement details and how to migrate to the new services.
Refer to our deprecation policy ( for more details.

This is the Microsoft Azure Media Services Client Library. ...

Features:
- Model Filters has a new parameter fade_in
 - Model Filters has a new parameter fade_out
 - Model StandardEncoderPreset has a new parameter experimental_options

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.media import MediaManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = MediaManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-iothubprovisioningservices

Microsoft Azure Iothubprovisioningservices Management Client Library for Python

`pip install azure-mgmt-iothubprovisioningservices` · installs (wheel) · licence: MIT · rank 2251 · last release 2026-10-28 · [PyPI](https://pypi.org/project/azure-mgmt-iothubprovisioningservices/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure IoT Hub Provisioning Services Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `IotDpsPropertiesDescription` added property `device_registry_namespaces`
 - Added enum `DeviceRegistryNamespaceAuthenticationType`
 - Added model `DeviceRegistryNamespaceDescription`
 - Added enum `LinkingState`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.iothubprovisioningservices import IotDpsClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-maps

Microsoft Azure Maps Client Library for Python

`pip install azure-mgmt-maps` · installs (wheel) · licence: MIT License · rank 2252 · last release 2023-09-12 · [PyPI](https://pypi.org/project/azure-mgmt-maps/)

<details><summary>README extract</summary>

This is the Microsoft Azure Maps Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation AccountsOperations.list_sas
 - Added operation MapsOperations.list_subscription_operations
 - Model Creator has a new parameter system_data
 - Model Dimension has a new parameter internal_metric_name
 - Model Dimension has a new ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.maps import AzureMapsManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-batchai

Microsoft Azure Batch AI Management Client Library for Python

`pip install azure-mgmt-batchai` · installs (wheel) · licence: MIT License · rank 2253 · last release 2024-10-31 · [PyPI](https://pypi.org/project/azure-mgmt-batchai/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 10-31-2024. This package will only receive security fixes until 10-31-2024. To receive updates on new features and non-security bug fixes, upgrade to the replacement package, azureml-core. Refer to the migration guide ( for guidance on upgrading.

Sections: Microsoft Azure SDK for Python, 7.0.0 (2024-10-31), Other Changes, 7.0.0b1 (2021-06-02), 2.0.0 (2018-06-07), 1.0.1 (2018-04-16), 1.0.0 (2018-03-19), 0.2.0 (2017-10-05), 0.1.0 (2017-10-03)

</details>

### azure-mgmt-iotcentral

Microsoft Azure Iotcentral Management Client Library for Python

`pip install azure-mgmt-iotcentral` · installs (wheel) · licence: not stated · rank 2255 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-iotcentral/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Iot Central Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.iotcentral import IotCentralClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = IotCentralClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-communication-email

Microsoft Azure MyService Management Client Library for Python

`pip install azure-communication-email` · installs (wheel) · licence: MIT License · rank 2270 · last release 2025-10-17 · [PyPI](https://pypi.org/project/azure-communication-email/)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Communication Services for Email.

The Azure Communication Email package is used to send emails to multiple types of recipients.

Features:
- Consumers can now provide a value for the `contentId` property when sending emails with attachments.
 This allows consumers to reference attachments in the email body using the `cid` scheme. ...

Example:
```python
from azure.communication.email import EmailClient

connection_string = "endpoint=
client = EmailClient.from_connection_string(connection_string);
```

...

</details>

### azure-mgmt-appcontainers

Microsoft Azure Appcontainers Management Client Library for Python

`pip install azure-mgmt-appcontainers` · installs (wheel) · licence: MIT · rank 2271 · last release 2026-09-15 · [PyPI](https://pypi.org/project/azure-mgmt-appcontainers/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Appcontainers Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ContainerAppsAPIClient` added operation group `available_environment_modes`
 - Client `ContainerAppsAPIClient` added operation group `container_app_private_endpoint_connections`
 - Client `ContainerAppsAPIClient` added operation group ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.appcontainers import ContainerAppsAPIClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-synapse-spark

Microsoft Azure Synapse Spark Client Library for Python

`pip install azure-synapse-spark` · installs (wheel) · licence: MIT License · rank 2296 · last release 2021-10-05 · [PyPI](https://pypi.org/project/azure-synapse-spark/)

<details><summary>README extract</summary>

This is the Microsoft Azure Synapse Spark Client Library.
This package has been tested with Python 2.7, 3.6, 3.7, 3.8 and 3.9.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 is ending 01 January 2022. For more information and questions, please refer to

Features:
- Added `LivyStatementStates` and `LivyStates`

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 0.7.0 (2021-10-05), Features Added, 0.6.0 (2021-08-10), 0.5.0 (2021-03-09), 0.4.0 (2020-12-08), 0.3.0 (2020-09-15), 0.2.0 (2020-07-01)

</details>

### async_generator

Async generators and context managers for Python 3.5+

`pip install async_generator` · installs (wheel) · licence: Apache Software License; MIT License · rank 2307 · last release 2018-08-01 · [PyPI](https://pypi.org/project/async_generator/)

<details><summary>README extract</summary>

Python 3.6 added async generators. (What's an async
generator? Check out my 5-minute lightning talk demo from PyCon 2016.) Python 3.7 adds some more
tools to make them usable, like `contextlib.asynccontextmanager`.

This library gives you all that back to Python 3.5.

For example, this code only works in Python 3.6+: ...

Example:
```python
async def load_json_lines(stream_reader):
    async for line in stream_reader:
        yield json.loads(line)
```

Sections: The async_generator library, Let's do this, How come some of those links talk about "trio"?

</details>

### alembic-postgresql-enum

Alembic autogenerate support for creation, alteration and deletion of enums

`pip install alembic-postgresql-enum` · installs (wheel) · licence: MIT · rank 2375 · last release 2026-10-27 · [PyPI](https://pypi.org/project/alembic-postgresql-enum/) · [source](https://github.com/Pogchamp-company/alembic-postgresql-enum)

<details><summary>README extract</summary>

[](
[](
[](

Alembic autogenerate support for creation, alteration and deletion of enums

Alembic will now automatically:
- Create enums that currently are not in postgres schema
- Remove/add/alter enum values
- Reorder enum values
- Delete unused enums from schema ...

Features:
* Creation of enums
* Deletion of unreferenced enums
* Detection of enum values changes
 * Creation of new enum values
 * Deletion of enums values
 * Renaming of enum values
* Partial index preservation
* Omitting managing enums

Example:
```python
# env.py
import alembic_postgresql_enum
...
```

...

</details>

### asana

Asana

`pip install asana` · installs (wheel) · licence: MIT · rank 2382 · last release 2026-10-27 · [PyPI](https://pypi.org/project/asana/)

<details><summary>README extract</summary>

- API version: 1.0
- Package version: 5.5.1

Python 3.4+

Example:
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = "me"
opts = {}

try:
    # Get a user
...
```

Sections: asana []() [][pypi-url], Requirements., Setuptools, Getting Started, Example: GET, POST, PUT, DELETE on tasks, GET - get multiple tasks, POST - create a task, PUT - update a task, DELETE - delete a task, Documentation for API Endpoints, Accessing response data, Example: Accessing task data, On the client, On the request

</details>

### azure-ai-ml

Microsoft Azure Machine Learning Client Library for Python

`pip install azure-ai-ml` · installs (wheel) · licence: MIT · rank 2389 · last release 2026-10-12 · [PyPI](https://pypi.org/project/azure-ai-ml/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

We are excited to introduce the GA of Azure Machine Learning Python SDK v2. The Python SDK v2 introduces new SDK capabilities like standalone local jobs, reusable components for pipelines and managed online/batch inferencing. Python SDK v2 allows you to move from simple to complex tasks easily and incrementally. ...

Features:
- Added Spark runtime 3.5 support for model monitoring serverless Spark compute while retaining runtime 3.4 support.

Example:
```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
```

...

</details>

### astropy-iers-data

IERS Earth Rotation and Leap Second tables for the astropy core package

`pip install astropy-iers-data` · installs (wheel) · licence: BSD-3-Clause · rank 2435 · last release 2026-11-02 · [PyPI](https://pypi.org/project/astropy-iers-data/) · [docs](https://github.com/astropy/astropy-iers-data/blob/main/README.rst) · [source](https://github.com/astropy/astropy-iers-data)

<details><summary>README extract</summary>

Note: This package is not currently meant to be used directly by users, and only
meant to be used from the core astropy package.

</details>

### adbc-driver-manager

A generic entrypoint for ADBC drivers.

`pip install adbc-driver-manager` · installs (wheel) · licence: Apache-2.0 · rank 2440 · last release 2026-10-26 · [PyPI](https://pypi.org/project/adbc-driver-manager/) · [source](https://github.com/apache/arrow-adbc)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Sections: ADBC Driver Manager for Python, Building

</details>

### aws-bedrock-token-generator

A lightweight library for generating short-term bearer tokens for AWS Bedrock API authentication

`pip install aws-bedrock-token-generator` · installs (wheel) · licence: Apache Software License · rank 2441 · last release 2025-07-29 · [PyPI](https://pypi.org/project/aws-bedrock-token-generator/) · [docs](https://github.com/aws/aws-bedrock-token-generator-python#readme) · [source](https://github.com/aws/aws-bedrock-token-generator-python)

<details><summary>README extract</summary>

The AWS Bedrock Token Generator for Python is a lightweight utility library that generates short-term bearer tokens for AWS Bedrock API authentication. This library simplifies the process of creating secure, time-limited tokens that can be used to authenticate with AWS Bedrock services without exposing long-term credentials.

Example:
```python
from aws_bedrock_token_generator import provide_token

token = provide_token()  # uses AWS_REGION env var and default credential chain
print(f"Token: {token}")
```

...

</details>

### anywidget

custom jupyter widgets made easy

`pip install anywidget` · installs (wheel) · licence: MIT · rank 2458 · last release 2026-04-27 · [PyPI](https://pypi.org/project/anywidget/)

<details><summary>README extract</summary>

anywidget

 reusable widgets made easy

 installation .
 docs .
 discord .
 learn

anywidget is both a specification and
toolkit for authoring reusable web-based widgets for interactive computing
environments.

- 🛠️ create custom Jupyter Widgets without complicated cookiecutter templates
- 📚 publish to PyPI like any other Python package ...

Example:
```python
import anywidget
import traitlets

class CounterWidget(anywidget.AnyWidget):
    # Widget front-end JavaScript code
    _esm = """
    function render({ model, el }) {
      let button = document.createElement("button");
      button.innerHTML = `count is ${model.get("value")}`;
      button.addEventListener("click", () => {
...
```

Sections: About, Usage, Packages

</details>

### azure-mgmt-security

Microsoft Azure Security Center Management Client Library for Python

`pip install azure-mgmt-security` · installs (wheel) · licence: MIT License · rank 2486 · last release 2024-05-20 · [PyPI](https://pypi.org/project/azure-mgmt-security/)

<details><summary>README extract</summary>

This is the Microsoft Azure Security Center Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation HealthReportsOperations.get
 - Added operation PricingsOperations.delete
 - Added operation group AzureDevOpsOrgsOperations
 - Added operation group AzureDevOpsProjectsOperations
 - Added operation group AzureDevOpsReposOperations ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.security import SecurityCenter
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-postgresqlflexibleservers

Microsoft Azure Postgresqlflexibleservers Management Client Library for Python

`pip install azure-mgmt-postgresqlflexibleservers` · installs (wheel) · licence: MIT · rank 2487 · last release 2026-11-03 · [PyPI](https://pypi.org/project/azure-mgmt-postgresqlflexibleservers/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Postgresqlflexibleservers Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `PostgreSQLManagementClient` added method `send_request`
 - Client `PostgreSQLManagementClient` added operation group `maintenance_events`
 - Client `PostgreSQLManagementClient` added operation group `major_version_upgrade_precheck`
 - ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.postgresqlflexibleservers import PostgreSQLManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-cli-core

Microsoft Azure Command-Line Tools Core Module

`pip install azure-cli-core` · installs (wheel) · licence: MIT · rank 2504 · last release 2026-11-03 · [PyPI](https://pypi.org/project/azure-cli-core/)

### alive-progress

A new kind of Progress Bar, with real-time throughput, ETA, and very cool animations!

`pip install alive-progress` · installs (wheel) · licence: MIT License · rank 2513 · last release 2025-07-20 · [PyPI](https://pypi.org/project/alive-progress/)

<details><summary>README extract</summary>

[](
[](

Have you ever wondered where your lengthy processing was at, and when would it finish? Do you usually hit `RETURN` several times to make sure it didn't crash, or the SSH connection didn't freeze? Have you ever thought it'd be awesome to be able to _pause some processing without hassle, return to the Python prompt to manually fix some ...

Example:
```python
from alive_progress.styles import showtime

showtime()
```

Sections: alive-progress, 📌 What's new in 3.3 series, Using `alive-progress`, Get it, Try it, Awake it, Master it, The `bar` handler, Auto-iterating, Modes of operation, Auto and Unknown: Counter, Manual: Percentage, Widgets available, The different `bar()` handler semantics

</details>

### azure-mgmt-appconfiguration

Microsoft Azure App Configuration Management Client Library for Python

`pip install azure-mgmt-appconfiguration` · installs (wheel) · licence: MIT License · rank 2516 · last release 2025-06-17 · [PyPI](https://pypi.org/project/azure-mgmt-appconfiguration/)

<details><summary>README extract</summary>

This is the Microsoft Azure App Configuration Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `ConfigurationStore` added property `default_key_value_revision_retention_period_in_seconds`
 - Model `ConfigurationStoreUpdateParameters` added property `default_key_value_revision_retention_period_in_seconds`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.appconfiguration import AppConfigurationManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-hdinsight

Microsoft Azure Hdinsight Management Client Library for Python

`pip install azure-mgmt-hdinsight` · installs (wheel) · licence: not stated · rank 2526 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-hdinsight/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure HDInsight Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `HDInsightManagementClient` added parameter `cloud_setting` in method `init`
 - Model `GatewaySettings` added property `rest_auth_entra_users`
 - Model `UpdateGatewaySettingsParameters` added property `rest_auth_entra_users`
 - Added model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.hdinsight import HDInsightManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-synapse

Microsoft Azure Synapse Management Client Library for Python

`pip install azure-mgmt-synapse` · installs (wheel) · licence: MIT License · rank 2559 · last release 2021-04-08 · [PyPI](https://pypi.org/project/azure-mgmt-synapse/)

<details><summary>README extract</summary>

This is the Microsoft Azure Synapse Management Client Library.
This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.
For a more complete view of Azure libraries, see the azure sdk python release

Sections: Microsoft Azure SDK for Python, Usage, Provide Feedback, 2.0.0 (2021-04-07), 1.0.0 (2021-03-10), 1.0.0b1 (2020-12-10), 0.5.0 (2020-11-23), 0.4.0 (2020-09-25), 0.3.0 (2020-06-17), 0.2.0 (2020-04-09), 0.1.0 (2020-02-27)

</details>

### aws-secretsmanager-caching

Client-side AWS Secrets Manager caching library

`pip install aws-secretsmanager-caching` · installs (wheel) · licence: Apache Software License · rank 2569 · last release 2026-09-23 · [PyPI](https://pypi.org/project/aws-secretsmanager-caching/)

<details><summary>README extract</summary>

The AWS Secrets Manager Python caching client enables in-process caching of secrets for Python applications.

Example:
```python
import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig() # See below for defaults
cache = SecretCache(config=cache_config, client=client)

secret = cache.get_secret_string('mysecret')
```

Sections: AWS Secrets Manager Python caching client, Getting Started, Required Prerequisites, Dependencies, Running Tests, Documentation, Usage, Forcing a Refresh, Cache Configuration, Decorators, Getting Help

</details>

### azure-mgmt-mysqlflexibleservers

Microsoft Azure Mysqlflexibleservers Management Client Library for Python

`pip install azure-mgmt-mysqlflexibleservers` · installs (wheel) · licence: not stated · rank 2581 · last release 2025-11-18 · [PyPI](https://pypi.org/project/azure-mgmt-mysqlflexibleservers/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Mysqlflexibleservers Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `MySQLManagementClient` added parameter `cloud_setting` in method `init`
 - Client `MySQLManagementClient` added operation group `private_endpoint_connections`
 - Client `MySQLManagementClient` added operation group `private_link_resources` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.mysqlflexibleservers import MySQLManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### arviz

Expose features from _ArviZverse_ refactored packages together in the ``arviz`` namespace.

`pip install arviz` · installs (wheel) · licence: Apache Software License · rank 2588 · last release 2026-08-11 · [PyPI](https://pypi.org/project/arviz/) · [docs](https://python.arviz.org) · [source](https://github.com/arviz-devs/arviz)

<details><summary>README extract</summary>

ArviZ (pronounced "AR-_vees") is a Python package for exploratory analysis of Bayesian models. It includes functions for posterior analysis, data storage, model checking, comparison and diagnostics.

ArviZ also has a Julia wrapper available ArviZ.jl.

The ArviZ documentation can be found in the official docs. ...

Sections: ArviZ in other languages, Documentation, Stable, Gallery, Institutional partners

</details>

### azure-mgmt-subscription

Microsoft Azure Subscription Management Client Library for Python

`pip install azure-mgmt-subscription` · installs (wheel) · licence: MIT License · rank 2592 · last release 2022-09-06 · [PyPI](https://pypi.org/project/azure-mgmt-subscription/)

<details><summary>README extract</summary>

This is the Microsoft Azure Subscription Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model AcceptOwnershipStatusResponse has a new parameter provisioning_state

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 3.1.1 (2022-09-05), Bugs Fixed, 3.1.0 (2022-08-30), Features Added, 3.0.0 (2022-01-21), 2.0.0 (2021-11-25), 1.0.0 (2020-12-16), 1.0.0b1 (2020-10-23), 0.7.0 (2020-10-12), 0.6.0 (2020-06-05)

</details>

### azure-mgmt-resource-deployments

Microsoft Azure Deployments Management Client Library for Python

`pip install azure-mgmt-resource-deployments` · installs (wheel) · licence: MIT · rank 2605 · last release 2026-09-10 · [PyPI](https://pypi.org/project/azure-mgmt-resource-deployments/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Deployments Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `DeploymentExtensionDefinition` added property `config_hash`
 - Model `DeploymentWhatIfProperties` added property `resource_predictions`
 - Model `ResourceReference` added property `symbolic_name_path`
 - Model `TargetResource` added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.deployments import DeploymentsMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-cli

Microsoft Azure Command-Line Tools

`pip install azure-cli` · installs (wheel) · licence: MIT · rank 2624 · last release 2026-11-03 · [PyPI](https://pypi.org/project/azure-cli/)

<details><summary>README extract</summary>

A great cloud needs great tools; we're excited to introduce *Azure CLI*, our next generation multi-platform command line experience for Azure.

Features:
Here are a few features and concepts that can help you get the most out of the Azure CLI.

The following examples are showing using the `--output table` format, you can change your default using the `$ az configure` command.

Sections: Microsoft Azure CLI, Usage, Getting Started, Highlights, Tab Completion, Querying, Creating a new Linux VM, More Samples and Snippets, Reporting issues and feedback

</details>

### azure-mgmt-redhatopenshift

Microsoft Azure Redhatopenshift Management Client Library for Python

`pip install azure-mgmt-redhatopenshift` · installs (wheel) · licence: MIT · rank 2633 · last release 2026-07-14 · [PyPI](https://pypi.org/project/azure-mgmt-redhatopenshift/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Red Hat Openshift Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `AzureRedHatOpenShiftClient` added method `send_request`
 - Added model `CloudError`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.redhatopenshift import AzureRedHatOpenShiftClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = AzureRedHatOpenShiftClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-cli-telemetry

Microsoft Azure CLI Telemetry Package

`pip install azure-cli-telemetry` · installs (wheel) · licence: MIT License · rank 2639 · last release 2023-08-01 · [PyPI](https://pypi.org/project/azure-cli-telemetry/)

<details><summary>README extract</summary>

This is the Microsoft Azure CLI Telemetry package. It is not intended to be installed directly by the end user.

This package includes:
1. Support API for Azure CLI to gather telemetry.
2. Telemetry upload process.

Sections: Microsoft Azure CLI Telemetry Package, 1.1.0, 1.0.8, 1.0.7, 1.0.6, 1.0.5, 1.0.4, 1.0.3, 1.0.2, 1.0.1, 1.0.0

</details>

### aws-psycopg2

A aws psycopg2 package from psycopg2.

`pip install aws-psycopg2` · installs (wheel) · licence: MIT License · rank 2640 · last release 2022-07-02 · [PyPI](https://pypi.org/project/aws-psycopg2/)

<details><summary>README extract</summary>

This is a custom compiled psycopg2 C library for Python. Due to AWS Lambda
missing the required PostgreSQL libraries in the AMI image, we needed to
compile psycopg2 with the PostgreSQL `libpq.so` library statically linked
libpq library instead of the default dynamic link.

</details>

### azure-mgmt-nspkg

Microsoft Azure Resource Management Namespace Package [Internal]

`pip install azure-mgmt-nspkg` · installs (wheel) · licence: MIT License · rank 2651 · last release 2018-10-02 · [PyPI](https://pypi.org/project/azure-mgmt-nspkg/)

<details><summary>README extract</summary>

This is the Microsoft Azure Management namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use PEP420 as namespace package strategy. ...

</details>

### azure-mgmt-netapp

Microsoft Azure Netapp Management Client Library for Python

`pip install azure-mgmt-netapp` · installs (wheel) · licence: MIT · rank 2652 · last release 2026-10-23 · [PyPI](https://pypi.org/project/azure-mgmt-netapp/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure NetApp Files Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `AccountProperties` added property `ldap_configuration`
 - Enum `NetAppProvisioningState` added member `CANCELED`
 - Added model `AccountEncryptionPatch`
 - Added model `AccountPropertiesPatch`
 - Added model `ActiveDirectoryPatch`
 - Added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.netapp import NetAppManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-sqlvirtualmachine

Microsoft Azure Sqlvirtualmachine Management Client Library for Python

`pip install azure-mgmt-sqlvirtualmachine` · installs (wheel) · licence: MIT · rank 2653 · last release 2026-07-20 · [PyPI](https://pypi.org/project/azure-mgmt-sqlvirtualmachine/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Sql Virtual Machine Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `SqlVirtualMachineManagementClient` added parameter `cloud_setting` in method `init`
 - Client `SqlVirtualMachineManagementClient` added method `send_request`
 - Model `AutoPatchingSettings` added property `additional_vm_patch`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.sqlvirtualmachine import SqlVirtualMachineManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### aws-opentelemetry-distro

AWS OpenTelemetry Python Distro

`pip install aws-opentelemetry-distro` · installs (wheel) · licence: Apache Software License · rank 2662 · last release 2026-10-30 · [PyPI](https://pypi.org/project/aws-opentelemetry-distro/)

<details><summary>README extract</summary>

Sections: AWS Distro For OpenTelemetry Python Distro, References

</details>

### azure-keyvault-administration

Microsoft Corporation Key Vault Administration Client Library for Python

`pip install azure-keyvault-administration` · installs (wheel) · licence: MIT License · rank 2664 · last release 2026-10-02 · [PyPI](https://pypi.org/project/azure-keyvault-administration/)

<details><summary>README extract</summary>

>Note: The Administration library only works with Managed HSM – functions targeting a Key Vault will fail.

Azure Key Vault helps solve the following problems:
- Vault administration (this library) - role-based access control (RBAC), and vault-level backup and restore options ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.administration import KeyVaultAccessControlClient

MANAGED_HSM_URL = os.environ["MANAGED_HSM_URL"]
credential = DefaultAzureCredential()
client = KeyVaultAccessControlClient(vault_url=MANAGED_HSM_URL, credential=credential)
```

...

</details>

### azure-mgmt-servicefabricmanagedclusters

Microsoft Azure Servicefabricmanagedclusters Management Client Library for Python

`pip install azure-mgmt-servicefabricmanagedclusters` · installs (wheel) · licence: not stated · rank 2690 · last release 2026-03-12 · [PyPI](https://pypi.org/project/azure-mgmt-servicefabricmanagedclusters/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Service Fabric Managed Clusters Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `ServiceFabricManagedClustersManagementClient` added parameter `cloud_setting` in method `init`
 - Client `ServiceFabricManagedClustersManagementClient` added method `send_request`
 - Enum `DiskType` added member `PREMIUM_V2_LRS`
 - Enum ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.servicefabricmanagedclusters import ServiceFabricManagedClustersManagementClient
import os

...

</details>

### azure-synapse-accesscontrol

Microsoft Azure Synapse AccessControl Client Library for Python

`pip install azure-synapse-accesscontrol` · installs (wheel) · licence: MIT License · rank 2698 · last release 2021-08-10 · [PyPI](https://pypi.org/project/azure-synapse-accesscontrol/)

<details><summary>README extract</summary>

This is the Microsoft Azure Synapse AccessControl Client Library.
This package has been tested with Python 2.7, 3.6, 3.7, 3.8 and 3.9.
For a more complete view of Azure libraries, see the azure sdk python release.

Sections: Microsoft Azure SDK for Python, Usage, Provide Feedback, 0.7.0 (2021-08-10), 0.6.0 (2021-03-09), 0.5.0 (2021-02-09), 0.4.0 (2020-12-08), 0.3.0 (2020-09-15), 0.2.0 (2020-07-01)

</details>

### azure-mgmt-imagebuilder

Microsoft Azure Imagebuilder Management Client Library for Python

`pip install azure-mgmt-imagebuilder` · installs (wheel) · licence: not stated · rank 2711 · last release 2026-06-02 · [PyPI](https://pypi.org/project/azure-mgmt-imagebuilder/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Image Builder Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ImageBuilderClient` added parameter `cloud_setting` in method `init`
 - Client `ImageBuilderClient` added method `send_request`
 - Model `ImageTemplatePropertiesOptimize` added property `workload`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.imagebuilder import ImageBuilderClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-botservice

Microsoft Azure Bot Service Client Library for Python

`pip install azure-mgmt-botservice` · installs (wheel) · licence: MIT License · rank 2713 · last release 2023-01-17 · [PyPI](https://pypi.org/project/azure-mgmt-botservice/)

<details><summary>README extract</summary>

This is the Microsoft Azure Bot Service Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation group EmailOperations
 - Added operation group OperationResultsOperations
 - Added operation group PrivateEndpointConnectionsOperations
 - Added operation group PrivateLinkResourcesOperations
 - Added operation group ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.botservice import AzureBotService
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-extendedlocation

Microsoft Azure Extended Location Management Client Library for Python

`pip install azure-mgmt-extendedlocation` · installs (wheel) · licence: MIT License · rank 2720 · last release 2024-10-30 · [PyPI](https://pypi.org/project/azure-mgmt-extendedlocation/)

<details><summary>README extract</summary>

This is the Microsoft Azure Extended Location Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.extendedlocation import CustomLocations
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = CustomLocations(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-synapse-managedprivateendpoints

Microsoft Azure Synapse Managed Private Endpoints Client Library for Python

`pip install azure-synapse-managedprivateendpoints` · installs (wheel) · licence: MIT License · rank 2722 · last release 2021-08-10 · [PyPI](https://pypi.org/project/azure-synapse-managedprivateendpoints/)

<details><summary>README extract</summary>

This is the Microsoft Azure Synapse Managed Private Endpoints Client Library.
This package has been tested with Python 2.7, 3.6, 3.7, 3.8 and 3.9.
For a more complete view of Azure libraries, see the azure sdk python release.

Sections: Microsoft Azure SDK for Python, Usage, Provide Feedback, 0.4.0 (2021-08-10), 0.3.0 (2021-03-09), 0.2.0 (2021-02-09), 0.1.0 (2020-12-08)

</details>

### azure-mgmt-servicelinker

Microsoft Azure Service Linker Management Client Library for Python

`pip install azure-mgmt-servicelinker` · installs (wheel) · licence: MIT License · rank 2726 · last release 2022-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-servicelinker/)

<details><summary>README extract</summary>

This is the Microsoft Azure Service Linker Management Client Library.
This package has been tested with Python 3.6+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 1.1.0 (2022-05-16), 1.0.0 (2022-04-22), 1.0.0b2 (2022-02-24), 1.0.0b1 (2021-09-28)

</details>

### appnope

Disable App Nap on macOS >= 10.9

`pip install appnope` · installs (wheel) · licence: BSD-2-Clause · rank 2733 · last release 2026-08-20 · [PyPI](https://pypi.org/project/appnope/) · [source](https://github.com/minrk/appnope)

<details><summary>README extract</summary>

Simple package for disabling App Nap on macOS >= 10.9,
which can be problematic.

To disable App Nap for the current process:

To reenable, for some reason:

or to only disable App Nap for a particular block:

It uses ctypes to wrap a `[NSProcessInfo beginActivityWithOptions]` call to disable App Nap.

To install:

 pip install appnope

Example:
```python
import appnope
appnope.nope()
```

</details>

### alembic_utils

A sqlalchemy/alembic extension for migrating procedures and views

`pip install alembic_utils` · installs (wheel) · licence: MIT License · rank 2797 · last release 2025-04-10 · [PyPI](https://pypi.org/project/alembic_utils/) · [source](https://github.com/olirice/alembic_utils)

<details><summary>README extract</summary>

Documentation:

Source Code:

Autogenerate Support for PostgreSQL Functions, Views, Materialized View, Triggers, and Policies

Alembic is the defacto migration tool for use with SQLAlchemy. Without extensions, alembic can detect local changes to SQLAlchemy models and autogenerate a database migration or "revision" script. ...

Example:
```python
# migrations/env.py
from alembic_utils.pg_function import PGFunction
from alembic_utils.replaceable_entity import register_entities

to_upper = PGFunction(
  schema='public',
  signature='to_upper(some_text text)',
  definition="""
  RETURNS text as
  $$
    SELECT upper(some_text)
  $$ language SQL;
  """
)

register_entities([to_upper])
```

Sections: Alembic Utils, TL;DR

</details>

### azure-mgmt-datalake-nspkg

Microsoft Azure Data Lake Management Namespace Package [Internal]

`pip install azure-mgmt-datalake-nspkg` · installs (wheel) · licence: MIT License · rank 2818 · last release 2018-10-17 · [PyPI](https://pypi.org/project/azure-mgmt-datalake-nspkg/)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Lake Management namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use PEP420 as namespace package strategy. ...

</details>

### anysqlite

(no summary)

`pip install anysqlite` · installs (wheel) · licence: not stated · rank 2823 · last release 2023-10-02 · [PyPI](https://pypi.org/project/anysqlite/) · [source](https://github.com/karosis88/anysqlite)

<details><summary>README extract</summary>

Anysqlite provides an `async/await` interface to the standard `sqlite3` library and supports both `trio` and `asyncio` backends using the power of Anyio.

Example:
```python
>>> import anysqlite
>>>
>>> conn = await anysqlite.connect(":memory:")
>>> cursor = await conn.execute("SELECT DATETIME()")
>>>
>>> response = await cursor.fetchone()
>>> print(response)
[('2023-10-02 13:42:42',)]
```

Sections: anysqlite, Basic usage

</details>

### aws-embedded-metrics

AWS Embedded Metrics Package

`pip install aws-embedded-metrics` · installs (wheel) · licence: Apache Software License · rank 2828 · last release 2026-03-27 · [PyPI](https://pypi.org/project/aws-embedded-metrics/)

<details><summary>README extract</summary>

Generate CloudWatch Metrics embedded within structured log events. The embedded metrics will be extracted so you can visualize and alarm on them for real-time incident detection. This allows you to monitor aggregated values while preserving the detailed event context that generated them.

- Use Cases
- Installation
- Usage
- API
- Examples ...

Example:
```python
from aws_embedded_metrics import metric_scope
from aws_embedded_metrics.storage_resolution import StorageResolution

@metric_scope
def my_handler(metrics):
    metrics.put_dimensions({"Foo": "Bar"})
    metrics.put_metric("ProcessingLatency", 100, "Milliseconds", StorageResolution.STANDARD)
...
```

Sections: aws-embedded-metrics, Use Cases, Usage, API, MetricsLogger, Configuration, Examples

</details>

### aioice

An implementation of Interactive Connectivity Establishment (RFC 5245)

`pip install aioice` · installs (wheel) · licence: BSD-3-Clause · rank 2831 · last release 2026-11-05 · [PyPI](https://pypi.org/project/aioice/) · [docs](https://aioice.readthedocs.io/)

<details><summary>README extract</summary>

`aioice` is a library for Interactive Connectivity Establishment (RFC 5245)
in Python. It is built on top of `asyncio`, Python's standard asynchronous
I/O framework.

Interactive Connectivity Establishment (ICE) is useful for applications that
establish peer-to-peer UDP data streams, as it facilitates NAT traversal. ...

Example:
```python
import asyncio
import aioice

async def connect_using_ice():
    connection = aioice.Connection(ice_controlling=True)

    # gather local candidates
    await connection.gather_candidates()

    # send your information to the remote party using your signaling method
    send_local_info(
        connection.local_candidates,
...
```

Sections: aioice, What is `aioice`?, Example

</details>

### aiortc

An implementation of WebRTC and ORTC

`pip install aiortc` · installs (wheel) · licence: BSD-3-Clause · rank 2838 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aiortc/) · [docs](https://aiortc.readthedocs.io/)

<details><summary>README extract</summary>

`aiortc` is a library for Web Real-Time Communication (WebRTC) and
Object Real-Time Communication (ORTC) in Python. It is built on top of
`asyncio`, Python's standard asynchronous I/O framework.

The API closely follows its Javascript counterpart while using pythonic
constructs:

- promises are replaced by coroutines ...

Features:
The main WebRTC and ORTC implementations are either built into web browsers,
or come in the form of native code. While they are extensively battle tested,
their internals are complex and they do not provide Python bindings. ...

Sections: What is `aiortc`?, Why should I use `aiortc`?

</details>

### azure-keyvault-securitydomain

Microsoft Corporation Azure Keyvault Securitydomain Client Library for Python

`pip install azure-keyvault-securitydomain` · installs (wheel) · licence: MIT · rank 2846 · last release 2026-10-02 · [PyPI](https://pypi.org/project/azure-keyvault-securitydomain/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Features:
- Added support for service API version `2025-07-01` #46782

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.securitydomain import SecurityDomainClient

VAULT_URL = os.environ["VAULT_URL"]
credential = DefaultAzureCredential()
client = SecurityDomainClient(vault_url=VAULT_URL, credential=credential)
```

Sections: Getting started, Prequisites, Authenticate the client, Create a client, Key concepts, Download operation, Upload operation, Transfer key, Examples, Get a transfer key, Troubleshooting, Next steps, 1.0.0b4 (2026-10-02), Bugs Fixed

</details>

### azure-monitor-ingestion

Microsoft Azure Monitor Ingestion Client Library for Python

`pip install azure-monitor-ingestion` · installs (wheel) · licence: MIT License · rank 2854 · last release 2025-07-18 · [PyPI](https://pypi.org/project/azure-monitor-ingestion/)

<details><summary>README extract</summary>

The Azure Monitor Ingestion client library is used to send custom logs to Azure Monitor using the Logs Ingestion API.

This library allows you to send data from virtually any source to supported built-in tables or to custom tables that you create in Log Analytics workspace. You can even extend the schema of built-in tables with custom columns. ...

Features:
- Added new `on_error` parameter to the `upload` method to allow users to handle errors in their own way.
 - An `LogsUploadError` class was added to encapsulate information about the error. ...

Example:
```python
import os
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient

endpoint = os.environ['DATA_COLLECTION_ENDPOINT']
credential = DefaultAzureCredential()
...

</details>

### azure-mgmt-resource-deploymentstacks

Microsoft Azure Deploymentstacks Management Client Library for Python

`pip install azure-mgmt-resource-deploymentstacks` · installs (wheel) · licence: not stated · rank 2863 · last release 2026-02-10 · [PyPI](https://pypi.org/project/azure-mgmt-resource-deploymentstacks/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Deploymentstacks Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `DeploymentStacksClient` added parameter `cloud_setting` in method `init`
 - Client `DeploymentStacksClient` added method `send_request`
 - Client `DeploymentStacksClient` added operation group ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.deploymentstacks import DeploymentStacksClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-resource-templatespecs

Microsoft Azure Templatespecs Management Client Library for Python

`pip install azure-mgmt-resource-templatespecs` · installs (wheel) · licence: MIT · rank 2937 · last release 2026-09-29 · [PyPI](https://pypi.org/project/azure-mgmt-resource-templatespecs/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Templatespecs Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `TemplateSpecsClient` added parameter `cloud_setting` in method `init`
 - Operation group `TemplateSpecVersionsOperations` added method `get_built_in`
 - Operation group `TemplateSpecVersionsOperations` added method `list_built_ins`
 - ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.templatespecs import TemplateSpecsClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-resource-deploymentscripts

Microsoft Azure Resource Deploymentscripts Management Client Library for Python

`pip install azure-mgmt-resource-deploymentscripts` · installs (wheel) · licence: MIT License · rank 2939 · last release 2025-06-10 · [PyPI](https://pypi.org/project/azure-mgmt-resource-deploymentscripts/)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Deploymentscripts Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.deploymentscripts import DeploymentScriptsClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = DeploymentScriptsClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### avro-gen3

Avro record class and specific record reader generator

`pip install avro-gen3` · installs (wheel) · licence: Apache Software License · rank 2955 · last release 2024-09-05 · [PyPI](https://pypi.org/project/avro-gen3/)

<details><summary>README extract</summary>

Current Avro implementation in Python is completely typelss and operates on dicts.
While in many cases this is convenient and pythonic, not being able to discover the schema
by looking at the code, not enforcing schema during record constructions, and not having any
context help from the IDE could hamper developer performance and introduce bugs. ...

Sections: AVRO-GEN, Avro record class and specific record reader generator., Usage

</details>

### azure-mgmt-resourcegraph

Microsoft Azure Resourcegraph Management Client Library for Python

`pip install azure-mgmt-resourcegraph` · installs (wheel) · licence: not stated · rank 2983 · last release 2025-11-24 · [PyPI](https://pypi.org/project/azure-mgmt-resourcegraph/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Graph Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model QueryRequestOptions has a new parameter authorization_scope_filter
 - Model ResourcesHistoryRequest has a new parameter management_groups

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 8.0.1 (2025-11-24), Other Changes, 8.1.0b3 (2022-12-26), Features Added, Breaking Changes, 8.1.0b2 (2022-08-30), 8.1.0b1 (2021-04-25), 8.0.0 (2021-03-31), 7.0.0 (2020-12-15)

</details>

### aws-lambda-typing

A package that provides type hints for AWS Lambda event, context and response objects

`pip install aws-lambda-typing` · installs (wheel) · licence: MIT License · rank 2984 · last release 2024-04-02 · [PyPI](https://pypi.org/project/aws-lambda-typing/) · [source](https://github.com/MousaZeidBaker/aws-lambda-typing)

<details><summary>README extract</summary>

A package that provides type hints for AWS Lambda event, context and response
objects. It's a convenient way to get autocomplete and type hints built into
IDEs. Type annotations are not checked at runtime but are only enforced by third
party tools such as type checkers, IDEs, linters, etc.

Example:
```python
from aws_lambda_typing import context as context, events

def handler(event: events.SQSEvent, context: context.Context) -> None:
    for record in event['Records']:
        print(record['body'])

    print(context.get_remaining_time_in_millis())

    message: events.sqs.SQSMessage
```

Sections: AWS Lambda Typing, Usage, Example: AWS SQS event, Demo, IDE code reference information, Types, Context, Events, Requests, Responses, Other, Issues

</details>

### aiocsv

(no summary)

`pip install aiocsv` · installs (wheel) · licence: MIT License · rank 3004 · last release 2026-10-30 · [PyPI](https://pypi.org/project/aiocsv/)

<details><summary>README extract</summary>

Asynchronous CSV reading and writing.

Example:
```python
import asyncio
import csv

import aiofiles
from aiocsv import AsyncReader, AsyncDictReader, AsyncWriter, AsyncDictWriter

async def main():
    # simple reading
    async with aiofiles.open("some_file.csv", mode="r", encoding="utf-8", newline="") as afp:
        async for row in AsyncReader(afp):
            print(row)  # row is a list

...
```

Sections: aiocsv, Usage, Example, Differences with `csv`, Reference, aiocsv.AsyncReader, aiocsv.AsyncDictReader, aiocsv.AsyncWriter, aiocsv.AsyncDictWriter, Building from source, Tests, Linting & other tools, Recommended VS Code settings

</details>

### azure-mgmt-dns

Microsoft Azure DNS Management Client Library for Python

`pip install azure-mgmt-dns` · installs (wheel) · licence: MIT License · rank 3065 · last release 2025-07-14 · [PyPI](https://pypi.org/project/azure-mgmt-dns/)

<details><summary>README extract</summary>

This is the Microsoft Azure DNS Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model RecordSet has a new parameter traffic_management_profile

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.dns import DnsManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = DnsManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### arize-phoenix-otel

LLM Observability

`pip install arize-phoenix-otel` · installs (wheel) · licence: Apache-2.0 · rank 3071 · last release 2026-11-06 · [PyPI](https://pypi.org/project/arize-phoenix-otel/) · [docs](https://arize.com/docs/phoenix/) · [source](https://github.com/Arize-ai/phoenix)

<details><summary>README extract</summary>

arize-phoenix-otel

Provides a lightweight wrapper around OpenTelemetry primitives with Phoenix-aware defaults. Phoenix OTEL also gives you access to tracing decorators for common GenAI patterns.

Features:
`arize-phoenix-otel` simplifies OpenTelemetry configuration for Phoenix users by providing:

- Phoenix-aware defaults for common OpenTelemetry primitives
- Automatic configuration from environment variables ...

Example:
```python
from phoenix.otel import register

# Recommended: Automatic instrumentation + production settings
tracer_provider = register(
    auto_instrument=True,  # Auto-trace OpenAI, LangChain, LlamaIndex, etc.
    batch=True,  # Production-ready batching
    project_name="my-app",  # Organize your traces
)
```

...

</details>

### astronomer-cosmos

Orchestrate your dbt projects in Airflow

`pip install astronomer-cosmos` · installs (wheel) · licence: Apache-2.0 · rank 3103 · last release 2026-11-03 · [PyPI](https://pypi.org/project/astronomer-cosmos/) · [docs](https://astronomer.github.io/astronomer-cosmos) · [source](https://github.com/astronomer/astronomer-cosmos)

<details><summary>README extract</summary>

Run your dbt Core projects as Apache Airflow® DAGs and Task Groups with a few lines of code. Benefits include:

- Run dbt projects against Airflow connections instead of dbt profiles
- Native support for installing and running dbt in a virtual environment to avoid dependency conflicts with Airflow ...

</details>

### array-record

A file format that achieves a new frontier of IO efficiency

`pip install array-record` · installs (wheel) · licence: Apache-2.0 · rank 3116 · last release 2026-10-20 · [PyPI](https://pypi.org/project/array-record/)

### argparse-addons

Additional argparse types and actions.

`pip install argparse-addons` · installs (wheel) · licence: MIT License · rank 3152 · last release 2023-01-29 · [PyPI](https://pypi.org/project/argparse-addons/)

<details><summary>README extract</summary>

Additional Python argparse types and actions.

Project homepage:

Example:
```python
parser.add_argument('--min-max',
                    type=argparse_addons.Integer(0, 255))
parser.add_argument('--min',
                    type=argparse_addons.Integer(0, None))
parser.add_argument('--max',
                    type=argparse_addons.Integer(None, 255))
parser.add_argument('--any',
                    type=argparse_addons.Integer())
```

Sections: About, Examples, Integer type, . Fork the repository., . Implement the new feature or bug fix., . Run the tests., . Create a pull request.

</details>

### azure-mgmt-containerregistrytasks

Microsoft Azure Containerregistrytasks Management Client Library for Python

`pip install azure-mgmt-containerregistrytasks` · installs (wheel) · licence: not stated · rank 3156 · last release 2026-03-16 · [PyPI](https://pypi.org/project/azure-mgmt-containerregistrytasks/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Containerregistrytasks Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ContainerRegistryTasksMgmtClient` added method `send_request`
 - Model `AgentPoolUpdateParameters` added property `properties`
 - Model `TaskRunUpdateParameters` added property `properties`
 - Model `TaskUpdateParameters` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistrytasks import ContainerRegistryTasksMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### airportsdata

Extensive database of location and timezone data for nearly every airport and landing strip in the world.

`pip install airportsdata` · installs (wheel) · licence: MIT · rank 3169 · last release 2026-11-03 · [PyPI](https://pypi.org/project/airportsdata/) · [docs](https://github.com/mborsetti/airportsdata/blob/main/README.rst) · [source](https://github.com/mborsetti/airportsdata/)

<details><summary>README extract</summary>

Extensive database of location and timezone data for nearly every operational airport, landing strip, and some seaplane
bases in the world (no heliports unless IATA coded), with entries.

Each entry consists of the following data: ...

Example:
```python
import airportsdata
icao_airports = airportsdata.load()  # key is the ICAO identifier (the default)
print(icao_airports['KJFK'])
```

Sections: airportsdata, Raw data, Python

</details>

### app-store-server-library

The App Store Server Library

`pip install app-store-server-library` · installs (wheel) · licence: MIT License · rank 3245 · last release 2026-06-01 · [PyPI](https://pypi.org/project/app-store-server-library/)

<details><summary>README extract</summary>

The Python server library for the App Store Server API, App Store Server Notifications, Retention Messaging API, and Advanced Commerce API. Also available in Swift, Node.js, and Java.

Example:
```python
from appstoreserverlibrary.api_client import AppStoreServerAPIClient, APIException
from appstoreserverlibrary.models.Environment import Environment

private_key = read_private_key("/path/to/key/SubscriptionKey_ABCDEFGHIJ.p8") # Implementation will vary

key_id = "ABCDEFGHIJ"
issuer_id = "99b16628-15e4-4668-972b-eeff55eeff55"
...
```

...

</details>

### analytics-python

The hassle-free way to integrate analytics into any python application.

`pip install analytics-python` · installs (wheel) · licence: MIT License · rank 3246 · last release 2023-03-22 · [PyPI](https://pypi.org/project/analytics-python/)

<details><summary>README extract</summary>

This library was renamed due to a naming conflict with an official python library.
Please use the new listing at

Segment is the simplest way to integrate analytics into your application.
One API allows you to turn on any other analytics service. No more learning
new APIs, repeated code, and wasted development time. ...

</details>

### anybadge

Simple, flexible badge generator for project badges.

`pip install anybadge` · installs (wheel) · licence: MIT License · rank 3251 · last release 2026-11-08 · [PyPI](https://pypi.org/project/anybadge/)

<details><summary>README extract</summary>

Features:
`anybadge` can be used to add badge generation to your Python projects,
and also provides a command line interface.

This utility can be used to generate .svg badge images, using configurable
thresholds for coloring the badges based on the badge ...

Example:
```python
from anybadge import badge
help(badge)
```

Sections: Overview, Demo, Basic usage, Command line, Python, Getting help, Command line usage, Output, Thresholds, Built-in templates, Colors, Emojis, Logos, Using logos in network-gated environments

</details>

### azure-cosmosdb-table

Microsoft Azure CosmosDB Table Client Library for Python

`pip install azure-cosmosdb-table` · installs (wheel) · licence: Apache Software License · rank 3255 · last release 2019-10-25 · [PyPI](https://pypi.org/project/azure-cosmosdb-table/)

<details><summary>README extract</summary>

This project provides a client library in Python that makes it easy to
consume Microsoft Azure CosmosDB Table services. For documentation please see
the Microsoft Azure Python Developer Center and our API Reference Page.

 If you are looking for the Service Bus or Azure Management
 libraries, please visit ...

Features:
- Table

 - Create/Read/Update/Delete Tables
 - Create/Read/Update/Delete Entities
 - Batch operations
 - Advanced Table Operations

Sections: Microsoft Azure CosmosDB Table SDK for Python, Compatibility, Features, Getting Started, Download, Option 1: Via PyPi, Option 2: Source Via Git, Option 3: Source Zip, Minimum Requirements, Usage, Code Sample, Need Help?, Learn More

</details>

### azure-cosmosdb-nspkg

Microsoft Azure CosmosDB Namespace Package [Internal]

`pip install azure-cosmosdb-nspkg` · installs (wheel) · licence: Apache Software License · rank 3282 · last release 2017-10-05 · [PyPI](https://pypi.org/project/azure-cosmosdb-nspkg/)

<details><summary>README extract</summary>

This is the Microsoft Azure CosmosDB namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.cosmosdb namespace.

If you are looking to install the Azure CosmosDB libraries, see the
azure bundle package.

</details>

### azure-mgmt-domainregistration

Microsoft Azure Domainregistration Management Client Library for Python

`pip install azure-mgmt-domainregistration` · installs (wheel) · licence: MIT · rank 3339 · last release 2026-06-30 · [PyPI](https://pypi.org/project/azure-mgmt-domainregistration/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Domainregistration Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.domainregistration import DomainRegistrationMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = DomainRegistrationMgmtClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-storage-file

Microsoft Azure Storage File Client Library for Python

`pip install azure-storage-file` · installs (wheel) · licence: MIT License · rank 3357 · last release 2019-08-02 · [PyPI](https://pypi.org/project/azure-storage-file/)

<details><summary>README extract</summary>

This project provides a client library in Python that makes it easy to
consume Microsoft Azure Storage services. For documentation please see
the Microsoft Azure Python Developer Center and our API Reference (also available on readthedocs).

 If you are looking for the Service Bus or Azure Management
 libraries, please visit ...

Features:
- Blob

 - Create/Read/Update/Delete Containers
 - Create/Read/Update/Delete Blobs
 - Advanced Blob Operations

- Queue

 - Create/Delete Queues
 - Insert/Peek Queue Messages
 - Advanced Queue Operations

- Files ...

Example:
```python
# Basic configuration: configure the root logger, including 'azure.storage'
logging.basicConfig(format='%(asctime)s %(name)-20s %(levelname)-5s %(message)s', level=logging.INFO)
```

...

</details>

### androguard

Androguard is a full python tool to play with Android files.

`pip install androguard` · installs (wheel) · licence: Other/Proprietary License · rank 3375 · last release 2026-06-01 · [PyPI](https://pypi.org/project/androguard/)

<details><summary>README extract</summary>

Do you think your phone has been pwned ? please check IsMyPhonePwned

New tool: Goauld Dynamic injection tool for Linux/Android

See the new version of Androguard:

Features:
Androguard is a full python tool to play with Android files.

* DEX, ODEX
* APK
* Android's binary xml
* Android resources
* Disassemble DEX/ODEX bytecodes
* Basic Decompiler for DEX/ODEX files
* Frida support for easy dynamic analysis
* SQLite ...

Sections: Androguard, Documentation, Features, Projects using Androguard, DAD

</details>

### astral

Calculations for the position of the sun and moon.

`pip install astral` · installs (wheel) · licence: Apache Software License · rank 3384 · last release 2022-11-05 · [PyPI](https://pypi.org/project/astral/) · [docs](https://sffjunkie.github.io/astral) · [source](https://github.com/sffjunkie/astral)

<details><summary>README extract</summary>

This is 'astral' a Python module which calculates

- Times for various positions of the sun: dawn, sunrise, solar noon,
sunset, dusk, solar elevation, solar azimuth and rahukaalam.
- Moon rise, set, azimuth and zenith.
- The phase of the moon.

For documentation see

</details>

### apkInspector

apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file.

`pip install apkInspector` · installs (wheel) · licence: Apache Software License · rank 3395 · last release 2026-08-28 · [PyPI](https://pypi.org/project/apkInspector/) · [source](https://github.com/erev0s/apkInspector)

<details><summary>README extract</summary>

apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file. What sets APKInspector apart is its adherence to the zip specification during APK parsing, eliminating the need for reliance on external libraries. ...

Features:
- Find end of central directory record
 - Parse central directory of APK and get details about each entry
 - Get details local header for each entry
 - Extract single or all files within an APK
 - Decode AndroidManifest.xml file ...

Sections: apkInspector, Documentation, CLI, Library, Features offered, Reliability, Planned to-do, rocket: apkInspector is being used by :rocket:, Presentation of the tool and the research behind it, Disclaimer

</details>

### azure-ai-contentunderstanding

Microsoft Corporation Azure AI Content Understanding Client Library for Python

`pip install azure-ai-contentunderstanding` · installs (wheel) · licence: not stated · rank 3402 · last release 2026-04-20 · [PyPI](https://pypi.org/project/azure-ai-contentunderstanding/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure AI Content Understanding is a multimodal AI service that extracts semantic content from documents, video, audio, and image files. It transforms unstructured content into structured, machine-readable data optimized for retrieval-augmented generation (RAG) and automated workflows.

Use the client library for Azure AI Content Understanding to: ...

Features:
- Added `usage` property on `AnalyzeLROPoller` and `AnalyzeAsyncLROPoller` to surface billing and token consumption details (`UsageDetails`) returned by the REST API.

Example:
```python
import os
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.identity import DefaultAzureCredential

endpoint = os.environ["CONTENTUNDERSTANDING_ENDPOINT"]
credential = DefaultAzureCredential()
...

</details>

### aiodocker

A simple Docker HTTP API wrapper written with asyncio and aiohttp.

`pip install aiodocker` · installs (wheel) · licence: Apache 2.0 · rank 3437 · last release 2026-05-27 · [PyPI](https://pypi.org/project/aiodocker/)

<details><summary>README extract</summary>

A simple Docker HTTP API wrapper written with asyncio and aiohttp.

Example:
```python
import asyncio
import aiodocker

async def list_things(docker):
    print('== Images ==')
    for image in (await docker.images.list()):
        tags = image'RepoTags' if image['RepoTags'] else ''
        print(image['Id'], tags)
    print('== Containers ==')
    for container in (await docker.containers.list()):
        print(f" {container._id}")
...
```

Sections: AsyncIO bindings for docker.io, Using pip instead (fallback), Running tests, Building packages, Documentation, Examples

</details>

### azure-ai-formrecognizer

Microsoft Azure Form Recognizer Client Library for Python

`pip install azure-ai-formrecognizer` · installs (wheel) · licence: MIT License · rank 3583 · last release 2024-04-09 · [PyPI](https://pypi.org/project/azure-ai-formrecognizer/)

<details><summary>README extract</summary>

Azure Document Intelligence (previously known as Form Recognizer) is a cloud service that uses machine learning to analyze text and structured data from your documents. It includes the following main features:

- Layout - Extract content and structure (ex. words, selection marks, tables) from documents. ...

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

endpoint = "
credential = AzureKeyCredential("<api_key>")
document_analysis_client = DocumentAnalysisClient(endpoint, credential)
```

...

</details>

### aiomqtt

The idiomatic asyncio MQTT client

`pip install aiomqtt` · installs (wheel) · licence: BSD License · rank 3593 · last release 2026-03-05 · [PyPI](https://pypi.org/project/aiomqtt/) · [docs](https://aiomqtt.bo3hm.com) · [source](https://github.com/empicano/aiomqtt)

<details><summary>README extract</summary>

Documentation:

Write code like this:

Publish

Subscribe

Features:
- No more callbacks! 👍
- No more return codes (welcome to the `MqttError`)
- Graceful disconnection (forget about `on_unsubscribe`, `on_disconnect`, etc.)
- Supports MQTT versions 5.0, 3.1.1 and 3.1
- Fully type-hinted ...

Example:
```python
async with Client("test.mosquitto.org") as client:
    await client.publish("temperature/outside", payload=28.4)
```

Sections: The idiomatic asyncio MQTT client 🙌, Key features, Note for Windows users, Versioning

</details>

### azure-mgmt-devtestlabs

Microsoft Azure Devtestlabs Management Client Library for Python

`pip install azure-mgmt-devtestlabs` · installs (wheel) · licence: not stated · rank 3609 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-devtestlabs/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Dev Test Labs Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model Disk has a new parameter storage_account_id

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.devtestlabs import DevTestLabsClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = DevTestLabsClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### agent-framework-core

Microsoft Agent Framework for building AI Agents with Python. This is the core package that has all the core abstractions and implementations.

`pip install agent-framework-core` · installs (wheel) · licence: MIT License · rank 3611 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-core/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

Highlights

- Flexible Agent Framework: build, orchestrate, and deploy AI agents and multi-agent systems
- Multi-Agent Orchestration: Group chat, sequential, concurrent, and handoff patterns
- Plugin Ecosystem: Extend with native functions, OpenAPI, Model Context Protocol (MCP), and more
- LLM Support: OpenAI, Foundry, Anthropic, and more ...

Example:
```python
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    api_key="",
    model="",
)
```

...

</details>

### asteroid-filterbanks

Asteroid's filterbanks

`pip install asteroid-filterbanks` · installs (wheel) · licence: MIT License · rank 3627 · last release 2021-04-09 · [PyPI](https://pypi.org/project/asteroid-filterbanks/)

<details><summary>README extract</summary>

[][codecov]

[][slack-invite]

Sections: Asteroid Filterbanks., Citing Asteroid

</details>

### azure-mgmt-logic

Microsoft Azure Logic Apps Management Client Library for Python

`pip install azure-mgmt-logic` · installs (wheel) · licence: MIT License · rank 3650 · last release 2022-06-13 · [PyPI](https://pypi.org/project/azure-mgmt-logic/)

<details><summary>README extract</summary>

This is the Microsoft Azure Logic Apps Management Client Library.
This package has been tested with Python 3.6+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 10.0.0 (2022-06-06), 9.0.0 (2020-12-18), 9.0.0b1 (2020-10-31), 4.0.0rc2 (2019-01-11), 4.0.0rc1 (2018-12-10), 3.0.0 (2018-05-18), 2.1.0 (2017-04-18), 2.0.0 (2017-03-16), 1.0.0 (2016-08-30)

</details>

### azure-mgmt-datalake-analytics

Microsoft Azure Data Lake Analytics Management Client Library for Python

`pip install azure-mgmt-datalake-analytics` · installs (wheel) · licence: MIT License · rank 3682 · last release 2018-06-26 · [PyPI](https://pypi.org/project/azure-mgmt-datalake-analytics/)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Lake Analytics Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6. ...

Sections: Microsoft Azure SDK for Python, Compatibility, Usage, Provide Feedback, 0.6.0 (2018-06-15), 0.5.0 (2018-06-14), 0.4.0 (2018-02-12), 0.3.0 (2018-01-09), 0.2.0 (2017-08-17), 0.1.6 (2017-06-19), 0.1.5 (2017-06-07), 0.1.4 (2017-04-20), 0.1.3 (2017-02-13), 0.1.2 (2017-01-09)

</details>

### actionlint-py

Python wrapper around invoking actionlint (https://github.com/rhysd/actionlint)

`pip install actionlint-py` · installs from source (sdist only) · licence: MIT License · rank 3712 · last release 2026-09-22 · [PyPI](https://pypi.org/project/actionlint-py/)

<details><summary>README extract</summary>

> Note: for `pre-commit` hooks I recommend officially supported hooks:
> See docs:

A python wrapper to provide a pip-installable [actionlint] binary.

Internally this package provides a convenient way to download the pre-built
actionlint binary for your particular platform.

Sections: actionlint-py, Usage, As a pre-commit hook, Alternative methods of running actionlint, As pre-commit hooks, Use as github action step, Roadmap

</details>

### asyncmy

The fastest asyncio MySQL/MariaDB driver for Python

`pip install asyncmy` · installs (wheel) · licence: Apache-2.0 · rank 3725 · last release 2026-11-07 · [PyPI](https://pypi.org/project/asyncmy/) · [docs](https://github.com/long2ice/asyncmy) · [source](https://github.com/long2ice/asyncmy.git)

<details><summary>README extract</summary>

`asyncmy` is the fastest asyncio MySQL/MariaDB driver for Python. It keeps the familiar aiomysql API while rewriting the entire protocol core in Cython — down to pointer-level packet parsing. See our benchmarks for Python-driver and Go/Rust comparisons, including their measured settings and results.

Features:
- 🚀 Fast Python queries — large-result fetching takes about half mysqlclient's time; pooled queries deliver 3.6× aiomysql's throughput in the local benchmark ...

Example:
```python
import asyncio
import os

from asyncmy import connect
from asyncmy.cursors import DictCursor

async def main():
    conn = await connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD", ""),
    )
    async with conn.cursor(cursor=DictCursor) as cursor:
...

</details>

### azure-mgmt-reservations

Microsoft Azure Reservations Management Client Library for Python

`pip install azure-mgmt-reservations` · installs (wheel) · licence: MIT · rank 3730 · last release 2026-07-30 · [PyPI](https://pypi.org/project/azure-mgmt-reservations/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Reservations Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `CurrentQuotaLimitBase` added property `system_data`
 - Model `QuotaRequestDetails` added property `system_data`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.reservations import ReservationsMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = ReservationsMgmtClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-recoveryservicesbackup-passivestamp

Microsoft Azure Passivestamp Management Client Library for Python

`pip install azure-mgmt-recoveryservicesbackup-passivestamp` · installs (wheel) · licence: not stated · rank 3746 · last release 2025-10-15 · [PyPI](https://pypi.org/project/azure-mgmt-recoveryservicesbackup-passivestamp/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Recoveryservicesbackup Passivestamp Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicesbackup.passivestamp import RecoveryServicesBackupPassiveClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = RecoveryServicesBackupPassiveClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-consumption

Microsoft Azure Consumption Management Client Library for Python

`pip install azure-mgmt-consumption` · installs (wheel) · licence: MIT · rank 3813 · last release 2026-07-20 · [PyPI](https://pypi.org/project/azure-mgmt-consumption/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Consumption Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ConsumptionManagementClient` added parameter `cloud_setting` in method `init`
 - Client `ConsumptionManagementClient` added parameter `polling_interval` in method `init`
 - Client `ConsumptionManagementClient` added method `send_request` ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.consumption import ConsumptionManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### asyncache

Helpers to use cachetools with async code.

`pip install asyncache` · installs (wheel) · licence: MIT License · rank 3819 · last release 2022-11-15 · [PyPI](https://pypi.org/project/asyncache/)

<details><summary>README extract</summary>

Helpers to use cachetools with asyncio.

Example:
```python
from asyncache import cached
from cachetools import TTLCache

pool = ...

@cached(TTLCache(1024, 60))
async def get_username(user_id):
    rec = await pool.fetchrow(
        """
        SELECT
            username
        FROM
            users
        WHERE
            id = $1
        """,
        user_id,
    )
    return rec and rec["username"]
```

Sections: asyncache, Example

</details>

### apache-sedona

Apache Sedona is a cluster computing system for processing large-scale spatial data

`pip install apache-sedona` · installs (wheel) · licence: Apache Software License · rank 3847 · last release 2026-08-05 · [PyPI](https://pypi.org/project/apache-sedona/) · [docs](https://sedona.apache.org) · [source](https://github.com/apache/sedona)

<details><summary>README extract</summary>

This library is the Python wrapper for Apache Sedona.

Apache Sedona is a cluster computing system for processing large-scale spatial data.
Apache Sedona extends Apache Spark / SparkSQL with a set of out-of-the-box Spatial Resilient Distributed Datasets (SRDDs)/ SpatialSQL that efficiently load, process, and analyze large-scale spatial data across ...

</details>

### awsume

Awsume - A cli that makes using AWS IAM credentials easy

`pip install awsume` · installs (wheel) · licence: MIT · rank 3848 · last release 2024-01-05 · [PyPI](https://pypi.org/project/awsume/)

### authzed

Client library for SpiceDB.

`pip install authzed` · installs (wheel) · licence: Apache-2.0 · rank 3851 · last release 2026-07-14 · [PyPI](https://pypi.org/project/authzed/)

<details><summary>README extract</summary>

This repository houses the Python client library for Authzed.

[Authzed] is a database and service that stores, computes, and validates your application's permissions.

Developers create a schema that models their permissions requirements and use a client library, such as this one, to apply the schema to the database, insert data into the ...

Example:
```python
from authzed.api.v1 import InsecureClient

client = InsecureClient(
    "spicedb:50051",
    "my super secret token"
)
```

Sections: Authzed Python Client, Getting Started, Basic Usage, Initializing a client, Performing an API call, Insecure Client Usage, Materialize API

</details>

### amazon-transcribe

Async Python SDK for Amazon Transcribe Streaming

`pip install amazon-transcribe` · installs (wheel) · licence: Apache Software License · rank 3877 · last release 2025-05-05 · [PyPI](https://pypi.org/project/amazon-transcribe/)

<details><summary>README extract</summary>

The Amazon Transcribe Streaming SDK allows users to directly interface with
the Amazon Transcribe Streaming service and their Python programs. The goal of
the project is to enable users to integrate directly with Amazon Transcribe
without needing anything more than a stream of audio bytes and a basic handler. ...

Example:
```python
import asyncio

# This example uses aiofile for asynchronous file reads.
# It's not a dependency of the project but can be installed
# with `pip install aiofile`.
import aiofile

from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
...
```

Sections: Amazon Transcribe Streaming SDK, Usage, Prerequisites, Quick Start

</details>

### azure-mgmt-notificationhubs

Microsoft Azure Notification Hubs Management Client Library for Python

`pip install azure-mgmt-notificationhubs` · installs (wheel) · licence: MIT License · rank 3886 · last release 2022-01-06 · [PyPI](https://pypi.org/project/azure-mgmt-notificationhubs/)

<details><summary>README extract</summary>

This is the Microsoft Azure Notification Hubs Management Client Library.
This package has been tested with Python 2.7, 3.6+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 8.0.0 (2022-01-06), 7.0.0 (2020-12-22), 7.0.0b1 (2020-10-28), 2.1.0 (2019-04-30), 2.0.0 (2018-05-25), 1.0.0 (2017-06-27), 0.30.0 (2016-10-05)

</details>

### austin-dist

Austin - Frame Stack Sampler for CPython

`pip install austin-dist` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 3900 · last release 2026-10-27 · [PyPI](https://pypi.org/project/austin-dist/) · [docs](https://github.com/P403n1x87/austin/blob/master/README.md) · [source](https://github.com/P403n1x87/austin)

_README extract left out: share-alike licence._

### arize-phoenix-client

LLM Observability

`pip install arize-phoenix-client` · installs (wheel) · licence: Apache-2.0 · rank 3910 · last release 2026-11-05 · [PyPI](https://pypi.org/project/arize-phoenix-client/) · [docs](https://arize.com/docs/phoenix/) · [source](https://github.com/Arize-ai/phoenix)

<details><summary>README extract</summary>

arize-phoenix-client

Phoenix Client provides an interface for interacting with the Phoenix platform via its REST API, enabling you to manage datasets, run experiments, analyze traces, and collect feedback programmatically.

Features:
- REST API Interface - Interact with Phoenix's OpenAPI REST interface
- Prompts - Create, version, and invoke prompt templates
- Datasets - Create and append to datasets from DataFrames, CSV files, or dictionaries ...

Example:
```python
from phoenix.client import Client, AsyncClient

# Automatic configuration from environment variables
client = Client()

client = Client(base_url="  # Local Phoenix server

# Remote instance with API key
client = Client(base_url=" api_key="your-api-key")

# Custom authentication headers
client = Client(
...
```

...

</details>

### asciitree

Draws ASCII trees.

`pip install asciitree` · installs (wheel) · licence: MIT · rank 3915 · last release 2026-10-25 · [PyPI](https://pypi.org/project/asciitree/) · [docs](https://asciitree.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Since Python 3.7, dictionaries preserve insertion order. On older versions, use
`collections.OrderedDict` to preserve the tree's display order.

For Python 2, use `asciitree<0.4`. Version 0.4.0 preserves the API and rendering
behavior but supports Python 3 only.

Read the documentation at <

Example:
```python
from asciitree import LeftAligned

tree = {
    "asciitree": {
        "sometimes": {"you": {}},
        "just": {"want": {"to": {}, "draw": {}}},
        "trees": {},
        "in": {"your": {"terminal": {}}},
    }
}

tr = LeftAligned()
print(tr(tree))
```

</details>

### adbc-driver-postgresql

A libpq-based ADBC driver for working with PostgreSQL.

`pip install adbc-driver-postgresql` · installs (wheel) · licence: Apache-2.0 · rank 3920 · last release 2026-10-26 · [PyPI](https://pypi.org/project/adbc-driver-postgresql/) · [source](https://github.com/apache/arrow-adbc)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Example:
```python
import adbc_driver_postgresql.dbapi

uri = "postgresql://postgres:password@localhost:5432/postgres"
with adbc_driver_postgresql.dbapi.connect(uri) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        print(cur.fetch_arrow_table())
```

Sections: ADBC PostgreSQL Driver for Python, Example, Building

</details>

### alpaca-py

The Official Python SDK for Alpaca APIs

`pip install alpaca-py` · installs (wheel) · licence: Apache Software License · rank 3940 · last release 2026-11-05 · [PyPI](https://pypi.org/project/alpaca-py/) · [docs](https://alpaca.markets/docs/python-sdk/) · [source](https://github.com/alpacahq/alpaca-py)

<details><summary>README extract</summary>

Example:
```python
from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import ListAccountsRequest
from alpaca.broker.enums import AccountEntities

broker_client = BrokerClient('api-key', 'secret-key')

# search for accounts created after January 30th 2022.
# Response should contain Contact and Identity fields for each account.
...
```

Sections: About, Documentation, Update, What’s New?, Broker API, OOP Design, Data Validation, Many Clients, API Keys, Trading and Market Data API, Usage, Broker API Example, Trading API Example

</details>

### amazon-textract-textractor

A package to use AWS Textract services.

`pip install amazon-textract-textractor` · installs (wheel) · licence: Apache 2.0 · rank 3941 · last release 2026-08-11 · [PyPI](https://pypi.org/project/amazon-textract-textractor/)

<details><summary>README extract</summary>

Textractor is a python package created to seamlessly work with Amazon Textract a document intelligence service offering text recognition, table extraction, form processing, and much more. Whether you are making a one-off script or a complex distributed document processing pipeline, Textractor makes it easy to use Textract. ...

Example:
```python
from textractor import Textractor

extractor = Textractor(profile_name="default")
```

Sections: Documentation, Examples, Setup, Text recognition, Table extraction, Form extraction, Analyze ID, Receipt processing (Analyze Expense), CLI, Tests, Citing

</details>

### azure

Microsoft Azure Client Libraries for Python

`pip install azure` · installs from source (sdist only) · licence: MIT License · rank 3958 · last release 2020-04-08 · [PyPI](https://pypi.org/project/azure/)

<details><summary>README extract</summary>

This package was the Microsoft Azure bundle.

Starting with v5.0.0, this package is deprecated. Please install the service specific packages prefixed by `azure` needed for your application.

The complete list of available packages can be found at:

Here's a non-exhaustive list of common packages: ...

</details>

### azure-ai-contentsafety

Microsoft Azure AI Content Safety Client Library for Python

`pip install azure-ai-contentsafety` · installs (wheel) · licence: MIT License · rank 3966 · last release 2023-12-12 · [PyPI](https://pypi.org/project/azure-ai-contentsafety/)

<details><summary>README extract</summary>

Azure AI Content Safety detects harmful user-generated and AI-generated content in applications and services. Content Safety includes text and image APIs that allow you to detect material that is harmful:

* Text Analysis API: Scans text for sexual content, violence, hate, and self-harm with multi-severity levels. ...

Example:
```python
import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import TextCategory
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions

key = os.environ["CONTENT_SAFETY_KEY"]
...
```

...

</details>

### aiorwlock

Read write lock for asyncio.

`pip install aiorwlock` · installs (wheel) · licence: Apache Software License · rank 4015 · last release 2026-02-20 · [PyPI](https://pypi.org/project/aiorwlock/) · [docs](https://github.com/aio-libs/aiorwlock) · [source](https://github.com/aio-libs/aiorwlock)

### azure-loganalytics

Microsoft Azure Log Analytics Client Library for Python

`pip install azure-loganalytics` · installs (wheel) · licence: MIT License · rank 4030 · last release 2021-11-12 · [PyPI](https://pypi.org/project/azure-loganalytics/)

<details><summary>README extract</summary>

This package is no longer being maintained. Please use our latest package azure-monitor-query.

A migration guide has been provided for the same.

Sections: Microsoft Azure SDK for Python, 0.1.1 (2021-11-11), 0.1.0 (2018-07-11)

</details>

### asyncio-atexit

Like atexit, but for asyncio

`pip install asyncio-atexit` · installs (wheel) · licence: MIT License · rank 4044 · last release 2022-04-26 · [PyPI](https://pypi.org/project/asyncio-atexit/)

<details><summary>README extract</summary>

Adds atexit functionality to asyncio:

atexit is part of the standard library,
and gives you a way to register functions to call when the interpreter exits.

asyncio doesn't have equivalent functionality to register functions
when the _event loop exits: ...

Example:
```python
import asyncio_atexit

async def close_db():
    await db_connection.close()

asyncio_atexit.register(close_db)
```

</details>

### azure-appconfiguration-provider

Microsoft App Configuration Provider Library for Python

`pip install azure-appconfiguration-provider` · installs (wheel) · licence: MIT License · rank 4053 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-appconfiguration-provider/)

<details><summary>README extract</summary>

Azure App Configuration is a managed service that helps developers centralize their application configurations simply and securely. This provider adds additional functionality above the azure-sdk-for-python.

Using the provider enables loading sets of configurations from an Azure App Configuration store in a managed way.

Features:
Currently the Azure App Configuration Provider enables:

* Connecting to an App Configuration Store using a connection string or Entra ID.
* Selecting multiple sets of configurations using `SettingSelector`. ...

Example:
```python
import os
from azure.appconfiguration.provider import load
from azure.identity import DefaultAzureCredential

endpoint = os.environ["APPCONFIGURATION_ENDPOINT_STRING"]
credential = DefaultAzureCredential()

...

</details>

### asyncclick

Composable command line interface toolkit, async fork

`pip install asyncclick` · installs (wheel) · licence: BSD-3-Clause · rank 4056 · last release 2026-06-30 · [PyPI](https://pypi.org/project/asyncclick/) · [source](https://github.com/python-trio/asyncclick/)

<details><summary>README extract</summary>

Asyncclick is a fork of Click (described below) that works with trio or asyncio.

AsyncClick allows you to seamlessly use async command and subcommand handlers.

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". ...

Example:
```python
import asyncclick as click
import anyio

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
async def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
...
```

Sections: $ asyncclick, Click, A Simple Example, Differences to Click, AsyncClick

</details>

### azure-servicefabric

Microsoft Azure Service Fabric Client Library for Python

`pip install azure-servicefabric` · installs (wheel) · licence: MIT License · rank 4073 · last release 2021-12-14 · [PyPI](https://pypi.org/project/azure-servicefabric/)

<details><summary>README extract</summary>

This is the Microsoft Azure Service Fabric Client Library.
This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.
For a more complete view of Azure libraries, see the azure sdk python release.

Sections: Microsoft Azure SDK for Python, Usage, Provide Feedback, 8.2.0.0 (2021-12-14), 8.0.0.0 (2021-05-03), 7.2.0.46 (2020-10-29), 7.1.0.45 (2020-05-14), 7.0.0.0 (2019-12-13), 6.6.0.0 (2019-12-07), 6.5.0.0 (2019-06-17), 6.4.0.0 (2018-12-07), 6.3.0.0 (2018-07-27), 6.2.0.0 (2018-05-10), 6.1.2.9 (2018-02-05)

</details>

### azure-mgmt-relay

Microsoft Azure Relay Management Client Library for Python

`pip install azure-mgmt-relay` · installs (wheel) · licence: MIT · rank 4092 · last release 2026-09-16 · [PyPI](https://pypi.org/project/azure-mgmt-relay/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Relay Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `RelayNamespaceProperties` added property `minimum_tls_version`
 - Added enum `TlsVersion`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.relay import RelayAPIMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = RelayAPIMgmtClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-redisenterprise

Microsoft Azure Redisenterprise Management Client Library for Python

`pip install azure-mgmt-redisenterprise` · installs (wheel) · licence: MIT · rank 4142 · last release 2026-11-04 · [PyPI](https://pypi.org/project/azure-mgmt-redisenterprise/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Redis Enterprise Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `RedisEnterpriseManagementClient` added method `send_request`
 - Client `RedisEnterpriseManagementClient` added operation group `clusters`
 - Client `RedisEnterpriseManagementClient` added operation group `migrations`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.redisenterprise import RedisEnterpriseManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt

Microsoft Azure Resource Management Client Libraries for Python

`pip install azure-mgmt` · installs from source (sdist only) · licence: MIT License · rank 4149 · last release 2020-04-08 · [PyPI](https://pypi.org/project/azure-mgmt/)

<details><summary>README extract</summary>

This package was the Microsoft Azure Resource Management bundle.

Starting with v5.0.0, this package is deprecated. Please install the service specific packages prefixed by `azure-mgmt` needed for your application.

The complete list of available packages can be found at:

Here's a non-exhaustive list of common packages: ...

</details>

### azure-mgmt-powerbiembedded

Microsoft Azure Power BI Embedded Management Client Library for Python

`pip install azure-mgmt-powerbiembedded` · installs (wheel) · licence: MIT License · rank 4161 · last release 2024-06-24 · [PyPI](https://pypi.org/project/azure-mgmt-powerbiembedded/)

<details><summary>README extract</summary>

This is the Microsoft Azure Power BI Embedded Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation group PowerBIEmbeddedManagementClientOperationsMixin

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.powerbiembedded import PowerBIEmbeddedManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = PowerBIEmbeddedManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### akshare

AKShare is an elegant and simple financial data interface library for Python, built for human beings!

`pip install akshare` · installs (wheel) · licence: MIT License · rank 4164 · last release 2026-11-06 · [PyPI](https://pypi.org/project/akshare/) · [docs](https://akshare.akfamily.xyz/)

<details><summary>README extract</summary>

资源分享：对于想了解更多财经数据与量化投研的小伙伴，推荐一个专注于财经数据和量化研究的知识社区。
该社区提供相关文档和视频学习资源，汇集了各类财经数据源和量化投研工具的使用经验。
有兴趣深入学习的朋友可点此了解更多，也推荐大家关注微信公众号【数据科学实战】。

重磅推荐：AKQuant 是一款专为 量化投研 (Quantitative Research) 打造的高性能量化回测框架。它以 Rust 铸造极速撮合内核，
以 Python 链接数据与 AI 生态，旨在为量化投资者提供可靠高效的量化投研解决方案。参见AKQuant

工具推荐：期魔方是一款本地化期货量化分析工具，适合数据分析爱好者使用。无需复杂部署，支持数据分析和机器学习功能，研究功能免费开放。
如需了解更多信息可访问期魔方。

Features:
AKShare requires Python(64 bit) 3.11 or higher and
aims to simplify the process of fetching financial data.

Write less, get more!

- Documentation: 中文文档 ...

Example:
```python
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date="20231022", adjust="")
print(stock_zh_a_hist_df)
```

...

</details>

### azure-mgmt-commerce

Microsoft Azure Commerce Management Client Library for Python

`pip install azure-mgmt-commerce` · installs (wheel) · licence: not stated · rank 4176 · last release 2026-05-15 · [PyPI](https://pypi.org/project/azure-mgmt-commerce/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Commerce Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `UsageManagementClient` added parameter `cloud_setting` in method `init`
 - Client `UsageManagementClient` added method `send_request`
 - Model `UsageAggregation` added property `properties`
 - Added model `ErrorObjectResponse`
 - Added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.commerce import UsageManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-scheduler

Microsoft Azure Scheduler Management Client Library for Python

`pip install azure-mgmt-scheduler` · installs (wheel) · licence: MIT License · rank 4181 · last release 2024-10-31 · [PyPI](https://pypi.org/project/azure-mgmt-scheduler/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 01-31-2022. This package will only receive security fixes until 01-31-2022. To receive updates on new features and non-security bug fixes, upgrade to the replacement service, Azure Logic Apps. Refer to the migration guide ( for guidance on upgrading.

Sections: Microsoft Azure SDK for Python, 7.0.0 (2024-10-31), Other Changes, 7.0.0b1 (2020-10-22), 2.0.0 (2018-05-23), 1.1.3 (2017-09-07), 1.1.2 (2017-04-18), 1.1.1 (2017-01-13), 1.1.0 (2016-11-14), 1.0.0 (2016-08-30)

</details>

### azure-servicemanagement-legacy

Microsoft Azure Legacy Service Management Client Library for Python

`pip install azure-servicemanagement-legacy` · installs (wheel) · licence: Apache Software License · rank 4183 · last release 2024-11-01 · [PyPI](https://pypi.org/project/azure-servicemanagement-legacy/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 10-31-2024. This package will only receive security fixes until 10-31-2024. To receive updates on new features and non-security bug fixes, upgrade to the specific service management package listed here.

</details>

### azure-mgmt-hanaonazure

Microsoft Azure Hanaonazure Management Client Library for Python

`pip install azure-mgmt-hanaonazure` · installs (wheel) · licence: not stated · rank 4191 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-hanaonazure/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure SAP Hana on Azure Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.hanaonazure import HanaManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = HanaManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-mgmt-managementpartner

Microsoft Azure Managementpartner Management Client Library for Python

`pip install azure-mgmt-managementpartner` · installs (wheel) · licence: not stated · rank 4193 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-managementpartner/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Management Partner Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model Error has a new parameter code
 - Model Error has a new parameter message

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.managementpartner import ACEProvisioningManagementPartnerAPI

client = ACEProvisioningManagementPartnerAPI(credential=DefaultAzureCredential())
```

...

</details>

### azure-mgmt-machinelearningcompute

Microsoft Azure Machine Learning Compute Management Client Library for Python

`pip install azure-mgmt-machinelearningcompute` · installs (wheel) · licence: MIT License · rank 4196 · last release 2018-05-29 · [PyPI](https://pypi.org/project/azure-mgmt-machinelearningcompute/)

<details><summary>README extract</summary>

This is the Microsoft Azure Machine Learning Compute Management Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6. ...

Sections: Microsoft Azure SDK for Python, Compatibility, Usage, Provide Feedback, 0.4.1 (2018-05-29), 0.4.0 (2018-01-02), 0.3.0 (2017-10-25), 0.2.0 (2017-10-17), 0.1.0 (2017-09-22)

</details>

### azure-mgmt-devspaces

Microsoft Azure Dev Spaces Client Library for Python

`pip install azure-mgmt-devspaces` · installs (wheel) · licence: MIT License · rank 4204 · last release 2019-05-23 · [PyPI](https://pypi.org/project/azure-mgmt-devspaces/)

<details><summary>README extract</summary>

This is the Microsoft Azure Dev Spaces Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7. ...

Sections: Microsoft Azure SDK for Python, Usage, Provide Feedback, 0.2.0 (2019-05-23), 0.1.0 (2018-07-12)

</details>

### azure-applicationinsights

Microsoft Azure Application Insights Client Library for Python

`pip install azure-applicationinsights` · installs (wheel) · licence: MIT License · rank 4208 · last release 2022-02-11 · [PyPI](https://pypi.org/project/azure-applicationinsights/)

<details><summary>README extract</summary>

This package is no longer being maintained. Use the azure-monitor-query package instead.

For migration instructions, see the migration guide.

Sections: Microsoft Azure SDK for Python, 0.1.1 (2022-02-11), 0.1.0 (2018-07-11)

</details>

### agent-framework-openai

OpenAI integrations for Microsoft Agent Framework.

`pip install agent-framework-openai` · installs (wheel) · licence: MIT License · rank 4209 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-openai/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_openai)

<details><summary>README extract</summary>

OpenAI integration for Microsoft Agent Framework.

This package provides:

- `OpenAIChatClient` for the OpenAI Responses API
- `OpenAIChatCompletionClient` for the Chat Completions API
- `OpenAIEmbeddingClient` for embeddings

Example:
```python
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(model="gpt-4.1")
```

Sections: agent-framework-openai, Which chat client should I use?, Hosted function results, Environment variables, OpenAI, Azure OpenAI, OpenAI example, Azure OpenAI example, ChatClient vs ChatCompletionClient, Concurrent reuse

</details>

### autovizwidget

AutoVizWidget: An Auto-Visualization library for pandas dataframes

`pip install autovizwidget` · installs (wheel) · licence: BSD License · rank 4251 · last release 2025-07-07 · [PyPI](https://pypi.org/project/autovizwidget/)

### aioapns

An efficient APNs Client Library for Python/asyncio

`pip install aioapns` · installs (wheel) · licence: Apache Software License · rank 4269 · last release 2025-04-14 · [PyPI](https://pypi.org/project/aioapns/)

<details><summary>README extract</summary>

aioapns is a library designed specifically for sending push-notifications to iOS devices
via Apple Push Notification Service. aioapns provides an efficient client through
asynchronous HTTP2 protocol for use with Python's `asyncio`
framework.

aioapns requires Python 3.8 or later. ...

Features:
* Internal connection pool which adapts to the current load
* Support for certificate and token based connections
* Ability to set TTL (time to live) for notifications
* Ability to set priority for notifications
* Ability to set collapse-key for ...

Example:
```python
import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType

async def run():
    apns_cert_client = APNs(
        client_cert='/path/to/apns-cert.pem',
        use_sandbox=False,
    )
...

</details>

### azure-containerregistry

Microsoft Azure Azure Container Registry Client Library for Python

`pip install azure-containerregistry` · installs (wheel) · licence: MIT License · rank 4272 · last release 2023-07-11 · [PyPI](https://pypi.org/project/azure-containerregistry/) · [source](https://github.com/Azure/azure-sdk-python)

<details><summary>README extract</summary>

Azure Container Registry allows you to store and manage container images and artifacts in a private registry for all types of container deployments.

Use the client library for Azure Container Registry to:

- List images or artifacts in a registry
- Obtain metadata for images and artifacts, repositories and tags ...

Example:
```python
# Create a ContainerRegistryClient that will authenticate through Active Directory
from azure.containerregistry import ContainerRegistryClient
from azure.identity import DefaultAzureCredential

endpoint = "
audience = "
client = ContainerRegistryClient(endpoint, DefaultAzureCredential(), audience=audience)
```

...

</details>

### annoy

Approximate Nearest Neighbors in C++/Python optimized for memory usage and loading/saving to disk.

`pip install annoy` · installs from source (sdist only) · licence: Apache License 2.0 · rank 4312 · last release 2023-06-14 · [PyPI](https://pypi.org/project/annoy/)

<details><summary>README extract</summary>

Annoy (Approximate Nearest Neighbors Oh Yeah) is a C++ library with Python bindings to search for points in space that are close to a given query point. It also creates large read-only file-based data structures that are mmapped into memory so that many processes may share the same data.

Example:
```python
from annoy import AnnoyIndex
import random

f = 40  # Length of item vector that will be indexed

t = AnnoyIndex(f, 'angular')
for i in range(1000):
    v = [random.gauss(0, 1) for z in range(f)]
    t.add_item(i, v)

t.build(10) # 10 trees
t.save('test.ann')

# ...

u = AnnoyIndex(f, 'angular')
...
```

Sections: Annoy, Background, Summary of features, Python code example, Full Python API, Tradeoffs, How does it work, More info, Source code, Discuss

</details>

### aistudio-sdk

Python client library for the AIStudio API

`pip install aistudio-sdk` · installs (wheel) · licence: Apache Software License · rank 4323 · last release 2026-07-27 · [PyPI](https://pypi.org/project/aistudio-sdk/)

<details><summary>README extract</summary>

实现封装一言API的PythonSDK，支持AIStudio开发者进行基于一言的项目/应用/插件开发需求
实现封装AIStudio模型库API的PythonSDK，支持AIStudio开发者进行模型库的操作开发需求

快速开始

如何构建、安装、运行


如何执行自动化测试

如何贡献

贡献patch流程及质量要求

版本信息

本项目的各版本信息和变更历史可以在这里查看。

维护者

* xiangyiqing(xiangyiqing@baidu.com)

* xiangyiqing(xiangyiqing@baidu.com)
* linyichong(linyichong@baidu.com)
* suoyi(suoyi@baidu.com)


Sections: Python Sdk, owners, committers

</details>

### asyncio-mqtt

Idiomatic asyncio wrapper around paho-mqtt

`pip install asyncio-mqtt` · installs (wheel) · licence: OSI Approved · rank 4324 · last release 2023-06-26 · [PyPI](https://pypi.org/project/asyncio-mqtt/) · [source](https://github.com/sbtinstruments/asyncio-mqtt)

<details><summary>README extract</summary>

Write code like this:

Subscriber

Publisher

_asyncio-mqtt combines the stability of the time-proven paho-mqtt library with a modern, asyncio-based interface.

- No more callbacks! 👍
- No more return codes (welcome to the `MqttError`)
- Graceful disconnection (forget about `on_unsubscribe`, `on_disconnect`, etc.)
- Compatible with `async` code ...

Features:
Managing a connection by calling `connect` and `disconnect` directly is a bit tricky. For example, when you're disconnecting the client, you'd have to make sure that there's no other task that still relies on the connection. ...

Example:
```python
async with Client("test.mosquitto.org") as client:
    async with client.messages() as messages:
        await client.subscribe("humidity/#")
        async for message in messages:
...

</details>

### avro-gen

Avro record class and specific record reader generator

`pip install avro-gen` · installs from source (sdist only) · licence: Apache Software License · rank 4330 · last release 2018-01-13 · [PyPI](https://pypi.org/project/avro-gen/)

<details><summary>README extract</summary>

Current Avro implementation in Python is completely typelss and operates on dicts.
While in many cases this is convenient and pythonic, not being able to discover the schema
by looking at the code, not enforcing schema during record constructions, and not having any
context help from the IDE could hamper developer performance and introduce bugs. ...

Sections: AVRO-GEN, Avro record class and specific record reader generator., Usage

</details>

### azure-schemaregistry

Microsoft Azure Azure Schema Registry Client Library for Python

`pip install azure-schemaregistry` · installs (wheel) · licence: MIT License · rank 4340 · last release 2024-09-18 · [PyPI](https://pypi.org/project/azure-schemaregistry/)

<details><summary>README extract</summary>

Azure Schema Registry is a schema repository service hosted by Azure Event Hubs, providing schema storage, versioning,
and management. The registry is leveraged by encoders to reduce payload size while describing payload structure with
schema identifiers rather than full schemas. This package provides:

1. ...

Features:
- Sync and async `JsonSchemaEncoder` have been added under `azure.schemaregistry.encoder.jsonencoder`.
- `InvalidContentError` have been added under `azure.schemaregistry.encoder.jsonencoder` for use with the `JsonSchemaEncoder`. ...

Example:
```python
from azure.schemaregistry import SchemaRegistryClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
...

</details>

### azureml-featurestore

Azure Machine Learning Feature Store SDK

`pip install azureml-featurestore` · installs (wheel) · licence: MIT License · rank 4368 · last release 2026-02-06 · [PyPI](https://pypi.org/project/azureml-featurestore/)

<details><summary>README extract</summary>

The `azureml-featurestore` package is the core SDK interface for Azure ML Feature Store. This SDK works along the
`azure-ai-ml` SDK to provide the managed feature store experience.

- Develop feature set specification in Spark with the ability for feature transformation.
- List and get feature sets defined in Azure ML Feature Store. ...

Sections: Azure Machine Learning Feature Store Python SDK, Main features in the `azureml-featurestore` package, Getting started, 1.2.1 (2025.09.17), 1.2.0 (2025.08.18), 1.1.2 (2025.03.27), 1.1.1 (2025.02.25), 1.1.0 (2024.03.12), 1.0.1 (2023.12.28), 1.0.0 (2023.11.14), 0.1.0b6 (2023.11.1), 0.1.0b5 (2023.10.4), 0.1.0b4 (2023.08.28), 0.1.0b3 (2023.07.10)

</details>

### artifacts-keyring

"Automatically retrieve credentials for Azure Artifacts."

`pip install artifacts-keyring` · installs from source (sdist only) · licence: "MIT" · rank 4457 · last release 2025-08-13 · [PyPI](https://pypi.org/project/artifacts-keyring/)

<details><summary>README extract</summary>

'artifacts-keyring' is a relatively thin wrapper around artifacts-credprovider. Make sure to also look at that repository for more information about different scenarios. For example:

* Environment variable to explicitly override tokens
* Safely using credentials in docker ...

Sections: NOTE, artifacts-keyring, Usage, Requirements, Publishing packages to an Azure Artifacts feed, Advanced configuration, Environment variables, Build Environment Variables

</details>

### aioconsole

Asynchronous console and interfaces for asyncio

`pip install aioconsole` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 4508 · last release 2025-10-14 · [PyPI](https://pypi.org/project/aioconsole/)

_README extract left out: share-alike licence._

### ag-ui-a2ui-toolkit

Framework-agnostic helpers for building A2UI subagent tools — op builders, prompt assembly, history walkers, and request/envelope orchestration shared across framework adapters.

`pip install ag-ui-a2ui-toolkit` · installs (wheel) · licence: MIT · rank 4513 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ag-ui-a2ui-toolkit/)

<details><summary>README extract</summary>

Framework-agnostic helpers for building A2UI subagent tools.

Each per-framework adapter (LangGraph, ADK, Mastra, …) composes these helpers
with its own framework-specific glue: tool decorator, runtime accessor, model
binding + invoke. Nothing in this package depends on any agent framework. ...

Sections: ag-ui-a2ui-toolkit, Surface, See also

</details>

### anyscale

Command Line Interface for Anyscale

`pip install anyscale` · installs (wheel) · licence: AS License · rank 4516 · last release 2026-11-05 · [PyPI](https://pypi.org/project/anyscale/)

<details><summary>README extract</summary>

This package contains the command line interface and the sdk for the Anyscale platform.

View Anyscale docs here
View CLI docs here
View SDK docs here

Selects the stream used for informational CLI and SDK output — progress messages,
block headings and spinners. ...

Sections: Anyscale, Environment variables, `ANYSCALE_LOG_STREAM`

</details>

### arize-phoenix-evals

LLM Evaluations

`pip install arize-phoenix-evals` · installs (wheel) · licence: Elastic-2.0 · rank 4527 · last release 2026-10-28 · [PyPI](https://pypi.org/project/arize-phoenix-evals/) · [docs](https://arize.com/docs/phoenix/) · [source](https://github.com/Arize-ai/phoenix)

<details><summary>README extract</summary>

Phoenix Evals provides lightweight, composable building blocks for writing and running evaluations on LLM applications, including tools to determine relevance, toxicity, hallucination detection, and much more.

Features:
- Works with your preferred model SDKs via adapters (OpenAI, LiteLLM, LangChain)
- Powerful input mapping and binding for working with complex data structures
- Several pre-built metrics for common evaluation tasks like hallucination detection ...

Example:
```python
from phoenix.evals import create_classifier
from phoenix.evals.llm import LLM

# Create an LLM instance
llm = LLM(provider="openai", model="gpt-4o")

# Create an evaluator
evaluator = create_classifier(
    name="helpfulness",
...

</details>

### airbyte-api

Python Client SDK for Airbyte API

`pip install airbyte-api` · installs (wheel) · licence: not stated · rank 4571 · last release 2026-06-23 · [PyPI](https://pypi.org/project/airbyte-api/) · [source](https://github.com/airbytehq/airbyte-api-python-sdk)

<details><summary>README extract</summary>

Programatically control Airbyte Cloud through an API.

Developers will need to create an API Key within your Developer Portal to make API requests. You can use your existing Airbyte account to log in to the Developer Portal. Once you are in the Developer Portal, use the API Keys tab to create or remove API Keys. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "airbyte-api",
# ]
# ///

from airbyte_api import AirbyteAPI

sdk = AirbyteAPI(
  # SDK arguments
)

# Rest of script here...
```

...

</details>

### awsiotsdk

AWS IoT SDK based on the AWS Common Runtime

`pip install awsiotsdk` · installs (wheel) · licence: Apache Software License · rank 4579 · last release 2026-07-24 · [PyPI](https://pypi.org/project/awsiotsdk/)

<details><summary>README extract</summary>

The AWS IoT Device SDK for Python v2 connects your Python applications and devices to the AWS IoT platform. It handles the complexities of secure communication, authentication, and device management so you can focus on your IoT solution. The SDK makes it easy to use AWS IoT services like Device Shadows, Jobs, and Fleet Provisioning. ...

Features:
The primary purpose of the AWS IoT Device SDK for Python v2 is to simplify the process of connecting devices to AWS IoT Core and interacting with AWS IoT services on various platforms. The SDK provides: ...

Sections: AWS IoT Device SDK for Python v2, Features, Minimum Requirements, macOS and Linux, Windows, Building from source, Getting Started, Samples, Specifics, Mac-Only TLS 1.3, Mac Keychain, Getting Help, Resources

</details>

### aiogoogle

Async Google API client

`pip install aiogoogle` · installs (wheel) · licence: MIT · rank 4597 · last release 2026-11-01 · [PyPI](https://pypi.org/project/aiogoogle/)

<details><summary>README extract</summary>

Async Google API client

Aiogoogle makes it possible to access most of Google's public APIs which include:

- Google Calendar API
- Google Drive API
- Google Contacts API
- Gmail API
- Google Maps API
- Youtube API
- Translate API
- Google Sheets API
- Google Docs API
- Gogle Analytics API
- Google Books API
- Google Fitness API ...

Sections: Aiogoogle, Documentation 📑

</details>

### argbind

Simple way to bind function arguments to the command line.

`pip install argbind` · installs from source (sdist only) · licence: MIT License · rank 4646 · last release 2024-05-24 · [PyPI](https://pypi.org/project/argbind/)

<details><summary>README extract</summary>

Build CLIs via docstrings and type annotations, with YAML support.

*ArgBind is a simple way to bind function or class arguments to the command line or to .yml files!*
It supports scoping of arguments, similar to other frameworks like
Hydra and
gin-config. ...

Features:
I built ArgBind mostly to help me configure my machine learning experiments. ML experiment
configuration is often highly nested, and can get out of hand quick. I didn't want to switch
my workflow around too much to accommodate a new framework. ...

Example:
```python
import argbind

@argbind.bind()
def hello(
    name : str = 'world'
):
    """Say hello to someone.

    Parameters

    name : str, optional
        Who you're saying hello to, by default 'world'
    """
    print("Hello " + name)

if name == "main":
...

</details>

### ahocorasick-rs

Search for multiple substrings at the same time, and quickly too

`pip install ahocorasick-rs` · installs (wheel) · licence: Apache 2.0 · rank 4655 · last release 2025-10-08 · [PyPI](https://pypi.org/project/ahocorasick-rs/)

<details><summary>README extract</summary>

`ahocorasick_rs` allows you to search for multiple substrings ("patterns") in a given string ("haystack") using variations of the Aho-Corasick algorithm.

In particular, it's implemented as a wrapper of the Rust `aho-corasick` library, and provides a faster alternative to the `pyahocorasick` library. ...

Example:
```python
>>> import ahocorasick_rs
>>> patterns = ["hello", "world", "fish"]
>>> haystack = "this is my first hello world. hello!"
>>> ac = ahocorasick_rs.AhoCorasick(patterns)
```

...

</details>

### aioesphomeapi

Python API for interacting with ESPHome devices.

`pip install aioesphomeapi` · installs (wheel) · licence: MIT · rank 4686 · last release 2026-11-05 · [PyPI](https://pypi.org/project/aioesphomeapi/)

<details><summary>README extract</summary>

`aioesphomeapi` allows you to interact with devices flashed with ESPHome.

Example:
```python
api = aioesphomeapi.APIClient("device.local", 6053, password="MyPassword")
```

Sections: aioesphomeapi, Usage

</details>

### aeventkit

Event-driven data pipelines

`pip install aeventkit` · installs (wheel) · licence: BSD-3-Clause · rank 4754 · last release 2026-10-19 · [PyPI](https://pypi.org/project/aeventkit/) · [source](https://github.com/ib-api-reloaded/eventkit)

<details><summary>README extract</summary>

The primary use cases of eventkit are

* to send events between loosely coupled components;
* to compose all kinds of event-driven data pipelines.

The interface is kept as Pythonic as possible,
with familiar names from Python and its libraries where possible.
For scheduling asyncio is used and there is seamless integration with it. ...

Example:
```python
import eventkit as ev

def f(a, b):
    print(a * b)

def g(a, b):
    print(a / b)

event = ev.Event()
event += f
event += g
event.emit(10, 5)
```

Sections: Introduction, Examples, Parallel processing, Inspired by, Documentation

</details>

### agent-sanitizer

Python client for agent-sanitizer: a thin bridge to the Node.js CLI for byte-identical sanitization verdicts.

`pip install agent-sanitizer` · installs (wheel) · licence: Apache-2.0 · rank 4759 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agent-sanitizer/) · [source](https://github.com/AlexanderMattTurner/agent-sanitizer)

<details><summary>README extract</summary>

A thin Python bridge to the `agent-sanitizer`
Node.js CLI. The sanitization logic has a single source of truth — the
JavaScript in `src/` — so this package shells out to the CLI rather than
re-implementing it, giving a Python pipeline byte-identical verdicts with no
second implementation to keep in sync.

- Node.js (>= 22) on `PATH`. ...

Example:
```python
from agent_sanitizer import sanitize

result = sanitize("untrusted text", html=True)
print(result.cleaned, result.found, result.warnings)
```

Sections: agent-sanitizer (Python client), Requirements, Optional: point at your own JS checkout, Usage, Secret redaction (`[secrets]` extra), In-process, The rehydration map contract, Daemon vs. one-shot, Versioning

</details>

### aws-cdk.asset-kubectl-v20

A Lambda Layer that contains kubectl v1.20

`pip install aws-cdk.asset-kubectl-v20` · installs (wheel) · licence: OSI Approved · rank 4791 · last release 2025-02-07 · [PyPI](https://pypi.org/project/aws-cdk.asset-kubectl-v20/) · [source](https://github.com/cdklabs/awscdk-asset-kubectl.git)

### atlassian-jwt-auth

Python implementation of the Atlassian Service to Service Authentication specification.

`pip install atlassian-jwt-auth` · installs (wheel) · licence: MIT License · rank 4810 · last release 2026-05-21 · [PyPI](https://pypi.org/project/atlassian-jwt-auth/) · [source](https://github.com/atlassian/asap-authentication-python)

<details><summary>README extract</summary>

This package provides an implementation of the Service to Service Authentication specification.

Example:
```python
import atlassian_jwt_auth

signer = atlassian_jwt_auth.create_signer('issuer', 'issuer/key', private_key_pem)
a_jwt = signer.generate_jwt('audience')
```

Sections: Atlassian JWT authentication, Using this library, To create a JWT for authentication, To create a JWT using a data uri, To make an authenticated HTTP request, To verify a JWT

</details>

### acsylla

A high performance asynchronous Cassandra and ScyllaDB client

`pip install acsylla` · installs (wheel) · licence: Apache Software License; MIT License · rank 4836 · last release 2026-10-19 · [PyPI](https://pypi.org/project/acsylla/)

<details><summary>README extract</summary>

A composition of *async* + *cassandra* + *scylla* words.

Under the hood _acsylla_ has modern, feature-rich and shard-aware C/C++ client library for Cassandra and ScyllaDB.

Features:
* Shard-Awareness
* Asynchronous API
* Simple, Prepared, and Batch statements
* Asynchronous I/O, parallel execution, and request pipelining
* Connection pooling
* Automatic node discovery
* Automatic reconnection
* Configurable load balancing
* ...

Example:
```python
import acsylla
import asyncio

async def main():
    cluster = acsylla.create_cluster(["localhost"])
    session = await cluster.create_session()
    await session.query(
        """
        CREATE KEYSPACE IF NOT EXISTS acsylla WITH REPLICATION = {
            'class': 'SimpleStrategy', 'replication_factor': 1
        }
        """
    )
...
...

</details>

### azure-functions-durable

Durable Functions For Python

`pip install azure-functions-durable` · installs (wheel) · licence: MIT License · rank 4884 · last release 2026-07-30 · [PyPI](https://pypi.org/project/azure-functions-durable/)

<details><summary>README extract</summary>

|Branch|Status|

|main||
|dev||

 Durable Functions is an extension of Azure Functions that lets you write stateful functions in a serverless compute environment. The extension lets you define stateful workflows by writing orchestrator functions and stateful entities by writing entity functions using the Azure Functions programming model. ...

Sections: Durable Functions for Python, Durable Functions Python 2.0 beta, Getting Started, Tooling

</details>

### azure-mgmt-hybridcompute

Microsoft Azure Hybridcompute Management Client Library for Python

`pip install azure-mgmt-hybridcompute` · installs (wheel) · licence: MIT · rank 4933 · last release 2026-11-03 · [PyPI](https://pypi.org/project/azure-mgmt-hybridcompute/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Hybrid Compute Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `HybridComputeManagementClient` added operation group `vm_applications`
 - Enum `IdentityKeyStore` added member `TPM_TRANSITION`
 - Model `MachineUpdateProperties` added property `client_public_key`
 - Added model `VmApplication`
 - Added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.hybridcompute import HybridComputeManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### aws-cryptographic-material-providers

AWS Cryptographic Material Providers Library for Python

`pip install aws-cryptographic-material-providers` · installs (wheel) · licence: not stated · rank 4935 · last release 2026-09-03 · [PyPI](https://pypi.org/project/aws-cryptographic-material-providers/)

<details><summary>README extract</summary>

These are the docs for the AWS Cryptographic Materials Providers Library for Python.

The latest full documentation can be found at Read the Docs.

Find us on GitHub.

Sections: aws-cryptographic-materials-providers-library-python, Getting Started, Required Prerequisites, Concepts, Thread safety

</details>

### aws-cryptography-internal-standard-library

(no summary)

`pip install aws-cryptography-internal-standard-library` · installs (wheel) · licence: not stated · rank 4939 · last release 2026-09-03 · [PyPI](https://pypi.org/project/aws-cryptography-internal-standard-library/)

### aws-cryptography-internal-dynamodb

(no summary)

`pip install aws-cryptography-internal-dynamodb` · installs (wheel) · licence: not stated · rank 4940 · last release 2026-09-03 · [PyPI](https://pypi.org/project/aws-cryptography-internal-dynamodb/)

### aws-cryptography-internal-primitives

(no summary)

`pip install aws-cryptography-internal-primitives` · installs (wheel) · licence: not stated · rank 4941 · last release 2026-09-03 · [PyPI](https://pypi.org/project/aws-cryptography-internal-primitives/)

### aws-cryptography-internal-kms

(no summary)

`pip install aws-cryptography-internal-kms` · installs (wheel) · licence: not stated · rank 4943 · last release 2026-09-03 · [PyPI](https://pypi.org/project/aws-cryptography-internal-kms/)

### adrf

Async support for Django REST framework

`pip install adrf` · installs (wheel) · licence: MIT License · rank 4953 · last release 2026-08-11 · [PyPI](https://pypi.org/project/adrf/) · [source](https://github.com/em1208/adrf)

<details><summary>README extract</summary>

Async support for Django REST framework

* Python 3.8+
* Django 4.1+

We highly recommend and only officially support the latest patch release of
each Python and Django series.

Example:
```python
from adrf.views import APIView

class AsyncAuthentication(BaseAuthentication):
    async def authenticate(self, request) -> tuple[User, None]:
        return user, None

class AsyncPermission:
    async def has_permission(self, request, view) -> bool:
        if random.random() < 0.7:
            return False

        return True

...
```

Sections: Async Django REST framework, Requirements, Examples, Async Views, Async ViewSets, ModelViewSet Routing, Async Serializers, Async Generics

</details>

### azure-schemaregistry-avroserializer

Microsoft Azure Schema Registry Avro Serializer Client Library for Python

`pip install azure-schemaregistry-avroserializer` · installs (wheel) · licence: MIT License · rank 4961 · last release 2023-09-07 · [PyPI](https://pypi.org/project/azure-schemaregistry-avroserializer/)

<details><summary>README extract</summary>

This package is no longer being maintained. Use the azure-schemaregistry-avroencoder package instead.

For migration instructions, see the migration guide.

Features:
- Async version of `AvroSerializer` has been added under `azure.schemaregistry.serializer.avroserializer.aio`.
- Depends on `azure-schemaregistry>=1.0.0,<2.0.0`.

Sections: Microsoft Azure SDK for Python, 1.0.0b4.post1 (2023-08-15), 1.0.0b4 (2021-11-11), Features Added, Breaking Changes, 1.0.0b3 (2021-10-06), 1.0.0b2 (2021-08-18), 1.0.0b1 (2020-09-09)

</details>

### arize-phoenix

AI Observability and Evaluation

`pip install arize-phoenix` · installs (wheel) · licence: Elastic-2.0 · rank 4973 · last release 2026-10-30 · [PyPI](https://pypi.org/project/arize-phoenix/) · [docs](https://arize.com/docs/phoenix/) · [source](https://github.com/Arize-ai/phoenix)

<details><summary>README extract</summary>

🇺🇸 English • 🇨🇳 中文 • 🇹🇼 繁體中文 • 🇯🇵 日本語 • 🇵🇹 Português • 🇧🇷 Português • 🇰🇷 한국어 • 🇪🇸 Español • 🇩🇪 Deutsch • 🇫🇷 Français • 🇮🇱 עברית • 🇸🇦 العربية • 🇷🇺 Русский • 🇵🇱 Polski • 🇨🇿 Čeština • 🇳🇱 Nederlands • 🇹🇷 Türkçe • 🇺🇦 Українська • 🇻🇳 Tiếng Việt • 🇵🇭 Tagalog • 🇮🇩 Indonesia • 🇹🇭 ไทย • 🇮🇳 हिन्दी • 🇧🇩 বাংলা • 🇵🇰 اردو • 🇷🇴 Română • 🇸🇪 Svenska • 🇮🇹 Italiano • ...

Sections: Run Locally, Trace Your Application, Deploy, Packages, Python Subpackages, TypeScript Subpackages, Tracing Integrations, Span Processors, JavaScript Integrations, Java Integrations, Go Integrations, Platforms, Vector Databases, Sandboxes

</details>

### azure-ai-agentserver-core

Foundation utilities and host framework for Azure AI Hosted Agents

`pip install azure-ai-agentserver-core` · installs (wheel) · licence: MIT · rank 4980 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-ai-agentserver-core/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

The `azure-ai-agentserver-core` package provides the foundation host framework for building Azure AI Hosted Agent containers. It handles the protocol-agnostic infrastructure — health probes, graceful shutdown, OpenTelemetry tracing, and ASGI serving — so that protocol packages can focus on their endpoint logic.

Example:
```python
from azure.ai.agentserver.invocations import InvocationAgentServerHost
from starlette.responses import JSONResponse

app = InvocationAgentServerHost()

@app.invoke_handler
async def handle(request):
    body = await request.json()
    return JSONResponse({"greeting": f"Hello, {body['name']}!"})

app.run()
```

...

</details>

### aws-durable-execution-sdk-python

AWS Durable Execution SDK for Python

`pip install aws-durable-execution-sdk-python` · installs (wheel) · licence: Apache-2.0 · rank 4984 · last release 2026-10-29 · [PyPI](https://pypi.org/project/aws-durable-execution-sdk-python/) · [docs](https://github.com/aws/aws-durable-execution-sdk-python#readme) · [source](https://github.com/aws/aws-durable-execution-sdk-python)

<details><summary>README extract</summary>

Build reliable, long-running AWS Lambda workflows with checkpointed steps, waits, callbacks, and parallel execution.

- Automatic checkpointing - Resume execution after Lambda pauses or restarts
- Durable steps - Run work with retry strategies and deterministic replay ...

Example:
```python
from aws_durable_execution_sdk_python import (
    DurableContext,
    StepContext,
    durable_execution,
    durable_step,
)
from aws_durable_execution_sdk_python.config import Duration

@durable_step
def validate_order(step_ctx: StepContext, order_id: str) -> dict:
    step_ctx.logger.info("Validating order", extra={"order_id": order_id})
...
```

...

</details>

### arviz-stats

Statistical computation and diagnostics for ArviZ.

`pip install arviz-stats` · installs (wheel) · licence: Apache Software License · rank 5011 · last release 2026-09-25 · [PyPI](https://pypi.org/project/arviz-stats/) · [docs](https://arviz-stats.readthedocs.io) · [source](https://github.com/arviz-devs/arviz-stats)

<details><summary>README extract</summary>

ArviZ (pronounced "AR-_vees") is a Python package for exploratory analysis of Bayesian models. It includes functions for posterior analysis, data storage, model checking, comparison and diagnostics.

arviz-stats is the subpackage in charge of the statistical and diagnostics computations.

ArviZ also has a Julia wrapper available ArviZ.jl. ...

Sections: arviz-stats, ArviZ in other languages, Documentation, Stable

</details>

### azure-ai-textanalytics

Microsoft Azure Text Analytics Client Library for Python

`pip install azure-ai-textanalytics` · installs (wheel) · licence: MIT License · rank 5039 · last release 2026-03-05 · [PyPI](https://pypi.org/project/azure-ai-textanalytics/)

<details><summary>README extract</summary>

The Azure Cognitive Service for Language is a cloud-based service that provides Natural Language Processing (NLP) features for understanding and analyzing text, and includes the following main features:

- Sentiment Analysis
- Named Entity Recognition
- Language Detection
- Key Phrase Extraction
- Entity Linking
- Multiple Analysis ...

Features:
- New enum values added for `HealthcareEntityCategory` and `HealthcareEntityRelation`.

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("<api_key>")
text_analytics_client = TextAnalyticsClient(endpoint=" credential=credential)
```

...

</details>

### ag-ui-langgraph

Implementation of the AG-UI protocol for LangGraph.

`pip install ag-ui-langgraph` · installs (wheel) · licence: MIT · rank 5046 · last release 2026-10-08 · [PyPI](https://pypi.org/project/ag-ui-langgraph/)

<details><summary>README extract</summary>

Implementation of the AG-UI protocol for LangGraph.

Provides a complete Python integration for LangGraph agents with the AG-UI protocol, including FastAPI endpoint creation and comprehensive event streaming.

Non-image attachments keep their LangChain content type: audio becomes `audio`,
video becomes `video`, and documents become `file`. ...

Features:
- Native LangGraph integration – Direct support for LangGraph workflows and state management
- FastAPI endpoint creation – Automatic HTTP endpoint generation with proper event streaming ...

Example:
```python
from langgraph.graph import StateGraph, MessagesState
from langchain_openai import ChatOpenAI
from ag_ui_langgraph import LangGraphAgent, add_langgraph_fastapi_endpoint
from fastapi import FastAPI
...

</details>

### azure-multiapi-storage

Microsoft Azure Storage Client Library for Python with multi API version support.

`pip install azure-multiapi-storage` · installs (wheel) · licence: MIT License · rank 5052 · last release 2025-09-28 · [PyPI](https://pypi.org/project/azure-multiapi-storage/)

<details><summary>README extract</summary>

Sections: 1.6.0, 1.5.0, 1.4.0, 1.3.0, 1.2.0, 1.1.0, 1.0.0, 0.10.0, 0.9.0, 0.8.0, 0.7.0, 0.6.2, 0.6.1, 0.6.0

</details>

### azure-ai-translation-document

Microsoft Azure Ai Translation Document Client Library for Python

`pip install azure-ai-translation-document` · installs (wheel) · licence: MIT License · rank 5058 · last release 2026-07-29 · [PyPI](https://pypi.org/project/azure-ai-translation-document/)

<details><summary>README extract</summary>

Azure Cognitive Services Document Translation is a cloud service that can be used to translate multiple and complex documents across languages and dialects while preserving original document structure and data format.
Use the client library for Document Translation to: ...

Example:
```python
"""DefaultAzureCredential will use the values from these environment
variables: AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET
"""
from azure.identity import DefaultAzureCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = os.environ["AZURE_DOCUMENT_TRANSLATION_ENDPOINT"]
...
```

...

</details>

### ada-url

URL parser and manipulator based on the WHAT WG URL standard

`pip install ada-url` · installs (wheel) · licence: Apache-2.0 · rank 5122 · last release 2026-07-28 · [PyPI](https://pypi.org/project/ada-url/) · [docs](https://ada-url.readthedocs.io) · [source](https://github.com/ada-url/ada-python)

<details><summary>README extract</summary>

This is `ada_url`, a fast standard-compliant Python library for working with URLs based on the `Ada` URL
parser.

* Documentation
* Development
* Ada

Example:
```python
>>> from ada_url import URL
>>> urlobj = URL('
>>> urlobj.href
'
```

Sections: ada-url, Usage examples, Parsing URLs, Altering URLs, Search parameters, Internationalized domain names, WHATWG URL compliance, Performance

</details>

### agent-framework-foundry

Microsoft Foundry integrations for Microsoft Agent Framework.

`pip install agent-framework-foundry` · installs (wheel) · licence: MIT License · rank 5144 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-foundry/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_foundry)

<details><summary>README extract</summary>

This package contains the Microsoft Foundry integrations for Microsoft Agent Framework, including Foundry chat clients, preconfigured Foundry agents, Foundry embedding clients, and Foundry memory providers.

This package supports `azure-ai-projects>=2.2.0,<2.8.0`. ...

Example:
```python
import os

from agent_framework.foundry import FoundryEmbeddingClient
from azure.identity.aio import AzureCliCredential

async with AzureCliCredential() as credential:
    async with FoundryEmbeddingClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["FOUNDRY_EMBEDDING_MODEL"],
...
```

...

</details>

### asn1tools

ASN.1 parsing, encoding and decoding.

`pip install asn1tools` · installs (wheel) · licence: MIT License · rank 5159 · last release 2026-09-01 · [PyPI](https://pypi.org/project/asn1tools/)

<details><summary>README extract</summary>

A Python package for ASN.1 parsing, encoding and decoding.

This project is *under development* and does only support a subset
of the ASN.1 specification syntax.

Supported codecs:

- Basic Encoding Rules (BER)
- Distinguished Encoding Rules (DER)
- Generic String Encoding Rules (GSER)
- JSON Encoding Rules (JER) ...

Example:
```python
>>> import asn1tools
>>> foo = asn1tools.compile_files('tests/files/foo.asn')
>>> encoded = foo.encode('Question', {'id': 1, 'question': 'Is 1+1=3?'})
>>> encoded
bytearray(b'0\x0e\x02\x01\x01\x16\x09Is 1+1=3?')
>>> foo.decode('Question', encoded)
{'id': 1, 'question': 'Is 1+1=3?'}
```

...

</details>

### akeyless

Akeyless API

`pip install akeyless` · installs (wheel) · licence: Apache Software License · rank 5160 · last release 2026-10-26 · [PyPI](https://pypi.org/project/akeyless/)

<details><summary>README extract</summary>

The purpose of this application is to provide access to Akeyless API. # noqa: E501

</details>

### azureml-core

Azure Machine Learning core packages, modules, and classes

`pip install azureml-core` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 5208 · last release 2026-06-16 · [PyPI](https://pypi.org/project/azureml-core/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after June 2026. This package will only receive security fixes until June 2026.

The azureml-core provides core packages, modules, and classes for Azure Machine Learning and includes the following: ...

</details>

### akracer

akracer is next version of py_mini_racer

`pip install akracer` · installs (wheel) · licence: MIT · rank 5211 · last release 2025-09-10 · [PyPI](https://pypi.org/project/akracer/) · [docs](https://github.com/akfamily/akracer#readme) · [source](https://github.com/akfamily/akracer)

<details><summary>README extract</summary>

AKRacer 主要是解决 py_mini_racer 在 64 位 ARM 操作系统中的动态链接库调用问题，主要
方案就是通过 `pip install akracer` 使得在对应 `py_mini_racer` 目录中下载相应的已经
编译好的动态链接库，目前主要包括 `armlibmini_racer.dylib` 和 `armlibmini_racer.glibc.so` 这
两个动态链接库，分别对应 Apple M 系列芯片和 Ubuntu 18.04，20.04 和 22.04 及树莓派 64 位操作系统。

需要在本地设置 PyPI 的环境变量

1. `HATCH_INDEX_USER` 为 `token`
2. ...

Sections: AKRacer, 安装, 环境变量设置, 定制化, 对应操作, 动态链接库, 项目管理

</details>

### aws-cdk.aws-lambda-python-alpha

The CDK Construct Library for AWS Lambda in Python

`pip install aws-cdk.aws-lambda-python-alpha` · installs (wheel) · licence: OSI Approved · rank 5224 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-lambda-python-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
python.PythonFunction(self, "MyFunction",
    entry="/path/to/my/function",  # required
    runtime=Runtime.PYTHON_3_8,  # required
    index="my_index.py",  # optional, defaults to 'index.py'
    handler="my_exported_func"
)
```

...

</details>

### alembic-autogenerate-enums

Alembic hook that allows enums values to be upgraded and downgraded in migrations automatically

`pip install alembic-autogenerate-enums` · installs (wheel) · licence: MIT License · rank 5257 · last release 2023-07-19 · [PyPI](https://pypi.org/project/alembic-autogenerate-enums/)

<details><summary>README extract</summary>

This package implements an Alembic hook that causes ``alembic revision
--autogenerate`` to output PostgreSQL ``ALTER TYPE .. ADD VALUE`` SQL
statements as part of new migrations.

Sections: alembic-autogenerate-enums, Usage, Notes, Tests

</details>

### atomicwrites-homeassistant

Atomic file writes.

`pip install atomicwrites-homeassistant` · installs (wheel) · licence: MIT License · rank 5310 · last release 2022-07-08 · [PyPI](https://pypi.org/project/atomicwrites-homeassistant/)

<details><summary>README extract</summary>

Atomic file writes.

Fork because the original package is unmaintained.

See API documentation for more
low-level interfaces.

Features that distinguish it from other similar libraries (see Alternatives and Credit):

- Race-free assertion that the target file doesn't yet exist. This can be
 controlled with the `overwrite` parameter. ...

Example:
```python
from atomicwrites import atomic_write

with atomic_write('foo.txt', overwrite=True) as f:
    f.write('Hello world.')
    # "foo.txt" doesn't exist yet.

# Now it does.
```

Sections: python-atomicwrites, How it works, fsync, Alternatives and Credit

</details>

### azure-eventhub-checkpointstoreblob

Microsoft Azure Event Hubs checkpointer implementation with Blob Storage Client Library for Python

`pip install azure-eventhub-checkpointstoreblob` · installs (wheel) · licence: MIT License · rank 5311 · last release 2025-02-13 · [PyPI](https://pypi.org/project/azure-eventhub-checkpointstoreblob/)

<details><summary>README extract</summary>

Azure EventHubs Checkpoint Store is used for storing checkpoints while processing events from Azure Event Hubs.
This Checkpoint Store package works as a plug-in package to `EventHubConsumerClient`. It uses Azure Storage Blob as the persistent store for maintaining checkpoints and partition ownership information. ...

Example:
```python
from azure.eventhub import EventHubConsumerClient
eventhub_client = EventHubConsumerClient.from_connection_string("my_eventhub_namespace_connection_string", "my_consumer_group", eventhub_name="my_eventhub")
```

Sections: _Disclaimer_, Getting started, Prerequisites, Key concepts, Checkpointing, Offsets & sequence numbers, Examples, Create an `EventHubConsumerClient`, Troubleshooting, General, Logging, Next steps, More sample code, Documentation

</details>

### atlasclient

Apache Atlas client

`pip install atlasclient` · installs from source (sdist only) · licence: Apache Software License · rank 5312 · last release 2019-08-19 · [PyPI](https://pypi.org/project/atlasclient/)

<details><summary>README extract</summary>

Apache Atlas client in Python.
Only compatible with Apache Atlas REST API v2.

* Free software: Apache Software License 2.0

 >>> from atlasclient.client import Atlas
 >>> client = Atlas('<atlas.host>', port=21000, username='admin', password='admin')
 >>> client.entity_guid(<guid>).status
 >>> params = {'typeName': 'DataSet', 'attrName': 'name', ...

Features:
* Lazy loading: requests are only performed when data are required and not yet available
* Resource object relationships: REST API from sub-resources are done transparently for the user, for instance the user does not have to know that it needs to ...

...

</details>

### awscurl

Curl like tool with AWS request signing

`pip install awscurl` · installs (wheel) · licence: MIT · rank 5410 · last release 2026-11-02 · [PyPI](https://pypi.org/project/awscurl/)

<details><summary>README extract</summary>

curl-like tool with AWS Signature Version 4 request signing.

Features:
* performs requests to AWS services with request signing using curl interface
* supports IAM profile credentials

Sections: awscurl, Features, Overview, Running via Docker, Examples, Options, Who uses awscurl, Related projects, Last but not least

</details>

### adbc-driver-snowflake

An ADBC driver for working with Snowflake.

`pip install adbc-driver-snowflake` · installs (wheel) · licence: Apache-2.0 · rank 5414 · last release 2026-04-07 · [PyPI](https://pypi.org/project/adbc-driver-snowflake/) · [source](https://github.com/apache/arrow-adbc)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Sections: ADBC Snowflake Driver for Python, Building

</details>

### archspec

A library to query system architecture

`pip install archspec` · installs (wheel) · licence: Other/Proprietary License · rank 5425 · last release 2026-10-28 · [PyPI](https://pypi.org/project/archspec/) · [docs](https://archspec.readthedocs.io) · [source](https://github.com/archspec/archspec.git)

<details><summary>README extract</summary>

Archspec aims at providing a standard set of human-understandable labels for
various aspects of a system architecture like CPU, network fabrics, etc. and
APIs to detect, query and compare them.

This project grew out of Spack and is currently under
active development. ...

Sections: Archspec (Python bindings), Running unit tests, Citing Archspec

</details>

### azure-ai-agentserver-invocations

Invocations protocol for Azure AI Hosted Agents

`pip install azure-ai-agentserver-invocations` · installs (wheel) · licence: MIT · rank 5471 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-ai-agentserver-invocations/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

The `azure-ai-agentserver-invocations` package provides the invocation protocol endpoints for Azure AI Hosted Agent containers. It plugs into the `azure-ai-agentserver-core` host framework and supports two transports on the same host: ...

Example:
```python
from azure.ai.agentserver.invocations import InvocationAgentServerHost
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.websockets import WebSocket

app = InvocationAgentServerHost()

@app.invoke_handler                 # POST /invocations (HTTP)
...
```

...

</details>

### amplitude-experiment

The official Amplitude Experiment Python SDK for server-side instrumentation.

`pip install amplitude-experiment` · installs (wheel) · licence: MIT License · rank 5485 · last release 2026-10-29 · [PyPI](https://pypi.org/project/amplitude-experiment/) · [source](https://github.com/amplitude/experiment-python-server)

<details><summary>README extract</summary>

Amplitude Python Server SDK for Experiment.

Example:
```python
from amplitude_experiment import Experiment, RemoteEvaluationConfig, RemoteEvaluationClient, User

# (1) Get your deployment's API key
apiKey = 'YOUR-API-KEY'

# (2) Initialize the experiment remote evaluation
experiment = Experiment.initialize_remote(api_key)

# (3) Fetch variants for a user
user = User(
    device_id="abcdefg",
...
```

Sections: Experiment Python SDK, Remote Evaluation Quick Start, Local Evaluation Quick Start, Running Unit Tests Suite, More Information, Need Help?

</details>

### arviz-base

Base ArviZ features and converters.

`pip install arviz-base` · installs (wheel) · licence: Apache Software License · rank 5487 · last release 2026-09-25 · [PyPI](https://pypi.org/project/arviz-base/) · [docs](https://arviz-base.readthedocs.io) · [source](https://github.com/arviz-devs/arviz-base)

<details><summary>README extract</summary>

ArviZ (pronounced "AR-_vees") is a Python package for exploratory analysis of Bayesian models. It includes functions for posterior analysis, data storage, model checking, comparison and diagnostics.

arviz-base is the subpackage in charge of converters and base manipulation.

ArviZ also has a Julia wrapper available ArviZ.jl. ...

Sections: arviz-base, ArviZ in other languages, Documentation, Stable

</details>

### arviz-plots

ArviZ-plots provides ready to use and composable plots for Bayesian Workflow.

`pip install arviz-plots` · installs (wheel) · licence: Apache Software License · rank 5509 · last release 2026-09-25 · [PyPI](https://pypi.org/project/arviz-plots/) · [docs](https://arviz-plots.readthedocs.io) · [source](https://github.com/arviz-devs/arviz-plots)

<details><summary>README extract</summary>

ArviZ (pronounced "AR-_vees") is a Python package for exploratory analysis of Bayesian models. It includes functions for posterior analysis, data storage, model checking, comparison and diagnostics.

arviz-plots is the subpackage in charge of the visualizations.

ArviZ also has a Julia wrapper available ArviZ.jl. ...

Sections: arviz-plots, ArviZ in other languages, Documentation, Stable

</details>

### azure-mgmt-costmanagement

Microsoft Azure Costmanagement Management Client Library for Python

`pip install azure-mgmt-costmanagement` · installs (wheel) · licence: MIT · rank 5512 · last release 2026-07-08 · [PyPI](https://pypi.org/project/azure-mgmt-costmanagement/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Cost Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `CostManagementClient` added parameter `cloud_setting` in method `init`
 - Client `CostManagementClient` added method `send_request`
 - Client `CostManagementClient` added operation group `budgets`
 - Client `CostManagementClient` added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

client = CostManagementClient(credential=DefaultAzureCredential())
```

...

</details>

### absurd-sdk

Python SDK for Absurd - PostgreSQL-based durable task execution

`pip install absurd-sdk` · installs (wheel) · licence: Apache-2.0 · rank 5549 · last release 2026-10-20 · [PyPI](https://pypi.org/project/absurd-sdk/) · [docs](https://github.com/earendil-works/absurd/tree/main/sdks/python) · [source](https://github.com/earendil-works/absurd)

<details><summary>README extract</summary>

Python SDK for Absurd: a
PostgreSQL-based durable task execution system.

Absurd is the simplest durable execution workflow system you can think of. It's
entirely based on Postgres and nothing else. ...

Example:
```python
from absurd_sdk import Absurd

app = Absurd("postgresql://localhost/absurd")

@app.register_task(name="order-fulfillment")
def process_order(params, ctx):
    step = ctx.run_step

    @step("process-payment")
    def payment():
        return {
            "payment_id": f"pay-{params['order_id']}",
            "amount": params["amount"],
        }
...
```

Sections: Absurd SDK for Python, What is Durable Execution?, Synchronous API, Asynchronous API, Using `@step` in synchronous tasks, Decomposed Steps, Spawning from a Separate Process, Task Result Snapshots

</details>

### azure-storage

Microsoft Azure Storage SDK for Python

`pip install azure-storage` · installs from source (sdist only) · licence: MIT License · rank 5557 · last release 2020-05-11 · [PyPI](https://pypi.org/project/azure-storage/)

<details><summary>README extract</summary>

This package was the Microsoft Azure Storage bundle.

Starting with v0.37.0, this package is deprecated. Please install the service specific packages prefixed by `azure-storage` needed for your application.

The complete list of available packages can be found at:

Here's a non-exhaustive list of common packages: ...

</details>

### aiohasupervisor

Asynchronous python client for Home Assistant Supervisor.

`pip install aiohasupervisor` · installs (wheel) · licence: Apache-2.0 · rank 5613 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aiohasupervisor/) · [source](https://github.com/home-assistant-libs/python-supervisor-client)

<details><summary>README extract</summary>

Python client for interfacing with the Home Assistant Supervisor
via its REST API.
Currently used in the Home Assistant Supervisor integration
in Home Assistant.

Add-ons which interface with Supervisor can also leverage it. ...

Example:
```python
client = SupervisorClient(unix_socket=Path(os.environ["SUPERVISOR_SOCKET"]))
```

Sections: Home Assistant Supervisor Client, Client Library for Home Assistant Supervisor, Prerequisites, Get the source code

</details>

### agentevals

Open-source evaluators for LLM agents

`pip install agentevals` · installs (wheel) · licence: MIT · rank 5617 · last release 2025-07-24 · [PyPI](https://pypi.org/project/agentevals/)

<details><summary>README extract</summary>

Agentic applications give an LLM freedom over control flow in order to solve problems. While this freedom
can be extremely powerful, the black box nature of LLMs can make it difficult to understand how changes in one part of your agent will affect others downstream.
This makes evaluating your agents especially important. ...

Example:
```python
from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

trajectory_evaluator = create_trajectory_llm_as_judge(
    prompt=TRAJECTORY_ACCURACY_PROMPT,
    model="openai:o3-mini",
)

# This is a fake trajectory, in reality you would run your agent to get a real trajectory
outputs = [
...
```

...

</details>

### argparse-dataclass

Declarative CLIs with argparse and dataclasses

`pip install argparse-dataclass` · installs (wheel) · licence: MIT License · rank 5661 · last release 2023-06-11 · [PyPI](https://pypi.org/project/argparse-dataclass/)

<details><summary>README extract</summary>

Declarative CLIs with `argparse` and `dataclasses`.

Features:
Features marked with a ✓ are currently implemented; features marked with a ⊘
are not yet implemented.

- [✓] Positional arguments
- [✓] Boolean flags
- [✓] Integer, string, float, and other simple types as arguments
- [✓] Default values ...

Example:
```python
>>> from argparse_dataclass import dataclass
>>> @dataclass
... class Options:
...     x: int = 42
...     y: bool = False
...
>>> print(Options.parse_args(['--y']))
Options(x=42, y=True)
```

Sections: `argparse_dataclass`, Features, Examples

</details>

### apispec-webframeworks

Web framework plugins for apispec.

`pip install apispec-webframeworks` · installs (wheel) · licence: MIT License · rank 5681 · last release 2024-09-16 · [PyPI](https://pypi.org/project/apispec-webframeworks/) · [source](https://github.com/marshmallow-code/apispec-webframeworks)

<details><summary>README extract</summary>

apispec plugins for
integrating with various web frameworks.

These plugins used to be in `apispec.ext` but have since
been moved to their own package.

Included plugins:

* `apispec_webframeworks.aiohttp`
* `apispec_webframeworks.bottle`
* `apispec_webframeworks.flask`
* `apispec_webframeworks.tornado` ...

Example:
```python
from flask import Flask
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

spec = APISpec(
    title="Gisty",
    version="1.0.0",
    info=dict(description="A minimal gist API"),
...
```

Sections: apispec-webframeworks, Migration from `apispec<1.0.0`, Example Usage, Documentation, Running tests

</details>

### aws_sdk_bedrock_runtime

aws_sdk_bedrock_runtime client

`pip install aws_sdk_bedrock_runtime` · installs (wheel) · licence: Apache Software License · rank 5694 · last release 2026-10-08 · [PyPI](https://pypi.org/project/aws_sdk_bedrock_runtime/)

<details><summary>README extract</summary>

The `aws-sdk-bedrock-runtime` package provides a client for making
requests to Amazon Bedrock Runtime.

> Note: This SDK is experimental and in early development. Breaking changes
> may occur prior to the release of version 1.0.0.

Sections: Amazon Bedrock Runtime Client, Documentation

</details>

### airbyte

PyAirbyte

`pip install airbyte` · does not install on CPython 3.14 · licence: not stated · rank 5712 · last release 2026-10-26 · [PyPI](https://pypi.org/project/airbyte/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> `main` is patches-only. The `release-candidate/v1` branch is the active trunk for new development.
> - New features and enhancements: branch from and target `release-candidate/v1`, not `main`. Only bug fixes and patches for the current release should target `main`. ...

Sections: PyAirbyte, Getting Started, Frequently asked Questions

</details>

### async-asgi-testclient

Async client for testing ASGI web applications

`pip install async-asgi-testclient` · installs from source (sdist only) · licence: MIT License · rank 5755 · last release 2022-06-13 · [PyPI](https://pypi.org/project/async-asgi-testclient/)

<details><summary>README extract</summary>

Async ASGI TestClient is a library for testing web applications that implements ASGI specification (version 2 and 3).

The motivation behind this project is building a common testing library that doesn't depend on the web framework (Quart, Startlette, ...).

It works by calling the ASGI app directly. ...

Example:
```python
from quart import Quart, jsonify

app = Quart(name)

@app.route("/")
async def root():
    return "plain response"

@app.route("/json")
async def json():
    return jsonify({"hello": "world"})

if name == 'main':
    app.run()
```

Sections: async-asgi-testclient, Quickstart, Usage

</details>

### a2ui-agent-sdk

A2UI Agent SDK

`pip install a2ui-agent-sdk` · installs (wheel) · licence: not stated · rank 5758 · last release 2026-11-02 · [PyPI](https://pypi.org/project/a2ui-agent-sdk/) · [source](https://github.com/a2ui-project/a2ui/tree/main/python/a2ui_agent)

<details><summary>README extract</summary>

The `python/a2ui_agent/src/a2ui` directory contains the Python implementation of
the A2UI agent SDK.

The following directories contain the base protocol logic, parsing, and schema operations directly under `src/a2ui/`: ...

Sections: A2UI Agent implementation, Core Components, Processor & Catalog Configuration (`src/a2ui/processor`), Constants (`src/a2ui/constants.py`), Catalog transformers (`src/a2ui/catalog_transformers`), Utilities (`src/a2ui/utils`), Parser (`src/a2ui/parser`), Agent framework integrations, Running tests, Building the SDK, Regenerating the Express parser, Formatting code, Releasing the SDK, Disclaimer

</details>

### adbc-driver-flightsql

An ADBC driver for working with Apache Arrow Flight SQL.

`pip install adbc-driver-flightsql` · installs (wheel) · licence: Apache-2.0 · rank 5771 · last release 2026-10-26 · [PyPI](https://pypi.org/project/adbc-driver-flightsql/) · [source](https://github.com/apache/arrow-adbc)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Sections: ADBC Apache Arrow Flight SQL Driver for Python, Building

</details>

### ai21

(no summary)

`pip install ai21` · installs (wheel) · licence: not stated · rank 5831 · last release 2025-11-06 · [PyPI](https://pypi.org/project/ai21/)

<details><summary>README extract</summary>

Example:
```python
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

client = AI21Client(
    # defaults to os.enviorn.get('AI21_API_KEY')
    api_key='my_api_key',
)

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
...
```

Sections: AI21 Labs Python SDK, Examples (tl;dr), Check out the Examples, Documentation, Usage, Async Usage, Chat, Completion, Chat Completion, Streaming, Async Streaming, Maestro, Agents (Beta), Agent CRUD Operations

</details>

### azure-eventhub-checkpointstoreblob-aio

Microsoft Azure Event Hubs checkpointer implementation with Blob Storage Client Library for Python

`pip install azure-eventhub-checkpointstoreblob-aio` · installs (wheel) · licence: MIT License · rank 5852 · last release 2025-02-13 · [PyPI](https://pypi.org/project/azure-eventhub-checkpointstoreblob-aio/)

<details><summary>README extract</summary>

Azure EventHubs Checkpoint Store is used for storing checkpoints while processing events from Azure Event Hubs.
This Checkpoint Store package works as a plug-in package to `EventHubConsumerClient`. It uses Azure Storage Blob as the persistent store for maintaining checkpoints and partition ownership information. ...

Example:
```python
from azure.eventhub.aio import EventHubConsumerClient
eventhub_client = EventHubConsumerClient.from_connection_string("my_eventhub_namespace_connection_string", "my_consumer_group", eventhub_name="my_eventhub")
```

Sections: _Disclaimer_, Getting started, Prerequisites, Key concepts, Checkpointing, Offsets & sequence numbers, Examples, Create an `EventHubConsumerClient`, Troubleshooting, General, Logging, Next steps, More sample code, Documentation

</details>

### aioshutil

Asynchronous shutil module.

`pip install aioshutil` · installs (wheel) · licence: BSD License · rank 5904 · last release 2025-10-21 · [PyPI](https://pypi.org/project/aioshutil/)

<details><summary>README extract</summary>

`aioshutil` is a Python library which provides asynchronous version of function of shutil module. `shutil` module is blocking and using it in asyncio applications will block the event loop and slow down the application, `aioshutil` provides asynchronous friendly versions of the functions of the `shutil` module as it performs blocking io in a ...

Example:
```python
from aioshutil import rmtree
await rmtree("/tmp")
```

Sections: aioshutil: Asynchronous shutil module., Introduction, Usage

</details>

### appengine-python-standard

Google App Engine services SDK for Python 3

`pip install appengine-python-standard` · installs (wheel) · licence: MIT License · rank 5924 · last release 2026-10-16 · [PyPI](https://pypi.org/project/appengine-python-standard/)

<details><summary>README extract</summary>

This is a release of the App Engine services SDK for Python 3. It provides access to various services and API endpoints that were previously only available on the Python 2.7 runtime.

See the documentation to learn more about using this SDK, and learn more about it in this product announcement (Fall 2021). ...

Sections: Google App Engine bundled services SDK for Python 3, Using the SDK

</details>

### azure-mgmt-databricks

Microsoft Azure Databricks Management Client Library for Python

`pip install azure-mgmt-databricks` · installs (wheel) · licence: MIT · rank 5975 · last release 2026-07-08 · [PyPI](https://pypi.org/project/azure-mgmt-databricks/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Bricks Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `AzureDatabricksManagementClient` added parameter `cloud_setting` in method `init`
 - Client `AzureDatabricksManagementClient` added method `send_request`
 - Model `AccessConnectorProperties` added property `refered_by`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.databricks import AzureDatabricksManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### attrdict

A dict with attribute-style access

`pip install attrdict` · installs (wheel) · licence: MIT License · rank 6002 · last release 2019-02-01 · [PyPI](https://pypi.org/project/attrdict/)

<details><summary>README extract</summary>

AttrDict is an MIT-licensed library that provides mapping objects that allow
their elements to be accessed both as keys and as attributes:
Attribute access makes it easy to create convenient, hierarchical settings
objects:

Example:
```python
> from attrdict import AttrDict
> a = AttrDict({'foo': 'bar'})
> a.foo
'bar'
> a['foo']
'bar'
```

Sections: AttrDict, Basic Usage, Valid Names, . The key does not shadow a class attribute (e.g., get)., Attributes vs. Keys, Classes, AttrMap, AttrDefault, Merging, Sequences

</details>

### azure-storage-nspkg

Microsoft Azure Storage Namespace Package [Internal]

`pip install azure-storage-nspkg` · installs (wheel) · licence: MIT License · rank 6035 · last release 2018-11-10 · [PyPI](https://pypi.org/project/azure-storage-nspkg/)

<details><summary>README extract</summary>

This is the Microsoft Azure Storage namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.storage namespace.

If you are looking to install the Azure Storage libraries, see the
azure bundle package.

</details>

### adbc-driver-sqlite

An ADBC driver for working with SQLite.

`pip install adbc-driver-sqlite` · installs (wheel) · licence: Apache-2.0 · rank 6050 · last release 2026-10-26 · [PyPI](https://pypi.org/project/adbc-driver-sqlite/) · [source](https://github.com/apache/arrow-adbc)

<details><summary>README extract</summary>

<!---
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements. See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership. ...

Example:
```python
import adbc_driver_sqlite.dbapi

with adbc_driver_sqlite.dbapi.connect() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        print(cur.fetch_arrow_table())
```

Sections: ADBC SQLite Driver for Python, Example, Building

</details>

### az.cli

An interface to execute Azure CLI commands using Python

`pip install az.cli` · installs (wheel) · licence: MIT License · rank 6053 · last release 2021-03-14 · [PyPI](https://pypi.org/project/az.cli/)

<details><summary>README extract</summary>

Python azure.cli.core interface to execute `az` Azure CLI commands in python.

The method returns a named tuple `AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])`. The `error_code` where 0 == success. A `result_dict` containing successfull return as a python dictionary. ...

Example:
```python
from az.cli import az

# AzResult = namedtuple('AzResult', ['exit_code', 'result_dict', 'log'])
exit_code, result_dict, logs = az("group show -n test")

# On 0 (SUCCESS) print result_dict, otherwise get info from `logs`
if exit_code == 0:
    print (result_dict)
else:
    print(logs)
```

Sections: Az.Cli, Usage, Example, Interactive, Build, Docker, Run

</details>

### azure-ai-agentserver-responses

Python SDK for building servers implementing the Azure AI Responses protocol

`pip install azure-ai-agentserver-responses` · installs (wheel) · licence: MIT · rank 6060 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-ai-agentserver-responses/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

The `azure-ai-agentserver-responses` package provides the Responses protocol endpoints for Azure AI Hosted Agent containers. It plugs into the `azure-ai-agentserver-core` host framework and adds the full response lifecycle: create, stream (SSE), cancel, delete, replay, and input-item listing.

Example:
```python
@app.response_handler
async def my_handler(request: CreateResponse, context: ResponseContext, cancellation_signal: asyncio.Event):
    ...
```

Sections: Azure AI Agent Server Responses client library for Python, Getting started, Prerequisites, Key concepts, ResponsesAgentServerHost, User isolation and response identifiers, TextResponse, ResponseEventStream, ResponseContext, Streaming and background modes, Telemetry flushing, Response lifecycle, Resilience, Examples

</details>

### autogen-core

Foundational interfaces and agent runtime implementation for AutoGen

`pip install autogen-core` · installs (wheel) · licence: MIT License · rank 6081 · last release 2025-09-30 · [PyPI](https://pypi.org/project/autogen-core/)

<details><summary>README extract</summary>

- Documentation

AutoGen core offers an easy way to quickly build event-driven, distributed, scalable, resilient AI agent systems. Agents are developed by using the Actor model. You can build and run your agent system locally and easily move to a distributed system in the cloud when you are ready.

</details>

### azure-mgmt-dataprotection

Microsoft Azure Dataprotection Management Client Library for Python

`pip install azure-mgmt-dataprotection` · installs (wheel) · licence: MIT · rank 6088 · last release 2026-09-07 · [PyPI](https://pypi.org/project/azure-mgmt-dataprotection/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Protection Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `BackupVault` added property `cost_management_settings`
 - Model `DeletedBackupVault` added property `cost_management_settings`
 - Model `PatchBackupVaultInput` added property `cost_management_settings`
 - Added model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### AlexaPy

Python API to control Amazon Echo Devices Programmatically.

`pip install AlexaPy` · installs (wheel) · licence: Apache Software License · rank 6094 · last release 2026-11-01 · [PyPI](https://pypi.org/project/AlexaPy/) · [source](https://gitlab.com/keatontaylor/alexapy)

<details><summary>README extract</summary>

Python Package for controlling Alexa devices (echo dot, etc) programmatically. This was originally designed for alexa_media_player a custom_component for Home Assistant.

NOTE: Alexa has no official API; therefore, this library may stop
working at any time without warning.

Sections: alexapy, API Reference

</details>

### asyncmy2

A fast asyncio MySQL driver

`pip install asyncmy2` · installs (wheel) · licence: Apache-2.0 · rank 6130 · last release 2026-08-02 · [PyPI](https://pypi.org/project/asyncmy2/) · [docs](https://github.com/vpmedia/asyncmy2) · [source](https://github.com/vpmedia/asyncmy2.git)

<details><summary>README extract</summary>

`asyncmy` is a fast asyncio MySQL/MariaDB driver, which reuse most of pymysql
and aiomysql but rewrite core protocol with cython to
speedup.

This project is a community maintained fork of

Features:
- API compatible with aiomysql.
- Faster by cython.
- MySQL replication protocol support with `asyncio`.
- Tested both MySQL and MariaDB in CI.

Example:
```python
import asyncio
import os

from asyncmy import connect
from asyncmy.cursors import DictCursor

async def run():
    conn = await connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD", ""))
    async with conn.cursor(cursor=DictCursor) as cursor:
        await cursor.execute("CREATE DATABASE IF NOT EXISTS test")
...
```

...

</details>

### a2ui-core

A2UI Python SDK - Core Library

`pip install a2ui-core` · installs (wheel) · licence: not stated · rank 6139 · last release 2026-11-02 · [PyPI](https://pypi.org/project/a2ui-core/) · [source](https://github.com/a2ui-project/a2ui/tree/main/python/a2ui_core)

<details><summary>README extract</summary>

`a2ui_core` is a framework-agnostic Python library containing the core data models, reactive state management, and JSON schema validation logic for the A2UI protocol (v0.9 and onwards).

It provides the logic-neutral, visual-agnostic layer used by python-based server agents, rendering backends, and conformance testing frameworks.

Features:
- Protocol Handling: Symmetrical processing and validation of A2UI specification envelope messages (`CreateSurface`, `UpdateComponents`, `UpdateDataModel`, and `DeleteSurface`). ...

...

</details>

### aws-cdk.aws-glue-alpha

This module is deprecated. All constructs are now available under aws-cdk-lib/aws-glue

`pip install aws-cdk.aws-glue-alpha` · installs (wheel) · licence: OSI Approved · rank 6169 · last release 2026-10-20 · [PyPI](https://pypi.org/project/aws-cdk.aws-glue-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> This API may emit warnings. Backward compatibility is not guaranteed.

<!--END STABILITY BANNER-->

All constructs moved to aws-cdk-lib/aws-glue.

This module is part of the AWS Cloud Development Kit project. ...

Features:
Developers should use this Construct to reduce the amount of boilerplate
code and complexity each individual has to navigate, and make it easier to
create best-practice Glue resources.

Example:
```python
import aws_cdk as cdk
import aws_cdk.aws_iam as iam
# stack: cdk.Stack
# role: iam.IRole
# script: glue.Code

glue.PySparkEtlJob(stack, "PySparkETLJob",
    role=role,
    script=script,
    job_name="PySparkETLJob"
)
```

...

</details>

### azure-mgmt-automation

Microsoft Azure Automation Management Client Library for Python

`pip install azure-mgmt-automation` · installs (wheel) · licence: MIT · rank 6213 · last release 2026-07-29 · [PyPI](https://pypi.org/project/azure-mgmt-automation/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Automation Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `AutomationClient` added parameter `api_version` in method `init`
 - Client `AutomationClient` added method `convert_graph_runbook_content`
 - Client `AutomationClient` added method `send_request`
 - Client `AutomationClient` added ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.automation import AutomationClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### argostranslate

Open-source neural machine translation library based on OpenNMT's CTranslate2

`pip install argostranslate` · installs (wheel) · licence: MIT License · rank 6302 · last release 2026-02-02 · [PyPI](https://pypi.org/project/argostranslate/) · [docs](https://argos-translate.readthedocs.io/en/latest/) · [source](https://github.com/argosopentech/argos-translate)

<details><summary>README extract</summary>

Demo | Website | Docs | Forum | GitHub | PyPI

Open-source offline translation library written in Python

Argos Translate uses OpenNMT for translations and can be used as either a Python library, command-line, or GUI application. ...

Example:
```python
import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "es"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
...
```

...

</details>

### autogen-agentchat

AutoGen agents and teams library

`pip install autogen-agentchat` · installs (wheel) · licence: MIT License · rank 6318 · last release 2025-09-30 · [PyPI](https://pypi.org/project/autogen-agentchat/)

<details><summary>README extract</summary>

- Documentation

AgentChat is a high-level API for building multi-agent applications.
It is built on top of the `autogen-core` package.
For beginner users, AgentChat is the recommended starting point.
For advanced users, `autogen-core`'s event-driven
programming model provides more flexibility and control over the underlying components. ...

</details>

### alt-profanity-check

A fast, robust library to check for offensive language in strings. Dropdown replacement of "profanity-check".

`pip install alt-profanity-check` · installs (wheel) · licence: MIT License · rank 6364 · last release 2026-09-14 · [PyPI](https://pypi.org/project/alt-profanity-check/)

<details><summary>README extract</summary>

Alt profanity check is a drop-in replacement of the `profanity-check` library for the not so well
maintained <

> A fast, robust Python library to check for profanity or offensive language in strings.
> Read more about how and why `profanity-check` was built in
> this blog post. ...

Example:
```python
from profanity_check import predict, predict_prob

predict(['predict() takes an array and returns a 1 for each string if it is offensive, else 0.'])
# [0]

predict(['fuck you'])
# [1]

predict_prob(['predict_prob() takes an array and returns the probability each string is offensive'])
# [0.08686173]

predict_prob(['go to hell, you scum'])
...
```

...

</details>

### aws-mfa-v2

Manage AWS MFA Security Credentials

`pip install aws-mfa-v2` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6371 · last release 2024-03-04 · [PyPI](https://pypi.org/project/aws-mfa-v2/) · [source](https://github.com/rkeiii/aws-mfa-v2)

_README extract left out: share-alike licence._

### asyncpg-trek

A simple migrations system for asyncpg

`pip install asyncpg-trek` · installs (wheel) · licence: MIT License · rank 6415 · last release 2024-07-19 · [PyPI](https://pypi.org/project/asyncpg-trek/) · [docs](https://github.com/adriangb/asyncpg-trek) · [source](https://github.com/adriangb/asyncpg-trek)

<details><summary>README extract</summary>

A simple library for managing migrations.

Me.
But maybe if you use [asyncpg] and prefer to write migrations as raw SQL (i.e. you're not using SQLAlchemy/Alembic) then you as well.

Features:
- async: migrations usually don't benefit from being async, but you benefit from using the same database driver in as your application uses (only [asyncpg] is supported). ...

Example:
```python
from pathlib import Path

import asyncpg
from asyncpg_trek import plan, execute, Direction
from asyncpg_trek.asyncpg import AsyncpgBackend

MIGRATIONS_DIR = Path(file).parent / "migrations"

async def migrate(
    conn: asyncpg.Connection,
    target_revision: str,
) -> None:
    backend = AsyncpgBackend(conn)
...
```

...

</details>

### agent-framework-orchestrations

Orchestration patterns for Microsoft Agent Framework. Includes SequentialBuilder, ConcurrentBuilder, HandoffBuilder, GroupChatBuilder, and MagenticBuilder.

`pip install agent-framework-orchestrations` · installs (wheel) · licence: MIT License · rank 6449 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-orchestrations/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_orchestrations)

<details><summary>README extract</summary>

Orchestration patterns for Microsoft Agent Framework. This package provides high-level builders for common multi-agent workflow patterns.

Example:
```python
from agent_framework.orchestrations import SequentialBuilder

workflow = SequentialBuilder(participants=[agent1, agent2, agent3]).build()

# Preserve agent1 and agent2 as visible progress, while the default builder output remains Workflow Output.
workflow = SequentialBuilder(
    participants=[agent1, agent2, agent3],
...
```

Sections: Agent Framework Orchestrations, Orchestration Patterns, SequentialBuilder, ConcurrentBuilder, HandoffBuilder, GroupChatBuilder, MagenticBuilder, Output Selection, Documentation

</details>

### aws-cdk.asset-node-proxy-agent-v5

@aws-cdk/asset-node-proxy-agent-v5

`pip install aws-cdk.asset-node-proxy-agent-v5` · installs (wheel) · licence: OSI Approved · rank 6452 · last release 2023-07-20 · [PyPI](https://pypi.org/project/aws-cdk.asset-node-proxy-agent-v5/) · [source](https://github.com/cdklabs/awscdk-asset-node-proxy-agent.git)

### ase-db-backends

ASE-DB backends

`pip install ase-db-backends` · installs (wheel) · licence: not stated · rank 6469 · last release 2025-11-12 · [PyPI](https://pypi.org/project/ase-db-backends/)

### awslabs.aws-api-mcp-server

Model Context Protocol (MCP) server for interacting with AWS

`pip install awslabs.aws-api-mcp-server` · installs (wheel) · licence: Apache Software License · rank 6508 · last release 2026-10-27 · [PyPI](https://pypi.org/project/awslabs.aws-api-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/aws-api-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

> [!TIP]
> This MCP server is superseded by the official AWS MCP server. Check out the migration guide on how to move your configuration over!

Features:
The AWS API MCP Server enables AI assistants to interact with AWS services and resources through AWS CLI commands. It provides programmatic access to manage your AWS infrastructure while maintaining proper security controls. ...

Sections: AWS API MCP Server, Overview, Prerequisites, ⚡ Using uv, 🐍 Using Python (pip), 🐳 Using Docker, 🔧 Using Cloned Repository, 🌐 HTTP Mode Configuration, For Linux/macOS, For Windows (Command Prompt), For Windows (PowerShell), 🏗️ Self-host on AgentCore Runtime, ⚙️ Configuration Options, 🚀 Quick Start

</details>

### azure-mgmt-securityinsight

Microsoft Azure Security Insight Management Client Library for Python

`pip install azure-mgmt-securityinsight` · installs (wheel) · licence: MIT License · rank 6530 · last release 2022-07-26 · [PyPI](https://pypi.org/project/azure-mgmt-securityinsight/)

<details><summary>README extract</summary>

This is the Microsoft Azure Security Insight Management Client Library.
This package has been tested with Python 3.6+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 1.0.0 (2022-07-26), 1.0.0b2 (2022-03-30), 1.0.0b1 (2020-11-10)

</details>

### apache-superset

A modern, enterprise-ready business intelligence web application

`pip install apache-superset` · installs (wheel) · licence: not stated · rank 6550 · last release 2026-05-13 · [PyPI](https://pypi.org/project/apache-superset/) · [docs](https://superset.apache.org/docs/intro)

<details><summary>README extract</summary>

A modern, enterprise-ready business intelligence web application.

- User Guide — For analysts and business users. Explore data, build charts, create dashboards, and connect databases.
- Administrator Guide — Install, configure, and operate Superset. Covers security, scaling, and database drivers. ...

Features:
Superset is a modern data exploration and data visualization platform. Superset can replace or augment proprietary business intelligence tools for many teams. Superset integrates well with a variety of data sources.

Superset provides: ...

Sections: Superset, Documentation, Why Superset?, Screenshots & Gifs, Get Involved, Resources, Repo Activity

</details>

### awacs

AWS Access Policy Language creation library

`pip install awacs` · installs (wheel) · licence: BSD License · rank 6661 · last release 2026-10-20 · [PyPI](https://pypi.org/project/awacs/) · [source](https://github.com/cloudtools/awacs)

<details><summary>README extract</summary>

awacs - Amazon Web Access Control Subsystem

The awacs library allows for easier creation of AWS Access Policy
Language JSON by writing Python code to describe the AWS policies.
To facilitate catching policy format or JSON errors early the
library has property and type checking built into the classes. ...

Example:
```python
from awacs.aws import Action, Allow, PolicyDocument, Principal, Statement
from awacs.iam import ARN as IAM_ARN
from awacs.s3  import ARN as S3_ARN

account = "123456789012"
user = "user/Bob"

pd = PolicyDocument(
    Version="2012-10-17",
    Id="S3-Account-Permissions",
    Statement=[
        Statement(
            Sid="1",
...
```

Sections: awacs, About, Examples

</details>

### arnparse

Parse ARNs using Python

`pip install arnparse` · installs (wheel) · licence: not stated · rank 6665 · last release 2019-03-12 · [PyPI](https://pypi.org/project/arnparse/)

<details><summary>README extract</summary>

Parse ARNs using Python

Motivation

Sometimes, you want to parse an Amazon Resource Name (ARN) into its
components to get some useful information from the ARN (e.g. AWS region,
account ID, etc).

You can find documentation on ARNs and their components here:

Installation

`pip install arnparse`

Examples

Example:
```python
from arnparse import arnparse

arn = arnparse('arn:aws:s3:::my_corporate_bucket/exampleobject.png')

assert arn.partition == 'aws'
assert arn.service == 's3'
assert arn.region is None
assert arn.account_id is None
assert arn.resource_type is None
assert arn.resource == 'my_corporate_bucket/exampleobject.png'
```

Sections: arnparse, S3 Object, VPC, CloudWatch Alarm, SNS Topic, API Gateway

</details>

### adb-shell

A Python implementation of ADB with shell and FileSync functionality.

`pip install adb-shell` · installs from source (sdist only) · licence: Apache Software License · rank 6693 · last release 2023-09-01 · [PyPI](https://pypi.org/project/adb-shell/)

<details><summary>README extract</summary>

Documentation for this package can be found at

Prebuilt wheel can be downloaded from nightly.link.

This Python package implements ADB shell and FileSync functionality. It originated from python-adb.

Example:
```python
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

# Load the public and private keys
adbkey = 'path/to/adbkey'
with open(adbkey) as f:
    priv = f.read()
with open(adbkey + '.pub') as f:
     pub = f.read()
signer = PythonRSASigner(pub, priv)

# Connect
...
```

Sections: adb\_shell, Async, Example Usage, Generate ADB Key Files

</details>

### agent-framework-ag-ui

AG-UI protocol integration for Agent Framework

`pip install agent-framework-ag-ui` · installs (wheel) · licence: MIT License · rank 6734 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-ag-ui/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

AG-UI protocol integration for Agent Framework, enabling seamless integration with AG-UI's web interface and streaming protocol.

Features:
This integration supports all 7 AG-UI features:

1. Agentic Chat: Basic streaming chat with tool calling support
2. Backend Tool Rendering: Tools executed on backend with results streamed to client
3. ...

Example:
```python
import os
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
from agent_framework import Agent
from agent_framework.ag_ui import add_agent_framework_fastapi_endpoint

# Configure API key authentication
API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)
...
```

...

</details>

### azure-mgmt-databoxedge

Microsoft Azure Databoxedge Management Client Library for Python

`pip install azure-mgmt-databoxedge` · installs (wheel) · licence: MIT · rank 6749 · last release 2026-07-14 · [PyPI](https://pypi.org/project/azure-mgmt-databoxedge/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Data Box Edge Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `DataBoxEdgeManagementClient` added parameter `cloud_setting` in method `init`
 - Client `DataBoxEdgeManagementClient` added method `send_request`
 - Client `DataBoxEdgeManagementClient` added operation group `device_capacity_check`
 - ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.databoxedge import DataBoxEdgeManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### aiodebug

A tiny library for monitoring and testing asyncio programs

`pip install aiodebug` · installs (wheel) · licence: Apache Software License · rank 6784 · last release 2022-01-04 · [PyPI](https://pypi.org/project/aiodebug/)

<details><summary>README extract</summary>

This is a tiny library for monitoring and testing asyncio programs.
Its monitoring features are meant to be always on in production.

Example:
```python
import aiodebug.log_slow_callbacks

aiodebug.log_slow_callbacks.enable(0.05)
```

Sections: aiodebug, Log warnings when callbacks block the event loop, Track event loop lags in StatsD, Speed up or slow down time in the event loop

</details>

### aiomonitor

Adds monitor and Python REPL capabilities for asyncio applications

`pip install aiomonitor` · installs (wheel) · licence: Apache Software License · rank 6827 · last release 2024-11-11 · [PyPI](https://pypi.org/project/aiomonitor/) · [docs](https://aiomonitor.readthedocs.io) · [source](https://github.com/aio-libs/aiomonitor)

<details><summary>README extract</summary>

aiomonitor is a module that adds monitor and cli capabilities
for asyncio applications. Idea and code were borrowed from curio project.
Task monitor that runs concurrently to the asyncio loop (or fast drop-in
replacement uvloop) in a separate thread as result monitor will work even if
the event loop is blocked for some reason. ...

Example:
```python
import aiomonitor

async def main():
    loop = asyncio.get_running_loop()
    run_forever = loop.create_future()
    with aiomonitor.start_monitor(loop):
        await run_forever

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```

...

</details>

### agent-framework-anthropic

Anthropic integration for Microsoft Agent Framework.

`pip install agent-framework-anthropic` · installs (wheel) · licence: MIT License · rank 6838 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-anthropic/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_anthropic)

<details><summary>README extract</summary>

Please install this package via pip:

The Anthropic integration enables communication with the Anthropic API, allowing your Agent Framework applications to leverage Anthropic's capabilities.

The package also includes Anthropic-hosted transport wrappers for:

- Microsoft Foundry via `AnthropicFoundryClient` ...

Example:
```python
from anthropic.types.beta import BetaTextBlockParam

from agent_framework_anthropic import AnthropicClient

client = AnthropicClient()
system_blocks: list[BetaTextBlockParam] = [
    {"type": "text", "text": "Stable instructions", "cache_control": {"type": "ephemeral", "ttl": "1h"}},
]

...
```

...

</details>

### aliyun-log-python-sdk

Aliyun log service Python client SDK

`pip install aliyun-log-python-sdk` · installs from source (sdist only) · licence: MIT License · rank 6881 · last release 2026-11-02 · [PyPI](https://pypi.org/project/aliyun-log-python-sdk/)

### azure-communication-identity

Microsoft Azure Communication Identity Service Client Library for Python

`pip install azure-communication-identity` · installs (wheel) · licence: MIT License · rank 6885 · last release 2024-02-15 · [PyPI](https://pypi.org/project/azure-communication-identity/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure Communication Identity client package is intended to be used to setup the basics for opening a way to use Azure Communication Service offerings. This package helps to create identity user tokens to be used by other client packages such as chat, calling, sms. ...

Example:
```python
# You can find your endpoint and access token from your resource in the Azure Portal
import os
from azure.communication.identity import CommunicationIdentityClient
from azure.identity import DefaultAzureCredential

connection_str = "endpoint=ENDPOINT;accessKey=KEY"
endpoint = "

...
```

...

</details>

### airflow-clickhouse-plugin

airflow-clickhouse-plugin — Airflow plugin to execute ClickHouse commands and queries

`pip install airflow-clickhouse-plugin` · installs (wheel) · licence: MIT License · rank 6955 · last release 2026-07-13 · [PyPI](https://pypi.org/project/airflow-clickhouse-plugin/) · [docs](https://github.com/bryzgaloff/airflow-clickhouse-plugin#airflow-clickhouse-plugin) · [source](https://github.com/bryzgaloff/airflow-clickhouse-plugin)

<details><summary>README extract</summary>

🔝 The most popular Apache Airflow plugin for ClickHouse, ranked in the top 1% of downloads on PyPI. Based on awesome mymarilyn/clickhouse-driver.

> 💡 Need expert help with Airflow, ClickHouse, or Data Engineering?
> As the creator of this plugin, I offer 1-on-1 technical consultations and data platform architecture design. ...

Features:
- SQL Templating: SQL queries and other parameters are templated.
- Multiple SQL Queries: execute run multiple SQL queries within a single `ClickHouseOperator`. The result of the last query is pushed to XCom (configurable by `do_xcom_push`). ...

Example:
```python
from airflow import DAG
from airflow_clickhouse_plugin.operators.clickhouse import ClickHouseOperator
from airflow.operators.python import PythonOperator
...

</details>

### arn

A Python library for parsing AWS ARNs

`pip install arn` · installs (wheel) · licence: not stated · rank 6987 · last release 2021-03-05 · [PyPI](https://pypi.org/project/arn/)

<details><summary>README extract</summary>

A Python library for parsing AWS ARNs.

Example:
```python
from arn.elbv2 import TargetGroupArn

target_group_arn_str = "arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/foo-bar/abc123"
target_group_arn = TargetGroupArn(target_group_arn_str)

# use the ARN instance's str to format the ARN back into a string
assert str(target_group_arn) == target_group_arn_str

# common attributes
...
```

Sections: arn, Usage

</details>

### autogen-ext

AutoGen extensions library

`pip install autogen-ext` · installs (wheel) · licence: MIT License · rank 6999 · last release 2025-09-30 · [PyPI](https://pypi.org/project/autogen-ext/)

<details><summary>README extract</summary>

- Documentation

AutoGen is designed to be extensible. The `autogen-ext` package contains many different component implementations maintained by the AutoGen project. However, we strongly encourage others to build their own components and publish them as part of the ecosytem.

</details>

### altcha

A library for creating and verifying challenges for ALTCHA.

`pip install altcha` · installs (wheel) · licence: MIT License · rank 7084 · last release 2026-10-04 · [PyPI](https://pypi.org/project/altcha/)

<details><summary>README extract</summary>

The ALTCHA Python Library is a lightweight, zero-dependency library designed for creating and verifying ALTCHA challenges, specifically tailored for Python applications.

- Python 3.9+

Example:
```python
from altcha import (
    create_challenge,
    solve_challenge,
    verify_solution,
    Payload,
)

HMAC_SECRET = "secret hmac key"

# Server: create a challenge
challenge = create_challenge(
    algorithm="PBKDF2/SHA-256",
    cost=5_000,
    hmac_secret=HMAC_SECRET,
)

# Client: solve the challenge
solution = solve_challenge(challenge)
...
```

Sections: ALTCHA Python Library, Compatibility, Example, Tests, PoW v2, Algorithms, Quick start, Deterministic mode, Expiry, Custom derive_key, PoW v1 (legacy), API reference, V2, Built-in derive_key functions

</details>

### azure-mgmt-kusto

Microsoft Azure Kusto Management Client Library for Python

`pip install azure-mgmt-kusto` · installs (wheel) · licence: MIT · rank 7148 · last release 2026-06-24 · [PyPI](https://pypi.org/project/azure-mgmt-kusto/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Kusto Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `KustoManagementClient` added parameter `cloud_setting` in method `init`
 - Client `KustoManagementClient` added method `send_request`
 - Model `AttachedDatabaseConfiguration` added property `system_data`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.kusto import KustoManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### asknews

Python SDK for AskNews

`pip install asknews` · installs (wheel) · licence: MIT · rank 7169 · last release 2026-11-07 · [PyPI](https://pypi.org/project/asknews/) · [source](https://github.com/emergentmethods/asknews-python-sdk)

<details><summary>README extract</summary>

Python SDK for the AskNews API.

Example:
```python
from asknews_sdk import AskNewsSDK

ask = AskNewsSDK(
    api_key="<YOUR API KEY>",
    scopes=["news", "chat", "stories", "analytics"]
)

query = "NVIDIA earnings"

# Fast lookup: prompt-optimized news context for your LLM.
news_context = ask.news.search_news(query).as_string

# Iterative discovery across news and other sources.
...
```

Sections: AskNews Python SDK, Usage

</details>

### awsglue-dev

Python interfaces to the AWS Glue ETL library for use as a local dependency.

`pip install awsglue-dev` · installs (wheel) · licence: not stated · rank 7180 · last release 2021-12-30 · [PyPI](https://pypi.org/project/awsglue-dev/)

<details><summary>README extract</summary>

This repository contains libraries used in the AWS Glue service. These libraries extend Apache Spark with additional data types and operations for ETL workflows. They are used in code generated by the AWS Glue service and can be used in scripts submitted with Glue jobs. ...

Sections: aws-glue-libs, Content, Licensing

</details>

### apswutils

A fork of sqlite-minutils for apsw

`pip install apswutils` · installs (wheel) · licence: Apache Software License · rank 7198 · last release 2025-12-18 · [PyPI](https://pypi.org/project/apswutils/)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

> [!TIP]
> ### Where to find the complete documentation for this library
> If you want to learn about everything this project can do, we
> recommend reading the Python library section of the sqlite-utils
> project
> here. ...

Example:
```python
from apswutils.db import *
```

Sections: apswutils, Use, Queries, Transactions, Differences from sqlite-utils and sqlite-minutils, Differences in error handling, Handling of default values

</details>

### awslabs.aws-documentation-mcp-server

An AWS Labs Model Context Protocol (MCP) server for AWS Documentation

`pip install awslabs.aws-documentation-mcp-server` · installs (wheel) · licence: Apache Software License · rank 7246 · last release 2026-10-30 · [PyPI](https://pypi.org/project/awslabs.aws-documentation-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

Model Context Protocol (MCP) server for AWS Documentation

This MCP server provides tools to access AWS documentation, search for content, and get recommendations.

Features:
- Read Documentation: Fetch and convert AWS documentation pages to markdown format
- Search Documentation: Search AWS documentation using the official search API (global only) ...

Example:
```python
read_documentation(url: str) -> str
```

Sections: AWS Documentation MCP Server, Features, Prerequisites, Environment Variables, Basic Usage, Tools, read_documentation, search_documentation (global only), read_sections (global only), search_table (global only), recommend (global only), get_available_services (China only), Running tests

</details>

### aiometer

A Python concurrency scheduling library, compatible with asyncio and trio

`pip install aiometer` · installs (wheel) · licence: MIT · rank 7262 · last release 2025-04-04 · [PyPI](https://pypi.org/project/aiometer/)

<details><summary>README extract</summary>

`aiometer` is a concurrency scheduling library compatible with `asyncio` and `trio` and inspired by Trimeter. It makes it easier to execute lots of tasks concurrently while controlling concurrency limits (i.e. applying _backpressure_) and collecting results in a predictable manner.

Content

- Example
- Features
- Installation ...

Features:
- Concurrency management and throttling helpers.
- `asyncio` and `trio` support.
- Fully type annotated.
- 100% test coverage.

Example:
```python
>>> import asyncio
>>> import functools
>>> import random
>>> import aiometer
>>> import httpx
>>>
>>> client = httpx.AsyncClient()
>>>
>>> async def fetch(client, request):
...     response = await client.send(request)
...     # Simulate extra processing...
...     await asyncio.sleep(2 * random.random())
...

</details>

### aws-cdk.aws-redshift-alpha

The CDK Construct Library for AWS::Redshift

`pip install aws-cdk.aws-redshift-alpha` · installs (wheel) · licence: OSI Approved · rank 7263 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-redshift-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
from aws_cdk.aws_redshift_alpha import Login
import aws_cdk.aws_ec2 as ec2

vpc = ec2.Vpc(self, "Vpc")
cluster = Cluster(self, "Redshift",
    master_user=Login(
        master_username="admin"
    ),
    vpc=vpc
)
```

...

</details>

### agent-framework-foundry-hosting

Foundry Hosting integration for Microsoft Agent Framework.

`pip install agent-framework-foundry-hosting` · installs (wheel) · licence: MIT License · rank 7314 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-foundry-hosting/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_foundry_hosting)

<details><summary>README extract</summary>

This package provides the integration of Agent Framework agents and workflows with the Foundry Agent Server, which can be hosted on Foundry infrastructure.

`FoundryToolbox` uses each discovered tool's `_meta.tool_configuration.require_approval` when
`approval_mode` is omitted or `None`. ...

Example:
```python
server = ResponsesHostServer(agent=create_agent)
```

Sections: Foundry Hosting, Toolbox tool approvals, Agent instances and factories, Hosting a `WorkflowAgent` is deprecated, Native Responses workflows, OAuth consent origin allowlist, Computer use, State store, Local persistence, User isolation, Agent Sessions, Invocations agent requests and wire compatibility, Workflow checkpoints, Function approvals

</details>

### agent-framework-a2a

A2A integration for Microsoft Agent Framework.

`pip install agent-framework-a2a` · installs (wheel) · licence: MIT License · rank 7373 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-a2a/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_a2a)

<details><summary>README extract</summary>

Please install this package via pip:

The A2A agent integration enables communication with remote A2A-compliant agents using the standardized A2A protocol. This allows your Agent Framework applications to connect to agents running on different platforms, languages, or services. ...

Example:
```python
from agent_framework.a2a import A2AAgent

# Connect to a remote A2A agent
a2a_agent = A2AAgent(url="
response = await a2a_agent.run("Hello!")
```

Sections: Get Started with Microsoft Agent Framework A2A, A2A Agent Integration, A2AAgent (Client), A2AExecutor (Hosting), Basic Usage Example

</details>

### auth0-api-python

SDK for verifying access tokens and securing APIs with Auth0, using Authlib.

`pip install auth0-api-python` · installs (wheel) · licence: MIT License · rank 7408 · last release 2026-08-03 · [PyPI](https://pypi.org/project/auth0-api-python/)

<details><summary>README extract</summary>

The `auth0-api-python` library allows you to secure APIs running on Python, particularly for verifying Auth0-issued access tokens.

It’s intended as a foundation for building more framework-specific integrations (e.g., with FastAPI, Django, etc.), but you can also use it directly in any Python server-side environment. ...

Features:
This SDK provides comprehensive support for securing APIs with Auth0-issued access tokens:

Example:
```python
from auth0_api_python import ApiClient, ApiClientOptions

api_client = ApiClient(ApiClientOptions(
    domain="",
    audience=""
))
```

...

</details>

### appdynamics

Python Agent for AppDynamics

`pip install appdynamics` · installs (wheel) · licence: See license in package description · rank 7453 · last release 2026-09-21 · [PyPI](https://pypi.org/project/appdynamics/)

<details><summary>README extract</summary>

Example:
```python
APPDYNAMICS, INC.

END USER LICENSE AGREEMENT

1. SOFTWARE LICENSE.

1.1 LICENSE GRANT.

...
```

</details>

### ag_ui_adk

ADK Middleware for AG-UI Protocol

`pip install ag_ui_adk` · installs (wheel) · licence: MIT · rank 7496 · last release 2026-11-03 · [PyPI](https://pypi.org/project/ag_ui_adk/)

<details><summary>README extract</summary>

Example:
```python
from ag_ui_adk import ADKAgent
from google.adk.agents import Agent

# 1. Create your ADK agent
my_agent = Agent(
    name="assistant",
    instruction="You are a helpful assistant."
    tools=[
        AGUIToolset(), # Add the tools provided by the AG-UI client
    ]
)

# 2. Create the middleware with direct agent embedding
agent = ADKAgent(
...
```

Sections: Prerequisites, Opt-in A2UI Express streaming, Quick Start, Usage options, Option 1: Direct Usage, Option 2: FastAPI Server, Option 3: Using ADK App with ResumabilityConfig (HITL), Running the ADK Backend Server for Dojo App, Examples, Simple Conversation, Multiple AG-UI Endpoints, In Tools via Session State, In Instruction Providers via Session State, Alternative: Via RunConfig custom_metadata

</details>

### agent-framework-devui

Debug UI for Microsoft Agent Framework with OpenAI-compatible API server.

`pip install agent-framework-devui` · installs (wheel) · licence: MIT License · rank 7519 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-devui/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

A lightweight, standalone sample app interface for running entities (agents/workflows) in the Microsoft Agent Framework supporting directory-based discovery, in-memory entity registration, and sample entity gallery.

> [!IMPORTANT]
> DevUI is a sample app to help you get started with the Agent Framework. It is not intended for production use. ...

Example:
```python
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from agent_framework.devui import serve

def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F and sunny"

# Create your agent
agent = Agent(
    name="WeatherAgent",
    client=OpenAIChatClient(),
...
```

...

</details>

### azure-communication-sms

Microsoft Azure Communication SMS Client Library for Python

`pip install azure-communication-sms` · installs (wheel) · licence: MIT License · rank 7542 · last release 2024-10-03 · [PyPI](https://pypi.org/project/azure-communication-sms/)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Communication Services for SMS.
Read more about Azure Communication Services here

Source code
| Package (Pypi)
| Package (Conda)
| API reference documentation
| Product documentation

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. ...

Example:
```python
from azure.communication.sms import SmsClient
from azure.identity import DefaultAzureCredential

connection_str = "endpoint=ENDPOINT;accessKey=KEY"
sms_client = SmsClient.from_connection_string(connection_string)

# To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have
...
```

...

</details>

### appdynamics-bindeps-linux-x64

Dependencies for AppDynamics Python agent

`pip install appdynamics-bindeps-linux-x64` · installs (wheel) · licence: Proprietary · rank 7553 · last release 2026-08-12 · [PyPI](https://pypi.org/project/appdynamics-bindeps-linux-x64/)

### awsebcli

Command Line Interface for AWS EB.

`pip install awsebcli` · installs from source (sdist only) · licence: Apache Software License · rank 7571 · last release 2026-10-21 · [PyPI](https://pypi.org/project/awsebcli/)

<details><summary>README extract</summary>

The AWS Elastic Beanstalk Command Line Interface (EB CLI) is a tool that helps you deploy and manage
your Elastic Beanstalk applications and environments. It also
provides integration with Git.

For detailed information about the EB CLI, see Using the Elastic Beanstalk Command Line Interface (EB CLI)
in the *AWS Elastic Beanstalk Developer Guide*. ...

Sections: EB CLI, Introduction, If you'd like to use the EB CLI, Dependencies, Getting Started, 3.27.5 (2026-10-21), 3.27.4 (2026-10-13), 3.27.3 (2026-06-29), 3.27.2 (2026-05-13), 3.27.1 (2026-03-25), 3.27 (2026-03-16), 3.26 (2026-01-07), 3.25.3 (2025-11-11), 3.25.2 (2025-10-28)

</details>

### appdynamics-proxysupport-linux-x64

Proxysupport for AppDynamics Python agent

`pip install appdynamics-proxysupport-linux-x64` · installs (wheel) · licence: Proprietary · rank 7574 · last release 2026-09-21 · [PyPI](https://pypi.org/project/appdynamics-proxysupport-linux-x64/)

### azure-messaging-webpubsubservice

Microsoft Azure WebPubSub Service Client Library for Python

`pip install azure-messaging-webpubsubservice` · installs (wheel) · licence: MIT License · rank 7599 · last release 2025-07-08 · [PyPI](https://pypi.org/project/azure-messaging-webpubsubservice/)

<details><summary>README extract</summary>

Azure Web PubSub Service is an Azure-managed service that helps developers easily build web applications with real-time features and publish-subscribe pattern. Any scenario that requires real-time publish-subscribe messaging between server and clients or among clients can use Azure Web PubSub service. ...

Example:
```python
>>> from azure.messaging.webpubsubservice import WebPubSubServiceClient

>>> service = WebPubSubServiceClient.from_connection_string(connection_string='<connection_string>', hub='hub')
```

...

</details>

### aiodynamo

Asyncio DynamoDB client

`pip install aiodynamo` · installs (wheel) · licence: not stated · rank 7627 · last release 2026-04-22 · [PyPI](https://pypi.org/project/aiodynamo/)

### aws-cdk.aws-neptune-alpha

The CDK Construct Library for AWS::Neptune

`pip install aws-cdk.aws-neptune-alpha` · installs (wheel) · licence: OSI Approved · rank 7644 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-neptune-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
import aws_cdk.aws_neptune_alpha as neptune
```

Sections: Amazon Neptune Construct Library, Starting a Neptune Database, Connecting, IAM Authentication, Customizing parameters, Adding replicas, Automatic minor version upgrades, Port, Logging, Metrics, Copy tags to snapshot, Neptune Serverless

</details>

### angr

A multi-architecture binary analysis toolkit, with the ability to perform dynamic symbolic execution and various static analyses on binaries

`pip install angr` · installs (wheel) · licence: BSD-2-Clause · rank 7655 · last release 2026-10-22 · [PyPI](https://pypi.org/project/angr/) · [source](https://github.com/angr/angr)

<details><summary>README extract</summary>

angr is a platform-agnostic binary analysis framework.
It is brought to you by the Computer Security Lab at UC Santa Barbara, SEFCOM at Arizona State University, their associated CTF team, Shellphish, the open source community, and @rhelmot.

Homepage:

Project repository:

Documentation:

API Documentation: ...

Example:
```python
import angr

project = angr.Project("angr-doc/examples/defcamp_r100/r100", auto_load_libs=False)

@project.hook(0x400844)
def print_flag(state):
    print("FLAG SHOULD BE:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()
```

Sections: angr, Project Links, What is angr?, Example, Quick Start

</details>

### astpretty

Pretty print the output of python stdlib `ast.parse`.

`pip install astpretty` · installs (wheel) · licence: MIT License · rank 7686 · last release 2022-05-16 · [PyPI](https://pypi.org/project/astpretty/)

<details><summary>README extract</summary>

Pretty print the output of python stdlib `ast.parse`.

astpretty is intended to be a replacement for `ast.dump`.

Example:
```python
>>> astpretty.pprint(ast.parse('if x == y: y += 4').body[0])
If(
    lineno=1,
    col_offset=0,
    test=Compare(
        lineno=1,
        col_offset=3,
        left=Name(lineno=1, col_offset=3, id='x', ctx=Load()),
        ops=[Eq()],
        comparators=[Name(lineno=1, col_offset=8, id='y', ctx=Load())],
    ),
    body=[
        AugAssign(
...
```

Sections: astpretty, Usage, Comparison with stdlib `ast.dump`

</details>

### aurelio-sdk

Aurelio Platform SDK

`pip install aurelio-sdk` · installs (wheel) · licence: not stated · rank 7704 · last release 2025-03-24 · [PyPI](https://pypi.org/project/aurelio-sdk/)

<details><summary>README extract</summary>

The Aurelio Platform SDK. API references

Example:
```python
from aurelio_sdk import AurelioClient
import os

client = AurelioClient(api_key=os.environ["AURELIO_API_KEY"])
```

Sections: Aurelio SDK, Authentication, Usage, Initializing the Client, Chunk, Extracting Text from Files, PDF Files, Video Files, Extracting Text from URLs, PDF URLs, Video URLs, Embeddings, Response Structure, Best Practices

</details>

### actions-toolkit

🛠 The GitHub ToolKit for developing GitHub Actions in Python.

`pip install actions-toolkit` · installs (wheel) · licence: MIT License · rank 7705 · last release 2022-10-28 · [PyPI](https://pypi.org/project/actions-toolkit/)

<details><summary>README extract</summary>

The GitHub Actions ToolKit provides an SDK to make creating actions easier in Python.

Example:
```python
>>> import os
>>> from actions_toolkit import core
>>> os.environ['INPUT_NAME'] = 'Actions Toolkit'
>>> core.get_input('name', required=True)
'Actions Toolkit'
>>> core.error('Something went wrong.')
::error::Something went wrong.
>>> core.info('Run successfully.')
Run successfully.
>>> core.set_failed('SSL certificates installation failed.')
...
```

Sections: Actions Toolkit, Usage

</details>

