# Atomic Handoff Packet — U48

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U48` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4fca9a25525324a2e8fb1d40fc4f8d6ee467900d` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=121 supported_pointer_and_anchor=121 unknown_class=0 neutral_ids=20` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U48_account_edi_ubl_cii.md` | `0e305511ca7f092831546fc2493f64e162600715b255702405b41c42481a2d24` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U48_account_edi_ubl_cii_NEUTRAL.md` | `b4456e31b40e7c46ab1f56151fd19b13ad942ee484d001f770a94c814d88a6f9` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 121 (FACT 121 · OBSERVATION 0 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 20 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 0 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 121; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U48-01 GLN (Global Location Number) on Partner
- CAP-U48-02 UBL/CII Module Architecture and Inheritance Chain
- CAP-U48-03 UBL 2.0/2.1 Export — Document Structure and Node Building
- CAP-U48-04 UBL Field-Level Mappings — Header Level
- CAP-U48-05 UBL Field-Level Mappings — Party Level
- CAP-U48-06 UBL Field-Level Mappings — Tax Level
- CAP-U48-07 UBL Field-Level Mappings — Line Level
- CAP-U48-08 CII (Factur-X / ZUGFeRD) Format Architecture
- CAP-U48-09 BIS 3 / Peppol Profile Architecture
- CAP-U48-10 Import (Inbound EDI) Flow
- CAP-U48-11 Thailand-Scope Analysis

## Contradiction claim ids
none

## Runtime-required claim ids
none

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
