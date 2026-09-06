# P08_POSTING_FINALITY_AND_CORRECTION_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · answers `CQ-P08-03` and `CQ-P08-06`

Consolidates `05`, `07`, `36`, `43`, `44`, `47`, `48` under the Phase-S dispositions. **No new research; explicit revision lineage.**

---

## 1. The posting act — what it does and does not do

| # | Behaviour | Evidence | Class |
|---|---|---|---|
| 1 | Assigns the entry number | S18 source; D16 data | `FACT VERIFIED` |
| 2 | Moves the state to posted | S18; all three databases | `FACT VERIFIED` |
| 3 | Asserts double entry **in the reporting currency only** | S18 | `FACT VERIFIED` |
| 4 | **Does not assert balance in the transaction currency** | S18 — no layer does | `FACT VERIFIED` |
| 5 | **Does not seal** unless the journal opts in — and no transacting journal does | **0 of 29** | `FACT VERIFIED` |
| 6 | **Does not make the entry immutable** | the state it would protect is outside the seal's field set | `FACT VERIFIED` |
| 7 | **Relocates a violating date rather than refusing it** | S18, asserted by the product's own test | `FACT VERIFIED` |
| 8 | **Derives the accounting date for every non-sale document, lock or no lock** | S18 mechanism; D16 20.95% vs 0.12% | `FACT VERIFIED` |
| 9 | Does not validate that the journal belongs to the entry's company | D19 — 1 posted entry violates it | `FACT VERIFIED` |
| 10 | Does not require provenance | D16 — 3.9% of posted entries have none | `FACT VERIFIED` |
| 11 | Does not prevent an entry whose every line is zero | D16 — **38** such posted entries | `FACT VERIFIED` |

> **Finality claim P08 can defend: posting assigns a number and changes a state. Nothing in the measured surface makes a posted entry final.**

## 2. The finality stack, ranked by what actually holds

| Layer | Holds? |
|---|---|
| Database uniqueness on (number, journal) for posted entries | **holds** — 0 duplicates measured |
| Database referential integrity on settlements | **holds** — a settled item cannot be deleted |
| Object-layer balance assertion, reporting currency | **holds unless a caller says otherwise** |
| Object-layer balance assertion, transaction currency | **does not exist** |
| Tamper seal | **exists, unengaged everywhere it could apply** |
| Gapless counter | **exists, never written** — and in the deployed line it is the live mechanism, in the source line it is retired |
| Posting-state protection | **absent from the seal's field set**, and a raw-statement path writes it directly |
| Period lock | **exists, unset on every transacting company** |
| Audit retention | **exists in the 19.0 estate, unset on 88 of 88 companies** |

**Seven of nine controls are present and unengaged. This is the package's central structural finding and it survived four independent challenges.**

## 3. Correction, reversal, cancellation, re-dating, supersession

| Mechanism | What P08 evidences | Class |
|---|---|---|
| **Reversal** | a link **on the entry**; the item carries none | `FACT VERIFIED` |
| **Cancellation** | returns the entry to draft and **destroys its settlements** | `FACT VERIFIED`, peer-corroborated from a different module |
| **Re-dating** | silent, **no attributable trace**, and **not gated on a lock** | `FACT VERIFIED` |
| **Supersession** | **no mechanism found** — a superseded entry and its replacement are linked only if someone used the reversal path | `A VERIFIED ABSENCE`, scope: the declared root set, **with the 7-observation independence limit** |
| **Deletion** | **positive residue**: 18 items name **5 entries that no longer exist**, each item re-parented to a different cancelled entry on the same date | `FACT VERIFIED` — D16 |
| **Correction spanning a close** | split across two periods with nothing linking them | `SUPPORTED INTERPRETATION` — received from a peer, **not re-derived by P08** |

### 3.1 The lineage weakness P08 owns

**Correction lineage in this ledger is not durable.** It lives on one field, on one object, and is destroyed by the very act — cancellation — most likely to accompany a correction. For the 5 deleted entries, the lineage is gone and **only the orphaned items testify that anything existed.**

**`P08-M-14`**: the denormalised parent number is the trace that a snapshot supposedly could not hold. P08 had ruled the question untestable and was wrong.

## 4. Revision lineage of this register

| Supersedes | Change |
|---|---|
| `05` posting model | adds the enforcement stack of `43`, the caller-key result of `44`, and the transacting-scope restatement |
| `07` manual GL control | adds that **no field records authorship**, so "manual" is not a state the ledger can report |
| `36` §2 control table | **corrected**: retention is present in the 19.0 estate, not absent; denominators restated to transacting scope |

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P08 EVIDENCE`, with one `SUPPORTED INTERPRETATION` and one `A VERIFIED ABSENCE` carrying a declared independence limit.**
