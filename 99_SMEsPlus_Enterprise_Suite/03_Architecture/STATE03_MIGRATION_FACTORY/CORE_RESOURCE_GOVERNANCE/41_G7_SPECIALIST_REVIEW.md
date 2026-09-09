# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G7 — Specialist Review: Backup / Restore / DR Capacity

Status: SPECIALIST REVIEW COMPLETE — MATERIAL CORRECTIONS REQUIRED
Reviewed evidence: `40_G7_BACKUP_RESTORE_DR_CAPACITY_DRAFT.md`
Review units: Platform/Infrastructure, Database Engineering, SRE/Performance, Security/Tenant Isolation, FinOps, Billing/Wallet, Product/Commercial Governance
Final Approver: Boss only

## 1. Review result

The draft is directionally coherent with G3/G5/G6, but it is NOT yet a freeze candidate. Specialist review identified 30 material controls that must be incorporated before independent challenge disposition.

## 2. Findings

| ID | Severity | Finding | Required correction |
|---|---|---|---|
| SR-01 | Critical | Historical backup may cover a different Tenant membership set than today's Cell placement. | Recovery set must preserve time-effective Tenant membership/placement lineage; never infer historical scope from current placement. |
| SR-02 | Critical | Restoring placement/control metadata can resurrect an older Placement Epoch and create split-brain. | Recovery authority must be monotonic/fenced; restored historical epoch cannot become write-authoritative without a new higher recovery epoch/authority event. |
| SR-03 | Critical | Tenant-selective scratch restore can expose all Cell tenants to recovery operators/services. | Require isolated recovery trust zone, scoped service identity, audited extraction, egress controls and explicit prohibition on customer/raw access. |
| SR-04 | Critical | Selective Tenant merge may duplicate or erase finalized accounting/inventory facts. | Require domain-level reconciliation/correction contracts and business-key/idempotency proof before forward repair/merge. |
| SR-05 | Critical | DB PITR and object-store versions may not share one transactional boundary. | Require recovery consistency classification: `COHERENT / RECONCILABLE / INCOMPLETE`; unresolved mismatch cannot route production writes. |
| SR-06 | Critical | External side effects are not recoverable by infrastructure restore. | Maintain external-effect reconciliation register and outcome proof for payments, tax submissions, partner APIs, notifications and other irreversible actions. |
| SR-07 | Critical | Wallet/usage operational ledgers cannot be naively rolled back because money/payment evidence may exist after the restore point. | Infrastructure recovery must preserve/reconstruct economic identities and use reconciliation/compensating lineage rather than silent financial-history rollback. |
| SR-08 | High | RPO ignores recoverability of control-plane/placement authority. | RPO readiness must include placement/routing/identity control data needed to safely re-establish Tenant authority. |
| SR-09 | High | RTO omits backlog catch-up and post-restore queue/integration recovery. | Include queue catch-up, deferred workload, cache/index warm-up, external reconciliation and observation in measured service-restoration objective. |
| SR-10 | High | Backup health failure is not connected strongly enough to Cell admission. | Protection degradation must feed Cell state/admission; severe unresolved backup/WAL risk can veto new placement/heavy work while preserving safe critical business continuity. |
| SR-11 | High | Recovery workspace could exhaust Cell/platform headroom during an incident. | Reserve DR capacity separately; recovery headroom is a hard eligibility dimension, not an afterthought. |
| SR-12 | High | Long incremental chains may reduce backup cost but make RTO infeasible or increase chain risk. | G8 must measure chain depth, combine/replay time, dependency loss risk and synthetic/full consolidation economics. |
| SR-13 | High | Backup verification/restoration itself can become a noisy neighbor. | Restore drills/verification need isolated or budgeted execution and cannot consume normal Cell critical reserve unchecked. |
| SR-14 | High | Same authority may be able to destroy production and all backups. | Require independent protection authority/tamper-resistance objective and test deletion/credential-compromise scenarios. |
| SR-15 | High | Key rotation/offboarding can make retained backups unreadable; retaining keys forever can violate security/deletion intent. | Add time-effective encryption-key retention/recovery/destruction contract tied to backup retention generations and legal hold. |
| SR-16 | High | Immutable retention can create uncontrollable physical cost or prevent legally required expiration. | Immutability is generation/time-bounded under approved retention; expiry/destruction must be auditable and policy-driven. |
| SR-17 | High | Schema/application version drift can make old backups technically restorable but operationally unusable. | Recovery manifest must bind application/schema version and define tested upgrade/migration path from recoverable historical versions. |
| SR-18 | High | Restore drill using synthetic/masked data may fail to prove production data-shape compatibility. | Recovery validation strategy must include controlled production-shaped evidence while preserving privacy/security; exact method remains open. |
| SR-19 | High | Data residency rules may be broken by cross-region backup/DR. | Backup, replicas, scratch recovery and DR destination must pass residency/compliance eligibility before copy/restore. |
| SR-20 | High | Enterprise dedicated runtime could still depend on one shared backup/control plane and inherit broad blast radius. | Enterprise isolation claim must explicitly classify backup/control dependencies; dedicated compute alone does not imply dedicated recovery boundary. |
| SR-21 | High | Cell movement can release source before destination has proven recoverability. | Destination protection baseline and recovery-set verification become mandatory source-release proof. |
| SR-22 | High | Recovery after logical deletion may resurrect deleted/expired data. | Current tombstones/retention outcomes must be re-applied after historical restore before production activation. |
| SR-23 | High | Backup copies/versioning may be mistakenly added to customer storage quota. | Protection amplification stays platform Cost-to-Serve unless a separately contracted retention/archive service is explicitly defined. |
| SR-24 | High | Customer-purchased backup option could accidentally define the minimum platform safety baseline. | Platform minimum protection is independent of optional customer backup/retention products. |
| SR-25 | Medium | Network/egress throughput for restore is absent from recovery headroom. | Recovery headroom vector includes network/egress/import throughput and provider/API throttling where material. |
| SR-26 | Medium | Backup catalog corruption could make valid backups undiscoverable. | Catalog/manifest itself needs redundant/reconstructable protection and independent integrity verification. |
| SR-27 | Medium | Recovery authorization can become a privileged bypass path around Tenant isolation. | Destructive/selective restore actions require scoped recovery permission, SoD/risk approval and immutable recovery audit. |
| SR-28 | Medium | RPO/RTO may be falsely reported from configured targets instead of achieved evidence. | Dashboard must distinguish `TARGET` from `MEASURED/ACHIEVED` recovery performance and test age/confidence. |
| SR-29 | Medium | Provider snapshot success can be treated as backup success without application consistency proof. | Backup completion requires manifest/consistency/integrity state, not provider API success alone. |
| SR-30 | Medium | Incident recovery may preserve data but lose audit provenance of the recovery itself. | Recovery events, source/target generations, operators, decisions, reconciliations and release evidence are immutable audit facts. |

## 3. Cross-gate consistency review

### G3 alignment
PASS with corrections: backup/restore amplification remains physical platform overhead; restore workspace must be a separate headroom dimension.

### G5 alignment
PASS with corrections: Cell recovery must preserve authoritative placement/fencing. The most material new issue is SR-02 — a historical Placement Epoch cannot regain authority after restore.

### G6 alignment
PASS with corrections: usage/wallet/economic identities survive restore. Financial history cannot be silently rewound merely because infrastructure state is recovered to an older point.

## 4. Specialist recommendation

`REWORK WITH TARGETED CORRECTIONS`.

The architecture should remain mechanism-neutral but must explicitly freeze the following candidate concepts before G7 can pass:
- time-effective recovery membership;
- monotonic recovery authority;
- coherent/reconcilable/incomplete recovery-set classification;
- isolated Tenant-selective recovery trust zone;
- domain/economic external-effect reconciliation;
- achieved-vs-target RPO/RTO evidence;
- separate DR capacity reserve;
- tamper-resistant backup authority;
- key lifecycle tied to backup generations;
- application/schema recovery compatibility;
- residency eligibility;
- platform minimum protection independent of customer add-ons.

Status: `READY FOR G7 INDEPENDENT CHALLENGE ROUND 1`.
