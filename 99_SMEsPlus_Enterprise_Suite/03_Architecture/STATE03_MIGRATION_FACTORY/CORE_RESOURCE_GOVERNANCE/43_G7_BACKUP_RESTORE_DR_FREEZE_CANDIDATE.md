# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G7 — Backup / Restore / DR Corrected Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Gate: G7 — Backup / DR
Corrections incorporated: SR-01..SR-30 and CH-01..CH-42
Supersedes for G7 decision use:
- `40_G7_BACKUP_RESTORE_DR_CAPACITY_DRAFT.md`
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Freeze boundary

G7 freezes conceptual protection/recovery contracts only.

G7 DOES NOT freeze numerical RPO/RTO, retention days, backup frequency, region/provider, database topology, storage product, replication factor, encryption/KMS product, DR hot/warm/cold mechanism, failover automation, or customer backup pricing.

## 2. Canonical recovery scopes

Four scopes remain distinct:

1. `PLATFORM CONTROL-PLANE RECOVERY`.
2. `CELL RECOVERY` for a bounded Standard Cell.
3. `TENANT-SELECTIVE RECOVERY` within shared infrastructure.
4. `ENTERPRISE TENANT RECOVERY` for a dedicated environment.

No single backup mechanism is assumed sufficient for every scope.

## 3. Backup, HA and DR are different controls

- HA/failover addresses selected availability failures.
- Backup/PITR provides recoverable historical state.
- DR is the end-to-end operational proof to detect, declare, fence, recover, reconcile, validate, route and resume.

A replica can reproduce corruption. A successful backup operation without verified restore evidence is not sufficient recovery proof.

## 4. Recovery Protection Set and time-effective membership

Each recovery generation has immutable lineage identifying what it actually protected at that time.

Minimum conceptual fields:
- `recovery_set_id` / generation;
- source environment/Cell;
- time-effective Tenant membership set;
- Tenant -> Organization Root -> Company identities covered;
- DB recovery coordinate;
- object/archive checkpoint/manifest;
- Usage/Wallet evidence checkpoint;
- Placement Epoch / movement lineage;
- application/schema compatibility version;
- encryption/key generation reference;
- parent/base backup dependencies;
- integrity and verification state;
- retention/legal-hold state;
- created/verified timestamps.

Current Cell placement can never be used to infer the historical Tenant contents of an older backup.

## 5. Recovery Consistency Classification

A recovery set is classified as:

- `COHERENT` — required DB/object/ledger/control coordinates are proven mutually consistent for the scope.
- `RECONCILABLE` — known skew exists but deterministic evidence/rules can reconcile it before production activation.
- `INCOMPLETE` — required component/dependency/evidence is absent or inconsistent beyond safe reconciliation.

Only COHERENT or successfully reconciled sets may become production-authoritative.

Provider snapshot/API success alone does not establish COHERENT status.

## 6. DB / object / archive consistency

Attachment/business metadata and binary content are reconciled through G3 canonical commit states and recovery manifests.

Recovery detects at minimum:
- metadata without object;
- object without metadata;
- wrong object version/hash/size;
- active/archive state mismatch;
- deleted/tombstoned object resurrected from historical copy.

Uncommitted/orphan physical objects never become active solely because a backup contained them.

## 7. Physical PITR != Tenant-selective rollback

In shared infrastructure, physical database PITR/continuous archiving may recover an entire database/cluster rather than one Tenant subset.

Therefore Standard Tenant-selective recovery uses the conceptual pattern:

`Verified recovery set -> isolated scratch recovery trust zone -> restore shared recovery state -> authorize/select canonical Tenant -> extract/reconstruct Tenant-owned data -> domain/economic reconciliation against current authoritative state -> controlled forward repair/merge or explicitly approved replacement -> validate -> audit -> release scratch`.

Destructive whole-shared-database rollback is prohibited as a Tenant-only recovery operation.

## 8. Isolated Recovery Trust Zone

Scratch/recovery environments containing shared backups are high-sensitivity environments.

