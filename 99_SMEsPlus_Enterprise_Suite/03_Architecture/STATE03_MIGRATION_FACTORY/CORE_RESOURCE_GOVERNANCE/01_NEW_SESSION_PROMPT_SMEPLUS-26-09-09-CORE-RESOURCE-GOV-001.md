# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# SMEsPlus Core Resource Governance & Package Capacity Architecture — NEW SESSION
# /L9999.9999

## 0. SESSION IDENTITY

- Project: SMEsPlus ENTERPRISE SUITE
- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Canonical Branch: `SMEsPlus`
- Jira: `ERPPLUS-152`
- Parent Architecture Session: `[SMEPLUS-26-09-06-SAAS-CELL-001]`
- Parent Jira: `ERPPLUS-151`
- Executor: SMEsPlus Core Architecture Team (`SMEs Core`)
- Review: AAS+ / PMO / Independent Architecture Challenge
- Final Approver: Boss only
- Scope: Architecture and design evidence only
- Build / Team C / production authorization: NOT GRANTED

This NEW SESSION is a controlled continuation of the existing SMEsPlus SaaS Cell Architecture. It MUST NOT restart prior research, discard prior evidence, or reinterpret previously approved Boss decisions without a material evidence delta.

Mandatory governance:

> No Evidence = No Progress.

> Never Skip Gate.

> No repeated question without material delta.

> Freeze invariants before mechanisms.

> Boss is the sole Final Approver.

---

## 1. WHY THIS SESSION EXISTS

SMEsPlus now requires a single coherent architecture for how Commercial Package, Organization Size, Tenant, Cell, Server Pool, Database Pool, File/Object Storage Pool, CPU, RAM, Worker Capacity, Queue, API, Storage, Backup, Metering, Prepaid Wallet, and Standard/Enterprise deployment boundaries work together.

The current architectural intent is NOT `one Tenant = one Docker = one Database` for STANDARD by default.

The current STANDARD direction remains a Pool-based Multi-tenant SaaS architecture with Tenant-aware controls:

`Shared Infrastructure + Tenant-specific Security + Tenant-specific Quota + Tenant-specific Metering + Tenant-aware Fair Scheduling`.

The purpose of this session is to remove ambiguity before detailed system design and implementation.

---

## 2. MANDATORY PARENT DECISIONS TO PRESERVE

The team MUST reconcile and preserve all parent decisions and their audit lineage, including at minimum:

1. Two deployment tiers only: `STANDARD` and `ENTERPRISE`.
2. STANDARD = shared resources / multi-tenant cells / cost optimized.
3. ENTERPRISE = dedicated resource / dedicated tenant environment / stronger SLA and isolation.
4. No third PRIVATE commercial tier.
5. Tier != organization size / company count / package name.
6. One product / one Core codebase / many cells.
7. Tenant identity != Server / Database / Cell identity.
8. Standard must horizontally scale; no nationwide monolithic server/database design.
9. Package may be sized by organization profile, but actual workload must validate package sufficiency.
10. Standard may have multiple package/capacity classes.
11. Package size != physical server identity.
12. Prepaid Before Usage for additional chargeable consumption.
13. 30-Day depletion notice is forecast/preparation control, not unsecured credit.
14. No Unsecured Postpaid Overage.
15. No Surprise Billing.
16. No Evidence = No Chargeable Overage.
17. Wallet balance does not reset by billing period.
18. Usage counters may reset by billing period while historical evidence remains auditable.
19. Customer-facing logical usage must be separated from internal physical infrastructure consumption.
20. SMEsPlus inefficiency, bad SQL, N+1, memory leaks, defective indexes, or platform defects MUST NOT be charged to customers as usage.

Relevant parent decision records include, but are not limited to, Architecture records 22 through 28 under `SAAS_CELL_ARCHITECTURE`.

---

## 3. CORE QUESTION THIS SESSION MUST ANSWER

The final architecture must answer, without contradiction:

> What does a customer buy?

> What resource envelope does that purchase include?

> How does SMEsPlus measure and enforce the envelope?

> Which resources are shared and which are isolated?

> How does STANDARD remain economically efficient while preventing noisy-neighbor risk?

> How are Database, File/Attachment Storage, CPU, RAM, Queue, Worker, API, Network, Backup, and heavy jobs governed per Tenant?

> How does a Package map to a Capacity Class without becoming a fixed Server identity?

> When should a Tenant move within STANDARD, upgrade Package, buy additional Capacity, or become an ENTERPRISE candidate?

> How do Billing, Wallet, Metering, Capacity, and Infrastructure stay traceable to the same usage evidence?

