# Software Development / Libraries (part 4 of 5)

[Index](README.md) · 1884 packages in this topic, 1694 more listed under another topic, by downloads.

[part 1](software-development-libraries.md) · [part 2](software-development-libraries-2.md) · [part 3](software-development-libraries-3.md) · part 4 · [part 5](software-development-libraries-5.md)

### mo-kwargs

Object destructuring of function parameters for Python!

`pip install mo-kwargs` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10745 · last release 2026-03-02 · [PyPI](https://pypi.org/project/mo-kwargs/)

<details><summary>README extract</summary>

Object destructuring of function parameters for Python!

See changes

Javascript has object destructuring, and it can be used for function parameters. This has a couple of benefts over Python's keyword arguments:

* Extra caller parameters are ignored (eg `f({a, b, c})`)
* Duplicate parameters are handled elegantly (eg `f({a, a})`) ...

Sections: More KWARGS!, Motivation, Provide default values, Handle too many parameters, Package all parameters, Version Changes, Features, Version 8

</details>

### sphinx-thebe

Integrate interactive code blocks into your documentation with Thebe and Binder.

`pip install sphinx-thebe` · installs (wheel) · licence: not stated · rank 10751 · last release 2024-02-07 · [PyPI](https://pypi.org/project/sphinx-thebe/)

<details><summary>README extract</summary>

Integrate interactive code blocks into your documentation with Thebe and Binder.

See the sphinx-thebe documentation for more details!

</details>

### pyobjc-framework-AppleScriptObjC

Wrappers for the framework AppleScriptObjC on macOS

`pip install pyobjc-framework-AppleScriptObjC` · installs (wheel) · licence: MIT · rank 10752 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AppleScriptObjC/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for framework 'AppleScriptObjC' on macOS 10.6. This framework is
not useful for most users, it provides additional functionality for AppleScript
based application bundles. ...

</details>

### vmware-vcenter

Client library for vmware-vcenter APIs

`pip install vmware-vcenter` · installs (wheel) · licence: MIT License · rank 10785 · last release 2026-09-03 · [PyPI](https://pypi.org/project/vmware-vcenter/)

<details><summary>README extract</summary>

The vCenter module of the VMware Cloud Foundation SDK provides methods related to content libraries and resource
deployment, tagging, and managing internal and external security certificates.

Package (PyPI) | REST API documentation

Example:
```python
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
...
```

Sections: VMware vCenter Server, Getting started, Prerequisites, Connect to a vCenter Server

</details>

### streamlit-keyup

Text input that returns value on every keystroke (Components v2)

`pip install streamlit-keyup` · installs (wheel) · licence: MIT License · rank 10792 · last release 2026-08-19 · [PyPI](https://pypi.org/project/streamlit-keyup/) · [source](https://github.com/blackary/streamlit-keyup)

<details><summary>README extract</summary>

If you're collecting text input from your users in your streamlit app, `st.text_input` works well -- as long as you're happy with
waiting to get the response when they're finished typing.

But, what if you want to get the input out, and do something with it every time they type a new key (AKA "on keyup")?

Example:
```python
import streamlit as st
from st_keyup import st_keyup

value = st_keyup("Enter a value", key="0")

# Notice that value updates after every key press
st.write(value)

# If you want to set a default value, you can pass one
with_default = st_keyup("Enter a value", value="Example", key="1")

...
```

Sections: streamlit-keyup, Usage

</details>

### mo-logs

More Logs! Structured Logging and Exception Handling

`pip install mo-logs` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 10802 · last release 2026-03-02 · [PyPI](https://pypi.org/project/mo-logs/)

<details><summary>README extract</summary>

This library provides two main features

* Structured logging - output is all JSON (with options to serialize to text for line loggers)
* Exception handling weaved in - Good logs must represent what happened,
and that can only be done if the logging library is intimately familiar with
the (exceptional) code paths taken. ...

Example:
```python
from mo_logs import logger
logger.info("Hello, World!")
```

Sections: More Logs - Structured Logging and Exception Handling, Motivation, Basic Usage, Use `logger.info()` for all logging, Importing, Using named parameters, Parametric parameters, Please, never use locals(), Formatting parameters, Destination: Datastore!, Exception Handling, Instead of `raise` use `logger.error()`, Always chain your exceptions, Use `raise from`?

</details>

### cognee

Cognee - is a library for enriching LLM context with a semantic layer for better understanding and reasoning.

`pip install cognee` · installs (wheel) · licence: Apache-2.0 · rank 10804 · last release 2026-11-06 · [PyPI](https://pypi.org/project/cognee/) · [source](https://github.com/topoteretes/cognee)

<details><summary>README extract</summary>

Cognee - The Free Open-Source AI Memory Platform for Agents

 Demo
 Docs
 Learn More
 Join Discord
 Join r/AIMemory
 Community Plugins & Add-ons

 Cognee is a free open-source AI memory platform that gives AI agents persistent long-term memory across sessions. ...

Example:
```python
import asyncio

import cognee

async def main():
    # Extract a knowledge graph and embed the text with local models.
    await cognee.remember(
        "Marie Curie was born in Warsaw and worked at the University of Paris.",
        dataset_name="local_quickstart",
    )

    # Retrieve the matching source text; no LLM generates an answer.
...
```

...

</details>

### pyobjc

Python<->ObjC Interoperability Module

`pip install pyobjc` · installs (wheel) · licence: MIT · rank 10809 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

PyObjC is a bridge between Python and Objective-C. It allows full
featured Cocoa applications to be written in pure Python. It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source. ...

</details>

### async-substrate-interface

Asyncio library for interacting with substrate. Mostly API-compatible with py-substrate-interface

`pip install async-substrate-interface` · installs (wheel) · licence: MIT License · rank 10832 · last release 2026-06-29 · [PyPI](https://pypi.org/project/async-substrate-interface/) · [source](https://github.com/opentensor/async-substrate-interface/)

<details><summary>README extract</summary>

This project provides an asynchronous interface for interacting with Substrate-based
blockchains. Its API is based on the py-substrate-interface
project, but is not fully compatible.

Additionally, this project uses cyscale instead
of py-scale-codec for
faster SCALE decoding. ...

Example:
```python
from async_substrate_interface import SubstrateInterface

def main():
    substrate = SubstrateInterface(
        url="wss://rpc.polkadot.io"
    )
    with substrate:
        result = substrate.query(
            module='System',
            storage_function='Account',
            params=['5CZs3T15Ky4jch1sUpSFwkUbYEnsCfe1WCY51fH3SPV6NFnf']
...
```

Sections: Async Substrate Interface, Usage, Caching, ENV VARS, Signed Commits, Contact

</details>

### paytmchecksum

This is for paytm checksum creation and verification in python

`pip install paytmchecksum` · installs from source (sdist only) · licence: MIT License · rank 10841 · last release 2020-07-03 · [PyPI](https://pypi.org/project/paytmchecksum/)

### python-cmr

Python wrapper to the NASA Common Metadata Repository (CMR) API.

`pip install python-cmr` · installs (wheel) · licence: MIT License · rank 10848 · last release 2024-09-13 · [PyPI](https://pypi.org/project/python-cmr/) · [source](https://github.com/nasa/python_cmr)

<details><summary>README extract</summary>

This repository is a copy
of jddeal/python_cmr which is no
longer maintained. It has been copied here with the permission of the original author for the purpose of continuing to
develop a python library that can be used for CMR access.

Python CMR is an easy to use wrapper to the NASA
EOSDIS Common Metadata Repository API. ...

Example:
```python
# search for granules matching a specific product/short_name
api.short_name("AST_L1T")

# search for granules matching a specific version
api.version("006")

# search for granules at a specific longitude and latitude
api.point(-112.73, 42.5)

# search for granules in an area bound by a box (lower left lon/lat, upper right lon/lat)
...
```

Sections: Python CMR, Examples

</details>

### django-mjml

Use MJML in Django templates

`pip install django-mjml` · installs (wheel) · licence: MIT License · rank 10866 · last release 2026-08-25 · [PyPI](https://pypi.org/project/django-mjml/)

<details><summary>README extract</summary>

The simplest way to use MJML in Django templates.


Sections: django-mjml, Requirements, Usage, Advanced settings, cmd mode, tcpserver mode, httpserver mode

</details>

### hume

A Python SDK for Hume AI

`pip install hume` · installs (wheel) · licence: MIT License · rank 10875 · last release 2026-08-17 · [PyPI](https://pypi.org/project/hume/) · [docs](https://dev.hume.ai) · [source](https://github.com/HumeAI/hume-python-sdk)

<details><summary>README extract</summary>

Integrate Hume APIs directly into your Python application

There were major breaking changes in version `0.7.0` of the SDK. If upgrading from a previous version, please
View the Migration Guide. That release deprecated several interfaces and moved them to the `hume[legacy]` package extra. The `legacy` extra was removed in `0.9.0`. ...

Example:
```python
from hume.client import HumeClient

client = HumeClient(api_key="YOUR_API_KEY")
client.empathic_voice.configs.list_configs()
```

Sections: Hume AI Python SDK, Migration Guide for Version 0.7.0 and Above, Documentation, Compatibility, Other Resources, Examples, Async Client, Namespaces, Exception Handling, Pagination, WebSockets, Advanced, Retries, Timeouts

</details>

### pyobjc-framework-ScreenSaver

Wrappers for the framework ScreenSaver on macOS

`pip install pyobjc-framework-ScreenSaver` · installs from source (sdist only) · licence: MIT · rank 10877 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ScreenSaver/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ScreenSaver" framework on macOS. This frameworks allows
you to write custom screensaver modules.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and ...

</details>

### port-ocean

Port Ocean is a Python framework for building integrations that ingest data into Port, the platform for building your AI software factory.

`pip install port-ocean` · installs (wheel) · licence: Apache Software License · rank 10878 · last release 2026-11-05 · [PyPI](https://pypi.org/project/port-ocean/) · [docs](https://docs.port.io/context-lake/ingestion/ingest-data-into-port/native-integrations/ocean-framework/overview/) · [source](https://github.com/port-labs/ocean)

<details><summary>README extract</summary>

Ocean is Port's open source integration framework. It makes it easy to ingest data from your third-party tools and infrastructure into Port, the platform for building your AI software factory.

- Python 3.12

Sections: Ocean, Prerequisites, Run Integration, Export Architecture, Real-Time updates Architecture, Integration Lifecycle, Folder Structure, Configuration

</details>

### dbt-metabase

dbt + Metabase integration.

`pip install dbt-metabase` · installs (wheel) · licence: MIT License · rank 10880 · last release 2026-05-06 · [PyPI](https://pypi.org/project/dbt-metabase/)

<details><summary>README extract</summary>

Integration between dbt and Metabase.

If dbt is your source of truth for database schemas and you use Metabase as your analytics tool, dbt-metabase can propagate table relationships, model and column descriptions and semantic types (e.g. ...

Example:
```python
from dbtmetabase import DbtMetabase, Filter

# Initializing instance
c = DbtMetabase(
    manifest_path="target/manifest.json",
    metabase_url="
    metabase_api_key="mb_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=",
)

# Exporting models
c.export_models(
    metabase_database="business",
    schema_filter=Filter(include=["public"]),
)

...
```

...

</details>

### pyobjc-framework-ScreenCaptureKit

Wrappers for the framework ScreenCaptureKit on macOS

`pip install pyobjc-framework-ScreenCaptureKit` · installs from source (sdist only) · licence: MIT · rank 10886 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ScreenCaptureKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ScreenCaptureKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### dealcloud-sdk

DealCloud SDK built on HTTPX via intapp-rest-client

`pip install dealcloud-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 10893 · last release 2026-10-15 · [PyPI](https://pypi.org/project/dealcloud-sdk/) · [docs](https://api.docs.dealcloud.com/sdk/python-1.X) · [source](https://pypi.org/project/dealcloud-sdk/)

<details><summary>README extract</summary>

A modern Python SDK for the DealCloud API, built on HTTPX via `intapp-rest-client`.

Features:
The SDK is a complete rewrite and a near drop-in replacement for the official `dealcloud_sdk`, providing a similar and more advanced enterprise featureset that covers a robust API surface of DealCloud. ...

Example:
```python
from dealcloud_sdk import DealCloud

# Initialize with credentials
dc = DealCloud(
    site_url="client.dealcloud.com",
    client_id="12345",
    client_secret="your_secret",
)

# Read data as pandas DataFrame
data = dc.read_data("Company", output="pandas", resolve="name")

# Get schema
schema = dc.get_schema()
users = dc.get_users()

...
```

...

</details>

### OdooRPC

OdooRPC is a Python package providing an easy way to pilot your Odoo servers through RPC.

`pip install OdooRPC` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 10907 · last release 2023-08-16 · [PyPI](https://pypi.org/project/OdooRPC/)

_README extract left out: share-alike licence._

### lenses

A lens library for python

`pip install lenses` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 10917 · last release 2023-10-24 · [PyPI](https://pypi.org/project/lenses/)

_README extract left out: share-alike licence._

### pyobjc-framework-CFNetwork

Wrappers for the framework CFNetwork on macOS

`pip install pyobjc-framework-CFNetwork` · installs from source (sdist only) · licence: MIT · rank 10919 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CFNetwork/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

PyObjC wrappers for the framework "CFNetwork", part of "CoreServices" on
macOS.

The CFNetwork framework provides a library of abstractions for networking
protocols. The most interesting bits for Python programmers are the
API's for working with proxy autoconfiguration and the API's for networking
diagnostics. ...

</details>

### pyobjc-framework-SyncServices

Wrappers for the framework SyncServices on macOS

`pip install pyobjc-framework-SyncServices` · installs from source (sdist only) · licence: MIT · rank 10924 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SyncServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SyncServices" framework on macOS.

Sync Services is a framework containing all the components you need
to sync your applications and devices. If your application uses
Sync Services, user data can be synced with other applications and
devices on the same computer, or other computers over the network via
MobileMe. ...

</details>

### pyobjc-framework-AddressBook

Wrappers for the framework AddressBook on macOS

`pip install pyobjc-framework-AddressBook` · installs from source (sdist only) · licence: MIT · rank 10929 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AddressBook/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AddressBook" framework on macOS. The Address Book is
a centralized database for contact and other information for people. Applications
that make use of the AddressBook framework all use the same database. ...

</details>

### conductor-python

Python SDK for working with https://github.com/conductor-oss/conductor

`pip install conductor-python` · installs (wheel) · licence: Apache Software License · rank 10935 · last release 2026-08-03 · [PyPI](https://pypi.org/project/conductor-python/)

<details><summary>README extract</summary>

The Python SDK for Conductor lets you build durable Conductor agents, workflows, and workers. Conductor coordinates retries, state, and observability while your Python code runs wherever you deploy it.

Get involved: ⭐ Conductor OSS · Choose a Conductor OSS contribution · Contribution guide ...

Features:
- Survive process failures: execution state is durable, so Conductor agents and workflows resume from completed work.
- Build dynamic agent graphs: define workflow graphs in Python or let an LLM plan them at runtime. ...

...

</details>

### intel-cmplr-lic-rt

Intel® oneAPI Runtime COMMON LICENSING

`pip install intel-cmplr-lic-rt` · installs (wheel) · licence: Other/Proprietary License · rank 10940 · last release 2026-10-16 · [PyPI](https://pypi.org/project/intel-cmplr-lic-rt/)

<details><summary>README extract</summary>

This Intel® oneAPI Runtime COMMON LICENSING package contains the Third Party program files and EULA needed to deploy executables to hosts without the Intel® oneAPI development Toolkits. This COMMON LICENSING package should be downloaded and installed along with the COMMON LIBRARIES package and one or more of the Compiler-Specific runtimes.

</details>

### pyobjc-framework-ScriptingBridge

Wrappers for the framework ScriptingBridge on macOS

`pip install pyobjc-framework-ScriptingBridge` · installs from source (sdist only) · licence: MIT · rank 10941 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ScriptingBridge/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ScriptingBrige" framework on macOS 10.5 or later. This
framework provides an easy way to use the scripting functionality of
applications ("AppleScript") from Cocoa applications. ...

</details>

### django-ical

iCal feeds for Django based on Django's syndication feed framework.

`pip install django-ical` · installs (wheel) · licence: MIT License · rank 10947 · last release 2023-06-12 · [PyPI](https://pypi.org/project/django-ical/)

<details><summary>README extract</summary>

django-ical is a simple library/framework for creating
iCal
feeds based in Django's
syndication feed framework.

This documentation is modeled after the documentation for the syndication feed
framework so you can think of it as a simple extension. ...

Sections: django-ical, Documentation, Changes, 1.9.2 (2023-06-12), 1.9.1 (2023-05-01), 1.9.0 (2023-04-04), 1.8.4 (2023-04-02), 1.8.3 (2022-01-25), 1.8.2 (2022-01-13), 1.8.1 (2022-01-08), 1.8.0 (2021-05-21), 1.7.3 (2021-05-03), 1.7.2 (2020-12-16), 1.7.1 (2020-05-09)

</details>

### pyobjc-framework-CoreData

Wrappers for the framework CoreData on macOS

`pip install pyobjc-framework-CoreData` · installs from source (sdist only) · licence: MIT · rank 10950 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreData/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreData" framework on macOS. The Core Data framework
provides generalized and automated solutions to common tasks associated
with object life-cycle and object graph management, including persistence. ...

</details>

### pyobjc-framework-Automator

Wrappers for the framework Automator on macOS

`pip install pyobjc-framework-Automator` · installs from source (sdist only) · licence: MIT · rank 10965 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Automator/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Automator" framework on macOS. The Automator framework
supports the development of actions for the Automator application, as well
as the ability to run a workflow in developer applications. An action is
a bundle that, when loaded and run, performs a specific task. ...

</details>

### unique-namer

Generate unique, human-readable, and memorable names or identifiers

`pip install unique-namer` · installs (wheel) · licence: MIT License · rank 10972 · last release 2025-07-03 · [PyPI](https://pypi.org/project/unique-namer/)

<details><summary>README extract</summary>

A Python package and command-line utility to generate unique and memorable names (e.g., `talented-toucan`, `naughty-watermelon`) and IDs (e.g., `broken-radio-7ab4g`). These names/IDs are ideal for naming temporary directories, user session IDs, gamer tags, project names, process names, or submitted jobs. ...

Features:
* Over 17 million unique names
* Nearly infinite unique identifiers
* 25 categories
* Customizable names and categories

Example:
```python
import namer

name = namer.generate()
print(name)   # Example: 'blushy-cyclist'
```

...

</details>

### recordclass

Mutable variant of namedtuple -- recordclass, which support assignments, compact dataclasses and other memory saving variants.

`pip install recordclass` · installs from source (sdist only) · licence: BSD License · rank 10995 · last release 2026-09-04 · [PyPI](https://pypi.org/project/recordclass/)

<details><summary>README extract</summary>

Recordclass is MIT Licensed python library.
It was started as a "proof of concept" for the problem of fast "mutable"
alternative of `namedtuple` (see question on stackoverflow).
It was evolved further in order to provide more memory saving, fast and flexible types. ...

Sections: Recordclass library, Memory footprint, Performance counters, Quick start, Quick start with dataobject, Quick start with recordclass, Changes, 0.24.1, 0.24, 0.23.1, 0.23, 0.22.1, 0.22.0.3, 0.22.0.2

</details>

### flake8-string-format

string format checker, plugin for flake8

`pip install flake8-string-format` · installs (wheel) · licence: MIT · rank 11003 · last release 2026-06-09 · [PyPI](https://pypi.org/project/flake8-string-format/)

<details><summary>README extract</summary>

An extension for Flake8 to check the
strings and parameters using `str.format`. It checks all strings whether they
use numbered parameters with an implicit index which isn't support in
Python 2.6.

In all instances of `'…'.format(…)` it will also check whether there are
enough parameters given. ...

Sections: String format parameter checker, Plugin for Flake8, Parameters, Error codes, Operation, Format strings, Changes, 0.4.0 - 2026-06-09, 0.3.0 - 2020-02-16, 0.2.3 - 2016-07-27, 0.2.2 - 2016-05-29, 0.2.1 - 2015-09-20, 0.2.0 - 2015-09-12, 0.1.0 - 2015-09-10

</details>

### django-tailwind-cli

Django and Tailwind integration based on the prebuilt Tailwind CSS CLI.

`pip install django-tailwind-cli` · installs (wheel) · licence: MIT · rank 11004 · last release 2026-10-27 · [PyPI](https://pypi.org/project/django-tailwind-cli/) · [docs](https://django-tailwind-cli.rtfd.io/) · [source](https://github.com/django-commons/django-tailwind-cli)

<details><summary>README extract</summary>

Tailwind CSS for Django without Node.js. The library downloads the
standalone Tailwind CSS CLI and wires it into Django
management commands, so there is no npm, no webpack, and no separate build tool to configure. It
follows the approach of the Tailwind integration for Phoenix.

Features:
- Downloads and manages the Tailwind CLI binary for your platform
- Rebuilds CSS on change, running under Django's own auto-reloader
- Produces minified production builds containing only the classes you use ...

Sections: django-tailwind-cli, What it does, Quickstart, Requirements, Configuration and commands, Documentation and related projects

</details>

### faker-vehicle

Vehicle related Provider for the Faker Python package.

`pip install faker-vehicle` · installs (wheel) · licence: Apache Software License · rank 11007 · last release 2020-11-13 · [PyPI](https://pypi.org/project/faker-vehicle/)

<details><summary>README extract</summary>

faker_vehicle is a provider for the Faker Python package.

It provides vehicle and machinery related fake data for testing purposes:

 * Vehicle Make
 * Vehicle Model
 * Vehicle Make / Model
 * Vehicle Make / Model / Year
 * Vehicle Make / Model / Category
 * Vehicle Year
 * Vehicle Object (you can format) ...

Example:
```python
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

fake.vehicle_year_make_model()
# 2014 Volkswagen Golf
fake.vehicle_year_make_model_cat()
# 1996 Dodge Ram Wagon 1500 (Van/Minivan)
fake.vehicle_make_model()
# Volvo V40
fake.vehicle_make()
# BMW
fake.vehicle_model()
# SL
...
```

Sections: faker_vehicle, Usage

</details>

### pyobjc-framework-SecurityInterface

Wrappers for the framework SecurityInterface on macOS

`pip install pyobjc-framework-SecurityInterface` · installs from source (sdist only) · licence: MIT · rank 11009 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SecurityInterface/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SecurityInterface" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### split

Functions to split or partition sequences.

`pip install split` · installs from source (sdist only) · licence: MIT License · rank 11016 · last release 2016-01-20 · [PyPI](https://pypi.org/project/split/)

<details><summary>README extract</summary>

Functions to split and partition sequences.

Example:
```python
>>> from split import chop
>>> list(chop(3, range(10)))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

Sections: python-split, Usage, Chunks of equal size, Subsequences by a predicate, Breaking on separators

</details>

### dotenv-linter

Linting dotenv files like a charm!

`pip install dotenv-linter` · installs (wheel) · licence: MIT License · rank 11024 · last release 2026-07-31 · [PyPI](https://pypi.org/project/dotenv-linter/) · [source](https://github.com/wemake-services/dotenv-linter)

<details><summary>README extract</summary>

Simple linter for `.env` files.

While `.env` files are very simple it is required to keep them consistent.
This tool offers a wide range of consistency rules and best practices.

And it integrates perfectly to any existing workflow.

Read the announcing post.

Sections: dotenv-linter, Examples, Pre-commit hooks, Gratis

</details>

### pyobjc-framework-DiscRecording

Wrappers for the framework DiscRecording on macOS

`pip install pyobjc-framework-DiscRecording` · installs from source (sdist only) · licence: MIT · rank 11027 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DiscRecording/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DiscRecording" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-CoreAudioKit

Wrappers for the framework CoreAudioKit on macOS

`pip install pyobjc-framework-CoreAudioKit` · installs from source (sdist only) · licence: MIT · rank 11033 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreAudioKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreAudioKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### terminaltables3

Generate simple tables in terminals from a nested list of strings. Fork of terminaltables.

`pip install terminaltables3` · installs (wheel) · licence: MIT License · rank 11051 · last release 2024-07-21 · [PyPI](https://pypi.org/project/terminaltables3/) · [docs](https://github.com/matthewdeanmartin/terminaltables3) · [source](https://github.com/matthewdeanmartin/terminaltables3)

<details><summary>README extract</summary>

Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

Tested on Python 3.8+

**This is a fork of the terminaltables project. Which is archived and unmaintained. This library is in a new namespace
but should otherwise be a drop in replacement. ...

Example:
```python
from terminaltables3 import AsciiTable

table_data = [
    ["Heading1", "Heading2"],
    ["row1 column1", "row1 column2"],
    ["row2 column1", "row2 column2"],
    ["row3 column1", "row3 column2"],
]
table = AsciiTable(table_data)
print
table.table
```

Sections: What is it, To Upgrade, Quickstart, Example Implementations

</details>

### cookies

Friendlier RFC 6265-compliant cookie parser/renderer

`pip install cookies` · installs (wheel) · licence: MIT License · rank 11054 · last release 2014-09-27 · [PyPI](https://pypi.org/project/cookies/)

<details><summary>README extract</summary>

What is this and what is it for?

cookies.py is a Python module for working with HTTP cookies: parsing and
rendering 'Cookie:' request headers and 'Set-Cookie:' response headers,
and exposing a convenient API for creating and modifying cookies. It can be
used as a replacement of Python's Cookie.py (aka http.cookies).

Features ...

</details>

### pylspci

Simple parser for lspci -mmnn.

`pip install pylspci` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11062 · last release 2022-08-04 · [PyPI](https://pypi.org/project/pylspci/) · [docs](https://lucidiot.tildepages.org/pylspci/)

_README extract left out: share-alike licence._

### pyobjc-framework-IOBluetooth

Wrappers for the framework IOBluetooth on macOS

`pip install pyobjc-framework-IOBluetooth` · installs from source (sdist only) · licence: MIT · rank 11073 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-IOBluetooth/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "IOBluetooth" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### athenaintel

Athena Intelligence Python Library

`pip install athenaintel` · installs (wheel) · licence: not stated · rank 11079 · last release 2026-11-05 · [PyPI](https://pypi.org/project/athenaintel/)

<details><summary>README extract</summary>

The Athena Intelligence Python Library provides convenient access to the Athena Intelligence API from
applications written in Python.

The library includes type definitions for all
request and response fields, and offers both synchronous and asynchronous clients powered by httpx.

Example:
```python
from athena import GeneralAgentConfig, GeneralAgentRequest, InputMessage
from athena.client import Athena

client = Athena(
  api_key="YOUR_API_KEY" # Defaults to ATHENA_API_KEY
)

response = client.agents.general.invoke(
    request=GeneralAgentRequest(
        config=GeneralAgentConfig(enabled_tools=[]),
        messages=[
...
```

...

</details>

### fritzconnection

Communicate with the AVM FRITZ!Box

`pip install fritzconnection` · installs (wheel) · licence: MIT License · rank 11086 · last release 2026-01-26 · [PyPI](https://pypi.org/project/fritzconnection/)

<details><summary>README extract</summary>

Python-Interface to communicate with the AVM Fritz!Box. Supports the TR-064 protocol, the (AHA-)HTTP-Interface and also allows call-monitoring.

Example:
```python
from fritzconnection import FritzConnection

fc = FritzConnection(address="192.168.178.1", user="user", password="pw")
print(fc)  # print router model information

# tr-064 interface: reconnect for a new ip
fc.call_action("WANIPConn1", "ForceTermination")

# http interface: gets history data from a device with given 'ain'
...
```

Sections: fritzconnection, Quickstart, call_action, call_http, Username and password, Caching, Library, Documentation

</details>

### WooCommerce

A Python wrapper for the WooCommerce REST API

`pip install WooCommerce` · installs (wheel) · licence: MIT License · rank 11089 · last release 2021-03-13 · [PyPI](https://pypi.org/project/WooCommerce/) · [docs](https://woocommerce.github.io/woocommerce-rest-api-docs/?python#libraries-and-tools) · [source](https://github.com/woocommerce/wc-api-python)

<details><summary>README extract</summary>

A Python wrapper for the WooCommerce REST API. Easily interact with the WooCommerce REST API using this library.

Example:
```python
from woocommerce import API

wcapi = API(
    url="
    consumer_key="ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    consumer_secret="cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    version="wc/v3"
)

# Force delete example.
print(wcapi.delete("products/100", params={"force": True}).json())

# Query example.
...
```

Sections: WooCommerce API - Python Client, Getting started, Setup, Options, Methods, GET, POST, PUT, DELETE, OPTIONS, Response, Request with `params` example

</details>

### pyobjc-framework-LaunchServices

Wrappers for the framework LaunchServices on macOS

`pip install pyobjc-framework-LaunchServices` · installs (wheel) · licence: MIT · rank 11090 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-LaunchServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Deprecated wrappers for the "LaunchServices" framework on macOS.

Use the "CoreServices" bindings instead.

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-CoreMIDI

Wrappers for the framework CoreMIDI on macOS

`pip install pyobjc-framework-CoreMIDI` · installs from source (sdist only) · licence: MIT · rank 11100 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreMIDI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreMIDI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### django-nonrelated-inlines

Django admin inlines for unrelated models

`pip install django-nonrelated-inlines` · installs (wheel) · licence: MIT License · rank 11117 · last release 2022-06-06 · [PyPI](https://pypi.org/project/django-nonrelated-inlines/)

<details><summary>README extract</summary>

Django admin inlines for unrelated models

Example:
```python
from nonrelated_inlines.admin import NonrelatedStackedInline

class CustomerInvoiceStackedInline(NonrelatedStackedInline):
    model = Invoice
    fields = [
        'id',
        'amount'
    ]

    def get_form_queryset(self, obj):
        return self.model.objects.filter(email=obj.email)

    def save_new_instance(self, parent, instance):
...
```

Sections: django-nonrelated-inlines, Getting started

</details>

### pyobjc-framework-ExceptionHandling

Wrappers for the framework ExceptionHandling on macOS

`pip install pyobjc-framework-ExceptionHandling` · installs (wheel) · licence: MIT · rank 11140 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ExceptionHandling/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ExceptionHandling" framework on macOS. The ExceptionHandling
framework provides facilities for monitoring and debugging exceptional
conditions in Cocoa programs.

PyObjC also provides low-level debugging utilities beyond the core
ExceptionHandling framework in the module `PyObjCTools.Debugging`. ...

</details>

### pyobjc-framework-OSAKit

Wrappers for the framework OSAKit on macOS

`pip install pyobjc-framework-OSAKit` · installs (wheel) · licence: MIT · rank 11150 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-OSAKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "OSAKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-LatentSemanticMapping

Wrappers for the framework LatentSemanticMapping on macOS

`pip install pyobjc-framework-LatentSemanticMapping` · installs (wheel) · licence: MIT · rank 11153 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-LatentSemanticMapping/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the framework "LatentSemanticMapping" on macOS 10.5 or later.

The Latent Semantic Mapping framework supports the classification of text and
other token-based content into developer-defined categories. ...

</details>

### pyobjc-framework-InstallerPlugins

Wrappers for the framework InstallerPlugins on macOS

`pip install pyobjc-framework-InstallerPlugins` · installs (wheel) · licence: MIT · rank 11158 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-InstallerPlugins/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "InstallerPlugins" framework on macOS. This framework
allows you to develop plugin's for the "Installer.app" application, and those
make it possible to add new functionality to ".pkg" and ".mpkg" installers
on macOS. ...

</details>

### pyobjc-framework-SearchKit

Wrappers for the framework SearchKit on macOS

`pip install pyobjc-framework-SearchKit` · installs (wheel) · licence: MIT · rank 11160 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SearchKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Deprecated wrappers for the "SearchKit" framework on macOS.

Use the CoreServices package instead.

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-PreferencePanes

Wrappers for the framework PreferencePanes on macOS

`pip install pyobjc-framework-PreferencePanes` · installs (wheel) · licence: MIT · rank 11162 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PreferencePanes/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PreferencePanes" framework on macOS. This framework allows
you to write Preference Panes for the "System Preferences" application.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the ...

</details>

### libconf

A pure-Python libconfig reader/writer with permissive license

`pip install libconf` · installs (wheel) · licence: MIT License · rank 11168 · last release 2019-11-21 · [PyPI](https://pypi.org/project/libconf/)

<details><summary>README extract</summary>

libconf is a pure-Python reader/writer for configuration files in libconfig
format, which is often used in C/C++ projects. It's interface is similar to
the json module: the four main methods are `load()`, `loads()`,
`dump()`, and `dumps()`.

Example usage:
The data can be accessed either via indexing (`['title']`) or via attribute
access `.title`.

Example:
```python
import io, libconf
>>> with io.open('example.cfg') as f:
...     config = libconf.load(f)
>>> config
{'capabilities': {'can-do-arrays': [3, 'yes', True],
                  'can-do-lists': (True,
                                   14880,
                                   ('sublist',),
                                   {'subgroup': 'ok'})},
...
```

...

</details>

### bencode.py

Simple bencode parser (for Python 2, Python 3 and PyPy)

`pip install bencode.py` · installs (wheel) · licence: Other/Proprietary License · rank 11171 · last release 2026-07-07 · [PyPI](https://pypi.org/project/bencode.py/) · [source](https://github.com/fuzeman/bencode.py)

<details><summary>README extract</summary>

Simple bencode parser (for Python 2, Python 3 and PyPy), forked from the bencode_ package by Thomas Rampelberg.


Example:
```python
>>> import bencodepy

>>> bencodepy.encode({'title': 'Example'})
b'd5:title7:Examplee'

>>> bencodepy.encode(12)
b'i12e'
```

Sections: bencode.py, Usage, bencode, API

</details>

### imgviz

Image Visualization Tools

`pip install imgviz` · installs (wheel) · licence: MIT License · rank 11176 · last release 2026-06-10 · [PyPI](https://pypi.org/project/imgviz/)

<details><summary>README extract</summary>

Installation |
 Getting Started |
 Examples |
 C++ Version

Example:
```python
# getting_started.py

import numpy as np

import imgviz

# sample data of rgb, depth, class label and instance masks
data = imgviz.data.arc2017()

rgb = data["rgb"]
gray = imgviz.rgb2gray(rgb)

# colorize depth image with viridis colormap
depth = data["depth"]
depthviz = imgviz.colorize(depth, vmin=0.3, vmax=1)

# colorize label image
...
```

Sections: imgviz, Image Visualization Tools, Dependencies, Getting Started, Examples

</details>

### scikeras

Scikit-Learn API wrapper for Keras.

`pip install scikeras` · installs (wheel) · licence: MIT License · rank 11179 · last release 2024-04-11 · [PyPI](https://pypi.org/project/scikeras/) · [docs](https://www.adriangb.com/scikeras/) · [source](https://github.com/adriangb/scikeras)

<details><summary>README extract</summary>

Scikit-Learn compatible wrappers for Keras Models.

Features:
SciKeras is derived from and API compatible with the now deprecated / removed `tf.keras.wrappers.scikit_learn`.

An overview of the differences as compared to the TF wrappers can be found in our
migration guide.

Sections: Scikit-Learn Wrapper for Keras, Why SciKeras, Migrating from `keras.wrappers.scikit_learn`, Documentation

</details>

### pyEDFlib

library to read/write EDF+/BDF+ files

`pip install pyEDFlib` · installs from source (sdist only) · licence: BSD License · rank 11185 · last release 2025-06-26 · [PyPI](https://pypi.org/project/pyEDFlib/)

<details><summary>README extract</summary>

pyEDFlib is a python library to read/write EDF+/BDF+ files based on EDFlib.

EDF means European Data Format and was firstly published Kemp1992.
In 2003, an improved version of the file protocol named EDF+ has been published and can be found at Kemp2003.

The EDF/EDF+ format saves all data with 16 Bit. ...

Example:
```python
from pyedflib import highlevel

# write an edf file
signals = np.random.rand(5, 256*300)*200 # 5 minutes of random signal
channel_names = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5']
signal_headers = highlevel.make_signal_headers(channel_names, sample_frequency=256)
header = highlevel.make_header(patientname='patient_x', gender='Female')
...
```

Sections: pyEDFlib, What is pyEDFlib, Documentation, Highlevel interface

</details>

### datawrapper

A lightweight Python wrapper for the Datawrapper API

`pip install datawrapper` · installs (wheel) · licence: MIT License · rank 11186 · last release 2026-07-26 · [PyPI](https://pypi.org/project/datawrapper/) · [docs](https://github.com/chekos/datawrapper) · [source](https://github.com/chekos/datawrapper)

<details><summary>README extract</summary>

A lightweight Python wrapper for the Datawrapper API

Features:
* Create, get, update, export and delete charts, tables and maps
* Add data from a `pandas.DataFrame` or a GeoJSON file with one simple call
* Get, update and delete folders, users and teams. ...

Example:
```python
import pandas as pd
import datawrapper as dw

# Configure a bar chart
chart = dw.BarChart(
    title="Top Programming Languages 2024",
    data=pd.DataFrame(
        {"Language": ["Python", "JavaScript", "Java"], "Users": [45.3, 38.2, 30.5]}
    ),
    axis_label_format=dw.NumberFormat.ONE_DECIMAL,
)

...
```

Sections: datawrapper, Features, Quick Start

</details>

### fastapi-injector

python-injector integration for FastAPI

`pip install fastapi-injector` · installs (wheel) · licence: BSD · rank 11187 · last release 2025-10-10 · [PyPI](https://pypi.org/project/fastapi-injector/)

<details><summary>README extract</summary>

Integrates injector with FastAPI.

Github:
PyPI:

Example:
```python
# app.py
from fastapi import FastAPI
from injector import Injector
from fastapi_injector import attach_injector

def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()
    app.include_router(...)
    ...
    attach_injector(app, injector)
    return app
```

Sections: FastAPI Injector, Usage, Request scope, SyncInjected, Dependency cleanup

</details>

### django-test-without-migrations

Disable migrations when running your Django tests.

`pip install django-test-without-migrations` · installs from source (sdist only) · licence: MIT License · rank 11188 · last release 2017-04-12 · [PyPI](https://pypi.org/project/django-test-without-migrations/)

<details><summary>README extract</summary>

*Test Without Migrations* is a `manage.py test` command extension.

The new Django 1.7 and 1.8 migration backend demands that you create a migration every time you change a model.

This can be inconvenient when you're just trying to explore your models code. ...

Sections: Usage, Inspiration

</details>

### pyobjc-framework-DiskArbitration

Wrappers for the framework DiskArbitration on macOS

`pip install pyobjc-framework-DiskArbitration` · installs (wheel) · licence: MIT · rank 11196 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DiskArbitration/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DiskArbitration" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### nbzip

Compresses and downloads all files in any of the user's directories.

`pip install nbzip` · installs (wheel) · licence: BSD License · rank 11207 · last release 2018-08-10 · [PyPI](https://pypi.org/project/nbzip/)

### dpcpp-cpp-rt

Intel® oneAPI DPC++/C++ Compiler Runtime

`pip install dpcpp-cpp-rt` · installs (wheel) · licence: Other/Proprietary License · rank 11214 · last release 2026-10-16 · [PyPI](https://pypi.org/project/dpcpp-cpp-rt/)

<details><summary>README extract</summary>

This COMPILER-SPECIFIC Intel® oneAPI DPC++/C++ Compiler Runtime package contains the compiler-specific shared libraries needed to deploy executables to hosts without the Intel® oneAPI development Toolkits. In addition to this package you will need both the COMMON LIBRARIES and COMMON LICENSING packages.

</details>

### pyobjc-framework-SecurityFoundation

Wrappers for the framework SecurityFoundation on macOS

`pip install pyobjc-framework-SecurityFoundation` · installs (wheel) · licence: MIT · rank 11216 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SecurityFoundation/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SecurityFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-DVDPlayback

Wrappers for the framework DVDPlayback on macOS

`pip install pyobjc-framework-DVDPlayback` · installs (wheel) · licence: MIT · rank 11219 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DVDPlayback/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DVDPlayback" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### flake8-unused-arguments

flake8 extension to warn on unused function arguments

`pip install flake8-unused-arguments` · installs (wheel) · licence: MIT License · rank 11220 · last release 2025-10-27 · [PyPI](https://pypi.org/project/flake8-unused-arguments/)

<details><summary>README extract</summary>

A flake8 plugin that checks for unused function arguments.

This package adds the following warnings:

 - `U100` - An unused argument.
 - `U101` - An unused argument starting with an underscore

Configuration options also exist:
 - `unused-arguments-ignore-abstract-functions` - don't show warnings for abstract functions. ...

</details>

### pyobjc-framework-DiscRecordingUI

Wrappers for the framework DiscRecordingUI on macOS

`pip install pyobjc-framework-DiscRecordingUI` · installs (wheel) · licence: MIT · rank 11223 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DiscRecordingUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DiscRecordingUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### setuptools-dso

setuptools extension to build non-python shared libraries

`pip install setuptools-dso` · installs (wheel) · licence: BSD · rank 11226 · last release 2026-08-28 · [PyPI](https://pypi.org/project/setuptools-dso/) · [docs](https://epics-base.github.io/setuptools_dso)

<details><summary>README extract</summary>

Building non-python shared libraries (eg. `libY.so`, `libY.dylib`, or `Y.dll`) for inclusion in a Python Wheel.

This extension is an alternative to bundling externally built
libraries in Python Wheel packages by providing the means to
replace an external build system (eg. ...

</details>

### pyobjc-framework-LocalAuthentication

Wrappers for the framework LocalAuthentication on macOS

`pip install pyobjc-framework-LocalAuthentication` · installs from source (sdist only) · licence: MIT · rank 11227 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-LocalAuthentication/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "LocalAuthentication" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### dlthub

dlthub is a commercial extension to dlt

`pip install dlthub` · installs (wheel) · licence: not stated · rank 11231 · last release 2026-10-30 · [PyPI](https://pypi.org/project/dlthub/)

<details><summary>README extract</summary>

dlthub is the a commercial extension to the open source data load tool (dlt). Features include:
* define data transformations in Python and SQL
* generate dbt packages from dlt pipelines
* dlthub projects: empower any team members to define sources, destinations and pipelines in a declarative yaml interface
* Iceberg support

Sections: dlthub, Documentation

</details>

### django-redis-sessions

Redis Session Backend For Django

`pip install django-redis-sessions` · installs (wheel) · licence: BSD · rank 11243 · last release 2021-01-13 · [PyPI](https://pypi.org/project/django-redis-sessions/)

<details><summary>README extract</summary>

Redis database backend for your sessions

- Installation
- Available Settings
- Changelog

</details>

### moz-sql-parser

Extract Parse Tree from SQL

`pip install moz-sql-parser` · installs from source (sdist only) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11253 · last release 2021-05-06 · [PyPI](https://pypi.org/project/moz-sql-parser/)

<details><summary>README extract</summary>

Let's make a SQL parser so we can provide a familiar interface to non-sql datastores!

|Branch |Status |

|master | |
|dev | |

SQL is a familiar language used to access databases. Although, each database vendor has its quirky implementation, there is enough standardization that the average developer does not need to know of those quirks. ...

Example:
```python
def listwrap(value):
    if value is None:
        return []
    elif isinstance(value, list)
        return value
    else:
        return [value]
```

Sections: Moz SQL Parser, Problem Statement, Objectives, Non-Objectives, Parsing SQL, Recursion Limit, Generating SQL, Run Tests, More about implementation, Array Programming

</details>

### rowdump

A modern structured Python library for formatted table output

`pip install rowdump` · installs (wheel) · licence: MIT · rank 11256 · last release 2025-07-11 · [PyPI](https://pypi.org/project/rowdump/) · [source](https://github.com/markjen/rowdump)

<details><summary>README extract</summary>

A modern, structured, no-dependency Python library for formatted table output
with support for custom formatting, ASCII box drawing, and flexible column
definitions.

Features:
- Structured table output with customizable column definitions
- ASCII box drawing for beautiful table borders
- Header separators with optional line between header and data
- Custom formatters for data transformation ...

Example:
```python
from datetime import datetime
from rowdump import Column, Dump

# Create a dump instance
dump = Dump()

# Define columns
columns = [
    Column("id", "ID", int, 5),
    Column("name", "Name", str, 15),
    Column("age", "Age", int, 3),
    Column("city", "City", str, 12),
]

# Set columns and print header
dump.cols(columns)

# Add rows
...
```

...

</details>

### pyobjc-framework-UserNotifications

Wrappers for the framework UserNotifications on macOS

`pip install pyobjc-framework-UserNotifications` · installs from source (sdist only) · licence: MIT · rank 11264 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-UserNotifications/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "UserNotifications" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### py-radix

Radix tree implementation

`pip install py-radix` · installs (wheel) · licence: BSD License · rank 11268 · last release 2025-12-04 · [PyPI](https://pypi.org/project/py-radix/)

<details><summary>README extract</summary>

py-radix implements the radix tree data structure for the storage and
retrieval of IPv4 and IPv6 network prefixes.

The radix tree is commonly used for routing table lookups. It efficiently
stores network prefixes of varying lengths and allows fast lookups of
containing networks.

Example:
```python
import radix

# Create a new tree
rtree = radix.Radix()

# Adding a node returns a RadixNode object. You can create
# arbitrary members in its 'data' dict to store your data
rnode = rtree.add("10.0.0.0/8")
rnode.data["blah"] = "whatever you want"

# You can specify nodes as CIDR addresses, or networks with
...
```

Sections: py-radix, Usage

</details>

### imagededup

Package for image deduplication

`pip install imagededup` · installs from source (sdist only) · licence: Apache-2.0 · rank 11269 · last release 2025-08-15 · [PyPI](https://pypi.org/project/imagededup/) · [docs](https://idealo.github.io/imagededup/)

<details><summary>README extract</summary>

imagededup is a python package that simplifies the task of finding exact and near duplicates in an image collection.

This package provides functionality to make use of hashing algorithms that are particularly good at finding exact
duplicates as well as convolutional neural networks which are also adept at finding near duplicates. ...

Example:
```python
from imagededup.methods import PHash
phasher = PHash()
```

Sections: Image Deduplicator (imagededup), 🚀 Quick Start, ⏳ Benchmarks, © Copyright

</details>

### hdwallet

Python-based library implementing a Hierarchical Deterministic (HD) Wallet generator for 200+ cryptocurrencies.

`pip install hdwallet` · installs (wheel) · licence: MIT License · rank 11279 · last release 2025-08-04 · [PyPI](https://pypi.org/project/hdwallet/) · [docs](https://hdwallet.readthedocs.com) · [source](https://github.com/hdwallet-io/python-hdwallet)

<details><summary>README extract</summary>

Python-based library implementing a Hierarchical Deterministic (HD) Wallet generator for 200+ cryptocurrencies.

> This library offers a flexible and scalable solution for developers integrating multi-currency wallet functionality. ...

Example:
```python
# !/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.entropies import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import BIP39_MNEMONIC_LANGUAGES
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.hds import BIP32HD
from hdwallet.derivations import CustomDerivation
...
```

Sections: Hierarchical Deterministic (HD) Wallet, Quick Usage, Example, Command Line Interface (CLI), Clients

</details>

### pyobjc-framework-Speech

Wrappers for the framework Speech on macOS

`pip install pyobjc-framework-Speech` · installs from source (sdist only) · licence: MIT · rank 11287 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Speech/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Speech" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### cart

CaRT Neutering format

`pip install cart` · installs (wheel) · licence: MIT License · rank 11308 · last release 2025-02-10 · [PyPI](https://pypi.org/project/cart/)

<details><summary>README extract</summary>

Compressed and RC4 Transport (CaRT) Neutering format. This is a file format that is used to neuter malware files for distribution in the malware analyst community.

</details>

### Unipath

Object-oriented alternative to os/os.path/shutil

`pip install Unipath` · installs from source (sdist only) · licence: MIT License · rank 11326 · last release 2015-02-11 · [PyPI](https://pypi.org/project/Unipath/)

<details><summary>README extract</summary>

Unipath is an object-oriented front end to the file/directory functions
scattered throughout several Python library modules. It's based on Jason
Orendorff's *path.py* but has a friendlier API and higher-level features.
Unipath is stable, well-tested, and has been used in production since 2008.
It runs on Python 2.6+ and 3.3+. ...

</details>

### llama-api-client

The official Python library for the llama-api-client API

`pip install llama-api-client` · installs (wheel) · licence: MIT License · rank 11345 · last release 2025-12-18 · [PyPI](https://pypi.org/project/llama-api-client/) · [source](https://github.com/meta-llama/llama-api-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Llama API Client Python library provides convenient access to the Llama API Client REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from llama_api_client import LlamaAPIClient

client = LlamaAPIClient(
    api_key=os.environ.get("LLAMA_API_KEY"),  # This is the default and can be omitted
)

create_chat_completion_response = client.chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "user",
        }
    ],
...
```

...

</details>

### namedlist

Similar to namedtuple, but instances are mutable.

`pip install namedlist` · installs (wheel) · licence: Apache Software License · rank 11348 · last release 2020-08-30 · [PyPI](https://pypi.org/project/namedlist/)

<details><summary>README extract</summary>

This package is no longer maintained, except for exceptional cases.
Please use the built-in dataclasses module instead.

Features:
namedlist provides 2 factory functions, namedlist.namedlist and
namedlist.namedtuple. namedlist.namedtuple is similar to
collections.namedtuple, with the following differences:

* namedlist.namedtuple supports per-field default values. ...

Example:
```python
>>> from namedlist import namedlist

>>> Point = namedlist('Point', 'x y')
>>> p = Point(1, 3)
>>> p.x = 2
>>> assert p.x == 2
>>> assert p.y == 3
```

...

</details>

### pylnk3

Windows LNK File Parser and Creator

`pip install pylnk3` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 11357 · last release 2025-04-28 · [PyPI](https://pypi.org/project/pylnk3/)

_README extract left out: share-alike licence._

### opencolorio

OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production with an emphasis on visual effects and computer animation.

`pip install opencolorio` · installs (wheel) · licence: Copyright Contributors to the OpenColorIO Project. · rank 11369 · last release 2026-10-01 · [PyPI](https://pypi.org/project/opencolorio/)

<details><summary>README extract</summary>

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the OpenColorIO Project. -->

Introduction

OpenColorIO (OCIO) is a complete color management solution geared towards
motion picture production with an emphasis on visual effects and computer
animation. ...

</details>

### prelude-python-sdk

The official Python library for the Prelude API

`pip install prelude-python-sdk` · installs (wheel) · licence: Apache Software License · rank 11370 · last release 2026-10-16 · [PyPI](https://pypi.org/project/prelude-python-sdk/) · [source](https://github.com/prelude-so/python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Prelude Python library provides convenient access to the Prelude REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from prelude_python_sdk import Prelude

client = Prelude(
    api_token=os.environ.get("API_TOKEN"),  # This is the default and can be omitted
)

verification = client.verification.create(
    target={
        "type": "phone_number",
        "value": "+30123456789",
    },
)
print(verification.id)
```

...

</details>

### pyobjc-framework-IOBluetoothUI

Wrappers for the framework IOBluetoothUI on macOS

`pip install pyobjc-framework-IOBluetoothUI` · installs (wheel) · licence: MIT · rank 11375 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-IOBluetoothUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "IOBluetoothUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-CoreWLAN

Wrappers for the framework CoreWLAN on macOS

`pip install pyobjc-framework-CoreWLAN` · installs from source (sdist only) · licence: MIT · rank 11379 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreWLAN/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreWLAN" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### django4-inline-actions

django4-inline-actions adds actions to each row of the ModelAdmin or InlineModelAdmin.

`pip install django4-inline-actions` · installs (wheel) · licence: BSD License · rank 11380 · last release 2025-05-07 · [PyPI](https://pypi.org/project/django4-inline-actions/) · [docs](https://github.com/HiroshiFuu/django4-inline-actions/blob/master/README.md) · [source](https://github.com/HiroshiFuu/django4-inline-actions)

<details><summary>README extract</summary>

<!-- -->
<!-- -->

django4-inline-actions adds actions to each row of the ModelAdmin or InlineModelAdmin. Add support for Django 4. And it should be supported by Django 5.

* Python 3.8 or newer

Example:
```python
from django.contrib import admin
from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin

from .models import Article, Author

class ArticleInline(InlineActionsMixin,
                    admin.TabularInline):
    model = Article
    inline_actions = []

...
```

...

</details>

### yamlable

A thin wrapper of PyYaml to convert Python objects to YAML and back.

`pip install yamlable` · installs (wheel) · licence: BSD License · rank 11396 · last release 2022-07-06 · [PyPI](https://pypi.org/project/yamlable/)

<details><summary>README extract</summary>

*A thin wrapper of PyYaml to convert Python objects to YAML and back.*

The documentation for users is available here:

A readme for developers is available here:

</details>

### spdx-python-model

SPDX Model Python Bindings

`pip install spdx-python-model` · installs (wheel) · licence: Apache-2.0 · rank 11398 · last release 2026-06-23 · [PyPI](https://pypi.org/project/spdx-python-model/) · [docs](https://spdx.github.io/spdx-python-model/doc/) · [source](https://github.com/spdx/spdx-python-model.git)

<details><summary>README extract</summary>

`spdx-python-model` is a Python library for working with the SPDX 3 data model.

Read the API documentation.

All bindings in this repository are auto-generated from the RDF and SHACL
definitions of the SPDX specification version 3 using
shacl2code during the package build
process. ...

Example:
```python
import spdx_python_model

p = spdx_python_model.v3_0_1.Person()
```

Sections: spdx-python-model, Usage

</details>

### django-fixture-magic

A few extra management tools to handle fixtures.

`pip install django-fixture-magic` · installs from source (sdist only) · licence: BSD License · rank 11406 · last release 2020-07-15 · [PyPI](https://pypi.org/project/django-fixture-magic/)

<details><summary>README extract</summary>

This package requires:

* Python 2.7, 3.6
* Django 1.8 - 2.1

Example:
```python
# Fixture Magic
CUSTOM_DUMPS = {
    'addon': {  # Initiate dump with: ./manage.py custom_dump addon id
        'primary': 'addons.addon',  # This is our reference model.
        'dependents': [  # These are the attributes/methods of the model that we wish to dump.
            'current_version',
            'current_version.files.all.0',
...
```

Sections: Requirements, Usage

</details>

### extra-platforms

🔎 Detect architectures, platforms, shells, terminals, CI systems and agents, grouped by family

`pip install extra-platforms` · installs (wheel) · licence: Apache-2.0 · rank 11425 · last release 2026-10-31 · [PyPI](https://pypi.org/project/extra-platforms/) · [docs](https://kdeldycke.github.io/extra-platforms) · [source](https://github.com/kdeldycke/extra-platforms)

<details><summary>README extract</summary>

Extra Platforms detects the runtime architecture, operating system (including Linux distribution), shell, terminal, CI environment & AI coding agents, and exposes rich, cacheable metadata (version, codename, icon, canonical URL). It also groups them into reusable families. ...

Example:
```python
>>> import extra_platforms
>>> extra_platforms.version
'13.13.0'
```

Sections: What is Extra Platforms?, Quick start, Examples, Architectures, Platforms, Shells, Terminals, CI systems, Agents, Used in

</details>

### json-with-comments

JSON with Comments (jsonc) for Python

`pip install json-with-comments` · installs (wheel) · licence: MIT · rank 11427 · last release 2026-08-24 · [PyPI](https://pypi.org/project/json-with-comments/) · [source](https://github.com/n-takumasa/json-with-comments)

<details><summary>README extract</summary>

Features:
* `load()`, `loads()`
 * Remove single line (`//`) and block comments (`/* */`)
 * Remove trailing commas from arrays and objects
* `dump()`, `dumps()`
 * Add comments
 * Add trailing commas

Example:
```python
>>> import jsonc
>>> jsonc.loads("{// comment \n}")
{}
>>> jsonc.loads("{/* comment */}")
{}
>>> jsonc.loads('{"spam": "ham // egg" /* comment */}')
{'spam': 'ham // egg'}
>>> jsonc.loads('{"spam": /* comment */"ham /* egg */"}')
{'spam': 'ham /* egg */'}
```

Sections: JSON with Comments for Python, Features, Usage

</details>

### pyobjc-framework-ServiceManagement

Wrappers for the framework ServiceManagement on macOS

`pip install pyobjc-framework-ServiceManagement` · installs (wheel) · licence: MIT · rank 11430 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ServiceManagement/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for framework 'ServiceManagement' on macOS 10.6. This framework
provides an interface to the system services subsystem, which basically means
a this provides a secure and object-oriented interface from launchd. ...

</details>

### eight

Python 2 to the power of 3. A lightweight porting helper library.

`pip install eight` · installs (wheel) · licence: Apache Software License · rank 11434 · last release 2021-03-16 · [PyPI](https://pypi.org/project/eight/)

<details><summary>README extract</summary>

Eight is a Python module that provides a minimalist compatibility layer between Python 3 and 2. Eight lets you write
code for Python 3.3+ while providing limited compatibility with Python 2.7 with no code changes. ...

Example:
```python
from eight import *
from eight import queue
from eight.collections import UserList, deque
```

Sections: eight: Python 2 to the power of 3, Synopsis, Wrapping stdio, Decoding command-line arguments, Wrapping environment variable getters and setters, Selecting from the buffet, Links, Bugs

</details>

### pygerrit2

Client library for interacting with Gerrit's REST API

`pip install pygerrit2` · installs from source (sdist only) · licence: MIT License · rank 11442 · last release 2021-06-03 · [PyPI](https://pypi.org/project/pygerrit2/)

<details><summary>README extract</summary>

Pygerrit2 provides a simple interface for clients to interact with
Gerrit Code Review via the REST API.

</details>

### multiprocessing

Backport of the multiprocessing package to Python 2.4 and 2.5

`pip install multiprocessing` · installs from source (sdist only) · licence: BSD License · rank 11446 · last release 2009-07-30 · [PyPI](https://pypi.org/project/multiprocessing/)

<details><summary>README extract</summary>

`multiprocessing` is a back port of the Python 2.6/3.0 multiprocessing
package. The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package.
This standalone variant is intended to be compatible with Python 2.4 and 2.5,
and will draw it's fixes/improvements from python-trunk. ...

Sections: python-multiprocessing, About, Bug reporting, Changes, 2.6.2.1 -- 2009-07-30, 2.6.1.1 -- 2009-02-07, 2.6.0.2 -- 2008-11-27, 2.6.0-0.1 -- 2008-10-27

</details>

### pytest-httpbin

Easily test your HTTP library against a local copy of httpbin

`pip install pytest-httpbin` · installs (wheel) · licence: MIT License · rank 11452 · last release 2024-09-18 · [PyPI](https://pypi.org/project/pytest-httpbin/)

<details><summary>README extract</summary>

httpbin is an amazing web service for testing HTTP libraries. It has several
great endpoints that can test pretty much everything you need in a HTTP
library. The only problem is: maybe you don't want to wait for your tests to
travel across the Internet and back to make assertions against a remote web
service.

Enter pytest-httpbin. ...

Example:
```python
def test_that_my_library_works_kinda_ok(httpbin):
    assert requests.get(httpbin.url + '/get/').status_code == 200
```

</details>

### pyobjc-framework-ImageCaptureCore

Wrappers for the framework ImageCaptureCore on macOS

`pip install pyobjc-framework-ImageCaptureCore` · installs from source (sdist only) · licence: MIT · rank 11456 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ImageCaptureCore/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ImageCaptureCore" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-Accessibility

Wrappers for the framework Accessibility on macOS

`pip install pyobjc-framework-Accessibility` · installs from source (sdist only) · licence: MIT · rank 11461 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Accessibility/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Accessibility" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pylint-junit

pylint reporter for junit format.

`pip install pylint-junit` · installs (wheel) · licence: MIT License · rank 11469 · last release 2025-01-21 · [PyPI](https://pypi.org/project/pylint-junit/)

<details><summary>README extract</summary>

Pylint plugin that generates JUnit based report that can be consumed
by CI environments like Jenkins, Azure Devops and such.

Features:
At the time of writing, few tools existed that where able to generate
JUnit format from pylint output. Both of these projects where not
handling "empty" results scenario well, eg both cases generated an empty
file and that caused issues in ci as the ...

Sections: pylint_junit, Why ?, Usage, Dependencies, Bugs / Feedback

</details>

### pyobjc-framework-Intents

Wrappers for the framework Intents on macOS

`pip install pyobjc-framework-Intents` · installs from source (sdist only) · licence: MIT · rank 11479 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Intents/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Intents" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-AVKit

Wrappers for the framework AVKit on macOS

`pip install pyobjc-framework-AVKit` · installs from source (sdist only) · licence: MIT · rank 11484 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AVKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AVKit" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### draftable-compare-api

Client library for the Draftable document comparison API

`pip install draftable-compare-api` · installs (wheel) · licence: MIT License · rank 11485 · last release 2025-08-21 · [PyPI](https://pypi.org/project/draftable-compare-api/) · [docs](https://github.com/draftable/compare-api-python-client/blob/stable/README.md) · [source](https://github.com/draftable/compare-api-python-client)

<details><summary>README extract</summary>

A thin Python client for the Draftable API which wraps all available endpoints and handles authentication and signing.

See the full API documentation for an introduction to the API, usage notes, and other reference material.

- Requirements
- Getting started
- CLI usage ...

Example:
```python
from draftable.endpoints import exceptions

identifier = '<identifier>'

try:
    comparison = comparisons.get(identifier)

    print("Comparison '{identifier}' ({visibility}) is {status}.".format(
        identifier = identifier,
        visibility = 'public' if comparison.public else 'private',
...
```

...

</details>

### pyobjc-framework-MapKit

Wrappers for the framework MapKit on macOS

`pip install pyobjc-framework-MapKit` · installs from source (sdist only) · licence: MIT · rank 11490 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MapKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MapKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### IxNetwork

IxNetwork Low Level API

`pip install IxNetwork` · installs (wheel) · licence: MIT License · rank 11492 · last release 2023-12-22 · [PyPI](https://pypi.org/project/IxNetwork/)

<details><summary>README extract</summary>

IxNetwork is the Python package for the IxNetwork Low Level API that allows you to configure and run IxNetwork tests.

Sections: Documentation, Compatibility Policy, Related Projects

</details>

### pyobjc-framework-SpriteKit

Wrappers for the framework SpriteKit on macOS

`pip install pyobjc-framework-SpriteKit` · installs from source (sdist only) · licence: MIT · rank 11495 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SpriteKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SpriteKit" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### aspose-cells-python

Aspose.Cells for Python via .NET is a high-performance library that unleashes the full potential of Excel in your Python projects. It can be used to efficiently manipulate and convert Excel and spreadsheet formats including XLS, XLSX, XLSB, ODS, CSV, and HTML - all from your Python code. Amazingly, it also offers free support.

`pip install aspose-cells-python` · does not install on CPython 3.14 · licence: Free To Use But Restricted; Other/Proprietary License · rank 11497 · last release 2026-10-16 · [PyPI](https://pypi.org/project/aspose-cells-python/) · [docs](https://docs.aspose.com/cells/python-net/)

<details><summary>README extract</summary>

Product Page API Reference Blog Free Support EULA

Try our free online apps demonstrating some of the most popular Aspose.Cells functionality.

Features:
Aspose.Cells for Python via .NET is a powerful spreadsheet management library that allows developers to create, format, and manipulate Excel files programmatically without the need for Microsoft Excel. It supports features like: ...

Example:
```python
# import the python package
import aspose.cells
from aspose.cells import License, Workbook, FileFormatType

# Instantiating a Workbook object
workbook = Workbook()
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the "A1" cell
cell = worksheet.cells.get("A1")
# Write "Hello World" to  "A1" in the first sheet
...
```

...

</details>

### prodict

A dict with dot-accessible attributes, IDE auto-completion and type conversion driven by annotations.

`pip install prodict` · installs (wheel) · licence: MIT · rank 11501 · last release 2026-10-26 · [PyPI](https://pypi.org/project/prodict/) · [docs](https://github.com/ramazanpolat/prodict/tree/master/docs) · [source](https://github.com/ramazanpolat/prodict)

<details><summary>README extract</summary>

**Prodict is a `dict` with dot-accessible attributes, IDE auto-completion, and type
conversion driven by annotations.**

Features:
- `d'key1'['key3']` is noisy and easy to get wrong; `d.key1.key2.key3` is not.
- Web services talk JSON. Turning a JSON response into objects you can navigate, with
 the types you expect, should take one line. ...

Example:
```python
class Comment:
    def init(self, user_id, comment, date):
        self.user_id = user_id
        self.comment = comment
        self.date = date

class Post:
    def init(self, title, date, comments):
        self.title = title
        self.date = date
        self.comments = comments

class User:
    def init(self, user_id, user_name, posts):
...
```

...

</details>

### pyobjc-framework-CryptoTokenKit

Wrappers for the framework CryptoTokenKit on macOS

`pip install pyobjc-framework-CryptoTokenKit` · installs from source (sdist only) · licence: MIT · rank 11505 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CryptoTokenKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CryptoTokenKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-CoreSpotlight

Wrappers for the framework CoreSpotlight on macOS

`pip install pyobjc-framework-CoreSpotlight` · installs from source (sdist only) · licence: MIT · rank 11510 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreSpotlight/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreSpotlight" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-StoreKit

Wrappers for the framework StoreKit on macOS

`pip install pyobjc-framework-StoreKit` · installs from source (sdist only) · licence: MIT · rank 11511 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-StoreKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "StoreKit" framework on macOS 10.7 or later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-ContactsUI

Wrappers for the framework ContactsUI on macOS

`pip install pyobjc-framework-ContactsUI` · installs from source (sdist only) · licence: MIT · rank 11512 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ContactsUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ContactsUI" framework on macOS 10.11.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-GameCenter

Wrappers for the framework GameCenter on macOS

`pip install pyobjc-framework-GameCenter` · installs from source (sdist only) · licence: MIT · rank 11514 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-GameCenter/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "GameCenter" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-MultipeerConnectivity

Wrappers for the framework MultipeerConnectivity on macOS

`pip install pyobjc-framework-MultipeerConnectivity` · installs from source (sdist only) · licence: MIT · rank 11515 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MultipeerConnectivity/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MultipeerConnectivity" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### urbanairship

``urbanairship`` is a Python library for using the Airship REST

`pip install urbanairship` · installs (wheel) · licence: Apache Software License · rank 11517 · last release 2026-10-27 · [PyPI](https://pypi.org/project/urbanairship/) · [docs](https://docs.airship.com/) · [source](https://github.com/urbanairship/python-library)

<details><summary>README extract</summary>

`urbanairship` is a Python library for using the Airship REST
API for push notifications, message
center messages, email, and SMS.

Python 3.10 or higher is required. Other requirements can be found in requirements.txt.

The best place to ask questions or report a problem is our support site:

Sections: Requirements, Questions, Usage

</details>

### pyobjc-framework-SceneKit

Wrappers for the framework SceneKit on macOS

`pip install pyobjc-framework-SceneKit` · installs from source (sdist only) · licence: MIT · rank 11519 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SceneKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SceneKit" framework on macOS introduced in macOS 10.8.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-GameController

Wrappers for the framework GameController on macOS

`pip install pyobjc-framework-GameController` · installs from source (sdist only) · licence: MIT · rank 11528 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-GameController/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "GameController" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-ModelIO

Wrappers for the framework ModelIO on macOS

`pip install pyobjc-framework-ModelIO` · installs from source (sdist only) · licence: MIT · rank 11529 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ModelIO/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ModelIO" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SafariServices

Wrappers for the framework SafariServices on macOS

`pip install pyobjc-framework-SafariServices` · installs from source (sdist only) · licence: MIT · rank 11530 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SafariServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SafariServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-CoreMediaIO

Wrappers for the framework CoreMediaIO on macOS

`pip install pyobjc-framework-CoreMediaIO` · installs from source (sdist only) · licence: MIT · rank 11533 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreMediaIO/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreMediaIO" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-Network

Wrappers for the framework Network on macOS

`pip install pyobjc-framework-Network` · installs from source (sdist only) · licence: MIT · rank 11534 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Network/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Network" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-NetworkExtension

Wrappers for the framework NetworkExtension on macOS

`pip install pyobjc-framework-NetworkExtension` · installs from source (sdist only) · licence: MIT · rank 11536 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-NetworkExtension/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "NetworkExtension" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-FileProvider

Wrappers for the framework FileProvider on macOS

`pip install pyobjc-framework-FileProvider` · installs from source (sdist only) · licence: MIT · rank 11539 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-FileProvider/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "FileProvider" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-NotificationCenter

Wrappers for the framework NotificationCenter on macOS

`pip install pyobjc-framework-NotificationCenter` · installs from source (sdist only) · licence: MIT · rank 11541 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-NotificationCenter/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "NotificationCenter" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-MetalPerformanceShaders

Wrappers for the framework MetalPerformanceShaders on macOS

`pip install pyobjc-framework-MetalPerformanceShaders` · installs from source (sdist only) · licence: MIT · rank 11542 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MetalPerformanceShaders/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MetalPerformanceShaders" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-PhotosUI

Wrappers for the framework PhotosUI on macOS

`pip install pyobjc-framework-PhotosUI` · installs from source (sdist only) · licence: MIT · rank 11543 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PhotosUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PhotosUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### mcpadapt

Adapt MCP servers to many agentic framework.

`pip install mcpadapt` · installs (wheel) · licence: MIT · rank 11549 · last release 2025-10-24 · [PyPI](https://pypi.org/project/mcpadapt/) · [source](https://github.com/grll/mcpadapt)

<details><summary>README extract</summary>

For more context, guides and API references visit our new documentation.

Unlock 650+ MCP servers tools in your favorite agentic framework.

Model Context Protocol is an open-source protocol introduced by Anthropic which allows anyone to simply and quickly make tools and resources available as "MCP Servers". ...

Example:
```python
from mcp import StdioServerParameters
from smolagents.tools import ToolCollection

serverparams = StdioServerParameters(command="uv", args=["run", "src/echo.py"])

with ToolCollection.from_mcp(serverparams) as tool_collection:
    ... # enjoy your tools!
```

Sections: MCPAdapt, Smolagents, Other Frameworks, Usage, Roadmap

</details>

### unicode-slugify

A slug generator that turns strings into unicode slugs.

`pip install unicode-slugify` · installs (wheel) · licence: BSD License · rank 11554 · last release 2021-10-20 · [PyPI](https://pypi.org/project/unicode-slugify/)

<details><summary>README extract</summary>

Unicode Slugify is a slugifier that generates unicode slugs. It was originally
used in the Firefox Add-ons web site to generate slugs for add-ons and add-on
collections. Many of these add-ons and collections had unicode characters and
required more than simple transliteration.

Example:
```python
from slugify import slugify, SLUG_OK

# Default usage : lower, spaces replaced with "-", only alphanum and "-_~" chars, keeps unicode
slugify(u'Bän...g (bang)')
# u'bäng-bang'

# Keep capital letters and spaces
slugify(u'Bän...g (bang)', lower=False, spaces=True)
# u'Bäng bang'

# Replace non ascii chars with their "best" representation
...
```

Sections: Unicode Slugify, Usage, Thanks

</details>

### pyobjc-framework-ExternalAccessory

Wrappers for the framework ExternalAccessory on macOS

`pip install pyobjc-framework-ExternalAccessory` · installs from source (sdist only) · licence: MIT · rank 11557 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ExternalAccessory/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ExternalAccessory" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-GameplayKit

Wrappers for the framework GameplayKit on macOS

`pip install pyobjc-framework-GameplayKit` · installs from source (sdist only) · licence: MIT · rank 11558 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-GameplayKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "GameplayKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-VideoToolbox

Wrappers for the framework VideoToolbox on macOS

`pip install pyobjc-framework-VideoToolbox` · installs from source (sdist only) · licence: MIT · rank 11562 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-VideoToolbox/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "VideoToolbox" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-MetalKit

Wrappers for the framework MetalKit on macOS

`pip install pyobjc-framework-MetalKit` · installs from source (sdist only) · licence: MIT · rank 11563 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MetalKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MetalKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-GameKit

Wrappers for the framework GameKit on macOS

`pip install pyobjc-framework-GameKit` · installs from source (sdist only) · licence: MIT · rank 11564 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-GameKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "GameKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-AuthenticationServices

Wrappers for the framework AuthenticationServices on macOS

`pip install pyobjc-framework-AuthenticationServices` · installs from source (sdist only) · licence: MIT · rank 11570 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AuthenticationServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AuthenticationServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-MediaToolbox

Wrappers for the framework MediaToolbox on macOS

`pip install pyobjc-framework-MediaToolbox` · installs from source (sdist only) · licence: MIT · rank 11576 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MediaToolbox/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MediaToolbox" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-CoreMotion

Wrappers for the framework CoreMotion on macOS

`pip install pyobjc-framework-CoreMotion` · installs from source (sdist only) · licence: MIT · rank 11582 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreMotion/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreMotion" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyphonetics

A Python 3 phonetics library.

`pip install pyphonetics` · installs (wheel) · licence: MIT License · rank 11601 · last release 2020-02-25 · [PyPI](https://pypi.org/project/pyphonetics/)

<details><summary>README extract</summary>

Pyphonetics is a Python 3 library for phonetic algorithms. Right now, the following algorithms are implemented and supported:

 * Soundex
 * Metaphone
 * Refined Soundex
 * Fuzzy Soundex
 * Lein
 * Matching Rating Approach

More will be added in the future.

The module is available in PyPI, just use `pip install pyphonetics`.

Sections: Pyphonetics, Instalation, Usage

</details>

### pyobjc-framework-AutomaticAssessmentConfiguration

Wrappers for the framework AutomaticAssessmentConfiguration on macOS

`pip install pyobjc-framework-AutomaticAssessmentConfiguration` · installs from source (sdist only) · licence: MIT · rank 11602 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AutomaticAssessmentConfiguration/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AutomaticAssessmentConfiguration" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### skypilot-nightly

SkyPilot: Manage all your AI compute.

`pip install skypilot-nightly` · installs (wheel) · licence: Apache Software License · rank 11612 · last release 2026-11-06 · [PyPI](https://pypi.org/project/skypilot-nightly/) · [docs](https://docs.skypilot.co/)

<details><summary>README extract</summary>

SkyPilot is a system to run, manage, and scale AI workloads on any AI infrastructure.

SkyPilot gives AI teams a simple interface to run jobs on any infra.
Infra teams get a unified control plane to manage any AI compute — with advanced scheduling, scaling, and orchestration.

:fire: *News* :fire: ...

Features:
SkyPilot is easy to use for AI users:
- Quickly spin up compute on your own infra
- Environment and job as code — simple and portable
- Easy job management: queue, run, and auto-recover many jobs ...

Sections: Manage all your AI compute, Overview, Getting started, Benefits of SkyPilot on Kubernetes, SkyPilot in 1 minute, Runnable examples, Learn more, Questions and feedback

</details>

### pyobjc-framework-PushKit

Wrappers for the framework PushKit on macOS

`pip install pyobjc-framework-PushKit` · installs from source (sdist only) · licence: MIT · rank 11617 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PushKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PushKit" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-OSLog

Wrappers for the framework OSLog on macOS

`pip install pyobjc-framework-OSLog` · installs from source (sdist only) · licence: MIT · rank 11623 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-OSLog/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "OSLog" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SystemExtensions

Wrappers for the framework SystemExtensions on macOS

`pip install pyobjc-framework-SystemExtensions` · installs from source (sdist only) · licence: MIT · rank 11624 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SystemExtensions/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SystemExtensions" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-AudioVideoBridging

Wrappers for the framework AudioVideoBridging on macOS

`pip install pyobjc-framework-AudioVideoBridging` · installs from source (sdist only) · licence: MIT · rank 11633 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AudioVideoBridging/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AudioVideoBridging" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-Virtualization

Wrappers for the framework Virtualization on macOS

`pip install pyobjc-framework-Virtualization` · installs from source (sdist only) · licence: MIT · rank 11636 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Virtualization/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Virtualization" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### chromedriver-binary

Installer for chromedriver.

`pip install chromedriver-binary` · installs from source (sdist only) · licence: MIT License · rank 11638 · last release 2026-11-08 · [PyPI](https://pypi.org/project/chromedriver-binary/)

<details><summary>README extract</summary>

Downloads and installs the chromedriver binary version 159.0.8149.0 for automated testing of webapps. The installer supports Linux, MacOS and Windows operating systems.

Alternatively the package chromedriver-binary-auto can be used to automatically detect the latest chromedriver version required for the installed Chrome/Chromium browser.

Example:
```python
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()
driver.get("
assert "Python" in driver.title
```

Sections: chromedriver-binary, Latest and fixed versions, From PyPI, From GitHub, Automatically detected versions, Usage, Example, Exporting chromedriver binary path

</details>

### PyPDF4

PDF toolkit

`pip install PyPDF4` · installs from source (sdist only) · licence: BSD License · rank 11639 · last release 2018-08-07 · [PyPI](https://pypi.org/project/PyPDF4/)

<details><summary>README extract</summary>

A Pure-Python library built as a PDF toolkit. It is capable of:

- extracting document information (title, author, ...)
- splitting documents page by page
- merging documents page by page
- cropping pages
- merging multiple pages into a single page
- encrypting and decrypting PDF files
- and more! ...

</details>

### pyobjc-framework-PassKit

Wrappers for the framework PassKit on macOS

`pip install pyobjc-framework-PassKit` · installs from source (sdist only) · licence: MIT · rank 11642 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PassKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PassKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-IntentsUI

Wrappers for the framework Intents on macOS

`pip install pyobjc-framework-IntentsUI` · installs from source (sdist only) · licence: MIT · rank 11646 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-IntentsUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "IntentsUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-ReplayKit

Wrappers for the framework ReplayKit on macOS

`pip install pyobjc-framework-ReplayKit` · installs from source (sdist only) · licence: MIT · rank 11647 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ReplayKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ReplayKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-CallKit

Wrappers for the framework CallKit on macOS

`pip install pyobjc-framework-CallKit` · installs from source (sdist only) · licence: MIT · rank 11651 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CallKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CallKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-ClassKit

Wrappers for the framework ClassKit on macOS

`pip install pyobjc-framework-ClassKit` · installs from source (sdist only) · licence: MIT · rank 11653 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ClassKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ClassKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-ShazamKit

Wrappers for the framework ShazamKit on macOS

`pip install pyobjc-framework-ShazamKit` · installs from source (sdist only) · licence: MIT · rank 11659 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ShazamKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ShazamKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-MetricKit

Wrappers for the framework MetricKit on macOS

`pip install pyobjc-framework-MetricKit` · installs from source (sdist only) · licence: MIT · rank 11660 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MetricKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MetricKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### PyBoolector

Python wrapper around the Boolector SMT solver

`pip install PyBoolector` · installs (wheel) · licence: MIT License · rank 11666 · last release 2026-10-14 · [PyPI](https://pypi.org/project/PyBoolector/)

<details><summary>README extract</summary>

This package, specifically, enables the Boolector Python wrapper
 to be installed from PyPi

</details>

### pyobjc-framework-libxpc

Wrappers for xpc on macOS

`pip install pyobjc-framework-libxpc` · installs from source (sdist only) · licence: MIT · rank 11671 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-libxpc/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "xpc" library on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### peopledatalabs

Official Python client for the People Data Labs API

`pip install peopledatalabs` · installs (wheel) · licence: MIT License · rank 11675 · last release 2026-01-12 · [PyPI](https://pypi.org/project/peopledatalabs/) · [docs](https://docs.peopledatalabs.com) · [source](https://github.com/peopledatalabs/peopledatalabs-python)

<details><summary>README extract</summary>

Official Python client for the People Data Labs API.

Example:
```python
from peopledatalabs import PDLPY

# specify your API key
client = PDLPY(
    api_key="YOUR API KEY",
)
```

Sections: People Data Labs Python Client, 🚀 Usage, Getting Person Data, By Enrichment, By Bulk Enrichment, By Search (Elasticsearch), By Search (SQL), By `PDL_ID` (Retrieve API), By Fuzzy Enrichment (Identify API), Getting Company Data

</details>

### pyobjc-framework-MediaPlayer

Wrappers for the framework MediaPlayer on macOS

`pip install pyobjc-framework-MediaPlayer` · installs (wheel) · licence: MIT · rank 11685 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MediaPlayer/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MediaPlayer" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### uplink

A Declarative HTTP Client for Python.

`pip install uplink` · installs (wheel) · licence: MIT License · rank 11686 · last release 2025-06-14 · [PyPI](https://pypi.org/project/uplink/) · [source](https://github.com/prkumar/uplink)

<details><summary>README extract</summary>

- Builds Reusable Objects for Consuming Web APIs.
- Works with Requests, aiohttp, and Twisted.
- Inspired by Retrofit.

Uplink turns your HTTP API into a Python class.

Build an instance to interact with the webservice.

Then, executing an HTTP request is as simply as invoking a method.

The returned object is a friendly `requests.Response`: ...

Features:
- Quickly Define Structured API Clients
 - Use decorators and type hints to describe each HTTP request
 - JSON, URL-encoded, and multipart request body and file upload
 - URL parameter replacement, request headers, and query parameter support ...

Example:
```python
from uplink import Consumer, get, Path, Query

class GitHub(Consumer):
    """A Python Client for the GitHub API."""

    @get("users/{user}/repos")
...

</details>

### rebulk

Rebulk - Define simple search patterns in bulk to perform advanced matching on any string.

`pip install rebulk` · installs (wheel) · licence: MIT · rank 11688 · last release 2026-07-03 · [PyPI](https://pypi.org/project/rebulk/)

<details><summary>README extract</summary>

ReBulk is a python library that performs advanced searches in strings
that would be hard to implement using re
module or String
methods only.

It includes some features like `Patterns`, `Match`, `Rule` that allows
developers to build a custom and complex string matcher using a readable
and extendable API.

This project is hosted on GitHub: <

Example:
```python
>>> from rebulk import Rebulk
>>> bulk = Rebulk().string('brown').regex(r'qu\w+').functional(lambda s: (20, 25))
```

Sections: ReBulk, Usage, String Patterns, Regular Expression Patterns, Functional Patterns, Chain Patterns, Patterns parameters, Match, Matches, Typed retrieval, Markers, Rules

</details>

### pyobjc-framework-OpenDirectory

Wrappers for the framework OpenDirectory on macOS

`pip install pyobjc-framework-OpenDirectory` · installs (wheel) · licence: MIT · rank 11707 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-OpenDirectory/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the 'OpenDirectory' and 'CFOpenDirectory' frameworks on
macOS 10.6 and later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks ...

</details>

### mo-parsing

Another PEG Parsing Tool

`pip install mo-parsing` · installs (wheel) · licence: MIT License · rank 11716 · last release 2026-08-22 · [PyPI](https://pypi.org/project/mo-parsing/)

<details><summary>README extract</summary>

A fork of pyparsing for faster parsing

Example:
```python
>>> from mo_parsing import Word
>>> from mo_parsing.utils import alphas
>>>
>>> greet = Word(alphas)("greeting") + "," + Word(alphas)("person") + "!"
>>> result = greet.parse_string("Hello, World!")
```

Sections: More Parsing!, Usage, The `Whitespace` Context, Navigating ParseResults, Parse Actions, Simple example, Debugging, Regular Expressions, Differences from PyParsing

</details>

### pyobjc-framework-MetalFX

Wrappers for the framework MetalFX on macOS

`pip install pyobjc-framework-MetalFX` · installs from source (sdist only) · licence: MIT · rank 11722 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MetalFX/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MetalFX" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-HealthKit

Wrappers for the framework HealthKit on macOS

`pip install pyobjc-framework-HealthKit` · installs from source (sdist only) · licence: MIT · rank 11737 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-HealthKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "HealthKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-AVRouting

Wrappers for the framework AVRouting on macOS

`pip install pyobjc-framework-AVRouting` · installs from source (sdist only) · licence: MIT · rank 11741 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AVRouting/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AVRouting" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SharedWithYou

Wrappers for the framework SharedWithYou on macOS

`pip install pyobjc-framework-SharedWithYou` · installs from source (sdist only) · licence: MIT · rank 11742 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SharedWithYou/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SharedWithYou" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-BackgroundAssets

Wrappers for the framework BackgroundAssets on macOS

`pip install pyobjc-framework-BackgroundAssets` · installs from source (sdist only) · licence: MIT · rank 11743 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-BackgroundAssets/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "BackgroundAssets" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-Accounts

Wrappers for the framework Accounts on macOS

`pip install pyobjc-framework-Accounts` · installs (wheel) · licence: MIT · rank 11744 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Accounts/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Accounts" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SharedWithYouCore

Wrappers for the framework SharedWithYouCore on macOS

`pip install pyobjc-framework-SharedWithYouCore` · installs from source (sdist only) · licence: MIT · rank 11745 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SharedWithYouCore/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SharedWithYouCore" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-ExtensionKit

Wrappers for the framework ExtensionKit on macOS

`pip install pyobjc-framework-ExtensionKit` · installs from source (sdist only) · licence: MIT · rank 11749 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ExtensionKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ExtensionKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SafetyKit

Wrappers for the framework SafetyKit on macOS

`pip install pyobjc-framework-SafetyKit` · installs from source (sdist only) · licence: MIT · rank 11753 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SafetyKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SafetyKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-Social

Wrappers for the framework Social on macOS

`pip install pyobjc-framework-Social` · installs (wheel) · licence: MIT · rank 11756 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Social/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Social" framework on macOS 10.8 or later.

Note that this framework is only available for 64-bit code.

* Documentation

* Issue Tracker

* Repository

</details>

### aioprometheus

A Prometheus Python client library for asyncio-based applications

`pip install aioprometheus` · installs (wheel) · licence: MIT License · rank 11761 · last release 2023-12-27 · [PyPI](https://pypi.org/project/aioprometheus/)

<details><summary>README extract</summary>

`aioprometheus` is a Prometheus Python client library for asyncio-based
applications. It provides metrics collection and serving capabilities for
use with Prometheus and compatible monitoring systems. It supports exporting
metrics into text and pushing metrics to a gateway. ...

Example:
```python
from aioprometheus import Counter

events_counter = Counter(
    "events_counter",
    "Total number of events.",
)

events_counter.inc({"kind": "event A"})
```

Sections: aioprometheus, Usage

</details>

### BrazilFiscalReport

Python library for generating Brazilian auxiliary fiscal documents in PDF from XML documents.

`pip install BrazilFiscalReport` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 11766 · last release 2026-10-13 · [PyPI](https://pypi.org/project/BrazilFiscalReport/)

_README extract left out: share-alike licence._

### dataiku-api-client

Python API client for Dataiku APIs

`pip install dataiku-api-client` · installs from source (sdist only) · licence: Apache Software License · rank 11773 · last release 2026-11-02 · [PyPI](https://pypi.org/project/dataiku-api-client/)

<details><summary>README extract</summary>

API client for Dataiku Data Science Studio

For more information, see:

Sections: 15.2.1 (2026-11-02), 15.2.0 (2026-10-16), 15.1.0 (2026-10-09), 15.0.2 (2026-09-29), 15.0.1 (2026-09-15), 15.0.0 (2026-08-14), 14.7.5 (2026-09-29), 14.7.4 (2026-09-14), 14.7.3 (2026-08-03), 14.7.2 (2026-07-13), 14.7.1 (2026-07-13), 14.7.0 (2026-06-18), 14.6.2 (2026-06-15), 14.6.1 (2026-06-05)

</details>

### static3

A really simple WSGI way to serve static (or mixed) content.

`pip install static3` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 11790 · last release 2016-05-10 · [PyPI](https://pypi.org/project/static3/)

_README extract left out: share-alike licence._

### pyobjc-framework-NaturalLanguage

Wrappers for the framework NaturalLanguage on macOS

`pip install pyobjc-framework-NaturalLanguage` · installs (wheel) · licence: MIT · rank 11791 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-NaturalLanguage/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "NaturalLanguage" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-CloudKit

Wrappers for the framework CloudKit on macOS

`pip install pyobjc-framework-CloudKit` · installs (wheel) · licence: MIT · rank 11793 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CloudKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CloudKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-ColorSync

Wrappers for the framework ColorSync on Mac OS X

`pip install pyobjc-framework-ColorSync` · installs (wheel) · licence: MIT · rank 11795 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ColorSync/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ColorSync" framework on MacOSX 10.13 or later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-iTunesLibrary

Wrappers for the framework iTunesLibrary on macOS

`pip install pyobjc-framework-iTunesLibrary` · installs (wheel) · licence: MIT · rank 11803 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-iTunesLibrary/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "iTunesLibrary" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks ...

</details>

### pyobjc-framework-IOSurface

Wrappers for the framework IOSurface on macOS

`pip install pyobjc-framework-IOSurface` · installs (wheel) · licence: MIT · rank 11811 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-IOSurface/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "IOSurface" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-NetFS

Wrappers for the framework NetFS on macOS

`pip install pyobjc-framework-NetFS` · installs (wheel) · licence: MIT · rank 11812 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-NetFS/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "NetFS" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-BusinessChat

Wrappers for the framework BusinessChat on macOS

`pip install pyobjc-framework-BusinessChat` · installs (wheel) · licence: MIT · rank 11814 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-BusinessChat/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "BusinessChat" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-FinderSync

Wrappers for the framework FinderSync on macOS

`pip install pyobjc-framework-FinderSync` · installs (wheel) · licence: MIT · rank 11818 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-FinderSync/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "FinderSync" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-MediaLibrary

Wrappers for the framework MediaLibrary on macOS

`pip install pyobjc-framework-MediaLibrary` · installs (wheel) · licence: MIT · rank 11822 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MediaLibrary/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MediaLibrary" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-MediaAccessibility

Wrappers for the framework MediaAccessibility on macOS

`pip install pyobjc-framework-MediaAccessibility` · installs (wheel) · licence: MIT · rank 11831 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MediaAccessibility/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AVKit" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-AdSupport

Wrappers for the framework AdSupport on macOS

`pip install pyobjc-framework-AdSupport` · installs (wheel) · licence: MIT · rank 11838 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AdSupport/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AdSupport" framework on macOS 10.14 or later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-BrowserEngineKit

Wrappers for the framework BrowserEngineKit on macOS

`pip install pyobjc-framework-BrowserEngineKit` · installs from source (sdist only) · licence: MIT · rank 11840 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-BrowserEngineKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "BrowserEngineKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-VideoSubscriberAccount

Wrappers for the framework VideoSubscriberAccount on macOS

`pip install pyobjc-framework-VideoSubscriberAccount` · installs (wheel) · licence: MIT · rank 11845 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-VideoSubscriberAccount/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "VideoSubscriberAccount" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### hazelcast-python-client

Hazelcast Python Client

`pip install hazelcast-python-client` · installs (wheel) · licence: Apache Software License · rank 11850 · last release 2026-06-25 · [PyPI](https://pypi.org/project/hazelcast-python-client/)

<details><summary>README extract</summary>

Hazelcast is an open-source distributed
in-memory data store and computation platform that provides a wide
variety of distributed data structures and concurrency primitives.

Hazelcast Python client is a way to communicate to Hazelcast clusters
and access the cluster data. ...

Example:
```python
import hazelcast

# Connect to Hazelcast cluster.
client = hazelcast.HazelcastClient()

# Get or create the "distributed-map" on the cluster.
distributed_map = client.get_map("distributed-map")

# Put "key", "value" pair into the "distributed-map" and wait for
# the request to complete.
distributed_map.set("key", "value").result()

...
```

Sections: Hazelcast Python Client, Hazelcast, Client, Overview, Usage, Configuration, Features, Getting Help, Issue Reports, Pull Requests, Copyright

</details>

### pyobjc-framework-SoundAnalysis

Wrappers for the framework SoundAnalysis on macOS

`pip install pyobjc-framework-SoundAnalysis` · installs (wheel) · licence: MIT · rank 11851 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SoundAnalysis/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SoundAnalysis" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-MetalPerformanceShadersGraph

Wrappers for the framework MetalPerformanceShadersGraph on macOS

`pip install pyobjc-framework-MetalPerformanceShadersGraph` · installs (wheel) · licence: MIT · rank 11856 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MetalPerformanceShadersGraph/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MetalPerformanceShadersGraph" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-FileProviderUI

Wrappers for the framework FileProviderUI on macOS

`pip install pyobjc-framework-FileProviderUI` · installs (wheel) · licence: MIT · rank 11865 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-FileProviderUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "FileProviderUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-CoreHaptics

Wrappers for the framework CoreHaptics on macOS

`pip install pyobjc-framework-CoreHaptics` · installs (wheel) · licence: MIT · rank 11868 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CoreHaptics/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CoreHaptics" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-DeviceCheck

Wrappers for the framework DeviceCheck on macOS

`pip install pyobjc-framework-DeviceCheck` · installs (wheel) · licence: MIT · rank 11869 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DeviceCheck/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DeviceCheck" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-PencilKit

Wrappers for the framework PencilKit on macOS

`pip install pyobjc-framework-PencilKit` · installs (wheel) · licence: MIT · rank 11870 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PencilKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PencilKit" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-ExecutionPolicy

Wrappers for the framework ExecutionPolicy on macOS

`pip install pyobjc-framework-ExecutionPolicy` · installs (wheel) · licence: MIT · rank 11872 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ExecutionPolicy/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ExecutionPolicy" framework on macOS 10.15 and later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-QuickLookThumbnailing

Wrappers for the framework QuickLookThumbnailing on macOS

`pip install pyobjc-framework-QuickLookThumbnailing` · installs (wheel) · licence: MIT · rank 11878 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-QuickLookThumbnailing/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "QuickLookThumbnailing" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-LinkPresentation

Wrappers for the framework LinkPresentation on macOS

`pip install pyobjc-framework-LinkPresentation` · installs (wheel) · licence: MIT · rank 11879 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-LinkPresentation/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "LinkPresentation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### fastmcp-dishka

Dishka dependency injection integration for FastMCP

`pip install fastmcp-dishka` · installs (wheel) · licence: Apache-2.0 · rank 11881 · last release 2026-10-15 · [PyPI](https://pypi.org/project/fastmcp-dishka/) · [source](https://github.com/vfaddey/fastmcp-dishka)

<details><summary>README extract</summary>

Integration package for using dishka dependency
injection with FastMCP tools, resources, and prompts.

It provides:

* `FastMCPProvider` with FastMCP request context objects for dishka.
* `setup_dishka()` middleware that opens a `Scope.REQUEST` container per
 tool/resource/prompt call.
* `@inject` support for parameters marked as `FromDishka[T]`.

Example:
```python
from dishka import Provider, Scope, make_async_container, provide
from fastmcp import FastMCP
from fastmcp_dishka import FastMCPProvider, FromDishka, inject, setup_dishka

class GreetingService:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"

class AppProvider(Provider):
...
```

Sections: FastMCP Dishka, Usage

</details>

### mo-sql-parsing

More SQL Parsing! Parse SQL into JSON parse tree

`pip install mo-sql-parsing` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11885 · last release 2026-08-22 · [PyPI](https://pypi.org/project/mo-sql-parsing/)

<details><summary>README extract</summary>

Parse SQL into JSON so we can translate it for other datastores!

See changes

The objective is to convert SQL queries to JSON-izable parse trees. This originally targeted MySQL, but has grown to include other database engines. *Please paste some SQL into a new issue if it does not work for you*

Example:
```python
def listwrap(value):
    if value is None:
        return []
    elif isinstance(value, list)
        return value
    else:
        return [value]
```

Sections: More SQL Parsing!, Objective, Parsing SQL, SQL Flavours, Double-quotes for literal strings, SQLServer Identifiers (`[]`), NULL is None, Normalized function call form, Generating SQL, Run Tests, More about implementation, Array Programming, Version Changes, Features, Version 11

</details>

### django-ajax-selects

Edit ForeignKey, ManyToManyField and CharField in Django Admin using jQuery UI AutoComplete.

`pip install django-ajax-selects` · installs (wheel) · licence: MIT License; Other/Proprietary License · rank 11887 · last release 2024-09-14 · [PyPI](https://pypi.org/project/django-ajax-selects/) · [docs](https://django-ajax-selects.readthedocs.io/en/latest/) · [source](https://github.com/crucialfelix/django-ajax-selects)

<details><summary>README extract</summary>

Example:
```python
# yourapp/lookups.py
from ajax_select import register, LookupChannel
from .models import Tag

@register('tags')
class TagsLookup(LookupChannel):

    model = Tag

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')[:50]

    def format_item_display(self, item):
...
```

Sections: Documentation, Quick Usage, Fully customizable, Assets included by default, Customize jquery, Compatibility

</details>

### dict-recursive-update

A Python module who does recursive update work on 2 dicts.

`pip install dict-recursive-update` · installs (wheel) · licence: MIT License · rank 11890 · last release 2018-01-23 · [PyPI](https://pypi.org/project/dict-recursive-update/)

<details><summary>README extract</summary>

A Python module who does recursive update work on 2 dicts.

Features:
This is originally designed for merge multiple configurations in different running environment such as production or stage.

As a node.js developer, package config and lodash are very handy for me. ...

Example:
```python
>>> from dict_recursive_update import recursive_update

>>> recursive_update({'a': {'b': 2}}, {'a': {'b': 3, 'd': 4}, 'e': 5})
{'a': {'b': 3, 'd': 4}, 'e': 5}

>>> recursive_update('a', 'b')
Traceback (most recent call last):
    ...
TypeError: Params of recursive_update should be dicts

...
```

Sections: dict-recursive-update, Usage, Examples, Why?

</details>

### smsapi-client

SmsAPI client

`pip install smsapi-client` · installs (wheel) · licence: Apache Software License · rank 11892 · last release 2026-05-14 · [PyPI](https://pypi.org/project/smsapi-client/)

<details><summary>README extract</summary>

﻿# smsapi-python

Client for SMSAPI.

Compatible with Python 2.7+, 3.+.

requests

Example:
```python
from smsapi.client import SmsApiPlClient
```

Sections: COMPATIBILITY, REQUIREMENTS, Client instance, Credentials, Access Token, Examples, Send SMS, Error handling

</details>

### rootpath

Python project/package root path detection.

`pip install rootpath` · installs (wheel) · licence: MIT License · rank 11896 · last release 2019-03-10 · [PyPI](https://pypi.org/project/rootpath/) · [source](https://github.com/grimen/python-rootpath)

<details><summary>README extract</summary>

*Python project/package root path detection.*

Auto-magic project/package root path detection - from a child module file for Python libraries/projects.

It does this by detecting typical package/project root files/folders (e.g. `.git`, `requirements.txt`, etc.), but it can also be overriden easily if needed. ...

Example:
```python
import rootpath

def bar():
    path = rootpath.detect()

    assert path == '/home/me/projects/py-foo'

    print('---')
    print('FILE:', file)
    print('ROOT:', path)
    print('---')

if name == 'main':
    bar()
```

Sections: `rootpath`, Introduction, Use: Basic, Use: Painless Python module imports, About

</details>

### pyobjc-framework-AppTrackingTransparency

Wrappers for the framework AppTrackingTransparency on macOS

`pip install pyobjc-framework-AppTrackingTransparency` · installs (wheel) · licence: MIT · rank 11900 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AppTrackingTransparency/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AppTrackingTransparency" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyopenxlsx

Python bindings for OpenXLSX-NX using nanobind

`pip install pyopenxlsx` · installs (wheel) · licence: BSD License · rank 11907 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pyopenxlsx/) · [source](https://github.com/twn39/pyopenxlsx)

<details><summary>README extract</summary>

> [!IMPORTANT]
> `pyopenxlsx` uses OpenXLSX-NX (v1.0.0+), a specialized C++ fork that includes critical performance optimizations and functional enhancements (such as agile encryption, streaming I/O, vector shapes, threaded comments, and custom properties) not currently available in the upstream repository. ...

Features:
1. C++ Foundation: Core operations happen in highly optimized C++. Recent updates eliminated `shared_ptr` heap allocations and deep copies for zero-allocation performance during high-throughput tasks.
2. ...

Example:
```python
from pyopenxlsx import Workbook

# Create a new workbook
with Workbook() as wb:
    ws = wb.active
    ws.title = "MySheet"

    # Write data
    ws["A1"].value = "Hello"
    ws["B1"].value = 42
    ws.cell(row=2, column=1).value = 3.14

...

</details>

### pyobjc-framework-MLCompute

Wrappers for the framework MLCompute on macOS

`pip install pyobjc-framework-MLCompute` · installs (wheel) · licence: MIT · rank 11909 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MLCompute/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MLCompute" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-AdServices

Wrappers for the framework AdServices on macOS

`pip install pyobjc-framework-AdServices` · installs (wheel) · licence: MIT · rank 11911 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-AdServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "AdServices" framework on macOS 11.1 or later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-KernelManagement

Wrappers for the framework KernelManagement on macOS

`pip install pyobjc-framework-KernelManagement` · installs (wheel) · licence: MIT · rank 11915 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-KernelManagement/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "KernelManagement" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-UserNotificationsUI

Wrappers for the framework UserNotificationsUI on macOS

`pip install pyobjc-framework-UserNotificationsUI` · installs (wheel) · licence: MIT · rank 11916 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-UserNotificationsUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "UserNotificationsUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### pyobjc-framework-ScreenTime

Wrappers for the framework ScreenTime on macOS

`pip install pyobjc-framework-ScreenTime` · installs (wheel) · licence: MIT · rank 11917 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ScreenTime/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ScreenTime" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### kink

Dependency injection for python.

`pip install kink` · installs (wheel) · licence: MIT License · rank 11920 · last release 2026-03-19 · [PyPI](https://pypi.org/project/kink/) · [docs](https://github.com/kodemore/kink) · [source](https://github.com/kodemore/kink)

<details><summary>README extract</summary>

Dependency injection container made for python

Features:
- Easy to use interface
- Extensible with custom dependency resolvers
- Automatic dependency injection (Autowiring)
- Lightweight
- Support for async with asyncio

Example:
```python
from kink import di
from os import getenv

di["db_name"] = getenv("DB_NAME")
di["db_password"] = getenv("DB_PASSWORD")
```

Sections: Kink, Features, Pip, Poetry, Why using dependency injection in python?, Short story, Long story, Relying on the global state is evil, Usage, Bootstrapping/Adding services manually, Adding *service* to di container, Adding factorised services to dependency injection, Requesting services from dependency injection container, Removing services from dependency injection container

</details>

### fspath

semantic path names and more

`pip install fspath` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 11931 · last release 2023-06-29 · [PyPI](https://pypi.org/project/fspath/)

_README extract left out: share-alike licence._

### delorean

library for manipulating datetimes with ease and clarity

`pip install delorean` · installs (wheel) · licence: MIT · rank 11932 · last release 2026-08-01 · [PyPI](https://pypi.org/project/delorean/)

<details><summary>README extract</summary>

`Delorean` is a library for clearing up the inconvenient truths that arise dealing with datetimes in Python. Understanding that timing is a delicate enough of a problem `delorean` hopes to provide a cleaner less troublesome solution to shifting, manipulating, and generating `datetimes`. ...

Example:
```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

est = ZoneInfo('US/Eastern')
d = datetime.now(timezone.utc)
d = d.astimezone(est)
return d
```

Sections: Delorean: Time Travel Made Easy, Getting Started

</details>

### pyobjc-framework-DataDetection

Wrappers for the framework DataDetection on macOS

`pip install pyobjc-framework-DataDetection` · installs (wheel) · licence: MIT · rank 11933 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DataDetection/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DataDetection" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-LocalAuthenticationEmbeddedUI

Wrappers for the framework LocalAuthenticationEmbeddedUI on macOS

`pip install pyobjc-framework-LocalAuthenticationEmbeddedUI` · installs (wheel) · licence: MIT · rank 11934 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-LocalAuthenticationEmbeddedUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "LocalAuthenticationEmbeddedUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation ...

</details>

### pyobjc-framework-MailKit

Wrappers for the framework MailKit on macOS

`pip install pyobjc-framework-MailKit` · installs (wheel) · licence: MIT · rank 11935 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MailKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MailKit" framework on macOS.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### django-bootstrap-form

django-bootstrap-form

`pip install django-bootstrap-form` · installs from source (sdist only) · licence: MIT · rank 11946 · last release 2018-03-15 · [PyPI](https://pypi.org/project/django-bootstrap-form/)

### modelsdotdev

An offline models.dev database bundle exposed as a typed Python module.

`pip install modelsdotdev` · installs (wheel) · licence: MIT · rank 11947 · last release 2026-08-18 · [PyPI](https://pypi.org/project/modelsdotdev/)

<details><summary>README extract</summary>

An offline models.dev database bundle exposed as a
Python module.

Example:
```python
from modelsdotdev import get_model_by_id, get_provider_by_name

provider = get_provider_by_name("OpenAI")
model = get_model_by_id("openai:gpt-5.5")

if provider is not None:
    provider_model = provider.get_model_by_id("gpt-5.5")
    provider_models = list(provider.iter_models())
```

</details>

### unflatten

Unflatten dict to dict with nested dict/arrays

`pip install unflatten` · installs (wheel) · licence: BSD License · rank 11949 · last release 2024-09-05 · [PyPI](https://pypi.org/project/unflatten/)

<details><summary>README extract</summary>

This package provides a function which can unpack a flat dictionary
into a structured `dict` with nested sub-dicts and/or sub-lists.

Development takes place on github.
The package is installable from PyPI.

Nested dicts:

Nested list:

Nested lists and dicts, intermixed:

Features:
- Added type annotations.

Example:
```python
>>> from unflatten import unflatten

>>> unflatten({'foo.bar': 'val'})
{'foo': {'bar': 'val'}}
```

Sections: unflatten - convert flat dict to nested dict/array, Description, Synopsis, Notes, See Also, Features, Nits, Packaging

</details>

### friendlywords

Python package to generate random human-readable strings, e.g. project and experiment names

`pip install friendlywords` · installs (wheel) · licence: MIT · rank 11960 · last release 2026-08-02 · [PyPI](https://pypi.org/project/friendlywords/) · [source](https://github.com/the-lay/py-friendly-words)

<details><summary>README extract</summary>

Python package to generate random human-readable strings, e.g. project and experiment names.
The word lists are taken from
glitchdotcom/friendly-words and the package provides
a convenient way to access it, as well as methods to easily generate combinations.

The package is simple, limited, and over-engineered at the same time. ...

Example:
```python
import friendlywords as fw

# generate random string that consists of N words (N > 0)
# if N is 1, the returned word is an object
# if N > 1, the first N-1 words are predicates
fw.generate(1)
>>> 'square'
fw.generate(4)
>>> 'southern florentine rain college'

# generate string that follow a given grammar
...
```

</details>

### django-background-tasks

Database backed asynchronous task queue

`pip install django-background-tasks` · installs (wheel) · licence: BSD License · rank 11966 · last release 2024-08-16 · [PyPI](https://pypi.org/project/django-background-tasks/)

<details><summary>README extract</summary>

=======================

.. image::
 :target:
 :alt: Build Status
.. image::
 :target:
 :alt: Coverage Status
.. image::
 :target:
 :alt: Documentation Status
.. image::
 :target:
 :alt: PyPI

Django Background Task is a database-backed work queue for Django, loosely based around `Ruby's DelayedJob`_ library. ...

Sections: Django Background Tasks, Docs

</details>

### pyobjc-framework-PHASE

Wrappers for the framework PHASE on macOS

`pip install pyobjc-framework-PHASE` · installs (wheel) · licence: MIT · rank 11968 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-PHASE/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "PHASE" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### rel

Registered Event Listener. Provides standard (pyevent) interface and functionality without external dependencies

`pip install rel` · installs (wheel) · licence: MIT License · rank 11976 · last release 2026-07-05 · [PyPI](https://pypi.org/project/rel/)

<details><summary>README extract</summary>

Registered Event Listener (rel) is a cross-platform asynchronous event dispatcher primarily designed for network applications. Select your preferred event notification methods with initialize([methods in order of preference]). If initialize(...) is not called, methods are tried in the default order: epoll, kqueue, poll, select, pyevent. ...

</details>

### pyobjc-framework-ThreadNetwork

Wrappers for the framework ThreadNetwork on macOS

`pip install pyobjc-framework-ThreadNetwork` · installs (wheel) · licence: MIT · rank 11978 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-ThreadNetwork/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "ThreadNetwork" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### urduhack

Natural Language Processing (NLP) library for Urdu language.

`pip install urduhack` · installs (wheel) · licence: MIT License · rank 11982 · last release 2020-07-06 · [PyPI](https://pypi.org/project/urduhack/) · [docs](https://urduhack.readthedocs.io/en/stable/) · [source](https://github.com/urduhack/urduhack)

<details><summary>README extract</summary>

Urduhack is a NLP library for urdu language. It comes with a lot of battery included features to help you process Urdu
data in the easiest way possible.

Our Goal

- Academic users Easier experimentation to prove their hypothesis without coding from scratch.
- NLP beginners Learn how to build an NLP project with production level code quality. ...

Example:
```python
import urduhack

# Downloading models
urduhack.download()

nlp = urduhack.Pipeline()
text = ""
doc = nlp(text)

for sentence in doc.sentences:
    print(sentence.text)
    for word in sentence.words:
        print(f"{word.text}\t{word.pos}")

    for token in sentence.tokens:
        print(f"{token.text}\t{token.ner}")
```

</details>

### deepagents-acp

Agent Client Protocol integration for Deep Agents

`pip install deepagents-acp` · installs (wheel) · licence: MIT License · rank 12000 · last release 2026-10-12 · [PyPI](https://pypi.org/project/deepagents-acp/) · [docs](https://reference.langchain.com/python/deepagents/) · [source](https://github.com/langchain-ai/deepagents)

<details><summary>README extract</summary>

This directory contains an Agent Client Protocol (ACP) connector that allows you to run a Python Deep Agent within a text editor that supports ACP such as Zed.

It includes an example coding agent that uses Anthropic's Claude models to write code with its built-in filesystem tools and shell, but you can also connect any Deep Agent with additional ...

Example:
```python
from deepagents_acp.server import AgentServerACP, AgentSessionContext

# Define available models
models = [
    {"value": "anthropic:claude-opus-5", "name": "Claude Opus 5"},
    {"value": "anthropic:claude-sonnet-5", "name": "Claude Sonnet 5"},
    {"value": "openai:gpt-6-astra", "name": "GPT-6 Astra"},
]

...
```

...

</details>

### bioutils

miscellaneous simple bioinformatics utilities and lookup tables

`pip install bioutils` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 12003 · last release 2026-10-14 · [PyPI](https://pypi.org/project/bioutils/) · [docs](https://biocommons.github.io/bioutils/) · [source](https://github.com/biocommons/bioutils)

<details><summary>README extract</summary>

Package Description

This project is a product of the biocommons community.

- Github repository: <
- Documentation <

Sections: bioutils, MacOS or Linux Systems, Linux (Debian-based systems)

</details>

### django-easy-audit

Yet another Django audit log app, hopefully the simplest one.

`pip install django-easy-audit` · installs (wheel) · licence: GNU General Public License v3 (GPLv3); Other/Proprietary License · rank 12010 · last release 2026-06-30 · [PyPI](https://pypi.org/project/django-easy-audit/) · [docs](https://github.com/soynatan/django-easy-audit/wiki) · [source](https://github.com/soynatan/django-easy-audit)

_README extract left out: share-alike licence._

### gitignorefile

A spec-compliant `.gitignore` parser for Python

`pip install gitignorefile` · installs from source (sdist only) · licence: MIT License · rank 12016 · last release 2022-09-04 · [PyPI](https://pypi.org/project/gitignorefile/) · [docs](https://github.com/excitoon/gitignorefile/blob/master/README.md) · [source](https://github.com/excitoon/gitignorefile)

<details><summary>README extract</summary>

A spec-compliant `.gitignore` parser for Python.

Example:
```python
import gitignorefile

matches = gitignorefile.parse("/home/michael/project/.gitignore")
matches("/home/michael/project/main.py") # False
matches("/home/michael/project/main.pyc") # True
matches("/home/michael/project/dir/main.pyc") # True
matches("/home/michael/project/pycache") # True
```

Sections: `gitignorefile`, Usage, `gitignorefile.parse()`, `gitignorefile.ignore()`, `gitignorefile.ignored()`, `gitignorefile.Cache`, Custom ignore file sources

</details>

### html2docx

Convert valid HTML input to docx.

`pip install html2docx` · installs (wheel) · licence: MIT License · rank 12023 · last release 2023-01-19 · [PyPI](https://pypi.org/project/html2docx/)

<details><summary>README extract</summary>

html2docx converts valid HTML input to docx output. The project is distributed
under the MIT license.

Example:
```python
from html2docx import html2docx

with open("my.html") as fp:
    html = fp.read()

# html2docx() returns an io.BytesIO() object. The HTML must be valid.
buf = html2docx(html, title="My Document")

with open("my.docx", "wb") as fp:
    fp.write(buf.getvalue())
```

Sections: html2docx, Usage

</details>

### pysphere

Python API for interacting with the vSphere Web Services SDK

`pip install pysphere` · does not install on CPython 3.14 · licence: BSD License · rank 12025 · last release ? · [PyPI](https://pypi.org/project/pysphere/)

<details><summary>README extract</summary>

Visit the project site for more information.

Among other operations, PySphere provides easy interfaces to:

- Connect to VMWare's ESX, ESXi, Virtual Center, Virtual Server hosts
- Query hosts, datacenters, resource pools, virtual machines
- VMs: Power on, power off, reset, revert to snapshot, get properties, update
 vmware tools, clone, migrate. ...

Sections: PySphere, Quick Example, Discussion Group

</details>

### flashgeotext

Extract and count countries and cities (+their synonyms) from text

`pip install flashgeotext` · installs (wheel) · licence: MIT License · rank 12029 · last release 2025-01-21 · [PyPI](https://pypi.org/project/flashgeotext/) · [source](https://github.com/iwpnd/flashgeotext)

<details><summary>README extract</summary>

Extract and count countries and cities (+their synonyms) from text, like GeoText on steroids using FlashText, a Aho-Corasick implementation. Flashgeotext is a fast, batteries-included (and BYOD) and native python library that extracts one or more sets of given city and country names (+ synonyms) from an input text.

introductory blogpost:

Example:
```python
from flashgeotext.geotext import GeoText

geotext = GeoText()

input_text = '''Shanghai. The Chinese Ministry of Finance in Shanghai said that China plans
                to cut tariffs on $75 billion worth of goods that the country
                imports from the US. Washington welcomes the decision.'''

geotext.extract(input_text=input_text)
...
```

...

</details>

### pyobjc-framework-Cinematic

Wrappers for the framework Cinematic on macOS

`pip install pyobjc-framework-Cinematic` · installs (wheel) · licence: MIT · rank 12030 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Cinematic/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Cinematic" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-Symbols

Wrappers for the framework Symbols on macOS

`pip install pyobjc-framework-Symbols` · installs (wheel) · licence: MIT · rank 12037 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Symbols/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Symbols" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-SensitiveContentAnalysis

Wrappers for the framework SensitiveContentAnalysis on macOS

`pip install pyobjc-framework-SensitiveContentAnalysis` · installs (wheel) · licence: MIT · rank 12038 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SensitiveContentAnalysis/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SensitiveContentAnalysis" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### terraform-compliance

BDD test framework for terraform

`pip install terraform-compliance` · installs (wheel) · licence: MIT License · rank 12067 · last release 2026-10-22 · [PyPI](https://pypi.org/project/terraform-compliance/)

### python-freeipa

Lightweight FreeIPA client

`pip install python-freeipa` · installs (wheel) · licence: MIT License · rank 12083 · last release 2025-09-26 · [PyPI](https://pypi.org/project/python-freeipa/) · [docs](https://python-freeipa.readthedocs.io/)

<details><summary>README extract</summary>

python-freeipa is lightweight FreeIPA client.
API documentation:

</details>

### pycups

Python bindings for libcups

`pip install pycups` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 12098 · last release 2024-04-18 · [PyPI](https://pypi.org/project/pycups/)

_README extract left out: share-alike licence._

### yaml-rs

A High-Performance YAML Parser for Python written in Rust

`pip install yaml-rs` · installs (wheel) · licence: Unlicense · rank 12102 · last release 2026-07-07 · [PyPI](https://pypi.org/project/yaml-rs/) · [source](https://github.com/lava-sh/yaml-rs)

<details><summary>README extract</summary>

*A High-Performance YAML v1.2 parser for Python written in Rust*

Features:
* The fastest YAML parser in Python (see benchmarks)
* Full YAML v1.2 spec support

Example:
```python
from pprint import pprint

import yaml_rs

yaml = """\
app:
  name: service
  environment: production
  debug: false
  version: 1.3.5

  log:
    level: INFO
    file: /var/log/service/app.log
    rotation:
      enabled: true
      max_size_mb: 50

  database:
    engine: mariadb
    host: localhost
    port: 3306
    username: app_user
...
```

Sections: yaml-rs, Features, Playground, Example, Comparison with other YAML parsing libraries, YAML 1.1-oriented libraries, PyYAML, oyaml, ryaml, YAML 1.2-oriented libraries, ruamel.yaml, strictyaml

</details>

### gelidum

Freeze your objects in python

`pip install gelidum` · installs (wheel) · licence: MIT License · rank 12112 · last release 2026-01-23 · [PyPI](https://pypi.org/project/gelidum/) · [docs](https://github.com/diegojromerolopez/gelidum/blob/main/README.md) · [source](https://github.com/diegojromerolopez/gelidum)

<details><summary>README extract</summary>

Freeze your objects in python.

Public domain photo by Katsujiro Maekawa

| Latin | English |

| *Caelum est hieme frigidum et gelidum; myrtos oleas quaeque alia assiduo tepore laetantur, aspernatur ac respuit; laurum tamen patitur atque etiam nitidissimam profert, interdum sed non saepius quam sub urbe nostra necat.* | *In winter the air is cold ...

Example:
```python
from typing import List
from gelidum import freeze

class Dummy(object):
  def init(self, attr1: int, attr2: List):
    self.attr1 = attr1
    self.attr2 = attr2

dummy = Dummy(1, [2, 3, 4])
# on_freeze='copy' by default
frozen_dummy = freeze(dummy)
assert(id(dummy) != id(frozen_dummy))

# on_freeze='copy' by default
...
```

...

</details>

### flake8-formatter-junit-xml

JUnit XML Formatter for flake8

`pip install flake8-formatter-junit-xml` · installs (wheel) · licence: MIT License · rank 12129 · last release 2018-04-11 · [PyPI](https://pypi.org/project/flake8-formatter-junit-xml/)

<details><summary>README extract</summary>

JUnit XML Formatter for flake8.

Sections: flake8-formatter-junit-xml, Usage

</details>

### sshkeyboard

sshkeyboard

`pip install sshkeyboard` · installs (wheel) · licence: MIT License · rank 12143 · last release 2021-10-28 · [PyPI](https://pypi.org/project/sshkeyboard/)

<details><summary>README extract</summary>

The only keyboard event callback library that works _everywhere_, even when
used through an SSH connection
(hence the name).

It works with headless computers and servers, or for example inside Windows
Subsystem for Linux (WSL 2). One good use case is controlling Raspberry Pi
based robots or RC cars through SSH. ...

Example:
```python
from sshkeyboard import listen_keyboard

def press(key):
    print(f"'{key}' pressed")

def release(key):
    print(f"'{key}' released")

listen_keyboard(
    on_press=press,
    on_release=release,
)
```

...

</details>

### ensure

Literate BDD assertions in Python with no magic

`pip install ensure` · installs (wheel) · licence: Apache Software License · rank 12161 · last release 2023-12-10 · [PyPI](https://pypi.org/project/ensure/)

<details><summary>README extract</summary>

*ensure* is a set of simple assertion helpers that let you write more expressive, literate, concise, and readable
Pythonic code for validating conditions. It's inspired by should.js,
expect.js, and builds on top of the
unittest/JUnit assert helpers. ...

Example:
```python
ensure({1: {2: 3}}).is_not_equal_to({1: {2: 4}})
ensure(True).does_not_equal(False)
ensure(1).is_in(range(10))
ensure(True).is_a(bool)
ensure(True).is(True)
ensure(True).is_not(False)
```

Sections: ensure: Literate assertions in Python, Synopsis, Notes, Raising custom exceptions, More examples, Enforcing function annotations, Motivation and goals, Links, Bugs

</details>

### punq

An IOC Container for Python 3.10+

`pip install punq` · installs (wheel) · licence: not stated · rank 12162 · last release 2026-09-08 · [PyPI](https://pypi.org/project/punq/) · [docs](https://bobthemighty.github.io/punq/) · [source](https://github.com/bobthemighty/punq)

<details><summary>README extract</summary>

<!-- quick_start -->

An unintrusive library for dependency injection in modern Python.
Inspired by Funq, Punq is a dependency injection library you can understand.

- No global state
- No decorators
- No weird syntax applied to arguments
- Supports type checking with strict modes of `mypy`, `pyright`, and `pyrefly` ...

Example:
```python
import punq

container = punq.Container()
```

Sections: Punq, Quick Start

</details>

### rnet

A blazing-fast Python HTTP client with TLS fingerprint

`pip install rnet` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12210 · last release 2025-08-02 · [PyPI](https://pypi.org/project/rnet/) · [docs](https://github.com/0x676e67/rnet/blob/main/rnet.pyi) · [source](https://github.com/0x676e67/rnet)

_README extract left out: share-alike licence._

### vocode-api

(no summary)

`pip install vocode-api` · installs (wheel) · licence: not stated · rank 12215 · last release 2024-08-27 · [PyPI](https://pypi.org/project/vocode-api/)

<details><summary>README extract</summary>

API documentation is available at here.

Example:
```python
from vocode.client import Vocode

vocode_client = Vocode(
  token="YOUR_API_KEY"
)

action_response = vocode_client.actions.get_action(
  id="action_id"
);

print(action_response)
```

Sections: Vocode Python Library, Documentation, Usage, Async Client, Timeouts, Handling Exceptions

</details>

### argparse-ext

argparse extension;

`pip install argparse-ext` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 12231 · last release 2021-12-25 · [PyPI](https://pypi.org/project/argparse-ext/) · [source](https://github.com/cykerway/argparse-ext/)

_README extract left out: share-alike licence._

### consolekit

Additional utilities for click.

`pip install consolekit` · installs (wheel) · licence: MIT License · rank 12248 · last release 2026-07-28 · [PyPI](https://pypi.org/project/consolekit/) · [docs](https://consolekit.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/consolekit)

### pyprobables

Probabilistic data structures in python

`pip install pyprobables` · installs (wheel) · licence: MIT · rank 12251 · last release 2026-02-08 · [PyPI](https://pypi.org/project/pyprobables/) · [docs](https://pyprobables.readthedocs.io/)

<details><summary>README extract</summary>

pyprobables is a pure-python library for probabilistic data structures.
The goal is to provide the developer with a pure-python implementation of
common probabilistic data-structures to use in their work.

To achieve better raw performance, it is recommended supplying an alternative
hashing algorithm that has been compiled in C. ...

Example:
```python
from probables import BloomFilter
blm = BloomFilter(est_elements=1000, false_positive_rate=0.05)
blm.add('google.com')
blm.check('facebook.com')  # should return False
blm.check('google.com')  # should return True
```

...

</details>

### ecsapi

A simple SDK for manage Seeweb ecs api

`pip install ecsapi` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 12258 · last release 2025-09-25 · [PyPI](https://pypi.org/project/ecsapi/)

<details><summary>README extract</summary>

A simple SDK for manage Seeweb ecs api

Sections: ecsapi_client, Required for production

</details>

### shippinglabel

Utilities for handling packages.

`pip install shippinglabel` · installs (wheel) · licence: MIT License · rank 12264 · last release 2025-05-08 · [PyPI](https://pypi.org/project/shippinglabel/) · [docs](https://shippinglabel.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/shippinglabel)

### flask-pydantic-spec

generate OpenAPI document and validate request & response with Python annotations.

`pip install flask-pydantic-spec` · installs (wheel) · licence: not stated · rank 12271 · last release 2025-11-25 · [PyPI](https://pypi.org/project/flask-pydantic-spec/)

<details><summary>README extract</summary>

A library to make it easy to add OpenAPI documentation to your Flask app, and validate the requests using Pydantic.

This library began as a fork of Spectree, but as we made changes we thought
other people might be interested in our approach.

Features:
* Less boilerplate code, only annotations, no need for YAML :sparkles:
* Generate API document with Redoc UI or Swagger UI :yum:
* Validate query, JSON data, response data with pydantic :wink:
* Has support for request/response types other than JSON.

Example:
```python
from flask_pydantic_spec import FlaskPydanticSpec
FlaskPydanticSpec("flask", title="Demo API", version="v1.0", path="doc")
```

Sections: Flask Pydantic Spec [][version-link] [][workflow-link], Features, Quick Start, Examples, Step by Step, How To, Demo, Flask, FAQ

</details>

### handy-archives

Some handy archive helpers for Python.

`pip install handy-archives` · installs (wheel) · licence: MIT License · rank 12280 · last release 2026-08-26 · [PyPI](https://pypi.org/project/handy-archives/) · [docs](https://handy-archives.readthedocs.io/en/latest) · [source](https://github.com/domdfcoding/handy-archives)

### dist-meta

Parse and create Python distribution metadata.

`pip install dist-meta` · installs (wheel) · licence: MIT License · rank 12282 · last release 2025-02-12 · [PyPI](https://pypi.org/project/dist-meta/) · [docs](https://dist-meta.readthedocs.io/en/latest) · [source](https://github.com/repo-helper/dist-meta)

<details><summary>README extract</summary>

Parse and create Python distribution metadata.

</details>

### jsl

A Python DSL for defining JSON schemas

`pip install jsl` · installs from source (sdist only) · licence: BSD License · rank 12291 · last release 2016-05-11 · [PyPI](https://pypi.org/project/jsl/)

<details><summary>README extract</summary>

Documentation PyPI

JSL is a Python DSL for defining JSON Schemas.

Example:
```python
import jsl

class Entry(jsl.Document):
    name = jsl.StringField(required=True)

class File(Entry):
    content = jsl.StringField(required=True)

class Directory(Entry):
    content = jsl.ArrayField(jsl.OneOfField([
        jsl.DocumentField(File, as_ref=True),
        jsl.DocumentField(jsl.RECURSIVE_REFERENCE_CONSTANT)
    ]), required=True)
```

Sections: JSL, Example

</details>

### intel-pti

Intel® Profiling Tools Interface

`pip install intel-pti` · installs (wheel) · licence: Other/Proprietary License · rank 12295 · last release 2026-11-02 · [PyPI](https://pypi.org/project/intel-pti/)

<details><summary>README extract</summary>

Framework for developing profiling tools for applications built on top of oneAPI and running on Intel XPUs.

</details>

### fastapi-route-logger-middleware

Simple middleware for FastAPI to generate log entries on all requests

`pip install fastapi-route-logger-middleware` · installs (wheel) · licence: MIT License · rank 12302 · last release 2021-12-31 · [PyPI](https://pypi.org/project/fastapi-route-logger-middleware/)

<details><summary>README extract</summary>

Basic middleware to log requests made to routes in FastAPI applications.

Sections: fastapi-route-logger, Usage

</details>

### dagster-ray

Dagster integration library for Ray

`pip install dagster-ray` · installs (wheel) · licence: Apache Software License · rank 12317 · last release 2026-10-22 · [PyPI](https://pypi.org/project/dagster-ray/) · [docs](https://danielgafni.github.io/dagster-ray/) · [source](https://github.com/danielgafni/dagster-ray)

<details><summary>README extract</summary>

Ray integration for Dagster.

`dagster-ray` enables working with distributed Ray compute from Dagster pipelines, combining Dagster's excellent orchestration capabilities and Ray's distributed computing power together.

> [!NOTE]
> This project is ready for production use, but some APIs may change between minor releases.

Learn more in the docs ...

Sections: `dagster-ray`, 🚀 Key Features, 📚 Docs, 👥 Who is using `dagster-ray`?

</details>

### pyleri

Python Left-Right Parser

`pip install pyleri` · installs (wheel) · licence: MIT License · rank 12342 · last release 2026-07-06 · [PyPI](https://pypi.org/project/pyleri/)

<details><summary>README extract</summary>

Pyleri is an easy-to-use parser created for SiriDB. We first used lrparsing and wrote jsleri for auto-completion and suggestions in our web console. Later we found small issues within the `lrparsing` module and also had difficulties keeping the language the same in all projects. ...

Example:
```python
# Imports, note that we skip the imports in other examples...
from pyleri import (
    Grammar,
    Keyword,
    Regex,
    Sequence)

# Create a Grammar Class to define your language
class MyGrammar(Grammar):
    r_name = Regex('(?:"(?:[^"]*)")+')
    k_hi = Keyword('hi')
    START = Sequence(k_hi, r_name)

...
```

Sections: Python Left-Right Parser, Related projects, Quick usage, Grammar, parse, export_js, export_c, export_go, export_java, export_py, Result, is_valid, Position, Tree

</details>

### django-nested-inline

Recursive nesting of inline forms for Django Admin

`pip install django-nested-inline` · installs (wheel) · licence: MIT License · rank 12367 · last release 2023-03-14 · [PyPI](https://pypi.org/project/django-nested-inline/)

<details><summary>README extract</summary>

Nested inline support for Django admin

Most of the code from this package is from

Github

Installation

pip install django-nested-inline

Usage

Add `nested_inline` to `INSTALLED_APPS`

Minifying Javascript

Released versions of this library should have a minified version of the js.

Minification is done with uglifyjs. ...

Example:
```python
# models.py

from django.db import models

class TopLevel(models.Model):
    name = models.CharField(max_length=200)

class LevelOne(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey('TopLevel')

class LevelTwo(models.Model):
    name = models.CharField(max_length=200)
...
```

</details>

### graphql-core-promise

Add support for promise-based dataloaders and resolvers to graphql-core v3+

`pip install graphql-core-promise` · installs (wheel) · licence: BSD License · rank 12368 · last release 2026-11-03 · [PyPI](https://pypi.org/project/graphql-core-promise/) · [source](https://github.com/fellowapp/graphql-core-promise)

<details><summary>README extract</summary>

[][main CI]
[][package]
[][package]

Add support for promise-based dataloaders and resolvers to graphql-core v3+. This aims to make migrating to graphene 3 and graphql-core 3 easier for existing projects.

Example:
```python
from graphql_core_promise import PromiseExecutionContext
from graphql.execution.execute import execute

execute(schema=..., document=..., execution_context_class=PromiseExecutionContext)
```

Sections: graphql-core-promise, Usage, graphql-core 3.2, graphql-core 3.3, With Django (graphql-core 3.2), Versioning and compatibility, How it works

</details>

### scaleapi

The official Python client library for Scale AI, the Data Platform for AI

`pip install scaleapi` · installs (wheel) · licence: MIT License · rank 12377 · last release 2026-04-24 · [PyPI](https://pypi.org/project/scaleapi/)

<details><summary>README extract</summary>

If you use earlier versions of the SDK, please refer to v1.0.4 documentation.

If you are migrating from earlier versions to v2, please refer to Migration Guide to v2.

Installation
____

Install with PyPI (pip)

or install with Anaconda (conda)

Usage ...

Example:
```python
import scaleapi

client = scaleapi.ScaleClient("YOUR_API_KEY_HERE")
```

Sections: Scale AI | Python SDK, Create Task, Retrieve a task, Task Attributes, Retrieve List of Tasks, Get Tasks Count, Cancel Task, Audit a Task, Update A Task's Unique Id, Clear A Task's Unique Id, Set A Task's Metadata, Set A Task's Tags, Add Tags to A Task, Delete Tags from A Task

</details>

### rsloop

An event loop for asyncio written in Rust

`pip install rsloop` · installs (wheel) · licence: Apache Software License · rank 12405 · last release 2026-10-19 · [PyPI](https://pypi.org/project/rsloop/) · [source](https://github.com/RustedBytes/rsloop)

<details><summary>README extract</summary>

`rsloop` is a PyO3-based `asyncio` event loop implemented in Rust.

Each `rsloop.Loop` owns a dedicated Rust runtime thread for loop coordination
and I/O work. That thread runs an rsloop-specialized `vibeio` runtime, using
io_uring on Linux, IOCP on Windows, and native kqueue readiness on macOS. ...

Example:
```python
import rsloop

async def main() -> str:
    return "done"

print(rsloop.run(main()))
```

Sections: An event loop for asyncio written in Rust, Documentation, Usage, Examples, Benchmarks

</details>

### aws-glue-schema-registry

Use the AWS Glue Schema Registry.

`pip install aws-glue-schema-registry` · installs (wheel) · licence: Apache Software License · rank 12417 · last release 2023-10-17 · [PyPI](https://pypi.org/project/aws-glue-schema-registry/) · [source](https://github.com/DisasterAWARE/aws-glue-schema-registry-python)

<details><summary>README extract</summary>

Use the AWS Glue Schema Registry in Python projects.

This library is a partial port of aws-glue-schema-registry which implements a subset of its features with full compatibility.

Features:
Feature | Java Library | Python Library | Notes

Serialization and deserialization using schema registry | ✔️ | ✔️
Avro message format | ✔️ | ✔️
JSON Schema message format | ✔️ | ✔️
Kafka Streams support | ✔️ | | N/A for Python, Kafka Streams is ...

Example:
```python
import boto3

# Pass your AWS credentials or profile information here
session = boto3.Session(access_key_id=xxx, secret_access_key=xxx, region_name='us-west-2')

glue_client = session.client('glue')
```

Sections: AWS Glue Schema Registry for Python, Usage, Linting, Tests, Tox

</details>

### pyobjc-framework-Carbon

Wrappers for the framework Carbon on macOS

`pip install pyobjc-framework-Carbon` · installs (wheel) · licence: MIT · rank 12421 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Carbon/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Carbon" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### eventsourcing

Event sourcing in Python

`pip install eventsourcing` · installs (wheel) · licence: BSD License · rank 12422 · last release 2026-10-13 · [PyPI](https://pypi.org/project/eventsourcing/) · [docs](https://eventsourcing.readthedocs.io/) · [source](https://github.com/pyeventsourcing/eventsourcing)

<details><summary>README extract</summary>

This project is a comprehensive Python library for implementing event sourcing, a design pattern where all
changes to application state are stored as a sequence of events. This library provides a solid foundation
for building event-sourced applications in Python, with a focus on reliability, performance, and developer
experience. ...

Features:
Flexible event store — flexible persistence of domain events. Combines
an event mapper and an event recorder in ways that can be easily extended. ...

Example:
```python
from eventsourcing.domain import Aggregate, event

class Dog(Aggregate):
    @event('Registered')
    def init(self, name: str) -> None:
        self.name = name
        self.tricks: list[str] = []

    @event('TrickAdded')
    def add_trick(self, trick: str) -> None:
...

</details>

### pyads

Python wrapper for TwinCAT ADS library

`pip install pyads` · installs (wheel) · licence: MIT · rank 12457 · last release 2026-06-16 · [PyPI](https://pypi.org/project/pyads/) · [docs](https://pyads.readthedocs.io) · [source](https://github.com/stlehmann/pyads)

<details><summary>README extract</summary>

This is a python wrapper for TwinCATs ADS library. It provides python functions
for communicating with TwinCAT devices. *pyads* uses the C API provided by *TcAdsDll.dll* on Windows *AdsLib.so* on Linux. The documentation for the ADS API is available on infosys.beckhoff.com.

Documentation: ...

Features:
- connect to a remote TwinCAT device like a plc or a PC with TwinCAT
- create routes on Linux devices and on remote plcs
- supports TwinCAT 2 and TwinCAT 3
- read and write values by name or address
- read and write DUTs (structures) from the plc ...

Example:
```python
import pyads

# connect to plc and open connection
plc = pyads.Connection('127.0.0.1.1.1', pyads.PORT_TC3PLC1)
plc.open()

# read int value by name
i = plc.read_by_name("GVL.int_val")

# write int value by name
...

</details>

### yamlpath

Command-line get/set/merge/validate/scan/convert/diff processors for YAML/JSON/Compatible data using powerful, intuitive, command-line friendly syntax

`pip install yamlpath` · installs (wheel) · licence: ISC License (ISCL) · rank 12458 · last release 2026-05-02 · [PyPI](https://pypi.org/project/yamlpath/)

<details><summary>README extract</summary>

Along with providing a
standard for defining YAML Paths,
this project aims to provide
generally-useful command-line tools
which implement YAML Paths. These bring intuitive YAML, EYAML, JSON, and
compatible data parsing and editing capabilties to the command-line. It is
also a
Python library
for other projects to readily employ YAML Paths.

Example:
```python
from types import SimpleNamespace

from yamlpath.common import Parsers
from yamlpath.wrappers import ConsolePrinter
from yamlpath import Processor

# The various classes of this library must be able to write messages somewhere
# when things go bad.  This project provides a CLI-centric logging class named
...
```

...

</details>

### pyobjc-framework-InputMethodKit

Wrappers for the framework InputMethodKit on macOS

`pip install pyobjc-framework-InputMethodKit` · installs from source (sdist only) · licence: MIT · rank 12471 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-InputMethodKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "InputMethodKit" framework on macOS 10.5 or later. The
interfaces in this framework allow you to develop input methods.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation ...

</details>

### panphon

Tools for using the International Phonetic Alphabet with phonological features

`pip install panphon` · installs (wheel) · licence: MIT · rank 12474 · last release 2025-06-12 · [PyPI](https://pypi.org/project/panphon/)

<details><summary>README extract</summary>

If you use PanPhon in research, please cite the following paper:

David R. Mortensen, Patrick Littell, Akash Bharadwaj, Kartik Goyal, Chris Dyer, Lori Levin (2016). "PanPhon: A Resource for Mapping IPA Segments to Articulatory Feature Vectors." *Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical ...

Features:
The `Distance` class includes methods for calculating edit distance, both in which the cost of substitutions is based upon Hamming distance between the feature vectors and in which the cost of substitutions are based upon edit weights for individual ...

Example:
```python
>>> import panphon
>>> ft = panphon.FeatureTable()
>>> ft.word_fts(u'swit')
...
```

...

</details>

### onemkl-sycl-blas

Intel® oneAPI Math Kernel Library

`pip install onemkl-sycl-blas` · installs (wheel) · licence: Other/Proprietary License · rank 12482 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-sycl-blas/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### mailosaur

The Mailosaur Python library lets you integrate email and SMS testing into your continuous integration process.

`pip install mailosaur` · installs (wheel) · licence: MIT License · rank 12495 · last release 2026-05-27 · [PyPI](https://pypi.org/project/mailosaur/) · [docs](https://mailosaur.com/docs/email-testing/python/) · [source](https://github.com/mailosaur/mailosaur-python)

<details><summary>README extract</summary>

Mailosaur lets you automate email and SMS tests as part of software development and QA.

- Unlimited test email addresses for all - every account gives users an unlimited number of test email addresses to test with. ...

Example:
```python
from mailosaur import MailosaurClient
mailosaur = MailosaurClient()
```

Sections: Mailosaur - Python library ·, Get Started, Set your API key, Create your code, API Reference, Creating an account, Test email addresses with Mailosaur, Find an email, What is this code doing?, My email wasn't found, Find an SMS message, Extracting verification codes from plain text, How many links?

</details>

### pyowm

A Python wrapper around OpenWeatherMap web APIs

`pip install pyowm` · installs (wheel) · licence: MIT License · rank 12507 · last release 2025-08-26 · [PyPI](https://pypi.org/project/pyowm/)

<details><summary>README extract</summary>

A Python wrapper around OpenWeatherMap web APIs

PyOWM is a client Python wrapper library for OpenWeatherMap (OWM) web APIs. It allows quick and easy consumption of OWM data from Python applications via a simple object model and in a human-friendly fashion.

PyOWM runs on Python 3.9+ ...

Example:
```python
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('your free OWM API key')
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
...
```

Sections: PyOWM, What is it?, What kind of data can I get with PyOWM ?, In case of trouble..., API key, Example, Documentation

</details>

### onemkl-sycl-rng

Intel® oneAPI Math Kernel Library

`pip install onemkl-sycl-rng` · installs (wheel) · licence: Other/Proprietary License · rank 12513 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-sycl-rng/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### kanjize

Easy converter between Kanji-Number and Integer

`pip install kanjize` · installs (wheel) · licence: MIT License · rank 12536 · last release 2025-06-14 · [PyPI](https://pypi.org/project/kanjize/) · [docs](https://github.com/nagataaaas/Kanjize/blob/master/README.md) · [source](https://github.com/nagataaaas/Kanjize.git)

<details><summary>README extract</summary>

Easy converter between Kanji-Number and Integer

Powered by Yamato Nagata

GitHub

Can Convert Number up to 10 ** 72 - 1

Example:
```python
from kanjize import number2kanji, kanji2number, Number, KanjizeConfiguration, KanjizeZero, KanjizeStyle

print(number2kanji(58076099))
# 五千八百七万六千九十九

print(number2kanji(58076099, config=KanjizeConfiguration(use_daiji=True)))
# 伍阡捌佰漆萬陸阡玖拾玖

print(kanji2number("五千八百七万六千九十九"))
# 58076099

print(kanji2number("223兆4千億4256万6千"))
# 223400042566000

...
```

</details>

### pybatfish

Python API and utilities for Batfish

`pip install pybatfish` · installs (wheel) · licence: Apache Software License · rank 12537 · last release 2026-09-18 · [PyPI](https://pypi.org/project/pybatfish/) · [docs](https://pybatfish.readthedocs.io/en/latest/) · [source](https://github.com/batfish/pybatfish)

<details><summary>README extract</summary>

Got questions, feedback, or feature requests? Join our community on Slack!

Pybatfish is a Python client for Batfish.

Batfish is a network validation tool that provides correctness guarantees for security, reliability, and compliance by analyzing the configuration of network devices. ...

Sections: Pybatfish, What is Batfish?, Configuration Compliance, Reliability, Change Analysis, How do I get started?, Pybatfish documentation

</details>

### pyobjc-framework-MediaExtension

Wrappers for the framework MediaExtension on macOS

`pip install pyobjc-framework-MediaExtension` · installs from source (sdist only) · licence: MIT · rank 12544 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-MediaExtension/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "MediaExtension" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### faker-e164

Faker Provider to generate phone numbers in E164 format.

`pip install faker-e164` · installs from source (sdist only) · licence: Apache Software License · rank 12554 · last release 2017-07-31 · [PyPI](https://pypi.org/project/faker-e164/)

<details><summary>README extract</summary>

`pip install faker-e164`

Example:
```python
from faker import Faker
from faker_e164.providers import E164Provider
fake = Faker()
fake.add_provider(E164Provider)

# To actually fake an e164 phone number
fake.e164()
```

Sections: Faker Provider for E164 Phone Numbers, Usage

</details>

### ffn

Financial functions for Python

`pip install ffn` · installs (wheel) · licence: MIT · rank 12557 · last release 2026-10-10 · [PyPI](https://pypi.org/project/ffn/) · [docs](https://pmorissette.github.io/ffn/) · [source](https://github.com/pmorissette/ffn)

<details><summary>README extract</summary>

If you are looking for a full backtesting framework, please check out bt.
bt is built atop ffn and makes it easy and fast to backtest quantitative strategies.

Features:
ffn is a library that contains many useful functions for those who work in **quantitative
finance**. It stands on the shoulders of giants (Pandas, Numpy, Scipy, etc.) and provides
a vast array of utilities, from performance measurement and ...

Example:
```python
import ffn
returns = ffn.get('aapl,msft,c,gs,ge', provider='yahoo', start='2010-01-01').to_returns().dropna()
print(returns.calc_mean_var_weights().as_format('.2%'))
```

Sections: ffn - Financial Functions for Python, Overview, Documentation

</details>

### prefect-gitlab

A Prefect collection for working with GitLab repositories.

`pip install prefect-gitlab` · installs (wheel) · licence: Apache Software License · rank 12561 · last release 2026-06-12 · [PyPI](https://pypi.org/project/prefect-gitlab/)

### sqlalchemy-citext

A sqlalchemy plugin that allows postgres use of CITEXT.

`pip install sqlalchemy-citext` · installs from source (sdist only) · licence: BSD License · rank 12578 · last release 2021-03-02 · [PyPI](https://pypi.org/project/sqlalchemy-citext/)

<details><summary>README extract</summary>

Example:
```python
from sqlalchemy import create_engine, MetaData, Integer
from sqlalchemy.schema import Column, Table
import sqlalchemy.orm as orm

from citext import CIText

engine = create_engine('postgresql://localhost/test_db')
meta = MetaData()

test_table = Table('test', meta,
    Column('id', Integer(), primary_key=True),
    Column('txt', CIText()))

...
```

</details>

### onemkl-sycl-lapack

Intel® oneAPI Math Kernel Library

`pip install onemkl-sycl-lapack` · installs (wheel) · licence: Other/Proprietary License · rank 12591 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-sycl-lapack/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### mozprofile

Library to create and modify Mozilla application profiles

`pip install mozprofile` · installs from source (sdist only) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12602 · last release 2024-04-26 · [PyPI](https://pypi.org/project/mozprofile/)

### django-redis-cache

Redis Cache Backend for Django

`pip install django-redis-cache` · installs from source (sdist only) · licence: BSD License · rank 12604 · last release 2022-03-09 · [PyPI](https://pypi.org/project/django-redis-cache/)

### onemkl-sycl-dft

Intel® oneAPI Math Kernel Library

`pip install onemkl-sycl-dft` · installs (wheel) · licence: Other/Proprietary License · rank 12610 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-sycl-dft/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### fastapi-cprofile

A FastAPI Middleware with cProfile to stats your service performance.

`pip install fastapi-cprofile` · installs (wheel) · licence: MIT License · rank 12612 · last release 2020-12-29 · [PyPI](https://pypi.org/project/fastapi-cprofile/)

<details><summary>README extract</summary>

A FastAPI Middleware with cProfile to help stats your service performance.
cProfile is a built-in python module that can perform profiling. It is the most commonly used profiler currently.

Features:
- [x] support custom cprofile param

Example:
```python
from fastapi_cprofile.profiler import CProfileMiddleware

app = FastAPI()
app.add_middleware(CProfileMiddleware)
```

Sections: fastapi-cprofile, Features, Code Sample

</details>

### deepagents-azure-blob-backend

Deprecated — use langchain-azure-storage[deepagents]. Azure Blob Storage filesystem backend for LangChain Deep Agents

`pip install deepagents-azure-blob-backend` · installs (wheel) · licence: MIT · rank 12616 · last release 2026-10-01 · [PyPI](https://pypi.org/project/deepagents-azure-blob-backend/) · [docs](https://oddrationale.github.io/deepagents-azure-blob-backend) · [source](https://github.com/oddrationale/deepagents-azure-blob-backend)

<details><summary>README extract</summary>

> [!WARNING]
> This package is deprecated and no longer maintained.
> Its Azure Blob Storage backend now ships first-party in `langchain-azure-storage`, maintained by LangChain and Microsoft in langchain-ai/langchain-azure:
> ```bash
> pip install "langchain-azure-storage[deepagents]"
> ```
> The constructor API changed during upstream review, so ...

Example:
```python
import asyncio
from deepagents import create_deep_agent
from deepagents_azure_blob_backend import AzureBlobBackend, AzureBlobConfig

async def main():
    config = AzureBlobConfig(
        account_url="
        container_name="agent-workspace",
        prefix="session-001/",
    )
    backend = AzureBlobBackend(config)

...
```

...

</details>

### onemkl-sycl-sparse

Intel® oneAPI Math Kernel Library

`pip install onemkl-sycl-sparse` · installs (wheel) · licence: Other/Proprietary License · rank 12623 · last release 2026-10-16 · [PyPI](https://pypi.org/project/onemkl-sycl-sparse/)

<details><summary>README extract</summary>

Intel® oneAPI Math Kernel Library (Intel® oneMKL) is a computing math library of highly optimized, extensively threaded routines for applications that require maximum performance. This package provides C and Data Parallel C++ (DPC++) programming language interfaces. ...

</details>

### tdl-xoa-driver

TDL XOA Python API is a Python library providing user-friendly communication interfaces to Teledyne LeCroy Xena Ethernet traffic generation test equipment. It provides a rich collection of APIs that can be used to either write test scripts or develop applications.

`pip install tdl-xoa-driver` · installs (wheel) · licence: Apache Software License · rank 12625 · last release 2026-09-28 · [PyPI](https://pypi.org/project/tdl-xoa-driver/)

<details><summary>README extract</summary>

TDL XOA Python API is a standalone Python library that provides a user-friendly and powerful interface for automating network testing tasks using Xena Networks test equipment. Xena test equipment is a high-performance network test device designed for testing and measuring the performance of network equipment and applications. ...

Features:
* Objected-oriented, high-level abstraction, to help users save time on parsing command responses.
* Supporting sending commands in batches to increase code execution efficiency. ...

Sections: TDL XOA Python API, Introduction, Documentation, Key Features

</details>

### taxcalc

Tax-Calculator

`pip install taxcalc` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 12641 · last release 2026-10-30 · [PyPI](https://pypi.org/project/taxcalc/)

<details><summary>README extract</summary>

| | |

| Org | |
| Package | |
| Testing | |

Tax-Calculator is an open-source microsimulation model for static and
conventional analysis of USA federal income and payroll taxes.

We are seeking contributors and maintainers. ...

</details>

### OleFileIO_PL

Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office) - Improved version of the OleFileIO module from PIL, the Python Image Library.

`pip install OleFileIO_PL` · installs from source (sdist only) · licence: BSD License · rank 12681 · last release 2015-01-25 · [PyPI](https://pypi.org/project/OleFileIO_PL/)

<details><summary>README extract</summary>

olefile is a Python package to
parse, read and write Microsoft OLE2
files (also
called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents,
vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix
files, Outlook messages, StickyNotes, several Microscopy file ...

Features:
- Parse, read and write any OLE file such as Microsoft Office 97-2003
 legacy document formats (Word .doc, Excel .xls, PowerPoint .ppt,
 Visio .vsd, Project .mpp), Image Composer and FlashPix files, Outlook
 messages, StickyNotes, Zeiss AxioVision ...

Sections: olefile (formerly OleFileIO\_PL), News, Features, Documentation, Real-life examples

</details>

### bai2

BAI2 Parser

`pip install bai2` · installs (wheel) · licence: MIT License · rank 12685 · last release 2025-11-04 · [PyPI](https://pypi.org/project/bai2/)

<details><summary>README extract</summary>

Python module for parsing and writing BAI2 files.

The library is not production ready at the moment as we don't have enough data to test against, please help us improve it.

Only tested on Python 3.10+, but should work on 3.7+.

Example:
```python
from bai2 import bai2

# parse from a file
with open(<file-path>) as f:
    bai2_file = bai2.parse_from_file(f)

# parse from a string
bai2_file = bai2.parse_from_string(<bai2_as_string>)

# parse from lines
bai2_file = bai2.parse_from_lines(<bai2_as_lines>)
```

Sections: bai2, Requirements, Usage, Models, Exceptions, Incongruences, Copyright

</details>

### ucxx-cu13

Python Bindings for the Unified Communication X library (UCX)

`pip install ucxx-cu13` · installs (wheel) · licence: BSD-3-Clause · rank 12705 · last release 2026-10-08 · [PyPI](https://pypi.org/project/ucxx-cu13/)

<details><summary>README extract</summary>

UCXX is an object-oriented C++ interface for UCX, with native support for Python bindings.

Before starting it is necessary to have the necessary dependencies installed. The simplest way to get started is to install Miniforge and then to create and activate an environment with the provided development file, for CUDA 13.x: ...

Sections: UCXX, Building, Environment setup, Faster conda dependency resolution, Convenience Script, C++, Python, Running benchmarks, Basic Usage, Synchronous, Asynchronous, Logging

</details>

### libucxx-cu13

Python Bindings for the Unified Communication X library (UCX)

`pip install libucxx-cu13` · installs (wheel) · licence: BSD-3-Clause · rank 12712 · last release 2026-10-08 · [PyPI](https://pypi.org/project/libucxx-cu13/)

<details><summary>README extract</summary>

UCXX is an object-oriented C++ interface for UCX, with native support for Python bindings.

Before starting it is necessary to have the necessary dependencies installed. The simplest way to get started is to install Miniforge and then to create and activate an environment with the provided development file, for CUDA 13.x: ...

Sections: UCXX, Building, Environment setup, Faster conda dependency resolution, Convenience Script, C++, Python, Running benchmarks, Basic Usage, Synchronous, Asynchronous, Logging

</details>

### pyobjc-framework-Collaboration

Wrappers for the framework Collaboration on macOS

`pip install pyobjc-framework-Collaboration` · installs (wheel) · licence: MIT · rank 12714 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-Collaboration/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "Collaboration" framework in macOS 10.5 or later. The
Collaboration framework provides access to identities, and manages
user interface elements for selecting identities. ...

</details>

### pyobjc-framework-DictionaryServices

Wrappers for the framework DictionaryServices on macOS

`pip install pyobjc-framework-DictionaryServices` · installs (wheel) · licence: MIT · rank 12715 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DictionaryServices/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Deprecated wrappers for the "DictionaryServices" framework on macOS 10.5 or later.

Use package "CoreServices" instead.

* Documentation

* Issue Tracker

* Repository

</details>

### pyobjc-framework-InstantMessage

Wrappers for the framework InstantMessage on macOS

`pip install pyobjc-framework-InstantMessage` · installs (wheel) · licence: MIT · rank 12718 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-InstantMessage/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for "InstantMessage" framework on macOS 10.5 or later. This framework
allows you to access iChat information, as well as a way to provide an
auxiliary video source to iChat Theater. ...

</details>

### apischema

JSON (de)serialization, GraphQL and JSON schema generation using Python typing.

`pip install apischema` · installs (wheel) · licence: MIT License · rank 12739 · last release 2024-10-01 · [PyPI](https://pypi.org/project/apischema/) · [docs](https://wyfo.github.io/apischema) · [source](https://github.com/wyfo/apischema)

<details><summary>README extract</summary>

JSON (de)serialization, GraphQL and JSON schema generation using Python typing.

*apischema* makes your life easier when dealing with API data.

Features:
(If you wonder how this differs from the *pydantic* library, see the dedicated section of the documentation — there are many differences.)

This library fulfills the following goals: ...

Example:
```python
from collections.abc import Collection
from dataclasses import dataclass, field
from uuid import UUID, uuid4

import pytest
from graphql import print_schema

from apischema import ValidationError, deserialize, serialize
from apischema.graphql import graphql_schema
from apischema.json_schema import deserialization_schema

...
```

Sections: apischema, Documentation, Why another library?, Example, Run the documentation examples

</details>

### PyTrie

A pure Python implementation of the trie data structure.

`pip install PyTrie` · installs (wheel) · licence: BSD License · rank 12746 · last release 2024-03-09 · [PyPI](https://pypi.org/project/PyTrie/)

<details><summary>README extract</summary>

`pytrie` is a a pure Python 3 implementation of the trie data structure.

A _trie_ is an ordered tree data structure that is used to store a mapping
where the keys are sequences, usually strings over an alphabet. ...

Sections: pytrie, 0.4.0, 0.3.1, 0.3, 0.2, 0.1

</details>

### stcrestclient

stcrestclient: Client modules for STC ReST API

`pip install stcrestclient` · installs (wheel) · licence: MIT License · rank 12747 · last release 2026-11-03 · [PyPI](https://pypi.org/project/stcrestclient/)

<details><summary>README extract</summary>

The stcrestclient package provides the `stchttp` ReST API library module. This allows simple function calls, nearly identical to those provided by `StcPython.py`, to be used to access TestCenter server sessions via the STC ReST API. ...

Example:
```python
>>> from stcrestclient import stchttp
>>> # Choose ONE of the following connection methods:
>>> # HTTP (default)
>>> stc = stchttp.StcHttp('stcserver.somewhere.com', timeout=10)
>>> # OR
>>> # HTTPS
>>> stc = stchttp.StcHttp('stcserver.somewhere.com', use_https=True, ca_cert="/path/to/server_cert.pem", timeout=10)
>>>
...
```

...

</details>

### environ

Stack Based Globals Management

`pip install environ` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 12751 · last release 2007-08-06 · [PyPI](https://pypi.org/project/environ/)

_README extract left out: share-alike licence._

### FormEncode

"HTML form validation, generation, and conversion package"

`pip install FormEncode` · installs (wheel) · licence: MIT License · rank 12761 · last release 2025-01-31 · [PyPI](https://pypi.org/project/FormEncode/)

<details><summary>README extract</summary>

FormEncode is a validation and form generation package.
The validation can be used separately from the form generation.
The validation works on compound data structures, with all parts being nestable.
It is separate from HTTP or any other input mechanism.

The latest documentation is available at

Sections: FormEncode, Introduction, Documentation, Changes

</details>

### chompjs

Parsing JavaScript objects into Python dictionaries

`pip install chompjs` · installs (wheel) · licence: MIT License · rank 12763 · last release 2026-05-17 · [PyPI](https://pypi.org/project/chompjs/)

<details><summary>README extract</summary>

Transforms JavaScript objects into Python data structures.

In web scraping, you sometimes need to transform Javascript objects embedded in HTML pages into valid Python dictionaries. `chompjs` is a library designed to do that as a more powerful replacement of standard `json.loads`:

Reference documentation

Features:
There are two functions available:
* `parse_js_object` - try reading first encountered JSON-like object. Raises `ValueError` on failure
* `parse_js_objects` - returns a generator yielding all encountered JSON-like objects. ...

Example:
```python
>>> chompjs.parse_js_object("{a: 100}")
{'a': 100}
>>>
>>> json_lines = """
... {'a': 12}
... {'b': 13}
... {'c': 14}
... """
>>> for entry in chompjs.parse_js_objects(json_lines):
...     print(entry)
...
{'a': 12}
{'b': 13}
...

</details>

### pyobjc-framework-CalendarStore

Wrappers for the framework CalendarStore on macOS

`pip install pyobjc-framework-CalendarStore` · installs (wheel) · licence: MIT · rank 12772 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-CalendarStore/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "CalendarStore" on macOS 10.5 and later. The CalendarStore
frameworks provides access to the iCal data. It's possible to fetch iCal
records, such as calendars and tasks, as well as modify them and get
notifications when records change in iCal. ...

</details>

### pyobjc-framework-DeviceDiscoveryExtension

Wrappers for the framework DeviceDiscoveryExtension on macOS

`pip install pyobjc-framework-DeviceDiscoveryExtension` · installs (wheel) · licence: MIT · rank 12773 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-DeviceDiscoveryExtension/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "DeviceDiscoveryExtension" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker ...

</details>

### opcua

Pure Python OPC-UA client and server library

`pip install opcua` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 12784 · last release 2021-03-03 · [PyPI](https://pypi.org/project/opcua/)

_README extract left out: share-alike licence._

### enry-python

Python bindings for go-enry language detector

`pip install enry-python` · installs (wheel) · licence: Apache-2.0 · rank 12800 · last release 2026-10-01 · [PyPI](https://pypi.org/project/enry-python/) · [docs](https://github.com/Esoiya/go-enry/tree/master/python) · [source](https://github.com/Esoiya/go-enry)

<details><summary>README extract</summary>

Python bindings through cFFI (ABI, out-of-line) for calling enry Go functions exposed by CGo wrapper.

The editable install builds the Go shared library and CFFI bindings automatically.
Build requirements and runtime dependencies come from `pyproject.toml`.

Features:
Historically, the Python package shipped a static library and used CFFI API mode (a compiled extension that links against `libenry`).
That approach relied on Go-generated headers/types (e.g. ...

Example:
```python
import enry

# Detect language by filename and content
language = enry.get_language("example.py", b"print('Hello, world!')")
print(f"Detected language: {language}")
```

...

</details>

### PySDL2

Python SDL2 bindings

`pip install PySDL2` · installs (wheel) · licence: zlib/libpng License; Public Domain · rank 12822 · last release 2024-12-30 · [PyPI](https://pypi.org/project/PySDL2/)

<details><summary>README extract</summary>

PySDL2 is a pure Python wrapper around the SDL2, SDL2\_mixer, SDL2\_image,
SDL2\_ttf, and SDL2\_gfx libraries.
Instead of relying on C code, it uses the built-in ctypes module to interface
with SDL2, and provides simple Python classes and wrappers for common
SDL2 functionality.

Sections: PySDL2, Requirements, Documentation

</details>

### dataclasses-jsonschema

JSON schema generation from dataclasses

`pip install dataclasses-jsonschema` · installs (wheel) · licence: MIT License · rank 12833 · last release 2022-10-27 · [PyPI](https://pypi.org/project/dataclasses-jsonschema/)

<details><summary>README extract</summary>

Please Note: This project is in maintenance mode. I'm currently only making urgent bugfixes.

A library to generate JSON Schema from python 3.7 dataclasses. Python 3.6 is supported through the dataclasses backport. Aims to be a more lightweight alternative to similar projects such as marshmallow & pydantic.

Features:
* Support for draft-04, draft-06, Swagger 2.0 & OpenAPI 3 schema types
* Serialisation and deserialisation
* Data validation against the generated schema

Example:
```python
from dataclasses import dataclass

from dataclasses_jsonschema import JsonSchemaMixin

@dataclass
class Point(JsonSchemaMixin):
    "A 2D point"
    x: float
    y: float
```

...

</details>

### flask-restplus

Fully featured framework for fast, easy and documented API development with Flask

`pip install flask-restplus` · installs (wheel) · licence: BSD License · rank 12840 · last release 2019-08-12 · [PyPI](https://pypi.org/project/flask-restplus/)

<details><summary>README extract</summary>

Flask-RESTPlus is an extension for Flask that adds support for quickly building REST APIs.
Flask-RESTPlus encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTPlus should be easy to pick up. ...

Example:
```python
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(name)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
...
```

...

</details>

### py-ballisticcalc.exts

LGPL library for small arms ballistic calculations (Python 3)

`pip install py-ballisticcalc.exts` · installs (wheel) · licence: not stated · rank 12847 · last release 2026-10-16 · [PyPI](https://pypi.org/project/py-ballisticcalc.exts/) · [source](https://github.com/o-murphy/py-ballisticcalc)

<details><summary>README extract</summary>

The compiled extensions include `cython+dopri`, a Dormand--Prince
5(4) adaptive engine with SciPy RK45-style controller semantics. The existing
Cash--Karp engine remains available with its compatibility controller.

LGPL library for small arms ballistic calculations based on point-mass (3 DoF) plus spin drift. ...

Sections: BallisticCalculator, pip, QuickStart, Examples, Ballistic Concepts, Units, Calculation Engines, About project, RISK NOTICE

</details>

### snowpark-connect-deps-2

Supporting JAR dependencies for Snowpark Connect (Part 2)

`pip install snowpark-connect-deps-2` · does not install on CPython 3.14 · licence: Apache Software License · rank 12853 · last release 2026-08-17 · [PyPI](https://pypi.org/project/snowpark-connect-deps-2/)

<details><summary>README extract</summary>

Supporting library JAR files for Snowpark Connect. This package contains Scala, Jackson, Commons, and other dependency JARs.

</details>

### facebook-wda

Python Client for Facebook WebDriverAgent

`pip install facebook-wda` · installs (wheel) · licence: MIT · rank 12855 · last release 2025-09-03 · [PyPI](https://pypi.org/project/facebook-wda/)

### snowpark-connect-deps-1

Spark JAR dependencies for Snowpark Connect (Part 1)

`pip install snowpark-connect-deps-1` · does not install on CPython 3.14 · licence: Apache Software License · rank 12856 · last release 2026-08-17 · [PyPI](https://pypi.org/project/snowpark-connect-deps-1/)

<details><summary>README extract</summary>

Spark framework JAR files for Snowpark Connect. This package contains Apache Spark 3.5.6 core components.

</details>

### assemblyline-v4-service

Assemblyline 4 - Service base

`pip install assemblyline-v4-service` · installs (wheel) · licence: MIT · rank 12859 · last release 2026-11-05 · [PyPI](https://pypi.org/project/assemblyline-v4-service/) · [source](https://github.com/CybercentreCanada/assemblyline-v4-service/)

<details><summary>README extract</summary>

This repository provides the base service functionality for Assemblyline 4 services.

| Tag Type | Description | Example Tag |

| latest | The most recent build (can be unstable). | `latest` |
| build_type | The type of build used. `dev` is the latest unstable build. `stable` is the latest stable build. ...

Sections: Assemblyline 4 - Service Base, Image variants and tags, Creating a new Assemblyline service, Documentation, Créer un nouveau service Assemblyline, Variantes et étiquettes d'image

</details>

### mdformat-gfm-alerts

Format 'GitHub Markdown Alerts,' which use blockquotes to render admonitions

`pip install mdformat-gfm-alerts` · installs (wheel) · licence: MIT · rank 12860 · last release 2026-07-26 · [PyPI](https://pypi.org/project/mdformat-gfm-alerts/)

<details><summary>README extract</summary>

[][ci-link] [][pypi-link]

An mdformat plugin for GFM Alerts. For the JS markdown-it equivalent, see antfu/markdown-it-github-alerts

By default, this package targets the alert syntax GitHub itself renders: `[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, and `[!CAUTION]` alone on their own line, per GitHub's alerts spec. ...

Example:
```python
from markdown_it import MarkdownIt

from mdformat_gfm_alerts.mdit_plugins import gfm_alerts_plugin

md = MarkdownIt()
md.use(gfm_alerts_plugin)  # pass custom_title=True to preserve inline custom titles

text = """
> [!WARNING]
> This is the warning text
"""
md.render(text)

# Warning

# This is the warning text
```

Sections: mdformat-gfm-alerts, Scope, Configuration, `mdformat` Usage, pre-commit / prek, uvx, HTML Rendering

</details>

### agentex-sdk

Agent Development Kit (ADK) overlay for the Agentex API — FastACP server, Temporal workflows, LLM provider integrations, observability

`pip install agentex-sdk` · installs (wheel) · licence: Apache-2.0 · rank 12884 · last release 2026-11-02 · [PyPI](https://pypi.org/project/agentex-sdk/) · [source](https://github.com/scaleapi/scale-agentex-python)

<details><summary>README extract</summary>

The Agent Development Kit (ADK) overlay for the Agentex API.

This package ships everything under `agentex.lib.*`:

- ACP server (`agentex.lib.sdk.fastacp`) — FastAPI-based agent control plane.
- Temporal workflows (`agentex.lib.core.temporal`) — durable agent execution.
- CLI (`agentex.lib.cli`) — `agentex init`, `agentex run`, deploy helpers. ...

Example:
```python
from agentex.lib.core.temporal.logging import make_workflow_logger

logger = make_workflow_logger(name)
```

Sections: agentex-sdk, What's in here, When to use this vs `agentex-client`, Workflow logging, Repo layout

</details>

### taskflow

Taskflow structured state management library.

`pip install taskflow` · installs (wheel) · licence: Apache-2.0 · rank 12887 · last release 2026-10-07 · [PyPI](https://pypi.org/project/taskflow/) · [source](https://opendev.org/openstack/taskflow)

<details><summary>README extract</summary>

A library to do [jobs, tasks, flows] in a highly available, easy to understand
and declarative manner (and more!) to be used with OpenStack and other
projects.

* Free software: Apache license

</details>

### sageattention

Accurate and efficient 8-bit plug-and-play attention.

`pip install sageattention` · installs (wheel) · licence: BSD License · rank 12896 · last release 2024-11-20 · [PyPI](https://pypi.org/project/sageattention/)

<details><summary>README extract</summary>

This repository provides the official implementation of SageAttention.

SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration
Paper:
Jintao Zhang, Jia Wei, Haofeng Huang, Pengle Zhang, Jun Zhu, Jianfei Chen ...

Example:
```python
from sageattention import sageattn
attn_output = sageattn(q, k, v, tensor_layout="HND", is_causal=False, smooth_k=True)
```

Sections: SageAttention, Project Updates, Base environment, How to use, Plug-and-play Example, Performance, Speed of Kernels, End-to-end performance

</details>

### pyobjc-framework-FSKit

Wrappers for the framework FSKit on macOS

`pip install pyobjc-framework-FSKit` · installs from source (sdist only) · licence: MIT · rank 12919 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-FSKit/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "FSKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### pyembroidery

Embroidery IO library

`pip install pyembroidery` · installs (wheel) · licence: MIT License · rank 12934 · last release 2024-03-27 · [PyPI](https://pypi.org/project/pyembroidery/)

<details><summary>README extract</summary>

Python library for the reading and writing of embroidery files.

Compatible with Python 3. Python 2 support was dropped at end-of-life 1-1-2020.

To install:

Any suggestions or comments please raise an issue on the github.

pyembroidery was coded from the ground up with all projects in mind. ...

Features:
Readers are sent a fileobject/stream, an EmbPattern and sometimes a settings dict. The reader parses the file, adding in metadata, threads, and stitches with as much valid information as the file contains. ...

Example:
```python
import pyembroidery
```

Sections: pyembroidery, Mandate, Philosophy, Overview, EmbPattern, EmbPattern Stitches, EmbPattern Threadlist, EmbPattern Extras, Thread Changes, File I/O, Embroidery Formats, Related Formats, Utility Formats, Versions

</details>

### trame-router

Vue Router widgets for trame

`pip install trame-router` · installs (wheel) · licence: MIT License · rank 12955 · last release 2026-09-16 · [PyPI](https://pypi.org/project/trame-router/)

<details><summary>README extract</summary>

Trame-router extend trame widgets and ui with Vue Router components and helper to streamline its usage with trame.
Vue Router is the official router for Vue.js on which trame is based.

Example:
```python
# [...]
from trame.ui.router import RouterViewLayout
from trame.widgets import router

with RouterViewLayout(server, "/"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is home")

with RouterViewLayout(server, "/foo"):
    with vuetify.VCard():
        vuetify.VCardTitle("This is foo")

with RouterViewLayout(server, "/bar/:id"):
...
```

Sections: trame-router enable multi-page navigation, Usage, Environment variables, Enjoying trame?, JavaScript dependency

</details>

### zeroentropy

The official Python library for the ZeroEntropy API

`pip install zeroentropy` · installs (wheel) · licence: Apache Software License · rank 12967 · last release 2026-03-03 · [PyPI](https://pypi.org/project/zeroentropy/) · [source](https://github.com/zeroentropy-ai/zeroentropy-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The ZeroEntropy Python SDK provides convenient type-safe access to the ZeroEntropy REST API from any Python 3.9+ application.

In order to get an API Key, you can visit our dashboard.

The REST API documentation can be found on docs.zeroentropy.dev. An introduction to how ZeroEntropy's API works can be found here. ...

Example:
```python
import os
from zeroentropy import ZeroEntropy

client = ZeroEntropy(
    api_key=os.environ.get("ZEROENTROPY_API_KEY"),  # This is the default and can be omitted
)

response = client.documents.add(
    collection_name="example_collection",
    content={
        "type": "text",
        "text": "Example Content",
    },
    path="my_document.txt",
)
...
```

...

</details>

### privata

A Python module privacy checker for keeping public interfaces intentional.

`pip install privata` · installs (wheel) · licence: MIT · rank 12974 · last release 2026-07-25 · [PyPI](https://pypi.org/project/privata/) · [docs](http://privata.nijho.lt/) · [source](https://github.com/basnijholt/privata)

<details><summary>README extract</summary>

Find Python code that looks public but is only used privately.

Privata is a static checker for keeping module boundaries intentional.
It scans your production Python modules and reports five kinds of interface drift:

- public top-level functions, classes, variables, and type aliases that are only used inside their own module ...

Example:
```python
# src/example/service.py
def helper() -> int:
    return 1

def run() -> int:
    return helper()
```

Sections: Privata, Example, Usage, What Privata Checks, Methods

</details>

### bytestruct

Declarative binary records and composable codecs, using only the standard library

`pip install bytestruct` · installs (wheel) · licence: MIT · rank 12975 · last release 2026-10-18 · [PyPI](https://pypi.org/project/bytestruct/) · [docs](https://doronz88.github.io/bytestruct/)

<details><summary>README extract</summary>

`bytestruct` parses and builds binary wire formats with the standard library alone. Fixed-size records are
dataclasses whose field annotations give each field's wire type; variable-length data is described by small
codecs that compose like construct's. Everything is fully typed. ...

Example:
```python
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Annotated

from bytestruct import BinaryStruct, Const, PaddedString, u16, u32

class Kind(IntEnum):
    FILE = 1
    DIRECTORY = 2

@dataclass
class Header(BinaryStruct, byte_order="<"):
...
```

Sections: bytestruct, Fixed-size records, Codecs, Errors, Performance

</details>

### cvprac

Arista Cloudvision(R) Portal Rest API Client written in python

`pip install cvprac` · installs (wheel) · licence: BSD License · rank 12976 · last release 2026-09-10 · [PyPI](https://pypi.org/project/cvprac/)

<details><summary>README extract</summary>

Features:
This module provides a RESTful API client for Cloudvision® Portal (CVP)
which can be used for building applications that work with Arista CVP.

When the class is instantiated the logging is configured. ...

Sections: Arista Cloudvision® Portal RESTful API Client, Overview, Requirements, Step 1: Clone the cvprac Github repo, Step 2: Check out the desired version or branch, Getting Started, Connecting, CVP On Premises, CVaaS, CVP Version Handling, CVP 2025.2.X+, Examples, Notes for API Class Usage, Containers

</details>

### adf-lib

A Python library for creating and manipulating ADF (Atlassian Document Format) documents

`pip install adf-lib` · installs (wheel) · licence: MIT License · rank 12992 · last release 2026-09-04 · [PyPI](https://pypi.org/project/adf-lib/) · [docs](https://github.com/lakmal98/adf-lib)

<details><summary>README extract</summary>

ADF Library is a Python package for creating and exporting Atlassian Document Format (ADF) content for Jira, Confluence, and other Atlassian Cloud products.

Features:
The library provides:

- high-level helpers for headings, paragraphs, tables, and links
- generic `Node` and `Mark` builders for the latest published ADF node and mark types
- plain Python dictionaries that can be sent directly to Atlassian APIs

Example:
```python
from adf_lib import ADF, Link, Mark, Node, NodeType, Table, Text
from adf_lib.constants.enums import HeadingLevel

doc = ADF()
doc.add(Text("My Document").heading(HeadingLevel.H1))
doc.add(Text("This is a formatted paragraph", "strong", "em").paragraph())

link = Link(href=" title="Example")
...
```

...

</details>

### pyeventsystem

An event driven middleware library for Python

`pip install pyeventsystem` · installs (wheel) · licence: MIT License · rank 12999 · last release 2019-02-18 · [PyPI](https://pypi.org/project/pyeventsystem/)

<details><summary>README extract</summary>

.. image::
 :target:
 :alt: build status

.. image::
 :target:
 :alt: coverage status

pyeventsystem is an event-driven middleware library for Python. In addition to
providing a mechanism for subscribing and listening to events, it also provides
a mechanism for intercepting functions, thus making it suitable for writing
middleware. ...

Sections: pyeventsystem, Simple Example

</details>

### graphene-federation

Federation implementation for graphene

`pip install graphene-federation` · installs (wheel) · licence: MIT · rank 13007 · last release 2025-10-09 · [PyPI](https://pypi.org/project/graphene-federation/)

<details><summary>README extract</summary>

Federation support for Graphene following the Apollo Federation specifications.

[][pypi-url]
[][unit-tests-url]
[][coveralls-url]
[][integration-tests-url]

This repository is heavily based on the repo it was forked from... Huge thanks to Preply for setting up the foundations. ...

Example:
```python
from graphene import Field, Int, ObjectType, String

from graphene_federation import LATEST_VERSION, build_schema, key

@key("id")
class User(ObjectType):
    id = Int(required=True)
    username = String(required=True)

    def __resolve_reference(self, info, **kwargs):
        """
...
```

...

</details>

### flake8-executable

A Flake8 plugin for checking executable permissions and shebangs.

`pip install flake8-executable` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 13016 · last release 2023-01-23 · [PyPI](https://pypi.org/project/flake8-executable/)

_README extract left out: share-alike licence._

### humanreadable

humanreadable is a Python library to convert human-readable values to other units.

`pip install humanreadable` · installs (wheel) · licence: MIT License · rank 13027 · last release 2026-05-09 · [PyPI](https://pypi.org/project/humanreadable/) · [source](https://github.com/thombashi/humanreadable)

<details><summary>README extract</summary>

humanreadable is a Python library to convert human-readable values to other units.

Sections: Summary, Usage, Convert a human-readable value to another unit, Convert a value to a human readable string, Set default unit, Units, Dependencies

</details>

### wuji-sdk

Wuji SDK: Python package for automatic device discovery and real-time data streaming with Wuji devices.

`pip install wuji-sdk` · installs (wheel) · licence: not stated · rank 13031 · last release 2026-10-26 · [PyPI](https://pypi.org/project/wuji-sdk/)

<details><summary>README extract</summary>

Python SDK for Wuji series devices. Provides automatic device discovery, connection management, and real-time data streaming for Wuji Glove, Wuji Hand 2, and other Wuji peripherals. ...

Example:
```python
import time
from wuji_sdk import SdkManager, DeviceType

manager = SdkManager.instance()
# scan() reports each device's type, so connect only the glove.
gloves = [d for d in manager.scan() if d.device_type == DeviceType.WujiGlove]
if not gloves:
    print("No Wuji Glove found")
    exit()
...
```

Sections: wuji-sdk (Python), Quick Start, Examples, Wuji Hand 2 Motion Examples, Choose Example 6 or 7, Run Example 7, Run Example 6, Cleanup Behavior, Retargeting

</details>

### dronecan

Python implementation of the DroneCAN protocol stack

`pip install dronecan` · installs (wheel) · licence: MIT License · rank 13034 · last release 2025-10-29 · [PyPI](https://pypi.org/project/dronecan/)

### simple-rest-client

Simple REST client for python 3.8+

`pip install simple-rest-client` · installs (wheel) · licence: not stated · rank 13053 · last release 2023-10-03 · [PyPI](https://pypi.org/project/simple-rest-client/)

<details><summary>README extract</summary>

Simple REST client for python 3.8+.

Sections: Simple Rest Client, Documentation, Projects using

</details>

### datadiff

DataDiff is a library to provide human-readable diffs of python data structures.

`pip install datadiff` · installs (wheel) · licence: Apache Software License · rank 13079 · last release 2023-08-27 · [PyPI](https://pypi.org/project/datadiff/)

<details><summary>README extract</summary>

DataDiff is a library to provide human-readable diffs of python data structures.
It can handle sequence types (lists, tuples, etc), sets, and dictionaries.

Dictionaries and sequences will be diffed recursively, when applicable.

It has special-case handling for multi-line strings, showing them as a typical unified diff. ...

Example:
```python
>>> from datadiff import diff
>>> a = dict(foo=1, bar=2, baz=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
>>> b = dict(foo=1, bar=4, baz=[0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> print diff(a, b)
--- a
+++ b
{
-'bar': 2,
+'bar': 4,
 'baz': [
 @@ -5,11 +5,8 @@
  6,
  7,
  8,
 -9,
 -10,
 -11,
 ],
 'foo': 1,
}
>>>
>>> from datadiff.tools import assert_equal
...
```

Sections: DataDiff, Example

</details>

### django4-background-tasks

Database backed asynchronous task queue

`pip install django4-background-tasks` · installs from source (sdist only) · licence: BSD License · rank 13096 · last release 2024-06-25 · [PyPI](https://pypi.org/project/django4-background-tasks/)

<details><summary>README extract</summary>

Django Background Task is a database-backed work queue for Django, loosely based around Ruby's DelayedJob library. This project was adopted and adapted from lilspikey `django-background-task`.

To avoid conflicts on PyPI we renamed it to django4-background-tasks. ...

Sections: Django 4 Background Tasks, Docs

</details>

### attrs-strict

Runtime validators for attrs

`pip install attrs-strict` · installs (wheel) · licence: Apache Software License · rank 13103 · last release 2023-08-14 · [PyPI](https://pypi.org/project/attrs-strict/) · [docs](https://github.com/bloomberg/attrs-strict/blob/main/README.md#attrs-runtime-validation) · [source](https://github.com/bloomberg/attrs-strict)

<details><summary>README extract</summary>

`attrs-strict` is a Python package which contains runtime validation for
`attrs` data classes based on the types existing in the typing module.

The purpose of the library is to provide runtime validation for attributes specified in
`attrs` data classes. ...

Example:
```python
from typing import List
import attr
from attrs_strict import type_validator

@attr.s
class SomeClass(object):
    list_of_numbers = attr.ib(validator=type_validator(), type=List[int])

sc = SomeClass([1, 2, 3, 4])
print(sc)
SomeClass(list_of_numbers=[1, 2, 3, 4])

try:
    SomeClass([1, 2, 3, "four"])
except ValueError as exception:
...
```

Sections: attrs runtime validation, Rationale, Quick Start, Building

</details>

### boxdetect

boxdetect is a Python package based on OpenCV which allows you to easily detect rectangular shapes like characters boxes on scanned forms.

`pip install boxdetect` · installs (wheel) · licence: MIT License · rank 13113 · last release 2023-01-18 · [PyPI](https://pypi.org/project/boxdetect/)

<details><summary>README extract</summary>

Share:

BoxDetect is a Python package based on OpenCV which allows you to easily detect rectangular shapes like character or checkbox boxes on scanned forms.

Main purpose of this library is to provide helpful functions for processing document images like bank forms, applications, etc. ...

Features:
- `boxdetect.pipelines.get_boxes` - basic pipeline for boxes extraction
- `boxdetect.pipelines.get_checkboxes` - pipeline which returns only the checkboxes with simple estimation of the state (checked/unchecked) ...

Example:
```python
from boxdetect import config

file_name = 'form_example1.png'

cfg = config.PipelinesConfig()

# important to adjust these values to match the size of boxes on your image
cfg.width_range = (30,55)
cfg.height_range = (25,40)

...

</details>

### pyc-wheel

Compile all py files in a wheel to pyc files.

`pip install pyc-wheel` · installs (wheel) · licence: MIT · rank 13147 · last release 2026-10-16 · [PyPI](https://pypi.org/project/pyc-wheel/) · [docs](https://karpierz.github.io/pyc_wheel/) · [source](https://github.com/karpierz/pyc_wheel)

<details><summary>README extract</summary>

Compile all py files in a wheel to pyc files.

Features:
is a strict fork of Grant Patten's pycwheel package
with a fixes allowing to work with Python3 or higher and with a code
reformatting and some improvements.

PyPI record.

Documentation.

Sections: pyc_wheel, Overview, Usage

</details>

### dodopayments

The official Python library for the Dodo Payments API

`pip install dodopayments` · installs (wheel) · licence: Apache Software License · rank 13153 · last release 2026-10-28 · [PyPI](https://pypi.org/project/dodopayments/) · [source](https://github.com/dodopayments/dodopayments-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Dodo Payments Python library provides convenient access to the Dodo Payments REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx. ...

Example:
```python
import os
from dodopayments import DodoPayments

client = DodoPayments(
    bearer_token=os.environ.get("DODO_PAYMENTS_API_KEY"),  # This is the default and can be omitted
    # defaults to "live_mode".
    environment="test_mode",
)

checkout_session_response = client.checkout_sessions.create(
    product_cart=[
        {
...
```

...

</details>

### xpinyin

Translate Chinese hanzi to pinyin (拼音) by Python, 汉字转拼音

`pip install xpinyin` · installs (wheel) · licence: MIT License · rank 13158 · last release 2025-06-02 · [PyPI](https://pypi.org/project/xpinyin/)

<details><summary>README extract</summary>

Translate Chinese hanzi to pinyin (拼音) by Python, 汉字转拼音

Example:
```python
>>> from xpinyin import Pinyin
>>> p = Pinyin()
>>> # default splitter is `-`
>>> p.get_pinyin("上海")
'shang-hai'
>>> # show tone marks
>>> p.get_pinyin("上海", tone_marks='marks')
'shàng-hǎi'
>>> p.get_pinyin("上海", tone_marks='numbers')
>>> 'shang4-hai3'
>>> # remove splitter
>>> p.get_pinyin("上海", '')
'shanghai'
>>> # set splitter as whitespace
...
```

Sections: xpinyin, Usage, 0.7.6 - Dec. 21, 2020, 0.7.5 - Dec. 21, 2020, 0.7.4 - Dec. 15, 2020, 0.7.3 - Dec. 14, 2020, 0.7.2 - Dec. 14, 2020, 0.7.0 - Dec. 13, 2020, 0.6.0 - Dec. 11, 2020, 0.5.7 - Jun. 28, 2020, 0.5.6 - Oct. 15, 2018, 0.5.5 - Feb. 28, 2016, 0.5.4 - Dec. 14, 2015, 0.5.3 - Dec. 25, 2014

</details>

### pytoniq-core

TON Blockchain SDK

`pip install pytoniq-core` · installs (wheel) · licence: not stated · rank 13166 · last release 2026-10-03 · [PyPI](https://pypi.org/project/pytoniq-core/)

<details><summary>README extract</summary>

Sections: pytoniq-core, Examples, Structure, boc, crypto, proof, tl, tl-b

</details>

### pyobjc-framework-SecurityUI

Wrappers for the framework SecurityUI on macOS

`pip install pyobjc-framework-SecurityUI` · installs (wheel) · licence: MIT · rank 13167 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pyobjc-framework-SecurityUI/) · [docs](https://pyobjc.readthedocs.io/en/latest/) · [source](https://github.com/ronaldoussoren/pyobjc)

<details><summary>README extract</summary>

Wrappers for the "SecurityUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

* Documentation

* Issue Tracker

* Repository

</details>

### grpc-requests

grpc for Humans. grpc reflection support client

`pip install grpc-requests` · installs (wheel) · licence: Apache License 2.0 · rank 13168 · last release 2025-03-23 · [PyPI](https://pypi.org/project/grpc-requests/)

<details><summary>README extract</summary>

Leverage reflection
to interact with GRPC in a familiar manner for users of the requests library.

Features:
- Create a client easily when connecting to servers implementing grpc reflection
- Still support creating a client from stubs when reflection isn't available
- All unary and stream methods supported
- TLS and compression connections supported ...

Example:
```python
from grpc_requests import Client

metadata = [("authorization", "bearer my.cool.jwt")]
client = Client.get_by_endpoint("cool.servers.arecool:443", ssl=True, metadata=metadata)
```

Sections: grpc_requests, GRPC for Humans, Features, Usage, Compatibility, Protobuf Compatibility, Questions, Comments, Issues?, 0.1.21 - 2025-03-22, Fixed, 0.1.20 - 2024-08-15, Added, 0.1.19 - 2024-07-18

</details>

### pretty-traceback

Human readable stacktraces.

`pip install pretty-traceback` · installs (wheel) · licence: MIT License · rank 13192 · last release 2024-08-17 · [PyPI](https://pypi.org/project/pretty-traceback/)

<details><summary>README extract</summary>

Human readable stacktraces for Python.

Project/Repo:

[][license_ref]
[][pyversions_ref]
[][version_ref]
[][pypi_ref]
[][downloads_ref]

Code Quality/CI:

[][github_build_ref]
[][gitlab_build_ref]
[][mypy_ref]
[][codecov_ref]
[][style_ref]

Features:
Pretty Traceback groups together what belongs together, adds coloring and alignment. All of this makes it easier for you to see patterns and filter out the signal from the noise. This tabular format is best viewed in a wide terminal. ...

Example:
```python
try:
    import pretty_traceback
    pretty_traceback.install()
except ImportError:
    pass    # no need to fail because of missing dev dependency
```

...

</details>

### siphash

siphash - python siphash implementation

`pip install siphash` · installs from source (sdist only) · licence: MIT License · rank 13198 · last release 2013-01-22 · [PyPI](https://pypi.org/project/siphash/)

<details><summary>README extract</summary>

pysiphash

A Python implementation of SipHash, a
fast short-input PRF.

Extract from the description:

SipHash is a family of pseudorandom functions (a.k.a. keyed hash
functions) optimized for speed on short messages.

Target applications include network traffic authentication and defense
against hash-flooding DoS attacks. ...

Sections: usage, speed

</details>

### glog

Simple Google-style logging wrapper for Python.

`pip install glog` · installs (wheel) · licence: BSD License · rank 13200 · last release 2016-12-14 · [PyPI](https://pypi.org/project/glog/)

<details><summary>README extract</summary>

A simple Google-style logging wrapper for Python.

This library attempts to greatly simplify logging in Python applications.
Nobody wants to spend hours pouring over the PEP 282 logger documentation, and
almost nobody actually needs things like loggers that can be reconfigured over
the network. We just want to get on with writing our apps. ...

Example:
```python
import glog as log

log.setLevel("INFO")  # Integer levels are also allowed.
log.info("It works.")
log.warn("Something not ideal")
log.error("Something went wrong")
log.fatal("AAAAAAAAAAAAAAA!")
```

Sections: glog for Python, Core benefits, Behaviours, Example use, Check macros / assert helpers

</details>

### matrx-graph

Channel-based, super-step workflow orchestration engine for the Matrx ecosystem

`pip install matrx-graph` · installs (wheel) · licence: MIT License · rank 13210 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-graph/) · [source](https://github.com/AI-Matrix-Engine/aidream-current)

<details><summary>README extract</summary>

Channel-based, super-step workflow orchestration engine for the Matrx ecosystem. Think of it as a typed DAG + Pregel scheduler designed for mixing deterministic nodes with agent-style nodes in the same graph, with durable checkpoints and optional human-in-the-loop interrupts.

Example:
```python
from matrx_graph import (
    Definition, NodeDef, EdgeDef, EdgeKind,
    compile_graph, Scheduler, register, register_builtin_nodes,
)

register_builtin_nodes()

# A custom action — registered once, referenced by name in node definitions
@register("greet")
async def greet(ctx, inputs, config):
    return {"message": f"Hello, {inputs['name']}!"}

...
```

Sections: matrx-graph, Design pillars, Design principle, Usage sketch, Dependency posture

</details>

### pyrsmi

Python System Management Library for AMD GPUs

`pip install pyrsmi` · installs (wheel) · licence: MIT License · rank 13216 · last release 2025-12-03 · [PyPI](https://pypi.org/project/pyrsmi/) · [source](https://github.com/ROCm/pyrsmi)

<details><summary>README extract</summary>

- `pyrsmi` is a Python package providing system management functionality for AMD GPUs.
- Version 1.0+ uses the new AMD SMI Library (`amdsmi`), replacing the deprecated `rocm-smi-lib`.
- It provides comprehensive monitoring and management capabilities for AMD Instinct™ MI-series GPUs.

- ROCm 6.0 or later with AMD SMI Library (`libamd_smi.so`) ...

Example:
```python
from pyrsmi import rocml

# Initialize the library
rocml.smi_initialize()

# Get device count
num_gpus = rocml.smi_get_device_count()
print(f"Found {num_gpus} GPU(s)")

# Get device information
for i in range(num_gpus):
    name = rocml.smi_get_device_name(i)
    memory = rocml.smi_get_device_memory_total(i) / (1024**3)  # Convert to GB
...
```

...

</details>

### aioclamd

Asynchronous client for virus scanning with ClamAV

`pip install aioclamd` · installs (wheel) · licence: MIT · rank 13224 · last release 2026-09-17 · [PyPI](https://pypi.org/project/aioclamd/) · [source](https://github.com/hbldh/aioclamd)

<details><summary>README extract</summary>

This package is an asynchronous version of the pleasant package
`python-clamd`. It has the same external
API, only all methods are coroutines and all communication is handled
asynchronously using the ``asyncio`` framework.

The `ClamdAsyncClient` connects to a ClamAV antivirus instance and scans
files and data for malicious threats. ...

Example:
```python
import asyncio

from aioclamd import ClamdAsyncClient

async def main(host, port):
    clamd = ClamdAsyncClient(host, port)
    print(await clamd.scan('/etc/clamav/clamd.conf'))

asyncio.run(main("127.0.0.1", 3310))

# Output:
# {'/etc/clamav/clamd.conf': ('OK', None)}
```

Sections: aioclamd, Usage

</details>

### pysigset

Signal blocking under Linux & OS X

`pip install pysigset` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 13225 · last release 2021-05-03 · [PyPI](https://pypi.org/project/pysigset/)

_README extract left out: share-alike licence._

### pyfatfs

FAT12/FAT16/FAT32 implementation with VFAT support

`pip install pyfatfs` · installs (wheel) · licence: MIT License · rank 13230 · last release 2024-03-03 · [PyPI](https://pypi.org/project/pyfatfs/) · [docs](https://pyfatfs.readthedocs.io) · [source](https://github.com/nathanhi/pyfatfs)

<details><summary>README extract</summary>

pyfatfs is a filesystem module for use with PyFilesystem2
for anyone who needs to access or modify files on a FAT filesystem. It also
provides a low-level API that allows direct interaction with a FAT filesystem
without PyFilesystem2 abstraction.

pyfatfs supports FAT12/FAT16/FAT32 as well as the VFAT extension (long file names).

Example:
```python
import fs
my_fs = fs.open_fs("fat:///dev/sda1")
```

Sections: pyfatfs, Usage, PyFilesystem2, Parameters, encoding, offset, preserve_case, read_only, utc, lazy_load

</details>

### dlthub-client

dltHub Runtime client: the dlthub CLI commands, MCP tools and the dlthub_sdk Python SDK

`pip install dlthub-client` · installs (wheel) · licence: Apache-2.0 · rank 13240 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dlthub-client/) · [docs](https://dlthub.com/docs/hub/introduction)

<details><summary>README extract</summary>

`dlthub-client` connects the open source data load tool (dlt) to the dltHub Runtime,
where you deploy, run and monitor pipelines, notebooks and apps. It contains:

- `dlthub` CLI commands: `login`, `deploy`, `run`, `serve`, `job`, `workspace`, `variable`, `dashboard` and more,
 added to the `dlthub` command as a plugin. ...

Example:
```python
import dlthub_sdk

runtime = dlthub_sdk.connect(token="dlt_u...")
ws = runtime.workspaces.get(id="...")

for job in ws.jobs.list():
    print(job.job_ref, job.is_paused)

for result in ws.jobs.trigger(refs=["jobs.my_pipeline"]):
    if result.started:
        run = ws.job_runs.get(id=result.job_run_id).wait()
        print(run.status)
```

Sections: dlthub-client, CLI, MCP tools, Python SDK, Documentation

</details>

### bioc

bioc - Processing BioC, Brat, and PubTator with Python.

`pip install bioc` · installs (wheel) · licence: MIT License · rank 13269 · last release 2023-08-15 · [PyPI](https://pypi.org/project/bioc/)

<details><summary>README extract</summary>

BioC XML / JSON format can be used to
share text documents and annotations.

Brat standoff format is created by the brat annotation tool to store
annotations on disk in a standoff format. annotations are stored separately from the annotated document text, which is
never modified by the tool. ...

Example:
```python
from bioc import biocxml
# Serialize ``collection`` as a BioC formatted stream to ``fp``.
with open(filename, 'w') as fp:
    biocxml.dump(collection, fp)
```

Sections: bioc - Processing BioC, Brat, and PubTator with Python, Getting started, BioC, Brat, PubTator, Documentation, Reference

</details>

### kcidb-io

KCIDB = Linux Kernel CI reporting - I/O data library

`pip install kcidb-io` · installs (wheel) · licence: GPL-2.0-or-later · rank 13294 · last release 2026-04-08 · [PyPI](https://pypi.org/project/kcidb-io/)

_README extract left out: share-alike licence._

### matrx-scheduler

Server-side execution engine for the matrx scheduling spine (sch_* tables): scanner, claim, runner, cron parser, HTTP API.

`pip install matrx-scheduler` · installs (wheel) · licence: MIT License · rank 13296 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-scheduler/)

<details><summary>README extract</summary>

Server-side execution engine for the matrx scheduling spine (`sch*` tables in
Supabase). Provides:

- a scanner loop that claims due tasks atomically,
- a runner that drives the host's agent_runner / tool_runner,
- an authoritative cron parser + next-due computation, ...

Features:
- Polls `sch_task` for rows where `next_due_at <= now()` and the host surface
 is in `surfaces[]` (or `'any'`).
- Atomically claims a candidate by inserting a `sch_run` with `claim_token`
 and `claim_expires_at` (the lease). ...

Example:
```python
from fastapi import FastAPI
import matrx_scheduler

app = FastAPI()

# Host startup wiring (any host).
matrx_scheduler.configure(
    supabase_client=service_role_client,
    surface="server",  # or "desktop", "extension", ...
    agent_runner=my_agent_runner,
...

</details>

### cloudbridge

A simple layer of abstraction over multiple cloud providers.

`pip install cloudbridge` · installs (wheel) · licence: MIT · rank 13309 · last release 2026-09-18 · [PyPI](https://pypi.org/project/cloudbridge/) · [source](https://github.com/CloudVE/cloudbridge)

<details><summary>README extract</summary>

CloudBridge provides a consistent layer of abstraction over different
Infrastructure-as-a-Service cloud providers, reducing or eliminating the need
to write conditional code for each cloud.

Detailed documentation can be found at

Example:
```python
from cloudbridge.factory import CloudProviderFactory, ProviderList

provider = CloudProviderFactory().create_provider(ProviderList.AWS, {})
print(provider.security.key_pairs.list())
```

Sections: Documentation, Usage example, Quick Reference, Design Goals

</details>

### bash

Bash for Python

`pip install bash` · installs from source (sdist only) · licence: GNU Library or Lesser General Public License (LGPL) · rank 13334 · last release 2016-05-30 · [PyPI](https://pypi.org/project/bash/)

_README extract left out: share-alike licence._

### hdx-python-utilities

HDX Python Utilities for streaming tabular data, date and time handling and other helpful functions

`pip install hdx-python-utilities` · installs (wheel) · licence: MIT License · rank 13349 · last release 2026-11-02 · [PyPI](https://pypi.org/project/hdx-python-utilities/)

<details><summary>README extract</summary>

The HDX Python Utilities Library provides a range of helpful utilities for Python developers.
Note that these are not specific to HDX.

1. Easy downloading of files with support for authentication, streaming and hashing
1. Retrieval of data from url with saving to file or from data previously saved
1. Date utilities
1. ...

Sections: Environment, Pre-commit, Packages, Project, Documentation

</details>

### aioredlock

Asyncio implemetation of Redis distributed locks

`pip install aioredlock` · installs (wheel) · licence: MIT License · rank 13350 · last release 2022-02-08 · [PyPI](https://pypi.org/project/aioredlock/)

<details><summary>README extract</summary>

The asyncio redlock algorithm implementation.

The redlock algorithm is a distributed lock implementation for Redis. There are many implementations of it in several languages. In this case, this is the asyncio compatible implementation for python 3.5+.

Example:
```python
from aioredlock import Aioredlock, LockError, Sentinel

# Define a list of connections to your Redis instances:
redis_instances = [
  ('localhost', 6379),
  {'host': 'localhost', 'port': 6379, 'db': 1},
  'redis://localhost:6379/2',
  Sentinel(('localhost', 26379), master='leader', db=3),
...
```

Sections: aioredlock, Redlock and asyncio, Usage, How it works, To-do

</details>

### lazyregistry

A lightweight Python library for lazy-loading registries with namespace support and type safety.

`pip install lazyregistry` · installs (wheel) · licence: MIT License · rank 13355 · last release 2026-02-22 · [PyPI](https://pypi.org/project/lazyregistry/) · [source](https://github.com/milkclouds/lazyregistry)

<details><summary>README extract</summary>

A lightweight Python library for lazy-loading registries with namespace support and type safety

Features:
- Lazy imports - Defer expensive imports until first access
- Instance registration - Register both import strings and direct objects
- Namespaces - Organize multiple registries
- Generic types - Type hints for IDE autocomplete on registry access ...

Example:
```python
from lazyregistry import Registry

registry = Registry(name="plugins")

# Register by import string (lazy - imported on access)
registry["json"] = "json:dumps"

# Register by instance (immediate - already imported)
import pickle
registry["pickle"] = pickle.dumps

# Import happens here
serializer = registry["json"]
```

...

</details>

### random-address

Retrieve real random US addresses, with coordinates, for tests and fixtures

`pip install random-address` · installs (wheel) · licence: MIT · rank 13365 · last release 2026-10-13 · [PyPI](https://pypi.org/project/random-address/) · [source](https://github.com/neosergio/random-address)

<details><summary>README extract</summary>

This is a tool to retrieve a real address from a list of real, random US addresses. It is meant for testing: seeding fixtures, exercising address forms, and giving geolocation code something genuine to work with. ...

Example:
```python
>>> from random_address import real_random_address
>>> real_random_address()
{'address1': '210 Beachcomber Drive', 'address2': '', 'city': 'Pismo Beach', 'state': 'CA',
 'postal_code': '93449', 'coordinates': {'lat': 35.169193, 'lng': -120.694434}}
```

...

</details>

### nocasedict

A case-insensitive list for Python

`pip install nocasedict` · installs (wheel) · licence: LGPL-2.1-or-later · rank 13380 · last release 2026-08-31 · [PyPI](https://pypi.org/project/nocasedict/) · [docs](https://nocasedict.readthedocs.io/en/master/) · [source](https://github.com/pywbem/nocasedict)

_README extract left out: share-alike licence._

### generative-ai-hub-sdk

[DEPRECATED] generative AI hub SDK

`pip install generative-ai-hub-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 13383 · last release 2025-05-14 · [PyPI](https://pypi.org/project/generative-ai-hub-sdk/)

<details><summary>README extract</summary>

This package is no longer maintained.

 Please use sap-ai-sdk-gen instead.

With this SDK you can leverage the power of generative models available in the generative AI Hub of SAP AI Core. ...

Sections: [DEPRECATED] SAP generative AI hub SDK, Configuration, Usage

</details>

### polymarket-us

Polymarket US Python SDK

`pip install polymarket-us` · installs (wheel) · licence: MIT · rank 13385 · last release 2026-10-08 · [PyPI](https://pypi.org/project/polymarket-us/) · [docs](https://docs.polymarket.us) · [source](https://github.com/Polymarket/polymarket-us-python)

<details><summary>README extract</summary>

Official Python SDK for the Polymarket US API.

Example:
```python
import asyncio
import os
from polymarket_us import AsyncPolymarketUS

async def main():
    async with AsyncPolymarketUS(
        key_id=os.environ["POLYMARKET_KEY_ID"],
        secret_key=os.environ["POLYMARKET_SECRET_KEY"],
    ) as client:
        # Concurrent requests
        events, markets = await asyncio.gather(
...
```

Sections: Polymarket US Python SDK, Usage, Public Endpoints (No Authentication), Authenticated Endpoints (Trading), Async Usage, Authentication, Error Handling, Configuration, Retries & reliability, WebSocket (Real-Time Data), API Reference, Events, Markets, Market response type migration

</details>

### ufal.udpipe

Bindings to UDPipe library

`pip install ufal.udpipe` · installs (wheel) · licence: mpl-2.0 · rank 13392 · last release 2025-11-20 · [PyPI](https://pypi.org/project/ufal.udpipe/)

<details><summary>README extract</summary>

The `ufal.udpipe` is a Python binding to UDPipe library <

The bindings is a straightforward conversion of the `C++` bindings API.
In Python 2, strings can be both `unicode` and UTF-8 encoded `str`, and the
library always produces `unicode`. In Python 3, strings must be only `str`.

The C++ API being wrapped follows. ...

Example:
```python
Helper Structures

  typedef vector<int> Children;

  typedef vector<uint8_t> Bytes;

  typedef vector<string> Comments;

  class ProcessingError {
  public:
    bool occurred();
    string message;
  };

  class Token {
   public:
    string form;
    string misc;

    Token(const string& form = string(), const string& misc = string());

...
```

Sections: ufal.udpipe, Wrapped C++ API, Examples, run_udpipe

</details>

### promql-builder

Library to compose PromQL queries in Python.

`pip install promql-builder` · installs (wheel) · licence: Apache Software License · rank 13398 · last release 2026-05-28 · [PyPI](https://pypi.org/project/promql-builder/) · [source](https://github.com/grafana/promql-builder.git)

<details><summary>README extract</summary>

A set of libraries for writing and composing PromQL queries as-code in Go,
Python or Typescript.

Example:
```python
from promql_builder.builders.promql import (
    div,
    gt,
    histogram_quantile,
    n,
    rate,
    sub,
    sum,
    time,
    vector,
)

# time() - demo_batch_last_success_timestamp_seconds > 3600
def batch_jobs_with_no_success_in_last_hour():
    return gt(
        sub(
            time(),
...
```

Sections: PromQL builder, Examples, Go, Python, Typescript, Maturity

</details>

### python-kadmin-rs

Python interface to the Kerberos administration interface (kadm5)

`pip install python-kadmin-rs` · installs (wheel) · licence: MIT · rank 13402 · last release 2026-10-17 · [PyPI](https://pypi.org/project/python-kadmin-rs/) · [docs](https://github.com/authentik-labs/kadmin-rs) · [source](https://github.com/authentik-labs/kadmin-rs.git)

<details><summary>README extract</summary>

This repository contains both a work-in-progress safe, idiomatic Rust bindings for libkadm5, the library to administrate a Kerberos realm that supports the Kerberos administration interface (mainly Heimdal and MIT Kerberos 5).

It also contains a Python API to those bindings.

This is a safe, idiomatic Rust interface to libkadm5. ...

Example:
```python
import kadmin

princ = "user/admin@EXAMPLE.ORG"
password = "vErYsEcUrE"
kadm = kadmin.KAdmin.with_password(kadmin.KAdm5Variant.MitClient, princ, password)
print(kadm.list_principals("*"))
```

Sections: kadmin, About compilation, About thread safety, python-kadmin-rs, # Releasing

</details>

### drf-jsonschema-serializer

JSON Schema support for Django REST Framework

`pip install drf-jsonschema-serializer` · installs (wheel) · licence: BSD License · rank 13415 · last release 2024-06-26 · [PyPI](https://pypi.org/project/drf-jsonschema-serializer/) · [docs](https://drf-jsonschema.readthedocs.io/en/stable/) · [source](https://github.com/maykinmedia/drf-jsonschema-serializer)

<details><summary>README extract</summary>

Features:
drf-jsonschema-serializer is a library built around Django REST Framework. It does the
following:

* Convert a DRF serializer into a JSON Schema.

* Provides `JSONSchemaField` that can validate JSON data according to
 a JSON schema. ...

</details>

### prices

Python price handling for humans

`pip install prices` · installs (wheel) · licence: BSD License · rank 13416 · last release 2022-10-07 · [PyPI](https://pypi.org/project/prices/)

<details><summary>README extract</summary>

Money:

Taxed money:

Taxed ranges:

Taxes:

While protecting you from all sorts of mistakes:

Example:
```python
from prices import Money
a = Money(10, 'USD')
a += Money(20, 'USD')
a.value
# Decimal('30')
a = a.quantize()
a.value
# Decimal('30.00')
a = Money('5.00', 'JPY')
a.quantize()
a.value
# Decimal('5')
```

</details>

### django-queryinspect

Django Query Inspector

`pip install django-queryinspect` · installs from source (sdist only) · licence: MIT License · rank 13423 · last release 2019-09-10 · [PyPI](https://pypi.org/project/django-queryinspect/)

### behresp

behresp

`pip install behresp` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 13429 · last release 2022-03-22 · [PyPI](https://pypi.org/project/behresp/)

<details><summary>README extract</summary>

This document tells you how to begin using or contributing to
Behavioral-Responses. Begin by reading the Tax-Calculator
documentation and then
the Behavioral-Responses user
guide that
describes how to write Python programs that use Behavioral-Responses
together with Tax-Calculator on your own computer. ...

Sections: Behavioral-Responses, What is Behavioral-Responses?, Disclaimer, Getting Started, Citing Behavioral-Responses

</details>

### ClusterShell

ClusterShell library and tools

`pip install ClusterShell` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 13430 · last release 2026-07-16 · [PyPI](https://pypi.org/project/ClusterShell/)

_README extract left out: share-alike licence._

### astatine

Some handy helper functions for Python's AST module.

`pip install astatine` · installs (wheel) · licence: MIT License · rank 13431 · last release 2023-08-15 · [PyPI](https://pypi.org/project/astatine/) · [docs](https://astatine.readthedocs.io/en/latest) · [source](https://github.com/python-formate/astatine)

<details><summary>README extract</summary>

Some handy helper functions for Python's AST module.

Astatine is a chemical element with the symbol At and atomic number 85.
Its name comes from the Greek astatos (ἄστατος), meaning "unstable".
It's a fitting name for Python's `ast` module, which has been unstable between releases.

</details>

### mastercard-api-core

MasterCard API Python Core SDK

`pip install mastercard-api-core` · installs from source (sdist only) · licence: BSD2 · rank 13436 · last release 2018-01-31 · [PyPI](https://pypi.org/project/mastercard-api-core/)

### gravitas-md2gdocs

Convert Markdown to Google Docs API requests

`pip install gravitas-md2gdocs` · installs (wheel) · licence: MIT · rank 13445 · last release 2025-12-10 · [PyPI](https://pypi.org/project/gravitas-md2gdocs/) · [docs](https://github.com/significant-gravitas/gravitas-md2gdocs#readme) · [source](https://github.com/significant-gravitas/gravitas-md2gdocs)

<details><summary>README extract</summary>

Convert Markdown to Google Docs API requests.

Example:
```python
from gravitas_md2gdocs import to_requests

markdown = """
# My Document

This is bold and *italic* text.

- Bullet one
- Bullet two

> A blockquote
"""

requests = to_requests(markdown)

# Use with your own Google Docs API client
docs_service.documents().batchUpdate(
    documentId=doc_id,
    body={'requests': requests}
).execute()
```

Sections: gravitas-md2gdocs, Usage, Basic: Get API Requests, Insert at a Specific Position, Helper Functions (requires `gravitas-md2gdocs[google]`), Setting Up Google Docs API, Alternative: Google Drive API with Native Markdown

</details>

### faker-enum

Enum provider for the Faker Python package.

`pip install faker-enum` · installs (wheel) · licence: MIT License · rank 13449 · last release 2018-10-26 · [PyPI](https://pypi.org/project/faker-enum/)

<details><summary>README extract</summary>

faker_enum is a provider for the Faker Python package.

Faker enum provides the ability to generate enum values based on an enum type.

>>>>>>
Usage
>>>>>>

Example:
```python
from enum import Enum

from faker import Faker
from faker_enum import EnumProvider

fake = Faker()
fake.add_provider(EnumProvider)

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

fake.enum(Color)
# One of [Color.RED, Color.GREEN, Color.BLUE]
```

Sections: Faker Enum, Summary

</details>

### upstash-ratelimit

Serverless ratelimiting package from Upstash

`pip install upstash-ratelimit` · installs (wheel) · licence: MIT License · rank 13450 · last release 2026-09-18 · [PyPI](https://pypi.org/project/upstash-ratelimit/) · [source](https://github.com/upstash/ratelimit-python)

<details><summary>README extract</summary>

> [!NOTE]
> This project is in GA Stage.
> The Upstash Professional Support fully covers this project. It receives regular updates, and bug fixes. The Upstash team is committed to maintaining and improving its functionality. ...

Example:
```python
from upstash_ratelimit import Ratelimit, FixedWindow
from upstash_redis import Redis

# Create a new ratelimiter, that allows 10 requests per 10 seconds
ratelimit = Ratelimit(
    redis=Redis.from_env(),
    limiter=FixedWindow(max_requests=10, window=10),
    # Optional prefix for the keys used in Redis. This is useful
...
```

Sections: Upstash Ratelimit Python SDK, Quick Start, Create database, Usage, Block until ready, Using multiple limits, Ratelimiting algorithms, Fixed Window, Pros, Cons, Sliding Window

</details>

### tabula

Ascii table

`pip install tabula` · installs from source (sdist only) · licence: Apache Software License · rank 13462 · last release 2012-11-01 · [PyPI](https://pypi.org/project/tabula/)

<details><summary>README extract</summary>

Ascii table

 pip install numpy

Sections: tabula, Dependencies

</details>

### trame-vtklocal

VTK Local Rendering using WASM

`pip install trame-vtklocal` · installs (wheel) · licence: Apache Software License · rank 13480 · last release 2026-10-28 · [PyPI](https://pypi.org/project/trame-vtklocal/)

<details><summary>README extract</summary>

Local Rendering using VTK.wasm to match server side rendering pipeline on the client side.
The current code base is still at its infancy but we aim to make it the default implementation for local rendering using VTK/ParaView with trame.
This WASM capability is starting to be available with VTK 9.4 but major improvement are happening in VTK 9.6. ...

Example:
```python
from trame.widgets import vtklocal, vuetify

state.app_loading = True
state._vtklocal_seen_active = False

def on_vtklocal_progress(event):
    if event.get("active"):
        state._vtklocal_seen_active = True
        state.app_loading = True
    elif state._vtklocal_seen_active:
        state.app_loading = False

...
```

...

</details>

### flynt

CLI tool to convert a python project's %-formatted strings to f-strings.

`pip install flynt` · installs (wheel) · licence: MIT · rank 13483 · last release 2025-07-29 · [PyPI](https://pypi.org/project/flynt/)

<details><summary>README extract</summary>

`flynt` is a command line tool to automatically convert a project's Python code from old "%-formatted" and .format(...) strings into Python 3.6+'s "f-strings".

F-Strings:

> Not only are they more readable, more concise, and less prone to error than other ways of formatting, but they are also faster!

Example:
```python
usage: flynt [-h] [-v | -q] [--no-multiline | -ll LINE_LENGTH] [-d |
             --stdout] [-s] [--no-tp] [--no-tf] [-tc] [-tj] [-f]
             [-a] [-e EXCLUDE [EXCLUDE ...]] [-nb] [--version]
             [--report]
             [src ...]

flynt v.1.0.3

positional arguments:
...
```

Sections: flynt - string formatting converter, Usage, Command line options, Sample output of a successful run, Pre-commit hook, Configuration files, About, Dangers of conversion

</details>

### tiledb

Pythonic interface to the TileDB array storage manager

`pip install tiledb` · installs (wheel) · licence: MIT License · rank 13493 · last release 2026-02-25 · [PyPI](https://pypi.org/project/tiledb/)

<details><summary>README extract</summary>

*TileDB-Py* is a Python interface to the TileDB Storage Engine.

* Installation
* Build Instructions
* TileDB Academy
* Python API reference

Sections: TileDB-Py, Quick Links

</details>

### plette

Structured Pipfile and Pipfile.lock models.

`pip install plette` · installs (wheel) · licence: ISC License (ISCL) · rank 13494 · last release 2026-10-16 · [PyPI](https://pypi.org/project/plette/)

<details><summary>README extract</summary>

Plette implements Pipfile and Pipfile.lock parsers, generators, and optional
validators to let the user work with them in a structured manner.

</details>

### tox-gh

Seamless integration of tox into GitHub Actions.

`pip install tox-gh` · installs (wheel) · licence: MIT · rank 13497 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tox-gh/) · [docs](https://github.com/tox-dev/tox-gh#tox-gh) · [source](https://github.com/tox-dev/tox-gh)

<details><summary>README extract</summary>

See the changelog for released changes and the contribution guide for news fragments.

Seamless integration of tox into GitHub Actions.

tox-gh automatically selects which tox environments to run on each Python version in your GitHub Actions matrix,
allowing parallel test execution across multiple workers. ...

Features:
GitHub Actions workflows typically define a matrix strategy with multiple Python versions:

Each matrix cell spawns a separate worker. ...

...

</details>

### hotglue-singer-sdk

A framework for building Singer taps and targets

`pip install hotglue-singer-sdk` · installs (wheel) · licence: Apache Software License · rank 13506 · last release 2026-11-05 · [PyPI](https://pypi.org/project/hotglue-singer-sdk/) · [docs](https://docs.hotglue.com) · [source](https://github.com/hotgluexyz/hotgluesingersdk)

<details><summary>README extract</summary>

This is a fork of Melanto's SingerSDK for special use in hotglue, an embedded integration platform for running Singer Taps and Targets.

Taps and targets built on the SDK are automatically compliant with the
Singer Spec, the
de-facto open source standard for extract and load pipelines.

Sections: Hotglue SDK for Taps, Authenticator Requirements, Usage

</details>

### mecab-ko

Python wrapper for the MeCab-ko morphological analyzer for Korean

`pip install mecab-ko` · installs (wheel) · licence: BSD License · rank 13507 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mecab-ko/)

<details><summary>README extract</summary>

This is a Python wrapper for the [MeCab-ko] morphological analyzer for Korean text.
It works with Python 3.9 and greater.

There are several implementations of python binding or wrapper for MeCab-ko, but they are generally not well maintained. ...

Example:
```python
>>> import mecab_ko as MeCab
>>> tagger = MeCab.Tagger("-Owakati")
>>> tagger.parse("아버지가방에들어가신다").split()
['아버지', '가', '방', '에', '들어가', '신다']

>>> tagger = MeCab.Tagger()
>>> print(tagger.parse("아버지가방에들어가신다"))
아버지  NNG,*,F,아버지,*,*,*,*
가      JKS,*,F,가,*,*,*,*
방      NNG,*,T,방,*,*,*,*
에      JKB,*,F,에,*,*,*,*
들어가  VV,*,F,들어가,*,*,*,*
...
```

Sections: Basic usage, Dictionaries, Common Issues, Windows Redistributable, Specifying a mecabrc, Alternatives, Releasing, Licensing

</details>

### null

Implements the null object pattern.

`pip install null` · installs from source (sdist only) · licence: MIT License · rank 13514 · last release 2013-03-05 · [PyPI](https://pypi.org/project/null/)

<details><summary>README extract</summary>

Implements the null object pattern.

Provides:

- a `Null` singleton that can be used like `None` (but is not `None` and
 is not equal to `None`)

- a `NullList` that returns `Null` instead of raising `IndexError`

- a `NullDict` that returns `Null` instead of raising `KeyError` ...

Sections: null, How do I run the tests?, 0.6.1, 0.6.0, 0.5.0

</details>

### oneccl

Intel® oneAPI Collective Communications Library Runtime Environment

`pip install oneccl` · installs (wheel) · licence: Other/Proprietary License · rank 13523 · last release 2026-10-30 · [PyPI](https://pypi.org/project/oneccl/)

### lumaai

The official Python library for the lumaai API

`pip install lumaai` · installs (wheel) · licence: Apache Software License · rank 13524 · last release 2026-04-07 · [PyPI](https://pypi.org/project/lumaai/) · [source](https://github.com/lumalabs/lumaai-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The LumaAI Python library provides convenient access to the LumaAI REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

The REST API documentation can be found on lumalabs.ai. ...

Example:
```python
import os
from lumaai import LumaAI

client = LumaAI(
    auth_token=os.environ.get("LUMAAI_API_KEY"),  # This is the default and can be omitted
)

generation = client.generations.create(
    model="ray-2",
    aspect_ratio="16:9",
    loop=False,
...
```

...

</details>

### zope.testrunner

Zope testrunner script.

`pip install zope.testrunner` · installs (wheel) · licence: ZPL-2.1 · rank 13537 · last release 2026-07-30 · [PyPI](https://pypi.org/project/zope.testrunner/) · [source](https://github.com/zopefoundation/zope.testrunner)

<details><summary>README extract</summary>

This package provides a flexible test runner with layer support.

Detailed documentation is hosted at

Example:
```python
import unittest
import doctest

class TestArithmetic(unittest.TestCase):

    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 4)

def doctest_string_formatting():
    """Test Python string formatting

        >>> print('{} + {}'.format(2, 2))
        2 + 2

    """

def test_suite():
    return unittest.TestSuite([
...
```

Sections: zope.testrunner, Using zope.testrunner, Buildout-based projects, Virtualenv-based projects, Some useful command-line options to get you started, Writing tests, Test grouping, Other features, 8.3 (2026-07-30), 8.2 (2026-01-23), 8.1 (2025-10-02), 8.0 (2025-09-12), 7.4 (2025-05-28), 7.3 (2025-05-15)

</details>

### pytest-mongo

MongoDB process and client fixtures plugin for Pytest.

`pip install pytest-mongo` · installs (wheel) · licence: LGPL-3.0-or-later · rank 13547 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pytest-mongo/) · [source](https://github.com/dbfixtures/pytest-mongo)

_README extract left out: share-alike licence._

### imagekitio

The official Python library for the ImageKit API

`pip install imagekitio` · installs (wheel) · licence: Apache Software License · rank 13559 · last release 2026-11-02 · [PyPI](https://pypi.org/project/imagekitio/) · [source](https://github.com/imagekit-developer/imagekit-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The ImageKit Python SDK provides convenient access to the ImageKit REST API from any Python 3.9+ application. It offers powerful tools for URL generation and transformation, signed URLs for secure content delivery, webhook verification, file uploads, and more. ...

Example:
```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),  # This is the default and can be omitted
)

# Upload a file
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

response = client.files.upload(
    file=file_data,
    file_name="uploaded-image.jpg",
)
...
```

...

</details>

### toml-rs

A High-Performance TOML Parser for Python written in Rust

`pip install toml-rs` · installs (wheel) · licence: Unlicense · rank 13581 · last release 2026-10-18 · [PyPI](https://pypi.org/project/toml-rs/) · [source](https://github.com/lava-sh/toml-rs)

<details><summary>README extract</summary>

_A High-Performance TOML v1.0.0 / v1.1.0 parser for Python written in Rust

[][pypi]
[][pypistats]
[][pypi]
[][pypi]

Features:
* The fastest TOML parser in Python (see benchmarks)

* Drop-in compatibility with most `tomllib` use cases
 (see below)

Example:
```python
import tomllib
from pprint import pprint

import toml_rs

toml = """\
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]
[servers.alpha]
ip = "10.0.0.1"
...
```

Sections: toml-rs, Features, Examples, Differences with `tomllib`

</details>

### dxpy

DNAnexus Platform API bindings for Python

`pip install dxpy` · installs from source (sdist only) · licence: Apache Software License · rank 13605 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dxpy/)

<details><summary>README extract</summary>

DNAnexus Documentation

dxpy API Documentation

Building

From the dx-toolkit root directory:

Debugging

Set the `_DX_DEBUG` environment variable to a positive integer before
running a dxpy-based program (such as `dx`) to display the input and
output of each API call. ...

Example:
```python
_foo = None

def get_foo():
    initialize()
    return _foo
```

Sections: dxpy: DNAnexus Python API, Debugging inside the IDE (PyCharm)

</details>

### SoftLayer

A library for SoftLayer's API

`pip install SoftLayer` · installs (wheel) · licence: MIT License · rank 13613 · last release 2026-03-24 · [PyPI](https://pypi.org/project/SoftLayer/)

<details><summary>README extract</summary>

This library provides a simple Python client to interact with SoftLayer's
XML-RPC API.

A command-line interface is also included and can be used to manage various
SoftLayer products and services.

Documentation for the Python client is available at Read the Docs .

Additional API documentation can be found on the SoftLayer Development Network: ...

Example:
```python
import SoftLayer
import logging

class invoices():

    def init(self):
        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def main(self):
        mask = "mask[id]"
        account = self.client.call('Account', 'getObject', mask=mask);
...
```

...

</details>

### packbits

PackBits encoder/decoder

`pip install packbits` · installs from source (sdist only) · licence: MIT License · rank 13622 · last release 2013-04-06 · [PyPI](https://pypi.org/project/packbits/)

<details><summary>README extract</summary>

This module implements a PackBits encoder/decoder for Python 2.x and 3.x.

PackBits encoding is used in PSD and TIFF files.

Sections: PackBits encoder/decoder, Usage

</details>

### tkcalendar

Calendar and DateEntry widgets for Tkinter

`pip install tkcalendar` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13638 · last release 2019-12-28 · [PyPI](https://pypi.org/project/tkcalendar/)

_README extract left out: share-alike licence._

### serpyco

Fast serialization of dataclasses using Cython

`pip install serpyco` · installs from source (sdist only) · licence: MIT License · rank 13643 · last release 2024-05-04 · [PyPI](https://pypi.org/project/serpyco/)

<details><summary>README extract</summary>

Serpyco is a serialization library for Python 3.6+ dataclasses that works just by defining your dataclasses:

Serpyco works by analysing the dataclass fields and can recognize many types : `List`, `Set`, `Tuple`, `Optional`, `Union`... You can also embed other dataclasses in a definition. ...

Features:
- Serialization and unserialization of dataclasses
- Validation of input/output data
- Very fast
- Extensible through custom encoders

Example:
```python
import dataclasses
import typing

import serpyco

@dataclasses.dataclass
class Example(object):
    name: str
    num: int
    tags: typing.List[str]

serializer = serpyco.Serializer(Example)

result = serializer.dump(Example(name="foo", num=2, tags=["hello", "world"]))
print(result)

{'name': 'foo', 'num': 2, 'tags': ['hello', 'world']}
...

</details>

### sops

Secrets OPerationS (sops) is an editor of encrypted files

`pip install sops` · installs from source (sdist only) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 13646 · last release 2018-11-28 · [PyPI](https://pypi.org/project/sops/)

<details><summary>README extract</summary>

This is the Python version of SOPS that is no longer maintained. We fix the occasional bug, but all improvements happen in the Go version of SOPS, over in the Master branch. You have been warned!

sop is an editor of encrypted files that supports YAML, JSON and BINARY formats and encrypts with AWS KMS and PGP (via GnuPG). Watch the demo. ...

Example:
```python
$ git clone
$ cd sops
$ gpg --import tests/sops_functional_tests_key.asc
$ sops example.yaml
```

...

</details>

### dumbyaml

A YAML parser that reads only a restricted version of YAML.

`pip install dumbyaml` · installs from source (sdist only) · licence: MIT License · rank 13666 · last release 2015-11-20 · [PyPI](https://pypi.org/project/dumbyaml/)

### nucliadb-sdk

NucliaDB SDK

`pip install nucliadb-sdk` · installs (wheel) · licence: Apache-2.0 · rank 13672 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nucliadb-sdk/) · [source](https://github.com/nuclia/nucliadb)

<details><summary>README extract</summary>

The NucliaDB SDK is a Python library designed as a thin wrapper around the NucliaDB HTTP API. It is tailored for developers who wish to create low-level scripts to interact with NucliaDB. ...

Example:
```python
from nucliadb_sdk import NucliaDB, Region

ndb = NucliaDB(region=Region.EUROPE1, api_key="my-api-key")
```

Sections: NucliaDB SDK, WARNING, How to use it?, Example Usage

</details>

### pysnowflake

Python Snowflake Kit

`pip install pysnowflake` · installs from source (sdist only) · licence: UNKNOWN · rank 13679 · last release 2014-11-20 · [PyPI](https://pypi.org/project/pysnowflake/)

<details><summary>README extract</summary>

A library that provides snowflake features to python, including Client and Server.
You will not need to

This is extend of with Client adding.

See documentations

Sections: Python SnowFlake, 0.1.3

</details>

### opencode-ai

The official Python library for the opencode API

`pip install opencode-ai` · installs (wheel) · licence: MIT License · rank 13685 · last release 2025-08-27 · [PyPI](https://pypi.org/project/opencode-ai/) · [source](https://github.com/sst/opencode-sdk-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Opencode Python library provides convenient access to the Opencode REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
from opencode_ai import Opencode

client = Opencode()

sessions = client.session.list()
```

Sections: Opencode Python API library, Documentation, Usage, Async usage, With aiohttp, Streaming responses, Using types, Handling errors, Retries, Timeouts, Advanced, Logging, How to tell whether `None` means `null` or missing, Accessing raw response data (e.g. headers)

</details>

### setoptconf

A module for retrieving program settings from various sources in a consistant method.

`pip install setoptconf` · installs (wheel) · licence: MIT License · rank 13691 · last release 2021-09-10 · [PyPI](https://pypi.org/project/setoptconf/)

<details><summary>README extract</summary>

`setoptconf` is a Python library that can be used to retrieve program settings
from a variety of common sources:

* Command Line
* Environment Variables
* INI Files
* JSON Files
* YAML Files
* Python Objects/Modules ...

Example:
```python
import setoptconf as soc
```

</details>

### pyproject-parser

Parser for 'pyproject.toml'

`pip install pyproject-parser` · installs (wheel) · licence: MIT License · rank 13694 · last release 2025-12-11 · [PyPI](https://pypi.org/project/pyproject-parser/) · [docs](https://pyproject-parser.readthedocs.io/en/latest) · [source](https://github.com/repo-helper/pyproject-parser)

### evernote3

Evernote SDK for Python3

`pip install evernote3` · installs (wheel) · licence: BSD License · rank 13708 · last release 2020-06-15 · [PyPI](https://pypi.org/project/evernote3/)

### vellum-ai

(no summary)

`pip install vellum-ai` · installs (wheel) · licence: MIT License · rank 13712 · last release 2026-10-02 · [PyPI](https://pypi.org/project/vellum-ai/) · [source](https://github.com/vellum-ai/vellum-python-sdks)

<details><summary>README extract</summary>

Learn more
 Talk to us

Vellum is the end-to-end development platform for building production-grade AI applications.

- Orchestration: A powerful SDK and IDE for defining and debugging the control flow of your AI applications
- Prompting: A best-in-class prompt playground for iterating on and refining prompts between models from any provider ...

Sections: Introduction, Core Features, Get Started, Client SDK, Workflows SDK, Open-Source vs. Paid

</details>

### braintrust-api

The official Python library for the braintrust API

`pip install braintrust-api` · installs (wheel) · licence: Apache Software License · rank 13746 · last release 2024-11-28 · [PyPI](https://pypi.org/project/braintrust-api/) · [source](https://github.com/braintrustdata/braintrust-api-py)

<details><summary>README extract</summary>

The Braintrust Python library provides convenient access to the Braintrust REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from braintrust_api import Braintrust

client = Braintrust(
    api_key=os.environ.get("BRAINTRUST_API_KEY"),  # This is the default and can be omitted
)

project = client.projects.create(
    name="foobar",
)
print(project.id)
```

...

</details>

### python-resize-image

A Small python package to easily resize images

`pip install python-resize-image` · installs (wheel) · licence: MIT License · rank 13754 · last release 2021-11-04 · [PyPI](https://pypi.org/project/python-resize-image/)

<details><summary>README extract</summary>

|python-resize-image v1.1.20 on PyPiMIT licenseStable|

This package provides function for easily resizing images.

- Pillow 2.7++
- Python 2.7/3.4

Example:
```python
from PIL import Image

from resizeimage import resizeimage

with open('test-image.jpeg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [200, 100])
        cover.save('test-image-cover.jpeg', image.format)
```

Sections: A python package to easily resize images, Dependencies, Introduction, Usage, API Reference, `resize_crop(image, size, validate=True)`, `resize(method, *args, **kwargs)`, Tests

</details>

### hdx-python-country

HDX Python country code and exchange rate (fx) utilities

`pip install hdx-python-country` · installs (wheel) · licence: MIT License · rank 13757 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hdx-python-country/) · [source](https://github.com/OCHA-DAP/hdx-python-country)

<details><summary>README extract</summary>

The HDX Python Country Library provides utilities to map between country and region
codes and names and to match administrative level names from different sources.
It also provides utilities for foreign exchange enabling obtaining current and historic
FX rates for different currencies. ...

Sections: Environment, Pre-commit, Packages, Project, Documentation, WFP DataBridges Client

</details>

### pingparsing

pingparsing is a CLI-tool/Python-library parser and transmitter for the ping command.

`pip install pingparsing` · installs (wheel) · licence: MIT License · rank 13762 · last release 2024-05-02 · [PyPI](https://pypi.org/project/pingparsing/) · [docs](https://pingparsing.rtfd.io/) · [source](https://github.com/thombashi/pingparsing)

<details><summary>README extract</summary>

pingparsing is a CLI-tool/Python-library parser and transmitter for the ping command.

Example:
```python
usage: pingparsing [-h] [-V] [--max-workers MAX_WORKERS]
                   [--timestamp {none,epoch,datetime}] [-c COUNT]
                   [-s PACKET_SIZE] [--ttl TTL] [-w DEADLINE]
                   [--timeout TIMEOUT] [-I INTERFACE] [--addopts OPTIONS]
                   [--indent INDENT] [--icmp-reply] [--timezone TIMEZONE]
...
```

Sections: Summary, CLI Usage, Execute ping and parse the result, Parse ping result file, Parse from the standard input, CLI help, Library Usage, Parsing `ping` command output, Recommended ping command execution, Linux, Windows, Dependencies, Optional Dependencies

</details>

### fast-ebook

Rust-powered EPUB2/EPUB3 library for Python. Fast reading, writing, validation, and markdown conversion.

`pip install fast-ebook` · installs (wheel) · licence: not stated · rank 13766 · last release 2026-04-10 · [PyPI](https://pypi.org/project/fast-ebook/) · [source](https://github.com/arc53/fast-ebook)

<details><summary>README extract</summary>

Rust-powered EPUB2/EPUB3 library for Python. Fast reading, writing, validation, and markdown conversion — MIT-licensed.

Converting War and Peace (1.8 MB EPUB) to a single markdown document:

| Library | Time | |

| ebooklib + html2text | 375 ms | baseline |
| fast-ebook `book.to_markdown()` | 56 ms | 6.7x faster | ...

Example:
```python
from fast_ebook import epub

book = epub.read_epub('war_and_peace.epub')
markdown = book.to_markdown()
```

Sections: fast-ebook, How fast?, Quick Start, Migration from ebooklib, Read, Write, Convert to Markdown, Parallel batch read, Documentation

</details>

### retinaface-py

RetinaFace: Single-stage Dense Face Localisation in the Wild

`pip install retinaface-py` · installs (wheel) · licence: MIT License · rank 13789 · last release 2023-02-14 · [PyPI](https://pypi.org/project/retinaface-py/)

<details><summary>README extract</summary>

A PyTorch implementation of RetinaFace: Single-stage Dense Face Localisation in the Wild. Model size only 1.7M, when Retinaface use mobilenet0.25 as backbone net. We also provide resnet50 as backbone net to get better result. The official code in Mxnet can be found here. ...

Sections: RetinaFace in PyTorch, Mobile or Edge device deploy, FDDB Performance., Data, Data1, Training, Evaluation, Evaluation widerface val, Evaluation FDDB, TensorRT, References

</details>

### hanzoai

The official Python library for the Hanzo API

`pip install hanzoai` · installs (wheel) · licence: Apache Software License · rank 13815 · last release 2026-10-26 · [PyPI](https://pypi.org/project/hanzoai/) · [source](https://github.com/hanzoai/python-sdk)

<details><summary>README extract</summary>

`hanzoai` is the Python client for the Hanzo API, generated from the API's own
OpenAPI document. Every `/v1` route is in it, and the names it exposes are the
document's operation ids. `.spec-lock` names the commit and sha256
of the document this tree was cut from.

Example:
```python
from hanzoai import Client

c = Client()                          # HANZO_CLIENT_ID / HANZO_CLIENT_SECRET

print(c.budget.left().left, "free calls left today")
print(c.policy.check("usr_7", "write", "graph:acme").allow)

a = c.search.find("q3 incident postmortems")
if a.denied:
    for cure in a.denied.cures:
        print(cure.kind, cure.url)
...
```

Sections: Hanzo Python SDK, Quickstart, Answers, Auth, Tenants, Held calls, Examples, The rest of the repo, Hanzo — the Open AI Cloud

</details>

### pytest-progress

pytest plugin for instant test progress status

`pip install pytest-progress` · installs (wheel) · licence: MIT License · rank 13817 · last release 2025-11-11 · [PyPI](https://pypi.org/project/pytest-progress/) · [source](https://github.com/ssrikanta/pytest-progress)

<details><summary>README extract</summary>

pytest-progress is a plugin for py.test that allows to
print the test progress like number of tests Passed , Failed, Skipped and also
instant test failure messages.

You will need the following prerequisites in order to use pytest-progress:

- Python 3.8, 3.9, 3.10, 3.11 and 3.12
- pytest

Sections: pytest-progress, Requirements, Examples

</details>

### adcp

Official Python client for the Ad Context Protocol (AdCP)

`pip install adcp` · installs (wheel) · licence: Apache Software License · rank 13821 · last release 2026-11-04 · [PyPI](https://pypi.org/project/adcp/) · [docs](https://docs.adcontextprotocol.org) · [source](https://github.com/adcontextprotocol/adcp-client-python)

<details><summary>README extract</summary>

Example:
```python
from adcp.testing import test_agent

# Zero configuration - just import and call with kwargs!
products = await test_agent.simple.get_products(
    brief='Coffee subscription service for busy professionals',
    buying_mode='brief',
)

print(f"Found {len(products.products)} products")
```

Sections: Choose your path, Building an AdCP Agent, Multi-agent discovery manifest, Connecting to AdCP Agents, The Core Concept, Upgrading to SDK 9, Quick Start: Test Helpers, Simple vs. Standard API, Available Test Helpers, Quick Start: Distributed Operations, Documentation, Features, Test Helpers, Type Safety

</details>

### oneccl-devel

Intel® oneAPI Collective Communications Library

`pip install oneccl-devel` · installs (wheel) · licence: Other/Proprietary License · rank 13830 · last release 2026-10-30 · [PyPI](https://pypi.org/project/oneccl-devel/)

### spookyhash

A Python wrapper for SpookyHash version 2

`pip install spookyhash` · installs (wheel) · licence: MIT License · rank 13838 · last release 2025-11-09 · [PyPI](https://pypi.org/project/spookyhash/) · [source](https://github.com/buhanec/spookyhash)

<details><summary>README extract</summary>

A Python wrapper of Bob Jenkins' SpookyHash version 2. Offers 32- 64- and 128-bit oneshot and incremental hashes.

Example:
```python
>>> import spookyhash

>>> spookyhash.hash32(b'hello world')
2617184861
>>> spookyhash.hash32(b'hello world', seed=0x12345678)
3380090220

>>> spookyhash.hash64(b'hello world')
14865987102431973981
>>> spookyhash.hash64(b'hello world', seed=123)
5719863273689036421

>>> spookyhash.hash128(b'hello world')
185933735475381961281710998418114941533
...
```

Sections: spookyhash, Usage, Oneshot Hashes, Incremental Hashes, Platform Independence

</details>

### impi-rt

Intel® MPI Library

`pip install impi-rt` · installs (wheel) · licence: Other/Proprietary License · rank 13860 · last release 2026-10-30 · [PyPI](https://pypi.org/project/impi-rt/)

<details><summary>README extract</summary>

Use this standards-based MPI implementation to deliver flexible, efficient, scalable cluster messaging on Intel® architecture. Compatible with the open-source MPICH implementation.

</details>

### PySmbClient

A convenient smbclient wrapper

`pip install PySmbClient` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 13868 · last release 2017-03-03 · [PyPI](https://pypi.org/project/PySmbClient/)

_README extract left out: share-alike licence._

### nucliadb-protos

Protobuf definitions for nucliadb

`pip install nucliadb-protos` · installs (wheel) · licence: Apache-2.0 · rank 13870 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nucliadb-protos/) · [source](https://github.com/nuclia/nucliadb)

### pyavd-utils

Rust based utilities used by PyAVD. Should not be used directly and may not follow semantic versioning.

`pip install pyavd-utils` · installs (wheel) · licence: Apache-2.0 · rank 13874 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pyavd-utils/) · [source](https://github.com/aristanetworks/avd)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2025-2026 Arista Networks, Inc.
 ~ Use of this source code is governed by the Apache License 2.0
 ~ that can be found in the LICENSE file.

This package is an internal dependency designed solely for the use of the `pyavd` Python library. It exposes low-level functionality and is not intended for direct use by end-users. ...

Sections: `pyavd-utils` 🦀, ⚠️ Danger, Purpose, Merge queue

</details>

### pyCalverter

Python Calendar Converter

`pip install pyCalverter` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 13883 · last release 2011-06-11 · [PyPI](https://pypi.org/project/pyCalverter/)

_README extract left out: share-alike licence._

### django-bootstrap-datepicker-plus

Bootstrap3/Bootstrap4/Bootstrap5 DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

`pip install django-bootstrap-datepicker-plus` · installs (wheel) · licence: MIT · rank 13891 · last release 2026-02-13 · [PyPI](https://pypi.org/project/django-bootstrap-datepicker-plus/) · [docs](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/) · [source](https://github.com/monim67/django-bootstrap-datepicker-plus)

<details><summary>README extract</summary>

This django widget contains Bootstrap 3, Bootstrap 4 and Bootstrap 5
Date-Picker, Time-Picker, DateTime-Picker, Month-Picker and Year-Picker input
with date-range-picker functionality for django version >= 2.0. ...

Example:
```python
# File: views.py
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from .models import Question

class CreateView(generic.edit.CreateView):
    model = Question
    fields = ["question_text", "pub_date"]
    def get_form(self):
        form = super().get_form()
...
```

Sections: django-bootstrap-datepicker-plus, Demo, Getting Started, Usage, Usage in Generic View, Advanced Usage, Types of DatePickers, Implement date-range-picker, Customization

</details>

### labqoat

Typed Python SDK and lab command-line client for the Labqoat platform

`pip install labqoat` · installs (wheel) · licence: MIT · rank 13895 · last release 2026-10-30 · [PyPI](https://pypi.org/project/labqoat/)

<details><summary>README extract</summary>

Typed SDK and CLI for the Labqoat starter API. Distribution
`labqoat`, import `labqoat`, commands `lab` and `labqoat`.

Example:
```python
from labqoat.client import Client

with Client(" "local", "your-password") as client:
    note = client.create_note("First", body="Hello")
    page = client.list_notes(limit=20)
    for item in client.iter_notes():
        print(item.id, item.title)
```

Sections: labqoat-python, Quick start, Inference and evaluation

</details>

### mac-vendor-lookup

Find the vendor for a given MAC address

`pip install mac-vendor-lookup` · installs (wheel) · licence: Apache Software License · rank 13898 · last release 2025-11-30 · [PyPI](https://pypi.org/project/mac-vendor-lookup/)

<details><summary>README extract</summary>

This library provides an easy way to get vendor information from a MAC address. It contains a local copy of the IEEE's
OUI prefix list. It has an asynchronous interface using Python 3's asyncio as well as a regular synchronous interface
for old-school usage.

Example:
```python
from mac_vendor_lookup import MacLookup

print(MacLookup().lookup("00:80:41:12:FE"))
```

Sections: Mac Vendor Lookup, Basic Usage, Update the vendor list, Vendor list custom location or path, Async Interface, Command line interface

</details>

### python-upwork-oauth2

Python bindings for Upwork API (OAuth2)

`pip install python-upwork-oauth2` · installs (wheel) · licence: Apache Software License · rank 13900 · last release 2024-11-26 · [PyPI](https://pypi.org/project/python-upwork-oauth2/)

<details><summary>README extract</summary>

This project provides a set of resources of Upwork API from
 based on OAuth 2.0.

Features:
The library supports all GraphQL calls, which are publicly shared at Upwork

Sections: Python bindings for Upwork API (OAuth2), Upwork API, Features, SLA, Requirements, Usage

</details>

### mastercard-places

MasterCard API Python SDK

`pip install mastercard-places` · installs from source (sdist only) · licence: BSD · rank 13901 · last release 2018-04-11 · [PyPI](https://pypi.org/project/mastercard-places/)

### pyresilience

Unified resilience patterns for Python — retry, circuit breaker, timeout, fallback, bulkhead, rate limiter, and cache in one decorator.

`pip install pyresilience` · installs (wheel) · licence: MIT · rank 13903 · last release 2026-10-18 · [PyPI](https://pypi.org/project/pyresilience/) · [docs](https://pyresilience.readthedocs.io/) · [source](https://github.com/AhsanSheraz/pyresilience)

<details><summary>README extract</summary>

All resilience patterns. One decorator. Zero dependencies.

Inspired by Java's Resilience4j. Stop juggling `tenacity` for retries, `pybreaker` for circuit breakers, and custom code for everything else. ...

Features:
- One library instead of many — No need to wire together `tenacity` + `pybreaker` + custom timeout/fallback/rate limiting code. One config, one decorator.
- Patterns that work together — Circuit breaker state is shared across retries. ...

Example:
```python
import requests
from pyresilience import resilient, RetryConfig, TimeoutConfig, CircuitBreakerConfig

@resilient(
    retry=RetryConfig(max_attempts=3, delay=1.0),
    timeout=TimeoutConfig(seconds=10),
    circuit_breaker=CircuitBreakerConfig(failure_threshold=5),
)
def call_api(endpoint: str) -> dict:
...

</details>

### mastercard-merchant-identifier

Mastercard API Python SDK

`pip install mastercard-merchant-identifier` · installs from source (sdist only) · licence: BSD · rank 13908 · last release 2019-05-14 · [PyPI](https://pypi.org/project/mastercard-merchant-identifier/)

### django-admin-cursor-paginator

Drop-in replacement for django admin default pagination that works fast with huge tables.

`pip install django-admin-cursor-paginator` · installs from source (sdist only) · licence: MIT License · rank 13923 · last release 2025-10-26 · [PyPI](https://pypi.org/project/django-admin-cursor-paginator/)

<details><summary>README extract</summary>

Drop-in replacement for django admin default pagination that works fast with huge tables.

- You are using django (>2.0) admin
- Some of your models/tables contains so much data that list page lags
- You don't want to make separate CRM page for them and just need fast and simple solution ...

Example:
```python
from admin_cursor_paginator import CursorPaginatorAdmin

class YourModelAdmin(CursorPaginatorAdmin):
    cursor_ordering_field = '-created_at'  # default is '-pk'

class AnotherModelAdmin(CursorPaginatorAdmin):
    cursor_ordering_field = 'parent__sort'  # joins are supported as well
```

Sections: django-admin-cursor-paginator, Prerequisites, Usage example, The problem, The solution, Test project

</details>

### money

Python Money Class

`pip install money` · installs from source (sdist only) · licence: MIT License · rank 13926 · last release 2016-04-17 · [PyPI](https://pypi.org/project/money/)

<details><summary>README extract</summary>

Money class with optional CLDR-backed locale-aware formatting and an extensible currency exchange solution.

This is version 1.3.0.

:Development:
:Latest release:

This package is compatible with Python 2.7, 3.4, 3.5 (tested in 2.7.11, 3.4.4, 3.5.1), but there are important Differences between Python versions. All code examples use Python 3.x. ...

Example:
```python
>>> from money import Money
>>> m = Money(amount='2.22', currency='EUR')
>>> m
EUR 2.22
```

Sections: Python Money, Usage, Currency presets, Formatting, Currency exchange, XMoney, Exceptions, Hierarchy, Differences between Python versions, Design decisions, Localization, Currency

</details>

### dictobj

A set of Python dictionary objects where keys can be accessed as instance attributes.

`pip install dictobj` · installs from source (sdist only) · licence: Apache Software License · rank 13948 · last release 2016-04-14 · [PyPI](https://pypi.org/project/dictobj/)

### py-memoize

Caching library for asynchronous Python applications (both based on asyncio and Tornado) that handles dogpiling properly and provides a configurable & extensible API.

`pip install py-memoize` · installs (wheel) · licence: Apache License 2.0 · rank 13951 · last release 2024-10-07 · [PyPI](https://pypi.org/project/py-memoize/)

<details><summary>README extract</summary>

Extended docs (including API docs) available at memoize.readthedocs.io.

What: Caching library for asyncio Python applications.

Why: Python deserves library that works in async world
(for instance handles dog-piling )
and has a proper, extensible API. ...

Example:
```python
import asyncio
import random
from memoize.wrapper import memoize

@memoize()
async def expensive_computation():
    return 'expensive-computation-' + str(random.randint(1, 100))

async def main():
    print(await expensive_computation())
    print(await expensive_computation())
    print(await expensive_computation())

if name == "main":
...
```

...

</details>

### toonify

TOON (Token-Oriented Object Notation) - A compact, human-readable serialization format for LLMs

`pip install toonify` · installs (wheel) · licence: MIT License · rank 13952 · last release 2026-02-06 · [PyPI](https://pypi.org/project/toonify/) · [docs](https://github.com/ScrapeGraphAI/toonify#readme) · [source](https://github.com/ScrapeGraphAI/toonify)

<details><summary>README extract</summary>

English | 中文 | 한국어

A compact, human-readable serialization format designed for passing structured data to Large Language Models with significantly reduced token usage.

Features:
TOON achieves CSV-like compactness while adding explicit structure, making it ideal for:
- Reducing token costs in LLM API calls
- Improving context window efficiency
- Maintaining human readability
- Preserving data structure and types

Example:
```python
from toon import encode, decode

# Encode Python dict to TOON
data = {
    'products': [
        {'sku': 'LAP-001', 'name': 'Gaming Laptop', 'price': 1299.99},
        {'sku': 'MOU-042', 'name': 'Wireless Mouse', 'price': 29.99}
    ]
}

toon_string = encode(data)
print(toon_string)
# Output:
# products[2]{sku,name,price}:
...
```

...

</details>

### martor

Django Markdown Editor

`pip install martor` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 13956 · last release 2026-10-31 · [PyPI](https://pypi.org/project/martor/) · [docs](https://github.com/agusmakmun/django-markdown-editor?tab=readme-ov-file#installation) · [source](https://github.com/agusmakmun/django-markdown-editor)

_README extract left out: share-alike licence._

### metaclass-registry

Zero-boilerplate metaclass-driven plugin registry system with lazy discovery and caching

`pip install metaclass-registry` · installs (wheel) · licence: MIT License · rank 13957 · last release 2026-10-16 · [PyPI](https://pypi.org/project/metaclass-registry/) · [docs](https://metaclass-registry.readthedocs.io) · [source](https://github.com/OpenHCSDev/metaclass-registry)

<details><summary>README extract</summary>

Zero-boilerplate metaclass-driven plugin registry system with lazy discovery and caching

Features:
- Zero Boilerplate: No custom metaclasses, no manual registry creation, just class attributes
- Lazy Discovery: Plugins discovered automatically on first access ...

Example:
```python
from metaclass_registry import AutoRegisterMeta, RegistryFamily

# Define the nominal family and its semantic key axis.
class PluginBase(metaclass=AutoRegisterMeta):
    registry_family = RegistryFamily(
        "plugin_name",
        registry_name="plugin",
    )
    registry = {}  # Local script: no package discovery required.
...
```

...

</details>

### anta

Arista Network Test Automation (ANTA) Framework

`pip install anta` · installs (wheel) · licence: Apache-2.0 · rank 13960 · last release 2026-09-10 · [PyPI](https://pypi.org/project/anta/)

<details><summary>README extract</summary>

<!--
 ~ Copyright (c) 2023-2026 Arista Networks, Inc.
 ~ Use of this source code is governed by the Apache License 2.0
 ~ that can be found in the LICENSE file.

| Code | |

| License | |
| GitHub | |
| PyPI | |

ANTA is a Python framework that automates tests for Arista devices. ...

Sections: Arista Network Test Automation (ANTA) Framework, Documentation

</details>

### pymqi

The development of this product is currently on hold.

`pip install pymqi` · installs from source (sdist only) · licence: Python Software Foundation License · rank 13971 · last release 2025-11-18 · [PyPI](https://pypi.org/project/pymqi/)

<details><summary>README extract</summary>

The development of this product is currently on hold.

</details>

### django-valkey

a valkey backend for django

`pip install django-valkey` · installs (wheel) · licence: BSD-3-Clause · rank 13978 · last release 2026-05-06 · [PyPI](https://pypi.org/project/django-valkey/) · [docs](https://django-valkey.readthedocs.io/en/latest/) · [source](https://github.com/django-commons/django-valkey)

<details><summary>README extract</summary>

django-valkey is a BSD licensed, full featured Valkey cache and session backend
for Django.

this project is a fork of the wonderful django-redis project.
they wrote all the good codes.

Features:
- Valkey is a free licenced and well maintained key/value database
- Uses native valkey-py url notation connection strings
- async support
- Pluggable clients
- Pluggable parsers
- Pluggable serializers ...

Sections: Valkey cache backend for Django, Introduction, Why use django-valkey?, Requirements, User guide, Documentation, Todo

</details>

### cachettl

cachettl is an elegant LRU TTL cache decorator that also works with asyncio. It has the cache_info(), cache_clear() methods and access to the remainingttl property.

`pip install cachettl` · installs from source (sdist only) · licence: MIT License · rank 13986 · last release 2024-07-06 · [PyPI](https://pypi.org/project/cachettl/) · [source](https://github.com/rabuchaim/cachettl)

<details><summary>README extract</summary>

An elegant LRU TTL Cache decorator that also works with asyncio. It has the cache_info(), cache_clear() methods and access to the remainingttl property.

More info about LRU (Last Recent Used) cache:

Example:
```python
@cachettl(ttl=10)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(print_datetime.cache_info()) # Displays cache statistics

print(print_datetime.cache_info().remainingttl) # Displays the remaining time-to-live

print_datetime.cache_clear() # Clear the cache
```

...

</details>

### python-statsd

A statsd client: send counters, gauges and timers over UDP to statsd and on to Graphite.

`pip install python-statsd` · installs (wheel) · licence: BSD-3-Clause · rank 13988 · last release 2026-10-28 · [PyPI](https://pypi.org/project/python-statsd/) · [docs](https://python-statsd.readthedocs.io/)

<details><summary>README extract</summary>

Type checked: mypy, basedpyright, pyrefly and ty

`python-statsd` is a client for statsd,
the metrics aggregation daemon that started at Etsy and now lives in its own
organisation, sitting in front of Graphite. It supports Python
3.10 and newer, and it has no dependencies.

Two metrics, two UDP packets, nothing blocking. ...

Example:
```python
import statsd

counter = statsd.Counter('app')
counter += 1

with statsd.Timer('app').time('render'):
    pass  # the work you are measuring
```

Sections: python-statsd, What goes on the wire, The metric types, See it working, Configuration, Documentation, Note on the package name, Links

</details>

### boltz-api

The official Python library for the boltz API

`pip install boltz-api` · installs (wheel) · licence: Apache Software License · rank 14003 · last release 2026-08-28 · [PyPI](https://pypi.org/project/boltz-api/) · [source](https://github.com/boltz-bio/boltz-api-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Boltz Python library provides convenient access to the Boltz REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from boltz_api import Boltz

client = Boltz(
    api_key=os.environ.get("BOLTZ_API_KEY"),  # This is the default and can be omitted
)

response = client.predictions.structure_and_binding.start(
    input={
        "entities": [
            {
                "chain_ids": ["string"],
                "type": "protein",
...
```

...

</details>

### filemagic

A Python API for libmagic, the library behind the Unix file command

`pip install filemagic` · installs from source (sdist only) · licence: Apache Software License · rank 14035 · last release 2013-05-29 · [PyPI](https://pypi.org/project/filemagic/)

<details><summary>README extract</summary>

.. _background:

Background

`libmagic < is the library that commonly
supports the *file* command on Unix system, other than Max OSX which has its
own implementation. The library handles the loading of *database* files that
describe the magic numbers used to identify various file types, as well as the
associated mime types. ...

</details>

### configparser2

This library brings the updated configparser from Python 3.5 to Python 2.6-3.5.

`pip install configparser2` · installs from source (sdist only) · licence: MIT License · rank 14072 · last release 2015-05-12 · [PyPI](https://pypi.org/project/configparser2/)

<details><summary>README extract</summary>

configparser2 is derived from Lukasz Langa's configparser mercurial repo. The
only difference is a name is not conflicting with the default python3
configparser.

Source Code for configparser2 is on
Github.

Features:
Whereas almost completely compatible with its older brother, `configparser2`
sports a bunch of interesting new features:

* there's now one default `ConfigParser` class, which basically is the old
 `SafeConfigParser` with a bunch of tweaks which ...

Example:
```python
from backports import configparser2
```

Sections: configparser2, Source Code, Docs for configparser, Why you'll love `configparser2`, A few words about Unicode, Versioning, Maintenance, 4.0.0, 3.5.0, 3.5.0b2, 3.5.0b1, 3.3.0r2, 3.3.0r1, 3.2.0r3

</details>

### privy-client

The official Python library for the Privy API API

`pip install privy-client` · installs (wheel) · licence: Apache Software License · rank 14073 · last release 2026-09-08 · [PyPI](https://pypi.org/project/privy-client/) · [source](https://github.com/privy-io/python-sdk)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

The Privy API Python library provides convenient access to the Privy API REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by httpx.

It is generated with Stainless. ...

Example:
```python
import os
from privy import PrivyAPI

client = PrivyAPI(
    app_id=os.environ.get("PRIVY_APP_ID"),  # This is the default and can be omitted
    app_secret=os.environ.get("PRIVY_APP_SECRET"),  # This is the default and can be omitted
    # defaults to "production".
    environment="staging",
)

wallet = client.wallets.get(
...
```

...

</details>

### frfr

Lightweight runtime type validation for Python. For real.

`pip install frfr` · installs (wheel) · licence: MIT · rank 14080 · last release 2026-03-27 · [PyPI](https://pypi.org/project/frfr/) · [docs](https://github.com/joshgreaves/frfr#readme) · [source](https://github.com/joshgreaves/frfr)

<details><summary>README extract</summary>

lightweight runtime validation. actually valid. for real.

frfr (for real for real) validates your data at runtime against Python types. you pass a type and some data, and it either gives you back a properly typed instance or tells you exactly why your data is cap.

that's it. that's the whole api.

Example:
```python
import dataclasses
from typing import Literal

import frfr

@dataclasses.dataclass
class Address:
    street: str
    city: str
    country: str = "US"

@dataclasses.dataclass
class Person:
    name: str
    address: Address | None
    role: Literal["admin", "user", "guest"]
    tags: list[str]

data = {
    "name": "bestie",
...
```

...

</details>

### django-debug-toolbar-request-history

Request History Panel for Django Debug Toolbar

`pip install django-debug-toolbar-request-history` · installs (wheel) · licence: BSD License · rank 14101 · last release 2021-10-19 · [PyPI](https://pypi.org/project/django-debug-toolbar-request-history/)

### PowerPlatform-Dataverse-Client

Python SDK for Microsoft Dataverse

`pip install PowerPlatform-Dataverse-Client` · installs (wheel) · licence: MIT · rank 14107 · last release 2026-10-07 · [PyPI](https://pypi.org/project/PowerPlatform-Dataverse-Client/) · [docs](https://github.com/microsoft/PowerPlatform-DataverseClient-Python#readme) · [source](https://github.com/microsoft/PowerPlatform-DataverseClient-Python.git)

<details><summary>README extract</summary>

The Dataverse SDK for Python lets Python developers access, manage, and manipulate Microsoft Dataverse business data using familiar Python syntax — no .NET knowledge required. It wraps the Dataverse Web API in a single typed client that works with tables and records as native Python dictionaries and pandas DataFrames. ...

Features:
- CRUD & bulk — single records plus native `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` / `BulkDelete`.
- Fluent QueryBuilder — type-safe `col()` filters; plus read-only SQL and FetchXML. ...

Example:
```python
from azure.identity import InteractiveBrowserCredential

# Local development: opens a browser to sign in
credential = InteractiveBrowserCredential()

# Production (unattended) alternatives:
...

</details>

### trame-rca

Remote Controlled Area widget for trame

`pip install trame-rca` · installs (wheel) · licence: Apache Software License · rank 14111 · last release 2026-10-09 · [PyPI](https://pypi.org/project/trame-rca/)

<details><summary>README extract</summary>

Remote Controlled Area widget for trame provide components
and communication infrastructure to display remote generated
image based content while allowing interaction forwarding
such as mouse, touch and multi-pointer devices.

This library aims to provide a core that can then be extended
or specialized for any backend. ...

Sections: Remote Controlled Area, Optional dependencies, TurboJPEG, Video encoding with VTKStreaming

</details>

### kdtree

A Python implementation of a kd-tree

`pip install kdtree` · installs (wheel) · licence: ISC License (ISCL) · rank 14117 · last release 2026-11-04 · [PyPI](https://pypi.org/project/kdtree/)

<details><summary>README extract</summary>

This package provides a simple implementation of a kd-tree in Python.

</details>

### bt

A flexible backtesting framework for Python

`pip install bt` · installs (wheel) · licence: MIT License · rank 14138 · last release 2026-10-10 · [PyPI](https://pypi.org/project/bt/) · [docs](https://pmorissette.github.io/bt/) · [source](https://github.com/pmorissette/bt)

<details><summary>README extract</summary>

Example:
```python
import numpy as np
import pandas as pd

import bt

prices = pd.DataFrame(
    {
        "asset_a": np.linspace(100, 120, 252),
        "asset_b": np.linspace(100, 110, 252),
    },
    index=pd.bdate_range("2020-01-01", periods=252),
)

strategy = bt.Strategy(
    "equal_weight",
    [
        bt.algos.RunMonthly(),
        bt.algos.SelectAll(),
...
```

Sections: A first backtest, Explore the documentation

</details>

### octostar-python-client

A client library for accessing Octostar API

`pip install octostar-python-client` · installs (wheel) · licence: MIT · rank 14153 · last release 2026-11-08 · [PyPI](https://pypi.org/project/octostar-python-client/) · [source](https://github.com/Octostarco/octostar-api)

<details><summary>README extract</summary>

A client library for accessing Octostar API

Example:
```python
from octostar import Client

client = Client(base_url="
```

Sections: octostar-python-client, Usage, Releasing

</details>

