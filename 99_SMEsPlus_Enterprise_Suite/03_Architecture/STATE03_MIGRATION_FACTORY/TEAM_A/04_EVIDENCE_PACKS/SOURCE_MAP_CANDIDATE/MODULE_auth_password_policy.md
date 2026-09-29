# Source Map (candidate) — `auth_password_policy`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_password_policy` |
| Display name | Password Policy |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `10ca730c7a5509fe` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_password_policy/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `web`
- Direct dependents in 300-module list (2): `auth_password_policy_portal`, `auth_password_policy_signup`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Implement basic password policy configuration & check
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`, `res.config.settings`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 32 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — auth_password_policy
Source revision: 19.0.post20260921 | Module: "Password Policy" (auth_password_policy/__manifest__.py:2), category Hidden/Tools (:4), LGPL-3 (:22). Basis: static reading of all module files and base hooks. No tests exist in this module (skeleton: tests_py 0; no tests folder).

## A. Capabilities and optionality
- A1. One enforceable rule: a minimum password length, held in a system parameter and editable in general Settings under a "Minimum Password Length" option (0 disables). auth_password_policy/models/res_config_settings.py:7-9; auth_password_policy/views/res_config_settings_views.xml:9-12
- A2. Shipped default is 8 characters (parameter created with forcecreate, noupdate), although the Settings field default is 0 when the parameter is unset. auth_password_policy/data/defaults.xml:2-6; auth_password_policy/models/res_config_settings.py:8; auth_password_policy/models/res_users.py:13,25
- A3. Server-side enforcement: whenever a password value is written, each non-empty new password shorter than the minimum causes a user-facing error stating the required and actual length; several failures are joined. auth_password_policy/models/res_users.py:16-33
- A4. Client-side "password strength meter" widget on the own-password and multi-user password wizards; required policy is fetched from the server; an additional non-mandatory recommendation set (16 chars with 2 words, or 12 chars with 3 character classes) drives the meter score only. auth_password_policy/views/res_users.xml:2-21; auth_password_policy/static/src/password_field.js:14-40; auth_password_policy/static/src/password_policy.js:11-71,80-84,97-108
- A5. Optionality: not auto_install and not an application; depends on base_setup and web; it is installed on demand. auth_password_policy/__manifest__.py:5. Conditional companions that auto-install when the paired module is present: auth_password_policy_portal (with portal) and auth_password_policy_signup (with auth_signup). auth_password_policy_portal/__manifest__.py:3-5; auth_password_policy_signup/__manifest__.py:2-5
- A6. Only length is enforced; there is no server check of character classes, words, reuse/history, expiry, or lockout in this module. Client code contains minimum-words and minimum-classes fields but the server policy supplies only length. auth_password_policy/models/res_users.py:12-14,21-33; auth_password_policy/static/src/password_policy.js:11-23

## B. Objects and relationships
- B1. No new business object. Extends res.users (owner: base) with a policy getter and a check; extends the settings screen with one parameter-backed field. auth_password_policy/models/res_users.py:6-33; auth_password_policy/models/res_config_settings.py:4-9
- B2. Lifecycle: none (a parameter). A password change flows: user/wizard/portal/signup -> password field write -> policy check -> hashing. base/models/res_users.py:217-219,294-297,919-931 (base owns the flow)

## C. Validations, security, audit
- C1. The check hooks the setter of the password field, so it applies to any path that sets a password through the ORM (user form, change-password wizards, own-password change, user creation/reset flows) — it rejects the write before hashing. auth_password_policy/models/res_users.py:16-19; base/models/res_users.py:217-219,294-297,919-931
- C2. Not applied to already-stored passwords; existing users are not forced to change, and login itself does not test length. UNKNOWN — EVIDENCE INSUFFICIENT for any other automatic rechecking (none found in module).
- C3. Empty passwords are skipped by this check (base separately forbids empty new passwords in the change flow). auth_password_policy/models/res_users.py:27-28; base/models/res_users.py:919-922
- C4. The parameter is read with elevated rights (sudo) so ordinary users can be checked; the policy values returned to clients contain only the minimum length. auth_password_policy/models/res_users.py:9-14,23-25
- C5. Who may change the setting: users who can open general Settings (base_setup screen); the module defines no groups, rules or access rows. auth_password_policy/views/res_config_settings_views.xml:6-9; skeleton: groups, rules, access none. Settings changes carry no dedicated audit trail here.
- C6. Not company-scoped: single global system parameter. auth_password_policy/models/res_config_settings.py:8

## D. Handoffs
- D1. Password storage, hashing, change and reset flows, identity check, and change-password wizards: base. base/models/res_users.py:217-221,294-297,899-931,1461-1476
- D2. Portal profile password change shows the minimum length: auth_password_policy_portal. auth_password_policy_portal/controllers.py:1-10
- D3. Public sign-up / reset form shows the minimum length and meter: auth_password_policy_signup (owner of sign-up flow: auth_signup). auth_password_policy_signup/controllers.py:1-10; auth_password_policy_signup/models/ir_http.py:1-11
- D4. Two-factor and passkeys are independent of this policy: see auth_totp and auth_passkey notes.

## E. Configuration/defaults that change outcomes
- E1. auth_password_policy.minlength (integer; default seed 8; 0 disables). Negative input in Settings is coerced to 0. auth_password_policy/data/defaults.xml:4-5; auth_password_policy/models/res_config_settings.py:11-15
- E2. A malformed non-integer value in the parameter would raise on read. UNKNOWN — EVIDENCE INSUFFICIENT (no guard seen at res_users.py:13,25; behaviour not tested).

## F. Effective extension path (module names only)
- Dependents: auth_password_policy_portal, auth_password_policy_signup (manifest scan). res.users is extended by many Community modules (see the base note); no module was found overriding get_password_policy or _check_password_policy other than this one (grep found only auth_password_policy definitions).

## G. Not verified
- Direct hashed-password writes exist in base only for the setter itself and for re-hashing at login when the stored hash scheme is outdated (no policy check needed there). base/models/res_users.py:294-306,372. UNKNOWN — EVIDENCE INSUFFICIENT: raw SQL or third-party code writing password columns outside the ORM.
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end behaviour beyond the policy scoring functions (widget templates and CSS not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: translation coverage for the error messages.

