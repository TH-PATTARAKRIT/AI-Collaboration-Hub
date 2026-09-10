# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G8 — Cost-to-Serve & Load-Test Readiness Draft

Status: DRAFT FOR SPECIALIST REVIEW
Gate: G8 — Cost / Load-Test Readiness
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Gate Purpose

G8 does not freeze package limits or prices. It establishes the measurement, experiment, economic-allocation and decision contracts required before any numerical capacity/package proposal can be trusted.

Mandatory principle:

> No measured workload evidence + no attributable Cost-to-Serve = no numerical Package/Cell/Enterprise crossover freeze.

## 2. Evidence Boundary

G8 distinguishes four evidence states:

1. `ARCHITECTURE ASSUMPTION` — plausible but not measured.
2. `BENCHMARK EVIDENCE` — repeatable lab result with declared environment/workload.
3. `PILOT/PRODUCTION-LIKE EVIDENCE` — representative workload result with tenant-level attribution.
4. `COMMERCIAL FREEZE EVIDENCE` — sufficiently representative, repeatable, reconciled and economically validated for Boss decision.

No benchmark result may be promoted to commercial freeze evidence without provenance, representativeness and reproducibility review.

## 3. Cost-to-Serve Model

Canonical monthly Cost-to-Serve model is:

`CTS_tenant = Direct_tenant + Allocated_shared + Recovery_protection + Platform_operations + External_services - Excluded_platform_defect_cost`

Where:
- `Direct_tenant` = resources directly attributable to one Tenant/workload;
- `Allocated_shared` = fair allocation of shared App/DB/Queue/Cache/Network/Observability capacity;
- `Recovery_protection` = backup, PITR, replica, restore-drill, recovery workspace and resilience overhead;
- `Platform_operations` = unavoidable control-plane/SRE/security/monitoring overhead allocated by governed policy;
- `External_services` = third-party usage actually attributable under verified evidence;
- `Excluded_platform_defect_cost` = retry amplification, bad SQL, leaks, missing indexes, failed internal processing and other platform-caused waste that cannot be customer-charged.

`Customer Chargeable Usage != Cost-to-Serve` remains mandatory.

## 4. Cost Pool Taxonomy

Cost pools to measure independently:
- App compute CPU/time and memory pressure;
- Database compute/connection/query/IO pressure;
- transactional DB storage growth;
- File/Attachment storage;
- Archive storage/retrieval;
- Queue/worker/background processing;
- API/network/egress;
- cache/shared middleware;
- observability/logging/telemetry;
- backup/PITR/replication;
- restore/recovery staging;
- control-plane/placement/routing;
- security/KMS/secret management;
- third-party AI/document/payment/integration services;
- per-Cell fixed operating overhead.

Shared cost allocation must use causal consumption signals where possible; simple equal-per-Tenant allocation is allowed only for genuinely non-variable fixed overhead and must be disclosed.

## 5. Normalized Economic Simulation Before Actual Price Inputs

Until actual hosting/vendor/operations quotations are available, G8 uses a dimensionless `Cost Unit (CU)` to compare architecture alternatives without pretending to know THB pricing.

For scenario `s`:

`CU_s = Σ(resource_quantity_s,r × normalized_unit_weight_r) + fixed_cell_share_s + recovery_share_s + ops_share_s`

Rules:
- CU is an engineering comparison instrument, not customer price.
- Normalized weights must be replaced/recalibrated from actual supplier invoices/quotes before commercial freeze.
- Sensitivity testing must vary each material unit-cost driver independently.
- Any architecture ranking that flips under plausible cost ranges is marked `ECONOMICALLY UNSTABLE` and cannot be frozen.

## 6. Mandatory Workload Scenario Families

Each test campaign must cover at least:

### S1 — Light SME
Low concurrency, small data set, ordinary sales/purchase/accounting usage.

### S2 — Normal SME
Steady interactive workload with moderate background jobs and standard reports.

### S3 — Heavy SME
High concurrency and sustained transaction rate near intended Standard operating envelope.

### S4 — Data / Attachment Heavy
Rapid DB growth, large retained attachments, archive transition, bulk upload/download.

### S5 — API / Integration Heavy
Burst and sustained APIs, webhook fan-out, retries, third-party dependency delay.

