# Communications / FIDO

[Index](README.md) · 1 packages in this topic, by downloads.

### django-otp-webauthn

FIDO2 WebAuthn support for django-otp: lets your users authenticate with Passkeys

`pip install django-otp-webauthn` · installs (wheel) · licence: BSD-3-Clause · rank 12812 · last release 2026-09-02 · [PyPI](https://pypi.org/project/django-otp-webauthn/) · [docs](https://django-otp-webauthn.readthedocs.io/en/latest/) · [source](https://github.com/Stormbase/django-otp-webauthn)

<details><summary>README extract</summary>

This package provides an implementation of WebAuthn Passkeys for Django. It is written as a plugin for the Django OTP framework for multi-factor authentication. Under the hood, this package uses py_webauth to handle all cryptographic operations.

> [!IMPORTANT]
> As of May 2025, I now consider this package stable enough for production use. ...

Features:
- Passkeys as a second factor. Lets users just click yes on the browser prompt to verify their identity after they have entered their password.
- Passwordless login with Passkeys (optional). ...

Example:
```python
# urls.py

from django.urls import include, path

urlpatterns = [
    ...
    path("webauthn/", include("django_otp_webauthn.urls", namespace="otp_webauthn")),
    ...
]
```

...

</details>

