# 16 — P05 AAS-03 INDEPENDENT CHALLENGE

`LAYER 2 — AUDIT QUARANTINE`
**This file and `11`, `15 §1`, `21` govern over every headline table elsewhere in this package
(`ER-AASR-1`).** Where a summary differs from §4 below, §4 governs.

## 1. Design of the Challenge

Four AAS-03 experts, dispatched in parallel, with **disjoint** scopes and no visibility of each
other's work. Each was given the primary research's findings as a brief and instructed:

> *"YOUR JOB IS TO DISPROVE, NOT TO CONFIRM."*

Every brief additionally carried four standing instructions, applying the project's method controls:
1. Re-derive each finding from source; cite only what you personally read.
2. Search hard for the guard, constraint, record rule, view attribute, test or override that makes
   the claimed defect **unreachable**, using multiple naming variants and separators.
3. Return a verdict from `CONFIRMED / OVERSTATED / CONTRADICTED / NOT DECIDABLE FROM SOURCE`.
4. **"If any path or line number in this brief is wrong, report it as a finding."**

Negative-claim discipline, unit/pattern/path-set declaration and the prohibition on `PASS`/`FAIL`
verdict wording were mandated in every brief.

| Expert | Scope | Findings in brief | Verdicts returned | New findings |
|---|---|---|---|---|
| 1 | Core expense engine — `hr_expense` and its five satellites | `F-01`, `F-19`..`F-28` | 11 | 18 |
| 2 | Petty cash, the custom fork, and negative claims `NC-A`/`NC-B` | `F-02`..`F-05`, 2 negatives | 6 | 11 |
| 3 | Employee advance and liquidation | `F-06`..`F-13` | 8 | 16 |
| 4 | Tax, WHT and settlement | `F-14`..`F-18`, `F-29`, `F-30` | 7 | 15 |

## 2. Aggregate Result

| Measure | Count |
|---|---|
| Primary-research findings put to challenge | 32 |
| **Confirmed as stated** | 14 |
| **Confirmed but UNDERSTATED** (the reviewer made the finding worse) | 6 |
| **OVERSTATED** — wording narrowed, substance survived | 4 |
| **Wrong mechanism or wrong citation** — conclusion survived, evidence replaced | 4 |
| **Severity CONTRADICTED** — re-classified downward | 2 |
| **Framing INVERTED** — the reviewer identified a different, worse root cause | 2 |
| Self-disproofs re-tested and upheld | 3 (`F-29`, `F-30`, `F-31`) |
| **New material findings from reviewers** | **60** |
| Errors found in the primary research's own brief | **18** |

> **The primary research authored 32 findings and was corrected on 12 of them.** Every one of those
> corrections came from independent review; none came from the author. This is the fifth consecutive
> SMEsPlus round in which that has been the pattern.

## 3. Errors Found in the Primary Research's Brief

Recorded in full because the brief was written by the author of the claims it bounded.

