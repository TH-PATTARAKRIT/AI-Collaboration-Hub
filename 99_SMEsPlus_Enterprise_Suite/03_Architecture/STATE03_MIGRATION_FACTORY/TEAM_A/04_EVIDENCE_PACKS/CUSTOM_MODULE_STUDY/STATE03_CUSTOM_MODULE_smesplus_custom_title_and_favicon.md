> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_custom_title_and_favicon

## 0. Header
- Module: smesplus_custom_title_and_favicon
- License (confirmed in manifest): LGPL-3 (smesplus_custom_title_and_favicon/__manifest__.py:17)
- Author (manifest): SMEsPlus (smesplus_custom_title_and_favicon/__manifest__.py:16); file header credits Kolpolok Ltd. (smesplus_custom_title_and_favicon/__manifest__.py:4-5)
- Version (manifest): 19.0.0.0.2 (smesplus_custom_title_and_favicon/__manifest__.py:11)
- Path: addons_Extramodule/addons_extra/smesplus_custom_title_and_favicon
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Branding: same as scgl_custom_title_and_favicon — custom browser tab title from a General Settings field on the login page and web client, plus a per-company favicon chosen on the company form (models/ir_ui_view.py:12-18; models/res_config.py:14-29; models/res_company.py:18; views/res_company_view.xml:8-10).
- Default title "SMEsPlus" loaded once on install under key `smesplus.web.base.title` (data/default_title.xml:5-8; models/res_config.py:9).
- Menu/edition hiding: none. Access rights: not affected (no groups, ACLs, menus).
- Relationship: file-by-file the module matches scgl_custom_title_and_favicon except author, asset path, parameter key, data-file root tag (`odoo` instead of legacy `openerp`, data/default_title.xml:2) and parameter record id (compared by directory diff of the two module folders).

## 2. Attachment to CORE
- Depends declared: web only (manifest:19-21).
- Overrides and core touchpoints (same as sibling; pointers here):
  - `ir.ui.view._render_template` (models/ir_ui_view.py:12-18): ADDS before core, sets the page title for the login and web-client bootstrap templates from the system parameter (read with elevated access, :17). Core method core:base/models/ir_ui_view.py:2545; templates core:web/views/webclient_templates.xml:136, :275. No ALTERS CORE CONTROL.
  - Core layout template `web.layout` (views/favicon.xml:3-12): REPLACES the core favicon link node (core:web/views/webclient_templates.xml:23), dropping the core's optional caller-supplied icon variable (inference).
  - `res.company` (models/res_company.py:11-18): ADDS `custom_favicon`, default image from core (core:base/static/img/res_company_logo.png).
  - `res.config.settings` (models/res_config.py:11-29): ADDS a setting; `get_values`/`set_values` ADD after core with elevated parameter access. Save is administrator-only in core (core:base/models/res_config.py:367-368).
  - Front-end patch of the web client keeping the server title (static/src/js/custom_title.js:6-12).

## 3. New objects, security, automation, external calls
- New field `custom_favicon`; no new models, ACLs, groups or rules. Favicon per company (views/favicon.xml:8); title global (models/res_config.py:9).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- All referenced core hooks exist in Community 19 (see pointers above).
- Undeclared dependency on base_setup (views/res_config.xml:8 vs manifest:19-21); core base_setup depends on web (core:base_setup/__manifest__.py:14).

## 5. Custom-to-custom dependencies
- None declared. Duplicate/overlap with scgl_custom_title_and_favicon and web_window_title (same `web_window_title` settings field, same overriding method). Installing more than one at the same time is unsafe to assume (inference).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which title module is installed in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the favicon is readable by anonymous users on the login page.
