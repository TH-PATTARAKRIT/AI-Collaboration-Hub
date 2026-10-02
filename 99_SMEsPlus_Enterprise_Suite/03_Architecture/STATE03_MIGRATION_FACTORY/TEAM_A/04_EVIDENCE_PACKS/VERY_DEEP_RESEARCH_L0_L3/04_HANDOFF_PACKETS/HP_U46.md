# Atomic Handoff Packet — U46

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U46` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `a8141b70b13e34978798000f6fb39f8823ae8bce` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=1198 supported_pointer_and_anchor=1198 unknown_class=0 neutral_ids=888` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U46_project_purchase_resource_family.md` | `2d081d2e1e21dd711ef7df8532d9f12a793fae9ede9fc9f6f7efbd5a9ef3e5f4` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U46_project_purchase_resource_family_NEUTRAL.md` | `2f7012399e9660e63211a72f479c7b23e1507882d51552175c5ef4bed0b2ca85` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 1198 (FACT 1145 · OBSERVATION 24 · INFERENCE 29 · UNKNOWN 0) |
| Neutral statements | 888 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 19 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 1198 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U46-01 Project definition, lifecycle, stages, templates and roles
- CAP-U46-02 Project access control, visibility, collaborators and portal sharing
- CAP-U46-03 Task lifecycle: stages, assignment, dependencies, recurrence, closing
- CAP-U46-04 Milestones, project updates, burndown and task analysis reports
- CAP-U46-05 Customer rating
- CAP-U46-06 Project cost and revenue bridges (profitability and analytic)
- CAP-U46-07 Collaboration extensions: personal tasks, text messages, mail add-in, skills, resource calendars
- CAP-U46-08 Purchase: requests for quotation, orders, receipts, vendor bills and extensions
- CAP-U46-10 External call interfaces (legacy XML/JSON and bearer-key JSON interface)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U46-C167, VDR-U46-C271, VDR-U46-C319, VDR-U46-C358, VDR-U46-C383, VDR-U46-C396, VDR-U46-C617, VDR-U46-C654, VDR-U46-C726, VDR-U46-C752, VDR-U46-C771, VDR-U46-C794, VDR-U46-C826, VDR-U46-C861, VDR-U46-C965, VDR-U46-C967, VDR-U46-C1083, VDR-U46-C1098, VDR-U46-C1103

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
