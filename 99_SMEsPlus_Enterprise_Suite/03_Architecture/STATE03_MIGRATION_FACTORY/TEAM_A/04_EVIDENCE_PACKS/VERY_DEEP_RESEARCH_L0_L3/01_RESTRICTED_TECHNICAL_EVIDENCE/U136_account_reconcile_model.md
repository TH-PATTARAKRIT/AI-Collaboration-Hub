# U136 — account.reconcile.model Rule Engine (GAP-021)
**Unit:** U136 | **Group:** G01 | **Priority:** P1 | **Gap:** GAP-021
**Primary file:** `account/models/account_reconcile_model.py` (203 lines)
**Date:** 2026-10-02

---

## ARCHITECTURAL FINDING — ODOO 19 BREAKING CHANGE

The legacy rule engine (rule_type: writeoff_button / writeoff_suggestion / invoice_matching, match_nature, `_apply_rules`, `_get_write_off_move_lines`, `_apply_rules_to_entry`) present in Odoo 14–17 has been **completely removed** from Odoo 19 Community. The model is a simplified counterpart-entry preset system. No Python rule engine exists in Community. **GAP-021 is PARTIAL: the data model exists but the Python rule-engine methods require custom extension.**

---

## L1–L12 APPLICABILITY

| Layer | Status | Notes |
|-------|--------|-------|
| L1 | YES | Registered in `account/__manifest__.py:43`, `account/models/__init__.py:12` |
| L2 | YES | Two ORM models: `account.reconcile.model` (94–203) and `account.reconcile.model.line` (8–92) |
| L3 | YES | trigger Selection(manual/auto_reconcile) at line 110; `action_set_auto_reconcile` at line 175 |
| L4 | YES | analytic.mixin inheritance; Many2many to account.tax; reconcile_model_id FK on account.move.line |
| L5 | YES | `account_reconcile_model_views.xml` full form/list/search; journal dashboard link |
| L6 | YES | ir.model.access.csv lines 91–96; two ir.rule records with `parent_of` domain |
| L7 | YES | chart_template creates default models (internal_transfer_reco, bank_fees_reco) |
| L8 | NO | No locked/secured logic |
| L9 | PARTIAL | account.reconcile.model.line.account_id defines DR/CR target; no Python posting logic in Community |
| L10 | NO | No cron for auto-reconcile; service_cron.xml has only auto-post and auto-send |
| L11 | NO | No dedicated RPC/controller; access via standard ORM |
| L12 | AWT | auto_reconcile trigger mechanics are handled by front-end JS; no Python `_apply_rules` |

---

