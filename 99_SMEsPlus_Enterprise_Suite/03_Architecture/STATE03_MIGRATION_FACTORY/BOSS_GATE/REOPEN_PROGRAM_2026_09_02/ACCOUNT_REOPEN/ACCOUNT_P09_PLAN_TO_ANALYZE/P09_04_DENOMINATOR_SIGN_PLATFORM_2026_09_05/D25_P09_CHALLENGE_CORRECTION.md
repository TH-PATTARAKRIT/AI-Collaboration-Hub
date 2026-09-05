# D25 — P09_CHALLENGE_CORRECTION — **the challenge returned after publication and overturned this round's verdict**

**Checkpoint:** `CP-P09D25` *(added — material delta after `CP-P09DFINAL`)* · **Layer:** 1 — clean-room.
**Every figure below was re-measured by the author before acceptance. All reproduce exactly.**

---

## 1. THE VERDICT I PUBLISHED IS WITHDRAWN

I published: *"'Depreciation makes the cost centre look more profitable' is **DISPROVED**. The real effect is erasure of cost, not inflation of profit."*

> ## **That distinction does not exist. The verdict is WITHDRAWN.**

A cost centre that **should** bear depreciation and bears **net zero** has an **overstated margin, by exactly the amount erased**. "Erasure of cost" and "looks more profitable" are the same fact stated from two sides. I disproved a strawman — that the `+3,595,851.11` residue was itself profit inflation — while the substantive claim was true all along.

**Measured, over all 23 cost centres:** the depreciation-expense analytic leg totals **−100,400,792.57** and is offset by an accumulated-depreciation credit **on the same cost centre**; **12 of 23 cost centres net exactly 0.00**.

> **Corrected verdict: `CONFIRMED`. Cost centres bear approximately zero net depreciation. Their margin is overstated by the depreciation they should have borne.**

## 2. A FOURTH CONSECUTIVE DENOMINATOR ERROR — SAME SHAPE

| | Published | **Correct** |
|---|---|---|
| stated population | *"entries carrying management records on depreciation accounts"* | unchanged wording |
| **actual population** | **17,405** — silently pre-filtered to **both-legged** entries | **17,465** |
| entries netting non-zero | **5** | **61** |
| rate | **99.99 %** | **99.6507 %** |

**60 one-legged entries were dropped from the denominator while the claim's wording still covered them.** The both-legged rate of 99.9943 % is correct *for that sub-population* and was published against a broader sentence.

**This is the fourth round in a row.** #01 an author-chosen list; #03 a pattern that excluded its own subject; #04 accounts-for-entries; **#05 a silent sub-population inside an unchanged sentence.** The unit was finally right and the population narrowed anyway.

## 3. THE MEASURE THAT WAS NEVER COMPUTED — AND IT IS THE ONE THAT MATTERS

| Measure | Value |
|---|---|
| scalar net across all cost centres | **+3,595,851.11** |
| **gross absolute movement across cost centres** | **154,922,194.55** |
| ratio | **≈ 43×** |

> **Every headline this programme has published — mine and my predecessors' — was a scalar whose gross distribution is forty-three times larger.** A single net figure was never capable of answering a question about attribution across 23 cost centres.

**And inside the entries I counted as contributing exactly 0.00:** cross-cost-centre displacement of **2,019,008.49 in each direction** — cost moved off one operating centre onto another, entry-balanced and invisible to every aggregate.

## 4. THREE FURTHER CORRECTIONS ACCEPTED

| # | My statement | Correction |
|---|---|---|
| 1 | the 5 outliers are "opening-balance / migration entries" | **only 2 are.** The others are an **asset disposal**, an **asset sale posted in the depreciation journal**, and a **manual accumulated-depreciation adjustment**. Calling them all migration was wrong |
| 2 | "98.24 % is meaningless" | **overstated.** It reconstructs exactly and is a coherent net-over-gross ratio; the two legs being different account sets is the measure's definition. **My replacement figure was the defective one** |
| 3 | TH-F-02 swing = 169,954 records | **correct but scope-narrow.** That is the **asset side only**. The full balance-sheet analytic population is **226,612 lines / −50,444,970.46**, including 16,761 payable-class lines. The swing is scope-dependent by an order of magnitude |
| 4 | 9 deployed code-block contradictions | **NOT DECIDABLE as published** — I gave a count without publishing the convention that produces it. Under the reviewer's convention it is **8**. And by posting volume the material account is a currency-gain account (**4,680 lines, −91.2 M**), not the one I named |

## 5. WHAT THE CHALLENGE CLOSED IN MY FAVOUR

- **the parse and the pairing join are sound** — 0 dangling or null links across the depreciation population; exactly 1 null across the whole table, not on a depreciation account;
- **"nets to exactly 0.00" is not a rounding artifact** — tested by exact equality on an unconstrained numeric column; **0** entries fall in the near-zero-but-not-zero band;
- **the Thai-name attack vector is empty** — **0** accounts in the deployed chart carry non-ASCII names, so the code-prefix rule does not under-select here;
- **all of `TH-F-02`'s components reproduce to the cent.**

## 6. THE RISK THE CHALLENGE FLAGGED THAT I HAD NOT SEEN

My population rule treats the depreciation-**expense** account type as meaning depreciation expense. **The shipped v18 Thai template types accumulated depreciation — a contra-asset — with exactly that type.** On any chart built from that template, my rule would fold contra-assets into the expense population silently. **It is safe in this deployment only by accident.** Same defect class as the name-search failure, a different key.

## 7. STATUS

**`CP-P09D19` remains `PARTIAL — RESUMABLE`.** One of four challenge classes ran; it overturned the round's headline verdict and corrected its denominator. **Three classes remain unrun, and the figures they would have tested are still author-measured.**

## CHECKPOINT
**`CP-P09D25` — COMPLETE — EVIDENCE VERIFIED.** Verdict withdrawn, denominator corrected, gross measure introduced.
