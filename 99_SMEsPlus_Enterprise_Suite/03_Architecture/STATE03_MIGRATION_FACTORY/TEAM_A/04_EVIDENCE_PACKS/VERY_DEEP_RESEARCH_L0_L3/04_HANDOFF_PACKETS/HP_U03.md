# Atomic Handoff Packet — U03

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U03` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `4202eba83fbc157e4a60e5d7241dfd613e6fef22` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=300 supported_pointer_and_anchor=300 unknown_class=7 neutral_ids=166` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U03_mail_audit_foundation.md` | `6b0f2e5b3a625ce2933f83584f1b366a7aafe3e3ffa2ba14c717a42034fff7aa` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U03_mail_audit_foundation_NEUTRAL.md` | `7bc8f7ef5e46b2791e07a02e739c11dd8495c3724fc7f7dd84522d348dc97292` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 300 (FACT 257 · OBSERVATION 17 · INFERENCE 19 · UNKNOWN 7) |
| Neutral statements | 166 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 8 |
| Claims bound to an existing C1 Function-ID | 59 (distinct C1 IDs: RCN-F02) |
| Claims with an existing Function-ID | 59; `FUNCTION MAPPING REQUIRED`: 241 |
| Existing Function-IDs referenced | RCN-F02×59 |

## Capabilities in scope
- CAP-U03-01 Field tracking and discussion log as an audit trail
- CAP-U03-02 Followers, subscriptions and notification routing
- CAP-U03-03 Activities (to-do tasks) as lightweight follow-up and approval hand-off
- CAP-U03-04 Mail templates and the outgoing mail queue
- CAP-U03-05 Incoming mail, aliases and the mail gateway
- CAP-U03-06 Thread and activity mixin contract inherited by business models
- CAP-U03-07 Customer portal access, share links and signup invitation
- CAP-U03-08 Security and multi-company aspects of the messaging models
- CAP-U03-09 Digest KPI emails (light)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U03-C025, VDR-U03-C054, VDR-U03-C055, VDR-U03-C175, VDR-U03-C202, VDR-U03-C254, VDR-U03-C272, VDR-U03-C299

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