Mandatory controls:
- no ordinary customer or support-user access;
- scoped recovery service identity;
- least privilege and Tenant-scoped extraction authorization;
- network/egress restrictions;
- audited access and exports;
- no reuse as analytics/test data without separate governed transformation/authorization;
- automatic/controlled teardown and data disposal after recovery purpose completes;
- residency/compliance eligibility equal to or stronger than source obligations.

Raw shared backup is never a customer export surface.

## 9. Monotonic placement/recovery authority

Historical placement state cannot regain write authority merely because it was restored.

Frozen invariant:

> Recovery activation must establish a monotonic/fencing-equivalent authority event that is provably newer than all known prior authoritative Placement Epochs for the affected Tenant/Cell scope.

Rules:
- historical restored epoch is evidence only;
- stale source/session/worker authority is rejected after recovery cutover;
- control-plane outage never authorizes random/round-robin Tenant routing;
- source/destination split-brain is a hard correctness veto.

Exact epoch technology remains open.

## 10. ERP truth: recover then repair, not blind rollback

Finalized accounting, inventory, tax, payment, approval and audit facts are not casually erased by infrastructure time travel.

Default pattern:
`recover historical evidence -> identify loss/corruption -> reconcile later legitimate facts/external side effects -> forward repair/correction/replay with provenance`.

Whole-Tenant replacement/rollback requires explicit incident-class authority and domain reconciliation because it may erase legitimate post-recovery-point business truth.

Domain reversal/correction semantics continue to govern finalized facts.

## 11. External side-effect reconciliation

Infrastructure restore cannot undo external reality.

Recovery maintains outcome/reconciliation evidence for material external effects such as:
- payment provider transactions;
- bank/payment confirmations;
- tax/regulatory submissions;
- external accounting/e-document references;
- partner API writes;
- email/notification delivery where business-significant;
- integration acknowledgements.

Before replay, each side effect is classified as `NOT EXECUTED / EXECUTED-PROVEN / FAILED-PROVEN / IDEMPOTENT-REPLAYABLE / AMBIGUOUS-HOLD`.

Ambiguous material effects block silent replay.

## 12. Usage / Wallet / financial continuity

G6 economic-event identity, Usage Evidence and Wallet history survive infrastructure recovery.

Mandatory:
- no double charge from replay;
- restored older wallet state cannot erase later proven funding/settlement;
- payment/funding callbacks remain idempotent by external settlement identity;
- inconsistencies enter `HELD / RECONCILIATION REQUIRED`;
- corrections use append/compensating lineage, not destructive historical rewrite;
- infrastructure recovery never fabricates unsecured customer debt.

## 13. Current security/retention controls override stale historical state where required

After historical restore, the system must re-resolve current authoritative high-risk controls before production activation, including where applicable:
- revoked/disabled identities;
- compromised/rotated secrets;
- Tenant offboarding/termination;
- legal hold;
- current retention/tombstone outcomes;
- security policy changes required after incident.

Historical restore cannot resurrect revoked admin access, compromised credentials or intentionally deleted active data without explicit authorized exception.

## 14. Deletion / tombstone / backup retention

Live logical deletion and backup physical retention remain separate.

- protection copies may retain logically deleted data only for approved protection/legal-hold period;
- such copies are platform protection overhead, not active logical Tenant quota;
- restore into production must forward-apply authoritative tombstones/offboarding/retention state;
- expired backup generations and their keys are disposed under auditable policy;
- legal hold can extend destruction but does not make backup normally customer-readable active data.

## 15. Encryption/key lifecycle

Every protected generation must remain decryptable for exactly its authorized recovery lifetime.

Conceptual controls:
- backup generation links to key generation/reference;
- restore readiness verifies key availability/authorization;
- key rotation preserves authorized historical recoverability;
- key compromise triggers controlled re-protection/rotation response as feasible;
- key destruction is tied to backup expiry/legal hold and is audited;
- secret material is not blindly restored into active service if it was revoked/compromised.

No KMS product is frozen.

## 16. Tamper-resistant/destructive-event recovery path

At least one material protection path must remain recoverable when ordinary production authority is compromised.

