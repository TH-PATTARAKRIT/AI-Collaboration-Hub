# P08_CORE_RECON_HANDOFF_PACK — for Core Accounting Reconciliation

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

This pack is what Core Accounting Reconciliation needs from P08 and nothing more. It is not an approval, not a design authority, and not a gate.

## 1. What P08 hands over

| # | Artefact | File |
|---|---|---|
| 1 | The accounting kernel model and the source-of-truth determination | `03` |
| 2 | The scope-ownership matrix — every material object assigned `PLATFORM` / `TENANT` / `COMPANY` | `01` |
| 3 | The declared reference root set, with the three root-set-wide negative claims | `01A` |
| 4 | Chart, identity, posting, manual GL, settlement, close, measurement, report models | `02`, `04`–`11` |
| 5 | The business-event register and the ledger contract every producer must satisfy | `12` |
| 6 | The accounting-event register — fifteen events the ledger emits on its own account, ten of them invisible | `13` |
| 7 | The event-to-ledger matrix, with debit and credit deliberately withheld | `14` |
| 8 | The orphan and duplicate posting attack — twenty-two attacks, none stopped outright | `16` |
| 9 | Contradictions, dependencies, source links, revisions | `17`–`19`, `21` |
| 10 | The Layer 2 evidence quarantine | `LAYER2_EVIDENCE_QUARANTINE/` |

## 2. The ten reconciliation questions P08 answers

| # | Question | P08's answer |
|---|---|---|
| 1 | What is the accounting source of truth? | The journal item. Everything above it in the chain is transient; everything below it is a projection or a reading. |
| 2 | Is the general ledger a store? | No. It is a reading of the journal items. There is no separate ledger table. |
| 3 | Is the subledger a store? | No. It is a projection of journal items net of the matching graph — **and, in the party dimension, a projection of the matching graph itself**. |
| 4 | Is the financial report derived? | Mostly. Three stored value classes are **not** derived from journal items, and no ledger control reaches them. |
| 5 | Is the general ledger original or derived truth? | **Both, and nothing marks which.** Under a document-generated entry it is derived with a recoverable origin; under a manual journal it is the first and only assertion. No field distinguishes them. |
| 6 | Can one business fact produce two accounting effects undetected? | Yes. There is no accounting-event identity to be *one* of — `A VERIFIED ABSENCE` across all 22 declared roots. |
| 7 | Is a posted fact immutable? | No. Nine header attributes are protected and the protection is waived by a caller-supplied parameter; a posted journal item's account, counterparty, label, reference and cost allocation are editable in place. |
| 8 | Is the entry balanced? | Not guaranteed. The assertion is application-level, suppressible by a caller-supplied parameter, and asserted in the reporting currency only. **No database constraint enforces it in any of the 22 declared roots.** |
| 9 | Is a closed period closed? | There is no period object. Closing is the movement of a date, reversible by writing an earlier one, leaving a field-change entry as its only evidence. |
| 10 | Will a past-period statement re-run to the same number? | No. At least eleven routes change it, of which two are unguarded master-data edits on accounts that already carry postings. |

## 3. The invariants Core Reconciliation should carry forward

0. **The accounting identity: the items of an entry sum to zero in every currency frame, enforced at the persistence layer, with no caller-supplied waiver.** *(`KRN-INV-00`, added after independent review — the draft's invariant list omitted the very invariant the package calls its most important finding.)*
1. `ONE FACT → ONE ACCOUNTING EFFECT` — enforceable only at the accounting-event node, which must exist.
2. A posted financial fact is immutable, **at the persistence layer**, with no caller-supplied waiver.
3. Every posted fact carries its provenance: event, instruction, actor, measurement context, tenant, company.
4. Correction is by new fact only.
5. **A tenant-scope mutation may never rewrite a company-scope posted fact, and may never silently change a company-scope issued statement.**
6. Every object with a financial effect has exactly one owning company; where ownership cannot be proven, the operation is denied. *(Now `KRN-INV-08` in the kernel model — the draft carried it here and not there.)*

## 4. The six things that must be reconciled with peers

| ID | With | Question |
|---|---|---|
| `HO-01` | P01–P07, P09 | the recognition point of every business event — P08 supplies the ledger contract, the producers supply the point |
| `HO-02` | P03 | where the valuation boundary sits between an inventory fact and a ledger fact |
| `HO-03` | P06 | the settlement event's own date, which P08 requires and the benchmark has none of |
| `HO-04` | P07 | the tax point as a carrier distinct from the accounting date; and the ownership of statutory statement layouts |
| `HO-05` | P09 | whether an analytic dimension is a fact or an attribution — this decides the membership of the immutable core |
| `HO-06` | P11 | the `PLATFORM` / `TENANT` / `COMPANY` assignments, especially the three splits the benchmark does not make |

## 5. What P08 could not close, and what would close it

| Item | What would close it |
|---|---|
| End-to-end reachability of the suppression parameters | one executed call against a running instance |
| Deployment status of the custom access-check override | the deployed module registry |
| Residual-drift, reconcilability-recompute, snapshot-on-decrease, rate-type-set behaviours | one runtime trial each |
| Which of the 22 roots is targeted | a programme declaration — `P08-BD-05` |
| The 67 unexamined custom modules | a bounded isolation sweep — **the highest-value remaining search in this domain** |
| Thai statutory requirements | authoritative evidence, Accounting-Tax track |

## 6. What P08 does not hand over

Debit and credit per business event. Those belong to the producing processes and are marked `UNKNOWN — EVIDENCE REQUIRED` in `14`. When each producer completes its posting pattern, **that matrix is where it is recorded**, so the ledger-side constraints established here travel with it.

## 7. Terminal state

**`HANDOFF PREPARED — CORE ACCOUNTING RECONCILIATION`.** The ledger contract is stated, the evidence is preserved, and the open items are named.

*(Corrected after independent review: the draft used a readiness label, which this session's own governance prohibits — a readiness declaration for a module, wave, state or gate is not available to this session in any form, including one immediately followed by a disclaimer.)*

This package declares no readiness, no approval, no completeness, no convergence, no freeze, no merge and no implementation authority. Its gate position is a **recommendation** and is stated in `26_P08_FINAL_RESEARCH_GATE_REPORT.md`. Boss alone decides.
