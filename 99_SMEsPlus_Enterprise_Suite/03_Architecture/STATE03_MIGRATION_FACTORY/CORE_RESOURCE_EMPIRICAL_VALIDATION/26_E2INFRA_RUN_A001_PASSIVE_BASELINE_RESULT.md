# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2INFRA-RUN-A001 — Passive Baseline Result

Status: VERIFIED PASSIVE BASELINE — NOT A CAPACITY RESULT
Jira: ERPPLUS-156
Run Class: A — PASSIVE_BASELINE
Target: `smedev / 103.253.74.216`
Target hostname: `smedevlopmemtserver`
Execution mode: read-only / non-destructive
Start capture: 2026-09-11 15:04 Asia/Bangkok
Reviewer: SMEsPlus Architecture / Governance Review
Verification status: VERIFIED WITH LIMITATIONS

## 1. Raw Evidence

Control-host raw file:
`/Users/admin/Desktop/SMEsPlus/E2_INFRA_EVIDENCE/E2INFRA-RUN-A001_raw.txt`

Raw file size:
`11,695 bytes`

SHA-256:
`c474cffc21b7c09f59496c7c7eaa8702ada9394c2a9b5da14d161299916cfd08`

Environment compose hash:
`d534ad53342c9660528e03e365f66d2bdfe4c8af8f44ced250b8a1a4b086e306`

## 2. Host Snapshot

Observed at passive baseline:
- uptime approximately 19 minutes;
- load average: `0.16, 0.27, 0.40`;
- RAM: 60 GiB total, ~3.6 GiB used, ~57 GiB available;
- Swap: 8 GiB total, 0 used;
- Root filesystem: 295 GiB usable filesystem, 29 GiB used, 251 GiB available, 11% used;
- Docker server/client: 29.1.3;
- Docker Compose: 2.40.3+ds1-0ubuntu1.

These values describe only the observed idle/passive state at the timestamp above.

## 3. Container Passive Utilization Snapshot

Selected observed `docker stats --no-stream` values:
- PostgreSQL: CPU ~6.31%, memory ~56.62 MiB;
- cAdvisor: CPU ~5.87%, memory ~380.5 MiB;
- Loki: CPU ~1.03%, memory ~216.7 MiB;
- Grafana: CPU ~0.73%, memory ~440.7 MiB;
- Redis: CPU ~0.41%, memory ~34.58 MiB;
- Promtail: CPU ~0.34%, memory ~141.6 MiB;
- MinIO: CPU ~0.05%, memory ~192.6 MiB;
- Prometheus: CPU ~0.00% at snapshot, memory ~835.6 MiB.

All values are point-in-time observations, not sustained averages and not capacity limits.

## 4. Service / Telemetry State

The active Prometheus targets observed healthy/up were:
- cAdvisor;
- MinIO;
- Node Exporter;
- Prometheus;
- Traefik.

No PostgreSQL exporter or Redis exporter target is currently active in the observed Prometheus configuration.

## 5. Resource Envelope Limitation

Container inspection confirms no explicit Docker CPU quota and no explicit Docker memory hard limit for the inspected services.

Therefore this run establishes an `UNBOUNDED_SHARED_VM_PASSIVE_BASELINE` only.

It must not be used to infer:
- per-service capacity;
- Tenant capacity;
- Cell capacity;
- Standard package capacity;
- Enterprise crossover;
- SLA;
- Product RPO/RTO.

## 6. Data / Component Baseline Carry-forward

PostgreSQL configuration snapshot remains component evidence only:
- 17.10;
- max_connections 100;
- shared_buffers 128MB;
- effective_cache_size 4GB;
- work_mem 4MB;
- maintenance_work_mem 64MB;
- wal_level replica;
- max_wal_size 1GB;
- checkpoint_timeout 5min;
- synchronous_commit on.

Redis authenticated configuration snapshot:
- 7.4.9;
- appendonly yes;
- maxmemory 0;
- maxmemory-policy noeviction.

MinIO persistent data path remains Docker-volume backed at `/data`.

## 7. Safety Result

No active load was generated.
No service was restarted.
No firewall/network/configuration was changed.
No package was installed.
No database/object/cache data was intentionally modified.
No Product Runtime was created or deployed.

## 8. Run Disposition

`E2INFRA-RUN-A001 = VALID PASSIVE BASELINE EVIDENCE`.

It proves the current lab can be observed and that current idle/shared-host state is measurable.

It does NOT prove sustainable load capacity or isolation behavior.

Next permissible step under current correction is design/review of a low-impact component probe. Active pressure/failure/recovery testing remains HOLD until its own safety/evidence contract is approved.

`E2-APPLICATION = DEFERRED UNTIL DEVELOPMENT`.
`Build / Merge / Deployment / Production = HOLD`.
Boss remains sole Final Approver.
