# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E1 — Run Ledger & Telemetry Evidence Contract

Status: E1 DRAFT FOR REVIEW
Jira: ERPPLUS-156
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Purpose

Define the minimum immutable evidence required for every architecture-lab experiment so that results are reproducible, challengeable, comparable and invalidatable.

## 2. Canonical Run Identity

Every experiment has a unique immutable `run_id` and belongs to one declared `campaign_id`.

Required identity fields:
- `session_id`;
- `gate_id`;
- `campaign_id`;
- `run_id`;
- `hypothesis_id` / proof-obligation IDs;
- benchmark class;
- workload family IDs;
- owner;
- reviewer/verifier;
- start/end timestamp with timezone.

## 3. Benchmark Class

Mandatory enum:
- COMPONENT_BENCHMARK;
- PRODUCTION_INTENT_SYSTEM_BENCHMARK;
- FAILURE_RECOVERY_EXPERIMENT;
- MOBILITY_PLACEMENT_EXPERIMENT;
- ECONOMIC_CTS_EXPERIMENT.

One run may carry multiple labels only when its evidence clearly satisfies each class. Do not upgrade a component test to system proof by description alone.

## 4. Version / Environment Binding

Every run records:
- application repository + commit SHA;
- build artifact identity/checksum where applicable;
- Node.js/runtime/framework version;
- schema/migration version;
- DB engine/version/topology;
- cache/queue versions;
- worker/runtime configuration;
- host/VM/container manifest;
- CPU/RAM limits visible to the workload;
- storage class/capacity/IOPS/throughput characteristics where known;
- network path/bandwidth/latency constraints;
- object-storage configuration where relevant;
- security/auth/tenant-isolation controls enabled;
- placement/governor version/configuration;
- backup/recovery configuration where relevant.

Any unknown material field is explicitly `UNKNOWN`; it is never silently assumed.

## 5. Workload Binding

Record:
- workload script/tool/version/checksum;
- dataset/fixture version/checksum;
- Tenant count only as an experiment input, never as capacity conclusion;
- Tenant profile mix;
- company/branch mix where relevant;
- data-size/distribution profile;
- read/write/process mix;
- request/concurrency/arrival model;
- heavy/background job mix;
- load shape;
- duration;
- cache/maintenance state;
- failure/degradation injection configuration;
- external dependency stubs/real endpoints classification.

## 6. Generator / Instrumentation Binding

Generator evidence:
- generator host(s);
- generator CPU/RAM/network utilization;
- distributed-generator topology when used;
- clock/time-sync condition;
- tool version/configuration;
- client-side timeout/retry behavior.

Telemetry evidence:
- metrics/log/traces sources;
- sampling/scrape interval;
- dropped data/collection errors;
- clock skew concerns;
- monitoring overhead characterization;
- dashboard/query version used for derived results.

A run is invalid for platform-capacity claims if the generator or telemetry pipeline is the hidden bottleneck and the impact cannot be bounded.

## 7. Result Evidence

Preserve raw and derived layers separately.

### Raw artifacts
- load generator output;
- application metrics;
- DB metrics;
- host/container metrics;
- queue/worker metrics;
- storage/network metrics;
- logs/traces where applicable;
- failure/recovery logs;
- cost-source snapshot/reference where economic.

Raw artifacts require location and checksum when feasible.

### Derived result record
- throughput/rate;
- latency percentiles/distribution;
- error/retry/failure rates;
- resource saturation indicators;
- Tenant fairness delta;
- backlog/drain time;
- achieved recovery metrics;
- physical/logical amplification;
- CTS inputs/derived outputs;
- confidence/variance;
- anomalies/unknowns.

Derived results must be reproducible from raw evidence and declared transformations.

## 8. Run Outcome State

Mandatory state:
- PLANNED;
- EXECUTED_VALID;
- EXECUTED_INVALID;
- ABORTED;
- HELD_FOR_REVIEW;
- VERIFIED;
- SUPERSEDED;
- INVALIDATED_BY_CHANGE.

Failed/invalid/aborted runs remain in lineage and are not deleted merely because they do not support the preferred architecture.

## 9. Evidence Quality / Gate Impact

Every reviewed run records:
- reviewer/verifier;
- review timestamp;
- verification status;
- defects/anomalies;
- claim scope supported;
- claim scope NOT supported;
- gate impact;
- retest requirement;
- invalidation triggers.

## 10. Tenant Isolation & Privacy Evidence

For multi-Tenant runs, retain explicit evidence for:
- canonical Tenant IDs used in synthetic fixtures;
- expected-deny cross-Tenant cases;
- leakage/error observations;
- per-Tenant metric attribution;
- test-data classification.

Raw telemetry made customer-facing later must never expose another Tenant's data or secrets.

## 11. Cost Evidence Contract

Economic runs record:
- cost-source type: supplier quote/invoice/public tariff/owned-infra accounting estimate;
- source date/effective period;
- currency;
- commitment/discount regime;
- fixed/shared/variable components;
- allocation method;
- PlatformDefect/Waste bucket;
- UnallocatedPlatform bucket;
- sensitivity assumptions;
- whether output is relative Cost Unit or actual currency.

Relative Cost Unit cannot be represented as actual THB/USD without source recalibration.

## 12. Minimum Run Ledger Row

`run_id | campaign_id | hypothesis | benchmark_class | app_commit | env_manifest | workload_version | fixture_version | tenant_mix | load_shape | start/end | raw_artifacts | checksum | derived_result | owner | reviewer | verification_status | anomalies | gate_impact | invalidation_trigger`

## 13. E1 Draft Disposition

`RUN LEDGER / TELEMETRY CONTRACT = DRAFTED FOR SPECIALIST REVIEW / INDEPENDENT CHALLENGE`.