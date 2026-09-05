# D04 — P09_MARGIN_LEDGER_SEMANTIC_TRACE and D05 — DEPRECIATION PROFITABILITY DISTORTION

**Checkpoints:** `CP-P09D04`, `CP-P09D05` · **Layer:** 1 — clean-room.
**The directive requires an attempt to DISPROVE the interpretation that depreciation makes the cost centre look more profitable. It is DISPROVED.**

---

> ## ⚠ CORRECTED AFTER PUBLICATION — see `D25`
> The population here is **17,405 both-legged entries**, a silent sub-population of the **17,465** the claim's wording covers; the correct rate is **99.6507 %**, and **61** entries net non-zero, not 5. The `DISPROVED` verdict on the profitability distortion is **WITHDRAWN — it is CONFIRMED**. The scalar net is 43× smaller than the gross cross-cost-centre movement of **154,922,194.55**.


## 1. WHAT +3,595,851.11 MEANS

**It means nothing about depreciation.** Decomposed exactly in `D01` §3.3: the depreciation mechanism contributes **0.00**; the entire residue is one opening-balance adjustment, one carry-forward, and 56 small unpaired expense entries, all at or near a financial-year boundary.

| Candidate meaning | Verdict |
|---|---|
| cost increase | **no** — the mechanism nets zero |
| cost reduction | **no** |
| **profit increase** | **DISPROVED** — see §2 |
| profit reduction | no |
| **contra effect** | **partly** — the balance-sheet leg is a contra-credit and does present as margin-positive, **but its paired debit cancels it on the same entry** |
| **report presentation artifact** | **yes, in part** — the surface aggregates a contra-credit as margin |
| **sign-convention artifact** | **no** — the convention is applied consistently |
| **population/aggregation artifact** | **YES — this is the answer** |

## 2. THE DISPROOF

The interpretation requires depreciation to leave a **net positive** on the cost centre. It does not:

1. **17,404 of 17,405 paired depreciation entries net exactly 0.00.** A mechanism that contributes zero cannot make anything look more profitable.
2. **The positive residue is dated at a financial-year boundary and named as an opening-balance carry-forward and adjustment.** These are migration postings, not depreciation events.
3. **Removing those five entries leaves the depreciation population contributing 0.00 exactly.**

> **`DISPROVED`. Depreciation does not make the cost centre appear more profitable. It makes the cost centre appear to have had NO depreciation at all.**

> **Refined by `D24`:** that is true for **94.38 %** of paired entries. For the remaining **5.62 %** the two legs land on **different** cost centres — so one cost centre is charged and another credited, and the aggregate still shows nothing. **For those, the distortion is misattribution between cost centres, not erasure.**

## 3. WHAT THE REAL DISTORTION IS

Not inflation of profit. **Erasure of cost.**

| | |
|---|---|
| economic cost incurred | ~99.6 M of depreciation expense across 17,405 entries |
| attributed to cost centres, net | **0.00** |
| visible on any surface that sums a cost centre without bucketing by account | **nothing** |
| visible on any surface that filters to profit-and-loss accounts | the full cost — **correctly** |

**The distortion is a disappearance, and it is total on net-balance surfaces.** That is worse than a profitability overstatement and easier to miss, because a cost centre showing no depreciation looks like a cost centre that owns no assets.

## 4. WHAT THE MIGRATION RESIDUE IS — ROUTED, NOT ADJUDICATED

Five entries carry ±78 M of one-sided balance-sheet management records at a year boundary. **P09 does not classify them.** They are opening-balance and carry-forward postings, and whether management records should have been created for them at all is an **asset and ledger question**.

**Routed:** to P04 (were these asset-module postings?) and P08 (should a carry-forward entry produce management attribution?). **`UNRESOLVED — EVIDENCE REQUIRED`.**

## 5. THE CORRECTED SEMANTIC STATEMENT FOR THE PACKAGE

> **The management ledger is a margin ledger. Depreciation enters it as a matched debit-and-credit pair that annihilates on 99.99 % of entries, so depreciation cost is absent from cost-centre margin rather than misstated in it. The aggregate positive residue observed at population level belongs to opening-balance migration entries and carries no depreciation meaning.**

## CHECKPOINT
**`CP-P09D04`, `CP-P09D05` — COMPLETE — EVIDENCE VERIFIED.** Profitability-distortion interpretation **DISPROVED**; the erasure finding **CONFIRMED and strengthened**. Auto-continue.
