# Atomic Handoff Packet — U29

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U29` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `a27ef573801f7c340f1b16382f924050ace10ac6` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=410 supported_pointer_and_anchor=410 unknown_class=13 neutral_ids=232` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U29_residual_bridges.md` | `96628e08925d03dfdaa9a336162e2b90358968ab0a0d8880bca7295f9cbf6dac` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U29_residual_bridges_NEUTRAL.md` | `03328ae4029d995be618abe671c1441d59f795e44e1ad428ffd187edc38fc66c` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 410 (FACT 357 · OBSERVATION 17 · INFERENCE 23 · UNKNOWN 13) |
| Neutral statements | 232 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 19 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 410 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U29-01 Sales margin on bundled (kit) products - cost bridge
- CAP-U29-02 Expiry-aware stock forecast on sales order lines
- CAP-U29-03 Transport dispatch on batch transfers (vehicle, driver, dock, capacity)
- CAP-U29-04 Visitor and event-attendee SMS contact bridges
- CAP-U29-05 SMS marketing campaign bridges (split-test winner metrics, SMS newsletter subscription)
- CAP-U29-06 Website bridges: portal timesheet visibility switch and public mail-group subscription block
- CAP-U29-07 Course certifications (survey-based certification slides in e-learning)
- CAP-U29-08 Management dashboards (events, expenses, project tasks, timesheets, live chat, warehouse metrics)
- CAP-U29-09 Builder, email theme and social-account bridges

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U29-C046, VDR-U29-C047, VDR-U29-C056, VDR-U29-C072, VDR-U29-C119, VDR-U29-C141, VDR-U29-C154, VDR-U29-C198, VDR-U29-C199, VDR-U29-C241, VDR-U29-C242, VDR-U29-C278, VDR-U29-C306, VDR-U29-C307, VDR-U29-C366, VDR-U29-C367, VDR-U29-C368, VDR-U29-C408, VDR-U29-C409

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
