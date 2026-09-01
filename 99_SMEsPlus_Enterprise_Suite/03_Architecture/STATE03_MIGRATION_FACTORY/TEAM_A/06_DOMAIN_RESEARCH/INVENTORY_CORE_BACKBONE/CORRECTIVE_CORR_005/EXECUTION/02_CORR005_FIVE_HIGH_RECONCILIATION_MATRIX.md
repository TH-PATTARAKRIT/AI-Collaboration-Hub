# 02 — Five High Reconciliation Matrix

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile all five High findings from IER-003 into TEAM A's own controlled registers | Claude (Team A, CORR-005) | This artifact; DR-002 A5/A7/A9/A10/A12/A13/A14/A15/A16/A17/A18 | 2026-09-01 | Independent Delta Re-Review (required next) | See table below | Directly gates whether any open Inventory research blocker remains at High severity |

This is the canonical, single-page reconciliation matrix for all five originally-open DR-002 High items. It restates — does not re-derive — the disposition already recorded in `DEEP_RESEARCH_DR002/EXECUTION/A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` §Part 3, gathered here for reviewer convenience.

## Reconciliation table

| ID | Original DR-002 status (2026-08-31) | IER-003 independent verdict | Boss disposition | CORR-005 reconciled classification | Primary evidence citation |
|---|---|---|---|---|---|
| **GRPA-H4** — `account.fiscal.position` base model unlocated | `EVIDENCE_MISSING` | `VERIFIED CLOSED` | N/A (no scope ruling required — a straightforward evidence miss) | **`VERIFIED CLOSED`** — RESOLVED | `01 ACCOUNT/account/models/partner.py:27` (`_name = 'account.fiscal.position'`); IER-003 [04](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/04_IER003_HIGH_H1_FISCAL_POSITION_BOUNDARY_REVIEW.md) |
| **GRPA-H5** (= H2) — orphaned `res.partner` brand/HQ columns | `EVIDENCE_MISSING` | `PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED` (owning module identified: `bh_parent_company`, author BHPRO; source still absent from the authorized machine) | **`CLOSED BY BOSS SCOPE EXCLUSION / LEGACY MIGRATION DATA CARRY-FORWARD ONLY`** — `bh_*`/`bhpro_*` are excluded from SMEsPlus source learning entirely | **`CLOSED BY BOSS SCOPE EXCLUSION`** — `CONTROLLED MIGRATION CARRY-FORWARD` | `ir_model_data`/`ir_module_module` provenance query; IER-003 [05](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md); Boss Inventory Scope Ruling §1.1 |
| **GRPA-H8** (= H3) — two uncoordinated Thai "branch" concepts | `CONFLICTING PRACTICE` | `CONFLICTING EVIDENCE` + `REQUIRES REAL USER VALIDATION` — structural conflict confirmed; TEAM A's "branch = child `res.company`" characterization corrected to "structurally available, not confirmed as this customer's practice" (single-company dataset) | **`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`** — approved SaaS Tenant/Company/Branch platform baseline is not reopened by Inventory | **`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`** — `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` + `ACCOUNTING/TAX CARRY-FORWARD` | `l10n_th`/`l10n_th_partner` full-file read; `res_company` cardinality check (1 row, unbranched); IER-003 [06](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md); Boss Inventory Scope Ruling §1.2 |
| **N-A7-03 / N-A9-02** (= H4) — cutoff/timing evidence | `EVIDENCE_MISSING` | `VERIFIED CLOSED` | N/A (no scope ruling required — a straightforward evidence miss) | **`VERIFIED CLOSED`** — RESOLVED | `stock/models/stock_move.py:28-31,149,193`; `stock_account/models/stock_picking.py` (full, `_is_date_in_lock_period()`); `stock_account/tests/test_account_move.py::test_backdate_picking_with_lock_date`; IER-003 [07](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/07_IER003_HIGH_H4_CUTOFF_TIMING_REVIEW.md) |
| **N-A13-02** (= H5) — company ACL / record-rule enforcement | `EVIDENCE_MISSING` | `VERIFIED WITH CONDITIONS` — ORM-layer `ir.rule` enforcement confirmed comprehensive; DB-layer gap (SAAS-03) explicitly unchanged, separate | N/A (no scope ruling required — a straightforward evidence miss, with an explicit condition) | **`VERIFIED WITH CONDITIONS`** — RESOLVED (ORM-layer); `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD` (whether every code path actually routes through the ORM vs. `sudo()`, not audited) | `stock/security/ir.model.access.csv` (full); `stock/security/stock_security.xml` (full, 16-model company-scoped `ir.rule` table); IER-003 [08](../../../../../INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/08_IER003_HIGH_H5_COMPANY_ACL_TENANT_REVIEW.md) |

## Disposition-type legend (per the governing prompt §6)

- `VERIFIED CLOSED` — IER-003 independently re-performed the evidence read and confirmed closure with primary-source citation; no Boss ruling needed.
- `CLOSED BY BOSS SCOPE EXCLUSION` — closed for Inventory-research purposes by binding governance decision (the `bh_*`/`bhpro_*` exclusion), **not** by technical proof; scope exclusion is explicitly not counted as implementation proof (Boss Inventory Scope Ruling §3: "Scope exclusion is not implementation proof").
- `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION` — closed for Inventory-research purposes because the underlying platform architecture (SaaS Tenant/Company/Branch) is an approved baseline Inventory does not own or redefine; the residual business-reality question (which legacy field the customer actually used) is carried forward to Migration/TBRAC, not resolved here.
- `VERIFIED WITH CONDITIONS` — the specific question asked (ORM-layer enforcement) is answered and closed; a narrower, explicitly-scoped residual (full code-path audit) is carried forward as a distinct future item, not silently folded into closure.

## What this reconciliation is and is not

**Is**: a documentation correction that folds already-established IER-003 evidence and binding Boss governance decisions into TEAM A's own controlled registers (A5, A7, A9, A10, A12, A13, A14, A15, A16, A17, A18 — see [04](04_CORR005_DR002_CROSS_FILE_CONSISTENCY_REPORT.md) for the full per-file change list).

**Is not**: new primary Inventory source research (none was performed — every citation above already existed in IER-003's own deliverables before this session began); a re-opening of `bh_*`/`bhpro_*` source learning; a redesign or re-research of the Tenant/Company/Branch architecture; a Boss Gate self-approval; a Team B authorization.

No Unknown was converted to a Fact by this reconciliation. No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
