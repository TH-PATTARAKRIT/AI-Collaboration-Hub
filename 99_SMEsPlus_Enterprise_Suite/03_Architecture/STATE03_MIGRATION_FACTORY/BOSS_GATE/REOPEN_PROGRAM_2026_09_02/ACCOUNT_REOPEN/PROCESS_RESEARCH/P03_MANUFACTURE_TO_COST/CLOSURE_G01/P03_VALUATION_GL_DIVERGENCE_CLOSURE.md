# P03R-F-01 — VALUATION vs GL DIVERGENCE, BOUNDED-DEEP CLOSURE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-04`.
**SAFETY VETO OBSERVED: no repair, no write, no post, no restore, no correction experiment.**
Read-only reconstruction only.

---

## 1. Origin event family — now named precisely

Round 4 established from the data: the trigger is a **vendor goods-receipt and bill
revaluation** on an average-costed raw material; manufacturing amplifies it.

**P01's final handoff names the exact mechanism**, which P03 could not see from its side.
**Attribution notice (`CC-01`): the following is P01's source read, INHERITED BY P03 AND NOT
VERIFIED BY P03** — the series-16 tree does not exist in P03's path set (`MD-01`). P03 states
it as P01's finding, not as its own:

> `purchase_stock/models/stock_move.py::_get_price_unit`, series-16 core.
> Three defects: **no zero-guard on `remaining_qty`**; `invoice_lines` summed **unsigned**, so
> refund lines *increase* the base; **no cancelled-bill filter**.
> Entry condition `qty_invoiced > qty_received`. Live firing set: **18 PO lines carrying
> `qty_received = 0.000000`** — the exact zero-denominator subset — at unit prices to
> ฿3,271,028.04.

**The zero-denominator defect is the arithmetic that would produce P03's observed explosion.**
P03 can confirm the *shape* — a division yielding 10¹²–10¹⁶ unit costs — from its own data, and
**cannot confirm the function**, because it cannot open the tree.
`remaining_value / remaining_qty` with `remaining_qty → 0` yields the 10¹²–10¹⁶ unit costs
P03 measured entering the valuation ledger.

## 2. First divergence point

| Step | Evidence | Owner |
|---|---|---|
| 1. A bill is recorded with quantity invoiced > quantity received | **P01, inherited** | **P01** |
| 2. `_get_price_unit` divides by a zero-or-tiny remaining quantity | **P01, inherited — not verified by P03** | **P01** |
| 3. The resulting unit cost enters the **valuation ledger** on a goods receipt | **P03 measured**: `WH/IN/03634`, unit 31 → **712,186.25**, 2024-08-27 09:46 | Inventory |
| 4. Average costing **compounds** it on each subsequent receipt | **P03 measured**: 4.4e9 → 1.5e13 → **5.2e16** over 2024-08-28 … 08-30, with ordinary receipts at ~30 interleaved | Inventory |
| 5. Bill revaluations write zero-quantity layers of −10¹⁷ | **P03 measured**: `AP2024081365`, `AP2024081372` | **P01** / Inventory |
| 6. **MO 4410 / 4412 consume the corrupt material**; `_cal_price` capitalises it into finished goods | **P03 measured**: product 11632 normal at 13.83–279.91 for ten months, then **2,266,696,491,129.46** | **P03 — amplifier** |
| 7. **UNBUILD 440–444** release the corrupt finished goods | **P03 measured**: 5 layers at −352,468,555,154.38 | **P03 — amplifier** |

> **First divergence is step 2 — inside P01's boundary.** P03's first involvement is step 6.
>
> **Evidence split (`CC-01`).** Steps 1–2 are **P01's, inherited and unverified by P03**.
> Steps 3–4 and 6–7 are **P03's own measurements**. The conclusion *"manufacturing amplifies,
> does not originate"* rests on **P03's own half** and does not depend on P01's source read —
> which is why it survives the challenge in `P03_CHALLENGE_CONVERGENCE_REGISTER.md` §1.

## 3. Why the GL is sane while the valuation ledger is extreme

