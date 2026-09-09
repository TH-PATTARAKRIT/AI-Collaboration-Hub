# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G0 — Open Assumption & Missing Evidence Register

Status: OPEN ITEMS CONTROLLED / G0 NOT YET CLOSED
Owner: SaaS Team under SMEs Core

## Open Assumptions / Missing Evidence

| ID | Area | Open Item | Required Evidence / Later Owner |
|---|---|---|---|
| OA-01 | Customer billing unit | Exact customer-facing metering units are not frozen | Usage taxonomy + traceability to internal resource cost |
| OA-02 | Package capacity | Included capacity envelopes per package are not frozen | Representative workload telemetry + load testing + commercial simulation |
| OA-03 | Warning thresholds | Exact capacity/wallet warning thresholds are not frozen | Forecast accuracy + customer behavior validation + operational safety |
| OA-04 | Protected Mode | Exact degrade/deny sequence is not frozen | Transaction criticality matrix + safety tests + customer impact analysis |
| OA-05 | Cell headroom | Exact STOP PLACEMENT / EXPAND / MOVE thresholds are not frozen | Stress/soak/noisy-neighbor testing + SRE evidence |
| OA-06 | DB/storage physical amplification | Logical quota to physical storage multiplier unknown | DB/index/WAL/replica/backup/PITR/temporary-space measurement |
| OA-07 | Heavy-job reservation | Exact estimation/reservation algorithm unknown | Workload classification + prediction error testing + queue/worker evidence |
| OA-08 | CPU/RAM enforcement | Per-tenant enforcement mechanism in shared runtime not frozen | Architecture options + benchmark + isolation/noisy-neighbor proof |
| OA-09 | DB connections/query controls | Safe tenant-aware limits not frozen | DB performance tests + query governance evidence |
| OA-10 | Cost-to-Serve | Unit cost by representative tenant profile not yet proven | FinOps model + measured infra cost + protection overhead |
| OA-11 | Standard→Enterprise crossover | Economic/technical crossover not frozen | Mobility test + dual-capacity cost + sustained-load economics |
| OA-12 | Migration method | DB/object-storage migration mechanism and downtime target not frozen | Rehearsal evidence + rollback proof + reconciliation |
| OA-13 | Commercial price | Standard base price 1,500–3,500 THB/month is only direction | Cost-to-Serve + margin simulation + Boss Final Freeze |
| OA-14 | Tax/accounting of wallet | Treatment of prepaid balances not resolved in this architecture evidence | Accounting/tax specialist review before commercial implementation |

## Control Rule

Open items above are not defects in G0 if they are explicitly recognized as later evidence obligations and do not contradict parent decisions.

G0 must not invent answers for OA-01 through OA-14.

## Gate Status

`MISSING EVIDENCE EXPLICITLY IDENTIFIED / NO SILENT ASSUMPTION ALLOWED`
