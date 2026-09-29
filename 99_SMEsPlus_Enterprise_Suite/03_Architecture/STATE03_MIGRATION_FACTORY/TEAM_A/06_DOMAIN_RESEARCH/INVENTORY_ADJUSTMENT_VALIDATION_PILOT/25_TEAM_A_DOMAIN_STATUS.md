> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS (Gx4)

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| IAV-F01 Physical count recording | C2 | V4/floor V3 | V2 | Targeted Validation Needed |
| IAV-F02 Applying the adjustment | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-IAV-05`) |
| IAV-F03 Financial posting timing | **C1** | V5/floor V4 | V2 | **Blocking Unknown + Evidence Conflict (`GAP-IAV-01`)** |
| IAV-F04 Scrap / Loss Account | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable) |
| IAV-F05 Cycle count scheduling | C3 | V4/floor V3 | V2 | Targeted Validation Needed |
| IAV-F06 Reversal of adjustment | C2 | V4/floor V3 | **V2** (was V0) | Resolved, documentation-tier (`GAP-IAV-02` closed 2026-09-29) |

## Next action

(1) `GAP-IAV-01` joins the shared cross-Gx AWT priority (Gx1 `GRV-F04`, Gx2 `SDV-F05`, this Gx `IAV-F03`) — one combined AWT session should test all three; (2) ~~close `GAP-IAV-02` (adjustment reversal) with a targeted documentation pass~~ **done 2026-09-29** — Odoo 19 docs confirm a native "Revert Inventory Adjustment" action; (3) continue to Gx5 (Partial Receipt/Delivery timing consistency) per Boss's continuous order — note Gx5 substantially overlaps with what Gx1 `GRV-F03` and Gx2 `SDV-F03` already covered; Gx5 should focus specifically on the timing-consistency angle (quantity vs. financial-timing alignment across a partial fulfillment) rather than re-researching backorder mechanics from scratch.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`, same as Gx1/Gx2. Ready for CHATGPT_AUDIT; not ready for BOSS_GATE pending `STATE03_BOSS_GATE_QUEUE.md` items.
