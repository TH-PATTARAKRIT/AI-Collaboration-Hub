> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx10)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-RCN-01 | Does "reconciliation" in this scenario mean the same thing as Odoo's documented "Bank Reconciliation"? | Risk of terminology conflation | **Contradicted — deliberately kept distinct** | Bank Reconciliation matches bank transactions to invoices/bills/payments; this scenario's subject is Stock-Fact-to-Financial-Fact identity, a different concept entirely (RCN-F04). |
| CQS-RCN-02 | Is there any documented direct link between a specific stock move and its resulting journal entry? | Assumed: no visible link exists ("black box" posting) | **Confirmed, at least for the backdating case** | Dual chatter on both picking and journal entry, synchronized who/when/why (RCN-F02) — direct, if backdating-specific, evidence of a real cross-reference. |
| CQS-RCN-03 | Does per-lot cost-origin tracking apply uniformly across costing methods, or is it FIFO-specific? | Assumed: uniform | **Unknown** | Documentation evidence found is FIFO-framed; AVCO behavior not evidenced this round. |

## Status

`CLOSED (documentation-tier)`: CQS-RCN-01, CQS-RCN-02.
`OPEN`: CQS-RCN-03.

This closes the Challenge Question Set activity for the full 10-scenario Lane C set (Gx1 through Gx10, Gx3 folded into Gx1).
