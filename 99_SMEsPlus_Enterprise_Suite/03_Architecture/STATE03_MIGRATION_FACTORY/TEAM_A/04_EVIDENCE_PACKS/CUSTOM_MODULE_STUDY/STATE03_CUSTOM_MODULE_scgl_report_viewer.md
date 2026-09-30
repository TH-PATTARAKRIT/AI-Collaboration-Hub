> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_report_viewer

Module: scgl_report_viewer
License (confirmed in manifest): AGPL-3 (scgl_report_viewer/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_report_viewer/__manifest__.py:8)
Version (manifest): 19.0.7.8.0 (scgl_report_viewer/__manifest__.py:5)
Path: Extra_Module_scgl/scgl_report_viewer
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- One common screen (client-side component) for accounting reports with a shared filter bar (period, comparison, journals, posted-only), expandable rows, drill-down to journal items, PDF/XLSX export and a warning row for unposted entries (scgl_report_viewer/__manifest__.py:3-4; scgl_report_viewer/models/report_engine.py:394-435).
- Report kinds registered: Balance Sheet, Profit and Loss, Cash Flow, Executive Summary (fed by OCA mis_builder, scgl_report_viewer/models/report_engine.py:35-40); Trial Balance, General Ledger, Partner Ledger, Aged Receivable, Aged Payable, Aged Partner Balance, Journal Audit, Tax Report, Depreciation Schedule (fed by OCA account_financial_report / account_asset_management; scgl_report_viewer/models/report_kinds.py:4-31).
- Thai tax return layouts computed inside the module from the ledger: VAT return (12 items), generic tax report grouped by account or tax, withholding forms PND53 and PND3, with period comparison (scgl_report_viewer/models/report_engine_tax.py:25-256; scgl_report_viewer/models/report_kinds.py:25-27).
- Per-company report settings (title, default period, default posted-only, default variant, default journals, visible/ordered columns), available to accounting managers (scgl_report_viewer/models/viewer_config.py:11-96; scgl_report_viewer/views/viewer_config_views.xml:62).
- Chatter side panel for partner and journal-entry rows; a "Returns" button to a tax-return module (scgl_report_viewer/models/report_engine.py:169-178; scgl_report_viewer/static/src/report_viewer/report_viewer.js:13).
- The provenance note states the code was written new from specifications, not from Enterprise report code (scgl_report_viewer/PROVENANCE.txt:5-7).

## 2. Attachment to CORE
- account (core): declared dependency (scgl_report_viewer/__manifest__.py:10); reads account.move, account.move.line, account.account, account.journal, account.tax, res.partner (scgl_report_viewer/models/report_engine.py:116, 134, 359, 403; scgl_report_viewer/models/report_engine_tax.py:69). No core Python method is overridden (all classes are new abstract/regular models).
- Menu re-pointing: existing menu entries (OCA ledger and financial-statement menus, custom account-menu entries, asset report menu) are changed to open this viewer instead of their original wizards/forms (scgl_report_viewer/views/actions.xml:51-65, 71-73, 90-111). REPLACES the entry screen of those OCA/custom reports; the OCA wizards remain used behind the scenes for exports (scgl_report_viewer/PROVENANCE.txt:20).
- Core JS reuse: Layout, popover, action service, mail Chatter (scgl_report_viewer/static/src/report_viewer/report_viewer.js:7-14); files exist in Community 19 (core:web/static/src/search/layout.js; core:mail/static/src/chatter/web_portal/chatter.js).
- Data source rules: the tax engine reads ledger data with direct database queries for the active company only, dated within the period, posted (or posted+draft when "unposted" is included) (scgl_report_viewer/models/report_engine_tax.py:31-70). These queries bypass ORM record rules. ALTERS CORE CONTROL (record-rule and multi-company allowed-companies scoping for tax reports; only the active company is used). Other kinds go through OCA wizards / mis_builder with ORM rules.
- Includes draft entries in tax figures when the user clears the posted-only option (scgl_report_viewer/models/report_engine_tax.py:33). Not a control change in core, but a reporting choice.
- No posting, lock-date, valuation, numbering or approval logic is touched.

