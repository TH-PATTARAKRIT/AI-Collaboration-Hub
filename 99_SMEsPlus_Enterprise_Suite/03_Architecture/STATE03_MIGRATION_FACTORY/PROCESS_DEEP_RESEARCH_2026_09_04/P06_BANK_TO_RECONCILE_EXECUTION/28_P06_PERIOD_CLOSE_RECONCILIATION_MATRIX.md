# P06_PERIOD_CLOSE_RECONCILIATION_MATRIX.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C07)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Cross-reference:** P08 (GL / Period Close). **P06 does not decide P08's close architecture.** Findings here are inputs to it.

---

## 1. The lock-date regime, as it actually resolves

**PC-F-01 — Five lock dates; four soft, one hard.**
`$V18E/account/models/company.py:598-631` — `_get_lock_date_violations` evaluates `fiscalyear_lock_date`, `sale_lock_date`, `purchase_lock_date`, `tax_lock_date` as soft, then `hard_lock_date` with an **inclusive** comparison (`accounting_date <= hard_lock_date`).

**PC-F-02 — Lock dates are inherited up the company hierarchy, and the strictest ancestor wins.**
`$V18E/account/models/company.py:397-401`:
```
def _compute_user_hard_lock_date(self):
    company.user_hard_lock_date = max(
        ...
        for c in company.with_context(active_test=False).sudo().parent_ids
```
and `:530-540` — `_get_user_lock_date` iterates `self.sudo().parent_ids`, documented as *"the field and exceptions … in this company and the parent companies."*
**Classification: FACT VERIFIED.** New evidence from this continuation; it was not in the prior round.
**Consequence:** a parent company's lock binds every branch. Combined with B27-F-04 (branches may hold different Tax IDs), **one company's period close can lock another legally distinct company's books.** Raised as **`P06-B-45`**.

**PC-F-03 — Soft lock dates support per-user exceptions; the hard lock date does not.**
`$V18E/account/models/company.py:530-536`, and the hard lock is one-way: it cannot be removed and cannot be decreased (`:496-499`).

---

## 2. The matrix — what each operation does against a locked period

| # | Operation | Lock checked? | Behaviour | Evidence |
|---|---|---|---|---|
| PC-01 | Post a journal entry dated in a locked period | **YES** | refused | `account_move.py:2377-2393` |
| PC-02 | Change a posted move's date into a locked period | **YES** | refused | `account_move.py:3280-3283` |
| PC-03 | Unlink a posted move's line | **YES** | refused | `account_move_line.py:1699-1706` |
| PC-04 | **Reconcile** two existing items in a locked period | **NO** | proceeds | zero lock hits across the reconcile primitives |
| PC-05 | **Un-reconcile** in a locked period | **NO** | proceeds | `remove_move_reconcile` is a bare unlink, `account_move_line.py:3078-3080` |
| PC-06 | Un-reconcile via the list-view action | **NO** | proceeds | `account_move_line.py:3082-3087` |
| PC-07 | `action_undo_reconciliation` on a statement line | **INDIRECTLY** | blocked, but for the wrong reason | see PC-F-05 |
| PC-08 | Validate a bank match dated in a locked period | **INDIRECTLY** | blocked as a side effect of line deletion | RM-F-30 |
| PC-09 | Cash-basis reversal on un-reconcile | **YES, as a date shift** | **relocated to today** | `account_partial_reconcile.py:513-514` |
| PC-10 | Exchange-difference reversal on un-reconcile | **YES, as a date shift** | relocated to `lock+1 day` | `account_move.py:5669-5674` |
| PC-11 | Manual reconcile-wizard write-off | **YES, as a date shift** | silently overridden, user warned not blocked | `account_reconcile_wizard.py:492-496, 426-429` |
| PC-12 | Auto-reconcile wizard, unbounded `from_date` | **NO** | operates back to `date.min` | `account_auto_reconcile_wizard.py:22-23, 98-99` |
| PC-13 | Cron auto-reconcile failing on a lock error | **N/A** | `UserError` swallowed at INFO | `account_bank_statement.py:145-159` |
| PC-14 | Locking a period that still contains unreconciled statement lines | **YES** | refused with a redirect | `company.py:519-528` |
| PC-15 | Full-reconcile write of `full_reconcile_id` | **NO** | **raw SQL, bypasses the ORM entirely** | `account_full_reconcile.py:52-57` |

