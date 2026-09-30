> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_dashboard_finance

Module: scgl_dashboard_finance
License (confirmed in manifest): LGPL-3 (scgl_dashboard_finance/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_dashboard_finance/__manifest__.py:8)
Version (manifest): 19.0.1.0.1 (scgl_dashboard_finance/__manifest__.py:5)
Path: Extra_Module_scgl/scgl_dashboard_finance
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds two published finance dashboards to the core "Finance" dashboard group: "Accounting" (cash, receivable/payable, revenue vs expenses, profit and loss, balance sheet snapshot) and "Benchmark" (margins, days sales/payables outstanding, current ratio, quarterly and year-over-year) (scgl_dashboard_finance/data/dashboards.xml:5-23; summary at scgl_dashboard_finance/__manifest__.py:3-4).
- Each dashboard is a stored spreadsheet document (two sheets: "Dashboard" and "Data") with 6 scorecards and at least 2 charts, per the module tests (scgl_dashboard_finance/tests/test_dashboards.py:18-27, 62-70). Figures are computed from accounting formulas of the Community spreadsheet_account module (ODOO.BALANCE ~152 uses, ODOO.RESIDUAL 4, ODOO.ACCOUNT.GROUP 17, ODOO.FISCALYEAR.START 2 in each file: scgl_dashboard_finance/data/files/accounting_dashboard.json, scgl_dashboard_finance/data/files/benchmark_dashboard.json).
- The XML header says the layout follows screenshots, not Enterprise code (scgl_dashboard_finance/data/dashboards.xml:3-4).

## 2. Attachment to CORE
- Creates data records of core model spreadsheet.dashboard (fields exist: core:spreadsheet_dashboard/models/spreadsheet_dashboard.py:14, 17, 19, 31). No Python code in the module (scgl_dashboard_finance/__init__.py is empty). No core method overridden. ADDS data only.
- Group placement: core group `spreadsheet_dashboard_group_finance` (core:spreadsheet_dashboard/data/dashboard.xml:4).
- Visibility: restricted to core group "Accounting read-only" (account.group_account_readonly) (scgl_dashboard_finance/data/dashboards.xml:10, 20). Main data model linked: journal items (line 8, 18).
- Sequence 10 and 25 place them around the core Invoicing dashboard (sequence 20 per comment, scgl_dashboard_finance/data/dashboards.xml:4; verified by test scgl_dashboard_finance/tests/test_dashboards.py:64, 70).
- Reads (through formulas) journal item balances via core RPC on account.account: `spreadsheet_fetch_debit_credit`, `spreadsheet_fetch_residual_amount` (core:spreadsheet_account/models/account.py:109, 135); posting, lock dates, valuation, numbering, approvals are not touched. No ALTERS CORE CONTROL identified.

## 3. New objects, security, automation, external calls
- No new models, ACLs, record rules, crons, server actions, or external calls.
- Security: dashboard visibility by group only (above). Data access when a viewer opens the spreadsheet is governed by the core spreadsheet_account methods (not reviewed for record-rule handling here).
- Company scoping: formulas pass the current company through the core fetch call, as shown by the test arguments (scgl_dashboard_finance/tests/test_dashboards.py:72-78). Multi-company consolidation behavior: UNKNOWN.

## 4. Odoo 19 compatibility
- Dependencies in manifest all exist in Community 19: spreadsheet_dashboard, spreadsheet_account, account (core folders present).
- Dashboard fields used exist (see section 2). Group xml ids exist (core:spreadsheet_dashboard/data/dashboard.xml:4).
- The test compares sequence against `spreadsheet_dashboard_account.dashboard_invoicing` (scgl_dashboard_finance/tests/test_dashboards.py:64), a module not listed in this manifest depends; the module exists in Community 19 (core:spreadsheet_dashboard_account), so tests need it installed.
- Spreadsheet format compatibility: the tests mention a chart-id requirement for newer spreadsheet format versions (scgl_dashboard_finance/tests/test_dashboards.py:22-24). Not run.
- Formula set limited to known Community functions (scgl_dashboard_finance/tests/test_dashboards.py:8-9, 55-58). No mismatch found by static reading.

## 5. Custom-to-custom dependencies
- None declared (scgl_dashboard_finance/__manifest__.py:10).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: the correctness of financial ratios (DSO/DPO, current ratio, margins) in the spreadsheet formulas; the JSON was not audited cell by cell.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the account groupings/codes used by formulas match the deployed chart of accounts (Thai chart handled by other modules).
- UNKNOWN - EVIDENCE INSUFFICIENT: runtime rendering (not run).
