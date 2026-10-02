> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Function Universe + Criticality

# 04 — FUNCTION REGISTER (Gx5)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| PDT-F01 | Per-shipment invoicing alignment (sales) | Whether each partial delivery gets its own timely invoice, or invoicing waits for full completion | **C1** | Financial-timing question, directly evidenced this round. |
| PDT-F02 | Per-receipt billing alignment (purchase) | Whether each partial receipt supports its own bill, tracked via shared Bill Reference | **C1** | Mirror of PDT-F01 on the purchase side. |
| PDT-F03 | Bill-before-receipt anomaly | Community-reported case of bill creation preceding receipt under "received quantities" policy | **C1** | Directly corroborates the open GRV-F06 soft-control finding; potential control gap or version nuance. |
| PDT-F04 | Cross-shipment quantity/bill reconciliation | How multiple partial receipts/bills against one PO are kept reconciled (shared Bill Reference) | **C2** | Data-integrity function — wrong reconciliation risks double-billing or under-billing across partials. |
