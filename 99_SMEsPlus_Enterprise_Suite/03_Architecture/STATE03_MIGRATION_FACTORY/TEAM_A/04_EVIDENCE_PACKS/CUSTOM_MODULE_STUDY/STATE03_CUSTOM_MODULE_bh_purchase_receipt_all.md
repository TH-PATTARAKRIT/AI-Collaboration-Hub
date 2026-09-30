> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: bh_purchase_receipt_all

- Module: bh_purchase_receipt_all
- License (confirmed in manifest): LGPL-3 (bh_purchase_receipt_all/__manifest__.py:14)
- Author (manifest): SCGL (bh_purchase_receipt_all/__manifest__.py:6)
- Version (manifest): 19.0.1.0.0 (bh_purchase_receipt_all/__manifest__.py:4)
- Path: addons_Extramodule/addons/bh_purchase_receipt_all
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a smart button on the purchase order showing all receipts of the order including back orders and back orders of back orders, at any depth (models/purchase_order.py:21-36; views/purchase_order_views.xml:16-29).
- Opens the receipt list (or the single receipt form) filtered to those documents (models/purchase_order.py:55-74).

## 2. Attachment to CORE
- `purchase.order` (core:purchase_stock/models/purchase_order.py): ADDS two computed, non-stored fields: the set of all related receipts and its count (models/purchase_order.py:8-16, 41-50). Core `picking_ids` (core:purchase_stock/models/purchase_order.py:22, 45-47) lists only receipts directly linked to order lines; this module extends that set by following the back-order link of each transfer (core:stock/models/stock_picking.py:560).
- ADDS action `bh_action_view_all_receipts`; reuses core action `stock.action_picking_tree_all` and core views `stock.vpicktree` and `stock.view_picking_form` (core:stock/views/stock_picking_views.xml:412, 66, 110). It sets a default partner in the context.
- View `purchase.purchase_order_form` (core:purchase/views/purchase_views.xml:126): new button placed after the core receipt button that purchase_stock adds (core:purchase_stock/views/purchase_views.xml:15-20). The new button carries no group restriction while the core button is restricted to stock users (core:...:19); this is view visibility only.
- No override of a core method. Core-control impact: none (read-only navigation). Record rules of the current user apply to the picking search because no elevated access is used (models/purchase_order.py:30). ALTERS CORE CONTROL: not found in code read.

## 3. New objects, security, automation, external calls
- New models, groups, ACLs, record rules, crons, server actions, external calls: none.

## 4. Odoo 19 compatibility
- Checked by grep in Community tree: `purchase.order.picking_ids` exists; `stock.picking.backorder_id` exists; `action_view_picking` button and `oe_button_box` anchor exist; the three stock XML ids exist (pointers above). No mismatch found.

## 5. Custom-to-custom dependencies
- None declared (depends: purchase, stock, purchase_stock; manifest:8).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: performance for orders with many back-order chains (one search per depth level, models/purchase_order.py:30-35); no data volume evidence.
- UNKNOWN - EVIDENCE INSUFFICIENT: receipts split by another route (not via the back-order link) would not be included; not tested.
