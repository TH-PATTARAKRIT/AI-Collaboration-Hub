# 74 — P05 CORRECTION / REVERSAL BOUNDARY V3

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-09` · **PHASE S CANDIDATE — NOT A FINAL CONTRACT**

## 1. What Can Be Corrected, and What Happens

| From state | Mechanism | Business truth after | P05 boundary effect |
|---|---|---|---|
| `captured` / `claimed` | free edit | fully valid | none |
| `submitted` | withdraw / refuse | claim void | none |
| **`authorised`** | **refuse** | claim void | **the draft accounting artefact is destroyed** — no trace that recognition occurred and was withdrawn |
| **`recorded`** | **reset to draft** | claim returns to draft | artefacts reversed, then **detached**; the claim shows no artefacts and reports unsettled, while the ledger retains both original and reversal as orphans |
| `recorded` | direct field mutation | **claim and ledger silently diverge** | amount, currency, date, category remain writable with **no propagation** |
| `settled` | reversal of settlement | obligation re-opens | P06 territory |

## 2. The Three Cancels

| Cancel | Semantics | Consequence |
|---|---|---|
| **Refuse a claim** | operational rejection | destroys the draft artefact |
| **Cancel the accounting artefact** | accounting rejection | **severs the link to the claim** |
| **Force-cancel from a non-accounting document** | neither | bypasses the integrity lock — **`EXTERNAL DOMAIN BOUNDARY` → P08** |

> **`CR-01` FACT VERIFIED — P05.** Three mechanisms named "cancel" have three different meanings and
> three different consequences for the audit trail. **A business user cannot tell which one they are
> invoking.**

## 3. The Central Defect

> **`CR-02` FACT VERIFIED — P05. P05 publishes no correction event.**
>
> Every consumer of a P05 output — settlement, ledger, attribution, tax — learns of a correction only
> by re-reading P05's current state, and after a reset that state **no longer references the artefacts
> it produced**. `CO-06` is therefore a **candidate output with no producer** (`ORPH-01`).

Attribute-by-attribute effect at the P05 boundary:

| Attribute | After correction |
|---|---|
| Payable | withdrawn, but consumers are not told |
| Accounting | reversed or destroyed; lineage severed |
| Analytic | reverses with the debit line; **never existed** on the float/advance chain |
| Tax/WHT | **no reversal hook exists in any withholding module** (class A, six modules) — a completed certificate can outlive a cancelled withholding line |
| Evidence | attachments survive independently of the severing |

## 4. Candidate Handoff Requirement

`CO-06` — a **correction event** carrying: original event identity · what changed · new values ·
reason · actor · timestamp · and an explicit statement of which downstream assertions are withdrawn.

**Required by:** `CH-01` (ledger), `CH-02` (attribution), `CH-03` (settlement), `CH-04` (tax).
**Evidence status:** `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED`. Derived from the defect, not observed.

## 5. Candidate Requirements

| ID | Requirement |
|---|---|
| `CRR-01` | Correction is **always a new linked fact**, never a mutation and never a detachment. |
| `CRR-02` | A posted P05 fact is **closed to amendment**. |
| `CRR-03` | Each cancel-like operation has a **distinct name and a distinct published event**. |
| `CRR-04` | A correction **publishes an event to every consumer** that received the original. |
| `CRR-05` | Correction lineage is **immutable and non-severable**. |

## 6. Boundary

Ledger-side integrity policy, and whether a hashed entry may be force-cancelled, are **P08's**.
`VB-01` applies to any statement about the vendor-advance module's correction behaviour: that source
copy carries version `1.0.0`, matching **none** of the three deployed generations — so its behaviour
is **not** established for any deployed generation. Recorded, not researched further.
