# U189 — account.payment: Core Payment Model, State Machine, Journal Entry, Reconciliation Chain
**Unit:** U189 | **Group:** G03 | **Priority:** P1 | **Status:** STUDIED
**Source file:** `account/models/account_payment.py` (1 250 lines)
**Secondary:** `account/models/account_move.py` (PAYMENT_STATE_SELECTION, `_compute_payment_state`, `_get_invoice_in_payment_state`)
**Odoo version:** 19.0.post20260921 Community

---

## 1. Model Identity

```
_name  = 'account.payment'
_inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
_order = "date desc, name desc"
_check_company_auto = True
```

Constraints:
- `_check_amount_not_negative`: `CHECK(amount >= 0.0)`
- `_journal_id_company_id_idx`: index on `(journal_id, company_id)`
- `_unmatched_idx`: partial index `(journal_id, company_id) WHERE is_matched IS NOT TRUE`

---

## 2. Core Business Fields

| Field | Type | Notes |
|---|---|---|
| `payment_type` | Selection | `inbound` (Receive) / `outbound` (Send); default `inbound` |
| `partner_type` | Selection | `customer` / `supplier`; default `customer` |
| `state` | Selection (computed, stored) | `draft` / `in_process` / `paid` / `canceled` / `rejected` |
| `amount` | Monetary | currency_field=`currency_id`; constraint >= 0 |
| `currency_id` | Many2one | Computed from `journal_id.currency_id` or company currency |
| `company_currency_id` | Many2one | Related to `company_id.currency_id` |
| `outstanding_account_id` | Many2one `account.account` | Transit/clearing account; computed, stored |
| `destination_account_id` | Many2one `account.account` | Receivable or payable; computed, stored |
| `memo` | Char | Inversed → `move_id.ref` |
| `move_id` | Many2one `account.move` | The journal entry; `copy=False` |
| `partner_id` | Many2one `res.partner` | |
| `journal_id` | Many2one `account.journal` | Bank/cash/credit journals only |
| `date` | Date | Default `context_today` |
| `is_reconciled` | Boolean | Computed, stored — counterpart/writeoff lines fully reconciled |
| `is_matched` | Boolean | Computed, stored — liquidity line residual is zero |

---

## 3. State Machine (v19 Community)

```
draft  ──action_post()──▶  in_process  ──auto via _compute_state()──▶  paid
  │                            │
  │                        action_cancel()
  │                            │
  └──────────────────────▶  canceled
                           rejected  (action_reject)
```

**In Odoo 19 the state machine lives on `account.payment` itself**, not delegated to `account.move.state`. The `state` field is Selection + computed + stored + `readonly=False`.

`_compute_state()` (line 455):
1. If `state` is falsy → set `draft`.
2. If `move_id` exists and state is `in_process` or `paid`: checks whether the sum of `amount_residual` on liquidity lines is zero (or the liquidity account has no reconcile flag) → sets `paid`, else `in_process`.
3. If `in_process` and all reconciled invoices/bills have `payment_state == 'paid'` → sets `paid`.

**action_post()** (line 1130):
```python
def action_post(self):
    # Guard: outbound payment method needing bank account must be validated
    for payment in self:
        if (payment.require_partner_bank_account
                and not payment.partner_bank_id.allow_out_payment
                and payment.payment_type == 'outbound'):
            raise UserError(...)
    # Payments whose outstanding account is asset_cash go directly to paid
    self.filtered(lambda pay: pay.outstanding_account_id.account_type == 'asset_cash').state = 'paid'
    # Everything else → in_process
    self.filtered(lambda pay: pay.state in {False, 'draft', 'in_process'}).state = 'in_process'
```
Setting `state` to `in_process`/`paid` triggers `write()` override (line 951), which creates and posts the journal entry.

**write() override** (line 951):
```python
def write(self, vals):
    if vals.get('state') in ('in_process', 'paid') and not vals.get('move_id'):
        self.filtered(lambda p: not p.move_id)._generate_journal_entry()
        self.move_id.filtered(lambda m: m.state == 'draft').action_post()
    res = super().write(vals)
    if self.move_id:
        self._synchronize_to_moves(set(vals.keys()))
    return res
```

