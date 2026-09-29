> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| BRP-F01 BoM Type selection | **C1** | V5/floor V4 | V2; source/dump finding received (not upgraded) | `GAP-BRP-01` — `SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` — not resolved |
| BRP-F02 Kit BOM | C2 | V4/floor V3 | V2; source/dump finding received (not upgraded) | `GAP-BRP-02` — same label, 2026-09-30 — not resolved |
| BRP-F03 Subcontracting BOM | **C1** | V5/floor V4 | V2 | Resolved, documentation-tier (`GAP-BRP-03` closed 2026-09-29 — fee captured via vendor bill at posting time) — unaffected by this round |
| BRP-F04 Work Center configuration | C2 | V4/floor V3 | V2; source/dump finding received (not upgraded) | `GAP-BRP-04` — same label, 2026-09-30, shared with Gx7 `GAP-MFG-04` — not resolved |
| BRP-F05 Routing Operations | C2 | V4/floor V3 | V2; source/dump finding received (not upgraded) | `GAP-BRP-05` — same label, 2026-09-30 — not resolved |
| BRP-F06 Reordering Rules | C2 | V4/floor V3 | V2; source/dump finding received (not upgraded) | `GAP-BRP-07` — same label, 2026-09-30, conditional on `purchase_request` (OCA) — not resolved |
| BRP-F07 Master Production Schedule | C3 | V4/floor V3 | V2; scope boundary disclosed (not upgraded) | `GAP-BRP-08` — **not a Community answer**: no MPS module in Community source, but confirmed genuinely installed in the actual test database — needs the real installed module's own source before further review |
| BRP-F08 By-Products | **C1** | V5/floor V4 | V2 (function); `GAP-BRP-09` itself V1 documentation-tier, source/dump finding received (not upgraded) | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30, Handoff `D-01`), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`** — Cost Share (%) mechanism found, materially refining (and partially contradicting) the 2026-09-29 candidate default; **not resolved, not closed** |
| BRP-F09 Multi-level BOM | C2 | V4/floor V3 | V2; source/dump finding received (not upgraded) | `GAP-BRP-10` — same label, 2026-09-30 — not resolved |

## Source-code verification round (2026-09-30, per Boss's "STATE03 Odoo Clean-Room Source & Dump Deep Study" prompt)

Boss's local Claude Code session (Source/Dump Deep Research Worker) delivered findings for all 8 open `BRP` gaps (`GAP-BRP-01,02,04,05,07,08,09,10`) via the consolidated `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` (`D-01`, `D-08`–`D-13`), superseding two earlier per-pilot files (`SRC_GAP-BRP-09_*`, `SRC_GAPS_BRP-01-02-04-05-07-08-10_*`) whose own proposed "Resolved (source-code tier)" wording is void per the Handoff's §6 relabel notice. This session (STATE03 Integration/Architecture Knowledge Owner) never read the source or dump directly; it reconciled the wording into `06_BUSINESS_RULE_REGISTER.md`, `22_UNKNOWN_AND_GAPS.md`, `19_PROVENANCE_REGISTER.md`, and `AWT_BACKLOG.md` using the mandated label. **No gap in this pilot is declared closed** beyond the already-existing `GAP-BRP-03` (documentation-tier, unaffected). The most material finding: `GAP-BRP-09`'s prior "no cost allocated to by-products" candidate default is now understood as the unwarned consequence of an unset (0%) Cost Share field, not a hard system rule — this is a refinement and partial contradiction, not a closure.

## Next action

(1) ~~`GAP-BRP-03` (subcontracting cost capture)~~ **done 2026-09-29** — vendor bill posting debits the Finished Goods Valuation Account, capturing the fee; (2) fold all 9 `BRP` functions into the shared cross-Gx AWT capstone session alongside Gx7's `MFG-F01`/`F02` (all Manufacturing-app functions, one environment); (3) `GAP-BRP-09` (by-product cost allocation) still this pilot's highest-value remaining question — now AWT-targeted at the Cost Share = 0 / Standard-FIFO-mixed edge cases specifically, per the 2026-09-30 source finding; (4) `GAP-BRP-08` (MPS) needs its actual installed module's source identified and license-checked before further review — it is not answerable from Community source alone.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`, same standard as every Lane C pilot. Ready for `CHATGPT_AUDIT`; not ready for `BOSS_GATE` pending `STATE03_BOSS_GATE_QUEUE.md` items.

## M1 SLICE CHECKPOINT — CLOSED (2026-09-29, per Boss's "STATE03 M1 Close Then Core Module Priority" instruction)

This is a checkpoint, **not a claim that Manufacturing is complete**. All 9 currently-selected `BRP` functions are documented at their evidence tier; `GAP-BRP-09` (By-Products cost allocation, C1) and `GAP-MFG-01` (Gx7's `MFG-F05`, negative-inventory revaluation, C1) both **remain Open/Conditional** — neither is resolved by reaching this checkpoint, and the 2026-09-30 source/dump round (see above) does not change this. Per Boss's explicit instruction, **no further Manufacturing/BOM/Routing scope is added** beyond this slice (including the `QUALITY_CONTROL_PILOT` follow-on module, now paused — see that pilot's own status note) unless a material gap in the *existing* slice requires a bounded follow-up. Research priority moves to the product-core module order in `STATE03_M1_CLOSE_THEN_CORE_MODULE_PRIORITY_PROMPT` §2: Shared Master Data → Sales → Purchase → Inventory → Accounting → O2C/P2P → Manufacturing (optional/conditional, last).
