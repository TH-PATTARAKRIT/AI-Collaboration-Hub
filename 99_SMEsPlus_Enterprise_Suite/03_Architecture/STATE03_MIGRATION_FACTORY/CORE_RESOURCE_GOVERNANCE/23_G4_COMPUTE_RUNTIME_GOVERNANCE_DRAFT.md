# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G4 — Compute / Runtime Governance Draft

Status: EXECUTION DRAFT — SUBJECT TO SPECIALIST REVIEW AND INDEPENDENT CHALLENGE
Gate: G4 — Compute / Runtime Gate
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. G4 Scope and Freeze Boundary

G4 must close the conceptual governance model for CPU, RAM, request concurrency, DB connections, query execution, workers, queues and foreseeable heavy jobs in STANDARD shared Cells.

G4 does NOT freeze:
- CPU or RAM quantities per Package/Tenant/Cell;
- worker counts or queue partitions;
- DB pool size or per-Tenant connection counts;
- timeout values;
- retry/backoff values;
- Kubernetes/Docker/cgroup/process-isolation mechanism;
- Node.js process topology;
- database proxy/pool product;
- queue technology;
- final customer-facing compute charging units;
- G5 Cell headroom thresholds;
- G8 load-test or Cost-to-Serve values.

## 2. Core Constraint

STANDARD is shared-resource multi-tenant. Therefore a logical Tenant compute entitlement cannot be represented as a claim that the Tenant owns fixed physical CPU/RAM inside a shared process unless the later implementation proves such isolation.

Canonical rule:

`Logical Tenant Workload Policy`
-> `Admission / Fair Scheduling / Concurrency / Time / Memory / Query / Queue controls`
-> shared runtime resources
-> measured Tenant-attributable telemetry
-> Cell/platform protection decisions.

## 3. Workload Classes — Draft

Workloads are classified by business-integrity and expected resource behavior, not by customer preference.

1. `CRITICAL INTEGRITY` — actions required to preserve/complete already-valid accounting, inventory, payment, approval or transaction-integrity sequences where interruption could create inconsistency.
2. `NORMAL INTERACTIVE` — ordinary synchronous user/API ERP operations expected to complete within controlled latency/work bounds.
3. `BACKGROUND NORMAL` — scheduled/asynchronous work with bounded impact and no need for immediate user response.
4. `HEAVY CONTROLLED` — predictable workloads capable of material CPU/RAM/DB/IO/queue/worker pressure, such as mass import/export, large report, reconciliation/allocation batch, archive restore, large integration burst or optional AI/document processing.
5. `OPTIONAL / DEFERRABLE` — non-critical work that may be delayed, throttled or rejected first during protection states.

Critical classification is platform-governed and finite. It is not unlimited free capacity.

## 4. CPU Governance

CPU pressure is governed primarily as flow/time/fairness and Cell headroom, not as an unproven per-Tenant hard CPU slice inside a shared process.

Required controls:
- Tenant-attributed request/job execution telemetry;
- request and job concurrency limits;
- bounded synchronous execution time;
- background/heavy-job scheduling classes;
- burst detection distinct from sustained load;
- admission/defer/reject controls before Cell saturation;
- detection of platform inefficiency so bad SQL/code does not become customer usage;
- isolation escalation for workloads that cannot be safely governed in shared execution.

A sustained heavy Tenant may trigger Package/Add-on/Cell-move/Enterprise review, but temporary legitimate bursts alone do not prove Enterprise suitability.

## 5. RAM / Memory Governance

RAM is a shared failure-sensitive resource. The architecture must prevent one request/job/Tenant from creating uncontrolled memory pressure.

Required conceptual controls:
- payload/input size preflight where reasonably estimable;
- streaming/chunking preference for large imports/exports/files;
- bounded batch/page/window sizes;
- per-request/job memory-risk classification;
- materialization avoidance for unbounded result sets;
- heavy-job isolation candidate when memory behavior is not safely governable in shared runtime;
- process/worker health telemetry and controlled restart/failure recovery;
- Cell-level memory headroom and admission protection carried to G5.

No customer may be charged merely because an inefficient SMEsPlus implementation used excess memory.

## 6. Request Concurrency and Runtime Admission

Every execution path must carry Trusted Tenant Context before Tenant-specific governance is applied.

Conceptual admission sequence:

`Request/Job`
-> prove Tenant + actor/service context
-> identify workload class
-> evaluate entitlement/policy
-> evaluate Tenant concurrency/rate state
-> evaluate Cell protection/headroom state
-> if heavy: preflight/reservation as required
-> ADMIT / QUEUE / DEFER / REJECT / REQUIRE CAPACITY ACTION
-> execute
-> emit trusted telemetry/evidence.

Admission decisions require reason codes and traceability.

## 7. Database Connection Governance

DB connections are pooled platform resources and cannot be allowed to scale linearly without control from Tenant request volume.

Required controls:
- centralized/controlled connection acquisition;
- bounded total Cell/app connection pools;
- Tenant-attributable waiting/usage telemetry where feasible;
- prevention of one Tenant monopolizing connection concurrency;
- bounded transaction duration;
- prompt release of connections after transaction scope;
- background/heavy jobs subject to separate concurrency/pool policy;
- connection leaks treated as platform defects;
- admission pressure before DB pool exhaustion.

A logical Tenant entitlement does not imply ownership of dedicated DB connections unless separately contracted/proven.

## 8. Query Governance

Query controls protect correctness and shared capacity without turning engineering defects into customer charges.

