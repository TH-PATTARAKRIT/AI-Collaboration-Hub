# PERFORMANCE / SPEED BUDGET & OPTIMIZATION POLICY

Policy ID: SMEPLUS-POL-PERF-001
Version: v1.1
Status: BOSS APPROVED / MANDATORY
Effective Date: 2026-08-30
Project: SMEsPlus Enterprise Suite
Applies To: Team B, Figma/UX, EXPERT IBPV, Team C, Team D, EXPERT IDTM, EXPERT IESA, Infrastructure/Operations and all AI test/review executors

## 1. Objective

Make Performance / Speed a controlled, measurable project property at every applicable lifecycle stage, comparable to Test Tolerance governance but measured using appropriate performance units and workload baselines.

The policy exists to identify which module, process, screen, API, report, background job, integration or Test Case requires Optimization before customer use **and to prove that the complete combined ERP/SaaS workflow remains within an approved system-level Performance Budget**.

Local speed evidence is diagnostic evidence. It is not a substitute for End-to-End or whole-system performance evidence.

## 2. Core Rule

Every applicable controlled flow/Test Case must have a **Performance Budget** before execution and an **Actual Performance Result** after execution.

Every applicable parent Business Flow / Cross-Domain Flow / User Journey / System Workload must also have its own Performance Budget and Actual Result.

No claimed speed/performance PASS is valid without a frozen workload condition, target/baseline and evidence.

**Child Test Case PASS != Parent Flow PASS.**

**Module PASS != End-to-End ERP PASS.**

**No System-Level Performance Evidence = No System-Level Performance PASS.**

## 3. Mandatory Performance Budget Fields

Each applicable record must include:

- Performance Budget ID
- Parent Performance Budget ID where applicable
- Requirement / Risk / Test reference
- Module / Domain / Flow / Screen / API / Job
- Business Process / Customer Journey reference where applicable
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
- end-to-end wall-clock duration where applicable
- critical-path duration / bottleneck stage where applicable
- baseline version
- allowed regression/degradation threshold
- evidence method
- trace / correlation ID where applicable
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
- End-to-End business process / user-journey timing expectation

Team B does not invent implementation-specific tuning.

### Figma / UX — Perceived Performance Design

Define, where material:

- user feedback/loading behavior
- asynchronous/progressive behavior
- blocking vs non-blocking interaction
- critical screen transition expectations
- long-running action UX
- timeout / retry / progress-state behavior
- user-perceived total task / page readiness expectation

Figma must not hide backend latency with misleading UI states.

### EXPERT IBPV — Pre-Build Performance Feasibility Verification

Verify that:

- performance expectations are consistent with the business flow
- critical process bottlenecks are identified before Development where possible
- UX design handles legitimate long-running operations safely
- cross-domain flow timing assumptions do not create functional/control conflicts
- component budgets are compatible with the parent Business Flow / End-to-End Performance Budget

IBPV records gaps; it does not optimize code.

### Team C — Engineering Instrumentation & Optimization

Team C must:

- implement required performance instrumentation and distributed tracing where applicable
- establish implementation baselines
- profile local and system-level bottlenecks
- optimize when thresholds are exceeded
- preserve before/after evidence
- preserve parent-child traceability from slow End-to-End flow to responsible module/API/query/job/integration
- avoid performance optimizations that break functional/accounting/security invariants

### Team D — QA / Regression Performance Measurement

Team D must:

- measure performance for applicable regression scenarios
- compare current results to frozen baselines
- measure both local Test Case and parent End-to-End flow performance where applicable
- flag material degradation
- verify that optimization changes did not create functional/compliance regressions

### EXPERT IESA Pre-Assurance Challenge

IESA may challenge:

- whether workload assumptions are realistic
- whether percentiles / throughput evidence are sufficient
- whether peak-load / growth / tenant-mix scenarios are missing
- whether critical flows require stronger performance evidence before IDTM execution
- whether Test Case budgets roll up into realistic Module / Cross-Domain / System-Level budgets

