# 73 — P05 CANDIDATE ACCOUNTING EVENT OUTPUT

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-08` · **PHASE S CANDIDATE — NOT A FINAL CONTRACT**

## 1. The Three-Way Separation

| Layer | Question | Owner |
|---|---|---|
| **P05 business event** | *What happened in the business?* | **P05** |
| **Accounting-relevant output** | *What must the ledger be told?* | **P05 produces it** |
| **Ledger truth, period architecture, statements** | *How is it recorded, controlled, closed and presented?* | **P08 — not researched here** |

> P05 may state that a cost of a given amount, for a given company, at a given date, against a given
> account, arising from a named business event, must be recognised — **and nothing beyond that.**
> Whether the ledger permits later mutation, how periods lock, and how statements are built are P08's.

## 2. Candidate Accounting Event — `CO-02`

| Element | P05 owns | Evidence |
|---|---|---|
| Business event reference | **should — but no durable identity exists** | four severing paths |
| Cost account | yes — resolved through a four-step fallback | FACT VERIFIED |
| Amount, currency, company | yes | FACT VERIFIED |
| **Recognition date** | yes, **and it is defective** | derived from the **clock** in two of three branches; one branch computes the first open period *after* a lock and books there | 
| Counterparty | yes | FACT VERIFIED |
| Tax split (recoverable) | yes, **forced price-included** regardless of configuration | FACT VERIFIED |
| Attribution | yes — **debit line only** | FACT VERIFIED |
| Reversal linkage | **NO** | reversal severs the link |

## 3. What P05 Must Not Claim

| Claim | Owner |
|---|---|
| That the entry is immutable / hash-protected | **P08** |
| That the period may be closed | **P08** |
| Statement classification or presentation | **P08** |
| Whether the ledger permits force-cancellation | **P08** — the observed core gap is routed, not owned |
| Statutory deductibility of the cost | **P07** |

## 4. Candidate Requirements

| ID | Requirement |
|---|---|
| `AER-01` | The accounting event carries an **immutable business-event identity**. |
| `AER-02` | The **recognition date derives from a document fact**, never from the clock, and never steps over a closed period to find an open one. |
| `AER-03` | Emitting an accounting event is a **distinct authorisation** from approving a claim. |
| `AER-04` | A **correction produces a new linked event**, never a mutation or a detachment. |
| `AER-05` | Tax treatment on a cost line **follows the tax's own configuration**, not a blanket coercion. |

## 5. Boundary

**P08 not researched.** No period-close, statement-construction or ledger-integrity architecture is
proposed here. `CH-01` carries the event; `CH-07` is the inbound period/lock state P05 consumes.
