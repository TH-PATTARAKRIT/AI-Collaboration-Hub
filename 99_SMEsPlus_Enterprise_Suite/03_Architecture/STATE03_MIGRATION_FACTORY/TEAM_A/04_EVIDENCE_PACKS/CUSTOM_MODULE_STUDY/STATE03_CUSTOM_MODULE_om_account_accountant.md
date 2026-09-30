> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: om_account_accountant (Clean-Room study, read-only, LGPL gate PASSED)
## 0. Header
- Module: om_account_accountant (manifest name "Odoo 19 Accounting Community") - om_account_accountant/__manifest__.py:2
- License confirmed in manifest: LGPL-3 - om_account_accountant/__manifest__.py:17 (code read permitted)
- Author: Odoo Mates, Odoo SA (maintainer Odoo Mates) - om_account_accountant/__manifest__.py:15-16 | Version: 1.0.5 - :3 | application=True - :40
- Path: addons_Extramodule/addons_extra/om_account_accountant (per batch_09.json entry; Third-party, source-readable)
- Source revision studied: workspace on-disk copy (files dated 2026-09-18/21); no VCS revision available
## 1. Business capability
- Umbrella "Accounting (Community)" app that substitutes for Enterprise "Accountant": bundles reports, assets, budgets, fiscal year, recurring payments, daily reports, customer follow-up (summary/description om_account_accountant/__manifest__.py:5-11; README.rst:5-7).
- Itself adds: Journals submenu, Bank and Cash menus, Account Groups/Tags/Payment Methods menus, Anglo-Saxon toggle, role renaming, "in_payment" invoice state, Reconcile action.
## 2. Attachment to CORE
- Depends only on other custom modules (om_account_accountant/__manifest__.py:19-27); no direct core depends listed (batch_09.json core_modules_depended=[]); core `account` is only reached transitively (UNVERIFIED, see 6). Meta-module: 7 bundled modules + a thin glue layer.
- ALTERS CORE CONTROL: overrides account.move._get_invoice_in_payment_state to return 'in_payment' (om_account_accountant/models/account_move.py:7-9); core hook returns 'paid' and is documented as the override point for the accountant module (core account/models/account_move.py:7367-7372). Changes payment-state lifecycle of invoices, payments (account_payment.py:259,914), hr_expense (hr_expense.py:483), POS (pos_session.py:1157).
- ALTERS CORE CONTROL (security): redefines core groups: group_account_user renamed "Accountant" + implies group_account_invoice + adds admin/root users; group_account_manager renamed "Advisor", implies account_user and REMOVES implied group_account_invoice; group_account_readonly renamed "Auditor" (om_account_accountant/security/group.xml:8-21). Core defs: account/security/account_security.xml:50-80.
- Also renames base category base.module_category_accounting_accounting to "Accounting" (security/group.xml:4-6).
- Menu overrides of core: renames account.menu_finance (views/menu.xml:4); clears groups on account.menu_action_account_moves_all and sets sequence 2 (menu.xml:12-18) = ALTERS CORE CONTROL (removes group restriction on Journal Items menu, core sets groups=group_account_readonly at account/views/account_menuitem.xml:33).
- View inherits: account.res_config_settings_view_form (views/settings.xml:4-9), account.view_partner_property_form (views/res_partner.xml:4-9), account.view_account_journal_form (views/account_journal.xml:4-15) - cosmetic (labels, optional column).
## 3. New objects / security / automation
- No new models/tables, no ir.model.access, no record rules, no crons, no wizards (files: models/account_move.py, models/settings.py only).
- Extended fields: res.config.settings.anglo_saxon_accounting related to company_id.anglo_saxon_accounting, readonly=False (om_account_accountant/models/settings.py:7-11); core field at account/models/company.py:144.
- Menus/actions: Account Groups (views/account_group.xml:4-14), Account Tags (views/account_tag.xml:4-13), Payment Methods with read-only views (views/payment_method.xml:4-60, menu groups=base.group_no_one :60), Bank/Cash statements (views/account_bank_statement.xml:4-17), Journals submenu with 4 actions, groups=account.group_account_readonly (views/menu.xml:20-39), Templates menu (menu.xml:6-10).
- Server action "Reconcile" bound to account.move.line: code `records.reconcile()`, group account.group_account_user (views/reconciliation.xml:4-11); core method account/models/account_move_line.py:3142.
## 4. Odoo 19 compatibility (Community tree grep)
- Core targets exist: hook (account_move.py:7367), company.anglo_saxon_accounting (company.py:144), account.group (account_account.py:1515), account.account.tag (account_account_tag.py:8), account.payment.method (account_payment_method.py:8-13), actions bank_statement_tree/view_bank_statement_tree (account_bank_statement_views.xml:50,123), journal actions (account_move_views.xml:1872-1899), menus finance_entries/configuration/account_account_menu/root_payment_menu (account_menuitem.xml:24,46,48,64), app name="account" (res_config_settings_views.xml:23), page "accounting" (partner_view.xml:210), journal payment_account_id (account_journal_views.xml:129,146).
- Uses Odoo-19 syntax: <list>, group_ids on ir.ui.menu/ir.actions.server (core base/models/ir_ui_menu.py:29).
- Risks: core 19 moves groups to res.groups.privilege (account_security.xml:40-43,58) while module.xml still relies on module_category rename (cosmetic, may not affect group UI); manifest duplicates 'sequence' key (__manifest__.py:13-14); README titled "Odoo 18" (README.rst:2). Runtime install not tested.
## 5. Custom-to-custom dependencies
- accounting_pdf_reports (batch_00), om_account_asset, om_account_budget, om_fiscal_year, om_recurring_payments, om_account_daily_reports, om_account_followup (batch_02) - all LGPL-3 per batch metadata; declared at __manifest__.py:20-26.
## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Whether core `account` is guaranteed installed: depends on transitive manifests of the 7 bundled modules (not read here).
- Whether views/settings.xml xpath and account.menu_finance rename behave without conflict at install: not run.
- Effect of the group.xml (4,x) implied changes vs core Odoo-19 privilege model on effective user permissions: not tested at runtime.
- Content of doc/, i18n/, static/ not inspected (non-functional).
