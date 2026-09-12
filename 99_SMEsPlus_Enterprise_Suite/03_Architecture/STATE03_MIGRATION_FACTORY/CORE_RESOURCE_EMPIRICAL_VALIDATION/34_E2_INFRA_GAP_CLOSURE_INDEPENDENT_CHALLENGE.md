# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# 34 — E2-INFRA Gap Closure Independent Challenge

Status: HOLD — CONTROL CORRECTIONS REQUIRED
Jira: ERPPLUS-156
Scope: VDR / Architecture Validation only

## Adversarial Challenge

1. A backup file exists but restores to an unusable database: current evidence would falsely pass continuity.
2. Both live data and backup archives are lost with the same guest disk: current backup location provides no host/storage failure separation.
3. Backup resumes after 11 days with no explanation: one successful run hides an extended protection gap.
4. Gzip integrity passes but SQL is logically incomplete: archive integrity is not business/data integrity.
5. MinIO tar opens but metadata/object consistency is invalid: archive readability is not usable recovery.
6. `smes-data internal=true` is cited as isolation while a multi-homed service bridges app/data/edge/storage zones.
7. Traefik or another multi-homed container becomes a transitive path across zones: network naming alone does not prove deny behavior.
8. Guest ext4 looks healthy while underlying hypervisor storage has no redundancy or failing disks.
9. Prometheus reports all configured targets UP while PostgreSQL/Redis service metrics are absent: monitoring can look green while critical data services degrade.
10. Idle CPU/RAM headroom is treated as capacity while no container protection limits exist.
11. `latest` images drift between runs, making empirical evidence non-reproducible.
12. Root/public SSH remains available and security updates are pending; a readiness claim ignores hardening state.

## Required Corrections

CR-01 Separate `backup execution`, `backup retention`, `backup failure-domain`, and `restore proof` statuses.
CR-02 Track the 2026-08-31 to 2026-09-11 backup gap as an unresolved incident/evidence gap.
CR-03 Require an isolated non-destructive restore target before running a restore drill.
CR-04 Require PostgreSQL and MinIO restore verification criteria before calling recovery PASS.
CR-05 Produce a zone-to-zone allow/deny matrix and verify actual reachability before network-isolation PASS.
CR-06 Require hypervisor-side storage evidence; guest evidence cannot substitute.
CR-07 Define DB/Redis telemetry minimums before active pressure testing.
CR-08 Define CPU/RAM/queue protection candidates before saturation tests.
CR-09 Freeze image IDs/digests for empirical runs; tag `latest` is not evidence-stable.
CR-10 Keep security hardening as a separate readiness track; do not silently modify SSH/firewall during this gate.

## Challenge Disposition

`E2-INFRA GAP CLOSURE = HOLD FOR CONTROLLED PROOF CONTRACT`.

This HOLD is against over-claiming readiness, not against continuing safe evidence collection.
