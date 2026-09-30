> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_report_viewer_deferred

## 0. Header
- Module: scgl_report_viewer_deferred
- License (confirmed in manifest): AGPL-3 (scgl_report_viewer_deferred/__manifest__.py:9)
- Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_report_viewer_deferred/__manifest__.py:10)
- Version (manifest): 19.0.1.0.0 (scgl_report_viewer_deferred/__manifest__.py:7)
- Path: Extra_Module_scgl/scgl_report_viewer_deferred
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Bridge that shows two accounting reports, Deferred Revenue and Deferred Expense, inside the company's single report viewer (module scgl_report_viewer) instead of the pivot view of scgl_account_deferred (manifest:5-6).
- Report layout: one group per account, one row per deferral schedule with period, total amount, amount before the period, in the period, after the period, and remaining at end; drill-down to the schedule record; group and grand totals (models/report_engine_deferred.py:33-70). Option "posted only" defaults to true (:35, :46).
- Export from the viewer for these two kinds opens the original pivot action of scgl_account_deferred, from which spreadsheet export is possible (models/report_engine_deferred.py:26-31).
- Two client actions and a rewiring of two existing menus to them (views/actions.xml:3-18). This changes which screen the existing menu entries open; nothing is hidden and no access right changes.

## 2. Attachment to CORE
- Depends declared: scgl_report_viewer and scgl_account_deferred (manifest:12); `auto_install` true (manifest:16), so it installs itself when both are present.
- Core Community objects: `ir.actions.client` (core:base/models/ir_actions.py:1427) for the two actions and `ir.ui.menu` for menu action replacement (menu action is a reference field, core:base/models/ir_ui_menu.py:35; XML `ref` on reference fields handled at core:odoo/tools/convert.py:422). `ir.actions.act_window` XML-id lookup for the export. No core method overridden; no ALTERS CORE CONTROL.
- Overrides of custom-module methods (by name): `_oca_report` (models/report_engine_deferred.py:21-24: ADDS branch for kinds "dr" and "de", else delegates) and `_oca_export` (:26-31: ADDS branch). Also mutates the shared kind registries of the viewer at import time (:14-15).
- The menu records `scgl_account_deferred.menu_scgl_deferred_revenue_report` and `..._expense_report` are modified from this module (views/actions.xml:13-18): REPLACES the target action of those menus (custom-to-custom).

## 3. New objects, security, automation, external calls
- New models/fields/ACLs/groups/rules: none. Reads `scgl.deferred.schedule` and its lines with the caller's rights (no elevation in the file), filtered to the current company only (models/report_engine_deferred.py:36-38).
- Company scoping: single current company (`env.company`) rather than all allowed companies (:36) — multi-company consolidated view not offered (inference).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Core objects referenced exist (see pointers). Fields of the deferral schedule (partner, move line, product, move, account, line states) belong to scgl_account_deferred and are not in Community; not checkable here.
- Licence note: the header comment states AGPL-3 (scgl_report_viewer_deferred/__manifest__.py:2) and the summary notes the neighbouring module is LGPL-3 (:5); not a compatibility item, only a licence-mix note for governance.
- Uses of removed core API: none found.

## 5. Custom-to-custom dependencies
- scgl_report_viewer (report engine, kinds registry, client action tag `scgl_report_viewer`) and scgl_account_deferred (schedule model, pivot actions, menu ids). Neither is in this assignment; behaviour described only as far as referenced here.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: the structure of the viewer engine (cell helpers, format helpers) used at models/report_engine_deferred.py:50-69.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether access to the report is limited by group in scgl_account_deferred (the menus are inherited from that module).
