# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G7 — Independent Adversarial Challenge Round 1

Status: CHALLENGE COMPLETE — CORRECTION REQUIRED
Gate: G7 — Backup / DR
Challenged evidence:
- `40_G7_BACKUP_RESTORE_DR_CAPACITY_DRAFT.md`
- `41_G7_SPECIALIST_REVIEW.md`
Independent role: Architecture Audit / Adversarial Challenge
Final Approver: Boss only

## 1. Challenge rule

The challenge assumes backups fail at the worst useful time, operators make mistakes, shared-Customer boundaries are under stress, financial/business truth cannot be casually rewound, and the DR mechanism may itself become a noisy-neighbor or security threat.

`Configured backup != recoverable system`.

`Recoverable infrastructure != reconciled ERP business truth`.

## 2. Adversarial attacks

| CH | Attack / failure mode | Severity | Required architecture response |
|---|---|---|---|
| CH-01 | A Cell backup from T-1 is restored after several Tenants moved out/in. Current placement list is used to decide restore scope. | Critical | Recovery set preserves time-effective Tenant membership; current placement can never define historical backup contents. |
| CH-02 | Restored placement database contains epoch 184 while production had already reached epoch 220. Router accepts 184 and reopens old Cell writes. | Critical | Recovery activation creates/validates monotonic authority greater than all known prior epochs; historical epoch is evidence only, never automatically authoritative. |
| CH-03 | Shared DB PITR is used to "restore Tenant A" and rolls Tenant B/C backward too. | Critical | Tenant-selective restore cannot use destructive whole-shared-DB rollback; use isolated recovery + controlled extraction/forward repair. |
| CH-04 | Scratch restore contains all tenants and a support operator exports the wrong tenant. | Critical | Isolated recovery trust zone + scoped machine identity + Tenant proof + egress control + immutable audit; no normal customer/support raw browse. |
| CH-05 | DB recovers metadata at 10:00, object store has only 09:57 versions, producing broken invoices/drawings. | Critical | Recovery set has consistency classification and object/DB manifest reconciliation; incomplete set cannot enter normal write service. |
| CH-06 | Object store has a newer file than DB metadata and recovery accidentally exposes an uncommitted object. | High | Canonical G3 retained-state/manifest governs activation; orphan/newer physical copies remain quarantined until metadata provenance is valid. |
| CH-07 | Payment was sent externally at 10:03, DB rolls back to 10:00, job replays and charges customer again. | Critical | External-effect outcome reconciliation + canonical economic/idempotency identity must run before replay. |
| CH-08 | Tax submission/reference was accepted externally after recovery point but local state is rolled back. | Critical | External regulatory/business side effect registry and authoritative reconciliation before business state is finalized. |
| CH-09 | Wallet funding callback existed after the recovery point; rollback deletes spendable funding history then replay settles usage differently. | Critical | Wallet/economic evidence cannot be treated as ordinary rollback state; reconstruct/reconcile from canonical external/internal identities and append compensating lineage. |
| CH-10 | Metering events replay from restored queue and double charge. | Critical | G6 economic-event dedupe and settlement idempotency survive recovery; placement/recovery generation is lineage, not charge identity. |
| CH-11 | Backup succeeds but encryption key required for restore was rotated/deleted. | Critical | Key-generation linkage, restore-key health checks and retention/destruction contract tied to backup generations. |
| CH-12 | Same privileged credential can delete primary data, replicas and backups. | Critical | Independent/tamper-resistant protection authority; compromise-path test mandatory. |
| CH-13 | Immutable backup is retained indefinitely due to misconfiguration, creating uncontrolled cost and privacy exposure. | High | Immutability is bounded by approved retention/legal hold; expiration/destruction policy auditable and tested. |
| CH-14 | Deleted customer's data is restored from old backup and becomes active again. | Critical | Post-restore forward application of tombstones/offboarding/retention state before routing; terminated Tenant cannot be reactivated by backup alone. |
| CH-15 | Legal hold was added after backup point; restore loses the hold and permits deletion. | Critical | Current authoritative legal-hold/retention controls must be re-resolved after recovery; historical policy snapshot alone cannot weaken current hold. |
| CH-16 | Old backup uses schema N-4 and current application cannot start against it. | High | Recovery compatibility matrix, versioned schema manifest and tested restore->upgrade path. |
| CH-17 | Backup software reports success but manifest/checksum is corrupt. | High | Backup is not `VERIFIED` until chain/dependency/integrity checks pass; provider API success is insufficient. |
| CH-18 | Incremental parent backup is expired while descendants remain. | High | Catalog dependency graph blocks unsafe parent deletion and detects orphan chains. |
| CH-19 | Incremental chain is technically valid but takes 18 hours to combine/replay, violating business expectations. | High | G8 measures achieved RTO against chain depth and compares full/synthetic/incremental strategies economically. |
| CH-20 | WAL archival falls behind and local WAL disk fills, taking Cell DB offline. | Critical | WAL/archive backlog is a Cell health/safety signal; capacity reserve, alerting and admission restrictions before exhaustion. |
| CH-21 | Backup job saturates DB I/O at month-end and blocks accounting close. | High | Protection jobs have resource budgets/scheduling; correlated business-close load included in G8 tests. |
| CH-22 | Restore drill runs inside production Cell and itself causes outage. | High | Restore verification uses isolated/budgeted environment; drill resource reservation cannot consume critical production reserve. |
| CH-23 | Disaster requires 2x DB + object copy + scratch extraction but no capacity is reserved. | Critical | Recovery workspace/headroom is a first-class platform reserve dimension and destination hard-veto criterion. |
| CH-24 | Cross-region restore saturates network/egress or provider API limits. | High | Recovery headroom includes network/egress/API throttling; RTO evidence includes data transfer time. |
| CH-25 | DR destination violates Thailand/data residency/customer contract. | Critical | Residency/compliance hard veto for backup copy, replica, scratch and recovery destination. |
| CH-26 | Cell is considered isolated but every Cell shares one backup catalog/control plane that fails globally. | Critical | Classify backup/control dependencies as Cell-local/scoped/global; blast-radius claims cannot exceed global dependency proof. |
| CH-27 | Enterprise customer has dedicated app/DB but shares destructive backup credentials with all Standard Cells. | High | Enterprise recovery isolation claims must include backup/control-plane boundaries, not just runtime. |
| CH-28 | Source Cell is released immediately after migration; destination backup fails that night. | Critical | Destination protection baseline/verified generation is mandatory before source capacity release. |
| CH-29 | Backup generation taken during Cell movement spans source/destination ambiguously. | High | Recovery manifest records movement/placement epoch lineage and prohibits ambiguous authoritative recovery set without reconciliation. |
| CH-30 | DR control plane is down and router round-robins Tenant to any healthy Cell. | Critical | Fail-static/fail-safe placement semantics remain; never guess Tenant location. |
| CH-31 | Restore of identity/permissions resurrects revoked admin privileges. | Critical | Current security revocations/high-risk identity state must be reconciled after historical restore before normal access. |
| CH-32 | Restore of secrets/config reintroduces compromised credentials. | Critical | Secret recovery follows separate rotation/compromise policy; historical secret material is not blindly reactivated. |
| CH-33 | Recovery operator uses raw shared backup to answer customer export request. | Critical | Customer export is an application-level authorized process; raw shared backup is never customer delivery surface. |
| CH-34 | Production backup is replicated to analytics/testing and exposed to broader users. | Critical | Protection copy purpose limitation; DR backups cannot be silently repurposed as test/analytics datasets. |
| CH-35 | Backup copy count is billed as customer storage. | High | Platform protection amplification remains Cost-to-Serve; only separately contracted customer retention/archive service may create chargeable entitlement. |
| CH-36 | Customer declines optional backup add-on; platform disables minimum recoverability. | Critical | Platform minimum backup/DR protection is invariant and independent of optional commercial products. |
| CH-37 | RPO dashboard says 5 minutes because configured WAL interval is 5 minutes, but object replication lag is 40 minutes. | Critical | Report achieved/recoverable RPO from weakest coherent component, not configured target. |
| CH-38 | RTO dashboard excludes incident declaration, reconciliation and queue catch-up. | High | RTO definition includes complete recover-to-usable-service chain; target vs achieved values separate. |
| CH-39 | Recovery completes technically but audit trail cannot prove which backup/generation/operator changed data. | Critical | Recovery action itself is immutable audited business/platform evidence linked to incident and recovery set. |
| CH-40 | A malicious/corrupt backup is restored directly into production and propagates compromise. | Critical | Clean recovery zone, integrity/corruption assessment and staged validation before re-entry. |
| CH-41 | Backup catalog is corrupted; backup blobs exist but cannot be located or mapped. | High | Catalog must be redundantly protected/reconstructable from manifests/object metadata and tested. |
| CH-42 | Many Cells fail simultaneously due to common regional/provider dependency, exceeding reserved recovery capacity. | Critical | G8 must test correlated multi-Cell disaster classes and recovery concurrency; recovery capacity cannot assume one Cell failure only without evidence. |

## 3. Contradiction search

No contradiction was found with the G3 rule that backup/replication/restore staging is physical platform overhead rather than naive customer logical quota.

No contradiction was found with G5 bounded-Cell architecture, but G7 materially limits the meaning of Cell blast radius: a Cell is only independently recoverable to the extent its backup, control-plane, key, routing and regional dependencies are proven independently resilient.

No contradiction was found with G6 metering/wallet architecture, but G7 adds a strict rule that financial/economic ledgers cannot be blindly time-rolled backward with ordinary infrastructure data.

## 4. Challenge disposition

`FAIL ROUND 1 — TARGETED CORRECTION REQUIRED`.

Correction must explicitly incorporate CH-01 through CH-42. Numerical RPO/RTO, retention, technology and provider selection remain HOLD.

After correction, perform independent re-challenge before G8 entry.
