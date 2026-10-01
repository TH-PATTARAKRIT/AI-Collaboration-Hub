# Atomic Handoff Packet — U27

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U27` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `e357e8f2bc9e2517e99ff6640a7e32257e057fd3` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=285 supported_pointer_and_anchor=278 unknown_class=7 neutral_ids=118` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U27_localization_framework.md` | `df3a61a215c19ee5c240386c6b70cb96c84766bff22bc7f88c18c4553bbb9baf` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U27_localization_framework_NEUTRAL.md` | `eb8f8a1cd69d84e647463894c45b68d070bb95a2f4b7a7315c5c29cec36c0142` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 285 (FACT 245 · OBSERVATION 7 · INFERENCE 26 · UNKNOWN 7) |
| Neutral statements | 118 |
| Contradiction (CONTRA) claims | 3 |
| Runtime/AWT-required (RT) claims | 25 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 3; `FUNCTION MAPPING REQUIRED`: 282 |
| Existing Function-IDs referenced | MCT-F03×3 |

## Capabilities in scope
- CAP-U27-01 Jurisdiction assignment of a company
- CAP-U27-02 Country-neutral accounting core boundary
- CAP-U27-03 Localization framework mechanisms
- CAP-U27-04 Country-pack lifecycle
- CAP-U27-05 Extension-boundary taxonomy of packs (FUTURE OPTIONAL COUNTRY PACK facts)
- CAP-U27-06 Multi-jurisdiction coexistence in one database
- CAP-U27-07 Gaps and design-relevant observations

## Contradiction claim ids
VDR-U27-C202, VDR-U27-C220, VDR-U27-C225

## Runtime-required claim ids
VDR-U27-C062, VDR-U27-C165, VDR-U27-C184, VDR-U27-C231, VDR-U27-C232, VDR-U27-C233, VDR-U27-C234, VDR-U27-C235, VDR-U27-C237, VDR-U27-C238, VDR-U27-C239, VDR-U27-C242, VDR-U27-C243, VDR-U27-C244, VDR-U27-C246, VDR-U27-C247, VDR-U27-C253, VDR-U27-C262, VDR-U27-C264, VDR-U27-C265, VDR-U27-C267, VDR-U27-C270, VDR-U27-C272, VDR-U27-C275, VDR-U27-C281

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
