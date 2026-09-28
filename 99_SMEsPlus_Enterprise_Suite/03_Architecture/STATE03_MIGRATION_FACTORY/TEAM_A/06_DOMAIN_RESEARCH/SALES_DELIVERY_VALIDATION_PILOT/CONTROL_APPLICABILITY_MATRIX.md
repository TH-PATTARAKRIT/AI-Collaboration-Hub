> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Control Applicability Matrix | Documentation-Tier

# CONTROL APPLICABILITY MATRIX (Gx2)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | SDV-F04/F05: invoicing-policy gate and COGS timing directly affect Financial Truth. |
| Inventory | **Applicable** | SDV-F02/F03/F06: delivery, backorder, and return are Stock Truth events. |
| Authority (approval/execute/post/reverse) | **Applicable, partially evidenced** | SDV-F04's "delivered quantities" gate is a structural control (stronger than Gx1's informational GRV-F06 finding); SDV-F07 shows a distinct financial-reversal instrument (Credit Note) separate from the stock-reversal instrument. Who may authorize a return/credit note — `Unknown`. |
| Period / reversal | **Applicable** | SDV-F06/F07 are this Deep Study's first real evidence for the Backbone Roadmap's Lane C scenario 3 (Return/Reversal); period/cut-off interaction (scenario 6) not yet evidenced — `Unknown`. |
| Tenant / Company / Data Scope | **Unknown** | No documentation evidence gathered this round on multi-company behavior of deliveries/returns/credit notes. |
| Audit / Event | **Unknown** | No documentation evidence on audit trail for delivery validation, return, or credit-note issuance. |
| Automation / Integration | **Applicable** | Sales Order → Delivery → (Backorder) → Invoice/COGS → (Return → Reverse Transfer + Credit Note) is a documented, systemic chain. |
| Cross-module effects | **Applicable** | SDV-F04/F05 directly depend on Gx1's Backbone Roadmap boundary rule (Inventory owns stock truth, Accounting owns financial truth) — SDV-F07 is direct documentary evidence of that boundary being implemented as two separate instruments. |
