> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_credit_control

Module: account_credit_control
License (confirmed in manifest): AGPL-3 (account_credit_control/__manifest__.py:46)
Author (manifest): Camptocamp, Odoo Community Association (OCA), Okia, Access Bookings, Tecnativa, ACSONE SA/NV (manifest:9-15)
Version (manifest): 19.0.1.0.0 (manifest:8)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_credit_control
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Overdue-receivable reminder ("dunning") process: a "run" on a controlling date finds unreconciled, posted receivable lines past due, and creates credit control lines per policy level (e.g. 1st/2nd/3rd reminder). (account_credit_control/models/credit_control_run.py:120-151; models/credit_control_policy.py:45-58, 141-155)
- Policies and levels: policy tied to receivable accounts; levels have delay days, computation basis (due date, end of month, previous reminder), channel (letter/email/phone), texts and mail template. (models/credit_control_policy.py:14-43, 288-332)
- Policy can be set per company, per partner, or per invoice; the more specific wins. (models/credit_control_policy.py:141-155; res_partner.py:31-38; account_move.py:14-26; res_company.py:15-23)
- Reminders are sent by email (grouped into a communication per partner/level/currency) or printed as letters; line states track draft/ignored/queued/to-do/sent/error. (models/credit_control_line.py:45-64; credit_control_communication.py:174-259; wizard/credit_control_emailer.py:46-68; wizard/credit_control_printer.py:43)
- Follow-up fields on the partner: responsible user, payment promise note, next action type/date, manual follow-up flag. (models/res_partner.py:42-70)
- Small-amount tolerance per company (default 0.1) so tiny balances do not trigger reminders. (models/res_company.py:12; credit_control_line.py:249-250)
- Analysis report (database view model) of reminder levels per partner. (report/account_credit_control_analysis.py:8-30)

## 2. Attachment to CORE
- Depends on core `base`, `account`, `mail` (manifest:17).
- `account.move` (core:account/models/account_move.py): adds policy and credit-line links (models/account_move.py:14-33).
- Override `button_cancel` on account.move (models/account_move.py:35; core:account/models/account_move.py:6384): ALTERS CORE CONTROL (cancellation). BLOCKS cancelling an invoice that has any credit control line beyond draft ("payment reminder already sent; issue credit note instead"); deletes draft credit lines silently; the lookup is done with elevated rights (py:41) so it applies regardless of user permissions. Otherwise calls core.
- `res.partner` (core:account/models/partner.py:550 receivable property): adds policy, follow-up fields, counter (res_partner.py:29-87). Constraint `_check_credit_policy` (res_partner.py:89-106) VALIDATES that the partner policy matches the partner's receivable account: ADDS validation on core partner save (also triggers when the core receivable account changes).
- `account.account`: adds read-only link to credit lines (models/account_account.py:10-17). `res.company`: adds tolerance and default policy (res_company.py:10-23). `res.config.settings`: exposes them plus "apply max policy level" default (res_config_settings.py:12-30).
- Override `_send` and `_postprocess_sent_message` on mail.mail (models/mail_mail.py:24-58; core:mail/models/mail_mail.py:250,769): ADDS behavior — after core, marks linked credit lines "sent" or "email error" based on outgoing mail outcome. Core calls unchanged.
- Override `_compute_body` on mail.compose.message when a context flag is set (wizard/mail_compose_message.py:13-37; core:mail/wizard/mail_compose_message.py:250): ADDS an invoice summary table to the email body.
- Uses `message_post_with_source` (core:mail/models/mail_thread.py:2638) and override `_message_auto_subscribe_followers` on its own model (credit_control_line.py:141; core:mail/models/mail_thread.py:4710).
- Views inherited: account.view_move_form, base.view_company_form, account.res_config_settings_view_form, account.partner_view_buttons, account.view_partner_property_form (views/account_move.xml:18; res_company.xml:6; res_config_settings_view.xml:6; res_partner.xml:19,43).
- Data record write on core company: sets default policy on `base.main_company` (data/data.xml:219-221, noupdate).
- Posting, lock dates, valuation and numbering are not touched. `ALTERS CORE CONTROL` applies to the cancel block and to the ACL grants below.

## 3. New objects, security, automation
- New models: credit.control.policy, .policy.level, .line, .run, .communication, .analysis (read-only DB view), res.partner.payment.action.type; wizards emailer, marker, printer, policy changer (manifest data list; models/*.py).
- Groups: Credit Control Info / User / Manager (implied chain) under a new privilege; Manager is added to the admin user (security/account_security.xml:4-39, 88-93).
- ACLs (security/ir.model.access.csv): ALTERS CORE CONTROL (security) — grants credit-control managers create/write/delete on core `mail.template` and `mail.message`, and users create/write on `mail.message` (csv:5-8); finance groups get read on credit lines, account managers full (csv:18-20).
- Record rules: global multi-company rules on run, communication, line, policy, analysis and action type using allowed companies (account_security.xml:42-87).
- Concurrency: run generation takes a database-level lock to stop parallel runs (credit_control_run.py:159-171). Line and policy selection use direct database queries in places (credit_control_policy.py:166-172; credit_control_communication.py:135-148; policy level lines 411-448), bypassing ORM record rules for those selections; policy module comment states ORM is used for move lines "to respect security rules" (policy.py:63-64,86).
- Deletion rule: only draft lines can be deleted (credit_control_line.py:278-288).
- External effects: outbound customer emails through mail templates and printed letters; no crons or server actions in this module (data list has no cron; grep of data/views/wizard found none). The queue-based sending is left to a separate module (comment at credit_control_communication.py:241).

## 4. Odoo 19 compatibility
- Checked and present in core 19: `res.groups.privilege` (core:base/models/res_groups_privilege.py:5), `_evaluate_res_ids` and `_compute_body` on composer (core:mail/wizard/mail_compose_message.py:250,1577), `_send` signature with `post_send_callback` (core:mail/models/mail_mail.py:769-770), `models.Constraint` usage style, `group_ids` on users, `base.main_company`/`base.user_admin`.
- No mismatches found among these. Views and remaining XML refs not exhaustively checked; QWeb report templates not read.

## 5. Custom-to-custom dependencies
- None declared in manifest. Mentions an optional companion `account_credit_control_queue_job` in a code comment (models/credit_control_communication.py:241); not present in this batch.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: legal/business validity of the shipped email texts and debt-collection wording in data/data.xml for this deployment.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether elevated-rights lookups and direct queries leak cross-company data in multi-company sessions (runtime not observed).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the cancel block on credit-note flows and e-invoice shortcuts using core `button_cancel`.
- UNKNOWN — EVIDENCE INSUFFICIENT: on-disk copy vs upstream OCA release.
