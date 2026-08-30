# PERFORMANCE / SPEED BUDGET & OPTIMIZATION POLICY

Policy ID: SMEPLUS-POL-PERF-001
Version: v1.0
Status: BOSS APPROVED / MANDATORY
Effective Date: 2026-08-30
Project: SMEsPlus Enterprise Suite
Applies To: Team B, Figma/UX, EXPERT IBPV, Team C, Team D, EXPERT IDTM, EXPERT IESA, Infrastructure/Operations and all AI test/review executors

## 1. Objective

Make Performance / Speed a controlled, measurable project property at every applicable lifecycle stage, comparable to Test Tolerance governance but measured using appropriate performance units and workload baselines.

The policy exists to identify which module, process, screen, API, report, background job, integration or Test Case requires Optimization before customer use.

## 2. Core Rule

Every applicable controlled flow/Test Case must have a **Performance Budget** before execution and an **Actual Performance Result** after execution.

No claimed speed/performance PASS is valid without a frozen workload condition, target/baseline and evidence.

## 3. Mandatory Performance Budget Fields

Each applicable record must include:

- Performance Budget ID
- Requirement / Risk / Test reference
- Module / Domain / Flow / Screen / API / Job
- Environment / build / commit reference
- Dataset size / data profile
- workload / traffic profile
- concurrent users / workers / transactions
- warm/cold-cache condition where relevant
- dependent service condition where relevant
- target metric
- target value
- hard ceiling where required
- p50 latency
- p95 latency
- p99 latency
- maximum latency where required
- throughput / transactions per second where applicable
- timeout / error rate
- baseline version
- allowed regression/degradation threshold
- evidence method
- actual result
- variance vs target/baseline
- bottleneck classification
- Optimization Required? YES / NO
- owner / action / retest reference
- Gate impact

Fields that do not apply must be explicitly marked `N/A` with rationale rather than silently omitted.

## 4. Lifecycle Responsibilities

### Team B — Business Performance Requirement

Define, where material:

- business-critical transaction timing expectation
- expected user / transaction volume
- batch / report completion expectation
- expected peak workload assumptions
- known business deadlines / cut-off windows
- process steps where delay creates operational risk

Team B does not invent implementation-specific tuning.

### Figma / UX — Perceived Performance Design

Define, where material:

- user feedback/loading behavior
- asynchronous/progressive behavior
- blocking vs non-blocking interaction
- critical screen transition expectations
- long-running action UX
- timeout / retry / progress-state behavior

Figma must not hide backend latency with misleading UI states.

### EXPERT IBPV — Pre-Build Performance Feasibility Verification

Verify that:

- performance expectations are consistent with the business flow
- critical process bottlenecks are identified before Development where possible
- UX design handles legitimate long-running operations safely
- cross-domain flow timing assumptions do not create functional/control conflicts

IBPV records gaps; it does not optimize code.

### Team C — Engineering Instrumentation & Optimization

Team C must:

- implement required performance instrumentation
- establish implementation baselines
- profile bottlenecks
- optimize when thresholds are exceeded
- preserve before/after evidence
- avoid performance optimizations that break functional/accounting/security invariants

### Team D — QA / Regression Performance Measurement

Team D must:

- measure performance for applicable regression scenarios
- compare current results to frozen baselines
- flag material degradation
- verify that optimization changes did not create functional/compliance regressions

### EXPERT IESA Pre-Assurance Challenge

IESA may challenge:

- whether workload assumptions are realistic
- whether percentiles / throughput evidence are sufficient
- whether peak-load / growth / tenant-mix scenarios are missing
- whether critical flows require stronger performance evidence before IDTM execution

No final Production verdict is issued in Pre-Assurance.

### EXPERT IDTM — Deep Performance Evidence

IDTM must:

- capture applicable Speed/Performance metrics for **every Test Case**, not only Dimension 7
- execute dedicated Performance & Scalability scenarios
- stress concurrency/race scenarios under measured latency
- run load/stress/soak tests where required
- measure cross-domain end-to-end duration
- identify module/API/query/job/integration bottlenecks
- classify `OPTIMIZATION REQUIRED` when budgets are exceeded
- independently retest optimized implementations

