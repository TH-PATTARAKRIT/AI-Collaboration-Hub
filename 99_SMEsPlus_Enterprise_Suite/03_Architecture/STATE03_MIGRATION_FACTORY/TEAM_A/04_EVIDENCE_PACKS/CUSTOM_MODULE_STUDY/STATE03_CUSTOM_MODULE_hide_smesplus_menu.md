> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: hide_smesplus_menu

## 0. Header
- Module: hide_smesplus_menu
- License (confirmed in manifest): LGPL-3 (addons_extra/hide_smesplus_menu/__manifest__.py:19)
- Author (manifest): Phatthraphon Chantaprasit (addons_extra/hide_smesplus_menu/__manifest__.py:5)
- Version (manifest): 1.0 (addons_extra/hide_smesplus_menu/__manifest__.py:4) - not in Odoo 19 series format
- Path: addons_Extramodule/addons_extra/hide_smesplus_menu
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Same capability as hide_odoo_menu, re-badged: removes the "My Odoo.com Account" entry from the backend user menu (manifest summary says "Hide SMEsPlus user menu", hide_smesplus_menu/__manifest__.py:7; the code removes the core key odoo_account).

## 2. Attachment to CORE
- Depends on web (manifest:8). Client-side only; no Python.
- Registers a client service "menuremove" that removes the user-menu registry item odoo_account (hide_smesplus_menu/static/src/js/user_menu_patch.js:9-20). Core item: core:web/static/src/webclient/user_menu/user_menu_items.js:143.
- Effect: removes a core UI entry (display only). No core method overridden. ALTERS CORE CONTROL: not applicable.
- Script is functionally identical to hide_odoo_menu (differences are line endings only, per file comparison).

## 3. New objects, security, automation, external calls
- None. Asset in web.assets_backend (manifest:12-18).

## 4. Odoo 19 compatibility
- Registry category and key exist in core 19 (core:web/static/src/webclient/user_menu/user_menu_items.js:138-143); registry.remove exists (core:web/static/src/core/registry.js:176).
- Duplicate service key "menuremove" versus hide_odoo_menu (js:20) - core registry rejects duplicate keys (core:web/static/src/core/registry.js:103-105).

## 5. Custom-to-custom dependencies
- None declared; CONFLICT RISK with hide_odoo_menu (same service key).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module name suggests it should hide an SMEsPlus-branded item that does not exist in this code; only odoo_account is removed.
