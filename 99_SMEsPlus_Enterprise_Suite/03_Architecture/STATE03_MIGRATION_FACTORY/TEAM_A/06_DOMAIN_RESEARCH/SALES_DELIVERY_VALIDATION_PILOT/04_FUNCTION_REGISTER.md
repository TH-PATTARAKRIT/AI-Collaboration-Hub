> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Module Function Universe + Criticality | Documentation-Tier

# 04 — FUNCTION REGISTER (Gx2)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| SDV-F01 | Delivery routing configuration (1/2/3-step) | Whether goods move stock→customer directly, or via pick/pack/output intermediate steps | **C3** | Configuration/procedural surface, mirrors GRV-F01. |
| SDV-F02 | Physical delivery execution (move to customer) | Confirming delivered quantity, moving stock out of a stock-owned location | **C2** | Creates the outbound Stock Truth fact; mirrors GRV-F02. |
| SDV-F03 | Partial delivery / backorder handling | Delivering less than ordered; system behavior for the remainder | **C2** | Quantity-integrity function, mirrors GRV-F03; documentation shows both delivered and invoiced quantities are tracked, backorders created for the remainder. |
| SDV-F04 | Invoicing policy (ordered vs. delivered quantities) | Whether a customer invoice can be created before or only after delivery | **C1** | Financial-control gate — mirrors GRV-F06 (bill control) but on the revenue side; "delivered quantities" policy structurally requires SDV-F02 to occur first. |
| SDV-F05 | COGS / valuation timing at delivery | Whether/when a delivery creates a GL-relevant COGS entry, under perpetual vs. periodic and considering the Odoo 19 invoice-timing change | **C1** | Directly determines Financial Truth timing and amount; **this is where GAP-SDV-01 (cross-Gx contradiction) lives.** |
| SDV-F06 | Return via Reverse Transfer (pre-invoice) | Customer returns goods before an invoice was sent/validated | **C2** | Stock-truth reversal; mirrors GRV-F07 (which Gx1 had zero evidence for) — this Gx supplies the first real evidence for that mirrored function, see `22_UNKNOWN_AND_GAPS.md`. |
| SDV-F07 | Return after invoicing, via Credit Note | Customer returns goods after invoice was sent/validated — a Reverse Transfer alone is documented as insufficient | **C1** | Financial-correction control: a validated invoice cannot be changed, so a Credit Note is the documented instrument; directly touches Financial Truth reversal. |

## Cross-reference to Gx1

SDV-F06/F07 give this Deep Study its first real documentation evidence for a "reversal of a completed stock movement" function — Gx1's mirrored function (`GRV-F07`, receipt-side reversal) remains undocumented (`GAP-GRV-06`, still open) and should be closed next using the same search pattern that produced SDV-F06/F07, rather than starting from zero.
