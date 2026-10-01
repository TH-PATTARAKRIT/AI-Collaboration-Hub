# Atomic Handoff Packet — U19

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U19` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `e4a14969d0059a12fe3062a46e326ba1f3ddc5ac` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=305 supported_pointer_and_anchor=294 unknown_class=11 neutral_ids=178` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U19_website_community.md` | `cd6c62625f3b35f5a2df60809e7fb9727a94edc5c909b4e1222e84060164eafc` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U19_website_community_NEUTRAL.md` | `9e01620aa2a70bb38030ae7ca40a4ed191feb0a5d80968a4926d8b11a62b076c` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 305 (FACT 283 · OBSERVATION 2 · INFERENCE 9 · UNKNOWN 11) |
| Neutral statements | 178 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 13 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 305 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U19-01 Public page serving, visibility levels and publishing control
- CAP-U19-02 Website form submission creating business records
- CAP-U19-03 Multi-website scoping, company binding, cookie consent and visitor tracking
- CAP-U19-04 Blog, partner showcase pages, and follow subscriptions
- CAP-U19-05 Community forum and public profiles with reputation-gated actions
- CAP-U19-06 Online courses: visibility, enrolment, invitations and completion
- CAP-U19-07 Live chat sessions, chat bots and visitor conversion
- CAP-U19-08 Public event registration and booth booking
- CAP-U19-09 Newsletter subscription, public mailing groups and rating feedback links
- CAP-U19-10 Donation payment hook and public integration endpoints

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U19-C023, VDR-U19-C066, VDR-U19-C106, VDR-U19-C204, VDR-U19-C245, VDR-U19-C248, VDR-U19-C257, VDR-U19-C259, VDR-U19-C260, VDR-U19-C264, VDR-U19-C265, VDR-U19-C266, VDR-U19-C267

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
