> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: pr_multi_approval_bridge

## 0. Header
- Module: pr_multi_approval_bridge
- License (confirmed in manifest): LGPL-3 (pr_multi_approval_bridge/__manifest__.py:44)
- Author (manifest): Ving Thailand Co., Ltd. (pr_multi_approval_bridge/__manifest__.py:33)
- Version (manifest): 19.0.1.0.0 (pr_multi_approval_bridge/__manifest__.py:4)
- Path: addons_Extramodule/addons/pr_multi_approval_bridge
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Approval-family bridge. When a user presses the "Request approval" action on a Purchase Request, the module opens the request-approval wizard of a third-party multi-approval product if a matching approval type is configured for that request; otherwise the original single-step behaviour is kept (pr_multi_approval_bridge/models/purchase_request.py:36-125; manifest description :7-26).
- Who approves / levels: NOT decided in this module. Approvers and levels are configured in the third-party approval product (model names `multi.approval.type`, `multi.approval`, `request.approval`, referenced at models/purchase_request.py:56, 89-90, 102-113, 130-136). The module contains no approver logic of its own.
- What blocks confirmation: when a type matches and no request exists, the button returns the wizard instead of moving the state (models/purchase_request.py:113-125); the manifest text says the request stays in draft until the approval flow finishes and that the approval type's own completion code may later call the approve action (manifest:14-22). Whether that completion code is actually configured is not visible here.
- Bypass observations (from code reading only): (a) with several records selected, the original path is used and the wizard is skipped (models/purchase_request.py:46-51); (b) if the third-party model is absent, if its matching helper raises, if no type matches, or if the wizard action cannot be found, the original path is used (:56-58, :63-70, :72-78, :91-98, :107-111); (c) the method only replaces one button action; other state-changing actions of the base Purchase Request module are not touched by this module (no other override present in the module).

## 2. Attachment to CORE
- Depends declared: purchase_request and multi_level_approval_configuration (manifest:34-37). Neither is a Community core module; both are outside this study (folders exist under addons_Extramodule/addons and addons_extra; not opened).
- Core Community objects extended: none directly. Core Community touchpoints: only `odoo` imports for models and translation helper (models/purchase_request.py:28).
- Overrides (by name):
  - `button_to_approve` on `purchase.request` (models/purchase_request.py:36-125): ADDS a wizard path before the original behaviour, and REPLACES the original outcome (state change) with a wizard action when an approval type matches; falls back to super in the cases listed in section 1. This is an override of a NON-core method (defined by purchase_request), so it is not marked ALTERS CORE CONTROL, but it does ALTER the third-party module's approval control.
  - `_open_existing_multi_approval` (new helper, models/purchase_request.py:128-151): opens the latest existing approval record for the request; uses sudo to search (:133).
- Uses sudo on the approval-type model (models/purchase_request.py:60), so the matching check is not limited by the caller's access rights.

## 3. New objects, security, automation, external calls
- New models/fields: none. Access file is header-only, no rows (pr_multi_approval_bridge/security/ir.model.access.csv:1). Record rules, groups: none. Company scoping: none in this module.
- Automation: none (no cron/server action). External calls: none (logging only, models/purchase_request.py:27-30).

## 4. Odoo 19 compatibility
- Names absent from the Community 19 tree (checked by text search in core addons): `purchase.request`, `to_approve_allowed_check` (called at models/purchase_request.py:86), `multi.approval`, `request.approval`, `multi.approval.type` — all provided by non-core modules; cannot be validated against Community.
- Core API used (`_inherit`, `self.env.ref(..., raise_if_not_found=False)`, `ensure_one`): standard; not individually checked.
- Manifest claims testing with the third-party product version 19.0.x (manifest:28-31); not verified.

## 5. Custom-to-custom dependencies
- Depends on purchase_request and multi_level_approval_configuration (manifest:34-37).
- Required by: purchase_request_dedupe_multi_approval (its manifest:35-38).
- Interacts with purchase_request_hide_approval_btn (hides the button this module rewires) and purchase_request_level_approve (also makes the same button invisible and adds its own two-level flow) — see those files.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: who the approvers are and how many levels the third-party approval type defines (source of that product not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the auto-created fields `x_need_approval` / `x_has_request_approval` (mentioned at models/purchase_request.py:24, 81) actually exist in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: how the module behaves when installed together with purchase_request_level_approve (both act on the same button; conflict resolution not shown).
