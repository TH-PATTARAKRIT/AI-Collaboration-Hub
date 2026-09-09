# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G3 — Independent Adversarial Challenge Round 1

Status: CHALLENGE COMPLETE — CORRECTION REQUIRED
Gate: G3 — Storage / Database Gate
Independent Role: Architecture Audit / Adversarial Challenge

## Challenge Method

Attack the G3 drafts for false certainty, customer unfairness, hidden physical-risk coupling, tenant-isolation weakness, accounting/audit damage, billing ambiguity and operational failure paths.

## CH-01 — Logical DB Meter Implementation Risk

Attack: The drafts say logical DB usage must be Tenant-attributable but do not constrain how. A naive periodic row-size scan across shared tables could create its own major database workload and still fail to capture semantic payload consistently.

Required correction:
- define meter as an event/incremental/reconstructable logical accounting contract where feasible;
- allow controlled periodic reconciliation/sampling/measurement;
- forbid billing directly from an unvalidated expensive approximation.

## CH-02 — Physical Headroom Is Not a Single Inequality

Attack: `Commercial Limit < Technical Hard Limit` can be misread as one GB comparison. A Cell can be unsafe due to WAL, temporary space, recovery workspace or maintenance even when primary data bytes are below disk capacity.

Required correction:
- define headroom as a vector of material physical dimensions;
- commercial quota must remain inside the admissible safe region, not merely below one disk number.

## CH-03 — Critical Operating Reserve Abuse

Attack: If critical writes are always allowed after commercial quota is exceeded, a Tenant can grow indefinitely by labeling workloads critical or by normal ERP activity while never upgrading.

Required correction:
- platform owns criticality classification;
- reserve is finite, separately protected and emergency-oriented;
- continued over-entitlement enters explicit remediation state;
- physical safety can still veto new writes if reserve/safety boundary is endangered.

## CH-04 — Attachment Commit Split-Brain

Attack: Binary upload can succeed while DB metadata commit fails, or metadata can commit while object persistence fails. This creates orphan objects or broken business references and inaccurate usage.

Required correction:
- define two-phase/compensating state machine conceptually: pending object, integrity verify, canonical metadata commit, active object, orphan/recovery queue;
- charge/logical usage becomes effective only at canonical committed retained state;
- orphan cleanup remains platform overhead unless customer evidence proves retained value.

## CH-05 — Archive Double-Counting During Transition

Attack: Active copy and archive copy may coexist during migration. Counting both to customer usage would penalize platform implementation; counting neither could hide retained content.

Required correction:
- one logical retained object identity has one customer storage attribution at Time T;
- temporary duplicate copies during lifecycle transition are platform physical overhead;
- effective state changes only after verified archive commit/cutover.

## CH-06 — Delete / Reclaim Timing Dispute

Attack: Customer requests deletion but object remains physically for asynchronous cleanup, backup retention or legal reasons. Billing could continue unpredictably.

Required correction:
- distinguish logical-retention entitlement from physical protection copies;
- define customer usage effective-time by canonical logical release policy, subject to retention/legal-hold constraints;
- backups/platform copies after logical release remain platform overhead unless contract explicitly defines retained archive service.

## CH-07 — Cross-Tenant Deduplication Leakage

Attack: Shared deduplication can reveal that another Tenant possesses identical content through timing, hash acceptance or storage-credit effects.

Required correction:
- no cross-Tenant deduplication may affect customer-visible quota/price or observable behavior by default;
- any future shared physical dedup requires separate security proof and must remain below the Tenant logical meter boundary.

## CH-08 — Transient Generated Output Double Charge

Attack: A heavy export may consume processing, temporary storage, network and later retained file storage. Without state boundaries the same operation can be charged multiple times accidentally.

Required correction:
- transient staging is not retained storage;
- retained File usage begins only on explicit retention/commit;
- processing/API/third-party charges require separate disclosed commercial unit mapping under G2 anti-double-charge rules.

## CH-09 — Restore / Migration Workspace Risk

Attack: Restoring 100 logical units may require materially more than 100 physical units during staging, validation, indexes, WAL or dual-copy transition. Tenant quota alone cannot authorize restore.

Required correction:
- restore/migration admission checks Tenant entitlement AND platform/Cell temporary headroom;
- heavy restore can require reservation even if final logical footprint fits entitlement;
- temporary physical amplification is measured for G7/G8, not billed blindly.

## CH-10 — Logical Quota Can Hide Negative Margin

Attack: A customer may remain inside a logical DB/file quota yet generate unusually expensive physical amplification, retention, API, restore or processing costs.

Required correction:
- G3 must not claim logical quota proves economic suitability;
- physical amplification and Cost-to-Serve feed G8 and Package/Enterprise recommendation;
- customer charges cannot be invented retroactively because internal costs are high.

## CH-11 — Retention / Legal Hold vs Capacity Enforcement

Attack: A customer can be over quota because legally required records cannot be deleted. Blocking all business work may create compliance or accounting harm.

Required correction:
- retention-locked content remains immutable/retained according to policy;
- over-entitlement state separates existing retained truth from additional optional growth;
- remediation may require Add-on/Package/Enterprise review, not destructive cleanup.

## CH-12 — Hash / Size Evidence Trust Boundary

Attack: Client-provided content length/hash cannot alone be trusted for billing, integrity or dedup decisions.

Required correction:
- canonical accepted size/hash must be server/platform-verified from received object evidence;
- customer meter uses verified canonical values, not untrusted client assertion.

## Round-1 Disposition

12 material findings identified.

`G3 = REWORK REQUIRED BEFORE RE-CHALLENGE`.

No numerical quota, price, topology, storage provider or physical threshold may freeze during correction.