## 3. New objects, security, automation, external calls
- New models: scgl.report.viewer.config and scgl.report.viewer.config.column (scgl_report_viewer/models/viewer_config.py:11, 87); unique per report kind and company via models.Constraint (line 26); abstract engine scgl.report.engine (scgl_report_viewer/models/report_engine.py:46-47).
- ACL: accounting managers full; accounting read-only users read (scgl_report_viewer/security/ir.model.access.csv:2-5). Menu "Report Viewer configuration" for accounting managers (scgl_report_viewer/views/viewer_config_views.xml:62). Opening the settings dialog is also checked in code (scgl_report_viewer/models/report_engine.py:465). No record rules; company scoping via a required company field defaulting to the current company (scgl_report_viewer/models/viewer_config.py:17).
- Engine methods are on an abstract model with no explicit group check in the report calls (grep for group checks found only config-related ones: scgl_report_viewer/models/report_engine.py:104, 465). Reachability of these methods by any internal user: UNKNOWN.
- Automation: a data-load function runs on every install/update to mark P&L / cash-flow / summary KPIs as budgetable (scgl_report_viewer/data/budgetable_kpis.xml:6; scgl_report_viewer/models/report_engine.py:180-198). Writes to mis_builder KPI records; no effect when the budget module is absent. No cron.
- Temporary mis_builder report instances are created per view and rely on that module's cleanup job (scgl_report_viewer/models/report_engine.py:251-312, 436-437).
- Creates temporary OCA wizard records to obtain report values (scgl_report_viewer/models/report_engine_oca.py:110-149).
- External calls: none.

## 4. Odoo 19 compatibility
- The module was written against 19 (version 19.0.7.8.0); core imports and the `models.Constraint` style are 19-compatible (core:web/static/src/webclient/actions/action_service.js:82).
- Core account fields used: matching_number, tax_line_id, tax_ids, date_maturity (core:account/models/account_move_line.py:195, 212, 304, 390); account.account `company_ids` (core:account/models/account_account.py:97).
- Non-Community models/wizards relied on (present only if OCA modules installed): mis.report.instance, mis.budget (mis_builder), *.report.wizard (account_financial_report), account.asset (asset management), account.withholding.move (guarded by a presence check, scgl_report_viewer/models/report_engine_tax.py:209-210), account.age.report.configuration (scgl_report_viewer/models/report_engine_oca.py:365). Their code was not read; compatibility with Community 19 for those: not checked.
- Mail is used in JS but not listed in the manifest depends; it comes indirectly through account (core dependency chain): not checked.
- Manifest depends on scgl_account_statements and scgl_account_menu (custom). The `Returns` action is looked up by xml id with "raise if not found" disabled (scgl_report_viewer/models/report_engine.py:173).
- Tests present (scgl_report_viewer/tests/test_report_viewer.py, 728 lines); not run.

## 5. Custom-to-custom dependencies
- scgl_account_statements, scgl_account_menu (scgl_report_viewer/__manifest__.py:10).
- Optional at runtime: scgl_account_tax_return (scgl_report_viewer/models/report_engine.py:173).
- Non-Community third-party: mis_builder, account_financial_report, account_asset_management (AGPL OCA).
- A sibling module (scgl_report_viewer_deferred) depends on this one; not studied here.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: correctness of Thai tax classification rules (withholding detection by amount sign or tax name keywords, exempt detection by name; scgl_report_viewer/PROVENANCE.txt:41-42) against the deployed tax configuration.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether users without accounting rights can call the engine methods over RPC.
- UNKNOWN - EVIDENCE INSUFFICIENT: multi-company behavior of OCA-fed reports.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether item 10 (carried-forward VAT) is ever populated; the note says it is zero and not stored (scgl_report_viewer/PROVENANCE.txt:42).
