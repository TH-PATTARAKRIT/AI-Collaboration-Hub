# Atomic Handoff Packet — U36

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U36` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `75e9c22ae66a93bf08872de7c8672eecd6fc2529` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=349 supported_pointer_and_anchor=339 unknown_class=11 neutral_ids=152` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U36_base_remaining.md` | `e40c783ddc92ad5988f708a7fcff1802cc131843ad99aef745b19a18d60e4cfd` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U36_base_remaining_NEUTRAL.md` | `e11e39ab3129cbcec61a16922214f06f89373970dd878ac7e25b4722987d925a` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 349 (FACT 312 · OBSERVATION 22 · INFERENCE 4 · UNKNOWN 11) |
| Neutral statements | 152 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 14 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 349 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U36-01 Application registry and lifecycle
- CAP-U36-02 View definition, inheritance and validation
- CAP-U36-03 Template engine and asset bundles
- CAP-U36-04 Request handling, authentication modes and binary content
- CAP-U36-05 Report actions and document rendering
- CAP-U36-06 Outgoing mail servers
- CAP-U36-07 Saved filters, export templates, embedded actions and language exchange
- CAP-U36-08 Actions, wizards and menus
- CAP-U36-09 Countries, languages, banks and contact classification
- CAP-U36-10 Metadata registry and platform support

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U36-C190, VDR-U36-C222, VDR-U36-C290, VDR-U36-C339, VDR-U36-C340, VDR-U36-C341, VDR-U36-C342, VDR-U36-C343, VDR-U36-C344, VDR-U36-C345, VDR-U36-C346, VDR-U36-C347, VDR-U36-C348, VDR-U36-C349

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
