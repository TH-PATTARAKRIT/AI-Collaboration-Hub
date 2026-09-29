# Source Map (candidate) — `auth_totp_portal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_totp_portal` |
| Display name | TOTPortal |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2807088f13ccbc9b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_totp_portal/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `portal`, `auth_totp`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 30 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_totp_portal (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Lets portal (external) users manage two-factor authentication (TOTP) from the portal Security page: enable, disable, list and revoke trusted devices, revoke all. auth_totp_portal/views/templates.xml:13-64.
- Conditional: auto-installs when portal and auth_totp are both installed. auth_totp_portal/__manifest__.py:2-5.
- Core to module: the enable / disable / revoke actions. auth_totp_portal/static/src/interactions/totp_enable.js:119-187; totp_disable.js:7-21; revoke_trusted_device.js:6-20; revoke_all_trusted_devices.js:7-21.

## B. Business objects and lifecycle
- Objects owned by auth_totp (parent): the user's 2FA state, an activation wizard (temporary record holding secret and QR), trusted devices. auth_totp/models/res_users.py:36; auth_totp/wizard/auth_totp_wizard.py:59.
- Lifecycle: not enabled -> user requests activation (wizard created with a fresh secret) -> user confirms with 6-digit code -> enabled; secret cleared from the wizard. auth_totp/models/res_users.py:182-205; auth_totp/wizard/auth_totp_wizard.py:59-66.
- Disable: revokes all trusted devices then removes the secret. auth_totp/models/res_users.py:155-160.
- Trusted device: created when user chooses to trust a browser; age limit from a system parameter. auth_totp/models/auth_totp.py:25-36.
- Portal page shows status and, if enabled, a table of trusted devices with created date. auth_totp_portal/views/templates.xml:20-58.

## C. Validations, security, session/audit
- Portal group is granted read/write/create/delete on the activation wizard, but each user is restricted to own wizard by a rule. auth_totp_portal/security/security.xml:3-11; auth_totp/security/security.xml:11-15.
- Trusted devices: portal and internal users may only touch their own; system administrators see all; public users none. auth_totp/security/security.xml:18-37.
- Every sensitive action (enable-wizard, enable, disable, revoke device(s)) requires fresh identity re-confirmation (password prompt). auth_totp/models/res_users.py:154,181,207 (decorator); auth_totp/wizard/auth_totp_wizard.py:58; base/models/res_users.py:1556; UI wrapper auth_totp_portal/static/src/interactions/totp_enable.js:126-131.
- Enable only for oneself and only if not already enabled. auth_totp/models/res_users.py:183-187.
- Code must be digits only; wrong code rejected. auth_totp/wizard/auth_totp_wizard.py:60-76. Client requires exactly 6 characters. auth_totp_portal/static/src/interactions/totp_enable.js:31-34.
- Code login: rate-limited, codes not reusable (must be newer than last used), failure/success logged. auth_totp/models/res_users.py:74-93.
- Secret is part of the session token, so disabling on own session refreshes the token to avoid logout. auth_totp/models/res_users.py:70-71,165-168.
- Non-internal users are sent to the portal Security page for 2FA invites; internal users keep parent behaviour. auth_totp_portal/models/res_users.py:10-14.
- Company scoping: no rule referencing company found in cited files: UNKNOWN — EVIDENCE INSUFFICIENT beyond that.

## D. Handoffs
- Injects a section into the portal Security page after the change-password section. auth_totp_portal/views/templates.xml:2-3; portal/views/portal_templates.xml:442.
- Uses portal's identity-check helper. auth_totp_portal/static/src/interactions/totp_disable.js:4.
- Embeds the auth_totp activation form layout into the page because portal users cannot read backend views. auth_totp_portal/views/templates.xml:4-11.
- Documentation link points to Odoo public docs. auth_totp_portal/views/templates.xml:16.

## E. Configuration/defaults
- Trusted device validity: system parameter with default constant; invalid or non-positive values fall back to default with a warning. auth_totp/models/auth_totp.py:25-36.

## F. Effective extension path
- auth_totp, portal; peers auth_passkey_portal, auth_password_policy_portal; auth_totp_mail (mail-based invites).

## G. Not verified
- Default trusted-device age in days (constant defined outside cited lines): UNKNOWN — EVIDENCE INSUFFICIENT.
- Test coverage: end-to-end tour on the portal exists (TEST) auth_totp_portal/tests/test_tour.py:15-21.
- Universal rules: none stated.

