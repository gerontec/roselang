# Unclassified / A (part 2 of 2)

[Index](README.md) · 752 packages in this topic, by downloads.

[part 1](unclassified-a.md) · part 2

### airflow-dbt

Apache Airflow integration for dbt

`pip install airflow-dbt` · installs (wheel) · licence: MIT License · rank 7711 · last release 2021-09-03 · [PyPI](https://pypi.org/project/airflow-dbt/)

<details><summary>README extract</summary>

This is a collection of Airflow operators to provide easy integration with dbt.

Example:
```python
from airflow import DAG
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtSnapshotOperator,
    DbtRunOperator,
    DbtTestOperator
)
from airflow.utils.dates import days_ago

default_args = {
  'dir': '/srv/app/dbt',
  'start_date': days_ago(0)
}

...
```

Sections: airflow-dbt, Usage, Building Locally, Code style, Package management, Amazon Managed Workflows for Apache Airflow (MWAA)

</details>

### aws_sdk_transcribe_streaming

aws_sdk_transcribe_streaming client

`pip install aws_sdk_transcribe_streaming` · installs (wheel) · licence: Apache Software License · rank 7720 · last release 2026-10-08 · [PyPI](https://pypi.org/project/aws_sdk_transcribe_streaming/)

<details><summary>README extract</summary>

The `aws-sdk-transcribe-streaming` package provides a client for making
requests to Amazon Transcribe Streaming Service.

> Note: This SDK is experimental and in early development. Breaking changes
> may occur prior to the release of version 1.0.0.

Sections: Amazon Transcribe Streaming Service Client, Documentation

</details>

### agent-framework-durabletask

Durable Task integration for Microsoft Agent Framework.

`pip install agent-framework-durabletask` · installs (wheel) · licence: MIT License · rank 7811 · last release 2026-10-30 · [PyPI](https://pypi.org/project/agent-framework-durabletask/) · [source](https://github.com/microsoft/agent-framework-durable-extension/tree/main/python)

<details><summary>README extract</summary>

Please install this package via pip:

This extra is part of the current unreleased stack. The matching package release must
include it before using the installation command against PyPI.
Install the optional storage dependencies through the shared extra:

The Functions package's `azure-blob-payloads` extra forwards to this extra. ...

Example:
```python
from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework_durabletask import DurableAIAgentWorker
from durabletask.worker import TaskHubGrpcWorker

# Create the worker
worker = TaskHubGrpcWorker(host_address="localhost:4001")

...
```

...

</details>

### antsibull-docs-parser

Python library for processing Ansible documentation markup

`pip install antsibull-docs-parser` · installs (wheel) · licence: GPL-3.0-or-later AND BSD-2-Clause · rank 7848 · last release 2026-09-01 · [PyPI](https://pypi.org/project/antsibull-docs-parser/) · [docs](https://docs.ansible.com/projects/antsibull-docs-parser/) · [source](https://github.com/ansible-community/antsibull-docs-parser/)

_README extract left out: share-alike licence._

### aws-shell

AWS Shell

`pip install aws-shell` · installs (wheel) · licence: Apache Software License · rank 7878 · last release 2020-10-07 · [PyPI](https://pypi.org/project/aws-shell/)

<details><summary>README extract</summary>

Sections: Upgrading the aws-shell, Configuration, Basic Usage, Profiles, Features, Auto Completion of Commands and Options, Shorthand Auto Completion, Server Side Auto Completion, Fuzzy Searching, Inline Documentation, Fish-Style Auto Suggestions, Toolbar Options, Dot Commands, Exiting the Shell

</details>

### access-parser

Access database (*.mdb, *.accdb) parser

`pip install access-parser` · installs from source (sdist only) · licence: Apache Software License · rank 7899 · last release 2025-01-23 · [PyPI](https://pypi.org/project/access-parser/)

<details><summary>README extract</summary>

Microsoft Access (.mdb / .accdb) database files parser. The parsing logic is fully written in python and works without any external binary dependencies.

Example:
```python
from access_parser import AccessParser

# .mdb or .accdb file
db = AccessParser("/path/to/mdb/file.mdb")

# Print DB tables
print(db.catalog)

# Tables are stored as defaultdict(list) -- tablecolumn
table = db.parse_table("table_name")

# Pretty print all tables
db.print_database()
```

Sections: AccessDB Parser (Pure Python), Demo, Usage Example, Known Issues, Thanks

</details>

### antsibull-fileutils

Tools for building the Ansible Distribution

`pip install antsibull-fileutils` · installs (wheel) · licence: GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0 · rank 7908 · last release 2026-06-21 · [PyPI](https://pypi.org/project/antsibull-fileutils/) · [source](https://github.com/ansible-community/antsibull-fileutils)

_README extract left out: share-alike licence._

### asdf

Python implementation of the ASDF Standard

`pip install asdf` · installs (wheel) · licence: BSD-3-Clause · rank 7992 · last release 2026-10-19 · [PyPI](https://pypi.org/project/asdf/) · [docs](https://asdf.readthedocs.io/en/stable/) · [source](https://github.com/asdf-format/asdf)

<details><summary>README extract</summary>

The A\ dvanced S\ cientific D\ ata F\ ormat (ASDF) is a
next-generation interchange format for scientific data. This package
contains the Python implementation of the ASDF specification. More
information on the ASDF file format including the specification can be found
here.

The ASDF format has the following features: ...

Features:
This section outlines basic use cases of the ASDF package for creating
and reading ASDF files.

Example:
```python
import asdf
import numpy as np

# Create some data
sequence = np.arange(100)
squares = sequence**2
random = np.random.random(100)

# Store the data in an arbitrarily nested dictionary
tree = {
    "foo": 42,
    "name": "Monty",
    "sequence": sequence,
    "powers": {"squares": squares},
    "random": random,
}

...
```

...

</details>

### aiomcache

Minimal pure python memcached client

`pip install aiomcache` · installs (wheel) · licence: BSD License · rank 7998 · last release 2024-05-07 · [PyPI](https://pypi.org/project/aiomcache/)

<details><summary>README extract</summary>

asyncio (PEP 3156) library to work with memcached.

Example:
```python
import asyncio
import aiomcache

async def hello_aiomcache():
    mc = aiomcache.Client("127.0.0.1", 11211)
    await mc.set(b"some_key", b"Some value")
    value = await mc.get(b"some_key")
    print(value)
    values = await mc.multi_get(b"some_key", b"other_key")
    print(values)
    await mc.delete(b"another_key")

...
```

Sections: memcached client for asyncio, Getting started, CHANGES, 0.8.2 (2024-05-07), 0.8.1 (2023-02-10), 0.8.0 (2022-12-11), 0.7.0 (2022-01-20), 0.6.0 (2017-12-03), 0.5.2 (2017-05-27), 0.5.1 (2017-03-08), 0.5.0 (2017-02-08), 0.4.0 (2016-09-26), 0.3.0 (2016-03-11), 0.2 (2015-12-15)

</details>

### atheris

A coverage-guided fuzzer for Python and Python extensions.

`pip install atheris` · installs (wheel) · licence: not stated · rank 8058 · last release 2026-06-17 · [PyPI](https://pypi.org/project/atheris/)

<details><summary>README extract</summary>

Atheris is a coverage-guided Python fuzzing engine. It supports fuzzing of Python code, but also native extensions written for CPython. Atheris is based off of libFuzzer. When fuzzing native code, Atheris can be used in combination with Address Sanitizer or Undefined Behavior Sanitizer to catch extra bugs.

Features:
You might see this error:

You'll get this error if the first 2 calls to `TestOneInput` didn't produce any
coverage events. Even if you have instrumented some Python code,
this can happen if the instrumentation isn't reached in those first 2 calls. ...

Example:
```python
# !/usr/bin/python3

import atheris

with atheris.instrument_imports():
  import some_library
  import sys

def TestOneInput(data):
  some_library.parse(data)

atheris.Setup(sys.argv, TestOneInput)
...

</details>

### amazoncaptcha

"Pure Python, lightweight, Pillow-based solver for the Amazon text captcha."

`pip install amazoncaptcha` · installs (wheel) · licence: MIT License · rank 8073 · last release 2023-05-14 · [PyPI](https://pypi.org/project/amazoncaptcha/) · [docs](https://amazoncaptcha.readthedocs.io/en/latest/) · [source](https://github.com/a-maliarov/amazoncaptcha)

<details><summary>README extract</summary>

The motivation behind the creation of this library is taking its start from the genuinely simple idea: "I don't want to use pytesseract or some other non-amazon-specific OCR services, nor do I want to install some executables to just solve a captcha. I desire to get a solution with 2 lines of code without any heavy add-ons, using a pure Python." ...

Example:
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome() # This is a simplified example
driver.get('

captcha = AmazonCaptcha.fromdriver(driver)
solution = captcha.solve()
```

Sections: Recent News, Quick Snippet, Usage and Class Methods, Additional

</details>

### agent-framework-declarative

Declarative specification support for Microsoft Agent Framework.

`pip install agent-framework-declarative` · installs (wheel) · licence: MIT License · rank 8090 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-declarative/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_declarative)

<details><summary>README extract</summary>

Please install this package via pip:

The package currently advertises Python 3.11–3.13 support. Python 3.14 and
3.15 can install the package, but Power Fx expressions are unavailable because
the `powerfx` dependency requires a `pythonnet` build that does not support
those Python versions.

Sections: Get Started with Microsoft Agent Framework Declarative, Declarative features, HTTP request client ownership and cookies, HTTP response body limits, MCP handler session lifetime

</details>

### aiopath

📁 Async pathlib for Python

`pip install aiopath` · installs (wheel) · licence: LGPL-3.0 · rank 8101 · last release 2023-10-16 · [PyPI](https://pypi.org/project/aiopath/)

_README extract left out: share-alike licence._

### absolufy-imports

A tool to automatically replace relative imports with absolute ones.

`pip install absolufy-imports` · installs (wheel) · licence: MIT License · rank 8131 · last release 2022-01-20 · [PyPI](https://pypi.org/project/absolufy-imports/)

<details><summary>README extract</summary>

A tool and pre-commit hook to automatically convert relative imports to absolute.

Sections: absolufy-imports, Usage as a pre-commit hook (recommended), Command-line example, Configuration, Application directories, Only use relative imports

</details>

### async-cache

an asyncio application layer cache and dataloader for python based microservices and applications with thundering herd protection

`pip install async-cache` · installs (wheel) · licence: MIT · rank 8149 · last release 2026-04-22 · [PyPI](https://pypi.org/project/async-cache/)

<details><summary>README extract</summary>

:info: In-memory application layer cache

Features:
Thundering Herd Protection
 Prevents duplicate work under concurrent load (e.g., popular keys). Without it, 100 misses = 100 DB hits; with it, = 1.

 .. code-block:: python ...

Example:
```python
from cache import AsyncCache

cache = AsyncCache(maxsize=1000, default_ttl=300)  # TTL in seconds

async def get_data(key):
    return await cache.get(
        key,
        loader=lambda: db_query(key),  # auto-caches on miss
    )

# Warmup hot keys at startup
await cache.warmup({"hot:key": lambda: preload_hot()})

# Metrics for observability
...
```

Sections: async-cache, Core Usage: Function API for Microservices, Key Features & Examples, Decorator Convenience

</details>

### azure-mgmt-frontdoor

Microsoft Azure Frontdoor Management Client Library for Python

`pip install azure-mgmt-frontdoor` · installs (wheel) · licence: MIT · rank 8169 · last release 2026-06-30 · [PyPI](https://pypi.org/project/azure-mgmt-frontdoor/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Front Door Service Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `FrontDoorManagementClient` added parameter `cloud_setting` in method `init`
 - Client `FrontDoorManagementClient` added method `send_request`
 - Enum `ActionType` added member `CAPTCHA`
 - Model `ManagedRuleDefinition` added property ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.frontdoor import FrontDoorManagementClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### asyncvnc

Asynchronous VNC for Python

`pip install asyncvnc` · installs (wheel) · licence: GPL · rank 8200 · last release 2023-02-26 · [PyPI](https://pypi.org/project/asyncvnc/)

_README extract left out: share-alike licence._

### azure-mgmt-managedservices

Microsoft Azure Managedservices Management Client Library for Python

`pip install azure-mgmt-managedservices` · installs (wheel) · licence: not stated · rank 8201 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-managedservices/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Managed Services Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation group OperationsWithScopeOperations
 - Model JustInTimeAccessPolicy has a new parameter managed_by_tenant_approvers
 - Model RegistrationAssignment has a new parameter system_data
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.managedservices import ManagedServicesClient

client = ManagedServicesClient(credential=DefaultAzureCredential())
```

...

</details>

### aws-cdk.aws-cognito-identitypool-alpha

This module is deprecated. All constructs are now available under aws-cdk-lib/aws-cognito-identitypool

`pip install aws-cdk.aws-cognito-identitypool-alpha` · installs (wheel) · licence: OSI Approved · rank 8206 · last release 2025-03-27 · [PyPI](https://pypi.org/project/aws-cdk.aws-cognito-identitypool-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> This API may emit warnings. Backward compatibility is not guaranteed.

<!--END STABILITY BANNER-->

All constructs moved to `aws-cdk-lib/aws-cognito-identitypool`.

> Identity Pools are in a separate module while the API is being stabilized. ...

Example:
```python
from aws_cdk.aws_cognito_identitypool_alpha import IdentityPool, UserPoolAuthenticationProvider
```

Sections: Amazon Cognito Identity Pool Construct Library, Identity Pools, Authenticated and Unauthenticated Identities, Authentication Providers, User Pool Authentication Provider, Server Side Token Check, Associating an External Provider Directly, OpenId Connect and Saml, Custom Providers, Role Mapping, Provider Urls, Authentication Flow, Cognito Sync, Importing Identity Pools

</details>

### agent-framework-azurefunctions

Azure Functions integration for Microsoft Agent Framework.

`pip install agent-framework-azurefunctions` · installs (wheel) · licence: MIT License · rank 8217 · last release 2026-10-30 · [PyPI](https://pypi.org/project/agent-framework-azurefunctions/) · [source](https://github.com/microsoft/agent-framework-durable-extension/tree/main/python)

<details><summary>README extract</summary>

Please install this package via pip:

The durable agent extension lets you host Microsoft Agent Framework agents on Azure Durable Functions so they can persist state, replay conversation history, and recover from failures automatically.

Example:
```python
from agent_framework_azurefunctions import AgentFunctionApp

# Use only after isolating the hub and upgrading all workers and clients.
_app = AgentFunctionApp(deployment_mode="isolated_v2")
# Register an existing agent with _app.add_agent(agent).
```

Sections: Durable Agent Extension, Entity Operations, HTTP Routes and Responses, Retention and State Budgets, Retention Metrics, Workflow HITL and Mixed Parent/Child Execution, JSON runtime boundary, Optional Blob Payload Offloading, Basic Usage Example

</details>

### atlas-provider-sqlalchemy

Load sqlalchemy models into an Atlas project.

`pip install atlas-provider-sqlalchemy` · installs (wheel) · licence: not stated · rank 8255 · last release 2026-10-30 · [PyPI](https://pypi.org/project/atlas-provider-sqlalchemy/)

<details><summary>README extract</summary>

Use Atlas with SQLAlchemy to manage your database schema as code. By connecting your SQLAlchemy models to Atlas,
you can define and edit your schema directly in Python, and Atlas will automatically plan and apply database schema migrations for you, eliminating
the need to write migrations manually. ...

Example:
```python
# import all models
from models import User, Task
from atlas_provider_sqlalchemy.ddl import print_ddl
print_ddl("mysql", [User, Task])
```

Sections: atlas-provider-sqlalchemy, Use-cases, Standalone, As Python Script, Usage, Apply, Diff, FAQ, How to include schema creation in the migration?, Credit, Issues

</details>

### alienplatform

Typed Python resource bindings for Alien workloads

`pip install alienplatform` · installs (wheel) · licence: not stated · rank 8271 · last release 2026-11-08 · [PyPI](https://pypi.org/project/alienplatform/)

<details><summary>README extract</summary>

`alienplatform` gives async Python applications typed access to resources linked by Alien. Provider selection, short-lived credential refresh, error metadata, and cloud behavior stay in the shared Rust binding core.

The package is under development and is not published to a package registry yet.

Example:
```python
from alienplatform import ai, container, key, kv, postgres, queue, sandbox, storage, vault, worker
from sqlalchemy.ext.asyncio import create_async_engine

files = storage("files")
await files.put("reports/today.json", b"{}", condition="absent")
assert await files.get("reports/today.json") == b"{}"
...
```

Sections: Alien Python bindings, Resources, AI, PostgreSQL TLS, Errors, Remote KV, Worker queue batches, Storage notifications in queues

</details>

### agent-framework-redis

Redis integration for Microsoft Agent Framework.

`pip install agent-framework-redis` · installs (wheel) · licence: MIT License · rank 8308 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-redis/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_redis)

<details><summary>README extract</summary>

Redis-backed conversation history, memory retrieval, and vector storage for
Microsoft Agent Framework.

| Your goal | Component |

| Persist ordered conversation messages across runs and application restarts | `RedisHistoryProvider` |
| Retrieve relevant memories and add them to an agent's context | `RedisContextProvider` |
| Store and search your ...

Example:
```python
import asyncio
from dataclasses import dataclass
from typing import Annotated

from agent_framework import VectorStoreField, vectorstoremodel
from agent_framework.redis import RedisStore

@vectorstoremodel
@dataclass
class Document:
    id: Annotated[str, VectorStoreField("key")]
    text: Annotated[str, VectorStoreField("data")]
...
```

...

</details>

### abx-plugins

ArchiveBox-compatible plugin suite (hooks, configs, binaries manifests)

`pip install abx-plugins` · installs (wheel) · licence: MIT License · rank 8318 · last release 2026-11-07 · [PyPI](https://pypi.org/project/abx-plugins/) · [docs](https://plugins.archivebox.io/) · [source](https://github.com/ArchiveBox/abx-plugins)

<details><summary>README extract</summary>

> [!TIP]
> ➡️ View The Live Gallery 🌠

ArchiveBox-compatible plugin suite (hooks and config schemas).

This package contains standalone plugin hook scripts and config schemas. A hook
can be run directly as a CLI; runners such as `abx-dl`
and `archivebox` add orchestration,
environment setup, and cache projection around the same scripts.

Example:
```python
from abx_plugins.plugins.base.utils import (
    load_config,
    emit_archive_result_record,
    emit_snapshot_record,
)
```

Sections: ArchiveBox Plugin Marketplace, Usage, Plugin Contract, Directory layout, Gallery screenshots, Key environment variables, Binary dependency contract, Plugin Hook Lifecycle, Base plugin utilities, Rules, Hook JSONL interface

</details>

### airbyte-source-declarative-manifest

Base source implementation for low-code sources.

`pip install airbyte-source-declarative-manifest` · does not install on CPython 3.14 · licence: MIT License · rank 8342 · last release 2024-11-08 · [PyPI](https://pypi.org/project/airbyte-source-declarative-manifest/) · [docs](https://docs.airbyte.com/integrations/sources/low-code) · [source](https://github.com/airbytehq/airbyte)

<details><summary>README extract</summary>

This is the repository for the Declarative-Manifest source connector, written in Python.
The declarative manifest source connector is a special connector that can create an arbitrary source
connector from a declarative manifest file. This allows users to create a source connector without writing any code. ...

Sections: Declarative-Manifest source connector, Prerequisites, Create credentials, Locally running the connector, Running unit tests, Building the docker image, Running as a docker container, Running our CI test suite, Dependency Management, Publishing a new version of the connector

</details>

### apache-flink

Apache Flink Python API

`pip install apache-flink` · installs from source (sdist only) · licence: Apache Software License · rank 8364 · last release 2026-06-22 · [PyPI](https://pypi.org/project/apache-flink/)

<details><summary>README extract</summary>

Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.

Learn more about Flink at ...

Sections: Apache Flink, Python Packaging, Python Requirements, Protobuf Code Generation, Running Test Cases

</details>

### asdf-standard

The ASDF Standard schemas

`pip install asdf-standard` · installs (wheel) · licence: not stated · rank 8399 · last release 2026-02-05 · [PyPI](https://pypi.org/project/asdf-standard/) · [docs](https://www.asdf-format.org/projects/asdf-standard/en/latest) · [source](https://github.com/asdf-format/asdf-standard)

<details><summary>README extract</summary>

This document describes the Advanced Scientific Data Format (ASDF),
pronounced *AZ*-diff. You can read the full specification at the online documentation.

> This is the Advanced Scientific Data Format - if you are looking for the Adaptable Seismic Data Format, go here:

Sections: ASDF specification and core schemas, Getting More Information

</details>

### agent-framework-ollama

Ollama integration for Microsoft Agent Framework.

`pip install agent-framework-ollama` · installs (wheel) · licence: MIT License · rank 8400 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-ollama/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

Please install this package as the extra for `agent-framework`:

and see the README for more information.

You can find samples how to run the connector in the Ollama provider samples.

Sections: Get Started with Microsoft Agent Framework Ollama, Run samples with the Ollama Connector

</details>

### azure-ai-translation-text

Microsoft Corporation Azure Ai Translation Text Client Library for Python

`pip install azure-ai-translation-text` · installs (wheel) · licence: not stated · rank 8410 · last release 2026-05-29 · [PyPI](https://pypi.org/project/azure-ai-translation-text/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure text translation is a cloud-based REST API provided by the Azure Translator service. It utilizes neural machine translation technology to deliver precise, contextually relevant, and semantically accurate real-time text translations across all supported languages.

Use the Text Translation client library for Python to: ...

Features:
- GA release of Azure AI Translator Text Translation SDK version 2.0.0.
- Updated to stable API version 2026-06-06.
- Added `TranslationTone` and `TranslationGender` enums for type-safe tone and gender options.

Example:
```python
credential = AzureKeyCredential(apikey)
text_translator = TextTranslationClient(credential=credential, region=region)
```

...

</details>

### any-llm-sdk

(no summary)

`pip install any-llm-sdk` · installs (wheel) · licence: Apache-2.0 · rank 8411 · last release 2026-11-05 · [PyPI](https://pypi.org/project/any-llm-sdk/) · [docs](https://docs.mozilla.ai/any-llm/) · [source](https://github.com/mozilla-ai/any-llm)

<details><summary>README extract</summary>

Communicate with any LLM provider using a single, unified interface.
Switch between OpenAI, Anthropic, Azure / Microsoft Foundry, Mistral, Ollama, and more without changing your code.

Documentation | otari.ai | Try the Demos | Contributing

Features:
- Simple, unified interface - Single function for all providers, switch models with just a string change
- Developer friendly - Full type hints for better IDE support and clear, actionable error messages ...

Example:
```python
pip install 'any-llm-sdk[mistral,ollama]'

export MISTRAL_API_KEY="YOUR_KEY_HERE"  # or OPENAI_API_KEY, etc
from any_llm import completion
import os

# Make sure you have the appropriate environment variable set
assert os.environ.get('MISTRAL_API_KEY')

response = completion(
    model="mistral-small-latest",
...

</details>

### agent-framework-github-copilot

GitHub Copilot integration for Microsoft Agent Framework.

`pip install agent-framework-github-copilot` · installs (wheel) · licence: MIT License · rank 8425 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-github-copilot/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_github_copilot)

<details><summary>README extract</summary>

Please install this package via pip:

The GitHub Copilot agent enables integration with GitHub Copilot, allowing you to interact with Copilot's agentic capabilities through the Agent Framework.

Context providers can contribute messages, instructions, and tools to a run. ...

Example:
```python
from agent_framework import tool
from agent_framework.github import GitHubCopilotAgent, GitHubCopilotOptions
from copilot.session import PermissionHandler

@tool(approval_mode="always_require")
def delete_file(path: str) -> str:
    """Delete a file."""
    ...

agent = GitHubCopilotAgent(
    tools=[delete_file],
...
```

...

</details>

### atlan-application-sdk-conformance

Conformance suite, remediation programs, and CLI for the Atlan Application SDK

`pip install atlan-application-sdk-conformance` · installs (wheel) · licence: Apache-2.0 · rank 8453 · last release 2026-11-06 · [PyPI](https://pypi.org/project/atlan-application-sdk-conformance/)

<details><summary>README extract</summary>

Dev-only conformance suite, remediation programs, and CLI for the
Atlan Application SDK.

Do not add this as a production dependency. It is intended for developer
machines and CI only.

Sections: atlan-application-sdk-conformance, Usage, Suppressing a finding, In CI

</details>

### apache-flink-libraries

Apache Flink Libraries

`pip install apache-flink-libraries` · installs (wheel) · licence: Apache Software License · rank 8503 · last release 2026-06-22 · [PyPI](https://pypi.org/project/apache-flink-libraries/)

<details><summary>README extract</summary>

Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.

Learn more about Flink at

This package bundles apache-flink needed libraries

Sections: Apache Flink, Python Packaging

</details>

### agent-framework

Microsoft Agent Framework for building AI Agents with Python. This package contains core and a curated set of optional integrations.

`pip install agent-framework` · installs (wheel) · licence: MIT License · rank 8509 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_meta)

<details><summary>README extract</summary>

Example:
```python
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    api_key='',
    azure_endpoint='',
    model='',
    api_version='',
)
```

Sections: Python 3.15 limitations, 1. Setup API Keys, 2. Create a Simple Agent, 3. Directly Use Chat Clients (No Agent Required), Connection and credential lifetimes, 4. Build an Agent with Tools and Functions, 5. Multi-Agent Orchestration, More Examples & Samples, Agent Framework Documentation

</details>

### asyncmock

Extension to the standard mock framework to support support async

`pip install asyncmock` · installs (wheel) · licence: BSD License · rank 8510 · last release 2020-03-15 · [PyPI](https://pypi.org/project/asyncmock/)

<details><summary>README extract</summary>

Awaitable mocks for async code.

The package specifically only extends mock and not any other part of unittest.

Example:
```python
my_mock = AsyncMock()

await my_mock("foo", bar=123)

my_mock.assert_called_with("foo", bar=123)
```

Sections: Async Mock, Usage, pytest Example

</details>

### agent-framework-azure-ai-search

Azure AI Search integration for Microsoft Agent Framework.

`pip install agent-framework-azure-ai-search` · installs (wheel) · licence: MIT License · rank 8567 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-azure-ai-search/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_azure_ai_search)

<details><summary>README extract</summary>

Connect Microsoft Agent Framework agents
to Azure AI Search for retrieval and vector storage.

- `AzureAISearchContextProvider` adds retrieved context to agents using semantic
 search or Knowledge Base retrieval.
- `AzureAISearchCollection` provides asynchronous batch upsert, get, delete,
 vector search, and keyword-hybrid search. ...

Example:
```python
import asyncio
from dataclasses import dataclass
from typing import Annotated

from agent_framework import VectorStoreField, vectorstoremodel
from agent_framework.azure import AzureAISearchStore

@vectorstoremodel
@dataclass
class Document:
    id: Annotated[str, VectorStoreField("key")]
...
```

...

</details>

### agent-framework-copilotstudio

Copilot Studio integration for Microsoft Agent Framework.

`pip install agent-framework-copilotstudio` · installs (wheel) · licence: MIT License · rank 8580 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-copilotstudio/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_copilotstudio)

<details><summary>README extract</summary>

Please install this package via pip:

The Copilot Studio agent enables integration with Microsoft Copilot Studio, allowing you to interact with published copilots through the Agent Framework.

Before using the Copilot Studio agent, you need:

1. ...

Example:
```python
import asyncio
from agent_framework.microsoft import CopilotStudioAgent

async def main():
    # Create agent using environment variables
    agent = CopilotStudioAgent()

    # Run a simple query
    result = await agent.run("What is the capital of France?")
    print(result)

asyncio.run(main())
```

Sections: Get Started with Microsoft Agent Framework Copilot Studio, Copilot Studio Agent, Prerequisites, Environment Variables, Basic Usage Example, Explicit Configuration Example, Authentication, Examples

</details>

### amazon-sqs-extended-client

Python version of AWS SQS extended client

`pip install amazon-sqs-extended-client` · installs (wheel) · licence: Apache Software License · rank 8581 · last release 2024-09-11 · [PyPI](https://pypi.org/project/amazon-sqs-extended-client/) · [source](https://github.com/awslabs/amazon-sqs-python-extended-client-lib)

<details><summary>README extract</summary>

The Amazon SQS Extended Client allows clients to manage Amazon SQS message payloads that exceed the 256 KB message size limit, up to a size of 2 GB. In the event of publishing such large messages, the client accomplishes this feat by storing the actual payload in a S3 bucket and by storing the reference of the stored object in the SQS queue. ...

Example:
```python
import boto3
import sqs_extended_client

sqs_extended_client = boto3.client("sqs", region_name="us-east-1")
sqs_extended_client.large_payload_support = "BUCKET_NAME_HERE"
sqs_extended_client.use_legacy_attribute = False

# Creating a SQS Queue and extracting it's Queue URL
queue = sqs_extended_client.create_queue(
...
```

...

</details>

### argo-workflows

Argo Workflows API

`pip install argo-workflows` · installs (wheel) · licence: not stated · rank 8595 · last release 2026-08-14 · [PyPI](https://pypi.org/project/argo-workflows/)

<details><summary>README extract</summary>

Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see # noqa: E501

</details>

### abxpkg

System package manager interfaces with Python type hints

`pip install abxpkg` · installs (wheel) · licence: MIT · rank 8603 · last release 2026-11-04 · [PyPI](https://pypi.org/project/abxpkg/) · [docs](https://abxpkg.archivebox.io/) · [source](https://github.com/ArchiveBox/abxpkg)

<details><summary>README extract</summary>

All-in-one multi-package manager CLI + Python API.

[][pypi]
[][pypi]
[][pypi]
[][licence]
[][repo]

Use `abxpkg` to detect & auto-install dependencies at runtime, serialize your dependencies to DB/config, and manage bins across many ecosystems. ...

Example:
```python
from abxpkg import apt, brew, pip, npm, env

apt.install('curl')
env.load('wget')
```

Sections: Usage, CLI, Per-`Binary` / per-`BinProvider` options as CLI flags, Select specific providers / re-order provider precedence, Shebang Line in Scripts, Python Library, Basic Usage, Advanced Usage, Configuration, API Reference, `BinProvider`, 🧩 Shared API, 🌍 EnvProvider (env), 🐧 AptProvider (apt)

</details>

### agent-framework-mem0

Mem0 integration for Microsoft Agent Framework.

`pip install agent-framework-mem0` · installs (wheel) · licence: MIT License · rank 8625 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-mem0/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_mem0)

<details><summary>README extract</summary>

Please install this package via pip:

The Mem0 context provider enables persistent memory capabilities for your agents, allowing them to remember user preferences and conversation context across different sessions and threads.

Example:
```python
provider = Mem0ContextProvider(
    api_key="your-key",
    user_id="user-id",
    search_user_id="user-id",
)
```

Sections: Get Started with Microsoft Agent Framework Mem0, Memory Context Provider, Basic Usage Example, Memory Scoping, Telemetry

</details>

### agent-framework-purview

Microsoft Purview (Graph dataSecurityAndGovernance) integration for Microsoft Agent Framework.

`pip install agent-framework-purview` · installs (wheel) · licence: MIT License · rank 8636 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-purview/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_purview)

<details><summary>README extract</summary>

`agent-framework-purview` adds Microsoft Purview (Microsoft Graph dataSecurityAndGovernance) policy evaluation to the Microsoft Agent Framework. It lets you enforce data security / governance policies on both the *prompt* (user input + conversation history) and the *model response* before they proceed further in your workflow.

> Status: Preview

Features:
- Middleware-based policy enforcement (agent-level and chat-client level)
- Blocks or allows content at both ingress (prompt) and egress (response) ...

Example:
```python
import asyncio
from agent_framework import Agent, Message, Role
from agent_framework.openai import OpenAIChatCompletionClient
from agent_framework.microsoft import PurviewPolicyMiddleware, PurviewSettings
from azure.identity import InteractiveBrowserCredential

...

</details>

### antsibull-changelog

Changelog tool for Ansible-core and Ansible collections

`pip install antsibull-changelog` · installs (wheel) · licence: GPL-3.0-or-later · rank 8648 · last release 2026-10-25 · [PyPI](https://pypi.org/project/antsibull-changelog/) · [docs](https://docs.ansible.com/projects/antsibull-changelog/) · [source](https://github.com/ansible-community/antsibull-changelog/)

_README extract left out: share-alike licence._

### agent-framework-chatkit

OpenAI ChatKit integration for Microsoft Agent Framework.

`pip install agent-framework-chatkit` · installs (wheel) · licence: MIT License · rank 8748 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-chatkit/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_chatkit)

<details><summary>README extract</summary>

This package provides an integration layer between Microsoft Agent Framework
and OpenAI ChatKit (Python).
Specifically, it mirrors the Agent SDK integration, and provides the following helpers: ...

Example:
```python
from collections.abc import AsyncIterator
from typing import Any

from azure.identity import AzureCliCredential
from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse

from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
...
```

Sections: Agent Framework and ChatKit Integration, Requirements and Limitations, Frontend Requirements, Air-Gapped / Regulated Environments, Example Usage

</details>

### aplr

Automatic Piecewise Linear Regression

`pip install aplr` · installs (wheel) · licence: MIT License · rank 8754 · last release 2026-09-13 · [PyPI](https://pypi.org/project/aplr/)

<details><summary>README extract</summary>

The documentation for Automatic Piecewise Linear Regression is available at

</details>

### azure-cognitiveservices-vision-computervision

Microsoft Azure Cognitive Services Computer Vision Client Library for Python

`pip install azure-cognitiveservices-vision-computervision` · installs (wheel) · licence: MIT License · rank 8790 · last release 2024-11-01 · [PyPI](https://pypi.org/project/azure-cognitiveservices-vision-computervision/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 11-01-2024. This package will only receive security fixes until 11-01-2024. To receive updates on new features and non-security bug fixes, upgrade to the replacement package, azure-ai-vision-imageanalysis.

Sections: Microsoft Azure SDK for Python, 0.9.1 (2024-11-01), Other Changes, 0.9.0 (2021-05-31), Breaking Changes, 0.8.0 (2021-03-22), 0.7.0 (2020-10-08), 0.6.0 (2020-05-18), 0.5.0 (2019-10-01), 0.4.0 (2019-06-27), 0.3.0 (2019-03-11), 0.2.0 (2018-06-22), 0.1.0 (2018-01-23)

</details>

### azure-ai-vision-imageanalysis

Microsoft Azure Ai Vision Imageanalysis Client Library for Python

`pip install azure-ai-vision-imageanalysis` · installs (wheel) · licence: MIT License · rank 8807 · last release 2024-10-16 · [PyPI](https://pypi.org/project/azure-ai-vision-imageanalysis/)

<details><summary>README extract</summary>

The Image Analysis service provides AI algorithms for processing images and returning information about their content. In a single service call, you can extract one or more visual features from the image simultaneously, including getting a caption for the image, extracting text shown in the image (OCR) and detecting objects. ...

Example:
```python
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    endpoint = os.environ["VISION_ENDPOINT"]
...
```

...

</details>

### azure-mgmt-kubernetesconfiguration

Microsoft Azure Kubernetes Configuration Management Client Library for Python

`pip install azure-mgmt-kubernetesconfiguration` · installs (wheel) · licence: MIT License · rank 8826 · last release 2023-09-22 · [PyPI](https://pypi.org/project/azure-mgmt-kubernetesconfiguration/)

<details><summary>README extract</summary>

This is the Microsoft Azure Kubernetes Configuration Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model FluxConfiguration has a new parameter reconciliation_wait_duration
 - Model FluxConfiguration has a new parameter wait_for_reconciliation
 - Model KustomizationDefinition has a new parameter post_build
 - Model KustomizationDefinition has a ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.kubernetesconfiguration import SourceControlConfigurationClient
import os

...

</details>

### azureml-dataset-runtime

The package is to coordinate dependencies within AzureML packages. This package is internal, and is not intended to be used directly.

`pip install azureml-dataset-runtime` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 8867 · last release 2026-07-31 · [PyPI](https://pypi.org/project/azureml-dataset-runtime/)

<details><summary>README extract</summary>

The purpose of this package is to coordinate dependencies within AzureML packages. This package is internal, and is not intended to be used directly.

</details>

### autowrapt

Bootstrap mechanism for monkey patches.

`pip install autowrapt` · installs (wheel) · licence: BSD-2-Clause · rank 8872 · last release 2026-09-24 · [PyPI](https://pypi.org/project/autowrapt/) · [docs](https://wrapt.readthedocs.io/en/latest/monkey.html#applying-patches-at-interpreter-startup)

<details><summary>README extract</summary>

Bootstrap mechanism for monkey patches.

autowrapt triggers the monkey patching of a Python application at
interpreter startup, without the application itself being modified. It is a
small companion to wrapt, whose
post import hook mechanism does the actual work. ...

Example:
```python
# mycompany/patches.py

import wrapt

def patch_requests(module):
    @wrapt.wrap_function_wrapper(module, "get")
    def wrapper(wrapped, instance, args, kwargs):
        print("GET", args[0] if args else kwargs.get("url"))

        return wrapped(*args, **kwargs)
```

Sections: autowrapt, Usage, Example, How it works, Limitations, Documentation

</details>

### addftool

(no summary)

`pip install addftool` · installs (wheel) · licence: not stated · rank 8910 · last release 2026-09-11 · [PyPI](https://pypi.org/project/addftool/)

### azure-mgmt-resourcehealth

Microsoft Azure Resourcehealth Management Client Library for Python

`pip install azure-mgmt-resourcehealth` · installs (wheel) · licence: MIT · rank 8912 · last release 2026-07-08 · [PyPI](https://pypi.org/project/azure-mgmt-resourcehealth/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Health Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ResourceHealthMgmtClient` added parameter `cloud_setting` in method `init`
 - Client `ResourceHealthMgmtClient` added method `send_request`
 - Enum `EventSubTypeValues` added member `FOREIGN_EXCHANGE_RATE_CHANGE`
 - Enum ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcehealth import ResourceHealthMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### axe-selenium-python

Python library to integrate axe and selenium for web accessibility testing.

`pip install axe-selenium-python` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 8920 · last release 2026-04-19 · [PyPI](https://pypi.org/project/axe-selenium-python/)

<details><summary>README extract</summary>

axe-selenium-python integrates aXe and selenium to enable automated web accessibility testing.

This version of axe-selenium-python is using axe-core@4.10.2.

You will need the following prerequisites in order to use axe-selenium-python:

- selenium >= 4.2
- Python 3.12+ ...

Example:
```python
from selenium import webdriver
from axe_selenium_python import Axe

def test_google():
    driver = webdriver.Firefox()
    driver.get("
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to file
...
```

...

</details>

### agent-framework-bedrock

Amazon Bedrock integration for Microsoft Agent Framework.

`pip install agent-framework-bedrock` · installs (wheel) · licence: MIT License · rank 8936 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-bedrock/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

Install the provider package:

The Bedrock integration enables Microsoft Agent Framework applications to call Amazon Bedrock models with familiar chat abstractions, including tool/function calling when you attach tools through `ChatOptions`.

Sections: Get Started with Microsoft Agent Framework Bedrock, Bedrock Integration, Basic Usage Example

</details>

### aiounittest

Test asyncio code more easily.

`pip install aiounittest` · installs (wheel) · licence: MIT License · rank 8956 · last release 2025-03-07 · [PyPI](https://pypi.org/project/aiounittest/)

<details><summary>README extract</summary>

The `aiounittest` is a helper library to ease of your pain (and boilerplate), when writing a test of the asynchronous code (asyncio). You can test:

* synchronous code (same as the unittest.TestCase)
* asynchronous code, it supports syntax with async/await (Python 3.5+) and asyncio.coroutine/yield from (Python 3.4) ...

Example:
```python
import asyncio
import aiounittest

async def add(x, y):
    await asyncio.sleep(0.1)
    return x + y

class MyTest(aiounittest.AsyncTestCase):

    async def test_async_add(self):
        ret = await add(5, 6)
        self.assertEqual(ret, 11)

    # or 3.4 way
    @asyncio.coroutine
    def test_sleep(self):
        ret = yield from add(5, 6)
...
```

Sections: aiounittest, Info, Usage

</details>

### allure-pytest-default-results

Generate default "unknown" results to show in Allure Report if test case does not run

`pip install allure-pytest-default-results` · installs (wheel) · licence: not stated · rank 8959 · last release 2026-04-06 · [PyPI](https://pypi.org/project/allure-pytest-default-results/) · [source](https://github.com/canonical/allure-pytest-default-results)

<details><summary>README extract</summary>

allure-pytest only reports tests that were attempted

If a test case does not run (because the runner set up failed or because a CI job timed out on a previous test), the test case will be omitted from Allure Report.

This plugin creates default "unknown" status results for each test case that's expected to run. ...

Example:
```python
import dataclasses
import json
import pathlib

@dataclasses.dataclass(frozen=True)
class Result:
    test_case_id: str
    path: pathlib.Path

    def eq(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.test_case_id == other.test_case_id

actual_results = pathlib.Path("allure-results")
...
```

</details>

### ax-platform

Adaptive Experimentation

`pip install ax-platform` · installs (wheel) · licence: MIT · rank 8974 · last release 2026-06-09 · [PyPI](https://pypi.org/project/ax-platform/) · [source](https://github.com/facebook/Ax)

<details><summary>README extract</summary>

Ax is an accessible, general-purpose platform for understanding, managing,
deploying, and automating adaptive experiments.

Adaptive experimentation is the machine-learning guided process of iteratively
exploring a (possibly infinite) parameter space in order to identify optimal
configurations in a resource-efficient manner. ...

Features:
- Expressive API: Ax has an expressive API that can address many real-world
 optimization tasks. It handles complex search spaces, multiple objectives,
 constraints on both parameters and outcomes, and noisy observations. ...

Example:
```python
>>> from ax import Client, RangeParameterConfig

>>> client = Client()
>>> client.configure_experiment(
      parameters=[
          RangeParameterConfig(
              name="x1",
...

</details>

### asgi-csrf

ASGI middleware for protecting against CSRF attacks

`pip install asgi-csrf` · installs (wheel) · licence: Apache Software License · rank 9021 · last release 2024-11-15 · [PyPI](https://pypi.org/project/asgi-csrf/)

<details><summary>README extract</summary>

ASGI middleware for protecting against CSRF attacks

Example:
```python
from asgi_csrf import asgi_csrf
from .my_asgi_app import app

app = asgi_csrf(app, signing_secret="secret-goes-here")
```

Sections: asgi-csrf, Background, Usage, Always setting the cookie if it is not already set, Configuring the cookie, Other cases that skip CSRF protection, always_protect, skip_if_scope, Custom errors with send_csrf_failed

</details>

### asdf-transform-schemas

ASDF schemas for transforms

`pip install asdf-transform-schemas` · installs (wheel) · licence: not stated · rank 9068 · last release 2025-05-27 · [PyPI](https://pypi.org/project/asdf-transform-schemas/) · [docs](https://www.asdf-format.org/projects/asdf-transform-schemas/en/latest) · [source](https://github.com/asdf-format/asdf-transform-schemas)

<details><summary>README extract</summary>

This package provides ASDF schemas for validating transform tags. Users should not
need to install this directly; instead, install an implementation package such
as asdf-astropy, which includes asdf-transform-schemas as a dependency.

</details>

### awslabs.cloudwatch-mcp-server

An AWS Labs Model Context Protocol (MCP) server for cloudwatch

`pip install awslabs.cloudwatch-mcp-server` · installs (wheel) · licence: Apache Software License · rank 9087 · last release 2026-09-22 · [PyPI](https://pypi.org/project/awslabs.cloudwatch-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

This AWS Labs Model Context Protocol (MCP) server for CloudWatch enables your troubleshooting agents to use CloudWatch data to do AI-powered root cause analysis and provide recommendations. It offers comprehensive observability tools that simplify monitoring, reduce context switching, and help teams quickly diagnose and resolve service issues. ...

Features:
Alarm Based Troubleshooting - Identifies active alarms, retrieves related metrics and logs, and analyzes historical alarm patterns to determine root causes of triggered alerts. Provides context-aware recommendations for remediation. ...

Example:
```python
result = await execute_cwl_insights_batch(
    ctx,
    log_group_names=['/aws/lambda/my-app'],  # Log group names (or ARNs for cross-account/region)
...

</details>

### agent-framework-azure-cosmos

Azure Cosmos DB for NoSQL integrations for Microsoft Agent Framework.

`pip install agent-framework-azure-cosmos` · installs (wheel) · licence: MIT License · rank 9098 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-azure-cosmos/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_azure_cosmos)

<details><summary>README extract</summary>

Use Azure Cosmos DB for NoSQL as an Agent Framework vector store, conversation history
provider, or workflow checkpoint store.

Example:
```python
from dataclasses import dataclass
from typing import Annotated

from agent_framework import VectorStoreField, vectorstoremodel
from agent_framework.azure import CosmosStore
from azure.identity.aio import AzureCliCredential

@vectorstoremodel(collection_name="documents")
@dataclass
class Document:
...
```

Sections: Microsoft Agent Framework integrations for Azure Cosmos DB, Authentication and settings, Vector store, Workflow checkpoints

</details>

### arcade-core

Arcade Core - Core library for Arcade platform

`pip install arcade-core` · installs (wheel) · licence: MIT License · rank 9102 · last release 2026-10-29 · [PyPI](https://pypi.org/project/arcade-core/)

<details><summary>README extract</summary>

Core library for the Arcade platform providing foundational components and utilities.

Features:
Arcade Core provides the essential building blocks for the Arcade platform:

- Tool Catalog & Toolkit Management: Core classes for managing and organizing tools
- Configuration & Schema Handling: Configuration management and validation ...

Example:
```python
import arcade_math
from arcade_core import ToolCatalog, Toolkit

# Create a tool catalog
catalog = ToolCatalog()

# Load a toolkit
toolkit = Toolkit.from_module(arcade_math)
```

Sections: Arcade Core, Overview, Usage

</details>

### aiotask-context

Store context information inside the asyncio.Task object

`pip install aiotask-context` · installs (wheel) · licence: not stated · rank 9124 · last release 2020-01-21 · [PyPI](https://pypi.org/project/aiotask-context/)

### agent-framework-claude

Claude Agent SDK integration for Microsoft Agent Framework.

`pip install agent-framework-claude` · installs (wheel) · licence: MIT License · rank 9140 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-claude/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_claude)

<details><summary>README extract</summary>

Please install this package via pip:

Requires Claude Agent SDK 0.2.140 or later for MCP 2-compatible custom-tool servers.

The Claude agent enables integration with Claude Agent SDK, allowing you to interact with Claude's agentic capabilities through the Agent Framework.

Sections: Get Started with Microsoft Agent Framework Claude, Claude Agent

</details>

### Avalara

Avalara Tax Python SDK.

`pip install Avalara` · installs from source (sdist only) · licence: not stated · rank 9161 · last release 2026-11-02 · [PyPI](https://pypi.org/project/Avalara/)

<details><summary>README extract</summary>

This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax. It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality. For more information about AvaTax REST v2, please visit Avalara's Developer Network or view the online Swagger documentation.

Example:
```python
from logging import config

# configure logging using file config or dictConfig
# or by setting basicConfig (this is default in case no logger is set)
config.fileConfig("logger_config.conf")

logger = logging.getLogger()

# set logger property
client.logger = logger
```

Sections: Avalara AvaTax Python SDK, Setup Test Credentials, Logging, Issue or suggestion

</details>

### assistant-stream

(no summary)

`pip install assistant-stream` · installs (wheel) · licence: MIT License · rank 9177 · last release 2026-08-04 · [PyPI](https://pypi.org/project/assistant-stream/)

### aiocontextvars

Asyncio support for PEP-567 contextvars backport.

`pip install aiocontextvars` · installs (wheel) · licence: BSD License · rank 9213 · last release 2019-04-08 · [PyPI](https://pypi.org/project/aiocontextvars/)

<details><summary>README extract</summary>

IMPORTANT: This package will be deprecated after
contextvars asyncio backport is fixed. Before then, this library
experimentally provides the missing asyncio support for the
`contextvars` backport library. Please read more in Python 3.7 contextvars
documentation.

In Python 3.7 this package *is* 100% `contextvars`. ...

Example:
```python
loop.call_soon(copy_context().run, my_meth)
```

Sections: aiocontextvars, Compatibility, 0.2.1 (2018-10-24), 0.2.0 (2018-09-09), 0.1.2 (2018-04-04), 0.1.1 (2017-12-03), 0.1.0 (2017-12-03)

</details>

### appdirs-stubs

Type stubs for appdirs

`pip install appdirs-stubs` · installs (wheel) · licence: MIT License · rank 9273 · last release 2026-01-10 · [PyPI](https://pypi.org/project/appdirs-stubs/) · [source](https://github.com/repo-helper/appdirs-stubs)

<details><summary>README extract</summary>

Type stubs for appdirs

Based on the work by Sebastian Meßmer in

</details>

### apple-compress

Python bindings for Apple's libcompression.

`pip install apple-compress` · installs (wheel) · licence: not stated · rank 9281 · last release 2024-04-05 · [PyPI](https://pypi.org/project/apple-compress/) · [docs](https://github.com/m1stadev/apple-compress/wiki/API-Usage)

<details><summary>README extract</summary>

Python bindings for Apple's libcompression.

Based on bindings from Asahi Linux.

- Python 3.8 or higher
- An *OS system

Sections: apple-compress, Requirements, Usage, Library, CLI

</details>

### asdf-astropy

ASDF serialization support for astropy

`pip install asdf-astropy` · installs (wheel) · licence: not stated · rank 9292 · last release 2026-03-27 · [PyPI](https://pypi.org/project/asdf-astropy/) · [docs](https://asdf-astropy.readthedocs.io/en/latest/) · [source](https://github.com/astropy/asdf-astropy)

### acvl-utils

Super cool utilities that we just love to use

`pip install acvl-utils` · installs (wheel) · licence: Apache-2.0 · rank 9300 · last release 2026-10-29 · [PyPI](https://pypi.org/project/acvl-utils/)

<details><summary>README extract</summary>

This repository contains functions / algorithms that the ACVL group uses frequently. Thus, we created this repository to have a central place with efficient implementations of these functions / algorithms.

Sections: ACVL Utilities, Packages, Array manipulation, Slicer, Miscellaneous, Imap tqdm

</details>

### aiperf

AIPerf is a package for performance testing of AI models

`pip install aiperf` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 9308 · last release 2026-09-24 · [PyPI](https://pypi.org/project/aiperf/)

<details><summary>README extract</summary>

AIPerf is a comprehensive benchmarking tool that measures the performance of generative AI models served by your preferred inference solution. It provides detailed metrics using a command line display as well as extensive benchmark performance reports.

Features:
- Scalable multiprocess architecture with 10 services communicating via ZMQ
- 3 UI modes: `dashboard` (real-time TUI), `simple` (progress bars), `none` (headless) ...

Sections: AIPerf, Quick Start, Setting up a Local Server, Basic Usage, Example with Custom Configuration, Features, Tutorials and Feature Guides, Getting Started, Load Control and Timing, Workloads and Data, Endpoint Types, Kubernetes, Analysis and Monitoring, Documentation

</details>

### azure-ai-evaluation

Microsoft Azure Evaluation Library for Python

`pip install azure-ai-evaluation` · installs (wheel) · licence: MIT License · rank 9313 · last release 2026-11-05 · [PyPI](https://pypi.org/project/azure-ai-evaluation/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Use Azure AI Evaluation SDK to assess the performance of your generative AI applications. Generative AI application generations are quantitatively measured with mathematical based metrics, AI-assisted quality and safety metrics. Metrics are defined as `evaluators`. ...

Features:
- `CoherenceEvaluator`, `FluencyEvaluator`, `GroundednessEvaluator`, `IntentResolutionEvaluator`, `RelevanceEvaluator`, `ResponseCompletenessEvaluator`, `RetrievalEvaluator`, `SimilarityEvaluator`, `ToolCallAccuracyEvaluator`, ...

Example:
```python
import os

from azure.ai.evaluation import evaluate, RelevanceEvaluator, ViolenceEvaluator, BleuScoreEvaluator

# NLP bleu score evaluator
bleu_score_evaluator = BleuScoreEvaluator()
result = bleu_score(
    response="Tokyo is the capital of Japan.",
...

</details>

### aiocqhttp

A Python SDK with async I/O for OneBot (CQHTTP).

`pip install aiocqhttp` · installs from source (sdist only) · licence: MIT License · rank 9345 · last release 2023-06-11 · [PyPI](https://pypi.org/project/aiocqhttp/)

<details><summary>README extract</summary>

aiocqhttp 是 OneBot (原 酷Q 的 CQHTTP 插件) 的 Python SDK，采用异步 I/O，封装了 web 服务器相关的代码，支持 OneBot 的 HTTP 和反向 WebSocket 两种通信方式，让使用 Python 的开发者能方便地开发插件。

本 SDK 要求使用 Python 3.7 或更高版本，以及建议搭配支持 OneBot v11 的 OneBot 实现。

使用方法见 文档。

如果在使用本 SDK 时遇到任何问题，请 提交 issue，也欢迎参与项目开发，具体流程请参考 贡献指南。

Sections: aiocqhttp, 文档, 遇到问题

</details>

### agent-framework-foundry-local

Foundry Local integration for Microsoft Agent Framework.

`pip install agent-framework-foundry-local` · installs (wheel) · licence: MIT License · rank 9350 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-foundry-local/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_foundry_local)

<details><summary>README extract</summary>

Requires Python 3.11-3.14 and Foundry Local SDK 2.3.1 or newer, below 3.0.
Supported platforms are Windows (x64/ARM64), Linux (x86_64/aarch64), and macOS
(Apple Silicon/arm64). Intel macOS is not supported; the standard Agent Framework
install skips this integration on unsupported platforms.
Install the integration: ...

Example:
```python
from agent_framework import Agent
from agent_framework.foundry import FoundryLocalClient

client = FoundryLocalClient(model="phi-4-mini")
agent = Agent(client=client, instructions="You are a helpful assistant.")
response = await agent.run("Why is the sky blue?")
print(response.text)
```

Sections: Get Started with Microsoft Agent Framework Foundry Local, Usage, Bring Your Own Model, Chat Options, Scope, Migration from SDK 0.5.1, Foundry Local Sample

</details>

### arcade-tdk

Arcade TDK - Toolkit Development Kit for building Arcade tools

`pip install arcade-tdk` · installs (wheel) · licence: MIT License · rank 9421 · last release 2026-10-12 · [PyPI](https://pypi.org/project/arcade-tdk/)

<details><summary>README extract</summary>

Features:
Arcade TDK provides the essential tools and utilities for building Arcade tools:

- Tool Decorator: Simple `@tool` decorator for creating Arcade tools
- Authentication: Auth providers and helpers for tool security ...

Example:
```python
from typing import Annotated

from arcade_tdk import tool

@tool
def hello_world(name: Annotated[str, "The name of the person to greet"]) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

# The tool is automatically registered and available for use
```

Sections: Overview, Usage, Advanced Usage

</details>

### azure-monitor-events-extension

Microsoft Azure Monitor Events Extension for Python

`pip install azure-monitor-events-extension` · installs (wheel) · licence: MIT License · rank 9425 · last release 2023-09-19 · [PyPI](https://pypi.org/project/azure-monitor-events-extension/)

<details><summary>README extract</summary>

The Azure Monitor Events Extension allows users to send custom events to Application Insights in conjunction with the Azure Monitor OpenTelemetry Distro.
This distro automatically installs the following libraries:

* Azure Portal
* Official Azure monitor docs
* OpenTelemetry Python Official Docs

Sections: Azure Monitor Events Extension, Additional documentation

</details>

### azure-mgmt-machinelearningservices

Microsoft Azure Machinelearningservices Management Client Library for Python

`pip install azure-mgmt-machinelearningservices` · installs (wheel) · licence: not stated · rank 9490 · last release 2026-05-18 · [PyPI](https://pypi.org/project/azure-mgmt-machinelearningservices/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Machine Learning Services Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Added operation PrivateEndpointConnectionsOperations.create_or_update
 - Added operation PrivateEndpointConnectionsOperations.delete
 - Added operation PrivateEndpointConnectionsOperations.list
 - Added operation ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.machinelearningservices import MachineLearningServicesMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-mgmt-resource-locks

Microsoft Azure Locks Management Client Library for Python

`pip install azure-mgmt-resource-locks` · installs (wheel) · licence: MIT · rank 9492 · last release 2026-09-29 · [PyPI](https://pypi.org/project/azure-mgmt-resource-locks/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Locks Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `ManagementLockObject` added property `system_data`
 - Added enum `CreatedByType`
 - Added model `ErrorAdditionalInfo`
 - Added model `ErrorDetail`
 - Added model `ErrorResponse`
 - Added model `SystemData`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.locks import ManagementLockClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### apache-hamilton

Apache Hamilton (incubating) is a lightweight Python library for directed acyclic graphs (DAGs) of transformations. Your DAG is **portable**; it runs anywhere Python runs, whether it's a script, notebook, Airflow pipeline, FastAPI server, etc. Your DAG is **expressive**; Apache Hamilton has extensive features to define and modify the execution of a DAG (e.g., data validation, experiment tracking, remote execution).

`pip install apache-hamilton` · installs (wheel) · licence: Apache-2.0 · rank 9495 · last release 2026-04-25 · [PyPI](https://pypi.org/project/apache-hamilton/) · [docs](https://hamilton.apache.org/en/latest/) · [source](https://github.com/apache/hamilton)

<details><summary>README extract</summary>

data transformation DAGs

> Disclaimer
> Apache Hamilton is an effort undergoing incubation at the Apache Software Foundation (ASF), sponsored by the Apache Incubator PMC.
> Incubation is required of all newly accepted projects until a further review indicates that the infrastructure, communications, and decision making process have stabilized in ...

Features:
Data teams write code to deliver business value, but few have the resources to standardize practices and provide quality assurance. ...

Example:
```python
from hamilton import driver
from hamilton_sdk.adapters import HamiltonTracker
import my_dag

# use your `username` and `project_id`
tracker = HamiltonTracker(
   username="my_username",
   project_id=1,
   dag_name="hello_world",
)

...

</details>

### aws-logging-handlers

Logging aws_logging_handlers to AWS services that support S3 and Kinesis stream logging with multiple threads

`pip install aws-logging-handlers` · installs from source (sdist only) · licence: MIT License · rank 9501 · last release 2020-11-30 · [PyPI](https://pypi.org/project/aws-logging-handlers/)

<details><summary>README extract</summary>

A python multithreaded logging handler package that streams records to
AWS services objects with support for the following AWS services: \* S3
\* Kinesis

Supports gzip compression(in S3)

Example:
```python
import logging
from aws_logging_handlers.S3 import S3Handler
from aws_logging_handlers.Kinesis import KinesisHandler

bucket="test_bucket" # The bucket should already exist

# The log will be rotated to a new object either when an object reaches 5 MB or when 120 seconds pass from the last rotation/initial logging
...
```

Sections: AWS Logging Handlers, Getting Started, Prerequisites, Examples

</details>

### arrow-odbc

Read the data of an ODBC data source as sequence of Apache Arrow record batches.

`pip install arrow-odbc` · installs (wheel) · licence: MIT · rank 9529 · last release 2026-11-07 · [PyPI](https://pypi.org/project/arrow-odbc/) · [source](https://github.com/pacman82/arrow-odbc-py)

<details><summary>README extract</summary>

Fill Apache Arrow arrays from ODBC data sources. This package is build on top of the `pyarrow` Python package and `arrow-odbc` Rust crate and enables you to read the data of an ODBC data source as sequence of Apache Arrow record batches.

* Fast. Makes efficient use of ODBC bulk reads and writes, to lower IO overhead.
* Flexible. ...

Example:
```python
from arrow_odbc import connect

connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};Server=localhost;TrustServerCertificate=yes;"
)

connection = connect(
    connection_string=connection_string,
    user="SA",
    password="My@Test@Password",
)
reader = connection.read_arrow_batches(
    query=f"SELECT * FROM MyTable WHERE a=?",
...
```

...

</details>

### arpy

Library for accessing 'ar' files

`pip install arpy` · installs (wheel) · licence: BSD-2-Clause · rank 9539 · last release 2026-08-31 · [PyPI](https://pypi.org/project/arpy/)

<details><summary>README extract</summary>

This library can be used to access ar files from python.

It supports both GNU and BSD formats and exposes the archived files using the standard python file interface.

Example:
```python
with arpy.Archive('file.ar') as ar:
    print("files: %s" % ar.namelist())
    with ar.open('content.txt') as f:
        print(f.read())
```

Sections: Arpy, Usage

</details>

### arcosparse

Helper to download and subset sparse data that has been Arcoified and are available through STAC and sqlite formated data

`pip install arcosparse` · installs (wheel) · licence: not stated · rank 9540 · last release 2026-03-09 · [PyPI](https://pypi.org/project/arcosparse/)

<details><summary>README extract</summary>

It is not recommended to use the `arcosparse` library directly.
Instead, if you want to work with sparse datasets, use the `copernicusmarine` Toolbox or tools like `earthkit`.

Issues on the repository are welcome and we will do our best to answer them.

Example:
```python
import glob

output_path = "some_folder"

# Get all partitioned Parquet files
parquet_files = glob.glob(f"{output_path}/*.parquet")

# # Read all files into a single dataframe
df = pd.concat(pd.read_parquet(file) for file in parquet_files)
```

Sections: Disclaimer, Usage, Main functions, `arcosparse.subset_and_return_dataframe`, `arcosparse.subset_and_save`, `arcosparse.get_entities`, `arcosparse.get_dataset_metadata`, Authentication, 0.5.1, 0.5.1: New features, 0.5.0, 0.5.0: Breaking Changes, 0.5.0: New features, 0.4.2

</details>

### atlan-application-sdk

Atlan Application SDK is a Python library for developing applications on the Atlan Platform

`pip install atlan-application-sdk` · installs (wheel) · licence: Apache-2.0 · rank 9544 · last release 2026-11-06 · [PyPI](https://pypi.org/project/atlan-application-sdk/) · [docs](https://github.com/atlanhq/application-sdk/README.md) · [source](https://github.com/atlanhq/application-sdk)

<details><summary>README extract</summary>

The Atlan Application SDK is a Python library designed for building applications on the Atlan platform. It offers a full PaaS (Platform-as-a-Service) toolkit — from local development to deployment and partner collaboration — so you can create integrations and tools that seamlessly extend the Atlan experience for our mutual customers.

Sections: Atlan Application SDK, Usage, Getting Started, 🐳 Docker, Pre-built Base Image (Harbor), Partner Collaboration, Need help?

</details>

### azure-mgmt-resource-subscriptions

Microsoft Azure Subscriptions Management Client Library for Python

`pip install azure-mgmt-resource-subscriptions` · installs (wheel) · licence: MIT · rank 9565 · last release 2026-07-20 · [PyPI](https://pypi.org/project/azure-mgmt-resource-subscriptions/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Resource Subscriptions Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `SubscriptionClient` added method `send_request`
 - Added model `CloudError`

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.subscriptions import SubscriptionClient

client = SubscriptionClient(credential=DefaultAzureCredential())
```

...

</details>

### aiochclient

Async http clickhouse client for python 3.10+

`pip install aiochclient` · installs from source (sdist only) · licence: MIT License · rank 9601 · last release 2026-06-04 · [PyPI](https://pypi.org/project/aiochclient/)

<details><summary>README extract</summary>

An async http(s) ClickHouse client for python 3.10+ supporting type
conversion in both directions, streaming, lazy decoding on select queries, and a
fully typed interface.

Example:
```python
from aiochclient import ChClient
from aiohttp import ClientSession

async def main():
    async with ClientSession() as s:
        client = ChClient(s)
        assert await client.is_alive()  # returns True if connection is Ok
```

Sections: aiochclient, Quick Start, Connecting to ClickHouse, Querying the database, Working with query results, Documentation, Type Conversion, Connection Pool Settings, Notes on Speed

</details>

### asgi-ratelimit

(no summary)

`pip install asgi-ratelimit` · installs (wheel) · licence: Apache Software License · rank 9614 · last release 2022-12-07 · [PyPI](https://pypi.org/project/asgi-ratelimit/) · [source](https://github.com/abersheeran/asgi-ratelimit)

<details><summary>README extract</summary>

Limit user access frequency. Base on ASGI.

100% coverage. High performance. Support regular matching. Customizable.

Example:
```python
from typing import Tuple

from ratelimit import RateLimitMiddleware, Rule

# Simple rate-limiter in memory:
from ratelimit.backends.simple import MemoryBackend

rate_limit = RateLimitMiddleware(
    ASGI_APP,
    AUTH_FUNCTION,
    MemoryBackend(),
    {
        r"^/towns": [Rule(second=1, group="default"), Rule(group="admin")],
...
```

Sections: ASGI RateLimit, Usage, Customizable rules, Block time, HTTP Method, Custom block handler, Built-in auth functions, Client IP, Starlette Session, Json Web Token, Custom auth error handler

</details>

### authentik-client

authentik

`pip install authentik-client` · installs (wheel) · licence: MIT · rank 9638 · last release 2026-10-21 · [PyPI](https://pypi.org/project/authentik-client/) · [source](https://github.com/GIT_USER_ID/GIT_REPO_ID)

<details><summary>README extract</summary>

This repo contains a generated API client to talk with authentik's API from Python.

Features:
This Python package is automatically generated by the OpenAPI Generator project:

- API version: 2026.8.5
- Package version: 2026.8.5
- Generator version: 7.24.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Example:
```python
import authentik_client
from authentik_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_client.Configuration(
    host = "/api/v3"
)

...
```

...

</details>

### autosar-data

read, write and modify Autosar arxml data using Python

`pip install autosar-data` · installs (wheel) · licence: not stated · rank 9679 · last release 2026-08-15 · [PyPI](https://pypi.org/project/autosar-data/) · [docs](https://danielt.github.io/autosar-data-py/) · [source](https://github.com/DanielT/autosar-data-py)

<details><summary>README extract</summary>

Python bindings for autosar-data

Features:
This crate implements Python bindings for autosar-data using PyO3. This allows all the features of `autosar-data` to be used from python code:

- read and write arxml files
- fully validate all data when it is loaded in strict mode ...

Example:
```python
from autosar_data import *

# load a file
model = AutosarModel()
(arxmlfile, warnings) = model.load_file("filename.arxml", False)
```

Sections: `autosar-data-py`, Features, API documentation, Example, Load data from a file, Load data from text, Create data from scratch, Working with data

</details>

### ap-client

Agent Platform API Client & CLI

`pip install ap-client` · installs (wheel) · licence: not stated · rank 9698 · last release 2026-10-23 · [PyPI](https://pypi.org/project/ap-client/)

<details><summary>README extract</summary>

A lightweight Python SDK and command line interface for Agent Platform. It provides helpers for configuring API access and managing templates, datasets, jobs, and groups.

</details>

### ag_ui_strands

Implementation of the AG-UI protocol for AWS Strands Agents.

`pip install ag_ui_strands` · installs (wheel) · licence: MIT · rank 9708 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ag_ui_strands/)

<details><summary>README extract</summary>

This package exposes a lightweight wrapper that lets any `strands.Agent` speak the AG-UI protocol. It mirrors the developer experience of the other integrations: give us a Strands agent instance, plug it into `StrandsAgent`, and wire it to FastAPI via `create_strands_app` (or `add_strands_fastapi_endpoint`).

- Python 3.10 to 3.14. ...

Example:
```python
agui_agent = StrandsAgent(
    agent=strands_agent,
    name="my_agent",
    hooks=[MyHookProvider()],
    plugins=[AgentSkills(skills="./skills/")],
)
```

...

</details>

### arcade-mcp-server

Model Context Protocol (MCP) server framework for Arcade.dev

`pip install arcade-mcp-server` · installs (wheel) · licence: MIT License · rank 9811 · last release 2026-10-29 · [PyPI](https://pypi.org/project/arcade-mcp-server/)

<details><summary>README extract</summary>

Arcade MCP (Model Context Protocol) Server enables AI assistants and development tools to interact with your Arcade tools through a standardized protocol. Build, deploy, and integrate MCP servers seamlessly across different AI platforms.

- Quickstart Guide - Get up and running in minutes
- Walkthrough - Learn by example ...

Features:
- 🚀 FastAPI-like Interface - Simple, intuitive API with `MCPApp`
- 🔧 Tool Discovery - Automatic discovery of tools in your project
- 🔌 Multiple Transports - Support for stdio and HTTP/SSE ...

Example:
```python
from arcade_mcp_server import MCPApp
from typing import Annotated

app = MCPApp(name="my-tools", version="1.0.0")

@app.tool
def greet(name: Annotated[str, "Name to greet"]) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

...

</details>

### aws-cdk.aws-location-alpha

The CDK Construct Library for AWS::Location

`pip install aws-cdk.aws-location-alpha` · installs (wheel) · licence: OSI Approved · rank 9849 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-location-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
# key: kms.Key

location.GeofenceCollection(self, "GeofenceCollection",
    geofence_collection_name="MyGeofenceCollection",  # optional, defaults to a generated name
    kms_key=key
)
```

Sections: AWS::Location Construct Library, Geofence Collection, Tracker, API key, Legacy Resources, Map, Place Index, Route Calculator

</details>

### ansible-vault

R/W an ansible-vault yaml file

`pip install ansible-vault` · installs (wheel) · licence: GPL-3.0-or-later · rank 9850 · last release 2025-05-15 · [PyPI](https://pypi.org/project/ansible-vault/)

_README extract left out: share-alike licence._

### arro3-io

(no summary)

`pip install arro3-io` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 9856 · last release 2026-10-12 · [PyPI](https://pypi.org/project/arro3-io/)

### ast-comments

(no summary)

`pip install ast-comments` · installs (wheel) · licence: MIT License · rank 9876 · last release 2026-02-22 · [PyPI](https://pypi.org/project/ast-comments/) · [source](https://github.com/t3rn0/ast-comments)

<details><summary>README extract</summary>

A Python extension to the built-in `ast` module that preserves comments in the Abstract Syntax Tree.
This library finds comments in source code and includes them as nodes in the parsed AST.

Example:
```python
>>> from ast_comments import *
>>> tree = parse("hello = 'hello' # comment to hello")
```

Sections: ast-comments, Usage

</details>

### agent-framework-gemini

Google Gemini integration for Microsoft Agent Framework.

`pip install agent-framework-gemini` · installs (wheel) · licence: MIT License · rank 9973 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-gemini/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_gemini)

<details><summary>README extract</summary>

Install the provider package:

The Gemini integration uses Google's current `google-genai` SDK for chat and text embeddings
through the Gemini Developer API or Gemini Enterprise Agent Platform (formerly Vertex AI).
Chat supports streaming, tool/function calling, and structured output. ...

Example:
```python
from agent_framework.gemini import GeminiEmbeddingClient

client = GeminiEmbeddingClient()
try:
    document = await client.get_embeddings(
        ["Agent Framework helps build AI agents."],
        options={"task_type": "RETRIEVAL_DOCUMENT", "dimensions": 768, "title": "Agent Framework"},
    )
    query = await client.get_embeddings(
...
```

...

</details>

### agent-framework-tools

Built-in tools for the Microsoft Agent Framework (local shell, and more).

`pip install agent-framework-tools` · installs (wheel) · licence: MIT License · rank 10008 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-tools/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_tools)

<details><summary>README extract</summary>

Beta built-in tools for the Microsoft Agent Framework. A home for first-party
Python tools that plug into any chat client's shell / function surface. The
first tool is `LocalShellTool`.

Example:
```python
import asyncio
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
from agent_framework.tools import LocalShellTool

async def main() -> None:
    client = OpenAIChatClient(model="gpt-5.4-nano")
    async with LocalShellTool() as shell:
        agent = Agent(
            client=client,
...
```

Sections: agent-framework-tools, `LocalShellTool` quick start, Modes, Safety, Output limits, Cross-OS, `ShellEnvironmentProvider` — context provider, `DockerShellTool` — sandboxed tier, Sandbox tiers at a glance, Relationship to `agent-framework-hyperlight`

</details>

### asysocks

(no summary)

`pip install asysocks` · installs (wheel) · licence: MIT License · rank 10022 · last release 2026-11-04 · [PyPI](https://pypi.org/project/asysocks/)

### Adafruit-Blinka

CircuitPython APIs for non-CircuitPython versions of Python such as CPython on Linux and MicroPython.

`pip install Adafruit-Blinka` · installs (wheel) · licence: MIT License · rank 10041 · last release 2026-10-28 · [PyPI](https://pypi.org/project/Adafruit-Blinka/)

<details><summary>README extract</summary>

This repository contains a selection of packages emulating the CircuitPython API
for devices or hosts running CPython or MicroPython. Working code exists to emulate these CircuitPython packages: ...

Sections: Introduction, Dependencies, Environments created with uv

</details>

### awslabs.aws-pricing-mcp-server

An AWS Labs Model Context Protocol (MCP) server for official pricing of AWS services

`pip install awslabs.aws-pricing-mcp-server` · installs (wheel) · licence: Apache Software License · rank 10058 · last release 2026-09-08 · [PyPI](https://pypi.org/project/awslabs.aws-pricing-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/aws-pricing-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

MCP server for accessing real-time AWS pricing information and providing cost analysis capabilities

Important Note: This server provides real-time pricing data from the AWS Pricing API. We cannot guarantee that AI assistants will always construct filters correctly or identify the absolute cheapest options. All calls are free of charge.

Sections: AWS Pricing MCP Server, Features, AWS Pricing Discovery & Information, Cost Analysis & Planning, Query pricing data with natural language, Prerequisites, ⚡ Using uv, Using Docker, AWS Authentication, Required Permissions, Configuration, Cost report output directory

</details>

### aws-solutions-constructs.core

Core CDK Construct for patterns library

`pip install aws-solutions-constructs.core` · installs (wheel) · licence: OSI Approved · rank 10072 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aws-solutions-constructs.core/) · [source](https://github.com/awslabs/aws-solutions-constructs.git)

<details><summary>README extract</summary>

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the Semantic Versioning model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

| Reference Documentation:| ...

Example:
```python
const stack = new cdk.Stack();

const props: CloudFrontToS3Props = {
  bucketProps: {
    blockPublicAccess: {
      blockPublicAcls: false,
      blockPublicPolicy: true,
      ignorePublicAcls: false,
      restrictPublicBuckets: true
    }
  }
};

new CloudFrontToS3(stack, 'test-cloudfront-s3', props);

...
```

...

</details>

### agent-framework-mistral

Mistral AI integration for Microsoft Agent Framework.

`pip install agent-framework-mistral` · installs (wheel) · licence: MIT License · rank 10073 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-mistral/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

Please install this package:

and see the README for more information.

See the Mistral agent sample and the
Mistral embedding sample for runnable examples.

The `MistralChatClient` provides chat completions using Mistral AI models, with support for
streaming, function tools, and structured output.

Example:
```python
from agent_framework import Agent
from agent_framework.mistral import MistralChatClient

# Using environment variables (MISTRAL_API_KEY, MISTRAL_CHAT_MODEL)
# Parameters can also be passed directly:
# MistralChatClient(model="mistral-large-latest", api_key="your-api-key")
client = MistralChatClient()
try:
...
```

Sections: Get Started with Microsoft Agent Framework Mistral AI, Chat Client, Quick Start, Configuration, Embedding Client

</details>

### arcade-serve

Arcade Serve - Serving infrastructure for Arcade tools and workers

`pip install arcade-serve` · installs (wheel) · licence: MIT License · rank 10075 · last release 2026-10-29 · [PyPI](https://pypi.org/project/arcade-serve/)

<details><summary>README extract</summary>

Serving infrastructure for Arcade tools and workers.

Features:
Arcade Serve provides the infrastructure for serving Arcade tools:

- FastAPI Worker: High-performance FastAPI-based worker implementation
- MCP Server: Model Context Protocol server for tool integration ...

Example:
```python
import arcade_math
from fastapi import FastAPI
from arcade_tdk import Toolkit
from arcade_serve.fastapi import FastAPIWorker

app = FastAPI()

worker_secret = os.environ.get("ARCADE_WORKER_SECRET")
worker = FastAPIWorker(app, secret=worker_secret)

worker.register_toolkit(Toolkit.from_module(arcade_math))
```

Sections: Arcade Serve, Overview, Usage

</details>

### assisted-service-client

AssistedInstall

`pip install assisted-service-client` · installs (wheel) · licence: Apache Software License · rank 10080 · last release 2026-11-07 · [PyPI](https://pypi.org/project/assisted-service-client/)

<details><summary>README extract</summary>

Assisted installation

This Python package is automatically generated by the Swagger Codegen project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

Python 2.7 and 3.4+

Example:
```python
from future import print_function
import time
import assisted_service_client
from assisted_service_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: urlAuth
configuration = assisted_service_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
...
```

Sections: assisted-service-client, Requirements., Setuptools, Getting Started, Documentation for API Endpoints, Documentation For Models, agentAuth, imageAuth, imageURLAuth, urlAuth, userAuth, watcherAuth

</details>

### acres

Access resources on your terms

`pip install acres` · installs (wheel) · licence: Apache Software License · rank 10096 · last release 2025-06-04 · [PyPI](https://pypi.org/project/acres/) · [docs](https://nipreps-acres.readthedocs.io/en/latest/) · [source](https://github.com/nipreps/acres)

<details><summary>README extract</summary>

This module provides simple, consistent access to package resources.

Features:
`importlib.resources` provides a simple, composable interface, using the
`files()` and `as_file()` functions:

`files()` returns a Traversable object, which is similar to a pathlib.Path,
except that the object may not actually exist, so `os` ...

Example:
```python
from acres import Loader

loader = Loader(somepkg)

res_text = loader.readable('data/some_resource.txt').read_text()
res_bytes = loader.readable('data/another_resource.bin').read_bytes()

with loader.as_path('data') as data_dir:
    # data_dir is a pathlib.Path until the "with" scope closes

...
```

...

</details>

### asyncstdlib-fw

Fork of asyncstdlib that work with fireworks-ai

`pip install asyncstdlib-fw` · installs (wheel) · licence: MIT License · rank 10106 · last release 2025-05-19 · [PyPI](https://pypi.org/project/asyncstdlib-fw/) · [docs](https://asyncstdlib.readthedocs.io/en/latest/) · [source](https://github.com/maxfischer2781/asyncstdlib)

<details><summary>README extract</summary>

The `asyncstdlib` library re-implements functions and classes of the Python
standard library to make them compatible with `async` callables, iterables
and context managers.
It is fully agnostic to `async` event loops and seamlessly works with
`asyncio`, third-party libraries such as `trio`, as well as
any custom `async` event loop. ...

</details>

### antlr4-tools

Tools to run ANTLR4 tool and grammar interpreter/profiler

`pip install antlr4-tools` · installs (wheel) · licence: MIT License · rank 10144 · last release 2025-04-27 · [PyPI](https://pypi.org/project/antlr4-tools/)

### aws-json-term-matcher

A Python library for advanced filtering and matching of AWS JSON logs, designed to simplify log parsing and enhance filtering capabilities.

`pip install aws-json-term-matcher` · installs (wheel) · licence: Apache Software License · rank 10154 · last release 2024-11-22 · [PyPI](https://pypi.org/project/aws-json-term-matcher/) · [source](https://github.com/pinzon/aws-json-term-matcher.git)

<details><summary>README extract</summary>

`aws_json_term_matcher` is a Python package designed to parse and evaluate filter expressions, such as those found in AWS CloudWatch log filters. This tool uses Lark for PEG parsing and supports logical operations like `AND`, `OR`, and parentheses for grouping.

Features:
- Parses logical expressions from JSON filters
- Supports `&&` (AND), `||` (OR), and parentheses for nested expressions
- Extensible to include evaluation and tree reduction (future updates)

Example:
```python
from aws_json_term_matcher.matcher import match

# Example log
log = {
    "eventType": "UpdateTrail",
    "bandwidth": 80,
    "latency": 45,
    "number": [0.001, 1000],
    "sourceIPAddress": "123.123.1.1",
    "resources": [
...

</details>

### anticaptchaofficial

Official anti-captcha.com library

`pip install anticaptchaofficial` · installs (wheel) · licence: MIT · rank 10161 · last release 2026-09-30 · [PyPI](https://pypi.org/project/anticaptchaofficial/)

<details><summary>README extract</summary>

Official library for solving images with text, Recaptcha v2/v3 Enterprise or non-Enterprise, Funcaptcha Arcoselabs, GeeTest and others.
Anti-Captcha is the most popular and reliable captcha solving service, working since 2007.
Prices for solving captchas start from $0.0005 per token.

- Image captcha
- Recaptcha v2
- Recaptcha v2 Enterprise ...

Example:
```python
balance = solver.get_balance()
if balance <= 0:
    print("too low balance!")
    return
```

Sections: anticaptchaofficial, How to solve, Basics, Solve image captcha with python, How to solve Recaptcha V2, How to solve Recaptcha V2 Enterprise, How to solve Recaptcha V3, Solve Hcaptcha, Solve FunCaptcha Arkoselabs, Solve GeeTest v3, Solve Geetest v4, Solve Turnstile, Antigate template tasks, Image to coordinates

</details>

### agent-framework-monty

Monty CodeAct integrations for Microsoft Agent Framework.

`pip install agent-framework-monty` · installs (wheel) · licence: MIT License · rank 10204 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-monty/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_monty)

<details><summary>README extract</summary>

Monty-backed CodeAct integrations for Microsoft Agent Framework.

> [!WARNING]
> This package is in beta. APIs may change before its stable release. It is
> included in `agent-framework[all]`.

> [!WARNING]
> FIDES integration is not supported with CodeAct providers. ...

Example:
```python
from agent_framework import Agent, tool
from agent_framework.monty import MontyCodeActProvider

@tool
def compute(operation: str, a: float, b: float) -> float:
    """Perform a math operation."""
    ops = {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}
    return ops[operation]

codeact = MontyCodeActProvider(
...
```

...

</details>

### ansys-api-platform-instancemanagement

Autogenerated python gRPC interface package for ansys-api-platform-instancemanagement, built on 08:43:11 on 05 August 2026

`pip install ansys-api-platform-instancemanagement` · installs (wheel) · licence: MIT · rank 10224 · last release 2026-08-05 · [PyPI](https://pypi.org/project/ansys-api-platform-instancemanagement/)

<details><summary>README extract</summary>

This Python package contains the auto-generated gRPC Python interface files for
the Product Instance Management (PIM) API.

Sections: Build, Manual Deployment, Automatic Deployment

</details>

### azure-mgmt-cosmosdbforpostgresql

Microsoft Azure Cosmosdbforpostgresql Management Client Library for Python

`pip install azure-mgmt-cosmosdbforpostgresql` · installs (wheel) · licence: MIT License · rank 10232 · last release 2023-09-20 · [PyPI](https://pypi.org/project/azure-mgmt-cosmosdbforpostgresql/)

<details><summary>README extract</summary>

This is the Microsoft Azure Cosmosdbforpostgresql Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.cosmosdbforpostgresql import CosmosdbForPostgresqlMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
client = CosmosdbForPostgresqlMgmtClient(credential=DefaultAzureCredential(), subscription_id=sub_id)
```

...

</details>

### azure-monitor-querymetrics

Microsoft Corporation Azure Monitor Query Metrics Client Library for Python

`pip install azure-monitor-querymetrics` · installs (wheel) · licence: MIT License · rank 10235 · last release 2025-07-28 · [PyPI](https://pypi.org/project/azure-monitor-querymetrics/)

<details><summary>README extract</summary>

The Azure Monitor Query Metrics client library enables you to perform read-only queries against Azure Monitor's metrics data platform. It is designed for retrieving numerical metrics from Azure resources, supporting scenarios such as monitoring, alerting, and troubleshooting. ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.monitor.querymetrics import MetricsClient

credential = DefaultAzureCredential()
metrics_client = MetricsClient(" endpoint>", credential)
```

...

</details>

### ansys-platform-instancemanagement

A Python wrapper for Ansys platform instancemanagement

`pip install ansys-platform-instancemanagement` · installs (wheel) · licence: MIT · rank 10242 · last release 2026-08-14 · [PyPI](https://pypi.org/project/ansys-platform-instancemanagement/) · [docs](https://pypim.docs.pyansys.com/) · [source](https://github.com/ansys/pypim)

<details><summary>README extract</summary>

PyPIM exposes a Pythonic interface to
communicate with the Product Instance Management (PIM) API.

The PIM API is a gRPC API, enabling both library and app developers to
start a product in a remote environment and communicate with its API. ...

Example:
```python
import ansys.platform.instancemanagement as pypim
from ansys.mapdl.core import Mapdl

if pypim.is_configured():
    with pypim.connect() as pim:
        with pim.create_instance(
            product_name="mapdl", product_version="221"
        ) as instance:
            instance.wait_for_ready()
            channel = instance.build_grpc_channel(
...
```

Sections: PyPIM, What is the PIM API?, Getting started, Configuration, Usage, Integration

</details>

### agent-framework-hyperlight

Hyperlight CodeAct integrations for Microsoft Agent Framework.

`pip install agent-framework-hyperlight` · installs (wheel) · licence: MIT License · rank 10249 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-hyperlight/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_hyperlight)

<details><summary>README extract</summary>

Hyperlight-backed CodeAct integrations for Microsoft Agent Framework.

> [!WARNING]
> FIDES integration is not supported with CodeAct providers. Host-tool calls
> made inside generated code bypass the agent's function middleware, so FIDES
> policy enforcement and label tracking do not apply to those nested calls or
> intermediate code values. ...

Example:
```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def compute(operation: str, a: float, b: float) -> float:
    """Perform a math operation."""
    ops = {"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}
    return ops[operation]

codeact = HyperlightCodeActProvider(
...
```

...

</details>

### agent-framework-azure-contentunderstanding

Azure Content Understanding integration for Microsoft Agent Framework.

`pip install agent-framework-azure-contentunderstanding` · installs (wheel) · licence: MIT License · rank 10251 · last release 2026-11-07 · [PyPI](https://pypi.org/project/agent-framework-azure-contentunderstanding/) · [source](https://github.com/microsoft/agent-framework/tree/main/python Import-Name: agent_framework_azure_contentunderstanding)

<details><summary>README extract</summary>

Please install this package via pip:

Before using this package, you need an Azure Content Understanding resource:

1. An active Azure subscription (create one for free)
2. A Microsoft Foundry resource created in a supported region
3. Default model deployments configured for your resource (GPT-4.1, GPT-4.1-mini, text-embedding-3-large) ...

Example:
```python
import asyncio
from agent_framework import Agent, AgentSession, Message, Content
from agent_framework.foundry import FoundryChatClient
from agent_framework.foundry import ContentUnderstandingContextProvider
from azure.identity import AzureCliCredential

credential = AzureCliCredential()

cu = ContentUnderstandingContextProvider(
    endpoint="
...
```

...

</details>

### azlocal

'azlocal' - Thin wrapper around 'az' to use with Localstack

`pip install azlocal` · installs (wheel) · licence: not stated · rank 10267 · last release 2026-09-07 · [PyPI](https://pypi.org/project/azlocal/)

<details><summary>README extract</summary>

"azlocal" - Thin wrapper around "az" to use with Localstack

Sections: azcli-local, Usage, Help

</details>

### arcengine

A Python library using numpy

`pip install arcengine` · installs (wheel) · licence: not stated · rank 10274 · last release 2026-01-29 · [PyPI](https://pypi.org/project/arcengine/)

<details><summary>README extract</summary>

A Python library for 2D sprite-based game development.

Example:
```python
from arcengine import ARCBaseGame, ActionInput, Camera, GameAction, Level, Sprite

class MyGame(ARCBaseGame):
    def step(self) -> None:
        # Your game logic here.
        # Call complete_action() when you are done handling the input.
        self.complete_action()

level = Level([Sprite([[1]], name="player")])

...
```

Sections: ARCEngine, Using uv (recommended), Quick Start, API Documentation, `ARCBaseGame`, Properties, Methods, `debug(message)`, `set_level(index)`, `set_level_by_name(name)`, `perform_action(action_input, raw=False)`, `complete_action()`, `is_action_complete()`, `win()`

</details>

### anls_star

A universal metric for Generative Large Language Models (GLLMs)

`pip install anls_star` · installs (wheel) · licence: Apache Software License · rank 10303 · last release 2026-01-12 · [PyPI](https://pypi.org/project/anls_star/) · [source](https://github.com/deepopinion/anls_star_metric)

<details><summary>README extract</summary>

🌟 A Universal Metric for Generative Large Language Models 🌟
*Now with benchmarks for gpt-4.5 preview as well as claude-37 and llama-3.1-405B*

 @misc{anls_star,
 title={ANLS* -- A Universal Document Processing Metric for Generative Large Language Models},
 author={David Peer and Philemon Schöpf and Volckmar Nebendahl and Alexander Rietzler and ...

Example:
```python
from anls_star import anls_score
anls = anls_score("Hello World", "Hello Wrld")
print(anls)
```

Sections: ANLS ★, How to use the ANLS* score?, Returning the closest match, Returning key scores, Benchmarks, How to Execute all Unit Tests, Packaging

</details>

### amazon-braket-sdk

An open source library for interacting with quantum computing devices on Amazon Braket

`pip install amazon-braket-sdk` · installs (wheel) · licence: Apache-2.0 · rank 10312 · last release 2026-10-28 · [PyPI](https://pypi.org/project/amazon-braket-sdk/)

<details><summary>README extract</summary>

The Amazon Braket Python SDK is an open source library that provides a framework that you can use to interact with quantum computing hardware devices through Amazon Braket.

For a one-page overview of common Amazon Braket SDK calls, see the Amazon Braket SDK cheat sheet. ...

Example:
```python
import boto3
from braket.aws import AwsDevice
from braket.circuits import Circuit
from braket.devices import Devices

device = AwsDevice(Devices.Amazon.SV1)

bell = Circuit().h(0).cnot(0, 1)
task = device.run(bell, shots=100)
print(task.result().measurement_counts)
```

...

</details>

### azure-communication-callautomation

Microsoft Azure Communication Call Automation Client Library for Python

`pip install azure-communication-callautomation` · installs (wheel) · licence: MIT License · rank 10319 · last release 2026-10-30 · [PyPI](https://pypi.org/project/azure-communication-callautomation/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Communication Call Automation. Call Automation provides developers the ability to build server-based, intelligent call workflows, and call recording for voice and PSTN channels.

Overview of Call Automation | Product documentation ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.communication.callautomation import (CallAutomationClient)

# Your unique Azure Communication service endpoint
endpoint_url = '<ENDPOINT>'
credential = DefaultAzureCredential()
client = CallAutomationClient(endpoint_url, credential)
```

Sections: _Disclaimer_, Getting started, Prerequisites, Key concepts, Examples, Initialize CallAutomationClient, Create Call, Play Media, Troubleshooting, Next steps, Provide Feedback

</details>

### apm-cli

MCP configuration tool

`pip install apm-cli` · installs (wheel) · licence: MIT License · rank 10335 · last release 2026-10-22 · [PyPI](https://pypi.org/project/apm-cli/)

<details><summary>README extract</summary>

An open-source, community-driven dependency manager for AI agents.

Think `package.json`, `requirements.txt`, or `Cargo.toml` — but for AI agent configuration.

GitHub Copilot | Claude Code | Grok Build | Cursor | OpenCode | Codex | Gemini | Windsurf | Kiro

Documentation · Quick Start · CLI Reference · Roadmap

> Portable by manifest. ...

Features:
AI coding agents need context to be useful — standards, prompts, skills, plugins — but today every developer sets this up manually. Nothing is portable nor reproducible. There's no manifest for it.

APM fixes this. ...

...

</details>

### AccessControl

Security framework for Zope

`pip install AccessControl` · installs (wheel) · licence: ZPL-2.1 · rank 10343 · last release 2026-11-03 · [PyPI](https://pypi.org/project/AccessControl/) · [source](https://github.com/zopefoundation/AccessControl)

<details><summary>README extract</summary>

AccessControl provides a general security framework for use in Zope.

Sections: AccessControl, 7.7 (2026-11-03), 7.6 (2026-10-30), 7.5 (2026-08-20), 7.4 (2026-07-13), 7.3 (2025-11-16), 7.2 (2024-11-03), 7.1 (2024-10-10), 7.0 (2024-05-30), 6.3 (2023-11-20), 6.2 (2023-09-04), 6.1 (2023-05-22), 6.0 (2023-01-12), 5.7 (2022-11-17)

</details>

### arctic-inference

Snowflake LLM inference library

`pip install arctic-inference` · installs from source (sdist only) · licence: not stated · rank 10365 · last release 2026-08-28 · [PyPI](https://pypi.org/project/arctic-inference/)

### azureml-telemetry

Used to collect telemetry data like Log messages, metrics, events, and activity messages

`pip install azureml-telemetry` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 10391 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-telemetry/)

<details><summary>README extract</summary>

The azureml-telemetry package is used to collect telemetry data and includes the following:

- Provides functionality for logging, capturing events and metrics, and monitoring code activity.
- Collect different types of telemetry using free text or structured logging. ...

Sections: Microsoft Azure Machine Learning Telemetry API for Python, Setup

</details>

### azure-communication-rooms

Microsoft Communication Rooms Client Library for Python

`pip install azure-communication-rooms` · installs (wheel) · licence: MIT License · rank 10419 · last release 2025-03-19 · [PyPI](https://pypi.org/project/azure-communication-rooms/)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Communication Services for Rooms.
Read more about Azure Communication Services here

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please
refer to

The Azure Communication Rooms package is used to do following: ...

Example:
```python
from azure.communication.rooms import RoomsClient

client = RoomsClient.from_connection_string(conn_str='<connection_str>' )
```

Sections: Azure Communication Rooms client library for Python, _Disclaimer_, Key concepts, Getting started, Prequisites, Client Initialization, Examples, Key parameters, Create a room, Update a room, Get a room, List rooms, Delete a room, Add or update participants in a room

</details>

### acceldata-sdk

Acceldata SDK

`pip install acceldata-sdk` · installs (wheel) · licence: MIT · rank 10430 · last release 2026-10-10 · [PyPI](https://pypi.org/project/acceldata-sdk/)

<details><summary>README extract</summary>

Acceldata SDK for instrumenting support in ADOC.

Refer to the documentation for details.

Sections: acceldata SDK, Version Log

</details>

### agent-framework-azure-ai

Azure AI Foundry integration for Microsoft Agent Framework.

`pip install agent-framework-azure-ai` · installs (wheel) · licence: MIT License · rank 10433 · last release 2026-03-30 · [PyPI](https://pypi.org/project/agent-framework-azure-ai/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

Please install this package via pip:

The Foundry Memory context provider enables semantic memory capabilities for your agents using Azure AI Foundry Memory Store. It automatically:
- Retrieves static (user profile) memories on first run
- Searches for contextual memories based on conversation ...

Sections: Get Started with Microsoft Agent Framework Azure AI, Foundry Memory Context Provider, Basic Usage Example

</details>

### amazon-braket-default-simulator

An open source quantum program simulator to be run locally with the Amazon Braket SDK

`pip install amazon-braket-default-simulator` · installs (wheel) · licence: Apache Software License · rank 10485 · last release 2026-11-03 · [PyPI](https://pypi.org/project/amazon-braket-default-simulator/)

<details><summary>README extract</summary>

The Amazon Braket Default Simulator is a Python open source library that provides an implementation of a quantum simulator
that you can run locally. You can use the simulator to test quantum tasks that you construct for the Amazon Braket SDK
before you submit them to the Amazon Braket service for execution. ...

Example:
```python
from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = LocalSimulator()

bell = Circuit().h(0).cnot(0, 1)
print(device.run(bell, shots=100).result().measurement_counts)
```

Sections: Amazon Braket Default Simulator, Setting up Amazon Braket Default Simulator Python, Usage, Documentation

</details>

### aws-cdk.cx-api

Cloud executable protocol

`pip install aws-cdk.cx-api` · installs (wheel) · licence: OSI Approved · rank 10493 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.cx-api/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

This module is part of the AWS Cloud Development Kit project.

* `@aws-cdk/aws-s3:createDefaultLoggingPolicy`

Enable this feature flag to create an S3 bucket policy by default in cases where
an AWS service would automatically create the Policy if one does not exist. ...

Sections: Cloud Executable API, V2 Feature Flags

</details>

### astral-dev-toolchain-cargo-nextest

A next-generation test runner for Rust.

`pip install astral-dev-toolchain-cargo-nextest` · installs (wheel) · licence: Apache-2.0 OR MIT · rank 10509 · last release 2026-11-04 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-nextest/) · [docs](https://nexte.st) · [source](https://github.com/nextest-rs/nextest)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-nextest` from tag `cargo-nextest-0.9.150` at commit `d225b1daf362c1ca8e5e048132618c1a81c57a28`.

cargo-nextest is a next-generation test runner for Rust.

For documentation and usage, see the nextest site.

</details>

### asdf-wcs-schemas

ASDF WCS schemas

`pip install asdf-wcs-schemas` · installs (wheel) · licence: not stated · rank 10522 · last release 2025-06-11 · [PyPI](https://pypi.org/project/asdf-wcs-schemas/) · [docs](https://www.asdf-format.org/projects/asdf-wcs-schemas/en/latest) · [source](https://github.com/asdf-format/asdf-wcs-schemas)

<details><summary>README extract</summary>

This package provides ASDF schemas for validating WCS tags. Users should not need to install this directly; instead, install an implementation package such as gwcs, which includes asdf-wcs-schemas as a dependency.

</details>

### aws-cdk.region-info

AWS region information, such as service principal names

`pip install aws-cdk.region-info` · installs (wheel) · licence: OSI Approved · rank 10567 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.region-info/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

Example:
```python
# Get the information for "eu-west-1":
region = region_info.RegionInfo.get("eu-west-1")

# Access attributes:
region.s3_static_website_endpoint
```

Sections: AWS Region-Specific Information Directory, Usage, The `RegionInfo` class, Low-Level API, Supplying new or missing information, Overriding incorrect information

</details>

### abxbus

Advanced Pydantic-powered event bus with async support

`pip install abxbus` · installs (wheel) · licence: MIT License · rank 10573 · last release 2026-11-04 · [PyPI](https://pypi.org/project/abxbus/) · [docs](https://abxbus.archivebox.io) · [source](https://github.com/ArchiveBox/abxbus)

<details><summary>README extract</summary>

AbxBus is an in-memory event bus library for async Python, TypeScript (node/browser), Rust, and Go.

It's designed for quickly building resilient, predictable, complex event-driven apps. ...

Example:
```python
import asyncio
from abxbus import EventBus, BaseEvent

class AuthRequestEvent(BaseEvent[str]):
    username: str

class AuthResponseEvent(BaseEvent[dict[str, str]]):
    token: str

class UserLoginEvent(BaseEvent[str]):
    username: str
    is_admin: bool

async def handle_auth_request(event: AuthRequestEvent):
...
```

...

</details>

### Acquisition

Acquisition is a mechanism that allows objects to obtain attributes from the containment hierarchy they're in.

`pip install Acquisition` · installs (wheel) · licence: ZPL-2.1 · rank 10600 · last release 2026-10-19 · [PyPI](https://pypi.org/project/Acquisition/) · [source](https://github.com/zopefoundation/Acquisition)

<details><summary>README extract</summary>

This package implements "environmental acquisiton" for Python, as
proposed in the OOPSLA96 paper by Joseph Gil and David H. Lorenz:

 We propose a new programming paradigm, environmental acquisition in
 the context of object aggregation, in which objects acquire
 behaviour from their current containers at runtime. ...

Example:
```python
>>> import ExtensionClass, Acquisition

>>> class C(ExtensionClass.Base):
...     color = 'red'

>>> class A(Acquisition.Implicit):
...     def report(self):
...         print(self.color)
...
>>> a = A()
>>> c = C()
>>> c.a = a

>>> c.a.report()
red

>>> d = C()
>>> d.color = 'green'
>>> d.a = a

>>> d.a.report()
green

>>> try:
...     a.report()
...
```

...

</details>

### amazon-braket-schemas

An open source library that contains the schemas for Amazon Braket

`pip install amazon-braket-schemas` · installs (wheel) · licence: Apache Software License · rank 10648 · last release 2026-09-02 · [PyPI](https://pypi.org/project/amazon-braket-schemas/)

<details><summary>README extract</summary>

Amazon Braket Python Schemas is an open source library that contains the schemas for Braket, including:
* intermediate representations (IR) for Amazon Braket quantum tasks and offers serialization and deserialization of those IR payloads. Think of the IR as the contract between the Amazon Braket SDK and Amazon Braket API for quantum programs. ...

Example:
```python
from braket.ir.openqasm import Program as OpenQASMProgram

program = OpenQASMProgram(source="OPENQASM 3.0; cnot $0, $1;")
print(program.json(indent=2))

"""
{
  "braketSchemaHeader": {
    "name": "braket.ir.openqasm.program",
    "version": "1"
  },
  "source": "OPENQASM 3.0; cnot $0, $1;",
  "inputs": null
}
"""
```

Sections: Amazon Braket Python Schemas, Prerequisites, Steps, Usage, Documentation

</details>

### airbyte-internal-ops

MCP and API interfaces that let the agents do the admin work

`pip install airbyte-internal-ops` · does not install on CPython 3.14 · licence: MIT License · rank 10678 · last release 2026-11-07 · [PyPI](https://pypi.org/project/airbyte-internal-ops/)

<details><summary>README extract</summary>

MCP and API interfaces that let the agents do the admin work.

Sections: airbyte-ops-mcp, Documentation, Ops Repo Subprojects, Connecting to the hosted MCP servers, Onboarding, Connector Registry, Getting Started

</details>

### asyauth

Unified authentication library

`pip install asyauth` · installs (wheel) · licence: not stated · rank 10683 · last release 2026-11-07 · [PyPI](https://pypi.org/project/asyauth/)

### arc-agi

ARC-AGI Toolkit

`pip install arc-agi` · installs (wheel) · licence: not stated · rank 10749 · last release 2026-06-10 · [PyPI](https://pypi.org/project/arc-agi/)

<details><summary>README extract</summary>

ARC-AGI Toolkit is an open-sourced python interface (API) for ARC-AGI-3 interactive environments. It provides a consistent API and tooling layer that lets agents interact with ARC-AGI-3 environments, locally or via API.

Example:
```python
import arc_agi
from arcengine import GameAction
arc = arc_agi.Arcade()
env = arc.make("ls20", render_mode="terminal")
```

Sections: ARC-AGI, QuickStart, Prerequisites, REPL Example, Minimal Example, Rendering Options, [0.9.9] - 2026-06-10, Updated, [0.9.8] - 2026-04-17, Fix, [0.9.7] - 2026-04-14, [0.9.6] - 2026-03-21

</details>

### arcgis2geojson

A Python library for converting ArcGIS JSON to GeoJSON

`pip install arcgis2geojson` · installs (wheel) · licence: MIT · rank 10782 · last release 2026-09-26 · [PyPI](https://pypi.org/project/arcgis2geojson/) · [source](https://github.com/chris48s/arcgis2geojson)

<details><summary>README extract</summary>

A Python library for converting ArcGIS JSON to GeoJSON: A partial port of ESRI's arcgis-to-geojson-utils.

Example:
```python
>>> from arcgis2geojson import arcgis2geojson

>>> input = """{
...     "attributes": {"OBJECTID": 123},
...     "geometry": {   "rings": [   [   [41.8359375, 71.015625],
...                                      [56.953125, 33.75],
...                                      [21.796875, 36.5625],
...
```

Sections: arcgis2geojson.py, Usage, As a Library, On the Console, Versioning, Licensing

</details>

### archinfo

Classes with architecture-specific information useful to other projects.

`pip install archinfo` · installs (wheel) · licence: BSD-2-Clause · rank 10834 · last release 2026-10-22 · [PyPI](https://pypi.org/project/archinfo/) · [source](https://github.com/angr/archinfo)

<details><summary>README extract</summary>

archinfo is a collection of classes that contain architecture-specific information.
It is useful for cross-architecture tools (such as pyvex).

Project repository:

Documentation:

Sections: archinfo, Project links

</details>

### astral-dev-toolchain-cargo-codspeed

Cargo extension to build & run your codspeed benchmarks

`pip install astral-dev-toolchain-cargo-codspeed` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 10837 · last release 2026-10-30 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-codspeed/) · [docs](https://codspeed.io/docs/reference/codspeed-rust/cargo-codspeed) · [source](https://github.com/CodSpeedHQ/codspeed-rust)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-codspeed` from tag `v6.0.0` at commit `5caa8dcab88a651dbb1db02e18a5fdd3bbcff7f0`.

A cargo subcommand for running CodSpeed on your project

Sections: cargo-codspeed, With `cargo`, Usage, Troubleshooting

</details>

### advent-of-code

(no summary)

`pip install advent-of-code` · installs (wheel) · licence: not stated · rank 10847 · last release 2026-03-07 · [PyPI](https://pypi.org/project/advent-of-code/)

<details><summary>README extract</summary>

Solutions to Advent of Code implemented in Rust and exposed to Python using PyO3.

Example:
```python
def solve(year: int, day: int, part: int, input: str) -> str
```

Sections: advent-of-code-python, Usage as a library, Usage as a command line tool

</details>

### apimatic-core

A library that contains core logic and utilities for consuming REST APIs using Python SDKs generated by APIMatic.

`pip install apimatic-core` · installs (wheel) · licence: MIT · rank 10858 · last release 2026-06-08 · [PyPI](https://pypi.org/project/apimatic-core/)

<details><summary>README extract</summary>

[][apimatic-core-pypi-url]
[][test-url]
[][coverage-url]
[][maintainability-url]
[][vulnerabilities-url]
[][license-url]

The APIMatic Core libraries provide a stable runtime that powers all the functionality of SDKs. ...

Sections: apimatic-core, Introduction, API Call Classes, Authentication, Configurations, Decorators, Exceptions, Factories, HTTP Configurations, HTTP, Logging Configuration, Logger, Types, Pagination

</details>

### augmax

Efficiently Composable Data Augmentation on the GPU with Jax

`pip install augmax` · installs (wheel) · licence: Apache-2.0 · rank 10863 · last release 2025-05-16 · [PyPI](https://pypi.org/project/augmax/) · [docs](https://augmax.readthedocs.io/en/latest/) · [source](https://github.com/khdlr/augmax)

<details><summary>README extract</summary>

Augmax is an image data augmentation framework supporting efficiently-composable transformations
with support for JAX function transformations.
Its strengths are efficient execution of complex augmentation pipelines and batched data augmentation on the GPU/TPU via the use of `jax.jit` and `jax.vmap`. ...

Example:
```python
import jax
import augmax

transform = augmax.Chain(
  augmax.RandomCrop(256, 256),
  augmax.HorizontalFlip(),
  augmax.Rotate(),
)

image = ...

rng = jax.random.PRNGKey(27)

transformed_image = transform(rng, image)
```

Sections: Augmax, Getting Started, Batch-wise Augmentation on the GPU, Augmenting a single image on the GPU, Augmenting an entire batch of images on the GPU

</details>

### android_backup

Unpack and repack android backups

`pip install android_backup` · installs from source (sdist only) · licence: Apache Software License · rank 10869 · last release 2018-06-06 · [PyPI](https://pypi.org/project/android_backup/)

### ascii-magic

Converts pictures into ASCII art

`pip install ascii-magic` · installs (wheel) · licence: MIT · rank 10892 · last release 2026-04-12 · [PyPI](https://pypi.org/project/ascii-magic/)

<details><summary>README extract</summary>

Python package that converts images into ASCII art for terminals and HTML.

Code based on ProfOak's Ascii Py.

Example:
```python
from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('moon.jpg')
my_art.to_terminal()
```

Sections: ASCII Magic, v2.7.5 - Apr 2026: Housekeeping, v2.7.4 - Jan 2026: Housekeeping, v2.7 - Oct 2025, v2.6 - Oct 2025, v2.5 - Oct 2025, v2.4 - Oct 2025, v2.3 - Feb 2023, v2.2 - Feb 2023, v2.1 - Feb 2023, v2.0 - Feb 2023, v1.6 - Sep 2021, v1.5 - Nov 2020, Quickstart

</details>

### aim

A super-easy way to record, search and compare AI experiments.

`pip install aim` · installs from source (sdist only) · licence: Apache Software License · rank 10911 · last release 2025-05-08 · [PyPI](https://pypi.org/project/aim/)

<details><summary>README extract</summary>

Drop a star to support Aim ⭐

 Join Aim discord community

 Aim logs your training runs and any AI Metadata, enables a beautiful UI to compare, observe them and an API to query them programmatically.

 SEAMLESSLY INTEGRATES WITH:

 TRUSTED BY ML TEAMS FROM:

 AimStack offers enterprise support that's beyond core Aim. ...

Example:
```python
from aim import Run

# Initialize a new run
run = Run()

# Log run parameters
run["hparams"] = {
    "learning_rate": 0.001,
    "batch_size": 32,
}

# Log metrics
for i in range(10):
    run.track(i, name='loss', step=i, context={ "subset":"train" })
    run.track(i, name='acc', step=i, context={ "subset":"train" })
```

...

</details>

### apimatic-requests-client-adapter

An adapter for requests client library consumed by the SDKs generated with APIMatic

`pip install apimatic-requests-client-adapter` · installs (wheel) · licence: MIT · rank 10983 · last release 2025-11-27 · [PyPI](https://pypi.org/project/apimatic-requests-client-adapter/)

<details><summary>README extract</summary>

[][pypi-apimatic-requests-client-adapter-url]
[][test-url]
[][coverage-url]
[][maintainability-url]
[][vulnerabilities-url]
[][license-url]

Requests is a simple, yet elegant, HTTP library. This repository contains the client implementation that uses the requests library for python SDK provided by APIMatic.

Sections: apimatic-requests-client-adapter, Introduction, Tests, Links

</details>

### astral-dev-toolchain-cargo-deny

Cargo plugin to help you manage large dependency graphs

`pip install astral-dev-toolchain-cargo-deny` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 11000 · last release 2026-09-15 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-deny/) · [docs](https://docs.rs/cargo-deny) · [source](https://github.com/EmbarkStudios/cargo-deny)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-deny` from tag `0.20.2` at commit `bca0dde53651ee946720e4540b5ce2610bec8f06`.

Cargo plugin for linting your dependencies

See the book 📕 for in-depth documentation.

To run on CI as a GitHub Action, see `cargo-deny-action`. ...

Sections: `❌ cargo-deny`, Quickstart, Usage, Initialize your project, Check your crates, Bans, Advisories, Sources, Pre-commit hook

</details>

### apimatic-core-interfaces

An abstract layer of the functionalities provided by apimatic-core-library, requests-client-adapter and APIMatic SDKs.

`pip install apimatic-core-interfaces` · installs (wheel) · licence: MIT · rank 11029 · last release 2025-10-29 · [PyPI](https://pypi.org/project/apimatic-core-interfaces/)

<details><summary>README extract</summary>

[](
[][maintainability-url]
[][vulnerabilities-url]
[][license-url]

This project contains the abstract layer for APIMatic's core library. The purpose of creating interfaces is to separate out the functionalities needed by APIMatic's core library module. ...

Sections: apimatic-core-interfaces, Introduction, Interfaces, Types, Enumerations

</details>

### azure-mgmt-streamanalytics

Microsoft Azure Stream Analytics Management Client Library for Python

`pip install azure-mgmt-streamanalytics` · installs (wheel) · licence: MIT License · rank 11047 · last release 2022-01-06 · [PyPI](https://pypi.org/project/azure-mgmt-streamanalytics/)

<details><summary>README extract</summary>

This is the Microsoft Azure Stream Analytics Management Client Library.
This package has been tested with Python 2.7, 3.6+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Sections: Microsoft Azure SDK for Python, _Disclaimer_, Usage, Provide Feedback, 1.0.0 (2022-01-06), 1.0.0rc1 (2020-09-18)

</details>

### ago

ago: Human readable timedeltas

`pip install ago` · installs (wheel) · licence: Public Domain · rank 11099 · last release 2026-07-02 · [PyPI](https://pypi.org/project/ago/)

<details><summary>README extract</summary>

The `ago.py` module makes customizable human readable timedeltas. For example:

Testing past tense:
Testing future tense:

Example:
```python
from ago import human
from datetime import datetime, timedelta

# With a datetime object
db_date = datetime(year=2010, month=5, day=4, hour=6, minute=54, second=33)
print('Created ' + human(db_date))  # "Created X years, Y months ago"

# With a timedelta object
delta = timedelta(days=5, hours=3, minutes=45)
...
```

Sections: What are human readable timedeltas?, How to Use, Basic Usage, Function Arguments, Examples, Advanced Usage, More Examples, Revision Control

</details>

### antimeridian

Correct GeoJSON geometries that cross the 180th meridian

`pip install antimeridian` · installs (wheel) · licence: Apache-2.0 · rank 11139 · last release 2026-09-03 · [PyPI](https://pypi.org/project/antimeridian/) · [docs](https://www.gadom.ski/antimeridian) · [source](https://github.com/gadomski/antimeridian)

<details><summary>README extract</summary>

Fix shapes that cross the antimeridian.
See the documentation for information about the underlying algorithm.
Depends on shapely and numpy.

Can fix:

- Shapely `Polygon`, `MultiPolygon`, `LineString`, and `MultiLineString` objects
- GeoJSON Polygons, MultiPolygons, Features and FeatureCollections, as dictionaries ...

Example:
```python
import antimeridian

fixed = antimeridian.fix_geojson(geojson)
```

Sections: antimeridian, Usage, Command line interface

</details>

### anki

Python library for Anki, the spaced repetition flashcard program

`pip install anki` · installs (wheel) · licence: AGPL-3.0-or-later · rank 11170 · last release 2026-11-04 · [PyPI](https://pypi.org/project/anki/) · [source](https://github.com/ankitects/anki)

_README extract left out: share-alike licence._

### amazon-sns-extended-client

Python version of AWS SNS extended client to publish large payload message

`pip install amazon-sns-extended-client` · installs (wheel) · licence: Apache Software License · rank 11205 · last release 2025-02-18 · [PyPI](https://pypi.org/project/amazon-sns-extended-client/) · [source](https://github.com/awslabs/amazon-sns-python-extended-client-lib)

<details><summary>README extract</summary>

Features:
sns-extended-client allows for publishing large messages through SNS via S3. This is the same mechanism that the Amazon library
amazon-sns-java-extended-client-lib provides.

Example:
```python
import boto3
from botocore.config import Config
import sns_extended_client

# Define Configuration for boto3's S3 Client
# NOTE - The boto3 version from 1.36.0 to 1.36.6 will throw an error if you enable accelerate_endpoint.
s3_client_config = Config(
    region_name = 'us-east-1',
    signature_version = 's3v4',
    s3={
...
```

Sections: Amazon SNS Extended Client Library for Python, Getting Started, Overview, Usage, Note, Setting a custom S3 config, Setting a custom S3 Key, Using SQSLargePayloadSize as reserved message attribute, CODE SAMPLE

</details>

### awsglue3-local

AWS Glue Python package for local development

`pip install awsglue3-local` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 11240 · last release 2021-09-13 · [PyPI](https://pypi.org/project/awsglue3-local/)

_README extract left out: share-alike licence._

### aws-cdk.core

AWS Cloud Development Kit Core Library

`pip install aws-cdk.core` · installs (wheel) · licence: OSI Approved · rank 11282 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.core/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

Example:
```python
MyStack(app, "MyStack",
    synthesizer=DefaultStackSynthesizer(
        file_assets_bucket_name="my-orgs-asset-bucket"
    )
)
```

Sections: Stacks and Stages, Stack Synthesizers, Nested Stacks, Accessing resources in a different stack, Removing automatic cross-stack references, Durations, Size (Digital Information Quantity), Secrets, ARN manipulation, Dependencies, Construct Dependencies, Stack Dependencies, Custom Resources, Custom Resource Providers

</details>

### agent-sandbox

Python SDK for the All-in-One Sandbox API, >=1.7.0

`pip install agent-sandbox` · installs (wheel) · licence: Apache-2.0 · rank 11339 · last release 2026-03-24 · [PyPI](https://pypi.org/project/agent-sandbox/) · [docs](https://github.com/agent-infra/sandbox-sdk#readme) · [source](https://github.com/agent-infra/sandbox-sdk)

<details><summary>README extract</summary>

A Python SDK for the All-in-One Sandbox API, providing access to sandbox, shell, file, jupyter, nodejs, and mcp services.

Features:
- Sandbox: Access sandbox environment information and installed packages
- Shell: Execute shell commands with session management
- File: Read, write, search, and manage files
- Jupyter: Execute Python code in Jupyter kernels ...

Example:
```python
from agent_sandbox import Sandbox

client = Sandbox(base_url="

ctx = client.sandbox.get_context()
print(ctx)

result = client.shell.exec_command(command="ls -la")
print(result)
```

Sections: Agent Sandbox Python SDK, Usage, Cloud Providers, Volcengine, Features, Requirements

</details>

### airflow-provider-hightouch

Hightouch Provider for Airflow

`pip install airflow-provider-hightouch` · installs (wheel) · licence: Apache Software License · rank 11378 · last release 2026-04-24 · [PyPI](https://pypi.org/project/airflow-provider-hightouch/)

<details><summary>README extract</summary>

Provides an Airflow Operator and Hook for Hightouch.
This allows the user to initiate a run for a sync from Airflow.

Example:
```python
from airflow_provider_hightouch.operators.hightouch import HightouchTriggerSyncOperator

with DAG(....) as dag:
...
    my_task = HightouchTriggerSyncOperator(task_id="run_my_sync", sync_id="123")
    my_other_task = HightouchTriggerSyncOperator(task_id="run_my_sync", sync_slug="my-sync-slug")
```

Sections: Apache Airflow Provider for Hightouch, Configuration, Modules, HightouchTriggerSyncOperator, HightouchSyncRunSensor, Examples, Issues

</details>

### alembic-autogen-check

CLI to check with alembic migrations are in sync with your SQLAlchemy models.

`pip install alembic-autogen-check` · installs (wheel) · licence: MIT License · rank 11405 · last release 2019-05-10 · [PyPI](https://pypi.org/project/alembic-autogen-check/)

### apispec-oneofschema

Plugin for apispec providing support for Marshmallow-OneOfSchema schemas

`pip install apispec-oneofschema` · installs (wheel) · licence: MIT · rank 11419 · last release 2025-07-28 · [PyPI](https://pypi.org/project/apispec-oneofschema/)

### astartes

Train:Test Algorithmic Sampling for Molecules and Arbitrary Arrays

`pip install astartes` · installs (wheel) · licence: MIT · rank 11428 · last release 2025-09-30 · [PyPI](https://pypi.org/project/astartes/)

<details><summary>README extract</summary>

Status Badges

 Usage
 Continuous Integration
 Release

Example:
```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
  X,  # preferably numpy arrays, but astartes will cast it for you
  y,
  sampler = 'kennard_stone',  # any of the supported samplers
)
```

Sections: astartes, (as-tar-tees), Online Documentation, `pip`, `conda`, Source, Statement of Need, Target Audience, Quick Start, Example Notebooks, Packages Using `astartes`, Using `astartes` with Categorical Data, Access Sampling Algorithms Directly, Theory and Application of `astartes`

</details>

### awslabs.billing-cost-management-mcp-server

A Model Context Protocol (MCP) server that provides tools for AWS Billing and Cost Management by wrapping boto3 SDK functions.

`pip install awslabs.billing-cost-management-mcp-server` · installs (wheel) · licence: Apache Software License · rank 11433 · last release 2026-10-30 · [PyPI](https://pypi.org/project/awslabs.billing-cost-management-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/billing-cost-management-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

MCP server for accessing AWS Billing and Cost Management capabilities.

Important Note: This server accesses cost and usage data from AWS Billing and Cost Management APIs. All API calls are performed using the caller's AWS credentials and follow AWS service limits and quotas.

Sections: AWS Billing and Cost Management MCP Server, Features, AWS Free Tier, AWS Cost and Usage Analysis, Cost Optimization Recommendations, Savings Plans and Reserved Instanaces, S3 Storage Lens Analysis, Cost and Usage Comparison, AWS Billing and Cost Management Pricing Calculator, AWS Billing Conductor & Proforma Cost Analysis, Cost Allocation Tags, Cost Category Definitions, AWS Invoicing, AWS Billing Preferences

</details>

### aimrocks

RocksDB wrapper implemented in Cython.

`pip install aimrocks` · does not install on CPython 3.14 · licence: Apache Software License · rank 11476 · last release 2024-04-24 · [PyPI](https://pypi.org/project/aimrocks/)

### azure-mgmt-desktopvirtualization

Microsoft Azure Desktop Virtualization Management Client Library for Python

`pip install azure-mgmt-desktopvirtualization` · installs (wheel) · licence: MIT License · rank 11504 · last release 2024-09-24 · [PyPI](https://pypi.org/project/azure-mgmt-desktopvirtualization/)

<details><summary>README extract</summary>

This is the Microsoft Azure Desktop Virtualization Management Client Library.
This package has been tested with Python 3.8+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- The 'DesktopVirtualizationMgmtClient' client had operation group 'app_attach_package_info' added in the current version
 - The 'DesktopVirtualizationMgmtClient' client had operation group 'app_attach_package' added in the current version
 - The ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.desktopvirtualization import DesktopVirtualizationMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### azure-communication-phonenumbers

Microsoft Azure Communication Phone Numbers Client Library for Python

`pip install azure-communication-phonenumbers` · installs (wheel) · licence: MIT License · rank 11506 · last release 2025-08-28 · [PyPI](https://pypi.org/project/azure-communication-phonenumbers/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

Azure Communication Phone Numbers client package is used to administer Phone Numbers.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Example:
```python
import os
from azure.communication.phonenumbers import PhoneNumbersClient
from azure.identity import DefaultAzureCredential

endpoint = "
# To use Azure Active Directory Authentication (DefaultAzureCredential) make sure to have your
# AZURE_TENANT_ID, AZURE_CLIENT_ID and AZURE_CLIENT_SECRET as env variables.
...
```

...

</details>

### anchorpy-core

Python bindings for Anchor Rust code

`pip install anchorpy-core` · installs (wheel) · licence: Apache-2.0 · rank 11521 · last release 2023-12-29 · [PyPI](https://pypi.org/project/anchorpy-core/) · [docs](https://kevinheavey.github.io/anchorpy-core/) · [source](https://github.com/kevinheavey/anchorpy-core)

### aiobotocore-otel

OpenTelemetry aiobotocore instrumentation

`pip install aiobotocore-otel` · installs (wheel) · licence: Apache Software License · rank 11546 · last release 2026-10-11 · [PyPI](https://pypi.org/project/aiobotocore-otel/) · [source](https://github.com/kjagiello/aiobotocore-otel)

### aws-cdk.aws-iam

CDK routines for easily assigning correct and minimal IAM permissions

`pip install aws-cdk.aws-iam` · installs (wheel) · licence: OSI Approved · rank 11583 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-iam/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Define a role and add permissions to it. ...

Features:
* Policy name uniqueness is enforced. If two policies by the same name are attached to the same
 principal, the attachment will fail.
* Policy names are not required - the CDK logical ID will be used and ensured to be unique. ...

Example:
```python
role = Role(self, "MyRole",
    assumed_by=ServicePrincipal("sns.amazonaws.com")
)

role.add_to_policy(PolicyStatement(
    resources=["*"],
    actions=["lambda:InvokeFunction"]
))
```

...

</details>

### azure-mgmt-quota

Microsoft Azure Quota Management Client Library for Python

`pip install azure-mgmt-quota` · installs (wheel) · licence: not stated · rank 11586 · last release 2025-10-09 · [PyPI](https://pypi.org/project/azure-mgmt-quota/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Quota Management Client Library.
This package has been tested with Python 3.9+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Model `QuotaMgmtClient` added parameter `cloud_setting` in method `init`
 - Client `QuotaMgmtClient` added method `send_request`
 - Client `QuotaMgmtClient` added operation group `group_quota_usages`
 - Client `QuotaMgmtClient` added operation ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.quota import QuotaMgmtClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### aws-dynamodb-parser

AWS DynamoDB utility for parsing DynamoDB responses

`pip install aws-dynamodb-parser` · installs (wheel) · licence: MIT License · rank 11593 · last release 2021-11-11 · [PyPI](https://pypi.org/project/aws-dynamodb-parser/)

<details><summary>README extract</summary>

[](

AWS DynamoDB utility for parsing DynamoDB responses

Example:
```python
import boto3
from aws_dynamodb_parser import parse

dynamodb_client = boto3.client("dynamodb")
response = dynamodb_client.get_item(
    TableName="TABLE_NAME",
    Key={
        "id": {"S": "a77b5fc0-75cb-408c-bebf-863873506cce"},
        "timestamp": {"S": "2020-10-01 13:13:47.388492"}
    }
)

item = response.get("Item", {})
print(item)
...
```

Sections: AWS DynamoDB Parser, parse, Examples, Documentation, Links

</details>

### anchorpy

The Python Anchor client.

`pip install anchorpy` · installs (wheel) · licence: not stated · rank 11634 · last release 2025-03-26 · [PyPI](https://pypi.org/project/anchorpy/) · [docs](https://kevinheavey.github.io/anchorpy/) · [source](https://github.com/kevinheavey/anchorpy)

<details><summary>README extract</summary>

AnchorPy is the gateway to interacting with Anchor programs in Python.
It provides:

- A static client generator
- A dynamic client similar to `anchor-ts`
- A Pytest plugin
- A CLI with various utilities for Anchor Python development.

Read the Documentation.

</details>

### ansi

ANSI cursor movement and graphics

`pip install ansi` · installs (wheel) · licence: MIT License · rank 11650 · last release 2024-01-22 · [PyPI](https://pypi.org/project/ansi/)

<details><summary>README extract</summary>

Various ANSI escape codes, used in moving the cursor in a text console or
rendering coloured text.

Example

Print something in bold yellow on a red background:

 >>> from ansi.colour import fg, bg
 >>> from ansi.colour.fx import reset
 >>> msg = (bg.red, fg.yellow, 'Hello world!', reset)
 >>> print(''.join(map(str, msg)))
 ... ...

</details>

### aws-cdk.aws-kms

The CDK Construct Library for AWS::KMS

`pip install aws-cdk.aws-kms` · installs (wheel) · licence: OSI Approved · rank 11670 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-kms/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Define a KMS key:

Define a KMS key with waiting period: ...

Example:
```python
kms.Key(self, "MyKey",
    enable_key_rotation=True
)
```

Sections: AWS Key Management Service Construct Library, Sharing keys between stacks, Importing existing keys, Import key by ARN, Import key by alias, Lookup key by alias, Key Policies, Appending to or replacing the default key policy

</details>

### anyjson

Wraps the best available JSON implementation available in a common interface

`pip install anyjson` · installs from source (sdist only) · licence: BSD License · rank 11676 · last release 2012-06-22 · [PyPI](https://pypi.org/project/anyjson/)

<details><summary>README extract</summary>

anyjson - JSON library wrapper

Overview

Anyjson loads whichever is the fastest JSON module installed and provides
a uniform API regardless of which JSON implementation is used.

Originally part of carrot (

Examples

To serialize a python object to a JSON string, call the `serialize` function: ...

Sections: #

</details>

### aws-sns-message-validator

Validator for AWS SNS messages.

`pip install aws-sns-message-validator` · installs (wheel) · licence: not stated · rank 11710 · last release 2022-02-15 · [PyPI](https://pypi.org/project/aws-sns-message-validator/)

<details><summary>README extract</summary>

PyPI:

An HTTP endpoint for AWS SNS needs to validate the received messages before processing them which involves some non-trivial logic, especially signature verification. In terms of implementation, AWS does not offer any help with SNS message validation in their SDK for Python (issue) nor does it provide example code in the documentation ...

Sections: AWS SNS Message Validator, Motivation, Prerequisite, Usage, Issues

</details>

### aws-cdk.aws-cloudwatch

The CDK Construct Library for AWS::CloudWatch

`pip install aws-cdk.aws-cloudwatch` · installs (wheel) · licence: OSI Approved · rank 11715 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-cloudwatch/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# fn: lambda.Function

errors = fn.metric_errors()
```

Sections: Amazon CloudWatch Construct Library, Metric objects, Instantiating a new Metric object, Metric Math, Search Expressions, Aggregation, Labels, Alarms, Alarm Actions, Notification formats, Composite Alarms, A note on units, Dashboards, Graph widget

</details>

### aws-cdk.aws-events

Amazon EventBridge Construct Library

`pip install aws-cdk.aws-events` · installs (wheel) · licence: OSI Approved · rank 11719 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-events/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# repo: codecommit.Repository
# project: codebuild.Project

on_commit_rule = repo.on_commit("OnCommit",
    target=targets.CodeBuildProject(project),
    branches=["master"]
)
```

Sections: Amazon EventBridge Construct Library, Rule, Scheduling, Event Targets, Cross-account and cross-region targets, Archiving, Granting PutEvents to an existing EventBus

</details>

### aws-cdk.aws-ec2

The CDK Construct Library for AWS::EC2

`pip install aws-cdk.aws-ec2` · installs (wheel) · licence: OSI Approved · rank 11723 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-ec2/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
import aws_cdk.aws_ec2 as ec2
```

Sections: Amazon EC2 Construct Library, VPC, Subnet Types, Control over availability zones, Choosing subnets for resources, Using NAT instances, Advanced Subnet Configuration, Accessing the Internet Gateway, Routing, Reserving subnet IP space, Sharing VPCs between stacks, Importing an existing VPC, Allowing Connections, Connection Peers

</details>

### aws-cdk.aws-s3

The CDK Construct Library for AWS::S3

`pip install aws-cdk.aws-s3` · installs (wheel) · licence: OSI Approved · rank 11730 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-s3/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Define an unencrypted S3 bucket. ...

Example:
```python
bucket = s3.Bucket(self, "MyFirstBucket")
```

Sections: Amazon S3 Construct Library, Encryption, Permissions, Enforcing SSL, Sharing buckets between stacks, Importing existing buckets, Bucket Notifications, EventBridge notifications, Block Public Access, Logging configuration, S3 Inventory, Website redirection, Static redirection, Routing rules

</details>

### aws-cdk.aws-logs

The CDK Construct Library for AWS::Logs

`pip install aws-cdk.aws-logs` · installs (wheel) · licence: OSI Approved · rank 11755 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-logs/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# Configure log group for short retention
log_group = LogGroup(stack, "LogGroup",
    retention=RetentionDays.ONE_WEEK
)# Configure log group for infinite retention
log_group = LogGroup(stack, "LogGroup",
    retention=Infinity
)
```

...

</details>

### asyncio-dgram

Higher level Datagram support for Asyncio

`pip install asyncio-dgram` · installs (wheel) · licence: MIT · rank 11757 · last release 2026-01-21 · [PyPI](https://pypi.org/project/asyncio-dgram/) · [source](https://github.com/jsbronder/asyncio-dgram.git)

<details><summary>README extract</summary>

Example:
```python
import asyncio

import asyncio_dgram

async def udp_echo_client():
    stream = await asyncio_dgram.connect(("127.0.0.1", 8888))

    await stream.send(b"Hello World!")
    data, remote_addr = await stream.recv()
    print(f"Client received: {data.decode()!r}")

    stream.close()

async def udp_echo_server():
...
```

Sections: Design, Example UDP echo client and server

</details>

### aws-cdk.aws-s3-assets

Deploy local files and directories to S3

`pip install aws-cdk.aws-s3-assets` · installs (wheel) · licence: OSI Approved · rank 11758 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-s3-assets/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
asset = assets.Asset(self, "SampleAsset",
    path=path.join(__dirname, "sample-asset-directory")
)
```

Sections: AWS CDK Assets, Attributes, Permissions, How does it work, Asset Bundling, CloudFormation Resource Metadata

</details>

### aws-cdk.assets

This module is deprecated. All types are now available under the core module

`pip install aws-cdk.assets` · installs (wheel) · licence: OSI Approved · rank 11768 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.assets/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> This API may emit warnings. Backward compatibility is not guaranteed.

<!--END STABILITY BANNER-->

All types moved to @aws-cdk/core.

</details>

### awslabs.aws-iac-mcp-server

An Infrastructure as Code MCP server that provides CloudFormation template validation, compliance checking, and deployment troubleshooting capabilities.

`pip install awslabs.aws-iac-mcp-server` · installs (wheel) · licence: Apache Software License · rank 11770 · last release 2026-09-08 · [PyPI](https://pypi.org/project/awslabs.aws-iac-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/aws-iac-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

Get started with this MCP server for creating and troubleshooting AWS infrastructure as code. Tools include CloudFormation template validation, compliance checking, deployment troubleshooting, CloudFormation documentation search, AWS CDK documentation search with official CDK knowledge bases, CDK code samples and constructs, and CDK and ...

Sections: AWS Infrastructure as Code MCP Server, MCP highlights, Features, Template Validation, Compliance Checking, Deployment Troubleshooting, CloudFormation Documentation Search, CDK Documentation Search, CDK Code Samples & Constructs, CDK Best Practices, Available MCP Tools, Read Documentation Tool, read_iac_documentation_page, CloudFormation Tools

</details>

### atcf-data-parser

Parse a-deck data posted online by the Automated Tropical Cyclone Forecasting System

`pip install atcf-data-parser` · installs (wheel) · licence: MIT · rank 11780 · last release 2026-04-07 · [PyPI](https://pypi.org/project/atcf-data-parser/) · [source](https://github.com/palewire/atcf-data-parser)

<details><summary>README extract</summary>

A Python parser and command-line utility for the a-deck data posted online by the Automated Tropical Cyclone Forecasting System

- Documentation: palewi.re/docs/atcf-data-parser/
- Code: github.com/palewire/atcf-data-parser
- Issues: github.com/palewire/atcf-data-parser/issues
- Packaging: pypi.org/project/atcf-data-parser

</details>

### aws-cdk.aws-ssm

The CDK Construct Library for AWS::SSM

`pip install aws-cdk.aws-ssm` · installs (wheel) · licence: OSI Approved · rank 11785 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-ssm/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project.

Example:
```python
# Retrieve the latest value of the non-secret parameter
# with name "/My/String/Parameter".
string_value = ssm.StringParameter.from_string_parameter_attributes(self, "MyValue",
    parameter_name="/My/Public/Parameter"
).string_value
...
```

Sections: AWS Systems Manager Construct Library, Using existing SSM Parameters in your CDK app, Creating new SSM Parameters in your CDK app

</details>

### aws-cdk.aws-sqs

The CDK Construct Library for AWS::SQS

`pip install aws-cdk.aws-sqs` · installs (wheel) · licence: OSI Approved · rank 11805 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-sqs/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
sqs.Queue(self, "Queue")
```

Sections: Amazon Simple Queue Service Construct Library, Basic usage, Encryption, First-In-First-Out (FIFO) queues

</details>

### azure-identity-broker

Microsoft Azure Identity Broker plugin for Python

`pip install azure-identity-broker` · installs (wheel) · licence: MIT License · rank 11809 · last release 2025-08-07 · [PyPI](https://pypi.org/project/azure-identity-broker/)

<details><summary>README extract</summary>

This package extends the Azure Identity library by providing supplemental credentials for authenticating via an authentication broker. An authentication broker is an application that runs on a user's machine that manages the authentication handshakes and token maintenance for connected accounts. ...

Features:
- Allow silent authentication attempts on all platforms. Previously, `use_default_broker_account=True` in `InteractiveBrowserBrokerCredential` only applied to Windows/WSL. (#42375)

Example:
```python
# On Windows
import win32gui
from azure.identity.broker import InteractiveBrowserBrokerCredential
from azure.storage.blob import BlobServiceClient

# Get the handle of the current window
current_window_handle = win32gui.GetForegroundWindow()

...

</details>

### aws-cdk.aws-lambda

The CDK Construct Library for AWS::Lambda

`pip install aws-cdk.aws-lambda` · installs (wheel) · licence: OSI Approved · rank 11821 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-lambda/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This construct library allows you to define AWS Lambda Functions.

Example:
```python
fn = lambda.Function(self, "MyFunction",
    runtime=lambda.Runtime.NODEJS_16_X,
    handler="index.handler",
    code=lambda.Code.from_asset(path.join(__dirname, "lambda-handler"))
)
```

...

</details>

### arm-pytorch-utilities

Utilities for working with pytorch

`pip install arm-pytorch-utilities` · installs (wheel) · licence: MIT License · rank 11824 · last release 2026-03-10 · [PyPI](https://pypi.org/project/arm-pytorch-utilities/) · [source](https://github.com/UM-ARM-Lab/arm_pytorch_utilities)

### aws-cdk.aws-applicationautoscaling

The CDK Construct Library for AWS::ApplicationAutoScaling

`pip install aws-cdk.aws-applicationautoscaling` · installs (wheel) · licence: OSI Approved · rank 11825 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-applicationautoscaling/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# resource: SomeScalableResource

capacity = resource.auto_scale_capacity(
    min_capacity=5,
    max_capacity=100
)
```

Sections: AWS Auto Scaling Construct Library, AutoScaling basics, Step Scaling, Scaling based on multiple datapoints, Target Tracking Scaling, Scheduled Scaling, Examples, Lambda Provisioned Concurrency Auto Scaling, ElastiCache Redis shards scaling with target value

</details>

### aws-cdk.aws-autoscaling-common

Common implementation package for @aws-cdk/aws-autoscaling and @aws-cdk/aws-applicationautoscaling

`pip install aws-cdk.aws-autoscaling-common` · installs (wheel) · licence: OSI Approved · rank 11861 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-autoscaling-common/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

</details>

### aws-cdk.aws-ecr

The CDK Construct Library for AWS::ECR

`pip install aws-cdk.aws-ecr` · installs (wheel) · licence: OSI Approved · rank 11882 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-ecr/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
repository = ecr.Repository(self, "Repository")
```

Sections: Amazon ECR Construct Library, Repositories, Image scanning, Image tag immutability, Encryption, Automatically clean up repositories

</details>

### aws-cdk.aws-sns

The CDK Construct Library for AWS::SNS

`pip install aws-cdk.aws-sns` · installs (wheel) · licence: OSI Approved · rank 11889 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-sns/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Add an SNS Topic to your stack: ...

Example:
```python
from aws_cdk.aws_kinesisfirehose import DeliveryStream
# stream: DeliveryStream

topic = sns.Topic(self, "Topic")

sns.Subscription(self, "Subscription",
    topic=topic,
    endpoint=stream.delivery_stream_arn,
    protocol=sns.SubscriptionProtocol.FIREHOSE,
    subscription_role_arn="SAMPLE_ARN"
)
```

...

</details>

### aiohttp-sse-client

A Server-Sent Event python client base on aiohttp

`pip install aiohttp-sse-client` · installs (wheel) · licence: Apache Software License · rank 11895 · last release 2021-02-27 · [PyPI](https://pypi.org/project/aiohttp-sse-client/)

<details><summary>README extract</summary>

A Server-Sent Event python client base on aiohttp, provides a simple interface to process Server-Sent Event.

* Free software: Apache Software License 2.0

Features:
* Full asyncio support
* Easy to integrate with other aiohttp based project
* Auto-reconnect for network issue
* Support python 3.6 and above

Example:
```python
from aiohttp_sse_client import client as sse_client

async with sse_client.EventSource(
    '
) as event_source:
    try:
        async for event in event_source:
            print(event)
    except ConnectionError:
        pass
```

Sections: SSE Client, Features, Usage, 0.2.1 (2021-02-27), 0.2.0 (2020-10-20), 0.1.7 (2020-03-30), 0.1.6 (2019-08-06), 0.1.5 (2019-08-06), 0.1.4 (2018-10-04), 0.1.3 (2018-10-03), 0.1.2 (2018-10-03), 0.1.1 (2018-10-02)

</details>

### aws-cdk.aws-certificatemanager

The CDK Construct Library for AWS::CertificateManager

`pip install aws-cdk.aws-certificatemanager` · installs (wheel) · licence: OSI Approved · rank 11899 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-certificatemanager/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
my_hosted_zone = route53.HostedZone(self, "HostedZone",
    zone_name="example.com"
)
acm.Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=acm.CertificateValidation.from_dns(my_hosted_zone)
)
```

Sections: AWS Certificate Manager Construct Library, DNS validation, Email validation, Cross-region Certificates, Requesting private certificates, Importing, Sharing between Stacks, Metrics

</details>

### aws-cdk.aws-ecr-assets

Docker image assets deployed to ECR

`pip install aws-cdk.aws-ecr-assets` · installs (wheel) · licence: OSI Approved · rank 11906 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-ecr-assets/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module allows bundling Docker images as assets. ...

Example:
```python
from aws_cdk.aws_ecr_assets import DockerImageAsset

asset = DockerImageAsset(self, "MyBuildImage",
    directory=path.join(__dirname, "my-image")
)
```

Sections: AWS CDK Docker Image Assets, Images from Dockerfile, Images from Tarball, Publishing images to ECR repositories, Pull Permissions

</details>

### argilla

The Argilla python server SDK

`pip install argilla` · installs (wheel) · licence: Apache 2.0 · rank 11914 · last release 2025-03-10 · [PyPI](https://pypi.org/project/argilla/)

<details><summary>README extract</summary>

Argilla

Work on data together, make your model outputs better!

Argilla is a collaboration tool for AI engineers and domain experts who need to build high-quality datasets for their projects.
If you just want to get started, we recommend our UI demo or our free Hugging Face Spaces deployment integration. ...

Features:
Whether you are working on monitoring and improving complex generative tasks involving LLM pipelines with RAG, or you are working on a predictive task for things like AB-testing of span- and text-classification models. ...

Example:
```python
settings = rg.Settings(
    guidelines="Classify the reviews as positive or negative.",
    fields=[
        rg.TextField(
            name="review",
            title="Text from the review",
            use_markdown=False,
        ),
...

</details>

### aws-cdk.aws-efs

The CDK Construct Library for AWS::EFS

`pip install aws-cdk.aws-efs` · installs (wheel) · licence: OSI Approved · rank 11925 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-efs/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
file_system = efs.FileSystem(self, "MyEfsFileSystem",
    vpc=ec2.Vpc(self, "VPC"),
    lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
    performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
...
```

Sections: Amazon Elastic File System Construct Library, File Systems, Create an Amazon EFS file system, Permissions, Access Point, Connecting, Mounting the file system using User Data, Deleting

</details>

### azure-maps-search

Microsoft Azure Maps Search Client Library for Python

`pip install azure-maps-search` · installs (wheel) · licence: MIT License · rank 11927 · last release 2024-12-12 · [PyPI](https://pypi.org/project/azure-maps-search/)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Maps Services for Search.
Read more about Azure Maps Services here

Source code | API reference documentation | Product documentation

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to <

Features:
- Integrated support for SAS-based authentication

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.maps.search import MapsSearchClient

credential = AzureKeyCredential(os.environ.get("AZURE_SUBSCRIPTION_KEY"))

search_client = MapsSearchClient(
    credential=credential,
)
```

...

</details>

### aresponses

Asyncio response mocking. Similar to the responses library used for 'requests'

`pip install aresponses` · installs (wheel) · licence: MIT License · rank 11930 · last release 2024-01-12 · [PyPI](https://pypi.org/project/aresponses/)

<details><summary>README extract</summary>

an asyncio testing server for mocking external services

Features:
- Fast mocks using actual network connections
 - allows mocking some types of network issues
 - use regular expression matching for domain, path, method, or body
 - works with https requests as well (by switching them to http requests)
 - works with ...

Example:
```python
def add(
    host_pattern=ANY,
    path_pattern=ANY,
    method_pattern=ANY,
    response="",
    *,
    route=None,
    body_pattern=ANY, m
    match_querystring=False,
    repeat=1
    )
```

Sections: aresponses, Features, Usage, Assertions, Regex and Repeat, Json Responses, Custom Handler, Passthrough, Context manager usage, working with pytest-aiohttp, Dev environment setup, Submitting a feature request, Updating package on pypi, 3.0.0

</details>

### aws-cdk.aws-cloudformation

The CDK Construct Library for AWS::CloudFormation

`pip install aws-cdk.aws-cloudformation` · installs (wheel) · licence: OSI Approved · rank 11936 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-cloudformation/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> This API may emit warnings. Backward compatibility is not guaranteed.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project.

</details>

### aws-durable-execution-sdk-python-testing

AWS Durable Execution Testing SDK for Python

`pip install aws-durable-execution-sdk-python-testing` · installs (wheel) · licence: Apache-2.0 · rank 11939 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-durable-execution-sdk-python-testing/) · [docs](https://github.com/aws/aws-durable-execution-sdk-python-testing#readme) · [source](https://github.com/aws/aws-durable-execution-sdk-python-testing)

<details><summary>README extract</summary>

Features:
Use the AWS Durable Execution Testing SDK for Python to test your Python durable functions locally.

The test framework contains a local runner, so you can run and test your durable function locally
before you deploy it.

Example:
```python
from aws_durable_execution_sdk_python.context import (
    DurableContext,
    durable_step,
    durable_with_child_context,
)
from aws_durable_execution_sdk_python.execution import durable_execution
from aws_durable_execution_sdk_python.config import Duration

@durable_step
def one(a: int, b: int) -> str:
    return f"{a} {b}"

@durable_step
...
```

Sections: Overview, Quick Start, A durable function under test, Your test code, In-process runner, Architecture, Documentation, Error Handling

</details>

### asyncio-pool

Pool of asyncio coroutines with familiar interface

`pip install asyncio-pool` · installs (wheel) · licence: MIT License · rank 11942 · last release 2022-05-21 · [PyPI](https://pypi.org/project/asyncio-pool/)

<details><summary>README extract</summary>

Pool of asyncio coroutines with familiar interface. Supports python 3.5+ (including PyPy 6+, which is also 3.5 atm)

AioPool makes sure _no more and _no less (if possible) than `size` spawned coroutines are active at the same time. ...

</details>

### aiohttp-xmlrpc

aiohttp XML-RPC server handler and client

`pip install aiohttp-xmlrpc` · installs (wheel) · licence: MIT · rank 11963 · last release 2022-01-11 · [PyPI](https://pypi.org/project/aiohttp-xmlrpc/) · [source](https://github.com/mosquito/aiohttp-xmlrpc)

<details><summary>README extract</summary>

XML-RPC server and client implementation based on aiohttp. Using lxml and aiohttp.Client.

Example:
```python
from aiohttp import web
from aiohttp_xmlrpc import handler
from aiohttp_xmlrpc.handler import rename

class XMLRPCExample(handler.XMLRPCView):

    @rename("nested.test")
    def rpc_test(self):
        return None

    def rpc_args(self, *args):
        return len(args)

    def rpc_kwargs(self, **kwargs):
        return len(kwargs)

...
```

Sections: AIOHTTP XMLRPC, Server example, Client example

</details>

### aws-lambda-context

AWS Lambda Context class for type checking and testing

`pip install aws-lambda-context` · installs (wheel) · licence: MIT License · rank 11964 · last release 2019-07-17 · [PyPI](https://pypi.org/project/aws-lambda-context/)

<details><summary>README extract</summary>

A micro library that provides the AWS Lambda Context class for type checking and testing.

Example:
```python
from aws_lambda_context import LambdaContext

def my_lambda_handler(event: Any, context: LambdaContext) -> None:
    ...
```

Sections: Python Lambda Context, Usage, References

</details>

### aspy.refactor-imports

Utilities for refactoring imports in python-like syntax.

`pip install aspy.refactor-imports` · installs (wheel) · licence: MIT License · rank 11988 · last release 2022-07-01 · [PyPI](https://pypi.org/project/aspy.refactor-imports/)

<details><summary>README extract</summary>

this library has been rewritten and renamed to `classify-imports` for version 4

Utilities for refactoring imports in python-like syntax.

Example:
```python
>>> from aspy.refactor_imports.import_obj import FromImport
>>> from aspy.refactor_imports.import_obj import ImportImport
>>> FromImport.from_str('from foo import bar').to_text()
'from foo import bar\n'
>>> ImportImport.from_str('import bar as baz').to_text()
'import bar as baz\n'
```

Sections: RENAMED, aspy.refactor_imports, Examples, aspy.refactor_imports.import_obj, Constructing an import object, Splitting an import object, Sorting import objects, aspy.refactor_imports.classify, Classify a module, Also as convenient constants

</details>

### aws-cdk.aws-elasticloadbalancingv2

The CDK Construct Library for AWS::ElasticLoadBalancingV2

`pip install aws-cdk.aws-elasticloadbalancingv2` · installs (wheel) · licence: OSI Approved · rank 12017 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-elasticloadbalancingv2/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
from aws_cdk.aws_autoscaling import AutoScalingGroup
# asg: AutoScalingGroup

# vpc: ec2.Vpc

# Create the load balancer in a VPC. 'internetFacing' is 'false'
# by default, which creates an internal load balancer.
lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)

...
```

...

</details>

### aws-cdk.aws-codeguruprofiler

The CDK Construct Library for AWS::CodeGuruProfiler

`pip install aws-cdk.aws-codeguruprofiler` · installs (wheel) · licence: OSI Approved · rank 12032 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-codeguruprofiler/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# The execution role of your application that publishes to the ProfilingGroup via CodeGuru Profiler Profiling Agent. (the following is merely an example)
publish_app_role = iam.Role(self, "PublishAppRole",
    assumed_by=iam.AccountRootPrincipal()
)

profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup")
...
```

Sections: AWS::CodeGuruProfiler Construct Library, Basic usage, Compute Platform configuration

</details>

### async-tiff

(no summary)

`pip install async-tiff` · installs (wheel) · licence: not stated · rank 12041 · last release 2026-05-06 · [PyPI](https://pypi.org/project/async-tiff/)

<details><summary>README extract</summary>

[][pypi_link]

Fast, low-level async TIFF reader for Python.

This documentation is for the Python bindings. Refer here for the Rust crate documentation.

For a higher-level API to read GeoTIFF files, visit `async-geotiff`.

Example:
```python
from async_tiff import TIFF
from async_tiff.store import S3Store

# You'll also need to provide credentials to access a requester pays bucket
store = S3Store("naip-visualization", region="us-west-2", request_payer=True)
path = "ny/2022/60cm/rgb/40073/m_4007307_sw_18_060_20220803.tif"

tiff = await TIFF.open(path, store=store)
...
```

Sections: async-tiff, Examples, Reading NAIP, Reading Sentinel 2 L2A

</details>

### ansitable

Quick and easy display of tabular data and matrices with optional ANSI color and borders

`pip install ansitable` · installs (wheel) · licence: MIT License · rank 12054 · last release 2026-10-12 · [PyPI](https://pypi.org/project/ansitable/) · [docs](https://petercorke.github.io/ansitable) · [source](https://github.com/petercorke/ansitable)

<details><summary>README extract</summary>

Pretty tables and matrices for Python

 GitHub •
 Conda •
 Quick example

Features:
- Unicode and ANSI colors — Beautiful output in any ANSI-capable terminal
- 7 export formats — Markdown, HTML, LaTeX, reStructuredText, Wikitable, CSV, Pandas ...

Example:
```python
from ansitable import ANSITable

table = ANSITable("Name", "Score", border="thin")
table.row("Alice", 95)
table.row("Bob", 87)
table.row("Carol", 92)
table.print()
```

Sections: ANSITable, Ecosystem & Dependencies, Quick example, Features, Documentation

</details>

### aws-cdk.aws-route53

The CDK Construct Library for AWS::Route53

`pip install aws-cdk.aws-route53` · installs (wheel) · licence: OSI Approved · rank 12058 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-route53/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

To add a public hosted zone: ...

Example:
```python
route53.PublicHostedZone(self, "HostedZone",
    zone_name="fully.qualified.domain.com"
)
```

Sections: Amazon Route53 Construct Library, Adding Records, Imports, VPC Endpoint Service Private DNS

</details>

### aws-cdk.custom-resources

Constructs for implementing CDK custom resources

`pip install aws-cdk.custom-resources` · installs (wheel) · licence: OSI Approved · rank 12060 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.custom-resources/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# on_event: lambda.Function
# is_complete: lambda.Function
# my_role: iam.Role

my_provider = cr.Provider(self, "MyProvider",
    on_event_handler=on_event,
    is_complete_handler=is_complete,  # optional async "waiter"
    log_retention=logs.RetentionDays.ONE_DAY,  # default is INFINITE
    role=my_role
)

...
```

...

</details>

### azure-postgresql-auth

Microsoft Azure PostgreSQL Auth Library for Python

`pip install azure-postgresql-auth` · installs (wheel) · licence: MIT · rank 12061 · last release 2026-09-01 · [PyPI](https://pypi.org/project/azure-postgresql-auth/) · [source](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/postgresql/azure-postgresql-auth)

<details><summary>README extract</summary>

The Azure PostgreSQL Auth client library provides Microsoft Entra ID authentication for Python database drivers connecting to Azure Database for PostgreSQL. It supports psycopg2, psycopg3, and SQLAlchemy with automatic token management and connection pooling.

Source code
| Package (PyPI)
| Samples

Features:
- Added `create_asyncpg_engine` for SQLAlchemy async engines using `asyncpg` and asynchronous Microsoft Entra credentials.

Example:
```python
from azure_postgresql_auth.psycopg2 import EntraConnection
from azure.identity import DefaultAzureCredential
from psycopg2 import pool
from functools import partial

credential = DefaultAzureCredential()
connection_factory = partial(EntraConnection, credential=credential)

connection_pool = pool.ThreadedConnectionPool(
    minconn=1,
...
```

...

</details>

### azurefunctions-extensions-base

Base Python worker extension for Azure Functions.

`pip install azurefunctions-extensions-base` · installs (wheel) · licence: MIT License · rank 12079 · last release 2026-05-12 · [PyPI](https://pypi.org/project/azurefunctions-extensions-base/)

<details><summary>README extract</summary>

This is the base library for allowing Python Function Apps to recognize and bind to SDk-types and HttpV2-types. It is not to be used directly.
Instead, please reference one of the extending packages:
* azurefunctions-extensions-http-fastapi
* azurefunctions-extensions-bindings-blob
* azurefunctions-extensions-bindings-cosmosdb
* ...

</details>

### aliyun-log-fastpb

Fast protobuf serialization for Aliyun Log using PyO3 and quick-protobuf

`pip install aliyun-log-fastpb` · installs (wheel) · licence: MIT License · rank 12088 · last release 2026-04-28 · [PyPI](https://pypi.org/project/aliyun-log-fastpb/)

<details><summary>README extract</summary>

中文文档 | English

Fast protobuf serialization for Aliyun Log using PyO3 and quick-protobuf.

Example:
```python
import aliyun_log_fastpb

# Prepare log data
log_group = {
    "LogItems": [
        {
            "Time": 1234567890,
            "Contents": [
                {"Key": "level", "Value": "INFO"},
                {"Key": "message", "Value": "Application started"}
            ]
        }
    ],
    "LogTags": [
...
```

Sections: aliyun-log-fastpb, Quick Start

</details>

### aws-cdk.aws-autoscaling

The CDK Construct Library for AWS::AutoScaling

`pip install aws-cdk.aws-autoscaling` · installs (wheel) · licence: OSI Approved · rank 12100 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-autoscaling/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project.

Example:
```python
# vpc: ec2.Vpc

autoscaling.AutoScalingGroup(self, "ASG",
    vpc=vpc,
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
    machine_image=ec2.AmazonLinuxImage()
)
```

...

</details>

### aimsim-core

Core AIMSim molecular featurization and comparison utilities.

`pip install aimsim-core` · installs (wheel) · licence: MIT · rank 12127 · last release 2025-09-09 · [PyPI](https://pypi.org/project/aimsim-core/)

<details><summary>README extract</summary>

Repository Status:

AIMSim has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.

Downloads Stats:

Sections: AIMSim README, Visualizing Diversity in your Molecular Dataset, Documentation and Tutorial, Purpose, `pip`, `conda`, Note for mordred-descriptor, Running AIMSim, Currently Implemented Fingerprints, Currently Implemented Similarity Scores, Currently Implemented Functionalities, `AIMSim` in the Literature

</details>

### aws-cdk.aws-elasticloadbalancing

The CDK Construct Library for AWS::ElasticLoadBalancing

`pip install aws-cdk.aws-elasticloadbalancing` · installs (wheel) · licence: OSI Approved · rank 12154 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-elasticloadbalancing/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# vpc: ec2.IVpc

# my_auto_scaling_group: autoscaling.AutoScalingGroup

lb = elb.LoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True,
    health_check=elb.HealthCheck(
        port=80
    )
)
lb.add_target(my_auto_scaling_group)
lb.add_listener(
    external_port=80
)
```

Sections: Amazon Elastic Load Balancing Construct Library, Configuring a Load Balancer

</details>

### aws-cdk.aws-codestarnotifications

The CDK Construct Library for AWS::CodeStarNotifications

`pip install aws-cdk.aws-codestarnotifications` · installs (wheel) · licence: OSI Approved · rank 12177 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-codestarnotifications/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project.

Example:
```python
import aws_cdk.aws_codestarnotifications as notifications
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_sns as sns
import aws_cdk.aws_chatbot as chatbot

project = codebuild.PipelineProject(self, "MyProject")

topic = sns.Topic(self, "MyTopic1")

slack = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
...
```

...

</details>

### aimrecords

A record-oriented data format which utilizes Protocol Buffers

`pip install aimrecords` · installs (wheel) · licence: MIT License · rank 12181 · last release 2020-11-09 · [PyPI](https://pypi.org/project/aimrecords/)

<details><summary>README extract</summary>

Library to effectively store the tracked experiment logs.

See the documentation here.

Sections: AimRecords - Record-oriented data storage, Getting Started, Requirements, Project Structure, Running the tests, Code Style

</details>

### aws-cdk.lambda-layer-kubectl-v35

A Lambda Layer that contains kubectl v1.35

`pip install aws-cdk.lambda-layer-kubectl-v35` · installs (wheel) · licence: OSI Approved · rank 12183 · last release 2026-05-13 · [PyPI](https://pypi.org/project/aws-cdk.lambda-layer-kubectl-v35/) · [source](https://github.com/cdklabs/awscdk-asset-kubectl.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

<!--END STABILITY BANNER-->

This module exports a single class called `KubectlV35Layer` which is a `lambda.LayerVersion` that
bundles the `kubectl` and the
`helm` command line.

> * Helm Version: 4.1.3
> * Kubectl Version: 1.35.2

Usage: ...

Example:
```python
# KubectlLayer bundles the 'kubectl' and 'helm' command lines
from aws_cdk.lambda_layer_kubectl_v35 import KubectlV35Layer
import aws_cdk.aws_lambda as lambda

# fn: lambda.Function

kubectl = KubectlV35Layer(self, "KubectlLayer")
fn.add_layers(kubectl)
```

</details>

### azure-cli-diff-tool

A tool for cli metadata management

`pip install azure-cli-diff-tool` · installs (wheel) · licence: MIT · rank 12188 · last release 2026-10-29 · [PyPI](https://pypi.org/project/azure-cli-diff-tool/)

<details><summary>README extract</summary>

The `azure-cli-diff-tool` is designed to aid azure-cli users in diffing metadata files to see its updates through historical versions for Azure CLI command modules and extensions.

1. Install Python 3.6+ from Please note that the version of Python that comes preinstalled on OSX is 2.7.

3. ...

Sections: Microsoft Azure CLI Diff Tools (azure-cli-diff-tool), Setting up your environment, Reporting issues and feedback, 0.1.2, 0.1.1, 0.1.0, 0.0.9, 0.0.8, 0.0.7, 0.0.6, 0.0.5, 0.0.4, 0.0.3, 0.0.2

</details>

### amazon-kclpy

A python interface for the Amazon Kinesis Client Library MultiLangDaemon

`pip install amazon-kclpy` · installs from source (sdist only) · licence: Apache-2.0 · rank 12194 · last release 2026-10-15 · [PyPI](https://pypi.org/project/amazon-kclpy/)

### aim-ui

Aim UI

`pip install aim-ui` · installs from source (sdist only) · licence: not stated · rank 12209 · last release 2025-05-08 · [PyPI](https://pypi.org/project/aim-ui/)

### aws-cdk.aws-signer

The CDK Construct Library for AWS::Signer

`pip install aws-cdk.aws-signer` · installs (wheel) · licence: OSI Approved · rank 12213 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-signer/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
signing_profile = signer.SigningProfile(self, "SigningProfile",
    platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
)
```

Sections: AWS::Signer Construct Library, Signing Platform, Signing Profile

</details>

### airflow-provider-duckdb

DuckDB (duckdb.org) provider for Apache Airflow

`pip install airflow-provider-duckdb` · installs (wheel) · licence: Apache License 2.0 · rank 12224 · last release 2023-06-26 · [PyPI](https://pypi.org/project/airflow-provider-duckdb/)

<details><summary>README extract</summary>

A DuckDB provider for Airflow. This provider exposes a hook/connection that returns a DuckDB connection.

This works for either local or MotherDuck connections.

Example:
```python
import pandas as pd
import pendulum

from airflow.decorators import dag, task
from duckdb_provider.hooks.duckdb_hook import DuckDBHook

@dag(
    schedule=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
)
def duckdb_transform():
    @task
    def create_df() -> pd.DataFrame:
        """
...
```

Sections: airflow-provider-duckdb, Connection, Usage

</details>

### aws-cdk.aws-sns-subscriptions

CDK Subscription Constructs for AWS SNS

`pip install aws-cdk.aws-sns-subscriptions` · installs (wheel) · licence: OSI Approved · rank 12225 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-sns-subscriptions/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
my_topic = sns.Topic(self, "MyTopic")
```

Sections: Subscriptions, HTTPS, Amazon SQS, AWS Lambda, Email, SMS

</details>

### alpaca-trade-api

Alpaca API python client

`pip install alpaca-trade-api` · installs (wheel) · licence: not stated · rank 12242 · last release 2024-01-12 · [PyPI](https://pypi.org/project/alpaca-trade-api/)

<details><summary>README extract</summary>

A new python SDK, Alpaca-py, is available. This SDK will be the primary python SDK starting in 2023. We recommend moving over your code to use the new SDK. Keep in mind, we will be maintaining this repo as usual until the end of 2022.

`alpaca-trade-api-python` is a python library for the Alpaca Commission Free Trading API. ...

Example:
```python
from alpaca_trade_api.rest import REST, TimeFrame
api = REST()

api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df

                              open      high       low     close    volume
timestamp
2021-06-08 08:00:00+00:00  126.100  126.3000  125.9600  126.3000     42107
...
```

...

</details>

### aws-cdk.aws-apigateway

The CDK Construct Library for AWS::ApiGateway

`pip install aws-cdk.aws-apigateway` · installs (wheel) · licence: OSI Approved · rank 12247 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-apigateway/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# integration: apigateway.LambdaIntegration

api = apigateway.RestApi(self, "hello-api")

v1 = api.root.add_resource("v1")
echo = v1.add_resource("echo")
echo_method = echo.add_method("GET", integration, api_key_required=True)

plan = api.add_usage_plan("UsagePlan",
    name="Easy",
    throttle=apigateway.ThrottleSettings(
        rate_limit=10,
...
```

...

</details>

### aws-cdk.aws-cloudfront

The CDK Construct Library for AWS::CloudFront

`pip install aws-cdk.aws-cloudfront` · installs (wheel) · licence: OSI Approved · rank 12255 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-cloudfront/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# Creates a distribution from an S3 bucket.
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket))
)
```

...

</details>

### async-upnp-client

Async UPnP Client

`pip install async-upnp-client` · installs (wheel) · licence: Apache-2.0 · rank 12260 · last release 2026-10-11 · [PyPI](https://pypi.org/project/async-upnp-client/)

<details><summary>README extract</summary>

Asyncio UPnP Client library for Python/asyncio.

Written initially for use in Home Assistant to drive `DLNA DMR`-capable devices, but useful for other projects as well.

Sections: Async UPnP Client, General set up, Changes, Releasing, Profiling, upnp-client

</details>

### aws-cdk.aws-secretsmanager

The CDK Construct Library for AWS::SecretsManager

`pip install aws-cdk.aws-secretsmanager` · installs (wheel) · licence: OSI Approved · rank 12287 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-secretsmanager/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Example:
```python
import aws_cdk.aws_secretsmanager as secretsmanager
```

Sections: AWS Secrets Manager Construct Library, Create a new Secret in a Stack, Grant permission to use the secret to a role, Rotating a Secret, Using a Custom Lambda Function, Using a Hosted Lambda Function, Rotating database credentials, Importing Secrets, Replicating secrets

</details>

### aws-cdk.aws-ecs

The CDK Construct Library for AWS::ECS

`pip install aws-cdk.aws-ecs` · installs (wheel) · licence: OSI Approved · rank 12308 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-ecs/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# vpc: ec2.Vpc

# Create an ECS cluster
cluster = ecs.Cluster(self, "Cluster",
    vpc=vpc
)

# Add capacity to it
cluster.add_capacity("DefaultAutoScalingGroupCapacity",
    instance_type=ec2.InstanceType("t2.xlarge"),
    desired_capacity=3
)

task_definition = ecs.Ec2TaskDefinition(self, "TaskDef")

...
```

...

</details>

### aws-cdk.aws-kinesisanalytics-flink-alpha

A CDK Construct Library for Kinesis Analytics Flink applications

`pip install aws-cdk.aws-kinesisanalytics-flink-alpha` · installs (wheel) · licence: OSI Approved · rank 12309 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-kinesisanalytics-flink-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
import path as path
import aws_cdk.integ_tests_alpha as integ
import aws_cdk as core
import aws_cdk.aws_cloudwatch as cloudwatch
import aws_cdk.aws_kinesisanalytics_flink_alpha as flink

app = core.App()
stack = core.Stack(app, "FlinkAppTest")

...
```

Sections: Kinesis Analytics Flink, Creating Flink Applications

</details>

### aws-cdk.aws-cognito

The CDK Construct Library for AWS::Cognito

`pip install aws-cdk.aws-cognito` · installs (wheel) · licence: OSI Approved · rank 12328 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-cognito/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

Features | Stability ...

Example:
```python
cognito.UserPool(self, "myuserpool",
    user_pool_name="myawesomeapp-userpool"
)
```

Sections: Amazon Cognito Construct Library, User Pools, Sign Up, Sign In, Attributes, Multi-factor Authentication (MFA), Account Recovery Settings, Emails, Device Tracking, Lambda Triggers, Trigger Permissions, Importing User Pools, Identity Providers, App Clients

</details>

### apig-wsgi

Wrap a WSGI application in an AWS Lambda handler function for running on API Gateway or an ALB.

`pip install apig-wsgi` · installs (wheel) · licence: MIT · rank 12331 · last release 2025-09-08 · [PyPI](https://pypi.org/project/apig-wsgi/) · [source](https://github.com/adamchainz/apig-wsgi)

<details><summary>README extract</summary>

Wrap a WSGI application in an AWS Lambda handler function for running on API Gateway or an ALB.

A quick example:

Improve your Django and Git skills with my books.

Example:
```python
from apig_wsgi import make_lambda_handler
from myapp.wsgi import app

# Configure this as your entry point in AWS Lambda
lambda_handler = make_lambda_handler(app)
```

Sections: apig-wsgi, Usage, Example

</details>

### aws-cdk.aws-servicediscovery

The CDK Construct Library for AWS::ServiceDiscovery

`pip install aws-cdk.aws-servicediscovery` · installs (wheel) · licence: OSI Approved · rank 12333 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-servicediscovery/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project. ...

Example:
```python
import aws_cdk.core as cdk
import aws_cdk.aws_servicediscovery as servicediscovery

app = cdk.App()
stack = cdk.Stack(app, "aws-servicediscovery-integ")

namespace = servicediscovery.HttpNamespace(stack, "MyNamespace",
    name="covfefe"
)

service1 = namespace.create_service("NonIpService",
    description="service registering non-ip instances"
)
...
```

...

</details>

### astral-dev-toolchain-cargo-shear

Detect and fix unused/misplaced dependencies from Cargo.toml

`pip install astral-dev-toolchain-cargo-shear` · installs (wheel) · licence: MIT · rank 12341 · last release 2026-10-07 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-shear/) · [source](https://github.com/Boshen/cargo-shear)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-shear` from tag `v1.14.0` at commit `e789f424d9b780d207c06342c63ef95609389fd6`.

Detect and fix issues in Rust projects:

- Unused dependencies in `Cargo.toml` ...

Sections: Cargo Shear ✂️ 🐑, Usage, Limitations, Configuration, Ignore false positives, Ignore unlinked files, Ignore scope, Keep pre-declared path dependencies, cargo-hakari `workspace-hack` crates, CI, JSON Output for CI Integration, Exit Code (for CI), Strict Mode with `--deny-warnings`, Technique

</details>

### azureml-inference-server-http

Azure Machine Learning inferencing server.

`pip install azureml-inference-server-http` · installs (wheel) · licence: Other/Proprietary License · rank 12352 · last release 2025-12-18 · [PyPI](https://pypi.org/project/azureml-inference-server-http/)

<details><summary>README extract</summary>

Check our official documentation AzureML Inference Server - Docs.

Please note, the AzureML Inference Server is now open source! The repo is available here: AzureML Inference Server - Github.

Features:
- Added ability to configure seperate dedicated health check port.

Sections: 1.5.1 (2025-12-18), Azureml_Inference_Server_Http 1.5.1 (2025-12-18), Enhancements, 1.5.0 (2025-08-13), Azureml_Inference_Server_Http 1.5.0 (2025-08-13), 1.4.1 (2025-06-10), Azureml_Inference_Server_Http 1.4.1 (2025-06-10), 1.4.0 (2024-11-13), Azureml_Inference_Server_Http 1.4.0 (2024-11-13), Deprecation, 1.3.4 (2024-10-21), Azureml_Inference_Server_Http 1.3.4 (2024-10-21)

</details>

### aspy.yaml

A few extensions to pyyaml.

`pip install aspy.yaml` · installs (wheel) · licence: MIT License · rank 12356 · last release 2019-05-23 · [PyPI](https://pypi.org/project/aspy.yaml/)

<details><summary>README extract</summary>

Some extensions to pyyaml.

Example:
```python
>>> from aspy.yaml import ordered_load
>>> ordered_load(
        'foo: bar\n'
        'bar: baz\n'
        'herp: derp\n'
    )
OrderedDict([('foo', 'bar'), ('bar', 'baz'), ('herp', 'derp')])
```

Sections: aspy.yaml, aspy.yaml.ordered_load, aspy.yaml.ordered_dump

</details>

### aws-cdk.aws-codebuild

The CDK Construct Library for AWS::CodeBuild

`pip install aws-cdk.aws-codebuild` · installs (wheel) · licence: OSI Approved · rank 12363 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-codebuild/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
codebuild.Project(self, "Project",
    logging=codebuild.LoggingOptions(
        cloud_watch=codebuild.CloudWatchLoggingOptions(
            log_group=logs.LogGroup(self, "MyLogGroup")
        )
    )
)
```

Sections: AWS CodeBuild Construct Library, Source, `CodeCommitSource`, `S3Source`, `GitHubSource` and `GitHubEnterpriseSource`, `BitBucketSource`, For all Git sources, Artifacts, CodePipeline, Caching, S3 Caching, Local Caching, Environment, Images

</details>

### aws-cdk.aws-sam

The CDK Construct Library for the AWS Serverless Application Model (SAM) resources

`pip install aws-cdk.aws-sam` · installs (wheel) · licence: OSI Approved · rank 12382 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-sam/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project. ...

Example:
```python
import aws_cdk.aws_sam as serverless
```

</details>

### aws-cdk.aws-autoscaling-hooktargets

Lifecycle hook for AWS AutoScaling

`pip install aws-cdk.aws-autoscaling-hooktargets` · installs (wheel) · licence: OSI Approved · rank 12386 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-autoscaling-hooktargets/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

</details>

### aws-cdk.aws-route53-targets

The CDK Construct Library for AWS Route53 Alias Targets

`pip install aws-cdk.aws-route53-targets` · installs (wheel) · licence: OSI Approved · rank 12389 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-route53-targets/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This library contains Route53 Alias Record targets for: ...

Example:
```python
import aws_cdk.aws_apigateway as apigw

# zone: route53.HostedZone
# rest_api: apigw.LambdaRestApi

route53.ARecord(self, "AliasRecord",
    zone=zone,
    target=route53.RecordTarget.from_alias(targets.ApiGateway(rest_api))
)
```

</details>

### aws-cdk.aws-kinesis

The CDK Construct Library for AWS::Kinesis

`pip install aws-cdk.aws-kinesis` · installs (wheel) · licence: OSI Approved · rank 12390 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-kinesis/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
kinesis.Stream(self, "MyFirstStream",
    stream_name="my-awesome-stream"
)
```

Sections: Amazon Kinesis Construct Library, Streams, Encryption, Import, Permission Grants, Read Permissions, Write Permissions, Custom Permissions, Metrics

</details>

### aws-cdk.aws-stepfunctions

The CDK Construct Library for AWS::StepFunctions

`pip install aws-cdk.aws-stepfunctions` · installs (wheel) · licence: OSI Approved · rank 12393 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-stepfunctions/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
import aws_cdk.aws_lambda as lambda

# submit_lambda: lambda.Function
# get_status_lambda: lambda.Function

submit_job = tasks.LambdaInvoke(self, "Submit Job",
    lambda_function=submit_lambda,
    # Lambda's result is in the attribute `Payload`
    output_path="$.Payload"
)

wait_x = sfn.Wait(self, "Wait X Seconds",
...
```

...

</details>

### aws-cdk.aws-codecommit

The CDK Construct Library for AWS::CodeCommit

`pip install aws-cdk.aws-codecommit` · installs (wheel) · licence: OSI Approved · rank 12403 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-codecommit/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
repo = codecommit.Repository(self, "Repository",
    repository_name="MyRepositoryName",
    description="Some description."
)
```

Sections: AWS CodeCommit Construct Library, Add initial commit, Events, CodeStar Notifications

</details>

### agentops

Observability and DevTool Platform for AI Agents

`pip install agentops` · installs (wheel) · licence: MIT License · rank 12409 · last release 2025-08-29 · [PyPI](https://pypi.org/project/agentops/)

### aws-cdk.aws-acmpca

The CDK Construct Library for AWS::ACMPCA

`pip install aws-cdk.aws-acmpca` · installs (wheel) · licence: OSI Approved · rank 12434 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-acmpca/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project.

Example:
```python
import aws_cdk.aws_acmpca as acmpca
```

Sections: AWS::ACMPCA Construct Library, Low-level `Cfn*` classes

</details>

### async-stripe

An asynchronous wrapper around Stripe's official python library.

`pip install async-stripe` · installs (wheel) · licence: Other/Proprietary License · rank 12437 · last release 2023-11-18 · [PyPI](https://pypi.org/project/async-stripe/) · [source](https://github.com/bhch/async-stripe)

<details><summary>README extract</summary>

An asynchronous wrapper around Stripe's official python library.

async-stripe monkey-patches the stripe library and replaces the synchronous
http request methods with asynchronous methods.

Monkey-patching allows us to avoid a complete rewrite and keep the usage api
similar to the official library. ...

Example:
```python
from async_stripe import stripe

stripe.api_key = '<stripe-secret-key>'

payment_intent = await stripe.PaymentIntent.create(amount=1000, currency='usd')

print(payment_intent.id)
```

Sections: async-stripe, How it works, Usage, Configuration

</details>

### akamai-edgeauth

Akamai Edge Authorization Token for Property Manager Behavior

`pip install akamai-edgeauth` · installs from source (sdist only) · licence: Apache 2.0 · rank 12441 · last release 2018-06-15 · [PyPI](https://pypi.org/project/akamai-edgeauth/)

<details><summary>README extract</summary>

Example:
```python
from akamai.edgeauth import EdgeAuth, EdgeAuthError
import requests # just for this example

ET_HOSTNAME = 'edgeauth.akamaized.net'
ET_ENCRYPTION_KEY = 'YourEncryptionKey'
DURATION = 500 # seconds
```

Sections: Example, Usage, Test, Others, Command

</details>

### agilicus

Agilicus SDK

`pip install agilicus` · installs (wheel) · licence: MIT License · rank 12447 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agilicus/) · [source](https://github.com/Agilicus)

<details><summary>README extract</summary>

The Agilicus Platform API.
is defined using OpenAPI 3.0,
and may be used from any language. This allows configuration of our Zero-Trust Network Access cloud native platform
using REST. You can see the API specification online.

This package provides a Python SDK, class library interfaces for use in
accessing individual collections. ...

Example:
```python
import agilicus
import argparse
import sys

scopes = agilicus.scopes.DEFAULT_SCOPES

parser = argparse.ArgumentParser(description="update-user")
parser.add_argument("--auth-doc", type=str)
parser.add_argument("--issuer", type=str)
parser.add_argument("--email", type=str)
parser.add_argument("--disable-user", type=bool, default=None)
...
```

...

</details>

### anarcii

A language model suite for numbering antigen receptor sequences.

`pip install anarcii` · installs (wheel) · licence: not stated · rank 12484 · last release 2026-06-30 · [PyPI](https://pypi.org/project/anarcii/)

<details><summary>README extract</summary>

ANARCII is a generalised language model for antigen receptor numbering.

For the user guide please read the wiki page.

Sections: ANARCII, Web tool, Citing this work, The paper, The software

</details>

### aws-solutions-constructs.aws-cloudfront-s3

CDK Constructs for AWS Cloudfront to AWS S3 integration.

`pip install aws-solutions-constructs.aws-cloudfront-s3` · installs (wheel) · licence: OSI Approved · rank 12489 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aws-solutions-constructs.aws-cloudfront-s3/) · [source](https://github.com/awslabs/aws-solutions-constructs.git)

<details><summary>README extract</summary>

Documentation for this pattern can be found here

</details>

### aws-cdk.aws-dynamodb

The CDK Construct Library for AWS::DynamoDB

`pip install aws-cdk.aws-dynamodb` · installs (wheel) · licence: OSI Approved · rank 12551 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-dynamodb/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

Here is a minimal deployable DynamoDB table definition:

Example:
```python
table = dynamodb.Table(self, "Table",
    partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
)
```

Sections: Amazon DynamoDB Construct Library, Importing existing tables, Keys, Billing Mode, Table Class, Configure AutoScaling for your table, Amazon DynamoDB Global Tables, Encryption, Get schema of table or secondary indexes, Kinesis Stream

</details>

### antsibull-docutils

Antsibull docutils helpers

`pip install antsibull-docutils` · installs (wheel) · licence: GPL-3.0-or-later · rank 12581 · last release 2026-09-01 · [PyPI](https://pypi.org/project/antsibull-docutils/) · [source](https://github.com/ansible-community/antsibull-docutils/)

_README extract left out: share-alike licence._

### agent-framework-lab

Experimental modules for Microsoft Agent Framework

`pip install agent-framework-lab` · installs (wheel) · licence: MIT License · rank 12590 · last release 2026-10-22 · [PyPI](https://pypi.org/project/agent-framework-lab/) · [source](https://github.com/microsoft/agent-framework/tree/main/python)

<details><summary>README extract</summary>

This is the experimental package for Microsoft Agent Framework, `agent-framework-lab`, which contains
various lab modules built on top of the core framework.
Lab modules are not part of the core framework and may experience breaking changes or be deprecated in the future. ...

Example:
```python
# Using GAIA module
from agent_framework.lab.gaia import GAIA
```

Sections: Agent Framework Lab, What are Lab Modules?, Lab Modules, Repository Structure, Usage, Running Tests Locally, Depending on new framework APIs, Should I consume Lab Modules?, Microsoft-maintained modules, Guidelines

</details>

### azure-search

Microsoft Azure Cognitive Search Client Library for Python

`pip install azure-search` · installs (wheel) · licence: MIT License · rank 12599 · last release 2021-01-22 · [PyPI](https://pypi.org/project/azure-search/)

<details><summary>README extract</summary>

This package was the Microsoft Azure Cognitive Search client library.

It is deprecated.

The new package can be found at:

</details>

### aws-cdk.aws-amplify-alpha

The CDK Construct Library for AWS::Amplify

`pip install aws-cdk.aws-amplify-alpha` · installs (wheel) · licence: OSI Approved · rank 12650 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-amplify-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
import aws_cdk.aws_codebuild as codebuild

amplify_app = amplify.App(self, "MyApp",
    source_code_provider=amplify.GitHubSourceCodeProvider(
        owner="<user>",
        repository="<repo>",
        oauth_token=SecretValue.secrets_manager("my-github-token")
    ),
    build_spec=codebuild.BuildSpec.from_object_to_yaml({
...
```

...

</details>

### aws-advanced-python-wrapper

Amazon Web Services (AWS) Advanced Python Wrapper

`pip install aws-advanced-python-wrapper` · installs (wheel) · licence: Apache Software License · rank 12692 · last release 2026-08-25 · [PyPI](https://pypi.org/project/aws-advanced-python-wrapper/) · [docs](https://github.com/awslabs/aws-advanced-python-wrapper/docs/) · [source](https://github.com/awslabs/aws-advanced-python-wrapper)

<details><summary>README extract</summary>

Hosting a database cluster in the cloud via Aurora is able to provide users with sets of features and configurations to obtain maximum performance and availability, such as database failover. However, at the moment, most existing drivers do not currently support those functionalities or are not able to entirely take advantage of it. ...

Example:
```python
from aws_advanced_python_wrapper import AwsWrapperConnection
from psycopg import Connection

with AwsWrapperConnection.connect(
        Connection.connect,
        "host=database.cluster-xyz.us-east-1.rds.amazonaws.com dbname=db user=john password=pwd",
        plugins="failover",
        wrapper_dialect="aurora-pg",
        autocommit=True
...
```

...

</details>

### azureml-train-restclients-hyperdrive

Contains classes needed to create HyperDriveRuns with azureml-train-core.

`pip install azureml-train-restclients-hyperdrive` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 12698 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-train-restclients-hyperdrive/)

<details><summary>README extract</summary>

The azureml-train-restclients-hyperdrive contains classes needed to create HyperDriveRuns with azureml-train-core.

Follow these instructions to install the Azure ML SDK on your local machine, create an Azure ML workspace, and set up your notebook environment, which is required for the next step. ...

</details>

### aioca

Asynchronous Channel Access client for asyncio and Python using libca via ctypes

`pip install aioca` · installs (wheel) · licence: Apache Software License · rank 12702 · last release 2026-05-06 · [PyPI](https://pypi.org/project/aioca/) · [source](https://github.com/DiamondLightSource/aioca)

<details><summary>README extract</summary>

aioca is an asynchronous EPICS Channel Access client for asyncio and Python
using libca via ctypes.

What | Where

Source | <
PyPI | `pip install aioca`
Documentation | <
Releases | <

<!-- README only content. Anything below this line won't be included in index.md -->

It exposes a high level interface similar to the commandline tools:: ...

</details>

### aws-cdk.aws-globalaccelerator

The CDK Construct Library for AWS::GlobalAccelerator

`pip install aws-cdk.aws-globalaccelerator` · installs (wheel) · licence: OSI Approved · rank 12708 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-globalaccelerator/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# Create an Accelerator
accelerator = globalaccelerator.Accelerator(self, "Accelerator")

# Create a Listener
listener = accelerator.add_listener("Listener",
    port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
    ]
)

# Import the Load Balancers
...
```

...

</details>

### ansys-api-edb

Autogenerated Python gRPC interface package for ansys-api-edb, built on 21:00:48 on 09 June 2026

`pip install ansys-api-edb` · installs (wheel) · licence: MIT · rank 12724 · last release 2026-06-09 · [PyPI](https://pypi.org/project/ansys-api-edb/) · [docs](https://github.com/ansys/ansys-api-edb/#readme) · [source](https://github.com/ansys/ansys-api-edb/)

<details><summary>README extract</summary>

This repository provides the auto-generated gRPC Python interface files for
the Ansys Edb Service.

Sections: ansys-api-edb gRPC Interface Package, Build

</details>

### azure-mgmt-appplatform

Microsoft Azure App Platform Management Client Library for Python

`pip install azure-mgmt-appplatform` · installs (wheel) · licence: MIT License · rank 12729 · last release 2025-06-05 · [PyPI](https://pypi.org/project/azure-mgmt-appplatform/)

<details><summary>README extract</summary>

This package has been deprecated and will no longer be maintained after 03-31-2025. This package will only receive security fixes until 03-31-2025. For more information, see the Azure Spring Apps retirement announcement.

Features:
- Added operation ConfigServersOperations.begin_delete
 - Added operation ConfigServersOperations.list
 - Added operation GatewaysOperations.begin_update_capacity
 - Added operation group JobExecutionOperations
 - Added operation group ...

Sections: Microsoft Azure SDK for Python, 10.0.1 (2025-06-04), Other Changes, 10.0.0 (2024-10-29), Breaking Changes, 9.1.0 (2024-07-03), Features Added, 9.0.0 (2024-01-26), 8.0.0 (2023-04-20), 8.0.0b1 (2023-02-13)

</details>

### aws-solutions-constructs.resources

Resource CDK Constructs for patterns library

`pip install aws-solutions-constructs.resources` · installs (wheel) · licence: OSI Approved · rank 12741 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aws-solutions-constructs.resources/) · [source](https://github.com/awslabs/aws-solutions-constructs.git)

<details><summary>README extract</summary>

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the Semantic Versioning model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

| Reference Documentation:| ...

</details>

### add-trailing-comma

Automatically add trailing commas to calls and literals

`pip install add-trailing-comma` · installs (wheel) · licence: MIT · rank 12809 · last release 2025-10-10 · [PyPI](https://pypi.org/project/add-trailing-comma/)

<details><summary>README extract</summary>

A tool (and pre-commit hook) to automatically add trailing commas to calls and
literals.

Example:
```python
# Sample of *ideal* syntax
function_call(
    argument,
    5 ** 5,
    kwarg=foo,
)
```

Sections: add-trailing-comma, As a pre-commit hook, multi-line method invocation style -- why?, Implemented features, trailing commas for function calls, trailing commas for tuple / list / dict / set literals, trailing commas for function definitions, trailing commas for `from` imports, trailing comma for class definitions, trailing comma for with statement, trailing comma for match statement, trailling comma for PEP-695 type aliases, unhug trailing paren, unhug leading paren

</details>

### array-api-extra

Extra array functions built on top of the array API standard.

`pip install array-api-extra` · installs (wheel) · licence: MIT · rank 12838 · last release 2026-10-25 · [PyPI](https://pypi.org/project/array-api-extra/)

<details><summary>README extract</summary>

[][docs-link]
[][pypi-link]
[][conda-link]
[][pypi-link]

Extra array functions built on top of the array API standard.

Used by:

- SciPy — Fundamental algorithms for
 scientific computing.
- scikit-learn — Machine
 Learning in Python. ...

Sections: array-api-extra, Versioning

</details>

### array-api-strict

A strict, minimal implementation of the Python array API standard.

`pip install array-api-strict` · installs (wheel) · licence: BSD License · rank 12876 · last release 2026-07-27 · [PyPI](https://pypi.org/project/array-api-strict/) · [source](https://github.com/data-apis/array-api-strict)

<details><summary>README extract</summary>

`array_api_strict` is a strict, minimal implementation of the Python array
API.

The purpose of array-api-strict is to provide an implementation of the array
API for consuming libraries to test against so they can be completely sure
their usage of the array API is portable.

It is *not* intended to be used by end-users. ...

</details>

### automaton

Friendly state machines for Python.

`pip install automaton` · installs (wheel) · licence: Apache-2.0 · rank 12899 · last release 2026-08-26 · [PyPI](https://pypi.org/project/automaton/) · [source](https://opendev.org/openstack/automaton)

<details><summary>README extract</summary>

Friendly state machines for Python. The goal of this library is to provide
well documented state machine classes and associated utilities. The state
machine pattern (or the implemented variation there-of) is a commonly
used pattern and has a multitude of various usages. ...

</details>

### aioblescan

Scanning Bluetooth for advertised info with asyncio.

`pip install aioblescan` · installs (wheel) · licence: MIT License · rank 12938 · last release 2023-01-07 · [PyPI](https://pypi.org/project/aioblescan/)

<details><summary>README extract</summary>

aioblescan is a Python 3/asyncio library to listen for BLE advertized
packets.

|PyPI version fury.ioMIT licenseGITHUB-BADGEDownloads|

Example:
```python
Scapy is great and you can do

    import scapy.all as sa
    test=sa.BluetoothHCISocket(0)
    command=sa.HCI_Cmd_LE_Set_Scan_Enable(enable=1,filter_dups=0)
    chdr=sa.HCI_Command_Hdr(len=len(command))
    hdr=sa.HCI_Hdr(type=1)
    test.send(hdr / chdr / command)

to get things going. But... the great thing with Scapy is that there is so
...
```

Sections: aioblescan, How to use, Interpreting the Tilt Data, FAQ

</details>

### awsgi2

A WSGI gateway for the AWS API Gateway/Lambda proxy integration

`pip install awsgi2` · installs (wheel) · licence: MIT License · rank 13028 · last release 2024-12-17 · [PyPI](https://pypi.org/project/awsgi2/) · [source](https://gitlab.com/advian-oss/python-awsgi2/)

<details><summary>README extract</summary>

AWSGI allows you to use WSGI-compatible middleware and frameworks like Flask and Django with the AWS API Gateway/Lambda proxy integration.

This is an improved fork of original aws-wsgi.

Example:
```python
import awsgi2
from flask import (
    Flask,
    jsonify,
)

app = Flask(name)

@app.route('/')
def index():
    return jsonify(status=200, message='OK')

def lambda_handler(event, context):
    return awsgi2.response(app, event, context, base64_content_types={"image/png"})
```

Sections: awsgi2, Examples, Flask, Django, Docker, SSH agent forwarding, pre-commit considerations, Test suite

</details>

### AstrBot

Easy-to-use multi-platform LLM chatbot and development framework

`pip install AstrBot` · installs (wheel) · licence: AGPL-3.0-or-later · rank 13062 · last release 2026-10-31 · [PyPI](https://pypi.org/project/AstrBot/) · [source](https://github.com/AstrBotDevs/AstrBot)

_README extract left out: share-alike licence._

### awslabs.redshift-mcp-server

An AWS Labs Model Context Protocol (MCP) server for Redshift

`pip install awslabs.redshift-mcp-server` · installs (wheel) · licence: Apache Software License · rank 13105 · last release 2026-10-16 · [PyPI](https://pypi.org/project/awslabs.redshift-mcp-server/) · [docs](https://awslabs.github.io/mcp/servers/redshift-mcp-server/) · [source](https://github.com/awslabs/mcp.git)

<details><summary>README extract</summary>

Model Context Protocol (MCP) server for Amazon Redshift.

This MCP server provides tools to discover, explore, and query Amazon Redshift clusters and serverless workgroups. It enables AI assistants to interact with Redshift resources safely and efficiently through a comprehensive set of discovery and query execution tools. ...

Features:
- Cluster Discovery: Automatically discover both provisioned Redshift clusters and serverless workgroups
- Metadata Exploration: Browse databases, schemas, tables, and columns ...

Example:
```python
list_clusters() -> list[RedshiftCluster]
```

...

</details>

### arcadedb-driver-grpc

Python gRPC client for ArcadeDB's data plane, generated from ArcadeDB's protobuf contract.

`pip install arcadedb-driver-grpc` · installs (wheel) · licence: Apache-2.0 · rank 13139 · last release 2026-11-05 · [PyPI](https://pypi.org/project/arcadedb-driver-grpc/) · [source](https://github.com/ArcadeData/arcadedb-drivers)

<details><summary>README extract</summary>

A Python gRPC client for ArcadeDB's data plane, generated from ArcadeDB's
protobuf contract (`contracts/arcadedb-server-*.proto`), with a hand-written facade on top for
authentication, the two streaming RPCs, and explicit transactions. ...

Example:
```python
from arcadedb_driver_grpc import create_client, messages

with create_client("localhost:50051", insecure=True) as client:
    response = client.raw.ExecuteQuery(
        messages.ExecuteQueryRequest(database="mydb", query="SELECT FROM Person WHERE age > 21", language="sql")
    )
    for result in response.results:
...
```

...

</details>

### aardwolf

Asynchronous RDP protocol implementation

`pip install aardwolf` · installs (wheel) · licence: MIT · rank 13142 · last release 2026-11-07 · [PyPI](https://pypi.org/project/aardwolf/) · [source](https://github.com/skelsec/aardwolf)

<details><summary>README extract</summary>

Features:
- Supports credssp auth via NTLM/Kerberos.
 - Built-in proxy client allows SOCKS/HTTP proxy tunneling without 3rd part software
 - PtH via CredSSP+Restricted admin mode
 - Scriptable Keyboard, Mouse input and Clipboard input/output
 - Can run in ...

Sections: AARDWOLF - Asynchronous RDP/VNC client in Python (headless), triangular_flag_on_post: Runs in the browser, Important, Features, Example scripts, URL format, Kudos

</details>

### athina-client

Light weight SDK to interact with athina datasets

`pip install athina-client` · installs (wheel) · licence: MIT License · rank 13150 · last release 2025-04-28 · [PyPI](https://pypi.org/project/athina-client/)

### autosemver

Tools to handle automatic semantic versioning in python

`pip install autosemver` · installs from source (sdist only) · licence: GPLv3 · rank 13155 · last release 2020-11-13 · [PyPI](https://pypi.org/project/autosemver/)

_README extract left out: share-alike licence._

### atlas-doc-parser

Atlassian Document Format Parser.

`pip install atlas-doc-parser` · installs (wheel) · licence: MIT License · rank 13156 · last release 2026-01-04 · [PyPI](https://pypi.org/project/atlas-doc-parser/) · [docs](https://sanhe-confluence-sdk.readthedocs.io/en/latest/) · [source](https://github.com/MacHu-GWU/atlas_doc_parser-project)

<details><summary>README extract</summary>

Turn your Confluence pages and Jira issues into AI-ready Markdown.

Confluence and Jira store rich text as Atlassian Document Format (ADF) - a complex JSON structure that LLMs can't directly consume. This library solves that:

Now your team's knowledge in Confluence and Jira becomes training data, context, or input for any AI workflow.

Example:
```python
from atlas_doc_parser.api import NodeDoc

# Parse ADF JSON from Confluence/Jira API
doc = NodeDoc.from_dict(adf_json)

# Convert to clean Markdown
markdown = doc.to_markdown()

# Feed to your AI
response = llm.chat(f"Summarize this: {markdown}")
```

</details>

### atomic-physics

Lightweight python library for calculations based on atomic structure

`pip install atomic-physics` · installs (wheel) · licence: not stated · rank 13159 · last release 2025-05-14 · [PyPI](https://pypi.org/project/atomic-physics/)

### airflow-provider-great-expectations

An Apache Airflow provider for Great Expectations

`pip install airflow-provider-great-expectations` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 13175 · last release 2026-01-28 · [PyPI](https://pypi.org/project/airflow-provider-great-expectations/) · [docs](https://great-expectations.github.io/airflow-provider-great-expectations/latest) · [source](https://github.com/great-expectations/airflow-provider-great-expectations)

<details><summary>README extract</summary>

A set of Airflow operators for Great Expectations, a framework for describing data using expressive tests and then validating that the data meets test criteria.

Visit the docs to learn more about the Great Expectations Airflow Provider:

- Getting started
- Examples
- Migration guide ...

</details>

### aws-request-signer

A python library to sign AWS requests using AWS Signature V4.

`pip install aws-request-signer` · installs (wheel) · licence: MIT License · rank 13181 · last release 2023-02-20 · [PyPI](https://pypi.org/project/aws-request-signer/) · [source](https://www.github.com/iksteen/aws-request-signer.git)

<details><summary>README extract</summary>

> A python library to sign AWS requests using AWS Signature V4.

This small python library serves only purpose: Helping you sign HTTP
requests for use with AWS (and compatible) services. The library is
unopinionated and should work with just about anything that makes HTTP
requests (requests, aiohttp). ...

Example:
```python
import hashlib

import requests
from aws_request_signer import AwsRequestSigner

AWS_REGION = ""
AWS_ACCESS_KEY_ID = "minio"
AWS_SECRET_ACCESS_KEY = "minio123"

URL = "

# Demo content for our target file.
content = b"Hello, World!\n"
content_hash = hashlib.sha256(content).hexdigest()

# Create a request signer instance.
...
```

Sections: aws-request-signer, Usage example, Meta

</details>

### amazon-dax-client

Amazon DAX Client for Python

`pip install amazon-dax-client` · installs from source (sdist only) · licence: Apache Software License · rank 13199 · last release 2026-09-15 · [PyPI](https://pypi.org/project/amazon-dax-client/)

<details><summary>README extract</summary>

The Amazon DAX Client for Python is used to access Amazon DAX clusters from
Python. It is nearly source-compatible with Boto3, with only a small change
needed to the client initialization to use DAX instead of DynamoDB. ...

Example:
```python
ddb = boto3.resource('dynamodb')
```

Sections: Amazon DAX Client for Python, Quick Start, Documentation, Getting Help, Changes

</details>

### azure-communication-chat

Microsoft Azure Communication Chat Client Library for Python

`pip install azure-communication-chat` · installs (wheel) · licence: MIT License · rank 13235 · last release 2024-04-11 · [PyPI](https://pypi.org/project/azure-communication-chat/)

<details><summary>README extract</summary>

This package contains a Python SDK for Azure Communication Services for Chat.
Read more about Azure Communication Services here

Source code
| Package (Pypi)
| Package (Conda)
| API reference documentation
| Product documentation

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. ...

Example:
```python
from azure.communication.identity import CommunicationIdentityClient
identity_client = CommunicationIdentityClient.from_connection_string("<connection string of your Communication service>")
user = identity_client.create_user()
tokenresponse = identity_client.get_token(user, scopes=["chat"])
token = tokenresponse.token
```

...

</details>

### airbyte-source-salesforce

Source implementation for Salesforce.

`pip install airbyte-source-salesforce` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 13237 · last release 2026-11-04 · [PyPI](https://pypi.org/project/airbyte-source-salesforce/) · [docs](https://docs.airbyte.com/integrations/sources/salesforce) · [source](https://github.com/airbytehq/airbyte)

<details><summary>README extract</summary>

This package contains the Airbyte Salesforce connector.

Airbyte is open-source data movement for ELT pipelines and AI agents. It moves data from APIs, databases, and files to warehouses, lakes, and AI applications.

Airbyte provides a catalog of 600+ connectors for APIs, databases, data warehouses, data lakes, and AI applications. ...

</details>

### ansys-fluent-core

PyFluent provides Pythonic access to Ansys Fluent.

`pip install ansys-fluent-core` · installs (wheel) · licence: MIT · rank 13245 · last release 2026-10-16 · [PyPI](https://pypi.org/project/ansys-fluent-core/) · [docs](https://fluent.docs.pyansys.com/) · [source](https://github.com/ansys/pyfluent)

<details><summary>README extract</summary>

Features:
PyFluent provides Pythonic access to Ansys Fluent. Its features enable the seamless use of
Fluent within the Python ecosystem and broad access to native Fluent features, including the
ability to:

- Launch Fluent using a local Ansys installation ...

Example:
```python
import ansys.fluent.core as pyfluent

solver_session = pyfluent.launch_fluent()
```

Sections: PyFluent, Overview, Documentation and issues, Using a virtual environment, Dependencies, Getting started, Launching Fluent, Basic usage

</details>

### airbyte-connector-models

Typed Pydantic models for Airbyte connectors

`pip install airbyte-connector-models` · does not install on CPython 3.14 · licence: MIT · rank 13330 · last release 2026-09-01 · [PyPI](https://pypi.org/project/airbyte-connector-models/) · [source](https://github.com/airbytehq/airbyte-connector-models)

<details><summary>README extract</summary>

Typed Pydantic models for Airbyte connectors, providing type-safe configuration and record handling.

Features:
This package provides automatically generated Pydantic models for:
- Config Models: Type-safe configuration for all Airbyte connectors
- Record Models: Typed records for all source connector streams ...

Example:
```python
from airbyte_connector_models.connectors.postgres.source.config import SourcePostgresConfigSpec
import airbyte as ab  # Optional import if using with PyAirbyte

# Type-safe config
config = SourcePostgresConfigSpec(
    host="localhost",
    port=5432,
    database="mydb",
    username="user",
    password="pass"
)

# Use with PyAirbyte (optional)
...
```

Sections: Airbyte Connector Models, Overview, Usage, Config Models, Record Models, Features, Structure

</details>

### agentic-devtools

Agentic devtools integrate Jira, DevOps & more

`pip install agentic-devtools` · installs (wheel) · licence: MIT · rank 13341 · last release 2026-10-29 · [PyPI](https://pypi.org/project/agentic-devtools/)

<details><summary>README extract</summary>

Agentic devtools integrate Jira, DevOps & more. This package provides
simple CLI commands that can be easily auto-approved by VS Code AI assistants.

Audience: End users of the AGDT CLI. This README focuses on installation
and
usage.

Features:
The Azure context system uses separate `AZURE_CONFIG_DIR` directories per account context. Both accounts can stay authenticated simultaneously and can be switched instantly via environment variable.

Available Contexts: ...

...

</details>

### autumn-sdk

Python SDK for the Autumn billing API

`pip install autumn-sdk` · installs (wheel) · licence: Apache-2.0 · rank 13344 · last release 2026-10-15 · [PyPI](https://pypi.org/project/autumn-sdk/)

<details><summary>README extract</summary>

The official Python SDK for the Autumn billing API.

Features:
* create - Creates a new feature.

Use this to programmatically create features for metering usage, managing access, or building credit systems.
* get - Retrieves a single feature by its ID. ...

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "autumn-sdk",
# ]
# ///

from autumn_sdk import Autumn

sdk = Autumn(
  # SDK arguments
)

# Rest of script here...
```

Sections: autumn-sdk, Summary, uv, PIP, Poetry, Shell and script usage with `uv`, PyCharm, SDK Example Usage, Example, Authentication, Available Resources and Operations, Autumn SDK, Balances, Billing

</details>

### abstract-utilities

Utility modules for data comparison, JSON handling, string manipulation, math operations, and general automation tasks.

`pip install abstract-utilities` · installs (wheel) · licence: MIT License · rank 13407 · last release 2026-11-06 · [PyPI](https://pypi.org/project/abstract-utilities/)

<details><summary>README extract</summary>

Abstract Utilities is a comprehensive collection of utility modules assembled to assist a multitude of common tasks. The aim of this collection is to eliminate the need to perpetually rewrite trivial but essential functions that are frequently used across projects. ...

Example:
```python
read_write_utils.write_to_file(file_path: str, contents: any)
```

Sections: Abstract Utilities, Modules, Class Utilities class_utils.py, Key Functions, Dependencies, Command Utilities, Functions, Notes, Command Line Utilities, Collator Utilities, Compare Utilities, Comparison Utilities

</details>

### astronomer-starship

Migrations to Astro

`pip install astronomer-starship` · installs (wheel) · licence: PROPRIETARY · rank 13477 · last release 2026-10-30 · [PyPI](https://pypi.org/project/astronomer-starship/) · [source](https://github.com/astronomer/starship/)

<details><summary>README extract</summary>

Astronomer Starship can send your Airflow workloads to new places!

Starship is a utility to migrate Airflow metadata such as Airflow Variables,
Connections, Environment Variables, Pools, and DAG History between two Airflow instances.

Read more at the official documentation! ...

Sections: Astronomer Starship, What is it?

</details>

### arro3-compute

(no summary)

`pip install arro3-compute` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 13565 · last release 2026-10-12 · [PyPI](https://pypi.org/project/arro3-compute/)

### agent-runtimes

Agent Runtimes

`pip install agent-runtimes` · installs (wheel) · licence: BSD-3-Clause · rank 13567 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agent-runtimes/) · [docs](https://agent-runtimes.datalayer.tech) · [source](https://github.com/datalayer/agent-runtimes)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2025-2026 Datalayer, Inc.
 ~ BSD 3-Clause License

Agent Runtimes runs AI agents and serves them over the protocols the agent world speaks. It is a Python server that hosts agents built from agentspecs (Pydantic AI by default), with their MCP tools, skills, code sandbox and guardrails. ...

Features:
- The meta-harness. Coding agents run as harnesses, driven over the Agent Client Protocol (ACP): Claude Code, Codex, OpenCode and pi today. ...

Sections: 🤖 🚀 Agent Runtimes, Run, Features, Examples, Documentation

</details>

### adafruit-ampy

ampy (Adafruit MicroPython tool) is a command line tool to interact with a CircuitPython or MicroPython board over a serial connection.

`pip install adafruit-ampy` · installs (wheel) · licence: MIT License · rank 13575 · last release 2021-02-13 · [PyPI](https://pypi.org/project/adafruit-ampy/)

<details><summary>README extract</summary>

MicroPython Tool (ampy) - Utility to interact with a CircuitPython or MicroPython board over a serial connection.

Ampy is meant to be a simple command line tool to manipulate files and run code on a CircuitPython or
MicroPython board over its serial connection. ...

Sections: ampy, Usage, Configuration

</details>

### arraylake

Python client for ArrayLake

`pip install arraylake` · installs (wheel) · licence: MIT · rank 13577 · last release 2026-10-28 · [PyPI](https://pypi.org/project/arraylake/) · [docs](https://docs.earthmover.io/)

<details><summary>README extract</summary>

earthmover.io -
 documentation

Arraylake is a cloud-based platform that understands a wide array of multidimensional scientific data. Organize, analyze, build, and collaborate—effortlessly.

Check out the documentation to get started.

</details>

### azure-ai-language-conversations

Microsoft Azure Conversational Language Understanding Client Library for Python

`pip install azure-ai-language-conversations` · installs (wheel) · licence: MIT License · rank 13603 · last release 2023-06-14 · [PyPI](https://pypi.org/project/azure-ai-language-conversations/) · [source](https://github.com/Azure/azure-sdk-python)

<details><summary>README extract</summary>

Conversational Language Understanding - aka CLU for short - is a cloud-based conversational AI service which provides many language understanding capabilities like:
- Conversation App: It's used in extracting intents and entities in conversations ...

Features:
- Added support for service version 2023-04-01.

Example:
```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

endpoint = "
credential = AzureKeyCredential("<api-key>")
client = ConversationAnalysisClient(endpoint, credential)
```

...

</details>

### asyncprawcore

Low-level asynchronous communication layer for Async PRAW 7+.

`pip install asyncprawcore` · installs (wheel) · licence: BSD License · rank 13629 · last release 2026-06-13 · [PyPI](https://pypi.org/project/asyncprawcore/) · [docs](https://asyncprawcore.readthedocs.io/) · [source](https://github.com/praw-dev/asyncprawcore)

<details><summary>README extract</summary>

asyncprawcore is a low-level communication layer used by Async PRAW 7+.

Example:
```python
import os
import pprint
import asyncio
import asyncprawcore

async def main():
    authenticator = asyncprawcore.TrustedAuthenticator(
        client_id=os.environ["PRAWCORE_CLIENT_ID"],
        client_secret=os.environ["PRAWCORE_CLIENT_SECRET"],
        requestor=asyncprawcore.Requestor(user_agent="YOUR_VALID_USER_AGENT"),
    )
...
```

Sections: asyncprawcore, Execution Example, Documentation, Depending on asyncprawcore, setup.py, requirements.txt

</details>

### astronomy-engine

Astronomy calculation for Sun, Moon, and planets.

`pip install astronomy-engine` · installs (wheel) · licence: MIT License · rank 13680 · last release 2023-12-14 · [PyPI](https://pypi.org/project/astronomy-engine/)

<details><summary>README extract</summary>

This is the complete programming reference for the Python version of
Astronomy Engine. Supports Python 3. Does NOT support Python 2.
See the home page for more info.

Example:
```python
import astronomy
```

Sections: Astronomy Engine (Python), Quick Start, Topic Index, Position of Sun, Moon, and planets, Geographic helper functions, Rise, set, and culmination times, Moon phases, Eclipses and Transits, Lunar perigee and apogee, Planet perihelion and aphelion, Visual magnitude and elongation, Oppositions and conjunctions, Equinoxes, solstices, and apparent solar motion, Coordinate transforms

</details>

### adaptive-cards-templating-py

This library largely implements the JSON-to-JSON Adaptive Cards Template language for Python. Most features are supported, except for the Adaptive expressions prebuilt functions.

`pip install adaptive-cards-templating-py` · installs (wheel) · licence: not stated · rank 13722 · last release 2025-05-14 · [PyPI](https://pypi.org/project/adaptive-cards-templating-py/) · [source](https://github.com/dionoid/adaptive-cards-templating-py)

<details><summary>README extract</summary>

This library largely implements the JSON-to-JSON Adaptive Cards Template language for Python. It allows you to dynamically expand Adaptive Card templates using data and host-specific information.

Features:
- Supports most standard features of the Adaptive Cards Template language.
- Inline data expansion with `$data`.
- Conditional rendering with `$when`.
- Expression evaluation using `${}` syntax.
- Custom functions like `if()` and `json()`. ...

Example:
```python
import json
from adaptive_cards_templating_py import Template

# Define a template
template_json = {
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "text": "${message}"
        }
    ]
}

# Create a Template instance
template = Template(template_json)

...

</details>

### ansys-api-fluent

Autogenerated python gRPC interface package for ansys-api-fluent, built on 12:42:17 on 02 October 2026

`pip install ansys-api-fluent` · installs (wheel) · licence: Apache-2.0 · rank 13803 · last release 2026-10-02 · [PyPI](https://pypi.org/project/ansys-api-fluent/)

<details><summary>README extract</summary>

This repository contains the Protocol Buffer (`.proto`) definition files for the Ansys Fluent gRPC API, along with pre-generated Python stubs published as the `ansys-api-fluent` PyPI package.

> Note: This repository targets the v1 API, compatible with Fluent 27R1 and later. ...

Sections: ansys-api-fluent, Documentation, Build documentation locally

</details>

### aiorun

Boilerplate for asyncio applications

`pip install aiorun` · installs (wheel) · licence: Apache Software License · rank 13853 · last release 2025-01-27 · [PyPI](https://pypi.org/project/aiorun/)

<details><summary>README extract</summary>

Here's the big idea (how you use it):

This package provides a `run()` function as the starting point
of your `asyncio`-based application. The `run()` function will
run forever. If you want to shut down when `main()` completes, just
call `loop.stop()` inside it: that will initiate shutdown.

Example:
```python
import asyncio
from aiorun import run

async def main():
    # Put your application code here
    await asyncio.sleep(1.0)

if name == 'main':
    run(main())
```

Sections: 🏃 aiorun, 🤔 Why?, 🖥️ What about TCP server startup?, 🐛 Error Handling, 💨 Do you like uvloop?, 🛡️ Smart shield for shutdown

</details>

### audiobox-aesthetics

Unified automatic quality assessment for speech, music, and sound.

`pip install audiobox-aesthetics` · installs (wheel) · licence: not stated · rank 13854 · last release 2025-05-01 · [PyPI](https://pypi.org/project/audiobox-aesthetics/)

<details><summary>README extract</summary>

Unified automatic quality assessment for speech, music, and sound.

* Paper arXiv / MetaAI.
* Blogpost ai.meta.com

Sections: audiobox-aesthetics, Pre-trained Models, Usage, How to run prediction using CLI, finetune the model, finished finetuning & upload the model

</details>

### ai-prompter

A prompt management library using Jinja2 templates to build complex prompts easily.

`pip install ai-prompter` · installs (wheel) · licence: MIT · rank 13859 · last release 2026-04-09 · [PyPI](https://pypi.org/project/ai-prompter/)

<details><summary>README extract</summary>

Stop hardcoding prompts. Start building maintainable, reusable AI prompt templates.

AI Prompter is a powerful Python library that transforms how you manage AI prompts. Using familiar Jinja2 templating, you can create dynamic, reusable prompts that scale with your applications - whether you're building chatbots, content generators, or complex AI ...

Features:
- 🎯 Template-Driven: Write prompts once, reuse everywhere with dynamic variables
- 📁 Organized: Keep prompts in separate files, organized and version-controlled
- 🔧 Flexible: Works with any LLM provider - OpenAI, Anthropic, local models ...

Example:
```python
from ai_prompter import Prompter

# Create a simple prompt template
prompter = Prompter(template_text="""
...

</details>

### ANARCI

Antibody Numbering and Antigen Receptor ClassIfication

`pip install ANARCI` · installs (wheel) · licence: not stated · rank 13861 · last release 2026-02-13 · [PyPI](https://pypi.org/project/ANARCI/)

<details><summary>README extract</summary>

Example:
```python
# 1A14:N|PDBID|CHAIN|SEQUENCE
//

    Those sequences where a significant alignment has been found report as below:

# 1A14:H|PDBID|CHAIN|SEQUENCE
# ANARCI numbered
# Domain 1 of 1
# Most significant HMM hit
# |species|chain_type|e-value|score|seqstart_index|seqend_index|
# |mouse|H|8.6e-58|184.9|0|119|
# Scheme = imgt
H 1       Q
H 2       V
...
```

Sections: Usage, Further info, Output files, Schemes

</details>

### ansys-api-tools-filetransfer

Autogenerated python gRPC interface package for ansys-api-tools-filetransfer.

`pip install ansys-api-tools-filetransfer` · installs (wheel) · licence: MIT · rank 13869 · last release 2026-03-03 · [PyPI](https://pypi.org/project/ansys-api-tools-filetransfer/) · [docs](https://github.com/ansys/ansys-api-tools-filetransfer/#readme) · [source](https://github.com/ansys/ansys-api-tools-filetransfer/)

<details><summary>README extract</summary>

This Python package contains the auto-generated gRPC Python interface files for
the filetransfer tool.

Sections: ansys-api-tools-filetransfer gRPC Interface Package, Build, Manual Deployment, Automatic Deployment

</details>

### ansys-pythonnet

.NET and Mono integration for Python (Ansys, Inc. fork)

`pip install ansys-pythonnet` · installs (wheel) · licence: MIT · rank 13873 · last release 2026-10-12 · [PyPI](https://pypi.org/project/ansys-pythonnet/)

<details><summary>README extract</summary>

Ansys fork of pythonnet.

We will try to keep this up-to-date with pythonnet and upstream changes that might benefit the pythonnet community

Changes relative to pythonnet:

* Revert of #1240.
* Opt-into explicit interface wrapping, #19. ...

</details>

### ansys-tools-filetransfer

A Python client for uploading and downloading files via gRPC.

`pip install ansys-tools-filetransfer` · installs (wheel) · licence: MIT License · rank 13909 · last release 2026-03-03 · [PyPI](https://pypi.org/project/ansys-tools-filetransfer/) · [source](https://github.com/ansys/ansys-tools-filetransfer)

<details><summary>README extract</summary>

The Ansys FileTransfer Tool provides a simple gRPC API for moving files between
a client and a server. Its target use case are local Docker deployments or
simple remote deployments.

The Ansys FileTransfer Tool is composed of two parts:

- A Python client, which is contained in this repository. ...

Sections: FileTransfer Tool, Documentation and issues

</details>

### astro-airflow-mcp

A FastMCP server for Airflow integration that can run standalone or as an Airflow 2/3 plugin

`pip install astro-airflow-mcp` · installs (wheel) · licence: not stated · rank 13910 · last release 2026-07-08 · [PyPI](https://pypi.org/project/astro-airflow-mcp/)

<details><summary>README extract</summary>

Table of Contents *generated with DocToc*

- Airflow MCP Server
 - Quickstart
 - IDEs
 - CLI Tools
 - Desktop Apps
 - Other MCP Clients
 - Configuration
 - Features
 - Available Tools
 - Consolidated Tools (Agent-Optimized)
 - Core Tools
 - MCP Resources
 - MCP Prompts
 - Airflow CLI Tool
 - Installation
 - Quick Reference
 - Instance Management ...

Features:
- Airflow 2.x and 3.x Support: Automatic version detection with adapter pattern

 - DAG management (list, get details, get source code, stats, warnings, import errors, trigger, pause/unpause)
 - DAG run management (list, get, trigger, trigger and ...

...

</details>

### astral-dev-toolchain-cargo-dist

Shippable application packaging for Rust

`pip install astral-dev-toolchain-cargo-dist` · installs (wheel) · licence: MIT OR Apache-2.0 · rank 13943 · last release 2026-10-30 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-dist/) · [source](https://github.com/axodotdev/cargo-dist)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-dist` from tag `v0.33.1` at commit `665cb7d48902a30386857f8f679e1b1942876f06`.

*dist distributes your binaries*

The TL;DR is that with dist set up, just doing this:

Will make this Github Release: ...

Sections: `dist` (formerly known as `cargo-dist`), Plan, Build, Host, Publish, Announce, Building, Distributing, Read The Book!, Updating Snapshots

</details>

### atlassian-doc-builder

Creating Atlassian Document in a programmatic way.

`pip install atlassian-doc-builder` · installs (wheel) · licence: MIT License · rank 13987 · last release 2026-06-24 · [PyPI](https://pypi.org/project/atlassian-doc-builder/) · [source](https://github.com/khwong-c/atlassian-doc-builder)

<details><summary>README extract</summary>

Creating Atlassian Documents in a programmatic way.

Provide an automatic way to generate documents and reports on the Atlassian Platform (e.g. Confluence, Jira).
Developer may automate report publication (e.g. functional verification report/requirement documents) into CI.

Features:
- Tree-Like Document Representation
- JSON ADF Rendering and Parsing
- Reusable Template with variable filling
- Document Validation

Sections: Atlassian Document Builder, Description, Getting Started, Dependencies, Creating ADF Documents, Features, Implemented Node Type, Roadmap, Examples

</details>

### alchemical

Modern SQLAlchemy simplified

`pip install alchemical` · installs (wheel) · licence: MIT License · rank 14049 · last release 2026-05-13 · [PyPI](https://pypi.org/project/alchemical/)

<details><summary>README extract</summary>

Modern SQLAlchemy simplified.

- Documentation
- PyPI
- Change Log

Sections: alchemical, Resources

</details>

### aot-biomaps

Acousto-Optic Tomography Reconstruction Library

`pip install aot-biomaps` · installs (wheel) · licence: not stated · rank 14051 · last release 2026-11-06 · [PyPI](https://pypi.org/project/aot-biomaps/)

<details><summary>README extract</summary>

AOT_biomaps is an advanced Python library for Acousto-Optic Tomography (AOT). It provides comprehensive tools for image reconstruction, acoustic simulation, optical modeling, and 2D/3D data processing.

This library was developed to meet the needs of the biomedical imaging research community, particularly for Acousto-Optic Tomography applications. ...

Features:
- ✅ Tomographic Reconstruction: MLEM, PDHG, LS, DEPIERRO, MAPEM, LBFGS
- ✅ Multi-Device Support: CPU (NumPy) and GPU (CuPy) with automatic fallback
- ✅ Sparse Matrices: Optimized CSR and SELL-C-sigma implementations ...

...

</details>

### aws-cdk.aws-batch

The CDK Construct Library for AWS::Batch

`pip install aws-cdk.aws-batch` · installs (wheel) · licence: OSI Approved · rank 14058 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-batch/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project. ...

Example:
```python
# shared_compute_envs: batch.ComputeEnvironment

high_prio_queue = batch.JobQueue(self, "JobQueue",
    compute_environments=[batch.JobQueueComputeEnvironment(
        compute_environment=shared_compute_envs,
        order=1
    )],
    priority=2
)

low_prio_queue = batch.JobQueue(self, "JobQueue",
...
```

...

</details>

### aristaproto

Arista Protobuf / Python gRPC bindings generator & library

`pip install aristaproto` · installs (wheel) · licence: MIT License · rank 14133 · last release 2026-06-09 · [PyPI](https://pypi.org/project/aristaproto/) · [source](https://github.com/aristanetworks/python-aristaproto)

<details><summary>README extract</summary>

This was originally forked from < @ b8a091ae7055dd949d193695a06c9536ad51eea8.

Afterwards, commits up to (and including) `124613f55fa8ff62a460e1ad33c5c78723b703a0` on `python-betterproto`, have been cherry-picked.

Changes in this project compared with the base project:

- Renamed to `aristaproto`.
- Cut support for Python < 3.9. ...

Example:
```python
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: example.proto
# plugin: python-aristaproto
from dataclasses import dataclass

import aristaproto

@dataclass
class Greeting(aristaproto.Message):
    """Greeting represents a message you can tell a user."""

    message: str = aristaproto.string_field(1)
```

...

</details>

### azure-mgmt-hybridkubernetes

Microsoft Azure Hybridkubernetes Management Client Library for Python

`pip install azure-mgmt-hybridkubernetes` · installs (wheel) · licence: MIT · rank 14139 · last release 2026-07-20 · [PyPI](https://pypi.org/project/azure-mgmt-hybridkubernetes/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This is the Microsoft Azure Hybrid Kubernetes Management Client Library.
This package has been tested with Python 3.10+.
For a more complete view of Azure libraries, see the azure sdk python release.

_Azure SDK Python packages support for Python 2.7 has ended 01 January 2022. For more information and questions, please refer to

Features:
- Client `ConnectedKubernetesClient` added method `send_request`
 - Model `ConnectedCluster` added property `kind`
 - Enum `ConnectivityStatus` added member `AGENT_NOT_INSTALLED`
 - Model `HybridConnectionConfig` added property `relay_tid`
 - Model ...

Example:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.hybridkubernetes import ConnectedKubernetesClient
import os

sub_id = os.getenv("AZURE_SUBSCRIPTION_ID")
...

</details>

### ansys-api-geometry

Autogenerated Python gRPC interface package for ansys-api-geometry, built on 11:01:36 on 23 February 2026

`pip install ansys-api-geometry` · installs (wheel) · licence: MIT · rank 14146 · last release 2026-02-23 · [PyPI](https://pypi.org/project/ansys-api-geometry/) · [docs](https://github.com/ansys/ansys-api-geometry/#readme) · [source](https://github.com/ansys/ansys-api-geometry/)

<details><summary>README extract</summary>

This repository provides the auto-generated gRPC Python interface files for
the Ansys Geometry Service.

Sections: ansys-api-geometry gRPC Interface Package, Build, Manual Deployment, Automatic Deployment

</details>

### astral-dev-toolchain-cargo-bloat

Find out what takes most of the space in your executable.

`pip install astral-dev-toolchain-cargo-bloat` · installs (wheel) · licence: MIT · rank 14171 · last release 2026-09-14 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-bloat/) · [source](https://github.com/RazrFalcon/cargo-bloat)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-bloat` from tag `v0.12.1` at commit `69ccabda2b1671c4fd675e9a660af29ee985506f`.

Find out what takes most of the space in your executable.

Supports ELF (Linux, BSD), Mach-O (macOS) and PE (Windows) binaries. ...

Sections: cargo-bloat, Usage

</details>

### attoworld

Tools from the Attosecond science group at the Max Planck Institute of Quantum Optics

`pip install attoworld` · installs (wheel) · licence: not stated · rank 14233 · last release 2026-11-04 · [PyPI](https://pypi.org/project/attoworld/)

<details><summary>README extract</summary>

Tools from the Attosecond science group at the Max Planck Institute of Quantum Optics, a.k.a. Attoworld

We are still in the building phase. Things may change, and haven't been validated; use at your own risk!

Documentation available here!

The module has several submodules to keep it organized: ...

Sections: Attoworld, Structure, Code guidelines, Making a PR, After your PR

</details>

### astral-dev-toolchain-cargo-xwin

Cross compile Cargo project to Windows MSVC target with ease

`pip install astral-dev-toolchain-cargo-xwin` · installs (wheel) · licence: MIT · rank 14242 · last release 2026-08-26 · [PyPI](https://pypi.org/project/astral-dev-toolchain-cargo-xwin/) · [source](https://github.com/rust-cross/cargo-xwin)

<details><summary>README extract</summary>

> Build provenance: This package is built and distributed by Astral as part of `astral-dev-toolchain`.
> It packages `cargo-xwin` from tag `v0.23.1` at commit `cb1c19572bd64c801f45c6fc96e234ccb0d5acc5`.

_formerly cargo-xwinbuild

> 🚀 Help me to become a full-time open-source developer by sponsoring me on GitHub ...

Sections: cargo-xwin, Prerequisite, Usage, Pre-caching for offline builds, Run tests with wine, Running Windows executables in WSL (without wine), Customization

</details>

### archil

Pure-Python client for Archil disks and sandboxes

`pip install archil` · installs (wheel) · licence: MIT License · rank 14244 · last release 2026-11-05 · [PyPI](https://pypi.org/project/archil/) · [docs](https://docs.archil.com)

<details><summary>README extract</summary>

Python client for Archil disks and sandboxes. Create persistent disks and microVM sandboxes, run commands against them, and read/write disk contents through the S3-compatible object API — all from scripts, CI, or notebooks. ...

Example:
```python
import archil

# Configure once per process — falls back to ARCHIL_API_KEY / ARCHIL_REGION env vars.
archil.configure(api_key="key-...", region="aws-us-east-1")

# Create a disk. The returned disk is available for use immediately. `token`
# here is the disk token — the one-time credential for mounting.
result = archil.create_disk(name="my-disk")
...
```

...

</details>

### azureml-pipeline-steps

Aeva : represents a unit of computation in azureml-pipeline

`pip install azureml-pipeline-steps` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 14276 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-pipeline-steps/)

<details><summary>README extract</summary>

Represents a unit of computation in azureml-pipeline

</details>

### arcade-mcp

Arcade.dev - Tool Calling platform for Agents

`pip install arcade-mcp` · installs (wheel) · licence: MIT License · rank 14282 · last release 2026-11-06 · [PyPI](https://pypi.org/project/arcade-mcp/)

<details><summary>README extract</summary>

Open-source Python framework for building MCP servers and tools.

Documentation • Examples • Discord

`arcade-mcp` is the Python framework for building Model Context Protocol servers and the tools that run inside them. It powers the 7,500+ prebuilt tools across 81 MCP servers at Arcade.dev, and is open-sourced so you can build your own. ...

Example:
```python
from typing import Annotated
from arcade_mcp_server import MCPApp

app = MCPApp(name="my_server", version="1.0.0")

@app.tool
def greet(name: Annotated[str, "Name to greet"]) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

if name == "main":
    app.run(transport="stdio")
```

Sections: Arcade MCP, What is arcade-mcp, Quick Start, Scaffold a new server, Run, Configure your MCP client, With Arcade Cloud

</details>

### aws-cdk.aws-fsx

The CDK Construct Library for AWS::FSx

`pip install aws-cdk.aws-fsx` · installs (wheel) · licence: OSI Approved · rank 14303 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-fsx/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER--> ...

Example:
```python
# vpc: ec2.Vpc

file_system = fsx.LustreFileSystem(self, "FsxLustreFileSystem",
    lustre_configuration=fsx.LustreConfiguration(deployment_type=fsx.LustreDeploymentType.SCRATCH_2),
    storage_capacity_gi_b=1200,
    vpc=vpc,
    vpc_subnet=vpc.private_subnets[0]
)
```

Sections: Amazon FSx Construct Library, FSx for Lustre, Basic Usage, Connecting, Mounting, Importing, FSx for Windows File Server

</details>

### aptos-sdk

Aptos SDK

`pip install aptos-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 14320 · last release 2026-10-13 · [PyPI](https://pypi.org/project/aptos-sdk/) · [source](https://github.com/aptos-labs/aptos-python-sdk)

<details><summary>README extract</summary>

[][discord-url]
[][pypi-url]
[][pypi-url]
[][codecov-url]

The official Python SDK for interacting with the Aptos blockchain. Get started with the integration guide.

> Note: The sync client is deprecated. Please use the async client for all new projects.

Example:
```python
import asyncio
from aptos_sdk.account import Account
from aptos_sdk.async_client import FaucetClient, RestClient

async def main():
    rest_client = RestClient("
    faucet_client = FaucetClient(" rest_client)

    # Create and fund two accounts
    alice = Account.generate()
    bob = Account.generate()
...
```

Sections: Aptos Python SDK, Quickstart, API Overview, Requirements, Quick devnet smoke test, Test coverage, Autoformatting, Autolinting, Package Publishing, Semantic versioning

</details>

### altex

A simple wrapper on top of Altair to make charts with an express API

`pip install altex` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 14341 · last release 2025-06-30 · [PyPI](https://pypi.org/project/altex/)

<details><summary>README extract</summary>

A simple wrapper on top of Altair to make charts in Streamlit with an express API.

If you're lazy and/or familiar with Altair, this is probably a good fit! Inspired by tvst/plost and plotly-express.

Features:
- Simple, express-like API
- Built on top of Altair
- Automatic Streamlit integration when available
- Sample data utilities
- Support for rolling averages, custom styling, and more

Example:
```python
import streamlit as st
import altex
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Create and display charts in Streamlit
altex.line_chart(data=data, x='x', y='y', title='My Chart')
altex.bar_chart(data=data, x='x', y='y', color='x')
...
```

Sections: Altex, Quick Start, 🎨 Demo App, Chart Types, Features

</details>

### adapta

Logging, data connectors, monitoring, secret handling and general lifehacks to make data people lives easier.

`pip install adapta` · installs (wheel) · licence: Apache-2.0 · rank 14349 · last release 2026-10-21 · [PyPI](https://pypi.org/project/adapta/) · [source](https://github.com/SneaksAndData/adapta)

<details><summary>README extract</summary>

This project aim at providing tools needed for everyday activities of data scientists and engineers:
- Connectors for various cloud APIs
- Secure secret handlers for various remote storages
- Logging framework
- Metrics reporting framework
- Storage drivers for various clouds and storage types ...

Sections: Adapta, Delta Lake, Secret Storages, NoSql (Astra DB), Dataclass Validation framework

</details>

### ansys-api-mechanical

Autogenerated python gRPC interface package for ansys-api-mechanical, built on 03:57:16 on 09 March 2026

`pip install ansys-api-mechanical` · installs (wheel) · licence: MIT · rank 14357 · last release 2026-03-09 · [PyPI](https://pypi.org/project/ansys-api-mechanical/)

<details><summary>README extract</summary>

This Python package contains the auto-generated gRPC Python interface files for
Mechanical.

Sections: ansys-api-mechanical gRPC Interface Package, Build, Manual Deployment, Automatic Deployment

</details>

### aws-croniter

A Python utility for AWS cron expressions. Validate and parse AWS EventBridge cron expressions seamlessly.

`pip install aws-croniter` · installs (wheel) · licence: MIT License · rank 14359 · last release 2026-06-09 · [PyPI](https://pypi.org/project/aws-croniter/)

<details><summary>README extract</summary>

AWS Croniter is a Python package for parsing, validating, and calculating occurrences of AWS EventBridge cron
expressions. AWS cron expressions are a powerful way to schedule events, but they differ from standard Unix cron syntax.
This library makes it easy to work
with AWS-specific cron
schedules programmatically.

Features:
- Validate AWS cron expressions against AWS EventBridge syntax.
- Parse and interpret cron rules with detailed validation error messages.

 - Next and previous occurrence times for a given schedule. ...

Example:
```python
from aws_croniter import AwsCroniter

cron_expression = "0 12 15 * ? 2023"  # AWS cron syntax
aws_cron = AwsCroniter(cron_expression)
```

...

</details>

### africastalking

Official Africa's Talking Python SDK

`pip install africastalking` · installs (wheel) · licence: MIT · rank 14374 · last release 2026-07-31 · [PyPI](https://pypi.org/project/africastalking/)

<details><summary>README extract</summary>

> The SDK provides convenient access to the Africa's Talking APIs to python apps.

Take a look at the API docs here.

Example:
```python
# import package
import africastalking

# Initialize SDK
username = "YOUR_USERNAME"    # use 'sandbox' for development in the test environment
api_key = "YOUR_API_KEY"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS

...
```

Sections: africastalking-python, Documentation, Usage, Initialization, `Application`, `Airtime`, `Sms`, `Voice`, `Token`, `MobileData`, `Insights`, `Whatsapp`, `Ussd`, Issues

</details>

### ansys-api-discovery

Autogenerated python gRPC interface package for ansys-api-discovery, built on 14:11:38 on 15 October 2026

`pip install ansys-api-discovery` · installs (wheel) · licence: MIT · rank 14382 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ansys-api-discovery/) · [docs](https://github.com/ansys/ansys-api-discovery/#readme) · [source](https://github.com/ansys/ansys-api-discovery/)

<details><summary>README extract</summary>

This repository provides the auto-generated gRPC Python interface files
for Discovery/SpaceClaim and the Ansys Geometry Service.

Sections: ansys-api-discovery gRPC Interface Package, Build, Manual Deployment, Automatic Deployment

</details>

### avro-validator

Pure python avro schema validator

`pip install avro-validator` · installs (wheel) · licence: MIT License · rank 14420 · last release 2022-07-26 · [PyPI](https://pypi.org/project/avro-validator/) · [docs](https://avro-validator.readthedocs.io/) · [source](https://github.com/leocalm/avro_validator)

<details><summary>README extract</summary>

A pure python avro schema validator.

The default avro library for Python provide validation of data against the schema, the problem is that the output of
this validation doesn't provide information about the error.
All you get is the `the datum is not an example of the schema` error message. ...

Example:
```python
from avro_validator.schema import Schema

schema_file = 'schema.avsc'

schema = Schema(schema_file)
parsed_schema = schema.parse()

data_to_validate = {
    'name': 'My Name'
}

parsed_schema.validate(data_to_validate)
```

Sections: Avro Validator, Validating data against Avro schema, Console usage, Error validating the data, Command usage, Library usage, Using schema file, Using a dict as schema, Invalid data, Invalid schema

</details>

### azurefunctions-extensions-http-fastapi

FastApi Python worker extension for Azure Functions.

`pip install azurefunctions-extensions-http-fastapi` · installs (wheel) · licence: MIT License · rank 14430 · last release 2025-07-21 · [PyPI](https://pypi.org/project/azurefunctions-extensions-http-fastapi/)

<details><summary>README extract</summary>

This library contains HttpV2 extensions for FastApi Request/Response types to use in your function app code.

Source code
| Package (PyPi)
| Developer Reference
| Samples

Example:
```python
# This function app receives streaming data from a client and processes it in real-time.
# It demonstrates streaming upload capabilities for scenarios such as uploading large files,
# processing continuous data streams, or handling IoT device data.

import azure.functions as func
...
```

Sections: Azure Functions Extensions Http FastApi library for Python, Getting started, Prerequisites, Instructions, Bind to the FastApi type, Next steps, More sample code

</details>

### ansys-api-dbu

Autogenerated Python gRPC interface package for ansys-api-dbu, built on 10:54:49 on 23 February 2026

`pip install ansys-api-dbu` · installs (wheel) · licence: MIT · rank 14446 · last release 2026-02-23 · [PyPI](https://pypi.org/project/ansys-api-dbu/) · [docs](https://github.com/ansys/ansys-api-dbu/#readme) · [source](https://github.com/ansys/ansys-api-dbu/)

<details><summary>README extract</summary>

This repository provides the auto-generated gRPC Python interface files for
the Ansys DBU Service.

Sections: ansys-api-dbu gRPC Interface Package, Build, Manual Deployment, Automatic Deployment

</details>

### aodhclient

Python client library for Aodh

`pip install aodhclient` · installs (wheel) · licence: Apache Software License · rank 14462 · last release 2026-08-25 · [PyPI](https://pypi.org/project/aodhclient/) · [source](https://opendev.org/openstack/python-aodhclient)

<details><summary>README extract</summary>

Python bindings to the OpenStack Aodh API

This is a client for OpenStack Aodh API. There's a Python API (the
aodhclient module), and a command-line script (installed
as aodh). Each implements the entire OpenStack Aodh API.

* Free software: Apache license

</details>

### azureml-defaults

Is a metapackage that is used internally by Azure Machine Learning

`pip install azureml-defaults` · installs (wheel) · licence: https://aka.ms/azureml-sdk-license · rank 14464 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-defaults/)

<details><summary>README extract</summary>

The azureml-defaults is a metapackage that is used internally by Azure Machine Learning.

</details>

### airporttime

convert local time to utc time by airport or vise-versa.

`pip install airporttime` · installs (wheel) · licence: not stated · rank 14589 · last release 2018-12-11 · [PyPI](https://pypi.org/project/airporttime/)

<details><summary>README extract</summary>

Convert local time to utc time by airport or vise-versa.

This works thanks to data from opentraveldata. The data source is here:

Usage

Here is the usage:

Example:
```python
>>> # import the library
>>> import airporttime

>>> # we are also going to use the datetime library
>>> from datetime import datetime

>>> # create an instance of AirportTime at 'ORD'
>>> apt = airporttime.AirportTime(iata_code='ORD')

>>> #  side note  the apt object contains one attribute, basically an instance of a row of data
...
```

</details>

### aws-cdk.aws-imagebuilder

The CDK Construct Library for AWS::ImageBuilder

`pip install aws-cdk.aws-imagebuilder` · installs (wheel) · licence: OSI Approved · rank 14610 · last release 2023-06-19 · [PyPI](https://pypi.org/project/aws-cdk.aws-imagebuilder/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> AWS CDK v1 has reached End-of-Support on 2023-06-01.
> This package is no longer being updated, and users should migrate to AWS CDK v2.
> For more information on how to migrate, see the *Migrating to AWS CDK v2* guide.

<!--END STABILITY BANNER-->

This module is part of the AWS Cloud Development Kit project. ...

Example:
```python
import aws_cdk.aws_imagebuilder as imagebuilder
```

</details>

### aws-cron-expression-validator

ValidatesAWS EventBridge cron expressions, which are similar to, but not compatible with Unix style cron expressions

`pip install aws-cron-expression-validator` · installs (wheel) · licence: MIT License · rank 14613 · last release 2025-11-26 · [PyPI](https://pypi.org/project/aws-cron-expression-validator/) · [source](https://github.com/grumBit/aws_cron_expression_validator)

<details><summary>README extract</summary>

Validates these AWS EventBridge cron expressions, which are similar to, but not compatible with Unix style cron expressions;

| Field | Values | Wildcards |

| Minute | 0-59 | , - \* / |
| Hour | 0-23 | , - \* / |
| Day-of-month | 1-31 | , - \* ? / L W |
| Month | 1-12 or JAN-DEC | , - \* / |
| Day-of-week | 1-7 or SUN-SAT | , - \* ? L # |
| Year ...

Example:
```python
from aws_cron_expression_validator.validator import AWSCronExpressionValidator, AWSCronExpressionMinuteError

my_expression = "0 180 ? * MON-FRI *"
try:
    AWSCronExpressionValidator.validate(my_expression)
except AWSCronExpressionMinuteError as e:
    print(f"Oh no! My expression has an invalid minute field: {e}")
except ValueError as e:
...
```

Sections: AWSCronExpressionValidator, Usage

</details>

### arguably

The best Python CLI library, arguably.

`pip install arguably` · installs (wheel) · licence: not stated · rank 14630 · last release 2024-05-10 · [PyPI](https://pypi.org/project/arguably/) · [source](https://github.com/treykeown/arguably)

<details><summary>README extract</summary>

The best Python CLI library, arguably.

`arguably` turns functions and docstrings into command line interfaces (CLIs). `arguably` has a tiny API and is
extremely easy to integrate. You can also use it directly through `python3 -m arguably your_script.py`, more on that
here. ...

Example:
```python
# !/usr/bin/env python3
import arguably

@arguably.command
def some_function(required, not_required=2, *others: int, option: float = 3.14):
    """
    this function is on the command line!

    Args:
        required: a required argument
        not_required: this one isn't required, since it has a default value
...
```

Sections: No integration required, Documentation, Dependencies, Future roadmap

</details>

### agentspecs

(no summary)

`pip install agentspecs` · installs (wheel) · licence: BSD License · rank 14660 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agentspecs/)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2025-2026 Datalayer, Inc.
 ~ BSD 3-Clause License

YAML-based specifications for AI agents, MCP servers, skills and more...

Features:
This repository is the source of truth for declarative specs consumed by Agent Runtimes code generation.

The YAML files in agentspecs/agentspecs are compiled into Python and TypeScript catalogs used by runtime and UI layers.

Example:
```python
from agentspecs.frames import compose_frames, render_frames

context = compose_frames(["sales-pipeline", "board-reporting"])
print(render_frames(context))
```

...

</details>

### attrdict3

A dict with attribute-style access

`pip install attrdict3` · installs (wheel) · licence: MIT License · rank 14666 · last release 2022-04-01 · [PyPI](https://pypi.org/project/attrdict3/)

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

### aws-cdk.aws-apprunner-alpha

The CDK Construct Library for AWS::AppRunner

`pip install aws-cdk.aws-apprunner-alpha` · installs (wheel) · licence: OSI Approved · rank 14688 · last release 2026-10-26 · [PyPI](https://pypi.org/project/aws-cdk.aws-apprunner-alpha/) · [source](https://github.com/aws/aws-cdk.git)

<details><summary>README extract</summary>

<!--BEGIN STABILITY BANNER-->---

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the Semantic Versioning model and breaking changes will be
> announced in the release notes. ...

Example:
```python
import aws_cdk.aws_apprunner_alpha as apprunner
```

Sections: AWS::AppRunner Construct Library, Introduction, Service, ECR Public, ECR, GitHub, IAM Roles, Auto Scaling Configuration, VPC Connector, VPC Ingress Connection, Dual Stack, Secrets Manager, Use a customer managed key, HealthCheck

</details>

### awesome-slugify

Python flexible slugify function

`pip install awesome-slugify` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 14717 · last release 2015-06-05 · [PyPI](https://pypi.org/project/awesome-slugify/)

_README extract left out: share-alike licence._

### azureml

Microsoft Azure Machine Learning Python client library

`pip install azureml` · installs (wheel) · licence: MIT License · rank 14733 · last release 2016-03-14 · [PyPI](https://pypi.org/project/azureml/)

### astroplan

Observation planning package for astronomers

`pip install astroplan` · installs from source (sdist only) · licence: BSD · rank 14736 · last release 2024-08-13 · [PyPI](https://pypi.org/project/astroplan/)

<details><summary>README extract</summary>

Observation planning package for astronomers

* License: BSD-3

If you use astroplan in your work, please cite Morris et al. 2018:

Sections: astroplan, Attribution

</details>

### airflow-dbt-python

A collection of Airflow operators, hooks, and utilities to execute dbt commands

`pip install airflow-dbt-python` · installs (wheel) · licence: MIT · rank 14741 · last release 2026-09-28 · [PyPI](https://pypi.org/project/airflow-dbt-python/) · [docs](https://airflow-dbt-python.readthedocs.io) · [source](https://github.com/tomasfarias/airflow-dbt-python)

<details><summary>README extract</summary>

A collection of *Airflow* operators, hooks, and utilities to execute *dbt* commands.

Read the documentation for examples, installation instructions, and more details.

Features:
*airflow-dbt-python* aims to make dbt a first-class citizen of Airflow by supporting additional features that integrate both tools. ...

Example:
```python
import datetime as dt

import pendulum
from airflow import DAG

from airflow_dbt_python.operators.dbt import (
    DbtRunOperator,
    DbtSeedOperator,
    DbtTestOperator,
)

args = {
    "owner": "airflow",
}

with DAG(
    dag_id="example_dbt_operator",
    default_args=args,
    schedule="0 0 * * *",
...
```

...

</details>

### all-packages

Install every package on PyPI

`pip install all-packages` · installs (wheel) · licence: MIT License · rank 14742 · last release 2022-01-11 · [PyPI](https://pypi.org/project/all-packages/)

<details><summary>README extract</summary>

The Python Package Index (PyPI) contains over 300,000 Python packages. Need a
Python library but don't want to search through all the options? Search no
further! `all_packages` is a Python script that attempts to install every
package on PyPI - all 349,451 of them as of 11 Jan 2022.

Sections: all_packages, Run

</details>

### adam-io

ADAM 6050-D REST API Python Wrapper

`pip install adam-io` · installs (wheel) · licence: MIT License · rank 14753 · last release 2020-12-22 · [PyPI](https://pypi.org/project/adam-io/)

<details><summary>README extract</summary>

/ADAM-6050_01_B20190725160245.jpg)

ADAM 6000-Series Manual

6050-D has 12 digital inputs and 6 digital outputs. It can be controlled with http requests. The aim of this repo is to wrap the ADAM API into a convenience module for Event Gates' deep learning platform VIS.

Example:
```python
from adam import ADAM6050D as ADAM

ip='192.168.1.1'
username = 'user'
password = 'pass'

adam = ADAM(ip, username, password)
```

Sections: ADAM 6050-D REST API Implementation, Usage Examples, Create adam object, Construct the digital output object, Change the state, Read the state of output, Read the state of input

</details>

### autoscraper

A Smart, Automatic, Fast and Lightweight Web Scraper for Python

`pip install autoscraper` · installs (wheel) · licence: MIT License · rank 14805 · last release 2022-07-17 · [PyPI](https://pypi.org/project/autoscraper/)

<details><summary>README extract</summary>

This project is made for automatic web scraping to make scraping easy.
It gets a url or the html content of a web page and a list of sample data which we want to scrape from that page. This data can be text, url or any html tag value of that page. It learns the scraping rules and returns the similar elements. ...

Example:
```python
from autoscraper import AutoScraper

url = '

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ["What are metaclasses in Python?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
```

Sections: How to use, Getting similar results, Getting exact result, Saving the model, Tutorials, Issues, Happy Coding ♥️

</details>

### aiosocks

SOCKS proxy client for asyncio and aiohttp

`pip install aiosocks` · installs from source (sdist only) · licence: Apache 2 · rank 14929 · last release 2017-11-20 · [PyPI](https://pypi.org/project/aiosocks/)

<details><summary>README extract</summary>

python 3.5+
aiohttp 2.3.2+

Features:
- SOCKS4, SOCKS4a and SOCKS5 version
- ProxyConnector for aiohttp
- SOCKS "CONNECT" command

Example:
```python
import asyncio
import aiosocks

async def connect():
  socks5_addr = aiosocks.Socks5Addr('127.0.0.1', 1080)
  socks4_addr = aiosocks.Socks4Addr('127.0.0.1', 1080)

  socks5_auth = aiosocks.Socks5Auth('login', 'pwd')
  socks4_auth = aiosocks.Socks4Auth('ident')

  dst = ('github.com', 80)

  # socks5 connect
...
```

Sections: SOCKS proxy client for asyncio and aiohttp, Dependencies, Features, TODO, Usage, direct usage, error handling, aiohttp usage

</details>

### azure-ai-voicelive

Microsoft Corporation Azure Ai Voicelive Client Library for Python

`pip install azure-ai-voicelive` · installs (wheel) · licence: MIT · rank 14943 · last release 2026-10-23 · [PyPI](https://pypi.org/project/azure-ai-voicelive/) · [source](https://github.com/Azure/azure-sdk-for-python)

<details><summary>README extract</summary>

This package provides a real-time, speech-to-speech client for Azure AI VoiceLive.
It opens a WebSocket session to stream microphone audio to the service and receive
typed server events (including audio) for responsive, interruptible conversations.

> Status: Preview (`1.3.0b1`). ...

Features:
- Azure Realtime Native Voice Support: Added `AzureRealtimeNativeVoice` and
 `AzureRealtimeNativeVoiceName`, and expanded `voice` fields to accept Azure realtime native voices. ...

Example:
```python
import asyncio
from azure.core.credentials import AzureKeyCredential
from azure.ai.voicelive import connect

async def main():
    async with connect(
        endpoint="your-endpoint",
        credential=AzureKeyCredential("your-api-key"),
        model="gpt-realtime"
    ) as connection:
...

</details>

### async-exit-stack

AsyncExitStack backport for Python 3.5+

`pip install async-exit-stack` · installs (wheel) · licence: Python Software Foundation License · rank 14962 · last release 2018-05-07 · [PyPI](https://pypi.org/project/async-exit-stack/)

<details><summary>README extract</summary>

* Free software: PSF license

This package contains code from the CPython project.

Example:
```python
from async_exit_stack import AsyncExitStack

async def some_async_function():
    async with AsyncExitStack() as stack:
        connections = [await stack.enter_async_context(get_connection())
            for i in range(5)]
        # All opened connections will automatically be released at the end of
...
```

Sections: AsyncExitStack backport for Python 3.5+, Usage example, Reference, 1.0.0 (2018-05-07)

</details>

### appsignal

The AppSignal integration for the Python programming language

`pip install appsignal` · installs (wheel) · licence: not stated · rank 14981 · last release 2026-10-23 · [PyPI](https://pypi.org/project/appsignal/) · [docs](https://docs.appsignal.com/python) · [source](https://github.com/appsignal/appsignal-python)

<details><summary>README extract</summary>

AppSignal solves all your Python monitoring needs in a single tool. You and
your team can focus on writing code and we'll provide the alerts if your app
has any issues.

- AppSignal.com website
- Documentation
- Support ...

Sections: AppSignal for Python, Description, Usage, Publishing, Linting and type checking, Running tests, Running the CLI command, Building wheels, Custom agent build, Clean up build artifacts

</details>

### agentx-harness

SemiAnalysis AgentX inference benchmark harness, built on AIPerf

`pip install agentx-harness` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 14991 · last release 2026-11-03 · [PyPI](https://pypi.org/project/agentx-harness/) · [source](https://github.com/SemiAnalysisAI/agentx-harness)

<details><summary>README extract</summary>

Features:
- Scalable multiprocess architecture with 10 services communicating via ZMQ
- 3 UI modes: `dashboard` (real-time TUI), `simple` (progress bars), `none` (headless) ...

Sections: AgentX Harness, Original README.md Below, AIPerf, Quick Start, Setting up a Local Server, Basic Usage, Example with Custom Configuration, Features, Tutorials and Feature Guides, Getting Started, Load Control and Timing, Workloads and Data, Endpoint Types, Analysis and Monitoring

</details>

