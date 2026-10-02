# Atomic Handoff Packet — U35

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U35` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `eed3d153cf6d2131a0cea025046115a7f06efe93` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=392 supported_pointer_and_anchor=383 unknown_class=9 neutral_ids=212` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U35_auth_barcodes_small_platform.md` | `49cf9b832949a06e5b7e9cb6ad4102fc502a6ded64f37f80b8077c77ee35ed9c` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U35_auth_barcodes_small_platform_NEUTRAL.md` | `864621bee975733b0c6fa3e81b71a2b5620a054976ed195ac4be24fb5ff333d5` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 392 (FACT 320 · OBSERVATION 13 · INFERENCE 50 · UNKNOWN 9) |
| Neutral statements | 212 |
| Contradiction (CONTRA) claims | 2 |
| Runtime/AWT-required (RT) claims | 16 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 392 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U35-01 Self-registration and invitation acceptance (sign-up page, token binding, template user)
- CAP-U35-02 Password reset by e-mailed link
- CAP-U35-03 Invitation lifecycle: user status, automatic invitations and the unregistered-user reminder
- CAP-U35-04 Password-policy support in sign-up and the external-user security page (not installed in the restored database)
- CAP-U35-05 Authenticator-application second step, enrolment, trusted browsers and portal management
- CAP-U35-06 E-mailed-code second step, enforcement policy, invitations and security alerts
- CAP-U35-07 Passkeys: registration, passwordless sign-in, identity re-check and portal management
- CAP-U35-08 Barcode nomenclatures, rule matching and scan handling
- CAP-U35-09 GS1 element-string decomposition and GS1-aware barcode search

## Contradiction claim ids
VDR-U35-C126, VDR-U35-C204

## Runtime-required claim ids
VDR-U35-C144, VDR-U35-C253, VDR-U35-C278, VDR-U35-C289, VDR-U35-C293, VDR-U35-C297, VDR-U35-C323, VDR-U35-C361, VDR-U35-C362, VDR-U35-C363, VDR-U35-C364, VDR-U35-C365, VDR-U35-C366, VDR-U35-C367, VDR-U35-C368, VDR-U35-C369

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
