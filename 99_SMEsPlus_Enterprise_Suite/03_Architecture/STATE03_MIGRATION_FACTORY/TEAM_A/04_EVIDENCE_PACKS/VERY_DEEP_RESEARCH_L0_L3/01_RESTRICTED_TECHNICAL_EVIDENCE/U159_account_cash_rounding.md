# U159 — account_cash_rounding: Invoice Cash Rounding L3 (Thai-Relevant)

**Unit:** U159 | **Group:** G01/G02 | **Priority:** P1 (TH)
**Research date:** 2026-10-02
**Source base:** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/`
**Status:** GATE-PASS — 20 claims

---

## Presence Check

`account_cash_rounding` is NOT a standalone module under `addons/`. The model and all logic are built into the `account` module:
- Model: `addons/account/models/account_cash_rounding.py`
- Integration: `addons/account/models/account_move.py`
- Line model: `addons/account/models/account_move_line.py`
- Payment term integration: `addons/account/models/account_payment_term.py`
- Tax totals display: `addons/account/models/account_tax.py`
- Settings toggle: `addons/account/models/res_config_settings.py`
- Security group: `addons/account/security/account_security.xml`

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U159-C01 | ACR-MODEL-FIELDS | `account/models/account_cash_rounding.py:15–43` | `_name = 'account.cash.rounding'` | C1 | Always | — | The `account.cash.rounding` model defines: `rounding` (Float, precision step, default 0.01), `strategy` (Selection: `add_invoice_line` or `biggest_tax`), `rounding_method` (Selection: UP/DOWN/HALF-UP, default HALF-UP), `profit_account_id` (Many2one account.account, company_dependent), `loss_account_id` (Many2one account.account, company_dependent) | Cash rounding configuration model holding precision step, strategy choice, rounding direction, and two company-dependent posting accounts |
| U159-C02 | ACR-VALIDATE-ROUNDING | `account/models/account_cash_rounding.py:45–49` | `@api.constrains('rounding')` | C1 | Always | — | `validate_rounding()` raises `ValidationError` if `rounding <= 0`, enforcing a strictly positive precision step | Constraint rejecting zero or negative rounding precision at save time |
| U159-C03 | ACR-ROUND-METHOD | `account/models/account_cash_rounding.py:51–57` | `def round(self, amount)` | C1 | Always | — | `round()` delegates to `float_round(amount, precision_rounding=self.rounding, rounding_method=self.rounding_method)` — supports UP, DOWN, HALF-UP tie-breaking | Precision rounding helper respecting the configured tie-breaking rule |
| U159-C04 | ACR-COMPUTE-DIFF | `account/models/account_cash_rounding.py:59–69` | `def compute_difference(self, currency, amount)` | C1 | Always | — | `compute_difference()` first applies `currency.round(amount)`, then computes `self.round(amount) - amount`, then applies `currency.round(difference)` — returns the delta needed to reach the rounded target | Two-step difference computation: currency rounding then cash rounding, result re-rounded to currency precision |
| U159-C05 | ACR-M2O-ON-MOVE | `account/models/account_move.py:717–721` | `invoice_cash_rounding_id = fields.Many2one(...)` | C1 | Always | — | `invoice_cash_rounding_id` is a Many2one to `account.cash.rounding` on `account.move`, gated in the form view by `account.group_cash_rounding` | Invoice-level pointer to the selected cash rounding configuration |
| U159-C06 | ACR-SETTINGS-TOGGLE | `account/models/res_config_settings.py:80` | `group_cash_rounding = fields.Boolean(...)` | C1 | Always | — | `group_cash_rounding` Boolean in `res.config.settings` with `implied_group='account.group_cash_rounding'` — the feature is opt-in at the company level | Company-level toggle that activates the cash rounding feature via a security group |
| U159-C07 | ACR-SECURITY-GROUP | `account/security/account_security.xml:86–88` | `<record id="group_cash_rounding" ...>` | C1 | Always | — | Security group named "Allow the cash rounding management" gates the `invoice_cash_rounding_id` field on the invoice form | Opt-in access group that must be enabled before the field appears on invoices |
| U159-C08 | ACR-FORM-VIEW-GATE | `account/views/account_move_views.xml:1555` | `<field name="invoice_cash_rounding_id" groups="account.group_cash_rounding" readonly="state != 'draft'"/>` | C1 | Always | — | The `invoice_cash_rounding_id` field is visible only when `account.group_cash_rounding` is active, and is read-only once the invoice leaves draft state | Form-view gating: feature must be enabled and invoice must be in draft for the field to be editable |
| U159-C09 | ACR-ONCHANGE-WARNING | `account/models/account_move.py:2768–2775` | `@api.onchange('invoice_cash_rounding_id')` | C1 | strategy = add_invoice_line AND profit_account missing | — | `_onchange_invoice_cash_rounding_id()` returns a warning dict if strategy is `add_invoice_line` and no `profit_account_id` is set — warning title references the rounding method name | UI-level warning raised when an invoice-line strategy is chosen without configuring a profit account |
| U159-C10 | ACR-RECOMPUTE-ROUNDING | `account/models/account_move.py:3076–3195` | `def _recompute_cash_rounding_lines(self)` | C1 | invoice_cash_rounding_id set | — | `_recompute_cash_rounding_lines()` is the main orchestrator: computes the rounding difference via nested `_compute_cash_rounding()`, removes the rounding line if already balanced, detects strategy changes, then calls nested `_apply_cash_rounding()` to create or update the line | Main method that reconciles the existing rounding journal line with the current invoice total on every relevant save |
| U159-C11 | ACR-COMPUTE-INNER | `account/models/account_move.py:3090–3102` | `def _compute_cash_rounding(self, total_amount_currency)` | C1 | currency == company currency | — | Inner `_compute_cash_rounding()` calls `compute_difference(currency, total_amount_currency)` for the foreign-currency delta; when invoice currency equals company currency, `diff_balance = diff_amount_currency`; otherwise the balance is converted via `currency_id._convert()` using invoice date or entry date | Dual-currency difference computation: passes through when currencies match, converts when they differ |
| U159-C12 | ACR-APPLY-BIGGEST-TAX | `account/models/account_move.py:3123–3139` | `if self.invoice_cash_rounding_id.strategy == 'biggest_tax':` | C1 | strategy = biggest_tax | — | When strategy is `biggest_tax`, iterates `self.line_ids.filtered('tax_repartition_line_id')` and selects the line with the highest `abs(balance)`; the rounding line is created/updated with that tax line's `account_id`, `tax_repartition_line_id`, `tax_tag_ids`, and `tax_ids` — effectively adjusting the largest tax bucket | Biggest-tax strategy posts the rounding delta into the largest existing tax line's account, reusing its tax attributes |
| U159-C13 | ACR-APPLY-ADD-LINE | `account/models/account_move.py:3141–3152` | `elif self.invoice_cash_rounding_id.strategy == 'add_invoice_line':` | C1 | strategy = add_invoice_line | — | When strategy is `add_invoice_line`, selects `loss_account_id` if `diff_balance > 0` (invoice rounds up, company loses value) or `profit_account_id` otherwise; creates a new line with `display_type='rounding'` and no tax_ids | Add-line strategy posts to profit or loss account depending on rounding direction |
| U159-C14 | ACR-LINE-CREATE-UPDATE | `account/models/account_move.py:3154–3158` | `if cash_rounding_line: cash_rounding_line.write(...)` | C1 | Always | — | The rounding line is updated via `write()` if it already exists, otherwise created via `env['account.move.line'].create()`; the line always carries `display_type='rounding'` | Idempotent create-or-update pattern for the rounding journal line |
| U159-C15 | ACR-DISPLAY-TYPE | `account/models/account_move_line.py:339` | `('rounding', "Rounding")` | C1 | Always | — | `display_type` field on `account.move.line` includes `'rounding'` as a named selection value, giving the rounding line its own distinct classification | Dedicated display type for cash rounding lines, distinct from product, tax, and payment-term lines |
| U159-C16 | ACR-SEQUENCE | `account/models/account_move_line.py:909` | `'rounding': 11000` | C1 | Always | — | `_compute_sequence()` assigns sequence 11000 to rounding lines, placing them after tax lines (10000) and before payment-term lines (12000) in invoice line ordering | Rounding line appears at sequence 11000, sandwiched between tax lines and payment term lines |
| U159-C17 | ACR-AMOUNT-TOTAL-IMPACT | `account/models/account_move.py:1199–1210` | `_compute_amount()` | C1 | Always | — | In `_compute_amount()`, a rounding line with `tax_repartition_line_id` is added to `total_tax`; a rounding line without it (add_invoice_line strategy) is added to `total_untaxed`; both contribute to `total` — so `amount_total` always includes the rounding difference | Cash rounding delta flows into amount_total in all cases; strategy determines whether it inflates tax or untaxed subtotal |
| U159-C18 | ACR-PAYMENT-TERM-INTEGRATION | `account/models/account_payment_term.py:171,242–249` | `def _compute_terms(self, ..., cash_rounding=None)` | C1 | cash_rounding set | — | `_compute_terms()` accepts `cash_rounding`; for non-balance payment term lines, calls `compute_difference()` on the line's foreign amount and adjusts the term amount — ensuring each payment installment is itself cash-rounded | Cash rounding is propagated to payment term lines so instalments also align to the rounding precision |
| U159-C19 | ACR-FISCAL-POSITION-ABSENT | `account/models/account_cash_rounding.py` (full file) | (no fiscal_position field or reference) | ABSENT | — | GAP | No linkage between `account.cash.rounding` and `account.fiscal.position` — rounding account selection is solely via `profit_account_id`/`loss_account_id` (company-dependent) and biggest-tax account; fiscal position does not remap the rounding account | Fiscal position has no effect on which account receives the cash rounding posting |
| U159-C20 | ACR-THB-WHOLE-BAHT | `account/models/account_cash_rounding.py:20–21,45–49` | `rounding = fields.Float(...)` | C1 | rounding = 1.00 | C1 | The `rounding` field is a plain Float with no upper bound; setting `rounding = 1.00` makes the engine round invoices to the nearest whole unit (1 THB); `validate_rounding()` only rejects values <= 0 — so whole-baht rounding is fully supported through configuration | Whole-baht rounding for Thai invoices is achievable by setting the precision step to 1.00 in the cash rounding record |

---

## Supporting Evidence

### account.cash.rounding model — full field inventory
File: `account/models/account_cash_rounding.py:8–69`
- `_name = 'account.cash.rounding'`
- `_check_company_auto = True`
- `name` (Char, translate=True, required)
- `rounding` (Float, default 0.01, help: "smallest coinage")
- `strategy` (Selection: biggest_tax | add_invoice_line)
- `profit_account_id` (Many2one account.account, company_dependent, check_company, domain excludes receivable/payable)
- `loss_account_id` (Many2one account.account, company_dependent, check_company, domain excludes receivable/payable)
- `rounding_method` (Selection: UP/DOWN/HALF-UP, default HALF-UP)

### _recompute_cash_rounding_lines logic flow
File: `account/models/account_move.py:3076–3195`
1. If no `invoice_cash_rounding_id` → unlink existing rounding line, return
2. If strategy changed (detected by presence/absence of `tax_line_id`) → unlink old line, start fresh
3. Sum `amount_currency` of all non-receivable/payable lines (excluding the rounding line itself)
4. Call `_compute_cash_rounding()` → get `diff_balance`, `diff_amount_currency`
5. If both are zero → unlink existing line, return (already rounded)
6. If existing line already has correct amounts → skip (no-op)
7. Call `_apply_cash_rounding()` → create or update the line

### Strategy branching in _apply_cash_rounding
File: `account/models/account_move.py:3112–3158`
- Base `rounding_line_vals`: balance, amount_currency, partner_id, move_id, currency_id, company_id, display_type='rounding'
- `biggest_tax`: add tax_repartition_line_id, account_id, tax_tag_ids, tax_ids from the biggest-balance tax line
- `add_invoice_line`: add account_id from profit/loss; `tax_ids = Command.clear()`

### _sync_rounding_lines context manager
File: `account/models/account_move.py:3248–3252`
```
@contextmanager
def _sync_rounding_lines(self, container):
    yield
    for invoice in container['records']:
        if invoice.state != 'posted':
            invoice._recompute_cash_rounding_lines()
