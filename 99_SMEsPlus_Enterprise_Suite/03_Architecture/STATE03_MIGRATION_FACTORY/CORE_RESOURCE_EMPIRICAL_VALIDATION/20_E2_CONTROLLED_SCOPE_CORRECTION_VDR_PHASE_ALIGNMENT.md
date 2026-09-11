# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2 — Controlled Scope Correction for VDR Phase Alignment

Status: CONTROLLED SCOPE CORRECTION — NO RESET
Jira: ERPPLUS-156
Parent evidence: 19_E2_SMEDEV_ACCESS_RUNTIME_PREFLIGHT_AND_BLOCKER_REFINEMENT.md
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Boss Correction

Boss clarified that SMEsPlus is still in VDR / Architecture Validation and has not entered Development. Therefore absence of a current SMEsPlus Node.js product runtime must not be treated as a defect or blocker requiring premature development.

This correction is a material governance clarification. It changes the interpretation and execution boundary of E2, but does not invalidate E0, E1, prior infrastructure evidence, or the verified SMEDEV lab-access evidence.

## 2. Correct Phase Interpretation

Current product lifecycle boundary:

VDR
-> Architecture Validation
-> Infrastructure Lab Validation where architecture-only proof is possible
-> Functional Design
-> Figma
-> Development
-> Product/Application Runtime Empirical Validation

Do not pull Development work into VDR to satisfy an empirical gate.

## 3. E2 Scope Split

### E2-INFRA — IN SCOPE NOW

Infrastructure-only empirical validation may continue using the verified SMEDEV lab where evidence is sufficient.

Allowed evidence targets include:
- host CPU / RAM / disk / network baseline;
- VM/container resource isolation and pressure behavior;
- Docker runtime and network-zone behavior;
- PostgreSQL component baseline and resource behavior;
- Redis component baseline and resource behavior;
- MinIO/object-storage component baseline and resource behavior;
- Prometheus/Grafana/Loki/cAdvisor/Node Exporter observability proof;
- infrastructure failure/restart/recovery behavior where non-destructive and explicitly controlled;
- infrastructure headroom and contention observations;
- evidence collection / checksum / run ledger discipline;
- architecture-lab documentation drift and configuration provenance.

These tests prove only infrastructure/component behavior. They must not be converted into product capacity, Tenant capacity, commercial entitlement, SLA, RPO/RTO, or Standard-to-Enterprise crossover claims.

### E2-APPLICATION — DEFER UNTIL DEVELOPMENT

The following proof obligations are not currently applicable for execution and are deferred until a real SMEsPlus application runtime exists under an authorized Development phase:
- real SMEsPlus API/BFF transaction workload;
- Tenant business-workload fairness;
- application-level noisy-neighbor results;
- Accounting / Inventory business-integrity assertions;
- per-Tenant application telemetry;
- real application queue/worker behavior;
- business transaction reconciliation under pressure;
- sustainable customer/Tenant/Company capacity;
- application-derived Standard-to-Enterprise crossover;
- product RPO/RTO including usable and reconciled business truth.

Deferred does not mean waived. These obligations remain in the future evidence universe and must re-enter when the Development runtime exists.

## 4. Reclassification of E2-BLK-01

Previous wording incorrectly bundled product-runtime absence into the current VDR Architecture Lab blocker.

New controlled interpretation:

`E2-BLK-01A — INFRASTRUCTURE LAB ACCESS / BASELINE` = PARTIALLY RESOLVED / ACTIVE VALIDATION
- SMEDEV access verified.
- Core infrastructure containers and observability stack verified present.
- Additional current configuration / provenance / run-evidence is still required per individual infrastructure test.

`E2-BLK-01B — SMEPLUS PRODUCT/APPLICATION RUNTIME` = DEFERRED / NOT CURRENTLY APPLICABLE FOR EXECUTION
- Not a defect in the VDR phase.
- Must not trigger development, source-code creation, deployment, or product runtime fabrication.
- Re-enters at the authorized Development/Application Runtime Empirical Validation phase.

## 5. Current Evidence State

Verified now:
- SSH access to SMEDEV `103.253.74.216`;
- current KVM/Ubuntu host identity;
- 40 vCPU, 60 GiB RAM, 300 GiB root disk at capture;
- Docker runtime present;
- PostgreSQL, Redis, MinIO, Prometheus, Grafana, Loki, Promtail, Node Exporter, cAdvisor, Traefik and supporting Dev/Test services present;
- application-facing containers are demo/placeholders and must not be treated as SMEsPlus product evidence;
- compose provenance exists at `/opt/smes-dev/docker-compose.yml` but `/opt/smes-dev` is not a Git working tree;
- README/IP drift exists between historical `.215` documentation and verified `.216` runtime host.

## 6. E2 Gate Rule After Correction

E2 may now continue only through `E2-INFRA` proof obligations that are valid without a product runtime.

E2 must not be declared a full Tenant Fairness / Runtime Safety PASS on infrastructure evidence alone.

Allowed disposition vocabulary:
- `E2-INFRA PASS CANDIDATE` when its infrastructure proof obligations are satisfied;
- `E2-APPLICATION DEFERRED UNTIL DEVELOPMENT`;
- overall E2 remains split-state until both lifecycle-appropriate components are eventually satisfied or formally superseded by the canonical gate model.

Do not open a downstream gate that requires product-level evidence merely because E2-INFRA passes.

## 7. Immediate Next Execution

Proceed with non-destructive, infrastructure-only verification in this order:

1. Freeze current SMEDEV environment manifest and hashes.
2. Verify container image IDs/tags and runtime resource settings.
3. Verify Docker network segmentation and exposed ports.
4. Verify PostgreSQL baseline configuration/resource limits without changing configuration.
5. Verify Redis baseline configuration/resource limits without changing configuration.
6. Verify MinIO baseline configuration/storage path without changing configuration.
7. Verify observability coverage for host/container/DB/queue/storage dimensions.
8. Define safe synthetic infrastructure/component test workloads that do not represent SMEsPlus business workloads.
9. Execute only tests that are non-destructive and evidence-valid in the current VDR/Architecture phase.
10. Specialist Review -> Independent Challenge -> Correction/Retest -> E2-INFRA disposition.

Any test requiring product code, Tenant business logic, schema, or application deployment is DEFERRED, not fabricated.

## 8. Governance

No Evidence = No Progress.
Never Skip Gate.
No repeated work without material delta.
No premature Development.
No fake Product Runtime.
No Build / Merge / Deployment / Production authorization is created by this correction.
Boss remains sole Final Approver.
