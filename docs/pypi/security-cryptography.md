# Security / Cryptography

[Index](README.md) · 64 packages in this topic, 36 more listed under another topic, by downloads.

### cryptography

cryptography is a package which provides cryptographic recipes and primitives to Python developers.

`pip install cryptography` · installs (wheel) · licence: Apache-2.0 OR BSD-3-Clause · rank 9 · last release 2026-09-30 · [PyPI](https://pypi.org/project/cryptography/) · [docs](https://cryptography.io/) · [source](https://github.com/pyca/cryptography/)

<details><summary>README extract</summary>

`cryptography` is a package which provides cryptographic recipes and
primitives to Python developers. Our goal is for it to be your "cryptographic
standard library". It supports Python 3.9+ and PyPy3 7.3.11+. ...

Example:
```python
>>> from cryptography.fernet import Fernet
>>> # Put this somewhere safe!
>>> key = Fernet.generate_key()
>>> f = Fernet(key)
>>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
>>> token
b'...'
>>> f.decrypt(token)
b'A really secret message. Not for prying eyes.'
```

Sections: pyca/cryptography, Discussion

</details>

### rsa

Pure-Python RSA implementation

`pip install rsa` · installs (wheel) · licence: Apache Software License · rank 157 · last release 2025-04-16 · [PyPI](https://pypi.org/project/rsa/) · [source](https://github.com/sybrenstuvel/python-rsa)

<details><summary>README extract</summary>

Hi folks,

I'm Sybren, one of the original authors and the maintainer of this project.
Unfortunately I don't have the time and brain space left to properly maintain
Python-RSA. As you can see from the lack of activity on the open issues, and the
lack of commits, that has been the case for a while now. ...

Sections: Python-RSA has been archived, Pure Python RSA implementation

</details>

### pyOpenSSL

Python wrapper module around the OpenSSL library

`pip install pyOpenSSL` · installs (wheel) · licence: Apache Software License · rank 166 · last release 2026-08-01 · [PyPI](https://pypi.org/project/pyOpenSSL/) · [source](https://github.com/pyca/pyopenssl)

<details><summary>README extract</summary>

Note: The Python Cryptographic Authority strongly suggests the use of pyca/cryptography
where possible. If you are using pyOpenSSL for anything other than making a TLS connection
you should move to cryptography and drop your pyOpenSSL dependency.

High-level wrapper around a subset of the OpenSSL library. Includes ...

Sections: pyOpenSSL -- A Python wrapper around the OpenSSL library, Discussion, 26.4.0 (2026-08-01), Backward-incompatible changes, Deprecations, Changes, 26.3.0 (2026-06-12), 26.2.0 (2026-05-04)

</details>

### asn1crypto

Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP

`pip install asn1crypto` · installs (wheel) · licence: MIT License · rank 229 · last release 2022-03-15 · [PyPI](https://pypi.org/project/asn1crypto/)

<details><summary>README extract</summary>

A fast, pure Python library for parsing and serializing ASN.1 structures.

 - Features
 - Why Another Python ASN.1 Library?
 - Related Crypto Libraries
 - Current Release
 - Dependencies
 - Installation
 - License
 - Security Policy
 - Documentation
 - Continuous Integration
 - Testing
 - Development
 - CI Tasks

Features:
In addition to an ASN.1 BER/DER decoder and DER serializer, the project includes
a bunch of ASN.1 structures for use with various common cryptography standards:

| Standard | Module | Source | ...

Sections: asn1crypto, Features, Why Another Python ASN.1 Library?, Related Crypto Libraries, Dependencies, Documentation, Tutorials, Reference, Continuous Integration, Git Repository, PyPi Source Distribution, Package, CI Tasks

</details>

### pycryptodome

Cryptographic library for Python

`pip install pycryptodome` · installs (wheel) · licence: BSD-2-Clause AND Unlicense AND MIT · rank 330 · last release 2026-11-07 · [PyPI](https://pypi.org/project/pycryptodome/) · [source](https://github.com/Legrandin/pycryptodome/)

<details><summary>README extract</summary>

PyCryptodome is a self-contained Python package of low-level
cryptographic primitives: one `pip install`, no system libraries,
and a broad, consistent API from AES and RSA to HPKE, KangarooTwelve and post-quantum ML-DSA.

It supports Python 3.9 and newer, and PyPy.

You install it with:
All modules are installed under the `Crypto` package.

Features:
* Self-contained. No runtime dependencies and no system libraries:
 all the C code ships with the package, so there is nothing else to install,
 patch, or keep in sync. Building from source only needs a C compiler. ...

Example:
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_GCM)         # a random nonce is generated
...

</details>

### argon2-cffi

Argon2 for Python

`pip install argon2-cffi` · installs (wheel) · licence: MIT · rank 344 · last release 2025-06-03 · [PyPI](https://pypi.org/project/argon2-cffi/) · [docs](https://argon2-cffi.readthedocs.io/) · [source](https://github.com/hynek/argon2-cffi)

<details><summary>README extract</summary>

Argon2 won the Password Hashing Competition and *argon2-cffi* is the simplest way to use it in Python:

<!-- end short -->

Example:
```python
>>> from argon2 import PasswordHasher
>>> ph = PasswordHasher()
>>> hash = ph.hash("correct horse battery staple")
>>> hash  # doctest: +SKIP
'$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'
>>> ph.verify(hash, "correct horse battery staple")
True
>>> ph.check_needs_rehash(hash)
False
...
```

Sections: argon2-cffi*: Argon2 for Python, Project Links, Added, Removed, Changed, argon2-cffi* for Enterprise

</details>

### pycryptodomex

Cryptographic library for Python

`pip install pycryptodomex` · installs (wheel) · licence: BSD License; Public Domain · rank 442 · last release 2026-11-05 · [PyPI](https://pypi.org/project/pycryptodomex/) · [source](https://github.com/Legrandin/pycryptodome/)

<details><summary>README extract</summary>

PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.

It supports Python 2.7, Python 3.8 and newer, and PyPy.

You can install it with:
All modules are installed under the `Cryptodome` package.

Check the pycryptodome project for the equivalent library that
works under the `Crypto` package. ...

</details>

### oscrypto

TLS (SSL) sockets, key generation, encryption, decryption, signing, verification and KDFs using the OS crypto libraries. Does not require a compiler, and relies on the OS for patching. Works on Windows, OS X and Linux/BSD.

`pip install oscrypto` · installs (wheel) · licence: MIT License · rank 867 · last release 2022-03-18 · [PyPI](https://pypi.org/project/oscrypto/)

<details><summary>README extract</summary>

A compilation-free, always up-to-date encryption library for Python that works
on Windows, OS X, Linux and BSD. Supports the following versions of Python:
2.6, 2.7, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10 and pypy. ...

Features:
Currently the following features are implemented. Many of these should only be
used for integration with existing/legacy systems. If you don't know which you
should, or should not use, please see Learning. ...

Sections: oscrypto, Features, Why Another Python Crypto Library?, Related Crypto Libraries, Dependencies, Documentation, Continuous Integration, Git Repository, Backend Options, Internet Tests, PyPi Source Distribution, Test Options, Force OpenSSL Shared Library Paths, Force Use of ctypes

</details>

### service-identity

Service identity verification for pyOpenSSL & cryptography.

`pip install service-identity` · installs (wheel) · licence: MIT · rank 869 · last release 2026-05-30 · [PyPI](https://pypi.org/project/service-identity/) · [docs](https://service-identity.readthedocs.io/) · [source](https://github.com/pyca/service-identity)

<details><summary>README extract</summary>

Use this package if:

- you want to verify that a PyCA *cryptography* certificate is valid for a certain hostname or IP address,
- or if you use pyOpenSSL and don’t want to be MITMed,
- or if you want to inspect certificates from either for service IDs. ...

Sections: Service Identity Verification for pyOpenSSL & *cryptography, Project Information, service-identity* for Enterprise, Added, Changed, Fixed

</details>

### pycrypto

Cryptographic modules for Python.

`pip install pycrypto` · installs from source (sdist only) · licence: Public Domain · rank 1296 · last release 2014-06-20 · [PyPI](https://pypi.org/project/pycrypto/)

<details><summary>README extract</summary>

This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.). The package is structured to make adding new modules easy. ...

</details>

### pyHanko

Tools for stamping and signing PDF files

`pip install pyHanko` · installs (wheel) · licence: MIT · rank 1720 · last release 2026-11-03 · [PyPI](https://pypi.org/project/pyHanko/) · [docs](https://docs.pyhanko.eu/) · [source](https://github.com/MatthiasValvekens/pyHanko)

<details><summary>README extract</summary>

``pyhanko`` is a library for working with signatures in PDF documents.

Note: pyHanko's CLI is no longer bundled together with the library. This functionality is now
distributed separately as ``pyhanko-cli``. ...

</details>

### pyhanko-certvalidator

Validates X.509 certificates and paths; forked from wbond/certvalidator

`pip install pyhanko-certvalidator` · installs (wheel) · licence: MIT · rank 1757 · last release 2026-10-17 · [PyPI](https://pypi.org/project/pyhanko-certvalidator/)

<details><summary>README extract</summary>

This library started as a fork of wbond/certvalidator with patches for pyHanko, but has since diverged considerably from its parent repository.

GitHub issues are disabled on this repository. Bug reports regarding this library should be submitted to the pyHanko issue tracker. ...

Features:
- X.509 path building
 - X.509 basic path validation
 - Signatures
 - RSA (including PSS padding), DSA, ECDSA and EdDSA algorithms. ...

Sections: certvalidator, Features, Dependencies, Test framework, Test cases

</details>

### pyaes

Pure-Python Implementation of the AES block-cipher and common modes of operation

`pip install pyaes` · installs from source (sdist only) · licence: MIT License · rank 1885 · last release 2017-09-20 · [PyPI](https://pypi.org/project/pyaes/)

<details><summary>README extract</summary>

A pure-Python implementation of the AES (FIPS-197)
block-cipher algorithm and common modes of operation (CBC, CFB, CTR, ECB,
OFB) with no dependencies beyond standard Python libraries. See README.md
for API reference and details.

</details>

### spake2

SPAKE2 password-authenticated key exchange (pure python)

`pip install spake2` · installs (wheel) · licence: MIT License · rank 2204 · last release 2024-09-25 · [PyPI](https://pypi.org/project/spake2/)

### magic-wormhole

Securely transfer data between computers

`pip install magic-wormhole` · installs (wheel) · licence: MIT · rank 2218 · last release 2026-05-05 · [PyPI](https://pypi.org/project/magic-wormhole/)

<details><summary>README extract</summary>

Get things from one computer to another, safely.

This package provides a library and a command-line tool named `wormhole`,
which makes it possible to get arbitrary-sized files and directories
(or short pieces of text) from one computer to another. ...

</details>

### pip-system-certs

Automatically configures Python to use system certificates via truststore

`pip install pip-system-certs` · installs (wheel) · licence: BSD-3-Clause · rank 2415 · last release 2025-10-16 · [PyPI](https://pypi.org/project/pip-system-certs/) · [source](https://gitlab.com/alelec/pip-system-certs)

<details><summary>README extract</summary>

This package automatically configures Python to use system certificates from the OS certificate store instead of the bundled certificates via the `truststore` library.

This allows pip and Python applications to verify TLS/SSL connections to servers whose certificates are trusted by your system. ...

Sections: pip-system-certs, Requirements, Compatibility, Known Issues, Architecture

</details>

### coincurve

Safest and fastest Python library for secp256k1 elliptic curve operations

`pip install coincurve` · installs from source (sdist only) · licence: MIT OR Apache-2.0 · rank 2562 · last release 2025-03-08 · [PyPI](https://pypi.org/project/coincurve/) · [source](https://github.com/ofek/coincurve)

<details><summary>README extract</summary>

| | |

| CI/CD | |
| Docs | |
| Package | |
| Meta | |

This library provides well-tested Python bindings for libsecp256k1, the heavily optimized C library
used by Bitcoin Core for operations on the elliptic curve secp256k1.

Feel free to read the documentation!

- Ethereum
- LBRY
- libp2p

and many more!

Sections: coincurve, Users

</details>

### safe-pysha3

SHA-3 (Keccak) for Python 3.10 - 3.15

`pip install safe-pysha3` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication; Python Software Foundation · rank 2746 · last release 2026-10-14 · [PyPI](https://pypi.org/project/safe-pysha3/) · [source](https://github.com/5afe/pysha3)

<details><summary>README extract</summary>

SHA-3 wrapper (keccak) for Python. The package is a wrapper around the
optimized Keccak Code Package, .

The module is a standalone version of my SHA-3 module from Python 3.6
(currently under development). The code in sha3module.c has been modified to
be compatible with Python 2.7 to 3.5. Python 2.6 and earlier are not
supported. ...

Example:
```python
>>> import sys
>>> import hashlib
>>> if sys.version_info < (3, 6):
...    import sha3
>>> s = hashlib.sha3_512()
>>> s.name
'sha3_512'
>>> s.digest_size
64
>>> s.update(b"data")
>>> s.hexdigest()
'ceca4daf960c2bbfb4a9edaca9b8137a801b65bae377e0f534ef9141c8684c0fedc1768d1afde9766572846c42b935f61177eaf97d355fa8dc2bca3fecfa754d'

...
```

...

</details>

### python-pkcs11

PKCS#11 support for Python

`pip install python-pkcs11` · installs (wheel) · licence: MIT · rank 2802 · last release 2026-10-20 · [PyPI](https://pypi.org/project/python-pkcs11/) · [docs](https://python-pkcs11.readthedocs.io/en/latest/) · [source](https://github.com/pyauth/python-pkcs11)

<details><summary>README extract</summary>

A high level, "more Pythonic" interface to the PKCS#11 (Cryptoki) standard
to support HSM and Smartcard devices in Python.

The interface is designed to follow the logical structure of a HSM, with
useful defaults for obscurely documented parameters. ...

Example:
```python
import pkcs11

# Initialise our PKCS#11 library
lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label='DEMO')

data = b'INPUT DATA'

# Open a session on our token
with token.open(user_pin='1234') as session:
    # Generate an AES key in this session
    key = session.generate_key(pkcs11.KeyType.AES, 256)

...
```

...

</details>

### gnupg

A Python wrapper for GnuPG

`pip install gnupg` · installs from source (sdist only) · licence: GNU General Public License v3 or later (GPLv3+) · rank 3254 · last release 2017-09-06 · [PyPI](https://pypi.org/project/gnupg/)

_README extract left out: share-alike licence._

### ocspbuilder

Creates and signs online certificate status protocol (OCSP) requests and responses for X.509 certificates

`pip install ocspbuilder` · installs (wheel) · licence: MIT License · rank 4060 · last release 2016-07-29 · [PyPI](https://pypi.org/project/ocspbuilder/)

### trustme

#1 quality TLS certs while you wait, for the discerning tester

`pip install trustme` · installs (wheel) · licence: Apache Software License; MIT License · rank 4115 · last release 2025-01-02 · [PyPI](https://pypi.org/project/trustme/)

<details><summary>README extract</summary>

You wrote a cool network client or server. It encrypts connections
using TLS. Your test
suite needs to make TLS connections to itself.

Uh oh. Your test suite *probably* doesn't have a valid TLS
certificate. Now what? ...

Example:
```python
import trustme

# ----- Creating certs -----

# Look, you just created your certificate authority!
ca = trustme.CA()

# And now you issued a cert signed by this fake CA
#
server_cert = ca.issue_cert("test-host.example.org")

# That's it!

# ----- Using your shiny new certs -----

# You can configure SSL context objects to trust this CA:
...
```

Sections: trustme: #1 quality TLS certs while you wait, Vital statistics, Cheat sheet, FAQ

</details>

### libpass

Fork of passlib, a comprehensive password hashing framework supporting over 30 schemes

`pip install libpass` · installs (wheel) · licence: BSD License · rank 4406 · last release 2026-10-17 · [PyPI](https://pypi.org/project/libpass/) · [docs](https://passlib.readthedocs.io) · [source](https://github.com/notypecheck/passlib)

<details><summary>README extract</summary>

This is a fork of

Passlib is a password hashing library for Python 3, which provides
cross-platform implementations of over 30 password hashing algorithms, as well
as a framework for managing existing password hashes. ...

Example:
```python
from passlib.context import CryptContext

context = CryptContext(
    schemes=["sha512_crypt"]
)

hash = context.hash("password")
# $6$rounds=656000$jFKvvPmUywlqjSs.$iNeK/OWVry7KThNyzR01xzqZzgk/VA75.sR4yXXblsPAoEugtdO3zn/O4VEG3Izp8l5.//lMGpuRCOqvKknHo1

# Verifying a password
is_valid = context.verify("password", hash) # True
```

Sections: Passlib, Usage

</details>

### cuid2

Next generation GUIDs. Collision-resistant ids optimized for horizontal scaling and performance.

`pip install cuid2` · installs (wheel) · licence: MIT · rank 4670 · last release 2026-11-07 · [PyPI](https://pypi.org/project/cuid2/) · [source](https://github.com/gordon-code/cuid2/)

<details><summary>README extract</summary>

CUID2 for Python 3. Next generation GUIDs. Collision-resistant ids optimized for
horizontal scaling and performance.

A port of the CUID2 reference implementation
by Parallel Drive to Python 3.

> :memo: Note: Originally taken from < before it
> was unpublished. Thank you to @joshuathompsonlindley for your original contribution! ...

Features:
For more information on the theory and usage of CUID2, see the
following.

Example:
```python
from cuid2 import create_id, is_cuid

my_cuid: str = create_id()
short_cuid: str = create_id(length=10)

print(is_cuid(my_cuid))  # True
```

Sections: cuid2, What is CUID2?, Why?, Improvements Over CUID, When to Use CUID2, Usage

</details>

### certvalidator

Validates X.509 certificates and paths

`pip install certvalidator` · installs (wheel) · licence: MIT License · rank 5600 · last release 2016-07-29 · [PyPI](https://pypi.org/project/certvalidator/)

### noiseprotocol

Implementation of Noise Protocol Framework

`pip install noiseprotocol` · installs (wheel) · licence: MIT License · rank 5708 · last release 2020-11-25 · [PyPI](https://pypi.org/project/noiseprotocol/)

### backports.ssl_match_hostname

The ssl.match_hostname() function from Python 3.5

`pip install backports.ssl_match_hostname` · installs from source (sdist only) · licence: Python Software Foundation License · rank 5718 · last release 2019-01-12 · [PyPI](https://pypi.org/project/backports.ssl_match_hostname/)

<details><summary>README extract</summary>

The Secure Sockets Layer is only actually *secure*
if you check the hostname in the certificate returned
by the server to which you are connecting,
and verify that it matches to hostname
that you are trying to reach.

But the matching logic, defined in RFC2818,
can be a bit tricky to implement on your own. ...

Example:
```python
from backports.ssl_match_hostname import match_hostname, CertificateError
[...]
sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv23,
                          cert_reqs=ssl.CERT_REQUIRED, ca_certs=...)
try:
    match_hostname(sslsock.getpeercert(), hostname)
except CertificateError, ce:
    ...
```

Sections: The ssl.match_hostname() function from Python 3.7, Requirements

</details>

### twofish

Bindings for the Twofish implementation by Niels Ferguson

`pip install twofish` · installs from source (sdist only) · licence: BSD License · rank 5859 · last release 2013-11-15 · [PyPI](https://pypi.org/project/twofish/)

<details><summary>README extract</summary>

Bindings for the Twofish implementation by Niels Ferguson libtwofish-dev.

Compatible with Python 2.6, 2.7 and 3.3.

The library performs a self-test at each import.

Sections: python-twofish, Usage, Example

</details>

### diceware

Passphrases you will remember

`pip install diceware` · installs (wheel) · licence: GNU General Public License v3 or later (GPLv3+) · rank 5909 · last release 2024-12-24 · [PyPI](https://pypi.org/project/diceware/) · [docs](https://diceware.readthedocs.io/)

_README extract left out: share-alike licence._

### ff3

Format Preserving Encryption (FPE) with FF3

`pip install ff3` · installs (wheel) · licence: Apache Software License · rank 6551 · last release 2026-01-26 · [PyPI](https://pypi.org/project/ff3/)

<details><summary>README extract</summary>

NOTE: NIST's February 2025 Draft 2 has entirely withdrawn FF3 from the NIST standard due to published vulnerabilities.

This software is provided for educational and experimental use and comes with no warranty of any kind.
It is intended for developers and researchers familiar with cryptographic standards. ...

Example:
```python
from ff3 import FF3Cipher

key = "2DE79D232DF5585D68CE47882AE256D6"
tweak = "CBD09280979564"
c = FF3Cipher(key, tweak)

plaintext = "3992520240"
ciphertext = c.encrypt(plaintext)
decrypted = c.decrypt(ciphertext)

print(f"{plaintext} -> {ciphertext} -> {decrypted}")

# format encrypted value
...
```

...

</details>

### cryptg

Cryptographic utilities for Telegram.

`pip install cryptg` · installs (wheel) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication · rank 7090 · last release 2026-11-05 · [PyPI](https://pypi.org/project/cryptg/)

<details><summary>README extract</summary>

This is a small native extension for Python 3 to help libraries that want to
work with the Telegram API, which uses the uncommon AES-IGE mode for it.

Note that while this wrapper library is licensed under CC0, the Rust dependencies
have their own license.

</details>

### M2Crypto

A Python crypto and SSL toolkit

`pip install M2Crypto` · installs from source (sdist only) · licence: BSD-2-Clause · rank 7235 · last release 2026-10-12 · [PyPI](https://pypi.org/project/M2Crypto/) · [docs](https://m2crypto.readthedocs.io/en/latest/)

<details><summary>README extract</summary>

**NOTE: This library is currently in maintenance mode (and it has been
in it since 2014 and I don’t plan to stop maintaining it anytime soon).
For new applications we recommend using a more modern alternative such
as [PyCA/cryptography]. Examples of how to migrate can be found in**
[the documentation]. ...

Sections: [M2Crypto], M2Crypto = Python + OpenSSL + SWIG

</details>

### fernet

A simple python fernet implementation

`pip install fernet` · installs from source (sdist only) · licence: MIT License · rank 7310 · last release 2016-09-18 · [PyPI](https://pypi.org/project/fernet/)

### opentimestamps

Create and verify OpenTimestamps proofs

`pip install opentimestamps` · installs (wheel) · licence: LGPL-3.0-or-later · rank 7477 · last release 2026-10-27 · [PyPI](https://pypi.org/project/opentimestamps/)

_README extract left out: share-alike licence._

### pykcs11

A Full PKCS#11 wrapper for Python

`pip install pykcs11` · installs (wheel) · licence: GPL-2.0-or-later · rank 7495 · last release 2026-10-31 · [PyPI](https://pypi.org/project/pykcs11/)

_README extract left out: share-alike licence._

### scrypt

Bindings for the scrypt key derivation function library

`pip install scrypt` · installs (wheel) · licence: 2-clause BSD · rank 8220 · last release 2025-08-05 · [PyPI](https://pypi.org/project/scrypt/)

<details><summary>README extract</summary>

This is a set of Python bindings for the scrypt key derivation
function.

Scrypt is useful when encrypting password as it is possible to specify
a *minimum* amount of time to use when encrypting and decrypting. ...

Example:
```python
>>> import scrypt
>>> data = scrypt.encrypt('a secret message', 'password', maxtime=0.1) # This will take at least 0.1 seconds
>>> data[:20]
'scrypt\x00\r\x00\x00\x00\x08\x00\x00\x00\x01RX9H'
>>> scrypt.decrypt(data, 'password', force=True) # This will also take at least 0.1 seconds
'a secret message'
...
```

Sections: Python scrypt bindings, Build From Source, 0.9.1, 0.9.0, 0.8.29, 0.8.24, 0.8.20, 0.8.19, 0.8.18, 0.8.17, 0.8.16, 0.8.15, 0.8.14, 0.8.13

</details>

### tlslite-ng

Pure python implementation of SSL and TLS.

`pip install tlslite-ng` · installs (wheel) · licence: GNU Lesser General Public License v2 (LGPLv2) · rank 8541 · last release 2025-01-22 · [PyPI](https://pypi.org/project/tlslite-ng/)

_README extract left out: share-alike licence._

### ECPy

Pure Pyhton Elliptic Curve Library

`pip install ECPy` · installs (wheel) · licence: Apache Software License · rank 8554 · last release 2020-10-26 · [PyPI](https://pypi.org/project/ECPy/)

<details><summary>README extract</summary>

ECPy (pronounced ekpy), is a pure python Elliptic Curve library
providing ECDSA, EDDSA (Ed25519), ECSchnorr, Borromean signatures as well as Point
operations.

Full html documentation is available here.

ECDSA sample

Point sample

Example:
```python
from ecpy.curves     import Curve,Point
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.ecdsa      import ECDSA

cv   = Curve.get_curve('secp256k1')
pu_key = ECPublicKey(Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
...
```

Sections: ECPy, 1.2.5, 1.2.4, 1.2.3, 1.2.2, 1.2.1, 1.2.0, 1.1.0, 1.0.1beta, 1.0.0beta, From Pypi, From Github, From tarball dist, From sources

</details>

### pyDes

Pure python implementation of DES and TRIPLE DES encryption algorithm

`pip install pyDes` · installs from source (sdist only) · licence: Public Domain · rank 8610 · last release 2016-05-06 · [PyPI](https://pypi.org/project/pyDes/)

<details><summary>README extract</summary>

This algorithm is a pure python implementation of the DES and
Triple DES algorithms. Triple DES is either DES-EDE3 with a
24 byte key, or DES-EDE2 with a 16 byte key.

</details>

### dilithium-py

A pure python implementation of ML-DSA (FIPS 204)

`pip install dilithium-py` · installs (wheel) · licence: MIT · rank 8820 · last release 2026-10-13 · [PyPI](https://pypi.org/project/dilithium-py/)

<details><summary>README extract</summary>

> [!CAUTION]
> :warning: **Under no circumstances should this be used for cryptographic
applications.** :warning:
> This is an educational resource and has not been designed to be secure
> against any form of side-channel attack. The intended use of this project
> is for learning and experimenting with ML-DSA and Dilithium ...

Example:
```python
>>> from dilithium_py.ml_dsa import ML_DSA_44
>>>
>>> # Example of signing
>>> pk, sk = ML_DSA_44.keygen()
>>> msg = b"Your message signed by ML_DSA"
>>> sig = ML_DSA_44.sign(sk, msg)
>>> assert ML_DSA_44.verify(pk, msg, sig)
>>>
>>> # Verification will fail with the wrong msg or pk
>>> assert not ML_DSA_44.verify(pk, b"", sig)
...
```

...

</details>

### sopsy

SOPS Python wrapper library

`pip install sopsy` · installs (wheel) · licence: MIT · rank 8997 · last release 2026-10-22 · [PyPI](https://pypi.org/project/sopsy/) · [source](https://git.sr.ht/~nka/sopsy)

<details><summary>README extract</summary>

SOPSy is a simple Python wrapper around SOPS.

Example:
```python
from sopsy import Sops

sops = Sops("secrets.yml")

my_secret_key = sops.get("my_secret_key")
print(f"single secret: {my_secret_key}")

secrets = sops.decrypt()
print(f"all my secrets: {secrets}")
```

Sections: SOPSy, Quickstart, API Reference

</details>

### opentimestamps-client

Command-line tool to create and verify OpenTimestamps proofs

`pip install opentimestamps-client` · installs (wheel) · licence: LGPL-3.0-or-later · rank 9135 · last release 2026-10-27 · [PyPI](https://pypi.org/project/opentimestamps-client/)

_README extract left out: share-alike licence._

### fastecdsa

Fast elliptic curve digital signatures

`pip install fastecdsa` · installs (wheel) · licence: CC0-1.0 · rank 9266 · last release 2026-09-24 · [PyPI](https://pypi.org/project/fastecdsa/) · [docs](https://fastecdsa.readthedocs.io)

<details><summary>README extract</summary>

This is a python package for doing fast elliptic curve cryptography, specifically
digital signatures.

Example:
```python
from fastecdsa.curve import Curve
curve = Curve(
    name,  # (str): The name of the curve
    p,     # (int): The value of p in the curve equation.
    a,     # (int): The value of a in the curve equation.
    b,     # (int): The value of b in the curve equation.
    q,     # (int): The order of the base point of the curve.
...
```

Sections: fastecdsa, About, ECDSA, EdDSA, Arbitrary Weierstrass Curves, Hash Functions, Performance, Publishing, Usage, Generating Keys, Signing and Verifying, Arbitrary Elliptic Curve Arithmetic

</details>

### ed25519-blake2b-fork

Ed25519 public-key signatures (BLAKE2b fork)

`pip install ed25519-blake2b-fork` · installs (wheel) · licence: MIT License · rank 9330 · last release 2026-03-02 · [PyPI](https://pypi.org/project/ed25519-blake2b-fork/)

<details><summary>README extract</summary>

This is a fork of python-ed25519-blake2b to automatically build wheels for different platforms.

This fork of python-ed25519
uses BLAKE2b instead of SHA512 as a hash algorithm. This allows the library
to create and verify signatures used in NANO. ...

Example:
```python
import ed25519_blake2b
signing_key, verifying_key = ed25519_blake2b.create_keypair()
open("my-secret-key","wb").write(signing_key.to_bytes())
vkey_hex = verifying_key.to_ascii(encoding="hex")
print "the public key is", vkey_hex
```

Sections: Dependencies, Speed and Key Sizes, Compilation, Prefixes and Encodings, Usage, API Summary

</details>

### pbkdf2

PKCS#5 v2.0 PBKDF2 Module

`pip install pbkdf2` · installs from source (sdist only) · licence: MIT License · rank 9453 · last release 2011-06-14 · [PyPI](https://pypi.org/project/pbkdf2/)

<details><summary>README extract</summary>

This module implements the password-based key derivation function, PBKDF2, specified in RSA PKCS#5 v2.0.

</details>

### py3rijndael

Rijndael algorithm library for Python3.

`pip install py3rijndael` · installs from source (sdist only) · licence: MIT License · rank 9531 · last release 2019-06-20 · [PyPI](https://pypi.org/project/py3rijndael/)

<details><summary>README extract</summary>

Rijndael algorithm library for Python3.

Rijndael is the key algorithm of AES,
and there is some of implementations already exist:

- pycrypto: Very old and not written in python.
- pycryptodome: In road of `pycrypto` but alive.

 Tested and works fine. but, not in Python 3, also depend on `pycrypto`.

 Tested and works fine. ...

Sections: py3rijndael, Usage

</details>

### pqcrypto

Python bindings for post-quantum cryptography — ML-KEM, ML-DSA, SLH-DSA, Classic McEliece, HQC, and SNTRUP

`pip install pqcrypto` · installs (wheel) · licence: Apache-2.0 · rank 9658 · last release 2026-08-15 · [PyPI](https://pypi.org/project/pqcrypto/) · [docs](https://github.com/backbone-hq/pqcrypto) · [source](https://github.com/backbone-hq/pqcrypto)

<details><summary>README extract</summary>

Python bindings for post-quantum cryptography. Wraps well-tested Rust
implementations of NIST-standardized and candidate KEM and signature schemes
via PyO3/maturin. All variants live in a single compiled wheel.

Example:
```python
from pqcrypto.kem.ml_kem_512 import keygen, encaps, decaps
from pqcrypto.kem.ml_kem_512 import PublicKey, SecretKey

pk, sk = keygen()
ct, ss = encaps(pk)
assert decaps(sk, ct) == ss

pk_obj = PublicKey(pk)
sk_obj = SecretKey(sk)
ct2, ss2 = pk_obj.encaps()
assert ss2 == sk_obj.decaps(ct2)
```

Sections: Quick Start, KEM — Key Encapsulation, Signatures, Size constants, Algorithms, Key Encapsulation

</details>

### libnacl

Python bindings for libsodium based on ctypes

`pip install libnacl` · installs (wheel) · licence: Apache Software License · rank 9668 · last release 2023-08-06 · [PyPI](https://pypi.org/project/libnacl/) · [docs](https://libnacl.readthedocs.org) · [source](https://github.com/saltstack/libnacl)

<details><summary>README extract</summary>

This library is used to gain direct access to the functions exposed by
Daniel J. Bernstein's nacl library via libsodium. It has
been constructed to maintain extensive documentation on how to use nacl
as well as being completely portable. ...

Features:
There are a number of libraries out there binding to libsodium, so why make
libnacl?

1. libnacl does not have any non-python hard deps outside of libsodium
2. libnacl does not need to be compiled
3. libnacl is easy to package and very portable
4. ...

Sections: Python libnacl, Higher Level Classes, Why libnacl, Linux distributions

</details>

### pyrage-stubs

A PEP 561 stub package for pyrage's types

`pip install pyrage-stubs` · installs (wheel) · licence: MIT · rank 10502 · last release 2026-08-23 · [PyPI](https://pypi.org/project/pyrage-stubs/) · [source](https://github.com/woodruffw/pyrage/tree/main/pyrage-stubs)

<details><summary>README extract</summary>

This is a PEP 561-compatible stubs
package for `pyrage`.

</details>

### bech32m

Encoding/decoding Bech32 and Bech32m

`pip install bech32m` · installs (wheel) · licence: MIT License · rank 10623 · last release 2023-06-14 · [PyPI](https://pypi.org/project/bech32m/) · [source](https://github.com/ods/bech32m)

### eciespy

Elliptic Curve Integrated Encryption Scheme for secp256k1/curve25519 in Python

`pip install eciespy` · installs (wheel) · licence: MIT · rank 10706 · last release 2026-10-21 · [PyPI](https://pypi.org/project/eciespy/) · [source](https://github.com/ecies/py)

<details><summary>README extract</summary>

Elliptic Curve Integrated Encryption Scheme for secp256k1/curve25519 in Python.

Other language versions (curve25519 is not supported in some versions):

- TypeScript
- Rust
- Golang
- WASM
- Java
- Dart
- Ruby

You can also check a web backend demo.

Example:
```python
>>> from ecies.keys import PrivateKey
>>> from ecies import encrypt, decrypt
>>> data = 'hello world🌍'.encode()
>>> sk = PrivateKey('secp256k1')
>>> sk_bytes = sk.secret  # bytes
>>> pk_bytes = sk.public_key.to_bytes(True)  # bytes
>>> decrypt(sk_bytes, encrypt(pk_bytes, data)).decode()
'hello world🌍'
>>> sk_hex = sk.to_hex() # hex str
...
```

...

</details>

### clvm

[Contract Language | Chialisp] Virtual Machine

`pip install clvm` · installs (wheel) · licence: Apache Software License · rank 10980 · last release 2025-09-17 · [PyPI](https://pypi.org/project/clvm/) · [source](https://github.com/Chia-Network/clvm)

<details><summary>README extract</summary>

This is the in-development version of a LISP-like language for encumbering and releasing funds with smart-contract capabilities.

See docs/clvm.org or for more info.

</details>

### python3-dtls

Python Datagram Transport Layer Security

`pip install python3-dtls` · installs (wheel) · licence: Apache Software License · rank 11008 · last release 2020-11-06 · [PyPI](https://pypi.org/project/python3-dtls/)

<details><summary>README extract</summary>

Sections: Design Goals, Distributions, Interfaces, Connection Handling, Demultiplexing, Shutdown and Unwrapping, Framework Compatibility, Logging

</details>

### clvm-tools

CLVM compiler.

`pip install clvm-tools` · installs (wheel) · licence: Apache Software License · rank 11025 · last release 2024-10-23 · [PyPI](https://pypi.org/project/clvm-tools/) · [source](https://github.com/Chia-Network/clvm_tools)

<details><summary>README extract</summary>

This is the in-development version of `clvm_tools` for clvm, which implements, a LISP-like language for encumbering and releasing funds with smart-contract capabilities.

Set up your virtual environments

 $ python3 -m venv venv
 $ . ./venv/bin/activate (windows: venv\Scripts\activate.bat)
 $ pip install -e . ...

Sections: Introduction, Set up, Quick examples, The Compiler, Basic example, Auto-quoting of literals, Known operators, @, (if), (qq) and (unquote), Macros, A Simple Example, Inline functions, A More Complex Example

</details>

### bip32

Minimalistic implementation of BIP32 (Bitcoin HD wallets)

`pip install bip32` · installs (wheel) · licence: BSD-3-Clause · rank 11204 · last release 2025-11-13 · [PyPI](https://pypi.org/project/bip32/) · [source](https://github.com/darosior/python-bip32)

<details><summary>README extract</summary>

A minimalistic implementation of BIP 32.

Example:
```python
>>> from bip32 import BIP32, HARDENED_INDEX
>>> bip32 = BIP32.from_seed(bytes.fromhex("01"))
# Specify the derivation path as a list ...
>>> bip32.get_xpriv_from_path([1, HARDENED_INDEX, 9998])
'xprv9y4sBgCuub5x2DtbdNBDDCZ3btybk8YZZaTvzV5rmYd3PbU63XLo2QEj6cUt4JAqpF8gJiRKFUW8Vm7thPkccW2DpUvBxASycypEHxmZzts'
# ... Or in usual m/the/path/
...
```

Sections: python-bip32, Usage, Dependencies, Running the test suite, Interface, BIP32, from_seed(seed), from_xpriv(xpriv), from_xpub(xpub), get_extended_privkey_from_path(path), get_privkey_from_path(path), get_extended_pubkey_from_path(path), get_pubkey_from_path(path), get_xpriv_from_path(path)

</details>

### django-secured-fields

Django encrypted fields with search enabled.

`pip install django-secured-fields` · installs (wheel) · licence: MIT · rank 12268 · last release 2026-10-03 · [PyPI](https://pypi.org/project/django-secured-fields/) · [source](https://github.com/C0D1UM/django-secured-fields)

<details><summary>README extract</summary>

Django encrypted fields with search enabled.

- Python 3.10+
- Django 4.2+
- PostgreSQL, MySQL or SQLite

Features:
- Automatically encrypt/decrypt field value using cryptography's Fernet
- Built-in search lookup on the encrypted fields from hashlib's _SHA-256_ hash value. `in` and `isnull` lookup also supported. ...

Example:
```python
# models.py
import secured_fields

phone_number = secured_fields.EncryptedCharField(max_length=10)
```

Sections: Django Secured Fields, Requirements, Features, Setup, Usage, Simple Usage, Enable Searching, Settings, APIs, Field Arguments, Changing `searchable` on a field with existing records, Encryption, Rotate Keys, `EncryptedMixin`

</details>

### pysha3

SHA-3 (Keccak) for Python 2.7 - 3.5

`pip install pysha3` · installs from source (sdist only) · licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication; Python Software Foundation · rank 12865 · last release 2017-07-18 · [PyPI](https://pypi.org/project/pysha3/)

<details><summary>README extract</summary>

SHA-3 wrapper (keccak) for Python. The package is a wrapper around the
optimized Keccak Code Package, .

The module is a standalone version of my SHA-3 module from Python 3.6
(currently under development). The code in sha3module.c has been modified to
be compatible with Python 2.7 to 3.5. Python 2.6 and earlier are not
supported. ...

Example:
```python
>>> import sys
>>> import hashlib
>>> if sys.version_info < (3, 6):
...    import sha3
>>> s = hashlib.sha3_512()
>>> s.name
'sha3_512'
>>> s.digest_size
64
>>> s.update(b"data")
>>> s.hexdigest()
'ceca4daf960c2bbfb4a9edaca9b8137a801b65bae377e0f534ef9141c8684c0fedc1768d1afde9766572846c42b935f61177eaf97d355fa8dc2bca3fecfa754d'

...
```

...

</details>

### pyscrypt

Pure-Python Implementation of the scrypt password-based key derivation function and scrypt file format library

`pip install pyscrypt` · installs from source (sdist only) · licence: MIT License · rank 12900 · last release 2015-02-03 · [PyPI](https://pypi.org/project/pyscrypt/)

<details><summary>README extract</summary>

A very simple, pure-Python implementation of the scrypt
password-based key derivation function and scrypt file format library with no
dependencies beyond standard Python libraries. See README.md for API
reference and details.

</details>

### arc4

A small and insanely fast ARCFOUR (RC4) cipher implementation of Python

`pip install arc4` · installs from source (sdist only) · licence: MIT License · rank 13084 · last release 2026-04-05 · [PyPI](https://pypi.org/project/arc4/)

<details><summary>README extract</summary>

A small and insanely fast ARCFOUR (RC4) cipher implementation of Python.

* Strongly focused on performance; entire source code is written in C.
* Thread-safety; you can improve further performance with multi-threading.
* Easily installable; single file with no dependency, pre-built wheels provided. ...

Example:
```python
>>> from arc4 import ARC4
>>> arc4 = ARC4(b'key')
>>> cipher = arc4.encrypt(b'some plain text to encrypt')
```

Sections: arc4, Benchmark, Usage, Documents

</details>

### keeper-mlkem

Fast ML-KEM implementation with C extensions

`pip install keeper-mlkem` · installs from source (sdist only) · licence: MIT · rank 13501 · last release 2025-11-26 · [PyPI](https://pypi.org/project/keeper-mlkem/) · [docs](https://github.com/Keeper-Security/commander-qrc/blob/master/README.md) · [source](https://github.com/Keeper-Security/commander-qrc)

<details><summary>README extract</summary>

Production-ready post-quantum cryptography library implementing ML-KEM (FIPS 203) for Keeper Commander applications.

Features:
This package provides a lightweight, optimized implementation of the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) as standardized in FIPS 203. ...

Example:
```python
from mlkem import ML_KEM, MLKEM_768_PARAMETERS

# Initialize ML-KEM-768
ml_kem = ML_KEM(MLKEM_768_PARAMETERS)

# Generate key pair
encapsulation_key, decapsulation_key = ml_kem.key_gen()

# Encapsulate (create shared secret)
shared_secret, ciphertext = ml_kem.encaps(encapsulation_key)

# Decapsulate (recover shared secret)
...
```

Sections: Keeper ML-KEM, Overview, Usage, Basic Example, Technical Specifications, System Requirements, About ML-KEM

</details>

### minisignxml

Minimal XML signature and verification, intended for use with SAML2

`pip install minisignxml` · installs (wheel) · licence: Apache Software License · rank 14495 · last release 2026-01-22 · [PyPI](https://pypi.org/project/minisignxml/) · [source](https://github.com/HENNGE/minisignxml)

<details><summary>README extract</summary>

Python library to sign and verify XML documents.

This library, *on purpose*, only supports a limited part of the xmldsig specification. It is mainly aimed at allowing SAML documents to be signed and verified.

Supported features:

* Simple API. ...

Example:
```python
def sign(
    *,
    element: Element,
    private_key: RSAPrivateKey,
    certificate: Certificate,
    config: SigningConfig = SigningConfig.default(),
    index: int = 0,
    attribute: str = "ID"
) -> bytes:
```

Sections: minisignxml, API, Signing, SigningConfig, Verifying, VerifyConfig

</details>

### borgbackup

Deduplicated, encrypted, authenticated and compressed backups

`pip install borgbackup` · installs from source (sdist only) · licence: BSD-3-Clause · rank 14560 · last release 2026-07-18 · [PyPI](https://pypi.org/project/borgbackup/) · [docs](https://borgbackup.readthedocs.io/) · [source](https://github.com/borgbackup/borg)

<details><summary>README extract</summary>

What is BorgBackup?

BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored. ...

</details>

### fastfpe

Fast Format Preserving Encryption (FPE) implementation in Rust

`pip install fastfpe` · installs (wheel) · licence: MIT · rank 14618 · last release 2026-02-05 · [PyPI](https://pypi.org/project/fastfpe/) · [docs](https://github.com/pjwerneck/fastfpe#readme) · [source](https://github.com/pjwerneck/fastfpe)

<details><summary>README extract</summary>

Fast Format Preserving Encryption (FPE) implementation in Rust with Python
bindings.

Format-preserving encryption (FPE) is a cryptographic method that encrypts data
while preserving its format. ...

Features:
- FF1 and FF3-1 Format Preserving Encryption algorithms
- Fast Rust implementation with Python bindings
- Support for custom alphabets
- Thread-safe ...

Example:
```python
>>> from fastfpe import ff3_1
>>>
>>> key = "3eaa133d22a7ee2432fb8ecfde1e97d9106dcf26b9edaa52b3ed4acd9a9b8445"
>>> tweak = "5be49f26c1dbb7"  # 7 bytes (14 hex chars)
>>> alphabet = "abcdef0123456789"
>>> plaintext = "024587931578"
>>>
>>> ciphertext = ff3_1.encrypt(key, tweak, alphabet, plaintext)
>>> ciphertext
'd756b8704a2d'
...
```

Sections: fastfpe, Features, Usage (FF3-1), Usage (FF1), Performance

</details>

### yubikey-manager

Library and CLI for managing your YubiKey configuration.

`pip install yubikey-manager` · installs (wheel) · licence: not stated · rank 14632 · last release 2026-06-30 · [PyPI](https://pypi.org/project/yubikey-manager/)

<details><summary>README extract</summary>

== YubiKey Manager CLI
image: package build", link="
image: build", link="
image: build", link="
image: build", link="

Python 3.10 (or later) library and command line tool for configuring a YubiKey.
If you're looking for a graphical application, check out Authenticator]. ...

</details>

## Also in this topic

- [Authlib](internet-www-http.md#authlib) - The ultimate Python library in building OAuth and OpenID Connect servers and clients.
- [joserfc](security.md#joserfc) - The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT
- [paramiko](internet.md#paramiko) - SSH2 protocol library
- [argon2-cffi-bindings](security.md#argon2-cffi-bindings) - Low-level CFFI bindings for Argon2
- [id](security.md#id) - A tool for generating OIDC identities
- [blake3](security.md#blake3) - Python bindings for the Rust blake3 crate
- [asyncssh](internet.md#asyncssh) - AsyncSSH: Asynchronous SSHv2 client and server library
- [rfc8785](file-formats-json.md#rfc8785) - A pure-Python implementation of RFC 8785 (JSON Canonicalization Scheme)
- [PGPy](security.md#pgpy) - Pretty Good Privacy for Python
- [pwdlib](security.md#pwdlib) - Modern password hashing for Python
- [fido2](internet.md#fido2) - FIDO2/WebAuthn library for implementing clients and servers.
- [aws-encryption-sdk](security.md#aws-encryption-sdk) - AWS Encryption SDK implementation for Python
- [sigstore](security.md#sigstore) - A tool for signing Python package distributions
- [pylibsrtp](communications-telephony.md#pylibsrtp) - Python wrapper around the libsrtp library
- [crypto](security.md#crypto) - Simple symmetric GPG file encryption and decryption
- [pymacaroons](internet-www-http.md#pymacaroons) - Macaroon library for Python
- [TgCrypto](communications.md#tgcrypto) - Fast and Portable Cryptography Extension Library for Pyrogram
- [django-cryptography-django5](internet-www-http.md#django-cryptography-django5) - Easily encrypt data in Django - Fork for Django 5 support
- [pysodium](security.md#pysodium) - python libsodium wrapper
- [signify](scientific-engineering-information-analysis.md#signify) - Module to generate and verify PE signatures
- [pyAesCrypt](security.md#pyaescrypt) - Encrypt and decrypt files and streams in AES Crypt format (version 2)
- [PGPy13](security.md#pgpy13) - Pretty Good Privacy for Python (temporary fork for py3.13 compatability)
- [SLH-DSA](security.md#slh-dsa) - Pure Python implementation of the SLH-DSA algorithm (based on FIPS 205).
- [galois](scientific-engineering-mathematics.md#galois) - A performant NumPy extension for Galois fields and their applications
- [dynamodb-encryption-sdk](security.md#dynamodb-encryption-sdk) - DynamoDB Encryption Client for Python
- [base58check](internet-www-http.md#base58check) - Base58check encoding and decoding of binary data
- [django-cryptography-5](internet-www-http.md#django-cryptography-5) - Easily encrypt data in Django
- [django-cryptography](internet-www-http-2.md#django-cryptography) - Easily encrypt data in Django
- [aia](internet-www-http-2.md#aia) - AIA chasing through OpenSSL for TLS certificate chain building and verifying
- [django-pgcrypto-fields](database.md#django-pgcrypto-fields) - Encrypted fields for Django dealing with pgcrypto postgres extension.
- [aws-encryption-sdk-cli](security.md#aws-encryption-sdk-cli) - This command line tool can be used to encrypt and decrypt files and directories using the AWS Encryption SDK.
- [bitcoinlib](office-business-financial.md#bitcoinlib) - Bitcoin cryptocurrency Library
- [pywidevine](multimedia-video.md#pywidevine) - Widevine CDM (Content Decryption Module) implementation in Python.
- [btclib-secp256k1](scientific-engineering-2.md#btclib-secp256k1) - Simple python bindings to libsecp256k1
- [endesive](communications-email.md#endesive) - Digital signatures for PDF, S/MIME, XML (XAdES), and CMS in Python.
- [cachekit](database-database-engines-servers.md#cachekit) - Backend-agnostic caching for Python — intent-based decorators with circuit breaker, distributed locking, Prometheus metrics, and optional zero-knowledge AES-256-GCM encryption, on a Rust-powered core. Zero-config L1 in-memory; scales to Redis, Memcached, File, or CachekitIO.
