> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_financial_report

Module: account_financial_report
License (confirmed in manifest): AGPL-3 (account_financial_report/__manifest__.py:56)
Author (manifest): Camptocamp, initOS GmbH, redCOR AG, ForgeFlow, Odoo Community Association (OCA) (manifest:12-17)
Version (manifest): 19.0.0.0.23 (manifest:9)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_financial_report
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Financial reporting suite launched from wizards, each exportable to screen (HTML), PDF and Excel: General Ledger, Trial Balance, Journal Ledger, Open Items, Aged Partner Balance, VAT Report. (account_financial_report/reports.xml:22-139; wizard/*.py; menuitems.xml:3-45)
- Configurable aging buckets for the Aged Partner Balance (a named set of interval lines), chosen in accounting settings. (models/account_age_report_configuration.py:8-46; models/res_config_settings.py:10-36)
- Account-group hierarchy helpers (full name/code, level, accounts per group incl. children) used by the trial balance grouping. (models/account_group.py:8-108)
- Report drill-through links from report lines to journal entries/accounts in the viewer (static/src/js/report.esm.js, report_action.esm.js).

## 2. Attachment to CORE
- Depends on core `account`, and on non-core `date_range` and `report_xlsx` (manifest:18).
- `account.account` (core:account/models/account_account.py): adds boolean "centralized" flag and shows it on the account form (models/account.py:9-13; view/account_view.xml:5-9). The flag's help text mentions a webkit report only, but the General Ledger code reads it and groups amounts per journal and month for such accounts (report/abstract_report.py:143; report/general_ledger.py:696,738-770).
- `account.group` (core:account/models/account_account.py:1514-1522): adds child list, level, complete name/code, and computed account lists. The account list of a group is computed by a direct database query on account codes (models/account_group.py:44-80); in Odoo 18/19 the core account has no stored group link (comment models/account_group.py:47-48; core:account/models/account_account.py:113 computed `group_id`). Read-only helper, no write to core data.
- `account.move.line`: adds stored many-to-many "analytic accounts" derived from the analytic distribution (models/account_move_line.py:12-37). Override `search_count` (models/account_move_line.py:64-70; core:odoo/orm/models.py:1360): REPLACES core behavior when a context flag is set — returns 0 without counting (performance shortcut); otherwise unchanged. On module load it creates a database index on (account, partner) of journal items if missing (models/account_move_line.py:39-62).
- `ir.actions.report`: overrides `_render_qweb_html` and `_render_xlsx` to force the report language from wizard data (models/ir_actions_report.py:15-27; core:base/models/ir_actions_report.py:1113); `_render_xlsx` belongs to the non-core `report_xlsx`. ADDS behavior around core rendering (language context).
- `res.config.settings`: stores the chosen aging configuration as a company default via elevated rights (models/res_config_settings.py:15-22).
- Views inherit core `account.view_account_form` and `account.res_config_settings_view_form` (view/account_view.xml:5; view/res_config_settings_views.xml:7). Menu parent: core `account.menu_finance_reports` (menuitems.xml:3-8; core:account/views/account_menuitem.xml:37).
- JS: patches the core web `ReportAction` component for HTML report viewers (static/src/js/report_action.esm.js:1-41; core:web/static/src/webclient/actions/reports/report_action.js).
- Reports read journal items mostly through the ORM (search_read / grouped reads), so access rights and record rules apply (e.g. report/general_ledger.py:121,507; report/trial_balance.py:210,525). One exception: tax detail lookup for the Journal Ledger uses a direct database query on selected line ids (report/journal_ledger.py:210-217).
- No override of posting, lock date, valuation, approvals, numbering or record rules. No `ALTERS CORE CONTROL` found; the two security-relevant items are ACLs (section 3) and the `search_count` shortcut.

## 3. New objects, security, automation
- New objects: transient wizards (general ledger, trial balance, journal ledger, open items, aged partner balance, VAT) plus abstract wizard/report bases; persistent models `account.age.report.configuration` and `.line` (models/account_age_report_configuration.py:9,28).
- ACLs: every internal user (base.group_user) has full CRUD on all wizard models and on the aging configuration models (security/ir.model.access.csv:2-9). Menus require accounting read-only group (menuitems.xml:7), but the aging configuration model itself is writable by any internal user.
- Record rule: aging configuration limited to allowed companies plus no-company records (security/security.xml:3-7).
- Wizard "Export" buttons store the label-length preference as a global company default with elevated rights (wizard/abstract_wizard.py:66-74).
- No crons, server actions or external calls.

## 4. Odoo 19 compatibility
- Present in core 19: `execute_query` (core:odoo/orm/environments.py:527), `SQL` helper, `Command`, `search_count(domain, limit)`, `account.move.line._get_tax_exigible_domain` (core:account/models/account_move_line.py:3456), `code_store` company-dependent field used in the group query (core:account/models/account_account.py:40), `formatted_read_group` (used by core addons via super, e.g. core:hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:75).
- MISMATCH: unique-name rule declared as a plain list attribute `_unique_name_config_combination` (models/account_age_report_configuration.py:43-46) — core 19 uses `models.Constraint` objects (as in core:odoo/orm/table_objects.py:79); as written it appears not enforced. Inferred from code style; not run.
- Not checked: `report_xlsx` / `date_range` API versions; QWeb template internals (report/templates/*.xml, ~3,700 lines); XLSX writer classes.

## 5. Custom-to-custom dependencies
- Declared: `date_range` (a STATE03 trace exists for it in the same folder), `report_xlsx` (not in this batch).
- Functional overlap with `accounting_pdf_reports` (same batch): both add ledger/trial-balance style reports; no code dependency.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: numerical correctness of report figures vs core data (runtime not observed).
- UNKNOWN — EVIDENCE INSUFFICIENT: display behaviour of centralized accounts in the General Ledger templates (templates not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the age-report-configuration duplicate-name rule is enforced at database level.
- UNKNOWN — EVIDENCE INSUFFICIENT: on-disk copy vs upstream OCA release.
