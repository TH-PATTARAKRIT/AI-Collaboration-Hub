# Atomic Handoff Packet — U39

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U39` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `b8676ee2e78d4f6fa25fd0f605a5d5ba9a8c7b78` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=549 supported_pointer_and_anchor=539 unknown_class=10 neutral_ids=196` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U39_hr_google_part_a.md` | `4605753af996ebe63759acfe4908280c724e1d47c6b0e46e391915000507a730` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U39_hr_google_part_a_NEUTRAL.md` | `b5b5af154946d58b3769692c16ab66d8b9add436d6923b8540bed23b8a53ec15` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 549 (FACT 492 · OBSERVATION 13 · INFERENCE 34 · UNKNOWN 10) |
| Neutral statements | 196 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 54 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 549 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U39-01 Linking a user's Google calendar account and controlling synchronization
- CAP-U39-02 Two-way synchronization of calendar events with Google Calendar
- CAP-U39-03 Connecting mail servers to Gmail with delegated sign-in
- CAP-U39-04 Bot protection of public forms with a risk-scoring service
- CAP-U39-05 Employee master record, dated versions, contracts and linked user and contact
- CAP-U39-06 Employee departure, onboarding and offboarding plans, alias and channel hooks
- CAP-U39-07 Organisation structure, reference lists, access scoping and salary-account splitting
- CAP-U39-08 Attendance recording, kiosk, automatic check-out and absence detection
- CAP-U39-09 Overtime rules, rule sets and the overtime ledger
- CAP-U39-10 Employee-aware bridges: calendar availability, company vehicles and recognition badges

## Contradiction claim ids
VDR-U39-C513

## Runtime-required claim ids
VDR-U39-C011, VDR-U39-C012, VDR-U39-C021, VDR-U39-C029, VDR-U39-C035, VDR-U39-C045, VDR-U39-C046, VDR-U39-C050, VDR-U39-C053, VDR-U39-C063, VDR-U39-C084, VDR-U39-C090, VDR-U39-C091, VDR-U39-C099, VDR-U39-C102, VDR-U39-C104, VDR-U39-C112, VDR-U39-C118, VDR-U39-C125, VDR-U39-C126, VDR-U39-C127, VDR-U39-C135, VDR-U39-C136, VDR-U39-C144, VDR-U39-C147, VDR-U39-C157, VDR-U39-C175, VDR-U39-C176, VDR-U39-C178, VDR-U39-C179, VDR-U39-C185, VDR-U39-C187, VDR-U39-C194, VDR-U39-C209, VDR-U39-C210, VDR-U39-C284, VDR-U39-C300, VDR-U39-C304, VDR-U39-C328, VDR-U39-C357, VDR-U39-C368, VDR-U39-C370, VDR-U39-C374, VDR-U39-C402, VDR-U39-C406, VDR-U39-C418, VDR-U39-C457, VDR-U39-C475, VDR-U39-C478, VDR-U39-C500, VDR-U39-C526, VDR-U39-C529, VDR-U39-C530, VDR-U39-C549

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
