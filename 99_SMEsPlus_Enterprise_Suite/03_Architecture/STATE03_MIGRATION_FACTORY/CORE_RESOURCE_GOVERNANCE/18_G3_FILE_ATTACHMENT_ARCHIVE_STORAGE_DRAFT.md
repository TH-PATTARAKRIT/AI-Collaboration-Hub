# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G3 — File / Attachment / Archive Storage Draft

Status: EXECUTION DRAFT — SUBJECT TO SPECIALIST REVIEW / INDEPENDENT CHALLENGE
Gate: G3 — Storage / Database Gate
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. Storage Domain Separation

G3 separates retained content into three customer-facing logical pools:

1. `Business Database Logical Usage` — structured canonical business facts/metadata.
2. `File / Attachment Storage` — active retained binary/document content.
3. `Archive Storage` — inactive/long-term retained content under approved lifecycle/retention policy.

These are commercial/logical capacity concepts. They do not imply dedicated physical disks, buckets, databases or servers per Tenant.

## 2. Attachment Storage Boundary

Default architecture direction:

`Transactional DB`
- canonical attachment metadata;
- Tenant ownership/security scope;
- business/document relation;
- object identifier/reference;
- content hash/checksum metadata where justified;
- size/media/type/lifecycle metadata;
- retention/legal-hold state;
- immutable/audit lineage as required.

`Object/File Storage capability`
- retained binary object content;
- controlled lifecycle;
- Tenant-aware namespace and authorization;
- replication/protection according to platform policy.

Rule:

> Large retained binary content should not inflate the transactional Business Database footprint without a documented semantic/technical reason.

This is a logical architecture boundary, not a freeze of S3, MinIO, filesystem, cloud provider, storage class, encryption product or exact implementation.

## 3. Tenant Security Boundary

A path/prefix/object key alone is not sufficient proof of Tenant authorization.

Every read/write/delete/restore operation must bind:
- canonical Tenant ID;
- authorized actor/service identity;
- business object/attachment identity;
- lifecycle/retention state;
- permission/policy decision;
- audit provenance where material.

If temporary signed access is used in a future implementation, the token must remain scoped, time-bounded and non-transferable beyond the approved resource contract. Exact mechanism is not frozen.

Cross-Tenant object discovery, enumeration, restore or metadata leakage is prohibited.

## 4. Customer File Usage Meter

Customer-facing File Storage usage should remain stable against backend implementation changes.

Candidate principle:
- retained object logical size is measured from the accepted canonical object size/content contract;
- backend compression, replication, erasure coding, backup copies or physical block allocation do not silently alter customer logical usage;
- physical storage amplification remains Cost-to-Serve/platform telemetry;
- a customer receives storage reduction only when the applicable object is logically released under retention rules and the metering contract considers it reclaimable.

Exact billing unit/rounding/minimum object size remain HOLD.

## 5. Archive Semantics

`Archive` means controlled retained state, not deletion.

Archive entry must preserve:
- Tenant and business-object identity;
- provenance/audit lineage;
- retention/legal-hold rules;
- integrity/hash evidence where applicable;
- retrieval/restore eligibility;
- archive effective timestamp;
- source storage state;
- archive storage evidence.

Archive restore may be a heavy workload and may require capacity preflight/reservation before execution.

## 6. Lifecycle State Model — Conceptual

Candidate retained-content states:

`ACTIVE`
-> `ARCHIVE_ELIGIBLE`
-> `ARCHIVED`
-> `RESTORE_REQUESTED`
-> `RESTORED/ACTIVE`

Separate deletion path where legally/semantically allowed:

`ACTIVE/ARCHIVED`
-> `DELETE_REQUESTED`
-> `RETENTION_CHECK`
-> `LOGICALLY_RELEASED`
-> `PHYSICAL_RECLAIM_PENDING`
-> `RECLAIMED`

Rules:
- legal hold/mandatory retention overrides ordinary cleanup;
- deletion never occurs solely to force quota compliance if business/audit truth must remain;
- logical release and physical reclaim may occur at different times and must be auditable;
- customer usage and platform physical cost may therefore diverge temporarily.

## 7. Upload / Growth Preflight

Material upload operations must support preflight where the expected size is known or bounded.

Candidate flow:

