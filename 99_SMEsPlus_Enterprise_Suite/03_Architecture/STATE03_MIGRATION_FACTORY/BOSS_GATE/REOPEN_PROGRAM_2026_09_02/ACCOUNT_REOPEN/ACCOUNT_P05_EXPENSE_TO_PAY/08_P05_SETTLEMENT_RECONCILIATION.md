# 08 — P05 SETTLEMENT & RECONCILIATION

`LAYER 2 — AUDIT QUARANTINE`

## 1. Settlement Paths

| Path | Instrument | Producer | Reconciles against |
|---|---|---|---|
| `S-01` Employee reimbursement | outbound `account.payment` via the payment register | `hr_expense_sheet.py:606-614` → core wizard | the expense bill's payable line |
| `S-02` Company-paid expense | `account.payment` created **at approval**, posted with the sheet | `hr_expense_sheet.py:763-782, 598` | bank statement, via the outstanding account |
| `S-03` Advance payment to employee | standard outbound payment on the advance bill | core | the advance bill's payable line |
| `S-04` Advance liquidation vs vendor bill | a manual `entry` plus `js_assign_outstanding_line` | `advance_request_reconcile.py:35-49` | the vendor bill's payable line |
| `S-05` Advance cash return | a manual two-line `entry`, **no payment object** | `advance_request_reconcile.py:62-92` | nothing — see `SR-04` |
| `S-06` Petty cash float top-up | vendor bill then normal payment | `hr_expense_petty_cash/models/account_move.py` | holder payable |
| `S-07` WHT settlement | payment write-off line | `l10n_th_withholding_tax/wizard/account_payment_register.py` | see `07` |

## 2. Payment-State Derivation

`_compute_from_account_move_ids` (`hr_expense_sheet.py:209-237`) derives the sheet's
`payment_state` and `amount_residual` **differently per branch**:

| Branch | Rule | Citation |
|---|---|---|
| `company_account`, any non-draft move | `amount_residual` forced to `0.0`; `payment_state` = `paid`, or `reversed` if **every** move has a reversal | `:212-220` |
| `company_account`, all moves draft | sum of residuals; state from the set of move states, collapsing mixed states to `partial` | `:221-229` |
| `own_account`, any posted move | sum of residuals; state taken from **`account_move_ids[:1]`** — the first move only | `:232-234` |
| `own_account`, no posted move | `0.0` / `not_paid` | `:235-237` |

### Findings

| ID | Finding | Class |
|---|---|---|
| `SR-01` | On the company-paid branch the sheet asserts `payment_state='paid'` and `amount_residual=0` **as soon as any move is non-draft** — before any bank movement. The comment states this openly: "the state/amount of the related account_move_ids are not relevant". Settlement status on this branch is an assumption, not an observation. | FACT VERIFIED |
| `SR-02` | On the employee-paid branch `payment_state` is read from `account_move_ids[:1]`, justified by the comment "Only one move is created". That invariant holds in the core producer, but the custom fork of `_do_create_moves` can attach more than one move to a sheet (see `05 §2` and `P05-F-05`). Where it does, the sheet reports the **first** move's payment state for the whole claim. | SUPPORTED INTERPRETATION |
| `SR-03` | `reversed` is asserted only when **every** move carries a `reversal_move_ids`. A partially reversed multi-move company-paid sheet reports `paid`. | FACT VERIFIED |
| `SR-04` | The advance cash-return path (`S-05`) creates a journal entry against the payment journal's default account **without an `account.payment`**. The cash movement will not appear in payment listings, payment-based reports, or the bank-reconciliation matching model that keys on payments. | FACT VERIFIED |
| `SR-05` | `_reconcile_payments` flips the sheet to `done` by direct `expense_sheet.state = 'done'` assignment when the residual reaches zero — writing a **stored computed field** (`state` is `compute='_compute_state', store=True`) directly. The next recompute of `_compute_state` will overwrite it from `approval_state`/moves. | FACT VERIFIED — `hr_expense/wizard/account_payment_register.py:39-40` vs `hr_expense_sheet.py:33-49, 264-309` |
| `SR-06` | Expense-linked payments are protected against edits by a guard set that, through a missing comma, does **not** contain `journal_id` or `ref`. See `11 C-01`. | FACT VERIFIED |

## 3. Reconciliation Matrix

