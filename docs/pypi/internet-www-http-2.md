# Internet / WWW/HTTP (part 2 of 2)

[Index](README.md) · 607 packages in this topic, 86 more listed under another topic, by downloads.

[part 1](internet-www-http.md) · part 2

### allianceauth-securegroups

On its own this app does very little! However it leverages any module that is capable of providing a filter. Giving you the ability to add a very wide range of automatic filtration options your groups.

`pip install allianceauth-securegroups` · installs (wheel) · licence: MIT License · rank 11247 · last release 2026-07-07 · [PyPI](https://pypi.org/project/allianceauth-securegroups/) · [source](https://github.com/Solar-Helix-Independent-Transport/allianceauth-secure-groupss)

<details><summary>README extract</summary>

Plugin for Auto Group Bot Stuffs for Alliance Auth.

On its own this app does very little! However it leverages any module that is capable of providing a filter. Giving you the ability to add a very wide range of automatic filtration options your groups.

Features:
- Manual Groups, either auto join or still request join via Alliance Auth's Built in Group Management system.
- Auto Groups, process all member states for a filter and add/remove who ever passes/doesn't. ...

Sections: Secure Groups, Features, Apps that provide a filter, Soon(tm) Wishlist, Configuration, Permissions, Notifications, Screenshots, Admin Setup of Smart Groups, User Group Selection, User Failed Checks, User Passed Checks, Audit Secure Groups, Discord Message Example

</details>

### aa-freight

An Alliance Auth app for running a freight service.

`pip install aa-freight` · installs (wheel) · licence: not stated · rank 11248 · last release 2026-10-05 · [PyPI](https://pypi.org/project/aa-freight/)

<details><summary>README extract</summary>

An Alliance Auth app for running a freight service.

Features:
Freight is an Alliance Auth (AA) app that helps running a central freight service for an alliance or corporation. It allows different modes of operation that support the most common approaches a central freight service is setup. (e.g. ...

Sections: Freight for Alliance Auth, Overview, Key Features, Screenshots, Reward Calculator, Contract List, Discord Notification, 2 - Update Eve Online app, 3 - Configure AA settings, 3a - Celery setup, 5 - Setup permissions, 6 - Setup contract handler, 7 - Define pricing, 8 - Setup Discord Proxy (optional)

</details>

### apiclient

Framework for making good API client libraries using urllib3.

`pip install apiclient` · installs from source (sdist only) · licence: MIT License · rank 11250 · last release 2019-03-21 · [PyPI](https://pypi.org/project/apiclient/)

<details><summary>README extract</summary>

Tiny framework for building *good* API client libraries thanks to
urllib3.

Features:
- Threadsafely reuses connections with Keep-Alive (via urllib3).
- Small and easy to understand codebase perfect for extending and building upon.
- Built-in support for rate limiting and request throttling. ...

Example:
```python
>>> from apiclient import APIClient
>>> class AcmePublicAPI(APIClient):
...    BASE_URL = '

>>> acme_api = AcmePublicAPI()

>>> acme_api.call('/hello')
{'what': 'world'}
>>> acme_api.call('/echo', params={"ping": "pong"})
{'ping': 'pong'}
```

Sections: Highlights, Examples, Extending, TODO, . Fork on Github., . Send a pull request., Changes, 1.0.3 (2016-05-15), 1.0.2 (2011-10-20), 1.0.1 (2011-10-10), 1.0 (2011-10-03)

</details>

### urlpy

Simple URL parsing, canonicalization and equivalence.

`pip install urlpy` · installs (wheel) · licence: MIT License · rank 11261 · last release 2020-04-28 · [PyPI](https://pypi.org/project/urlpy/)

<details><summary>README extract</summary>

A library with helper functions to parse URLs, and sanitize and normalize them
in pure python.

This includes support for escaping, unescaping, cleaning and sorting parameters
and query strings, and a little more sanitization. ...

</details>

### aa-memberaudit-dc

Doctrine Checker Addon module for Memberaudit

`pip install aa-memberaudit-dc` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11294 · last release 2026-07-10 · [PyPI](https://pypi.org/project/aa-memberaudit-dc/) · [source](https://github.com/Geuthur/aa-memberaudit-dc)

_README extract left out: share-alike licence._

### aa-inactivity

An app for monitoring game activity of members with Member Audit and Alliance Auth.

`pip install aa-inactivity` · installs (wheel) · licence: not stated · rank 11301 · last release 2026-09-18 · [PyPI](https://pypi.org/project/aa-inactivity/)

<details><summary>README extract</summary>

An app for monitoring game activity of members with Member Audit and Alliance Auth.

- Features
- Screenshots
- Installation
- Permissions
- Settings

Features:
- Automatically notify users who become inactive.
- Automatically notify managers when users become inactive.
- Approval process for leave of absence requests
- Can inform managers about various events via Discord webhook
- List of inactive users ...

Example:
```python
CELERYBEAT_SCHEDULE['inactivity_check_inactivity'] = {
    'task': 'inactivity.tasks.check_inactivity',
    'schedule': crontab(minute=0, hour=0),
}
```

Sections: AA Inactivity, Content, Features, Screenshots, Step 0 - Requirements, Step 2 - Config, Permissions, Settings

</details>

### aa-memberaudit-dashboard

Dashboard Addon for Member Audit

`pip install aa-memberaudit-dashboard` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 11304 · last release 2026-09-10 · [PyPI](https://pypi.org/project/aa-memberaudit-dashboard/) · [docs](https://github.com/Geuthur/aa-memberaudit-dashboard/blob/master/README.md) · [source](https://github.com/Geuthur/aa-memberaudit-dashboard)

_README extract left out: share-alike licence._

### aa-memberaudit-securegroups

An Alliance Auth app that enables secure group management with Member Audit.

`pip install aa-memberaudit-securegroups` · installs (wheel) · licence: not stated · rank 11324 · last release 2026-07-13 · [PyPI](https://pypi.org/project/aa-memberaudit-securegroups/)

<details><summary>README extract</summary>

An Alliance Auth app that enables secure group management with Member Audit.

Features:
Member Audit Secure Groups provides Secure Groups filters based on character information from Member Audit.
The following filters are provided:

- Activity Filter
- Asset Filter
- Character Age Filter
- Compliance Filter
- Corporation Role Filter ...

Sections: Member Audit Secure Groups, Features, Step 1 - Check prerequisites, Step 3: Configure Auth settings, Step 5: Setup secure groups (Optional), Updating from aa-ma-securegroups, Step 3: Finalize App Update, Documentation

</details>

### allianceauth-blacklist

Integration with Alliance Auth's State System, creates an maintains a Blacklisted State to ensure no services access is granted to Blacklisted users

`pip install allianceauth-blacklist` · installs (wheel) · licence: MIT License · rank 11350 · last release 2026-05-31 · [PyPI](https://pypi.org/project/allianceauth-blacklist/) · [source](https://github.com/Solar-Helix-Independent-Transport/allianceauth-blacklist)

<details><summary>README extract</summary>

You Shall Not Pass!

Features:
- Integration with Alliance Auth's State System, creates an maintains a Blacklisted State to ensure no services access is granted to Blacklisted users
- Notes
- Comments on Notes

Sections: allianceauth-blacklist, Features, Permissions

</details>

### pyspelling

Spell checker.

`pip install pyspelling` · installs (wheel) · licence: MIT · rank 11363 · last release 2026-10-11 · [PyPI](https://pypi.org/project/pyspelling/)

<details><summary>README extract</summary>

[][donate-link]
[][codecov-link]
[][pypi-link]
[][pypi-link]
[][license-link]

Features:
PySpelling is a module to help with automating spell checking in a project with Aspell or
Hunspell. It is essentially a wrapper around the command line utility of these two spell checking tools, and
allows you to setup different spelling tasks for ...

Sections: PySpelling, Overview, Documentation

</details>

### backports.ssl

The Python 3.4 standard `ssl` module API implemented on top of pyOpenSSL

`pip install backports.ssl` · installs from source (sdist only) · licence: MIT License · rank 11408 · last release 2015-12-09 · [PyPI](https://pypi.org/project/backports.ssl/)

<details><summary>README extract</summary>

backports.ssl

What is it?

It's the Python 3.4 standard ``ssl`` module API implemented on top of
pyOpenSSL::

 import backports.ssl as ssl
 import socket

 context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
 context.verify_mode = ssl.CERT_REQUIRED ...

</details>

### rets-python

rets-python

`pip install rets-python` · installs (wheel) · licence: MIT License · rank 11644 · last release 2024-10-15 · [PyPI](https://pypi.org/project/rets-python/)

<details><summary>README extract</summary>

Python 3 client for the Real Estate Transaction Standard (RETS) Version 1.7.2

</details>

### fhirpathpy

FHIRPath implementation in Python

`pip install fhirpathpy` · installs (wheel) · licence: not stated · rank 11655 · last release 2026-08-25 · [PyPI](https://pypi.org/project/fhirpathpy/) · [docs](https://github.com/beda-software/fhirpath-py#readme) · [source](https://github.com/beda-software/fhirpath-py.git)

<details><summary>README extract</summary>

FHIRPath implementation in Python

Parser was generated with antlr4

Example:
```python
from fhirpathpy import evaluate

patient = {
  "resourceType": "Patient",
  "id": "example",
  "name": [
    {
      "use": "official",
      "given": [
        "Peter",
        "James"
      ],
      "family": "Chalmers"
    },
    {
      "use": "usual",
      "given": [
        "Jim"
      ]
    },
    {
      "use": "maiden",
      "given": [
...
```

Sections: fhirpath.py, Getting started, Usage, evaluate, compile, Using data models, User-defined functions

</details>

### zope.location

Zope Location

`pip install zope.location` · installs (wheel) · licence: Zope Public License · rank 11664 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.location/)

<details><summary>README extract</summary>

In Zope 3, "locations" are special objects, that have a structural
location, indicated with _name and _parent` attributes.

See zope.container
for a useful extension of this concept to "containers".

Documentation is hosted at

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: `zope.location, Changes, 6.0 (2025-09-12), 5.1 (2025-01-31), 5.0 (2023-05-25), 4.3 (2022-11-29), 4.2 (2018-10-09), 4.1.0 (2017-08-03), 4.0.3 (2014-03-19), 4.0.2 (2013-03-11), 4.0.1 (2013-02-19), 4.0.0 (2012-06-07), 3.9.1 (2011-08-22), 3.9.0 (2009-12-29)

</details>

### breadability

Port of Readability HTML parser in Python

`pip install breadability` · installs (wheel) · licence: BSD License · rank 11702 · last release 2026-08-12 · [PyPI](https://pypi.org/project/breadability/)

<details><summary>README extract</summary>

I've tried to work with the various forks of some ancient codebase that ported
readability to Python. The lack of tests, unused regex's, and commented out
sections of code in other Python ports just drove me nuts. ...

Example:
```python
from future import print_function

from breadability.readable import Article

if name == "main":
    document = Article(html_as_text, url=source_url)
    print(document.readable)
```

Sections: breadability - another readability Python (v2.6-v3.3) port, Alternatives, Tests, Usage, Command line, Options, Python API, Work to be done, Inspiration, 0.1.21 (August 9th 2026), 0.1.20 (April 13th 2014), 0.1.19 (April 13th 2014), 0.1.18 (April 6th 2014), 0.1.17 (Jan 22nd 2014)

</details>

### zope.lifecycleevent

Object life-cycle events

`pip install zope.lifecycleevent` · installs (wheel) · licence: Zope Public License · rank 11708 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.lifecycleevent/)

<details><summary>README extract</summary>

Features:
In a loosely-coupled system, events can be used by parts of the system
to inform each other about relevant occurrences. The zope.event
package (optionally together with zope.interface and
zope.component) provides a generic mechanism to dispatch ...

Sections: `zope.lifecycleevent`, Overview, Changes, 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0 (2023-07-06), 4.4 (2022-05-09), 4.3 (2018-10-05), 4.2.0 (2017-07-12), 4.1.0 (2014-12-27), 4.0.3 (2013-09-12), 4.0.2 (2013-03-08), 4.0.1 (2013-02-11), 4.0.0 (2013-02-11)

</details>

### zope.publisher

The Zope publisher publishes Python objects on the web.

`pip install zope.publisher` · installs (wheel) · licence: ZPL-2.1 · rank 11727 · last release 2026-06-24 · [PyPI](https://pypi.org/project/zope.publisher/) · [docs](https://zopepublisher.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.publisher)

<details><summary>README extract</summary>

This package allows you to publish Python objects on the web. It
has support for plain HTTP/WebDAV clients, web browsers as well as
XML-RPC and FTP clients. Input and output streams are represented by
request and response objects which allow for easy client interaction
from Python. ...

Sections: zope.publisher, Changes, 8.1 (2026-06-24), 8.0 (2025-09-12), 7.3 (2025-03-05), 7.2 (2024-12-19), 7.1 (2024-09-27), 7.0 (2023-08-29), 6.1.0 (2022-03-15), 6.0.2 (2021-06-07), 6.0.1 (2021-04-15), 6.0.0 (2021-01-20), 5.2.1 (2020-06-15), 5.2.0 (2020-03-30)

</details>

### django-diagram

Generate an Entity Relationship Diagram for a Django project in Mermaid format

`pip install django-diagram` · installs (wheel) · licence: All Rights Reserved · rank 11729 · last release 2023-02-18 · [PyPI](https://pypi.org/project/django-diagram/)

<details><summary>README extract</summary>

Generate an Entity Relationship Diagram for a Django project in Mermaid format

Sections: django-diagram, Usage

</details>

### django-rest-multiple-models

Multiple model/queryset view (and mixin) for Django Rest Framework

`pip install django-rest-multiple-models` · installs (wheel) · licence: MIT License · rank 11734 · last release 2018-12-01 · [PyPI](https://pypi.org/project/django-rest-multiple-models/)

<details><summary>README extract</summary>

drf-multiple-models provides an easy view (and mixin) for serializing multiple models in a single view. It is built on top of (and meant to be an extension for) Django Rest Framework.

Sections: Django Rest Multiple Model View, Usage

</details>

### WSGIProxy2

A WSGI Proxy with various http client backends

`pip install WSGIProxy2` · installs (wheel) · licence: MIT License · rank 11751 · last release 2021-08-26 · [PyPI](https://pypi.org/project/WSGIProxy2/)

<details><summary>README extract</summary>

Example:
```python
>>> from wsgiproxy import HostProxy
>>> proxy = HostProxy(application_url)
```

Sections: Usage, Changes, 0.5.1 (2021-08-26), 0.5.0 (2021-08-18), 0.4.6 (2019-02-22), 0.4.5 (2018-09-19), 0.4.4 (2017-06-02), 0.4.3 (2017-02-17), 0.4.2 (2014-12-20), 0.4.1 (2013-12-21), 0.4 (2013-12-21), 0.3 (2013-09-12), 0.2, 0.1

</details>

### dj-static

Serve production static files with Django.

`pip install dj-static` · installs from source (sdist only) · licence: BSD License · rank 11787 · last release 2014-07-11 · [PyPI](https://pypi.org/project/dj-static/)

<details><summary>README extract</summary>

dj-static
~~~~~~~~~

This is a simple Django middleware utility that allows you to properly
serve static assets from production with a WSGI server like Gunicorn.

Django `doesn't recommend <
the production use of its static file server for a number of reasons.
There exists, however, a lovely WSGI application aptly named `Static < ...

</details>

### zope.i18n

Zope Internationalization Support

`pip install zope.i18n` · installs (wheel) · licence: Zope Public License · rank 11799 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.i18n/)

<details><summary>README extract</summary>

This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.

* Gettext-based message catalogs for message strings.

* Locale discovery for Web-based requests.

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: zope.i18n, CHANGES, 6.0 (2025-09-12), 5.3 (2025-07-23), 5.2 (2024-09-27), 5.1 (2023-08-28), 5.0 (2023-03-27), 4.9.0 (2021-12-09), 4.8.0 (2021-09-07), 4.7.0 (2019-07-10), 4.6.2 (2019-02-19), 4.6.1 (2018-10-24), 4.6.0 (2018-10-22), 4.5 (2018-10-19)

</details>

### rebrowser-playwright

A high-level API to automate web browsers

`pip install rebrowser-playwright` · installs (wheel) · licence: Apache-2.0 · rank 11819 · last release 2026-11-02 · [PyPI](https://pypi.org/project/rebrowser-playwright/)

<details><summary>README extract</summary>

> ⚠️ This is the original `playwright-python` patched with `rebrowser-patches`.
> 🕵️ The ultimate goal is to pass all automation detection tests presented in `rebrowser-bot-detector`.
> 🪄 It's designed to be a drop-in replacement for the original `playwright` without changing your codebase. ...

Example:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
```

Sections: rebrowser-playwright, 🎭 Playwright for Python, Documentation, API Reference, Example, Other languages

</details>

### Flask-SSLify

Force SSL on your Flask app.

`pip install Flask-SSLify` · installs from source (sdist only) · licence: BSD License · rank 11903 · last release 2015-04-02 · [PyPI](https://pypi.org/project/Flask-SSLify/)

<details><summary>README extract</summary>

Flask-SSLify

This is a simple Flask extension that configures your Flask application to redirect
all incoming requests to ``https``.

Redirects only occur when ``app.debug`` is ``False``.

</details>

### zope.contenttype

Zope contenttype

`pip install zope.contenttype` · installs (wheel) · licence: Zope Public License · rank 11912 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.contenttype/)

<details><summary>README extract</summary>

A utility module for content-type (MIME type) handling.

Functions include:

- Guessing a content type given a name and (optional) body data.
- Guessing a content type given some text.
- Parsing MIME types.

Documentation is hosted at

Sections: `zope.contenttype`, 6.0 (2025-09-12), 5.2 (2025-02-14), 5.1 (2023-09-21), 5.0 (2023-03-27), 4.6 (2022-09-07), 4.5.0 (2019-12-19), 4.4 (2018-10-05), 4.3.0 (2017-08-10), 4.2.0 (2016-08-26), 4.1.0 (2014-12-26), 4.0.1 (2013-02-20), 4.0.0 (2013-02-11), 3.5.5 (2011-07-27)

</details>

### filestack-python

Filestack Python SDK

`pip install filestack-python` · installs (wheel) · licence: Apache Software License · rank 11926 · last release 2024-09-17 · [PyPI](https://pypi.org/project/filestack-python/)

### zope.browser

Shared Zope Toolkit browser components

`pip install zope.browser` · installs (wheel) · licence: Zope Public License · rank 11940 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.browser/)

<details><summary>README extract</summary>

This package provides shared browser components for the Zope Toolkit.
These components consist of a set of interfaces defining common
concepts, including:

- `IView`
- `IBrowserView`
- `IAdding`
- `ITerms`
- `ISystemErrorView`

Documentation is hosted at

Sections: zope.browser, 4.0 (2025-09-12), 3.1 (2025-02-13), 3.0 (2023-03-27), 2.4 (2022-04-06), 2.3 (2018-10-05), 2.2.0 (2017-08-10), 2.1.0 (2014-12-26), 2.0.2 (2013-03-08), 2.0.1 (2013-02-11), 2.0.0 (2013-02-11), 1.3 (2010-04-30), 1.2 (2009-05-18), 1.1 (2009-05-13)

</details>

### aiohttp-middlewares

Collection of useful middlewares for aiohttp applications.

`pip install aiohttp-middlewares` · installs (wheel) · licence: BSD-3-Clause · rank 11959 · last release 2026-09-16 · [PyPI](https://pypi.org/project/aiohttp-middlewares/) · [docs](https://aiohttp-middlewares.readthedocs.io/) · [source](https://github.com/playpauseandstop/aiohttp-middlewares)

<details><summary>README extract</summary>

Collection of useful middlewares for aiohttp.web applications.

- Works on Python 3.10+
- Works with aiohttp.web 3.11.0+
- BSD licensed
- Latest documentation on Read The Docs
- Source, issues, and pull requests on GitHub

Example:
```python
from aiohttp import web
from aiohttp_middlewares import (
    cors_middleware,
    error_middleware,
)

app = web.Application(
    middlewares=(
        cors_middleware(origins=("
        error_middleware(),
    )
)
```

Sections: aiohttp-middlewares, Quick Start

</details>

### certbot-dns-route53

Route53 DNS Authenticator plugin for Certbot

`pip install certbot-dns-route53` · installs (wheel) · licence: Apache-2.0 · rank 11981 · last release 2026-10-29 · [PyPI](https://pypi.org/project/certbot-dns-route53/)

<details><summary>README extract</summary>

Amazon Web Services Route 53 DNS Authenticator plugin for Certbot

</details>

### djangorestframework-bulk

Django REST Framework bulk CRUD view mixins

`pip install djangorestframework-bulk` · installs from source (sdist only) · licence: MIT License · rank 11992 · last release 2015-04-26 · [PyPI](https://pypi.org/project/djangorestframework-bulk/)

<details><summary>README extract</summary>

Django REST Framework bulk CRUD view mixins.

Features:
Django REST Framework comes with many generic views however none
of them allow to do bulk operations such as create, update and delete. ...

Example:
```python
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class FooSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = FooModel
        # only necessary in DRF3
        list_serializer_class = BulkListSerializer

...
```

Sections: Django REST Framework Bulk, Overview, Requirements, Example, Router, DRF3, Notes, 0.2.1 (2015-04-26), 0.2 (2015-02-09), 0.1.4 (2015-02-01), 0.1.3 (2014-06-11), 0.1.2 (2014-04-15), 0.1.1 (2014-01-20), 0.1 (2014-01-18)

</details>

### Flask-Cognito

Authenticate users to Cognito user pool via JWT.

`pip install Flask-Cognito` · installs from source (sdist only) · licence: BSD License · rank 12015 · last release 2024-04-13 · [PyPI](https://pypi.org/project/Flask-Cognito/)

<details><summary>README extract</summary>

Flask-Cognito

Authenticate users based on AWS Cognito JWT.

Example:
```python
# configuration
app.config.update({
    'COGNITO_REGION': 'eu-central-1',
    'COGNITO_USERPOOL_ID': 'eu-central-1c3fea2',

    # optional
    'COGNITO_APP_CLIENT_ID': 'abcdef123456',  # client ID you wish to verify user is authenticated against
    'COGNITO_CHECK_TOKEN_EXPIRATION': False,  # disable token expiration checking for testing purposes
...
```

Sections: Initialization, Check Authentication, Restrict access by Cognito Group

</details>

### zope.container

Zope Container

`pip install zope.container` · installs (wheel) · licence: ZPL-2.1 · rank 12034 · last release 2026-08-20 · [PyPI](https://pypi.org/project/zope.container/) · [docs](https://zopecontainer.readthedocs.io) · [source](https://github.com/zopefoundation/zope.container)

<details><summary>README extract</summary>

This package define interfaces of container components, and provides
container implementations such as a BTreeContainer and
OrderedContainer, as well as the base class used by `zope.site.folder`
for the Folder implementation.

Documentation is hosted at

Sections: `zope.container`, 7.3 (2026-08-20), 7.2 (2025-11-15), 7.1 (2025-11-06), 7.0 (2025-09-12), 6.1 (2024-09-18), 6.0 (2024-05-29), 5.2 (2023-10-05), 5.1 (2023-04-24), 5.0 (2023-01-24), 4.10 (2022-11-17), 4.9 (2022-11-16), 4.8 (2022-11-06), 4.7 (2022-09-15)

</details>

### django-admin-csvexport

Django-admin-action to export items as csv-formatted data.

`pip install django-admin-csvexport` · installs (wheel) · licence: BSD-2-Clause · rank 12045 · last release 2026-01-15 · [PyPI](https://pypi.org/project/django-admin-csvexport/)

<details><summary>README extract</summary>

Django-admin-csvexport is a django-admin-action, that allows you to export the
items of your django-admin changelist as csv-formatted data.

Features:
* selectable model-fields
* related models included
* customizable csv-format
* view or download csv-data

Example:
```python
class MyModelAdmin(admin.ModelAdmin):
    csvexport_export_fields = [
        'field_a',
        'field_b,
        'relational_field.field_a_on_related_model',
        ...
    ]
    csvexport_selected_fields = [
        'field_a',
        'field_b,
        'relational_field.field_a_on_related_model',
        ...
    ]
```

Sections: Welcome to django-admin-csvexport, Description, Features, Configuration, Usage

</details>

### django-modeltree

TODO

`pip install django-modeltree` · installs (wheel) · licence: BSD License · rank 12053 · last release 2026-01-15 · [PyPI](https://pypi.org/project/django-modeltree/)

<details><summary>README extract</summary>

Do you have a model layout with various relations and looking for a way to
navigate it with ease? Then django-modeltree is what you are looking for. Build
your modeltree in a single line and accessing related models and their objects
in a elegant and performant way. No need for complex query building anymore.
Find out how this works here. ...

Sections: Welcome to django-modeltree, About, Links

</details>

### django-cryptography

Easily encrypt data in Django

`pip install django-cryptography` · installs (wheel) · licence: BSD License · rank 12069 · last release 2022-04-06 · [PyPI](https://pypi.org/project/django-cryptography/) · [docs](https://django-cryptography.readthedocs.io) · [source](https://github.com/georgemarshall/django-cryptography)

<details><summary>README extract</summary>

A set of primitives for easily encrypting data in Django, wrapping
the Python Cryptography library. Also provided is a drop in
replacement for Django's own cryptographic primitives, using
Cryptography as the backend provider.

Do not forget to read the documentation.

Example:
```python
from django.db import models

from django_cryptography.fields import encrypt

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    sensitive_data = encrypt(models.CharField(max_length=50))
```

Sections: Django Cryptography, Cryptography by example, Requirements

</details>

### mod-wsgi

Installer for Apache/mod_wsgi.

`pip install mod-wsgi` · installs from source (sdist only) · licence: Apache Software License · rank 12071 · last release 2026-10-13 · [PyPI](https://pypi.org/project/mod-wsgi/) · [docs](https://modwsgi.readthedocs.io/) · [source](https://github.com/GrahamDumpleton/mod_wsgi)

<details><summary>README extract</summary>

Overview

The mod_wsgi package provides an Apache module that implements a WSGI
compliant interface for hosting Python-based web applications on top of
the Apache web server, conforming to the WSGI specification (PEP 3333). ...

</details>

### django-cms

Lean enterprise content management powered by Django.

`pip install django-cms` · installs (wheel) · licence: BSD License · rank 12087 · last release 2026-09-23 · [PyPI](https://pypi.org/project/django-cms/) · [docs](https://docs.django-cms.org/) · [source](https://github.com/django-cms/django-cms)

<details><summary>README extract</summary>

Lean, open-source enterprise content management powered by Django.
Backed by the non-profit django CMS Association (Sponsor us).

This repository contains the core package published as `django-cms` on PyPI. ...

Features:
Build complex publishing workflows with simple, composable parts:

* robust internationalisation (i18n) and multi-site support
* front-end (inline) editing so editors can work directly on rendered pages
* a flexible placeholder and plugin system for ...

Sections: django CMS, Start here, Features, Test django CMS in our demo, Documentation, Getting Help, The django CMS Association

</details>

### django-memoize

An implementation of memoization technique for Django.

`pip install django-memoize` · installs from source (sdist only) · licence: BSD License · rank 12135 · last release 2020-04-27 · [PyPI](https://pypi.org/project/django-memoize/)

<details><summary>README extract</summary>

django-memoize

django-memoize is an implementation
of `memoization < technique
for Django. You can think of it as a cache for function or method results.

</details>

### djangorestframework-jwt

JSON Web Token based authentication for Django REST framework

`pip install djangorestframework-jwt` · installs (wheel) · licence: MIT License · rank 12146 · last release 2017-06-23 · [PyPI](https://pypi.org/project/djangorestframework-jwt/)

<details><summary>README extract</summary>

JSON Web Token Authentication support for Django REST Framework

Full documentation for the project is available at docs.

Features:
This package provides JSON Web Token Authentication support for
Django REST framework.

If you want to know more about JWT, check out the following resources:

- DjangoCon 2014 - JSON Web Tokens Video \| Slides
- Auth with JSON Web Tokens
- JWT.io

Sections: REST framework JWT Auth, Overview, Requirements

</details>

### zope.traversing

Resolving paths in the object hierarchy

`pip install zope.traversing` · installs (wheel) · licence: Zope Public License · rank 12175 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.traversing/)

<details><summary>README extract</summary>

This package provides adapters for resolving object paths by traversing
an object hierarchy. This package also includes support for traversal
namespaces (e.g. `++view++`, `++skin++`, etc.) as well as computing
URLs via the `@@absolute_url` view.

Documentation is hosted at

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: zope.traversing, Changes, 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0 (2023-03-27), 4.4.1 (2020-03-31), 4.4.0 (2020-03-30), 4.3.1 (2018-10-16), 4.3 (2018-10-05), 4.2.0 (2017-09-23), 4.1.0 (2016-08-05), 4.0.0 (2014-03-21), 4.0.0a3 (2013-03-12), 4.0.0a2 (2013-02-21)

</details>

### ignore

Download .gitignore files for a given language

`pip install ignore` · installs from source (sdist only) · licence: MIT License · rank 12186 · last release 2011-11-29 · [PyPI](https://pypi.org/project/ignore/)

<details><summary>README extract</summary>

Quickly grab common .gitignore files from the command line.

Sections: ignore, Usage

</details>

### aia

AIA chasing through OpenSSL for TLS certificate chain building and verifying

`pip install aia` · installs (wheel) · licence: BSD License · rank 12273 · last release 2021-11-27 · [PyPI](https://pypi.org/project/aia/)

<details><summary>README extract</summary>

This library was built as a workaround to the CPython
issue 18617
(AIA chasing for missing intermediate certificates on TLS connections)
regarding SSL/TLS.

Why a session?
That's not really a session in the HTTP sense,
it's just a way to cache the downloaded certificates in memory,
so one doesn't need to validate the same certificate more than ...

Example:
```python
from aia import AIASession
aia_session = AIASession()

# A GET result (only if status was 200), as bytes
content = aia_session.download("

# Return a `http.client.HTTPResponse` object, like `urllib.request.urlopen`
response = aia_session.urlopen("

# Indirectly, the same above
from urllib.request import urlopen
url = "
...
```

Sections: AIA Chasing in Python, How to use it?

</details>

### certbot-nginx

Nginx plugin for Certbot

`pip install certbot-nginx` · installs (wheel) · licence: Apache-2.0 · rank 12285 · last release 2026-10-29 · [PyPI](https://pypi.org/project/certbot-nginx/)

### django-rest-framework

alias.

`pip install django-rest-framework` · installs from source (sdist only) · licence: BSD · rank 12288 · last release 2017-07-20 · [PyPI](https://pypi.org/project/django-rest-framework/)

### matrx-scraper

Web scraping engine, HTML parsing, and search integration for the Matrx ecosystem

`pip install matrx-scraper` · installs (wheel) · licence: MIT License · rank 12289 · last release 2026-10-30 · [PyPI](https://pypi.org/project/matrx-scraper/) · [source](https://github.com/AI-Matrix-Engine/aidream-current)

<details><summary>README extract</summary>

Web scraping, HTML parsing, site crawling, headless-browser automation, and
search for Python. An 8-stage parser turns raw HTML into clean AI-ready content
plus structured extractions (tables, code blocks, categorized links, metadata,
schema.org). ...

Example:
```python
from matrx_scraper import scrape, scrape_many_stream, parse_html, audit_html

result = await scrape("
result.success           # bool  — outcome
result.failure_reason    # str | None
result.title
result.ai_content        # clean, AI-ready markdown
result.links             # links by category
result.tables            # parsed tables
...
```

Sections: matrx-scraper, Quickstart, Crawl a site, Drive a browser, Other clients, AI tools and MCP, Running the microservice, Extending it in a host, Documentation

</details>

### cent

Python SDK for Centrifugo's HTTP server API: API client, tokens, proxy handlers

`pip install cent` · installs (wheel) · licence: MIT · rank 12310 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cent/) · [docs](https://centrifugal.dev/docs/server/server_api)

<details><summary>README extract</summary>

Python SDK for the HTTP server API
of Centrifugo: every API method,
including those of Centrifugo PRO, in a blocking `Client` and an async
`AsyncClient`; connection, subscription and server API tokens; the proxy
handlers and the endpoints client SDKs call. For a real-time client over
WebSocket, see centrifuge-python.

| | Version | ...

Example:
```python
import os
import cent

client = cent.Client(" api_key=os.environ["CENTRIFUGO_API_KEY"])

res = client.publish(channel="news", data={"text": "hello"})
print(f"published at offset {res.offset}")
```

Sections: cent, Example, Payloads, Pages and stream positions, Timeouts, Errors, Retries, Broadcast and batch, Automatic batching, Authentication, HTTP client, tracing and metrics, Shutdown, HTTP handlers, Proxy

</details>

### zope.cachedescriptors

Method and property caching decorators

`pip install zope.cachedescriptors` · installs (wheel) · licence: Zope Public License · rank 12381 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.cachedescriptors/)

<details><summary>README extract</summary>

Cached descriptors cache their output. They take into account
instance attributes that they depend on, so when the instance
attributes change, the descriptors will change the values they
return.

Cached descriptors cache their data in v` attributes, so they are
also useful for managing the computation of volatile attributes for
persistent objects. ...

Example:
```python
>>> class Point:
...     def init(self, x, y):
...         self.x, self.y = x, y
...
...     @property.CachedProperty
...     def no_deps_no_parens(self):
...         print("No deps, no parens")
...         return 1
...
...     @property.CachedProperty()
...     def no_deps(self):
...         print("No deps")
...         return 2
...
...
```

...

</details>

### httpx2-pytest

Send responses to httpx2.

`pip install httpx2-pytest` · installs (wheel) · licence: MIT · rank 12387 · last release 2026-09-04 · [PyPI](https://pypi.org/project/httpx2-pytest/) · [docs](https://github.com/angryfoxx/httpx2-pytest#readme) · [source](https://github.com/angryfoxx/httpx2-pytest)

<details><summary>README extract</summary>

httpx2-pytest (this project) builds on the design and API of pytest-httpx by Colin Bounouar — the established pytest plugin for mocking HTTPX. That project defined the `httpx_mock` fixture and request-matching model many test suites already rely on. ...

Example:
```python
import httpx2

response = httpx2.get("
```

Sections: Send responses to HTTPX2 using pytest, HTTPX2 mocking options, About HTTPX2, Add responses, How response is selected, Matching on URL, Ignoring query parameters, Matching on query parameters, Matching on HTTP method, Matching on proxy URL, Matching on HTTP headers, Matching on HTTP body, Matching on HTTP JSON body, Matching on HTTP multipart body

</details>

### latest-user-agents

Get the latest user agent strings for major browsers and OSs

`pip install latest-user-agents` · installs from source (sdist only) · licence: MIT License · rank 12398 · last release 2025-01-24 · [PyPI](https://pypi.org/project/latest-user-agents/) · [source](https://github.com/jnrbsn/python-latest-user-agents)

<details><summary>README extract</summary>

_Get the latest user agent strings for major browsers and OSs

Example:
```python
In [1]: from latest_user_agents import get_latest_user_agents, get_random_user_agent

In [2]: get_latest_user_agents()
Out[2]:
['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0',
...
```

Sections: latest-user-agents, Basic usage, Bugs, requests, questions, etc.

</details>

### zapros

Modern and extensible HTTP client for Python.

`pip install zapros` · installs (wheel) · licence: MIT · rank 12493 · last release 2026-11-06 · [PyPI](https://pypi.org/project/zapros/) · [docs](https://zapros.dev) · [source](https://github.com/kap-sh/zapros)

<details><summary>README extract</summary>

/zəˈproʊz/ · the "za" from "bizarre" + "prose"

 ### Modern and extensible Python HTTP client

 Documentation

</details>

### zope.annotation

Object annotation mechanism

`pip install zope.annotation` · installs (wheel) · licence: Zope Public License · rank 12494 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.annotation/)

<details><summary>README extract</summary>

This package provides a mechanism to store additional information about
objects without need to modify object class.

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: `zope.annotation` README, Changes, 6.0 (2025-09-12), 5.2 (2025-08-06), 5.1 (2025-02-13), 5.0 (2023-03-27), 4.8 (2022-09-06), 4.7.0 (2018-10-16), 4.6.0 (2017-09-22), 4.5 (2017-06-03), 4.4.1 (2015-01-09), 4.4.0 (2015-01-09), 4.3.0 (2014-12-26), 4.2.0 (2013-03-18)

</details>

### drf-api-logger

The production standard for DRF API observability: request/response logging, profiling, masking, and admin analytics.

`pip install drf-api-logger` · installs (wheel) · licence: Apache-2.0 · rank 12496 · last release 2026-07-08 · [PyPI](https://pypi.org/project/drf-api-logger/) · [docs](https://github.com/vishalanandl177/DRF-API-Logger#readme) · [source](https://github.com/vishalanandl177/DRF-API-Logger)

<details><summary>README extract</summary>

The production standard for DRF API observability. Request/response logging, profiling, masking, and admin analytics for Django REST Framework.

Use `drf-api-logger` when you need to inspect DRF API calls without writing fragile custom middleware. ...

Features:
- Request/response logging: URL, method, headers, body, response, status code, client IP, execution time, and optional trace ID. ...

Example:
```python
from drf_api_logger import API_LOGGER_SIGNAL

# Create signal listeners
def log_to_file(**kwargs):
    """Log API data to file"""
    with open('api_logs.json', 'a') as f:
        json.dump(kwargs, f)
        f.write('\n')

def send_to_analytics(**kwargs):
    """Send API data to analytics service"""
    analytics_service.track_api_call(
...
```

...

</details>

### recipe-scrapers

Python package, scraping recipes from all over the internet

`pip install recipe-scrapers` · installs (wheel) · licence: MIT License · rank 12497 · last release 2026-10-18 · [PyPI](https://pypi.org/project/recipe-scrapers/)

<details><summary>README extract</summary>

- Documentation
- Supported Sites
- Contributing Guide
- Issue Tracker
- Share Project Ideas

A Python package for extracting recipe data from cooking websites. Parses recipe information from
either standard HTML structure,
Schema markup (including JSON-LD, Microdata, and RDFa formats) or
OpenGraph metadata. ...

Example:
```python
from recipe_scrapers import scrape_me

scraper = scrape_me("
scraper.title()
scraper.instructions()
scraper.to_json()
# for a complete list of methods:
# help(scraper)
```

Sections: recipe-scrapers, Quick Links, Basic Usage, Special Thanks, Share Your Project

</details>

### flup

Random assortment of WSGI servers (py3)

`pip install flup` · installs (wheel) · licence: BSD License · rank 12567 · last release 2018-02-07 · [PyPI](https://pypi.org/project/flup/)

### uwsgidecorators

uwsgidecorators standalone package

`pip install uwsgidecorators` · installs from source (sdist only) · licence: MIT License · rank 12575 · last release 2014-11-05 · [PyPI](https://pypi.org/project/uwsgidecorators/)

<details><summary>README extract</summary>

uwsgidecorators ( module on Pypi.
People asked for it and here it is.

</details>

### django-enumfields

Real Python Enums for Django.

`pip install django-enumfields` · installs (wheel) · licence: MIT License · rank 12577 · last release 2021-02-23 · [PyPI](https://pypi.org/project/django-enumfields/)

<details><summary>README extract</summary>

This package lets you use real Python (PEP435-style) enums with Django.

Example:
```python
class MyForm(forms.Form):

    color = EnumField(Color, max_length=1).formfield()
```

Sections: Included Tools, EnumField, EnumIntegerField, Usage in Forms, Enum, EnumFieldListFilter, Django Rest Framework integration

</details>

### tabulator

Consistent interface for stream reading and writing tabular data (csv/xls/json/etc)

`pip install tabulator` · installs (wheel) · licence: MIT License · rank 12580 · last release 2021-03-21 · [PyPI](https://pypi.org/project/tabulator/)

<details><summary>README extract</summary>

A library for reading and writing tabular data (csv/xls/json/etc).

> [Important Notice] We have released Frictionless Framework. This framework is logical continuation of `tabulator` that was extended to be a complete data solution. The change in not breaking for the existing software so no actions are required. ...

Features:
- Supports most common tabular formats: CSV, XLS, ODS, JSON, Google Sheets, SQL, and others. See complete list below.
- Loads local and remote data: Supports HTTP, FTP and S3. ...

Example:
```python
from tabulator import Stream

with Stream('data.csv', headers=1) as stream:
    stream.headers # [header1, header2, ..]
    for row in stream:
        print(row)  # [value1, value2, ..]
```

...

</details>

### djangocms-admin-style

Adds pretty CSS styles for the django CMS admin interface.

`pip install djangocms-admin-style` · installs (wheel) · licence: BSD License · rank 12605 · last release 2024-02-29 · [PyPI](https://pypi.org/project/djangocms-admin-style/)

<details><summary>README extract</summary>

Adds pretty CSS styles for the django CMS admin interface. Supports optional
`django-admin-shortcuts` package.

+---------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| .. image:: | .. ...

Example:
```python
// Show widget in CMS colors if djangocms-admin-style is installed
.djangocms-admin-style #my-widget {
    color:  var(--dca-primary, black);
}
```

Sections: django CMS Admin Style, Documentation, Configuration, Extending styles in your own app, Running Tests

</details>

### dockerflow

Python tools and helpers for Mozilla's Dockerflow

`pip install dockerflow` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 12608 · last release 2026-03-04 · [PyPI](https://pypi.org/project/dockerflow/)

<details><summary>README extract</summary>

This package implements a few helpers and tools for Mozilla's
Dockerflow pattern.
The documentation can be found on python-dockerflow.readthedocs.io

Sections: Python Dockerflow, Issues & questions

</details>

### zope.size

Interfaces and simple adapter that give the size of an object

`pip install zope.size` · installs (wheel) · licence: Zope Public License · rank 12620 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.size/)

<details><summary>README extract</summary>

This package provides a definition of simple interface that allows
applications to retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the `getSize`
method that returns size in bytes. ...

Sections: `zope.size`, Changes, 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0 (2023-06-30), 4.4 (2022-08-30), 4.3 (2018-10-05), 4.2.0 (2017-07-27), 4.1.0 (2014-12-29), 4.0.1 (2013-03-08), 4.0.0 (2013-02-13), 3.5.0 (2011-11-29), 3.4.1 (2009-09-10), 3.4.0 (2006-09-29)

</details>

### django-analytical

Analytics service integration for Django projects

`pip install django-analytical` · installs (wheel) · licence: MIT · rank 12655 · last release 2025-07-10 · [PyPI](https://pypi.org/project/django-analytical/) · [docs](https://django-analytical.readthedocs.io/)

<details><summary>README extract</summary>

The django-analytical application integrates analytics services into a
Django project.

Using an analytics service with a Django project means adding Javascript
tracking code to the project templates. Of course, every service has
its own specific installation instructions. ...

</details>

### zope.tal

Zope Template Application Language (TAL)

`pip install zope.tal` · installs (wheel) · licence: Zope Public License · rank 12656 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.tal/)

<details><summary>README extract</summary>

The Zope3 Template Attribute Languate (TAL) specifies the custom namespace
and attributes which are used by the Zope Page Templates renderer to inject
dynamic markup into a page. It also includes the Macro Expansion for TAL
(METAL) macro language used in page assembly. ...

Sections: zope.tal, Changes, 6.0 (2025-09-12), 5.1.1 (2025-08-14), 5.1 (2025-02-14), 5.0.1 (2023-01-23), 5.0 (2023-01-19), 4.5 (2021-05-28), 4.4 (2018-10-05), 4.3.1 (2018-03-21), 4.3.0 (2017-08-08), 4.2.0 (2016-04-12), 4.1.1 (2015-06-05), 4.1.0 (2014-12-19)

</details>

### django-sri

Subresource Integrity for Django

`pip install django-sri` · installs (wheel) · licence: BSD-3-Clause · rank 12664 · last release 2026-09-22 · [PyPI](https://pypi.org/project/django-sri/) · [source](https://github.com/RealOrangeOne/django-sri)

<details><summary>README extract</summary>

Subresource Integrity for Django.

Example:
```python
from pathlib import Path
from sri import get_sri, get_sri_of_static

get_sri(Path("/path/to/myfile.txt"))  # "sha256-..."
get_sri(Path("/path/to/myfile.txt"), "sha512")  # "sha512-..."

get_sri_of_static("index.js")  # "sha256-..."
get_sri_of_static("index.js", "sha512")  # "sha512-..."
```

Sections: Django SRI, Usage, Template Tags, Algorithms, API, _"Does this work with whitenoise or alike?"_, `jinja2`

</details>

### zope.site

Local registries for zope component architecture

`pip install zope.site` · installs (wheel) · licence: Zope Public License · rank 12666 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.site/)

<details><summary>README extract</summary>

This package provides a local and persistent site manager
implementation, so that one can register local utilities and
adapters. It uses local adapter registries for its adapter and utility
registry. The module also provides some facilities to organize the
local software and ensures the correct behavior inside the ZODB.

Documentation is hosted at

Example:
```python
         _ global site _
        /                       \
    myfolder                 myfolder2
        |
    myfolder11

>>> myfolder2 = folder.rootFolder()
>>> myfolder2.setSiteManager(site.LocalSiteManager(myfolder2))
```

...

</details>

### oidc-provider-mock

OpenID Connect provider server for testing authentication

`pip install oidc-provider-mock` · installs (wheel) · licence: MIT · rank 12672 · last release 2026-10-04 · [PyPI](https://pypi.org/project/oidc-provider-mock/) · [docs](https://github.com/geigerzaehler/oidc-provider-mock) · [source](https://github.com/geigerzaehler/oidc-provider-mock)

<details><summary>README extract</summary>

<!-- THIS FILE HAS BEEN GENERATED FROM REAMDE.md.tpl -->

[][docs]

> A mock OpenID Provider server to test and develop OpenID Connect
> authentication.

You can find the full documentation here.

Example:
```python
@pytest.fixture
def oidc_server():
    with oidc_provider_mock.run_server_in_thread() as server:
        yield f"

def test_auth_code_login(client: flask.testing.FlaskClient, oidc_server: str):
    # Add OIDC claims for the user we want to authenticate
    response = httpx2.put(
        f"{oidc_server}/users/{quote('alice@example.com')}",
...
```

Sections: OpenID Provider Mock, Usage, Alternatives

</details>

### zope.filerepresentation

File-system Representation Interfaces

`pip install zope.filerepresentation` · installs (wheel) · licence: Zope Public License · rank 12686 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.filerepresentation/)

<details><summary>README extract</summary>

The interfaces defined here are used for file-system and file-system-like
representations of objects, such as file-system synchronization, FTP, PUT, and
WebDAV.

Documentation is hosted at

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: `zope.filerepresentation`, Changes, 7.0 (2025-09-12), 6.1 (2025-02-14), 6.0 (2023-01-14), 5.0.0 (2020-03-31), 4.2.0 (2017-08-10), 4.1.0 (2014-12-27), 4.0.2 (2013-03-08), 4.0.1 (2013-02-11), 4.0.0 (2013-02-11), 3.6.1 (2011-11-29), 3.6.0 (2009-10-08), 3.5.0 (2009-01-31)

</details>

### blacksheep

Fast web framework for Python asyncio

`pip install blacksheep` · installs (wheel) · licence: MIT · rank 12700 · last release 2026-10-11 · [PyPI](https://pypi.org/project/blacksheep/) · [docs](https://www.neoteroi.dev/blacksheep/) · [source](https://github.com/Neoteroi/BlackSheep)

<details><summary>README extract</summary>

BlackSheep is an asynchronous web framework to build event based web
applications with Python. It is inspired by
Flask, ASP.NET
Core, and the work by Yury
Selivanov.

Example:
```python
from datetime import datetime, timezone

from blacksheep import Application, get

app = Application()

@get("/")
async def home():
    return f"Hello, World! {datetime.now(timezone.utc).isoformat()}"
```

Sections: BlackSheep, Getting started using the CLI ✨, Dependencies, Getting started with the documentation, Requirements, Automatic bindings and dependency injection, Generation of OpenAPI Documentation, Web framework features, Client features, Documentation, Branches

</details>

### highcharts-core

High-end Data Visualization for the Python Ecosystem. Official wrapper for Highcharts Core (JS).

`pip install highcharts-core` · installs (wheel) · licence: Other/Proprietary License · rank 12703 · last release 2026-05-19 · [PyPI](https://pypi.org/project/highcharts-core/) · [docs](https://core-docs.highchartspython.com/en/latest/) · [source](https://github.com/highcharts-for-python/highcharts-core)

<details><summary>README extract</summary>

High-end data visualization for the Python ecosystem

Highcharts Core for Python is a Python library that provides a Python wrapper
for the Highcharts Core JavaScript data
visualization library, with full integration into the robust Python ecosystem, including:

 * Jupyter Labs/Notebook. ...

Features:
Highcharts is the world's most popular, most powerful,
category-defining JavaScript data visualization library. If you are building a web or
mobile app/dashboard that will be visualizing data in some fashion, you should
absolutely take a look at the ...

Example:
```python
# PRECISE-LOCATION PATTERN: BEST PRACTICE!
# This method of importing Highcharts for Python objects yields the fastest
# performance for the import statement. However, it is more verbose and requires
...

</details>

### gsheets

Pythonic wrapper for the Google Sheets API

`pip install gsheets` · installs (wheel) · licence: MIT License · rank 12730 · last release 2022-06-12 · [PyPI](https://pypi.org/project/gsheets/) · [docs](https://gsheets.readthedocs.io)

<details><summary>README extract</summary>

`gsheets` is a small wrapper around the Google Sheets API (v4) to provide
more convenient access to Google Sheets from Python scripts.

Turn on the API, download an OAuth client ID as JSON file, and create a
`Sheets object from it. Use its index access (_getitem__`) to retrieve
SpreadSheet objects by their id, or use `.get()` with a sheet URL. ...

Example:
```python
>>> from gsheets import Sheets

>>> sheets = Sheets.from_files('~/client_secrets.json', '~/storage.json')
>>> sheets  #doctest: +ELLIPSIS
<gsheets.api.Sheets object at 0x...>
```

Sections: gsheets, Links, Quickstart, See also

</details>

### pymobiledetect

Detect mobile and tablet browsers

`pip install pymobiledetect` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 12743 · last release 2018-05-10 · [PyPI](https://pypi.org/project/pymobiledetect/)

_README extract left out: share-alike licence._

### zope.processlifetime

Zope process lifetime events

`pip install zope.processlifetime` · installs (wheel) · licence: ZPL-2.1 · rank 12766 · last release 2026-11-05 · [PyPI](https://pypi.org/project/zope.processlifetime/) · [docs](https://zopeprocesslifetime.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.processlifetime)

<details><summary>README extract</summary>

This package provides interfaces / implementations for events relative
to the lifetime of a server process (startup, database opening, etc.)
These events are usually used with zope.event.

Documentation is hosted at

- Add support for Python 3.15.

- Add support for Python 3.14.

- Drop support for Python 3.10.

- Drop support for Python 3.9. ...

Sections: `zope.processlifetime`, Changes, 4.1 (2026-11-05), 4.0 (2025-09-12), 3.1 (2025-02-14), 3.0 (2023-03-27), 2.4 (2022-08-26), 2.3.0 (2018-10-05), 2.2.0 (2017-09-01), 2.1.0 (2014-12-27), 2.0.0 (2013-02-22), 1.0 (2009-05-13)

</details>

### zope.pagetemplate

Zope Page Templates

`pip install zope.pagetemplate` · installs (wheel) · licence: Zope Public License · rank 12777 · last release 2025-11-21 · [PyPI](https://pypi.org/project/zope.pagetemplate/)

<details><summary>README extract</summary>

Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

Page Templates are based on a Template Attribute Language with expressions provided by
TALES. ...

Sections: zope.pagetemplate, Changes, 6.1 (2025-11-21), 6.0 (2025-09-12), 5.2 (2025-08-06), 5.1 (2024-02-08), 5.0 (2023-02-07), 4.6.0 (2021-11-04), 4.5.0 (2020-02-10), 4.4.1 (2018-10-16), 4.4 (2018-10-05), 4.3.0 (2017-09-04), 4.2.1 (2015-06-06), 4.2.0 (2015-06-02)

</details>

### dry-rest-permissions

Rules based permissions for the Django Rest Framework

`pip install dry-rest-permissions` · installs (wheel) · licence: BSD License · rank 12794 · last release 2018-01-31 · [PyPI](https://pypi.org/project/dry-rest-permissions/)

### zope.tales

Zope Template Application Language Expression Syntax (TALES)

`pip install zope.tales` · installs (wheel) · licence: Zope Public License · rank 12811 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.tales/) · [docs](https://zopetales.readthedocs.io/)

<details><summary>README extract</summary>

`zope.tales` (Template Attribute Language - Expression Syntax) is an
expression language designed to work with zope.tal (although it can be used
independently). The two are integrated to produce page templates in
zope.pagetemplate.

The specification for TAL and TALES can be found at

Documentation on this implementation and its API can be found at

Sections: zope.tales, Changes, 7.0 (2025-09-12), 6.1 (2025-02-14), 6.0 (2023-07-12), 5.2 (2022-08-24), 5.1 (2020-07-06), 5.0.2 (2020-03-27), 5.0.1 (2019-06-26), 5.0 (2019-04-08), 4.3 (2018-10-05), 4.2.0 (2017-09-22), 4.1.1 (2015-06-06), 4.1.0 (2014-12-29)

</details>

### dicomweb-client

Client for DICOMweb RESTful services.

`pip install dicomweb-client` · installs (wheel) · licence: MIT License · rank 12854 · last release 2026-08-17 · [PyPI](https://pypi.org/project/dicomweb-client/) · [docs](https://dicomweb-client.readthedocs.io/) · [source](https://github.com/ImagingDataCommons/dicomweb-client.git)

<details><summary>README extract</summary>

Python client for DICOMweb services.

Please refer to the online documentation at dicomweb-client.readthedocs.io, which includes a user guide with examples, a developer guide, and complete documentation of the application programming interface of the `dicomweb_client` Python package as well as the command line interface of the `dicomweb_client` ...

Sections: DICOMweb Client, Documentation

</details>

### socid-extractor

Extract accounts' identifiers and metadata from personal pages on various platforms.

`pip install socid-extractor` · installs (wheel) · licence: MIT · rank 12872 · last release 2026-07-13 · [PyPI](https://pypi.org/project/socid-extractor/) · [source](https://github.com/soxoj/socid-extractor)

<details><summary>README extract</summary>

> Turn any public profile page into a structured account record — usernames, display names, bios, avatars, locations, joined-at dates, follower counts, external links, and the stable internal identifiers that uniquely pin an account across renames, redesigns, and deletions. ...

Example:
```python
import requests
import socid_extractor

r = requests.get('
print(socid_extractor.extract(r.text))
# {'patreon_id': '33913189', 'patreon_username': 'annetlovart',
# 'fullname': 'Annet Lovart',
# 'links': "[' ...]"}
```

Sections: socid_extractor, Quick start, Use cases, Commercial Use, SOWEL classification, Tools using socid_extractor

</details>

### zope.testbrowser

Programmable browser for functional black-box tests

`pip install zope.testbrowser` · installs (wheel) · licence: Zope Public License · rank 12928 · last release 2026-10-19 · [PyPI](https://pypi.org/project/zope.testbrowser/) · [docs](https://zopetestbrowser.readthedocs.io/)

<details><summary>README extract</summary>

`zope.testbrowser` provides an easy-to-use programmable web browser
with special focus on testing. It is used in Zope, but it's not Zope
specific at all. For instance, it can be used to test or otherwise
interact with any web site.

Documentation is available at:

- Add support for Python 3.14, 3.15.

- Drop support for Python 3.9, 3.10. ...

Example:
```python
    # my/package/tests.py
    from zope.app.testing.functional import defineLayer
    from zope.app.testing.functional import FunctionalDocFileSuite
    defineLayer('MyFtestLayer', 'ftesting.zcml', allow_teardown=True)

    def test_suite():
        suite = FunctionalDocFileSuite('test.txt', ...)
        suite.layer = MyFtestLayer
...
```

...

</details>

### onetimepass

Module for generating and validating HOTP and TOTP tokens

`pip install onetimepass` · installs from source (sdist only) · licence: MIT License · rank 12931 · last release 2015-07-31 · [PyPI](https://pypi.org/project/onetimepass/)

<details><summary>README extract</summary>

Current development release: onetimepass-master.tar.gz

Example:
```python
import onetimepass as otp
my_secret = 'MFRGGZDFMZTWQ2LK'
my_token = otp.get_totp(my_secret)
```

Sections: Versions, What is OneTimePass, How to use OneTimePass

</details>

### Zope

Zope application server / web framework

`pip install Zope` · installs (wheel) · licence: ZPL-2.1 · rank 12939 · last release 2026-10-22 · [PyPI](https://pypi.org/project/Zope/) · [docs](https://zope.readthedocs.io) · [source](https://github.com/zopefoundation/Zope)

<details><summary>README extract</summary>

Zope is an open-source web application server.

This document provides some general information about Zope and provides
links to other documents. The full documentation can be found at

Sections: Bug tracker, 6.3 (2026-10-22), 6.2 (2026-08-05), 6.1 (2026-04-22), 6.0 (2026-03-04), 6.0b2 (2026-01-15), 6.0b1 (2025-11-22)

</details>

### zope.contentprovider

Content Provider Framework for Zope Templates

`pip install zope.contentprovider` · installs (wheel) · licence: ZPL-2.1 · rank 12951 · last release 2026-10-23 · [PyPI](https://pypi.org/project/zope.contentprovider/) · [docs](https://zopecontentprovider.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.contentprovider)

<details><summary>README extract</summary>

This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content provider
objects are dynamically looked up based on the setup/configuration of the
application.

Detailed documentation is available at ...

Sections: zope.contentprovider, Changes, 7.1 (2026-10-22), 7.0 (2025-09-12), 6.1 (2025-07-23), 6.0 (2024-06-07), 5.0 (2023-04-14), 4.2.1 (2018-11-08), 4.2 (2018-10-05), 4.1.0 (2017-08-08), 4.0.0 (2014-12-24), 4.0.0a1 (2013-02-22), 3.7.2 (2010-05-25), 3.7.1 (2010-04-30)

</details>

### zope.browserpage

ZCML directives for configuring browser views for Zope.

`pip install zope.browserpage` · installs (wheel) · licence: Zope Public License · rank 12989 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.browserpage/)

<details><summary>README extract</summary>

This package provides ZCML directives for configuring browser views.
More specifically it defines the following ZCML directives:

- `browser:page`
- `browser:pages`
- `browser:view`

These directives also support menu item registration for pages, when
`zope.browsermenu` package is installed. Otherwise, they simply ignore
the menu attribute. ...

Sections: `zope.browserpage`, Changes, 6.0 (2025-09-12), 5.1 (2025-06-26), 5.0 (2023-01-19), 4.4.0 (2019-06-18), 4.3.0 (2018-10-05), 4.2.0 (2017-08-02), 4.1.0 (2014-12-24), 4.1.0a1 (2013-02-22), 4.0.0 (2012-07-04), 3.12.2 (2010-05-24), 3.12.1 (2010-04-30), 3.12.0 (2010-04-26)

</details>

### zope.browserresource

Browser resources implementation for Zope.

`pip install zope.browserresource` · installs (wheel) · licence: ZPL-2.1 · rank 12995 · last release 2026-11-06 · [PyPI](https://pypi.org/project/zope.browserresource/) · [docs](https://zopebrowserresource.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.browserresource/)

<details><summary>README extract</summary>

This package provides an implementation of browser resources. It also
provides directives for defining those resources using ZCML.

Resources are static files and directories that are served to the browser
directly from the filesystem. The most common example are images, CSS style
sheets, or JavaScript files. ...

Sections: zope.browserresource, Changes, 6.1 (2026-11-06), 6.0 (2025-09-12), 5.2 (2025-02-14), 5.1 (2023-08-28), 5.0 (2023-02-14), 4.4 (2019-12-10), 4.3 (2018-10-05), 4.2.1 (2017-09-01), 4.2.0 (2017-08-04), 4.1.0 (2014-12-26), 4.0.2 (2014-11-04), 4.0.1 (2013-04-03)

</details>

### PasteScript

A pluggable command-line frontend, including commands to setup package file layouts

`pip install PasteScript` · installs (wheel) · licence: MIT License · rank 13050 · last release 2025-01-22 · [PyPI](https://pypi.org/project/PasteScript/)

<details><summary>README extract</summary>

PasteScript is a pluggable command-line tool.

Note: Paste Script is being maintained on life support. That
means that critical bugs will be fixed, and support for new versions
of Python will be handled, but other than that new features are not
being considered. ...

</details>

### zope.viewlet

Zope Viewlets

`pip install zope.viewlet` · installs (wheel) · licence: ZPL-2.1 · rank 13094 · last release 2026-11-05 · [PyPI](https://pypi.org/project/zope.viewlet/) · [docs](https://zopeviewlet.readthedocs.io/) · [source](https://github.com/zopefoundation/zope.viewlet)

<details><summary>README extract</summary>

Viewlets provide a generic framework for building pluggable user
interfaces. Viewlets are a special type of content provider that allows a
template to define a region (a "viewlet manager") into which content
("viewlets") can be plugged.

Documentation is hosted at

- Add support for Python 3.15.

- Drop support for Python 3.10. ...

Sections: zope.viewlet, Changes, 6.1 (2026-11-05), 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0 (2023-03-27), 4.3 (2022-03-18), 4.2.1 (2018-12-17), 4.2 (2018-10-09), 4.1.0 (2017-09-23), 4.0.0 (2014-12-24), 4.0.0a1 (2013-02-24), 3.7.2 (2010-05-25), 3.7.1 (2010-04-30)

</details>

### zope.datetime

Zope datetime

`pip install zope.datetime` · installs (wheel) · licence: Zope Public License · rank 13132 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.datetime/)

<details><summary>README extract</summary>

Functions to parse and format date/time strings in common formats.

The documentation is hosted at

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: `zope.datetime`, CHANGES, 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0.0 (2023-04-25), 4.3.0 (2021-02-26), 4.2.0 (2017-08-14), 4.1.0 (2014-12-26), 4.0.0 (2013-02-19), 3.4.1 (2011-11-29), 3.4.0 (2007-07-20)

</details>

### archivebox

Self-hosted internet archiving solution.

`pip install archivebox` · installs (wheel) · licence: MIT License · rank 13151 · last release 2026-10-27 · [PyPI](https://pypi.org/project/archivebox/) · [docs](https://github.com/ArchiveBox/ArchiveBox/wiki) · [source](https://github.com/ArchiveBox/ArchiveBox)

<details><summary>README extract</summary>

Open-source self-hosted web archiving.

▶️ Quickstart | Demo | GitHub | Documentation | Info & Motivation | Community

ArchiveBox is a self-hosted app that lets you preserve content from websites in a variety of formats.

We aim to make your data immediately useful, and kept in formats that other programs can read directly. ...

Features:
- Free & open source, own your own data & maintain your privacy by self-hosting
- Powerful CLI with modular dependencies and support for Google Drive/NFS/SMB/S3/B2/etc.
- Comprehensive documentation, active development, and rich community ...

...

</details>

### django-admin-json-editor

A simple Django app to add JSON widget into Django Administration.

`pip install django-admin-json-editor` · installs from source (sdist only) · licence: MIT License · rank 13152 · last release 2020-05-27 · [PyPI](https://pypi.org/project/django-admin-json-editor/)

<details><summary>README extract</summary>

Application adds support for editing JSONField in Django Administration via

Example:
```python
class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = 'all'
        widgets = {
            'data': JSONEditorWidget(DATA_SCHEMA, collapsed=False),
        }
```

Sections: Django Administration JSON Editor, Quick start, Dynamic schema

</details>

### Flask-Security

Quickly add security features to your Flask application.

`pip install Flask-Security` · installs (wheel) · licence: MIT License · rank 13157 · last release 2026-10-21 · [PyPI](https://pypi.org/project/Flask-Security/) · [docs](https://flask-security.readthedocs.io) · [source](https://github.com/pallets-eco/flask-security)

### featrixsphere

Transform any CSV into a production-ready ML model in minutes, not months.

`pip install featrixsphere` · installs (wheel) · licence: MIT License · rank 13162 · last release 2026-11-06 · [PyPI](https://pypi.org/project/featrixsphere/) · [docs](https://github.com/Featrix/sphere#readme) · [source](https://github.com/Featrix/sphere)

<details><summary>README extract</summary>

Transform any CSV into a production-ready ML model in minutes, not months.

The Featrix Sphere API automatically builds neural embedding spaces from your data and trains high-accuracy predictors without requiring any ML expertise. Just upload your data, specify what you want to predict, and get a production API endpoint. ...

Example:
```python
# Option A: Upload CSV file
fm = featrix.create_foundational_model(
    name="my_model",
    data_file="your_data.csv"
)

# Option B: Upload DataFrame directly (no CSV file needed!)
import pandas as pd
df = pd.read_csv("your_data.csv")  # or create/modify DataFrame however you want
fm = featrix.create_foundational_model(name="my_model", df=df)

...
```

...

</details>

### WTForms-Components

Additional fields, validators and widgets for WTForms.

`pip install WTForms-Components` · installs (wheel) · licence: BSD License · rank 13190 · last release 2024-11-15 · [PyPI](https://pypi.org/project/WTForms-Components/)

<details><summary>README extract</summary>

WTForms-Components

Additional fields, validators and widgets for WTForms.

</details>

### django-service-objects

Service objects for Django

`pip install django-service-objects` · installs (wheel) · licence: MIT License · rank 13203 · last release 2022-02-24 · [PyPI](https://pypi.org/project/django-service-objects/)

<details><summary>README extract</summary>

[][build-status-link]
[][python-support-link]
[][django-link]
[][license-link]

Service objects for Django

This is a small library providing a `Service` base class to derive your service objects from. ...

Example:
```python
from django import forms

from service_objects.services import Service

class CreateUser(Service):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)
    subscribe_to_newsletter = forms.BooleanField(required=False)

    def process(self):
        email = self.cleaned_data['email']
...
```

Sections: django-service-objects [][latest-version-link], What?, Example, Documentation

</details>

### python-coveralls

Python interface to coveralls.io API

`pip install python-coveralls` · installs (wheel) · licence: Apache Software License · rank 13204 · last release 2019-08-01 · [PyPI](https://pypi.org/project/python-coveralls/)

<details><summary>README extract</summary>

This package provides a module to interface with the API.

Sections: Python interface to coveralls.io API, CONFIGURATION, TRAVIS.YML, COVERALLS OPTIONS

</details>

### pyrabbit2

A Pythonic interface to the RabbitMQ Management HTTP API

`pip install pyrabbit2` · installs (wheel) · licence: MIT License · rank 13248 · last release 2019-01-24 · [PyPI](https://pypi.org/project/pyrabbit2/)

<details><summary>README extract</summary>

Fork module to communicate the RabbitMQ HTTP Management API

The main documentation lives at

There's no way to easily write programs against RabbitMQs management API
without resorting to some messy urllib boilerplate code involving HTTP
Basic authentication and parsing the JSON responses, etc. ...

</details>

### HTMLCompare

library to compare HTML while ignoring non-functional differences

`pip install HTMLCompare` · installs (wheel) · licence: MIT · rank 13266 · last release 2026-09-19 · [PyPI](https://pypi.org/project/HTMLCompare/) · [source](https://github.com/FelixSchwarz/htmlcompare)

<details><summary>README extract</summary>

A Python library to check whether two HTML documents are "the same". It ignores
differences which do not change what the document means, so a test does not fail
just because a template engine emitted the attributes in a different order or
wrote `margin: 0px` instead of `margin: 0`.

Usage ...

Example:
```python
import htmlcompare

result = htmlcompare.compare_html(expected_html, actual_html)
if not result:
    print(result)
```

</details>

### shinyswatch

Bootswatch + Bootstrap 5 themes for Shiny.

`pip install shinyswatch` · installs (wheel) · licence: MIT License · rank 13273 · last release 2026-10-29 · [PyPI](https://pypi.org/project/shinyswatch/) · [source](https://github.com/rstudio/py-shinyswatch)

<details><summary>README extract</summary>

<!-- DO NOT EDIT BY HAND: Edit docs/index.qmd and run `make docs-readme` to update -->

Bootswatch + Bootstrap 5 themes for
Shiny.

Here are just three of the 25 themes in shinyswatch:

| Minty | Sketchy | Superhero |

| | | |

Example:
```python
from shiny import App, Inputs, Outputs, Session, render, ui

import shinyswatch

app_ui = ui.page_fluid(
    ui.input_slider("num", "Number:", min=10, max=100, value=30),
    ui.output_text_verbatim("slider_val"),
    theme=shinyswatch.theme.darkly,  # <- Use a shinyswatch theme here
)

def server(input: Inputs, output: Outputs, session: Session):
...
```

Sections: shinyswatch, Usage, Theme picker, Plot Theming, Examples

</details>

### python-cas

Python CAS client library

`pip install python-cas` · installs (wheel) · licence: MIT License · rank 13282 · last release 2026-05-05 · [PyPI](https://pypi.org/project/python-cas/)

<details><summary>README extract</summary>

`Python CAS` implements CAS protocol (Central Authentication Service) client.

This project was started by refactoring out CASClient classes from the
django-cas-ng project.

Now CASClient can be used by any python project,
e.g. Django, Pyramid, Flask, Sanic, FastAPI, Tornado, web2py etc.

Features:
- Support Client part of CAS version 1.0, 2.0 and 3.0.
- Support Python 3.10+

Sections: Python CAS, Features, Documentation, References

</details>

### zope.ptresource

Page template resource plugin for zope.browserresource

`pip install zope.ptresource` · installs (wheel) · licence: Zope Public License · rank 13284 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.ptresource/)

<details><summary>README extract</summary>

This package provides a "page template" resource class, a resource
whose content is processed with the Zope Page Templates engine before
being returned to client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in the package's `configure.zcml` file. ...

Sections: zope.ptresource, Changes, 6.0 (2025-09-12), 5.1 (2025-02-14), 5.0 (2023-03-27), 4.3.0 (2021-12-15), 4.2.0 (2018-10-05), 4.1.0 (2017-08-31), 4.0.0 (2014-12-24), 4.0.0a1 (2013-02-25), 3.9.0 (2009-08-27)

</details>

### api-client-pydantic

API Client extension for validate and transform requests / responses using pydantic.

`pip install api-client-pydantic` · installs (wheel) · licence: MIT License · rank 13285 · last release 2024-12-15 · [PyPI](https://pypi.org/project/api-client-pydantic/) · [source](https://github.com/mom1/api-client-pydantic)

<details><summary>README extract</summary>

Example:
```python
from apiclient_pydantic import serialize, serialize_all_methods

# serialize request and response data
@serialize(config: Optional[ConfigDict] = None, validate_return: bool = True, response: Optional[Type[BaseModel]] = None)

# wraps all local methods of a class with a decorator 'serialize'.
...
```

Sections: Python API Client Pydantic Extension, Usage, Related projects, apiclient-pydantic-generator - Now deprecated.

</details>

### asyncwhois

Python WHOIS and RDAP utility for querying and parsing information about Domains, IPv4s, IPv6s, and AS numbers.

`pip install asyncwhois` · installs (wheel) · licence: MIT License · rank 13300 · last release 2026-10-02 · [PyPI](https://pypi.org/project/asyncwhois/)

<details><summary>README extract</summary>

`asyncwhois` | Python utility for WHOIS and RDAP queries.

Example:
```python
import asyncio
from pprint import pprint

import asyncwhois

# pick a domain
domain = 'bitcoin.org'
# domain could also be a URL; asyncwhois uses tldextract to parse the URL
# domain = '

# basic example
query_string, parsed_dict = asyncwhois.whois(domain)
# query_string  # The semi-free text output from the whois server
...
```

Sections: asyncwhois, Quickstart, RDAP, Proxies, Exported Functions

</details>

### zope.browsermenu

Browser menu implementation for Zope.

`pip install zope.browsermenu` · installs (wheel) · licence: Zope Public License · rank 13328 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.browsermenu/)

<details><summary>README extract</summary>

This package provides an implementation of browser menus and ZCML directives
for configuring them.

- Replace `pkg_resources` namespace with PEP 420 native namespace.

Sections: `zope.browsermenu`, Changes, 6.0 (2025-09-12), 5.1 (2025-02-13), 5.0 (2023-02-08), 4.4 (2018-10-05), 4.3.0 (2017-08-03), 4.2.0 (2017-05-28), 4.1.1 (2015-06-05), 4.1.0 (2014-12-24), 4.1.0a1 (2013-02-22), 4.0.0 (2012-07-04), 3.9.1 (2010-04-30), 3.9.0 (2009-08-27)

</details>

### starlette-graphene3

Use Graphene v3 on Starlette

`pip install starlette-graphene3` · installs (wheel) · licence: MIT License · rank 13361 · last release 2022-06-01 · [PyPI](https://pypi.org/project/starlette-graphene3/) · [source](https://github.com/ciscorn/starlette-graphene3)

<details><summary>README extract</summary>

A simple ASGI app for using Graphene v3 with Starlette / FastAPI.

It supports:

- Queries and Mutations (over HTTP or WebSocket)
- Subscriptions (over WebSocket)
- File uploading (
- GraphiQL / GraphQL Playground

File uploading requires `python-multipart` to be installed.

- tartiflette &mdash; Python GraphQL Engine by dailymotion ...

Example:
```python
import asyncio

import graphene
from graphene_file_upload.scalars import Upload

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class Query(graphene.ObjectType):
    me = graphene.Field(User)

...
```

Sections: starlette-graphene3, Alternatives, Example, GraphQLApp

</details>

### pygeocodio

Python wrapper for Geocod.io API

`pip install pygeocodio` · installs (wheel) · licence: BSD License · rank 13368 · last release 2025-06-18 · [PyPI](https://pypi.org/project/pygeocodio/)

<details><summary>README extract</summary>

Python wrapper for Geocodio geocoding API.

Full documentation on Read the Docs.

* Geocode an individual address
* Batch geocode up to 10,000 addresses at a time
* Parse an address into its identifiable components
* Reverse geocode an individual geographic point
* Batch reverse geocode up to 10,000 points at a time
* Perform operations using the ...

Example:
```python
>>> from geocodio import GeocodioClient
>>> client = GeocodioClient(YOUR_API_KEY)
```

Sections: Py-Geocodio, Geocodio API Features, Basic usage, Geocoding, Batch geocoding, Address parsing, Reverse geocoding, Batch reverse geocoding, CLI usage, Documentation

</details>

### aiohttp-sse-client2

A Server-Sent Event python client base on aiohttp

`pip install aiohttp-sse-client2` · installs (wheel) · licence: Apache Software License · rank 13413 · last release 2023-02-07 · [PyPI](https://pypi.org/project/aiohttp-sse-client2/)

<details><summary>README extract</summary>

This is a fork of the aiohttp-sse-client
project by Jason Hu. The motivations for the fork are:

* Better error messages when the request fails (#190)
* Update the library to support new Python versions

The fork will be retired if the upstream package comes back alive.

Features:
* Full asyncio support
* Easy to integrate with other aiohttp based project
* Auto-reconnect for network issue
* Support python 3.6 and above

Example:
```python
from aiohttp_sse_client2 import client as sse_client

async with sse_client.EventSource(
    '
) as event_source:
    try:
        async for event in event_source:
            print(event)
    except ConnectionError:
        pass
```

...

</details>

### zope.sequencesort

Sequence Sorting

`pip install zope.sequencesort` · installs (wheel) · licence: Zope Public License · rank 13417 · last release 2025-09-12 · [PyPI](https://pypi.org/project/zope.sequencesort/)

<details><summary>README extract</summary>

This package provides support for sorting sequences based on multiple
keys, including locale-based comparisons and per-key directions.

Sections: zope.sequencesort, 6.0 (2025-09-12), 5.1 (2025-01-22), 5.0 (2023-01-19), 4.2 (2021-11-04), 4.1.2 (2018-10-10), 4.1.1 (2018-10-05), 4.1.0 (2018-08-13), 4.0.1 (2013-03-04), 4.0.0 (2013-02-28), 3.4.0 (2007-10-03)

</details>

### django-decorator-include

Include Django URL patterns with decorators

`pip install django-decorator-include` · installs (wheel) · licence: BSD-2-Clause · rank 13496 · last release 2026-06-23 · [PyPI](https://pypi.org/project/django-decorator-include/) · [source](https://github.com/twidi/django-decorator-include)

<details><summary>README extract</summary>

Include Django URL patterns with decorators.

Maintained by Steve Mapes, Stéphane "Twidi" Angel, and Jon Dufresne on

based on the original work from Jeff Kistler on

Example:
```python
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.urls import path
from django.contrib.auth.decorators import login_required, user_passes_test

from decorator_include import decorator_include

from mysite.views import index

def only_user(username):
    def check(user):
...
```

Sections: django-decorator-include, Usage

</details>

### basicauth

An incredibly simple HTTP basic auth implementation.

`pip install basicauth` · installs (wheel) · licence: Public Domain · rank 13555 · last release 2022-12-23 · [PyPI](https://pypi.org/project/basicauth/)

<details><summary>README extract</summary>

A dead simple HTTP basic auth encoder and decoder. Why? Because HTTP should be
drop dead easy... That's why.

Example:
```python
>>> from basicauth import encode
>>> username, password = 'rdegges', 'omghax!!!'
>>> encoded_str = encode(username, password)
>>> print encoded_str
'Basic cmRlZ2dlczpvbWdoYXglMjElMjElMjE='
```

Sections: python-basicauth, Usage, Tests

</details>

### flask-weasyprint

Make PDF in your Flask app with WeasyPrint

`pip install flask-weasyprint` · installs (wheel) · licence: BSD License · rank 13591 · last release 2026-03-13 · [PyPI](https://pypi.org/project/flask-weasyprint/) · [docs](https://doc.courtbouillon.org/flask-weasyprint) · [source](https://github.com/Kozea/Flask-WeasyPrint)

<details><summary>README extract</summary>

Flask-WeasyPrint generates PDF files out of your Flask website thanks to
WeasyPrint.

* Free software: BSD license
* For Python 3.11+, tested on CPython and PyPy

Flask-WeasyPrint has been created and developed by Kozea (
Professional support, maintenance and community management is provided by
CourtBouillon ( ...

</details>

### qctrl-client

Q-CTRL Client

`pip install qctrl-client` · installs (wheel) · licence: not stated · rank 13742 · last release 2026-10-06 · [PyPI](https://pypi.org/project/qctrl-client/) · [docs](https://docs.q-ctrl.com) · [source](https://github.com/qctrl)

<details><summary>README extract</summary>

The Q-CTRL Python Client package provides a Python client to access Q-CTRL's GraphQL API. It is used as a base for Q-CTRL's client-side product packages and for inter-service communication.

</details>

### Flask-BabelEx

Adds i18n/l10n support to Flask applications

`pip install Flask-BabelEx` · installs (wheel) · licence: BSD License · rank 13745 · last release 2020-02-07 · [PyPI](https://pypi.org/project/Flask-BabelEx/)

<details><summary>README extract</summary>

Flask-BabelEx

Adds i18n/l10n support to Flask applications with the help of the
`Babel`_ library.

This is fork of official Flask-Babel extension with following features:

1. It is possible to use multiple language catalogs in one Flask application;
2. ...

</details>

### postal

Python bindings to libpostal for fast international address parsing/normalization

`pip install postal` · installs from source (sdist only) · licence: MIT License · rank 13748 · last release 2025-10-29 · [PyPI](https://pypi.org/project/postal/)

### jinja2-fragments

Render Jinja2 template block as HTML page fragments on Python web frameworks.

`pip install jinja2-fragments` · installs (wheel) · licence: MIT · rank 13805 · last release 2026-04-08 · [PyPI](https://pypi.org/project/jinja2-fragments/) · [source](https://github.com/sponsfreixes/jinja2-fragments)

<details><summary>README extract</summary>

Jinja2 Fragments allows rendering individual blocks from
Jinja2 templates. This library was created
to enable the pattern of
Template Fragments with Jinja2. It's a
great pattern if you are using HTMX or some other library that
leverages fetching partial HTML. ...

Example:
```python
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2_fragments import render_block

environment = Environment(
    loader=FileSystemLoader("my_templates"),
    autoescape=select_autoescape(("html", "jinja2")),
)
rendered_html = render_block(
    environment, "page.html.jinja2", "content", magic_number=42
)
```

...

</details>

### aiotus

Asynchronous tus (tus.io) client library

`pip install aiotus` · installs (wheel) · licence: Apache Software License · rank 13844 · last release 2026-11-01 · [PyPI](https://pypi.org/project/aiotus/) · [docs](https://aiotus.readthedocs.io)

<details><summary>README extract</summary>

``aiotus`` implements the client-side of the tus protocol.

Features:
* Implements the core protocol as
 well as the creation
 and concatenation extensions.
* Built-in retry support in case of communication errors.
* Extensive test bench, including tests against the reference tusd server.

Example:
```python
import aiotus

creation_url = "

metadata = {
    "Filename": "image.jpeg".encode(),
    "Content-Type": "image/jpeg".encode()
}

# Upload a file to a tus server.
with open("image.jpeg", "rb") as f:
    location = await aiotus.upload(creation_url, f, metadata)
    # 'location' is the URL where the file was uploaded to.

...
```

Sections: aiotus - Asynchronous tus client library, Features, Usage, Requirements, Documentation

</details>

### http-router

A simple router system for HTTP applications

`pip install http-router` · installs (wheel) · licence: MIT License · rank 13855 · last release 2026-10-20 · [PyPI](https://pypi.org/project/http-router/) · [docs](https://github.com/klen/http-router) · [source](https://github.com/klen/http-router)

<details><summary>README extract</summary>

A small, fast HTTP path router for Python.

Give it a URL path and an HTTP method, and it hands you the callable you bound
to that route — together with any path parameters it captured. No framework, no
request object, no magic.

Features:
- Static (`/users`), dynamic (`/users/{id}`) and regex routes.
- Typed path parameters: `str`, `int`, `float`, `path`, `uuid`.
- Any HTTP method, with shortcuts like `router.get` and `router.post`. ...

Example:
```python
from http_router import Router

router = Router()

@router.get("/health")
def health():
    return "ok"

@router.get("/users/{id}")
def get_user(id):
    return {"id": id}

@router.post("/users")
def create_user():
    return {"created": True}

result = router("/users/42", method="GET")
...
```

...

</details>

### django-oidc-provider

OpenID Connect Provider implementation for Django.

`pip install django-oidc-provider` · installs (wheel) · licence: MIT License · rank 13858 · last release 2025-09-23 · [PyPI](https://pypi.org/project/django-oidc-provider/)

### pyexcel-webio

A generic request and response interface for pyexcel web extensions.

`pip install pyexcel-webio` · installs (wheel) · licence: New BSD · rank 13936 · last release 2017-10-23 · [PyPI](https://pypi.org/project/pyexcel-webio/)

<details><summary>README extract</summary>

Example:
```python
from flask import Flask, Request
import pyexcel as pe
from pyexcel.ext import webio

class ExcelRequest(webio.ExcelInput, Request):
    def _get_file_tuple(self, field_name):
        filehandle = self.files[field_name]
        filename = filehandle.filename
        extension = filename.split(".")[1]
        return extension, filehandle

...
```

Sections: Known constraints, Introduction, Known extensions, Usage, . git clone, . cd pyexcel-webio, How to update test environment and update documentation, . git clone # generic setup, . git clone commons, What is pyexcel-commons, What is .moban.d, Acceptance criteria, . Has Test cases written, . Has all code lines tested

</details>

### pyocclient

Python client library for ownCloud

`pip install pyocclient` · installs from source (sdist only) · licence: MIT License · rank 13940 · last release 2020-09-17 · [PyPI](https://pypi.org/project/pyocclient/)

<details><summary>README extract</summary>

This pure python library makes it possible to connect to an ownCloud instance
and perform file, share and attribute operations.

Please note that this is not a sync client implementation but a library
that provides functions to abstract away HTTP calls for various ownCloud APIs.

See the ownCloud homepage for more information about ownCloud.

Features:
Supports connecting to ownCloud 8.2, 9.0, 9.1 and newer.

Example:
```python
import owncloud

oc = owncloud.Client('

oc.login('user', 'password')

oc.mkdir('testdir')

oc.put_file('testdir/remotefile.txt', 'localfile.txt')

link_info = oc.share_file_with_link('testdir/remotefile.txt')

print "Here is your link: " + link_info.get_link()
```

...

</details>

### django-session-security

Client and server side session timeout with warnings

`pip install django-session-security` · installs (wheel) · licence: MIT License · rank 13991 · last release 2026-04-24 · [PyPI](https://pypi.org/project/django-session-security/)

<details><summary>README extract</summary>

Supported python versions
 Python 3.10, 3.11, 3.12, 3.13, 3.14
Supported django versions
 Django 4.2, 5.0, 5.1, 5.2, 6.0

A little javascript and middleware work together to ensure that the user was
active during the past X minutes in any tab he has open. ...

Features:
Or "Why does this app even exist" ? Here are the reasons:

- if the user session expires before the user is done reading a page: he will
 have to login again. ...

Sections: Documentation, About, Why not just set the session to expire after X minutes ?, How does it work ?, Note to SSO (single sign-on) users, Requirements, Resources

</details>

### ha-garmin

Python client for Garmin Connect API

`pip install ha-garmin` · installs (wheel) · licence: not stated · rank 14031 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ha-garmin/) · [docs](https://github.com/cyberjunky/ha-garmin#readme) · [source](https://github.com/cyberjunky/ha-garmin)

<details><summary>README extract</summary>

Python client for Garmin Connect API, designed for Home Assistant integration.

> Note: ha-garmin covers the subset of the Garmin Connect API that the
> Home Assistant Garmin Connect integration
> needs, with data shaped for its coordinators and sensors. For the full suite of
> Garmin Connect API calls, use python-garminconnect.

Features:
- Native Garmin Connect API integration
- Robust authentication with multiple login strategies and automatic fallbacks
- MFA support with automatic endpoint fallback
- Token persistence - save and restore sessions to avoid re-login ...

Example:
```python
import asyncio
from datetime import date
from ha_garmin import GarminAuth, GarminClient, GarminMFARequired

# Auth is synchronous
auth = GarminAuth()

if not auth.load_session(".garmin_tokens.json"):
...

</details>

### requests-async

Simple async HTTP client with requests-like interface, powered by httpx

`pip install requests-async` · installs (wheel) · licence: MIT · rank 14038 · last release 2025-08-05 · [PyPI](https://pypi.org/project/requests-async/) · [docs](https://github.com/yourusername/requests-async#readme) · [source](https://github.com/yourusername/requests-async)

<details><summary>README extract</summary>

A simple, elegant async HTTP client for Python, built on top of httpx. Get the power of async HTTP requests with a familiar requests-like interface - just add `await`!

Features:
- 🚀 Blazing Fast: Built on httpx for maximum performance
- 🔄 Drop-in Replacement: Same API as requests, just add `await`
- 📦 Simple: Minimal learning curve if you know requests
- 🛡️ Reliable: Built on battle-tested httpx foundation ...

Example:
```python
import asyncio
import requests_async

async def main():
    # Simple GET request
    response = await requests_async.get('
    print(response.json())

    # POST with JSON data
    response = await requests_async.post(
        '
        json={'key': 'value'}
    )
    print(response.status_code)

asyncio.run(main())
```

...

</details>

### django-tenant-users

A Django app to extend django-tenants to incorporate global multi-tenant users

`pip install django-tenant-users` · installs (wheel) · licence: MIT License · rank 14057 · last release 2026-10-18 · [PyPI](https://pypi.org/project/django-tenant-users/) · [docs](https://django-tenant-users.readthedocs.io/) · [source](https://github.com/Corvia/django-tenant-users)

<details><summary>README extract</summary>

Welcome to `django-tenant-users`, the sidekick to `django-tenants`
that sorts out user management in a multi-tenant Django world. 🚀

Features:
Building on the solid foundation of `django-tenants`,
`django-tenant-users` focuses on the nuances of user management across
tenants. It ensures users can authenticate globally but have permissions
tailored to each specific tenant. ...

Sections: django-tenant-users, Overview, Getting Started, . Usage: Check out the Using Guide to

</details>

### django-private-storage

Private media file storage for Django projects

`pip install django-private-storage` · installs (wheel) · licence: License-Expression :: OSI Approved :: Apache-2.0 · rank 14063 · last release 2025-10-05 · [PyPI](https://pypi.org/project/django-private-storage/)

<details><summary>README extract</summary>

This module offers a private media file storage,
so user uploads can be protected behind a login.

It uses the Django storage API's internally,
so all form rendering and admin integration work out of the box.

Example:
```python
from django.db import models
from private_storage.fields import PrivateFileField

class MyModel(models.Model):
    title = models.CharField("Title", max_length=200)
    file = PrivateFileField("File")
```

Sections: django-private-storage, Configuration, Usage, Images, Other topics, Storing files on Amazon S3, MinIO storage, Defining access rules, Retrieving files by object ID, Optimizing large file transfers, For apache, For Nginx, Other webservers, Using multiple storages

</details>

### django-magiclink

Passwordless authentication for Django with Magic Links

`pip install django-magiclink` · installs (wheel) · licence: MIT · rank 14097 · last release 2026-10-31 · [PyPI](https://pypi.org/project/django-magiclink/) · [source](https://github.com/pyepye/django-magiclink)

<details><summary>README extract</summary>

Passwordless Authentication for Django with Magic Links.

This package was created with a focus on ease of setup, security and testing (coverage is currently at 100%). The idea is to use sane defaults to quickly create secure single-use token authentication for Django.

Example:
```python
urlpatterns = [
    ...
    path('auth/', include('magiclink.urls', namespace='magiclink')),
    ...
]
```

Sections: Django MagicLink, Setup, Basic login flow, Configuration, Login page, Login sent page, Login failed page, Magic link email, Signup page, Configuration settings, Magic Link cleanup, Unsubscribe / stopping email spam, Manual usage, Creating magiclinks

</details>

### djust

Phoenix LiveView-style reactive components for Django with Rust-powered performance. Real-time UI updates over WebSocket, no JavaScript build step required.

`pip install djust` · installs (wheel) · licence: MIT License · rank 14114 · last release 2026-11-07 · [PyPI](https://pypi.org/project/djust/) · [docs](https://djust.org/quickstart/) · [source](https://github.com/djust-org/djust)

<details><summary>README extract</summary>

Reactive server-side rendering for Django, powered by Rust

djust brings Phoenix LiveView-style reactive views to Django. You write
server-side Python; the browser updates itself over a WebSocket. There is no
JavaScript to write, no bundler, and no build step in your project.

djust.org · Documentation · Quick Start · Examples

Features:
- One codebase. Views, state and event handlers are Python. No API layer, no frontend build.
- Small wire traffic. A Rust virtual DOM diffs each render and sends only the changed patches.
- Fast templates. ...

Example:
```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from djust.websocket import LiveViewConsumer
...

</details>

### feedgenerator

Standalone version of django.utils.feedgenerator

`pip install feedgenerator` · installs (wheel) · licence: BSD License · rank 14141 · last release 2025-08-17 · [PyPI](https://pypi.org/project/feedgenerator/)

<details><summary>README extract</summary>

FeedGenerator is a standalone version of Django’s
feedgenerator
module. It has evolved over time and includes numerous enhancements.

</details>

### parse-accept-language

Parse Accept-Language HTTP header

`pip install parse-accept-language` · installs (wheel) · licence: Apache License 2.0 · rank 14207 · last release 2017-09-04 · [PyPI](https://pypi.org/project/parse-accept-language/)

### aiotieba

Asynchronous I/O Client for Baidu Tieba

`pip install aiotieba` · installs (wheel) · licence: Unlicense · rank 14212 · last release 2026-11-01 · [PyPI](https://pypi.org/project/aiotieba/) · [docs](https://aiotieba.cc/) · [source](https://github.com/lumina37/aiotieba/)

<details><summary>README extract</summary>

*输出样例*

继续阅读入门教程

Example:
```python
import asyncio

import aiotieba

async def main():
    async with aiotieba.Client() as client:
        threads = await client.get_threads("天堂鸡汤")
        for thread in threads[3:6]:
            print(f"tid={thread.tid}\ntext={thread.text}")

asyncio.run(main())
```

Sections: 安装, 尝试一下, 项目特色, 友情链接, 特别鸣谢

</details>

### uptime-kuma-api-v2

A python wrapper for the Uptime Kuma WebSocket API

`pip install uptime-kuma-api-v2` · installs (wheel) · licence: MIT License · rank 14243 · last release 2026-05-26 · [PyPI](https://pypi.org/project/uptime-kuma-api-v2/)

<details><summary>README extract</summary>

A wrapper for the Uptime Kuma Socket.IO API

uptime-kuma-api-v2 is a Python wrapper for the Uptime Kuma Socket.IO API.

Based on Original Version by

Python version 3.7+ is required.

Supported Uptime Kuma versions:

| Uptime Kuma | uptime-kuma-api-v2 |

| 2.0.0-beta.2 | 1.0.0 - 1.0.2 |

Installation ...

Example:
```python
>>> from uptime_kuma_api import UptimeKumaApi, MonitorType
>>> api = UptimeKumaApi('INSERT_URL')
>>> api.login('INSERT_USERNAME', 'INSERT_PASSWORD')
```

</details>

### type-lens

type-lens is a Python template project designed to simplify the setup of a new project.

`pip install type-lens` · installs (wheel) · licence: MIT License · rank 14289 · last release 2025-10-20 · [PyPI](https://pypi.org/project/type-lens/) · [docs](https://docs.type-lens.litestar.dev/) · [source](https://github.com/litestar-org/type-lens)

### mailmanclient

mailmanclient -- Python bindings for Mailman REST API

`pip install mailmanclient` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 14316 · last release 2023-01-04 · [PyPI](https://pypi.org/project/mailmanclient/)

_README extract left out: share-alike licence._

### pulsar-relay-client

Client library for the pulsar-relay HTTP wire contract (auth, transport, device flow, topic management)

`pip install pulsar-relay-client` · installs (wheel) · licence: MIT · rank 14346 · last release 2026-05-14 · [PyPI](https://pypi.org/project/pulsar-relay-client/) · [source](https://github.com/mvdbeek/pulsar-relay)

<details><summary>README extract</summary>

Python client for the pulsar-relay HTTP wire contract.

Used by:

- the Pulsar daemon's relay subscriber/auth layer
- Galaxy's BYOC (Bring-Your-Own-Compute) Pulsar manager
- pulsar-relay's own end-to-end tests ...

Example:
```python
from pulsar_relay_client import RelayTransport

transport = RelayTransport(
    "
    credentials_file="/etc/pulsar/relay_credentials.json",
    cursor_path="/var/lib/pulsar/relay_cursor.json",
)
transport.post_message("job_status_update_my_manager", {"job_id": "j1", "state": "ok"})
...
```

Sections: pulsar-relay-client, Modules, Quick start, Versioning

</details>

### hexor

Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.

`pip install hexor` · installs (wheel) · licence: Apache Software License · rank 14354 · last release 2023-06-06 · [PyPI](https://pypi.org/project/hexor/) · [source](https://github.com/yasserbdj96/hexor)

<details><summary>README extract</summary>

Coloring texts and their backgrounds in command line interface (cli), with rgb or hex types.

* python3

Example:
```python
from hexor import hexor

# Usage example:
# p1 = hexor(return_option)

# return_option: [True, False]
# True to return results
# False to print results

# color_format: ['hex', 'rgb']
# 'hex' for hex colors (e.g., #ffffff, #cccccc)
# 'rgb' for rgb colors (e.g., (255, 255, 255), rgb(250, 12, 0))

# The default options are: hexor() = hexor(False)
...
```

Sections: hexor, Languages, Script Usage, Script Examples, Screenshot

</details>

### django-database-view

A simple Django app to handle database views.

`pip install django-database-view` · installs (wheel) · licence: MIT License · rank 14355 · last release 2021-09-08 · [PyPI](https://pypi.org/project/django-database-view/)

<details><summary>README extract</summary>

A simple pluggable application that allows to work with database views.

Sections: django-database-view, Quick start

</details>

### Flask-SeaSurf

An updated CSRF extension for Flask.

`pip install Flask-SeaSurf` · installs (wheel) · licence: BSD License · rank 14384 · last release 2024-07-29 · [PyPI](https://pypi.org/project/Flask-SeaSurf/)

<details><summary>README extract</summary>

SeaSurf is a Flask extension for preventing cross-site request forgery (CSRF).

CSRF vulnerabilities have been found in large and popular sites such as
YouTube. These attacks are problematic because the mechanism they use is
relatively easy to exploit. This extension attempts to aid you in securing
your application from such attacks. ...

Sections: Flask-SeaSurf, Usage, Documentation

</details>

### drf-recaptcha

Django rest framework recaptcha field serializer

`pip install drf-recaptcha` · installs (wheel) · licence: MIT License · rank 14400 · last release 2025-08-22 · [PyPI](https://pypi.org/project/drf-recaptcha/) · [source](https://github.com/llybin/drf-recaptcha)

<details><summary>README extract</summary>

Django REST reCAPTCHA v2 and v3 field serializer

* Python: 3.10, 3.11, 3.12, 3.13
* Django: 4.2, 5.0, 5.1, 5.2
* DRF: 3.14, 3.15, 3.16

Example:
```python
from rest_framework.serializers import Serializer, ModelSerializer
from drf_recaptcha.fields import ReCaptchaV2Field, ReCaptchaV3Field
from feedback.models import Feedback

class V2Serializer(Serializer):
    recaptcha = ReCaptchaV2Field()
    ...

class GetOTPView(APIView):
    def post(self, request):
...
```

Sections: Django REST reCAPTCHA, Requirements, Usage, Settings, Priority of secret_key value, Silence the check error, reCAPTCHA v3, Priority of score value

</details>

### pyrabbit

A Pythonic interface to the RabbitMQ Management HTTP API

`pip install pyrabbit` · installs from source (sdist only) · licence: MIT License · rank 14414 · last release 2014-08-28 · [PyPI](https://pypi.org/project/pyrabbit/)

<details><summary>README extract</summary>

The main documentation lives at

There's no way to easily write programs against RabbitMQs management API
without resorting to some messy urllib boilerplate code involving HTTP
Basic authentication and parsing the JSON responses, etc. ...

</details>

### wrapper-tls-requests

A powerful and lightweight Python library for making secure and reliable HTTP/TLS fingerprint requests.

`pip install wrapper-tls-requests` · installs (wheel) · licence: MIT · rank 14436 · last release 2026-02-23 · [PyPI](https://pypi.org/project/wrapper-tls-requests/) · [docs](https://thewebscraping.github.io/tls-requests/) · [source](https://github.com/thewebscraping/tls-requests)

<details><summary>README extract</summary>

TLS Requests is a powerful Python library for secure HTTP requests, offering browser-like TLS client, fingerprinting, anti-bot page bypass, and high performance.

* * *

Installation

To install the library, you can choose between two methods:

Example:
```python
import tls_requests
r = tls_requests.get('
r
<Response [200]>
```

Sections: TLS Requests, Key Benefits, Unlocking Cloudflare Bot Fight Mode, Enhanced Capabilities, Additional Features

</details>

### sphinxcontrib-django

Improve the Sphinx autodoc for Django classes.

`pip install sphinxcontrib-django` · installs (wheel) · licence: Apache Software License · rank 14439 · last release 2023-09-26 · [PyPI](https://pypi.org/project/sphinxcontrib-django/) · [docs](https://sphinxcontrib-django.readthedocs.io/) · [source](https://github.com/edoburu/sphinxcontrib-django)

<details><summary>README extract</summary>

This is a sphinx extension which improves the documentation of Django apps.

Features:
Improvements for the output of Sphinx's autodoc for Django classes:

* List all model and form fields as class parameters
* Improve model field representations
* Link related and reverse related fields to the referenced class
* Hide irrelevant ...

Example:
```python
def patch_django(app):
    """
    Your custom code here
    """

def setup(app):
    app.connect("django-configured", patch_django)
```

Sections: sphinxcontrib-django, Features, Configuration, Advanced Usage

</details>

### django-prose-editor

Prose editor for the Django admin based on ProseMirror

`pip install django-prose-editor` · installs (wheel) · licence: BSD License · rank 14465 · last release 2026-10-26 · [PyPI](https://pypi.org/project/django-prose-editor/) · [docs](https://django-prose-editor.readthedocs.io/)

<details><summary>README extract</summary>

Prose editor for the Django admin based on ProseMirror and Tiptap. Announcement blog post.

After installing the package (using `pip install
django-prose-editor[sanitize]`) the following should get you started:

Check the documentation.

Example:
```python
from django_prose_editor.fields import ProseEditorField

content = ProseEditorField(
    extensions={
        "Bold": True,
        "Italic": True,
        "BulletList": True,
        "ListItem": True,
        "Link": True,
    },
    sanitize=True,  # Server side sanitization is strongly recommended.
)
```

Sections: django-prose-editor, Intro

</details>

### djangocms-text-ckeditor

Text Plugin for django CMS with CKEditor support

`pip install djangocms-text-ckeditor` · installs (wheel) · licence: BSD License · rank 14515 · last release 2025-03-26 · [PyPI](https://pypi.org/project/djangocms-text-ckeditor/)

<details><summary>README extract</summary>

CKEditor (v4) is a ready-for-use HTML text editor designed to simplify web content
creation. It's a WYSIWYG editor that brings common word processor features
directly to your web pages. Enhance your website experience with our community
maintained editor. This package aims to integrate CKEditor into django CMS as
a text plugin.

Example:
```python
from djangocms_text_ckeditor.fields import HTMLField
```

Sections: django CMS Text CKEditor, Documentation, Upgrading from `cms.plugins.text`, Configuration, Inline editing feature, Default content in Placeholder, CKEDITOR_SETTINGS, Customizing plugin editor, Customizing HTMLField editor, Inline preview, Drag & Drop Images, Usage as a model field, Auto Hyphenate Text, Extending the plugin

</details>

### django-termsandconditions

Django app that enables users to accept terms and conditions of a site.

`pip install django-termsandconditions` · installs (wheel) · licence: MIT License · rank 14527 · last release 2026-05-05 · [PyPI](https://pypi.org/project/django-termsandconditions/)

<details><summary>README extract</summary>

Django Terms and Conditions gives you an configurable way to send users
to a T&C acceptance page before they can access the site.

*Note that version 2.1+ requires Python 3.12+ and Django 5.2+.*

Creator and Maintainer: - Tim White ()

Contributors: - Adibo () - Nathan Swain ()

Features ...

Sections: Django Terms and Conditions, Requirements, Add urls to urls.py, Terms and Conditions Versioning, Terms and Conditions Default URLs, Terms and Conditions Middleware, Terms and Conditions Useful Methods, Terms and Conditions Cache, Terms and Conditions View Decorator, {% block title %}{% endblock %}, Terms and Conditions Template Tag, Using terms with as\_template filter, Terms and Conditions Pipeline, 1. Modify your `settings.py`

</details>

### sqlalchemy-searchable

Provides fulltext search capabilities for declarative SQLAlchemy models.

`pip install sqlalchemy-searchable` · installs (wheel) · licence: BSD-3-Clause · rank 14535 · last release 2026-02-16 · [PyPI](https://pypi.org/project/sqlalchemy-searchable/) · [docs](https://sqlalchemy-searchable.readthedocs.io/) · [source](https://github.com/falcony-io/sqlalchemy-searchable)

<details><summary>README extract</summary>

Fulltext searchable models for SQLAlchemy. Only supports PostgreSQL

- Documentation
- Issue Tracker
- Code

Sections: SQLAlchemy-Searchable, Resources

</details>

### aioresponses-ng

Maintained fork of aioresponses with aiohttp compatibility fixes

`pip install aioresponses-ng` · installs (wheel) · licence: MIT · rank 14565 · last release 2026-07-05 · [PyPI](https://pypi.org/project/aioresponses-ng/) · [source](https://github.com/mountaingod2/aioresponses-ng)

<details><summary>README extract</summary>

> This is a maintained fork of aioresponses
> with aiohttp compatibility fixes. The API is identical - just swap the package name.

Aioresponses is a helper to mock/fake web requests in python aiohttp package.

For the *requests* module there are a lot of packages that help us with testing (e.g. *httpretty*, *responses*, *requests-mock*). ...

Features:
- Easy to mock out HTTP requests made by `aiohttp.ClientSession`

Example:
```python
import aiohttp
import asyncio
from aioresponses import aioresponses

@aioresponses()
def test_request(mocked):
    loop = asyncio.get_event_loop()
    mocked.get(' status=200, body='test')
    session = aiohttp.ClientSession()
    resp = loop.run_until_complete(session.get('

    assert resp.status == 200
    mocked.assert_called_once_with('
```

...

</details>

### WSME

Simplify the writing of REST APIs, and extend them with additional protocols.

`pip install WSME` · installs (wheel) · licence: MIT License · rank 14599 · last release 2026-07-13 · [PyPI](https://pypi.org/project/WSME/)

<details><summary>README extract</summary>

Web Services Made Easy (WSME) simplifies the writing of REST web services
by providing simple yet powerful typing, removing the need to directly
manipulate the request and the response objects. ...

Example:
```python
from wsme import WSRoot, expose

class MyService(WSRoot):
    @expose(unicode, unicode)  # First parameter is the return type,
                               # then the function argument types
    def hello(self, who=u'World'):
        return u"Hello {0} !".format(who)

ws = MyService(protocols=['restjson', 'restxml'])
application = ws.wsgiapp()
```

Sections: Web Services Made Easy, Introduction, How Easy?, Main features, Changes, Getting Help

</details>

### flup-py3

Random assortment of WSGI servers

`pip install flup-py3` · installs (wheel) · licence: BSD License · rank 14624 · last release 2018-02-08 · [PyPI](https://pypi.org/project/flup-py3/)

### djangocms-attributes-field

Adds attributes to Django models.

`pip install djangocms-attributes-field` · installs (wheel) · licence: BSD License · rank 14625 · last release 2025-11-02 · [PyPI](https://pypi.org/project/djangocms-attributes-field/) · [source](https://github.com/django-cms/djangocms-attributes-field/)

<details><summary>README extract</summary>

This project is an opinionated implementation of JSONField for arbitrary HTML
element attributes.

It aims to provide a sensible means of storing and managing
arbitrary HTML element attributes for later emitting them into templates. ...

Example:
```python
# models.py
...
from django.db import models
from djangocms_attributes_field.fields import AttributesField
...
MyCoolModel(models.Model):
    ...
    attributes = AttributesField()
```

Sections: django CMS Attributes Field, Documentation, Configuration, AttributeField, property: [field_name]_str, AttributeWidget, Running Tests

</details>

### flask-mongoengine

Flask-MongoEngine is a Flask extension that provides integration with MongoEngine and WTF model forms.

`pip install flask-mongoengine` · installs (wheel) · licence: BSD License · rank 14642 · last release 2020-11-21 · [PyPI](https://pypi.org/project/flask-mongoengine/)

<details><summary>README extract</summary>

A Flask extension that provides integration with MongoEngine.
For more information on MongoEngine please check out the MongoEngine Documentation.

It handles connection management for your app.
You can also use WTForms as model forms for your models.

Make sure you have `wheel` installed:

Example:
```python
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(name)
app.config.from_pyfile('the-config.cfg')
db = MongoEngine(app)
```

Sections: Flask-MongoEngine, Pre-requisite, Configuration, Custom Queryset, MongoEngine and WTForms, Session Interface, Debug Toolbar Panel, Upgrading, 0.6 to 0.7

</details>

### django-author

Add special User ForeignKey fields which update automatically

`pip install django-author` · installs from source (sdist only) · licence: MIT License · rank 14644 · last release 2022-04-19 · [PyPI](https://pypi.org/project/django-author/)

<details><summary>README extract</summary>

Example:
```python
from django.db import models
from author.decorators import with_author

@with_author
class Entry(models.Model):
    title = models.CharField('title', max_length=50)
    body = models.TextField('body')
```

Sections: Usage, Settings, Backend

</details>

### pymantic

Semantic Web and RDF library for Python

`pip install pymantic` · installs (wheel) · licence: BSD License · rank 14648 · last release 2025-10-02 · [PyPI](https://pypi.org/project/pymantic/)

<details><summary>README extract</summary>

Example:
```python
>>> from pymantic.rdf import *
>>> from pymantic.parsers import turtle_parser
>>> import requests
>>> Resource.prefixes['foaf'] = Prefix('
>>> graph = turtle_parser.parse(requests.get('
>>> bond_james = Resource(graph, '
>>> print("%s knows:" % (bond_james.get_scalar('foaf:name'),))
>>> for person in bond_james['foaf:knows']:
...
```

Sections: Pymantic, Semantic Web and RDF library for Python, Quick Start, Requirements, Documentation

</details>

### django-allauth-ui

(no summary)

`pip install django-allauth-ui` · installs (wheel) · licence: MIT License · rank 14651 · last release 2025-05-28 · [PyPI](https://pypi.org/project/django-allauth-ui/) · [source](https://github.com/danihodovic/django-allauth-ui)

<details><summary>README extract</summary>

UI templates for django-allauth
built with Tailwind.

django-allauth is a great library, but the templates it provides out of the box
are minimal html. I usually end up re-designing the login / logout / signup
pages for each new Django project. This library aims at providing good
defaults for new projects.

Features:
- 📱 Mobile-friendly design
- 💄 Configurable themes
- 🕵️ Support for Allauth User Sessions
- 📱Support for Multi-Factor Authentication
- 🗣️ Translations
 - 🇪🇸 Spanish
 - 🇫🇷 French
 - 🇧🇷 Portuguese
 - 🇹🇷 Turkish
 - 🇮🇹 Italian

Sections: AllAuth UI, Features, Configuration, Hacking on the project

</details>

### django-extra-fields

Additional fields for Django Rest Framework.

`pip install django-extra-fields` · installs from source (sdist only) · licence: BSD License · rank 14652 · last release 2020-09-22 · [PyPI](https://pypi.org/project/django-extra-fields/)

<details><summary>README extract</summary>

This package renamed as "drf-extra-fields", earlier it was named as django-extra-fields. New versions can be tracked from here.

Extra Fields for Django Rest Framework

Example:
```python
# serializer

from drf_extra_fields.fields import Base64ImageField

class UploadedBase64ImageSerializer(serializers.Serializer):
    file = Base64ImageField(required=False)
    created = serializers.DateTimeField()

# use the serializer
file = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
...
```

Sections: THIS PACKAGE IS DEPRECATED, DRF-EXTRA-FIELDS, Usage, Base64ImageField, Base64FileField, PointField, IntegerRangeField, FloatRangeField, DecimalRangeField, DateRangeField, DateTimeRangeField, PresentablePrimaryKeyRelatedField, PresentableSlugRelatedField, read_source parameter

</details>

### tastytrade

An unofficial, typed, asynchronous Python SDK for Tastytrade!

`pip install tastytrade` · installs (wheel) · licence: MIT License · rank 14677 · last release 2026-08-07 · [PyPI](https://pypi.org/project/tastytrade/) · [docs](https://tastyworks-api.rtfd.io) · [source](https://github.com/tastyware/tastytrade)

<details><summary>README extract</summary>

A simple, asynchronous SDK for Tastytrade's public API. This will allow you to create trading algorithms for whatever strategies you may have quickly and painlessly in Python.

Features:
- Up to 10x less code than using the API directly
- Powerful websocket implementation for account alerts and data streaming
- 100% typed, with Pydantic models for all JSON responses from the API
- 95%+ unit test coverage ...

Example:
```python
from tastytrade import Session
session = Session('client_secret', 'refresh_token')
```

Sections: Tastytrade Python SDK, Features, Getting started, Creating a session, Using the streamer, Getting current positions, Placing an order, Options chain/streaming greeks, Disclaimer

</details>

### instana

Python Distributed Tracing & Metrics Sensor for Instana.

`pip install instana` · installs (wheel) · licence: MIT · rank 14679 · last release 2026-10-14 · [PyPI](https://pypi.org/project/instana/) · [docs](https://ibm.biz/monitoring-python) · [source](https://github.com/instana/python-sensor)

<details><summary>README extract</summary>

The `instana` Python package collects key metrics and distributed traces for [Instana].

Any feedback is welcome. Happy Python visibility.

> [!NOTE]
> Support for OpenTracing is deprecated starting on version 3.0.0. If you still want to use it, rely on any version earlier than 3.0.0 or use the `legacy_2.x` branch.

Sections: Instana, Activating Without Code Changes, Activating With Code Changes, Documentation, More

</details>

### tinyhtml

A tiny library to safely render compact HTML5 from Python expressions.

`pip install tinyhtml` · installs (wheel) · licence: Apache Software License; MIT License · rank 14680 · last release 2025-01-11 · [PyPI](https://pypi.org/project/tinyhtml/)

<details><summary>README extract</summary>

A tiny library to safely render compact HTML5 from Python expressions.

This is the entire API. The following documentation is longer than the
implementation.

The most important function is `h()`. Below you see how to render attributes,
normal elements, and void/self-closing elements.

Use `frag()` to pass around groups of elements. ...

Features:
* Output is compact: Naturally produces no superfluous whitespace between
 elements.

* Fragments provide repr_html() for Jupyter notebook integration and
 _html__ for integration with other ecosystems (see
 MarkupSafe). ...

Example:
```python
>>> from tinyhtml import html, h, frag, raw
```

Sections: tinyhtml, Introduction, Features and patterns, Hello world, Interoperability, A table

</details>

### django-fieldsignals

Django signals that fire when specific model fields change

`pip install django-fieldsignals` · installs (wheel) · licence: MIT License · rank 14706 · last release 2025-12-25 · [PyPI](https://pypi.org/project/django-fieldsignals/) · [source](https://github.com/craigds/django-fieldsignals)

<details><summary>README extract</summary>

django-fieldsignals simply makes it easy to tell when the fields on your model have changed.

Often model updates are quite expensive. Sometimes the expensive operations
are very rare. This makes it tempting to put the update logic in a view,
rather than in a save() method or in a signal receiver: ...

Example:
```python
# A bad example. Don't do this!
def edit_poll(request, poll_id):

    # ...

    if form.cleaned_data['poll_name'] != poll.name:
        poll.update_slug(form.cleaned_data['poll_name'])
    poll.save()
```

Sections: Introduction, Where should my signals code live?, Notes

</details>

### Flask-JSON

Better JSON support for Flask

`pip install Flask-JSON` · installs (wheel) · licence: BSD License · rank 14712 · last release 2023-05-06 · [PyPI](https://pypi.org/project/Flask-JSON/)

<details><summary>README extract</summary>

Flask-JSON is a simple extension that adds better JSON support to Flask
application.

Features:

* Works on python 2.6, 2.7, 3.3+ and Flask 0.10+.
* More ways to generate JSON responses (comparing to plain Flask).
* Extended JSON encoding support.

Example:
```python
from datetime import datetime
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(name)
FlaskJSON(app)

@app.route('/get_time')
def get_time():
    return json_response(time=datetime.utcnow())

@app.route('/get_time_and_value')
@as_json
def get_time_and_value():
...
```

Sections: Flask-JSON, Usage, Documentation

</details>

### invisible-core

Pure config for a stealth Firefox profile: seed -> fingerprint -> prefs, engine download, proxy, geo, and the Juggler client the wrappers drive it with. Zero Playwright.

`pip install invisible-core` · installs (wheel) · licence: MIT AND Apache-2.0 · rank 14718 · last release 2026-11-08 · [PyPI](https://pypi.org/project/invisible-core/) · [source](https://github.com/feder-cr/invisible_core)

<details><summary>README extract</summary>

Pure config for a patched Firefox stealth profile - zero Playwright dependency.

`seed → fingerprint profile → Firefox prefs`, plus patched-binary download,
proxy config, geo/timezone resolution, and `invisible_core.juggler`: the client
that drives the engine over its own protocol, with the human input rhythm, which
every wrapper below shares ...

Example:
```python
from invisible_core import (ensure_binary, generate_profile, prepare_session_geo,
                            translate_profile_to_prefs)

profile = generate_profile(seed=42)        # deterministic Bayesian fingerprint
geo     = prepare_session_geo("auto", None)  # zone and language of the exit (here, this machine's public IP)
...
```

Sections: invisible_core, What the fields actually mean

</details>

### Flask-QRcode

A concise Flask extension to render QR codes on Jinja2 templates using python-qrcode

`pip install Flask-QRcode` · installs (wheel) · licence: GPL-3.0-or-later · rank 14749 · last release 2026-10-16 · [PyPI](https://pypi.org/project/Flask-QRcode/) · [docs](https://marcoagner.github.io/Flask-QRcode/) · [source](https://github.com/marcoagner/Flask-QRcode)

_README extract left out: share-alike licence._

### WTForms-Alchemy

Generates WTForms forms from SQLAlchemy models.

`pip install WTForms-Alchemy` · installs (wheel) · licence: BSD License · rank 14792 · last release 2025-08-11 · [PyPI](https://pypi.org/project/WTForms-Alchemy/)

<details><summary>README extract</summary>

WTForms-Alchemy

Generates WTForms forms from SQLAlchemy models.

</details>

### fastapi-guard

Production-ready security middleware for FastAPI — IP filtering, rate limiting, penetration detection, and 20+ per-route security decorators.

`pip install fastapi-guard` · installs (wheel) · licence: MIT · rank 14812 · last release 2026-10-17 · [PyPI](https://pypi.org/project/fastapi-guard/) · [docs](https://guard-core.github.io/fastapi-guard/latest/) · [source](https://github.com/Guard-Core/fastapi-guard)

<details><summary>README extract</summary>

Website ·
 Docs ·
 Playground ·
 Dashboard ·
 Discord

 Production-ready security middleware for FastAPI.

 IP filtering, rate limiting, signature-based attack-pattern detection, and 20+ per-route security decorators.

Tell me what is working and what is not →

Six minutes. It decides what gets built next.

Anonymous unless you choose otherwise.

Example:
```python
from fastapi import FastAPI
from guard import SecurityMiddleware, SecurityConfig

app = FastAPI()

config = SecurityConfig(
    enable_rate_limiting=True,
    rate_limit=100,
    rate_limit_window=60,
    enable_ip_banning=True,
    auto_ban_threshold=5,
    auto_ban_duration=86400,
    custom_log_file="security.log",
    enforce_https=True,
...
```

...

</details>

### django-multiupload

Dead simple drop-in multi file upload field for django forms using HTML5's multiple attribute.

`pip install django-multiupload` · installs (wheel) · licence: BSD License · rank 14867 · last release 2021-10-06 · [PyPI](https://pypi.org/project/django-multiupload/)

<details><summary>README extract</summary>

Dead simple drop-in multi file upload field for django forms using HTML5's ``multiple`` attribute.

Example:
```python
# forms.py
from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
    attachments = MultiMediaField(
        min_num=1,
...
```

Sections: Django Multiupload, Usage

</details>

### pyxnat

XNAT in Python

`pip install pyxnat` · installs (wheel) · licence: BSD License · rank 14888 · last release 2025-11-06 · [PyPI](https://pypi.org/project/pyxnat/)

<details><summary>README extract</summary>

The source code is currently hosted on GitHub at:

Binary installers for the latest released version are available at the Python
package index. pyxnat can be installed
using `pip` with the following command:

- requests v2.20 or higher
- python-lxml v4.3.2 or higher recommended, earlier versions may work.

For development purposes: ...

Sections: pyxnat, Where to get it, Dependencies, Documentation, Running the test suite, Building the documentation

</details>

### Scweet

Scrape tweets, profiles, followers and more from Twitter/X — no API key needed

`pip install Scweet` · installs (wheel) · licence: MIT License · rank 14906 · last release 2026-10-22 · [PyPI](https://pypi.org/project/Scweet/) · [docs](https://altimis.github.io/Scweet/) · [source](https://github.com/Altimis/Scweet)

<details><summary>README extract</summary>

Scrape Twitter / X without the official API.

 Tweets, profiles, followers, trends and more.

Runs on Apify. You do not need X accounts, cookies or proxies.

- Configure and run from your browser, no code needed, or drive it from code with the Python API
- Search tweets, profile timelines, follower / following lists ...

Features:
One page of X is easy to fetch. 10,000 tweets is not, because accounts get rate-limited, cookies expire, and X changes its API.

Your run finishes
- A wide date range is split into intervals that run in parallel. ...

Example:
```python
from Scweet import Scweet

s = Scweet(auth_token="YOUR_AUTH_TOKEN")
tweets = s.search("bitcoin", limit=100)

for tweet in tweets:
    print(tweet["text"])
```

...

</details>

### FastAPI-SQLAlchemy

Adds simple SQLAlchemy support to FastAPI

`pip install FastAPI-SQLAlchemy` · installs (wheel) · licence: MIT License · rank 14933 · last release 2020-09-25 · [PyPI](https://pypi.org/project/FastAPI-SQLAlchemy/) · [source](https://github.com/mfreeborn/fastapi-sqlalchemy)

<details><summary>README extract</summary>

FastAPI-SQLAlchemy provides a simple integration between FastAPI and SQLAlchemy in your application. It gives access to useful helpers to facilitate the completion of common tasks.

Example:
```python
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import db  # an object to provide global access to a database session

from app.models import User

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="sqlite://")

...
```

Sections: FastAPI-SQLAlchemy, Examples, Usage inside of a route, Usage outside of a route

</details>

## Also in this topic

- [fastapi](internet.md#fastapi) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [gunicorn](internet.md#gunicorn) - WSGI HTTP Server for UNIX
- [Markdown](communications-email.md#markdown) - Python implementation of John Gruber's Markdown.
- [snowballstemmer](database.md#snowballstemmer) - This package provides 36 stemmers for 34 languages generated from Snowball algorithms.
- [sqlmodel](database.md#sqlmodel) - SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
- [Sphinx](documentation.md#sphinx) - Python documentation generator
- [drf-spectacular](documentation.md#drf-spectacular) - Sane and flexible OpenAPI 3 schema generation for Django REST framework
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [autobahn](communications.md#autobahn) - WebSocket client & server library, WAMP real-time framework
- [atlassian-python-api](internet.md#atlassian-python-api) - Python Atlassian REST API Wrapper
- [xlwt](database.md#xlwt) - Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.6, 2.7, 3.3+
- [selectolax](internet.md#selectolax) - A fast HTML5 parser with CSS selectors, written in Cython, using the Lexbor engine.
- [firecrawl-py](internet.md#firecrawl-py) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [premailer](communications.md#premailer) - Turns CSS blocks into style attributes
- [pycurl](internet-file-transfer-protocol-ftp.md#pycurl) - PycURL -- A Python Interface To The cURL library
- [django-ninja](internet.md#django-ninja) - Django Ninja - Fast Django REST framework
- [mitmproxy](internet-proxy-servers.md#mitmproxy) - An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.
- [cadwyn](internet.md#cadwyn) - Production-ready community-driven modern Stripe-like API versioning in FastAPI
- [connexion](internet.md#connexion) - Connexion - API first applications with OpenAPI/Swagger
- [drf-spectacular-sidecar](documentation.md#drf-spectacular-sidecar) - Serve self-contained distribution builds of Swagger UI and Redoc with Django
- [commonmark](documentation.md#commonmark) - Python parser for the CommonMark Markdown spec
- [django-polymorphic](database.md#django-polymorphic) - Seamless polymorphic inheritance for Django models.
- [PubChemPy](database-front-ends.md#pubchempy) - A simple Python wrapper around the PubChem PUG REST API.
- [DBUtils](database.md#dbutils) - Database connections for multi-threaded environments.
- [geocoder](internet.md#geocoder) - Geocoder is a simple and consistent geocoding library.
- [litestar](internet.md#litestar) - Litestar - A production-ready, highly performant, extensible ASGI API Framework
- [seleniumbase](internet.md#seleniumbase) - SeleniumBase is a framework for web crawling, scraping, and testing. Supports pytest. CDP Mode adds stealth. Includes many tools.
- [stpyv8](internet.md#stpyv8) - Python Wrapper for Google V8 Engine
- [PyStemmer](database.md#pystemmer) - Snowball stemming algorithms, for information retrieval
- [litestar-htmx](internet.md#litestar-htmx) - HTMX Integration for Litestar
- [swagger-ui-bundle](internet.md#swagger-ui-bundle) - Swagger UI bundled for usage with Python
- [pyngrok](internet-proxy-servers.md#pyngrok) - The complete ngrok agent for Python: programmatic tunnels for ingress, inspection, webhooks, demos, and APIs
- [proxy.py](internet.md#proxypy) - \u26a1 Fast \u2022 \U0001fab6 Lightweight \u2022 \U0001f51f Dependency \u2022 \U0001f50c Pluggable \u2022 \U0001f608 TLS interception \u2022 \U0001f512 DNS-over-HTTPS \u2022 \U0001f525 Poor Mans VPN \u2022 \u23ea Reverse & \u23e9 Forward \u2022 \U0001f46e\U0001f3ff Proxy Server framework \u2022 \U0001f310 Web Server framework \u2022 \u27b5 \u27b6 \u27b7 \u27a0 PubSub framework \u2022 \U0001f477 Work acceptor & executor framework.
- [fastapi-utils](internet.md#fastapi-utils) - Reusable utilities for FastAPI
- [emails](communications.md#emails) - Modern python library for emails.
- [django-rq](internet.md#django-rq) - An app that provides django integration for RQ (Redis Queue)
- [firecrawl](internet.md#firecrawl) - Python SDK for Firecrawl, the context API for AI agents: search, scrape, parse, crawl, map, and interact with the web, run Agent and Monitor jobs, and search scientific papers (PubMed, bioRxiv, medRxiv, arXiv)
- [spider-client](internet.md#spider-client) - Python SDK for Spider Cloud API
- [django-ninja-extra](internet.md#django-ninja-extra) - Django Ninja Extra - Class Based Utility and more for Django Ninja(Fast Django REST framework)
- [mailman](communications-email.md#mailman) - Mailman -- the GNU mailing list manager
- [piccolo-admin](database-front-ends.md#piccolo-admin) - A powerful and modern admin interface / CMS, powered by Piccolo and ASGI.
- [repath](internet.md#repath) - Generate regular expressions form ExpressJS path patterns
- [AMQPStorm](communications.md#amqpstorm) - Thread-safe Python3 RabbitMQ Client & Management library.
- [scrapy-ingest](database.md#scrapy-ingest) - One pipeline. Full crawl observability in SQL or Elasticsearch.
- [django-revproxy](internet-proxy-servers.md#django-revproxy) - Yet another Django reverse proxy application
- [fastapi-debug-toolbar](internet.md#fastapi-debug-toolbar) - A debug toolbar for FastAPI.
- [mcpforunityserver](games-entertainment.md#mcpforunityserver) - MCP for Unity Server: A Unity package for Unity Editor integration via the Model Context Protocol (MCP).
- [workspace-mcp](communications-chat.md#workspace-mcp) - Comprehensive, highly performant Google Workspace Streamable HTTP & SSE MCP Server for Calendar, Gmail, Docs, Sheets, Slides & Drive
- [django-graphql-jwt](internet.md#django-graphql-jwt) - JSON Web Token for Django GraphQL.
- [django-ninja-jwt](internet.md#django-ninja-jwt) - Django Ninja JWT - JSON Web Token for Django-Ninja
- [arcp](internet.md#arcp) - arcp (Archive and Package) URI parser and generator
- [fastapi-restful](internet.md#fastapi-restful) - Quicker FastApi developing tools
- [odata-query](database.md#odata-query) - An OData query parser and transpiler.
- [rocrate](internet.md#rocrate) - RO-Crate metadata generator/parser
- [ws4py](communications.md#ws4py) - WebSocket client and server library for Python 2 and 3 as well as PyPy
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [fastapi-decorators](internet.md#fastapi-decorators) - Create decorators for your endpoints using FastAPI dependencies.
- [airium](database-front-ends.md#airium) - Easy and quick html builder with natural syntax correspondence (python->html). No templates needed. Serves pure pythonic library with no dependencies.
- [servestatic](communications-file-sharing.md#servestatic) - Production-grade static file server for Python WSGI & ASGI.
- [nvidia-sphinx-theme](documentation.md#nvidia-sphinx-theme) - A Sphinx theme for NVIDIA projects
- [jina](database-database-engines-servers.md#jina) - Multimodal AI services & pipelines with cloud-native stack: gRPC, Kubernetes, Docker, OpenTelemetry, Prometheus, Jaeger, etc.
- [crate](database.md#crate) - CrateDB Python Client
- [aiopenapi3](internet.md#aiopenapi3) - client and validator for OpenAPI3 3.0, OpenAPI 3.1, OpenAPI 3.2, Swagger 2.0
- [pywa](communications-chat.md#pywa) - 🚀 Build WhatsApp Bots in Python • Fast, Effortless, Powerful
- [h2o-wave](communications-chat.md#h2o-wave) - Python driver for H2O Wave Realtime Apps
- [grafana-client](communications.md#grafana-client) - A client library for accessing the Grafana HTTP API, written in Python
- [aiomisc](internet.md#aiomisc) - aiomisc - miscellaneous utils for asyncio
- [fastapi-cors](internet.md#fastapi-cors) - Simple env support of CORS settings for Fastapi applications
- [times](internet.md#times) - Times is a small, minimalistic, Python library for dealing with time conversions between universal time and arbitrary timezones.
- [django-graphiql-debug-toolbar](internet.md#django-graphiql-debug-toolbar) - Django Debug Toolbar for GraphiQL IDE.
- [pymediawiki](internet.md#pymediawiki) - Wikipedia and MediaWiki API wrapper for Python
- [minfraud](internet.md#minfraud) - MaxMind minFraud API
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [django-post_office](communications-email.md#django-post_office) - A Django app to monitor and send mail asynchronously, complete with template support.
- [twitter-ads](internet.md#twitter-ads) - A Twitter supported and maintained Ads API SDK for Python.
- [websockets-proxy](internet-proxy-servers.md#websockets-proxy) - Connect to websockets through a proxy server.
- [docarray](database-database-engines-servers.md#docarray) - The data structure for multimodal data
- [status](internet.md#status) - HTTP status code reporting for GET and POST requests
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
- [apitally](internet.md#apitally) - Simple API monitoring & analytics for REST APIs built with FastAPI, Flask, Django, Starlette, Litestar and BlackSheep.
- [TikTokLive](communications-chat.md#tiktoklive) - Unofficial TikTok LIVE API for Python: real-time chat, gift, like, follow and viewer events from any TikTok livestream.
- [fastapi-slim](internet.md#fastapi-slim) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [transferit-py](communications-file-sharing.md#transferit-py) - Pure-Python client for transfer.it — upload and download files via the MEGA backend, no browser required.
- [aioauth](internet.md#aioauth) - Asynchronous OAuth 2.0 framework for Python 3.
- [generic-connection-pool](database.md#generic-connection-pool) - generic connection pool
- [emoji-country-flag](communications-chat.md#emoji-country-flag) - En/Decode unicode country flags emoji
