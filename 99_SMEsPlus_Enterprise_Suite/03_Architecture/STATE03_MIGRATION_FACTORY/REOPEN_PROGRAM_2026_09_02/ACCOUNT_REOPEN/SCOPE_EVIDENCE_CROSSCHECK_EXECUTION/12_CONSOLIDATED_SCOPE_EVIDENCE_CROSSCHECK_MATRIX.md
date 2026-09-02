# 12 — CONSOLIDATED SCOPE EVIDENCE CROSS-CHECK MATRIX (`SC-01`..`SC-10`)

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` This matrix consolidates files `02`–`11`. It resolves nothing and rules on nothing.

| SC | Decision ID | Topic | Evidence pointer result | Owner status | Gate impact | Readiness classification |
|---|---|---|---|---|---|---|
| `SC-01` | `ACC-DEC-004` | Fixed assets, depreciation, disposal | Verified | Boss | No gate defined | `READY AFTER BOSS SCOPE DECISION` |
| `SC-02` | `ACC-DEC-005` | Deferred revenues/expenses, recognition schedules | Verified | Boss | No gate defined | `READY AFTER BOSS SCOPE DECISION` |
| `SC-03` | `ACC-DEC-006` | Budgets / budgetary positions / budget analysis | Verified | Boss | No gate defined | `READY AFTER BOSS SCOPE DECISION` |
| `SC-04` | `ACC-DEC-007` | Treasury / Cash & Bank | Partial | Unassigned (Treasury) | No gate defined | `READY AFTER OWNER ASSIGNED` |
| `SC-05` | `ACC-DEC-008` | Employee expenses / Tax Returns / Cash Roundings / WT Certificates / manufacturing valuation / price difference / write-down | Verified | Boss (4 sub-items); Joint/Unassigned (3 sub-items) | No gate defined / Joint | `READY AFTER BOSS SCOPE DECISION` + `READY AFTER JOINT_SESSION` (split) |
| `SC-06` | `ACC-DEC-009` | VAT and CIT ownership; `PND1`/`PND54`/`PP36` scope | Partial | Boss / Legal-Tax | `COA-G06` | `READY AFTER BOSS SCOPE DECISION` (sequenced behind `ACC-DEC-014`) |
| `SC-07` | `ACC-DEC-010` | Approval-before-posting workflow (`ACC-004` draft) | Verified | Boss | `CO-02` | `READY AFTER BOSS SCOPE DECISION` |
| `SC-08` | `ACC-DEC-011` | Analytic/dimension model ownership; branch (สาขา) statutory status | Verified | Boss / Legal-Tax (dual) | `COA-G07` | `READY AFTER OWNER ASSIGNED` + `READY AFTER LEGAL_TAX_REVIEW` (split) |
| `SC-09` | `ACC-DEC-012` | Financial Reporting design owner | Verified | Unassigned (Team B, sequenced) | `COA-G05` | `READY AFTER OWNER ASSIGNED` (sequenced behind `COA-G01` + `ACC-DEC-014`) |
| `SC-10` | `ACC-DEC-013` | Standard COA template mechanics (`B13 DT-03`) | Verified | Boss | `COA-G04S` | `READY AFTER BOSS SCOPE DECISION` |

## Result tally

- **Evidence pointer result:** 8 of 10 rows `Verified`; 2 of 10 (`SC-04`, `SC-06`) `Partial` — in both cases because one specific sub-citation's anchor was confirmed to exist but its full body was not read in this session's targeted fetch, not because any pointer was found false or unlocatable.
- **Rows classified `MISSING SOURCE POINTER`:** none. Every cited anchor code checked (10 of 10 rows) resolved to a real file with topically on-point content.
- **Rows classified `HOLD / EVIDENCE REQUIRED`:** none at the row level — all 10 rows had locatable, checkable evidence; the underlying *subject matter* of several rows (e.g. `SC-01`, `SC-02`, `SC-03`) is itself `HOLD / EVIDENCE REQUIRED` in the source material, which this cross-check correctly reports rather than resolves.
- **Rows requiring Boss decision:** all 10 (every row's Next Action routes to Boss, whether directly or via an owner-assignment/legal-tax step Boss must first authorize).
- **Rows requiring Legal-Tax review before closure:** `SC-06`, `SC-08` (and, on the statutory-format side, `SC-09` indirectly via `06_LEGAL_TAX_REVIEW_BRIEF.md` §D).
- **Rows requiring Joint Session 3 before closure (in whole or part):** `SC-05` only, and only for its manufacturing/price-difference/write-down sub-items.
- **Rows with an owner-assignment gap (no named owner anywhere in the chain):** `SC-04` (Treasury), `SC-09` (Financial Reporting), and the ownership half of `SC-08` (Analytic/dimension).

## Cross-package consistency finding

Every one of the 10 rows was checked against **two independent required registers** — the Batch A `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` and the source-pack `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`. No discrepancy in Decision ID, topic, gate impact, or evidence citation was found between the two across any of the 10 rows. The Batch A register is a faithful, unexpanded carry-forward of the source-pack register plus a stable Decision ID and Batch A's own uniform status layer, exactly as both files' own "Rule" fields claim.

## Structural finding (applies to all 10 rows)

Nearly every row's deepest evidence citation is a bare file number ("`12`", "`14`", "`17`", "`A1`", etc.) that resolves not inside either of this session's two required input packages, but one layer further back, on branch `audit/account-menu-process-deep-study-2026-09-02-001` at commit `5183e9f6ef4272e68c65d831580886e341118d53` — a package this session's governing prompt did **not** name as a required input. This session located that branch/commit (it is cited internally by the required packages themselves) and fetched the specific files needed to check each anchor, without re-auditing that package's conclusions wholesale. See `01_SOURCE_PACKAGE_VERIFICATION_REGISTER.md` §B for the disclosure and files `02`–`11` for the per-row detail. This is reported as a structural observation for Boss, not a defect: the citation chain is real and traceable, but a future prompt that wants this session's SC evidence pointers *fully* self-contained within its own required inputs should explicitly add that branch/commit to its required-source list.

## Explicit non-claim

No item above is ruled IN, OUT, DEFERRED, APPROVED, REJECTED, or MODIFIED by this cross-check. No owner is assigned by this cross-check. No gate is opened, closed, or moved. This matrix only reports whether existing evidence pointers resolve to real, topically-supporting content — it is a routing and verification record, not a decision.
