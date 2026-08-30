# PERFORMANCE BUDGET HIERARCHY & ROLL-UP TEMPLATE

Template ID: SMEPLUS-TPL-PERF-ROLLUP-001
Version: v1.0
Status: MANDATORY TEMPLATE
Project: SMEsPlus Enterprise Suite

## 1. Purpose

Provide one traceable structure for measuring performance from local Test Cases through Module, Cross-Domain, End-to-End ERP and Whole-System workload levels.

## 2. Performance Hierarchy Register

| Perf ID | Parent Perf ID | Level | Module / Flow / Journey | Test / Requirement Ref | Workload / Dataset | Concurrency | Target | Hard Ceiling | p50 | p95 | p99 | Max | Throughput | E2E Wall Clock | Critical Path | Actual | Variance | Status | Optimization Required | Evidence |
|---|---|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| TBD | TBD | P0-P5 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 3. Level Definitions

- P0 — Atomic operation / DB query / internal step
- P1 — Test Case / API action / screen action
- P2 — Module / business function / screen flow
- P3 — Cross-Module / Cross-Domain business process
- P4 — End-to-End ERP user journey / business transaction
- P5 — Whole-system workload / mixed-tenant / peak operating profile

## 4. Parent Flow Reconciliation

For every P2-P5 record, document:

- Child Perf IDs
- actual parent wall-clock duration
- critical-path child/spans
- orchestration / rendering / queue / dependency overhead
- difference between child diagnostic totals and observed parent duration
- bottleneck owner
- Optimization action if budget exceeded

## 5. Gate Rule

```text
Child PASS + Parent FAIL = PERFORMANCE FAIL / OPTIMIZATION REQUIRED
```

A parent flow must be measured directly. Child averages or child PASS counts cannot substitute for the parent result.

## 6. Optimization Retest

After Optimization, preserve:

- Before metrics
- Change reference / commit
- Team D regression result
- IDTM child-level retest
- IDTM parent/E2E retest
- IESA disposition where applicable
- Remaining bottleneck / residual risk

## 7. Evidence Rule

**No Performance Baseline = No Performance PASS**

**No System-Level Performance Evidence = No System-Level Performance PASS**
