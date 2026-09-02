# 05 — ACCOUNT SCOPE RESEARCH REGISTER (`ACC-DEC-004`–`ACC-DEC-013`, `SC-01`..`SC-10`)

| Field | Value |
|---|---|
| Decision IDs | `ACC-DEC-004` through `ACC-DEC-013` |
| Batch A Approved Direction | Include all 10 scope questions as research-required items |
| Batch A Control Status | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` (applies uniformly to all 10) |
| Boss Approval Record | branch `boss/account-batch-a-research-routing-approval-2026-09-02`, commit `fa75eb0ebfd8c3eee41b0e78c7afb39cbac7e751`, §2 row 5 |
| Source Routing Pack | `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`, branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`, commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| Rule (unchanged) | This session cannot add scope. Each row only routes an existing scope question already surfaced in the source package to Boss; none is resolved, expanded, or narrowed. |

Boss's Batch A uniform status (`RESEARCH REQUIRED / BOSS FINAL DECISION PENDING`) is applied to every row below as the governing control status. The source pack's finer-grained per-item status (`BOSS DECISION REQUIRED` vs. `GAP OWNER ROUTING REQUIRED`) is preserved alongside it because it determines *what kind* of research/routing is needed per item.

## Execution table

| Decision ID | SC ID | Item | Owner | Evidence Location | Batch A Status | Source-Pack Status | Gate Impact | Next Action |
|---|---|---|---|---|---|---|---|---|
| `ACC-DEC-004` | SC-01 | Fixed assets, depreciation, disposal | Boss | source `05` row `ACC-DEC-004`; source `12` UK-02 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | No gate defined | If IN, feed into `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §Fixed Asset research pass |
| `ACC-DEC-005` | SC-02 | Deferred revenues/expenses and recognition schedules | Boss | source `05` row `ACC-DEC-005`; source `12` UK-04 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | No gate defined | Same routing as `ACC-DEC-004` |
| `ACC-DEC-006` | SC-03 | Budgets / budgetary positions / budget analysis | Boss | source `05` row `ACC-DEC-006`; source `13` UK-03 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | No gate defined | If IN, assign a Team A/B research owner (currently none) |
| `ACC-DEC-007` | SC-04 | Treasury / Cash & Bank (bank journals, statements, reconciliation, cheques, PromptPay, bank feeds) | Boss (assign owner) | source `05` row `ACC-DEC-007`; source `02` M-BNK-*; source `18` ST-03 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `GAP OWNER ROUTING REQUIRED` | No gate defined | Assign named Treasury owner (currently UNASSIGNED); see `10` §Treasury/Cash & Bank |
| `ACC-DEC-008` | SC-05 | Employee expenses (HR→Accounting), Tax Returns closing menu, Cash Roundings, WT Certificates menu, manufacturing valuation, price difference, inventory write-down (`113900`) | Boss | source `05` row `ACC-DEC-008`; source `A1` §C.4; source `08` objections 5–6; source `04` HO-31 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED / JOINT (split)` | No gate defined / Joint | Manufacturing valuation, price difference, and write-down route to Joint Session 3 (`04_ACCOUNT_INVENTORY_JOINT_SESSION_3_EXECUTION_RECORD.md`); HR-expense, Tax Returns, Cash Roundings, WT Certificates route to Boss scope ruling |
| `ACC-DEC-009` | SC-06 | VAT and CIT ownership (Accounting Core vs. separate Tax domain); scope status of `PND1`/`PND54`/`PP36` | Boss | source `05` row `ACC-DEC-009`; source `10` objections 7, 9; prior `VC-06` | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | `COA-G06` | Feeds `02_LEGAL_TAX_REVIEW_ROUTING_EXECUTION_RECORD.md`, which covers all forms regardless of eventual ownership split |
| `ACC-DEC-010` | SC-07 | Approval-before-posting workflow (`ACC-004` draft) — IN or OUT | Boss | source `05` row `ACC-DEC-010`; source `14` OBJN-07 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | `CO-02` | If IN, Team B designs at `CO-02` once unblocked |
| `ACC-DEC-011` | SC-08 | Analytic/dimension model ownership; branch (สาขา) as dimension vs. statutory attribute | Boss / Legal-Tax | source `05` row `ACC-DEC-011`; source `13` objections 2, 4 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `GAP OWNER ROUTING REQUIRED` + `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G07` | Assign owner; branch statutory-status question routed via `02` §D item `DBD-6` |
| `ACC-DEC-012` | SC-09 | Financial Reporting design owner (statement production, OUT neighbour, not designed) | Boss | source `05` row `ACC-DEC-012`; source `09` RU-08 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `GAP OWNER ROUTING REQUIRED` | `COA-G05` | Assign named Team B owner; see `10` §Financial Statement Taxonomy |
| `ACC-DEC-013` | SC-10 | Standard COA template mechanics (`B13 DT-03`) — still unapproved | Boss | source `05` row `ACC-DEC-013`; source `17` VC-05 | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` | `BOSS DECISION REQUIRED` | `COA-G04S` | Boss rules APPROVE / REJECT / MODIFY; carries forward from a prior round |

## Coverage check

10 of 10 rows populated (`ACC-DEC-004`–`ACC-DEC-013`, `SC-01`..`SC-10`). 0 resolved by this session. Every row remains `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING`.

## Explicit non-claim

No scope item above is ruled IN, OUT, DEFERRED, APPROVED, REJECTED, or MODIFIED by this record. No owner is assigned. This register only carries the Batch A research status forward into a per-item execution table with evidence pointers.
