# Atomic Handoff Packet — U20

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U20` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `c89f426258d4b674388f089b7b4cde128a6ddc5b` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=348 supported_pointer_and_anchor=348 unknown_class=0 neutral_ids=111` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U20_payment_providers.md` | `df86fa7f01224fdbec4063297595703a9e9216379569766779dcbbe656513bbd` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U20_payment_providers_NEUTRAL.md` | `f1f657272c016a30c9ecb7937b5e811529afd560f25c93c2c79262b510aca244` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 348 (FACT 315 · OBSERVATION 13 · INFERENCE 20 · UNKNOWN 0) |
| Neutral statements | 111 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 52 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 348 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U20-01 Gateway add-on contract and provider lifecycle
- CAP-U20-02 Initiating an online payment through a gateway
- CAP-U20-03 Gateway notifications, return handling and forgery and replay protection
- CAP-U20-04 Amount and currency validation and state translation
- CAP-U20-05 Credential storage, access and logging
- CAP-U20-06 Capture, void, refund and saved payment methods
- CAP-U20-07 Availability, currencies, countries and Thailand relevance
- CAP-U20-08 Offline payment modes (wire transfer and cash on delivery)
- CAP-U20-09 Demo gateway
- CAP-U20-10 External connectivity and merchant onboarding

## Contradiction claim ids
VDR-U20-C085

## Runtime-required claim ids
VDR-U20-C052, VDR-U20-C057, VDR-U20-C058, VDR-U20-C059, VDR-U20-C082, VDR-U20-C083, VDR-U20-C095, VDR-U20-C096, VDR-U20-C100, VDR-U20-C101, VDR-U20-C117, VDR-U20-C118, VDR-U20-C119, VDR-U20-C126, VDR-U20-C134, VDR-U20-C136, VDR-U20-C139, VDR-U20-C141, VDR-U20-C142, VDR-U20-C143, VDR-U20-C144, VDR-U20-C146, VDR-U20-C147, VDR-U20-C148, VDR-U20-C149, VDR-U20-C150, VDR-U20-C180, VDR-U20-C195, VDR-U20-C316, VDR-U20-C317, VDR-U20-C318, VDR-U20-C319, VDR-U20-C320, VDR-U20-C321, VDR-U20-C322, VDR-U20-C323, VDR-U20-C324, VDR-U20-C325, VDR-U20-C326, VDR-U20-C327, VDR-U20-C328, VDR-U20-C329, VDR-U20-C330, VDR-U20-C331, VDR-U20-C332, VDR-U20-C333, VDR-U20-C334, VDR-U20-C335, VDR-U20-C336, VDR-U20-C337, VDR-U20-C338, VDR-U20-C339

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
