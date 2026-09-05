# P08_SOURCE_TO_REPORT_TRUTH_TRACE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T09`

The directive mandates one trace and one question. The trace is:

> Business Source → Accounting Event → Journal → Journal Entry → Journal Item → Ledger → Subledger → Reconciliation → Trial Balance → Financial Statements → Close

The question is **what is the accounting source of truth**. This artifact walks the chain hop by hop and states, for each hop, **what object holds the truth, whether the link to the previous hop is stored or reconstructed, and what the deployed data measures.**

Source observations are product line **18.0**. Deployed measurements are `DB-SM`, product line **16.0**, 447,384 journal items — with `DB-BK` and `DB-EV` at **19.0** where cited. No deployed database matches the source line; see `40_P08_VERSION_PREMISE_CORRECTION.md`. Every hop below labels which layer it rests on.

---

## 1. The trace

### Hop 1 — Business Source → Accounting Event

| | |
|---|---|
| **Carrier** | the originating business record itself. There is **no separate object between the business record and the entry.** |
| **Link** | **stored, and one-directional.** The entry points back at its origin. The origin does not, in general, point forward at what it produced. |
| **Identity durability** | **channel-dependent, and this is the corrected finding of this session.** Some inbound channels carry a database-enforced identity key — imported bank lines carry an import key under a uniqueness constraint, and payment transactions carry a reference under one. Most do not. |
| **Deployed measurement** | **0 of 13,814** bank statement lines in `DB-SM` carry either dedup key. The constraint exists; nothing populated the column. |
| **Verdict** | `FACT VERIFIED` — 18.0 source for the mechanism, 16.0 data for the population. The identity machinery is **present, per-channel, and unengaged**. |

The class-A claim that no accounting-event identity exists anywhere was **WITHDRAWN as CONTRADICTED** in `39_P08_ACCOUNTING_EVENT_IDENTITY_FORENSIC.md`. The correct statement is narrower and worse: identity exists for a minority of channels, is not a platform property, and is not populated where it exists.

### Hop 2 — Accounting Event → Journal

| | |
|---|---|
| **Carrier** | the journal is a **classification and numbering context**, not a truth carrier. It supplies a sequence, a default account set and a seal setting. |
| **Deployed measurement** | **64 journals in `DB-SM`; 0 with the tamper seal enabled.** |
| **Verdict** | `FACT VERIFIED`. The journal contributes no financial fact. Its material contribution — the seal — is off everywhere measured. |

### Hop 3 — Journal → Journal Entry

| | |
|---|---|
| **Carrier** | the entry. It holds the date, the posting state, the origin pointer for **47.17%** of items, the seal (unused) and the reversal link. |
| **Uniqueness** | a database index enforces one name per journal **only for posted entries with a name other than the placeholder**. Draft and cancelled entries are unconstrained. |
| **Deployed measurement** | **33,147 posted entries share (reference, company, type) with at least one other, in 4,308 groups.** **83,820** plain entries have no recoverable link to any originating object; **5,786** of those have no reference either. |
| **Verdict** | `FACT VERIFIED`. The entry is the **strongest** identity object in the chain and it is still not an identity. |

### Hop 4 — Journal Entry → Journal Item

| | |
|---|---|
| **Carrier** | **the item. This is where the money is.** |
| **Link** | stored and mandatory. |
| **What is lost across the hop** | provenance. Fully analysed in `41_P08_JOURNAL_ITEM_TRUTH_ROLE_MATRIX.md`: 69.07% of items carry a Tier-1 origin pointer, but for **47.17%** that pointer sits on the **entry**, not the item; **17.00%** carry no provenance mark of any kind; **18.49%** satisfy two or more origin predicates at once, so no field partitions the population. |
| **Verdict** | `FACT VERIFIED`. |

### Hop 5 — Journal Item → Ledger

| | |
|---|---|
| **Carrier** | **there is no ledger object.** The general ledger is a *query shape over items*, not a stored artifact. |
| **Negative claim** | `A VERIFIED ABSENCE` — no persisted ledger, ledger-balance or ledger-period table across **22 of 22 core roots**, pattern re-run with a positive control in `34_P08_CLASS_A_ROOT_SET_REVALIDATION.md`. |
| **Consequence** | the ledger cannot be tampered with independently of the items, and it cannot be *reconciled* against them either. There is nothing to compare. |

### Hop 6 — Ledger → Subledger

| | |
|---|---|
| **Carrier** | **no subledger exists as a distinct ledger.** Receivables, payables, inventory valuation, asset and tax detail are the *same item rows*, filtered by account. |
| **Consequence** | subledger-to-GL agreement is **true by construction and therefore unverifiable**. There is no independent record whose disagreement could be detected. |
| **Peer corroboration** | P04 independently reported the absence of a subledger-to-GL reconciliation. **CONFIRMS P08**; recorded as one root cause, not two findings. |
| **Verdict** | `FACT VERIFIED`, and this is a **material design consequence**, not a defect of the benchmark: a single-ledger model trades detectability for consistency. |

### Hop 7 — Subledger → Reconciliation

| | |
|---|---|
| **Carrier** | pairwise settlement records, each binding a debit side to a credit side with an amount. |
| **Integrity** | both sides are required and neither declares a delete rule, so the database refuses to remove a settled item. |
| **Deployed measurement** | **63,773 settlement records covering 100,580 settled lines; residual drift 0** when the graph is reconstructed independently. **46.4% were recorded after their own as-of date; 22.7% more than 30 days after; 710 more than a year; maximum 594 days.** |
| **Verdict** | `FACT VERIFIED`. **The arithmetic is sound and the chronology is not.** Settlement is accurate about *how much* and unreliable about *when*. |

