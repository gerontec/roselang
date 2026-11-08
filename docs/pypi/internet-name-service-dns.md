# Internet / Name Service (DNS)

[Index](README.md) · 11 packages in this topic, 4 more listed under another topic, by downloads.

### idna

Internationalized Domain Names in Applications (IDNA)

`pip install idna` · installs (wheel) · licence: BSD-3-Clause · rank 5 · last release 2026-09-17 · [PyPI](https://pypi.org/project/idna/) · [source](https://github.com/kjd/idna)

<details><summary>README extract</summary>

Support for Internationalized Domain Names in Applications
(IDNA) and Unicode IDNA
Compatibility Processing. It
supersedes the standard library's `encodings.idna`, which only
implements the 2003 specification, offering broader script coverage and
limiting domains with known security vulnerabilities.

Example:
```python
>>> import idna
>>> idna.encode('ドメイン.テスト')
b'xn--eckwd4c7c.xn--zckzah'
>>> print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
ドメイン.テスト
```

Sections: Internationalized Domain Names in Applications (IDNA), Usage, Compatibility Mapping (UTS #46), Exceptions, Command-line tool, Additional Notes

</details>

### dnspython

DNS toolkit

`pip install dnspython` · installs (wheel) · licence: ISC · rank 122 · last release 2026-11-03 · [PyPI](https://pypi.org/project/dnspython/) · [docs](https://dnspython.readthedocs.io/en/stable/) · [source](https://github.com/rthalley/dnspython.git)

<details><summary>README extract</summary>

`dnspython` is a DNS toolkit for Python. It supports almost all record types. It
can be used for queries, zone transfers, and dynamic updates. It supports
TSIG-authenticated messages and EDNS0.

`dnspython` provides both high- and low-level access to DNS. ...

Sections: dnspython, INTRODUCTION, Notices

</details>

### publicsuffix2

Get a public suffix for a domain name using the Public Suffix List. Forked from and using the same API as the publicsuffix package.

`pip install publicsuffix2` · installs (wheel) · licence: MIT License; Mozilla Public License 2.0 (MPL 2.0) · rank 1678 · last release 2019-12-21 · [PyPI](https://pypi.org/project/publicsuffix2/)

<details><summary>README extract</summary>

This module allows you to get the public suffix, as well as the registrable domain,
of a domain name using the Public Suffix List from

A public suffix is a domain suffix under which you can register domain
names, or under which the suffix owner does not control the subdomains. ...

Example:
```python
>>> from publicsuffix2 import get_public_suffix
>>> get_public_suffix('www.example.com')
'example.com'
>>> get_sld('www.example.com')
'example.com'
>>> get_public_suffix('www.example.co.uk')
'example.co.uk'
>>> get_public_suffix('www.super.example.co.uk')
'example.co.uk'
>>> get_sld("co.uk")  # returns eTLD as is
'co.uk'
```

Sections: Public Suffix List module for Python, Usage, Source

</details>

### publicsuffixlist

publicsuffixlist implement

`pip install publicsuffixlist` · installs (wheel) · licence: MPL-2.0 · rank 2113 · last release 2026-11-07 · [PyPI](https://pypi.org/project/publicsuffixlist/) · [source](https://github.com/ko-zu/psl)

<details><summary>README extract</summary>

Public Suffix List parser implementation for
Python 3.8+.

- Compliant with TEST DATA.
- Supports IDN (unicode and punycoded).
- Supports Python3.8+.
- Shipped with built-in PSL and an updater script.
- Written in Pure Python with no library dependencies.

Example:
```python
from publicsuffixlist import PublicSuffixList

psl = PublicSuffixList()
# Uses built-in PSL file

print(psl.publicsuffix("www.example.com")) # "com"
# The longest public suffix part

print(psl.privatesuffix("www.example.com")) # "example.com"
# The shortest domain assigned for a registrant

print(psl.privatesuffix("com")) # None
...
```

Sections: publicsuffixlist, Usage, Limitation, Domain Label Validation, Punycode Handling, Handling Arbitrary Binary, Source / Link

</details>

### dnslib

Simple library to encode/decode DNS wire-format packets

`pip install dnslib` · installs (wheel) · licence: BSD · rank 4076 · last release 2025-03-03 · [PyPI](https://pypi.org/project/dnslib/)

### python-designateclient

OpenStack DNS-as-a-Service - Client

`pip install python-designateclient` · installs (wheel) · licence: Apache-2.0 · rank 10253 · last release 2026-07-01 · [PyPI](https://pypi.org/project/python-designateclient/) · [docs](https://docs.openstack.org/python-designateclient/latest) · [source](https://opendev.org/openstack/python-designateclient)

<details><summary>README extract</summary>

This is a client library for Designate built on the Designate API. It
provides a Python API (the `designateclient` module) and a command-line tool
(`designate`).

Development takes place via the usual OpenStack processes as outlined in the
developer guide. The master
repository is in Git.

See release notes and more at < ...

</details>

### py3dns

Python 3 DNS library

`pip install py3dns` · installs (wheel) · licence: Python License (CNRI Python License) · rank 10811 · last release 2024-06-06 · [PyPI](https://pypi.org/project/py3dns/)

<details><summary>README extract</summary>

Release 4.0.0 Sat, Jul 1, 2023
Removed class DnsAsyncRequest since Python 3.12 dropped asyncore. Bumping
major version since this is a breaking change. If you need async DNS, use
aiodns instead.

Changed behavior when /etc/resolv.conf is missing. Instead of
FileNotFoundError, assume DNS server is '127.0.0.1'.

Release 3.2.0 Mon Jul 23 2018 ...

</details>

### octodns

OctoDNS: DNS as code - Tools for managing DNS across multiple providers

`pip install octodns` · installs (wheel) · licence: MIT · rank 11797 · last release 2026-08-15 · [PyPI](https://pypi.org/project/octodns/) · [docs](https://octodns.readthedocs.io/) · [source](https://github.com/octodns/octodns)

<details><summary>README extract</summary>

In the vein of infrastructure as
code octoDNS provides a set of tools & patterns that make it easy to manage your DNS records across multiple providers. The resulting config can live in a repository and be deployed just like the rest of your code, maintaining a clear history and using your existing review & workflow. ...

Sections: Documentation, Getting help

</details>

### dns-lexicon

Manipulate DNS records on various DNS providers in a standardized/agnostic way

`pip install dns-lexicon` · installs (wheel) · licence: MIT · rank 12878 · last release 2026-11-01 · [PyPI](https://pypi.org/project/dns-lexicon/) · [docs](https://dns-lexicon.github.io/dns-lexicon/user_guide.html) · [source](https://github.com/dns-lexicon/dns-lexicon)

<details><summary>README extract</summary>

Manipulate DNS records on various DNS providers in a standardized/agnostic way.

Features:
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a standardized way.

Lexicon can be used as:

Lexicon was designed to be used in automation, specifically letsencrypt. ...

Example:
```python
# Create a TXT entry in domain.net zone hosted by CloudFlare
from lexicon.client import Client
from lexicon.config import ConfigResolver

config = ConfigResolver().with_env().with_dict({
    "provider_name" : "cloudflare",
    "domain": "domain.net",
})

with Client(config) as operations:
    operations.create_record("TXT", "foo", "bar")
```

Sections: Why using Lexicon?, Documentation, Licensing

</details>

### dnsdb2

Client for DNSDB API version 2 with Flexible Search

`pip install dnsdb2` · installs (wheel) · licence: Apache Software License · rank 13624 · last release 2026-10-29 · [PyPI](https://pypi.org/project/dnsdb2/)

<details><summary>README extract</summary>

DomainTools' Farsight DNSDB® is the world’s largest DNS intelligence database that provides a unique, fact-based, multifaceted view of the configuration of the global Internet infrastructure. DNSDB leverages the richness of Farsight’s Security Information Exchange (SIE) data-sharing platform and is engineered and operated by leading DNS experts. ...

Example:
```python
import dnsdb2
apikey = "INSERT YOUR DNSDB API KEY HERE"
client = dnsdb2.Client(apikey, swclient="yourappname", version="v0.0")
```

Sections: Requirements, Examples, API Documentation, Client Objects, ping, rate\_limit, lookup\_rrset, summarize\_rrset, lookup\_rdata\_name, summarize\_rdata\_name, lookup\_rdata\_ip, summarize\_rdata\_ip, lookup\_rdata\_raw, summarize\_rdata\_raw

</details>

### vinyldns-python

Python client library for VinylDNS

`pip install vinyldns-python` · installs (wheel) · licence: Apache Software License · rank 14037 · last release 2026-05-21 · [PyPI](https://pypi.org/project/vinyldns-python/)

<details><summary>README extract</summary>

Python client library for VinylDNS

This project is a work in progress! If you would like to help us get this where it needs to be,
please reach out to us in gitter.

To run, `pip install vinyldns-python` and then:

Example:
```python
>>> from vinyldns.client import VinylDNSClient
>>> local_client = VinylDNSClient("ApiEndpoint", "UserAccessKey", "UserSecretKey")
>>> local_client.list_zones()
>>>
>>> # If all of the following environments are set
>>> # - VINYLDNS_API_URL
>>> # - VINYLDNS_ACCESS_KEY_ID
>>> # - VINYLDNS_SECRET_ACCESS_KEY
...
```

</details>

## Also in this topic

- [fqdn](internet.md#fqdn) - Validates fully-qualified domain names against RFC 1123, so that they are acceptable to modern browsers
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [dkimpy](communications-email.md#dkimpy) - DKIM (DomainKeys Identified Mail), ARC (Authenticated Receive Chain), and TLSRPT (TLS Report) email signing and verification
- [pyspf](communications-email.md#pyspf) - SPF (Sender Policy Framework) implemented in Python.
