# 24 — Unresolved Evidence Register

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `HONEST, CONSOLIDATED LIST — SUBSTANTIAL BY EXPECTATION, NOT BY FAILURE`

---

## 1. Why This Register Is Long

Per governing brief rule #3, no code/DB access exists for this session, and public documentation for a maintenance/equipment/asset domain does not reach implementation-level mechanism detail on many points. A substantial `UNRESOLVED` list is expected and is stated plainly here rather than concealed or thinned out by overconfident inference.

## 2. Consolidated Register

| ID | Item | Source File(s) | Severity | What Would Resolve It |
|---|---|---|---|---|
| UE-01 | Native Equipment↔Asset link — exists or not | `04`, `11`, `19`, `20` (CR-01) | `BLOCKING` | Live instance inspection across versions; or an official documentation page not yet located |
| UE-02 | Native Equipment↔Product link | `04`, `05`, `20` (CR-02) | `MATERIAL` | Live instance inspection |
| UE-03 | Equipment status/state single-field enum, exact values | `04` | `MATERIAL` | Live instance inspection or a documentation page specifically on equipment lifecycle states |
| UE-04 | Equipment usage/meter/runtime field | `04` | `MATERIAL` | Live instance inspection |
| UE-05 | Equipment↔Work Center enforced cardinality | `04`, `11` | `MATERIAL` | Live instance inspection or schema-level documentation |
| UE-06 | Maintenance Request cost field, existence | `06` | `MATERIAL` | Live instance inspection |
| UE-07 | Any maintenance-cost-to-production-cost linkage in any edition/module not searched this session | `06`, `12` | `BLOCKING` for Hypothesis-A-adjacent design | Broader search across enterprise/paid editions and third-party modules; live instance inspection |
| UE-08 | Exact day-count convention for "Based on days per period" prorata (actual/365, actual/actual, 30/360) | `07`, `08` | `MATERIAL` | Direct documentation page with a worked example, or live instance testing |
| UE-09 | Last-period/disposal-date prorata mechanics | `07` | `MATERIAL` | Direct documentation or live instance testing |
| UE-10 | Leap-year handling in depreciation schedule | `07` | `MATERIAL` | Direct documentation or live instance testing |
| UE-11 | Rounding rule for depreciation entries | `07` | `WATCH` | Direct documentation or live instance testing |
| UE-12 | Pause/resume behavior for an Asset's depreciation schedule | `07` | `MATERIAL` | Direct documentation or live instance testing |
| UE-13 | Exact GL account pairing for Modify Depreciation (increase and decrease) | `07`, `18` | `MATERIAL` | Direct documentation with worked journal entries |
| UE-14 | Exact GL account pairing and computation for disposal gain/loss | `09`, `18` | `MATERIAL` | Direct documentation with worked journal entries |
| UE-15 | Whether the annual useful-life/residual-value review (IAS 16 requirement) is fulfilled by the documented Modify action or is unsupported | `09` | `MATERIAL` | Direct documentation or live instance testing against IAS 16's specific annual-review workflow expectation |
| UE-16 | Blank-field fallback behavior for Asset Model's Fixed Asset/Depreciation/Expense accounts | `03` | `MATERIAL` | Direct documentation or live instance testing |
| UE-17 | Analytic distribution field presence on the asset-model-equivalent record | `03` | `WATCH` | Direct documentation |
| UE-18 | Multi-company scoping of the asset-model-equivalent record | `03` | `WATCH` | Direct documentation |
| UE-19 | Asset Model → Asset inheritance/override mechanics, effective-dating | `03`, `21` (BA-08) | `BLOCKING` for the asset-model-target-control-point decision | Direct documentation or live instance testing |
| UE-20 | Royal Decree number governing Thai depreciation caps (145 vs. 620/473 discrepancy) | `08`, `16`, `20` (CR-03) | `BLOCKING` | Direct retrieval and reading of the gazetted decree text |
| UE-21 | Whether Thai "daily calculation" applies to tax depreciation only, accounting depreciation only, or both | `08`, `16`, `20` (CR-04) | `MATERIAL` | Primary Revenue Department / TFAC source retrieval |
| UE-22 | Thai disposal/write-off deductibility documentation requirements for fixed assets | `16` | `MATERIAL` | Revenue Department source retrieval |
| UE-23 | Thai tax treatment of gain on asset disposal | `16` | `MATERIAL` | Revenue Department source retrieval |
| UE-24 | Gazetted TAS 16 Thai-language standard text | `15`, `16` | `MATERIAL` | TFAC direct source retrieval |
| UE-25 | Gazetted TAS 2 Thai-language standard text | `15` | `WATCH` (secondary to this package's primary object) | TFAC direct source retrieval |
| UE-26 | Reference-ERP Off-Balance/statistical account mechanism — presence or absence | `14`, `23` | `MATERIAL` — search this session was narrower than other files | Dedicated follow-up documentation search or live instance inspection |
| UE-27 | Production-quantity (units-of-production) depreciation/allocation method — reference-ERP support | `22` (T15) | `MATERIAL` | Direct documentation search specifically for this method |
| UE-28 | Equipment-transfer-between-Work-Centers effect on historical cost attribution | `22` (T18) | `MATERIAL` | Direct documentation or live instance testing |
| UE-29 | Termination condition for a post-depreciation internal usage charge (when does it stop accruing) | `13`, `22` (T09) | `MATERIAL` | Boss decision — this is a design gap, not a research gap; no source anywhere specifies it |

## 3. Roll-Up

| Severity | Count |
|---|---:|
| `BLOCKING` | 4 (UE-01, UE-07, UE-19, UE-20) |
| `MATERIAL` | 21 |
| `WATCH` | 4 |
| **Total** | **29** |
| **Resolved by this session** | **0** |

## 4. What Would Meaningfully Reduce This List

Live reference-ERP instance access (not available this session); direct retrieval and reading of primary Thai statutory texts (Royal Decree, Revenue Department rulings, TFAC TAS 16/TAS 2 gazetted text) rather than secondary summaries; a broader documentation search covering enterprise/paid editions and third-party modules for the maintenance-cost-integration and off-balance-mechanism questions specifically.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