**P03's measurement:** 25 of the 30 extreme valuation rows name a journal entry; **all 25
entries exist and carry entirely different, sane amounts** (e.g. valuation row 27394 at
1.53 × 10²¹ against journal entry 105228 with a total debit of **874,350.00**). **25
mismatched, 0 matched.** The GL sums to **exactly 0.00** across 447,384 lines and holds **no**
line above 10¹².

**The explanation, stated at the limit of the evidence:** the subsidiary valuation ledger and
the general ledger were written by **different computations from different inputs** — the
valuation row carries the corrupt per-unit arithmetic, the journal entry carries an amount
that does not reflect it. **P03 can demonstrate the divergence exhaustively and cannot
demonstrate which write produced the sane figure**, because that requires the series-16
posting path (`MD-01`) and, for a definitive answer, a runtime reconstruction the safety veto
forbids.

**Classification: `FACT VERIFIED` for the divergence; `UNRESOLVED — SPECIFIC EVIDENCE
UNAVAILABLE` for the mechanism that produced the sane GL figure.** Stated as unresolved
rather than filled with a plausible story.

## 4. Manufacturing: origin or amplifier — settled

| Attribution of the 30 corrupt rows | Rows |
|---|---|
| Receipt / other — **P01 / Inventory** | 8 |
| Revaluation, no move — **P01 / Inventory** | 4 |
| Raw consumption — **P03** | 2 |
| Finished output — **P03** | 4 |
| Unbuild — **P03** | 12 |

> **18 of 30 rows are manufacturing-origin, and 0 of 30 are manufacturing-*caused*.**
> The distinction is the finding. **P01 independently withdrew its earlier routing of this
> item to P03 as owner**; P03 independently concluded the same from the data. **Two sessions
> converged on the same attribution from opposite directions.**

## 5. Cancellation and blast radius — the property that governs remediation

| Measure | Value |
|---|---|
| Valuation ledger, all 74,982 rows | **205,490,835.88** |
| Excluding the 30 corrupt rows | **400,338,755.98** |
| Net contribution of the 30 | **−194,847,920.10 (−48.7 %)** |
| **Gross exposure of the 30** | **~10²¹, in both directions** |

> The position is **not** "wrong by 195 million". It is **"wrong by 10²¹ in both directions,
> currently almost cancelling"**. Any partial correction — reversing one unbuild, revaluing
> one product, deleting one entry — **breaks the cancellation and releases an error of
> astronomical magnitude**.

`TZ-09`, `Tolerance = 0`. **Remediation sequencing is a decision, not a task**, and it is
above P03. Routed to P11 as `P11-D-5` and to Boss.

## 6. Controls SMEsPlus would need — `DESIGN CANDIDATE` only

| ID | Control |
|---|---|
| `R-17` | **A cost-injection path validates the magnitude of its inputs and refuses what it cannot justify.** A production order consuming a component at 1.6 × 10¹² per unit against a ten-month history of 30 must fail, not post |
| `R-19` | The subsidiary valuation ledger and the general ledger must be **continuously reconcilable**, with divergence detected rather than discovered |
| `R-21` | **No division without a zero-guard on the denominator** in any cost computation — the specific arithmetic defect P01 names |
| `R-22` | Signed aggregation over invoice lines must respect refunds; cancelled documents must be excluded by predicate, not by convention |

`R-21`/`R-22` are stated because P03 must not repeat them, **not** as instructions to P01.
No implementation is authorised; `AASP-VETO-01` stands.

## 7. Disposition

> **`CQ-P03-04` — `EXTERNAL / CROSS-PROCESS OWNER — HANDOFF PUBLISHED`.**
>
> Origin mechanism: **P01-owned and P01-retained**, named to the function and defect.
> Amplification path and blast-radius measurement: **P03-owned, FACT VERIFIED**.
> The sane-GL mechanism: **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE**.
> Remediation sequencing: **BOSS DECISION REQUIRED**, package in `P03_TO_P11_HANDOFF.md`.

**No repair, write, post or restore was performed or attempted.**
