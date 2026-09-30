> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_tax_period_date

Module: smesplus_tax_period_date ("Tax Period Date")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 19.0.0.1
Path: addons_Extramodule/addons_extra/smesplus_tax_period_date
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom
Relationship to scgl_tax_period_date: a comparison of the two module trees, ignoring line endings, shows identical Python and view files; only the manifest author differs (SCGL vs SMEsPlus). The SMEsPlus copy holds LF line endings and leftover compiled cache folders; the SCGL copy has CRLF.

## 1. Business capability
- Lets accounting record a "Tax Period Date" on each journal entry or invoice = the reporting period in which the VAT of the document is to be declared, which can differ from the accounting date (smesplus_tax_period_date/models/tax_period.py:21-23).
- At entry creation, copies that date onto all tax lines of the entry so that tax lines can be reported by declared period (models/tax_period.py:25-31, 34-36).
- Exposes the header date on the entry form and a hidden-by-default column on the journal-items list (views/view_tax_period.xml:3-11, 24-33).
- Business relevance: it is the data source of the "Tax Period Date" column in the SMEsPlus Thai VAT sale/purchase reports (see smesplus_account_reports).

## 2. Attachment to CORE
- Core module depended on: account (__manifest__.py:1-17).
- account.move (core:account/models/account_move.py): new field tax_period (date), no default, not required (models/tax_period.py:22-23). Form position: before the invoice-date label block (views/view_tax_period.xml:8-10; core:account/views/account_move_views.xml:1077).
- account.move.line (core:account/models/account_move_line.py): new field tax_period_date (models/tax_period.py:34-36). List position: after the maturity-date column (views/view_tax_period.xml:29; core:account/views/account_move_views.xml:155, 188).
- Core method override: create on account.move (models/tax_period.py:25-31) - ADDS behavior after core. After core has created the entry and its automatically generated tax lines (core:account/models/account_move.py:3893-3894 and the line sync in core:account/models/account_move_line.py:1781-1800), the module writes the header date onto each line with a tax-line marker (core:account/models/account_move_line.py:212).
- What it does NOT do: no write override, so later edits of the header date, or tax lines added/recomputed after creation, are not re-stamped. No constraint ties the tax period to the accounting date or to the tax lock date.
- ALTERS CORE CONTROL: no. Posting, lock dates (core:account/models/account_move.py:2823), numbering, valuation and approvals are untouched. The write to tax lines occurs on a freshly created (draft) entry, so no posted-entry protection is engaged; behavior when entries are created directly in posted state is not applicable because core refuses that (core:account/models/account_move.py:3895-3896).

## 3. New objects, security, automation, external calls
- New models: none (field additions only).
- Security: none shipped; inherits core access of account.move / account.move.line. No groups, no record rules, no company scoping added.
- Cron, server actions, external calls: none.

## 4. Odoo 19 compatibility
- Checked: tax_line_id on account.move.line exists (core:account/models/account_move_line.py:212). View anchors o_td_label (core:account/views/account_move_views.xml:1077) and view_move_line_tree with date_maturity (core:account/views/account_move_views.xml:155, 188) exist.
- The create override uses the older single-model decorator but forwards the incoming list unchanged (models/tax_period.py:25-27), against core's multi-record create (core:account/models/account_move.py:3893-3894). Compatible in effect.
- Unused imports (models/tax_period.py:1-18): harmless. Commented-out block for a legacy list layout (views/view_tax_period.xml:12-20): inactive.
- models/__init__.py imports tax_period (checked by file inspection), so the model file is loaded.

## 5. Custom-to-custom dependencies
- Declared dependencies: none.
- Depended on by: smesplus_account_reports (smesplus_account_reports/__manifest__.py:16).
- Duplicate of scgl_tax_period_date (same field names). Both installed together: outcome not observed.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether users are expected to set tax_period manually on every document or a rule elsewhere defaults it (no default found in module).
- UNKNOWN - EVIDENCE INSUFFICIENT: how existing entries created before installation are back-filled (no migration or data file in module).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the line-level tax_period_date is used by any report; only the header value is read by the studied report module.
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of import / multi-record creation when the tax lines are generated only after the create call returns.
