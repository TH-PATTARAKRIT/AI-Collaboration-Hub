# 02 — P05 EXPENSE CLASSIFICATION MATRIX

`LAYER 2 — AUDIT QUARANTINE`

## 1. The Eight Directive Classes vs. What the Reference Actually Distinguishes

The P05 directive requires eight classes to be distinguished. The finding of this matrix is that
the reference platform distinguishes **three**, and derives the rest — where it derives them at all —
from partner identity or from a chart-of-accounts convention, not from a typed field.

| # | Directive Class | Typed carrier in the reference? | What actually carries it | Class |
|---|---|---|---|---|
| 1 | `DIRECT EXPENSE` | **Yes (implicit)** | The default. Any expense line whose account resolves to an expense-type account. | FACT VERIFIED |
| 2 | `PREPAID EXPENSE` | **No** | No prepaid mechanism found in the P05 surface. The advance flow debits an **expense** account, not a prepaid asset. | `NC-08` class B |
| 3 | `ACCRUED EXPENSE` | **No** | No accrual mechanism in the expense surface. Timing is governed only by the entry date. | `NC-09` class B |
| 4 | `EMPLOYEE RECEIVABLE` | **No** | The advance does not create a receivable. It creates a payable and an immediate expense. | FACT VERIFIED — see §3 |
| 5 | `EMPLOYEE PAYABLE` | **No distinct account** | The employee's partner's `property_account_payable_id` — the same field a vendor uses. | FACT VERIFIED |
| 6 | `PETTY CASH` | **Yes, as a payment mode** | `payment_mode='petty_cash'` + `petty.cash` master record. **The GL consequence is disputed** — see `05 §4` / `EX-04`. | DISPUTED |
| 7 | `CORPORATE CARD CLEARING` | **No process model** | `liability_credit_card` exists as an account *type*; no card statement, no clearing, no card master. | `NC-04` class B |
| 8 | `VENDOR AP` | **Yes** | Standard vendor bill. In the expense surface it is reached through `vendor_id` on a company-paid line. | FACT VERIFIED |

## 2. What the Reference Actually Types

The single typed discriminator in the expense surface is `payment_mode`:

| Value | Label | Origin | Accounting branch |
|---|---|---|---|
| `own_account` | Employee (to reimburse) | Core, **default** | Vendor bill against the employee |
| `company_account` | Company | Core | Per-line payment against an outstanding account |
| `petty_cash` | Petty Cash | CUSTOM `selection_add` | Routed with `own_account` — see `EX-04` |

`ENT18/hr_expense/models/hr_expense.py:170-179`; `CUSTOM/hr_expense_petty_cash/models/hr_expense.py:11-14`

### 2.1 Consequence — the classification is a *funding* axis, not a *nature* axis

`payment_mode` answers "whose money left first", not "what kind of cost is this".
The nature of the cost is carried only by the resolved expense account, which is derived, not declared:

| Priority | Source of the expense account | Citation |
|---|---|---|
| 1 | `hr.expense.account_id` (user-overridable, stored, precomputed) | `hr_expense.py:181-188, 982-985` |
| 2 | The product's expense account | `hr_expense.py:988-989` |
| 3 | The product **category** company-dependent fallback | `hr_expense.py:991-992` |
| 4 | The journal default — **only if the journal is a purchase journal** | `hr_expense.py:997-1001` |

> **`P05-F-23`** Priority 4 is unreachable on the company-paid branch, because that branch's journal is
> the payment method line's bank/cash journal (`hr_expense_sheet.py:276-277` `_compute_journal_id`,
> read at `hr_expense.py:890`), never a purchase journal.
> *Citation corrected by AAS-03 Expert 1: the brief's original `hr_expense_sheet.py:247-250` is
> `_compute_from_account_move_ids`, not the journal selection. Substance unaffected.*
> The docstring at `hr_expense.py:970-979` documents four fallbacks; three are reachable there.
> If all reachable fallbacks miss, `_get_base_account` returns an **empty recordset** and
> `_prepare_move_lines_vals` writes `account_id: False` (`hr_expense.py:1006-1010`).

### 2.2 The account-domain exclusion

`hr.expense.account_id` excludes `asset_receivable`, `liability_payable`, `asset_cash`,
`liability_credit_card` (`hr_expense.py:186`).

