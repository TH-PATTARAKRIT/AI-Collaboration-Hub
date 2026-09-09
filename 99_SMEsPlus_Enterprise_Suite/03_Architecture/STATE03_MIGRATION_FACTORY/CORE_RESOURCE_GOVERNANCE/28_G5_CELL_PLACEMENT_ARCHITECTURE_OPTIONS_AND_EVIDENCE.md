# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G5 — Cell / Placement Architecture Options and Evidence

Status: G5 EVIDENCE / OPTION COMPARISON
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Purpose

Challenge the Standard Cell / Placement hypothesis without treating Boss-proposed mechanisms as the answer. This record compares materially viable patterns against approved invariants and current G1-G4 evidence.

## 2. Binding invariants carried into G5

- STANDARD is shared-resource multi-tenant unless a material evidence delta triggers an explicit reopening.
- ENTERPRISE is the dedicated-resource / dedicated-tenant tier.
- Package != Tenant != Cell != Server != Database Host.
- Tenant Count != Capacity.
- Package is commercial entitlement, not physical placement identity.
- Cell admission must be based on measurable capacity/headroom.
- Shared infrastructure does not relax Tenant isolation.
- Platform defects/inefficiency cannot be reclassified as customer-caused heavy usage.
- Numerical thresholds and topology remain unfrozen.

Boss clarification preserved: Server Pool, DB Pool, Object Storage Pool, mixed-package Cells, package-class Cells, Docker-per-Tenant and similar mechanisms remain hypotheses unless evidence supports them.

## 3. External architecture evidence reviewed

### E-G5-EXT-01 — Deployment stamp / cell as horizontal scale unit
Microsoft Azure Architecture Center, `Deployment Stamps Pattern`:
https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp

Relevant evidence:
- an application can be deployed as multiple independent stamps/cells;
- each stamp can serve a subset of tenants;
- more stamps can be added for horizontal scale;
- independent stamps can contain failure blast radius;
- multitenant stamps still require multitenancy/noisy-neighbor controls.

### E-G5-EXT-02 — Multitenant stamp trade-off
Microsoft Azure Architecture Center, `Architectural Approaches for a Multitenant Solution`:
https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/overview

Relevant evidence:
- a stamp may serve multiple tenants or a single tenant;
- single-tenant stamps increase isolation but consume dedicated infrastructure;
- multitenant stamps retain noisy-neighbor and tenant-isolation obligations.

### E-G5-EXT-03 — Pool isolation risks
AWS Well-Architected SaaS Lens, `Pool isolation`:
https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html

Relevant evidence:
- shared compute/storage increases isolation complexity;
- pooled environments increase noisy-neighbor and blast-radius risk;
- per-tenant consumption attribution becomes more difficult and requires tenant-aware instrumentation.

### E-G5-EXT-04 — Tenant isolation is invariant, mechanism varies
AWS Well-Architected SaaS Lens, `Tenant Isolation`:
https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.html

Relevant evidence:
- shared infrastructure does not permit weakened Tenant isolation;
- isolation implementation varies by domain/deployment mechanism.

### E-G5-EXT-05 — Pool / silo / bridge are granular choices
AWS Well-Architected SaaS Lens, `Bridge model` and `Targeted isolation`:
https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/bridge-model.html
https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/targeted-isolation.html

Relevant evidence:
- isolation can differ by subsystem/resource;
- pooled and isolated resources can coexist where justified;
- a binary all-pooled vs all-silo choice is not required for every resource.

## 4. Architecture alternatives

### Option A — One very large shared national pool / monolithic placement domain

Concept:
- most/all Standard tenants share one large logical deployment domain;
- scaling primarily occurs inside that domain.

Strengths:
- maximum resource pooling;
- lowest apparent placement complexity;
- less cross-cell movement.

Material risks:
- larger failure blast radius;
- natural service/database limits can become platform-wide limits;
- harder controlled rollout/recovery;
- noisy-neighbor and operational incidents affect a larger tenant population;
- conflicts with parent requirement that Standard must not depend on one nationwide monolithic server/database installation.

G5 disposition: `REJECT AS STANDARD REFERENCE ARCHITECTURE`.
Reason: violates an approved scaling/failure-boundary direction and concentrates operational risk without compensating evidence.

### Option B — Package-class Cells (Small/Medium/Large package maps to separate Cell classes)

Concept:
- tenants of similar commercial package are grouped into corresponding Cells.

Strengths:
- workload expectations may become more homogeneous if package actually correlates with workload;
- operational tuning may be easier if package behavior is empirically distinct.

Material risks:
- risks coupling commercial package to physical placement;
- package upgrade/downgrade can create unnecessary relocation;
- organization/package size may correlate poorly with transaction/storage/API intensity;
- can create stranded capacity across package-class Cells;
- may create false certainty that package label is a capacity predictor.

