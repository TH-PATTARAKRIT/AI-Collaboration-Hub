# Atomic Handoff Packet — U47

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U47` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `f293c19afe1e4366a5e6acb1da4890c82fb9f220` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=150 supported_pointer_and_anchor=150 unknown_class=0 neutral_ids=49` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U47_account_remaining.md` | `e357970b697a33d57f52dc289a9c97f2ca340f6204d320a8482eea5349b36f67` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U47_account_remaining_NEUTRAL.md` | `9fb53020751f61c2a00cb763651978790fae024b6a960902f05983454faa80ec` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 150 (FACT 150 · OBSERVATION 0 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 49 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 1 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 150; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U47-01 Bank Statement Line Model and Reconciliation Engine
- CAP-U47-02 Currency Table and Multi-Currency Reporting
- CAP-U47-03 Payment Register Wizard
- CAP-U47-04 Accrued Orders Wizard
- CAP-U47-05 Account Move Reversal Wizard
- CAP-U47-06 Partial Reconcile Model and Tax Cash Basis Engine
- CAP-U47-07 Full Reconcile Model
- CAP-U47-08 Reconcile Model (Bank Statement Matching Rules)
- CAP-U47-09 Payment Terms Model
- CAP-U47-10 Cash Rounding Model

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U47-C117

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
