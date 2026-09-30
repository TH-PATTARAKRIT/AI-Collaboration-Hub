> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_inventory_lot_filter

Module: scgl_inventory_lot_filter
License (confirmed in manifest): LGPL-3 (scgl_inventory_lot_filter/__manifest__.py:9)
Author (manifest): SCG Legacy (scgl_inventory_lot_filter/__manifest__.py:7)
Version (manifest): 19.0.1.1 (scgl_inventory_lot_filter/__manifest__.py:3)
Path: addons_Extramodule/addons/scgl_inventory_lot_filter
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- On the scrap form, the lot/serial picker offers only lots of the chosen product that currently have on-hand quantity above zero (scgl_inventory_lot_filter/models/stock_scrap.py:6-11; scgl_inventory_lot_filter/views/stock_scrap_view.xml:9-14).
- On the detailed-operations list of a stock move, the "Pick From" choice is limited to stock at the move's source location and below for the same product; for outgoing transfers and manufacturing component consumption it also requires positive quantity (scgl_inventory_lot_filter/models/stock_move_line.py:6-13; scgl_inventory_lot_filter/views/stock_move_operations_view.xml:9-14).
- Purpose stated in manifest summary: hide lots with no on-hand quantity (scgl_inventory_lot_filter/__manifest__.py:4).

## 2. Attachment to CORE
- stock.scrap: ADDS a helper field `lot_ids` (computed, not stored) and narrows the domain of core field `lot_id` on the form (core:stock/views/stock_scrap_views.xml:60). No core method overridden. Filters a picker only; does not add a save-time validation, so a lot chosen by other means (import, code) is not blocked.
- stock.move.line: ADDS helper field `filter_quant_ids` and narrows the domain of `quant_id` (core:stock/models/stock_move_line.py:93 is a non-stored dummy field) in the operations list (core:stock/views/stock_move_views.xml:166). No core method overridden.
- Uses `product_qty` of stock.lot (on-hand quantity, computed) (core:stock/models/stock_lot.py:53), `picking_code` on stock.move (core:stock/models/stock_move.py:175) and mrp `raw_material_production_id` (core:mrp/models/stock_move.py:33).
- Nothing here BLOCKS/ALTERS posting, lock dates, valuation, numbering. No ALTERS CORE CONTROL identified; it is a UI narrowing only.

## 3. New objects, security, automation, external calls
- No new models, ACLs, record rules, crons, server actions, or external calls.
- Company scoping: the helper searches are made under the current user's rights and companies (scgl_inventory_lot_filter/models/stock_scrap.py:10; scgl_inventory_lot_filter/models/stock_move_line.py:12), no explicit company filter.
- Both classes are declared with the abstract-model base while extending concrete models (scgl_inventory_lot_filter/models/stock_scrap.py:3; scgl_inventory_lot_filter/models/stock_move_line.py:3).

## 4. Odoo 19 compatibility
- Referenced views and fields exist in Community 19: form `stock.stock_scrap_form_view` (core:stock/views/stock_scrap_views.xml:24), list `stock.view_stock_move_line_operation_tree` (core:stock/views/stock_move_views.xml:166), `quant_id` in that list (core:stock/views/stock_move_views.xml:182, 235), `lot_id` (core:stock/models/stock_scrap.py:30).
- The two compute methods read fields from `self` as single-record values without looping or dependency declaration (scgl_inventory_lot_filter/models/stock_scrap.py:9; scgl_inventory_lot_filter/models/stock_move_line.py:9-12). With more than one record in the recordset this pattern normally raises a single-record error; forms load one record, list editing may load several. Risk noted, not run-tested.
- Manifest declares `mrp` as dependency though only one mrp field is used (scgl_inventory_lot_filter/__manifest__.py:10-14).

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether extending a model with an abstract-model class base behaves correctly in the Community 19 registry (not run).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior when the selected product is untracked or has no source location (empty search, filter becomes empty list).
- UNKNOWN - EVIDENCE INSUFFICIENT: performance on databases with many quants (search is unbounded per record).
