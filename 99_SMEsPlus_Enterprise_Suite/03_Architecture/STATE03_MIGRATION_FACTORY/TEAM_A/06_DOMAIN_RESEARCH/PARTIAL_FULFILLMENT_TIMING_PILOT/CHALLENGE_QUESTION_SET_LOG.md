> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx5)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-PDT-01 | Does invoicing wait for full order completion, or trigger per partial shipment? | "Invoicing is batched to completion" | **Contradicted** | Documentation: two invoices for a fully-backordered order, one per delivery (EV-PDT-01). |
| CQS-PDT-02 | Is "received quantities" Bill Control Policy an enforced hard gate? | Extends Gx1's `CQS-GRV-04` | **Further weakened, not yet confirmed/denied** | A community report (EV-PDT-04, lower tier) describes bill creation preceding receipt under this exact policy — consistent with, not proof of, the "soft control" hypothesis. |
| CQS-PDT-03 | Does the system enforce that total billed quantity across multiple partial bills never exceeds the PO total? | Assumed: yes, automatically | **Unknown** | No documentation found either confirming or denying an automatic cross-bill total check. |

## Status

`CLOSED (documentation-tier)`: CQS-PDT-01.
`OPEN (Evidence Conflict extension, cross-Gx)`: CQS-PDT-02 — feeds the same lineage as `GAP-GRV-06`/`CQS-GRV-04`.
`OPEN (Targeted Validation Needed)`: CQS-PDT-03.
