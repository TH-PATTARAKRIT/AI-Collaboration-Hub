# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G3 — Storage / Database Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Gate: G3 — Storage / Database Gate
Supersedes for G3 decision use:
- `17_G3_DATABASE_CAPACITY_AND_LOGICAL_QUOTA_DRAFT.md`
- `18_G3_FILE_ATTACHMENT_ARCHIVE_STORAGE_DRAFT.md`
Corrections incorporated: CH-01 through CH-12 from `20_G3_INDEPENDENT_CHALLENGE_ROUND1.md`
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. G3 Freeze Boundary

G3 freezes only the conceptual logical-storage, physical-headroom, lifecycle and enforcement contracts.

G3 does NOT freeze:
- numerical DB/File/Archive quotas;
- per-file limits;
- warning percentages;
- prices/rates;
- storage provider/product;
- shared-schema/schema-per-tenant/DB-per-cell/DB-per-tenant topology;
- backup/replication multiplier;
- exact database engine deployment;
- object-store implementation;
- exact logical DB metering algorithm;
- exact archive retrieval SLA;
- Cell physical thresholds.

## 2. Three Logical Customer Storage Pools

The canonical entitlement dimensions are:

1. `Business Database Logical Usage` — Tenant-attributable structured canonical business facts and materially Tenant-owned application/audit metadata.
2. `File / Attachment Storage` — active retained binary/document content.
3. `Archive Storage` — inactive/long-term retained content under approved lifecycle/retention policy.

These are logical commercial dimensions and never identify a physical Server, DB host, disk, bucket or Cell.

## 3. Customer Logical Usage != Platform Physical Consumption

Customer logical meters must remain stable against implementation-only changes.

Platform physical consumption may include:
- table heap/storage format;
- indexes;
- TOAST/overflow/large-value storage;
- WAL/logs;
- free-space/visibility structures;
- vacuum/bloat/maintenance effects;
- temporary processing space;
- replicas;
- backups/PITR;
- object replicas/versioning/erasure coding;
- restore/migration staging;
- transient export/upload chunks.

These physical dimensions feed safety, telemetry and Cost-to-Serve. They are not automatically customer chargeable usage.

## 4. Business Database Logical Meter Contract

The logical DB meter must be:
- Tenant-attributable from trusted execution/data provenance;
- reconstructable for material billing/dispute timestamps;
- independent from raw shared-database filesystem size;
- implementation-stable enough that index tuning, vacuum or compression changes do not rewrite customer usage.

### 4.1 Metering implementation constraint — CH-01 correction

The future meter SHOULD use incremental/event-derived logical accounting where feasible, with controlled reconciliation to authoritative data/physical telemetry.

A naive full scan of shared tables per billing cycle is NOT accepted as a frozen architecture mechanism.

Any estimation/sampling algorithm must be validated for accuracy, operational cost and dispute reproducibility before it can support chargeable usage.

`No validated evidence = no chargeable DB overage`.

## 5. Physical Database / Storage Headroom Vector — CH-02 correction

`Commercial Limit < Technical Failure Boundary` is a multidimensional safety rule, not one scalar GB inequality.

Conceptual headroom vector includes, where material:
- primary DB/data capacity;
- transaction/WAL/log reserve;
- temporary/query/workspace capacity;
- maintenance/vacuum/index-operation reserve;
- replication/failover obligations;
- backup/recovery/restore staging;
- object/file storage available capacity;
- archive capacity;
- I/O/performance pressure associated with storage growth.

A Tenant entitlement is admissible only while Cell/platform evidence shows a safe operating region remains after required reserves.

## 6. Staged Capacity State Machine

Canonical conceptual states:

`NORMAL`
-> `INFORMATION`
-> `WARNING`
-> `CAPACITY ACTION REQUIRED`
-> `PROTECTED MODE`
-> `HARD CAP / EMERGENCY SAFETY`.

Triggers must distinguish:
- Tenant logical entitlement pressure;
- Cell/platform physical headroom pressure;
- retention/legal-hold pressure;
- heavy-workload temporary workspace pressure.

Each state transition must carry reason code, evidence timestamp and applicable action policy.

Exact thresholds remain HOLD.

## 7. Critical Integrity Reserve — CH-03 correction

Critical ERP workload classification is platform-governed, not customer self-declared.

A protected physical operating reserve may be maintained for explicitly classified integrity-critical operations where technically safe.

