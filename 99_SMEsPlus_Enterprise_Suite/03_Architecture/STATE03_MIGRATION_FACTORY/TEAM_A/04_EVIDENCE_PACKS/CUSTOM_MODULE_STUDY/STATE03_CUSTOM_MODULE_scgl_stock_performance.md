> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_stock_performance

Module: scgl_stock_performance ("SMEsPlus - Warehouse Performance")
License (confirmed in manifest): LGPL-3
Author (manifest): SCG Legacy (Thailand) Co., Ltd.
Version (manifest): 19.0.1.1.0
Path: Extra_Module_scgl/scgl_stock_performance
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_06): Customer-authorized Custom

## 1. Business capability
- Adds a read-only reporting screen "Warehouse Analysis" under Inventory > Reporting, built only from transfers that are already done (scgl_stock_performance/models/stock_performance.py:1-5, 63).
- Two measures per completed transfer: delay (actual transfer date minus scheduled date, in days, positive = late) and cycle time (actual transfer date minus creation date, in days) (models/stock_performance.py:31-34).
- Flags per transfer: late, backorder, plus count of completed stock moves (models/stock_performance.py:35-37).
- Views: weekly line chart, pivot (operation type by month, delay and cycle-time measures), list with totals/averages, and a search view with receipt/delivery/internal, late and backorder filters (views/stock_performance_views.xml:5-77).
- Default action opens filtered to deliveries and the current month (views/stock_performance_views.xml:85).

## 2. Attachment to CORE
- Core module depended on: stock (__manifest__.py:1-17).
- Reads (does not change) core objects: stock.picking (scheduled date core:stock/models/stock_picking.py:595, deadline :599, transfer date :606, backorder link :560, responsible :637), stock.picking.type (operation code core:stock/models/stock_picking.py:42, warehouse :49), stock.move state (done count) (models/stock_performance.py:60).
- Menu is placed under the core Inventory > Reporting menu (views/stock_performance_views.xml:93; core:stock/views/stock_menu_views.xml:36).
- Core method overrides: none. No core field added, no default changed, no validation changed.
- ALTERS CORE CONTROL: no.

## 3. New objects, security, automation, external calls
- New object: scgl.stock.performance, a database-view-backed model, not a stored table (models/stock_performance.py:10-13, 39-41). Fields are all read-only.
- ACL: one line, read-only for the core Inventory User group (security/ir.model.access.csv:2). Menu restricted to the same group (views/stock_performance_views.xml:94).
- Record rules: none shipped. The model carries a company field (models/stock_performance.py:26) but no company-scoping rule exists in the module; core rules are attached per model, so none of the core stock.picking rules cover this new model (inference). Company isolation of the report is therefore not enforced by this module.
- Cron / server actions: none. External calls: none.
- Tests present: tests/test_stock_performance.py:8-72 (receipt late/cycle, delivery on-time and filters, menu/action wiring).

## 4. Odoo 19 compatibility
- Checked in Community 19: stock.picking date_done, scheduled_date, date_deadline, backorder_id, user_id; stock.picking.type code and warehouse_id; stock.group_stock_user; menu stock.menu_warehouse_report - all present (pointers in section 2).
- Observation: the parent menu core:stock/views/stock_menu_views.xml:36 is limited to the stock manager group, while this module's menu declares the lighter Inventory User group (views/stock_performance_views.xml:94). Whether a user with only the lighter group can reach the entry is not confirmed at runtime.
- The act_window "path" attribute and graph/pivot attribute usage were not checked.

## 5. Custom-to-custom dependencies
- None declared (depends only on stock).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the SQL view is refreshed correctly when other modules add picking states or when pending ORM writes are unflushed (the test itself flushes first, tests/test_stock_performance.py:29).
- UNKNOWN - EVIDENCE INSUFFICIENT: runtime behavior of multi-company users on this report (no rule found in module; no runtime observation).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the "Boss 25/09" comments (views/stock_performance_views.xml:4, 92) reflect an approved requirement document.
