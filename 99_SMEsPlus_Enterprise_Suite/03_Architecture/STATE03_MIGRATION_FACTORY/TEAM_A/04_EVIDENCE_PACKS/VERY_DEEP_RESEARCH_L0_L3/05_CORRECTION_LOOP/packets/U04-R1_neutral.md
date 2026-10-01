# Correction packet U04-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** How the cost used for order-line margin is chosen when the stock-margin capability is installed.
- **BUSINESS RULE:** Lines without stock movements, and lines added from a delivery with no ordered quantity, use the standard cost computation. Lines with delivered stock and a non-standard costing method use a blend of delivered cost and standard cost. [N-U04R1-001] [N-U04R1-002]
- **CONSTRAINT:** Lines with delivered stock, an ordered quantity and a standard costing method are not recomputed and keep their stored cost. [N-U04R1-003]
- **RISK:** Margin figures for standard-cost products may not follow later cost changes after delivery. [N-U04R1-003]
- **UNKNOWN:** Whether this matters in practice depends on when the stored cost is set, which requires runtime confirmation.
