> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: purchase_request_level_approve

## 0. Header
- Module: purchase_request_level_approve
- License (confirmed in manifest): LGPL-3 (purchase_request_level_approve/__manifest__.py:90)
- Author (manifest): BH Pro International (purchase_request_level_approve/__manifest__.py:89)
- Version (manifest): 19.0.1.3.0 (purchase_request_level_approve/__manifest__.py:4)
- Path: addons_Extramodule/addons/purchase_request_level_approve
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability (approval family, in depth)
Two-level approval of Purchase Requests, layered on top of the non-core purchase_request module (manifest description :8-36).

State model
- Adds state `approved_level1` (label "Approved") and relabels `approved` as "Confirm"; also re-lists `cancel` (models/purchase_request.py:36-47). Draft -> to_approve -> approved_level1 -> approved; reject returns to draft or to to_approve; cancel is a terminal archived state (models/purchase_request.py:185-367).

Who approves
- Level 1 = the manager of the requester's HR employee record (employee parent's linked user), computed and stored (models/purchase_request.py:91-105, field :52-57). Empty if requester has no employee or no manager (:98-101 docstring, :103-105).
- Level 2 = the user in `assigned_to` of the request, described as taken from the employee field `pr_approver` (relabelled "Manager Confirm" on hr.employee, models/hr_employee.py:37; consumption of `assigned_to` at models/purchase_request.py:113-125, :256-260). The link between `pr_approver` and `assigned_to` is defined in the non-core purchase_request module and not read here.
- Level 2 is user-specific, not group-based (changelog: purchase_request_level_approve/__manifest__.py:82-84; code models/purchase_request.py:123-125).
- "By Approve" flag on the employee (models/hr_employee.py:38, view views/hr_employee_view.xml:17-19): (a) if the Level 1 approver has it, Level 1 is recorded as approved automatically when the request enters to_approve or is sent back (models/purchase_request.py:146-165, calls at :205, :216, :418); (b) if the Level 2 approver has it, that person can Confirm directly from to_approve and Level 1 is stamped with the same user (models/purchase_request.py:126-132, :262-296).

What blocks confirmation (final Confirm, `action_approve_level2`, models/purchase_request.py:244-297)
- Caller must be the request's `assigned_to` user (:256-260).
- State must be approved_level1, or to_approve with the By Approve flag on the Level 2 approver (:264-273); otherwise error.
- No check that the Level 2 approver differs from the requester (no such comparison anywhere in the module; text search of models/ and wizard/).
- Level 1 approval (`action_approve_level1`, :219-239): state must be to_approve (:226) and caller must be the computed Level 1 user (:228-231).

Whether approvals can be bypassed (code-reading observations; runtime not tested)
1. Settings stored but not enforced: four settings (require manager, require approver, allow send back, auto-open RFQ) are saved as system parameters (models/res_config_settings.py:27-54) but no code in the module reads them (text search for `get_param` and the parameter names finds only the definitions and the settings view). So "Require Manager" and "Require Approver" do not actually stop submission; the "Send Back" option is not applied to the reject wizard (wizard/purchase_request_level_reject.py:27-33 always offers both modes).
2. Cancel has no authority check: `action_cancel` (models/purchase_request.py:337-367) only stops if already cancelled (:349-352); the state test is commented out (:353-357) and there is no requester/approver test although the docstring says only requester, Level 1 or Level 2 may cancel (:340-346). It also archives the record (:361). The button is shown only in to_approve and approved_level1 (views/purchase_request_view.xml:64-68) but the method is not state-guarded. It is visible to anyone who can open the form and call the method.
3. Reject wizard re-check: the authority check happens when opening the wizard (models/purchase_request.py:302-319); the wizard's own confirm (wizard/purchase_request_level_reject.py:38-53) does not repeat it, so a user with the wizard ACL (see section 3) could confirm a reject for a request they are not approver of if they can create the wizard record directly.
4. Reset to draft: `button_draft` is extended only to clear approval fields (models/purchase_request.py:423-433); its visibility is widened to states to_approve, approved_level1, rejected, approved (views/purchase_request_view.xml:77-79). Who may press it is decided by the non-core module (UNKNOWN below).
5. Legacy actions retained: the module keeps the base methods "for compatibility" (models/purchase_request.py:13-14) and hides only `button_to_approve` (views/purchase_request_view.xml:11-13). Whether the base approve/reject buttons for managers remain visible is decided by the non-core view (UNKNOWN below).
6. Send-ready action `action_send_ready_to_check` (models/purchase_request.py:185-206) exists but no button calls it in this module's view (only `action_submit_for_approval` is placed, views/purchase_request_view.xml:37-41). The submit action does not clear earlier approval stamps (models/purchase_request.py:211-217), unlike the send-ready action (:193-200).
7. Level 1 empty: if the requester has no manager the Level 1 button can never appear for anyone (models/purchase_request.py:121-122), yet a Level 2 approver flagged By Approve can still Confirm from to_approve (:129-132).
8. Access errors possible for ordinary users: the compute of approval rights reads employee data of another user without elevation (models/purchase_request.py:137-144). Core grants read of the employee model only to HR officers and system users (core:hr/security/ir.model.access.csv:4-5). Whether an ordinary requester hits an access error on opening the form is not tested.

