# Source Map (candidate) — `auth_password_policy_portal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_password_policy_portal` |
| Display name | Password Policy support for Signup |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a8a33c0058fe6c0e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_password_policy_portal/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_password_policy`, `portal`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `ir.http`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 15 of 15 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_password_policy_portal (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Bridge module: adds the password-length policy hint and strength meter to the portal "Security" page's new-password field. auth_password_policy_portal/views/templates.xml:2-10.
- Conditional: auto-installs when auth_password_policy and portal are both present. auth_password_policy_portal/__manifest__.py:3,5.
- No menu, settings or data of its own. auth_password_policy_portal/__manifest__.py:6.

## B. Business objects and lifecycle
- No models of its own; only extends the web-request helper for translations. auth_password_policy_portal/models/ir_http.py:5-11.
- Applies to the portal user changing their own password (Security page section "change password"). portal/views/portal_templates.xml:431,442 (parent).

## C. Validations, security, session/audit
- Meter is placed only on the first "new password" input because the confirmation must match. auth_password_policy_portal/views/templates.xml:4,5-7.
- Minimum-length hint attribute added to that first input. auth_password_policy_portal/views/templates.xml:8-9.
- Actual enforcement occurs when a password is saved: shorter than the configured minimum is rejected with a message; empty values skipped. auth_password_policy/models/res_users.py:16-33 (parent module).
- No groups, record rules, company scoping, session or audit additions (no security files). auth_password_policy_portal/__manifest__.py:6.
- The meter component name is reused from the signup bridge/public assets; whether it is loaded on the portal page depends on frontend assets of auth_password_policy: UNKNOWN — EVIDENCE INSUFFICIENT (this module's manifest lists no assets, auth_password_policy_portal/__manifest__.py:1-9).

## D. Handoffs
- Extends the values prepared for portal pages with the configured minimum length. auth_password_policy_portal/controllers.py:6-10.
- Provides translation set of auth_password_policy to frontend. auth_password_policy_portal/models/ir_http.py:9-11.

## E. Configuration/defaults
- Minimum length parameter defaults to 8 at install. auth_password_policy/data/defaults.xml:3-6.
- Admin setting can lower to 0 (no minimum). auth_password_policy/models/res_config_settings.py:7-15.

## F. Effective extension path
- auth_password_policy, portal; sibling modules auth_totp_portal, auth_passkey_portal (same Security page); auth_password_policy_signup.

## G. Not verified
- Runtime rendering of meter on the portal page: UNKNOWN — EVIDENCE INSUFFICIENT.
- Tests: none in module tree.
- Manifest title duplicates the signup bridge's title ("Password Policy support for Signup"). auth_password_policy_portal/__manifest__.py:2 (observation).

