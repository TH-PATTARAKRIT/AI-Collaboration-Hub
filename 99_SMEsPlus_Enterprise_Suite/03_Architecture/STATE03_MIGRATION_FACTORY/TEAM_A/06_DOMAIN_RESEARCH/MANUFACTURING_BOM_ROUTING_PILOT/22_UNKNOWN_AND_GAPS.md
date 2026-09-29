> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-BRP-01 | Whether a BoM Type can be changed after the BoM is in use by open Sales/Manufacturing Orders, or whether it locks | Unknown — structural/data-integrity question for `BRP-F01` | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-02 | Whether a Kit can also carry manufacturing operations (a hybrid sell-and-lightly-assemble case) and how valuation behaves if so | `BRP-F02` boundary case not evidenced | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-03 | How a subcontractor's own fee/labor is captured and valued into the returned product | `BRP-F03`'s financial-completion mechanics — the C1 function's own open half | **Targeted Validation Needed** | Official-doc pass focused specifically on subcontracting cost capture, or AWT |
| GAP-BRP-04 | Whether Work Center Cost per hour supports time-based variation (shift/overtime rates) or is a flat figure | `BRP-F04` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-05 | Behavior of a BoM with Work Orders disabled; whether actual-vs-expected duration variance is tracked | `BRP-F05` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-BRP-06 | Same network/egress constraint as every prior Gx/pilot | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior units |

## Status summary

```
GAPS OPEN                    : 6
TARGETED VALIDATION          : 1 (GAP-BRP-03 — the one C1 function's own open half)
NON-BLOCKING                 : 5 (GAP-BRP-01, 02, 04, 05, 06)
```
