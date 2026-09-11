# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E2-INFRA — Infrastructure Readiness Matrix

Jira: ERPPLUS-156
Target: smedev / 103.253.74.216
Capture: 2026-09-11T22:26:37+07:00 and follow-up read-only checks
Scope: VDR / Architecture Validation only
Application Development / Product Runtime / Build / Merge / Deployment / Production: HOLD
Final Approver: Boss only

## 1. Executive Disposition

Overall: `INFRASTRUCTURE READINESS = PARTIAL / VERIFIED WITH MATERIAL GAPS`.

This matrix evaluates current Architecture Lab readiness only. It does not certify Production readiness and does not imply Product/Tenant capacity.

## 2. Readiness Matrix

| Area | Verified Evidence | Status | Gate Impact |
|---|---|---|---|
| Compute | 40 vCPU; 60 GiB RAM; ~57 GiB available; swap 0 used; load avg 0.06/0.23/0.31 at capture | PASS for passive lab baseline | Supports continued read-only/passive validation only |
| Storage | Single 300 GiB virtual disk; ext4 root; ~252 GiB available; Docker data on same filesystem | HOLD | No separate data/backup failure domain; no IOPS/latency proof |
| Network | 103.253.74.216/24; gateway 103.253.74.1; Docker zones smes-app/data/edge/ops/storage present | CONDITIONAL PASS | Logical zones exist but segmentation effectiveness not yet proven |
| Firewall | UFW active; inbound OpenSSH/80/443 allowed | CONDITIONAL PASS | Basic host control present; exposure review remains |
| Docker Runtime | Docker 29.1.3; Compose 2.40.3; containers stable >8h at capture | PASS for lab runtime presence | Valid infrastructure-lab substrate |
| Capacity Protection | All inspected containers NanoCPUs=0 and Memory=0 | FAIL / HOLD | No explicit CPU/RAM hard limits; noisy-neighbor protection unproven |
| PostgreSQL | postgres:17-alpine running/healthy; persistent volume present | CONDITIONAL PASS | Runtime presence verified; tuning/backup/recovery and metrics proof incomplete |
| Redis | redis:7-alpine running/healthy; authentication previously verified; persistent volume present | CONDITIONAL PASS | Service available; maxmemory/noeviction baseline creates capacity-control gap |
| Object Storage | MinIO running/healthy; persistent volume; localhost 9000/9001 binding | CONDITIONAL PASS | Presence verified; durability/failure-domain/restore proof incomplete |
| Observability | Prometheus ready; node-exporter/cAdvisor/Traefik/MinIO/Prometheus monitored; Grafana/Loki/Promtail running | HOLD | No PostgreSQL exporter and no Redis exporter; application metrics intentionally deferred |
| Security / SSH | SSH public-key login as root verified; effective PermitRootLogin=prohibit-password, PubkeyAuthentication=yes, PasswordAuthentication=yes | HOLD | Root key access works; password auth remains enabled and hardening review required before stronger readiness claim |
| Patch Baseline | Multiple OS/security updates are available | HOLD | Host is not current to latest available package set; no change executed in this phase |
| Backup Presence | Nightly cron defined; PostgreSQL + MinIO archives exist through 2026-08-31 local | HOLD | Backup evidence is stale relative to 2026-09-11 capture |
| Backup Scheduler | cron service active; /etc/cron.d/smes-backup exists | HOLD | Schedule exists but backup.log stopped updating on 2026-08-31; execution continuity not proven |
| Restore / Recovery | No restore/recovery script or completed restore evidence found in inspected paths | FAIL / HOLD | Recovery readiness not proven |
| Image Reproducibility | Several images use `latest`; compose file itself has SHA-256 evidence | HOLD | Environment cannot yet be called fully reproducible |
| Product Runtime | Demo/placeholder only by phase design | DEFERRED | Not applicable to VDR infrastructure readiness; future Development proof obligation |

## 3. Verified Strengths

1. Architecture Lab target is reachable by SSH and stable enough for passive evidence capture.
2. Compute headroom is currently high at idle/passive state.
3. Core infrastructure components are running.
4. Docker network zones and host firewall are present.
5. Persistent Docker volumes exist for PostgreSQL, Redis, MinIO and observability services.
6. Monitoring substrate exists and can observe host/container/edge/object-storage layers.

## 4. Material Gaps

### IR-GAP-01 — Capacity protection absent
All inspected containers have no explicit CPU or memory limit. No safe noisy-neighbor conclusion can be made.

### IR-GAP-02 — Storage failure-domain separation absent/unproven
Root, Docker data and local backup artifacts are on the same 300 GiB virtual disk/filesystem from the guest perspective.

### IR-GAP-03 — Database/cache observability incomplete
Prometheus has no PostgreSQL exporter and no Redis exporter in the inspected configuration.

### IR-GAP-04 — Backup continuity stale
Backup cron is installed and cron is active, but the backup log and latest archives stop at 2026-08-31.

### IR-GAP-05 — Restore proof absent
No controlled restore/reconciliation evidence was found.

### IR-GAP-06 — Image reproducibility incomplete
Multiple services use floating `latest` tags.

### IR-GAP-07 — Security hardening incomplete
SSH public-key access is proven, but `PasswordAuthentication yes` remains effective. This is a hardening gap, not a current connectivity failure.

### IR-GAP-08 — Patch currency incomplete
Available OS/security updates were observed. No patching was executed because this session remains read-only/control-first.

## 5. Safe Work Allowed Now

Allowed without Product Development:
- further read-only evidence capture;
- checksum/manifests;
- passive baseline repetition;
- configuration review;
- network attachment analysis;
- backup scheduler/root-cause investigation;
- restore procedure design;
- low-impact probes only after controlled probe contract and challenge.

Not allowed yet:
- uncontrolled stress/saturation;
- failure injection;
- service restart;
- firewall/network/config modification;
- package installation/update;
- production readiness declaration;
- Product/Tenant capacity claims.

## 6. Gate Disposition

`E2-INFRA INFRASTRUCTURE READINESS MATRIX = ESTABLISHED`.

`OVERALL READINESS = PARTIAL / VERIFIED WITH MATERIAL GAPS`.

`PASSIVE BASELINE = VALID`.

`ACTIVE PRESSURE / FAILURE / RECOVERY = HOLD`.

`E2-APPLICATION = DEFERRED UNTIL DEVELOPMENT`.

No Evidence = No Progress.
Never Skip Gate.