## 2. Attachment to CORE
- Depends declared: purchase_request, hr, mail (manifest:91-95). Core Community objects touched: `hr.employee` (fields added models/hr_employee.py:37-38; form view extended at group "user", views/hr_employee_view.xml:15-19; core group at core:hr/views/hr_employee_views.xml:360), `hr.employee.public` (models/hr_employee.py:41-44; core model core:hr/models/hr_employee_public.py:11), `res.config.settings` (models/res_config_settings.py:24-25; core base settings form core:base/views/res_config_settings_views.xml:4), mail thread (message_post / tracking used across models/purchase_request.py).
- Overrides of non-core `purchase.request` methods (by name):
  - `button_draft` (:423-433): ADDS after the base behaviour (clears approval stamps and reason).
  - `state` selection extension (:36-47): ADDS states; relabels the base "approved" state.
  - Compute `_compute_level1_user_id`, `_compute_approval_rights` (new, :91-132).
  - Actions new: `action_send_ready_to_check`, `action_submit_for_approval`, `action_approve_level1`, `action_approve_level2`, `action_open_reject_wizard`, `action_cancel`, `_do_reject_hard`, `_do_reject_soft` (:185-418). `action_cancel` defined here on the request model; whether the base module also defines `action_cancel`/cancel logic is not read (UNKNOWN).
- No Community core method is overridden. No ALTERS CORE CONTROL.
- `_do_reject_hard` bumps the counter field `revise_count` (models/purchase_request.py:388), a field of the non-core module.

## 3. New objects, security, automation, external calls
- New transient model `purchase.request.level.reject` (wizard/purchase_request_level_reject.py:17-19) with fields request, current state, mode (hard / soft), reason (required) (:21-36).
- New fields on purchase.request: level1_user_id (stored compute, no `groups`), level1_approved_by / date, level2_approved_by / date, reject_reason (all tracked), can_approve_level1 / level2 / level2_now (computed), `active` (models/purchase_request.py:52-86). Adding `active` makes cancelled requests disappear from default lists (:361).
- New fields on hr.employee: `pr_approver` (user), `by_approve` (boolean); no `groups` restriction on either field (models/hr_employee.py:37-38). Editing is governed by core employee write access, which core gives to HR officers (core:hr/security/ir.model.access.csv:4).
- ACLs: two rows on the wizard model for the purchase request user and manager groups (of the non-core module), full CRUD both (security/ir.model.access.csv:2-3). No record rules, no new groups, no company scoping in this module.
- Menus/actions: a "Configuration" menu and "Settings" entry under the purchase request root menu, restricted to the request manager group (views/res_config_settings_view.xml:62-76); settings block restricted to request user group (:25).
- Automation: none (no cron). Notifications: chatter posts on each action (message_post in models/purchase_request.py:163, :201, :237, :289-296, :364, :390, :411). External calls: none.
- Form view: hides the base "Request approval" button (views/purchase_request_view.xml:11-13); adds Submit for Approval / Approve / Confirm / Reject / Cancel buttons (:37-68); Level 1 / Level 2 page (:85-118); reject banner (:17-23); Cancelled ribbon (:28-31). A stray bare `state` statusbar field line is at views/purchase_request_view.xml:81-82 whose effect in an inheriting view is unclear (UNKNOWN below).

## 4. Odoo 19 compatibility
- Names not in the Community 19 tree (text search of core addons): `purchase.request`, `revise_count`, `to_approve_allowed_check` (used models/purchase_request.py:192, :213), `assigned_to`/`requested_by`/`pr_approver` as request fields — all defined by the non-core purchase_request module; not checkable.
- Core references confirmed present: `hr.employee.parent_id` (core:hr/models/hr_employee.py:195), `res.users.employee_id` / `employee_ids` (core:hr/models/res_users.py:63-64), `hr.employee.public` (core:hr/models/hr_employee_public.py:11), employee form group "user" (core:hr/views/hr_employee_views.xml:360), `web_ribbon` widget (core:web/static/src/views/widgets/ribbon/ribbon.js:71), settings base form (core:base/views/res_config_settings_views.xml:4).
- Changelog states Odoo 19 no longer accepts an inline settings-action target and it was changed (manifest:70-73, version 19.0.1.1.1); not tested here.
- The statusbar attribute lists a state `rejected` (views/purchase_request_view.xml:73, :78) that this module does not add to the state selection (:36-47); its existence depends on the non-core module (UNKNOWN below).

## 5. Custom-to-custom dependencies
- Depends on purchase_request (non-core). Uses the group names `purchase_request.group_purchase_request_user` / `..._manager` in ACL and menus.
- Sibling/conflict with pr_multi_approval_bridge (same button rewired) and purchase_request_hide_approval_btn (same button hidden) — see those files.
- Its fields `pr_approver`, `by_approve` on hr.employee are consumed by sale_order_level_approve (sale_order_level_approve/models/sale_order.py:106, :156-157), which depends on purchase_request rather than on this module.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the base purchase_request module still shows its own approve / reject buttons to managers, allowing state change without the two-level path.
- UNKNOWN — EVIDENCE INSUFFICIENT: who may press the reset-to-draft button and whether the base module restricts it by group.
- UNKNOWN — EVIDENCE INSUFFICIENT: how `assigned_to` is derived from `pr_approver` (related field defined outside this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the `rejected` state exists in the deployed database.
- UNKNOWN — EVIDENCE INSUFFICIENT: effect of the bare `state` statusbar line at views/purchase_request_view.xml:81-82.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether ordinary requesters hit access errors on employee data (runtime not tested).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether downstream RFQ creation (non-core) requires state `approved` or accepts other states.
