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
| BRP-F08 By-Products | **C1** | V5/floor V4 | V2 (function); `GAP-BRP-09` itself V1 | **Open/Conditional (`GAP-BRP-09`) — candidate default disclosed 2026-09-29 (third-party listing + pre-19 forum), not officially confirmed for Odoo 19.0, not upgraded to V2** |
| BRP-F09 Multi-level BOM | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-BRP-10`, non-blocking) |

## Next action

(1) ~~`GAP-BRP-03` (subcontracting cost capture)~~ **done 2026-09-29** — vendor bill posting debits the Finished Goods Valuation Account, capturing the fee; (2) fold all 9 `BRP` functions into the shared cross-Gx AWT capstone session alongside Gx7's `MFG-F01`/`F02` (all Manufacturing-app functions, one environment); (3) `GAP-BRP-09` (by-product cost allocation) is now this pilot's highest-value remaining question — official-doc pass or AWT; (4) ~~consider a follow-on pass for Master Production Schedule/reordering rules, byproducts, and multi-level BOM explosion~~ **done 2026-09-29** — `BRP-F06`–`F09` added this round.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`, same standard as every Lane C pilot. Ready for `CHATGPT_AUDIT`; not ready for `BOSS_GATE` pending `STATE03_BOSS_GATE_QUEUE.md` items.

## M1 SLICE CHECKPOINT — CLOSED (2026-09-29, per Boss's "STATE03 M1 Close Then Core Module Priority" instruction)

This is a checkpoint, **not a claim that Manufacturing is complete**. All 9 currently-selected `BRP` functions are documented at their evidence tier; `GAP-BRP-09` (By-Products cost allocation, C1) and `GAP-MFG-01` (Gx7's `MFG-F05`, negative-inventory revaluation, C1) both **remain Open/Conditional** — neither is resolved by reaching this checkpoint. Per Boss's explicit instruction, **no further Manufacturing/BOM/Routing scope is added** beyond this slice (including the `QUALITY_CONTROL_PILOT` follow-on module, now paused — see that pilot's own status note) unless a material gap in the *existing* slice requires a bounded follow-up. Research priority moves to the product-core module order in `STATE03_M1_CLOSE_THEN_CORE_MODULE_PRIORITY_PROMPT` §2: Shared Master Data → Sales → Purchase → Inventory → Accounting → O2C/P2P → Manufacturing (optional/conditional, last).