---

## 4. CANONICAL LAYER MODEL TO TEST

The team MUST explicitly validate or correct the following separation:

### Layer 1 — Commercial Package
What the customer buys.

Examples may later include Small / Medium / Large, but package names and final prices are NOT frozen by this session start.

### Layer 2 — Tenant
Who the customer/security boundary is.

### Layer 3 — Capacity Entitlement
What logical limits and included allowances the Tenant is entitled to consume.

### Layer 4 — Cell / Placement
Where the Tenant is operationally placed.

### Layer 5 — Infrastructure
Actual App nodes, Database clusters, Object Storage, Worker pools, Queue, Cache, network and backup infrastructure.

Invariant candidate:

`PACKAGE != TENANT != CELL != SERVER != DATABASE HOST`.

This must be proven or corrected with evidence before freeze.

---

## 5. STANDARD ARCHITECTURE HYPOTHESIS TO CHALLENGE

The team MUST challenge, not blindly accept, this working hypothesis:

```text
SMEsPlus STANDARD

Tenant Gateway
    -> Shared App Pool
    -> Shared / Cell-scoped Database Pool
    -> Shared Object/File Storage Pool
    -> Shared Queue / Worker Pool
    -> Tenant-aware Resource Governor
    -> Tenant-aware Metering / Usage Ledger
```

A Tenant Resource Governor does NOT automatically imply one Docker/Container per Tenant.

A Tenant quota does NOT automatically imply one Database per Tenant.

A Package does NOT automatically imply one physical Server.

Containers / isolated workers may be used for heavy jobs or specific workload isolation if evidence supports them, but do not freeze `Docker-per-Tenant` without a material technical/economic justification.

---

## 6. RESEARCH STANDARD — L1 TO L12

Execute the complete research ladder. Do not skip levels.

### L1 — Domain Definition
Define Package, Capacity, Resource Entitlement, Tenant, Cell, Pool, Quota, Limit, Reserve, Headroom, Usage, Overage, Prepaid Credit, Reserved Capacity, Logical Usage and Physical Consumption.

### L2 — Resource Inventory
Enumerate all resources that can become material constraints: CPU, RAM, DB size, DB connections, query time, IOPS, WAL/log growth, File/Attachment Storage, Archive Storage, backup, restore, worker time, queue depth, API, network, concurrent requests, generated files, reporting, export/import and AI/external services.

### L3 — Functional Controls
Define how the platform measures, warns, reserves, throttles, rejects, top-ups, upgrades, relocates and records usage.

### L4 — Cross-System Interaction
Reconcile Package, Billing, Wallet, Tenant Management, Cell Placement, Database, Storage, Worker, API, Backup, Audit and Customer Portal.

### L5 — Whole-System Capacity
Model `Tenant Envelope -> Cell Envelope -> Platform Envelope`.

### L6 — Contradictions / Edge Cases
Test burst usage, rapid DB growth, large attachment uploads, 1M-row imports, bulk exports, heavy reports, tenant migration, partial failures, rollback, wallet depletion, forecast error, cell saturation and data-heavy low-user tenants.

### L7 — Control / Internal Control
Define approvals, spending controls, prepaid enforcement, evidence, segregation of duties and administrative override limits.

### L8 — Data / Identity / Immutability
Ensure tenant identity, usage evidence, billing records, capacity history and migration history remain immutable/traceable where required.

### L9 — SaaS / Multi-Company
Ensure Tenant/Company boundaries and cross-tenant deny-by-default controls remain intact under shared pools.

### L10 — Migration / Historical
Design package upgrades, capacity add-ons, Standard cell-to-cell movement and Standard-to-Enterprise mobility while preserving lineage and semantics.

### L11 — Reconciliation / End-to-End Proof
Prove the chain:

`Customer Package -> Entitlement -> Actual Usage -> Meter -> Wallet/Charge -> Capacity Enforcement -> Customer Statement -> Internal Cost-to-Serve`.

### L12 — Adversarial Challenge
Attack assumptions, economics, noisy-neighbor protection, data growth, DB failure boundaries, fairness, gaming, operational burden, forecasting error, customer experience and hidden-cost risk.

---

## 7. REQUIRED WORKSTREAMS

### WS-01 — Commercial Package Capacity Model
Define what a Package includes and what remains usage-based or optional.

Must evaluate:
- organization size as package-sizing signal, not sole determinant;
- user count;
- company/branch count;
- transaction volume;
- storage;
- API/integration;
- processing workload;
- growth forecast;
- support/SLA boundaries;
- Standard package mobility.

