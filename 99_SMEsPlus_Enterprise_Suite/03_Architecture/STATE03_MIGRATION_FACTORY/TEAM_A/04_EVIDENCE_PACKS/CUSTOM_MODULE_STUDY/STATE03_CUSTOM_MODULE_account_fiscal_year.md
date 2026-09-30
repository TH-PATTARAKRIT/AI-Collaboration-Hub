> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_fiscal_year

Module: account_fiscal_year
License (confirmed in manifest): AGPL-3 (account_fiscal_year/__manifest__.py:14)
Author (manifest): Agile Business Group, Camptocamp SA, Odoo Community Association (OCA) (manifest:12)
Version (manifest): 19.0.1.0.0 (manifest:8)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_fiscal_year
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets finance staff define explicit fiscal-year periods per company (name, start date, end date) instead of relying only on the company's "last day / last month of fiscal year" setting. (account_fiscal_year/models/account_fiscal_year.py:9-31)
- Prevents a company from having overlapping fiscal-year records and rejects an end date earlier than the start date. (account_fiscal_year/models/account_fiscal_year.py:33-59)
- Shows the current fiscal-year start/end on the company list and form. (account_fiscal_year/views/res_company_views.xml:12-26)

## 2. Attachment to CORE
- Depends on core `account` (manifest:15-17).
- `res.company` (core account, core:account/models/company.py:74-75 defines the fiscal year-end day/month): module adds two read-only computed date fields, "start/end of current fiscal year" (account_fiscal_year/models/res_company.py:11-21).
- Override of core method `compute_fiscalyear_dates` on res.company (account_fiscal_year/models/res_company.py:30; core:account/models/company.py:1115): REPLACES the core answer when a matching fiscal-year record exists (returns that record's dates plus the record itself); when none matches it falls back to the core-style calendar computation, then trims the result so it does not run into neighbouring defined years (gap handling, res_company.py:56-84). Business effect: any caller of this helper gets the custom-record dates. Core callers found: core:analytic/models/analytic_line.py:273, core:stock_account/models/res_company.py:280, core:l10n_in/models/account_invoice.py:434. This is a change of a period-definition input, not of posting/lock dates; it is NOT the same field as the core fiscal-year lock date (core:account/models/company.py:76). Marked: ADDS/REPLACES period boundaries only; no `ALTERS CORE CONTROL` on posting, lock, valuation approvals found in this module.
- Views: inherits core company tree and form views (core:base/views/res_company_views.xml:4,64) to add the two fields.

## 3. New objects, security, automation
- New model `account.fiscal.year` (account_fiscal_year/models/account_fiscal_year.py:10).
- ACLs: account users read only; account managers full rights (account_fiscal_year/security/ir.model.access.csv:2-3).
- Record rule: multi-company scoping — records visible if no company or company is among the user's allowed companies (account_fiscal_year/security/account_fiscal_year_rule.xml:8-14).
- No crons, server actions, or external calls found.

## 4. Odoo 19 compatibility
- `odoo.fields.Domain` import used (account_fiscal_year/models/account_fiscal_year.py:6): exists in Community 19 (core:odoo/fields/__init__.py:20).
- `date_utils.get_fiscal_year` used (res_company.py:56): exists (core:odoo/tools/date_utils.py:232).
- `fiscalyear_last_day/month`, `compute_fiscalyear_dates` referenced: exist in core (see section 2).
- `self.env._` translation style is used (account_fiscal_year/models/account_fiscal_year.py:42); also used in core 19 (core:account/models/company.py:1130). No mismatches found. Tests folder not analysed.

## 5. Custom-to-custom dependencies
- None declared (manifest depends only on `account`).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether any other installed custom module relies on the returned `record` key of the overridden helper.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the on-disk copy matches the upstream OCA release.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the post-override results for the three core callers listed above with gaps between fiscal years (runtime not observed).
