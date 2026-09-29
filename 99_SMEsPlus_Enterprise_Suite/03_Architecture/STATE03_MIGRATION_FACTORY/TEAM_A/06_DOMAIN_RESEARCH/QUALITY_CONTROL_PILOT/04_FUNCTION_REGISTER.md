> Domain: QUALITY_CONTROL_PILOT | Function/Criticality Register | Documentation-Tier | **IN PROGRESS — 3 of an unknown-total function set**

# 04 — FUNCTION REGISTER

| Function ID | Function | Criticality | Target V | Actual V | Notes |
|---|---|---|---|---|---|
| `QCP-F01` | Quality Control Point (QCP) configuration — triggers a quality check by Operation (Manufacturing, Delivery, etc.), optionally scoped by Product/Product Category and by Quantity (every N units) | C2 | V4/floor V3 | V2 | `EV-QCP-01` |
| `QCP-F02` | Quality Check types — Pass/Fail, Measure (with a recorded numeric value), Picture (captured image), selectable per QCP | C2 | V4/floor V3 | V2 | `EV-QCP-02` |
| `QCP-F03` | Manufacturing-Order-triggered quality check — selecting "Manufacturing" as a QCP's Operation creates a quality check on new MOs; optionally scoped further to one specific Work Order Operation. A pending/incomplete mandatory check **blocks MO finalization** (`GAP-QCP-01` resolved) | **C1** | V5/floor V4 | V2 | `EV-QCP-02`, `EV-QCP-03`–`06`; direct extension of `M1`'s BoM/MO scope |

**Row count this pass: 3.** Not a complete function population for this module — see `00_DOMAIN_INDEX.md` §Scope for what remains.
