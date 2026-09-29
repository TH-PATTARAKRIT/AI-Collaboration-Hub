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
| GAP-BRP-09 | The precise cost-allocation method between a primary product and its By-Product(s) | `BRP-F08`'s own C1 open half | **Targeted Validation Needed** | Official-doc pass focused specifically on by-product cost allocation, or AWT |
| GAP-BRP-10 | Whether a cost change at a lower BOM level re-costs already-completed higher-level MOs, or only future ones | `BRP-F09` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |

## Status summary

```
GAPS OPEN                    : 10
RESOLVED (2026-09-29)        : 1 (GAP-BRP-03, documentation-tier)
TARGETED VALIDATION          : 1 (GAP-BRP-09 — the pilot's second open C1 half)
NON-BLOCKING                 : 8 (GAP-BRP-01, 02, 04, 05, 06, 07, 08, 10)
```