**action_cancel()** (line 1156):
```python
def action_cancel(self):
    self.state = 'canceled'
    draft_moves = self.move_id.filtered(lambda m: m.state == 'draft')
    draft_moves.unlink()
    (self.move_id - draft_moves).button_cancel()
```
Draft moves are deleted; posted moves are cancelled via `button_cancel()` (which in v19 creates a cancellation/reversal entry).

---

## 4. outstanding_account_id — Clearing Account

**Compute** (line 624):
```python
@api.depends('payment_method_line_id')
def _compute_outstanding_account_id(self):
    for pay in self:
        pay.outstanding_account_id = pay.payment_method_line_id.payment_account_id
```
The clearing account is taken from `account.payment.method.line.payment_account_id` which is typically "Outstanding Receipts" (inbound) or "Outstanding Payments" (outbound).

**Community fallback** (line 940): If `accounting` is not installed (Community without `account_accountant` module), `_get_outstanding_account()` resolves `account_journal_payment_debit_account_id` / `account_journal_payment_credit_account_id` via chart template, falling back to `company_id.transfer_account_id`.

**Guard** (line 324): If `outstanding_account_id` is falsy when building journal lines → `UserError`.

---

## 5. Journal Entry Line Construction

### 5.1 `_prepare_move_lines_per_type()` (line 312)

Returns dict with keys `liquidity_lines`, `counterpart_lines`, `write_off_lines`, `withholding_lines`.

**Liquidity amount** (line 350):
```python
if self.payment_type == 'inbound':
    liquidity_amount_currency = self.amount        # positive
elif self.payment_type == 'outbound':
    liquidity_amount_currency = -self.amount       # negative
```

**Balance conversion** (line 363):
```python
liquidity_balance = self.currency_id._convert(
    liquidity_amount_currency,
    self.company_id.currency_id,
    self.company_id,
    self.date,
)
```

**Counterpart** (line 379):
```python
counterpart_amount_currency = -liquidity_amount_currency - write_off_amount_currency - withholding_amount_currency
counterpart_balance = -liquidity_balance - write_off_balance - withholding_balance
```

### 5.2 `_prepare_move_liquidity_lines()` (line 288)
Account → `outstanding_account_id`; carries date_maturity, partner_id, currency_id, balance, amount_currency.

### 5.3 `_prepare_move_counterpart_lines()` (line 300)
Account → `destination_account_id` (receivable/payable); same structure.

### 5.4 `destination_account_id` (line 629)
```python
if pay.partner_type == 'customer':
    → partner.property_account_receivable_id  (account_type = asset_receivable)
elif pay.partner_type == 'supplier':
    → partner.property_account_payable_id     (account_type = liability_payable)
```
Falls back to a company-level search if no partner.

### 5.5 `_generate_move_vals()` (line 1085)
Creates `account.move` with `move_type='entry'`, `origin_payment_id=self.id`, plus all line vals from `_prepare_move_line_default_vals()`.

---

## 6. Multi-Currency Handling

- `currency_id`: computed from `journal_id.currency_id or journal_id.company_id.currency_id` (line 621).
- `company_currency_id`: related to `company_id.currency_id` (line 115).
- FX conversion: `currency_id._convert(amount_currency, company_currency, company, date)` (line 363).
- `amount_company_currency_signed` (line 531): stored; computed from sum of liquidity line `balance` values when move exists, or via `_convert()` otherwise.
- When `currency_id != company_currency_id`, the journal lines carry both `amount_currency` (in payment currency) and `balance` (in company currency); the difference auto-generates FX gain/loss lines in the accounting engine.

---

## 7. `is_matched` and `is_reconciled` (_compute_reconciliation_status, line 473)

