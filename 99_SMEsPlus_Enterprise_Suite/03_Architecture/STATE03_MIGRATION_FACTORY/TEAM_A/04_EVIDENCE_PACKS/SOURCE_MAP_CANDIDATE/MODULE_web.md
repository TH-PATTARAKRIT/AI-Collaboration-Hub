# Source Map (candidate) — `web`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `web` |
| Display name | Web |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e34b9cf41fb4219f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/web/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (29): `api_doc`, `attachment_indexation`, `auth_oauth`, `auth_passkey`, `auth_password_policy`, `auth_signup`, `auth_totp`, `barcodes`, `base_iban`, `base_import`, `base_import_module`, `base_setup` … (+17)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (8): `iot_base`, `test_http`, `test_import_export`, `test_orm`, `test_read_group`, `test_rpc`, `test_search_panel`, `test_testing_utilities`
- Custom / third-party modules that declare a dependency (name — license only) (18): `nthub_binary_field_preview` — LGPL-3, `scgl_jasper_api` — LGPL-3, `l10n_th_withholding_tax_cert_form` — AGPL-3, `oi_action_file` — OPL-1, `scgl_custom_title_and_favicon` — LGPL-3, `report_xlsx` — AGPL-3, `oi_pdf_viewer` — OPL-1, `hide_odoo_menu` — LGPL-3, `oi_jasper_report` — OPL-1, `date_range` — LGPL-3, `import_bridge_axis` — OPL-1, `web_chatter_resize` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 1, server actions 1, reports 3, mail templates 0, scheduled jobs 0, wizards 2, web routes 60
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `base.document.layout` (Company Document Layout); `res.users.settings.embedded.action` (User Settings for Embedded Actions)
- Objects extended from other modules (13): `ir.model`, `ir.http`, `base`, `res.company`, `res.users.settings`, `ir.ui.menu`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.ui.view`, `properties.base.definition`, `res.users`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `base.document.layout` ← Community: `account`, `l10n_ca`, `l10n_cz`, `l10n_din5008`, `l10n_fr_account`, `l10n_ma`, `l10n_mu_account`, `l10n_my_ubl_pint`, `l10n_sk`, `sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.model`, `ir.http`, `base`, `res.company`, `res.users.settings`, `ir.ui.menu`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.ui.view`, `properties.base.definition`, `res.users`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 47 of 47 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — web
Source revision: 19.0.post20260921 | Module: "Web" (web/__manifest__.py:5), category Hidden (:6), auto_install (:15), depends on base only (:14). Framework/infrastructure module (brief note). Basis: static reading of manifest, security files, login/session/database controllers, selected models; the large client code base was not read.

## A. Capabilities and optionality
- A1. Provides the browser client of the system: page shell, menus, views, field widgets, list/form/kanban/pivot/graph engines, dialogs, translations, assets bundling, report layout, and the endpoints the client calls. web/__manifest__.py:8-13
- A2. Server-side query helpers used by all screens: paged search-and-read, combined save-and-read, spec-driven read, grouped reads and progress-bar aggregation, side-panel category/filter counts, batch onchange. web/models/models.py:66,90,109,702,802,1370,1646,1989
- A3. Login and session endpoints: login page (password), session authenticate/check/destroy/logout, "become administrator" switch for system users, health check. web/controllers/home.py:103-188; web/controllers/session.py:25-90
- A4. Database manager endpoints (create, duplicate, drop, backup, restore, change master password, list) guarded by the server master password; login page can hide the manager when database listing is disabled. web/controllers/database.py:59-179; web/controllers/home.py:147-148
- A5. Generic data endpoints for the client: RPC method call and button call for logged-in users, export to CSV/Excel with field discovery, pivot export, file/image serving with cache keys, attachment upload, report rendering/download, company logo, web app manifest and service worker, vcard download (contact card). web/controllers/dataset.py:28-35; web/controllers/export.py:291-688; web/controllers/binary.py:53-260; web/controllers/report.py:26-153; web/controllers/webmanifest.py:63-94
- A6. Company document layout designer (transient wizard: logo, header/footer, company details, colours, layout, font, paper format, live preview), saved back to the company; style bundle for reports regenerated when style fields change. web/models/base_document_layout.py:18-60,252-254; web/models/models.py:2231-2260
- A7. Per-user memory of side "embedded actions" (order/visibility), one row per user setting, action and record. web/models/res_users_settings_embedded_action.py:5-20
- A8. Web app name setting (parameter web.web_app_name) shown in Settings. web/models/res_config_settings.py:10
- A9. Neutralised-database banner, developer profiling switch, debug-mode parsing from URL. web/views/neutralize_views.xml; web/controllers/profiling.py:12-23; web/models/ir_http.py:51-60
- A10. Optionality: auto_install True with dependency only on base → present in every database; ~40 modules depend on it directly (manifest scan, includes auth_totp, auth_passkey, auth_password_policy, auth_signup, bus, onboarding, resource, portal, project, hr, mail_plugin, spreadsheet, web_hierarchy, website-related). web/__manifest__.py:14-15

