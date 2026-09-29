> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| BRP-F01 BoM Type selection | **C1** | V5/floor V4 | V2 | Targeted Validation Needed (`GAP-BRP-01`, non-blocking) |
| BRP-F02 Kit BOM | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-02`, non-blocking) |
| BRP-F03 Subcontracting BOM | **C1** | V5/floor V4 | V2 | Resolved, documentation-tier (`GAP-BRP-03` closed 2026-09-29 — fee captured via vendor bill at posting time) |
| BRP-F04 Work Center configuration | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-04`, non-blocking) |
| BRP-F05 Routing Operations | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-05`, non-blocking) |

## Next action

(1) ~~`GAP-BRP-03` (subcontracting cost capture)~~ **done 2026-09-29** — vendor bill posting debits the Finished Goods Valuation Account, capturing the fee; (2) fold `BRP-F01`/`F03`/`F04`/`F05` into the shared cross-Gx AWT capstone session alongside Gx7's `MFG-F01`/`F02` (all Manufacturing-app functions, one environment); (3) consider a follow-on pass for Master Production Schedule/reordering rules, byproducts, and multi-level BOM explosion — explicitly out of scope this round, not silently declared complete.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`, same standard as every Lane C pilot. Ready for `CHATGPT_AUDIT`; not ready for `BOSS_GATE` pending `STATE03_BOSS_GATE_QUEUE.md` items.