Do NOT freeze final price bands without Cost-to-Serve evidence.

### WS-02 — Database Capacity Model
Separate customer-visible logical Database allowance from internal physical DB/storage cost.

Must address:
- business data size;
- indexes;
- WAL / transaction logs;
- replication;
- temporary space;
- PITR;
- backups;
- restore staging;
- vacuum / maintenance headroom;
- growth rate;
- per-tenant logical usage measurement;
- cell-level physical capacity;
- commercial limit vs technical hard limit.

Mandatory candidate principle to prove:

> Commercial Limit < Technical Failure Boundary.

### WS-03 — File / Attachment / Archive Storage
Design separately from Business Database.

Must evaluate:
- Object Storage architecture;
- metadata in DB vs binary object content;
- tenant namespace/security;
- per-file size limits;
- per-tenant storage allowance;
- hot vs archive lifecycle;
- legal/audit retention;
- customer-visible usage;
- top-up / storage add-on;
- upload preflight;
- large export packaging;
- backup/restore relationship.

### WS-04 — CPU / RAM / Runtime Governance
Define how STANDARD controls CPU- and RAM-producing workloads when tenants share App processes/nodes.

Must distinguish:
- hard infrastructure limit;
- logical tenant limit;
- request concurrency;
- worker concurrency;
- background jobs;
- timeouts;
- query limits;
- memory-intensive processing;
- heavy-job isolation;
- sustained heavy workload vs temporary burst.

Do NOT claim OS/container hard limits per tenant inside the same shared process unless technically proven.

### WS-05 — Worker / Queue / Heavy Job Governance
Define workload classes and fair scheduling.

Candidate priority model may include critical ERP, normal interactive, background, heavy/optional workloads, but final classes are evidence-dependent.

Heavy jobs must support preflight / capacity reservation where economically necessary.

### WS-06 — Database Connection & Query Governance
Define connection budgets, statement timeout, query cost controls, runaway query detection, batch limits, transaction boundaries and protection against one tenant exhausting the DB pool.

### WS-07 — Cell Capacity & Placement
Design Cell capacity classes and placement strategy without binding package to a specific physical server.

Must answer:
- shared mixed-package cell vs package-class cell;
- S/M/L Cell classes if justified;
- tenant placement signals;
- cell headroom;
- admission control;
- stop-placement threshold;
- horizontal scale trigger;
- live/cold movement requirements;
- noisy-neighbor containment;
- cell failure blast radius.

### WS-08 — Metering & Usage Ledger
Create one auditable usage evidence model that can support:
- customer dashboard;
- billing/wallet deductions;
- capacity enforcement;
- cost-to-serve;
- dispute handling;
- package recommendation;
- Enterprise candidacy.

Internal raw telemetry and customer-facing commercial units MUST be related but do not need to be identical.

### WS-09 — Prepaid Wallet & Capacity Authorization
Preserve:

> Prepaid Before Usage.

> 30-Day Notice != 30-Day Credit.

> No Unsecured Postpaid Overage.

Design:
- Total Balance;
- Reserved Balance;
- Available Balance;
- pending authorized usage;
- heavy job pre-authorization;
- top-up confirmation;
- projected depletion;
- 30-day notice;
- accelerated depletion recalculation;
- service continuity boundaries;
- exit/export capacity.

### WS-10 — Customer Usage & Capacity UX
The customer must understand:
- current Package;
- included Capacity;
- current usage;
- remaining allowance;
- projected month-end usage/cost;
- projected depletion date;
- recommended top-up;
- what action is blocked or allowed;
- evidence behind any charge.

First Image requirement:

> The customer should know what is included, what is being consumed, and what will cost more before consumption becomes chargeable.

### WS-11 — Backup / Restore / DR Capacity
Separate customer logical quota from platform protection overhead.

Must model:
- backups;
- PITR;
- replicas;
- RPO/RTO;
- restore workspace;
- attachment backup/replication;
- archive;
- tenant restore vs cell restore;
- Enterprise differences.

### WS-12 — Cost-to-Serve & Economic Validation
No package capacity may be frozen without a measurable Cost-to-Serve model.

At minimum simulate:
- Light SME;
- Normal SME;
- Heavy SME;
- Data-heavy / attachment-heavy SME;
- API-heavy SME;
- Manufacturing/report-heavy SME;
- sustained heavy tenant / Enterprise candidate.

For every scenario ask:

1. Is customer cost understandable and fair?
2. Does SMEsPlus preserve target margin?
3. Is the Tenant safe for the selected Cell?
4. Is Package upgrade enough?
5. Is Enterprise economically/technically preferable?

