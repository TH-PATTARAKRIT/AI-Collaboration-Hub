> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_reports_ext

## 0. Header
- Module: l10n_th_reports_ext
- License (confirmed in manifest): LGPL-3 (l10n_th_reports_ext/__manifest__.py:12)
- Author (manifest): SMEsPlus (l10n_th_reports_ext/__manifest__.py:10)
- Version (manifest): 19.0.1.4 (l10n_th_reports_ext/__manifest__.py:3)
- Path: addons_Extramodule/addons_extra/l10n_th_reports_ext (a second same-named folder exists at addons_Extramodule/addons/l10n_th_reports_ext; a file-level comparison reports that its manifest and tax_report_vat.py differ from this copy; that other copy was NOT read)
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Replaces the Excel export of the Thai Sales Tax Report and Purchase Tax Report (input/output VAT listing) with a custom spreadsheet layout: one line per journal entry with tax invoice number, reference, accounting date, contact, tax id, branch text, total amount, amount excluding VAT, VAT amount, bill date, tax branch, and the partner's legal-form title, plus a grand-total row (l10n_th_reports_ext/models/tax_report_vat.py:8-13,91-193).
- Header block shows report title (sales or purchase), the period from the report options, company name, VAT number and branch label (tax_report_vat.py:120-136).
- Amounts are aggregated per journal entry through a single database aggregation over the tax-tagged lines, signed by the tag's negate flag, ordered by earliest date (tax_report_vat.py:46-87). The module's own comment explains the aim as a performance improvement: fetching only line ids, aggregating in the database, then loading entries in bulk (tax_report_vat.py:24-44).
- Amounts use a fixed baht currency format regardless of company currency (tax_report_vat.py:96-97).
- For any origin type other than purchase or sale the standard export is used (tax_report_vat.py:12-13).

## 2. Attachment to CORE
- Manifest depends only on l10n_th_reports (manifest:13-15). That module is NOT in the Community 19 tree (no l10n_th_reports directory; core has only l10n_th) and no folder of that name was found under addons_Extramodule (directory listing), so the extended model is not verifiable here.
- Extends the abstract report handler model l10n_th.tax.report.handler (tax_report_vat.py:9): override of _generate_data - REPLACES the parent output for sale and purchase reports (super() is called only for other types) (tax_report_vat.py:11-13). ALTERS CORE CONTROL: no control; it changes what the exported tax report file contains, which is a statutory-reporting output. The parent handler and the report framework (account.generic_tax_report, _get_options_domain) belong to the Enterprise reporting layer, not to Community (grep of Community core found no such names).
- Reads core objects: account.move.line (tax_tag_ids, balance; core:account/models/account_move_line.py:234), account.account.tag (core:account/models/account_account_tag.py:14-20), account.move (name, ref, date, invoice_date, partner_id), res.partner (vat, parent_id, l10n_th_branch_name defined in core:l10n_th/models/res_partner.py:9-19), company (vat).
- Also reads partner fields branch and partner_company_type_id, which come from other add-ons (l10n_th_partner and partner_company_type) - not declared in this module's manifest (tax_report_vat.py:160-176; see section 5).

## 3. New objects, security, automation, external calls
- No new models, fields, ACLs, groups, rules, cron or external calls. Output is an in-memory spreadsheet built with the xlsxwriter library (tax_report_vat.py:91-93).
- Company scoping: the header uses the current environment company (tax_report_vat.py:129) while the line selection follows the report options' domain (tax_report_vat.py:19-22); multi-company selections in report options may not match the header company (not verified).

## 4. Odoo 19 compatibility
- Imports odoo.fields.Domain and odoo.tools.SQL (tax_report_vat.py:4-5): Domain exists in core 19 (Domain used elsewhere in core); SQL is imported but the aggregation is passed as a plain string with a parameter list through the cursor (tax_report_vat.py:54-80) - SQL import unused.
- The aggregation reads the column balance_negate of the tag table, but core 19 defines balance_negate as a computed field without storage (core:account/models/account_account_tag.py:20), so no such column is expected in the database; a direct database read would probably fail (not executed). Likewise it depends on a relation table name auto-generated for tax_tag_ids (comment at tax_report_vat.py:37-40; field core:account/models/account_move_line.py:234-238) - naming assumed, not verified.
- Parent module l10n_th_reports and its handler method signature _generate_data(base_tags, tax_tags, origin_type, options) are not present in the Community tree: UNKNOWN whether they exist in the target environment.
- xlsxwriter is imported inside the method (tax_report_vat.py:92); library availability not declared in the manifest.

## 5. Custom-to-custom dependencies
- Declared: only l10n_th_reports (Enterprise-origin, not in workspace listing).
- Implicit (undeclared): partner.branch from l10n_th_partner (l10n_th_partner/models/res_partner.py:15) and partner_company_type_id from the partner_company_type add-on (via l10n_th_partner manifest depends), read at tax_report_vat.py:160-176. If those add-ons are not installed the export would raise an attribute error.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: the parent l10n_th_reports source and the exact statutory format of the standard Thai tax report (parent not available).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the aggregation query runs correctly against the Odoo 19 schema (balance_negate column question above).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the layout matches the Revenue Department filing format (no specification read).
- UNKNOWN - EVIDENCE INSUFFICIENT: which of the two differing folders named l10n_th_reports_ext (addons vs addons_extra) is the deployed version; only the addons_extra copy was studied.
