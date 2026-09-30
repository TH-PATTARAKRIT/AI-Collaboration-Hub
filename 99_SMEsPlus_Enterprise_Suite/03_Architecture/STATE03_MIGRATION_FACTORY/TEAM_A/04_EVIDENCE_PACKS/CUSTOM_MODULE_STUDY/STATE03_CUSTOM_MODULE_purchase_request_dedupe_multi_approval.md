> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: purchase_request_dedupe_multi_approval

## 0. Header
- Module: purchase_request_dedupe_multi_approval
- License (confirmed in manifest): LGPL-3 (purchase_request_dedupe_multi_approval/__manifest__.py:34)
- Author (manifest): BHPRO (purchase_request_dedupe_multi_approval/__manifest__.py:33)
- Version (manifest): 19.0.1.0.0 (purchase_request_dedupe_multi_approval/__manifest__.py:4)
- Path: addons_Extramodule/addons/purchase_request_dedupe_multi_approval
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Approval-family display fix. Removes visual duplicates on the Purchase Request form: a second identical header button and a second identical alert box that appear when the third-party approval product injects its form additions twice (manifest description :9-27).
- Who approves / levels / what blocks confirmation: none. The module changes only what is shown; it adds no approval rule.
- Access effect: VISIBILITY ONLY. The duplicate elements get the invisible attribute at view-load time (models/purchase_request.py:65, :92). Underlying buttons/methods and access rights are untouched; the kept (first) copy remains functional (manifest:22-27).
- Bypass observation: since only the second and later duplicates are hidden, a user cannot see them but the actions still exist on the server; hiding is not an access control.

## 2. Attachment to CORE
- Depends declared: purchase_request and pr_multi_approval_bridge (manifest:35-38); no Community core module named directly.
- Override (by name): `_get_view` on `purchase.request` (models/purchase_request.py:30-44): ADDS after core — calls the core view builder first, then edits the resulting arch for form views only (:34-35). Core method compared: `_get_view` on the base model class (core:base/models/ir_ui_view.py:2978; class Base begins core:base/models/ir_ui_view.py:2728). Not a core control; no ALTERS CORE CONTROL. Errors during deduplication are logged and swallowed (:37-42).
- Helpers: `_prl_button_key` (:47-53), `_prl_dedupe_buttons` (:55-71: buttons inside any header with same name/label/type; buttons with neither name nor label are skipped :62-63), `_prl_dedupe_alerts` (:73-98: alert boxes with same class and text).
- Because it matches on name+label, two legitimately different buttons that share the same name and label would also be hidden (inference from :53, :64).

## 3. New objects, security, automation, external calls
- New models/fields: none. Security files: none (`data` list empty, manifest:39). XML view file is an empty shell with a comment (views/purchase_request_view.xml:1-7) and is not listed in manifest data.
- Automation: none. External calls: none (logging only).
- Performance note: the deduplication runs on each form view build for this model (models/purchase_request.py:30-44); cost not measured.

## 4. Odoo 19 compatibility
- `_get_view` signature `(view_id=None, view_type='form', **options)` matches Community 19 (core:base/models/ir_ui_view.py:2978). Return of a tuple (arch, view) as used here at :32/:44 — return shape not checked in detail.
- Names not in Community 19 tree: `purchase.request` (non-core). No removed core API found.
- Uses `invisible="1"` attribute form (models/purchase_request.py:65) — consistent with Odoo 17+ view syntax; not runtime-tested.

## 5. Custom-to-custom dependencies
- Depends on pr_multi_approval_bridge and purchase_request (manifest:35-38).
- Sibling of purchase_request_hide_approval_btn (different approach to reducing button confusion).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the duplicate-injection symptom currently occurs in the deployed database (module addresses a symptom in the third-party product).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the module could hide a legitimate button when combined with purchase_request_level_approve, whose view adds several buttons to the same header (that module's view file was read; overlap of names not observed, but the runtime merged arch was not inspected).
