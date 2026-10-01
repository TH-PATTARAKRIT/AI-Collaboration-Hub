# Atomic Handoff Packet — U02

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U02` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `0cf339b5e4a39aecce5774997f8547d4d98e64a6` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=494 supported_pointer_and_anchor=486 unknown_class=9 neutral_ids=244` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U02_product_uom_analytic.md` | `0f6e9dd8fdb01ff1d11161caa4eafd074b5ebe33ec7ade993edc656f9a966521` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U02_product_uom_analytic_NEUTRAL.md` | `d59f4c205693864a067166cda257c5d1ce1c62c56886fde76ce8c2ccc0c334e9` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 494 (FACT 433 · OBSERVATION 18 · INFERENCE 34 · UNKNOWN 9) |
| Neutral statements | 244 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 5 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 36; `FUNCTION MAPPING REQUIRED`: 458 |
| Existing Function-IDs referenced | RTG-F01×29, RTG-F04×7 |

## Capabilities in scope
- CAP-U02-01 Product master: definition vs variant, product type, inventory tracking, variants, archive, uniqueness
- CAP-U02-02 Product categories and company-dependent properties (accounting, valuation, routing) - hand-off to stock and accounting units
- CAP-U02-03 Pricelists and price rules: rule types, applicability, computation order, currency, scoping, lookup by sales
- CAP-U02-04 Units of measure: tree of units, conversion and rounding, change-after-use rules, packagings
- CAP-U02-05 Vendor price lines on the product (supplier info): selection, validity, minimum quantity, currency, company scope
- CAP-U02-06 Analytic accounting: plans, accounts, applicability, distribution models, analytic lines, attachment to documents
- CAP-U02-07 Product documents, combos, tags, attribute exclusions, catalog helper and bulk attribute wizard (brief)
- CAP-U02-08 Roles, access rights, record rules and multi-company scoping on product, pricelist, unit, analytic, tracker and calendar objects
- CAP-U02-09 Scheduled and automated behaviour; configuration and optionality switches
- CAP-U02-10 Marketing trackers (utm) and working calendars (resource): what they give the core chains (light touch)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U02-C094, VDR-U02-C211, VDR-U02-C269, VDR-U02-C366, VDR-U02-C424

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
