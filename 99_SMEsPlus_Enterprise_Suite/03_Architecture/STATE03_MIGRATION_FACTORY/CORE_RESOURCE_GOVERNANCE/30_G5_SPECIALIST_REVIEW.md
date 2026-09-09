# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G5 — Specialist Review

Status: SPECIALIST REVIEW COMPLETE
Artifact reviewed: `28_G5_CELL_PLACEMENT_ARCHITECTURE_OPTIONS_AND_EVIDENCE.md`, `29_G5_STANDARD_CELL_CAPACITY_AND_PLACEMENT_DRAFT.md`
Gate: G5 — Cell / Placement
Final Approver: Boss only

## 1. Review lenses

1. Platform / Infrastructure Architecture
2. Database Engineering & Performance
3. SRE / Performance & Load Testing
4. Security / Tenant Isolation
5. FinOps / SaaS Cost Economics
6. Billing / Wallet / Metering Architecture
7. Product Package / Commercial Governance
8. Independent Operations / Mobility Readiness

## 2. Specialist findings

### SR-01 — Cell must be a bounded operational unit, not merely a naming label
Result: ACCEPT WITH CONTROL.
The draft must ensure that a Cell has explicit membership/placement authority, measurable headroom, state, and failure/movement semantics. Otherwise `Cell` becomes architectural vocabulary with no enforceable boundary.

### SR-02 — Placement must use hard veto dimensions before any weighted score
Result: ACCEPT.
A weighted score must never allow abundant CPU to offset exhausted DB connections, storage headroom, or an isolation defect.

### SR-03 — New-Tenant cold-start placement has insufficient evidence
Result: MATERIAL OPEN FINDING.
A new Tenant has no historical workload. Placement must use declared/customer-profile assumptions, package entitlement, industry/workload profile, conservative reserve, and a defined early-observation/rebalancing period. Package alone is insufficient.

### SR-04 — Correlated burst risk is not covered by per-Tenant prediction
Result: MATERIAL OPEN FINDING.
Month-end/accounting close, payroll, tax deadlines, campaigns or batch schedules can create simultaneous legitimate bursts across many Tenants. Cell admission needs aggregate/correlated-burst safety margin, not only independent Tenant averages.

### SR-05 — Shared global services can defeat Cell blast-radius containment
Result: MATERIAL OPEN FINDING.
If routing, identity, queue, database control, storage metadata or observability are globally singular dependencies, a Cell model can still have national blast radius. G5 must classify `Cell-local`, `Cell-scoped shared`, and `platform-global` dependency proof obligations.

### SR-06 — Database/data gravity may make placement asymmetric
Result: MATERIAL OPEN FINDING.
A Tenant cannot be considered movable merely because App capacity exists elsewhere. Database, object data, queue/jobs, integrations and backup topology can dominate move cost/time. Destination eligibility must include data-plane compatibility and temporary dual-capacity headroom.

### SR-07 — Stop-placement is not enough for an already-hot Cell
Result: MATERIAL OPEN FINDING.
Existing load can grow after placement. The model needs `rebalance candidate`, targeted workload isolation, package/capacity review, and controlled movement logic without implying automatic migration.

### SR-08 — Placement history is security-sensitive configuration
Result: ACCEPT WITH CONTROL.
Administrative placement override must be authorization-controlled, reason-coded, immutable/auditable, and unable to bypass Tenant isolation/capacity hard vetoes.

### SR-09 — Routing cache split-brain can create duplicate execution
Result: MATERIAL OPEN FINDING.
After a move, stale routers/workers might send writes/jobs to both source and destination. The model requires a placement epoch/fencing concept or equivalent authority mechanism; cache invalidation alone is insufficient proof.

### SR-10 — Movement must protect long-running transactions and queued jobs
Result: MATERIAL OPEN FINDING.
The pre-cutover process needs a defined transaction/job drain or fencing boundary, idempotent replay rules, and explicit status for jobs started before the movement epoch.

### SR-11 — Mixed-package Cells need anti-fragmentation evidence
Result: MATERIAL OPEN FINDING.
Multi-dimensional capacity can strand unusable headroom (e.g., CPU free but DB connections exhausted). Placement ranking must consider dominant-resource fragmentation and not only percentage utilization.

### SR-12 — Package-class Cells remain an empirical optimization, not a prohibited design
Result: ACCEPT.
Keep as a candidate for G8 A/B simulation. Do not hard-code rejection based only on conceptual purity.

### SR-13 — Enterprise candidacy must not become an automated eviction mechanism
Result: MATERIAL OPEN FINDING.
Recommendation may be system-generated, but final commercial migration must use evidence, customer/commercial controls and later mobility gates. Temporary pressure or platform defect must not force Enterprise.

### SR-14 — Cell capacity must reserve platform/system workload
Result: MATERIAL OPEN FINDING.
Maintenance, backup, schema/index operations, observability, recovery and platform jobs can consume material capacity. Admission must account for platform reserve separately from Tenant entitlement.

### SR-15 — Failure-domain size requires empirical upper-bound discovery
Result: ACCEPT / CARRY TO G8.
No tenant-count constant should be invented now. G8 must test operational blast radius, recovery duration and cost as Cell size increases.

### SR-16 — Control plane and data plane availability must be separated
Result: MATERIAL OPEN FINDING.
Existing tenants should not necessarily fail merely because new-placement control is unavailable. The model needs fail-static/last-authoritative placement semantics while prohibiting unsafe new movement/admission.

## 3. Specialist recommendation

Proceed to Independent Challenge only after correction explicitly covers SR-03 through SR-16 material findings. Current Option C + E direction remains plausible, but G5 is not yet ready for Gate disposition.

Build / Merge / Production remain HOLD.
