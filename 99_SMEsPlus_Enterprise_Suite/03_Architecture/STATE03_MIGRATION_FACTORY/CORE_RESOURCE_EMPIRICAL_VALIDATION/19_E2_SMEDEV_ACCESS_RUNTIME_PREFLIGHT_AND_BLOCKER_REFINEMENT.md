# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2 — SMEDEV Access, Runtime Preflight & Blocker Refinement

Status: MATERIAL DELTA VERIFIED — ACCESS RESOLVED / PRODUCT RUNTIME STILL HOLD
Jira: ERPPLUS-156
Owner: SaaS Team / SMEs Core — Infrastructure + SRE + Database + Security
Reviewer: Independent Architecture Audit / Adversarial Challenge
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Purpose

Record fresh read-only verification of the newly reachable `smedev` Dev/Test candidate Architecture Lab and refine `E2-BLK-01` without overstating empirical readiness.

## 2. Access Evidence

Verification timestamp: `2026-09-11T14:53:06+07:00` onward.

Authorized execution device:
`THPATTARAKRIT-SOLUTION-SERVICE-2.local`

Verified SSH target:
- alias supplied/used by Boss: `smedev`
- IPv4: `103.253.74.216`
- SSH user: `root`
- authentication: public-key login succeeded using the existing authorized ED25519 key on the connected device

Host identity returned by the target:
`smedevlopmemtserver`

Therefore the prior access portion of `E2-BLK-01` is materially resolved for this target.

## 3. Fresh Host Manifest

Verified from the target itself:

- virtualization: `KVM` / QEMU
- OS: `Ubuntu 26.04 LTS`
- kernel: `Linux 7.0.0-30-generic`
- architecture: `x86_64`
- vCPU: `40`
- sockets: `1`
- cores/socket: `40`
- threads/core: `1`
- CPU model exposed to guest: `Common KVM processor`
- RAM: `60 GiB total`, approximately `57 GiB available` at capture
- swap: `8 GiB`
- root disk: `300 GiB`
- root filesystem: ext4, approximately `295 GiB`, `29 GiB used`, `251 GiB available`
- primary interface: `ens18`
- primary IPv4: `103.253.74.216/24`
- default gateway: `103.253.74.1`

This is current VM-level evidence only. It does not prove hypervisor/physical-host capacity or sustainable Cell capacity.

## 4. Runtime / Tooling Manifest

Verified host-level tools:

- Docker `29.1.3`
- Git `2.53.0`
- Python 3 available

Not found at host level:

- Node.js
- npm
- psql client
- redis-server binary
- k6

Absence from host PATH does not imply the corresponding containerized service is absent.

## 5. Running Lab Stack

Fresh `docker ps` / `docker compose ps` evidence showed the following running services:

- `smes-traefik`
- `smes-portainer`
- `smes-pgadmin`
- `smes-postgres` — `postgres:17-alpine`, healthy
- `smes-redis` — `redis:7-alpine`, healthy
- `smes-minio` — pinned MinIO release, healthy
- `smes-prometheus`
- `smes-grafana`
- `smes-loki`
- `smes-promtail`
- `smes-node-exporter`
- `smes-cadvisor` — healthy
- `smes-api`
- `smes-bff`
- `smes-frontend`
- `smes-worker`
- `smes-webapp` — healthy

Network exposure observed at host level:
- public listeners: TCP 22, 80, 443
- selected administration/data services are bound internally/localhost according to the current stack design.

## 6. Lab Configuration Evidence

Lab path:
`/opt/smes-dev`

Compose file:
`/opt/smes-dev/docker-compose.yml`

SHA-256:
`d534ad53342c9660528e03e365f66d2bdfe4c8af8f44ced250b8a1a4b086e306`

The directory is **not** a Git working tree (`NO_GIT_REPO`). Therefore there is no verified product repo/branch/commit provenance for the deployed lab stack.

The stack README describes it as a single-host Dev/Test consolidation and explicitly identifies application components as placeholders.

Important configuration drift was found:
- README references host `103.253.74.215`;
- actual verified SSH/runtime host is `103.253.74.216`.

