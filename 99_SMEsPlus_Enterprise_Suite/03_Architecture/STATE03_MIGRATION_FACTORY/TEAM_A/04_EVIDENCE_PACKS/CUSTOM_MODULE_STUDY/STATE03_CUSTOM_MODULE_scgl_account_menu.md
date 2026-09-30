> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_menu

Module: scgl_account_menu
License (confirmed in manifest): AGPL-3 (scgl_account_menu/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:8)
Version (manifest): 19.0.1.3.0 (__manifest__.py:5)
Path: Extra_Module_scgl/scgl_account_menu
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Data-only module (no Python or JS, __manifest__.py:4; only views/menus.xml is loaded, line 14-16) that reorganises the accounting menu tree into groups: Accounting, Review, Reporting (Statement / Ledgers / Partner / Taxes / Management) and Configuration (views/menus.xml:6-150).
- Renames the top-level app from "Invoicing" to "Accounting" (views/menus.xml:7-9).
- Exposes hidden or unlinked tools as menus: Secure Journal Entries wizard (views/menus.xml:34-35), Lock Journal Entries (relocated, lines 26-30), Aged Receivable / Aged Payable wizard actions (lines 89-106), Aged Partner Intervals (lines 135-137), Tax Returns entry pointing to an OCA VAT wizard (lines 24-25).
- Overrides the core Analytic Reporting action to force explicit list and form views (views/menus.xml:155-161).
- Provenance note: menus rewritten from core XML ids and OCA menus; declares no OEEL-1 source read (PROVENANCE.txt:5-9).

## 2. Attachment to CORE
- core:account menus reused as parents: menu_finance (core:account/views/account_menuitem.xml:5), menu_finance_entries (:24), account_closing_menu (:29), account_audit_menu (:31), account_audit_control_menu (:32), menu_finance_reports (:37), account_reports_partners_reports_menu (:38), account_reports_taxes_and_fiscal_menu (:39), account_reports_management_menu (:40), account_reports_legal_statements_menu (:44), account_account_menu (:48), account_invoicing_menu (:59). All exist.
- Changes to core objects (record overrides, ALTERS presentation only):
  - ir.ui.menu account.menu_finance renamed (views/menus.xml:7-9).
  - ir.actions.act_window account.action_analytic_reporting: view mode, view id and view list replaced (views/menus.xml:155-161; core:account/views/account_analytic_line_views.xml:94). REPLACES core action view binding.
  - Menu for core wizard action account.action_view_account_secure_entries_wizard now visible to group account.group_account_manager (views/menus.xml:34-35; core:account/wizard/account_secure_entries_wizard.xml:34). ADDS visibility; does not change the wizard.
- Lock-date relevance: the module only re-parents the OCA "Lock Journal Entries" menu under Closing (views/menus.xml:26-30). It does not change lock logic. Not `ALTERS CORE CONTROL`. Menu access is governed by the groups of each target menu; some new menus have no `groups` (menu_tax_returns, menu_fiscal_years_closing, menu_aged_receivable, menu_aged_payable, views/menus.xml:24,31,103,105) and inherit the parent's groups.
- Overrides of core methods by name: none.

## 3. New objects, security, automation, external calls
- New records: 2 window actions on wizard model aged.partner.balance.report.wizard (views/menus.xml:89-102) and new menu items. New models, ACLs, rules, crons, server actions, external calls: none found.
- Menus set inactive: scgl_account_statements.menu_statement_reports, account_financial_report.menu_oca_reports, account_credit_control.base_credit_control_configuration_menu (views/menus.xml:69-71,127-129,148-150).

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- All core menu ids and actions listed in section 2 exist. Analytic views analytic.view_account_analytic_line_tree and _form exist (core:analytic/views/analytic_line_views.xml:3,71).
- Depends on non-Community modules: account_financial_report, account_asset_management, account_fiscal_year, account_lock_date_update, account_credit_control (__manifest__.py:11-12). These are not in the Community tree; whether their menu ids referenced here exist in the installed versions is `not checked` (outside the assigned folders).
- Tests reference the layout (tests/test_menu.py:8,18,24,32).

## 5. Custom-to-custom dependencies
- scgl_account_statements, scgl_account_reports (__manifest__.py:11-12); references menu ids menu_balance_sheet, menu_profit_loss, menu_cash_flow, menu_statement_reports, menu_executive_summary (views/menus.xml:60-71,122-125) and scgl_account_reports.menu_scgl_vat_report (:117). Those ids exist in the two modules' files (scgl_account_statements/views/menus.xml:37-42; scgl_account_reports/views/scgl_vat_report_wizard_view.xml:38).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: existence and group settings of the OCA menu ids and actions (account_financial_report.*, account_asset_management.*, account_credit_control.*, account_fiscal_year.*, account_lock_date_update.*) in the installed versions.
- UNKNOWN - EVIDENCE INSUFFICIENT: effect of the menu changes on users who lack the groups of the re-parented menus.
- UNKNOWN - EVIDENCE INSUFFICIENT: load-order safety of overriding menus that belong to other modules (depends list covers them, but not verified at runtime).
