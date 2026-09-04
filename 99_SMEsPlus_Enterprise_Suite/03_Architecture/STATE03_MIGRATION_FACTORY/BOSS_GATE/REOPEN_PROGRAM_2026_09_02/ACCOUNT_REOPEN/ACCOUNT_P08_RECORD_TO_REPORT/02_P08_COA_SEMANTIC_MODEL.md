# P08_COA_SEMANTIC_MODEL — Chart of Accounts Semantics

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 (clean-room) · Evidence in `LAYER2_EVIDENCE_QUARANTINE/E02_COA_AND_IDENTITY.md`

Reference behaviour is **benchmark evidence only**. Nothing in this file is an SMEsPlus design decision.

## 1. What the benchmark actually does

| # | Observed semantic | Class |
|---|---|---|
| COA-01 | A ledger account is identified internally by an opaque surrogate key. The account number is not part of that key. | FACT VERIFIED |
| COA-02 | Account-number uniqueness is not enforced by the database. It is applied by the application at save time, and it is deferrable by the calling context. | FACT VERIFIED |
| COA-03 | Uniqueness scope is the **branch of the legal-entity tree** — a number is refused if any ancestor-or-descendant entity already uses it. | FACT VERIFIED |
| COA-04 | A ledger account is owned by a **set** of legal entities, not by one. The same account record may be shared across many entities. | FACT VERIFIED |
| COA-05 | Visibility runs **downward only** (a parent's account is visible in a subsidiary; a subsidiary's account is not visible in the parent), while uniqueness is checked in **both** directions. A number can therefore be refused because of an account the operator cannot see, and the refusal message discloses that invisible number. | FACT VERIFIED (mechanism) + SUPPORTED INTERPRETATION (the disclosure consequence) |
| COA-06 | The account number is stored **per tree root**, not per entity. Every entity sharing a root shares one number for a given account; numbers can differ only between separate trees. | FACT VERIFIED |
| COA-07 | The interface nevertheless presents one editable number row **per entity**. Editing the row for one entity changes the number for every entity under the same root. | FACT VERIFIED (store and interface) + SUPPORTED INTERPRETATION (the silent cross-entity effect) |
| COA-08 | Number content is constrained only by character set and length. No digit count, no mask, no prefix conformance, no relation to classification. | FACT VERIFIED |
| COA-09 | Classification is a flat vocabulary of **18** values with no extension point present in the build. | FACT VERIFIED |
| COA-10 | The balance-sheet / income-statement split is **derived from the text of the classification value** (the substring before the first separator), not from a declared attribute. | FACT VERIFIED |
| COA-11 | Carry-forward behaviour is derived from that same text: an account carries forward unless its structural group is income or expense. | FACT VERIFIED |
| COA-12 | Exactly one current-year-result account may exist per entity; it is auto-provisioned when needed by counting downward from a high reserved number. | FACT VERIFIED |
| COA-13 | Reconcilability is defaulted from classification, forced on for the two subsidiary-ledger control classes, forced off for income/expense/equity/liquidity/off-balance, and **left untouched** for the remaining asset and liability classes. | FACT VERIFIED |
| COA-14 | Groupings are defined as **number-prefix ranges owned by the tree root**. There is no link between account and grouping; membership is recomputed on every read, most-specific range winning. | FACT VERIFIED |
| COA-15 | The grouping hierarchy is itself derived and self-healing: a grouping's parent is recomputed as the longest enclosing range whenever a range changes, and children re-attach upward when a grouping is removed. Overlapping ranges of equal granularity are rejected. | FACT VERIFIED |
| COA-16 | **Changing an account number silently re-parents the account** into a different grouping and a different top-level node, re-sorts the chart, and changes the number for every entity under the tree root. | FACT VERIFIED |
| COA-17 | Nothing in the number-write path consults whether the account has been posted to — although the system computes and exposes exactly that fact for search purposes. | VERIFIED ABSENCE (Class A), scope = the account write path and its uniqueness routine |
| COA-18 | Because postings reference the account object and read its number through it, a re-code **retroactively restates every historical statement**, including periods behind a posting lock and including entries protected by a tamper-evident seal — without invalidating that seal. | FACT VERIFIED (mechanism); SUPPORTED INTERPRETATION (seal consequence) |
| COA-19 | Retirement is a forward-looking input block, not an archive. It changes nothing about history and both of its posting checks are suppressible by the calling context. | FACT VERIFIED |
| COA-20 | Deletion is refused whenever a posting, a tax-mapping or a jurisdiction-mapping references the account. | FACT VERIFIED |
| COA-21 | Account identity can be **destroyed by an administrative merge**: references are repointed by direct data manipulation and the losing records removed by direct deletion. Number, name, tags, journal allow-list and grouping are not consulted when deciding which accounts may merge. | FACT VERIFIED |
| COA-22 | Only two conditions block a merge pair: shared ownership by one entity, or both accounts carrying tamper-evident entries. An inverse split operation exists and leaves postings untouched. | FACT VERIFIED |
| COA-23 | An account currency **forces** the transaction currency of its lines — but only when it differs from the entity's functional currency; setting it equal to the functional currency imposes nothing. | FACT VERIFIED |
| COA-24 | The delivered chart content is minimal: two chart definitions totalling 71 account rows, and **zero groupings**. The jurisdiction chart uses 10 of the 18 classifications. | FACT VERIFIED |

