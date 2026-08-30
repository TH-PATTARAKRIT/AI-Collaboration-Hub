# CROSS-MODULE DATA-TRANSFER PERFORMANCE POLICY

Policy ID: SMEPLUS-POL-XMOD-PERF-001
Version: v1.0
Status: MANDATORY
Effective Date: 2026-08-30
Authority: Boss Directive `SMEPLUS-BDR-XMOD-PERF-2026-08-30-001`
Project: SMEsPlus Enterprise Suite
Applies To: Team B, Figma/UX, EXPERT IBPV, Team C, Team D, EXPERT IDTM, EXPERT IESA, Infrastructure/Operations

## 1. Purpose

Prevent SMEsPlus from becoming an ERP where individual modules are fast but inter-module communication, orchestration, propagation or consistency makes the complete customer workflow slow.

This policy supplements `SMEPLUS-POL-PERF-001` and makes module/domain handoff performance a mandatory measurable property.

## 2. Control Object — Handoff Performance Budget

Every material module/domain boundary in an approved Business Flow must have a controlled Handoff Performance Budget where performance is material.

Each record must include, as applicable:

- Handoff Performance Budget ID
- Parent P3/P4/P5 Performance Budget ID
- Source Module / Domain
- Destination Module / Domain
- Business Flow / Test / Requirement reference
- communication mode: synchronous / asynchronous / batch / event / other approved mechanism
- environment / build / commit
- dataset / payload profile
- transaction/event/request volume
- concurrency / tenant-mix profile
- target handoff duration
- hard ceiling where applicable
- p50 / p95 / p99 where statistically meaningful
- queue / propagation / consistency-lag budget where applicable
- timeout / retry budget
- payload-size / fan-out reference where material
- actual result
- variance
- critical-path contribution
- bottleneck classification
- Optimization Required? YES / NO
- evidence / trace / correlation reference
- remediation and retest reference

A handoff without a required baseline/evidence is `CROSS-MODULE PERFORMANCE EVIDENCE MISSING`.

## 3. Required Timing Decomposition

Where observable and material, the measured handoff must distinguish:

```text
Producer Processing / Commit
→ Outbound Request / Publish
→ Transport / Queue Wait
→ Consumer Start
→ Consumer Processing
→ Consumer Commit
→ Downstream Visibility / Consistency
→ User / Parent Flow Ready
```

For synchronous communication, measure request/response and blocking critical path.

For asynchronous communication, separately measure:

- producer acknowledgement
- event/message publication
- queue wait
- consumer processing
- downstream consistency completion
- user-visible completion if different

## 4. Mandatory Handoff Risks

Testing and assurance must detect, where applicable:

- chatty cross-module communication
- N+1 service/domain calls
- serial synchronous chains
- excessive round trips
- payload/serialization amplification
- queue lag / backlog
- event propagation lag
- slow consistency/read-model availability
- lock / transaction contention
- retry storms
- duplicate/replay amplification
- authorization/context recalculation overhead
- orchestration bottleneck
- external dependency wait
- tenant/workload contention
- fan-out/fan-in bottlenecks

## 5. IDTM Requirements

EXPERT IDTM must include handoff-performance evidence in applicable Test Cases across all 10 Dimensions, especially:

- Concurrency & Race Conditions
- Multi-Tenant & Security Isolation
- Integration & Idempotency
- Performance & Scalability
- Resilience / Chaos / Recovery
- Cross-Domain ERP Integrity

Required conditions, as applicable:

- normal workload
- peak workload
- burst workload
- increasing concurrency
- mixed tenants / companies
- delayed downstream dependency
- retry / timeout / duplicate / replay
- queue backlog
- large payload / high record volume
- cross-domain End-to-End transaction

If each module is locally within budget but the handoff or parent flow exceeds budget, the result is not a clean PASS.

## 6. IESA Requirements

EXPERT IESA must independently assess whether:

- inter-module budgets and evidence cover the material ERP flows
- cross-module transfer delay is acceptable for intended customer workloads
- no hidden handoff dominates the P3/P4/P5 critical path
- queue/consistency lag is operationally acceptable
- scalability headroom remains under peak and mixed-tenant workloads
- Optimization improved both the local handoff and the original parent/E2E flow
- the architecture avoids avoidable coordination overhead that would recreate common ERP latency problems

IESA may issue `PERFORMANCE / SCALABILITY GAP FOUND`, `CROSS-MODULE PERFORMANCE GAP`, `OPTIMIZATION REQUIRED BEFORE PRODUCTION`, or `EVIDENCE MISSING` as applicable. IESA does not approve Production.

## 7. Optimization Loop

```text
Cross-Module / Handoff Budget Breach
→ Trace Critical Path
→ Identify Responsible Handoff / Query / Queue / Service / Orchestration
→ Team C Optimization
→ Team D Regression Recheck
→ IDTM Independent Handoff Retest
→ IDTM Parent / E2E Retest
→ IESA Assurance Review
```

Optimization evidence must include before/after comparison under materially equivalent workload conditions.

## 8. Anti-Masking Rules

Prohibited:

- declaring Cross-Domain PASS from module-level PASS alone
- averaging fast handoffs to hide one critical slow handoff
- omitting queue wait or consistency lag from asynchronous performance
- measuring only service processing time while ignoring network/orchestration/transport delay
- hiding retry or replay overhead
- changing payload/workload after execution to create PASS
- claiming Optimization from a local improvement when the original P3/P4/P5 flow remains slow

## 9. Gate Principle

```text
P2 Modules PASS
+
P3 Cross-Module Handoff FAIL
=
P3/P4/P5 PERFORMANCE NOT PASS
```

Material unresolved handoff latency may hold IDTM, IESA Final Assurance or Production progression.

## 10. Governing Principles

**Fast modules connected slowly do not create a fast ERP.**

**No Cross-Module Handoff Evidence = No Cross-Domain Performance PASS.**

**Child PASS != Handoff PASS != End-to-End PASS.**

**Optimization must improve the customer/business critical path, not only an isolated benchmark.**

**No Evidence = No Progress.**

**Never Skip Gate.**

**Boss = Sole Final Approver.**
