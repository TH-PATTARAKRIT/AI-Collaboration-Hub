# Atomic Handoff Packet — U21

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U21` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `48093292ea347b9e625e2fd13aa0d38551e61422` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=519 supported_pointer_and_anchor=514 unknown_class=9 neutral_ids=235` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U21_platform_security_integration.md` | `0ec45d4189a76729e5b80cda334fa7851c93787736cd82ea285b668067dca817` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U21_platform_security_integration_NEUTRAL.md` | `a7dc788c3d9117d99358c0bbfa62f041cbaa086fc8dd46fa67e6f47e487aee0e` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 519 (FACT 415 · OBSERVATION 33 · INFERENCE 62 · UNKNOWN 9) |
| Neutral statements | 235 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 10 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 519 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U21-01 Second-factor sign-in (authenticator codes and e-mailed codes)
- CAP-U21-02 Passkey sign-in and credential management
- CAP-U21-03 Browser sign-in, sessions, request-forgery protection and real-time channels
- CAP-U21-04 Programmatic access (remote calls, API keys, documentation, database service)
- CAP-U21-05 Data import (spreadsheet-style files and data-module packages)
- CAP-U21-06 Certificate and key storage
- CAP-U21-07 Third-party account links (calendar synchronisation and mail-server sign-in)
- CAP-U21-08 Other outbound service calls and add-in access
- CAP-U21-09 Spreadsheet formulas, dashboards and sharing
- CAP-U21-10 Privacy lookup and erasure, and small platform utilities

## Contradiction claim ids
VDR-U21-C181, VDR-U21-C212

## Runtime-required claim ids
VDR-U21-C110, VDR-U21-C118, VDR-U21-C151, VDR-U21-C205, VDR-U21-C228, VDR-U21-C315, VDR-U21-C428, VDR-U21-C463, VDR-U21-C515, VDR-U21-C519

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
