# Correction packet C01-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** When goods are set aside for a confirmed order, and which period locks restrict stock documents.
- **BUSINESS RULE:** When a delivery is confirmed, available stock is reserved immediately if the operation type is configured to reserve at confirmation; other options reserve manually or shortly before the scheduled date. [N-C01R1-001]
- **OPTIONALITY:** Reservation timing is configured per operation type; in the studied configuration all types reserve at confirmation. [N-C01R1-001] [N-C01R1-002]
- **CONSTRAINT:** A transfer's completion date cannot fall in a period closed by the fiscal-year or hard lock; the sales, purchase and tax locks do not apply to transfers. [N-C01R1-003]
- **RISK:** Stock cut-off control relies on the fiscal-year and hard locks only. [N-C01R1-003]
- **UNKNOWN:** Reservation behaviour with insufficient stock and the order in which the confirmation extensions run need runtime confirmation.
