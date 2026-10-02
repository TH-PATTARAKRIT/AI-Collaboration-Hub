# Atomic Handoff Packet — U60

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U60` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `f81f447c3039d0e28dd7ade55d542b8b804f1913` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=105 supported_pointer_and_anchor=105 unknown_class=0 neutral_ids=18` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U60_website_core_extensions.md` | `8165fee35a370b147e342a6f11770a20a5dd917ae8e7dd447f2e6a7f67760336` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U60_website_core_extensions_NEUTRAL.md` | `c478e1d8394d80a93b72676dd1f5f75c08ba3ee5e32819d39dac8caae339eaf5` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 105 (FACT 105 · OBSERVATION 0 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 18 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 0 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 105; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U60-01 — Website view Copy-on-Write (COW) isolation
- CAP-U60-02 — Website visitor tracking
- CAP-U60-03 — URL rewriting and routing management
- CAP-U60-04 — Website menu tree
- CAP-U60-05 — Website form controller
- CAP-U60-06 — Blog publishing system (website_blog)
- CAP-U60-07 — Website CRM lead capture (website_crm)
- CAP-U60-08 — IAP company reveal for anonymous visitors (website_crm_iap_reveal)
- CAP-U60-09 — Live chat to CRM bridge (website_crm_livechat)
- CAP-U60-10 — Partner/reseller locator (website_crm_partner_assign)
- CAP-U60-11 — SMS from website visitor context (website_crm_sms)
- CAP-U60-12 — Customer showcase (website_customer)

## Contradiction claim ids
none

## Runtime-required claim ids
none

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
