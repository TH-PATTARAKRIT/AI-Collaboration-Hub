# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# 35 — E2-INFRA Gap Closure Correction & Proof Contract

Status: CONTROL CORRECTION COMPLETE — FURTHER PROOF REQUIRED
Jira: ERPPLUS-156
Scope: VDR / Architecture Validation only

## 1. Corrected Status Taxonomy

Backup must be tracked as four independent controls:
1. `Backup Execution`
2. `Backup Retention / Continuity`
3. `Backup Failure-Domain Separation`
4. `Restore / Recovery Proof`

Current state:
- Backup Execution = PASS for latest run only
- Backup Retention / Continuity = HOLD due unexplained 2026-08-31 to 2026-09-11 gap
- Failure-Domain Separation = HOLD; backups reside on same guest filesystem
- Restore / Recovery Proof = HOLD; no drill evidence

## 2. Restore Drill Contract — DESIGN ONLY

No restore drill may run against the live lab data path.

Minimum preconditions:
- isolated temporary restore target or disposable DB/container/volume;
- exact backup artifact and checksum;
- explicit no-overwrite/no-live-data rule;
- PostgreSQL import completion criteria;
- schema/object-count or equivalent consistency checks appropriate to current infra-demo data;
- MinIO archive extraction/object readability criteria;
- raw start/end timestamps and logs;
- cleanup plan;
- Specialist Review + Independent Challenge before execution.

## 3. Network Isolation Proof Contract

Create a matrix of:
`Source Service / Source Zone -> Destination Service / Destination Zone -> Expected Allow/Deny -> Actual Result -> Evidence`.

Do not alter Docker networks/firewall during proof collection.
Multi-homed services require explicit architectural justification and negative-path tests.

## 4. Hypervisor / Storage Proof Contract

Guest evidence is insufficient. Required from infrastructure owner / Proxmox layer:
- node identity;
- VM mapping for SMEDEV;
- storage pool type;
- physical disk / RAID / ZFS / LVM-thin state;
- redundancy/replication;
- capacity/free-space;
- physical disk health where available;
- backup repository/failure-domain location;
- snapshot/backup distinction.

## 5. Observability Minimum Contract

Before active DB/Redis pressure testing, evidence must include at least:
- PostgreSQL connections, transaction/activity, locks, DB size/growth, checkpoint/WAL or equivalent relevant indicators;
- Redis memory, clients, ops, evictions, persistence/replication indicators applicable to the chosen mode;
- host/container CPU, RAM, disk, network already present;
- timestamps and stable run identity.

Tool choice is not frozen by this document.

## 6. Capacity Protection Contract

Before saturation testing, define candidate protection boundaries for:
- CPU;
- memory;
- DB connections;
- Redis memory/policy;
- worker/queue concurrency when applicable;
- storage growth;
- monitoring/alert thresholds.

No numerical thresholds are frozen here.

## 7. Reproducibility Control

Empirical runs must record immutable image IDs/digests. Tags such as `latest` are descriptive only and cannot serve as stable evidence identifiers.

## 8. Security Hardening Boundary

SSH/firewall/package update findings remain separate controlled actions. This proof contract does not authorize modification.

## 9. Current Disposition

Safe read-only evidence collection may continue.
Restore execution, network changes, resource-limit changes, package installation and failure injection remain HOLD pending their respective proof contracts and authorization.
