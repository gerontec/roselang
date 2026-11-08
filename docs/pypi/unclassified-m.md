# Unclassified / M (part 1 of 3)

[Index](README.md) · 770 packages in this topic, by downloads.

part 1 · [part 2](unclassified-m-2.md) · [part 3](unclassified-m-3.md)

### multidict

multidict implementation

`pip install multidict` · installs (wheel) · licence: Apache-2.0 · rank 55 · last release 2026-10-24 · [PyPI](https://pypi.org/project/multidict/)

<details><summary>README extract</summary>

Multidict is dict-like collection of *key-value pairs* where key
might occur more than once in the container.

*HTTP Headers* and *URL query string* require specific data structure:
*multidict*. It behaves mostly like a regular `dict` but it may have
several *values* for the same *key* and *preserves insertion ordering*. ...

Example:
```python
>>> dct = CIMultiDict(key='val')
>>> 'Key' in dct
True
>>> dct['Key']
'val'
```

Sections: multidict, Introduction

</details>

### mcp

Model Context Protocol SDK

`pip install mcp` · installs (wheel) · licence: MIT License · rank 116 · last release 2026-10-02 · [PyPI](https://pypi.org/project/mcp/) · [docs](https://py.sdk.modelcontextprotocol.io/) · [source](https://github.com/modelcontextprotocol/python-sdk)

<details><summary>README extract</summary>

Python implementation of the Model Context Protocol (MCP)

[][pypi-url]
[][mit-url]
[][python-url]
[][docs-url]
[][protocol-url]
[][spec-url]

The documentation lives at .

It has a Get started guide, What's new in v2, the API reference, and the migration guide. ...

Example:
```python
from mcp.server import MCPServer

mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

Sections: MCP Python SDK, Documentation, What is MCP?, Requirements, A server in 15 lines, A client in 10 lines

</details>

### msal

The Microsoft Authentication Library (MSAL) for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry standard OAuth2 and OpenID Connect.

`pip install msal` · installs (wheel) · licence: MIT License · rank 194 · last release 2026-09-17 · [PyPI](https://pypi.org/project/msal/) · [docs](https://msal-python.readthedocs.io/)

<details><summary>README extract</summary>

| `dev` branch | Reference Docs | # of Downloads per different platforms | # of Downloads per recent MSAL versions | Benchmark Diagram |

 | | | | 📉

The Microsoft Authentication Library for Python enables applications to integrate with the Microsoft identity platform. ...

Example:
```python
from msal import PublicClientApplication
app = PublicClientApplication(
    "your_client_id",
    authority="
```

Sections: Microsoft Authentication Library (MSAL) for Python, Versions, Usage, Migrating from ADAL, Roadmap, Samples and Documentation, Submit Feedback

</details>

### msal-extensions

Microsoft Authentication Library extensions (MSAL EX) provides a persistence API that can save your data on disk, encrypted on Windows, macOS and Linux. Concurrent data access will be coordinated by a file lock mechanism.

`pip install msal-extensions` · installs (wheel) · licence: MIT License · rank 247 · last release 2025-03-14 · [PyPI](https://pypi.org/project/msal-extensions/)

<details><summary>README extract</summary>

The Microsoft Authentication Extensions for Python offers secure mechanisms for client applications to perform cross-platform token cache serialization and persistence. It gives additional support to the Microsoft Authentication Library for Python (MSAL). ...

Example:
```python
def build_persistence(location, fallback_to_plaintext=False):
    """Build a suitable persistence instance based your current OS"""
    try:
        return build_encrypted_persistence(location)
    except:
        if not fallback_to_plaintext:
            raise
        logging.warning("Encryption unavailable. Opting in to plain text.")
...
```

Sections: Microsoft Authentication Extensions for Python, Versions, Usage, Creating an encrypted token cache file to be used by MSAL

</details>

### mcp-types

Model Context Protocol wire types

`pip install mcp-types` · installs (wheel) · licence: MIT License · rank 280 · last release 2026-10-02 · [PyPI](https://pypi.org/project/mcp-types/) · [docs](https://py.sdk.modelcontextprotocol.io/) · [source](https://github.com/modelcontextprotocol/python-sdk)

<details><summary>README extract</summary>

The wire types for the Model Context Protocol.

This package holds the protocol message models, JSON-RPC envelope types, per-version
surface validators, and the protocol-version registry. ...

Example:
```python
from mcp_types import Tool, CallToolRequest
from mcp_types.version import LATEST_PROTOCOL_VERSION
```

</details>

### marshmallow

A lightweight library for converting complex datatypes to and from native Python datatypes.

`pip install marshmallow` · installs (wheel) · licence: MIT · rank 306 · last release 2026-11-04 · [PyPI](https://pypi.org/project/marshmallow/) · [source](https://github.com/marshmallow-code/marshmallow)

<details><summary>README extract</summary>

marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

In short, marshmallow schemas can be used to:

- Validate input data.
- Deserialize input data to app-level objects.
- Serialize app-level objects to primitive Python types. ...

Example:
```python
from datetime import date
from pprint import pprint

from marshmallow import Schema, fields

class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

bowie = dict(name="David Bowie")
...
```

Sections: marshmallow: simplified object serialization, Get it now, Documentation, Ecosystem, Backers, Project Links

</details>

### mypy-boto3-s3

Type annotations for boto3 S3 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-s3` · installs (wheel) · licence: MIT · rank 536 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mypy-boto3-s3/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 S3 1.43.106
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-s3 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### ml-dtypes

ml_dtypes is a stand-alone implementation of several NumPy dtype extensions used in machine learning.

`pip install ml-dtypes` · installs (wheel) · licence: Apache-2.0 · rank 583 · last release 2026-08-13 · [PyPI](https://pypi.org/project/ml-dtypes/) · [source](https://github.com/jax-ml/ml_dtypes)

<details><summary>README extract</summary>

`ml_dtypes` is a stand-alone implementation of several NumPy dtype extensions used in machine learning libraries, including:

 an alternative to the standard `float16` format
- 8-bit floating point representations, parameterized by number of exponent and
 mantissa bits, as well as the bias (if any) and representability of infinity,
 NaN, and ...

Example:
```python
>>> from ml_dtypes import bfloat16
>>> import numpy as np
>>> np.zeros(4, dtype=bfloat16)
array([0, 0, 0, 0], dtype=bfloat16)
```

Sections: ml_dtypes, Example Usage, Specifications of implemented floating point formats, `bfloat16`, `float4_e2m1fn`, `float6_e2m3fn`, `float6_e3m2fn`, `float8_e3m4`, `float8_e4m3`, `float8_e4m3b11fnuz`, `float8_e4m3fn`, `float8_e4m3fnuz`, `float8_e5m2`, `float8_e5m2fnuz`

</details>

### mashumaro

Fast and well tested serialization library

`pip install mashumaro` · installs (wheel) · licence: Apache-2.0 · rank 690 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mashumaro/) · [source](https://github.com/Fatal1ty/mashumaro)

<details><summary>README extract</summary>

Work with familiar Python data structures and type annotations. Mashumaro
generates specialized encoders and decoders for them — no handwritten schemas
or framework-specific models required.

Documentation ·
Benchmarks ·
Who uses mashumaro? ·
Releases

Features:
- Standard Python first. Keep ordinary dataclasses, collections, and type
 annotations; add a lightweight mixin only when you want methods on a model.
- Fast by design. ...

Example:
```python
from dataclasses import dataclass
from datetime import datetime

from mashumaro.mixins.json import DataClassJSONMixin

@dataclass
class Event(DataClassJSONMixin):
    name: str
    starts_at: datetime
    speakers: list[str]

event = Event(
    name="PyCon",
    starts_at=datetime(2026, 5, 13, 9, 0),
    speakers=["Alice", "Bob"],
)

...
```
...

</details>

### mergedeep

A deep merge function for 🐍.

`pip install mergedeep` · installs (wheel) · licence: MIT License · rank 740 · last release 2021-02-05 · [PyPI](https://pypi.org/project/mergedeep/)

<details><summary>README extract</summary>

A deep merge function for 🐍.

Check out the mergedeep docs

Example:
```python
from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merged = merge({}, a, b, c)

print(merged)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
```

Sections: mergedeep, Usage, Merge strategies

</details>

### markitdown

Utility tool for converting various files to Markdown

`pip install markitdown` · installs (wheel) · licence: MIT · rank 886 · last release 2026-10-21 · [PyPI](https://pypi.org/project/markitdown/) · [docs](https://github.com/microsoft/markitdown#readme) · [source](https://github.com/microsoft/markitdown)

<details><summary>README extract</summary>

> [!TIP]
> MarkItDown is a Python package and command-line utility for converting various files to Markdown (e.g., for indexing, text analysis, etc).
> For more information, and full documentation, see the project README.md on GitHub.

> [!IMPORTANT]
> MarkItDown performs I/O with the privileges of the current process. ...

Example:
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("test.xlsx")
print(result.markdown)
```

Sections: MarkItDown, Usage, Command-Line, Python API, More Information, Trademarks

</details>

### msoffcrypto-tool

Python tool and library for decrypting and encrypting MS Office files using a password or other keys

`pip install msoffcrypto-tool` · installs (wheel) · licence: MIT License · rank 912 · last release 2026-11-03 · [PyPI](https://pypi.org/project/msoffcrypto-tool/)

<details><summary>README extract</summary>

msoffcrypto-tool is a Python tool and library for decrypting and encrypting MS Office files using a password or other keys.

Example:
```python
import msoffcrypto

encrypted = open("encrypted.docx", "rb")
file = msoffcrypto.OfficeFile(encrypted)

file.load_key(password="Passw0rd")  # Use password

with open("decrypted.docx", "wb") as f:
    file.decrypt(f)

encrypted.close()
```

Sections: msoffcrypto-tool, Examples, As CLI tool (with password), Decryption, Encryption (OOXML only, experimental), As library, MS-OFFCRYPTO specs, Other, Tests, Todo, Resources, Alternatives

</details>

### mammoth

Convert Word documents from docx to simple and clean HTML and Markdown

`pip install mammoth` · installs (wheel) · licence: BSD License · rank 917 · last release 2026-09-26 · [PyPI](https://pypi.org/project/mammoth/)

<details><summary>README extract</summary>

Mammoth is designed to convert .docx documents, such as those created by
Microsoft Word, Google Docs and LibreOffice, and convert them to HTML.
Mammoth aims to produce simple and clean HTML by using semantic
information in the document, and ignoring other details. ...

Example:
```python
import mammoth

with open("document.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
```

Sections: Mammoth .docx to HTML converter, Usage, CLI, Images, Styles, Markdown, Library, Basic conversion, Custom style map, Custom image handlers, Bold, Italic, Underline, Strikethrough

</details>

### mini-swe-agent

Mini SWE Agent - A simple AI software engineering agent

`pip install mini-swe-agent` · installs (wheel) · licence: MIT License · rank 923 · last release 2026-07-23 · [PyPI](https://pypi.org/project/mini-swe-agent/) · [docs](https://mini-swe-agent.com/latest/) · [source](https://github.com/SWE-agent/mini-swe-agent)

<details><summary>README extract</summary>

📣 mini-swe-agent now powers Ramp SWE-Bench

📣 mini-swe-agent beats Claude Code and Codex on DeepSWE

📣 Run mini-swe-agent on our new & extremely challenging benchmark, ProgramBench

📣 New tutorial on building minimal AI agents

> [!WARNING]
> This is mini-swe-agent v2. Read the migration guide. For the previous version, check out the v1 branch. ...

Example:
```python
agent = DefaultAgent(
    LitellmModel(model_name=...),
    LocalEnvironment(),
)
agent.run("Write a sudoku game")
```

Sections: The minimal AI software engineering agent, Let's get started!, Attribution

</details>

### mistralai

Python Client SDK for the Mistral AI API.

`pip install mistralai` · installs (wheel) · licence: not stated · rank 1039 · last release 2026-11-01 · [PyPI](https://pypi.org/project/mistralai/) · [source](https://github.com/mistralai/client-python.git)

<details><summary>README extract</summary>

Before you begin, you will need a Mistral AI API key.

1. Get your own Mistral API Key:
2. Set your Mistral API Key as an environment variable. You only need to do this once.

Example:
```python
# !/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
# "mistralai",
# ]
# ///

from mistralai.client import Mistral

sdk = Mistral(
  # SDK arguments
)

# Rest of script here...
```

Sections: Mistral Python Client, API Key Setup, Service-account token, Summary, uv, PIP, Poetry, Shell and script usage with `uv`, Agents extra dependencies, Voice agents extra dependencies, Additional packages, SDK Example Usage, Create Chat Completions, Upload a file

</details>

### mypy-boto3-sqs

Type annotations for boto3 SQS 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sqs` · installs (wheel) · licence: MIT · rank 1116 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-sqs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SQS 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sqs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-dynamodb

Type annotations for boto3 DynamoDB 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dynamodb` · installs (wheel) · licence: MIT · rank 1154 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-dynamodb/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 DynamoDB 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dynamodb docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-lambda

Type annotations for boto3 Lambda 1.43.123 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-lambda` · installs (wheel) · licence: MIT · rank 1186 · last release 2026-10-30 · [PyPI](https://pypi.org/project/mypy-boto3-lambda/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Lambda 1.43.123
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-lambda docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### motor

Non-blocking MongoDB driver for Tornado or asyncio

`pip install motor` · installs (wheel) · licence: Apache Software License · rank 1229 · last release 2025-05-14 · [PyPI](https://pypi.org/project/motor/) · [docs](https://motor.readthedocs.io) · [source](https://github.com/mongodb/motor)

<details><summary>README extract</summary>

> [!WARNING]
> Motor will be deprecated on May 14th, 2026, one year after the production release of the PyMongo Async driver.
> Critical bug fixes will be made until May 14th, 2027.
> We strongly recommend that Motor users migrate to the PyMongo Async driver while Motor is still supported.
> To learn more, see the migration guide: ...

Sections: Motor, About, Bugs / Feature Requests, How To Ask For Help, Dependencies, Examples, Documentation, Learning Resources

</details>

### mypy-boto3-secretsmanager

Type annotations for boto3 SecretsManager 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-secretsmanager` · installs (wheel) · licence: MIT · rank 1249 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-secretsmanager/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 SecretsManager 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-secretsmanager docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-cloudformation

Type annotations for boto3 CloudFormation 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cloudformation` · installs (wheel) · licence: MIT · rank 1297 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-cloudformation/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudFormation 1.43.110 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cloudformation docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-ec2

Type annotations for boto3 EC2 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ec2` · installs (wheel) · licence: MIT · rank 1307 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-ec2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EC2 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ec2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-kiota-http

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-http` · installs (wheel) · licence: MIT License · rank 1315 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-http/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_http)

<details><summary>README extract</summary>

The Microsoft Kiota HTTP Library is a python HTTP implementation with HTTPX library.

A Kiota generated project will need a reference to a http package to make HTTP requests to an API endpoint.

Read more about Kiota here.

In order to use this library, install the package by running:

Sections: Microsoft Kiota HTTP library, Using the Microsoft Kiota HTTP library, Trademarks

</details>

### microsoft-kiota-authentication-azure

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-authentication-azure` · installs (wheel) · licence: MIT License · rank 1317 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-authentication-azure/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_authentication_azure)

<details><summary>README extract</summary>

The Microsoft Kiota Authentication Azure Library is an implementation to authenticate HTTP requests using @azure/identity.

A Kiota generated project will need a reference to an authentication provider to make calls to an API endpoint.

Read more about Kiota here.

In order to use this library, install the package by running: ...

Sections: Microsoft Kiota Authentication Azure Library for Python, Using the Microsoft Kiota Authentication Azure library, Trademarks

</details>

### microsoft-kiota-abstractions

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-abstractions` · installs (wheel) · licence: MIT License · rank 1322 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-abstractions/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_abstractions)

<details><summary>README extract</summary>

The Microsoft Kiota abstractions library for Python is the python package that defines the basic constructs Kiota projects need once an SDK has been generated from an OpenAPI definition.

A Kiota generated project will need a reference to the abstraction package to build and run.

Read more about Kiota here. ...

Sections: Microsoft Kiota Abstractions Library for Python, Using the Abstractions Library, Trademarks

</details>

### mypy-boto3-rds

Type annotations for boto3 RDS 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-rds` · installs (wheel) · licence: MIT · rank 1329 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-rds/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 RDS 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-rds docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-protobuf

Generate mypy stub files from protobuf specs

`pip install mypy-protobuf` · installs (wheel) · licence: Apache License 2.0 · rank 1330 · last release 2026-04-28 · [PyPI](https://pypi.org/project/mypy-protobuf/)

<details><summary>README extract</summary>

mypy-protobuf: Generate mypy stub files from protobuf specs

===========================================================

2.10 is the last version of mypy-protobuf which supports targeting python 2.7.

Built originally with love at Dropbox

See Changelog for recent changes.

Earlier releases might work, but aren't tested

- protoc >= 32.0 ...

Features:
See Changelog for full listing

Example:
```python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Edition version of proto2 file"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

...
```

...

</details>

### mypy-boto3-sts

Type annotations for boto3 STS 1.43.94 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sts` · installs (wheel) · licence: MIT · rank 1349 · last release 2026-09-14 · [PyPI](https://pypi.org/project/mypy-boto3-sts/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 STS 1.43.94
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sts docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### marshmallow-enum

Enum field for Marshmallow

`pip install marshmallow-enum` · installs (wheel) · licence: MIT · rank 1356 · last release 2019-08-21 · [PyPI](https://pypi.org/project/marshmallow-enum/)

<details><summary>README extract</summary>

Enum field for use with Marshmallow.

Example:
```python
from enum import Enum

class StopLight(Enum):
    green = 1
    yellow = 2
    red = 3
```

Sections: marshmallow-enum, Using The Field, Customizing loading and dumping behavior, Custom Error Message, Version 1.5, Version 1.4

</details>

### microsoft-kiota-serialization-json

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-serialization-json` · installs (wheel) · licence: MIT License · rank 1359 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-serialization-json/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_serialization_json)

<details><summary>README extract</summary>

The Microsoft Kiota Serialization Library for JSON is a python implementation to serialize/deserialize JSON.

A Kiota generated project will need a reference to a json serialization package to handle json payloads from an API endpoint.

Read more about Kiota here.

In order to use this library, install the package by running:

Sections: Microsoft Kiota Serialization library for JSON, Using the Microsoft Kiota Serialization JSON library, Trademarks

</details>

### microsoft-kiota-serialization-text

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-serialization-text` · installs (wheel) · licence: MIT License · rank 1361 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-serialization-text/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_serialization_text)

<details><summary>README extract</summary>

The Microsoft Kiota Text Serialization Library is a python implementation to serialize/deserialize text/plain.

A Kiota generated project will need a reference to a json serialization package to handle json payloads from an API endpoint.

Read more about Kiota here.

In order to use this library, install the package by running:

Sections: Microsoft Kiota Text Serialization library, Using the Microsoft Kiota Text Serialization library, Trademarks

</details>

### metricflow

Translates a simple metric definition into reusable SQL and executes it against the SQL engine of your choice.

`pip install metricflow` · installs (wheel) · licence: Apache-2.0 · rank 1362 · last release 2026-09-10 · [PyPI](https://pypi.org/project/metricflow/) · [docs](https://docs.getdbt.com/docs/build/about-metricflow) · [source](https://github.com/dbt-labs/metricflow)

<details><summary>README extract</summary>

Build and maintain all of your metric logic in code.

See our latest updates in the Metricflow Changelog!

MetricFlow is a semantic layer that simplifies defining and managing metrics. It compiles these metric definitions into clear, reusable SQL, ensuring consistent and accurate results when analyzing data by relevant attributes (dimensions). ...

Sections: Welcome to MetricFlow, Licensing, Open Semantic Interchange (OSI) Initiative, Getting Started, Tutorial, Resources

</details>

### msgraph-core

Core component of the Microsoft Graph Python SDK

`pip install msgraph-core` · installs (wheel) · licence: MIT · rank 1384 · last release 2026-10-06 · [PyPI](https://pypi.org/project/msgraph-core/) · [docs](https://github.com/microsoftgraph/msgraph-sdk-python-core/docs) · [source](https://github.com/microsoftgraph/msgraph-sdk-python-core)

<details><summary>README extract</summary>

The Microsoft Graph Core Python Client Library contains core classes used by Microsoft Graph Python Client Library to send native HTTP requests to Microsoft Graph API.

> NOTE:
> This is a new major version of the Python Core library for Microsoft Graph based on the Kiota project. We recommend to use this library with the full Python SDK. ...

Example:
```python
# Using EnvironmentCredential for demonstration purposes.
# There are many other options for getting an access token. See the following for more information.
#
from azure.identity.aio import EnvironmentCredential
from msgraph_core.authentication import AzureIdentityAuthenticationProvider

credential=EnvironmentCredential()
...
```

...

</details>

### microsoft-kiota-serialization-multipart

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-serialization-multipart` · installs (wheel) · licence: MIT License · rank 1466 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-serialization-multipart/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_serialization_multipart)

<details><summary>README extract</summary>

The Multipart Serialization Library for Python is the python `multipart/form-data` serialization library implementation.

A Kiota generated project will need a reference to a multipart serialization package to handle multipart payloads from a supporting API endpoint.

Read more about Kiota here. ...

Sections: Microsoft Kiota Multipart Serialization Library for Python, Using the Microsoft Kiota Multipart Serialization Library, Trademarks

</details>

### microsoft-kiota-serialization-form

Core abstractions for kiota generated libraries in Python

`pip install microsoft-kiota-serialization-form` · installs (wheel) · licence: MIT License · rank 1468 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-serialization-form/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python Import-Name: kiota_serialization_form)

<details><summary>README extract</summary>

The Form Serialization Library for Python is the python `application/x-www-form-urlencoded` serialization library implementation.

A Kiota generated project will need a reference to a form serialization package to handle `application/x-www-form-urlencoded payloads` from a supporting API endpoint.

Read more about Kiota here. ...

</details>

### mutmut

mutation testing for Python 3

`pip install mutmut` · installs (wheel) · licence: BSD-3-Clause · rank 1473 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mutmut/) · [docs](https://mutmut.readthedocs.io/en/latest/) · [source](https://github.com/boxed/mutmut)

<details><summary>README extract</summary>

Mutmut is a mutation testing system for Python, with a strong focus on ease
of use. If you don't know what mutation testing is try starting with
this article.

Some highlight features:

- Found mutants can be applied on disk with a simple command making it very
 easy to work with the results ...

Example:
```python
    main process (clean) -> fork server (imports pytest) -> N mutant workers

Because the fork server only imports and forks, and never runs a test
itself, every worker starts from the same predictable state. This is the
same design as the `forkserver` start method in Python's
`multiprocessing`, and it is still only one pytest import for the whole
...
```

...

</details>

### mypy-boto3-glue

Type annotations for boto3 Glue 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-glue` · installs (wheel) · licence: MIT · rank 1484 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-glue/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Glue 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-glue docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### msgraph-sdk

The Microsoft Graph Python SDK

`pip install msgraph-sdk` · installs (wheel) · licence: MIT · rank 1549 · last release 2026-10-22 · [PyPI](https://pypi.org/project/msgraph-sdk/) · [docs](https://github.com/microsoftgraph/msgraph-sdk-python/docs) · [source](https://github.com/microsoftgraph/msgraph-sdk-python)

<details><summary>README extract</summary>

Get started with the Microsoft Graph SDK for Python by integrating the Microsoft Graph API into your Python application.

> Note:
> * This SDK allows you to build applications using the v1.0 of Microsoft Graph. If you want to try the latest Microsoft Graph APIs, try the beta SDK.

Example:
```python
import asyncio

from azure.identity.aio import ClientSecretCredential

credential = ClientSecretCredential("tenantID",
                                    "clientID",
                                    "clientSecret")
scopes = ['
```

...

</details>

### mixpanel

Official Mixpanel library for Python

`pip install mixpanel` · installs (wheel) · licence: Apache-2.0 · rank 1584 · last release 2026-10-13 · [PyPI](https://pypi.org/project/mixpanel/)

### marko

A markdown parser with high extensibility.

`pip install marko` · installs (wheel) · licence: MIT · rank 1629 · last release 2026-10-27 · [PyPI](https://pypi.org/project/marko/) · [docs](https://marko-py.readthedocs.io)

<details><summary>README extract</summary>

> A markdown parser with high extensibility.

[][spec]

Marko is a pure Python markdown parser that adheres to the specifications of CommonMark's spec v0.31.2. It has been designed with high extensibility in mind, as detailed in the Extensions section.

Marko requires Python 3.9 or higher.

Features:
Of all the Python markdown parsers available, a common issue is the difficulty for users to add their own features. Additionally, both Python-Markdown and mistune do not comply with CommonMark specifications. ...

Example:
```python
import marko

print(marko.convert(text))
```

Sections: 𝓜𝓪𝓻𝓴𝓸, Why Marko, Use Marko, Extensions

</details>

### mistral_common

Mistral-common is a library of common utilities for Mistral AI.

`pip install mistral_common` · installs (wheel) · licence: Apache-2.0 · rank 1804 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mistral_common/)

<details><summary>README extract</summary>

mistral-common is a set of tools to help you work with Mistral AI models.

We open-source the tokenizers, validation and normalization code that can be used with our models.

This ensures that you can take full advantage of our models for the following features:

- tokenization of text, images and tools calls. ...

Sections: Mistral-common, What is it?, For who ?, How to use it ?

</details>

### magicattr

A getattr and setattr that works on nested objects, lists, dicts, and any combination thereof without resorting to eval

`pip install magicattr` · installs (wheel) · licence: MIT · rank 1880 · last release 2026-10-07 · [PyPI](https://pypi.org/project/magicattr/)

<details><summary>README extract</summary>

A getattr and setattr that works on nested objects, lists,
dictionaries, and any combination thereof without resorting to eval.

It differs from getattr and setattr in that it retains the failure cause
instead of always raising an AttributeError.

Example:
```python
class Person:
    settings = {
        'autosave': True,
        'style': {
            'height': 30,
            'width': 200
        },
        'themes': ['light', 'dark']
    }
    def init(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends

bob = Person(name="Bob", age=31, friends=[])
...
```

Sections: Magicattr, Example, What it can't do?, How does it work?

</details>

### mypy-boto3-ssm

Type annotations for boto3 SSM 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ssm` · installs (wheel) · licence: MIT · rank 1891 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-ssm/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SSM 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ssm docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### methodtools

Expand standard functools to methods

`pip install methodtools` · installs (wheel) · licence: BSD License · rank 1936 · last release 2024-08-23 · [PyPI](https://pypi.org/project/methodtools/)

<details><summary>README extract</summary>

Expand functools features to methods, classmethods, staticmethods and even for
(unofficial) hybrid methods.

For now, methodtools only provides `methodtools.lru_cache`.

Use `methodtools` module instead of `functools` module. Than it will work as
you expected.

Example:
```python
from methodtools import lru_cache

class A(object):

    # cached method. the storage lifetime follows `self` object
    @lru_cache()
    def cached_method(self, args):
        ...

    # cached classmethod. the storage lifetime follows `A` class
    @lru_cache()  # the order is important!
    @classmethod  # always lru_cache on top of classmethod
...
```

Sections: methodtools, See also

</details>

### marshmallow-sqlalchemy

SQLAlchemy integration with the marshmallow (de)serialization library

`pip install marshmallow-sqlalchemy` · installs (wheel) · licence: MIT · rank 1938 · last release 2026-10-19 · [PyPI](https://pypi.org/project/marshmallow-sqlalchemy/) · [source](https://github.com/marshmallow-code/marshmallow-sqlalchemy)

<details><summary>README extract</summary>

Homepage:

SQLAlchemy integration with the marshmallow (de)serialization library.

Example:
```python
import sqlalchemy as sa
from sqlalchemy.orm import (
    DeclarativeBase,
    backref,
    relationship,
    sessionmaker,
)

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

engine = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class Author(Base):
...
```

Sections: marshmallow-sqlalchemy, Declare your models, Generate marshmallow schemas, (De)serialize your data, Get it now, Documentation, Project links

</details>

### mypy-boto3-bedrock-runtime

Type annotations for boto3 BedrockRuntime 1.43.62 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock-runtime` · installs (wheel) · licence: MIT · rank 1951 · last release 2026-07-31 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock-runtime/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 BedrockRuntime 1.43.62 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock-runtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### multipledispatch

Multiple dispatch

`pip install multipledispatch` · installs (wheel) · licence: BSD · rank 1973 · last release 2023-06-27 · [PyPI](https://pypi.org/project/multipledispatch/)

<details><summary>README extract</summary>

A relatively sane approach to multiple dispatch in Python.

This implementation of multiple dispatch is efficient, mostly complete,
performs static analysis to avoid conflicts, and provides optional namespace
support. It looks good too.

See the documentation at

Features:
- Dispatches on all non-keyword arguments

- Supports inheritance

- Supports instance methods

- Supports union types, e.g. `(int, float)`

- Supports builtin abstract classes, e.g. `Iterator, Number, ...`

- Caches for fast repeated lookup ...

Example:
```python
>>> from multipledispatch import dispatch

>>> @dispatch(int, int)
... def add(x, y):
...     return x + y

>>> @dispatch(object, object)
... def add(x, y):
...     return "%s + %s" % (x, y)

>>> add(1, 2)
3

>>> add(1, 'hello')
'1 + hello'
```

...

</details>

### mail-parser

A tool that parses emails by enhancing the Python standard library, extracting all details into a comprehensive object.

`pip install mail-parser` · installs (wheel) · licence: Apache-2.0 · rank 2000 · last release 2026-10-30 · [PyPI](https://pypi.org/project/mail-parser/) · [source](https://github.com/SpamScope/mail-parser)

<details><summary>README extract</summary>

Project website: spamscope.ai/en/

mail-parser is a production-grade, RFC-compliant email parsing library that goes far beyond a
simple wrapper for Python's email module.
It transforms raw email messages into richly structured Python objects with unparalleled precision,
making complex email processing accessible and reliable. ...

Features:
🔒 Security-First Design: Built specifically for email security analysis and digital forensics,
mail-parser excels at detecting malformed structures, hidden content, and RFC non-compliance that
could indicate malicious intent. ...

Example:
```python
import mailparser

mail = mailparser.parse_from_bytes(byte_mail)      # Parse from bytes object
mail = mailparser.parse_from_file(f)               # Parse from file path
...

</details>

### mypy-boto3-ecs

Type annotations for boto3 ECS 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ecs` · installs (wheel) · licence: MIT · rank 2043 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-ecs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ECS 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ecs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-ecr

Type annotations for boto3 ECR 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ecr` · installs (wheel) · licence: MIT · rank 2061 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mypy-boto3-ecr/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ECR 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ecr docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### modelscope

ModelScope: bring the notion of Model-as-a-Service to life.

`pip install modelscope` · installs (wheel) · licence: Apache-2.0 · rank 2126 · last release 2026-10-09 · [PyPI](https://pypi.org/project/modelscope/)

<details><summary>README extract</summary>

Discord

 English |
 中文 |
 日本語

ModelScope is built upon the notion of “Model-as-a-Service” (MaaS). It seeks to bring together most advanced machine learning models from the AI community, and streamlines the process of leveraging AI models in real-world applications. ...

Features:
1. A unified and concise user interface is abstracted for different tasks and different models. Model inferences and training can be implemented by as few as 3 and 10 lines of code, respectively. ...

Example:
```python
>>> from modelscope.pipelines import pipeline
>>> word_segmentation = pipeline('word-segmentation',model='damo/nlp_structbert_word-segmentation_chinese-base')
>>> word_segmentation('今天天气不错，适合出去游玩')
{'output': '今天 天气 不错 ， 适合 出去 游玩'}
```

...

</details>

### mypy-boto3-iam

Type annotations for boto3 IAM 1.43.70 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-iam` · installs (wheel) · licence: MIT · rank 2144 · last release 2026-08-12 · [PyPI](https://pypi.org/project/mypy-boto3-iam/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 IAM 1.43.70
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-iam docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-sns

Type annotations for boto3 SNS 1.43.97 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sns` · installs (wheel) · licence: MIT · rank 2195 · last release 2026-09-17 · [PyPI](https://pypi.org/project/mypy-boto3-sns/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SNS 1.43.97
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sns docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### minimal-snowplow-tracker

A minimal snowplow event tracker for Python. Add analytics to your Python and Django apps, webapps and games

`pip install minimal-snowplow-tracker` · installs from source (sdist only) · licence: Apache Software License · rank 2404 · last release 2018-10-13 · [PyPI](https://pypi.org/project/minimal-snowplow-tracker/)

<details><summary>README extract</summary>

Features:
Add analytics to your Python apps and Python games with the Snowplow event tracker for Python.

With this tracker you can collect event data from your Python-based applications, games or Python web servers/frameworks. ...

Sections: Python Analytics for Snowplow, Overview

</details>

### mypy-boto3-athena

Type annotations for boto3 Athena 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-athena` · installs (wheel) · licence: MIT · rank 2427 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-athena/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Athena 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-athena docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mitmproxy-rs

(no summary)

`pip install mitmproxy-rs` · installs (wheel) · licence: not stated · rank 2444 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mitmproxy-rs/)

### mypy-boto3-kms

Type annotations for boto3 KMS 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kms` · installs (wheel) · licence: MIT · rank 2465 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mypy-boto3-kms/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 KMS 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kms docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcap

MCAP libraries for Python

`pip install mcap` · installs (wheel) · licence: MIT License · rank 2482 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mcap/)

### marshmallow-oneofschema

marshmallow multiplexing schema

`pip install marshmallow-oneofschema` · installs (wheel) · licence: MIT License · rank 2519 · last release 2025-05-08 · [PyPI](https://pypi.org/project/marshmallow-oneofschema/) · [source](https://github.com/marshmallow-code/marshmallow-oneofschema)

<details><summary>README extract</summary>

An extension to marshmallow to support schema (de)multiplexing.

marshmallow is a fantastic library for serialization and deserialization of data.
For more on that project see its GitHub
page or its Documentation.

This library adds a special kind of schema that actually multiplexes other schemas
based on object type. ...

Example:
```python
import marshmallow
import marshmallow.fields
from marshmallow_oneofschema import OneOfSchema

class Foo:
    def init(self, foo):
        self.foo = foo

class Bar:
    def init(self, bar):
        self.bar = bar

class FooSchema(marshmallow.Schema):
    foo = marshmallow.fields.String(required=True)

    @marshmallow.post_load
...
```

Sections: marshmallow-oneofschema, Example

</details>

### mssql-python

A Python library for interacting with Microsoft SQL Server

`pip install mssql-python` · installs (wheel) · licence: not stated · rank 2558 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mssql-python/)

<details><summary>README extract</summary>

Features:
By simplifying the architecture, DDBC delivers:

- Consistency across platforms
- Lower function call overhead
- Zero external dependencies on Windows (`pip install mssql-python` is all you need) ...

Sections: What makes mssql-python different?, Powered by DDBC – Direct Database Connectivity, Why is this architecture important?, Built with PyBind11 + Modern C++ for Performance and Safety, What's new in v1.17.0, Enhancements, Bug Fixes, What's Next

</details>

### marimo

A library for making reactive notebooks and apps

`pip install marimo` · installs (wheel) · licence: Apache-2.0 · rank 2591 · last release 2026-10-19 · [PyPI](https://pypi.org/project/marimo/)

<details><summary>README extract</summary>

A reactive Python notebook that's reproducible, git-friendly, and deployable as scripts or apps.

 Docs ·
 Discord ·
 Examples ·
 Gallery ·
 YouTube

 English
 繁體中文
 简体中文
 日本語
 Español ...

Sections: A reactive programming environment, Quickstart, Questions?, Learn more, Inspiration ✨

</details>

### mypy-boto3-stepfunctions

Type annotations for boto3 SFN 1.43.117 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-stepfunctions` · installs (wheel) · licence: MIT · rank 2595 · last release 2026-10-21 · [PyPI](https://pypi.org/project/mypy-boto3-stepfunctions/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SFN 1.43.117
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-stepfunctions docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-security-utilities-secret-masker

A tool for detecting and masking secrets

`pip install microsoft-security-utilities-secret-masker` · installs (wheel) · licence: MIT · rank 2604 · last release 2025-03-10 · [PyPI](https://pypi.org/project/microsoft-security-utilities-secret-masker/)

<details><summary>README extract</summary>

Example:
```python
from microsoft_security_utilities_secret_masker import SecretMasker, load_regex_patterns_from_json_file

# Load built-in detection rules
precisely_classified_regex_patterns = load_regex_patterns_from_json_file('PreciselyClassifiedSecurityKeys.json')
...
```

Sections: Usage, 1.0.0b4, 1.0.0b3, 1.0.0b2, 1.0.0b1

</details>

### mypy-boto3-logs

Type annotations for boto3 CloudWatchLogs 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-logs` · installs (wheel) · licence: MIT · rank 2614 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-logs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudWatchLogs 1.43.125 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-logs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mapbox-earcut

Python bindings for the mapbox earcut C++ polygon triangulation library

`pip install mapbox-earcut` · installs (wheel) · licence: ISC License (ISCL) · rank 2656 · last release 2026-09-08 · [PyPI](https://pypi.org/project/mapbox-earcut/) · [source](https://github.com/skogler/mapbox_earcut_python)

<details><summary>README extract</summary>

Python bindings for the C++ implementation of the Mapbox Earcut library, which
provides very fast and quite robust triangulation of 2D polygons.

Original code: earcut.hpp

Original description: ...

Example:
```python
import mapbox_earcut as earcut
import numpy as np

# A Nx2 array of vertices. Must be 2D.
verts = np.array([[0, 0], [1, 0], [1, 1]]).reshape(-1, 2)

# An array of end-indices for each ring.
# The first ring is the outer contour of the polygon.
# Subsequent ones are holes.
...
```

</details>

### markdown-to-mrkdwn

A library to convert Markdown to Slack's mrkdwn format

`pip install markdown-to-mrkdwn` · installs (wheel) · licence: MIT License · rank 2672 · last release 2026-05-27 · [PyPI](https://pypi.org/project/markdown-to-mrkdwn/)

<details><summary>README extract</summary>

A lightweight, efficient library for converting standard Markdown to Slack's mrkdwn format. This library helps you maintain consistent formatting when sending messages to Slack from your applications.

Features:
- Fast and lightweight conversion from Markdown to Slack's mrkdwn format
- No external dependencies

 - Headings (H1, H2, H3, H4, H5, H6)
 - Text formatting (bold, italic, strikethrough)
 - Lists (ordered and unordered, with nesting)
 - Ordered ...

Example:
```python
from markdown_to_mrkdwn import SlackMarkdownConverter

# Create a converter instance
converter = SlackMarkdownConverter()

# Convert markdown to mrkdwn
markdown_text = """
# Heading 1
Bold text
- List item
Link
~~Strikethrough text~~
"""
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)
```

...

</details>

### mem0ai

Long-term memory for AI Agents

`pip install mem0ai` · installs (wheel) · licence: Apache-2.0 · rank 2707 · last release 2026-09-25 · [PyPI](https://pypi.org/project/mem0ai/)

<details><summary>README extract</summary>

Learn more
 Join Discord
 Demo

 📄 Benchmarking Mem0's token-efficient memory algorithm →

| Benchmark | Old | New | Tokens | Latency p50 |

| LoCoMo | 71.4 | 92.5 | 7.0K | 0.88s |
| LongMemEval | 67.8 | 94.4 | 6.8K | 1.09s |
| BEAM (1M) | — | 64.1 | 6.7K | 1.00s |
| BEAM (10M) | — | 48.6 | 6.9K | 1.05s | ...

Features:
Core Capabilities:
- Multi-Level Memory: Seamlessly retains User, Session, and Agent state with adaptive personalization
- Developer-Friendly: Intuitive API, cross-platform SDKs, and a fully managed service option

Applications: ...

Example:
```python
from openai import OpenAI
from mem0 import Memory

openai_client = OpenAI()
memory = Memory()

def chat_with_memories(message: str, user_id: str = "default_user") -> str:
    # Retrieve relevant memories
...

</details>

### mypy-boto3-cloudwatch

Type annotations for boto3 CloudWatch 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cloudwatch` · installs (wheel) · licence: MIT · rank 2730 · last release 2026-10-20 · [PyPI](https://pypi.org/project/mypy-boto3-cloudwatch/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudWatch 1.43.116 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cloudwatch docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### MouseInfo

An application to display XY position and RGB color information for the pixel currently under the mouse. Works on Python 2 and 3.

`pip install MouseInfo` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 2745 · last release 2020-03-27 · [PyPI](https://pypi.org/project/MouseInfo/)

_README extract left out: share-alike licence._

### model-hosting-container-standards

Python toolkit for standardized model hosting container implementations with Amazon SageMaker integration

`pip install model-hosting-container-standards` · installs (wheel) · licence: Apache Software License · rank 2763 · last release 2026-06-15 · [PyPI](https://pypi.org/project/model-hosting-container-standards/)

<details><summary>README extract</summary>

A standardized Python framework for seamless integration between ML frameworks (TensorRT-LLM, vLLM) and Amazon SageMaker hosting.

Features:
This package simplifies model deployment by providing:
- Unified Handler System: Consistent `/ping` and `/invocations` endpoints across frameworks
- Flexible Configuration: Environment variables, decorators, or custom scripts ...

Example:
```python
import model_hosting_container_standards.sagemaker as sagemaker_standards
from fastapi import Request, Response

# Register decorators - automatically create /ping and /invocations routes
@sagemaker_standards.register_ping_handler
async def ping(request: Request) -> Response:
    """Framework ping handler with automatic routing."""
...
```

...

</details>

### mongomock-motor

Library for mocking AsyncIOMotorClient built on top of mongomock.

`pip install mongomock-motor` · installs (wheel) · licence: MIT License · rank 2793 · last release 2025-05-16 · [PyPI](https://pypi.org/project/mongomock-motor/) · [source](https://github.com/michaelkryukov/mongomock_motor)

<details><summary>README extract</summary>

Best effort mock for AsyncIOMotorClient
(Database, Collection, e.t.c) built on top of mongomock library.

Example:
```python
from mongomock_motor import AsyncMongoMockClient

async def test_mock_client():
    collection = AsyncMongoMockClient()'tests'

    assert await collection.find({}).to_list(None) == []

    result = await collection.insert_one({'a': 1})
    assert result.inserted_id

    assert len(await collection.find({}).to_list(None)) == 1
```

Sections: mongomock-motor, Example / Showcase

</details>

### mcp-for-blender

Open source Blender integration through the Model Context Protocol (not affiliated with Blender Foundation)

`pip install mcp-for-blender` · installs (wheel) · licence: MIT · rank 2821 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mcp-for-blender/)

<details><summary>README extract</summary>

*formerly `blender-mcp` — the PyPI package is now `mcp-for-blender`.*
*Existing setups keep working; no config change is required. Read more*

Disclaimer: This is a third-party integration and not made by Blender

Prompt-assisted 3D modeling, scene creation, and manipulation — driven by AI.

Supporters

CodeRabbit
Guillermo Rauch ...

Features:
| | |

| Two-way communication | Connect Claude AI to Blender through a socket-based server |
| Object manipulation | Create, modify, and delete 3D objects in Blender |
| Material control | Apply and modify materials and colors |
| Visual ...

...

</details>

### mypy-boto3-ses

Type annotations for boto3 SES 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ses` · installs (wheel) · licence: MIT · rank 2844 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-ses/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SES 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ses docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mitmproxy-linux

(no summary)

`pip install mitmproxy-linux` · installs (wheel) · licence: not stated · rank 2950 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mitmproxy-linux/)

### mypy-boto3-kinesis

Type annotations for boto3 Kinesis 1.43.101 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kinesis` · installs (wheel) · licence: MIT · rank 2952 · last release 2026-09-23 · [PyPI](https://pypi.org/project/mypy-boto3-kinesis/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Kinesis 1.43.101
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kinesis docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mssql-python-odbc

Internal implementation package for mssql-python: Microsoft ODBC Driver 18 for SQL Server binaries. Not intended for direct use.

`pip install mssql-python-odbc` · installs (wheel) · licence: Other/Proprietary License · rank 3037 · last release 2026-10-12 · [PyPI](https://pypi.org/project/mssql-python-odbc/)

<details><summary>README extract</summary>

Internal implementation package for mssql-python —
Microsoft's official Python driver for SQL Server, Azure SQL, and SQL databases in Fabric.

This package ships the platform-specific Microsoft ODBC Driver 18 for SQL Server binaries
(and the supporting runtime libraries they depend on) as a standalone, pure-data wheel, so that
`mssql-python` does ...

Sections: mssql-python-odbc, Not intended for direct use, Documentation

</details>

### mini-racer

Minimal, modern embedded V8 for Python.

`pip install mini-racer` · installs (wheel) · licence: ISC · rank 3050 · last release 2026-02-01 · [PyPI](https://pypi.org/project/mini-racer/)

<details><summary>README extract</summary>

Minimal, modern embedded V8 for Python.

Full documentation.

- Latest ECMAScript support
- Web Assembly support
- Unicode support
- Thread safe
- Re-usable contexts

MiniRacer can be easily used by Django or Flask projects to minify assets, run babel or
WASM modules. ...

Example:
```python
$ python3
>>> from py_mini_racer import MiniRacer
>>> ctx = MiniRacer()
>>> ctx.eval("1+1")
2
>>> ctx.eval("var x = {company: 'Sqreen'}; x.company")
'Sqreen'
>>> print(ctx.eval("'❤'"))
❤
>>> ctx.eval("var fun = () => ({ foo: 1 });")
```

...

</details>

### mcpo

A simple, secure MCP-to-OpenAPI proxy server

`pip install mcpo` · installs (wheel) · licence: not stated · rank 3057 · last release 2026-02-27 · [PyPI](https://pypi.org/project/mcpo/)

<details><summary>README extract</summary>

Expose any MCP tool as an OpenAPI-compatible HTTP server—instantly.

mcpo is a dead-simple proxy that takes an MCP server command and makes it accessible via standard RESTful OpenAPI, so your tools "just work" with LLM agents and apps expecting OpenAPI servers.

No custom protocol. No glue code. No hassle. ...

Sections: ⚡️ mcpo, 🤔 Why Use mcpo Instead of Native MCP?, 🚀 Quick Usage, 🌐 Serving Under a Subpath (`--root-path`), 🔄 Using a Config File, 🔐 OAuth 2.1 Authentication, OAuth Configuration Options, 🔧 Requirements

</details>

### mypy-boto3-lakeformation

Type annotations for boto3 LakeFormation 1.43.113 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-lakeformation` · installs (wheel) · licence: MIT · rank 3078 · last release 2026-10-13 · [PyPI](https://pypi.org/project/mypy-boto3-lakeformation/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 LakeFormation 1.43.113 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-lakeformation docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mrml

A Python wrapper for MRML (Rust port of MJML).

`pip install mrml` · installs (wheel) · licence: not stated · rank 3104 · last release 2026-04-25 · [PyPI](https://pypi.org/project/mrml/)

<details><summary>README extract</summary>

This project is a reimplementation of the nice `MJML` markup language in Rust, built for python.

To have more information, take a look at the repository.

Example:
```python
import mrml

# without options
result = mrml.to_html("<mjml></mjml>")
assert result.content.startswith("<!doctype html>")

# with options
parser_options = mrml.ParserOptions(include_loader = mrml.memory_loader({
    'hello-world.mjml': '<mj-text>Hello World!</mj-text>',
}))
...
```

Sections: mrml-python, Usage in python

</details>

### m3u8

Python m3u8 parser

`pip install m3u8` · installs (wheel) · licence: MIT · rank 3212 · last release 2024-08-07 · [PyPI](https://pypi.org/project/m3u8/)

<details><summary>README extract</summary>

Python m3u8 parser.

To load a playlist into an object from uri, file path or directly from
string, use the `load/loads` functions:

Example:
```python
import m3u8

playlist = m3u8.load('  # this could also be an absolute filename
print(playlist.segments)
print(playlist.target_duration)

# if you already have the content as string, use

playlist = m3u8.loads('#EXTM3U8 ... etc ... ')
```

Sections: m3u8, Documentation, Loading a playlist, Dumping a playlist, Frequently Asked Questions, Running Tests

</details>

### mypy-boto3-cognito-idp

Type annotations for boto3 CognitoIdentityProvider 1.43.108 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cognito-idp` · installs (wheel) · licence: MIT · rank 3297 · last release 2026-10-02 · [PyPI](https://pypi.org/project/mypy-boto3-cognito-idp/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CognitoIdentityProvider 1.43.108
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cognito-idp docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-apigateway

Type annotations for boto3 APIGateway 1.43.100 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-apigateway` · installs (wheel) · licence: MIT · rank 3303 · last release 2026-09-22 · [PyPI](https://pypi.org/project/mypy-boto3-apigateway/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 APIGateway 1.43.100 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-apigateway docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mitmproxy-wireguard

WireGuard interface for mitmproxy

`pip install mitmproxy-wireguard` · installs (wheel) · licence: MIT · rank 3338 · last release 2023-04-04 · [PyPI](https://pypi.org/project/mitmproxy-wireguard/) · [source](https://github.com/decathorpe/mitmproxy_wireguard)

<details><summary>README extract</summary>

Transparently proxy any device that can be configured as a WireGuard client!

 * one worker thread for the user-space WireGuard server
 * one worker thread for the user-space network stack
 * one worker thread for communicating with the Python runtime
* full support for IPv4 packets (TCP and UDP)
* partial support for IPv6 packets (TCP and UDP)
* ...

Sections: mitmproxy_wireguard, DONE, TODO, Requirements, Architecture, Interface, Hacking, Docs, Introspecting the tokio runtime, Code style

</details>

### msgpack-types

Type stubs for msgpack

`pip install msgpack-types` · installs (wheel) · licence: Apache Software License · rank 3354 · last release 2026-06-29 · [PyPI](https://pypi.org/project/msgpack-types/) · [source](https://github.com/sbdchd/msgpack-types)

<details><summary>README extract</summary>

> Type stubs for msgpack

Allows for autocomplete and static typing.

Sections: msgpack-types, related

</details>

### moreorless

Python diff wrapper

`pip install moreorless` · installs (wheel) · licence: MIT · rank 3427 · last release 2026-05-12 · [PyPI](https://pypi.org/project/moreorless/)

<details><summary>README extract</summary>

This is a thin wrapper around `difflib.unified_diff` that Does The Right Thing
for "No newline at eof". The args are also simplified compared to `difflib`:

Example:
```python
moreorless.unified_diff(
    astr: str,
    bstr: str,
    filename: str,
    n: int = 3,
) -> str:
    ...

# raises moreorless.patch.PatchException
moreorless.patch.apply_single_file(
    contents: str,
    patch: str,
    allow_offsets: bool = True,
) -> str:
    ...

# uses click to write to stdout with colors
...
```

Sections: moreorless, Version Compat, Versioning

</details>

### mypy-boto3-xray

Type annotations for boto3 XRay 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-xray` · installs (wheel) · licence: MIT · rank 3459 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-xray/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 XRay 1.43.115
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-xray docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-agents-activity

A protocol library for Microsoft Agents

`pip install microsoft-agents-activity` · installs (wheel) · licence: MIT · rank 3477 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-activity/)

<details><summary>README extract</summary>

Core types and schemas for building conversational AI agents that work across Microsoft 365 platforms like Teams, Copilot Studio, and Webchat.

This library is part of the Microsoft 365 Agents SDK for Python - a comprehensive framework for building enterprise-grade conversational AI agents. ...

Features:
✅ Type-safe - Built with Pydantic for automatic validation
✅ Rich content - Support for cards, images, videos, and interactive elements
✅ Teams ready - Full Microsoft Teams integration
✅ Cross-platform - Works across all Microsoft 365 chat ...

Example:
```python
@AGENT_APP.conversation_update("membersAdded")
async def on_members_added(context: TurnContext, _state: TurnState):
    await context.send_activity(
        "Welcome to the empty agent! "
...

</details>

### mozilla-django-oidc

A lightweight authentication and access management library for integration with OpenID Connect enabled authentication services.

`pip install mozilla-django-oidc` · installs (wheel) · licence: MPL-2.0 · rank 3483 · last release 2025-12-19 · [PyPI](https://pypi.org/project/mozilla-django-oidc/) · [docs](https://mozilla-django-oidc.readthedocs.io)

<details><summary>README extract</summary>

A lightweight authentication and access management library for integration with OpenID Connect enabled authentication services.

The full documentation is at <

* Keep it as minimal/lightweight as possible
* Store as few authn/authz artifacts as possible
* Allow custom functionality by overriding the authentication backend
* Mainly support OIDC ...

Sections: mozilla-django-oidc, Documentation, Design principles, Running Unit Tests, Running test services, Running integration tests, Linting, Releasing a new version

</details>

### mypy-boto3-signer

Type annotations for boto3 Signer 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-signer` · installs (wheel) · licence: MIT · rank 3499 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-signer/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Signer 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-signer docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-agents-hosting-core

Core library for Microsoft Agents

`pip install microsoft-agents-hosting-core` · installs (wheel) · licence: MIT · rank 3515 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-hosting-core/)

<details><summary>README extract</summary>

The core hosting library for Microsoft 365 Agents SDK. This library provides the fundamental building blocks for creating conversational AI agents, including activity processing, state management, authentication, and channel communication. ...

Example:
```python
agents_sdk_config = load_configuration_from_env(environ)

STORAGE = MemoryStorage()
CONNECTION_MANAGER = MsalConnectionManager(**agents_sdk_config)
ADAPTER = CloudAdapter(connection_manager=CONNECTION_MANAGER)
AUTHORIZATION = Authorization(STORAGE, CONNECTION_MANAGER, **agents_sdk_config)

AGENT_APP = AgentApplicationTurnState

...
```

...

</details>

### mypy-boto3-events

Type annotations for boto3 EventBridge 1.43.102 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-events` · installs (wheel) · licence: MIT · rank 3526 · last release 2026-09-24 · [PyPI](https://pypi.org/project/mypy-boto3-events/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_events/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EventBridge 1.43.102 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-events docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcp-proxy-for-aws

MCP Proxy for AWS

`pip install mcp-proxy-for-aws` · installs (wheel) · licence: Apache Software License · rank 3540 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mcp-proxy-for-aws/) · [docs](https://github.com/aws/mcp-proxy-for-aws/blob/main/README.md) · [source](https://github.com/aws/mcp-proxy-for-aws.git)

<details><summary>README extract</summary>

Features:
The MCP Proxy for AWS package provides two ways to connect AI applications to MCP servers on AWS:

1. Using it as a proxy - It becomes a lightweight, client-side bridge between MCP clients (AI assistants like Claude Desktop, Kiro CLI) and MCP ...

Example:
```python
from botocore.credentials import Credentials
from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client

creds = Credentials(access_key='...', secret_key='...', token='...')

mcp_client = aws_iam_streamablehttp_client(
    endpoint=mcp_url,
    aws_region=region,
    aws_service=service,
...
```

...

</details>

### mlx

A framework for machine learning on Apple silicon.

`pip install mlx` · installs (wheel) · licence: MIT · rank 3598 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mlx/)

<details><summary>README extract</summary>

Quickstart | Installation |
Documentation |
Examples

MLX is an array framework for machine learning on Apple silicon,
brought to you by Apple machine learning research.

Some key features of MLX include:

- Familiar APIs: MLX has a Python API that closely follows NumPy. ...

Sections: MLX, Examples, Quickstart, Citing MLX

</details>

### mkdocs-git-revision-date-localized-plugin

Mkdocs plugin that enables displaying the localized date of the last git modification of a markdown file.

`pip install mkdocs-git-revision-date-localized-plugin` · installs (wheel) · licence: MIT License · rank 3613 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mkdocs-git-revision-date-localized-plugin/)

<details><summary>README extract</summary>

MkDocs plugin that enables displaying the date of the last git modification of a page. The plugin uses babel and timeago.js to provide different localized date formats. Works with `mkdocs-material`, see adding a git repository.

(*Example when used together with the mkdocs-material theme*) ...

Sections: mkdocs-git-revision-date-localized-plugin, Setup, Note when using build systems like Github Actions, Documentation, Related MkDocs plugins

</details>

### mockito

Spying framework

`pip install mockito` · installs (wheel) · licence: MIT · rank 3645 · last release 2026-04-15 · [PyPI](https://pypi.org/project/mockito/)

<details><summary>README extract</summary>

Mockito is a spying framework originally based on the Java library with the same name. (Actually *we* invented the strict stubbing mode
back in 2009.)

Example:
```python
from mockito import when, mock, unstub

when(os.path).exists('/foo').thenReturn(True)

# or:
import requests  # the famous library
# you actually want to return a Response-like obj, we'll fake it
response = mock({'status_code': 200, 'text': 'Ok'})
when(requests).get(...).thenReturn(response)

# use it
requests.get('

# clean up
unstub()
```

Sections: Quick Start, Read the docs, Breaking changes in v2, New in v2

</details>

### mkdocs-macros-plugin

Unleash the power of MkDocs with macros and variables

`pip install mkdocs-macros-plugin` · installs (wheel) · licence: MIT License · rank 3661 · last release 2025-11-13 · [PyPI](https://pypi.org/project/mkdocs-macros-plugin/)

<details><summary>README extract</summary>

:open_file_folder: Used by > 2K repositories on Github

🥇 Listed as High-Quality Plugin

mkdocs-macros-plugin is a general-purpose plugin for MkDocs
that uses variables and macros (functions) to automate tasks, and produce richer and more beautiful pages.

View the mkdocs-macro documentation on Read the Docs.

Features:
mkdocs-macros-plugin is a plugin that makes it easier for contributors
of an MkDocs website to produce richer and more beautiful pages. It transforms the markdown pages
into jinja2 templates
that use variables, calls to macros and custom filters. ...

Example:
```python
{{ macros_info() }}
```

...

</details>

### mypy-boto3-autoscaling

Type annotations for boto3 AutoScaling 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-autoscaling` · installs (wheel) · licence: MIT · rank 3675 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-autoscaling/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AutoScaling 1.43.126 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-autoscaling docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-schemas

Type annotations for boto3 Schemas 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-schemas` · installs (wheel) · licence: MIT · rank 3699 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-schemas/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Schemas 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-schemas docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mux-python

Mux API

`pip install mux-python` · installs (wheel) · licence: MIT · rank 3744 · last release 2026-01-08 · [PyPI](https://pypi.org/project/mux-python/)

<details><summary>README extract</summary>

PyPI |
 Mux Docs |
 Mux API Reference

Official Mux API wrapper for python projects, supporting both Mux Data and Mux Video.

Mux Video is an API-first platform, powered by data and designed by video experts to make beautiful video possible for every development team. ...

Features:
Mux Python is a code generated lightweight wrapper around the Mux REST API and reflects them accurately. This has a few consequences you should watch out for: ...

Example:
```python
import os
import mux_python
from mux_python.rest import ApiException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
...

</details>

### minify-html

Extremely fast and smart HTML + JS + CSS minifier

`pip install minify-html` · installs (wheel) · licence: MIT · rank 3756 · last release 2025-10-25 · [PyPI](https://pypi.org/project/minify-html/) · [source](https://github.com/wilsonzlin/minify-html.git)

<details><summary>README extract</summary>

A Rust HTML minifier meticulously optimised for speed and effectiveness, with bindings for other languages.

- Advanced minification strategy beats other minifiers in effectiveness while still being much faster.
- Handles invalid HTML and templating syntax.
- Uses oxc and lightningcss for super fast JS and CSS minification. ...

Example:
```python
import minify_html

minified = minify_html.minify("  Hello, world!
", minify_js=True, remove_processing_instructions=True)
```

Sections: minify-html, Performance, Compatibility and usage, Use, Get

</details>

### mlx-metal

A framework for machine learning on Apple silicon.

`pip install mlx-metal` · does not install on CPython 3.14 · licence: MIT · rank 3758 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mlx-metal/)

<details><summary>README extract</summary>

Quickstart | Installation |
Documentation |
Examples

MLX is an array framework for machine learning on Apple silicon,
brought to you by Apple machine learning research.

Some key features of MLX include:

- Familiar APIs: MLX has a Python API that closely follows NumPy. ...

Sections: MLX, Examples, Quickstart, Citing MLX

</details>

### mypy-boto3-elbv2

Type annotations for boto3 ElasticLoadBalancingv2 1.43.88 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-elbv2` · installs (wheel) · licence: MIT · rank 3825 · last release 2026-09-03 · [PyPI](https://pypi.org/project/mypy-boto3-elbv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElasticLoadBalancingv2 1.43.88
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-elbv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### maison

Read settings from config files

`pip install maison` · installs (wheel) · licence: MIT · rank 3841 · last release 2025-10-09 · [PyPI](https://pypi.org/project/maison/) · [source](https://github.com/dbatten/maison)

<details><summary>README extract</summary>

Read configuration settings from configuration files.

📚 View Documentation | 🐛 Report a Bug | ✨ Request a Feature

When developing a `python` package, e.g a command-line tool, it can be helpful
to allow the user to set their own configuration options to allow them to tailor
the tool to their needs. ...

Features:
- Supports multiple config files and multiple config filetypes.
- Optional merging of multiple configs.
- Optional config validation with pydantic.
- Caching of config files for quick access.
- Fully tested and typed.

Example:
```python
from maison import UserConfig

from my_useful_package import run_useful_action

config = UserConfig(package_name="acme")

if config.values["enable_useful_option"]:
    run_useful_action()
```

Sections: Maison, Motivation, Features, Usage

</details>

### mypy-boto3-batch

Type annotations for boto3 Batch 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-batch` · installs (wheel) · licence: MIT · rank 3936 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mypy-boto3-batch/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Batch 1.43.106
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-batch docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mkdocs-monorepo-plugin

Plugin for adding monorepository support in Mkdocs.

`pip install mkdocs-monorepo-plugin` · installs (wheel) · licence: Apache-2.0 · rank 3944 · last release 2025-06-05 · [PyPI](https://pypi.org/project/mkdocs-monorepo-plugin/)

<details><summary>README extract</summary>

This introduces support for the !include syntax in mkdocs.yml, allowing you to import additional Mkdocs navigation.
 It enables large or complex repositories to have their own sets of docs/ folders, whilst generating only a single Mkdocs site.
 This is built and maintained by the Backstage open source team.

</details>

### modin

Modin: Make your pandas code run faster by changing one line of code.

`pip install modin` · installs (wheel) · licence: Apache 2 · rank 3990 · last release 2025-10-02 · [PyPI](https://pypi.org/project/modin/)

<details><summary>README extract</summary>

Example:
```python
import modin.config as modin_cfg
import unidist.config as unidist_cfg

modin_cfg.Engine.put("ray")  # Modin will use Ray
modin_cfg.Engine.put("dask")  # Modin will use Dask

modin_cfg.Engine.put('unidist') # Modin will use Unidist
unidist_cfg.Backend.put('mpi') # Unidist will use MPI backend
```

Sections: Scale your pandas workflows by changing one line of code, Forums, Socials, Docs, What is Modin?, From PyPI, From conda-forge, Choosing a Compute Engine, Which engine should I use?, Pandas API Coverage, More about Modin, Faster pandas, even on your laptop, Modin can handle the datasets that pandas can't, Modin Architecture

</details>

### microsoft-agents-authentication-msal

A msal-based authentication library for Microsoft Agents

`pip install microsoft-agents-authentication-msal` · installs (wheel) · licence: MIT · rank 3994 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-authentication-msal/)

<details><summary>README extract</summary>

Provides secure authentication for your agents using Microsoft Authentication Library (MSAL). It handles getting tokens from Azure AD so your agent can securely communicate with Microsoft services like Teams, Graph API, and other Azure resources. ...

Features:
✅ Multiple auth types - Client secret, certificate, managed identity
✅ Token caching - Automatic token refresh and caching
✅ Multi-tenant - Support for different Azure AD tenants
✅ Agent-to-agent - Secure communication between agents
✅ On-behalf-of ...

Example:
```python
from .start_server import start_server

start_server(
    agent_application=AGENT_APP,
    auth_configuration=CONNECTION_MANAGER.get_default_connection_configuration(),
)
```

...

</details>

### mypy-boto3-eks

Type annotations for boto3 EKS 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-eks` · installs (wheel) · licence: MIT · rank 4043 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mypy-boto3-eks/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EKS 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-eks docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-bedrock

Type annotations for boto3 Bedrock 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock` · installs (wheel) · licence: MIT · rank 4047 · last release 2026-10-20 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Bedrock 1.43.116
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-codebuild

Type annotations for boto3 CodeBuild 1.43.38 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codebuild` · installs (wheel) · licence: MIT · rank 4078 · last release 2026-06-30 · [PyPI](https://pypi.org/project/mypy-boto3-codebuild/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 CodeBuild 1.43.38
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codebuild docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### miscreant

Misuse-resistant authenticated symmetric encryption

`pip install miscreant` · installs from source (sdist only) · licence: MIT License · rank 4082 · last release 2017-12-25 · [PyPI](https://pypi.org/project/miscreant/)

<details><summary>README extract</summary>

Misuse resistant symmetric encryption library providing AES-SIV (RFC 5297), AES-PMAC-SIV, and STREAM constructions

</details>

### mypy-boto3-acm

Type annotations for boto3 ACM 1.43.121 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-acm` · installs (wheel) · licence: MIT · rank 4157 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mypy-boto3-acm/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ACM 1.43.121
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-acm docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy_baseline

Integrate mypy with existing codebase.

`pip install mypy_baseline` · installs (wheel) · licence: MIT License · rank 4159 · last release 2026-04-13 · [PyPI](https://pypi.org/project/mypy_baseline/) · [source](https://github.com/orsinium-labs/mypy-baseline)

<details><summary>README extract</summary>

A CLI tool for painless integration of mypy with an existing Python project. When you run it for the first time, it will remember all type errors that you already have in the project (generate "baseline"). All consecutive runs will ignore these errors and report only ones that you introduced after that. ...

Sections: mypy-baseline, Usage

</details>

### mcap-protobuf-support

Protobuf support for the Python MCAP library

`pip install mcap-protobuf-support` · installs (wheel) · licence: MIT License · rank 4166 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mcap-protobuf-support/)

### marshmallow-jsonschema

JSON Schema Draft v7 (http://json-schema.org/) formatting with marshmallow

`pip install marshmallow-jsonschema` · installs (wheel) · licence: MIT License · rank 4234 · last release 2026-04-26 · [PyPI](https://pypi.org/project/marshmallow-jsonschema/)

<details><summary>README extract</summary>

`marshmallow-jsonschema` translates marshmallow
schemas into JSON Schema Draft v7 compliant
documents.

Features:
A few common reasons:

- Render a marshmallow schema as a form in another runtime (web browser,
 mobile, native desktop) where you can't import Python. ...

Example:
```python
from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema

class UserSchema(Schema):
    username = fields.String()
    age = fields.Integer()
    birthday = fields.Date()

JSONSchema().dump(UserSchema())
```

...

</details>

### mypy-boto3-textract

Type annotations for boto3 Textract 1.43.69 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-textract` · installs (wheel) · licence: MIT · rank 4241 · last release 2026-08-11 · [PyPI](https://pypi.org/project/mypy-boto3-textract/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_textract/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Textract 1.43.69
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-textract docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3

Legacy type annotations for boto3, use types-boto3 instead.

`pip install mypy-boto3` · installs (wheel) · licence: MIT · rank 4250 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3/) · [docs](https://youtype.github.io/boto3_stubs_docs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

[!\[PyPI - Downloads\](

Dynamic
boto3 1.43.0

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
types-boto3 page.

See how it helps to find and fix potential bugs:

- mypy-boto3
 - How to install
 - Usage
 - Latest changes
 - Versioning
 - Support and contributing

Example:
```python
from typing import overload

import boto3
from botocore.client import BaseClient
from types_boto3.literals import ServiceName
from types_boto3_ec2.client import EC2Client
from types_boto3_ec2.literals import EC2ServiceName
from types_boto3_s3.client import S3Client
from types_boto3_s3.literals import S3ServiceName

@overload
...
```

Sections: mypy-boto3, Usage, Latest changes, Versioning

</details>

### mypy-boto3-sesv2

Type annotations for boto3 SESV2 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sesv2` · installs (wheel) · licence: MIT · rank 4309 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-sesv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SESV2 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sesv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-redshift-data

Type annotations for boto3 RedshiftDataAPIService 1.43.117 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-redshift-data` · installs (wheel) · licence: MIT · rank 4325 · last release 2026-10-21 · [PyPI](https://pypi.org/project/mypy-boto3-redshift-data/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 RedshiftDataAPIService 1.43.117
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-redshift-data docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### misaki

G2P engine for TTS

`pip install misaki` · does not install on CPython 3.14 · licence: Apache Software License · rank 4354 · last release 2025-04-05 · [PyPI](https://pypi.org/project/misaki/)

<details><summary>README extract</summary>

Misaki is a G2P engine designed for Kokoro models.

Hosted demo:

Example:
```python
!pip install -q "misaki[en]"

from misaki import en

g2p = en.G2P(trf=False, british=False, fallback=None) # no transformer, American English

text = 'Misaki is a G2P engine designed for Kokoro models.'

phonemes, tokens = g2p(text)

print(phonemes) # misˈɑki ɪz ə ʤˈitəpˈi ˈɛnʤən dəzˈInd fɔɹ kˈOkəɹO mˈɑdᵊlz.
```

Sections: misaki, English Usage, English, Japanese, Korean, Chinese, Vietnamese, TODO

</details>

### mcp-server-fetch

A Model Context Protocol server providing tools to fetch and convert web content for usage by LLMs

`pip install mcp-server-fetch` · installs (wheel) · licence: MIT License · rank 4365 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mcp-server-fetch/) · [source](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

<details><summary>README extract</summary>

A Model Context Protocol server that provides web content fetching capabilities. This server enables LLMs to retrieve and process content from web pages, converting HTML to markdown for easier consumption.

Source:

Requires MCP Python SDK 2.x (`mcp>=2.3,<3`). ...

Sections: Fetch MCP Server, Available Tools, Prompts, Errors, Content negotiation, Using uv (recommended), Using PIP, Configuration, Configure for Claude.app, Configure for VS Code, Customization - robots.txt, Customization - Private addresses, Customization - Allowed hosts, Customization - User-agent

</details>

### Metaphone

A Python implementation of the metaphone and double metaphone algorithms.

`pip install Metaphone` · installs from source (sdist only) · licence: BSD · rank 4371 · last release 2016-08-24 · [PyPI](https://pypi.org/project/Metaphone/)

<details><summary>README extract</summary>

*A Python implementation of the Metaphone and Double Metaphone algorithms*

As described on the Wikipedia page, the original Metaphone algorithm was
published in 1990 as an improvement over the Soundex algorithm. Like
Soundex, it was limited to English-only use. ...

Example:
```python
$ python
>>> from metaphone import doublemetaphone
>>> doublemetaphone("architect")
(u"ARKTKT", u"")
>>> doublemetaphone("bajador")
(u"PJTR", u"PHTR")
>>> doublemetaphone("Τι είναι το Unicode;")
(u'NKT', u'')
```

Sections: Metaphone, About, Double Metaphone, Usage, Running the Unit Tests, Example Code, In the Wild

</details>

### mkdocs-mermaid2-plugin

A MkDocs plugin for including mermaid graphs in markdown sources

`pip install mkdocs-mermaid2-plugin` · installs (wheel) · licence: MIT License · rank 4395 · last release 2025-10-17 · [PyPI](https://pypi.org/project/mkdocs-mermaid2-plugin/)

<details><summary>README extract</summary>

An MkDocs plugin that renders Mermaid text descriptions into diagrams (flow charts, sequence diagrams, pie charts, etc.).

* See the mkdocs-mermaid2 documentation on Read The Docs.
* See the package on Pypi.
* View the general Mkdocs documentation ...

Sections: Mkdocs-Mermaid2, Introduction, Automatic, Manual, Test, Configuration, Basic configuration, Specifying the version of the Mermaid library, Additional settings for the Material theme, For more information

</details>

### mypy-boto3-route53

Type annotations for boto3 Route53 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-route53` · installs (wheel) · licence: MIT · rank 4401 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-route53/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Route53 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-route53 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### msgpack-python

MessagePack (de)serializer.

`pip install msgpack-python` · installs from source (sdist only) · licence: Apache Software License · rank 4428 · last release 2018-03-10 · [PyPI](https://pypi.org/project/msgpack-python/)

<details><summary>README extract</summary>

This package is deprecated. Install msgpack instead.

</details>

### miniKanren

Relational programming in Python

`pip install miniKanren` · installs (wheel) · licence: not stated · rank 4470 · last release 2025-06-24 · [PyPI](https://pypi.org/project/miniKanren/) · [source](http://github.com/pythological/kanren)

<details><summary>README extract</summary>

Logic/relational programming in Python with miniKanren.

Example:
```python
>>> from kanren import run, eq, membero, var, lall
>>> x = var()
>>> run(1, x, eq(x, 5))
(5,)
```

Sections: `kanren`, Motivation, Examples, Representing Knowledge, Constraints, Graph Relations, Extending `kanren`, About, References

</details>

### mkdocs-awesome-pages-plugin

An MkDocs plugin that simplifies configuring page titles and their order

`pip install mkdocs-awesome-pages-plugin` · installs (wheel) · licence: MIT License · rank 4498 · last release 2024-12-22 · [PyPI](https://pypi.org/project/mkdocs-awesome-pages-plugin/) · [source](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/)

<details><summary>README extract</summary>

Sections: Features, Customize Navigation, Rest, Titles, Links, Sections, Change Sort Order, Natural Sort Type, Sorting Case Sensitivity, Order Navigation By Preference, Collapse Single Nested Pages, For all pages, For a sub-section, For a single page

</details>

### mypy-boto3-organizations

Type annotations for boto3 Organizations 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-organizations` · installs (wheel) · licence: MIT · rank 4529 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mypy-boto3-organizations/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Organizations 1.43.114 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-organizations docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcap-ros2-support

ROS2 support for the Python MCAP library

`pip install mcap-ros2-support` · installs (wheel) · licence: MIT License · rank 4535 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mcap-ros2-support/)

<details><summary>README extract</summary>

Example:
```python
# Reading from a MCAP file
from mcap_ros2.reader import read_ros2_messages

for msg in read_ros2_messages("my_data.mcap"):
    print(f"{msg.channel.topic}: f{msg.ros_msg}")
```

Sections: Reading ROS2 Messages, Stay in touch

</details>

### microsoft-teams-cards

Cards package for Microsoft Teams

`pip install microsoft-teams-cards` · installs (wheel) · licence: MIT · rank 4543 · last release 2026-11-05 · [PyPI](https://pypi.org/project/microsoft-teams-cards/)

<details><summary>README extract</summary>

Adaptive Cards models and specialized action types for Microsoft Teams applications.
Provides Pydantic-based models for creating Adaptive Cards and Teams-specific actions.

Features:
- Adaptive Card Models: Pydantic models for Adaptive Card schema
- Teams Actions: Specialized action types for Teams interactions

Example:
```python
from microsoft_teams.cards import AdaptiveCard, TextBlock, SubmitAction

# Create adaptive card components
card = AdaptiveCard(
    body=[
        TextBlock(text="Hello from Teams!")
    ],
    actions=[
        SubmitAction(title="Click Me", data={"action": "hello"})
    ]
)
```

Sections: Microsoft Teams Cards, Features, Basic Usage, Teams-Specific Actions

</details>

### mkdocs-minify-plugin

An MkDocs plugin to minify HTML, JS or CSS files prior to being written to disk

`pip install mkdocs-minify-plugin` · installs (wheel) · licence: MIT License · rank 4547 · last release 2024-01-29 · [PyPI](https://pypi.org/project/mkdocs-minify-plugin/)

<details><summary>README extract</summary>

[][pypi-link]

An MkDocs plugin to minify HTML, JS or CSS files prior to being written to disk.

HTML minification is done using htmlmin2.

JS minification is done using jsmin.

CSS minification is done using csscompressor.

Install the plugin using pip:

Activate the plugin in `mkdocs.yml`: ...

Sections: mkdocs-minify-plugin, Setup, Options

</details>

### microsoft-teams-common

Common package for Microsoft Teams

`pip install microsoft-teams-common` · installs (wheel) · licence: MIT · rank 4565 · last release 2026-11-05 · [PyPI](https://pypi.org/project/microsoft-teams-common/)

<details><summary>README extract</summary>

Shared utilities including HTTP client, logging, storage, and event handling.
Provides common functionality used across other Teams SDK packages.

Features:
- HTTP Client: Async HTTP client with token support and interceptors
- Event System: Type-safe event emitter for application lifecycle management
- Storage: Local storage implementations for key-value and list data ...

Example:
```python
from microsoft_teams.common import Client, ClientOptions

# Create HTTP client
client = Client(ClientOptions(
    base_url="
    headers={"User-Agent": "Teams-Bot/1.0"}
))

# Make requests
response = await client.get("/users/me")
data = await client.post("/messages", json={"text": "Hello"})
```

Sections: Microsoft Teams Common Utilities, Features, HTTP Client, Event System, Storage, Logging

</details>

### microsoft-teams-api

API package for Microsoft Teams

`pip install microsoft-teams-api` · installs (wheel) · licence: MIT · rank 4583 · last release 2026-11-05 · [PyPI](https://pypi.org/project/microsoft-teams-api/)

<details><summary>README extract</summary>

Core API client library for Microsoft Teams Bot Framework integration.
Provides HTTP clients, authentication, and typed models for Teams Bot Framework APIs.

Features:
- API Clients: Bot, User, Conversation, Team, and Meeting clients
- Authentication: ClientCredentials and TokenCredentials support
- Activity Models: Typed Pydantic models for Teams activities ...

Example:
```python
from microsoft_teams.api import ApiClient

# Initialize API client
api = ApiClient("

# Bot token operations
token_response = await api.bots.token.get(credentials)
graph_token = await api.bots.token.get_graph(credentials)

# User token operations
user_token = await api.users.token.get(params)
token_status = await api.users.token.get_status(params)
```

...

</details>

### mypy-boto3-scheduler

Type annotations for boto3 EventBridgeScheduler 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-scheduler` · installs (wheel) · licence: MIT · rank 4612 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-scheduler/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_scheduler/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EventBridgeScheduler 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-scheduler docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mnemonic

Implementation of Bitcoin BIP-0039

`pip install mnemonic` · installs (wheel) · licence: MIT License · rank 4639 · last release 2024-01-05 · [PyPI](https://pypi.org/project/mnemonic/)

<details><summary>README extract</summary>

Reference implementation of BIP-0039: Mnemonic code for generating
deterministic keys

This BIP describes the implementation of a mnemonic code or mnemonic sentence --
a group of easy to remember words -- for the generation of deterministic wallets.

It consists of two parts: generating the mnenomic, and converting it into a
binary seed. ...

Example:
```python
from mnemonic import Mnemonic
```

Sections: python-mnemonic, Abstract, BIP Paper, Usage examples, 0.21 - 2024-01-05, Added, Changed, Removed, 0.20 - 2021-07-27, 0.19 - 2019-10-01

</details>

### mslex

shlex for windows

`pip install mslex` · installs (wheel) · licence: Apache Software License · rank 4647 · last release 2024-10-16 · [PyPI](https://pypi.org/project/mslex/)

<details><summary>README extract</summary>

shlex for windows

* Free software: Apache Software License 2.0

Features:
This is the missing shlex package for windows shell quoting. It provides three
functions -- split, quote, and join -- just like shlex.

Sections: mslex, Features, Windows Quoting, Automatic selection between mslex and shlex

</details>

### mypy-boto3-firehose

Type annotations for boto3 Firehose 1.43.29 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-firehose` · installs (wheel) · licence: MIT · rank 4650 · last release 2026-06-12 · [PyPI](https://pypi.org/project/mypy-boto3-firehose/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_firehose/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Firehose 1.43.29
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-firehose docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcp-atlassian

The Model Context Protocol (MCP) Atlassian integration is an open-source implementation that bridges Atlassian products (Jira and Confluence) with AI language models following Anthropic's MCP specification. This project enables secure, contextual AI interactions with Atlassian tools while maintaining data privacy and security. Key features include:

`pip install mcp-atlassian` · installs (wheel) · licence: not stated · rank 4675 · last release 2026-08-19 · [PyPI](https://pypi.org/project/mcp-atlassian/)

<details><summary>README extract</summary>

Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). Supports both Cloud and Server/Data Center deployments.

<details>
<summary>Confluence Demo</summary>

</details>

Sections: MCP Atlassian, Quick Start, 1. Get Your API Token, 2. Configure Your IDE, Autohand Code, 3. Start Using, Documentation, Compatibility, Key Tools

</details>

### moocore

Core Algorithms for Multi-Objective Optimization

`pip install moocore` · installs (wheel) · licence: LGPL-2.1-or-later · rank 4723 · last release 2026-07-12 · [PyPI](https://pypi.org/project/moocore/) · [docs](https://multi-objective.github.io/moocore/python/) · [source](https://github.com/multi-objective/moocore/)

_README extract left out: share-alike licence._

### mapbox-vector-tile

Mapbox Vector Tile encoding and decoding.

`pip install mapbox-vector-tile` · installs (wheel) · licence: MIT License · rank 4736 · last release 2025-07-08 · [PyPI](https://pypi.org/project/mapbox-vector-tile/) · [source](https://github.com/tilezen/mapbox-vector-tile)

<details><summary>README extract</summary>

Example:
```python
>>> import mapbox_vector_tile

# Using WKT
>>> mapbox_vector_tile.encode([
    {
      "name": "water",
      "features": [
        {
          "geometry":"POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))",
          "properties":{
            "uid":123,
            "foo":"bar",
            "cat":"flew"
          }
        }
      ]
    },
    {
...
```

Sections: Mapbox Vector Tile, Encoding, Coordinate transformations for encoding, Quantization, Custom extents, Decoding, Use native protobuf library for performance

</details>

### mypy-boto3-emr-serverless

Type annotations for boto3 EMRServerless 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-emr-serverless` · installs (wheel) · licence: MIT · rank 4821 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-emr-serverless/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EMRServerless 1.43.110 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-emr-serverless docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-kiota-bundle

Bundle package for kiota generated libraries in Python

`pip install microsoft-kiota-bundle` · installs (wheel) · licence: MIT License · rank 4826 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-kiota-bundle/) · [docs](https://learn.microsoft.com/openapi/kiota/) · [source](https://github.com/microsoft/kiota-python)

<details><summary>README extract</summary>

The Microsoft Kiota Bundle Library is a library providing default implementations for client setup. The package provides
a request adapter implementation with defaults serialization libraries setup fo use with a generated Kiota client. This
is the preferred dependency for integrating with Microsoft Graph.

Read more about Kiota here. ...

Sections: Microsoft Kiota Bundle library, Using the Microsoft Kiota Bundle library, Trademarks

</details>

### mteb

Massive Text Embedding Benchmark

`pip install mteb` · installs (wheel) · licence: Apache-2.0 · rank 4828 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mteb/) · [docs](https://embeddings-benchmark.github.io/mteb/) · [source](https://github.com/embeddings-benchmark/mteb)

<details><summary>README extract</summary>

Installation |
 Usage |
 Leaderboard |
 Documentation |
 Citing

Features:
| Overview | |

| 📈 [Leaderboard] | The interactive leaderboard of the benchmark |
| Get Started. | |
| 🏃 [Get Started] | Overview of how to use mteb |
| 🤖 [Defining Models] | How to use existing models and define custom ones |
| 📋 [Selecting tasks] ...

Example:
```python
import mteb
from sentence_transformers import SentenceTransformer

# Select model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = mteb.get_model(
    model_name
)  # if the model is not implemented in MTEB it will be eq. to SentenceTransformer(model_name)

# Select tasks
tasks = mteb.get_tasks(tasks=["Banking77Classification.v2"])

...
```

Sections: MTEB, Example Usage, Overview, Citing

</details>

### mongo-orchestration

Restful service for managing MongoDB servers

`pip install mongo-orchestration` · installs (wheel) · licence: Apache Software License · rank 4830 · last release 2026-02-25 · [PyPI](https://pypi.org/project/mongo-orchestration/)

<details><summary>README extract</summary>

See the wiki
for documentation.

Mongo Orchestration is an HTTP server that provides a REST API for
creating and managing MongoDB configurations on a single host.

THIS PROJECT IS FOR TESTING OF MONGODB DRIVERS.

Features:
- Start and stop mongod servers, replica sets, and sharded clusters on the host running mongo-orchestration.
- Add and remove replica set members.
- Add and remove shards and mongos routers. ...

Sections: Mongo Orchestration, Features, Requires, Usage, Examples, Configuration File, Predefined Configurations, Mongo Launch, Tests, Run all tests, Run a test module, Run a single test case, Run a single test method, Changes in Version 0.11.2 (2026-02-25)

</details>

### mypy-boto3-efs

Type annotations for boto3 EFS 1.43.23 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-efs` · installs (wheel) · licence: MIT · rank 4848 · last release 2026-06-04 · [PyPI](https://pypi.org/project/mypy-boto3-efs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EFS 1.43.23
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-efs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### msgraphfs

(no summary)

`pip install msgraphfs` · installs (wheel) · licence: MIT License · rank 4852 · last release 2026-07-02 · [PyPI](https://pypi.org/project/msgraphfs/) · [source](https://github.com/acsone/msgraphfs)

<details><summary>README extract</summary>

Filesystem interface to Microsoft Graph API (SharePoint, OneDrive)

Quickstart

This package can be installed using:

`pip install msgraphfs`


`uv add msgraphfs`

The `msgd://`, `sharepoint://`, and `onedrive://` protocols are included in fsspec's known_implementations registry, allowing seamless integration with fsspec-compatible libraries. ...

Example:
```python
storage_options = {
    'client_id': CLIENT_ID,
    'tenant_id': TENANT_ID,
    'client_secret': CLIENT_SECRET,
    'site_name': 'YourSite',
    'drive_name': 'Documents'
}
df = pd.read_csv('msgd://folder/file.csv', storage_options=storage_options)
```

...

</details>

### mypy-boto3-sagemaker

Type annotations for boto3 SageMaker 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sagemaker` · installs (wheel) · licence: MIT · rank 4879 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-sagemaker/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 SageMaker 1.43.125 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sagemaker docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-backup

Type annotations for boto3 Backup 1.43.78 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-backup` · installs (wheel) · licence: MIT · rank 4885 · last release 2026-08-21 · [PyPI](https://pypi.org/project/mypy-boto3-backup/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Backup 1.43.78
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-backup docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mkdocs-techdocs-core

The core MkDocs plugin used by Backstage's TechDocs as a wrapper around multiple MkDocs plugins and Python Markdown extensions

`pip install mkdocs-techdocs-core` · installs (wheel) · licence: Apache-2.0 · rank 4893 · last release 2026-08-21 · [PyPI](https://pypi.org/project/mkdocs-techdocs-core/)

<details><summary>README extract</summary>

This is the base Mkdocs plugin used when using Mkdocs with Spotify's TechDocs. It is written in Python and packages all of our Mkdocs defaults, such as theming, plugins, etc in a single plugin.

Sections: mkdocs-techdocs-core, Usage, Running Locally, Linting, MkDocs plugins and extensions, Other plugins and extensions, Caveats, Theme

</details>

### mjml-python

A Python wrapper for MRML (Rust port of MJML).

`pip install mjml-python` · installs (wheel) · licence: MIT License · rank 4908 · last release 2026-09-01 · [PyPI](https://pypi.org/project/mjml-python/)

<details><summary>README extract</summary>

Compile MJML at runtime without a Node.js service, external API, or subprocess.
`mjml-python` is a Python wrapper around the Rust MJML engine MRML, a high-performance port of the official MJML.

Features:
Using MJML traditionally requires either:

- running the Node.js-based MJML CLI as a subprocess, or
- calling an external MJML API service.

Both approaches add memory overhead, latency, operational complexity, and cost.

From MRML: ...

Example:
```python
from mjml import mjml2html

html = mjml2html(
    '''
        <mjml>
          <mj-body>
            <mj-section>
              <mj-column>
                <mj-image width="100px" src="/assets/img/logo-small.png"></mj-image>
                <mj-divider border-color="#F45E43"></mj-divider>
                <!-- Say hello to the user -->
...

</details>

### multiurl

A package to download several URL as one, as well as supporting multi-part URLs

`pip install multiurl` · installs (wheel) · licence: Apache Software License · rank 4920 · last release 2026-06-18 · [PyPI](https://pypi.org/project/multiurl/)

<details><summary>README extract</summary>

A package to download several URL as one, as well as supporting multi-part URLs

Example:
```python
from multiurl import download

download(url="
         target="data.file")
```

Sections: multiurl, Simple example, Download from two URLs into one file, Download parts of URLs, Download parts of URLs form several URLs

</details>

### meilisearch

The python client for Meilisearch API.

`pip install meilisearch` · installs (wheel) · licence: MIT License · rank 4922 · last release 2026-07-22 · [PyPI](https://pypi.org/project/meilisearch/) · [docs](https://meilisearch.github.io/meilisearch-python/)

### microsoft-opentelemetry

Microsoft OpenTelemetry distro for Python

`pip install microsoft-opentelemetry` · installs (wheel) · licence: MIT License · rank 5009 · last release 2026-11-06 · [PyPI](https://pypi.org/project/microsoft-opentelemetry/) · [docs](https://microsoft.github.io/opentelemetry-distro-python/) · [source](https://github.com/microsoft/opentelemetry-distro-python)

<details><summary>README extract</summary>

Python package for a Microsoft OpenTelemetry distribution that provides a single onboarding experience for observability across Azure Monitor, OTLP-compatible backends, and Microsoft Agent 365 integrations.

Example:
```python
from microsoft.opentelemetry import use_microsoft_opentelemetry

use_microsoft_opentelemetry(
    enable_azure_monitor=True,
    azure_monitor_connection_string="InstrumentationKey=...;IngestionEndpoint=...",
)
```

Sections: microsoft-opentelemetry, Getting Started, Prerequisites, Quick Start, Configuration Reference, All Options, InvokeAgent semantic parameters, Sampling, A365 Exporter Environment Variables, OTLP Export, Auto-Instrumented Libraries, Default Instrumentations When `enable_a365=True`, Samples, Documentation

</details>

### mypy-boto3-comprehend

Type annotations for boto3 Comprehend 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-comprehend` · installs (wheel) · licence: MIT · rank 5014 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-comprehend/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Comprehend 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-comprehend docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-emr

Type annotations for boto3 EMR 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-emr` · installs (wheel) · licence: MIT · rank 5016 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-emr/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EMR 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-emr docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-cloudtrail

Type annotations for boto3 CloudTrail 1.43.90 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cloudtrail` · installs (wheel) · licence: MIT · rank 5030 · last release 2026-09-08 · [PyPI](https://pypi.org/project/mypy-boto3-cloudtrail/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudTrail 1.43.90 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cloudtrail docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-agents-hosting-fastapi

Integration library for Microsoft Agents with FastAPI

`pip install microsoft-agents-hosting-fastapi` · installs (wheel) · licence: MIT · rank 5031 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-hosting-fastapi/)

<details><summary>README extract</summary>

This library provides FastAPI integration for Microsoft Agents, enabling you to build conversational agents using the FastAPI web framework.

Features:
- FastAPI integration for Microsoft Agents
- JWT authorization middleware
- Channel service API endpoints
- Streaming response support
- Cloud adapter for processing agent activities

Example:
```python
from fastapi import FastAPI, Request
from microsoft_agents.hosting.fastapi import start_agent_process, CloudAdapter
from microsoft_agents.hosting.core.app import AgentApplication

app = FastAPI()
connection_manager = MsalConnectionManager(**agents_sdk_config)
adapter = CloudAdapter(connection_manager=connection_manager)
...
```

Sections: Microsoft Agents Hosting FastAPI, Packages Overview, Features, Usage

</details>

### mypy-boto3-resourcegroupstaggingapi

Type annotations for boto3 ResourceGroupsTaggingAPI 1.43.15 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-resourcegroupstaggingapi` · installs (wheel) · licence: MIT · rank 5057 · last release 2026-05-26 · [PyPI](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ResourceGroupsTaggingAPI 1.43.15
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-resourcegroupstaggingapi docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-appflow

Type annotations for boto3 Appflow 1.43.90 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-appflow` · installs (wheel) · licence: MIT · rank 5091 · last release 2026-09-08 · [PyPI](https://pypi.org/project/mypy-boto3-appflow/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Appflow 1.43.90
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-appflow docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-sagemaker-runtime

Type annotations for boto3 SageMakerRuntime 1.43.68 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sagemaker-runtime` · installs (wheel) · licence: MIT · rank 5094 · last release 2026-08-10 · [PyPI](https://pypi.org/project/mypy-boto3-sagemaker-runtime/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 SageMakerRuntime 1.43.68 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sagemaker-runtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-s3control

Type annotations for boto3 S3Control 1.43.90 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-s3control` · installs (wheel) · licence: MIT · rank 5098 · last release 2026-09-08 · [PyPI](https://pypi.org/project/mypy-boto3-s3control/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 S3Control 1.43.90
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-s3control docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcp-server-time

A Model Context Protocol server providing tools for time queries and timezone conversions for LLMs

`pip install mcp-server-time` · installs (wheel) · licence: MIT License · rank 5100 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mcp-server-time/) · [source](https://github.com/modelcontextprotocol/servers/tree/main/src/time)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.modelcontextprotocol/server-time -->

A Model Context Protocol server that provides time and timezone conversion capabilities. This server enables LLMs to get current time information and perform timezone conversions using IANA timezone names, with automatic system timezone detection.

Source: ...

Sections: Time MCP Server, Available Tools, Results and errors, Using uv (recommended), Using PIP, Configuration, Configure for Claude.app, Configure for Zed, Configure for VS Code, Configure for Zencoder, Customization - System Timezone, Example Interactions, Debugging, Examples of Questions for Claude

</details>

### magiccube

NxNxN Rubik Cube implementation

`pip install magiccube` · installs (wheel) · licence: BSD-3-Clause · rank 5101 · last release 2025-04-27 · [PyPI](https://pypi.org/project/magiccube/)

<details><summary>README extract</summary>

A fast implementation of the Rubik Cube based in Python 3.x.

Makes it easy to create cubes of various sizes (2x2x2, 3x3x3, 4x4x4, 6x6x6, ...., 100x100x100).

Fast rotation speed when compared with other Python implementations, which makes it suitable for Rubik Cube simulations.

Includes:

- Simple solver for the 3x3x3 cube. ...

Example:
```python
import magiccube

# 3x3x3 Cube
cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
print(cube)
```

Sections: MagicCube: A NxNxN Rubik Cube implementation, Usage, Documentation and Examples, Basic moves, Advanced Moves, Cube Coordinates, Solver, Move Optimizer

</details>

### mypy-boto3-identitystore

Type annotations for boto3 IdentityStore 1.43.105 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-identitystore` · installs (wheel) · licence: MIT · rank 5158 · last release 2026-09-29 · [PyPI](https://pypi.org/project/mypy-boto3-identitystore/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 IdentityStore 1.43.105 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-identitystore docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microsoft-teams-apps

The app package for a Microsoft Teams agent

`pip install microsoft-teams-apps` · installs (wheel) · licence: MIT · rank 5161 · last release 2026-11-05 · [PyPI](https://pypi.org/project/microsoft-teams-apps/)

<details><summary>README extract</summary>

High-level framework for building Microsoft Teams applications.
Handles activity routing, authentication, and provides Microsoft Graph integration.

Features:
- Activity Routing: Decorator-based routing for different activity types
- OAuth Integration: Built-in OAuth flow handling for user authentication ...

Example:
```python
from microsoft_teams.apps import App, ActivityContext
from microsoft_teams.api import MessageActivity

app = App()

@app.on_message
async def handle_message(ctx: ActivityContext[MessageActivity]):
    await ctx.send(f"You said: {ctx.activity.text}")

# Start the app
await app.start()
```

Sections: Microsoft Teams Apps Framework, Features, Basic Usage, Unauthenticated Requests, OAuth and Graph Integration, Optional Graph Dependencies

</details>

### mypy-boto3-elasticache

Type annotations for boto3 ElastiCache 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-elasticache` · installs (wheel) · licence: MIT · rank 5163 · last release 2026-10-20 · [PyPI](https://pypi.org/project/mypy-boto3-elasticache/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElastiCache 1.43.116 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-elasticache docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-cloudfront

Type annotations for boto3 CloudFront 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cloudfront` · installs (wheel) · licence: MIT · rank 5178 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mypy-boto3-cloudfront/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudFront 1.43.114 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cloudfront docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-codepipeline

Type annotations for boto3 CodePipeline 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codepipeline` · installs (wheel) · licence: MIT · rank 5195 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-codepipeline/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodePipeline 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codepipeline docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-wafv2

Type annotations for boto3 WAFV2 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-wafv2` · installs (wheel) · licence: MIT · rank 5247 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-wafv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 WAFV2 1.43.125
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-wafv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-opensearch

Type annotations for boto3 OpenSearchService 1.43.121 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-opensearch` · installs (wheel) · licence: MIT · rank 5268 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mypy-boto3-opensearch/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearch/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 OpenSearchService 1.43.121 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-opensearch docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-application-autoscaling

Type annotations for boto3 ApplicationAutoScaling 1.43.33 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-application-autoscaling` · installs (wheel) · licence: MIT · rank 5273 · last release 2026-06-18 · [PyPI](https://pypi.org/project/mypy-boto3-application-autoscaling/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ApplicationAutoScaling 1.43.33
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-application-autoscaling docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozilla-repo-urls

Process Mozilla's repository URLs. The intent is to centralize URLs parsing.

`pip install mozilla-repo-urls` · installs (wheel) · licence: MPL-2.0 · rank 5279 · last release 2025-06-03 · [PyPI](https://pypi.org/project/mozilla-repo-urls/)

<details><summary>README extract</summary>

Process Mozilla's repository URLs. The intent is to centralize URLs parsing.

1. `uv tool install tox --with tox-uv`
1. `uv tool run tox -e py313`

Sections: mozilla-repo-urls, Running tests

</details>

### mailchimp-transactional

Mailchimp Transactional API

`pip install mailchimp-transactional` · installs (wheel) · licence: not stated · rank 5281 · last release 2026-03-24 · [PyPI](https://pypi.org/project/mailchimp-transactional/)

<details><summary>README extract</summary>

No description provided (generated by Swagger Codegen # noqa: E501

</details>

### mypy-boto3-bedrock-agentcore

Type annotations for boto3 BedrockAgentCore 1.43.122 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock-agentcore` · installs (wheel) · licence: MIT · rank 5283 · last release 2026-10-29 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock-agentcore/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 BedrockAgentCore 1.43.122 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock-agentcore docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-sso-admin

Type annotations for boto3 SSOAdmin 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sso-admin` · installs (wheel) · licence: MIT · rank 5297 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mypy-boto3-sso-admin/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SSOAdmin 1.43.119
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sso-admin docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### matrix-nio

A Python Matrix client library, designed according to sans I/O principles.

`pip install matrix-nio` · installs (wheel) · licence: not stated · rank 5306 · last release 2026-07-23 · [PyPI](https://pypi.org/project/matrix-nio/) · [docs](https://matrix-nio.readthedocs.io/en/latest/) · [source](https://github.com/matrix-nio/matrix-nio)

<details><summary>README extract</summary>

nio is a multilayered Matrix client library. The
underlying base layer doesn't do any network IO on its own, but on top of that
is a full-fledged batteries-included asyncio layer using
aiohttp. File IO is only done if you
enable end-to-end encryption (E2EE).

Documentation

The full API documentation for nio can be found at

Features ...

</details>

### mosaicml-streaming

Streaming lets users create PyTorch compatible datasets that can be streamed from cloud-based object stores

`pip install mosaicml-streaming` · installs (wheel) · licence: not stated · rank 5326 · last release 2025-07-15 · [PyPI](https://pypi.org/project/mosaicml-streaming/)

<details><summary>README extract</summary>

[Website]
- [Quick Start]
- [Docs]
- [We're Hiring!]

We built StreamingDataset to make training on large datasets from cloud storage as fast, cheap, and scalable as possible.

It’s specially designed for multi-node, distributed training for large models—maximizing correctness guarantees, performance, and ease of use. ...

Example:
```python
dataset = StreamingDataset(
    cache_limit='100gb',
    ...
)
```

Sections: 👋 Welcome, 🚀 Getting Started, 🏁 Quick Start, 1. Prepare Your Data, 2. Upload Your Data to Cloud Storage, 3. Build a StreamingDataset and DataLoader, 📚 What next?, 🔑 Key Features, Seamless data mixing, True Determinism, Instant mid-epoch resumption, High throughput, Equal convergence, Random access

</details>

### mypy-boto3-ce

Type annotations for boto3 CostExplorer 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ce` · installs (wheel) · licence: MIT · rank 5329 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-ce/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CostExplorer 1.43.110 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ce docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-apigatewayv2

Type annotations for boto3 ApiGatewayV2 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-apigatewayv2` · installs (wheel) · licence: MIT · rank 5333 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-apigatewayv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ApiGatewayV2 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-apigatewayv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### maxminddb-geolite2

Provides access to the geolite2 database. This product includes GeoLite2 data created by MaxMind, available from http://www.maxmind.com/

`pip install maxminddb-geolite2` · installs from source (sdist only) · licence: not stated · rank 5357 · last release 2018-07-18 · [PyPI](https://pypi.org/project/maxminddb-geolite2/)

### mypy-boto3-iot

Type annotations for boto3 IoT 1.43.102 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-iot` · installs (wheel) · licence: MIT · rank 5381 · last release 2026-09-24 · [PyPI](https://pypi.org/project/mypy-boto3-iot/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 IoT 1.43.102
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-iot docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-cognito-identity

Type annotations for boto3 CognitoIdentity 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cognito-identity` · installs (wheel) · licence: MIT · rank 5411 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-cognito-identity/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CognitoIdentity 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cognito-identity docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-redshift

Type annotations for boto3 Redshift 1.43.75 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-redshift` · installs (wheel) · licence: MIT · rank 5527 · last release 2026-08-19 · [PyPI](https://pypi.org/project/mypy-boto3-redshift/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Redshift 1.43.75
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-redshift docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-rds-data

Type annotations for boto3 RDSDataService 1.43.37 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-rds-data` · installs (wheel) · licence: MIT · rank 5544 · last release 2026-06-29 · [PyPI](https://pypi.org/project/mypy-boto3-rds-data/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds_data/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 RDSDataService 1.43.37 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-rds-data docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### merge3

Python implementation of 3-way merge

`pip install merge3` · installs (wheel) · licence: GPL-2.0-or-later · rank 5560 · last release 2026-10-25 · [PyPI](https://pypi.org/project/merge3/) · [source](https://github.com/breezy-team/merge3)

_README extract left out: share-alike licence._

### mypy-boto3-transcribe

Type annotations for boto3 TranscribeService 1.43.98 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-transcribe` · installs (wheel) · licence: MIT · rank 5623 · last release 2026-09-18 · [PyPI](https://pypi.org/project/mypy-boto3-transcribe/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 TranscribeService 1.43.98 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-transcribe docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-codeartifact

Type annotations for boto3 CodeArtifact 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codeartifact` · installs (wheel) · licence: MIT · rank 5624 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-codeartifact/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodeArtifact 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codeartifact docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### matscipy

Generic Python Materials Science tools

`pip install matscipy` · installs (wheel) · licence: not stated · rank 5626 · last release 2026-10-13 · [PyPI](https://pypi.org/project/matscipy/) · [docs](http://libatoms.github.io/matscipy/) · [source](https://github.com/libAtoms/matscipy)

<details><summary>README extract</summary>

Matscipy is a generic materials science toolbox built around the Atomic
Simulation Environment (ASE). It provides
useful routines for:

- Plasticity and dislocations
- Fracture mechanics
- Electro-chemistry
- Tribology
- Elastic properties

In addition to domain-specific routines, it also implements a set of
general-purpose, low-level utilities: ...

Sections: Matscipy, Quick start, Documentation, Seeking help, Running tests, Dependencies, Citing matscipy

</details>

### mlx-whisper

OpenAI Whisper on Apple silicon with MLX and the Hugging Face Hub

`pip install mlx-whisper` · installs (wheel) · licence: MIT · rank 5641 · last release 2025-08-29 · [PyPI](https://pypi.org/project/mlx-whisper/)

<details><summary>README extract</summary>

Speech recognition with Whisper in MLX. Whisper is a set of open source speech
recognition models from OpenAI, ranging from 39 million to 1.5 billion
parameters.[^1]

Install `ffmpeg`:

Install the `mlx-whisper` package with:

Example:
```python
import mlx_whisper

text = mlx_whisper.transcribe(speech_file)["text"]
```

Sections: Whisper, Setup, Run, CLI, API, Converting models

</details>

### murmurhash2

murmurhash2 for Python

`pip install murmurhash2` · installs (wheel) · licence: MIT · rank 5646 · last release 2022-02-12 · [PyPI](https://pypi.org/project/murmurhash2/) · [source](https://github.com/messense/murmurhash2-py)

<details><summary>README extract</summary>

32-bit murmurhash2 & 3 for Python

Example:
```python
from murmurhash2 import murmurhash2, murmurhash3

SEED = 3242157231
print(murmurhash2(b'key', SEED))
print(murmurhash3(b'key', SEED))
```

Sections: murmurhash2-py, Usage

</details>

### mypy-boto3-transfer

Type annotations for boto3 Transfer 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-transfer` · installs (wheel) · licence: MIT · rank 5647 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mypy-boto3-transfer/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Transfer 1.43.114
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-transfer docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mplcursors

Interactive data selection cursors for Matplotlib.

`pip install mplcursors` · installs (wheel) · licence: not stated · rank 5672 · last release 2026-03-18 · [PyPI](https://pypi.org/project/mplcursors/) · [source](https://github.com/anntzer/mplcursors)

<details><summary>README extract</summary>

GitHubPyPI|
Read the DocsBuild|

mplcursors provides interactive data selection cursors for Matplotlib. It is
inspired from mpldatacursor, with a much simplified API.

mplcursors requires Matplotlib\≥3.1.

Read the documentation on readthedocs.org.

As usual, install using pip:

or your favorite package manager.

Run tests with pytest.

</details>

### mypy-boto3-servicediscovery

Type annotations for boto3 ServiceDiscovery 1.43.48 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-servicediscovery` · installs (wheel) · licence: MIT · rank 5698 · last release 2026-07-14 · [PyPI](https://pypi.org/project/mypy-boto3-servicediscovery/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ServiceDiscovery 1.43.48 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-servicediscovery docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mailchimp-marketing

Mailchimp Marketing API

`pip install mailchimp-marketing` · installs (wheel) · licence: not stated · rank 5772 · last release 2022-11-02 · [PyPI](https://pypi.org/project/mailchimp-marketing/)

<details><summary>README extract</summary>

No description provided (generated by Swagger Codegen # noqa: E501

</details>

### mpld3

D3 Viewer for Matplotlib

`pip install mpld3` · installs (wheel) · licence: BSD License · rank 5780 · last release 2025-11-05 · [PyPI](https://pypi.org/project/mpld3/)

<details><summary>README extract</summary>

- Maintainers: @vladh, @cliffckerr
- Status: I (@vladh) am not currently able to dedicate much time to resolving mpld3 issues.
 However, I _will_ gladly look at your pull request and review it. ...

</details>

### mcp-grafana

Grafana MCP server - interact with Grafana via the Model Context Protocol

`pip install mcp-grafana` · installs (wheel) · licence: Apache-2.0 · rank 5782 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mcp-grafana/)

<details><summary>README extract</summary>

A Model Context Protocol (MCP) server for Grafana.

This provides access to your Grafana instance and the surrounding ecosystem.

Features:
_The following features are currently available in MCP server. This list is for informational purposes only and does not represent a roadmap or commitment to future features._

Sections: Grafana MCP server, Quick Start, Requirements, Features, Dashboards, Run Panel Query, Context Window Management, Datasources, Query Examples, Prometheus Querying, Loki Querying, InfluxDB Querying, SQL Datasource Querying, CloudWatch Querying

</details>

### mypy-boto3-codedeploy

Type annotations for boto3 CodeDeploy 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codedeploy` · installs (wheel) · licence: MIT · rank 5813 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-codedeploy/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodeDeploy 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codedeploy docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### metaflow

Metaflow: More AI and ML, Less Engineering

`pip install metaflow` · installs (wheel) · licence: Apache Software License · rank 5846 · last release 2026-11-06 · [PyPI](https://pypi.org/project/metaflow/) · [docs](https://docs.metaflow.org) · [source](https://github.com/Netflix/metaflow)

<details><summary>README extract</summary>

Metaflow is a human-centric framework designed to help scientists and engineers build and manage real-life AI and ML systems. Serving teams of all sizes and scale, Metaflow streamlines the entire development lifecycle—from rapid prototyping in notebooks to reliable, maintainable production deployments—enabling teams to iterate quickly and deliver ...

Sections: Metaflow, From prototype to production (and back), Getting started, Deploying infrastructure for Metaflow in your cloud, Get in touch

</details>

### mypy-boto3-s3tables

Type annotations for boto3 S3Tables 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-s3tables` · installs (wheel) · licence: MIT · rank 5860 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-s3tables/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 S3Tables 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-s3tables docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-appconfig

Type annotations for boto3 AppConfig 1.43.43 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-appconfig` · installs (wheel) · licence: MIT · rank 5870 · last release 2026-07-08 · [PyPI](https://pypi.org/project/mypy-boto3-appconfig/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 AppConfig 1.43.43
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-appconfig docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mysql-replication

Pure Python Implementation of MySQL replication protocol build on top of PyMYSQL.

`pip install mysql-replication` · installs (wheel) · licence: Apache 2 · rank 5902 · last release 2026-08-06 · [PyPI](https://pypi.org/project/mysql-replication/)

<details><summary>README extract</summary>

Pure Python Implementation of MySQL replication protocol build on top of PyMYSQL. This allows you to receive event like insert, update, delete with their datas and raw SQL queries.

- MySQL to NoSQL database replication
- MySQL to search engine replication
- Invalidate cache when something change in database
- Audit
- Real time analytics ...

Sections: python-mysql-replication, Use cases, Documentation, Limitations, Featured, AWS blog, Books, Blogs, Projects using this library

</details>

### mypy-boto3-appconfigdata

Type annotations for boto3 AppConfigData 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-appconfigdata` · installs (wheel) · licence: MIT · rank 5917 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-appconfigdata/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AppConfigData 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-appconfigdata docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mssql-django

Django backend for Microsoft SQL Server

`pip install mssql-django` · installs (wheel) · licence: BSD License · rank 5939 · last release 2026-09-18 · [PyPI](https://pypi.org/project/mssql-django/)

<details><summary>README extract</summary>

mssql-django is the official Microsoft‑supported Django database backend for SQL Server, Azure SQL and SQL Database in Microsoft Fabric.

It provides a reliable, enterprise‑grade database connectivity option for the Django web framework, enabling Python developers to build and run production‑ready applications on Microsoft’s data platform. ...

Sections: Django Backend for Microsoft SQL, Quick Start, Configuration Reference, Standard Django Settings, TEST Settings, OPTIONS, Disabling MARS, Selecting the database driver, Backend-Specific Settings, Known Limitations, Version-Specific Notes, Helpful Links, Still have questions?, Trademarks

</details>

### mypy-boto3-dms

Type annotations for boto3 DatabaseMigrationService 1.43.59 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dms` · installs (wheel) · licence: MIT · rank 5940 · last release 2026-07-29 · [PyPI](https://pypi.org/project/mypy-boto3-dms/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 DatabaseMigrationService 1.43.59
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dms docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mermaid-builder

MermaidJS markup builder for Python

`pip install mermaid-builder` · installs (wheel) · licence: MIT License · rank 5949 · last release 2024-06-14 · [PyPI](https://pypi.org/project/mermaid-builder/)

<details><summary>README extract</summary>

MermaidJS Markup builder helps to script MermaidJS markup creation.

MermaidJS is an amazing product, but the syntax is very human readable and writeable (comparing to graphviz for exmaple).

for example, node or arrow shape on a flowchart is something that is easy to see as ASCII, but not easy to adhoc script. ...

Example:
```python
chart = (Chart(title='test1')
    .add_node('user')
    .add_node('client')
    .add_node('server')
    .add_node('database')
    .add_link_between('user', 'client')
    .add_link_between('client', 'server')
    .add_link_between('server', 'database'))
```

Sections: Python MermaidJS Markup Builder, NOTE: This is Work in progress, Examples, Flow chart, untyped version, OOP (more complicated version), Sequence diagram, Run tests

</details>

### mypy-boto3-bedrock-agentcore-control

Type annotations for boto3 BedrockAgentCoreControl 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock-agentcore-control` · installs (wheel) · licence: MIT · rank 5961 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock-agentcore-control/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 BedrockAgentCoreControl 1.43.125
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock-agentcore-control docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-docdb

Type annotations for boto3 DocDB 1.43.123 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-docdb` · installs (wheel) · licence: MIT · rank 6012 · last release 2026-10-30 · [PyPI](https://pypi.org/project/mypy-boto3-docdb/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 DocDB 1.43.123
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-docdb docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-codecommit

Type annotations for boto3 CodeCommit 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codecommit` · installs (wheel) · licence: MIT · rank 6036 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-codecommit/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecommit/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodeCommit 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codecommit docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### meraki

Cisco Meraki Dashboard API library

`pip install meraki` · installs (wheel) · licence: MIT License · rank 6038 · last release 2026-10-17 · [PyPI](https://pypi.org/project/meraki/) · [source](https://github.com/meraki/dashboard-api-python)

<details><summary>README extract</summary>

A Python client for the Cisco Meraki dashboard API, covering every
current operation. It's generated from the API's OpenAPI spec, so it tracks the latest releases automatically. The full
source, including the generator, is here for Early Access participants and contributors; pull requests that maintain
backwards compatibility are welcome. ...

Example:
```python
import meraki
```

Sections: Meraki Dashboard API Python Library, Features, Setup, Usage, Examples, Keyword argument validation, Smart flow rate limiting, AsyncIO, Further documentation

</details>

### mypy-boto3-timestream-write

Type annotations for boto3 TimestreamWrite 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-timestream-write` · installs (wheel) · licence: MIT · rank 6042 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-timestream-write/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 TimestreamWrite 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-timestream-write docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-pi

Type annotations for boto3 PI 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-pi` · installs (wheel) · licence: MIT · rank 6055 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-pi/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 PI 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-pi docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-neptune

Type annotations for boto3 Neptune 1.43.28 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-neptune` · installs (wheel) · licence: MIT · rank 6059 · last release 2026-06-11 · [PyPI](https://pypi.org/project/mypy-boto3-neptune/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Neptune 1.43.28
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-neptune docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-es

Type annotations for boto3 ElasticsearchService 1.43.47 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-es` · installs (wheel) · licence: MIT · rank 6065 · last release 2026-07-13 · [PyPI](https://pypi.org/project/mypy-boto3-es/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElasticsearchService 1.43.47
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-es docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-acm-pca

Type annotations for boto3 ACMPCA 1.43.65 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-acm-pca` · installs (wheel) · licence: MIT · rank 6066 · last release 2026-08-05 · [PyPI](https://pypi.org/project/mypy-boto3-acm-pca/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 ACMPCA 1.43.65
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-acm-pca docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-route53resolver

Type annotations for boto3 Route53Resolver 1.43.102 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-route53resolver` · installs (wheel) · licence: MIT · rank 6072 · last release 2026-09-24 · [PyPI](https://pypi.org/project/mypy-boto3-route53resolver/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Route53Resolver 1.43.102 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-route53resolver docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-ram

Type annotations for boto3 RAM 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ram` · installs (wheel) · licence: MIT · rank 6092 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-ram/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 RAM 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ram docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-iot-data

Type annotations for boto3 IoTDataPlane 1.43.17 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-iot-data` · installs (wheel) · licence: MIT · rank 6093 · last release 2026-05-28 · [PyPI](https://pypi.org/project/mypy-boto3-iot-data/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 IoTDataPlane 1.43.17 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-iot-data docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-fis

Type annotations for boto3 FIS 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-fis` · installs (wheel) · licence: MIT · rank 6099 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-fis/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 FIS 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-fis docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### macaroonbakery

A Python library port for bakery, higher level operation to work with macaroons

`pip install macaroonbakery` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6101 · last release 2023-12-13 · [PyPI](https://pypi.org/project/macaroonbakery/)

_README extract left out: share-alike licence._

### mypy-boto3-elasticbeanstalk

Type annotations for boto3 ElasticBeanstalk 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-elasticbeanstalk` · installs (wheel) · licence: MIT · rank 6116 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-elasticbeanstalk/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElasticBeanstalk 1.43.124 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-elasticbeanstalk docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-dynamodbstreams

Type annotations for boto3 DynamoDBStreams 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dynamodbstreams` · installs (wheel) · licence: MIT · rank 6187 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mypy-boto3-dynamodbstreams/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 DynamoDBStreams 1.43.114 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dynamodbstreams docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-timestream-query

Type annotations for boto3 TimestreamQuery 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-timestream-query` · installs (wheel) · licence: MIT · rank 6191 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-timestream-query/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 TimestreamQuery 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-timestream-query docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-amplify

Type annotations for boto3 Amplify 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-amplify` · installs (wheel) · licence: MIT · rank 6206 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-amplify/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Amplify 1.43.115
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-amplify docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### Mosek

Python API for Mosek

`pip install Mosek` · installs (wheel) · licence: https://mosek.com/products/license-agreement · rank 6208 · last release 2026-11-05 · [PyPI](https://pypi.org/project/Mosek/)

<details><summary>README extract</summary>

MOSEK is a package for large-scale convex and mixed-integer optimization,
including LP, QP, SOCP, exponential and power cone problems, SDP, QCQP and MIP.
Documentation and examples can be found at the
MOSEK requires a license. Free of charge trial
licenses as well as licenses for non-commercial academic use can be obtained
from

</details>

### mypy-boto3-mwaa

Type annotations for boto3 MWAA 1.43.87 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-mwaa` · installs (wheel) · licence: MIT · rank 6212 · last release 2026-09-02 · [PyPI](https://pypi.org/project/mypy-boto3-mwaa/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 MWAA 1.43.87
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-mwaa docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-kafka

Type annotations for boto3 Kafka 1.43.79 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kafka` · installs (wheel) · licence: MIT · rank 6217 · last release 2026-08-24 · [PyPI](https://pypi.org/project/mypy-boto3-kafka/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kafka/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Kafka 1.43.79
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kafka docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-mediaconvert

Type annotations for boto3 MediaConvert 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-mediaconvert` · installs (wheel) · licence: MIT · rank 6260 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-mediaconvert/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 MediaConvert 1.43.126 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-mediaconvert docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-appsync

Type annotations for boto3 AppSync 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-appsync` · installs (wheel) · licence: MIT · rank 6261 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-appsync/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 AppSync 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-appsync docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-lambda-microvms

Type annotations for boto3 LambdaMicroVMs 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-lambda-microvms` · installs (wheel) · licence: MIT · rank 6295 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-lambda-microvms/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda_microvms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 LambdaMicroVMs 1.43.125 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-lambda-microvms docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-verifiedpermissions

Type annotations for boto3 VerifiedPermissions 1.43.13 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-verifiedpermissions` · installs (wheel) · licence: MIT · rank 6305 · last release 2026-05-21 · [PyPI](https://pypi.org/project/mypy-boto3-verifiedpermissions/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 VerifiedPermissions 1.43.13 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-verifiedpermissions docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-elb

Type annotations for boto3 ElasticLoadBalancing 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-elb` · installs (wheel) · licence: MIT · rank 6312 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-elb/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ElasticLoadBalancing 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-elb docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-resource-groups

Type annotations for boto3 ResourceGroups 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-resource-groups` · installs (wheel) · licence: MIT · rank 6317 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-resource-groups/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ResourceGroups 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-resource-groups docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-kinesisanalyticsv2

Type annotations for boto3 KinesisAnalyticsV2 1.43.51 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kinesisanalyticsv2` · installs (wheel) · licence: MIT · rank 6323 · last release 2026-07-17 · [PyPI](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 KinesisAnalyticsV2 1.43.51 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kinesisanalyticsv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-pinpoint

Type annotations for boto3 Pinpoint 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-pinpoint` · installs (wheel) · licence: MIT · rank 6326 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-pinpoint/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Pinpoint 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-pinpoint docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mlforecast

Scalable machine learning based time series forecasting

`pip install mlforecast` · installs (wheel) · licence: Apache Software License · rank 6327 · last release 2026-07-10 · [PyPI](https://pypi.org/project/mlforecast/) · [docs](https://nixtlaverse.nixtla.io/mlforecast/) · [source](https://github.com/Nixtla/mlforecast)

<details><summary>README extract</summary>

mlforecast is a framework to perform time series forecasting using
machine learning models, with the option to scale to massive amounts of
data using remote clusters.

Features:
Current Python alternatives for machine learning models are slow,
inaccurate and don’t scale well. So we created a library that can be
used to forecast in production environments. ...

Example:
```python
from mlforecast.utils import generate_daily_series

series = generate_daily_series(
    n_series=20,
    max_length=100,
    n_static_features=1,
    static_as_categorical=False,
    with_trend=True
)
series.head()
```

...

</details>

### mypy-boto3-serverlessrepo

Type annotations for boto3 ServerlessApplicationRepository 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-serverlessrepo` · installs (wheel) · licence: MIT · rank 6347 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-serverlessrepo/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ServerlessApplicationRepository 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-serverlessrepo docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-kinesisanalytics

Type annotations for boto3 KinesisAnalytics 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kinesisanalytics` · installs (wheel) · licence: MIT · rank 6352 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-kinesisanalytics/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 KinesisAnalytics 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kinesisanalytics docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-glacier

Type annotations for boto3 Glacier 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-glacier` · installs (wheel) · licence: MIT · rank 6356 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-glacier/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Glacier 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-glacier docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-dataexchange

Type annotations for boto3 DataExchange 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dataexchange` · installs (wheel) · licence: MIT · rank 6360 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-dataexchange/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 DataExchange 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dataexchange docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-codestar-connections

Type annotations for boto3 CodeStarconnections 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codestar-connections` · installs (wheel) · licence: MIT · rank 6372 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-codestar-connections/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodeStarconnections 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codestar-connections docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-managedblockchain

Type annotations for boto3 ManagedBlockchain 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-managedblockchain` · installs (wheel) · licence: MIT · rank 6374 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-managedblockchain/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ManagedBlockchain 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-managedblockchain docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-mq

Type annotations for boto3 MQ 1.43.48 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-mq` · installs (wheel) · licence: MIT · rank 6379 · last release 2026-07-14 · [PyPI](https://pypi.org/project/mypy-boto3-mq/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 MQ 1.43.48
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-mq docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-iotwireless

Type annotations for boto3 IoTWireless 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-iotwireless` · installs (wheel) · licence: MIT · rank 6397 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-iotwireless/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 IoTWireless 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-iotwireless docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-cloudcontrol

Type annotations for boto3 CloudControlApi 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-cloudcontrol` · installs (wheel) · licence: MIT · rank 6410 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-cloudcontrol/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CloudControlApi 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-cloudcontrol docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mode-streaming

AsyncIO Service-based programming

`pip install mode-streaming` · installs (wheel) · licence: BSD License · rank 6424 · last release 2026-08-12 · [PyPI](https://pypi.org/project/mode-streaming/) · [docs](https://faust-streaming.github.io/mode/) · [source](https://github.com/faust-streaming/mode)

<details><summary>README extract</summary>

Documentation:

Source Code:

Features:
We have decided to fork the original *Mode* project because there is a critical process of releasing new versions which causes uncertainty in the community. Everybody is welcome to contribute to this *fork*, and you can be added as a maintainer. ...

Example:
```python
class PageViewCache(Service):
    redis: Redis = None

    async def on_start(self) -> None:
        self.redis = connect_to_redis()

    async def update(self, url: str, n: int = 1) -> int:
        return await self.redis.incr(url, n)

    async def get(self, url: str) -> int:
        return await self.redis.get(url)
```

...

</details>

### mypy-boto3-codeconnections

Type annotations for boto3 CodeConnections 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-codeconnections` · installs (wheel) · licence: MIT · rank 6459 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-codeconnections/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 CodeConnections 1.43.115 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-codeconnections docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-pipes

Type annotations for boto3 EventBridgePipes 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-pipes` · installs (wheel) · licence: MIT · rank 6465 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-pipes/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pipes/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EventBridgePipes 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-pipes docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### minisbd

Free and open source library for fast sentence boundary detection

`pip install minisbd` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 6466 · last release 2026-03-03 · [PyPI](https://pypi.org/project/minisbd/) · [docs](https://github.com/LibreTranslate/MiniSBD) · [source](https://github.com/LibreTranslate/MiniSBD)

_README extract left out: share-alike licence._

### mypy-boto3-bedrock-agent-runtime

Type annotations for boto3 AgentsforBedrockRuntime 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock-agent-runtime` · installs (wheel) · licence: MIT · rank 6523 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock-agent-runtime/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AgentsforBedrockRuntime 1.43.125
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock-agent-runtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mlx-audio

MLX-Audio is a package for inference of text-to-speech (TTS) and speech-to-speech (STS) models locally on your Mac using MLX

`pip install mlx-audio` · installs (wheel) · licence: MIT · rank 6553 · last release 2026-11-02 · [PyPI](https://pypi.org/project/mlx-audio/) · [source](https://github.com/Blaizzy/mlx-audio)

<details><summary>README extract</summary>

The best audio processing library built on Apple's MLX framework, providing fast and efficient text-to-speech (TTS), speech-to-text (STT), speech-to-speech (STS), music generation, and more on Apple Silicon.

Features:
- Fast inference optimized for Apple Silicon (M series chips)
- Multiple model architectures for TTS, STT, STS, and music generation
- Multilingual support across models
- Voice customization and cloning capabilities ...

Example:
```python
from mlx_audio.tts.utils import load_model

# Load model
model = load_model("mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-8bit")

# Generate speech
for result in model.generate(
    "Hello from MLX-Audio!",
    voice="Vivian",
    lang_code="English",
):
    print(f"Generated {result.audio.shape[0]} samples")
...
```

...

</details>

### mypy-boto3-dax

Type annotations for boto3 DAX 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dax` · installs (wheel) · licence: MIT · rank 6566 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-dax/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 DAX 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dax docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-bedrock-agent

Type annotations for boto3 AgentsforBedrock 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-bedrock-agent` · installs (wheel) · licence: MIT · rank 6612 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-bedrock-agent/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AgentsforBedrock 1.43.126 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-bedrock-agent docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozfile

Library of file utilities for use in Mozilla testing

`pip install mozfile` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6633 · last release 2022-10-13 · [PyPI](https://pypi.org/project/mozfile/)

### manygo

Python library with helpers for packaging golang source code

`pip install manygo` · installs (wheel) · licence: MIT · rank 6657 · last release 2026-09-25 · [PyPI](https://pypi.org/project/manygo/) · [source](https://github.com/jmelahman/manygo)

<details><summary>README extract</summary>

A Python library for generating platform-specific tags for Golang packages and binaries.

Features:
- Convert Golang platform identifiers (GOOS and GOARCH) to Python platform tags

Example:
```python
>>> import manygo
>>> manygo.get_platform_tag('linux', 'amd64')
'manylinux_2_17_x86_64'

>>> manygo.get_platform_tag('darwin', 'arm64')
'macosx_11_0_arm64'
```

Sections: manygo, Features, Usage

</details>

### mypy-gitlab-code-quality

Simple script to generate gitlab code quality report from output of mypy.

`pip install mypy-gitlab-code-quality` · installs (wheel) · licence: MIT License · rank 6667 · last release 2025-03-31 · [PyPI](https://pypi.org/project/mypy-gitlab-code-quality/)

<details><summary>README extract</summary>

Simple script to generate gitlab code quality report
from output of mypy.

Example gitlab codequality report from gitlab documentation:

Sections: mypy-gitlab-code-quality, Usage, Example .gitlab-ci.yml

</details>

### mkdocs-jupyter

Use Jupyter in mkdocs websites

`pip install mkdocs-jupyter` · installs (wheel) · licence: Apache-2.0 · rank 6698 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mkdocs-jupyter/) · [docs](https://github.com/danielfrg/mkdocs-jupyter#readme) · [source](https://github.com/danielfrg/mkdocs-jupyter)

<details><summary>README extract</summary>

- Docs demo Site
- Add Jupyter Notebooks directly to the mkdocs navigation

 - `.ipynb` and `.py` files (using
 jupytext)
- Same style as regular Jupyter Notebooks
 - Support Jupyter Themes
- Option to execute the notebook before converting
- Support for ipywidgets
- Support for mkdocs TOC
- Option to include notebook source

Sections: mkdocs-jupyter: Use Jupyter Notebooks in mkdocs, Configuration, Markdown cell processor, Notebook page metadata, Including or Ignoring Files, Notebooks outside the docs directory, Execute Notebook, Kernel, Ignore Code Input, Remove Cell Using Tags, Jupyter themes, Custom notebook templates, HTML exporter options, Extra CSS classes

</details>

### ml-goodput-measurement

Package to monitor Goodput, Badput and other metrics of ML workloads.

`pip install ml-goodput-measurement` · installs (wheel) · licence: not stated · rank 6719 · last release 2026-08-17 · [PyPI](https://pypi.org/project/ml-goodput-measurement/)

<details><summary>README extract</summary>

<!--
 Copyright 2023 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at ...

Features:
ML Goodput Measurement is a library intended to be used with Cloud accelerators
 to log necessary information and query a job's Goodput and Badput Breakdown. ...

Example:
```python
from ml_goodput_measurement import goodput
from ml_goodput_measurement import monitoring
```

...

</details>

### maybe-else

Provides a Maybe class as a Python implementation of null-aware operators.

`pip install maybe-else` · installs (wheel) · licence: MIT · rank 6745 · last release 2019-11-14 · [PyPI](https://pypi.org/project/maybe-else/)

<details><summary>README extract</summary>

Features:
Provides a `Maybe` class which serves as a pseudo-implementation of null-aware operators in python:

* can be used to avoid common `var if var is not None else handle_none(var)` structures
* Null-aware item access
* Null-aware attribute access
* ...

Sections: Overview, Usage

</details>

### morefs

A collection of self-contained fsspec-based filesystems

`pip install morefs` · installs (wheel) · licence: Apache-2.0 · rank 6770 · last release 2024-07-08 · [PyPI](https://pypi.org/project/morefs/) · [source](https://github.com/iterative/morefs)

<details><summary>README extract</summary>

Features:
* `AsyncLocalFileSystem` that provides async implementation of `LocalFileSystem`.
* In-memory filesystems `DictFileSystem` built on nested dictionaries and `MemFS` built on tries, and are much faster than fsspec's `MemoryFileSystem`. ...

Example:
```python
import asyncio
from morefs.asyn_local import AsyncLocalFileSystem

async def main():
    fs = AsyncLocalFileSystem(auto_mkdir=False)

    f = await fs.open_async("foo", mode="w")
    async with f:
        await f.write("foobar")

    content = await fs._cat("foo")
    print(content)
    print(fs.cat("foo"))  # you can still use sync methods

...
```

Sections: morefs, Features, Usage, AsyncLocalFileSystem, DictFS, MemFS, OverlayFileSystem, Issues

</details>

### mwaa-dr

DR Solution for Amazon Managed Workflows for Apache Airflow (MWAA)

`pip install mwaa-dr` · installs (wheel) · licence: not stated · rank 6810 · last release 2026-03-30 · [PyPI](https://pypi.org/project/mwaa-dr/) · [docs](https://github.com/aws-samples/mwaa-disaster-recovery/blob/main/PYPIDOC.md) · [source](https://github.com/aws-samples/mwaa-disaster-recovery.git)

<details><summary>README extract</summary>

The `mwaa-dr` PyPi package is a part of the larger MWAA DR solution for the use case where exporting and importing metadata store needs to be performed independent to the broader DR solution. As of the time of writing, access to the MWAA metadata store is only available through DAGs. ...

Example:
```python
# Importing DAG is necessary for DAG detection
from airflow import DAG
from mwaa_dr.v_2_10.dr_factory import DRFactory_2_10

factory = DRFactory_2_10(
    dag_id='backup',
    path_prefix='data',
    storage_type='S3'
)

# Assigning the returned dag to a global variable is necessary for DAG detection
dag: DAG = factory.create_backup_dag()
```

Sections: MWAA Disaster Recovery, Simple Use Case, Metadata Backup DAG, Metadata Restore DAG, Metadata Cleanup DAG, Advance Use Case

</details>

### mcp-server-git

A Model Context Protocol server providing tools to read, search, and manipulate Git repositories programmatically via LLMs

`pip install mcp-server-git` · installs (wheel) · licence: MIT License · rank 6831 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mcp-server-git/) · [source](https://github.com/modelcontextprotocol/servers/tree/main/src/git)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.modelcontextprotocol/server-git -->

Features:
A Model Context Protocol server for Git repository interaction and automation. This server provides tools to read, search, and manipulate Git repositories via Large Language Models.

Source:

Requires MCP Python SDK 2.x (`mcp>=2.3,<3`). ...

Sections: mcp-server-git: A git MCP server, Overview, Tools, Errors, Prompts, Using uv (recommended), Using PIP, Configuration, Commit identity, Usage with Claude Desktop, Usage with VS Code, Usage with Zed, Usage with Zencoder, Debugging

</details>

### mozterm

Terminal abstractions built around the blessings module.

`pip install mozterm` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6882 · last release 2018-07-03 · [PyPI](https://pypi.org/project/mozterm/)

### mypy-boto3-service-quotas

Type annotations for boto3 ServiceQuotas 1.43.89 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-service-quotas` · installs (wheel) · licence: MIT · rank 6902 · last release 2026-09-04 · [PyPI](https://pypi.org/project/mypy-boto3-service-quotas/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ServiceQuotas 1.43.89 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-service-quotas docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mkdocs-exclude

A mkdocs plugin that lets you exclude files or trees.

`pip install mkdocs-exclude` · installs from source (sdist only) · licence: Apache · rank 6918 · last release 2019-02-20 · [PyPI](https://pypi.org/project/mkdocs-exclude/)

<details><summary>README extract</summary>

`mkdocs-exclude` is a
mkdocs plugin that allows you
to exclude files from your input using unix-style wildcards (globs) or
regular expressions (regexes).

This implements what people were asking for in some mkdocs bugs, such as
< and

Sections: File exclude plugin for mkdocs, Quick start

</details>

### marin-iris-native

Native runtime components for Iris.

`pip install marin-iris-native` · installs (wheel) · licence: not stated · rank 6925 · last release 2026-07-25 · [PyPI](https://pypi.org/project/marin-iris-native/)

### mlperf-logging

MLPerf compliance tools.

`pip install mlperf-logging` · installs (wheel) · licence: Apache Software License · rank 6937 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mlperf-logging/)

<details><summary>README extract</summary>

MLPerf Compliance Logging Utilities and Helper Functions

Sections: MLPerf Logging, Packages, Instructions

</details>

### mkdocs-awesome-nav

A plugin for customizing the navigation structure of your MkDocs site.

`pip install mkdocs-awesome-nav` · installs (wheel) · licence: MIT License · rank 6940 · last release 2025-12-02 · [PyPI](https://pypi.org/project/mkdocs-awesome-nav/) · [source](https://github.com/lukasgeiter/mkdocs-awesome-nav/)

<details><summary>README extract</summary>

> Formerly known as `mkdocs-awesome-pages-plugin`. Read more about the change

This MkDocs plugin gives you full control over your navigation structure without having to write the entire thing by hand. Whether you just want to add an external link or restructure the entire navigation tree, `awesome-nav` has you covered.

Features:
- Adjusting Item Order: Manually re-order navigation items or use the extensive sorting options.
- Adding Sections & Links: Create sections and add external links.
- Customizing Titles: Change the title of sections and override page titles. ...

Sections: Awesome Nav for MkDocs, Feature Highlights

</details>

### mypy-boto3-pricing

Type annotations for boto3 Pricing 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-pricing` · installs (wheel) · licence: MIT · rank 6968 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-pricing/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pricing/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Pricing 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-pricing docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcp-server-appwrite

Build and deploy application backends. Add authentication, PostgreSQL/MySQL databases, vector databases, storage, serverless functions, realtime, messaging, hosting, domains, CDN and firewall.

`pip install mcp-server-appwrite` · installs (wheel) · licence: not stated · rank 6971 · last release 2026-11-07 · [PyPI](https://pypi.org/project/mcp-server-appwrite/)

<details><summary>README extract</summary>

<!-- mcp-name: io.github.appwrite/mcp -->

A Model Context Protocol server for Appwrite.
It exposes Appwrite's API — databases, users, functions, teams, storage, and more
— as tools your MCP client can call.

Connect to the hosted server at ` and authenticate
through your browser. ...

Sections: Appwrite MCP server, Connect your client, Reasons and environments, Self-hosted Appwrite, Documentation

</details>

### markdown-pdf

Markdown to pdf renderer

`pip install markdown-pdf` · installs (wheel) · licence: AGPL-3.0-only · rank 7002 · last release 2026-08-26 · [PyPI](https://pypi.org/project/markdown-pdf/)

_README extract left out: share-alike licence._

### matplotlib-label-lines

Label lines in matplotlib.

`pip install matplotlib-label-lines` · installs (wheel) · licence: MIT · rank 7022 · last release 2025-04-25 · [PyPI](https://pypi.org/project/matplotlib-label-lines/)

### microsoft-agents-copilotstudio-client

A client library for Microsoft Agents

`pip install microsoft-agents-copilotstudio-client` · installs (wheel) · licence: MIT · rank 7063 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-copilotstudio-client/)

<details><summary>README extract</summary>

The Copilot Studio Client is for connecting to and interacting with agents created in Microsoft Copilot Studio. This library allows you to integrate Copilot Studio agents into your Python applications.

This client library provides a direct connection to Copilot Studio agents, bypassing traditional chat channels. ...

Example:
```python
def create_client():
    settings = ConnectionSettings(
        environment_id=environ.get("COPILOTSTUDIOAGENT__ENVIRONMENTID"),
        agent_identifier=environ.get("COPILOTSTUDIOAGENT__SCHEMANAME"),
        cloud=None,
        copilot_agent_type=None,
        custom_power_platform_cloud=None,
    )
    token = acquire_token(
        settings,
...
```

...

</details>

### MonkeyType

Generating type annotations from sampled production types

`pip install MonkeyType` · installs (wheel) · licence: BSD License · rank 7071 · last release 2023-03-20 · [PyPI](https://pypi.org/project/MonkeyType/)

<details><summary>README extract</summary>

MonkeyType collects runtime types of function arguments and return values, and
can automatically generate stub files or even add draft type annotations
directly to your Python code based on the types collected at runtime.

Example:
```python
def add(a, b):
    return a + b
```

Sections: MonkeyType, Example, Motivation, Requirements, How MonkeyType works, Troubleshooting, 23.3.0, 22.2.0, 21.5.0, 20.5.0, 20.4.2, 20.4.1, 19.11.2, 19.11.1

</details>

### multi-storage-client

Unified high-performance Python client for object and file stores.

`pip install multi-storage-client` · installs (wheel) · licence: Apache-2.0 · rank 7099 · last release 2026-10-30 · [PyPI](https://pypi.org/project/multi-storage-client/) · [docs](https://nvidia.github.io/multi-storage-client/) · [source](https://github.com/NVIDIA/multi-storage-client)

<details><summary>README extract</summary>

The Multi-Storage Client (MSC) is a unified high-performance Python client for object and file stores such as AWS S3, Azure Blob Storage, Google Cloud Storage (GCS), NVIDIA AIStore, Oracle Cloud Infrastructure (OCI) Object Storage, POSIX file systems, and more. ...

</details>

### meteostat

Access and analyze historical weather and climate data with Python.

`pip install meteostat` · installs (wheel) · licence: not stated · rank 7116 · last release 2026-11-03 · [PyPI](https://pypi.org/project/meteostat/)

<details><summary>README extract</summary>

[][downloads-url]
 [][coverage-url]
 [][provider-tests-url]
 [][issues-url]
 [][license-url]
 [][stars-url]

 Access and analyze historical weather and climate data with Python.

 Explore the docs »

 Visit Website
 Report Bug
 Request Feature

Example:
```python
from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

# Specify location and time range
POINT = ms.Point(50.1155, 8.6842, 113)  # Try with your location
START = date(2018, 1, 1)
END = date(2018, 12, 31)

# Get nearby weather stations
stations = ms.stations.nearby(POINT, limit=4)

# Get daily data & perform interpolation
...
```

Sections: Meteostat Python Package, 🚀 Usage, 🌟 Featured In

</details>

### mypy-boto3-sso

Type annotations for boto3 SSO 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sso` · installs (wheel) · licence: MIT · rank 7117 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-sso/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SSO 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sso docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mpxj

Python wrapper for the MPXJ Java library for manipulating project files

`pip install mpxj` · installs (wheel) · licence: LGPL-2.0-or-later · rank 7121 · last release 2026-10-05 · [PyPI](https://pypi.org/project/mpxj/)

_README extract left out: share-alike licence._

### matplotlib-stubs

Unofficial stubs for the matplotlib package.

`pip install matplotlib-stubs` · installs (wheel) · licence: MIT License · rank 7156 · last release 2025-10-24 · [PyPI](https://pypi.org/project/matplotlib-stubs/)

<details><summary>README extract</summary>

Unofficial python stubs for the matplotlib package.

Official matplotlib stubs now exist (in matplotlib>=3.8), so this repo was archived from 2023/09/19 to 2025/08/02.\
However, the official stubs are still incomplete, so this repo was unarchived.

</details>

### mozsystemmonitor

Monitor system resource usage.

`pip install mozsystemmonitor` · installs (wheel) · licence: MPL 2.0 · rank 7163 · last release 2022-11-14 · [PyPI](https://pypi.org/project/mozsystemmonitor/)

### missingno

Missing data visualization module for Python.

`pip install missingno` · installs (wheel) · licence: MIT License · rank 7264 · last release 2023-02-26 · [PyPI](https://pypi.org/project/missingno/)

### mypy-boto3-ebs

Type annotations for boto3 EBS 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ebs` · installs (wheel) · licence: MIT · rank 7280 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-ebs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 EBS 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ebs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### marin-dupekit-native

Native (Rust) text-deduplication kernels for marin-dupekit.

`pip install marin-dupekit-native` · installs (wheel) · licence: not stated · rank 7318 · last release 2026-10-30 · [PyPI](https://pypi.org/project/marin-dupekit-native/)

### minidump

Python library to parse Windows minidump file format

`pip install minidump` · installs (wheel) · licence: MIT License · rank 7325 · last release 2024-08-15 · [PyPI](https://pypi.org/project/minidump/)

<details><summary>README extract</summary>

Python library to parse Windows minidump file format

</details>

### mypy-boto3-ec2-instance-connect

Type annotations for boto3 EC2InstanceConnect 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ec2-instance-connect` · installs (wheel) · licence: MIT · rank 7388 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-ec2-instance-connect/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 EC2InstanceConnect 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ec2-instance-connect docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mlx-vlm

MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) and Omni Models (VLMs with audio and video support) on your Mac using MLX.

`pip install mlx-vlm` · installs (wheel) · licence: MIT License · rank 7420 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mlx-vlm/) · [source](https://github.com/Neywa-Labs/mlx-vlm)

<details><summary>README extract</summary>

Run and fine-tune multimodal models on Apple Silicon. Text, images, video, and audio in — any out. Built on MLX.

 Installation ·
 Documentation ·
 Releases

 macOS · Apple silicon

 Built by Neywa Labs, the local AI company behind Nativ.

Example:
```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

# Load model with audio support
model_path = "mlx-community/gemma-3n-E2B-it-4bit"
model, processor = load(model_path)
config = model.config

# Prepare audio input
audio = ["/path/to/audio1.wav", "/path/to/audio2.mp3"]
...
```

...

</details>

### mcp-clickhouse

An MCP server for ClickHouse.

`pip install mcp-clickhouse` · installs (wheel) · licence: Apache-2.0 · rank 7450 · last release 2026-09-21 · [PyPI](https://pypi.org/project/mcp-clickhouse/)

<details><summary>README extract</summary>

An MCP server for ClickHouse.

The server implements MCP `2026-07-28` and supports legacy initialize handshakes from
`2024-11-05` through `2025-11-25`. Modern clients use sessionless requests and
`server/discover`. Existing clients can continue to negotiate the legacy protocol. ...

Example:
```python
# my_middleware.py
import logging
from fastmcp.server.middleware import Middleware, MiddlewareContext, CallNext

logger = logging.getLogger("my-middleware")

class LoggingMiddleware(Middleware):
    """Log all tool calls."""

    async def on_call_tool(self, context: MiddlewareContext, call_next: CallNext):
...
```

...

</details>

### mojimoji

A fast converter between Japanese hankaku and zenkaku characters

`pip install mojimoji` · installs from source (sdist only) · licence: Apache Software License · rank 7464 · last release 2024-01-12 · [PyPI](https://pypi.org/project/mojimoji/)

<details><summary>README extract</summary>

A Cython-based fast converter between Japanese hankaku and zenkaku characters.

Example:
```python
>>> import mojimoji
>>> print(mojimoji.zen_to_han('アイウａｂｃ０１２'))
ｱｲｳabc012
>>> print(mojimoji.zen_to_han('アイウａｂｃ０１２', kana=False))
アイウabc012
>>> print(mojimoji.zen_to_han('アイウａｂｃ０１２', digit=False))
ｱｲｳabc０１２
>>> print(mojimoji.zen_to_han('アイウａｂｃ０１２', ascii=False))
ｱｲｳａｂｃ012
```

Sections: mojimoji, Examples, Zenkaku to Hankaku, Hankaku to Zenkaku, Benchmarks, Library versions, Results, Links

</details>

### multiset

An implementation of a multiset.

`pip install multiset` · installs (wheel) · licence: MIT License · rank 7483 · last release 2024-08-27 · [PyPI](https://pypi.org/project/multiset/)

<details><summary>README extract</summary>

This package provides a multiset implementation for python.

Features:
A multiset is similar to the builtin set, but it allows an element to occur multiple times.
It is an unordered collection of elements which have to be hashable just like in a set.
It supports the same methods and operations as set does, e.g. ...

Example:
```python
>>> set1 = Multiset('aab')
>>> set2 = Multiset('abc')
>>> sorted(set1 | set2)
['a', 'a', 'b', 'c']
```

Sections: multiset, Overview, Documentation

</details>

### mistralai-vibe-sdk

Vibe SDK

`pip install mistralai-vibe-sdk` · installs (wheel) · licence: not stated · rank 7535 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mistralai-vibe-sdk/)

<details><summary>README extract</summary>

High-level Python interface for running Vibe agents.

The SDK gives you:

- `Agent` and stateful async/sync sessions
- Pydantic-based tool authoring
- Built-in filesystem tools
- Client-handled tools for UI- or host-dependent actions, such as asking the user a question ...

Example:
```python
from mistralai.vibe.sdk import Agent, AgentConfig
from mistralai.vibe.sdk.providers.completion import MistralCompletionConfig

agent = Agent(
    config=AgentConfig(
        completion=MistralCompletionConfig(model="mistral-large-latest"),
        system_prompt="You are a concise assistant.",
    )
)

async with agent.session() as session:
...
```

Sections: Vibe SDK, Quick Start, Tool annotations, Skills, MCP Servers, Local (stdio) servers, Connector-backed servers, Remote HTTP servers

</details>

### ManimPango

Bindings for Pango for using with Manim.

`pip install ManimPango` · installs from source (sdist only) · licence: MIT · rank 7544 · last release 2026-10-24 · [PyPI](https://pypi.org/project/ManimPango/) · [docs](https://manimpango.manim.community/) · [source](https://github.com/ManimCommunity/manimpango)

<details><summary>README extract</summary>

ManimPango is a C binding for Pango using Cython, which is internally used in Manim to render (non-LaTeX) text.

Sections: ManimPango, BUILDING, Linux/MacOS, Using `tar` archives, MinGW/Msys2, Visual Studio

</details>

### manifestoo-core

A library to reason about Odoo addons manifests

`pip install manifestoo-core` · installs (wheel) · licence: MIT License · rank 7573 · last release 2026-09-18 · [PyPI](https://pypi.org/project/manifestoo-core/) · [docs](https://manifestoo-core.readthedocs.io/en/stable/) · [source](https://github.com/acsone/manifestoo-core)

<details><summary>README extract</summary>

[][github-link]
[][codecov-link]
[][pypi-link]

<!--- shortdesc-begin -->

A library to reason about Odoo addons manifests.

<!--- shortdesc-end -->

Features:
<!--- features-begin -->

`manifestoo_core` provides the following features:

* Detect the Odoo series from an addon version.
* Information about core Odoo CE and EE addons for each Odoo version. ...

Sections: Manifestoo Core, Features

</details>

### mypy-boto3-quicksight

Type annotations for boto3 QuickSight 1.43.125 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-quicksight` · installs (wheel) · licence: MIT · rank 7682 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mypy-boto3-quicksight/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 QuickSight 1.43.125 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-quicksight docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mailchecker

Cross-language temporary email detection library. Stop users from signing up with temporary email addresses.

`pip install mailchecker` · installs (wheel) · licence: MIT License · rank 7688 · last release 2026-07-19 · [PyPI](https://pypi.org/project/mailchecker/)

### mypy-boto3-greengrassv2

Type annotations for boto3 GreengrassV2 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-greengrassv2` · installs (wheel) · licence: MIT · rank 7696 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-greengrassv2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 GreengrassV2 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-greengrassv2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mscerts

Python package for providing Microsoft's CA Bundle.

`pip install mscerts` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7699 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mscerts/) · [source](https://github.com/ralphje/mscerts)

<details><summary>README extract</summary>

This package provides easy access to the Root Certificate Authorities present in
the Microsoft Trusted Root Program. It is a fork of Kenneth Reitz's
certifi project, which provides access
to Mozilla's collection of Root Certificates. ...

Example:
```python
>>> import mscerts

>>> mscerts.where()
'/usr/local/lib/python3.7/site-packages/mscerts/cacert.pem'
```

Sections: mscerts, Usage, Addition/Removal of Certificates

</details>

### mypy-boto3-rekognition

Type annotations for boto3 Rekognition 1.43.103 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-rekognition` · installs (wheel) · licence: MIT · rank 7706 · last release 2026-09-25 · [PyPI](https://pypi.org/project/mypy-boto3-rekognition/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Rekognition 1.43.103 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-rekognition docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-s3files

Type annotations for boto3 S3Files 1.43.116 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-s3files` · installs (wheel) · licence: MIT · rank 7723 · last release 2026-10-20 · [PyPI](https://pypi.org/project/mypy-boto3-s3files/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3files/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 S3Files 1.43.116
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-s3files docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-config

Type annotations for boto3 ConfigService 1.43.42 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-config` · installs (wheel) · licence: MIT · rank 7739 · last release 2026-07-07 · [PyPI](https://pypi.org/project/mypy-boto3-config/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_config/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ConfigService 1.43.42 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-config docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### model-library

Model Library for vals.ai

`pip install model-library` · installs (wheel) · licence: MIT · rank 7740 · last release 2026-11-05 · [PyPI](https://pypi.org/project/model-library/)

<details><summary>README extract</summary>

Open-source model library for interacting with a variety of LLM providers. Originally developed for internal use at vals.ai benchmarks. This tool is designed to be a general-purpose solution for projects that need a unified interface for multiple model providers.

Requires Python 3.11+ and uv. ...

Example:
```python
import asyncio

from model_library import model

async def main():
    llm = model("anthropic/claude-opus-4-6-thinking")

    result = await llm.query(
        "What is QSBS? Explain your thinking in detail and make it concise."
    )

    print(result.output_text)
    print(result.metadata)  # cost, token, and performance telemetry

...
```

...

</details>

### mypy-boto3-translate

Type annotations for boto3 Translate 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-translate` · installs (wheel) · licence: MIT · rank 7751 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-translate/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_translate/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Translate 1.43.110 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-translate docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### msgraph-beta-sdk

The Microsoft Graph Beta Python SDK

`pip install msgraph-beta-sdk` · installs (wheel) · licence: not stated · rank 7758 · last release 2026-11-06 · [PyPI](https://pypi.org/project/msgraph-beta-sdk/) · [docs](https://github.com/microsoftgraph/msgraph-beta-sdk-python/docs) · [source](https://github.com/microsoftgraph/msgraph-beta-sdk-python)

<details><summary>README extract</summary>

Get started with the Microsoft Graph Beta SDK for Python by integrating the Microsoft Graph API into your Python application.

> Note:
> * This SDK allows you to build applications using the latest beta version of Microsoft Graph. If you want to try the v1.0 Microsoft Graph API, use the v1.0 SDK.

Example:
```python
# Example using async credentials.
from azure.identity.aio import EnvironmentCredential
from msgraph_beta import GraphServiceClient

scopes = ['User.Read', 'Mail.Read']
credential = EnvironmentCredential()
client = GraphServiceClient(credential, scopes=scopes)
```

...

</details>

### microsoft-agents-hosting-teams

Integration library for Microsoft Agents with Teams

`pip install microsoft-agents-hosting-teams` · installs (wheel) · licence: MIT · rank 7777 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-hosting-teams/)

<details><summary>README extract</summary>

Integration library for building Microsoft Teams agents using the Microsoft 365 Agents SDK. This library provides specialized handlers and utilities for Teams-specific functionality like messaging extensions, task modules, adaptive cards, and meeting events.

This library extends the core hosting capabilities with Teams-specific features. ...

Features:
✅ Messaging Extensions - Search and action-based extensions
✅ Task Modules - Interactive dialogs and forms
✅ Adaptive Cards - Rich card interactions
✅ Meeting Events - Start, end, participant changes
✅ Team Management - Member operations, channel ...

Sections: Microsoft Agents Hosting - Teams, What is this?, Packages Overview, Key Classes Reference, Migration from Bot Framework, Quick Links, Sample Applications

</details>

### mypy-boto3-apigatewaymanagementapi

Type annotations for boto3 ApiGatewayManagementApi 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-apigatewaymanagementapi` · installs (wheel) · licence: MIT · rank 7784 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ApiGatewayManagementApi 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-apigatewaymanagementapi docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozinfo

Library to get system information for use in Mozilla testing

`pip install mozinfo` · installs (wheel) · licence: MPL · rank 7796 · last release 2023-07-28 · [PyPI](https://pypi.org/project/mozinfo/)

### mypy-boto3-sso-oidc

Type annotations for boto3 SSOOIDC 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-sso-oidc` · installs (wheel) · licence: MIT · rank 7828 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-sso-oidc/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 SSOOIDC 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-sso-oidc docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozdevice

Mozilla-authored device management

`pip install mozdevice` · installs (wheel) · licence: MPL · rank 7875 · last release 2024-11-07 · [PyPI](https://pypi.org/project/mozdevice/)

### multiaddr

Python implementation of jbenet's multiaddr

`pip install multiaddr` · installs (wheel) · licence: MIT License · rank 7882 · last release 2026-03-17 · [PyPI](https://pypi.org/project/multiaddr/)

<details><summary>README extract</summary>

Features:
- Multiaddr Protocol Support: Full support for the multiaddr specification
- DNS Resolution: Async DNS and DNSADDR resolution with trio
- Thin Waist Validation: Network interface discovery and wildcard expansion ...

Example:
```python
from multiaddr import Multiaddr

# construct from a string
m1 = Multiaddr("/ip4/127.0.0.1/udp/1234")

# construct from bytes
# m2 = Multiaddr(bytes_addr=m1.to_bytes()) # deprecated
m2 = Multiaddr(m1.to_bytes())

assert str(m1) == "/ip4/127.0.0.1/udp/1234"
assert str(m1) == str(m2)
assert m1.to_bytes() == m2.to_bytes()
assert m1 == m2
...
```

Sections: py-multiaddr, Requirements, Usage, Simple, En/decapsulate, Tunneling, DNS Resolution, Thin Waist Address Validation, Features

</details>

### massive

Official Massive (formerly Polygon.io) REST and Websocket client.

`pip install massive` · installs (wheel) · licence: MIT License · rank 7931 · last release 2026-10-26 · [PyPI](https://pypi.org/project/massive/) · [docs](https://massive.com/docs) · [source](https://github.com/massive-com/client-python)

### mattermostwrapper

A mattermost api v4 wrapper to interact with api

`pip install mattermostwrapper` · installs from source (sdist only) · licence: MIT · rank 7987 · last release 2020-02-17 · [PyPI](https://pypi.org/project/mattermostwrapper/)

### microsoft-agents-hosting-aiohttp

Integration library for Microsoft Agents with aiohttp

`pip install microsoft-agents-hosting-aiohttp` · installs (wheel) · licence: MIT · rank 8042 · last release 2026-10-19 · [PyPI](https://pypi.org/project/microsoft-agents-hosting-aiohttp/)

<details><summary>README extract</summary>

Integration library for hosting Microsoft 365 Agents using aiohttp. This library provides HTTP adapters, middleware, and utilities for building web-based agent applications with the popular aiohttp framework.

This library bridges the Microsoft 365 Agents SDK with aiohttp, allowing you to create HTTP endpoints that handle agent conversations. ...

Features:
✅ HTTP hosting - Full aiohttp integration for web hosting
✅ JWT authentication - Built-in security with middleware
✅ Agent-to-agent - Support for multi-agent communication
✅ Streaming - Real-time response streaming
✅ Error handling - Comprehensive ...

Example:
```python
agents_sdk_config = load_configuration_from_env(environ)

STORAGE = MemoryStorage()
CONNECTION_MANAGER = MsalConnectionManager(**agents_sdk_config)
...

</details>

### module-level-lint

A Flake8 plugin to checking module level docstrings, future-imports, and dunders as specified in PEP 8

`pip install module-level-lint` · installs (wheel) · licence: MIT License · rank 8054 · last release 2026-02-13 · [PyPI](https://pypi.org/project/module-level-lint/) · [source](https://github.com/hanhwanglim/module-level-lint)

<details><summary>README extract</summary>

A Flake8 plugin to enforce code quality by checking module level docstrings, future-imports, and module level dunders as specified in PEP 8

Example:
```python
import random

# Bad: Module docstring is not at the top of the file
"""This is a docstring"""

def foo():
    pass
```

Sections: Module Level Lint, Usage, Features, Lint, Format, Configuration

</details>

### meshcat

WebGL-based visualizer for 3D geometries and scenes

`pip install meshcat` · installs (wheel) · licence: MIT · rank 8080 · last release 2021-11-07 · [PyPI](https://pypi.org/project/meshcat/)

### mypy-boto3-fms

Type annotations for boto3 FMS 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-fms` · installs (wheel) · licence: MIT · rank 8116 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-fms/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fms/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 FMS 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-fms docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### messagebird

MessageBird's REST API

`pip install messagebird` · installs (wheel) · licence: BSD-2-Clause · rank 8139 · last release 2024-06-21 · [PyPI](https://pypi.org/project/messagebird/)

<details><summary>README extract</summary>

This repository contains the open source Python client for MessageBird's REST API. Documentation can be found at:

Requirements

- Sign up for a free MessageBird account
- Create a new access key in the developers sections
- An application written in Python >3.8

Installation

The easiest way to install the messagebird package is either via pip: ...

Example:
```python
import messagebird
```

</details>

### mypy-boto3-geo-places

Type annotations for boto3 LocationServicePlacesV2 1.43.43 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-geo-places` · installs (wheel) · licence: MIT · rank 8152 · last release 2026-07-08 · [PyPI](https://pypi.org/project/mypy-boto3-geo-places/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 LocationServicePlacesV2 1.43.43
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-geo-places docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mindroom

A universal interface for AI agents with persistent memory, where every conversation has a home

`pip install mindroom` · installs (wheel) · licence: Apache-2.0 · rank 8153 · last release 2026-11-08 · [PyPI](https://pypi.org/project/mindroom/) · [docs](https://github.com/mindroom-ai/mindroom) · [source](https://github.com/mindroom-ai/mindroom)

<details><summary>README extract</summary>

AI agents that know you and your work, in a chat app anyone can use.

Open source under Apache 2.0 · Any model, local or cloud · Self-host the whole stack

Website · Docs · Showcase · MindRoom Chat · Hosted · Quick start ...

Features:
🔌 Connected to your tools and documents

Personal agents and shared team agents connect to 100+ tools, including email, calendar, Slack, Jira, GitHub, and any MCP server, and search your own documents. ...

Sections: MindRoom, See it in action, What people use it for, Personal, Work, Why MindRoom, How it compares to OpenClaw and Hermes, Quick start, Your computer + MindRoom Chat (fastest), macOS app, Full stack with Docker Compose, First steps, How agents respond, Configuration

</details>

### moka-py

A high performance caching library for Python written in Rust

`pip install moka-py` · installs (wheel) · licence: MIT · rank 8157 · last release 2026-08-21 · [PyPI](https://pypi.org/project/moka-py/) · [source](https://github.com/deliro/moka-py)

<details><summary>README extract</summary>

moka-py is a Python binding to the Moka cache written in Rust. It brings Moka’s high-performance, feature‑rich caching to Python.

Features:
- Synchronous cache: Thread-safe in-memory caching for Python.
- TTL: Evicts entries after a configurable time to live (TTL).
- TTI: Evicts entries after a configurable time to idle (TTI). ...

Example:
```python
from time import sleep
from moka_py import Moka

# Create a cache with a capacity of 100 entries, with a TTL of 10.0 seconds
# and a TTI of 0.1 seconds. Entries are always removed after 10 seconds
# and are removed after 0.1 seconds if there are no `get`s happened for this time.

...
```

...

</details>

### mypy-boto3-dlm

Type annotations for boto3 DLM 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-dlm` · installs (wheel) · licence: MIT · rank 8170 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-dlm/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 DLM 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-dlm docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-ds

Type annotations for boto3 DirectoryService 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ds` · installs (wheel) · licence: MIT · rank 8189 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-ds/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 DirectoryService 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ds docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### method-python

Python library for the Method API

`pip install method-python` · installs (wheel) · licence: MIT · rank 8190 · last release 2026-01-17 · [PyPI](https://pypi.org/project/method-python/)

### marshmallow-polyfield

An unofficial extension to Marshmallow to allow for polymorphic fields

`pip install marshmallow-polyfield` · installs from source (sdist only) · licence: Apache Software License · rank 8207 · last release 2022-10-26 · [PyPI](https://pypi.org/project/marshmallow-polyfield/)

<details><summary>README extract</summary>

This branch supports Marshmallow 3.0 and above. For 2.0 support see The 2.0 branch

An unofficial extension to Marshmallow to allow for polymorphic fields.

Marshmallow is a fantastic library for serialization and deserialization of data.
For more on that project see its GitHub page or its Documentation. ...

Example:
```python
def shape_schema_serialization_disambiguation(base_object, parent_obj):
    class_to_schema = {
        Rectangle.name: RectangleSchema,
        Triangle.name: TriangleSchema
    }
    try:
        return class_to_schemabase_object.class.name
    except KeyError:
        pass

    raise TypeError("Could not detect type. "
...
```

Sections: Marshmallow-Polyfield, Importing, Example

</details>

### more-click

Implementations of common CLI patterns on top of Click

`pip install more-click` · installs (wheel) · licence: MIT License · rank 8213 · last release 2025-10-21 · [PyPI](https://pypi.org/project/more-click/) · [docs](https://more_click.readthedocs.io) · [source](https://github.com/cthoyt/more-click.git)

<details><summary>README extract</summary>

Implementations of common CLI patterns on top of Click.

Example:
```python
# cli.py
import click
from more_click import host_option, port_option

@click.command()
@host_option
@port_option
def web(host: str, port: str):
    from .wsgi import app  # modify to point to your module-level `flask.Flask` instance
    app.run(host=host, port=port)

if name == 'main':
    web()
```

Sections: More Click, 💪 Getting Started, Web Tools, 👋 Attribution, 🍪 Cookiecutter, 📖 Building the Documentation, Initial Configuration, Configuring ReadTheDocs, Configuring Archival on Zenodo, Registering with the Python Package Index (PyPI), Configuring your machine's connection to PyPI, Uploading to PyPI, Releasing on GitHub, Updating Package Boilerplate

</details>

### mypy-boto3-comprehendmedical

Type annotations for boto3 ComprehendMedical 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-comprehendmedical` · installs (wheel) · licence: MIT · rank 8223 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-comprehendmedical/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ComprehendMedical 1.43.0 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-comprehendmedical docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### managed-deepagents

Managed Deep Agents — the define_deep_agent authoring interface plus the CLI that compiles and deploys a code-first Deep Agent repository to a managed LangGraph runtime.

`pip install managed-deepagents` · installs (wheel) · licence: MIT License · rank 8240 · last release 2026-11-06 · [PyPI](https://pypi.org/project/managed-deepagents/) · [source](https://github.com/langchain-ai/managed-deepagents-sdk)

<details><summary>README extract</summary>

Example:
```python
from managed_deepagents import define_deep_agent

# The system prompt comes from instructions.md next to this file.
agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-5.5",
    tools=[query_db],
)
```

Sections: Evaluate, Define an Agent, Async subagents, Run context and channels, Self-hosted channel runtime configuration, Setting up channels on deploy, Tool and middleware runtime types, Slack channels, Replying from the agent, Buttons your agent posts, Setting up the Slack app, GitHub channels, Setting up the GitHub App, Linear channels

</details>

### mypy-boto3-kendra

Type annotations for boto3 Kendra 1.43.23 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kendra` · installs (wheel) · licence: MIT · rank 8300 · last release 2026-06-04 · [PyPI](https://pypi.org/project/mypy-boto3-kendra/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Kendra 1.43.23
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kendra docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-grafana

Type annotations for boto3 ManagedGrafana 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-grafana` · installs (wheel) · licence: MIT · rank 8309 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-grafana/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ManagedGrafana 1.43.115 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-grafana docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mkdocs-minify-html-plugin

MkDocs plugin for minification using minify-html, an extremely fast and smart HTML + JS + CSS minifier

`pip install mkdocs-minify-html-plugin` · installs (wheel) · licence: not stated · rank 8313 · last release 2026-10-31 · [PyPI](https://pypi.org/project/mkdocs-minify-html-plugin/) · [source](https://github.com/monosans/mkdocs-minify-html-plugin)

<details><summary>README extract</summary>

MkDocs plugin that minifies the built HTML pages, including inline CSS and JS, with minify-html.

Sections: mkdocs-minify-html-plugin, Usage, Options

</details>

### mypy-boto3-meteringmarketplace

Type annotations for boto3 MarketplaceMetering 1.43.114 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-meteringmarketplace` · installs (wheel) · licence: MIT · rank 8324 · last release 2026-10-14 · [PyPI](https://pypi.org/project/mypy-boto3-meteringmarketplace/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 MarketplaceMetering 1.43.114
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-meteringmarketplace docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-directconnect

Type annotations for boto3 DirectConnect 1.43.95 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-directconnect` · installs (wheel) · licence: MIT · rank 8339 · last release 2026-09-15 · [PyPI](https://pypi.org/project/mypy-boto3-directconnect/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 DirectConnect 1.43.95 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-directconnect docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mitsuba

Mitsuba 3: A Retargetable Forward and Inverse Renderer

`pip install mitsuba` · installs (wheel) · licence: BSD License · rank 8402 · last release 2026-08-07 · [PyPI](https://pypi.org/project/mitsuba/)

<details><summary>README extract</summary>

| Documentation | Tutorial videos | Linux | MacOS | Windows | PyPI |

| [][2]| [][10] | [][4] | [][6] | [][8] | [][12] |

Mitsuba 3 is a research-oriented rendering system for forward and inverse light
transport simulation developed at EPFL in Switzerland. ...

Example:
```python
# Import the library using the alias "mi"
import mitsuba as mi
# Set the variant of the renderer
mi.set_variant('scalar_rgb')
# Load a scene
scene = mi.load_dict(mi.cornell_box())
# Render the scene
img = mi.render(scene)
# Write the rendered image to an EXR file
mi.Bitmap(img).write('cbox.exr')
```

Sections: Mitsuba Renderer 3, Introduction, Main Features, Tutorial videos, documentation, Requirements, Usage, About

</details>

### mypy-boto3-ivs

Type annotations for boto3 IVS 1.43.121 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ivs` · installs (wheel) · licence: MIT · rank 8418 · last release 2026-10-28 · [PyPI](https://pypi.org/project/mypy-boto3-ivs/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 IVS 1.43.121
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ivs docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mobly

Automation framework for special end-to-end test cases

`pip install mobly` · installs (wheel) · licence: Apache2.0 · rank 8433 · last release 2026-08-07 · [PyPI](https://pypi.org/project/mobly/)

### meeteval

(no summary)

`pip install meeteval` · installs from source (sdist only) · licence: MIT License · rank 8513 · last release 2025-09-08 · [PyPI](https://pypi.org/project/meeteval/)

<details><summary>README extract</summary>

Features | Installation | Python Interface | Command Line Interface | Visualization | Cite

Example:
```python
import meeteval
data = meeteval.io.load('example_files/hyp.stm').to_seglst()

for s in data:
  # Add or modify the data in-placee
  s['speaker'] = ...

# Dump in any format
meeteval.io.dump(data, 'hyp.rttm')
```

Sections: MeetEval, A meeting transcription evaluation toolkit, Features, Metrics for meeting transcription evaluation, Error visualization, File format conversion, From PyPI, From source, Command-line interface, File Formats, Segmental Time Mark (STM), Time Marked Conversation (CTM), Python interface

</details>

### mypy-boto3-pinpoint-sms-voice-v2

Type annotations for boto3 PinpointSMSVoiceV2 1.43.112 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-pinpoint-sms-voice-v2` · installs (wheel) · licence: MIT · rank 8520 · last release 2026-10-12 · [PyPI](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice-v2/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 PinpointSMSVoiceV2 1.43.112 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-pinpoint-sms-voice-v2 docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-guardduty

Type annotations for boto3 GuardDuty 1.43.115 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-guardduty` · installs (wheel) · licence: MIT · rank 8521 · last release 2026-10-19 · [PyPI](https://pypi.org/project/mypy-boto3-guardduty/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 GuardDuty 1.43.115 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-guardduty docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-healthlake

Type annotations for boto3 HealthLake 1.43.117 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-healthlake` · installs (wheel) · licence: MIT · rank 8528 · last release 2026-10-21 · [PyPI](https://pypi.org/project/mypy-boto3-healthlake/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 HealthLake 1.43.117 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-healthlake docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### momentchi2

A collection of methods for computing the cdf of a weighted sum of chi-squared random variables.

`pip install momentchi2` · installs (wheel) · licence: MIT License · rank 8542 · last release 2021-08-27 · [PyPI](https://pypi.org/project/momentchi2/)

<details><summary>README extract</summary>

A Python implementation of three approximate methods for computing the
cumulative distribution function of a weighted sum of chi-squared
random variables. All the methods are based on moment-matching techniques. ...

Example:
```python
# Hall-Buckley-Eagleson method
from momentchi2 import hbe

# should give value close to 0.95, actually 0.94908
hbe(coeff=[1.5, 1.5, 0.5, 0.5], x=10.203)

# x is a list, output approx. 0.05, 0.95
hbe([1.5, 1.5, 0.5, 0.5], [0.627, 10.203])

# x is a numpy array - preferred approach for speed
import numpy as np
from momentchi2 import hbe
...
```

...

</details>

### mypy-boto3-securityhub

Type annotations for boto3 SecurityHub 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-securityhub` · installs (wheel) · licence: MIT · rank 8545 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-securityhub/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securityhub/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

Sections: Generate locally (recommended), VSCode extension, From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations

</details>

### mypy-boto3-marketplace-entitlement

Type annotations for boto3 MarketplaceEntitlementService 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-marketplace-entitlement` · installs (wheel) · licence: MIT · rank 8546 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-marketplace-entitlement/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 MarketplaceEntitlementService 1.43.0
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-marketplace-entitlement docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-keyspaces

Type annotations for boto3 Keyspaces 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-keyspaces` · installs (wheel) · licence: MIT · rank 8570 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-keyspaces/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Keyspaces 1.43.110 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-keyspaces docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-ivs-realtime

Type annotations for boto3 Ivsrealtime 1.43.118 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-ivs-realtime` · installs (wheel) · licence: MIT · rank 8594 · last release 2026-10-22 · [PyPI](https://pypi.org/project/mypy-boto3-ivs-realtime/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Ivsrealtime 1.43.118 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-ivs-realtime docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### meltanolabs-target-snowflake

Singer target for Snowflake, built with the Meltano SDK for Singer Targets.

`pip install meltanolabs-target-snowflake` · installs (wheel) · licence: Apache-2.0 · rank 8598 · last release 2026-10-20 · [PyPI](https://pypi.org/project/meltanolabs-target-snowflake/)

<details><summary>README extract</summary>

Target for Snowflake.

Built with the Meltano Singer SDK.

Features:
- `about`
- `stream-maps`
- `schema-flattening`
- `target-schema`

Sections: `target-snowflake`, Capabilities, Settings, Initializing a Snowflake Account, Configure using environment variables, Usage, Executing the Target Directly, Create and Run Tests, SDK Dev Guide

</details>

### mypy-boto3-account

Type annotations for boto3 Account 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-account` · installs (wheel) · licence: MIT · rank 8654 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mypy-boto3-account/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Account 1.43.106
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-account docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-connect

Type annotations for boto3 Connect 1.43.126 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-connect` · installs (wheel) · licence: MIT · rank 8655 · last release 2026-11-06 · [PyPI](https://pypi.org/project/mypy-boto3-connect/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Connect 1.43.126
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-connect docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mkdocs-panzoom-plugin

MkDocs Plugin to enable pan & zoom on images and mermaid diagrams

`pip install mkdocs-panzoom-plugin` · installs (wheel) · licence: MIT License · rank 8659 · last release 2026-10-24 · [PyPI](https://pypi.org/project/mkdocs-panzoom-plugin/)

<details><summary>README extract</summary>

This plugin makes use of the panzoom (LICENCE) library by Andrei Kashcha

> Live Demo

`pip install mkdocs-panzoom-plugin`

Add it to your `mkdocs.yml`:

> [!WARNING]
>As of version 0.4.0 (performance optimizations) the following lines are needed:
>```yaml
>markdown_extensions:
> - pymdownx.superfences:
> custom_fences:
> - name: mermaid
> class: ...

Sections: Panzoom for MkDocs, Setup, Usage, Config, Selectors, Exclude items, Hint, Use different key, Set Initial Zoom Level, Exclude Pages, Enable Fullscreen, Automatic Zoom State Persistence

</details>

### multi-model-server

Multi Model Server is a tool for serving neural net models for inference

`pip install multi-model-server` · installs (wheel) · licence: Apache License Version 2.0 · rank 8673 · last release 2023-06-20 · [PyPI](https://pypi.org/project/multi-model-server/)

<details><summary>README extract</summary>

Multi Model Server (MMS) is a flexible and easy to use tool for
serving deep learning models exported from MXNet
or the Open Neural Network Exchange (ONNX).

Use the MMS Server CLI, or the pre-configured Docker images, to start a
service that sets up HTTP endpoints to handle model inference requests. ...

Sections: Project Description, Prerequisites, Important links, Source code

</details>

### marvin

a simple and powerful tool to get things done with AI

`pip install marvin` · installs (wheel) · licence: not stated · rank 8680 · last release 2026-10-27 · [PyPI](https://pypi.org/project/marvin/)

<details><summary>README extract</summary>

Marvin is a Python library for extracting structured data and running tasks with language models. It builds on Pydantic AI for model access and adds typed tasks, tools, and conversation history. Made by Prefect.

Example:
```python
import marvin
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    email: str

contacts = marvin.extract("Email Ada at ada@example.com", Contact)
print(contacts)
```

Sections: Marvin, Use, Docs

</details>

### mypy-boto3-servicecatalog

Type annotations for boto3 ServiceCatalog 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-servicecatalog` · installs (wheel) · licence: MIT · rank 8696 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-servicecatalog/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 ServiceCatalog 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-servicecatalog docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-workspaces

Type annotations for boto3 WorkSpaces 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-workspaces` · installs (wheel) · licence: MIT · rank 8702 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-workspaces/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 WorkSpaces 1.43.124 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-workspaces docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozdebug

Utilities for running applications under native code debuggers intended for use in Mozilla testing

`pip install mozdebug` · installs (wheel) · licence: MPL · rank 8717 · last release 2026-01-19 · [PyPI](https://pypi.org/project/mozdebug/)

### mypy-boto3-location

Type annotations for boto3 LocationService 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-location` · installs (wheel) · licence: MIT · rank 8718 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-location/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 LocationService 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-location docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-mediaconnect

Type annotations for boto3 MediaConnect 1.43.119 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-mediaconnect` · installs (wheel) · licence: MIT · rank 8776 · last release 2026-10-26 · [PyPI](https://pypi.org/project/mypy-boto3-mediaconnect/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 MediaConnect 1.43.119 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-mediaconnect docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mcp-proxy-for-aws-cli

MCP Proxy for AWS (version-pinned CLI distribution)

`pip install mcp-proxy-for-aws-cli` · installs (wheel) · licence: Apache Software License · rank 8778 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mcp-proxy-for-aws-cli/) · [docs](https://github.com/aws/mcp-proxy-for-aws/blob/main/README.md) · [source](https://github.com/aws/mcp-proxy-for-aws.git)

<details><summary>README extract</summary>

`mcp-proxy-for-aws-cli` is the distribution to install for CLI and `uvx` use. It contains no
code of its own: it is a thin wrapper that depends on
`mcp-proxy-for-aws` — which owns the
implementation — and pins that library plus its entire runtime dependency tree to exact
versions. ...

Sections: MCP Proxy for AWS (version-pinned distribution), Documentation

</details>

### mypy-boto3-fsx

Type annotations for boto3 FSx 1.43.104 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-fsx` · installs (wheel) · licence: MIT · rank 8811 · last release 2026-09-28 · [PyPI](https://pypi.org/project/mypy-boto3-fsx/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fsx/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 FSx 1.43.104
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-fsx docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-polly

Type annotations for boto3 Polly 1.43.124 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-polly` · installs (wheel) · licence: MIT · rank 8814 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mypy-boto3-polly/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_polly/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Polly 1.43.124
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-polly docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mozshellutil

Shell command line parsing utilities for Mozilla testing

`pip install mozshellutil` · installs (wheel) · licence: MPL · rank 8837 · last release 2026-01-19 · [PyPI](https://pypi.org/project/mozshellutil/)

### mypy-boto3-imagebuilder

Type annotations for boto3 Imagebuilder 1.43.122 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-imagebuilder` · installs (wheel) · licence: MIT · rank 8843 · last release 2026-10-29 · [PyPI](https://pypi.org/project/mypy-boto3-imagebuilder/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 Imagebuilder 1.43.122 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-imagebuilder docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-kinesisvideo

Type annotations for boto3 KinesisVideo 1.43.0 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-kinesisvideo` · installs (wheel) · licence: MIT · rank 8846 · last release 2026-04-29 · [PyPI](https://pypi.org/project/mypy-boto3-kinesisvideo/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 KinesisVideo 1.43.0 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-kinesisvideo docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### model-archiver

Model Archiver is used for creating archives of trained neural net models that can be consumed by MXNet-Model-Server inference

`pip install model-archiver` · installs (wheel) · licence: Apache License Version 2.0 · rank 8852 · last release 2019-05-16 · [PyPI](https://pypi.org/project/model-archiver/)

<details><summary>README extract</summary>

Model Archiver is a tool used for creating archives of trained neural
net models that can be consumed by MXNet-Model-Server inference.

Use the Model Archiver CLI to start create a `.mar` file.

Model Archiver is part of MMS.
However,you ca install Model Archiver stand alone.

Detailed documentation and examples are provided in the README. ...

Sections: Project Description, Prerequisites, Important links, Source code

</details>

### mypy-boto3-support

Type annotations for boto3 Support 1.43.84 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-support` · installs (wheel) · licence: MIT · rank 8856 · last release 2026-08-31 · [PyPI](https://pypi.org/project/mypy-boto3-support/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

Sections: Generate locally (recommended), VSCode extension, From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations

</details>

### mypy-boto3-globalaccelerator

Type annotations for boto3 GlobalAccelerator 1.43.106 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-globalaccelerator` · installs (wheel) · licence: MIT · rank 8871 · last release 2026-09-30 · [PyPI](https://pypi.org/project/mypy-boto3-globalaccelerator/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 GlobalAccelerator 1.43.106 compatible
with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-globalaccelerator docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-license-manager

Type annotations for boto3 LicenseManager 1.43.120 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-license-manager` · installs (wheel) · licence: MIT · rank 8877 · last release 2026-10-27 · [PyPI](https://pypi.org/project/mypy-boto3-license-manager/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

Sections: Generate locally (recommended), VSCode extension, From PyPI with pip, Usage, VSCode, PyCharm, Emacs, Sublime Text, Other IDEs, mypy, pyright, Pylint compatibility, Explicit type annotations, Client annotations

</details>

### mypy-boto3-accessanalyzer

Type annotations for boto3 AccessAnalyzer 1.43.10 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-accessanalyzer` · installs (wheel) · licence: MIT · rank 8882 · last release 2026-05-18 · [PyPI](https://pypi.org/project/mypy-boto3-accessanalyzer/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 AccessAnalyzer 1.43.10 compatible with
VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-accessanalyzer docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-geo-routes

Type annotations for boto3 LocationServiceRoutesV2 1.43.21 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-geo-routes` · installs (wheel) · licence: MIT · rank 8888 · last release 2026-06-03 · [PyPI](https://pypi.org/project/mypy-boto3-geo-routes/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_routes/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for
boto3 LocationServiceRoutesV2 1.43.21
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-geo-routes docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-budgets

Type annotations for boto3 Budgets 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-budgets` · installs (wheel) · licence: MIT · rank 8892 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-budgets/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_budgets/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Budgets 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-budgets docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### mypy-boto3-health

Type annotations for boto3 Health 1.43.110 service generated with mypy-boto3-builder 8.12.0

`pip install mypy-boto3-health` · installs (wheel) · licence: MIT · rank 8894 · last release 2026-10-08 · [PyPI](https://pypi.org/project/mypy-boto3-health/) · [docs](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/) · [source](https://github.com/youtype/mypy_boto3_builder)

<details><summary>README extract</summary>

Type annotations for boto3 Health 1.43.110
compatible with VSCode,
PyCharm,
Emacs,
Sublime Text,
mypy,
pyright and other tools.

Generated with
mypy-boto3-builder 8.12.0.

More information can be found on
boto3-stubs page and in
mypy-boto3-health docs.

See how it helps you find and fix potential bugs: ...

Example:
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import EC2Client, EC2ServiceResource
    from mypy_boto3_ec2.waiters import BundleTaskCompleteWaiter
    from mypy_boto3_ec2.paginators import DescribeVolumesPaginator
else:
    EC2Client = object
    EC2ServiceResource = object
    BundleTaskCompleteWaiter = object
...
```

...

</details>

### microdf-python

Weighted pandas DataFrames and Series for survey microdata

`pip install microdf-python` · installs (wheel) · licence: MIT · rank 8897 · last release 2026-10-12 · [PyPI](https://pypi.org/project/microdf-python/)

<details><summary>README extract</summary>

Weighted pandas DataFrames and Series for survey microdata analysis.

Features:
Survey microdata comes with weights, and analysing it in pandas means getting two
things right that pandas will not do for you.

The estimators are not the obvious ones. A weighted median is not the median of
weighted values. ...

Example:
```python
import microdf as mdf
import pandas as pd

# Create sample data with weights
df = pd.DataFrame(
    {"income": [10_000, 20_000, 30_000, 40_000, 50_000], "weights": [1, 2, 3, 2, 1]}
)

# Create a MicroDataFrame
mdf_df = mdf.MicroDataFrame(df, weights="weights")

# All operations are weight-aware
print(mdf_df.income.mean())  # Weighted mean
...
```

Sections: microdf, Why this exists, Key Features, Usage, Questions

</details>