Required property set:
- backup authority separated from ordinary production mutation/deletion authority;
- tamper-resistant/immutable/retention-controlled generation or technically equivalent protection;
- integrity manifests/checks;
- privileged deletion controls/SoD proportional to risk;
- clean recovery zone;
- corruption/ransomware assessment before production re-entry;
- tested credential-compromise and deletion scenarios.

A writable replica controlled by the same compromised authority is not the sole recovery guarantee.

## 17. Backup chain/catalog integrity

Incremental/differential backup dependencies are first-class lineage.

Rules:
- parent/base dependency graph is explicit;
- required ancestors cannot expire while descendants depend on them;
- catalog corruption does not destroy discoverability: manifests/catalog data must be redundantly protected or reconstructable;
- backup generation state distinguishes `CREATED / INTEGRITY-VERIFIED / CHAIN-COMPLETE / RESTORE-TESTED / EXPIRED / DESTROYED`;
- chain length/dependency depth feeds G8 RTO/cost validation.

## 18. Application/schema/version compatibility

Recovery manifest binds the protected data state to application/schema compatibility metadata.

A backup is operationally usable only if a tested path exists to:
- restore with compatible runtime/schema;
- or restore then apply controlled forward schema/application migrations.

G8 must include old-generation restore compatibility tests. Technology/version numbers remain open.

## 19. RPO — target vs achieved

RPO is end-to-end recoverable business truth, not configured DB archival interval.

Material components include the weakest coherent recovery element:
- DB/WAL/log protection;
- object/file/archive protection;
- Usage/Wallet durable evidence;
- placement/control data;
- required queue/job durability;
- external-effect reconciliation coverage.

Customer/internal dashboards must distinguish:
- `RPO TARGET`;
- `LATEST VERIFIED RECOVERY POINT`;
- `ACHIEVED/MEASURED RPO`;
- freshness/confidence.

Numerical objectives remain HOLD.

## 20. RTO — target vs achieved

Measured usable-service RTO includes:

`detect + declare + fence + reserve/provision recovery capacity + retrieve/combine backup + DB restore/replay + object recovery + schema compatibility work + consistency validation + security/tombstone reconciliation + queue/integration catch-up + business/economic reconciliation + placement authority + routing + observation`.

Restore throughput alone is not RTO.

Numerical RTO remains HOLD until repeated drills.

## 21. DR capacity/headroom vector

Recovery headroom is separately budgeted from customer logical entitlement.

Dimensions include where material:
- source/evidence preservation;
- destination DB/storage;
- scratch selective-recovery environment;
- WAL/log replay;
- object restore/synchronization;
- validation/reconciliation outputs;
- compute/RAM/DB connections/workers;
- network/egress/import throughput;
- provider/API throttling;
- correlated multi-Cell recovery concurrency.

Insufficient recovery headroom is a hard recovery/admission constraint, not something hidden by a package quota.

## 22. Backup/recovery workload governance

Backup, snapshot, verification and restore testing are platform workloads.

Controls:
- Cell-aware scheduling/concurrency;
- resource budgets;
- no unchecked use of critical operating reserve;
- accounting-close/payroll/tax correlated load included in G8;
- restore drills isolated/budgeted from production;
- backup/archival backlog is a safety signal;
- severe unresolved protection degradation can veto new placement/heavy optional work while preserving safe integrity-critical business continuity.

Platform protection workload is Cost-to-Serve, not customer usage.

## 23. WAL/log/archive backlog safety

For WAL/log-based recovery systems, protection lag can become an availability risk as unarchived local logs accumulate.

Architecture must monitor backlog, remaining headroom and archive throughput and enter progressively stronger protection/admission state before physical exhaustion.

Exact thresholds remain HOLD.

## 24. Cell recovery state machine

Candidate conceptual states:

`PROTECTED/READY -> PROTECTION DEGRADED -> RECOVERY DECLARED -> FENCED -> RECOVERY CAPACITY RESERVED -> RESTORING -> RECONCILING -> VALIDATING -> ROUTE-CANDIDATE -> OBSERVATION -> RECOVERED`.

Failure branches:
`INCOMPLETE RECOVERY SET / AUTHORITY CONFLICT / SECURITY HOLD / RECONCILIATION HOLD / CAPACITY HOLD / RESIDENCY HOLD`.