## VDR CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U136-C01 | MODEL-HEADER | account/models/account_reconcile_model.py:94–99 | `class AccountReconcileModel` | C1 | Always | C1 | `account.reconcile.model` declares `_inherit = ['mail.thread']`, `_order = 'sequence, id'`, `_check_company_auto = True` | The reconciliation preset header model inherits the mail thread mixin, orders by sequence then by record identifier, and enforces company consistency automatically |
| U136-C02 | MODEL-LINE | account/models/account_reconcile_model.py:8–13 | `class AccountReconcileModelLine` | C1 | Always | C1 | `account.reconcile.model.line` declares `_inherit = ['analytic.mixin']`, `_order = 'sequence, id'`, `_check_company_auto = True` | The counterpart line sub-model inherits the analytic distribution mixin, orders by sequence then identifier, and enforces company consistency |
| U136-C03 | TRIGGER-FIELD | account/models/account_reconcile_model.py:110–111 | `trigger = fields.Selection(...)` | C1 | Always | C1 | `trigger` Selection field values are `('manual', 'Manual')` and `('auto_reconcile', 'Automated')`, default `'manual'`, with tracking enabled | The trigger field controls automation mode; manual requires user action while automated signals the client to apply the preset without prompting |
| U136-C04 | ACTION-AUTO | account/models/account_reconcile_model.py:175–176 | `def action_set_auto_reconcile` | C1 | Always | C1 | `action_set_auto_reconcile` sets `self.trigger = 'auto_reconcile'`; mirror `action_set_manual` sets `self.trigger = 'manual'` at line 172–173 | Two button-bound methods toggle the automation flag between manual and automated states |
| U136-C05 | MATCH-LABEL | account/models/account_reconcile_model.py:138–146 | `match_label = fields.Selection(...)` | C1 | Always | C1 | `match_label` Selection values: `('contains', 'Contains')`, `('not_contains', 'Not Contains')`, `('match_regex', 'Match Regex')`; paired with `match_label_param` Char at line 146 | Three label-matching modes exist: substring containment, negated containment, and full regular expression matching against statement line label, transaction details, or note |
| U136-C06 | REGEX-VALIDATE | account/models/account_reconcile_model.py:152–159 | `_check_match_label_param` | C1 | match_label=='match_regex' | C1 | `@api.constrains('match_label','match_label_param')` calls `re.compile(record.match_label_param)` and raises `UserError` if `re.error` | Regex validity for the label parameter is enforced at save time via a constrains decorator; invalid patterns raise a user-facing error |
| U136-C07 | MATCH-AMOUNT | account/models/account_reconcile_model.py:130–137 | `match_amount = fields.Selection(...)` | C1 | Always | C1 | `match_amount` Selection: `('lower','Is lower than or equal to')`, `('greater','Is greater than or equal to')`, `('between','Is between')`; bounds in `match_amount_min` and `match_amount_max` Float fields | Amount matching uses three comparison modes; the between mode requires both a minimum and maximum bound |
| U136-C08 | MATCH-PARTNER | account/models/account_reconcile_model.py:147–148 | `match_partner_ids` | C1 | Always | C1 | `match_partner_ids = fields.Many2many('res.partner')` restricts model to specified partners; empty means all partners | Partner filtering uses a Many2many relation; when empty the model applies to transactions from any partner |
| U136-C09 | MATCH-JOURNAL | account/models/account_reconcile_model.py:126–129 | `match_journal_ids` | C1 | Always | C1 | `match_journal_ids = fields.Many2many('account.journal')` with domain `[('type', 'in', ('bank', 'cash', 'credit'))]`; empty means all bank/cash/credit journals | Journal scope restriction limits model availability to selected bank, cash, or credit journals; empty selection means all such journals |
| U136-C10 | CAN-BE-PROPOSED | account/models/account_reconcile_model.py:161–164 | `_compute_can_be_proposed` | C1 | Always | C1 | `can_be_proposed = True` when NOT `mapped_partner_id` AND (`match_label` OR `match_amount` OR `match_partner_ids` OR `trigger == 'auto_reconcile'`) | The computed boolean flag gates whether the frontend should surface this model as a suggestion; pure partner-mapping models are excluded from proposal logic |
| U136-C11 | PARTNER-MAPPING | account/models/account_reconcile_model.py:166–170 | `_compute_partner_mapping` | C1 | Always | C1 | `mapped_partner_id` is set when `match_label` is set AND exactly one `line_ids` exists AND that line has `partner_id` AND no `account_id`; used for partner-lookup-only models | A special partner-mapping mode exists: a single-line model with a partner but no account acts as a label-to-partner resolver rather than a counterpart entry generator |
| U136-C12 | LINE-AMOUNT-TYPE | account/models/account_reconcile_model.py:25–34 | `amount_type = fields.Selection(...)` | C1 | Always | C1 | `amount_type` Selection on `account.reconcile.model.line`: `('fixed','Fixed')`, `('percentage','Percentage of balance')`, `('percentage_st_line','Percentage of statement line')`, `('regex','From label')` | Four amount computation methods exist for counterpart lines: absolute fixed amount, percentage of outstanding balance, percentage of statement line amount, or regex-extracted amount from the label |
| U136-C13 | LINE-REGEX-AMOUNT | account/models/account_reconcile_model.py:41–51 | `amount_string` help text | C1 | amount_type=='regex' | C1 | When `amount_type='regex'` the `amount_string` contains a raw regex with a capturing group; the system extracts the amount from the statement label using that pattern; multi-group capture supports integer+decimal split | Regex-based amount extraction uses a capturing group pattern directly on the statement label text; two-group patterns support split integer and decimal extraction |
| U136-C14 | LINE-AMOUNT-FLOAT | account/models/account_reconcile_model.py:36,70–76 | `_compute_float_amount` | C1 | Always | C1 | `amount = Float(compute='_compute_float_amount', store=True)` converts `amount_string` via `float()` and silently sets to 0 on `ValueError` | The float amount is a stored computed shortcut derived from the string representation; non-numeric strings silently yield zero without raising |
| U136-C15 | LINE-AMOUNT-VALIDATE | account/models/account_reconcile_model.py:78–91 | `_validate_amount` | C1 | Always | C1 | `@api.constrains('amount_string')` raises `UserError` if: fixed amount is 0, percentage_st_line is 0, percentage is 0, or regex fails `re.compile()` | Amount constraints prevent zero fixed/percentage values and invalid regex patterns; validation fires on every write to the amount string field |
| U136-C16 | LINE-TAX | account/models/account_reconcile_model.py:52–60 | `tax_ids = fields.Many2many(...)` | C1 | Always | C1 | `tax_ids` Many2many to `account.tax` via relation table `account_reconcile_model_line_account_tax_rel`; `ondelete='restrict'` prevents tax deletion when referenced | Tax applicability is supported on counterpart lines; the restrict delete policy protects referential integrity between tax records and reconcile model lines |
| U136-C17 | LINE-ANALYTIC | account/models/account_reconcile_model.py:10 | `_inherit = ['analytic.mixin']` | C1 | group_analytic_accounting | C1 | `account.reconcile.model.line` inherits `analytic.mixin` which adds `analytic_distribution` JSON field; view at account_reconcile_model_views.xml:106–108 shows the widget with `business_domain: 'general'` | Analytic distribution is natively supported on counterpart lines through mixin inheritance; the distribution widget uses the general business domain |
| U136-C18 | AML-FK | account/models/account_move_line.py:162–168 | `reconcile_model_id` | C1 | Always | C1 | `account.move.line` has `reconcile_model_id = fields.Many2one('account.reconcile.model', copy=False, readonly=True, check_company=True)` | Journal item lines store a reference to the reconciliation model that generated them; this field is read-only and not copied on duplication |
| U136-C19 | NO-CRON | account/data/service_cron.xml:1–22 | cron records | C1 | Always | C1,GAP | `service_cron.xml` contains only `ir_cron_auto_post_draft_entry` and `ir_cron_account_move_send`; no cron for `account.reconcile.model`; no `_apply_rules` Python method in Community | There is no scheduled job that automatically applies reconciliation models to unreconciled statement lines in Community; the auto_reconcile trigger is a client-side signal only |
| U136-C20 | LEGACY-REMOVED | account/models/account_reconcile_model.py:1–203 (entire file) | entire file | C1 | Always | C1,GAP | Fields `rule_type`, `match_nature`, `match_same_currency`, `match_total_amount`, `match_total_amount_param` and methods `_apply_rules`, `_get_write_off_move_lines`, `_apply_rules_to_entry` are absent from the file; the file is only 203 lines | The Odoo 14–17 Python rule engine has been entirely removed from Odoo 19 Community; GAP-021 requires custom Python extension to restore server-side rule application |
| U136-C21 | ACCESS-RULES | account/security/account_security.xml:206–216 | ir.rule records | C1 | Always | C1 | Two ir.rule records use `domain_force=[('company_id','parent_of',company_ids)]` for both `account.reconcile.model` and `account.reconcile.model.line`; `parent_of` allows parent companies to read child company models | Multi-company record rules use the `parent_of` operator enabling parent companies to view reconciliation models belonging to their subsidiary companies |
| U136-C22 | ACL | account/security/ir.model.access.csv:91–96 | access lines | C1 | Always | C1 | group_account_readonly: read-only; group_account_invoice: read+write (no delete); group_account_basic: full CRUD on both models | Three access tiers govern reconcile model permissions; the billing group can create/update models but cannot delete them |
| U136-C23 | CHART-TEMPLATE | account/models/chart_template.py:1195–1220 | `_get_account_reconcile_model` | C1 | Always | C1 | `@template(model='account.reconcile.model')` creates two defaults: `internal_transfer_reco` (no conditions, 100% line) and `bank_fees_reco` (match_label=contains 'Bank Fees', 100% line) | Chart template installation creates two default models automatically: one for internal transfers with no conditions and one for bank fees with a label containment filter |
| U136-C24 | SEQUENCE-ORDER | account/models/account_reconcile_model.py:104,98 | `sequence`, `_order` | C1 | Always | C1 | `AccountReconcileModel._order = 'sequence, id'`; `sequence = fields.Integer(required=True, default=10)` | Models are applied in ascending sequence order when multiple models match a statement line; the `id` serves as tiebreaker within the same sequence value |
| U136-C25 | TRIGGER-AWT | account/views/account_reconcile_model_views.xml:29–36 | button declarations | C1,AWT | trigger=='auto_reconcile' | AWT | Two header buttons toggle trigger state; the `auto_reconcile` state is flagged to the JS front-end which is responsible for automatic application; no Python back-end enforcement of auto-application | The automated trigger flag is stored in the database and surfaced to the client but the matching and auto-application logic is absent from Community Python — it is an AWT boundary |

