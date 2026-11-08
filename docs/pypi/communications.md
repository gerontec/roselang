# Communications

[Index](README.md) · 70 packages in this topic, 1 more listed under another topic, by downloads.

### pyasn1

Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

`pip install pyasn1` · installs (wheel) · licence: BSD-2-Clause · rank 70 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pyasn1/) · [docs](https://pyasn1.readthedocs.io) · [source](https://github.com/pyasn1/pyasn1)

<details><summary>README extract</summary>

ASN.1 library for Python

This is a free and open source implementation of ASN.1 types and codecs
as a Python package. It has been first written to support particular
protocol (SNMP) but then generalized to be suitable for a wide range
of protocols based on
ASN.1 specification. ...

Example:
```python
class Record(Sequence):
    componentType = NamedTypes(
        NamedType('id', Integer()),
        OptionalNamedType(
            'room', Integer().subtype(
                implicitTag=Tag(tagClassContext, tagFormatSimple, 0)
            )
        ),
        DefaultedNamedType(
            'house', Integer(0).subtype(
...
```

</details>

### pyasn1-modules

A collection of ASN.1-based protocols modules

`pip install pyasn1-modules` · installs (wheel) · licence: BSD License · rank 84 · last release 2025-03-28 · [PyPI](https://pypi.org/project/pyasn1-modules/) · [source](https://github.com/pyasn1/pyasn1-modules)

<details><summary>README extract</summary>

ASN.1 modules for Python

The `pyasn1-modules` package contains a collection of
ASN.1
data structures expressed as Python classes based on pyasn1
data model.

If ASN.1 module you need is not present in this collection, try using
Asn1ate tool that compiles ASN.1 documents
into pyasn1 code. ...

</details>

### kombu

Messaging library for Python.

`pip install kombu` · installs (wheel) · licence: BSD-3-Clause · rank 451 · last release 2026-11-03 · [PyPI](https://pypi.org/project/kombu/) · [source](https://github.com/celery/kombu)

<details><summary>README extract</summary>

:Version: 5.7.0
:Documentation:
:Download:
:Source:
:DeepWiki:
:Keywords: messaging, amqp, rabbitmq, redis, mongodb, python, queue

`Kombu` is a messaging library for Python.

The aim of `Kombu` is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQ protocol, and also
provide proven and tested ...

Features:
* Allows application authors to support several message server
 solutions by using pluggable transports.

 * AMQP transport using the py-amqp, or qpid-python libraries. ...

Example:
```python
from kombu import Connection, Exchange, Queue

media_exchange = Exchange('media', 'direct', durable=True)
video_queue = Queue('video', exchange=media_exchange, routing_key='video')

def process_media(body, message):
    print(body)
...

</details>

### humanfriendly

Human friendly output for text interfaces using Python

`pip install humanfriendly` · installs (wheel) · licence: MIT License · rank 463 · last release 2021-09-17 · [PyPI](https://pypi.org/project/humanfriendly/)

<details><summary>README extract</summary>

The functions and classes in the `humanfriendly` package can be used to make
text interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
 simple, human friendly formats. ...

Example:
```python
>>> from humanfriendly import format_size, parse_size
>>> from humanfriendly.prompts import prompt_for_input
>>> user_input = prompt_for_input("Enter a readable file size: ")

  Enter a readable file size: 16G

>>> num_bytes = parse_size(user_input)
>>> print(num_bytes)
16000000000
>>> print("You entered:", format_size(num_bytes))
...
```

Sections: humanfriendly: Human friendly input/output in Python, Getting started, Command line, A note about size units, Contact

</details>

### coloredlogs

Colored terminal output for Python's logging module

`pip install coloredlogs` · installs (wheel) · licence: MIT License · rank 541 · last release 2021-06-11 · [PyPI](https://pypi.org/project/coloredlogs/)

<details><summary>README extract</summary>

The `coloredlogs` package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal. It's currently tested
on Python 2.7, 3.5+ and PyPy (2 and 3). ...

Example:
```python
import coloredlogs, logging

# Create a logger object.
logger = logging.getLogger(name)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
coloredlogs.install(level='DEBUG')

...
```

...

</details>

### pyserial

Python Serial Port Extension

`pip install pyserial` · installs (wheel) · licence: BSD License · rank 987 · last release 2020-11-23 · [PyPI](https://pypi.org/project/pyserial/)

<details><summary>README extract</summary>

Python Serial Port Extension for Win32, OSX, Linux, BSD, Jython, IronPython

Stable:

Latest:

</details>

### pika

Pika Python AMQP Client Library

`pip install pika` · installs (wheel) · licence: BSD License · rank 1092 · last release 2026-08-06 · [PyPI](https://pypi.org/project/pika/) · [source](https://github.com/pika/pika)

<details><summary>README extract</summary>

Pika is a RabbitMQ (AMQP 0-9-1) client library for Python.

Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including
RabbitMQ's extensions.

- Supports Python 3.7+ (CPython and PyPy; versions are listed on
 PyPI). Pika 1.1.0 was the last release
 that supported Python 2.7. ...

Sections: Pika, Introduction, Documentation, Example, Pika provides the following adapters, Multiple connection parameters, Connection recovery

</details>

### aiosmtplib

asyncio SMTP client

`pip install aiosmtplib` · installs (wheel) · licence: MIT · rank 1111 · last release 2026-09-08 · [PyPI](https://pypi.org/project/aiosmtplib/) · [docs](https://aiosmtplib.readthedocs.io/en/stable/) · [source](https://github.com/cole/aiosmtplib)

<details><summary>README extract</summary>

|precommit.cicodecovzero-depspypi-versiondownloadspypi-license|

aiosmtplib is an asynchronous SMTP client for use with asyncio.

For documentation, see Read The Docs.

Example:
```python
import asyncio
from email.message import EmailMessage

import aiosmtplib

message = EmailMessage()
message["From"] = "root@localhost"
message["To"] = "somebody@example.com"
message["Subject"] = "Hello World!"
message.set_content("Sent via aiosmtplib")

asyncio.run(aiosmtplib.send(message, hostname="127.0.0.1", port=25))
```

Sections: aiosmtplib, Quickstart, Requirements, Bug Reporting

</details>

### paho-mqtt

MQTT version 5.0/3.1.1 client class

`pip install paho-mqtt` · installs (wheel) · licence: EPL-2.0 OR BSD-3-Clause · rank 1263 · last release 2026-11-04 · [PyPI](https://pypi.org/project/paho-mqtt/) · [docs](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html) · [source](https://github.com/eclipse-paho/paho.mqtt.python)

<details><summary>README extract</summary>

The full documentation is available here.

Warning breaking change - Release 2.0 contains a breaking change; see the release notes and migration details.

This document describes the source code for the Eclipse Paho MQTT Python client library, which implements versions 5.0, 3.1.1, and 3.1 of the MQTT protocol. ...

Example:
```python
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
...
```

...

</details>

### netaddr

A network address manipulation library for Python

`pip install netaddr` · installs (wheel) · licence: BSD License · rank 1284 · last release 2024-05-28 · [PyPI](https://pypi.org/project/netaddr/) · [docs](https://netaddr.readthedocs.io/en/latest/) · [source](https://github.com/netaddr/netaddr/)

<details><summary>README extract</summary>

A Python library for representing and manipulating network addresses.

Provides support for:

Layer 3 addresses

- IPv4 and IPv6 addresses, subnets, masks, prefixes
- iterating, slicing, sorting, summarizing and classifying IP networks
- dealing with various ranges formats (CIDR, arbitrary ranges and
 globs, nmap) ...

</details>

### autobahn

WebSocket client & server library, WAMP real-time framework

`pip install autobahn` · installs (wheel) · licence: MIT · rank 1310 · last release 2026-11-04 · [PyPI](https://pypi.org/project/autobahn/) · [source](https://github.com/crossbario/autobahn-python)

<details><summary>README extract</summary>

WebSocket & WAMP for Python on Twisted and asyncio.

Quick Links:
Source Code -
Documentation -
WebSocket Examples -
WAMP Examples
Community:
Forum -
StackOverflow -
Twitter -
IRC \#autobahn/chat.freenode.net
**Companion
Projects**:
Autobahn|JS -
Autobahn|Cpp -
Autobahn|Testsuite -
Crossbar.io -
WAMP ...

Features:
- framework for WebSocket
 and WAMP clients and servers
- runs on CPython and
 <span class="title-ref">PyPy &lt;
- runs under Twisted and
 asyncio -
 implements WebSocket
 RFC6455 and Draft
 Hybi-10+
- implements
 WebSocket compression ...

...

</details>

### crcmod

CRC Generator

`pip install crcmod` · installs from source (sdist only) · licence: MIT License · rank 1376 · last release 2010-07-20 · [PyPI](https://pypi.org/project/crcmod/)

<details><summary>README extract</summary>

The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC). There is no attempt in this package
to explain how the CRC works. There are a number of resources on the web that
give a good explanation of the algorithms. ...

Sections: crcmod for Calculating CRCs, Guidelines, Dependencies, Python Version, Building C extension, Code Generation

</details>

### pamqp

RabbitMQ Focused AMQP low-level library

`pip install pamqp` · installs (wheel) · licence: BSD-3-Clause · rank 1517 · last release 2026-10-30 · [PyPI](https://pypi.org/project/pamqp/) · [docs](https://gmr.github.io/pamqp/)

<details><summary>README extract</summary>

pamqp is a low level AMQP 0-9-1 frame encoding and decoding library for Python 3.11+.

pamqp is not an end-user client library for talking to RabbitMQ but rather is
used by client libraries for marshaling and unmarshaling AMQP frames.

gmr.github.io/pamqp

Features:
- AMQP 0-9-1 frame encoding and decoding
- Auto-generated command classes from the AMQP specification
- Support for all AMQP data types including field tables and arrays
- RabbitMQ extensions (Connection.Blocked, Connection.Unblocked, etc.) ...

Sections: pamqp, Documentation, Features, Used By

</details>

### django-celery-beat

Database-backed Periodic Tasks.

`pip install django-celery-beat` · installs (wheel) · licence: BSD License · rank 1550 · last release 2026-02-28 · [PyPI](https://pypi.org/project/django-celery-beat/)

<details><summary>README extract</summary>

:Version: 2.8.1
:Web:
:Download:
:Source:
:DeepWiki:
:Keywords: django, celery, beat, periodic task, cron, scheduling

This extension enables you to store the periodic task schedule in the
database.

The periodic tasks can be managed from the Django Admin interface, where you
can create, edit and delete periodic tasks and how often they should run.

Example:
```python
>>> from django_celery_beat.models import PeriodicTask, IntervalSchedule

# executes every 10 seconds.
>>> schedule, created = IntervalSchedule.objects.get_or_create(
...     every=10,
...     period=IntervalSchedule.SECONDS,
... )
```

...

</details>

### premailer

Turns CSS blocks into style attributes

`pip install premailer` · installs (wheel) · licence: Python Software Foundation License · rank 1792 · last release 2021-08-02 · [PyPI](https://pypi.org/project/premailer/)

<details><summary>README extract</summary>

Example:
```python
>>> from premailer import transform
>>> print(transform("""
...
...
...         h1 { border:1px solid black }
...         p { color:red;}
...         p::first-letter { float:left; }
...
...
...         h1 { color:blue; }
...
...
# Peter

...         Hej

...
... """))

    p::first-letter {float:left}

    h1 { color:blue; }

# Peter

    Hej
```

Sections: premailer, Python versions, Turns CSS blocks into style attributes, Getting started, Turning relative URLs into absolute URLs, Ignore certain `` or `, HTML attributes created additionally, Capturing logging from `cssutils`, If execution speed is on your mind, Advanced options, Choosing the cache implementation, Getting coding, Code style is all black

</details>

### crcmod-plus

CRC generator - modernized

`pip install crcmod-plus` · installs (wheel) · licence: MIT · rank 1866 · last release 2026-09-30 · [PyPI](https://pypi.org/project/crcmod-plus/) · [docs](https://github.com/ntamas/crcmod-plus#readme) · [source](https://github.com/ntamas/crcmod-plus)

<details><summary>README extract</summary>

The software in this repository is a modernised version of the `crcmod` Python
package, originally written by Ray Buvel. I took the original source code of
`crcmod` 1.7, dropped support for Python 2, reformatted the source files with
`black`, ran it through `ruff`, and added a modern build pipeline around it
based on `setuptools`, `pytest`, `tox` ...

Sections: `crcmod` for calculating CRCs, Guidelines, Dependencies, Python version, Building C extension, Code generation

</details>

### django-celery-results

Celery result backends for Django.

`pip install django-celery-results` · installs (wheel) · licence: BSD License · rank 1977 · last release 2025-04-10 · [PyPI](https://pypi.org/project/django-celery-results/) · [docs](https://django-celery-results.readthedocs.io/en/latest/) · [source](https://github.com/celery/django-celery-results)

<details><summary>README extract</summary>

:Version: 2.6.0
:Web:
:Download:
:Source:
:Keywords: django, celery, database, results

This extension enables you to store Celery task results using the Django ORM.

It defines a single model (`django_celery_results.models.TaskResult`)
used to store task results, and you can query this database table like
any other Django model.

Sections: About, With pip, Issues with mysql, django-celery-results for enterprise

</details>

### kazoo

"Higher Level Zookeeper Client"

`pip install kazoo` · installs (wheel) · licence: Apache Software License · rank 2308 · last release 2026-03-21 · [PyPI](https://pypi.org/project/kazoo/) · [docs](https://kazoo.readthedocs.io) · [source](https://github.com/python-zk/kazoo)

<details><summary>README extract</summary>

`kazoo` implements a higher level API to Apache
ZooKeeper for Python clients.

See the full docs for more information.

License

`kazoo` is offered under the Apache License 2.0.

Authors ...

Features:
* bump deps for Python > 3.8 (43e6f068)
 * add Python 3.13 & 3.14 (b385289e)
 * be a little more verbose about ZK download URL (4ed8a304)

 * removing tiny remaining bits of Python2 hybridation (0751174)
 * add support for SNI (273bd56)

Sections: Kazoo, 2.11.0 (2026-03-21), Features, Bug Fixes, 2.10.0 (2024-01-28), Test, Doc, Chore, Refactor, 2.9.0 (2022-10-08)

</details>

### reedsolo

Pure-Python Reed Solomon encoder/decoder

`pip install reedsolo` · installs (wheel) · licence: MIT No Attribution License (MIT-0); The Unlicense (Unlicense) · rank 3112 · last release 2023-01-17 · [PyPI](https://pypi.org/project/reedsolo/)

<details><summary>README extract</summary>

A pythonic universal errors-and-erasures Reed-Solomon Codec to protect your data from errors and bitrot. It includes a pure python implementation and an optional speed-optimized Cython/C extension.

This is a burst-type implementation, so that it supports any Galois field higher than 2^3, but not binary streams. ...

Example:
```python
# Initialization
>>> from reedsolo import RSCodec, ReedSolomonError
>>> rsc = RSCodec(10)  # 10 ecc symbols

# Encoding
# just a list of numbers/symbols:
>>> rsc.encode([1,2,3,4])
b'\x01\x02\x03\x04,\x9d\x1c+=\xf8h\xfa\x98M'
# bytearrays are accepted and the output will be matched:
>>> rsc.encode(bytearray([1,2,3,4]))
...
```

...

</details>

### deep-translator

A flexible free and unlimited python tool to translate between different languages in a simple way using multiple translators

`pip install deep-translator` · installs (wheel) · licence: MIT License · rank 3308 · last release 2023-06-28 · [PyPI](https://pypi.org/project/deep-translator/) · [docs](https://deep-translator.readthedocs.io/en/latest/) · [source](https://github.com/nidhaloff/deep_translator)

<details><summary>README extract</summary>

A flexible FREE and UNLIMITED tool to translate between different languages in a simple way using multiple translators.

* Free software: MIT license



I needed to translate a text using python. It was hard to find a simple way to do it. ...

Features:
- It's the only python tool that integrates many translators
- Multi language support
- Support for ChatGpt (version >= 1.11.0)
- Supports batch translation
- High level of abstraction
- Automatic language detection
- Easy to use and extend ...

Example:
```python
from deep_translator import GoogleTranslator

# Use any translator you like, in this example GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
```

...

</details>

### pysnmp

A Python library for SNMP

`pip install pysnmp` · installs (wheel) · licence: not stated · rank 3745 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pysnmp/) · [source](https://github.com/lextudio/pysnmp)

<details><summary>README extract</summary>

This is a pure-Python, open source and free implementation of v1/v2c/v3
SNMP engine distributed under 2-clause
BSD license.

Features

* Complete SNMPv1/v2c and SNMPv3 support based on IETF RFC standards. ...

</details>

### exchangelib

Client for Microsoft Exchange Web Services (EWS)

`pip install exchangelib` · installs (wheel) · licence: BSD-2-Clause · rank 3844 · last release 2025-10-10 · [PyPI](https://pypi.org/project/exchangelib/) · [docs](https://ecederstrand.github.io/exchangelib/) · [source](https://github.com/ecederstrand/exchangelib.git)

<details><summary>README extract</summary>

This module is an ORM for your Exchange mailbox, providing Django-style access to all your data. It is a
platform-independent, well-performing, well-behaving, well-documented, well-tested and simple interface for
communicating with an on-premise Microsoft Exchange 2007-2016 server or Office365 using Exchange Web Services
(EWS). ...

Example:
```python
from exchangelib import Credentials, Account

credentials = Credentials("john@example.com", "topsecret")
account = Account("john@example.com", credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by("-datetime_received")[:100]:
    print(item.subject, item.sender, item.datetime_received)
```

Sections: Exchange Web Services client library, Teaser, Documentation

</details>

### IPy

Class and tools for handling of IPv4 and IPv6 addresses and networks

`pip install IPy` · installs (wheel) · licence: BSD License · rank 4126 · last release 2026-10-08 · [PyPI](https://pypi.org/project/IPy/)

<details><summary>README extract</summary>

IPy - class and tools for handling of IPv4 and IPv6 addresses and networks.

Website:

The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 addresses and networks. It was
greatly inspired by RIPE's Perl module NET::IP's interface but
doesn't share the implementation. ...

Example:
```python
>>> from IPy import IP
>>> ip = IP('127.0.0.0/30')
>>> for x in ip:
...  print(x)
...
127.0.0.0
127.0.0.1
127.0.0.2
127.0.0.3
>>> ip2 = IP('0x7f000000/30')
>>> ip == ip2
1
>>> ip.reverseNames()
['0.0.0.127.in-addr.arpa.', '1.0.0.127.in-addr.arpa.', '2.0.0.127.in-addr.arpa.', '3.0.0.127.in-addr.arpa.']
>>> ip.reverseName()
...
```

...

</details>

### emails

Modern python library for emails.

`pip install emails` · installs (wheel) · licence: Apache Software License · rank 4475 · last release 2026-09-28 · [PyPI](https://pypi.org/project/emails/)

<details><summary>README extract</summary>

Build, transform, and send emails in Python with a high-level API.

`python-emails` helps you compose HTML and plain-text messages, attach files,
embed inline images, render templates, apply HTML transformations, sign with
DKIM, and send through SMTP without hand-building MIME trees.

Features:
- A concise API over `email` and `smtplib`
- HTML and plain-text messages in one object
- File attachments and inline images
- CSS inlining, image embedding, and HTML cleanup
- Jinja2, Mako, and string template support
- DKIM signing ...

Example:
```python
import emails

message = emails.html(
    subject="Your receipt",
    html="Hello!
Your payment was received.
",
    mail_from=("Billing", "billing@example.com"),
)
message.attach(filename="receipt.pdf", data=open("receipt.pdf", "rb"))

...

</details>

### pysmi

A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.

`pip install pysmi` · installs (wheel) · licence: BSD-2-Clause · rank 4588 · last release 2026-04-26 · [PyPI](https://pypi.org/project/pysmi/) · [source](https://github.com/lextudio/pysmi)

<details><summary>README extract</summary>

PySMI is a pure-Python implementation of
SNMP SMI MIB parser.
This tool is designed to turn ASN.1 MIBs into various formats. As of this moment,
JSON and PySNMP modules can be generated
from ASN.1 MIBs.

Features:
* Understands SMIv1, SMIv2 and de-facto SMI dialects
* Turns MIBs into PySNMP classes and JSON documents
* Maintains an index of MIB objects over many MIB modules
* Automatically pulls ASN.1 MIBs from local directories, ZIP archives,
 and HTTP ...

Sections: SNMP MIB Compiler, Features, How to get PySMI

</details>

### pycapnp

A cython wrapping of the C++ Cap'n Proto library

`pip install pycapnp` · installs (wheel) · licence: BSD-2-Clause · rank 4820 · last release 2026-07-03 · [PyPI](https://pypi.org/project/pycapnp/)

<details><summary>README extract</summary>

Cap'n'proto Mailing List Documentation

* C++14 supported compiler
 - gcc 6.1+ (5+ may work)
 - clang 6 (3.4+ may work)
 - Visual Studio 2017+
* cmake (needed for bundled capnproto)
 - ninja (macOS + Linux)
 - Visual Studio 2017+
* capnproto-1.0 (>=0.8.0 will also work if linking to system libraries)
 - Not necessary if using bundled capnproto
* ...

Example:
```python
import os
import capnp

import addressbook_capnp

def writeAddressBook(file):
    addresses = addressbook_capnp.AddressBook.new_message()
    people = addresses.init('people', 2)

    alice = people[0]
    alice.id = 123
    alice.name = 'Alice'
    alice.email = 'alice@example.com'
    alicePhones = alice.init('phones', 1)
...
```

...

</details>

### hl7

Python library parsing HL7 v2.x messages

`pip install hl7` · installs (wheel) · licence: BSD License · rank 5087 · last release 2022-03-31 · [PyPI](https://pypi.org/project/hl7/) · [source](https://github.com/johnpaulett/python-hl7)

<details><summary>README extract</summary>

python-hl7 is a simple library for parsing messages of Health Level 7
(HL7) version 2.x into Python objects.

</details>

### pyserial-asyncio

Python Serial Port Extension - Asynchronous I/O support

`pip install pyserial-asyncio` · installs (wheel) · licence: BSD License · rank 5225 · last release 2021-09-30 · [PyPI](https://pypi.org/project/pyserial-asyncio/)

<details><summary>README extract</summary>

Async I/O extension package for the Python Serial Port Extension for OSX, Linux, BSD

</details>

### TgCrypto

Fast and Portable Cryptography Extension Library for Pyrogram

`pip install TgCrypto` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 5761 · last release 2022-11-11 · [PyPI](https://pypi.org/project/TgCrypto/) · [docs](https://docs.pyrogram.org) · [source](https://github.com/pyrogram/tgcrypto)

_README extract left out: share-alike licence._

### python-olm

python CFFI bindings for the olm cryptographic ratchet library

`pip install python-olm` · installs from source (sdist only) · licence: Apache Software License · rank 5879 · last release 2023-11-28 · [PyPI](https://pypi.org/project/python-olm/)

<details><summary>README extract</summary>

Python bindings for Olm.

The specification of the Olm cryptographic ratchet which is used for peer to
peer sessions of this library can be found here.

The specification of the Megolm cryptographic ratchet which is used for group
sessions of this library can be found here. ...

Example:
```python
>>> alice = Account()
>>> alice.identity_keys
{'curve25519': '2PytGagXercwHjzQETLcMa3JOsaU2qkPIESaqoi59zE',
 'ed25519': 'HHpOuFYdHwoa54GxSttz9YmaTmbuVU3js92UTUjYJgM'}
```

Sections: python-olm, Accounts, Account Creation, One Time keys, Pickling, Sessions, Session Creation, Encryption, Group Sessions, Group Session Creation, Group Encryption

</details>

### pysnmpcrypto

Strong cryptography support for PySNMP (SNMP library for Python)

`pip install pysnmpcrypto` · installs (wheel) · licence: BSD License · rank 6168 · last release 2024-09-09 · [PyPI](https://pypi.org/project/pysnmpcrypto/) · [source](https://github.com/lextudio/pysnmpcrypto)

<details><summary>README extract</summary>

Strong crypto support for PySNMP

The `pysnmpcrypto` package is an optional extension to SNMP library for
Python pysnmp 6.0+. The `pysnmpcrypto` library
provides stronger authentication and encryption features to the SNMP library
by way of invoking stronger crypto algorithms. ...

</details>

### Pyrogram

Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

`pip install Pyrogram` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6209 · last release 2023-04-30 · [PyPI](https://pypi.org/project/Pyrogram/) · [docs](https://docs.pyrogram.org) · [source](https://github.com/pyrogram/pyrogram)

_README extract left out: share-alike licence._

### feedgen

Feed Generator (ATOM, RSS, Podcasts)

`pip install feedgen` · installs from source (sdist only) · licence: BSD License; GNU Lesser General Public License v3 or later (LGPLv3+) · rank 6279 · last release 2023-12-25 · [PyPI](https://pypi.org/project/feedgen/)

_README extract left out: share-alike licence._

### webexteamssdk

Community-developed Python SDK for the Webex Teams APIs

`pip install webexteamssdk` · installs from source (sdist only) · licence: MIT License · rank 6289 · last release 2024-06-14 · [PyPI](https://pypi.org/project/webexteamssdk/)

<details><summary>README extract</summary>

*Work with the Webex APIs in native Python!*

webexteamssdk v1.7 will be the last 🤞 release of the `webexteamssdk` package. This will be the last release
supporting Python v2 and v3 compatibility; it is compatible Python v3 releases *up to Python v3.10*. ...

Features:
webexteamssdk does all of this for you:

* Transparently sources your Webex access token from your local environment

* Provides and uses default arguments and settings everywhere possible, so you don't have to think about things like API
 endpoint ...

Example:
```python
from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI()

# Find all rooms that have 'webexteamssdk Demo' in their title
all_rooms = api.rooms.list()
demo_rooms = [room for room in all_rooms if 'webexteamssdk Demo' in room.title]

...

</details>

### AMQPStorm

Thread-safe Python3 RabbitMQ Client & Management library.

`pip install AMQPStorm` · installs (wheel) · licence: MIT License · rank 6605 · last release 2026-08-04 · [PyPI](https://pypi.org/project/AMQPStorm/) · [docs](https://amqpstorm.readthedocs.io/) · [source](https://github.com/eandersson/amqpstorm)

<details><summary>README extract</summary>

Thread-safe Python 3 RabbitMQ Client & Management library.

Documentation available at

AMQPStorm is a library designed to be consistent, stable and thread-safe.

- 100% Test Coverage!
- Supports Python 3.11+.

Sections: AMQPStorm, Introduction

</details>

### django-celery-email

An async Django email backend using celery

`pip install django-celery-email` · installs (wheel) · licence: BSD License · rank 6708 · last release 2019-12-11 · [PyPI](https://pypi.org/project/django-celery-email/)

<details><summary>README extract</summary>

A Django email backend that uses a Celery queue for out-of-band sending
of the messages.

To enable `django-celery-email` for your project you need to add `djcelery_email` to
`INSTALLED_APPS`:
You must then set `django-celery-email` as your `EMAIL_BACKEND`:
By default `django-celery-email` will use Django's builtin `SMTP` email backend
for the ...

Example:
```python
from django.core import mail

emails = (
    ('Hey Man', "I'm The Dude! So that's what you call me.", 'dude@aol.com', ['mr@lebowski.com']),
    ('Dammit Walter', "Let's go bowlin'.", 'dude@aol.com', ['wsobchak@vfw.org']),
)
results = mail.send_mass_mail(emails)
```

...

</details>

### msg-parser

This module enables reading, parsing and converting Microsoft Outlook MSG E-Mail files.

`pip install msg-parser` · installs (wheel) · licence: BSD License · rank 6992 · last release 2019-12-14 · [PyPI](https://pypi.org/project/msg-parser/)

<details><summary>README extract</summary>

Python module for parsing outlook msg files.

* Free software: BSD license

Features:
* Parse MSG file.
* Convert MSG file to EML file.
* Output MSG file as JSON string.
* Handles nested MSG/EML attachments.
* Works 100% on Linux machines, do not require any windows libraries.

Sections: msg_parser, Features, Usage

</details>

### redfish

Redfish Python Library

`pip install redfish` · installs (wheel) · licence: BSD License · rank 6996 · last release 2026-10-23 · [PyPI](https://pypi.org/project/redfish/)

<details><summary>README extract</summary>

As of version 3.0.0, Python2 is no longer supported. If Python2 is required, `redfish for more details.

Example:
```python
import redfish
```

Sections: python-redfish-library, Description, Building from zip file source, Requirements, Usage, Import the relevant Python module, Create a Redfish object, Login to the service, Perform a GET operation, Perform a POST operation, Notes about HTTP methods and arguments, Asynchronous client, Working with tasks, Logout the created session

</details>

### Mastodon.py

Python wrapper for the Mastodon API

`pip install Mastodon.py` · installs (wheel) · licence: MIT License · rank 7421 · last release 2026-10-18 · [PyPI](https://pypi.org/project/Mastodon.py/) · [docs](https://mastodonpy.readthedocs.io/) · [source](https://github.com/halcy/Mastodon.py)

<details><summary>README extract</summary>

Python wrapper for the Mastodon ( ) API.
Feature complete for public API as of Mastodon version 4.7.3 and easy to get started with:

You can install Mastodon.py via pypi:

We currently try to support Python 3.7 and above, and try to at least not break Python 3 versions
below that. Python 2 support is no longer a goal. ...

Example:
```python
from mastodon import Mastodon

# Register your app! This only needs to be done once (per server, or when
# distributing rather than hosting an application, most likely per device and server).
# Uncomment the code and substitute in your information:
'''
Mastodon.create_app(
    'pytooterapp',
    api_base_url = '
...
```

Sections: Mastodon.py, Citing

</details>

### webexpythonsdk

Work with the Webex APIs in native Python!

`pip install webexpythonsdk` · installs (wheel) · licence: MIT License · rank 7846 · last release 2026-04-14 · [PyPI](https://pypi.org/project/webexpythonsdk/) · [docs](https://webexcommunity.github.io/WebexPythonSDK) · [source](https://github.com/WebexCommunity/WebexPythonSDK)

<details><summary>README extract</summary>

*Work with the Webex APIs in native Python!*

Welcome to the new webexpythonsdk library! The latest release removes support for Python v2 and
is compatible with Python v3.10+. The new Webex Python SDK replaces the previous webexteamssdk;
and with the exception of the Python version support and the name change, the two libraries are
functionally ...

Features:
webexpythonsdk does all of this for you:

* Transparently sources your Webex access token from your local environment

* Provides and uses default arguments and settings everywhere possible, so you don't have to think
 about things like API endpoint ...

Example:
```python
from webexpythonsdk import WebexAPI

api = WebexAPI()

# Find all rooms that have 'webexpythonsdk Demo' in their title
all_rooms = api.rooms.list()
...

</details>

### pyfcm

Python client for FCM - Firebase Cloud Messaging (Android, iOS and Web)

`pip install pyfcm` · installs (wheel) · licence: MIT License · rank 8100 · last release 2026-08-18 · [PyPI](https://pypi.org/project/pyfcm/)

<details><summary>README extract</summary>

Python client for FCM - Firebase Cloud Messaging (Android, iOS and Web)

Firebase Cloud Messaging (FCM) is the new version of GCM. It inherits
the reliable and scalable GCM infrastructure, plus new features. GCM
users are strongly recommended to upgrade to FCM. ...

Features:
- All FCM functionality covered
- Tornado support

Example:
```python
# Send to single device.
from pyfcm import FCMNotification

fcm = FCMNotification(service_account_file="<service-account-json-path>", project_id="<project-id>")

# Google oauth2 credentials(such as ADC, impersonate credentials) can be used instead of service account file.

fcm = FCMNotification(
...
```

...

</details>

### t61codec

Python Codec for ITU T.61 Strings

`pip install t61codec` · installs (wheel) · licence: MIT · rank 8130 · last release 2026-10-22 · [PyPI](https://pypi.org/project/t61codec/) · [docs](https://t61codec.readthedocs.io) · [source](https://github.com/exhuma/t61codec)

<details><summary>README extract</summary>

A Python codec for ITU-T Rec. T.61 (11/1988), the 8-bit Teletex code,
implemented to the letter of the recommendation: accented letters are
composed from their diacritic prefix, only the combinations of Figure B-1
are accepted, and undefined bytes and control functions are errors.

For background see and

Example:
```python
import t61codec
t61codec.register()
```

Sections: Python Codec for ITU T.61 Strings, Upgrading from 2.x, Usage

</details>

### tlds

Automatically updated list of valid TLDs taken directly from IANA

`pip install tlds` · installs (wheel) · licence: MIT License · rank 8347 · last release 2026-10-30 · [PyPI](https://pypi.org/project/tlds/)

<details><summary>README extract</summary>

The `tlds` module provides a a set of valid TLDs directly taken from IANA. The package is automatically updated daily.

Available on PyPI.

Sections: Automatically updated list of valid TLDs for Python, Usage

</details>

### x690

Pure-Python ASN.1 BER encoder and decoder with typed values, light on memory for large documents

`pip install x690` · installs (wheel) · licence: MIT · rank 8419 · last release 2026-10-27 · [PyPI](https://pypi.org/project/x690/) · [docs](https://exhuma.github.io/x690/) · [source](https://github.com/exhuma/x690)

<details><summary>README extract</summary>

Encode and decode ASN.1 data in BER (ITU-T X.690) with pure Python. x690
turns every encoded value into a typed Python object, decodes documents of a
million values in a few megabytes of memory, and takes new types with a few
lines of code. It is the encoding layer of puresnmp.

Documentation:

Example:
```python
>>> from x690 import decode
>>> from x690.types import Integer, OctetString, Sequence
>>> data = bytes(Sequence([Integer(42), OctetString(b"hello")]))
>>> data
b'0\n\x02\x01*\x04\x05hello'
>>> decode(data)
(Sequence([Integer(42), OctetString(b'hello')]), 12)
```

Sections: x690, Example

</details>

### ws4py

WebSocket client and server library for Python 2 and 3 as well as PyPy

`pip install ws4py` · installs (wheel) · licence: BSD License · rank 8495 · last release 2024-12-19 · [PyPI](https://pypi.org/project/ws4py/)

<details><summary>README extract</summary>

WebSocket client and server library for Python 2 and 3 as well as PyPy

</details>

### pr-commenter

Create and manage automatic comments in a Github PR

`pip install pr-commenter` · installs (wheel) · licence: BSD License · rank 8607 · last release 2025-02-28 · [PyPI](https://pypi.org/project/pr-commenter/)

<details><summary>README extract</summary>

Create and manage automatic comments in a Github PR

`pr-commenter` is CLI app to add a comment a Github PR based on content from stdin, files or environment variables.

You can create a new comment, hide a previous one of the same type or update the "current" one from a different process. ...

Sections: pr-commenter, Basic usage, Advanced example, Failed tests

</details>

### ciscoconfparse

Parse, Audit, Query, Build, and Modify Cisco IOS-style and JunOS-style configs

`pip install ciscoconfparse` · installs (wheel) · licence: GNU General Public License (GPL); GNU General Public License v3 (GPLv3) · rank 8639 · last release 2024-11-22 · [PyPI](https://pypi.org/project/ciscoconfparse/) · [docs](http://www.pennington.net/py/ciscoconfparse/) · [source](https://github.com/mpenning/ciscoconfparse)

_README extract left out: share-alike licence._

### WSDiscovery

WS-Discovery implementation for python

`pip install WSDiscovery` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 9247 · last release 2025-01-24 · [PyPI](https://pypi.org/project/WSDiscovery/)

_README extract left out: share-alike licence._

### pysmi-lextudio

A pure-Python implementation of SNMP/SMI MIB parsing and conversion library.

`pip install pysmi-lextudio` · installs (wheel) · licence: BSD License · rank 9689 · last release 2024-04-03 · [PyPI](https://pypi.org/project/pysmi-lextudio/) · [source](https://github.com/lextudio/pysmi)

<details><summary>README extract</summary>

SNMP MIB Compiler

PySMI is a pure-Python implementation of
SNMP SMI MIB parser.
This tool is designed to turn ASN.1 MIBs into various formats. As of this moment,
JSON and PySNMP modules can be generated
from ASN.1 MIBs.

Features ...

</details>

### cobs

Consistent Overhead Byte Stuffing (COBS)

`pip install cobs` · installs from source (sdist only) · licence: MIT License · rank 9735 · last release 2026-03-09 · [PyPI](https://pypi.org/project/cobs/)

<details><summary>README extract</summary>

:Author: Craig McQueen
:Contact:
:Copyright: 2010 Craig McQueen

Python functions for encoding and decoding COBS.

The `cobs` package is provided, which contains modules containing functions
for encoding and decoding according to COBS methods. ...

Example:
```python
>>> from cobs import cobs
>>> encoded = cobs.encode(b'Hello world\x00This is a test')
>>> encoded
b'\x0cHello world\x0fThis is a test'
>>> cobs.decode(encoded)
b'Hello world\x00This is a test'
```

Sections: Consistent Overhead Byte Stuffing (COBS), Intro, What Is COBS?, References, Modules Provided, Usage, Documentation, Consistent Overhead Byte Stuffing--Reduced (COBS/R), Examples

</details>

### pysnmp-lextudio

A deprecated package. Please use 'pysnmp' instead.

`pip install pysnmp-lextudio` · installs (wheel) · licence: BSD License · rank 9750 · last release 2024-10-06 · [PyPI](https://pypi.org/project/pysnmp-lextudio/) · [source](https://github.com/lextudio/pysnmp)

<details><summary>README extract</summary>

⚠️ Deprecated: This package is no longer maintained.

LeXtudio Inc. has taken control of PySNMP PyPI packages, so please use pysnmp package instead.

Features:
The `7.x` releases of `new-package` introduce significant changes that may not be backward compatible with your current setup.

To upgrade, please follow the upgrade guide.

Sections: `pysnmp-lextudio` Package, Why Stick to `6.2.x` Versions?

</details>

### grafana-client

A client library for accessing the Grafana HTTP API, written in Python

`pip install grafana-client` · installs (wheel) · licence: MIT License · rank 9864 · last release 2026-10-20 · [PyPI](https://pypi.org/project/grafana-client/) · [source](https://github.com/grafana-toolbox/grafana-client)

<details><summary>README extract</summary>

<!-- -->

A client library for accessing the Grafana HTTP API, written in Python.

Install the package from PyPI.

Features:
| API | Status |

| Admin | + |
| Alerting | +- |
| Alerting Notification Channels | + |
| Alerting Provisioning | + |
| Annotations | + |
| Authentication | +- |
| Dashboard | + |
| Dashboard Versions | + |
| Dashboard Permissions | + |
| Data ...

Example:
```python
from grafana_client import GrafanaApi

# Connect to Grafana API endpoint using the `GrafanaApi` class
grafana = GrafanaApi.from_url("

# Create user
user = grafana.admin.create_user(
    {
        "name": "User",
        "email": "user@example.org",
        "login": "user",
        "password": "userpassword",
        "OrgId": 1,
    }
)

...
```

...

</details>

### pyais

AIS message decoding

`pip install pyais` · installs (wheel) · licence: MIT License · rank 9951 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyais/) · [source](https://github.com/M0r13n/pyais)

<details><summary>README extract</summary>

AIS message encoding and decoding. 100% pure Python.

Supports AIVDM/AIVDO messages. Supports single messages, files and
TCP/UDP sockets. This library has been used and tested extensively in representative real-world scenarios. This includes tests with live feeds from Spire, the Norwegian Coastal Administration and others. ...

Example:
```python
from pyais import decode

decoded = decode(b"!AIVDM,1,1,,B,15NG6V0P01G?cFhE`R2IU?wn28R>,0*05")
print(decoded)
```

Sections: pyais, General, Performance, Usage, TCP server, Live feed, AIS Monitor, Encode, Encode data using a dictionary, Create a message directly, CLI encoder, Under the hood, Tag block, How to work with tag blocks

</details>

### minimalmodbus

Easy-to-use Modbus RTU and Modbus ASCII implementation for Python

`pip install minimalmodbus` · installs (wheel) · licence: Apache Software License · rank 9989 · last release 2023-07-17 · [PyPI](https://pypi.org/project/minimalmodbus/) · [docs](https://minimalmodbus.readthedocs.io)

<details><summary>README extract</summary>

Easy-to-use Modbus RTU and Modbus ASCII implementation for Python.

Other web pages:

Obsolete web pages:

Features:
MinimalModbus is an easy-to-use Python module for talking to instruments (slaves)
from a computer (master) using the Modbus protocol, and is intended to be running on the master.
The only dependence is the pySerial module (also pure Python). ...

Sections: MinimalModbus, Web resources, Features

</details>

### pyserial-asyncio-fast

Python Serial Port Extension - Asynchronous I/O support

`pip install pyserial-asyncio-fast` · installs (wheel) · licence: BSD-3-Clause · rank 9994 · last release 2025-03-27 · [PyPI](https://pypi.org/project/pyserial-asyncio-fast/) · [docs](http://pyserial-asyncio.readthedocs.io) · [source](https://github.com/home-assistant-libs/pyserial-asyncio-fast)

<details><summary>README extract</summary>

Async I/O extension package for the Python Serial Port Extension for OSX, Linux, BSD

It depends on pySerial and is compatible with Python 3.9 and later.

This version implements eager writes like cpython `asyncio` selector_events does:

This can significantly reduce overhead since the asyncio writer is no longer added and removed frequently.

Sections: pyserial-asyncio-fast, Documentation

</details>

### signalwire

Client library for connecting to SignalWire.

`pip install signalwire` · installs (wheel) · licence: MIT License · rank 10321 · last release 2025-02-04 · [PyPI](https://pypi.org/project/signalwire/)

<details><summary>README extract</summary>

The Relay SDK for Python enables developers to connect and use SignalWire's Relay APIs within their own Python code. Our Relay SDK allows developers to build or add robust and innovative communication services to their applications.

Sections: SignalWire Python, Getting Started, Versioning

</details>

### oauth2-client

A client library for OAuth2

`pip install oauth2-client` · installs (wheel) · licence: not stated · rank 10566 · last release 2023-04-28 · [PyPI](https://pypi.org/project/oauth2-client/)

<details><summary>README extract</summary>

OAuth2Client is a simple python client library for OAuth2. It is based on the requests
 .. _requests:

:warning: Starting version `1.2.0`, versions older that python `3.6.0` will not be supported anymore. This late version was released by the end 2016. ...

Example:
```python
scopes = ['scope_1', 'scope_2']

service_information = ServiceInformation('
                                         '
                                         'client_id',
                                         'client_secret',
                                          scopes)
manager = CredentialManager(service_information,
...
```

Sections: OAuth2Client, Presentation, Login process, User credentials, Client credentials, Refresh token, Token expiration, Read other fields from token response

</details>

### tb-paho-mqtt-client

MQTT version 5.0/3.1.1 client class

`pip install tb-paho-mqtt-client` · installs (wheel) · licence: OSI Approved · rank 11618 · last release 2025-04-07 · [PyPI](https://pypi.org/project/tb-paho-mqtt-client/)

<details><summary>README extract</summary>

The full documentation is available here.

Warning breaking change - Release 2.0 contains a breaking change; see the release notes and migration details.

This document describes the source code for the Eclipse Paho MQTT Python client library, which implements versions 5.0, 3.1.1, and 3.1 of the MQTT protocol. ...

Example:
```python
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
...
```

...

</details>

### keeper-pam-webrtc-rs

Keeper PAM WebRTC for Python - A secure, stable, and high-performance Tube API for Python, providing WebRTC-based secure tunneling with enterprise-grade security and reliability optimizations.

`pip install keeper-pam-webrtc-rs` · installs (wheel) · licence: MIT · rank 11985 · last release 2026-11-06 · [PyPI](https://pypi.org/project/keeper-pam-webrtc-rs/)

<details><summary>README extract</summary>

Python bindings for the Keeper PAM WebRTC tunneling library.

Provides a secure WebRTC-based tunneling API for connecting to remote services. Supports three connection modes:

- tunnel — raw TCP tunneling
- guacd — Guacamole protocol (for RDP, SSH, VNC, etc. via a guacd server)
- socks5 — SOCKS5 proxy

Example:
```python
import keeper_pam_connections

keeper_pam_connections.initialize_logger("gateway", verbose=False, level=20)
# Debugging only: show_pwd=True also logs every guacd connect value (passwords, private keys, passphrases).
registry = keeper_pam_connections.PyTubeRegistry()
```

Sections: keeper-pam-connections, Usage, Requirements

</details>

### snmpsim

SNMP Simulator is a tool that acts as multitude of SNMP Agents built into real physical devices, from SNMP Manager's point of view. Simulator builds and uses a database of physical devices' SNMP footprints to respond like their original counterparts do.

`pip install snmpsim` · installs (wheel) · licence: BSD License · rank 12043 · last release 2026-04-26 · [PyPI](https://pypi.org/project/snmpsim/) · [source](https://github.com/lextudio/snmpsim)

<details><summary>README extract</summary>

This is a pure-Python, open source and free implementation of SNMP agents simulator
distributed under 2-clause BSD license.

Features:
* SNMPv1/v2c/v3 support
* SNMPv3 USM supports MD5/SHA/SHA224/SHA256/SHA384/SHA512 auth and
 DES/3DES/AES128/AES192/AES256 privacy crypto algorithms
* Runs over IPv4 and/or IPv6 transports
* Simulates many EngineID's, each with its own set of ...

Sections: SNMP Simulator, Features, Download, How to use SNMP simulator, Documentation, Getting help, Feedback and collaboration

</details>

### desktop-notifier

Python library for cross-platform desktop notifications

`pip install desktop-notifier` · installs (wheel) · licence: MIT · rank 12483 · last release 2025-08-08 · [PyPI](https://pypi.org/project/desktop-notifier/)

<details><summary>README extract</summary>

`desktop-notifier` is a Python library for cross-platform desktop notifications.
Currently supported platforms are:

* Linux via the dbus service org.freedesktop.Notifications
* macOS and iOS via the Notification Center framework
* Windows via the WinRT / Python bridge

Features:
Where supported by the native platform APIs, `desktop-notifier` allows for:

* Clickable notifications with callbacks on user interaction
* Multiple action buttons
* A single reply field (e.g., for chat notifications)
* Notification sounds
* ...

Example:
```python
import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Hello world!", message="Sent from Python")

asyncio.run(main())
```

...

</details>

### Hydrogram

Sleek, advanced, and asynchronous Telegram MTProto API framework in Python, designed for fluid user and bot interactions.

`pip install Hydrogram` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 12583 · last release 2024-06-30 · [PyPI](https://pypi.org/project/Hydrogram/) · [docs](https://docs.hydrogram.org) · [source](https://github.com/hydrogram/hydrogram)

_README extract left out: share-alike licence._

### createsend

A library which implements the complete functionality of the Campaign Monitor API.

`pip install createsend` · installs (wheel) · licence: DFSG approved; OSI Approved; MIT License · rank 12776 · last release 2026-10-30 · [PyPI](https://pypi.org/project/createsend/)

### amqtt

Python's asyncio-native MQTT broker and client.

`pip install amqtt` · installs (wheel) · licence: MIT · rank 13312 · last release 2026-09-16 · [PyPI](https://pypi.org/project/amqtt/)

<details><summary>README extract</summary>

`aMQTT` is an open source MQTT broker and client[^1], natively implemented with Python's asyncio.

Features:
- Full set of MQTT 3.1.1 protocol specifications
- Communication over multiple TCP and/or websocket ports, including support for SSL/TLS
- Support QoS 0, QoS 1 and QoS 2 messages flow
- Client auto-reconnection on network lost ...

Sections: Features, Documentation, Containerization, Python Version Compatibility

</details>

### lcm

Lightweight Communication and Marshalling

`pip install lcm` · installs (wheel) · licence: not stated · rank 13397 · last release 2026-09-24 · [PyPI](https://pypi.org/project/lcm/)

<details><summary>README extract</summary>

Lightweight Communications and Marshalling (LCM)

LCM is a set of libraries and tools for message passing and data marshalling,
targeted at real-time systems where high-bandwidth and low latency are
critical. ...

Features:
* Low-latency inter-process communication
* Efficient broadcast mechanism using UDP Multicast
* Type-safe message marshalling
* User-friendly logging and playback
* No centralized "database" or "hub" -- peers communicate directly
* No daemons
* Few ...

Sections: Roadmap, Quick Links, Features, Unmaintained languages

</details>

### Kurigram

Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

`pip install Kurigram` · installs (wheel) · licence: LGPL-3.0-or-later · rank 13504 · last release 2026-09-12 · [PyPI](https://pypi.org/project/Kurigram/) · [docs](https://docs.kurigram.icu) · [source](https://github.com/KurimuzonAkuma/pyrogram)

_README extract left out: share-alike licence._

### email-normalize

Return a normalized email-address stripping ISP specific behaviors

`pip install email-normalize` · installs (wheel) · licence: BSD License · rank 13775 · last release 2026-07-29 · [PyPI](https://pypi.org/project/email-normalize/)

<details><summary>README extract</summary>

A Python 3.11+ library for normalizing email addresses by stripping
mailbox-provider-specific behaviors such as plus addressing
(`foo+bar@gmail.com`) and period ignoring (`f.o.o@gmail.com`).

Example:
```python
import email_normalize

result = email_normalize.normalize('f.o.o+bar@gmail.com')
print(result.normalized_address)  # foo@gmail.com
print(result.mailbox_provider)    # Google
print(result.mx_records)          # [(5, 'gmail-smtp-in.l.google.com'), ...]
```

Sections: email-normalize, Usage, Synchronous, Async, Without DNS Lookups, Normalization Rules, Documentation

</details>

### rfc3161ng

Python implementation of the RFC3161 specification, using pyasn1

`pip install rfc3161ng` · installs (wheel) · licence: MIT License · rank 14431 · last release 2020-10-30 · [PyPI](https://pypi.org/project/rfc3161ng/)

<details><summary>README extract</summary>

A simple client library for cryptographic timestamping service implementing the
protocol from RFC3161.

This started as a fork of and
has some additional patches such as Python3 support.

The latest version of this library is available from

There are several timestamping services around. Here is a list of
publicly available services you can try:

Sections: rfc3161ng, Public providers, Example, Verifying timestamp using OpenSSL

</details>

### ft4222

Python wrapper around libFT4222.

`pip install ft4222` · installs (wheel) · licence: MIT AND LicenseRef-FTDI · rank 14500 · last release 2026-02-13 · [PyPI](https://pypi.org/project/ft4222/)

<details><summary>README extract</summary>

The FT4222H is a High/Full Speed USB2.0-to-Quad SPI/I2C device controller. This project
provides (incomplete) python binding to LibFT4222
(user guide).
It provides a similar api than LibFT4222 does.

The complete documentation can be found here

Example:
```python
import ft4222
import ft4222.I2CMaster

# list devices
nbDev = ft4222.createDeviceInfoList()
for i in range(nbDev):
    print(ft4222.getDeviceInfoDetail(i, False))

# open device with default description 'FT4222 A'
dev = ft4222.openByDescription('FT4222 A')

# init i2c master, clock speed 100kHz
dev.i2cMaster_Init(100)

...
```

Sections: python-ft4222, Example, I2C Master, GPIO, SPI Master and GPIO, Accessrights, Requirements, Windows

</details>

### cose

CBOR Object Signing and Encryption (COSE) implementation

`pip install cose` · installs (wheel) · licence: BSD License · rank 14797 · last release 2021-07-01 · [PyPI](https://pypi.org/project/cose/)

<details><summary>README extract</summary>

This project is a Python implementation of the IETF CBOR Encoded Message Syntax (COSE). COSE has reached RFC status and is now available at RFC 8152.

Example:
```python
from binascii import unhexlify
from cose.messages import Enc0Message
from cose.keys import SymmetricKey

# Create a COSE Encrypt0 Message
msg = Enc0Message(
    phdr={'ALG': 'A128GCM', 'IV': unhexlify(b'01010101010101010101010101010101')},
    uhdr={'KID': b'meriadoc.brandybuck@buckland.example'},
    payload='a secret message'.encode('utf-8')
)

...
```

Sections: pycose:snake: --- CBOR Object Signing and Encryption, What is COSE ?, Examples, Encoding, Decoding, More examples, Cryptography, Documentation

</details>

## Also in this topic

- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
