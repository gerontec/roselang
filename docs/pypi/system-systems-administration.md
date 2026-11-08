# System / Systems Administration

[Index](README.md) · 13 packages in this topic, 106 more listed under another topic, by downloads.

### python-dotenv

Read key-value pairs from a .env file and set them as environment variables

`pip install python-dotenv` · installs (wheel) · licence: BSD-3-Clause · rank 35 · last release 2026-10-01 · [PyPI](https://pypi.org/project/python-dotenv/) · [source](https://github.com/theskumar/python-dotenv)

<details><summary>README extract</summary>

[][build_status_link]
[][pypi_link]

python-dotenv reads key-value pairs from a `.env` file and can set them as
environment variables. It helps in the development of applications following the
12-factor principles.

- Getting Started ...

Example:
```python
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
```

...

</details>

### subprocess-tee

subprocess-tee

`pip install subprocess-tee` · installs (wheel) · licence: MIT License · rank 1758 · last release 2024-06-17 · [PyPI](https://pypi.org/project/subprocess-tee/) · [docs](https://subprocess-tee.readthedocs.io) · [source](https://github.com/pycontribs/subprocess-tee)

<details><summary>README extract</summary>

This package provides a drop-in alternative to `subprocess.run` that
captures the output while still printing it in real-time, just the way
`tee` does.

Printing output in real-time while still capturing is valuable for
any tool that executes long-running child processes. ...

Example:
```python
# from subprocess import run
from subprocess_tee import run

result = run("echo 123")
result.stdout == "123\n"
```

</details>

### enrich

enrich

`pip install enrich` · installs (wheel) · licence: MIT License · rank 3511 · last release 2022-01-10 · [PyPI](https://pypi.org/project/enrich/) · [source](https://github.com/pycontribs/enrich)

<details><summary>README extract</summary>

Enriched extends rich library functionality
with a set of changes that were not accepted to rich itself.

Example:
```python
from enrich.console import Console
import sys

console = Console(soft_wrap=True)
console.print(...)  # no longer need to pass soft_wrap to each print
```

Sections: enrich, Console with implicit soft wrapping, Console.print can also deal with ANSI escapes, Soft-wrapping logger

</details>

### selinux

shim selinux module

`pip install selinux` · installs (wheel) · licence: MIT License · rank 4165 · last release 2022-12-24 · [PyPI](https://pypi.org/project/selinux/) · [source](https://github.com/pycontribs/selinux)

<details><summary>README extract</summary>

Pure-python selinux shim module for use in virtualenvs in order to avoid
failure to load selinux in Ansible modules.

You still need to have libselinux python bindings package installed on your
system for it to work but you no longer have the problem of not being able
to import it from inside isolated (default) virtualenvs. ...

</details>

### ps-mem

A utility to report core memory usage per program

`pip install ps-mem` · installs (wheel) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 4561 · last release 2022-05-28 · [PyPI](https://pypi.org/project/ps-mem/)

_README extract left out: share-alike licence._

### doc8

Style checker for Sphinx (or other) RST documentation

`pip install doc8` · installs (wheel) · licence: Apache-2.0 · rank 5572 · last release 2025-06-13 · [PyPI](https://pypi.org/project/doc8/) · [docs](https://doc8.readthedocs.io)

<details><summary>README extract</summary>

*doc8* is an *opinionated* style checker for rst_ (with basic support for
plain text) styles of documentation.


Example:
```python
$ doc8  -h

usage: doc8 [-h] [--config path] [--allow-long-titles] [--ignore code]
            [--no-sphinx] [--ignore-path path] [--ignore-path-errors path]
            [--default-extension extension] [--file-encoding encoding]
            [--max-line-length int] [-e extension] [-v] [--version]
            [path [path ...]]

...
```

Sections: doc8, Quick start, Usage, INI file usage, Option conflict resolution, API

</details>

### git-url-parse

git-url-parse - A simple GIT URL parser.

`pip install git-url-parse` · installs (wheel) · licence: MIT License · rank 7755 · last release 2019-03-23 · [PyPI](https://pypi.org/project/git-url-parse/)

<details><summary>README extract</summary>

A simple GIT URL parser similar to giturlparse.py.

Sections: giturlparse, Documentation

</details>

### molecule-docker

Molecule aids in the development and testing of Ansible roles

`pip install molecule-docker` · installs (wheel) · licence: MIT License · rank 8849 · last release 2022-09-29 · [PyPI](https://pypi.org/project/molecule-docker/) · [docs](https://molecule.readthedocs.io) · [source](https://github.com/ansible-community/molecule-docker)

<details><summary>README extract</summary>

Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

Please note that this driver is currently in its early stage of development.

This plugin will function only if you also install `community.docker` ansible
collection. ...

Sections: Molecule Docker Plugin, Get Involved, FAQ

</details>

### molecule-vagrant

Vagrant Molecule Plugin :: run molecule tests using Vagrant

`pip install molecule-vagrant` · installs (wheel) · licence: MIT License · rank 10659 · last release 2023-01-06 · [PyPI](https://pypi.org/project/molecule-vagrant/) · [source](https://github.com/ansible-community/molecule-vagrant)

<details><summary>README extract</summary>

Molecule Vagrant is designed to allow use of Vagrant for provisioning of test
resources.

Sections: Molecule Vagrant Plugin, Documentation, Get Involved

</details>

### pip-review

pip-review lets you smoothly manage all available PyPI updates.

`pip install pip-review` · installs from source (sdist only) · licence: BSD License · rank 11451 · last release 2022-11-29 · [PyPI](https://pypi.org/project/pip-review/)

<details><summary>README extract</summary>

*Looking for a new maintainer! See

`pip-review` is a convenience wrapper around `pip`. It can list available updates by deferring to `pip list --outdated`. It can also automatically or interactively install available updates for you by deferring to `pip install`.

Example, report-only:

Example, actually install everything: ...

Sections: pip-review, Origins

</details>

### pigeon-home-runner

Self-hosted, email-driven agent: tell your cloud SI to send signed jobs via email that execute on your machine.

`pip install pigeon-home-runner` · installs (wheel) · licence: Apache Software License · rank 11690 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pigeon-home-runner/) · [docs](https://github.com/Pigeon-Home/homing-pigeon#readme) · [source](https://github.com/Pigeon-Home/homing-pigeon)

<details><summary>README extract</summary>

Works with Muse, Grok, ChatGPT, Claude, Gemini, Copilot, or any assistant that can send a message.

> ⚠️ USE AT YOUR OWN RISK. Installing this application hands full administrative
> control of the system to whoever holds the shared secret. The holder
> can install software, read files, add users, and pivot to your network. ...

Features:
Homing Pigeon is a personal remote-development agent. The point is not
that the SI becomes smarter. It is that the SI gets a way to delegate
work to a computer it could not otherwise reach. ...

...

</details>

### AuthEncoding

Framework for handling LDAP style password hashes.

`pip install AuthEncoding` · installs (wheel) · licence: ZPL-2.1 · rank 13130 · last release 2026-09-17 · [PyPI](https://pypi.org/project/AuthEncoding/) · [source](https://github.com/zopefoundation/AuthEncoding)

<details><summary>README extract</summary>

Features:
AuthEncoding is a framework for handling LDAP style password hashes.

It is used in Zope but does not depend on any other Zope package.

Sections: Overview, 6.1 (2026-09-17), 6.0 (2024-02-26), 5.0 (2023-01-12), 4.3 (2021-06-29), 4.2.1 (2021-04-08), 4.2 (2020-09-30), 4.1 (2018-10-30), 4.0.0 (2015-09-30), 3.0.0 (2015-09-28)

</details>

### crudini

A utility for manipulating ini files

`pip install crudini` · installs (wheel) · licence: GNU General Public License v2 (GPLv2) · rank 13479 · last release 2025-04-16 · [PyPI](https://pypi.org/project/crudini/)

_README extract left out: share-alike licence._

## Also in this topic

- [setuptools](software-development-libraries.md#setuptools) - Most extensible Python build backend with support for C/C++ extension modules
- [psutil](software-development-libraries.md#psutil) - Cross-platform lib for process and system monitoring.
- [invoke](software-development.md#invoke) - Pythonic task execution
- [humanfriendly](communications.md#humanfriendly) - Human friendly output for text interfaces using Python
- [fqdn](internet.md#fqdn) - Validates fully-qualified domain names against RFC 1123, so that they are acceptable to modern browsers
- [coloredlogs](communications.md#coloredlogs) - Colored terminal output for Python's logging module
- [nvidia-ml-py](software-development-libraries.md#nvidia-ml-py) - Python Bindings for the NVIDIA Management Library
- [ansible-core](system-installation-setup.md#ansible-core) - Radically simple IT automation
- [ldap3](software-development-libraries.md#ldap3) - A strictly RFC 4510 conforming LDAP V3 pure Python client library
- [pip-tools](software-development-quality-assurance.md#pip-tools) - pip-tools keeps your pinned dependencies fresh.
- [rq](internet.md#rq) - RQ is a simple, lightweight, library for creating background jobs, and processing them.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [c7n-org](system-distributed-computing.md#c7n-org) - Cloud Custodian - Parallel Execution
- [supervisor](system-boot.md#supervisor) - A system for controlling process state under UNIX
- [fabric](software-development.md#fabric) - High level SSH command execution
- [python3-openid](internet-www-http.md#python3-openid) - OpenID support for modern servers and consumers.
- [plumbum](software-development-build-tools.md#plumbum) - Plumbum: shell combinators library
- [ndg-httpsclient](internet.md#ndg-httpsclient) - Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
- [ansible-compat](software-development-bug-tracking.md#ansible-compat) - Ansible compatibility goodies
- [port-for](internet-www-http.md#port-for) - Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.
- [arq](internet.md#arq) - Job queues in python with asyncio and redis
- [ansible-lint](software-development-quality-assurance.md#ansible-lint) - Checks playbooks for practices and behavior that could potentially be improved
- [pip-licenses](system-system-shells.md#pip-licenses) - Dump the software license list of Python packages installed with pip.
- [magic-wormhole](security-cryptography.md#magic-wormhole) - Securely transfer data between computers
- [pytest-github-actions-annotate-failures](software-development-quality-assurance.md#pytest-github-actions-annotate-failures) - pytest plugin to annotate failed tests with a workflow command for GitHub Actions
- [python-ldap](database.md#python-ldap) - Python modules for implementing LDAP clients
- [pip-system-certs](security-cryptography.md#pip-system-certs) - Automatically configures Python to use system certificates via truststore
- [django-two-factor-auth](security.md#django-two-factor-auth) - Complete Two-Factor Authentication for Django
- [pynvml](software-development-libraries.md#pynvml) - Python utilities for the NVIDIA Management Library
- [pywinrm](software-development-libraries.md#pywinrm) - Python library for Windows Remote Management
- [crowdstrike-falconpy](security.md#crowdstrike-falconpy) - The CrowdStrike Falcon SDK for Python
- [molecule](software-development-bug-tracking.md#molecule) - Molecule aids in the development and testing of Ansible roles
- [ansi2html](software-development-quality-assurance.md#ansi2html) - Convert text with ANSI color codes to HTML or to LaTeX
- [ansible-runner](software-development-libraries-2.md#ansible-runner) - "Consistent Ansible Python API and CLI with container and process isolation runtime capabilities"
- [rpyc](internet.md#rpyc) - Remote Python Call (RPyC) is a transparent and symmetric distributed computing library
- [ldaptor](software-development-libraries-2.md#ldaptor) - A Pure-Python Twisted library for LDAP
- [c7n](system-distributed-computing.md#c7n) - Cloud Custodian - Policy Rules Engine
- [pykerberos](software-development-libraries-2.md#pykerberos) - High-level interface to Kerberos
- [certbot](internet-www-http.md#certbot) - ACME client
- [pytest-testinfra](software-development-testing.md#pytest-testinfra) - Test infrastructures
- [molecule-plugins](software-development-bug-tracking.md#molecule-plugins) - Molecule Plugins
- [pyroute2](software-development-libraries-2.md#pyroute2) - Python Netlink library
- [django-rq](internet.md#django-rq) - An app that provides django integration for RQ (Redis Queue)
- [certbot-dns-cloudflare](internet-www-http.md#certbot-dns-cloudflare) - Cloudflare DNS Authenticator plugin for Certbot
- [python-hostlist](system-clustering.md#python-hostlist) - Python module for hostlist handling
- [kerberos](software-development-libraries-2.md#kerberos) - Kerberos high-level interface
- [flameprof](internet.md#flameprof) - cProfile flamegraph generator
- [django-encrypted-model-fields](internet-www-http.md#django-encrypted-model-fields) - A set of fields that wrap standard Django fields with encryption provided by the python cryptography library.
- [nvidia-ml-py3](software-development-libraries-2.md#nvidia-ml-py3) - Python Bindings for the NVIDIA Management Library
- [ansible-builder](software-development-build-tools.md#ansible-builder) - A tool for building Ansible Execution Environments
- [verboselogs](software-development.md#verboselogs) - Verbose logging level for Python's logging module
- [proxmoxer](software-development-libraries-2.md#proxmoxer) - Python Wrapper for the Proxmox 2.x API (HTTP and SSH)
- [contractions](software-development.md#contractions) - Fixes contractions such as `you're` to you `are`
- [django-auth-ldap](internet-www-http.md#django-auth-ldap) - Django LDAP authentication backend
- [dlipower](software-development-libraries-2.md#dlipower) - Control digital loggers web power switch
- [rq-dashboard](internet.md#rq-dashboard) - rq-dashboard is a general purpose, lightweight, web interface to monitor your RQ queues, jobs, and workers in realtime.
- [saq](internet.md#saq) - Distributed Python job queue with asyncio and redis
- [pamela](software-development-libraries-3.md#pamela) - PAM interface using ctypes
- [bitmath](communications-file-sharing.md#bitmath) - Pythonic module for representing and manipulating file sizes with different prefix notations (file size unit conversion)
- [getmac](software-development-libraries-3.md#getmac) - Get MAC addresses of remote hosts and local interfaces
- [cloudsmith-cli](internet.md#cloudsmith-cli) - Cloudsmith Command-Line Interface (CLI)
- [pyrad](software-development-libraries-3.md#pyrad) - RADIUS tools
- [pyzabbix](system-monitoring.md#pyzabbix) - Zabbix API Python interface
- [ansible-sign](software-development-quality-assurance.md#ansible-sign) - Ansible content validation library and CLI
- [yagmail](communications-email.md#yagmail) - Yet Another GMAIL client
- [npmai-agents](office-business-scheduling.md#npmai-agents) - Production-grade autonomous AI agent framework with 1,371 tools across 100 classes and a 5-role LLM pipeline — built on the NPMAI ECOSYSTEM.
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [nvitop](system-hardware.md#nvitop) - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.
- [pyinfra](system-installation-setup.md#pyinfra) - pyinfra automates/provisions/manages/deploys infrastructure.
- [tailer](software-development-libraries-3.md#tailer) - Python tail is a simple implementation of GNU tail and head.
- [awxkit](system-software-distribution.md#awxkit) - The official command line interface for Ansible AWX
- [mechanize](internet.md#mechanize) - Stateful, programmatic web browsing
- [zabbix-utils](system-monitoring.md#zabbix-utils) - A library with modules for working with Zabbix (Zabbix API, Zabbix sender, Zabbix get)
- [python-openid](internet-www-http.md#python-openid) - OpenID support for servers and consumers.
- [redislite](software-development-libraries-3.md#redislite) - Redis built into a python package
- [executor](internet.md#executor) - Programmer friendly subprocess wrapper
- [mitogen](system-distributed-computing.md#mitogen) - Library for writing distributed self-replicating programs.
- [sqlalchemy-cratedb](adaptive-technologies.md#sqlalchemy-cratedb) - SQLAlchemy dialect for CrateDB.
- [ansible-tower-cli](system-software-distribution.md#ansible-tower-cli) - A CLI tool for Ansible Tower and AWX.
- [cot](software-development-libraries-3.md#cot) - Common OVF Tool
- [google-compute-engine](internet.md#google-compute-engine) - Google Compute Engine
- [poetry-dotenv-plugin](software-development.md#poetry-dotenv-plugin) - A Poetry plugin to automatically load environment variables from .env files
- [ansible-base](system-installation-setup.md#ansible-base) - Radically simple IT automation
- [octodns](internet-name-service-dns.md#octodns) - OctoDNS: DNS as code - Tools for managing DNS across multiple providers
- [pip-licenses-cli](system-system-shells.md#pip-licenses-cli) - Dump the software license list of Python packages installed with pip.
- [certbot-dns-route53](internet-www-http-2.md#certbot-dns-route53) - Route53 DNS Authenticator plugin for Certbot
- [pysphere](software-development-libraries-4.md#pysphere) - Python API for interacting with the vSphere Web Services SDK
- [python-freeipa](software-development-libraries-4.md#python-freeipa) - Lightweight FreeIPA client
- [testinfra](software-development-testing.md#testinfra) - Test infrastructures
- [certbot-nginx](internet-www-http-2.md#certbot-nginx) - Nginx plugin for Certbot
- [libucx-cu13](system-hardware.md#libucx-cu13) - The Unified Communication X library (UCX)
- [hashin](software-development-build-tools.md#hashin) - Edits your requirements.txt by hashing them in
- [ucxx-cu13](software-development-libraries-4.md#ucxx-cu13) - Python Bindings for the Unified Communication X library (UCX)
- [libucxx-cu13](software-development-libraries-4.md#libucxx-cu13) - Python Bindings for the Unified Communication X library (UCX)
- [py3-wget](communications-file-sharing.md#py3-wget) - A tool to download files. It supports progress bar, cksum, timeout, retry failed download.
- [dns-lexicon](internet-name-service-dns.md#dns-lexicon) - Manipulate DNS records on various DNS providers in a standardized/agnostic way
- [superlance](system-boot.md#superlance) - superlance plugins for supervisord
- [piper](scientific-engineering-bio-informatics.md#piper) - A lightweight python toolkit for gluing together restartable, robust command line pipelines
- [pyrsmi](software-development-libraries-4.md#pyrsmi) - Python System Management Library for AMD GPUs
- [python-kadmin-rs](software-development-libraries-4.md#python-kadmin-rs) - Python interface to the Kerberos administration interface (kadm5)
- [fabric2](software-development.md#fabric2) - High level SSH command execution
- [libucx-cu12](system-hardware.md#libucx-cu12) - The Unified Communication X library (UCX)
- [Fabric3](software-development.md#fabric3) - Fabric is a simple, Pythonic tool for remote execution and deployment (py2.7/py3.4+ compatible fork).
- [spaceforge](software-development-libraries-5.md#spaceforge) - A Python framework for building Spacelift plugins
- [aws-google-auth](security.md#aws-google-auth) - Acquire AWS STS (temporary) credentials via Google Apps SAML Single Sign On
- [django-allauth-ui](internet-www-http-2.md#django-allauth-ui) - 