```
Cash rounding lines are re-synchronized only while the invoice is in draft (not after posting).

### _compute_amount classification of rounding lines
File: `account/models/account_move.py:1199–1210`
- Line 1199: rounding line WITH `tax_repartition_line_id` → counted as tax
- Line 1205: rounding line WITHOUT `tax_repartition_line_id` → counted as untaxed
- Both paths add to `total` → `amount_total` always reflects rounded value

### Tax totals summary (widget) integration
File: `account/models/account_tax.py:2727,2909–2931`
- `_get_tax_totals_summary(cash_rounding=None)` parameter allows the widget to show the rounding delta
- Lines with `special_type='cash_rounding'` extracted at line 2909 to populate `cash_rounding_base_amount_currency`

---

## Thai Billing Relevance

1. **Whole-baht rounding**: Configure `account.cash.rounding.rounding = 1.00` — the engine supports any positive float. No code change needed.
2. **Strategy choice for TH**: `add_invoice_line` creates a visible line on the Thai tax invoice, satisfying RD documentation requirements. `biggest_tax` silently adjusts VAT; may be acceptable for internal purposes but less transparent for Thai tax invoices.
3. **Profit/loss accounts**: Must be mapped per Thai chart of accounts. `profit_account_id` for rounding-down scenarios (company gains), `loss_account_id` for rounding-up (company pays more).
4. **No fiscal position remap**: Cannot reroute rounding to a different account via fiscal position — must configure the accounts directly on the `account.cash.rounding` record.
5. **Payment alignment**: Payment term lines will also be cash-rounded (`account_payment_term.py:242–249`), keeping receivables/payables consistent with the invoice total.
6. **Feature gate**: Requires enabling "Cash Rounding" in Accounting → Settings before the field appears on invoices.
