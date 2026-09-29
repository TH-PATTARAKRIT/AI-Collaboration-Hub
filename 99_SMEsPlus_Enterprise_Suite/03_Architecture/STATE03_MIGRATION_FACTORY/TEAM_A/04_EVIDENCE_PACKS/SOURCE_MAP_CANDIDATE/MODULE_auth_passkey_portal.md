# Source Map (candidate) — `auth_passkey_portal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_passkey_portal` |
| Display name | Passkeys Portal |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `74665907237f67e7` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_passkey_portal/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_passkey`, `portal`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Passkeys for portal users
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 24 of 24 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_passkey_portal (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Lets portal users list, add, rename and delete their own passkeys (device-bound sign-in credentials) on the portal Security page. auth_passkey_portal/views/templates.xml:4-39.
- Conditional: auto-installs with auth_passkey and portal. auth_passkey_portal/__manifest__.py:13,27.
- Front-end-only module (no models, no security files). auth_passkey_portal/__manifest__.py:14-16.

## B. Business objects and lifecycle
- Object owned by auth_passkey: a passkey record (name, created, last used) tied to its creating user; a temporary "create" helper record holds the name during registration. auth_passkey_portal/views/templates.xml:20-24; auth_passkey_portal/static/src/js/passkeys_portal_create.js:46.
- Add: identity check -> request registration options -> user enters a name -> device registration -> key stored. auth_passkey_portal/static/src/js/passkeys_portal_create.js:16-56.
- Rename: direct name update, empty name ignored. auth_passkey_portal/static/src/js/passkeys_portal.js:25-38.
- Delete: identity check then removal of own key. auth_passkey_portal/static/src/js/passkeys_portal.js:42-49; auth_passkey/models/auth_passkey_key.py:127-135.
- "Last used" column is the record's last modified time. auth_passkey_portal/views/templates.xml:24.

## C. Validations, security, session/audit
- Portal users may read and modify passkeys but not create/delete directly; creation goes through the helper record with create rights. auth_passkey/security/ir.model.access.csv:3,5.
- Record rules: own passkeys only (by creator); admins (ERP manager) can view and delete others' keys. auth_passkey/security/security.xml:3-11,23-30.
- Delete of another person's key is denied and logged; deleting own key refreshes the session token. auth_passkey/models/auth_passkey_key.py:127-140.
- Add and delete require fresh identity confirmation. auth_passkey/models/res_users.py:20 (decorator); auth_passkey_portal/static/src/js/passkeys_portal_create.js:17-25.
- Rename is not preceded by an identity check in this module. auth_passkey_portal/static/src/js/passkeys_portal.js:33 (observation).
- Passkey login skips the second factor (MFA). auth_passkey/models/res_users.py:66-70; auth_passkey_portal/__manifest__.py:9.
- Permission (TEST): a portal user cannot rename another user's passkey. auth_passkey_portal/tests/test_passkey_portal.py:37-40 (TEST).
- Company scoping: none seen in cited files.

## D. Handoffs
- Inserts a "Passkeys" section before the "revoke all devices" popup on portal Security page. auth_passkey_portal/views/templates.xml:2-3; portal/views/portal_templates.xml:500.
- Reuses portal identity-check helper and dialog component. auth_passkey_portal/static/src/js/passkeys_portal.js:1-3.
- Uses the browser passkey library of auth_passkey. auth_passkey_portal/static/src/js/passkeys_portal_create.js:7.

## E. Configuration/defaults
- Registration uses the system's configured base URL (tests set it). auth_passkey_portal/tests/test_passkey_portal.py:22 (TEST). Production requirement for URL/HTTPS: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- auth_passkey, portal; peers auth_totp_portal, auth_password_policy_portal.

## G. Not verified
- Failure behaviour when device registration is cancelled (error only logged to browser console, passkey_portal_create.js:43-45; downstream outcome not verified): UNKNOWN — EVIDENCE INSUFFICIENT.
- Universal rules: none stated.

