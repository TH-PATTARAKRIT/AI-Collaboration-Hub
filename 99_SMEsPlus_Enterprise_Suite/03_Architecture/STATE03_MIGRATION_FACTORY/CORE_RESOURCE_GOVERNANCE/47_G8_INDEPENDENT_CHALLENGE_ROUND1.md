# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G8 — Independent Adversarial Challenge Round 1

Status: CHALLENGE COMPLETE — CORRECTION REQUIRED
Gate: G8 — Cost / Load-Test Readiness
Inputs:
- `45_G8_COST_TO_SERVE_AND_LOAD_TEST_READINESS_DRAFT.md`
- `46_G8_SPECIALIST_REVIEW.md`
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Challenge Objective

Attempt to falsify the G8 model before it is used to justify Package limits, Cell capacity, pricing, or Standard-to-Enterprise recommendations.

## 2. Adversarial Failure Modes

### CH-01 — Benchmark-to-production fallacy
A lab result may be repeatable yet non-representative. Require explicit representativeness evidence and prohibit automatic promotion.

### CH-02 — Single-dimensional success
CPU headroom can look healthy while lock waits, queue backlog or recovery reserve is failing. Acceptance must be vector-based.

### CH-03 — Simpson's paradox across Tenants
Aggregate latency/cost can improve while one Tenant class degrades. Require Tenant/class stratification.

### CH-04 — Mean-cost pricing trap
Mean CTS can make light Tenants subsidize heavy-tail Tenants unintentionally. Report distribution and concentration.

### CH-05 — Peak coincidence hidden by monthly totals
Tenants with equal monthly work can have radically different reserve costs. Track coincident peak contribution.

### CH-06 — Stranded headroom omitted
Package-class Cells may appear cheap if unused reserved resources are ignored. Attribute stranded capacity explicitly.

### CH-07 — Cell fixed-cost dilution fantasy
Do not divide fixed cost by design maximum Tenant count; use observed/forecast occupancy bands.

### CH-08 — CU weight manipulation
Normalized Cost Units can be tuned to predetermine winner. Require sensitivity ranges and rank stability.

### CH-09 — On-demand cloud list-price bias
Architecture can be mis-ranked if long-term discounts/private infrastructure economics are ignored. Compare procurement regimes separately.

### CH-10 — Free labor assumption
More Cells/topologies may be technically efficient but operationally expensive. Include SRE toil, patching, observability and incident overhead.

### CH-11 — Free observability assumption
Per-Tenant telemetry and immutable usage evidence have real storage/compute cost. Measure them.

### CH-12 — Instrumentation changes workload
Deep tracing can alter latency/CPU. Require monitoring-overhead characterization.

### CH-13 — Load generator is bottleneck
Prove generator capacity/network headroom and clock consistency.

### CH-14 — Unrealistic request distribution
Uniform random traffic misses real skew and hot keys. Require empirical/skewed distributions.

### CH-15 — Unrealistic Tenant homogeneity
Identical synthetic Tenants hide noisy-neighbor behavior. Require heterogeneous mix.

### CH-16 — Cache bias
Warm cache can overstate sustainable capacity; cold cache can understate normal operation. Measure phases separately.

### CH-17 — Autovacuum/checkpoint invisibility
Short runs miss maintenance interaction. Soak must cross relevant DB/backup/queue cycles.

### CH-18 — Failure-free benchmark
Healthy-path capacity is not deployable capacity. Inject slow/failing dependencies, replica lag, queue stalls and storage pressure.

### CH-19 — Retry storm double counting
Platform retries can look like customer demand and CTS. Preserve causal exclusion and idempotent lineage.

### CH-20 — Security-disabled benchmark
A benchmark without Tenant authorization, encryption/audit and policy checks is not production-intent evidence.

### CH-21 — No paired fairness baseline
Noisy-neighbor claim needs before/with/after comparison for unaffected Tenants.

### CH-22 — Break point misnamed as capacity
The crash/saturation point is not admission capacity. Require sustainable envelope and recovery criteria.

### CH-23 — No hysteresis validation
A threshold may cause placement/throttling oscillation. Test state transitions under near-boundary noise.

### CH-24 — Unknown telemetry treated as zero load
Missing telemetry must fail conservative, consistent with G4/G5.

### CH-25 — Backup cost averaged away
Restore workspace and disaster concurrency are spiky. Model reserved and event-driven recovery cost.