No state may skip required evidence solely to meet a time target.

## 25. Cell movement and Standard -> Enterprise protection continuity

Source capacity is not released until destination proves:
- authoritative placement cutover;
- data/object/ledger reconciliation;
- destination protection policy active;
- verified recoverable baseline or equivalent continuous protection lineage;
- backup/recovery manifest linked across movement;
- no unresolved source/destination recovery ambiguity.

A backup spanning movement must identify source/destination Placement Epoch lineage and cannot be declared coherent while authority is ambiguous.

## 26. Global dependency/blast-radius classification

G5 dependency classes apply to recovery too:
- CELL-LOCAL;
- CELL-SCOPED SHARED;
- PLATFORM-GLOBAL.

Backup catalog, key authority, identity, placement control, routing and region/provider dependencies must be classified explicitly.

A Cell's claimed recovery/blast-radius isolation is limited by its broadest required global dependency.

## 27. Enterprise recovery boundary

Dedicated Enterprise runtime does not automatically prove dedicated recovery isolation.

Enterprise architecture must declare which of DB protection, object backup, key authority, backup catalog, control plane, region and recovery capacity are dedicated vs shared.

Stronger/dedicated RPO/RTO or recovery envelope may be offered only when technically/economically evidenced.

## 28. Platform minimum protection vs customer options

Platform minimum recoverability is a product integrity/safety baseline and cannot be disabled because a customer declines an optional backup/retention product.

Optional commercial services may later provide longer retention, customer-specific recovery objectives or additional export/archive capability, but they cannot define whether SMEsPlus keeps a minimum safe recovery posture.

Protection copies/versioning are platform Cost-to-Serve unless separately contracted as customer-visible retained service.

## 29. Residency/compliance eligibility

Before backup copy, replica, scratch recovery or DR activation:
- region/residency policy;
- customer contractual restrictions;
- regulatory/legal constraints;
- encryption/key locality where material;
- operator/access locality where material
must pass hard eligibility.

No cost/ranking score can override a residency/security hard veto.

## 30. Restore validation / drills

`Backup success != Restore proof`.

Required evidence:
- backup generation/chain completeness;
- checksum/integrity verification;
- key availability;
- DB/object consistency;
- schema/runtime compatibility;
- Tenant isolation;
- tombstone/security reconciliation;
- economic/external-effect reconciliation;
- achieved RPO/RTO;
- recovery capacity peak;
- unresolved findings/corrective closure.

Validation must include production-shaped data behavior under controlled security/privacy constraints. Synthetic-only evidence is insufficient where it cannot reproduce material production data shape/failure behavior.

## 31. Correlated-disaster readiness

G8 must test more than one isolated Cell failure.

Required scenario classes include:
- one Cell corruption;
- control-plane dependency outage;
- region/provider-zone failure where architecture supports it;
- backup authority compromise;
- multiple concurrent Cell recovery;
- object-storage protection lag;
- WAL/archive backlog;
- recovery during accounting-close/high-load period.

No numerical simultaneous-recovery capacity is frozen before tests.

## 32. Recovery observability

Minimum signals:
- latest verified recovery generation;
- latest coherent recoverable point;
- target vs achieved RPO;
- target vs achieved RTO/drill age;
- WAL/log/archive backlog;
- object protection lag;
- chain depth/completeness;
- key-health state;
- catalog integrity;
- restore workspace estimate/headroom;
- Cell/protection state;
- unresolved recovery findings;
- last compromise/deletion recovery test.

Stale/unknown recovery telemetry is not healthy evidence.

## 33. Recovery audit/SoD

High-risk recovery actions create immutable recovery facts:
- incident/recovery ID;
- scope/Tenant set;
- selected recovery set/point;
- actor/service identity;
- approval/SoD evidence where risk warrants;
- source evidence preservation;
- authority/fencing events;
- data changes/merge/correction lineage;
- external/economic reconciliation;
- post-validation and source-release decision.

Super-admin authority cannot silently bypass Tenant isolation, recovery evidence or destructive-change audit.

## 34. G7 freeze-candidate invariants

