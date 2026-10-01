# Correction packet B01-R1 — control-document lineage restoration

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Boundary B01 (`1c7a8e8e`); corrections originally applied in place at `4a4f39cf` and `c348a8c8`. Request CR-011 · CORRECTION_REQUIRED · Material.

| Superseded statement (original, commit `1c7a8e8e`) | Status | Corrected statement | Evidence |
|---|---|---|---|
| "perpetual-valuation accounting flag is OFF (`anglo_saxon_accounting` = false)" | SUPERSEDED | The company valuation-mode field is `inventory_valuation` = periodic with closing period manual; the anglo-saxon accounting flag is a different setting (= false) | source `stock_account/models/res_company.py:29` (valuation-mode field); restored dump company row; finding by U10 (CAP-U10-02), re-verified by controller |
| "behavior that depends on valuation mode is CONDITIONAL on the perpetual-valuation setting, which is OFF" | SUPERSEDED-IN-PART | Conditional on the valuation-mode setting, which is periodic here | as above |
| "181 under `account`" (chart-loader records) | SUPERSEDED | 179 (147 accounts, 18 taxes, 7 journals, 5 tax groups, 2 reconcile models); the earlier figure wrongly included 2 cron-generated server actions | dump query by model; U13 observation |
| B01-U05 "closing job is active while the perpetual-valuation flag is off" | SUPERSEDED | The job only processes companies whose closing period is daily/monthly; this company is manual, so nothing is processed | U10 CAP-U10-04 |

`WORKER_SPEC_L2_L3.md` also described the state as "perpetual-valuation flag OFF": still true in effect (periodic) but ambiguous wording; workers used the source-derived terms afterwards.
