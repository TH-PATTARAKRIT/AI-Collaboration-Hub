# Atomic Handoff Packet — U09

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U09` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `072a94c6e1001bca274b41de660be15b5574d5a5` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=333 supported_pointer_and_anchor=333 unknown_class=9 neutral_ids=172` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U09_stock_quants_lots_adjustments.md` | `36ad119c89d55406e0fbedc75fbc68c2cd34dff41b10e984f350e62579857955` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U09_stock_quants_lots_adjustments_NEUTRAL.md` | `8d46bf09dddba92239da5b24f29e98e313fb12ff10e46c916368664cda9d24eb` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 333 (FACT 279 · OBSERVATION 23 · INFERENCE 22 · UNKNOWN 9) |
| Neutral statements | 172 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 24 (distinct C1 IDs: IAV-F03, IAV-F04) |
| Claims with an existing Function-ID | 147; `FUNCTION MAPPING REQUIRED`: 186 |
| Existing Function-IDs referenced | IAV-F01×19, IAV-F02×28, IAV-F03×14, IAV-F04×10, IAV-F05×19, IAV-F06×21, RCN-F01×36 |

## Capabilities in scope
- CAP-U09-01 Quant model and quantity integrity
- CAP-U09-02 Inventory counting and adjustment application
- CAP-U09-03 Cycle counts and scheduling
- CAP-U09-04 Reversal and correction of an applied adjustment
- CAP-U09-05 Financial hooks of adjustments and scrap
- CAP-U09-06 Lots, serial numbers and tracking
- CAP-U09-07 Packages and package types
- CAP-U09-08 Scrap
- CAP-U09-09 Stock quantity computations and history views
- CAP-U09-10 Roles, record rules, ACL, scheduled behaviour and failure paths

## Contradiction claim ids
VDR-U09-C100, VDR-U09-C144

## Runtime-required claim ids
VDR-U09-C021, VDR-U09-C023, VDR-U09-C029, VDR-U09-C091, VDR-U09-C093, VDR-U09-C094, VDR-U09-C110, VDR-U09-C126, VDR-U09-C145, VDR-U09-C188, VDR-U09-C215, VDR-U09-C228, VDR-U09-C243, VDR-U09-C275, VDR-U09-C298, VDR-U09-C332

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
