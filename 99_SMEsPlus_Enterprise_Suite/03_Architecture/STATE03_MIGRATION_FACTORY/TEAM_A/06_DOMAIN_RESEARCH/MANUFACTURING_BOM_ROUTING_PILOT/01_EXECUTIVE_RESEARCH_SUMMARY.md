> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Executive Summary | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY

## Material finding — a real financial-control surface: the Subcontracting Location's type

> **Classified (Boss's Corrective Checkpoint §B4): `Conditional Reference Finding` — version/module/configuration/evidence-pointer scoped, not a universal statement, not SMEsPlus target behavior. See `06_BUSINESS_RULE_REGISTER.md` BRP-F03.**

The clearest, most consequential finding this round is `BRP-F03`: Odoo 19 keeps outsourced-production components inside your own inventory valuation by modeling the subcontractor's premises as an **Internal Location**, not an external/Customer-type one. This is a genuine configuration-dependent financial-control point — if a Subcontracting Location were ever set up as external, sending components to a subcontractor would incorrectly drop them from stock valuation, understating the balance sheet for the entire outsourced-production window. Criticality: **C1**. The other half of this function — how the subcontractor's own fee is captured — closed the same day: the vendor bill for the subcontracting service, once posted, debits the Finished Goods Valuation Account, folding component cost + fee into one figure at vendor-bill time (consistent with, not a further self-confirmation of, the Boss-flagged valuation-timing Material Finding).

## Structural finding — BoM Type is the router, not a detail

`BRP-F01` (BoM Type: Manufacture / Kit / Subcontracting) is the single field that determines which of three structurally different stock-and-financial models applies to a product. Gx7's entire valuation-timing scope (`MANUFACTURING_VALUATION_PILOT`) turns out to be the "Manufacture this product" branch specifically — Kit (`BRP-F02`) has no manufacturing financial event at all (component value passes through unchanged), and Subcontracting (`BRP-F03`) has its own distinct model. This pilot did not contradict Gx7; it located Gx7 as one of three branches and characterized the other two.

## Cost-input finding — Work Centers and Routing feed, but do not replace, Gx7's cost computation

`BRP-F04` (Work Center Cost per hour) and `BRP-F05` (Routing Operations, expected duration) are the two inputs that combine into the operations-cost component Gx7's `MFG-F04` already treats as a black-box input ("component cost + operations cost, per BOM"). This pilot opens that box: operations cost = Σ(Work Center Cost per hour × Operation expected duration) — not independently confirmed against Odoo's actual computation formula, recorded as `SOURCE/RUNTIME VERIFICATION REQUIRED`.

## Follow-on pass (2026-09-29, same day): Reordering Rules, MPS, By-Products, Multi-level BOM

Per Boss's instruction to continue this module automatically, 4 further functions were added: `BRP-F06` (Reordering Rules) and `BRP-F07` (Master Production Schedule) — found to be **explicitly mutually exclusive per product**, a genuine business-rule contradiction the documentation itself warns against combining; `BRP-F08` (By-Products) — a second C1 finding, structurally identical in shape to `BRP-F03`'s open half: a real value-allocation question (this time between primary and secondary output) not yet evidenced; `BRP-F09` (Multi-level BOM) — confirms recursive resolution and flags that every other function in this pilot compounds at each level of a nested structure.

## Scope discipline

9 functions researched (`BRP-F01`–`F09`), all at documentation-tier (V2), 0 at V0/V1. Not researched this round, explicitly out of scope: quality-checkpoint integration with manufacturing, dropshipping-manufacturing interaction. These remain candidates for a further follow-on pass, not silently declared complete.

## Status

Documentation-tier only (V2 for all 5 functions). Not a Gate PASS, not Team B design input, not STATE03 completion. Ready for the same `CHATGPT_AUDIT` / PMO chain as every other Deep Study unit once queued.
