# Communications / Email

[Index](README.md) · 40 packages in this topic, 4 more listed under another topic, by downloads.

### Markdown

Python implementation of John Gruber's Markdown.

`pip install Markdown` · installs (wheel) · licence: BSD-3-Clause · rank 265 · last release 2026-11-05 · [PyPI](https://pypi.org/project/Markdown/) · [docs](https://Python-Markdown.github.io/) · [source](https://github.com/Python-Markdown/markdown)

<details><summary>README extract</summary>

[][build]
[][codecov]
[][md-pypi]
[][md-pypi]
[][bsdlicense]
[][Code of Conduct]

This is a Python implementation of John Gruber's Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues. See Features for information
on what exactly is supported and what is not. ...

Example:
```python
import markdown
html = markdown.markdown(your_text_string)
```

</details>

### RTFDE

A library for extracting HTML content from RTF encapsulated HTML as commonly found in the exchange MSG email format.

`pip install RTFDE` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 1325 · last release 2025-12-09 · [PyPI](https://pypi.org/project/RTFDE/)

_README extract left out: share-alike licence._

### python-oxmsg

Extract attachments from Outlook .msg files.

`pip install python-oxmsg` · installs (wheel) · licence: MIT License · rank 1660 · last release 2025-02-03 · [PyPI](https://pypi.org/project/python-oxmsg/) · [docs](https://scanny.github.io/python-oxmsg/) · [source](https://github.com/scanny/python-oxmsg)

<details><summary>README extract</summary>

Parse Outlook MSG (.msg) files to extract email messages and attachments.

The target use case is extracting Outlook message text and accessing attachments. There is no support for modifying messages or creating them from scratch. In addition to message text, other message properties such as sent-date, etc. are also accessible. ...

Example:
```python
>>> from oxmsg import Message
>>> msg = Message.load("message.msg")
>>> msg.message_class
'IPM.Note'
>>> msg.attachment_count
1
>>> attachment = msg.attachments[0]
>>> attachment.attached_by_value  # -- attachment bytes only available when True --
True
>>> attachment.file_name
'q1-objectives.pptx'
>>> attachment.mime_type
...
```

Sections: python-oxmsg, Documentation, Usage, CLI

</details>

### Wikipedia-API

Python Wrapper for Wikipedia

`pip install Wikipedia-API` · installs (wheel) · licence: MIT License · rank 1957 · last release 2026-09-04 · [PyPI](https://pypi.org/project/Wikipedia-API/) · [source](https://github.com/martin-majlis/Wikipedia-API)

<details><summary>README extract</summary>

`Wikipedia-API` is easy to use Python wrapper for Wikipedias' API. It supports extracting texts, sections, links, categories, translations, etc from Wikipedia. Documentation provides code snippets for the most common use cases.

Example:
```python
import wikipediaapi

# Synchronous client
wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName (merlin@example.com)', language='en')

# Asynchronous client
wiki = wikipediaapi.AsyncWikipedia(user_agent='MyProjectName (merlin@example.com)', language='en')
```

...

</details>

### django-anymail

Django email backends and webhooks for Amazon SES, Brevo, MailerSend, Mailgun, Mailjet, Mailtrap, Mandrill, Postal, Postmark, Resend, Scaleway TEM, SendGrid, SparkPost, and Unisender Go (EmailBackend, transactional email tracking and inbound email signals)

`pip install django-anymail` · installs (wheel) · licence: BSD-3-Clause · rank 2183 · last release 2026-09-05 · [PyPI](https://pypi.org/project/django-anymail/) · [docs](https://anymail.dev/en/stable/) · [source](https://github.com/anymail/django-anymail)

<details><summary>README extract</summary>

Anymail lets you send and receive email in Django using your choice
of transactional email service providers (ESPs). It extends the
standard `django.core.mail` with many common ESP-added features, providing
a consistent API that avoids locking your code to one specific ESP
(and making it easier to change ESPs later if needed). ...

Sections: Anymail: Django email integration for transactional ESPs, Anymail 1-2-3, Thanks

</details>

### aiosmtpd

aiosmtpd - asyncio based SMTP server

`pip install aiosmtpd` · installs (wheel) · licence: OSI Approved; Apache Software License · rank 2804 · last release 2024-05-18 · [PyPI](https://pypi.org/project/aiosmtpd/) · [docs](https://aiosmtpd.readthedocs.io/) · [source](https://github.com/aio-libs/aiosmtpd)

<details><summary>README extract</summary>

github licensePyPI VersionPyPI PythonPyPI PythonImpl|
GA badgeCodeQL badgecodecovreadthedocs|
GH ReleaseGH PRsGH LastCommit|
PyPI DLGH DL|
GH Discussions|

This is a server for SMTP and related MTA protocols,
similar in utility to the standard library's |smtpd.py|_ module,
but rewritten to be based on `asyncio`. ...

Sections: aiosmtpd - asyncio based SMTP server, Signing Keys

</details>

### dkimpy

DKIM (DomainKeys Identified Mail), ARC (Authenticated Receive Chain), and TLSRPT (TLS Report) email signing and verification

`pip install dkimpy` · installs from source (sdist only) · licence: DFSG approved · rank 3048 · last release 2024-07-04 · [PyPI](https://pypi.org/project/dkimpy/)

<details><summary>README extract</summary>

dkimpy - DKIM (DomainKeys Identified Mail)

Friendly fork of:

dkimpy is a library that implements DKIM (DomainKeys Identified Mail) email
signing and verification. Basic DKIM requirements are defined in RFC 6376:

This is dkimpy 1.1.8.

Example:
```python
>>> res = dkim.verify(smessage, tlsrpt='strict')
```

Sections: INTRODUCTION, VERSION, REQUIREMENTS, DKIM SCRIPTS, ARC (Authenticated Receive Chain), TLSRPT (TLS Report), LIMITATIONS, FEEDBACK

</details>

### IMAPClient

Easy-to-use, Pythonic and complete IMAP client library

`pip install IMAPClient` · installs (wheel) · licence: not stated · rank 3736 · last release 2026-09-18 · [PyPI](https://pypi.org/project/IMAPClient/)

<details><summary>README extract</summary>

IMAPClient is an easy-to-use, Pythonic and complete IMAP client
library.

========================= ========================================
Supported Python versions 3.8 - 3.14
License New BSD
Project home
PyPI
Documentation
Discussions
Test Status
========================= ========================================

Features:
- Arguments and return values are natural Python types.
- IMAP server responses are fully parsed and readily usable.
- IMAP unique message IDs (UIDs) are handled transparently. There is
 no need to call different methods to use UIDs. ...

Example:
```python
from imapclient import IMAPClient

# context manager ensures the session is cleaned up
with IMAPClient(host="imap.host.org") as client:
    client.login('someone', 'secret')
    client.select_folder('INBOX')

...

</details>

### postmarker

Python client library for Postmark API

`pip install postmarker` · installs (wheel) · licence: MIT License · rank 4222 · last release 2022-01-15 · [PyPI](https://pypi.org/project/postmarker/)

<details><summary>README extract</summary>

Python client library for Postmark API.

Gitter:

Example:
```python
>>> from postmarker.core import PostmarkClient
>>> postmark = PostmarkClient(server_token='API_TOKEN')
>>> postmark.emails.send(
    From='sender@example.com',
    To='receiver@example.com',
    Subject='Postmark test',
    HtmlBody='<html><body><strong>Hello</strong> dear Postmark user.</body></html>'
)
```

Sections: Postmarker, Usage example, Documentation, Thanks

</details>

### mailjet-rest

Mailjet V3 API wrapper

`pip install mailjet-rest` · installs (wheel) · licence: MIT · rank 4464 · last release 2026-10-07 · [PyPI](https://pypi.org/project/mailjet-rest/) · [docs](https://dev.mailjet.com) · [source](https://github.com/mailjet/mailjet-apiv3-python)

<details><summary>README extract</summary>

Features:
Welcome to the [Mailjet] official Python API wrapper!

Check out all the resources and Python code examples in the official Mailjet Documentation.

Example:
```python
import os
from mailjet_rest import Client

api_key = os.environ.get("MJ_APIKEY_PUBLIC", "")
api_secret = os.environ.get("MJ_APIKEY_PRIVATE", "")

with Client(auth=(api_key, api_secret), version="v3.1") as mailjet:
    data = {
        "Messages": [
            {
                "From": {"Email": "pilot@mailjet.com", "Name": "Mailjet Pilot"},
...
```

Sections: Official Mailjet Python Wrapper, Overview, Compatibility, Requirements, Test dependencies, conda & make, Using conda, Management script, Authentication, Quick Start, Advanced Configuration, API Versioning, Base URL, Usage

</details>

### authres

authres - Authentication Results Header Module

`pip install authres` · installs from source (sdist only) · licence: Apache Software License · rank 4578 · last release 2019-08-03 · [PyPI](https://pypi.org/project/authres/)

### eml-parser

Python EML parser library

`pip install eml-parser` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 5595 · last release 2026-10-27 · [PyPI](https://pypi.org/project/eml-parser/) · [docs](https://eml-parser.readthedocs.io/) · [source](https://github.com/GOVCERT-LU/eml_parser)

_README extract left out: share-alike licence._

### authheaders

A library wrapping email authentication header verification and generation.

`pip install authheaders` · installs from source (sdist only) · licence: MIT License · rank 5868 · last release 2024-06-24 · [PyPI](https://pypi.org/project/authheaders/)

<details><summary>README extract</summary>

Python module for generating email authentication headers: Authheaders can generate both authentication results header fields and DKIM/ ARC signatures. It can perform DKIM, SPF, and DMARC validation, and the results are packaged into a single Authentication-Results header. ...

</details>

### flufl.bounce

Email bounce detectors

`pip install flufl.bounce` · installs (wheel) · licence: Apache Software License · rank 5883 · last release 2026-10-11 · [PyPI](https://pypi.org/project/flufl.bounce/) · [docs](https://fluflbounce.readthedocs.io) · [source](https://gitlab.com/flufl/flufl.bounce.git)

<details><summary>README extract</summary>

Email bounce detectors.

The `flufl.bounce` library provides a set of heuristics and an API for
detecting the original bouncing email addresses from a bounce message. Many
formats found in the wild are supported, as are VERP and RFC 3464 (DSN).

Sections: flufl.bounce, Project details

</details>

### aioimaplib

Python asyncio IMAP4rev1 client library

`pip install aioimaplib` · installs (wheel) · licence: GPL-3.0-only · rank 6131 · last release 2026-10-13 · [PyPI](https://pypi.org/project/aioimaplib/) · [source](https://github.com/iroco-co/aioimaplib)

_README extract left out: share-alike licence._

### mailman

Mailman -- the GNU mailing list manager

`pip install mailman` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 6286 · last release 2024-10-02 · [PyPI](https://pypi.org/project/mailman/) · [docs](https://docs.mailman3.org/projects/mailman/en/latest/index.html) · [source](https://gitlab.com/mailman/mailman.git)

_README extract left out: share-alike licence._

### pyspf

SPF (Sender Policy Framework) implemented in Python.

`pip install pyspf` · installs from source (sdist only) · licence: Python Software Foundation License · rank 6666 · last release 2020-01-02 · [PyPI](https://pypi.org/project/pyspf/)

<details><summary>README extract</summary>

Example:
```python
>>> import spf
>>> spf.check2(i='69.55.226.139',
...           s='terry@wayforward.net',
...           h='mx1.wayforward.net')
('pass', 'sender SPF verified')
```

Sections: SPF, Sender-Policy-Framework queries in Python., Quick Start, Description

</details>

### tnefparse

a TNEF decoding library written in Python, without external dependencies

`pip install tnefparse` · installs (wheel) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6815 · last release 2021-01-24 · [PyPI](https://pypi.org/project/tnefparse/)

_README extract left out: share-alike licence._

### mjml

Python implementation for MJML - a framework that makes responsive-email easy

`pip install mjml` · installs (wheel) · licence: MIT License · rank 7170 · last release 2025-12-27 · [PyPI](https://pypi.org/project/mjml/) · [source](https://github.com/FelixSchwarz/mjml-python)

<details><summary>README extract</summary>

This is an unofficial Python port of mjml v4. It is implemented in pure Python and does not require JavaScript/NodeJS. mjml is a markup language created by Mailjet and designed to reduce the pain of coding a responsive email.

Example:
```python
from mjml import mjml_to_html
with open('foo.mjml', 'rb') as mjml_fp:
    result = mjml_to_html(mjml_fp)
assert not result.errors
html: str = result.html
```

Sections: mjml-python, Usage, Limitations, Goals / Motivation, Documentation, Alternatives / Additional Resources

</details>

### mailgun

Python SDK for Mailgun

`pip install mailgun` · installs (wheel) · licence: Apache-2.0 · rank 7273 · last release 2026-10-21 · [PyPI](https://pypi.org/project/mailgun/) · [docs](https://documentation.mailgun.com) · [source](https://github.com/mailgun/mailgun-python)

<details><summary>README extract</summary>

Welcome to the official Python SDK for Mailgun!

Check out all the resources and Python code examples in the official
Mailgun Documentation.

Features:
The Mailgun API is part of the Sinch family and enables you to send, track, and receive email effortlessly.

Example:
```python
import os
from mailgun import Client

def post_analytics_usage_metrics() -> None:
    """
    # Usage Metrics
    # POST /analytics/usage/metrics
    :return:
    """
    data = {
        "start": "Sun, 08 Jun 2025 00:00:00 +0000",
        "end": "Tue, 08 Jul 2025 00:00:00 +0000",
        "resolution": "day",
        "duration": "1m",
...
```

...

</details>

### quotequail

A library that identifies quoted text in plain text and HTML email messages.

`pip install quotequail` · installs from source (sdist only) · licence: MIT License · rank 7498 · last release 2026-09-21 · [PyPI](https://pypi.org/project/quotequail/)

<details><summary>README extract</summary>

A library that identifies quoted text in plain text and HTML email messages.
quotequail has no mandatory dependencies, however using HTML methods require
libxml.

(Interested in working on projects like this? Close is looking for great engineers to join our team) ...

Example:
```python
In [1]: import quotequail

In [2]: quotequail.quote("""Hello world.

On 2012-10-16 at 17:02 , Someone <someone@example.com> wrote:

> Some quoted text
""")
Out[2]:
[(True, 'Hello world.\n\nOn 2012-10-16 at 17:02 , Someone <someone@example.com> wrote:'),
 (False, '\n> Some quoted text\n')]

In [3]: quotequail.unwrap("""Hello

...
```

Sections: quotequail, Introduction, Examples

</details>

### yagmail

Yet Another GMAIL client

`pip install yagmail` · installs (wheel) · licence: MIT License · rank 7750 · last release 2026-05-26 · [PyPI](https://pypi.org/project/yagmail/)

<details><summary>README extract</summary>

*An asynchronous `asyncio` version is built-in (see Asynchronous Client below).*

The goal here is to make it as simple and painless as possible to send emails.

In the end, your code will look something like this (an async version is also available below): ...

Example:
```python
import yagmail
yag = yagmail.Client('mygmailusername', 'mygmailpassword')
contents = ['This is the body, and here is just text
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('to@someone.com', 'subject', contents)
```

Sections: yagmail -- Yet Another GMAIL/SMTP client, Start a connection, Usability, Recipients, Oauth2, This is a big title, Attaching Files, Asynchronous Client, Feedback, Roadmap (and priorities), Errors

</details>

### pytracking2

Email open and click tracking

`pip install pytracking2` · installs (wheel) · licence: BSD License · rank 7922 · last release 2023-09-19 · [PyPI](https://pypi.org/project/pytracking2/)

<details><summary>README extract</summary>

This repo is a fork of `powergo/pytracking` since it's unmaintained, with code used from `QueraTeam/pytracking` which
made changes to make the code compatible with Python 3.5-3.10 and Django 1.11-4.0.
This fork made further changes and gets released on PyPI under the name `pytracking2`. ...

Features:
There are two main steps when tracking email opens and link clicks:

Example:
```python
import pytracking

open_tracking_url = pytracking.get_open_tracking_url(
    {"customer_id": 1}, base_open_tracking_url="
    webhook_url=" include_webhook_url=True)

# This will produce a URL such as:
#
```

...

</details>

### mailbits

Assorted e-mail utility functions

`pip install mailbits` · installs (wheel) · licence: MIT · rank 8775 · last release 2025-11-29 · [PyPI](https://pypi.org/project/mailbits/) · [source](https://github.com/jwodder/mailbits)

<details><summary>README extract</summary>

GitHub
| PyPI
| Issues
| Changelog

`mailbits` provides a small assortment of functions for working with the
Python standard library's `Message`/`EmailMessage`, `Address`, and
`Group` types, as well as a couple other features. ...

Example:
```python
class MessageDict(TypedDict):
    unixfrom: str | None
    headers: dict[str, Any]
    preamble: str | None
    content: Any
    epilogue: str | None

mailbits.email2dict(msg: email.message.Message, include_all: bool = False) -> MessageDict
```

Sections: API, `ContentType`, `email2dict()`, `format_addresses()`, `message2email()`, `parse_address()`, `parse_addresses()`, `recipient_addresses()`

</details>

### aspose-email-foss

Pure Python CFB and Outlook MSG toolkit for reading, projecting, and writing message data.

`pip install aspose-email-foss` · installs (wheel) · licence: MIT · rank 9290 · last release 2026-03-16 · [PyPI](https://pypi.org/project/aspose-email-foss/) · [docs](https://github.com/aspose-email-foss/Aspose.Email-FOSS-for-Python#readme) · [source](https://github.com/aspose-email-foss/Aspose.Email-FOSS-for-Python)

<details><summary>README extract</summary>

Aspose.Email FOSS for Python is a pure Python toolkit for working with:

- Compound File Binary (CFB) containers
- Outlook MSG files
- High-level MAPI-style message objects
- `email.message.EmailMessage` conversion

It is focused on practical MSG read/write workflows in a lightweight open-source package.

Features:
- Read CFB and Outlook MSG containers
- Inspect low-level storages, streams, and property bags
- Read, edit, and write messages through `MapiMessage`
- Work with recipients, attachments, and embedded messages ...

Example:
```python
from datetime import datetime, timezone

from aspose.email_foss import msg

message = msg.MapiMessage.create("Hello", "Body")
message.set_property(msg.PropertyId.SENDER_NAME, "Build Agent")
...

</details>

### sparkpost

SparkPost Python API client

`pip install sparkpost` · installs (wheel) · licence: Apache Software License · rank 10672 · last release 2021-11-09 · [PyPI](https://pypi.org/project/sparkpost/)

<details><summary>README extract</summary>

Sign up for a SparkPost account and visit our Developer Hub for even more content.

The official Python package for using the SparkPost API.

* Documentation for python-sparkpost
* SparkPost API Reference

Example:
```python
from sparkpost import SparkPost
sp = SparkPost() # uses environment variable
```

Sections: SparkPost Python API client, Documentation, Get a key, Send a message, Django Integration, Using with Google Cloud

</details>

### django-post_office

A Django app to monitor and send mail asynchronously, complete with template support.

`pip install django-post_office` · installs (wheel) · licence: MIT · rank 11417 · last release 2026-10-08 · [PyPI](https://pypi.org/project/django-post_office/)

<details><summary>README extract</summary>

Django Post Office is a simple app to send and manage your emails in
Django. Some awesome features are:

- Designed to scale, handles millions of emails efficiently
- Allows you to send email asynchronously
- Multi backend support
- Supports HTML email
- Supports inlined images in HTML email
- Supports database based email templates ...

Example:
```python
from post_office import mail

mail.send(
    'recipient@example.com',  # List of email addresses also accepted
    'from@example.com',
    subject='My email',
    message='Hi there!',
    html_message='Hi there!',
)
```

...

</details>

### neverbounce-sdk

Official Python SDK for the NeverBounce API

`pip install neverbounce-sdk` · installs (wheel) · licence: MIT License · rank 11778 · last release 2020-08-05 · [PyPI](https://pypi.org/project/neverbounce-sdk/)

<details><summary>README extract</summary>

Welcome to NeverBounce's Python SDK! We hope that it will aid you in consuming
our service. Please report any bugs to the github issue tracker and make sure
you read the documentation before use.

Example:
```python
import neverbounce_sdk
api_key = 'secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = neverbounce_sdk.client(api_key=api_key,timeout=30)
```

Sections: NeverBounceApi-Python, Usage, See Also

</details>

### sharepoint-to-text

Text extraction library for typical file formats found in SharePoint repositories

`pip install sharepoint-to-text` · installs (wheel) · licence: Apache-2.0 · rank 11786 · last release 2026-10-03 · [PyPI](https://pypi.org/project/sharepoint-to-text/) · [docs](https://github.com/Horsmann/sharepoint-to-text#readme) · [source](https://github.com/Horsmann/sharepoint-to-text.git)

<details><summary>README extract</summary>

`sharepoint-to-text` is a typed, pure-Python library for extracting text and
structured content from formats commonly found in SharePoint and document
management systems.

Every supported format returns the same `ExtractedDocument` model. The public
API does not expose format-specific result classes or direct extractor
functions.

Example:
```python
import sharepoint2text

document = next(sharepoint2text.read_file("document.docx"))
print(document.full_text)
print(document.source.path)
```

Sections: sharepoint-to-text, Quick Start, Read from disk, Read from bytes, Read a folder, Process structural units, Read images or skip their extraction, Public Data Model, API Reference, File-size limits, Iterator semantics, Per-file batch reporting, JSON and Markdown, Attachments

</details>

### pyIsEmail

Simple, robust email validation

`pip install pyIsEmail` · installs (wheel) · licence: MIT License · rank 12097 · last release 2022-10-25 · [PyPI](https://pypi.org/project/pyIsEmail/) · [source](https://github.com/michaelherold/pyIsEmail)

<details><summary>README extract</summary>

Example:
```python
from pyisemail import is_email

address = "test@example.com"
bool_result = is_email(address)
detailed_result = is_email(address, diagnose=True)
```

Sections: pyIsEmail, Getting Started, Usage, Versioning, Copyright

</details>

### django-mailbox

Import mail from POP3, IMAP, local mailboxes or directly from Postfix or Exim4 into your Django application automatically.

`pip install django-mailbox` · installs from source (sdist only) · licence: MIT License · rank 12110 · last release 2024-04-21 · [PyPI](https://pypi.org/project/django-mailbox/)

### mailgun2

A python client for Mailgun API v2

`pip install mailgun2` · installs (wheel) · licence: Apache Software License · rank 12158 · last release 2022-03-18 · [PyPI](https://pypi.org/project/mailgun2/)

<details><summary>README extract</summary>

Originally at <

A super simple Python API for interacting with Mailgun. Currently
only supports sending messages. Powered by Requests.

Example:
```python
from mailgun2 import Mailgun
mailer = Mailgun('example.mailgun.org', 'public_key', 'private_key')
mailer.send_message(
    'from@yourdomain.com',
    ['to@you.com', 'others@you.com'],
    subject='Hi!',
    text='Sweet.'
    )
```

Sections: python-mailgun2, Usage

</details>

### checkdmarc

A Python module and command line parser for SPF and DMARC records

`pip install checkdmarc` · installs (wheel) · licence: Apache-2.0 · rank 12654 · last release 2026-10-13 · [PyPI](https://pypi.org/project/checkdmarc/) · [docs](https://domainaware.github.io/checkdmarc/)

<details><summary>README extract</summary>

A Python module, command line utility, and web application for validating SPF and DMARC DNS records.

Features:
- API, CLI, and web interfaces
- Can test multiple domains at once
- CLI output in JSON or CSV format
- DNSSEC validation
- SPF
 - Record validation
 - Counting of DNS lookups and void lookups
 - Counting of lookups per mechanism ...

Sections: checkdmarc, Features

</details>

### mandrill

Deprecated. Replaced by mailchimp-transactional - A CLI client and Python API library for the Mandrill email as a service platform.

`pip install mandrill` · installs from source (sdist only) · licence: Apache Software License · rank 13627 · last release 2021-04-01 · [PyPI](https://pypi.org/project/mandrill/)

<details><summary>README extract</summary>

This SDK is deprecated, and replaced by mailchimp-transactional

Find the current Mailchimp Transactional SDKs at

Features:
Mandrill is a Python API client and suite of CLI-based tools for the Mandrill email as a platform service.

The API client is comprehensive, but the CLI functionality is minimal at this time. ...

Sections: Deprecated, Overview

</details>

### postmark-python

The Official Postmark Python SDK.

`pip install postmark-python` · installs (wheel) · licence: MIT · rank 13668 · last release 2026-10-29 · [PyPI](https://pypi.org/project/postmark-python/) · [docs](https://github.com/ActiveCampaign/postmark-python/wiki) · [source](https://github.com/ActiveCampaign/postmark-python)

<details><summary>README extract</summary>

The official (Beta) Python SDK for Postmark — send emails, manage bounces, templates, webhooks, and more.

For tutorials and detailed usage, check out the wiki.

For details about the Postmark API in general, see the Postmark developer docs.

- Python 3.10+

Example:
```python
import asyncio
import os

import postmark

# Tokens are read from the environment here. Optionally: pip install python-dotenv,
# then use load_dotenv() to populate os.environ from a .env file.

async def main():
    async with postmark.ServerClient(os.environ["POSTMARK_SERVER_TOKEN"]) as client:
        response = await client.outbound.send(
...
```

Sections: postmark-python, Requirements, Quick Start, Two Client Types, Django

</details>

### dramatiq-crontab

Cron style scheduler for asynchronous Dramatiq tasks in Django.

`pip install dramatiq-crontab` · installs (wheel) · licence: BSD License · rank 14151 · last release 2026-10-26 · [PyPI](https://pypi.org/project/dramatiq-crontab/)

<details><summary>README extract</summary>

Cron style scheduler for asynchronous Dramatiq tasks in Django.

- setup recurring tasks via crontab syntax
- lightweight helpers build on robust tools like [Dramatiq] and [APScheduler]
- [Sentry] cron monitor support

You need to have [Dramatiq] installed and setup properly.

Add `dramatiq_crontab` to your `INSTALLED_APPS` in `settings.py`: ...

Example:
```python
# tasks.py
import dramatiq
from dramatiq_crontab import cron

@cron("*/5 * * * *")  # every 5 minutes
@dramatiq.actor
def my_task():
    my_task.logger.info("Hello World")
```

Sections: Dramatiq Crontab, Setup, Setup Redis as a lock backend (optional), Usage, Interval, Sentry Cron Monitors, The crontab command

</details>

### endesive

Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.

`pip install endesive` · installs (wheel) · licence: MIT · rank 14315 · last release 2026-10-31 · [PyPI](https://pypi.org/project/endesive/) · [source](https://github.com/m32/endesive)

<details><summary>README extract</summary>

endesive is a Python library for creating and verifying digital signatures in:

- PDF documents (CMS/CAdES detached signatures, Adobe-compatible)
- S/MIME messages (sign, verify, encrypt, decrypt)
- Plain data streams (CMS detached signatures)
- XML documents (XAdES BES/T, enveloped and enveloping) ...

Features:
- PDF signing and verification with optional TSA timestamping and OCSP data
- S/MIME signing/verification and envelope encryption/decryption
- CMS detached signatures for arbitrary binary/text payloads
- XAdES BES/T generation for XML workflows ...

Example:
```python
import datetime
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from endesive.pdf import cms

with open("cert.p12", "rb") as fp:
...

</details>

### threadweave

The canonical JWZ email message-threading algorithm with RFC 5322 identification-field parsing — pure stdlib, no runtime dependencies.

`pip install threadweave` · installs (wheel) · licence: Apache Software License · rank 14608 · last release 2026-07-12 · [PyPI](https://pypi.org/project/threadweave/) · [source](https://github.com/ContextualWisdomLab/threadweave)

<details><summary>README extract</summary>

**The canonical JWZ email message-threading algorithm for Python — pure
stdlib, zero runtime dependencies.**

`threadweave` turns a flat list of email messages into conversation trees using
Jamie Zawinski's threading algorithm,
built on top of RFC 5322 §3.6.4 identification-field parsing (`Message-ID`,
`References`, `In-Reply-To`). ...

Features:
- Builds the JWZ id-table of containers and links `References` chains **without
 creating loops and without overriding a message's good existing parent**. ...

Example:
```python
from threadweave import Message, thread_messages

threads = thread_messages([
    Message(message_id="a", subject="Deploy plan"),
    Message(message_id="b", in_reply_to="a", references=["a"], subject="Re: Deploy plan"),
...

</details>

### redmail

Email sending library

`pip install redmail` · installs (wheel) · licence: MIT License · rank 14869 · last release 2023-02-25 · [PyPI](https://pypi.org/project/redmail/) · [docs](https://red-mail.readthedocs.io) · [source](https://github.com/Miksus/red-mail)

<details><summary>README extract</summary>

> Next generation email sender

Red Mail is an advanced email sender library.
It is a sister library for Red Box, advanced email reader.
It makes sending emails trivial and has a lot of advanced features such as:

- Attachments
- Templating (with Jinja)
- Embedded images
- Prettified tables
- Send as cc or bcc
- Gmail preconfigured ...

Features:
Sending emails SHOULD NOT be this complicated:

With Red Mail, it is simple as this:

More examples:
- simple example
- email with attachments
- email with embedded images
- email with embedded plots
- email with body parameters ...

Example:
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')
msg['Subject'] = 'An example email'
...

</details>

### pytracking

Email open and click tracking

`pip install pytracking` · installs (wheel) · licence: BSD License · rank 14946 · last release 2021-10-23 · [PyPI](https://pypi.org/project/pytracking/)

<details><summary>README extract</summary>

:Authors:
 Power Go
:Version: 0.2.2

This library provides a set of functions that provide open and click tracking
when sending emails. This is particularly useful if you rely on an Email
Service Provider (ESP) which does not provide open and click tracking. ...

Features:
There are two main steps when tracking email opens and link clicks:

Example:
```python
import pytracking

open_tracking_url = pytracking.get_open_tracking_url(
    {"customer_id": 1}, base_open_tracking_url="
    webhook_url=" include_webhook_url=True)

# This will produce a URL such as:
#
```

...

</details>

## Also in this topic

- [aiosmtplib](communications.md#aiosmtplib) - asyncio SMTP client
- [django-celery-email](communications.md#django-celery-email) - An async Django email backend using celery
- [createsend](communications.md#createsend) - A library which implements the complete functionality of the Campaign Monitor API.
- [email-normalize](communications.md#email-normalize) - Return a normalized email-address stripping ISP specific behaviors
