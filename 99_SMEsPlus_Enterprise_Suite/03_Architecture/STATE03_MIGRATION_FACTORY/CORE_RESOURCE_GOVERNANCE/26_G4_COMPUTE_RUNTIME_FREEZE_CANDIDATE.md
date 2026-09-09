# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G4 — Compute / Runtime Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Gate: G4 — Compute / Runtime Gate
Supersedes for G4 decision use: `23_G4_COMPUTE_RUNTIME_GOVERNANCE_DRAFT.md`
Corrections incorporated: CH-01 through CH-16 from `25_G4_INDEPENDENT_CHALLENGE_ROUND1.md`
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. G4 Freeze Boundary

G4 freezes conceptual governance semantics for shared compute/runtime resources only.

G4 DOES NOT freeze:
- numerical CPU/RAM entitlement;
- Tenant/Cell concurrency counts;
- worker counts;
- queue partition count;
- DB connection pool size;
- statement/transaction timeout values;
- lock-wait values;
- retry/backoff/hysteresis values;
- runtime/process/container/Kubernetes/cgroup topology;
- DB proxy/pool technology;
- queue technology;
- exact heavy-job isolation mechanism;
- customer-facing compute charging units/rates;
- G5 Cell headroom thresholds;
- G8 Cost-to-Serve/load-test values.

No later team may interpret G4 logical governance as evidence of hard per-Tenant CPU/RAM isolation in a shared process.

## 2. Runtime Governance Model

Canonical conceptual chain:

`Trusted Request / Job Intent`
-> establish canonical Tenant + actor/service authorization
-> classify workload
-> evaluate effective entitlement/policy
-> evaluate Tenant aggregate fairness state
-> evaluate resource-specific admission state
-> evaluate Cell/platform protection state
-> preflight/reserve if foreseeable material workload
-> `ADMIT / QUEUE / DEFER / REJECT / CAPACITY ACTION`
-> execute under bounded runtime contract
-> emit Tenant-attributed + platform telemetry
-> reconcile reservation/usage/result.

Admission/fair scheduling is logical governance bounded by actual runtime capability. If a workload cannot be safely governed in shared execution, the valid dispositions are stronger isolation, asynchronous controlled execution, defer, reject or redesign—not a false hard-limit claim.

## 3. Canonical Workload Classes

1. `CRITICAL INTEGRITY` — finite platform-classified operations needed to preserve/complete valid business-integrity sequences.
2. `NORMAL INTERACTIVE` — ordinary bounded synchronous ERP/API operations.
3. `BACKGROUND NORMAL` — bounded asynchronous/scheduled work.
4. `HEAVY CONTROLLED` — foreseeably material CPU/RAM/DB/IO/queue/worker work requiring enhanced admission/preflight.
5. `OPTIONAL / DEFERRABLE` — non-critical work restricted/deferred first under pressure.
6. `PLATFORM / SYSTEM` — maintenance, migration, observability, internal reconciliation, indexing/DB/platform operations; explicitly not arbitrary Tenant usage.

Classification is platform-governed. Customers cannot self-label work as critical to gain priority or reserve.

## 4. Tenant Fairness Identity — CH-03

Primary runtime fairness/admission accounting aggregates at canonical `Tenant ID`.

Optional subordinate controls may exist for:
- user;
- API key/client;
- Company;
- integration;
- job type.

But multiplying users, sessions, API keys, credentials or child jobs never creates additional Tenant entitlement.

Child/subjobs inherit canonical Tenant, parent workload identity and reservation/evidence lineage.

## 5. CPU Governance — CH-01

CPU governance in STANDARD is based on controlled admission, concurrency, scheduling, bounded work, isolation escalation and Cell headroom.

Rules:
- do not claim hard Tenant CPU slice where runtime mechanism cannot prove it;
- CPU-blocking/event-loop-blocking work that cannot be bounded safely in shared execution must be isolated/deferred/rejected/redesigned;
- temporary burst != sustained heavy workload;
- platform inefficiency is separated from legitimate Tenant workload;
- protection acts before shared execution saturation.

