# P06_SETTLEMENT_STATE_MATRIX.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Purpose

The Payment State Model file establishes *what the states are*. This file establishes *what combinations of them can occur*, which combinations are contradictory, and which combinations the reference implementation permits without complaint. A settlement matrix is only useful if it enumerates the **illegal** cells, because those are the cells the target design must make unreachable.

---

## 2. The four axes

| Axis | Field | Values | Writer |
|---|---|---|---|
| **P — Payment state** | `account.payment.state` | draft · in_process · paid · canceled · rejected | computed+writable |
| **A — Accounting posting state** | `account.move.state` | draft · posted · cancel | posting engine |
| **B — Bank confirmation** | *no field* — proxy `account.payment.is_matched` | true · false | computed, config-dependent |
| **R — Reconciliation** | `account.bank.statement.line.is_reconciled` / `account.payment.is_reconciled` | true · false | computed |

**Nominal cardinality:** 5 × 3 × 2 × 2 = **60** cells.
**DENOMINATOR:** POPULATION: the Cartesian product of the four declared value sets. UNIT: state combination. This is an **analytical** denominator, not an observed one — no runtime census of occupied cells was taken (source NC-01, no database access). Every "reachable / unreachable" judgement below is derived from source reading, class **B or D**, never class A.

---

## 3. Settlement lifecycle — the intended path

```
 [P draft / A none / B false / R false]
        │  action_post  →  write() generates + posts the move
        ▼
 [P in_process / A posted / B false / R false]        ← money committed, bank silent
        │  bank event arrives, statement line matched
        ▼
 [P paid / A posted / B true / R true]                ← the only fully-consistent terminal cell
```

Three exits from the nominal path, each producing a distinct terminal shape:

```
 rejected   ← bank refused          → P rejected / A posted / B false / R false
 canceled   ← we withdrew           → P canceled / A cancel or deleted / B false / R false
 reversed   ← corrected after the fact → P paid / A posted / B true / R FALSE   ← see SSM-F-06
```

---

## 4. The matrix — occupied, illegal, and silently permitted

Legend: **OK** = coherent · **ILLEGAL** = contradictory, must be unreachable · **PERMITTED** = contradictory but the reference does not prevent it · **N/A** = cannot arise.

| # | P | A | B | R | Verdict | Evidence / mechanism |
|---|---|---|---|---|---|---|
| 1 | draft | none | F | F | OK | initial |
| 2 | draft | draft | F | F | OK | draft move exists |
| 3 | draft | posted | F | F | **PERMITTED** | `state` is `readonly=False` on a stored compute (`$V18E/account/models/account_payment.py:48`); a direct write to `draft` does not unpost the move |
| 4 | in_process | posted | F | F | OK | the normal in-flight cell |
| 5 | in_process | **none** | F | F | **PERMITTED** | with no outstanding account, `_generate_journal_entry` does not fire (`$V18E/account/models/account_payment.py:1001-1002`) and the ValidationError at `:837-845` is conditioned on `outstanding_account_id` |
| 6 | paid | **none** | F | F | **PERMITTED — SEVERE** | same mechanism. A payment reaches its terminal state with **no journal entry at all**. |
| 7 | paid | posted | **T** | F | **PERMITTED** | `is_matched = True` by config branch (`:436-450`) while counterpart lines remain unreconciled |
| 8 | paid | posted | F | T | **PERMITTED** | counterpart reconciled but the liquidity leg never matched — `is_matched` false, yet `_compute_state` promoted to `paid` via the invoice-derived branch (`:424`) |
| 9 | paid | posted | T | T | **OK** | the only fully coherent terminal cell |
| 10 | paid | **cancel** | T | T | **PERMITTED** | `button_cancel` does not reset `payment.state`; only `action_cancel` does, and it is a separate method |
| 11 | canceled | posted | F | F | **PERMITTED** | `action_cancel` (`:1078-1082`) unlinks *draft* moves and cancels the rest; a posted+hashed move cannot be cancelled, leaving P canceled over A posted |
| 12 | rejected | posted | T | T | **PERMITTED — SEVERE** | `action_reject` (`:1074-1075`) is a bare `self.state = 'rejected'`. **Nothing un-matches or un-reconciles.** A bank-rejected payment keeps its reconciliation. |
| 13 | rejected | posted | F | F | OK-ish | the intended shape, but see SSM-F-03 |
| 14 | paid | posted | T | **F** | **PERMITTED** | reversal after reconciliation — `remove_move_reconcile()` destroys R silently and leaves P untouched. See SSM-F-06. |
| 15 | in_process | posted | **T** | F | **PERMITTED** | cash-type outstanding account or journal-default liquidity; B asserted without any bank event |
| 16 | draft | none | **T** | F | **PERMITTED** | zero-amount payment: `:442-444` sets both `is_reconciled` and `is_matched` true regardless of state |
| 17 | canceled | none | F | F | OK | never posted |
| 18 | paid | posted | T | T → then A **draft** | **PERMITTED — SEVERE** | `button_draft` calls `remove_move_reconcile()` (`$V18E/account/models/account_move.py:5283`) **before** the lock-date check at `:3238-3241` |

