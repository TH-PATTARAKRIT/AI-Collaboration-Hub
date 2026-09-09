# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G4 — Independent Adversarial Challenge Round 1

Status: CHALLENGE COMPLETE — MATERIAL CORRECTIONS REQUIRED
Gate: G4 — Compute / Runtime Gate
Challenged artifacts:
- `23_G4_COMPUTE_RUNTIME_GOVERNANCE_DRAFT.md`
- `24_G4_SPECIALIST_REVIEW.md`
Independent role: Architecture Audit / Adversarial Challenge
Final Approver: Boss only

## 1. Challenge Standard

Attack the G4 model for:
- shared-runtime noisy neighbor;
- CPU/event-loop starvation;
- memory/OOM blast radius;
- DB connection/query monopolization;
- transaction correctness under cancellation;
- queue fairness/gaming;
- retry storms and poison jobs;
- Tenant-context loss;
- priority inversion/starvation;
- heavy-job estimate error;
- telemetry lag/measurement failure;
- billing/metering double count;
- emergency safety behavior;
- operational burden and observability gaps.

## 2. Findings

### CH-01 — Shared process CPU governance can create false isolation claims — CRITICAL
The draft correctly avoids claiming dedicated CPU, but wording around Tenant controls could still be misread as hard per-Tenant CPU enforcement inside one shared process.

Correction required:
- explicitly define admission/fairness as best-effort logical governance bounded by the actual runtime mechanism;
- if a workload can block/starve shared execution beyond controllable limits, it must be isolated/deferred/rejected rather than represented as safely rate-limited.

### CH-02 — Memory/OOM is a process-level failure risk, not merely a Tenant quota issue — CRITICAL
A single underestimated job may cause shared process memory exhaustion before policy reacts.

Correction required:
- high-memory-risk work must use preflight plus bounded/chunked/streaming processing where semantics permit;
- workloads without credible memory bound require stronger execution isolation or denial;
- memory emergency action must prioritize process/Cell survival and correctness.

### CH-03 — Canonical fairness identity can be gamed through users/API keys/sessions — MATERIAL
Per-user/session limits allow one Tenant to multiply concurrency.

Correction required:
- primary fairness/admission accounting must aggregate at canonical Tenant scope, with optional subordinate actor/key controls;
- aliases/credentials do not create additional Tenant entitlement.

### CH-04 — Connection fairness and query fairness are different resources — MATERIAL
A Tenant can monopolize DB by many short connections/transactions or by fewer long/expensive queries.

Correction required:
- govern acquisition/concurrency and execution duration/cost separately;
- pool saturation decisions must consider wait time, active transactions, long transactions and downstream DB pressure.

### CH-05 — Timeout/cancel can create ambiguous transaction state — CRITICAL
Killing a query or request without explicit transaction semantics can leave client ambiguity, locks or partial side effects.

Correction required:
- cancellation must have defined transaction outcome and recovery/reconciliation path;
- after DB statement/transaction error, the application must not continue as though the transaction succeeded;
- externally visible material commands require idempotency/reconciliation evidence.

### CH-06 — Long transactions/lock contention can harm other Tenants even with low CPU — CRITICAL
CPU fairness alone does not address locks and transaction duration.

Correction required:
- transaction-duration and lock-wait/runaway-lock telemetry are first-class protection signals;
- heavy batch work must avoid unbounded transaction scopes;
- DB protection can defer/reject new heavy work before lock/connection cascades.

### CH-07 — Queue fairness can be gamed by job fragmentation — MATERIAL
A Tenant can split one heavy workload into thousands of small jobs to obtain a larger service share.

Correction required:
- scheduler must account for Tenant aggregate load and workload weight, not only job count;
- child/subjobs inherit parent Tenant/workload identity and reservation lineage.

### CH-08 — Critical priority can starve normal tenants — MATERIAL
Permanent high-priority critical streams could starve eligible normal interactive work.

Correction required:
- critical priority is bounded and exception-oriented;
- fairness must include starvation controls unless emergency correctness requires temporary override;
- critical work cannot be self-declared by customer.

### CH-09 — Async Tenant context cannot be trusted solely from queue payload — CRITICAL
A stale/tampered/misrouted message could execute under wrong scope.

Correction required:
- execution must re-establish/revalidate canonical Tenant/work authorization at dequeue;
- queue metadata is evidence input, not sole authorization;
- system/privileged jobs require explicit scope/batch provenance and cross-Tenant separation controls.

### CH-10 — Retry storms can create both overload and false customer usage — CRITICAL
Platform retries may amplify compute/DB/queue cost and duplicate metering.

Correction required:
- retries are finite and failure-class-aware;
- platform-caused retry/rework is classified separately from customer-intended usage;
- usage events require idempotency/dedup lineage where retries can repeat the same logical action.

### CH-11 — Heavy-job estimate can be wrong after execution begins — CRITICAL
Reservation at start does not guarantee final safety.

Correction required:
- long heavy jobs require runtime checkpoints/budgets and controlled pause/cancel/re-reserve paths where feasible;
- crossing a safety boundary must not simply continue because initial reservation existed;
- already committed correct chunks must be reconciled, not blindly rerun.

### CH-12 — Telemetry lag/failure can cause unsafe admission or false restriction — MATERIAL
If metrics are stale, the governor may admit overload or deny healthy workloads.

Correction required:
- each protection signal needs freshness/confidence state;
- stale/unknown critical safety telemetry must fail conservative for new heavy/optional work;
- normal/critical transaction policy under degraded observability must be explicitly bounded.

### CH-13 — Protection state flapping can destabilize runtime — MATERIAL
Repeatedly entering/leaving throttle states can amplify queue/retry traffic.

Correction required:
- G4 must require hysteresis/cool-down concept; exact values remain later evidence;
- state changes are reason-coded and auditable.

### CH-14 — Failed/cancelled jobs can be commercially misclassified — MATERIAL
Estimated reservation, actual resource use and customer value can diverge.

Correction required:
- reserved credit/resource != measured final usage;
- unused reservation is released/reconciled;
- platform-failed/retried work is not automatically chargeable;
- customer-caused valid third-party/non-refundable cost requires separate published commercial rule if ever charged.

### CH-15 — System maintenance jobs can become hidden cross-Tenant noisy neighbors — CRITICAL
Vacuum-like maintenance, indexing, backup coordination, migrations or platform analytics may consume large resources without Tenant attribution.

Correction required:
- platform/system workload is a separate workload class with explicit scope, scheduling and Cost-to-Serve attribution;
- it must not be charged to an arbitrary Tenant;
- it must participate in Cell capacity protection.

### CH-16 — Emergency safety must not create business-truth corruption — CRITICAL
An emergency veto that stops writes mid-flow can create uncertain business outcome.

Correction required:
- emergency protection acts at safe admission/transaction boundaries wherever possible;
- in-flight atomic transaction semantics are preserved by DB/application recovery contract;
- ambiguous client outcome requires idempotent retry/reconciliation, not duplicate business effect.

## 3. Challenge Disposition

Findings: 16
- Critical: 9
- Material: 7

Disposition:

`REWORK REQUIRED BEFORE G4 RE-CHALLENGE`.

No numerical thresholds or runtime mechanisms may be frozen as part of the corrections.
