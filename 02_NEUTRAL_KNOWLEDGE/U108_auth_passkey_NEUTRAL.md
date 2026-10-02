# U108 — auth_passkey: WebAuthn Registration/Authentication Flow
**Unit**: U108 | **Module**: auth_passkey | **GAP**: GAP-020
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Module Overview

`auth_passkey` auto-installs with Odoo 19 (depends on `base_setup` and `web`). It implements the WebAuthn specification using a vendored Python library bundled at `addons/auth_passkey/_vendor/webauthn/`. The manifest explicitly states that passkey authentication unconditionally skips MFA.

## Controller Layer

Two public HTTP routes are exposed:

- `/auth/passkey/start-auth` (jsonrpc, auth=public): Initiates a WebAuthn authentication challenge. No session is required to call this endpoint.
- `/.well-known/assetlinks.json` (http, auth=public): Serves Android Digital Asset Links JSON for the `com.odoo.mobile` package, enabling passkey credential sharing between the Odoo web and Android mobile app.

At module load time, `'webauthn_response'` is appended to the global `CREDENTIAL_PARAMS` list from the web home controller, making it a recognized POST parameter on the standard login endpoint.

## Credential Model

`auth.passkey.key` stores one WebAuthn credential per record (ordered by `id desc`). Fields:

- `name`: visible to the owner — the human-readable label
- `credential_identifier`: base64url-encoded WebAuthn credential ID — restricted to `base.group_system`
- `public_key`: stored as base64 URL-safe encoded bytes — restricted to `base.group_system`; both reads and writes bypass the ORM via raw SQL to circumvent the group restriction at authentication time
- `sign_count`: anti-replay counter — restricted to `base.group_system`; updated after every successful authentication
- `create_uid`: the owning user

A DB-level UNIQUE constraint enforces one record per `credential_identifier` across the system.

## Challenge Lifecycle

Challenges are stored in `request.session['webauthn_challenge']` during `_start_auth()` / `_start_registration()`. The helper `_get_session_challenge()` pops the value (single-use, consumed on read); a missing challenge raises `AccessDenied` immediately.

Both authentication and registration verification enforce:
- `rp_id` derived from `get_base_url()` host
- `expected_origins` = web origin + Android APK key hashes for `com.odoo.mobile`
- `require_user_verification=True`

Registration additionally enforces `resident_key=REQUIRED`.

## Registration Flow

1. User triggers `action_create_passkey` on `res.users` — gated by `@check_identity` (password re-confirmation)
2. Server calls `_start_registration()`, stores challenge, returns options to browser
3. Browser completes WebAuthn registration and returns credential
4. Transient wizard `auth.passkey.key.create.make_key()` — also gated by `@check_identity` — calls `_verify_registration_options()`, creates the passkey record via ORM, then writes the public key via raw SQL UPDATE
5. Session token is immediately recomputed after creation

## Authentication Flow

1. Browser requests challenge via `/auth/passkey/start-auth`
2. Browser completes WebAuthn assertion and submits `webauthn_response` as a login credential
3. `res.users._login()` intercepts `credential['type'] == 'webauthn'`, looks up the login via SQL JOIN on `credential_identifier`
4. `res.users._check_credentials()` intercepts, searches passkey with `sudo()`, calls `_verify_auth()` with stored public key and sign count
5. On success: `sign_count` updated, returns `{'auth_method': 'passkey', 'mfa': 'skip'}`

## MFA Bypass

The `mfa='skip'` return value from `_check_credentials` is the authoritative mechanism for MFA bypass. No additional configuration is required — any successful passkey login bypasses MFA unconditionally.

## Session Token Invalidation

`auth_passkey_key_ids` is included in session token computation fields. The SQL query aggregates all passkey IDs for the user via LEFT JOIN + ARRAY_AGG. Any change to the passkey set (creation or deletion) triggers immediate session token recomputation, invalidating all existing sessions.

## Security Rules

- **Internal/portal users**: Row-level rule restricts access to own passkeys only (`create_uid = user.id`)
- **ERP Manager**: Unrestricted read + unlink on all passkey records; cannot write or create
- **ACL**: Internal users have read+write but not create/unlink on `auth.passkey.key`; creation goes through the transient `auth.passkey.key.create` model which has full CRUD

## Mobile Support

APK key hashes for `com.odoo.mobile` are computed at module load from hard-coded SHA-256 certificate fingerprints and formatted as `android:apk-key-hash:<base64url>` strings. These are appended to `expected_origins` during both authentication and registration verification.

## Vendored Library

WebAuthn operations use a vendored copy of the Python `webauthn` library bundled at `addons/auth_passkey/_vendor/webauthn/`, not a pip dependency. Functions used: `generate_authentication_options`, `verify_authentication_response`, `generate_registration_options`, `verify_registration_response`, `options_to_json`, `base64url_to_bytes`, `bytes_to_base64url`.
