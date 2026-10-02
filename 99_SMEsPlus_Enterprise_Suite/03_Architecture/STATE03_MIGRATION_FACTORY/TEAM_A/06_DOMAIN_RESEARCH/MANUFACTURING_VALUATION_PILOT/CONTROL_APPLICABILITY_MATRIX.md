> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX (Gx7)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | MFG-F01/F02/F03 are all direct financial-posting functions. |
| Inventory | **Applicable** | Raw material and finished-good stock truth both change through this flow. |
| Authority (approval/execute/post/reverse) | **Applicable, partially evidenced** | MFG-F03's manual post/reverse is itself an authority-gated action; who may trigger it is not documented. |
| Period / reversal | **Applicable** | MFG-F03 is explicitly this Gx's own period/interim-timing mechanism, self-reversing in spirit like Gx6's accrual. |
| Tenant / Company / Data Scope | **Unknown** | Not evidenced. |
| Audit / Event | **Unknown** | Not evidenced beyond the named events themselves. |
| Automation / Integration | **Applicable** | MFG-F01/F02 are documented as automatic (not manual triggers), a genuine automation. |
| Cross-module effects | **Applicable — confirms and generalizes the Gx6 rule** | The clearest evidence yet that "post at financial-transaction time" generalizes correctly across a third distinct event type. |
