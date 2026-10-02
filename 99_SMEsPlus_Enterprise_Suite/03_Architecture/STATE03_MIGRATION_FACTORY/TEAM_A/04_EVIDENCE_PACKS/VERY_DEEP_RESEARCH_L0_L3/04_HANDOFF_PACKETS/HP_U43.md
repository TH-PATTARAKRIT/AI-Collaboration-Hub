# Atomic Handoff Packet — U43

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U43` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `28b2af3e728ebb47c4682f8df745199fc3d3b09d` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=156 supported_pointer_and_anchor=156 unknown_class=0 neutral_ids=120` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U43_mail_family_maintenance_microsoft.md` | `4a404659d47031131b461b32697649f0f936311691289aaddd831260d40ae11f` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U43_mail_family_maintenance_microsoft_NEUTRAL.md` | `80bdf7a799bf4e47119d6556620137cba2677a156461910640e46e845954e7c0` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 156 (FACT 149 · OBSERVATION 1 · INFERENCE 6 · UNKNOWN 0) |
| Neutral statements | 120 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 11 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 156 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U43-01 OdooBot onboarding and bot replies
- CAP-U43-02 Mailing group lifecycle and moderation
- CAP-U43-03 Mailing group membership, tokens and portal
- CAP-U43-04 Mail plugin authentication, enrichment and logging
- CAP-U43-05 Maintenance request workflow
- CAP-U43-06 Equipment, categories, teams and alias intake
- CAP-U43-07 Maintenance security and multi-company
- CAP-U43-08 Microsoft account OAuth and token lifecycle
- CAP-U43-09 Outlook calendar synchronization
- CAP-U43-10 Outlook mail server OAuth (SMTP and IMAP)

## Contradiction claim ids
VDR-U43-C106

## Runtime-required claim ids
VDR-U43-C012, VDR-U43-C032, VDR-U43-C052, VDR-U43-C059, VDR-U43-C060, VDR-U43-C061, VDR-U43-C070, VDR-U43-C102, VDR-U43-C117, VDR-U43-C141, VDR-U43-C142

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