No final Production verdict is issued in Pre-Assurance.

### EXPERT IDTM — Deep Performance Evidence

IDTM must:

- capture applicable Speed/Performance metrics for **every Test Case**, not only Dimension 7
- execute dedicated Performance & Scalability scenarios
- stress concurrency/race scenarios under measured latency
- run load/stress/soak tests where required
- measure Module, Cross-Domain and End-to-End business-flow duration
- measure parent System/User-Journey performance directly; it must not infer system PASS merely from child Test Case PASS
- identify module/API/query/job/integration bottlenecks from the observed End-to-End critical path
- classify `OPTIMIZATION REQUIRED` when any applicable local or parent budget is exceeded
- independently retest optimized implementations at both affected child and parent levels

### EXPERT IESA Final Assurance

IESA must independently assess:

- performance evidence completeness
- child-to-parent Performance Budget traceability
- Module and Cross-Domain response time
- complete End-to-End / User-Journey wall-clock performance
- scalability headroom
- bottleneck concentration
- degradation trends
- expected customer workload fitness
- operational sustainability
- whether residual performance risk is acceptable for Boss decision

A set of fast isolated Test Cases cannot compensate for an unacceptably slow combined business workflow.

### Production Operations

Approved local and parent baselines become monitoring references for:

- latency / duration
- End-to-End customer-journey duration
- throughput
- timeout / error rate
- queue depth / processing delay
- resource saturation
- trend degradation
- capacity planning
- recurring Optimization backlog

## 5. Performance Budget Hierarchy & Mandatory Roll-Up

Performance must be controlled at multiple levels. Applicable levels are mandatory and cannot be collapsed into only Test Case metrics.

| Level | Control Unit | Purpose |
|---|---|---|
| P0 | Atomic operation / DB query / internal step | Diagnose low-level bottlenecks |
| P1 | Test Case / API action / screen action | Control individual behaviour |
| P2 | Module / business function / screen flow | Prove module-level operational speed |
| P3 | Cross-Module / Cross-Domain business process | Detect accumulated and coordination latency |
| P4 | End-to-End ERP user journey / business transaction | Measure real user/business completion time |
| P5 | Whole-system workload / mixed-tenant / peak operating profile | Prove platform-level customer fitness |

Rules:

1. Each applicable P1-P5 level must have a frozen target/budget before the controlled run.
2. A lower-level PASS does not automatically create a higher-level PASS.
3. A higher-level result must be **measured directly under its approved workload**, not produced only by averaging child results.
4. A critical slow child cannot be hidden inside an acceptable average.
5. A fast child set cannot hide orchestration, serialization, queue, rendering, network, lock-wait or dependency delays that make the parent flow slow.
6. IDTM and IESA must preserve drill-down traceability from a failed P3/P4/P5 result to the contributing P0/P1/P2 bottlenecks.
7. All applicable levels must satisfy their approved budgets for a clean Performance PASS.

## 6. Roll-Up Measurement Rules

### Sequential Work

For sequential business steps, record the actual End-to-End wall-clock time and component spans. Component durations may be used for diagnosis, but the observed parent duration is the authoritative customer/business measure.

### Parallel Work

For parallel work, do not naively sum all child durations. Measure the parent wall-clock duration and identify the **critical path** and blocking dependencies.

### Asynchronous Work

Where user acknowledgement and backend completion differ, measure separately:

- action-to-feedback / acknowledgement
- user-visible ready state
- backend settlement/completion
- downstream consistency completion where material

### Page / Screen Load

A screen is not Performance PASS merely because each API call independently meets its own budget. The complete user-visible page/screen readiness time must also meet its approved parent budget.

### Cross-Domain ERP Flow

A business transaction is not Performance PASS merely because Sales, Inventory, Accounting or Payment each pass individually. The complete End-to-End flow must have independent measured evidence.

