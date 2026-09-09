# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G5 — Standard Cell Capacity and Placement Draft

Status: EXECUTION DRAFT
Gate: G5 — Cell / Placement
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. Cell definition

A `Cell` is a bounded Standard deployment / scale / fault-containment unit that serves a subset of Tenants under one Core product and common governance.

A Cell is NOT automatically:
- one physical server;
- one database host;
- one container;
- one package class;
- one tenant;
- one region.

Its exact physical composition remains a mechanism decision for later evidence.

## 2. Placement identity model

Canonical identity chain:

`Tenant ID -> Placement Record -> Cell ID -> Resource/Service Endpoints`

Rules:
- Tenant ID remains stable across Cell movement.
- Cell ID is operational placement identity, not business identity.
- Package changes do not automatically mutate Cell placement.
- Placement history is time-effective and auditable.
- Routing must resolve the current authoritative placement record.

## 3. Cell capacity envelope

Cell capacity is a multidimensional vector, not one scalar tenant count.

Minimum dimensions:
- application CPU / event-loop pressure;
- memory pressure;
- interactive request concurrency;
- DB connection acquisition pressure;
- query/transaction/lock pressure;
- business DB physical headroom;
- object/file growth and throughput;
- queue depth / age;
- worker saturation;
- network / I/O where material;
- backup / recovery / restore headroom;
- system/platform workload;
- observability signal freshness/confidence.

Rule: a healthy score in one dimension cannot compensate for an unsafe hard-veto dimension.

## 4. Placement control model

Placement is two-stage:

### Stage A — Hard eligibility / veto
A candidate Cell is ineligible if any required condition fails, including:
- tenant residency/region constraint;
- incompatible Core/schema/extension contract;
- insufficient hard safety headroom in a material resource;
- degraded/unknown critical telemetry;
- unresolved isolation/security boundary;
- active stop-placement/degraded state;
- recovery/maintenance state that forbids new admission.

### Stage B — Preference ranking
Eligible Cells may be ranked by evidence such as:
- remaining multidimensional headroom;
- predicted workload fit;
- balance / fragmentation;
- growth trend;
- operational risk;
- data gravity / movement cost;
- Cost-to-Serve signals;
- version/update ring compatibility if used.

No ranking algorithm or weights are frozen in G5.

## 5. Cell state machine

Conceptual states:

`HEALTHY -> CAUTION -> STOP_PLACEMENT -> REBALANCE/DRAIN -> DEGRADED -> RECOVERY -> HEALTHY`

Controls:
- state is driven by fresh multi-signal evidence;
- anti-flap/hysteresis is mandatory;
- `STOP_PLACEMENT` does not automatically stop existing Tenant business work;
- emergency controls preserve business truth and transaction correctness;
- state transitions are auditable with reason codes and evidence pointers.

Exact thresholds remain HOLD.

## 6. Tenant workload classification for placement

Placement may use observed workload profile, but profile is not Tenant identity or package identity.

Candidate dimensions:
- interactive transaction intensity;
- DB/query intensity;
- file/attachment intensity;
- API/integration intensity;
- background/batch intensity;
- reporting intensity;
- growth rate;
- burstiness;
- recovery/backup footprint.

Controls:
- temporary burst does not permanently label a Tenant heavy;
- platform defects are excluded before tenant workload attribution;
- classification requires confidence and recency;
- new Tenants without history use conservative declared/profile assumptions plus observation, not fabricated certainty.

## 7. Mixed-package placement rule

Default G5 direction:
- different commercial packages MAY share one Standard Cell;
- package is not an automatic placement partition;
- a package-class Cell may be introduced later only if telemetry/load economics prove a material benefit.

This prevents commercial packaging from silently becoming infrastructure topology.

## 8. Noisy-neighbor prevention chain

`Tenant Runtime Governor (G4) -> Cell Headroom Monitor -> Admission Control -> Targeted Isolation/Deferral -> Stop Placement -> Movement/Scale-out`

Required behavior:
- protect before physical exhaustion;
- identify Tenant-local vs Cell-global pressure;
- do not move/upgrade a Tenant until SMEsPlus-caused inefficiency is excluded;
- sustained attributable pressure can trigger package/capacity review or Enterprise candidacy;
- temporary legitimate bursts use reservations/fairness/protection before forced mobility.

## 9. Horizontal scale-out logic

When a Cell cannot safely accept new placement:

`STOP NEW PLACEMENT -> USE/CREATE ANOTHER ELIGIBLE CELL -> CONTINUE STANDARD SERVICE`

The control plane must never depend on a fixed `N tenants = full Cell` rule.

## 10. Standard Cell-to-Cell movement contract

Conceptual movement stages:

`Candidate Evidence -> Destination Eligibility -> Capacity Reservation -> Preflight -> Data/File Sync or Transfer -> Job/Integration Coordination -> Final Delta/Quiesce Boundary -> Authoritative Route Switch -> Reconciliation -> Observation -> Source Release`

Mandatory integrity:
- one canonical Tenant identity;
- no duplicate business truth;
- transaction/posting state remains consistent;
- usage/wallet/billing lineage is continuous;
- attachments/document links remain provable;
- queue jobs do not execute twice or against stale placement;
- routing caches cannot override authoritative placement after cutover;
- rollback/recovery state is explicit.

Exact movement mechanism/downtime target remains HOLD.

## 11. Placement control-plane failure requirements

The placement/routing control plane is a critical dependency.

Requirements:
- authoritative placement record must be durable/auditable;
- cached routing must have bounded staleness and invalidation/recovery semantics;
- control-plane outage must not silently route a Tenant to the wrong Cell;
- fail-safe behavior prefers known last-authoritative placement over guessing;
- movement requires atomic/equivalent authority handoff semantics at the routing boundary.

## 12. Cell blast-radius rule

A Cell is intentionally a bounded blast-radius unit.

Therefore:
- failure of one Cell should not require failure of all Standard Cells;
- shared global services must be reviewed separately because they can recreate platform-wide blast radius;
- shared identity/control/telemetry components require resilient design and must not weaken Tenant isolation.

G5 does not freeze which services are global vs Cell-local; it records this as a downstream architecture proof obligation.

## 13. Package / Enterprise relationship

Package upgrade != Cell movement.
Cell movement != Enterprise migration.
Enterprise recommendation != punishment for temporary burst.

Enterprise candidacy requires sustained evidence such as:
- isolation/SLA requirement;
- sustained legitimate workload beyond safe/economic Standard envelope;
- data/processing profile that makes dedicated capacity materially preferable;
- customer request for dedicated resource boundary.

## 14. G5 non-decisions

NOT frozen:
- Cell physical size;
- tenant count per Cell;
- placement weights/thresholds;
- package-class Cell policy;
- database topology;
- object-storage topology;
- cache/queue topology;
- container/VM/Kubernetes mechanism;
- live vs cold movement mechanism;
- regional layout;
- exact failure-domain composition.

## 15. Evidence obligations carried to G8

- mixed-package Cell load test;
- correlated burst/noisy-neighbor test;
- stale telemetry/admission test;
- placement replay/forecast accuracy;
- stop-placement safety margin test;
- Cell failure blast-radius test;
- routing/control-plane failure test;
- Cell-to-Cell movement rehearsal;
- package-class vs mixed-Cell cost/performance comparison;
- targeted isolated-lane benchmark;
- capacity fragmentation and stranded-headroom measurement.
