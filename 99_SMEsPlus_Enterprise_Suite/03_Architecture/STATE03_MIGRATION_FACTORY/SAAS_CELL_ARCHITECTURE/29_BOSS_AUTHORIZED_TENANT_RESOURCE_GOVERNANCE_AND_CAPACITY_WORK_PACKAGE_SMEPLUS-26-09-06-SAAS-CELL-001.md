# [SMEPLUS-26-09-06-SAAS-CELL-001]
## Boss Authorized — Tenant Resource Governance & Capacity Work Package Before Pricing

Status: BOSS AUTHORIZED FOR ARCHITECTURE DESIGN
Scope: STATE03 / Architecture Design Only
Pricing Freeze: NOT AUTHORIZED
Implementation / Production Build: NOT AUTHORIZED
Boss: Sole Final Approver

---

## 1. Purpose

Design the measurable resource-governance architecture that must exist before final Standard/Enterprise pricing is defined.

The work package must preserve the approved SMEsPlus SaaS direction:

- STANDARD remains Pool-Based Multi-Tenant SaaS.
- ENTERPRISE remains Dedicated Resource / Dedicated Tenant Environment.
- Package size is a commercial/capacity choice and is not identical to deployment tier.
- Tenant != Cell != Server != Database Host.
- Shared Infrastructure + Tenant-specific Control.
- No Unsecured Postpaid Overage.
- Prepaid Before Usage for additional chargeable consumption.
- 30-Day Notice is a preparation control, not credit.
- No Surprise Billing.
- No Evidence = No Chargeable Overage.

---

## 2. Reference Architecture Boundary

### STANDARD

Shared Application Pool
+ Shared Database Pool / Cell Database
+ Shared Object/File Storage Pool
+ Shared Queue / Worker Pool
+ Tenant-aware Security
+ Tenant-aware Quota
+ Tenant-aware Metering
+ Tenant-aware Fair Scheduling

A tenant quota or governor does NOT imply one Docker/container/database per tenant.

### ENTERPRISE

Dedicated Resource Envelope / Dedicated Tenant Environment with the same Core product semantics.

Mechanism remains open: VM, container, namespace, node pool, dedicated DB boundary, storage boundary, or hybrid are not frozen at this stage.

---

## 3. Work Package Sequence

### WP-01 — Tenant Resource Envelope Model

Define the logical capacity envelope per tenant and package.

Minimum dimensions:
- Business Database logical usage
- File / Attachment Storage
- Archive Storage
- Transaction / processing workload
- Concurrent requests
- Background jobs
- API / Integration volume
- Queue usage
- DB connections
- Event / log volume

Deliverables:
- TENANT_RESOURCE_ENVELOPE_MODEL.md
- RESOURCE_DIMENSION_REGISTER.md
- TENANT_USAGE_LEDGER_CONTRACT.md

Gate question:
Can SMEsPlus measure and attribute material resource consumption to the correct tenant without guessing?

---

### WP-02 — Database vs Attachment vs Archive Quota

Separate customer-facing capacity into distinct controlled pools.

Business Database:
- canonical transactional/business facts
- master data
- accounting/inventory/workflow/audit metadata

File / Attachment Storage:
- documents
- PDFs
- images
- drawings
- generated files
- import/export payloads

Archive Storage:
- inactive/long-term files under approved retention policy

Key rule:
Customer logical quota must not equal physical failure boundary.

Commercial Limit < Technical Hard Limit.

Deliverables:
- TENANT_STORAGE_ENVELOPE_MODEL.md
- DATABASE_ATTACHMENT_ARCHIVE_BOUNDARY.md
- CUSTOMER_LOGICAL_STORAGE_METER.md

Gate question:
Can a tenant hit its commercial quota without placing the physical database/storage platform at failure risk?

---

### WP-03 — Storage Forecast & 30-Day Notification

Design forecast-driven capacity notification.

Mandatory:
- current usage
- remaining allowance
- recent growth rate
- projected depletion/insufficiency date
- projected month-end usage
- estimated required top-up/add-on/upgrade
- evidence trace

Approved principle:
Notify 30 days before projected insufficiency when forecast supports it.

Clarification:
30-Day Notice != 30-Day Credit.

