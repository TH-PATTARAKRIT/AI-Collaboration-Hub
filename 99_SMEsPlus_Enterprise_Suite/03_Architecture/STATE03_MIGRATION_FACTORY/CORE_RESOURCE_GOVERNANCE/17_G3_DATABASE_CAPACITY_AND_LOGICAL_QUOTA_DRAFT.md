# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G3 — Database Capacity & Logical Quota Draft

Status: EXECUTION DRAFT — SUBJECT TO SPECIALIST REVIEW / INDEPENDENT CHALLENGE
Gate: G3 — Storage / Database Gate
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. G3 Database Scope

This model closes the conceptual separation among:

1. Tenant-visible Business Database logical usage;
2. Cell/database physical consumption and operational headroom;
3. platform protection overhead (indexes, WAL/logs, replicas, backups, restore workspace, maintenance/transient space);
4. enforcement behavior before physical exhaustion.

No numerical GB quota, DB topology, schema model, PostgreSQL tenancy pattern, Cell threshold, price, or rate is frozen by G3.

## 2. Canonical Database Capacity Layers

### D1 — Tenant Business Data Logical Usage
Customer-facing logical capacity representing Tenant-attributable canonical business facts and metadata under the product contract.

Candidate included classes:
- master/business records;
- transactional records;
- accounting/inventory/workflow facts;
- audit/application metadata that is materially Tenant-owned;
- approved retained structured payload metadata.

It MUST NOT be defined as raw database filesystem bytes.

### D2 — Database Physical Footprint
Engineering measurement of actual DB storage consumption, including structures that may not map 1:1 to customer logical content.

Examples:
- table heap;
- indexes;
- TOAST / overflow storage;
- free-space / visibility structures;
- temporary processing footprint;
- maintenance/bloat effects;
- WAL / transaction logs;
- replicas;
- backup/PITR footprint;
- restore staging.

### D3 — Cell Database Safety Envelope
Multi-dimensional safety boundary used by placement/admission/protection controls.

It must reserve sufficient operational headroom for:
- normal writes and transaction completion;
- vacuum/maintenance;
- index operations where required;
- WAL/log continuity;
- failover/replication obligations;
- restore/recovery workspace where applicable;
- emergency integrity reserve.

`Tenant Commercial Quota` MUST NOT be the same boundary as `Cell Database Failure Boundary`.

## 3. Logical Meter Principle

A Tenant logical DB meter must be reconstructable from Tenant-attributed application/data facts and must not depend solely on physical relation/database size.

Reasons:
- physical table size can include indexes, TOAST and internal storage structures;
- shared tables may contain rows for many Tenants;
- vacuum/bloat/index changes can alter physical bytes without a customer business event;
- implementation/index improvements must not change customer charges retroactively.

Therefore:

`Customer Logical DB Usage -> independently attributable logical measure`

and

`Physical DB Consumption -> platform telemetry / Cost-to-Serve / safety evidence`

must be related by reconciliation, not treated as identical measurements.

Exact logical-byte or commercial-unit algorithm remains HOLD for G6/G8 evidence.

## 4. Reconciliation Contract

At minimum retain a periodic/reconstructable reconciliation chain:

`Tenant logical record/activity evidence`
-> `Tenant logical DB usage ledger`
-> `shared DB physical telemetry`
-> `Cell physical capacity state`
-> `variance / amplification analysis`

Large divergence is not automatically customer overage. It is an engineering signal requiring classification such as:
- expected index amplification;
- expected storage format overhead;
- platform inefficiency/bloat;
- abnormal Tenant workload pattern;
- corruption/operational anomaly;
- measurement defect.

## 5. Headroom States — Conceptual

No exact thresholds are frozen.

Candidate DB capacity states:

`NORMAL`
-> `INFORMATION`
-> `WARNING`
-> `CAPACITY ACTION REQUIRED`
-> `PROTECTED MODE`
-> `HARD CAP / EMERGENCY SAFETY`

