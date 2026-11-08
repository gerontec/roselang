# Internet / Proxy Servers

[Index](README.md) · 8 packages in this topic, 6 more listed under another topic, by downloads.

### socksio

Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5.

`pip install socksio` · installs (wheel) · licence: MIT License · rank 731 · last release 2020-04-17 · [PyPI](https://pypi.org/project/socksio/)

<details><summary>README extract</summary>

Client-side sans-I/O SOCKS proxy implementation.
Supports SOCKS4, SOCKS4A, and SOCKS5.

`socksio` is a sans-I/O library similar to
`h11` or
`h2`, this means the library itself
does not handle the actual sending of the bytes through the network, it only
deals with the implementation details of the SOCKS protocols so you can use
it in any I/O ...

Example:
```python
import socket

sock = socket.create_connection(("localhost", 8080))
```

Sections: SOCKSIO, Usage, Reference documents

</details>

### mitmproxy

An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.

`pip install mitmproxy` · installs (wheel) · licence: MIT License · rank 1913 · last release 2026-10-25 · [PyPI](https://pypi.org/project/mitmproxy/) · [docs](https://docs.mitmproxy.org/stable/) · [source](https://github.com/mitmproxy/mitmproxy/)

<details><summary>README extract</summary>

``mitmproxy`` is an interactive, SSL/TLS-capable intercepting proxy with a console
interface for HTTP/1, HTTP/2, and WebSockets.

``mitmdump`` is the command-line version of mitmproxy. Think tcpdump for HTTP.

``mitmweb`` is a web-based interface for mitmproxy.

Sections: mitmproxy, Documentation & Help

</details>

### pyngrok

The complete ngrok agent for Python: programmatic tunnels for ingress, inspection, webhooks, demos, and APIs

`pip install pyngrok` · installs (wheel) · licence: MIT · rank 3846 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pyngrok/) · [docs](https://pyngrok.readthedocs.io) · [source](https://github.com/alexdlaird/pyngrok)

<details><summary>README extract</summary>

`pyngrok` gives Python the complete `ngrok` agent, with programmatic tunnels for
ingress, inspection, webhooks, demos, and APIs. `ngrok` is a reverse proxy that opens secure
tunnels from public URLs to localhost, and because `pyngrok` runs the real agent, you get everything it offers, from
traffic policies and OAuth to its web inspector and ...

Example:
```python
from pyngrok import ngrok

# Open a HTTP tunnel on the default port 80
# .ngrok.io" -> "
http_tunnel = ngrok.connect()

# Open a SSH tunnel
# "localhost:22">
ssh_tunnel = ngrok.connect("22", "tcp")

# Open a named tunnel from the config file
named_tunnel = ngrok.connect(name="my-config-file-tunnel")

...
```

Sections: Basic Usage, Open a Tunnel, `ngrok`'s API, Command Line Usage, Documentation, Integration Examples

</details>

### hass-nabucasa

Home Assistant cloud integration by Nabu Casa, Inc.

`pip install hass-nabucasa` · installs (wheel) · licence: GPL-3.0-only · rank 5204 · last release 2026-10-28 · [PyPI](https://pypi.org/project/hass-nabucasa/) · [source](https://github.com/NabuCasa/hass-nabucasa)

_README extract left out: share-alike licence._

### snitun

SNI proxy with TCP multiplexer

`pip install snitun` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 5269 · last release 2026-06-29 · [PyPI](https://pypi.org/project/snitun/) · [source](https://github.com/NabuCasa/snitun.git)

_README extract left out: share-alike licence._

### ray-haproxy

HAProxy binary distribution for Ray Serve

`pip install ray-haproxy` · installs (wheel) · licence: GPLv2 · rank 6757 · last release 2026-06-29 · [PyPI](https://pypi.org/project/ray-haproxy/)

_README extract left out: share-alike licence._

### django-revproxy

Yet another Django reverse proxy application

`pip install django-revproxy` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 6926 · last release 2024-11-06 · [PyPI](https://pypi.org/project/django-revproxy/) · [docs](https://django-revproxy.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

A simple reverse proxy using Django. It allows to use Django as a
reverse Proxy to HTTP requests. It also allows to use Django as an
authentication Proxy.

Documentation available at

Features:
* Proxies all HTTP methods: HEAD, GET, POST, PUT, DELETE, OPTIONS, TRACE, CONNECT and PATCH
* Copy all http headers sent from the client to the proxied server
* Copy all http headers sent from the proxied server to the client (except hop-by-hop)
* ...

Sections: Welcome to django-revproxy, Features, Dependencies

</details>

### websockets-proxy

Connect to websockets through a proxy server.

`pip install websockets-proxy` · installs (wheel) · licence: MIT License · rank 11957 · last release 2024-11-09 · [PyPI](https://pypi.org/project/websockets-proxy/)

<details><summary>README extract</summary>

This module will enable you to use websockets package with proxies.

Proxy heavy-lifting is done by python-socks package.

Example:
```python
from websockets_proxy import Proxy, proxy_connect

proxy = Proxy.from_url("...")
async with proxy_connect("wss://example.com", proxy=proxy) as ws:
    ...
```

Sections: websockets_proxy, Usage, WebSocket proxy checker, Server, Client

</details>

## Also in this topic

- [maxminddb](internet.md#maxminddb) - Reader for the MaxMind DB format
- [geoip2](internet.md#geoip2) - MaxMind GeoIP API
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [txtorcon](internet.md#txtorcon) - Twisted-based Tor controller client, with state-tracking and configuration abstractions. https://txtorcon.readthedocs.org https://github.com/meejah/txtorcon
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [minfraud](internet.md#minfraud) - MaxMind minFraud API
