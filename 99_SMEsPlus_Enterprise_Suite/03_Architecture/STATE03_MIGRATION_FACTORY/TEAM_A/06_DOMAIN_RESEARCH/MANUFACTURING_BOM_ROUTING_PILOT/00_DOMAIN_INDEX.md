> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Team A (Maker) | Documentation-Only | Boss sole Final Approver

# 00 — DOMAIN INDEX

**Not a Lane C "Gx" unit.** This is the first module of the Next-Prompt autonomous expansion (Boss order, 2026-09-29, "STATE03 Next Prompt — Autonomous Research Continuation and Module Expansion"), selected per `STATE03_NEXT_PROMPT_FIRST_CHECKPOINT.md` §4 as the next READY module. Scope: BOM structure/type, Kit, Subcontracting, and Work Center/Routing — the Manufacturing/MRP surface Lane C's `MANUFACTURING_VALUATION_PILOT` (Gx7) did not cover (Gx7 was scoped narrowly to consumption/WIP/completion/cost valuation timing, 5 functions).

**Naming discipline** (per the checkpoint's §3 finding): this pilot is deliberately *not* numbered as a "Gx" and does not use "Cross-Proof" language, to avoid the same naming-collision risk flagged there. It is Wave 5 (Manufacturing/MRP, BOM/Production Master) of `STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.md`, Team A/documentation-tier only.

## Relationship to Gx7 (`MANUFACTURING_VALUATION_PILOT`)

Complementary, not overlapping. Gx7 already established: components consume automatically to WIP, finished goods complete automatically from WIP, MO cost is BOM-component-cost + operations cost, and (this session) a disclosed version tension on negative-inventory revaluation (`MFG-F05`). This pilot studies the *structural* layer those postings ride on top of — what a BOM actually is, its three types, and how routing/work centers feed the cost figure `MFG-F04` treats as an input.

Same taxonomy as Lane C pilots (01, BASELINE_CARRY_FORWARD, 04, 06, 11, CONTROL_APPLICABILITY_MATRIX, 19, 22, CHALLENGE_QUESTION_SET_LOG, 25, AWT_BACKLOG).
