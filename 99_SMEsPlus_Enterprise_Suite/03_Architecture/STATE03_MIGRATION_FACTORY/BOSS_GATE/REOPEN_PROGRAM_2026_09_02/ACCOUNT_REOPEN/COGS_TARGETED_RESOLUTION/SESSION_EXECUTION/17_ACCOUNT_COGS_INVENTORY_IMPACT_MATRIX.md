# 17 — Account / COGS / Inventory Impact Matrix

Maps the three priority Joint Decisions and the two named `CGS-U` items to the downstream modules/gates they affect, per project-memory context (Account module Batch A gates, Inventory v2.0 HELD status) and this session's own files.

| Item | Account Module Impact | COGS/Inventory Impact | Downstream Gate Affected | Current Status |
|---|---|---|---|---|
| `JT-04` (recognition timing) | Determines when a COGS journal entry is eligible to post — directly shapes the Account module's posting-trigger design | Determines whether Inventory's delivery event or the Account module's invoice event is authoritative for cost release | Blocks Boss Account Ruling on COGS posting timing; blocks Inventory v2.0's COGS-gap dependency resolution (per project memory: Inventory v2.0 HELD, COGS gap dependency not fully resolved) | NOT DECIDABLE (file `08`) |
| `JT-05` (return cost basis) | Determines the Account module's credit-note-to-GL reversal logic | Determines whether Inventory needs per-unit original-cost lineage (a data-model requirement) | Blocks any return/credit-note posting design in the Account module; blocks Inventory v2.0 return-flow finalization | NOT DECIDABLE (file `09`) |
| `JT-01` (valuation policy owner) | Determines which Account-module record (Category-equivalent, Product-equivalent, or a new SMEsPlus concept) carries GL account defaults | Determines Inventory's category/product data model requirements for costing method and valuation account assignment | Blocks chart-of-accounts design; blocks Inventory v2.0 category-design finalization | NOT DECIDABLE (file `10`) |
| `CGS-U03` (Price Difference Account scope) | Determines whether a dedicated GL account is needed for Standard-Price adjustments only, or also for FIFO/AVCO | Determines Inventory's costing-method-to-account mapping completeness | Blocks `JT-02` closure | HOLD (file `12`) |
| `CGS-U34`/`CGS-U36` (landed cost residual) | Determines the Account module's landed-cost clearing/COGS posting design and its failure-mode control | Determines Inventory's landed-cost allocation completeness after full sale | Blocks `JT-08` closure; Audit VETO concern retained | HOLD (file `13`) |

## Cross-Reference to Project-Memory Status (Not Re-Derived, Cited for Context Only)

Per the orchestrating session's own project memory (not independently re-verified this session, since Account-module gate status was explicitly out of scope for a COGS-focused session per Fact Verification file `02` row 6): the Account module Batch A gates were recorded as "all open/blocked, zero resolved" as of 2026-09-02, and Inventory v2.0 is recorded as HELD with the COGS gap dependency "not fully resolved" even after the COGS Deep Research session executed. Nothing in this session's findings contradicts that recorded status — if anything, the NOT DECIDABLE dispositions on `JT-01`/`JT-04`/`JT-05` in this package are consistent with, and help explain, why that dependency remains unresolved.

## What This Matrix Does Not Do

It does not re-verify Account module gate status directly (no Account-module files were opened this session — this is a COGS-focused targeted-resolution session, consistent with its mandate). It does not claim Inventory v2.0 can now be finalized. It does not assign a numeric "impact score" — the governing rule against inventing percentages applies equally to inventing a spurious quantitative severity scale here.
