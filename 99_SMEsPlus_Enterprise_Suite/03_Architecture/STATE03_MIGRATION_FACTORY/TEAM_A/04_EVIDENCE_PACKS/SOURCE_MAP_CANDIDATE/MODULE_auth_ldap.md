# Source Map (candidate) — `auth_ldap`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `auth_ldap` |
| Display name | Authentication via LDAP |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5e65eacf181170f0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/auth_ldap/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `base_setup`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `res.company.ldap` (Company LDAP configuration)
- Objects extended from other modules (3): `res.company`, `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.company`, `res.users`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 50 of 50 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — auth_ldap
Source revision: 19.0.post20260921 | Module: "Authentication via LDAP" (auth_ldap/__manifest__.py:4), category Hidden/Tools (:7), LGPL-3 (:20). Depends on base and base_setup (:5); needs the external python-ldap library (:13-18). Basis: static reading of all module files and the base_setup switch. Not executed.

## A. Capabilities and optionality
- A1. Lets people log in with a directory (LDAP) username and password, and creates a local Odoo user automatically the first time they succeed. auth_ldap/README.rst:1-5; auth_ldap/models/res_users.py:13-32; auth_ldap/models/res_company_ldap.py:220-247
- A2. Multiple directory servers can be configured, tried in configured sequence; each belongs to a company; usernames must still be unique across all companies. auth_ldap/models/res_company_ldap.py:35,38-39; auth_ldap/README.rst:10-13
- A3. Per server configuration: address, port (default 389), optional service account (bind DN + password; empty = anonymous), search base, search filter with a login placeholder that must return exactly one entry, optional STARTTLS, "create users automatically" (default on), optional template user to copy. auth_ldap/models/res_company_ldap.py:38-72
- A4. "Test Connection" button reports success, unreachable server, bad bind credentials, timeout, or other error. auth_ldap/models/res_company_ldap.py:266-350; auth_ldap/views/ldap_installer_views.xml:11
- A5. Optionality: not auto_install, not an application. Turned on from General Settings ("LDAP Authentication" switch installs the module; a further "LDAP Server" button appears once installed). base_setup/models/res_config_settings.py:23; base_setup/views/res_config_settings_views.xml:151-156; auth_ldap/views/res_config_settings_views.xml:8-13
- A6. Referral chasing is off by default, controlled by parameter auth_ldap.disable_chase_ref (default true). auth_ldap/models/res_company_ldap.py:109-111
- A7. Password change by an LDAP-backed user is attempted on the directory first; if the directory accepts, the local password is blanked. auth_ldap/models/res_users.py:52-69; auth_ldap/models/res_company_ldap.py:249-264 (README states the opposite — that Odoo does not manage LDAP password changes: auth_ldap/README.rst:33-34; see G).

## B. Objects and relationships
- B1. res.company.ldap "Company LDAP configuration": belongs to a company (removed with it), ordered by sequence. auth_ldap/models/res_company_ldap.py:32-39
- B2. Company gets a list of its LDAP configurations, visible only to Settings administrators; copied when the company is duplicated. auth_ldap/models/res_company.py:10-11
- B3. General Settings screen shows the current company's LDAP list. auth_ldap/models/res_config_settings.py:10
- B4. Local user record: created from the directory entry (name from "cn", login = typed login, email if the login looks like an email, company of the matching configuration) or copied from the template user; created without triggering a password-reset invitation. auth_ldap/models/res_company_ldap.py:201-245
- B5. Lifecycle of an LDAP user: no local account -> first successful directory login -> local account created (blank local password) -> later logins re-verified against the directory each time. auth_ldap/README.rst:39-47; auth_ldap/models/res_company_ldap.py:231-247

