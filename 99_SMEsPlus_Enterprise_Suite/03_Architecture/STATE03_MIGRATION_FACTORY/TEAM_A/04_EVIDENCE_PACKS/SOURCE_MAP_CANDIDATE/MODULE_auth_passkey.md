# Source Map (candidate) — `auth_passkey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_passkey` |
| Display name | Passkeys |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7f26ee45e2bfe370` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_passkey/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `web`
- Direct dependents in 300-module list (2): `auth_passkey_portal`, `auth_timeout`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Log in with a Passkey
- Inventory of user-facing artifacts (counts): menu items 0, views 6, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `auth.passkey.key` (Passkey); `auth.passkey.key.create` (Create a Passkey)
- Objects extended from other modules (2): `res.users.identitycheck`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users.identitycheck`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 3 (of which company-scoped by text 0); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 42 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — auth_passkey
Source revision: 19.0.post20260921 | Module: "Passkeys" (auth_passkey/__manifest__.py:2), version 1.1 (:3), category Hidden/Tools (:12), LGPL-3 (:38). Basis: static reading of models, controller, security, views, vendored library notes and tests (not run).

## A. Capabilities and optionality
- A1. Passwordless login and identity re-check using passkeys (WebAuthn standard). Stated: a passkey login does not require a second factor. auth_passkey/__manifest__.py:4-10
- A2. Login page gets a "Use a Passkey" entry next to social-login buttons and a hidden field carrying the passkey response. auth_passkey/views/auth_passkey_login_templates.xml:3-16
- A3. Users register passkeys themselves (button "Add Passkey" on the user form for the own record and on the preferences form); each passkey has a name and can be renamed or deleted. auth_passkey/views/res_users_views.xml:9-22,33-46; auth_passkey/models/auth_passkey_key.py:126-157
- A4. Passkeys can also stand in for the password when the system asks for an identity re-check before sensitive actions (default method becomes passkey if the user owns one; user can switch to password). auth_passkey/models/res_users_identitycheck.py:8-15,17-41
- A5. Registration and login both require user verification (PIN/biometric) by the authenticator; the server re-verifies it. auth_passkey/models/auth_passkey_key.py:74,90,103-104,119 (TEST) auth_passkey/tests/test_passkey_demo.py:397-402
- A6. Built-in support for the official Odoo Android app: the origin list includes the app's signing-key hash and the site publishes a digital-asset-links file. auth_passkey/mobile_utils.py:5-36; auth_passkey/controllers/main.py:16-20 (TEST) auth_passkey/tests/test_passkey_demo.py:487-506
- A7. Optionality: auto_install = True, depends on base_setup and web, so present by default; no settings switch to disable it and no company-level policy in this module. auth_passkey/__manifest__.py:13-14
- A8. The WebAuthn library is vendored (v2.0.0 with modified imports) because it could not be added as a dependency. auth_passkey/_vendor/webauthn/INFO:1-6

## B. Objects and relationships
- B1. auth.passkey.key: one credential per row; name, credential identifier (unique across the system), public key, signature counter; owner is the creating user (create_uid), newest first. Identifier/public key/counter are visible only to Settings administrators. auth_passkey/models/auth_passkey_key.py:21-35
- B2. auth.passkey.key.create (transient): wizard collecting the passkey name and the registration response from the browser. auth_passkey/models/auth_passkey_key.py:160-194
- B3. res.users gains the list of the user's passkeys. auth_passkey/models/res_users.py:14
- B4. Identity-check wizard (owner: base) gains method "Passkey". auth_passkey/models/res_users_identitycheck.py:5-8
- B5. Lifecycle: register (identity re-check -> browser creates credential -> server verifies challenge/origin -> row created, session token refreshed) -> used at login (counter updated) -> renamed/deleted by owner or deleted by administrator. auth_passkey/models/res_users.py:20-32; auth_passkey/models/auth_passkey_key.py:166-194,126-143; auth_passkey/models/res_users.py:49-71

## C. Validations, security, audit
- C1. Login flow: passkey id in the response is matched to a login; unknown passkey is refused ("Unknown passkey"); signature verified against session challenge (single use), site origin and relying-party id; counter stored. auth_passkey/models/res_users.py:34-71; auth_passkey/models/auth_passkey_key.py:62-92
- C2. Successful passkey authentication returns "mfa: skip", i.e. bypasses the second step of auth_totp. auth_passkey/models/res_users.py:67-71; base/models/res_users.py:337-341; odoo/http.py:1258
- C3. Adding or deleting a passkey is part of the session-token fields, so other sessions of that user are invalidated while the acting session is refreshed. auth_passkey/models/res_users.py:75-85; auth_passkey/models/auth_passkey_key.py:130-135,192-193
- C4. Registration, deletion and denied deletion attempts are written to the server log with user, id and IP (no audit table). auth_passkey/models/auth_passkey_key.py:42-50,136-143,185-191
- C5. Creating and deleting via the UI requires a recent identity check (password or passkey within 10 minutes) and HTTP context. auth_passkey/models/auth_passkey_key.py:126,166; auth_passkey/models/res_users.py:20; base/models/res_users.py:87-108
- C6. Access: internal and portal users read/write their own passkeys only (rule on creator), no create/delete on the model itself (creation goes through the wizard/user record); the Access Rights administrator group (base.group_erp_manager) can view and delete anyone's, not edit or create. auth_passkey/security/ir.model.access.csv:2-6; auth_passkey/security/security.xml:3-32
- C7. Only the owner can delete via the action; an attempt on another user's passkey is logged and ignored. auth_passkey/models/auth_passkey_key.py:129-143
- C8. Public endpoint to start a login challenge; the challenge is kept in the session. auth_passkey/controllers/main.py:11-14; auth_passkey/models/auth_passkey_key.py:69-77
- C9. No company scoping: passkeys belong to the user. (No company field or company rule in module files.)

## D. Handoffs
- D1. Login/session/MFA framework and identity-check wizard: base (res.users) and web login controller (credential parameter list extended with the passkey response). auth_passkey/controllers/main.py:3-7; web/controllers/home.py:31,128
- D2. Portal users get passkey management in the portal: auth_passkey_portal (auto-install module). auth_passkey_portal/__manifest__.py:2-12
- D3. Choice of available authentication methods and session/inactivity re-lock: auth_timeout (uses passkey list, second-factor type, password). auth_timeout/models/res_users.py:7-28
- D4. Second-factor policy and codes: auth_totp (skipped by passkey) and auth_totp_mail; see auth_totp note.

## E. Configuration/defaults that change outcomes
- E1. The site address setting (web.base.url) determines relying-party id and accepted origin; tests set it explicitly. auth_passkey/models/auth_passkey_key.py:73,81; auth_passkey/tests/test_passkey_demo.py:228 (TEST)
- E2. Rules: userVerification always REQUIRED; resident (discoverable) credential REQUIRED at registration; not configurable here. auth_passkey/models/auth_passkey_key.py:74,103-104
- E3. No setting to forbid password login once passkeys exist, and no enforcement policy. UNKNOWN — EVIDENCE INSUFFICIENT beyond absence in module files.

## F. Effective extension path (module names only)
- Modules that depend on auth_passkey: auth_passkey_portal, auth_timeout (manifest scan). Objects extended by this module: res.users, res.users.identitycheck (owners base).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end script behaviour (login and registration interactions) beyond file presence.
- UNKNOWN — EVIDENCE INSUFFICIENT: vendored library internals and attestation policy.
- UNKNOWN — EVIDENCE INSUFFICIENT: which authenticators/browsers work in practice.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether administrators can force passkey removal on account compromise beyond the delete right in C6.