| # | Error | Raised by | Disposition |
|---|---|---|---|
| 1 | `F-23` cited `hr_expense_sheet.py:247-250` for the company-paid journal selection; those lines are `_compute_from_account_move_ids`. Correct: `:276-277` + `hr_expense.py:890`. | 1 | Corrected in `02 §2.1` |
| 2 | `F-22` "lock-date protection is asymmetric" implies enforcement differs; it does not. Only the **default date derivation** is asymmetric. | 1 | Corrected in `03 §3.2` |
| 3 | `F-25` consequence overstated (`duplicate_expense_ids` is not stored) **and** understated (`currency_id`, `company_id` also omitted from the depends). | 1 | Corrected in `09 DUP-01` |
| 4 | `F-01` line range cites the method (`20-28`) for a set literal spanning `21-25`. | 1 | Cosmetic; noted |
| 5 | `F-28`'s sudo citation covers only the first of three `sudo()` creates (`:760`, `:769`, `:773`). | 1 | Noted |
| 6 | `F-19` is understated — nine fields are view-only-protected, the apparent model-side guard is an `@api.onchange` never registered as an inverse, and the employee's own record rule has no state clause. | 1 | Strengthened in `11 C-20`, `10 §4.1` |
| 7 | **`F-02`'s consequence citation is the wrong mechanism.** `_get_expense_account_destination` is never called on the petty-cash path; the credit comes from core `_compute_needed_terms`, because hr_expense's override of it is gated on `company_account`. | 2 | Corrected in `05 §6`, `01 §4.1` |
| 8 | `F-02` is understated — it is one of **two** dead paths in the module, and the module's tests are a non-executing v14 artefact. | 2 | Strengthened in `05 §6`, `01 §4.4` |
| 9 | `F-05` claimed 3 divergences; **9** material ones exist, and the most consequential (the missing `super()` call) was absent. Conversely divergence (a)'s severity was overstated — no caller consumes the return value. | 2 | Corrected in §4.2 below |
| 10 | `F-03` is one-sided: the balance compute **is** company-filtered because it is not `sudo()`. The genuinely unscoped access is a different, `sudo()` call the brief did not cite. | 2 | Corrected in `02 §4`, `22 §3 R-02` |
| 11 | `F-03` line range `38-49` should be `38-50`. | 2 | Corrected |
| 12 | **`NC-A` was bounded to `R1` while declaring `R2` in its own path set.** `R2` yields 40 files. The claim was contradicted by a root inside its own declared boundary. | 2 | `21 NC-E-05` |
| 13 | `NC-B` incomplete — misses `account.journal.type == 'credit'` and its auto-provisioned card account, reachable from the company-paid expense path. | 2 | `21 NC-E-06`, corrected in `02 §5` |
| 14 | The brief declared a path set but **no unit**, so its file counts were not comparable. | 2 | Corrected in `21 §1` |
| 15 | **`F-07`'s mechanism is a factual error.** The advance line's `account_id` is never passed to the bill; resolution is core `_compute_account_id`, whose chain includes a **product-category** fallback the brief omitted entirely. | 3 | Corrected in `02 §3`, `05 §3` |
| 16 | `F-06` over-reaches on three limbs (sequence integrity, payment state, and the `unmodifiable_fields` skip — the last being true but inert). | 3 | Corrected in `10 EC-13` |
| 17 | `F-11` severity wrong — `@api.model` `create` is auto-wrapped and handles list input correctly. | 3 | Re-classified in `10 EF-10` |
| 18 | `F-13`'s framing is inverted — Odoo tolerates the cycle; the defect is a **missing** dependency. | 3 | Corrected in `08 §3` |
| 19 | `F-30`'s citation range `2-4` should be `2-7`; the `domain_force` the whole disproof rests on is at `:6`. | 4 | Corrected in `21 NC-E-02` |
| 20 | `F-29`'s disproof is correct but under-specified and rests on a **local uncommitted edit**; the entire test suite still targets the superseded branch. | 4 | Corrected in `07 §4`, `21 NC-27` |
| 21 | `F-18` is understated — the latch does not merely short-circuit, it **restores the gross amount**, so a payment-date change silently drops the whole WHT. | 4 | Escalated to `07 TX-03` |
| 22 | `F-14` incomplete in attribution and consequence — the inversion is inherited, the correct classifier is a local addition, and the two are bound together in one widget. | 4 | Extended in `07 TX-10`, `TX-11` |
| 23 | `F-16` understated — `wht_amount` drives the net figure printed on the vendor remittance advice. | 4 | Escalated to `07 TX-08`, `TX-09` |
| 24 | `F-17` severity overstated — a non-stored many2many nulls `relation` before validation, so there is no schema consequence. | 4 | Downgraded |
| 25 | **Scope gap:** the brief's declared roots omit `ENT18/addons/l10n_th_reports`, an `auto_install` second WHT implementation. Any conclusion about Thai withholding coverage that ignores it is incomplete. | 4 | Added as `07 §2`, `TX-01` |

## 4. Per-Finding Verdicts

### 4.1 Expert 1 — Core Expense Engine

