# 10 — Unknown Register Mechanical Count Reconciliation

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently, mechanically recompute A14's counts rather than trust the prose recount | Independent Evidence Reviewer | A14 tables, recounted row-by-row | 2026-09-01 | Boss | **RECONCILED — TEAM A's claimed counts are correct** | No count-integrity finding; separately, this review's own verdicts change 3 of the 5 High items' *disposition* without changing the *count* |

## 1. Mechanical recount, performed independently against A14's actual rows (not its own prose summary)

| Severity | Rows counted directly from A14 Part 1 + Part 2 tables | TEAM A's claimed count (A14 §"Mechanical count reconciliation", restated authoritatively in A15 §2) | Match? |
|---|---|---|---|
| Critical open | Part 1 "Critical" table: 3 rows, all `RESOLVED` → 0 open | 0 | **MATCH** |
| High open | Part 1 "High — 3 remain open": GRPA-H4, GRPA-H5, GRPA-H8 (3 rows) + Part 2: N-A7-03/N-A9-02 (1 row, 2 IDs), N-A13-02 (1 row) = 5 rows | 5 | **MATCH** |
| Medium open | Part 1 "Medium" table: 10 rows, of which M10 and M17 marked `RESOLVED` this pass → 8 open (M11,M12,M13,M14,M15,M16,M18,M19) + Part 2: 6 new rows (N-DB-01, N-CONC-01, N-A7-01, N-A7-02, N-A7-04, N-A12-01), all open → 8+6 = 14 | 14 | **MATCH** |
| Low open | Part 1 "Low" table: 4 rows (GRPA-L20–L23), all open + Part 2: 3 new rows (N-A13-01, N-A5-02, N-A5-03), all open → 4+3 = 7 | 7 | **MATCH** |
| **Total open** | 0+5+14+7 = **26** | 26 (A15 §2 "Total open") | **MATCH** |

**A14's own "shown working" recount language (its final paragraph, showing 8+6=14 and 4+3=7 arithmetic explicitly) is exactly what it claims to be — intentional transparency about the arithmetic, not a symptom of an actual miscount.** This independent recount confirms both the intermediate and final figures are internally consistent and match the authoritative restatement in A15 §2.

## 2. Duplicate / alias ID check

Every ID in A14 Part 1 and Part 2 was checked for uniqueness: no ID appears twice, and no two different topics share one ID. `GRPA-H8` is explicitly cross-referenced as `(= this pass's SAAS-02/TH-INV-01)` — this is a deliberate, disclosed cross-reference between related-but-differently-scoped entries in three separate registers (A14/A10/A11), not a duplicate-counting error; each register counts it once, in its own table, for its own purpose. **No duplicate/alias-ID issue found.**

## 3. Severity/status inconsistency check

Checked every row for internal consistency between its declared `Status` column and its presence in the severity bucket it's counted under: no row was found miscategorized (e.g., no row marked `RESOLVED` counted as open, no row with an open status omitted from its severity's open count). **No inconsistency found.**

## 4. Items marked resolved but still used as blockers elsewhere — checked

GRPA-M10 and GRPA-M17 (this pass's two Medium resolutions) were checked against every other A0–A20 deliverable for residual "still treated as open" references: neither appears anywhere outside A14 with an unresolved framing — A9 §2 and A6 §4 both cite the same underlying facts (`is_in`/`is_out` semantics; `Procurement` NamedTuple) in their *resolved*, confirmed form. The three independently-re-confirmed Critical resolutions (GRPA-Crit-1/2/3) are likewise consistently referenced as resolved throughout (A6 §2 for Crit-3; A14 Part 1 itself for 1/2). **No stale-blocker inconsistency found.**

## 5. Effect of this review's own verdicts on the register — disposition change, not count change

This review's independent verdicts in [04](04_IER003_HIGH_H1_FISCAL_POSITION_BOUNDARY_REVIEW.md)–[08](08_IER003_HIGH_H5_COMPANY_ACL_TENANT_REVIEW.md) close or substantially advance 3 of the 5 High items (GRPA-H4, N-A7-03/N-A9-02, N-A13-02) and materially advance a 4th (GRPA-H5). **This does not change TEAM A's own package's counts** — A14/A15 remain an accurate record of what TEAM A itself established as of its own session close, and this review does not edit them (per the independence rules). It changes what the *next* TEAM A pass's register should say once these findings are folded in — see [14](14_IER003_TARGETED_TEAM_A_CORRECTIVE_RECOMMENDATION.md) for the precise, itemized correction scope, and [13](13_IER003_FINDING_AND_GATE_IMPACT_REGISTER.md) for the consolidated finding-level register this review produces in its own right.

## Disposition

**Count integrity: VERIFIED, no discrepancy.** This is a positive integrity finding about TEAM A's own bookkeeping discipline, independent of and additional to the substantive corrections found elsewhere in this review.

No Unknown was converted to a Fact anywhere in this reconciliation. No item is silently dropped.
