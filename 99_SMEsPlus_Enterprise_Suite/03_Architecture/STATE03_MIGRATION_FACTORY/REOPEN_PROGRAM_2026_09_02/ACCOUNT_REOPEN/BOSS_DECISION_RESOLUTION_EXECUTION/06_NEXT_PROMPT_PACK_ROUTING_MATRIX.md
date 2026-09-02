# 06 — NEXT PROMPT PACK ROUTING MATRIX

`None may be merged into another without a Boss decision` (governing prompt §3, mirrored from source `22` §1, carried by `12_NEXT_CONTROLLED_PROMPT_PACKS.md`). This file routes the 13 decision components to the ten existing packs (`PP-01`..`PP-10`) defined in `12_NEXT_CONTROLLED_PROMPT_PACKS.md`, and proposes two **candidate, unauthorized** pack skeletons for the two components no existing pack names. No pack below is authorized by this file — only Boss authorizes a pack.

## Routing to existing packs

| Existing Pack | Consumes (this package) | Decision components routed to it | Depends on |
|---|---|---|---|
| `PP-01` (Boss decision batch resolution) | This package's `02`, `05` | All 13 — this file's own package IS the `PP-01` deliverable named in `12_NEXT_CONTROLLED_PROMPT_PACKS.md` row 1 | — |
| `PP-02` (`COA-G01` unblock) | `09_COA_G01_UNBLOCK_ROUTING_PACK.md` (boss-decision package) | Not directly a decision component here, but gates `DC-09`'s design start | Boss / PMO / independent re-audit |
| `PP-03` (Legal-Tax review commissioning) | `06_LEGAL_TAX_REVIEW_BRIEF.md` | `DC-06A`, `DC-06B`, `DC-08B` (prerequisite); indirectly `DC-09` (DBD statement-format evidence) | Boss commissions a licensed Thai reviewer |
| `PP-04` (Joint Session 3) | `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` | `DC-05B` | Boss convenes; Inventory-side attendee confirmed |
| `PP-06` (AR/AP + Asset research, Team A) | `10` §A | `DC-01`, `DC-02` (if ruled IN) | Boss scope ruling on `DC-01`/`DC-02` |
| `PP-07` (Treasury / Cash & Bank) | `10` §B | `DC-04` | Owner named |
| `PP-08` (Financial Statement Taxonomy, `COA-G05`) | `10` §C | `DC-09` | `PP-02` + `PP-03` complete; owner named |

`PP-05`, `PP-09`, `PP-10` (TBRAC naming, `G-A3` lineage, branch-merge governance) are not directly routed to by any of the 13 decision components in this package — they remain open from the source boss-decision package but sit outside this package's `SC-01`..`SC-10` scope.

## Components with no existing pack — candidate skeletons (NOT authorized)

| Candidate Pack ID | Routes | Suggested session prompt ID | Would consume | Would produce | Owner to commission | Status |
|---|---|---|---|---|---|---|
| `PP-11` (candidate) | `DC-05A` | `SMEPLUS-26-09-0X-ACC-EMPLOYEE-EXPENSE-TAX-RETURNS-SCOPE-001` | This package's `02`/`05` `DC-05A` detail | Scope ruling record per sub-item (HR-expense, Tax Returns, Cash Roundings, WT Certificates) | Boss (rules directly) or a commissioned scoping session | Not authorized — routing candidate only |
| `PP-12` (candidate) | `DC-08A` | `SMEPLUS-26-09-0X-ACC-ANALYTIC-DIMENSION-OWNER-001` | `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §2, `UK-02`/`UK-04`/`UK-07`/`UK-08` | Named Accounting Core owner; dimension-model research scope | Team B (once named) | Not authorized — routing candidate only |

`DC-07` (approval-before-posting) and `DC-10` (COA template mechanics) route to no pack at all — both explicitly "carry forward" as direct Boss rulings once their prerequisite evidence (a `CO-02` tie-in for `DC-07`; Legal-Tax depreciation-rate findings for `DC-10`) is available, per `12_NEXT_CONTROLLED_PROMPT_PACKS.md`'s own pattern of not assigning every item a pack. `DC-03` (Budgets) similarly routes to no pack pending the evidence gap described in `05_BOSS_DECISION_FORM_SC01_SC10.md`.

## Full component-to-pack matrix

| Component | Immediate next pack | Prerequisite | Downstream pack (if applicable) |
|---|---|---|---|
| `DC-01` | `PP-06` | Boss ruling IN | — |
| `DC-02` | `PP-06` | Boss ruling IN, sequenced behind `DC-01` | — |
| `DC-03` | None | Evidence-strength decision (see `05`) | `PP-06`-adjacent, not currently in `10` §A's scope |
| `DC-04` | `PP-07` | Owner named | — |
| `DC-05A` | `PP-11` (candidate) | Boss ruling per sub-item | — |
| `DC-05B` | `PP-04` | Boss convenes | — |
| `DC-06A` | `PP-03` | Boss commissions | Ownership ruling returns to a `PP-01`-successor pack |
| `DC-06B` | `PP-03` | Boss commissions | Scope ruling returns to a `PP-01`-successor pack |
| `DC-07` | None | `CO-02` tie-in | Team B design at `CO-02` |
| `DC-08A` | `PP-12` (candidate) | Owner named | — |
| `DC-08B` | `PP-03` | Boss commissions | — |
| `DC-09` | `PP-08` | `PP-02` + `PP-03` complete, owner named | — |
| `DC-10` | None | Legal-Tax findings (recommended, not required) | — |

## Explicit non-claim

This matrix routes. It authorizes nothing — including the two candidate packs `PP-11`/`PP-12`, which exist here only to give Boss a ready skeleton if the corresponding component is ruled toward research. Only Boss selects and authorizes a pack, per `12_NEXT_CONTROLLED_PROMPT_PACKS.md`'s own "How to use this file" instruction, which this matrix follows rather than overrides.
