> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_account_daily_reports

Module: om_account_daily_reports · License (confirmed in manifest): LGPL-3 (om_account_daily_reports/__manifest__.py:9)
Author (manifest): Odoo Mates (manifest:8) · Version (manifest): 1.0.2 (manifest:3)
Path: addons_Extramodule/addons_extra/om_account_daily_reports
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Three printable (PDF) reports: Day Book, Cash Book, Bank Book (report/reports.xml:4-27; manifest:2, 5).
- Each has a selection wizard: date range, posted-only versus all entries, journals, and (cash/bank) accounts, display filter (all / with movement / non-zero balance), sort (date or journal and partner), optional opening balance row (wizard/account_bankbook_report.py:23-44; wizard/account_cashbook_report.py:23-44; wizard/account_daybook_report.py:9-17).
- Cash and bank wizards pre-select accounts of the company's cash or bank journals: journal default account plus payment accounts of inbound/outbound payment method lines (wizard/account_bankbook_report.py:9-21).
- Read-only reporting: nothing is written to accounting data.

## 2. Attachment to CORE
- Depends on core `account` and on `accounting_pdf_reports` (manifest:14), the latter not part of Community and not read here.
- Reads core `account.move.line`, `account.move`, `account.journal`, `account.account` (report/report_daybook.py:11-60; report/report_bankbook.py:10-135). Reads database tables directly through the cursor for the three reports (report/report_daybook.py:60, report/report_bankbook.py:68/108, report/report_cashbook.py:55/86); this path does not apply ORM record rules.
- Core menu attached: new "Daily Reports" folder under `account.menu_finance_reports` (views/om_daily_reports.xml:5-8); three menu entries limited to `account.group_account_user` and `account.group_account_manager` (wizard/daybook.xml:44; wizard/cashbook.xml:53; wizard/bankbook.xml:53).
- No inheritance of core models, no override of any core method. Therefore no posting, lock-date, valuation, approval, numbering or security override. No `ALTERS CORE CONTROL` item.
- Report-model methods `_get_report_values` on its own three abstract report models (report/report_bankbook.py:139; report/report_cashbook.py:116; report/report_daybook.py:75) are module-owned, not overrides of core.
- "All entries" is defined as everything except cancelled (draft plus posted) for the day book (report/report_daybook.py:16-20).

## 3. New objects, security, automation, external calls
- Transient models: account.daybook.report, account.cashbook.report, account.bankbook.report (wizard/__init__.py:3-5). Abstract report models `report.om_account_daily_reports.report_daybook`, `..._cashbook`, `..._bankbook`.
- ACLs (security/ir.model.access.csv:2-7): Manager and Accountant groups full rights on the three wizards. No record rules, no new groups.
- Company scoping: wizard defaults limit journals to the current company (wizard/account_daybook_report.py:15; cash/bank :29). The day book query also restricts to allowed companies (report/report_daybook.py:41). For cash/bank books, company scoping depends on the move-line filter helper described in section 4, and on the selected journals/accounts: UNKNOWN - EVIDENCE INSUFFICIENT.
- Fallback when no account is selected: searches all bank journals without company filter (report/report_bankbook.py:155-157); for the day book, all accounts are read (report/report_daybook.py:89, account search without extra filter).
- No crons, no server actions, no external calls.

## 4. Odoo 19 compatibility (grep against Community 19)
- MISMATCH (probable): `account.move.line._query_get()` is called by the cash book and bank book (report/report_cashbook.py:34, 64; report/report_bankbook.py:35-39, 77). Grep of the whole Community 19 tree found no definition of `_query_get`. It is possibly supplied by the `accounting_pdf_reports` dependency (not read): UNKNOWN - EVIDENCE INSUFFICIENT.
- The day book does not use `_query_get` (report/report_daybook.py).
- Found in core: `default_account_id`, `inbound_payment_method_line_ids`, `outbound_payment_method_line_ids` on account.journal (core:account/models/account_journal.py:126, 205, 220), `payment_account_id` (core:account/models/account_payment_method.py:110), menu `account.menu_finance_reports` (core:account/views/account_menuitem.xml:37).
- Community 19 has no `accounting_pdf_reports` module (module listing checked): dependency must come from elsewhere in the workspace.
- Raw SQL text table/column names (e.g., move-line column names) were not verified against the 19 schema: not checked.
- Manifest `sequence` is given as a string (manifest:7) - possible type mismatch; effect not checked.

## 5. Custom-to-custom dependencies
- `accounting_pdf_reports` (manifest:14): third-party module outside Community; not read in this assignment.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Origin and behavior of `_query_get` at runtime: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether direct-database reads leak data across companies or restricted users for cash/bank books: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether the cash/bank book opening-balance logic matches core accounting semantic for income/expense accounts: UNKNOWN - EVIDENCE INSUFFICIENT.
