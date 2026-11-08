# Security

[Index](README.md) · 135 packages in this topic, 57 more listed under another topic, by downloads.

### SecretStorage

Python bindings to FreeDesktop.org Secret Service API

`pip install SecretStorage` · installs (wheel) · licence: BSD-3-Clause · rank 222 · last release 2025-11-23 · [PyPI](https://pypi.org/project/SecretStorage/) · [docs](https://secretstorage.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring,
KWallet (since version 5.97) and KeePassXC. ...

Sections: Module description, Building the module, Get the code

</details>

### joserfc

The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT

`pip install joserfc` · installs (wheel) · licence: BSD License · rank 267 · last release 2026-11-03 · [PyPI](https://pypi.org/project/joserfc/) · [docs](https://jose.authlib.org/) · [source](https://github.com/authlib/joserfc)

<details><summary>README extract</summary>

`joserfc` is a Python library that provides a comprehensive implementation of several
essential JSON Object Signing and Encryption (JOSE) standards.

This package contains implementation of:

- RFC7515: JSON Web Signature
- RFC7516: JSON Web Encryption
- RFC7517: JSON Web Key
- RFC7518: JSON Web Algorithms
- RFC7519: JSON Web Token ...

Example:
```python
>>> from joserfc import jwt, jwk
>>> key = jwk.import_key("your-secret-key", "oct")
>>> encoded_jwt = jwt.encode({"alg": "HS256"}, {"k": "value"}, key)
>>> encoded_jwt
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrIjoidmFsdWUifQ._M8ViO_GK6TnZ9G9eqdlS7IpNWzhoGwaYYDQ3hEwwmA'
>>> token = jwt.decode(encoded_jwt, key)
>>> token.header
...
```

Sections: JOSE RFC, Usage, Useful Links

</details>

### argon2-cffi-bindings

Low-level CFFI bindings for Argon2

`pip install argon2-cffi-bindings` · installs (wheel) · licence: MIT · rank 340 · last release 2026-08-20 · [PyPI](https://pypi.org/project/argon2-cffi-bindings/) · [source](https://github.com/hynek/argon2-cffi-bindings)

<details><summary>README extract</summary>

*argon2-cffi-bindings* provides low-level CFFI bindings to the official implementation of the [Argon2] password hashing algorithm.

<!-- [[[cog

import subprocess
out = subprocess.check_output(["git", "submodule"], text=True)
id = out.strip().split(" ", 1)[0]
link = f'[`{id[:7]}`](
print(f"The currently vendored Argon2 commit ID is {link}.")
]]] ...

Example:
```python
from _argon2_cffi_bindings import ffi, lib
```

Sections: Low-level Python CFFI Bindings for Argon2, Extract commit ID; refresh using `tox -e cog-render`, Usage, Disabling Vendored Code, Overriding Automatic SSE2 Detection, Python API, Project Information, Vendored Code, argon2-cffi-bindings* for Enterprise

</details>

### cyclonedx-python-lib

Python library for CycloneDX

`pip install cyclonedx-python-lib` · installs (wheel) · licence: Apache Software License · rank 510 · last release 2026-08-13 · [PyPI](https://pypi.org/project/cyclonedx-python-lib/) · [docs](https://cyclonedx-python-library.readthedocs.io/) · [source](https://github.com/CycloneDX/cyclonedx-python-lib)

<details><summary>README extract</summary>

[![shield_pypi-version]][link_pypi]
[![shield_conda-forge-version]][link_conda-forge]
[![shield_rtfd]][link_rtfd]
[![shield_gh-workflow-test]][link_gh-workflow-test]
[![shield_coverage]][link_codacy]
[![shield_ossf-best-practices]][link_ossf-best-practices]
[![shield_license]][license_file]
[![shield_website]][link_website]
[![shield_slack]][link_s ...

Sections: CycloneDX Python Library, Documentation

</details>

### pip-audit

A tool for scanning Python environments for known vulnerabilities

`pip install pip-audit` · installs (wheel) · licence: Apache Software License · rank 576 · last release 2026-06-10 · [PyPI](https://pypi.org/project/pip-audit/) · [source](https://github.com/pypa/pip-audit)

<details><summary>README extract</summary>

<!--- BADGES: START --->

<!--- BADGES: END --->

`pip-audit` is a tool for scanning Python environments for packages
with known vulnerabilities. It uses the Python Packaging Advisory Database
( via the
PyPI JSON API as a source
of vulnerability reports.

This project is maintained in part by Trail of Bits
with support from Google. ...

Features:
* Support for auditing local environments and requirements-style files
* Support for multiple vulnerability services
 (PyPI,
 OSV)
* Support for emitting
 SBOMs in
 CycloneDX XML or JSON
* Support for automatically fixing vulnerable dependencies ...

...

</details>

### bandit

Security oriented static analyser for python code.

`pip install bandit` · installs (wheel) · licence: Apache-2.0 · rank 669 · last release 2026-02-25 · [PyPI](https://pypi.org/project/bandit/) · [docs](https://bandit.readthedocs.io/) · [source](https://github.com/PyCQA/bandit)

<details><summary>README extract</summary>

A security linter from PyCQA

* Free software: Apache license

Features:
Bandit is a tool designed to find common security issues in Python code. To do
this Bandit processes each file, builds an AST from it, and runs appropriate
plugins against the AST nodes. ...

Sections: Overview, Show Your Style, References, Container Images

</details>

### semgrep

Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.

`pip install semgrep` · installs (wheel) · licence: LGPL-2.1-or-later · rank 771 · last release 2026-11-05 · [PyPI](https://pypi.org/project/semgrep/) · [docs](https://semgrep.dev/docs) · [source](https://github.com/semgrep/semgrep)

_README extract left out: share-alike licence._

### id

A tool for generating OIDC identities

`pip install id` · installs (wheel) · licence: Apache Software License · rank 849 · last release 2026-02-04 · [PyPI](https://pypi.org/project/id/) · [source](https://github.com/di/id)

<details><summary>README extract</summary>

<!--- @begin-badges@ --->

<!--- @end-badges@ --->

`id` is a Python tool for generating OIDC identities. It can automatically
detect and produce OIDC credentials on a number of environments, including
GitHub Actions, GitLab pipelines and Google Cloud.

Example:
```python
>>> from id import detect_credential
>>> detect_credential(audience='something')
'<OIDC token>'
```

Sections: id, Usage, Tokens in environment variables, Licensing, SLSA Provenance

</details>

### jwcrypto

Implementation of JOSE Web standards

`pip install jwcrypto` · installs (wheel) · licence: LGPL-3.0-or-later · rank 875 · last release 2026-09-15 · [PyPI](https://pypi.org/project/jwcrypto/)

_README extract left out: share-alike licence._

### blake3

Python bindings for the Rust blake3 crate

`pip install blake3` · installs (wheel) · licence: CC0-1.0 OR Apache-2.0 · rank 916 · last release 2026-10-08 · [PyPI](https://pypi.org/project/blake3/) · [source](https://github.com/oconnor663/blake3-py)

<details><summary>README extract</summary>

Python bindings for the official Rust implementation of
BLAKE3, based on
PyO3. These bindings expose all the features of
BLAKE3, including extendable output, keying, and multithreading. The basic API
matches that of Python's standard
`hashlib` module.

Example:
```python
from blake3 import blake3

# Hash some input all at once. The input can be bytes, a bytearray, or a memoryview.
hash1 = blake3(b"foobarbaz").digest()

# Hash the same input incrementally.
hasher = blake3()
hasher.update(b"foo")
hasher.update(b"bar")
hasher.update(b"baz")
hash2 = hasher.digest()
assert hash1 == hash2

...
```

Sections: blake3-py, Examples, C Bindings

</details>

### oletools

Python tools to analyze security characteristics of MS Office and OLE files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), for Malware Analysis and Incident Response #DFIR

`pip install oletools` · installs (wheel) · licence: BSD License · rank 1204 · last release 2024-07-02 · [PyPI](https://pypi.org/project/oletools/)

<details><summary>README extract</summary>

|Say Thanks!|

oletools is a package of
python tools to analyze Microsoft OLE2
files
(also called Structured Storage, Compound File Binary Format or Compound
Document File Format), such as Microsoft Office 97-2003 documents, MSI
files or Outlook messages, mainly for malware analysis, forensics and
debugging. It is based on the
olefile parser. ...

Sections: python-oletools, News, Tools, Tools to analyze malicious documents, Tools to analyze the structure of OLE files, Projects using oletools, Documentation

</details>

### pcodedmp

A VBA p-code disassembler

`pip install pcodedmp` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 1214 · last release 2019-07-30 · [PyPI](https://pypi.org/project/pcodedmp/)

_README extract left out: share-alike licence._

### RestrictedPython

RestrictedPython is a defined subset of the Python language which allows to provide a program input into a trusted environment.

`pip install RestrictedPython` · installs (wheel) · licence: ZPL-2.1 · rank 1294 · last release 2026-11-04 · [PyPI](https://pypi.org/project/RestrictedPython/) · [docs](https://restrictedpython.readthedocs.io/) · [source](https://github.com/zopefoundation/RestrictedPython)

<details><summary>README extract</summary>

RestrictedPython is a tool that helps to define a subset of the Python language which allows to provide a program input into a trusted environment.
RestrictedPython is not a sandbox system or a secured environment, but it helps to define a trusted environment and execute untrusted code inside of it.

For full documentation please see

Features:
- Update setuptools version pin.
 (#292)

Example:
```python
>>> from RestrictedPython import compile_restricted
>>> from RestrictedPython import safe_globals
>>>
>>> source_code = """
... def example():
...     return 'Hello World!'
... """
>>>
>>> loc = {}
>>> byte_code = compile_restricted(source_code, '<inline>', 'exec')
>>> exec(byte_code, safe_globals, loc)
>>>
>>> loc'example'
'Hello World!'
```

...

</details>

### PGPy

Pretty Good Privacy for Python

`pip install PGPy` · installs from source (sdist only) · licence: BSD License · rank 1377 · last release 2022-11-24 · [PyPI](https://pypi.org/project/PGPy/) · [docs](https://pgpy.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

`PGPy` is a Python library for implementing Pretty Good Privacy into Python programs, conforming to the OpenPGP specification per RFC 4880.

Features:
Currently, PGPy can load keys and signatures of all kinds in both ASCII armored and binary formats.

It can create and verify RSA, DSA, and ECDSA signatures, at the moment. It can also encrypt and decrypt messages using RSA and ECDH.

Sections: PGPy: Pretty Good Privacy for Python, Features, Documentation, Discussion, Requirements

</details>

### checkov

Infrastructure as code static analysis

`pip install checkov` · installs (wheel) · licence: Apache Software License · rank 1797 · last release 2026-11-02 · [PyPI](https://pypi.org/project/checkov/)

<details><summary>README extract</summary>

Checkov is a static code analysis tool for infrastructure as code (IaC) and also a software composition analysis (SCA) tool for images and open source packages.

It scans cloud infrastructure provisioned using Terraform, Terraform plan, Cloudformation, AWS SAM, Kubernetes, Helm charts, Kustomize, Dockerfile, Serverless, Bicep, OpenAPI, ARM ...

Sections: Screenshots, Getting started, Requirements, Upgrade, Configure an input folder or file, Scan result sample (CLI), Using Docker, Running or skipping checks, Examples, Suppressing/Ignoring a check, Suppression comment format, Example, Logging, Skipping directories

</details>

### django-otp

A pluggable framework for adding two-factor authentication to Django using one-time passwords.

`pip install django-otp` · installs (wheel) · licence: Unlicense · rank 1831 · last release 2026-10-16 · [PyPI](https://pypi.org/project/django-otp/) · [docs](https://django-otp-official.readthedocs.io/)

<details><summary>README extract</summary>

This project makes it easy to add support for one-time passwords (OTPs) to Django. It can be
integrated at various levels, depending on how much customization is required.
It integrates with `django.contrib.auth`, although it is not a Django
authentication backend. ...

Sections: django-otp, Configuration, The Future

</details>

### zxcvbn

(no summary)

`pip install zxcvbn` · installs (wheel) · licence: MIT License · rank 1890 · last release 2025-02-19 · [PyPI](https://pypi.org/project/zxcvbn/)

<details><summary>README extract</summary>

A realistic password strength estimator.

This is a Python implementation of the library created by the team at Dropbox.
The original library, written for JavaScript, can be found
here.

While there may be other Python ports available, this one is the most up
to date and is recommended by the original developers of zxcvbn at this
time.

Features:
- Tested in Python versions 3.8-3.13
- Accepts user data to be added to the dictionaries that are tested against (name, birthdate, etc)
- Gives a score to the password, from 0 (terrible) to 4 (great) ...

Example:
```python
from zxcvbn import zxcvbn

results = zxcvbn('JohnSmith123', user_inputs=['John', 'Smith'])

print(results)
```

Sections: zxcvbn, Features, Usage, Custom Ranked Dictionaries, CLI

</details>

### pwdlib

Modern password hashing for Python

`pip install pwdlib` · installs (wheel) · licence: MIT License · rank 2010 · last release 2026-08-12 · [PyPI](https://pypi.org/project/pwdlib/) · [docs](https://frankie567.github.io/pwdlib/) · [source](https://github.com/frankie567/pwdlib)

<details><summary>README extract</summary>

Modern password hashing for Python

Documentation:

Source Code:

Features:
For years, the de-facto standard to hash passwords was `passlib`. Unfortunately, it has not been very active recently and its maintenance status is under question. Starting Python 3.13, `passlib` won't work anymore. ...

Example:
```python
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
hash = password_hash.hash("herminetincture")
password_hash.verify("herminetincture", hash)  # True
```

Sections: pwdlib, Quickstart, Why `pwdlib`?, Setup environment, Run unit tests, Format the code, Publish a new version, Serve the documentation

</details>

### safety

Scan dependencies for known vulnerabilities and licenses.

`pip install safety` · installs (wheel) · licence: MIT · rank 2069 · last release 2026-05-29 · [PyPI](https://pypi.org/project/safety/) · [docs](https://docs.safetycli.com/safety-docs) · [source](https://github.com/pyupio/safety)

<details><summary>README extract</summary>

> [!NOTE]
> Come and join us at SafetyCLI. We are hiring for various roles.

Features:
- Versatile, comprehensive dependency security scanning for Python packages.
- Leverages Safety DB, the most comprehensive vulnerability data available for Python.
- Clear output with detailed recommendations for vulnerability remediation. ...

Sections: Introduction, Key Features, Getting Started, GitHub Action, Command Line Interface, 2. Log In or Register, 3. Running Your First Scan, Basic Commands, Service-Level Agreement (SLA), Detailed Documentation, Resources

</details>

### ast-grep-cli

Structural Search and Rewrite code at large scale using precise AST pattern.

`pip install ast-grep-cli` · installs (wheel) · licence: MIT License · rank 2132 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ast-grep-cli/) · [docs](https://ast-grep.github.io/) · [source](https://github.com/ast-grep/ast-grep)

<details><summary>README extract</summary>

ast-grep(sg) is a CLI tool for code structural search, lint, and rewriting.

ast-grep is an abstract syntax tree based tool to search code by pattern code. Think of it as your old-friend `grep`, but matching AST nodes instead of text.
You can write patterns as if you are writing ordinary code. ...

Features:
ast-grep's core is an algorithm to search and replace code based on abstract syntax tree produced by tree-sitter.
It can help you to do lightweight static analysis and massive scale code manipulation in an intuitive way.

Key highlights: ...

Sections: ast-grep(sg), Introduction, Screenshot, Command line usage example, Example, Feature Highlight

</details>

### scapy

Scapy: interactive packet manipulation tool

`pip install scapy` · installs (wheel) · licence: GPL-2.0-only · rank 2138 · last release 2026-10-02 · [PyPI](https://pypi.org/project/scapy/) · [docs](https://scapy.readthedocs.io) · [source](https://github.com/secdev/scapy)

_README extract left out: share-alike licence._

### aws-encryption-sdk

AWS Encryption SDK implementation for Python

`pip install aws-encryption-sdk` · installs (wheel) · licence: Apache Software License · rank 2171 · last release 2026-09-04 · [PyPI](https://pypi.org/project/aws-encryption-sdk/)

<details><summary>README extract</summary>

The AWS Encryption SDK for Python provides a fully compliant, native Python implementation of the AWS Encryption SDK.

The latest full documentation can be found at Read the Docs.

Find us on GitHub.

Security issue notifications

See Support Policy for details on the current support status of all major versions of this library.

Example:
```python
import aws_encryption_sdk
from aws_encryption_sdk.identifiers import CommitmentPolicy

client = aws_encryption_sdk.EncryptionSDKClient(
    commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT
)
```

...

</details>

### django-two-factor-auth

Complete Two-Factor Authentication for Django

`pip install django-two-factor-auth` · installs (wheel) · licence: MIT License · rank 2508 · last release 2025-09-27 · [PyPI](https://pypi.org/project/django-two-factor-auth/) · [docs](https://django-two-factor-auth.readthedocs.io/en/stable/)

<details><summary>README extract</summary>

Complete Two-Factor Authentication for Django. Built on top of the one-time
password framework django-otp and Django's built-in authentication framework
`django.contrib.auth` for providing the easiest integration into most Django
projects. ...

Sections: Django Two-Factor Authentication, Getting help, See Also

</details>

### cvss

CVSS2/3/4 library with interactive calculator for Python 2 and Python 3

`pip install cvss` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 2509 · last release 2025-08-04 · [PyPI](https://pypi.org/project/cvss/) · [source](https://github.com/RedHatProductSecurity/cvss)

_README extract left out: share-alike licence._

### securesystemslib

A library that provides cryptographic and general-purpose routines for Secure Systems Lab projects at NYU

`pip install securesystemslib` · installs (wheel) · licence: MIT · rank 2522 · last release 2026-10-20 · [PyPI](https://pypi.org/project/securesystemslib/) · [source](https://github.com/secure-systems-lab/securesystemslib)

<details><summary>README extract</summary>

Securesystemslib is a cryptography interface for signing and verifying digital
signatures. It is developed for the TUF and
in-toto projects: the key and signature containers are
compatible with metadata formats from those projects.

Under the hood, Securesystemslib can use various digital signing systems
(e.g. ...

Sections: securesystemslib, Usage, Contact, Legacy key migration

</details>

### tuf

A secure updater framework for Python

`pip install tuf` · installs (wheel) · licence: Apache-2.0 OR MIT · rank 2573 · last release 2026-09-02 · [PyPI](https://pypi.org/project/tuf/) · [docs](https://theupdateframework.readthedocs.io/en/stable/) · [source](https://github.com/theupdateframework/python-tuf)

<details><summary>README extract</summary>

The Update Framework (TUF) is a framework for
secure content delivery and updates. It protects against various types of
supply chain attacks and provides resilience to compromise. This repository is a
reference implementation written in Python. It is intended to conform to
version 1.0 of the TUF
specification. ...

</details>

### sigstore

A tool for signing Python package distributions

`pip install sigstore` · installs (wheel) · licence: Apache-2.0 · rank 2699 · last release 2026-10-20 · [PyPI](https://pypi.org/project/sigstore/) · [docs](https://sigstore.github.io/sigstore-python/) · [source](https://github.com/sigstore/sigstore-python)

<details><summary>README extract</summary>

<!--- @begin-badges@ --->

<!--- @end-badges@ --->

`sigstore` is a Python tool for generating and verifying Sigstore signatures.
You can use it to sign and verify Python package distributions, or anything
else! ...

Features:
* Support for keyless signature generation and verification with Sigstore
* Support for signing with "ambient" OpenID Connect identities
* A comprehensive CLI and corresponding
 importable Python API

Sections: sigstore-python, Index, Features, Usage, Signing, Signing with DSSE envelopes, Verifying, Identities, Signatures from GitHub Actions, Troubleshooting, Common issues, My problem is something else, Documentation, Licensing

</details>

### crowdstrike-falconpy

The CrowdStrike Falcon SDK for Python

`pip install crowdstrike-falconpy` · installs (wheel) · licence: The Unlicense (Unlicense) · rank 2931 · last release 2026-09-28 · [PyPI](https://pypi.org/project/crowdstrike-falconpy/) · [docs](https://www.falconpy.io) · [source](https://github.com/CrowdStrike/falconpy/tree/main/src/falconpy)

<details><summary>README extract</summary>

The FalconPy SDK contains a collection of Python classes that abstract CrowdStrike Falcon OAuth2 API interaction, removing duplicative code and allowing developers to focus on just the logic of their solution requirements.

+ Overview
+ Quick Start
+ Documentation and Support
+ Contribute to FalconPy

Features:
There are many CrowdStrike Falcon API service collections collectively containing hundreds of individual operations, all of which are accessible to your project via FalconPy. ...

Example:
```python
"""CrowdStrike FalconPy Quick Start."""
import os
from falconpy import Hosts

# Use the API Clients and Keys page within your Falcon console to generate credentials.
# You will need to assign the Hosts: READ scope to your client to run this example.

...

</details>

### cyclonedx-bom

CycloneDX Software Bill of Materials (SBOM) generator for Python projects and environments

`pip install cyclonedx-bom` · installs (wheel) · licence: Apache Software License · rank 3043 · last release 2026-11-04 · [PyPI](https://pypi.org/project/cyclonedx-bom/) · [docs](https://cyclonedx-bom-tool.readthedocs.io/) · [source](https://github.com/CycloneDX/cyclonedx-python/)

<details><summary>README extract</summary>

[![shield_pypi-version]][link_pypi]
[![shield_docker-version]][link_docker]
[![shield_rtfd]][link_rtfd]
[![shield_gh-workflow-test]][link_gh-workflow-test]
[![shield_coverage]][link_codacy]
[![shield_ossf-best-practices]][link_ossf-best-practices]
[![shield_license]][license_file]
[![shield_website]][link_website]
[![shield_slack]][link_slack]
[![s ...

Sections: CycloneDX Python SBOM Generation Tool, Requirements, Usage, Basic usage, Advanced usage and details, Internals

</details>

### ast-grep-py

Structural Search and Rewrite code at large scale using precise AST pattern.

`pip install ast-grep-py` · installs (wheel) · licence: MIT License · rank 3218 · last release 2026-11-02 · [PyPI](https://pypi.org/project/ast-grep-py/) · [docs](https://ast-grep.github.io/) · [source](https://github.com/ast-grep/ast-grep)

<details><summary>README extract</summary>

`ast-grep` is a tool for code structural search, lint, and rewriting.

This crate intends to build a native python binding of ast-grep and provide a python API for programmatic usage.

Sections: ast-grep python binding, ast-grep, Usage, Setup virtualenv, Activate venv, Build bindings, Run tests

</details>

### jwskate

A Pythonic implementation of the JOSE / JSON Web Crypto related RFCs (JWS, JWK, JWA, JWT, JWE)

`pip install jwskate` · installs (wheel) · licence: MIT · rank 3310 · last release 2025-04-02 · [PyPI](https://pypi.org/project/jwskate/) · [docs](https://guillp.github.io/jwskate/)

<details><summary>README extract</summary>

from jwskate import JweCompact

A Pythonic implementation of the JOSE set of IETF specifications: Json Web Signature, Keys,
Algorithms, Tokens and Encryption (RFC7515 to 7519), hence the name JWSKATE, and
their extensions ECDH Signatures (RFC8037), JWK Thumbprints (RFC7638), and
JWK Thumbprint URI (RFC9278), with respects to JWT Best Current ...

Features:
- Simple, Clean, Pythonic interface
- Convenience wrappers around `cryptography` for all algorithms described in JWA
- Json Web Keys (JWK) loading, dumping and generation
- Arbitrary data signature and verification using Json Web Keys ...

Example:
```python
from jwskate import Jwk

# Let's generate a random private key, to use with alg 'RS256'.
# Based on that alg, jwskate knows it must be an RSA key.
...

</details>

### requests-oauth2client

An OAuth2.x client based on `requests`.

`pip install requests-oauth2client` · installs (wheel) · licence: Apache-2.0 · rank 3334 · last release 2025-12-22 · [PyPI](https://pypi.org/project/requests-oauth2client/)

<details><summary>README extract</summary>

`requests_oauth2client` is an OAuth 2.x client for Python, able to obtain, refresh and revoke tokens from any
OAuth2.x/OIDC compliant Authorization Server. It sits upon and extends the famous requests HTTP client module. ...

Example:
```python
from requests_oauth2client import *
```

Sections: Documentation, Usage, Calling APIs with Access Tokens, Using an OAuth2Client, Obtaining tokens, Using OAuth2Client as a requests Auth Handler, Client Credentials grant, As Auth Handler, Exchanging code for tokens, Client-Initiated BackChannel Authentication (CIBA), Token Exchange, Client Secret Basic

</details>

### gssapi

Python GSSAPI Wrapper

`pip install gssapi` · installs from source (sdist only) · licence: ISC · rank 3777 · last release 2026-08-26 · [PyPI](https://pypi.org/project/gssapi/)

<details><summary>README extract</summary>

Python-GSSAPI provides both low-level and high level wrappers around the GSSAPI
C libraries. While it focuses on the Kerberos mechanism, it should also be
useable with other GSSAPI mechanisms.

Documentation can be found at

* A working implementation of GSSAPI (such as from MIT Kerberos)
 which supports delegation and includes header files ...

Sections: Python-GSSAPI, Requirements, Basic, Compiling from Scratch, For Running the Tests, Easy Way, From the Git Repo, Tests, Structure, Low-Level API, High-Level API, Extensions, Python Free-Threading (PEP 779), The Team

</details>

### ocspresponder

RFC 6960 compliant OCSP Responder framework written in Python 3.5+.

`pip install ocspresponder` · installs (wheel) · licence: Apache Software License · rank 4062 · last release 2016-05-02 · [PyPI](https://pypi.org/project/ocspresponder/)

<details><summary>README extract</summary>

RFC 6960 compliant OCSP Responder framework written in Python 3.5+.

It is based on the ocspbuilder and asn1crypto libraries. The HTTP
server is implemented using Bottle.

Current status: Alpha. Don't use for production yet.

Features:
Goals

- Simple: Don't overwhelm the user with a gazillion options.
- Flexible: Configurable using Python code.

Supported extensions

- Nonce (RFC 6960 Section 4.4.1)

Not (yet) implemented

- Multiple certificates per request / response

Example:
```python
from ocspresponder import OCSPResponder, CertificateStatus

def validate(serial: int) -> (CertificateStatus, Optional[datetime]):
    if certificate_is_valid(serial):
        return (CertificateStatus.good, None)
    elif certificate_is_expired(serial):
        expired_at = get_expiration_date(serial)
...

</details>

### crypto

Simple symmetric GPG file encryption and decryption

`pip install crypto` · installs (wheel) · licence: MIT License · rank 4300 · last release 2015-05-14 · [PyPI](https://pypi.org/project/crypto/)

<details><summary>README extract</summary>

Documentation:

Description

crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg) encryption and decryption for one or more files on Unix and Linux platforms. It runs on top of gpg and requires a gpg install on your system. Encryption is performed with the AES256 cipher algorithm. ...

</details>

### django-guardian

Per object permissions for Django

`pip install django-guardian` · installs (wheel) · licence: BSD License · rank 4326 · last release 2026-10-20 · [PyPI](https://pypi.org/project/django-guardian/) · [docs](https://django-guardian.readthedocs.io/) · [source](https://github.com/django-guardian/django-guardian)

<details><summary>README extract</summary>

`django-guardian` is an implementation of _per-object permissions on top
of Django’s authorization backend. Read an introduction to per-object permissions on djangoadvent articles.

Online documentation is available at

See real-world usage: Check out Who Uses Guardian to see how thousands of projects worldwide use django-guardian in production.

Example:
```python
>>> from django.contrib.auth.models import User, Group
>>> jack = User.objects.create_user('jack', 'jack@example.com', 'topsecretagentjack')
>>> admins = Group.objects.create(name='admins')
>>> jack.has_perm('change_group', admins)
False
>>> from guardian.shortcuts import assign_perm
>>> assign_perm('change_group', jack, obj=admins)
...
```

...

</details>

### fickling

A static analyzer and interpreter for Python pickle data

`pip install fickling` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 4658 · last release 2026-11-03 · [PyPI](https://pypi.org/project/fickling/) · [source](https://github.com/trailofbits/fickling)

_README extract left out: share-alike licence._

### stix2

Produce and consume STIX 2 JSON content

`pip install stix2` · installs (wheel) · licence: BSD License · rank 4683 · last release 2026-02-12 · [PyPI](https://pypi.org/project/stix2/) · [docs](https://stix2.readthedocs.io/) · [source](https://github.com/oasis-open/cti-python-stix2/)

<details><summary>README extract</summary>

This is an OASIS TC Open Repository.
See the Governance section for more information.

This repository provides Python APIs for serializing and de-serializing STIX2
JSON content, along with higher-level APIs for common tasks, including data
markings, versioning, and for resolving STIX IDs across multiple data sources. ...

Example:
```python
from stix2 import Indicator

indicator = Indicator(name="File hash for malware variant",
                      indicator_types=["malicious-activity"],
                      pattern_type="stix",
                      pattern="[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']")
```

Sections: cti-python-stix2, Usage, Governance, About OASIS TC Open Repositories, Feedback

</details>

### ROPGadget

This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation.

`pip install ROPGadget` · installs (wheel) · licence: BSD License · rank 4705 · last release 2025-10-15 · [PyPI](https://pypi.org/project/ROPGadget/)

<details><summary>README extract</summary>

ROPgadget supports ELF, PE, Mach-O, and Raw formats on x86, x64, ARM, ARM64, PowerPC, SPARC, MIPS, RISC-V 64, and RISC-V Compressed architectures.

</details>

### pwntools

Pwntools CTF framework and exploit development library.

`pip install pwntools` · installs (wheel) · licence: MIT License · rank 4733 · last release 2025-10-12 · [PyPI](https://pypi.org/project/pwntools/)

<details><summary>README extract</summary>

Pwntools is a CTF framework and exploit development library. Written in Python, it is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible.

Example:
```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

Sections: pwntools - CTF toolkit, Documentation

</details>

### polyfile-weave

A utility to recursively map the structure of a file.

`pip install polyfile-weave` · installs (wheel) · licence: Apache Software License · rank 4763 · last release 2026-01-22 · [PyPI](https://pypi.org/project/polyfile-weave/)

<details><summary>README extract</summary>

A utility to identify and map the semantic and syntactic structure of files,
including polyglots, chimeras, and schizophrenic files. It has a pure-Python implementation of libmagic and can act as a drop-in replacement for the `file` command. However, unlike `file`, PolyFile can recursively identify embedded files, like binwalk. ...

Example:
```python
from polyfile.magic import MagicMatcher

with open("file_to_test", "rb") as f:
    # the default instance automatically loads all file definitions
    for match in MagicMatcher.DEFAULT_INSTANCE.match(f.read()):
        for mimetype in match.mimetypes:
            print(f"Matched MIME: {mimetype}")
        print(f"Match string: {match!s}")
```

...

</details>

### sshpubkeys

SSH public key parser

`pip install sshpubkeys` · installs (wheel) · licence: BSD License · rank 5220 · last release 2021-02-04 · [PyPI](https://pypi.org/project/sshpubkeys/)

<details><summary>README extract</summary>

- Dropped support for Python 2.6 and 3.3
- Even in loose mode, DSA keys must be 1024, 2048, or 3072 bits (earlier this was looser)
- The interface (API) is exactly the same

Example:
```python
import sys
from sshpubkeys import SSHKey

ssh = SSHKey("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAYQCxO38tKAJXIs9ivPxt7AY"
      "dfybgtAR1ow3Qkb9GPQ6wkFHQqcFDe6faKCxH6iDRteo4D8L8B"
      "xwzN42uZSB0nfmjkIxFTcEU3mFSXEbWByg78aoddMrAAjatyrh"
      "H1pON6P0= ojarva@ojar-laptop", strict=True)
try:
    ssh.parse()
except InvalidKeyError as err:
...
```

Sections: OpenSSH Public Key Parser for Python, Major changes between versions 2 and 3, Usage, Options, Exceptions, Tests

</details>

### PyRIC

Python Wireless Library

`pip install PyRIC` · installs from source (sdist only) · licence: GNU General Public License v3 (GPLv3) · rank 5252 · last release 2016-12-04 · [PyPI](https://pypi.org/project/PyRIC/)

_README extract left out: share-alike licence._

### bashkit

A sandboxed bash interpreter for AI agents

`pip install bashkit` · installs (wheel) · licence: MIT License · rank 5455 · last release 2026-11-04 · [PyPI](https://pypi.org/project/bashkit/) · [source](https://github.com/everruns/bashkit)

<details><summary>README extract</summary>

Sandboxed bash interpreter for Python. Native bindings to the `bashkit` Rust core for fast, in-process execution with a virtual filesystem.

Homepage: bashkit.sh

Features:
- Sandboxed execution in-process, without containers or subprocess orchestration
- Full bash syntax: variables, pipelines, redirects, loops, functions, and arrays
- 164 built-in commands including `grep`, `sed`, `awk`, `jq`, `curl`, and `find` ...

Example:
```python
from bashkit import Bash

bash = Bash()

result = bash.execute_sync("echo 'Hello, World!'")
print(result.stdout)  # Hello, World!

bash.execute_sync("export APP_ENV=dev")
print(bash.execute_sync("echo $APP_ENV").stdout)  # dev
```

...

</details>

### pySigma

Sigma rule processing and conversion tools

`pip install pySigma` · installs (wheel) · licence: LGPL-2.1-only · rank 5676 · last release 2026-11-01 · [PyPI](https://pypi.org/project/pySigma/) · [source](https://github.com/SigmaHQ/pySigma)

_README extract left out: share-alike licence._

### authy

Authy API Client

`pip install authy` · installs from source (sdist only) · licence: MIT License · rank 5781 · last release 2020-04-15 · [PyPI](https://pypi.org/project/authy/)

<details><summary>README extract</summary>

Documentation for Python usage of the Authy API lives in the official Twilio documentation.

The Authy API supports multiple channels of 2FA:
* One-time passwords via SMS and voice.
* Soft token (TOTP via the Authy App)
* Push authentication via the Authy App ...

Example:
```python
from authy.api import AuthyApiClient
authy_api = AuthyApiClient('your_api_key')
```

Sections: Authy Quickstart, Usage, 2FA Workflow, Phone Verification, Copyright

</details>

### flake8-bandit

Automated security testing with bandit and flake8.

`pip install flake8-bandit` · installs (wheel) · licence: MIT License · rank 6137 · last release 2022-08-29 · [PyPI](https://pypi.org/project/flake8-bandit/)

<details><summary>README extract</summary>

Automated security testing built right into your workflow!

You already use flake8 to lint all your code for errors, ensure docstrings are formatted correctly, sort your imports correctly, and much more... ...

Sections: flake8-bandit, Configuration, How's it work?

</details>

### stem

Stem is a Python controller library that allows applications to interact with Tor (https://www.torproject.org/).

`pip install stem` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 (LGPLv3) · rank 6205 · last release 2023-06-06 · [PyPI](https://pypi.org/project/stem/)

_README extract left out: share-alike licence._

### cisco-ai-skill-scanner

Security scanner for Agent Skills packages - Detects prompt injection, data exfiltration, and malicious code

`pip install cisco-ai-skill-scanner` · installs (wheel) · licence: Apache Software License · rank 6210 · last release 2026-10-26 · [PyPI](https://pypi.org/project/cisco-ai-skill-scanner/) · [docs](https://github.com/cisco-ai-defense/skill-scanner#readme) · [source](https://github.com/cisco-ai-defense/skill-scanner)

<details><summary>README extract</summary>

A best-effort security scanner for AI Agent Skills that detects prompt injection, data exfiltration, and malicious code patterns. It combines pattern-based detection (YAML + YARA-X), AST and dataflow analysis, an optional LLM-as-a-judge, and a bounded CEL decision layer over typed detector facts. ...

Features:
- Multi-Engine Detection - Static analysis, behavioral dataflow, LLM semantic analysis, and cloud-based scanning for layered, best-effort coverage ...

Example:
```python
from skill_scanner import SkillScanner
from skill_scanner.core.analyzers import BehavioralAnalyzer

# Create scanner with analyzers
scanner = SkillScanner(analyzers=[
    BehavioralAnalyzer(),
])

# Scan a skill
result = scanner.scan_skill("/path/to/skill")

print(f"Findings: {len(result.findings)}")
...

</details>

### licensecheck

Output the licenses used by dependencies and check if these are compatible with the project license

`pip install licensecheck` · installs (wheel) · licence: MIT · rank 6369 · last release 2026-06-18 · [PyPI](https://pypi.org/project/licensecheck/) · [docs](https://github.com/FHPythonUtils/LicenseCheck/blob/master/README.md) · [source](https://github.com/FHPythonUtils/LicenseCheck)

<details><summary>README extract</summary>

Sections: Examples from the command-line, Using pyproject.toml (default if not piping input), Use csv format, Groups, Help, Configuration Example, Example 1: pyproject.toml, Documentation, Language information, Working with the repo

</details>

### pysodium

python libsodium wrapper

`pip install pysodium` · installs from source (sdist only) · licence: BSD License · rank 6572 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pysodium/)

<details><summary>README extract</summary>

This is a very simple wrapper around libsodium masquerading as nacl.

This wrapper requires a pre-installed libsodium from:

then it provides access to the following functions:

Constants:

Note ...

Example:
```python
crypto_aead_aegis128l_decrypt(ciphertext, ad, nonce, key)
crypto_aead_aegis128l_encrypt(message, ad, nonce, key)
crypto_aead_aegis128l_decrypt_detached(ciphertext, mac, ad, nonce, key)
crypto_aead_aegis128l_encrypt_detached(message, ad, nonce, key)
crypto_aead_aegis256_decrypt(ciphertext, ad, nonce, key)
...
```

</details>

### pyarmor

A tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

`pip install pyarmor` · installs (wheel) · licence: Free To Use But Restricted · rank 6577 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pyarmor/)

<details><summary>README extract</summary>

Pyarmor is a command line tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

Features:
* The obfuscated script is still a normal `.py` script, in most of cases the original python scripts can be replaced with obfuscated scripts seamlessly. ...

Example:
```python
from pyarmor_runtime import pyarmor
pyarmor(name, file, b'\x28\x83\x20\x58....')
```

Sections: Protect Python Scripts By Pyarmor, Key Features, Quick Start, More Resources

</details>

### aikido-zen

Aikido Zen for Python

`pip install aikido-zen` · installs (wheel) · licence: GNU Affero General Public License v3 or later (AGPLv3+) · rank 6800 · last release 2026-10-15 · [PyPI](https://pypi.org/project/aikido-zen/) · [source](https://github.com/AikidoSec/firewall-python)

_README extract left out: share-alike licence._

### pyarmor.cli.core

Provide extension module pytransform3 for Pyarmor

`pip install pyarmor.cli.core` · installs (wheel) · licence: Free To Use But Restricted · rank 6983 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pyarmor.cli.core/)

<details><summary>README extract</summary>

Pyarmor is a command line tool used to obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts.

This package provides prebuilt extension module `pytransform3` and `pyarmor_runtime` required by Pyarmor

It includes prebuilt extensions support the following platforms for Python 3.7+: ...

</details>

### pycti

Python API client for OpenCTI.

`pip install pycti` · installs (wheel) · licence: Apache Software License · rank 6995 · last release 2026-11-06 · [PyPI](https://pypi.org/project/pycti/)

<details><summary>README extract</summary>

The official OpenCTI Python client helps developers to use the OpenCTI API by providing easy to use methods and utils.
This client is also used by some OpenCTI components.

Sections: OpenCTI client for Python, Documentation, Client usage, API reference, Tests, Launch tests, Prerequisite, Launching, About

</details>

### stackone-defender

Indirect prompt injection defense for AI agents using tool calls

`pip install stackone-defender` · installs (wheel) · licence: Apache-2.0 · rank 7131 · last release 2026-10-21 · [PyPI](https://pypi.org/project/stackone-defender/) · [source](https://github.com/StackOneHQ/defender-py)

<details><summary>README extract</summary>

Indirect prompt injection defense for AI agents using tool calls (MCP, CLI, or direct APIs). Detects and gates prompt injection attacks hidden in tool results (emails, documents, PRs, etc.) before they reach your LLM.

Python package: `stackone-defender` — aligned with `@stackone/defender` on npm.

Example:
```python
from stackone_defender import create_prompt_defense

# Tier 1 + Tier 2 are on by default. block_high_risk=True enables allow/block.
defense = create_prompt_defense(block_high_risk=True)

# Optional: preload ONNX to avoid first-call latency (requires [onnx] extra)
defense.warmup_tier2()

...
```

...

</details>

### jose

An implementation of the JOSE draft

`pip install jose` · installs from source (sdist only) · licence: BSD License · rank 7499 · last release 2015-11-13 · [PyPI](https://pypi.org/project/jose/)

<details><summary>README extract</summary>

JOSE is a framework intended to provide a method to securely transfer
claims (such as authorization information) between parties. The JOSE framework
provides a collection of specifications to serve this purpose. A JSON Web
Token (JWT) contains claims that can be used to allow a system to apply access
control to resources it owns. ...

Sections: JOSE, Documentation, Builds, CHANGES, 1.0.0 (2015-10-06), 0.3.0 (2015-04-10), 0.2.2 (2015-01-07), 0.2.1 (2014-11-24), 0.1 (2014-04-16)

</details>

### secops

Python SDK for wrapping the Google SecOps API for common use cases

`pip install secops` · installs (wheel) · licence: Apache-2.0 · rank 7532 · last release 2026-05-22 · [PyPI](https://pypi.org/project/secops/) · [docs](https://github.com/google/secops-wrapper#readme) · [source](https://github.com/google/secops-wrapper.git)

<details><summary>README extract</summary>

A Python SDK for interacting with Google Security Operations products, currently supporting Chronicle/SecOps SIEM.
This wraps the API for common use cases, including UDM searches, entity lookups, IoCs, alert management, case management, and detection rule management.

Follow these steps to ensure your environment is properly configured:

1. ...

Example:
```python
# Step 1: List and retrieve an OKTA parser
parsers = chronicle.list_parsers(log_type="OKTA")
parser_id = parsers0.split("/")[-1]
parser_details = chronicle.get_parser(log_type="OKTA", id=parser_id)

# Extract and decode parser code
import base64
parser_code = base64.b64decode(parser_details["cbn"]).decode('utf-8')

...
```

...

</details>

### fhconfparser

Provides a config language independent way to read a config file.

`pip install fhconfparser` · installs (wheel) · licence: MIT License · rank 7563 · last release 2024-01-24 · [PyPI](https://pypi.org/project/fhconfparser/) · [docs](https://github.com/FHPythonUtils/FHConfParser/blob/master/README.md) · [source](https://github.com/FHPythonUtils/FHConfParser)

<details><summary>README extract</summary>

Provides a config language independent way to read a config file.

For instance toml and ini syntax is very similar but not identical. Currently, tools such as
pylint must implement custom ways to deal with this. Hopefully this code
streamlines that a bit.

Sections: FHConfParser, Rationale for project, Documentation, Language information, Built for, Chocolatey, Windows - Python.org, Apt, Dnf, Homebrew, MacOS - Python.org, How to run, Windows, Linux/ MacOS

</details>

### cerbos

SDK for working with Cerbos: an open core, language-agnostic, scalable authorization solution

`pip install cerbos` · installs (wheel) · licence: Apache-2.0 · rank 7590 · last release 2026-10-12 · [PyPI](https://pypi.org/project/cerbos/)

<details><summary>README extract</summary>

Python clients for accessing Cerbos.

Cerbos is the open core, language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

Example:
```python
from cerbos.sdk.grpc.client import CerbosClient
from cerbos.engine.v1 import engine_pb2
from cerbos.request.v1 import request_pb2
from google.protobuf.struct_pb2 import Value

principal = engine_pb2.Principal(
    id="john",
    roles={"employee"},
    policy_version="20210210",
    attr={
        "department": Value(string_value="marketing"),
...
```

Sections: Cerbos Python SDK, Usage, gRPC Client, HTTP client, Cerbos Hub, Get help

</details>

### keeper-secrets-manager-core

Keeper Secrets Manager for Python 3

`pip install keeper-secrets-manager-core` · installs (wheel) · licence: MIT License · rank 7649 · last release 2026-06-15 · [PyPI](https://pypi.org/project/keeper-secrets-manager-core/) · [docs](https://github.com/Keeper-Security/secrets-manager) · [source](https://github.com/Keeper-Security/secrets-manager)

<details><summary>README extract</summary>

For more information, see our official documentation page

Python Requirements: Python 3.9 or higher

For deployments where the server public key is not shipped with the SDK,
a caller-supplied EC P-256 public key can be supplied via any of three
paths (precedence is programmatic > one-time token > pre-existing config): ...

Example:
```python
from keeper_secrets_manager_core import SecretsManager
from keeper_secrets_manager_core.storage import FileKeyValueStorage

# Programmatic — wins over the other two if all are present
sm = SecretsManager(
    token='REGION:ONE_TIME_TOKEN',
    server_public_key='url-safe-base64-EC-P256-public-key',
    server_public_key_id='your-key-id',
...
```

...

</details>

### pyClamd

pyClamd is a python interface to Clamd (Clamav daemon).

`pip install pyClamd` · installs from source (sdist only) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 7685 · last release 2017-08-27 · [PyPI](https://pypi.org/project/pyClamd/)

_README extract left out: share-alike licence._

### git-dumper

A tool to dump a git repository from a website

`pip install git-dumper` · installs (wheel) · licence: MIT License · rank 7892 · last release 2026-02-28 · [PyPI](https://pypi.org/project/git-dumper/)

<details><summary>README extract</summary>

A tool to dump a git repository from a website.

Sections: git-dumper, Usage, Example, Disclaimer, Build from source, How does it work?

</details>

### libsast

A generic SAST library built on top of semgrep and regex

`pip install libsast` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 7913 · last release 2026-10-27 · [PyPI](https://pypi.org/project/libsast/) · [docs](https://github.com/ajinabraham/libsast/blob/master/README.md) · [source](https://github.com/ajinabraham/libsast)

_README extract left out: share-alike licence._

### abi3info

A library for abi3 and other CPython API information

`pip install abi3info` · installs (wheel) · licence: MIT · rank 7955 · last release 2026-09-25 · [PyPI](https://pypi.org/project/abi3info/) · [docs](https://woodruffw.github.io/abi3info/) · [source](https://github.com/woodruffw/abi3info)

<details><summary>README extract</summary>

abi3info exposes information about CPython's "limited API" (including the
stable ABI, called `abi3`) as a Python library.

Example:
```python
import abi3info

abi3info.FEATURE_MACROS
abi3info.MACROS
abi3info.STRUCTS
abi3info.TYPEDEFS
abi3info.FUNCTIONS
abi3info.DATAS
```

Sections: abi3info, Usage, Examples, Licensing

</details>

### requests-hardened

A library that overrides the default behaviors of the requests library, and adds new security features.

`pip install requests-hardened` · installs (wheel) · licence: BSD-3-Clause · rank 8009 · last release 2026-07-14 · [PyPI](https://pypi.org/project/requests-hardened/) · [source](https://github.com/saleor/requests-hardened/)

<details><summary>README extract</summary>

`requests-hardened` is a library that overrides the default behaviors of the `requests`
library, and adds new security features.

Features:
- SSRF Filters: blocks private and loopback IP ranges.
- HTTP Redirects: can be used safely alongside the SSRF filter feature.
- Proxy Support: proxies can be used in combination with SSRF Filters for a defense in depth. ...

Example:
```python
from requests_hardened import Config, Manager

# Creates a global "manager" that can be used to create `requests.Session`
# objects with hardening in place.
http_manager = Manager(
    Config(
        default_timeout=(2, 10),
        never_redirect=False,
        ip_filter_enable=True,
        ip_filter_allow_loopback_ips=False,
...
```

...

</details>

### captcha

A captcha library that generates audio and image CAPTCHAs.

`pip install captcha` · installs (wheel) · licence: BSD License · rank 8032 · last release 2025-03-01 · [PyPI](https://pypi.org/project/captcha/) · [docs](https://captcha.lepture.com/) · [source](https://github.com/lepture/captcha)

<details><summary>README extract</summary>

A captcha library that generates audio and image CAPTCHAs.

Features:
1. Audio CAPTCHAs
2. Image CAPTCHAs

Example:
```python
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

audio = AudioCaptcha(voicedir='/path/to/voices')
image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

data = audio.generate('1234')
audio.write('1234', 'out.wav')

data = image.generate('1234')
image.write('1234', 'out.png')
```

Sections: Captcha, Features, Usage, Useful Links

</details>

### pygitguardian

Python Wrapper for GitGuardian's API -- Scan security policy breaks everywhere

`pip install pygitguardian` · installs (wheel) · licence: MIT License · rank 8218 · last release 2026-10-29 · [PyPI](https://pypi.org/project/pygitguardian/)

<details><summary>README extract</summary>

API client library for the GitGuardian API.

The GitGuardian API puts at your fingertips the power to detect more than 200 types of secrets in any text content, as well as other potential security vulnerabilities. ...

Example:
```python
# please don't hardcode your gg_api_key in source code :)
API_KEY = os.getenv("GITGUARDIAN_API_KEY")
DOCUMENT = """
    import urllib.request
    url = '
    response = urllib.request.urlopen(url)
    consume(response.read())"
"""

client = GGClient(api_key=API_KEY)

# Check the health of the API and the API key used.
...
```

Sections: py-gitguardian - GitGuardian API Client, Requirements, Projects using `py-gitguardian`, Getting started, Examples, Scanning text content, Scanning multiple files, Transform results to dict or JSON, Dependencies

</details>

### dncil

The FLARE team's open-source library to disassemble Common Intermediate Language (CIL) instructions.

`pip install dncil` · installs (wheel) · licence: Apache Software License · rank 8282 · last release 2022-12-12 · [PyPI](https://pypi.org/project/dncil/)

<details><summary>README extract</summary>

`dncil` is a Common Intermediate Language (`CIL`) disassembly library written in Python that supports parsing the header, instructions, and exception handlers of `.NET` managed methods. Parsed data is exposed through an object-oriented API to help you quickly develop `CIL` analysis tools using `dncil`. ...

Example:
```python
>  main_method_body.flags
SmallFormat  :  false
TinyFormat   :  false
FatFormat    :  false
TinyFormat1  :  true
MoreSects    :  false
InitLocals   :  false
CompressedIL :  false
>  main_method_body.size
14
>  hexdump.hexdump(main_method_body.get_bytes())
00000000: 36 00 72 01 00 00 70 28  04 00 00 0A 00 2A        6.r...p(.....*
...
```

Sections: Example, Linting

</details>

### ggshield

Detect secrets from all sources using GitGuardian's brains

`pip install ggshield` · installs (wheel) · licence: MIT License · rank 8463 · last release 2026-10-26 · [PyPI](https://pypi.org/project/ggshield/)

<details><summary>README extract</summary>

> [!IMPORTANT]
> macOS: upgrading to 1.54.0 triggers a Keychain prompt for `ggshield-py`, a second binary that now reads your saved token as part of our performance improvements. Click Always Allow; it won't ask again. ...

Sections: ggshield: protect your code with GitGuardian, macOS, Homebrew, Standalone .pkg package, Linux, Deb and RPM packages, Windows, Chocolatey, Standalone .zip archive, All operating systems, Using pipx, Using pip, Initial setup, Using `ggshield auth login`

</details>

### ansible-pylibssh

Python bindings for libssh client specific to Ansible use case

`pip install ansible-pylibssh` · installs (wheel) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 8544 · last release 2026-03-16 · [PyPI](https://pypi.org/project/ansible-pylibssh/) · [source](https://github.com/ansible/pylibssh)

_README extract left out: share-alike licence._

### abi3audit

Scans Python wheels for abi3 violations and inconsistencies

`pip install abi3audit` · installs (wheel) · licence: MIT · rank 8698 · last release 2026-01-23 · [PyPI](https://pypi.org/project/abi3audit/) · [source](https://github.com/pypa/abi3audit)

<details><summary>README extract</summary>

<!--- @begin-badges@ --->

<!--- @end-badges@ --->

*Read the Trail of Bits blog post about how we find bugs with `abi3audit`!*

`abi3audit` scans Python extensions for `abi3` violations and inconsistencies.

It can scan individual (unpackaged) shared objects, packaged wheels, or entire
package version histories. ...

Sections: abi3audit, Index, Motivation, Usage, Examples, Limitations, Licensing

</details>

### flawfinder

a program that examines source code looking for security weaknesses

`pip install flawfinder` · installs (wheel) · licence: GNU General Public License v2 or later (GPLv2+) · rank 8726 · last release 2026-05-17 · [PyPI](https://pypi.org/project/flawfinder/)

_README extract left out: share-alike licence._

### pyAesCrypt

Encrypt and decrypt files and streams in AES Crypt format (version 2)

`pip install pyAesCrypt` · installs (wheel) · licence: Apache Software License · rank 8858 · last release 2023-11-11 · [PyPI](https://pypi.org/project/pyAesCrypt/)

<details><summary>README extract</summary>

pyAesCrypt is a Python 3 file-encryption module and script that uses AES256-CBC to encrypt/decrypt files and binary streams.

pyAesCrypt is compatible with the AES Crypt file format (version 2).

It is Free Software, released under the Apache License, Version 2.0.

pyAesCrypt is brought to you by Marco Bellaccini - marco.bellaccini(at!)gmail.com. ...

Example:
```python
import pyAesCrypt
password = "please-use-a-long-and-random-password"
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password)
```

Sections: pyAesCrypt, About pyAesCrypt, Module usage example, Script usage examples, FAQs

</details>

### PGPy13

Pretty Good Privacy for Python (temporary fork for py3.13 compatability)

`pip install PGPy13` · installs (wheel) · licence: BSD License · rank 9009 · last release 2025-03-01 · [PyPI](https://pypi.org/project/PGPy13/) · [docs](https://pgpy.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

`PGPy` is a Python library for implementing Pretty Good Privacy into Python programs, conforming to the OpenPGP specification per RFC 4880.

`PGPy13` is a (hopefully) temporary fork of the main PGPy project with
one and only two patches installed:

1. ...

Features:
Currently, PGPy can load keys and signatures of all kinds in both ASCII armored and binary formats.

It can create and verify RSA, DSA, and ECDSA signatures, at the moment. It can also encrypt and decrypt messages using RSA and ECDH.

Sections: PGPy: Pretty Good Privacy for Python, Disclaimer, Features, Documentation, Discussion, Requirements

</details>

### plugin-scanner

Lint, verify, and gate plugin ecosystems for maintainers, CI, and publish workflows.

`pip install plugin-scanner` · installs (wheel) · licence: Apache-2.0 · rank 9012 · last release 2026-11-05 · [PyPI](https://pypi.org/project/plugin-scanner/) · [docs](https://github.com/hashgraph-online/hol-guard/tree/main/docs/guard) · [source](https://github.com/hashgraph-online/hol-guard)

<details><summary>README extract</summary>

| | Stop risky AI actions before they compromise your machine. HOL Guard is a local-first security layer for AI agents, tools, plugins, skills, MCP servers, and package installs.

Install HOL Guard
Read the documentation
PyPI Package (`hol-guard`)
Report an Issue | ...

Features:
AI agents can run commands, install dependencies, read files, and call external tools within one session. HOL Guard reviews those actions at supported execution points and keeps the policy decision, approval request, and receipt together. ...

...

</details>

### libmagic

libmagic bindings

`pip install libmagic` · installs from source (sdist only) · licence: GNU General Public License (GPL) · rank 9113 · last release 2012-03-02 · [PyPI](https://pypi.org/project/libmagic/)

_README extract left out: share-alike licence._

### pykeepass

Python library to interact with keepass databases (supports KDBX3 and KDBX4)

`pip install pykeepass` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 9295 · last release 2026-08-09 · [PyPI](https://pypi.org/project/pykeepass/) · [source](https://github.com/libkeepass/pykeepass)

_README extract left out: share-alike licence._

### leakguard

leakguard — fast secret scanner for your codebase

`pip install leakguard` · installs (wheel) · licence: MIT License · rank 9419 · last release 2026-03-10 · [PyPI](https://pypi.org/project/leakguard/) · [source](https://github.com/adrian-lorenz/leakguard)

<details><summary>README extract</summary>

> Fast, lightweight secret scanner for codebases (Rust CLI + Python package).

`leakguard` scans source files for accidentally committed credentials, tokens, and sensitive config values.

Features:
- 104 built-in rules across cloud, LLM, database, HTTP auth, observability, and SaaS ecosystems
- Fast local scanning with sensible defaults
- CI-friendly outputs: `pretty`, `json`, `sarif`, `markdown` ...

Example:
```python
from leakguard import scan_text, scan_text_dict, replace_text

findings = scan_text("My API key is sk-proj-abc123xyz...")
for f in findings:
    print(f.rule_id, f.severity, f.secret, f.secret_hash)

# Disable specific rules for this call
findings = scan_text("...", disable_rules=["http-insecure-url"])

# Optional replacer for secret output
...
```

...

</details>

### taxii2-client

TAXII 2 Client Library

`pip install taxii2-client` · installs (wheel) · licence: BSD License · rank 9449 · last release 2021-03-12 · [PyPI](https://pypi.org/project/taxii2-client/) · [docs](https://taxii2client.readthedocs.io/) · [source](https://github.com/oasis-open/cti-taxii-client/)

<details><summary>README extract</summary>

NOTE: This is an OASIS TC Open Repository. See the
Governance section for more information.

cti-taxii-client is a minimal client implementation for the TAXII 2.X server.
It supports the following TAXII 2.X API services:

- Server Discovery
- Get API Root Information
- Get Status
- Get Collections
- Get a Collection
- Get Objects
- Add Objects ...

Example:
```python
from taxii2client.v21 import Server
server = Server(' user='user_id', password='user_password')
```

Sections: cti-taxii-client, Usage, Governance, About OASIS TC Open Repositories, Feedback

</details>

### akeyless-cloud-id

AKEYLESS Cloud ID Retriever

`pip install akeyless-cloud-id` · installs (wheel) · licence: Apache Software License · rank 9463 · last release 2026-09-20 · [PyPI](https://pypi.org/project/akeyless-cloud-id/)

<details><summary>README extract</summary>

Akeyless Python Cloud Id

Retrieves cloud identity

Currently, AWS, GCP, Azure and Alibaba Cloud are supported.
In order to get cloud identity you should import this package and call the relevant method per your chosen CSP: ...

Sections: #, Minimum requirements, Optional Dependencies

</details>

### sslyze

Fast and powerful SSL/TLS scanning library.

`pip install sslyze` · installs from source (sdist only) · licence: GNU Affero General Public License v3 · rank 9741 · last release 2026-03-29 · [PyPI](https://pypi.org/project/sslyze/) · [docs](https://nabla-c0d3.github.io/sslyze/documentation) · [source](https://github.com/nabla-c0d3/sslyze)

_README extract left out: share-alike licence._

### bitwarden-sdk

A Bitwarden Client for python

`pip install bitwarden-sdk` · installs (wheel) · licence: Other/Proprietary License · rank 9755 · last release 2026-05-21 · [PyPI](https://pypi.org/project/bitwarden-sdk/)

<details><summary>README extract</summary>

- Python 3
- Rust
- `maturin` (install with `pip install maturin`, or `pip install maturin[patchelf]` on Linux)
- `npm`
- `uv` (recommended; used in test automation)

You will need to build and run the script using a virtual environment. This will be slightly
different depending on the OS you are using:

Example:
```python
from bitwarden_sdk import BitwardenClient
```

Sections: Build locally, Requirements, Build, Run, Use without building locally

</details>

### doppler-sdk

(no summary)

`pip install doppler-sdk` · installs (wheel) · licence: Apache Software License · rank 9758 · last release 2024-04-08 · [PyPI](https://pypi.org/project/doppler-sdk/) · [docs](https://docs.doppler.com/docs/sdk-python) · [source](https://github.com/DopplerHQ/python-sdk)

<details><summary>README extract</summary>

Doppler's SDK provides convenient access to the Doppler API from applications written in Python.

Sections: doppler-sdk, Usage, Reference Docs

</details>

### SLH-DSA

Pure Python implementation of the SLH-DSA algorithm (based on FIPS 205).

`pip install SLH-DSA` · installs (wheel) · licence: GNU Lesser General Public License v3 or later (LGPLv3+) · rank 9812 · last release 2026-08-17 · [PyPI](https://pypi.org/project/SLH-DSA/)

_README extract left out: share-alike licence._

### python-evtx

Pure Python parser for Windows event log files (.evtx).

`pip install python-evtx` · installs (wheel) · licence: Apache-2.0 · rank 9847 · last release 2025-05-02 · [PyPI](https://pypi.org/project/python-evtx/) · [source](https://github.com/williballenthin/python-evtx)

<details><summary>README extract</summary>

Introduction

python-evtx is a pure Python parser for recent Windows Event Log files (those with the file extension ".evtx"). The module provides programmatic access to the File and Chunk headers, record templates, and event entries. For example, you can use python-evtx to review the event logs of Windows 7 systems from a Mac or Linux workstation. ...

</details>

### whodap

Simple RDAP Utility for Python that looks like WHOIS

`pip install whodap` · installs (wheel) · licence: MIT · rank 9985 · last release 2026-10-01 · [PyPI](https://pypi.org/project/whodap/)

<details><summary>README extract</summary>

`whodap` | Simple RDAP Utility for Python

- Support for asyncio HTTP requests (`httpx2`)
- Leverages the `SimpleNamespace` type for cleaner RDAP Response traversal
- Keeps the familiar look of WHOIS via the `to_whois_dict` method for DNS lookups

Example:
```python
import asyncio
from pprint import pprint

import whodap

# Looking up a domain name
response = whodap.lookup_domain(domain='bitcoin', tld='org')
# Equivalent asyncio call
loop = asyncio.get_event_loop()
response = loop.run_until_complete(whodap.aio_lookup_domain(domain='bitcoin', tld='org'))
...
```

Sections: whodap, Quickstart, Exported Functions and Classes, Common Usage Patterns, Roadmap, RDAP Resources

</details>

### nassl

Experimental OpenSSL wrapper for Python 3.11+ and SSLyze.

`pip install nassl` · installs (wheel) · licence: GNU Affero General Public License v3 · rank 10009 · last release 2026-10-31 · [PyPI](https://pypi.org/project/nassl/)

_README extract left out: share-alike licence._

### fastapi-cloudauth

fastapi-cloudauth supports simple integration between FastAPI and cloud authentication services (AWS Cognito, Auth0, Firebase Authentication).

`pip install fastapi-cloudauth` · installs (wheel) · licence: MIT License · rank 10067 · last release 2022-01-06 · [PyPI](https://pypi.org/project/fastapi-cloudauth/) · [source](https://github.com/tokusumi/fastapi-cloudauth)

<details><summary>README extract</summary>

fastapi-cloudauth standardizes and simplifies the integration between FastAPI and cloud authentication services (AWS Cognito, Auth0, Firebase Authentication).

Features:
* [X] Verify access/id token: standard JWT validation (signature, expiration), token audience claims, etc.
* [X] Verify permissions based on scope (or groups) within access token and extract user info
* [X] Get the detail of login user info (name, ...

Example:
```python
import os
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from fastapi_cloudauth.cognito import Cognito, CognitoCurrentUser, CognitoClaims

app = FastAPI()
auth = Cognito(
    region=os.environ["REGION"],
    userPoolId=os.environ["USERPOOLID"],
    client_id=os.environ["APPCLIENTID"]
)

...
```

...

</details>

### srp-ext

Secure Remote Password

`pip install srp-ext` · installs from source (sdist only) · licence: BSD License · rank 10184 · last release 2017-07-17 · [PyPI](https://pypi.org/project/srp-ext/)

<details><summary>README extract</summary>

This package provides an implementation of the Secure Remote Password
protocol (SRP). SRP is a cryptographically strong authentication
protocol for password-based, mutual authentication over an insecure
network connection. ...

</details>

### dynamodb-encryption-sdk

DynamoDB Encryption Client for Python

`pip install dynamodb-encryption-sdk` · installs (wheel) · licence: Apache Software License · rank 10379 · last release 2024-08-07 · [PyPI](https://pypi.org/project/dynamodb-encryption-sdk/)

<details><summary>README extract</summary>

The Amazon DynamoDB Encryption Client for Python provides client-side encryption of Amazon
DynamoDB items to help you to protect your table data before you send it to DynamoDB. It
provides an implementation of the Amazon DynamoDB Encryption Client that is fully compatible
with the Amazon DynamoDB Encryption Client for Java. ...

Example:
```python
>>> from dynamodb_encryption_sdk.encrypted.item import decrypt_python_item, encrypt_python_item
>>> plaintext_item = {
...     'some': 'data',
...     'more': 5
... }
>>> encrypted_item = encrypt_python_item(
...     item=plaintext_item,
...     crypto_config=my_crypto_config
... )
>>> decrypted_item = decrypt_python_item(
...
```

...

</details>

### otpauth

Implements one time password of HOTP/TOTP

`pip install otpauth` · installs (wheel) · licence: BSD License · rank 10436 · last release 2026-08-22 · [PyPI](https://pypi.org/project/otpauth/) · [docs](https://otp.authlib.org/) · [source](https://github.com/authlib/otpauth)

<details><summary>README extract</summary>

One time password implementations in Python. HOTP and TOTP.

Documentation:
GitHub:

Example:
```python
import otpauth

totp = otpauth.HOTP(b"user-secret")

# generate a code for now
code: int = totp.generate()

# you may want to convert it to string
str_code: str = totp.string_code(code)

# verify the code
totp.verify(code)  # => True
totp.verify(str_code)  # => True
```

Sections: OTP Auth, Usage

</details>

### uefi-firmware

Various data structures and parsing tools for UEFI firmware.

`pip install uefi-firmware` · installs (wheel) · licence: BSD-3-Clause · rank 10441 · last release 2026-06-04 · [PyPI](https://pypi.org/project/uefi-firmware/)

<details><summary>README extract</summary>

The UEFI firmware parser is a simple module and set of scripts for parsing, extracting,
and recreating UEFI firmware volumes.
This includes parsing modules for BIOS, OptionROM, Intel ME and other formats too.
Please use the example scripts for parsing tutorials.

Example:
```python
import uefi_firmware
with open('/path/to/firmware.rom', 'r') as fh:
  file_content = fh.read()
parser = uefi_firmware.AutoParser(file_content)
if parser.type() != 'unknown':
  firmware = parser.parse()
  firmware.showinfo()
```

Sections: UEFI Firmware Parser, Usage, Scripts

</details>

### aiohttp-swagger

Swagger API Documentation builder for aiohttp server

`pip install aiohttp-swagger` · installs (wheel) · licence: BSD License · rank 10517 · last release 2021-10-22 · [PyPI](https://pypi.org/project/aiohttp-swagger/)

<details><summary>README extract</summary>

LOOCKING FOR MAINTAINERS!!!!!

*aiohttp-swagger: Swagger API Documentation builder for aiohttp server*

Documentation |

Code |
Issues |
Python version | Python 3.4 and above

What's aiohttp-swagger

aiohttp-swagger is a plugin for aiohttp.web server that allow to document APIs using Swagger show the Swagger-ui console.

What's new? ...

Sections: aiohttp-swagger, Version 1.0.0

</details>

### zaproxy

ZAP API Client

`pip install zaproxy` · installs (wheel) · licence: Apache Software License · rank 10545 · last release 2026-06-12 · [PyPI](https://pypi.org/project/zaproxy/) · [docs](https://www.zaproxy.org/docs/api/) · [source](https://github.com/zaproxy/zap-api-python.git)

<details><summary>README extract</summary>

The Python implementation to access the ZAP API. For more information
about ZAP consult the (main) ZAP project.

The latest released version can be downloaded from the using:

 pip install zaproxy ...

Sections: ZAP Python API, How to Obtain, Getting Help, Issues

</details>

### plyara

Parse YARA rules

`pip install plyara` · installs (wheel) · licence: Apache Software License · rank 10584 · last release 2025-02-06 · [PyPI](https://pypi.org/project/plyara/)

<details><summary>README extract</summary>

Parse YARA rules into a dictionary representation.

Plyara is a script and library that lexes and parses a file consisting of one more YARA rules into a python dictionary representation. ...

Example:
```python
>>> import plyara
>>> parser = plyara.Plyara()
>>> mylist = parser.parse_string('rule MyRule { strings: $a="1" \n condition: false }')
>>>
>>> import pprint
>>> pprint.pprint(mylist)
[{'condition_terms': ['false'],
  'raw_condition': 'condition: false ',
  'raw_strings': 'strings: $a="1" \n ',
  'rule_name': 'MyRule',
  'start_line': 1,
...
```

Sections: plyara, Usage, Additional Information, Reusing The Parser, Breaking Change: Import Effects, Background, New Parameter: Import Effects, Note, Breaking Change: Logic Hash Versions, Pre-Processing, Cloning, Unit Tests, Coverage

</details>

### depgather

Get a list of deps given a pyproject.toml, uv.lock, requirements.txt etc

`pip install depgather` · installs (wheel) · licence: MIT · rank 10849 · last release 2026-06-17 · [PyPI](https://pypi.org/project/depgather/) · [docs](https://github.com/FHPythonUtils/DepGather/blob/master/README.md) · [source](https://github.com/FHPythonUtils/DepGather)

<details><summary>README extract</summary>

Get a list of deps given a pyproject.toml, uv.lock, requirements.txt etc

Sections: DepGather, Documentation, Language information, Working with the repo

</details>

### hol-guard

Open-source antivirus and runtime protection for AI agents, tools, MCP servers, plugins, skills, and package installs.

`pip install hol-guard` · installs (wheel) · licence: Apache-2.0 · rank 10966 · last release 2026-11-04 · [PyPI](https://pypi.org/project/hol-guard/) · [docs](https://github.com/hashgraph-online/hol-guard/tree/main/docs/guard) · [source](https://github.com/hashgraph-online/hol-guard)

<details><summary>README extract</summary>

| | Stop risky AI actions before they compromise your machine. HOL Guard is a local-first security layer for AI agents, tools, plugins, skills, MCP servers, and package installs.

Install HOL Guard
Read the documentation
PyPI Package (`hol-guard`)
Report an Issue | ...

Features:
AI agents can run commands, install dependencies, read files, and call external tools within one session. HOL Guard reviews those actions at supported execution points and keeps the policy decision, approval request, and receipt together. ...

...

</details>

### cerbos-sqlalchemy

SQLAlchemy adapter for generating queries with Cerbos: an open core, language-agnostic, scalable authorization solution

`pip install cerbos-sqlalchemy` · installs (wheel) · licence: Apache-2.0 · rank 11066 · last release 2026-08-03 · [PyPI](https://pypi.org/project/cerbos-sqlalchemy/) · [source](https://github.com/cerbos/query-plan-adapters/tree/main/sqlalchemy)

<details><summary>README extract</summary>

An adapter library that takes a Cerbos Query Plan (PlanResources API) response and converts it into a SQLAlchemy Select instance. This is designed to work alongside a project using the Cerbos Python SDK. ...

Example:
```python
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.model import Principal, ResourceDesc

from cerbos_sqlalchemy import get_query
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import Select

Base = declarative_base()

class LeaveRequest(Base):
    tablename = "leave_request"

...
```

Sections: Cerbos + SQLAlchemy Adapter, Conformance contract, Requirements, Database collation requirements, Usage, Overriding default predicates

</details>

### tempenv

Environment Variable Context Manager

`pip install tempenv` · installs (wheel) · licence: Apache Software License · rank 11135 · last release 2025-03-23 · [PyPI](https://pypi.org/project/tempenv/)

<details><summary>README extract</summary>

Manage environment variables in a temporary scope.

Some products use environment variables as a primary means to supply
credentials. To ensure the lifetime of exposed credentials is short,
wrap them in a TemporaryEnvironment so that they are automatically
destroyed on scope exit.

You can: ...

Example:
```python
def test_set(self):
    user_before = os.environ.get("USER")
    with TemporaryEnvironment({"USER": "nobody", "OTHER": "foo"}):
        assert os.environ.get("USER") == "nobody"
        assert os.environ.get("OTHER") == "foo"
    assert os.environ.get("USER") == user_before
```

Sections: tempenv, Examples, Bugs

</details>

### mitreattack-python

MITRE ATT&CK python library

`pip install mitreattack-python` · installs (wheel) · licence: Apache Software License · rank 11194 · last release 2026-11-05 · [PyPI](https://pypi.org/project/mitreattack-python/) · [docs](https://mitreattack-python.readthedocs.io/) · [source](https://github.com/mitre-attack/mitreattack-python/)

<details><summary>README extract</summary>

This repository contains a library of Python tools and utilities for working with ATT&CK data.
For more information, see the full documentation on ReadTheDocs.

Sections: mitreattack-python, MitreAttackData Library, Related MITRE Work, CTI, ATT&CK, STIX

</details>

### pyscard

Smartcard module for Python.

`pip install pyscard` · installs from source (sdist only) · licence: GNU Lesser General Public License v2 or later (LGPLv2+) · rank 11221 · last release 2026-10-27 · [PyPI](https://pypi.org/project/pyscard/)

_README extract left out: share-alike licence._

### landlock

Python interface to the Landlock Linux Security Module.

`pip install landlock` · installs (wheel) · licence: MIT License · rank 11359 · last release 2025-05-03 · [PyPI](https://pypi.org/project/landlock/)

<details><summary>README extract</summary>

Harden your Python code by with rule-based file system access restrictions.

Features:
| Landlock ABI Version | Feature | Supported |

| 1 | Initial support | ✅ |
| 2 | File renaming and linking | ✅ |
| 3 | File truncation | ✅ |
| 4 | TCP bind and connect | ❌ |
| 5 | Device IOCTL | ✅ |
| 6 | Abstract UNIX socket | ❌ |
| 7 | Linux ...

Example:
```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
```

Sections: 🔒🐍 Landlock for Python, Example, Features

</details>

### vici

Native Python interface for strongSwan's VICI protocol

`pip install vici` · installs (wheel) · licence: MIT · rank 11467 · last release 2025-10-27 · [PyPI](https://pypi.org/project/vici/)

<details><summary>README extract</summary>

About

The strongSwan VICI protocol allows external applications to monitor, configure
and control the IKE daemon charon. This Python package provides a native client
side implementation of the VICI protocol, well suited to script automated tasks
in a reliable way.

Basic Usage

.. code-block:: python ...

</details>

### nono-py

Python bindings for nono capability-based sandboxing

`pip install nono-py` · installs (wheel) · licence: Apache Software License · rank 11677 · last release 2026-08-24 · [PyPI](https://pypi.org/project/nono-py/) · [docs](https://docs.nono.sh) · [source](https://github.com/nolabs-ai/nono-py)

<details><summary>README extract</summary>

Python bindings for nono, a capability-based sandboxing library.

nono provides OS-enforced sandboxing using Landlock (Linux) and Seatbelt (macOS). Once a sandbox is applied, unauthorized operations are structurally impossible.

Example:
```python
from nono_py import CapabilitySet, AccessMode, apply, is_supported

# Check platform support
if not is_supported():
    print("Sandboxing not supported on this platform")
    exit(1)

# Build capability set
caps = CapabilitySet()
caps.allow_path("/tmp", AccessMode.READ_WRITE)
caps.allow_path("/home/user/project", AccessMode.READ)
...
```

Sections: nono-py, From source, Usage, API Reference, Sandboxing, `CapabilitySet` + `apply()`, `sandboxed_exec`, Network Proxy, Filesystem Snapshots, Audit Trail, Resource Limiting, Other Classes, Functions

</details>

### smda

A recursive disassembler optimized for CFG recovery from memory dumps. Based on capstone.

`pip install smda` · installs (wheel) · licence: BSD-2-Clause · rank 11678 · last release 2026-10-30 · [PyPI](https://pypi.org/project/smda/) · [source](https://github.com/danielplohmann/smda)

<details><summary>README extract</summary>

SMDA is a minimalist recursive disassembler library optimized for accurate Control Flow Graph (CFG)
recovery from memory dumps. It is based on Capstone and analyzes
PE, ELF and Mach-O files, .NET assemblies, raw DEX files, and arbitrary memory dumps (ideally with a
known base address). ...

Example:
```python
>>> from smda.Disassembler import Disassembler
>>> disassembler = Disassembler()
>>> report = disassembler.disassembleFile("/bin/cat")
>>> print(report)
 0.068s -> (architecture: intel.64bit, base_addr: 0x00000000): 140 functions
>>> for fn in report.getFunctions():
...     print(fn)
...     for ins in fn.getInstructions():
...         print(ins)
...
```

...

</details>

### stix2-validator

APIs and scripts for validating STIX 2.x documents.

`pip install stix2-validator` · installs (wheel) · licence: BSD License · rank 12048 · last release 2026-11-06 · [PyPI](https://pypi.org/project/stix2-validator/) · [docs](https://stix2-validator.readthedocs.io/) · [source](https://github.com/oasis-open/cti-stix-validator/)

<details><summary>README extract</summary>

NOTE: This is an OASIS TC Open Repository. See the Governance
section for more information.

The STIX Validator checks that STIX JSON content conforms to the
requirements specified in the STIX 2.1 specification. ...

Example:
```python
from stix2validator import validate_file, print_results

results = validate_file("stix_file.json")
print_results(results)
```

Sections: `cti-stix-validator`, `Usage`, As A Script, As A Library, Governance, `About OASIS TC Open Repositories`, `Feedback`

</details>

### keepercommander

Keeper Commander for Python 3

`pip install keepercommander` · installs (wheel) · licence: MIT License · rank 12120 · last release 2026-11-03 · [PyPI](https://pypi.org/project/keepercommander/)

<details><summary>README extract</summary>

Keeper Commander is a command-line and terminal UI interface to Keeper® Password Manager and KeeperPAM. Commander can be used to access and control your Keeper vault, perform administrative actions (managing users, teams, roles, SSO, privileged access resources, device approvals, data import/export), launch sessions, rotate passwords, integrate ...

Sections: About Keeper Commander, Windows and macOS Binaries, Linux / Python using PIP, Running from Source, Starting Commander, Documentation

</details>

### skylos

Python dead code, security and secrets scanner with a pull-request gate; narrower checks for TypeScript, Java and more.

`pip install skylos` · installs (wheel) · licence: Apache-2.0 · rank 12220 · last release 2026-11-02 · [PyPI](https://pypi.org/project/skylos/) · [docs](https://docs.skylos.dev) · [source](https://github.com/duriantaco/skylos)

<details><summary>README extract</summary>

Code checks that show their work.

Skylos is an open-source (Apache-2.0) CLI and pull-request gate for Python
projects that runs without an account. `skylos .` finds dead code: unused
functions, classes, imports and empty files. Add `-a` to check security bugs,
hard-coded secrets, vulnerable dependencies, code quality and AI-code
mistakes. ...

Sections: Skylos, What Is Skylos?, Read The Results, Choose the Right Command, Start In 60 Seconds, Check Every Agent Edit (Claude Code, Codex, Cursor), Common Workflows, What Skylos Catches, Give Coding Agents Project Standards, Verify AI Agents Before They Ship, Test Running Agent Behavior, How Skylos Fits, What Leaves Your Machine, Agent Harness Artifacts

</details>

### django-user-sessions

Django sessions with a foreign key to the user

`pip install django-user-sessions` · installs (wheel) · licence: MIT License · rank 12276 · last release 2022-12-13 · [PyPI](https://pypi.org/project/django-user-sessions/)

<details><summary>README extract</summary>

Django includes excellent built-in sessions, however all the data is hidden
away into base64 encoded data. This makes it very difficult to run a query on
all active sessions for a particular user. `django-user-sessions` fixes this
and makes session objects a first class citizen like other ORM objects. ...

Features:
To get the list of a user's sessions:

Or logout the user everywhere:

The user's IP address and user agent are also stored on the session. This
allows to show a list of active sessions to the user in the admin:

And also in a custom layout:

Example:
```python
user.session_set.filter(expire_date__gt=now())
```

Sections: Django User Sessions, Features, GeoIP, Getting help, Running tests, Releasing

</details>

### navi-sanitize

Deterministic sanitization for untrusted text: strips invisible and control characters, applies NFKC and replaces common homoglyphs. No dependencies.

`pip install navi-sanitize` · installs (wheel) · licence: MIT · rank 12374 · last release 2026-09-29 · [PyPI](https://pypi.org/project/navi-sanitize/) · [docs](https://docs.projectnavi.ai/navi-sanitize) · [source](https://github.com/Project-Navi/navi-sanitize)

<details><summary>README extract</summary>

Deterministic sanitization of untrusted text for Python 3.12+, with no dependencies.
`clean()` removes null bytes and 492 invisible, formatting and control characters,
applies NFKC normalization, and replaces 66 curated homoglyphs (Cyrillic, Greek,
Armenian, Cherokee, Latin Extended and typographic lookalikes) with ASCII. ...

Example:
```python
from navi_sanitize import clean, path_escaper, walk

clean("Неllo Wоrld")                             # 'Hello World' (Cyrillic Н, о)
clean("pass\u200bword\x00")                      # 'password'
clean("ｆｕｌｌ ｗｉｄｔｈ")                     # 'full width'
clean("../../etc/passwd", escaper=path_escaper)  # 'etc/passwd'
...
```

Sections: navi-sanitize, Limits, Documentation

</details>

### pysentry-rs

Security vulnerability auditing tool for Python packages

`pip install pysentry-rs` · installs (wheel) · licence: MIT License · rank 12535 · last release 2026-08-20 · [PyPI](https://pypi.org/project/pysentry-rs/) · [source](https://github.com/nyudenkov/pysentry)

<details><summary>README extract</summary>

Fast, reliable vulnerability scanning for Python dependencies.

Documentation · Benchmarks · Help test & improve · Usage survey

PySentry audits Python projects for known security vulnerabilities. ...

Features:
- Every dependency format — `uv.lock`, `poetry.lock`, `Pipfile.lock`, `pylock.toml`, `pyproject.toml`, `Pipfile`, `requirements.txt`, and PEP 723 inline script metadata. Lock files take precedence when both are present. ...

Sections: PySentry, Features, Used by, Quick start, Pre-commit, CI, Configuration, Documentation, Requirements, Feedback

</details>

### osquery

Osquery Python API

`pip install osquery` · installs (wheel) · licence: BSD License · rank 12689 · last release 2024-07-24 · [PyPI](https://pypi.org/project/osquery/)

<details><summary>README extract</summary>

osquery exposes an operating system as a high-performance relational database. This allows you to write SQL-based queries to explore operating system data. With osquery, SQL tables represent abstract concepts such as running processes, loaded kernel modules, open network connections, browser plugins, hardware events or file hashes. ...

Example:
```python
# !/usr/bin/env python

import osquery

@osquery.register_plugin
class MyTablePlugin(osquery.TablePlugin):
    def name(self):
        return "foobar"

    def columns(self):
        return [
            osquery.TableColumn(name="foo", type=osquery.STRING),
            osquery.TableColumn(name="baz", type=osquery.STRING),
        ]

...
```

...

</details>

### aws-encryption-sdk-cli

This command line tool can be used to encrypt and decrypt files and directories using the AWS Encryption SDK.

`pip install aws-encryption-sdk-cli` · installs (wheel) · licence: Apache Software License · rank 12825 · last release 2025-11-27 · [PyPI](https://pypi.org/project/aws-encryption-sdk-cli/)

<details><summary>README extract</summary>

This command line tool can be used to encrypt and decrypt files and directories using the AWS Encryption SDK.

The latest full documentation can be found at Read the Docs.

Find us on GitHub.

Security issue notifications

See Support Policy for details on the current support status of all major versions of this library.

Example:
```python
# With parameters:
--wrapping-keys provider=aws-kms key=$KEY_1 key=$KEY_2

# KMSMasterKeyProvider is called as:
key_provider = StrictAwsKmsMasterKeyProvider(key_ids=[$KEY_1, $KEY_2])
```

Sections: aws-encryption-sdk-cli, Getting Started, Required Prerequisites, Usage, Input and Output, Parameter Values, Encryption Context, Encrypt, Decrypt, Output Metadata, Skipped Files, Master Key Provider, AWS KMS, Advanced Configuration

</details>

### bridgecrew

Infrastructure as code static analysis

`pip install bridgecrew` · installs (wheel) · licence: Apache Software License · rank 12871 · last release 2026-03-26 · [PyPI](https://pypi.org/project/bridgecrew/)

### srp

Secure Remote Password

`pip install srp` · installs (wheel) · licence: BSD License · rank 12961 · last release 2024-11-01 · [PyPI](https://pypi.org/project/srp/)

<details><summary>README extract</summary>

This package provides an implementation of the Secure Remote Password
protocol (SRP). SRP is a cryptographically strong authentication
protocol for password-based, mutual authentication over an insecure
network connection. ...

</details>

### dlint

Dlint is a tool for encouraging best coding practices and helping ensure Python code is secure.

`pip install dlint` · installs (wheel) · licence: BSD-3-Clause · rank 13026 · last release 2026-10-20 · [PyPI](https://pypi.org/project/dlint/) · [source](https://github.com/dlint-py/dlint)

<details><summary>README extract</summary>

Dlint is a tool for encouraging best coding practices and helping ensure Python code is secure.

> The most important thing I have done as a programmer in recent years is to
> aggressively pursue static code analysis. ...

Sections: Dlint, Using, CLI, Inline Editor, Integrating, Custom Plugins, Linting, Coverage, Benchmarking

</details>

### django-password-validators

Additional libraries for validating passwords in Django.

`pip install django-password-validators` · installs (wheel) · licence: BSD License · rank 13202 · last release 2023-12-11 · [PyPI](https://pypi.org/project/django-password-validators/)

<details><summary>README extract</summary>

Additional libraries for validating passwords in Django 3.2 or later.

The application works well under python 4.x and 3.x versions.

Django version after the number 1.9, allows you to configure password validation.
Configuration validation is placed under the variable AUTH_PASSWORD_VALIDATORS.

Sections: Django Password Validators, Validators, UniquePasswordsValidator, PasswordCharacterValidator

</details>

### fuzzfetch

Downloader for firefox/jsshell builds.

`pip install fuzzfetch` · installs (wheel) · licence: Mozilla Public License 2.0 (MPL 2.0) · rank 13339 · last release 2025-12-11 · [PyPI](https://pypi.org/project/fuzzfetch/)

<details><summary>README extract</summary>

Fuzzfetch is a python tool for retrieving builds from the Firefox-CI Taskcluster instance.

Overview

Fuzzfetch can be used to retrieve nearly any build type indexed by Firefox-CI. This includes AddressSanitizer, ThreadSanitizer, Valgrind, debug, and Fuzzing builds for Firefox, Spidermonkey, and Thunderbird.

Installation

Usage ...

</details>

### ca9

Open source Python package security and evidence-backed SCA triage

`pip install ca9` · installs (wheel) · licence: MPL-2.0 · rank 13393 · last release 2026-11-07 · [PyPI](https://pypi.org/project/ca9/) · [docs](https://duriantaco.github.io/ca9/) · [source](https://github.com/duriantaco/ca9)

<details><summary>README extract</summary>

Local, evidence-backed supply-chain defense for open-source packages.

ca9 is the supply-chain engine behind the dependency and install checks in
Skylos. Skylos calls ca9's library API
(`ca9.api`) to decide whether a package is malicious, too new, confused with an
internal name, installed from a mutable or untrusted source, or published
without ...

Example:
```python
import json
from pathlib import Path
from ca9.parsers.snyk import SnykParser
from ca9.engine import analyze

data = json.loads(Path("snyk.json").read_text())
vulns = SnykParser().parse(data)

report = analyze(
    vulnerabilities=vulns,
    repo_path=Path("./my-project"),
    coverage_path=Path("coverage.json"),
)

for result in report.results:
...
```

...

</details>

### S3Scanner

Scan for open S3 buckets and dump the contents

`pip install S3Scanner` · installs (wheel) · licence: MIT License · rank 13554 · last release 2021-11-29 · [PyPI](https://pypi.org/project/S3Scanner/)

<details><summary>README extract</summary>

A tool to find open S3 buckets and dump their contents💧

Features:
* ⚡️ Multi-threaded scanning
* 🔭 Supports tons of S3-compatible APIs
* 🕵️‍♀️ Scans all bucket permissions to find misconfigurations
* 💾 Dump bucket contents to a local folder
* 🐳 Docker support

Sections: S3Scanner, Usage, Features, Examples, S3-compatible APIs, Interpreting Results

</details>

### strongdm

strongDM SDK for the Python programming language.

`pip install strongdm` · installs from source (sdist only) · licence: Apache Software License · rank 13589 · last release 2026-11-04 · [PyPI](https://pypi.org/project/strongdm/)

<details><summary>README extract</summary>

This is the official strongDM SDK for the Python
programming language.

Learn more with our 📚strongDM API docs or
📓browse the SDK
reference.

Example:
```python
import os
import strongdm

def main():
    client = strongdm.Client(os.getenv("SDM_API_ACCESS_KEY"),
                        os.getenv("SDM_API_SECRET_KEY"))

    users = client.accounts.list('')
    for user in users:
        print(user)

if name == "main":
    main()
```

Sections: strongDM SDK for Python, Authentication, List Users, Useful Links

</details>

### yubico-client

Library for verifying Yubikey One Time Passwords (OTPs)

`pip install yubico-client` · installs (wheel) · licence: BSD License · rank 13669 · last release 2020-05-21 · [PyPI](https://pypi.org/project/yubico-client/)

<details><summary>README extract</summary>

Python class for verifying Yubico One Time Passwords (OTPs) based on the
validation protocol version 2.0.

For more information and usage examples, please see the.
documentation.

Documentation is available at

Sections: Yubico Python Client, Documentation, Running Tests, 1.13.0 - 2020-05-21, 1.12.0 - 2019-11-18, 1.11.0 - 2019-07-06, 1.10.0 - 2015-10-02, 1.9.1 - 2014-02-05, 1.9.0 - 2014-01-16, 1.8.0 - 2013-11-09, 1.7.0 - 2013-04-06, 1.6.2 - 2013-04-02, 1.6.1 - 2013-03-19, 1.6.0 - 2013-01-24

</details>

### k5test

A library for testing Python applications in self-contained Kerberos 5 environments

`pip install k5test` · installs (wheel) · licence: ISC License (ISCL); MIT License · rank 13687 · last release 2024-03-20 · [PyPI](https://pypi.org/project/k5test/)

<details><summary>README extract</summary>

*k5test* is a library for setting up self-contained Kerberos 5 environments,
and running Python unit tests inside those environments. It is based on
the file of the same name found alongside the MIT Kerberos 5 unit tests.

*k5test* can be used to set up a self-contained MIT krb5 or Heimdal
environment. ...

Sections: K5Test, Using k5test to set up a Kerberos 5 deployment, Using k5test to run unit tests

</details>

### bbot

OSINT automation for hackers.

`pip install bbot` · installs (wheel) · licence: AGPL-3.0 · rank 13832 · last release 2026-08-24 · [PyPI](https://pypi.org/project/bbot/) · [docs](https://www.blacklanternsecurity.com/bbot/) · [source](https://github.com/blacklanternsecurity/bbot)

_README extract left out: share-alike licence._

### sherlock-project

Hunt down social media accounts by username across social networks

`pip install sherlock-project` · installs (wheel) · licence: MIT License · rank 13945 · last release 2026-09-10 · [PyPI](https://pypi.org/project/sherlock-project/) · [source](https://github.com/sherlock-project/sherlock)

<details><summary>README extract</summary>

Hunt down social media accounts by username across 400+ social networks

 Additional documentation can be found at our GitHub repository

</details>

### python-flirt

A Python library for parsing, compiling, and matching Fast Library Identification and Recognition Technology (FLIRT) signatures.

`pip install python-flirt` · installs (wheel) · licence: Apache Software License · rank 13968 · last release 2026-10-23 · [PyPI](https://pypi.org/project/python-flirt/) · [source](https://github.com/williballenthin/lancelot/tree/master/pyflirt)

<details><summary>README extract</summary>

A Python library for parsing, compiling, and matching Fast Library Identification and Recognition Technology (FLIRT) signatures. These signatures are typically used by the Hex-Rays IDA Pro tool; this library is the result of reverse engineering the matching engine and reimplementing parsers and matchers. ...

Example:
```python
setuptools.setup(
  ...
  install_requires=[
    "python-flirt~=0.6.3",
  ]
  ...
)
```

Sections: python-flirt, Usage, Usage: signature file formats, Usage: matching references, Usage: example tool

</details>

### appthreat-vulnerability-db

AppThreat's vulnerability database and package search library with a built-in sqlite based storage. OSV, CVE, GitHub, npm are the primary sources of vulnerabilities.

`pip install appthreat-vulnerability-db` · installs (wheel) · licence: MIT License · rank 13989 · last release 2026-11-03 · [PyPI](https://pypi.org/project/appthreat-vulnerability-db/)

<details><summary>README extract</summary>

An offline vulnerability database and package search library. `vdb` downloads
data from AppThreat vuln-list, OSV, NVD and GitHub, converts it into the CVE 5.2
schema, and stores it in SQLite with indexes built for fast offline lookup by
purl, CPE or git URL. ...

Features:
Advisories are merged from several upstream feeds because the same CVE is
often published independently by NVD, an OSV feed and a GitHub advisory, with
different affected ranges; querying the union of them reduces false negatives. ...

Example:
```python
import json
import os
from vdb.lib import config, db as db_lib, search
from vdb.lib.orasclient import download_image

# Prefer an organization-controlled URL. The upstream default is for local
# testing and bootstrap.
...

</details>

### fingerprint-pro-server-api-sdk

This version of SDK is marked as deprecated. Please follow our [migration guide](https://dev.fingerprint.com/reference/migrating-from-server-api-v3-to-v4) to migrate. Fingerprint Server API allows you to search, update, and delete identification events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.

`pip install fingerprint-pro-server-api-sdk` · installs (wheel) · licence: MIT License · rank 14196 · last release 2026-09-29 · [PyPI](https://pypi.org/project/fingerprint-pro-server-api-sdk/) · [source](https://github.com/fingerprintjs/python-sdk)

<details><summary>README extract</summary>

> [!WARNING]
> This version is deprecated. Please upgrade to the latest Python SDK version.

> [!IMPORTANT]
> This SDK package is deprecated. This package (`fingerprint_pro_server_api_sdk`) uses Server API v3.
> Please migrate to the new `fingerprint_server_sdk` package, which uses Server API v4. Follow the migration guide for details. ...

Example:
```python
import fingerprint_pro_server_api_sdk

# Configure API key authorization and region
configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY")
# configuration = fingerprint_pro_server_api_sdk.Configuration(api_key="SECRET_API_KEY", region="eu")

# create an instance of the API class
...
```

...

</details>

### microsandbox

Python SDK for microsandbox — secure, fast microVM-based sandboxing.

`pip install microsandbox` · installs (wheel) · licence: Apache Software License · rank 14269 · last release 2026-11-01 · [PyPI](https://pypi.org/project/microsandbox/) · [docs](https://docs.microsandbox.dev) · [source](https://github.com/superradcompany/microsandbox)

<details><summary>README extract</summary>

Lightweight VM sandboxes for Python applications that need hardware-level isolation for AI agents, tools, tests, and untrusted code.

The `microsandbox` Python package provides async Python bindings to the microsandbox runtime. ...

Features:
- Hardware VM isolation with a guest Linux kernel
- Async sandbox lifecycle, execution, filesystem, metrics, and logs APIs
- OCI image, bind-rootfs, disk-image, and snapshot-based sandboxes ...

Example:
```python
import asyncio

from microsandbox import Sandbox

async def main() -> None:
    async with await Sandbox.create("python-readme", image="alpine", replace=True) as sandbox:
        output = await sandbox.shell("echo 'Hello from microsandbox!'")
        print(output.stdout_text.strip())

asyncio.run(main())
```

...

</details>

### axioms-fastapi

OAuth2/OIDC authentication and authorization for FastAPI APIs

`pip install axioms-fastapi` · installs (wheel) · licence: MIT License · rank 14322 · last release 2025-11-15 · [PyPI](https://pypi.org/project/axioms-fastapi/) · [docs](https://axioms-fastapi.abhishek-tiwari.com) · [source](https://github.com/abhishektiwari/axioms-fastapi)

<details><summary>README extract</summary>

OAuth2/OIDC authentication and authorization for FastAPI APIs. Supports authentication and claim-based fine-grained authorization (scopes, roles, permissions) using JWT tokens. Works with access tokens issued by various authorization servers including AWS Cognito, Auth0, Okta, Microsoft Entra, etc. ...

Features:
* JWT token validation with automatic public key retrieval from JWKS endpoints
* Algorithm validation to prevent algorithm confusion attacks (only secure asymmetric algorithms allowed)
* Issuer validation (`iss` claim) to prevent token substitution ...

Example:
```python
from fastapi import FastAPI, Depends
from axioms_fastapi import init_axioms, require_auth, require_scopes, register_axioms_exception_handler

app = FastAPI()

# Initialize Axioms with your configuration
...

</details>

### filebytes

Scripts to parse the following file formats - Executable and Linking Format (ELF), Portable Executable (PE), Mach-O and OAT (Android Runtime).

`pip install filebytes` · installs from source (sdist only) · licence: BSD License · rank 14328 · last release 2020-02-09 · [PyPI](https://pypi.org/project/filebytes/)

### aws-google-auth

Acquire AWS STS (temporary) credentials via Google Apps SAML Single Sign On

`pip install aws-google-auth` · installs (wheel) · licence: MIT License · rank 14521 · last release 2022-05-02 · [PyPI](https://pypi.org/project/aws-google-auth/)

<details><summary>README extract</summary>

This command-line tool allows you to acquire AWS temporary (STS)
credentials using Google Apps as a federated (Single Sign-On, or SSO)
provider.

You'll first have to set up Google Apps as a SAML identity provider
(IdP) for AWS. ...

Sections: aws-google-auth, Setup, Important Data, Usage, Native Python, Via Docker, Feeding password from stdin, Storage of profile credentials, Notes on Authentication

</details>

### mrz

Machine readable zone generator and checker for passports, visas, id cards and other travel documents

`pip install mrz` · installs (wheel) · licence: GNU General Public License v3 (GPLv3) · rank 14564 · last release 2020-08-31 · [PyPI](https://pypi.org/project/mrz/)

_README extract left out: share-alike licence._

### owasp-depscan

Fully open-source security audit for project dependencies based on known vulnerabilities and advisories.

`pip install owasp-depscan` · installs (wheel) · licence: MIT · rank 14928 · last release 2026-11-07 · [PyPI](https://pypi.org/project/owasp-depscan/)

<details><summary>README extract</summary>

OWASP dep-scan is a next-generation security and risk audit tool based on known vulnerabilities, advisories, and license limitations for project dependencies. Both local repositories and container images are supported as the input, and the tool is ideal for integration with ASPM/VM platforms and in CI environments.

Features:
- Scan most application code (local repos, Linux container images, Kubernetes manifests, and OS) to identify known CVEs with prioritization
- Perform advanced reachability analysis for multiple languages (see the reachability matrix below) ...

...

</details>

## Also in this topic

- [Authlib](internet-www-http.md#authlib) - The ultimate Python library in building OAuth and OpenID Connect servers and clients.
- [magika](scientific-engineering-artificial-intelligence.md#magika) - A tool to determine the content type of a file with deep learning
- [courlan](internet-www-http.md#courlan) - Clean, filter and sample URLs to optimize data collection – includes spam, content type and language filters.
- [trafilatura](internet-www-http.md#trafilatura) - Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML.
- [netaddr](communications.md#netaddr) - A network address manipulation library for Python
- [ndg-httpsclient](internet.md#ndg-httpsclient) - Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
- [mitmproxy](internet-proxy-servers.md#mitmproxy) - An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.
- [django-axes](internet-log-analysis.md#django-axes) - Keep track of failed login attempts in Django-powered sites.
- [txtorcon](internet.md#txtorcon) - Twisted-based Tor controller client, with state-tracking and configuration abstractions. https://txtorcon.readthedocs.org https://github.com/meejah/txtorcon
- [acme](internet-www-http.md#acme) - ACME protocol implementation in Python
- [jwt](internet-www-http.md#jwt) - JSON Web Token library for Python 3.
- [josepy](internet-www-http.md#josepy) - JOSE protocol implementation in Python
- [csp-toolkit](internet-www-http.md#csp-toolkit) - Parse, analyze, generate, and find bypasses in Content Security Policy headers
- [certbot](internet-www-http.md#certbot) - ACME client
- [certbot-dns-cloudflare](internet-www-http.md#certbot-dns-cloudflare) - Cloudflare DNS Authenticator plugin for Certbot
- [scrapy-stealth](internet-www-http.md#scrapy-stealth) - Stealthy Crawling. Maximum Results. A pluggable anti-bot and stealth framework for Scrapy.
- [django-encrypted-model-fields](internet-www-http.md#django-encrypted-model-fields) - A set of fields that wrap standard Django fields with encryption provided by the python cryptography library.
- [pymacaroons](internet-www-http.md#pymacaroons) - Macaroon library for Python
- [djangosaml2](internet-www-http.md#djangosaml2) - pysaml2 integration for Django
- [TgCrypto](communications.md#tgcrypto) - Fast and Portable Cryptography Extension Library for Pyrogram
- [openshell](scientific-engineering.md#openshell) - OpenShell is the safe, private runtime for autonomous AI agents.
- [dissect.cstruct](internet-log-analysis.md#dissectcstruct) - A Dissect module implementing a parser for C-like structures: structure parsing in Python made easy
- [veracode-api-signing](internet-www-http.md#veracode-api-signing) - Easily sign any request destined for the Veracode API Gateway
- [pymisp](internet.md#pymisp) - Python API for MISP.
- [prov](scientific-engineering-information-analysis.md#prov) - A library for W3C Provenance Data Model supporting PROV-N, PROV-JSON, PROV-XML, PROV-O (RDF) and PROV-JSONLD
- [dissect.util](internet-log-analysis.md#dissectutil) - A Dissect module implementing various utility functions for the other Dissect modules
- [django-graphql-jwt](internet.md#django-graphql-jwt) - JSON Web Token for Django GraphQL.
- [geoip2fast](internet.md#geoip2fast) - GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!
- [hstspreload](internet-www-http.md#hstspreload) - Chromium HSTS Preload list as a Python package
- [boxlite](scientific-engineering-artificial-intelligence.md#boxlite) - Python bindings for Boxlite runtime
- [dissect.ntfs](internet-log-analysis.md#dissectntfs) - A Dissect module implementing a parser for the NTFS file system, used by the Windows operating system
- [PyLTI1p3](internet-www-http.md#pylti1p3) - LTI 1.3 Advantage Tool implementation in Python
- [django-simple-captcha](internet-www-http.md#django-simple-captcha) - A very simple, yet powerful, Django captcha application
- [dissect.esedb](internet-log-analysis.md#dissectesedb) - Superseded by dissect.database. A Dissect module implementing a parser for Microsofts Extensible Storage Engine Database (ESEDB), used for example in Active Directory, Exchange and Windows Update
- [wafw00f](internet.md#wafw00f) - The Web Application Firewall Fingerprinting Toolkit
- [agent_governance_toolkit](scientific-engineering-artificial-intelligence.md#agent_governance_toolkit) - Public Preview — Unified installer and runtime policy enforcement for the Agent Governance Toolkit
- [django-defender](internet-www-http.md#django-defender) - redis based Django app that locks out users after too many failed login attempts.
- [advocate](internet-www-http.md#advocate) - A wrapper around the requests library for safely making HTTP requests on behalf of a third party
- [censys](documentation-sphinx.md#censys) - An easy-to-use and lightweight API wrapper for Censys APIs (censys.io).
- [agentrust-trace](scientific-engineering-artificial-intelligence.md#agentrust-trace) - TRACE v0.2: hardware-attested governance records for AI agents
- [aiocoap](internet.md#aiocoap) - Python CoAP library
- [h2o-authn](internet.md#h2o-authn) - H2O Python Clients Authentication Helpers
- [certbot-dns-route53](internet-www-http-2.md#certbot-dns-route53) - Route53 DNS Authenticator plugin for Certbot
- [keeper-pam-webrtc-rs](communications.md#keeper-pam-webrtc-rs) - Keeper PAM WebRTC for Python - A secure, stable, and high-performance Tube API for Python, providing WebRTC-based secure tunneling with enterprise-grade security and reliability optimizations.
- [safe-netrc](internet.md#safe-netrc) - Safe netrc file parser
- [aia](internet-www-http-2.md#aia) - AIA chasing through OpenSSL for TLS certificate chain building and verifying
- [certbot-nginx](internet-www-http-2.md#certbot-nginx) - Nginx plugin for Certbot
- [checkdmarc](communications-email.md#checkdmarc) - A Python module and command line parser for SPF and DMARC records
- [oidc-provider-mock](internet-www-http-2.md#oidc-provider-mock) - OpenID Connect provider server for testing authentication
- [django-otp-webauthn](communications-fido.md#django-otp-webauthn) - FIDO2 WebAuthn support for django-otp: lets your users authenticate with Passkeys
- [socid-extractor](internet-www-http-2.md#socid-extractor) - Extract accounts' identifiers and metadata from personal pages on various platforms.
- [onetimepass](internet-www-http-2.md#onetimepass) - Module for generating and validating HOTP and TOTP tokens
- [asyncwhois](internet-www-http-2.md#asyncwhois) - Python WHOIS and RDAP utility for querying and parsing information about Domains, IPv4s, IPv6s, and AS numbers.
- [dnsdb2](internet-name-service-dns.md#dnsdb2) - Client for DNSDB API version 2 with Flexible Search
- [dissect.target](internet-log-analysis.md#dissecttarget) - This module ties all other Dissect modules together, it provides a programming API and command line tools which allow easy access to various data sources inside disk images or file collections (a.k.a. targets)
- [drf-recaptcha](internet-www-http-2.md#drf-recaptcha) - Django rest framework recaptcha field serializer
- [fastapi-guard](internet-www-http-2.md#fastapi-guard) - Production-ready security middleware for FastAPI — IP filtering, rate limiting, penetration detection, and 20+ per-route security decorators.
