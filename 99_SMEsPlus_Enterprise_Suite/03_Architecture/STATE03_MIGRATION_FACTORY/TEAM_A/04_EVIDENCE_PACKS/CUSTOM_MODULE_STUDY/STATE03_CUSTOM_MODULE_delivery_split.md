> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: delivery_split

- Module: delivery_split
- License (confirmed in manifest): AGPL-3 (delivery_split/__manifest__.py:39)
- Author (manifest): Cybrosys Techno Solutions (delivery_split/__manifest__.py:30)
- Version (manifest): 19.0.1.0.0 (delivery_split/__manifest__.py:24)
- Path: addons_Extramodule/addons/delivery_split
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Allows one sales order to ship to several recipients: each order line carries a recipient, and deliveries are created per recipient (manifest description, delivery_split/__manifest__.py:27-29; models/sale_order_line.py:29-34).
- Two order-level switches: "Delivery Split" and "Consolidate Orders" (models/sale_order.py:30-37). With split on and consolidate off, every stock move gets its own delivery; with consolidate on, moves with the same recipient share one delivery (models/stock_move.py:34-46, 53-65).
- Sales analysis gains delivery reference, delivery status, delivery date (done date) and delivery contact (report/sale_report.py:7-32; views/sale_report_view.xml:7-11).

## 2. Attachment to CORE
- `sale.order`: ADDS the two flags (form fields placed after the shipping address, readonly once state is sale, views/sale_order_views.xml:9-14). ADDS an on-change on customer that overwrites every line recipient with the new customer when split is on (models/sale_order.py:39-45), which would discard per-line recipients already chosen.
- `sale.order.line`: ADDS `recipient_id` (models/sale_order_line.py:29-34). Overrides `_prepare_procurement_values` (core:sale_stock/models/sale_order_line.py:284): ADDS behavior after core: passes the recipient as the partner in the procurement values when split is on (models/sale_order_line.py:56-57); core rule uses that value as delivery partner (core:stock/models/stock_rule.py:337, 363). It also writes the customer into the line recipient whenever empty, regardless of the split flag (models/sale_order_line.py:53-54). The field is not shown on the order-line grid (view block commented out, views/sale_order_views.xml:15-20).
- `stock.move._key_assign_picking` (core:stock/models/stock_move.py:1527): ADDS to the grouping key (order id, plus move id or recipient) when split is on (models/stock_move.py:30-46). ALTERS CORE CONTROL (delivery grouping rule) only for split orders.
- `stock.move._search_picking_for_assignation` (core:stock/models/stock_move.py:1544): REPLACES core behavior for split orders. Not consolidated: never reuses a delivery. Consolidated: searches by recipient and sales order and four states only (models/stock_move.py:53-65); core criteria (references, source and destination locations, operation type, printed flag, partially-available state) are not applied on this path (core:stock/models/stock_move.py:1534-1541). Result: moves of different operation types of the same order and recipient could be attached to one transfer. ALTERS CORE CONTROL (transfer assignment criteria; no accounting effect found).
- `sale.report` (core:sale/report/sale_report.py:172 hook `_select_additional_fields`, `_from_sale` :180, `_group_by_sale` :198): ADDS columns and joins to stock moves and outgoing transfers (report/sale_report.py:26-51). One-to-many join can repeat sale lines once per move/transfer, so summed sales figures may be inflated where a line has several moves (join at report/sale_report.py:36-45; core sums grouped without line id, core:sale/report/sale_report.py:198-227). Not run.
- Pivot view `sale.view_order_product_pivot` (core:sale/report/sale_report_views.xml:4) extended with the delivery fields.
- Posting, lock dates, valuation, approvals, security rules, multi-company, numbering: not touched. ALTERS CORE CONTROL: only the transfer-grouping items above.

## 3. New objects, security, automation, external calls
- New models: none. New security: none (no ACL, groups or rules in manifest data). Crons/server actions/external calls: none.
- The recipient domain restricts to partners of the current company or shared partners, written with a function inside the domain (models/sale_order_line.py:32-34).

## 4. Odoo 19 compatibility
- Checked by grep in Community tree.
- Confirmed present: `_key_assign_picking`, `_search_picking_for_assignation` (core:stock/models/stock_move.py:1527, 1544), `sale.order.line._prepare_procurement_values` (core:sale_stock/models/sale_order_line.py:284; the core signature takes no extra arguments, module passes kwargs through, models/sale_order_line.py:49-51), `stock.picking.sale_id` (core:sale_stock/models/stock.py:187), `_select_additional_fields` returning a mapping (core:sale/report/sale_report.py:172-178).
- Possible mismatch: core `_key_assign_picking` and picking search use `reference_ids` rather than a procurement group (core:stock/models/stock_move.py:1527-1541); the module's replacement search no longer uses them. `_onchange_product_template_id` is called on super only if it exists (models/sale_order_line.py:40-42); it does not exist in the Community 19 sale order line (grep negative).
- Function inside a domain list (models/sale_order_line.py:32-34) may not be evaluated as intended; effect unverified.

## 5. Custom-to-custom dependencies
- None declared (depends: sale_management, stock; manifest:34).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: how users enter per-line recipients, since the line column is commented out (views/sale_order_views.xml:15-20).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior with multi-step delivery routes (pick/pack/ship) under the replaced picking-search rule.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether Sales Analysis totals are inflated in practice (needs data test).
- UNKNOWN - EVIDENCE INSUFFICIENT: invoicing/delivery address effects on the invoice; invoice partner logic not touched in code read.
