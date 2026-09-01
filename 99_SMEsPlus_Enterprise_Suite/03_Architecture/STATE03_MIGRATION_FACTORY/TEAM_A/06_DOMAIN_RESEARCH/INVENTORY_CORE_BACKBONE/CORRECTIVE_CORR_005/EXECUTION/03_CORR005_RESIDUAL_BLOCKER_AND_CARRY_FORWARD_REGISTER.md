# 03 — Residual Blocker and Carry-Forward Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Recompute residual counts from the reconciled package and distinguish open Inventory research blockers from controlled cross-domain carry-forwards | Claude (Team A, CORR-005) | This artifact; A14 §Mechanical count reconciliation, A15 §2 | 2026-09-01 | Independent Delta Re-Review (required next) | Recomputed, not copied | Primary count-of-record for the CORR-005 package |

Per the governing prompt §7, the original DR-002 terminal count (`0 Critical / 5 High / 14 Medium / 7 Low`) is **not** copied forward. It is recomputed below from the reconciled register (`A14` §Part 3), with two distinct views.

## View 1 — Open Inventory Research Blockers

Items still actionable by further authorized Inventory evidence research.

| Severity | Open (2026-08-31, original) | Change this reconciliation | Open (2026-09-01, reconciled) |
|---|---:|---|---:|
| Critical | 0 | none | **0** |
| High | 5 | −5 (3 → `RESOLVED`; 2 → `CONTROLLED CARRY-FORWARD`, moved to View 2) | **0** |
| Medium | 14 | none — no Medium item is among the five High items reconciled here | **14** |
| Low | 7 | none | **7** |
| **Total** | **26** | **−5** | **21** |

The 14 open Medium items (GRPA-M11, M12, M13, M14, M15, M16, M18, M19, N-DB-01, N-CONC-01, N-A7-01, N-A7-02, N-A7-04, N-A12-01) and 7 open Low items (GRPA-L20–L23, N-A13-01, N-A5-02, N-A5-03) are listed in full in `DEEP_RESEARCH_DR002/EXECUTION/A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` Part 1/Part 2 and are unchanged by this reconciliation — none was in the five-High scope this session was authorized to reconcile.

## View 2 — Controlled Carry-Forwards

Items no longer classified as open Inventory research blockers, but still relevant to another workstream. None of these is counted in View 1's totals; none is silently dropped.

| ID | Carry-forward type | Owning workstream | What is carried forward | What must NOT be inferred from this carry-forward |
|---|---|---|---|---|
| GRPA-H5 (H2) | `CONTROLLED MIGRATION CARRY-FORWARD` | Migration | The existence of `bh_parent_company`-owned `res.partner` columns and their populated legacy data, so a migration does not silently lose them (A12 §12) | That `bh_parent_company`'s internal logic, validation rules, or schema is known, safe, or suitable as a SMEsPlus design reference — it is not, and is not to be sourced further |
| GRPA-H8 (H3) | `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` | Migration / TBRAC (real-user validation) | The legacy `branch` (`l10n_th_partner`) vs. `company_registry` (`l10n_th`) field-mapping question — which value, if either, was the customer's actual operational practice (A12 §12) | That either legacy field is Thailand-wide statutory truth, or that the SMEsPlus platform Branch model is undecided — it is an approved baseline, not reopened |
| GRPA-H8 (H3) | `ACCOUNTING/TAX CARRY-FORWARD` | Accounting / Tax | Thai tax-document branch semantics remain an Accounting/Tax interface concern | That Inventory owns or has resolved tax-document branch representation |
| N-A13-02 residual | `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD` | Future implementation/test verification (SaaS) | Whether every code path in `stock_account`/`sale_stock`/`purchase_stock`/`mrp` that touches company-scoped models actually routes through the standard ORM (and thus respects the confirmed `ir.rule` set) versus using `sudo()` internally — not audited by IER-003 | That ORM-layer enforcement (now confirmed) is equivalent to DB-layer enforcement — SAAS-03 (A10) remains a separate, open, unchanged concern |

**Total: 3 distinct carry-forward items (H2 → 1, H3 → 2, N-A13-02 residual → 1, counted here as 4 rows because H3 spans two owning workstreams for the same underlying item).**

## Combined statement

**21 open Inventory research blockers (0 Critical / 0 High / 14 Medium / 7 Low) + 4 controlled carry-forward rows spanning 3 distinct items, none Inventory-Gate-blocking, none silently dropped.**

No Boss scope exclusion is counted as technical implementation proof anywhere in this register (Boss Inventory Scope Ruling §3: "Scope exclusion is not implementation proof"). No carry-forward is presented as a Fact. If a material Critical/High Inventory research blocker beyond these five had been discovered during reconciliation, it would be registered here honestly rather than concealed to force a ready status — none was found; see [04](04_CORR005_DR002_CROSS_FILE_CONSISTENCY_REPORT.md) for the consistency sweep that checked for exactly this.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
