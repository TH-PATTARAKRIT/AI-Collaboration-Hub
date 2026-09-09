# BOSS DIRECTION — STANDARD TO ENTERPRISE MOBILITY MUST BE DESIGNED

Session: `[SMEPLUS-26-09-06-SAAS-CELL-001]`
Jira: `ERPPLUS-151`
Date: 2026-09-09
Status: **BOSS DIRECTION — ARCHITECTURE DESIGN REQUIRED; NOT YET PRICING/MECHANISM FREEZE**

## 1. Boss Direction

The Architecture Advisor and SME Core Team must explicitly design the case where a customer moves from **STANDARD** to **ENTERPRISE**.

This is not an exceptional afterthought. Upward mobility is a first-class SaaS capability and must be designed before Pricing Freeze.

## 2. Constitutional Position

- STANDARD remains Pool-Based Multi-Tenant SaaS with tenant-specific control.
- ENTERPRISE remains Dedicated Resource / Dedicated Tenant Environment with stronger isolation, SLA and reserved capacity.
- STANDARD -> ENTERPRISE is a normal supported mobility path.
- ENTERPRISE -> STANDARD is a controlled exception and requires separate validation.
- Tier != Company Size.
- Tenant identity must remain stable across tier movement.
- Tenant != Cell != Server != Database Host.
- Cell/tier movement must not change business, accounting, tax, audit or transaction semantics.
- One Core Codebase remains mandatory; no customer Core fork is created by migration.

## 3. New Work Package

Add:

### WP-09 — STANDARD TO ENTERPRISE MOBILITY CONTRACT

This work package is mandatory before Commercial / Pricing Freeze.

It must define at minimum:

1. Mobility trigger model.
2. Customer-requested vs system-recommended upgrade path.
3. Technical and economic crossover criteria.
4. Enterprise destination capacity reservation and provisioning.
5. Database migration / replication / cutover options.
6. File & attachment migration.
7. Tenant configuration, permissions, extensions and integration continuity.
8. Scheduled jobs / queues / workers continuity.
9. Wallet, prepaid balance, usage ledger and billing continuity.
10. Audit evidence, reconciliation and provenance continuity.
11. Cutover window, routing change and service continuity.
12. Rollback and recovery contract.
13. Post-cutover validation and observation period.
14. Standard capacity release after verified completion.

## 4. Candidate Mobility Triggers

Migration may be considered when there is evidence of one or more of the following:

- sustained workload beyond a Standard shared-cell envelope;
- persistent CPU / memory / database / queue / storage pressure attributable to legitimate tenant workload;
- sustained transaction volume materially above Standard package economics;
- large or rapidly growing database / attachment footprint;
- high integration / API / background processing intensity;
- stronger isolation, SLA, compliance or performance requirements;
- customer-requested dedicated environment;
- measured economic crossover where reserved Enterprise capacity is more efficient than sustained Standard overage.

Temporary legitimate bursts alone must not automatically force Enterprise.
SMEsPlus software inefficiency, bad SQL, missing indexes, memory leaks or architectural defects must never be treated as customer-caused Enterprise justification.

## 5. Mobility Control Flow — Candidate

`Observe -> Recommend/Request -> Commercial Review -> Customer Approval -> Prepaid/Reserved Capacity Confirmed -> Provision Enterprise Destination -> Preflight -> Rehearsal/Backup -> Data & File Synchronization -> Final Delta -> Cutover -> Reconciliation -> Observe -> Release Standard Capacity`

Exact mechanism is intentionally NOT frozen.

## 6. Migration Integrity Contract

The following must remain continuous and provable across movement:

- Tenant ID / canonical tenant identity
- Company identities and legal/accounting boundaries
- Users, roles and access controls
- Business transactions and states
- Accounting postings and reconciliations
- Tax evidence
- Audit logs
- Document links and attachments
- Canonical configuration
- Approved extensions and extension contracts
- Integration endpoints / credentials subject to secure rotation policy
- Usage history
- Wallet / prepaid credit balance
- Billing history and charge evidence
- Reporting lineage
- Knowledge-of-Truth provenance where applicable

Migration must not create duplicate business truth.

## 7. Commercial / Wallet Continuity

Moving to Enterprise must not reset or erase financial history.

At minimum:

- existing prepaid wallet balance remains traceable;
- unused prepaid service credit must be carried forward, reconciled or explicitly settled under an approved commercial rule;
- Standard usage up to the cutover remains separately auditable;
- Enterprise reserved-capacity billing starts from a clearly defined effective point;
- no double charging across the cutover boundary;
- additional Enterprise capacity must be prepaid or otherwise secured before activation;
- `30-Day Notice != 30-Day Credit` remains in force;
- `No Unsecured Postpaid Overage` remains in force;
- `No Evidence = No Chargeable Overage` remains in force;
- `No Surprise Billing` remains in force.

## 8. Data Mobility Principle

The migration design must support moving from shared resource pools to a dedicated Enterprise resource boundary without changing application-level business semantics.

Possible technical mechanisms may include replication, logical copy, snapshot/restore, change-data capture, object-storage synchronization, routing cutover, or other methods.

No mechanism is frozen at this stage.

## 9. Mandatory Gates — Candidate

G1 — Mobility Candidate Evidence

G2 — Customer / Commercial Approval

G3 — Enterprise Capacity Reserved and Payment/Secured Credit Confirmed

G4 — Technical Readiness / Compatibility Verification

G5 — Backup / Rehearsal / Rollback Readiness

G6 — Migration / Synchronization Complete

G7 — Final Delta and Cutover

G8 — Reconciliation / Integrity Proof

G9 — Observation / Stability Verification

G10 — Standard Capacity Release

No gate may be skipped without an approved material exception.

## 10. Evidence Required Before Pricing Freeze

WP-09 must produce evidence covering at least:

- Standard-to-Enterprise data movement feasibility;
- database-size migration scenarios;
- attachment/object-storage migration scenarios;
- large tenant cutover duration assumptions;
- downtime / near-zero-downtime alternatives;
- rollback feasibility;
- wallet and billing reconciliation;
- audit/log continuity;
- integration continuity;
- cost of temporary dual capacity during migration;
- operational complexity and observability requirements.

## 11. Updated Pre-Pricing Sequence

`WP-01 -> WP-02 -> WP-03 -> WP-04 -> WP-05 -> WP-06 -> WP-08 -> WP-07 -> WP-09 -> PRE-PRICING EVIDENCE GATE -> COMMERCIAL SIMULATION -> BOSS PRICING DECISION`

WP-09 may be researched in parallel with WP-06/WP-08 where evidence dependencies permit, but final mobility disposition must be complete before Pricing Freeze.

## 12. Not Frozen

The following remain open until evidence exists:

- migration downtime target;
- exact replication technology;
- PostgreSQL topology;
- object-storage topology;
- container / VM / Kubernetes mechanism;
- migration throughput assumptions;
- cutover thresholds;
- automatic vs human-approved mobility recommendation rules;
- commercial crossover point;
- package sizes / GB limits / transaction weights;
- final Enterprise capacity packages and prices.

## 13. Architectural Principle

> **A tenant may move from shared capacity to dedicated capacity without changing who the tenant is or what its business facts mean.**

> **Standard to Enterprise is a capacity and isolation move — not a product fork, data reset, or business-semantic migration.**

## 14. Governance

- No Evidence = No Progress.
- Never Skip Gate.
- Boss is the sole Final Approver for this architecture decision/freeze.
- No production migration execution is authorized by this record.
