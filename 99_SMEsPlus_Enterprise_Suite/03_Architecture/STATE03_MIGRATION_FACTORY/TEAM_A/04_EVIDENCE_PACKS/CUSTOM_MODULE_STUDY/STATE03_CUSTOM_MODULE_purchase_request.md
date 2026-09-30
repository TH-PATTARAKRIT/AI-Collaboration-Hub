> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE - purchase_request

Module: purchase_request
License (confirmed in manifest): LGPL-3 (purchase_request/__manifest__.py:31)
Author (manifest): ForgeFlow, Odoo Community Association (OCA) (purchase_request/__manifest__.py:6)
Version (manifest): 19.0.1.0 (purchase_request/__manifest__.py:7)
Path: addons_Extramodule/addons_extra/purchase_request  (a second folder named purchase_request also exists under addons_Extramodule/addons/ - not studied, may differ)
Source revision studied: workspace on-disk copy (not verified against upstream). Local edits are visible (Thai labels, commented-out blocks, added fields).

## 1. Business capability
- An internal "request to buy" document (header + product lines) that staff raise before purchasing; it is approved or rejected, then turned into a request-for-quotation (RFQ) for a chosen supplier, with follow-up of ordered / received quantity per request line (purchase_request/models/purchase_request.py:17-22; models/purchase_request_line.py:16-21).
- Requests can also be generated automatically from stock replenishment for products flagged "generate Purchase Request instead of RFQ" (models/product_template.py:10-14; models/stock_rule.py:72-130).

## 2. Attachment to CORE (depends: purchase, product, purchase_stock, hr, project + custom smesplus_uom_ext - __manifest__.py:13)
- core `purchase.order`: adds a vendor image (models/purchase_order.py:10-14); form shows it and moves payment terms next to picking type (views/purchase_order_view.xml:10-36; core:purchase/views/purchase_views.xml:126).
- core `purchase.order.line`: adds link to request lines and allocations; REPLACES the product field definition (adds purchase-ok filter and tracking) (models/purchase_order.py:103-120).
- core `hr.employee` / `hr.employee.public`: adds "purchase request approver" user link `pr_approver` (models/hr_employee.py:7, :13; views/hr_employee_view.xml:9). `project.project` link on request header (models/purchase_request.py:161).
- core `product.template`: company-dependent flag (models/product_template.py:10-14). core `stock.move`: link to created request line, allocations, merge and cancel hooks (models/stock_move.py:11-86). `stock.warehouse.orderpoint`, `stock.rule`, `stock.move.line`, `stock.picking`: see below.
- Core method overrides, by name:
  - `purchase.order.button_confirm` - ADDS after core: posts a chatter note on each linked request (models/purchase_order.py:80-84). Does not alter the confirmation itself.
  - `purchase.order.unlink` - ADDS: deletes related allocations after core delete (models/purchase_order.py:86-97).
  - `purchase.order.line.write` - ADDS before core: chatter notes on quantity/price change; service lines trigger allocation updates (models/purchase_order.py:221-246). `_prepare_stock_moves` - ADDS: attaches allocations to created receipts (models/purchase_order.py:140-151).
  - `stock.rule._run_buy` - REPLACES core for flagged products: creates/extends a draft request instead of an RFQ; other procurements continue to core (models/stock_rule.py:83-95). ALTERS CORE CONTROL (replenishment: no RFQ for flagged products).
  - `stock.move._action_cancel` - ADDS: creates an activity for the product responsible (models/stock_move.py:49-72). `_merge_moves_fields`, `_prepare_merge_moves_distinct_fields`, `copy_data` - ADD (models/stock_move.py:33-140).
  - `stock.move.line._action_done`, `stock.picking._action_done` - ADD after core: allocate received quantity to requests and post notes (models/stock_move_line.py:69-118; models/stock_picking.py:35-64). Picking override drops the core return value (models/stock_picking.py:36).
  - `stock.warehouse.orderpoint._quantity_in_progress` - ADDS quantities of open requests to the "in progress" figure (models/orderpoint.py:10-22).
- No override touches posting, lock dates, valuation or numbering of core. Approval control is new for requests only. Purchase order approval is untouched here (see purchase_request_level_approve_po).

## 3. New objects, security, automation
- New models: purchase.request, purchase.request.line, purchase.request.allocation, wizard purchase.request.line.make.purchase.order (+item), wizard purchase.request.rejected (models/purchase_request.py:19; models/purchase_request_line.py:18; models/purchase_request_allocation.py:8; wizard/purchase_request_line_make_purchase_order.py:8,318; wizard/purchase_request_rejected.py:6).
- Numbering: sequence code purchase.request, prefix PR, 5 digits, noupdate (data/purchase_request_sequence.xml:5-10); used at create (models/purchase_request.py:33-34, :283-284).
- Groups: Purchase Request User (implies internal user) and Purchase Request Manager (implies user) (security/purchase_request.xml:9-21).
- Record rules: company scope global for request and line (security/purchase_request.xml:22-39); user sees/edits only own requests (:54-63); a user can read requests they follow or own (:40-53); manager unrestricted (:64-72); same three for lines (:73-105).
- ACL: user/manager full on request, line; stock users and purchase users read; only purchase users may use the RFQ wizard (security/ir.model.access.csv:2-18). Rows 19-20 reuse one record id for the rejection wizard, so only one group row survives load (security/ir.model.access.csv:19-20).
- Chatter subtypes for approve/reject/done (data/purchase_request_data.xml:6-29). Report: request print (reports/report_purchase_request.xml, not detailed).
- Automation: no cron of its own; procurement scheduler may create requests through the stock rule; a cron user id in context narrows which draft request is reused (models/stock_rule.py:67-69). External calls: none.

