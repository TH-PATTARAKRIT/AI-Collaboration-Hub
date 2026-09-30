> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: courier_type

- Module: courier_type
- License (confirmed in manifest): LGPL-3 (courier_type/__manifest__.py:8)
- Author (manifest): SMEsPlus (courier_type/__manifest__.py:6)
- Version (manifest): 19.0.1.0.0 (courier_type/__manifest__.py:3)
- Path: addons_Extramodule/addons_extra/courier_type
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Maintains a list of courier job codes ("Courier Type": job code, title, remark, transfer number, route, active/blocked service status, courier partner) (courier_type/models/is_courier.py:4-33; views/is_courier_view.xml:71-84).
- Partners can be flagged as couriers and can carry a list of job codes with an Active/Block status each (models/res_partner.py:6-13; models/courier_type_line.py:4-22; views/res_partner_view.xml:12-28).
- A courier job code (and a free-text "port") is chosen on purchase orders and sales orders, copied to receipts/deliveries, to invoices, and (for lots) to lots, quants and move lines for display and grouping (models/purchase_order.py:7-13, 32-37; models/sale_order.py:6-40; models/stock_lot.py:8; models/stock_quant.py:7-8; models/stock_move_line.py:7; models/account_move.py:7-8). Purchase analysis gains group-by courier type and a line description (models/purchase_report.py:8-29).
- Menu: Courier Type under Purchase configuration (views/is_courier_view.xml:83).

## 2. Attachment to CORE
- `purchase.order` (purchase): ADDS fields courier type set + selected job code (computed from vendor's active job codes); default job code is taken from the first order found that has any (models/purchase_order.py:25-30). Overrides `_prepare_picking`: ADDS behavior after core (copies job code to the receipt) (models/purchase_order.py:32-37; core:purchase_stock/models/purchase_order.py:360).
- `sale.order` (sale, sale_stock): ADDS port, courier flag, job code fields (non-stored) (models/sale_order.py:6-24). Overrides `_prepare_invoice` (ADDS port and job code to the invoice values, core:sale/models/sale_order.py:1413), `action_confirm` (ADDS: after core, writes job code onto the order's deliveries, core:sale/models/sale_order.py:1168), `create` and `write` (ADDS: fill job code from partner defaults; models/sale_order.py:91-103). The `write` override sets job code to the last available option whenever it is not in the written values, so a user's earlier choice may be replaced on any later save (models/sale_order.py:99-103).
- `stock.move.line._get_value_production_lot`: overridden to copy the receipt's job code to newly created lots (models/stock_move_line.py:9-13). See section 4: this hook does not exist in Community 19.
- `res.partner` (base): ADDS courier flag, job-code lines; overrides `write` (ADDS behavior after core: synchronises a mirror table "courier.type.customers" with the partner's job-code lines, creating/updating/removing rows) (models/res_partner.py:23-63). Declared with the model-level decorator instead of the record-level one (models/res_partner.py:23).
- `type.courier.unlink`: blocks deletion when a partner uses the job code, asks to archive (models/is_courier.py:44-52). Applies only to this module's own model.
- Other: `stock.picking` gets job code and a stored port copied from the sales order (models/stock_picking.py:7-21); `stock.lot`, `stock.quant`, `stock.move.line`, `account.move`, `purchase.report` get display fields.
- Core controls: nothing found that blocks or alters posting, lock dates, valuation, approvals, numbering. The Block status is informational at picking level; no code was found refusing a document when a courier is blocked (the Block status only filters the choice list, models/sale_order.py:48-49; models/purchase_order.py:21). ALTERS CORE CONTROL: not found in code read.

## 3. New objects, security, automation, external calls
- New models: type.courier, courier.type.line, courier.type.customers (models/__init__.py:1-3).
- ACL: all three models are readable, writable, creatable and deletable by every internal user (security/ir.model.access.csv:2-4). No groups defined, no record rules, no company field on the new models, so no company scoping.
- Crons, server actions, external calls: none.
- Unused/dead helpers: `check_customer_ids` on type.courier and res.partner (models/is_courier.py:35-42; models/res_partner.py:15-21; the latter assigns a field that is not defined on res.partner in this module).

## 4. Odoo 19 compatibility
- Checked by grep in Community tree.
- MISMATCH: `_get_value_production_lot` on stock.move.line not found anywhere in Community 19 addons; lot creation uses `_prepare_new_lot_vals` (core:stock/models/stock_move_line.py:746, 756). The override at models/stock_move_line.py:9-13 would never run, so job code is likely not copied to auto-created lots (and therefore not to quants).
- RISK: `@api.model` on `write` (models/res_partner.py:23) and on `create` (models/sale_order.py:91). In Community 19 a method marked as model-level is called on an empty recordset from RPC (core:odoo/service/model.py:83-89), and the multi-record wrapper is only applied by the create-multi decorator (core:odoo/orm/decorators.py:357-371). Effect: direct RPC `write` on partners would receive an unexpected argument; `create` on sale.order called with a single mapping would iterate the mapping instead of a list. Not run; behavior unverified.
- Typos in declarations: `stirng=` (models/is_courier.py:11; views/is_courier_view.xml:17); `tracking=True` on models without chatter (models/is_courier.py:15,18; models/courier_type_line.py:18).
- Present in core 19: `purchase.report._select/_group_by` returning SQL objects (core:purchase/report/purchase_report.py:55-60, 123), aliases `po` and `l` (lines 63, 102); `stock.picking.sale_id` (core:sale_stock/models/stock.py:187); widget `sol_o2m` (core:sale/static/src/js/sale_order_line_field/sale_order_line_field.js:234); view anchors sale_shipping, other_tab_group/sale_info_group, group_product_id (core pointers: sale/views/sale_order_views.xml:897; account/views/account_move_views.xml:1510-1512; purchase/report/purchase_report_views.xml:72).
- The `sol_o2m` widget is a sale-order-line widget reused on partner and courier forms (views/res_partner_view.xml:14; views/is_courier_view.xml:32); suitability not verified.

## 5. Custom-to-custom dependencies
- None declared (depends: purchase, stock, sale, sale_stock; manifest:9-14).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the sales-order job code and port persist in the database; the fields are declared non-stored without a compute (models/sale_order.py:6, 15-23) yet are read on confirm and on invoicing.
- UNKNOWN - EVIDENCE INSUFFICIENT: the business meaning of "Job Code", "Transfer Number", "Route", "Port" (manifest description only says "Custom any for SWR", manifest:4).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the "Block" status is meant to prevent transactions; no enforcing code found.
- UNKNOWN - EVIDENCE INSUFFICIENT: intended default rule for job code on new purchase orders (takes another order's value, models/purchase_order.py:25-30).
