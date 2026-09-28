> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx10)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-RCN-01 | Whether the stock-move-to-journal-entry cross-link (RCN-F02) exists and is inspectable for *ordinary* (non-backdated) transactions, or is a backdating-specific enhancement | Materially affects how strong a "provenance" claim can be made for the general case, not just the backdating edge case | **Targeted Validation Needed — the single most important open question for this scenario** | Documentation pass specifically on ordinary journal-entry-to-stock-move references (developer/technical docs may be needed, as with `GAP-MCT-02`), or runtime evidence |
| GAP-RCN-02 | Whether per-lot cost-origin tracking (RCN-F03) applies under AVCO, not just FIFO | `CQS-RCN-03` | **Non-blocking** | Documentation or runtime pass |
| GAP-RCN-03 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN              : 3
TARGETED VALIDATION    : 1 (GAP-RCN-01)
NON-BLOCKING           : 2 (GAP-RCN-02, 03)
```

This closes the Gap Register activity for the full 10-scenario Lane C set.
