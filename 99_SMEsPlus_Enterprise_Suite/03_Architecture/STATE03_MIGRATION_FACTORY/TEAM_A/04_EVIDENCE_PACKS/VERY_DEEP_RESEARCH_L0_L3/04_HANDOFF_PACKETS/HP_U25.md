# Atomic Handoff Packet — U25

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U25` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `6e31d186fb216a43c571222ebcc6591e0ff21d7d` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=299 supported_pointer_and_anchor=288 unknown_class=11 neutral_ids=213` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U25_multicurrency_international.md` | `4f47184241885418fb1944c2c04694ef3343e315e399c45f359e8eafdc614ffd` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U25_multicurrency_international_NEUTRAL.md` | `0c42b85f508f4279a551cdbaceab5e48b24c10b70808df4d8c730a95392acc6e` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 299 (FACT 223 · OBSERVATION 14 · INFERENCE 51 · UNKNOWN 11) |
| Neutral statements | 213 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 25 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 299 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U25-01 Currency catalogue and exchange-rate model
- CAP-U25-02 Document currency and rate dates on orders, invoices and payments
- CAP-U25-03 Foreign-currency accounting entries, reconciliation and exchange differences
- CAP-U25-04 Foreign-currency payments, bank statements and write-offs
- CAP-U25-05 Foreign customer and vendor master data and tax treatment
- CAP-U25-06 International trade documents and logistics
- CAP-U25-07 Foreign-currency reporting, revaluation, price lists and rounding
- CAP-U25-08 Multi-company and multi-currency interplay, including foreign-owned structures in Thailand
- CAP-U25-09 Roles, access, validation constraints and failure behaviour

## Contradiction claim ids
VDR-U25-C286

## Runtime-required claim ids
VDR-U25-C020, VDR-U25-C024, VDR-U25-C048, VDR-U25-C051, VDR-U25-C078, VDR-U25-C104, VDR-U25-C105, VDR-U25-C109, VDR-U25-C113, VDR-U25-C114, VDR-U25-C115, VDR-U25-C116, VDR-U25-C153, VDR-U25-C154, VDR-U25-C155, VDR-U25-C156, VDR-U25-C180, VDR-U25-C181, VDR-U25-C182, VDR-U25-C203, VDR-U25-C211, VDR-U25-C264, VDR-U25-C265, VDR-U25-C282, VDR-U25-C284

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
