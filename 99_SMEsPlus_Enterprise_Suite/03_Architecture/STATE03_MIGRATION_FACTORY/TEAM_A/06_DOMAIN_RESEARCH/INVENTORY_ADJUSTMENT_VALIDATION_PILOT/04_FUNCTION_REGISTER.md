> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Function Universe + Criticality | Documentation-Tier

# 04 — FUNCTION REGISTER (Gx4)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| IAV-F01 | Physical count recording | Entering a counted quantity against a product/location's system quantity | **C2** | Stock Truth input; no financial effect by itself until applied. |
| IAV-F02 | Applying the adjustment (single / Apply All with reason) | Committing the counted quantity as the new system quantity | **C2** | Creates the authoritative Stock Truth delta. |
| IAV-F03 | Financial posting of the adjustment | Whether/when the quantity delta creates a GL entry | **C1** | Third data point on the recurring valuation-timing question (`GAP-IAV-01`). |
| IAV-F04 | Scrap / Inventory Loss location + Loss Account | Scrapping goods to a dedicated loss location with its own account | **C1** | Distinct, dedicated financial-control surface, separate from ordinary adjustment. |
| IAV-F05 | Cycle count scheduling (Inventory Frequency) | Per-location automatic scheduling of the next count date | **C3** | Configuration/scheduling only, no direct financial or quantity effect. |
| IAV-F06 | Reversal / correction of an applied adjustment | Undoing or correcting a previously applied count | **C2** | Mirrors the reversal theme from Gx1/Gx2; not yet evidenced this round (see Gap Register). |
