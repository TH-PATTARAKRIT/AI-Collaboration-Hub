# Atomic Handoff Packet — U01

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U01` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `6c566b350d988229a59097bf9f090b966d53285a` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=476 supported_pointer_and_anchor=461 unknown_class=15 neutral_ids=246` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U01_base_platform.md` | `6e01b3c45bc53a1f452f44993034219d54ee2f340d995435bc65403e67acb6e1` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U01_base_platform_NEUTRAL.md` | `0bdb9004635e01a06fa4d07da1afa66912966604efe29023eeaa2b923820ce54` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 476 (FACT 398 · OBSERVATION 26 · INFERENCE 37 · UNKNOWN 15) |
| Neutral statements | 246 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 476 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U01-01 Multi-company data-scope mechanics
- CAP-U01-02 Record rules engine
- CAP-U01-03 Access control (groups, ACL, field-level, menu/action visibility)
- CAP-U01-04 Users and authentication-related lifecycle (base only)
- CAP-U01-05 Partner master data
- CAP-U01-06 Currency and rates
- CAP-U01-07 Sequences and numbering
- CAP-U01-08 Scheduler framework
- CAP-U01-09 Server actions and automated actions
- CAP-U01-10 Configuration parameters and settings flow
- CAP-U01-11 Attachments, external identifiers, translations and language activation

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U01-C047, VDR-U01-C147, VDR-U01-C200, VDR-U01-C253, VDR-U01-C254, VDR-U01-C285, VDR-U01-C306, VDR-U01-C343, VDR-U01-C344, VDR-U01-C390, VDR-U01-C415, VDR-U01-C445, VDR-U01-C446, VDR-U01-C447, VDR-U01-C448, VDR-U01-C449

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