**This is the structural reason class 4 (`EMPLOYEE RECEIVABLE`), class 6 (`PETTY CASH` as an asset)
and class 7 (`CORPORATE CARD CLEARING`) cannot be expressed on an expense line at all.**
An expense line is definitionally a P&L debit in this design. The petty-cash module works around
this by attempting to rewrite the *credit* side after the fact — the mechanism at `EX-04`.

## 3. Employee Advance — Classification Finding

| Question | Answer | Evidence |
|---|---|---|
| Does an advance create an employee receivable? | **No.** | `advance_expense_request.py:239-273` builds `move_type='in_invoice'` |
| What is debited? | An **expense-type account**, resolved entirely by the core ORM. **CORRECTED by AAS-03 Expert 3:** the advance line's own `account_id` is never passed to the bill; resolution is `account_move_line._compute_account_id` (`ENT18/account/models/account_move_line.py:547`, product branch `:602-611`) → `property_account_expense_id` → **product-category** `property_account_expense_categ_id` → fiscal-position remap → sibling-line account → journal default (`:621-629`). The brief's original attribution to `advance_expense_request_line.py:131` was a **factual error**. | `advance_expense_request.py:248-257`; `ENT18/account/models/account_move_line.py:547, 602-611, 621-629` |
| Is this the shipped default? | **Yes.** `__manifest__.py:19` lists `demo/advance_request_demo.xml` under the **`data`** key, not `demo`. Every install therefore creates account `555555 "Employee Advance Expense"` with `account_type=expense` and points the shipped advance product's `property_account_expense_id` at it, `noupdate="1"`. The misclassification is shipped, not accidental. (Expert 3 `X3-N-01`) | `demo/advance_request_demo.xml:3-10, 21` |
| Divergence risk | Because the bill debits the **core-resolved** account while both clearing paths credit the **advance line's** `account_id` (`05 §4`), the two can be different accounts. Neither is validated against the other. | Expert 3 §1 |
| What is credited? | The requester's partner payable — the standard `in_invoice` payment-term line. | `advance_expense_request.py:261` |
| When is expense recognised? | **At advance disbursement**, before any cost is incurred or evidenced. | `advance_expense_request.py:272` `action_post()` |
| Is `advance_expense_request_line.account_id` used? | Written by an onchange; **not passed** into the bill. **SETTLED by AAS-03 Expert 3** (whose own hypothesis that it was never read was disproved): it **is** read, in exactly two places — `wizard/advance_request_reconcile.py:73` and `models/account_move.py:90` — both the **credit side of a clearing entry**. It is never validated and never required, which is exactly why the clearing collapse at `05 §4 GL-05` is reachable. | `advance_expense_request_line.py:100-104, 131`; `16 §4.3` |

> **`CD-01` DESIGN CANDIDATE / CONTRADICTION** — This makes `PREPAID EXPENSE` and `EMPLOYEE RECEIVABLE`
> structurally absent and creates a double-recognition exposure: the advance debits the expense account,
> and the employee's later `hr.expense` claim for the same cost debits it again. Whether the exposure is
> *reachable end to end* depends on whether the liquidation paths fully offset. Carried to
> `11_CONTRADICTION_REGISTER` as `C-02` and to `16 §4` (Expert 3) for adversarial settlement.

## 4. Petty Cash — Classification Finding

| Aspect | Reference behaviour | Citation |
|---|---|---|
| Master record | `petty.cash`: holder partner, petty cash account, max limit, computed balance | `petty_cash.py:12-33` |
| Holder identity | A `res.partner`, **not** an `hr.employee` | `petty_cash.py:13-17` |
| Balance | Non-stored compute: Σ(debit−credit) of posted lines on (`partner_id`, `account_id`) | `petty_cash.py:38-50` |
| Company scope | **None.** No `company_id`, no record rule, `unique(partner_id)` is global. | `petty_cash.py:12-36` |
| Uniqueness consequence | One partner cannot hold a float in two companies of the same database. | `petty_cash.py:34-36` |
| Balance consequence | **CORRECTED BY AAS-03 EXPERT 2.** The primary research claimed the balance sums across all companies. The written domain does omit company, **but the search is not `sudo()`**, so the core record rule `account.account_move_line_comp_rule` (`ENT18/account/security/account_security.xml:153`) *does* company-filter it. The real defect is different and arguably worse: **the same float record shows a different balance to different users**, depending on each user's allowed companies. Class C. | `petty_cash.py:42-48`; `ENT18/account/security/account_security.xml:153` |
| Genuine unscoped access | `hr_expense_petty_cash/models/account_move.py:24` does `self.env["petty.cash"].sudo().search([("partner_id","=",…)], limit=1)` — **sudo, unscoped, `limit=1`**. With the global `unique(partner_id)`, a partner holds exactly one float record system-wide, so **company B's vendor bills are gated by company A's float configuration** (`:33-38` raises if that account appears on any line). Class C. This, not the balance compute, is the citation `TZ-02` should carry. | Expert 2 §1 |
| Currency | `petty_cash_balance` and `petty_cash_limit` are bare `Float` with **no currency field** — the same defect class as the WHT amount (`07`). | `petty_cash.py:23-30` |
| Compute staleness | `@api.depends("partner_id","account_id")` omits the journal lines the method actually reads, so the balance is stale within a transaction. The v14 tests worked around this by calling `_compute_petty_cash_balance()` by hand. | `petty_cash.py:38-39` |

