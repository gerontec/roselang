# Communications / Conferencing

[Index](README.md) · 5 packages in this topic, 2 more listed under another topic, by downloads.

### pipecat-ai

An open source framework for voice (and multimodal) assistants

`pip install pipecat-ai` · installs (wheel) · licence: BSD-2-Clause · rank 3638 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pipecat-ai/) · [docs](https://docs.pipecat.ai/) · [source](https://github.com/pipecat-ai/pipecat)

<details><summary>README extract</summary>

Pipecat is an open-source Python framework for building real-time voice and multimodal conversational agents. Build a single voice agent or a full multi-agent system where specialists hand off, fan out in parallel, and coordinate over a shared bus, locally or distributed across processes and machines. ...

Sections: 🎙️ Pipecat: Real-Time Voice & Multimodal AI Agents, 🚀 What you can build, 🧠 Why Pipecat?, 🌐 Pipecat ecosystem, 📱 Client SDKs, 🧭 Structured conversations, 🪄 Beautiful UIs, 🛠️ Create and deploy projects, 🔍 Debugging, 🖥️ Terminal, 🤖 Claude Code skills, 📺️ Pipecat TV channel, 🎬 See it in action, 🧩 Available services

</details>

### daily-python

Daily Client SDK for Python

`pip install daily-python` · installs (wheel) · licence: BSD License · rank 6874 · last release 2026-11-03 · [PyPI](https://pypi.org/project/daily-python/) · [docs](https://reference-python.daily.co) · [source](https://github.com/daily-co/daily-python)

<details><summary>README extract</summary>

> Looking to develop voice and video agents?
> Check out our voice and multimodal conversational AI framework Pipecat, which has excellent support for Daily and already uses this Python SDK.

The Daily client SDK for Python allows you to build video and audio calling into your native desktop and server applications. ...

Sections: 🐍 Daily Client SDK for Python, 📚 Documentation, 📋 Requirements, 🛟 Getting help

</details>

### pipecat-ai-prebuilt

A simple, ready-to-use prebuilt client supporting all Pipecat transports.

`pip install pipecat-ai-prebuilt` · installs (wheel) · licence: BSD 2-Clause License · rank 8821 · last release 2026-10-02 · [PyPI](https://pypi.org/project/pipecat-ai-prebuilt/) · [source](https://github.com/pipecat-ai/pipecat-prebuilt)

<details><summary>README extract</summary>

A simple, ready-to-use prebuilt client supporting all Pipecat transports.

This prebuilt client provides a lightweight UI to quickly test and verify transport
behavior without needing a custom implementation.

Ideal for development, debugging, and quick prototyping.

Example:
```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pipecat_ai_prebuilt.frontend import PipecatPrebuiltUI

app = FastAPI()

# Mount the frontend at /client
app.mount("/client", PipecatPrebuiltUI)

@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/client/")
```

Sections: Pipecat AI Prebuilt, 🧰 Example Usage, 🧪 Try a Sample App, 📋 Prerequisites, 🔧 Set Up the Environment, 🚀 Publishing, Prerequisites, Publishing Process

</details>

### pipecat-ai-whisker

A real-time debugger for Pipecat

`pip install pipecat-ai-whisker` · installs (wheel) · licence: BSD-2-Clause · rank 12548 · last release 2026-08-19 · [PyPI](https://pypi.org/project/pipecat-ai-whisker/) · [source](https://github.com/pipecat-ai/whisker)

<details><summary>README extract</summary>

Whisker is a low-level debugger for the Pipecat voice and multimodal conversational AI framework.

Pipecat is a multi-agent systems: workers spawn sub-workers, send jobs to each other, and exchange messages on a shared bus. Whisker gives you a single view over the whole system so you can see exactly what every part is doing. ...

Example:
```python
pipeline = Pipeline(...)
worker = PipelineWorker(pipeline, ...)

whisker = WhiskerServer()
worker.add_observer(whisker.create_observer(worker))

runner = WorkerRunner()
await runner.add_workers(whisker, worker)
await runner.run()
```

...

</details>

### pipecat-ai-small-webrtc-prebuilt

A simple, ready-to-use client for testing the SmallWebRTCTransport.

`pip install pipecat-ai-small-webrtc-prebuilt` · installs (wheel) · licence: BSD 2-Clause License · rank 14283 · last release 2026-04-22 · [PyPI](https://pypi.org/project/pipecat-ai-small-webrtc-prebuilt/) · [source](https://github.com/pipecat-ai/small-webrtc-prebuilt)

<details><summary>README extract</summary>

A simple, ready-to-use client for testing the SmallWebRTCTransport.

This prebuilt client provides basic WebRTC functionality and serves as a lightweight tool
to quickly verify transport behavior without needing a custom implementation.

Ideal for development, debugging, and quick prototyping.

Example:
```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pipecat_ai_small_webrtc_prebuilt.frontend import SmallWebRTCPrebuiltUI

app = FastAPI()

# Mount the frontend at /prebuilt
app.mount("/prebuilt", SmallWebRTCPrebuiltUI)

@app.get("/", include_in_schema=False)
async def root_redirect():
...
```

Sections: SmallWebRTC Prebuilt, 🧰 Example Usage, 🧪 Try a Sample App, 📋 Prerequisites, 🔧 Set Up the Environment, 🚀 Publishing, Prerequisites, Publishing Process

</details>

## Also in this topic

- [matrix-client](communications-chat.md#matrix-client) - Client-Server SDK for Matrix
- [webexpythonsdk](communications.md#webexpythonsdk) - Work with the Webex APIs in native Python!
