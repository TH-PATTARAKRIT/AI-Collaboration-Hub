# [SMEPLUS-26-09-10-CORE-RESOURCE-EMPIRICAL-001]
# E1 — Corrected Experiment Contract & Exit Contract

Status: CORRECTED CANDIDATE — READY FOR INDEPENDENT RE-CHALLENGE
Corrects: SR-02..SR-13 and CH C-01..C-12
Final Approver: Boss only
Build / Merge / Deployment / Production: HOLD

## 1. Business Outcome Reconciliation

Every write-bearing production-intent run must prove more than transport success.

Required result layers:
1. request/response outcome;
2. persisted canonical business effect;
3. duplicate/missing-effect detection;
4. idempotency/retry reconciliation;
5. domain-state reconciliation for material entities.

A high-throughput run with incorrect business outcomes is `INVALID FOR CAPACITY`.

## 2. Accounting / Inventory Integrity Assertions

Where the tested workflow reaches Accounting or Inventory truth, the campaign must include applicable assertions such as:
- expected posting count/state;
- debit/credit or ledger reconciliation identities where implemented;
- inventory movement/quantity/state consistency;
- no duplicate posting/movement from retry;
- reconciliation of committed vs failed/ambiguous outcomes.

Exact functional rules remain owned by domain evidence; performance testing does not invent accounting logic.

## 3. Per-Tenant Fairness / Starvation Evidence

Shared-resource campaigns must retain per-Tenant evidence for:
- latency/error distribution;
- DB connection wait;
- queue wait/depth;
- throughput/service share;
- rejected/deferred/throttled actions;
- governor/protection state transitions;
- starvation/fairness incidents;
- post-pressure recovery.

Cell average PASS cannot hide Tenant harm.

## 4. Correlated-Burst Provenance

Every correlated-burst campaign records:
- business rationale/source pattern;
- synchronization model;
- affected Tenant/workload families;
- whether timing is synthetic, replay-derived or observed from verified business evidence;
- generator scheduling method;
- proof that correlation is not created accidentally by generator batching.

## 5. External Dependency Mode

Mandatory enum per dependency:
- `STUB`;
- `CONTROLLED_SIMULATOR`;
- `REAL_NONPROD`;
- `UNCONTROLLED_EXTERNAL`.

UNCONTROLLED_EXTERNAL behavior that materially determines result validity forces HOLD unless the variance is explicitly bounded and the claim is limited accordingly.

## 6. Run / Comparison / Supersession Lineage

Run Ledger adds:
- `comparison_group_id`;
- `baseline_run_id` where applicable;
- `supersedes_run_id`;
- `superseded_by_run_id`;
- `campaign_decision_reference`;
- `failed/aborted reason`;
- `raw_artifact_manifest_id`.

Failed/invalid runs remain visible and cannot be erased by a later favorable run.

## 7. Cost Source Confidence / Expiry

Economic evidence records:
- source effective date;
- source expiry/review date;
- procurement/commitment regime;
- currency/FX basis where relevant;
- source confidence;
- known exclusions;
- recalibration trigger.

A stale/changed cost regime invalidates affected CTS/price/crossover evidence unless equivalence is proven.

## 8. Recovery RTO Completion Boundary

For any claimed recovery scope:

`RTO achieved` ends only when the claimed usable service is available AND required business truth is reconciled sufficiently for that scope.

The clock cannot stop merely when:
- VM starts;
- DB accepts connections;
- application health endpoint returns OK;
- routing is restored;
if business state, external effects, security state or placement authority remain unresolved.

## 9. Security / Correctness Hard Veto

Every relevant campaign records explicit:
- Tenant-isolation result;
- authorization/security control result;
- business-integrity result;
- placement/split-brain result where applicable;
- recovery-truth result where applicable.

Any hard-veto FAIL blocks the affected mechanism/capacity candidate regardless of throughput or cost benefit.

## 10. Fixture Representativeness + Data Classification

Fixture manifest includes:
- synthetic/anonymized/source classification;
- sanitization method where applicable;
- business-relationship realism;
- distribution/selectivity/skew profile;
- expected working-set behavior;
- limitations and claims it cannot support.

Privacy-safe but unrealistic fixtures cannot support broad package sizing.
Realistic but unauthorized protected data is prohibited.

## 11. Environment Drift / Campaign Event Log

During long runs/campaigns record material events including:
- deployment/restart;
- config change;
- host migration;
- backup/maintenance event;
- autoscaling/resource-limit change if any;
- DB maintenance/failover;
- network/storage incident;
- observability configuration change.

Unexplained drift can invalidate comparability.

## 12. Raw Artifact Integrity

Capacity-grade results require raw artifact location + checksum/manifest when feasible.

If a checksum cannot be produced, the exception must state why, what alternative integrity proof exists and whether it limits the claim. Manual summary without reconstructable raw evidence cannot support a final numerical freeze.

## 13. Platform Defect Exclusion

Every abnormal spike/failure must be classified:
- legitimate Tenant demand;
- expected shared amplification;
- platform retry/failure amplification;
- bad query/index/schema/application behavior;
- control/observability overhead;
- external dependency;
- unknown/anomaly.

Unknown/anomaly remains HOLD and cannot become customer usage or Enterprise-candidacy evidence.

## 14. E1 Exit Contract

### Approved to carry forward
- workload family taxonomy and proof obligations;
- benchmark classes;
- Run Ledger/telemetry schema;
- business-outcome/domain-integrity evidence requirement;
- per-Tenant fairness contract;
- environment/generator/instrumentation binding;
- fixture/data-safety contract;
- validity/repetition/distribution rules;
- evidence invalidation/supersession rules;
- cost-source confidence/expiry rules;
- recovery RTO truth boundary;
- security/correctness hard-veto contract.

### Still HOLD
- verified Architecture Lab environment/access;
- actual load execution;
- any numerical capacity;
- prices/margins;
- RPO/RTO values;
- topology/mechanism selection;
- Cell A/B winner;
- Standard->Enterprise crossover.

### Next-gate boundary
E2 may prepare execution packages, test scripts, synthetic fixtures and environment-verification checklists.

However:
`NO CAPACITY-GRADE RUN MAY BE CLAIMED VALID UNTIL VERIFIED LAB ENVIRONMENT + TELEMETRY + GENERATOR EVIDENCE EXISTS`.

Product Build / Merge / Deployment / Production remain HOLD.