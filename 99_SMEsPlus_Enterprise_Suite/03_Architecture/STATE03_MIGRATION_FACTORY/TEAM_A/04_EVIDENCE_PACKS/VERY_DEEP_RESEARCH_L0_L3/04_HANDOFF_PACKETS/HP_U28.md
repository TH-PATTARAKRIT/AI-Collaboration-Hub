# Atomic Handoff Packet — U28

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U28` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `c094725d74bd0e40199829796ec2bd00c8bdd0a7` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=296 supported_pointer_and_anchor=281 unknown_class=15 neutral_ids=139` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U28_thai_entity_structures.md` | `2813432c7b27e3a6847d54219987f090d8c234c5a3b2e70bf71861960f29a2b3` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U28_thai_entity_structures_NEUTRAL.md` | `d469671c77539f853d0de7258ad8a750d5f68c9a2ce1e511ca3b61518072b653` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 296 (FACT 250 · OBSERVATION 11 · INFERENCE 20 · UNKNOWN 15) |
| Neutral statements | 139 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 25 |
| Claims bound to an existing C1 Function-ID | 66 (distinct C1 IDs: MCT-F02, PCO-F01) |
| Claims with an existing Function-ID | 103; `FUNCTION MAPPING REQUIRED`: 193 |
| Existing Function-IDs referenced | MCT-F02×62, MCT-F03×12, MCT-F04×25, PCO-F01×4 |

## Capabilities in scope
- CAP-U28-01 Company and legal-entity model (hierarchy, branch semantics, entity-type mapping)
- CAP-U28-02 Tax identity and branch identification (company and partner)
- CAP-U28-03 Foreign ownership and group relationships
- CAP-U28-04 Inter-company flows (payment clearing, stock transit, valuation)
- CAP-U28-05 Reporting and consolidation across entities
- CAP-U28-06 Statutory documents, entity numbering and identity on documents (Thailand)
- CAP-U28-07 Company-to-jurisdiction assignment for the foreign-group structures
- CAP-U28-08 Roles, record rules and audit across entities

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U28-C023, VDR-U28-C024, VDR-U28-C034, VDR-U28-C035, VDR-U28-C036, VDR-U28-C037, VDR-U28-C071, VDR-U28-C076, VDR-U28-C093, VDR-U28-C097, VDR-U28-C117, VDR-U28-C141, VDR-U28-C143, VDR-U28-C145, VDR-U28-C146, VDR-U28-C165, VDR-U28-C180, VDR-U28-C207, VDR-U28-C208, VDR-U28-C234, VDR-U28-C246, VDR-U28-C253, VDR-U28-C269, VDR-U28-C273, VDR-U28-C295

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