```python
residual_field = 'amount_residual' if pay.currency_id == company.currency_id else 'amount_residual_currency'
# is_matched: liquidity lines residual == 0
if journal.default_account_id in liquidity_lines.account_id:
    pay.is_matched = True   # direct bank account usage — always matched
else:
    pay.is_matched = pay.currency_id.is_zero(sum(liquidity_lines.mapped(residual_field)))
# is_reconciled: counterpart + writeoff lines with reconcile=True all zero
reconcile_lines = (counterpart_lines + writeoff_lines).filtered(lambda l: l.account_id.reconcile)
pay.is_reconciled = pay.currency_id.is_zero(sum(reconcile_lines.mapped(residual_field)))
```

---

## 8. Reconciliation — link payment → invoice

**`_compute_stat_buttons_from_reconciliation()`** (line 680): Raw SQL via `account.partial.reconcile`; finds invoice moves (out_invoice, out_refund, in_invoice, in_refund, out_receipt, in_receipt) whose `account.move.line` (receivable/payable) is reconciled against a line from the payment's move. Result stored in `reconciled_invoice_ids`, `reconciled_bill_ids`, `reconciled_statement_line_ids`.

**`_search_reconciled_invoice_ids()`** (line 787): Reverse search — given invoice ids, finds payments via `account.move.reconciled_payment_ids`.

**`invoice_ids`** Many2many `account_move__account_payment` relation (line 140): Contains the invoice even before reconciliation is done.

---

## 9. Community vs Enterprise Distinction

### `_get_invoice_in_payment_state()` (account_move.py line 7367):
```python
def _get_invoice_in_payment_state(self):
    return 'paid'   # Community: no 'in_payment' shown
```
Enterprise (`account_accountant`) overrides this to return `'in_payment'`.

### `_valid_payment_states()` (account_payment.py line 255):
```python
def _valid_payment_states(self):
    return ['in_process', 'paid'] if self.env['account.move']._get_invoice_in_payment_state() == 'paid' else ['in_process']
```
Community returns `['in_process', 'paid']` because `_get_invoice_in_payment_state()` == `'paid'`.

### Community journal entry creation (line 912):
```python
accounting_installed = self.env['account.move']._get_invoice_in_payment_state() == 'in_payment'
if (not accounting_installed and not pay.outstanding_account_id) or context.get('force_payment_move'):
    outstanding_account = pay._get_outstanding_account(pay.payment_type)
    pay.outstanding_account_id = outstanding_account.id
```
In Community (`accounting_installed=False`), if `outstanding_account_id` is not set, one is automatically resolved from the chart template.

---

## 10. Payment State on Invoices (`payment_state` on account.move)

**PAYMENT_STATE_SELECTION** (account_move.py line 49):
```
not_paid | in_payment | paid | partial | reversed | blocked | invoicing_legacy
```

**`_compute_payment_state()`** (account_move.py line 1234): SQL-driven. Logic:
1. Group moves: `legacy` (keep `invoicing_legacy`), `blocked` (keep), `invoices` (is_invoice + posted or non-zero draft), `unpaid` → `not_paid`.
2. For invoices: join `account.partial.reconcile` → counterpart lines → `account.move`s, check `pay.is_matched`.
3. If `amount_residual == 0`:
   - has payment/statement → if `all_payments_matched` → `paid` else `_get_invoice_in_payment_state()` (Community: `paid`)
   - reversed by credit note → `reversed`
4. If residual != 0 but partial reconciliation exists → `partial`.
5. Unreconciled in_process/paid payments (no move) → `_get_invoice_in_payment_state()`.

---

## 11. `_synchronize_to_moves()` (line 999)

Keeps draft `account.move` in sync with `account.payment`. Trigger fields (line 1067):
```
date, amount, payment_type, partner_type, payment_reference,
currency_id, partner_id, destination_account_id, partner_bank_id, journal_id
```
Does NOT synchronize posted moves (`if pay.move_id.state == 'posted': continue`).

---

## 12. Duplicate Payment Detection

`_fetch_duplicate_reference()` (line 793): SQL query matching same partner_id, company_id, date, payment_type, amount in states `('draft', 'in_process')`.

---

## Source File Evidence

All claims sourced from:
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account/models/account_payment.py`
- `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account/models/account_move.py`
