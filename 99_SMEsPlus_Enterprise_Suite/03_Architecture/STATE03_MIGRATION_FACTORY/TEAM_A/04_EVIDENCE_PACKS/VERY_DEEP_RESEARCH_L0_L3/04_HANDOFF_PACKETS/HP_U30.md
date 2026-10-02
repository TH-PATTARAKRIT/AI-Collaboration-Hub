# Atomic Handoff Packet — U30

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U30` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `fde16ab94701e08561ea327fa5a6c24d4cdb6c91` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=356 supported_pointer_and_anchor=356 unknown_class=4 neutral_ids=137` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U30_tax_line_sync_totals_cashbasis.md` | `5897e322d70c59b6585c920ef10a00196a089eb8e76a08a98fafa160a08d5301` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U30_tax_line_sync_totals_cashbasis_NEUTRAL.md` | `d05c9a8298ddf68dfe8f8dd0aed0d1da40fd3bd9f45234e2e35445a8a6f14ef5` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 356 (FACT 325 · OBSERVATION 12 · INFERENCE 15 · UNKNOWN 4) |
| Neutral statements | 137 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 11 |
| Claims bound to an existing C1 Function-ID | 7 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 7; `FUNCTION MAPPING REQUIRED`: 349 |
| Existing Function-IDs referenced | PCO-F01×7 |

## Capabilities in scope
- CAP-U30-01 Synchronisation of derived journal items (framework, order, protection, balance check)
- CAP-U30-02 Payment-term items (due-date items of receivable and payable)
- CAP-U30-03 Tax-item generation and update from base items
- CAP-U30-04 Rounding allocation across lines, tax items and currencies
- CAP-U30-05 Cash-rounding, early-payment, discount-allocation and balancing items
- CAP-U30-06 Document tax totals summary (display, edit, stored versus recomputed)
- CAP-U30-07 Cash-basis tax exigibility, end to end
- CAP-U30-08 Tax items on credit note, switch, reset, cancel and fiscal-position change
- CAP-U30-09 Multi-currency tax items, rate date and exchange interplay

## Contradiction claim ids
VDR-U30-C094

## Runtime-required claim ids
VDR-U30-C072, VDR-U30-C127, VDR-U30-C217, VDR-U30-C274, VDR-U30-C286, VDR-U30-C328, VDR-U30-C329, VDR-U30-C340, VDR-U30-C343, VDR-U30-C345, VDR-U30-C355

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
