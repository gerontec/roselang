# Communications / Chat

[Index](README.md) · 26 packages in this topic, 6 more listed under another topic, by downloads.

### slack-sdk

The Slack API Platform SDK for Python

`pip install slack-sdk` · installs (wheel) · licence: MIT License · rank 316 · last release 2026-10-30 · [PyPI](https://pypi.org/project/slack-sdk/) · [docs](https://docs.slack.dev/tools/python-slack-sdk/) · [source](https://github.com/slackapi/python-slack-sdk)

<details><summary>README extract</summary>

The Slack platform offers several APIs to build apps. Each Slack API delivers part of the capabilities from the platform, so that you can pick just those that fit for your needs. This SDK offers a corresponding package for each of Slack’s APIs. They are small and powerful when used independently, and work seamlessly when used together, too. ...

Example:
```python
import os
from slack_sdk import WebClient
from ssl import SSLContext

sslcert = SSLContext()
# pip3 install proxy.py
# proxy --port 9000 --log-level d
proxyinfo = "

client = WebClient(
    token=os.environ['SLACK_BOT_TOKEN'],
    ssl=sslcert,
    proxy=proxyinfo
)
response = client.chat_postMessage(channel="#random", text="Hello World!")
...
```

...

</details>

### python-telegram-bot

We have made you a wrapper you can't refuse

`pip install python-telegram-bot` · installs (wheel) · licence: LGPL-3.0-only · rank 1450 · last release 2026-06-12 · [PyPI](https://pypi.org/project/python-telegram-bot/) · [docs](https://docs.python-telegram-bot.org) · [source](https://github.com/python-telegram-bot/python-telegram-bot)

_README extract left out: share-alike licence._

### slackclient

Slack API clients for Web API and RTM API (Legacy) - Please use https://pypi.org/project/slack-sdk/ instead.

`pip install slackclient` · installs (wheel) · licence: MIT License · rank 1530 · last release 2022-04-22 · [PyPI](https://pypi.org/project/slackclient/)

<details><summary>README extract</summary>

This `slackclient` PyPI project is in maintenance mode now and `slack-sdk` project is the successor. The v3 SDK provides more functionalities such as Socket Mode, OAuth flow module, SCIM API, Audit Logs API, better asyncio support, retry handlers, and many more.

Refer to the migration guide to learn how to smoothly migrate your existing code.

Features:
The Python `slackclient` library is a developer kit for interfacing with the Slack Web API and Real Time Messaging (RTM) API on Python 3.6 and above.

Comprehensive documentation on using the Slack Python can be found at ...

Example:
```python
import os
from slack import RTMClient
from slack.errors import SlackApiError

@RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
...

</details>

### Telethon

Full-featured Telegram client library for Python 3

`pip install Telethon` · installs (wheel) · licence: MIT · rank 2202 · last release 2026-09-10 · [PyPI](https://pypi.org/project/Telethon/) · [docs](https://docs.telethon.dev) · [source](https://codeberg.org/Lonami/Telethon)

<details><summary>README extract</summary>

Telethon is an asyncio Python 3
MTProto library to interact with Telegram's API
as a user or through a bot account (bot API alternative).

Telegram is a popular messaging application. This library is meant
to make it easy for you to write Python programs that can interact
with Telegram. ...

Example:
```python
from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from  under API Development.
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
```

Sections: Telethon, What is this?, Creating a client, Doing stuff, Next steps

</details>

### aiogram

Modern and fully asynchronous framework for Telegram Bot API

`pip install aiogram` · installs (wheel) · licence: MIT · rank 2402 · last release 2026-08-26 · [PyPI](https://pypi.org/project/aiogram/) · [docs](https://docs.aiogram.dev/) · [source](https://github.com/aiogram/aiogram/)

<details><summary>README extract</summary>

aiogram is a modern and fully asynchronous framework for
Telegram Bot API written in Python 3.10+ using
asyncio and
aiohttp.

Make your bots faster and more powerful!

Documentation:
 - 🇺🇸 English
 - 🇺🇦 Ukrainian

Features:
- Asynchronous (asyncio docs, 492)
- Has type hints (484) and can be used with mypy
- Supports PyPy
- Supports Telegram Bot API 10.3 and gets fast updates to the latest versions of the Bot API ...

Sections: aiogram, Features

</details>

### mleap

MLeap Python API

`pip install mleap` · installs (wheel) · licence: Apache Software License · rank 3561 · last release 2026-10-05 · [PyPI](https://pypi.org/project/mleap/)

<details><summary>README extract</summary>

This package contains libraries to integrate MLeap with:
* PySpark
* Scikit-Learn
* gensim (optional, Word2Vec serialization)
* TensorFlow (coming soon)

Example:
```python
# Define your pipeline
feature_pipeline = [string_indexer, feature_assembler]

featurePipeline = Pipeline(stages=feature_pipeline)

# Fit your pipeline
fittedPipeline = featurePipeline.fit(df)

# Serialize your pipeline
fittedPipeline.serializeToBundle("jar:file:/tmp/pyspark.example.zip", fittedPipeline.transform(df))
```

Sections: Python integration package for MLeap, PySpark Integration, StringMap transformer, MathUnary transformer, Scikit-Learn Integration, gensim Integration, Documentation

</details>

### open-webui

Open WebUI

`pip install open-webui` · does not install on CPython 3.14 · licence: Other/Proprietary License · rank 4814 · last release 2026-11-03 · [PyPI](https://pypi.org/project/open-webui/)

<details><summary>README extract</summary>

Open WebUI is a home for AI: an extensible, easy-to-use, self-hosted platform built to run entirely offline. Connect local models through Ollama or use OpenAI-compatible APIs for local and cloud models. ...

Sections: Open WebUI, Python, Docker, Desktop App, Ecosystem, Troubleshooting and Updates, Documentation

</details>

### zulip

Bindings for the Zulip message API

`pip install zulip` · installs (wheel) · licence: Apache Software License · rank 5473 · last release 2025-09-30 · [PyPI](https://pypi.org/project/zulip/) · [docs](https://zulip.com/api) · [source](https://github.com/zulip/python-zulip-api/)

<details><summary>README extract</summary>

The Zulip API Python bindings require the
following dependencies:

* Python (version >= 3.9)
* requests (version >= 0.12.1)

Note: If you'd like to use the Zulip bindings with Python 2, we
recommend installing version 0.6.4.

Example:
```python
import zulip
import logging
stream = zulip.ZulipStream(type="stream", to=["support"], subject="your subject")
logger = logging.getLogger("your_logger")
logger.addHandler(logging.StreamHandler(stream))
logger.setLevel(logging.DEBUG)
logger.info("This is an INFO test.")
logger.debug("This is a DEBUG test.")
logger.warn("This is a WARN test.")
...
```

Sections: Dependencies, Using the API, Examples, Logging, Sending messages, Working with an untrusted server certificate

</details>

### chainlit

Build Conversational AI.

`pip install chainlit` · does not install on CPython 3.14 · licence: Apache-2.0 · rank 5587 · last release 2026-08-25 · [PyPI](https://pypi.org/project/chainlit/) · [docs](https://docs.chainlit.io/) · [source](https://github.com/Chainlit/chainlit)

<details><summary>README extract</summary>

Build python production-ready conversational AI applications in minutes, not weeks ⚡️

> ⚠️ Notice: Chainlit is now community-maintained.
> As of May 1st 2025, the original Chainlit team has stepped back from active development. The project is maintained by @Chainlit/chainlit-maintainers under a formal Maintainer Agreement. ...

Example:
```python
import chainlit as cl

@cl.step(type="tool")
async def tool():
    # Fake tool
    await cl.sleep(2)
    return "Response from the tool!"

@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
...
```

Sections: Welcome to Chainlit 👋, 🚀 Quickstart, 🐍 Pure Python, 📚 More Examples - Cookbook

</details>

### matrix-client

Client-Server SDK for Matrix

`pip install matrix-client` · installs (wheel) · licence: Apache Software License · rank 6180 · last release 2021-07-26 · [PyPI](https://pypi.org/project/matrix-client/)

<details><summary>README extract</summary>

Matrix client-server SDK for Python 2.7 and 3.4+

Example:
```python
from matrix_client.client import MatrixClient

client = MatrixClient("

# New user
token = client.register_with_password(username="foobar", password="monkey")

# Existing user
token = client.login(username="foobar", password="monkey")

room = client.create_room("my_room_alias")
room.send_text("Hello!")
```

Sections: Matrix Client SDK for Python, Usage, Structure, API, Client, Samples, Building the Documentation

</details>

### slackify-markdown

Convert markdown to Slack-compatible formatting

`pip install slackify-markdown` · installs (wheel) · licence: MIT License · rank 6871 · last release 2026-05-25 · [PyPI](https://pypi.org/project/slackify-markdown/) · [docs](https://github.com/thesmallstar/slackify-markdown-python#readme)

<details><summary>README extract</summary>

A Python library for converting Markdown to slack specific markdown. This is inspired from existing npm package slackify-markdown

Features:
This library converts regular Markdown to Slack-specific markdown, making it easy to use and display correctly in Slack messages.

Example:
```python
from slackify_markdown import slackify_markdown

markdown = """
# Title

This is bold text and this is *italic text*.

# Subtitle
1. Item 1
2. *Item 2*

# Another Subtitle
* Element 1 - *Description 1*
* Element 2 - *Description 2*

Link

"""

slack_output = slackify_markdown(markdown)
"""
*Title*

This is *bold text* and this is _italic text.

...
```

Sections: Slackify Markdown, Overview, Usage, Features, Example Conversions

</details>

### workspace-mcp

Comprehensive, highly performant Google Workspace Streamable HTTP & SSE MCP Server for Calendar, Gmail, Docs, Sheets, Slides & Drive

`pip install workspace-mcp` · installs (wheel) · licence: MIT · rank 7390 · last release 2026-10-30 · [PyPI](https://pypi.org/project/workspace-mcp/) · [docs](https://github.com/taylorwilsdon/google_workspace_mcp#readme) · [source](https://github.com/taylorwilsdon/google_workspace_mcp)

<details><summary>README extract</summary>

*Full natural language control over Google Calendar, Drive, Gmail, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through all MCP clients, AI assistants and developer tools.*
*Includes a full featured CLI & Code Mode for use with tools like Claude Code and Codex!* ...

Features:
Workspace MCP connects AI assistants to all twelve major Google Workspace services - 120+ tools behind a single MCP server, with OAuth 2.1 multi-user auth, three progressive tool tiers, read-only mode, a full CLI, and stateless container deployment. ...

Sections: Google Workspace MCP Server, What It Does, Services, 📧, 📁, 📅, 📝, 📊, 🖼️, 📋, ✅, 👤, 💬, 🔍

</details>

### mautrix

A Python 3 asyncio Matrix framework.

`pip install mautrix` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 7856 · last release 2026-07-05 · [PyPI](https://pypi.org/project/mautrix/)

<details><summary>README extract</summary>

A Python 3.10+ asyncio Matrix framework.

Matrix room: #maunium:maunium.net

* Basic HTTP request sender (mautrix.api)

* Client API endpoints as functions (mautrix.client.api)

* Medium-level application service framework (mautrix.appservice) ...

Sections: mautrix-python, Components

</details>

### slackblocks

Python wrapper for the Slack Blocks API

`pip install slackblocks` · installs (wheel) · licence: BSD License; MIT License · rank 8086 · last release 2026-10-31 · [PyPI](https://pypi.org/project/slackblocks/) · [docs](https://nicklambourne.github.io/slackblocks/) · [source](https://github.com/nicklambourne/slackblocks)

<details><summary>README extract</summary>

> Build Slack messages in Python — without writing JSON by hand.

`slackblocks` is a typed, validating Python wrapper around the Slack Block Kit API. It exists because Block Kit JSON is verbose, easy to get subtly wrong, and unpleasant to maintain in source control.

This release conforms to the shared cross-language slackblocks specification.

Features:
- Concise — `SectionBlock("Hello, *world*!")` instead of a 10-line JSON object.
- Validated — character limits, required fields, mutually-exclusive options, and element-type restrictions are enforced at construction time, so you find out *before* ...

Example:
```python
from slackblocks import (
    ActionsBlock,
    Button,
    DividerBlock,
    HeaderBlock,
    Message,
    SectionBlock,
)

message = Message(
    channel="#general",
...

</details>

### wecom-aibot-python-sdk

企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道，提供消息收发、流式回复、模板卡片、事件回调、文件下载解密等核心能力。

`pip install wecom-aibot-python-sdk` · installs (wheel) · licence: MIT · rank 8991 · last release 2026-03-23 · [PyPI](https://pypi.org/project/wecom-aibot-python-sdk/) · [source](https://github.com/WecomTeam/wecom-aibot-python-sdk)

<details><summary>README extract</summary>

企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道，提供消息收发、流式回复、模板卡片、事件回调、文件下载解密等核心能力。

> 本项目是 @wecom/aibot-node-sdk（Node.js 版）的 Python 等价实现。

- 🔗 WebSocket 长连接 — 基于 `wss://openws.work.weixin.qq.com` 内置默认地址，开箱即用
- 🔐 自动认证 — 连接建立后自动发送认证帧（bot_id + secret）
- 💓 心跳保活 — 自动维护心跳，连续未收到 ack 时自动判定连接异常
- 🔄 断线重连 — 指数退避重连策略（1s → 2s → 4s → ... → 30s 上限），支持自定义最大重连次数 ...

Example:
```python
import asyncio
import os
from dotenv import load_dotenv
from aibot import WSClient, WSClientOptions, generate_req_id

# 加载 .env 文件中的环境变量
load_dotenv()

# 1. 创建客户端实例
ws_client = WSClient(
    WSClientOptions(
        bot_id=os.getenv('WECHAT_BOT_ID'),       # 企业微信后台获取的机器人 ID
        secret=os.getenv('WECHAT_BOT_SECRET'),   # 企业微信后台获取的机器人 Secret
...
```

...

</details>

### pywa

🚀 Build WhatsApp Bots in Python • Fast, Effortless, Powerful

`pip install pywa` · installs (wheel) · licence: MIT · rank 9655 · last release 2026-09-24 · [PyPI](https://pypi.org/project/pywa/) · [docs](https://pywa.readthedocs.io/) · [source](https://github.com/david-lev/pywa)

<details><summary>README extract</summary>

The Python framework for building WhatsApp bots.

 Fast. Typed. Production-ready. From prototype to production in minutes.

PyWa is a comprehensive, fully-typed Python framework for
the WhatsApp Cloud API. ...

Example:
```python
# main.py
from pywa import WhatsApp, filters, types

wa = WhatsApp(
    phone_id="1234567890",
    token="EAA...",
    app_id=1234567890,
    app_secret="****",
    callback_url="
    verify_token="my-verify-token",
)

@wa.on_message(filters.text)
def echo(_: WhatsApp, msg: types.Message):
    msg.reply(f"You said: {msg.text}")
```

...

</details>

### h2o-wave

Python driver for H2O Wave Realtime Apps

`pip install h2o-wave` · installs (wheel) · licence: Apache-2.0 · rank 9837 · last release 2026-11-03 · [PyPI](https://pypi.org/project/h2o-wave/) · [docs](https://wave.h2o.ai/) · [source](https://github.com/h2oai/wave)

<details><summary>README extract</summary>

H2O Wave is a lightweight software stack for programming interactive web applications
entirely in Python (no HTML/Javascript/CSS required).

It is designed to make it fast, fun and easy to build low-latency, realtime,
collaborative, web-based applications. ...

Example:
```python
from h2o_wave import main, app, Q, ui

@app('/')
async def serve(q: Q):
    q.page['hello'] = ui.markdown_card(
        box='1 1 3 3',
        title='Hello world!',
        content='Welcome to Wave!'
    )
    await q.page.save()
```

Sections: H2O Wave, Hello world, Links

</details>

### dhooks-lite

A wrapper for sending messages to Discord webhooks.

`pip install dhooks-lite` · installs (wheel) · licence: not stated · rank 10936 · last release 2026-07-25 · [PyPI](https://pypi.org/project/dhooks-lite/) · [docs](https://dhooks-lite.readthedocs.io)

<details><summary>README extract</summary>

Another simple class wrapper for interacting with Discord webhooks.

Features:
dhooks-lite is a library with a set of classes for interacting with Discord webhooks written in Python 3.

This library aims to differentiate itself from similar libraries with the following properties:

- is fully tested ...

Example:
```python
import datetime
from dhooks_lite import Webhook, Embed, Footer, Image, Thumbnail, Author, Field

hook = Webhook(DISCORD_WEBHOOK_URL)
e1 = Embed(
    description='Only a few years ago, scientists stumbled upon an electrical current of cosmic proportions.(...)',
    title='Universe\'s highest electric current found',
    url='
...
```

...

</details>

### matrix-synapse

Homeserver for the Matrix decentralised comms protocol

`pip install matrix-synapse` · installs (wheel) · licence: AGPL-3.0-or-later OR LicenseRef-Element-Commercial · rank 11443 · last release 2026-11-02 · [PyPI](https://pypi.org/project/matrix-synapse/) · [docs](https://element-hq.github.io/synapse/latest) · [source](https://github.com/element-hq/synapse)

_README extract left out: share-alike licence._

### python-twitter

A Python wrapper around the Twitter API

`pip install python-twitter` · installs (wheel) · licence: Apache Software License · rank 11494 · last release 2018-11-03 · [PyPI](https://pypi.org/project/python-twitter/)

<details><summary>README extract</summary>

Python Twitter

A Python wrapper around the Twitter API.

By the Python-Twitter Developers

This library provides a pure Python interface for the Twitter API. It works with Python versions from 2.7+ and Python 3.

Twitter provides a service that allows people to connect via the web, IM, and SMS. ...

Example:
```python
>>> import twitter
>>> api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
```

Sections: Introduction, Getting the code, Running Tests, Documentation, Using, Models, API, Todo, More Information

</details>

### pypresence

Discord RPC client written in Python

`pip install pypresence` · installs (wheel) · licence: MIT · rank 11643 · last release 2026-07-08 · [PyPI](https://pypi.org/project/pypresence/) · [source](https://github.com/qwertyquerty/pypresence)

<details><summary>README extract</summary>

> A Discord Rich Presence Client in Python? Looks like you've come to the right place.

Sections: Documentation, Discord Server, Patreon, Documentation, pypresence Documentation, Discord Rich Presence Documentation, Discord RPC Documentation, Examples

</details>

### wecom-aibot-sdk

企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道

`pip install wecom-aibot-sdk` · installs (wheel) · licence: MIT · rank 12448 · last release 2026-06-02 · [PyPI](https://pypi.org/project/wecom-aibot-sdk/) · [source](https://github.com/xiaowangzhixiao/wecom-aibot-python-sdk)

<details><summary>README extract</summary>

企业微信智能机器人 Python SDK —— 基于 WebSocket 长连接通道，提供消息收发、流式回复、模板卡片、事件回调、文件下载解密等核心能力。

> 本项目为 @wecom/aibot-node-sdk 的 Python 版本，API 和使用方式保持一致。

- WebSocket 长连接 — 基于 `wss://openws.work.weixin.qq.com` 内置默认地址，开箱即用
- 自动认证 — 连接建立后自动发送认证帧（botId + secret）
- 心跳保活 — 自动维护心跳，连续未收到 ack 时自动判定连接异常
- 断线重连 — 指数退避重连策略（1s → 2s → 4s → ... → 30s 上限），支持自定义最大重连次数 ...

Example:
```python
import asyncio
from wecom_aibot_sdk import WSClient, generate_req_id

async def main():
    # 1. 创建客户端实例
    ws_client = WSClient(
        bot_id="your-bot-id",       # 企业微信后台获取的机器人 ID
        secret="your-bot-secret",   # 企业微信后台获取的机器人 Secret
    )

    # 2. 监听认证成功
    ws_client.on("authenticated", lambda: print("认证成功"))

    # 3. 监听文本消息并进行流式回复
...
```

...

</details>

### twython

Actively maintained, pure Python wrapper for the Twitter API. Supports both normal and streaming Twitter APIs

`pip install twython` · installs (wheel) · licence: MIT License · rank 12893 · last release 2021-07-16 · [PyPI](https://pypi.org/project/twython/)

<details><summary>README extract</summary>

`Twython` is a Python library providing an easy way to access Twitter data. Supports Python 3. It's been battle tested by companies, educational institutions and individuals alike. Try it today!

Note: As of Twython 3.7.0, there's a general call for maintainers put out. ...

Features:
- User information
 - Twitter lists
 - Timelines
 - Direct Messages
 - and anything found in the docs

 - Update user status with an image
 - Change user avatar
 - Change user background image
 - Change user banner image ...

Example:
```python
from twython import Twython
```

...

</details>

### TikTokLive

Unofficial TikTok LIVE API for Python: real-time chat, gift, like, follow and viewer events from any TikTok livestream.

`pip install TikTokLive` · installs (wheel) · licence: Other/Proprietary License · rank 13457 · last release 2026-09-10 · [PyPI](https://pypi.org/project/TikTokLive/) · [docs](https://isaackogan.github.io/TikTokLive/) · [source](https://github.com/isaackogan/TikTokLive)

<details><summary>README extract</summary>

TikTok LIVE API (TikTokLive) is the #1 TikTok LIVE client for Python. Connect to any TikTok LIVE stream and receive real-time chat messages, gifts, likes, follows, shares, viewer counts, battles, and more using just a creator's `@unique_id`. No login, no credentials or app are required. ...

Example:
```python
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@isaackogz")

# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
...
```

...

</details>

### slack-blocks-markdown

Convert Markdown to Slack Block Kit blocks using mistletoe

`pip install slack-blocks-markdown` · installs (wheel) · licence: not stated · rank 14218 · last release 2025-12-15 · [PyPI](https://pypi.org/project/slack-blocks-markdown/) · [docs](https://github.com/atacan/slack-blocks-markdown/blob/main/README.md) · [source](https://github.com/atacan/slack-blocks-markdown)

<details><summary>README extract</summary>

Convert Markdown to Slack Block Kit blocks using Python. This library provides a clean, efficient way to transform your Markdown content into Slack's interactive Block Kit format.

Features:
- 🚀 Complete Markdown Support: Headers, paragraphs, lists, code blocks, quotes, tables, links, and inline formatting
- 📱 Slack Block Kit Compatible: All blocks follow official Slack specifications with proper constraints ...

Example:
```python
from slack_blocks_markdown import markdown_to_blocks

# Convert markdown to Slack blocks (returns list of dictionaries)
markdown = """# Project Update

This is a bold announcement about our new features:

- ✅ User authentication
- ✅ Real-time updates
- 🚧 Mobile app (coming soon)

> Note: This is still in beta, so please report any issues!
"""

...
```

...

</details>

### emoji-country-flag

En/Decode unicode country flags emoji

`pip install emoji-country-flag` · installs (wheel) · licence: MIT License · rank 14696 · last release 2025-09-21 · [PyPI](https://pypi.org/project/emoji-country-flag/) · [docs](https://flag.readthedocs.io/) · [source](https://github.com/cvzi/flag)

<details><summary>README extract</summary>

Flag emoji for Python.
Converts flag emoji to ASCII and other way round.

This is based on by schinckel

How it works

All the flag emoji are actually composed of two unicode letters. These are the 26 regional indicator symbols.

Alone they look like this:
🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 ...

Example:
```python
>>> import flag

>>> flag.flag("IL")
'🇮🇱'

>>> flag.flag("GBENG")
'🏴󠁧󠁢󠁥󠁮󠁧󠁿'

>>> flag.flagize("Flag of Israel :IL:")
'Flag of Israel 🇮🇱'

>>> flag.dflagize("Flag of Israel 🇮🇱")
'Flag of Israel :IL:'

>>> flag.flagize("England :gb-eng: is part of the UK :GB:", subregions=True)
'England 🏴󠁧󠁢󠁥󠁮󠁧󠁿 is part of the UK 🇬🇧'

...
```

</details>

## Also in this topic

- [TgCrypto](communications.md#tgcrypto) - Fast and Portable Cryptography Extension Library for Pyrogram
- [Pyrogram](communications.md#pyrogram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
- [webexteamssdk](communications.md#webexteamssdk) - Community-developed Python SDK for the Webex Teams APIs
- [webexpythonsdk](communications.md#webexpythonsdk) - Work with the Webex APIs in native Python!
- [Hydrogram](communications.md#hydrogram) - Sleek, advanced, and asynchronous Telegram MTProto API framework in Python, designed for fluid user and bot interactions.
- [Kurigram](communications.md#kurigram) - Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots
