> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: mis_builder

Module: mis_builder · License (confirmed in manifest): AGPL-3 (mis_builder/__manifest__.py:46)
Author (manifest): ACSONE SA/NV, Odoo Community Association (OCA) (manifest:11) · Version (manifest): 19.0.1.2.1 (manifest:6)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/mis_builder
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A management-reporting toolkit: report templates made of KPIs (formula-driven rows), optional sub-columns, styles and user-defined data queries (mis_builder/models/mis_report.py:73-401).
- Report instances place a template over one or several periods (fixed dates, relative dates, date ranges, comparisons, sums of periods), with posted-only or all-entries choice, single or multi company and a chosen currency (models/mis_report_instance.py:40-70, 477-560).
- Formulas can sum account-level debit/credit/balance by account selection, with variation, opening and ending-balance modes (models/aep.py:81-146, 317-390). Output: on-screen widget, PDF, XLSX, drill-down to underlying move lines, annotations on cells, add-to-dashboard (models/mis_report_instance.py:773-799, 957; wizard/mis_builder_dashboard.py:35-94).
- Formulas are evaluated by a restricted expression evaluator built on the core evaluator (models/mis_safe_eval.py:19-38).

## 2. Attachment to CORE
- Depends on core `account` and `board` (manifest:14-15); external: report_xlsx, date_range (manifest:16-17).
- Reads core `account.move.line` grouped by account and company (debit, credit sums) with a configurable "posted" versus "posted or draft" filter on the move-line parent state (models/aep.py:420-460; models/mis_report.py:911-930). Reads core `account.account` (selection by domain, including a per-company search using `company_ids`, models/aep.py:283-293) and company fiscal-year start via `compute_fiscalyear_dates` of the first company (models/aep.py:364-368). It writes nothing to accounting data.
- Core menus used: `account.menu_finance_reports` (views/mis_report_instance.xml:225) and `account.menu_finance_configuration` (views/mis_report.xml:305).
- Core method override: `ir.actions.report._render_qweb_pdf` (report/mis_report_instance_qweb.py:14-27). ADDS behavior: for this module's own PDF report only, it passes a landscape setting through context, then calls the parent unchanged; all other reports pass straight to parent.
- No override of posting, lock dates, valuation/cost, approvals, numbering. No `ALTERS CORE CONTROL` item found in the studied files.
- User-defined queries can read any model chosen by the report designer, using the user's own access rights on the model (models/mis_report.py:565-600); where the model has a company field, the query is restricted to the instance's allowed companies (models/mis_report_instance.py:413-416).

## 3. New objects, security, automation, external calls
- Persistent models: mis.report, mis.report.kpi, mis.report.subkpi, mis.report.kpi.expression, mis.report.query, mis.report.subreport, mis.report.style, mis.report.instance, mis.report.instance.period, mis.report.instance.period.sum, mis.report.instance.annotation; transient wizard add.mis.report.instance.dashboard.wizard; abstract mixins mis.kpi.data and prorata.read_group.mixin (models/__init__.py:4-11).
- Groups: "MIS Report: view annotations" and "MIS Report: add annotations" (implies view); the add-annotation group is auto-assigned to the root and admin users (security/res_groups.xml:3-16).
- ACLs: for all template/instance/style models, Accounting Manager (`account.group_account_manager`) has full rights, all internal users (`base.group_user`) read-only (security/ir.model.access.csv:2-21). Wizard: internal users read/write/create (:22). Annotations: read for view group, full for edit group (:23-24).
- Record rule: instances visible when company field empty or in the user's companies, and likewise for the multi-company list (security/mis_builder_security.xml:3-10). Applies to all users (no group set).
- Menus: Reporting entries gated by `account.group_account_readonly` (views/mis_report_instance.xml:228); template configuration under Accounting configuration (views/mis_report.xml:303-313).
- Cron: "Vacuum temporary reports" every 4 hours (datas/ir_cron.xml:3-10) which deletes temporary instances not modified for over 24 hours (models/mis_report_instance.py:668-676).
- The dashboard wizard creates a window action with elevated rights and a per-user customized dashboard view (wizard/mis_builder_dashboard.py:43-92).
- Annotation model creates a database index at initialization (models/mis_report_instance_annotation.py:36-44). No external network calls found; front-end widget assets registered (manifest:31-41).

## 4. Odoo 19 compatibility (grep against Community 19)
- Found in core: `Domain` (core:odoo/orm/domains.py:196, imported at models/aep.py:8), `compute_fiscalyear_dates` (core:addons/account/models/company.py:1115), `include_initial_balance` and `company_ids` on account.account (core:addons/account/models/account_account.py:71, 97), `_read_group` (core:odoo/orm/models.py:1867), `env._` (core:odoo/orm/environments.py:315), `_get_conversion_rate` (core:addons/base/models/res_currency.py:273), safe-eval helpers `compile_codeobj`, `assert_valid_codeobj`, `_SAFE_OPCODES`, `_BUILTINS` (core:odoo/tools/safe_eval.py:135, 222, 253, 318), `account.menu_finance_configuration`, `account.group_account_readonly`.
- No `<tree>` tags found in views; list view mode used (views/mis_report.xml:300).
- Manifest still declares a legacy `qweb` key (manifest:43); ignored by 19 as far as core structure shows: UNKNOWN - EVIDENCE INSUFFICIENT.
- Runtime behavior not exercised (no code run). Overall: no mismatch found in the checked references; not every reference checked (widget JS not reviewed: not checked).

## 5. Custom-to-custom dependencies
- report_xlsx (OCA reporting-engine) and date_range (OCA server-ux): outside Community and outside this folder; not read (manifest:16-17). The module sits in a folder named _REQUIRED_OCA_DEPENDS.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Whether fiscal-year start taken from the first selected company gives correct opening balances for multi-company instances with different fiscal calendars: UNKNOWN - EVIDENCE INSUFFICIENT (the code carries a note that this is a known limitation, models/aep.py:364).
- Behavior of the JavaScript widget and drill-down under Odoo 19 front-end: UNKNOWN - EVIDENCE INSUFFICIENT.
- Effect of the global multi-company rule combined with the user-defined query models: UNKNOWN - EVIDENCE INSUFFICIENT.
