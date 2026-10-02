# Atomic Handoff Packet — U42

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U42` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4b1acb4d7c5c37ef92f70db7604e515ca076134b` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=411 supported_pointer_and_anchor=404 unknown_class=7 neutral_ids=227` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U42_mail_remaining.md` | `aada99335d2de75879adeefdbd8e08d877e2c988b2636a2860024a45324b4a0c` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U42_mail_remaining_NEUTRAL.md` | `4eaa7eb8634e57c97a2aa4bb6548c3c8cdc9476f4d22d55d57d327548545ef92` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 411 (FACT 372 · OBSERVATION 12 · INFERENCE 20 · UNKNOWN 7) |
| Neutral statements | 227 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 26 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 411 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U42-01 Discussion channels, groups, chats and their members
- CAP-U42-02 Guests, presence, real-time bus coupling, call infrastructure and retention of messaging data
- CAP-U42-03 Message reactions, favourites, attachments, link previews and posting access
- CAP-U42-04 Mail composer and mass-send contract
- CAP-U42-05 Template rendering sandbox, who can edit templates, and signed action links
- CAP-U42-06 Scheduled messages and delayed notifications
- CAP-U42-07 Outgoing notification pipeline, web push, and what leaves the system
- CAP-U42-08 Mail gateway, fetchmail, bounce handling, loop protection and sender policies
- CAP-U42-09 Blacklist, opt-out and sender policies
- CAP-U42-10 Activity plans, contact and user extensions, server actions, scheduled jobs and settings

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U42-C029, VDR-U42-C076, VDR-U42-C081, VDR-U42-C082, VDR-U42-C083, VDR-U42-C088, VDR-U42-C103, VDR-U42-C108, VDR-U42-C125, VDR-U42-C136, VDR-U42-C177, VDR-U42-C251, VDR-U42-C253, VDR-U42-C258, VDR-U42-C261, VDR-U42-C262, VDR-U42-C269, VDR-U42-C276, VDR-U42-C277, VDR-U42-C315, VDR-U42-C317, VDR-U42-C318, VDR-U42-C320, VDR-U42-C341, VDR-U42-C354, VDR-U42-C365

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
