# Atomic Handoff Packet — TXC

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `TXC` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `ef6c4a3b9cb42df856f7c673ad907276e3ef17b8` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=562 supported_pointer_and_anchor=555 unknown_class=7 neutral_ids=84` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/TXC_thaitax_schema_dump_reconciliation.md` | `13e7e298b8205f93b0873e646ba3051d6494bc1b48c6083f7e6c11d88efa0c95` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/TXC_thaitax_schema_dump_reconciliation_NEUTRAL.md` | `787e8bd6df78a2d66f8edd6d42a9b2bf1810d8a771f68ed6f2520017431aaa32` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 562 (FACT 49 · OBSERVATION 488 · INFERENCE 18 · UNKNOWN 7) |
| Neutral statements | 84 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 23 |
| Claims bound to an existing C1 Function-ID | 14 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 14; `FUNCTION MAPPING REQUIRED`: 548 |
| Existing Function-IDs referenced | PCO-F01×14 |

## Capabilities in scope
- CAP-TXC-01 Tax definition and classification data
- CAP-TXC-02 Tax return and report definition structure
- CAP-TXC-03 Fiscal position and mapping data
- CAP-TXC-04 Journal entry, entry line, reconciliation and journal tax and currency data
- CAP-TXC-05 Accounts and payments including withholding-related columns
- CAP-TXC-06 Partner, company, product, country and currency tax configuration, with lock dates
- CAP-TXC-07 Order, purchase, expense and stock line tax and currency columns
- CAP-TXC-08 Thai localisation additions and seeded Thai tax configuration
- CAP-TXC-09 Constraint, index, key and relation-table reconciliation
- CAP-TXC-10 Optional tax-path source not present in this database

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-TXC-C095, VDR-TXC-C097, VDR-TXC-C098, VDR-TXC-C099, VDR-TXC-C100, VDR-TXC-C101, VDR-TXC-C207, VDR-TXC-C226, VDR-TXC-C325, VDR-TXC-C326, VDR-TXC-C328, VDR-TXC-C329, VDR-TXC-C337, VDR-TXC-C343, VDR-TXC-C401, VDR-TXC-C402, VDR-TXC-C403, VDR-TXC-C411, VDR-TXC-C548, VDR-TXC-C549, VDR-TXC-C550, VDR-TXC-C551, VDR-TXC-C552

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
