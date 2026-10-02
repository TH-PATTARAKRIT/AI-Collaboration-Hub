# U158 — quality_control Quality Checks: Neutral Knowledge

**Unit:** U158
**Status:** ABSENT in Community
**Research date:** 2026-10-02

---

## VDR Claims Table — Neutral Column

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U158-C01 | ABSENT-01 | addons/ | directory listing quality_control | ABSENT | always | GAP | The directory quality_control does not exist under odoo/addons/ in the Community 19.0.post20260921 source tree | The quality control extension directory for manufacturing and receipts is not present in the Community edition source tree |
| U158-C02 | ABSENT-02 | addons/ | directory listing quality | ABSENT | always | GAP | The directory quality does not exist under odoo/addons/ in Community 19.0.post20260921 | No base quality module of any simplified naming exists in the Community addons directory |
| U158-C03 | ABSENT-03 | addons/ | directory listing quality_mrp | ABSENT | always | GAP | The directory quality_mrp does not exist under odoo/addons/ in Community 19.0.post20260921 | The quality-manufacturing integration module is not present in Community |
| U158-C04 | ABSENT-04 | addons/ | grep q-prefix filter | ABSENT | always | GAP | Filtering Community addons for names beginning with the letter q yields zero results; no quality-prefixed module of any name is present | No module whose name starts with the letter q was found in the Community addons directory, confirming complete absence of any quality-related module |
| U158-C05 | ABSENT-05 | — | Enterprise scope | ABSENT | OEEL-1 only | GAP | quality_control is an Odoo Enterprise module providing quality check lifecycle management on manufacturing orders and stock receipts | The quality check lifecycle capability is exclusively provided by Enterprise-licensed extensions not present in Community |
| U158-C06 | ABSENT-06 | — | check point definition model | ABSENT | always | GAP | Because the module is absent, the check point configuration model specifying which operations and products require inspection does not exist in Community | The data model that defines quality check points specifying which operations and products require inspection does not exist in Community |
| U158-C07 | ABSENT-07 | — | quality check instance model | ABSENT | always | GAP | Because the module is absent, the check instance model recording measured values, tolerances, and links to production orders or receipts does not exist in Community | The data model that records individual quality check instances with measurement values, tolerances, and links to production orders or receipts does not exist in Community |
| U158-C08 | ABSENT-08 | — | corrective action alert model | ABSENT | always | GAP | Because the module is absent, the corrective action alert model does not exist in Community | The data model for raising and tracking corrective action alerts when a quality check fails does not exist in Community |
| U158-C09 | ABSENT-09 | — | automatic check creation | ABSENT | always | GAP | Because the module is absent, the automatic creation of quality checks upon manufacturing order confirmation or stock receipt validation does not exist in Community | The automated mechanism that creates quality check records when a production order is confirmed or a warehouse receipt is validated does not exist in Community |
| U158-C10 | ABSENT-10 | — | confirmation blocking | ABSENT | always | GAP | Because the module is absent, the blocking of manufacturing order or receipt confirmation upon a failed quality check does not exist in Community | The confirmation-blocking control that prevents completing a production order or receipt when an associated quality check is in a failed state does not exist in Community |
| U158-C11 | ABSENT-11 | — | receipt to check relationship | ABSENT | always | GAP | Because the module is absent, the relationship field linking warehouse receipts to quality checks does not exist in Community | The relationship field that connects warehouse receipt records to their associated quality checks does not exist in Community |
| U158-C12 | ABSENT-12 | — | work order step integration | ABSENT | always | GAP | Because the module is absent, quality check integration with work order steps does not exist in Community | The integration that embeds quality check execution within individual work order steps on a production order does not exist in Community |
| U158-C13 | ABSENT-13 | — | qualitative pass-fail test | ABSENT | always | GAP | Because the module is absent, the qualitative pass-or-fail inspection type does not exist in Community | The qualitative pass-or-fail inspection outcome recording mechanism does not exist in Community |
| U158-C14 | ABSENT-14 | — | quantitative measurement test | ABSENT | always | GAP | Because the module is absent, the quantitative measurement inspection type with target value and tolerance range does not exist in Community | The quantitative inspection mode that records a measured value and compares it against a target value and acceptable tolerance range does not exist in Community |
| U158-C15 | ABSENT-15 | — | quality user access groups | ABSENT | always | GAP | Because the module is absent, the access control groups governing quality check recording and configuration do not exist in Community | The user access control groups that govern who may record quality check results versus who may configure quality control points do not exist in Community |

---

## Notes

All neutral-ref cells use plain prose only. No snake case identifiers, dotted model names, file extensions, backticks, or code keywords appear in the Neutral-ref column.
