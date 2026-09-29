> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-BRP-01 | Does sending components to a subcontractor reduce your own stock valuation, the way shipping to a customer would? | Assumed: yes, valuation follows physical location | **Contradicted** | Official documentation states explicitly that subcontracting does not impact inventory valuation — the destination is modeled as an Internal Location, not external. |
| CQS-BRP-02 | Does a Kit product carry its own independent stock value, separate from its components? | Assumed: a sellable product always has its own valuation line | **Contradicted** | Documentation states "Kit Value Does Not Change" — value lives entirely at the component level; the kit is a bundling label, not a valuation object. |
| CQS-BRP-03 | Is "Routing" a separate master-data object from the Bill of Materials, as in some other MRP systems? | Assumed: routing exists independently of BOM | **Contradicted (for this documentation pass)** | Odoo 19 documentation this round describes Operations as entries *on* the BoM itself (an Operations tab), not a standalone Routing record — not independently confirmed against source; flagged, not assumed further. |

| CQS-BRP-04 | Can Reordering Rules and the Master Production Schedule both apply to the same product for complementary coverage? | Assumed: yes, they'd naturally complement each other (immediate vs. long-term) | **Contradicted** | Documentation explicitly warns against combining them on the same product — doing so creates inaccurate forecasts and unnecessary replenishment orders. |
| CQS-BRP-05 | Are by-products treated as waste/scrap, with no separate valuation? | Assumed: a secondary output is a disposal record, not inventory | **Contradicted** | By-products are declared, trackable inventory with their own stock/valuation identity, not a scrap record. |
| CQS-BRP-06 | Does a multi-level BOM require the top-level user to manually trigger each sub-assembly's own manufacturing order? | Assumed: manual cascade, one MO at a time | **Contradicted** | Confirming the top-level MO is documented as automatically generating the necessary manufacturing/purchase orders down the whole chain, not requiring manual triggering at each level. |

## Status

`CLOSED (documentation-tier)`: CQS-BRP-01, CQS-BRP-02, CQS-BRP-03, CQS-BRP-04, CQS-BRP-05, CQS-BRP-06.

No round cap. Further challenge questions may be added on a subsequent follow-on pass if one is authorized (e.g., quality-checkpoint integration with manufacturing, which remains out of scope for this pilot).
