# 03 — P05 EXPENSE RECOGNITION MATRIX + ACCOUNTING EVENT REGISTER

`LAYER 2 — AUDIT QUARANTINE`

## 1. Recognition Timing — The Central Finding

> **Expense is recognised at APPROVAL, not at posting, not at payment, and not at the date the cost
> was incurred.** The approval transition is the accounting event owner.

`_do_approve` calls `_do_create_moves()` **before** it writes `approval_state = 'approve'`, and the
moves are created `sudo()` with an explicit comment that the approver "may not have the accounting
rights (and there is no reason to give them those rights)".

`ENT18/hr_expense/models/hr_expense_sheet.py:711-721` and `:746-760`

The document state model then *derives* itself from the entries rather than driving them:
`_compute_state` (`:264-309`) reads `account_move_ids` and `payment_state` to decide whether the
sheet reads `approve`, `post` or `done`. There is no independent posting decision.

## 2. Accounting Event Register

| ID | Accounting Event | Emitted by | Entry state at emission | Date used | Lock-date consulted |
|---|---|---|---|---|---|
| `AE-01` | Employee claim recognised | `_do_approve` → `_prepare_bills_vals` | `draft` | `accounting_date` (derived) | **Yes** |
| `AE-02` | Employee claim posted | `action_sheet_move_post` → `action_post` | `posted` | unchanged | Yes (core) |
| `AE-03` | Company-paid cost recognised | `_do_approve` → `_prepare_payments_vals` (per line) | `draft` | `expense.date` | **No** |
| `AE-04` | Company-paid cost posted | `action_sheet_move_post` → `origin_payment_id.action_post` | `posted` | unchanged | Yes (core) |
| `AE-05` | Advance recognised **and posted in one action** | `button_post_bill` | `posted` immediately | `date.today()` (server) | Yes (core `action_post`) |
| `AE-06` | Advance liquidated vs vendor bill | `advance.request.reconcile.apply` | `posted` immediately | the vendor bill's `date` | Yes (core) |
| `AE-07` | Advance cash return | `advance.expense.clear.wizard.apply_payment` | `posted` immediately | wizard `date` (context today default) | Yes (core) |
| `AE-08` | Petty cash float top-up | manual bill with `is_petty_cash` | `posted` on user action | move `date` | Yes (core) |
| `AE-09` | WHT withheld | `account.payment.register` write-off line | with the payment | payment date | Yes (core) |
| `AE-10` | Claim reversal | `_do_reverse_moves` | reversal posted, `cancel=True` | `context_today` | Yes (core) |
| `AE-11` | Draft entry destroyed on refusal | `_do_refuse` → `unlink()` | — | — | n/a |
| `AE-12` | Entry force-cancelled from an advance | direct `write({'state':'cancel'})` | `cancel` | — | **Partial** — see `10 EC-08` |

## 3. Date Derivation — `AE-01` vs `AE-03`

### 3.1 `AE-01` (employee-paid) — `_calculate_default_accounting_date`
`ENT18/hr_expense/models/hr_expense_sheet.py:798-822`

| Condition | Resulting accounting date |
|---|---|
| latest expense date **after** end of current month | that expense date |
| latest expense date **within** current month | **today** |
| otherwise | `min( max( end-of-month(latest expense), end-of-month(lock date + 1 month) ), today )` |

Three observations, all `FACT VERIFIED`:
1. The date is **system-derived from the clock**, not from the document. "Today" appears in two of the
   three branches. The same claim approved on two different days books to two different periods.
2. The lock date is consulted, but as a *floor to step over*, not as a barrier: the function actively
   computes the first open period after the lock and books there.
3. `accounting_date` is only assigned inside `_do_create_moves` for `own_account` sheets
   (`:758-759`). It is left unset on the company-paid branch.

### 3.2 `AE-03` (company-paid) — no equivalent
`_prepare_move_vals` sets `date = most_recent_expense` (`:856-857`), then `_prepare_payments_vals`
overrides it per line with `date = self.date`, the individual expense date (`hr_expense.py:959`,
with the inline comment "Overidden … so we can use the expense date").

**No fiscal-lock consultation exists on this branch at the point the default date is derived.**

> **CORRECTION (AAS-03 Expert 1).** The original wording — *"lock-date protection is asymmetric
> between the two payment modes"* — was **OVERSTATED** and is withdrawn. Lock-date *enforcement* is
> **not** asymmetric: `ENT18/account/models/account_move.py:3235, 3240, 3282` enforce on date/state
> write and at post, and both branches post through `action_post`
> (`hr_expense_sheet.py:595, 598`). The surviving, verified claim is narrower:
> **the default accounting date is lock-aware on the `own_account` branch only.**
>
> Two amplifications supplied by Expert 1 that survive re-derivation:
> (a) even on `own_account`, the lock date is consulted **only** in the third branch (`:814-822`);
> the `:808-812` branches return without consulting it;
> (b) `_do_create_moves:759` reads `sheet.accounting_date or sheet._calculate_default_accounting_date()`,
> and `accounting_date` (`hr_expense_sheet.py:206`) is a **plain writable Date** — pre-setting it
> skips the lock-aware computation entirely.

