> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: web_window_title

## 0. Header
- Module: web_window_title
- License (confirmed in manifest): LGPL-3 (web_window_title/__manifest__.py:3)
- Author (manifest): renjie <i@renjie.me> (web_window_title/__manifest__.py:6)
- Version (manifest): 19.0.0.0.1 (web_window_title/__manifest__.py:10)
- Path: addons_Extramodule/addons_extra/web_window_title
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Branding: lets an administrator set the browser tab title (General Settings, "Window" block, field "Title") and applies it to the login page and the main web client (models/res_config.py:11-29; models/ir_ui_view.py:12-18; views/res_config.xml:10-27; static/src/js/web_window_title.js:6-12).
- Demo data sets the title to "Demo" (data/demo.xml:5-8, demo mode only, manifest:12-14).
- Menu/edition hiding: none. Access rights: not affected.

## 2. Attachment to CORE
- Depends declared: base_setup (manifest:11).
- Core touchpoints:
  - `ir.ui.view._render_template` (models/ir_ui_view.py:12-18): ADDS before core — sets the `title` value for the login and web-client bootstrap templates from the system parameter `web.base.title` read with elevated access (:17). Core: core:base/models/ir_ui_view.py:2545; templates core:web/views/webclient_templates.xml:136, :275; core title default core:web/views/webclient_templates.xml:22. No ALTERS CORE CONTROL.
  - `res.config.settings` (models/res_config.py:11-29): ADDS field `web_window_title`; `get_values`/`set_values` ADD after core. Save is administrator-only in core (core:base/models/res_config.py:367-368).
  - Settings view: inherits the base_setup settings form, inserts a block before the languages section (views/res_config.xml:8-10; core:base_setup/views/res_config_settings_views.xml:34).
  - Front end: patches the main web client start-up to keep the server-rendered title in the browser title (static/src/js/web_window_title.js:6-12; core title service core:web/static/src/core/browser/title_service.js:24).
- The module registers its script as web.assets_backend (manifest:21-25).

## 3. New objects, security, automation, external calls
- No new models/ACLs/groups/rules. Data: one system parameter `web.base.title` (models/res_config.py:9). The value is global, not per company.
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Comment in manifest says updated for Odoo 19 (manifest:10). Hooks used exist in Community 19 (pointers above). The parameter name `web.base.title` is not found in the Community `web`, `base_setup` or `base` folders (text search), i.e. it is defined only by this module.
- Alias in the script header `web.window.title` (static/src/js/web_window_title.js:1) is a legacy-style alias; effect in 19 not tested.

## 5. Custom-to-custom dependencies
- None declared. Same purpose and same settings field name as scgl_custom_title_and_favicon and smesplus_custom_title_and_favicon (different parameter keys). See those files; co-installation conflicts are inferred, not tested.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: which title module is installed in the deployed database.
