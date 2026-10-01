# Atomic Handoff Packet — U24

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U24` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `60f40461290326b5a60108327c9ad81efa1db87d` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=260 supported_pointer_and_anchor=242 unknown_class=18 neutral_ids=136` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U24_thailand_localization.md` | `692e3bc89b16c2a9270677784a6730f36f573f5e67d12cb92a02db9f8e5d3b17` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U24_thailand_localization_NEUTRAL.md` | `597a970befd2d8ac0d1edbddf2665e10cd37ddebce9621def5debfe785d3200e` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 260 (FACT 188 · OBSERVATION 20 · INFERENCE 34 · UNKNOWN 18) |
| Neutral statements | 136 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 12 |
| Claims bound to an existing C1 Function-ID | 5 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 20; `FUNCTION MAPPING REQUIRED`: 240 |
| Existing Function-IDs referenced | MCT-F03×5, PCO-F01×5, PCO-F02×10 |

## Capabilities in scope
- CAP-U24-01 Thai chart of accounts structure and loading
- CAP-U24-02 Thai VAT: taxes, tags, accounts and standard sale and purchase entries
- CAP-U24-03 Withholding tax in the Thai tax set
- CAP-U24-04 Tax invoice, receipt, credit note and debit note documents
- CAP-U24-05 Thai partner identity (tax ID, branch) and address
- CAP-U24-06 Payments, PromptPay/EMV QR and bank/journal setup
- CAP-U24-07 Period, lock and fiscal-year behaviour
- CAP-U24-08 Thai statutory-output gaps (not present in Community)
- CAP-U24-09 Country-pack boundary and cross-border touchpoints

## Contradiction claim ids
VDR-U24-C130

## Runtime-required claim ids
VDR-U24-C005, VDR-U24-C064, VDR-U24-C076, VDR-U24-C079, VDR-U24-C092, VDR-U24-C132, VDR-U24-C138, VDR-U24-C156, VDR-U24-C171, VDR-U24-C195, VDR-U24-C207, VDR-U24-C213

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
