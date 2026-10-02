# U135 — account_payment_interco L3 Deep Study (GAP-002 Extension)

**Unit:** U135 | **Gap:** GAP-002 | **Priority:** P0 | **G Group:** G01
**Researcher:** Claude Sonnet 4.6 | **Date:** 2026-10-02
**Source tree (READ-ONLY):** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account_payment_interco`

---

## L1 — Manifest / Dependencies

**File:** `account_payment_interco/__manifest__.py:1-12`

- **name:** "Intercompany Payment - Account"
- **category:** 'Accounting/Accounting'
- **summary:** "Enable Intercompany payments to reconcile with their invoices on post."
- **version:** '1.0'
- **depends:** `['account_payment']`  — only one dependency; does NOT depend on `account_inter_company_rules` (Enterprise-only)
- **license:** LGPL-3  — Community module
- **data:** `['views/res_config_settings_views.xml']`
- No wizards, no security CSV, no cron data files

**L1 Assessment:** APPLICABLE. Module is Community LGPL-3. Sole dependency is `account_payment` (also Community).

---

## L2 — Models / Fields / ORM

### res_company.py (L2)
**File:** `account_payment_interco/models/res_company.py:1-27`

Three new Many2one fields added to `res.company`:

| Field | Model | Domain | Purpose |
|---|---|---|---|
| `account_interco_clearing_journal_id` | `account.journal` | `type = general` | The general journal for interco clearing entries; `check_company=True` |
| `account_interco_payable_id` | `account.account` | `account_type = liability_payable, reconcile = True` | Interco payable clearing account; must be reconcilable |
| `account_interco_receivable_id` | `account.account` | `account_type = asset_receivable, reconcile = True` | Interco receivable clearing account; must be reconcilable |

### res_config_settings.py (L2)
**File:** `account_payment_interco/models/res_config_settings.py:1-25`

Three `related` fields on `res.config.settings` mirroring the three `res.company` fields above. All `readonly=False`, `check_company=True`. Exposed in Settings UI.

### account_move.py (L2)
**File:** `account_payment_interco/models/account_move.py:1-121`

`account.move` inherits two new methods:
- `_interco_filter_moves(self)` — filter predicate for eligible interco moves (line 7)
- `_check_interco_clearing(self, payments)` — main interco journal creation logic (line 39)

And overrides:
- `_post(self, soft=True)` — calls super then triggers interco clearing if applicable (line 30)

**L2 Assessment:** APPLICABLE. 3 company-level config fields + settings relay + 2 new methods + 1 override.

---

## L3 — Workflow / State Machine

### Trigger: _post override
**File:** `account_payment_interco/models/account_move.py:30-37`

```
def _post(self, soft=True):
    moves = super()._post(soft)
    if interco_moves := moves.sudo()._interco_filter_moves():
        for invoice in interco_moves:
            transactions = invoice.sudo().transaction_ids.filtered(...)
            invoice._check_interco_clearing(transactions.payment_id)
    return moves
