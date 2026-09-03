# 13 — Post-Depreciation Internal Usage Costing (Boss-Approved Business Intent, Worked as a Design Candidate)

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `DESIGN CANDIDATE ANALYSIS — NOT AN ACCOUNTING FACT`

---

## 1. Scope and Framing

Per governing brief section 19 and the workflow instruction: this file rigorously works through the Boss-approved post-depreciation internal usage formula — **Residual Book Value × Original Depreciation Cost Rate ÷ Original Cost Base**, and a daily-rate variant — as a `DESIGN CANDIDATE`. It is explicitly Boss-approved *business intent*, not a verified accounting fact (file `10` establishes there is no statutory or reference-ERP precedent for it), and this file does not hard-code monthly logic.

## 2. The Formula, Restated Precisely

`Internal Usage Cost (period) = Residual Book Value × (Original Depreciation Cost Rate ÷ Original Cost Base)`

Where, on a plain reading:
- **Residual Book Value**: the not-depreciable/salvage value fixed at asset setup (file `09` — the portion structurally excluded from the depreciable base, remaining on the books at full depreciation).
- **Original Depreciation Cost Rate**: the periodic depreciation amount the asset used to generate while still actively depreciating (e.g., the straight-line monthly/annual charge it had before reaching full depreciation).
- **Original Cost Base**: the Original Value (or Depreciable Value — this is the first ambiguity, addressed in §3) the rate was originally calculated against.

The daily-rate variant substitutes a per-day figure for Original Depreciation Cost Rate and applies it to however many days the period covers, rather than treating the period as one indivisible unit — directly analogous to the reference-ERP's own documented "Based on days per period" prorata option (file `07` §2), which is useful precedent for the *mechanical shape* of a daily rate even though it has no precedent for *this specific post-depreciation application*.

## 3. Candidate Base Question: Which Base Is Canonical?

The governing brief explicitly asks this file to investigate whether the canonical base should be Original Value, Depreciable Base, Gross Carrying Amount, residual-adjusted base, or a daily rate — not to assume Original Cost Base means any one of these. Working through each:

| Candidate base | What it means | Trade-off |
|---|---|---|
| **Original Value** (full purchase cost, including the residual portion) | Rate = original periodic depreciation charge ÷ full original cost | Simple, matches "Original Cost Base" most literally by name. But mixes a rate computed against the *full* asset value with a *Residual*-Book-Value numerator that was, by definition, never part of the depreciated portion — a base/numerator mismatch that could understate or overstate depending on how large the residual carve-out was relative to total cost. |
| **Depreciable Base** (Original Value − Not Depreciable Value, i.e., the amount that was actually depreciated) | Rate = original periodic depreciation charge ÷ depreciable base | More internally consistent: the rate reflects value actually consumed per period, over the base actually consumed. This produces a rate of exactly 100%/schedule-length by construction, which may be too blunt (it just reproduces the average periodic depreciation rate) unless intentionally desired. |
| **Gross Carrying Amount** (accounting term for the asset's cost before any accumulated depreciation is netted — effectively the same figure as Original Value in the absence of revaluation) | Functionally equivalent to Original Value under a cost-model asset (no revaluation) — Thai practice under TAS 16 is generally cost-model, so this likely collapses to the same number as "Original Value" for SMEsPlus's use case, though the governing brief treats them as separately worth investigating, which this file does, concluding they are likely synonymous absent revaluation. | Same trade-off as Original Value above |
| **Residual-adjusted base** | A base that itself nets out the residual amount from whichever of the above is chosen — this is really a modifier on the other options, not a fifth independent option | Adds a layer of internal consistency (matching the numerator's residual nature) at the cost of additional complexity and another design decision (how exactly to net it) |
| **Daily rate** | Not a "base" at all — a different unit of the *rate* term, converting whatever periodic rate is chosen into a per-day figure | Orthogonal axis, not a competing base — can be combined with any of the above base choices |

**No single answer is asserted here as correct** — this is precisely why the file is a `DESIGN CANDIDATE` analysis, not a resolution. The Depreciable Base option is flagged as the most internally consistent on pure formula-construction grounds, but "most internally consistent" is not the same as "Boss-preferred" or "correct" — that decision belongs to the Boss, informed by this analysis, per file `26`.

## 4. Trade-Offs Summary

- **Original Value / Gross Carrying Amount** base: simplest to explain, but produces a rate whose denominator includes value (the residual) that was never actually depreciated, which is conceptually awkward when the numerator (Residual Book Value) is exactly that same excluded amount.
- **Depreciable Base**: mechanically self-consistent, but reduces the formula to reproducing (Residual Book Value × the average historical periodic depreciation percentage), which may or may not be the economic signal the Boss actually wants (e.g., if the intent is "charge the machine's continued use at roughly what it used to cost to own," this base achieves exactly that; if the intent is something more like a market-rate rental-equivalent charge, none of these bases achieve that — a different design entirely).
- **Daily variant**: mechanically straightforward once a periodic rate and base are chosen (divide by days in the reference period), but inherits the same unresolved Thai day-count-convention gap flagged in file `08` if it is meant to align with Thai daily tax depreciation conventions — those are two different "daily" concepts (Thai tax day-count vs. this internal formula's own day granularity) that should not be assumed identical without a separate decision.

## 5. Classification

`DESIGN CANDIDATE` throughout this file. No sub-question in this file rises to `FACT VERIFIED` or `SUPPORTED INTERPRETATION` because there is no accounting-standard or reference-ERP precedent to independently corroborate any specific base choice (file `10` §3). This is original SMEsPlus design work requiring a Boss decision among the options in §3, not a research conclusion this file can supply on its own.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