Rules:
- reserve is finite;
- ordinary optional/heavy workloads cannot consume it;
- reserve is not unlimited free commercial entitlement;
- sustained over-entitlement creates remediation/review obligation;
- emergency physical-safety/correctness veto can block new writes when the reserve or failure boundary is endangered.

The architecture promises integrity control, not infinite processing after capacity exhaustion.

## 8. Attachment/Object Canonical Commit Contract — CH-04 correction

Default logical boundary:

`Transactional DB = canonical metadata/ownership/business relation`

`Object/File Storage capability = retained binary content`.

Attachment activation must handle partial failure conceptually through controlled states such as:

`UPLOAD_PENDING`
-> `OBJECT_RECEIVED`
-> `INTEGRITY_VERIFIED`
-> `METADATA_COMMIT_PENDING`
-> `ACTIVE_RETAINED`

Failure branches:
- `ORPHAN_OBJECT_PENDING_CLEANUP`;
- `BROKEN_REFERENCE_RECOVERY_REQUIRED`.

Customer retained File usage becomes effective only when the object reaches the canonical retained/committed state defined by the future implementation contract.

Orphan/temporary copies created by platform failure handling are platform overhead unless separate evidence proves customer-retained value.

Exact transaction/orchestration technology is not frozen.

## 9. Object Authorization / Tenant Isolation

Object key, path or prefix alone is never sufficient authorization proof.

Every material object action must validate:
- canonical Tenant ID;
- authorized actor/service;
- attachment/business-object identity;
- policy/permission result;
- lifecycle/retention/legal-hold state;
- audit provenance where required.

Cross-Tenant discovery, enumeration, restore and metadata leakage are prohibited.

## 10. Verified Size / Integrity Evidence — CH-12 correction

Client-provided content length/hash is not sufficient for canonical billing or integrity evidence.

The platform must establish verified accepted size/integrity evidence from the received canonical object/process.

Customer logical File usage uses verified canonical values according to the later metering contract.

Exact hash algorithm, checksum mechanism and rounding unit remain HOLD.

## 11. Archive Lifecycle Contract

`Archive != Delete`.

Archive retains the same canonical business/document identity and provenance while moving to an inactive/long-term storage state.

Required archive evidence includes:
- Tenant identity;
- object/business identity;
- source state;
- archive effective timestamp;
- retention/legal-hold state;
- integrity evidence where material;
- restore eligibility;
- supersession/state lineage.

## 12. Archive Transition Attribution — CH-05 correction

One logical retained object has one customer storage attribution at Time T.

During Active->Archive transition:
- temporary active+archive duplicate copies are platform physical overhead;
- logical customer attribution changes only after verified lifecycle commit/cutover;
- no double customer quota/charge may arise solely from implementation copy overlap.

## 13. Deletion / Logical Release / Physical Reclaim — CH-06 correction

Deletion lifecycle must distinguish:

`DELETE_REQUESTED`
-> `RETENTION_CHECK`
-> `LOGICALLY_RELEASED`
-> `PHYSICAL_RECLAIM_PENDING`
-> `RECLAIMED`.

Rules:
- legal hold/mandatory retention can veto logical release;
- customer logical usage reduction follows the canonical logical-release metering rule, not arbitrary backend cleanup timing;
- platform backup/protection copies remaining after valid logical release are platform overhead unless the contract explicitly provides separately retained archive service;
- every state is auditable and reconstructable.

## 14. Compression / Deduplication Stability — CH-07 correction

Customer logical usage must not fluctuate solely because backend compression or deduplication changes.

Default control:
- no cross-Tenant deduplication may affect customer-visible quota, price or observable behavior;
- any future physical cross-Tenant deduplication requires separate security proof against existence/inference leakage;
- such optimization remains below the Tenant logical meter boundary.

## 15. Generated / Transient Output — CH-08 correction

Transient generated output or upload staging with controlled TTL is not retained File usage.

Retained File usage begins only when the output is explicitly/canonically committed for retention.

Processing, API, third-party and retained-storage charges, if later used commercially, must obey the G2 anti-double-charge mapping and be separately disclosed/traceable.

## 16. Upload / Import / Restore / Migration Admission — CH-09 correction

Material storage-growing workloads use a two-envelope preflight:

`Tenant logical entitlement check`
AND
`Cell/platform temporary + final physical headroom check`.

Candidate sequence:

`Estimate -> validate entitlement -> validate physical headroom -> reserve required logical/temporary capacity -> execute -> verify -> commit -> measure actual -> reconcile/release reserve`.