```

The trigger fires on `account.move._post()` — i.e., when an **invoice** is confirmed/posted.

### Filter Predicate: _interco_filter_moves
**File:** `account_payment_interco/models/account_move.py:7-28`

An invoice qualifies for interco clearing when ALL of:
1. `m.is_invoice()` — must be an invoice (not a generic journal entry)
2. `m.payment_state in ('not_paid', 'partial', 'in_payment')` — has outstanding balance
3. `m.company_id.account_interco_clearing_journal_id` is set — invoice's company has clearing journal configured
4. `m.transaction_ids.payment_id` — invoice has linked payment transactions with payments
5. `m.company_id not in m.transaction_ids.payment_id.company_id` — payment was made from a **different** company than the invoice company
6. Directional account check:
   - If inbound (sale): invoice company has `account_interco_receivable_id` AND payment company has `account_interco_payable_id`
   - If outbound (purchase): invoice company has `account_interco_payable_id` AND payment company has `account_interco_receivable_id`
7. Payment state filter: transactions linked to payment must be `in_process` or `paid`, from a different company, and that company has `account_interco_clearing_journal_id` set

### Main Logic: _check_interco_clearing
**File:** `account_payment_interco/models/account_move.py:39-121`

**Phase 1 — Clearing entry in PAYMENT company (lines 45-82):**
For each payment:
1. Calls `payment._seek_for_lines()` to extract `counterpart_lines` (the outstanding receivable/payable lines on the payment move)
2. Computes `clearing_balance` = negated sum of counterpart line balances
3. Selects `other_interco_account` from payment company:
   - Sale (is_sale): `payment.company_id.account_interco_payable_id`
   - Purchase: `payment.company_id.account_interco_receivable_id`
4. Creates journal entry `payment_clearing` using `with_company(payment.company_id)`:
   - Line 1: DR/CR `counterpart_account` (original payment outstanding account) — `clearing_balance`
   - Line 2: DR/CR `other_interco_account` — `-clearing_balance`
5. Posts `payment_clearing` with `action_post()`
6. **Reconciles** `counterpart_lines + payment_clearing_line` — clears the payment's outstanding account

**Phase 2 — Settlement entry in INVOICE company (lines 84-120):**
1. Gets `invoice_lines` — the receivable or payable lines on the invoice
2. Selects `self_interco_account`:
   - Sale: `self.company_id.account_interco_receivable_id`
   - Purchase: `self.company_id.account_interco_payable_id`
3. Creates journal entry `entry` using `with_company(self.company_id)`:
   - Line 1: DR/CR `self_interco_account` with partner = payment company's partner
   - Line 2: DR/CR `invoice_line_account` (original AR/AP) with partner = original partner
4. Posts `entry` with `action_post()`
5. **Reconciles** `entry_receivable_line + invoice_lines` — clears the invoice's AR/AP

**L3 Assessment:** APPLICABLE. Two-phase automatic journal creation on invoice post. No wizard — fully automatic. sudo() used to cross company boundaries.

---

## L4 — Cross-Module Call Chain

**File:** `account_payment_interco/models/account_move.py:30-37`

Call chain on invoice post:
1. `account.move._post()` (this module overrides it)
2. → `super()._post()` (account module)
3. → `moves.sudo()._interco_filter_moves()` — sudo needed to read other company's payment data
4. → `invoice.sudo()._check_interco_clearing(payments)` — sudo needed to create moves in other company
5. → `self.env['account.move'].with_company(payment.company_id).create(...)` — creates clearing entry in payment company
6. → `payment_clearing.action_post()` — posts it
7. → `(counterpart_lines + payment_clearing_line).reconcile()` — reconciles payment outstanding
8. → `self.env['account.move'].with_company(self.company_id).create(...)` — creates settlement entry in invoice company
9. → `entry.action_post()` — posts it
10. → `(entry_receivable_line + invoice_lines).reconcile()` — reconciles invoice AR/AP

Also calls `payment._seek_for_lines()` — method from `account_payment` module that returns `(liquidity_lines, counterpart_lines, writeoff_lines)` tuple.

**L4 Assessment:** APPLICABLE. Intra-call chain entirely within `account_payment_interco` + `account` + `account_payment` modules. No calls to Enterprise modules.

---

## L5 — Views / Wizards / Reports

**File:** `account_payment_interco/views/res_config_settings_views.xml:1-52`

- Inherits `account.res_config_settings_view_form`
- Adds an `<xpath>` inside `//block[@id='default_accounts']`
- New setting block `id="interco_clearing"` with `groups="base.group_multi_company"` — only visible when multi-company is active
- Three field widgets: clearing journal, payable account, receivable account
- Payable and receivable fields have `required="account_interco_clearing_journal_id"` — conditional required

No wizards. No reports. No separate form views for interco journal entries.

**L5 Assessment:** APPLICABLE (settings view only). No wizard/report complexity.

---

## L6 — Access / Record Rules / sudo / Company Boundaries

**File:** `account_payment_interco/models/account_move.py:33`

```python
if interco_moves := moves.sudo()._interco_filter_moves():
```

**File:** `account_payment_interco/models/account_move.py:35`

```python
invoice.sudo()._check_interco_clearing(transactions.payment_id)
```

**File:** `account_payment_interco/models/account_move.py:57`

```python
self.env['account.move'].with_company(payment.company_id).create({...})
```

**File:** `account_payment_interco/models/account_move.py:96`

```python
self.env['account.move'].with_company(self.company_id).create({...})
```

- `sudo()` is used at both the filter and the clearing logic — to bypass record rules that would normally prevent reading/writing across company boundaries
- `with_company(payment.company_id)` — creates payment clearing entry in payment company context
- `with_company(self.company_id)` — creates settlement entry in invoice company context
- No `ir.rule` is defined in this module to restrict access to interco entries
- No security CSV in the module — relies on base `account` module record rules
- `check_company=True` on config fields prevents cross-company config misuse at field level

**L6 Assessment:** APPLICABLE. sudo() + with_company() pattern used. No dedicated ir.rule in this module.

---

## L7 — Config Prerequisites

**File:** `account_payment_interco/models/account_move.py:11-13` (filter predicate)

