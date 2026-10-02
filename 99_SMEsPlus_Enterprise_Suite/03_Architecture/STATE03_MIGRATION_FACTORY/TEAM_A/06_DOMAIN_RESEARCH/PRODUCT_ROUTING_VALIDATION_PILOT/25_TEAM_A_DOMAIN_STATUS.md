> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS (Gx8)

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| RTG-F01 Product Type × Track Inventory | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-RTG-01`) |
| RTG-F02 Consumable expense timing | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable); high documentation confidence, clean/simple mechanism |
| RTG-F03 Storable/COGS expense timing | **C1** | V5/floor V4 | V2 | Blocking Unknown; 4th independent confirmation of the Gx6 rule |
| RTG-F04 Service routing | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-RTG-02`) |

## Next action

(1) Fold RTG-F02/F03 into the existing AWT capstone session (add a Consumable-product test case alongside the storable/receipt/delivery/adjustment/manufacturing cases); (2) surface `CQS-RTG-02`'s finding (Product Type × Track Inventory, not three peer types) to whoever next revises the Backbone Roadmap document; (3) continue to Gx9 (Multi-company/Tenant isolation) per Boss's order.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`. Ready for CHATGPT_AUDIT.
