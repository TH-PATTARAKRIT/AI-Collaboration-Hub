> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: sale_order_level_approve

## 0. Header
- Module: sale_order_level_approve
- License (confirmed in manifest): LGPL-3 (sale_order_level_approve/__manifest__.py:26)
- Author (manifest): SMEsPlus (sale_order_level_approve/__manifest__.py:23)
- Version (manifest): 19.0.1.0.0 (sale_order_level_approve/__manifest__.py:3)
- Path: addons_Extramodule/addons/sale_order_level_approve
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability (approval family, in depth)
Two-level approval of quotations before they become confirmed sales orders (manifest:4-22).

Flow
- Draft/Sent -> "To be Approved" (state `ready_to_check`, sent by the salesperson) -> "Approved" (`approved_level1`, Level 1) -> Confirm by Level 2, which calls the standard confirmation and reaches `sale` (models/sale_order.py:14-24, :183-214, :216-256, :258-338).

Who approves
- Level 1 = manager (employee parent's linked user) of the employee record linked to the salesperson (`user_id`) (models/sale_order.py:84-103).
- Level 2 = the `pr_approver` user of the salesperson's employee record (models/sale_order.py:105-112), a field belonging to the purchase-request family (manifest comment :30).
- Both fields are stored computes that are also editable (readonly=False) (models/sale_order.py:29-49). The form makes Level 1 editable while state is draft or sent, and Level 2 editable while draft, sent or ready_to_check (views/sale_order_view.xml:80-81, :90-91). Nothing in the module restricts these fields by group or checks that the approver differs from the salesperson (text search of models/ and wizards/ finds no such comparison).
- "By Approve" flag on the employee (field defined in purchase_request_level_approve; used at models/sale_order.py:151-157): Level 1 auto-passes on send if the manager has it (:159-178, called :213); a Level 2 approver with it may confirm from ready_to_check with Level 1 stamped by the same person (:140-146, :272-296).
- Only the assigned user may approve; the true system superuser (uid 1) also passes; ordinary administrators do not (models/sale_order.py:117-139 docstring and code).

What blocks confirmation
- Direct confirm from draft/sent is refused for everyone except the system superuser with the message "Direct confirmation is disabled" (models/sale_order.py:428-435). This is done inside the core confirmation error check (see section 2), so every caller of standard confirm on a draft/sent order is blocked, not only the form button.
- The form hides both standard Confirm buttons (views/sale_order_view.xml:58-63) and shows "Confirm Sale Order" only at approved_level1 for the Level 2 user (:31-35).
- Level 1 approval also needs a resolved Level 2 approver (models/sale_order.py:228-233); send-for-check needs a resolved Level 1 approver (:191-195).

Whether approvals can be bypassed (code-reading observations; runtime not tested)
1. Context flag: the confirmation guard is skipped when the context key `_skip_sale_confirm_guard` is set and state is approved_level1 (models/sale_order.py:412-426). The key is passed by Level 2 (:337) but any caller able to supply context to the standard confirm on an order already in approved_level1 would confirm without the Level 2 identity check. This requires the order to have passed Level 1.
2. Approver reassignment: since both approver fields are editable before approval (views/sale_order_view.xml:80-81, :90-91) and no group/identity check exists, a user who can edit the quotation could name themselves as approver, then approve. Inference from the code; not executed.
3. By Approve shortcut: a Level 2 approver flagged By Approve can confirm from ready_to_check, skipping a separate Level 1 (models/sale_order.py:277-278). The form button for Level 2 is only visible at approved_level1 (views/sale_order_view.xml:35), and the computed "now" flag is not placed in the view (only can_approve_level1/2 at :111-112), so this shortcut is reachable by direct method call rather than by the form as shipped. Inference.
4. Reset to draft: the method checks the state only (models/sale_order.py:361-366); the group restriction to the sales manager group is on the form button only (views/sale_order_view.xml:48). Direct calls are not group-checked in this module. Reset clears approval stamps (:368-374).
5. Reject: authority is checked inside the wizard (wizards/sale_order_reject_wizard.py:44-55); reason mandatory (:14). Wizard ACL for salesman and sales manager groups (security/ir.model.access.csv:2-3).
6. Superuser: uid 1 may confirm directly and approve at either level (models/sale_order.py:129-138, :430).
7. Other confirm paths: core confirms draft/sent quotations automatically after online payment and from the order-validation helper (core:sale/models/payment_transaction.py:120-131, core:sale/models/sale_order.py:1295-1300). Under this module those calls hit the block above for non-superusers. Actual behaviour with portal payment installed is not tested.

## 2. Attachment to CORE
- Depends declared: sale_management, hr, purchase_request (manifest:27-31).
- Core objects extended: `sale.order` (state selection, new fields, actions), core form view `sale.view_order_form` (views/sale_order_view.xml:7; core buttons at core:sale/views/sale_order_views.xml:308-324; Other Info page core:sale/views/sale_order_views.xml:852), `hr.employee`.
- Core state list: quotation, sent, sale, cancel (core:sale/models/sale_order.py:26-31). Module adds `ready_to_check` and `approved_level1` (models/sale_order.py:14-24).
- Overrides of core methods:
  - `_confirmation_error_message` (models/sale_order.py:397-438): ALTERS CORE CONTROL. Core allows confirmation only from quotation/sent and checks lines have products (core:sale/models/sale_order.py:1205-1218). Module (a) REPLACES the state check for context-flagged calls from approved_level1 and re-implements the product-line check (:412-426); (b) BLOCKS confirmation of draft/sent for non-superusers (:430-435); (c) otherwise ADDS nothing and falls to core (:438). Core `action_confirm` calls this check for each order before writing state (core:sale/models/sale_order.py:1168-1180).
  - `_prepare_confirmation_values` (models/sale_order.py:440-447): pass-through (calls core only; no change). Core at core:sale/models/sale_order.py:1220-1231.
- Standard `action_confirm` is called, not replaced, on Level 2 approval (models/sale_order.py:337); downstream sale-order processing (deliveries, etc.) runs from the core confirmation.

## 3. New objects, security, automation, external calls
- New transient model `sale.order.reject.wizard` (wizards/sale_order_reject_wizard.py:6-27): order, current state, mandatory reason, and target (draft or back to ready_to_check).
- New fields on sale.order: level1_user_id, level2_user_id (stored, tracked, editable), approval user/date stamps, reject_reason (tracked), three computed flags (models/sale_order.py:29-79). No `groups` on any field.
- ACL: two rows for the wizard (salesman and sales manager groups, full CRUD) (security/ir.model.access.csv:2-3). No record rules, no new groups, no company scoping added.
- The approver lookup runs the employee search with elevated access (models/sale_order.py:91-98); the By Approve helper reads employee data without elevation (:151-157) — core allows employee-model read to HR officers and system users only (core:hr/security/ir.model.access.csv:4-5), so ordinary salespeople may hit access errors (not tested).
- Automation: none (no cron). Chatter posts with formatted HTML on each step (models/sale_order.py:197-211 and others). External calls: none.
- Views: buttons, "Approvers" page, reject banner (views/sale_order_view.xml:15-127).

## 4. Odoo 19 compatibility
- References confirmed in Community 19: `_confirmation_error_message`, `_prepare_confirmation_values` (core:sale/models/sale_order.py:1205, :1220), `is_downpayment` on order lines (core:sale/models/sale_order_line.py:74), `display_type` (core:sale/models/sale_order_line.py:63), buttons `id="action_confirm"` and the unnamed-id second button (core:sale/views/sale_order_views.xml:308-324), page `other_information` (core:sale/views/sale_order_views.xml:852), `_is_superuser` (core:base/models/res_users.py:1185).
- Absent from Community: `pr_approver`, `by_approve` on hr.employee (defined by non-core modules); code defends by checking field presence (models/sale_order.py:106).
- The module re-implements the product-line check text of core; if core changes that check in a later release the copy would drift (inference).

## 5. Custom-to-custom dependencies
- Depends on purchase_request (manifest:30) for the employee field `pr_approver`; uses `by_approve` which is defined in purchase_request_level_approve (see that file), but does not declare that module as a dependency — installation without it would raise an error at the By Approve helper (models/sale_order.py:157). Whether the deployment always installs both is not shown.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether `pr_approver` is a user or an employee link in the deployment (the code accepts either, models/sale_order.py:109-112; purchase_request_level_approve defines it as a user link).
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction with other installed modules that confirm quotations automatically (portal payment, subscriptions, POS-to-sale, imports).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other installed modules also extend the `state` selection of sale.order or the confirmation check.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the bypass observations 1-3 are reachable in the deployed instance (not executed).
