> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Control Applicability Matrix

# CONTROL APPLICABILITY MATRIX (Gx6)

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | Entire Gx is a financial-control mechanism. |
| Inventory | **Applicable** | Stock Valuation/Variation accounts are inventory-derived. |
| Authority (approval/execute/post/reverse) | **Applicable, partially evidenced** | Lock Dates are a hard authority control (Hard Lock = irreversible); who may set/override a lock is not documented. |
| Period / reversal | **Applicable — this Gx's entire subject** | Accrual entries are explicitly self-reversing (paired Reversal Date). |
| Tenant / Company / Data Scope | **Unknown** | Not evidenced. |
| Audit / Event | **Applicable, partially evidenced** | Hard Lock's inalterability is itself an audit-relevant control; full event trail not documented. |
| Automation / Integration | **Applicable, partially evidenced** | Whether Stock Closing is manual-only or schedulable is unconfirmed (`PCO-F03` UNKNOWN). |
| Cross-module effects | **Applicable — resolves the shared cross-Gx question** | Directly reconciles Gx1/Gx2/Gx4's valuation-timing findings. |
