# Scientific/Engineering / Artificial Intelligence

[Index](README.md) · 393 packages in this topic, 268 more listed under another topic, by downloads.

### huggingface-hub

Client library to download and publish models, datasets and other repos on the huggingface.co hub

`pip install huggingface-hub` · installs (wheel) · licence: Apache Software License · rank 121 · last release 2026-10-29 · [PyPI](https://pypi.org/project/huggingface-hub/)

<details><summary>README extract</summary>

The official CLI and Python client for the Hugging Face Hub.

 About
 Documentation
 Install
 CLI Guide
 Contributing

 English |
 Deutsch |
 Français |
 हिंदी |
 한국어 |
 中文 (简体) |
 ಕನ್ನಡ

Example:
```python
from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="zai-org/GLM-5.2", filename="config.json")
```

Sections: Quick start, What is `huggingface_hub`?, Built for humans and AI agents, Use the Python library, Download files, Create a repository, Upload files, Integrating with the Hub.

</details>

### hf-xet

Fast transfer of large files with the Hugging Face Hub.

`pip install hf-xet` · installs (wheel) · licence: Apache-2.0 · rank 143 · last release 2026-10-30 · [PyPI](https://pypi.org/project/hf-xet/) · [docs](https://huggingface.co/docs/hub/xet/index) · [source](https://github.com/huggingface/xet-core.git)

<details><summary>README extract</summary>

`hf-xet` enables `huggingface_hub` to utilize xet storage for uploading and downloading to HF Hub. Xet storage provides chunk-based deduplication, efficient storage/retrieval with local disk caching, and backwards compatibility with Git LFS. This library is not meant to be used directly, and is instead intended to be used from huggingface_hub.

Features:
♻ chunk-based deduplication implementation: avoid transferring and storing chunks that are shared across binary files (models, datasets, etc).

🤗 Python bindings: bindings for huggingface_hub package. ...

Sections: 🤗 hf-xet - xet client tech, used in huggingface_hub, Welcome, Key features, Quick Start

</details>

### tokenizers

(no summary)

`pip install tokenizers` · installs (wheel) · licence: Apache Software License · rank 156 · last release 2026-10-09 · [PyPI](https://pypi.org/project/tokenizers/) · [source](https://github.com/huggingface/tokenizers)

<details><summary>README extract</summary>

Provides an implementation of today's most used tokenizers, with a focus on performance and
versatility.

Bindings over the Rust implementation.
If you are interested in the High-level design, you can go check it there.

Otherwise, let's dive in! ...

Example:
```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import ByteLevel

tok = Tokenizer(BPE())
tok.pre_tokenizer = Whitespace()                 # ✅ thread-safe on 3.14t
tok.post_processor = ByteLevel(trim_offsets=True)
```

...

</details>

### langchain

Building applications with LLMs through composability

`pip install langchain` · installs (wheel) · licence: MIT License · rank 198 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain/) · [docs](https://reference.langchain.com/python/langchain/langchain/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

To help you ship LangChain apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Sections: 🦜️🔗 LangChain, 🤔 What is this?, 📖 Documentation, Resources

</details>

### langchain-core

Building applications with LLMs through composability

`pip install langchain-core` · installs (wheel) · licence: MIT License · rank 207 · last release 2026-11-05 · [PyPI](https://pypi.org/project/langchain-core/) · [docs](https://reference.langchain.com/python/langchain_core/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

To help you ship LangChain apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Sections: 🦜🍎️ LangChain Core, 🤔 What is this?, ⛰️ Why build on top of LangChain Core?, 📖 Documentation, Resources

</details>

### transformers

Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.

`pip install transformers` · installs (wheel) · licence: Apache 2.0 License · rank 269 · last release 2026-11-06 · [PyPI](https://pypi.org/project/transformers/)

<details><summary>README extract</summary>

English |
 简体中文 |
 繁體中文 |
 한국어 |
 Español |
 日本語 |
 हिन्दी |
 मराठी |
 Русский |
 Português |
 తెలుగు |
 Français |
 Deutsch |
 Italiano |
 Tiếng Việt |
 العربية |
 اردو |
 বাংলা |
 فارسی |
 Română |
 Türkçe ...

Features:
1. Easy-to-use state-of-the-art models:
 - High performance on natural language understanding & generation, computer vision, audio, video, and multimodal tasks.
 - Low barrier to entry for researchers, engineers, and developers. ...

Example:
```python
from transformers import pipeline

pipeline = pipeline(task="text-generation", model="Qwen/Qwen2.5-1.5B")
pipeline("the secret to baking a really good cake is ")
...
```

Sections: Quickstart, Why should I use Transformers?, When shouldn't I use Transformers?, 100 projects using Transformers, Example models

</details>

### safetensors

(no summary)

`pip install safetensors` · installs (wheel) · licence: Apache Software License · rank 313 · last release 2026-06-09 · [PyPI](https://pypi.org/project/safetensors/) · [source](https://github.com/huggingface/safetensors)

<details><summary>README extract</summary>

Example:
```python
from safetensors.numpy import save_file, load_file
import numpy as np

tensors = {
   "a": np.zeros((2, 2)),
   "b": np.zeros((2, 3), dtype=np.uint8)
}

save_file(tensors, "./model.safetensors")

# Now loading
loaded = load_file("./model.safetensors")
```

Sections: Usage, Numpy, Torch

</details>

### datasets

HuggingFace community-driven open-source library of datasets

`pip install datasets` · installs (wheel) · licence: Apache Software License · rank 373 · last release 2026-10-05 · [PyPI](https://pypi.org/project/datasets/)

<details><summary>README extract</summary>

🤗 Datasets is a lightweight library providing two main features:

- one-line dataloaders for many public datasets: one-liners to download and pre-process any of the major public datasets (image datasets, audio datasets, text datasets in 467 languages and dialects, 3D medical images, video datasets, agent traces, etc.) provided on the HuggingFace ...

Example:
```python
from datasets import load_dataset

# Load a dataset and print the first example in the training set
squad_dataset = load_dataset('rajpurkar/squad')
print(squad_dataset'train')

# Process the dataset - add a column with the length of the context texts
dataset_with_length = squad_dataset.map(lambda x: {"length": len(x["context"])})

...
```

...

</details>

### langchain-protocol

Python bindings for the LangChain agent streaming protocol

`pip install langchain-protocol` · installs (wheel) · licence: MIT License · rank 403 · last release 2026-11-05 · [PyPI](https://pypi.org/project/langchain-protocol/) · [source](https://github.com/langchain-ai/agent-protocol)

<details><summary>README extract</summary>

Example:
```python
from langchain_protocol import Command, SubscribeParams

params: SubscribeParams = {
    "channels": ["messages", "lifecycle"],
}

subscribe: Command = {
    "id": 1,
    "method": "subscription.subscribe",
    "params": params,
}
```

Sections: Usage, What this package includes

</details>

### fastmcp

The fast, Pythonic way to build MCP servers and clients.

`pip install fastmcp` · installs (wheel) · licence: Apache-2.0 · rank 408 · last release 2026-11-03 · [PyPI](https://pypi.org/project/fastmcp/) · [docs](https://gofastmcp.com) · [source](https://github.com/PrefectHQ/fastmcp)

<details><summary>README extract</summary>

Move fast and make things.

*Made with 💙 by Prefect*

The Model Context Protocol (MCP) connects LLMs to tools and data. FastMCP is a full MCP application framework for servers, clients, and interactive apps. A server starts with ordinary Python:

Features:
Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. ...

Example:
```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if name == "main":
    mcp.run()
```

Sections: FastMCP 🚀, Why FastMCP, Scale MCP with Horizon, 📚 Documentation

</details>

### fastmcp-slim

The dependency-slim FastMCP package.

`pip install fastmcp-slim` · installs (wheel) · licence: Apache-2.0 · rank 423 · last release 2026-11-03 · [PyPI](https://pypi.org/project/fastmcp-slim/) · [docs](https://gofastmcp.com) · [source](https://github.com/PrefectHQ/fastmcp)

<details><summary>README extract</summary>

Move fast and make things.

*Made with 💙 by Prefect*

The Model Context Protocol (MCP) connects LLMs to tools and data. FastMCP gives you everything you need to go from prototype to production:

Features:
Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. ...

Example:
```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if name == "main":
    mcp.run()
```

Sections: FastMCP 🚀, Why FastMCP, Run FastMCP in production with Horizon, 📚 Documentation

</details>

### langchain-openai

An integration package connecting OpenAI and LangChain

`pip install langchain-openai` · installs (wheel) · licence: MIT License · rank 511 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain-openai/) · [docs](https://reference.langchain.com/python/integrations/langchain_openai/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-openai, 🤔 What is this?, 📖 Documentation, Resources

</details>

### langchain-text-splitters

LangChain text splitting utilities

`pip install langchain-text-splitters` · installs (wheel) · licence: MIT License · rank 539 · last release 2026-10-02 · [PyPI](https://pypi.org/project/langchain-text-splitters/) · [docs](https://docs.langchain.com/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: 🦜✂️ LangChain Text Splitters, 🤔 What is this?, 📖 Documentation, Resources

</details>

### strands-agents

A model-driven approach to building AI agents in just a few lines of code

`pip install strands-agents` · installs (wheel) · licence: Apache Software License · rank 548 · last release 2026-11-04 · [PyPI](https://pypi.org/project/strands-agents/) · [docs](https://strandsagents.com)

<details><summary>README extract</summary>

Documentation
 ◆ Samples
 ◆ CLI
 ◆ MCP Server

 Harness (Python, TypeScript)
 ◆ SDK (Python, TypeScript)
 ◆ Box
 ◆ Shell
 ◆ Evals
 ◆ Labs

Strands Agents is a simple yet powerful SDK that takes a model-driven approach to building and running AI agents. ...

Features:
- Lightweight & Flexible: Simple agent loop that just works and is fully customizable
- Model Agnostic: Support for Amazon Bedrock, Anthropic, Gemini, LiteLLM, Llama, Ollama, OpenAI, Writer, and custom providers ...

Example:
```python
from strands import Agent
from strands.vended_tools import http_request

agent = Agent(tools=[http_request])
agent("Tell me about the Strands harness features:
```

...

</details>

### mlflow-skinny

MLflow is an open source platform for the complete machine learning lifecycle

`pip install mlflow-skinny` · installs (wheel) · licence: Apache Software License · rank 696 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mlflow-skinny/) · [docs](https://mlflow.org/docs/latest) · [source](https://github.com/mlflow/mlflow)

<details><summary>README extract</summary>

📣 This is the `mlflow-skinny` package, a lightweight MLflow package without SQL storage, server, UI, or data science dependencies.
Additional dependencies can be installed to leverage the full feature set of MLflow. For example:

- To use the `mlflow.sklearn` component of MLflow Models, install `scikit-learn`, `numpy` and `pandas`. ...

Example:
```python
import mlflow

mlflow.set_tracking_uri("
mlflow.openai.autolog()
```

Sections: Get Started in 3 Simple Steps, LLMs & Agents, Model Training, Integrations, OpenTelemetry, Agent Frameworks (Python), Agent Frameworks (TypeScript), Agent Frameworks (Java), Model Providers, Gateways, Tools & No-Code, Hosting MLflow, 👥 Core Members

</details>

### sentence-transformers

Embeddings, Retrieval, and Reranking

`pip install sentence-transformers` · installs (wheel) · licence: Apache-2.0 · rank 775 · last release 2026-10-21 · [PyPI](https://pypi.org/project/sentence-transformers/) · [source](https://github.com/huggingface/sentence-transformers/)

<details><summary>README extract</summary>

<!--- BADGES: START --->

[][#github-license]
[][#pypi-package]
[][#pypi-package]
[][#docs-package]

<!-- [][#pypi-package] -->

<!--- BADGES: END --->

This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embedding and reranker models. ...

Example:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
```

Sections: Sentence Transformers: Embeddings, Retrieval, and Reranking, Getting Started, Embedding Models, Reranker Models, Sparse Encoder Models, Multi-Vector Encoder Models, Pre-Trained Models, Training, Companion Blog Posts, Application Examples

</details>

### ctranslate2

Fast inference engine for Transformer models

`pip install ctranslate2` · installs (wheel) · licence: MIT · rank 782 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ctranslate2/) · [docs](https://opennmt.net/CTranslate2) · [source](https://github.com/OpenNMT/CTranslate2)

<details><summary>README extract</summary>

CTranslate2 is a C++ and Python library for efficient inference with Transformer models.

The project implements a custom runtime that applies many performance optimization techniques such as weights quantization, layers fusion, batch reordering, etc., to accelerate and reduce the memory usage of Transformer models on CPU and GPU. ...

Features:
* Fast and efficient execution on CPU and GPU
The execution is significantly faster and requires less resources than general-purpose deep learning frameworks on supported models and tasks thanks to many advanced optimizations: layer fusion, padding ...

Sections: CTranslate2, Key features, Recommended libraries, Benchmarks, CPU, GPU, Additional resources

</details>

### langchain-anthropic

Integration package connecting Claude (Anthropic) APIs and LangChain

`pip install langchain-anthropic` · installs (wheel) · licence: MIT License · rank 785 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain-anthropic/) · [docs](https://reference.langchain.com/python/integrations/langchain_anthropic/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Example:
```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model="claude-sonnet-5-5",
    max_tokens=16000,
    output_config={"effort": "medium"},
)
```

Sections: langchain-anthropic, 🤔 What is this?, 📖 Documentation, Migrating to Claude Sonnet 5.5, Resources

</details>

### lightgbm

LightGBM Python-package

`pip install lightgbm` · installs (wheel) · licence: not stated · rank 795 · last release 2026-07-18 · [PyPI](https://pypi.org/project/lightgbm/) · [docs](https://lightgbm.readthedocs.io/en/latest/) · [source](https://github.com/lightgbm-org/LightGBM.git)

<details><summary>README extract</summary>

Sections: LightGBM Python-package, Preparation, Use LightGBM with PyArrow, Use LightGBM with Polars, Use LightGBM with Dask, Use LightGBM with pandas, Use LightGBM Plotting Capabilities, Use LightGBM with scikit-learn, Build from Sources, Build Threadless Version, Build MPI Version, Build GPU Version, Build CUDA Version, Build with MinGW-w64 on Windows

</details>

### accelerate

Accelerate

`pip install accelerate` · installs (wheel) · licence: Apache Software License · rank 799 · last release 2026-09-09 · [PyPI](https://pypi.org/project/accelerate/)

<details><summary>README extract</summary>

🤗 Accelerate was created for PyTorch users who like to write the training loop of PyTorch models but are reluctant to write and maintain the boilerplate code needed to use multi-GPUs/TPU/fp16.

🤗 Accelerate abstracts exactly and only the boilerplate code related to multi-GPUs/TPU/fp16 and leaves the rest of your code unchanged. ...

Features:
You should use 🤗 Accelerate when you want to easily run your training scripts in a distributed environment without having to renounce full control over your training loop. ...

Example:
```python
from accelerate import Accelerator, DeepSpeedPlugin

# deepspeed needs to know your gradient accumulation steps beforehand, so don't forget to pass it
...

</details>

### mlflow

MLflow is an open source platform for the complete machine learning lifecycle

`pip install mlflow` · installs (wheel) · licence: Apache Software License · rank 811 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mlflow/) · [docs](https://mlflow.org/docs/latest) · [source](https://github.com/mlflow/mlflow)

<details><summary>README extract</summary>

MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug,
evaluate, monitor, and optimize production-quality AI applications while
controlling costs and managing access to models and data. ...

Example:
```python
import mlflow

mlflow.set_tracking_uri("
mlflow.openai.autolog()
```

Sections: Get Started in 3 Simple Steps, LLMs & Agents, Model Training, Integrations, OpenTelemetry, Agent Frameworks (Python), Agent Frameworks (TypeScript), Agent Frameworks (Java), Model Providers, Gateways, Tools & No-Code, Hosting MLflow, 👥 Core Members

</details>

### magika

A tool to determine the content type of a file with deep learning

`pip install magika` · installs (wheel) · licence: Apache Software License · rank 845 · last release 2026-05-04 · [PyPI](https://pypi.org/project/magika/) · [docs](https://github.com/google/magika/blob/main/python/README.md) · [source](https://github.com/google/magika/)

<details><summary>README extract</summary>

<!-- -->

Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection. Under the hood, Magika employs a custom, highly optimized model that only weighs about a few MBs, and enables precise file identification within milliseconds, even when running on a single CPU. ...

Example:
```python
>>> from magika import Magika
>>> m = Magika()
>>> res = m.identify_bytes(b'function log(msg) {console.log(msg);}')
>>> print(res.output.label)
javascript
```

Sections: Magika Python Package, Using Magika as a command-line tool, Using Magika as a Python module, Core Concepts, API documentation

</details>

### wandb

A CLI and library for interacting with the Weights & Biases API.

`pip install wandb` · installs (wheel) · licence: MIT License · rank 866 · last release 2026-10-16 · [PyPI](https://pypi.org/project/wandb/) · [docs](https://docs.wandb.ai) · [source](https://github.com/wandb/wandb)

<details><summary>README extract</summary>

Use W&B to build better models faster. Track and visualize all the pieces of your machine learning pipeline, from datasets to production machine learning models. Get started with W&B today, sign up for a W&B account!

Building an LLM app? Track, debug, evaluate, and monitor LLM apps with Weave, our new suite of tools for GenAI. ...

Example:
```python
import wandb

# Project that the run is recorded to
project = "my-awesome-project"

# Dictionary with hyperparameters
config = {"epochs": 1337, "lr": 3e-4}

# The `with` syntax marks the run as finished upon exiting the `with` block,
# and it marks the run "failed" if there's an exception.

...
```

...

</details>

### langchain-classic

Building applications with LLMs through composability

`pip install langchain-classic` · installs (wheel) · licence: MIT License · rank 941 · last release 2026-06-10 · [PyPI](https://pypi.org/project/langchain-classic/) · [docs](https://reference.langchain.com/python/langchain_classic/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

To help you ship LangChain apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Sections: 🦜️🔗 LangChain Classic, 🤔 What is this?, 📖 Documentation

</details>

### faster-whisper

Faster Whisper transcription with CTranslate2

`pip install faster-whisper` · installs (wheel) · licence: MIT License · rank 963 · last release 2025-10-31 · [PyPI](https://pypi.org/project/faster-whisper/)

<details><summary>README extract</summary>

faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models.

This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU. ...

Example:
```python
from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
...
```

...

</details>

### mlflow-tracing

MLflow Tracing SDK is an open-source, lightweight Python package that only includes the minimum set of dependencies and functionality to instrument your code/models/agents with MLflow Tracing.

`pip install mlflow-tracing` · installs (wheel) · licence: Apache Software License · rank 964 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mlflow-tracing/) · [docs](https://mlflow.org/docs/latest) · [source](https://github.com/mlflow/mlflow)

<details><summary>README extract</summary>

MLflow Tracing (`mlflow-tracing`) is an open-source, lightweight Python package that only includes the minimum set of dependencies and functionality
to instrument your code/models/agents with MLflow Tracing Feature. It is designed to be a perfect fit for production environments where you want: ...

Example:
```python
import mlflow

mlflow.set_tracking_uri("databricks")
# Specify the experiment to log the traces to
mlflow.set_experiment("/Path/To/Experiment")
```

Sections: ✨ Features, 🌐 Choose Backend, 🚀 Getting Started, Connect to the MLflow Server, Start Logging Traces, 📘 Documentation, 🛑 Features _Not_ Included

</details>

### faiss-cpu

A library for efficient similarity search and clustering of dense vectors.

`pip install faiss-cpu` · installs (wheel) · licence: MIT · rank 1097 · last release 2026-09-16 · [PyPI](https://pypi.org/project/faiss-cpu/) · [docs](https://github.com/facebookresearch/faiss/wiki) · [source](https://github.com/facebookresearch/faiss)

<details><summary>README extract</summary>

Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. ...

Sections: Faiss, News, Introduction, How Faiss works, Full documentation of Faiss, Reference, Legal

</details>

### torchmetrics

PyTorch native Metrics

`pip install torchmetrics` · installs (wheel) · licence: Apache Software License · rank 1133 · last release 2026-03-09 · [PyPI](https://pypi.org/project/torchmetrics/) · [docs](https://torchmetrics.rtfd.io/en/latest/) · [source](https://github.com/Lightning-AI/torchmetrics)

<details><summary>README extract</summary>

Machine learning metrics for distributed, scalable PyTorch applications.

______________

 What is Torchmetrics •
 Implementing a metric •
 Built-in metrics •
 Docs •
 Community •
 License

______________

______________

Over 340,000 developers use Lightning Cloud - purpose-built for PyTorch and PyTorch Lightning.

- GPUs from $0.19. ...

Example:
```python
import torch

# import our library
import torchmetrics

# initialize metric
metric = torchmetrics.classification.Accuracy(task="multiclass", num_classes=5)

# move the metric to device you want computations to take place
device = "cuda" if torch.cuda.is_available() else "cpu"
metric.to(device)

n_batches = 10
for i in range(n_batches):
...
```

...

</details>

### pytorch-lightning

PyTorch Lightning is the lightweight PyTorch wrapper for ML researchers. Scale your models. Write less boilerplate.

`pip install pytorch-lightning` · installs (wheel) · licence: Apache Software License · rank 1219 · last release 2026-09-10 · [PyPI](https://pypi.org/project/pytorch-lightning/) · [docs](https://pytorch-lightning.rtfd.io/en/latest/) · [source](https://github.com/Lightning-AI/lightning)

<details><summary>README extract</summary>

**The lightweight PyTorch wrapper for high-performance AI research.
Scale your models, not the boilerplate.**

______________

 Website •
 How To Use •
 Docs •
 Examples •
 Community •
 Lightning AI •
 License

______________

Lightning disentangles PyTorch code to decouple the science from the engineering.

______________

Example:
```python
import os
import torch
from torch import nn
import torch.nn.functional as F
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader, random_split
from torchvision import transforms
import pytorch_lightning as pl
```

...

</details>

### peft

Parameter-Efficient Fine-Tuning (PEFT)

`pip install peft` · installs (wheel) · licence: Apache Software License · rank 1311 · last release 2026-10-01 · [PyPI](https://pypi.org/project/peft/)

<details><summary>README extract</summary>

Fine-tuning large pretrained models is often prohibitively costly due to their scale. Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of large pretrained models to various downstream applications by only fine-tuning a small number of (extra) model parameters instead of all the model's parameters. ...

Features:
There are many benefits of using PEFT but the main one is the huge savings in compute and storage, making PEFT applicable to many different use cases.

Example:
```python
import torch
from transformers import AutoModelForCausalLM
from peft import LoraConfig, TaskType, get_peft_model

device = torch.accelerator.current_accelerator().type if hasattr(torch, "accelerator") else "cuda"
model_id = "Qwen/Qwen2.5-3B-Instruct"
...

</details>

### google-generativeai

Google Generative AI High level API client library and tools.

`pip install google-generativeai` · installs (wheel) · licence: Apache Software License · rank 1350 · last release 2025-12-16 · [PyPI](https://pypi.org/project/google-generativeai/)

<details><summary>README extract</summary>

With Gemini 2.0, we took the chance to create a single unified SDK for all developers who want to use Google's GenAI models (Gemini, Veo, Imagen, etc). As part of that process, we took all of the feedback from this SDK and what developers like about other SDKs in the ecosystem to create the Google Gen AI SDK. ...

</details>

### typesafe-sdk

Python SDK for TypeSafe AI API.

`pip install typesafe-sdk` · installs (wheel) · licence: MIT · rank 1388 · last release 2026-10-14 · [PyPI](https://pypi.org/project/typesafe-sdk/) · [docs](https://docs.typesafe.ai/go/python-sdk) · [source](https://github.com/typesafe-ai/typesafe-sdk-python)

<details><summary>README extract</summary>

Python SDK for TypeSafe AI.

Example:
```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
...
```

Sections: TypeSafe AI Python SDK, Quickstart, Documentation

</details>

### deepagents

Production-ready, extensible agent harness with a built-in filesystem and context management, sub-agent delegation, skills, and long-term memory.

`pip install deepagents` · installs (wheel) · licence: MIT License · rank 1445 · last release 2026-11-05 · [PyPI](https://pypi.org/project/deepagents/) · [docs](https://reference.langchain.com/python/deepagents/) · [source](https://github.com/langchain-ai/deepagents)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out Deep Agents.js.

To help you ship LangChain apps to production faster, check out LangSmith.
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

Example:
```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="openai:gpt-6-astra",
    system_prompt="You are a research assistant.",
)
result = agent.invoke({"messages": "Research LangGraph and write a summary"})
```

Sections: 🧠🤖 Deep Agents, 🤔 What is this?, ❓ FAQ, How is this different from LangGraph or LangChain?, Does this work with open-weight or local models?, Can I use this in production?, 📖 Resources

</details>

### catboost

CatBoost Python Package

`pip install catboost` · installs (wheel) · licence: Apache License, Version 2.0 · rank 1548 · last release 2026-02-18 · [PyPI](https://pypi.org/project/catboost/) · [docs](https://catboost.ai/docs/) · [source](https://github.com/catboost/catboost)

<details><summary>README extract</summary>

CatBoost is a fast, scalable, high performance gradient boosting on decision trees library. Used for ranking, classification, regression and other ML tasks.

</details>

### bedrock-agentcore

An SDK for using Bedrock AgentCore

`pip install bedrock-agentcore` · installs (wheel) · licence: Apache Software License · rank 1572 · last release 2026-11-06 · [PyPI](https://pypi.org/project/bedrock-agentcore/) · [docs](https://github.com/aws/bedrock-agentcore-sdk-python)

<details><summary>README extract</summary>

Documentation
 ◆ Samples
 ◆ Discord
 ◆ Boto3 Python SDK
 ◆ Runtime Python SDK

Features:
Amazon Bedrock AgentCore enables you to deploy and operate highly effective agents securely, at scale using any framework and model. ...

Sections: Bedrock AgentCore SDK, Overview, Amazon Bedrock AgentCore services, 🏗️ Deployment, AgentCore CLI (Recommended), AWS CDK (Advanced)

</details>

### llama-index-core

Interface between LLMs and your data

`pip install llama-index-core` · installs (wheel) · licence: MIT · rank 1636 · last release 2026-09-21 · [PyPI](https://pypi.org/project/llama-index-core/) · [docs](https://docs.llamaindex.ai/en/stable/) · [source](https://github.com/run-llama/llama_index)

<details><summary>README extract</summary>

The core python package to the LlamaIndex library. Core classes and abstractions
represent the foundational building blocks for LLM applications, most notably,
RAG. Such building blocks include abstractions for LLMs, Vector Stores, Embeddings,
Storage, Callables and several others. ...

</details>

### diffusers

State-of-the-art diffusion in PyTorch.

`pip install diffusers` · installs (wheel) · licence: Apache Software License · rank 1669 · last release 2026-10-27 · [PyPI](https://pypi.org/project/diffusers/)

<details><summary>README extract</summary>

🤗 Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even 3D structures of molecules. Whether you're looking for a simple inference solution or training your own diffusion models, 🤗 Diffusers is a modular toolbox that supports both. ...

Example:
```python
from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", dtype=torch.float16)
pipeline.to("cuda")
pipeline("An image of a squirrel in Picasso style").images[0]
```

Sections: PyTorch, Quickstart, How to navigate the documentation, Popular Tasks & Pipelines, Popular libraries using 🧨 Diffusers

</details>

### jaxtyping

Type annotations and runtime checking for shape and dtype of JAX/NumPy/PyTorch/etc. arrays.

`pip install jaxtyping` · installs (wheel) · licence: MIT License · rank 1705 · last release 2026-06-13 · [PyPI](https://pypi.org/project/jaxtyping/) · [source](https://github.com/patrick-kidger/jaxtyping)

<details><summary>README extract</summary>

A library providing type annotations and runtime type-checking for the shape and dtype of JAX/PyTorch/NumPy/MLX/TensorFlow arrays and tensors.

_The name 'jax'typing is now historical, we support all of the above and have no JAX dependency!_

Example:
```python
from jaxtyping import Float
from torch import Tensor

# Accepts floating-point 2D arrays with matching axes
def matrix_multiply(x: Float[Tensor, "dim1 dim2"],
                    y: Float[Tensor, "dim2 dim3"]
                  ) -> Float[Tensor, "dim1 dim3"]:
    ...
```

Sections: jaxtyping, Documentation, See also: other libraries in the JAX ecosystem

</details>

### math-verify

HuggingFace library for verifying mathematical answers

`pip install math-verify` · installs (wheel) · licence: Apache Software License · rank 1738 · last release 2026-01-10 · [PyPI](https://pypi.org/project/math-verify/) · [source](https://github.com/huggingface/math-verify)

### intervaltree

Editable interval tree data structure for Python 2 and 3

`pip install intervaltree` · installs (wheel) · licence: Apache-2.0 · rank 1810 · last release 2025-12-24 · [PyPI](https://pypi.org/project/intervaltree/)

<details><summary>README extract</summary>

[][build status]

A mutable, self-balancing interval tree for Python 2 and 3. Queries may be by point, by range overlap, or by range envelopment.

This library was designed to allow tagging text and time intervals, where the intervals include the lower bound but not the upper bound.

Version 3 changes! ...

Example:
```python
>>> from intervaltree import Interval, IntervalTree
>>> t = IntervalTree()
>>> t
IntervalTree()
```

</details>

### gymnasium

A standard API for reinforcement learning and a diverse set of reference environments (formerly Gym).

`pip install gymnasium` · installs (wheel) · licence: MIT License · rank 1904 · last release 2026-10-05 · [PyPI](https://pypi.org/project/gymnasium/) · [docs](https://gymnasium.farama.org) · [source](https://github.com/Farama-Foundation/Gymnasium)

<details><summary>README extract</summary>

Gymnasium is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. ...

Example:
```python
import gymnasium as gym
env = gym.make("CartPole-v1")

observation, info = env.reset(seed=42)
for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
env.close()
```

Sections: Environments, API, Notable Related Libraries, Environment Versioning

</details>

### lightning

The Deep Learning framework to train, deploy, and ship AI products Lightning fast.

`pip install lightning` · installs (wheel) · licence: Apache Software License · rank 1917 · last release 2026-09-10 · [PyPI](https://pypi.org/project/lightning/) · [docs](https://lightning.ai/lightning-docs) · [source](https://github.com/Lightning-AI/lightning)

<details><summary>README extract</summary>

The deep learning framework to pretrain and finetune AI models.

Serving models? Use LitServe to build custom inference servers in pure Python.

______________

 Quick start •
 Examples •
 PyTorch Lightning •
 Fabric •
 Lightning Cloud •
 Community •
 Docs

Features:
Training models in plain PyTorch requires writing and maintaining a lot of repetitive engineering code. Handling backpropagation, mixed precision, multi-GPU, and distributed training is error-prone and often reimplemented for every project. ...

Example:
```python
# main.py
# ! pip install torchvision
import torch, torch.nn as nn, torch.utils.data as data, torchvision as tv, torch.nn.functional as F
import lightning as L

# --------------------------------
# Step 1: Define a LightningModule
# --------------------------------
...

</details>

### semchunk

A Python library for splitting text into smaller chunks while preserving as much local semantic context as possible.

`pip install semchunk` · installs (wheel) · licence: MIT License · rank 1937 · last release 2026-06-13 · [PyPI](https://pypi.org/project/semchunk/) · [docs](https://github.com/isaacus-dev/semchunk/blob/main/README.md) · [source](https://github.com/isaacus-dev/semchunk)

<details><summary>README extract</summary>

semchunk is a Python library for splitting text into smaller chunks while preserving as much local semantic context as possible.

semchunk supports AI-powered chunking, chunk overlapping, and chunk offsets, and works with any tokenizer or token counter, including those from Tiktoken and Transformers. ...

Example:
```python
import semchunk
import tiktoken                        # Transformers and Tiktoken are not dependencies,
from transformers import AutoTokenizer # they're just here for demonstration purposes.

chunk_size = 4 # A low chunk size is used here for demonstration purposes. Keep in mind, semchunk
...
```

Sections: semchunk 🧩, Setup 📦, Quickstart 👩‍💻, Usage 🕹️, `chunkerify()`, `chunk()`, How It Works 🔍, Benchmarks 📊

</details>

### tom-swe

Theory of Mind modeling for Software Engineering assistants

`pip install tom-swe` · installs (wheel) · licence: MIT License · rank 2011 · last release 2025-11-26 · [PyPI](https://pypi.org/project/tom-swe/) · [docs](https://github.com/All-Hands-AI/ToM-SWE#readme) · [source](https://github.com/All-Hands-AI/ToM-SWE)

<details><summary>README extract</summary>

* [10/2025] Beta testing program launched - join us in testing ToM-enhanced agents!

ToM-SWE is a Theory of Mind package designed to enhance Software Engineering agents with personalized user understanding and adaptive behavior. ...

Example:
```python
from tom_swe.tom_module import TomModule
import asyncio

async def demo():
    tom = TomModule()

    # Consult on user preferences
    consultation = await tom.consult(
        user_id="demo_user",
        current_context="User wants to implement a new feature"
    )
    print(consultation)

asyncio.run(demo())
```

Sections: News, Introduction, Join the Beta Test, Get Started, Set up LLM API Credentials, Easy Sample Demo, Core Features, Main Commands, OpenHands Integration, Prompts, Requirements

</details>

### outlines-core

Structured Text Generation in Rust

`pip install outlines-core` · installs (wheel) · licence: Apache-2.0 · rank 2055 · last release 2026-01-09 · [PyPI](https://pypi.org/project/outlines-core/) · [docs](https://dottxt-ai.github.io/outlines-core/) · [source](https://github.com/dottxt-ai/outlines-core)

<details><summary>README extract</summary>

[![Latest Version]][crates.io] [![License]][github]

*Structured generation (in Rust).*

This package provides the core functionality for structured generation, formerly implemented in Outlines,
with a focus on performance and portability, it offers a convenient way to:

- build regular expressions from JSON schemas ...

Example:
```python
import json

from outlines_core.json_schema import build_regex_from_schema
from outlines_core.guide import Guide, Index, Vocabulary

schema =  {
  "title": "Foo",
  "type": "object",
  "properties": {"date": {"type": "string", "format": "date"}}
}
regex = build_regex_from_schema(json.dumps(schema))

...
```

Sections: Outlines-core, Example, Vocabulary, Python Bindings, Setup, Before pushing your code, Join us

</details>

### nvidia-cudnn-frontend

NVIDIA cuDNN Frontend — Python and C++ Graph API with SOTA attention (SDPA / Flash Attention), MoE grouped GEMM fusions, and FP8/MXFP8 kernels for Hopper, Blackwell, and Rubin GPUs.

`pip install nvidia-cudnn-frontend` · installs (wheel) · licence: Apache Software License; MIT License · rank 2062 · last release 2026-11-04 · [PyPI](https://pypi.org/project/nvidia-cudnn-frontend/) · [docs](https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/) · [source](https://github.com/NVIDIA/cudnn-frontend)

<details><summary>README extract</summary>

cuDNN Frontend is NVIDIA's modern, open-source entry point to the cuDNN library and a growing collection of high-performance open-source kernels — scaled dot-product attention (SDPA / Flash Attention), grouped GEMM fusions for Mixture-of-Experts (MoE) training, fused normalization + activation, and more. ...

Features:
* Unified Graph API: Create reusable, persistent `cudnn_frontend::graph::Graph` objects to describe complex subgraphs.
* Ease of Use: Simplified C++ and Python bindings (via `nanobind`) that abstract away the boilerplate of the backend API. ...

Example:
```python
graph = cudnn.pygraph(..., cuda_graph_retention=cudnn.cuda_graph_retention.NONE)
```

...

</details>

### docling-ibm-models

This package contains the AI models used by the Docling PDF conversion package

`pip install docling-ibm-models` · installs (wheel) · licence: MIT · rank 2072 · last release 2026-10-21 · [PyPI](https://pypi.org/project/docling-ibm-models/) · [source](https://github.com/docling-project/docling-ibm-models)

<details><summary>README extract</summary>

AI modules to support the Docling PDF document conversion project.

- TableFormer is an AI module that recognizes the structure of a table and the bounding boxes of the table content.

Sections: Docling IBM models, Pipeline Overview, Datasets, Models, TableModel04, Configuration file, Model weights, Inference Tests

</details>

### optax

A gradient processing and optimization library in JAX.

`pip install optax` · installs (wheel) · licence: Apache Software License · rank 2102 · last release 2026-03-20 · [PyPI](https://pypi.org/project/optax/) · [docs](https://optax.readthedocs.io/) · [source](https://github.com/google-deepmind/optax)

<details><summary>README extract</summary>

Optax is a gradient processing and optimization library for JAX.

Optax is designed to facilitate research by providing building blocks
that can be easily recombined in custom ways.

Our goals are to

* Provide simple, well-tested, efficient implementations of core components. ...

Example:
```python
optimizer = optax.adam(learning_rate)
# Obtain the `opt_state` that contains statistics for the optimizer.
params = {'w': jnp.ones((num_weights,))}
opt_state = optimizer.init(params)
```

Sections: Optax, Introduction, Quickstart, Source code, Documentation, Benchmarking, Other optimization-adjacent libraries in JAX, Citing Optax

</details>

### docling-slim

Modular version of the Docling package: SDK and CLI for parsing PDF, DOCX, HTML, and more, to a unified document representation for powering downstream workflows such as gen AI applications.

`pip install docling-slim` · installs (wheel) · licence: MIT · rank 2134 · last release 2026-11-05 · [PyPI](https://pypi.org/project/docling-slim/) · [source](https://github.com/docling-project/docling)

<details><summary>README extract</summary>

Lightweight SDK for parsing documents with minimal dependencies and opt-in extras

Docling Slim is a minimal-dependency version of Docling that allows you to install only the components you need. It provides the core document processing functionality with ~50MB of base dependencies, and you can add specific features through optional extras. ...

Sections: Docling Slim, When to Use Docling Slim, For Most Users: Use the Main Docling Package, With Specific Features, Available Extras, Convenience Bundles, CLI, Core Components, PDF Formats, Office Formats (office = docx + pptx + xlsx), Web Formats (web = html + markdown), Other Formats, OCR Engines, Models

</details>

### docling

SDK and CLI for parsing PDF, DOCX, HTML, and more, to a unified document representation for powering downstream workflows such as gen AI applications.

`pip install docling` · installs (wheel) · licence: MIT · rank 2152 · last release 2026-11-05 · [PyPI](https://pypi.org/project/docling/) · [source](https://github.com/docling-project/docling)

<details><summary>README extract</summary>

Docling simplifies document processing by parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the generative AI ecosystem.

Features:
- 🗂️ Parsing of multiple document formats including PDF, DOCX, PPTX, XLSX, HTML, EPUB, Apple Pages, Numbers & Keynote, WAV, MP3, WebVTT, Box Notes, email formats (EML, MSG), iCalendar (ICS), images (PNG, TIFF, JPEG, ...), LaTeX, DocLang, plain text, ...

Example:
```python
from docling.document_converter import DocumentConverter

source = "  # a document via a local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
```

...

</details>

### bitsandbytes

k-bit optimizers and matrix multiplication routines.

`pip install bitsandbytes` · installs (wheel) · licence: MIT · rank 2193 · last release 2026-08-27 · [PyPI](https://pypi.org/project/bitsandbytes/) · [docs](https://huggingface.co/docs/bitsandbytes/main)

<details><summary>README extract</summary>

`bitsandbytes` enables accessible large language models via k-bit quantization for PyTorch. We provide three main features for dramatically reducing memory consumption for inference and training:

* 8-bit optimizers uses block-wise quantization to maintain 32-bit performance at a small fraction of the memory cost. ...

Sections: bitsandbytes, System Requirements, Legend, book: Documentation, QLoRA, LLM.int8(), 8-bit Optimizers

</details>

### inspect-ai

Framework for large language model evaluations

`pip install inspect-ai` · installs (wheel) · licence: MIT License · rank 2199 · last release 2026-11-07 · [PyPI](https://pypi.org/project/inspect-ai/) · [docs](https://inspect.aisi.org.uk/) · [source](https://github.com/UKGovernmentBEIS/inspect_ai)

<details><summary>README extract</summary>

[](

Welcome to Inspect, a framework for large language model evaluations created by the UK AI Security Institute.

Inspect provides many built-in components, including facilities for prompt engineering, tool usage, multi-turn dialog, and model graded evaluations. Extensions to Inspect (e.g. ...

</details>

### orbax-checkpoint

Orbax Checkpoint

`pip install orbax-checkpoint` · installs (wheel) · licence: Apache Software License · rank 2213 · last release 2026-11-03 · [PyPI](https://pypi.org/project/orbax-checkpoint/) · [source](http://github.com/google/orbax)

<details><summary>README extract</summary>

`pip install orbax-checkpoint` (latest PyPi release) OR

`pip install 'git+ (from this repository, at HEAD)

`import orbax.checkpoint`

Orbax includes a checkpointing library oriented towards JAX users, supporting a
variety of different features required by different frameworks, including
asynchronous checkpointing, various types, and various ...

</details>

### sherpa-onnx-core

Core shared libraries for sherpa-onnx

`pip install sherpa-onnx-core` · installs (wheel) · licence: Apache-2.0 · rank 2312 · last release 2026-10-27 · [PyPI](https://pypi.org/project/sherpa-onnx-core/)

### assemblyai

AssemblyAI Python SDK

`pip install assemblyai` · installs (wheel) · licence: MIT License · rank 2319 · last release 2026-10-23 · [PyPI](https://pypi.org/project/assemblyai/) · [docs](https://github.com/AssemblyAI/assemblyai-python-sdk/blob/master/README.md) · [source](https://github.com/AssemblyAI/assemblyai-python-sdk)

<details><summary>README extract</summary>

> _Build with AI models that can transcribe and understand audio

With a single API call, get access to AI models built on the latest AI breakthroughs to transcribe and understand audio and speech data securely at large scale. ...

Features:
- AssemblyAI's Python SDK
- Overview
- Documentation
- Migrating to 1.0
- Quick Start
 - Installation
 - Examples
 - Choosing a transcriber
 - Core Examples
 - Asyncio Examples
 - Speech Understanding Examples
 - LLM Gateway Examples
 - Streaming ...

Example:
```python
import assemblyai as aai

# set the API key
aai.settings.api_key = f"{ASSEMBLYAI_API_KEY}"
```

...

</details>

### evaluate

HuggingFace community-driven open-source library of evaluation

`pip install evaluate` · installs (wheel) · licence: Apache Software License · rank 2342 · last release 2025-09-18 · [PyPI](https://pypi.org/project/evaluate/)

<details><summary>README extract</summary>

> Tip: For more recent evaluation approaches, for example for evaluating LLMs, we recommend our newer and more actively maintained library LightEval.

🤗 Evaluate is a library that makes evaluating and comparing models and reporting their performance easier and more standardized.

It currently contains: ...

Sections: With pip, Usage, Adding a new evaluation module

</details>

### tilelang

A tile level programming language to generate high performance code.

`pip install tilelang` · installs (wheel) · licence: MIT · rank 2350 · last release 2026-09-30 · [PyPI](https://pypi.org/project/tilelang/)

<details><summary>README extract</summary>

Documentation ·
Installation ·
Examples ·
Releases ·
Contributing ·
TileLang (Ascend 950)

Tile Language (tile-lang) is a concise domain-specific language designed to streamline the development of high-performance GPU/CPU/NPU kernels (e.g., GEMM, Dequant GEMM, FlashAttention, LinearAttention). ...

Example:
```python
import torch
import tilelang
import tilelang.language as T

@tilelang.jit
def matmul_relu(A, B, block_M: int = 128, block_N: int = 128, block_K: int = 32):
    M, N, K = T.const("M, N, K")
    A: T.Tensor((M, K), T.float16)
    B: T.Tensor((K, N), T.float16)
    C = T.empty((M, N), T.float16)

...
```

Sections: Tile Language, Latest News, 2026, 2025, Quick Start, Examples, Benchmark Summary, Join the Discussion

</details>

### sherpa-onnx

(no summary)

`pip install sherpa-onnx` · installs (wheel) · licence: Apache licensed, as found in the LICENSE file · rank 2370 · last release 2026-10-27 · [PyPI](https://pypi.org/project/sherpa-onnx/)

<details><summary>README extract</summary>

### Supported functions

|Speech recognition| Speech synthesis | Source separation |

| ✔️ | ✔️ | ✔️ |

|Speaker identification| Speaker diarization | Speaker verification |

| ✔️ | ✔️ | ✔️ |

| Spoken Language identification | Audio tagging | Voice activity detection |

| ✔️ | ✔️ | ✔️ | ...

Sections: Flutter, Tauri, Introduction, Links for Huggingface Spaces, Links for pre-built Android APKs, Links for pre-built Flutter APPs, Real-time speech recognition, Text-to-speech, Links for pre-built Lazarus APPs, Generating subtitles, Links for pre-trained models, Some pre-trained ASR models (Streaming), Some pre-trained ASR models (Non-Streaming), Useful links

</details>

### flax

Flax: A neural network library for JAX designed for flexibility

`pip install flax` · installs (wheel) · licence: Apache Software License · rank 2393 · last release 2026-10-27 · [PyPI](https://pypi.org/project/flax/)

<details><summary>README extract</summary>

Overview
| Quick install
| What does Flax look like?
| Documentation

Released in 2024, Flax NNX is a new simplified Flax API that is designed to make
it easier to create, inspect, debug, and analyze neural networks in
JAX. It achieves this by adding first class support
for Python reference semantics. ...

Features:
Flax is a high-performance neural network library and ecosystem for
JAX that is designed for flexibility:
Try new forms of training by forking an example and by modifying the training
loop, not adding features to a framework. ...

Example:
```python
class MLP(nnx.Module):
  def init(self, din: int, dmid: int, dout: int, *, rngs: nnx.Rngs):
    self.linear1 = nnx.Linear(din, dmid, rngs=rngs)
    self.dropout = nnx.Dropout(rate=0.1, rngs=rngs)
...

</details>

### gensim

Python framework for fast Vector Space Modelling

`pip install gensim` · installs from source (sdist only) · licence: LGPL-2.1-only · rank 2433 · last release 2025-10-18 · [PyPI](https://pypi.org/project/gensim/) · [source](https://github.com/RaRe-Technologies/gensim)

_README extract left out: share-alike licence._

### simsimd

Portable mixed-precision BLAS-like vector math library for x86 and ARM

`pip install simsimd` · installs (wheel) · licence: Apache Software License · rank 2461 · last release 2026-03-07 · [PyPI](https://pypi.org/project/simsimd/)

<details><summary>README extract</summary>

Computing dot-products, similarity measures, and distances between low- and high-dimensional vectors is ubiquitous in Machine Learning, Scientific Computing, Geospatial Analysis, and Information Retrieval.
These algorithms generally have linear complexity in time, constant or linear complexity in space, and are data-parallel. ...

Features:
SimSIMD (Arabic: "سيمسيم دي") is a mixed-precision math library of over 350 SIMD-optimized kernels extensively used in AI, Search, and DBMS workloads. ...

Example:
```python
ndim = 1536 # OpenAI Ada embeddings
matrix1 = np.packbits(np.random.randint(2, size=(10_000, ndim)).astype(np.uint8))
matrix2 = np.packbits(np.random.randint(2, size=(1_000, ndim)).astype(np.uint8))

distances = simsimd.cdist(matrix1, matrix2,
...

</details>

### unstructured

A library that prepares raw documents for downstream ML tasks.

`pip install unstructured` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 2529 · last release 2026-11-06 · [PyPI](https://pypi.org/project/unstructured/)

<details><summary>README extract</summary>

The `unstructured` library provides open-source components for ingesting and pre-processing images and text documents, such as PDFs, HTML, Word docs, and many more. The use cases of `unstructured` revolve around streamlining and optimizing the data processing workflow for LLMs. ...

Example:
```python
from unstructured.partition.auto import partition

elements = partition("example-docs/layout-parser-paper.pdf")
```

Sections: Open-Source Pre-Processing Tools for Unstructured Data, eight_pointed_black_star: Quick Start, Run the library in a container, clap: Quick Tour, Documentation, PDF Document Parsing Example, bug: Reporting Bugs, books: Learn more, chart_with_upwards_trend: Analytics

</details>

### modelscope-hub

The official Python client to connect with ModelScope Hub.

`pip install modelscope-hub` · installs (wheel) · licence: Apache Software License · rank 2566 · last release 2026-10-30 · [PyPI](https://pypi.org/project/modelscope-hub/)

<details><summary>README extract</summary>

The official Python SDK & CLI for ModelScope Hub — download, upload, and manage AI assets from one unified interface.

modelscope.cn | modelscope.ai

Features:
`modelscope-hub` connects your code to the ModelScope ecosystem — models, datasets, Studio spaces, skills, and MCP servers — through a single `HubApi` class or the `ms-hub` CLI. ...

Example:
```python
from modelscope_hub import HubApi

api = HubApi(token="your-token")
user = api.whoami()
print(user.username)
```

Sections: Why modelscope-hub?, News, Command names, Quick Start, Authenticate, Download, Continuous dataset downloads, Upload, Create a Repository, Visibility and gated access, Model and dataset zones, Deploy a Studio, CLI Reference, `ms-hub login`

</details>

### kornia

Open Source Differentiable Computer Vision Library for PyTorch

`pip install kornia` · installs (wheel) · licence: Apache Software License · rank 2577 · last release 2026-10-23 · [PyPI](https://pypi.org/project/kornia/) · [docs](https://kornia.readthedocs.io/en/latest) · [source](https://github.com/kornia/kornia)

<details><summary>README extract</summary>

English | 简体中文

Docs •
Try it Now •
Tutorials •
Examples •
Blog •
Community

Kornia is a differentiable computer vision library that provides a rich set of differentiable image processing and geometric vision algorithms. ...

Example:
```python
import numpy as np
import kornia_rs as kr

from kornia.augmentation import AugmentationSequential, RandomAffine, RandomBrightness
from kornia.filters import StableDiffusionDissolving

# Load and prepare your image
img: np.ndarray = kr.read_image_any("img.jpeg")
img = kr.resize(img, (256, 256), interpolation="bilinear")

...
```

Sections: Key Components, From pip, From source with editable mode, From Github url (latest version), Quick Start, Strengthen the Core (Priority), AI Models, Documentation And Tutorial Optimization

</details>

### strands-agents-tools

A collection of specialized tools for Strands Agents

`pip install strands-agents-tools` · installs (wheel) · licence: Apache Software License · rank 2659 · last release 2026-11-04 · [PyPI](https://pypi.org/project/strands-agents-tools/) · [docs](https://strandsagents.com/)

<details><summary>README extract</summary>

Strands Agents Tools (`strands-agents-tools`) is deprecated in favor of the vended SDK tools.

See the migration guide for how to move off this package.

 Documentation
 ◆ Samples
 ◆ CLI
 ◆ MCP Server

 Harness (Python, TypeScript)
 ◆ SDK (Python, TypeScript)
 ◆ Box
 ◆ Shell
 ◆ Evals
 ◆ Labs ...

Example:
```python
from strands import Agent
from strands_tools import file_read, file_write, editor

agent = Agent(tools=[file_read, file_write, editor])

agent.tool.file_read(path="config.json")
agent.tool.file_write(path="output.txt", content="Hello, world!")
agent.tool.editor(command="view", path="script.py")
```

...

</details>

### chex

Chex: Testing made fun, in JAX!

`pip install chex` · installs (wheel) · licence: Apache Software License · rank 2736 · last release 2026-06-12 · [PyPI](https://pypi.org/project/chex/) · [docs](https://chex.readthedocs.io/) · [source](https://github.com/google-deepmind/chex)

<details><summary>README extract</summary>

<!-- disableFinding(SNIPPET_INVALID_LANGUAGE) -->

Chex is a library of utilities for helping to write reliable JAX code.

This includes utils to help:

* Instrument your code (e.g. assertions, warnings)
* Debug (e.g. transforming `pmaps` in `vmaps` within a context manager).
* Test JAX code across many `variants` (e.g. jitted vs non-jitted).

Example:
```python
@chex.dataclass
class Parameters:
  x: chex.ArrayDevice
  y: chex.ArrayDevice

parameters = Parameters(
    x=jnp.ones((2, 2)),
    y=jnp.ones((1, 2)),
)

# Dataclasses can be treated as JAX pytrees
jax.tree_util.tree_map(lambda x: 2.0 * x, parameters)

# and as mappings by dm-tree
tree.flatten(parameters)
```

...

</details>

### llama-index

Interface between LLMs and your data

`pip install llama-index` · installs (wheel) · licence: MIT · rank 2737 · last release 2026-09-21 · [PyPI](https://pypi.org/project/llama-index/) · [docs](https://docs.llamaindex.ai/en/stable/) · [source](https://github.com/run-llama/llama_index)

<details><summary>README extract</summary>

> [!NOTE]
> The current focus of LlamaIndex is to build the best AI-powered engine for document parsing and extraction. LlamaParse is our enterprise platform for agentic OCR, parsing, extraction, indexing and more. LiteParse represents our efforts to build the best free, fast, cheap text parser in the market. ...

Example:
```python
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
index = VectorStoreIndex.from_documents(documents)
```

...

</details>

### vllm

A high-throughput and memory-efficient inference and serving engine for LLMs

`pip install vllm` · installs (wheel) · licence: Apache-2.0 · rank 2774 · last release 2026-11-02 · [PyPI](https://pypi.org/project/vllm/) · [docs](https://docs.vllm.ai/en/latest/)

<details><summary>README extract</summary>

| Documentation | Blog | Paper | Twitter/X | User Forum | Developer Slack |

🔥 We have built a vLLM website to help you get started with vLLM. Please visit vllm.ai to learn more.
For events, please visit vllm.ai/events to join us.

vLLM is a fast and easy-to-use library for LLM inference and serving. ...

Sections: Easy, fast, and cheap LLM serving for everyone, About, Getting Started, Contact Us, Media Kit

</details>

### humming-kernels

JIT-compiled GPU GEMM kernels for quantized inference

`pip install humming-kernels` · installs (wheel) · licence: Apache-2.0 · rank 2817 · last release 2026-10-30 · [PyPI](https://pypi.org/project/humming-kernels/) · [docs](https://github.com/vllm-project/humming/tree/main/docs) · [source](https://github.com/vllm-project/humming)

<details><summary>README extract</summary>

Humming is a high-performance, lightweight, and highly flexible JIT (Just-In-Time) compiled GEMM kernel library specifically designed for quantized inference.

Features:
- High Flexibility
 - Supports inference for any weight type under 8-bit across FP16 / BF16 / FP8 / FP4 / INT8 / INT4 activations (provided the activation's dynamic range covers the weight type).
 - Supports various quantization strategies. ...

Example:
```python
import torch
from humming.layer import HummingLayer

layer = HummingLayer(
    shape_n=8192,
    shape_k=8192,
    weight_config={"dtype": "int6"},
    torch_dtype=torch.float16,
).cuda()

weight = torch.randn((8192, 8192), dtype=torch.float16, device="cuda:0")
inputs = torch.randn((128, 8192), dtype=torch.float16, device="cuda:0")

...
```

...

</details>

### verifiers

Verifiers: Environments for LLM Reinforcement Learning

`pip install verifiers` · installs (wheel) · licence: MIT · rank 2820 · last release 2026-11-03 · [PyPI](https://pypi.org/project/verifiers/) · [docs](https://github.com/primeintellect-ai/verifiers) · [source](https://github.com/primeintellect-ai/verifiers.git)

<details><summary>README extract</summary>

Features:
verifiers is our library for creating environments to train and evaluate LLMs.

verifiers is tightly integrated with the Environments Hub, as well as our training framework prime-rl and our Hosted Training platform.

Sections: Overview, Further reading, Pre-commit hooks, Tests

</details>

### langchain-ollama

An integration package connecting Ollama and LangChain

`pip install langchain-ollama` · installs (wheel) · licence: MIT License · rank 2851 · last release 2026-04-07 · [PyPI](https://pypi.org/project/langchain-ollama/) · [docs](https://reference.langchain.com/python/integrations/langchain_ollama/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-ollama, 🤔 What is this?, 📖 Documentation

</details>

### agno

The programming language for agentic software.

`pip install agno` · installs (wheel) · licence: Apache Software License · rank 2885 · last release 2026-10-29 · [PyPI](https://pypi.org/project/agno/) · [docs](https://docs.agno.com) · [source](https://github.com/agno-agi/agno)

<details><summary>README extract</summary>

The self-driving agent platform

Agno is a self-driving agent platform. Build agents for your product, your company, or your customers. Run them as durable services on AgentOS. Put them to work automating company operations.

- Build agents with the Agno, Claude Agent, or Codex SDKs. Combine agents into teams and workflows. ...

Sections: Introduction, Get started, Templates for every cloud, What's included, Tutorials, Telemetry

</details>

### pytorch-metric-learning

Composable metric learning losses, miners, distances, samplers, and retrieval metrics for PyTorch.

`pip install pytorch-metric-learning` · installs (wheel) · licence: MIT · rank 2901 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pytorch-metric-learning/) · [docs](https://kevinmusgrave.github.io/pytorch-metric-learning/) · [source](https://github.com/KevinMusgrave/pytorch-metric-learning)

<details><summary>README extract</summary>

Train embedding models with composable PyTorch losses, hard-example miners,
distances, reducers, and regularizers. Use them in your own training loop for
retrieval, clustering, recognition, or learning from pairs and triplets.

Docs for humans ·
Documentation source

Example:
```python
import torch
from pytorch_metric_learning import losses

torch.manual_seed(17)
model = torch.nn.Linear(8, 4)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
data = torch.randn(12, 8)
labels = torch.arange(4).repeat_interleave(3)
loss_func = losses.ContrastiveLoss(neg_margin=1.4)

optimizer.zero_grad(set_to_none=True)
...
```

Sections: A minimal training step, Learn more, Citing this library

</details>

### albucore

High-performance image processing functions for deep learning and computer vision.

`pip install albucore` · installs (wheel) · licence: MIT · rank 2944 · last release 2026-11-05 · [PyPI](https://pypi.org/project/albucore/)

<details><summary>README extract</summary>

Albucore is a library of optimized atomic functions designed for efficient image processing. These functions serve as the foundation for AlbumentationsX, an image augmentation library.

If you use Albucore as part of an AlbumentationsX pipeline, please cite
AlbumentationsX: One Augmentation Pipeline for Images and Related Annotations. ...

Features:
Image processing operations can be implemented in several ways, with performance depending on dtype, size, layout, and channel count. ...

Example:
```python
import numpy as np
import albucore

image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
result = albucore.multiply(image, 1.5)

# Grayscale images keep an explicit channel dimension
gray_image = np.random.randint(0, 256, (100, 100, 1), dtype=np.uint8)
...

</details>

### rerun-sdk

The Rerun Logging SDK

`pip install rerun-sdk` · installs (wheel) · licence: not stated · rank 3257 · last release 2026-11-04 · [PyPI](https://pypi.org/project/rerun-sdk/) · [docs](https://www.rerun.io/docs) · [source](https://github.com/rerun-io/rerun)

<details><summary>README extract</summary>

The data primitives to build, understand, and improve your data loop.
Designed for multi-rate, multimodal data, from the first recording to massive scale.

The open source Rerun Python SDK provides a single toolchain to log, transform, query, view, and train on multi-rate, multimodal data.

Example:
```python
import numpy as np
import rerun as rr

rr.init("rerun_example_app", spawn=True)

positions = np.vstack([xyz.ravel() for xyz in np.mgrid[3 * [slice(-5, 5, 10j)]]]).T
colors = np.vstack([rgb.ravel() for rgb in np.mgrid[3 * [slice(0, 255, 10j)]]]).astype(np.uint8).T

rr.log("points3d", rr.Points3D(positions, colors=colors))
```

...

</details>

### equinox

Elegant easy-to-use neural networks in JAX.

`pip install equinox` · installs (wheel) · licence: Apache Software License · rank 3293 · last release 2026-05-05 · [PyPI](https://pypi.org/project/equinox/) · [source](https://github.com/patrick-kidger/equinox)

<details><summary>README extract</summary>

Equinox is your one-stop JAX library, for everything you need that isn't already in core JAX:

- neural networks (or more generally any model), with easy-to-use PyTorch-like syntax;
- filtered APIs for transformations;
- useful PyTree manipulation routines;
- advanced features like runtime errors; ...

Example:
```python
import equinox as eqx
import jax

class Linear(eqx.Module):
    weight: jax.Array
    bias: jax.Array

    def init(self, in_size, out_size, key):
        wkey, bkey = jax.random.split(key)
        self.weight = jax.random.normal(wkey, (out_size, in_size))
        self.bias = jax.random.normal(bkey, (out_size,))

    def call(self, x):
...
```

Sections: Equinox, Documentation, Quick example, See also: other libraries in the JAX ecosystem

</details>

### tensorflow-metadata

Library and standards for schema and statistics.

`pip install tensorflow-metadata` · installs (wheel) · licence: Apache Software License · rank 3380 · last release 2026-06-09 · [PyPI](https://pypi.org/project/tensorflow-metadata/)

<details><summary>README extract</summary>

TensorFlow Metadata provides standard representations for metadata that are
useful when training machine learning models with TensorFlow.

The metadata serialization formats include:

* A schema describing tabular data (e.g., tf.Examples).
* A collection of summary statistics over such datasets. ...

</details>

### chonkie

🦛 CHONK your texts with Chonkie ✨ - The no-nonsense chunking library

`pip install chonkie` · installs (wheel) · licence: not stated · rank 3412 · last release 2026-07-07 · [PyPI](https://pypi.org/project/chonkie/) · [docs](https://docs.chonkie.ai)

<details><summary>README extract</summary>

_The lightweight ingestion library for fast, efficient and robust RAG pipelines

Installation •
Usage •
Chunkers •
Integrations •
Benchmarks

Tired of making your gazillionth chunker? Sick of the overhead of large libraries? Want to chunk your texts quickly and efficiently? Chonkie the mighty hippo is here to help! ...

Example:
```python
# First import the chunker you want from Chonkie
from chonkie import RecursiveChunker

# Initialize the chunker
chunker = RecursiveChunker()

# Chunk some text
chunks = chunker("Chonkie is the goodest boi! My favorite chunking hippo hehe.")

# Access chunks
for chunk in chunks:
    print(f"Chunk: {chunk.text}")
...
```

...

</details>

### model2vec

Fast State-of-the-Art Static Embeddings

`pip install model2vec` · installs (wheel) · licence: MIT License · rank 3473 · last release 2026-10-11 · [PyPI](https://pypi.org/project/model2vec/) · [source](https://github.com/MinishLab/model2vec)

<details><summary>README extract</summary>

Fast State-of-the-Art Static Embeddings

Quickstart • Main Features • Model List • Results

Model2Vec is a technique to turn any sentence transformer into a small, fast static embedding model. Model2Vec reduces model size by a factor up to 50 and makes models up to 500 times faster, with a small drop in performance. ...

Example:
```python
from model2vec import StaticModel

# Load a model from the HuggingFace hub (in this case the potion-base-32M model)
model = StaticModel.from_pretrained("minishlab/potion-base-32M")

# Make embeddings
embeddings = model.encode(["It's dangerous to go alone!", "It's a secret to everybody."])

# Make sequences of token embeddings
...
```

Sections: Quickstart, Main Features, What is Model2Vec?, Documentation, Model List, Results, Citing

</details>

### optimum

Optimum Library is an extension of the Hugging Face Transformers library, providing a framework to integrate third-party libraries from Hardware Partners and interface with their specific functionality.

`pip install optimum` · installs (wheel) · licence: Apache Software License · rank 3497 · last release 2026-08-04 · [PyPI](https://pypi.org/project/optimum/)

<details><summary>README extract</summary>

Optimum is an extension of Transformers 🤖 Diffusers 🧨 TIMM 🖼️ and Sentence-Transformers 🤗, providing a set of optimization tools and enabling maximum efficiency to train and run models on targeted hardware, while keeping things easy to use.

Sections: 🤗 Optimum, Accelerated Inference, ONNX + ONNX Runtime, Intel (OpenVINO + NNCF), ExecuTorch, Quanto, Accelerated training, Intel Gaudi Accelerators, AWS Trainium

</details>

### webrtcvad-wheels

Python interface to the Google WebRTC Voice Activity Detector (VAD) [released with binary wheels!]

`pip install webrtcvad-wheels` · installs (wheel) · licence: MIT License · rank 3535 · last release 2026-10-02 · [PyPI](https://pypi.org/project/webrtcvad-wheels/)

<details><summary>README extract</summary>

This is a python interface to the WebRTC Voice Activity Detector (VAD).
It is forked from
wiseman/py-webrtcvad to
provide updated releases with **binary wheels for Windows, macOS, and
Linux. Also includes additional fixes and improvements**.

A VAD
classifies a piece of audio data as being voiced or unvoiced. ...

Example:
```python
import webrtcvad
vad = webrtcvad.Vad()
```

Sections: py-webrtcvad-wheels, How to use it, How to run unit tests

</details>

### torchdata

Composable data loading modules for PyTorch

`pip install torchdata` · installs (wheel) · licence: BSD License · rank 3582 · last release 2025-02-20 · [PyPI](https://pypi.org/project/torchdata/)

<details><summary>README extract</summary>

Sections: #, What is TorchData?, Stateful DataLoader, torchdata.nodes, Version Compatibility, Local pip or conda, From source, From nightly, Beta Usage and Feedback

</details>

### outlines

Probabilistic Generative Model Programming

`pip install outlines` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 3587 · last release 2026-08-06 · [PyPI](https://pypi.org/project/outlines/) · [docs](https://dottxt-ai.github.io/outlines/) · [source](https://github.com/dottxt-ai/outlines)

<details><summary>README extract</summary>

🗒️ *Structured outputs for LLMs* 🗒️

Made with ❤👷️ by the team at .txt

Trusted by NVIDIA, Cohere, HuggingFace, vLLM, etc.

[][pypi]
[][pypistats]
[][stars]

[][discord]
[][dottxt-blog]
[][twitter]

The .txt API is currently in early access. Request access here → ...

Features:
LLMs are powerful but their outputs are unpredictable. Most solutions attempt to fix bad outputs after generation using parsing, regex, or fragile code that breaks easily. ...

Example:
```python
import outlines
from enum import Enum
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
...
```

...

</details>

### qwen-vl-utils

Qwen Vision Language Model Utils - PyTorch

`pip install qwen-vl-utils` · installs (wheel) · licence: Apache Software License · rank 3589 · last release 2025-09-23 · [PyPI](https://pypi.org/project/qwen-vl-utils/) · [source](https://github.com/QwenLM/Qwen2-VL.git)

<details><summary>README extract</summary>

Qwen-VL Utils contains a set of helper functions for processing and integrating visual language information with Qwen-VL Series Model.

Example:
```python
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

# You can directly insert a local file path, a URL, or a base64-encoded image into the position where you want in the text.
messages = [
    # Image
    ## Local file path
...
```

Sections: qwen-vl-utils, Usage, Qwen2VL, Qwen2.5VL, Qwen3VL

</details>

### azureml-mlflow

Contains the integration code of AzureML with Mlflow.

`pip install azureml-mlflow` · installs (wheel) · licence: MIT License · rank 3619 · last release 2026-09-02 · [PyPI](https://pypi.org/project/azureml-mlflow/)

<details><summary>README extract</summary>

The azureml-mlflow package contains the integration code of AzureML with MLflow.
MLflow ( is an open-source platform for tracking machine learning experiments and managing models.
You can use MLflow logging APIs with Azure Machine Learning so that metrics and artifacts are logged to your Azure
machine learning workspace.

Example:
```python
import mlflow
from azureml.core import Workspace

workspace = Workspace.from_config()

mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())
```

</details>

### yacs

Yet Another Configuration System

`pip install yacs` · installs (wheel) · licence: Apache Software License · rank 3637 · last release 2020-08-10 · [PyPI](https://pypi.org/project/yacs/)

<details><summary>README extract</summary>

A simple experiment configuration system for research

</details>

### langchain-groq

An integration package connecting Groq and LangChain

`pip install langchain-groq` · installs (wheel) · licence: MIT License · rank 3768 · last release 2026-06-10 · [PyPI](https://pypi.org/project/langchain-groq/) · [docs](https://reference.langchain.com/python/integrations/langchain_groq/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-groq, 📖 Documentation

</details>

### botframework-connector

Microsoft Bot Framework Bot Builder SDK for Python.

`pip install botframework-connector` · installs (wheel) · licence: MIT License · rank 3814 · last release 2026-01-05 · [PyPI](https://pypi.org/project/botframework-connector/)

<details><summary>README extract</summary>

Within the Bot Framework, the Bot Connector service enables your bot to exchange messages with users on channels that are configured in the Bot Framework Portal.

Example:
```python
from botbuilder.schema import *
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials

APP_ID = '<your-app-id>'
APP_PASSWORD = '<your-app-password>'
SERVICE_URL = '
CHANNEL_ID = 'slack'
BOT_ID = '<bot-id>'
RECIPIENT_ID = '<user-id>'

...
```

Sections: Microsoft Bot Framework Connector for Python, How to Use, Authentication, Example, Rest API Documentation, Documentation/Wiki, Requirements, Source Code

</details>

### botbuilder-schema

BotBuilder Schema

`pip install botbuilder-schema` · installs (wheel) · licence: MIT License · rank 3828 · last release 2026-01-05 · [PyPI](https://pypi.org/project/botbuilder-schema/)

<details><summary>README extract</summary>

BotBuilder-schema contains the serialized data sent across the wire between user and bot when using Bot Framework.

Sections: BotBuilder-Schema, Documentation/Wiki, Requirements, Source Code

</details>

### langchain-litellm

An integration package connecting LiteLLM and LangChain

`pip install langchain-litellm` · installs (wheel) · licence: MIT License · rank 3878 · last release 2026-10-25 · [PyPI](https://pypi.org/project/langchain-litellm/) · [docs](https://docs.langchain.com/oss/python/integrations/chat/litellm) · [source](https://github.com/langchain-ai/langchain-litellm)

<details><summary>README extract</summary>

📦 Distribution
🔧 Project
🚀 Activity

This package contains the LangChain integration with LiteLLM. LiteLLM is a library that simplifies calling Anthropic, Azure, Huggingface, Replicate, etc.

For conceptual guides, tutorials, and examples on using these classes, see the LangChain Docs.

Sections: langchain-litellm, 🤔 What is this?, 📖 Documentation

</details>

### agnoctl

The Agno CLI: connect and operate AgentOS from the terminal, built for humans and coding agents

`pip install agnoctl` · installs (wheel) · licence: Apache Software License · rank 3879 · last release 2026-09-16 · [PyPI](https://pypi.org/project/agnoctl/) · [docs](https://docs.agno.com) · [source](https://github.com/agno-agi/agno)

<details><summary>README extract</summary>

The CLI for AgentOS, built for humans and coding agents.

Create a new AgentOS interactively:

Choose from nine maintained starters—Docker, AWS, Azure, Fly, GCP, Helm, Modal,
Railway, and Render—using the arrow keys or `1`–`9`, then name your project.
Press Enter to use `agentos-docker` and `agent-platform`. ...

</details>

### botbuilder-core

Microsoft Bot Framework Bot Builder

`pip install botbuilder-core` · installs (wheel) · licence: MIT License · rank 3904 · last release 2026-01-05 · [PyPI](https://pypi.org/project/botbuilder-core/)

<details><summary>README extract</summary>

Within the Bot Framework, BotBuilder-core enables you to build bots that exchange messages with users on channels that are configured in the Bot Framework Portal.

Sections: BotBuilder-Core SDK for Python, Documentation/Wiki, Requirements, Source Code

</details>

### botframework-streaming

Microsoft Bot Framework Bot Builder

`pip install botframework-streaming` · installs (wheel) · licence: MIT License · rank 3911 · last release 2026-01-05 · [PyPI](https://pypi.org/project/botframework-streaming/)

<details><summary>README extract</summary>

Streaming Extensions libraries for BotFramework.

Sections: BotFramework-Streaming for Python, Documentation/Wiki, Requirements, Source Code

</details>

### langchain-huggingface

An integration package connecting Hugging Face and LangChain.

`pip install langchain-huggingface` · installs (wheel) · licence: MIT License · rank 4152 · last release 2026-10-07 · [PyPI](https://pypi.org/project/langchain-huggingface/) · [docs](https://reference.langchain.com/python/integrations/langchain_huggingface/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-huggingface, 🤔 What is this?, 📖 Documentation, Resources

</details>

### langchain-mistralai

An integration package connecting Mistral and LangChain

`pip install langchain-mistralai` · installs (wheel) · licence: MIT License · rank 4198 · last release 2026-07-05 · [PyPI](https://pypi.org/project/langchain-mistralai/) · [docs](https://reference.langchain.com/python/integrations/langchain_mistralai/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-mistralai, 📖 Documentation, Resources

</details>

### neptune-api

A client library for accessing Neptune API

`pip install neptune-api` · installs (wheel) · licence: Apache Software License · rank 4346 · last release 2026-01-07 · [PyPI](https://pypi.org/project/neptune-api/) · [docs](https://docs.neptune.ai/) · [source](https://github.com/neptune-ai/neptune-api)

<details><summary>README extract</summary>

A client library for accessing Neptune API

Example:
```python
from neptune_api import Client

client = Client(base_url="
```

Sections: neptune-api, Usage, Update OpenAPI spec

</details>

### neptune-fetcher

Neptune Fetcher (DEPRECATED - use neptune-query instead)

`pip install neptune-fetcher` · installs (wheel) · licence: Apache Software License · rank 4382 · last release 2025-09-18 · [PyPI](https://pypi.org/project/neptune-fetcher/) · [docs](https://docs.neptune.ai/fetcher_setup) · [source](https://github.com/neptune-ai/neptune-fetcher)

<details><summary>README extract</summary>

> [!IMPORTANT]
> This package is deprecated and no longer actively developed.
> Use `neptune-query` instead:
> ```bash
> pip uninstall -y neptune-fetcher && pip install "neptune-query>=1.0.0,<2.0.0"
> ```
> For instructions, see the migration guide.

Neptune Fetcher is a read-only API for querying metadata logged with the Neptune Python client. ...

Example:
```python
import neptune_fetcher.alpha as npt
```

Sections: Neptune Fetcher [DEPRECATED], Documentation, Usage, Old Fetcher API

</details>

### fastmcp-tasks

Background task execution for FastMCP servers via the io.modelcontextprotocol/tasks extension (SEP-2663).

`pip install fastmcp-tasks` · installs (wheel) · licence: Apache-2.0 · rank 4421 · last release 2026-11-03 · [PyPI](https://pypi.org/project/fastmcp-tasks/) · [docs](https://gofastmcp.com) · [source](https://github.com/PrefectHQ/fastmcp)

<details><summary>README extract</summary>

A complete implementation of background tasks for the Model Context Protocol — the `io.modelcontextprotocol/tasks` extension defined in SEP-2663.

The MCP tasks extension is a Final SEP, but as of this writing it ships in the ecosystem as a schema and a prose specification — no language SDK provides a working runtime for it. ...

Example:
```python
from fastmcp import FastMCP
from fastmcp_tasks import TasksExtension

mcp = FastMCP("Analytics")
mcp.add_extension(TasksExtension(url="redis://localhost:6379/0"))

@mcp.tool(task=True)
async def analyze(dataset: str) -> str:
    # Long-running work. The client gets a task handle immediately and
...
```

Sections: fastmcp-tasks, What background tasks are, Usage, Running out-of-process workers, Configuration

</details>

### problog

ProbLog2: Probabilistic Logic Programming toolbox

`pip install problog` · installs (wheel) · licence: Apache-2.0 · rank 4511 · last release 2026-09-09 · [PyPI](https://pypi.org/project/problog/)

<details><summary>README extract</summary>

ProbLog 2 is a Probabilistic Logic Programming toolbox.
It allows to intuitively build programs that do not only encode complex interactions between a large sets of heterogenous components,
but also the inherent uncertainties that are present in real-life situations. ...

Sections: ProbLog, Python

</details>

### prime-traces

Prime Intellect Traces SDK - Upload, query and export traces

`pip install prime-traces` · installs (wheel) · licence: MIT License · rank 4517 · last release 2026-11-02 · [PyPI](https://pypi.org/project/prime-traces/) · [docs](https://github.com/PrimeIntellect-ai/prime/tree/main/packages/prime-traces) · [source](https://github.com/PrimeIntellect-ai/prime.git)

<details><summary>README extract</summary>

Upload and query training, evaluation and inference traces through the Prime
Traces service.

Example:
```python
from prime_traces import LineFormat, TracesClient

client = TracesClient()  # PRIME_API_KEY / PRIME_TRACES_URL / ~/.prime/config.json

receipts = client.upload_records(traces, context={"source": "prime-rl"})

# One complete episode per record, for multi-agent runs
receipts = client.upload_records(episodes, line_format=LineFormat.EPISODE)

...
```

Sections: Prime Traces SDK, Upload, Query, Search indexed content, Async, Configuration, Not yet available, Examples, Related packages

</details>

### inspect-evals

Collection of large language model evaluations

`pip install inspect-evals` · installs (wheel) · licence: MIT · rank 4542 · last release 2026-10-30 · [PyPI](https://pypi.org/project/inspect-evals/) · [docs](https://ukgovernmentbeis.github.io/inspect_evals/) · [source](https://github.com/UKGovernmentBEIS/inspect_evals)

<details><summary>README extract</summary>

A library of evaluations built using Inspect AI.

Example:
```python
from inspect_ai import eval, eval_set
from inspect_evals.arc import arc_easy, arc_challenge
eval(arc_easy)
eval_set([arc_easy, arc_challenge], log_dir='logs-run-42')
```

Sections: Explore evaluations and read the docs →, Quick start, About the project, Getting started, Usage, Running evaluations, Documentation, Hardware recommendations, Disk, Cache location, RAM, Harbor Framework Evaluations

</details>

### prime-runs

Prime Intellect Runs SDK - Track eval and training runs on the Prime platform

`pip install prime-runs` · installs (wheel) · licence: MIT License · rank 4568 · last release 2026-11-02 · [PyPI](https://pypi.org/project/prime-runs/) · [docs](https://github.com/PrimeIntellect-ai/prime/tree/main/packages/prime-runs) · [source](https://github.com/PrimeIntellect-ai/prime.git)

<details><summary>README extract</summary>

Track evaluation and training runs on the Prime Intellect platform: `init()`
opens the run, records stream out while it proceeds, and `finish()` closes it
out with a terminal status.

Example:
```python
import prime_runs as pr

run = pr.init(
    name="gsm8k-qwen3-8b",
    environments=["gsm8k"],      # hub names (get-or-create) or owner/name slugs
    model="Qwen/Qwen3-8B",
    framework="verifiers",
    config="eval.toml",          # the launched file, stored byte for byte
)
print(run.url)                   #

for episode in rollouts:
...
```

Sections: Prime Runs SDK, Eval runs, Training runs, How it behaves, Opting out of Prime Traces, Configuration, Related packages

</details>

### xformers

XFormers: A collection of composable Transformer building blocks.

`pip install xformers` · installs (wheel) · licence: BSD License · rank 4589 · last release 2026-02-20 · [PyPI](https://pypi.org/project/xformers/)

<details><summary>README extract</summary>

XFormers: A collection of composable Transformer building blocks.XFormers aims at being able to reproduce most architectures in the Transformer-family SOTA,defined as compatible and combined building blocks as opposed to monolithic models

</details>

### langchain-openrouter

An integration package connecting OpenRouter and LangChain

`pip install langchain-openrouter` · installs (wheel) · licence: MIT License · rank 4607 · last release 2026-09-22 · [PyPI](https://pypi.org/project/langchain-openrouter/) · [docs](https://reference.langchain.com/python/integrations/langchain_openrouter/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Sections: langchain-openrouter, 🤔 What is this?, 📖 Documentation, Resources

</details>

### langchain-xai

An integration package connecting xAI and LangChain

`pip install langchain-xai` · installs (wheel) · licence: MIT License · rank 4621 · last release 2026-07-21 · [PyPI](https://pypi.org/project/langchain-xai/) · [docs](https://reference.langchain.com/python/integrations/langchain_xai/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-xai, 🤔 What is this?, 📖 Documentation, Resources

</details>

### py3langid

Fork of the language identification tool langid.py, featuring a modernized codebase and faster execution times.

`pip install py3langid` · installs (wheel) · licence: BSD-3-Clause · rank 4628 · last release 2026-09-02 · [PyPI](https://pypi.org/project/py3langid/)

<details><summary>README extract</summary>

`py3langid` is a fork of the standalone language identification tool `langid.py` by Marco Lui.

Original license: BSD-2-Clause. Fork license: BSD-3-Clause.

Execution speed has been improved and the code base has been modernized for Python 3.10+:

- Import: Loading the package (`import py3langid`) is about 25% faster ...

Example:
```python
>>> import py3langid as langid

>>> langid.classify('This text is in English.')
('en', -68.562286)
>>> langid.rank('This text is in English.')   # all languages, most likely first

>>> from py3langid.langid import LanguageIdentifier, MODEL_FILE
>>> identifier = LanguageIdentifier.from_model_file(MODEL_FILE, norm_probs=True)
...
```

...

</details>

### chronos-forecasting

Chronos: Pretrained models for time series forecasting

`pip install chronos-forecasting` · installs (wheel) · licence: Apache Software License · rank 4644 · last release 2026-09-08 · [PyPI](https://pypi.org/project/chronos-forecasting/)

<details><summary>README extract</summary>

- 5 Jun 2026: ☁️ Deploy Chronos-2 to AWS with AutoGluon-Cloud — real-time, serverless, or batch inference in 3 lines of code, pandas DataFrames in, forecasts out. See the new deployment guide. ...

Example:
```python
import pandas as pd  # requires: pip install 'pandas[pyarrow]'
from chronos import Chronos2Pipeline

pipeline = Chronos2Pipeline.from_pretrained("amazon/chronos-2", device_map="cuda")

# Load historical target values and past values of covariates
context_df = pd.read_parquet("

# (Optional) Load future values of covariates
...
```

Sections: Chronos: Pretrained Models for Time Series Forecasting, 🚀 News, ✨ Introduction, Available Models, 📈 Usage, Forecasting, Example Notebooks

</details>

### unsloth

2-5X faster training, reinforcement learning & finetuning

`pip install unsloth` · installs (wheel) · licence: Apache-2.0 · rank 4677 · last release 2026-11-06 · [PyPI](https://pypi.org/project/unsloth/) · [docs](https://unsloth.ai/docs) · [source](https://github.com/unslothai/unsloth)

<details><summary>README extract</summary>

Features •
 Quickstart •
 Notebooks •
 Documentation

Download the native Unsloth Desktop app for your operating system:

 Platform
 Link

 Windows
 Download

 macOS
 Download

 Linux / Ubuntu (deb)
 Download

 Linux / Ubuntu (ARM64) (deb)
 Download

 Linux (AppImage)
 Download

 Windows (ARM64)
 Download

Download from Unsloth or GitHub Releases. ...

Sections: Unsloth is the first desktop app to run and train models., ⚡ Get started, macOS, Linux, WSL, Windows, Docker, Homebrew, Winget (Windows), ⭐ Features, Run & Build with AI, Train & Deploy, 🚀 Unsloth Start, Unsloth Desktop (recommended), Unsloth Studio (web UI)

</details>

### pythainlp

Thai Natural Language Processing library

`pip install pythainlp` · installs (wheel) · licence: Apache-2.0 · rank 4702 · last release 2026-10-09 · [PyPI](https://pypi.org/project/pythainlp/) · [docs](https://pythainlp.org/docs/) · [source](https://github.com/PyThaiNLP/pythainlp.git)

<details><summary>README extract</summary>

pythainlp.org
| Tutorials
| License info
| Model cards
| Adopters
| *เอกสารภาษาไทย*

Designed to be a Thai-focused counterpart to NLTK,
PyThaiNLP provides standard tools for linguistic analysis under
an Apache-2.0 license, with its data and models covered by CC0-1.0
and CC-BY-4.0.

| Version | Python version | Changes | Documentation | ...

Features:
- Linguistic units: Sentence, word, and subword segmentation
 (`sent_tokenize`, `word_tokenize`, `subword_tokenize`).
- Tagging: Part-of-speech tagging (`pos_tag`).
- Transliteration: Romanization (`transliterate`) and IPA conversion. ...

Example:
```python
import pythainlp
print(pythainlp.is_offline_mode())  # True if PYTHAINLP_OFFLINE=1
```

...

</details>

### langchain-deepseek

An integration package connecting DeepSeek and LangChain

`pip install langchain-deepseek` · installs (wheel) · licence: MIT License · rank 4718 · last release 2026-09-22 · [PyPI](https://pypi.org/project/langchain-deepseek/) · [docs](https://reference.langchain.com/python/integrations/langchain_deepseek/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-deepseek, 🤔 What is this?, 📖 Documentation, Resources

</details>

### indic-numtowords

A module to convert numbers to words for Indian languages and English.

`pip install indic-numtowords` · installs (wheel) · licence: MIT License · rank 4768 · last release 2025-08-18 · [PyPI](https://pypi.org/project/indic-numtowords/) · [source](https://github.com/AI4Bharat/indic-numtowords)

<details><summary>README extract</summary>

> A module to convert numbers to words for Indian languages and English.

Sections: AI4Bharat num2words, Import, Usage, Parameters, Meta

</details>

### langid

langid.py is a standalone Language Identification (LangID) tool.

`pip install langid` · installs from source (sdist only) · licence: BSD License · rank 4785 · last release 2016-04-05 · [PyPI](https://pypi.org/project/langid/)

### bedrock-agentcore-starter-toolkit

A starter toolkit for using Bedrock AgentCore

`pip install bedrock-agentcore-starter-toolkit` · installs (wheel) · licence: Apache Software License · rank 4853 · last release 2026-10-06 · [PyPI](https://pypi.org/project/bedrock-agentcore-starter-toolkit/) · [docs](https://github.com/aws/bedrock-agentcore-starter-toolkit)

<details><summary>README extract</summary>

Documentation
 ◆ Samples
 ◆ Discord
 ◆ Boto3 Python SDK
 ◆ Runtime Python SDK
 ◆ Starter Toolkit

> ⚠️ Recommendation: The Starter Toolkit CLI is no longer supported. Please use the AgentCore CLI.
> The AgentCore CLI (`@aws/agentcore`) is now the recommended way to create, develop, and deploy AI agents on Amazon Bedrock AgentCore. ...

Features:
Amazon Bedrock AgentCore enables you to deploy and operate highly effective agents securely, at scale using any framework and model. ...

...

</details>

### browsergym-core

BrowserGym: a gym environment for web task automation in the Chromium browser

`pip install browsergym-core` · installs (wheel) · licence: Apache Software License · rank 4956 · last release 2026-01-20 · [PyPI](https://pypi.org/project/browsergym-core/)

<details><summary>README extract</summary>

This package provides `browsergym.core`, which provides the core functionalities of BrowserGym.

1. Install the package

Sections: BrowserGym core, Setup

</details>

### interpret-core

Fit interpretable models. Explain blackbox machine learning.

`pip install interpret-core` · installs (wheel) · licence: not stated · rank 4962 · last release 2026-03-17 · [PyPI](https://pypi.org/project/interpret-core/)

<details><summary>README extract</summary>

Minimal dependency core system for the interpret package.

</details>

### unstructured-inference

A library for performing inference using trained models.

`pip install unstructured-inference` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 4982 · last release 2026-10-28 · [PyPI](https://pypi.org/project/unstructured-inference/)

<details><summary>README extract</summary>

The `unstructured-inference` repo contains hosted model inference code for layout parsing models.
These models are invoked via API as part of the partitioning bricks in the `unstructured` package.

Requires Python >=3.11, <3.14.

Example:
```python
from unstructured_inference.inference.layout import DocumentLayout

layout = DocumentLayout.from_file("sample-docs/loremipsum.pdf")

print(layout.pages[0].elements)
```

Sections: Open-Source Pre-Processing Tools for Unstructured Data, Package, Detectron2, Getting Started, Models, Using a non-default model, Using your own model, Learn more

</details>

### tensorflow-datasets

tensorflow/datasets is a library of datasets ready to use with TensorFlow.

`pip install tensorflow-datasets` · installs (wheel) · licence: Apache Software License · rank 4991 · last release 2026-05-08 · [PyPI](https://pypi.org/project/tensorflow-datasets/)

<details><summary>README extract</summary>

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.

</details>

### kaldialign

Kaldi alignment methods wrapped into Python

`pip install kaldialign` · installs (wheel) · licence: Apache-2.0 · rank 5000 · last release 2026-06-15 · [PyPI](https://pypi.org/project/kaldialign/)

<details><summary>README extract</summary>

A small package that exposes edit distance computation functions from Kaldi. It uses the original Kaldi code and wraps it using pybind11.

Example:
```python
from kaldialign import align

EPS = '*'
a = ['a', 'b', 'c']
b = ['a', 's', 'x', 'c']
ali = align(a, b, EPS)
assert ali == [('a', 'a'), ('b', 's'), (EPS, 'x'), ('c', 'c')]
```

Sections: kaldialign, Examples, Alignment, Edit distance, Batch error rate, Compound word matching, Motivation

</details>

### rotary-embedding-torch

Rotary Embedding - Pytorch

`pip install rotary-embedding-torch` · installs (wheel) · licence: MIT License · rank 5002 · last release 2026-11-07 · [PyPI](https://pypi.org/project/rotary-embedding-torch/)

<details><summary>README extract</summary>

A standalone library for adding rotary embeddings to transformers in Pytorch, following its success as relative positional encoding. Specifically it will make rotating information into any axis of a tensor easy and efficient, whether they be fixed positional or learned. ...

Example:
```python
import torch
from rotary_embedding_torch import RotaryEmbedding

# instantiate the positional embedding in your transformer and pass to all your attention layers

rotary_emb = RotaryEmbedding(dim = 32)

# mock queries and keys - dimensions should end with (seq_len, feature dimension), and any number of preceding dimensions (batch, heads, etc)

...
```

...

</details>

### llama-index-legacy

Interface between LLMs and your data

`pip install llama-index-legacy` · installs (wheel) · licence: MIT License · rank 5069 · last release 2024-11-07 · [PyPI](https://pypi.org/project/llama-index-legacy/) · [docs](https://docs.llamaindex.ai/en/stable/) · [source](https://github.com/run-llama/llama_index)

<details><summary>README extract</summary>

LlamaIndex (GPT Index) is a data framework for your LLM application.

PyPI:

LlamaIndex.TS (Typescript/Javascript):

Documentation:

Twitter:

Discord:

NOTE: This README is not updated as frequently as the documentation. Please check out the documentation above for the latest updates!

Example:
```python
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

from llama_index.legacy.legacy import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
index = VectorStoreIndex.from_documents(documents)
```

Sections: 🗂️ LlamaIndex 🦙, Ecosystem, 🚀 Overview, Context, Proposed Solution, 📄 Documentation, 💻 Example Usage, 🔧 Dependencies

</details>

### clearml

ClearML - Auto-Magical Experiment Manager, Version Control, and MLOps for AI

`pip install clearml` · installs (wheel) · licence: Apache Software License · rank 5082 · last release 2026-11-03 · [PyPI](https://pypi.org/project/clearml/)

<details><summary>README extract</summary>

**ClearML - Auto-Magical Suite of tools to streamline your AI workflow
Experiment Manager, MLOps/LLMOps and Data-Management**

`🌟 ClearML is open-source - Leave a star to support the project! 🌟`

ClearML is a ML/DL development and production suite. It contains FIVE main modules: ...

Features:
ClearML is our solution to a problem we share with countless other researchers and developers in the machine
learning/deep learning universe: Training production-grade deep learning models is a glorious but messy process. ...

Example:
```python
from clearml import Task
task = Task.init(project_name='examples', task_name='hello world')
```

Sections: ClearML, ClearML Experiment Manager, Start using ClearML, ClearML Architecture, Additional Modules, Why ClearML?, Who We Are

</details>

### webrtcvad

Python interface to the Google WebRTC Voice Activity Detector (VAD)

`pip install webrtcvad` · installs from source (sdist only) · licence: MIT License · rank 5085 · last release 2017-01-07 · [PyPI](https://pypi.org/project/webrtcvad/)

<details><summary>README extract</summary>

This is a python interface to the WebRTC Voice Activity Detector
(VAD). It is compatible with Python 2 and Python 3.

A VAD
classifies a piece of audio data as being voiced or unvoiced. It can
be useful for telephony and speech recognition. ...

Example:
```python
import webrtcvad
vad = webrtcvad.Vad()
```

Sections: py-webrtcvad, How to use it, How to run unit tests

</details>

### wandb-workspaces

A library for programatically working with the Weights & Biases UI.

`pip install wandb-workspaces` · installs (wheel) · licence: Apache-2.0 · rank 5115 · last release 2026-10-06 · [PyPI](https://pypi.org/project/wandb-workspaces/) · [docs](https://docs.wandb.ai/ref/wandb_workspaces/) · [source](https://github.com/wandb/wandb-workspaces)

<details><summary>README extract</summary>

`wandb-workspaces` is a Python library for programatically working with Weights & Biases workspaces and reports. This feature is in Public Preview.

Example:
```python
import wandb_workspaces.workspaces as ws
import wandb_workspaces.reports.v2 as wr

workspace = ws.Workspace(
   name="Example W&B Workspace",
   entity="your-entity",
   project="your-project",
   sections=[
      ws.Section(
            name="Validation Metrics",
            panels=[
               wr.LinePlot(x="Step", y=["val_loss"]),
...
```

Sections: wandb-workspaces, Quickstart, 2. Create a workspace, 3. Create a report, More examples

</details>

### langchain-fireworks

An integration package connecting Fireworks and LangChain

`pip install langchain-fireworks` · installs (wheel) · licence: MIT License · rank 5147 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain-fireworks/) · [docs](https://reference.langchain.com/python/integrations/langchain_fireworks/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-fireworks, 🤔 What is this?, 📖 Documentation, Resources

</details>

### onnxslim

OnnxSlim: A Toolkit to Help Optimize Onnx Model

`pip install onnxslim` · installs (wheel) · licence: MIT · rank 5148 · last release 2026-11-04 · [PyPI](https://pypi.org/project/onnxslim/)

<details><summary>README extract</summary>

OnnxSlim can help you slim your onnx model, with less operators, but same accuracy, better inference speed.

- 🚀 2026/06/02: Achieved 10M downloads
- 🚀 2026/01/04: Achieved 5M downloads
- 🚀 2025/11/29: Top 1% on PyPI
- 🚀 2025/11/27: OnnxSlim is merged into NVIDIA TensorRT-Model-Optimizer 🤗🤗🤗 ...

Sections: Using Prebuilt, How to use, Bash, Inscript, Projects using OnnxSlim, References, Contact

</details>

### jaxopt

Hardware accelerated, batchable and differentiable optimizers in JAX.

`pip install jaxopt` · installs (wheel) · licence: Apache Software License · rank 5179 · last release 2025-04-14 · [PyPI](https://pypi.org/project/jaxopt/)

<details><summary>README extract</summary>

Status
| Installation
| Documentation
| Examples
| Cite us

Hardware accelerated, batchable and differentiable optimizers in
JAX.

- Hardware accelerated: our implementations run on GPU and TPU, in addition
 to CPU.
- Batchable: multiple instances of the same optimization problem can be
 automatically vectorized using JAX's vmap. ...

Sections: JAXopt, Disclaimer

</details>

### tokie

Blazingly fast tokenizer — 50x faster, 10x smaller, 100% accurate

`pip install tokie` · installs (wheel) · licence: Apache Software License; MIT License · rank 5235 · last release 2026-07-24 · [PyPI](https://pypi.org/project/tokie/) · [docs](https://docs.rs/tokie) · [source](https://github.com/chonkie-inc/tokie)

<details><summary>README extract</summary>

10-136x faster tokenization, 10x smaller model files, 100% accurate

 GitHub · crates.io · HuggingFace

tokie is a fast, correct tokenizer library built in Rust with Python bindings. Drop-in replacement for HuggingFace tokenizers — supports BPE (GPT-2, tiktoken, SentencePiece), WordPiece (BERT), and Unigram encoders.

Example:
```python
import tokie

# Load from HuggingFace Hub (tries .tkz first, falls back to tokenizer.json)
tokenizer = tokie.Tokenizer.from_pretrained("bert-base-uncased")

# Encode — callable syntax or .encode()
encoding = tokenizer("Hello, world!")
print(encoding.ids)               # [101, 7592, 1010, 2088, 999, 102]
...
```

Sections: Quick Start, Padding & Truncation, Pair Encoding (Cross-Encoders), Byte Offsets, Save & Load (.tkz format), Benchmarks

</details>

### fairscale

FairScale: A PyTorch library for large-scale and high-performance training.

`pip install fairscale` · installs from source (sdist only) · licence: BSD License · rank 5258 · last release 2022-12-11 · [PyPI](https://pypi.org/project/fairscale/)

<details><summary>README extract</summary>

FairScale is a PyTorch extension library for high performance and large scale training on one or multiple machines/nodes. This library extends basic PyTorch capabilities while adding new experimental ones.

</details>

### arize

A helper library to interact with Arize AI APIs

`pip install arize` · installs (wheel) · licence: Apache-2.0 · rank 5261 · last release 2026-11-06 · [PyPI](https://pypi.org/project/arize/) · [docs](https://docs.arize.com/arize) · [source](https://github.com/Arize-ai/client_python)

<details><summary>README extract</summary>

Features:
A helper package to interact with Arize AI APIs.

Arize is an AI engineering platform. It helps engineers develop, evaluate, and observe AI applications and agents.

Arize has both Enterprise and OSS products to support this goal: ...

Example:
```python
resp = client.datasets.list_examples(
    dataset="",
    space=..., # Optional, space ID or name
    dataset_version_id=..., # Optional, defaults to latest version
    limit=... # number of desired examples. Defaults to 100
    all=... # Whether or not to export all of the examples. Defaults to False
)
```

...

</details>

### mlx-lm

LLMs with MLX and the Hugging Face Hub

`pip install mlx-lm` · installs (wheel) · licence: MIT · rank 5305 · last release 2026-10-16 · [PyPI](https://pypi.org/project/mlx-lm/) · [source](https://github.com/ml-explore/mlx-lm)

<details><summary>README extract</summary>

MLX LM is a Python package for generating text and fine-tuning large language
models on Apple silicon with MLX.

Some key features include:

* Integration with the Hugging Face Hub to easily use thousands of LLMs with a
 single command.
* Support for quantizing and uploading models to the Hugging Face Hub. ...

Example:
```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

prompt = "Write a story about Einstein"

messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
)

text = generate(model, tokenizer, prompt=prompt, verbose=True)
```

...

</details>

### haystack-ai

LLM framework to build customizable, production-ready LLM applications. Connect components (models, vector DBs, file converters) to pipelines or agents that can interact with your data.

`pip install haystack-ai` · installs (wheel) · licence: Apache-2.0 · rank 5335 · last release 2026-10-21 · [PyPI](https://pypi.org/project/haystack-ai/)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Docs | |
| Package | |
| Meta | |

Haystack is an open-source AI orchestration framework for building production-ready LLM applications in Python.

Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. ...

Features:
Agents built for production
Extend agent behavior with lifecycle hooks (`before_llm`, `before_tool`, `on_exit`, …) for guardrails and custom logic, and track `step_count`, `token_usage`, and tool calls out of the box for monitoring and cost control. ...

Sections: Documentation, Features, Telemetry, Organizations using Haystack

</details>

### torch-einops-utils

Personal utility functions

`pip install torch-einops-utils` · installs (wheel) · licence: MIT License · rank 5341 · last release 2026-11-06 · [PyPI](https://pypi.org/project/torch-einops-utils/) · [source](https://github.com/lucidrains/torch-einops-utils)

<details><summary>README extract</summary>

Some utility functions to help myself (and perhaps others) go faster with ML/AI work

return just the primary output by default, extras only on request

any number of extras, individually or all at once

`primary` may be a tuple of names, or a callable receiving the bound call arguments, for when the shape of the primary depends on the mode

Example:
```python
from torch_einops_utils import maybe_return

@maybe_return('memories')
def forward(self, ids, return_memories = False):
    memories = build_memories(ids) if return_memories else None

    return backbone(ids), memories

model(ids)                             # logits
model(ids, return_memories = True)     # Output(logits, memories)
...
```

Sections: torch-einops-utils, maybe_return, log_table

</details>

### arckit

Tools for working with the Abstraction & Reasoning Corpus (ARC-AGI)

`pip install arckit` · installs (wheel) · licence: Apache-2.0 · rank 5345 · last release 2025-08-22 · [PyPI](https://pypi.org/project/arckit/) · [source](https://github.com/mxbi/arckit)

<details><summary>README extract</summary>

Python and command-line tools for easily working with the ARC, ARC-AGI & ARC-AGI-2 datasets.

Arckit provides tools for loading the data in a friendly format (without a separate download!), visualizing the data with high-quality vector graphics, and evaluating models on the dataset. ...

Example:
```python
>>> import arckit
>>> train_set, eval_set = arckit.load_data() # Load ARC-AGI-2 train/eval.
>>> train_set, eval_set = arckit.load_data("kaggle") # Load ARC Prize 2025
>>> train_set, eval_set = arckit.load_data("arcagi") # Load latest ARC-AGI-1

# TaskSets are iterable and indexable
>>> train_set

>>> train_set[0]

# Indexing can be done by task ID
...
```

...

</details>

### langchain-azure-ai

An integration package to support Microsoft Foundry (formerly Azure AI) capabilities in LangChain/LangGraph ecosystem.

`pip install langchain-azure-ai` · installs (wheel) · licence: MIT · rank 5368 · last release 2026-11-04 · [PyPI](https://pypi.org/project/langchain-azure-ai/) · [source](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-ai)

<details><summary>README extract</summary>

This package contains the LangChain integration for Microsoft Foundry (formerly known Azure AI). To learn more about how to use this package, see the LangChain documentation in Microsoft Foundry.

| I want to... | Start with | ...

Example:
```python
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from langchain_core.messages import HumanMessage, SystemMessage

model = AzureAIOpenAIApiChatModel(
    endpoint="
    credential="your-api-key", #if using Entra ID you can should use DefaultAzureCredential() instead
    model="gpt-5"
)

messages = [
    SystemMessage(
...
```

...

</details>

### qwix

Qwix is a Jax quantization library.

`pip install qwix` · installs (wheel) · licence: Apache-2.0 · rank 5389 · last release 2026-06-22 · [PyPI](https://pypi.org/project/qwix/) · [source](https://github.com/google/qwix)

<details><summary>README extract</summary>

Qwix is a Jax quantization library supporting Quantization-Aware Training (QAT)
and Post-Training Quantization (PTQ) for both XLA targets (CPU/GPU/TPU) and ODML
targets (LiteRT).

Features:
* Weight-only quantization.
 * Dynamic-range quantization.
 * Static-range quantization.

 * QAT: this mode emulates quantized behavior during serving with fake
 quantization. ...

Example:
```python
import jax
from flax import linen as nn

class MLP(nn.Module):

  dhidden: int
  dout: int

  @nn.compact
  def call(self, x):
    x = nn.Dense(self.dhidden, use_bias=False)(x)
    x = nn.relu(x)
    x = nn.Dense(self.dout, use_bias=False)(x)
    return x

model = MLP(64, 16)
model_input = jax.random.uniform(jax.random.key(0), (8, 16))
```

...

</details>

### aqtp

Accurate Quantized Training library.

`pip install aqtp` · installs (wheel) · licence: Apache Software License · rank 5443 · last release 2025-08-01 · [PyPI](https://pypi.org/project/aqtp/) · [source](https://github.com/google/aqt)

<details><summary>README extract</summary>

AQT is a software library designed for easy tensor operation quantization in JAX.

Features:
* Excellent quantized int8 model quality with no hand-tuning at all.
 * Excellent training speedup in production using contemporary ML accelerators.
 * Simple and flexible APIs suitable for both production and research. ...

Example:
```python
# necessary imports
import aqt.jax.v2.flax.aqt_flax as aqt
import aqt.jax.v2.config as aqt_config
import flax.linen as nn
```

Sections: AQT : Accurate Quantized Training, Features, Usage, Flexible Quantization Configs, How to make and use a simple AQT quantizer, AQT Versions, Backpropagation Acceleration, AQT Serving, Other Weight Transformations, How AQT Works Internally, Citing AQT

</details>

### llm

CLI utility and Python library for interacting with Large Language Models from organizations like OpenAI, Anthropic and Gemini plus local models installed on your own machine.

`pip install llm` · installs (wheel) · licence: Apache-2.0 · rank 5477 · last release 2026-11-03 · [PyPI](https://pypi.org/project/llm/) · [docs](https://llm.datasette.io/)

<details><summary>README extract</summary>

<!-- [[[cog

import tempfile
import subprocess
from pathlib import Path

readme_markdown = ''

with tempfile.TemporaryDirectory() as tmpdir:
 tmp_path = Path(tmpdir)
 # Run: sphinx-build -M markdown ./docs ./tmpdir
 subprocess.run([
 "sphinx-build",
 "-M", "markdown",
 "./docs",
 str(tmp_path)
 ], check=True)
 index_file = tmp_path / "markdown" / ...

Sections: LLM, Quick start, Project news

</details>

### data-designer

General framework for synthetic data generation

`pip install data-designer` · installs (wheel) · licence: Apache-2.0 · rank 5528 · last release 2026-11-02 · [PyPI](https://pypi.org/project/data-designer/)

<details><summary>README extract</summary>

Generate high-quality synthetic datasets from scratch or using your own seed data.

📄 Read the technical report — Architecture, programming model, and case studies for multimodal synthetic data generation.

Data Designer helps you create synthetic datasets that go beyond simple LLM prompting. ...

Example:
```python
import data_designer.config as dd
from data_designer.interface import DataDesigner

# Initialize with default settings
data_designer = DataDesigner()
config_builder = dd.DataDesignerConfigBuilder()

# Add a product category
config_builder.add_column(
    dd.SamplerColumnConfig(
        name="product_category",
...
```

...

</details>

### data-designer-config

Configuration layer for DataDesigner synthetic data generation

`pip install data-designer-config` · installs (wheel) · licence: Apache-2.0 · rank 5529 · last release 2026-11-02 · [PyPI](https://pypi.org/project/data-designer-config/)

<details><summary>README extract</summary>

Configuration layer for NeMo Data Designer synthetic data generation framework.

This package provides the configuration API for defining synthetic data generation pipelines. It's a lightweight dependency that can be used standalone for configuration management.

Example:
```python
import data_designer.config as dd

# Initialize config builder with model config(s)
config_builder = dd.DataDesignerConfigBuilder(
    model_configs=[
        dd.ModelConfig(
            alias="my-model",
            model="nvidia/nemotron-3.5-lightning-30b-a3b",
            provider="nvidia",
...
```

Sections: data-designer-config, Usage

</details>

### data-designer-engine

Generation engine for DataDesigner synthetic data generation

`pip install data-designer-engine` · installs (wheel) · licence: Apache-2.0 · rank 5532 · last release 2026-11-02 · [PyPI](https://pypi.org/project/data-designer-engine/)

<details><summary>README extract</summary>

Generation engine for NeMo Data Designer synthetic data generation framework.

This package contains the execution engine that powers Data Designer. It depends on `data-designer-config` and includes heavy dependencies like pandas, numpy, and native HTTP-based LLM integration.

</details>

### numkong

Portable mixed-precision math, linear-algebra, & retrieval library with 2000+ SIMD kernels for x86, Arm, RISC-V, LoongArch, Power, & WebAssembly

`pip install numkong` · installs (wheel) · licence: Apache-2.0 · rank 5606 · last release 2026-11-01 · [PyPI](https://pypi.org/project/numkong/)

<details><summary>README extract</summary>

NumKong for Python is the main high-level SDK in the project.
It targets the gap between `numpy` and low-level native kernels: you keep buffer-protocol interoperability and shape-aware outputs, but you stop giving up mixed precision, widened accumulators, packed reuse, and backend-specific optimizations every time you leave `float64`. ...

Features:
Capability detection is explicit:

The current implementation releases the GIL around the native dense metric calls and around the packed and symmetric matrix kernels. ...

Example:
```python
import numpy as np
import numkong as nk

a, b = np.random.randn(1536).astype(np.float32), np.random.randn(1536).astype(np.float32)
dot = nk.dot(a, b)  # widened accumulation, not same-dtype
print(dot)
```

...

</details>

### dm-env

A Python interface for Reinforcement Learning environments.

`pip install dm-env` · installs (wheel) · licence: Apache Software License · rank 5611 · last release 2022-12-21 · [PyPI](https://pypi.org/project/dm-env/)

### datarobot

This client library is designed to support the DataRobot API.

`pip install datarobot` · installs (wheel) · licence: DataRobot Tool and Utility Agreement · rank 5702 · last release 2026-10-15 · [PyPI](https://pypi.org/project/datarobot/) · [docs](https://docs.datarobot.com/en/docs/api/reference/sdk/index.html)

<details><summary>README extract</summary>

DataRobot is a client library for working with the DataRobot platform API.

This package is released under the terms of the DataRobot Tool and Utility Agreement, which
can be found on our Legal page, along with our privacy policy and more.

Example:
```python
import datarobot as dr
dr.Client(token='your_token', endpoint='
```

Sections: About datarobot, Usage, Extra, Helpful links, Bug Reporting and Q&A

</details>

### tinysegmenter

Very compact Japanese tokenizer

`pip install tinysegmenter` · installs from source (sdist only) · licence: BSD License · rank 5743 · last release 2018-09-16 · [PyPI](https://pypi.org/project/tinysegmenter/)

<details><summary>README extract</summary>

“TinySegmenter in Python” is a Python port by Masato Hagiwara of TinySegmenter, which is an extremely compact Japanese tokenizer originally written in JavaScript by Mr. Taku Kudo.

The library has been finally packaged by Jehan. ...

Example:
```python
> import tinysegmenter
> segmenter = tinysegmenter.TinySegmenter()
> print(' | '.join(segmenter.tokenize(u"私の名前は中野です")))
私  名前  中野 | です
```

Sections: TinySegmenter, Usage

</details>

### runloop_api_client

Official Python SDK for Runloop — secure Linux sandboxes (Devboxes) where AI agents run code, edit files, and expose ports

`pip install runloop_api_client` · installs (wheel) · licence: MIT License · rank 5753 · last release 2026-10-23 · [PyPI](https://pypi.org/project/runloop_api_client/) · [docs](https://docs.runloop.ai) · [source](https://github.com/runloopai/api-client-python)

<details><summary>README extract</summary>

<!-- prettier-ignore -->

Run AI agents and AI-generated code in Devboxes: isolated Linux sandboxes with a shell, a
filesystem, networking, and optional GPUs. Use this library to create a sandbox, run commands in it,
read and write files, expose ports over HTTPS, and snapshot the whole machine so you can pause and
resume it later. ...

Example:
```python
from runloop_api_client import RunloopSDK

runloop = RunloopSDK()  # Uses RUNLOOP_API_KEY environment variable by default

# Create a sandbox, run a command in it, and clean it up on exit.
with runloop.devbox.create(name="my-devbox") as devbox:
    devbox.file.write(file_path="main.py", contents="print('hello from a sandbox')")
...
```

...

</details>

### headroom-ai

Compress tool outputs, logs, JSON and chat history before each LLM call. Fewer input tokens, same answers; in-process, no API key. Library, proxy and MCP server.

`pip install headroom-ai` · installs (wheel) · licence: Apache-2.0 · rank 5774 · last release 2026-11-05 · [PyPI](https://pypi.org/project/headroom-ai/) · [docs](https://docs.headroomlabs.ai/docs) · [source](https://github.com/headroomlabs-ai/headroom)

<details><summary>README extract</summary>

Compress tool outputs, logs, JSON and chat history before each LLM call, so the
model sees fewer input tokens and the same facts. Runs in-process, in Python,
with no API key and no model download. Originals are cached locally and
retrievable. ...

Example:
```python
from headroom import compress

result = compress(messages, model="gpt-4o")  # OpenAI or Anthropic message dicts
result.messages  # same shape as the input, fewer tokens
result.tokens_before, result.tokens_after, result.tokens_saved
```

Sections: Headroom (`headroom-ai`), Use it from a Python app that calls an LLM, Use it around a coding agent (no code changes), Other entry points

</details>

### lineax

Linear solvers in JAX and Equinox.

`pip install lineax` · installs (wheel) · licence: Apache Software License · rank 5793 · last release 2026-05-01 · [PyPI](https://pypi.org/project/lineax/) · [source](https://github.com/google/lineax)

<details><summary>README extract</summary>

Lineax is a JAX library for linear solves and linear least squares. That is, Lineax provides routines that solve for $x$ in $Ax = b$. (Even when $A$ may be ill-posed or rectangular.)

Features include:
- PyTree-valued matrices and vectors;
- General linear operators for Jacobians, transposes, etc.;
- Efficient linear least squares (e.g. ...

Example:
```python
import jax.random as jr
import lineax as lx

matrix_key, vector_key = jr.split(jr.PRNGKey(0))
matrix = jr.normal(matrix_key, (10, 8))
vector = jr.normal(vector_key, (10,))
operator = lx.MatrixLinearOperator(matrix)
solution = lx.linear_solve(operator, vector, solver=lx.QR())
```

Sections: Lineax, Documentation, Quick examples, See also: other libraries in the JAX ecosystem

</details>

### stirrup

The lightweight foundation for building agents

`pip install stirrup` · installs (wheel) · licence: MIT License · rank 5798 · last release 2026-10-22 · [PyPI](https://pypi.org/project/stirrup/) · [docs](https://stirrup.artificialanalysis.ai) · [source](https://github.com/ArtificialAnalysis/Stirrup)

<details><summary>README extract</summary>

Stirrup is a lightweight framework, or starting point template, for building agents. It differs from other agent frameworks by:

- Working with the model, not against it: Stirrup gets out of the way and lets the model choose its own approach to completing tasks (similar to Claude Code). ...

Features:
- 🧪 Code execution: Run code locally, in Docker, or in an E2B sandbox
- 🔎 Online search / web browsing: Search and fetch web pages
- 🔌 MCP client support: Connect to MCP servers and use their tools/resources ...

Example:
```python
import asyncio

from stirrup import Agent
from stirrup.clients.chat_completions_client import ChatCompletionsClient

async def main() -> None:
    """Run an agent that searches the web and creates a chart."""

    # Create client using ChatCompletionsClient
...

</details>

### bert-score

PyTorch implementation of BERT score

`pip install bert-score` · installs (wheel) · licence: MIT License · rank 5812 · last release 2023-02-20 · [PyPI](https://pypi.org/project/bert-score/)

<details><summary>README extract</summary>

Automatic Evaluation Metric described in the paper BERTScore: Evaluating Text Generation with BERT (ICLR 2020). We now support about 130 models (see this spreadsheet for their correlations with human evaluation). ...

Features:
BERTScore leverages the pre-trained contextual embeddings from BERT and matches
words in candidate and reference sentences by cosine similarity.
It has been shown to correlate with human judgment on sentence-level and
system-level evaluation. ...

Sections: BERTScore, News, Overview, Usage, Python Function, Command Line Interface (CLI), Practical Tips, Default Behavior, Default Model, Default Layers

</details>

### conformer

The convolutional module from the Conformer paper

`pip install conformer` · installs (wheel) · licence: MIT License · rank 5928 · last release 2023-05-17 · [PyPI](https://pypi.org/project/conformer/)

### mooncake-transfer-engine-cuda13

A KVCache-centric Disaggregated Architecture for large-scale LLM inference and training. (CUDA 13 version)

`pip install mooncake-transfer-engine-cuda13` · installs (wheel) · licence: Apache Software License · rank 5984 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mooncake-transfer-engine-cuda13/) · [docs](https://kvcache-ai.github.io/Mooncake) · [source](https://github.com/kvcache-ai/Mooncake)

<details><summary>README extract</summary>

Paper
 | Slides
 | Traces
 | Documentation
 | Blog
 | Slack

Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI.
Under real workloads, Mooncake’s innovative architecture enables Kimi to handle 75% more requests while adhering to SLOs. ...

Sections: 🔄 Updates, 🎉 Overview, 🔥 Show Cases, Transfer Engine (TE), Mooncake Store, Mooncake EP and Process Group (PG), Tensor-Centric Ecosystem, SGLang Integration (Guide), vLLM Integration (Guide), 🌐 Ecosystem Integrations, 🚀 Getting Started, Skills for AI Assistants, 📦 Open Source Traces and Tools

</details>

### vector-quantize-pytorch

Vector Quantization - Pytorch

`pip install vector-quantize-pytorch` · installs (wheel) · licence: MIT License · rank 5994 · last release 2026-11-05 · [PyPI](https://pypi.org/project/vector-quantize-pytorch/) · [source](https://github.com/lucidrains/vector-quantizer-pytorch)

<details><summary>README extract</summary>

A vector quantization library originally transcribed from Deepmind's tensorflow implementation, made conveniently into a package. It uses exponential moving averages to update the dictionary.

VQ has been successfully used by Deepmind and OpenAI for high quality generation of images (VQ-VAE-2) and music (Jukebox).

Example:
```python
import torch
from vector_quantize_pytorch import VectorQuantize

vq = VectorQuantize(
    dim = 256,
    codebook_size = 512,     # codebook size
    decay = 0.8,             # the exponential moving average decay, lower means the dictionary will change faster
    commitment_weight = 1.   # the weight on the commitment loss
)

...
```

...

</details>

### transformers-stream-generator

This is a text generation method which returns a generator, streaming out each token in real-time during inference, based on Huggingface/Transformers.

`pip install transformers-stream-generator` · installs from source (sdist only) · licence: Apache Software License · rank 6028 · last release 2024-03-11 · [PyPI](https://pypi.org/project/transformers-stream-generator/)

<details><summary>README extract</summary>

This is a text generation method which returns a generator, streaming out each token in real-time during inference, based on Huggingface/Transformers.

+ original

+ stream

Example:
```python
from transformers_stream_generator import init_stream_support
init_stream_support()
```

Sections: transformers-stream-generator, Description, Web Demo, Usage, Example

</details>

### openviking

An Agent-native context database

`pip install openviking` · installs (wheel) · licence: AGPL-3.0 · rank 6058 · last release 2026-11-02 · [PyPI](https://pypi.org/project/openviking/) · [docs](https://openviking.ai) · [source](https://github.com/volcengine/openviking)

_README extract left out: share-alike licence._

### botbuilder-integration-aiohttp

Microsoft Bot Framework Bot Builder

`pip install botbuilder-integration-aiohttp` · installs (wheel) · licence: MIT License · rank 6109 · last release 2026-01-05 · [PyPI](https://pypi.org/project/botbuilder-integration-aiohttp/)

<details><summary>README extract</summary>

Within the Bot Framework, This library enables you to integrate your bot within an aiohttp web application.

Sections: BotBuilder-Integration-Aiohttp for Python, Documentation/Wiki, Requirements, Source Code

</details>

### vit-pytorch

Vision Transformer (ViT) - Pytorch

`pip install vit-pytorch` · installs (wheel) · licence: MIT License · rank 6142 · last release 2026-11-07 · [PyPI](https://pypi.org/project/vit-pytorch/) · [source](https://codeberg.org/lucidrains/vit-pytorch)

<details><summary>README extract</summary>

Example:
```python
import torch
from vit_pytorch import ViT

v = ViT(
    image_size = 256,
    patch_size = 32,
    num_classes = 1000,
    dim = 1024,
    depth = 6,
    heads = 16,
    mlp_dim = 2048,
    dropout = 0.1,
    emb_dropout = 0.1
)

img = torch.randn(1, 3, 256, 256)

preds = v(img) # (1, 1000)
```

Sections: Vision Transformer - Pytorch, Usage, Parameters, Simple ViT, NaViT, Distillation, Deep ViT, CaiT, Token-to-Token ViT, CCT, Cross ViT, PiT, LeViT, CvT

</details>

### optimistix

Nonlinear optimisation in JAX and Equinox.

`pip install optimistix` · installs (wheel) · licence: Apache Software License · rank 6173 · last release 2026-02-16 · [PyPI](https://pypi.org/project/optimistix/) · [source](https://github.com/patrick-kidger/optimistix)

<details><summary>README extract</summary>

Optimistix is a JAX library for nonlinear solvers: root finding, minimisation, fixed points, and least squares.

Features include:

- interoperable solvers: e.g. autoconvert root find problems to least squares problems, then solve using a minimisation algorithm.
- modular optimisers: e.g. ...

Example:
```python
import jax.numpy as jnp
import optimistix as optx

# Let's solve the ODE dy/dt=tanh(y(t)) with the implicit Euler method.
# We need to find y1 s.t. y1 = y0 + tanh(y1)dt.

y0 = jnp.array(1.)
dt = jnp.array(0.1)

def fn(y, args):
    return y0 + jnp.tanh(y) * dt

solver = optx.Newton(rtol=1e-5, atol=1e-5)
sol = optx.fixed_point(fn, solver, y0)
...
```

Sections: Optimistix, Documentation, Quick example, See also: other libraries in the JAX ecosystem, Credit

</details>

### orbax-export

Orbax Export

`pip install orbax-export` · installs (wheel) · licence: Apache Software License · rank 6220 · last release 2025-09-17 · [PyPI](https://pypi.org/project/orbax-export/) · [source](http://github.com/google/orbax)

<details><summary>README extract</summary>

`pip install orbax-export` (latest PyPi release) OR

`pip install 'git+ (from this repository, at HEAD)

`import orbax.export`

Orbax includes a serialization library for JAX users, enabling the exporting of JAX models to the TensorFlow SavedModel format. ...

</details>

### x-transformers

X-Transformers

`pip install x-transformers` · installs (wheel) · licence: MIT License · rank 6262 · last release 2026-11-07 · [PyPI](https://pypi.org/project/x-transformers/) · [source](https://codeberg.org/lucidrains/x-transformers)

<details><summary>README extract</summary>

A concise but fully-featured transformer, complete with a set of promising experimental features from various papers.

Example:
```python
import torch
from x_transformers import XTransformer

model = XTransformer(
    dim = 512,
    enc_num_tokens = 256,
    enc_depth = 6,
    enc_heads = 8,
    enc_max_seq_len = 1024,
    dec_num_tokens = 256,
    dec_depth = 6,
    dec_heads = 8,
    dec_max_seq_len = 1024,
    tie_token_emb = True      # tie embeddings of encoder and decoder
)

...
```

...

</details>

### auto-round

Repository of AutoRound: Advanced Weight-Only Quantization Algorithm for LLMs

`pip install auto-round` · installs (wheel) · licence: Apache Software License · rank 6409 · last release 2026-10-16 · [PyPI](https://pypi.org/project/auto-round/)

<details><summary>README extract</summary>

English | 简体中文

User Guide | 用户指南

AutoRound is an easy-to-use post-training quantization toolkit for Large Language Models (LLMs) and Vision-Language Models (VLMs).
It supports several practical low-bit and adaptive-bit quantization algorithms, with a particular focus on SignRoundV1 and SignRoundV2. ...

Example:
```python
from auto_round import AutoRound

# Load a model (supports FP8/BF16/FP16/FP32)
model_name_or_path = "Qwen/Qwen3-0.6B"

# Available schemes: "W2A16", "W3A16", "W4A16", "W8A16", "NVFP4", "MXFP4" (no real kernels), "GGUF:Q4_K_M", etc.
ar = AutoRound(model_name_or_path, scheme="W4A16")

# Highest accuracy (4–5× slower).
...
```

...

</details>

### arize-otel

OpenTelemetry tracing helpers for Arize

`pip install arize-otel` · installs (wheel) · licence: BSD · rank 6441 · last release 2026-09-28 · [PyPI](https://pypi.org/project/arize-otel/) · [docs](https://docs.arize.com/arize/large-language-models/tracing) · [source](https://github.com/Arize-ai/arize-otel-python)

<details><summary>README extract</summary>

- Overview
- Uploading large blobs from OpenInference
- Installation
- Quickstart
 - Automatically instrument installed OpenInference packages
 - Add pre-export span processors
 - Send traces to Arize
 - Send traces to Custom Endpoint
 - Specify exporter type
 - Turn off batch processing of spans
 - Debug ...

Features:
`arize-otel` provides Arize-aware OpenTelemetry defaults for instrumenting LLM
applications and exporting their traces to Arize.

Example:
```python
from arize.otel import register_with_routing, set_routing_context
from openinference.instrumentation.openai import OpenAIInstrumentor

tracer_provider = register_with_routing(
    api_key="your-arize-api-key",
    # endpoint and transport are optional and default to Arize's GRPC endpoint
)

...
```

...

</details>

### torchtnt

A lightweight library for PyTorch training tools and utilities

`pip install torchtnt` · installs (wheel) · licence: BSD License · rank 6477 · last release 2024-05-22 · [PyPI](https://pypi.org/project/torchtnt/)

<details><summary>README extract</summary>

TNT is a library for PyTorch training tools and utilities.

</details>

### autogluon.tabular

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.tabular` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 6502 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.tabular/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### autogluon.core

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.core` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 6512 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.core/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### POT

Python Optimal Transport Library

`pip install POT` · installs (wheel) · licence: MIT License · rank 6514 · last release 2026-07-29 · [PyPI](https://pypi.org/project/POT/)

<details><summary>README extract</summary>

This open source Python library provides several solvers for optimization
problems related to Optimal Transport for signal, image processing and machine
learning.

Website and documentation:

Source Code (MIT):

POT has the following main features: ...

Example:
```python
import ot
```

Sections: POT: Python Optimal Transport, Implemented Features, Using and citing the toolbox, Dependencies, Examples, Short examples, Examples and Notebooks, References

</details>

### pyglove

PyGlove: A library for manipulating Python objects.

`pip install pyglove` · installs (wheel) · licence: Apache Software License · rank 6529 · last release 2025-07-15 · [PyPI](https://pypi.org/project/pyglove/)

<details><summary>README extract</summary>

Getting started
| Installation
| Examples
| Reference docs

PyGlove is a general-purpose library for Python object manipulation.
It introduces symbolic object-oriented programming to Python, allowing
direct manipulation of objects that makes meta-programs much easier to write. ...

Example:
```python
import pyglove as pg

@pg.symbolize
class Hello:
  def init(self, subject):
    self._greeting = f'Hello, {subject}!'

  def greet(self):
    print(self._greeting)

hello = Hello('World')
hello.greet()
```

Sections: PyGlove: Manipulating Python Programs, What is PyGlove, Hello PyGlove, Examples, Citing PyGlove

</details>

### pettingzoo

Gymnasium for multi-agent reinforcement learning.

`pip install pettingzoo` · installs (wheel) · licence: MIT License · rank 6537 · last release 2026-08-13 · [PyPI](https://pypi.org/project/pettingzoo/) · [docs](https://pettingzoo.farama.org) · [source](https://github.com/Farama-Foundation/PettingZoo)

<details><summary>README extract</summary>

PettingZoo is a Python library for conducting research in multi-agent reinforcement learning, akin to a multi-agent version of Gymnasium.

The documentation website is at pettingzoo.farama.org and we have a public discord server (which we also use to coordinate development work) that you can join here: ...

Example:
```python
from pettingzoo import make
env = make("aec", "butterfly/pistonball-v6")  # need to specify aec or parallel API
```

Sections: Environments, Getting started, API, Parallel API, SuperSuit, Environment Versioning

</details>

### autogluon.features

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.features` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 6542 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.features/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### clu

Set of libraries for ML training loops in JAX.

`pip install clu` · installs (wheel) · licence: Apache Software License · rank 6545 · last release 2024-04-10 · [PyPI](https://pypi.org/project/clu/)

<details><summary>README extract</summary>

This repository contains common functionality for writing ML training loops. The
goal is to make trainings loops short and readable (but moving common tasks to
small libraries) without removing the flexibility required for research.

To get started, check out this Colab:

If you're looking for usage examples, see: ...

</details>

### kaldi-native-fbank

(no summary)

`pip install kaldi-native-fbank` · installs (wheel) · licence: Apache-2.0 · rank 6596 · last release 2026-11-05 · [PyPI](https://pypi.org/project/kaldi-native-fbank/)

<details><summary>README extract</summary>

Kaldi-compatible online fbank feature extractor without external dependencies.

Tested on the following architectures and operating systems:

 - Linux
 - macOS
 - Windows
 - Android
 - x86
 - arm
 - aarch64

Example:
```python
python3 -c "import kaldi_native_fbank; print(kaldi_native_fbank.version)"
```

Sections: Introduction, Usage, Python APIs, NeMo buffered filter banks

</details>

### autogluon.common

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.common` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 6622 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.common/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### diffrax

GPU+autodiff-capable ODE/SDE/CDE solvers written in JAX.

`pip install diffrax` · installs (wheel) · licence: Apache Software License · rank 6668 · last release 2026-02-18 · [PyPI](https://pypi.org/project/diffrax/) · [source](https://github.com/patrick-kidger/diffrax)

<details><summary>README extract</summary>

Diffrax is a JAX-based library providing numerical differential equation solvers.

Features include:

- ODE/SDE/CDE (ordinary/stochastic/controlled) solvers;
- lots of different solvers (including `Tsit5`, `Dopri8`, symplectic solvers, implicit solvers);
- vmappable _everything_ (including the region of integration); ...

Example:
```python
from diffrax import diffeqsolve, ODETerm, Dopri5
import jax.numpy as jnp

def f(t, y, args):
    return -y

term = ODETerm(f)
solver = Dopri5()
y0 = jnp.array([2., 3.])
solution = diffeqsolve(term, solver, t0=0, t1=1, dt0=0.1, y0=y0)
```

Sections: Diffrax, Documentation, Quick example, See also: other libraries in the JAX ecosystem

</details>

### faster-coco-eval

Faster interpretation of the original COCOEval

`pip install faster-coco-eval` · installs (wheel) · licence: not stated · rank 6680 · last release 2026-08-24 · [PyPI](https://pypi.org/project/faster-coco-eval/)

<details><summary>README extract</summary>

The Fastest, Most Reliable COCO Evaluation Library for Computer Vision

| Aspect | pycocotools | faster-coco-eval |

| Support & Development | Outdated and not actively maintained. Issues and incompatibilities arise with new releases. | Actively maintained, continuously evolving, and regularly updated with new features and bug fixes. ...

Example:
```python
import faster_coco_eval

# This single line replaces pycocotools with faster-coco-eval
faster_coco_eval.init_as_pycocotools()

# Now use the familiar pycocotools API
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

# Load annotations and predictions
anno_json = "path/to/annotations.json"
...
```

...

</details>

### clearml-agent

ClearML Agent - Auto-Magical DevOps for Deep Learning

`pip install clearml-agent` · installs (wheel) · licence: Apache Software License · rank 6718 · last release 2026-06-02 · [PyPI](https://pypi.org/project/clearml-agent/)

<details><summary>README extract</summary>

**ClearML Agent - MLOps/LLMOps made easy
MLOps/LLMOps scheduler & orchestration solution supporting Linux, macOS and Windows**

`🌟 ClearML is open-source - Leave a star to support the project! 🌟` ...

Sections: ClearML-Agent, Formerly known as Trains Agent, Simple, Flexible Experiment Orchestration, Kubernetes Integration (Optional), SLURM (Optional), Using the ClearML Agent, What The ClearML Agent Actually Does, System Design & Flow, ClearML Agent Usage Examples, Configuring the ClearML Agent, Running the ClearML Agent, Starting the ClearML Agent in docker mode, Starting the ClearML Agent - Priority Queues, Stopping the ClearML Agent

</details>

### cellpylib

CellPyLib, A library for working with Cellular Automata, for Python.

`pip install cellpylib` · installs from source (sdist only) · licence: Apache Software License · rank 6816 · last release 2023-02-15 · [PyPI](https://pypi.org/project/cellpylib/)

<details><summary>README extract</summary>

CellPyLib is a library for working with Cellular Automata, for Python. Currently, only 1- and 2-dimensional k-color cellular automata with periodic boundary conditions are supported. The size of the neighbourhood can be adjusted.

</details>

### cached-path

A file utility for accessing both local and remote files through a unified interface

`pip install cached-path` · installs (wheel) · licence: Apache Software License · rank 6819 · last release 2026-03-20 · [PyPI](https://pypi.org/project/cached-path/) · [docs](https://cached-path.readthedocs.io/) · [source](https://github.com/allenai/cached_path)

<details><summary>README extract</summary>

A file utility library that provides a unified, simple interface for accessing both local and remote files.
This can be used behind other APIs that need to access files agnostic to where they are located.

- Documentation
- PyPI Package
- Contributing
- License

Example:
```python
from cached_path import cached_path
```

Sections: cached-path, Quick links, Usage, Using custom headers for HTTP requests, Cache directory, Team

</details>

### pydantic-ai-todo

Todo/task planning toolset for pydantic-ai agents

`pip install pydantic-ai-todo` · installs (wheel) · licence: MIT License · rank 6824 · last release 2026-07-22 · [PyPI](https://pypi.org/project/pydantic-ai-todo/) · [docs](https://github.com/vstorm-co/pydantic-ai-todo#readme) · [source](https://github.com/vstorm-co/pydantic-ai-todo)

<details><summary>README extract</summary>

Task Planning and Tracking for AI Agents

 Capabilities API — plug-and-play with one line
 Subtasks & Dependencies — hierarchical task management
 PostgreSQL Storage — persistent multi-tenant tasks
 Event System — webhooks and callbacks

Todo Toolset for Pydantic AI adds task planning capabilities to any Pydantic AI agent. ...

Example:
```python
from pydantic_ai import Agent
from pydantic_ai_todo import TodoCapability

agent = Agent("openai:gpt-4.1", capabilities=[TodoCapability()])
result = await agent.run("Create a todo list for building a REST API")
```

...

</details>

### optimum-onnx

Optimum ONNX is an interface between the Hugging Face libraries and ONNX / ONNX Runtime

`pip install optimum-onnx` · installs (wheel) · licence: Apache Software License · rank 6844 · last release 2025-12-23 · [PyPI](https://pypi.org/project/optimum-onnx/)

<details><summary>README extract</summary>

Export your Hugging Face models to ONNX

Documentation | ONNX | Hub

Sections: 🤗 Optimum ONNX, ONNX export, Inference, Examples

</details>

### py-trees

pythonic implementation of behaviour trees

`pip install py-trees` · installs (wheel) · licence: BSD-3-Clause · rank 6845 · last release 2026-09-10 · [PyPI](https://pypi.org/project/py-trees/) · [docs](https://py-trees.readthedocs.io/en/devel/) · [source](https://github.com/splintered-reality/py_trees)

<details><summary>README extract</summary>

[About] [What's New?] [Documentation] [Getting Started] [Next Steps] [Maintainers] [Acknowledgments] [Releases]

PyTrees is a Python implementation of behaviour trees designed to facilitate the rapid development of medium sized decision making engines for use in fields like robotics.

Brief feature list: ...

Sections: PyTrees, About, Documentation, Getting Started, Next Steps

</details>

### vicinity

Lightweight Nearest Neighbors with Flexible Backends

`pip install vicinity` · installs (wheel) · licence: MIT License · rank 6870 · last release 2026-09-26 · [PyPI](https://pypi.org/project/vicinity/) · [source](https://github.com/MinishLab/vicinity)

<details><summary>README extract</summary>

Lightweight Nearest Neighbors with Flexible Backends

Quickstart •
Main Features •
Supported Backends •
Installation

Vicinity is a light-weight, low-dependency vector store. It provides a simple and intuitive interface for nearest neighbor search, with support for different backends and evaluation. ...

Example:
```python
import numpy as np
from vicinity import Vicinity, Backend, Metric

# Create some dummy data as strings or other serializable objects
items = ["triforce", "master sword", "hylian shield", "boomerang", "hookshot"]
vectors = np.random.rand(len(items), 128)

# Initialize the Vicinity instance (using the basic backend and cosine metric)
...
```

Sections: Quickstart, Main Features, Backend Parameters, Citing

</details>

### imgaug

Image augmentation library for deep neural networks

`pip install imgaug` · installs (wheel) · licence: MIT License · rank 6966 · last release 2020-02-05 · [PyPI](https://pypi.org/project/imgaug/)

<details><summary>README extract</summary>

A library for image augmentation in machine learning experiments, particularly convolutional
neural networks. Supports the augmentation of images, keypoints/landmarks, bounding boxes, heatmaps and segmentation
maps in a variety of different ways.

</details>

### subagents-pydantic-ai

Subagent toolset for pydantic-ai with dual-mode execution and dynamic agent creation

`pip install subagents-pydantic-ai` · installs (wheel) · licence: MIT License · rank 6967 · last release 2026-10-05 · [PyPI](https://pypi.org/project/subagents-pydantic-ai/) · [docs](https://github.com/vstorm-co/subagents-pydantic-ai#readme) · [source](https://github.com/vstorm-co/subagents-pydantic-ai)

<details><summary>README extract</summary>

Declarative multi-agent orchestration.

 Delegate to specialist sub-agents — sync, async, or auto — with token tracking and cancellation.

 Docs ·
 PyPI ·
 Install ·
 Ecosystem ·
 Deep Agents

 Sync / async / auto • Nested subagents • Runtime agent creation • Background tasks • Token tracking ...

Example:
```python
from pydantic_ai import Agent
from subagents_pydantic_ai import SubAgentCapability, SubAgentConfig

agent = Agent(
    "openai:gpt-4.1",
    capabilities=[SubAgentCapability(
        default_model="openai:gpt-4.1",
        subagents=[
            SubAgentConfig(
                name="researcher",
...
```

...

</details>

### chalkpy

Python SDK for Chalk

`pip install chalkpy` · installs (wheel) · licence: not stated · rank 6974 · last release 2026-11-05 · [PyPI](https://pypi.org/project/chalkpy/) · [docs](https://docs.chalk.ai)

<details><summary>README extract</summary>

Chalk enables innovative machine learning teams to focus on building
the unique products and models that make their business stand out.
Behind the scenes Chalk seamlessly handles data infrastructure with
a best-in-class developer experience. Here’s how it works –

Features:
To get started, define your features with
Pydantic-inspired Python classes.
You can define schemas, specify relationships, and add metadata
to help your team share and re-use work.

Example:
```python
@features
class User:
    id: int
    full_name: str
    nickname: Optional[str]
    email: Optional[str]
    birthday: date
    credit_score: float
    datawarehouse_feature: float

    transactions: DataFrame[Transaction] = has_many(lambda: Transaction.user_id == User.id)
```

...

</details>

### sgl-eval

One-click accuracy evaluation harness for SGLang.

`pip install sgl-eval` · installs (wheel) · licence: Apache Software License · rank 7008 · last release 2026-10-14 · [PyPI](https://pypi.org/project/sgl-eval/) · [source](https://github.com/sgl-project/sgl-eval)

<details><summary>README extract</summary>

One-click accuracy evaluation harness for SGLang.

Point at any OpenAI-compatible endpoint. Scoring logic (graders, evaluators,
prompts, dataset configs) is vendored from NeMo-Skills;
sgl-eval contributes the transport, runner, and benchmark wiring.

Sections: sgl-eval, Quick start, Reading a run, Running less than the whole thing, Benchmarks, Presets, Architecture, Scope

</details>

### kaldifst

(no summary)

`pip install kaldifst` · installs (wheel) · licence: Apache-2.0 · rank 7025 · last release 2026-11-04 · [PyPI](https://pypi.org/project/kaldifst/)

<details><summary>README extract</summary>

Python wrapper for OpenFst and its extensions from Kaldi, e.g.,
`fstdeterminizestar`.

Note: It does not depend on Kaldi. You don't need to install
Kaldi to use this repo.

Please refer to <
for installation and usage.

Sections: Introduction, Documentation

</details>

### jraph

Jraph: A library for Graph Neural Networks in Jax

`pip install jraph` · installs (wheel) · licence: Apache Software License · rank 7030 · last release 2022-08-12 · [PyPI](https://pypi.org/project/jraph/)

<details><summary>README extract</summary>

Sections: Jraph - A library for graph neural networks in jax., New! PMAP Examples and Data Loading., New! Interactive Jraph Colabs, Quick Start, (destination nodes)., You can optionally add edge attributes., We then save the number of nodes and the number of edges., in a GraphsTuple possible.

</details>

### langchain-perplexity

An integration package connecting Perplexity and LangChain

`pip install langchain-perplexity` · installs (wheel) · licence: MIT License · rank 7144 · last release 2026-10-21 · [PyPI](https://pypi.org/project/langchain-perplexity/) · [docs](https://reference.langchain.com/python/integrations/langchain_perplexity/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-perplexity, 🤔 What is this?, 📖 Documentation, Resources

</details>

### spmd-types

A type system for distributed (SPMD) tensor computations in PyTorch

`pip install spmd-types` · installs (wheel) · licence: BSD License · rank 7188 · last release 2026-10-22 · [PyPI](https://pypi.org/project/spmd-types/) · [docs](https://meta-pytorch.org/spmd_types/) · [source](https://github.com/meta-pytorch/spmd_types)

<details><summary>README extract</summary>

A type system for distributed (SPMD) tensor computations in PyTorch. This
package provides two type systems:

* Local SPMD types, which allow you to use Megatron-style differentiable
 collectives in a safe way by tracking whether or not your backward gradients
 are pending reduction or not. ...

Example:
```python
import torch
import torch.distributed as dist
import spmd_types as spmd
import spmd_types.checker
from torch.distributed.device_mesh import init_device_mesh

# Set up a fake process group (no GPUs needed)
dist.init_process_group(backend="fake", rank=0, world_size=8)
mesh = init_device_mesh("cpu", (2, 4), mesh_dim_names=("dp", "tp"))
...
```

Sections: `spmd_types`, Quick start, Documentation

</details>

### python-doctr

Document Text Recognition (docTR): deep Learning for high-performance OCR on documents.

`pip install python-doctr` · installs (wheel) · licence: Apache Software License · rank 7191 · last release 2026-08-21 · [PyPI](https://pypi.org/project/python-doctr/) · [docs](https://mindee.github.io/doctr) · [source](https://github.com/mindee/doctr)

<details><summary>README extract</summary>

Optical Character Recognition made seamless & accessible to anyone, powered by PyTorch

docTR was originally created by Mindee. It is now actively developed and maintained by t2k GmbH.

What you can expect from this repository:

- efficient ways to parse textual information (localize and identify each word) from your documents ...

Example:
```python
from doctr.models import ocr_predictor

model = ocr_predictor(det_arch="db_resnet50", reco_arch="crnn_vgg16_bn", pretrained=True)
```

...

</details>

### unstructured-ingest

Local ETL data pipeline to get data RAG ready

`pip install unstructured-ingest` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 7217 · last release 2026-10-27 · [PyPI](https://pypi.org/project/unstructured-ingest/)

<details><summary>README extract</summary>

For details, see the Unstructured Ingest overview in the Unstructured documentation.

</details>

### neptune-query

Neptune Query is a Python library for retrieving data from Neptune.

`pip install neptune-query` · installs (wheel) · licence: Apache Software License · rank 7247 · last release 2026-04-07 · [PyPI](https://pypi.org/project/neptune-query/) · [docs](https://docs.neptune.ai/) · [source](https://github.com/neptune-ai/neptune-query)

<details><summary>README extract</summary>

The `neptune_query` package is a read-only API for fetching metadata.

With the Query API, you can:

- List experiments, runs, and attributes of a project.
- Fetch experiment or run metadata as a data frame.
- Define filters to fetch experiments, runs, and attributes that meet certain criteria.

Example:
```python
import neptune_query as nq
```

Sections: Neptune Query API, Usage, Runs API, Documentation, Examples, Example 1: Fetch metric values, Example 2: Fetch metadata as one row per run, Example 3: Define filters, Example 4: Exclude archived runs, Example 5: Fetch runs belonging to specific experiment

</details>

### gigatoken

Tokenize your documents at GB/s

`pip install gigatoken` · installs (wheel) · licence: MIT · rank 7305 · last release 2026-11-02 · [PyPI](https://pypi.org/project/gigatoken/) · [source](https://github.com/marcelroed/gigatoken)

<details><summary>README extract</summary>

~1000x faster than HuggingFace's tokenizers, drop-in replacement.

*Tokenize your text data at GB/s!*

Note that both HF tokenizers and tiktoken are already running multithreaded Rust!

Gigatoken is the fastest tokenizer for language modeling.
It supports a wide range of CPU hardware, and nearly all commonly used tokenizers. ...

Example:
```python
import gigatoken as gt

# Minimum change from existing HuggingFace tokenizers usage (compatibility mode)
hf_tokenizer = ...
tokenizer = gt.Tokenizer(hf_tokenizer).as_hf()

# tokenizer can be used in the same contexts as hf_tokenizer
tokens = tokenizer.encode_batch(["This is a test string", "And here is another"])

# OR with tiktoken
...
```

...

</details>

### haystack-experimental

Experimental components and features for the Haystack LLM framework.

`pip install haystack-experimental` · installs (wheel) · licence: Freely Distributable; Apache Software License · rank 7320 · last release 2026-07-28 · [PyPI](https://pypi.org/project/haystack-experimental/)

<details><summary>README extract</summary>

> [!WARNING]
> This project is archived and no longer maintained.
> `0.19.0.post1` is the final release. There will be no further releases, bug fixes, or compatibility updates,
> and the repository is read-only.
> - Most experiments graduated into Haystack itself. ...

Example:
```python
from haystack import Document
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack_experimental.components.summarizers import LLMSummarizer

summarizer = LLMSummarizer(chat_generator=OpenAIChatGenerator())
summarizer.run(documents=[Document(content="...")])
```

Sections: Haystack experimental package, Experiments catalog, Graduated experiments, Discontinued experiments, Usage, Telemetry

</details>

### laya

Fast, non-autoregressive System 1 decision engine with calibrated probabilities

`pip install laya` · installs (wheel) · licence: Apache Software License · rank 7356 · last release 2026-11-07 · [PyPI](https://pypi.org/project/laya/)

<details><summary>README extract</summary>

Multilingual, non-autoregressive System 1 decision engine. Typed decisions over 100+ languages in a single forward pass — 33 ms — trained with reinforcement learning against strictly proper scoring rules (RLCD), with a router that picks the right checkpoint per request.

Features:
On a shared benchmark (17,416 questions, one T4 GPU, identical questions per model — seed 13, 20 options per choice question, the first 300 test rows per language, from `research/results/t4_colab_benchmark.json`; `tests/test_doc_tables.py` checks ...

Example:
```python
import laya

agent = laya.Agent(vegaml=True)   # the 0.8B universal reader (nandakishorm/vega-U), the default

# Switching the model underneath is one string. Every option keeps the same engine, questions and fields:
...

</details>

### optimum-quanto

A pytorch quantization backend for optimum.

`pip install optimum-quanto` · installs (wheel) · licence: Apache Software License · rank 7362 · last release 2025-03-06 · [PyPI](https://pypi.org/project/optimum-quanto/)

<details><summary>README extract</summary>

🤗 Optimum Quanto is a pytorch quantization backend for optimum.

It has been designed with versatility and simplicity in mind:

- all features are available in eager mode (works with non-traceable models),
- quantized models can be placed on any device (including CUDA and MPS),
- automatically inserts quantization and dequantization stubs, ...

Example:
```python
from transformers import AutoModelForCausalLM
from optimum.quanto import QuantizedModelForCausalLM, qint4

model = AutoModelForCausalLM.from_pretrained('meta-llama/Meta-Llama-3-8B')
qmodel = QuantizedModelForCausalLM.quantize(model, weights=qint4, exclude='lm_head')
```

...

</details>

### pyAgrum-nightly

Bayesian networks and other Probabilistic Graphical Models.

`pip install pyAgrum-nightly` · installs (wheel) · licence: LGPL-3.0-only OR MIT · rank 7452 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyAgrum-nightly/) · [docs](https://pyagrum.readthedocs.io/) · [source](https://gitlab.com/agrumery/aGrUM)

_README extract left out: share-alike licence._

### tslearn

A machine learning toolkit dedicated to time-series data

`pip install tslearn` · installs (wheel) · licence: BSD-2-Clause · rank 7455 · last release 2026-10-22 · [PyPI](https://pypi.org/project/tslearn/) · [docs](http://tslearn.readthedocs.io) · [source](https://github.com/tslearn-team/tslearn)

<details><summary>README extract</summary>

| Section | Description |
|-|-|
| Installation | Installing the dependencies and tslearn |
| Getting started | A quick introduction on how to use tslearn |
| Available features | An extensive overview of tslearn's functionalities |
| Documentation | A link to our API reference and a gallery of examples |
| Contributing | A guide for heroes willing ...

Example:
```python
>>> from tslearn.utils import to_time_series_dataset
>>> my_first_time_series = [1, 3, 4, 2]
>>> my_second_time_series = [1, 2, 4, 2]
>>> my_third_time_series = [1, 2, 4, 2, 2]
>>> X = to_time_series_dataset([my_first_time_series,
                                my_second_time_series,
                                my_third_time_series])
...
```

...

</details>

### nvidia-modelopt

Nvidia Model Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, Neural Architecture Search (NAS), distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed.

`pip install nvidia-modelopt` · installs (wheel) · licence: Apache-2.0 · rank 7476 · last release 2026-11-02 · [PyPI](https://pypi.org/project/nvidia-modelopt/)

### lerobot

🤗 LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch

`pip install lerobot` · installs (wheel) · licence: Apache Software License · rank 7530 · last release 2026-11-05 · [PyPI](https://pypi.org/project/lerobot/) · [docs](https://huggingface.co/docs/lerobot/index) · [source](https://github.com/huggingface/lerobot)

<details><summary>README extract</summary>

LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch. The goal is to lower the barrier to entry so that everyone can contribute to and benefit from shared datasets and pretrained models. ...

Example:
```python
from lerobot.robots.myrobot import MyRobot

# Connect to a robot
robot = MyRobot(config=...)
robot.connect()

# Read observation and send action
obs = robot.get_observation()
action = model.select_action(obs)
robot.send_action(action)
```

Sections: Quick Start, Robots & Control, LeRobot Dataset, SoTA Models, Inference & Evaluation, Third-Party Hardware, Resources

</details>

### whisper-ctranslate2

Whisper command line client that uses CTranslate2 and faster-whisper

`pip install whisper-ctranslate2` · installs (wheel) · licence: MIT License · rank 7540 · last release 2026-10-05 · [PyPI](https://pypi.org/project/whisper-ctranslate2/)

<details><summary>README extract</summary>

Whisper command line client compatible with original OpenAI client based on CTranslate2.

It uses CTranslate2 and Faster-whisper Whisper implementation that is up to 4 times faster than openai/whisper for the same accuracy while using less memory.

Key features: ...

Sections: Introduction, Python package, Using prebuild Docker image, Usage, CTranslate2 specific options, Batched inference, Quantization, Loading the model from a directory, Using Voice Activity Detection (VAD) filter, Print colors, Live transcribe from your microphone, Diarization (speaker identification), Need help?, Contact

</details>

### azureml-train-automl

Used for automatically finding the best machine learning model and its parameters.

`pip install azureml-train-automl` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 7549 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-train-automl/)

<details><summary>README extract</summary>

The azureml-train-automl package contains functionality for automatically finding the best machine learning model and its parameters, given training and test data.

</details>

### fhaviary

Gymnasium framework for training language model agents on constructive tasks

`pip install fhaviary` · installs (wheel) · licence: Apache Software License · rank 7572 · last release 2026-09-15 · [PyPI](https://pypi.org/project/fhaviary/) · [source](https://github.com/Future-House/aviary)

<details><summary>README extract</summary>

Aviary [^1] is a gymnasium for defining custom language agent RL environments.
The library features pre-existing environments on
math [^2], general knowledge [^3], biological sequences [^4], scientific literature search [^5], and protein stability. ...

Features:
A pictorial overview of the five implemented Aviary environments and the language decision process framework.

Example:
```python
from collections import namedtuple
from aviary.core import Environment, Message, ToolRequestMessage, Tool

# State in this example is simply a counter
CounterEnvState = namedtuple("CounterEnvState", ["count"])

class CounterEnv(Environment[CounterEnvState]):
    """A simple environment that allows an agent to modify a counter."""

...
```

...

</details>

### mistralai-workflows

Mistral Workflows - Build reliable AI workflows with Python

`pip install mistralai-workflows` · installs (wheel) · licence: Apache Software License · rank 7601 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mistralai-workflows/) · [docs](https://docs.mistral.ai/workflows/getting-started/introduction)

<details><summary>README extract</summary>

Build reliable, production-grade AI workflows with Python.

Features:
Mistral Workflows is a Python SDK for building AI-powered workflows with built-in reliability, observability, and scalability. It provides fault tolerance, durability, and exactly-once execution guarantees.

Example:
```python
from datetime import timedelta

from mistralai.workflows import workflow, activity

@activity
async def get_weather(city: str) -> str:
    # Your activity implementation
    return f"Weather in {city}: Sunny"

@workflow.define
class WeatherWorkflow:
    @workflow.run
    async def run(self, city: str) -> str:
...
```

Sections: Mistral Workflows, Overview, Features, Quick Start, Documentation, Examples

</details>

### torcheval

A library for providing a simple interface to create new metrics and an easy-to-use toolkit for metric computations and checkpointing.

`pip install torcheval` · installs (wheel) · licence: BSD License · rank 7610 · last release 2023-08-24 · [PyPI](https://pypi.org/project/torcheval/)

<details><summary>README extract</summary>

This library is currently in Alpha and currently does not have a stable release. The API may change and may not be backward compatible. If you have suggestions for improvements, please open a GitHub issue. We'd love to hear your feedback. ...

Example:
```python
import torch
from torcheval.metrics.functional import multiclass_accuracy

NUM_BATCHES = 16
BATCH_SIZE = 8
INPUT_SIZE = 10
NUM_CLASSES = 6
eval_frequency = 4

model = torch.nn.Sequential(torch.nn.Linear(INPUT_SIZE, NUM_CLASSES), torch.nn.ReLU())
optim = torch.optim.Adagrad(model.parameters(), lr=0.001)
loss_fn = torch.nn.CrossEntropyLoss()

...
```

...

</details>

### litdata

The Deep Learning framework to train, deploy, and ship AI products Lightning fast.

`pip install litdata` · installs (wheel) · licence: Apache-2.0 · rank 7656 · last release 2026-09-30 · [PyPI](https://pypi.org/project/litdata/) · [docs](https://lightning-ai.github.io/litdata/) · [source](https://github.com/Lightning-AI/litdata)

<details><summary>README extract</summary>

Transform

✅ Parallelize data processing
✅ Create vector embeddings
✅ Run distributed inference
✅ Scrape websites at scale

Optimize / Stream

✅ Stream raw files with no prep
✅ Stream large cloud datasets
✅ Accelerate training by 20x
✅ Pause and resume data streaming
✅ Use remote data without local loading ...

Features:
Speeding up model training involves more than kernel tuning. Data loading frequently slows down training, because datasets are too large to fit on disk, consist of millions of small files, or stream slowly from the cloud. ...

Example:
```python
from torch.utils.data import DataLoader
from litdata import StreamingRawDataset
from PIL import Image
import io

def to_image(data: bytes):
    return Image.open(io.BytesIO(data)).convert("RGB")

dataset = StreamingRawDataset(
...

</details>

### fhlmi

A client to provide LLM responses for FutureHouse applications.

`pip install fhlmi` · installs (wheel) · licence: Apache Software License · rank 7742 · last release 2026-10-27 · [PyPI](https://pypi.org/project/fhlmi/) · [source](https://github.com/Future-House/ldp/packages/lmi)

<details><summary>README extract</summary>

<!-- pyml disable-num-lines 6 line-length -->

A Python library for interacting with Large Language Models (LLMs)
through a unified interface,
hence the name Language Model Interface (LMI).

Example:
```python
from lmi import LiteLLMModel
from aviary.core import Message

llm = LiteLLMModel()

messages = [Message(content="What is the meaning of life?")]

result = await llm.call_single(messages)
# assert result.text == "42"
```

Sections: Language Model Interface (LMI), Quick start, Documentation, LLMs, LLMModel, LiteLLMModel, Cost tracking, Rate limiting, Basic Usage, Rate Limit Format, Storage Options, Monitoring Rate Limits, Timeout Configuration, Weight-based Rate Limiting

</details>

### semhash

Fast Multimodal Semantic Deduplication & Filtering

`pip install semhash` · installs (wheel) · licence: MIT License · rank 7744 · last release 2026-09-30 · [PyPI](https://pypi.org/project/semhash/) · [source](https://github.com/MinishLab/semhash)

<details><summary>README extract</summary>

Fast Multimodal Semantic Deduplication & Filtering

Quickstart •
Main Features •
Usage •
Benchmarks

SemHash is a lightweight, multimodal library for semantic deduplication, outlier filtering, and representative sample selection. ...

Example:
```python
from datasets import load_dataset
from semhash import SemHash

# Load a dataset to deduplicate
texts = load_dataset("ag_news", split="train")["text"]

# Initialize a SemHash instance
semhash = SemHash.from_records(records=texts)

# Deduplicate the texts
deduplicated_texts = semhash.self_deduplicate().selected

# Filter outliers
...
```

...

</details>

### seqio

SeqIO: Task-based datasets, preprocessing, and evaluation for sequence models.

`pip install seqio` · installs (wheel) · licence: Apache Software License · rank 7764 · last release 2025-08-28 · [PyPI](https://pypi.org/project/seqio/)

<details><summary>README extract</summary>

*Task-based datasets, preprocessing, and evaluation for sequence models*

*Go to SeqIO ReadTheDocs Documentation Page.*

Features:
SeqIO is a library for processing sequential data to be fed into downstream
sequence models. It uses
`tf.data.Dataset`
to create scalable data pipelines but requires minimal use of TensorFlow. ...

Example:
```python
seqio.TaskRegistry.add(
    "wmt19_ende",
    seqio.TfdsDataSource(tfds_name="wmt19_translate/de-en:1.0.0"),
    preprocessors=[
        functools.partial(
            translate, source_language='en', target_language='de'),
        seqio.preprocessors.tokenize, seqio.preprocessors.append_eos
    ],
    output_features={
        'inputs':
...
```

...

</details>

### qwen-omni-utils

Qwen Omni Language Model Utils - PyTorch

`pip install qwen-omni-utils` · installs (wheel) · licence: Apache Software License · rank 7781 · last release 2026-02-10 · [PyPI](https://pypi.org/project/qwen-omni-utils/) · [source](https://github.com/QwenLM/Qwen2-VL.git)

<details><summary>README extract</summary>

Qwen-Omni Utils contains a set of helper functions for processing and integrating visual and audio language information with Qwen-Omni Model.

Example:
```python
from transformers import Qwen2_5OmniForConditionalGeneration, AutoProcessor
from qwen_omni_utils import process_mm_info

# You can directly insert a local file path, a URL, or a base64-encoded image into the position where you want in the text.
messages = [
    # Image
    ## Local file path
...
```

Sections: qwen-omni-utils, Usage, Qwen2Omni, Qwen2VL, Qwen2.5VL

</details>

### dyNET38

Fork version of DyNet: DyNet38 shares wheels of DyNet for Python 3.8+

`pip install dyNET38` · installs (wheel) · licence: Apache Software License · rank 7817 · last release 2025-12-30 · [PyPI](https://pypi.org/project/dyNET38/)

<details><summary>README extract</summary>

The Dynamic Neural Network Toolkit

- General
- Installation
 - C++
 - Python
- Getting Started
- Citing
- Releases and Contributing

DyNet is a neural network library developed by Carnegie Mellon University and many others. ...

Sections: General, Getting started, Citing

</details>

### ncnn

ncnn is a high-performance neural network inference framework optimized for the mobile platform

`pip install ncnn` · installs (wheel) · licence: BSD License · rank 7834 · last release 2026-10-20 · [PyPI](https://pypi.org/project/ncnn/)

<details><summary>README extract</summary>

ncnn is a high-performance neural network inference framework optimized for mobile, embedded, and desktop deployment.
It has no third-party runtime dependencies, runs across CPU and Vulkan GPU backends, and provides tools such as pnnx for converting PyTorch and ONNX models to ncnn. ...

Features:
- No third-party runtime dependencies and no BLAS / NNPACK requirement.
- Pure C++ implementation with C API and Python binding.
- Optimized CPU inference for mobile and embedded processors, including ARM NEON and multi-core scheduling. ...

Example:
```python
import torch
import torch.nn as nn
import pnnx

class Model(nn.Module):
    def init(self):
        super().init()
        self.conv = nn.Conv2d(3, 8, 1)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(8, 4)

...

</details>

### langchain-daytona

Daytona sandbox integration for Deep Agents

`pip install langchain-daytona` · installs (wheel) · licence: MIT License · rank 7868 · last release 2026-10-23 · [PyPI](https://pypi.org/project/langchain-daytona/) · [docs](https://github.com/langchain-ai/deepagents/tree/main/libs/partners/daytona) · [source](https://github.com/langchain-ai/deepagents)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-daytona, 🤔 What is this?, Resources

</details>

### rax

Learning-to-Rank using JAX.

`pip install rax` · installs (wheel) · licence: Apache Software License · rank 7918 · last release 2025-01-03 · [PyPI](https://pypi.org/project/rax/)

<details><summary>README extract</summary>

Rax is a Learning-to-Rank library written in JAX. Rax provides off-the-shelf
implementations of ranking losses and metrics to be used with JAX. It provides
the following functionality:

- Ranking losses (`rax.*_loss`): `rax.softmax_loss`,
 `rax.pairwise_logistic_loss`, ... ...

Example:
```python
import jax.numpy as jnp
import rax

scores = jnp.array([2.2, -1.3, 5.4])  # output of a model.
labels = jnp.array([1.0,  0.0, 0.0])  # indicates doc 1 is relevant.

rax.ndcg_metric(scores, labels)  # computes a ranking metric.
# 0.63092977

rax.pairwise_hinge_loss(scores, labels)  # computes a ranking loss.
# 2.1
```

Sections: 🦖 Rax: Learning-to-Rank using JAX, Ranking, Synopsis, Examples, Citing Rax

</details>

### nooa

Code-generating agent orchestration system with event sourcing and serialized execution

`pip install nooa` · does not install on CPython 3.14 · licence: Apache Software License · rank 7994 · last release 2026-11-06 · [PyPI](https://pypi.org/project/nooa/) · [source](https://github.com/NVIDIA-NeMo/labs-OO-Agents)

<details><summary>README extract</summary>

A Pythonic way to build AI agents.

Docs · Quick Start · Notebook Tutorials · Examples · Paper · Blog

NVIDIA-labs Object Oriented Agents (NOOA) is a model-agnostic Python framework designed to support reliable AI agent development. Many agent frameworks represent prompts, tools, callbacks, and workflows as separate abstractions. ...

Example:
```python
from nooa import Agent

# The agent is a Python object.
class SupportAgent(Agent):
    """You are a support agent."""

    # State lives on the object. Fields are typed.
    order_db: OrderDB

    # Ordinary method. Just Python.
    def is_refund_eligible(self, order: Order) -> bool:
...
```

...

</details>

### torchx

TorchX SDK and Components

`pip install torchx` · installs (wheel) · licence: BSD License · rank 8005 · last release 2024-07-16 · [PyPI](https://pypi.org/project/torchx/)

<details><summary>README extract</summary>

TorchX is a universal job launcher for PyTorch applications.
TorchX is designed to have fast iteration time for training/research and support
for E2E production ML pipelines when you're ready.

TorchX currently supports:

* Kubernetes (EKS, GKE, AKS, etc)
* Slurm
* AWS Batch
* Docker
* Local
* Ray (prototype)
* GCP Batch (prototype) ...

Sections: TorchX, Quickstart, Documentation, Requirements, Stable, Nightly, Source, Docker

</details>

### ema-pytorch

Easy way to keep track of exponential moving average version of your pytorch module

`pip install ema-pytorch` · installs (wheel) · licence: MIT License · rank 8055 · last release 2026-07-31 · [PyPI](https://pypi.org/project/ema-pytorch/) · [source](https://github.com/lucidrains/ema-pytorch)

<details><summary>README extract</summary>

A simple way to keep track of an Exponential Moving Average (EMA) version of your pytorch model

Example:
```python
import torch
from ema_pytorch import EMA

# your neural network as a pytorch module

net = torch.nn.Linear(512, 512)

# wrap your neural network, specify the decay (beta)

ema = EMA(
    net,
    beta = 0.9999,              # exponential moving average factor
...
```

Sections: EMA - Pytorch, Usage, Target Representation Routing

</details>

### pynini

Finite-state grammar compilation

`pip install pynini` · installs (wheel) · licence: Apache Software License · rank 8081 · last release 2025-09-04 · [PyPI](https://pypi.org/project/pynini/)

<details><summary>README extract</summary>

This is a Python extension module for compiling, optimizing and applying grammar
rules. Rules can be compiled into weighted finite state transducers, pushdown
transducers, or multi-pushdown transducers. It uses OpenFst finite-state
transducers (FSTs) and FST archives (FArs) as inputs and outputs. ...

Sections: OpenGrm Pynini, Dependencies, Windows, MacOS, Linux, Mandatory disclaimer

</details>

### pycaret

PyCaret - An open source, low-code machine learning library in Python.

`pip install pycaret` · installs (wheel) · licence: MIT License · rank 8097 · last release 2024-04-28 · [PyPI](https://pypi.org/project/pycaret/)

<details><summary>README extract</summary>

Example:
```python
# Classification Functional API Example

# loading sample dataset
from pycaret.datasets import get_data
data = get_data('juice')

# init setup
from pycaret.classification import *
s = setup(data, target = 'Purchase', session_id = 123)

# model training and selection
best = compare_models()

# evaluate trained model
evaluate_model(best)

...
```

Sections: An open-source, low-code machine learning library in Python, 🎉🎉🎉 PyCaret 3.3 is now available. 🎉🎉🎉, Docs •, Welcome to PyCaret, 📄 Option 2: Build from Source, 📦 Option 3: Docker, 🏃‍♂️ Quickstart, 1. Functional API, 2. OOP API, 📁 Modules, Classification, Regression, Time Series, Clustering

</details>

### pyulog

Python log parser for ULog

`pip install pyulog` · installs (wheel) · licence: BSD-3-Clause · rank 8141 · last release 2026-10-20 · [PyPI](https://pypi.org/project/pyulog/) · [source](https://github.com/PX4/pyulog)

<details><summary>README extract</summary>

This module allows you to parse ULog files, which are used within the PX4
autopilot middleware.

The file format is documented on

</details>

### google-tunix

A lightweight JAX-native LLM post-training framework.

`pip install google-tunix` · installs (wheel) · licence: Apache-2.0 · rank 8186 · last release 2026-06-11 · [PyPI](https://pypi.org/project/google-tunix/) · [source](https://github.com/google/tunix)

<details><summary>README extract</summary>

Tunix (Tune-in-JAX) is a JAX based library designed to streamline the
post-training of Large Language Models. It provides efficient and scalable
support for:

- SOTA Training performance on TPUs
- Supervised Fine-Tuning
- Reinforcement Learning (RL)
- Agentic RL ...

Features:
- Full Weights Fine-Tuning
 - PEFT (Parameter-Efficient
 Fine-Tuning)
 - DPO (Direct Preference Optimization)
 - ORPO (Odds Ratio Preference Optimization) ...

Sections: Tunix: A Lightweight LLM Post-Training Library, High Level Architecture, Key Features, News, Framework & Infra Highlights, Getting Started, Collaborations and Partnership, Citing Tunix

</details>

### fiftyone-brain

FiftyOne Brain

`pip install fiftyone-brain` · installs (wheel) · licence: Apache-2.0 · rank 8196 · last release 2026-09-30 · [PyPI](https://pypi.org/project/fiftyone-brain/)

<details><summary>README extract</summary>

Open Source AI from Voxel51

FiftyOne Website •
FiftyOne Docs •
FiftyOne Brain Docs •
Blog •
Community

FiftyOne Brain contains the open source AI/ML capabilities for the
FiftyOne ecosystem, enabling users to
automatically analyze and manipulate their datasets and models. ...

Sections: Documentation, Repository layout

</details>

### local-attention

Local attention, window with lookback, for language modeling

`pip install local-attention` · installs (wheel) · licence: MIT License · rank 8335 · last release 2025-07-16 · [PyPI](https://pypi.org/project/local-attention/)

### distrax

Distrax: Probability distributions in JAX.

`pip install distrax` · installs (wheel) · licence: Apache Software License · rank 8341 · last release 2026-06-12 · [PyPI](https://pypi.org/project/distrax/) · [source](https://github.com/google-deepmind/distrax)

<details><summary>README extract</summary>

Distrax is a lightweight library of probability distributions and bijectors. It
acts as a JAX-native reimplementation of a subset of
TensorFlow Probability (TFP), with
some new features and emphasis on extensibility.

Example:
```python
import distrax
import jax
import jax.numpy as jnp

from tensorflow_probability.substrates import jax as tfp
tfd = tfp.distributions

key = jax.random.PRNGKey(1234)
mu = jnp.array([-1., 0., 1.])
sigma = jnp.array([0.1, 0.2, 0.3])

dist_distrax = distrax.MultivariateNormalDiag(mu, sigma)
dist_tfp = tfd.MultivariateNormalDiag(mu, sigma)

...
```

Sections: Distrax, Design Principles, Features, Distributions, Bijectors, Jitting Distrax, A note about `vmap` and `pmap`, Subclassing Distributions and Bijectors, Examples, Citing Distrax

</details>

### fiftyone-db

FiftyOne DB

`pip install fiftyone-db` · installs from source (sdist only) · licence: Apache Software License · rank 8397 · last release 2025-12-30 · [PyPI](https://pypi.org/project/fiftyone-db/)

<details><summary>README extract</summary>

Supporting package for FiftyOne.

> [!NOTE]
> These steps are to be performed by authorized Voxel51 engineers.

The `fiftyone-db` package is usually cut from the `fiftyone:develop` branch.
The PyPI uploads will be triggered when a release tag is pushed to the
repository:

1. Navigate to the
 releases page.

1. Select `Draft a new release`.

1. ...

Sections: `fiftyone-db`, Releasing the fiftyone-db package

</details>

### dora-search

Easy grid searches for ML.

`pip install dora-search` · installs (wheel) · licence: MIT · rank 8502 · last release 2026-09-09 · [PyPI](https://pypi.org/project/dora-search/)

<details><summary>README extract</summary>

This is a fork of facebookresearch/dora, as we diverged a bit from upstream.

- Installation
- Introduction
- Making your code compatible with Dora
- The `dora` command
- `dora run`: Running XP locally
- `dora launch`: Launching XP remotely
- `dora info`: Inspecting an XP
- `dora grid`: Managing a grid search
- The Dora API
- Sharing XPs ...

Example:
```python
from itertools import product
from dora import Explorer, Launcher

@Explorer
def explorer(launcher: Launcher):
    launcher(batch_size=128)  # Schedule an experiments with the given batch size.
    # For an argparse based project, this will get converted to the `--batch_size=128` flag
...
```

...

</details>

### voxel51-eta

Extensible Toolkit for Analytics

`pip install voxel51-eta` · installs (wheel) · licence: Apache Software License · rank 8540 · last release 2026-08-10 · [PyPI](https://pypi.org/project/voxel51-eta/)

<details><summary>README extract</summary>

**An open and extensible computer vision, machine learning and video analytics
infrastructure.**

ETA is very portable:

- Installable on Mac or Linux
- Supports Python 3.10 or later
- Supports TensorFlow 1.X and 2.X
- Supports CPU-only and GPU-enabled installations

Sections: ETA: Extensible Toolkit for Analytics, Requirements, Step 0: Setup your Python environment, Step 1: Clone the repository, Setting up your execution environment, CLI, Quickstart, Organization, Generating Documentation

</details>

### nnunetv2

nnU-Net is a framework for out-of-the box image segmentation.

`pip install nnunetv2` · installs (wheel) · licence: Apache Software License · rank 8562 · last release 2026-07-01 · [PyPI](https://pypi.org/project/nnunetv2/) · [source](https://github.com/MIC-DKFZ/nnUNet)

<details><summary>README extract</summary>

nnU-Net is a semantic segmentation framework that automatically adapts its pipeline to a dataset. It analyzes the training data, creates a dataset fingerprint, configures suitable U-Net variants, and provides an end-to-end workflow from preprocessing to training, model selection, and inference. ...

Sections: nnU-Net, Start Here, Documentation, Scope, Project Notes

</details>

### hyper-connections

Hyper-Connections

`pip install hyper-connections` · installs (wheel) · licence: MIT License · rank 8612 · last release 2026-05-13 · [PyPI](https://pypi.org/project/hyper-connections/) · [source](https://github.com/lucidrains/hyper-connections)

<details><summary>README extract</summary>

Attempt to make multiple residual streams, proposed in Hyper-Connections paper out of Bytedance AI lab, accessible as an easy to use library, as well as for following any new research in this direction.

Write up on mHC from Subhadip Mitra

Example:
```python
import torch
from torch import nn

# a single branch layer

branch = nn.Linear(512, 512)

# before

residual = torch.randn(2, 1024, 512)

residual = branch(residual) + residual

# after, say 4 streams in paper

from hyper_connections import get_init_and_expand_reduce_stream_functions

...
```

Sections: Hyper Connections, Usage

</details>

### fasttext-langdetect

80x faster and 95% accurate language identification with fastText

`pip install fasttext-langdetect` · installs (wheel) · licence: MIT License · rank 8695 · last release 2026-10-27 · [PyPI](https://pypi.org/project/fasttext-langdetect/) · [source](https://github.com/zafercavdar/fasttext-langdetect)

<details><summary>README extract</summary>

`fasttext-langdetect` is a thin Python wrapper around Facebook's pretrained
`lid.176` fastText
language identification models.

Example:
```python
from ftlangdetect import detect

result = detect(text="Bugün hava çok güzel", low_memory=False)
print(result)
# {'lang': 'tr', 'score': 1.0}

result = detect(text="Bugün hava çok güzel", low_memory=True)
print(result)
# {'lang': 'tr', 'score': 0.9982126951217651}

# Multi-line input is fine — whitespace is normalized internally
...
```

Sections: fasttext-langdetect, Usage, Model cache location, Benchmark, Recall per language, References

</details>

### bentoml

BentoML: The easiest way to serve AI apps and models

`pip install bentoml` · installs (wheel) · licence: Apache Software License · rank 8755 · last release 2026-10-23 · [PyPI](https://pypi.org/project/bentoml/) · [docs](https://docs.bentoml.com) · [source](https://github.com/bentoml/bentoml)

<details><summary>README extract</summary>

🍱 Build model inference APIs and multi-model serving systems with any open-source or custom AI models. 👉 Join our forum!

BentoML is a Python library for building online serving systems optimized for AI apps and model inference.

- 🍱 Easily build APIs for Any AI/ML Model. ...

Example:
```python
import bentoml

@bentoml.service(
    image=bentoml.images.Image(python_version="3.11").python_packages("torch", "transformers"),
)
class Summarization:
    def init(self) -> None:
        import torch
        from transformers import pipeline

        device = "cuda" if torch.cuda.is_available() else "cpu"
...
```

Sections: Unified Model Serving Framework, What is BentoML?, Getting started, 💻 Run locally, 🐳 Deploy using Docker, Examples, Advanced topics, Usage tracking and feedback

</details>

### ldp

Agent framework for constructing language model agents and training on constructive tasks.

`pip install ldp` · installs (wheel) · licence: Apache Software License · rank 8765 · last release 2026-10-27 · [PyPI](https://pypi.org/project/ldp/) · [source](https://github.com/Future-House/ldp)

<details><summary>README extract</summary>

LDP [^1] is a framework for enabling modular interchange of language agents, environments, and optimizers.
A language decision process (LDP)
is a partially-observable Markov decision process (POMDP)
where actions and observations consist of natural language.
The full definition from the Aviary paper [^1] is: ...

Features:
A pictorial overview of the language decision process (LDP) framework
together with five implemented Aviary environments.

Example:
```python
from ldp.agent import SimpleAgent
from aviary.core import DummyEnv

env = DummyEnv()
agent = SimpleAgent()

obs, tools = await env.reset()
agent_state = await agent.init_state(tools=tools)

done = False
while not done:
    action, agent_state, _ = await agent.get_asv(agent_state, obs)
...

</details>

### boxlite

Python bindings for Boxlite runtime

`pip install boxlite` · installs (wheel) · licence: Apache-2.0 · rank 8783 · last release 2026-11-06 · [PyPI](https://pypi.org/project/boxlite/) · [docs](https://github.com/boxlite-ai/boxlite/tree/main/docs) · [source](https://github.com/boxlite-ai/boxlite)

<details><summary>README extract</summary>

Python bindings for BoxLite - an embeddable virtual machine runtime for secure, isolated code execution.

Access the agent API through `Box.agents`
and `SimpleBox.agents`, including synchronous wrappers, grouped options and error handling.

Features:
The BoxLite Python SDK provides a Pythonic API for creating and managing isolated execution environments. Built with PyO3, it wraps the Rust BoxLite runtime with async-first Python bindings. ...

Example:
```python
import asyncio
import boxlite

async def main():
    # Create a box and run a command
    async with boxlite.SimpleBox(image="python:slim") as box:
        result = await box.exec("python", "-c", "print('Hello from BoxLite!')")
        print(result.stdout)
        # Output: Hello from BoxLite!

asyncio.run(main())
```

...

</details>

### prompty

Prompty is an asset class and format for LLM prompts

`pip install prompty` · installs (wheel) · licence: MIT License · rank 8799 · last release 2026-10-21 · [PyPI](https://pypi.org/project/prompty/) · [docs](https://prompty.ai) · [source](https://github.com/Microsoft/prompty)

<details><summary>README extract</summary>

Prompty is a markdown file format (`.prompty`) for LLM
prompts. The Python runtime loads, renders, parses, and
executes these files. Every `.prompty` file becomes a typed
`Prompty` object.

Example:
```python
import prompty

# One-shot: load + prepare + run
result = prompty.invoke("greeting.prompty", inputs={"name": "Jane"})
print(result)

# Step-by-step
agent = prompty.load("greeting.prompty")
messages = prompty.prepare(agent, inputs={"name": "Jane"})
result = prompty.run(agent, messages)
```

Sections: Prompty — Python Runtime, Extras, Quick Start, 1. Write a `.prompty` File, 2. Run It, 3. Async, API Reference, Core Functions, Agent Turns (Tool Calling), Connection Registry, Structured Output, Streaming, Tracing, `.prompty` File Format

</details>

### autogluon.timeseries

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.timeseries` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 8870 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.timeseries/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### matrx-ai

Unified multi-provider AI client, orchestration, and tool system

`pip install matrx-ai` · installs (wheel) · licence: MIT License · rank 8903 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-ai/) · [source](https://github.com/AI-Matrix-Engine/aidream-current)

<details><summary>README extract</summary>

Unified multi-provider AI client, orchestration, and tool system for Python. One `UnifiedAIClient` that speaks to 12+ provider SDKs (OpenAI, Anthropic, Google, Groq, Cerebras, xAI, Together, ElevenLabs, Hugging Face, Cohere, Fireworks, Replicate) through a common `UnifiedConfig` / `UnifiedMessage` / `UnifiedResponse` contract, with streaming, tool ...

Example:
```python
from matrx_ai import UnifiedAIClient, UnifiedConfig, UnifiedMessage, Provider, Role

client = UnifiedAIClient()
config = UnifiedConfig(
    provider=Provider.ANTHROPIC,
    ai_model="claude-sonnet-4-6",
    messages=[UnifiedMessage(role=Role.USER, content="Summarize the Magna Carta.")],
    stream=False,
)
response = await client.run(config)
...
```

...

</details>

### pageindex

Python SDK for PageIndex — reasoning-based, vectorless document retrieval, cloud and local

`pip install pageindex` · installs (wheel) · licence: MIT License · rank 8907 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pageindex/) · [docs](https://docs.pageindex.ai) · [source](https://github.com/VectifyAI/PageIndex)

<details><summary>README extract</summary>

Reasoning-based RAG ◦ No Vector DB, No Chunking ◦ Context-Aware Retrieval ◦ Reads Like a Human

 ☁️ Cloud •
 📖 Docs •
 📝 Blog •
 ✉️ Contact

- [Oct '26] 🔥 Page Search API: find the pages that answer each question in about a second, and send your LLM only those. ...

Example:
```python
import os
from pageindex import PageIndexClient

os.environ["OPENAI_API_KEY"] = "your-openai-key"

client = PageIndexClient(
    index="gpt-6-luna",                 # model to build the tree index
    chat="gpt-6-sol",                   # model to search the tree
)
doc_id = client.submit_document("report.pdf")["doc_id"]

...
```

...

</details>

### agentscope

AgentScope: A Flexible yet Robust Multi-Agent Platform.

`pip install agentscope` · installs (wheel) · licence: Apache-2.0 · rank 8914 · last release 2026-10-27 · [PyPI](https://pypi.org/project/agentscope/) · [docs](https://docs.agentscope.io/) · [source](https://github.com/agentscope-ai/agentscope)

<details><summary>README extract</summary>

中文主页 | Documentation | Roadmap

AgentScope 2.0 is a production-ready, easy-to-use agent framework with essential abstractions that keep up with rising model capability.

We design for increasingly agentic LLMs. ...

Example:
```python
from agentscope.agent import Agent
from agentscope.console import launch_console
from agentscope.tool import Toolkit, Bash, Grep, Glob, Read, Write, Edit
from agentscope.credential import DashScopeCredential
from agentscope.model import DashScopeChatModel

import os, asyncio

async def main() -> None:
    agent = Agent(
        name="Friday",
...
```

Sections: What is AgentScope 2.0?, News, Quickstart, From PyPI, From source, Agent, Agent Service — All You Need to Build Your App, Publications

</details>

### diffq

Differentiable quantization framework for PyTorch.

`pip install diffq` · installs from source (sdist only) · licence: Creative Commons Attribution-NonCommercial 4.0 International · rank 8954 · last release 2023-05-05 · [PyPI](https://pypi.org/project/diffq/)

<details><summary>README extract</summary>

DiffQ performs differentiable quantization using pseudo quantization noise.
It can automatically tune the number of bits used per weight or group of weights,
in order to achieve a given trade-off between model size and accuracy.

Go read our paper for more details.

See the changelog for details on releases. ...

Example:
```python
import torch
from torch.nn import functional as F
import diffq
from diffq import DiffQuantizer

model = MyModel()
optim = ...  # The optimizer must be created before the quantizer
quantizer = DiffQuantizer(model)
quantizer.setup_optimizer(optim)

# Distributed data parallel must be created after DiffQuantizer!
...
```

...

</details>

### inspect-tool-support

Sandbox container tool code for inspect_ai

`pip install inspect-tool-support` · installs (wheel) · licence: MIT License · rank 8961 · last release 2025-08-11 · [PyPI](https://pypi.org/project/inspect-tool-support/)

<details><summary>README extract</summary>

Inspect calls into the sandboxed image are done statelessly via `docker exec inspect-tool-support`.

Some tools can be implemented without the need for any in-process state. For those tools, the tool code will be executed within the `inspect-tool-support` process. ...

Features:
The release process for this project separates code commits from package publishing. While developers can make frequent commits to the repository, package releases are performed on a different tempo, typically when enough meaningful changes have ...

Sections: Design, Stateful Tool Design Pattern, Overview, Documenting Changes

</details>

### lbox-clients

This module contains client sdk uses to conntect to the Labelbox API and backends

`pip install lbox-clients` · installs (wheel) · licence: Apache Software License · rank 9294 · last release 2025-01-16 · [PyPI](https://pypi.org/project/lbox-clients/) · [docs](https://labelbox-python.readthedocs.io/en/latest/) · [source](https://github.com/Labelbox/labelbox-python)

<details><summary>README extract</summary>

This is an example module which can be cloned and reused to develop modules under the `lbox` namespace.

</details>

### einops-exts

Einops Extensions

`pip install einops-exts` · installs (wheel) · licence: MIT License · rank 9399 · last release 2023-01-05 · [PyPI](https://pypi.org/project/einops-exts/)

### arxyne

Run any engineering simulation from one command.

`pip install arxyne` · installs (wheel) · licence: BUSL-1.1 · rank 9424 · last release 2026-11-08 · [PyPI](https://pypi.org/project/arxyne/) · [docs](https://docs.arxyne.com)

<details><summary>README extract</summary>

<!-- mcp-name: com.arxyne/solver -->

Every simulation, on one record.

How Physical AI fits into the design and engineering pipeline.

</details>

### pykalman

An implementation of the Kalman Filter, Kalman Smoother, and EM algorithm in Python

`pip install pykalman` · installs (wheel) · licence: BSD License · rank 9448 · last release 2026-01-31 · [PyPI](https://pypi.org/project/pykalman/) · [docs](https://pykalman.readthedocs.io/en/latest/) · [source](https://github.com/pykalman/pykalman)

<details><summary>README extract</summary>

The dead-simple Kalman Filter, Kalman Smoother, and EM library for Python.

`pykalman` is a Python library for Kalman filtering and smoothing, providing efficient algorithms for state estimation in time series. It includes tools for linear dynamical systems, parameter estimation, and sequential data modeling. ...

Example:
```python
from pykalman import KalmanFilter
import numpy as np
kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])
measurements = np.asarray([[1,0], [0,0], [0,1]])  # 3 observations
kf = kf.em(measurements, n_iter=5)
(filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
...
```

Sections: Welcome to pykalman, speech_balloon: Where to ask questions, zap: Usage, Examples

</details>

### langchain-typesafe

A LangChain integration for TypeSafe classifiers

`pip install langchain-typesafe` · installs (wheel) · licence: MIT License · rank 9451 · last release 2026-11-05 · [PyPI](https://pypi.org/project/langchain-typesafe/) · [docs](https://reference.langchain.com/python/integrations/langchain_typesafe/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Example:
```python
from langchain_typesafe import Choice, Noul, Score, TypeSafeClassifier

classifier = TypeSafeClassifier()

result = classifier.invoke(
    {
        "state": "Stripe has failed to connect for three days. Help ASAP.",
        "questions": {
            "department": Choice(
                instructions="Which team should handle this?",
...
```

Sections: langchain-typesafe, Usage, Experimental middleware, `ModelRouterMiddleware`, `AutoModeMiddleware`, LangChain messages as state, Custom HTTP clients, Error handling, Documentation

</details>

### controlnet-aux

Auxillary models for controlnet

`pip install controlnet-aux` · installs (wheel) · licence: Apache Software License · rank 9528 · last release 2025-05-08 · [PyPI](https://pypi.org/project/controlnet-aux/)

<details><summary>README extract</summary>

This is a PyPi installable package of lllyasviel's ControlNet Annotators

The code is copy-pasted from the respective folders in < and connected to the 🤗 Hub.

All credit & copyright goes to < .

Example:
```python
import requests
from PIL import Image
from io import BytesIO

from controlnet_aux.processor import Processor

# load image
url = "

response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert("RGB").resize((512, 512))

# load processor from processor_id
# options are:
...
```

Sections: ControlNet auxiliary models, DWPose, Usage, Image resolution

</details>

### tk

TensorKit is a deep learning helper between Python and C++.

`pip install tk` · installs (wheel) · licence: Apache Software License · rank 9535 · last release 2019-07-08 · [PyPI](https://pypi.org/project/tk/)

### PyMaxflow

A mincut/maxflow package for Python

`pip install PyMaxflow` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 9648 · last release 2024-11-25 · [PyPI](https://pypi.org/project/PyMaxflow/)

_README extract left out: share-alike licence._

### fiftyone

FiftyOne: the open-source tool for building high-quality datasets and computer vision models

`pip install fiftyone` · installs (wheel) · licence: Apache Software License · rank 9659 · last release 2026-09-29 · [PyPI](https://pypi.org/project/fiftyone/)

<details><summary>README extract</summary>

**The open-source tool for building high-quality datasets and computer vision
models**

Website •
Docs •
Try it Now •
Getting Started Guides •
Tutorials •
Blog •
Community

We created FiftyOne to supercharge your visual AI
development by enabling you to visualize and label your data, evaluate your
models, and maximize data and model quality more ...

Example:
```python
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
session = fo.launch_app(dataset)
```

...

</details>

### h2o

H2O, Fast Scalable Machine Learning, for python

`pip install h2o` · installs from source (sdist only) · licence: Apache Software License · rank 9723 · last release 2026-08-12 · [PyPI](https://pypi.org/project/h2o/)

<details><summary>README extract</summary>

H2O scales statistics, machine learning and math over BigData. H2O is extensible and users can build blocks using simple math legos in the core. H2O keeps familiar interfaces like python, R, Excel & JSON so that BigData enthusiasts & experts can explore, munge, model and score datasets using a range of simple to advanced algorithms. ...

</details>

### liac-arff

A module for read and write ARFF files in Python.

`pip install liac-arff` · installs from source (sdist only) · licence: MIT License · rank 9805 · last release 2020-08-31 · [PyPI](https://pypi.org/project/liac-arff/)

### opendatalab

OpenDataLab Python SDK

`pip install opendatalab` · installs (wheel) · licence: MIT License · rank 9851 · last release 2023-08-02 · [PyPI](https://pypi.org/project/opendatalab/)

<details><summary>README extract</summary>

IMPORTANT: OpenDataLab SDK WIP, not ensure the necessary compatibility of OpenAPI and SDK. As a result, please use the SDK with the latest version.

OpenDataLab Python SDK is a python library to access Opendatalab
and use open datasets.
It provides:

- A pythonic way to access opendatalab resources. ...

Sections: OpenDataLab Python SDK, Usage, Help, Version, Login, Logout, List Dataset Files, Documentation

</details>

### toktok-rs

Fast, exact BPE tokenizer for OpenAI encodings — Rust core, tiktoken-identical ids

`pip install toktok-rs` · installs (wheel) · licence: MIT · rank 9852 · last release 2026-10-21 · [PyPI](https://pypi.org/project/toktok-rs/) · [source](https://github.com/vectorize-io/toktok)

<details><summary>README extract</summary>

A fast, exact BPE tokenizer for OpenAI encodings — Rust core, Python bindings.
Token ids are byte-identical to tiktoken.

The Pile, 25 MB, cl100k_base, single thread, GitHub runners. Ids verified
identical before timing.

| encoder | throughput | CPU per MB | p99 per doc | | ...

Example:
```python
import toktok

toktok.batch_count(["hello world", "how many tokens is this?"])
# [2, 6]

toktok.batch_count(docs, "o200k_base")                # GPT-4o and friends
toktok.batch_count(docs, "cl100k_base", threads=4)    # 0 = every core (default)
toktok.batch_count(["a<|endoftext|>b"], with_special=True)   # [3]
```

...

</details>

### sahi

A vision library for performing sliced inference on large images/small objects

`pip install sahi` · installs (wheel) · licence: MIT · rank 9903 · last release 2026-11-01 · [PyPI](https://pypi.org/project/sahi/) · [docs](https://github.com/obss/sahi/tree/main/docs) · [source](https://github.com/obss/sahi)

<details><summary>README extract</summary>

Features:
SAHI helps developers overcome real-world challenges in object detection by
enabling sliced inference for detecting small objects in large images. It
supports various popular detection models and provides easy-to-use APIs. ...

Sections: SAHI: Slicing Aided Hyper Inference, Overview, Approved by AI Tools, Quick Start, Learning Resources, Notebooks & Demos, Framework Agnostic Sliced/Standard Prediction, Error Analysis Plots & Evaluation, Interactive Visualization & Inspection, Other Utilities

</details>

### graph-retriever

Retriever combining unstructured similarity and structured document traversal.

`pip install graph-retriever` · installs (wheel) · licence: Apache-2.0 · rank 9907 · last release 2025-04-04 · [PyPI](https://pypi.org/project/graph-retriever/) · [source](https://github.com/datastax/graph-rag)

<details><summary>README extract</summary>

Retrievers combining vector (similarity search over unstructured data) and graph
(structured relationships).

</details>

### langchain-graph-retriever

LangChain retriever for traversing document graphs on top of vector-based similarity search.

`pip install langchain-graph-retriever` · installs (wheel) · licence: Apache-2.0 · rank 9919 · last release 2025-04-04 · [PyPI](https://pypi.org/project/langchain-graph-retriever/) · [source](https://github.com/datastax/graph-rag)

<details><summary>README extract</summary>

LangChain Graph Retriever is a Python library that supports traversing a document graph on top of vector-based similarity search.
It works seamlessly with LangChain's retriever framework and supports various graph traversal strategies for efficient document discovery.

Features:
- Vector Search: Perform similarity searches using vector embeddings.
- Graph Traversal: Apply traversal strategies such as breadth-first (Eager) or Maximal Marginal Relevance (MMR) to explore document relationships. ...

Example:
```python
from langchain_graph_retriever import GraphRetriever
from langchain_core.vectorstores import Chroma

# Initialize the vector store (Chroma in this example)
vector_store = Chroma(embedding_function=your_embedding_function)

# Create the Graph Retriever
...

</details>

### langchain-modal

Modal sandbox integration for Deep Agents

`pip install langchain-modal` · installs (wheel) · licence: MIT License · rank 9956 · last release 2026-10-26 · [PyPI](https://pypi.org/project/langchain-modal/) · [docs](https://github.com/langchain-ai/deepagents/tree/main/libs/partners/modal) · [source](https://github.com/langchain-ai/deepagents)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-modal, 🤔 What is this?, Resources

</details>

### mlOpus

MLOps tools for research and development.

`pip install mlOpus` · installs from source (sdist only) · licence: Apache Software License · rank 9979 · last release 2026-04-16 · [PyPI](https://pypi.org/project/mlOpus/) · [source](https://github.com/lariel-fernandes/mlopus)

<details><summary>README extract</summary>

A collection of MLOps tools for AI/ML/DS research and development.

 - Compatible with any "MLflow-like" provider through plugins.
 - Search entities in MongoDB Query Language with predicate push-down to the MLflow provider.
 - Local cache for artifacts and entity metadata.
 - Offline mode to work with local cache only. ...

Sections: MLOpus, Main features

</details>

### onnxtr

Onnx Text Recognition (OnnxTR): docTR Onnx-Wrapper for high-performance OCR on documents.

`pip install onnxtr` · installs (wheel) · licence: Apache Software License · rank 9998 · last release 2026-08-24 · [PyPI](https://pypi.org/project/onnxtr/) · [source](https://github.com/felixdittrich92/OnnxTR)

<details><summary>README extract</summary>

> :warning: Please note that this is a wrapper around the doctr library to provide a Onnx pipeline for docTR. For feature requests, which are not directly related to the Onnx pipeline, please refer to the base project.

Optical Character Recognition made seamless & accessible to anyone, powered by Onnx

What you can expect from this repository: ...

Example:
```python
from onnxtr.io import DocumentFile

# PDF
pdf_doc = DocumentFile.from_pdf("path/to/your/doc.pdf")
# Image
single_img_doc = DocumentFile.from_images("path/to/your/img.jpg")
# Webpage (requires `weasyprint` to be installed)
webpage_doc = DocumentFile.from_url("
# Multiple page images
...
```

...

</details>

### mistralai-workflows-plugins-mistralai

Mistral AI plugin for Mistral Workflows - Provides native Mistral AI integration

`pip install mistralai-workflows-plugins-mistralai` · installs (wheel) · licence: Apache Software License · rank 10027 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mistralai-workflows-plugins-mistralai/) · [docs](https://docs.mistral.ai/workflows/getting-started/introduction)

<details><summary>README extract</summary>

Native Mistral AI integration for Mistral Workflows.

Features:
This plugin provides Mistral AI-specific activities and models for building AI workflows with the Mistral AI API.

Example:
```python
import mistralai.workflows as workflows
import mistralai.workflows.plugins.mistralai as workflows_mistralai

@workflows.workflow.define(name="chat-workflow")
class ChatWorkflow:
    @workflows.workflow.entrypoint
    async def run(self, prompt: str) -> str:
        response = await workflows_mistralai.mistralai_chat_stream(
...
```

Sections: Mistral Workflows - Mistral AI Plugin, Overview, Features, Quick Start, Documentation, Examples

</details>

### traceml

Engine for ML/Data tracking, visualization, dashboards, and model UI for Polyaxon.

`pip install traceml` · installs (wheel) · licence: Apache 2.0 · rank 10038 · last release 2026-11-06 · [PyPI](https://pypi.org/project/traceml/)

<details><summary>README extract</summary>

Engine for ML/Data tracking, visualization, explainability, drift detection, and dashboards for Polyaxon.

Example:
```python
from traceml import tracking

tracking.init(..., is_offline=True, ...)
```

Sections: TraceML, [WIP] Local sandbox, Offline usage, Simple usage in a Python script, Keras, PyTorch, Tensorflow, Fastai, Pytorch Lightning, HuggingFace, Tracking artifacts, Tracking DataFrames, Summary, [WIP] Summaries

</details>

### autogluon

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 10054 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### laion-clap

Contrastive Language-Audio Pretraining Model from LAION

`pip install laion-clap` · installs (wheel) · licence: Apache Software License · rank 10065 · last release 2025-05-04 · [PyPI](https://pypi.org/project/laion-clap/)

<details><summary>README extract</summary>

With CLAP, you can extract a latent representation of any given audio and text for your own model, or for different downstream tasks.

All codes are comming officially with the following paper, accepted by IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2023:
 - Large-Scale Contrastive Language-Audio Pretraining ...

Example:
```python
import numpy as np
import librosa
import torch
import laion_clap

# quantization
def int16_to_float32(x):
    return (x / 32767.0).astype(np.float32)

def float32_to_int16(x):
    x = np.clip(x, a_min=-1., a_max=1.)
    return (x * 32767.).astype(np.int16)

model = laion_clap.CLAP_Module(enable_fusion=False)
...
```

...

</details>

### langchain-exa

An integration package connecting Exa and LangChain

`pip install langchain-exa` · installs (wheel) · licence: MIT License · rank 10222 · last release 2026-03-26 · [PyPI](https://pypi.org/project/langchain-exa/) · [docs](https://reference.langchain.com/python/integrations/langchain_exa/) · [source](https://github.com/langchain-ai/langchain)

<details><summary>README extract</summary>

Looking for the JS/TS version? Check out LangChain.js.

Sections: langchain-exa, 🤔 What is this?, 📖 Documentation

</details>

### labelbox

Labelbox Python API

`pip install labelbox` · does not install on CPython 3.14 · licence: Apache Software License · rank 10236 · last release 2026-10-22 · [PyPI](https://pypi.org/project/labelbox/) · [docs](https://labelbox-python.readthedocs.io/en/latest/) · [source](https://github.com/Labelbox/labelbox-python)

<details><summary>README extract</summary>

Core mono-module for Labelbox's Python SDK.

Sections: Labelbox, Setup, Repository Organization, Linting / Formatting, Documentation

</details>

### river-client

Python client for River ML training API

`pip install river-client` · installs (wheel) · licence: Apache-2.0 · rank 10238 · last release 2026-11-05 · [PyPI](https://pypi.org/project/river-client/)

<details><summary>README extract</summary>

Python client for the River ML training API — sampling,
LoRA and full-weight fine-tuning, and reinforcement learning against River-hosted models.

Example:
```python
import river_client as river

client = river.Client(api_key="your-key", endpoint="api.river.ai")

# Stateless sampling from a base model
samples = client.sample(
    "What is 2+2?",
    base_model="Qwen/Qwen3.6-35B-A3B-FP8",
    max_tokens=50,
)
print(samples[0].text)

# Training with a session
with client.session() as session:
...
```

Sections: river-client, Quick start, Reinforcement learning, Dedicated streaming inference, Export checkpoints to Hugging Face, AI agent skill

</details>

### gymnasium-robotics

RL Robotics environments with Gymnasium API.

`pip install gymnasium-robotics` · installs (wheel) · licence: MIT License · rank 10256 · last release 2026-01-02 · [PyPI](https://pypi.org/project/gymnasium-robotics/) · [docs](https://robotics.farama.org) · [source](https://github.com/Farama-Foundation/Gymnasium-Robotics)

<details><summary>README extract</summary>

This library contains a collection of Reinforcement Learning robotic environments that use the Gymnasium API. The environments run with the MuJoCo physics engine and the maintained mujoco python bindings. ...

Example:
```python
import gymnasium as gym

env = gym.make("FetchReach-v3")
env.reset()
obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

# The following always has to hold:
assert reward == env.compute_reward(obs["achieved_goal"], obs["desired_goal"], info)
...
```

Sections: Environments, Multi-goal API

</details>

### aegra-api

Aegra core API - Self-hosted Agent Protocol server

`pip install aegra-api` · installs (wheel) · licence: Apache-2.0 · rank 10262 · last release 2026-10-23 · [PyPI](https://pypi.org/project/aegra-api/) · [docs](https://github.com/aegra/aegra#readme) · [source](https://github.com/aegra/aegra)

<details><summary>README extract</summary>

Aegra API - Self-hosted Agent Protocol server.

Aegra is an open-source, self-hosted alternative to LangSmith Deployments. This package provides the core API server that implements the Agent Protocol, allowing you to run AI agents on your own infrastructure without vendor lock-in.

Features:
- Agent Protocol Compliant: Works with Agent Chat UI, LangGraph Studio, CopilotKit
- Drop-in Replacement: Compatible with the LangGraph SDK
- Self-Hosted: Run on your own PostgreSQL database ...

Example:
```python
# graphs/my_agent/graph.py
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: list[str]

def process_node(state: State) -> State:
    messages = state.get("messages", [])
    messages.append("Processed!")
...

</details>

### ogx-client

OpenAPI-generated Python client for OGX

`pip install ogx-client` · installs (wheel) · licence: MIT License · rank 10318 · last release 2026-10-09 · [PyPI](https://pypi.org/project/ogx-client/) · [docs](https://ogx-ai.github.io/docs) · [source](https://github.com/ogx-ai/ogx)

<details><summary>README extract</summary>

This is the specification of the OGX that provides
 a set of endpoints and their corresponding interfaces that are
 tailored to
 best leverage Llama Models.

 🔗 COMBINED: This specification includes both stable production-ready APIs
 and experimental pre-release APIs. ...

Example:
```python
import ogx_client
from ogx_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to
# See configuration.py for a list of all supported configuration parameters.
configuration = ogx_client.Configuration(
    host = "
)

# Enter a context with an instance of the API client
...
```

Sections: ogx-client, Requirements., Setuptools, Tests, Migrating from `ogx_client` <= 1.1.3, Getting Started, Documentation for API Endpoints, Documentation For Models

</details>

### setfit

Efficient few-shot learning with Sentence Transformers

`pip install setfit` · installs (wheel) · licence: Apache Software License · rank 10324 · last release 2026-09-04 · [PyPI](https://pypi.org/project/setfit/)

<details><summary>README extract</summary>

🤗 Models | 📊 Datasets | 📕 Documentation | 📖 Blog | 📃 Paper

SetFit is an efficient and prompt-free framework for few-shot fine-tuning of Sentence Transformers. It achieves high accuracy with little labeled data - for instance, with only 8 labeled examples per class on the Customer Reviews sentiment dataset, SetFit is competitive with fine-tuning ...

Example:
```python
from datasets import load_dataset
from setfit import SetFitModel, Trainer, TrainingArguments, sample_dataset

# Load a dataset from the Hugging Face Hub
dataset = load_dataset("stanfordnlp/sst2")

# Simulate the few-shot regime by sampling 8 examples per class
train_dataset = sample_dataset(dataset["train"], label_column="label", num_samples=8)
...
```

...

</details>

### nemo-safe-synthesizer

Safe synthesizer

`pip install nemo-safe-synthesizer` · installs (wheel) · licence: Apache-2.0 · rank 10384 · last release 2026-10-23 · [PyPI](https://pypi.org/project/nemo-safe-synthesizer/)

<details><summary>README extract</summary>

NVIDIA NeMo Safe Synthesizer creates private, safe versions of sensitive tabular datasets -- entirely synthetic data with no one-to-one mapping to your original records. Purpose-built for privacy compliance and sensitive information protection while preserving data utility for downstream AI tasks.

Sections: 🛡️ NeMo Safe Synthesizer, Quick Start, Prerequisites, Run the public container, Running, Running the Pipeline, Subcommands, Managing Configurations, Attention Configuration, Training (`attn_implementation`), Generation (`attention_backend`), NIM Integration, Local Endpoint, Disable Classification

</details>

### agentenv-framework-protocol

Open data-plane protocol and server SDK for agent environments.

`pip install agentenv-framework-protocol` · installs (wheel) · licence: Apache-2.0 · rank 10424 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agentenv-framework-protocol/) · [docs](https://www.agentenvframework.com/docs) · [source](https://github.com/scaleapi/agentenv-framework/tree/main/packages/agentenv-protocol)

<details><summary>README extract</summary>

Example:
```python
from agentenv_protocol import ToolContext

    @tool(name="{environment_name}_list_inbox")
    def list_inbox(self, ctx: ToolContext) -> list[dict]:
        """Messages addressed to the caller."""
        return [m for m in self.messages if m["to"] == ctx.caller.role]
```

Sections: Errors, Who is calling, Serving, Framework-only routes and the control token, Tool access without a gateway, Tools served on another server's behalf, Resources, Instructions at connect, Getting part of the data, A skill for agents, Uploading an export through a grant, Calling an env's tools, Website readiness, Websites with tools

</details>

### probe-research

CLI + SDK + read-only MCP client for Probe Research (experiment tracking).

`pip install probe-research` · installs (wheel) · licence: Apache Software License · rank 10435 · last release 2026-11-08 · [PyPI](https://pypi.org/project/probe-research/) · [source](https://github.com/prbe-ai/research-os-agent)

<details><summary>README extract</summary>

> License & repo status (2026-08-12). This project is open source under
> Apache-2.0. The source of truth now lives in Probe's monorepo, and
> this repository is transitioning into a CI-generated distribution mirror
> carrying exactly what installations pull from here: the Claude Code / Codex
> plugin marketplace (`probe-research`, ...

Example:
```python
import probe

probe.init(
    project="folding",
    experiment="dockq-sweep",
    question="does a lower sampling temperature improve DockQ?",
)
probe.log({"loss": 0.42, "dockq": 0.71}, step=42)    # from anywhere, any thread
probe.finish()
```

...

</details>

### datarobot-early-access

This client library is designed to support the DataRobot API.

`pip install datarobot-early-access` · installs (wheel) · licence: DataRobot Tool and Utility Agreement · rank 10460 · last release 2026-11-02 · [PyPI](https://pypi.org/project/datarobot-early-access/) · [docs](https://datarobot-public-api-client.readthedocs-hosted.com/en/early-access/)

<details><summary>README extract</summary>

DataRobot is a client library for working with the DataRobot platform API. This package is the "early access" version of the client. Do NOT use this package in production--you will expose yourself to risk of breaking changes and bugs. For the most stable version, see the quarterly release on PyPI at ...

Example:
```python
import datarobot as dr
dr.Client(token='your_token', endpoint='
```

Sections: About datarobot_early_access, Usage, Extra, Helpful links, Bug Reporting and Q&A

</details>

### fev

fev: Forecast evaluation library

`pip install fev` · installs (wheel) · licence: Apache Software License · rank 10492 · last release 2026-08-31 · [PyPI](https://pypi.org/project/fev/)

<details><summary>README extract</summary>

`fev` (Forecast EValuation library) is a lightweight package that makes it easy to benchmark time series forecasting models.

- Extensible: Easy to define your own forecasting tasks and benchmarks.
- Reproducible: Ensures that the results obtained by different users are comparable.
- Easy to use: Compatible with most popular forecasting libraries. ...

Example:
```python
import fev

task = fev.Task(
    dataset_path="autogluon/chronos_datasets",
    dataset_config="m4_hourly",
    horizon=24,
)
```

Sections: fev, How is `fev` different from other benchmarking tools?, 🚀 Quickstart, 📚 Documentation, 🏅 Leaderboards, 📈 Datasets, Research code

</details>

### braindecode

Deep learning software to decode EEG, ECG or MEG signals

`pip install braindecode` · installs (wheel) · licence: BSD-3-Clause · rank 10586 · last release 2026-11-02 · [PyPI](https://pypi.org/project/braindecode/) · [docs](https://braindecode.org/stable/index.html) · [source](https://github.com/braindecode/braindecode)

<details><summary>README extract</summary>

Braindecode is an open-source Python toolbox for decoding raw electrophysiological brain
data with deep learning models. It includes dataset fetchers, data preprocessing and
visualization tools, as well as implementations of several deep learning architectures
and data augmentations for analysis of EEG, ECoG and MEG. ...

Sections: Braindecode, Documentation, Citing, Licensing, Additional Components

</details>

### datatile

A library for managing, summarizing, and visualizing data.

`pip install datatile` · installs (wheel) · licence: Apache 2.0 · rank 10669 · last release 2022-08-14 · [PyPI](https://pypi.org/project/datatile/)

### unified-planning

Unified Planning Framework

`pip install unified-planning` · installs (wheel) · licence: Apache Software License · rank 10728 · last release 2025-12-17 · [PyPI](https://pypi.org/project/unified-planning/)

<details><summary>README extract</summary>

Unified Planning: A library that makes it easy to formulate planning problems and to invoke automated planners.

</details>

### agent_governance_toolkit

Public Preview — Unified installer and runtime policy enforcement for the Agent Governance Toolkit

`pip install agent_governance_toolkit` · installs (wheel) · licence: MIT · rank 10888 · last release 2026-06-11 · [PyPI](https://pypi.org/project/agent_governance_toolkit/) · [docs](https://github.com/microsoft/agent-governance-toolkit/tree/main/docs) · [source](https://github.com/microsoft/agent-governance-toolkit)

<details><summary>README extract</summary>

Unified installer and runtime policy enforcement for the Agent Governance Toolkit

*One install for the complete governance stack — kernel · trust mesh · runtime supervisor · reliability engineering*

> [!IMPORTANT]
> Public Preview — The `agent-governance-toolkit` package on PyPI is a public preview release. APIs may change before GA. ...

Features:
Running AI agents in production without governance is like deploying microservices without TLS, RBAC, or monitoring. Each layer solves a different problem:

| Concern | Without Governance | With Agent Governance | ...

Example:
```python
import asyncio
from agent_os import StatelessKernel, ExecutionContext
from agentmesh import AgentIdentity

# Boot the governance kernel
kernel = StatelessKernel()
...

</details>

### owlready2

A package for ontology-oriented programming in Python: load OWL 2.0 ontologies as Python objects, modify them, save them, and perform reasoning via HermiT. Includes an optimized RDF quadstore.

`pip install owlready2` · installs from source (sdist only) · licence: LGPL-3.0-or-later · rank 10918 · last release 2026-06-22 · [PyPI](https://pypi.org/project/owlready2/)

_README extract left out: share-alike licence._

### lmstudio

LM Studio Python SDK

`pip install lmstudio` · installs (wheel) · licence: not stated · rank 10926 · last release 2025-08-22 · [PyPI](https://pypi.org/project/lmstudio/) · [docs](https://lmstudio.ai/docs/sdk/)

<details><summary>README extract</summary>

Example:
```python
import lmstudio as lms

model = lms.llm()
model.complete("Once upon a time,")
```

Sections: LM Studio Python SDK, Using the SDK, Examples, SDK versioning, Fetching the source code, Recommended local checks, Code consistency checks, Expanding the API

</details>

### sequence-ai

The inference and benchmark platform for physical AI: deploy a robot policy, run it on your robot, score it.

`pip install sequence-ai` · installs (wheel) · licence: Apache-2.0 · rank 10957 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sequence-ai/) · [docs](https://generalsequences.com/docs/)

<details><summary>README extract</summary>

Deploy a robot policy, then drive a robot with it.

Your key, which starts `seq_dev`, manages your policies and reads the account, so the CLI and your own code
use it; making keys, paying and changing the account take you signed in (`seq login`, once, in your browser; `seq
login --profile NAME` keeps another sign-in apart, and `seq profile list` ...

Features:
Three things, and each of them is something a loop written straight against the HTTP endpoints
has to get right before it behaves properly on a robot:

| | Without it | ...

Example:
```python
import sequence_ai

with sequence_ai.connect(model="my_pi05_user") as policy_user:  # your deployment, by the name you gave it
    while not done_user():
...

</details>

### dex-retargeting

Hand pose retargeting for dexterous robot hand.

`pip install dex-retargeting` · does not install on CPython 3.14 · licence: MIT License · rank 10998 · last release 2025-04-05 · [PyPI](https://pypi.org/project/dex-retargeting/)

<details><summary>README extract</summary>

Example:
```python
from dex_retargeting.seq_retarget import SeqRetargeting

retargeting: SeqRetargeting
sapien_joint_names = [joint.get_name() for joint in robot.get_active_joints()]
retargeting_joint_names = retargeting.joint_names
retargeting_to_sapien = np.array([retargeting_joint_names.index(name) for name in sapien_joint_names]).astype(int)

...
```

Sections: Dex Retargeting, This repo originates from AnyTeleop Project, v0.5.0, Examples, Retargeting from human hand video, Retarget from hand object pose dataset, FAQ and Troubleshooting, Joint Orders for Retargeting

</details>

### autogluon.multimodal

Fast and Accurate ML in 3 Lines of Code

`pip install autogluon.multimodal` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 11030 · last release 2026-09-18 · [PyPI](https://pypi.org/project/autogluon.multimodal/) · [docs](https://auto.gluon.ai) · [source](https://github.com/autogluon/autogluon/)

<details><summary>README extract</summary>

Installation | Documentation | Release Notes

AutoGluon, developed by AWS AI, automates machine learning tasks enabling you to easily achieve strong predictive performance in your applications. ...

Example:
```python
from autogluon.tabular import TabularPredictor
predictor = TabularPredictor(label="class").fit("train.csv", presets="best")
predictions = predictor.predict("test.csv")
```

Sections: Fast and Accurate ML in 3 Lines of Code, zap: Quickstart, mag: Resources, Hands-on Tutorials / Talks, Scientific Publications, Articles, Train/Deploy AutoGluon in the Cloud, pencil: Citing AutoGluon, wave: How to get involved

</details>

### quadrilateral-fitter

QuadrilateralFitter is an efficient and easy-to-use Python library for fitting irregular quadrilaterals from irregular polygons or any noisy data.

`pip install quadrilateral-fitter` · installs (wheel) · licence: MIT License · rank 11126 · last release 2024-08-28 · [PyPI](https://pypi.org/project/quadrilateral-fitter/)

<details><summary>README extract</summary>

QuadrilateralFitter is an efficient and easy-to-use library for fitting irregular quadrilaterals from polygons or point clouds.

QuadrilateralFitter helps you find that four corners polygon that best approximates your noisy data or detection, so you can apply further processing steps like: _perspective correction or _pattern matching, without ...

Example:
```python
from quadrilateral_fitter import QuadrilateralFitter

# Fit an input polygon of N sides
fitted_quadrilateral = QuadrilateralFitter(polygon=your_noisy_polygon).fit()
```

Sections: QuadrilateralFitter, Usage, API Reference, QuadrilateralFitter(polygon), QuadrilateralFitter.fit(simplify_polygons_larger_than = 10), Real Case Example

</details>

### batchgeneratorsv2

Batchgenerators but better

`pip install batchgeneratorsv2` · installs (wheel) · licence: Apache Software License · rank 11137 · last release 2026-10-29 · [PyPI](https://pypi.org/project/batchgeneratorsv2/)

<details><summary>README extract</summary>

This repository is work in progress. If builds upon the batchgenerators
framework but makes several key changes to the transforms:

1. Transforms now explicitly distinguish between data types: images, segmentation, pixel-wise regression target, keypoints, bbox
2. All transforms have been reimplemented from scratch with a focus on performance. ...

</details>

### exomem

Local knowledge substrate for owned markdown/Obsidian vaults, exposed through MCP, REST, and CLI with multimodal OCR/ASR/CLIP search

`pip install exomem` · installs (wheel) · licence: AGPL-3.0-or-later · rank 11147 · last release 2026-11-08 · [PyPI](https://pypi.org/project/exomem/) · [docs](https://github.com/Artexis10/exomem/blob/main/QUICKSTART.md) · [source](https://github.com/Artexis10/exomem)

_README extract left out: share-alike licence._

### datamol

A python library to work with molecules. Built on top of RDKit.

`pip install datamol` · installs (wheel) · licence: Apache-2.0 · rank 11184 · last release 2026-09-09 · [PyPI](https://pypi.org/project/datamol/) · [docs](https://docs.datamol.io) · [source](https://github.com/datamol-io/datamol)

<details><summary>README extract</summary>

datamol - molecular processing made easy

 Docs

 Homepage

Datamol is a python library to work with molecules. It's a layer built on top of RDKit and aims to be as light as possible.

- 🐍 Simple pythonic API
- ⚗️ RDKit first: all you manipulate are `rdkit.Chem.Mol` objects. ...

Example:
```python
import datamol as dm

# Common functions
mol = dm.to_mol("O=C(C)Oc1ccccc1C(=O)O", sanitize=True)
fp = dm.to_fp(mol)
selfies = dm.to_selfies(mol)
inchi = dm.to_inchi(mol)

# Standardize and sanitize
mol = dm.to_mol("O=C(C)Oc1ccccc1C(=O)O")
mol = dm.fix_mol(mol)
mol = dm.sanitize_mol(mol)
mol = dm.standardize_mol(mol)

# Dataframe manipulation
...
```

Sections: Try Online, Documentation, Updates, Quick API Tour, Compatibilities

</details>

### codecarbon

Track and reduce the CO2 emissions of your computing

`pip install codecarbon` · installs (wheel) · licence: MIT · rank 11193 · last release 2026-10-23 · [PyPI](https://pypi.org/project/codecarbon/) · [docs](https://docs.codecarbon.io/) · [source](https://github.com/mlco2/codecarbon)

<details><summary>README extract</summary>

Estimate and track carbon emissions from your computer, quantify and analyze their impact.

- A lightweight, easy to use Python library – Simple API to track emissions
- Open source, free & community driven – Built by and for the community
- Effective visual outputs – Put emissions in context with real-world equivalents ...

Example:
```python
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# Your code here

emissions = tracker.stop()
print(f"Emissions: {emissions} kg CO₂")
```

Sections: Track & reduce CO₂ emissions from your local computing, Quickstart (Python), Quickstart (CLI), Configuration, How it works, Visualize, Quick links, Links, Contact

</details>

### paper-qa

LLM Chain for answering questions from docs

`pip install paper-qa` · installs (wheel) · licence: Apache Software License · rank 11200 · last release 2026-08-12 · [PyPI](https://pypi.org/project/paper-qa/) · [source](https://github.com/Future-House/paper-qa)

<details><summary>README extract</summary>

<!-- pyml disable-num-lines 6 line-length -->

PaperQA2 is a package for doing high-accuracy retrieval augmented generation (RAG) on PDFs, text files, Microsoft Office documents, and source code files,
with a focus on the scientific literature. ...

Example:
```python
from paperqa import Settings, ask

answer_response = ask(
    "What is PaperQA2?",
    settings=Settings(temperature=0.5, paper_directory="my_papers"),
)
```

Sections: PaperQA2, Quickstart, Example Output, What is PaperQA2, PaperQA2 vs PaperQA, PaperQA2 Goes CalVer in December 2025, What's New in Version 5 (aka PaperQA2)?, What's New in December 2025?, PaperQA2 Algorithm, CLI Usage, Bundled Settings, Rate Limits, Library Usage, Agentic Adding/Querying Documents

</details>

### fastcluster

Fast hierarchical clustering routines for R and Python.

`pip install fastcluster` · installs from source (sdist only) · licence: BSD License; GNU General Public License v2 (GPLv2) · rank 11244 · last release 2025-05-06 · [PyPI](https://pypi.org/project/fastcluster/)

_README extract left out: share-alike licence._

### interpret

Fit interpretable models. Explain blackbox machine learning.

`pip install interpret` · installs (wheel) · licence: not stated · rank 11295 · last release 2026-03-17 · [PyPI](https://pypi.org/project/interpret/)

<details><summary>README extract</summary>

In the beginning machines learned in darkness, and data scientists struggled in the void to explain them.

Let there be light.

</details>

### faiss-gpu-cu12

A library for efficient similarity search and clustering of dense vectors.

`pip install faiss-gpu-cu12` · does not install on CPython 3.14 · licence: MIT License · rank 11338 · last release 2026-03-07 · [PyPI](https://pypi.org/project/faiss-gpu-cu12/)

<details><summary>README extract</summary>

This repository is based on kyamagu/faiss-wheels.

Features:
This repository provides scripts to build GPU-enabled wheels for the faiss library.
Distributes `faiss-gpu-cuXX` packages to PyPI using the contents of this repository.

Sections: faiss-wheels, Overview, Key Features, Important Requirements, For CUDA 12, For CUDA 11, Driver Compatibility Reference, Advanced: Using System CUDA Libraries, Versioning, Building from Source, Build Configuration, Build Commands, Build Requirements

</details>

### forecasting-tools

AI forecasting and research tools to help humans reason about and forecast the future

`pip install forecasting-tools` · installs (wheel) · licence: MIT · rank 11356 · last release 2026-11-08 · [PyPI](https://pypi.org/project/forecasting-tools/) · [source](https://github.com/Metaculus/forecasting-tools)

<details><summary>README extract</summary>

Features:
This repository contains forecasting and research tools built with Python and Streamlit. The project aims to assist users in making predictions, conducting research, and analyzing data related to hard to answer questions (especially those from ...

Example:
```python
from forecasting_tools import TemplateBot, MetaculusClient, GeneralLlm

bot = TemplateBot(
    research_reports_per_question=3,  # Number of separate research attempts per question
    predictions_per_research_report=5,  # Number of predictions to make per research report
...
```

...

</details>

### agentrust-trace

TRACE v0.2: hardware-attested governance records for AI agents

`pip install agentrust-trace` · installs (wheel) · licence: Apache Software License · rank 11364 · last release 2026-09-25 · [PyPI](https://pypi.org/project/agentrust-trace/) · [source](https://github.com/agentrust-io/trace-spec)

<details><summary>README extract</summary>

Community updates and contributor highlights: AgenTrust on LinkedIn.

 Specification |
 Schema |
 Examples |
 Test Suite |
 Reference Impl

 TRACE Specification is an LF Project, hosted at the Linux Foundation as its own series, "TRACE Specification, a Series of LF Projects, LLC".

> Developer Preview. ...

Example:
```python
import time
from agentrust_trace import generate_key, sign_record

key = generate_key()

record = {
    "eat_profile": "tag:agentrust-io.com,2026:trace-v0.2",
    "iat": int(time.time()),
    "subject": "spiffe://trust.example.org/agent/payments-processor",
    "model": {"provider": "example-provider", "model_id": "example-model-1"},
...
```

...

</details>

### phidata

Build multi-modal Agents with memory, knowledge and tools.

`pip install phidata` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11395 · last release 2025-01-27 · [PyPI](https://pypi.org/project/phidata/) · [docs](https://docs.phidata.com)

<details><summary>README extract</summary>

Phidata is a framework for building multi-modal agents, use phidata to:

- Build multi-modal agents with memory, knowledge, tools and reasoning.
- Build teams of agents that can work together to solve problems.
- Chat with your agents using a beautiful Agent UI.

Features:
- Simple & Elegant
- Powerful & Flexible
- Multi-Modal by default
- Multi-Agent orchestration
- A beautiful Agent UI to chat with your agents
- Agentic RAG built-in
- Structured Outputs
- Reasoning Agents
- Monitoring & Debugging built-in ...

Example:
```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
...

</details>

### dstack

dstack is an open-source orchestration engine for running AI workloads on any cloud or on-premises.

`pip install dstack` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 11402 · last release 2026-11-04 · [PyPI](https://pypi.org/project/dstack/) · [docs](https://dstack.ai/docs) · [source](https://github.com/dstackai/dstack)

<details><summary>README extract</summary>

`dstack` is a unified control plane for GPU provisioning and orchestration that works with any GPU cloud, Kubernetes, or on-prem clusters.

It streamlines development, training, and inference, and is compatible with any hardware, open-source tools, and frameworks. ...

Sections: Accelerators, Latest news ✨, How does it work?, Launch the server, Define configurations, Apply configurations, Useful links

</details>

### atif

Pydantic models for the Agent Trajectory Interchange Format (ATIF v1.8).

`pip install atif` · installs (wheel) · licence: MIT · rank 11441 · last release 2026-10-11 · [PyPI](https://pypi.org/project/atif/) · [source](https://github.com/bolu61/python-atif)

<details><summary>README extract</summary>

Pydantic models for the Agent Trajectory Interchange Format (ATIF), a
standardized JSON schema for logging the complete interaction history of
autonomous LLM agents (user messages, agent responses, tool calls, observations,
metrics, and embedded subagent trajectories). Implements ATIF v1.8. ...

Example:
```python
from atif import Trajectory

data = {
    "schema_version": "ATIF-v1.8",
    "agent": {"name": "my-agent", "version": "1.0.0", "model_name": "claude-sonnet-4-6"},
    "steps": [
        {"step_id": 1, "source": "user", "message": "What time is it?"},
        {
            "step_id": 2,
            "source": "agent",
...
```

Sections: atif, Usage, Versioning, AI disclosure

</details>

### novita-sandbox

Novita Agent Sandbox SDK - Python library for Novita Agent Sandbox

`pip install novita-sandbox` · installs (wheel) · licence: MIT License · rank 11450 · last release 2026-11-05 · [PyPI](https://pypi.org/project/novita-sandbox/) · [docs](https://novita.ai/docs/guides/sandbox-overview)

<details><summary>README extract</summary>

A Python SDK for Novita Agent Sandbox environments that provides code execution, desktop automation, and cloud computing capabilities..

📖 Documentation • 🔑 Get API Key

Features:
- Code Interpreter: Execute Python, JavaScript, and other languages in isolated environments
- Desktop Automation: Control desktop applications and GUI interactions
- Cloud Computing: Scalable sandbox environments for various computing tasks ...

Example:
```python
import os
from novita_sandbox import Novita

novita = Novita(api_key=os.getenv("NOVITA_API_KEY", ""))

# Using the official template `base` by default
sandbox = novita.sandbox.create("base")

# File operations
sandbox.files.write('/tmp/test.txt', 'Hello, World!')
content = sandbox.files.read('/tmp/test.txt')

# Command execution
...
```

...

</details>

### paper-qa-pypdf

PaperQA readers implemented using PyPDF

`pip install paper-qa-pypdf` · installs (wheel) · licence: Apache Software License · rank 11474 · last release 2026-08-12 · [PyPI](https://pypi.org/project/paper-qa-pypdf/)

<details><summary>README extract</summary>

<!-- pyml disable-num-lines 6 line-length -->

PDF reading code backed by
PyPDF.

To also parse images or take full-page screenshots,
use the `media` extra: `pip install paper-qa-pypdf[media]`.
This is backed by pypdfium2. ...

</details>

### microsoft-agents-a365-runtime

Telemetry, tracing, and monitoring components for AI agents

`pip install microsoft-agents-a365-runtime` · installs (wheel) · licence: MIT · rank 11493 · last release 2026-10-20 · [PyPI](https://pypi.org/project/microsoft-agents-a365-runtime/) · [docs](https://github.com/microsoft/Agent365-python/tree/main/libraries/microsoft-agents-a365-runtime) · [source](https://github.com/microsoft/Agent365-python)

<details><summary>README extract</summary>

Core runtime utilities and environment management for AI agent applications. This package provides essential Power Platform API discovery, environment configuration, and authentication scope resolution.

Sections: microsoft-agents-a365-runtime, Usage, Trademarks

</details>

### microsoft-agents-a365-observability-core

Telemetry, tracing, and monitoring components for AI agents

`pip install microsoft-agents-a365-observability-core` · installs (wheel) · licence: MIT · rank 11545 · last release 2026-10-20 · [PyPI](https://pypi.org/project/microsoft-agents-a365-observability-core/) · [docs](https://github.com/microsoft/Agent365-python/tree/main/libraries/microsoft-agents-a365-observability-core) · [source](https://github.com/microsoft/Agent365-python)

<details><summary>README extract</summary>

Telemetry, tracing, and monitoring components for AI agents built on OpenTelemetry. This package provides structured spans for agent invocation, tool execution, and LLM inference with context propagation and pluggable exporters. ...

Sections: microsoft-agents-a365-observability-core, Usage, Agent 365 OBS export authentication, Trademarks

</details>

### minigrid

Minimalistic gridworld reinforcement learning environments.

`pip install minigrid` · installs (wheel) · licence: MIT License · rank 11600 · last release 2026-10-15 · [PyPI](https://pypi.org/project/minigrid/) · [docs](https://minigrid.farama.org/) · [source](https://minigrid.farama.org/)

<details><summary>README extract</summary>

The Minigrid library contains a collection of discrete grid-world environments to conduct research on Reinforcement Learning. The environments follow the Gymnasium standard API and they are designed to be lightweight, fast, and easily customizable. ...

Sections: Environments, Minigrid, BabyAI, Training an Agent

</details>

### rtdl_num_embeddings

On Embeddings for Numerical Features in Tabular Deep Learning.

`pip install rtdl_num_embeddings` · installs (wheel) · licence: Apache Software License · rank 11610 · last release 2025-04-13 · [PyPI](https://pypi.org/project/rtdl_num_embeddings/) · [docs](https://github.com/yandex-research/rtdl-num-embeddings/tree/main/package/README.md) · [source](https://github.com/yandex-research/rtdl-num-embeddings/tree/main/package/README.md)

### openvino-tokenizers

Convert tokenizers into OpenVINO models

`pip install openvino-tokenizers` · installs (wheel) · licence: Apache Software License · rank 11614 · last release 2026-10-01 · [PyPI](https://pypi.org/project/openvino-tokenizers/)

<details><summary>README extract</summary>

OpenVINO Tokenizers adds text processing operations to OpenVINO.

Features:
- Perform tokenization and detokenization without third-party dependencies
- Convert a HuggingFace tokenizer into OpenVINO model tokenizer and detokenizer
- Combine OpenVINO models into a single model ...

Example:
```python
import numpy as np
from transformers import AutoTokenizer
from openvino import compile_model, save_model
from openvino_tokenizers import convert_tokenizer

hf_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
ov_tokenizer = convert_tokenizer(hf_tokenizer)

compiled_tokenzier = compile_model(ov_tokenizer)
text_input = ["Test string"]

...
```

...

</details>

### rdt

Reversible Data Transforms

`pip install rdt` · installs (wheel) · licence: BUSL-1.1 · rank 11635 · last release 2026-10-30 · [PyPI](https://pypi.org/project/rdt/) · [source](https://github.com/sdv-dev/RDT/)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
RDT (Reversible Data Transforms) is a Python library that transforms raw data into fully numerical
data, ready for data science. The transforms are reversible, allowing you to convert from numerical
data back into your original format.

Example:
```python
from rdt import get_demo

customers = get_demo()
```

Sections: Overview, Quickstart, Load the demo data, Creating the HyperTransformer & config, Fitting & using the HyperTransformer, What's Next?

</details>

### uniception

Generalizable Perception Stack for 3D, 4D, spatial AI and scene understanding

`pip install uniception` · installs (wheel) · licence: BSD 3-Clause · rank 11886 · last release 2026-03-22 · [PyPI](https://pypi.org/project/uniception/) · [docs](https://github.com/castacks/UniCeption/blob/main/README.md)

<details><summary>README extract</summary>

UniCeption houses modular building blocks for developing and training generalizable perception models for all things related to 3D, 4D, spatial AI and scene understanding.
It is designed to be flexible and extensible, allowing researchers to easily experiment with different architectures and configurations. ...

Sections: UniCeption, Downloading Checkpoints, Encoders, Information Sharing Blocks, Prediction Heads, Codebases built on top of UniCeption

</details>

### torch-optimizer

pytorch-optimizer

`pip install torch-optimizer` · installs (wheel) · licence: Apache Software License · rank 11908 · last release 2021-10-31 · [PyPI](https://pypi.org/project/torch-optimizer/) · [docs](https://pytorch-optimizer.readthedocs.io)

<details><summary>README extract</summary>

torch-optimizer -- collection of optimizers for PyTorch compatible with optim
module.

Example:
```python
import torch_optimizer as optim

# model = ...
optimizer = optim.DiffGrad(model.parameters(), lr=0.001)
optimizer.step()
```

Sections: torch-optimizer, Simple example, Documentation, Visualizations, Warning, A2GradExp, A2GradInc, A2GradUni, AccSGD, AdaBelief, AdaBound, AdaMod, Adafactor, Adahessian

</details>

### coqui-tts-trainer

General purpose model trainer for PyTorch that is more flexible than it should be, by 🐸Coqui.

`pip install coqui-tts-trainer` · installs (wheel) · licence: Apache Software License · rank 11923 · last release 2026-04-10 · [PyPI](https://pypi.org/project/coqui-tts-trainer/) · [source](https://github.com/idiap/coqui-ai-Trainer)

<details><summary>README extract</summary>

An opinionated general purpose model trainer on PyTorch with a simple code base.
Fork of the original, unmaintained repository. New PyPI package: coqui-tts-trainer

Example:
```python
import torch
profiler = torch.profiler.profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.CUDA,
    ],
    schedule=torch.profiler.schedule(wait=1, warmup=1, active=3, repeat=2),
    on_trace_ready=torch.profiler.tensorboard_trace_handler("./profiler/"),
    record_shapes=True,
...
```

Sections: 👟 Trainer, Implementing a model, Training a model with auto-optimization, Training a model with advanced optimization, Training with Batch Size Finder, Training with DDP, Training with Accelerate, Adding a callback, Profiling example

</details>

### gymnax

JAX-native reinforcement-learning environments

`pip install gymnax` · installs (wheel) · licence: Apache-2.0 · rank 12005 · last release 2026-10-18 · [PyPI](https://pypi.org/project/gymnax/)

<details><summary>README extract</summary>

Reinforcement Learning Environments in JAX 🌍

Are you fed up with slow CPU-based RL environment processes? Do you want to leverage massive vectorization for high-throughput RL experiments? `gymnax` brings the power of `jit` and `vmap`/`pmap` to the classic gym API. ...

Example:
```python
import jax
import jax.numpy as jnp
import gymnax

key = jax.random.key(0)
key, key_reset, key_act, key_step = jax.random.split(key, 4)

# Instantiate the environment & its settings.
env, env_params = gymnax.make("Pendulum-v1")

# Reset the environment.
obs, state = env.reset(key_reset, env_params)

# Sample a random action.
...
```

...

</details>

### ethos-u-vela

Neural network model compiler for Arm Ethos-U NPUs

`pip install ethos-u-vela` · installs from source (sdist only) · licence: Apache-2.0 · rank 12047 · last release 2026-09-03 · [PyPI](https://pypi.org/project/ethos-u-vela/)

<details><summary>README extract</summary>

<!--
SPDX-FileCopyrightText: Copyright 2020-2026 Arm Limited and/or its affiliates <open-source-office@arm.com>

SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the License); you may
not use this file except in compliance with the License.
You may obtain a copy of the License at ...

Sections: Vela, Requirements, Manually Building, Discover available nightly versions, Getting Started, Output, Warnings, Performance information, Additional Vela Information, Inclusive language commitment

</details>

### cpm-kernels

CPM CUDA kernels

`pip install cpm-kernels` · installs (wheel) · licence: Apache Software License · rank 12070 · last release 2022-03-07 · [PyPI](https://pypi.org/project/cpm-kernels/)

### jax-jumpy

Common backend for Jax or Numpy.

`pip install jax-jumpy` · installs (wheel) · licence: Apache Software License · rank 12109 · last release 2023-03-17 · [PyPI](https://pypi.org/project/jax-jumpy/) · [source](https://github.com/Farama-Foundation/Jumpy)

<details><summary>README extract</summary>

Jumpy is a common backend for NumPy and optionally JAX:

* If Jax is installed and jax inputs are provided then the `jax.numpy` function is run
* If Jax is installed and the function is jitted then the `jax.numpy` function is run
* Otherwise the jumpy function returns the NumPy outputs

There are several functions (e.g. ...

</details>

### strands-agents-builder

An example Strands agent demonstrating streaming, tool use, and interactivity from your terminal. This agent builder can help you to build your own agents and tools.

`pip install strands-agents-builder` · installs (wheel) · licence: Apache Software License · rank 12118 · last release 2025-09-17 · [PyPI](https://pypi.org/project/strands-agents-builder/) · [docs](https://strandsagents.com)

<details><summary>README extract</summary>

Documentation
 ◆ Samples
 ◆ Python SDK
 ◆ Tools
 ◆ Agent Builder
 ◆ MCP Server

An interactive Strands agent toolkit designed to help you build, test, and extend your own custom AI agents and tools. With the Strands Agent Builder, you can create specialized agents, develop custom tools, and compose complex AI workflows—all from your terminal.

Features:
- 🏗️ Create and test custom tools with instant hot-reloading
- 🤖 Build specialized agents with focused capabilities
- 🔄 Extend existing tools and enhance their functionality
- 💬 Interactive command-line interface with rich output ...

...

</details>

### agentenv-framework

SDK and CLI for building, deploying and running agent environments and the tasks that grade agents in them.

`pip install agentenv-framework` · installs (wheel) · licence: Apache-2.0 · rank 12124 · last release 2026-11-08 · [PyPI](https://pypi.org/project/agentenv-framework/) · [docs](https://www.agentenvframework.com/docs) · [source](https://github.com/scaleapi/agentenv-framework)

<details><summary>README extract</summary>

AgentEnv Framework is a Python SDK and CLI for building, deploying and running agentic environments and the tasks that grade agents inside them. Environments are containerized servers that speak the open `agentenv-framework-protocol`; AgentEnv Framework builds them into versioned images, deploys them behind a gateway, points an agent at them, and ...

Sections: Run a bundle from the Hub, Plugins, OpenEnv, Time zones, Documentation map, Versioning and compatibility

</details>

### chematic

Pure-Rust cheminformatics — SMILES, fingerprints, 190+ descriptors, pKa, ADMET

`pip install chematic` · installs from source (sdist only) · licence: Apache Software License; MIT License · rank 12163 · last release 2026-10-23 · [PyPI](https://pypi.org/project/chematic/) · [docs](https://docs.rs/chematic) · [source](https://github.com/kent-tokyo/chematic)

<details><summary>README extract</summary>

Pure-Rust cheminformatics library for Python — SMILES parsing, descriptors,
fingerprints, substructure search, formats, reactions, and bounded 3D tools.

The current published line is 1.1.3. It includes molecule pickling, indexed
SDF access, V3000 bond-stereo collections, and reusable Python MMFF94/UFF
force fields. ...

Features:
- Zero C/C++ dependencies — pure Rust, no RDKit or OpenBabel required
- SMILES / MOL / SDF / ChemicalJSON parsing and writing
- Indexed SDF datasets — `SdfDataset` provides cheap record counts,
 metadata, random access, and bounded range reads ...

Example:
```python
import chematic

mol = chematic.from_smiles("CC(=O)Oc1ccccc1C(=O)O")  # aspirin

print(mol.mw)      # 180.16
print(mol.logp)    # 1.31
print(mol.tpsa)    # 63.6
print(mol.qed)     # 0.55

...

</details>

### langfun

Langfun: Language as Functions.

`pip install langfun` · installs (wheel) · licence: Apache Software License · rank 12216 · last release 2024-07-23 · [PyPI](https://pypi.org/project/langfun/)

<details><summary>README extract</summary>

Installation | Getting started | Tutorial

Langfun is a PyGlove powered library that
aims to *make language models (LM) fun to work with*. Its central principle is
to enable seamless integration between natural language and programming by
treating language as functions. ...

Features:
Langfun is *powerful and scalable*:

* Seamless integration between natural language and computer programs.
* Modular prompts, which allows a natural blend of texts and modalities;
* Efficient for both request-based workflows and batch jobs;
* A ...

Example:
```python
import langfun as lf
import pyglove as pg

from IPython import display

class Item(pg.Object):
  name: str
  color: str

class ImageDescription(pg.Object):
  items: list[Item]

image = lf.Image.from_uri('
display.display(image)

...

</details>

### colpali-engine

The code used to train and run inference with the ColPali architecture.

`pip install colpali-engine` · installs (wheel) · licence: MIT License · rank 12226 · last release 2026-08-22 · [PyPI](https://pypi.org/project/colpali-engine/)

<details><summary>README extract</summary>

[[Model card]](
[[ViDoRe Leaderboard]](
[[Demo]](
[[Blog Post]](

This repository contains the code used for training and running visual document retrievers introduced by the *ColPali: Efficient Document Retrieval with Vision Language Models* paper. ...

Example:
```python
import torch
from PIL import Image
from transformers.utils.import_utils import is_flash_attn_2_available

from colpali_engine.models import ColQwen2, ColQwen2Processor

model_name = "vidore/colqwen2-v1.0"

model = ColQwen2.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",  # or "mps" if on Apple Silicon
...
```

...

</details>

### gandalf-the-grader

Agent-as-judge grading framework for evaluating AI agent outputs against rubric criteria

`pip install gandalf-the-grader` · installs (wheel) · licence: Apache-2.0 · rank 12261 · last release 2026-10-19 · [PyPI](https://pypi.org/project/gandalf-the-grader/) · [source](https://github.com/Handshake-AI-Research/gandalf-the-grader)

<details><summary>README extract</summary>

Read the launch blog post for the motivation, benchmark results, and design rationale behind Gandalf.

Gandalf is a reactive agent-as-judge for rubric-graded agent environments. ...

Sections: Gandalf the Grader, Runtime dependencies, Quick start, Configuration, `grader.toml`, Custom Judge Prompt, Rubric JSON, Trajectory Format (ATIF), Environment Variables, Tracing / Observability, Output, Next steps

</details>

### lion-pytorch

Lion Optimizer - Pytorch

`pip install lion-pytorch` · installs (wheel) · licence: MIT License · rank 12283 · last release 2026-07-09 · [PyPI](https://pypi.org/project/lion-pytorch/) · [source](https://codeberg.org/lucidrains/lion-pytorch)

<details><summary>README extract</summary>

🦁 Lion, EvoLved Sign Momentum, new optimizer discovered by Google Brain that is purportedly better than Adam(w), in Pytorch. This is nearly a straight copy from here, with few minor modifications.

It is so simple, we may as well get it accessible and used asap by everyone to train some great models, if it really works 🤞 ...

Example:
```python
# toy model

import torch
from torch import nn

model = nn.Linear(10, 1)

# import Lion and instantiate with parameters

from lion_pytorch import Lion

opt = Lion(model.parameters(), lr=1e-4, weight_decay=1e-2)

# forward and backwards

loss = model(torch.randn(10))
loss.backward()

# optimizer step

opt.step()
opt.zero_grad()
```

Sections: 🦁 Lion - Pytorch, Instructions, Updates, Usage, Appreciation

</details>

### neptune

Neptune Client

`pip install neptune` · installs (wheel) · licence: Apache Software License · rank 12290 · last release 2026-03-17 · [PyPI](https://pypi.org/project/neptune/) · [docs](https://docs.neptune.ai/) · [source](https://github.com/neptune-ai/neptune-client)

<details><summary>README extract</summary>

Website
 Docs
 Blog

> [!IMPORTANT]
> This is the Python client for Neptune app version `2.x`.

> For the new Neptune client, go to neptune-client-scale →

> [!NOTE]
> For Neptune `2.x` setup and instructions, see the documentation.

</details>

### torchprofile

Count the MACs / FLOPs of PyTorch models

`pip install torchprofile` · installs (wheel) · licence: MIT License · rank 12330 · last release 2026-03-10 · [PyPI](https://pypi.org/project/torchprofile/) · [source](https://github.com/zhijian-liu/torchprofile)

<details><summary>README extract</summary>

TorchProfile counts the number of MACs (multiply-accumulate operations) in a PyTorch model. It works by tracing the computation graph with `torch.jit.trace`, making it more accurate than hook-based profilers and more general than ONNX-based ones.

Example:
```python
import torch
from transformers import AutoModel
from torchprofile import profile_macs

model = AutoModel.from_pretrained("meta-llama/Llama-3.2-1B").eval()
inputs = torch.randint(0, model.config.vocab_size, (1, 128))

macs = profile_macs(model, inputs)
print(f"{macs / 1e9:.2f} GMACs")
```

Sections: TorchProfile, Quick Start

</details>

### faiss-gpu

A library for efficient similarity search and clustering of dense vectors (GPU support).

`pip install faiss-gpu` · installs (wheel) · licence: MIT · rank 12402 · last release 2026-09-16 · [PyPI](https://pypi.org/project/faiss-gpu/) · [docs](https://github.com/facebookresearch/faiss/wiki) · [source](https://github.com/facebookresearch/faiss)

<details><summary>README extract</summary>

Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. ...

Sections: Faiss, News, Introduction, How Faiss works, Full documentation of Faiss, Reference, Legal

</details>

### lmcache

A LLM serving engine extension to reduce TTFT and increase throughput, especially under long-context scenarios.

`pip install lmcache` · installs (wheel) · licence: Apache-2.0 · rank 12410 · last release 2026-11-06 · [PyPI](https://pypi.org/project/lmcache/) · [source](https://github.com/LMCache/LMCache)

<details><summary>README extract</summary>

Documentation |
 FAQ |
 Join Slack |
 Community Meeting |
 Roadmap

 ⭐ If LMCache helps you serve LLMs faster and cheaper, give us a star — it helps more teams discover the project.

- [2026/05] 🔥 Agentic workload benchmark on AMD MI300X (blog).
- [2026/04] 🔥 LMCache's new multiprocess (MP) architecture release (blog). ...

Features:
- Engine-independent deployment: LMCache, as a standalone daemon process, manages KV cache independently from the inference engine process, so that KV cache will not be lost even if the inference engine crashes (i.e., no fate-sharing with engines). ...

Sections: A KV Cache Management Layer for Scalable LLM Inference, Blog |, Updates, About, Key features, Getting Started, Adoption and Partnerships

</details>

### semble

Fast and Accurate Code Search for Agents

`pip install semble` · installs (wheel) · licence: MIT License · rank 12430 · last release 2026-11-03 · [PyPI](https://pypi.org/project/semble/) · [source](https://github.com/MinishLab/semble)

<details><summary>README extract</summary>

Fast and Accurate Code Search for Agents

 Uses ~99% fewer tokens than grep+read

Quickstart •
CLI •
MCP Server •
Installation •
Benchmarks

Semble is a code search library built for agents. It returns the exact code snippets they need instantly, using ~99% fewer tokens than grep+read. ...

Example:
```python
from semble import ContentType, SembleIndex

# Index a local directory (code only, the default)
index = SembleIndex.from_path("./my-project")

# Index docs and prose (markdown, rst, etc.)
index = SembleIndex.from_path("./my-project", content=ContentType.DOCS)

# Index everything (code, docs, and config)
...
```

Sections: Quickstart, Main Features, CLI, MCP Server, Benchmarks, How it works, Using a custom model, Citing

</details>

### layoutparser

A unified toolkit for Deep Learning Based Document Image Analysis

`pip install layoutparser` · installs (wheel) · licence: Apache Software License · rank 12436 · last release 2022-04-06 · [PyPI](https://pypi.org/project/layoutparser/)

<details><summary>README extract</summary>

LayoutParser aims to provide a wide range of tools that aims to streamline Document Image Analysis (DIA) tasks. Please check the LayoutParser demo video (1 min) or full talk (15 min) for details. And here are some key features: ...

Example:
```python
import layoutparser as lp
model = lp.AutoLayoutModel('lp://EfficientDete/PubLayNet')
# image = Image.open("path/to/image")
layout = model.detect(image)
```

Sections: What is LayoutParser, Examples, Citing `layoutparser`

</details>

### langchain-baseten

Integration package connecting Baseten and LangChain

`pip install langchain-baseten` · installs (wheel) · licence: MIT License · rank 12498 · last release 2026-10-07 · [PyPI](https://pypi.org/project/langchain-baseten/) · [docs](https://github.com/basetenlabs/langchain-baseten/tree/main/libs/baseten) · [source](https://github.com/basetenlabs/langchain-baseten)

<details><summary>README extract</summary>

This package contains the LangChain integration with Baseten.

Example:
```python
from langchain_baseten import ChatBaseten

# Option 1: Use Model APIs with model slug
model = ChatBaseten(
    model="zai-org/GLM-5.2",  # Choose from available model slugs:
    api_key="your-api-key",  # Or set BASETEN_API_KEY env var
)

# Option 2: Use dedicated deployments with model url
model = ChatBaseten(
    model_url="
...
```

Sections: langchain-baseten, Chat Models, Embeddings, Configuration, Deployment Options

</details>

### chalk-remote-call-python

Chalk remote call Python runtime interface client

`pip install chalk-remote-call-python` · installs (wheel) · licence: not stated · rank 12508 · last release 2026-10-30 · [PyPI](https://pypi.org/project/chalk-remote-call-python/) · [docs](https://docs.chalk.ai)

<details><summary>README extract</summary>

A Python runtime interface for Chalk's RemoteCallService. This package provides a gRPC server backed by a Rust implementation (tonic + PyO3) that lets you define a `handler(event, context)` function to process incoming Arrow-serialized requests. ...

Example:
```python
from chalk_remote_call import serve

def handler(event, context):
    return list(event.values())[0]

serve(handler=handler, port=8080)
```

Sections: chalk-remote-call-python, Requirements, Usage, 1. Write a handler, 2. Start the server, CLI options, Environment variables, Reserved columns, 3. Docker image, Programmatic usage, Invocation context, Architecture, Setup, Running tests

</details>

### reme-ai

Remember Me, Refine Me.

`pip install reme-ai` · installs (wheel) · licence: Apache-2.0 · rank 12514 · last release 2026-11-05 · [PyPI](https://pypi.org/project/reme-ai/) · [docs](https://reme.agentscope.io) · [source](https://github.com/agentscope-ai/ReMe)

<details><summary>README extract</summary>

A local-first, self-evolving personal knowledge base for AI agents.

> Previous versions: 0.3.x ·
> 0.2.x ·
> MemoryScope

🧠 ReMe turns conversations and resources into readable, editable, searchable, and interconnected Markdown memory. ...

Sections: ✨ Why ReMe?, 📰 Latest Updates, 🚀 Quick Start, Docker, Environment Variables, Start the Service, 5-Minute Memory Demo, ReMe Studio (Optional), 🤝 Use ReMe with Your Agent, 🧠 How ReMe Works, Workspace Layout, Memory Lifecycle, 📊 Benchmarks, 🧩 Extensions and Plugins

</details>

### copulas

Create tabular synthetic data using copulas-based modeling.

`pip install copulas` · installs (wheel) · licence: BUSL-1.1 · rank 12558 · last release 2026-10-30 · [PyPI](https://pypi.org/project/copulas/) · [source](https://github.com/sdv-dev/Copulas/)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
Copulas is a Python library for modeling multivariate distributions and sampling from them
using copula functions.
Given a table of numerical data, use Copulas to learn the distribution and
generate new synthetic data following the same statistical ...

Example:
```python
from copulas.datasets import sample_trivariate_xyz

real_data = sample_trivariate_xyz()
real_data.head()
```

Sections: Overview, Usage, Tutorials

</details>

### azureml-automl-core

Contains the non-ML non-Azure specific common code associated with running AutoML.

`pip install azureml-automl-core` · installs (wheel) · licence: Other/Proprietary License · rank 12568 · last release 2026-05-14 · [PyPI](https://pypi.org/project/azureml-automl-core/)

<details><summary>README extract</summary>

The azureml-automl-core package is a package containing functionality used by the azureml-train-automl package. It is not designed for end-user consumption and is meant only for use as part of the Azure Machine Learning SDK.

</details>

### docling-rs

Fast, local document-to-Markdown for LLMs and RAG: docling in Rust, with docling's, MarkItDown's, Marker's and MinerU's Python APIs. PDF (layout, tables, OCR), DOCX, PPTX, XLSX, HTML, EPUB, email and more.

`pip install docling-rs` · installs (wheel) · licence: MIT License · rank 12598 · last release 2026-11-06 · [PyPI](https://pypi.org/project/docling-rs/) · [docs](https://github.com/docling-project/docling.rs/blob/master/crates/docling-py/README.md) · [source](https://github.com/docling-project/docling.rs)

<details><summary>README extract</summary>

A strangler-fig drop-in for Python docling's common conversion path,
backed by the Rust docling.rs engine:
same call shape, no torch, ~4× faster PDF conversion at a fraction of the
memory (see `docs/PDF_CONFORMANCE.md`).

Coming from MarkItDown? The same
package speaks its API — change the import, keep the code: ...

Example:
```python
# was:  from docling.document_converter import DocumentConverter
from docling_rs import DocumentConverter

result = DocumentConverter().convert("document.pdf")
print(result.document.export_to_markdown())
data = result.document.export_to_dict()     # docling-core JSON wire format (schema 1.10.0)
```

...

</details>

### resize-right

Resize Right

`pip install resize-right` · installs (wheel) · licence: MIT License · rank 12622 · last release 2022-05-05 · [PyPI](https://pypi.org/project/resize-right/)

### azureml-train-automl-client

Used for automatically finding the best machine learning model and its parameters.

`pip install azureml-train-automl-client` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 12635 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-train-automl-client/)

<details><summary>README extract</summary>

The azureml-train-automl-client package contains functionality for automatically finding the best machine learning model and its parameters, given training and test data.

</details>

### navec

Compact high quality word embeddings for russian language

`pip install navec` · installs (wheel) · licence: MIT License · rank 12678 · last release 2020-10-29 · [PyPI](https://pypi.org/project/navec/)

<details><summary>README extract</summary>

Navec is a library of pretrained word embeddings for russian language. It shows competitive or better results than RusVectores, loads ~10 times faster (~1 sec), takes ~10 times less space (~50 MB). See natasha.github.io article for more info.

> Navec = large russian text datasets + vanila GloVe + quantization

How to read model filename: ...

Example:
```python
>>> from navec import Navec

>>> path = 'hudlit_12B_500K_300d_100q.tar'
>>> navec = Navec.load(path)
```

Sections: Downloads, Usage, Evaluation

</details>

### torch-checkpointing

A high-performance, distributed-training-ready checkpointing library for PyTorch models

`pip install torch-checkpointing` · installs (wheel) · licence: BSD License · rank 12717 · last release 2026-10-23 · [PyPI](https://pypi.org/project/torch-checkpointing/) · [source](https://github.com/meta-pytorch/torch_checkpointing)

<details><summary>README extract</summary>

High-performance asynchronous checkpointing for PyTorch. It takes checkpoint saving off your training loop's critical path:

- Zero-overhead saves — `save()` returns immediately; model state is staged off the training device and written by a background process while your training step keeps running. ...

Features:
- Non-blocking async saves overlapped with training (host-side staging + a background-process write).
- One high-level `CheckpointManager` for both save and load, with auto-detected rank, storage, and metadata. ...

Sections: `torch_checkpointing`, Key features, Documentation

</details>

### torchrl

A modular, primitive-first, python-first PyTorch library for Reinforcement Learning

`pip install torchrl` · installs (wheel) · licence: not stated · rank 12726 · last release 2026-10-10 · [PyPI](https://pypi.org/project/torchrl/) · [docs](https://pytorch.org/rl) · [source](https://github.com/pytorch/rl)

<details><summary>README extract</summary>

TorchRL is a PyTorch-native toolkit for reinforcement learning, decision making,
robotics, and simulation. It is not a single algorithm implementation or a
narrow benchmark suite: it is a collection of composable pieces for building RL
systems while keeping the code close to the PyTorch programming model. ...

Example:
```python
import torch
from tensordict.nn import TensorDictModule
from torch import nn

from torchrl.envs import PendulumEnv, StepCounter, TransformedEnv

# A PyTorch-native environment with an ordinary transform stack.
env = TransformedEnv(PendulumEnv(), StepCounter(max_steps=200))

# Policies are regular nn.Modules wrapped with explicit TensorDict keys.
...
```

...

</details>

### slovnet

Deep-learning based NLP modeling for Russian language

`pip install slovnet` · installs (wheel) · licence: MIT License · rank 12749 · last release 2023-01-23 · [PyPI](https://pypi.org/project/slovnet/)

<details><summary>README extract</summary>

SlovNet is a Python library for deep-learning based NLP modeling for Russian language. Library is integrated with other Natasha projects: Nerus — large automatically annotated corpus, Razdel — sentence segmenter, tokenizer and Navec — compact Russian embeddings. ...

Example:
```python
>>> from navec import Navec
>>> from slovnet import NER
>>> from ipymarkup import show_span_ascii_markup as show_markup

...
```

Sections: Downloads, Usage, NER, Morphology, Syntax, Documentation, Evaluation

</details>

### minizinc

Access MiniZinc directly from Python

`pip install minizinc` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12845 · last release 2025-02-25 · [PyPI](https://pypi.org/project/minizinc/) · [docs](https://python.minizinc.dev/) · [source](https://github.com/MiniZinc/minizinc-python.git)

<details><summary>README extract</summary>

The python package that allows you to access all of MiniZinc's functionalities directly from Python.

 Explore the docs »

 Report Bug
 Request Feature

Example:
```python
import minizinc

# Create a MiniZinc model
model = minizinc.Model()
model.add_string("""
var -100..100: x;
int: a; int: b; int: c;
constraint a*(x*x) + b*x = c;
solve satisfy;
""")

# Transform Model into a instance
gecode = minizinc.Solver.lookup("gecode")
inst = minizinc.Instance(gecode, model)
inst["a"] = 1
inst["b"] = 4
inst["c"] = 0

...
```

Sections: MiniZinc Python, About The Project, Getting Started, Usage, Roadmap, Contact

</details>

### diffq-fixed

Differentiable quantization framework for PyTorch -- fixed for compatibility with Python 3.11+

`pip install diffq-fixed` · installs from source (sdist only) · licence: Creative Commons Attribution-NonCommercial 4.0 International · rank 12880 · last release 2025-03-03 · [PyPI](https://pypi.org/project/diffq-fixed/)

<details><summary>README extract</summary>

DiffQ performs differentiable quantization using pseudo quantization noise.
It can automatically tune the number of bits used per weight or group of weights,
in order to achieve a given trade-off between model size and accuracy.

Go read our paper for more details.

See the changelog for details on releases. ...

Example:
```python
import torch
from torch.nn import functional as F
import diffq
from diffq import DiffQuantizer

model = MyModel()
optim = ...  # The optimizer must be created before the quantizer
quantizer = DiffQuantizer(model)
quantizer.setup_optimizer(optim)

# Distributed data parallel must be created after DiffQuantizer!
...
```

...

</details>

### neptune-scale

A minimal client library

`pip install neptune-scale` · installs (wheel) · licence: Apache Software License · rank 12882 · last release 2025-11-26 · [PyPI](https://pypi.org/project/neptune-scale/) · [docs](https://docs.neptune.ai/) · [source](https://github.com/neptune-ai/neptune-client-scale)

<details><summary>README extract</summary>

Quickstart
 Website
 Docs
 Examples
 Blog

Neptune is an experiment tracker purpose-built for foundation model training.

With Neptune, you can monitor thousands of per-layer metrics—losses, gradients, and activations—at any scale. Visualize them with no lag and no missed spikes. Drill down into logs and debug training issues fast. ...

Example:
```python
from neptune_scale import Run

run = Run(experiment_name="MyExperimentName")
```

Sections: neptune.ai, Get started, Example usage, Getting help, People behind Neptune

</details>

### brax

A differentiable physics engine written in JAX.

`pip install brax` · installs (wheel) · licence: Apache Software License · rank 12926 · last release 2026-03-15 · [PyPI](https://pypi.org/project/brax/)

<details><summary>README extract</summary>

> WARNING
> Only `brax/training` is actively being maintained as of 0.13.0. Instead of `brax/envs`, users should use MuJoCo Playground, all of which train well with `brax/training`. ...

Sections: One API, Four Pipelines, Quickstart: Colab in the Cloud, Using Brax Locally, Learn More, Citing Brax

</details>

### langchain-openviking

OpenViking integrations for LangChain and LangGraph

`pip install langchain-openviking` · installs (wheel) · licence: AGPL-3.0 · rank 12963 · last release 2026-11-06 · [PyPI](https://pypi.org/project/langchain-openviking/) · [docs](https://openviking.ai) · [source](https://github.com/volcengine/openviking)

_README extract left out: share-alike licence._

### datatrove

HuggingFace library to process and filter large amounts of webdata

`pip install datatrove` · installs (wheel) · licence: Apache Software License · rank 13008 · last release 2026-09-30 · [PyPI](https://pypi.org/project/datatrove/) · [source](https://github.com/huggingface/datatrove)

<details><summary>README extract</summary>

DataTrove is a library to process, filter and deduplicate text data at a very large scale. It provides a set of prebuilt commonly used processing blocks with a framework to easily add custom functionality.

DataTrove processing pipelines are platform-agnostic, running out of the box locally or on a slurm cluster. ...

Example:
```python
from datatrove.pipeline.readers import CSVReader
from datatrove.pipeline.filters import SamplerFilter
from datatrove.pipeline.writers import JsonlWriter

pipeline = [
    CSVReader(
        data_folder="/my/input/path"
    ),
    SamplerFilter(rate=0.5),
    JsonlWriter(
        output_folder="/my/output/path"
    )
]
```

...

</details>

### ovphysx

PhysX simulation library for ovstage-populated scenes with Warp array interoperability. x86_64 wheels require a CPU with AVX.

`pip install ovphysx` · installs (wheel) · licence: LicenseRef-NVIDIA-Omniverse · rank 13022 · last release 2026-10-15 · [PyPI](https://pypi.org/project/ovphysx/) · [docs](https://nvidia-omniverse.github.io/PhysX/ovphysx/latest/index.html) · [source](https://github.com/NVIDIA-Omniverse/PhysX)

<details><summary>README extract</summary>

<!-- SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

ovphysx is a self-contained Python library for ovstage/USD-based physics simulation
with Warp-array output and downstream DLPack interoperability. It wraps NVIDIA
PhysX and provides: ...

Example:
```python
from pathlib import Path

import ovphysx
from ovphysx.samples.python_samples.schema_support import physx_schema_paths
import ovstage
from ovphysx import PhysX

usd_path = (
    Path(ovphysx.file).resolve().parent
    / "samples"
    / "data"
    / "simple_physics_scene.usda"
)
if not usd_path.is_file():
...
```

Sections: ovphysx, Quick start

</details>

### CoLT5-attention

Conditionally Routed Attention

`pip install CoLT5-attention` · installs (wheel) · licence: MIT License · rank 13076 · last release 2026-08-14 · [PyPI](https://pypi.org/project/CoLT5-attention/) · [source](https://github.com/lucidrains/CoLT5-attention)

<details><summary>README extract</summary>

Implementation of the conditionally routed efficient attention in the proposed CoLT5 architecture, in Pytorch.

They used coordinate descent from this paper (main algorithm originally from Wright et al) to route a subset of tokens for 'heavier' branches of the feedforward and attention blocks. ...

Example:
```python
import torch

from colt5_attention import (
    ConditionalRoutedFeedForward,
    ConditionalRoutedAttention,
    ConditionalRoutedTransformerBlock
)

# mock input, say it is 32768 length

tokens = torch.randn(2, 32768, 512)
mask = torch.ones(2, 32768).bool()  # can handle variable lengthed sequences

# feedforward

...
```

Sections: CoLT5 Attention - Pytorch, Appreciation, Usage, Differentiable Topk, Todo

</details>

### ipymarkup

NER, syntax tree markup visualisations for Jupyter Notebook

`pip install ipymarkup` · installs (wheel) · licence: MIT License · rank 13077 · last release 2020-05-26 · [PyPI](https://pypi.org/project/ipymarkup/)

<details><summary>README extract</summary>

Collection of NLP visualizations for NER and syntax tree markup. Similar to Spacy displaCy and displaCy ENT.

Example:
```python
>>> from ipymarkup import show_ner_ascii_markup, show_dep_ascii_markup

...
```

</details>

### cua-bench

Run computer-use benchmark datasets on local and cloud sandboxes

`pip install cua-bench` · does not install on CPython 3.14 · licence: MIT · rank 13089 · last release 2026-10-19 · [PyPI](https://pypi.org/project/cua-bench/) · [docs](https://docs.trycua.com) · [source](https://github.com/trycua/cua)

<details><summary>README extract</summary>

Run computer-use benchmark datasets on local sandboxes.

Cua Cloud has ended; `--on cloud` now fails with a pointer to the notice.

Documentation - Installation, guides, and API reference.

Browse the tasksets at cua.ai/cuabench/registry and run
one by name on a desktop sandbox: ...

Example:
```python
cb.Task(
    description="...",
    computer={
        "provider": "native",  # a real sandbox (the only provider since 0.3)
        "setup_config": {
            "os_type": "linux",  # linux | windows | macos (local only) | android (local only)
            "image": "ghcr.io/me/my-desktop:docker-1",  # optional
...
```

Sections: cua-bench, Registry tasksets, Running tasks, Datasets, Images, Tasks, A coding-agent harness as the agent, Upgrading from 0.2, Running Tests

</details>

### natasha

Named-entity recognition for russian language

`pip install natasha` · installs (wheel) · licence: MIT License · rank 13099 · last release 2023-07-24 · [PyPI](https://pypi.org/project/natasha/)

<details><summary>README extract</summary>

Natasha solves basic NLP tasks for Russian language: tokenization, sentence segmentation, word embedding, morphology tagging, lemmatization, phrase normalization, syntax parsing, NER tagging, fact extraction. Quality on every task is similar or better then current SOTAs for Russian language on news articles, see evaluation section. ...

Example:
```python
>>> from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,

    Doc
)

>>> segmenter = Segmenter()
>>> morph_vocab = MorphVocab()

>>> emb = NewsEmbedding()
>>> morph_tagger = NewsMorphTagger(emb)
>>> syntax_parser = NewsSyntaxParser(emb)
...
```

...

</details>

### polyglot

Polyglot is a natural language pipeline that supports massive multilingual applications.

`pip install polyglot` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 13128 · last release 2016-07-03 · [PyPI](https://pypi.org/project/polyglot/)

_README extract left out: share-alike licence._

### tflite

Parsing TensorFlow Lite Models (*.tflite) Easily

`pip install tflite` · installs (wheel) · licence: Apache Software License · rank 13138 · last release 2025-01-28 · [PyPI](https://pypi.org/project/tflite/) · [source](https://github.com/zhenhuaw-me/tflite)

<details><summary>README extract</summary>

This `tflite` package parses TensorFlow Lite (TFLite) models (`*.tflite`), which are built by TFLite converter. For background, please refer to Introducing TFLite Parser Python Package.

Sections: Easily Parse TFLite Models with Python, Usage, Enhancements, Compatibility Handling, Resources, Disclaimer

</details>

### pytextrank

Python implementation of TextRank as a spaCy pipeline extension, for graph-based natural language work plus related knowledge graph practices; used for for phrase extraction of text documents.

`pip install pytextrank` · installs (wheel) · licence: MIT License · rank 13144 · last release 2024-02-21 · [PyPI](https://pypi.org/project/pytextrank/) · [source](http://github.com/DerwenAI/pytextrank)

<details><summary>README extract</summary>

PyTextRank is a Python implementation of *TextRank* as a
spaCy pipeline extension,
for graph-based natural language work -- and related knowledge graph practices.
This includes the family of ...

Example:
```python
import spacy
import pytextrank

# example text
...
```

Sections: PyTextRank, Getting Started, Attribution, Kudos

</details>

### nemo-evaluator

NeMo Evaluator — benchmark environments, pluggable solvers, interceptor proxy, and decision-grade scoring for LLMs

`pip install nemo-evaluator` · does not install on CPython 3.14 · licence: Apache Software License · rank 13276 · last release 2026-06-03 · [PyPI](https://pypi.org/project/nemo-evaluator/) · [docs](https://docs.nvidia.com/nemo/evaluator/) · [source](https://github.com/NVIDIA-NeMo/Evaluator)

<details><summary>README extract</summary>

Documentation | GitHub | Issues

LLM evaluation framework with benchmark environments, pluggable solvers, composable interceptor proxy, and multi-format reporting.

Example:
```python
from nemo_evaluator import benchmark, scorer, ScorerInput, exact_match

@benchmark(name="my-bench", dataset="hf://my-org/data?split=test",
           prompt="Q: {question}\nA:", target_field="answer")
@scorer
def my_scorer(sample: ScorerInput) -> dict:
    return exact_match(sample)
```

Sections: NeMo Evaluator, Quick Start, Benchmarks, Adapter Proxy, Solvers, Export, BYOB (Bring Your Own Benchmark), Sandboxes, SLURM, CLI, Compare Results Between Runs, Implement Quality Gates, Examples

</details>

### axial-positional-embedding

Axial Positional Embedding

`pip install axial-positional-embedding` · installs (wheel) · licence: MIT License · rank 13279 · last release 2025-02-25 · [PyPI](https://pypi.org/project/axial-positional-embedding/) · [source](https://github.com/lucidrains/axial_positional_embedding)

<details><summary>README extract</summary>

A type of positional embedding that is very effective when working with attention networks on multi-dimensional data, or for language models in general.

Example:
```python
import torch
from axial_positional_embedding import AxialPositionalEmbedding

pos_emb = AxialPositionalEmbedding(
    dim = 512,
    axial_shape = (64, 64),          # axial shape will multiply up to the maximum sequence length allowed (64 * 64 = 4096)
...
```

Sections: Axial Positional Embedding, Usage

</details>

### product-key-memory

Product Key Memory

`pip install product-key-memory` · installs (wheel) · licence: MIT License · rank 13396 · last release 2025-11-01 · [PyPI](https://pypi.org/project/product-key-memory/) · [source](https://github.com/lucidrains/product-key-memory)

<details><summary>README extract</summary>

Standalone Product Key Memory module for augmenting Transformer models

Example:
```python
import torch
from product_key_memory import PKM

pkm = PKM(
    dim = 512,
    heads = 4,
    dim_head = 128,       # keep at 128 for best results
    num_keys = 256,       # number of subkeys, # values will be num_keys ^ 2
    topk = 32             # the top number of subkeys to select
)

x = torch.randn(1, 1024, 512)
...
```

Sections: Product Key Memory, Usage, Learning Rates, Appreciation, Todo

</details>

### pyversity

Fast Diversification for Search & Retrieval

`pip install pyversity` · installs (wheel) · licence: MIT License · rank 13475 · last release 2026-02-02 · [PyPI](https://pypi.org/project/pyversity/) · [source](https://github.com/Pringled/pyversity)

<details><summary>README extract</summary>

Fast Diversification for Search & Retrieval

Quickstart •
Supported Strategies •
Benchmarks •
Motivation •
Examples •
References

Pyversity is a fast, lightweight library for diversifying retrieval results.
Retrieval systems often return highly similar items. ...

Example:
```python
import numpy as np
from pyversity import diversify, Strategy

# Define embeddings and scores (e.g. cosine similarities of a query result)
embeddings = np.random.randn(100, 256)
scores = np.random.rand(100)

# Diversify the result
diversified_result = diversify(
    embeddings=embeddings,
    scores=scores,
    k=10, # Number of items to select
...
```

Sections: Quickstart, Benchmarks, Motivation, Examples, References

</details>

### hugpy-core

Hugpy Core: a small fleet API, worker console, dispatch and consolidated history.

`pip install hugpy-core` · installs (wheel) · licence: Proprietary · rank 13481 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hugpy-core/)

<details><summary>README extract</summary>

Core is the Flask console, API and fleet coordinator. It registers Wrapper hosts,
mirrors their inventory and execution evidence into PostgreSQL, and routes work.
Wrapper owns execution, loading, memory admission, worker settings and local model
copies. Core uses Wrapper's reported feasibility; it does not run a second sizing
solver. ...

Sections: Hugpy Core, API, UI and operations, Downloads and feature gallery

</details>

### infinity-parser2

Document parsing Python package supporting PDF and image parsing using Infinity-Parser2-Pro model.

`pip install infinity-parser2` · installs (wheel) · licence: Apache Software License · rank 13534 · last release 2026-08-27 · [PyPI](https://pypi.org/project/infinity-parser2/)

<details><summary>README extract</summary>

🤗 Infinity-Parser2-Pro |
🤗 Infinity-Parser2-Flash |
📊 Dataset |
📄 Paper |
🚀 Demo

- [2026-05-11] Released flagship document parsing models: Infinity-Parser2-Pro, Infinity-Parser2-Flash, and the dataset Infinity-Doc2-5M. Infinity-Parser2 achieves SOTA results on olmOCR-bench and ParseBench. ...

Features:
- Upgraded Data Engine: We have comprehensively enhanced our synthetic data engine to support both fixed-layout and flexible-layout document formats. ...

Example:
```python
from PIL import Image
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info

# Load the model and processor
model = AutoModelForImageTextToText.from_pretrained(
    "infly/Infinity-Parser2-Pro",
    torch_dtype="float16",
    device_map="auto",
)
...

</details>

### mtcnn

Multitask Cascaded Convolutional Networks for face detection and alignment (MTCNN) in Python >= 3.10 and TensorFlow >= 2.12

`pip install mtcnn` · installs (wheel) · licence: MIT License · rank 13536 · last release 2024-10-08 · [PyPI](https://pypi.org/project/mtcnn/) · [docs](https://github.com/ipazc/mtcnn/docs) · [source](https://github.com/ipazc/mtcnn)

<details><summary>README extract</summary>

Features:
MTCNN is a robust face detection and alignment library implemented for Python >= 3.10 and TensorFlow >= 2.12, designed to detect faces and their landmarks using a multitask cascaded convolutional network. ...

Example:
```python
from mtcnn import MTCNN
from mtcnn.utils.images import load_image

# Create a detector instance
detector = MTCNN(device="CPU:0")

# Load an image
image = load_image("ivan.jpg")

# Detect faces in the image
result = detector.detect_faces(image)

# Display the result
print(result)
```

Sections: Overview, Usage Example, Models Overview, Documentation, About this project

</details>

### mistralai-agents

Mistral Agents SDK - build and serve agents in Python

`pip install mistralai-agents` · installs (wheel) · licence: Apache Software License · rank 13582 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mistralai-agents/)

<details><summary>README extract</summary>

Build an agent in Python. Try it on your laptop, then run the same code in production with one command.

An agent is a model and its instructions, plus the tools, sandboxes, connectors, skills and subagents it can use. The same agent runs in your process, on your own server with `agents serve`, or on Mistral with `agents deploy`.

Example:
```python
import asyncio

from mistralai import agents

agent = agents.Agent(model="mistral-large-4")

async def main() -> None:
    result = await agent.run("Say hello")
    print(result.text)

asyncio.run(main())
```

Sections: Mistral Managed Agents, Hello world, Create a project, Learn more, Feedback

</details>

### mooncake-transfer-engine

A KVCache-centric Disaggregated Architecture for large-scale LLM inference and training.

`pip install mooncake-transfer-engine` · installs (wheel) · licence: Apache Software License · rank 13592 · last release 2026-11-03 · [PyPI](https://pypi.org/project/mooncake-transfer-engine/) · [docs](https://kvcache-ai.github.io/Mooncake) · [source](https://github.com/kvcache-ai/Mooncake)

<details><summary>README extract</summary>

Paper
 | Slides
 | Traces
 | Documentation
 | Blog
 | Slack

Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI.
Under real workloads, Mooncake’s innovative architecture enables Kimi to handle 75% more requests while adhering to SLOs. ...

Sections: 🔄 Updates, 🎉 Overview, 🔥 Show Cases, Transfer Engine (TE), Mooncake Store, Mooncake EP and Process Group (PG), Tensor-Centric Ecosystem, SGLang Integration (Guide), vLLM Integration (Guide), 🌐 Ecosystem Integrations, 🚀 Getting Started, Skills for AI Assistants, 📦 Open Source Traces and Tools

</details>

### torchmonarch

Monarch: Single controller library

`pip install torchmonarch` · does not install on CPython 3.14 · licence: BSD-3-Clause · rank 13607 · last release 2026-10-10 · [PyPI](https://pypi.org/project/torchmonarch/) · [docs](https://meta-pytorch.org/monarch/) · [source](https://github.com/meta-pytorch/monarch)

<details><summary>README extract</summary>

Monarch is a distributed programming framework for PyTorch based on scalable
actor messaging. It provides:

1. Remote actors with scalable messaging: Actors are grouped into collections
 called meshes and messages can be broadcast to all members.
2. ...

Example:
```python
from monarch.actor import Actor, endpoint, this_host

# spawn 8 trainer processes one for each gpu
training_procs = this_host().spawn_procs({"gpus": 8})

# define the actor to run on each process
class Trainer(Actor):
    @endpoint
    def train(self, step: int): ...

# create the trainers
trainers = training_procs.spawn("trainers", Trainer)

...
```

...

</details>

### keyphrase-vectorizers

Set of vectorizers that extract keyphrases with part-of-speech patterns from a collection of text documents and convert them into a document-keyphrase matrix.

`pip install keyphrase-vectorizers` · installs (wheel) · licence: BSD License · rank 13673 · last release 2024-05-02 · [PyPI](https://pypi.org/project/keyphrase-vectorizers/)

<details><summary>README extract</summary>

This package was developed during the writing of our PatternRank paper. You can check out the paper here. When using KeyphraseVectorizers or PatternRank in academic papers and theses, please use the BibTeX entry below. ...

Example:
```python
from typing import List
import flair
from flair.models import SequenceTagger
from flair.tokenization import SegtokSentenceSplitter

docs = ["""Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
...
```

...

</details>

### onnx2tf

A tool for converting ONNX files to LiteRT/TFLite/TensorFlow, PyTorch native code (nn.Module), TorchScript (.pt), state_dict (.pt), Exported Program (.pt2), and Dynamo ONNX. It also supports direct conversion from LiteRT to PyTorch.

`pip install onnx2tf` · installs (wheel) · licence: MIT · rank 13692 · last release 2026-09-14 · [PyPI](https://pypi.org/project/onnx2tf/) · [docs](https://github.com/PINTO0309/onnx2tf#readme) · [source](https://github.com/PINTO0309/onnx2tf)

<details><summary>README extract</summary>

A tool for converting ONNX files to LiteRT/TFLite/TensorFlow, PyTorch native code (nn.Module), TorchScript (.pt), state_dict (.pt), Exported Program (.pt2), and Dynamo ONNX. It also supports direct conversion from LiteRT to PyTorch.

You should use LiteRT Torch rather than onnx2tf. and

Example:
```python
import sys

import torch

sys.path.append("tmp_yolox_s")
from yolox_s_pytorch import load_model

model = load_model(device="cpu", eval_mode=True)
x = torch.zeros((1, 3, 640, 640), dtype=torch.float32)

with torch.no_grad():
    output = model(x)

print("input :", tuple(x.shape))
print("output:", tuple(output.shape))
...
```

...

</details>

### ctgan

Create tabular synthetic data using a conditional GAN

`pip install ctgan` · installs (wheel) · licence: BUSL-1.1 · rank 13719 · last release 2026-10-30 · [PyPI](https://pypi.org/project/ctgan/) · [source](https://github.com/sdv-dev/CTGAN/)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
CTGAN is a collection of Deep Learning based synthetic data generators for single table data, which are able to learn from real data and generate synthetic data with high fidelity.

| Important Links | | ...

Example:
```python
from ctgan import CTGAN
from ctgan import load_demo

real_data = load_demo()

# Names of the columns that are discrete
discrete_columns = [
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native-country',
    'income',
]

ctgan = CTGAN(epochs=10)
...
```

Sections: Overview, Use CTGAN through the SDV library, Use the CTGAN standalone library, Usage Example, Citing CTGAN, Related Projects

</details>

### rlax

A library of reinforcement learning building blocks in JAX.

`pip install rlax` · installs (wheel) · licence: Apache Software License · rank 13790 · last release 2026-06-12 · [PyPI](https://pypi.org/project/rlax/) · [source](https://github.com/google-deepmind/rlax)

<details><summary>README extract</summary>

RLax (pronounced "relax") is a library built on top of JAX that exposes
useful building blocks for implementing reinforcement learning agents. Full
documentation can be found at
 rlax.readthedocs.io.

Sections: RLax, Content, Usage, Background, Reinforcement Learning Algorithms, Citing RLax

</details>

### torchrl-nightly

A modular, primitive-first, python-first PyTorch library for Reinforcement Learning

`pip install torchrl-nightly` · installs (wheel) · licence: not stated · rank 13905 · last release 2026-11-08 · [PyPI](https://pypi.org/project/torchrl-nightly/) · [docs](https://pytorch.org/rl) · [source](https://github.com/pytorch/rl)

<details><summary>README extract</summary>

TorchRL is a PyTorch-native toolkit for reinforcement learning, decision making,
robotics, and simulation. It is not a single algorithm implementation or a
narrow benchmark suite: it is a collection of composable pieces for building RL
systems while keeping the code close to the PyTorch programming model. ...

Example:
```python
import torch
from tensordict.nn import TensorDictModule
from torch import nn

from torchrl.envs import PendulumEnv, StepCounter, TransformedEnv

# A PyTorch-native environment with an ordinary transform stack.
env = TransformedEnv(PendulumEnv(), StepCounter(max_steps=200))

# Policies are regular nn.Modules wrapped with explicit TensorDict keys.
...
```

...

</details>

### galileo-core

(no summary)

`pip install galileo-core` · installs (wheel) · licence: Apache Software License · rank 13964 · last release 2026-11-02 · [PyPI](https://pypi.org/project/galileo-core/)

<details><summary>README extract</summary>

Shared schemas and configuration for Galileo's Python packages.

This package is now maintained inside the Orbit monorepo at `libs/python/core/`.

Example:
```python
import galileo_core
```

Sections: galileo-core (in Orbit), Package Layout, Running Tests, Building Distribution Artifacts, Custom HTTP Headers (API gateways / IBM APIC), Import Path, Publishing

</details>

### tensorfs

Load, store and share model weights: a self-describing tensor format, a deduplicating local store and the tfs CLI

`pip install tensorfs` · installs (wheel) · licence: MIT · rank 13975 · last release 2026-11-06 · [PyPI](https://pypi.org/project/tensorfs/) · [docs](https://github.com/cozy-creator/cozy-creator/blob/master/crates/tensorfs-py/API.md) · [source](https://github.com/cozy-creator/cozy-creator)

<details><summary>README extract</summary>

TensorFS is a Rust library with Python bindings and the `tfs` command-line tool for
loading, storing and sharing model weights.

The TensorFS overview,
Python guide
and format specification
cover the shared library and format. Python-specific documentation lives alongside these bindings.

</details>

### langchain-docling

Docling LangChain integration

`pip install langchain-docling` · installs (wheel) · licence: MIT · rank 14082 · last release 2026-08-14 · [PyPI](https://pypi.org/project/langchain-docling/) · [source](https://github.com/docling-project/docling-langchain)

<details><summary>README extract</summary>

A Docling integration for
LangChain.

Example:
```python
from langchain_docling import DoclingLoader

FILE_PATH = ["  # Docling Technical Report

loader = DoclingLoader(file_path=FILE_PATH)
docs = loader.load()
```

Sections: Docling LangChain integration, Usage, Basic usage, Docling Serve or Managed Docling, Advanced usage, Docs and examples

</details>

### sam3

SAM3 (Segment Anything Model 3) implementation

`pip install sam3` · installs (wheel) · licence: MIT License · rank 14096 · last release 2026-05-26 · [PyPI](https://pypi.org/project/sam3/)

<details><summary>README extract</summary>

Meta Superintelligence Labs

Nicolas Carion\*,
Laura Gustafson\*,
Yuan-Ting Hu\*,
Shoubhik Debnath\*,
Ronghang Hu\*,
Didac Suris\*,
Chaitanya Ryali\*,
Kalyan Vasudev Alwala\*,
Haitham Khedr\*, Andrew Huang,
Jie Lei,
Tengyu Ma,
Baishan Guo,
Arpit Kalla, Markus Marks,
Joseph Greer,
Meng Wang, Peize Sun,
Roman Rädle,
Triantafyllos Afouras,
Effrosyni ...

Example:
```python
import torch
# ############################## For Image
from PIL import Image
from sam3.model_builder import build_sam3_image_model
from sam3.model.sam3_image_processor import Sam3Processor
# Load the model
model = build_sam3_image_model()
processor = Sam3Processor(model)
# Load an image
image = Image.open("")
...
```

...

</details>

### cpex

CPEX - ContextForge Plugin Extensibility Framework

`pip install cpex` · installs (wheel) · licence: Apache-2.0 · rank 14121 · last release 2026-09-18 · [PyPI](https://pypi.org/project/cpex/) · [source](https://github.com/contextforge-org/cpex)

<details><summary>README extract</summary>

A composable enforcement framework for AI agents and toolchains.

> Read the project vision to learn why hooks, plugins, and policy are the path to agent security.

CPEX lets you intercept, enforce, and extend application behavior through plugins without modifying core logic. ...

Features:
AI agents execute across trust domains, calling tools, accessing data, and delegating to other agents. Adding security, governance, or policy enforcement typically means embedding that logic directly into application code, leading to duplication, ...

Example:
```python
from cpex.framework import hook, Plugin, PluginResult

class RateLimitPlugin(Plugin):
    @hook("tool_pre_invoke")
    async def check_rate_limit(self, payload, context):
        if self.is_over_limit(context):
...

</details>

### molbloom

Purchaseable SMILES filter

`pip install molbloom` · installs from source (sdist only) · licence: MIT License · rank 14165 · last release 2026-03-23 · [PyPI](https://pypi.org/project/molbloom/)

<details><summary>README extract</summary>

Can I buy this molecule? Returns results in about 500 ns and consumes about 100MB of RAM (or 2 GB if using all ZINC20).

If `buy` returns `True` - it may be purchasable with a measured error rate of 0.0003. If it returns `False` - it is not purchasable.
The catalog information is from ZINC20. ...

Example:
```python
from molbloom import buy
buy('CCCO')
# True
buy('ONN1CCCC1')
# False
```

Sections: molbloom, Simple Reagents, Querying Small World, Custom Filter, Build with C Tool, Build with Python

</details>

### docling-ocr-onnxtr

Onnx Text Recognition (OnnxTR) OCR plugin for docling

`pip install docling-ocr-onnxtr` · installs (wheel) · licence: Apache Software License · rank 14216 · last release 2026-10-09 · [PyPI](https://pypi.org/project/docling-ocr-onnxtr/) · [source](https://github.com/felixdittrich92/docling-OCR-OnnxTR/OnnxTR)

<details><summary>README extract</summary>

The `docling-OCR-OnnxTR` repository provides a plugin that integrates the OnnxTR OCR engine into the Docling framework, enhancing document processing capabilities with efficient and accurate text recognition.

Key Features: ...

Example:
```python
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import (
    ConversionResult,
    DocumentConverter,
    InputFormat,
    PdfFormatOption,
)
from docling_ocr_onnxtr import OnnxtrOcrOptions

def main():
    # Source document to convert
    source = "

...
```

Sections: Usage, Configuration

</details>

### ogb

Open Graph Benchmark

`pip install ogb` · installs (wheel) · licence: MIT License · rank 14280 · last release 2023-04-07 · [PyPI](https://pypi.org/project/ogb/)

<details><summary>README extract</summary>

Features:
The Open Graph Benchmark (OGB) is a collection of benchmark datasets, data loaders, and evaluators for graph machine learning. Datasets cover a variety of graph machine learning tasks and real-world applications. ...

Example:
```python
from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.loader import DataLoader

# Download and process data at './dataset/ogbg_molhiv/'
dataset = PygGraphPropPredDataset(name = 'ogbg-molhiv')

split_idx = dataset.get_idx_split()
train_loader = DataLoader(dataset[split_idx['train']], batch_size=32, shuffle=True)
...
```

Sections: Overview, Requirements, From source, Package Usage, (1) Data loaders, (2) Evaluators, Citing OGB / OGB-LSC

</details>

### histomicstk

A Python toolkit for Histopathology Image Analysis

`pip install histomicstk` · installs from source (sdist only) · licence: Apache Software License · rank 14363 · last release 2025-02-07 · [PyPI](https://pypi.org/project/histomicstk/)

<details><summary>README extract</summary>

HistomicsTK is a Python package for the analysis of digital pathology images. It can function as a stand-alone library, or as a Digital Slide Archive plugin that allows users to invoke image analysis jobs through HistomicsUI. ...

Sections: HistomicsTK, Previous Versions, See Also

</details>

### mistralai-otel-observability

OTLP-first Mistral AI observability SDK

`pip install mistralai-otel-observability` · installs (wheel) · licence: Apache Software License · rank 14364 · last release 2026-11-04 · [PyPI](https://pypi.org/project/mistralai-otel-observability/) · [docs](https://docs.mistral.ai)

<details><summary>README extract</summary>

Manual, OTLP-first observability helpers for GenAI applications.

The package installs into `mistralai.observability.otel` and owns private OpenTelemetry providers for traces, metrics,
and logs. It does not install global tracer or meter providers and does not configure Python logging.

Example:
```python
from mistralai.observability.otel import ObservabilityConfig, observability
from mistralai.observability.otel import semconv_constants as genai

observability.configure(
    ObservabilityConfig(
        service_name="my-app",
        endpoint="
        protocol="http/protobuf",
    )
)

with observability.operation(
    genai.OPERATION_NAME_CHAT,
...
```

...

</details>

### envpool

"C++-based high-performance parallel environment execution engine (vectorized env) for general RL environments."

`pip install envpool` · installs (wheel) · licence: Apache Software License · rank 14371 · last release 2026-11-08 · [PyPI](https://pypi.org/project/envpool/)

<details><summary>README extract</summary>

EnvPool is a C++-based batched environment pool with pybind11 and thread pool. It has high performance (\~1M raw FPS with Atari games, \~3M raw FPS with MuJoCo simulator on DGX-A100) and compatible APIs (supports Gymnasium and dm\_env, both sync and async, both single and multi player environment). Currently it supports:

- [x] Atari games ...

Example:
```python
import envpool
print(envpool.version)
```

Sections: PyPI, From Source, Documentation, Benchmark Results, API Usage, Synchronous API, Asynchronous API, Rendering, Pixel Observations, Citing EnvPool, Disclaimer

</details>

### linear-attention-transformer

Linear Attention Transformer

`pip install linear-attention-transformer` · installs (wheel) · licence: MIT License · rank 14386 · last release 2021-09-07 · [PyPI](https://pypi.org/project/linear-attention-transformer/)

### minari

A standard format for offline reinforcement learning datasets, with popular reference datasets and related utilities.

`pip install minari` · installs (wheel) · licence: MIT License · rank 14397 · last release 2026-09-29 · [PyPI](https://pypi.org/project/minari/) · [docs](https://minari.farama.org/) · [source](https://github.com/Farama-Foundation/Minari)

<details><summary>README extract</summary>

Minari is a Python library for conducting research in offline reinforcement learning, akin to an offline version of Gymnasium or an offline RL version of HuggingFace's datasets library.

The documentation website is at minari.farama.org. ...

Example:
```python
import minari

dataset = minari.load_dataset("D4RL/door/human-v2")

for episode_data in dataset.iterate_episodes():
    observations = episode_data.observations
    actions = episode_data.actions
    rewards = episode_data.rewards
    terminations = episode_data.terminations
    truncations = episode_data.truncations
    infos = episode_data.infos
...
```

Sections: Command Line API, Basic Usage, Reading a Dataset, Writing a Dataset, Training Libraries Integrating Minari

</details>

### openvino-genai

Library of the most popular Generative AI model pipelines, optimized execution methods, and samples

`pip install openvino-genai` · installs (wheel) · licence: Apache Software License · rank 14423 · last release 2026-10-01 · [PyPI](https://pypi.org/project/openvino-genai/)

<details><summary>README extract</summary>

OpenVINO™ GenAI is a flavor of OpenVINO™, aiming to simplify running inference of generative AI models.
It hides the complexity of the generation process and minimizes the amount of code required.

Example:
```python
import openvino_genai as ov_genai
pipe = ov_genai.LLMPipeline(models_path, "CPU")
print(pipe.generate("The Sun is yellow because", max_new_tokens=100))
```

Sections: OpenVINO™ GenAI Library, OpenVINO™ GenAI Dependencies, Usage, Prerequisites, Python, C++, Performance Metrics, Structured Output generation, Tokenization, How It Works, Debug Log

</details>

### sdv

Generate synthetic data for single table, multi table and sequential data

`pip install sdv` · installs (wheel) · licence: BUSL-1.1 · rank 14438 · last release 2026-11-06 · [PyPI](https://pypi.org/project/sdv/) · [source](https://github.com/sdv-dev/SDV/)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
The Synthetic Data Vault (SDV) is a Python library designed to be your one-stop shop for
creating tabular synthetic data. The SDV uses a variety of machine learning algorithms to learn
patterns from your real data and emulate them in synthetic data.

Example:
```python
from sdv.datasets.demo import download_demo

real_data, metadata = download_demo(modality='single_table', dataset_name='fake_hotel_guests')
```

Sections: Overview, Features, Getting Started, Synthesizing Data, Evaluating Synthetic Data, What's Next?

</details>

### linformer

Linformer implementation in Pytorch

`pip install linformer` · installs (wheel) · licence: MIT License · rank 14448 · last release 2024-01-05 · [PyPI](https://pypi.org/project/linformer/)

### azureml-pipeline

Used to build, optimize, and manage their machine learning workflows.

`pip install azureml-pipeline` · installs (wheel) · licence: Other/Proprietary License · rank 14458 · last release 2026-02-25 · [PyPI](https://pypi.org/project/azureml-pipeline/)

<details><summary>README extract</summary>

Machine learning (ML) pipelines are used by data scientists to build, optimize, and manage their machine learning workflows. A typical pipeline involves a sequence of steps that cover the following areas: ...

</details>

### torchtyping

Runtime type annotations for the shape, dtype etc. of PyTorch Tensors.

`pip install torchtyping` · installs (wheel) · licence: Apache Software License · rank 14485 · last release 2024-08-01 · [PyPI](https://pypi.org/project/torchtyping/)

<details><summary>README extract</summary>

*Welcome! For new projects I now strongly recommend using my newer jaxtyping project instead. It supports PyTorch, doesn't actually depend on JAX, and unlike TorchTyping it is compatible with static type checkers. :)*

Turn this:
into this:
with programmatic checking that the shape (dtype, ...) specification is met. ...

Example:
```python
# EXAMPLE

from torch import rand
from torchtyping import TensorType, patch_typeguard
from typeguard import typechecked

patch_typeguard()  # use before @typechecked

@typechecked
def func(x: TensorType["batch"],
         y: TensorType["batch"]) -> TensorType["batch"]:
    return x + y

func(rand(3), rand(3))  # works
func(rand(3), rand(1))
...
```

...

</details>

### supervisely

Supervisely Python SDK.

`pip install supervisely` · installs (wheel) · licence: not stated · rank 14531 · last release 2026-10-27 · [PyPI](https://pypi.org/project/supervisely/)

<details><summary>README extract</summary>

Open Ecosystem of Apps,
SDK for Python

Website:

Supervisely Ecosystem:

Dev Documentation:

Source Code of SDK for Python:

Supervisely Ecosystem on GitHub:

Complete video course on YouTube: What is Supervisely?

Example:
```python
import supervisely as sly

# authenticate with your personal API token
api = sly.Api.from_env()

# create project and dataset
project = api.project.create(workspace_id=123, name="demo project")
dataset = api.dataset.create(project.id, "dataset-01")

# upload data
image_info = api.image.upload_path(dataset.id, "img.png", "/Users/max/img.png")
...
```

...

</details>

### tfds-nightly

tensorflow/datasets is a library of datasets ready to use with TensorFlow.

`pip install tfds-nightly` · installs (wheel) · licence: Apache Software License · rank 14556 · last release 2025-10-25 · [PyPI](https://pypi.org/project/tfds-nightly/)

<details><summary>README extract</summary>

tensorflow/datasets is a library of public datasets ready to use with
TensorFlow. Each dataset definition contains the logic necessary to download and
prepare the dataset, as well as to read it into a model using the
`tf.data.Dataset` API.

Usage outside of TensorFlow is also supported.

See the README on GitHub for further documentation.

</details>

### deepecho

Create sequential synthetic data of mixed types using a GAN.

`pip install deepecho` · installs (wheel) · licence: BUSL-1.1 · rank 14606 · last release 2026-10-30 · [PyPI](https://pypi.org/project/deepecho/) · [source](https://github.com/sdv-dev/Deepecho/)

<details><summary>README extract</summary>

This repository is part of The Synthetic Data Vault Project, a project from DataCebo.

Features:
DeepEcho is a Synthetic Data Generation Python library for mixed-type, **multivariate
time series**. It provides:

1. Multiple models based both on classical statistical modeling of time series and the latest
 in Deep Learning techniques.
2. ...

Example:
```python
from deepecho import PARModel
from deepecho.demo import load_demo

# Load demo data
data = load_demo()

# Define data types for all the columns
data_types = {
    'region': 'categorical',
    'day_of_week': 'categorical',
    'total_sales': 'continuous',
    'nb_customers': 'count',
}

model = PARModel(cuda=False)
```

Sections: Overview, Quickstart, Standalone usage, What's next?

</details>

### tsdb

TSDB (Time Series Data Beans): a Python toolbox helping load 172 open-source time-series datasets

`pip install tsdb` · installs (wheel) · licence: BSD License · rank 14634 · last release 2026-04-09 · [PyPI](https://pypi.org/project/tsdb/) · [docs](https://docs.pypots.com) · [source](https://github.com/WenjieDu/TSDB)

<details><summary>README extract</summary>

*load 173 public time-series datasets with a single line of code ;-)

TSDB is a part of

PyPOTS

(a Python toolbox for data mining on Partially-Observed Time Series), and was separated from PyPOTS for decoupling datasets from learning algorithms. ...

Example:
```python
import tsdb

# list all available datasets in TSDB
tsdb.list()
# 'physionet_2012',
# 'physionet_2019',
# 'electricity_load_diagrams',
# 'beijing_multisite_air_quality',
# 'italy_air_quality',
# 'vessel_ais',
# 'electricity_transformer_temperature',
# 'pems_traffic',
# 'solar_alabama',
# 'ucr_uea_ACSF1',
# 'ucr_uea_Adiac',
# ...

...
```

Sections: Welcome to TSDB, ❖ Usage Examples, ❖ List of Available Datasets, ❖ Citing TSDB/PyPOTS

</details>

### medspacy-quickumls

QuickUMLS is a tool for fast, unsupervised biomedical concept extraction from medical text

`pip install medspacy-quickumls` · installs from source (sdist only) · licence: MIT License · rank 14710 · last release 2024-05-14 · [PyPI](https://pypi.org/project/medspacy-quickumls/)

<details><summary>README extract</summary>

[NOTE: This is an updated fork of QuickUMLS for usage in medspacy to accelerate recent developments from the medspacy team to incorporate QuickUMLS into spacy pipelines.]

Example:
```python
from quickumls import QuickUMLS

matcher = QuickUMLS(quickumls_fp, overlapping_criteria, threshold,
                    similarity_name, window, accepted_semtypes)
```

Sections: QuickUMLS, APIs, spaCy pipeline component, References

</details>

### fbgemm-gpu-nightly-cpu

(no summary)

`pip install fbgemm-gpu-nightly-cpu` · installs (wheel) · licence: BSD License · rank 14836 · last release 2026-10-16 · [PyPI](https://pypi.org/project/fbgemm-gpu-nightly-cpu/)

<details><summary>README extract</summary>

FBGEMM_GPU (FBGEMM GPU Kernels Library) is a collection of high-performance
PyTorch GPU operator libraries for training and inference. The library provides
efficient table batched embedding bag, data layout transformation, and
quantization supports. ...

</details>

### torch-xla

XLA bridge for PyTorch

`pip install torch-xla` · does not install on CPython 3.14 · licence: BSD License · rank 14889 · last release 2025-11-17 · [PyPI](https://pypi.org/project/torch-xla/) · [source](https://github.com/pytorch/xla)

<details><summary>README extract</summary>

<b>Current CI status:</b>

PyTorch/XLA is a Python package that uses the XLA deep learning
compiler to connect the PyTorch deep learning
framework and Cloud
TPUs. You can try it right now, for free, on a
single Cloud TPU VM with
Kaggle!

Take a look at one of our Kaggle
notebooks to get
started: ...

Sections: PyTorch/XLA, TPU, C++11 ABI builds, Github Doc Map, Getting Started, Simple single process, Multi processing, PyTorch/XLA tutorials, Reference implementations, Available docker images and wheels, Python packages, Use nightly build, Docker, Troubleshooting

</details>

### otari

Python client for the otari gateway

`pip install otari` · installs (wheel) · licence: Apache-2.0 · rank 14977 · last release 2026-09-25 · [PyPI](https://pypi.org/project/otari/) · [docs](https://mozilla-ai.github.io/otari/) · [source](https://github.com/mozilla-ai/otari-sdk-python)

<details><summary>README extract</summary>

Python client for otari, the open-source core that powers otari.ai.
Communicate with any LLM provider through otari using a single, typed interface.

TypeScript SDK | Documentation | Platform (Beta)

> New to otari? The otari repo explains what it is and why you’d use it.

Example:
```python
from otari import OtariClient

client = OtariClient(
    platform_token="tk_your_api_token",
)

response = client.completion(
    model="openai:gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)

print(response.choices[0].message.content)
```

Sections: Otari Python Client SDK, Quickstart, Requirements, Setting up credentials, Authentication, Usage, Chat completions, Streaming, Responses API, Messages API, Response metadata, Embeddings, Listing models, Moderation

</details>

### exmol

Counterfactual generation with STONED SELFIES

`pip install exmol` · installs (wheel) · licence: MIT License · rank 14982 · last release 2025-05-08 · [PyPI](https://pypi.org/project/exmol/)

<details><summary>README extract</summary>

- Explaining why that molecule
 - Install
 - Quickstart
 - Counterfactual Generation
 - Descriptor Attribution
 - Usage
 - Further Examples
 - Chemical Space
 - SVG
 - Disable Progress Bars
 - API and Docs
 - Developing
 - Citation

`exmol` is a package to explain black-box predictions of molecules. ...

Example:
```python
import exmol

# mol of interest
base = 'Cc1onc(-c2ccccc2Cl)c1C(=O)NC1C(=O)N2C1SC(C)(C)C2C(=O)O'

samples = exmol.sample_space(base, my_model, batched=False)
```

Sections: Explaining why that molecule, Quickstart, Counterfactual Generation, Descriptor Attribution, Usage, Further Examples, Chemical Space, SVG, Disable Progress Bars, API and Docs

</details>

## Also in this topic

- [onnxruntime](scientific-engineering.md#onnxruntime) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [torch](scientific-engineering.md#torch) - Tensors and Dynamic neural networks in Python with strong GPU acceleration
- [nltk](scientific-engineering.md#nltk) - Natural Language Toolkit
- [nvidia-nccl-cu12](scientific-engineering.md#nvidia-nccl-cu12) - NVIDIA Collective Communication Library (NCCL) Runtime
- [nvidia-nccl-cu13](scientific-engineering.md#nvidia-nccl-cu13) - NVIDIA Collective Communication Library (NCCL) Runtime
- [nvidia-cudnn-cu13](scientific-engineering.md#nvidia-cudnn-cu13) - cuDNN runtime libraries
- [nvidia-cublas](scientific-engineering.md#nvidia-cublas) - CUBLAS native runtime libraries
- [nvidia-nvjitlink](scientific-engineering.md#nvidia-nvjitlink) - Nvidia JIT LTO Library
- [nvidia-nvshmem-cu13](scientific-engineering.md#nvidia-nvshmem-cu13) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [nvidia-cuda-nvrtc](scientific-engineering.md#nvidia-cuda-nvrtc) - NVRTC native runtime libraries
- [nvidia-cufft](scientific-engineering.md#nvidia-cufft) - CUFFT native runtime libraries
- [nvidia-cusolver](scientific-engineering.md#nvidia-cusolver) - CUDA solver native runtime libraries
- [nvidia-cusparse](scientific-engineering.md#nvidia-cusparse) - CUSPARSE native runtime libraries
- [nvidia-cuda-runtime](scientific-engineering.md#nvidia-cuda-runtime) - CUDA Runtime native Libraries
- [nvidia-cuda-cupti](scientific-engineering.md#nvidia-cuda-cupti) - CUDA profiling tools runtime libs.
- [nvidia-cufile](scientific-engineering.md#nvidia-cufile) - cuFile GPUDirect libraries
- [nvidia-nvtx](scientific-engineering.md#nvidia-nvtx) - NVIDIA Tools Extension
- [nvidia-curand](scientific-engineering.md#nvidia-curand) - CURAND native runtime libraries
- [spacy-legacy](scientific-engineering.md#spacy-legacy) - Legacy registered functions for spaCy backwards compatibility
- [nvidia-cudnn-cu12](scientific-engineering.md#nvidia-cudnn-cu12) - cuDNN runtime libraries
- [nvidia-cublas-cu12](scientific-engineering.md#nvidia-cublas-cu12) - CUBLAS native runtime libraries
- [nvidia-cuda-nvrtc-cu12](scientific-engineering.md#nvidia-cuda-nvrtc-cu12) - NVRTC native runtime libraries
- [nvidia-cufft-cu12](scientific-engineering.md#nvidia-cufft-cu12) - CUFFT native runtime libraries
- [nvidia-cusparse-cu12](scientific-engineering.md#nvidia-cusparse-cu12) - CUSPARSE native runtime libraries
- [nvidia-cusolver-cu12](scientific-engineering.md#nvidia-cusolver-cu12) - CUDA solver native runtime libraries
- [nvidia-nvjitlink-cu12](scientific-engineering.md#nvidia-nvjitlink-cu12) - Nvidia JIT LTO Library
- [nvidia-cuda-runtime-cu12](scientific-engineering.md#nvidia-cuda-runtime-cu12) - CUDA Runtime native Libraries
- [nvidia-curand-cu12](scientific-engineering.md#nvidia-curand-cu12) - CURAND native runtime libraries
- [nvidia-cuda-cupti-cu12](scientific-engineering.md#nvidia-cuda-cupti-cu12) - CUDA profiling tools runtime libs.
- [nvidia-nvtx-cu12](scientific-engineering.md#nvidia-nvtx-cu12) - NVIDIA Tools Extension
- [optuna](scientific-engineering.md#optuna) - A hyperparameter optimization framework
- [tensorflow](scientific-engineering.md#tensorflow) - TensorFlow is an open source machine learning framework for everyone.
- [kfp](scientific-engineering.md#kfp) - Kubeflow Pipelines SDK
- [timm](scientific-engineering.md#timm) - PyTorch Image Models
- [shap](scientific-engineering.md#shap) - A unified approach to explain the output of any machine learning model.
- [tritonclient](scientific-engineering.md#tritonclient) - Python client library and utilities for communicating with Triton Inference Server
- [nvidia-cufile-cu12](scientific-engineering.md#nvidia-cufile-cu12) - cuFile GPUDirect libraries
- [livekit-api](multimedia-sound-audio.md#livekit-api) - Python Server API for LiveKit
- [livekit](multimedia-sound-audio.md#livekit) - Python Real-time SDK for LiveKit
- [tensorflow-estimator](scientific-engineering.md#tensorflow-estimator) - TensorFlow Estimator.
- [pydantic-ai](internet.md#pydantic-ai) - AI Agent Framework, the Pydantic way
- [gradio](scientific-engineering.md#gradio) - Python library for easily interacting with trained machine learning models
- [gradio-client](scientific-engineering.md#gradio-client) - Python library for easily interacting with trained machine learning models
- [torchaudio](multimedia-sound-audio.md#torchaudio) - An audio package for PyTorch
- [nvidia-nvshmem-cu12](scientific-engineering.md#nvidia-nvshmem-cu12) - NVSHMEM creates a global address space that provides efficient and scalable communication for NVIDIA GPU clusters.
- [ultralytics](scientific-engineering.md#ultralytics) - Ultralytics YOLO 🚀 for SOTA object detection, instance segmentation, semantic segmentation, depth estimation, classification, pose estimation, oriented object detection, and multi-object tracking.
- [ultralytics-thop](scientific-engineering.md#ultralytics-thop) - Ultralytics THOP package for fast computation of PyTorch model FLOPs and parameters.
- [livekit-agents](multimedia-sound-audio.md#livekit-agents) - A powerful framework for building realtime voice AI agents
- [livekit-blingfire](multimedia-sound-audio.md#livekit-blingfire) - BlingFire bindings for livekit-agents
- [tensorflow-text](scientific-engineering.md#tensorflow-text) - TF.Text is a TensorFlow library of text related ops, modules, and subgraphs.
- [xai-sdk](internet-www-http.md#xai-sdk) - The official Python SDK for the xAI API
- [tensorflow-serving-api](scientific-engineering.md#tensorflow-serving-api) - TensorFlow Serving Python API.
- [pysbd](scientific-engineering.md#pysbd) - pysbd (Python Sentence Boundary Disambiguation) is a rule-based sentence boundary detection that works out-of-the-box across many languages.
- [nvidia-cuda-cccl](scientific-engineering.md#nvidia-cuda-cccl) - CUDA CCCL
- [sacrebleu](scientific-engineering.md#sacrebleu) - Hassle-free computation of shareable, comparable, and reproducible BLEU, chrF, and TER scores
- [dbos](database.md#dbos) - Ultra-lightweight durable execution in Python
- [rembg](scientific-engineering.md#rembg) - Remove image background
- [tensorflow-io-gcs-filesystem](scientific-engineering.md#tensorflow-io-gcs-filesystem) - TensorFlow IO
- [livekit-plugins-silero](multimedia-sound-audio.md#livekit-plugins-silero) - Agent Framework Plugin for Silero
- [nvidia-nvvm](scientific-engineering.md#nvidia-nvvm) - NVVM Libraries
- [nvidia-cuda-nvcc](scientific-engineering.md#nvidia-cuda-nvcc) - CUDA nvcc
- [nvidia-cuda-crt](scientific-engineering.md#nvidia-cuda-crt) - CUDA C Runtime
- [livekit-plugins-openai](multimedia-sound-audio.md#livekit-plugins-openai) - Agent Framework plugin for services from OpenAI
- [mediapipe](scientific-engineering.md#mediapipe) - MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web. See the privacy notice at https://goo.gle/mediapipe-privacy.
- [albumentations](scientific-engineering.md#albumentations) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volumes, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows.
- [onnxruntime-gpu](scientific-engineering.md#onnxruntime-gpu) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [nvidia-cuda-nvdisasm](scientific-engineering.md#nvidia-cuda-nvdisasm) - CUDA nvdisasm
- [kornia-rs](scientific-engineering.md#kornia-rs) - Low level implementations for computer vision in Rust
- [ml-collections](scientific-engineering.md#ml-collections) - ML Collections is a library of Python collections designed for ML usecases.
- [silero-vad](scientific-engineering.md#silero-vad) - Voice Activity Detector (VAD) by Silero
- [livekit-plugins-elevenlabs](multimedia-sound-audio.md#livekit-plugins-elevenlabs) - Agent Framework plugin for voice synthesis with ElevenLabs' API.
- [open-clip-torch](scientific-engineering.md#open-clip-torch) - Open reproduction of contrastive language-image pretraining (CLIP) and related.
- [livekit-plugins-deepgram](multimedia-sound-audio.md#livekit-plugins-deepgram) - Agent Framework plugin for services using Deepgram's API.
- [livekit-plugins-cartesia](multimedia-sound-audio.md#livekit-plugins-cartesia) - LiveKit Agents Plugin for Cartesia
- [tf-keras](scientific-engineering.md#tf-keras) - Deep learning for humans.
- [stagehand](internet-www-http.md#stagehand) - Browserbase's SDK for building browser agents
- [cma](scientific-engineering.md#cma) - CMA-ES, Covariance Matrix Adaptation Evolution Strategy for non-linear numerical optimization in Python
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [tensorflow-cpu](scientific-engineering.md#tensorflow-cpu) - TensorFlow is an open source machine learning framework for everyone.
- [nvidia-cublas-cu11](scientific-engineering.md#nvidia-cublas-cu11) - CUBLAS native runtime libraries
- [nvidia-cudnn-cu11](scientific-engineering.md#nvidia-cudnn-cu11) - cuDNN runtime libraries
- [torch-audiomentations](multimedia.md#torch-audiomentations) - A Pytorch library for audio data augmentation. Inspired by audiomentations. Useful for deep learning.
- [pipecat-ai](communications-conferencing.md#pipecat-ai) - An open source framework for voice (and multimodal) assistants
- [nvidia-cuda-nvcc-cu12](scientific-engineering.md#nvidia-cuda-nvcc-cu12) - CUDA nvcc
- [livekit-plugins-turn-detector](multimedia-sound-audio.md#livekit-plugins-turn-detector) - End of utterance detection for LiveKit Agents
- [instanttensor](scientific-engineering.md#instanttensor) - An ultra-fast, distributed Safetensors loader
- [livekit-plugins-google](multimedia-sound-audio.md#livekit-plugins-google) - Agent Framework plugin for services from Google Cloud
- [nvidia-cuda-runtime-cu11](scientific-engineering.md#nvidia-cuda-runtime-cu11) - CUDA Runtime native Libraries
- [nvidia-cuda-nvrtc-cu11](scientific-engineering.md#nvidia-cuda-nvrtc-cu11) - NVRTC native runtime libraries
- [livekit-plugins-assemblyai](multimedia-sound-audio.md#livekit-plugins-assemblyai) - Agent Framework plugin for AssemblyAI
- [supervision](multimedia-graphics.md#supervision) - A set of easy-to-use utils that will come in handy in any Computer Vision project
- [lap](education.md#lap) - Linear Assignment Problem solver (LAPJV/LAPMOD).
- [scrapling](internet-www-http.md#scrapling) - Scrapling is an undetectable, powerful, flexible, high-performance Python framework that makes Web Scraping easy and effortless as it should be!
- [tensorflow-hub](scientific-engineering.md#tensorflow-hub) - TensorFlow Hub is a library to foster the publication, discovery, and consumption of reusable parts of machine learning models.
- [paddlex](scientific-engineering.md#paddlex) - Low-code development tool based on PaddlePaddle.
- [demucs](multimedia-sound-audio.md#demucs) - Music source separation in the waveform domain.
- [stanza](scientific-engineering.md#stanza) - A Python NLP Library for Many Human Languages, by the Stanford NLP Group
- [tensorflow-probability](scientific-engineering.md#tensorflow-probability) - Probabilistic modeling and statistical inference in TensorFlow
- [milvus-lite](database.md#milvus-lite) - Lightweight version of Milvus for local development and testing
- [flyteidl](scientific-engineering.md#flyteidl) - IDL for Flyte Platform
- [pymoo](scientific-engineering.md#pymoo) - Multi-Objective Optimization in Python
- [optuna-integration](scientific-engineering.md#optuna-integration) - Integration libraries of Optuna.
- [mlxtend](scientific-engineering.md#mlxtend) - Machine Learning Library Extensions
- [spark-nlp](scientific-engineering.md#spark-nlp) - John Snow Labs Spark NLP is a natural language processing library built on top of Apache Spark ML. It provides simple, performant & accurate NLP annotations for machine learning pipelines, that scale easily in a distributed environment.
- [nvidia-cusparse-cu11](scientific-engineering.md#nvidia-cusparse-cu11) - CUSPARSE native runtime libraries
- [nvidia-cufft-cu11](scientific-engineering.md#nvidia-cufft-cu11) - CUFFT native runtime libraries
- [usearch](database-database-engines-servers.md#usearch) - Smaller & Faster Single-File Vector Search Engine from Unum
- [sktime](scientific-engineering.md#sktime) - A unified framework for machine learning with time series
- [nvidia-cusolver-cu11](scientific-engineering.md#nvidia-cusolver-cu11) - CUDA solver native runtime libraries
- [livekit-plugins-anthropic](multimedia-sound-audio.md#livekit-plugins-anthropic) - Agent Framework plugin for services from Anthropic
- [nvidia-curand-cu11](scientific-engineering.md#nvidia-curand-cu11) - CURAND native runtime libraries
- [nvidia-cuda-cupti-cu11](scientific-engineering.md#nvidia-cuda-cupti-cu11) - CUDA profiling tools runtime libs.
- [nvidia-nvtx-cu11](scientific-engineering.md#nvidia-nvtx-cu11) - NVIDIA Tools Extension
- [nvidia-nccl-cu11](scientific-engineering.md#nvidia-nccl-cu11) - NVIDIA Collective Communication Library (NCCL) Runtime
- [livekit-plugins-krisp](multimedia-sound-audio.md#livekit-plugins-krisp) - Krisp VIVA noise reduction plugin for LiveKit Agents
- [ibm-watsonx-ai](internet.md#ibm-watsonx-ai) - IBM watsonx.ai API Client
- [google-cloud-pipeline-components](scientific-engineering.md#google-cloud-pipeline-components) - This SDK enables a set of First Party (Google owned) pipeline components that allow users to take their experience from Vertex AI SDK and other Google Cloud services and create a corresponding pipeline using KFP or Managed Pipelines.
- [flytekit](scientific-engineering.md#flytekit) - Flyte SDK for Python
- [monai](scientific-engineering.md#monai) - AI Toolkit for Healthcare Imaging
- [unitycatalog-ai](scientific-engineering.md#unitycatalog-ai) - Official Python library for Unity Catalog AI support
- [fiddle](scientific-engineering.md#fiddle) - Fiddle: A Python-first configuration library
- [chainlit](communications-chat.md#chainlit) - Build Conversational AI.
- [pytorch-tokenizers](scientific-engineering.md#pytorch-tokenizers) - A package with common tokenizers in Python and C++
- [openshell](scientific-engineering.md#openshell) - OpenShell is the safe, private runtime for autonomous AI agents.
- [nemo-toolkit](scientific-engineering.md#nemo-toolkit) - NeMo - a toolkit for Conversational AI
- [nvidia-cuda-tileiras](scientific-engineering.md#nvidia-cuda-tileiras) - TileIR Assembler Package
- [tfp-nightly](scientific-engineering.md#tfp-nightly) - Probabilistic modeling and statistical inference in TensorFlow
- [megatron-core](scientific-engineering.md#megatron-core) - Megatron Core - a library for efficient and scalable training of transformer based models
- [ai-edge-litert](scientific-engineering.md#ai-edge-litert) - LiteRT is for mobile and embedded devices.
- [gin-config](scientific-engineering.md#gin-config) - Gin-Config: A lightweight configuration library for Python
- [encodec](multimedia-sound-audio.md#encodec) - High fidelity neural audio codec
- [nvidia-cuda-cccl-cu12](scientific-engineering.md#nvidia-cuda-cccl-cu12) - CUDA CCCL
- [pygam](scientific-engineering.md#pygam) - Generalized Additive Models in Python.
- [planarity](scientific-engineering.md#planarity) - Python Wrapper for the Edge Addition Planarity Suite and Graph Library
- [effdet](scientific-engineering.md#effdet) - EfficientDet for PyTorch
- [keybert](scientific-engineering.md#keybert) - KeyBERT performs keyword extraction with state-of-the-art transformer models.
- [livekit-plugins-soniox](multimedia-sound-audio.md#livekit-plugins-soniox) - Agent Framework plugin for services using Soniox's API.
- [bertopic](scientific-engineering.md#bertopic) - BERTopic performs topic Modeling with state-of-the-art transformer models.
- [flyteidl2](scientific-engineering.md#flyteidl2) - IDL for Flyte
- [pixeltable-pgserver](database.md#pixeltable-pgserver) - Embedded Postgres Server for Pixeltable
- [funasr](multimedia-sound-audio.md#funasr) - OpenAI-compatible speech recognition toolkit with WebSocket streaming, vLLM acceleration, and llama.cpp/GGUF edge runtime.
- [gluonts](scientific-engineering.md#gluonts) - Probabilistic time series modeling in Python.
- [audiomentations](multimedia.md#audiomentations) - A Python library for audio data augmentation. Inspired by albumentations. Useful for machine learning.
- [lhotse](multimedia-sound-audio.md#lhotse) - Data preparation for speech processing models training.
- [livekit-plugins-xai](multimedia-sound-audio.md#livekit-plugins-xai) - Agent Framework plugin for xAI
- [pgmpy](scientific-engineering.md#pgmpy) - Python Toolkit for Causal and Probabilistic Reasoning
- [daily-python](communications-conferencing.md#daily-python) - Daily Client SDK for Python
- [pybullet](games-entertainment-simulation.md#pybullet) - Official Python Interface for the Bullet Physics SDK specialized for Robotics Simulation and Reinforcement Learning
- [rfdetr](scientific-engineering.md#rfdetr) - RF-DETR
- [tflite-runtime](scientific-engineering.md#tflite-runtime) - TensorFlow Lite is for mobile and embedded devices.
- [onnx-asr](multimedia-sound-audio.md#onnx-asr) - A lightweight Python package for Automatic Speech Recognition using ONNX models
- [livekit-plugins-azure](multimedia-sound-audio.md#livekit-plugins-azure) - Agent Framework plugin for services from Azure
- [ConfigSpace](scientific-engineering.md#configspace) - Creation and manipulation of parameter configuration spaces for automated algorithm configuration and hyperparameter tuning.
- [resemble-perth](multimedia-sound-audio.md#resemble-perth) - Audio Watermarking and Detection Library
- [nvidia-npp-cu12](scientific-engineering.md#nvidia-npp-cu12) - NPP native runtime libraries
- [workspace-mcp](communications-chat.md#workspace-mcp) - Comprehensive, highly performant Google Workspace Streamable HTTP & SSE MCP Server for Calendar, Gmail, Docs, Sheets, Slides & Drive
- [mxnet](scientific-engineering.md#mxnet) - Apache MXNet is an ultra-scalable deep learning framework. This version uses openblas and MKLDNN.
- [npmai-agents](office-business-scheduling.md#npmai-agents) - Production-grade autonomous AI agent framework with 1,371 tools across 100 classes and a 5-role LLM pipeline — built on the NPMAI ECOSYSTEM.
- [onnxruntime-openvino](scientific-engineering.md#onnxruntime-openvino) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [poutyne](scientific-engineering.md#poutyne) - A simplified framework and utilities for PyTorch.
- [livekit-plugins-aws](multimedia-sound-audio.md#livekit-plugins-aws) - LiveKit Agents Plugin for services from AWS
- [deepparse](scientific-engineering.md#deepparse) - A library for parsing multinational street addresses using deep learning.
- [tf-keras-nightly](scientific-engineering.md#tf-keras-nightly) - Deep learning for humans.
- [torch-tb-profiler](scientific-engineering.md#torch-tb-profiler) - PyTorch Profiler TensorBoard Plugin
- [cassio](scientific-engineering.md#cassio) - A framework-agnostic Python library to seamlessly integrate Apache Cassandra(R) with ML/LLM/genAI workloads.
- [livekit-plugins-groq](multimedia-sound-audio.md#livekit-plugins-groq) - Groq inference plugin for LiveKit Agents
- [gradio-rangeslider](scientific-engineering.md#gradio-rangeslider) - 🛝 Slider component for selecting a range of values
- [tf-nightly](scientific-engineering.md#tf-nightly) - TensorFlow is an open source machine learning framework for everyone.
- [tf2onnx](scientific-engineering.md#tf2onnx) - Tensorflow to ONNX converter
- [foundry-local-sdk](scientific-engineering.md#foundry-local-sdk) - Foundry Local Python SDK (v2): in-process Python bindings for the Foundry Local native runtime.
- [tensorflow-io](scientific-engineering.md#tensorflow-io) - TensorFlow IO
- [ale-py](scientific-engineering.md#ale-py) - The Arcade Learning Environment (ALE) - a platform for AI research.
- [livekit-plugins-rime](multimedia-sound-audio.md#livekit-plugins-rime) - LiveKit Agents Plugin for Rime
- [dlib](scientific-engineering.md#dlib) - A toolkit for making real world machine learning and data analysis applications
- [pytorch-forecasting](scientific-engineering.md#pytorch-forecasting) - Forecasting timeseries with PyTorch - dataloaders, normalizers, metrics and models
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [openTSNE](scientific-engineering.md#opentsne) - Extensible, parallel implementations of t-SNE
- [spacy-transformers](scientific-engineering.md#spacy-transformers) - spaCy pipelines for pre-trained BERT and other transformers
- [tfx-bsl](scientific-engineering.md#tfx-bsl) - tfx_bsl (TFX Basic Shared Libraries) contains libraries shared by many TFX (TensorFlow eXtended) libraries and components.
- [torchreid](education.md#torchreid) - Torchreid-Pip: Deep learning person re-identification in PyTorch.
- [omnivoice](multimedia-sound-audio.md#omnivoice) - OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models
- [tensorflowjs](scientific-engineering.md#tensorflowjs) - 
- [albumentationsx](scientific-engineering.md#albumentationsx) - Fast, flexible, and advanced augmentation library for deep learning, computer vision, and medical imaging. Albumentations offers a wide range of transformations for both 2D (images, masks, bboxes, keypoints) and 3D (volume data, volumetric masks, keypoints) data, with optimized performance and seamless integration into ML workflows. Available under AGPL-3.0-only or a commercial license with agreed coverage for your team, products, and deployments.
- [bittensor-wallet](scientific-engineering.md#bittensor-wallet) - 
- [swanlab](scientific-engineering.md#swanlab) - Python library for streamlined tracking and management of AI training processes.
- [clip-interrogator](education.md#clip-interrogator) - Generate a prompt from an image
- [nemo-text-processing](scientific-engineering.md#nemo-text-processing) - NeMo text processing for ASR and TTS
- [ai-edge-litert-nightly](scientific-engineering.md#ai-edge-litert-nightly) - LiteRT is for mobile and embedded devices.
- [onnxruntime-directml](scientific-engineering.md#onnxruntime-directml) - ONNX Runtime is a runtime accelerator for Machine Learning models
- [livekit-plugins-speechmatics](multimedia-sound-audio.md#livekit-plugins-speechmatics) - Agent Framework plugin for Speechmatics
- [torchax](scientific-engineering.md#torchax) - torchax is a library for running Jax and PyTorch together
- [spacy-alignments](scientific-engineering.md#spacy-alignments) - A spaCy package for the Rust tokenizations library
- [iden](scientific-engineering.md#iden) - simple library to manage a dataset of shards to train machine learning models
- [ecologits](internet.md#ecologits) - EcoLogits tracks and estimates the energy consumption and environmental impacts of using generative AI models through APIs.
- [krippendorff](scientific-engineering.md#krippendorff) - Fast computation of the Krippendorff's alpha measure.
- [pytorch_optimizer](scientific-engineering.md#pytorch_optimizer) - optimizer & lr scheduler & objective function collections in PyTorch
- [tensorflow-decision-forests](scientific-engineering.md#tensorflow-decision-forests) - Collection of training and inference decision forest algorithms.
- [analytics-mcp](internet.md#analytics-mcp) - MCP server for Google Analytics
- [blackjax](education.md#blackjax) - Flexible and fast sampling in Python
- [litert-converter](scientific-engineering-2.md#litert-converter) - LiteRT is for mobile and embedded devices.
- [tensorflow-data-validation](scientific-engineering-2.md#tensorflow-data-validation) - A library for exploring and validating machine learning data.
- [bittensor-drand](scientific-engineering-2.md#bittensor-drand) - Rust-backed Python library for generating timelock-encrypted weight commitments for Bittensor's commit-reveal mechanism using drand randomness.
- [turboquant-py](scientific-engineering-2.md#turboquant-py) - Python implementation of the TurboQuant and QJL vector quantization algorithms
- [kubeflow](scientific-engineering-2.md#kubeflow) - Kubeflow Python SDK to manage ML workloads and to interact with Kubeflow APIs.
- [livekit-plugins-inworld](multimedia-sound-audio.md#livekit-plugins-inworld) - Agent Framework plugin for voice synthesis and speech-to-text with Inworld's API.
- [livekit-plugins-gladia](multimedia-sound-audio.md#livekit-plugins-gladia) - Agent Framework plugin for services using Gladia's API.
- [lightly](scientific-engineering-2.md#lightly) - A deep learning package for self-supervised learning and world models
- [h2o-authn](internet.md#h2o-authn) - H2O Python Clients Authentication Helpers
- [coqui-tts](multimedia.md#coqui-tts) - Deep learning for Text to Speech.
- [tensorflow-intel](scientific-engineering-2.md#tensorflow-intel) - TensorFlow is an open source machine learning framework for everyone.
- [ydf](scientific-engineering-2.md#ydf) - YDF (short for Yggdrasil Decision Forests) is a library for training, serving, evaluating and analyzing decision forest models such as Random Forest and Gradient Boosted Trees.
- [flytekitplugins-ray](scientific-engineering-2.md#flytekitplugins-ray) - This package holds the Ray plugins for flytekit
- [trackers](scientific-engineering-2.md#trackers) - A unified library for object tracking featuring clean room re-implementations of leading multi-object tracking algorithms
- [tensorizer](internet.md#tensorizer) - A tool for fast PyTorch module, model, and tensor serialization + deserialization.
- [sharepoint-to-text](communications-email.md#sharepoint-to-text) - Text extraction library for typical file formats found in SharePoint repositories
- [nvidia-matmul-heuristics](scientific-engineering-2.md#nvidia-matmul-heuristics) - NVIDIA Matmul Heuristics
- [open-spiel](games-entertainment.md#open-spiel) - A Framework for Reinforcement Learning in Games
- [ai](internet.md#ai) - AI Agent Framework for Python
- [skorch](scientific-engineering-2.md#skorch) - scikit-learn compatible neural network library for pytorch
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [lightly-utils](scientific-engineering-2.md#lightly-utils) - A utility package for lightly
- [livekit-plugins-fishaudio](multimedia-sound-audio.md#livekit-plugins-fishaudio) - Agent Framework plugin for voice synthesis and speech recognition with Fish Audio's API.
- [nvidia-nvfatbin-cu12](scientific-engineering-2.md#nvidia-nvfatbin-cu12) - NVIDIA compiler library for fatbin interaction
- [skforecast](scientific-engineering-2.md#skforecast) - Python library for time series forecasting using scikit-learn compatible models, statistical methods, and foundation models.
- [tensorflow-recommenders](scientific-engineering-2.md#tensorflow-recommenders) - Tensorflow Recommenders, a TensorFlow library for recommender systems.
- [skrl](scientific-engineering-2.md#skrl) - Modular and flexible library for reinforcement learning on PyTorch, JAX and NVIDIA Warp
- [sec-parser](office-business-financial.md#sec-parser) - Parse SEC EDGAR HTML documents into a tree of elements that correspond to the visual structure of the document.
- [tensorflow-cpu-aws](scientific-engineering-2.md#tensorflow-cpu-aws) - TensorFlow is an open source machine learning framework for everyone.
- [livekit-plugins-langchain](multimedia-sound-audio.md#livekit-plugins-langchain) - LangChain/LangGraph plugin for LiveKit agents
- [flytekitplugins-spark](scientific-engineering-2.md#flytekitplugins-spark) - Spark 3 plugin for flytekit
- [pipecat-ai-whisker](communications-conferencing.md#pipecat-ai-whisker) - A real-time debugger for Pipecat
- [ai-dynamo-runtime](scientific-engineering-2.md#ai-dynamo-runtime) - Dynamo Inference Framework Runtime
- [netron](scientific-engineering-2.md#netron) - Viewer for neural network, deep learning and machine learning models.
- [torch-npu](scientific-engineering-2.md#torch-npu) - NPU bridge for PyTorch
- [livekit-plugins-anam](multimedia-sound-audio.md#livekit-plugins-anam) - Agent Framework plugin for anam
- [tensorflow-transform](scientific-engineering-2.md#tensorflow-transform) - A library for data preprocessing with TensorFlow
- [geneva](scientific-engineering-2.md#geneva) - Geneva - Multimodal Data Lake for AI
- [featrixsphere](internet-www-http-2.md#featrixsphere) - Transform any CSV into a production-ready ML model in minutes, not months.
- [nemo-gym](scientific-engineering-2.md#nemo-gym) - NeMo Gym is a library for building reinforcement learning environments
- [persista](scientific-engineering-2.md#persista) - library for persisting and caching data
- [flwr](scientific-engineering-2.md#flwr) - Flower: A Friendly Federated AI Framework
- [qiskit-connector](scientific-engineering-2.md#qiskit-connector) - Quantum Computing Qiskit Connector For Quantum Backend Use In Realtime
- [aisimulate](scientific-engineering-2.md#aisimulate) - AISimulate: GPU-free inference simulation and deployment configuration
- [pybboxes](education.md#pybboxes) - Light Weight Toolkit for Bounding Boxes
- [tensorflow-gpu](scientific-engineering-2.md#tensorflow-gpu) - Removed: please install "tensorflow" instead.
- [bithuman](multimedia.md#bithuman) - Real-time talking-avatar SDK: audio in, lip-synced frames out, on your own Mac, Linux or Windows machine.
- [nvidia-vfx](multimedia-video.md#nvidia-vfx) - Python bindings for NVIDIA Video Effects SDK
- [docculus](scientific-engineering-2.md#docculus) - Library for LangChain documents
- [dlib-bin](scientific-engineering-2.md#dlib-bin) - A toolkit for making real world machine learning and data analysis applications
- [executorch](scientific-engineering-2.md#executorch) - On-device AI across mobile, embedded and edge for PyTorch
- [ai-dynamo](scientific-engineering-2.md#ai-dynamo) - Distributed Inference Framework
- [livekit-plugins-sarvam](multimedia-sound-audio.md#livekit-plugins-sarvam) - Agent Framework plugin for services using Sarvam.ai's API.
- [supertonic](multimedia-sound-audio.md#supertonic) - High-quality Text-to-Speech synthesis with ONNX Runtime
- [lytekit](scientific-engineering-2.md#lytekit) - Latch fork of Flyte SDK for Python
- [inference-sdk](scientific-engineering-2.md#inference-sdk) - With no prior knowledge of machine learning or device-specific deployment, you can deploy a computer vision model to a range of devices and environments using Roboflow Inference.
- [konlpy](scientific-engineering-2.md#konlpy) - Python package for Korean natural language processing.
- [gradio-pdf](scientific-engineering-2.md#gradio-pdf) - Easily display PDFs in Gradio
- [yandex-cli](office-business.md#yandex-cli) - Interact with Yandex 360 services (Wiki, Tracker, Forms, …) from a CLI, an MCP server, or a Python SDK.
- [lytekitplugins-pods](scientific-engineering-2.md#lytekitplugins-pods) - Flytekit plugin to support K8s Pod tasks
- [pystempel](scientific-engineering-2.md#pystempel) - Polish stemmer.
- [torchio](scientific-engineering-2.md#torchio) - Tools for medical image processing with PyTorch
- [transnetv2-pytorch](multimedia-video.md#transnetv2-pytorch) - TransNetV2 PyTorch implementation for video scene detection
- [boxmot](scientific-engineering-2.md#boxmot) - BoxMOT: pluggable SOTA tracking modules for segmentation, object detection and pose estimation models
- [livekit-plugins-dtln](multimedia-sound-audio.md#livekit-plugins-dtln) - DTLN noise suppression plugin for LiveKit Agents — self-hosted, in-process, no cloud API
- [pygad](scientific-engineering-2.md#pygad) - PyGAD: A Python Library for Building the Genetic Algorithm and Training Machine Learning Algoithms (Keras & PyTorch).
- [tensorflow-io-nightly](scientific-engineering-2.md#tensorflow-io-nightly) - TensorFlow IO
- [mnn](scientific-engineering-2.md#mnn) - C methods for MNN Package
- [returnn](scientific-engineering-2.md#returnn) - The RWTH extensible training framework for universal recurrent neural networks
