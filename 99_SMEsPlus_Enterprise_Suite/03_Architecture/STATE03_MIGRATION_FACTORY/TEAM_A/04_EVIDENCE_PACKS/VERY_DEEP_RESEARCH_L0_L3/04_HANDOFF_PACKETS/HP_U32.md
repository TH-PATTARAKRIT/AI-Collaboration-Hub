# Atomic Handoff Packet — U32

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U32` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4d17ae852ab6883b81ff44f374c99f984a42737e` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=225 supported_pointer_and_anchor=214 unknown_class=12 neutral_ids=114` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U32_taxed_flows_other_paths.md` | `6489625cf62ca2d1857b12772764289269a6e86b08a411f5634458e309be323e` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U32_taxed_flows_other_paths_NEUTRAL.md` | `ccf679065b9d04db207cb6e24489b5fe1c884211df0232b619daabe919b15746` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 225 (FACT 176 · OBSERVATION 12 · INFERENCE 25 · UNKNOWN 12) |
| Neutral statements | 114 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 26 |
| Claims bound to an existing C1 Function-ID | 14 (distinct C1 IDs: GRV-F05, PCO-F01) |
| Claims with an existing Function-ID | 16; `FUNCTION MAPPING REQUIRED`: 209 |
| Existing Function-IDs referenced | GRV-F05×13, MFG-F03×2, PCO-F01×1 |

## Capabilities in scope
- CAP-U32-01 Bank statement lines and reconcile models that can add taxed lines
- CAP-U32-02 Employee expense taxes (computation, receipts, company-paid entries, re-invoicing)
- CAP-U32-03 Landed costs, manufacturing and subcontracting entries and their tax interaction
- CAP-U32-04 Electronic-invoice tax hooks (category, exemption, how Thai taxes map, amount checks, import)
- CAP-U32-05 Discount, loyalty reward, delivery, product-matrix and margin lines: tax effects
- CAP-U32-06 Down-payment lines: tax effects
- CAP-U32-07 Early-payment discount tax-base redistribution with several taxes
- CAP-U32-08 Fiscal-position and partner-driven tax mapping at order, purchase, bill and expense hand-offs
- CAP-U32-09 Optional tax add-ons not installed: calculation and entry-effect depth (formula tax, withholding on payment, tag update, debit note, VAT validation)
- CAP-U32-10 Other entry generators that carry no tax: cut-off, accrual and price-difference lines

## Contradiction claim ids
VDR-U32-C146

## Runtime-required claim ids
VDR-U32-C006, VDR-U32-C024, VDR-U32-C027, VDR-U32-C044, VDR-U32-C059, VDR-U32-C083, VDR-U32-C094, VDR-U32-C100, VDR-U32-C110, VDR-U32-C114, VDR-U32-C125, VDR-U32-C127, VDR-U32-C143, VDR-U32-C154, VDR-U32-C155, VDR-U32-C166, VDR-U32-C175, VDR-U32-C184, VDR-U32-C198, VDR-U32-C202, VDR-U32-C207, VDR-U32-C213, VDR-U32-C217, VDR-U32-C218, VDR-U32-C219, VDR-U32-C225

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
