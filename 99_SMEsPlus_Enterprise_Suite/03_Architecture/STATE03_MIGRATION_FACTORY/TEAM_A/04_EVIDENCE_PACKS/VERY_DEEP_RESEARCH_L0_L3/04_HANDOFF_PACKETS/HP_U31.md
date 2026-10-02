# Atomic Handoff Packet — U31

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U31` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `312243328b17e2b741bf597f699b7ee67ff79744` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=270 supported_pointer_and_anchor=256 unknown_class=14 neutral_ids=135` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U31_tax_report_engine_tags.md` | `36b1c9aa8ccc595492c06178461fa75367e08f775c70a80a07e9c146f8eb2ed6` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U31_tax_report_engine_tags_NEUTRAL.md` | `b62a31aba9f73135dbb5497609df1df5720f13bcfd870041ecc87ece5fabb564` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 270 (FACT 203 · OBSERVATION 21 · INFERENCE 32 · UNKNOWN 14) |
| Neutral statements | 135 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 21 |
| Claims bound to an existing C1 Function-ID | 7 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 14; `FUNCTION MAPPING REQUIRED`: 256 |
| Existing Function-IDs referenced | PCO-F01×7, PCO-F02×7 |

## Capabilities in scope
- CAP-U31-01 Report definition structure
- CAP-U31-02 Computation methods a report line can declare
- CAP-U31-03 Running, displaying, exporting and filing a report (entry points and what is absent)
- CAP-U31-04 Thai VAT and withholding report definitions as supplied
- CAP-U31-05 Provisioning, naming and country scope of tax grid tags
- CAP-U31-06 Applying tax grid tags to journal items (documents, credit notes, entries, reversals)
- CAP-U31-07 Cash-basis exigibility and its tags
- CAP-U31-08 Re-applying tags to existing journal items
- CAP-U31-09 Tax closing flag, return periods, date scope and carry-over
- CAP-U31-10 Access control, company scope and audit of report and tag data

## Contradiction claim ids
VDR-U31-C101

## Runtime-required claim ids
VDR-U31-C063, VDR-U31-C086, VDR-U31-C088, VDR-U31-C105, VDR-U31-C106, VDR-U31-C143, VDR-U31-C144, VDR-U31-C166, VDR-U31-C179, VDR-U31-C182, VDR-U31-C199, VDR-U31-C201, VDR-U31-C215, VDR-U31-C216, VDR-U31-C217, VDR-U31-C218, VDR-U31-C245, VDR-U31-C246, VDR-U31-C263, VDR-U31-C266, VDR-U31-C269

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
