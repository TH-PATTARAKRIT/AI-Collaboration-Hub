# S02 — P09_THF01_BUDGET_ZEROING_PROOF

**Checkpoint:** `CP-P09S02` · **Layer:** 1 — clean-room.

---

## 1. THE PROOF OBLIGATION

Prove or disprove: *the accumulated-depreciation leg is admitted to budget consumption, and the result nets to zero.*

## 2. THE GATE, RE-DERIVED

Budget consumption admits a management record only when its general account's type resolves, on its **first token**, to income or expense (or the type is null). A depreciation-**expense** type resolves to `expense` and is admitted. A fixed-asset type resolves to `asset` and is **excluded**.

**FACT VERIFIED.** The gate is a first-token match, so the template's mistyped accumulated-depreciation accounts **would** be admitted.

## 3. THE DEPLOYED TEST — AND ITS DECISIVE LIMITATION

| Measurement | Result |
|---|---|
| budget header records in the deployed database | **ZERO** |
| budget line records | **ZERO** |

> **The deployment holds no budgets at all. Budget consumption cannot be zeroed where no budget exists.**

**Therefore the budget-zeroing question is `NOT DECIDABLE` in the only deployment for which data exists — and this is true of my previous claim and of its retraction equally.** Neither can be tested there. Recording only the retraction would substitute one over-claim for another.

## 4. WHAT *CAN* BE PROVEN — THE GATE SIMULATION

The gate can be applied to the deployed management records directly, which answers what budget consumption *would* admit if a budget existed. Exhaustive over all 339,382 records; no sampling, no truncation.

| Class | Records | Sum |
|---|---|---|
| **admitted** — income / expense account types | **112,770** | **+24,860,594.23** |
| **excluded** — balance-sheet account types | **226,612** | **−50,444,970.46** |
| no general account | 0 | — |

And for the depreciation accounts specifically, from `S01`:

| Leg | Deployed type | Gate outcome |
|---|---|---|
| accumulated depreciation | `asset_fixed` | **EXCLUDED** |
| depreciation expense | depreciation-expense | **ADMITTED** |

> **In this deployment the gate does exactly what it should: it excludes the balance-sheet leg. The depreciation cost would be consumed once, at its full amount. TH-F-01's zeroing does NOT occur here.**

## 5. CLASSIFICATION

| Claim | Verdict |
|---|---|
| the gate admits a depreciation-expense-typed account | **FACT VERIFIED** |
| the shipped template types accumulated depreciation that way | **FACT VERIFIED** |
| a deployment configured from that template would zero its depreciation budget consumption | **SUPPORTED INTERPRETATION** — arithmetic follows; unobserved |
| **budget consumption nets to zero on a Thai-chart install** | **CONTRADICTED as stated** — not observed, and untestable in the only deployment available because it holds no budgets |
| **budget zeroing overall** | **`UNRESOLVED — EVIDENCE REQUIRED`: a deployment with both budgets AND template-derived depreciation accounts.** Neither condition is met anywhere in the searched population |

## 6. THE FINDING THIS PROOF PRODUCED INSTEAD — AND IT IS LARGER

**Two-thirds of the management ledger sits on balance-sheet accounts.**

**226,612 of 339,382 records — 66.8 % — carry a balance-sheet general account.** Under the reference product's own declared design, which the prior round established is a **margin ledger** whose balance is revenue minus cost, a balance-sheet-account record has no margin meaning at all.

This is not a Thai issue, not a template issue, and not configuration-specific. It is the **general form of the zeroing finding, measured**: the management ledger is majority-populated by records that the product's own consumers filter out.

| Reading | Consequence |
|---|---|
| every budget-style surface (income/expense gated) | sees **112,770** records |
| the analytic account balance (ungated) | sees **all 339,382**, and the two populations partly annihilate |
| the difference between those two views | **226,612 records** |

**Classification: `FACT VERIFIED`.** This supersedes TH-F-01 as the more important budget-related finding of this supplement, and it needs no localization to hold.

## 7. WHAT WOULD SETTLE THE ORIGINAL QUESTION

1. a deployment holding **both** budgets and assets configured against template-derived accounts — **not present in the searched population**;
2. failing that, the question stays `UNRESOLVED — EVIDENCE REQUIRED` and must not be reported as either confirmed or refuted.

## CHECKPOINT

**`CP-P09S02` — COMPLETE — EVIDENCE VERIFIED.** Budget zeroing: **UNRESOLVED**, prior claim **CONTRADICTED as stated**, and a larger measured finding produced in its place. Auto-continue.