Required per company:
1. `account_interco_clearing_journal_id` must be set (general journal) — checked in both invoice company (line 11) and payment company (line 26)
2. For sale/inbound direction: invoice company needs `account_interco_receivable_id`; payment company needs `account_interco_payable_id`
3. For purchase/outbound direction: invoice company needs `account_interco_payable_id`; payment company needs `account_interco_receivable_id`
4. Multi-company must be active (`base.group_multi_company`) for the settings section to appear
5. `account_payment` module must be installed (manifest dependency)
6. Payment must come from a payment provider (transaction-based payment flow via `payment.transaction`)

**L7 Assessment:** APPLICABLE. 3 per-company accounts + multi-company group required.

---

## L8 — Immutability / Audit

No lock checks added by this module. Once posted, standard `account.move` immutability applies. No reversal logic added.

**L8 Assessment:** NOT APPLICABLE to this module specifically — relies on base account immutability.

**Key finding:** If one company's clearing entry is reversed, there is NO code in this module to auto-reverse the other company's entry. Each leg is independent after creation. This is a GAP.

---

## L9 — Accounting Postings

### Sale scenario (Company KE issues invoice; Company BE makes payment):

**Clearing entry in Company BE (payment company):**
```
DR  AR/AP outstanding account (counterpart_account)    [clearing_balance]
CR  account_interco_payable_id (Company BE)            [-clearing_balance]
```

**Settlement entry in Company KE (invoice company):**
```
DR  account_interco_receivable_id (Company KE)         [-clearing_counterpart_balance]
CR  AR invoice line account                            [clearing_counterpart_balance]
```

Both entries use the payment's currency for the clearing entry and the company's own currency for the settlement entry (line 105: `currency_id': self.company_id.currency_id.id`).

### Purchase scenario (Company KE issues bill; Company BE makes payment):

**Clearing entry in Company BE (payment company):**
```
DR  account_interco_receivable_id (Company BE)         [-clearing_balance]
CR  AP/outstanding account (counterpart_account)       [clearing_balance]
```

**Settlement entry in Company KE (invoice company):**
```
DR  AP bill line account                               [clearing_counterpart_balance]
CR  account_interco_payable_id (Company KE)            [-clearing_counterpart_balance]
```

**L9 Assessment:** APPLICABLE. Two entries created: one in payment company, one in invoice company. Currency conversion handled via balance fields.

---

## L10 — Cron / Queue

No cron jobs. No job queue. Everything is synchronous in-transaction on `_post()`.

**L10 Assessment:** NOT APPLICABLE.

---

## L11 — API

No RPC endpoints, no controllers. Standard ORM method override only.

**L11 Assessment:** NOT APPLICABLE.

---

## L12 — Runtime / AWT

To confirm cross-company journal entries appear in both companies at runtime:
1. Configure two companies each with a clearing journal + interco receivable + interco payable accounts
2. Create sale order in Company KE for a partner
3. Create payment via payment provider in Company BE for the same partner
4. Confirm sale order → automatic invoice created (if `sale.automatic_invoice` = True)
5. Post the invoice (`_post()` trigger fires)
6. Verify: search `account.move` with `company_id = Company KE` for type=entry with ref "Interco Settlement"
7. Verify: search `account.move` with `company_id = Company BE` for type=entry with ref containing payment memo
8. Verify invoice `payment_state` = 'paid'
9. Verify counterpart lines are reconciled
10. Verify payment outstanding lines are reconciled

**L12 Assessment:** AWT required — multi-company setup with payment provider needed.

---

## Test Coverage

**File:** `account_payment_interco/tests/test_interco_clearing.py`

- `TestIntercoClearingSale.test_interco_sale` — full sale flow with verification
- `TestIntercoClearingPurchase.test_interco_purchase` — full purchase flow with verification
- Uses `freeze_time` for deterministic dates, KES/USD cross-currency setup
- Tests both `accounting_installed=True` and `accounting_installed=False` subtests
- Tagged `post_install` only

---

## GAP-002 Assessment

**GAP-002 Status: PARTIAL CLOSE**

`account_payment_interco` provides:
- Automatic two-way journal entry creation on invoice post
- Reconciliation of both legs (payment outstanding + invoice AR/AP)
- Multi-currency support (payment currency for clearing, company currency for settlement)
- Configurable per-company clearing journal + accounts

**Remaining gaps:**
1. No automatic reversal propagation — reversing one leg does not reverse the other
2. No error handling if `with_company` context fails (e.g., if accounts differ between companies)
3. Currency conversion uses `balance` field (already converted) — relies on ORM-level conversion, no explicit rate override
4. No `ir.rule` restricting who can edit interco entries after creation
5. Only works when payment is via `payment.transaction` (provider-based) — manual journal payments are NOT covered
