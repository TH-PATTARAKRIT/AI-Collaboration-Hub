# Atomic Handoff Packet — U06

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U06` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `e0a987bc17ccc7e0c0d3131c470843ad0e8ccec1` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=339 supported_pointer_and_anchor=333 unknown_class=6 neutral_ids=186` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U06_purchase_order.md` | `6b3c16228207e431898d7c784be80c9d41dc7b7793aa110d519db3114205eecf` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U06_purchase_order_NEUTRAL.md` | `b10230474387470817445657be7f2dd6337138b238be9f1c1488d62e39aadbef` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 339 (FACT 285 · OBSERVATION 11 · INFERENCE 37 · UNKNOWN 6) |
| Neutral statements | 186 |
| Contradiction (CONTRA) claims | 3 |
| Runtime/AWT-required (RT) claims | 18 |
| Claims bound to an existing C1 Function-ID | 7 (distinct C1 IDs: GRV-F06, PDT-F02, PDT-F03) |
| Claims with an existing Function-ID | 7; `FUNCTION MAPPING REQUIRED`: 332 |
| Existing Function-IDs referenced | GRV-F06×5, PDT-F02×1, PDT-F03×1 |

## Capabilities in scope
- CAP-U06-01 RFQ / PO state machine (draft / sent / to approve / purchase / cancel, plus lock)
- CAP-U06-02 Confirmation and approval (double validation)
- CAP-U06-03 Cancellation, reset to draft, unlock / lock
- CAP-U06-04 Vendor pricing and supplier info
- CAP-U06-05 Vendor bill generation and control
- CAP-U06-06 Line rules and amounts
- CAP-U06-07 Reminders and schedulers
- CAP-U06-08 Purchase agreements (purchase_requisition)
- CAP-U06-09 Roles and security
- CAP-U06-10 Multi-company / data scope and exception behaviour

## Contradiction claim ids
VDR-U06-C001, VDR-U06-C024, VDR-U06-C235

## Runtime-required claim ids
VDR-U06-C011, VDR-U06-C031, VDR-U06-C032, VDR-U06-C056, VDR-U06-C079, VDR-U06-C089, VDR-U06-C165, VDR-U06-C172, VDR-U06-C207, VDR-U06-C214, VDR-U06-C216, VDR-U06-C226, VDR-U06-C269, VDR-U06-C272, VDR-U06-C309, VDR-U06-C316, VDR-U06-C321, VDR-U06-C332

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
