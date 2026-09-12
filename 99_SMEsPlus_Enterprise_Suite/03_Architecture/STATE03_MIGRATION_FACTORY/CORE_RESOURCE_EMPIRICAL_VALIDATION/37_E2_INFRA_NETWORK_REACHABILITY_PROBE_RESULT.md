# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# 37 — E2-INFRA Network Reachability Probe Result

Status: PARTIAL PROOF — ISOLATION NOT CLOSED
Jira: ERPPLUS-156
Target: `smedev / 103.253.74.216`
Scope: non-destructive VDR / Architecture Validation probe

## 1. Probe Boundary

No container creation, network change, firewall change, restart, package install or configuration mutation was performed.
Existing containers and existing network attachments were used only for TCP/DNS reachability checks.

## 2. Multi-Homed Webapp Result

`smes-webapp` is attached to `smes-app`, `smes-data`, `smes-edge`, and `smes-storage`.

TCP connection probes from the existing webapp container returned:
- `postgres:5432 = ALLOW`
- `redis:6379 = ALLOW`
- `minio:9000 = ALLOW`
- `traefik:80 = ALLOW`
- `prometheus:9090 = ALLOW`

This is direct evidence that a multi-homed service has broad east-west reachability across multiple infrastructure zones.

## 3. Data-Zone Container Probe

The PostgreSQL container is attached only to `smes-data`.
A DNS lookup confirmed `redis` resolves inside the same data zone.
A broader cross-zone lookup probe did not complete within the controlled command window and was terminated without changing runtime state.

Therefore no negative-path isolation PASS is claimed from the incomplete probe.

## 4. Interpretation

- Network zone objects exist and `smes-data` is configured internal.
- Multi-homing materially weakens the meaning of zone separation for the services that span zones.
- Reachability does not by itself prove an architecture defect because expected service flows are not yet frozen.
- A canonical expected allow/deny matrix is required before declaring a route correct or incorrect.

## 5. Disposition

`NETWORK ZONE PRESENCE = VERIFIED`

`MULTI-HOMED BROAD REACHABILITY = VERIFIED`

`NEGATIVE ISOLATION PROOF = INCOMPLETE`

`NETWORK ISOLATION READINESS = HOLD`

No configuration change is authorized by this result.
