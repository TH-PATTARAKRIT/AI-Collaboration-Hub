> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx9)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-MCT-01 | Inter-company stock-move sync's valuation treatment (independent per-company computation vs. copied) not documented | Directly relevant to this Deep Study's whole valuation-timing thread across a company boundary | **Targeted Validation Needed — flagged as high-value** | Documentation pass specifically on inter-company stock valuation, or runtime evidence |
| GAP-MCT-02 | No official documentation for warehouse-level user record-rule mechanics (only corroborating community/marketplace evidence) | `MCT-F05`'s mechanism itself remains undocumented at official-source tier | **Non-blocking** | Odoo developer/technical documentation pass (different doc tree than the applications docs used so far), or runtime evidence |
| GAP-MCT-03 | Whether consolidation reporting handles inter-company eliminations automatically | `MCT-F04` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-MCT-04 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN              : 4
TARGETED VALIDATION    : 1 (GAP-MCT-01)
NON-BLOCKING           : 3 (GAP-MCT-02, 03, 04)
```
