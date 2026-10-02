# Atomic Handoff Packet — U37

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U37` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `638ea932a577239fbf60acee7117bac280243aef` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=472 supported_pointer_and_anchor=462 unknown_class=10 neutral_ids=112` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U37_base_family_bus_calendar_cloud.md` | `c60b432f5de69b5d91e067a68c3d90480962161e5f1bd9e8419cc6e8327a72a2` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U37_base_family_bus_calendar_cloud_NEUTRAL.md` | `bbc8b2c849afa147635c614874145148bb747568acc81411eaa96c45485a5dd2` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 472 (FACT 449 · OBSERVATION 6 · INFERENCE 7 · UNKNOWN 10) |
| Neutral statements | 112 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 11 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 472 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U37-01 Contact directory application
- CAP-U37-02 Address geolocation
- CAP-U37-03 Bank account number validation
- CAP-U37-04 Record import from spreadsheet and text files
- CAP-U37-05 Module package import and installation requests
- CAP-U37-06 Real-time notification channel
- CAP-U37-07 Calendar events, attendees, recurrence and visibility
- CAP-U37-08 Event reminders, invitations and text-message reminders
- CAP-U37-09 Certificates and cryptographic keys
- CAP-U37-10 Add-ons not installed in the examined database

## Contradiction claim ids
VDR-U37-C415

## Runtime-required claim ids
VDR-U37-C027, VDR-U37-C056, VDR-U37-C079, VDR-U37-C144, VDR-U37-C198, VDR-U37-C251, VDR-U37-C330, VDR-U37-C374, VDR-U37-C415, VDR-U37-C418, VDR-U37-C472

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
