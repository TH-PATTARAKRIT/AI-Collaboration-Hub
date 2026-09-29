> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-BRP-01 | Whether a BoM Type can be changed after the BoM is in use by open Sales/Manufacturing Orders, or whether it locks | Unknown — structural/data-integrity question for `BRP-F01` | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-02 | Whether a Kit can also carry manufacturing operations (a hybrid sell-and-lightly-assemble case) and how valuation behaves if so | `BRP-F02` boundary case not evidenced | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-03 | **RESOLVED 2026-09-29, documentation-tier (V2).** Vendor price on the subcontracted product = subcontractor's fee/service cost; product cost = component cost + that fee. Posting the vendor bill debits the Finished Goods Valuation Account, capturing the fee at vendor-bill time. See `06_BUSINESS_RULE_REGISTER.md` BRP-F03. | `BRP-F03`'s financial-completion mechanics now documented | **Resolved (documentation-tier)** | AWT for runtime confirmation only — not blocking |
| GAP-BRP-04 | Whether Work Center Cost per hour supports time-based variation (shift/overtime rates) or is a flat figure | `BRP-F04` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-05 | Behavior of a BoM with Work Orders disabled; whether actual-vs-expected duration variance is tracked | `BRP-F05` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-06 | Same network/egress constraint as every prior Gx/pilot | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior units |
| GAP-BRP-07 | Whether automatic Reordering Rules have any approval/authorization gate before order creation | `BRP-F06` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-08 | Whether MPS forecasts feed any automated process beyond guiding manual order placement | `BRP-F07` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-09 | The precise cost-allocation method between a primary product and its By-Product(s) | `BRP-F08`'s own C1 open half | **Open / Conditional** (candidate default found, sub-documentation-tier — see below; not Resolved) | Official-doc pass focused specifically on by-product cost allocation, or AWT |
| GAP-BRP-10 | Whether a cost change at a lower BOM level re-costs already-completed higher-level MOs, or only future ones | `BRP-F09` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |

## GAP-BRP-09 — full C1 record (per Boss's "STATE03 Population Lineage Correction & Autonomous Continuation" §3, 2026-09-29)

| Field | Value |
|---|---|
| Gap/Function ID | `GAP-BRP-09` / `BRP-F08` (By-Products) |
| Criticality | **C1** |
| Target V | V5 (floor V4) |
| Actual V | **V1** — third-party marketplace listing + pre-19/V12 community forum corroboration; explicitly **not** upgraded to V2 because the official `mo_costs.html` documentation page does not itself state a by-product cost-allocation rule |
| Evidence pointer | `EV-BRP-13` (third-party app listing, `mfg_byproduct_cost`), `EV-BRP-14` (Odoo forum, V12, "deduct cost for by-product") — `19_PROVENANCE_REGISTER.md` |
| Source/version/configuration scope | Candidate default described for Odoo core generally (third-party listing) and confirmed pre-19 (V12 forum); **not independently confirmed for Odoo 19.0 specifically** — this is the open version/scope question |
| Business/control risk | If the candidate default holds ("no material cost allocated to by-products, full production cost charged to primary FG"), a by-product with independent market value would enter stock at zero/unset cost while the primary good's unit cost is inflated by the entire production cost — a discoverable financial-misstatement risk, structurally identical in shape to `BRP-F03`'s original (now-resolved) valuation-continuity risk |
| Status | **Open / Conditional** — not Resolved, not generalized into SMEsPlus target behavior |
| Route to close | Official-doc pass targeting Odoo 19.0 specifically, or AWT runtime confirmation once `BGQ-04` resolves |

## Status summary

```
GAPS OPEN                    : 10
RESOLVED (2026-09-29)        : 1 (GAP-BRP-03, documentation-tier)
OPEN / CONDITIONAL (partial evidence, sub-doc-tier) : 1 (GAP-BRP-09 — the pilot's second open C1 half; see full record above)
NON-BLOCKING                 : 8 (GAP-BRP-01, 02, 04, 05, 06, 07, 08, 10)
```
