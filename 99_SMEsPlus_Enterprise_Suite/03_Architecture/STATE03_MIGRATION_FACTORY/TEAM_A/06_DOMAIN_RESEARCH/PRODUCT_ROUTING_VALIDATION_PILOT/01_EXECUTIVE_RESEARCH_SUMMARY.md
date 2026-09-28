> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx8)

## Scope

Four functions: the Product Type × Track Inventory classification model itself, consumable expense timing, storable/COGS expense timing, and service routing.

## Headline finding — confirms the Backbone Roadmap's own rule, with a precise mechanism

The Backbone Roadmap states `Consumable / Service != Inventory-managed stock fact` as a target-design input requiring reconciliation. This Gx's documentation evidence **confirms** it directly: only a Goods-type product with Track Inventory enabled enters Stock Truth at all; Consumable (Goods, Track Inventory off) and Service never do. This is Confirmed, not merely assumed — see `RTG-F01`/`CQS-RTG-01`.

## Second finding — the accounting-timing distinction is exactly the Anglo-Saxon consumable/storable split

"Consumables are expensed when the corresponding vendor bill is posted, whereas storable goods are expensed when the customer invoice is posted." This isn't a new mechanism — it's the textbook Anglo-Saxon accounting rule (consumables never become a balance-sheet asset, so they expense on purchase; storables sit on the balance sheet as inventory until sold, expensing as COGS on sale) — but this Gx is the first to state it this specifically for this Deep Study, and it slots cleanly into the Gx6 "post at financial-transaction time" model: for a consumable, the *vendor bill* is the relevant financial transaction (there's no future customer sale event that matters for its own value); for a storable, the *customer invoice* is (matching Gx2's finding exactly).

## Not established

Full runtime confirmation, as always. Whether the "Track Inventory" toggle can be changed after a product already has transaction history (a forum thread title suggested this is a real user question, not opened/read this round).
