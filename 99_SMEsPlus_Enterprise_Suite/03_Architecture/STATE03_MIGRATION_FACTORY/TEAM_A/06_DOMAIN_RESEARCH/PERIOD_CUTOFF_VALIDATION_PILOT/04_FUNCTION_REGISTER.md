> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Function Universe + Criticality

# 04 — FUNCTION REGISTER (Gx6)

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| PCO-F01 | Lock Dates (Everything / Purchase / Sales / Tax / Fiscal Year, Hard Lock) | Restricting creation/modification of entries before a date | **C1** | Direct, hard financial control; Hard Lock is documented as irreversible. |
| PCO-F02 | Fiscal Year / Period configuration | Default 12-month year ending Dec 31, configurable | **C3** | Configuration only. |
| PCO-F03 | Month-end Stock Closing + accrual entries | The mechanism that resolves the cross-Gx valuation-timing question | **C1** | Directly determines Financial Truth completeness at period end; this Gx's central finding. |
| PCO-F04 | Physical-date vs. recorded-date cut-off consistency | Whether a stock movement's physical date and its eventual financial posting date can diverge, and how that divergence is bridged | **C1** | This is the literal scenario-6 question; `PCO-F03` is the documented bridging mechanism. |