### EXPERT IESA Final Assurance

IESA must independently assess:

- performance evidence completeness
- cross-domain response time
- scalability headroom
- bottleneck concentration
- degradation trends
- expected customer workload fitness
- operational sustainability
- whether residual performance risk is acceptable for Boss decision

### Production Operations

Approved baselines become monitoring references for:

- latency / duration
- throughput
- timeout / error rate
- queue depth / processing delay
- resource saturation
- trend degradation
- capacity planning
- recurring Optimization backlog

## 5. Mandatory Metrics by Test Type

As applicable:

### UI / User Flow
- action-to-feedback latency
- page/screen ready time
- end-to-end task completion duration

### API / Service
- p50 / p95 / p99 response latency
- throughput
- timeout / error rate

### Batch / Report / Background Job
- total duration
- records processed per unit time
- queue delay
- resource usage

### Database-Critical Flow
- query duration
- query count where relevant
- lock wait / deadlock evidence
- transaction duration

### Concurrency
- throughput under concurrency
- percentile latency under concurrency
- saturation point
- error/retry rate

### Cross-Domain ERP Flow
- total business transaction duration
- domain-by-domain elapsed time
- bottleneck stage

## 6. Performance Budget vs Test Tolerance

Functional/Data Test Tolerance and Performance Budget are separate controls.

### Functional / Data Error

```text
0% <= T_case <= 0.001%
```

as governed by `SMEPLUS-POL-TEST-TOL-001`.

### Performance / Speed

Use appropriate target units and a pre-approved Regression Threshold, for example:

- milliseconds / seconds
- p95 / p99 latency
- transactions per second
- records per second
- total batch duration
- percentage degradation versus a frozen baseline

No universal performance percentage is assumed by this policy.

## 7. Performance Result Categories

Allowed evidence-based categories:

- PERFORMANCE WITHIN BUDGET
- PERFORMANCE WITHIN BUDGET WITH WATCH
- PERFORMANCE REGRESSION FOUND
- BOTTLENECK FOUND
- OPTIMIZATION REQUIRED
- PERFORMANCE EVIDENCE MISSING
- PERFORMANCE RETEST REQUIRED
- PERFORMANCE GATE HOLD
- READY FOR NEXT ASSURANCE REVIEW

These are not Boss approval statuses.

## 8. Optimization Trigger Logic

```text
Actual Performance > Approved Budget / Hard Ceiling
OR
Regression > Approved Regression Threshold
OR
Critical Business Flow becomes operationally unusable under approved workload

→ PERFORMANCE GAP FOUND
→ OPTIMIZATION REQUIRED
→ Team C optimization
→ Team D regression measurement
→ IDTM independent retest where applicable
→ IESA Final Assurance review
```

## 9. Optimization Register

Every material performance gap must enter the `PERFORMANCE_OPTIMIZATION_REGISTER` with:

- Finding ID
- Module / Flow / Test Case
- baseline and actual metrics
- severity / business impact
- suspected bottleneck area
- assigned owner
- remediation action
- before/after evidence
- regression result
- IDTM retest result where applicable
- IESA disposition where applicable
- Boss ruling if risk acceptance is required

## 10. Anti-Gaming Rules

Prohibited:

- changing workload after execution to create a PASS
- changing target/threshold after seeing results without controlled re-baselining
- averaging severe slow flows into an acceptable project-wide mean
- reporting only average latency while hiding p95/p99 tail latency where material
- comparing results from materially different environments without disclosure
- claiming Optimization success without before/after evidence
- accepting faster performance when accounting/security/data correctness regresses
- hiding timeout/blocked/error cases from performance statistics

## 11. Gate Principle

A functional PASS and a performance FAIL are not a clean PASS.

Material unresolved Performance / Scalability gaps can block IDTM/IESA/Production progression when they make the intended system workload unsafe, unstable or operationally unfit.

## 12. Governing Principles

**No Evidence = No Progress**

**No Performance Baseline = No Performance PASS**

**Functional correctness does not excuse unacceptable speed.**

**Optimization must not break business/accounting/security correctness.**

**Never Skip Gate**

**Boss = Sole Final Approver**
