> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Function Universe + Criticality

# 04 — FUNCTION REGISTER (Gx7)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| MFG-F01 | Raw material consumption → WIP transfer | Component value moves from its stock valuation account to a WIP account | **C1** | Automatic financial posting, gated by Automated valuation mode. |
| MFG-F02 | Finished goods completion → valuation transfer | WIP value + labor/operations cost transfers to the finished good's valuation account | **C1** | Same class as MFG-F01; determines finished-good cost basis. |
| MFG-F03 | Manual interim WIP posting/reversal | For long-running MOs spanning a reporting boundary | **C2** | Optional, per-MO mechanism; not the default automatic path. |
| MFG-F04 | MO cost computation | Component cost + quantity + operations/work-center cost, per BOM | **C2** | Determines the value moved by MFG-F01/F02, but is itself a computation, not a posting event. |
| MFG-F05 | Negative-inventory / revaluation entries during an MO | Flagged edge case from a forum thread title only | **C1 (provisional)** | Financial-control-adjacent by name; not yet characterized — criticality may change once evidenced. |
