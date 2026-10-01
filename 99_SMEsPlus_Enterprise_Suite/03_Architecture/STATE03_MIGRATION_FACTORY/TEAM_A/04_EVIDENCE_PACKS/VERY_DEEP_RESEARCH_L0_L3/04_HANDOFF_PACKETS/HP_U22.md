# Atomic Handoff Packet — U22

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U22` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `37e4d26ffb0c181ae669db46028f9c9b95b34051` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=546 supported_pointer_and_anchor=546 unknown_class=26 neutral_ids=324` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U22_core_bridges.md` | `c406d103589d3fb7704573832f8a24e1e31f264b02458bbcc1c071c87dcdc2d3` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U22_core_bridges_NEUTRAL.md` | `d99c46a659a9c0cbe055afe38a888b5dec1c364e4fe4b2e4291334fed22db819` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 546 (FACT 469 · OBSERVATION 20 · INFERENCE 31 · UNKNOWN 26) |
| Neutral statements | 324 |
| Contradiction (CONTRA) claims | 1 |
| Runtime/AWT-required (RT) claims | 62 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 546 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U22-01 Customer-demand-linked purchasing (traceability, notifications, alternatives)
- CAP-U22-02 Promotion, coupon, gift card, eWallet and loyalty program definition, card issuance and balance history (base `loyalty`)
- CAP-U22-03 Free-shipping reward and prepaid-instrument restrictions on delivery payment (`sale_loyalty_delivery`)
- CAP-U22-04 Sales margin cost sources (delivered-cost and expense bridges) and the invoice-based product margin report
- CAP-U22-05 Project-linked stock transfers: analytic costing and re-invoicing of consumed materials
- CAP-U22-06 Carrier- and weight-aware automatic delivery batching, and pickup-point (Mondial Relay) shipping address
- CAP-U22-07 Variant grid (matrix) entry on sales and purchase orders
- CAP-U22-08 Electronic order and invoice exchange scaffolding: UBL ordering import/export, proxy client, deprecated Peppol fields, SEPA QR
- CAP-U22-09 Print-on-demand fulfilment through an external service (Gelato): order forwarding, shipping quotes, status webhook, product sync
- CAP-U22-10 Postal dispatch of documents and posting-time side effects of small bridges (snailmail, product email, fleet service log, SMS template rights, service flag, maintenance location)

## Contradiction claim ids
VDR-U22-C181

## Runtime-required claim ids
VDR-U22-C041, VDR-U22-C048, VDR-U22-C120, VDR-U22-C121, VDR-U22-C122, VDR-U22-C151, VDR-U22-C152, VDR-U22-C159, VDR-U22-C160, VDR-U22-C167, VDR-U22-C204, VDR-U22-C205, VDR-U22-C206, VDR-U22-C250, VDR-U22-C251, VDR-U22-C253, VDR-U22-C254, VDR-U22-C288, VDR-U22-C293, VDR-U22-C294, VDR-U22-C328, VDR-U22-C329, VDR-U22-C372, VDR-U22-C373, VDR-U22-C374, VDR-U22-C375, VDR-U22-C376, VDR-U22-C380, VDR-U22-C382, VDR-U22-C405, VDR-U22-C406, VDR-U22-C407, VDR-U22-C430, VDR-U22-C431, VDR-U22-C432, VDR-U22-C433, VDR-U22-C434, VDR-U22-C437, VDR-U22-C440, VDR-U22-C443, VDR-U22-C444, VDR-U22-C445, VDR-U22-C448, VDR-U22-C456, VDR-U22-C457, VDR-U22-C458, VDR-U22-C459, VDR-U22-C461, VDR-U22-C462, VDR-U22-C463, VDR-U22-C467, VDR-U22-C473, VDR-U22-C481, VDR-U22-C487, VDR-U22-C488, VDR-U22-C489, VDR-U22-C490, VDR-U22-C533, VDR-U22-C534, VDR-U22-C535, VDR-U22-C536, VDR-U22-C545

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