The residual asymmetry is in failure *mode*: a back-dated company-paid expense fails hard at posting,
where the employee-paid branch silently shifts the date instead. `P05-F-22`, carried to `10 EC-12`.

### 3.3 Maturity date divergence on the company-paid branch
`ENT18/hr_expense/models/account_move.py:62-76` sets the payment-term line's `date_maturity` to
`expense_sheet_id.accounting_date or fields.Date.context_today(...)`. Since `accounting_date` is not
populated on this branch (§3.1 obs. 3), `date_maturity` falls to **today** while the move `date` is
the **expense date**. Ageing and entry date diverge by construction. `P05-F-new-01`.

## 4. Recognition Matrix by Class

| Class | Recognition trigger | Recognised amount | Reversal path | Timing correctness |
|---|---|---|---|---|
| Direct expense, employee-paid | Claim approval | `total_amount` (company currency) | `_do_reverse_moves`, then detached | Cost date ≠ entry date; see §3.1 |
| Direct expense, company-paid | Claim approval | per line `total_amount` | reversal, per line | Entry date = expense date |
| Petty cash | Claim approval | `total_amount` | as employee-paid | **GL target disputed** — `EX-04` |
| Employee advance | **Advance disbursement** | `requested_amount` less already-billed | `state='cancel'` write, or clearing entry | **Recognised before the cost exists** |
| Vendor expense (service purchase) | Vendor bill posting | bill amount | credit note | Standard |
| Prepaid | — | — | — | **Not supported** (`NC-08` B) |
| Accrued | — | — | — | **Not supported** (`NC-09` B) |

## 5. Recognition Integrity Defects

| ID | Defect | Evidence | Class |
|---|---|---|---|
| `RI-01` | Recognition happens at approval by a user who is explicitly *not* required to hold accounting rights, under `sudo()`. | `hr_expense_sheet.py:747-749` | FACT VERIFIED |
| `RI-02` | Refusal after approval `unlink()`s the draft entry, leaving no record that recognition occurred and was withdrawn. | `hr_expense_sheet.py:733-734` | FACT VERIFIED |
| `RI-03` | Reset detaches the entries from the claim (`Command.clear()`), and reversal nulls `expense_sheet_id` on the original. After a reset the claim shows **no** entries and `payment_state` recomputes to `not_paid`, while the ledger retains both the original and its reversal as orphans. | `hr_expense_sheet.py:602-604`; `account_move.py:87-90` | FACT VERIFIED |
| `RI-04` | Amount, currency, date, product and quantity remain writable on the expense line after posting; nothing propagates the change to the posted line. | `hr_expense.py:613-643` | FACT VERIFIED |
| `RI-05` | The advance recognises expense at disbursement with `tax_ids` explicitly emptied, so neither VAT nor WHT attaches to the recognised amount. | `advance_expense_request.py:255` | FACT VERIFIED |
| `RI-06` | The advance's accounting date is the **server's** date (`date.today()`), not the user's context date. Across a UTC offset this shifts period assignment at month and year boundaries. | `advance_expense_request.py:263-264` | FACT VERIFIED |
| `RI-07` | `button_post_bill` asserts no state in Python. Whether approval actually gates recognition depends on view-level gating alone. Expert 3 tasked to settle. | `advance_expense_request.py:239-273`; `16 §4` | SUPPORTED INTERPRETATION |

## 6. What SMEsPlus Must Decide

| ID | Decision | Owner |
|---|---|---|
| `BD-01` | Is the accounting event owner **approval** or **posting**? The reference chose approval; the consequence is that a non-accountant emits ledger facts. | BOSS CONTROLLED DECISION |
| `BD-02` | Must an advance create an employee **receivable** rather than an expense? Answering "yes" invalidates the reference pattern entirely for this flow. | BOSS CONTROLLED DECISION |
| `BD-03` | Is an entry's date permitted to be derived from the clock at all, or must it always be derived from a document fact? (Same question as Account Wave A raised for the core ledger — see `12 D-04`.) | BOSS CONTROLLED DECISION |
| `BD-04` | Are `PREPAID` and `ACCRUED` in scope for P05, given the reference supplies neither? | BOSS CONTROLLED DECISION |