Rules:
- controls activate before physical exhaustion;
- stop/new-placement decisions occur before unsafe headroom;
- optional/high-growth workloads are restricted before integrity-critical writes where technically safe;
- a protected physical operating reserve must exist for explicitly classified critical ERP integrity operations;
- operating reserve is finite and cannot be treated as unlimited free entitlement;
- if physical safety/correctness cannot be preserved, emergency hard-cap behavior may supersede ordinary commercial entitlement.

## 6. Database Growth Admission

Operations likely to create material DB growth must be classifiable for preflight where reasonably predictable:
- mass import;
- bulk posting/reprocessing;
- large allocation/reconciliation;
- history ingestion/migration;
- high-volume API batch;
- report materialization into retained DB state;
- archive restore into active DB.

Candidate control:

`Estimate growth -> check Tenant entitlement -> check Cell headroom -> reserve if required -> execute -> measure actual -> reconcile/release reserve`.

A forecast error must not rewrite historical usage evidence.

## 7. Entitlement Reduction Safety

When a Package/Add-on shrinks below current logical DB usage:
- do not delete canonical business/accounting/audit truth;
- enter controlled over-entitlement state;
- block or preauthorize additional non-critical growth first;
- offer cleanup/archive only where semantically/legal permitted;
- schedule upgrade/add-on/Enterprise review as applicable;
- preserve reconstructable entitlement and usage history.

## 8. DB Capacity Ownership & Tenant Isolation

Every Tenant-attributed DB usage event must carry trusted Tenant execution context.

Forbidden:
- attributing shared/system DB growth to a customer without evidence;
- cross-Tenant pooling of logical DB entitlement for unrelated customers;
- using admin/background work without preserved Tenant provenance as billable evidence;
- treating a shared physical database as a shared Tenant security boundary.

## 9. PostgreSQL Technical Evidence — Mechanism-Neutral Use

Current PostgreSQL 18 documentation provides two relevant facts used only as engineering evidence, not topology freeze:

- `pg_total_relation_size` includes table storage, indexes and TOAST data, demonstrating that physical relation size contains implementation/storage structures beyond a simple logical business payload.
  Source: https://www.postgresql.org/docs/18/functions-admin.html
- PostgreSQL can store oversized values through TOAST or Large Object facilities, so binary/large-field choices can materially affect transactional DB footprint.
  Source: https://www.postgresql.org/docs/18/lo-intro.html

These facts support separation of customer logical usage from physical DB footprint. They do NOT mandate PostgreSQL topology, shared schema, RLS, DB-per-Tenant or any final storage implementation.

## 10. Database Invariants Candidate

G3-DB-01 Customer logical DB usage != physical DB filesystem usage.

G3-DB-02 Shared DB physical overhead must not be blindly billed to individual Tenants.

G3-DB-03 Cell DB headroom is multi-dimensional and includes operational/recovery reserve.

G3-DB-04 Commercial quota must remain below technical failure boundary in every material dimension.

G3-DB-05 Noisy-neighbor controls must engage before DB resource exhaustion.

G3-DB-06 Platform inefficiency/bloat/index defects are not automatically customer usage.

G3-DB-07 Critical integrity reserve is finite, platform-governed and safety-bounded.

G3-DB-08 Downgrade/quota shrink cannot destroy business truth.

G3-DB-09 Tenant logical usage and physical telemetry must reconcile through explainable variance classes.

G3-DB-10 Numerical quotas/thresholds remain HOLD until measured evidence exists.

## 11. Open Evidence Obligations

- actual logical DB measurement algorithm;
- shared-table per-Tenant attribution cost/accuracy;
- amplification ratios for indexes/TOAST/WAL/backup/replication;
- DB growth profiles by representative Tenant class;
- emergency operating reserve size;
- maintenance/vacuum headroom evidence;
- restore workspace requirement;
- numerical Cell stop-placement thresholds;
- Cost-to-Serve and pricing conversion.

These obligations proceed to later gates and are not silently closed by conceptual G3 approval.
