# Desktop Environment / Gnome

[Index](README.md) · 1 packages in this topic, 1 more listed under another topic, by downloads.

### dbus-next

A zero-dependency DBus library for Python with asyncio support

`pip install dbus-next` · installs (wheel) · licence: MIT License · rank 5952 · last release 2021-07-25 · [PyPI](https://pypi.org/project/dbus-next/)

<details><summary>README extract</summary>

The next great DBus library for Python.

Documentation

Chat

python-dbus-next is a Python library for DBus that aims to be a fully featured high level library primarily geared towards integration of applications into Linux desktop and mobile environments. ...

Example:
```python
from dbus_next.aio import MessageBus

import asyncio

loop = asyncio.get_event_loop()

async def main():
    bus = await MessageBus().connect()
    # the introspection xml would normally be included in your project, but
    # this is convenient for development
...
```

Sections: python-dbus-next, The Client Interface, The Service Interface, The Low-Level Interface, Projects that use python-dbus-next, Copyright

</details>

## Also in this topic

- [desktop-notifier](communications.md#desktop-notifier) - Python library for cross-platform desktop notifications
