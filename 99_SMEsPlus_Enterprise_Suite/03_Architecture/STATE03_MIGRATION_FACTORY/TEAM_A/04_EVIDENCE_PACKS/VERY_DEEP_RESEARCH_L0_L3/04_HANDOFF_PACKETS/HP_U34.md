# Atomic Handoff Packet — U34

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U34` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `68ed16dfa6dc48b5675f44aa1ff5307e0ddb5f0f` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=373 supported_pointer_and_anchor=373 unknown_class=9 neutral_ids=203` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U34_account_edi_bridges_utilities.md` | `d243bd815d80c6e14328a4c35921dc55d3e6cb012b3e32af1e35bc7b9594d1d3` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U34_account_edi_bridges_utilities_NEUTRAL.md` | `e3db54d729e5bbffd9b90d2966185618d7f529960f0c5e7ecb88e9bf59c92a28` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 373 (FACT 335 · OBSERVATION 9 · INFERENCE 20 · UNKNOWN 9) |
| Neutral statements | 203 |
| Contradiction (CONTRA) claims | 4 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 373 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U34-01 E-invoice format registry, partner electronic address and delivery-location number
- CAP-U34-02 E-invoice export pipeline, delivery and attachment handling
- CAP-U34-03 Export field mapping: parties, taxes, currency and amounts
- CAP-U34-04 Export validation constraints and failure reporting
- CAP-U34-05 E-invoice import: detection, decoding, retrieval and corrections
- CAP-U34-06 Regional format boundary and dependent modules
- CAP-U34-07 Fleet vendor-bill bridge
- CAP-U34-08 Runtime API documentation service
- CAP-U34-09 Attachment text indexation

## Contradiction claim ids
VDR-U34-C085, VDR-U34-C086, VDR-U34-C273, VDR-U34-C274

## Runtime-required claim ids
VDR-U34-C023, VDR-U34-C059, VDR-U34-C061, VDR-U34-C070, VDR-U34-C097, VDR-U34-C174, VDR-U34-C177, VDR-U34-C196, VDR-U34-C213, VDR-U34-C220, VDR-U34-C282, VDR-U34-C321, VDR-U34-C325, VDR-U34-C326, VDR-U34-C353, VDR-U34-C364

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
