# 05 — P05 EVENT-TO-GL MATRIX

`LAYER 2 — AUDIT QUARANTINE`
Every row cites the code that produces the line. Accounts are named by their *derivation*, never by a
chart code, because no chart is in scope for this session.

## 1. `AE-01/02` — Employee-paid claim (`own_account`)

Producer: `_prepare_bills_vals` (`hr_expense_sheet.py:824-842`) + `_prepare_move_lines_vals`
(`hr_expense.py:1004-1019`) + core `_compute_needed_terms`.

| Dr/Cr | Account derivation | Amount | Partner | Analytic | Citation |
|---|---|---|---|---|---|
| **DR** | `_get_base_account()` — expense line account | `price_unit × quantity`, taxes **price-included** | `work_contact_id` | `analytic_distribution` carried | `hr_expense.py:1006-1018` |
| **DR** | tax accounts from `tax_ids` | computed tax | — | — | `hr_expense.py:1018`; core tax engine |
| **CR** | `work_contact_id.property_account_payable_id` (or its parent's) | `total_amount` | `work_contact_id` | — | `hr_expense_sheet.py:895-899` |

Notes, all `FACT VERIFIED`:
- Taxes on an expense line are **always** treated as price-included regardless of their configuration:
  `_prepare_product_base_line_for_taxes_computation` forces `special_mode='total_included'`
  (`hr_expense/models/account_move.py:78-83`), and `_compute_totals` forces `force_price_include=True`
  (`account_move_line.py:24-27`). The field help states this openly (`hr_expense.py:198`).
- `move_type='in_invoice'` but the journal may be **any** type: `_check_journal_move_type` is
  suppressed for expense moves (`hr_expense/models/account_move.py:47-49`).

## 2. `AE-03/04` — Company-paid claim (`company_account`), **one entry per expense line**

Producer: `_prepare_payments_vals` (`hr_expense.py:887-968`).

| Dr/Cr | Account derivation | Amount | Partner | Citation |
|---|---|---|---|---|
| **DR** | `_get_base_account()` | `total_amount − Σ tax line balances` | `vendor_id` (**may be empty**) | `hr_expense.py:912-933` |
| **DR** | tax accounts | per tax line | — | `hr_expense.py:930-932` |
| **CR** | `payment_method_line_id.payment_account_id` **or** `company.expense_outstanding_account_id` | `total_amount` | `vendor_id` | `hr_expense.py:936-943`; `hr_expense_sheet.py:878-883` |

Accompanied by an `account.payment` with `payment_type='outbound'`, `partner_type='supplier'`,
`amount = total_amount_currency`, `date = expense.date` (`hr_expense.py:944-955`).

> **`GL-01` FACT VERIFIED** — the base line's `balance` is **overwritten after the loop**:
> `base_move_line['balance'] = self.total_amount - total_tax_line_balance` (`hr_expense.py:933`).
> Because `base_move_line` is the loop variable, this assigns to the **last** base line only. With a
> single base line per expense this is correct; the construction is fragile against any future
> multi-base-line case. Recorded as a design fragility, not a live defect.

> **`GL-02` FACT VERIFIED** — `_check_payable_receivable` is disabled for this branch
> (`account_move_line.py:14-16`), so the outstanding line may legitimately carry a payable/receivable
> typed account that the core constraint would otherwise reject.

> **`GL-03` FACT VERIFIED** — the outstanding line carries **no** `expense_id`
> (`hr_expense.py:936-943` sets no `expense_id`), while the base line does (`:917`). Line-level
> traceability back to the expense exists on the debit side only.

## 3. `AE-05` — Employee advance disbursement (CUSTOM)

Producer: `advance_expense_request.py:239-273`.

| Dr/Cr | Account derivation | Amount | Partner | Citation |
|---|---|---|---|---|
| **DR** | resolved from `product_id` — **no `account_id` is passed** | `requested_amount` less already-billed portion | `requested_by.partner_id` | `:245-257` |
| **CR** | payment-term line, `requested_by.partner_id` payable | same | `requested_by.partner_id` | `:261, 268` |

`tax_ids` is explicitly `[]` (`:255`). `date` and `invoice_date` are both `date.today()` (`:263-264`).
The entry is posted immediately by `action_post()` (`:272`).

> **`GL-04` FACT VERIFIED** (settled by AAS-03 Expert 3). The debit is a **P&L expense**, not a
> balance-sheet advance. The account is resolved wholly by core `_compute_account_id`
> (`ENT18/account/models/account_move_line.py:547`, product branch `:602-611`), in the order
> product `property_account_expense_id` → product-category `property_account_expense_categ_id` →
> fiscal-position remap → sibling-line account → journal default (`:621-629`). The advance line's own
> `account_id` is **never passed** and plays no part.
>
> **It is the shipped default, not a configuration accident:** `__manifest__.py:19` lists
> `demo/advance_request_demo.xml` under the **`data`** key (the `demo` key is commented out at `:21`),
> so every install creates account `555555 "Employee Advance Expense"` typed `account_type=expense`
> and points the shipped advance product at it with `noupdate="1"`
> (`demo/advance_request_demo.xml:3-10, 21`).

## 4. `AE-06/07` — Advance liquidation (CUSTOM)

### 4.1 Offset against a vendor bill — `_prepare_own_account_transfer_move_vals`
`scgl_advance_expense_request/models/account_move.py:58-114`

| Dr/Cr | Account derivation | Amount | Partner |
|---|---|---|---|
| **CR** (per advance) | `advance_id.line_ids[0].account_id` | `min(advance.amount_toclear, remaining bill AP)` | `advance.requested_by.partner_id` |
| **DR** (one line) | `ap_lines.account_id[:1]` — first payment-term line's account | Σ of the credits | the bill's `partner_id` |

Then `js_assign_outstanding_line` reconciles the new debit against the bill (`wizard/advance_request_reconcile.py:43-44`).

### 4.2 Cash returned — `apply_payment`
`scgl_advance_expense_request/wizard/advance_request_reconcile.py:62-92`

| Dr/Cr | Account derivation | Amount |
|---|---|---|
| **DR** | `journal_id.default_account_id` | `amount_toclear` |
| **CR** | `advance_expense_id.line_ids[0].account_id` | `amount_toclear` |

> **`GL-05` FACT VERIFIED, AND ESCALATED BY AAS-03 EXPERT 3** — both liquidation paths credit
> `line_ids[0].account_id`. A multi-line advance spanning several expense accounts is cleared entirely
> against the **first line's** account; the offsetting credit does not follow the original debits.
> The same file uses `ap_lines.account_id[:1]` for the debit side, with the same first-wins defect.
>
> **Escalation.** `advance.expense.request.line.account_id` is populated **only** by the form onchange
> (`advance_expense_request_line.py:123-134`) — no `default`, no `compute`, no `required`. Any line
> created outside the form (RPC, `create()`, data import, or `copy()` — `line_ids` is `copy=True` and
> `copy` does not re-fire onchanges) therefore has `account_id = False`. Both clearing builders then
> emit `Command.create({"account_id": False, …})`, and core `_compute_account_id`'s tail
> (`ENT18/account/models/account_move_line.py:621-629`) assigns **`journal_id.default_account_id`**.
> In `apply_payment` the debit line already *is* `journal_id.default_account_id`, so the entire
> clearing entry collapses to a debit and a credit **on the same bank/cash account** — it nets to zero
> economic effect, posts cleanly, still writes `move_lines_cleared`, and flips `is_clear` to True.
> **A silently no-op clearing that reports the advance as fully cleared.** `TZ-07`.
>
> Note also that the bill was debited to the **core-resolved** account (`05 §3` `GL-04`), while the
> clearing credits the **advance-line** account. Nothing validates that these are the same account.

> **`GL-06` FACT VERIFIED** — neither wizard sets `currency_id` or `amount_currency` on any line.
> Both use bare `debit`/`credit`, which are company-currency fields, while `amount_toclear` derives
> from `requested_amount`, a `Monetary` on `currency_id = related company_id.currency_id`. A
> foreign-currency advance or a foreign-currency vendor bill has no defined behaviour in this path.
> Declared search boundary: the two files named above, pattern
> `grep -nE "currency|amount_currency"` → no match on line construction. Class **B**, `21 NC-10`.

> **`GL-07` FACT VERIFIED** — `apply_payment` builds a two-line entry with `move_type='entry'` on the
> **payment** journal, but creates no `account.payment`. The cash movement exists as a journal entry
> only and will not appear in payment-based reconciliation tooling.

## 5. `AE-08` — Petty cash float

`hr_expense_petty_cash/models/account_move.py:90-111` builds a single invoice line to
`petty_cash.account_id` for `limit − balance`, on a bill whose partner is the holder.
`_check_petty_cash_amount` (`:22-88`) then enforces, at post time:
- a bill touching the petty cash account **must** have `is_petty_cash` set (`:32-38`);
- an `is_petty_cash` bill must have **exactly one** line (`:39-46`) on **that** account (`:47-54`);
- the amount must not exceed `limit − balance` (`:55-88`).

| Dr/Cr | Account | Amount |
|---|---|---|
| **DR** | `petty_cash.account_id` | `limit − balance` |
| **CR** | holder partner payable (standard `in_invoice` term line) | same |

## 6. `BE-12` / `EX-04` — Petty cash **spend**: the disputed row

The intended entry is:

| Dr/Cr | Intended account |
|---|---|
| **DR** | expense account of the claim line |
| **CR** | `petty_cash.account_id`, partner = holder |

The only code that would produce the intended credit is
`hr_expense_petty_cash/models/hr_expense.py:72-79`, which overrides `_get_account_move_line_values()`
and calls `super()` on the same name.

**Verified fact:** the token `_get_account_move_line_values` occurs **0 times** in the entire `ENT18`
tree (search boundary: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo`, all file
types, literal token, no filter). It occurs in `LEGACY14` in three modules including this module's
own v14 ancestor. It is a **v14-era API**.

Meanwhile `hr_expense_petty_cash/models/hr_expense_sheet.py:96` groups `petty_cash` with
`own_account`, so the claim is built by `_prepare_bills_vals`.

> **MECHANISM CORRECTED BY AAS-03 EXPERT 2.** The primary research attributed the credit to
> `_get_expense_account_destination` (`hr_expense_sheet.py:895-899`). **That method is never called on
> the own-account / petty-cash branch.** Its only callers are `hr_expense/models/account_payment.py:17`,
> `hr_expense/models/hr_expense.py:938` (`_prepare_payments_vals`, company-paid only) and
> `hr_expense/models/account_move.py:74` — and that last one sits inside `_compute_needed_terms`
> **guarded by `if move.expense_sheet_id.payment_mode == 'company_account'` at `:62`**. For a
> petty-cash sheet the guard is false, so core `_compute_needed_terms`
> (`ENT18/account/models/account_move.py:1232`) runs and the payment-term line's account falls to the
> standard partner-payable resolution (`account_move_line.py:547` `_compute_account_id`).
> **The conclusion is unchanged; the citation was wrong.**

**Therefore the actual entry appears to be:**

| Dr/Cr | Actual account |
|---|---|
| **DR** | expense account of the claim line |
| **CR** | **employee payable**, partner = the employee's work contact |

…with the petty cash account never credited, and `petty_cash_balance` — which sums posted lines on
(holder partner, petty cash account) — never decreasing as a result of a claim.

> **`TZ-01` TOLERANCE-ZERO — UPHELD BY AAS-03 EXPERT 2 ON FOUR INDEPENDENT LINES, AND UNDERSTATED.**
> Expert 2 attacked the claim from four angles; all four confirm it.
>
> **(a) The port never touched it.** A `diff -rq` of the v14 and v18 module trees shows 10 differing
> files. `models/hr_expense.py:72-79` — the override — is **byte-identical to v14**, while the porter
> edited every other method in that same file. It was never re-pointed at a v18 API.
> **(b) It was live in v14.** The v14 module's own test calls `sheet.action_sheet_move_create()`
> (`LEGACY14/hr_expense_petty_cash/tests/test_hr_expense_petty_cash.py:252`), the v14 entry point that
> consumed the hook; two sibling LEGACY14 modules chain-override the same name.
> **(c) Nothing in `ENT18` routes to it.** 0 files, whole tree, all file types, both `addons` and
> `addons_archive`. Naming variants `_get_account_move_line`, `account_move_line_values`,
> `move_line_values`, `_prepare_account_move_line`, `_prepare_move_line*` were all tried; only
> `_prepare_move_lines_vals` exists. Structurally the v14 hook returned *a list of lines per expense*
> so `[-1]` was the credit line; the v18 method returns **one dict for one debit line** and the payable
> counterpart is not in that list at all — the idiom has no v18 analogue and could not be mechanically
> retrofitted.
> **(d) The tests are decisive, and they cannot run.** `tests/` is **byte-identical between v14 and
> v18** — a pure v14 artefact. `setUp` dies at **line 19** on `env.ref("account.data_account_type_payable")`
> (that xmlid: 0 files in `ENT18`), and six further v14-only APIs follow (`user_type_id`,
> `hr.expense.unit_amount`, `hr_expense.air_ticket`, `action_sheet_move_create`, `account_move_id`).
> The suite therefore **never reaches** the assertion that would have caught the dead redirection.
> The module ships **zero effective test coverage on v18**.
>
> **Resulting GL effect, with Expert 2's confidence classes:** `move_type='in_invoice'`, journal = the
> sheet's `journal_id`, partner = the employee's work contact (class A); DR the expense account from
> `_get_base_account()` (class A); CR the work contact's `property_account_payable_id` via the standard
> payment-term line (class C on the exact resolution order, **class A** on "it is not
> `petty.cash.account_id` and not `petty.cash.partner_id`").
>
> **Net: identical to a plain employee reimbursement. The float account is never credited and the
> holder's balance never decreases** — the balance query filters on `account_id = petty_cash.account_id`,
> which no expense line ever carries. `_check_petty_cash_amount` therefore degenerates into a **one-way
> ratchet: it sees top-ups and never drawdowns.** `TZ-01` is promoted to `FACT VERIFIED` on limbs (a)–(d)
> and the GL consequence is carried at Expert 2's stated classes, not above them.

## 7. `AE-09` — WHT

See `07_P05_TAX_WHT_MATRIX.md`. Summary row:

| Dr/Cr | Account | Amount |
|---|---|---|
| **DR** | vendor/employee payable | gross |
| **CR** | bank | gross − WHT |
| **CR** | `account.withholding.tax.account_id` (payment write-off line, tagged) | WHT | 

Producer: `l10n_th_withholding_tax/wizard/account_payment_register.py:16-26, 59-70`.

## 8. Event-to-GL Coverage Gaps

| Directive-required event | GL mapping found? | Class |
|---|---|---|
| Expense request (pre-spend) | No entry by design — correct | FACT VERIFIED |
| Evidence attached / missing receipt | No accounting effect; no control | `10 EC-11` |
| Prepaid expense recognition + amortisation | **None** | `21 NC-08` class B |
| Accrued expense recognition + reversal | **None** | `21 NC-09` class B |
| Employee receivable on over-advance | **None** — the over-advance is a *credit to expense* | `GL-05` |
| Corporate card clearing | **None** | `21 NC-04` class B |
| Tax non-deductible split | **SETTLED by AAS-03 Expert 4: none.** `account_disallowed_expenses` is **report-only** — a read-only SQL aggregation with no write path to any journal (class **A**) — and has **no connection to `hr_expense`** (class **A**). See `07 §6`. | `07 TX-24` |
| Analytic allocation | Present on the debit line only | `06` |
