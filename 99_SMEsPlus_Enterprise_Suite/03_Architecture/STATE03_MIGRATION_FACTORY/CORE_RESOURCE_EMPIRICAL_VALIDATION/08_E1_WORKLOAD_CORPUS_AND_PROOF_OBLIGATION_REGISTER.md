# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E1 — Workload Corpus & Proof Obligation Register

Status: E1 DRAFT FOR REVIEW
Jira: ERPPLUS-156
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Purpose

Define what SMEsPlus must test before any resource-capacity number can become a numerical candidate.

This register intentionally avoids unsupported transaction rates, concurrency counts, GB values, CPU/RAM values and package prices. Those values must be generated from measurement, not inserted as assumptions and later mistaken for evidence.

## 2. Canonical Workload Families

### WF-01 — LIGHT SME
Business behavior:
- low-to-moderate interactive activity;
- small active dataset;
- low attachment growth;
- infrequent heavy reports/import/export;
- ordinary API/integration use.

Proof obligations:
- baseline latency/error profile;
- minimum platform overhead per Tenant;
- idle/background cost;
- fairness under neighboring heavier Tenants.

### WF-02 — NORMAL SME
Business behavior:
- sustained daily sales/purchase/inventory/accounting traffic;
- regular attachments;
- scheduled reports/background jobs;
- moderate API/integration use.

Proof obligations:
- sustainable interactive performance;
- DB/worker/queue behavior;
- expected resource distribution;
- backup/recovery burden;
- baseline CTS distribution.

### WF-03 — HEAVY SME
Business behavior:
- high sustained transaction activity;
- larger working set;
- frequent reporting/batch processing;
- higher concurrency and integration traffic.

Proof obligations:
- sustained shared-cell safety;
- dominant-resource identification;
- fairness impact on other Tenants;
- targeted-isolation effectiveness;
- Enterprise-candidacy evidence after platform-defect exclusion.

### WF-04 — DATA / ATTACHMENT HEAVY
Business behavior:
- high DB growth and/or document/image/file retention;
- frequent uploads/downloads;
- archive lifecycle activity;
- restore/export operations.

Proof obligations:
- logical-vs-physical amplification;
- object/DB interaction cost;
- upload/download admission behavior;
- backup/restore workspace and bandwidth burden;
- archive economics.

### WF-05 — API / INTEGRATION HEAVY
Business behavior:
- high inbound/outbound API volume;
- webhook/event traffic;
- integration retries/failures;
- bursty partner systems.

Proof obligations:
- rate/admission/fairness behavior;
- retry amplification classification;
- idempotency/reconciliation cost;
- network/egress and queue pressure;
- external dependency degradation behavior.

### WF-06 — MANUFACTURING / REPORT HEAVY
Business behavior:
- inventory/movement/costing-intensive processes;
- BOM/MRP-like calculations where applicable;
- large operational and financial reports;
- heavy background recalculation/export workloads.

Proof obligations:
- interactive-vs-heavy workload isolation;
- DB lock/query behavior;
- worker/queue saturation and drain;
- memory/temporary workspace amplification;
- targeted isolated lane value.

### WF-07 — CORRELATED MULTI-TENANT BURST
Examples:
- month-end accounting close;
- tax/report deadlines;
- payroll-like deadlines where applicable;
- synchronized import/export or integration windows;
- morning/opening-hour traffic peaks.

Proof obligations:
- Cell coincident-peak behavior;
- stop-placement/admission control;
- fairness during legitimate simultaneous bursts;
- recovery time after burst;
- reserve adequacy.

### WF-08 — FAILURE / RECOVERY LOAD
Behavior:
- normal traffic while selected dependencies degrade;
- DB/storage latency;
- queue backlog;
- object-store partial failure;
- network impairment;
- telemetry/metering degradation;
- Cell/placement/control-plane recovery;
- backup/restore contention.

Proof obligations:
- integrity preservation;
- bounded blast radius;
- no false capacity from stale telemetry;
- retry amplification control;
- recovery reserve;
- target-vs-achieved recovery evidence.

