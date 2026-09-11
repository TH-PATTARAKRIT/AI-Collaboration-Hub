# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2-INFRA — Read-only Architecture Lab Preflight Evidence Register

Status: VERIFIED PRE-FLIGHT EVIDENCE — NOT A CAPACITY PASS
Jira: ERPPLUS-156
Scope authority: 20_E2_CONTROLLED_SCOPE_CORRECTION_VDR_PHASE_ALIGNMENT.md
Target: `smedev / 103.253.74.216`
Capture time: 2026-09-11 15:01-15:03 Asia/Bangkok
Execution mode: READ-ONLY / NON-DESTRUCTIVE
Build / Merge / Deployment / Production: HOLD
Boss: sole Final Approver

## 1. Host / Lab Baseline

Verified earlier in the same controlled session and carried forward:
- SSH access as root: PASS.
- Hostname: `smedevlopmemtserver`.
- KVM/QEMU VM.
- Ubuntu 26.04 LTS, kernel 7.0.0-30-generic.
- 40 vCPU.
- 60 GiB RAM.
- 300 GiB root disk.
- Target IPv4: `103.253.74.216/24`.

Current compose file:
`/opt/smes-dev/docker-compose.yml`
SHA-256:
`d534ad53342c9660528e03e365f66d2bdfe4c8af8f44ced250b8a1a4b086e306`

## 2. Runtime / Container Resource Controls

Docker runtime is present and the stack is active.

Observed for all inspected containers:
- `NanoCpus = 0`;
- `Memory = 0`;
- restart policy generally `unless-stopped`.

Interpretation:
- no explicit Docker CPU quota is configured at container level;
- no explicit Docker memory hard limit is configured at container level;
- therefore current container-level resource-isolation behavior is not yet bounded by hard CPU/RAM envelopes.

This is not automatically a defect for a Dev/Test architecture lab, but it prevents claiming proven resource-governor isolation.

## 3. Image / Service Baseline

Verified image examples:
- PostgreSQL: `postgres:17-alpine`, image ID `sha256:dc17045ccfd343b49600570ea734b9c4991cf1c3f3302e67df51e3b402dd55c4`.
- Redis: `redis:7-alpine`, image ID `sha256:6ab0b6e7381779332f97b8ca76193e45b0756f38d4c0dcda72dbb3c32061ab99`.
- MinIO: `minio/minio:RELEASE.2023-09-30T07-02-29Z`, image ID `sha256:6262bc9a2730eeaf16be1bf436a3c2bca2ab76639f113778601a9f89c1485b56`.
- Traefik: `traefik:v3.5`.
- Prometheus: `prom/prometheus:latest`.
- Grafana: `grafana/grafana:latest`.
- Loki/Promtail: `latest` tags.
- cAdvisor / Node Exporter: `latest` tags.
- API/BFF remain `traefik/whoami:latest` placeholders.
- Frontend remains `nginx:alpine` placeholder.
- Worker remains a Redis-based placeholder.
- `smes-webapp` remains an infrastructure demo, not SMEsPlus Product Runtime.

Evidence limitation:
several observability/support components use mutable `latest` tags; image IDs are captured but source/version governance is not yet frozen.

## 4. Docker Network Segmentation

Network objects verified:
- `smes-app`
- `smes-data`
- `smes-edge`
- `smes-ops`
- `smes-storage`

Strictly isolated data services:
- `smes-postgres` -> `smes-data` only.
- `smes-redis` -> `smes-data` only.

Observed cross-zone attachments include:
- Traefik -> app, edge, ops, storage.
- API placeholder -> app, data, edge, ops, storage.
- BFF placeholder -> app, data, edge, ops.
- Webapp demo -> app, data, edge, storage.
- Worker placeholder -> app, data, storage.
- MinIO -> edge, storage.
- Prometheus/Grafana -> edge, ops.

Interpretation:
logical zone objects exist, but several service attachments cross multiple zones. Current evidence proves network naming and attachment topology, not least-privilege segmentation.

## 5. Host Port Exposure / Firewall

Host bindings observed:
- Traefik: public `0.0.0.0:80`, `0.0.0.0:443` and IPv6 equivalents.
- Traefik dashboard: `127.0.0.1:8080`.
- MinIO: `127.0.0.1:9000-9001`.
- other inspected data/ops service ports are container-only and not directly host-published.

