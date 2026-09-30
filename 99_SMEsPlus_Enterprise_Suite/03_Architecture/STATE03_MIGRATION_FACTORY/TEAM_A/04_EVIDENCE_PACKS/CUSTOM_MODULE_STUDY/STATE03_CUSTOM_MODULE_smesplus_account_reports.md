> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_account_reports

Module: smesplus_account_reports ("SMEsPlus Account Reports")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 19.0.1.4
Path: addons_Extramodule/addons_extra/smesplus_account_reports
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_06): Company Extra/Custom
Note: manifest depends on account, account_reports (Enterprise, NOT in the Community tree) and smesplus_tax_period_date (__manifest__.py:1-26); batch file listed only account.

## 1. Business capability
- Adds four Thai VAT listing reports (tax invoice registers) under the standard Tax Report family, available for Thailand (data/generic_tax_report.xml:3-13, 73-83, 136-146, 209-):
  - Sale VAT report and Purchase VAT report: one row per tax line at 7% VAT, with running number, document date, tax period date, document number, reference, partner name, tax ID, branch, tax name, base amount, tax amount, and a total row (models/account_generic_tax_report.py:7-186, 189-203; column list data/generic_tax_report.xml:15-70).
  - Sale VAT (zero) and Purchase VAT (zero): one row per document whose total tax is zero, i.e. zero-rated/exempt sales and purchases (models/account_generic_tax_report.py:206-380 for sale, 382-end for purchase; the zero-tax condition is at :283 and :454).
- Purpose: supports the monthly Thai VAT filing lists (input/output tax) with the declared tax period displayed (data/generic_tax_report.xml:25-28).
- Adds a stored text field with the names of the taxes on each journal item, used in the reports and shown (hidden) on invoice lines (models/account_move_line.py:7-13; views/account_move_line_view.xml:8-10).

## 2. Attachment to CORE
- Core module: account. Community 19 has the report definition model and the root generic tax report (core:account/models/account_report.py:45; core:account/data/account_reports_data.xml:6) and helper for tax-detail data (core:account/models/account_move_line_tax_details.py:28).
- Enterprise dependency assumed (absent from Community tree, searched): the custom-handler mechanism (report field custom_handler_model_id, parent model account.report.custom.handler, option splitting per column group, the report query builder, header-template fields). The four handler classes inherit that Enterprise base (models/account_generic_tax_report.py:8-12, 190-192, 207-209, 383-385) and the data file wires them (data/generic_tax_report.xml:10, 80, 143). The templates call Enterprise cell templates (views/report_templates.xml:34, 46, 50, 123).
- account.move.line (core:account/models/account_move_line.py): adds tax_names (models/account_move_line.py:7-13). account.move: reads tax_period supplied by smesplus_tax_period_date (models/account_generic_tax_report.py:38, 415).
- Core method overrides: none on core objects. New report handler classes only.
- ALTERS CORE CONTROL: no. Read-only reporting. Unlike ORM reads, the handlers run direct database queries built from the report's own company/date query, so per-record access rules are not evaluated (inference from the raw-cursor pattern at models/account_generic_tax_report.py:77, 288, 459; isolation depends on the report option filters).

## 3. New objects, security, automation, external calls
- New models: abstract report handlers account.sale.vat.report.handler, account.purchase.vat.report.handler, account.sale.vat.report.zero, account.purchase.vat.report.zero. New report records and columns (data/generic_tax_report.xml).
- Security: none shipped (no ACL, groups or rules); report visibility is governed by Enterprise reports access.
- Company scoping: multi-company filter set to "tax units" (data/generic_tax_report.xml:5); availability limited to country Thailand (:12-13).
- Cron, server actions, external calls: none.
- Layout templates (views/report_templates.xml:3, 56, 136, 177) exist but the report records reference them only in commented-out lines (data/generic_tax_report.xml:84-86, 147-149, 220-222), so they appear inactive.

## 4. Odoo 19 compatibility
- Checked: account.report (core:account/models/account_report.py:45), only_tax_exigible (:67), availability_condition (:73), filter_multi_company with tax_units choice (:120-122), default opening filter present; _get_query_tax_details signature (core:account/models/account_move_line_tax_details.py:28).
- Not present in Community tree (grep negative): custom_handler_model_id, account.report.custom.handler, _split_options_per_column_group, _get_report_query, main_table_header_template - resolved only if Enterprise account_reports is installed.
- Fragile logic: the 7% reports include a row only when the tax-group name equals the English string "VAT 7%" (models/account_generic_tax_report.py:88); a group named differently or translated is excluded. Amounts are output as formatted text with a baht sign (:118-139), not as numbers. Unused import at :1. Direct cursor use (:77, 288, 459) instead of the ORM query helper. Sale/purchase sign handling differs between report pairs (:87, 298).
- view xpath for tax_names uses page/invoice_line_ids/list/tax_ids (views/account_move_line_view.xml:8); core has invoice_line_ids at core:account/views/account_move_views.xml:1157 - exact path not confirmed.

## 5. Custom-to-custom dependencies
- smesplus_tax_period_date (declared, __manifest__.py:16). Not the SCGL copy scgl_tax_period_date.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of the four reports without Enterprise account_reports (module cannot be exercised here).
- UNKNOWN - EVIDENCE INSUFFICIENT: how withholding tax (WHT) lines and non-7% VAT are meant to appear in these lists.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the totals reconcile to the official VAT return form (no comparison artifact in module).
