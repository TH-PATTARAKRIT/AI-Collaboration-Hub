> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: purchase_request_hide_approval_btn

## 0. Header
- Module: purchase_request_hide_approval_btn
- License (confirmed in manifest): LGPL-3 (purchase_request_hide_approval_btn/__manifest__.py:21)
- Author (manifest): BHPRO (purchase_request_hide_approval_btn/__manifest__.py:20)
- Version (manifest): 19.0.1.0.0 (purchase_request_hide_approval_btn/__manifest__.py:4)
- Path: addons_Extramodule/addons/purchase_request_hide_approval_btn
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Approval-family menu/button hiding. Hides the "Request approval" button (method `button_to_approve`) on the Purchase Request form so users only use the multi-approval button (manifest description :8-19).
- What is hidden: one header button, via the invisible attribute (views/purchase_request_view.xml:16-19).
- Access rights: NOT affected. Hidden in the form view only; no group, ACL or rule is changed. The method remains callable by any user who can trigger it outside the form (for example from list actions or remote calls); the manifest itself states the aim is to prevent state changes bypassing the workflow (manifest:11-13) but the module does not block the method. This is inference from the absence of any Python file: the module has an empty `__init__.py` (purchase_request_hide_approval_btn/__init__.py) and lists only the view in data (manifest:25-27).
- Who approves / levels / what blocks confirmation: none defined here.

## 2. Attachment to CORE
- Depends declared: purchase_request only (manifest:22-24). No Community core view is modified.
- Extends the non-core form view `purchase_request.view_purchase_request_form` (views/purchase_request_view.xml:11), priority 99 (:12), with an attributes edit on `//header/button[@name='button_to_approve']` (:16).
- No core method overridden; no ALTERS CORE CONTROL.

## 3. New objects, security, automation, external calls
- New models/fields/ACLs/groups/rules: none. Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Only a view inheritance; names referenced come from purchase_request (not in Community tree; cannot be checked). Attribute form `invisible=1` is Odoo 17+ style.

## 5. Custom-to-custom dependencies
- Depends on purchase_request (non-core).
- Related: purchase_request_level_approve also sets the same button invisible (purchase_request_level_approve/views/purchase_request_view.xml:11-13); its changelog says other modules xpath on this button name, naming this module (purchase_request_level_approve/__manifest__.py:54-60). pr_multi_approval_bridge overrides the method behind this button.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the base purchase_request module has other paths that call `button_to_approve` (its source is outside this study).
