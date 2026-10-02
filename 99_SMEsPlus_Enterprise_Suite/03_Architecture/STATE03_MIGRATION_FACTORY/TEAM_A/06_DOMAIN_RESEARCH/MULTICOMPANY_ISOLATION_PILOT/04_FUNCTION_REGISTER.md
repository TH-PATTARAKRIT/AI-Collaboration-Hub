> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Function Universe + Criticality

# 04 — FUNCTION REGISTER (Gx9)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| MCT-F01 | Warehouse-company binding | Required, singular Company field on warehouse; users linked to companies | **C1** | Structural tenant-isolation boundary. |
| MCT-F02 | Inter-company transaction automation | Auto-create counterpart bill/SO/PO, stock-move sync — 4 independent togglable behaviors | **C1** | Cross-company financial and stock handoff, directly touches this Deep Study's whole valuation-timing thread across a company boundary. |
| MCT-F03 | Shared vs. per-company Chart of Accounts | Design choice, not fixed | **C2** | Affects how consolidation and cross-company reconciliation work. |
| MCT-F04 | Consolidation reporting | Combines multiple companies' financials into one view | **C2** | Reporting function, not itself a control. |
| MCT-F05 | Warehouse-level user access control | NOT a native single-field configuration — requires manual record rules + per-warehouse groups | **C1** | Real authority-control gap between "company-level" (native, structural) and "warehouse-level" (manual, non-trivial) isolation. |
