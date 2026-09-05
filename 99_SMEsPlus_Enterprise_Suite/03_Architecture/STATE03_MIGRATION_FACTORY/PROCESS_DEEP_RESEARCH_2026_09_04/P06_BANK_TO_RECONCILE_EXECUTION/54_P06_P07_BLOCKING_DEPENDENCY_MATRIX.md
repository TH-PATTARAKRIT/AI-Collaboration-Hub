# P06_P07_BLOCKING_DEPENDENCY_MATRIX.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S15)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do NOT treat them as one group."* Each is assessed separately.

---

## 1. The three, retrieved verbatim

From `origin/research/account-p07-th-tax-compliance-2026-09-04-001`:`10_P07_CROSS_PROCESS_OWNERSHIP.md` §3. **IDs verified as `X-07`, `X-08`, `X-09`** — the only three rows whose Owner is `P06` alone and whose Status is `BLOCKING for P07`.

> `| X-07 | Payment event, date, currency, amount | P06 | The WHT tax point (S-30) and the cash-basis VAT tax point | The payment date must be the anchor of the withholding fact; today the PND reports the invoice date instead (W-C-01) | BLOCKING for P07 |`
> `| X-08 | Partial payment / allocation | P06 | Proportional withholding | The allocation must be visible to the withholding computation; today the whole invoice's WHT is taken on the first payment (W-C-02) | BLOCKING for P07 |`
> `| X-09 | Payment reversal / cancellation | P06 | Reversal of a withholding fact | A reversal must not silently remove a row from an already-filed period (A-09) | BLOCKING for P07 |`

---

## 2. `X-07` — the payment date as the withholding anchor

| Dimension | Assessment |
|---|---|
| **What P07 needs** | The payment date to anchor the withholding fact |
| **Statutory basis** | `S-30` Revenue Code s.50 — *"shall withhold income tax **at every time of payment**"*; `S-32` s.52 — remit *"**within 7 days from the date of payment**"* |
| **P07's evidence of the defect** | `W-C-01` — *"The PND period is driven by the invoice date, not the payment date. An invoice dated in one month and paid in the next is reported in the month **before** the withholding occurred, and never in the month it occurred."* |
| **Does P06 own the fact?** | **YES.** The payment event, its date, currency and amount are P06's. |
| **Does P06 supply it correctly?** | **NO, and P06 must say so.** The payment date is user-settable, and **changing it silently drops the entire withholding** (P05 `TX-03`, rated HIGH: *"Full gross is paid, no WHT journal line exists"*). |
| **Can P06 resolve it?** | **PARTIALLY.** P06 can specify that a settlement event carries an immutable date — which is also what P08 asks for (`XP-05`, `P06-B-57`). **The reporting query keys on the invoice, and that is P07's to change.** |
| **Status** | **P06 OWNED (the fact) + P07 OWNED (the reporting key) — BOTH REQUIRED** |

**PBD-F-01 — `X-07` and P08's `XP-05` are the same underlying gap seen from two processes.** P07 needs the payment date to anchor a tax fact; P08 needs the settlement event to have a date of its own. **One target requirement satisfies both**, and P06 accepts it as `P06-B-57`. **That convergence is the most useful thing in this file.**

---

## 3. `X-08` — allocation visible to the withholding computation

| Dimension | Assessment |
|---|---|
| **What P07 needs** | Per-invoice allocation visible to the WHT computation, so a partial payment withholds proportionally |
| **P07's evidence** | `W-C-02` — *"`payment_state != 'not_paid'` is satisfied by `partial`, `in_payment`, `paid`, `reversed` and `blocked`. A **partial** payment therefore causes the **whole** invoice's withholding to be reported."* Worked example `TPF-04`: a 25 Sep bill partly paid 2 Oct is reported on the **September** PND; *"The October PND … contains nothing for it."* |
| **Does P06 own the fact?** | **YES** — allocation per document is a settlement fact. |
| **Does P06 supply it?** | **The data exists; its integrity does not.** Allocation exists as partial reconciles. But the settled amount is mutated by **two mutually-unaware custom WHT subsystems** (`P06-B-13`), and P05 documents two further defects: `TX-04` (*"Core then writes the *entire* payment difference — the unpaid **principal** — to the withholding-tax GL account"*) and `TX-05` (*"**vendor underpaid**, bill left partially open, no WHT line"*). |
| **Can P06 resolve it?** | **NO alone.** P06 can specify that allocation is a first-class, per-document, immutable fact. **The `payment_state != 'not_paid'` reporting predicate is P07's.** |
| **Status** | **P11 RECONCILIATION REQUIRED** — the fact is P06's, the predicate is P07's, and the two custom subsystems belong to neither |

