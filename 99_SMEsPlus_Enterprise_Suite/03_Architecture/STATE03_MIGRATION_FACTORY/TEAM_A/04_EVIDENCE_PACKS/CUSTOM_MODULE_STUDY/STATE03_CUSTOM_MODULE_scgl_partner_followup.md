> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_partner_followup

Module: scgl_partner_followup
License (confirmed in manifest): LGPL-3 (scgl_partner_followup/__manifest__.py:7)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_partner_followup/__manifest__.py:8)
Version (manifest): 19.0.1.0.0 (scgl_partner_followup/__manifest__.py:5)
Path: Extra_Module_scgl/scgl_partner_followup
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds hidden-by-default columns to the customer list for payment follow-up: responsible user, reminder mode (automatic/manual), follow-up status, next reminder date, follow-up level, total due, total overdue (scgl_partner_followup/views/res_partner_views.xml:10-20).
- Total due = unreconciled, posted receivable balance across the partner's commercial entity; overdue = the part past its due date (scgl_partner_followup/models/res_partner.py:61-74, 76-90).
- Status: "in need of action" when overdue and next reminder date is empty/reached; "with overdue invoices" when overdue but next reminder is in the future; "no action needed" otherwise (scgl_partner_followup/models/res_partner.py:86-90).
- Two search filters on the customer list: in need of action, with overdue invoices (scgl_partner_followup/views/res_partner_views.xml:30-34).
- The header says the design came from screenshots, without reading Enterprise code (scgl_partner_followup/models/res_partner.py:2).

## 2. Attachment to CORE
- res.partner (core:base, core:account): ADDS fields listed above. No core method overridden; all methods are new (scgl_partner_followup/models/res_partner.py:36-107).
- Responsible user defaults to the partner's salesperson but is editable and stored (scgl_partner_followup/models/res_partner.py:17-19, 36-39). ADDS a default.
- Reads account.move.line: receivable lines, posted, unreconciled, using `amount_residual`, `date_maturity`, `reconciled`, `parent_state`, `account_type` (scgl_partner_followup/models/res_partner.py:65-71); all exist (core:account/models/account_move_line.py:69, 246, 258, 317, 390). Read only; nothing is written to ledger.
- Depends on OCA `account_credit_control` (non-Community; scgl_partner_followup/__manifest__.py:10): fields `manual_followup`, `payment_next_action_date`, and models `credit.control.line`, `credit.control.policy.level` come from there (scgl_partner_followup/models/res_partner.py:25, 41, 44, 53). Writing "Reminders = manual" flips the OCA manual-followup flag on the partner (scgl_partner_followup/models/res_partner.py:46-48) - this changes whether the partner is included in automatic credit-control runs (per field help, scgl_partner_followup/models/res_partner.py:23). Classified: ADDS behavior on an OCA control, not a core control. No core posting/lock-date/valuation/numbering control is altered.
- Views: inherit `base.view_partner_tree` after column `company_id` (core:base/views/res_partner_views.xml:14, 33) and `base.view_res_partner_filter` before `inactive` (core:base/views/res_partner_views.xml:330).

## 3. New objects, security, automation, external calls
- No new models, ACLs, groups, crons, server actions, or external calls.
- Multi-company: totals are computed from lines visible to the current user; no explicit company filter, so with several companies selected they add up across companies (scgl_partner_followup/models/res_partner.py:65-71). Record rules of account.move.line apply because the ORM grouping is used.
- Amounts are computed on the fly (not stored); the search on status computes all overdue partners then filters (scgl_partner_followup/models/res_partner.py:92-107).

## 4. Odoo 19 compatibility
- Core fields used exist in Community 19 (see section 2). `currency_id` on partner comes from the account module (core:account/models/partner.py:543). `_read_group` with aggregate `amount_residual:sum` matches the 19 style.
- OCA module account_credit_control 19.0.1.0.0 is present in the workspace's required-OCA folder (Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_credit_control/__manifest__.py:8); its code was not read.
- Field `commercial_partner_id` exists (core:base/models/res_partner.py:518-520).
- Test file exists (scgl_partner_followup/tests/test_partner_followup.py); not run.
- No mismatches with Community 19 found in the files read.

## 5. Custom-to-custom dependencies
- None on scgl_* modules. OCA dependency: account_credit_control.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: how OCA credit-control runs treat partners set to manual (OCA code not read).
- UNKNOWN - EVIDENCE INSUFFICIENT: performance of the totals/search on large ledgers (unbounded aggregation).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether foreign-currency receivables are converted before summing (the sum uses residual in company currency field `amount_residual`; currency of total_due is the partner's company currency).