## 2. What this means for the P08 question

The chart layer contributes three answers to *what is the accounting source of truth*:

**COA-A — The account number is a presentation attribute, not an identity.** Identity is the surrogate key; the number is a mutable, tree-scoped label read through it. Any SMEsPlus statement that "the chart of accounts is the source of truth for account identity" is false in the benchmark: the chart holds *labels*, the ledger holds *references*.

**COA-B — Structure is derived, not declared, at three levels.** Statement side (balance sheet vs income statement), carry-forward behaviour, and grouping membership are all computed from text — the classification value's prefix, and the account number's prefix. Three separate report-shaping decisions therefore depend on string conventions that nothing validates.

**COA-C — Historical statements are not stable under master-data change.** Re-coding, re-grouping, and merging all restate history, and none of them consults the posting population. This is the chart-layer instance of the same property found at the report layer and the currency layer: **the benchmark's financial statements are re-derivations, not records**.

## 3. Requirements this raises for SMEsPlus (DESIGN CANDIDATE — no implementation authority)

| ID | Candidate requirement | Driven by |
|---|---|---|
| `P08-RQ-COA-01` | Account identity must be explicit and immutable, and the account number must be versioned with effective dates rather than overwritten. | COA-16, COA-17, COA-18 |
| `P08-RQ-COA-02` | Statement side and carry-forward behaviour must be declared attributes of the classification, never derived from the spelling of a code or a value. | COA-10, COA-11 |
| `P08-RQ-COA-03` | Grouping membership must be an explicit, stored, effective-dated relationship. Number-prefix inference may drive a *proposal*, never the stored truth. | COA-14, COA-15, COA-16 |
| `P08-RQ-COA-04` | Any master-data change capable of restating an issued statement must be blocked, or must require an explicit restatement authorisation that is itself an auditable fact. | COA-16, COA-18, COA-21 |
| `P08-RQ-COA-05` | Number uniqueness and number visibility must share one scope. A refusal must never disclose an object outside the requester's visibility. | COA-05 |
| `P08-RQ-COA-06` | The number-per-entity contract must be settled explicitly: either the number is a tenant/entity attribute or a group attribute. The benchmark's split between a per-entity interface and a per-root store is a defect, not a model. | COA-06, COA-07 |
| `P08-RQ-COA-07` | Account merge must not exist as a data-manipulation operation on a posted chart. If a merge capability is required, it must be a mapping, leaving both identities intact. | COA-21, COA-22 |
| `P08-RQ-COA-08` | Control-account status must be a declared property with its own posting restrictions — see `07_P08_MANUAL_GL_CONTROL.md`. | COA-13 |

## 4. Open items carried to the registers

`P08-U-COA-01` (Class D) — whether a classification-driven recompute of the reconcilability flag bypasses the routines that maintain open-item residuals. Requires runtime confirmation.
`P08-U-COA-02` (Class B) — whether any module outside the searched scope restores a posting-time guard on manual entries to control accounts.
`P08-U-COA-03` (Class C) — migration behaviour of the per-entity to per-tree number conversion.
`P08-U-COA-04` (Class C) — the legacy custom tree was not searched for chart-layer overrides.
