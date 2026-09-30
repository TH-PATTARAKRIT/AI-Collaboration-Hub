> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_recurring_payments

Module: om_recurring_payments · License (confirmed in manifest): LGPL-3 (om_recurring_payments/__manifest__.py:11)
Author (manifest): Odoo Mates (manifest:3) · Version (manifest): 1.0.0 (manifest:5; name string says "Odoo 19 Recurring Payment", manifest:2)
Path: addons_Extramodule/addons_extra/om_recurring_payments
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Schedules repeating customer receipts or supplier payments. A template defines journal, period unit (days/weeks/months/years), interval, and whether generated payments are left unposted or posted (om_recurring_payments/models/recurring_template.py:5-23).
- A recurring payment picks partner, amount, direction (inbound/outbound), template (must be in "done" state), start and end dates; confirming it generates one schedule line per period between the dates (models/recurring_payment.py:7-36, 38-70).
- A daily job turns each due, not-yet-done schedule line into a real payment and optionally posts it (models/recurring_payment.py:80-84, 123-138; data/recurring_cron.xml:5-13).

## 2. Attachment to CORE
- Depends on core `account` only (manifest:10). No `_inherit` of any core model: the module has no override of any core method, so nothing is added, replaced or blocked in core objects by inheritance.
- Creates core `account.payment` records (payment type, amount, currency, journal, company, date, memo carrying the recurring reference, partner) and, when the template says "Posted", calls core payment posting (models/recurring_payment.py:124-138). Posting therefore goes through core `action_post` (core:account/models/account_payment.py:1130), so core lock-date, journal and validation checks apply. No bypass found. No `ALTERS CORE CONTROL` item.
- Core link fields used: `account.journal`, `res.partner`, `res.company`, `res.currency` (models/recurring_payment.py:13-19, 112-119).
- Core menu used: `account.menu_finance_configuration` (views/recurring_template_view.xml:56-60).
- Numbering: uses its own sequence code `recurring.payment`, prefix RP, padding 3, no company (data/sequence.xml:6-12; models/recurring_payment.py:86-94). Not the core payment numbering.

## 3. New objects, security, automation, external calls
- Models: account.recurring.template, recurring.payment, recurring.payment.line (models/__init__.py:1-2).
- ACLs (security/ir.model.access.csv:2-4): Accountant (`account.group_account_user`) full rights on templates and recurring payments; Invoicing group (`account.group_account_invoice`) full rights on schedule lines. No record rules and no new groups: multi-company isolation is not enforced by any rule in this module (company field present with defaults only, models/recurring_payment.py:14, 117; recurring_template.py:23). Effective isolation depends on core rules: UNKNOWN - EVIDENCE INSUFFICIENT.
- Cron "Generate Recurring Payments", daily, noupdate (data/recurring_cron.xml:5-13). It scans schedule lines of all companies dated today or earlier and not done, and creates (and, per template, posts) payments for each (models/recurring_payment.py:80-84). There is no per-line error isolation in the loop; one failing line (for example a payment date inside a locked period) would end the run for the remaining lines - behavior when core raises an error: UNKNOWN - EVIDENCE INSUFFICIENT (code not run).
- Guards: cannot delete a "done" recurring payment (models/recurring_payment.py:101-105); cannot reset to draft if any line is done (:72-78); amount must be positive (:96-99).
- Observed logic points (not run): the create override passes the last loop record's values rather than the whole batch to the parent (models/recurring_payment.py:86-94); the schedule-line default date is fixed at module load time (:115); a helper `_compute_next_call` in the template model references fields that the model does not define and is not attached to any field (models/recurring_template.py:25-32); a context key `force_company` is used for sequence selection (:90).
- No external network calls, no server actions.

## 4. Odoo 19 compatibility (grep against Community 19)
- Found in core: `memo`, `payment_type`, `date` on account.payment (core:account/models/account_payment.py:107, 99, 16), `action_post` (:1130), menu `account.menu_finance_configuration`.
- MISMATCH (harmless): context key `force_company` is not used by core sequence selection in 19; company is taken from the current environment (core:base/models/ir_sequence.py:286-287).
- Field `next_call`, `date_begin`, `date_end` referenced by `_compute_next_call` do not exist on account.recurring.template (models/recurring_template.py:25-32): dead code, not a runtime reference in 19 unless called.
- Views were not checked against Community 19 view ids beyond menu parents: not checked.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Whether payments created for a journal from a different company than the schedule line's company are rejected by core: UNKNOWN - EVIDENCE INSUFFICIENT.
- Which user identity the cron uses for created payments and how bank reconciliation/approval workflow interacts with auto-posted payments: UNKNOWN - EVIDENCE INSUFFICIENT.
- Behavior for schedules whose end date is inclusive (loop stops before the end date, models/recurring_payment.py:66): UNKNOWN - EVIDENCE INSUFFICIENT as to intended business rule.
