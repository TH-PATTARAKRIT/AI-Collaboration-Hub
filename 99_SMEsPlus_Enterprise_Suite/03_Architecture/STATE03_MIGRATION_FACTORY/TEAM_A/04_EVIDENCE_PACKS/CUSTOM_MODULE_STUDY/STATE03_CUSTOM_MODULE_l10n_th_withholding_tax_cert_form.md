> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_withholding_tax_cert_form

## 0. Header
- Module: l10n_th_withholding_tax_cert_form
- License (confirmed in manifest): AGPL-3 (l10n_th_withholding_tax_cert_form/__manifest__.py:8)
- Author (manifest): Ecosoft, Odoo Community Association (OCA), SMEsPlus (l10n_th_withholding_tax_cert_form/__manifest__.py:7)
- Version (manifest): 19.0.1.0.2 (l10n_th_withholding_tax_cert_form/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/l10n_th_withholding_tax_cert_form
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a PDF print-out "WT Certificates (pdf)" of a withholding tax certificate laid out to fill the statutory Thai withholding-tax certificate form (pre-printed style: absolutely positioned text, no page margins) (l10n_th_withholding_tax_cert_form/data/report_data.xml:13-23; data/paper_format.xml:2-16; reports/layout.xml:2-439).
- Printed content: certificate number and the number of the certificate it substitutes; payer and payee tax-ID printed one digit per box, names and addresses; income tax form tick (PND1/PND3/PND3a/PND53 etc.); payment date converted to the Buddhist calendar year (adds 543) (reports/layout.xml:11-19,24-62,97-135,176-189); lines grouped by income type with date, base and tax amount per type, with free-text descriptions for "other" types (reports/layout.xml:190-372, helper models/withholding_tax_cert.py:10-25); totals and the total tax amount in Thai words (reports/layout.xml:374-386); three contribution amounts (government pension/teachers' welfare fund, social security fund, provident fund) shown in a "money paid in" block (reports/layout.xml:388-410).
- Adds those three contribution amounts as manual input fields on the certificate form, editable in Draft (models/withholding_tax_cert.py:27-29; views/withholding_tax_cert.xml:7-16).
- Manifest also registers a report stylesheet in the report asset bundle (manifest:18-22).

## 2. Attachment to CORE
- Depends on web, l10n_th_withholding_tax_cert, l10n_th_amount_to_text (manifest:11); the latter two are custom/third-party (section 5). Core objects used: ir.actions.report and report.paperformat (data records), the web report container template (reports/layout.xml:441 calls web.html_container).
- Extends custom model withholding.tax.cert (models/withholding_tax_cert.py:8): new fields and two helper methods (_compute_desc_type_other, _group_wt_line). ADDS only. The grouping helper uses read_group (models/withholding_tax_cert.py:19-24), which still exists in core 19 (core:orm/models.py:2755).
- Paper format record: marks "Withholding tax A4" as default with zero margins (data/paper_format.xml:4,9-12). If the default flag makes this the default paper format for other reports, their layout could be affected; not verified against core semantics.
- Calls the Thai amount-to-text override from l10n_th_amount_to_text through the currency with Thai language context (reports/layout.xml:383-385; see l10n_th_amount_to_text file).
- Defines an abstract report model (reports/withholding_report_pdf.py:7-21) named report.withholding_tax_pdf; the core report engine looks up report.<report_name> where report_name = l10n_th_withholding_tax_cert_form.withholding_tax_pdf (core:base/models/ir_actions_report.py:1122), so this model probably is not used, and the core default supplies the document list. Effect: none visible.
- No core method overridden. ALTERS CORE CONTROL: no.

## 3. New objects, security, automation, external calls
- No new persistent models; three new float fields on withholding.tax.cert (no tracking). No ACLs, groups, rules, cron, external calls. Access to the report follows that of withholding.tax.cert (ACL: invoicing group; see l10n_th_withholding_tax_cert file). Multi-company: inherits the company rule of the certificate.
- Report is bound to the certificate model's Print menu (data/report_data.xml:20-21).

## 4. Odoo 19 compatibility
- The layout takes characters of the tax id by slicing (reports/layout.xml:25-61,99-135); if a tax id is empty the print fails (slicing a missing value). Checked by reading the template only.
- Template date handling assumes o.date is set, otherwise blank (reports/layout.xml:182-189).
- Test file test_wt_cert_form.py uses SingleTransactionCase and render_qweb_pdf (tests/test_wt_cert_form.py:5-43); not run.
- The layout depends on the certificate lines' income type codes (4B14, 4B25, 6 etc.) defined in l10n_th_withholding_tax_cert (reports/layout.xml:272,332,359).
- Fonts/stylesheet in static/ not examined.

## 5. Custom-to-custom dependencies
- l10n_th_withholding_tax_cert (extends its model and view l10n_th_withholding_tax_cert.view_withholding_tax_cert_form, views/withholding_tax_cert.xml:5) and l10n_th_amount_to_text (Thai amount in words) - both declared in manifest:11.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the layout coordinates match the current Revenue Department form on a physical printer (no print test performed).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the "default" paper-format flag has effects on other reports.
- UNKNOWN - EVIDENCE INSUFFICIENT: how the contribution amounts are supposed to be validated against income types (no logic ties them to lines).