### Purchase request state flow (business language)
- States: Draft, To be approved, Approved, Rejected (models/purchase_request.py:8-14). "Done" is commented out at header level but still in line-level list (models/purchase_request_line.py:12).
1. Draft -> To be approved: button "Request approval", open to any user who can edit; blocked if there is no line with a non-zero quantity that is not cancelled (models/purchase_request.py:316-318, :360-369, :262-267; views/purchase_request_view.xml:24-30).
2. To be approved -> Approved: button "Approve", shown only to Purchase Request Manager group (views/purchase_request_view.xml:25-32). Server rule: if an approver is set on the request, only that user may approve, otherwise the action stops with a message; if none is set, any manager who can see the button can approve, including the requester if he holds the manager group (models/purchase_request.py:320-329; no self-approval check found).
3. To be approved -> Rejected: button "Reject" (manager group) opens a wizard needing a reason; the wizard cancels all lines and writes the reason to chatter only; when no active line remains the request turns Rejected automatically (models/purchase_request.py:331-358; wizard/purchase_request_rejected.py:8-13; models/purchase_request_line.py:336-338).
4. To be approved / Rejected -> Draft: "Reset" (manager group); un-cancels lines and adds one to the revise counter (models/purchase_request.py:312-314; views/purchase_request_view.xml:11-17).
- Editing is locked in To be approved / Approved / Rejected (models/purchase_request.py:49-55); delete allowed only in Draft (models/purchase_request.py:300-310).
- WHO approves: the approver of a request = the approver user set on the requester's employee record (`pr_approver`), pulled by a related field (models/purchase_request.py:82-95; models/hr_employee.py:7). The approver domain refers to the manager group. Multi-level approval is in separate modules (comments at models/purchase_request.py:321, :333) - not read here.
### How a request becomes a purchase order
1. Only Approved requests can be selected; wizard rejects others, a completed line, mixed companies, or mixed picking types (wizard/purchase_request_line_make_purchase_order.py:43-73).
2. Wizard opens from the request header (button "Create RFQ", no group on button) or as a list action on request lines (views/purchase_request_view.xml:33-39; wizard/..._view.xml:52-66); ACL limits actual use to purchase users (security/ir.model.access.csv:17-18). Supplier defaults if all lines share one preferred supplier (wizard/...py:112-114).
3. On confirm, a draft RFQ is created for the supplier (or an existing draft RFQ is chosen), lines are merged with an equal product/unit line unless "copy description" is ticked, a price of zero is set then filled by the core onchange, planned date = line required date; an allocation record links request line to RFQ line; RFQ quantity is recomputed from allocations (wizard/...py:231-304; models/purchase_request_line.py:389-415).
4. RFQ is then handled by core confirmation; on confirm, notes are posted on requests (models/purchase_order.py:80-84); on receipt allocations grow and notes are posted (models/stock_move_line.py:69-118). Request line shows RFQ/PO quantity and purchase status (models/purchase_request_line.py:98-118, :352-374).

## 4. Odoo 19 compatibility (grep in Community 19)
- `groups_id` on users in approver domain: 19 field is `group_ids` (models/purchase_request.py:88 vs core:base/models/res_users.py:257).
- `qty_done` on stock move lines used at models/stock_move_line.py:76, models/stock_move.py:121, models/purchase_request_allocation.py:78; 19 uses `quantity` (core:stock/models/stock_move_line.py:37). Allocation-on-receipt logic likely fails / dependency invalid in 19 (inference; not run).
- `product_uom` on purchase order line (models/purchase_request_allocation.py:116); 19 uses `product_uom_id` (core:purchase/models/purchase_order_line.py:43).
- Allocation lookup maps a field `purchase_request_id` that the allocation model does not define (models/stock_move.py:77-79 vs models/purchase_request_allocation.py:11-70).
- Service-receipt message reads key `product_uom` but sender provides `product_uom_id` (models/purchase_order.py:207 vs :216).
- Hook `_prepare_merge_move_sort_method` not found in core stock move (models/stock_move.py:40 ; core:stock/models/stock_move.py grep no hit). Request line refers to purchase-line state "done" which core 19 order states do not have (models/purchase_request_line.py:357 vs core:purchase/models/purchase_order.py:105-111).
- `get_same_group_uoms` on units of measure not found in Community 19 (models/purchase_request_line.py:212); may come from custom smesplus_uom_ext (not read).
- `create` decorated as single-record but loops as list (models/purchase_request.py:280-290).
- OK items: `_run_buy` pair structure matches (core:purchase_stock/models/stock_rule.py:59-62); `onchange_product_id` exists (core:purchase/models/purchase_order_line.py:382); view anchors found (stock.view_template_property_form core:stock/views/product_views.xml:177; stock.view_stock_move_operations core:stock/views/stock_move_views.xml:120; purchase_order_form). stock_picking_views.xml is not in the manifest data list (__manifest__.py:21-28).

## 5. Custom-to-custom dependencies
- smesplus_uom_ext (__manifest__.py:13; folder addons_Extramodule/addons_extra/smesplus_uom_ext exists, not read). Downstream: purchase_request_level_approve_po depends on purchase_request_level_approve.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: content of the second folder named purchase_request under addons/ and which copy is loaded.
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of `pr_approver` when a user has several employee records (multi-company), since the related field takes one.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether automatic tests pass on 19 (tests exist: purchase_request/tests/*.py; not run).