---

## 8. STORAGE ENFORCEMENT DESIGN MUST NOT BE ALL-OR-NOTHING

The team MUST design staged behavior rather than wait for 100% usage and then shut down ERP.

Candidate states to validate:

`NORMAL -> INFORMATION -> WARNING -> CAPACITY ACTION REQUIRED -> PROTECTED MODE -> HARD CAP`

Exact thresholds are NOT frozen.

Protected Mode should prioritize restricting high-growth / optional workload before mission-critical business posting, where technically safe.

Examples to evaluate:
- large attachment upload;
- mass import;
- large generated export;
- optional AI/document processing;
- large report materialization;
- archive restore;
- high-volume API batch.

Mission-critical accounting/inventory transactions require explicit operating reserve and failure-boundary design.

---

## 9. REQUIRED INVARIANT REGISTER

At minimum evaluate and disposition the following candidates:

- CRG-01: Tenant identity is independent of physical Server/Node/Cell identity.
- CRG-02: Package is a commercial entitlement, not a physical host identity.
- CRG-03: Tenant quota does not imply dedicated infrastructure.
- CRG-04: Standard remains shared-resource multi-tenant unless evidence justifies isolation.
- CRG-05: Commercial quota must not equal the platform physical failure boundary.
- CRG-06: Customer logical storage usage is distinct from replication/backup/system overhead.
- CRG-07: Attachments should not inflate the transactional DB binary footprint without justified reason.
- CRG-08: Resource enforcement must preserve tenant isolation and accounting integrity.
- CRG-09: Heavy optional workload may require preflight and resource/credit reservation.
- CRG-10: 30-Day forecast warning does not create unsecured service credit.
- CRG-11: Additional chargeable consumption requires paid/secured entitlement before execution.
- CRG-12: No customer may be charged for SMEsPlus implementation inefficiency.
- CRG-13: Usage evidence must reconcile to customer statements and internal telemetry.
- CRG-14: Package migration or cell movement must not change business semantics.
- CRG-15: Standard-to-Enterprise mobility must preserve identity, audit lineage and data semantics.
- CRG-16: Cell admission is based on measurable capacity, not fixed tenant count alone.
- CRG-17: Noisy-neighbor prevention must operate before physical resource exhaustion.
- CRG-18: Backup/DR overhead is a platform protection concern and must not be naively equated to customer logical quota.

Each invariant must end as `APPROVE / MODIFY / REJECT / HOLD` with evidence and rationale.

---

## 10. REQUIRED DELIVERABLES

Create at minimum:

1. `02_CORE_RESOURCE_GOVERNANCE_TERMINOLOGY_AND_INVARIANTS.md`
2. `03_PACKAGE_TO_CAPACITY_ENTITLEMENT_MODEL.md`
3. `04_DATABASE_CAPACITY_AND_LOGICAL_QUOTA_MODEL.md`
4. `05_FILE_ATTACHMENT_ARCHIVE_STORAGE_MODEL.md`
5. `06_CPU_RAM_RUNTIME_RESOURCE_GOVERNANCE_MODEL.md`
6. `07_WORKER_QUEUE_HEAVY_JOB_GOVERNANCE_MODEL.md`
7. `08_DATABASE_CONNECTION_AND_QUERY_GOVERNANCE_MODEL.md`
8. `09_STANDARD_CELL_CAPACITY_AND_PLACEMENT_MODEL.md`
9. `10_USAGE_LEDGER_METERING_AND_PREPAID_AUTHORIZATION_MODEL.md`
10. `11_CUSTOMER_CAPACITY_DASHBOARD_AND_30_DAY_FORECAST_MODEL.md`
11. `12_BACKUP_RESTORE_DR_CAPACITY_MODEL.md`
12. `13_COST_TO_SERVE_AND_PACKAGE_ECONOMIC_SIMULATION.md`
13. `14_STANDARD_TO_ENTERPRISE_CAPACITY_MOBILITY_MODEL.md`
14. `15_CROSS_MODEL_CONTRADICTION_AND_RECONCILIATION_REGISTER.md`
15. `16_INDEPENDENT_ADVERSARIAL_CHALLENGE_REPORT.md`
16. `17_PMO_VERIFICATION_AND_BOSS_DECISION_PACKAGE.md`

If research discovers that any deliverable must split into more files, do so without deleting traceability.

---

## 11. GATE SEQUENCE

### G0 — Parent Evidence Reconciliation
Read and reconcile existing SaaS Cell architecture and Boss decisions. Do not redesign from memory.

