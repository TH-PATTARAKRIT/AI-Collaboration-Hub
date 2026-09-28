> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx6)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-PCO-01 | No documented correction mechanism for a post-Hard-Lock error | Cannot state how a design should handle this case | **Targeted Validation Needed** | Documentation search on "correcting entries after lock date," or runtime evidence |
| GAP-PCO-02 | Whether Stock Closing is a required manual action or can be scheduled/automated | Affects operational-design assumptions about period-close reliability | **Non-blocking** | Documentation or runtime pass |
| GAP-PCO-03 | Whether a bill created before receipt (Gx5 `GAP-PDT-01`, if confirmed as a real gap) interacts with the accrual mechanism or bypasses it entirely | Compound question across two open findings | **Non-blocking, flagged as a good combined AWT target** | AWT, combined with the Gx5 `PDT-F03` test |
| GAP-PCO-04 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Cross-Gx resolution action taken

The valuation-timing question previously logged as an Evidence Conflict in `GRV-F04` (Gx1), `GAP-SDV-01` (Gx2), and `GAP-IAV-01` (Gx4) is **downgraded from "Evidence Conflict" to "Resolved — documentation-tier, high confidence, AWT still recommended for final confirmation"** in each of those files via addendum (originals not deleted). See each file's own update note.

## Status summary

```
GAPS OPEN                 : 4
TARGETED VALIDATION       : 1 (GAP-PCO-01)
NON-BLOCKING              : 3 (GAP-PCO-02, 03, 04)
CROSS-Gx ITEMS RESOLVED THIS ROUND : 3 (GRV-F04 conflict, GAP-SDV-01, GAP-IAV-01)
```
