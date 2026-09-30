> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: l10n_th_withholding_tax_report

Module: l10n_th_withholding_tax_report · License (confirmed in manifest): AGPL-3 (l10n_th_withholding_tax_report/__manifest__.py:9)
Author (manifest): Ecosoft, Odoo Community Association (OCA) (manifest:7) · Version (manifest): 19.0.1.0.1 (manifest:6)
Path: addons_Extramodule/addons_extra/l10n_th_withholding_tax_report
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a Thai withholding-tax (WHT) reporting wizard under Accounting > Reporting (l10n_th_withholding_tax_report/views/menu.xml:2-6). The user picks an income-tax form (PND3 or PND53), a date range and a company (wizard/withholding_tax_report_wizard.py:20-36).
- Produces the report as on-screen HTML, PDF, plain text (pipe-delimited lines, one per certificate line, in a Thai-calendar date style) and XLSX (wizard/withholding_tax_report_wizard.py:45-66, 231-233; models/report_withholding_tax.py:36-83; data/report_data.xml:4-49).
- Source rows are lines of withholding-tax certificates that are not in draft state (models/report_withholding_tax.py:150-161). The certificate model itself is not in core (see section 5).

## 2. Attachment to CORE
- Depends on core `account` (manifest:12). Attaches to core menu `account.menu_finance_reports` (views/menu.xml:4; core:account/views/account_menuitem.xml:37).
- Core object `ir.actions.report`: adds four report records for the module's own transient model (data/report_data.xml:4-49). No new columns on core models.
- Override `ir.actions.report.render_qweb_text` (models/ir_actions_report.py:22-30): ADDS behavior after the parent result (trims whitespace of the text output, plus an empty hook to swap character entities). Not a control alteration. Core 19 has no method of this name; it has `_render_qweb_text` (core:base/models/ir_actions_report.py:1104) - see section 4.
- Override `ir.ui.view._render` (models/ir_actions_report.py:36-42) and new helper `_prepare_qcontext` (:44-70): the module supplies its own rendering context (company, user, time helpers, json, image helper) for view records. In core 19 the view model has no method of these names (core:base/models/ir_ui_view.py:2543-2546 has only `render_public_asset` / `_render_template`), so this is a new method on every `ir.ui.view` record rather than a replacement of an existing core method. Effect on other callers of a view `_render`: UNKNOWN - EVIDENCE INSUFFICIENT.
- No override of posting, lock dates, valuation, approvals, numbering. No `ALTERS CORE CONTROL` item found in the studied files.

## 3. New objects, security, automation, external calls
- Transient models: `withholding.tax.report` (models/report_withholding_tax.py:13) and `withholding.tax.report.wizard` (wizard/withholding_tax_report_wizard.py:17); abstract XLSX report `report.withholding.tax.report.xlsx` (report/report_withholding_tax_xlsx.py:175-177).
- ACL: both transient models granted read/write/create/delete to `base.group_user` (security/ir.model.access.csv:2-3). No record rules, no new groups.
- Company scoping: wizard company field limited to the user's allowed companies (wizard/withholding_tax_report_wizard.py:39-43); the HTML/PDF/text path filters certificates by the company's partner (models/report_withholding_tax.py:158). The XLSX button path searches certificate lines by state, date and form only, with no company filter (wizard/withholding_tax_report_wizard.py:162); whether certificate-level record rules compensate is UNKNOWN - EVIDENCE INSUFFICIENT.
- The XLSX button writes the file as a binary `ir.attachment` and returns a download URL (wizard:205-229). No crons, no server actions, no outbound network calls found.
- Dead/duplicate files not imported by `__init__`: models/report_withholding_tax copy.py, models/report_withholding_tax.py_bkp, report/report_withholding_tax_xlsx_backup.py (models/__init__.py:3-4).
- Static asset registered: static/src/css/report.css (manifest:31).

## 4. Odoo 19 compatibility (grep against Community 19)
- MISMATCH: `super().render_qweb_text` - not present in core 19 (core has `_render_qweb_text`, core:base/models/ir_actions_report.py:1104); override at models/ir_actions_report.py:23 would fail if invoked.
- MISMATCH (tests only): `odoo.modules.module.get_resource_path` imported at l10n_th_withholding_tax_report/tests/test_wt_cert_report.py:5; grep of core module.py found no such function.
- Found in core: `keep_query` (core:base/models/ir_qweb.py:507), `image_data_uri` (core:odoo/tools/image.py:563), `pycompat.to_text` (core:odoo/tools/pycompat.py:27), `json.scriptsafe` (core:odoo/tools/json.py:59), config `test_enable` (core:odoo/tools/config.py:285).
- Report type value `xlsx` (data/report_data.xml:44) is not in core's selection (core:base/models/ir_actions_report.py:170-174); it depends on the external report_xlsx module.
- Wizard field `income_tax_form` selection is redefined locally, shadowing an import from the certificate module (wizard:14-15, 20-25).
- Fields read from partners (`branch`, `firstname`, `lastname`, `title`) at models/report_withholding_tax.py:45-52 and wizard:117-123 are not checked against core; `branch`/`firstname` presumably come from l10n_th_partner (external): UNKNOWN - EVIDENCE INSUFFICIENT.

## 5. Custom-to-custom / third-party dependencies
- Manifest depends (manifest:11-17): account (core), report_xlsx_helper, date_range, l10n_th_partner, l10n_th_withholding_tax_cert. The latter four are outside Community and outside this module folder; not read here.
- Wizard imports a constant from l10n_th_withholding_tax_cert (wizard:11).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Structure and semantics of `withholding.tax.cert` / `withholding.tax.cert.line` (state values, company_partner_id, tax_payer, wt_percent): UNKNOWN - EVIDENCE INSUFFICIENT (module not read).
- Whether the tax authority text layout produced by the text report matches any statutory filing format: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether the tests run on Odoo 19: UNKNOWN - EVIDENCE INSUFFICIENT (tests not executed).
