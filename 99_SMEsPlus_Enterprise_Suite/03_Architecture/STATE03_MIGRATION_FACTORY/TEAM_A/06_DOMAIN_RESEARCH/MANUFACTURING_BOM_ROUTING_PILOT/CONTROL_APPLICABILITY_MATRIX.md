> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | `BRP-F03` (subcontracting valuation non-impact rule) is the pilot's central financial-control finding; `BRP-F01`/`F04`/`F05` are financial-adjacent (routing/cost inputs). |
| Inventory | **Applicable** | `BRP-F03`'s Subcontracting Location and `BRP-F02`'s component pass-through are both core Stock Truth mechanisms. |
| Authority (approval/execute/post/reverse) | **Partially evidenced** | `BRP-F04`'s Allowed Employees is a documented authorization-adjacent control (who may work a station); no broader approval/reversal control evidenced for BoM Type changes. |
| Period / reversal | **Unknown** | Not evidenced this round for any of the 5 functions. |
| Tenant / Company / Data Scope | **Unknown** | Not evidenced this round. |
| Audit / Event | **Partially evidenced** | Work Order start/completion are documented as trackable events; no broader audit-trail behavior evidenced. |
| Automation / Integration | **Applicable** | Work Center/Routing cost computation feeding `MFG-F04` is a documented cross-function automation; BoM Type routing is itself a configuration-driven automation branch point. |
| Cross-module effects | **Applicable** | This entire pilot is Manufacturing/MRP feeding Gx7's Inventory↔Accounting boundary — a direct extension of Lane C's own Backbone Roadmap concern, at the structural (not valuation-timing) layer. |