### G1 — Terminology / Invariant Gate
Freeze shared vocabulary before numerical sizing.

### G2 — Package / Entitlement Gate
Define what the customer buys and what capacity is included conceptually.

### G3 — Storage / Database Gate
Close logical quota, attachment, archive and platform headroom model.

### G4 — Compute / Runtime Gate
Close CPU, RAM, DB connection, worker and queue governance model.

### G5 — Cell / Placement Gate
Close Standard shared-cell capacity and movement logic.

### G6 — Metering / Wallet Gate
Close usage evidence, prepaid authorization and customer transparency model.

### G7 — Backup / DR Gate
Close platform protection overhead and restore architecture boundaries.

### G8 — Cost / Load-Test Readiness Gate
Produce assumptions, measurements required and economic simulation. Numerical package limits remain HOLD until evidence exists.

### G9 — Independent Adversarial Challenge
Challenge all open assumptions and identify false certainty.

### G10 — PMO Verification
Verify completeness, evidence, contradictions, traceability and unresolved decisions.

### G11 — Boss Final Decision Gate
Stop and present Boss with only decisions that genuinely require Boss judgment.

Do NOT self-declare final architecture approval.

---

## 12. NUMERICAL SIZING RULE

Examples such as Database 50 GB / 100 GB / 250 GB, File Storage 100 GB / 250 GB / 500 GB, CPU/RAM values, cell utilization thresholds or package prices are HYPOTHESES until supported by evidence.

For every proposed number provide:

- source or benchmark;
- workload assumption;
- load-test requirement;
- cost-to-serve effect;
- operational headroom;
- failure boundary;
- customer experience impact;
- recommended confidence level.

No Evidence = No Freeze.

---

## 13. REQUIRED LOAD / CAPACITY TEST DESIGN

The session must define the test plan even if execution is not yet authorized.

At minimum include:

- concurrent users;
- order/invoice/posting throughput;
- inventory movement throughput;
- batch import;
- heavy report;
- attachment upload/download;
- API burst;
- DB growth;
- index growth;
- WAL/log growth;
- backup duration;
- restore duration;
- worker saturation;
- queue backlog;
- memory pressure;
- noisy-neighbor attack;
- multiple package classes in one cell;
- cell near-admission limit;
- tenant relocation scenario.

---

## 14. DECISION DISCIPLINE

Use these labels:

- `FACT`
- `EVIDENCE`
- `INTERPRETATION`
- `ASSUMPTION`
- `RECOMMENDATION`
- `OPEN DECISION`
- `BOSS DECISION REQUIRED`

Do not convert an assumption into a fact by repetition.

Do not claim `best practice` without source/evidence.

Do not freeze Docker, Kubernetes, RLS, schema-per-tenant, DB-per-tenant, VM-per-tenant, cgroups, physical server mapping or any other mechanism merely because it is familiar.

Mechanism follows proven requirements.

---

## 15. STOP CONDITIONS

Stop and mark `HOLD` if any of the following occurs:

- missing parent evidence;
- contradictory Boss decisions not reconciled;
- numerical sizing without evidence;
- inability to prove tenant isolation under a proposed shared design;
- inability to reconcile customer logical quota to actual metering;
- inability to explain physical headroom;
- package model that makes STANDARD economically non-viable;
- resource model that requires hidden postpaid exposure;
- architecture that silently turns STANDARD into per-tenant dedicated infrastructure;
- any proposal that changes previously approved business/accounting semantics.

---

## 16. FINAL OUTPUT TO BOSS

At the Boss Final Decision Gate, provide:

1. One-page architecture overview.
2. Package-to-Capacity matrix.
3. STANDARD shared-pool reference architecture.
4. Database / File / Archive quota model.
5. CPU / RAM / Worker / Queue governance model.
6. Cell capacity and placement model.
7. Prepaid / 30-day warning / capacity authorization model.
8. Cost-to-Serve evidence summary.
9. Open assumptions ranked by risk.
10. Explicit Boss decisions required.
11. Recommended next session only after Boss decision.

Do not ask Boss to select low-level mechanisms that the technical evidence can resolve independently.

---

## 17. SESSION CONSTITUTION

> Understand deeply.

> Transfer accurately.

> Preserve verifiably.

> Shared infrastructure does not mean uncontrolled infrastructure.

> Package defines entitlement; telemetry proves consumption.

> Customer quota controls commercial consumption; platform headroom protects system integrity.

> Prepaid before additional chargeable usage.

> No Evidence = No Progress.

> Never Skip Gate.

> Boss is the sole Final Approver.
