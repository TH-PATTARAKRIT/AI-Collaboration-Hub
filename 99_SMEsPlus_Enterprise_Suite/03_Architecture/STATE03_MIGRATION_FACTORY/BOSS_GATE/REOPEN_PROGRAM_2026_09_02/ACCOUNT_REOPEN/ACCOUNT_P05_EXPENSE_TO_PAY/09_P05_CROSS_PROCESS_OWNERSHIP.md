# 09 — P05 CROSS-PROCESS OWNERSHIP REGISTER

`LAYER 2 — AUDIT QUARANTINE`

## 1. Ownership Rule Applied

`ONE FACT → ONE EVENT OWNER → ONE ACCOUNTING EFFECT.`
Where two processes can emit the same accounting effect, the duplicate is attacked and recorded.

## 2. Ownership Boundaries

| Fact | P05 owns? | Contending process | Boundary evidence | Duplicate risk |
|---|---|---|---|---|
| Employee reimbursement liability | **Yes** | P01 (Procure-to-Pay) if the same cost is also entered as a vendor bill | Both produce `move_type='in_invoice'`; the only discriminator is `expense_sheet_id` being set | **HIGH** — no cross-check exists |
| Vendor service purchase | **No — P01 owns it** | P05 reaches vendor AP through `vendor_id` on a company-paid expense line | `hr_expense.py:180, 961` | **MEDIUM** — an expense line can name a vendor and post to vendor-facing accounts without a purchase document |
| Advance to employee | **Yes** | — | `advance.expense.request` | — |
| Advance to vendor | **No — P01 owns it** | `scgl_purchase_advance_payment` sits on `purchase` | that module's manifest `depends: ['purchase']` | **PEER DEPENDENCY OPEN** — P01 must state whether it owns vendor advances |
| Petty cash float | **Yes** | P08/P09 cash management | `petty.cash` + `is_petty_cash` bills | **MEDIUM** |
| Payment execution | **No — settlement/treasury owns it** | P05 nevertheless **creates and posts** payments on the company-paid branch, at approval | `hr_expense_sheet.py:763-782` | **HIGH** — `EX-03` |
| WHT withholding | **Shared** | P01 and P02 use the same payment-register extension | `l10n_th_withholding_tax/wizard/account_payment_register.py` | Low — single implementation |
| Analytic allocation | **Consumes, does not own** | P10 / controlling | `hr_expense.py:516-527` | — |
| Fiscal lock enforcement | **Consumes** | Core ledger (Account Wave A) | `hr_expense_sheet.py:814` | — |
| Chart of accounts | **Consumes** | Core ledger | — | — |
| Employee master | **Consumes** | HR | — | — |

## 3. Duplicate Attack Results

| ID | Duplicate | Verdict | Evidence |
|---|---|---|---|
| `DUP-01` | Same cost claimed twice as two expense lines | Detected but **advisory only** — `action_approve_expense_sheets` opens a wizard, and `wizard/hr_expense_approve_duplicate.py:30-32` then calls `_do_approve()` unconditionally. **CORRECTED by AAS-03 Expert 1:** the brief claimed the incomplete `@api.depends` defeats detection. It does not — `duplicate_expense_ids` is **not stored** (`hr_expense.py:110`), so the compute re-executes on every fresh read and `date` *is* matched; the missing depends degrades only same-transaction cache invalidation. The finding is simultaneously **understated**: the depends omits `date`, **`currency_id` and `company_id`**, all three of which the SQL joins on. A real gap Expert 1 added: `hr_expense_sheet.py:576` filters duplicates to `state in {'approved','done'}`, so a duplicate merely **submitted** raises no warning at all. | `hr_expense.py:110, 490-514`; `hr_expense_sheet.py:576-580`; `wizard/hr_expense_approve_duplicate.py:30-32` |
| `DUP-02` | Same receipt attached to two expenses | Detected by attachment **checksum** only. A re-photographed or re-scanned receipt has a different checksum and is not detected. | `hr_expense.py:467-488` |
| `DUP-03` | Cost paid by advance **and** claimed as an expense | **NOT DETECTED.** Declared boundary: `scgl_advance_expense_request` (all files) and `ENT18/hr_expense` (all files); pattern `grep -rn "advance" ` in `hr_expense`, and `grep -rn "hr\.expense\|hr_expense"` in the advance module. No cross-reference exists in either direction. Class **A** — verified absence within those two module scopes. | — |
| `DUP-04` | Same cost as an expense claim **and** a vendor bill | **NOT DETECTED.** Same boundary as `DUP-03`. Class **A** within scope. | — |
| `DUP-05` | Petty-cash claim reducing the float **and** an employee reimbursement for the same cost | **NOT DETECTED**, and made worse by `TZ-01`: if the petty-cash credit lands on the employee payable, the float is never reduced at all. | `05 §6` |
| `DUP-06` | One expense sheet producing multiple payments on the company branch | **BY DESIGN** — one payment per line. Not a defect, but it breaks the assumption of `_compute_from_account_move_ids`'s employee branch that "only one move is created". | `hr_expense_sheet.py:763-767, 231-234` |

> **`OW-01`** The three highest-value duplicates (`DUP-03`, `DUP-04`, `DUP-05`) are all *cross-document*
> duplicates, and none of them is detected. Every duplicate control in the reference operates **within**
> the expense document family. For SMEsPlus the duplicate control must key on the *cost event*, not on
> the document.

## 4. Convergence with Account Wave A

Three P05 findings restate, in a different surface, conclusions already reached for the core ledger:

| P05 finding | Account Wave A counterpart | Convergence |
|---|---|---|
| `SR-07` — the claim↔entry relation is severed by three paths and cannot be a reconciliation key | Wave A: "no event identity" | **Same root cause.** An immutable, non-severable event identity is required at platform level, not per process. |
| `03 §3` — accounting date derived from the clock, in two of three branches | Wave A: "system-derived accounting date" | **Same root cause**, now shown to recur in a second process and in a custom module (`RI-06`). |
| `05 §2`, `GL-06` — FX and currency handling absent from the custom clearing paths | Wave A: "silent 1:1 FX fallback"; `GB-08` Boss ruling on FX rate ownership and missing-rate policy | The `GB-08` ruling is **binding on P05** and is recorded as a dependency (`12 D-02`). |

## 5. Handoff Ownership to Core Reconciliation

| Element P11/Core needs | P05 can supply | Condition |
|---|---|---|
| Expense by nature | Yes | via the resolved expense account |
| Expense by cost centre | Partial | debit line only; advance chain carries none (`AN-02`) |
| Employee payable balance | Partial | only by partner, not by account (`04 §5`) |
| Advance outstanding balance | **No** | there is no advance asset account (`GL-04`) |
| Float position | **Disputed** | depends on `TZ-01` |
| WHT payable and certificate basis | Pending | Expert 4 (`16 §4`) |
| Claim-to-entry audit trail | **No** | `SR-07` |
