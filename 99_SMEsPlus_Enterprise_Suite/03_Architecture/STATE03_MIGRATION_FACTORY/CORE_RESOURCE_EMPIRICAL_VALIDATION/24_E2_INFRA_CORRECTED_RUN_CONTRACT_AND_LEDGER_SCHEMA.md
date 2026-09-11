# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2-INFRA — Corrected Run Contract & Run Ledger Schema

Status: CORRECTION PACKAGE — READY FOR RE-CHALLENGE
Jira: ERPPLUS-156
Parent challenge: 23_E2_INFRA_INDEPENDENT_CHALLENGE_ROUND1.md

## 1. Phase Boundary

This contract applies only to infrastructure/component empirical validation during VDR / Architecture Validation.

It does not authorize Product Runtime creation, Development, Build, Merge, Deployment, Production, business workload simulation, Tenant capacity conclusions, or commercial/SLA claims.

## 2. Run Classes

### RUN-CLASS-A — PASSIVE_BASELINE
Read-only observation only. No synthetic load generation.
Allowed: host metrics snapshot, docker stats, container health, configuration reads, Prometheus query/read, service reachability probes.

### RUN-CLASS-B — LOW_IMPACT_COMPONENT_PROBE
Small controlled read-only or isolated-temp-data component probe. No sustained saturation. Must have stop criteria and evidence path.

### RUN-CLASS-C — UNBOUNDED_HOST_COMPONENT_PRESSURE
Not authorized in Round 1. Requires separate Boss/governance approval because current containers have no hard CPU/memory limits.

### RUN-CLASS-D — FAILURE_RECOVERY
Not authorized in Round 1. Requires explicit non-production blast-radius control, reset/rollback proof and separate authorization.

## 3. Hard Stop Criteria for Any Future Active Probe

Stop immediately if any of the following occurs:
- host available memory < 20% of total;
- swap consumption rises above 25% of configured swap during the probe;
- root filesystem usage reaches >= 80%;
- any previously healthy infrastructure service becomes unhealthy or exits;
- sustained host CPU > 85% for more than 30 seconds in a low-impact probe;
- unexpected error/timeout occurs outside the isolated probe target;
- unknown persistent data may be modified;
- telemetry becomes unavailable or inconsistent.

These are safety controls for lab execution, not product thresholds or commercial limits.

## 4. Data Safety Rule

Round 1 active probes must be either:
- read-only; or
- operate on explicitly isolated temporary objects/data with deterministic cleanup ownership.

Existing PostgreSQL/Redis/MinIO persistent data must not be modified by empirical probes unless fixture ownership and reset/recovery evidence are established.

## 5. Environment Freeze Per Run

Each run record must capture:
- Run ID;
- timestamp Asia/Bangkok;
- target hostname/IP;
- host CPU/RAM/disk snapshot;
- compose file SHA-256;
- Docker version / Compose version;
- container name + image tag + immutable image ID;
- container resource-limit snapshot;
- network attachment snapshot;
- relevant config snapshot;
- telemetry target health;
- raw evidence location + SHA-256;
- reviewer;
- verification status;
- invalidation/supersession status.

## 6. Observability Limitation

Current detailed PostgreSQL and Redis exporters are absent from active Prometheus targets.
Therefore:
- host/container-level effects may be measured;
- PostgreSQL/Redis internal bottleneck attribution remains limited;
- no detailed DB/Redis capacity conclusion may be frozen from current telemetry alone.

## 7. Network Verification Contract

For Round 1, network validation is limited to read-only connectivity and expected-reachability checks. No firewall, Docker network or routing changes are authorized.

Observed multi-zone attachments are treated as architecture evidence requiring least-privilege review, not as proven segmentation.

## 8. Mutable Image Rule

Mutable tags such as `latest` may remain in the current lab during VDR, but every run must freeze the observed immutable image ID. Cross-run comparison is invalid if image ID changes unless the run is explicitly classified as a version delta.

## 9. Demo / Placeholder Rule

`smes-webapp`, `smes-api`, `smes-bff`, `smes-frontend`, and `smes-worker` may be used only as infrastructure probes where appropriate.
Results must be labelled:
`INFRASTRUCTURE PROBE ONLY — NOT SMEPLUS PRODUCT PERFORMANCE`.

## 10. Recovery Semantics

If future component restart/recovery tests are authorized, recovery means only the named infrastructure component returns to its defined healthy/readable state.
It must never be labelled Product RTO or business recovery.

## 11. Run Ledger Schema

| Field | Requirement |
|---|---|
| Run ID | Mandatory unique ID |
| Run Class | A/B/C/D |
| Target | Exact host/service |
| Start/End | Asia/Bangkok timestamp |
| Environment Hash | Mandatory |
| Image IDs | Mandatory |
| Workload/Probe | Exact command/tool + version |
| Data Scope | Read-only / isolated temp |
| Safety Stop Criteria | Mandatory for B/C/D |
| Metrics | Exact sources |
| Raw Evidence | Path |
| SHA-256 | Mandatory |
| Reviewer | Named role |
| Verification | PASS/HOLD/INVALID |
| Invalidation Reason | If applicable |
| Claim Boundary | Exact allowed claim |

## 12. First Authorized Run After Re-Challenge

Proposed first run:
`E2INFRA-RUN-A001 — Passive Baseline`.

Allowed observations:
- uptime/load average;
- CPU/memory/swap/disk snapshot;
- `docker stats --no-stream`;
- container health/state;
- Prometheus active-target health;
- PostgreSQL read-only configuration snapshot;
- Redis authenticated read-only configuration snapshot;
- MinIO mount/storage path snapshot;
- network/port/firewall snapshot.

No active load. No data mutation. No restart. No configuration change.

## 13. Correction Mapping

CR-01 resolved by explicit run-class separation.
CR-02 resolved by hard stop criteria.
CR-03 resolved by data safety rule.
CR-04 resolved by environment freeze requirements.
CR-05 resolved by observability limitation.
CR-06 resolved by read-only network verification contract.
CR-07 resolved by prohibiting pressure/failure runs in Round 1.
CR-08 resolved by run ledger schema.
CR-09 resolved by demo/placeholder claim boundary.
CR-10 resolved by explicit E2-APPLICATION deferment.

Re-challenge required before E2INFRA-RUN-A001 is recorded as empirical evidence.
