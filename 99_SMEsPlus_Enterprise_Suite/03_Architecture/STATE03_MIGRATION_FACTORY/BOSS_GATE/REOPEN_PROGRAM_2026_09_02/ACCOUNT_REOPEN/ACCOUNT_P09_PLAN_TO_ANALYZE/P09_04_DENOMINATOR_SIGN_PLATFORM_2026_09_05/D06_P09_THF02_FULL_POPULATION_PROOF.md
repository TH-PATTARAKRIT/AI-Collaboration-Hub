# D06 — P09_THF02_FULL_POPULATION_PROOF and D07 — GATE SEMANTIC DIFF

**Checkpoints:** `CP-P09D05`, `CP-P09D06` · **Layer:** 1 — clean-room.

---

## 1. REPRODUCED FROM THE COMPLETE POPULATION

Exhaustive over every management record in the deployed database. No sampling, no truncation.

| Quantity | Exact value |
|---|---|
| total management records | **339,382** |
| Gate A — profit-and-loss types only | **112,770** records · **+24,860,594.23** |
| Gate B — Gate A **plus** current, non-current and fixed asset types | **282,724** records · **−252,214,900.89** |
| **delta** | **+169,954** records · **−277,075,495.12** |

**All six figures reproduce exactly.** Records with no general account: **0**.

## 2. THE GATE DIFFERENCE, STATED PRECISELY

| | Gate A | Gate B |
|---|---|---|
| admits | first token of the account type is income or expense, **or** the type is null | the same, **plus** the type is exactly one of current asset, non-current asset, or fixed asset |
| where found | the studied v18 build **and three of four** candidate v19 builds | **one** candidate v19 build, in **two** places in the same query — the expense branch and the outer filter |
| account types excluded by both | liability, equity, receivable, payable, off-balance | same |
| company / context conditions | identical in both | identical |

**Why 169,954 more records enter: three whole balance-sheet classes are added to a filter that previously admitted none of them.**

## 3. THE DECOMPOSITION THE PRIOR ROUND DID NOT DO — AND IT CHANGES THE READING

| Newly admitted class | Records | Value |
|---|---|---|
| **current assets** — inventory and similar | **151,463** (89.1 %) | −227,709,854.61 |
| fixed assets other than accumulated depreciation | 1,047 | −153,362,284.19 |
| **accumulated depreciation** | 17,444 | **+103,996,643.68** |
| **total** | **169,954** | **−277,075,495.12** |

> **`TH-F-02`'s swing is dominated by current-asset records, not by depreciation.** Depreciation is 10 % of the added records and moves the total the *other way*.

**And the depreciation part behaves exactly as `D01` predicts.** Under Gate A the expense leg alone is admitted at −100,400,792.57. Under Gate B its balance-sheet partner joins at +103,996,643.68, and the two **cancel to the same near-zero residue** — so:

> **Under Gate B, depreciation's budget consumption collapses from a correct full cost to approximately nothing.** That half of `TH-F-02` is **CONFIRMED**, and it is a **budget-surface instance of the same zeroing** already proven at entry level.

**The other 152,510 newly admitted records are a separate and larger issue**: inventory-class management records entering budget consumption at −227.7 M. **P09 does not characterise that; it is an account-type-semantics question owned by P08.**

## 4. CLASSIFICATION

| Claim | Verdict |
|---|---|
| the divergent gate admits balance-sheet types | **FACT VERIFIED** — read directly, two places |
| the swing is 169,954 records / −277,075,495.12 | **FACT VERIFIED** — reproduced exactly |
| the swing is *about depreciation* | **CONTRADICTED** — depreciation is 10 % of it, moving the total the opposite way |
| under the divergent gate depreciation budget consumption zeroes | **FACT VERIFIED** |
| any deployment currently runs the divergent gate | **NOT DECIDABLE** — no deployment has the budget module installed on a version this source describes |

## CHECKPOINT
**`CP-P09D05`, `CP-P09D06` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
