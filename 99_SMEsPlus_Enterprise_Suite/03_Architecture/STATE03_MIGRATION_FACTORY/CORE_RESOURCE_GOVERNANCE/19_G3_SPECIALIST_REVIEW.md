# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G3 — Specialist Review: Storage / Database

Status: SPECIALIST REVIEW COMPLETE — CHALLENGE REQUIRED
Inputs:
- `17_G3_DATABASE_CAPACITY_AND_LOGICAL_QUOTA_DRAFT.md`
- `18_G3_FILE_ATTACHMENT_ARCHIVE_STORAGE_DRAFT.md`

## 1. Platform / Infrastructure Architecture

Finding P-01: Separation of Tenant logical usage from Cell/platform physical headroom is architecture-consistent and preserves shared STANDARD economics.

Required control: headroom cannot be one scalar percentage. Storage/DB safety must be evaluated across multiple failure dimensions and recovery obligations.

Finding P-02: File/object storage must remain a capability boundary rather than a provider-specific freeze.

## 2. Database Engineering & Performance

Finding DB-01: Raw DB size is unsuitable as the sole customer logical meter in a shared multi-tenant database. PostgreSQL physical sizing functions include implementation structures such as indexes and TOAST; physical amplification can change without a customer commercial event.

Finding DB-02: A Tenant-attributable logical DB meter in shared tables may be expensive or inaccurate if implemented as repeated scans. G6/G8 must define an incremental/reconstructable accounting strategy plus periodic reconciliation rather than a naive full scan per bill cycle.

Finding DB-03: Physical headroom must explicitly consider maintenance/recovery workspace. A DB that appears below disk capacity can still be operationally unsafe if it lacks room for WAL, maintenance, temporary operations or recovery.

## 3. SRE / Performance & Load Testing

Finding SRE-01: Large uploads, archive restores, history imports and report materialization are burst workloads. The model needs admission/preflight and actual-vs-reserved reconciliation tests.

Finding SRE-02: Protected Mode must be tested under both commercial-quota pressure and physical-pool pressure. These are different triggers and must produce deterministic states/reason codes.

Finding SRE-03: Emergency integrity reserve requires proof that it cannot be consumed by ordinary optional jobs.

## 4. Security / Tenant Isolation

Finding SEC-01: Object key/prefix separation is insufficient as the sole authorization mechanism. Canonical Tenant ownership and policy decision must gate object access.

Finding SEC-02: Cross-Tenant deduplication can create existence/inference risks and billing ambiguity. It must not be a customer-visible shared optimization without dedicated security review.

Finding SEC-03: Delete/archive/restore operations must preserve Tenant provenance and legal-hold/retention controls.

## 5. FinOps / SaaS Cost Economics

Finding FIN-01: Customer logical usage should remain stable despite compression, replication or backend implementation changes; otherwise the customer cannot predict cost.

Finding FIN-02: Physical amplification factors must still be measured for Cost-to-Serve. A logical quota that ignores platform amplification economically is acceptable only if package economics incorporate the multiplier later.

Finding FIN-03: Archive can have materially different storage/retrieval economics. Do not freeze Archive price or ratio before G7/G8 evidence.

## 6. Billing / Wallet / Metering Architecture

Finding BILL-01: G2 anti-double-charge rule must apply to stored files, transient generated outputs and processing workload.

Finding BILL-02: Logical release vs physical reclaim must not create unexplained customer statement changes. The customer meter needs a clear effective-time rule.

Finding BILL-03: Customer logical DB meter must not include platform defects, bloat, index tuning mistakes or backup copies as chargeable usage.

## 7. Product Package / Commercial Governance

Finding PROD-01: DB, File and Archive should remain separate entitlement dimensions because customer behavior and cost drivers differ.

Finding PROD-02: Package downgrade below current retained data requires non-destructive over-entitlement/grandfather behavior and customer action path.

Finding PROD-03: No numerical GB values can be treated as package promises at G3.

## 8. Specialist Consolidated Risks Requiring Independent Challenge

1. Logical DB meter may be conceptually correct but operationally unscalable if poorly implemented.
2. Commercial quota and physical headroom could be conflated in enforcement.
3. Emergency operating reserve could become an unbounded bypass.
4. Archive transition could be double-counted while active and archive copies coexist.
5. Logical deletion and delayed physical reclaim could create billing disputes.
6. Cross-Tenant object deduplication may leak existence information.
7. Generated output may be double charged as processing + storage without explicit commercial mapping.
8. Attachment metadata/object authorization may diverge during partial failures.
9. Restore staging can consume more physical capacity than the restored logical object set.
10. Platform physical amplification could be ignored commercially, creating negative margin even when customer logical quotas appear safe.

Disposition: `READY FOR G3 INDEPENDENT CHALLENGE ROUND 1`.
