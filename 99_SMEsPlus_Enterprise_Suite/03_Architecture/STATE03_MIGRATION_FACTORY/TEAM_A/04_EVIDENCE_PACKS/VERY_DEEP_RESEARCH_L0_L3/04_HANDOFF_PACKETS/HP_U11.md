# Atomic Handoff Packet — U11

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U11` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4202eba83fbc157e4a60e5d7241dfd613e6fef22` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=420 supported_pointer_and_anchor=411 unknown_class=10 neutral_ids=194` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U11_account_entry_lifecycle.md` | `62daed46442b8f4ff08be025a74d0763638a87b68e69ff817547bc0cee1d79c5` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U11_account_entry_lifecycle_NEUTRAL.md` | `db7958b015786ae837552e897eb5e37ffd89034dea2fdd2c6f18a1d9fb78e226` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 420 (FACT 366 · OBSERVATION 17 · INFERENCE 27 · UNKNOWN 10) |
| Neutral statements | 194 |
| Contradiction (CONTRA) claims | 4 |
| Runtime/AWT-required (RT) claims | 14 |
| Claims bound to an existing C1 Function-ID | 77 (distinct C1 IDs: PCO-F01, PCO-F04, SDV-F07) |
| Claims with an existing Function-ID | 215; `FUNCTION MAPPING REQUIRED`: 205 |
| Existing Function-IDs referenced | PCO-F01×50, PCO-F04×5, SDV-F07×22 |

## Capabilities in scope
- CAP-U11-01 Entry state machine (draft / posted / cancel; payment-state hand-off)
- CAP-U11-02 Posting validation (balance assertion, required fields, journal/type, currency, tax-country, date, auto-post)
- CAP-U11-03 Naming, sequences and inalterability (hash chain)
- CAP-U11-04 Lock dates and lock exceptions
- CAP-U11-05 Reversal and credit notes
- CAP-U11-06 Auto-post and scheduled entries
- CAP-U11-07 Entry-line computation and dynamic lines
- CAP-U11-08 Journals
- CAP-U11-09 Audit trail, compliance, roles/ACL/record rules
- CAP-U11-10 Multi-company / data-scope and cross-module triggers into entry creation

## Contradiction claim ids
VDR-U11-C005, VDR-U11-C082, VDR-U11-C134, VDR-U11-C135

## Runtime-required claim ids
VDR-U11-C108, VDR-U11-C167, VDR-U11-C187, VDR-U11-C188, VDR-U11-C218, VDR-U11-C222, VDR-U11-C252, VDR-U11-C268, VDR-U11-C269, VDR-U11-C311, VDR-U11-C343, VDR-U11-C377, VDR-U11-C384, VDR-U11-C414

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
