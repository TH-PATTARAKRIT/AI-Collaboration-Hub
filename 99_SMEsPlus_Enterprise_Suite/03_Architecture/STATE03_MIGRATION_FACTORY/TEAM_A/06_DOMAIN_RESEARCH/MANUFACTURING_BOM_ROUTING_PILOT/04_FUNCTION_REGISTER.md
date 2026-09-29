> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Function Universe + Criticality | Documentation-Tier

# 04 — FUNCTION REGISTER

| ID | Function | Scope note | Criticality | Criticality reason |
|---|---|---|---|---|
| BRP-F01 | BOM Type selection (Manufacture / Kit / Subcontracting) | The single field that routes a product's entire downstream stock and financial treatment | **C1** | Determines which of three structurally different postings/ownership models applies — a misrouted type would misstate stock or financial ownership, not just a cost detail |
| BRP-F02 | Kit BOM (components-only, no Manufacturing Order) | A kit is a sales-side bundling construct, not a production event | **C2** | No separate financial posting of its own (per WHAT below) — component values pass through unchanged; risk is in mis-modeling it as manufactured |
| BRP-F03 | Subcontracting BOM (outsourced production) | Components sent to a subcontractor location while manufacturing happens off-site | **C1** | Financial-control-adjacent: governs whether sent-out components leave your valuation (they do not) and how a subcontractor's own output re-enters your stock/valuation |
| BRP-F04 | Work Center configuration (Cost per hour, Allowed Employees) | Defines the cost rate that operations consume | **C2** | Feeds `MFG-F04` (MO cost computation, Gx7) as an input — wrong rate configuration misvalues every MO using that work center, but is itself a computed-cost input, not a posting event |
| BRP-F05 | Routing Operations / Work Orders (per-BOM operation steps) | Named steps on a BOM, each tied to a Work Center with an expected duration | **C2** | Determines *how much* of BRP-F04's cost rate is consumed per unit produced — a sequencing/time input to cost, not itself a financial posting |
