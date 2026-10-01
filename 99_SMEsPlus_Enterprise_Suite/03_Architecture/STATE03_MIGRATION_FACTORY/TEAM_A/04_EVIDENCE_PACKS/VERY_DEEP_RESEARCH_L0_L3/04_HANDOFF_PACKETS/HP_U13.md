# Atomic Handoff Packet — U13

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U13` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `c348a8c908cd07ac04a16c4f185024bcc3a5c650` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=484 supported_pointer_and_anchor=475 unknown_class=9 neutral_ids=201` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U13_account_tax_chart_localization.md` | `c9785886dc2df59601ef7d0bceb763a51da0045ce3d8f28ab1ef67e7ef956717` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U13_account_tax_chart_localization_NEUTRAL.md` | `fda65f39bfaee900781d350e478f8ca6b1c9bc22aaccbb85ba0d2e113dd89485` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 484 (FACT 436 · OBSERVATION 22 · INFERENCE 17 · UNKNOWN 9) |
| Neutral statements | 201 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 12 |
| Claims bound to an existing C1 Function-ID | 6 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 29; `FUNCTION MAPPING REQUIRED`: 455 |
| Existing Function-IDs referenced | MCT-F03×10, PCO-F01×6, PCO-F02×13 |

## Capabilities in scope
- CAP-U13-01 Tax computation engine
- CAP-U13-02 Fiscal positions and tax/account mapping
- CAP-U13-03 Chart of accounts, account types, guards, company chart loading
- CAP-U13-04 Currencies in accounting and cash rounding
- CAP-U13-05 Accounting company settings and period configuration
- CAP-U13-06 Partner accounting properties and defaults
- CAP-U13-07 Analytic distribution on journal items (account side)
- CAP-U13-08 Thai localization (`l10n_th`) — Community only
- CAP-U13-09 E-invoicing, payment QR and location number
- CAP-U13-10 Roles, record rules, ACL, data scope, exceptions, scheduled jobs

## Contradiction claim ids
VDR-U13-C217, VDR-U13-C368

## Runtime-required claim ids
VDR-U13-C088, VDR-U13-C131, VDR-U13-C184, VDR-U13-C218, VDR-U13-C259, VDR-U13-C296, VDR-U13-C297, VDR-U13-C333, VDR-U13-C351, VDR-U13-C454, VDR-U13-C455, VDR-U13-C484

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