G5 disposition: `HOLD AS OPTIONAL PLACEMENT OPTIMIZATION, NOT DEFAULT`.
Required evidence before adoption: telemetry proving materially lower variance / lower Cost-to-Serve / lower noisy-neighbor risk than mixed Cells.

### Option C — General-purpose multi-tenant Cells with evidence-based placement (mixed packages)

Concept:
- Standard uses multiple bounded multi-tenant Cells;
- package does not determine physical Cell;
- placement uses hard compatibility/safety constraints plus multidimensional headroom and workload evidence;
- multiple package classes may coexist when the resulting aggregate workload remains safe.

Strengths:
- preserves pooling/economies of scale;
- keeps commercial package independent from placement;
- supports horizontal scale by adding Cells;
- confines failure blast radius relative to a national monolith;
- allows package changes without mandatory movement;
- placement can learn from actual workload rather than organization-size proxy.

Material risks:
- requires strong tenant-aware runtime governance, isolation, metering and observability;
- heterogeneous workload creates noisy-neighbor risk;
- placement algorithm can be wrong if telemetry is stale/incomplete;
- Cell movement becomes a first-class operational capability.

G5 disposition: `RECOMMENDED REFERENCE DIRECTION`, subject to G5 controls and later load/economic evidence.

### Option D — Single-tenant dedicated Cell for every Standard tenant

Concept:
- each Standard tenant receives dedicated application/data runtime resources.

Strengths:
- strongest practical resource isolation and simplest noisy-neighbor boundary;
- easier per-tenant cost attribution.

Material risks:
- forfeits pooling economics;
- infrastructure/operations scale approximately with tenant count;
- risks silently turning Standard into Enterprise economics;
- requires idle/peak capacity per tenant;
- conflicts with current two-tier commercial boundary absent a material evidence delta.

G5 disposition: `REJECT AS STANDARD DEFAULT; PRESERVE AS ENTERPRISE / EXCEPTION CHALLENGER`.

### Option E — General-purpose Cells plus targeted isolated execution lanes

Concept:
- same Tenant remains in its Standard Cell for canonical business identity/data placement;
- selected heavy/optional workloads may execute through stronger isolation boundaries or dedicated worker lanes where G4 evidence requires it;
- this does not imply full Tenant dedicated infrastructure.

Strengths:
- retains Standard pooling for normal ERP workload;
- provides stronger containment for memory-heavy/batch/AI/import/export workloads;
- aligns with G4 rule that shared runtime must not claim hard isolation it cannot technically provide.

Material risks:
- increased orchestration/observability complexity;
- Tenant context must be re-established across async execution;
- capacity/metering must prevent double counting and reservation errors.

G5 disposition: `RECOMMEND AS COMPANION PATTERN TO OPTION C`, mechanism not frozen.

## 5. Comparative matrix

| Criterion | A National Pool | B Package-class Cells | C Evidence-based Mixed Cells | D Dedicated Standard | E Targeted isolation lanes |
|---|---|---|---|---|---|
| Scale-out | Weak/centralized | Good | Strong | Strong but expensive | Companion only |
| Blast-radius containment | Weak | Medium/Strong | Strong | Strongest | Improves heavy-workload containment |
| Pooling economics | Strong initially | Medium | Strong | Weak | Strong for base workload |
| Package/placement decoupling | Medium | Weak | Strong | Medium | Strong |
| Noisy-neighbor control burden | High | Medium | High but governable | Low | Reduces selected risks |
| Operational complexity | Medium | High | High | Very High at scale | High |
| Standard→Enterprise mobility | Harder from monolith | Medium | Natural conceptual path | Tier distinction blurred | Compatible |
| Evidence fit with G1-G4 | Weak | Partial | Strongest | Conflicts with current Standard invariant | Strong companion |

## 6. G5 recommendation

`Option C + Option E` is the current SaaS Team recommendation for the G5 reference model:

- bounded, horizontally scalable multi-tenant Cells;
- mixed commercial packages allowed by default;
- placement driven by safety/compatibility/headroom/workload evidence, not package label;
- targeted stronger isolation for selected workload classes when shared runtime cannot safely govern them;
- dedicated full-tenant environment remains ENTERPRISE, not Standard default.

This recommendation does NOT freeze:
- number of tenants per Cell;
- Cell CPU/RAM/DB/storage size;
- Cell topology;
- database tenancy mechanism;
- container/VM/Kubernetes mechanism;
- package-class optimization;
- live migration technology.

## 7. Confidence / evidence obligations

Confidence: `MEDIUM — ARCHITECTURE PATTERN SUPPORTED; SMEsPlus NUMERICAL PROOF PENDING`.

Must carry to G8:
- representative mixed-package noisy-neighbor load tests;
- Cell saturation tests;
- placement scoring replay against synthetic/representative tenants;
- operational cost of more Cells vs larger Cells;
- targeted isolation cost/latency;
- Cell failure and recovery tests;
- Cell movement throughput/downtime evidence;
- economic comparison versus package-class Cells.
