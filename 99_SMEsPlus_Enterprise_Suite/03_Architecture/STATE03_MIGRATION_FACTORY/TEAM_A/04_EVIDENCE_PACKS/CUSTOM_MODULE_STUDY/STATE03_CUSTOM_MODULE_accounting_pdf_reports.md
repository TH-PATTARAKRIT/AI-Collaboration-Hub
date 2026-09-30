> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — accounting_pdf_reports

Module: accounting_pdf_reports
License (confirmed in manifest): LGPL-3 (accounting_pdf_reports/__manifest__.py:10)
Author (manifest): Odoo Mates, Odoo SA (manifest:9)
Version (manifest): 1.0.6 (manifest:3) — title "Odoo 19 Accounting Financial Reports" (manifest:2)
Path: addons_Extramodule/addons_extra/accounting_pdf_reports
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Printable (PDF) accounting reports launched from wizards: General Ledger, Partner Ledger, Trial Balance, Balance Sheet, Profit and Loss (both via configurable financial-report definitions), Tax Report, Aged Partner Balance (receivable/payable/both), Journals Audit, plus a printable "Journals Entries" for selected journal entries. (accounting_pdf_reports/report/report.xml:4-69; wizard/*.xml menus, e.g. wizard/general_ledger.xml:41, wizard/balance_sheet.xml:111)
- Common filters: company, journals, date range, "all posted" vs "all entries", analytic accounts, accounts, partners, comparison period on financial reports. (wizard/account_report_common.py:9-21; account_report.py:17-30; account_report_common_account.py:9-16)
- Configurable financial report structure (tree with sign, detail level, style; lines by accounts, by account type, or by another report). (models/account_financial_report.py:4-73; data seeded in wizard/balance_sheet.xml:4-70)
- Adds "Ledgers" list-view menus (General Ledger, Partner Ledger as grouped journal-item lists). (views/ledger_menu.xml:4-33)

## 2. Attachment to CORE
- Depends on core `account` only (manifest:15).
- `account.move.line` (core:account/models/account_move_line.py): module ADDS a method `_query_get` that turns wizard context (dates, journals, state, company, accounts, partners, analytic) into a search filter (accounting_pdf_reports/models/account_move_line.py:8-75). Core 19 has no method of this name (grep of core:addons found none), so this is a new method, not an override. It uses the ORM search path, hence normal access and record rules apply to that path. Also adds `format_analytic_distribution` (models/account_move_line.py:77-98).
- New model `account.account.type` seeded with 18 type records (data/account_account_type.xml; models/account_account_type.py:4-33) mirroring the core selection `account_type` on `account.account` (core:account/models/account_account.py:44-47); financial-report lines of type "account type" match accounts through that selection value (report/report_financial.py:59-62).
- Core menus reused/changed: adds submenus under `account.menu_finance_reports` and changes the sequence of core menu `account.account_reports_management_menu` (accounting_pdf_reports/views/menu.xml:4-21; core:account/views/account_menuitem.xml:37,40). Adds "Ledgers" menu under `account.menu_finance_entries` (views/ledger_menu.xml:27). Inherits core settings view to add an "Enhanced Financial Reports" block with two outward links to a third-party app store (views/settings.xml:9-33) — links only, no calls.
- Report action bound to core `account.move` "Print" menu: "Journals Entries" (report/report.xml:61-69).
- No override of any core Python method. Nothing touches posting, lock dates, valuation/cost, approvals, numbering or record rules: no `ALTERS CORE CONTROL` found. Read-side access note in section 3.

## 3. New objects, security, automation
- New transient wizards (account.common.report family, account.report.general.ledger, account.balance.report, account.report.partner.ledger, accounting.report, account.aged.trial.balance, account.tax.report.wizard, account.print.journal) and persistent models `account.financial.report`, `account.account.type` (see grep of `_name` in wizard/ and models/).
- ACLs (security/ir.model.access.csv:2-25): accountants (group account_user) and managers full rights on report wizards; partner ledger for group account_invoice; read-only for all internal users on the common wizard bases and on `account.account.type` (csv:22-25). Menu access restricted to account_user/manager (e.g. wizard/general_ledger.xml:46, partner_ledger.xml:41). No new groups, no record rules, no company scoping rule on financial-report definitions.
- Data access: general ledger, trial balance, financial and tax reports build SQL from `_query_get` (ORM-derived filter). The Aged Partner and Journals Audit reports issue direct database queries filtered only by company/state/dates (report/report_aged_partner.py:47-102; report/report_journal.py:17-26): these initial selections do not go through ORM record rules — impact for users with restricted rules UNKNOWN.
- Install-time data removal: `pre_init_hook` drops a leftover relation table of the partner-ledger wizard if it exists (accounting_pdf_reports/__init__.py:6-7; manifest pre_init_hook). Business effect: only wizard scratch data.
- No crons, no server actions, no outbound calls from code.

## 4. Odoo 19 compatibility
- `account.account.type` reintroduced as custom model because core 19 uses a selection (core:account/models/account_account.py:44); some data mappings depend on the `type` values matching the core selection keys (seen matching in data/account_account_type.xml and model:10-29).
- `self.check_access('read')` (models/account_move_line.py:10) exists (core:odoo/orm/models.py:4106); `Query.from_clause` / `where_clause` used with `.code`/`.params` (py:70-74) exist (core:odoo/tools/query.py:158,173); whether `.code`/`.params` attributes exist on the returned SQL object: not checked.
- Core view refs `account.view_move_line_tree_grouped_general`, `..._partner`, `account.view_account_move_line_filter`, menus `account.menu_finance_reports`, `account.account_reports_management_menu`, `account.menu_finance_entries` exist (core:account/views/account_move_views.xml:246,258,306; account_menuitem.xml:24,37,40). `account.action_report_journal` is referenced (wizard/account_report_print_journal.py:21); core lists it as a protected report xmlid (core:account/models/ir_actions_report.py:82) but its definition file was not located: not checked.
- DUPLICATE: `account.print.journal` is defined twice with different behaviour (wizard/account_report_print_journal.py:6 and wizard/account_journal_audit.py:6); load order (wizard/__init__.py) makes the audit version take effect last for the print action — inferred, not run.
- `res.config.settings` inherit targets `app name="account"` (views/settings.xml:9) in core `account.res_config_settings_view_form`: exact anchor not verified.
- Other model/field references (`include_initial_balance`, `parent_state`, `max_date`, `matched_debit_ids`, `account_type`) exist in core (core:account/models/account_account.py:71; account_move_line.py:69,266; account_partial_reconcile.py:64). No further mismatches found.

## 5. Custom-to-custom dependencies
- None declared. It duplicates functions of other reporting modules in the same workspace (e.g. `account_financial_report`, folder-listing only; overlap not evaluated).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether output figures reconcile with core/other reporting modules (runtime not observed).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of Aged Partner/Journals Audit under restrictive record rules.
- UNKNOWN — EVIDENCE INSUFFICIENT: which of the two `account.print.journal` definitions is effective at runtime.
- UNKNOWN — EVIDENCE INSUFFICIENT: QWeb templates (report/*.xml) were not read line by line.
- UNKNOWN — EVIDENCE INSUFFICIENT: on-disk copy vs upstream release.