## 6. RAM / OOM Governance — CH-02

Memory safety is a shared-process/worker/Cell concern and may fail faster than commercial quota controls.

Required contract:
- preflight input/payload/output size where materially estimable;
- bounded batch/window/page size;
- prefer streaming/chunking for large data movement where semantics permit;
- prevent unbounded in-memory materialization;
- high-memory-risk work requires stronger isolation or denial when credible bounds cannot be established;
- process/worker memory health participates in protection/admission;
- emergency memory safety may stop new work to preserve correctness/availability.

No memory amplification caused by SMEsPlus defect becomes Chargeable Usage.

## 7. Connection Acquisition Governance — CH-04

DB connection acquisition is a distinct controlled resource.

Required rules:
- bounded platform/Cell/app pool;
- controlled acquisition path;
- Tenant aggregate concurrency/fairness policy;
- wait-time and saturation telemetry;
- prompt release after transaction scope;
- leak detection classified as platform defect;
- heavy/background concurrency may be separately bounded;
- admission/backpressure activates before connection refusal cascade.

Logical entitlement does not imply dedicated DB connections.

## 8. Query / Transaction Governance — CH-04/05/06

Query execution pressure is distinct from connection acquisition pressure.

Protection signals may include:
- query duration;
- transaction duration;
- lock wait/contention;
- rows/result/materialization class;
- repeated expensive access pattern;
- downstream I/O/DB pressure;
- waiting connection pressure.

Rules:
- normal paths use bounded result/pagination/batching principles;
- heavy batch work must not use unbounded transaction scopes;
- query/statement/transaction timeout policy is workload-class-aware;
- cancellation must have explicit transaction outcome semantics;
- after failed/aborted DB transaction, application cannot continue as if success occurred;
- ambiguous externally visible material command outcome requires idempotency/reconciliation path;
- DB protection can defer/reject new heavy work before lock/connection cascade.

Bad SQL, N+1, missing index, defective query plan usage or connection leak is Platform Inefficiency until remediated and re-measured.

## 9. Tenant Scope at Data Access and Async Execution — CH-09

Trusted Tenant Context must be established/revalidated at each material execution boundary.

For queued work:
- enqueue captures canonical Tenant/workload/auth provenance;
- dequeue/execution revalidates authorization/scope;
- queue payload alone is not sufficient authorization proof;
- system/privileged jobs require explicit scope/batch provenance;
- cross-Tenant platform batches must partition/attribute execution safely and cannot become hidden customer context.

## 10. Queue / Worker Fair Scheduling — CH-07/08

Scheduler fairness uses Tenant aggregate load plus workload weight/class, not job count alone.

Required controls:
- bounded in-flight work;
- Tenant-aware weighted service accounting;
- queue age and starvation monitoring;
- bounded critical-priority override;
- normal eligible tenants receive starvation protection except during explicit emergency correctness action;
- heavy/optional work yields before critical/normal work;
- job fragmentation does not create extra service share;
- poison jobs are isolated/held rather than endlessly retried.

Queue depth alone is insufficient; pressure considers depth, age, service rate, job weight and downstream resources.

## 11. Retry / Redelivery Contract — CH-10

Retries are finite, failure-class-aware and idempotency-controlled.

Rules:
- non-retryable business validation failures are not auto-retried;
- material retryable commands/jobs carry idempotency/deduplication identity where duplicate effect is possible;
- platform-caused retry/rework is classified separately from customer-intended logical usage;
- retry amplification does not create duplicate customer charge/evidence;
- retry storms are protection events and may cause temporary admission reduction;
- poison messages/jobs move to held/dead-letter/recovery disposition after bounded attempts.

Exact backoff algorithm remains HOLD.

