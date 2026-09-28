> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX (Gx4)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | IAV-F03/F04: adjustment and scrap both carry documented financial-posting behavior. |
| Inventory | **Applicable** | IAV-F01/F02: core Stock Truth correction mechanism. |
| Authority (approval/execute/post/reverse) | **Unknown** | No documentation evidence on who may apply an adjustment or scrap goods (role/permission). |
| Period / reversal | **Applicable, partially evidenced** | IAV-F06 (reversal) unevidenced; no period/cut-off interaction found this round either. |
| Tenant / Company / Data Scope | **Unknown** | Not evidenced. |
| Audit / Event | **Applicable, partially evidenced** | Bulk-apply "reason" recording is a documented audit-adjacent data point; full event/audit-trail behavior otherwise unevidenced. |
| Automation / Integration | **Applicable** | Cycle-count scheduling (IAV-F05) is a documented automation; scrap's dependency on both product-category and location configuration is a documented cross-configuration integration. |
| Cross-module effects | **Applicable** | IAV-F03/F04 both touch Accounting; this is this Gx's own instance of the Backbone Roadmap's Inventory↔Accounting boundary. |
