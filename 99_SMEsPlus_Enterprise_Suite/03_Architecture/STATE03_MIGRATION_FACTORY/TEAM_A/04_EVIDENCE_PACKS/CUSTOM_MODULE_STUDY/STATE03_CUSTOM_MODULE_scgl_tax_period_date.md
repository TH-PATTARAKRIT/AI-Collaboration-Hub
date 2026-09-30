> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_tax_period_date

Module: scgl_tax_period_date ("Tax Period Date")
License (confirmed in manifest): LGPL-3
Author (manifest): SCGL
Version (manifest): 19.0.0.1
Path: Extra_Module_scgl/scgl_tax_period_date
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_06): Customer-authorized Custom
Note: functionally the same module as smesplus_tax_period_date (see that file). Comparison of both trees, ignoring line-ending differences, shows the Python and view files are identical; only the manifest author differs (SCGL vs SMEsPlus) and this copy has CRLF line endings in its Python file.

## 1. Business capability
- Lets an accountant record a "Tax Period Date" on a journal entry/invoice, i.e. the period in which the VAT on the document should be reported, independent of the accounting date (scgl_tax_period_date/models/tax_period.py:21-23).
- Copies that date onto the tax lines of the entry when the entry is created, so tax lines can be listed/filtered by declared tax period (models/tax_period.py:25-31, 34-36).
- Shows the date on the entry form and (optional, hidden by default) on the journal-item list (views/view_tax_period.xml:3-11, 24-33).

## 2. Attachment to CORE
- Core module depended on: account (__manifest__.py:1-17).
- account.move: adds field tax_period (date) (models/tax_period.py:22-23). Form field inserted before the label block of the invoice-date area (views/view_tax_period.xml:8-10; core:account/views/account_move_views.xml:1077).
- account.move.line: adds field tax_period_date (models/tax_period.py:34-36). List column added after the maturity-date column (views/view_tax_period.xml:29; core:account/views/account_move_views.xml:155, 188).
- Core method override: account.move create (models/tax_period.py:25-31). It ADDS behavior after core: after the entry is created it writes the header date onto every line that carries a tax line marker. It does not replace core creation.
- Gaps observed: no write override, so changing the header date later does not update existing tax lines; tax lines produced by later edits are not stamped (models/tax_period.py:25-31 is the only propagation).
- ALTERS CORE CONTROL: no. Posting, lock dates, numbering, approvals untouched. Note that the header field is not blocked by lock dates because no lock check is involved (no evidence of any check in module).

## 3. New objects, security, automation, external calls
- New models: none (two field additions only).
- Security: none shipped (no ACL file, no groups, no record rules); inherits core access on account.move / account.move.line.
- Cron, server actions, external calls: none.

## 4. Odoo 19 compatibility
- Checked: core account.move.line tax_line_id exists (core:account/models/account_move_line.py:212); core account.move create is multi-record (core:account/models/account_move.py:3893-3894) while this override is declared with the single-record decorator but passes the list straight through to core (models/tax_period.py:25-27) - works with list input; style is outdated only.
- Checked: view anchors o_td_label (core:account/views/account_move_views.xml:1077) and view_move_line_tree (core:account/views/account_move_views.xml:155) exist.
- Commented-out block references a legacy tree/page layout (views/view_tax_period.xml:12-20) and is inactive.
- Many imports in models/tax_period.py:1-18 are unused (harmless).

## 5. Custom-to-custom dependencies
- Declared: none. The header field tax_period is read by smesplus_account_reports, but that module declares a dependency on the SMEsPlus copy, not this one (smesplus_account_reports/__manifest__.py:16; report reads at smesplus_account_reports/models/account_generic_tax_report.py:38, 415); the line-level tax_period_date is not read there. Duplicate of smesplus_tax_period_date: installing both would define the same field names twice on the same models; combined behavior not observed.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: which of the two copies (SCGL or SMEsPlus) is the deployed one in a given customer database.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the tax authority report of the customer relies on tax_period_date on lines or on the header tax_period (this module supplies both; the report module studied uses the header).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior for entries created in batches or by import when tax lines are generated after create.
