# SMEsPlus Community19 - G13-G16 A1 Roster Reconciliation and Static Intake V1.00

Date: 2026-09-24
Mode: A1 SOURCE EVIDENCE ONLY
Boss boundary: NO A2 RUNTIME / NO A3 / NO MASTER

## 1. Current governed group counts

| Group | Name | Current governed count | A1 disposition |
|---|---|---:|---|
| G13 | PEOPLE | 29 | ACTIVE - roster reconciliation in progress |
| G14 | COLLABORATION | 16 | ACTIVE - roster reconciliation in progress |
| G15 | DASHBOARD_REPORT | 11 | ACTIVE - roster reconciliation in progress |
| G16 | TECHNICAL_INTEGRATION | 19 | ACTIVE - roster reconciliation in progress |

These counts are planning/control counts, not Formal Coverage.

## 2. Evidence reconciled in this run

1. Current A1 control index records G13=29, G14=16, G15=11, G16=19 inside the Boss-approved 247 current-study module set.
2. Historical Group Structure V2 evidence measured the installed 299-module set and referenced `GROUP_STRUCTURE_V2_CORE.tsv` with SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`.
3. Historical Group Structure V2 recorded G13=29, G14=16, G15=11, G16=20.
4. Therefore G13-G15 group counts are unchanged between that historical mapping and the current A1 control index, while G16 has a one-row delta (20 -> 19).
5. The exact G16 row removed/reclassified by the current scope rebase is NOT proven by the evidence currently reachable. It must not be guessed.
6. The authoritative Community19 source root `Odoo Community 19.0.post20260921` is not reachable because the authorized desktop source device is offline.
7. Exact current technical-name membership for G13-G16 therefore remains CURRENT-SOURCE RE-ANCHOR PENDING.

## 3. Static source-study targets already supported by prior evidence

The following are source-study targets/carry-forward leads only. They are NOT promoted here as the exact current G13-G16 roster.

### G13 PEOPLE - source-trace leads
- `hr.employee`, `hr.department`, `hr.job` under `addons/hr`
- attendance concepts under `addons/hr_attendance`: `hr.attendance`, `check_in`, `check_out`, overlap/constraint handling
- time-off concepts under `addons/hr_holidays`: `hr.leave`, `hr.leave.type`, `hr.leave.allocation`, approval/validation/day calculations
- expense concepts under `addons/hr_expense`: `hr.expense`, `hr.expense.sheet`, submit/approve/accounting/analytic links
- recruitment concepts under `addons/hr_recruitment`: `hr.applicant`, `hr.job`, stages and employee creation/hired transition
- cross-domain identity links: employee -> user -> partner -> resource -> calendar

### G14 COLLABORATION - evidence boundary
- Exact current technical roster not yet recoverable from the controlled mapping bytes.
- No module is credited to G14 in this run without exact roster evidence.

### G15 DASHBOARD_REPORT - evidence boundary
- Exact current technical roster not yet recoverable from the controlled mapping bytes.
- Historical/preliminary inventories mention dashboard/report components, but they are mixed-source and cannot establish current Community19 G15 membership.
- No module is credited to G15 in this run without exact roster evidence.

### G16 TECHNICAL_INTEGRATION - evidence boundary
- Current count is 19; historical Group Structure V2 count was 20.
- Preliminary/mixed inventories mention technical/integration components, but they cannot identify the current 19-row governed roster.
- `cloud_storage_google` is separately governed BLOCKED-TECHNICAL in the current scope bookkeeping; this run does NOT assert that it is the one-row G16 delta without direct roster evidence.
- No module is credited to G16 in this run without exact roster evidence.

## 4. Evidence quality and contradiction register

| ID | Finding | State | Gate impact |
|---|---|---|---|
| G13-16-A1-001 | Current counts G13=29/G14=16/G15=11/G16=19 are controlled in the A1 index | VERIFIED CONTROL FACT | permits group-level A1 activation |
| G13-16-A1-002 | Historical mapping file hash is known but file bytes are not reachable in this run | PARTIAL | exact roster cannot be reconstructed from hash alone |
| G13-16-A1-003 | G16 historical count 20 vs current 19 | OPEN CONTRADICTION / MATERIAL DELTA | exact changed row must be identified before roster seal |
| G13-16-A1-004 | Authoritative current Community19 source root unavailable | SOURCE ACCESS BLOCKED | byte-level source re-anchor pending |
| G13-16-A1-005 | Historical HR/source-learning material contains useful trace targets but is not current roster proof | SECONDARY EVIDENCE ONLY | no membership credit |

## 5. Next A1-only route

1. Continue G13-G16 in parallel; do not wait for earlier groups.
2. Recover exact `GROUP_STRUCTURE_V2_CORE.tsv` bytes or an equivalent Boss-controlled 247-row current roster artifact.
3. Reconcile G13-G16 technical names against the current 247 current-study set and separately governed `cloud_storage_google` row.
4. Resolve the exact G16 20 -> 19 membership delta without inference.
5. When the authoritative Community19 source root becomes reachable, re-anchor every admitted module to current manifest/source bytes and extract models, fields, rules, states, security, config, cron/background mechanisms, routes/controllers, UI static surfaces, tests/migrations/data, direct/reverse dependencies and cross-module handoffs.
6. Keep A2 Runtime, A3, MASTER, GMVQ answering and Formal Coverage prohibited until a new explicit Boss order.

Status: A1 ACTIVE / ROSTER RECONCILIATION IN PROGRESS / CURRENT-SOURCE RE-ANCHOR PENDING
