> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx8)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-RTG-01 | Is "Consumable != Inventory-managed stock fact" (Backbone Roadmap's own stated rule) actually true in the reference system? | Could have been merely a Boss target-design assumption, not a proven reference fact | **Confirmed** | Track Inventory off means no stock-at-locations, no valuation, no lot/serial tracking, no reordering rules — categorically excluded from Stock Truth. |
| CQS-RTG-02 | Is "Stockable/Consumable/Service" really three independent, mutually exclusive product types in Odoo 19? | Assumed: yes, three peer options (also assumed by the Backbone Roadmap's own phrasing) | **Contradicted** | It's two orthogonal fields (Product Type: Goods/Service, and Track Inventory: on/off for Goods) — the "three types" framing is a simplification, not the literal structure. Worth flagging to whoever owns the Backbone Roadmap document, since it uses the three-way framing too. |
| CQS-RTG-03 | Does the consumable/storable expense-timing split match this Deep Study's general "post at financial-transaction time" rule? | Independent verification of the Gx6 resolution | **Confirmed, and clarifies which transaction applies to which product type** | Consumable → vendor bill is the relevant transaction (no future sale event matters for it); Storable → customer invoice is (matches Gx2 exactly). |

## Status

`CLOSED (documentation-tier, high confidence)`: all three — this Gx had unusually clean, convergent evidence.

**Recommendation for Boss/PMO**: `CQS-RTG-02`'s finding (two fields, not three types) is worth surfacing to whoever maintains `STATE03_ACCOUNTING_INVENTORY_BACKBONE_EXECUTION_ROADMAP.md`, since that document's own §4 table uses the three-type framing. Not changed here — that document is outside this Deep Study's own artifact set — flagged for Boss's attention via `STATE03_BOSS_GATE_QUEUE.md` is not appropriate either (not a Boss-only decision), so this is simply noted here for whoever next touches that Roadmap document.
