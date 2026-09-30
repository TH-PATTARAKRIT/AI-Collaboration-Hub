> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - purchase_request_level_approve_po

Module: purchase_request_level_approve_po
License (confirmed in manifest): LGPL-3 (purchase_request_level_approve_po/__manifest__.py:134)
Author (manifest): BH Pro International (purchase_request_level_approve_po/__manifest__.py:133)
Version (manifest): 19.0.1.3.0 (purchase_request_level_approve_po/__manifest__.py:4)
Path: addons_Extramodule/addons/purchase_request_level_approve_po
Source revision studied: workspace on-disk copy (not verified against upstream). Manifest carries a changelog of local fixes dated 2026-05-23 and 2026-06-05 (__manifest__.py:55-131).

## 1. Business capability
- Adds a two-level internal approval to the ordinary purchase order (not to the purchase request) before it may be confirmed: Level 1 = the requester's line manager in HR; Level 2 = the "purchase request approver" named on the requester's employee record; then a Purchase Manager performs the final "Confirm Order" (purchase_request_level_approve_po/models/purchase_order.py:1-24, :118-181; __manifest__.py:11-30).
- Company-wide switches decide whether manager / approver are mandatory, whether Level 2 may send back to Level 1, and whether direct confirmation from Draft is blocked (models/res_config_settings.py:23-51).

## 2. Attachment to CORE (depends: purchase, purchase_request_level_approve, hr, mail - __manifest__.py:135-140)
- core `purchase.order`: state list extended with three new states between RFQ and Purchase Order: "Ready to Check", "Approved" (Level 1 done), "Confirm" (Level 2 done) (models/purchase_order.py:44-56; core states at core:purchase/models/purchase_order.py:105-111). Adds stored fields for each level's approver, approver/date stamps, reject reason, vendor code display and three per-user visibility flags (models/purchase_order.py:61-113).
- core form/list views: REPLACES the standard "Confirm Order" button with "Send Ready to Check" plus a Purchase-Manager-only "Confirm Order" that appears only at the last state; hides the draft-confirm button; adds Approve / Confirm / Reject buttons and an "Approval Level" tab; priority 99 (views/purchase_order_view.xml:20, :40-92, :152-188; core:purchase/views/purchase_views.xml:126, :135-138).
- Core method overrides, by name:
  - `button_confirm` - REPLACES core for the last step and BLOCKS/ALTERS core control: (a) blocks confirmation while approvals pending; (b) by default blocks direct confirmation from RFQ / RFQ Sent; (c) at state "Confirm" only members of the Purchase Manager group may confirm, and then the module calls core `button_approve` directly instead of the core confirmation path (models/purchase_order.py:502-583; core:purchase/models/purchase_order.py:615-640). ALTERS CORE CONTROL (approvals): core confirmation checks (confirmation error message, supplier registration on product, analytic validation, double-validation routing to "To Approve") run only for the pass-through path and are NOT run at the final step (core:purchase/models/purchase_order.py:626-638). Core's own two-step validation by amount is therefore not applied to orders that use this workflow (inference from code path).
  - `button_draft` - ADDS after core: clears approver stamps and reject reason (models/purchase_order.py:588-598).
- New action methods (no core equivalent): send ready to check (draft or sent -> Ready to Check), Level 1 approve, Level 2 confirm, open reject wizard, hard reject (-> Draft) and soft reject / send back (-> Ready to Check), final confirm wrapper (models/purchase_order.py:263-495).
- Not overridden: core `button_approve`, `button_cancel`, `write`. `button_approve` stays callable on any order state by anyone with the method reachable (core body filters only by approval right, core:purchase/models/purchase_order.py:615-619) - path to skip the workflow exists in principle (inference; not run).

