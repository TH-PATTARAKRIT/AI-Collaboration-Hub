# U108 — auth_passkey Neutral Knowledge Layer (GAP-020 P1)

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

## Purpose

This document captures the neutral, human-readable knowledge derived via the Passkeys module source evidence. It is free of technical identifiers, code tokens, and file system references. It can be shared with non-technical stakeholders, regulatory reviewers, or used as input for gap analysis without exposing implementation specifics.

---

## NK-001 — Module Identity and Activation

The Passkeys module provides WebAuthn-based passwordless authentication for the Odoo platform. It activates automatically whenever its prerequisite platform modules are installed, requiring no manual administrator action. The module is licensed under a weak copyleft open-source licence and authored by the platform vendor.

---

## NK-002 — Passkey Record Schema

Each registered passkey is stored as a named record belonging to one user. The record holds:

- A human-readable name chosen by the user at registration time
- A unique credential identifier assigned by the authenticator hardware or software
- A public key value used for cryptographic signature verification
- A signature counter used to detect cloned authenticators or replay attacks
- A reference to the owning user record

The credential identifier, public key, and signature counter are restricted fields, meaning only administrators with the highest privilege level can read them through the normal application interface. A database-level uniqueness constraint prevents duplicate credential identifiers.

The user model carries a one-to-many relation pointing at all passkey records that user owns, using the record creator as the linking column.

---

## NK-003 — Safe Schema Migration

During module initialization, the code inspects the database to check whether the public key storage column already exists before attempting to add it. This guards against failure when upgrading a system that already has the column via a prior installation.

---

## NK-004 — Challenge Generation and Session Binding

All WebAuthn challenges are generated as 64 random bytes using a cryptographically secure random number generator. This size exceeds the minimum 16 bytes required by the WebAuthn specification and is sufficient to prevent guessing or brute-force attacks.

Both the registration and authentication flows store their challenge in the server-side session immediately after generating it. The challenge is consumed with a destructive read (pop), ensuring it is single-use: once the server reads the challenge for verification, it is removed and cannot be used again.

User verification (biometric or PIN confirmation at the authenticator) is set to required in both flows, meaning a passkey without local verification cannot be used on this platform.

---

## NK-005 — Registration Verification

When the browser returns the authenticator's registration response, the server:

1. Decodes the session challenge and removes it
2. Constructs a list of allowed origins (the server's own web origin plus Android app origins)
3. Passes the browser's credential, the challenge, and the origin list to the WebAuthn library for verification
4. On success, extracts the raw credential identifier and public key bytes

The platform requests no attestation statement at all, accepting any authenticator that meets the resident-key and user-verification requirements regardless of manufacturer.

Nine public key algorithm types are supported by default, with ECDSA using SHA-256 as the preferred algorithm.

---

## NK-006 — Passkey Record Persistence

Creating a passkey record requires the caller to pass identity verification first. The wizard model then:

1. Calls the registration verification function to extract the credential identifier and public key
2. Writes the new passkey through the user's relationship list rather than directly to it, ensuring session invalidation logic fires on the parent user record
3. Stores the public key bytes using a direct parameterized database statement, bypassing the access-group-restricted field setter
4. Recomputes and replaces the current session token so the new passkey is immediately reflected in the session state

Passkey creation is logged with the creating user's name, record identifier, and originating IP address.

---

## NK-007 — Authentication Challenge Endpoint

The endpoint that generates authentication options is publicly accessible — no existing session or login is required to call it. This is intentional: the browser needs challenge options before it can present a passkey prompt to the user. The challenge is stored in the session and consumed once during subsequent verification.

---

## NK-008 — Authentication Verification

When the browser presents an authentication response:

1. The server runs a database lookup to resolve which user account owns the presented credential identifier
2. If no matching record is found, access is denied with a clear error message
3. The passkey record for that user and credential identifier is loaded
4. The signature is verified against the stored public key using the WebAuthn library
5. On success the system returns an authentication result that explicitly marks multi-factor authentication as skipped, because passkey authentication is considered sufficient on its own
6. The signature counter in the passkey record is advanced to the new value returned by the verifier

---

## NK-009 — Cryptographic Security Checks in the Verification Library

The bundled WebAuthn verification library enforces two critical security properties:

First, if user verification was required, the authenticator-data flags must confirm that the authenticator locally verified the user. A response without this flag causes verification to fail.

Second, the signature counter must have increased since the last successful authentication when either the stored or presented counter is nonzero. A counter that has not increased is treated as evidence of a cloned authenticator or replay attempt, causing verification to fail.

---

## NK-010 — Access Control Rules

Three layered access controls govern passkey records:

1. A record-level rule restricts internal users and portal users to records they themselves created; cross-user passkey access is blocked.

2. A separate record-level rule grants the platform manager role the ability to read and remove any user's passkeys (for administrative use), but explicitly blocks that role at creating or modifying passkey records.

3. A model-level access table grants internal users and portal users read and write rights at the model level, while the record rule above narrows what they can actually reach. Creation and removal rights at the model level are granted only through specific workflows (creation wizard and user-relation removal).

---

## NK-011 — Session Token Invalidation on Passkey Changes

The session token computation is extended to incorporate the list of passkeys owned by each user. This means that registering a new passkey, renaming one, or removing one automatically invalidates all active sessions for that user. A database query combining the user table with the passkey table is embedded in the session token hash computation.

---

## NK-012 — Identity Check Integration

The platform's identity re-verification dialog is extended to offer passkey as a choosable authentication method. When the current user has at least one registered passkey, passkey becomes the default method in the dialog rather than password. If passkey verification fails, the error is presented as a user-friendly message rather than a raw access denial.

A fallback action allows the user to switch to password authentication within the same dialog session.

---

## NK-013 — Passkey Removal Security

Removing a passkey requires identity re-verification by the caller. Additionally, at runtime the system checks that the passkey being removed belongs to the user making the request. Attempts to remove another user's passkey are silently blocked and logged as a security warning.

Removal is performed through the user's relationship list rather than directly on the record model, ensuring session token invalidation fires. After removal the current session token is recomputed.

---

## NK-014 — Android Mobile App Integration

The module includes support for the Odoo mobile application on Android. A specific Android app package identifier and its certificate fingerprint are hardcoded in the module. A publicly accessible endpoint at the industry-standard asset-links path serves a JSON document linking the web domain to the Android application, enabling the Android operating system to offer passkeys registered on the web app when the user opens the mobile app.

---

*Generated: 2026-10-02 | Agent: Claude Sonnet 4.6 | DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION*
