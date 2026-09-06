# P04 → P08 HANDOFF (Record-to-Report)

**LAYER 2.** Published, not executed.

| # | Evidence | Consequence for P08 | Materiality |
|---|---|---|---|
| 1 | **`P04-F-154`** — all three `account.asset` account fields **exclude `off_balance` by domain** | The Boss policy *"off-balance double entries pair with off-balance"* **cannot be implemented on the asset object.** Any managerial/off-balance internal-usage ledger is a **separate mechanism** needing its own chart structure | **High** — it constrains the chart design, not just P04's |
| 2 | **`P04-F-155`** — `set_to_close` **raises** before the fiscal lock date, while `write()`'s depreciation-account re-assignment **silently skips** locked moves | Two different lock behaviours in one module. Account re-assignment on an asset with posted history applies **partially and silently** | **High** — period integrity |
| 3 | **`P04-F-153`** — the analytic distribution is written to **both** legs of the depreciation entry, so the analytic account nets to zero; and only on **draft** moves | Any P08 report reading analytic balances for depreciation reads **zero**, correctly, from a wiring choice rather than an absence of cost | **High** |
| 4 | `write()` addresses depreciation lines **positionally** (`line_ids[::2]`), assuming exactly two lines in a fixed order | A structural risk to any entry shape that is not the assumed one | **Medium** — recorded, not observed firing |
| 5 | Carried: derecognition entry left in **draft** and silently deletable; blank account **drops a leg** — cause now known (`CQ-P04-01`) | Financial-statement completeness at disposal | **High**, previously published |

**No P08 work was performed.** No chart decision is proposed.
