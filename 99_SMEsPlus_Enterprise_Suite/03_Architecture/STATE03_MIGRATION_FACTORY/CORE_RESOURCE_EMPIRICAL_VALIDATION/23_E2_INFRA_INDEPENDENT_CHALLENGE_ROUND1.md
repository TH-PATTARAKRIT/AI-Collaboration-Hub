# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2-INFRA — Independent Challenge Round 1

Status: HOLD — CONTROL CORRECTIONS REQUIRED
Jira: ERPPLUS-156
Challenge scope: 20_E2_CONTROLLED_SCOPE_CORRECTION_VDR_PHASE_ALIGNMENT.md + 21_E2_INFRA_READONLY_PREFLIGHT_EVIDENCE_REGISTER.md + 22_E2_INFRA_SPECIALIST_REVIEW.md

## 1. Challenge Question

Can SMEDEV now be used for infrastructure-only empirical pressure/recovery tests without creating false certainty, violating VDR phase boundaries, or damaging the shared Dev/Test environment?

## 2. Adversarial Findings

CH-01 — False isolation risk
Container CPU/memory limits are absent. A test could saturate the entire VM and be misread as per-service capacity evidence.

CH-02 — Redis memory exhaustion risk
`maxmemory=0` means Redis can grow until host/container memory pressure intervenes. Pressure testing without a pre-defined ceiling and abort condition is unsafe.

CH-03 — Metrics attribution risk
cAdvisor and Node Exporter show host/container utilization but cannot explain PostgreSQL/Redis internal bottlenecks by themselves.

CH-04 — Cross-network ambiguity
Services connected to multiple zone networks may bypass the intended architecture path. A successful request does not prove intended segmentation.

CH-05 — Mutable-tag repeatability risk
`latest` tags can move between runs; image ID capture must be part of every run manifest.

CH-06 — Demo contamination risk
The Python/Flask demo can be used as an infrastructure probe, but its throughput/latency cannot be called SMEsPlus application performance.

CH-07 — Existing-data contamination risk
PostgreSQL/Redis/MinIO contain persistent volumes. Synthetic component tests must not modify unknown retained data without reset/fixture ownership evidence.

CH-08 — Recovery semantics inflation
Container restart time is not product RTO and not business recovery. Component recovery claims must remain component-scoped.

CH-09 — Shared-lab blast-radius risk
The current VM is already hosting multiple services. Destructive failure injection or uncontrolled saturation may impair unrelated evidence collection or retained Dev/Test assets.

CH-10 — Root-access governance risk
SSH root access is verified. Root availability must not be interpreted as authorization to modify host/firewall/compose/config during VDR validation.

CH-11 — Tooling provenance risk
No versioned load-generator baseline is currently frozen. Ad hoc shell loops/curl floods would not meet repeatability evidence standards.

CH-12 — Product-phase leakage risk
Installing or deploying SMEsPlus product runtime solely to satisfy E2 would violate Boss's clarified VDR phase boundary.

## 3. Mandatory Corrections Before Any Pressure Run

CR-01 — Establish run classification: `UNBOUNDED_HOST_COMPONENT_BASELINE` vs future bounded-envelope test. Never mix results.

CR-02 — Define hard stop criteria for CPU, RAM, swap, disk, error rate and service health before executing load.

CR-03 — Define a non-destructive synthetic workload that uses isolated temporary objects/data or read-only operations wherever possible.

CR-04 — Freeze exact image IDs, compose hash, host manifest and observation timestamp per run.

CR-05 — Record observability limitation: no DB/Redis exporter means those dimensions cannot receive detailed bottleneck conclusions.

CR-06 — Define expected network path and perform only read-only connectivity/negative-path checks unless explicit infrastructure change authorization exists.

CR-07 — Prohibit host/config/container restart/failure injection in Round 1. Start with passive baseline and low-impact component probes only.

CR-08 — Define immutable run ledger schema before first empirical run.

CR-09 — Keep demo/API placeholder results explicitly labelled `INFRASTRUCTURE PROBE ONLY`.

CR-10 — Keep E2-APPLICATION and all product/Tenant/commercial conclusions DEFERRED.

## 4. Challenge Disposition

`E2-INFRA PRE-FLIGHT EVIDENCE = ACCEPTED`.

`E2-INFRA PRESSURE / FAILURE / RECOVERY RUN = HOLD PENDING CR-01..CR-10`.

No existing evidence justifies product capacity, Tenant capacity, SLA, RPO/RTO, or Standard-to-Enterprise numerical claims.

No Development work is required or authorized.
Build / Merge / Deployment / Production remain HOLD.
Boss remains sole Final Approver.
