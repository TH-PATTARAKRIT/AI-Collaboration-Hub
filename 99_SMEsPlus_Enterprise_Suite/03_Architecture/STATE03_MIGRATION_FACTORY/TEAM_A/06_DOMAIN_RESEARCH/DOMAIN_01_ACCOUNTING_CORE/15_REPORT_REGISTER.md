> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 15 — REPORT REGISTER

Reporting is a deferred domain. Only touchpoints are recorded.

| ID | Touchpoint | Status |
|---|---|---|
| RPT-01 | `account_report.py` exists inside the readable `account` module (report definition scaffolding) | Present, not analysed — deferred |
| RPT-02 | `account_reports` — the reporting engine | **OEEL-1 BLACK-BOX**, not read |
| RPT-03 | Trial balance / general ledger / balance sheet / P&L | Provided by RPT-02, therefore unobservable at source |
| RPT-04 | `include_initial_balance` on account type drives report carry-forward behaviour | Observed at model level (SE-18) |
| RPT-05 | `account_account_tag` used for reporting classification | Observed structurally |
| RPT-06 | Thai statutory reports | Deferred to Tax/Reporting domain; known to depend on the black-box engine |

**Consequence.** Core accounting *reporting behaviour* cannot be evidenced from source in this
system, because the engine is proprietary. Only the data shape that feeds it is observable.
This mirrors a limitation already recorded in prior governance evidence and is repeated here as
a domain fact, not as a new claim.
