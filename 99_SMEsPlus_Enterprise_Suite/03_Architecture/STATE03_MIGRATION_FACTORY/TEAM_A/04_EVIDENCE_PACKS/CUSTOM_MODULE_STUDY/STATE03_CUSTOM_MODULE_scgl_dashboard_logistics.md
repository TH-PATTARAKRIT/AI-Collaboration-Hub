> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_dashboard_logistics

Module: scgl_dashboard_logistics
License (confirmed in manifest): LGPL-3 (scgl_dashboard_logistics/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_dashboard_logistics/__manifest__.py:8)
Version (manifest): 19.0.1.0.1 (scgl_dashboard_logistics/__manifest__.py:5)
Path: Extra_Module_scgl/scgl_dashboard_logistics
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds four published dashboards to the core "Logistics" dashboard group: Warehouse Daily Overview (transfers), Operation Analysis (stock moves), Purchase & Vendors (purchase analysis), Manufacturing (manufacturing orders) (scgl_dashboard_logistics/data/dashboards.xml:6-41).
- Each is a stored spreadsheet document driven by pivot definitions on the underlying model, with a date filter (scgl_dashboard_logistics/tests/test_dashboards.py:47-49):
  - Warehouse Daily: stock.picking, counts by operation type (scgl_dashboard_logistics/data/files/warehouse_daily_dashboard.json).
  - Operation Analysis: stock.move, quantity by product / operation type / destination location (scgl_dashboard_logistics/data/files/operation_analysis_dashboard.json).
  - Purchase & Vendors: purchase.report, totals, ordered/received/billed quantities by vendor, buyer, product, category (scgl_dashboard_logistics/data/files/purchase_vendors_dashboard.json).
  - Manufacturing: mrp.production, counts and quantity by state and product (scgl_dashboard_logistics/data/files/manufacturing_dashboard.json).
- Order relative to a core "Warehouse Metrics" dashboard is fixed by sequences 100/200/400/500 (scgl_dashboard_logistics/data/dashboards.xml:5; test at scgl_dashboard_logistics/tests/test_dashboards.py:39-41).

## 2. Attachment to CORE
- Creates data records of core model spreadsheet.dashboard (core:spreadsheet_dashboard/models/spreadsheet_dashboard.py:14, 17, 19, 31). No Python code, no core method overridden. ADDS data only.
- Group: core `spreadsheet_dashboard_group_logistics` (core:spreadsheet_dashboard/data/dashboard.xml:29).
- Visibility by role: stock users for Warehouse Daily and Operation Analysis; purchase users for Purchase & Vendors; manufacturing users for Manufacturing (scgl_dashboard_logistics/data/dashboards.xml:11, 20, 29, 38). Main data models linked: stock.picking, stock.move, purchase.report, mrp.production (lines 9, 18, 27, 36).
- Read-only analytics; posting, lock dates, valuation, numbering, approvals untouched. No ALTERS CORE CONTROL identified.

## 3. New objects, security, automation, external calls
- No new models, ACLs, record rules, crons, server actions or external calls.
- Data access is through the pivot reads of the viewer's own rights (core spreadsheet behavior; not traced). The purchase report is a database view without company field checks in this module: multi-company behavior UNKNOWN.

## 4. Odoo 19 compatibility
- All measures/groupings named in the JSON exist in Community 19: purchase.report fields product_id, partner_id, user_id, price_total, category_id, order_id, untaxed_total, qty_ordered, qty_received, qty_billed (core:purchase/report/purchase_report.py:27-51); mrp.production product_qty and state (core:mrp/models/mrp_production.py:112, 177); stock.move quantity (core:stock/models/stock_move.py:171). Fields `picking_type_id`, `location_dest_id` exist on stock.picking and stock.move (core:stock/models/stock_picking.py:613, 620; core:stock/models/stock_move.py:81, 150).
- Core dependencies purchase/stock/mrp/spreadsheet_dashboard exist. Groups referenced exist (core:stock/security/stock_security.xml:10; core:purchase/security/ with group_purchase_user; core:mrp/security/ with group_mrp_user).
- The module's tests compare each measure and group-by with the live model fields (scgl_dashboard_logistics/tests/test_dashboards.py:43-75); not run.
- Spreadsheet format/version compatibility with the 19 viewer: not run.

## 5. Custom-to-custom dependencies
- None declared (scgl_dashboard_logistics/__manifest__.py:10).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the purchase.report "received/billed" measures match the business's definitions.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the dashboards render correctly on the target version (not run).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior with several companies selected.
