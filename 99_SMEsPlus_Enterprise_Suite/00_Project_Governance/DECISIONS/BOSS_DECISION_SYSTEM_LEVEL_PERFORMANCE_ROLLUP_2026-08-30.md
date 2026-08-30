# BOSS DECISION — SYSTEM-LEVEL PERFORMANCE ROLL-UP

Decision ID: SMEPLUS-BDR-PERF-ROLLUP-2026-08-30-001
Project: SMEsPlus Enterprise Suite
Date: 2026-08-30
Authority: Boss
Status: APPROVED / EFFECTIVE

## Decision

Boss clarifies and approves that Performance / Speed Governance must not stop at individual Test Case measurement.

Individual Test Case performance controls are required primarily to identify local Optimization targets and prevent slow components from degrading the complete ERP/SaaS experience.

The project must also measure and control the combined performance of Module Flows, Cross-Domain Business Processes, End-to-End ERP User Journeys and Whole-System Workloads.

## Core Ruling

```text
Test Case Performance PASS
!=
System-Level Performance PASS
```

A system may not be treated as acceptable merely because individual Test Cases are within budget if the complete combined flow is operationally slow.

Example principle:

```text
Individual API / Test Cases = PASS
but
Complete Page / Business Flow = unacceptably slow

=> SYSTEM PERFORMANCE FAIL
=> OPTIMIZATION REQUIRED
```

No numeric system-level speed target is created by this ruling. Targets must be defined and frozen per approved Business Flow / User Journey / Workload before execution.

## Mandatory Performance Hierarchy

Performance evidence must roll through the following applicable levels:

1. P0 — Atomic operation / DB query / internal step
2. P1 — Test Case / API action / screen action
3. P2 — Module / business function / screen flow
4. P3 — Cross-Module / Cross-Domain business process
5. P4 — End-to-End ERP user journey / business transaction
6. P5 — Whole-system workload / mixed-tenant / peak operating profile

All applicable levels require controlled evidence.

A lower-level PASS does not automatically create a higher-level PASS.

## Measurement Ruling

Parent / End-to-End results must be measured directly under the approved workload.

- Sequential flows: measure actual total wall-clock duration and component spans.
- Parallel flows: measure parent wall-clock duration and critical path; do not naively sum all child durations.
- Asynchronous flows: separately measure user acknowledgement, user-visible ready state, backend completion and downstream consistency where material.
- Screens/pages: measure complete user-visible readiness, not only individual API timings.
- Cross-domain ERP flows: measure complete transaction duration across all participating domains.

## Optimization Purpose

Per-Test-Case measurement exists so the project can trace a slow overall experience back to the responsible bottleneck, such as:

- screen rendering
- API/service
- database query
- lock/contention
- queue/background processing
- external dependency
- cross-domain orchestration
- network/dependency wait
- tenant/workload contention

Optimization must then be independently retested at both the affected local level and the affected Parent / End-to-End level.

## Mandatory Flow

```text
Performance Budget at Parent / E2E level
        ↓
Allocate / trace local component budgets
        ↓
Execute Test Cases + collect local speed evidence
        ↓
Execute Module / Cross-Domain / End-to-End workload
        ↓
Measure actual combined wall-clock + critical path
        ↓
Within Budget?
   ├─ YES → continue assurance
   └─ NO  → OPTIMIZATION REQUIRED
                 ↓
              Team C
                 ↓
          Team D Regression
                 ↓
          IDTM Independent Retest
                 ↓
          IESA Final Assurance
```

## Anti-Masking Rule

The following are prohibited:

- averaging many fast Test Cases to hide one operationally critical slow flow
- declaring a Module/System PASS only from individual child PASS results
- ignoring p95/p99 tail latency where material
- ignoring orchestration/rendering/queue/dependency delays that occur only when components work together
- declaring Optimization complete without proving improvement at the original End-to-End failure point

## Gate Impact

A material Parent / End-to-End / Whole-System performance failure can hold the IDTM Gate, IESA Final Assurance or Production Gate even when all individual Test Cases are functionally correct.

## Authority

This ruling clarifies and strengthens `SMEPLUS-POL-PERF-001`.

**No Performance Baseline = No Performance PASS**

**No System-Level Performance Evidence = No System-Level Performance PASS**

**Boss = Sole Final Approver**
