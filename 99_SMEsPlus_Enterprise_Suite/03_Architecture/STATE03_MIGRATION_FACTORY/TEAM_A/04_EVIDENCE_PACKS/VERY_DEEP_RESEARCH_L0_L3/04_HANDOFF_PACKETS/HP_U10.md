# Atomic Handoff Packet — U10

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U10` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4a4f39cfae874bd65cdcc9a6a5c8b7e17dfafd79` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=365 supported_pointer_and_anchor=360 unknown_class=5 neutral_ids=180` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U10_stock_valuation.md` | `0a5ca7b670e71d746a6f8d5ab2731b40355675248ea302e127f858fdc109af53` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U10_stock_valuation_NEUTRAL.md` | `4ab114a269ed2aa9d1155ba9811fce1b5f9081fa507c5782b21d538b404dafa9` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 365 (FACT 326 · OBSERVATION 11 · INFERENCE 23 · UNKNOWN 5) |
| Neutral statements | 180 |
| Contradiction (CONTRA) claims | 7 |
| Runtime/AWT-required (RT) claims | 13 |
| Claims bound to an existing C1 Function-ID | 140 (distinct C1 IDs: GRV-F04, GRV-F05, IAV-F03, IAV-F04, PCO-F03, PDT-F02, SDV-F05, SDV-F07) |
| Claims with an existing Function-ID | 145; `FUNCTION MAPPING REQUIRED`: 220 |
| Existing Function-IDs referenced | GRV-F04×13, GRV-F05×52, GRV-F07×2, IAV-F03×6, IAV-F04×4, PCO-F03×40, PDT-F02×8, SDV-F05×13, SDV-F06×3, SDV-F07×4 |

## Capabilities in scope
- CAP-U10-01 Where and how stock value and cost are stored, and the costing methods
- CAP-U10-02 Valuation mode switch (periodic versus perpetual) and the accounting-style flag
- CAP-U10-03 Accounting entries at receipt and delivery, billing timing and returns
- CAP-U10-04 Inventory valuation closing at period end
- CAP-U10-05 Landed costs
- CAP-U10-06 Cost changes, revaluation and adjustment or scrap valuation hooks
- CAP-U10-07 Valuation reports and accounting properties
- CAP-U10-08 Roles, record rules, multi-company scope, constraints and configuration check
- CAP-U10-09 Cross-module trigger map into valuation

## Contradiction claim ids
VDR-U10-C005, VDR-U10-C006, VDR-U10-C007, VDR-U10-C012, VDR-U10-C099, VDR-U10-C107, VDR-U10-C264

## Runtime-required claim ids
VDR-U10-C066, VDR-U10-C098, VDR-U10-C101, VDR-U10-C103, VDR-U10-C107, VDR-U10-C149, VDR-U10-C154, VDR-U10-C155, VDR-U10-C164, VDR-U10-C194, VDR-U10-C195, VDR-U10-C241, VDR-U10-C292

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
