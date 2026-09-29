> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| BRP-F01 BoM Type selection | **C1** | V5/floor V4 | V2 | Targeted Validation Needed (`GAP-BRP-01`, non-blocking) |
| BRP-F02 Kit BOM | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-02`, non-blocking) |
| BRP-F03 Subcontracting BOM | **C1** | V5/floor V4 | V2 | Resolved, documentation-tier (`GAP-BRP-03` closed 2026-09-29 — fee captured via vendor bill at posting time) |
| BRP-F04 Work Center configuration | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-04`, non-blocking) |
| BRP-F05 Routing Operations | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-05`, non-blocking) |
| BRP-F06 Reordering Rules | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-07`, non-blocking) |
| BRP-F07 Master Production Schedule | C3 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-08`, non-blocking) |
| BRP-F08 By-Products | **C1** | V5/floor V4 | V2 | **Targeted Validation Needed (`GAP-BRP-09`) — cost-allocation method open** |
| BRP-F09 Multi-level BOM | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-10`, non-blocking) |

## Next action

(1) ~~`GAP-BRP-03` (subcontracting cost capture)~~ **done 2026-09-29** — vendor bill posting debits the Finished Goods Valuation Account, capturing the fee; (2) fold all 9 `BRP` functions into the shared cross-Gx AWT capstone session alongside Gx7's `MFG-F01`/`F02` (all Manufacturing-app functions, one environment); (3) `GAP-BRP-09` (by-product cost allocation) is now this pilot's highest-value remaining question — official-doc pass or AWT; (4) ~~consider a follow-on pass for Master Production Schedule/reordering rules, byproducts, and multi-level BOM explosion~~ **done 2026-09-29** — `BRP-F06`–`F09` added this round.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`, same standard as every Lane C pilot. Ready for `CHATGPT_AUDIT`; not ready for `BOSS_GATE` pending `STATE03_BOSS_GATE_QUEUE.md` items.
