# Atomic Handoff Packet — U07

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U07` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `03a764e23aaf4fa35ec7dc78b06323d4ba7b551d` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=373 supported_pointer_and_anchor=365 unknown_class=9 neutral_ids=157` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U07_purchase_receiving.md` | `0e9069fac023333101abb9ce84513218c3388766c2010c4ad079291ed831739e` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U07_purchase_receiving_NEUTRAL.md` | `b1a9f4bdedc63783d9f5ce68ab12dcac7ad872ea814e4a96c7898c3bc0b36780` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 373 (FACT 323 · OBSERVATION 14 · INFERENCE 27 · UNKNOWN 9) |
| Neutral statements | 157 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 14 |
| Claims bound to an existing C1 Function-ID | 72 (distinct C1 IDs: GRV-F04, GRV-F05, PDT-F02, PDT-F03) |
| Claims with an existing Function-ID | 271; `FUNCTION MAPPING REQUIRED`: 102 |
| Existing Function-IDs referenced | BRP-F06×63, GRV-F01×53, GRV-F02×18, GRV-F03×39, GRV-F04×39, GRV-F05×7, GRV-F07×25, PDT-F02×5, PDT-F03×21, PDT-F04×1 |

## Capabilities in scope
- CAP-U07-01 Receipt creation from a purchase order
- CAP-U07-02 Received quantity and purchase line status
- CAP-U07-03 Bill-before-receipt, over-receipt and under-receipt situations
- CAP-U07-04 Returns of received goods and refund hand-off
- CAP-U07-05 Valuation and price-difference behaviour attributable to purchase_stock
- CAP-U07-06 Replenishment link: buy route, reordering rules to RFQ
- CAP-U07-07 Dropship and cross-document links (requisition, MRP, repair)
- CAP-U07-08 Roles, record rules, multi-company scope, scheduled behaviour, exceptions

## Contradiction claim ids
VDR-U07-C065, VDR-U07-C129

## Runtime-required claim ids
VDR-U07-C036, VDR-U07-C038, VDR-U07-C066, VDR-U07-C111, VDR-U07-C130, VDR-U07-C132, VDR-U07-C133, VDR-U07-C161, VDR-U07-C162, VDR-U07-C207, VDR-U07-C271, VDR-U07-C300, VDR-U07-C332, VDR-U07-C373

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
