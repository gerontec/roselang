# Unclassified / L

[Index](README.md) · 296 packages in this topic, by downloads.

### litellm

Library to easily interface with LLM API providers

`pip install litellm` · installs (wheel) · licence: MIT · rank 295 · last release 2026-11-07 · [PyPI](https://pypi.org/project/litellm/) · [docs](https://docs.litellm.ai) · [source](https://github.com/BerriAI/litellm)

<details><summary>README extract</summary>

LiteLLM AI Gateway

 Open Source AI Gateway for 100+ LLMs. Self-hosted. Enterprise-ready. Call any LLM in OpenAI format.

LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — OpenAI, Anthropic, Gemini, Bedrock, Azure, and more — using the OpenAI format. ...

Features:
Managing LLM calls across providers gets complicated fast — different SDKs, auth patterns, request formats, and error types for every model. LiteLLM removes that friction: ...

Example:
```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic
...
```

...

</details>

### lz4

LZ4 Bindings for Python

`pip install lz4` · installs (wheel) · licence: BSD License · rank 319 · last release 2025-11-03 · [PyPI](https://pypi.org/project/lz4/)

<details><summary>README extract</summary>

Sections: python-lz4, Introduction, Documentation, Homepage, Licensing

</details>

### langgraph

Building stateful, multi-actor applications with LLMs

`pip install langgraph` · installs (wheel) · licence: MIT · rank 426 · last release 2026-11-05 · [PyPI](https://pypi.org/project/langgraph/) · [docs](https://reference.langchain.com/python/langgraph/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/langgraph)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangGraph.js.

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Sections: 🦜🕸️ LangGraph, 🤔 What is this?, 📖 Documentation

</details>

### langgraph-sdk

SDK for interacting with LangGraph API

`pip install langgraph-sdk` · installs (wheel) · licence: MIT · rank 436 · last release 2026-11-06 · [PyPI](https://pypi.org/project/langgraph-sdk/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/sdk-py)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from langgraph_sdk import get_client

# If you're using a remote server, initialize the client with `get_client(url=REMOTE_URL)`
client = get_client()

# List all assistants
assistants = await client.assistants.search()

# We auto-create an assistant for each graph you register in config.
agent = assistants[0]

# Start a new thread
...
```

Sections: LangGraph Python SDK, 🤔 What is this?, 📖 Documentation, Quick Start, Known Limitations, Thread-Centric Streaming (v3)

</details>

### langgraph-checkpoint

Library with base interfaces for LangGraph checkpoint savers.

`pip install langgraph-checkpoint` · installs (wheel) · licence: MIT · rank 441 · last release 2026-10-26 · [PyPI](https://pypi.org/project/langgraph-checkpoint/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from langgraph.checkpoint.memory import InMemorySaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

checkpointer = InMemorySaver()
checkpoint = {
    "v": 4,
    "ts": "2024-07-31T20:14:19.804150+00:00",
    "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...
```

Sections: LangGraph Checkpoint, 🤔 What is this?, 📖 Documentation, Key concepts, Checkpoint, Thread, Serde, Pending writes, Interface, Usage

</details>

### langgraph-prebuilt

Library with high-level APIs for creating and executing LangGraph agents and tools.

`pip install langgraph-prebuilt` · installs (wheel) · licence: MIT · rank 448 · last release 2026-10-15 · [PyPI](https://pypi.org/project/langgraph-prebuilt/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/prebuilt)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

# Define the tools for the agent to use
def search(query: str):
    """Call to surf the web."""
    # This is a placeholder, but don't tell the LLM that...
    if "sf" in query.lower() or "san francisco" in query.lower():
...
```

Sections: LangGraph Prebuilt, 🤔 What is this?, 📖 Documentation, Agents, Tools, ToolNode, ValidationNode, Agent Inbox

</details>

### langchain-google-vertexai

An integration package connecting Google VertexAI and LangChain

`pip install langchain-google-vertexai` · installs (wheel) · licence: MIT · rank 610 · last release 2026-10-23 · [PyPI](https://pypi.org/project/langchain-google-vertexai/) · [docs](https://reference.langchain.com/python/integrations/langchain_google_vertexai/) · [source](https://github.com/langchain-ai/langchain-google/tree/master/libs/vertexai)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

This package contains the LangChain integrations for Google Cloud generative models via the Vertex AI Platform.

Sections: langchain-google-vertexai, 📖 Documentation

</details>

### lazy-loader

Makes it easy to load subpackages and functions on demand.

`pip install lazy-loader` · installs (wheel) · licence: BSD-3-Clause · rank 616 · last release 2026-09-21 · [PyPI](https://pypi.org/project/lazy-loader/) · [source](https://github.com/scientific-python/lazy-loader)

<details><summary>README extract</summary>

`lazy-loader` makes it easy to load subpackages and functions on demand.

1. Allow subpackages to be made visible to users without incurring import costs.
2. Allow external libraries to be imported only when used, improving import times.

For a more detailed discussion, see the SPEC.

Example:
```python
subpackages = [
    ...,
    'filters',
    ...
]

import lazy_loader as lazy
getattr, dir, _ = lazy.attach(name, subpackages)
```

Sections: Motivation, Usage, Lazily load subpackages, Lazily load subpackages and functions, Type checkers, Early failure, External libraries, Optional requirements

</details>

### logfire-api

Shim for the Logfire SDK which does nothing unless Logfire is installed

`pip install logfire-api` · installs (wheel) · licence: MIT · rank 626 · last release 2026-11-07 · [PyPI](https://pypi.org/project/logfire-api/)

<details><summary>README extract</summary>

Shim for the logfire SDK Python API which does nothing unless logfire is installed.

This package is designed to be used by packages that want to provide opt-in integration with Logfire. ...

</details>

### langfuse

Langfuse Python SDK - LLM observability/tracing, datasets, experiments, LLM-as-a-judge evaluation, and prompt management

`pip install langfuse` · installs (wheel) · licence: MIT · rank 655 · last release 2026-11-05 · [PyPI](https://pypi.org/project/langfuse/) · [docs](https://langfuse.com/docs/observability/sdk/overview) · [source](https://github.com/langfuse/langfuse-python)

<details><summary>README extract</summary>

> [!IMPORTANT]
> The SDK was rewritten in v4 and released in March 2026. Refer to the v4 migration guide for instructions on updating your code.
> This is the latest Langfuse Python SDK (v4, OpenTelemetry). The legacy v2 client API (`trace()`, `span()`, `generation()`, `api.trace.list`) is deprecated. Do not use it for new instrumentation. ...

Example:
```python
# env: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_BASE_URL

from langfuse import get_client

langfuse = get_client()

# Create a span using a context manager
with langfuse.start_as_current_observation(as_type="span", name="process-request") as span:
    # Your processing logic here
    span.update(output="Processing complete")

...
```

Sections: Langfuse Python SDK, Quickstart, Docs

</details>

### langchain-community

Community contributed LangChain integrations.

`pip install langchain-community` · installs (wheel) · licence: MIT · rank 665 · last release 2026-05-22 · [PyPI](https://pypi.org/project/langchain-community/) · [docs](https://reference.langchain.com/python/langchain_community/) · [source](https://github.com/langchain-ai/langchain-community/tree/main/libs/community)

### locket

File-based locks for Python on Linux and Windows

`pip install locket` · installs (wheel) · licence: BSD License · rank 667 · last release 2022-04-20 · [PyPI](https://pypi.org/project/locket/)

<details><summary>README extract</summary>

Locket implements a file-based lock that can be used by multiple processes provided they use the same path.

Locks largely behave as (non-reentrant) `Lock` instances from the `threading`
module in the standard library. Specifically, their behaviour is: ...

Example:
```python
import locket

# Wait for lock
with locket.lock_file("path/to/lock/file"):
    perform_action()

# Raise LockError if lock cannot be acquired immediately
with locket.lock_file("path/to/lock/file", timeout=0):
    perform_action()

# Raise LockError if lock cannot be acquired after thirty seconds
...
```

</details>

### lxml-html-clean

HTML cleaner from lxml project

`pip install lxml-html-clean` · installs (wheel) · licence: BSD-3-Clause · rank 820 · last release 2026-10-26 · [PyPI](https://pypi.org/project/lxml-html-clean/) · [docs](https://lxml-html-clean.readthedocs.io/)

<details><summary>README extract</summary>

This project was initially a part of lxml. Because HTML cleaner is designed as blocklist-based, many reports about possible security vulnerabilities were filed for lxml and that make the project problematic for security-sensitive environments. Therefore we decided to extract the problematic part to a separate project. ...

Sections: lxml_html_clean, Motivation, Documentation

</details>

### langchain-google-genai

An integration package connecting Google's genai package and LangChain

`pip install langchain-google-genai` · installs (wheel) · licence: MIT · rank 926 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain-google-genai/) · [docs](https://reference.langchain.com/python/integrations/langchain_google_genai/) · [source](https://github.com/langchain-ai/langchain-google/tree/master/libs/genai)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

This package provides access to Google Gemini's chat, vision, embeddings, and other capabilities within the LangChain ecosystem.

Sections: langchain-google-genai, 📖 Documentation

</details>

### Levenshtein

Python extension for computing string edit distances and similarities.

`pip install Levenshtein` · installs (wheel) · licence: GPL-2.0-or-later · rank 949 · last release 2026-09-12 · [PyPI](https://pypi.org/project/Levenshtein/) · [docs](https://rapidfuzz.github.io/Levenshtein/) · [source](https://github.com/rapidfuzz/Levenshtein.git)

_README extract left out: share-alike licence._

### langcodes

Tools for labeling human languages with IETF language tags

`pip install langcodes` · installs (wheel) · licence: MIT License · rank 992 · last release 2025-12-02 · [PyPI](https://pypi.org/project/langcodes/) · [source](https://github.com/georgkrause/langcodes)

<details><summary>README extract</summary>

langcodes knows what languages are. It knows the standardized codes that
refer to them, such as `en` for English, `es` for Spanish and `hi` for Hindi.

These are IETF language tags. You may know them by their old name, ISO 639
language codes. ...

Sections: Langcodes: a library for language codes, Standards implemented, Documentation, Standardizing language tags, Language objects, Checking validity, Getting alpha3 codes, Working with language names, Describing Language objects in natural language, Describing components of language codes, Recognizing language names in natural language, Ambiguity, Demographic language data, Comparing and matching languages

</details>

### langchain-google-community

An integration package connecting miscellaneous Google's products and LangChain

`pip install langchain-google-community` · installs (wheel) · licence: MIT · rank 1099 · last release 2026-10-05 · [PyPI](https://pypi.org/project/langchain-google-community/) · [docs](https://reference.langchain.com/python/integrations/langchain_google_community/) · [source](https://github.com/langchain-ai/langchain-google/tree/master/libs/community)

### langdetect

Language detection library ported from Google's language-detection.

`pip install langdetect` · installs from source (sdist only) · licence: Apache Software License · rank 1131 · last release 2021-05-07 · [PyPI](https://pypi.org/project/langdetect/)

<details><summary>README extract</summary>

Port of Nakatani Shuyo's language-detection library (version from 03/03/2014) to Python.

Example:
```python
>>> from langdetect import detect
>>> detect("War doesn't show who's right, just who's left.")
'en'
>>> detect("Ein, zwei, drei, vier")
'de'
```

Sections: langdetect, Languages, Basic usage, How to add new language?, Original project

</details>

### langgraph-checkpoint-postgres

Library with a Postgres implementation of LangGraph checkpoint saver.

`pip install langgraph-checkpoint-postgres` · installs (wheel) · licence: MIT · rank 1139 · last release 2026-10-14 · [PyPI](https://pypi.org/project/langgraph-checkpoint-postgres/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from langgraph.checkpoint.postgres import PostgresSaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable"
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
...
```

Sections: LangGraph Checkpoint Postgres, 🤔 What is this?, 📖 Documentation, Usage, Async

</details>

### lightning-utilities

Lightning toolbox for across the our ecosystem.

`pip install lightning-utilities` · installs (wheel) · licence: Apache-2.0 · rank 1157 · last release 2026-02-22 · [PyPI](https://pypi.org/project/lightning-utilities/) · [docs](https://dev-toolbox.rtfd.io/en/latest/) · [source](https://github.com/Lightning-AI/utilities)

<details><summary>README extract</summary>

This repository covers the following use-cases:

1. _Reusable GitHub workflows
2. _Shared GitHub actions
3. _General Python utilities in `lightning_utilities.core`_
4. _CLI `python -m lightning_utilities.cli --help`_

Usage:

See usage of other workflows in .github/workflows/ci-use-checks.yaml.

Example:
```python
from lightning_utilities.core.imports import module_available

if module_available("some_package.something"):
    from some_package import something
```

Sections: Lightning Utilities, 1. Reusable workflows, 2. Reusable composite actions, 3. General Python utilities `lightning_utilities.core`, 4. CLI `lightning_utilities.cli`

</details>

### langchain-aws

An integration package connecting AWS and LangChain

`pip install langchain-aws` · installs (wheel) · licence: MIT · rank 1273 · last release 2026-11-06 · [PyPI](https://pypi.org/project/langchain-aws/) · [source](https://github.com/langchain-ai/langchain-aws)

<details><summary>README extract</summary>

This package contains the LangChain integrations with AWS.

Sections: langchain-aws, 📖 Documentation

</details>

### looker-sdk

Looker REST API

`pip install looker-sdk` · installs (wheel) · licence: MIT · rank 1401 · last release 2026-10-26 · [PyPI](https://pypi.org/project/looker-sdk/)

<details><summary>README extract</summary>

The Looker SDK for Python provides a convenient way to communicate with the
Looker API available on your Looker server. The library requires python3.6+
and is annotated using the typing module. ...

Example:
```python
import looker_sdk

# For this to work you must either have set environment variables or created a looker.ini as described below in "Configuring the SDK"
sdk = looker_sdk.init40()  # or init31() for the older v3.1 API
my_user = sdk.me()

# output can be treated like a dictionary
print(my_user["first_name"])
# or a model instance (User in this case)
...
```

Sections: Looker SDK, Basic Usage, Full tutorial, Sample project setup, Configuring the SDK, Code example

</details>

### livekit-protocol

Python protocol stubs for LiveKit

`pip install livekit-protocol` · installs (wheel) · licence: Apache-2.0 · rank 1447 · last release 2026-11-05 · [PyPI](https://pypi.org/project/livekit-protocol/) · [docs](https://docs.livekit.io) · [source](https://github.com/livekit/python-sdks/)

### lance-namespace-urllib3-client

Lance Namespace Specification

`pip install lance-namespace-urllib3-client` · installs (wheel) · licence: Apache-2.0 · rank 1489 · last release 2026-09-14 · [PyPI](https://pypi.org/project/lance-namespace-urllib3-client/) · [source](https://github.com/lance-format/lance-namespace)

<details><summary>README extract</summary>

This OpenAPI specification is a part of the Lance namespace specification. It contains 2 parts:

The `components/schemas`, `components/responses`, `components/examples`, `tags` sections define
the request and response shape for each operation in a Lance Namespace across all implementations.
See for more details. ...

Example:
```python
import lance_namespace_urllib3_client
from lance_namespace_urllib3_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = lance_namespace_urllib3_client.Configuration(
    host = "
)

...
```

...

</details>

### lance-namespace

Lance Namespace interface and plugin registry

`pip install lance-namespace` · installs (wheel) · licence: Apache-2.0 · rank 1492 · last release 2026-09-14 · [PyPI](https://pypi.org/project/lance-namespace/) · [docs](https://lance.org/format/namespace/) · [source](https://github.com/lance-format/lance-namespace)

<details><summary>README extract</summary>

Lance Namespace interface and plugin registry.

Features:
This package provides:
- `LanceNamespace` ABC interface for namespace implementations
- `connect()` factory function for creating namespace instances
- `register_namespace_impl()` for external implementation registration ...

Example:
```python
import lance_namespace

# Connect using native implementations (requires lance package)
ns = lance_namespace.connect("dir", {"root": "/path/to/data"})
ns = lance_namespace.connect("rest", {"uri": "

# Register a custom implementation
lance_namespace.register_namespace_impl("glue", "lance_glue.GlueNamespace")
...
```

Sections: lance-namespace, Overview, Usage, Creating Custom Implementations

</details>

### langchain-mcp-adapters

Make Anthropic Model Context Protocol (MCP) tools compatible with LangChain and LangGraph agents.

`pip install langchain-mcp-adapters` · installs (wheel) · licence: MIT · rank 1532 · last release 2026-08-06 · [PyPI](https://pypi.org/project/langchain-mcp-adapters/) · [source](https://www.github.com/langchain-ai/langchain-mcp-adapters)

<details><summary>README extract</summary>

This library provides a lightweight wrapper that makes Anthropic Model Context Protocol (MCP) tools compatible with LangChain and LangGraph.

> [!note]
> A JavaScript/TypeScript version of this library is also available at langchainjs.

Features:
- 🛠️ Convert MCP tools into LangChain tools that can be used with LangGraph agents
- 📦 A client implementation that allows you to connect to multiple MCP servers and load tools from them

Example:
```python
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "http",
            "url": "
            "headers": {
                "Authorization": "Bearer YOUR_TOKEN",
...

</details>

### litellm-proxy-extras

Additional files for the LiteLLM Proxy. Reduces the size of the main litellm package.

`pip install litellm-proxy-extras` · installs (wheel) · licence: MIT · rank 1555 · last release 2026-11-07 · [PyPI](https://pypi.org/project/litellm-proxy-extras/) · [docs](https://docs.litellm.ai) · [source](https://github.com/BerriAI/litellm)

<details><summary>README extract</summary>

Additional files for the proxy. Reduces the size of the main litellm package.

Currently, only stores the migration.sql files for litellm-proxy.

To install, run:


To use the migrations, run:

</details>

### litellm-enterprise

Package for LiteLLM Enterprise features

`pip install litellm-enterprise` · installs (wheel) · licence: LicenseRef-Proprietary · rank 1562 · last release 2026-11-07 · [PyPI](https://pypi.org/project/litellm-enterprise/) · [docs](https://docs.litellm.ai) · [source](https://github.com/BerriAI/litellm)

<details><summary>README extract</summary>

Code in this folder is licensed under a commercial license. Please review the LICENSE file within the /enterprise folder

These features are covered under the LiteLLM Enterprise contract

👉 Using in an Enterprise / Need specific features ? Meet with us here

See all Enterprise Features here 👉 Docs

</details>

### lxml-stubs

Type annotations for the lxml package

`pip install lxml-stubs` · installs (wheel) · licence: Apache Software License · rank 1666 · last release 2024-01-10 · [PyPI](https://pypi.org/project/lxml-stubs/)

<details><summary>README extract</summary>

This repository contains external type annotations (see
PEP 484) for the
lxml package.

Sections: lxml-stubs, About

</details>

### latex2sympy2-extended

Convert LaTeX math to SymPy expressions

`pip install latex2sympy2-extended` · installs (wheel) · licence: MIT · rank 1699 · last release 2026-01-10 · [PyPI](https://pypi.org/project/latex2sympy2-extended/) · [source](https://github.com/OrangeX4/latex2sympy2.git)

<details><summary>README extract</summary>

`latex2sympy2_extended` parses LaTeX math expressions and converts it into the equivalent SymPy form. The latex2sympy2_extended is adapted from OrangeX4/latex2sympy.

ANTLR 4.13.1 is used to generate the parser.

Features:
* Arithmetic: Add (+), Sub (-), Dot Mul (·), Cross Mul (×), Frac (/), Power (^), Abs (|x|), Sqrt (√), etc...
* Alphabet: a - z, A - Z, α - ω, Subscript (x_1), Accent Bar(ā), etc... ...

Example:
```python
from latex2sympy2_extended import latex2sympy

tex = r"\frac{d}{dx}(x^{2}+x)"
latex2sympy(tex)
# => "Derivative(x**2 + x, x)"
```

Sections: latex2sympy2_extended, About, Features, Usage, Basic, Examples, Eval At, Matrix, Determinant, Transpose, Elementary Transformation

</details>

### logistro

Simple wrapper over logging for a couple basic features

`pip install logistro` · installs (wheel) · licence: not stated · rank 1798 · last release 2025-11-01 · [PyPI](https://pypi.org/project/logistro/) · [source](https://github.com/geopozo/logistro)

<details><summary>README extract</summary>

`logistro` is an extremely light addition to `logging`, providing sensible defaults.

It also includes `getPipeLogger()` which can be passed to `Popen()` so that its
`stderr` is piped to the already thread-safe `logging` library.

`debug2` I use if I'm in a situation where it's okay to dump large amounts of
information. I'm planning on scrolling. ...

Example:
```python
import logistro

logger = logistro.getLogger(name)

logger.debug2(...) # new!
logger.debug(...) # or debug1()
logger.info(...)
logger.warning(...)
logger.error(...)
logger.critical(...)
logger.exception(...) # always inside except:

# For subprocesses:

pipe, logger = logistro.getPipeLogger(name+"-subprocess")
...
```

...

</details>

### llama-index-workflows

An event-driven, async-first, step-based way to control the execution flow of AI applications like Agents.

`pip install llama-index-workflows` · installs (wheel) · licence: MIT · rank 1841 · last release 2026-10-21 · [PyPI](https://pypi.org/project/llama-index-workflows/)

<details><summary>README extract</summary>

LlamaIndex Workflows are a framework for orchestrating and chaining together complex systems of steps and events.

Workflows shine when you need to orchestrate complex, multi-step processes that involve AI models, APIs, and decision-making. Here are some examples of what you can build: ...

Features:
- async-first - workflows are built around python's async functionality - steps are async functions that process incoming events from an asyncio queue and emit new events to other queues. ...

Example:
```python
import asyncio
from pydantic import BaseModel, Field
from workflows import Context, Workflow, step
from workflows.events import Event, StartEvent, StopEvent

class MyEvent(Event):
    msg: list[str]

class RunState(BaseModel):
    num_runs: int = Field(default=0)

...

</details>

### llguidance

Bindings for the Low-level Guidance (llguidance) Rust library for use within Guidance

`pip install llguidance` · installs (wheel) · licence: MIT · rank 1868 · last release 2026-09-30 · [PyPI](https://pypi.org/project/llguidance/) · [source](https://github.com/microsoft/llguidance)

<details><summary>README extract</summary>

Performance results from MaskBench

* 2025-06-23 llguidance is now deemed v1.0.0
* 2025-06-11 Making Structured Outputs Go Brrr blog post released
* 2025-05-20 LLGuidance shipped in OpenAI for JSON Schema
* 2025-04-11 integration merged into Chromium
* 2025-03-25 integration merged into vLLM (v0.8.2)
* 2025-02-26 integration merged into SGLang ...

Sections: Low-level Guidance (llguidance), About, Integrations, Technical details, Comparison and performance, Building, Trademarks

</details>

### lmnr

Python SDK for Laminar

`pip install lmnr` · installs (wheel) · licence: Apache-2.0 · rank 1871 · last release 2026-11-05 · [PyPI](https://pypi.org/project/lmnr/)

<details><summary>README extract</summary>

Python SDK for Laminar.

Laminar is an open-source platform for engineering LLM products. Trace, evaluate, annotate, and analyze LLM data. Bring LLM applications to production with confidence.

Check our open-source repo and don't forget to star it ⭐

Features:
Bring rigor to the development of your LLM applications with evaluations.

You can run evaluations locally by providing executor (part of the logic used in your application) and evaluators (numeric scoring functions) to `evaluate` function. ...

Example:
```python
from lmnr import Laminar

Laminar.initialize(project_api_key="")
```

Sections: Laminar Python, Quickstart, Set-up for self-hosting, Instrumentation, Manual instrumentation, Automatic instrumentation, Evaluations, Overview, Client for HTTP operations

</details>

### llama-index-instrumentation

Instrumentation and Observability for LlamaIndex

`pip install llama-index-instrumentation` · installs (wheel) · licence: MIT · rank 1874 · last release 2026-08-29 · [PyPI](https://pypi.org/project/llama-index-instrumentation/) · [docs](https://developers.llamaindex.ai/python/framework/module_guides/observability/instrumentation/) · [source](https://github.com/run-llama/llama_index/tree/main/llama-index-instrumentation)

<details><summary>README extract</summary>

This project provides the instrumentation hooks for observability in LlamaIndex.

Instrumentation uses a mix of

- spans
- events
- dispatchers that manage span and event handlers

For more in-depth usage, you can see an example in the workflows repo.

For other documentation, you can see the LlamaIndex documentation.

</details>

### lmnr-claude-code-proxy

Thin proxy server for Claude Code and Laminar tracing

`pip install lmnr-claude-code-proxy` · installs (wheel) · licence: LicenseRef-Proprietary · rank 1901 · last release 2026-10-23 · [PyPI](https://pypi.org/project/lmnr-claude-code-proxy/)

<details><summary>README extract</summary>

This library contains a tiny Rust proxy for Claude Code that can accept
requests from claude-agent-sdk with trace id and span id in order
to associate spans from the proxy with the parent context.

</details>

### langgraph-checkpoint-sqlite

Library with a SQLite implementation of LangGraph checkpoint saver.

`pip install langgraph-checkpoint-sqlite` · installs (wheel) · licence: MIT · rank 2112 · last release 2026-10-30 · [PyPI](https://pypi.org/project/langgraph-checkpoint-sqlite/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-sqlite)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from langgraph.checkpoint.sqlite import SqliteSaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

with SqliteSaver.from_conn_string(":memory:") as checkpointer:
    checkpoint = {
        "v": 4,
        "ts": "2024-07-31T20:14:19.804150+00:00",
...
```

Sections: LangGraph SQLite Checkpoint, 🤔 What is this?, 📖 Documentation, Usage, Async

</details>

### legacy-cgi

Fork of the standard library cgi and cgitb modules removed in Python 3.13

`pip install legacy-cgi` · installs (wheel) · licence: PSF-2.0 · rank 2178 · last release 2025-10-27 · [PyPI](https://pypi.org/project/legacy-cgi/) · [source](https://github.com/jackrosenthal/legacy-cgi)

<details><summary>README extract</summary>

This is a fork of the standard library modules `cgi` and `cgitb`. They have
been removed from the Python standard libary in Python 3.13 by PEP-594.

Sections: Python CGI, Purpose, Documentation

</details>

### llama-index-embeddings-openai

llama-index embeddings openai integration

`pip install llama-index-embeddings-openai` · installs (wheel) · licence: MIT · rank 2309 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-openai/)

### llama-index-llms-openai

llama-index llms openai integration

`pip install llama-index-llms-openai` · installs (wheel) · licence: MIT · rank 2352 · last release 2026-10-12 · [PyPI](https://pypi.org/project/llama-index-llms-openai/)

<details><summary>README extract</summary>

Example:
```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo")
resp = await llm.acomplete("Paul Graham is ")
print(resp)
```

Sections: LlamaIndex Llms Integration: Openai, Setup, Basic Usage, Generate Completions, Chat Responses, Streaming Responses, Stream Complete, Stream Chat, Configure Model, Asynchronous Usage, Set API Key at a Per-Instance Level, LLM Implementation example

</details>

### lsprotocol

Python types for Language Server Protocol.

`pip install lsprotocol` · installs (wheel) · licence: MIT License · rank 2442 · last release 2025-06-17 · [PyPI](https://pypi.org/project/lsprotocol/) · [source](https://github.com/microsoft/lsprotocol)

<details><summary>README extract</summary>

Features:
LSP is used by editors to communicate with various tools to enables services like code completion, documentation on hover, formatting, code analysis, etc. The intent of this library is to allow you to build on top of the types used by LSP. ...

Example:
```python
from lsprotocol import types

position = types.Position(line=10, character=3)
```

Sections: Overview, Usage, Using LSP types, Using built-in type converters

</details>

### loro

Python bindings for [Loro](https://loro.dev)

`pip install loro` · installs (wheel) · licence: not stated · rank 2475 · last release 2026-10-22 · [PyPI](https://pypi.org/project/loro/) · [source](https://github.com/loro-dev/loro-py)

<details><summary>README extract</summary>

Python bindings for Loro CRDT. If you have
any issues or suggestions, please feel free to create an issue or join our
Discord community.

Features:
- High-performance CRDT operations with Rust implementation
- Rich data types support: Text, List, Map, Tree, Movable List, Counter
- Python-friendly API design

Example:
```python
from loro import LoroDoc

# Create a new document
doc = LoroDoc()
# Get a text container
text = doc.get_text("text")
# Insert text
text.insert(0, "Hello, Loro!")
# store the `subscription` reference to prevent garbage collection
sub = doc.subscribe_root(lambda e: print(e))
doc.commit()
```

Sections: loro-py, Features, Quick Start, Prerequisites, 1.17.1

</details>

### language-data

Supplementary data about languages used by the langcodes module

`pip install language-data` · installs (wheel) · licence: MIT License · rank 2534 · last release 2025-11-28 · [PyPI](https://pypi.org/project/language-data/) · [source](https://github.com/georgkrause/language_data)

<details><summary>README extract</summary>

This package is not meant to be used on its own. Please see langcodes for documentation.

`language_data` is a supplement to the langcodes module, for working with standardized codes for human languages. It stores the more bulky and hard-to-index data about languages, particularly what they are named in various languages. ...

Sections: language_data: a supplement to langcodes, Data, Caveats, Dependencies, Update CLDR data

</details>

### langgraph-cli

CLI for interacting with LangGraph API

`pip install langgraph-cli` · installs (wheel) · licence: MIT · rank 2571 · last release 2026-11-06 · [PyPI](https://pypi.org/project/langgraph-cli/) · [source](https://github.com/langchain-ai/langgraph/tree/main/libs/cli)

<details><summary>README extract</summary>

To help you ship LangGraph apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Sections: LangGraph CLI, 🤔 What is this?, 📖 Documentation, Commands, `langgraph new` 🌱, `langgraph dev` 🏃‍♀️, `langgraph up` 🚀, `langgraph build`, `langgraph dockerfile`, `langgraph deploy metrics`, Configuration

</details>

### locate

Locate the file location of your current running script.

`pip install locate` · installs (wheel) · licence: Other/Proprietary License · rank 2782 · last release 2022-12-15 · [PyPI](https://pypi.org/project/locate/)

<details><summary>README extract</summary>

This library provides three callables:

- `this_dir()` returns the directory of the current Python file, or when using from an interactive session, it returns
 the current working directory. ...

Example:
```python
import locate
from pathlib import Path

this_dir = locate.this_dir()

print(f"This file is located in: {this_dir}")
print()

# Create files to demonstrate importing from a directory
foo = Path(locate.this_dir(), "foo")
foo.mkdir(exist_ok=True)

Path(foo, "bar1.py").write_text("print('Importing bar1')")
...
```

Sections: Locate, Safety, Examples, Input, Output, Motivation, Other considerations

</details>

### langgraph-runtime-inmem

Inmem implementation for the LangGraph API server.

`pip install langgraph-runtime-inmem` · installs (wheel) · licence: Elastic-2.0 · rank 2812 · last release 2026-11-03 · [PyPI](https://pypi.org/project/langgraph-runtime-inmem/)

<details><summary>README extract</summary>

This is the inmem implementation of the LangGraph Runtime API.

</details>

### leb128

LEB128(Little Endian Base 128)

`pip install leb128` · installs (wheel) · licence: not stated · rank 2830 · last release 2026-01-09 · [PyPI](https://pypi.org/project/leb128/)

<details><summary>README extract</summary>

LEB128 or Little Endian Base 128 is a form of variable-length code compression used to store an arbitrarily large integer in a small number of bytes. LEB128 is used in the DWARF debug file format and the WebAssembly binary encoding for all integer literals.

Example:
```python
import io
import leb128

# unsigned leb128
assert leb128.u.encode(624485) == bytearray([0xe5, 0x8e, 0x26])
assert leb128.u.decode(bytearray([0xe5, 0x8e, 0x26])) == 624485
assert leb128.u.decode_reader(io.BytesIO(bytearray([0xe5, 0x8e, 0x26]))) == (624485, 3)

# signed leb128
assert leb128.i.encode(-12345) == bytearray([0xc7, 0x9f, 0x7f])
...
```

Sections: LEB128, Example

</details>

### langgraph-api

(no summary)

`pip install langgraph-api` · installs (wheel) · licence: Elastic-2.0 · rank 2847 · last release 2026-11-03 · [PyPI](https://pypi.org/project/langgraph-api/)

<details><summary>README extract</summary>

This package implements the LangGraph API for rapid development and testing. Build and iterate on LangGraph agents with a tight feedback loop. The server is backed by a predominently in-memory data store that is persisted to local disk when the server is restarted. ...

Sections: LangGraph API, Quickstart, Usage, How-To, Attaching a debugger, CLI options

</details>

### llama-parse

Parse files into RAG-Optimized formats.

`pip install llama-parse` · installs (wheel) · licence: MIT · rank 2855 · last release 2026-02-13 · [PyPI](https://pypi.org/project/llama-parse/)

<details><summary>README extract</summary>

> ⚠️ DEPRECATION NOTICE
> This repository and its packages are deprecated and will be maintained until May 1, 2026.
> Please migrate to the new packages:
> - Python: `pip install llama-cloud>=1.0` (GitHub)
> - TypeScript: `npm install @llamaindex/llama-cloud` (GitHub)
> The new packages provide the same functionality with improved performance, ...

Example:
```python
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
...
```

...

</details>

### llama-index-readers-file

llama-index readers file integration

`pip install llama-index-readers-file` · installs (wheel) · licence: MIT · rank 2966 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-readers-file/)

<details><summary>README extract</summary>

This is the default integration for different loaders that are used within `SimpleDirectoryReader`.

Provides support for the following loaders:

- DocxReader
- HWPReader
- PDFReader
- EpubReader
- FlatReader
- HTMLTagReader
- ImageCaptionReader
- ImageReader
- ImageVisionLLMReader
- IPYNBReader
- MarkdownReader
- MboxReader
- PptxReader ...

Example:
```python
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PDFReader,
    EpubReader,
    FlatReader,
    HTMLTagReader,
    ImageCaptionReader,
    ImageReader,
    ImageVisionLLMReader,
    IPYNBReader,
    MarkdownReader,
    MboxReader,
    PptxReader,
    PandasCSVReader,
...
```

Sections: LlamaIndex Readers Integration: File, Usage

</details>

### llama-cloud-services

Tailored SDK clients for LlamaCloud services.

`pip install llama-cloud-services` · installs (wheel) · licence: MIT · rank 3155 · last release 2026-02-13 · [PyPI](https://pypi.org/project/llama-cloud-services/)

<details><summary>README extract</summary>

> ⚠️ DEPRECATION NOTICE
> This repository and its packages are deprecated and will be maintained until May 1, 2026.
> Please migrate to the new packages:
> - Python: `pip install llama-cloud>=1.0` (GitHub)
> - TypeScript: `npm install @llamaindex/llama-cloud` (GitHub)
> The new packages provide the same functionality with improved performance, ...

Example:
```python
from llama_cloud_services import (
    LlamaParse,
    LlamaExtract,
    LlamaCloudIndex,
)
from llama_cloud_services import LlamaParse, LlamaExtract

parser = LlamaParse(api_key="YOUR_API_KEY")
extract = LlamaExtract(api_key="YOUR_API_KEY")
index = LlamaCloudIndex(
    "my_first_index", project_name="default", api_key="YOUR_API_KEY"
)
```

...

</details>

### livekit-plugins-noise-cancellation

Livekit plugin for noise cancellation of inbound AudioStream

`pip install livekit-plugins-noise-cancellation` · installs (wheel) · licence: SEE LICENSE IN https://livekit.io/legal/terms-of-service · rank 3179 · last release 2026-11-06 · [PyPI](https://pypi.org/project/livekit-plugins-noise-cancellation/)

<details><summary>README extract</summary>

Add realtime enhanced noise cancellation to inbound `AudioStream`. Fully compatible with LiveKit Agents.

Requires LiveKit Cloud.

Read more in the documentation

This package runs server-side on inbound audio (e.g. in an agent or on an `AudioStream`). Remote participants’ tracks are cleaned before your code or the agent consumes the audio.

Example:
```python
from livekit.plugins import noise_cancellation

# ...
await session.start(
    # ...,
    room_input_options=room_io.RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC(),
    ),
)
# ...
```

Sections: Enhanced Noise Cancellation Plugin for LiveKit, Audio chain, Usage, In LiveKit Agents, On AudioStream, Available Models, Notes

</details>

### lazy-model

(no summary)

`pip install lazy-model` · installs (wheel) · licence: Apache Software License · rank 3182 · last release 2025-08-07 · [PyPI](https://pypi.org/project/lazy-model/)

<details><summary>README extract</summary>

This library provides a lazy interface for parsing objects from dictionaries. During the parsing, it saves the raw data inside the object and parses each field on demand.

Example:
```python
from lazy_model import LazyModel
from pydantic import validator

class Sample(LazyModel):
    i: int
    s: str

    @validator("s")
    def s_upper(cls, v):
        return v.upper()

obj = Sample.lazy_parse({"i": "10", "s": "test"})

# at this point the data is stored in a raw format inside the object

print(obj.dict)

# >>> {'i': NAO, 's': NAO}

...
```

Sections: Lazy parsing for Pydantic models, Usage

</details>

### linkedin-api-client

Official Python client library for LinkedIn APIs

`pip install linkedin-api-client` · installs (wheel) · licence: Other/Proprietary License · rank 3196 · last release 2023-06-29 · [PyPI](https://pypi.org/project/linkedin-api-client/) · [docs](https://github.com/linkedin-developers/linkedin-api-python-client) · [source](https://github.com/linkedin-developers/linkedin-api-python-client)

<details><summary>README extract</summary>

Features:
This library provides a thin Python client for making requests to LinkedIn APIs, utilizing the Python requests HTTP client library. ...

Example:
```python
from linkedin_api.clients.restli.client import RestliClient

restli_client = RestliClient()

response = restli_client.get(
  resource_path="/me",
  access_token=
)
print(response.entity)
```

Sections: LinkedIn API Python Client, Overview, Features, Requirements, Getting Started, Pre-requisites, Simple API Request Example, Finder Request Example, More Examples, API Reference, `class RestliClient`, Constructor, Properties, Methods

</details>

### langchain-postgres

An integration package connecting Postgres and LangChain

`pip install langchain-postgres` · installs (wheel) · licence: MIT · rank 3347 · last release 2026-10-06 · [PyPI](https://pypi.org/project/langchain-postgres/)

<details><summary>README extract</summary>

The `langchain-postgres` package implementations of core LangChain abstractions using `Postgres`.

The package is released under the MIT license.

Feel free to use the abstraction as provided or else modify them / extend them as appropriate for your own application.

The package supports the asyncpg and psycopg3 drivers.

Example:
```python
from langchain_core.documents import Document
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_postgres import PGEngine, PGVectorStore

# Replace the connection string with your own Postgres connection string
CONNECTION_STRING = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"
...
```

...

</details>

### langchain-experimental

Building applications with LLMs through composability

`pip install langchain-experimental` · installs (wheel) · licence: MIT · rank 3371 · last release 2026-05-22 · [PyPI](https://pypi.org/project/langchain-experimental/) · [source](https://github.com/langchain-ai/langchain-experimental/tree/main/libs/experimental)

<details><summary>README extract</summary>

This package holds experimental LangChain code, intended for research and experimental
uses.

> [!WARNING]
> `langchain-experimental` is being sunset. See #87 for details. Thank you to everyone who has contributed ideas, prototypes, fixes, reviews, and maintenance over the years. ...

</details>

### lib-detect-testenv

Detect test environment - pytest, doctest, unittest, or regular execution

`pip install lib-detect-testenv` · installs (wheel) · licence: MIT License · rank 3501 · last release 2026-10-28 · [PyPI](https://pypi.org/project/lib-detect-testenv/) · [source](https://github.com/bitranox/lib_detect_testenv.git)

<details><summary>README extract</summary>

<!-- Badges -->

Detect test environments: pytest, doctest, and setup.py test

This library provides utility functions to detect whether your code is running in a test environment. It supports detection of pytest, doctest (including PyCharm's docrunner), and setup.py test execution contexts.

Features:
This repository commits a `uv.lock`. It pins every package the project needs, transitive
dependencies included, to an exact version and to the hashes of that version's files. ...

Example:
```python
from lib_detect_testenv import is_testenv_active

if is_testenv_active():
    print("Running in test environment")
else:
    print("Running in production")
```

...

</details>

### llama-index-indices-managed-llama-cloud

llama-index indices llama-cloud integration

`pip install llama-index-indices-managed-llama-cloud` · installs (wheel) · licence: MIT · rank 3541 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-indices-managed-llama-cloud/)

<details><summary>README extract</summary>

NOTE: This package has been deprecated and is no longer maintained. Please use the llama-cloud package instead.

LlamaCloud is a new generation of managed parsing, ingestion, and retrieval services, designed to bring production-grade context-augmentation to your LLM and RAG applications.

Currently, LlamaCloud supports ...

Example:
```python
import os

os.environ[
    "LLAMA_CLOUD_API_KEY"
] = "llx-..."  # can provide API-key in env or in the constructor later on

from llama_index.core import SimpleDirectoryReader
from llama_index.indices.managed.llama_cloud import LlamaCloudIndex

# create a new index (uses managed embeddings by default)
index = LlamaCloudIndex.from_documents(
...
```

Sections: LlamaCloud Index + Retriever, Access, Setup, Usage, Retriever Settings

</details>

### llama-index-cli

llama-index cli

`pip install llama-index-cli` · installs (wheel) · licence: MIT · rank 3633 · last release 2026-04-02 · [PyPI](https://pypi.org/project/llama-index-cli/)

<details><summary>README extract</summary>

> DEPRECATED: This package is deprecated and no longer maintained.
> It will not receive any further updates or bug fixes.
> Please consider alternative solutions.

</details>

### llama-index-readers-llama-parse

llama-index readers llama-parse integration

`pip install llama-index-readers-llama-parse` · installs (wheel) · licence: MIT · rank 3646 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-readers-llama-parse/)

<details><summary>README extract</summary>

NOTE: This package has been deprecated and is no longer maintained. Please use the llama-cloud package instead.

LlamaParse is an API created by LlamaIndex to efficiently parse and represent files for efficient retrieval and context augmentation using LlamaIndex frameworks.

LlamaParse directly integrates with LlamaIndex. ...

Example:
```python
import nest_asyncio

nest_asyncio.apply()

from llama_parse import LlamaParse

parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    verbose=True,
)

# sync
documents = parser.load_data("./my_file.pdf")

# sync batch
...
```

Sections: LlamaParse, Getting Started, Using with `SimpleDirectoryReader`, Examples, Terms of Service

</details>

### lm-eval

A framework for evaluating language models

`pip install lm-eval` · installs (wheel) · licence: MIT · rank 3794 · last release 2026-08-31 · [PyPI](https://pypi.org/project/lm-eval/) · [source](https://github.com/EleutherAI/lm-evaluation-harness)

<details><summary>README extract</summary>

- [2025/12] CLI refactored with subcommands (`run`, `ls`, `validate`) and YAML config file support via `--config`. See the CLI Reference and Configuration Guide.
- [2025/12] Lighter install: Base package no longer includes `transformers`/`torch`. Install model backends separately: `pip install lm_eval[hf]`, `lm_eval[vllm]`, etc. ...

Features:
This project provides a unified framework to test generative language models on a large number of different evaluation tasks.

Features:

- Over 60 standard academic benchmarks for LLMs, with hundreds of subtasks and variants implemented. ...

Example:
```python
import torch

steer_config = {
    "layers.3": {
        "steering_vector": torch.randn(1, 768),
        "bias": torch.randn(1, 768),
        "steering_coefficient": 1,
...

</details>

### lib3mf

lib3mf is an implementation of the 3D Manufacturing Format file standard

`pip install lib3mf` · installs (wheel) · licence: BSD License · rank 3863 · last release 2026-02-23 · [PyPI](https://pypi.org/project/lib3mf/)

<details><summary>README extract</summary>

[![Build Status]](

lib3mf is a C++ implementation of the 3D Manufacturing Format file standard.

It provides 3MF reading and writing capabilities, as well as conversion and validation tools for input and output data. ...

Example:
```python
import lib3mf
from lib3mf import get_wrapper

# Get version
def get_version(wrapper):
    major, minor, micro = wrapper.GetLibraryVersion()
    print("Lib3MF version: {:d}.{:d}.{:d}".format(major, minor, micro), end="")
    hasInfo, prereleaseinfo = wrapper.GetPrereleaseInformation()
    if hasInfo:
        print("-" + prereleaseinfo, end="")
...
```

Sections: lib3mf, Example (Create Cube), Documentation, Obtaining lib3mf, Using lib3mf

</details>

### looseversion

Version numbering for anarchists and software realists

`pip install looseversion` · installs (wheel) · licence: Python Software Foundation License · rank 3865 · last release 2023-07-05 · [PyPI](https://pypi.org/project/looseversion/)

<details><summary>README extract</summary>

A backwards/forwards-compatible fork of `distutils.version.LooseVersion`,
for times when PEP-440 isn't what you need.

The goal of this package is to be a drop-in replacement for the original `LooseVersion`.
It implements an identical interface and comparison logic to `LooseVersion`. ...

Example:
```python
>>> from looseversion import LooseVersion
>>> LooseVersion("1.0.0") < LooseVersion("2.0.0")
True
>>> LooseVersion("1.0.0") < "2"
True
```

Sections: From PyPI, From source, Usage

</details>

### log-symbols

Colored symbols for various log levels for Python

`pip install log-symbols` · installs (wheel) · licence: MIT · rank 3967 · last release 2019-08-08 · [PyPI](https://pypi.org/project/log-symbols/)

<details><summary>README extract</summary>

Colored symbols for various log levels for Python. Find the documentation here:

</details>

### lintrunner

(no summary)

`pip install lintrunner` · installs (wheel) · licence: not stated · rank 3995 · last release 2026-05-08 · [PyPI](https://pypi.org/project/lintrunner/) · [source](https://github.com/suo/lintrunner)

### luqum

A Lucene query parser generating ElasticSearch queries and more !

`pip install luqum` · installs (wheel) · licence: Apache Software License; GNU Lesser General Public License v3 or later (LGPLv3+) · rank 4051 · last release 2025-02-18 · [PyPI](https://pypi.org/project/luqum/)

_README extract left out: share-alike licence._

### llama-index-multi-modal-llms-openai

llama-index multi-modal-llms openai integration

`pip install llama-index-multi-modal-llms-openai` · installs (wheel) · licence: MIT · rank 4233 · last release 2025-09-25 · [PyPI](https://pypi.org/project/llama-index-multi-modal-llms-openai/)

### libcoal

An extension of the Flexible Collision Library

`pip install libcoal` · installs (wheel) · licence: BSD-3-Clause · rank 4302 · last release 2026-05-21 · [PyPI](https://pypi.org/project/libcoal/)

<details><summary>README extract</summary>

FCL was forked in 2015, creating a new project called HPP-FCL.
Since then, a large part of the code has been rewritten or removed (unused and untested code), and new features have been introduced (see below).
Due to these major changes, it was decided in 2024 to rename the HPP-FCL project to Coal. ...

Example:
```python
import numpy as np
import coal
# Optional:
# The Pinocchio library is a rigid body algorithms library and has a handy SE3 module.
# It can be installed as simply as `conda -c conda-forge install pinocchio`.
# Installing pinocchio also installs coal.
import pinocchio as pin

def loadConvexMesh(file_name: str):
    loader = coal.MeshLoader()
...
```

...

</details>

### llama-index-agent-openai

llama-index agent openai integration

`pip install llama-index-agent-openai` · installs (wheel) · licence: MIT · rank 4345 · last release 2025-06-29 · [PyPI](https://pypi.org/project/llama-index-agent-openai/)

### llama-index-program-openai

llama-index program openai integration

`pip install llama-index-program-openai` · installs (wheel) · licence: MIT · rank 4370 · last release 2025-05-30 · [PyPI](https://pypi.org/project/llama-index-program-openai/)

### llama-index-question-gen-openai

llama-index question_gen openai integration

`pip install llama-index-question-gen-openai` · installs (wheel) · licence: MIT · rank 4404 · last release 2025-05-30 · [PyPI](https://pypi.org/project/llama-index-question-gen-openai/)

### lpips

LPIPS Similarity metric

`pip install lpips` · installs (wheel) · licence: BSD License · rank 4407 · last release 2021-08-25 · [PyPI](https://pypi.org/project/lpips/)

<details><summary>README extract</summary>

The Unreasonable Effectiveness of Deep Features as a Perceptual Metric
Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, Oliver Wang. In CVPR, 2018.

Example:
```python
import lpips
loss_fn_alex = lpips.LPIPS(net='alex') # best forward scores
loss_fn_vgg = lpips.LPIPS(net='vgg') # closer to "traditional" perceptual loss, when used for optimization

import torch
img0 = torch.zeros(1,3,64,64) # image should be RGB, IMPORTANT: normalized to [-1,1]
img1 = torch.zeros(1,3,64,64)
d = loss_fn_alex(img0, img1)
```

...

</details>

### loudness

Python bindings for libloudness, for calculating integrated loudness in LUFS (ITU BS.1770 / EBU R 128)

`pip install loudness` · installs (wheel) · licence: MIT · rank 4417 · last release 2025-12-26 · [PyPI](https://pypi.org/project/loudness/)

<details><summary>README extract</summary>

A Python package (battle-tested C++ under the hood) for calculating integrated loudness (LUFS) with the ITU BS.1770 loudness algorithm. Useful for EBU R 128 compliance. Takes NumPy arrays as input (supports mono and stereo/multichannel). Based on libloudness (original implementation by Magnus Bro Kolstø, Nomono).

Example:
```python
import soundfile as sf
import loudness

audio, sr = sf.read("audio.wav", dtype="float32")  # shape (samples, channels)
lufs = loudness.integrated_loudness(audio, sr)
print(f"{lufs:.2f} LUFS")
```

Sections: loudness, Usage example, Performance, [0.2.0] - 2025-12-26, Added, Removed, Alternatives (Python)

</details>

### libtpu

Google Cloud TPU runtime library.

`pip install libtpu` · installs (wheel) · licence: Google Cloud Platform Terms of Service · rank 4425 · last release 2026-11-05 · [PyPI](https://pypi.org/project/libtpu/)

<details><summary>README extract</summary>

`libtpu` is the core library that enables machine learning frameworks like
`JAX`, `PyTorch`, and `TensorFlow` to execute models on Google Cloud TPUs. It
provides core functionality for compilation, inter-chip communication (ICI), and
runtime execution.

`libtpu` also includes a set of SDK primitives for direct TPU interaction and
deployment. ...

Sections: What is libtpu?, Version 0.0.46, Compatibility, Version 0.0.45, Version 0.0.43, Version 0.0.21.1

</details>

### libpinocchio

A fast and flexible implementation of Rigid Body Dynamics algorithms and their analytical derivatives

`pip install libpinocchio` · installs (wheel) · licence: BSD-3-Clause · rank 4438 · last release 2026-07-08 · [PyPI](https://pypi.org/project/libpinocchio/)

<details><summary>README extract</summary>

Pinocchio is open-source software actively developed by the Willow team at Inria in the lovely city of Paris.
Pinocchio instantiates state-of-the-art Rigid Body Algorithms for poly-articulated systems, building upon and revisiting the foundational algorithms introduced by Roy Featherstone. ...

Sections: Pinocchio main features, Documentation, Examples, Tutorials, Pinocchio continuous integrations, Performances, Conda, Docker, ROS, Visualization, Citing Pinocchio, Questions and Issues, Core-dev team, Open-source projects relying on Pinocchio

</details>

### langchain-mongodb

An integration package connecting MongoDB and LangChain

`pip install langchain-mongodb` · installs (wheel) · licence: not stated · rank 4472 · last release 2026-09-22 · [PyPI](https://pypi.org/project/langchain-mongodb/)

<details><summary>README extract</summary>

Example:
```python
import os
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings

# Pull MongoDB Atlas URI from environment variables
MONGODB_ATLAS_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]
DB_NAME = "langchain_db"
COLLECTION_NAME = "test"
VECTOR_SEARCH_INDEX_NAME = "index_name"

...
```

Sections: langchain-mongodb, Usage, Using MongoDBAtlasVectorSearch

</details>

### langgraph-checkpoint-redis

Redis implementation of the LangGraph agent checkpoint saver and store.

`pip install langgraph-checkpoint-redis` · installs (wheel) · licence: MIT License · rank 4494 · last release 2026-11-02 · [PyPI](https://pypi.org/project/langgraph-checkpoint-redis/) · [source](https://www.github.com/redis-developer/langgraph-redis)

<details><summary>README extract</summary>

This repository contains Redis implementations for LangGraph, providing both Checkpoint Savers and Stores functionality.

Features:
The project consists of three main components:

1. Redis Checkpoint Savers: Implementations for storing and managing checkpoints using Redis
2. Redis Stores: Redis-backed key-value stores with optional vector search capabilities
3. ...

Example:
```python
import ast
import operator as op

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.middleware.redis import (
    SemanticCacheMiddleware,
    SemanticCacheConfig,
    ToolResultCacheMiddleware,
    ToolCacheConfig,
)

...
```

...

</details>

### linear-operator

A linear operator implementation, primarily designed for finite-dimensional positive definite operators (i.e. kernel matrices).

`pip install linear-operator` · installs (wheel) · licence: MIT · rank 4564 · last release 2026-02-27 · [PyPI](https://pypi.org/project/linear-operator/) · [docs](https://linear_operator.readthedocs.io) · [source](https://github.com/cornellius-gp/linear_operator/)

<details><summary>README extract</summary>

<!-- docs_intro_start -->

LinearOperator is a PyTorch package for abstracting away the linear algebra routines needed for structured matrices (or operators).

This package is in beta.
Currently, most of the functionality only supports positive semi-definite and triangular matrices. ...

Features:
Before describing what linear operators are and why they make a useful abstraction, it's easiest to see an example.
Let's say you wanted to compute a matrix solve:

$$\boldsymbol A^{-1} \boldsymbol b.$$ ...

Example:
```python
# A = torch.randn(1000, 1000)
# b = torch.randn(1000)
torch.linalg.solve(A, b)  # computes A^{-1} b
```

...

</details>

### langchain-chroma

An integration package connecting Chroma and LangChain.

`pip install langchain-chroma` · installs (wheel) · licence: MIT · rank 4625 · last release 2025-12-12 · [PyPI](https://pypi.org/project/langchain-chroma/) · [docs](https://reference.langchain.com/python/integrations/langchain_chroma/) · [source](https://github.com/langchain-ai/langchain/tree/master/libs/partners/chroma)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-chroma, 🤔 What is this?, 📖 Documentation

</details>

### langmem

Prebuilt utilities for memory management and retrieval.

`pip install langmem` · installs (wheel) · licence: not stated · rank 4629 · last release 2025-10-27 · [PyPI](https://pypi.org/project/langmem/)

<details><summary>README extract</summary>

LangMem helps agents learn and adapt from their interactions over time.

It provides tooling to extract important information from conversations, optimize agent behavior through prompt refinement, and maintain long-term memory. ...

Features:
- 🧩 Core memory API that works with any storage system
- 🧠 Memory management tools that agents can use to record and search information during active conversations "in the hot path" ...

Example:
```python
# Import core components (1)
from langgraph.prebuilt import create_react_agent
from langgraph.store.memory import InMemoryStore
from langmem import create_manage_memory_tool, create_search_memory_tool

# Set up storage (2)
store = InMemoryStore(
    index={
        "dims": 1536,
        "embed": "openai:text-embedding-3-small",
    }
)

...
```

...

</details>

### lazrs

(no summary)

`pip install lazrs` · installs (wheel) · licence: MIT · rank 4656 · last release 2026-07-27 · [PyPI](https://pypi.org/project/lazrs/)

### logzero

Robust and effective logging for Python 2 and 3

`pip install logzero` · installs (wheel) · licence: MIT License · rank 4664 · last release 2021-03-17 · [PyPI](https://pypi.org/project/logzero/)

<details><summary>README extract</summary>

Robust and effective logging for Python 2 and 3.

Features

* Easy logging to console and/or (rotating) file.
* Provides a fully configured standard Python logger object.
* JSON logging (with integrated python-json-logger)
* Pretty formatting, including level-specific colors in the console. ...

Example:
```python
from logzero import logger

logger.debug("hello")
logger.info("info")
logger.warning("warn")
logger.error("error")

# This is how you'd log an exception
try:
    raise Exception("this is a demo exception")
except Exception as e:
    logger.exception(e)

# JSON logging
import logzero
logzero.json()

logger.info("JSON test")

...
```

Sections: logzero, JSON logging

</details>

### locust-cloud

Locust Cloud

`pip install locust-cloud` · installs (wheel) · licence: MIT · rank 4753 · last release 2025-12-15 · [PyPI](https://pypi.org/project/locust-cloud/) · [source](https://github.com/locustcloud/locust-cloud)

<details><summary>README extract</summary>

See for general information on Locust Cloud, or for usage instructions.

If you encounter issues with the code here, contact Locust Cloud support or file an issue here

</details>

### langchain-tavily

An integration package connecting Tavily and LangChain

`pip install langchain-tavily` · installs (wheel) · licence: MIT License · rank 4771 · last release 2026-04-16 · [PyPI](https://pypi.org/project/langchain-tavily/) · [source](https://github.com/tavily-ai/langchain-tavily)

<details><summary>README extract</summary>

This package contains the LangChain integration with Tavily

Don't miss out on these exciting new features! Check out the full documentation to learn more.

Example:
```python
from langchain_tavily import TavilySearch

tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # include_favicon=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
...
```

Sections: 🦜️🔗 LangChain Tavily, Credentials, Tavily Search, Instantiation, Invoke directly with args, Agent Tool Calling, Tavily Extract, Tavily Crawl, Tavily Map

</details>

### liger-kernel

Efficient Triton kernels for LLM Training

`pip install liger-kernel` · installs (wheel) · licence: not stated · rank 4775 · last release 2026-10-21 · [PyPI](https://pypi.org/project/liger-kernel/)

<details><summary>README extract</summary>

Stable
 Nightly
 Discord

Installation | Getting Started | Examples | High-level APIs | Low-level APIs | Cite our work

 Latest News 🔥

 - [2025/12/19] We announced a liger kernel discord channel at We will be hosting Liger Kernel x Triton China Meetup in mid of January 2026
 - [2025/03/06] We release a joint blog post on TorchTune × Liger - Peak ...

Features:
- Ease of use: Simply patch your Hugging Face model with one line of code, or compose your own model using our Liger Kernel modules. ...

Example:
```python
from liger_kernel.chunked_loss import LigerFusedLinearORPOLoss
orpo_loss = LigerFusedLinearORPOLoss()
y = orpo_loss(lm_head.weight, x, target)
```

...

</details>

### logzio-python-handler

Logging handler to send logs to your Logz.io account with bulk SSL

`pip install logzio-python-handler` · installs (wheel) · licence: Apache License 2 · rank 4779 · last release 2026-02-01 · [PyPI](https://pypi.org/project/logzio-python-handler/)

### llama-index-embeddings-bedrock

llama-index embeddings bedrock integration

`pip install llama-index-embeddings-bedrock` · installs (wheel) · licence: MIT · rank 4847 · last release 2026-08-29 · [PyPI](https://pypi.org/project/llama-index-embeddings-bedrock/)

<details><summary>README extract</summary>

This integration provides support for Amazon Bedrock embedding models through LlamaIndex.

Example:
```python
from llama_index.embeddings.bedrock import BedrockEmbedding

# Initialize the embedding model
embed_model = BedrockEmbedding(
    model_name="cohere.embed-english-v3",
    region_name="us-east-1",
)

# Get a single embedding
embedding = embed_model.get_text_embedding("Hello world")

# Get batch embeddings
...
```

Sections: LlamaIndex Embeddings Integration: Bedrock, Usage, Amazon Titan, Cohere, Configuration, Use an Application Inference Profile, Examples

</details>

### lakefs-sdk

lakeFS API

`pip install lakefs-sdk` · installs (wheel) · licence: BUSL-1.1 · rank 4897 · last release 2026-10-01 · [PyPI](https://pypi.org/project/lakefs-sdk/)

<details><summary>README extract</summary>

lakeFS HTTP API

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 1.0.0
- Package version: 1.88.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Python 3.7+

Example:
```python
import time
import lakefs_sdk
from lakefs_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lakefs_sdk.Configuration(
    host = "/api/v1"
)

...
```

Sections: lakefs-sdk, Requirements., Setuptools, Tests, Getting Started, Documentation for API Endpoints, Documentation For Models, basic_auth, jwt_token, cookie_auth

</details>

### libarchive-c

Python interface to libarchive

`pip install libarchive-c` · installs (wheel) · licence: CC0 · rank 4915 · last release 2025-05-22 · [PyPI](https://pypi.org/project/libarchive-c/)

<details><summary>README extract</summary>

A Python interface to libarchive. It uses the standard ctypes module to
dynamically load and access the C library.

Example:
```python
import libarchive
```

Sections: Compatibility, python, libarchive, Usage, Extracting archives, Reading archives, Displaying progress, Creating archives, Symbolic links, File metadata codecs

</details>

### langchain-qdrant

An integration package connecting Qdrant and LangChain

`pip install langchain-qdrant` · installs (wheel) · licence: MIT · rank 4934 · last release 2025-10-22 · [PyPI](https://pypi.org/project/langchain-qdrant/) · [docs](https://reference.langchain.com/python/integrations/langchain_qdrant/) · [source](https://github.com/langchain-ai/langchain/tree/master/libs/partners/qdrant)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-qdrant, 🤔 What is this?, 📖 Documentation

</details>

### livekit-plugins-krisp-internal

LiveKit Krisp Viva noise filter (private wheel)

`pip install livekit-plugins-krisp-internal` · installs (wheel) · licence: SEE LICENSE IN https://livekit.io/legal/terms-of-service · rank 5038 · last release 2026-10-29 · [PyPI](https://pypi.org/project/livekit-plugins-krisp-internal/)

<details><summary>README extract</summary>

Closed-source Python wheel that wraps the Krisp Viva noise filter SDK and exposes it as a LiveKit `FrameProcessor`. Consumed by the public `livekit-plugins-krisp` plugin; not intended for direct end-user installation.

Example:
```python
from livekit.plugins.krisp_internal import KrispVivaFilterFrameProcessor

processor = KrispVivaFilterFrameProcessor(
    noise_suppression_level=100,  # 0..=100, runtime-adjustable via the property
    frame_duration_ms=10,         # one of 10, 15, 20, 30, 32
    sample_rate=16000,            # one of 8000, 16000, 24000, 32000, 44100, 48000
)

...
```

Sections: LiveKit Krisp Viva Noise Filter — Internal Wheel, Requirements, Usage

</details>

### langchain-cohere

An integration package connecting Cohere and LangChain

`pip install langchain-cohere` · installs (wheel) · licence: MIT License · rank 5267 · last release 2026-06-01 · [PyPI](https://pypi.org/project/langchain-cohere/) · [source](https://github.com/langchain-ai/langchain-cohere)

<details><summary>README extract</summary>

This package contains the LangChain integrations for Cohere.

Cohere empowers every developer and enterprise to build amazing products and capture true business value with language AI.

Example:
```python
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage

llm = ChatCohere()

messages = [HumanMessage(content="Hello, can you introduce yourself?")]
print(llm.invoke(messages))
```

Sections: Langchain-Cohere, Usage Examples, Chat, Vision (Image Inputs), ReAct Agent, RAG Retriever, Text Embedding

</details>

### llama-cpp-python

Python bindings for the llama.cpp library

`pip install llama-cpp-python` · installs from source (sdist only) · licence: MIT · rank 5304 · last release 2026-10-01 · [PyPI](https://pypi.org/project/llama-cpp-python/) · [docs](https://llama-cpp-python.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

Simple Python bindings for @ggerganov's `llama.cpp` library.
This package provides:

- Low-level access to C API via `ctypes` interface.
- High-level Python API for text completion
 - OpenAI-like API
 - LangChain compatibility
 - LlamaIndex compatibility ...

Example:
```python
from llama_cpp import Llama

llm = Llama(
      model_path="./models/7B/llama-model.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
...
```

...

</details>

### langchain-quickjs

JavaScript REPL middleware for deepagents

`pip install langchain-quickjs` · installs (wheel) · licence: MIT License · rank 5308 · last release 2026-11-07 · [PyPI](https://pypi.org/project/langchain-quickjs/) · [docs](https://github.com/langchain-ai/deepagents/tree/main/libs/partners/quickjs) · [source](https://github.com/langchain-ai/deepagents)

<details><summary>README extract</summary>

A `deepagents` middleware that gives an agent a persistent, sandboxed JavaScript REPL tool, backed by `quickjs-rs` (QuickJS embedded via PyO3 + rquickjs).

Instead of issuing N serial tool calls, the model can write one block of JavaScript that orchestrates work in-loop — variables and functions defined in one call survive into the next, ...

Features:
Tool calling is fine for small, discrete requests. It falls apart when the model needs to:

- loop over a list and call a tool per item
- run two independent tool calls concurrently ...

Example:
```python
from deepagents import create_deep_agent
from langchain_quickjs import CodeInterpreterMiddleware

agent = create_deep_agent(
    model="claude-sonnet-4-6",
    middleware=[CodeInterpreterMiddleware()],
)

...

</details>

### logging

A logging module for Python

`pip install logging` · installs from source (sdist only) · licence: not stated · rank 5337 · last release 2013-06-04 · [PyPI](https://pypi.org/project/logging/)

<details><summary>README extract</summary>

This module is intended to provide a standard error logging mechanism in Python as per PEP 282.

</details>

### langgraph-supervisor

An implementation of a supervisor multi-agent architecture using LangGraph

`pip install langgraph-supervisor` · installs (wheel) · licence: MIT · rank 5355 · last release 2025-11-19 · [PyPI](https://pypi.org/project/langgraph-supervisor/) · [source](https://github.com/langchain-ai/langgraph-supervisor-py)

<details><summary>README extract</summary>

> Note: We now recommend using the supervisor pattern directly via tools rather than this library for most use cases. The tool-calling approach gives you more control over context engineering and is the recommended pattern in the LangChain multi-agent guide. See our supervisor tutorial for a step-by-step guide. ...

Features:
- 🤖 Create a supervisor agent to orchestrate multiple specialized agents
- 🛠️ Tool-based agent handoff mechanism for communication between agents
- 📝 Flexible message history management for conversation control ...

Example:
```python
from langchain_openai import ChatOpenAI

from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent

model = ChatOpenAI(model="gpt-4o")

# Create specialized agents

...

</details>

### langchain-nvidia-ai-endpoints

An integration package connecting NVIDIA AI Endpoints and LangChain

`pip install langchain-nvidia-ai-endpoints` · installs (wheel) · licence: MIT License · rank 5366 · last release 2026-10-14 · [PyPI](https://pypi.org/project/langchain-nvidia-ai-endpoints/) · [source](https://github.com/langchain-ai/langchain-nvidia)

<details><summary>README extract</summary>

The `langchain-nvidia-ai-endpoints` package contains LangChain integrations for chat models and embeddings powered by NVIDIA AI Foundation Models, and hosted on the NVIDIA API Catalog.

A strong starting point is Nemotron, NVIDIA's open model family built for agentic AI. ...

Example:
```python
import getpass
import os

if not os.environ.get("NVIDIA_API_KEY", "").startswith("nvapi-"):
    nvidia_api_key = getpass.getpass("Enter your NVIDIA API key: ")
    assert nvidia_api_key.startswith("nvapi-"), f"{nvidia_api_key[:5]}... is not a valid key"
    os.environ["NVIDIA_API_KEY"] = nvidia_api_key
```

...

</details>

### libpff-python

Python bindings for libpff

`pip install libpff-python` · installs (wheel) · licence: LGPL-3.0-or-later · rank 5459 · last release 2026-09-26 · [PyPI](https://pypi.org/project/libpff-python/) · [docs](https://github.com/libyal/libpff/wiki/Home) · [source](https://github.com/libyal/libpff)

_README extract left out: share-alike licence._

### laces

Django components that know how to render themselves.

`pip install laces` · installs (wheel) · licence: BSD License · rank 5467 · last release 2025-01-14 · [PyPI](https://pypi.org/project/laces/) · [docs](https://github.com/tbrlpld/laces/blob/main/README.md) · [source](https://github.com/tbrlpld/laces)

<details><summary>README extract</summary>

Django components that know how to render themselves.

Laces components provide a simple way to combine data (in the form of Python objects) with the Django templates that are meant to render that data.
The components can then be simply rendered in any other template using the `{% component %}` template tag. ...

Features:
"Laces" is somewhat of a reference to the feature of tying data and templates together.
The components are also "self-rendering," which could be seen as "self-reliance," which relates to "bootstrapping."
And while "bootstraps" aren't really "(shoe) ...

Example:
```python
# my_app/components.py

from laces.components import Component

class WelcomePanel(Component):
    template_name = "my_app/components/welcome.html"
```

...

</details>

### libhoney

Python library for sending data to Honeycomb

`pip install libhoney` · installs (wheel) · licence: Apache Software License · rank 5475 · last release 2024-03-06 · [PyPI](https://pypi.org/project/libhoney/) · [source](https://github.com/honeycombio/libhoney-py)

<details><summary>README extract</summary>

Python library for sending events to Honeycomb, a service for debugging your software in production.

- Usage and Examples

For tracing support and automatic instrumentation of Django, Flask, AWS Lambda, and other frameworks, check out our Beeline for Python.

</details>

### lazy

Lazy attributes for Python objects

`pip install lazy` · installs (wheel) · licence: BSD-2-Clause · rank 5518 · last release 2026-07-04 · [PyPI](https://pypi.org/project/lazy/) · [docs](https://lazy.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Features:
Lazy attributes are computed attributes that are evaluated only
once, the first time they are used. Subsequent uses return the
results of the first call. They come handy when code should run

- *late*, i.e. just before it is needed, and ...

Example:
```python
from lazy import lazy

class FileUploadTmpStore(object):

    @lazy
    def store(self):
        location = settings.get('fs.filestore')
        return FileSystemStore(location)

    def put(self, uid, fp):
        self.store.put(uid, fp)
        fp.seek(0)

    def get(self, uid, default=None):
        return self.store.get(uid, default)

...
```

...

</details>

### launchdarkly-api

LaunchDarkly REST API

`pip install launchdarkly-api` · installs (wheel) · licence: Apache 2.0 · rank 5520 · last release 2026-10-30 · [PyPI](https://pypi.org/project/launchdarkly-api/) · [source](https://github.com/launchdarkly/api-client-python)

<details><summary>README extract</summary>

This repository contains a client library for LaunchDarkly's REST API. This client was automatically
generated from our OpenAPI specification using a code generation library.

This REST API is for custom integrations, data export, or automating your feature flag workflows. ...

Example:
```python
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "
)

...
```

...

</details>

### langgraph-checkpoint-aws

A LangChain checkpointer implementation that uses Bedrock Session Management Service and ElastiCache Valkey to enable stateful and resumable LangGraph agents.

`pip install langgraph-checkpoint-aws` · installs (wheel) · licence: MIT · rank 5563 · last release 2026-11-06 · [PyPI](https://pypi.org/project/langgraph-checkpoint-aws/) · [source](https://github.com/langchain-ai/langchain-aws/tree/main/libs/langgraph-checkpoint-aws)

<details><summary>README extract</summary>

A custom AWS-based persistence solution for LangGraph agents that provides multiple storage backends including Bedrock AgentCore Memory, DynamoDB with S3 offloading, and high-performance Valkey (Redis-compatible) storage.

Features:
This package provides multiple persistence solutions for LangGraph agents:

Example:
```python
from langgraph_checkpoint_aws.async_saver import AsyncBedrockSessionSaver
from langgraph_checkpoint_aws import AsyncValkeySaver
from langgraph_checkpoint_aws import DynamoDBSaver

# Async Bedrock usage
session_saver = AsyncBedrockSessionSaver(region_name="us-west-2")
session_id = (await session_saver.session_client.create_session()).session_id

...
```

...

</details>

### libify

Import Databricks notebooks as libraries/modules

`pip install libify` · installs (wheel) · licence: MIT License · rank 5589 · last release 2020-09-22 · [PyPI](https://pypi.org/project/libify/)

<details><summary>README extract</summary>

Libify makes it easy to import notebooks in Databricks. Notebook imports can also be nested to create complex workflows easily. Supports Databricks Runtime Version 5.5 and above.

<details>
 <summary><strong>Installation</strong></summary>

1. Click the Clusters icon in the sidebar
2. Click a cluster name (make sure the cluster is running)
3. ...

Example:
```python
import libify
libify.exporter(globals())
```

Sections: Libify, Typical Usage

</details>

### lzfse

Python bindings for the LZFSE reference implementation

`pip install lzfse` · installs (wheel) · licence: MIT · rank 5663 · last release 2026-10-16 · [PyPI](https://pypi.org/project/lzfse/) · [source](https://github.com/m1stadev/lzfse)

<details><summary>README extract</summary>

Python bindings for the LZFSE reference implementation.

This project is based on ydkhatril's pyliblzfse, I have only added CI and renamed the library to lzfse.

</details>

### lob

Lob Python Bindings

`pip install lob` · installs from source (sdist only) · licence: MIT License · rank 5664 · last release 2022-02-19 · [PyPI](https://pypi.org/project/lob/)

<details><summary>README extract</summary>

This is the python wrapper for the Lob.com API. See full Lob.com documentation here. For best results, be sure that you're using the latest version of the Lob API and the latest version of the python wrapper.

This library supports active Python releases (i.e., versions which have not reached their end of life), as well as PyPy 3. ...

Sections: lob-python, Getting Started, Registration, Usage, Examples, API Documentation

</details>

### ladybug

Highly scalable, extremely fast, easy-to-use embeddable graph database

`pip install ladybug` · installs (wheel) · licence: MIT · rank 5677 · last release 2026-11-06 · [PyPI](https://pypi.org/project/ladybug/) · [docs](https://docs.ladybugdb.com/) · [source](https://github.com/LadybugDB/ladybug-python)

<details><summary>README extract</summary>

Ladybug is an embedded graph database built for query speed and scalability. Ladybug is optimized for handling complex analytical workloads
on very large databases and provides a set of retrieval features, such as a full text search and vector indices. Our core feature set includes:

- Flexible Property Graph Data Model and Cypher query language ...

Sections: Ladybug, Getting Started, Build from Source, Contact

</details>

### lean-lsp-mcp

Lean Theorem Prover MCP

`pip install lean-lsp-mcp` · installs (wheel) · licence: MIT · rank 5710 · last release 2026-11-03 · [PyPI](https://pypi.org/project/lean-lsp-mcp/) · [source](https://github.com/oOo0oOo/lean-lsp-mcp)

<details><summary>README extract</summary>

MCP server that allows agentic interaction with the Lean theorem prover via the Language Server Protocol using leanclient. This server provides a range of tools for LLM agents to understand, analyze and interact with Lean projects.

Features:
* Rich Lean Interaction: Access diagnostics, goal states, term information, hover documentation and more.
* External Search Tools: Use `LeanSearch`, `Loogle`, `Lean Finder` and `Lean Hammer` to find relevant theorems and definitions. ...

Sections: lean-lsp-mcp, Lean Theorem Prover MCP, Key Features, Setup, Overview, 2. Run `lake build`, 3. Configure your IDE/Setup, MCP Tools, List of available tools, Disabling Tools, MCP Configuration, Environment Variables, Transport Methods, OpenAI Secure MCP Tunnel

</details>

### leanclient

Interact with the Lean theorem prover language server

`pip install leanclient` · installs (wheel) · licence: MIT · rank 5727 · last release 2026-08-19 · [PyPI](https://pypi.org/project/leanclient/) · [docs](https://leanclient.readthedocs.io) · [source](https://github.com/oOo0oOo/leanclient)

<details><summary>README extract</summary>

leanclient is a thin Python wrapper around the native Lean 4 language server.
It enables interaction with a Lean 4 language server instance running in a subprocess.

Check out the documentation for more information.

Features:
- Interact: Query and change lean files via the LSP.
- Thin wrapper: Directly expose the Lean Language Server.
- Fast: Typically more than 95% of time is spent waiting.
- Parallel: Easy batch processing of files using all your cores.

Example:
```python
import leanclient as lc

# Start a new client, point it to your lean project root (where lakefile.toml is located).
PROJECT_PATH = "path/to/your/lean/project/root/"
client = lc.LeanLSPClient(PROJECT_PATH)

# Query a lean file in your project
file_path = "MyProject/Basic.lean"
...

</details>

### langchainhub

The LangChain Hub API client

`pip install langchainhub` · installs (wheel) · licence: MIT License · rank 5737 · last release 2024-08-11 · [PyPI](https://pypi.org/project/langchainhub/)

### loongsuite-util-genai

LoongSuite GenAI Utils

`pip install loongsuite-util-genai` · installs (wheel) · licence: Apache-2.0 · rank 5769 · last release 2026-05-11 · [PyPI](https://pypi.org/project/loongsuite-util-genai/) · [source](https://github.com/alibaba/loongsuite-python-agent)

<details><summary>README extract</summary>

本文档描述 LoongSuite 对 OpenTelemetry GenAI Util 的扩展：适用范围、接入步骤与配置项。\ 对外发行\ 时 PyPI 包名为 \ loongsuite-util-genai\ ；Python 导入命名空间仍为 \ `opentelemetry.util.genai`\ （与上游 GenAI Util 一致，见下节）。本仓库源码目录为 \ `util/opentelemetry-util-genai`\ 。 ...

Example:
```python
from opentelemetry import trace
from opentelemetry.util.genai.extended_handler import get_extended_telemetry_handler
from opentelemetry.util.genai.types import InputMessage, LLMInvocation, OutputMessage, Text

# 可选：确认当前进程已由 Instrumentation 设置 TracerProvider（未设置时多为 NoOp）
_ = trace.get_tracer_provider()

handler = get_extended_telemetry_handler()

...
```

...

</details>

### lemminflect

A python module for English lemmatization and inflection.

`pip install lemminflect` · installs (wheel) · licence: MIT License · rank 5786 · last release 2022-10-02 · [PyPI](https://pypi.org/project/lemminflect/)

<details><summary>README extract</summary>

A python module for English lemmatization and inflection.

LemmInflect uses a dictionary approach to lemmatize English words and inflect them into forms specified by a user supplied Universal Dependencies or Penn Treebank tag. ...

Example:
```python
> from lemminflect import getLemma
getLemma('watches', upos='VERB')
('watch',)
```

Sections: &nbsp; LemmInflect, About, Documentation, Accuracy of the Lemmatizer, Library Usage, Usage as a Spacy Extension, Issues

</details>

### langgraph-checkpoint-mongodb

Library with a MongoDB implementation of LangGraph checkpoint saver.

`pip install langgraph-checkpoint-mongodb` · installs (wheel) · licence: not stated · rank 5820 · last release 2026-10-08 · [PyPI](https://pypi.org/project/langgraph-checkpoint-mongodb/)

<details><summary>README extract</summary>

Implementation of LangGraph CheckpointSaver that uses MongoDB.

Example:
```python
from langgraph.checkpoint.mongodb import MongoDBSaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "checkpoint_example"

with MongoDBSaver.from_conn_string(MONGODB_URI, DB_NAME) as checkpointer:
    checkpoint = {
...
```

Sections: LangGraph Checkpoint MongoDB, Usage, Async

</details>

### langchain-pinecone

An integration package connecting Pinecone and LangChain

`pip install langchain-pinecone` · does not install on CPython 3.14 · licence: MIT · rank 5861 · last release 2025-11-02 · [PyPI](https://pypi.org/project/langchain-pinecone/) · [source](https://github.com/langchain-ai/langchain-pinecone/tree/main/libs/pinecone)

<details><summary>README extract</summary>

This package contains the LangChain integration with Pinecone.

Example:
```python
from pinecone import ServerlessSpec

index_name = "langchain-test-index"  # change if desired

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

...
```

Sections: langchain-pinecone, Running Tests, Required Environment Variables for Tests, Usage, Initialization, Manage vector store, Add items to vector store, Delete items from vector store, Query vector store, Query directly, Similarity search with score, Query by turning into retriever, Async Model Listing

</details>

### lightkube-models

Models and Resources for lightkube module

`pip install lightkube-models` · installs (wheel) · licence: MIT · rank 5867 · last release 2026-08-29 · [PyPI](https://pypi.org/project/lightkube-models/) · [source](https://github.com/gtsystem/lightkube-models)

<details><summary>README extract</summary>

This is a python module containing definitions of kubernetes
models and resources to be used by lightkube.

The version of this package (first 3 parts `major.minor.micro`), match
the kubernetes schema version used to generate the models.

You should install the module version matching your kubernetes installation or just
use compatible resources.

</details>

### ldapdomaindump

Active Directory information dumper via LDAP

`pip install ldapdomaindump` · installs (wheel) · licence: MIT · rank 5885 · last release 2025-04-04 · [PyPI](https://pypi.org/project/ldapdomaindump/)

### libigl

libigl: A simple C++ geometry processing library

`pip install libigl` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 5895 · last release 2026-09-01 · [PyPI](https://pypi.org/project/libigl/)

<details><summary>README extract</summary>

This repository contains the source code for the python bindings for the C++
libigl library written using
nanobind. Functions allow NumPy
arrays as input and output for dense matrices and vectors and SciPy sparse
matrices for sparse matrices.

Example:
```python
import importlib.metadata
libigl_version = importlib.metadata.version('libigl')
```

Sections: libigl Python Bindings, Documentation, Getting the current version of libigl within python code, Compiling and modifying the bindings, Adding a missing binding, Packaging a wheel from an existing build, Downloading all the artifacts

</details>

### literalai

An SDK for observability in Python applications

`pip install literalai` · installs from source (sdist only) · licence: Apache License 2.0 · rank 5932 · last release 2025-04-16 · [PyPI](https://pypi.org/project/literalai/)

<details><summary>README extract</summary>

Example:
```python
from literalai import LiteralClient
from dotenv import load_dotenv

load_dotenv()

literalai_client = LiteralClient()

@literalai_client.step(type="run")
def my_step(input):
    return f"World"

@literalai_client.thread
def main():
    print(my_step("Hello"))

main()
client.flush_and_stop()
print("Done")
```

Sections: Literal AI client, Usage

</details>

### lzstring

lz-string for python

`pip install lzstring` · installs from source (sdist only) · licence: MIT License · rank 5956 · last release 2018-06-01 · [PyPI](https://pypi.org/project/lzstring/)

<details><summary>README extract</summary>

lz-string for python 2/3

Based on the LZ-String javascript found here:

Example:
```python
>>> import lzstring
>>> x = lzstring.LZString()
>>> compressed = x.compressToBase64(u'你好') # 'gbyl9NI='
>>> x.decompressFromBase64(compressed) # '你好'
```

Sections: lz-string-python, Example

</details>

### langextract

LangExtract: A library for extracting structured data from language models

`pip install langextract` · installs (wheel) · licence: Apache-2.0 · rank 5958 · last release 2026-11-07 · [PyPI](https://pypi.org/project/langextract/) · [docs](https://github.com/google/langextract/blob/main/README.md) · [source](https://github.com/google/langextract)

<details><summary>README extract</summary>

Features:
1. Precise Source Grounding: Maps every extraction to its exact location in the source text, enabling visual highlighting for easy traceability and verification.
2. ...

Example:
```python
import langextract as lx
import textwrap

# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")

...
```

...

</details>

### lovelyplots

Format Matplotlib Plots for thesis, scientific papers and reports.

`pip install lovelyplots` · installs (wheel) · licence: MIT License · rank 5960 · last release 2024-03-06 · [PyPI](https://pypi.org/project/lovelyplots/)

<details><summary>README extract</summary>

> [!WARNING]
> As of version 1.0.0, you need to add ``import lovelyplots`` before setting the style (``plt.style.use('ipynb')``).

LovelyPlots is a repository containing ``matplotlib`` style sheets to nicely format figures for scientific papers, thesis and presentations while keeping them fully editable in ``Adobe Illustrator``. ...

Example:
```python
import lovelyplots
import matplotlib.pyplot as plt
plt.style.use('ipynb')
```

Sections: LovelyPlots, Usage, Examples, Styles, Color cycles, Lines styles, markers and combinations styles, Color maps, Utils, Fonts, Tips and Tricks, Adobe Illustrator, Latex and SVG files, Retina displays, Useth in Google Colab

</details>

### livekit-plugins-ai-coustics

LiveKit AI Coustics noise filtering plugin

`pip install livekit-plugins-ai-coustics` · installs (wheel) · licence: SEE LICENSE IN https://livekit.io/legal/terms-of-service · rank 6004 · last release 2026-10-19 · [PyPI](https://pypi.org/project/livekit-plugins-ai-coustics/)

<details><summary>README extract</summary>

Python LiveKit plugin for Ai-coustics audio enhancement, providing real-time noise filtering and audio quality improvement for LiveKit audio streams.

Example:
```python
from livekit.agents import RoomIO
from livekit.plugins import ai_coustics

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    # Configure RoomIO with AI-coustics noise cancellation
    room_io = RoomIO(
        # Available enhancement models:
        # - EnhancerModel.QUAIL_L      (default, best for voice enhancement)
...
```

Sections: Ai-coustics Audio Enhancement Plugin for Python, Requirements, Usage, LiveKit Agents Framework

</details>

### llama-index-vector-stores-postgres

llama-index vector_stores postgres integration

`pip install llama-index-vector-stores-postgres` · installs (wheel) · licence: MIT · rank 6023 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-postgres/)

<details><summary>README extract</summary>

This integration allows you to use PostgreSQL with the `pgvector` extension as a vector store for LlamaIndex.

Example:
```python
from llama_index.vector_stores.postgres import PGVectorStore

vector_store = PGVectorStore.from_params(
    database="your_database",
    host="localhost",
    password="your_password",
    port="5432",
    user="your_user",
    table_name="your_table",
    embed_dim=1536,  # OpenAI embedding dimension
)
```

Sections: LlamaIndex Vector_Stores Integration: Postgres, Usage, Basic Setup, Query Modes, MMR (Maximal Marginal Relevance) Queries, MMR Parameters

</details>

### lightkube

Lightweight kubernetes client library

`pip install lightkube` · installs (wheel) · licence: MIT · rank 6054 · last release 2026-10-31 · [PyPI](https://pypi.org/project/lightkube/) · [source](https://github.com/gtsystem/lightkube)

<details><summary>README extract</summary>

Modern lightweight kubernetes module for python

Features:
* *Simple* interface shared across all kubernetes APIs.
* Extensive *type hints* to avoid common mistakes and to support autocompletion. ...

Example:
```python
from lightkube import Client
from lightkube.resources.core_v1 import Pod

with Client() as client:
    pod = client.get(Pod, name="my-pod", namespace="default")
    print(pod.namespace.uid)
```

Sections: lightkube, Highlights, Usage, List, Create, Modify, Delete, Monitoring & Interaction

</details>

### llama-index-llms-azure-openai

llama-index llms azure openai integration

`pip install llama-index-llms-azure-openai` · installs (wheel) · licence: MIT · rank 6104 · last release 2026-09-25 · [PyPI](https://pypi.org/project/llama-index-llms-azure-openai/)

<details><summary>README extract</summary>

Example:
```python
OPENAI_API_VERSION = "2023-07-01-preview"
AZURE_OPENAI_ENDPOINT = "
OPENAI_API_KEY = "<your-api-key>"

import os

os.environ["OPENAI_API_KEY"] = "<your-api-key>"
os.environ[
    "AZURE_OPENAI_ENDPOINT"
] = "
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"

# Use your LLM
from llama_index.llms.azure_openai import AzureOpenAI

...
```

Sections: LlamaIndex Llms Integration: Azure Openai, Prerequisites, Set the environment variables, Streaming completion, Streaming chat, LLM Implementation example

</details>

### langserve

(no summary)

`pip install langserve` · installs (wheel) · licence: Other/Proprietary License · rank 6271 · last release 2025-10-17 · [PyPI](https://pypi.org/project/langserve/) · [source](https://github.com/langchain-ai/langserve)

<details><summary>README extract</summary>

> [!WARNING]
> We recommend using LangGraph Platform rather than LangServe for new projects.
> Please see the LangGraph Platform Migration Guide for more information.
> We will continue to accept bug fixes for LangServe from the community; however, we
> will not be accepting new feature contributions.

Features:
LangServe helps developers
deploy `LangChain` runnables and chains
as a REST API.

This library is integrated with FastAPI and
uses pydantic for data validation. ...

Example:
```python
# !/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
...

</details>

### lazr.config

Create configuration schemas, and process and validate configurations.

`pip install lazr.config` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6291 · last release 2026-08-01 · [PyPI](https://pypi.org/project/lazr.config/) · [docs](https://lazrconfig.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/lazr.config)

_README extract left out: share-alike licence._

### llama-index-embeddings-azure-openai

llama-index embeddings azure openai integration

`pip install llama-index-embeddings-azure-openai` · installs (wheel) · licence: MIT · rank 6328 · last release 2026-10-01 · [PyPI](https://pypi.org/project/llama-index-embeddings-azure-openai/)

### lazr.delegates

Easily write objects that delegate behavior

`pip install lazr.delegates` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6382 · last release 2026-08-01 · [PyPI](https://pypi.org/project/lazr.delegates/) · [docs](https://lazrdelegates.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/lazr.delegates)

_README extract left out: share-alike licence._

### llama-index-embeddings-google-genai

llama-index embeddings google genai integration

`pip install llama-index-embeddings-google-genai` · installs (wheel) · licence: MIT · rank 6427 · last release 2026-08-29 · [PyPI](https://pypi.org/project/llama-index-embeddings-google-genai/)

<details><summary>README extract</summary>

This package provides a wrapper around the Google GenAI API, allowing you to use Gemini and Vertex AI embeddings in your projects.

Example:
```python
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

embed_model = GoogleGenAIEmbedding(model_name="gemini-embedding-2-preview")

embeddings = embed_model.get_text_embedding("Hello, world!")
print(embeddings)
```

Sections: Google GenAI Embeddings, Usage, Vertex AI

</details>

### langchain-ibm

An integration package connecting IBM watsonx.ai and LangChain

`pip install langchain-ibm` · installs (wheel) · licence: MIT · rank 6593 · last release 2026-10-05 · [PyPI](https://pypi.org/project/langchain-ibm/) · [source](https://github.com/langchain-ai/langchain-ibm/tree/main/libs/ibm)

<details><summary>README extract</summary>

This package provides the integration between LangChain and IBM watsonx.ai through the `ibm-watsonx-ai` SDK.

Example:
```python
import os
from getpass import getpass

watsonx_api_key = getpass()
os.environ["WATSONX_API_KEY"] = watsonx_api_key
```

Sections: langchain-ibm, Setting up, Setting parameters, Chat Models, Embedding Models, LLMs, Reranker, Toolkit

</details>

### lime

Local Interpretable Model-Agnostic Explanations for machine learning classifiers

`pip install lime` · installs from source (sdist only) · licence: BSD · rank 6644 · last release 2020-06-26 · [PyPI](https://pypi.org/project/lime/)

### lazr.restfulclient

A programmable client library that takes advantage of the commonalities among lazr.restful web services.

`pip install lazr.restfulclient` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6674 · last release 2026-10-22 · [PyPI](https://pypi.org/project/lazr.restfulclient/) · [docs](https://lazrrestfulclient.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/lazr.restfulclient)

_README extract left out: share-alike licence._

### lazr.uri

A self-contained, easily reusable library for parsing, manipulating, and generating URIs.

`pip install lazr.uri` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6723 · last release 2026-08-01 · [PyPI](https://pypi.org/project/lazr.uri/) · [docs](https://lazruri.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/lazr.uri)

_README extract left out: share-alike licence._

### launchpadlib

Script Launchpad through its web services interfaces. Officially supported.

`pip install launchpadlib` · installs (wheel) · licence: GNU Library or Lesser General Public License (LGPL) · rank 6797 · last release 2026-10-13 · [PyPI](https://pypi.org/project/launchpadlib/) · [docs](https://launchpadlib.readthedocs.io/en/latest/) · [source](https://code.launchpad.net/launchpadlib)

_README extract left out: share-alike licence._

### liquidpy

A port of liquid template engine for python

`pip install liquidpy` · installs (wheel) · licence: MIT · rank 6835 · last release 2026-08-10 · [PyPI](https://pypi.org/project/liquidpy/) · [source](https://github.com/pwwang/liquidpy)

<details><summary>README extract</summary>

A port of liquid template engine for python, on the shoulders of jinja2

[][9] [][10] [][9] [][11] [][11] [][12] [][12]

Example:
```python
from liquid import Liquid
liq = Liquid('{{a}}', from_file=False)
ret = liq.render(a = 1)
# ret == '1'

# load template from a file
liq = Liquid('/path/to/template.html')
```

Sections: Playground, Baisic usage, Loading a template, Switching to a different mode, Changing default options, Documentation

</details>

### labmaze

LabMaze: DeepMind Lab's text maze generator.

`pip install labmaze` · installs from source (sdist only) · licence: Apache 2.0 · rank 6945 · last release 2023-10-04 · [PyPI](https://pypi.org/project/labmaze/)

### llama-index-llms-openai-like

llama-index llms openai like integration

`pip install llama-index-llms-openai-like` · installs (wheel) · licence: MIT · rank 6989 · last release 2026-10-01 · [PyPI](https://pypi.org/project/llama-index-llms-openai-like/)

<details><summary>README extract</summary>

`pip install llama-index-llms-openai-like`

This package is a thin wrapper around the OpenAI API. It is designed to be used with the OpenAI API, but can be used with any OpenAI-compatible API.

Example:
```python
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    model="model-name",
    api_base="
    api_key="fake",
    # Explicitly set the context window to match the model's context window
    context_window=128000,
    # Controls whether the model uses chat or completion endpoint
    is_chat_model=True,
...
```

Sections: LlamaIndex Llms Integration: Openai Like, Usage

</details>

### leptonai

NVIDIA DGX Cloud Lepton AI Platform, SDK and CLI

`pip install leptonai` · installs (wheel) · licence: not stated · rank 7133 · last release 2026-10-20 · [PyPI](https://pypi.org/project/leptonai/)

<details><summary>README extract</summary>

The Python library and `lep` CLI for NVIDIA DGX Cloud Lepton

Homepage •
Examples •
Documentation •
CLI References

The LeptonAI Python library lets you operate the NVIDIA DGX Cloud Lepton platform from Python and the command line. Key features include: ...

Example:
```python
from leptonai.client import Client, local

# Connect to a workspace endpoint...
c = Client("my-workspace", "my-endpoint", token="MY_TOKEN")
# ...or to something running locally:
c = Client(local(port=8080))

# Discover the available paths and their docs
print(c.paths())
print(c.run.doc)

# Call the endpoint as if it were a local function
...
```

Sections: Lepton AI, Getting started, Calling an endpoint from Python, Checking out more examples, Skills: Operating Lepton from Claude Code or Codex

</details>

### ledoc-ui

A bundle of static files for ledoc as a python package.

`pip install ledoc-ui` · installs (wheel) · licence: MIT · rank 7176 · last release 2024-09-02 · [PyPI](https://pypi.org/project/ledoc-ui/)

<details><summary>README extract</summary>

This package only contains static files for ledoc_ui as a bundle.

It is intended to be used as a python package dependency for any webserver that serves UI for `openapi.json`.

As long as the `openapi.json` in standard format is served at `/openapi.json` path, the UI will work out of the box at `/ledoc`.

Example:
```python
from ledoc_ui import ledoc_ui_path
```

Sections: Ledoc_ui, Getting Started

</details>

### logger

Python logging helper

`pip install logger` · installs from source (sdist only) · licence: UNKNOWN · rank 7221 · last release 2013-10-22 · [PyPI](https://pypi.org/project/logger/)

### llama-index-llms-anthropic

llama-index llms anthropic integration

`pip install llama-index-llms-anthropic` · installs (wheel) · licence: MIT · rank 7248 · last release 2026-10-12 · [PyPI](https://pypi.org/project/llama-index-llms-anthropic/)

<details><summary>README extract</summary>

Anthropic is an AI research company focused on developing advanced language models, notably the Claude series. Their flagship model, Claude, is designed to generate human-like text while prioritizing safety and alignment with human intentions. ...

Example:
```python
import os

from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings

os.environ["ANTHROPIC_API_KEY"] = "YOUR ANTHROPIC API KEY"
from llama_index.llms.anthropic import Anthropic

# To customize your API key, do this
# otherwise it will lookup ANTHROPIC_API_KEY from your env variable
...
```

...

</details>

### lambdatest-selenium-driver

Python Selenium SDK for testing with Smart UI

`pip install lambdatest-selenium-driver` · installs (wheel) · licence: MIT License · rank 7316 · last release 2025-12-09 · [PyPI](https://pypi.org/project/lambdatest-selenium-driver/)

<details><summary>README extract</summary>

SmartUI SDK for python selenium
- Installation
- Methods
- Usage

Example:
```python
from lambdatest_selenium_driver import smartui_snapshot
from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get('
    smartui_snapshot(driver,"Snapshotname")
except Exception as err:
    print(err)
finally:
    driver.close()
```

Sections: lambdatest-selenium-driver, Methods, Usage, Reporting bugs, Pull Requests, About LambdaTest

</details>

### libvirt-python

The libvirt virtualization API python binding

`pip install libvirt-python` · installs from source (sdist only) · licence: LGPL-v2.0-or-later · rank 7361 · last release 2026-11-02 · [PyPI](https://pypi.org/project/libvirt-python/)

_README extract left out: share-alike licence._

### listentome

Async-first audio I/O for Python, built on PortAudio.

`pip install listentome` · installs (wheel) · licence: not stated · rank 7403 · last release 2026-08-27 · [PyPI](https://pypi.org/project/listentome/)

<details><summary>README extract</summary>

listentome is an async-first audio I/O library for Python, built on PortAudio.

The key features are:

- Async native: streams are async context managers and async iterators. No callbacks, no queues, no `call_soon_threadsafe`.
- Bytes in, bytes out: audio blocks are plain `bytes`. No NumPy requirement, no raw/array duality. ...

Example:
```python
import anyio

import listentome as ltm

async def main() -> None:
    async with ltm.InputStream(samplerate=48_000, channels=1) as stream:
        async for block in stream:
            print(f"got {len(block)} bytes")

anyio.run(main)
```

Sections: listentome, Requirements, Example, Record, Play, Duplex, Use with Pydantic AI, Devices, Sync facade

</details>

### libraft-cu12

RAFT: Reusable Algorithms Functions and other Tools (C++)

`pip install libraft-cu12` · installs (wheel) · licence: Apache-2.0 · rank 7413 · last release 2026-10-08 · [PyPI](https://pypi.org/project/libraft-cu12/) · [docs](https://docs.rapids.ai/api/raft/stable/)

<details><summary>README extract</summary>

Example:
```python
import cupy as cp

from cuvs.distance import pairwise_distance

n_samples = 5000
n_features = 50

in1 = cp.random.random_sample((n_samples, n_features), dtype=cp.float32)
in2 = cp.random.random_sample((n_samples, n_features), dtype=cp.float32)

output = pairwise_distance(in1, in2, metric="euclidean")
```

Sections: RAFT: Reusable Accelerated Functions and Tools, Useful Resources, What is RAFT?, #, Is RAFT right for me?, Getting started, RAPIDS Memory Manager (RMM), Multi-dimensional Arrays, C++ Example, Python Example, References

</details>

### llama-index-vector-stores-chroma

llama-index vector_stores chroma integration

`pip install llama-index-vector-stores-chroma` · installs (wheel) · licence: MIT · rank 7497 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-chroma/)

### llama-index-vector-stores-azureaisearch

llama-index vector_stores azureaisearch integration

`pip install llama-index-vector-stores-azureaisearch` · installs (wheel) · licence: MIT · rank 7502 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-azureaisearch/)

### langchain-milvus

An integration package connecting Milvus and LangChain

`pip install langchain-milvus` · installs (wheel) · licence: MIT License · rank 7536 · last release 2026-07-17 · [PyPI](https://pypi.org/project/langchain-milvus/) · [source](https://github.com/langchain-ai/langchain-milvus)

<details><summary>README extract</summary>

This repository contains the Milvus integration package for LangChain:

- langchain-milvus - A powerful integration between LangChain and Milvus, enabling vector search and retrievers for AI applications.

Features:
LangChain Milvus provides seamless integration between LangChain, a framework for building applications with large language models (LLMs), and Milvus, a powerful vector database designed for similarity search and AI applications. ...

Sections: 🦜️🔗 LangChain Milvus, Overview, Features, Usage

</details>

### lib-layered-config

Cross-platform layered configuration loader for Python

`pip install lib-layered-config` · installs (wheel) · licence: MIT License · rank 7566 · last release 2026-11-01 · [PyPI](https://pypi.org/project/lib-layered-config/) · [source](https://github.com/bitranox/lib_layered_config.git)

<details><summary>README extract</summary>

<!-- Badges -->

Here is the odd thing about configuration bugs: hardly any of them are about the value. They are about authorship. By the time a setting reaches your program it has passed through as many as six hands - the defaults you shipped, a file in `/etc`, a per-host tweak, something in the user's home directory, a `.env`, and an ...

Features:
- Deterministic layering - precedence is always `defaults → app → host → user → dotenv → env`.
- Immutable value object - returned `Config` prevents accidental mutation and exposes dotted-path helpers. ...

Example:
```python
from lib_layered_config import read_config

config = read_config(vendor="Acme", app="ConfigKit", slug="config-kit")
print(config.get("service.timeout", default=30))
print(config.origin("service.timeout"))
```

...

</details>

### lib-log-rich

Rich-powered logging runtime with contextual metadata, multi-sink fan-out, and ring-buffer dumps

`pip install lib-log-rich` · installs (wheel) · licence: MIT License · rank 7589 · last release 2026-10-29 · [PyPI](https://pypi.org/project/lib-log-rich/) · [source](https://github.com/bitranox/lib_log_rich.git)

<details><summary>README extract</summary>

* Enjoy vibrant Rich-style colored console output with clean formatting.
* Tailor colored (or monochrome) logs with flexible templates and themes, while your OS takes care of persistence.
* Forget about manual logfile rotation.
* Export logs as JSON, HTML or plain text whenever you need. ...

Features:
Rich-powered logging backbone with contextual metadata, multi-target fan-out (console, journald, Windows Event Log, Graylog), ring-buffer dumps, and
queue-based decoupling for multi-threaded workloads. ...

Example:
```python
# entrypoint.py
import lib_log_rich as log

log.init(log.RuntimeConfig(service="billing", environment="prod"))

from billing import payments  # import after init so the runtime exists

payments.PaymentProcessor().charge_order("ord-42")

...

</details>

### lib-cli-exit-tools

CLI exit handling helpers: clean signals, exit codes, and error printing

`pip install lib-cli-exit-tools` · installs (wheel) · licence: MIT License · rank 7607 · last release 2026-10-12 · [PyPI](https://pypi.org/project/lib-cli-exit-tools/) · [source](https://github.com/bitranox/lib_cli_exit_tools.git)

<details><summary>README extract</summary>

<!-- Badges -->

Small helpers for robust CLI exit handling:
- Portable signal handling (SIGINT, SIGTERM/SIGBREAK)
- Consistent exception → exit code mapping
- Concise error printing with optional traceback and subprocess stdout/stderr capture

Features:
Building CLI applications that behave correctly in shell pipelines, CI/CD systems, and across platforms is surprisingly tricky. This library solves five common pain points:

1. ...

Example:
```python
from future import annotations

import rich_click as click

from lib_cli_exit_tools import run_cli

@click.command()
def hello() -> None:
    """Say hello with automatic signal-aware exit handling."""
    click.echo("Hello from lib_cli_exit_tools!")

if name == "main":
    raise SystemExit(run_cli(hello))
```

...

</details>

### lambdapdk

Library of open source Process Design Kits

`pip install lambdapdk` · installs (wheel) · licence: Apache-2.0 · rank 7762 · last release 2026-09-11 · [PyPI](https://pypi.org/project/lambdapdk/)

<details><summary>README extract</summary>

Lambdapdk is a collection of open-source Process Design Kits (PDKs) that enable chip design across multiple technology nodes. Each PDK includes standard cell libraries, I/O libraries, and memory compilers with full integration into the SiliconCompiler build system and Lambdalib Verilog hardware abstraction library. ...

Example:
```python
from siliconcompiler import ASIC, Design
from siliconcompiler.targets import skywater130_demo

# Create design and add source files
design = Design("mydesign")
design.set_topmodule("mydesign", fileset="rtl")
design.add_file("mydesign.v", fileset="rtl")
design.add_file("mydesign.sdc", fileset="sdc")

# Create ASIC project and load target
...
```

...

</details>

### llama-index-vector-stores-qdrant

llama-index vector_stores qdrant integration

`pip install llama-index-vector-stores-qdrant` · installs (wheel) · licence: MIT · rank 7827 · last release 2026-10-08 · [PyPI](https://pypi.org/project/llama-index-vector-stores-qdrant/)

### localstack-snapshot

Extracted snapshot testing lib for LocalStack

`pip install localstack-snapshot` · installs (wheel) · licence: Apache Software License · rank 8065 · last release 2026-11-04 · [PyPI](https://pypi.org/project/localstack-snapshot/)

<details><summary>README extract</summary>

Sections: Quickstart, Configuration options, Format code, Build distribution

</details>

### langchain-weaviate

An integration package connecting Weaviate and LangChain

`pip install langchain-weaviate` · installs (wheel) · licence: MIT License · rank 8126 · last release 2026-07-10 · [PyPI](https://pypi.org/project/langchain-weaviate/) · [source](https://github.com/langchain-ai/langchain-weaviate)

<details><summary>README extract</summary>

This package contains the Weaviate integrations for LangChain.

- Weaviate is an open source, AI-native vector database that helps developers create intuitive and reliable AI-powered applications.
- LangChain is a framework for developing applications powered by language models. ...

Sections: langchain-weaviate, About, Requirements, Usage, Further resources

</details>

### llama-index-llms-bedrock-converse

llama-index llms bedrock converse integration

`pip install llama-index-llms-bedrock-converse` · installs (wheel) · licence: MIT · rank 8261 · last release 2026-10-14 · [PyPI](https://pypi.org/project/llama-index-llms-bedrock-converse/)

<details><summary>README extract</summary>

Example:
```python
from llama_index.llms.bedrock_converse import BedrockConverse

# Set your AWS profile name
profile_name = "Your aws profile name"

# Simple completion call
resp = BedrockConverse(
    model="anthropic.claude-3-haiku-20240307-v1:0",
    profile_name=profile_name,
).complete("Paul Graham is ")
print(resp)
```

Sections: LlamaIndex Llms Integration: Bedrock Converse, Usage, Call chat with a list of messages, Streaming, Configure Model, Connect to Bedrock with Access Keys, Use an Application Inference Profile, Function Calling, Async usage, Prompt Caching System and regular messages, LLM Implementation example

</details>

### linear-tsv

Line-oriented, tab-separated value format

`pip install linear-tsv` · installs from source (sdist only) · licence: Apache Software License · rank 8319 · last release 2018-01-20 · [PyPI](https://pypi.org/project/linear-tsv/)

### lance-namespace-impls

Third-party catalog implementations for Lance Namespace

`pip install lance-namespace-impls` · installs (wheel) · licence: Apache-2.0 · rank 8445 · last release 2026-10-05 · [PyPI](https://pypi.org/project/lance-namespace-impls/)

<details><summary>README extract</summary>

Third-party catalog implementations for Lance Namespace.

</details>

### lbr-trex-client

Lbr-trex-client package contains TRex traffic generator client API as Python package.

`pip install lbr-trex-client` · installs (wheel) · licence: not stated · rank 8473 · last release 2024-02-26 · [PyPI](https://pypi.org/project/lbr-trex-client/) · [source](https://github.com/CESNET/lbr-trex-client)

<details><summary>README extract</summary>

Cisco TRex traffic generator is distributed as a
single .tar.gz archive
and contains all external libraries/packages for running TRex.
This means trying to use or import TRex Client Python API in your code is relatively complicated, especially
if your code runs on different machine than TRex itself. ...

Example:
```python
import lbr_trex_client

from trex.stl.api import *
from trex.astf.api import *
from trex_stl_lib.api import *
from trex_client import CTRexClient
from trex_exceptions import TRexInUseError
from scapy.layers.dns import *
...
```

Sections: Python package lbr-trex-client, Usage, Differences compared to official TRex API, Known issues, Links to official TRex documentation, Custom TRex API

</details>

### llama-models

Llama models

`pip install llama-models` · installs (wheel) · licence: not stated · rank 8587 · last release 2025-11-04 · [PyPI](https://pypi.org/project/llama-models/)

<details><summary>README extract</summary>

🤗 Models on Hugging Face | Blog | Website | Get Started | Llama Cookbook

Llama is an accessible, open large language model (LLM) designed for developers, researchers, and businesses to build, experiment, and responsibly scale their generative AI ideas. Part of a foundational system, it serves as a bedrock for innovation in the global community. ...

Example:
```python
# inference.py
from transformers import AutoTokenizer, Llama4ForConditionalGeneration
import torch

model_id = "meta-llama/Llama-4-Scout-17B-16E-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    {"role": "user", "content": "Who are you?"},
]
inputs = tokenizer.apply_chat_template(
...
```

...

</details>

### livy

A Python client for Apache Livy

`pip install livy` · installs (wheel) · licence: MIT License · rank 8602 · last release 2021-01-27 · [PyPI](https://pypi.org/project/livy/)

<details><summary>README extract</summary>

Livy is an open source REST interface
for interacting with Spark. `pylivy` is a
Python client for Livy, enabling easy remote code execution on a Spark cluster.

Sections: pylivy, Documentation

</details>

### logging-formatter-anticrlf

Python logging Formatter for CRLF Injection (CWE-93 / CWE-117) prevention

`pip install logging-formatter-anticrlf` · installs (wheel) · licence: BSD-2-clause · rank 8679 · last release 2023-09-28 · [PyPI](https://pypi.org/project/logging-formatter-anticrlf/)

<details><summary>README extract</summary>

logging Formatter to sanitize CRLF errors (CWE-93, some forms of CWE-117)

This class is a drop-in replacement for `logging.Formatter`, and has the
exact same construction arguments. However, as a final step of formatting a
log line, it escapes carriage returns (\\r) and linefeeds (\\n). ...

Example:
```python
import sys
import logging
import anticrlf

handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(anticrlf.LogFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger = logging.getLogger(name)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Example text with a newline\nhere")
```

Sections: logging-formatter-anticrlf, Examples, Changing Replacements

</details>

### LucoPy

Python SDK to support the Luco data observability tool.

`pip install LucoPy` · installs (wheel) · licence: MIT License · rank 8689 · last release 2023-09-27 · [PyPI](https://pypi.org/project/LucoPy/)

<details><summary>README extract</summary>

Python SDK to interact with the Luco API.

Contact: support@lu.co

Example:
```python
import LucoPy.data_quality.great_expectations.utils as ge_utils

check = ge_utils.convert_expectation_to_check(expectation)

collection = ge_utils.convert_suite_to_collection(suite)
```

Sections: LucoPy, How to Use, Authentication, Azure Service Principal, Other Identities, LucoApi Class, Submission Class, Data Quality, Fail conditions, Great Expectations

</details>

### llama-index-retrievers-bm25

llama-index retrievers bm25 integration

`pip install llama-index-retrievers-bm25` · installs (wheel) · licence: MIT · rank 8704 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-retrievers-bm25/)

### langchain-oracledb

An integration package connecting Oracle Database and LangChain

`pip install langchain-oracledb` · installs (wheel) · licence: UPL-1.0 · rank 8722 · last release 2026-09-30 · [PyPI](https://pypi.org/project/langchain-oracledb/) · [source](https://github.com/oracle/langchain-oracle)

<details><summary>README extract</summary>

This package contains the LangChain integrations with Oracle AI Vector Search.

> ⭐ If this package is useful to you, consider starring the repository — it helps other developers discover these integrations.

Example:
```python
import os

import oracledb

# Please update with your username, password, hostname, port and service_name
username = os.environ["ORACLE_DB_USERNAME"]
password = os.environ["ORACLE_DB_PASSWORD"]
dsn = os.environ["ORACLE_DB_DSN"]

connection = oracledb.connect(user=username, password=password, dsn=dsn)
print("Connection successful!")
```

...

</details>

### luhn

Generate and verify Luhn check digits

`pip install luhn` · installs from source (sdist only) · licence: MIT · rank 8759 · last release 2015-06-23 · [PyPI](https://pypi.org/project/luhn/)

<details><summary>README extract</summary>

Generate and verify Luhn check digits

Install with

Use `verify` to check digit strings

and use `generate` to produce them

or `append` for convenience

Example:
```python
>>> from luhn import *
>>> verify('356938035643809')
True
>>> verify('534618613411236')
False
```

</details>

### langchain-unstructured

An integration package connecting Unstructured and LangChain

`pip install langchain-unstructured` · installs (wheel) · licence: MIT License · rank 8771 · last release 2025-12-27 · [PyPI](https://pypi.org/project/langchain-unstructured/) · [source](https://github.com/langchain-ai/langchain-unstructured)

<details><summary>README extract</summary>

This package contains the LangChain integration with Unstructured

Example:
```python
from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader(
    file_path = ["example.pdf", "fake.pdf"],
    api_key=UNSTRUCTURED_API_KEY,
    partition_via_api=True,
    chunking_strategy="by_title",
    strategy="fast",
)
```

Sections: langchain-unstructured, Loaders

</details>

### LnkParse3

Windows Shortcut file (LNK) parser

`pip install LnkParse3` · installs (wheel) · licence: MIT License · rank 8773 · last release 2026-02-27 · [PyPI](https://pypi.org/project/LnkParse3/)

<details><summary>README extract</summary>

Windows Shortcut file (LNK) parser

LnkParse3 is a minimalistic python package for forensics of a binary file with LNK extension aka Microsoft Shell Link aka Windows shortcut. It is aimed to dig up as much data as possible and to process even malformed files. It is not able to create or modify files.

Features:
- easy to use
- CLI tool & package
- JSON output

Example:
```python
>>> import LnkParse3
>>> with open('tests/samples/microsoft_example', 'rb') as indata:
>>>     lnk = LnkParse3.lnk_file(indata)
>>>     lnk.print_json()
{
    "data": {
        "relative_path": ".\\a.txt",
        "working_directory": "C:\\test"
    },
    "extra": {
        "DISTRIBUTED_LINK_TRACKER_BLOCK": {
...
```

...

</details>

### linopy

Linear optimization with N-D labeled arrays in Python

`pip install linopy` · installs (wheel) · licence: MIT License · rank 8886 · last release 2026-10-21 · [PyPI](https://pypi.org/project/linopy/) · [source](https://github.com/PyPSA/linopy)

<details><summary>README extract</summary>

&nbsp; &nbsp; &nbsp; &nbsp; Linear\
&nbsp; &nbsp; &nbsp; &nbsp; Integer\
&nbsp; &nbsp; &nbsp; &nbsp; Non-linear\
&nbsp; &nbsp; &nbsp; &nbsp; Optimization in\
&nbsp; &nbsp; &nbsp; &nbsp; PYthon

linopy is an open-source python package that facilitates optimization with real world data. ...

Example:
```python
>>> import pandas as pd
>>> import linopy

>>> m = linopy.Model()

>>> days = pd.Index(["Mon", "Tue", "Wed", "Thu", "Fri"], name="day")
>>> apples = m.add_variables(lower=0, name="apples", coords=[days])
>>> bananas = m.add_variables(lower=0, name="bananas", coords=[days])
>>> apples
```

Sections: Benchmarks, Main features, In a Nutshell, Citing Linopy

</details>

### langsmith-mcp-server

MCP server for Langsmith SDK integration

`pip install langsmith-mcp-server` · installs (wheel) · licence: MIT · rank 8890 · last release 2026-02-25 · [PyPI](https://pypi.org/project/langsmith-mcp-server/)

<details><summary>README extract</summary>

A production-ready Model Context Protocol (MCP) server that provides seamless integration with the LangSmith observability platform. This server enables language models to fetch conversation history, prompts, runs and traces, datasets, experiments, and billing usage from LangSmith.

Sections: 🦜🛠️ LangSmith MCP Server, 📋 Example Use Cases, 🚀 Quickstart, 🛠️ Available Tools, 💬 Conversation & Threads, 📚 Prompt Management, 🔍 Traces & Runs, 📊 Datasets & Examples, 🧪 Experiments & Evaluations, 📈 Usage & Billing, 📄 Pagination (char-based), 📝 General Prerequisites, 🔌 MCP Client Integration, 📦 From PyPI

</details>

### libbs

Deprecated: 'libbs' has been renamed to 'declib'. Install 'declib' instead.

`pip install libbs` · installs (wheel) · licence: BSD License · rank 8946 · last release 2026-06-03 · [PyPI](https://pypi.org/project/libbs/)

<details><summary>README extract</summary>

> `libbs` has been renamed to `declib`.
> This package is now a deprecation shim. Installing it will pull in `declib`
> and emit a `DeprecationWarning` on import. No further updates will be made
> to `libbs`.

Replace `libbs` with `declib` in your imports:

All sources, docs, examples, and tests now live in the `declib` repository.

Example:
```python
# Before
from libbs.api import DecompilerInterface

# After
from declib.api import DecompilerInterface
```

Sections: libbs (deprecated), Migrate

</details>

### libsql

(no summary)

`pip install libsql` · installs (wheel) · licence: not stated · rank 8982 · last release 2025-09-02 · [PyPI](https://pypi.org/project/libsql/)

### libuuu

A python wraper for libuuu.

`pip install libuuu` · installs (wheel) · licence: BSD License · rank 9027 · last release 2025-12-16 · [PyPI](https://pypi.org/project/libuuu/)

<details><summary>README extract</summary>

A python wrapper for `libuuu`.

Supported Python versions: 3.9 or newer.

Sections: libuuu, Building libraries, Linux & MacOS, Windows, Building python package

</details>

### llama-index-embeddings-huggingface

llama-index embeddings huggingface integration

`pip install llama-index-embeddings-huggingface` · installs (wheel) · licence: MIT · rank 9075 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-huggingface/)

### langchain-astradb

An integration package connecting Astra DB and LangChain

`pip install langchain-astradb` · installs (wheel) · licence: MIT · rank 9105 · last release 2025-10-23 · [PyPI](https://pypi.org/project/langchain-astradb/) · [source](https://github.com/langchain-ai/langchain-datastax/tree/main/libs/astradb)

<details><summary>README extract</summary>

This package contains the LangChain integrations for using DataStax Astra DB.

> DataStax Astra DB is a serverless vector-capable database built on Apache Cassandra® and made conveniently available
> through an easy-to-use JSON API.

> [!IMPORTANT]
> This package replaces the _deprecated_ Astra DB classes found under `langchain_community.*`. ...

Example:
```python
from langchain_astradb import AstraDBVectorStore

my_store = AstraDBVectorStore(
  embedding=my_embedding,
  collection_name="my_store",
  api_endpoint="
  token="AstraCS:...",
)
```

Sections: langchain-astradb, Architecture sketch, Integrations overview, Vector Store, LLM Cache, Semantic LLM Cache, Document loader, Store, Byte Store, Collection defaults mismatch, The case of hybrid search, Warnings about indexing, Remediation

</details>

### llama-index-embeddings-ollama

llama-index embeddings ollama integration

`pip install llama-index-embeddings-ollama` · installs (wheel) · licence: MIT · rank 9110 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-ollama/)

<details><summary>README extract</summary>

The `llama-index-embeddings-ollama` package contains LlamaIndex integrations for generating embeddings using Ollama, a tool for running large language models locally.

Ollama allows you to run embedding models on your local machine, providing privacy, cost savings, and the ability to work offline. ...

Example:
```python
import asyncio
from llama_index.embeddings.ollama import OllamaEmbedding

embed_model = OllamaEmbedding(model_name="nomic-embed-text")

async def main():
    # Async single embedding
    embedding = await embed_model.aget_text_embedding("Hello, world!")

    # Async batch embeddings
    embeddings = await embed_model.aget_text_embeddings(
...
```

...

</details>

### llama-index-llms-ollama

llama-index llms ollama integration

`pip install llama-index-llms-ollama` · installs (wheel) · licence: MIT · rank 9196 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-llms-ollama/)

<details><summary>README extract</summary>

Example:
```python
from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3.1:latest", request_timeout=120.0)
```

Sections: LlamaIndex Llms Integration: Ollama, Setup, Usage, Initialize Ollama, Generate Completions, Chat Responses, Streaming Responses, Stream Complete, Stream Chat, JSON Mode, Structured Outputs, Asynchronous Chat, LLM Implementation example

</details>

### llama-index-embeddings-databricks

llama-index embeddings databricks integration

`pip install llama-index-embeddings-databricks` · installs (wheel) · licence: MIT · rank 9251 · last release 2026-08-29 · [PyPI](https://pypi.org/project/llama-index-embeddings-databricks/)

<details><summary>README extract</summary>

This integration adds support for embedding models hosted on the databricks platform via serving endpoints. The API follows the specifications of OpenAI, so this integration simply adapts the `llama-index-embeddings-openai` integration and internally uses the `openai` Python API library, too. ...

Example:
```python
import os
from llama_index.core import Settings
from llama_index.embeddings.databricks import DatabricksEmbedding

# Set up the DatabricksEmbedding class with the required model, API key and serving endpoint
embed_model = DatabricksEmbedding(
    model="databricks-bge-large-en",
    api_key="<MY TOKEN>",
    endpoint="<MY ENDPOINT>",
)
...
```

Sections: LlamaIndex Embeddings Integration: Databricks, Usage

</details>

### ldfparser

LDF Language support for Python

`pip install ldfparser` · installs (wheel) · licence: MIT License · rank 9302 · last release 2025-01-27 · [PyPI](https://pypi.org/project/ldfparser/) · [docs](https://c4deszes.github.io/ldfparser/) · [source](https://github.com/c4deszes/ldfparser)

<details><summary>README extract</summary>

> This tool is able parse LIN Description Files, retrieve signal names and frames from them, as well as encoding messages using frame definitions and decoding them.

The library is still in a pre-release state, therefore features may break between minor versions. ...

Features:
+ Semantic validation of LDF files

+ Retrieve header information (version, baudrate)

+ Retrieve Signal and Frame information

+ Retrieve Signal encoding types and use them to convert values

+ Retrieve Node attributes ...

Example:
```python
import ldfparser
import binascii

# Load LDF
ldf = ldfparser.parse_ldf(path = "network.ldf")
frame = ldf.get_unconditional_frame('Frame_1')

# Get baudrate from LDF
print(ldf.get_baudrate())

# Encode signal values into frame
...

</details>

### langchainplus-sdk

Client library to connect to the LangSmith LLM Tracing and Evaluation Platform.

`pip install langchainplus-sdk` · installs (wheel) · licence: MIT License · rank 9422 · last release 2023-07-03 · [PyPI](https://pypi.org/project/langchainplus-sdk/)

<details><summary>README extract</summary>

This package contains the Python client for interacting with the LangSmith platform.

To install:

LangSmith helps you and your team develop and evaluate language models and intelligent agents. ...

Example:
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = " # or your own server
os.environ["LANGCHAIN_API_KEY"] = "<YOUR-LANGCHAINPLUS-API-KEY>"
# os.environ["LANGCHAIN_PROJECT"] = "My Project Name" # Optional: "default" is used if not set
```

Sections: LangSmith Client SDK, 1. Connect to LangSmith, 2. Log Traces, Logging Traces with LangChain, Logging Traces Outside LangChain, Create a Dataset from Existing Runs, Evaluating Runs, Additional Documentation

</details>

### lorem-text

Dummy lorem ipsum text generator

`pip install lorem-text` · installs (wheel) · licence: MIT License · rank 9646 · last release 2025-05-10 · [PyPI](https://pypi.org/project/lorem-text/)

<details><summary>README extract</summary>

Dummy lorem ipsum text generator

* Free software: MIT license

Features:
Dummy lorem ipsum text generator for Python.

* Generate dummy senetnce, paragraphs and words.
* Command line interface tool included.

Example:
```python
from lorem_text import lorem
```

Sections: Lorem Text, Features, Usage, Command Line Interface

</details>

### logging-journald

Pure python logging handler for writing logs to the journald using native protocol

`pip install logging-journald` · installs (wheel) · licence: MIT · rank 9664 · last release 2026-07-30 · [PyPI](https://pypi.org/project/logging-journald/) · [source](https://github.com/mosquito/logging-journald)

<details><summary>README extract</summary>

Pure python logging handler for writing logs to the journald using
native protocol.

`MESSAGE_ID` field

As defined in catalog documentation:

> A `128-bit` message identifier ID for recognizing certain message types, if this is desirable. ...

Example:
```python
import logging
from logging_journald import JournaldLogHandler, check_journal_stream

# Use python default handler
LOG_HANDLERS = None

if (
    # Check if program running as systemd service
    check_journal_stream() or
    # Check if journald socket is available
    JournaldLogHandler.SOCKET_PATH.exists()
):
...
```

</details>

### loki-logger-handler

Handler designed for transmitting logs to Grafana Loki in JSON format.

`pip install loki-logger-handler` · installs (wheel) · licence: MIT License · rank 9714 · last release 2025-05-26 · [PyPI](https://pypi.org/project/loki-logger-handler/)

<details><summary>README extract</summary>

A logging handler that sends log messages to (Grafana) Loki in JSON format.

Features:
* Logs pushed in JSON format by default
* Custom labels definition
* Allows defining *loguru* and *logger* extra keys as labels
* Logger extra keys added automatically as keys into pushed JSON
* Publish in batch of Streams
* Publish logs compressed

Example:
```python
from loki_logger_handler.loki_logger_handler import LokiLoggerHandler
import logging
import os

# Set up logging
logger = logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)

# Create an instance of the custom handler with structured metadata
custom_handler = LokiLoggerHandler(
  url=os.environ["LOKI_URL"],
...
```

...

</details>

### lusid-sdk

LUSID API

`pip install lusid-sdk` · installs (wheel) · licence: MIT License · rank 9738 · last release 2026-11-08 · [PyPI](https://pypi.org/project/lusid-sdk/) · [source](https://github.com/finbourne/lusid-sdk-python)

<details><summary>README extract</summary>

All URIs are relative to *

Class | Method | HTTP request | Description

*AborApi* | add_diary_entry | POST /api/abor/{scope}/{code}/accountingdiary | [EARLY ACCESS] AddDiaryEntry: Add a diary entry to the specified Abor. This would be type 'Other'. ...

Sections: Documentation for API Endpoints, Documentation for Models

</details>

### langchain-neo4j

An integration package connecting Neo4j and LangChain

`pip install langchain-neo4j` · installs (wheel) · licence: MIT · rank 9774 · last release 2026-10-09 · [PyPI](https://pypi.org/project/langchain-neo4j/) · [source](https://github.com/langchain-ai/langchain-neo4j)

<details><summary>README extract</summary>

This package contains the LangChain integration with Neo4j.

Example:
```python
from langchain_neo4j import Neo4jGraph

graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")
graph.query("MATCH (n) RETURN n LIMIT 1;")
```

Sections: 🦜️🔗 LangChain Neo4j, 💻 Examples, Neo4jGraph, Neo4jVector, GraphCypherQAChain, Neo4jSaver, AsyncNeo4jSaver, LLMGraphTransformer, 🧪 Tests, Unit Tests, Integration Tests, 🧹 Code Formatting and Linting

</details>

### libscca-python

Python bindings for libscca

`pip install libscca-python` · installs (wheel) · licence: LGPL-3.0-or-later · rank 9791 · last release 2026-05-27 · [PyPI](https://pypi.org/project/libscca-python/) · [docs](https://github.com/libyal/libscca/wiki/Home) · [source](https://github.com/libyal/libscca)

_README extract left out: share-alike licence._

### llama-index-llms-google-genai

llama-index llms google genai integration

`pip install llama-index-llms-google-genai` · installs (wheel) · licence: MIT · rank 9809 · last release 2026-10-14 · [PyPI](https://pypi.org/project/llama-index-llms-google-genai/)

<details><summary>README extract</summary>

Example:
```python
from llama_index.llms.google_genai import GoogleGenAI

llm = GoogleGenAI(model="gemini-3-flash-preview")
resp = llm.complete("Write a short, but joyous, ode to LlamaIndex")
print(resp)
```

Sections: LlamaIndex Llms Integration: Google GenAI, Usage, Basic Content Generation, Chat with Messages, Streaming Responses, Specific Model Usage, Asynchronous API

</details>

### ldpc

LDPC: Python Tools for Low Density Parity Check Codes

`pip install ldpc` · installs (wheel) · licence: not stated · rank 9861 · last release 2025-12-08 · [PyPI](https://pypi.org/project/ldpc/) · [docs](https://software.roffe.eu/ldpc)

<details><summary>README extract</summary>

LDPC Version 2: A C++ rewrite of the `LDPCv1` package for decoding low density parity check checks.
Warning, whilst efforts have been made to provide backwards compatability with LDPCv1, the new version may introduce breaking changes.

The documentation for `LDPCv2` can be found here

Example:
```python
import numpy as np
import ldpc.codes
from ldpc.bplsd_decoder import BpLsdDecoder

H = ldpc.codes.hamming_code(5)

# The
bp_osd = BpLsdDecoder(
            H,
            error_rate = 0.1,
            bp_method = 'product_sum',
            max_iter = 2,
            schedule = 'serial',
            lsd_method = 'lsd_cs',
            lsd_order = 0
...
```

Sections: LDPC: Software for Decoding Classical and Quantum Codes, Documentation, New features, ToDos, BP+LSD Quickstart, Attribution

</details>

### listcrunch

A simple human-readable way to compress redundant sequential data

`pip install listcrunch` · installs (wheel) · licence: MIT License · rank 9890 · last release 2020-06-15 · [PyPI](https://pypi.org/project/listcrunch/)

<details><summary>README extract</summary>

A simple human-readable way to compress redundant sequential data.

Example:
```python
from listcrunch import crunch

compressed_string = crunch([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
# Returns '1:0-8;2:9', meaning 1 appears in indices 0-8 (inclusive),
# and 2 occurs at index 9.
```

Sections: ListCrunch, Example

</details>

### localstack-twisted

An asynchronous networking framework written in Python

`pip install localstack-twisted` · installs (wheel) · licence: MIT License · rank 9909 · last release 2026-11-05 · [PyPI](https://pypi.org/project/localstack-twisted/) · [docs](https://docs.twistedmatrix.com/) · [source](https://github.com/twisted/twisted)

<details><summary>README extract</summary>

This package re-distributes the unmodified twisted code for use in LocalStack, excluding the tests and a few modules not needed by LocalStack in order to reduce the size.

Clone the repository with submodules

 git clone --recurse-submodules git@github.com:localstack/twisted-distribution

Sections: LocalStack Distribution of Twisted, Build project, Clone, Build, Upgrade to latest tagged version, Publish to pypi

</details>

### localstack-py-avro-schema

Generate Apache Avro schemas for Python types including standard library data-classes and Pydantic data models.

`pip install localstack-py-avro-schema` · installs (wheel) · licence: Apache Software License · rank 10023 · last release 2026-04-23 · [PyPI](https://pypi.org/project/localstack-py-avro-schema/) · [docs](https://py-avro-schema.readthedocs.io) · [source](https://github.com/localstack/py-avro-schema)

<details><summary>README extract</summary>

Generate Apache Avro schemas for Python types including standard library data-classes and Pydantic data models.

:blue_book: Documentation:

Sections: py-avro-schema, Terms & Conditions

</details>

### lbt-dragonfly

Collection of all Dragonfly core Python libraries

`pip install lbt-dragonfly` · installs (wheel) · licence: AGPL-3.0 · rank 10028 · last release 2026-11-06 · [PyPI](https://pypi.org/project/lbt-dragonfly/)

_README extract left out: share-alike licence._

### logic2-automation

Library for using the Saleae Logic 2 Automation API

`pip install logic2-automation` · installs (wheel) · licence: not stated · rank 10074 · last release 2025-11-18 · [PyPI](https://pypi.org/project/logic2-automation/)

<details><summary>README extract</summary>

`logic2-automation` implements a Python client for the Logic 2 Automation API.

Documentation can be found at

Sections: Saleae Logic 2 Automation, 1.0.11, 1.0rc11, 1.0.8, 1.0.7, 1.0.6, 1.0.5, 1.0.4, 1.0.3, 1.0.2, 1.0.1, 1.0.0

</details>

### libfwsi-python

Python bindings for libfwsi

`pip install libfwsi-python` · installs (wheel) · licence: LGPL-3.0-or-later · rank 10097 · last release 2026-05-22 · [PyPI](https://pypi.org/project/libfwsi-python/) · [docs](https://github.com/libyal/libfwsi/wiki/Home) · [source](https://github.com/libyal/libfwsi)

_README extract left out: share-alike licence._

### langchain-cerebras

An integration package connecting Cerebras and LangChain

`pip install langchain-cerebras` · does not install on CPython 3.14 · licence: MIT License · rank 10109 · last release 2025-11-24 · [PyPI](https://pypi.org/project/langchain-cerebras/) · [source](https://github.com/langchain-ai/langchain-cerebras)

<details><summary>README extract</summary>

This package contains the LangChain integration with Cerebras.

At Cerebras, we've developed the world's largest and fastest AI processor, the Wafer-Scale Engine-3 (WSE-3). The Cerebras CS-3 system, powered by the WSE-3, represents a new class of AI supercomputer that sets the standard for generative AI training and inference with unparalleled ...

Example:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_cerebras import ChatCerebras

chat = ChatCerebras(
    model="llama-3.3-70b",
)

system = "You are an expert on animals who must answer questions in a manner that a 5 year old can understand."
human = "I want to learn more about this animal: {text}"
...
```

...

</details>

### langchain-elasticsearch

An integration package connecting Elasticsearch and LangChain

`pip install langchain-elasticsearch` · installs (wheel) · licence: MIT License · rank 10113 · last release 2025-12-16 · [PyPI](https://pypi.org/project/langchain-elasticsearch/) · [source](https://github.com/langchain-ai/langchain-elastic)

<details><summary>README extract</summary>

This package contains the LangChain integration with Elasticsearch.

Example:
```python
from langchain_elasticsearch import ElasticsearchStore

embeddings = ... # use a LangChain Embeddings class or ElasticsearchEmbeddings

vectorstore = ElasticsearchStore(
    es_cloud_id="your-cloud-id",
    es_api_key="your-api-key",
    index_name="your-index-name",
    embeddings=embeddings,
)
```

Sections: langchain-elasticsearch, Elasticsearch setup, Elastic Cloud, Usage, ElasticsearchStore, ElasticsearchRetriever, ElasticsearchEmbeddings, ElasticsearchCache, Index the generated text, ElasticsearchEmbeddingsCache

</details>

### llama-index-llms-langchain

llama-index llms langchain integration

`pip install llama-index-llms-langchain` · installs (wheel) · licence: MIT · rank 10120 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-llms-langchain/)

<details><summary>README extract</summary>

Example:
```python
from langchain.llms import OpenAI
from llama_index.llms.langchain import LangChainLLM
```

Sections: LlamaIndex Llms Integration: Langchain, Usage, Import Required Libraries, Initialize LangChain LLM, Generate Streaming Response, LLM Implementation example

</details>

### llm-github-models

LLM plugin to access GitHub Models API

`pip install llm-github-models` · installs (wheel) · licence: Apache Software License · rank 10130 · last release 2025-08-13 · [PyPI](https://pypi.org/project/llm-github-models/)

<details><summary>README extract</summary>

This is a plugin for llm that uses GitHub Models via the Azure AI Inference SDK. GitHub Models is available to all GitHub users and offers free usage of many AI LLMs.

Features:
- Support for all >30 models, including GPT-4o, 4.1, o3, DeepSeek-R1, Llama3.x and more
- Support for schemas
- Output token usage
- Support for Embedding Models
- Async and streaming outputs (model dependent)
- Support for model attachments ...

Sections: GitHub Models Plugin for LLM, Features, Usage, Example, Usage in GitHub Actions, Image attachments, Chat Models, AI21 Jamba 1.5 Large, AI21 Jamba 1.5 Mini, Codestral 25.01, Cohere Command R, Cohere Command R 08-2024, Cohere Command R+, Cohere Command R+ 08-2024

</details>

### lycoris-lora

Lora beYond Conventional methods, Other Rank adaptation Implementations for Stable diffusion

`pip install lycoris-lora` · installs (wheel) · licence: Apache-2.0 · rank 10175 · last release 2026-10-19 · [PyPI](https://pypi.org/project/lycoris-lora/)

<details><summary>README extract</summary>

A project that implements different parameter-efficient fine-tuning algorithms for Stable Diffusion.

This project originated from LoCon (see archive branch).

If you are interested in discussing more details, you can join our Discord server ...

Example:
```python
from lycoris import create_lycoris, LycorisNetwork

LycorisNetwork.apply_preset(
    {"target_name": [".*attn.*"]}
)
lycoris_net = create_lycoris(
    your_model,
    1.0,
    linear_dim=16,
    linear_alpha=2.0,
    algo="lokr"
)
lycoris_net.apply_to()

# after apply_to(), your_model() will run with LyCORIS net
...
```

...

</details>

### langgraph-swarm

An implementation of a multi-agent swarm using LangGraph

`pip install langgraph-swarm` · installs (wheel) · licence: MIT · rank 10187 · last release 2025-12-04 · [PyPI](https://pypi.org/project/langgraph-swarm/)

<details><summary>README extract</summary>

A Python library for creating swarm-style multi-agent systems using LangGraph. A swarm is a type of multi-agent architecture where agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent.

Features:
- 🤖 Multi-agent collaboration - Enable specialized agents to work together and hand off context to each other
- 🛠️ Customizable handoff tools - Built-in tools for communication between agents ...

Example:
```python
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool, create_swarm

...

</details>

### local-operator

A team of proactive AI assistants that can work together behind the scenes to help you get mundane tasks done so you can focus on the fun stuff.

`pip install local-operator` · installs (wheel) · licence: MIT License · rank 10334 · last release 2026-11-08 · [PyPI](https://pypi.org/project/local-operator/)

<details><summary>README extract</summary>

Roles, teams, and cross-agent messaging on top of a fast terminal UI, using every AI subscription you already pay for

A manager session with three workers running in the background (each with its own role, budget, and progress) while the shared plan updates. ...

Sections: Local Operator, ✨ Why Local Operator, 🚀 Quickstart, 🪟 Desktop App (local-operator-ui), 🏢 Agent Organizations, 🔁 Cross-Agent Communication, 🛰️ Agent Mesh (your own devices), 🌙 Always On, 💳 Subscriptions, 🧮 Built for Token and Cache Efficiency, 🖥️ A Tour of the Terminal UI (TUI), Slash commands, Keys worth knowing, 🔌 Providers

</details>

### llama-index-utils-workflow

llama-index utils for workflows

`pip install llama-index-utils-workflow` · installs (wheel) · licence: not stated · rank 10357 · last release 2026-06-17 · [PyPI](https://pypi.org/project/llama-index-utils-workflow/)

<details><summary>README extract</summary>

Utilities for LlamaIndex workflows, including visualization tools.

Features:
- Workflow visualization with `draw_all_possible_flows()`
- Latest execution visualization with `draw_most_recent_execution()`
- Label truncation support for better readability with long event names

Example:
```python
from llama_index.utils.workflow import draw_all_possible_flows

# Basic workflow visualization
draw_all_possible_flows(my_workflow, "workflow.html")

# With label truncation for long event names (v0.4.0+)
draw_all_possible_flows(my_workflow, "workflow.html", max_label_length=15)

# Latest execution visualization
handler = my_workflow.run()
...
```

Sections: LlamaIndex Utils: Workflow, Features, Usage

</details>

### langchain-voyageai

An integration package connecting VoyageAI and LangChain

`pip install langchain-voyageai` · installs (wheel) · licence: MIT · rank 10382 · last release 2026-08-14 · [PyPI](https://pypi.org/project/langchain-voyageai/) · [source](https://github.com/langchain-ai/langchain/tree/master/libs/partners/voyageai)

<details><summary>README extract</summary>

This package contains the LangChain integrations for VoyageAI through their `voyageai` client package.

Example:
```python
from langchain_voyageai import VoyageAIEmbeddings
```

Sections: langchain-voyageai, Text Embedding Model, Voyage-4 Family Models, Code Embeddings, Contextualized Chunk Embeddings, Custom API Endpoint

</details>

### llama-index-embeddings-openai-like

llama-index embeddings openai integration

`pip install llama-index-embeddings-openai-like` · installs (wheel) · licence: MIT · rank 10386 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-openai-like/)

<details><summary>README extract</summary>

This integration allows you to use OpenAI-like embeddings APIs with LlamaIndex.

Example:
```python
from llama_index.embeddings.openai_like import OpenAILikeEmbedding

embedding = OpenAILikeEmbedding(
    model_name="my-model-name",
    api_key="fake",
    api_base="
    embed_batch_size=10,
)
```

Sections: OpenAILike Embeddings, Usage

</details>

### langchain-cli

CLI for interacting with LangChain

`pip install langchain-cli` · installs (wheel) · licence: MIT · rank 10423 · last release 2025-08-30 · [PyPI](https://pypi.org/project/langchain-cli/) · [source](https://github.com/langchain-ai/langchain/tree/master/libs/cli)

<details><summary>README extract</summary>

This package implements the official CLI for LangChain. Right now, it is most useful
for getting started with LangChain Templates!

CLI Docs

</details>

### lambdatest-sdk-utils

SDK utils

`pip install lambdatest-sdk-utils` · installs (wheel) · licence: MIT License · rank 10450 · last release 2025-11-26 · [PyPI](https://pypi.org/project/lambdatest-sdk-utils/)

### linkml-renderer

linkml-renderer

`pip install linkml-renderer` · installs (wheel) · licence: Other/Proprietary License · rank 10466 · last release 2024-06-26 · [PyPI](https://pypi.org/project/linkml-renderer/)

<details><summary>README extract</summary>

Generating HTML, Markdown, Mermaid, and other rendering artefacts from LinkML data.

This applies a configurable *generic* mapping between instance data and the target output file.
This is an example of a "no code" approach to generating visual representations of data.

In general, writing custom code (e.g. ...

Sections: linkml-renderer, Command Line Usage, Python Usage, Output types, How it works, Limitations and Future plans

</details>

### loess

LOESS: smoothing via robust locally-weighted regression in one or two dimensions

`pip install loess` · installs (wheel) · licence: Other/Proprietary License · rank 10548 · last release 2026-07-10 · [PyPI](https://pypi.org/project/loess/)

<details><summary>README extract</summary>

Smoothing via robust locally-weighted regression in one or two dimensions

LOESS is the Python implementation by Cappellari et al. (2013) of the
algorithm by Cleveland (1979)
for the one-dimensional case and Cleveland & Devlin (1988) for the two-dimensional case. ...

Example:
```python
xout, yout, wout = loess_1d(x, y, xnew=None, degree=1, frac=0.5,
                            npoints=None, rotate=False, sigy=None)
```

Sections: The LOESS Package, Attribution, Documentation, loess_1d, Purpose, Calling Sequence, Parameters, Other parameters, Returns, loess_2d, Other Parameters

</details>

### littleutils

Small personal collection of python utility functions

`pip install littleutils` · installs (wheel) · licence: MIT License · rank 10556 · last release 2024-07-07 · [PyPI](https://pypi.org/project/littleutils/)

### learnosity-sdk

Learnosity SDK for Python

`pip install learnosity-sdk` · installs (wheel) · licence: Apache 2.0 license. See LICENSE.md for details. · rank 10580 · last release 2026-01-14 · [PyPI](https://pypi.org/project/learnosity-sdk/)

<details><summary>README extract</summary>

Everything you need to start building your app in Learnosity, with the Python programming language.

(Prefer another language? Click here)

An official Learnosity open-source project.

Features:
The Learnosity Python SDK makes it simple to interact with Learnosity APIs.

It provides a number of convenience features for developers, that make it simple to do the following essential tasks:
* Creating signed security requests for API ...

Example:
```python
from learnosity_sdk.request import Init # Learnosity helper.
from learnosity_sdk.utils import Uuid   # Learnosity helper.
from .. import config          # config.py, which stores the consumer key and secret.
```

...

</details>

### langwatch-scenario

The end-to-end agent testing library

`pip install langwatch-scenario` · installs (wheel) · licence: Apache Software License · rank 10588 · last release 2026-11-02 · [PyPI](https://pypi.org/project/langwatch-scenario/)

<details><summary>README extract</summary>

Scenario is an Agent Testing Framework based on simulations, it can:

- Test real agent behavior by simulating users in different scenarios and edge cases
- Evaluate and judge at any point of the conversation, powerful multi-turn control
- Combine it with any LLM eval framework or custom evals, agnostic by design ...

Example:
```python
# Define any custom assertions
def check_for_weather_tool_call(state: scenario.ScenarioState):
    assert state.has_tool_call("get_current_weather")

result = await scenario.run(
    name="checking the weather",

    # Define the prompt to guide the simulation
    description="""
        The user is planning a boat trip from Barcelona to Rome,
...
```

...

</details>

### lunary

Python SDK for Lunary, the open-source platform where GenAI teams manage and improve LLM chatbots.

`pip install lunary` · installs (wheel) · licence: not stated · rank 10609 · last release 2026-11-05 · [PyPI](https://pypi.org/project/lunary/) · [docs](https://lunary.ai/docs/py) · [source](https://github.com/lunary-ai/lunary/tree/main/packages/python-sdk)

<details><summary>README extract</summary>

📈 Python monitoring for AI apps and agent

website - docs -

Use it with any LLM model and custom agents (not limited to OpenAI).

To get started, get a project ID by registering here.

Example:
```python
from anthropic import Anthropic
import lunary

client = Anthropic()
lunary.monitor(client)

parsed = client.messages.parse(
    model="claude-sonnet-4-5-20250929",
    max_tokens=256,
    messages=[{"role": "user", "content": "Return JSON with an answer field for 2 + 2."}],
    output_format=dict,
)

with client.messages.stream(
...
```

Sections: Lunary Python SDK, 🤖 Anthropic Integration, Diagnosing event delivery errors, 📖 Documentation

</details>

### llama-index-storage-kvstore-postgres

llama-index kvstore postgres integration

`pip install llama-index-storage-kvstore-postgres` · installs (wheel) · licence: MIT · rank 10624 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-storage-kvstore-postgres/)

### laszip

Bindings for LASzip made with pybind11

`pip install laszip` · installs (wheel) · licence: not stated · rank 10627 · last release 2025-12-31 · [PyPI](https://pypi.org/project/laszip/) · [source](https://github.com/tmontaigu/laszip-python)

<details><summary>README extract</summary>

Unofficial bindings between Python and LASzip made
using pybind11.

The main purpose is for integration within laspy.

Building can be done using cmake or pip.

First `pybind11` needs to be installed. You can install it via `vcpkg` or `conda` or other means. ...

Sections: laszip-python, Building, Source distribution

</details>

### llama-index-storage-docstore-postgres

llama-index docstore postgres integration

`pip install llama-index-storage-docstore-postgres` · installs (wheel) · licence: MIT · rank 10671 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-storage-docstore-postgres/)

### launchable

Launchable CLI

`pip install launchable` · installs (wheel) · licence: Apache Software License · rank 10732 · last release 2026-10-28 · [PyPI](https://pypi.org/project/launchable/)

<details><summary>README extract</summary>

Sections: Usage, Preparation, Run tests cli, Run tests exe_deploy.jar, Add dependency, How to update launchable/jar/exe_deploy.jar, Prerequisite, Versioning

</details>

### libsql-client

Python SDK for libSQL

`pip install libsql-client` · installs (wheel) · licence: MIT License · rank 10767 · last release 2024-05-03 · [PyPI](https://pypi.org/project/libsql-client/) · [docs](https://libsql.org/libsql-client-py/) · [source](https://github.com/libsql/libsql-client-py)

<details><summary>README extract</summary>

API reference | Github | PyPI

This is the source repository of the Python SDK for libSQL. You can either connect to a local SQLite database or to a remote libSQL server (sqld).

> _NOTE:_ If you want to use libSQL with SQLAlchemy, you should check out the libSQL dialect.

Example:
```python
import asyncio
import libsql_client

async def main():
    url = "file:local.db"
    async with libsql_client.create_client(url) as client:
        result_set = await client.execute("SELECT * from users")
        print(len(result_set.rows), "rows")
        for row in result_set.rows:
            print(row)

asyncio.run(main())
```

Sections: Python SDK for libSQL, Getting Started, Synchronous API

</details>

### libtad

Python library for accessing Time and Date APIs

`pip install libtad` · installs (wheel) · licence: not stated · rank 10860 · last release 2023-02-07 · [PyPI](https://pypi.org/project/libtad/)

### librouteros

Python implementation of MikroTik RouterOS API

`pip install librouteros` · installs (wheel) · licence: GPL-2.0-or-later · rank 10953 · last release 2026-09-15 · [PyPI](https://pypi.org/project/librouteros/) · [docs](https://librouteros.readthedocs.io)

_README extract left out: share-alike licence._

### llm-guard

LLM-Guard is a comprehensive tool designed to fortify the security of Large Language Models (LLMs). By offering sanitization, detection of harmful language, prevention of data leakage, and resistance against prompt injection attacks, LLM-Guard ensures that your interactions with LLMs remain safe and secure.

`pip install llm-guard` · does not install on CPython 3.14 · licence: not stated · rank 10977 · last release 2025-05-19 · [PyPI](https://pypi.org/project/llm-guard/) · [docs](https://llm-guard.com/) · [source](https://github.com/protectai/llm-guard)

<details><summary>README extract</summary>

Sections: What is LLM Guard?, Getting Started, Prompt scanners, Output scanners

</details>

### lib4sbom

Software Bill of Material (SBOM) generator and consumer library

`pip install lib4sbom` · installs (wheel) · licence: Apache-2.0 · rank 10999 · last release 2026-04-17 · [PyPI](https://pypi.org/project/lib4sbom/)

<details><summary>README extract</summary>

Lib4SBOM is a library to parse and generate Software Bill of Materials (SBOMs). It supports SBOMs created in both
SPDX and CycloneDX formats.

It has been developed on the assumption that having a generic abstraction of SBOM regardless of the underlying format will be useful to developers.

The following facilities are provided: ...

Example:
```python
>>> from lib4sbom.parser import SBOMParser
>>> test_parser = SBOMParser()
>>> print (f"SBOM type {test_parser.get_type()}")
SBOM type auto
>>> test_parser.parse_file("test_sbom.spdx")
>>> print (f"SBOM type {test_parser.get_type()}")
SBOM type spdx
>>> sbom_files = test_parser.get_files()
>>> print (sbom_files)
[]
...
```

...

</details>

### logfmter

A Python package which supports global logfmt formatted logging.

`pip install logfmter` · installs (wheel) · licence: MIT · rank 11035 · last release 2026-03-11 · [PyPI](https://pypi.org/project/logfmter/)

<details><summary>README extract</summary>

Add logfmt structured logging using the stdlib logging module and without changing a single log call.

Features:
- enables both human and computer readable logs, recommended as a "best practice" by Splunk
- formats all first and third party logs, you never have to worry about a library using a different logging format ...

Example:
```python
> logging.warn("user created", extra=user)

at=WARNING msg="user created" first_name=John last_name=Doe age=25
```

Sections: Why, Usage, Integration, Configuration, Extension, Guides, Gotchas, Required Software, Getting Started

</details>

### llmx

LLMX: A library for LLM Text Generation

`pip install llmx` · installs (wheel) · licence: MIT License · rank 11038 · last release 2024-02-06 · [PyPI](https://pypi.org/project/llmx/)

<details><summary>README extract</summary>

A simple python package that provides a unified interface to several LLM providers of chat fine-tuned models [OpenAI, AzureOpenAI, PaLM, Cohere and local HuggingFace Models].

> Note
> llmx wraps multiple api providers and its interface _may_ change as the providers as well as the general field of LLMs evolve. ...

Example:
```python
from llmx import llm
from llmx.datamodel import TextGenerationConfig

messages = [
    {"role": "system", "content": "You are a helpful assistant that can explain concepts clearly to a 6 year old child."},
    {"role": "user", "content": "What is  gravity?"}
]

openai_gen = llm(provider="openai")
...
```

Sections: LLMX - An API for Chat Fine-Tuned Language Models, Usage, A Note on Using Local HuggingFace Models, Current Work, Caveats

</details>

### logfire-mcp

The Pydantic Logfire MCP server! 🔍

`pip install logfire-mcp` · installs (wheel) · licence: MIT · rank 11058 · last release 2026-07-13 · [PyPI](https://pypi.org/project/logfire-mcp/) · [source](https://github.com/pydantic/logfire-mcp)

<details><summary>README extract</summary>

> [!IMPORTANT]
> This repository is archived. The STDIO MCP server in this package is no longer being updated.
> We now have a remote MCP server, which allows us to iterate faster on tools and provide a better experience.

Read more in our documentation.

If you have any questions, reach out to us on Slack or email us at engineering@pydantic.dev.

</details>

### legit-api-client

Inventory

`pip install legit-api-client` · installs (wheel) · licence: MIT · rank 11067 · last release 2026-11-05 · [PyPI](https://pypi.org/project/legit-api-client/) · [source](https://github.com/GIT_USER_ID/GIT_REPO_ID)

<details><summary>README extract</summary>

No description provided (generated by Openapi Generator

This Python package is automatically generated by the OpenAPI Generator project:

- API version: 1.0
- Package version: 1.1.5502
- Generator version: 7.27.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Python 3.11+ ...

Example:
```python
import legit_api_client
from legit_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = legit_api_client.Configuration(
    host = "
)

...
```

Sections: legit-api-client, Requirements., Setuptools, Tests, Getting Started, Documentation for API Endpoints, Documentation For Models, BearerAuth, Request headers

</details>

### langchain-redis

An integration package connecting Redis and LangChain for AI working memory

`pip install langchain-redis` · does not install on CPython 3.14 · licence: MIT License · rank 11077 · last release 2026-09-21 · [PyPI](https://pypi.org/project/langchain-redis/) · [source](https://github.com/langchain-ai/langchain-redis)

<details><summary>README extract</summary>

This package contains the LangChain integration with Redis, providing powerful tools for vector storage, semantic caching, and chat history management.

Example:
```python
from langchain_redis import RedisVectorStore, RedisConfig
from langchain_core.embeddings import Embeddings

embeddings = Embeddings()  # Your preferred embedding model

config = RedisConfig(
    index_name="my_vectors",
    redis_url="redis://localhost:6379",
    distance_metric="COSINE"  # Options: COSINE, L2, IP
)

...
```

Sections: langchain-redis, Configuration, Redis Connection Options, Standard Redis Connection, Redis Sentinel Connection, Features, 1. Vector Store, Usage, 2. Cache, What is Redis LangCache?

</details>

### lob-python

Lob

`pip install lob-python` · installs (wheel) · licence: MIT · rank 11097 · last release 2026-09-02 · [PyPI](https://pypi.org/project/lob-python/)

<details><summary>README extract</summary>

The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. &lt;p&gt; Looking for our previous documentation? # noqa: E501

</details>

### lets-be-rational

Pure python implementation of Peter Jaeckel's LetsBeRational.

`pip install lets-be-rational` · installs (wheel) · licence: MIT License · rank 11172 · last release 2026-05-29 · [PyPI](https://pypi.org/project/lets-be-rational/) · [source](https://github.com/vollib/py_lets_be_rational)

<details><summary>README extract</summary>

Features:
`lets_be_rational` is the canonical package for Peter Jaeckel's LetsBeRational algorithm.
It provides a pure Python implementation and keeps the historical `py_lets_be_rational`
import path available for compatibility.

Sections: Overview, Execution Speed, Numba Dependency, About "Let's be Rational"

</details>

### llm-anthropic

LLM access to models by Anthropic, including the Claude series

`pip install llm-anthropic` · installs (wheel) · licence: Apache-2.0 · rank 11182 · last release 2026-09-28 · [PyPI](https://pypi.org/project/llm-anthropic/)

<details><summary>README extract</summary>

LLM access to models by Anthropic, including the Claude series

Example:
```python
import llm

model = llm.get_model("claude-haiku-4.5")
print(model.prompt("Fun facts about chipmunks"))
```

Sections: llm-anthropic, Usage, New models, Web search, Web fetch, MCP connector, Code execution, Fast mode, Counting tokens, Usage from Python, Mid-conversation system messages, Extended thinking, Refusals, Model options

</details>

### libsql-experimental

(no summary)

`pip install libsql-experimental` · installs from source (sdist only) · licence: not stated · rank 11260 · last release 2025-06-09 · [PyPI](https://pypi.org/project/libsql-experimental/)

<details><summary>README extract</summary>

This package is experimental, which means it is not consider to be production grade. Furthermore, the package currently only supports Linux and macOS.

 SQLite for Production. Powered by libSQL.

 Turso ·
 Quickstart ·
 Examples ·
 Docs ·
 Discord ·
 Blog & Tutorials

1. Turso Quickstart — Learn how create and connect your first database.
2. ...

Sections: Turso + Python (experimental), Documentation, What is Turso?

</details>

### llama-index-vector-stores-milvus

llama-index vector_stores milvus integration

`pip install llama-index-vector-stores-milvus` · installs (wheel) · licence: MIT · rank 11431 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-milvus/)

### leval

Limited evaluator

`pip install leval` · installs (wheel) · licence: MIT · rank 11835 · last release 2026-08-13 · [PyPI](https://pypi.org/project/leval/)

<details><summary>README extract</summary>

> A limited expression evaluator

A little more suited for dynamic usage than `ast.literal_eval()`
while remaining as safe as the functions you pass in.

Under the hood, it uses the `ast` module to parse the expression,
then walks the AST in Python to evaluate the result. ...

Example:
```python
from leval.simple import simple_eval

assert simple_eval('1 + 2') == 3
assert simple_eval('x < -80 or x > 125 or x == 85', values={'x': 85})
assert simple_eval('abs(x) > 80', values={'x': -85}, functions={'abs': abs})
assert simple_eval('x.y.z + 8', values={('x', 'y', 'z'): 34}) == 42
```

Sections: Leval, Example usage, Simple API, Advanced API

</details>

### llama-index-llms-vertex

llama-index llms vertex integration

`pip install llama-index-llms-vertex` · installs (wheel) · licence: MIT · rank 12106 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-llms-vertex/)

<details><summary>README extract</summary>

NOTE: Gemini has largely been replaced by Google GenAI. Visit the Google GenAI page for the latest examples and documentation.

</details>

### lzallright

A Python 3.11+ LZO compression library in safe Rust, ported from LZ👌 (lzokay)

`pip install lzallright` · installs (wheel) · licence: MIT · rank 12123 · last release 2026-10-07 · [PyPI](https://pypi.org/project/lzallright/) · [source](https://github.com/vlaci/lzallright)

<details><summary>README extract</summary>

A Python 3.11+ implementation of the
LZO compression format in safe Rust,
ported from the C++ LZ👌 library.

Licensed under the friendly MIT license.

Wheels are built statically without any external dependencies.

</details>

### la-panic

AppleOS Kernel Panic Parser

`pip install la-panic` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 12151 · last release 2023-11-12 · [PyPI](https://pypi.org/project/la-panic/)

_README extract left out: share-alike licence._

### logstash_formatter

JSON formatter meant for logstash

`pip install logstash_formatter` · installs from source (sdist only) · licence: MIT License · rank 12176 · last release 2018-02-13 · [PyPI](https://pypi.org/project/logstash_formatter/)

<details><summary>README extract</summary>

This library is provided to allow standard python logging to output log data
as json objects ready to be shipped out to logstash.

This project has been originally open sourced by exoscale (which is a great hosting service btw), thanks to them.

Example:
```python
import logging
from logstash_formatter import LogstashFormatterV1

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = LogstashFormatterV1()

handler.setFormatter(formatter)
logger.addHandler(handler)
```

Sections: logstash_formatter: JSON logs for logstash, Usage, Sample output for LogstashFormatter, Sample output for LogstashFormatterV1

</details>

### linear-python

A Python client for the Linear API

`pip install linear-python` · installs (wheel) · licence: MIT License · rank 12257 · last release 2024-12-20 · [PyPI](https://pypi.org/project/linear-python/)

<details><summary>README extract</summary>

A Python client for the Linear API.

- Python 3.7+

 - requests
 - python-dotenv
 - strawberry-graphql
 - pydantic
 - typing-extensions

Example:
```python
from linear_python import LinearClient
client = LinearClient("<Linear API Key Here>")
```

Sections: Linear Python, Requirements, Usage, Configuration, Get Current User (Viewer), Create an Issue, Resources

</details>

### llama-index-llms-openrouter

llama-index llms openrouter integration

`pip install llama-index-llms-openrouter` · installs (wheel) · licence: MIT · rank 12266 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-llms-openrouter/)

<details><summary>README extract</summary>

Example:
```python
from llama_index.llms.openrouter import OpenRouter
from llama_index.core.llms import ChatMessage

llm = OpenRouter(
    api_key="<your-api-key>",
    max_tokens=256,
    context_window=4096,
    model="gryphe/mythomax-l2-13b",
)
```

Sections: LlamaIndex Llms Integration: Openrouter, Setup, Initialize OpenRouter, Generate Chat Responses, Streaming Responses, Complete with Prompt, Streaming Completion, Model Configuration, Provider Routing (OpenRouter), LLM Implementation example

</details>

### langflow-base-nightly

A Python package with a built-in web application

`pip install langflow-base-nightly` · installs (wheel) · licence: MIT · rank 12318 · last release 2026-06-09 · [PyPI](https://pypi.org/project/langflow-base-nightly/) · [docs](https://docs.langflow.org) · [source](https://github.com/langflow-ai/langflow)

### llama-index-vector-stores-pinecone

llama-index vector_stores pinecone integration

`pip install llama-index-vector-stores-pinecone` · installs (wheel) · licence: MIT · rank 12346 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-pinecone/)

### lumigo-core

Lumigo core utils

`pip install lumigo-core` · installs (wheel) · licence: Apache License 2.0 · rank 12424 · last release 2025-06-08 · [PyPI](https://pypi.org/project/lumigo-core/)

<details><summary>README extract</summary>

This is lumigo/python-core, Lumigo's core utils for distributed tracing.

</details>

### lbt-honeybee

Installs a collection of Honeybee core and extension libraries.

`pip install lbt-honeybee` · installs (wheel) · licence: AGPL-3.0 · rank 12501 · last release 2026-11-06 · [PyPI](https://pypi.org/project/lbt-honeybee/)

_README extract left out: share-alike licence._

### libtorrent

Python bindings for libtorrent-rasterbar

`pip install libtorrent` · does not install on CPython 3.14 · licence: BSD · rank 12617 · last release 2026-08-10 · [PyPI](https://pypi.org/project/libtorrent/)

### libdatachannel-py

libdatachannel-py is a Python binding for libdatachannel.

`pip install libdatachannel-py` · installs (wheel) · licence: Apache-2.0 · rank 12618 · last release 2026-10-14 · [PyPI](https://pypi.org/project/libdatachannel-py/) · [source](https://github.com/shiguredo/libdatachannel-py)

<details><summary>README extract</summary>

We will not respond to PRs or issues that have not been discussed on Discord. Also, Discord is only available in Japanese.

Please read < before use.

利用前に < をお読みください。

Sections: libdatachannel-py, About Shiguredo's open source software, 時雨堂のオープンソースソフトウェアについて, libdatachannel-py について, 特徴, 音声や映像コーデックの利用, Python, プラットフォーム, リリースビルド, 開発ビルド, テスト, lint と typecheck, サンプル, 優先実装

</details>

### llama-index-vector-stores-opensearch

llama-index vector_stores opensearch integration

`pip install llama-index-vector-stores-opensearch` · installs (wheel) · licence: MIT · rank 12731 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-opensearch/)

### libadvian

Small helpers that do not warrant their own library

`pip install libadvian` · installs (wheel) · licence: MIT License · rank 12832 · last release 2025-05-23 · [PyPI](https://pypi.org/project/libadvian/)

<details><summary>README extract</summary>

Small helpers that do not warrant their own library.

 - init_logging (libadvian.logging): Initializes default logger to our standard log format.
 - b64_to_uuid and uuid_to_b64 (libadvian.binpackers): URL-safe base64 UUID decode/encode.
 - ensure[utf8|str] (libadvian.binpackers): For making sure you are dealing with bytes or strings. ...

Example:
```python
libadvian.logging.httpmulti.HTTP_LOGGING_CONFIG"handlers".update({"session_options": { "headers": {
    "Myheader": "myval"
}}})
```

Sections: libadvian, Notable helpers, HTTP Logging notes, Docker, SSH agent forwarding, pre-commit considerations, Test suite

</details>

### lqp

Validate and translate Logical Query Protocol (LQP) S-expressions into Protobuf

`pip install lqp` · installs (wheel) · licence: not stated · rank 12907 · last release 2026-10-30 · [PyPI](https://pypi.org/project/lqp/)

<details><summary>README extract</summary>

Python SDK for the Logical Query Protocol (LQP). Provides ProtoBuf
bindings, a parser and pretty-printer for the human-readable S-expression syntax, and a
CLI for converting between S-expression and ProtoBuf formats.

Sections: LQP Python SDK, CLI Usage, Examples, Formatting, VSCode

</details>

### llama-index-storage-kvstore-redis

llama-index kvstore redis integration

`pip install llama-index-storage-kvstore-redis` · installs (wheel) · licence: MIT · rank 12912 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-storage-kvstore-redis/)

### llama-index-vector-stores-faiss

llama-index vector_stores faiss integration

`pip install llama-index-vector-stores-faiss` · installs (wheel) · licence: MIT · rank 12943 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-faiss/)

### llama-index-tools-mcp

llama-index tools mcp integration

`pip install llama-index-tools-mcp` · installs (wheel) · licence: MIT · rank 12949 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-tools-mcp/)

<details><summary>README extract</summary>

This tool connects to MCP Servers and allows an Agent to call the tools provided by MCP Servers.

This idea is migrated from Integrate MCP Tools into LlamaIndex.

Example:
```python
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

# We consider there is a mcp server running on 127.0.0.1:8000, or you can use the mcp client to connect to your own mcp server.
mcp_client = BasicMCPClient("
mcp_tool_spec = McpToolSpec(
    client=mcp_client,
    # Optional: Filter the tools by name
...
```

Sections: MCP ToolSpec, Usage, Helper Functions, `workflow_as_mcp`, `get_tools_from_mcp_url` / `aget_tools_from_mcp_url`, MCP Client Usage, Basic Client Operations, OAuth Authentication, Use a custom HTTP Client, Notebook Example

</details>

### loralib

PyTorch implementation of low-rank adaptation (LoRA), a parameter-efficient approach to adapt a large pre-trained deep learning model which obtains performance on-par with full fine-tuning.

`pip install loralib` · installs (wheel) · licence: MIT License · rank 13056 · last release 2023-08-27 · [PyPI](https://pypi.org/project/loralib/)

<details><summary>README extract</summary>

*(For the radio communication technique, see LoRa.)*

This repo contains the source code of the Python package `loralib` and several examples of how to integrate it with PyTorch models, such as those in Hugging Face.
We only support PyTorch for now.
See our paper for a detailed description of LoRA. ...

Example:
```python
# ===== Before =====
# layer = nn.Linear(in_features, out_features)

# ===== After ======
import loralib as lora
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Sections: LoRA: Low-Rank Adaptation of Large Language Models, Repository Overview, Quickstart, Now training can proceed as usual., Additional Notes, Contact

</details>

### langflow-base

A Python package with a built-in web application

`pip install langflow-base` · installs (wheel) · licence: MIT · rank 13095 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langflow-base/) · [docs](https://docs.langflow.org) · [source](https://github.com/langflow-ai/langflow)

### langchain-together

An integration package connecting Together AI and LangChain

`pip install langchain-together` · installs (wheel) · licence: MIT License · rank 13247 · last release 2026-03-24 · [PyPI](https://pypi.org/project/langchain-together/) · [source](https://github.com/langchain-ai/langchain-together)

<details><summary>README extract</summary>

This package contains the LangChain integration with Together AI.

Example:
```python
from langchain_together import ChatTogether
import os

os.environ["TOGETHER_API_KEY"] = "my-key"

llm = ChatTogether(
    model="Qwen/Qwen2.5-7B-Instruct-Turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",  # if not set in environment variable
)
```

Sections: langchain-together, Chat Models, Structured Outputs, Function Calls, JSON Mode, Function Calling, JSON Mode, Embeddings

</details>

### large-image

Python modules to work with large, multiresolution images.

`pip install large-image` · installs (wheel) · licence: Apache-2.0 · rank 13348 · last release 2026-10-29 · [PyPI](https://pypi.org/project/large-image/)

<details><summary>README extract</summary>

*Python modules to work with large, multiresolution images.*

Large Image is developed and maintained by the Data & Analytics group at Kitware, Inc. for processing large geospatial and medical images. This provides the backbone for several of our image analysis platforms including Resonant GeoData, HistomicsUI, and the Digital Slide Archive.

Features:
- Tile serving made easy
- Supports a wide variety of geospatial and medical image formats
- Convert to tiled Cloud Optimized (Geo)Tiffs (also known as pyramidal tiffs)
- Python methods for retiling or accessing regions of images efficiently ...

Sections: Large Image, Highlights, Pip, Conda, Docker Images, Modules

</details>

### langdiff

LangDiff is a Python library that solves the hard problems of streaming structured LLM outputs to frontends.

`pip install langdiff` · installs (wheel) · licence: Apache-2.0 · rank 13426 · last release 2025-08-19 · [PyPI](https://pypi.org/project/langdiff/) · [docs](https://langdiff.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

LangDiff is a Python library that solves the hard problems of streaming structured LLM outputs to frontends.

LangDiff provides intelligent partial parsing with granular, type-safe events as JSON structures build token by token, plus automatic JSON Patch generation for efficient frontend synchronization. ...

Example:
```python
parse_partial('{"it')
parse_partial('{"items":')
parse_partial('{"items": ["Buy a b')
parse_partial('{"items": ["Buy a banana", "')
parse_partial('{"items": ["Buy a banana", "Pack b')
parse_partial('{"items": ["Buy a banana", "Pack bags"]}')
```

Sections: ⚖️ LangDiff: Progressive UI from LLM, Demo, Core Features, Streaming Parsing, Change Tracking, Usage, Motivation, The Problem with Traditional Streaming Approaches, The Coupling Problem, The LangDiff Approach

</details>

### lookml

A batteries included API for automating your LookML

`pip install lookml` · installs (wheel) · licence: MIT License · rank 13474 · last release 2021-02-04 · [PyPI](https://pypi.org/project/lookml/)

### llama-index-llms-gemini

llama-index llms gemini integration

`pip install llama-index-llms-gemini` · installs (wheel) · licence: MIT · rank 13487 · last release 2026-01-21 · [PyPI](https://pypi.org/project/llama-index-llms-gemini/)

<details><summary>README extract</summary>

As of version `0.6.2`, this integration is no longer supported, and has been replaced by `llama-index-llms-google-genai`. Visit the Google GenAI page for the latest examples and documentation.

</details>

### langsmith-fetch

LangSmith Fetch - Minimal CLI for fetching LangSmith threads and traces

`pip install langsmith-fetch` · installs (wheel) · licence: not stated · rank 13528 · last release 2025-12-12 · [PyPI](https://pypi.org/project/langsmith-fetch/)

<details><summary>README extract</summary>

LangSmith Fetch is CLI for fetching threads or traces from LangSmith projects. It is designed to be easily used by humans or code agents to programmatically fetch LangSmith data for testing and debugging.

Sections: LangSmith Fetch, 🚀 Quickstart, Commands, Flags, Output Formats, Concepts, Configuration, Tests

</details>

### lc3py

LC3 Codec library wrapper

`pip install lc3py` · installs (wheel) · licence: Apache-2.0 · rank 13602 · last release 2025-02-12 · [PyPI](https://pypi.org/project/lc3py/)

### lighter-sdk

Python SDK for lighter.xyz

`pip install lighter-sdk` · installs (wheel) · licence: not stated · rank 13640 · last release 2026-10-19 · [PyPI](https://pypi.org/project/lighter-sdk/)

<details><summary>README extract</summary>

Python SDK for Lighter trading. Includes api clients and signer.

</details>

### lfx

Langflow Executor - A lightweight CLI tool for executing and serving Langflow AI flows

`pip install lfx` · installs (wheel) · licence: not stated · rank 13649 · last release 2026-11-04 · [PyPI](https://pypi.org/project/lfx/)

<details><summary>README extract</summary>

The Langflow Executor (LFX) is a command-line tool that serves and runs flows statelessly from flow JSON files with minimal dependencies.

Running a flow with LFX is similar to running flows with the `--backend-only` environment variable enabled, but even more lightweight because the Langflow package and all of its dependencies don't need to be ...

Example:
```python
"""A simple agent flow example for Langflow.

Usage:
    uv run lfx run simple_agent.py "How are you?"
"""

import os
from pathlib import Path

from lfx import components as cp
from lfx.graph import Graph
from lfx.log.logger import LogConfig

async def get_graph() -> Graph:
    """Create and return the graph with async component initialization."""
...
```

...

</details>

### langchain-agentcore-codeinterpreter

Amazon Bedrock AgentCore Code Interpreter sandbox integration for Deep Agents

`pip install langchain-agentcore-codeinterpreter` · installs (wheel) · licence: MIT · rank 13651 · last release 2026-10-28 · [PyPI](https://pypi.org/project/langchain-agentcore-codeinterpreter/) · [source](https://github.com/langchain-ai/langchain-aws)

<details><summary>README extract</summary>

Amazon Bedrock AgentCore Code Interpreter sandbox integration for Deep Agents.

This package provides `AgentCoreSandbox` — a `SandboxBackendProtocol` implementation that wraps AgentCore's Code Interpreter, a secure, isolated MicroVM environment for executing code. ...

Example:
```python
from langchain_agentcore_codeinterpreter import AgentCoreSandbox

with AgentCoreSandbox.create(region="us-west-2") as backend:
    result = backend.execute("echo hello")
    print(result.output, result.exit_code)  # "hello" 0
```

Sections: langchain-agentcore-codeinterpreter, Prerequisites, Usage, Standalone, With Deep Agents, File operations, Session behavior

</details>

### llama-index-postprocessor-cohere-rerank

llama-index postprocessor cohere rerank integration

`pip install llama-index-postprocessor-cohere-rerank` · installs (wheel) · licence: MIT · rank 13733 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-postprocessor-cohere-rerank/)

### logfire-cli

The command-line interface for Pydantic Logfire.

`pip install logfire-cli` · installs (wheel) · licence: MIT · rank 13758 · last release 2026-11-07 · [PyPI](https://pypi.org/project/logfire-cli/) · [docs](https://pydantic.dev/docs/logfire/) · [source](https://github.com/pydantic/logfire-cli)

<details><summary>README extract</summary>

The Rust command-line interface for Pydantic Logfire.
Sign in, query your traces and logs, manage projects and tokens, and connect your
coding agent to Logfire from the terminal.

This package installs the native CLI, not the Python instrumentation SDK.
Install an application SDK separately to send telemetry; see the
Logfire documentation.

Sections: Logfire CLI, New to Logfire, Use an existing account, Connect a local project, Run Python with automatic instrumentation, Set up instrumentation with a coding agent, Help and updates

</details>

### llama-index-embeddings-langchain

llama-index embeddings langchain integration

`pip install llama-index-embeddings-langchain` · installs (wheel) · licence: MIT · rank 13826 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-langchain/)

### llama-index-readers-confluence

llama-index readers confluence integration

`pip install llama-index-readers-confluence` · installs (wheel) · licence: MIT · rank 14033 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-readers-confluence/)

<details><summary>README extract</summary>

This loader loads pages from a given Confluence cloud instance. The user needs to specify the base URL for a Confluence
instance to initialize the ConfluenceReader - base URL needs to end with `/wiki`.

The user can optionally specify OAuth 2.0 credentials to authenticate with the Confluence instance. ...

Example:
```python
# Example that reads the pages with the `page_ids`
from llama_index.readers.confluence import ConfluenceReader

token = {"access_token": "<access_token>", "token_type": "<token_type>"}
oauth2_dict = {"client_id": "<client_id>", "token": token}

base_url = "

page_ids = ["<page_id_1>", "<page_id_2>", "<page_id_3"]
space_key = "<space_key>"

...
```

Sections: Confluence Loader, Advanced Configuration, Usage, Event System Integration

</details>

### libsasscompiler

django pipeline scss/sass compiler, no needed of ruby

`pip install libsasscompiler` · installs (wheel) · licence: MIT · rank 14078 · last release 2026-02-22 · [PyPI](https://pypi.org/project/libsasscompiler/)

<details><summary>README extract</summary>

A fast scss/sass compiler for django-pipeline using python libsass port (no needed of ruby-sass anymore)

Same as django-pipeline

Sections: Libsasscompiler, Requirements, Usage

</details>

### lgpio

Linux SBC GPIO module

`pip install lgpio` · installs from source (sdist only) · licence: unlicense.org · rank 14081 · last release 2024-04-13 · [PyPI](https://pypi.org/project/lgpio/)

<details><summary>README extract</summary>

lgpio is a module for Linux Single Board Computers (SBC) which allows control of the General Purpose Input Outputs (GPIO).

Features:
* reading and writing GPIO singly and in groups
* software timed PWM and waves
* callbacks on GPIO level change
* notifications via pipe on GPIO level change
* I2C wrapper
* SPI wrapper
* serial link wrapper

Sections: lgpio Package, Features

</details>

### logging-test-case

Provides class LoggingTestCase to help test log files.

`pip install logging-test-case` · installs (wheel) · licence: MIT · rank 14132 · last release 2020-05-25 · [PyPI](https://pypi.org/project/logging-test-case/)

<details><summary>README extract</summary>

Production systems rely heavily upon logging. Unit tests should verify
logs are correct. `unittest.assertLogs()` allows developers to verify
logs are correct. Including this context manager in every test case
becomes tiresome. Also, if the test fails, the logs are not displayed.

This project provides the function decorator `@capturelogs`. ...

Example:
```python
class CaptureLogsExample(unittest.TestCase):
    def test_assert_logs(self):
        """Verify logs using built-in self.assertLogs()."""
        with self.assertLogs('foo', level='INFO') as logs:
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')
...
```

...

</details>

### localstack-extension-platform-observability

LocalStack Extension: LocalStack Extension: Platform observability

`pip install localstack-extension-platform-observability` · installs (wheel) · licence: not stated · rank 14137 · last release 2024-07-16 · [PyPI](https://pypi.org/project/localstack-extension-platform-observability/)

<details><summary>README extract</summary>

LocalStack extension for providing insights into the LocalStack platform in the form of service-specific traces and metrics.

Sections: LocalStack Extension: Platform observability, Usage, Metrics, Trace logs, Lambda, Lambda SQS Event source listeners

</details>

### lamindb_setup

Setup & configure LaminDB.

`pip install lamindb_setup` · installs (wheel) · licence: not stated · rank 14143 · last release 2026-10-27 · [PyPI](https://pypi.org/project/lamindb_setup/)

<details><summary>README extract</summary>

The `lamindb` library offers joint database and storage access through registries that are based on the Django ORM and `universal_pathlib`. Django requires an environment with settings to be in place at import time. `lamindb_setup` takes care of setting up an environment so that a user importing `lamindb` can focus on high-level data workloads. ...

</details>

### llama-index-storage-docstore-redis

llama-index docstore redis integration

`pip install llama-index-storage-docstore-redis` · installs (wheel) · licence: MIT · rank 14210 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-storage-docstore-redis/)

### lyteidl

IDL for Flyte Platform

`pip install lyteidl` · installs (wheel) · licence: not stated · rank 14224 · last release 2026-05-01 · [PyPI](https://pypi.org/project/lyteidl/)

### latch_persistence

Add your description here

`pip install latch_persistence` · installs (wheel) · licence: not stated · rank 14235 · last release 2026-07-10 · [PyPI](https://pypi.org/project/latch_persistence/)

### letschatty

Models and custom classes to work across the Chattyverse

`pip install letschatty` · installs (wheel) · licence: MIT License · rank 14250 · last release 2026-11-06 · [PyPI](https://pypi.org/project/letschatty/)

<details><summary>README extract</summary>

poetry version patch; poetry build; poetry publish

Models and custom classes to work across the Chattyverse.

Lastest update: 2024-11-07

Sections: PUSH, Chatty Analytics, Architecture, Models, Services

</details>

### litert-lm-builder

Python tools for building and inspecting LiteRT-LM file formats

`pip install litert-lm-builder` · installs (wheel) · licence: Apache Software License · rank 14317 · last release 2026-11-05 · [PyPI](https://pypi.org/project/litert-lm-builder/)

<details><summary>README extract</summary>

Command-line tool and Python API for building and unpacking LiteRT-LM files.

</details>

### langchain-parallel

A LangChain integration for Parallel Web AI services, including Chat and Search.

`pip install langchain-parallel` · installs (wheel) · licence: MIT License · rank 14367 · last release 2026-07-13 · [PyPI](https://pypi.org/project/langchain-parallel/) · [source](https://github.com/parallel-web/langchain-parallel)

<details><summary>README extract</summary>

This package provides LangChain integrations for Parallel, covering Parallel's full developer-facing API surface.

Features:
| Surface | Class | Backed by |

| Chat completions with citations + structured output | `ChatParallel` | `/chat/completions` (lite/base/core) |
| Web search → Documents (RAG) | `ParallelSearchRetriever` | `/v1/search` |
| Web search tool (agents) | ...

Example:
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_parallel.chat_models import ChatParallelWeb

chat = ChatParallelWeb(model="speed")

messages = [
    SystemMessage(content="You are a helpful assistant with access to real-time web information."),
...
```

...

</details>

### langflow

A Python package with a built-in web application

`pip install langflow` · installs (wheel) · licence: MIT · rank 14471 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langflow/) · [docs](https://docs.langflow.org) · [source](https://github.com/langflow-ai/langflow)

<details><summary>README extract</summary>

Langflow is a powerful platform for building and deploying AI-powered agents and workflows. It provides developers with both a visual authoring experience and built-in API and MCP servers that turn every workflow into a tool that can be integrated into applications built on any framework or stack. ...

Sections: ✨ Highlight features, 🖥️ Langflow Desktop, ⚡️ Quickstart, Run, Run from source, Docker, 🚀 Deployment, ⭐ Stay up-to-date

</details>

### llama-index-storage-index-store-redis

llama-index index_store redis integration

`pip install llama-index-storage-index-store-redis` · installs (wheel) · licence: MIT · rank 14506 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-storage-index-store-redis/)

### llama-index-embeddings-vertex

llama-index embeddings vertex integration

`pip install llama-index-embeddings-vertex` · installs (wheel) · licence: MIT · rank 14508 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-embeddings-vertex/)

<details><summary>README extract</summary>

Implements Vertex AI Embeddings Models:

| Model | Release Date |

| textembedding-gecko@003 | December 12, 2023 |
| textembedding-gecko@002 | November 2, 2023 |
| textembedding-gecko-multilingual@001 | November 2, 2023 |
| textembedding-gecko@001 | June 7, 2023 |
| multimodalembedding | | ...

Example:
```python
from google.oauth2 import service_account
from llama_index.embeddings.vertex import VertexTextEmbedding

credentials = service_account.Credentials.from_service_account_file(
    "path/to/your/service-account.json"
)

embedding = VertexTextEmbedding(
    model_name="textembedding-gecko@003",
    project="your-project-id",
...
```

Sections: LlamaIndex Embeddings Integration: Vertex, New Features, Example Usage

</details>

### lovely-numpy

💟 Lovely numpy

`pip install lovely-numpy` · installs (wheel) · licence: MIT · rank 14554 · last release 2026-05-15 · [PyPI](https://pypi.org/project/lovely-numpy/) · [docs](https://xl0.github.io/lovely-numpy) · [source](https://github.com/xl0/lovely-numpy)

<details><summary>README extract</summary>

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Example:
```python
from lovely_numpy import lo
```

Sections: 💟 Lovely NumPy, Read full docs, More lovely stuff, Working with numbers, How to use, <code>Lo</code> and behold!, Going `.deeper`, Now in `.rgb` color, See the `.chans`, Grouping, Histogram, Options \| Docs, Without <code>Lo</code>, Matplotlib integration \| Docs

</details>

### linkml-map

a framework for specifying and executing mappings between data models

`pip install linkml-map` · installs (wheel) · licence: not stated · rank 14578 · last release 2026-08-26 · [PyPI](https://pypi.org/project/linkml-map/)

<details><summary>README extract</summary>

LinkML Map is a framework for specifying and executing declarative mappings between data models.
At its core is the TransformationSpecification — a YAML-based language for describing how to
map one data model to another, independent of serialization format or execution engine.

Features:

- YAML-based lightweight transformation syntax ...

Sections: linkml-map, Quickstart, More

</details>

### libthumbor

libthumbor is the python extension to generate thumbor URLs

`pip install libthumbor` · installs (wheel) · licence: MIT License · rank 14586 · last release 2022-03-31 · [PyPI](https://pypi.org/project/libthumbor/)

<details><summary>README extract</summary>

libthumbor allows easy usage of
thumbor in Python. Check the docs for django integration.

This version is compliant with the new URL generation schema (thumbor 3.0.0 and up).

Example:
```python
from libthumbor import CryptoURL

crypto = CryptoURL(key='my-security-key')

encrypted_url = crypto.generate(
    width=300,
    height=200,
    smart=True,
    image_url='/path/to/my/image.jpg'
)
```

Sections: Using it, Docs, Bernardo Heynemann, Rafael Caricio, Fábio Costa

</details>

### langgraph-checkpoint-mysql

Library with a MySQL implementation of LangGraph checkpoint saver.

`pip install langgraph-checkpoint-mysql` · installs (wheel) · licence: MIT · rank 14607 · last release 2026-01-23 · [PyPI](https://pypi.org/project/langgraph-checkpoint-mysql/) · [source](https://www.github.com/tjni/langgraph-checkpoint-mysql)

<details><summary>README extract</summary>

Implementation of LangGraph CheckpointSaver that uses MySQL.

> [!TIP]
> The code in this repository tries to mimic the code in langgraph-checkpoint-postgres as much as possible to enable keeping in sync with the official checkpointer implementation. ...

Example:
```python
from langgraph.checkpoint.mysql.pymysql import PyMySQLSaver

write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
read_config = {"configurable": {"thread_id": "1"}}

DB_URI = "mysql://mysql:mysql@localhost:3306/mysql"
with PyMySQLSaver.from_conn_string(DB_URI) as checkpointer:
...
```

Sections: LangGraph Checkpoint MySQL, Dependencies, Usage, Async

</details>

### langchain-oci

An integration package connecting OCI and LangChain

`pip install langchain-oci` · installs (wheel) · licence: UPL-1.0 · rank 14640 · last release 2026-10-21 · [PyPI](https://pypi.org/project/langchain-oci/) · [source](https://github.com/oracle/langchain-oracle)

<details><summary>README extract</summary>

This package contains the LangChain integrations with Oracle Cloud Infrastructure (OCI).

> ⭐ If this package is useful to you, consider starring the repository — it helps other developers discover these integrations.

Example:
```python
from langchain_core.messages import HumanMessage
from langchain_oci import OCIGenAIEmbeddings
from langchain_oci import create_deepagents_agent
from langchain_oci.datastores import ADB

# ADB datastore requires langchain-oracledb
store = ADB(
    dsn="mydb_low",
    user="ADMIN",
    password="***",
...
```

...

</details>

### loggly-python-handler

Python logging handler that sends messages to Loggly

`pip install loggly-python-handler` · installs (wheel) · licence: MIT License · rank 14650 · last release 2020-01-03 · [PyPI](https://pypi.org/project/loggly-python-handler/)

<details><summary>README extract</summary>

Python Logging Loggly Handler

A simple Python logging Loggly handler that can be used to send to a Loggly Gen2 https endpoint. Borrowed the extra fields concept from the graypy logging library. Check out Loggly's Python logging documentation to learn more.

Sections: Use in python, Configuration, Use Configuration in python file, Use in Django, settings.py, views.py

</details>

### liboqs-python

Python bindings for liboqs, providing post-quantum public key cryptography algorithms

`pip install liboqs-python` · installs (wheel) · licence: not stated · rank 14673 · last release 2026-10-28 · [PyPI](https://pypi.org/project/liboqs-python/) · [source](https://github.com/open-quantum-safe/liboqs-python.git)

<details><summary>README extract</summary>

The Open Quantum Safe (OQS) project has the goal of developing and
prototyping quantum-resistant cryptography.

liboqs-python offers a Python 3 wrapper for the
Open Quantum Safe
liboqs
C library, which is a C library for quantum-resistant cryptographic algorithms. ...

Example:
```python
import oqs
```

Sections: liboqs-python: Python 3 bindings for liboqs, About, Pre-requisites, Run the examples, Run the unit test, Platform-specific notes, Usage in standalone applications, Docker, Team

</details>

### lambda-multiprocessing

drop-in replacement for multiprocessing.Pool in AWS Lambda functions (without /dev/shm shared memory)

`pip install lambda-multiprocessing` · installs (wheel) · licence: MIT License · rank 14704 · last release 2025-07-01 · [PyPI](https://pypi.org/project/lambda-multiprocessing/)

<details><summary>README extract</summary>

This library is for doing multiprocessing in AWS Lambda in python.

(This is unrelated to inline lambda functions such as `f = lambda x: x*x`.
 That's a different kind of lambda function.)

If you deploy Python code to an AWS Lambda function,
the multiprocessing functions in the standard library such as `multiprocessing.Pool.map` will not work. ...

Example:
```python
from lambda_multiprocessing import Pool

def work(x):
    return x*x

with Pool() as p:
    results = p.map(work, range(5))
assert results == [x*x for x in range(5)]
```

Sections: lambda_multiprocessing - Multiprocessing in AWS Lambda, The Problem, The Solution, Usage, Limitations, Concurrency Safety, Design, Deadlock, 1.0

</details>

### large-image-source-gdal

A GDAL tilesource for large_image.

`pip install large-image-source-gdal` · installs (wheel) · licence: Apache-2.0 · rank 14808 · last release 2026-10-29 · [PyPI](https://pypi.org/project/large-image-source-gdal/)

<details><summary>README extract</summary>

A GDAL tilesource for large_image.

See the large-image package for more details.

</details>

### logscope

Fancy logging with local SQLite storage.

`pip install logscope` · installs (wheel) · licence: MIT · rank 14820 · last release 2025-03-21 · [PyPI](https://pypi.org/project/logscope/)

<details><summary>README extract</summary>

Logscope is a Python logging library that brings together SQLite storage and pretty console output. Write logs to both your terminal and a queryable database with a dead-simple API.

Features:
- Write logs to SQLite + console simultaneously
- Smart context tracking (captures function names and calling code)
- Colorized, pretty console output
- Thread-safe SQLite operations
- Dead simple API ...

Example:
```python
from logscope import logger

# Get a logger with default settings (SQLite + console output)
log = logger()

# Log some things!
log("Starting analysis")
log("Processing item", {"id": 123, "status": "pending"})
```

Sections: Logscope, Features, Quick Start, Configuration, Tracing Functions, How It Works, Querying Logs, Database Schema, Example Queries

</details>

### langchain-google-alloydb-pg

LangChain integrations for Google Cloud AlloyDB for PostgreSQL

`pip install langchain-google-alloydb-pg` · installs (wheel) · licence: Apache Software License · rank 14855 · last release 2026-10-29 · [PyPI](https://pypi.org/project/langchain-google-alloydb-pg/) · [source](https://github.com/googleapis/langchain-google-alloydb-pg-python.git)

<details><summary>README extract</summary>

- Client Library Documentation
- Product Documentation

The AlloyDB for PostgreSQL for LangChain package provides a first class experience for connecting to
AlloyDB instances from the LangChain ecosystem while providing the following benefits: ...

Example:
```python
from langchain_google_alloydb_pg import AlloyDBEngine, AlloyDBVectorStore
from langchain_google_vertexai import VertexAIEmbeddings

engine = AlloyDBEngine.from_instance("project-id", "region", "my-cluster", "my-instance", "my-database")
embeddings_service = VertexAIEmbeddings(model_name="text-embedding-005")
...
```

...

</details>

### llama-index-vector-stores-redis

llama-index vector_stores redis integration

`pip install llama-index-vector-stores-redis` · does not install on CPython 3.14 · licence: MIT · rank 14858 · last release 2026-08-31 · [PyPI](https://pypi.org/project/llama-index-vector-stores-redis/)

### lightning-sdk

SDK to develop using Lightning AI Studios

`pip install lightning-sdk` · installs (wheel) · licence: Apache-2.0 · rank 14871 · last release 2026-11-06 · [PyPI](https://pypi.org/project/lightning-sdk/) · [docs](https://lightning.ai/docs/overview/sdk-reference) · [source](https://github.com/Lightning-AI/sdk)

<details><summary>README extract</summary>

Automate Lightning AI resources from Python scripts, notebooks, and CI.

______________

 Quick start •
 Examples •
 CLI •
 Development •
 Docs

Features:
Lightning SDK turns Lightning AI into a Python API. Use it to create and manage
compute, run training or batch jobs, operate persistent studios, deploy
containers, inspect logs, and manage sandboxes without leaving your code. ...

Example:
```python
from lightning_sdk.sandbox import Sandbox

sandbox = Sandbox.create(name="python-readme", instance_type="cpu-1")
command = sandbox.run_command("python --version")
print(command.output)
sandbox.delete()
```

...

</details>

### lemonaid-inbox

Attention inbox for managing notifications from lemons and other background tools

`pip install lemonaid-inbox` · installs (wheel) · licence: not stated · rank 14917 · last release 2026-11-06 · [PyPI](https://pypi.org/project/lemonaid-inbox/) · [docs](https://github.com/petergaultney/lemonaid/tree/main/docs) · [source](https://github.com/petergaultney/lemonaid)

<details><summary>README extract</summary>

Monitor progress of and switch between lemons (go on... say 'LLMs' three times fast)
running in the terminal.

Hooks in Claude Code, Codex CLI, OpenCode and OpenClaw write a notification
whenever a session stops or needs input. The `lma` inbox shows those sessions,
what each is doing, and jumps you to its tmux pane or WezTerm tab. ...

Sections: 🍋🥤 lemonaid, Documentation

</details>

### lightsim2grid

LightSim2grid implements a c++ backend targeting the Grid2Op platform.

`pip install lightsim2grid` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 14971 · last release 2026-11-03 · [PyPI](https://pypi.org/project/lightsim2grid/) · [source](https://github.com/Grid2op/lightsim2grid)

<details><summary>README extract</summary>

Provide a fast backend for grid2op using c++ KLU and Eigen librairies. Its primary goal is to serve as a fast
backend for the grid2op platform, used primarily as a testbed platform for sequential decision making in
the world of power system.

See the Disclaimer to have a more detailed view on what is and what is not this package. ...

Features:
- Multiple powerflow algorithms: Newton-Raphson (single or distributed slack), Fast-Decoupled and
 Gauss-Seidel, each selectable with a choice of linear solver (Eigen SparseLU, SuiteSparse KLU, NICSLU
 or CKTSO) via the `lightsim2grid.algorithm` ...

Example:
```python
import grid2op
from lightsim2grid import LightSimBackend
env_name = "l2rpn_case14_sandbox"  # or any other name.
env = grid2op.make(env_name, backend=LightSimBackend())

...

</details>

