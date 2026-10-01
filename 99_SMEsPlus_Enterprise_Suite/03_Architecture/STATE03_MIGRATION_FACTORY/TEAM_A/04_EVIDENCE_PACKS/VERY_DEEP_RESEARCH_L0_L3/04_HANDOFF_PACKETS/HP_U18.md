# Atomic Handoff Packet — U18

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U18` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `a6cbd9a072fb2726f5ee4d1bf9cd9419f0bdadd5` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=470 supported_pointer_and_anchor=464 unknown_class=8 neutral_ids=136` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U18_crm_marketing_events.md` | `f52a71154603a9c92b012dcba81cb1b437934bd481d3d46f5f9d71712c097582` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U18_crm_marketing_events_NEUTRAL.md` | `2d01752f5cc99673803a5bd01f2f0291f805c33a088608dc8fe9c322c7e2b835` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 470 (FACT 452 · OBSERVATION 2 · INFERENCE 8 · UNKNOWN 8) |
| Neutral statements | 136 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 42 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 470 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U18-01 Lead and opportunity lifecycle (create, qualify, win, lose, restore, convert, merge, deduplicate)
- CAP-U18-02 Lead intake channels and assignment (teams, capacity, rules, scheduled and manual assignment)
- CAP-U18-03 Opportunity to quotation hand-off, revenue feedback and customer grading by purchase
- CAP-U18-04 Event registration, seats, tickets and automated attendee communications
- CAP-U18-05 Event ticket and booth sales, invoicing hooks and lead generation from registrations
- CAP-U18-06 Mass mailing: audience, scheduling and sending, open / click / bounce tracking, short links, marketing cards
- CAP-U18-07 Mailing consent, unsubscribe, opt-out and blacklist handling (email and SMS)
- CAP-U18-08 SMS dispatch, delivery reports, prepaid-credit consumption and failure behaviour
- CAP-U18-09 External-service data exchange and prepaid credits: IAP accounts, lead enrichment, lead mining, partner autocomplete, VAT lookup
- CAP-U18-10 Survey participation, scoring, certification and lead generation from answers

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U18-C059, VDR-U18-C060, VDR-U18-C086, VDR-U18-C089, VDR-U18-C101, VDR-U18-C103, VDR-U18-C132, VDR-U18-C192, VDR-U18-C194, VDR-U18-C242, VDR-U18-C245, VDR-U18-C249, VDR-U18-C264, VDR-U18-C270, VDR-U18-C316, VDR-U18-C325, VDR-U18-C327, VDR-U18-C341, VDR-U18-C345, VDR-U18-C352, VDR-U18-C360, VDR-U18-C363, VDR-U18-C368, VDR-U18-C369, VDR-U18-C377, VDR-U18-C379, VDR-U18-C390, VDR-U18-C406, VDR-U18-C415, VDR-U18-C417, VDR-U18-C418, VDR-U18-C419, VDR-U18-C420, VDR-U18-C422, VDR-U18-C424, VDR-U18-C425, VDR-U18-C426, VDR-U18-C427, VDR-U18-C447, VDR-U18-C452, VDR-U18-C453, VDR-U18-C454

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