### S6 — Manufacturing / Report Heavy
MRP-style transactional bursts, inventory/accounting handoffs, long reports, exports and cost rollups.

### S7 — Correlated Multi-Tenant Burst
Month-end/accounting close, tax/payroll deadline, simultaneous reports/imports across many Tenants in one Cell.

### S8 — Fault / Recovery Load
DB failover, backup lag, restore staging, replay/reconciliation and Cell recovery while normal traffic continues.

### S9 — Movement Load
Tenant Cell-to-Cell movement and Standard-to-Enterprise cutover with queued work, attachments and metering continuity.

### S10 — Sustained Enterprise Candidate
One Tenant whose legitimate sustained workload is large enough to test Standard isolation/economic crossover.

## 7. Test Dimensions

Every scenario records at minimum:
- Tenant count and workload mix;
- concurrent interactive users/requests;
- request arrival distribution and burst shape;
- transaction/script mix;
- DB dataset size and growth rate;
- file/attachment object count and size distribution;
- API/integration rates;
- worker/queue mix and depth;
- report/import/export/heavy job profile;
- backup/archive/recovery activity;
- Cell topology/version/host class;
- CPU, RAM, DB connections, query latency, lock/wait, IOPS/throughput, WAL/log growth;
- queue wait/run/retry/failure;
- app latency percentiles and error rate;
- per-Tenant fairness/noisy-neighbor indicators;
- physical storage amplification;
- network/egress;
- recovery target vs achieved RPO/RTO where applicable;
- measured CU and attributable cost-driver variance.

## 8. Load Shape Requirements

Tests must include:
- steady state;
- step load;
- ramp load;
- burst/spike;
- soak/endurance;
- skewed Tenant distribution;
- correlated Tenant behavior;
- degraded dependency/failure injection;
- placement/movement/recovery operations under load.

Single average TPS/latency numbers are insufficient.

## 9. Reproducibility Contract

Every benchmark run records:
- immutable test run ID;
- Git commit/version under test;
- schema/configuration version;
- infrastructure manifest;
- workload script/version;
- data seed/fixture version;
- warm/cold cache state;
- test start/end timestamps;
- environment background activity;
- monitoring source and sampling interval;
- raw result artifact checksum/location;
- pass/fail disposition and reviewer.

Repeat runs are required until result variance is understood. One favorable run cannot define capacity.

## 10. Safety Envelope Discovery

G8 seeks a multidimensional safe operating region, not a single tenant-count limit.

For each Cell candidate, measure the boundary where one or more material dimensions show unacceptable behavior, including:
- latency/error SLO breach;
- connection/lock queue instability;
- memory/OOM risk;
- CPU starvation;
- storage/IO/WAL/backup backlog;
- worker/queue starvation;
- noisy-neighbor fairness failure;
- recovery reserve erosion;
- movement/recovery workspace insufficiency.

Admission threshold must remain inside the measured failure boundary with empirically justified reserve. Exact reserve remains HOLD until measured.

## 11. Noisy-Neighbor / Fairness Proof

A Standard Cell test must prove that a heavy Tenant cannot materially degrade an unrelated Normal Tenant beyond future agreed service objectives.

Measure per-Tenant:
- latency/error deltas before/during/after heavy neighbor;
- connection wait;
- queue wait;
- resource-share skew;
- retry amplification;
- blocked/deflected heavy workload behavior;
- recovery time after pressure ends.

Test both legitimate heavy workload and platform-defect workload; the latter must be corrected rather than used to justify customer package/Enterprise upsell.

## 12. Mixed-Package vs Package-Class Cell Experiment

G5 Option C (mixed-package Cells) remains the reference hypothesis; Option B (package-class Cells) remains empirical candidate.

A/B comparison must measure:
- utilization;
- dominant-resource fragmentation;
- stranded headroom;
- noisy-neighbor variance;
- package-change-induced movement;
- operational complexity;
- fixed Cell overhead;
- recovery/blast-radius cost;
- movement rate;
- Cost-to-Serve distribution;
- p95/p99 tenant experience.

Selection requires statistically/repeatedly material advantage, not intuition.

## 13. Scale-Up vs Scale-Out Experiment

For each Cell profile, compare:
- vertical resource increase;
- additional Cell scale-out;
- targeted isolated heavy-job lane;
- Enterprise dedicated boundary for sustained heavy Tenant.