### CH-26 — Recovery test without normal traffic
DR may pass only because customer workload is stopped. Test recovery contention where service design permits.

### CH-27 — Single-Cell recovery only
Correlated incident can require multiple Cell recoveries. Include concurrency budget and prioritization.

### CH-28 — Data egress/transfer omitted
Cell movement/DR/object restore can materially change cost and duration. Record bytes and topology.

### CH-29 — Historical data growth omitted
A one-month snapshot misses retention compounding and archive economics. Model cohorts/horizons.

### CH-30 — Enterprise crossover false precision
One fixed crossover threshold cannot represent workload, SLA, region and compliance variation. Use ranges and reason codes.

### CH-31 — Enterprise upsell caused by platform defect
Bad query/index/retry/memory behavior must be corrected before classifying Tenant as Enterprise candidate.

### CH-32 — Package change feedback loop
Moving a Tenant because Package changes can create movement cost that makes package-class Cells seem worse or better depending on accounting. Keep movement cost explicit.

### CH-33 — Cost allocation forced to 100%
Uncertain overhead should remain Platform/Unallocated rather than fabricated Tenant causality.

### CH-34 — Third-party price volatility
AI/document/payment/API vendor costs can change abruptly. Sensitivity/scenario analysis required.

### CH-35 — FX and tax contamination
Infrastructure vendor FX/tax treatment can alter THB cost but is not the same as customer pricing/tax. Keep technical CTS and commercial pricing layers separate.

### CH-36 — Revenue used to justify architecture safety
High-revenue Tenant must not bypass capacity/security hard veto. Economics cannot override safety.

### CH-37 — Sampled telemetry misses expensive rare event
Large report/export/restore may be rare but material. Exact/reconstructable evidence required for high-cost events.

### CH-38 — Measurement window gaming
A Tenant can look efficient if expensive jobs occur outside observation window. Define complete period and scheduled-work obligations.

### CH-39 — Queue backlog hidden after test stop
A test that ends before backlog drains understates total work and recovery time. Include post-load drain/recovery phase.

### CH-40 — Capacity without rollback proof
Load-triggered placement/movement changes may be irreversible or risky. Test rollback/source-release and reconciliation.

### CH-41 — Data generator ignores referential/business semantics
Random rows can produce unrealistic query plans and transaction contention. Representative fixtures must preserve domain relationships.

### CH-42 — Package economics ignore customer support burden
Some workload types create support/incident burden independent of compute. Track operational/support burden separately; do not silently assign without evidence.

### CH-43 — Margin target retrofits the data
A desired price/margin must not be used to reverse-engineer acceptable capacity. Capacity derives from safety/measurement; price derives from CTS + commercial policy.

### CH-44 — Test result cherry-picking
All declared runs, including failed/aborted runs, require lineage. Superseded runs remain audit-visible.

### CH-45 — Tool-specific benchmark becomes architecture dependency
No single tool's metric vocabulary may define canonical capacity semantics.

### CH-46 — Region/provider lock-in hidden inside benchmark
Reference environment must separate workload characteristics from provider-specific instance naming and mechanisms.

### CH-47 — No confidence decay
Old benchmark evidence becomes stale after code/schema/workload/provider change. Require evidence invalidation/retest triggers.

### CH-48 — No falsification threshold for mixed vs package-class Cells
Without predeclared decision metrics, team can rationalize either outcome afterward. Define comparison metrics before experiment.

## 3. Mandatory Corrections

Corrected candidate must add:
- raw vs policy-adjusted measurement separation;
- occupancy/stranded-headroom accounting;
- peak/coincident reserve contribution;
- Tenant-level cost/fairness distributions;
- unallocated Platform bucket;
- monitoring overhead measurement;
- generator validation;
- warm/cold/maintenance/recovery phases;
- predeclared A/B decision metrics;
- evidence confidence/invalidation policy;
- procurement-regime and cost-driver sensitivity;
- post-load drain/recovery accounting;
- explicit non-overridable safety gates;
- technical CTS vs commercial pricing separation.

## 4. Challenge Disposition

`REWORK — 48 ADVERSARIAL FAILURE MODES IDENTIFIED`.

No fatal contradiction with G0–G7 was found. G8 may continue only after all material findings are incorporated and independently re-challenged.