**Counted:** 18 cells characterised. **1 fully coherent** (cell 9). **13 PERMITTED contradictions**, of which **3 are marked SEVERE**. The remaining 42 of the 60 nominal cells were **not individually characterised** — Class C (not yet searched). They are not asserted unreachable.

---

## 5. Findings

**SSM-F-01 — Of the 18 cells characterised, exactly one is fully coherent, and reaching it is not enforced.**
*(Bounded by AAS1-C-03: this is a statement about the 18 cells examined, not about all 60. The remaining 42 are Class C — not yet searched — and are not asserted incoherent or unreachable.)*
Cell 9 is the only combination among those 18 in which all four axes agree. Every other terminal shape in §4 is a disagreement between at least two axes, and the reference implementation raises no error in any of them. The system does not know what a correct settlement looks like; it only knows how to compute four values that usually agree.

**SSM-F-02 — A payment can be terminal with no accounting entry (cell 6).**
`$V18E/account/models/account_payment.py:1001-1002` — `need_move = self.filtered(lambda p: not p.move_id and p.outstanding_account_id)`. With no outstanding account there is no move, and the ValidationError at `:837-845` is itself conditioned on the same field. Combined with `account.move._compute_payment_state`'s move-less branch (`$V18E/account/models/account_move.py:1213-1218`), the **invoice is marked settled while the receivable stands in full**. This is the same defect as PSM-F-13 seen from the settlement side.

**SSM-F-03 — `rejected` and `canceled` are indistinguishable in structure and carry no cause.**
`$V18E/account/models/account_payment.py:1072-1082`. Both are single assignments. A bank rejection — the single most important negative event in a treasury process — leaves no reason code, no bank response reference, no timestamp beyond `tracking`, and does not unwind matching (cell 12).

**SSM-F-04 — Batch state is computed from member *flags*, not member *states*, and excludes the failed members from its own quorum.**
`$V18E/account_batch_payment/models/account_batch_payment.py:117-125`:
```
if batch.payment_ids and all(pay.is_matched and pay.is_sent for pay in batch.payment_ids.filtered(lambda p: p.state not in ('canceled', 'rejected'))):
    batch.state = 'reconciled'
```
**Canceled and rejected members are filtered out of the quorum.** A batch of ten payments in which nine settle and one is rejected by the bank computes to `reconciled`. The batch reports success while a real payment failed.
**Batch states: 3** (`draft`, `sent`, `reconciled`) — DENOMINATOR: POPULATION: the `state` selection at `:17-21`. UNIT: value.

**SSM-F-05 — Batch validation does not change any payment state.**
`$V18E/account_batch_payment/models/account_batch_payment.py:285-292` and `:319-329` — `validate_batch` runs a validity gate then `mark_as_sent()`, which is `self.write({'is_sent': True})` (`$V18E/account/models/account_payment.py:1046-1047`). "Sent to the bank" is a boolean flag, not a state. There is therefore **no state that means "irrevocably instructed to the bank"** — the point of no return in any real treasury process.

**SSM-F-06 — Reversal after reconciliation silently vacates R while leaving P at `paid` (cells 14, 18).**
Two independent code paths destroy the reconciliation with no warning and no reference to the statement line whose match is being broken:
- `$V18E/account/models/account_move.py:5283` (`button_draft`) — `self.mapped('line_ids').remove_move_reconcile()`
- `$V18E/account/models/account_move.py:4771-4775` (`_reverse_moves`, `cancel=True`) — same call
and the primitive itself is a bare unlink (`$V18E/account/models/account_move_line.py:3078-3080`).
**Ordering defect:** in `button_draft`, the destructive `remove_move_reconcile()` at `:5283` precedes the state write at `:5284` that triggers the lock-date check at `:3238-3241`. Within one transaction a raise still rolls back, but any caller that reaches `:5283` without the subsequent state write is unprotected.
**PATTERN `statement_line_id|bank.statement` over `$V18E/account/models/account_move.py` lines 5274-5290 and 4760-4803: 0 hits.** Neither method knows it is invalidating a bank reconciliation. **Class A within that declared scope.**

