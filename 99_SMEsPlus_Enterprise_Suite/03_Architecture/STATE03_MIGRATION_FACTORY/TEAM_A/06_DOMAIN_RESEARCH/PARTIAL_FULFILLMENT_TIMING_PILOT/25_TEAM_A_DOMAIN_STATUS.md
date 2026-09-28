> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS (Gx5)

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| PDT-F01 Per-shipment invoicing alignment | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable) |
| PDT-F02 Per-receipt billing alignment | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable) |
| PDT-F03 Bill-before-receipt anomaly | **C1** | V5/floor V4 | **V1** (community-tier evidence only, below the documentation-tier V2 this Deep Study otherwise treats as its floor) | **Blocking Unknown + Evidence Conflict — lowest-confidence finding in the Deep Study so far, explicitly flagged rather than rounded up** |
| PDT-F04 Cross-shipment reconciliation | C2 | V4/floor V3 | V2 | Targeted Validation Needed |

## Next action

(1) `PDT-F03`/`GAP-PDT-01` should be the **first** thing checked once AWT is available — it is cheap to test (attempt bill creation before receipt under "received quantities" policy) and would either confirm a real control gap or lay the forum report to rest; (2) `GAP-PDT-03` (does invoice-timing determine COGS-timing) is the single most likely documentation-tier lead to actually resolve the larger cross-Gx valuation-timing conflict — worth a dedicated follow-up search before assuming only AWT can resolve it; (3) continue to Gx6 (Period/Cut-off) per Boss's continuous order.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`. Ready for CHATGPT_AUDIT; not ready for BOSS_GATE pending `STATE03_BOSS_GATE_QUEUE.md`.