`Request -> validate Tenant/permission -> validate object policy -> check File entitlement -> check storage/Cell/platform headroom -> reserve if needed -> upload -> integrity verify -> commit metadata -> measure actual -> reconcile/release reservation`.

If the upload fails before canonical commit, partial object cleanup must be deterministic and auditable.

Resumable/multipart implementation is not frozen.

## 8. Large Export / Generated Output Boundary

Generated output must not be double counted by default.

Conceptual rule:
- transient generated output with controlled TTL is processing/staging overhead unless separately contracted;
- if the customer elects to retain the output as an attachment/file, it becomes File Storage usage from the retention/commit point;
- one underlying output must not be charged both as retained storage and duplicated storage merely because the platform creates temporary chunks/copies;
- heavy generation may still consume separately governed processing capacity if that commercial unit is explicitly defined later.

## 9. Compression, Deduplication & Customer Fairness

Backend compression/deduplication may improve platform economics but must not make customer charges unstable or expose cross-Tenant information.

Candidate controls:
- customer logical usage is independent of backend compression ratio;
- no customer-visible cross-Tenant deduplication credit by default;
- physical deduplication, if ever used, is a platform implementation concern and requires security analysis against existence/inference leakage;
- Cost-to-Serve may use actual physical savings without rewriting historical customer usage.

## 10. Storage Headroom Model

Storage safety is evaluated at least across:

`Tenant logical allowance`
-> `storage service operational soft limits`
-> `Cell/storage-pool headroom`
-> `platform protection/recovery reserve`
-> `technical hard/failure boundary`.

No single customer quota may be allowed to consume the platform recovery/safety reserve.

Admission/protection must activate before physical exhaustion.

## 11. Staged Enforcement — Storage

Candidate states remain:

`NORMAL -> INFORMATION -> WARNING -> CAPACITY ACTION REQUIRED -> PROTECTED MODE -> HARD CAP`.

In Protected Mode, preferentially restrict high-growth/optional actions where technically safe, such as:
- large attachment uploads;
- mass imports containing retained binaries;
- bulk export retention;
- optional AI/document processing output;
- non-critical archive restore;
- high-volume integration file ingestion.

Do not destroy existing retained evidence. Critical business continuity remains subject to explicit finite operating reserve and physical safety.

## 12. Downgrade / Add-on Expiry

If current File/Archive usage exceeds a future reduced entitlement:
- retain existing content under controlled over-entitlement/grandfather state;
- block or preauthorize new growth first;
- allow customer-approved cleanup/archive lifecycle actions where permitted;
- do not silently delete attachments supporting accounting/tax/audit/business truth;
- preserve active upload/restore reservations under lease-aware rules from G2.

## 13. Backup / Replication Boundary

Customer File/Archive logical usage is not equal to:
- replicas;
- backup copies;
- versioning copies created by platform protection;
- erasure-coding overhead;
- temporary migration copies;
- restore staging;
- disaster-recovery copies.

These physical multipliers are carried into G7/G8 Cost-to-Serve and DR evidence.

## 14. G3 Storage Invariants Candidate

G3-ST-01 Business DB, File/Attachment and Archive are distinct logical capacity pools.

G3-ST-02 Attachment binary storage is separated from transactional DB by default; exceptions require justification.

G3-ST-03 Tenant object authorization requires canonical policy/ownership proof, not only path/prefix separation.

G3-ST-04 Customer File logical usage must not fluctuate solely due to backend compression/replication changes.

G3-ST-05 Archive != deletion; lifecycle and retention lineage remain auditable.

G3-ST-06 Logical release and physical reclaim may differ in time and must reconcile.

G3-ST-07 Temporary generated output is not retained File usage until committed to retention.

G3-ST-08 Cross-Tenant deduplication must not create inference/security or billing ambiguity.

G3-ST-09 Storage enforcement is staged and non-destructive.

G3-ST-10 Numerical storage quotas, rates and technical thresholds remain HOLD.

## 15. Open Evidence Obligations

- object/file storage implementation alternatives and failure domains;
- canonical logical-size definition and rounding policy;
- per-file limits and multipart/resume behavior;
- physical replication/versioning/backup amplification;
- archive retrieval latency/cost profile;
- deletion/reclaim lag and usage statement rules;
- legal/tax/document retention matrix by document class;
- cross-region/DR design;
- large upload/export/restore load tests;
- security challenge of namespace, temporary access and object discovery;
- numerical headroom/threshold evidence.