**PBD-F-02 — `X-08` cannot be closed by either process acting alone**, because the defect sits in a third place: two custom modules that both mutate the settled amount and do not know about each other.

---

## 4. `X-09` — reversal must not silently alter a filed period

| Dimension | Assessment |
|---|---|
| **What P07 needs** | A reversal that cannot retroactively remove a row from an already-filed tax period |
| **P07's evidence** | `A-09` — *"If the reversal returns the invoice to `not_paid`, branch 2 stops reporting it — retroactively changing a previously filed period's content with no trace"*; `A-15` — *"the **reported** figure can change without any ledger change"* |
| **Does P06 own the fact?** | **YES** — payment reversal and cancellation are P06's. |
| **Does P06 supply it?** | **NO. Reversal linkage does not exist.** `action_reject` is a bare `self.state = 'rejected'` with no cause, no bank reference, no unwind (`RPL-F-01`), and it is the same flag that removes the payment from the batch quorum (`RPL-F-02`). And un-reconciling is not lock-gated at all (attack A6) — **corroborated independently by P08 `REC-11` and P02 `P02-F-46`.** |
| **Can P06 resolve it?** | **PARTIALLY.** P06 specifies the returned/failed-payment lifecycle (`30_`): a reversal is an ingested external event that supersedes rather than erases, carries a cause, and restores the residual. **Whether a filed period may change at all is a statutory question.** |
| **Status** | **STATUTORY HOLD + P06 OWNED (the mechanism)** |

**PBD-F-03 — `X-09` is the one of the three with a hard statutory component**, and P06 takes no position on it. P07's own posture is identical, and P05 reached the same HOLD independently. **Three processes hold the same statutory question in the same state — that is the correct outcome, not a gap.**

---

## 5. Consolidated

| ID | Fact owner | Defect location | Can P06 close? | Status |
|---|---|---|---|---|
| **`X-07`** | P06 | P06 (mutable date) **+** P07 (reporting key) | partially | **P06 OWNED + P07 OWNED** |
| **`X-08`** | P06 | two custom WHT modules **+** P07 predicate | no | **P11 RECONCILIATION REQUIRED** |
| **`X-09`** | P06 | P06 (no reversal linkage) **+** statute | partially | **STATUTORY HOLD + P06 OWNED** |

**Not one of the three is fully resolvable by P06, and not one is fully resolvable by P07.** P07 said as much: `P07-D-21` — *"`W-C-01`, `W-C-02`, `W-M-02` **cannot be closed by P07 alone**"*.

---

## 6. What P06 supplies, stated constructively

The round-3 challenge (E3-C-04) recorded that accepting a dependency and declaring it broken is honest but not helpful. **These are the requirements P06 commits to, which close the P06 half of all three:**

| ID | Requirement | Closes |
|---|---|---|
| `P07-R-01` | A settlement event carries **its own immutable date**, distinct from the documents it settles, and that date determines every downstream period — tax and accounting alike. | `X-07`, and P08's `XP-05` |
| `P07-R-02` | Allocation is a **first-class per-document fact**, written once, immutable, and readable by any consumer. No module may mutate a settled amount after the fact. | `X-08` (P06 half) |
| `P07-R-03` | A reversal is a **new event linked to the event it reverses**. It supersedes and never erases. It carries a cause, a counterparty reference and its own date. | `X-09` (P06 half), and P08's `KRN-INV-01` |
| `P07-R-04` | A settlement fact, once reported to an authority, is **immutable in that period**. A later correction produces a new fact in a new period, visibly linked. | the mechanism half of `X-09` |

**PBD-F-04 — `P07-R-01` and `P07-R-03` are the same two requirements P08 asked for.** Three peer processes converge on: **the settlement event needs an identity, a date and a reversal link.** That is a stronger design signal than any single process could produce, and it is the clearest actionable output of the whole peer round.

---

## 7. Cross-process duplicate-ownership risks P07 flags

`10_P07_CROSS_PROCESS_OWNERSHIP.md` §5, recorded not adjudicated:
- `DUP-01` — *"The withholding fact is created in **P06** (payment) but reported from a P01 artefact (the bill line). **Two processes hold a claim on one tax fact.**"*
- `DUP-02` — the sales-side withholding fact *"is created in **P06** … and is **claimed by no reporting process at all**"*
- `DUP-03` — *"Two withholding frameworks can both act on one **P06** payment event."*

**P06 confirms `DUP-03` from its own evidence** (`P06-B-13`: two mutually-unaware custom WHT subsystems mutate the settled amount). **`DUP-01` and `DUP-02` are P07/P01 matters and P06 takes no position**, noting only that P01 is still unpublished, so `DUP-01` cannot be reconciled by anyone yet.
