# Source Map (candidate) — `base_setup`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_setup` |
| Display name | Initial Setup Tools |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `07e88ce844c51965` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_setup/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (19): `account`, `auth_ldap`, `auth_oauth`, `auth_passkey`, `auth_password_policy`, `auth_signup`, `base_geolocalize`, `certificate`, `cloud_storage`, `crm`, `event`, `google_account` … (+7)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (6): `web_window_title` — LGPL-3, `wk_redis_session` — Other proprietary, `19_bhpro_master_data` — OPL-1, `deepseek_r1` — GPL-3, `partner_firstname` — AGPL-3, `bh_hide_odoo_edition` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 1, views 2, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `kpi.provider` (KPI Provider)
- Objects extended from other modules (3): `ir.http`, `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `kpi.provider` ← Community: `account`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `res.users`, `res.config.settings`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 37 of 37 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_setup
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Provides the "General Settings" page used at first configuration: user invitation, language, company info, document layout, default access rights, import/export switch, and a set of integration switches (base_setup/__manifest__.py:8-11; base_setup/views/res_config_settings_views.xml:11-186).
- Installs automatically; depends on base and web (base_setup/__manifest__.py:14,25).
- Settings toggles that install other optional modules on save: data import, Google/Microsoft calendar sync, mail plugin, OAuth login, LDAP login, inter-company rules, phone, Unsplash images, SMS, partner autocomplete, geolocalization, reCAPTCHA, Cloudflare Turnstile, Google address autocomplete (base_setup/models/res_config_settings.py:14-32). (TEST) saving settings installs a module only when a toggle was set (base_setup/tests/test_res_config.py:71-96).
- Other capabilities: bulk user creation from email addresses (base_setup/models/res_users.py:12-37); an admin dashboard data endpoint (base_setup/controllers/main.py:10-51); a demo-data-active probe (base_setup/controllers/main.py:53-59); cross-database KPI summary endpoint and provider registry (base_setup/controllers/kpi.py:20-177; base_setup/models/kpi_provider.py:4-25).
- Adds category tags to the contact kanban card (base_setup/views/res_partner_views.xml:9-11).

## B. Business objects, relationships, lifecycle
- Settings screen is a temporary record (no stored business data) that adds fields on the shared settings model: company selection, counts of companies/users/languages, company address summary, report footer, layout, multi-currency group, "show effect" flag, profiling-enabled-until (base_setup/models/res_config_settings.py:11-46,98-136).
- "Default access rights for new users" group: created on demand as a group named "Default access for new users" and registered under the base module's external id, never overwritten (base_setup/models/res_config_settings.py:58-79). (TEST) adding a group to it makes newly created users members of that group, existing users unchanged (base_setup/tests/test_default_group.py:18-45).
- Bulk invite: existing deactivated users matching an email are reactivated; new users are created with login = normalized email (base_setup/models/res_users.py:19-35).
- KPI provider: abstract contract that other modules override to return KPIs of type integer or return status (late/longterm/to_do/to_submit/done) (base_setup/models/kpi_provider.py:8-25).

## C. Validations, automation, security, credentials
- Bulk invite requires the mail/discuss capability (a normalized-email field); otherwise an error tells the admin to install Discuss (base_setup/models/res_users.py:16-17). Any other access control is the user model's create rights: UNKNOWN — EVIDENCE INSUFFICIENT at this module.
- Dashboard endpoint requires the ERP-manager group; returns active internal-user count, count and latest 10 internal users who never logged in (base_setup/controllers/main.py:10-51).
- Import/Export switch and feedback-effect switch are shown only to debug-feature users; API-key management shown to system administrators only (base_setup/views/res_config_settings_views.xml:124,127,130).
- KPI endpoint: no platform auth, no session; accepts up to 500 (database, API key) pairs; for each database it silently ignores missing databases, version mismatch (different release series) and invalid keys, so nothing about database existence leaks; runs each provider read-only (rolls back after each) and returns provider errors per addon plus the active internal users with last login (base_setup/controllers/kpi.py:74-145,149-177). (TEST) invalid credential, missing database, version mismatch, credential limit and partial provider failure are covered (base_setup/tests/test_kpi_controller.py:76-164). Credential implication: caller supplies per-database user API keys with the remote-procedure scope (base_setup/controllers/kpi.py:102).
- KPI providers are discovered from installed addon manifests through a "kpi_providers" entry; malformed or failing entries are logged and skipped (base_setup/controllers/kpi.py:33-71). (TEST) parsing/filtering (base_setup/tests/test_kpi_controller.py:206).
- Settings page company: required, defaults to the current company; "root company" flag is true when the company has no parent (base_setup/models/res_config_settings.py:11-13,133-136). (TEST) multi-company config group behavior (base_setup/tests/test_res_config.py:23).
- Session information sent to internal users includes whether the "celebration effect" is enabled (base_setup/models/ir_http.py:9-13).

## D. Handoffs to other modules
- Each toggle hands off to its module: base_import (import), google_calendar, microsoft_calendar, mail_plugin, auth_oauth, auth_ldap, account_inter_company_rules, voip, web_unsplash, sms, partner_autocomplete, base_geolocalize, google_recaptcha, website_cf_turnstile, google_address_autocomplete (base_setup/models/res_config_settings.py:14-32). Which of these exist in this tree: UNKNOWN — EVIDENCE INSUFFICIENT (only three appear in the assigned module list: base_import, google_recaptcha, google_address_autocomplete).
- Users, companies, languages, layouts, groups: base module; document layout configurator, report preview: web (base_setup/views/res_config_settings_views.xml:86-90).
- Databases-list dashboard consuming KPI data: a separate "databases" module (per provider docstring) (base_setup/models/kpi_provider.py:12).

## E. Configuration/defaults that change outcomes
- System parameter "base_setup.show_effect" defaults True on install and is not overwritten later (base_setup/data/base_setup_data.xml:3-7).
- Default access rights: with the group empty new users get basic employee access; the help text states that by default new users receive highest rights for installed apps (base_setup/views/res_config_settings_views.xml:117).
- Profiling-enabled-until stored as base profiling parameter (base_setup/models/res_config_settings.py:46).
- Settings blocks depend on company count, user count and language count for wording (base_setup/views/res_config_settings_views.xml:21-24,40-43,69-72).

## F. Effective extension path
- Other modules extend the settings view and add their own module_* toggles (pattern: base_setup/models/res_config_settings.py:14-32), and override the KPI provider contract or declare providers in their manifest (base_setup/models/kpi_provider.py:8-11; base_setup/controllers/kpi.py:39).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: the widget that sends bulk invitations (client side).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether a demo-data probe or dashboard data is used by other modules.

