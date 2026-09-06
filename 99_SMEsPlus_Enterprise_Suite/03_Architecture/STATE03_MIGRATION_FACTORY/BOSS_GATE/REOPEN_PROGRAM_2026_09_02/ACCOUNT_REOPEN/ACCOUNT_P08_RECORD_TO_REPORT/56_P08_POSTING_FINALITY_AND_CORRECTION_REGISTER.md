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
| 6 | ~~Does not make the entry immutable~~ **WITHDRAWN — `P08-CONTRA-54`** | **A default-on guard refuses to write nine named fields on a posted entry** — the accounting date, the entire line set, the party, the payment term, the currency, the fiscal position and the cash-rounding rule. **No configuration; on for every company and every journal in the estate.** It is defeated only by a caller-supplied key. P08 measured the **optional seal** and concluded about **immutability** — the wrong instrument for the claim | **`CONTRADICTED — CORRECTED`** |
| 7 | **Relocates a violating date rather than refusing it** | S18, asserted by the product's own test | `FACT VERIFIED` |
| 8 | Derives the accounting date for a non-sale **invoice-type** document, lock or no lock | **CORRECTED — `P08-CONTRA-50`.** The derivation's caller returns early unless the move is an invoice; **129,577 posted plain entries never enter it.** "Every non-sale document" was the widest-scoped statement of the defect and is withdrawn | `FACT VERIFIED`, re-scoped |
| 9 | Does not validate that the journal belongs to the entry's company | D19 — 1 posted entry violates it | `FACT VERIFIED` |
| 10 | Does not require provenance | D16 — 3.9% of posted entries have none | `FACT VERIFIED` |
| 11 | Does not prevent an entry whose every line is zero | D16 — **38** such posted entries | `FACT VERIFIED` |

> **CORRECTED FINALITY CLAIM — `P08-CONTRA-54`.** Posting assigns a number, changes a state, **and makes nine named fields unwritable by default**. What it does **not** do is seal the entry against the paths that bypass the object layer: the posting state itself is outside the seal's field set, a raw-statement path writes it directly, and the readonly guard is switched off by a caller-supplied key.
>
> **The corrected claim is narrower, harder to dismiss, and points design the other way: a default-on immutability guard over a named field set already exists, and it is defeated by a request parameter.**

## 2. The finality stack, ranked by what actually holds

| Layer | Holds? |
|---|---|
| Database uniqueness on (number, journal) for posted entries | **holds** — 0 duplicates measured |
| Database referential integrity on settlements | **DEFEATED — `P08-CONTRA-55`.** A module **installed in all three deployed databases** deletes the settlement table and the item table in **raw SQL**, in that order — precisely the order that defeats the constraint — with **no company predicate, no state predicate, and a commit per table**. It also resets the entry-number sequence to 1. The one control this package ranked as unconditionally holding does not hold |
| Object-layer balance assertion, reporting currency | **holds unless a caller says otherwise** |
| Object-layer balance assertion, transaction currency | **does not exist** |
| Tamper seal | **exists, unengaged everywhere it could apply** |
| Gapless counter | **exists, never written** — and in the deployed line it is the live mechanism, in the source line it is retired |
| Posting-state protection | **absent from the seal's field set**, and a raw-statement path writes it directly |
| Period lock | **exists, unset on every transacting company** |
| Audit retention | **exists in the 19.0 estate, unset on 88 of 88 companies** |

**CORRECTED — `P08-CONTRA-56`. The "seven of nine" double-counts one control as three.** The seal, the entry hash and the gapless counter are **not independent observations**: the hash and counter are written only when the seal is enabled, so their zeros are **entailed** by the seal's zero. After collapsing that entailment and adding the default-on carriers of row 6, the honest statement is:

> **Of the independent controls in this stack, the ones that require configuration are unengaged everywhere they could apply; the ones that are on by default hold at the object layer and are bypassed by paths that do not go through it.**

That is a weaker headline than "seven of nine" and a more accurate one.

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


---

## 5. Corrections applied after the bounded AAS-03 challenge

| ID | Correction | Found by |
|---|---|---|
| `P08-CONTRA-50` | The date derivation reaches only invoice-type documents; 129,577 posted plain entries never enter it | E1 |
| `P08-CONTRA-54` | A default-on guard makes nine named fields unwritable on a posted entry. The central finality claim is withdrawn and re-issued | E1 |
| `P08-CONTRA-55` | Settlement referential integrity does **not** hold — a module installed in all three databases defeats it in raw SQL | E3 |
| `P08-CONTRA-56` | "Seven of nine" double-counts one control as three | E1 |

**Author's note on `P08-CONTRA-54`.** The nine-field guard and its bypass key were already established in this package's own earlier work. They were not carried into the finality stack. This is not a search failure; it is a failure to bring known evidence to a claim that turned on it.
