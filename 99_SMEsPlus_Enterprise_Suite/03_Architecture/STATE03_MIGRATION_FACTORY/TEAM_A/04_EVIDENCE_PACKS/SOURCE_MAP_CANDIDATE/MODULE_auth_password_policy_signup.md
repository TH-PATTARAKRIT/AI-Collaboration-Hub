# Source Map (candidate) — `auth_password_policy_signup`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_password_policy_signup` |
| Display name | Password Policy support for Signup |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4bce4ed562a6bce9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_password_policy_signup/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_password_policy`, `auth_signup`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 16 of 16 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: auth_password_policy_signup (Odoo 19.0.post20260921)
Scope: this note covers only the pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Bridge module: shows the password-length policy on the public self-signup / reset-password form. auth_password_policy_signup/__manifest__.py:3 (depends auth_password_policy + auth_signup).
- Conditional: installs automatically when both parent modules are present. auth_password_policy_signup/__manifest__.py:5.
- Core: signup password field gets a "minimum length" attribute and a live strength meter next to it. auth_password_policy_signup/views/signup_templates.xml:4-9.
- Optional/none: no menu, no settings screen, no data records of its own. auth_password_policy_signup/__manifest__.py:6-8.

## B. Business objects and lifecycle
- No business objects (no models of its own). auth_password_policy_signup/models/ir_http.py:5-11 only extends the web-request helper (translation list).
- The policy value itself belongs to auth_password_policy (system parameter for minimum length); this module only reads it. auth_password_policy_signup/controllers.py:9.

## C. Validations, security, session/audit
- Front-end only: meter and length hint are advisory in the browser; the browser-side check does not itself enforce. auth_password_policy_signup/static/src/public/components/password_meter/password_meter.js:19-25.
- Enforcement point is elsewhere: on saving a user password the policy check rejects passwords shorter than the configured minimum with a message. auth_password_policy/models/res_users.py:16-33 (parent module, same tree).
- Empty password is skipped by the check (not rejected here). auth_password_policy/models/res_users.py:27-28.
- No groups, record rules or company scoping added. No audit/session behaviour added. (module contains no security files: auth_password_policy_signup/__manifest__.py:6-8)

## D. Handoffs
- Extends the signup configuration handed to the login/signup pages with a "minimum length" value. auth_password_policy_signup/controllers.py:7-10; base function auth_signup/controllers/main.py:126.
- Loads the shared password meter/policy scripts for the public site. auth_password_policy_signup/__manifest__.py:9-15.
- Adds the module's translation set to public pages. auth_password_policy_signup/models/ir_http.py:9-11.

## E. Configuration/defaults that change outcomes
- Minimum password length parameter: default 8 on install (not overwritten on update). auth_password_policy/data/defaults.xml:3-6.
- Settings field for administrators, floor of 0. auth_password_policy/models/res_config_settings.py:7-15.
- If the parameter is empty/absent the hint's minimum is not populated; behaviour of the meter with a missing value: UNKNOWN — EVIDENCE INSUFFICIENT (JS treats non-numeric as no minimum, password_meter.js:19-20, but page-level outcome not verified).

## F. Effective extension path
- auth_password_policy, auth_signup (dependencies); portal-side counterpart auth_password_policy_portal.

## G. Not verified
- Whether signup form-level submission is blocked client-side when the length is short: UNKNOWN — EVIDENCE INSUFFICIENT.
- Any test coverage for this module: none found in module tree (no tests directory).
- Universal rules: none stated.