## B. Objects and relationships
- B1. Own persistent objects are few: embedded-action settings (linked to user settings and window actions; removed with either) and transient wizards (document layout). web/models/res_users_settings_embedded_action.py:8-16; web/models/base_document_layout.py:18
- B2. It extends core objects rather than owning business data: models (base), companies, users and user settings, partners (vcard), views and menus, HTTP dispatch, image/QWeb rendering, model registry lookups, properties definitions. Server files: web/models/ir_model.py, ir_http.py, models.py, res_users.py, res_users_settings.py, ir_ui_menu.py, ir_ui_view.py, res_partner.py, properties_base_definition.py.
- B3. No lifecycle/states.

## C. Validations, security, audit — authentication implications
- C1. Login flow: the password credential is authenticated through the session; on success the redirect helper decides between full session and second-step (MFA) URL; failures show a generic "Wrong login/password". web/controllers/home.py:126-139; base/models/res_users.py:784-800; web/controllers/utils.py:236-250
- C2. Extension hook for login captcha: password logins call a captcha check unless skipped; other credential types (e.g., passkey) are not captcha-checked. web/models/res_users.py:33-36; web/controllers/home.py:130-131
- C3. Credential parameter whitelist (login, password, type) — modules extend it (passkey adds its response). web/controllers/home.py:31,128; auth_passkey/controllers/main.py:7
- C4. Session authenticate endpoint returns no user when the account needs a second factor ("uid: null") instead of leaking a half-logged session (TEST for TOTP) web/controllers/session.py:44-49; auth_totp/tests/test_totp.py:132-157.
- C5. Web client shell refuses non-internal users (redirect to login-success page), checks session validity, marks the page no-store and not frameable, and rotates a cache secret when security-relevant user data change (password, 2FA). web/controllers/home.py:51-81
- C6. Database manager is protected by the master password; if the master password is still the shipped default, the first supplied value is set as the new master password. web/controllers/database.py:71-77,94-98,111-115; database names are pattern-checked. web/controllers/database.py:78-79
- C7. RPC endpoints require a logged-in user (auth=user); ordinary model access rights and record rules apply on every call. web/controllers/dataset.py:28-35
- C8. Table access: document-layout wizard — Settings administrators (create/read/write); embedded action settings — internal users full but restricted by rule to own entries; Settings administrators see all. web/security/ir.model.access.csv:2-3; web/security/web_security.xml:3-23
- C9. Embedded-action ordering/visibility strings must be lists of integers or "false" without duplicates (validation error). web/models/res_users_settings_embedded_action.py:18-50 (constraint methods)
- C10. Company scoping: only through the company style bundle (built for all companies at once) and the wizard's company field; no company record rules in this module. web/models/models.py:2244-2251
- C11. Auditing: no audit trail of its own; the base login logs success/failure; profiling and debug are session-scoped. base/models/res_users.py:760-782

## D. Handoffs
- D1. Authentication, MFA, API keys: base (res.users) with auth_totp, auth_passkey, auth_ldap, auth_oauth, auth_signup, auth_timeout (see their notes).
- D2. Real-time notifications: bus. Guided setup panels: onboarding. Org-chart view: web_hierarchy. Working calendars: resource.
- D3. Documents/reports business content (invoices, orders) use the layout and report controllers but are owned by their modules (account, sale, etc.); modules extending the document layout wizard: account, base, l10n_ca, l10n_cz, l10n_din5008, l10n_fr_account, l10n_ma, l10n_mu_account, l10n_my_ubl_pint, l10n_sk, sale (grep).
- D4. Modules extending the login controller (Home): auth_passkey, auth_signup, auth_timeout, auth_totp, bus, http_routing, portal (grep).
- D5. Modules overriding captcha/bootstrap hooks: mail_bot (grep for hook names).

## E. Configuration/defaults that change outcomes
- E1. Server option list_db: hides the database manager link on the login page when off. web/controllers/home.py:147-148
- E2. Parameter web.web_app_name; debug mode via URL parameter with an allowed list. web/models/res_config_settings.py:10; web/models/ir_http.py:51-60
- E3. Company style fields (layout, font, colours) trigger regeneration of the shared report style bundle. web/models/models.py:2231-2251

## F. Effective extension path (module names only)
- Depend on web directly: api_doc, attachment_indexation, auth_oauth, auth_passkey, auth_password_policy, auth_signup, auth_totp, barcodes, base_iban, base_import, base_import_module, base_setup, bus, google_address_autocomplete, hr, html_editor, http_routing, iap, iot_base, mail_plugin, onboarding, portal, project, resource, spreadsheet, transifex, utm, web_hierarchy, web_tour, website (plus test_* modules). Transitively nearly all modules (668 in dependency scan).
- ir.http is extended by 42 modules (inheritance scan count).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side JavaScript behaviour (views, widgets, services); only file inventory known.
- UNKNOWN — EVIDENCE INSUFFICIENT: export permission gating (whether a separate export right exists) — export routes require login only in the lines read (web/controllers/export.py:291-688); no group check seen but file not read fully.
- UNKNOWN — EVIDENCE INSUFFICIENT: profiling endpoint access control (route is public; enforcement is inside the profile model, not read). web/controllers/profiling.py:12
- UNKNOWN — EVIDENCE INSUFFICIENT: 30 Python test modules in web/tests were not read.

