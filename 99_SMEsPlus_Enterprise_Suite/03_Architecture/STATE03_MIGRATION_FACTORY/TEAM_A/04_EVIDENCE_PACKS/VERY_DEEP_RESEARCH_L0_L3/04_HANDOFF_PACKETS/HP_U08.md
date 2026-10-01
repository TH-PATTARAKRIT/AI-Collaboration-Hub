# Atomic Handoff Packet — U08

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U08` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `c81735867b1407b714e164555b1e474ef3f949e5` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=597 supported_pointer_and_anchor=588 unknown_class=10 neutral_ids=227` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U08_stock_transfers.md` | `3bc3b83afdfe5337d85a9889f8cdf45dcbe54bd5172785b54264eb73fd8f56ad` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U08_stock_transfers_NEUTRAL.md` | `3dc626346ca778f811dbfe08ae592b2b1551d43cb38ea2000a68498028bf9c46` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 597 (FACT 543 · OBSERVATION 22 · INFERENCE 22 · UNKNOWN 10) |
| Neutral statements | 227 |
| Contradiction (CONTRA) claims | 6 |
| Runtime/AWT-required (RT) claims | 15 |
| Claims bound to an existing C1 Function-ID | 3 (distinct C1 IDs: MCT-F01, MCT-F05) |
| Claims with an existing Function-ID | 191; `FUNCTION MAPPING REQUIRED`: 406 |
| Existing Function-IDs referenced | BRP-F06×30, GRV-F01×48, GRV-F02×45, GRV-F03×19, GRV-F07×40, MCT-F01×2, MCT-F05×1, SDV-F01×47, SDV-F02×45, SDV-F03×19, SDV-F06×40 |

## Capabilities in scope
- CAP-U08-01 Warehouse and routing configuration
- CAP-U08-02 Transfer (picking) and movement state machine
- CAP-U08-03 Reservation and availability
- CAP-U08-04 Validation (done) of a transfer, backorders and over-processing
- CAP-U08-05 Returns and reverse transfers
- CAP-U08-06 Cancellation, unreserve, edit restrictions after done, and date/lead-time propagation
- CAP-U08-07 Procurement, scheduler and replenishment
- CAP-U08-08 Operation types, sequences/naming, default locations, location types, removal strategies
- CAP-U08-09 Batch transfers, carriers & shipping, drop-shipping
- CAP-U08-10 Roles, record rules and multi-company / warehouse scope

## Contradiction claim ids
VDR-U08-C173, VDR-U08-C232, VDR-U08-C337, VDR-U08-C514, VDR-U08-C574, VDR-U08-C582

## Runtime-required claim ids
VDR-U08-C055, VDR-U08-C104, VDR-U08-C106, VDR-U08-C166, VDR-U08-C169, VDR-U08-C201, VDR-U08-C231, VDR-U08-C269, VDR-U08-C272, VDR-U08-C273, VDR-U08-C332, VDR-U08-C387, VDR-U08-C440, VDR-U08-C541, VDR-U08-C597

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
