# U158 — quality_control Quality Checks on Manufacturing/Receipts (L3)

**Unit:** U158
**Title:** quality_control — quality checks on manufacturing/receipts (or ABSENT)
**Status:** ABSENT — module not present in Community edition
**Research date:** 2026-10-02
**Researcher:** DeepSeek worker (STATE03 VDR)

---

## Presence Check

```
ls "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/quality_control"
# → No such file or directory (exit code 1)

ls "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/quality"
# → No such file or directory (exit code 1)

ls "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/quality_mrp"
# → No such file or directory (exit code 1)
```

Community addons listing filtered for names beginning with `q` returns zero results. No quality-prefixed module of any name exists in the Community 19.0.post20260921 source tree.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U158-C01 | ABSENT-01 | addons/ | directory listing quality_control | ABSENT | always | GAP | The directory `quality_control` does not exist under `odoo/addons/` in the Community 19.0.post20260921 source tree | The quality control extension directory for manufacturing and receipts is not present in the Community edition source tree |
| U158-C02 | ABSENT-02 | addons/ | directory listing quality | ABSENT | always | GAP | The directory `quality` does not exist under `odoo/addons/` in Community 19.0.post20260921 | No base quality module of any simplified naming exists in the Community addons directory |
| U158-C03 | ABSENT-03 | addons/ | directory listing quality_mrp | ABSENT | always | GAP | The directory `quality_mrp` does not exist under `odoo/addons/` in Community 19.0.post20260921 | The quality-manufacturing integration module is not present in Community |
| U158-C04 | ABSENT-04 | addons/ | grep ^q filter | ABSENT | always | GAP | Filtering Community addons for names beginning with the letter q yields zero results; no quality-prefixed module of any name is present | No module whose name starts with the letter q was found in the Community addons directory, confirming complete absence of any quality-related module |
| U158-C05 | ABSENT-05 | — | Enterprise scope | ABSENT | OEEL-1 only | GAP | `quality_control` is an Odoo Enterprise module (OEEL-1 license) providing quality check lifecycle management on manufacturing orders and stock receipts | The quality check lifecycle capability — covering check point definition, automatic check creation on production orders and receipts, pass/fail recording, and blocking confirmation on failure — is exclusively provided by Enterprise-licensed extensions |
| U158-C06 | ABSENT-06 | — | quality.point model | ABSENT | always | GAP | Because the module is absent, the `quality.point` model (picking_type_id, product_id, test_type, measure_on) does not exist in Community | The data model that defines quality check points specifying which operations and products require inspection does not exist in Community |
| U158-C07 | ABSENT-07 | — | quality.check model | ABSENT | always | GAP | Because the module is absent, the `quality.check` model (lot_id, picking_id, workorder_id, measure, norm, tolerance_min, tolerance_max) does not exist in Community | The data model that records individual quality check instances with measurement values, tolerances, and links to production orders or receipts does not exist in Community |
| U158-C08 | ABSENT-08 | — | quality.alert model | ABSENT | always | GAP | Because the module is absent, the `quality.alert` model for corrective action tracking does not exist in Community | The data model for raising and tracking corrective action alerts when a quality check fails does not exist in Community |
| U158-C09 | ABSENT-09 | — | auto-creation logic | ABSENT | always | GAP | Because the module is absent, the automatic creation of quality checks upon manufacturing order confirmation or stock receipt validation does not exist in Community | The automated mechanism that creates quality check records when a production order is confirmed or a warehouse receipt is validated does not exist in Community |
| U158-C10 | ABSENT-10 | — | block mechanism | ABSENT | always | GAP | Because the module is absent, the blocking of manufacturing order or stock picking confirmation upon a failed quality check does not exist in Community | The confirmation-blocking control that prevents completing a production order or receipt when an associated quality check is in a failed state does not exist in Community |
| U158-C11 | ABSENT-11 | — | stock.picking integration | ABSENT | always | GAP | Because the module is absent, the `check_ids` Many2many field on `stock.picking` linking receipts to quality checks does not exist in Community | The relationship field that connects warehouse receipt records to their associated quality checks does not exist in Community |
| U158-C12 | ABSENT-12 | — | mrp_workorder integration | ABSENT | always | GAP | Because the module is absent, quality check integration with work order steps in manufacturing does not exist in Community | The integration that embeds quality check execution within individual work order steps on a production order does not exist in Community |
| U158-C13 | ABSENT-13 | — | test type passfail | ABSENT | always | GAP | Because the module is absent, the pass/fail qualitative test type for quality checks does not exist in Community | The qualitative pass-or-fail inspection outcome recording mechanism does not exist in Community |
| U158-C14 | ABSENT-14 | — | test type measure | ABSENT | always | GAP | Because the module is absent, the quantitative measure test type with norm and tolerance range for quality checks does not exist in Community | The quantitative inspection mode that records a measured value and compares it against a target value and acceptable tolerance range does not exist in Community |
| U158-C15 | ABSENT-15 | — | security groups | ABSENT | always | GAP | Because the module is absent, the quality_user and quality_manager security groups do not exist in Community | The user access control groups that govern who may record quality check results versus who may configure quality control points do not exist in Community |

---

## Summary

`quality_control`, `quality`, and `quality_mrp` are all absent from Odoo Community 19.0.post20260921. Quality control in Odoo is an Enterprise-only capability. The entire lifecycle — check point definition, automatic check instantiation on manufacturing orders and stock receipts, pass/fail and quantitative measurement recording, corrective action alerts, and confirmation blocking on failure — is implemented exclusively in Enterprise modules not present in the Community source tree.

**Gap severity:** HIGH — SMEsPlus will require a custom Community implementation or alternative quality management approach for any quality inspection workflow.
