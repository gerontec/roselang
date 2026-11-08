# Home Automation

[Index](README.md) · 23 packages in this topic, 3 more listed under another topic, by downloads.

### python-statemachine

Python Finite State Machines made easy.

`pip install python-statemachine` · installs (wheel) · licence: MIT License · rank 3106 · last release 2026-10-14 · [PyPI](https://pypi.org/project/python-statemachine/)

<details><summary>README extract</summary>

Expressive statecharts and FSMs for modern Python.

Welcome to python-statemachine, an intuitive and powerful state machine library designed for a
great developer experience. Define flat state machines or full statecharts with compound states,
parallel regions, and history — all with a clean, _pythonic_, declarative API that works in both
sync and ...

Example:
```python
>>> from statemachine import StateChart, State

>>> class TrafficLightMachine(StateChart):
...     "A traffic light machine"
...     green = State(initial=True)
...     yellow = State()
...     red = State()
...
...     cycle = (
...         green.to(yellow)
...         | yellow.to(red)
...         | red.to(green)
...     )
...
...
```

...

</details>

### homeassistant

Open-source home automation platform running on Python 3.

`pip install homeassistant` · installs (wheel) · licence: Apache-2.0 · rank 4231 · last release 2026-11-05 · [PyPI](https://pypi.org/project/homeassistant/) · [source](https://github.com/home-assistant/core)

<details><summary>README extract</summary>

Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.

Check out home-assistant.io for a
demo, installation instructions,
tutorials and documentation. ...

Sections: Home Assistant, Featured integrations

</details>

### hass-web-proxy-lib

A library to proxy web traffic through Home Assistant integrations.

`pip install hass-web-proxy-lib` · installs (wheel) · licence: MIT License · rank 6595 · last release 2026-05-05 · [PyPI](https://pypi.org/project/hass-web-proxy-lib/) · [source](https://github.com/dermotduffy/hass-web-proxy-lib)

<details><summary>README extract</summary>

A small Home Assistant library to proxy web
traffic through Home Assistant. Used by the Home Assistant Web Proxy
Integration and any
other integration that needs to proxy traffic through Home Assistant. ...

Example:
```python
@callback
async def async_setup_entry(hass: HomeAssistant) -> None:
    """Set up the HASS web proxy entry."""
    session = async_get_clientsession(hass)
    hass.http.register_view(MyProxyView(hass, session))

class MyProxyView(ProxyView):
    """A proxy view for My Integration."""

    url = "/api/my_integration/proxy/"
...
```

...

</details>

### ha-mcp

Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

`pip install ha-mcp` · installs (wheel) · licence: MIT · rank 6662 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ha-mcp/) · [source](https://github.com/homeassistant-ai/ha-mcp)

<details><summary>README extract</summary>

> Breaking change (v7.3.0): `ha_config_set_yaml` has been moved to beta.

 # HA-MCP — Manage Home Assistant with AI

 Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

The recommended way to run ha-mcp is the HA-MCP integration. ...

Sections: 🚀 Get Started, 🏠 Home Assistant app (add-on), 🧪 Demo server (Windows / macOS / Linux), 🧙 Setup Wizard for 15+ clients, 💬 What Can You Do With It?, ✨ Features, 🆚 ha-mcp vs. Home Assistant's built-in MCP Server, 🔌 Custom Component (ha_mcp_tools) — File & YAML Services, 🧠 Better Results with Agent Skills, Bundled Skills (built-in), 🔍 Tool Discovery for AI Agents, Smaller or local LLMs (Ollama, etc.), Enable search-based discovery, When to enable

</details>

### aiohomematic

Async Python library for Homematic(IP) devices via OpenCCU, CCU3, CUxD and CCU-Jack.

`pip install aiohomematic` · installs (wheel) · licence: MIT License · rank 7319 · last release 2026-11-07 · [PyPI](https://pypi.org/project/aiohomematic/) · [docs](https://sukramj.github.io/aiohomematic) · [source](https://github.com/sukramj/aiohomematic)

<details><summary>README extract</summary>

[][release]
[](LICENSE)
[][release]
[][sponsors]

A modern, async Python library for controlling and monitoring Homematic and HomematicIP devices. Powers the Home Assistant integration "Homematic(IP) Local". ...

Features:
- Automatic entity discovery from device/channel parameters
- Broad backend support: CCU3, OpenCCU, CUxD, CCU-Jack, and godevccu for testing ...

Example:
```python
import asyncio

from aiohomematic.central import CentralConfig
from aiohomematic.client import InterfaceConfig
from aiohomematic.const import Interface

async def main() -> None:
    config = CentralConfig(
        central_id="ccu-main",
        name="ccu-main",
        host="ccu.local",
        username="admin",
        password="secret",
...
```

...

</details>

### openccu-data

Extract and distribute Homematic CCU/OpenCCU configuration metadata (translations, easymodes, link profiles).

`pip install openccu-data` · installs (wheel) · licence: MIT License · rank 7803 · last release 2026-09-29 · [PyPI](https://pypi.org/project/openccu-data/) · [source](https://github.com/sukramj/openccu-data)

<details><summary>README extract</summary>

Extract and distribute Homematic CCU configuration metadata
(translations, easymodes, link profiles, device images) from
OpenCCU-Base /
OpenCCU.

This repository is the single source of truth for the data artifacts that
are consumed by aiohomematic and
aiohomematic-config. Both
projects vendor the produced JSON archives at runtime. ...

Sections: openccu-data, What this provides, Repository layout, Usage, Console scripts, Environment variables, Vendoring into consumer projects

</details>

### esphome

ESPHome is a system to configure your microcontrollers by simple yet powerful configuration files and control them remotely through Home Automation systems.

`pip install esphome` · installs (wheel) · licence: MIT · rank 8018 · last release 2026-11-02 · [PyPI](https://pypi.org/project/esphome/) · [docs](https://esphome.io) · [source](https://github.com/esphome/esphome)

### ha-mcp-dev

Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

`pip install ha-mcp-dev` · installs (wheel) · licence: MIT · rank 9645 · last release 2026-11-08 · [PyPI](https://pypi.org/project/ha-mcp-dev/) · [source](https://github.com/homeassistant-ai/ha-mcp)

<details><summary>README extract</summary>

> Breaking change (v7.3.0): `ha_config_set_yaml` has been moved to beta.

 # HA-MCP — Manage Home Assistant with AI

 Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

The recommended way to run ha-mcp is the HA-MCP integration. ...

Sections: 🚀 Get Started, 🏠 Home Assistant app (add-on), 🧪 Demo server (Windows / macOS / Linux), 🧙 Setup Wizard for 15+ clients, 💬 What Can You Do With It?, ✨ Features, 🆚 ha-mcp vs. Home Assistant's built-in MCP Server, 🔌 Custom Component (ha_mcp_tools) — File & YAML Services, 🧠 Better Results with Agent Skills, Bundled Skills (built-in), 🔍 Tool Discovery for AI Agents, Smaller or local LLMs (Ollama, etc.), Enable search-based discovery, When to enable

</details>

### openccu-loom-client

Async Python REST + WebSocket client for the openccu-loom daemon

`pip install openccu-loom-client` · installs (wheel) · licence: MIT License · rank 9704 · last release 2026-11-07 · [PyPI](https://pypi.org/project/openccu-loom-client/)

<details><summary>README extract</summary>

Status: Beta — transport, event bus, domain store, the full daemon
REST surface (HA-relevant + admin/ops), and the `aiohomematic` compat
namespace are in place (see "Status of the wire contract" below).

Async Python REST + WebSocket client for the
openccu-loom daemon. ...

Example:
```python
from openccu_loom_client import BoxIngressConfig, LoomConfig, NoAuth, start_box_pairing

session = await start_box_pairing(host="openccu-lite.local", app="my-app", instance="nas")
show_to_user(session.code)          # the six digits
result = await session.wait()       # approved / rejected / expired
if result.state == "approved":
...
```

Sections: openccu-loom-client, Architecture, Connecting through an openccu-lite box

</details>

### aiohomematic-config

Presentation-layer library for Homematic device configuration UI.

`pip install aiohomematic-config` · installs (wheel) · licence: MIT License · rank 9900 · last release 2026-11-05 · [PyPI](https://pypi.org/project/aiohomematic-config/) · [source](https://github.com/sukramj/aiohomematic-config)

<details><summary>README extract</summary>

Presentation-layer library for Homematic device configuration UI.

Transforms Homematic device paramset descriptions into UI-optimized structures. No RPC knowledge, no CCU access -- operates purely on data structures from aiohomematic.

Example:
```python
from aiohomematic_config import FormSchemaGenerator

generator = FormSchemaGenerator(locale="en")
schema = generator.generate(
    descriptions=descriptions,
    current_values=current_values,
    channel_type="HEATING_CLIMATECONTROL_TRANSCEIVER",
)
# schema is a Pydantic model, JSON-serializable
print(schema.model_dump_json(indent=2))
```

Sections: aiohomematic-config, Quick Start, Key Components

</details>

### python-miio

Python library for interfacing with Xiaomi smart appliances

`pip install python-miio` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 10540 · last release 2022-07-18 · [PyPI](https://pypi.org/project/python-miio/) · [docs](https://python-miio.readthedocs.io) · [source](https://github.com/rytilahti/python-miio)

_README extract left out: share-alike licence._

### mci

MiLight-Control-Interface

`pip install mci` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 10602 · last release 2016-10-24 · [PyPI](https://pypi.org/project/mci/)

_README extract left out: share-alike licence._

### esphome-device-builder

ESPHome Device Builder

`pip install esphome-device-builder` · installs (wheel) · licence: Apache-2.0 · rank 11096 · last release 2026-11-06 · [PyPI](https://pypi.org/project/esphome-device-builder/) · [docs](https://esphome.io) · [source](https://github.com/esphome/device-builder)

<details><summary>README extract</summary>

> Status: stable. The dashboard reached its 1.0 release and ships
> as the default builder in the official ESPHome add-on (as of ESPHome
> 2026.6.0). Issues
> and feedback welcome — please check existing issues / the
> project board
> first, and join the Discord channel
> for live discussion. ...

Sections: ESPHome Device Builder Dashboard, Try it, Home Assistant add-on, ESPHome Desktop (macOS / Windows / Linux), Standalone (PyPI), Standard ESPHome container image, Username / password authentication, Behind a reverse proxy, Listening on a UNIX socket (`--socket`), Subpath mounts (X-Forwarded-Prefix), Send builds to another dashboard, Pairing in four steps

</details>

### esphome-device-builder-frontend

Prebuilt web frontend for the ESPHome Device Builder Dashboard

`pip install esphome-device-builder-frontend` · installs (wheel) · licence: Apache Software License · rank 11224 · last release 2026-11-08 · [PyPI](https://pypi.org/project/esphome-device-builder-frontend/) · [docs](https://esphome.io) · [source](https://github.com/esphome/device-builder-frontend)

<details><summary>README extract</summary>

A web-based dashboard for managing, configuring, and deploying ESPHome IoT device firmware. Built with Lit web components and TypeScript.

> This repository contains the frontend source only. The dashboard runs as part of the ESPHome Device Builder Dashboard, which ships a prebuilt copy of this frontend bundled in. ...

Example:
```python
src/
├── api/            # WebSocket/HTTP API client and types
├── components/     # Lit web components
│   ├── device/     # Device editor, navigator, component catalog
│   └── wizard/     # Device creation wizard steps
├── pages/          # Routed page components (dashboard, device, secrets)
├── context/        # Lit Context definitions
...
```

...

</details>

### anycubic-cloud-api

Async client for the Anycubic Cloud API and its MQTT stream

`pip install anycubic-cloud-api` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 11616 · last release 2026-10-16 · [PyPI](https://pypi.org/project/anycubic-cloud-api/)

_README extract left out: share-alike licence._

### pyemvue

Unofficial library for interacting with the Emporia Vue energy monitor.

`pip install pyemvue` · installs (wheel) · licence: MIT License · rank 12018 · last release 2025-06-05 · [PyPI](https://pypi.org/project/pyemvue/)

<details><summary>README extract</summary>

A Python Library for reading data from the Emporia Vue energy monitoring system.

The library can be invoked directly to pull back some basic info but requires your email and password to be added to a keys.json file, which is then replaced with the access tokens.

The backing API documentation can be accessed here

keys.json

Example:
```python
# !/usr/bin/python3

import pyemvue
from pyemvue.enums import Scale, Unit

def print_recursive(usage_dict, info, depth=0):
    for gid, device in usage_dict.items():
        for channelnum, channel in device.channels.items():
            name = channel.name
            if name == 'Main':
                name = info[gid].device_name
...
```

...

</details>

### soco

SoCo (Sonos Controller) is a simple library to control Sonos speakers.

`pip install soco` · installs (wheel) · licence: MIT · rank 12459 · last release 2026-11-06 · [PyPI](https://pypi.org/project/soco/)

<details><summary>README extract</summary>

SoCo (Sonos Controller) is a Python library that allows you to
control Sonos speakers programmatically. It was originally created at Music
Hack Day Sydney by Rahim Sonawalla and is now developed by a team of
people at its GitHub repository.

For more background on the project, please see Rahim's blog post. ...

Features:
SoCo supports the following controls amongst others:

- Play, Pause, Stop
- Next track, Previous track
- Volume get and set
- Mute (or unmute)
- Get current transport information (if speaker is
 playing, paused or stopped) ...

Example:
```python
>>> from soco import SoCo
>>> my_zone = SoCo('192.168.1.101')
>>> my_zone.player_name
Kitchen
>>> my_zone.status_light = True
>>> my_zone.volume = 6
```

...

</details>

### pyvesync

pyvesync is a library to manage Etekcity Devices, Cosori Air Fryers, and Levoit Air Purifiers run on the VeSync app.

`pip install pyvesync` · installs (wheel) · licence: MIT License · rank 12671 · last release 2026-11-08 · [PyPI](https://pypi.org/project/pyvesync/) · [docs](https://webdjoe.github.io/pyvesync/latest/)

<details><summary>README extract</summary>

pyvesync is a library to manage VeSync compatible smart home devices

Check out the new pyvesync documentation for usage and full API details.

Features:
Before filing an issue to request a new feature or device, please ensure that you will take the time to test the feature thoroughly. New features cannot be simply tested on Home Assistant. ...

Example:
```python
import asyncio
from pyvesync import VeSync

async def main():
    async with VeSync("user", "password") as manager:
        await manager.login()
        await manager.update()

        # Acts as a set of device instances
        device_container = manager.devices

        outlets = device_container.outlets  # List of outlet instances
...
```

...

</details>

### tapo

Unofficial Tapo API Client. Works with TP-Link Tapo smart devices. Tested with light bulbs (L430C, L430P, L510, L520, L530, L535, L610, L630), light strips (L900, L920, L930), plugs (P100, P105, P110, P110M, P115, P125, P125M, TP10), power strips (P300, P304M, P306, P316M), hubs (H100, H110, H200, H500), switches (S200B, S200D, S210), sensors (KE100, T100, T110, T300, T310, T315) and cameras (C120, C210, C220, C225, C325WB, C520WS, TC40, TC70).

`pip install tapo` · installs (wheel) · licence: MIT · rank 12768 · last release 2026-11-01 · [PyPI](https://pypi.org/project/tapo/) · [source](https://github.com/mihai-dinculescu/tapo)

<details><summary>README extract</summary>

[][license]
[][crates]
[][crates_documentation]
[][crates]
[][pypi]
[][pypi]
[][pypi]\
Unofficial Tapo API Client. Works with TP-Link Tapo smart devices. Tested with light bulbs (L430C, L430P, L510, L520, L530, L535, L610, L630), light strips (L900, L920, L930), plugs (P100, P105, P110, P110M, P115, P125, P125M, TP10), power strips (P300, P304M, ...

Example:
```python
client = ApiClient("<tapo-username>", "tapo-password")
device = await client.p110("<device ip address>")

await device.on()
```

Sections: Tapo, Rust Library, Usage, Examples, Python Library, MCP Server, Troubleshooting

</details>

### pyatv

A client library for Apple TV and AirPlay devices

`pip install pyatv` · installs (wheel) · licence: MIT · rank 13250 · last release 2026-06-19 · [PyPI](https://pypi.org/project/pyatv/) · [source](https://github.com/postlund/pyatv)

<details><summary>README extract</summary>

This is an asyncio python library for interacting with Apple TV and AirPlay devices. It mainly
targets Apple TVs (all generations, including tvOS 15 and later), but also supports audio streaming via AirPlay
to receivers like the HomePod, AirPort Express and third-party speakers. It can act as remote control to the Music
app/iTunes in macOS. ...

Sections: A client library for Apple TV and AirPlay devices, What can it do?, Great, but how do I use it?, I need to change something?, Shortcuts to the good stuff

</details>

### huawei-solar

A Python wrapper for the Huawei Inverter modbus TCP API

`pip install huawei-solar` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 13411 · last release 2026-08-11 · [PyPI](https://pypi.org/project/huawei-solar/) · [source](https://github.com/wlcrs/huawei-solar-lib)

_README extract left out: share-alike licence._

### xknx

An Asynchronous Library for the KNX protocol. Documentation: https://xknx.io/

`pip install xknx` · installs (wheel) · licence: MIT · rank 13955 · last release 2026-11-05 · [PyPI](https://pypi.org/project/xknx/) · [source](https://github.com/XKNX/xknx.git)

<details><summary>README extract</summary>

See documentation at:

We need your help for testing and improving XKNX. For questions, feature requests, bug reports either open an issue, join the XKNX chat on Discord or write an email.

Example:
```python
"""Example for switching a light on and off."""

import asyncio

from xknx import XKNX
from xknx.devices import Light

async def main():
    """Connect to KNX/IP bus, switch on light, wait 2 seconds and switch it off again."""
    async with XKNX() as xknx:
        light = Light(
            xknx,
            name="TestLight",
...
```

Sections: XKNX - An asynchronous KNX library written in Python, Documentation, Help, Home-Assistant, Example, Attributions

</details>

### RPi.GPIO

A module to control Raspberry Pi GPIO channels

`pip install RPi.GPIO` · installs from source (sdist only) · licence: MIT License · rank 14087 · last release 2022-02-06 · [PyPI](https://pypi.org/project/RPi.GPIO/)

<details><summary>README extract</summary>

This package provides a Python module to control the GPIO on a Raspberry Pi.

Note that this module is unsuitable for real-time or timing critical applications. This is because you
can not predict when Python will be busy garbage collecting. ...

Sections: 0.7.1, 0.7.0, 0.6.5, 0.6.4, 0.6.3, 0.6.2, 0.6.1, 0.6.0a3, 0.5.11, 0.5.10, 0.5.9, 0.5.8, 0.5.7, 0.5.6

</details>

## Also in this topic

- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [btsocket](education.md#btsocket) - Python library for BlueZ Bluetooth Management API
- [minimalmodbus](communications.md#minimalmodbus) - Easy-to-use Modbus RTU and Modbus ASCII implementation for Python
