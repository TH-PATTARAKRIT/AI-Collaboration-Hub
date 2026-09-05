# D22 — P09_PUBLICATION_INTEGRITY_CHECK

**Checkpoint:** `CP-P09D22` · **Layer:** 1 — clean-room.
**The directive requires these seven checks to pass BEFORE any headline is published. They were run before this round's headline was written, and four of them failed on first pass.**

---

| # | Check | Result |
|---|---|---|
| **A** | **denominator audit** — does every published count state its subject, unit and population rule? | **FAILED on first pass, then repaired.** The inherited headline counted **accounts**; the claim is about **entries**. Repaired in `D01`; rule `NC-11` issued |
| **B** | **sign audit** — is the sign a property of the accounting or of the aggregation? | **FAILED on first pass, then repaired.** The +3.6 M is an aggregation artifact of 5 migration entries; the mechanism contributes 0.00. `D03`, `D04` |
| **C** | **headline-to-register reconciliation** | **PASSES after repair.** Every figure in the final report traces to a measured value in `D01`, `D06`, `D08`, `D10` |
| **D** | **full-population check** — no sampling, no truncation | **PASSES.** 339,382 records, 447,384 journal rows, 339 accounts, 27 template rows, 5 databases — all exhaustive |
| **E** | **tool / extraction completeness** | **PASSES with one declared limit.** All five databases restored with a client that reads every format present; **0** analytic records failed to resolve to a journal row |
| **F** | **routing completeness audit** | **FAILED on first pass, then repaired.** 5 of 14 Thai/statutory items were unrouted; all 14 now routed in `D12` |
| **G** | **decision-authority audit** | **PASSES.** P09 ranks build risk and **does not select a build**; `HOLD-AS-01` and `DIS-09` remain unadjudicated; no statutory claim anywhere |

## THE RESULT THAT MATTERS

**Four of seven checks failed on first pass — and each failure was in work already published.** Had these audits been a review step rather than a publication gate, this round would have shipped a headline asserting that depreciation inflates cost-centre profitability, which is **false**.

> **The audits caught what four rounds of adversarial review had not: that the number everyone was arguing about was measuring the wrong thing.**

## CHECKPOINT
**`CP-P09D22` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
