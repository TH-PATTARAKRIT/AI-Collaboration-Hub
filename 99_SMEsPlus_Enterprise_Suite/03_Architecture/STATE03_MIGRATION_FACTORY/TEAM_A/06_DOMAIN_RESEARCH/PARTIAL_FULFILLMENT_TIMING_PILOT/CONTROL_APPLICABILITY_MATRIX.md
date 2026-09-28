> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX (Gx5)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | PDT-F01/F02: per-shipment invoicing/billing directly affects Financial Truth timing. |
| Inventory | **Applicable, indirectly** | Depends on GRV-F03/SDV-F03's Stock Truth events; this Gx doesn't add new Stock Truth evidence itself. |
| Authority (approval/execute/post/reverse) | **Unknown, and now a live open question** | `PDT-F03` directly raises whether "received quantities" is an enforced authority control or advisory — unresolved. |
| Period / reversal | **Unknown** | Not evidenced this round. |
| Tenant / Company / Data Scope | **Unknown** | Not evidenced. |
| Audit / Event | **Unknown** | Not evidenced. |
| Automation / Integration | **Applicable** | Bill Reference as a cross-document reconciliation mechanism is a documented integration point. |
| Cross-module effects | **Applicable** | This entire Gx is about the Sales/Purchase ↔ Accounting timing interface. |
