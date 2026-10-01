# Atomic Handoff Packet — TXA1

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `TXA1` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `760d9d0f75d2a1029c3b3390235bd83d9d156220` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=338 supported_pointer_and_anchor=330 unknown_class=8 neutral_ids=123` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/TXA1_thaitax_engine_vat_classes.md` | `10d17cdb57c16e02dace3501067f5c46cec6e0add15cd54f84e396da50585010` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/TXA1_thaitax_engine_vat_classes_NEUTRAL.md` | `7ce60dd8576412abdc8e6ae392eddca69cdd3c1851d82502052f2b39180c6333` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 338 (FACT 293 · OBSERVATION 21 · INFERENCE 16 · UNKNOWN 8) |
| Neutral statements | 123 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 7 |
| Claims bound to an existing C1 Function-ID | 4 (distinct C1 IDs: GRV-F04, PCO-F01) |
| Claims with an existing Function-ID | 4; `FUNCTION MAPPING REQUIRED`: 334 |
| Existing Function-IDs referenced | GRV-F04×1, PCO-F01×3 |

## Capabilities in scope
- CAP-TXA1-01 Generic tax calculation engine (types, ordering, base chains, price-included extraction)
- CAP-TXA1-02 Rounding methods, totals summary, discounts and cash rounding
- CAP-TXA1-03 Distribution lines, tax grid tags, accounts and tax journal items
- CAP-TXA1-04 Sales VAT and purchase VAT on documents (default tax resolution and document flows)
- CAP-TXA1-05 Thai tax treatments represented in the Thai template (standard-rated, zero-rated, exempt, withholding) and their document presentation
- CAP-TXA1-06 Non-deductible tax handling and tax on stock and cost flows
- CAP-TXA1-07 Price-included / price-excluded handling, currency conversion and multi-currency tax amounts
- CAP-TXA1-08 Company, partner, product and fiscal-position configuration that drives tax behaviour
- CAP-TXA1-09 Tax record lifecycle, template loading, security and locks (tax scope)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-TXA1-C224, VDR-TXA1-C299, VDR-TXA1-C324, VDR-TXA1-C331, VDR-TXA1-C333, VDR-TXA1-C334, VDR-TXA1-C338

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
