# 14 — Targeted TEAM A Corrective Recommendation

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Specify the precise correction scope for the next TEAM A Inventory session — not perform it | Independent Evidence Reviewer | This artifact | 2026-09-01 | Boss / TEAM A (next session) | Recommendation only | Does not block the Gate decision — see [16](16_IER003_BOSS_GATE_RECOMMENDATION.md) |

Per the controlling prompt's independence rules, this review may recommend TEAM A's corrective scope but may not perform it. The items below are documentation/register updates a future TEAM A session should make; none requires new primary research this review has not already supplied the evidence for.

## 1. Documentation corrections (evidence already supplied by this review — fold in, do not re-research)

| Register | Current entry | Recommended update | Source |
|---|---|---|---|
| A14 GRPA-H4 | `EVIDENCE_MISSING` | `RESOLVED` — cite `01 ACCOUNT/account/models/partner.py:27` | [04](04_IER003_HIGH_H1_FISCAL_POSITION_BOUNDARY_REVIEW.md) |
| A14 N-A7-03/N-A9-02 | `EVIDENCE_MISSING` | `RESOLVED` — cite `stock/models/stock_move.py:28-193` and `stock_account/models/stock_picking.py` (full) | [07](07_IER003_HIGH_H4_CUTOFF_TIMING_REVIEW.md) |
| A14 N-A13-02 | `EVIDENCE_MISSING` | `RESOLVED (ORM-layer); SAAS-03 DB-layer gap remains separately open` — cite `stock/security/stock_security.xml` (full) | [08](08_IER003_HIGH_H5_COMPANY_ACL_TENANT_REVIEW.md) |
| A14 GRPA-H5 | `EVIDENCE_MISSING` | `PARTIALLY VERIFIED` — owning module identified as `bh_parent_company` (author BHPRO) via `ir_model_data`; source still absent from machine | [05](05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md) |
| A14 GRPA-M14 | `PARTIALLY VERIFIED` | `RESOLVED` — live data contains zero legacy `'product'` values | [03](03_IER003_PRIMARY_CLAIM_REPERFORMANCE_REPORT.md) §3 |
| A5 §3 (branch = child res.company) | States this as established fact | Soften to "structurally available via `res.company.parent_id`, not confirmed as this customer's actual practice (single-company dataset)" | [06](06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md) |
| A16 scenario 6 | `NOT READY` | `Inventory side ready` | [11](11_IER003_ACCOUNTING_X_INVENTORY_CROSS_PROOF_READINESS.md) |
| A16 scenario 9 | `NOT READY` | `Inventory side ready; Accounting side still pending` | [11](11_IER003_ACCOUNTING_X_INVENTORY_CROSS_PROOF_READINESS.md) |
| A2/A20 (N-DB-01) | `EVIDENCE_MISSING — ENVIRONMENTAL LIMITATION` | `RESOLVED` — a session with container-provisioning permission completed the restore; see [09](09_IER003_DATABASE_DUMP_REVERIFICATION_REPORT.md) | This review |

## 2. New item to register (not a correction — a new disclosure this review surfaced)

Add to A14 Part 2: the `iTEST02` dump's `stock_quant` table is empty and `stock_move` has only 48 rows with none `done` — register as a new Low/Medium item (data-volume caveat for any future empirical Cross-Proof testing against this specific dump). See [13](13_IER003_FINDING_AND_GATE_IMPACT_REGISTER.md) F1.

## 3. Genuine remaining research gaps — unchanged, still open, still TEAM-A-actionable if a future pass is scoped for them

N-A7-01, N-A7-02, N-A7-04, N-A12-01, N-CONC-01, N-A13-01, N-A5-02, N-A5-03, and all GROUP A carried-forward Medium/Low items other than M14. None of these was in this review's five-High scope; none is corrected or closed here. A future TEAM A pass scoped to close these would be doing genuine incremental research, not merely documentation upkeep — distinguish this from §1 above when prioritizing.

## 4. Explicitly NOT recommended

- **Not recommended**: re-running the blocked DB restore — it is no longer blocked; this review already supplied the queries and results needed for §1's corrections. A future session should reuse this review's results DELTA-FIRST rather than re-restore from scratch, consistent with the project's own established DELTA-FIRST convention.
- **Not recommended**: re-opening GRPA-H1/H4/H8's Thailand-regulatory or real-user-validation dependencies as if they were source-research tasks — they are external dependencies (see [16](16_IER003_BOSS_GATE_RECOMMENDATION.md)), not something a source-reading session can close.
- **Not recommended**: treating this list as authorization for TEAM B Inventory design, schema/API/ORM work, or any lifecycle stage beyond a documentation-correction pass to TEAM A's own register.

No Evidence = No Progress. This recommendation is corrective and additive only — it does not ask TEAM A to retract or apologize for any prior finding; every correction above is a case where TEAM A itself already disclosed the gap honestly (`EVIDENCE_MISSING`/`PARTIALLY VERIFIED`) rather than asserting false certainty.
