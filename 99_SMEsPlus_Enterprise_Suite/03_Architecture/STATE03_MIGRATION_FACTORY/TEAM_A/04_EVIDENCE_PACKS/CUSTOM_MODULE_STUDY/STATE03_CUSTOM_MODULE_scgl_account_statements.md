> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_statements

Module: scgl_account_statements
License (confirmed in manifest): AGPL-3 (scgl_account_statements/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:8)
Version (manifest): 19.0.1.1.0 (__manifest__.py:5)
Path: Extra_Module_scgl/scgl_account_statements
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Live, drill-down financial statements built as configuration data for the OCA report builder (mis_builder): Balance Sheet, Profit and Loss, Cash Flow (indirect method), Executive Summary (data/mis_reports.xml:16, 143, 216, 322; PROVENANCE.txt:5,10-16).
- Each statement is a report definition (76 KPI rows, 10 style records) plus a ready-made report instance with comparison periods: balance sheet today vs prior year-end; P&L year-to-date, prior year, this month; cash flow year-to-date and prior year; executive summary this month, last month, year-to-date (data/mis_reports.xml:426-439). All instances show posted entries only (target_move = posted, lines 426,429,433,436).
- Rows are defined by core account type values, so they work with any chart of accounts (manifest summary __manifest__.py:3-4; PROVENANCE.txt line 10).
- Executive Summary sections: Cash, Profitability, Balance Sheet, Performance (PROVENANCE.txt:13-16).
- Menus open each instance directly under Reporting > Statement Reports (views/menus.xml:4-42).
- Module contains no Python or JS (PROVENANCE.txt:5; file list shows only data, views, tests).

## 2. Attachment to CORE
- core:account: depends on it (__manifest__.py:10) for account types and the Reporting menu.
  - Account types used in report formulas: asset_cash, asset_current, asset_fixed, asset_non_current, asset_prepayments, asset_receivable, equity_unaffected, expense_depreciation, expense_direct_cost, income_other, liability_credit_card, liability_current, liability_non_current, liability_payable (data/mis_reports.xml, various). All exist in core 19 (core:account/models/account_account.py:44-64).
  - Menu parent account.menu_finance_reports (views/menus.xml:37; core:account/views/account_menuitem.xml:37). New parent menu "Statement Reports" restricted to group account.group_account_readonly (views/menus.xml:37-38).
- No core model is extended and no core method is overridden. Overrides of core methods by name: none. No core control is changed. Not `ALTERS CORE CONTROL`.
- Other module attachment (non-core): creates records of mis_builder models mis.report, mis.report.kpi, mis.report.style, mis.report.instance, mis.report.instance.period (data/mis_reports.xml:6-16, 426-439) and window actions on mis.report.instance using the mis_builder result form (views/menus.xml:4-35).
- Data is loaded with update mode on (noupdate="0", data/mis_reports.xml:2): a module upgrade overwrites local edits of these report definitions.

## 3. New objects, security, automation, external calls
- New models: none. ACLs: none. Groups: none. Record rules: none in this module. Company scoping is entirely from mis_builder and core rules; the instances carry no company setting in the data (data/mis_reports.xml:426-436). Whether they follow the user's active companies is UNKNOWN - EVIDENCE INSUFFICIENT.
- Child menus (balance sheet, P&L, cash flow, executive summary) have no groups of their own and inherit the parent's group (views/menus.xml:39-42).
- Crons / server actions / external calls: none found.
- Formulas use mis_builder expression functions for balance, period balance, initial balance and ending balance (counts: 21 ending, 19 period, 2 unallocated, 1 initial; data/mis_reports.xml, by pattern count).

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Core-side references verified: account type values (above), menu id menu_finance_reports.
- Depends on OCA mis_builder (__manifest__.py:10), not in the Community tree; the model and field names used in the data records and the view id mis_builder.mis_report_instance_result_view_form (views/menus.xml:8) are `not checked`. PROVENANCE.txt:7 names the version studied by the authors as 19.0.1.2.1.
- Expressions reference no core model field except account type values; no mismatch found on the core side.

## 5. Custom-to-custom dependencies
- None declared (depends account and mis_builder only). Used by scgl_account_menu, which re-parents these menu ids: menu_balance_sheet, menu_profit_loss, menu_cash_flow, menu_executive_summary, menu_statement_reports (scgl_account_menu/views/menus.xml:60-71,122-125).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: accounting correctness of statement layouts under Thai reporting standards; tests check computation, balance and cash tie-out only (tests/test_statements.py:41-66).
- UNKNOWN - EVIDENCE INSUFFICIENT: multi-company consolidation behavior of the instances.
- UNKNOWN - EVIDENCE INSUFFICIENT: how accounts of types not listed above (for example equity, income, expense, expense_other, off_balance) are treated in each statement; only the types found by pattern search are listed, the search was not exhaustive.
- UNKNOWN - EVIDENCE INSUFFICIENT: export (PDF/Excel) behavior claimed in the manifest summary; the export is provided by mis_builder, which was not studied.
