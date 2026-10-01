# Atomic Handoff Packet — U04

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U04` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `2d9932ef7d4f1f527374512fdb113e712fb03184` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=458 supported_pointer_and_anchor=458 unknown_class=11 neutral_ids=243` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U04_sales_order.md` | `703fd657f5dfd6553018e14a1618243482ddf69c0c3289eff905ea2645b3f2b6` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U04_sales_order_NEUTRAL.md` | `da232446ca1add8422c4289a8b27ca4ae49b8f76c8689ceea7a73fc7d1cb99cc` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 458 (FACT 370 · OBSERVATION 22 · INFERENCE 55 · UNKNOWN 11) |
| Neutral statements | 243 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 20 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 458 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U04-01 Order state machine (quotation, sent, sales order, cancelled; lock flag)
- CAP-U04-02 Quotation to sales order confirmation (pre-checks, side effects, signature/payment path, auto-lock)
- CAP-U04-03 Cancellation and reset to draft
- CAP-U04-04 Pricing (pricelist, price computation, discounts, taxes mapping, currency, rounding)
- CAP-U04-05 Order line rules (types, quantities, editing restrictions, deletion, combos, down-payment lines)
- CAP-U04-06 Order-level amounts and taxes (totals, tax totals, amounts to invoice/paid, multi-currency)
- CAP-U04-07 Roles and record-level security
- CAP-U04-08 Scheduled and automated behaviour
- CAP-U04-09 Quotation templates and options, margin, PDF quote builder, sales teams
- CAP-U04-10 Multi-company and data-scope specifics of orders

## Contradiction claim ids
VDR-U04-C176

## Runtime-required claim ids
VDR-U04-C039, VDR-U04-C043, VDR-U04-C102, VDR-U04-C103, VDR-U04-C125, VDR-U04-C127, VDR-U04-C133, VDR-U04-C168, VDR-U04-C176, VDR-U04-C179, VDR-U04-C204, VDR-U04-C237, VDR-U04-C251, VDR-U04-C262, VDR-U04-C297, VDR-U04-C325, VDR-U04-C389, VDR-U04-C412, VDR-U04-C439, VDR-U04-C444

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