## 7. Mandatory Metrics by Test Type

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
- critical-path duration
- bottleneck stage

### Whole-System Workload
- representative mixed workload
- End-to-End latency distributions for critical journeys
- throughput / capacity
- saturation point
- resource contention
- tenant-mix impact where applicable

## 8. Performance Budget vs Test Tolerance

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
- End-to-End user-journey duration
- percentage degradation versus a frozen baseline

No universal performance percentage is assumed by this policy.

## 9. Performance Result Categories

Allowed evidence-based categories:

- PERFORMANCE WITHIN BUDGET
- PERFORMANCE WITHIN BUDGET WITH WATCH
- LOCAL PERFORMANCE PASS / PARENT FLOW FAIL
- SYSTEM-LEVEL PERFORMANCE FAIL
- PERFORMANCE REGRESSION FOUND
- BOTTLENECK FOUND
- OPTIMIZATION REQUIRED
- PERFORMANCE EVIDENCE MISSING
- PERFORMANCE ROLL-UP EVIDENCE MISSING
- PERFORMANCE RETEST REQUIRED
- PERFORMANCE GATE HOLD
- READY FOR NEXT ASSURANCE REVIEW

These are not Boss approval statuses.

## 10. Optimization Trigger Logic

```text
Actual Local Performance > Approved Local Budget / Hard Ceiling
OR
Actual Parent / E2E Performance > Approved Parent Budget / Hard Ceiling
OR
Regression > Approved Regression Threshold
OR
Critical Business Flow becomes operationally unusable under approved workload

→ PERFORMANCE GAP FOUND
→ BOTTLENECK / CRITICAL-PATH ANALYSIS
→ OPTIMIZATION REQUIRED
→ Team C optimization
→ Team D regression measurement
→ IDTM independent child + parent retest where applicable
→ IESA Final Assurance review
```

## 11. Optimization Register

Every material performance gap must enter the `PERFORMANCE_OPTIMIZATION_REGISTER` with:

- Finding ID
- Performance hierarchy level P0-P5
- Parent Performance Budget ID
- Module / Flow / Test Case / User Journey
- baseline and actual metrics
- parent End-to-End metric where applicable
- severity / business impact
- suspected bottleneck area
- critical-path evidence
- assigned owner
- remediation action
- before/after evidence
- regression result
- IDTM retest result where applicable
- IESA disposition where applicable
- Boss ruling if risk acceptance is required

## 12. Anti-Gaming Rules

Prohibited:

- changing workload after execution to create a PASS
- changing target/threshold after seeing results without controlled re-baselining
- averaging severe slow flows into an acceptable project-wide mean
- treating child Test Case PASS as automatic parent/system PASS
- reporting only average latency while hiding p95/p99 tail latency where material
- summing parallel child timings and presenting the number as user-visible duration
- ignoring orchestration / rendering / queue / dependency time that appears only at parent level
- comparing results from materially different environments without disclosure
- claiming Optimization success without before/after evidence at the affected child and parent levels
- accepting faster performance when accounting/security/data correctness regresses
- hiding timeout/blocked/error cases from performance statistics

## 13. Gate Principle

A functional PASS and a performance FAIL are not a clean PASS.

A local Test Case Performance PASS and a Parent / End-to-End Performance FAIL are not a clean PASS.

Material unresolved Performance / Scalability gaps can block IDTM/IESA/Production progression when they make the intended system workload unsafe, unstable or operationally unfit.

## 14. Governing Principles

**No Evidence = No Progress**

**No Performance Baseline = No Performance PASS**

**No System-Level Performance Evidence = No System-Level Performance PASS**

**Child Test Case PASS != Parent Flow PASS**

**Functional correctness does not excuse unacceptable speed.**

**Optimization must not break business/accounting/security correctness.**

**Never Skip Gate**

**Boss = Sole Final Approver**