## 12. Heavy Job Preflight + Runtime Budget — CH-11

Initial reservation is necessary but not sufficient for long material work.

Conceptual sequence:

`Estimate`
-> Tenant entitlement check
-> financial authorization check when chargeable
-> Cell/platform safety check
-> reserve required resource/credit/runtime slot
-> execute in bounded chunks/checkpoints where feasible
-> continuously compare actual vs budget/safety
-> continue / pause / re-reserve / controlled-cancel
-> reconcile committed chunks + actual result
-> release unused reservation.

An initial reservation never authorizes continuing into a newly unsafe physical state.

Already-correct committed chunks must be reconciled; they are not blindly rerun after pause/failure.

## 13. Telemetry Freshness / Unknown State — CH-12

Material protection signals carry:
- observation timestamp;
- source;
- freshness;
- validity/confidence state where applicable.

If critical safety telemetry is stale/unknown:
- new heavy/optional admission fails conservative/defer by default;
- existing work is governed by its safety contract;
- normal/critical work may continue only within explicitly safe bounded policy;
- unknown telemetry cannot be treated as proof of spare capacity.

## 14. Protection Hysteresis / State Flapping — CH-13

Protection state changes require hysteresis/cool-down or equivalent anti-flap control.

Exact values remain later evidence.

Each transition records:
- prior/new state;
- reason code;
- relevant evidence snapshot;
- timestamp;
- affected resource/workload classes;
- recovery condition.

## 15. Commercial Reservation / Failed Job Reconciliation — CH-14

`Reserved resource/credit != measured final consumption`.

Rules:
- unused reservation is released/reconciled;
- a failed/cancelled job does not automatically become customer Chargeable Usage;
- platform-failed/retried work cannot be double-charged;
- separately contracted reserved capacity may have its own commercial rule independent of measured consumption;
- non-refundable third-party/customer-caused external cost, if ever chargeable, requires separately published/authorized rule and evidence;
- anti-double-charge rules from G2 remain mandatory.

## 16. Platform/System Workload — CH-15

Platform/system work participates in Cell capacity planning and protection but is not arbitrarily assigned to one Tenant.

Examples:
- maintenance/index work;
- migrations;
- platform reconciliation;
- observability processing;
- backup/restore orchestration;
- shared operational jobs.

It must have:
- explicit scope;
- workload class;
- scheduling policy;
- platform Cost-to-Serve attribution;
- safety interaction with Tenant workloads.

Where a system job is legitimately Tenant-specific, Tenant attribution must be explicit and separate from any conclusion about commercial chargeability.

## 17. Emergency Safety / Business Correctness — CH-16

Emergency protection should act at safe admission/transaction boundaries wherever possible.

Rules:
- do not intentionally interrupt an atomic transaction in a way that fabricates success;
- DB/application recovery contract determines commit/rollback outcome;
- ambiguous client outcome uses idempotent retry/status reconciliation;
- new writes may be rejected when no safe capacity remains;
- critical priority cannot override a physical correctness/failure boundary;
- business truth is preserved over availability when both cannot be guaranteed simultaneously.

## 18. Tenant-local vs Cell-global Pressure — SR-02

Protection distinguishes:
1. Tenant-local entitlement/fairness pressure;
2. workload-specific safety pressure;
3. Cell-global shared resource pressure;
4. platform/system pressure.

A Tenant-local restriction must not be used to hide Cell-global capacity failure.

A Cell-global protection state may reduce admission across multiple Tenants even when an individual Tenant is within logical entitlement.

G5 must prove placement/headroom policy that reduces frequency/risk of Cell-global protection.

## 19. Customer-Facing Restriction Contract — SR-12

Customer-facing reason codes must translate internal complexity into an understandable action message without exposing unsafe internal detail.

