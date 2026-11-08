# Communications / Telephony

[Index](README.md) · 5 packages in this topic, by downloads.

### phonenumbers

Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

`pip install phonenumbers` · installs (wheel) · licence: Apache-2.0 · rank 529 · last release 2026-11-06 · [PyPI](https://pypi.org/project/phonenumbers/)

<details><summary>README extract</summary>

This is a Python port of Google's libphonenumber library
It supports Python 2.5-2.7 and Python 3.x (in the same codebase, with no
2to3 conversion needed).

Original Java code is Copyright (C) 2009-2015 The Libphonenumber Authors.

Release HISTORY,
derived from upstream release notes.

Documentation

Installation

Install using pip with: ...

Example:
```python
>>> import phonenumbers
>>> x = phonenumbers.parse("+442083661177", None)
>>> print(x)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> type(x)
<class 'phonenumbers.phonenumber.PhoneNumber'>
>>> y = phonenumbers.parse("020 8366 1177", "GB")
>>> print(y)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> x == y
...
```

</details>

### twilio

Twilio API client and TwiML generator

`pip install twilio` · installs (wheel) · licence: MIT License · rank 765 · last release 2026-11-06 · [PyPI](https://pypi.org/project/twilio/)

<details><summary>README extract</summary>

The documentation for the Twilio API can be found here.

The Python library documentation can be found here.

`twilio-python` uses a modified version of Semantic Versioning for all changes. See this document for details.

Example:
```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
```

Sections: twilio-python, Documentation, Versions, OAuth Feature for Twilio APIs, Use the helper library, API Credentials, Specify Region and/or Edge, Make a Call, Get data about an existing call, Iterate through records, Use the `list` method, Asynchronous API Requests, Enable Debug Logging, Handling Exceptions

</details>

### phonenumberslite

Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

`pip install phonenumberslite` · installs (wheel) · licence: Apache-2.0 · rank 1426 · last release 2026-11-06 · [PyPI](https://pypi.org/project/phonenumberslite/)

<details><summary>README extract</summary>

This is a Python port of Google's libphonenumber library
It supports Python 2.5-2.7 and Python 3.x (in the same codebase, with no
2to3 conversion needed).

Original Java code is Copyright (C) 2009-2015 The Libphonenumber Authors.

Release HISTORY,
derived from upstream release notes.

Documentation

Installation

Install using pip with: ...

Example:
```python
>>> import phonenumbers
>>> x = phonenumbers.parse("+442083661177", None)
>>> print(x)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> type(x)
<class 'phonenumbers.phonenumber.PhoneNumber'>
>>> y = phonenumbers.parse("020 8366 1177", "GB")
>>> print(y)
Country Code: 44 National Number: 2083661177 Leading Zero: False
>>> x == y
...
```

</details>

### pylibsrtp

Python wrapper around the libsrtp library

`pip install pylibsrtp` · installs (wheel) · licence: BSD-3-Clause · rank 2813 · last release 2025-10-13 · [PyPI](https://pypi.org/project/pylibsrtp/) · [docs](https://pylibsrtp.readthedocs.io/)

<details><summary>README extract</summary>

`pylibsrtp` is a Python wrapper around libsrtp, making it possible to
encrypt and decrypt Secure Real-time Transport Protocol (SRTP) packets from
Python code.

SRTP is a profile of the Real-time Transport Protocol (RTP) which provides
confidentiality, message authentication, and replay protection. It is defined
by RFC 3711. ...

Example:
```python
# !/usr/bin/env python

from pylibsrtp import Policy, Session

key = (b'\x00' * 30)
rtp = b'\x80\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + (b'\xd4' * 160)

# protect RTP
tx_policy = Policy(key=key, ssrc_type=Policy.SSRC_ANY_OUTBOUND)
tx_session = Session(policy=tx_policy)
srtp = tx_session.protect(rtp)

# unprotect RTP
...
```

Sections: pylibsrtp, What is `pylibsrtp`?, Example, Building pylibsrtp

</details>

### plivo

A Python SDK to make voice calls & send SMS using Plivo and to generate Plivo XML

`pip install plivo` · installs (wheel) · licence: MIT License · rank 6774 · last release 2026-09-25 · [PyPI](https://pypi.org/project/plivo/)

<details><summary>README extract</summary>

The Plivo Python SDK makes it simpler to integrate communications into your
Python applications using the Plivo REST API. Using the SDK, you will be able
to make voice calls, send SMS and generate Plivo XML to control your call flows.

See for more information.

</details>

