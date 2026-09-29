> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-BRP-01 | Does sending components to a subcontractor reduce your own stock valuation, the way shipping to a customer would? | Assumed: yes, valuation follows physical location | **Contradicted** | Official documentation states explicitly that subcontracting does not impact inventory valuation — the destination is modeled as an Internal Location, not external. |
| CQS-BRP-02 | Does a Kit product carry its own independent stock value, separate from its components? | Assumed: a sellable product always has its own valuation line | **Contradicted** | Documentation states "Kit Value Does Not Change" — value lives entirely at the component level; the kit is a bundling label, not a valuation object. |
| CQS-BRP-03 | Is "Routing" a separate master-data object from the Bill of Materials, as in some other MRP systems? | Assumed: routing exists independently of BOM | **Contradicted (for this documentation pass)** | Odoo 19 documentation this round describes Operations as entries *on* the BoM itself (an Operations tab), not a standalone Routing record — not independently confirmed against source; flagged, not assumed further. |

## Status

`CLOSED (documentation-tier)`: CQS-BRP-01, CQS-BRP-02, CQS-BRP-03.

No round cap. Further challenge questions may be added on a follow-on pass (Master Production Schedule, byproducts, multi-level BOM).