Restore/migration may require materially more temporary physical capacity than its final logical footprint. That amplification is engineering/Cost-to-Serve evidence and is not blindly customer billed.

## 17. Retention-Locked Over-Entitlement — CH-11 correction

A Tenant can exceed current entitlement while holding legally/semantically required content.

Mandatory behavior:
- preserve retained business/audit truth;
- enter explicit over-entitlement/remediation state;
- restrict/preauthorize additional optional/high-growth actions first;
- offer Add-on/Package/Enterprise review or permitted archive/cleanup actions;
- never delete protected evidence merely to fit quota.

## 18. Downgrade / Add-on Expiry

Entitlement shrink below current DB/File/Archive usage requires preflight and non-destructive disposition consistent with G2.

Allowed outcomes include:
- scheduled future effective date;
- controlled grandfather/over-entitlement state;
- permitted cleanup/archive;
- Add-on renewal;
- Package change;
- Enterprise review;
- HOLD.

Active reservations remain lease-aware.

## 19. Economic Boundary — CH-10 correction

Passing a logical storage quota does NOT prove economic suitability.

Physical amplification, archive retrieval cost, retention, backup/replication, restore complexity and sustained workload feed:
- G7 Backup/DR;
- G8 Cost-to-Serve / Load-Test Readiness;
- Package recommendation;
- Standard-to-Enterprise review.

Unexpected internal cost does not authorize retroactive or undisclosed customer charges.

## 20. Physical/Logical Reconciliation

Required conceptual chain:

`Tenant logical DB/File/Archive evidence`
-> `Tenant usage ledger`
-> `physical DB/object/archive telemetry`
-> `Cell/platform headroom state`
-> `amplification/variance classification`
-> `Cost-to-Serve and protection decisions`.

Variance classes include expected physical amplification, platform inefficiency, workload pattern, lifecycle transition, backup/DR overhead, anomaly and measurement defect.

## 21. G3 Invariants — Freeze Candidate

G3-01 Business DB, File/Attachment and Archive are separate logical entitlement pools.

G3-02 Customer logical usage != platform physical storage consumption.

G3-03 Raw shared-database size cannot be the sole customer DB billing meter.

G3-04 Logical DB metering must be Tenant-attributable, reconstructable and operationally validated.

G3-05 Commercial/storage admission is evaluated inside a multidimensional safe physical headroom region.

G3-06 Attachment binaries are separated from transactional DB by default; exceptions require evidence/justification.

G3-07 Object authorization requires canonical Tenant/policy proof, not only key/prefix isolation.

G3-08 Canonical retained File usage begins only after verified retained-state commit.

G3-09 Archive transition cannot double count temporary platform copies.

G3-10 Archive != deletion; retention and lifecycle lineage remain auditable.

G3-11 Logical release and physical reclaim are separate auditable states.

G3-12 Cross-Tenant deduplication cannot affect customer-visible quota/behavior without separate security proof.

G3-13 Transient generated/staging output is not retained File usage until canonical retention commit.

G3-14 Restore/migration admission checks both final logical entitlement and temporary physical headroom.

G3-15 Critical operating reserve is finite, platform-governed and safety-bounded.

G3-16 Retention-locked over-entitlement cannot be solved by destructive deletion of business truth.

G3-17 Physical amplification feeds Cost-to-Serve but is not automatically customer chargeable usage.

G3-18 No numerical quota, price, provider, topology or physical threshold is frozen at G3.

## 22. External Technical Evidence Anchor

PostgreSQL 18 documentation is used only as technical evidence supporting the logical-vs-physical separation:
- `pg_total_relation_size` includes table, indexes and TOAST data: https://www.postgresql.org/docs/18/functions-admin.html
- oversized values can be stored through TOAST/Large Object mechanisms: https://www.postgresql.org/docs/18/lo-intro.html

No PostgreSQL deployment topology is frozen by this evidence.

## 23. Open Evidence Carried Forward

- exact logical DB measurement algorithm and cost;
- exact File/Archive commercial unit and rounding;
- retention/legal matrix by document class;
- object-store technology/failure-domain choice;
- physical amplification ratios;
- backup/replication/versioning multipliers;
- archive retrieval economics;
- cleanup/reclaim lag;
- restore/migration staging factor;
- load-test results for file-heavy/data-heavy scenarios;
- numerical headroom/stop-placement thresholds;
- Cost-to-Serve and package economics.

Status: `READY FOR G3 INDEPENDENT RE-CHALLENGE`.
