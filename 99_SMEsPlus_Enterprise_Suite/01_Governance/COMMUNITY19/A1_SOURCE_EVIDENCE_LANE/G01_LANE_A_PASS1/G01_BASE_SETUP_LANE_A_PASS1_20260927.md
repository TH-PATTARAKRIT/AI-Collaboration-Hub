# G01 PLATFORM_BASE — LANE A PASS-1 — `base_setup`

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T3 |
| Group | G01 PLATFORM_BASE |
| Module | `base_setup` (governed roster member, FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material viewed. No runtime proof claimed. |

Clean-room note: findings are neutral WHAT / WHY / RISK abstractions. Identifiers are pointers only; nothing here is a recommendation to copy schema, ORM, workflow or UI.

## 1. Evidence Pointer Table

All paths relative to `addons/` at the anchor commit. SHA-1 = `git hash-object` of the fetched file.

| # | Path | Git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | base_setup/__manifest__.py | 92ae94dd346f4f755bd269a4f0f866738416c930 | Manifest: deps, data, assets, auto_install |
| E2 | base_setup/__init__.py | 373b1d07b83190f9c39a471a8b4d18ec2f75bb99 | Package imports |
| E3 | base_setup/models/__init__.py | b639ed0659740e3bd156d3ccdcf00cff2729c4b7 | Model file list |
| E4 | base_setup/controllers/__init__.py | 72e10793996ae31ba335216a5485e2ef063e9315 | Controller file list (kpi, main) |
| E5 | base_setup/models/res_config_settings.py | 7de297811c8722411552e9bdc4ba12b1d2201029 | General Settings fields, module toggles, actions, counters |
| E6 | base_setup/models/res_users.py | ba102d652e5cc2ad3b7af2f9b860897427ae7c23 | Bulk user invite by e-mail list |
| E7 | base_setup/models/ir_http.py | 4e7bb7df171c1c59592178b01f34d4fe5d00cd47 | Session info flag for internal users |
| E8 | base_setup/models/kpi_provider.py | 4211916c589872d4bc4597f601fba0fbfa2b1d67 | Abstract KPI provider extension point |
| E9 | base_setup/controllers/main.py | cce2c3f7609f7659ca0e034ba4e34a10014f4b32 | Settings dashboard JSON routes |
| E10 | base_setup/controllers/kpi.py | 69c9c21c1aa03bb90589d7c56f5c5b9bee6fe3e8 | Unauthenticated multi-DB KPI summary route |
| E11 | base_setup/data/base_setup_data.xml | e0d02590384d7e6a23dd6287b227ffb13358fbac | Seed config param `base_setup.show_effect` |
| E12 | base_setup/views/res_config_settings_views.xml | f97b9b257d32480312e4ca826fed780ee99ca19e | General Settings form, action, menu |
| E13 | base_setup/views/res_partner_views.xml | db3f0c946dbeaceadae7e83432baa1c85bf4e311 | Partner kanban: tags shown |

Blob count (this module): 13.

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: "Initial Setup Tools" — hosts the General Settings surface used to configure a new database and to toggle installation of optional feature modules. Depends on `base`, `web`. `auto_install` and `installable` true; LGPL-3; backend JS assets under `static/src/views`. [E1]
2. WHY: acts as the anchor page other modules extend (e.g. `auth_signup` inherits its settings form). [E12]
3. Manifest lists no security files. [E1]

### 2.2 Data (models, inheritance, key fields, identity/uniqueness)
4. One new model: `kpi.provider` (abstract, no storage) exposing an empty KPI summary hook for other modules to override. [E8]
5. Inherited: `res.config.settings` (transient), `res.users`, `ir.http`. No new stored business fields and no uniqueness constraints declared. [E3, E5–E7]
6. Settings fields — categories: (a) company context (`company_id` required, root-company flag, name, address summary, country code/groups, report footer and layout — related to company); (b) `module_*` install toggles (import, Google/Microsoft calendar, mail plugin, OAuth, LDAP, inter-company, VoIP, Unsplash, SMS, partner autocomplete, geolocalize, reCAPTCHA, Turnstile, Google address autocomplete); (c) group toggle `group_multi_currency` (implies `base.group_multi_currency`); (d) config-param fields `show_effect`, `profiling_enabled_until`; (e) computed counters (companies, internal users, installed languages). [E5]
7. RISK: related fields on settings (report footer, layout) write through to the company record — settings is not a pure param store. [E5]

### 2.3 Business rules / states / lifecycle / exceptions
8. Bulk invite (`web_create_users`): normalises e-mails; reactivates matching archived users (by login or normalized e-mail) instead of duplicating; creates new users with login = normalized e-mail, marking context so a valid signup token is prepared. Raises if the normalized-email field is absent (requires the Discuss/mail layer). [E6]
9. Default-groups action: if the "default access for new users" group reference is missing, it is created on demand and registered as noupdate data, then opened for editing. WHY: governs rights granted to newly created internal users. [E5, E12]
10. Counters use privileged counts (all companies; internal = non-share users). Active-user counter in the model does not filter on active flag, whereas the dashboard route filters active=true — potential count divergence between surfaces. [E5, E9]
11. Document layout edit returns nothing when no external layout is set. [E5]

### 2.4 Security
12. General Settings menu restricted to `base.group_system`; several blocks/buttons restricted to `base.group_no_one` (developer mode) or `base.group_multi_company`. [E12]
13. `/base_setup/data` (auth=user) enforces `base.group_erp_manager` explicitly, then runs raw SQL counts of active internal users and "pending" users (no login-log rows) and returns up to 10 pending ids/logins. [E9]
14. `/base_setup/demo_active` (auth=user) returns whether any module has demo data — no group check observed. [E9]
15. `/kpi/summary` is `auth='none'`, no session save; accepts up to 500 [db, api_key] pairs; per DB it verifies version series and an RPC-scoped API key, silently omitting DBs that are missing, mismatched or fail auth (explicit anti-enumeration intent); returns KPI provider output plus internal users list (id, name, login, last login) and provider errors. Provider calls are rolled back after each call. RISK for A1: unauthenticated endpoint that exposes user identity data when a valid key is supplied; cross-database reach on the same server. [E10]
16. KPI providers are discovered from any addon manifest key `kpi_providers` via dynamic import; invalid entries logged and skipped; result cached per worker. RISK: extension point loads code by manifest declaration. [E10]
17. `show_effect` session flag only emitted to internal users. [E7]

### 2.5 UI surfaces (names only)
18. Action `action_general_configuration` (path "settings"), menu `menu_config` "General Settings" under Administration. [E12]
19. Settings blocks: Users, Languages, Companies, Contacts, Integrations, Performance, About; settings ids include `invite_users_setting` (widget `res_config_invite_users`), `active_user_setting`, `access_rights`, `languages_setting`, `company_details_settings`, `document_layout_setting`, `companies_setting`, `inter_company`, `module_auth_oauth`, `module_auth_ldap`, `allow_import`, `mail_pluggin_setting`, `sms`, `recaptcha`, `partner_autocomplete`, `google_address_autocomplete`, `unsplash`, `feedback_motivate_setting`, `profiling_enabled_until`. Buttons: Manage Users, Add/Manage Languages, Update Info, Manage Companies, Configure/Edit/Preview Document Layout, Default Access Rights, Manage API Keys. [E12]
20. Routes: `/base_setup/data`, `/base_setup/demo_active`, `/kpi/summary`. [E9, E10]
21. Partner kanban shows category tags. [E13]

### 2.6 Jobs / config
22. No crons. [E1]
23. Config params: `base_setup.show_effect` (seeded True, noupdate, forcecreate False), `base.profiling_enabled_until` (settings-bound). [E5, E11]
24. Feature toggles are the `module_*` booleans (install/uninstall triggers handled by base settings machinery, not in this module). [E5]

## 3. Cross-module edges
- `auth_signup` extends settings form, overrides `/base_setup/data` (resend flag) and `web_create_users` (re-invite). Invite side effects (token, mail) come from `auth_signup`, not base_setup. [E6, E9]
- `base`: res.config.settings machinery (module/group/param binding), groups `group_system`, `group_erp_manager`, `group_no_one`, `group_multi_company`, `group_multi_currency`, API key check helper, user/company/language actions.
- `web`: document layout configurator and report preview actions. [E12]
- `mail`/Discuss: required for normalized e-mail in bulk invite. [E6]
- Optional modules referenced only as toggles (auth_oauth, auth_ldap, sms, google_recaptcha, website_cf_turnstile, etc.).

## 4. Evidence gaps / contradictions
- G1: Active-user count basis differs (model vs dashboard route) — see #10.
- G2: Dashboard route uses a controller-level env cursor; its binding in core `http.Controller` not fetched/verified.
- G3: Base settings machinery (how `module_*`/`implied_group`/`config_parameter` apply) lives in `base/models/res_config.py`; not analysed beyond one cross-reference in the auth_signup file.
- G4: API-key verification helper (`_check_apikey_credentials`) and `Manifest` loader in core not fetched.
- G5: Static JS (settings widgets, invite widget) not reviewed per instruction.
- G6: `/base_setup/demo_active` lacks an explicit group check in source; exposure beyond logged-in users not implied (auth=user).

## 5. Limitations
- Source presence ≠ runtime reachability. No execution, no runtime observation, no Formal Coverage claim.
- No GMVQ QIDs answered; evidence only for A1.
- Single commit anchor; no version comparison.