### WF-09 — MOBILITY / PLACEMENT
Behavior:
- Cell-to-Cell move;
- Standard->Enterprise migration;
- long-running job/session during movement;
- placement authority switch;
- post-cutover observation.

Proof obligations:
- no split brain;
- Tenant/business identity continuity;
- DB/file/job/integration continuity;
- usage/wallet/billing continuity;
- source release safety;
- temporary dual-capacity cost.

### WF-10 — SUSTAINED ENTERPRISE CANDIDATE
Behavior:
- workload intentionally maintained beyond the expected economical/safe Standard envelope;
- may also include stronger isolation/SLA/recovery requirements.

Proof obligations:
- distinguish legitimate sustained demand from platform defect;
- compare Standard shared burden vs dedicated resource burden;
- derive reason-coded crossover range;
- verify same Core semantics.

## 3. Mandatory Load Shapes

Each applicable family is exercised using relevant combinations of:
- steady;
- ramp;
- step;
- spike/burst;
- soak/endurance;
- hot-key/data skew;
- cold -> warming -> steady cache phases;
- correlated Tenant burst;
- degraded dependency;
- failure/recovery;
- post-load drain/recovery observation.

No one load shape can establish general capacity.

## 4. Tenant Mix Dimensions

Every production-intent campaign declares:
- Tenant family mix;
- active/inactive Tenant ratio;
- top-Tenant concentration;
- dataset size distribution;
- attachment growth distribution;
- API/integration mix;
- background/heavy-job mix;
- burst correlation;
- working-set skew;
- organizational/company/branch complexity where workload-relevant.

## 5. Business Process Mix

The workload corpus must include representative business actions across applicable core ERP domains rather than synthetic ping-only traffic.

At minimum the final production-intent corpus should cover combinations of:
- authentication/context establishment;
- read/search/list/detail flows;
- create/update controlled business documents;
- approval/control paths where applicable;
- Sales/Purchase/Inventory transaction chains;
- accounting/posting/reconciliation interactions when implemented and safe to test;
- file/attachment upload/download;
- reports/export;
- API/integration;
- background/heavy jobs;
- audit/metering/control overhead.

Exact endpoints/workflows bind to the current implemented SMEsPlus build at execution time.

## 6. Counterfactual Fairness Contract

For each heavy family, compare:

`Normal Tenant baseline without heavy neighbor`
vs
`Same Normal Tenant during heavy-neighbor pressure`
vs
`Post-pressure recovery`.

Record per-Tenant distribution rather than Cell average only.

## 7. Required Result Dimensions

Where material collect:
- request/transaction throughput;
- latency distribution;
- error/failure/retry distribution;
- CPU;
- RAM / OOM pressure;
- DB connection acquisition;
- query latency / locks / waits;
- storage IOPS/throughput;
- WAL/log/backup backlog;
- DB/File/Archive growth;
- worker/queue depth and wait;
- API/network/egress;
- usage/metering/wallet/reconciliation backlog;
- Tenant fairness delta;
- recovery time;
- resource amplification;
- Cost-to-Serve inputs;
- generator/instrumentation headroom.

## 8. Claim-to-Proof Mapping

| Claim class | Minimum evidence |
|---|---|
| subsystem performance | component benchmark + version/env binding + repeated runs |
| ERP system capacity | production-intent system benchmark + realistic process/data mix + security/control path |
| Tenant fairness | paired counterfactual + per-Tenant percentiles/errors/waits |
| Cell safe envelope | multi-dimensional sustained evidence + reserve + failure/degraded tests |
| quota candidate | logical usage + physical amplification + UX/CTS evidence |
| RPO/RTO candidate | repeated recovery drills + coherent business truth + target-vs-achieved |
| Cell architecture winner | predeclared A/B metrics + repeated comparable experiments |
| Enterprise crossover | sustained workload + platform-defect exclusion + Standard vs dedicated CTS/ops/isolation/recovery comparison |
| price/margin candidate | current actual cost evidence + commercial/tax inputs + Boss decision |

## 9. E1 Draft Disposition

`WORKLOAD CORPUS = DRAFTED FOR SPECIALIST REVIEW / INDEPENDENT CHALLENGE`.

No numerical load level is frozen by this document.