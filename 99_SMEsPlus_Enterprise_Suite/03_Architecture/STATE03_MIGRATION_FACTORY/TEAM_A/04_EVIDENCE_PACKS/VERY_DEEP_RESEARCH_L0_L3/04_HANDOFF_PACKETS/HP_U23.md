# Atomic Handoff Packet — U23

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U23` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `1617494887bf16d9fdb9b0facb4ed1d028c02389` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=508 supported_pointer_and_anchor=493 unknown_class=15 neutral_ids=172` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U23_not_installed_current.md` | `2f19c4ba3b3954b9316f2415ac2445b1cbf543f42f786aaf2d3b14c8a92c1e5b` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U23_not_installed_current_NEUTRAL.md` | `080abb141d014097d773d3239cf6271ae5cfdb9242b55e7aa32c327d508f4f5a` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 508 (FACT 455 · OBSERVATION 17 · INFERENCE 21 · UNKNOWN 15) |
| Neutral statements | 172 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 19 |
| Claims bound to an existing C1 Function-ID | 1 (distinct C1 IDs: PCO-F01) |
| Claims with an existing Function-ID | 1; `FUNCTION MAPPING REQUIRED`: 507 |
| Existing Function-IDs referenced | PCO-F01×1 |

## Capabilities in scope
- CAP-U23-01 Withholding tax registered at payment time
- CAP-U23-02 Debit note issuance and numbering
- CAP-U23-03 Partner tax-number validation (VAT or TIN) and cross-border check
- CAP-U23-04 Formula-defined taxes
- CAP-U23-05 Re-applying tax-report tags to existing journal items
- CAP-U23-06 Accounting consistency tests
- CAP-U23-07 External authentication: directory server and identity providers
- CAP-U23-08 Password policy and session timeout
- CAP-U23-09 External (cloud) attachment storage
- CAP-U23-10 Peripheral features: personal dashboards, extended address, sparse storage, bot challenge, course forum

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U23-C061, VDR-U23-C062, VDR-U23-C077, VDR-U23-C094, VDR-U23-C095, VDR-U23-C115, VDR-U23-C134, VDR-U23-C135, VDR-U23-C136, VDR-U23-C164, VDR-U23-C166, VDR-U23-C185, VDR-U23-C191, VDR-U23-C286, VDR-U23-C325, VDR-U23-C341, VDR-U23-C382, VDR-U23-C441, VDR-U23-C508

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