## C. Validations, security, audit
- C1. Order of checks at login: local login is tried first; the directory is consulted only if no local user with that login exists (existing local user -> original denial stands). auth_ldap/models/res_users.py:13-32
- C2. For an existing user whose local check fails, a second attempt goes against the directory unless the context is a non-interactive API call for a user restricted to API keys (e.g. 2FA on). auth_ldap/models/res_users.py:34-50
- C3. Empty password never authenticates (guards against unauthenticated bind); filter must match exactly one entry with a DN; connection/directory errors are logged and treated as a failed login. auth_ldap/models/res_company_ldap.py:133-162,116-131,159-161,195-199
- C4. Login text is escaped into the directory filter. auth_ldap/models/res_company_ldap.py:6,122
- C5. If a matching local login exists but is archived, or creation is off / no configuration allows it, access is denied ("No local user found for LDAP login and not configured to create one"). auth_ldap/models/res_company_ldap.py:234-247
- C6. Access: only Settings administrators (base.group_system) have rights on the configuration; no other group, no record rules, no company rule. Configurations are fetched with elevated rights at login. auth_ldap/security/ir.model.access.csv:2; auth_ldap/models/res_company_ldap.py:82. The lookup does not filter by the user's company (all configured servers are tried in sequence order). auth_ldap/models/res_company_ldap.py:82-94
- C7. The service-account password is held as a plain text field in the configuration (masked in the form); it is not encrypted in this module. auth_ldap/models/res_company_ldap.py:45-46; auth_ldap/views/ldap_installer_views.xml:24
- C8. LDAP logins come back with "mfa: default", so two-factor (auth_totp) still applies after a directory success. auth_ldap/models/res_users.py:27-31,45-49; see auth_totp note.
- C9. Failures are logged (error level) with the LDAP exception text; there is no dedicated audit table or login-attempt log in this module; the base login cooldown wraps _login. auth_ldap/models/res_company_ldap.py:160,196,198; base/models/res_users.py:760-782
- C10. If the template user has a password set, every auto-created user inherits it as a local password (README warning). auth_ldap/README.rst:57-64. The password-policy module is not consulted when the directory changes the password (blanking uses direct storage update). auth_ldap/models/res_users.py:57-60,63-69
- C11. Test coverage (TEST): a first-time directory login (mocked) creates the user and yields a session. auth_ldap/tests/test_auth_ldap.py:11-70

## D. Handoffs
- D1. Login, credential check, session and MFA framework: base (res.users) and web (login controller). auth_ldap/models/res_users.py:13-50; base/models/res_users.py:760-782
- D2. Settings entry and module switch: base_setup. base_setup/models/res_config_settings.py:23
- D3. Company object: base (res.company). auth_ldap/models/res_company.py:7-11
- D4. Second factor after directory success: auth_totp / auth_totp_mail; passkey skips MFA only for passkey logins (see auth_passkey note).
- D5. No accounting, HR or other business handoff. Users created here are ordinary internal users with rights from the template or defaults of base. UNKNOWN — EVIDENCE INSUFFICIENT: exact default groups given to users created without a template (defined by base).

## E. Configuration/defaults that change outcomes
- E1. Search filter and base determine which directory entries can log in; filter must be unique per login. auth_ldap/models/res_company_ldap.py:47-64
- E2. create_user (default on) and template user decide whether unknown directory users get accounts and with which groups. auth_ldap/models/res_company_ldap.py:65-68,240-245
- E3. STARTTLS flag: when on, an unsupporting server makes all attempts fail; when off the bind is unencrypted (plain ldap:// URI is always used). auth_ldap/models/res_company_ldap.py:69-72,106,112-113
- E4. Sequence order between configurations; first success wins. auth_ldap/models/res_company_ldap.py:35,38,94
- E5. Parameter auth_ldap.disable_chase_ref. auth_ldap/models/res_company_ldap.py:109

## F. Effective extension path (module names only)
- Objects extended by this module: res.users, res.company, res.config.settings (owners base, base_setup). No other Community module declares a dependency on auth_ldap and none references res.company.ldap (grep of manifests and sources found none).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: runtime behaviour against a real directory (nothing executed; test uses mocked directory).
- UNKNOWN — EVIDENCE INSUFFICIENT: reconciliation of README statement that Odoo does not change LDAP passwords with the code that does (auth_ldap/models/res_users.py:52-61).
- UNKNOWN — EVIDENCE INSUFFICIENT: case handling of logins (local lookup lowercases inside creation, but the first lookup uses the login as typed). auth_ldap/models/res_users.py:18; auth_ldap/models/res_company_ldap.py:231
- UNKNOWN — EVIDENCE INSUFFICIENT: whether directory groups/attributes beyond "cn" are ever synchronised (none found in module).

