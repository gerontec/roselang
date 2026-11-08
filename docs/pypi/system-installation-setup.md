# System / Installation/Setup

[Index](README.md) · 4 packages in this topic, 23 more listed under another topic, by downloads.

### ansible-core

Radically simple IT automation

`pip install ansible-core` · installs (wheel) · licence: GPL-3.0-or-later · rank 959 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ansible-core/) · [docs](https://docs.ansible.com/ansible-core/) · [source](https://github.com/ansible/ansible/)

_README extract left out: share-alike licence._

### django-crontab

dead simple crontab powered job scheduling for django

`pip install django-crontab` · installs from source (sdist only) · licence: MIT License · rank 8108 · last release 2016-03-07 · [PyPI](https://pypi.org/project/django-crontab/)

<details><summary>README extract</summary>

dead simple crontab powered job scheduling for django (1.8+).

install via pip:
add it to installed apps in django settings.py:
now create a new method that should be executed by cron every 5 minutes, f.e. ...

Example:
```python
def my_scheduled_job():
  pass
```

Sections: about, setup, config, faq

</details>

### pyinfra

pyinfra automates/provisions/manages/deploys infrastructure.

`pip install pyinfra` · installs (wheel) · licence: MIT · rank 8214 · last release 2026-07-27 · [PyPI](https://pypi.org/project/pyinfra/) · [docs](https://docs.pyinfra.com) · [source](https://github.com/pyinfra-dev/pyinfra)

<details><summary>README extract</summary>

pyinfra turns Python code into shell commands and runs them on your servers. Execute ad-hoc commands and write declarative operations. Target SSH servers, local machine and Docker containers. Fast and scales from one server to thousands. Think ansible but Python instead of YAML, and a lot faster.

Example:
```python
from pyinfra.operations import apt

apt.packages(
    name="Ensure iftop is installed",
    packages=['iftop'],
    update=True,
    _sudo=True,
)
```

Sections: Getting Started •, Quickstart

</details>

### ansible-base

Radically simple IT automation

`pip install ansible-base` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 11195 · last release 2022-01-31 · [PyPI](https://pypi.org/project/ansible-base/) · [docs](https://docs.ansible.com/ansible/) · [source](https://github.com/ansible/ansible)

_README extract left out: share-alike licence._

## Also in this topic

- [tqdm](desktop-environment.md#tqdm) - Fast, Extensible Progress Meter
- [pexpect](software-development.md#pexpect) - Pexpect allows easy control of interactive console applications.
- [progressbar2](desktop-environment.md#progressbar2) - A Python Progressbar library to provide visual (yet text based) progress to long running operations.
- [pyinstaller](software-development.md#pyinstaller) - PyInstaller bundles a Python application and all its dependencies into a single package.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [port-for](internet-www-http.md#port-for) - Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.
- [shtab](desktop-environment.md#shtab) - Automagic shell tab completion for Python CLI applications
- [certbot](internet-www-http.md#certbot) - ACME client
- [geckodriver-autoinstaller](software-development-libraries-2.md#geckodriver-autoinstaller) - Automatically install geckodriver that supports the currently installed version of chrome.
- [certbot-dns-cloudflare](internet-www-http.md#certbot-dns-cloudflare) - Cloudflare DNS Authenticator plugin for Certbot
- [frappe-bench](software-development-build-tools.md#frappe-bench) - CLI to manage Multi-tenant deployments for Frappe apps
- [feu](scientific-engineering.md#feu) - A lightweight Python library for managing packages and versions across different Python environments
- [chromedriver-autoinstaller](software-development-libraries-3.md#chromedriver-autoinstaller) - Automatically install chromedriver that supports the currently installed version of chrome.
- [to-requirements.txt](software-development.md#to-requirementstxt) - Automatically add and delete modules to requirements.txt installing them using pip.
- [setupmeta](software-development-build-tools.md#setupmeta) - Simplify your setup.py
- [cot](software-development-libraries-3.md#cot) - Common OVF Tool
- [google-compute-engine](internet.md#google-compute-engine) - Google Compute Engine
- [chromedriver-binary](software-development-libraries-4.md#chromedriver-binary) - Installer for chromedriver.
- [certbot-dns-route53](internet-www-http-2.md#certbot-dns-route53) - Route53 DNS Authenticator plugin for Certbot
- [pyrig](software-development-build-tools.md#pyrig) - A Python project setup and management tool built on infrastructure as code and convention over configuration.
- [certbot-nginx](internet-www-http-2.md#certbot-nginx) - Nginx plugin for Certbot
- [hashin](software-development-build-tools.md#hashin) - Edits your requirements.txt by hashing them in
- [jumpssh](software-development.md#jumpssh) - Python library for remote ssh calls through a gateway.
