# Atomic Handoff Packet — TXA2

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `TXA2` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4de853a31e5de99f19f62217b954267e252735f3` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=328 supported_pointer_and_anchor=328 unknown_class=0 neutral_ids=133` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/TXA2_thaitax_documents_period_reversal.md` | `a13d78f7ae37436c6e1ee10605fb1a5293a8ff746efb64f8e9ef4a8bda81828c` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/TXA2_thaitax_documents_period_reversal_NEUTRAL.md` | `f685cf276b76bf106a0bb5d08487c2bbbe101b87ef7ebb3fd72599abdedebdff` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 328 (FACT 279 · OBSERVATION 16 · INFERENCE 33 · UNKNOWN 0) |
| Neutral statements | 133 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 23 |
| Claims bound to an existing C1 Function-ID | 121 (distinct C1 IDs: GRV-F04, MCT-F02, PCO-F01, PCO-F03, PCO-F04, PDT-F01, PDT-F02, RCN-F02, SDV-F05, SDV-F07) |
| Claims with an existing Function-ID | 126; `FUNCTION MAPPING REQUIRED`: 202 |
| Existing Function-IDs referenced | GRV-F04×1, MCT-F02×2, MCT-F03×2, PCO-F01×43, PCO-F02×3, PCO-F03×2, PCO-F04×29, PDT-F01×13, PDT-F02×5, RCN-F02×3, SDV-F05×3, SDV-F07×20 |

## Capabilities in scope
- CAP-TXA2-01 Tax document types, states and issuing identity
- CAP-TXA2-02 Tax-relevant dates: invoice date, accounting date, due date, supply and delivery dates
- CAP-TXA2-03 Lock dates, tax lock, cut-off and the absence of a tax-period object
- CAP-TXA2-04 Correction of posted tax documents: reset, cancel, reverse, re-issue, copy and debit note
- CAP-TXA2-05 Numbering, sequences, gaps and inalterability of tax documents
- CAP-TXA2-06 Tax journal entries: tax lines, tags, cash basis, withholding, reversal and re-tagging
- CAP-TXA2-07 Multi-company isolation, access groups and record rules for tax and fiscal records
- CAP-TXA2-08 Audit trail for tax-relevant records: tracking, chatter, deletion and attachment rules
- CAP-TXA2-09 Cross-module triggers into taxed documents: sales, purchase, inventory, expenses, payments
- CAP-TXA2-10 Document presentation of tax documents: titles, report selection, stored PDFs

## Contradiction claim ids
VDR-TXA2-C005, VDR-TXA2-C061

## Runtime-required claim ids
VDR-TXA2-C006, VDR-TXA2-C024, VDR-TXA2-C028, VDR-TXA2-C036, VDR-TXA2-C040, VDR-TXA2-C042, VDR-TXA2-C053, VDR-TXA2-C054, VDR-TXA2-C085, VDR-TXA2-C107, VDR-TXA2-C121, VDR-TXA2-C122, VDR-TXA2-C125, VDR-TXA2-C131, VDR-TXA2-C149, VDR-TXA2-C163, VDR-TXA2-C185, VDR-TXA2-C236, VDR-TXA2-C242, VDR-TXA2-C299, VDR-TXA2-C300, VDR-TXA2-C307, VDR-TXA2-C317

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