| Finding | Verdict |
|---|---|
| `F-01` payment guard defeated by a missing comma | **CONFIRMED (exact).** Independently AST-evaluated. Searched for a compensating guard across the module: `write()` is the only override, `@ondelete` protects deletion only, no view-level readonly covers `journal_id` on expense payments. |
| `F-19` post-posting mutability | **CONFIRMED and UNDERSTATED** — see §3 #6 |
| `F-20` three paths sever the claim↔entry link | **CONFIRMED**, with one correction (`_reverse_moves` filters to `own_account`; `button_cancel` writes on **all** of `self`) and one addition (both also clear `ref`; after a reset **no** entry retains the link) |
| `F-21` payable/receivable check disabled | **CONFIRMED (exact).** No re-imposition found elsewhere. |
| `F-22` lock-date asymmetry | **OVERSTATED** — see §3 #2. Two amplifications survive: the lock is consulted only in the third branch, and `accounting_date` is a plain writable Date whose pre-setting skips the lock-aware computation entirely. |
| `F-23` unreachable fallback | **CONFIRMED as to substance; citation wrong** — see §3 #1 |
| `F-24` optional `vendor_id` on a supplier payment | **CONFIRMED (exact).** The view confirms rather than guards: `vendor_id` is rendered with no `required` and no `readonly`. |
| `F-25` duplicate-detection depends | **OVERSTATED and UNDERSTATED** — see §3 #3 |
| `F-26` employee payable = vendor payable | **CONFIRMED.** Mitigation the brief omitted: the payable property is read `.with_company()`, so it is company-scoped. The finding stands. |
| `F-27` partner / commercial-partner split | **CONFIRMED (exact).** The shipped mitigation is a **view-level warning only**; there is no block. |
| `F-28` entries created at approval | **CONFIRMED (exact).** `_do_refuse` correctly raises if any move is posted. |

### 4.2 Expert 2 — Petty Cash and the Custom Fork

| Finding | Verdict |
|---|---|
| `F-02` petty-cash GL redirection is dead code | **UPHELD on four independent lines, and UNDERSTATED. Mechanism citation wrong** — see `05 §6` for the full four-limb argument and §3 #7–#8 |
| `F-03` no company scoping on `petty.cash` | **UPHELD**, with one mitigant and one aggravator the primary research had backwards — see §3 #10 |
| `F-04` orphan file | **UPHELD, and it is a *maintained* orphan** — the dead files were **edited during the v18 port** (`attrs` → `invisible=` conversion), i.e. someone maintained dead code believing it live. Were the orphan view ever re-added, it and the live view both `xpath` the **same anchor** and both inject `is_petty_cash` → duplicate-field view error. |
| `F-05` forked `_do_create_moves` | **UPHELD on all three claims; enumeration INCOMPLETE (3 claimed, 9 found); one severity overstated.** The nine divergences: (D1) intended mode grouping; (D2) injects `preferred_payment_method_line_id`, whose own compute will overwrite it on any partner/company recompute; (D3) **payments created before moves with no `move_id`**, so the payment's journal, company and outstanding account all resolve blind to it; (D4) reassigns `moves_sudo` — real but **blast radius is the return value only**, since no caller in `ENT18` consumes it; (D5) writes `state:'in_process'` in the same write as `move_id`, dodging the second-entry generation and the `_check_move_id` guard, and leaving a payment `in_process` against a **still-draft** move whose lines have zero residual — a path that can flip the payment to `paid`; (D6) per-record rather than batched; (D7) **omits the upstream `journal_id` write whose own comment says it prevents a recompute chain that voids the lines' company currency**; (D8) a now-no-op union; (D9) **the fork never calls `super()`**, so `sale_expense` and `project_sale_expense`, which both override `_do_create_moves` to assign analytic accounts before delegating, are **silently bypassed** if this module sits earlier in the MRO — reinvoiceable and project expenses lose their analytic distribution. |
| `NC-A` | **CONTRADICTED as an `R1`-wide claim; substance survives with a corrected boundary** — see §3 #12 |
| `NC-B` | **UPHELD as "no process model", INCOMPLETE as written** — see §3 #13 |

### 4.3 Expert 3 — Employee Advance and Liquidation

