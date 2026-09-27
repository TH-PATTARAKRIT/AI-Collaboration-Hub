# G01 PLATFORM_BASE — Module `web` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T1 |
| Group | G01 PLATFORM_BASE |
| Module | `web` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web/`) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (breadth pass; JS client only counted, not studied, per brief) |

Nothing here is runtime proof. Source presence does not show runtime reachability. No Formal Coverage is claimed. No GMVQ QIDs are answered.

## 1. Evidence Pointer Table

| Path (addons/web/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 72f3f25791583968056ca4a42ab3e9cd13db9e93 | Deps, data list, asset bundles |
| `__init__.py` | 7d34c7c054abd3105d5bb41fe9674111e1c27c16 | Package imports |
| `models/__init__.py` | 6b4064172b54bf0353a21e7510c0cb3c5604ee8e | Model imports |
| `models/models.py` | 867fba726ae06ad57ce492901491e4f663897815 | Generic client-facing data API on every model and the company style hook |
| `models/ir_http.py` | bd03fa8e5e43ec580a63a068121f5a292215ac66 | Session info, debug handling, cookies |
| `models/base_document_layout.py` | 22081a0aee2b641f52103655180ae2e5ebdc3d4d | Document layout configurator (transient) |
| `models/res_users_settings_embedded_action.py` | d405c082b8d655edb935a36368a94130399868f2 | Per-user embedded-action prefs |
| `models/res_users_settings.py` | 1f12dcd09222c5b9e3013285c7304f730df111a8 | User settings extension |
| `models/res_users.py` | 77aa76a5ac7edfc1a2c7873b19b77a6d0c9932ed | User name-search ordering, captcha hook |
| `models/ir_model.py` | fe8a370758c5eb66d79e3d5e0bf4de8cd27128b4 | Model selector and definitions |
| `models/ir_ui_menu.py` | 5dd7e44ef837c66b1b019077d8ffda5418b1ae85 | Menu payload for client |
| `models/ir_ui_view.py` | 62d09e10d7b206841c174d9f84a7addf6c1de9d7 | View-type info |
| `models/ir_qweb_fields.py` | a341e7a20fb5754922ec183f4671b848a25ac59f | Image field URL rendering |
| `models/res_partner.py` | cb1f489a49e2a4cf86a695df9c40d9a6f9c29a7d | vCard build (optional lib) |
| `models/res_config_settings.py` | e8e0ee36cbdad638ee67fef8b54ef92bcade557a | Web app name setting |
| `models/properties_base_definition.py` | 0c8fb5efe3664d9cb5293ac223627693d2e38f0a | Properties definition read |
| `controllers/__init__.py` | aba8eb68511c5372d8b1e03e36dbbfe12af23824 | Controller imports |
| `controllers/main.py` | 2b2732ff3df9c4784f903fcd731a57c85a02992d | Compatibility shim |
| `controllers/utils.py` | c619741d173d38d54fd9dba49ceb48ca08476d40 | Action path resolution helpers |
| `controllers/action.py` | 384f3063b85831674c89d964d42b90cecf91ea26 | Action load/run routes |
| `controllers/binary.py` | 7b7b84f771eeb5a0f096500f7530a48c956f41b1 | Content/image/asset/upload routes |
| `controllers/database.py` | 434b915ceb3a935c1fdbee248d4a4ed7a8533b48 | Database manager routes |
| `controllers/dataset.py` | a1c5bdd99c32a38e5e2e0b8f4ea682aa42c50823 | Generic RPC call routes |
| `controllers/domain.py` | 6a71bbe176dfc39cc9f944f1a9b95ddf770219b3 | Domain validation |
| `controllers/export.py` | cb750f193c5548fe70a01422d644c66805a20e69 | CSV/XLSX export |
| `controllers/home.py` | 292aaa75a2c35b71acb3c97488a6dc2c96309c9f | Webclient entry, login, become, health |
| `controllers/json.py` | 1d1b408ea56cd92249b743012dd6eb039caba38d | Experimental JSON view routes |
| `controllers/model.py` | 9608975d383138ee9f579b3a4ec695dedfa79126 | Model definitions route |
| `controllers/pivot.py` | a687d2d1dbd443c0b49c2e1b259a2dd2c9767bb1 | Pivot XLSX export |
| `controllers/profiling.py` | ef5fdbba3f0caa489e8df0b22132687b9af96e71 | Profiling toggle/viewers |
| `controllers/report.py` | 59346f1c49a260ec097fdd6c6fd7ab999d63d07a | Report render/download/barcode |
| `controllers/session.py` | 2fbcfc872381751ac3336b2549babcca159d76cc | Session auth/info/logout |
| `controllers/vcard.py` | b543a25f12c66f7ccb9b89d5cf4bc9f65ee77c56 | Partner vCard download |
| `controllers/view.py` | dfc38f00e6b214eedca4bf5754b422a3cfc67e50 | Custom view edit |
| `controllers/webclient.py` | e94d5478a1d0836b7b0b8057dfca1b4142cb845c | Translations, version, bundles, tests |
| `controllers/webmanifest.py` | f5ecf5029cbde89d3f06997b4328fa11348f2b54 | PWA manifest, service worker, scoped app |
| `security/ir.model.access.csv` | a46f838bbce724d26c3b0e285c7a9f3c97c12f23 | ACLs |
| `security/web_security.xml` | 58d06cd00cd5b8d2730c702bff9c6cce6f7533bd | Record rules |
| `views/webclient_templates.xml` | a34e38e46f8f698ef196004676c4cf08b6f77dc5 | Layout/login/bootstrap templates |
| `views/report_templates.xml` | f86d660c4250c133351fd647e75195edc4cc766d | Report layouts, preview report actions |
| `views/base_document_layout_views.xml` | 674972008e0644cf719e9aca062c9ba0d829881d | Layout configurator view and action |
| `views/partner_view.xml` | 0378f5086df2c03f560c0a97557fd99023e00e95 | vCard server action bound to partner |
| `views/speedscope_template.xml` | e87c024f2d40fd596263ace37919202211145755 | Profiler viewer template |
| `views/memory_template.xml` | 5c7dd581935db4cef1a3cae638acbb944e3701bf | Memory profile template |
| `views/speedscope_config_wizard.xml` | b4fc68ae53218b306de2a8be23b99fec6cda7501 | Profiler config template |
| `views/neutralize_views.xml` | 19ad2cd215825bca9b37e38f971541ec017f5383 | Neutralized-DB banner (inactive by default) |
| `views/ir_ui_view_views.xml` | b196530fcaf54e03e38a989b365e477cd67e055d | View form extension |
| `data/ir_attachment.xml` | 33993487161c6001b365d2bbc377878291884d73 | Image placeholder attachment |
| `data/report_layout.xml` | 3f1d72d6896752ad6218469b90c361783a57c180 | Report layout records and company style attachment |

Blobs cited: **49**.

## 2. Findings by Card Section

### 2.1 Manifest / deps / purpose
1. WHAT: this is the core web client module. It depends only on `base`, is `auto_install`, and its category is Hidden. WHY: it is the platform foundation that every UI module assumes. RISK: any platform-base redesign has to supply the same always-present client and RPC layer. (`__manifest__.py`)
2. The manifest declares 13 data files (2 security, 9 views, 2 data) and about 29 named asset bundles (backend, frontend, lazy/dark, report, tests, unit tests, clickbot). It contains about 268 static-asset path lines. JS/SCSS were counted only and not studied. (`__manifest__.py`)

### 2.2 Data (models, inheritance, key fields, identity)
3. One new persistent model: `res.users.settings.embedded.action`. It stores per-user preferences (order, visibility, top-bar visibility) for embedded actions, keyed by user-setting, window action and optional record id. Identity: a unique constraint on (user_setting_id, action_id, res_id). Both links cascade on delete. (`models/res_users_settings_embedded_action.py`)
4. One new transient model: `base.document.layout`. It is a configurator whose fields are mostly related to company report-branding fields (logo, header/footer, company details, paper format, layout, font, colors, background) and to company contact fields (read-only). It can also take primary/secondary colors from the logo. (`models/base_document_layout.py`)
5. Inheritance of `base` (all models): adds a generic client data API (spec-driven read, search-read, save, multi-save, resequence, read-group with unfold limits, grouping sets, progress bar, search-panel ranges, batched onchange, translation override). A constant caps the number of auto-opened groups at 10 unless the context overrides it. (`models/models.py`)
6. Inheritance of `res.company`: when a create or write touches layout, font or colors, one shared company-style attachment is re-rendered for all companies. (`models/models.py`, `data/report_layout.xml`)
7. Other extensions: `res.users.settings` (one2many to the embedded prefs, plus get/set API); `res.users` (current user moved first in name search; captcha hook for password credentials); `ir.model` (model selector limited to internal users with read access, non-transient and non-abstract models); `ir.ui.menu` (client menu payload); `ir.ui.view` (view-type icons); `ir.qweb.field.image`/`image_url` (cache-busted image URLs); `res.partner` (vCard); `res.config.settings` (`web_app_name`); `properties.base.definition` (read after a model access check). (respective `models/*.py`)
8. Seed data: 7 `report.layout` records, 1 company-style `ir.attachment`, 1 image placeholder attachment. (`data/*.xml`)

### 2.3 Business rules / states / lifecycle / exceptions
9. Embedded-action preference strings must hold unique ids that are integers or "false". A violation raises a validation error. Set is an upsert: it finds an existing row, otherwise creates one. (`models/res_users_settings_embedded_action.py`, `models/res_users_settings.py`)
10. Generic onchange checks write access, or create access for new records, except on `res.users`, where self-writable fields apply. RISK: the self-edit exemption is a special case that a redesign must control on purpose. (`models/models.py` ~L2027)
11. Search-panel range methods raise a user error for unsupported field types. `fill_temporal` cannot be combined with limit or offset. (`models/models.py`)
12. The action loader raises a dedicated missing-action error. Custom view edit refuses a view that the current user does not own. Domain validation runs an EXPLAIN-only query and returns a boolean. (`controllers/action.py`, `controllers/view.py`, `controllers/domain.py`)
13. No state machine or document lifecycle is defined in this module (it is a platform layer).

### 2.4 Security
14. ACLs: `base.document.layout` gives read, write and create to `base.group_system`, with no unlink. The embedded-action model gives full CRUD to `base.group_user`. (`security/ir.model.access.csv`)
15. Record rules: internal users see only embedded-action rows linked to their own user settings. `base.group_system` has an unrestricted rule. (`security/web_security.xml`)
16. Controllers use several auth levels: `auth='user'` (dataset call_kw/call_button, action, export, report, session, model definitions, pivot export); `auth='public'` (/web/content, /web/image, assets, translations, bundle, manifest, barcode, set_profiling); `auth='none'` (/, /web, /odoo, login, health, filestore, company logo, database manager, fonts); `auth='bearer'` (`/json/1/...`). RISK: public or none routes depend on downstream record checks. A1 must check each route's enforcement, which this pass does not prove. (`controllers/*.py`)
17. Database manager routes (create/duplicate/drop/backup/restore/change_password) are `auth='none'`, POST, and `csrf=False`. They are gated by the master password: backup and restore call the check directly, and the others pass it to a service RPC. The `list_db` config also controls exposure. RISK: this is a high-impact admin surface outside tenant auth. (`controllers/database.py`, `controllers/home.py`)
18. `/web/become` lets a system-group user switch the session to the superuser and recompute the session token. RISK: this is a privilege-escalation surface limited only by the system group. (`controllers/home.py`)
19. Sudo sites exist in action resolution, attachment lookup in assets, domain validation `_search`, export property definitions, custom-view fetch (followed by an owner check), language list, the webmanifest menu lookup, config params, and company-hierarchy session info. RISK: each sudo needs an A1 check that a later guard exists. (`controllers/*.py`, `models/ir_http.py`)
20. Company controls: session info builds allowed companies and their ancestor hierarchy under sudo. The `cids` cookie is normalized, and it is cleared on logout. (`models/ir_http.py`)
21. Export: the `/json` route checks `base.group_allow_export`, and the session exposes that flag. No explicit check for this group was found in the source of `controllers/export.py`, but enforcement may exist elsewhere, possibly client-side or in `base` (**gap**). (`controllers/json.py`, `models/ir_http.py`)

### 2.5 UI surfaces (names only)
22. Routes (grouped): `/web/action/{load,run,load_breadcrumbs}`; `/web/dataset/call_kw`, `/web/dataset/call_button`; `/web/content*`, `/web/image*`, `/web/assets/*`, `/web/binary/upload_attachment`, `/web/binary/company_logo`, `/logo(.png)`, `/web/sign/get_fonts`, `/web/filestore/*`; `/web/database/{selector,manager,create,duplicate,drop,backup,restore,change_password,list}`; `/web/domain/validate`; `/web/export/{formats,get_fields,namelist,csv,xlsx}`; `/`, `/web`, `/odoo/*`, `/scoped_app/*`, `/web/webclient/load_menus`, `/web/login`, `/web/login_successful`, `/web/become`, `/web/health`, `/robots.txt`; `/json/*`, `/json/1/*`; `/web/model/get_definitions`; `/web/pivot/export_xlsx`; `/web/set_profiling`, `/web/speedscope/*`, `/web/profile_config/*`; `/report/<converter>/<name>[/<docids>]`, `/report/barcode*`, `/report/download`, `/report/check_wkhtmltopdf`; `/web/session/{get_session_info,authenticate,get_lang_list,modules,check,account,destroy,logout}`; `/web/partner/vcard` (+ legacy alias); `/web/view/edit_custom`; `/web/webclient/{bootstrap_translations,translations,version_info}`, `/web/tests*`, `/web/bundle/*`; `/web/manifest.webmanifest`, `/web/service-worker.js`, `/odoo/offline`, `/scoped_app`, `/scoped_app_icon_png`, `/web/manifest.scoped_app_manifest`.
23. Actions: `action_base_document_layout_configurator` (window); 3 preview `ir.actions.report` (internal/external/layout preview); server action "Download (vCard)" bound to `res.partner`. This module declares no menus. (`views/*.xml`)
24. Templates: layout, frontend layout, login family, webclient bootstrap, offline, scoped app, 7 external report layout variants plus internal/basic/minimal, and the neutralize banner (inactive). (`views/webclient_templates.xml`, `views/report_templates.xml`, `views/neutralize_views.xml`)

### 2.6 Jobs / config / toggles / integrations
25. No crons are declared in the manifest data.
26. Config parameters read: `web.max_file_upload_size`, `web.active_ids_limit` (default 20000), `web.quick_login`, `web.web_app_name` (also a settings field), `web.json.enabled` (JSON route gate, or the DB demo flag), `web.base.url`, `database.uuid`, `base_setup.show_effect`, `speedscope_cdn`. Server config keys: `list_db`, `x_sendfile`, `data_dir`, `server_wide_modules`, `test_enable`. (`models/ir_http.py`, `controllers/*.py`)
27. Debug modes are parsed from the `debug` query argument against an allowlist. Profiling can be toggled via a route that calls `ir.profile`. (`models/ir_http.py`, `controllers/profiling.py`)
28. Integrations: optional `vobject` library for vCard, where a missing library disables the feature with a warning; a wkhtmltopdf check route; a speedscope viewer from a CDN via config param; PWA manifest and service worker. (`models/res_partner.py`, `controllers/report.py`, `controllers/profiling.py`, `controllers/webmanifest.py`)

## 3. Cross-module Edges
- Hard dependency: `base` only.
- Models from `base` that this module extends: `base` (abstract), `res.company`, `res.users`, `res.users.settings`, `res.partner`, `res.config.settings`, `ir.http`, `ir.model`, `ir.ui.menu`, `ir.ui.view`, `ir.qweb.field.image`/`image_url`, `properties.base.definition`.
- Reverse extension points: `document_layout_save` is documented as meant to be overridden; `_on_webclient_bootstrap` and `_should_captcha_login` on users; `session_info` (extended by `web_tour`, see that file); the `web.assets_*` bundles that downstream modules append to; `/web_enterprise/partner/.../vcard` route alias (name only).
- References to `base_setup.show_effect` param and `base.group_allow_export` group point to other modules/data.

## 4. Evidence Gaps / Contradictions
- G-1: JS client (about 268 asset lines) was not studied (out of scope by brief). All client-side rules are unevidenced.
- G-2: Server-side `group_allow_export` enforcement for CSV/XLSX export was not found in `controllers/export.py`. A1 should check `base` and the client.
- G-3: Master-password enforcement for create/duplicate/drop is delegated to service RPC in `odoo/service` (outside `addons/web`) and was not read.
- G-4: `models/models.py` (2376 lines) and `controllers/export.py`/`json.py` were read by structural scan, not line by line.
- G-5: The static/ tree could not be listed (no API). Test files were not reviewed.
- No contradictions were observed.

## 5. Limitations
Static source only, at a single commit. No runtime, configuration or DB state was observed. Line references are approximate pointers. Findings are neutral abstractions and are not design recommendations.