### Purchase order approval flow (business language)
1. RFQ (Draft / RFQ Sent) -> Ready to Check: requester presses "Send Ready to Check"; needs at least one line; if switches on, needs a manager (HR parent) and a Level 2 approver, otherwise error (models/purchase_order.py:263-308; switches models/res_config_settings.py:23-36).
2. Ready to Check -> Approved (Level 1): only the manager resolved at that moment may press "Approve" (models/purchase_order.py:313-333, :102-114, :152-168). Requester = Purchase Representative if that user has an employee record, else the record creator (models/purchase_order.py:118-134).
3. Approved -> Confirm (Level 2): only the requester's `pr_approver` user may press "Confirm" (models/purchase_order.py:338-392, :170-181). `pr_approver` field itself is defined in purchase_request (purchase_request/models/hr_employee.py:7).
4. Confirm -> Purchase Order: a Purchase Manager presses "Confirm Order" (button and server check) (views/purchase_order_view.xml:56-61; models/purchase_order.py:544-578).
- Reject: Level 1 manager can reject from Ready to Check, Level 2 approver from Approved; wizard offers "Reject (back to Draft)" or "Send Back to Level 1"; reason mandatory; send back only from Approved and only if the setting allows (models/purchase_order.py:397-476; wizard/purchase_order_level_reject.py:27-62).
- "By Approve" flag on an employee (defined in purchase_request_level_approve, not read): a Level 1 approver with the flag is auto-approved at once; a Level 2 approver with the flag may confirm directly from Ready to Check, approving Level 1 at the same time (models/purchase_order.py:207-237, :356-381).
- Self-approval: nothing prevents a person who is both requester's manager / approver and creator of the order from approving their own order if HR data point to them - UNKNOWN whether HR data can produce this (no explicit self-approval check in code).

## 3. New objects, security, automation, external calls
- New model: wizard `purchase.order.level.reject` (wizard/purchase_order_level_reject.py:17-38). ACL: purchase users and managers full on that wizard (security/ir.model.access.csv:2-3). No new groups; no record rules; approver rights come from HR data, not from groups. Approver users still need normal purchase access to open the order (UNKNOWN which).
- Settings stored as system parameters under the module prefix; menu "PO Level Approve Settings" limited to Purchase Manager group (models/res_config_settings.py:25-50; views/res_config_settings_view.xml:64-69). Whether a Purchase Manager can save the settings page: UNKNOWN.
- Automation: none (no cron, no server action). External calls: none.
- Multi-company: no company logic added; fields inherit order's company scope.

## 4. Odoo 19 compatibility (grep in Community 19)
- Core order state list in 19 has no "done"; module text mentions po lock turning state to done (models/purchase_order.py:558; __manifest__.py:99-107) but 19 locks with a separate `locked` flag (core:purchase/models/purchase_order.py:112-117, :619). Only comment / message text affected.
- `button_approve(force=False)`, `button_draft`, `button_confirm`, `_approval_allowed` exist (core:purchase/models/purchase_order.py:615, :621, :625, :1251). `res.users.employee_id` exists (core:hr/models/res_users.py:64). View anchors `button_confirm`, `draft_confirm`, `button_cancel`, `purchase_order_tree` exist (core:purchase/views/purchase_views.xml:135-145, :550).
- Core order-line fields in the form stay editable in the new states because core readonly conditions list only purchase / to approve / cancel (core:purchase/views/purchase_views.xml:246, :269, :286); module adds no lock or approval-reset on line edits -> approved amounts can change after approval (inference from view attributes; not run).
- Other flows that call core `button_confirm` on a draft order (portal, automated jobs) would hit the block (models/purchase_order.py:539-543) - not checked.
- Field `by_approve` referenced (models/purchase_order.py:216) lives in another custom module: not checked.

## 5. Custom-to-custom dependencies
- purchase_request_level_approve (manifest depends; supplies `by_approve` per comments at __manifest__.py:61-70; folder addons_Extramodule/addons/purchase_request_level_approve, not read here). Indirectly purchase_request via `pr_approver` (purchase_request/models/hr_employee.py:7).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module's level-approve depends chain actually installs purchase_request (its manifest was not read).
- UNKNOWN - EVIDENCE INSUFFICIENT: what happens to orders in the new states created by procurement / other modules that expect draft or sent.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether audit of who changed order lines after approval exists elsewhere (tracking only on the approver stamps, models/purchase_order.py:78-89).
