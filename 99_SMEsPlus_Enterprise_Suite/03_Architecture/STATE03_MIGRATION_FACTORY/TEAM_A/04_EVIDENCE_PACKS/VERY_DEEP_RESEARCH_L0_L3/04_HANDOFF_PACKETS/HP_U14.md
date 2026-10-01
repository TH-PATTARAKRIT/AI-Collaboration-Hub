# Atomic Handoff Packet — U14

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U14` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `6b7cf4e1c5800fce34f40d3cf221005d36995900` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=536 supported_pointer_and_anchor=525 unknown_class=11 neutral_ids=197` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U14_mrp_core.md` | `b90ca7ce5b59cddfbe2dbbf80c892d45bc82221c8378ac012a4ab6ee32efb738` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U14_mrp_core_NEUTRAL.md` | `b463bde8dfdfc2ea0c01ad2dba95e8428aa8dda30011f9eaf3af18f95ea8f54d` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 536 (FACT 475 · OBSERVATION 28 · INFERENCE 22 · UNKNOWN 11) |
| Neutral statements | 197 |
| Contradiction (CONTRA) claims | 8 |
| Runtime/AWT-required (RT) claims | 19 |
| Claims bound to an existing C1 Function-ID | 27 (distinct C1 IDs: BRP-F01, BRP-F03, BRP-F08, MFG-F01, MFG-F02) |
| Claims with an existing Function-ID | 127; `FUNCTION MAPPING REQUIRED`: 409 |
| Existing Function-IDs referenced | BRP-F01×3, BRP-F02×14, BRP-F03×2, BRP-F04×13, BRP-F05×31, BRP-F06×15, BRP-F07×4, BRP-F08×13, BRP-F09×3, MFG-F01×6, MFG-F02×3, MFG-F03×6, MFG-F04×14 |

## Capabilities in scope
- CAP-U14-01 Bill of materials (BoM) definition, kinds, lookup and kit expansion
- CAP-U14-02 Work centers, BoM operations (routing) and productivity-loss master data
- CAP-U14-03 Manufacturing order (MO) creation, quantity change, confirmation, lifecycle state and cancellation (incl. project link)
- CAP-U14-04 Component reservation, MO readiness and 1/2/3-step manufacturing routing
- CAP-U14-05 Consumption of components, production recording (lots/serials), consumption policy, expiry check and completion ("Mark as Done")
- CAP-U14-06 Backorders, splitting and merging of manufacturing orders
- CAP-U14-07 Work-order generation, execution (start/pause/finish) and planning/scheduling on work-center calendars
- CAP-U14-08 Scrap from manufacturing orders / work orders, and Unbuild orders
- CAP-U14-09 Replenishment and planning for manufacturing (manufacture rule, reordering rules with BoM, MTO for manufacture, lead times, kit procurement)
- CAP-U14-10 Manufacturing cost fields (work center / operation / work order / by-product share) and cost reports; verification of MFG-F01..F04

## Contradiction claim ids
VDR-U14-C002, VDR-U14-C037, VDR-U14-C077, VDR-U14-C469, VDR-U14-C470, VDR-U14-C471, VDR-U14-C493, VDR-U14-C499

## Runtime-required claim ids
VDR-U14-C073, VDR-U14-C117, VDR-U14-C185, VDR-U14-C192, VDR-U14-C231, VDR-U14-C232, VDR-U14-C258, VDR-U14-C285, VDR-U14-C295, VDR-U14-C335, VDR-U14-C336, VDR-U14-C388, VDR-U14-C390, VDR-U14-C422, VDR-U14-C432, VDR-U14-C477, VDR-U14-C514, VDR-U14-C534, VDR-U14-C536

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
