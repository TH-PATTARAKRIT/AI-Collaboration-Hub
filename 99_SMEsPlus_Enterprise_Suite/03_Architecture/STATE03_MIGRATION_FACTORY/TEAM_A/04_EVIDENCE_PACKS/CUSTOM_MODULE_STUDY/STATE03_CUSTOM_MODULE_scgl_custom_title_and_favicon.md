> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_custom_title_and_favicon

## 0. Header
- Module: scgl_custom_title_and_favicon
- License (confirmed in manifest): LGPL-3 (scgl_custom_title_and_favicon/__manifest__.py:17)
- Author (manifest): SCGLegacy (scgl_custom_title_and_favicon/__manifest__.py:16); file header credits Kolpolok Ltd. (scgl_custom_title_and_favicon/__manifest__.py:4-5)
- Version (manifest): 19.0.0.0.2 (scgl_custom_title_and_favicon/__manifest__.py:11)
- Path: addons_Extramodule/addons/scgl_custom_title_and_favicon
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Branding: sets a custom browser tab title (text chosen in General Settings) on the login page and the main web client, and a per-company browser tab icon (favicon) picked on the company form (models/ir_ui_view.py:12-18; models/res_config.py:14-29; models/res_company.py:18; views/res_company_view.xml:8-10).
- Default title value "SCGL" is written on install as a system parameter (data/default_title.xml:5-8, marked as loaded once only).
- Menu/edition hiding: none. Visibility/access rights: not affected (no groups, ACLs or menus touched).

## 2. Attachment to CORE
- Depends declared: web only (manifest:19-21).
- Core objects touched:
  - `ir.ui.view._render_template` (core:base/models/ir_ui_view.py:2545; called by the HTTP layer at core:odoo/http.py:1586): override `_render_template` (models/ir_ui_view.py:12-18) ADDS before core — for the login page and web client bootstrap templates (core templates core:web/views/webclient_templates.xml:136, :275) it injects a `title` value read from a system parameter with elevated access (:17). Replaces any title the core code supplied for those two templates (the core layout falls back to "Odoo" when no title, core:web/views/webclient_templates.xml:22). Not a control; no ALTERS CORE CONTROL.
  - Core layout template `web.layout` (views/favicon.xml:3-12): REPLACES the core favicon link node (core:web/views/webclient_templates.xml:23). The core node allows an override variable (`x_icon`) from callers; the replacement ignores it, so any caller-supplied icon on any page using this layout is lost (inference).
  - `res.company` (models/res_company.py:11-18): ADDS a binary field "Company Favicon", default the standard company logo image from core (file at core:base/static/img/res_company_logo.png).
  - `res.config.settings` (models/res_config.py:11-29): ADDS a text setting; `get_values` (:16-24) ADDS after core; `set_values` (:26-29) ADDS after core and stores with elevated access. Core settings save is restricted to administrators (core:base/models/res_config.py:367-368).
  - Company form `base.view_company_form` (views/res_company_view.xml:6): field added after the colour field (core colour field: core:base/views/res_company_views.xml:51).
  - Settings page: block inserted before the languages section of the base_setup settings view (views/res_config.xml:8-10; core:base_setup/views/res_config_settings_views.xml:34).
- Front end: a patch of the main web client that, at start-up, keeps the server-rendered title as a part of the browser title (static/src/js/custom_title.js:6-12; core client uses a title service at core:web/static/src/webclient/webclient.js:28 and `setParts` at core:web/static/src/core/browser/title_service.js:24).

## 3. New objects, security, automation, external calls
- New field: `custom_favicon` on the company (models/res_company.py:18). No new models, no ACLs, no groups, no record rules.
- Company scoping: favicon is per company (URL built from the current company id, views/favicon.xml:8); title is one global system parameter (models/res_config.py:9, :20, :29), not per company.
- Data: system parameter key `scgl.web.base.title` (data/default_title.xml:6; models/res_config.py:9). The data file uses the legacy `openerp` root tag (data/default_title.xml:2); Community 19 still accepts it (core:odoo/tools/convert.py:665-667).
- Automation: none. External calls: none.
- The favicon is fetched through the generic image route for the company record (views/favicon.xml:8); whether the public login page can read it depends on core image access rules for that binary field (not checked).

## 4. Odoo 19 compatibility
- Confirmed present in Community 19: `_render_template`, `web.layout`, `web.login`, `web.webclient_bootstrap`, company form and colour field, `file_open` import, `base_setup` settings view with a languages block (pointers above).
- Undeclared dependency: the settings view inherits a view of the base_setup module (views/res_config.xml:8) although only web is listed (manifest:19-21). Core base_setup depends on web, not the reverse (core:base_setup/__manifest__.py:14; core:web/__manifest__.py:14). Install would fail if base_setup is absent.
- Overlap: same setting field name and the same purpose as web_window_title and smesplus_custom_title_and_favicon, each storing under a different key. See section 5.

## 5. Custom-to-custom dependencies
- None declared.
- Functional duplicates/conflicts: smesplus_custom_title_and_favicon is a renamed copy (differences: author, asset path, parameter key `smesplus.web.base.title`, root tag `odoo` in the data file); web_window_title (third-party) declares the same `web_window_title` settings field with key `web.base.title` and the same `_render_template` override. Installing more than one makes several overrides of the same method and the same settings field name compete; the last loaded one decides the shown value (inference; not tested).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which of the three title modules is actually installed in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the company favicon URL is readable by anonymous users on the login page.