---

## GAP-021 FINDING

**GAP-021 Status: PARTIAL CLOSED**

The `account.reconcile.model` data model exists in full in Odoo 19 Community with matching conditions (label, amount, partner, journal) and counterpart line definitions (account, amount_type, taxes, analytic). However, the **Python server-side rule engine** (`_apply_rules`, `_get_write_off_move_lines`, `_apply_rules_to_entry`, `rule_type`, `match_nature`, `match_same_currency`, `match_total_amount_param`) present in Odoo 14–17 has been entirely removed. The `auto_reconcile` trigger is a UI/client-side flag with no back-end Python enforcement. Custom Python extension is required to restore server-side rule application for GAP-021.

---

## L9 ACCOUNTING POSTINGS

The `account.reconcile.model.line` record defines the counterpart account for a writeoff entry via `account_id`. When a user applies the model during bank reconciliation, the system creates an `account.move` with:
- **DR**: Statement line amount to bank account (liquidity line, via `_prepare_move_line_default_vals`)
- **CR**: Target account from `account.reconcile.model.line.account_id` (counterpart/writeoff)
- Taxes applied from `tax_ids` generate additional tax lines
- Analytic distribution from `analytic_distribution` is propagated to the counterpart line
- The resulting journal item receives `reconcile_model_id` pointing back to this model

No explicit `_create_writeoff` or `_get_write_off_move_lines` Python method exists in Community; posting is handled by the JS layer calling standard `account.bank.statement.line` reconciliation methods.