| Finding | Verdict |
|---|---|
| `F-06` raw `state='cancel'` write | **UPHELD AND ESCALATED on one limb; three limbs DISPROVED.** Escalation: the **inalterable-hash lock is bypassed** — `'state'` is not a member of `_get_integrity_hash_fields()` — so a hashed journal entry can be forced to `cancel`, and reconciliation partials survive against it. Disproved: sequence integrity, payment state, and the `unmodifiable_fields` skip. Reachability corrected: neither button is reachable from the documented happy path, but `state` carries no ORM guard, so `write({'state':'approved'})` on a `done` request re-exposes **Reject**. ACL bound: the operator must hold `account.group_account_invoice`. |
| `F-07` advance recognised as expense at disbursement | **UPHELD on substance; MECHANISM WRONG** — see §3 #15. Double recognition is **reachable and unblocked** by two routes, and a third route (the clearing wizard) **fabricates a bank receipt**. |
| `F-08` clearing credits line 0 only | **UPHELD, and the failure mode is worse:** lines created outside the form onchange have `account_id = False`, so the clearing entry collapses to a debit and a credit **on the same bank account** — nets to zero, posts cleanly, and still flags the advance cleared. |
| `F-09` candidate set scoped to the current user | **UPHELD AND ESCALATED** — the scoping is a client-side domain only; `apply()` validates nothing, and the wizard's ACL grants CRUD to **all users**. |
| `F-10` server date | **UPHELD.** The same module uses `context_today` in two other places, so it is an inconsistency, not a convention. |
| `F-11` single-signature `create` | **FACT UPHELD, SEVERITY CONTRADICTED** — see §3 #17 |
| `F-12` approver through a One2many | **UPHELD**, and material because `button_approved` gates on it. |
| `F-13` circular stored computes | **UPHELD, but the cited cycle is NOT the operative defect** — see §3 #18 |
| *Additional task:* is `advance_expense_request_line.account_id` ever read? | **HYPOTHESIS DISPROVED** — it **is** read, in exactly two places, both the credit side of a clearing entry. It is written only by an onchange, never validated, never required — which is precisely why `F-08`'s fallback failure is reachable. |

### 4.4 Expert 4 — Tax, WHT and Settlement

| Finding | Verdict |
|---|---|
| `F-14` inverted receipt move types | **CONFIRMED, SETTLED DEFINITIVELY, EXTENDED.** Three independent core authorities agree on the semantics; the mapping is genuinely inverted and there is no reason it is written that way. |
| `F-15` `self` assignment in a per-record loop | **CONFIRMED**, "last value wins for all records" is correct and it does **not** raise — verified against the ORM. **Severity raised**: the corrupted stored value drives a printed settlement document. |
| `F-16` bare Float, no currency | **CONFIRMED and EXTENDED** — see §3 #23 |
| `F-17` label in the `relation` slot | **CONFIRMED as a coding defect; SEVERITY DOWNGRADED** — see §3 #24 |
| `F-18` latched recompute | **CONFIRMED and MATERIALLY WORSE THAN STATED** — see §3 #21, plus a companion defect in the opposite direction. |
| `F-29` self-disproof (WHT on the bill path) | **The disproof is CORRECT, but under-specified and rests on a local uncommitted edit** — see §3 #20 |
| `F-30` self-disproof (WHT ACL/rule) | **The disproof is CORRECT; citation range wrong** — see §3 #19. And the ACL/rule being present **does not make the model company-safe**: the rule is what creates the duplicate (`07 TX-17`). |

## 5. Reviewer Self-Correction

One reviewer retracted a claim of its own mid-report: Expert 4 initially suspected that a re-declared
`@api.depends` truncated the dependency set, then established from `ENT18/fields.py:557-593` that
`get_depends` uses `resolve_mro(...)` and **unions** `_depends` across the whole MRO, and withdrew
that limb — leaving the finding resting on assignment order alone (`07 TX-05`).
Recorded because a reviewer who corrects itself in writing is evidence the challenge was real.

## 6. Consequence for `EC-07`

`EC-07` requires **two consecutive fresh independent passes** with no new material population,
no new material finding class, no new gating unknown, no reopened tolerance-zero issue and no new
Gate-changing contradiction.

This was **pass one**. It produced **60 new material findings, 7 new tolerance-zero boundaries, a new
material population (`l10n_th_reports`, a second WHT subsystem the primary research had not scoped),
and 6 new gating or near-gating unknowns** — from every reviewer that reported.

**`EC-07` is therefore not merely unsatisfied; its counter has not started.** The next pass would be
pass one of two, not two of two.
