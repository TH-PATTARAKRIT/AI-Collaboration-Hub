> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_inventory_lot_filter

Module: smesplus_inventory_lot_filter ("SMEsPlus Stock Lot/Serial Filter")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 19.0.1.1
Path: addons_Extramodule/addons_extra/smesplus_inventory_lot_filter
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom

## 1. Business capability
- Narrows the lot/serial choices offered to the warehouse user so that only stock that actually exists is proposed.
  - In the detailed-operations popup of a transfer line: the "Pick From" choice lists only stock records for the product under the source location (and its child locations); for deliveries and for manufacturing component consumption it also requires a positive quantity (smesplus_inventory_lot_filter/models/stock_move_line.py:6-13; views/stock_move_operations_view.xml:9-14).
  - On the scrap form: the lot choice lists only lots of the product with positive on-hand quantity (models/stock_scrap.py:6-10; views/stock_scrap_view.xml:9-14).
- Purpose given in manifest: hide lot records that have no on-hand quantity (__manifest__.py:1-22).

## 2. Attachment to CORE
- Core modules depended on: base, stock, mrp (__manifest__.py:1-22).
- stock.move.line (core:stock/models/stock_move_line.py): new helper field filter_quant_ids (models/stock_move_line.py:6). Existing dummy field quant_id "Pick From" (core:stock/models/stock_move_line.py:93) gets its domain restricted in view (views/stock_move_operations_view.xml:12-14; core:stock/views/stock_move_views.xml:166, 235). Uses core fields picking_code (core:stock/models/stock_move.py:175) and, from mrp, raw_material_production_id (core:mrp/models/stock_move.py:33).
- stock.scrap (core:stock/models/stock_scrap.py:30): new helper field lot_ids (models/stock_scrap.py:6); domain on lot_id restricted in view (views/stock_scrap_view.xml:12-14). Uses lot on-hand quantity field (core:stock/models/stock_lot.py:53).
- Core method overrides: none. Only computed helper fields plus view domains.
- ALTERS CORE CONTROL: no in the strict sense; it is a UI input filter. Valuation and reservation logic untouched. Because it is only a view domain, API/import writes are not restricted by it.

## 3. New objects, security, automation, external calls
- New models: none (both classes extend existing models). Security: none shipped. No cron / server action / external call.
- Both compute methods perform one database search per computation (models/stock_move_line.py:12; models/stock_scrap.py:10).

## 4. Odoo 19 compatibility
- Checked in Community 19: view ids stock.view_stock_move_line_operation_tree (core:stock/views/stock_move_views.xml:166) and stock.stock_scrap_form_view (core:stock/views/stock_scrap_views.xml:24) exist; quant_id field present in view (core:stock/views/stock_move_views.xml:175).
- Potential defects (from code reading, not run):
  - The compute methods address the record set as a single record (models/stock_move_line.py:9-13, models/stock_scrap.py:9-11) without iterating and without dependency declaration; with several records in one batch this pattern is fragile.
  - Both classes extend real (stored) models but are declared with the abstract-model base class (models/stock_move_line.py:3, models/stock_scrap.py:3). Core only rejects the opposite direction, i.e. an abstract target extended by a concrete class (core:odoo/orm/model_classes.py:234-238); the effect of an abstract extension on a concrete model was not determined.
  - The helper field on move line is a many-to-many computed without store; the source location is taken from the parent move (models/stock_move_line.py:9), so lines without a move get an empty location filter.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the abstract-base declaration makes the module load and work cleanly in Odoo 19 (no runtime observation).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior with multi-record computation (list view, batch).
- UNKNOWN - EVIDENCE INSUFFICIENT: why mrp is a declared dependency beyond the component-consumption branch at models/stock_move_line.py:10.
