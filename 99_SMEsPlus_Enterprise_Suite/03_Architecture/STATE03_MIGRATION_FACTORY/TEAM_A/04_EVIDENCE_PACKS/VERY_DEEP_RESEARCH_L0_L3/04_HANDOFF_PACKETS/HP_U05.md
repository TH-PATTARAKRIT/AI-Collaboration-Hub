# Atomic Handoff Packet — U05

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U05` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `9d1b9bf96b63a995af5e7ea1a4f93a6f37f82e6b` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=477 supported_pointer_and_anchor=477 unknown_class=13 neutral_ids=258` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U05_sales_invoicing_delivery.md` | `b2180d631d7965c7f4d3797e4bb4177901c2d245939e235270e77ce8184ba302` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U05_sales_invoicing_delivery_NEUTRAL.md` | `648eddd4d538ed0cfbc3ac6188fa9e40cf9891edae0dec8f1dc4c5ee58adb8d0` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 477 (FACT 414 · OBSERVATION 17 · INFERENCE 33 · UNKNOWN 13) |
| Neutral statements | 258 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 14 |
| Claims bound to an existing C1 Function-ID | 81 (distinct C1 IDs: PDT-F01, SDV-F04, SDV-F07) |
| Claims with an existing Function-ID | 180; `FUNCTION MAPPING REQUIRED`: 297 |
| Existing Function-IDs referenced | PDT-F01×12, PDT-F04×24, SDV-F01×36, SDV-F02×17, SDV-F03×9, SDV-F04×37, SDV-F06×13, SDV-F07×32 |

## Capabilities in scope
- CAP-U05-01 Invoicing policy (ordered vs delivered quantities)
- CAP-U05-02 Invoice creation from an order (incl. order invoicing status)
- CAP-U05-03 Down payments / advance invoices
- CAP-U05-04 Credit notes, refunds and returns feeding back into the order
- CAP-U05-05 Delivery from sales (`sale_stock`): confirmation to delivery, delivered quantity, status
- CAP-U05-06 Interplay of delivered and invoiced quantities (upselling, reconciliation)
- CAP-U05-07 Loyalty / promotion programs (`sale_loyalty`)
- CAP-U05-08 Cross-sell and cross-module links (`sale_crm`, `sale_purchase`, `sale_mrp`, `sale_timesheet`, `sale_project`)
- CAP-U05-09 Roles, record rules, multi-company scope and scheduled behavior for invoicing/delivery links

## Contradiction claim ids
VDR-U05-C146, VDR-U05-C191

## Runtime-required claim ids
VDR-U05-C034, VDR-U05-C097, VDR-U05-C141, VDR-U05-C143, VDR-U05-C180, VDR-U05-C239, VDR-U05-C241, VDR-U05-C275, VDR-U05-C341, VDR-U05-C388, VDR-U05-C389, VDR-U05-C445, VDR-U05-C453, VDR-U05-C460

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
