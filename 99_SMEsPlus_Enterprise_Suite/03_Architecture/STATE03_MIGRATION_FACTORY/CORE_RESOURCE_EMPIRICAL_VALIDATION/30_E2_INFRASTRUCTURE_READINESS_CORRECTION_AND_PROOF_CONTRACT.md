# E2-INFRA — Infrastructure Readiness Correction & Proof Contract

Session: [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
Jira: ERPPLUS-156
Parent challenge: 29_E2_INFRASTRUCTURE_READINESS_INDEPENDENT_CHALLENGE.md
Scope: VDR / Architecture Validation
Final Approver: Boss only

## 1. Correction Principle

This correction changes evidence interpretation and future proof obligations only. It does not authorize server configuration changes.

## 2. Corrected Claim Boundaries

1. Passive idle headroom is baseline evidence, not capacity evidence.
2. Docker network names/attachments are topology evidence, not isolation proof.
3. Local backup archives are backup-presence evidence, not recoverability evidence.
4. cron configuration is scheduler-intent evidence, not successful backup continuity evidence.
5. Container health is process/service-presence evidence, not end-to-end correctness evidence.
6. Prometheus readiness is observability-substrate evidence, not full observability coverage.
7. Guest disk layout is guest-storage evidence, not hypervisor/storage resilience evidence.
8. Product/Tenant RTO, SLA and capacity remain deferred until the Development/Application lifecycle phase.

## 3. Corrected Readiness Classes

### Class A — VERIFIED NOW
- SSH lab access;
- guest VM identity/OS/KVM;
- 40 vCPU / 60 GiB / 300 GiB guest resource manifest;
- Docker/Compose runtime;
- running infrastructure component presence;
- host firewall presence;
- persistent volume presence;
- passive resource baseline.

### Class B — VERIFIED WITH LIMITATIONS / NEEDS PROOF
- storage resilience;
- network isolation;
- DB/cache observability;
- backup continuity;
- backup integrity;
- security hardening;
- reproducibility;
- capacity protection.

### Class C — DEFERRED
- Product Runtime performance;
- per-Tenant application behavior;
- Product RPO/RTO;
- customer/Tenant/Cell capacity;
- Standard-to-Enterprise crossover;
- commercial pricing/SLA.

## 4. Mandatory Future Proof Contracts

### PC-01 Network Segmentation
Required: intended zone matrix, actual network attachments, allowed/denied flow matrix, low-impact reachability tests, and Independent Challenge.

### PC-02 Storage Resilience
Required: Proxmox/storage-pool evidence, physical/storage failure-domain mapping, guest-volume mapping, and backup target separation evidence.

### PC-03 Backup Continuity
Required: explain why backup/log evidence stopped after 2026-08-31; prove current scheduled execution or record controlled defect. No assumption from cron presence.

### PC-04 Backup Integrity / Restore
Required: checksum/integrity validation, isolated restore target, PostgreSQL restore validation, MinIO object restore validation, reconciliation criteria, raw evidence, and run ledger.

### PC-05 Observability Minimum
Before active capacity tests: PostgreSQL and Redis metrics must be measurable by approved instrumentation or equivalent evidence method; host/container/edge/object-store visibility alone is insufficient.

### PC-06 Capacity Protection
Before active pressure/failure testing: define explicit CPU/RAM/IO/concurrency protection boundaries, blast-radius criteria, abort threshold, reset/recovery path, and independent review.

### PC-07 Image Reproducibility
Record exact image IDs/digests for every run; future controlled hardening should replace floating tags with pinned versions/digests where appropriate.

### PC-08 Security Hardening Review
Review SSH password authentication, root administrative access model, inbound exposure, patch currency, secrets handling, and audit logging. Any modification requires separate change authorization.

## 5. Current Allowed Execution

Allowed:
- read-only inspection;
- passive baseline repetition;
- evidence/checksum capture;
- backup continuity diagnosis without modification;
- network topology/reachability proof under low-impact contract;
- hypervisor evidence collection if authorized access becomes available.

Not authorized by this document:
- package updates;
- firewall changes;
- SSH configuration changes;
- Docker resource-limit changes;
- image updates;
- restarts;
- failure injection;
- destructive restore;
- Product deployment.

## 6. Disposition

`CORRECTION PACKAGE = COMPLETE FOR CLAIM BOUNDARY / PROOF CONTRACT`.

Proceed to Independent Re-Challenge of the corrected interpretation.