G7-01 Backup != HA != DR.
G7-02 Backup success without verified restore evidence is not recoverability proof.
G7-03 Recovery set preserves time-effective Tenant membership and protection lineage.
G7-04 Physical shared-DB PITR cannot be assumed to provide Tenant-selective rollback.
G7-05 Tenant-selective recovery uses isolated recovery trust boundaries and controlled extraction/forward repair.
G7-06 Recovery activation requires monotonic/fencing-equivalent placement authority; historical epochs never automatically regain write authority.
G7-07 DB/object/ledger recovery must be COHERENT or explicitly RECONCILED before production activation.
G7-08 Infrastructure restore cannot blindly undo/replay external side effects.
G7-09 Finalized ERP truth is recovered/reconciled/corrected, not casually erased through destructive rollback.
G7-10 Usage/Wallet/economic identities remain idempotent and reconstructable across recovery.
G7-11 Current security revocations, tombstones, offboarding and legal holds are reconciled after historical restore before activation.
G7-12 Backup key lifecycle is tied to authorized recovery lifetime.
G7-13 At least one material recovery path resists ordinary production-control compromise.
G7-14 Incremental dependency chains are explicit and protected from unsafe ancestor deletion.
G7-15 Application/schema compatibility is part of recoverability.
G7-16 RPO/RTO are measured end-to-end and reported as TARGET vs ACHIEVED.
G7-17 Recovery workspace/headroom is a first-class platform capacity dimension.
G7-18 Backup/restore work is platform workload/Cost-to-Serve and is separately governed from Tenant usage.
G7-19 Protection backlog can affect Cell admission before physical exhaustion.
G7-20 Source Cell/environment is not released after movement until destination protection continuity is proven.
G7-21 Cell recovery isolation claims are limited by shared/global backup/control dependencies.
G7-22 Enterprise dedicated runtime does not automatically imply dedicated recovery boundary.
G7-23 Platform minimum recoverability is independent from optional customer backup products.
G7-24 Backup/DR overhead is not naively customer logical quota.
G7-25 Residency/security hard veto applies to protection and recovery destinations.
G7-26 Restore drills and destructive-event tests are mandatory evidence before numerical recovery objectives can freeze.
G7-27 No numerical RPO/RTO/retention/provider/topology/recovery price is frozen at G7.

## 35. External evidence anchors

- PostgreSQL 18 Continuous Archiving/PITR: physical continuous-archive recovery supports point-in-time recovery but restores the database cluster rather than a subset; archival lag can accumulate WAL and threaten availability if storage fills. https://www.postgresql.org/docs/18/continuous-archiving.html
- Azure Architecture Center Deployment Stamps: independent stamps/cells serving Tenant subsets can contain outage blast radius, but repeatable operational design is required. https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp
- AWS SaaS Lens Pool Isolation: pooled resources increase Tenant-isolation/noisy-neighbor/outage-scope complexity and require explicit isolation controls. https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html
- NIST SP 1339 (2026): backup management includes regular backup, testing and recovery-exercise review. https://www.nist.gov/publications/ot-backup-quick-start-guide
- NIST SP 1800-11: destructive-event recovery must restore trustworthy data integrity. https://www.nist.gov/publications/data-integrity-recovering-ransomware-and-other-destructive-events

These are architecture evidence anchors only; they do not freeze vendor or numeric objectives.

## 36. Carry-forward to G8

G8 must quantify/measure:
- full vs incremental/synthetic backup economics and chain depth;
- WAL/log generation/archive throughput/backlog safety;
- object backup/replication/versioning amplification;
- restore workspace peak multiplier;
- DB/object restore throughput;
- queue/integration catch-up time;
- one-Cell and correlated multi-Cell recovery concurrency;
- recovery during month-end/correlated business peaks;
- tamper-resistant copy cost;
- key/catalog/control-plane recovery readiness;
- application/schema historical restore compatibility;
- mixed-package Cell recovery cost distribution;
- Enterprise stronger-recovery economic crossover;
- measured RPO/RTO ranges with confidence.

Status: `READY FOR G7 INDEPENDENT RE-CHALLENGE`.