Required conceptual controls:
- trusted Tenant scope on every applicable data access path;
- bounded query/result sizes for normal paths;
- statement/operation timeout policy by workload class;
- runaway/long-query detection;
- pagination/batching for large result sets;
- query-cancellation/retry semantics that preserve transaction correctness;
- N+1/missing-index/bad-plan classification as platform inefficiency unless legitimate customer workload remains material after remediation;
- heavy analytical/report queries may be routed to controlled asynchronous paths where semantics permit;
- no automatic retry loop that amplifies failure load indefinitely.

Exact database mechanisms remain open.

## 9. Worker / Queue Governance

Queues absorb asynchronous demand but are not infinite capacity.

Required controls:
- queue item carries canonical Tenant identity and workload class;
- idempotency/deduplication identity for retryable material jobs;
- per-class and Tenant-aware fair scheduling;
- bounded in-flight concurrency;
- retry budget + backoff + dead-letter/held disposition;
- queue-age/lag telemetry;
- poison-job isolation;
- heavy/optional jobs can be deferred before critical/normal work;
- queue admission may stop before physical worker/DB/resource saturation;
- starvation prevention for eligible normal tenants.

Queue depth alone is not a complete capacity metric; service rate, job weight, age and downstream pressure matter.

## 10. Heavy Job Contract

Foreseeably material workloads require controlled preflight.

Candidate sequence:

`Estimate`
-> classify workload
-> validate Tenant entitlement
-> validate prepaid/secured authorization if chargeable
-> validate Cell/platform headroom
-> reserve entitlement/credit/runtime slot where required
-> execute in controlled mode
-> measure actual
-> reconcile/release unused reserve
-> append evidence.

The estimate may be imperfect; the runtime must support checkpoints, bounded chunking or safe cancellation/recovery rather than running unbounded until failure.

## 11. Protection State Behavior

G3 staged states are carried forward:

`NORMAL -> INFORMATION -> WARNING -> CAPACITY ACTION REQUIRED -> PROTECTED MODE -> HARD CAP / EMERGENCY SAFETY`.

At compute/runtime pressure, controls should progressively:
1. reduce optional/heavy concurrency;
2. defer scheduled/background non-critical work;
3. require reservation/capacity action for heavy work;
4. protect critical/normal interactive capacity where technically safe;
5. stop new resource-expanding execution when safety/correctness would be endangered.

Emergency physical safety may veto new work, including critical work, if correctness cannot otherwise be guaranteed.

## 12. Failure and Retry Safety

Retries must not turn transient failure into a retry storm or duplicate business effect.

Required conceptual rules:
- material commands/jobs use idempotency or equivalent duplicate-effect protection;
- retry budgets are finite;
- exponential/backoff/jitter mechanism may be selected later;
- non-retryable business validation failures are not retried automatically;
- partial execution must have explicit reconciliation/recovery state;
- queue redelivery must not duplicate accounting/inventory/payment effects.

## 13. Tenant Fairness / Noisy Neighbor

Fairness is multidimensional and may combine:
- concurrent requests;
- execution time;
- weighted job slots;
- queue service share;
- DB connection pressure;
- query duration;
- memory-risk class;
- API/integration flow;
- sustained resource pressure.

No single raw metric is assumed to be the final commercial unit.

## 14. Usage / Billing Boundary

CPU milliseconds, RAM bytes, DB connections, queue depth and internal worker time are engineering telemetry by default.

They may support:
- protection;
- package recommendation;
- Cost-to-Serve;
- Enterprise candidacy;
- dispute evidence lineage.

They do not become Chargeable Usage unless a later published customer-facing unit/rule explicitly maps them without double charging and excludes platform inefficiency.

## 15. G4 Draft Invariants

G4-01 Shared STANDARD runtime requires Tenant-aware admission/fair scheduling before physical exhaustion.

G4-02 Logical compute entitlement does not imply dedicated physical CPU/RAM/DB connections.

G4-03 Trusted Tenant Context is mandatory before Tenant-specific runtime governance or attribution.

G4-04 DB connection pools are bounded platform resources; one Tenant may not monopolize them.

G4-05 Long/runaway query controls must preserve transaction correctness and classify platform defects separately.

G4-06 Queue/worker governance must be Tenant-aware, workload-class-aware, retry-safe and starvation-resistant.

G4-07 Heavy foreseeable workloads require preflight; reservation is mandatory when entitlement, financial authorization or technical safety could be crossed.

G4-08 Queue depth alone is not sufficient evidence of workload pressure.

G4-09 Critical operating priority is finite and platform-governed; it does not create unlimited free capacity.

G4-10 Retry/redelivery must not duplicate business effect.

G4-11 Platform inefficiency is not Chargeable Usage.

G4-12 Emergency safety can veto work when correctness/availability cannot be preserved.

G4-13 Exact CPU/RAM/connection/worker/timeout thresholds and implementation mechanisms remain HOLD.

## 16. Open Evidence Carried Forward

- representative request/job execution-cost distributions;
- burst vs sustained-load behavior;
- memory-risk and large-payload benchmarks;
- DB connection pool saturation behavior;
- query latency/cancellation/recovery tests;
- worker service-rate and queue-lag tests;
- retry-storm and poison-job tests;
- fair-scheduling/noisy-neighbor tests;
- heavy-job estimation/reservation accuracy;
- Cell headroom/placement thresholds in G5;
- commercial unit mapping and Cost-to-Serve in later gates.

Status: `READY FOR G4 SPECIALIST REVIEW`.
