# Adaptive Technologies

[Index](README.md) · 4 packages in this topic, by downloads.

### axe-playwright-python

Automated web accessibility testing using axe-core engine and Playwright.

`pip install axe-playwright-python` · installs (wheel) · licence: not stated · rank 5045 · last release 2026-07-24 · [PyPI](https://pypi.org/project/axe-playwright-python/) · [docs](https://pamelafox.github.io/axe-playwright-python) · [source](https://github.com/pamelafox/axe-playwright-python)

<details><summary>README extract</summary>

Automated web accessibility testing using axe-core engine
and Playwright.

- Full documentation.

- "Automated accessibility audits" - Pamela Fox (North Bay Python 2023)
- Using Python to Fix my Accessibility Night of a Website &
 Website Accessibility Audit Reports via GH Actions
 by Jay Miller

Example:
```python
from playwright.sync_api import sync_playwright
from axe_playwright_python.sync_playwright import Axe

axe = Axe()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("
    results = axe.run(page)
    browser.close()

print(f"Found {results.violations_count} violations.")
...
```

Sections: axe-playwright-python, Documentation, Further Reading & More, Dependencies, Usage

</details>

### sqlalchemy-cratedb

SQLAlchemy dialect for CrateDB.

`pip install sqlalchemy-cratedb` · installs (wheel) · licence: Apache Software License · rank 10131 · last release 2026-10-19 · [PyPI](https://pypi.org/project/sqlalchemy-cratedb/) · [docs](https://cratedb.com/docs/sqlalchemy-cratedb/) · [source](https://github.com/crate/sqlalchemy-cratedb)

<details><summary>README extract</summary>

The [SQLAlchemy] dialect for [CrateDB], based on the HTTP-based DBAPI client
library [crate-python].

Sections: SQLAlchemy dialect for CrateDB, About, Documentation and help

</details>

### tonsdk

Python SDK for TON

`pip install tonsdk` · installs (wheel) · licence: Apache Software License · rank 14626 · last release 2024-07-09 · [PyPI](https://pypi.org/project/tonsdk/) · [source](https://github.com/tonfactory/tonsdk)

<details><summary>README extract</summary>

This low-level Python library allows you to work with the TON blockchain.

- tonsdk/provider part is dirty.

Example:
```python
from abc import ABC, abstractmethod
import asyncio
import aiohttp
from tvm_valuetypes import serialize_tvm_stack

from tonsdk.provider import ToncenterClient, SyncTonlibClient, prepare_address, address_state
from tonsdk.utils import TonCurrencyEnum, from_nano
from tonsdk.boc import Cell

class AbstractTonClient(ABC):
    @abstractmethod
...
```

Sections: TONsdk, Description, Notes, How to use, General usage examples, Clients usage example (dirty)

</details>

### covalent

Covalent Workflow Tool

`pip install covalent` · installs from source (sdist only) · licence: Apache Software License · rank 14755 · last release 2025-05-14 · [PyPI](https://pypi.org/project/covalent/)

<details><summary>README extract</summary>

Run AI, ML, and Scientific Research Code on Any Cloud or On-Prem Cluster with a Single Line

Check our Quick Start Guide for setup instructions or dive into your First Experiment. Learn more on the Concepts.

Covalent is a Python library for AI/ML engineers, developers, and researchers. ...

Features:
Get a quick overview of what Covalent offers. Our infographic summarizes the main features, providing you with a snapshot of our capabilities:

Sections: What is Covalent?, Out-of-box observability - Try out the demo, Explore Covalent Through Examples, Explore Our Extensive Plugin Ecosystem, Key Features at a Glance, Know More About Covalent

</details>