Conceptual reason classes:
- INCLUDED CAPACITY PRESSURE;
- HEAVY WORK REQUIRES RESERVATION;
- TEMPORARY SHARED CAPACITY PROTECTION;
- PACKAGE / ADD-ON REVIEW;
- ENTERPRISE REVIEW;
- PLATFORM SAFETY / SERVICE PROTECTION;
- RETRY / RECOVERY IN PROGRESS.

A recommendation/restriction must be evidence-backed and distinguish temporary burst from sustained behavior.

## 20. Compute Cost-to-Serve Variance Classes — SR-10

Later G8 evidence must separate at minimum:
- legitimate Tenant workload;
- shared platform baseline;
- platform/system maintenance;
- retry/rework amplification;
- Platform Inefficiency/defect;
- protection/headroom cost;
- third-party workload cost;
- anomaly/measurement defect.

Only explicit published commercial mapping can convert eligible customer-facing value/usage to Chargeable Usage.

## 21. G4 Invariants — Freeze Candidate

G4-01 STANDARD shared compute/runtime uses Tenant-aware logical admission/fair scheduling; it does not claim unproven hard per-Tenant CPU/RAM isolation.

G4-02 Canonical Tenant ID is the primary aggregate fairness identity; multiplying users/keys/sessions/jobs does not multiply entitlement.

G4-03 CPU-blocking or memory-unbounded work that cannot be safely governed in shared execution requires isolation/defer/reject/redesign.

G4-04 Connection acquisition fairness and query/transaction execution protection are separate controls.

G4-05 DB transaction cancellation/failure must have explicit outcome/recovery semantics; ambiguity requires idempotent reconciliation.

G4-06 Transaction duration and lock contention are first-class shared-capacity protection signals.

G4-07 Queue scheduling accounts for Tenant aggregate workload and job weight, not job count alone.

G4-08 Critical priority is finite/platform-governed and includes starvation control where correctness permits.

G4-09 Async execution revalidates Tenant authorization/scope at dequeue; queued metadata alone is not sufficient authorization.

G4-10 Retry/redelivery is finite and idempotency-aware; platform retry amplification is not customer chargeable usage by default.

G4-11 Heavy jobs require both initial preflight/reservation and runtime budget/checkpoint control where feasible.

G4-12 Stale/unknown safety telemetry cannot be used as evidence of spare capacity; new heavy/optional work fails conservative/defer.

G4-13 Protection state transitions require anti-flap/hysteresis concept and auditable reason/evidence.

G4-14 Reserved capacity/credit is reconciled separately from actual measured consumption.

G4-15 Platform/system workload is explicitly governed and Cost-to-Serve attributed; it is not arbitrarily charged to Tenants.

G4-16 Emergency safety acts at safe boundaries where possible and preserves business truth/correctness over forced availability.

G4-17 Tenant-local and Cell-global pressure are separate states; one cannot be used to conceal the other.

G4-18 Customer restriction/recommendation reason is evidence-backed and understandable.

G4-19 Internal CPU/RAM/DB/queue/worker telemetry is not automatically a customer commercial unit.

G4-20 No numerical runtime quantity, threshold or infrastructure mechanism is frozen at G4.

## 22. Open Evidence Carried Forward

G4 closes conceptual governance, not empirical capacity.

Still required later:
- CPU/event-loop/blocking workload benchmarks;
- memory/OOM/high-payload tests;
- DB pool saturation and fairness tests;
- long transaction/lock contention tests;
- timeout/cancellation/idempotency tests;
- queue weighted fairness/starvation tests;
- retry storm/poison job tests;
- async Tenant-context security tests;
- heavy-job estimate/checkpoint/re-reservation tests;
- telemetry freshness/failure tests;
- protection hysteresis tests;
- platform workload interference tests;
- representative Cell noisy-neighbor/load evidence;
- G5 Cell headroom/admission/movement model;
- G8 Cost-to-Serve and package economics.

Status: `READY FOR G4 INDEPENDENT RE-CHALLENGE`.
