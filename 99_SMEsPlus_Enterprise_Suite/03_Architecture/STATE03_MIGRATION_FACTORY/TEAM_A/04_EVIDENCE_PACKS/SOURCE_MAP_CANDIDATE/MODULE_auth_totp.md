# Source Map (candidate) — `auth_totp`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_totp` |
| Display name | Two-Factor Authentication (TOTP) |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `702a2279c9f98b6a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_totp/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (3): `auth_timeout`, `auth_totp_mail`, `auth_totp_portal`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Extra Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `auth_totp.wizard` (2-Factor Setup Wizard); `auth_totp.device` (Authentication Device); `auth.totp.rate.limit.log` (TOTP rate limit logs)
- Objects extended from other modules (2): `res.users.apikeys`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `auth_totp.device` ← Community: `auth_timeout`, `auth_totp_mail`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `res.users.apikeys`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 49 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — auth_totp
Source revision: 19.0.post20260921 | Module: "Two-Factor Authentication (TOTP)" (auth_totp/__manifest__.py:2), category Extra Tools (:18), LGPL-3 (:37). Basis: static reading of models, controller, security, views, tests and the base login hooks it plugs into.

## A. Capabilities and optionality
- A1. Lets a user protect their own account with a time-based 6-digit one-time code from an authenticator app; after password success, a second step asks for the code before the session becomes fully logged in. auth_totp/__manifest__.py:6-11; auth_totp/controllers/home.py:16-92
- A2. Code parameters: 6 digits, 30-second step, SHA-1, secret 160 bits; a code is accepted if valid within one step either side of the current time. auth_totp/models/totp.py:10,15-17,23-41
- A3. Optional per user, self-service: only the user themself can turn it on (via an on-screen activation wizard showing a QR code and secret); administrators may only turn it off for others. auth_totp/models/res_users.py:98-101,154-160,181-187; auth_totp/wizard/auth_totp_wizard.py:21-75; auth_totp/views/res_users_views.xml:30-47
- A4. "Trust this device": at code entry the user can tick "Don't ask again on this device"; a browser cookie plus a stored device key then skips the second step until expiry (default 90 days, overridable by parameter auth_totp.trusted_device_age; invalid or non-positive value falls back to 90 with a log warning). auth_totp/controllers/home.py:11-12,33-41,60-81; auth_totp/models/auth_totp.py:25-38; auth_totp/views/templates.xml:27-28
- A5. Turning 2FA on blocks password-based programmatic (RPC) access for that user; scripts must use API keys instead. auth_totp/models/res_users.py:66-69; auth_totp/__manifest__.py:13-15; base/models/res_users.py:308-310,356,396 (TEST) auth_totp/tests/test_totp.py:79-100 (password RPC denied after enabling; allowed again after disabling, :113-119)
- A6. Filters on the user list: "Two-factor authentication Enabled/Disabled". auth_totp/views/res_users_views.xml:10-11
- A7. Optionality: auto_install = True with dependency on web, so it is present in practically every database; feature is off per user until they enable it. auth_totp/__manifest__.py:17,19. Mandatory enforcement policy is NOT in this module (see D2).

## B. Objects and relationships
- B1. Extends res.users (owner: base) with: secret (never readable through normal access, stored in a raw column), last-used code counter, "enabled" indicator (derived from having a secret), and a list of trusted devices. auth_totp/models/res_users.py:33-36,38-41,61-64
- B2. Trusted device (auth_totp.device): a specialised API-key store, one row per remembered browser with description ("Browser on Platform (City, Country)"), scope "browser", expiry; owner is the user, removed with the user. auth_totp/models/auth_totp.py:15-18; auth_totp/controllers/home.py:61-74; base/models/res_users.py:1519-1530
- B3. Activation wizard (auth_totp.wizard, transient): holds user, generated secret, QR image, entered code. auth_totp/wizard/auth_totp_wizard.py:21-32
- B4. Rate-limit log (auth.totp.rate.limit.log, transient): user, IP address, type (send email / code check). auth_totp/models/auth_totp_rate_limit_log.py:4-15
- B5. Lifecycle of 2FA for a user: disabled -> (identity re-check + wizard with valid code) -> enabled -> (disable by self or admin) -> disabled. Disabling revokes all trusted devices and clears the secret. auth_totp/models/res_users.py:154-179,181-205

## C. Validations, security, audit
- C1. Login step: each code check is counted; more than 5 checks within one hour for the same user blocks further checks with an access-denied message; the counter is cleared on success. Same limit (5/h) exists for "send email" type (used by auth_totp_mail). auth_totp/models/res_users.py:24-27,75-76,90,120-152
- C2. Replay protection: a code whose time-step is not newer than the last accepted one is rejected ("use the latest 6-digit code"). auth_totp/models/res_users.py:84-88 (TEST) auth_totp/tests/test_totp.py:87-91
- C3. Failed/successful/reuse checks and enable/disable events are written to the server log with user and login (no dedicated audit table). auth_totp/models/res_users.py:81,85,89,100,106,117,158,170
- C4. Sensitive actions (enable wizard, disable, revoke devices, confirm activation) require a recent password re-check (within 10 minutes) and must be done over HTTP. auth_totp/models/res_users.py:154,181,207; auth_totp/wizard/auth_totp_wizard.py:58; base/models/res_users.py:87-108
- C5. Changing the password revokes all of the user's trusted devices. Enabling/disabling 2FA changes the session token fields so other sessions are invalidated while the acting session is refreshed. auth_totp/models/res_users.py:71-72,109-116,164-168,214-217
- C6. Half-logged-in state: after password, the session holds only a "pre-login" user; the authenticate call returns no user id until the code is validated (TEST) auth_totp/tests/test_totp.py:132-157. Login attempts pass through base's cooldown context. auth_totp/controllers/home.py:45; base/models/res_users.py:1215; odoo/http.py:1250-1259,1268-1288
- C7. Access: trusted devices readable by employees and portal users (rule limits to own rows); public users see none; Settings administrators see all rows to revoke. Wizard: internal users full rights limited by rule to own wizard. Rate-limit log: no rights for normal groups (system only through sudo). auth_totp/security/ir.model.access.csv:2-4; auth_totp/security/security.xml:2-38
- C8. Administrative action "Disable two-factor authentication" appears in the user list action menu for group base.group_erp_manager (Access Rights); the action method itself accepts self or an administrator/superuser. auth_totp/data/ir_action_data.xml:4-13; auth_totp/models/res_users.py:157
- C9. No company scoping: authentication data belong to the user, not to a company. (No company field or company rule in module files.)

## D. Handoffs
- D1. Login framework hooks (partial session, MFA type/URL, credential types, API key store, identity re-check): owner base (res.users) with web/controllers. base/models/res_users.py:312-330,1313-1319; web/controllers/utils.py:236-250
- D2. Mandatory-2FA policy setting (parameter auth_totp.policy: all required / employee required), invitation email, and a second method "totp_mail" (code by email): owner auth_totp_mail. auth_totp_mail/models/res_users.py:94-95,122-136
- D3. Portal users enabling 2FA from the portal: auth_totp_portal (auto_install with portal). auth_totp_portal/__manifest__.py:4-5
- D4. Inactivity re-authentication: auth_timeout (depends on auth_totp, auth_totp_mail, auth_passkey, bus). auth_timeout/__manifest__.py:5
- D5. Passkey login can skip the second step: see auth_passkey note (mfa 'skip' value in base contract). base/models/res_users.py:337-341

## E. Configuration/defaults that change outcomes
- E1. auth_totp.trusted_device_age (days; default 90). auth_totp/models/auth_totp.py:28; auth_totp/controllers/home.py:12
- E2. Rate limits are constants (5 per 3600 s) — not configurable in this module. auth_totp/models/res_users.py:24-27
- E3. QR issuer name uses the request host name, otherwise the company display name. auth_totp/wizard/auth_totp_wizard.py:37-39

## F. Effective extension path (module names only)
- Depend on / extend auth_totp objects: auth_totp_mail, auth_totp_portal, auth_timeout (manifest scan; auth_totp_mail extends the device and user models). Other Community modules mentioning totp: l10n_fr_pdp, test_website (references only; not analysed).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side tour scripts and the front-end login template beyond the fields cited.
- UNKNOWN — EVIDENCE INSUFFICIENT: how the mobile app or third-party clients react to the pre-login state (code carries a workaround comment at home.py:82-87).
- UNKNOWN — EVIDENCE INSUFFICIENT: effect of proxy/IP configuration on the recorded IP in the rate-limit log.
- UNKNOWN — EVIDENCE INSUFFICIENT: l10n_fr_pdp and test_website usage of totp.

