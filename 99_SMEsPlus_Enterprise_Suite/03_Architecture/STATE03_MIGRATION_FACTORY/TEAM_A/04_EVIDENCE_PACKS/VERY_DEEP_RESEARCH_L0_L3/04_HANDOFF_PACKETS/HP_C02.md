# Atomic Handoff Packet — C02

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `C02` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `72cf594ad5ac53bb4b2c5fcb994885f599b4de33` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=310 supported_pointer_and_anchor=300 unknown_class=11 neutral_ids=211` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/C02_procure_to_pay_chain.md` | `42d89f57933e4b53d004cabaf2d2ec286f88794dc1b0da6bf132b6e5f2dbd669` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/C02_procure_to_pay_chain_NEUTRAL.md` | `fcc1e534a1c92c80a408c4f94d72e8e0a1e46544d98dca62ad42dc1e83fc075e` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 310 (FACT 235 · OBSERVATION 19 · INFERENCE 45 · UNKNOWN 11) |
| Neutral statements | 211 |
| Contradiction (CONTRA) claims | 6 |
| Runtime/AWT-required (RT) claims | 33 |
| Claims bound to an existing C1 Function-ID | 62 (distinct C1 IDs: GRV-F04, GRV-F05, GRV-F06, PCO-F01, PCO-F03, PCO-F04, PDT-F02, PDT-F03, RCN-F03) |
| Claims with an existing Function-ID | 178; `FUNCTION MAPPING REQUIRED`: 132 |
| Existing Function-IDs referenced | BRP-F06×23, GRV-F01×4, GRV-F02×18, GRV-F03×27, GRV-F04×18, GRV-F05×10, GRV-F06×11, GRV-F07×36, PCO-F01×3, PCO-F03×6, PCO-F04×1, PDT-F02×4, PDT-F03×7, PDT-F04×7, RCN-F03×2, RTG-F01×1 |

## Capabilities in scope
- CAP-C02-01 Happy path end to end: need or RFQ, confirm (approval branch), receipt creation, receipt validation, vendor bill creation, posting, payment registration, reconciliation, paid
- CAP-C02-02 Bill control variants (ordered versus received): sequence differences, what is blocked or allowed, quantities and statuses on order line, bill and receipt
- CAP-C02-03 Return and refund chain: receipt return, vendor credit note, effects on received and billed quantities, stock, accounting and valuation
- CAP-C02-04 Cancellation chain at each stage: request, approved or locked order, partly received order, draft bill, posted bill, paid bill
- CAP-C02-05 Partial flows: partial receipt and backorder, partial billing, partial payment, price or quantity change after approval
- CAP-C02-06 Replenishment-driven procurement: reordering rule or make-to-order need to RFQ, merging into an existing RFQ, vendor selection, lead times, dropship variant, landed costs
- CAP-C02-07 Multi-company data scope across the chain (source only; single-company DB) and role separation (create, approve, receive, bill, pay), with segregation-of-duties gaps
- CAP-C02-08 Accounting, stock, audit, tax and compliance implications across the chain
- CAP-C02-09 Consistency audit of U06, U07, U08, U10, U11 and U12 at shared hand-off points

## Contradiction claim ids
VDR-C02-C108, VDR-C02-C286, VDR-C02-C287, VDR-C02-C294, VDR-C02-C304, VDR-C02-C305

## Runtime-required claim ids
VDR-C02-C036, VDR-C02-C042, VDR-C02-C067, VDR-C02-C068, VDR-C02-C069, VDR-C02-C099, VDR-C02-C100, VDR-C02-C132, VDR-C02-C140, VDR-C02-C143, VDR-C02-C147, VDR-C02-C159, VDR-C02-C175, VDR-C02-C179, VDR-C02-C188, VDR-C02-C189, VDR-C02-C224, VDR-C02-C225, VDR-C02-C230, VDR-C02-C235, VDR-C02-C247, VDR-C02-C248, VDR-C02-C255, VDR-C02-C280, VDR-C02-C281, VDR-C02-C284, VDR-C02-C288, VDR-C02-C289, VDR-C02-C291, VDR-C02-C297, VDR-C02-C299, VDR-C02-C303, VDR-C02-C310

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