### Hop 8 — Reconciliation → Trial Balance

| | |
|---|---|
| **Carrier** | **no stored trial balance.** Computed at query time from items. |
| **Balance property** | **0 unbalanced posted entries in the reporting currency** across 169,143 posted entries in `DB-SM` — the invariant holds in the currency the report is expressed in. |
| **The failure** | **1,851 posted entries have a non-zero transaction-currency sum**; **53** of these have two or more foreign-currency lines. The balance check is written against the reporting currency only, so the transaction-currency imbalance has **no defence at any layer** — see `43_P08_DOUBLE_ENTRY_ENFORCEMENT_MATRIX.md`. |
| **Verdict** | `FACT VERIFIED`. The trial balance balances **because the only invariant enforced is the one the trial balance is expressed in.** That is a tautology, not a control. |

### Hop 9 — Trial Balance → Financial Statements

| | |
|---|---|
| **Carrier** | report definitions — line formulas over accounts. |
| **What the statements read** | account, date, amounts, currency, company, partner, journal, entry, display type, posting state. **They read essentially no provenance field.** A scoped search of core reporting for the purchase-order-line, sales-order-line, expense, asset and matching-rule pointers returns zero hits — `B NOT FOUND IN SEARCHED SCOPE`, bounded to 18.0 core reporting. **The deployed databases add a custom reporting module this bound does not cover.** |
| **Verdict** | `FACT VERIFIED` within the stated bound. The statements aggregate the object that carries the least provenance. |

### Hop 10 — Financial Statements → Close

| | |
|---|---|
| **Carrier** | **no accounting-period object.** `A VERIFIED ABSENCE` across **22 of 22 roots**. The period is a **date range on a company record**, not a thing with a state. |
| **Year-end result** | **no posted profit-and-loss closing entry.** The year-end result is derived at report time. |
| **Lock behaviour** | a posting aimed at a locked period is **silently re-dated forward and posted**, including under the irrevocable lock. Verified in 18.0 source and by the product's own test, which asserts a 2020 entry posting into 2021 under a mid-2021 lock. |
| **Deployed measurement** | **0 of 89 companies** across the three databases have any period lock set. **6,418** posted entries carry an accounting date more than a year before their creation; maximum **6,701 days**; **22,162** are future-dated. |
| **Verdict** | `FACT VERIFIED`. **Close is not a state transition in this model. It is a date comparison, and in the deployed evidence nobody set the date.** |

---

## 2. The answer to the mandated question

> **What is the accounting source of truth?**

**The journal item is the source of truth for amount, account, currency, company and date.** Nothing downstream of it is stored; the ledger, subledger, trial balance and statements are all query shapes over the same rows.

**The journal item is not the source of truth for meaning.** Meaning — what economic event this is, what produced it, whether it is original or derived — sits on the entry for nearly half the population, on nothing at all for 17%, and is ambiguous for 18.49%.

**And the entry is not an identity.** It has no durable key from the business source in the general case, no seal in the deployed data, and 33,147 posted entries in one database collide on their own reference triple.

The honest statement is therefore three statements, and the package now carries all three rather than the single sentence it started with:

| Dimension of truth | Where it actually lives | Strength |
|---|---|---|
| **Monetary fact** | the **journal item** | **strong** — sole store, database-integral, arithmetically consistent |
| **Economic meaning** | **split** between item, entry and nothing | **weak** — no partition, 17% unmarked |
| **Event identity** | **the business record, per channel** | **absent as a platform property** — present for a minority of channels, unpopulated where present |

**`SUPPORTED INTERPRETATION → FACT VERIFIED`** for the first row; **`FACT VERIFIED`** for the second and third; the *design* consequence is `DESIGN CANDIDATE` and belongs to P11 and the Boss, not to P08.

---

## 3. Where the chain breaks, ranked

| # | Break | Hop | Class | Measured |
|---|---|---|---|---|
| 1 | **No durable event identity as a platform property** | 1 | `FACT VERIFIED` | 0 of 13,814 lines carry the key that exists |
| 2 | **Provenance sits above the object the statements read** | 4 → 9 | `FACT VERIFIED` | 47.17% entry-only, 17.00% none |
| 3 | **The enforced invariant is the reporting currency only** | 8 | `FACT VERIFIED` | 1,851 imbalances, 53 multi-line, no defence at any layer |
| 4 | **Close is a date comparison with no state** | 10 | `FACT VERIFIED` | 0 of 89 companies configured |
| 5 | **Settlement chronology is unreliable** | 7 | `FACT VERIFIED` | 46.4% backdated, max 594 days |
| 6 | **Subledger agreement is unverifiable by construction** | 6 | `FACT VERIFIED` | no independent record exists |
| 7 | **Entry uniqueness is partial** | 3 | `FACT VERIFIED` | 33,147 colliding posted entries |

---

## 4. Bounds

- Hops 1, 3, 6, 9, 10 rest on **18.0 source** for mechanism and **16.0 data** for population. The mechanism is not asserted to hold in 16.0 or 19.0 except where separately measured.
- Hop 9's negative claim is bounded to **core reporting in 18.0** and **does not cover the custom reporting module present in the deployed databases**. `C NOT YET SEARCHED` for that module's provenance use.
- Every count in this artifact is reproduced from the enumerations published in files 33–44, each of which declares its POPULATION, PATTERN, PATH SET and UNIT with a positive control. No count originates here.
