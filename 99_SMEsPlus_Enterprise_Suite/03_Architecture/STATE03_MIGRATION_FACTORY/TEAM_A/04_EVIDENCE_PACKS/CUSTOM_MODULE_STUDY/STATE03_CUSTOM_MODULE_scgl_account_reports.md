> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_reports

Module: scgl_account_reports
License (confirmed in manifest): AGPL-3 (scgl_account_reports/__manifest__.py:18)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:16)
Version (manifest): 19.0.2.1.0 (__manifest__.py:3)
Path: Extra_Module_scgl/scgl_account_reports
Source revision studied: workspace on-disk copy (not verified against upstream)
Note: the folder license note says the module was moved from LGPL-3 to AGPL-3 because it depends on an OCA XLSX report module (PROVENANCE.txt:4-6).

## 1. Business capability
- Thai purchase-tax / sales-tax (input/output VAT) listings for a date range: a wizard chooses type (sale or purchase), dates, optional zero-rated/exempt-only mode, rate (default 7) or tax groups, and companies (wizard/scgl_vat_report_wizard.py:5-33, views/scgl_vat_report_wizard_view.xml:7-27).
- Outputs: PDF (QWeb), Excel, or an on-screen move-line list (wizard/scgl_vat_report_wizard.py:48-76; report/scgl_vat_report_xlsx.py:4-54).
- Columns include a "tax period" per document, partner tax id and branch, tax names, base and tax amount, with totals (report/scgl_vat_report_xlsx.py:10-13; models/scgl_vat_report.py:38-47, 104-125).
- Manifest says v2.0 replaced an earlier handler built on an OEEL-1 report engine with direct queries on standard tables (__manifest__.py:11-14; models/scgl_vat_report.py:6-11). Self-declared.

## 2. Attachment to CORE
- core:account, account.move.line: adds stored computed text field `tax_names` (comma list of applied tax names) (models/account_move_line.py:7-13). No override of any core method. Overrides of core methods by name: none.
- core:account view account.view_move_form: adds hidden tax-names column in invoice lines (views/account_move_line_view.xml:8-10).
- core:account menu menu_finance_reports: new wizard menu, no groups on the menu item (views/scgl_vat_report_wizard_view.xml:38-42; core:account/views/account_menuitem.xml:37).
- Report queries use core tables/fields: move line tax_line_id, tax_ids relation, tax_base_amount, balance, ref, date; move amount_tax; tax type_tax_use, rate and tax group; partner vat and company_registry (models/scgl_vat_report.py:38-92). No control (posting, lock, valuation, approval) is changed. Not `ALTERS CORE CONTROL`.
- Data-access note: the queries are raw SQL over shared tables and filter only by state posted, the company ids in the wizard and date range (models/scgl_vat_report.py:20-25). Core record rules are not applied to raw SQL. The company list is user-editable with default = the user's active companies (wizard/scgl_vat_report_wizard.py:24-27, 44), so company scoping depends on who can read res.company records (core:base/security/base_security.xml:105-128 defines res.company rules). Flagged as a security-relevant behavior; runtime effect is UNKNOWN - EVIDENCE INSUFFICIENT.

## 3. New objects, security, automation, external calls
- New models: scgl.vat.report (abstract), scgl.vat.report.wizard (transient), report models for QWeb and Excel (models/scgl_vat_report.py:13; wizard:5; report/scgl_vat_report_xlsx.py:5,58).
- ACL: only the wizard, group account.group_account_readonly with full CRUD (security/ir.model.access.csv:2). No rules. Report actions declared in report/scgl_vat_report_templates.xml:58,67 (groups not set on the actions).
- Crons / server actions / external calls: none. A backup file `models/account_generic_tax_report.py_bkp` sits in the module folder but is not imported (models/__init__.py:1-2). It was not read.

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Mismatch: the SQL selects `am.tax_period` from account_move (models/scgl_vat_report.py:39,55,74,92). No `tax_period` field exists in core 19 account.move (no match in core:account/models/account_move.py). It is expected from the custom dependency scgl_tax_period_date (__manifest__.py:22), which was not studied. If that module does not create a stored column, the reports fail.
- Exist in core 19: tax_line_id (core:account/models/account_move_line.py:212), tax_base_amount (:222), ref stored related (:80), account.move.amount_tax stored (core:account/models/account_move.py:556), relation table account_move_line_account_tax_rel (core:account/models/account_move_line.py:198), res.partner vat (core:base/models/res_partner.py:237) and company_registry stored (:241), tax_group_id on tax (core:account/models/account_tax.py:156).
- Depends on OCA report_xlsx, absent from the Community tree (__manifest__.py:21); `not checked`.
- Zero-rated query requires the document's total tax = 0 (models/scgl_vat_report.py:91), a business rule choice, not a compatibility issue.

## 5. Custom-to-custom dependencies
- scgl_tax_period_date (__manifest__.py:22). Referenced by scgl_account_menu (menu id scgl_account_reports.menu_scgl_vat_report).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: source and semantics of tax_period (defined outside this module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the report matches the statutory filing format; no tests folder exists in this module.
- UNKNOWN - EVIDENCE INSUFFICIENT: handling of credit notes and cash-basis taxes (rows are grouped and signed only by tax type, models/scgl_vat_report.py:17,104-125).
- UNKNOWN - EVIDENCE INSUFFICIENT: content of the unread backup file and whether it is still needed.