Decision uses marginal CU per capacity gain, resilience/blast radius, movement burden and SRE complexity.

## 14. Standard -> Enterprise Crossover Model

Enterprise candidacy must require one or more of:
- sustained measured Standard resource pressure after platform defects are excluded;
- dedicated isolation/SLA/compliance requirement;
- customer-requested dedicated environment;
- lower/more predictable total cost at dedicated boundary;
- Standard movement/fragmentation overhead materially exceeds dedicated cost.

Crossover is modeled as a range, not one universal threshold.

`Enterprise if Dedicated CTS + dedicated ops/risk premium < Standard CTS + shared contention reserve + repeated movement/isolation overhead`, subject also to security/SLA requirements.

## 15. Backup/DR Economic Load

G7 carry-forward is mandatory. Measure:
- backup amplification ratio;
- WAL/archive throughput and backlog;
- replica overhead;
- restore workspace peak;
- restore/replay throughput;
- Tenant-selective extraction/reconciliation duration;
- concurrent Cell recovery capacity;
- tamper-resistant copy overhead;
- restore-drill labor/automation cost;
- target vs achieved RPO/RTO.

These are platform Cost-to-Serve inputs and cannot be naively mapped to customer logical storage quota.

## 16. Metering / Wallet Load Proof

G6 economic evidence must test:
- event ingestion throughput;
- dedupe/idempotency under retries;
- entitlement/rule lookup overhead;
- reservation contention;
- wallet authorization concurrency;
- reconciliation backlog;
- Cell movement/recovery replay without double charge;
- dashboard aggregation cost.

Metering platform inefficiency remains platform CTS unless an explicit disclosed commercial unit exists.

## 17. Test Tool Neutrality

G8 does not freeze a load-test tool. Suitable tools may include application-level load generators plus database-specific tools.

PostgreSQL `pgbench` can measure database transaction rate/latency with custom scripts, concurrent clients, rate-limited arrival and detailed failure/retry statistics, but PostgreSQL documentation explicitly warns that meaningless benchmarks are easy to produce and recommends sufficiently long/repeated representative tests. It is therefore a component benchmark only, not ERP end-to-end proof.

Source: https://www.postgresql.org/docs/18/pgbench.html

## 18. External Architecture/Economic Evidence

AWS SaaS Lens states that multi-tenant cost analysis requires tenant-level consumption attribution and correlation of consumption with infrastructure cost; shared resources require application-level instrumentation rather than relying only on infrastructure tags.
Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/expenditure-awareness.html

AWS SaaS Lens also treats tenant activity/consumption telemetry as necessary to understand how each Tenant imposes load and to support metering/tiering decisions.
Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-activity-and-consumption.html

Azure Architecture Center Deployment Stamps identifies independent stamps/cells as a horizontal scaling and blast-radius containment pattern, but notes scale-up within a single instance can also be valid; this supports explicit scale-up-vs-scale-out economic testing rather than assuming either approach.
Source: https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp

Azure Noisy Neighbor guidance describes pooled resources as economically efficient but requires quotas/throttling/governance because one Tenant can degrade others.
Source: https://learn.microsoft.com/en-gb/azure/architecture/antipatterns/noisy-neighbor/noisy-neighbor

## 19. G8 Evidence Artifacts Required Before Numerical Freeze

Before any numerical Package/Cell proposal may reach Boss Final Freeze, evidence must include:
- workload catalog and scripts;
- representative data fixtures;
- environment manifest;
- per-run immutable results;
- repeatability/variance analysis;
- tenant fairness/noisy-neighbor evidence;
- failure/recovery evidence;
- movement evidence;
- physical amplification evidence;
- cost-pool attribution;
- actual supplier/infrastructure unit-cost source;
- scenario Cost-to-Serve distribution;
- sensitivity analysis;
- mixed-vs-package-class comparison;
- scale-up-vs-scale-out comparison;
- Enterprise crossover analysis;
- unresolved confidence limits.

## 20. Draft G8 Disposition

Architecture and test-readiness model can progress to Specialist Review.

Numerical Package limits, Tenant/Cell count, CPU/RAM, DB/File quotas, thresholds, prices, target margin and Enterprise crossover numbers remain `HOLD — MEASUREMENT REQUIRED`.