| Reconciliation question | Answer | Evidence |
|---|---|---|
| Can an expense claim be traced to its journal entries after a reset? | **No.** `Command.clear()` detaches them and `_reverse_moves` nulls the back-link. | `hr_expense_sheet.py:604`; `hr_expense/models/account_move.py:88` |
| Can an entry be traced to its claim after cancellation? | **No.** `button_cancel` writes `expense_sheet_id = False`. | `hr_expense/models/account_move.py:97-103` |
| Can a claim be traced to its entry after the claim is deleted? | **No.** `ondelete='set null'`. | `hr_expense/models/account_move.py:12` |
| Is there a guard against deleting only some of a claim's entries? | Yes — but it reads `expense_sheet_id`, which the three paths above have already nulled. | `hr_expense/models/account_move.py:92-95` |
| Is line-level traceability complete? | **No.** `expense_id` is on the debit line only, never on the outstanding/credit line. | `hr_expense.py:917` vs `:936-943` |
| Can an advance be traced to its clearing? | Partly — `move_lines_cleared` (m2m) and `clear_move_id` on the request. | `advance_expense_request.py:119-120` |
| Is the advance clearing amount idempotent? | **No — and the stored clearing state is permanently stale.** **CORRECTED by AAS-03 Expert 3:** the brief blamed a dependency cycle. Odoo 18 explicitly tolerates the cycle (`ENT18/odoo/modules/registry.py`, `transitive_triggers`: `if field in seen … return`), so the cycle is not the defect. The operative defect is a **missing** dependency: an enumeration of all seven `@api.depends` decorators in the module (pattern `grep -rn --include='*.py' "@api.depends"`, path set = the whole module, unit = decorator) shows **none** references any `account.move` field (`payment_state`, `state`, `amount_residual`) or `move_lines_cleared`. The stored `bill_state` and `is_clear` are therefore never marked for recompute when an advance bill is posted, paid or cleared. The author's workaround is the non-stored twins `bill_state_dump`/`is_clear_dump`, which the **form** uses for every button `invisible`, while the **list view and every search filter** read the stale stored fields. The filters "Bill Paid", "Not Clear" and "Cleared" — the natural management report on outstanding employee advances — read stale data by construction. | `advance_expense_request.py:131-149, 311-337`; `views/advance_expense_request_view.xml:11,18,25,47,79-81,189-193,230-249` |

> **`SR-07a` BOUND ON `SR-07`, raised by AAS-03 Expert 4 — a survival path the package never checked.**
> A full-package grep for `mail.message` / `chatter` / `tracking` / `ir.attachment` / `message_post` /
> `_creation_message` returned **zero hits across all 39 files present when the sweep was run**: the package never evaluated whether
> lineage survives outside the foreign key. It partly does.
> **(a)** `hr_expense/models/account_move.py:51-54` overrides `_creation_message()` to post
> *"Expense entry created from: &lt;sheet link&gt;"* as a permanent `mail.message` at move creation. None
> of the severing paths edits or deletes that historical chatter — `write()` on `expense_sheet_id`
> does not touch message history. **(b)** `hr_expense_sheet.py:838-841` copies the receipt attachments
> onto the move addressed by `(res_model, res_id)`, not through the severed FK, so they too survive.
> **Exception:** for draft moves that `_do_reverse_moves` **`unlink()`s**, `mail.thread.unlink()`
> (`mail/models/mail_thread.py:348-361`) deletes the `mail.message` rows as well — no survival there.
>
> **This bounds `SR-07`'s severity without overturning it.** After severing there is **no relational
> path** (confirmed verbatim by Expert 4 against every cited line), but a **forensic, non-relational
> path** survives for three of the four mechanisms. Parsing chatter HTML or matching attachment
> checksums is **not** a substitute for a stable identifier and cannot serve as an automated
> reconciliation key — so the design requirement at `17 §6 DI-05` stands unchanged. Recorded in the
> same style as `SC-03` bounds `SC-01`.

> **`SR-07` — the reconciliation identity is not stable.** Three distinct code paths sever the only
> link between an expense claim and its accounting effect, and a fourth (deletion) is defended by a
> guard that reads the field the other three have already cleared. For SMEsPlus this means
> **the claim↔entry relation cannot be the reconciliation key.** An immutable event identity is
> required instead. This is the same conclusion Account Wave A reached for the core ledger
> ("no event identity"); recorded as a cross-process convergence in `09 §4`.

## 4. Period Close

| Question | Answer | Evidence |
|---|---|---|
| Is there a close/cutover routine in P05? | **NOT FOUND IN SEARCHED SCOPE.** Boundary: `hr_expense`, `hr_expense_petty_cash`, `scgl_advance_expense_request`; pattern `grep -rinE "close|cutoff|cut_off|period_end"` on `*.py`. Class **B** — `21 NC-11`. | — |
| What prevents posting into a closed period? | Core fiscal lock, consulted asymmetrically — see `03 §3`. | `hr_expense_sheet.py:814` |
| Are unapproved claims accrued at close? | **No mechanism.** Claims not yet approved have no entry at all (`03 §1`). | `21 NC-09` |
| Are approved-but-unposted claims visible? | Yes — they hold **draft** entries created at approval. A period can therefore close with draft expense entries in it. | `hr_expense_sheet.py:711-721` |
