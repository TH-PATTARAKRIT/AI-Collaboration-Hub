> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx4)

## Scope

Six functions identified (`04_FUNCTION_REGISTER.md`): recording a physical count, applying the adjustment (single or batch-with-reason), the resulting financial posting, scrap/inventory-loss handling (its own dedicated account concept), cycle-count scheduling, and reversing/correcting an applied adjustment.

## Material finding

Documentation states plainly that inventory-adjustment changes "update the Balance Sheet as soon as they are applied, there are no additional steps needed." This is now the **third** documentation-tier data point (after Gx1's generic "perpetual valuation" claim and Gx2's "perpetual-at-invoicing" claim) bearing on the same open valuation-timing question. Rather than treat this as resolving the question, it is logged as a third data point in the same `GAP-...-01`-class Evidence Conflict lineage (`GAP-IAV-01`), because it may describe a genuinely different case (a manual count/adjustment, which has no "invoice" event to defer to — unlike a receipt or delivery) rather than contradicting the other two claims.

## Second finding: Scrap has its own dedicated account, distinct from ordinary adjustment

Scrapping goods requires an explicit **Loss Account** on the destination location (an "Inventory Loss" location type), separate from the general Stock Valuation account — e.g. a documented example names a "Scrapped Goods" journal/account. This means "Inventory Adjustment" is not one uniform function for accounting purposes — ordinary count corrections and scrap both move quantity out of stock, but only scrap is documented as requiring its own dedicated loss-account configuration. Recorded as `IAV-F04`, distinct from `IAV-F03`.

## Not established

No source/runtime access, as with all prior Gx. AWT backlog prepared instead.
