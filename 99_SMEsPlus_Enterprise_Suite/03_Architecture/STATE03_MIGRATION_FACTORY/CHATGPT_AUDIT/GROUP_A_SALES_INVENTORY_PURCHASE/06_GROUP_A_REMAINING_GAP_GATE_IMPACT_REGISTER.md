> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Remaining Gap Gate-Impact Register

# 06 — REMAINING GAP GATE-IMPACT REGISTER

Every open item from `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`, plus every finding this independent review
raised on its own, classified as: `GATE BLOCKING` / `CONTROLLED CARRY-FORWARD` / `OUT-OF-SCOPE — REGISTER ONLY` /
`ALREADY RESOLVED / STALE ENTRY`.

## 01 — High-tier items (all pre-existing, Team A's own register)

| # | Item | This review's Gate-impact classification | Rationale |
|---|---|---|---|
| 4 | `account.fiscal.position`'s base model file never located | `CONTROLLED CARRY-FORWARD` | Narrow, explicitly out of CORR-003's 4-cluster scope, does not affect any Critical finding this review re-verified |
| 5 | `res.partner` multi-brand/HQ orphaned columns | `CONTROLLED CARRY-FORWARD` | Same dump-forensics technique that resolved Critical #1 (independently confirmed effective by this review in Cluster C) is flagged by Team A as a plausible future resolution path — reasonable, not urgent |
| 8 | Two uncoordinated Thai "branch" modules | `CONTROLLED CARRY-FORWARD` | Correctly TBRAC-classified as `Company Variation` (independently confirmed in Cluster D review) — a build-hygiene signal, not a blocking Unknown |

## 02 — Medium-tier items (10 total; sampled, not exhaustively re-derived)

Items 10–19 (stock_move.is_in/is_out, returned_move_ids, produce_line_ids, sale_order_line.is_service owning
module, product.type literal, purchase_order_line minor unexplained columns, stock_dropshipping full contents,
WHT form-code currency, Thai address reach) — all reviewed for registration completeness only (not re-derived
from source, consistent with a proportionate review effort for Medium-tier items).

**Classification: `CONTROLLED CARRY-FORWARD` for all 10.** Every item is narrow in blast radius, explicitly
registered (not silently dropped), and none intersects with any of the three Critical findings this review
independently re-verified in Clusters A/B/C. No Medium item was found mischaracterized in severity.

## 03 — Low-tier items (4 total)

MRP/Repair/Purchase-Requisition extension columns; `stock_warehouse` MRP/repair extension columns;
`product_template` cold-chain/manufacturing columns; `num2words` Thai-locale correctness.

**Classification: `OUT-OF-SCOPE — REGISTER ONLY` for all 4.** Correctly flagged by Team A as out-of-GROUP-A-scope
observations; appropriately not elevated.

## 04 — Findings raised by this independent review

| # | Finding | Source cluster | Severity | Gate-impact classification |
|---|---|---|---|---|
| IR-1 | Methodology note states "PostgreSQL 16" but the dump requires PostgreSQL 18-class tooling to restore at all (PG16's `pg_restore` fails immediately with a hard version error); ignored-error count also differs (18 claimed vs. 30 independently observed, same root cause) | Cluster C, §00a | MEDIUM | `CONTROLLED CARRY-FORWARD` — does not block the Gate because every substantive data claim was independently reproduced exactly with correct tooling; recommend Team A correct the tool-version statement in `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` §03 for the record, but this is a documentation-accuracy correction, not a re-opening of the underlying finding |
| IR-2 | Fit-Gap item #15's rationale ("many SME businesses expect a salesperson-initiated RMA flow") is an unqualified generalization, inconsistent with the TBRAC discipline maintained everywhere else in the pack | Cluster D, §03 | LOW | `CONTROLLED CARRY-FORWARD` — recommend a wording qualifier before/alongside Team B handoff; does not affect the validity of the underlying EXTEND candidate or block the Gate |
| IR-3 | Cluster A/B: two secondary citations not independently re-opened this pass (base `stock.rule.run()`'s reflective dispatch internals; `_action_assign()`'s negative "does not re-trigger" claim) | Cluster A/B, §02 | LOW | `OUT-OF-SCOPE — REGISTER ONLY` — disclosed for transparency; both sit adjacent to citations that WERE exactly verified, and neither is a Critical-tier claim |

## 05 — Summary

- **No item in this register is `GATE BLOCKING`.**
- **No item is `ALREADY RESOLVED / STALE ENTRY`** in the sense of contradicting a current claim — the one
  previously-stale statement in the chain (file 18's SHA-256 coverage wording) was already corrected by Team A
  before this review began (see `05_GROUP_A_GATE_PACKAGE_AND_HASH_RECONCILIATION.md` §02).
- Three new findings were raised by this review (IR-1, IR-2, IR-3), all `CONTROLLED CARRY-FORWARD` or
  `OUT-OF-SCOPE — REGISTER ONLY`, none rising to a severity that would withhold a `PASS` recommendation.
