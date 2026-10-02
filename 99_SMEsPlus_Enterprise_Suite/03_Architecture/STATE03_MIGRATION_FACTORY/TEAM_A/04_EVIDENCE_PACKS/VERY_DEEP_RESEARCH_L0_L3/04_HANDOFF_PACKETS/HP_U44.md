# Atomic Handoff Packet — U44

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U44` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `965bfe005afec384e538994d457a656d6a7db804` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=193 supported_pointer_and_anchor=193 unknown_class=1 neutral_ids=138` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U44_mrp_bridges_onboarding_partner.md` | `a3b715b0a1618db315d85880d1271969a3d1a06617fae430bb6a30b226a405fc` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U44_mrp_bridges_onboarding_partner_NEUTRAL.md` | `ffb102f22358a1c784b16bc7f3aa00b153efbac50f408e837de475f6009576d4` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 193 (FACT 178 · OBSERVATION 14 · INFERENCE 0 · UNKNOWN 1) |
| Neutral statements | 138 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 25 |
| Claims bound to an existing C1 Function-ID | 68 (distinct C1 IDs: BRP-F03, BRP-F08, GRV-F05) |
| Claims with an existing Function-ID | 86; `FUNCTION MAPPING REQUIRED`: 107 |
| Existing Function-IDs referenced | BRP-F03×51, BRP-F08×2, BRP-F09×10, GRV-F05×15, MFG-F04×8 |

## Capabilities in scope
- CAP-U44-01 Landed costs on production orders and subcontract receipts
- CAP-U44-02 Subcontracting valuation and portal analytic access
- CAP-U44-03 Purchase and subcontracting bridge (resupply, lead time, demand, report)
- CAP-U44-04 Dropship subcontracting
- CAP-U44-05 Expiry confirmation and repair bridges
- CAP-U44-06 BoM Overview report
- CAP-U44-07 MO Overview report and printed production documents
- CAP-U44-08 Onboarding steps and panels
- CAP-U44-09 Partner autocomplete and enrichment (outbound data)
- CAP-U44-10 Partnership grades and price lists

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U44-C008, VDR-U44-C022, VDR-U44-C023, VDR-U44-C024, VDR-U44-C025, VDR-U44-C028, VDR-U44-C040, VDR-U44-C041, VDR-U44-C058, VDR-U44-C061, VDR-U44-C073, VDR-U44-C086, VDR-U44-C094, VDR-U44-C114, VDR-U44-C130, VDR-U44-C139, VDR-U44-C146, VDR-U44-C148, VDR-U44-C151, VDR-U44-C154, VDR-U44-C156, VDR-U44-C161, VDR-U44-C175, VDR-U44-C181, VDR-U44-C182

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