This requires controlled reconciliation before using the README as authoritative deployment evidence.

## 7. Application-Layer Verification

The current compose file shows:

- `api` image = `traefik/whoami:latest`
- `bff` image = `traefik/whoami:latest`
- `frontend` image = `nginx:alpine`
- `worker` image = `redis:7-alpine` and is documented as a placeholder
- `webapp` = locally built image `smes-webapp:latest`

The `smes-webapp` image was built from `/opt/smes-dev/app/webapp`.

Its Dockerfile uses:
`python:3.12-slim`

Application source is a Flask/Python demonstration that uploads images, converts them, stores objects in MinIO, and stores metadata in PostgreSQL.

Internal health verification returned:
`HTTP 200` with `{"status":"ok"}`.

Therefore the current lab proves infrastructure integration and a demo workload, but it does **not** prove the current clean-room SMEsPlus Node.js product runtime.

## 8. Independent Challenge

The following evidence-inflation paths are rejected:

1. Successful SSH access != executable SMEsPlus product baseline.
2. Healthy PostgreSQL/Redis/MinIO/observability containers != Tenant-aware ERP runtime.
3. `traefik/whoami` API/BFF placeholders != SMEsPlus API/BFF implementation.
4. Python Flask demo != current Node.js product architecture.
5. HTTP 200 health != business outcome / Tenant isolation / Accounting-Inventory integrity proof.
6. 40 vCPU / 60 GiB / 300 GiB VM specification != sustainable Cell capacity.
7. README planned host `103.253.74.215` != current verified host `103.253.74.216` until reconciled.
8. A non-Git `/opt/smes-dev` deployment != exact source branch/commit provenance.
9. Prometheus/cAdvisor availability != per-Tenant attribution evidence.
10. No k6/load-generator baseline means capacity-grade E2 campaigns cannot begin yet.

## 9. Blocker Refinement

Previous blocker:
`E2-BLK-01 — CANDIDATE DEV/TEST LAB INFRASTRUCTURE IDENTIFIED; VERIFIED ACCESS + PROVISIONED SMEPLUS EXECUTABLE RUNTIME BASELINE ABSENT`.

Refined blocker after fresh proof:

`E2-BLK-01 — SMEDEV ACCESS + INFRASTRUCTURE LAB STACK VERIFIED; CURRENT SMEPLUS NODE.JS PRODUCT RUNTIME / SOURCE PROVENANCE / PER-TENANT TELEMETRY / LOAD-GENERATOR BASELINE ABSENT`.

Resolved in this checkpoint:
- verified SSH target/access;
- current VM-level CPU/RAM/disk/network manifest;
- current Docker/DB/cache/object-storage/observability stack presence;
- current compose checksum;
- basic infrastructure-demo health.

Still open:
1. exact `TH-PATTARAKRIT/SMEsPlus` branch+commit deployed to lab;
2. reproducible Node.js build/start/deployment manifest;
3. real SMEsPlus API/BFF/frontend/worker replacing placeholders;
4. Tenant/security/audit path enabled in exercised product runtime;
5. DB migration/schema/index baseline tied to that product commit;
6. per-Tenant application/DB/queue/runtime telemetry;
7. version-pinned load generator and E2 scripts;
8. synthetic multi-Tenant fixture with cross-Tenant negative cases;
9. raw artifact/checksum path for E2 runs;
10. reconciliation of documented `.215` host vs actual `.216` host;
11. fresh hypervisor/physical resource evidence if any Cell-capacity claim depends on it.

## 10. Gate Disposition

`LAB ACCESS = PASS`.

`LAB INFRASTRUCTURE STACK PRESENCE = PASS FOR DEV/TEST PRECONDITION PURPOSES`.

`CURRENT SMEPLUS PRODUCT RUNTIME = HOLD`.

`E2 CAPACITY-GRADE RUN EXECUTION = HOLD`.

`E3 = NOT OPENED`.

`NO NUMERICAL CAPACITY RESULT EXISTS`.

No Evidence = No Progress.
Never Skip Gate.
Boss remains sole Final Approver.
