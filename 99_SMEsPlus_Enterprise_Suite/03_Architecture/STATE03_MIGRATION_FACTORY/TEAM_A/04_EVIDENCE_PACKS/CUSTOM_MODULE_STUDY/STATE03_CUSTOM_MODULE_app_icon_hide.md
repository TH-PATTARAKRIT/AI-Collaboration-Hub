> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: app_icon_hide

## 0. Header
- Module: app_icon_hide
- License (confirmed in manifest): LGPL-3 (addons_extra/app_icon_hide/__manifest__.py:8)
- Author (manifest): SMEsPlus (addons_extra/app_icon_hide/__manifest__.py:4)
- Version (manifest): 18.0.1.1.0 (addons_extra/app_icon_hide/__manifest__.py:3) - note: 18.0 series number in an Odoo 19 workspace
- Path: addons_Extramodule/addons_extra/app_icon_hide
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Cosmetic branding change: hides the "About" block (edition/version/copyright notice) on the General Settings page using a stylesheet rule (app_icon_hide/static/css/custom.css:1-3). The manifest summary calls it "Hide mobile icon in General Setting Page" (manifest:7), which does not match what the stylesheet targets (see section 6).

## 2. Attachment to CORE
- Depends on base (manifest:9). No Python models are loaded (app_icon_hide/__init__.py:1 has the models import commented out).
- The CSS selector targets the element with id "about" that core places in the General Settings view (core:base_setup/views/res_config_settings_views.xml:200). Effect: ADDS a display rule after core styles; no core method overridden. No ALTERS CORE CONTROL.
- Stylesheet is registered in the backend asset bundle, i.e. loaded on every backend page (manifest:13-17), so any element with id "about" anywhere in the backend is hidden.

## 3. New objects, security, automation, external calls
- New models, fields, ACLs, groups, record rules: none. Data files: none (manifest:10-12 commented). Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- No Python references to check. CSS target id "about" exists in the core 19 tree (core:base_setup/views/res_config_settings_views.xml:200).
- Version tag in manifest is 18.0.x (manifest:3); whether the target Odoo 19 loader accepts this without a migration is not checked.

## 5. Custom-to-custom dependencies
- None declared. Functionally overlaps with bh_hide_odoo_edition (hides the same About block by view edit) - see that module's file.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: what "mobile icon" in the manifest summary refers to; the code only hides id "about".
