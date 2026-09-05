# D01 — P09_HEADLINE_DENOMINATOR_REPAIR

**Checkpoint:** `CP-P09D01` · **Log version:** P09#05 · **Baseline verified:** `e2b5623`, head = remote, tree clean.
**Layer:** 1 — clean-room.

---

> ## ⚠ CORRECTED AFTER PUBLICATION — see `D25`
> The population here is **17,405 both-legged entries**, a silent sub-population of the **17,465** the claim's wording covers; the correct rate is **99.6507 %**, and **61** entries net non-zero, not 5. The `DISPROVED` verdict on the profitability distortion is **WITHDRAWN — it is CONFIRMED**. The scalar net is 43× smaller than the gross cross-cost-centre movement of **154,922,194.55**.


## 1. THE ERROR IS DEEPER THAN EITHER PRIOR CORRECTION

Two rounds corrected the **population**. Neither questioned the **unit**. Both were wrong for the same reason.

| Round | Denominator used | Unit | Verdict |
|---|---|---|---|
| P09#03 | accounts each **asset references** | account | **wrong population** |
| P09#04 | **every account of the type** in the chart | account | **right population, wrong unit** |
| **P09#05** | **the paired accounting entry** | **entry** | **correct** |

> **The quantity being claimed was always "does the allocation annihilate?" That is a property of an ACCOUNTING EVENT, not of an account.** Counting accounts — by any population rule — cannot answer it. Both prior denominators were units that could not carry the claim.

## 2. THE CORRECT MEASUREMENT

Unit = **one accounting entry** carrying at least one management record on a depreciation account. Population = every such entry in the deployed database, exhaustive, joined through the journal row to its entry.

| Class | Entries | Accumulated-depreciation side | Expense side | Net |
|---|---|---|---|---|
| **carrying BOTH legs** | **17,405** | +26,145,323.62 | −99,632,164.48 | −73,486,840.86 |
| — of which net **exactly 0.00** | **17,404 — 99.99 %** | | | **0.00** |
| — of which do not | **1** | −79,104,680.82 | +5,617,839.96 | −73,486,840.86 |
| carrying only the balance-sheet leg | 4 | +77,851,320.06 | — | +77,851,320.06 |
| carrying only the expense leg | 56 | — | −768,628.09 | −768,628.09 |
| **GRAND TOTAL** | | | | **+3,595,851.11** |

Analytic records with no resolvable journal row: **0**.

## 3. WHAT THIS DOES TO EVERY PRIOR HEADLINE

### 3.1 The mechanism claim is CONFIRMED, and far more strongly than before
**17,404 of 17,405 paired entries net to exactly 0.00 — 99.99 %.** Per-entry, not in aggregate. This is the strongest evidence the symmetric-allocation mechanism has received in the entire programme.

### 3.2 The "98.24 % annihilated" figure is withdrawn as meaningless
It was computed by summing **two non-identical populations** — 17,444 records on one account set against 17,488 on another — and dividing. The sets are not the same events. **A ratio between two populations that are not the same population is not a rate.** The meaningful figure is the per-entry one in §2.

### 3.3 The "+3,595,851.11 net" is **entirely an artifact of five entries**
Reconciled exactly:

| Component | Value |
|---|---|
| 17,404 exactly-zeroing paired entries | **0.00** |
| 1 non-zeroing paired entry — an **opening-balance adjustment** dated at a financial-year boundary | −73,486,840.86 |
| 4 balance-sheet-only entries — dominated by an **opening-balance carry-forward** at the same year boundary | +77,851,320.06 |
| 56 expense-only entries | −768,628.09 |
| **total** | **+3,595,851.11** |

> **The grand net is a migration and carry-forward residue. It is not produced by the depreciation mechanism, and the depreciation mechanism contributes exactly 0.00 to it.**

> ### ⚠ REFINED BY `D24` — READ BOTH
> The 99.99 % is an **entry-level** figure. At **cost-centre level** the annihilation is **94.38 %** (16,427 of 17,405): **978 entries leave a non-zero effect on an individual cost centre**, and 977 of those are a **redistribution between two different cost centres** that cancels in aggregate and is invisible to any population-level analysis. **Both figures must be quoted together.**

## 4. WHY THE PROXY WAS INVALID — STATED AS A RULE

An account is a **place**; the claim is about an **event**. Aggregating by place answers *"how much sits on these accounts"*; it cannot answer *"do these two amounts arise from one event and cancel"*. The two questions have the same units and different meanings, and the arithmetic gives an answer to the wrong one without complaining.

> **`NC-11` — Before choosing a population, state the claim's SUBJECT. If the claim is about an event, the unit is the event; an account, a record or a module cannot substitute for it, no matter how the population is defined.**

**This is the third denominator failure in three consecutive rounds, and the first where the population was correct.** Correcting a population does not repair a unit.

## CHECKPOINT
**`CP-P09D01` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
