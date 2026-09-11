# E2-INFRA — Infrastructure Readiness Independent Challenge

Session: [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
Jira: ERPPLUS-156
Input: 27_E2_INFRASTRUCTURE_READINESS_MATRIX.md + 28_E2_INFRASTRUCTURE_READINESS_SPECIALIST_REVIEW.md
Challenge role: Independent Architecture Audit / Adversarial Challenge
Final Approver: Boss only

## Challenge Result

`CHALLENGE = HOLD FOR CONTROLLED CORRECTION PACKAGE; NO UPSTREAM RESET REQUIRED`.

The readiness classification is directionally correct, but several attack cases must be made explicit before any stronger E2-INFRA disposition.

## Attack Cases

### CH-01 — Idle headroom falsely treated as capacity
40 vCPU / 60 GiB and low load do not prove sustainable capacity.

### CH-02 — Logical Docker network names falsely treated as isolation
A service attached to multiple networks can bridge intended zones. Zone naming is not enforcement proof.

### CH-03 — Local backup falsely treated as recoverability
Backups on the same guest disk/failure domain can be lost with the guest/storage failure.

### CH-04 — Cron present falsely treated as backup continuity
cron service is active, but artifacts/logs stop after 2026-08-31. Scheduler configuration alone is insufficient.

### CH-05 — Backup file falsely treated as valid backup
Presence of .sql.gz/.tar.gz does not prove integrity, completeness or restoreability.

### CH-06 — Healthy container falsely treated as service readiness
Container health checks may only prove process/port state, not data integrity or dependency correctness.

### CH-07 — Prometheus ready falsely treated as full observability
No PostgreSQL/Redis exporter means key capacity and failure signals remain invisible.

### CH-08 — Firewall active falsely treated as complete security
Host firewall permits SSH/80/443 from Anywhere. Exposure is not yet risk-classified for the Architecture Lab.

### CH-09 — Public-key root access falsely treated as hardened SSH
`permitrootlogin prohibit-password` is stronger than password root login but general PasswordAuthentication remains enabled; account surface remains broader than a key-only administrative model.

### CH-10 — Floating images invalidate reproducibility
Several `latest` tags can change behavior between runs without an explicit config change.

### CH-11 — No resource limit means failure test can affect unrelated services
Active load/failure testing without cgroup/resource boundaries can cause lab-wide collateral impact.

### CH-12 — Recovery target conflation
Infrastructure component restore time must not be called Product RTO or Tenant RTO.

### CH-13 — Guest disk evidence does not prove hypervisor/storage resilience
Guest sees one 300 GiB virtual disk. RAID/ZFS/replication/storage-pool properties are not established by guest evidence.

### CH-14 — Security update count alone is not patch-risk classification
Pending packages require security-impact review; raw count is not equivalent to exploitable risk.

## Mandatory Corrections

CR-01 Freeze claim boundary: passive baseline != capacity.
CR-02 Create network attachment/segmentation proof register.
CR-03 Separate local backup presence from off-host backup readiness.
CR-04 Investigate backup continuity gap without mutating system.
CR-05 Define backup integrity/restore proof contract.
CR-06 Define observability minimum for PostgreSQL/Redis before active capacity work.
CR-07 Define resource-protection prerequisite before active pressure/failure tests.
CR-08 Define image pinning/reproducibility requirement.
CR-09 Define security hardening review items without executing changes.
CR-10 Keep Product RTO/SLA/Tenant capacity deferred.
CR-11 Request hypervisor/storage evidence separately from guest evidence.
CR-12 Require any future correction implementation to use a separate controlled change authorization.

## Gate Impact

E2-INFRA passive evidence remains valid.
No active pressure/failure/recovery authorization is granted by this challenge.
