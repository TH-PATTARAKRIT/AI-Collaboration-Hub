> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX (Gx9)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | MCT-F02/F03/F04 all directly touch financial structure. |
| Inventory | **Applicable** | MCT-F01/F05 are inventory-side tenant/access boundaries. |
| Authority (approval/execute/post/reverse) | **Applicable — this Gx's central finding** | MCT-F05: company-level is structural/automatic; warehouse-level requires manual, non-trivial configuration. |
| Period / reversal | **Not evidenced this round** | Out of this Gx's scope. |
| Tenant / Company / Data Scope | **Applicable — this Gx's entire subject; first Gx to evidence this dimension at all** | MCT-F01 is the structural answer every prior Gx left `Unknown`. |
| Audit / Event | **Unknown** | Not evidenced. |
| Automation / Integration | **Applicable** | MCT-F02 is a deliberate, configurable cross-tenant-boundary automation. |
| Cross-module effects | **Applicable** | MCT-F02's stock-move sync directly composes with every valuation-timing finding from Gx1-8. |
