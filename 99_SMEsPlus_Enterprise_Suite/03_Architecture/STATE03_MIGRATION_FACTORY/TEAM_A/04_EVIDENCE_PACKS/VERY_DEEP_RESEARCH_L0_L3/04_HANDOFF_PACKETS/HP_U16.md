# Atomic Handoff Packet — U16

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U16` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `c4e39cfa1aefd34013f6664d093393fb931a8c94` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=449 supported_pointer_and_anchor=445 unknown_class=12 neutral_ids=233` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U16_project_timesheet_expense.md` | `92f739d465a60d1e0a12f64ea3bacaa0aad7ac110e5b40104962eb503f11347d` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U16_project_timesheet_expense_NEUTRAL.md` | `f6b721a5cb0e1b3dc6e403c6cf00fdea733597242961091286f8641f5a22ce18` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 449 (FACT 392 · OBSERVATION 17 · INFERENCE 28 · UNKNOWN 12) |
| Neutral statements | 233 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 449 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U16-01 Employee expense capture and categories
- CAP-U16-02 Expense approval workflow
- CAP-U16-03 Expense accounting entry creation (employee-paid and company-paid)
- CAP-U16-04 Employee reimbursement and expense settlement status
- CAP-U16-05 Re-invoicing expenses to customers
- CAP-U16-06 Timesheet recording, cost valuation and analytic linkage
- CAP-U16-07 Billing services and timesheets from sales orders
- CAP-U16-08 Sale-to-project generation and project analytic distribution
- CAP-U16-09 Project profitability and project cost links (purchase, stock, landed cost, expense, time)
- CAP-U16-10 Time-off, attendance comparison and project collaboration extensions

## Contradiction claim ids
VDR-U16-C002

## Runtime-required claim ids
VDR-U16-C016, VDR-U16-C042, VDR-U16-C075, VDR-U16-C089, VDR-U16-C154, VDR-U16-C158, VDR-U16-C161, VDR-U16-C162, VDR-U16-C163, VDR-U16-C202, VDR-U16-C203, VDR-U16-C296, VDR-U16-C414, VDR-U16-C418, VDR-U16-C419, VDR-U16-C422

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
