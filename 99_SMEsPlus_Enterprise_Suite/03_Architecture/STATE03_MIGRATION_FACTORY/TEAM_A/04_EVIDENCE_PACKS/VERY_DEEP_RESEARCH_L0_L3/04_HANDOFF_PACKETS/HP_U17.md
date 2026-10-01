# Atomic Handoff Packet — U17

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U17` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `0556fad6571d6d7ba270a39d77c54f5e35bca60a` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=499 supported_pointer_and_anchor=488 unknown_class=11 neutral_ids=207` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U17_hr_fleet_calendar.md` | `3e1ebc21a966b63f16679a3b2d8b148af14a705a5d8aeac03097db621b33985c` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U17_hr_fleet_calendar_NEUTRAL.md` | `4026969960829ee5b4d40b83784665682ae5a3b487b99ed1df5105f06bd23bb2` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 499 (FACT 455 · OBSERVATION 13 · INFERENCE 20 · UNKNOWN 11) |
| Neutral statements | 207 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 499 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U17-01 Employee master record and dated versions
- CAP-U17-02 Employee data access scoping, manager hierarchy and company boundaries
- CAP-U17-03 Time-off request lifecycle and approval
- CAP-U17-04 Time-off allocations, accrual plans and balances
- CAP-U17-05 Attendance recording, kiosk and overtime
- CAP-U17-06 Work entry generation, conflict control and validation
- CAP-U17-07 Recruitment pipeline
- CAP-U17-08 Skills, resumes and certifications
- CAP-U17-09 Fleet vehicles, contracts, services and driver assignment
- CAP-U17-10 Calendar events, attendees, invitations and reminders

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U17-C090, VDR-U17-C178, VDR-U17-C224, VDR-U17-C269, VDR-U17-C270, VDR-U17-C273, VDR-U17-C279, VDR-U17-C355, VDR-U17-C431, VDR-U17-C440, VDR-U17-C441, VDR-U17-C442, VDR-U17-C443, VDR-U17-C447, VDR-U17-C451, VDR-U17-C497

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
