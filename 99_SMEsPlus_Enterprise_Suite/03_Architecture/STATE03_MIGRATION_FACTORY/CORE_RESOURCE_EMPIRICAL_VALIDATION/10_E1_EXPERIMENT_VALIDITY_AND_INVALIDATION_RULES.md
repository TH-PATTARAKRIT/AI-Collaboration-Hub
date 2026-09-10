# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E1 — Experiment Validity & Invalidation Rules

Status: E1 DRAFT FOR REVIEW
Jira: ERPPLUS-156
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Validity Principle

An experiment is valid only for the exact claim its workload, environment, controls and evidence can support.

`ONE RUN != GENERAL CAPACITY PROOF`.

## 2. Minimum Validity Criteria

For a run to support a numerical/mechanism candidate, all material criteria must be satisfied:

1. current target application/runtime identity is verified;
2. environment manifest is complete enough to reproduce material behavior;
3. workload is representative for the claim;
4. fixture/data distribution is controlled and versioned;
5. production-intent security/Tenant controls are active for whole-system claims;
6. generator has measured headroom;
7. telemetry is complete enough and collection defects are bounded;
8. run duration/load shape is appropriate;
9. repeated runs show explainable variance;
10. warm/cold/maintenance state is declared;
11. failure/degraded behavior is included where the claim depends on resilience;
12. Tenant-level fairness is measured for shared-resource claims;
13. post-load drain/recovery is observed where queues/backlogs can persist;
14. platform-defect/retry amplification is separated from legitimate Tenant workload;
15. raw artifacts and derived methods are traceable;
16. independent review is complete;
17. evidence is current/non-stale.

## 3. Invalid Run Conditions

A run is `EXECUTED_INVALID` or `HELD_FOR_REVIEW` when material issues include:
- load generator saturation;
- monitoring pipeline overload/data loss;
- unknown application commit/runtime;
- security/Tenant isolation disabled for production-intent claim;
- non-representative fixture/workload;
- clock/timing corruption;
- uncontrolled external dependency variance;
- unexpected platform defect not causally classified;
- major environment drift during campaign;
- result calculation cannot be reproduced;
- failed integrity/isolation assertion.

Invalid runs remain evidence of the failure condition but cannot support the intended capacity claim.

## 4. Repetition / Variance Rule

No critical numerical candidate may rely on one favorable run.

The campaign must use enough repeated comparable runs to characterize normal variance and identify outliers. Exact repetition count is not frozen in E1; it is selected according to workload duration, variance, cost and statistical confidence requirements.

Unexplained material variance = HOLD.

## 5. Tail / Distribution Rule

Average-only evidence is insufficient for shared SaaS capacity.

Where material, retain distributions including median and upper percentiles such as p90/p95/p99, error rates and maxima/peaks, plus per-Tenant distributions for noisy-neighbor analysis.

Exact percentile acceptance targets remain unfrozen until evidence/program criteria are established.

## 6. Sustainable Capacity Rule

`Crash / saturation point != safe admission capacity`.

Safe numerical candidates must preserve:
- operational headroom;
- correlated-burst reserve;
- recovery/maintenance reserve;
- Tenant fairness;
- acceptable backlog/drain behavior;
- security/correctness hard vetoes.

## 7. Benchmark Class Boundary

Component benchmarks isolate subsystems and cannot alone establish whole-system ERP capacity.

Production-intent system benchmarks must include material real control paths: Tenant context, auth/authorization, audit, metering/governor, DB/queue/storage path and relevant background work.

## 8. Campaign Comparability

A/B comparison requires materially equivalent:
- application version;
- workload/fixture;
- load shape;
- test duration;
- security/control stack;
- telemetry;
- cost regime;
- failure/recovery obligations.

If not equivalent, differences must be normalized or the comparison is HOLD.

## 9. Evidence Invalidation Triggers

Affected evidence is invalidated or requires equivalence proof after material change in:
- application code/path;
- Node.js/runtime/framework;
- schema/index/query behavior;
- DB/storage/cache/queue technology/version;
- security/Tenant isolation path;
- host/VM/container resource class;
- network/storage topology;
- placement/governor algorithm;
- metering/wallet path;
- workload/business process distribution;
- backup/recovery model;
- cost/provider regime;
- observability instrumentation if it affects measured behavior.

## 10. Controlled Reuse Rule

Old evidence may be reused only when:
- exact unchanged SHA/config/environment is proven; or
- a documented equivalence analysis shows the changed factor cannot materially affect the claim.

Otherwise retest is required.

## 11. Security / Integrity Veto

A result that is economically attractive but fails Tenant isolation, business correctness, accounting integrity, recovery truth or authoritative placement safety is REJECTED for production architecture regardless of throughput/cost advantage.

## 12. Numerical Promotion Ladder

`ASSUMPTION -> LAB OBSERVATION -> REPEATED VALID RUN -> VERIFIED CAMPAIGN -> NUMERICAL CANDIDATE -> BOSS FROZEN`.

Only Boss may move a numerical/mechanism/commercial candidate into final frozen state.

## 13. E1 Draft Disposition

`VALIDITY / INVALIDATION RULES = DRAFTED FOR SPECIALIST REVIEW / INDEPENDENT CHALLENGE`.