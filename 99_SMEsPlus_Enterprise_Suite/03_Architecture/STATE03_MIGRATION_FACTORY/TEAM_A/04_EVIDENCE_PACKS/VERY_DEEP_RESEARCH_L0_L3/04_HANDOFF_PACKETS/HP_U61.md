# Atomic Handoff Packet — U61

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U61` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `e0b1c6226f68b0da9aa98edf8259bae85a6f38f9` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=130 supported_pointer_and_anchor=130 unknown_class=0 neutral_ids=40` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U61_website_portal_bridges.md` | `3ce0f749d62273a6cc5f242dea27954c5c2005a8506576ba8e8c5b005c679ae5` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U61_website_portal_bridges_NEUTRAL.md` | `89b506943f42e8ea1dc0db0b5e51e990537dbec725c7e76c4cc09a1366631266` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 130 (FACT 130 · OBSERVATION 0 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 40 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 0 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 130; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U61-01 — Forum: public Q&A with karma-gated participation
- CAP-U61-02 — Google Maps: partner/company location widget
- CAP-U61-03 — HR Recruitment: public job listing and online application
- CAP-U61-04 — HR Recruitment Livechat: chatbot for recruitment flow
- CAP-U61-05 — Website Links: short-link tracking and UTM
- CAP-U61-06 — Website Livechat: live chat widget and visitor tracking
- CAP-U61-07 — Website Mail: email subscription (follow) management
- CAP-U61-08 — Website Partner: public partner directory
- CAP-U61-09 — Website Payment: multi-website provider and donation
- CAP-U61-10 — Website Profile: karma-based public user profile
- CAP-U61-11 — Website Project: task submission portal
- CAP-U61-12 — Website Slides (eLearning): courses, slides, quizzes, enrollment
- CAP-U61-13 — Website Slides Forum: forum embedded within eLearning channel
- CAP-U61-14 — Website SMS: SMS contact action from visitor
- CAP-U61-15 — Website Timesheet: portal timesheet visibility gate

## Contradiction claim ids
none

## Runtime-required claim ids
none

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
