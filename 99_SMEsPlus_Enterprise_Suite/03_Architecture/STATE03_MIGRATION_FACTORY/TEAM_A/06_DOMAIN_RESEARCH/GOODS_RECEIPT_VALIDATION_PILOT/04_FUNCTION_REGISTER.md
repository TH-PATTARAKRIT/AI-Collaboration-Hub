> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Module Function Universe (Master Prompt §4.1) + Criticality Matrix (§4.3) | Documentation-Tier | Non-frozen denominator

# 04 — FUNCTION REGISTER (Module Function Universe + Criticality)

Denominator is explicitly **not frozen** (Master Prompt §12 Phase A Step 3). These 7 functions are the candidate population discovered from documentation this round; more may be added on Material Delta.

| ID | Function (neutral name) | Scope note | Criticality | Criticality reason (evidence-based) |
|---|---|---|---|---|
| GRV-F01 | Receipt routing configuration (single/multi-step) | Whether goods move vendor→stock directly, or via input/quality intermediate steps | **C3** | Configuration surface only; does not itself alter financial or stock-quantity truth, only the physical/procedural path. |
| GRV-F02 | Physical receipt execution (move to stock) | The act of confirming received quantity and moving stock into a stock-owned location | **C2** | Directly creates the Stock Truth fact the Backbone Roadmap's Lane C depends on; incorrect execution corrupts on-hand quantity but is inventory-scoped until valuation attaches. |
| GRV-F03 | Partial receipt / backorder handling | Receiving less than ordered; system behavior for the remaining quantity | **C2** | Quantity-integrity function; documented as user-triggered (edit + validate), not silent — see CQS-GRV-02. Wrong handling causes duplicate or lost quantity, but is still inventory-scoped. |
| GRV-F04 | Inventory valuation at receipt (perpetual vs periodic; costing method) | Whether/when a stock-in creates a GL-relevant value, and how FIFO/AVCO/Standard determine that value | **C1** | Directly determines Financial Truth (GL posting timing and amount) per the Backbone Roadmap's "Inventory owns stock truth, Accounting owns financial truth" boundary. Errors here are financial-statement-material. |
| GRV-F05 | Landed cost allocation onto received goods | Additional cost (freight, duty, etc.) allocated onto the received stock's valuation | **C1** | Alters the financial value basis of inventory and, downstream, COGS; gated by Product Category costing method, not by valuation method (material finding, see CQS-GRV-03). |
| GRV-F06 | Three-way match / bill control policy | Whether vendor-bill creation/payment is gated on quantity received vs quantity ordered | **C1** | Financial-control / authorization function (Backbone Roadmap Lane C, AP boundary); documentation indicates this is a **soft/informational** control (`Should Be Paid` flag), not a hard block — a control-design-relevant nuance, not yet runtime-confirmed. |
| GRV-F07 | Reversal / return of received goods | Undoing a previously validated receipt, in full or in part | **C2** | Maps directly to Backbone Roadmap Lane C proof scenario #3 ("Return / Reversal -> Stock reversal -> Financial correction/reversal interface"); not yet documentation-evidenced in this round (see GAP-GRV-07 in `22_UNKNOWN_AND_GAPS.md`) — Criticality assigned by cross-module dependency, not by direct evidence yet. |

## Criticality legend (Master Prompt §4.3, applied)

- **C1** — direct financial-statement or hard financial-control impact.
- **C2** — direct inventory/stock-truth impact, financial impact only via handoff.
- **C3** — configuration/procedural impact only.
- **C4** — cosmetic/reporting-only (none identified in this pilot yet).

## Note on GRV-F07

Assigned Criticality by architectural inference (it is the explicit Lane C proof scenario #3), not by direct documentation evidence gathered this round — this is flagged, not hidden, per Master Prompt §2.7 ("No Evidence = No Progress. Unknown is valid; unsupported certainty is not.").
