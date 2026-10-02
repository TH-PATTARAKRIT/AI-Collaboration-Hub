> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Function Universe + Criticality

# 04 — FUNCTION REGISTER (Gx8)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| RTG-F01 | Product Type × Track Inventory classification | The actual v19 model replacing the old 3-way Storable/Consumable/Service split | **C2** | Gating classification — determines which of every other Gx's functions even apply to a given product. |
| RTG-F02 | Consumable expense timing | Goods, Track Inventory off — expensed at vendor-bill time | **C1** | Financial-timing rule, distinct from storable goods. |
| RTG-F03 | Storable/COGS expense timing | Goods, Track Inventory on — expensed at customer-invoice time | **C1** | Confirms Gx2's finding via an independent, more precise accounting-doctrine source. |
| RTG-F04 | Service routing | Never enters Stock Truth; Invoicing Policy still applies for revenue timing | **C2** | Confirms the Backbone Roadmap's Service exclusion directly. |