**SSM-F-07 — Partial un-reconcile rolls the payment back to `in_process`, but only from `paid`.**
`$V18E/account/models/account_partial_reconcile.py:110,136` — `to_update_payments = self._get_to_update_payments(from_state='paid')` … `to_update_payments.state = 'in_process'`. A payment sitting at `rejected` or `canceled` is not rolled back, and a payment that reached `paid` by the invoice-derived branch is rolled back on a reconciliation event it never depended on.

**SSM-F-08 — Un-reconciling reverses, rather than deletes, the dependent entries — into a possibly different period.**
`$V18E/account/models/account_partial_reconcile.py:115-133` locates cash-basis moves by `tax_cash_basis_rec_id` and pools them with `exchange_move_id`, then `_reverse_moves(default_values_list, cancel=True)` with a date from `_get_accounting_date`. When the original period is locked, `$V18E/account/models/account_move.py:5669-5674` **shifts the reversal forward to `last_lock_date + 1 day`**.
**Consequence:** undoing a settlement in a closed period produces a reversal in an open one. The two halves of a single correction land in different periods, and neither period's statements are wrong on their own — only the pair is.

**SSM-F-09 — Cash-basis and exchange-difference entries can never be reset to draft, and the code carries a second permanent marker to keep that true after the reconciliation is gone.**
`$V18E/account/models/account_move.py:5343-5350` — a `UserError` for exchange-difference entries and another for cash-basis, the latter testing `move.tax_cash_basis_rec_id or move.tax_cash_basis_origin_move_id` precisely because the first field is emptied when the reconciliation is undone. This is the one place in the reconciliation chain where the implementation deliberately preserves an audit fact across an undo.

---

## 6. Transitions the reference does not express

| ID | Transition a treasury process requires | Present? |
|---|---|---|
| T-01 | instructed → irrevocable (point of no return) | **NOT FOUND** — only the `is_sent` boolean (SSM-F-05) |
| T-02 | bank-rejected → unwind matching + reopen the obligation | **NOT FOUND** — `action_reject` is a bare assignment (SSM-F-03), cell 12 |
| T-03 | value-dated vs booked-dated confirmation | **NOT FOUND** in the searched scope; the statement line carries one `date` |
| T-04 | partially confirmed by the bank (batch part-settled) | **NOT FOUND** — batch quorum excludes failures (SSM-F-04) |
| T-05 | returned/bounced item reverses a settlement | **NOT FOUND** in the v18 pattern set; a v14 custom module `account_payment_return` implements it (see Custom Delta) |
| T-06 | recalled/amended instruction | **NOT FOUND** |
| T-07 | reconciliation superseded by a corrected match, with both retained | **NOT FOUND** — the old partial is unlinked, not superseded |

**DENOMINATOR for this table:** POPULATION: the S-01 P06 module set. PATTERN: model/field/method names for each concept plus common synonyms. UNIT: mechanism. **Every row is Class B — not found in the searched scope — not Class A.**

---

## 7. Requirements arising

| ID | Requirement |
|---|---|
| SSM-R-01 | The settlement matrix must be **closed**: every cell is either declared legal or made unreachable by a guard, and the guard is tested. |
| SSM-R-02 | A payment may not reach a terminal state without an accounting entry. |
| SSM-R-03 | `rejected` must carry a cause, a bank reference and a timestamp, and must unwind matching. |
| SSM-R-04 | A batch's state must be computed over **all** members, failures included. |
| SSM-R-05 | An irrevocable-instruction state must exist and must be a state, not a flag. |
| SSM-R-06 | Breaking a reconciliation must be an explicit, authorised, logged act — never a side effect of resetting a document. |
| SSM-R-07 | A correction spanning a closed period must produce a single visible pairing of the original and its reversal, not two unlinked entries in different periods. |
| SSM-R-08 | Partial bank confirmation must be representable. |

---

# End