Forecast must be recalculated continuously from actual usage.

Deliverables:
- STORAGE_FORECAST_MODEL.md
- 30_DAY_CAPACITY_NOTIFICATION_CONTRACT.md
- CUSTOMER_CAPACITY_VISIBILITY_MODEL.md

Gate question:
Can the customer see an impending shortage early enough to act, while SMEsPlus still enforces prepaid-before-usage?

---

### WP-04 — Capacity Pre-Authorization for Heavy Jobs

Define workloads that require capacity pre-check/reservation before execution.

Candidate heavy workloads:
- mass import
- bulk export
- large report generation
- mass reconciliation/allocation
- AI/document processing
- large archive restore
- high-volume integration burst
- high-growth attachment upload

Control flow:
Estimate -> Reserve Capacity/Credit -> Execute -> Measure Actual -> Release Unused Reserve.

Key rule:
Do not start a heavy job that can reasonably be predicted to cross tenant or cell safety limits.

Deliverables:
- HEAVY_WORKLOAD_CLASSIFICATION.md
- CAPACITY_PREAUTHORIZATION_CONTRACT.md
- RESOURCE_RESERVATION_LEDGER.md

Gate question:
Can SMEsPlus prevent a large workload from failing midway because quota/capacity was insufficient?

---

### WP-05 — Protected Mode / Hard Cap Rules

Define progressive control states instead of immediate whole-ERP shutdown.

Candidate states (thresholds NOT frozen):
- NORMAL
- INFORMATION
- WARNING
- CAPACITY ACTION REQUIRED
- PROTECTED MODE
- HARD CAP

Protected Mode should restrict high-growth / optional workloads first.

Examples:
- large attachment uploads
- mass imports
- bulk exports
- optional AI workloads
- optional integration jobs
- non-critical archive restore

Critical ERP integrity must be protected. The system must avoid uncontrolled database/storage growth while not arbitrarily destroying or corrupting business continuity.

Deliverables:
- TENANT_CAPACITY_STATE_MACHINE.md
- PROTECTED_MODE_RULESET.md
- HARD_CAP_VETO_MATRIX.md

Gate question:
Are the restriction rules deterministic, explainable, reversible, and auditable?

---

### WP-06 — Cell Physical Headroom Model

Define capacity at three levels:

Tenant Envelope -> Cell Envelope -> Platform Envelope

STANDARD remains horizontally scalable.

Cell controls must include at least:
- CPU pressure
- memory pressure
- DB capacity
- DB connections
- storage
- worker/queue pressure
- network/I/O where material
- placement headroom

Key rules:
- Tenant Count != Capacity.
- Never use commercial quota as the physical failure boundary.
- Stop new placement before a cell enters unsafe physical headroom.
- Expand or create additional cells when measured capacity requires it.

Deliverables:
- CELL_CAPACITY_ENVELOPE.md
- CELL_PLACEMENT_AND_HEADROOM_POLICY.md
- CELL_SCALE_OUT_TRIGGER_MODEL.md

Gate question:
Can the platform safely decide KEEP / STOP PLACEMENT / EXPAND / MOVE using measured evidence?

---

### WP-07 — Storage Add-on & Package Upgrade Rules

Define how customers increase capacity without hidden billing.

Possible actions:
- DB capacity add-on
- File storage add-on
- Archive add-on
- package upgrade
- temporary capacity reservation
- Standard -> Enterprise review

Mandatory:
- price/charge visible before activation
- prepaid or secured credit confirmation before chargeable activation
- auditable effective date/time
- usage evidence retained

Deliverables:
- CAPACITY_ADDON_CONTRACT.md
- PACKAGE_MOBILITY_MODEL.md
- STANDARD_TO_ENTERPRISE_CAPACITY_REVIEW_GATE.md

Gate question:
Can a customer add capacity without surprise cost and without SMEsPlus financing unsecured overage?

---

### WP-08 — Backup / Retention / Archive Cost Model

Separate sellable logical capacity from internal physical cost.

Internal physical cost may include:
- primary data
- indexes
- WAL / transaction logs
- replication
- backups
- point-in-time recovery
- temporary processing space
- archive copies

