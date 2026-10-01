# Atomic Handoff Packet — U15

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U15` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `a820711a47a9e0785cffddccdd5dd0cf6527ae37` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=355 supported_pointer_and_anchor=345 unknown_class=10 neutral_ids=205` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U15_mrp_accounting_subcontracting.md` | `c213dbf00ae0e501c02809890aa32bf26ede289834215bae6a7cf1907aabb700` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U15_mrp_accounting_subcontracting_NEUTRAL.md` | `83cf73635e6ce3676e12835c0dc87541afe5bf04bd1522d66e1c0fdc2d0135a6` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 355 (FACT 286 · OBSERVATION 26 · INFERENCE 33 · UNKNOWN 10) |
| Neutral statements | 205 |
| Contradiction (CONTRA) claims | 5 |
| Runtime/AWT-required (RT) claims | 24 |
| Claims bound to an existing C1 Function-ID | 168 (distinct C1 IDs: BRP-F01, BRP-F03, BRP-F08, GRV-F05, MFG-F01, MFG-F02) |
| Claims with an existing Function-ID | 242; `FUNCTION MAPPING REQUIRED`: 113 |
| Existing Function-IDs referenced | BRP-F01×1, BRP-F02×8, BRP-F03×105, BRP-F04×22, BRP-F08×12, GRV-F05×12, MFG-F01×20, MFG-F02×18, MFG-F03×15, MFG-F04×29 |

## Capabilities in scope
- CAP-U15-01 Manufacturing order cost computation and by-product cost allocation
- CAP-U15-02 Production accounting postings (consumption, finished goods, labour) and manual WIP entry
- CAP-U15-03 Work-centre cost handling, analytic and project cost tracking
- CAP-U15-04 Cost roll-up from the BoM and kit valuation treatment
- CAP-U15-05 Landed costs on manufacturing orders and subcontracting receipts
- CAP-U15-06 Subcontracting set-up: BoM type, subcontractors, locations, routes and operation types
- CAP-U15-07 Receipt-driven subcontract production, tracking, returns and the subcontractor portal
- CAP-U15-08 Subcontracting valuation, purchase and drop-shipping integration
- CAP-U15-09 Repair order lifecycle and its stock movements
- CAP-U15-10 Repair links to sales, kits, manufacturing, purchasing and accounting

## Contradiction claim ids
VDR-U15-C020, VDR-U15-C046, VDR-U15-C052, VDR-U15-C068, VDR-U15-C084

## Runtime-required claim ids
VDR-U15-C039, VDR-U15-C050, VDR-U15-C061, VDR-U15-C063, VDR-U15-C072, VDR-U15-C087, VDR-U15-C089, VDR-U15-C090, VDR-U15-C114, VDR-U15-C118, VDR-U15-C141, VDR-U15-C153, VDR-U15-C163, VDR-U15-C199, VDR-U15-C230, VDR-U15-C232, VDR-U15-C235, VDR-U15-C236, VDR-U15-C258, VDR-U15-C267, VDR-U15-C317, VDR-U15-C336, VDR-U15-C337, VDR-U15-C354

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
