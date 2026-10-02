# Atomic Handoff Packet — U62

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U62` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `0fff4d5bf81fb845efbbd2c34cf74da491c55f03` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=152 supported_pointer_and_anchor=152 unknown_class=0 neutral_ids=44` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U62_peppol_iot_lunch_mailing_payment_providers.md` | `67003b66928e793d7dfec52a5e777cc3360fee61eaeb16a79d666dbe6586bf1a` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U62_peppol_iot_lunch_mailing_payment_providers_NEUTRAL.md` | `b8eee11a6885194a0bf0177b98e55f7d301b71bf669f71f2b3b19744ba6cc99a` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 152 (FACT 150 · OBSERVATION 2 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 44 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 2 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 152; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U62-01 PEPPOL Registration and Proxy State Management
- CAP-U62-02 PEPPOL Document Sending and Receiving
- CAP-U62-03 PEPPOL Partner Verification
- CAP-U62-04 PEPPOL Advanced Fields (account_peppol_advanced_fields)
- CAP-U62-05 SEPA QR Code (account_qr_code_sepa)
- CAP-U62-06 Data Recycle (data_recycle)
- CAP-U62-07 IoT Base (iot_base)
- CAP-U62-08 UBL/CII Test Helpers (l10n_account_edi_ubl_cii_tests)
- CAP-U62-09 Withholding Tax at POS — Thailand CRITICAL (l10n_account_withholding_tax_pos)
- CAP-U62-10 Lunch Module
- CAP-U62-11 Marketing Card (marketing_card)
- CAP-U62-12 Mass Mailing Core (mass_mailing)
- CAP-U62-13 Mass Mailing Bridge Modules
- CAP-U62-14 Payment Provider — Adyen
- CAP-U62-15 Payment Provider — Amazon Payment Services (payment_aps)
- CAP-U62-16 Payment Provider — AsiaPay
- CAP-U62-17 Payment Provider — Authorize.Net
- CAP-U62-18 Payment Provider — Buckaroo
- CAP-U62-19 Payment Provider — Demo (payment_demo)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U62-C125, VDR-U62-C126

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