UFW status: active.
Allowed inbound rules:
- OpenSSH;
- 80/tcp;
- 443/tcp;
with IPv6 equivalents.

Positive control evidence:
- PostgreSQL 5432 is not directly host-published.
- Redis 6379 is not directly host-published.
- MinIO 9000/9001 is localhost-bound at host level.

## 6. PostgreSQL Baseline

Read-only `SHOW` evidence:
- server_version: `17.10`.
- max_connections: `100`.
- shared_buffers: `128MB`.
- effective_cache_size: `4GB`.
- work_mem: `4MB`.
- maintenance_work_mem: `64MB`.
- wal_level: `replica`.
- max_wal_size: `1GB`.
- checkpoint_timeout: `5min`.
- synchronous_commit: `on`.

Interpretation:
current settings are a component baseline only. They do not establish sustainable SaaS workload capacity or production tuning.

## 7. Redis Baseline

Authentication control verified: unauthenticated CONFIG/INFO request is rejected.

Authenticated read-only baseline obtained without exposing the password:
- redis_version: `7.4.9`.
- databases: `16`.
- appendonly: `yes`.
- maxmemory: `0` (no Redis maxmemory ceiling configured).
- maxmemory-policy: `noeviction`.
- timeout: `0`.
- tcp-keepalive: `300`.
- save: `3600 1 300 100 60 10000`.

Interpretation:
Redis authentication is positive evidence. Absence of a maxmemory limit means current runtime does not prove bounded memory behavior under pressure.

## 8. MinIO Storage Baseline

MinIO data mount verified as Docker volume:
`/var/lib/docker/volumes/smes-dev_miniodata/_data -> /data`.

This proves the current data path, not redundancy, off-host durability, restore capability, or production-grade object storage resilience.

## 9. Observability Coverage

Prometheus active targets verified UP:
- Prometheus self;
- Node Exporter;
- cAdvisor;
- Traefik;
- MinIO cluster metrics.

Current Prometheus configuration does NOT show active PostgreSQL exporter or Redis exporter jobs.
Application API metrics job is commented and the API remains placeholder.

Therefore current observability coverage is:
- host metrics: PRESENT;
- container metrics: PRESENT;
- ingress/proxy metrics: PRESENT;
- MinIO metrics: PRESENT;
- PostgreSQL detailed exporter metrics: NOT VERIFIED / ABSENT FROM ACTIVE TARGETS;
- Redis detailed exporter metrics: NOT VERIFIED / ABSENT FROM ACTIVE TARGETS;
- SMEsPlus per-Tenant/application metrics: DEFERRED UNTIL DEVELOPMENT.

## 10. Evidence Classification

PASS / VERIFIED:
- Lab access;
- current host identity;
- container stack presence;
- network objects and attachments;
- firewall/host port bindings at capture;
- PostgreSQL configuration snapshot;
- Redis authenticated configuration snapshot;
- MinIO volume path;
- Prometheus target state for host/container/Traefik/MinIO.

HOLD / INCOMPLETE FOR E2-INFRA PASS:
- explicit CPU/RAM resource envelopes;
- Redis bounded memory control;
- DB/Redis component-level observability coverage;
- least-privilege cross-zone segmentation proof;
- immutable/pinned version policy for all mutable `latest` images;
- safe synthetic component workload design and repeatability evidence;
- controlled pressure/recovery/repeat-run evidence;
- raw run artifact/checksum ledger for empirical runs.

DEFERRED UNTIL DEVELOPMENT:
- SMEsPlus business workload;
- Tenant business fairness;
- product/application metrics;
- business-integrity reconciliation;
- customer/Tenant capacity;
- product RPO/RTO;
- Standard-to-Enterprise crossover.

## 11. Gate Impact

`E2-INFRA PRE-FLIGHT = VERIFIED WITH OPEN CONTROL GAPS`.

`E2-INFRA PRESSURE/RECOVERY RUN = NOT YET AUTHORIZED AS EVIDENCE-COMPLETE`.

`E2-APPLICATION = DEFERRED UNTIL DEVELOPMENT`.

`E3 = NOT OPENED`.

No numerical product capacity result exists.
No Evidence = No Progress.
Never Skip Gate.