Customer-facing quota must remain understandable and must not expose raw infrastructure complexity unless needed.

Deliverables:
- BACKUP_RETENTION_ARCHIVE_COST_MODEL.md
- LOGICAL_VS_PHYSICAL_STORAGE_MAPPING.md
- RETENTION_POLICY_BOUNDARY.md

Gate question:
Can SMEsPlus compute real Cost-to-Serve without misleading customers about what their logical quota means?

---

## 4. Pre-Pricing Evidence Gate

Pricing SHALL NOT be frozen until the following evidence exists:

1. Measured transaction/workload telemetry model.
2. Storage growth model for DB vs attachments vs archive.
3. Load tests for representative Light / Normal / Heavy / Very Heavy tenants.
4. Cell headroom and noisy-neighbor tests.
5. Backup/replication/retention multiplier evidence.
6. Cost-to-Serve per representative customer profile.
7. Commercial simulation showing customer fairness and SMEsPlus margin.
8. Package/capacity mobility test cases.

Required decision questions:
- Is the customer price understandable?
- Is the included capacity sufficient for the intended customer profile?
- Is the customer protected from surprise billing?
- Is SMEsPlus protected from unsecured resource consumption?
- Does the package remain safe for the shared cell?
- When should the customer add capacity, upgrade package, or move to Enterprise?

---

## 5. Candidate Package Simulation Profiles

Exact numbers are NOT frozen.

Simulation should include at minimum:
- Light SME
- Normal SME
- High-transaction SME
- File-heavy SME
- API-heavy SME
- Manufacturing-heavy SME
- Reporting/batch-heavy SME
- Sustained-heavy Enterprise candidate

Package sizing may use organization size as a sales signal, but actual workload remains authoritative for capacity suitability.

Principle:
Organization size helps select the room. Actual workload determines whether the room is sufficient.

---

## 6. Architecture Invariants for This Work Package

TRG-01 Tenant execution context is mandatory for metered operations.
TRG-02 Cross-tenant usage attribution is prohibited.
TRG-03 Commercial quota must not equal physical failure boundary.
TRG-04 No Unsecured Postpaid Overage.
TRG-05 Additional chargeable capacity requires prepaid/secured authorization before activation.
TRG-06 30-Day Notice is forecast preparation, not credit.
TRG-07 Historical usage evidence is immutable/auditable after period closure.
TRG-08 Wallet balance does not reset at month-end.
TRG-09 Usage counters may reset by billing period while evidence remains preserved.
TRG-10 Heavy workloads may require pre-authorization/reservation.
TRG-11 STANDARD remains shared/pool-based unless evidence justifies dedicated isolation for a specific workload or tier.
TRG-12 Tenant != Cell != Server != Database Host.
TRG-13 Tenant Count != Capacity.
TRG-14 Tier != Company Size.
TRG-15 Customer data ownership does not imply unlimited free processing capacity.
TRG-16 No Evidence = No Chargeable Overage.
TRG-17 No Surprise Billing.
TRG-18 Pricing must follow business workload and must not distort correct business/accounting behavior.

---

## 7. Explicit Non-Decisions

This authorization does NOT freeze:
- Small/Medium/Large package names
- 50 GB / 100 GB / 250 GB quota values
- THB prices
- transaction weights
- per-GB rates
- API rates
- CPU/RAM mechanisms
- Kubernetes / Docker / cgroup choices
- shared-schema vs schema-per-tenant vs DB-per-cell topology
- exact warning percentages
- suspension timing

All such items require evidence and Boss Final Approval.

---

## 8. Execution Order

WP-01 -> WP-02 -> WP-03 -> WP-04 -> WP-05 -> WP-06 -> WP-08 -> WP-07 -> Pre-Pricing Evidence Gate -> Commercial Simulation -> Boss Pricing Decision

Reason for WP-08 before WP-07 finalization:
Storage add-on pricing cannot be made reliable until logical-vs-physical storage cost, backup, replication and retention multipliers are understood.

---

## 9. Stop Condition

After completion of the Pre-Pricing Evidence Gate, STOP at:

`READY FOR BOSS COMMERCIAL / PRICING DECISION`

Do not self-freeze package prices, capacities, deployment mechanisms or production infrastructure.
