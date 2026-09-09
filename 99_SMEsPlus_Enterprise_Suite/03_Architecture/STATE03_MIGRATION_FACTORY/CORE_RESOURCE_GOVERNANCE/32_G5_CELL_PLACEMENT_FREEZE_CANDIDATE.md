# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G5 — Cell / Placement Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE
Gate: G5 — Cell / Placement
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Freeze scope

G5 freezes only conceptual Cell / Placement governance. It does NOT freeze physical topology, tenant count, CPU/RAM/DB/storage size, placement score weights, region layout, database tenancy mechanism, container/VM mechanism, movement technology or numerical thresholds.

## 2. Recommended Standard reference direction

`Bounded multi-tenant Cells + evidence-based placement + targeted stronger isolation for selected heavy workloads + dedicated full-tenant environment reserved for ENTERPRISE`.

Commercial package remains independent from physical placement.

## 3. Minimum Cell-boundary proof contract

A resource group may be called a `Cell` only when the architecture can prove:
- authoritative Tenant membership / placement mapping;
- measurable Cell-level capacity/headroom;
- Cell health/state and admission control;
- controlled routing to that Cell;
- explicit failure/recovery semantics;
- explicit movement/source-release semantics;
- inventory of platform-global dependencies that can exceed the Cell blast radius.

G5 does not claim that every dependency is Cell-local. Blast-radius statements must be limited to the boundary actually proven.

## 4. Capacity / placement eligibility

Placement uses mandatory hard-veto eligibility before any ranking.

Hard-veto examples:
- stale/unknown critical telemetry;
- insufficient hard safety headroom in any material dimension;
- Cell in STOP_PLACEMENT/DEGRADED/RECOVERY state;
- incompatible version/schema/extension/data-plane contract;
- unresolved Tenant-isolation/security proof;
- region/residency violation;
- insufficient temporary movement/recovery workspace where movement is involved.

No weighted score can override a hard veto.

## 5. Multidimensional ranking / fragmentation

Eligible Cells may be ranked using multidimensional evidence.

Ranking must account for dominant-resource scarcity and stranded headroom. A Cell with abundant CPU but exhausted DB connections, storage growth margin, worker capacity or recovery headroom is not treated as broadly spare.

Weights/algorithm remain HOLD until G8 testing.

## 6. New-Tenant cold-start rule

A new Tenant without historical telemetry is placed using:
- declared/known business profile;
- Package Entitlement as a commercial boundary only;
- expected workload dimensions where available;
- conservative uncertainty reserve;
- confidence label;
- early observation/reassessment window.

Package or organization size alone is never considered proof of workload suitability.

## 7. Correlated-burst rule

Cell capacity must reserve for aggregate/correlated legitimate bursts, not only independent Tenant averages.

G8 must test scenarios including accounting close, payroll/tax deadlines, batch windows, API bursts and simultaneous report workload.

Exact safety margin remains HOLD.

## 8. Cell state / growth after admission

Conceptual states:

`HEALTHY -> CAUTION -> STOP_PLACEMENT -> REBALANCE_CANDIDATE/DRAIN -> DEGRADED -> RECOVERY -> HEALTHY`

Controls:
- anti-flap / hysteresis / cooldown mandatory;
- stop-placement does not automatically stop existing critical ERP activity;
- already-hot Cells can create prioritized rebalance candidates;
- movement has a concurrency budget and cannot trigger herd relocation;
- targeted isolation/defer is preferred before unnecessary full-Tenant movement where safe.

## 9. Platform/system reserve

Admission and Cell headroom must separately account for platform/system work such as:
- backup/recovery;
- maintenance/index/schema operations;
- observability;
- control-plane operations;
- platform jobs;
- emergency/recovery reserve.

Platform reserve is Cost-to-Serve and not silently charged as Tenant usage.

## 10. Global dependency classification

Every critical dependency must be classified later as one of:
- CELL-LOCAL;
- CELL-SCOPED SHARED;
- PLATFORM-GLOBAL.

Platform-global dependencies such as identity, placement authority, routing, telemetry or shared infrastructure require separate HA/security/blast-radius proof. A Cell cannot claim containment for failure modes that originate in an unbounded global dependency.

## 11. Movement authority / split-brain prevention

Canonical placement uses a monotonic `Placement Epoch` (or technically equivalent fencing/authority construct).

Required semantics:
- exactly one authoritative placement epoch for write-capable execution;
- routers/sessions/workers must validate current placement authority before write execution;
- stale source epoch is rejected/redirected safely after cutover;
- cache invalidation alone is not considered sufficient correctness proof;
- movement authority handoff is auditable and reconstructable.

The exact implementation of epoch/fencing remains open.

## 12. Standard Cell-to-Cell movement sequence

