# 10 — JT-05 Fact Package: Return Cost Basis (C-03)

Source definition: `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` — "`JT-05` | Return cost basis (`C-03`). | Return flows"

This is the second priority cluster the parent prompt names as previously found "not decidable from documentation alone," and is separately flagged in DR file `30` §11 as **the single most material cross-cutting finding** alongside `JT-04`.

## 1. What Is Already Established (Fact) — `CGS-U32`

- Under **AVCO**, a customer return is valued at the **average cost prevailing at the time of the return**, not the original cost at which the item was sold. The average is not recalculated retroactively.
- Under **FIFO**, layer-consumption behavior on return is only **community-corroborated**, not primary-documented — a materially weaker evidence tier than the AVCO finding.
- A **documented, unreconciled discrepancy** exists between (a) the financial-reversal amount on a credit note and (b) the independently-computed inventory-valuation reversal amount. The reference system's own stated resolution for this discrepancy is **"manual adjustment"** — i.e., the vendor's own documentation admits the two sides do not automatically agree.
- A later-period return carries **three independently-settable dates** — original sale date, physical return date, credit-note reversal date — with **no forced alignment** between them.
- The reference ERP's own feature-level "Returns and refunds" documentation is **completely silent on cost basis** (`CGS-U33`); the cost-basis answer had to be assembled from a separate, non-cross-referenced documentation surface — described in DR file `19` as a genuine usability/evidence gap in the reference system itself, not a research shortfall.

## 2. Fact vs. Configuration vs. Interpretation vs. Assumption vs. Target Design

| Layer | Statement |
|---|---|
| **FACT** | The AVCO current-cost-on-return behavior, the credit-note-vs-inventory discrepancy, and the "manual adjustment" stated remedy are each independently documented in the reference ERP's own material (DR file `19` §2, §6). |
| **CONFIGURATION** | Which costing method (AVCO vs. FIFO vs. Standard) a given category/product uses determines which of these sub-cases applies — this is a per-tenant configuration fact. |
| **INTERPRETATION** | Calling this "the single most material carried-forward item in the package" (DR file `30` §6) is this research's own materiality judgment, based on the discrepancy being *admitted by the vendor itself* rather than merely undocumented — a stronger signal than most other unknowns in the register. This session concurs with that judgment on the evidence presented. |
| **ASSUMPTION** | There is no evidence that Thai accounting standards mandate a specific return-cost-basis mechanism beyond general inventory-costing consistency requirements (TAS 2, already researched in DR file `24`) — whether TAS 2's general principles resolve the AVCO-current-vs-original-cost question specifically was not tested against the return scenario in that research pass. This is a distinct, not-yet-closed thread, same pattern as `JT-04`'s Thai-timing gap. |
| **TARGET DESIGN** | SMEsPlus's own return-cost-basis rule (original cost, current cost, or another rule; how the financial and inventory reversal amounts will be forced to reconcile or explicitly allowed to diverge with a control) is not decided by this file. |

## 3. Why This Cannot Be Closed by Documentation Alone

Two independent reasons, both evidence-backed:

1. The **FIFO sub-case** rests on community corroboration only — closing it with confidence requires either a live reference-instance test or a primary-source citation that was not found in the DR pass (`OPEN — LIVE INSTANCE REQUIRED` per file `03`).
2. Even where the reference behavior IS well-documented (AVCO), it is documented as **internally inconsistent by the vendor's own admission** ("manual adjustment" as the stated fix). There is no "correct" reference answer to adopt — only a documented control gap. SMEsPlus must design its own reconciliation control; no amount of further reading of the same reference material resolves this, because the material itself describes an unresolved gap.

## 4. Disposition

**HOLD — EVIDENCE REQUIRED (FIFO sub-case), WITH A DESIGN LAYER ON TOP (AVCO sub-case).** The AVCO fact pattern is FACT VERIFIED as a description of reference-system behavior, including its own internal inconsistency. The FIFO fact pattern is PARTIALLY VERIFIED at best (community evidence only). Neither sub-case gives SMEsPlus an adoptable answer — the AVCO case is a documented anti-pattern (a gap the reference itself patches manually), not a design to copy.

## 5. Does New Evidence Materially Change the Proposed Disposition?

No new runtime evidence was acquired. This session's contribution: confirming the discrepancy is genuinely vendor-admitted (not an inference by the DR researchers), which raises confidence that this is real, not overstated, and therefore reinforces rather than softens its `BLOCKING` severity. This session also recommends, as a concrete next step, testing whether Thai TAS 2's inventory-costing-consistency principle constrains the *choice* between original-cost and current-cost return valuation even though it does not name returns explicitly (routed to file `13`).
