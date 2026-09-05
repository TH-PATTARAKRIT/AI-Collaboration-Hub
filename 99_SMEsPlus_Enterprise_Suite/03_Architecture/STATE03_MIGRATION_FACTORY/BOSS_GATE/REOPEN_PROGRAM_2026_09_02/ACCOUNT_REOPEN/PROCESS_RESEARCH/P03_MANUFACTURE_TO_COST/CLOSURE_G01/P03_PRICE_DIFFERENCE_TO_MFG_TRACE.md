# P03 — PRICE DIFFERENCE → MANUFACTURING TRACE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-01`.

---

## 1. What economic amount the final P01 mechanism produces

| Field | P01's final position |
|---|---|
| Mechanism | vendor-bill price-difference correction, `account.move.line._create_in_invoice_svl` |
| Amount | `unit_valuation_difference = price_unit − layers_price_unit[layer]`, applied over `out_qty = po_line.qty_received − Σ layers.remaining_qty` |
| Unit | **one vendor-bill line**, joined to a PO line, joined to that PO line's valuation layers |
| Denominator | **14,335** bill lines carrying a `purchase_line_id` (positive control); 14,312 product-matched; **23** mismatched; **18** valid on posted bills; **13** where the base method returns ≥1 layer and the filter actively drops them |
| Live effect | the correction is **skipped** where overlap is nil, and **computed on the wrong basis** where overlap is partial |

**P03 does not restate this as its own.** It is consumed at `b820b29` and attributed.

## 2. Does that amount change RM valuation?

**Yes — that is the mechanism's purpose.** The correction writes a valuation layer against the
received material, altering the raw material's cost. Where the filter empties the layer set,
**the correction does not happen**, so RM valuation retains the receipt price.

## 3. Does the effect reach manufacturing?

> **Yes, but only as an input, and by a route that carries no lineage.**

| Question | Answer |
|---|---|
| Does manufacturing read the correction? | **No.** `_cal_price` reads the *value of the consumed layers*, whatever it is |
| Does manufacturing know a correction occurred? | **No.** No field, flag or reference distinguishes a corrected layer from an uncorrected one |
| Does manufacturing participate in the filter chain? | **No** — `MD-03`, no `mrp*` module defines the method in either available series |
| So what reaches manufacturing? | **A number.** The RM unit cost, corrected or not, corrupt or not |

> **`P03C-F-01`. The purchase price-difference effect reaches manufacturing only as a changed
> unit cost, with no lineage marker of any kind.** Manufacturing cannot tell a corrected cost
> from an original one, nor a corrupt one from a sound one. This is the same structural
> property that let the 10²¹ explosion pass through `_cal_price` unchallenged (`CQ-P03-04`).
> `FACT VERIFIED` for series 18 by direct read; **P01 reports the same shape for series 16**.

## 4. Prior counts and units — why they differed

| Count | Unit | Population | Value | Status |
|---|---|---|---|---|
| P01, earlier | bill lines "affected by the kit filter" | assumed kit-gated | withdrawn | **superseded — the filter has no kit predicate** |
| P01, final | bill lines where the filter drops ≥1 layer | 14,335 with a `purchase_line_id` | **13** | current |
| P03, round 4 | corrupt valuation rows | 74,982 valuation rows | **30** | current |
| P03, round 4 | manufacturing-origin corrupt rows | the 30 | **18** | current |

**These are four different units over three different populations and none contradicts
another.** The 13 and the 30 are unrelated sets measured for unrelated purposes — the 13 is
*corrections not applied*, the 30 is *values already corrupt*. Recorded explicitly so a later
reader does not net them.

## 5. Subcontracting — the series split P01 supplies

| Series | Subcontract extra cost derived from |
|---|---|
| **18** | the **receipt's** price unit — P03's `OWN-03` premise **stands** |
| **19** | the **vendor bill first**, PO for the unbilled remainder, receipt only as a fallback — P03's premise **does not hold** |

**P03's `DEP-06` remains OPEN for series 18**, as P01 states, and P01 has no deployment to
test it in: subcontracting is installed in **one** of three deployments — the one with **10
journal entries in total** — and **zero subcontract transactions** have been observed.

The series-18 **credit-split construct** (component cost vs subcontracting service cost) is
**CONTRADICTED for series 19** — it is gone. **P03's cost model must not assume it.**

## 6. Disposition

> **`CQ-P03-01` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for what enters
> manufacturing and by what route.
> **`DEP-06` (series-18 FIFO/average bill-difference path) remains `UNRESOLVED — SPECIFIC
> EVIDENCE UNAVAILABLE`** — no deployment exercises it.
> The mechanism itself is **P01-owned**; P03 states only the interface.
