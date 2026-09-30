> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: bh_hide_odoo_edition

## 0. Header
- Module: bh_hide_odoo_edition
- License (confirmed in manifest): LGPL-3 (addons/bh_hide_odoo_edition/__manifest__.py:19)
- Author (manifest): SCGL (addons/bh_hide_odoo_edition/__manifest__.py:6)
- Version (manifest): 19.0.1.0.0 (addons/bh_hide_odoo_edition/__manifest__.py:4)
- Path: addons_Extramodule/addons/bh_hide_odoo_edition
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Removes the edition/version/copyright notice ("Community Edition" text) from the General Settings page, as a branding/white-label step (manifest summary, bh_hide_odoo_edition/__manifest__.py:5).

## 2. Attachment to CORE
- Depends on base_setup (manifest:8). Two mechanisms:
  1. View inheritance on core view base_setup.res_config_settings_view_form: replaces the div with id "about" with nothing (bh_hide_odoo_edition/views/res_config_settings_view.xml:5-12). Core block being removed: core:base_setup/views/res_config_settings_views.xml:200-204 (contains the res_config_edition widget).
  2. Client template extension of the core widget template res_config_edition: sets the Setting element condition to always false (bh_hide_odoo_edition/static/src/templates/res_config_edition.xml:4-10). Core template: core:web/static/src/webclient/settings_form_view/widgets/res_config_edition.xml:3-4.
- Effect: REPLACES core About block with empty (view) and disables core widget rendering (template). No Python method overridden. Not an access control; ALTERS CORE CONTROL: not applicable (display only).
- The template file is listed in the backend asset bundle (manifest:12-18).

## 3. New objects, security, automation, external calls
- None: no models, fields, ACLs, groups, rules, cron or external calls.

## 4. Odoo 19 compatibility
- Referenced core view id base_setup.res_config_settings_view_form and div id "about" exist (core:base_setup/views/res_config_settings_views.xml:200). Template name res_config_edition exists (core:web/static/src/webclient/settings_form_view/widgets/res_config_edition.xml:3) and contains a Setting element (core line 4).
- Not checked: whether removing the about div via the view while the widget template also disabled produces any console warning.

## 5. Custom-to-custom dependencies
- None declared. Overlaps in effect with app_icon_hide (same target hidden by CSS).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether other places (e.g. the About dialog in the user menu, other pages) still display edition information.
