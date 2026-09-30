> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_account_followup

Module: om_account_followup · License (confirmed in manifest): LGPL-3 (om_account_followup/__manifest__.py:8)
Author (manifest): Odoo Mates, Odoo S.A (manifest:7) · Version (manifest): 1.0.3 (manifest:3)
Path: addons_Extramodule/addons_extra/om_account_followup
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Customer payment follow-up (dunning): a company-level plan of follow-up levels, each with days after due date, a printed message, and switches for "send email", "send letter" and "manual action" (with responsible user and note) (om_account_followup/models/followup.py:5-78).
- A processing wizard finds partners with overdue receivable items, assigns the follow-up level per item, sends emails, prepares letters (PDF report), creates manual actions and clears finished ones (wizard/followup_print.py:45-145).
- Partner form gets a follow-up tab: responsible, next action and date, note, unreconciled receivable items, latest level and date, amount due / overdue, worst due date (models/partner.py:360-413; views/partners.xml:76-139).
- Statistics views by partner and by item (models/followup_partner.py:5-23; report/followup_report.py:5-8) and four email templates (data/mail_template_data.xml:6, 44, 84, 121).

## 2. Attachment to CORE
- Depends on core `account` and `mail` (manifest:10).
- `account.move.line` (models/account_move.py:4-13): adds follow-up level, latest follow-up date, and a computed balance amount. No method override.
- `res.partner` (models/partner.py:10-413): adds the follow-up fields above plus actions to print, email and mark done. Core method overrides by name:
  - `write` (models/partner.py:203-222): ADDS behavior around core - when the payment responsible changes, posts a chatter notification to the new responsible before calling the parent. Not a control alteration.
  - `fields_view_get` (models/partner.py:13-24): a view-architecture hook that moves the follow-up tab first when a context flag is set; does not exist in Community 19 (see section 4).
- `res.config.settings` (models/settings.py:4-15): ADDS an action to open the follow-up levels form.
- Reads core receivable items: account type receivable, not fully reconciled, with due date (models/partner.py:230-240, 380-383). Writes follow-up level and date on `account.move.line` (wizard/followup_print.py:107-112), including items of posted entries; whether core immutability checks apply to those two fields: UNKNOWN - EVIDENCE INSUFFICIENT.
- Core views/menus: partner form/tree/search (base), `account.view_move_line_form` (views/account_move.xml:63), menus `account.menu_finance_configuration` and `account.menu_finance` (views/followup_view.xml:190-206; wizard/followup_print_view.xml:40).
- No override of posting, lock dates, valuation, approvals, numbering, security or record rules of core models. No `ALTERS CORE CONTROL` item.

## 3. New objects, security, automation, external calls
- Models: followup.followup (one per company; unique constraint, models/followup.py:14-17), followup.line (unique days per plan, :75-78, description format validation :80-91), followup.stat.by.partner and followup.stat (database views, `_auto = False`), transients followup.print and followup.sending.results.
- ACLs (security/ir.model.access.csv:2-11): Invoicing group read on plan/levels; Manager full; statistic models read/write for Invoicing/Accountant; the two transient wizards full rights for every internal user (`base.group_user`, :10-11) - the processing wizard is therefore model-accessible to all internal users, while menu entries are group-limited (wizard/followup_print_view.xml:48).
- Record rules: three global rules on plan and both statistics models limiting to the user's company and its child companies (security/security.xml:5-28). Note rule uses the user's main company, not the set of allowed companies.
- Automation: no cron; processing is manual through the wizard. It sends outbound emails to customers through mail templates (models/partner.py:102-147), posts chatter messages, and creates manual actions. Emails go out via the standard mail queue: external effect.
- No server actions, no HTTP calls.
- Duplicate menu records with identical ids appear twice in one file (views/followup_view.xml:190-197 and 199-206).
- Demo data present (manifest:25).

## 4. Odoo 19 compatibility (grep against Community 19)
- MISMATCH: `super().fields_view_get(...)` (models/partner.py:13-16); no `fields_view_get` definition exists anywhere under the Community 19 tree (grep of all Python files). The override is dead code unless something calls it.
- Found in core: `models.Constraint` (core:odoo/orm/table_objects.py:79, used at models/followup.py:14 and :75), `account.view_move_line_form`, `account.menu_finance`, `account.menu_finance_configuration`, `base.view_partner_form`, `base.view_partner_tree`, `base.view_res_partner_filter`, receivable account type `asset_receivable` (core:account/models/account_account.py:30), `full_reconcile_id` and `date_maturity` (core:account/models/account_move_line.py:259, 390).
- No field-name clash found in core Python for `payment_responsible_id`, `payment_next_action`, `unreconciled_aml_ids` or `latest_followup*` (grep in core account and base models). Core has a `no_followup` field on journal items (referenced only in core tests, core:account/tests/test_account_move_out_invoice.py:4903): its relation to this module: UNKNOWN - EVIDENCE INSUFFICIENT.
- Database-view SQL on move lines (models/followup_partner.py:28-48; report/followup_report.py:25) not verified against 19 column set: not checked.

## 5. Custom-to-custom dependencies
- None declared (only core account and mail).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Effect of the record rule based on the user's main company when several companies are active: UNKNOWN - EVIDENCE INSUFFICIENT.
- Wording of email/print templates against legal or local dunning requirements: UNKNOWN - EVIDENCE INSUFFICIENT (templates not analysed).
- Whether the follow-up fields on posted journal items trigger any core protection when written: UNKNOWN - EVIDENCE INSUFFICIENT.