`Evidence -> Destination Hard Eligibility -> Temporary Capacity Reserve -> Preflight -> Data/File/Config Synchronization -> Job/Integration Coordination -> Drain/Quiesce/Fence Boundary -> Final Delta -> Placement Epoch Switch -> Route Switch -> Reconciliation -> Observation -> Source Release`

Mandatory proof before source release:
- canonical Tenant ID unchanged;
- business/accounting/inventory truth reconciled;
- no unresolved transaction outcome;
- no duplicate/stranded queued jobs;
- attachments/document references intact;
- usage/wallet/billing history continuous;
- destination is authoritative;
- rollback/recovery decision is explicit.

## 13. Long-running transaction / job control

Before placement epoch switch:
- long-running write transactions must finish, be safely cancelled before side effects, or be reconciled through explicit outcome semantics;
- queued work re-resolves authoritative placement at dequeue;
- jobs carry Tenant identity and lineage sufficient to detect stale placement;
- idempotency/replay control is mandatory;
- stale sessions/API requests must not continue writing to released source placement.

## 14. Data-gravity eligibility

Destination eligibility includes more than App headroom.

It must account for:
- DB/data compatibility and movement path;
- object/file synchronization;
- queue/job coordination;
- integration endpoint continuity;
- backup/recovery compatibility;
- temporary dual-capacity/workspace;
- sync throughput and rollback reserve.

A destination with free compute but insufficient data-plane/movement capacity is not eligible.

## 15. Control-plane failure semantics

Existing service uses `last-authoritative known placement` only where integrity/security remain provable.

If placement authority is unavailable:
- do not guess or round-robin a Tenant to another Cell;
- prohibit new movement and unsafe new admission;
- existing write traffic may continue only against provably current/acceptable authority semantics defined by implementation evidence;
- control-plane and data-plane availability objectives are separated.

## 16. Administrative override control

Privileged placement override:
- cannot bypass Tenant isolation or correctness hard vetoes;
- cannot convert stale/unknown telemetry into evidence;
- requires explicit authorization, reason code, before/after evidence and immutable audit trail;
- emergency override must define expiry/review and recovery path.

## 17. Package-class Cells

Package-class Cells are NOT prohibited.

Disposition:
`EMPIRICAL OPTIMIZATION CANDIDATE`.

G8 must compare them against mixed-package Cells using:
- utilization/stranded headroom;
- noisy-neighbor variance;
- movement caused by package changes;
- operations burden;
- Cost-to-Serve;
- customer experience.

No default selection is frozen from package name alone.

## 18. Enterprise candidacy

Enterprise recommendation requires sustained evidence after excluding platform-caused inefficiency.

Possible evidence:
- sustained legitimate workload beyond safe/economic Standard envelope;
- isolation/SLA/compliance need;
- customer-requested dedicated environment;
- economic crossover demonstrated by Cost-to-Serve.

Temporary burst, bad SQL, missing indexes, platform retry amplification, memory leak or platform defect cannot independently justify Enterprise migration.

## 19. Targeted isolated workload lanes

Targeted isolation changes resource execution boundary only.

Mandatory:
- same Core business semantics/version contract;
- Tenant context revalidated;
- reservation lineage preserved;
- one canonical usage evidence chain;
- unused reserve released;
- platform-failed/retried work not automatically customer-chargeable;
- no hidden second product fork.

## 20. Scale-out economics

G5 approves horizontal Cell scale-out as a capability, not as an always-preferred immediate action.

G8 must compare:
- scale-up vs scale-out cost;
- stranded headroom;
- fixed per-Cell operating overhead;
- recovery/blast-radius improvement;
- deployment/observability complexity.

No scale trigger is numerically frozen.

## 21. Residual evidence obligations

Carry to G7/G8:
- Cell recovery / DR proof;
- global control-plane HA proof;
- mixed-package and correlated-burst load tests;
- stale telemetry admission tests;
- placement algorithm replay;
- movement split-brain / stale-session / stale-job tests;
- Cell-to-Cell movement duration and rollback tests;
- package-class vs mixed-Cell economics;
- targeted isolation performance/cost;
- dominant-resource fragmentation measurement;
- blast-radius vs Cell-size trade-off.

## 22. G5 freeze candidate disposition

No physical mechanism or numerical sizing is frozen.

Conceptually frozen candidate:
- Cell = bounded measurable placement/scale/fault unit, not a server label;
- Standard uses multiple multi-tenant Cells;
- package does not dictate Cell;
- placement is hard-veto + evidence-ranked;
- Cell capacity is multidimensional;
- movement preserves Tenant identity/business truth and requires single placement authority;
- targeted isolation may protect heavy workload without converting Standard to dedicated-per-Tenant;
- dedicated full-Tenant resource boundary remains Enterprise.
