> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx8)

### RTG-F01 — Product Type × Track Inventory classification

- **WHAT**: A product form has a **Product Type** field (Goods or Service) and, for Goods, a separate **Track Inventory** checkbox. A Goods product with Track Inventory on is storable; a Goods product with it off is what the old model called Consumable.
- **WHY**: Businesses need to distinguish physical items worth tracking at the unit/location level (raw materials, finished goods) from physical items not worth that overhead (packaging, office supplies) from pure services — but the mechanism for this in v19 is two independent fields, not three peer radio-button options.
- **BUSINESS RULE**: "Each product type impacts different operations in other Odoo applications, such as Sales and Purchase, and should be chosen carefully." Track Inventory specifically gates stock-at-locations tracking, inventory valuation, lot/serial tracking, and reordering rules.
- **STATE**: N/A — a classification, not a lifecycle.
- **DATA CONCEPT**: `(Product Type: Goods|Service) × (Track Inventory: on|off)` — the "three product types" language used elsewhere (including the Backbone Roadmap itself) is a simplification of this two-dimensional model, accurate in effect but not in literal field structure.
- **CONTROL**: This is the master gate for every other Gx's product-category-dependent functions (valuation mode, costing method, landed cost eligibility, WIP/manufacturing) — none of them apply unless Track Inventory is on.
- **DEPENDENCY**: Upstream of GRV-F04, SDV-F05, IAV-F03, MFG-F01/F02 — this Gx should have logically preceded those, but Material Delta discipline means it's added now as an upstream clarification, not a redo.
- **EVENT**: N/A.
- **RISK**: A design that treats "Stockable/Consumable/Service" as three mutually exclusive database values (rather than two orthogonal fields) risks a data-model mismatch with the reference behavior — worth flagging for any future SMEsPlus clean-room product-classification design, as a *concept to consider*, not a structure to copy.
- **UNKNOWN**: Whether Track Inventory can be toggled after a product has transaction history (a forum thread title suggests this is a live user question) — not opened/read, flagged only.

### RTG-F02 — Consumable expense timing

- **WHAT**: A Goods product with Track Inventory off is expensed when its vendor bill is posted.
- **WHY**: Since it's never tracked as inventory (no stock valuation asset is ever created for it), there's no balance-sheet asset to release later at sale — the purchase itself is the only financial event that matters for its value.
- **BUSINESS RULE**: Direct documentation quote: "consumables are expensed when the corresponding vendor bill is posted."
- **STATE**: Purchased → vendor bill posted → expensed. No stock-truth state at all (confirmed by RTG-F01).
- **DATA CONCEPT**: No stock valuation account entry ever exists for this product type.
- **CONTROL**: This is a *simpler* instance of the Gx6 rule — the financial-transaction event (vendor bill) is the only event, with no period-end accrual complexity, because there's no intermediate stock-truth state to bridge.
- **DEPENDENCY**: Independent of GRV-F01-F07 entirely — a consumable never enters the receipt-validation pilot's scope at all.
- **EVENT**: "Vendor bill posted, expense recognized."
- **RISK**: A design assuming all "goods" purchases behave like Gx1's stockable-receipt flow would be wrong for consumables specifically.
- **UNKNOWN**: None material — this is a clean, simple, fully-reconciled finding.

### RTG-F03 — Storable/COGS expense timing

> **STATUS DOWNGRADE (2026-09-29, Boss ruling).** "Independent" below refers to an independent *documentation source*, not an independent *reviewer* — this row was still authored by the same TEAM_A session as Gx2/Gx6. The underlying Gx6 resolution remains `Material Finding — Independently Unverified` pending `CHATGPT_AUDIT`. See `00_Architecture_Governance/STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`.

- **WHAT**: A Goods product with Track Inventory on is expensed (as COGS) when the customer invoice is posted, confirming Gx2's `SDV-F05` finding via an independent, more doctrinally precise source.
- **WHY**: The product sits on the balance sheet as an inventory asset from receipt until sale, at which point its cost is released to the income statement as COGS.
- **BUSINESS RULE**: Direct documentation quote: "storable goods are expensed when the customer invoice is posted." This is the textbook Anglo-Saxon accounting model.
- **STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: Identical to Gx2's `SDV-F05` and Gx6's `PCO-F03` — this row exists to record that a *third, independent* documentation source states the same rule, strengthening (not just repeating) the existing resolution.
- **RISK**: None new — this closes out any remaining doubt about the Gx6 resolution's correctness for the storable-goods case specifically.
- **UNKNOWN**: None material beyond what Gx6/Gx7's AWT backlog already covers.

### RTG-F04 — Service routing

- **WHAT**: A Service-type product never has stock-truth state; its "Invoicing Policy" field (same field family as `SDV-F04`) still governs revenue-recognition timing on the sales side.
- **WHY**: Services are never physical, so Stock Truth is categorically inapplicable — but revenue timing (ordered vs. delivered — for a service, presumably "ordered vs. performed/rendered") is still a live business question.
- **BUSINESS RULE**: "The Invoicing Policy field appears on the product form only when a product is for sale" — i.e., it's a Sales-side concept applicable regardless of product type, not specific to stockable goods.
- **STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: N/A for Stock Truth; Financial Truth timing follows the same Invoicing Policy mechanism documented in Gx2.
- **RISK**: None identified — this function's main value is confirming exclusion, not revealing new complexity.
- **UNKNOWN**: What "delivered quantities" means operationally for a Service (there's no physical delivery to validate) — not evidenced this round; presumably some manual/timesheet-based trigger, not confirmed.
