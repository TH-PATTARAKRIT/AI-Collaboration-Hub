# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E0 — Correction & Exit Contract

Status: CORRECTION EVIDENCE — READY FOR RE-CHALLENGE
Corrects: CH-01..CH-15
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Authority Precedence

For this empirical program:
1. Boss Final Approval / current September architecture evidence governs the conceptual/product baseline.
2. Current-session evidence governs empirical execution claims.
3. Older planning/technology documents remain reference unless explicitly reconciled.
4. A stale or conflicting technology document cannot redefine the current benchmark target by itself.

Therefore current SMEsPlus product identity for this program is clean-room Node.js SaaS ERP. The July FastAPI/Python entries are not valid current runtime truth for empirical capacity claims.

## 2. Evidence-State Taxonomy

The following states are mandatory:
- `PLANNING BASELINE`
- `CANDIDATE TOOL / CANDIDATE MECHANISM`
- `VERIFIED LAB ENVIRONMENT`
- `EXPERIMENT CONTRACT APPROVED`
- `RUN EXECUTED`
- `RESULT VERIFIED`
- `NUMERICAL CANDIDATE`
- `BOSS FROZEN`
- `INVALIDATED / SUPERSEDED`

No lower state may be presented as a higher state.

## 3. Benchmark-Class Metadata

Every Run Ledger entry must classify the run as at least one of:
- `COMPONENT BENCHMARK`
- `PRODUCTION-INTENT SYSTEM BENCHMARK`
- `RECOVERY / FAILURE EXPERIMENT`
- `ECONOMIC / CTS EXPERIMENT`
- `MOBILITY / PLACEMENT EXPERIMENT`

Component benchmark output can inform a subsystem model but cannot alone establish ERP end-to-end capacity.

## 4. Environment Execution Hold

Before any result may support numerical capacity:
- environment manifest must be verified;
- current application/runtime version must be bound;
- DB/network/storage/queue/worker configuration must be recorded;
- Tenant/security controls must be active for production-intent runs;
- observability configuration and overhead must be known;
- generator headroom must be proven;
- test-data provenance must be controlled.

Until then:
`EMPIRICAL EXECUTION FOR CAPACITY FREEZE = HOLD`.

## 5. Tool Neutrality

- k6 remains a candidate load-generator tool because it appears in the July test standard, but availability/version is unverified.
- pgbench remains a candidate DB component benchmark tool only.
- Experiment convenience never freezes architecture.
- Any alternative load/benchmark tool may be proposed through controlled technical review if it better satisfies proof obligations.

## 6. Workload Representativeness

E1 must define workload corpus with:
- business-process mix;
- read/write ratio;
- data volume and distribution;
- hot/cold working sets;
- transaction size;
- concurrency/rate/burst shapes;
- heavy/background jobs;
- integration/API behavior;
- correlated Tenant bursts;
- failure/recovery periods;
- Tenant heterogeneity.

A synthetic workload is accepted only for the claim it is representative enough to support.

## 7. Data Safety

Synthetic/anonymized governed fixtures are the default.
Production/customer data cannot be copied into the lab without separate authorization, purpose limitation, sanitization and security controls.

## 8. Cost Evidence Boundary

Normalized Cost Units may be used for relative architecture comparison only when assumptions/weights/sensitivity are explicit.
They cannot become THB cost, package price or margin evidence until recalibrated against current supplier/owned-infrastructure source data.

## 9. Evidence Invalidation

A material change to application code, runtime, schema/index/query path, DB/storage/queue version, security/control path, infrastructure class/topology, workload distribution, backup/recovery model, cost source, placement algorithm or governor invalidates affected evidence unless equivalence is proven.

## 10. E0 Exit Contract

### Safe to carry into E1
- Boss-approved conceptual architecture.
- Complete empirical HOLD register.
- Node.js current product identity for benchmark target.
- G8 measurement/economic evidence contract.
- candidate test-tool references, explicitly non-frozen.
- environment/evidence gaps and owners.

### Remains HOLD
- actual lab readiness/access;
- numerical capacity;
- prices/margins;
- topology/mechanism freeze;
- achieved RPO/RTO;
- mixed-vs-package-class winner;
- Standard->Enterprise crossover.

### E1 authorization
`WORKLOAD CORPUS / EXPERIMENT CONTRACT DESIGN = AUTHORIZED TO PROCEED`.

### Not authorized
`CAPACITY-GRADE LOAD EXECUTION = HOLD UNTIL VERIFIED LAB ENVIRONMENT`.

`PRODUCT BUILD / MERGE / DEPLOYMENT / PRODUCTION = HOLD`.

## 11. Controlled Re-entry

If E1 or later evidence finds that current Node.js runtime/product identity, conceptual tenant boundary, shared-cell model or other Boss-approved invariant is materially contradicted, only the affected scope re-enters architecture review with explicit evidence.

No general reset.