**DENOMINATOR for the "NO" rows:** PATTERN `lock_date|_get_violated_lock_dates|_check_fiscal_lock_dates|_get_lock_date_violations`. PATH SET: `account/models/account_move_line.py` (12 hits), `account/models/account_partial_reconcile.py` (2 hits, both date-shift), `account/models/account_full_reconcile.py` (**0**), `account/models/account_bank_statement_line.py` (**0**), `account_accountant/models/bank_rec_widget.py` (**0**), `account_accountant/wizard/account_auto_reconcile_wizard.py` (**0**). UNIT: matching line. **Class A within that declared six-file scope.**

---

## 3. The three distinct behaviours, named

The prompt requires these separated. They are genuinely different, and conflating them is how this area gets mis-specified.

**PC-F-04 — REFUSE.** The operation raises. Applies to posting, re-dating and line deletion (PC-01 to PC-03). This is the only behaviour that preserves the closed period.

**PC-F-05 — RELOCATE.** The operation proceeds, and the *compensating entry* is moved forward to an open period (PC-09 to PC-11). The original stays where it is.
**This is the most consequential behaviour for P06 and it is not a control.** Undoing a settlement inside a closed period produces a reversal in an open one. Neither period's statements are individually wrong; only the pair is inconsistent, and nothing links them for a reader. `P06-B-46`.

**PC-F-06 — PROCEED SILENTLY.** The operation completes with no check at all (PC-04 to PC-06, PC-12, PC-15). **The reconciliation relation is simply not part of the period-close regime.**
Mechanically this holds because reconciliation writes `account.partial.reconcile` rows and updates `full_reconcile_id` by raw SQL, so the ORM `write` path — where the lock check lives — is never reached. Corroborated positively by the protected-field lists: `$V18E/account/models/account_move_line.py:3368-3374` names `balance, tax_line_id, tax_ids, tax_tag_ids, account_id, journal_id, amount_currency, currency_id, partner_id` — and **`amount_residual`, `full_reconcile_id`, `matching_number` and `reconciled` are all absent.**

**PC-F-07 — PC-07's indirect block fires on the wrong record.** The check reached via line deletion is scoped to `self.move_id` — the **statement line's own move**. The counterpart invoice, whose residual and payment status are being retroactively changed, is never date-checked. A statement line dated in an open period can therefore un-reconcile an invoice dated inside a hard-locked one.
**Classification: FACT VERIFIED** (the scope of `self.move_id` at `account_move_line.py:1700-1703` is unambiguous). The prior round rated the *existence* of the block medium-high confidence pending a test; **the scoping defect does not depend on that test** — whether or not the block fires, it fires on the wrong move.

---

## 4. Accounting consequence

A signed-off bank reconciliation is **not a durable fact**. After close, and without any lock-date error:
- items can be un-matched and re-matched, changing which invoice a receipt settled;
- an invoice's ageing and payment status can change retroactively;
- the cash-basis tax position of a filed period can move, with the compensating entry landing in a later period;
- none of this perturbs the inalterability hash chain, which does not cover reconciliation objects (attack A8).

**This is the single strongest finding of the P06 programme and this continuation strengthens rather than softens it.**

---

## 5. Handoff to P08

P08 is **not published** — `research/account-p08-*` is absent from origin. **PEER DEPENDENCY OPEN.**

P06 supplies these as inputs and claims no authority over the close architecture:

| # | Input to P08 |
|---|---|
| 1 | The reconciliation relation must be inside the close regime, not outside it. |
| 2 | RELOCATE is not an acceptable default; a correction spanning a close must be a single visible paired act. |
| 3 | Lock inheritance across a company hierarchy must be a declared decision, given that hierarchy members may be legally distinct (`P06-B-45`). |
| 4 | The pre-close control (no unreconciled statement lines) is a one-time gate; a post-close control is needed too. |
| 5 | No accounting-relevant field may be written by raw SQL that bypasses the guard layer. |

---

## 6. Blocker impact

| ID | Status |
|---|---|
| Attack A6 | **CONFIRMED DEFECT — strengthened.** Three behaviours now separated; the wrong-record scoping is verified independently of the untested block. |
| `P06-OQ-20` (RM-F-30 needs a test) | **narrowed** — the reliance question stands, but PC-F-07 no longer depends on it. |
| `P06-B-45` | **NEW** — lock inheritance may bind legally distinct companies. |
| `P06-B-46` | **NEW** — RELOCATE splits a correction across two periods with no link. |

---

# End
