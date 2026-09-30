> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: hide_odoo_menu

## 0. Header
- Module: hide_odoo_menu
- License (confirmed in manifest): LGPL-3 (addons/hide_odoo_menu/__manifest__.py:19)
- Author (manifest): Phatthraphon Chantaprasit (addons/hide_odoo_menu/__manifest__.py:5)
- Version (manifest): 1.0 (addons/hide_odoo_menu/__manifest__.py:4) - not in Odoo 19 series format
- Path: addons_Extramodule/addons/hide_odoo_menu
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Removes the "My Odoo.com Account" entry from the backend user menu (manifest summary, hide_odoo_menu/__manifest__.py:7). Branding/white-label step so users are not directed to the vendor account portal.

## 2. Attachment to CORE
- Depends on web (manifest:8). Pure client-side module: no Python.
- Registers a small client service named "menuremove" whose start step removes the user-menu registry item "odoo_account" (hide_odoo_menu/static/src/js/user_menu_patch.js:9-19). Core item registered at core:web/static/src/webclient/user_menu/user_menu_items.js:143 (definition core:web/static/src/webclient/user_menu/user_menu_items.js:72-76, opens the vendor account page).
- Effect: removes a core UI entry; no core method overridden. Not a security control (the underlying route is not disabled). ALTERS CORE CONTROL: not applicable.
- Unused imports of UserMenu and patch are present in the script (js:1-2); no patch is applied.

## 3. New objects, security, automation, external calls
- None (no models, ACLs, cron, external calls). Asset registered in web.assets_backend (manifest:12-18).

## 4. Odoo 19 compatibility
- Registry category user_menuitems and key odoo_account exist in core 19 (core:web/static/src/webclient/user_menu/user_menu_items.js:138-143). Registry remove method exists (core:web/static/src/core/registry.js:176).
- Service name "menuremove" is also used by hide_smesplus_menu (identical script apart from line endings); core registry add throws if a key already exists (core:web/static/src/core/registry.js:103-105). Installing both would therefore risk a duplicate-key error - see section 5.

## 5. Custom-to-custom dependencies
- None declared, but CONFLICT RISK with hide_smesplus_menu: same service key "menuremove" (hide_odoo_menu/static/src/js/user_menu_patch.js:20 vs hide_smesplus_menu/static/src/js/user_menu_patch.js:20).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether both modules are intended to be installed together.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether removing the item in a service start step is reliably applied before the user menu first renders.
