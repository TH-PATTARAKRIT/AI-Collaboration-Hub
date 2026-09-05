# P08_PERIOD_CLOSE_CONTROL_RECONCILIATION

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T10`

Reconciles P08's period-close model with peer evidence from P04, P06 and P10, and with the database evidence acquired in Phase C. **P08 does not decide the final policy; it establishes what the evidence proves.**

## 1. The six dates the directive requires be distinguished

| Concept | Carrier in the benchmark | Verified |
|---|---|---|
| Business event date | the source document's own date | present, per producing process |
| **Accounting recognition period** | **no carrier** — there is no period object at all | `A VERIFIED ABSENCE`, 22 of 22 roots |
| Posting date | the row's creation stamp | present, but it is a technical audit column, not an accounting attribute |
| Journal date | the entry's accounting date | present, and it is the **only** period attribution the ledger has |
| Correction period | no carrier — a correction lands in whatever month its date falls in | `A VERIFIED ABSENCE` for a distinct carrier |
| Report period | a date-range predicate evaluated at query time | present, derived |

**Four of six have no carrier.** The ledger collapses recognition, correction and reporting period into one field: the entry's accounting date.

## 2. What the controls do, and what the deployed data shows they did

| Control | What it does | What the databases show |
|---|---|---|
| Fiscal-year lock | relocates a violating entry's date forward rather than refusing | **set on 0 of 89 companies** in 3 of 3 databases |
| Irrevocable lock | same relocation on the posting path; refuses only a reopen | **the column does not exist** in the production-scale database |
| Sale / purchase / tax locks | journal-type scoped | not set |
| Tamper seal | the only unconditional immutability in the system | **enabled on 0 of 64 journals; carried by 0 of 169,143 posted entries** |
| Retention of posted facts | prevents deletion of once-posted entries | **the column does not exist in any of the three databases** |

**The period-control layer is fully present in source and fully unengaged in deployment.** That is the single most important reconciliation in this file, and it re-frames every control finding in the package: the question is not only whether a control can be bypassed, but whether it was ever switched on.

## 3. Measured consequence, in the database with no lock set

| Measurement over 169,143 posted entries | Value |
|---|---|
| Posted more than 30 days after their accounting date | 28,847 |
| Posted more than 90 days after | 14,017 |
| **Posted more than a year after — i.e. backwards across at least one fiscal-year boundary** | **6,418** |
| Largest gap between accounting date and creation | **6,701 days** |
| Accounting date in the future relative to creation | 22,162 |

P08 asserts nothing about whether any individual entry was improper. What is verified is that **no control was in a position to distinguish a legitimate late posting from an improper one**, because none was configured.

## 4. Peer reconciliation

| Peer | Their finding | P08 disposition |
|---|---|---|
| **P04 — Acquire-to-Retire** | An entry aimed at a locked period is **silently re-dated forward and posted**, including for the irrevocable lock; the product's own test asserts a full annual depreciation charge crossing a fiscal-year boundary. The same lock **hard-refuses** an asset re-evaluation | **CONFIRMS P08**, verified independently by P08 against source. Recorded as `P08-PEER-01`/`-02` and `P08-CONTRA-16`. **Extended by Phase C**: in the deployed database the lock is not set at all, so the relocation path was never even reached |
| **P06 — Bank-to-Reconcile** | Reconcile and unreconcile behaviour around the lock date | **CONFIRMS P08.** P08 verified independently that **no lock guard exists inside either settlement model** — `A VERIFIED ABSENCE` now across 21 of 21 roots. Un-settling in a closed period is unconstrained on the direct paths; only the compensating entry is date-shifted |
| **P10 — Time-Based Recognition** | Recognition period versus posting date; the recognition event is collapsed into the posting act | **CONFIRMS AND EXTENDS P08.** P08's independent finding that there is **no accounting-period object in 22 of 22 roots** is the structural cause of P10's observation. Recorded as a shared root cause, not two findings |
| **P03 — Manufacture-to-Cost** | Machine/manufacturing cost posting and work-in-progress ownership | **PEER-OWNED.** P08 supplies the ledger contract; the posting pattern is P03's. `PEER DEPENDENCY OPEN` |
| **P05 — Expense-to-Pay** | Journal cancellation, mutation and reconciliation integrity | **CONFIRMS P08** on cancellation silently returning an entry to draft and destroying settlements. `PEER DEPENDENCY OPEN` for the expense-specific paths |
| **P09 — Plan-to-Analyze** | The analytic dimension is schema, not data; analytic record versus economic effect | **EXTENDS P08.** Bears on `P08-BD-09` — whether an analytic dimension is a fact or an attribution, which decides membership of the immutable core |

**Contradictions are preserved, not harmonised.** No peer finding was rewritten to agree with P08, and P08 changed its own wording where a peer was right — see the revision log.

## 5. What P08 does **not** decide

The policy questions remain Boss-controlled and are stated, not answered:

| ID | Question |
|---|---|
| `P08-BD-06` | Is the year-end result posted, or derived at report time? |
| `P08-BD-16` | **New.** Should a period lock **refuse** a violating posting, or relocate it? The benchmark relocates; every peer that met the behaviour called it a defect; but refusing changes the operational burden materially and that is a business decision |
| `P08-BD-17` | **New.** Should the platform **require** a period-control configuration, given that the deployed evidence shows none was ever set? A control nobody configures is equivalent to a control that does not exist |
