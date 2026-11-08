# Internet / XMPP

[Index](README.md) · 1 packages in this topic, by downloads.

### slixmpp

Slixmpp is an elegant Python library for XMPP (aka Jabber).

`pip install slixmpp` · installs (wheel) · licence: MIT · rank 9417 · last release 2026-07-08 · [PyPI](https://pypi.org/project/slixmpp/)

<details><summary>README extract</summary>

Slixmpp is an MIT licensed XMPP library for Python 3.11+. It is a fork of
SleekXMPP.

Slixmpp's goals is to only rewrite the core of the library (the low level
socket handling, the timers, the events dispatching) in order to remove all
threads.

Slixmpp uses rust to improve performance on critical modules. ...

Example:
```python
import asyncio
import logging

from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout

class EchoBot(ClientXMPP):

    def init(self, jid, password):
        ClientXMPP.init(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

...
```

Sections: Slixmpp, Building, The Slixmpp Boilerplate

</details>

