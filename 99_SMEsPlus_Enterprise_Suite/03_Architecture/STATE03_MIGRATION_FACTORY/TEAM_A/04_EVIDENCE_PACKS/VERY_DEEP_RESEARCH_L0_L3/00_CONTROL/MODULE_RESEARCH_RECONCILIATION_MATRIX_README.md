# 692-Module Research Reconciliation Matrix — README

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** *Diagnostic reconciliation only — not a frozen denominator, not Formal Coverage, not a completeness claim.* The 300/108/284 register split is treated as **PROVISIONAL** (workbook hash mismatch unresolved); no competing universe is created: the population is the existing 692-module source enumeration (`MODULE_UNIVERSE_RECONCILIATION_692.tsv`). Prior accepted evidence (B00–B02, U01–U29, C01–C02, TXA1/TXA2/TXC/TXS and all correction packets) is carried forward unchanged.

## Reconciliation
Total modules in matrix: **692** = source enumeration (every module exactly one status).

| Status | Modules |
|---|---|
| BOUNDARY_ONLY | 227 |
| EXCLUDED_WITH_EVIDENCE | 65 |
| L3_DEEP_STUDIED | 73 |
| NOT_STUDIED | 85 |
| PARTIAL | 242 |
| **Total** | **692** |

By register phase (provisional) × status:

| Phase | Status | Modules |
|---|---|---|
| CURRENT | EXCLUDED_WITH_EVIDENCE | 29 |
| CURRENT | L3_DEEP_STUDIED | 72 |
| CURRENT | PARTIAL | 199 |
| EVIDENCE-ONLY | BOUNDARY_ONLY | 227 |
| EVIDENCE-ONLY | EXCLUDED_WITH_EVIDENCE | 36 |
| EVIDENCE-ONLY | L3_DEEP_STUDIED | 1 |
| EVIDENCE-ONLY | NOT_STUDIED | 17 |
| EVIDENCE-ONLY | PARTIAL | 3 |
| NEXT | NOT_STUDIED | 68 |
| NEXT | PARTIAL | 40 |

## Status rules (mechanical, applied in this order)
1. `EXCLUDED_WITH_EVIDENCE` — installed `test_*` framework fixtures and `theme_*` presentation modules classified in B02 (non-business; evidence = B02 + structural extract).
2. `BOUNDARY_ONLY` — non-Thai `l10n_*` country packs (FUTURE OPTIONAL COUNTRY PACK): manifest/dependency/extension-boundary profile only, by scope ruling (U27 recount is authoritative; SCOPE-R1).
3. `L3_DEEP_STUDIED` — number of claim pointers into the module ≥ max(15, 6 × non-test Python KLOC) **and** the module's best-evidence unit is not a breadth-first unit (U17–U21) **and** the module is not on the curated partial list (unread areas recorded by the owning unit). Claims come from unit capability sections that carry D1/D2/D3 and ten-dimension coverage.
4. `PARTIAL` — ≥1 claim pointer but rule 3 not met (below threshold, breadth-first primary unit, or curated unread areas).
5. `STRUCTURAL_ONLY` — no claims, but a committed L1 candidate record exists. (0 modules at this checkpoint.)
6. `NOT_STUDIED` — no claims and no committed L1 record (only the automated structural extract in the restricted local area).
**Limits of the rules:** thresholds are a diagnostic heuristic (claim density), not semantic proof; a module can be `L3_DEEP_STUDIED` here and still have runtime-only items (AWT) or be pending Claude semantic review; `PARTIAL` tiny glue modules mostly mean "mentioned once or twice".

## Claude verification column (from the verifier log, as of 2026-10-02; `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md`)
| Value (modules at L3/PARTIAL) | Modules |
|---|---|
| MECHANICAL ONLY (hash-integrity); semantic review not evidenced in verifier log | 194 |
| ACCEPTED (static tier) | 90 |
| SECURITY ESCALATION REVIEWED; semantic review queued | 27 |
| CONDITIONALLY VERIFIED (2 claims) | 4 |

`MECHANICAL ONLY` means hash-integrity intake only — the log's §28 summary states all units were verified in §10–§27, but those sections show unit-level semantic reads only for U20, U24–U29, TXA1/TXA2/TXC/TXS and the correction packets; this matrix records the **evidenced** status and asks the verifier to confirm the rest (`U01`–`U04`, `U06`–`U19`, `U21`–`U23`, `C01`, `C02`).

## Next-priority tags (queue order A→E)
| Tag | Meaning | Modules |
|---|---|---|
| - | 365 |
| B | 199 |
| C | 77 |
| D | 41 |
| D2 | 10 |

A = unfinished Thai Tax Core source-level work → units **U30–U32** (running). B = CURRENT-phase modules not yet L3. C = direct dependencies of CURRENT modules, or modules that depend on/override them, outside the CURRENT list. D = remaining NEXT-phase. D2 = other evidence-only non-country-pack modules. E = cross-module contradiction/consistency checks (scheduled after each family wave). Queue file: `NEXT_ATOMIC_UNIT_QUEUE.tsv` (U33+).

Columns of the matrix: module · register_phase · scope_class · installed_in_dump · status · status_basis · py_kloc · claim_pointers · primary_unit · all_units · existing_function_ids · c1_bound_claims · sample_pointers · db_declared_ids/db_models/db_fields (B01, installed only) · direct_depends · reverse_dep_count · claude_verification · remaining_work · next_priority.