> **`TZ-02` TOLERANCE-ZERO — company isolation.** Both consequences above are structural, not
> configuration-dependent. **SETTLED by AAS-03 Expert 2:** an independent search of the whole custom
> tree (5087 files, patterns declared at `21 NC-05`) finds **no other module touching `petty.cash`,
> no `ir.rule` for it anywhere, and zero `company_id`/`check_company` in the module** — class **A**
> within that root. Expert 2 also corrected which consequence follows; see the two rows above.
>
> **SCOPE REVALIDATION (`CORR1`)** — `TZ-02` was originally framed on a blanket
> "Tenant+Company mandatory everywhere" assumption. It is **upheld and re-derived** in
> `22_P05_SCOPE_OWNERSHIP_MATRIX.md §3 R-02` from the object's own financial semantics:
> the float balance is Σ posted GL lines on a company's account, therefore `petty.cash` is
> COMPANY-scoped and company context is required and absent. The requirement is now proven,
> not assumed.

## 5. Corporate Card — Classification Finding

Declared search, all four roots, pattern
`grep -rilE "corporate[ _-]?card|company[ _-]?card|card[ _-]?statement|card[ _-]?clearing" --include='*.py' --include='*.xml'`:
**0 files** in `ENT18`, `ARC18`, `CUSTOM`, `LEGACY14`.

Positive counter-evidence that qualifies the negative: `liability_credit_card` **is** a valid
`account.account.account_type`, referenced in eight core locations including the journal report and
the cash-flow report (`ENT18/account_reports/models/account_journal_report.py:637, 838, 843, 974`;
`account_cash_flow_report.py:195`).

> **CORRECTED AND EXTENDED BY AAS-03 EXPERT 2.** The primary research's counter-evidence was
> incomplete. A **first-class corporate-card construct does exist in v18** and was missed:
> `account.journal.type` includes `('credit', 'Credit Card')`
> (`ENT18/account/models/account_journal.py:98`), with
> `default_account_id_types['credit'] = 'liability_credit_card'` (`:379`), an auto-provisioning
> `_prepare_credit_account_vals` (`:767`) and a lookup at `:844`. Because
> `_get_expense_account_destination` for company-paid expenses uses `payment_method_line_id.journal_id`
> (`hr_expense_sheet.py:879`), **the company-paid expense path can already be pointed at a credit-card
> journal today.**

**Conclusion, correctly classed and restated:** a corporate-card *account type* **and a corporate-card
journal type* both exist and are reachable from the company-paid expense path. What was
**NOT FOUND IN SEARCHED SCOPE** is a corporate-card *process model* — card master, statement import
mapped to a card, cardholder allocation, clearing (`21 NC-04`, class **B**). This is **not** a
statement that the capability cannot be built. Class B is not upgraded.

## 6. Classification Gap Summary

| Directive class | Reference support | Gap severity for SMEsPlus |
|---|---|---|
| Direct expense | Full | — |
| Prepaid expense | Absent (`NC-08` B) | **Design requirement** |
| Accrued expense | Absent (`NC-09` B) | **Design requirement** |
| Employee receivable | Absent, and actively contradicted by the advance design | **Design requirement — HIGH** |
| Employee payable | Conflated with vendor AP | **Design requirement — HIGH** |
| Petty cash | Present but GL effect disputed | **Blocked pending `16 §4`** |
| Corporate card clearing | Absent (`NC-04` B) | **Design requirement** |
| Vendor AP | Full | — |

**Six of eight directive classes are either absent or conflated in the reference.**
P05 for SMEsPlus is therefore predominantly a *design* problem, not a *transfer* problem.
Carried to `17_P05_AAS_PLUS.md §6` as Layer 1 design input.
