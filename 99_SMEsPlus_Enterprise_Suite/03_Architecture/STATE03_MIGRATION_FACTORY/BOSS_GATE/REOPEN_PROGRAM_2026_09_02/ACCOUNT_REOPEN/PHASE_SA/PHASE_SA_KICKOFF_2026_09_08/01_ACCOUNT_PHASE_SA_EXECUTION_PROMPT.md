# ACCOUNT PHASE SA — CLEAN-ROOM SYNTHESIS / ARCHITECTURE EXECUTION PROMPT

Session: `[SMEPLUS-26-09-08-ACC-PHASE-SA-KICKOFF-001]`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `architecture/account-phase-sa-kickoff-2026-09-08-001`  
Parent authority: `79d7027818928a1ab94cbd7c5f9b2f37233caacd`

## Mission

Begin Account Phase SA from the conditionally closed Phase S evidence lineage. Convert accumulated learning into an independent SMEsPlus accounting architecture. Do not copy, translate, rename or mechanically reproduce v18/v19/vendor schema, ORM, workflow, menu, state model or UI.

The job is to understand what the business/accounting problem actually is, preserve the learned semantics and controls, compare alternatives, then design the SMEsPlus solution from first principles.

## Constitutional rules

1. **SOURCE IS EVIDENCE, NOT DESIGN.**
2. **LEARN BEHAVIOR, NOT STRUCTURE.**
3. **TRANSFER BUSINESS MEANING, NOT APPLICATION ARCHITECTURE.**
4. **EVERY SMEPLUS DESIGN MUST HAVE AN INDEPENDENT CLEAN-ROOM RATIONALE.**
5. **THE TARGET IS NOT REFERENCE-SYSTEM PARITY; THE TARGET IS A BETTER SMEPLUS SYSTEM.**
6. Similarity is allowed where common ERP/accounting semantics justify it; dependency on vendor architecture is not.
7. All SMEsPlus-owned persistent business tables MUST use `smeplus_*`.
8. Boss-approved decisions are frozen unless a material delta is proven.
9. SMT is first-line detection. Boss must not be the first person to discover an obvious defect, ambiguity or source-copying problem.
10. No Evidence = No Progress. Never Skip Gate. No repeated Boss question without material delta.

## Boss-approved invariants to carry forward

### Accounting event ownership

- Source Module owns the Business Fact.
- Accounting Core owns the canonical immutable Accounting Event Identity.
- Posting Engine owns Ledger Posting.
- Accounting Event Identity is not Source Document Number, Journal Number or Reconciliation Matching Number.
- Same-event retry must be idempotent.
- Reversal creates a new event referencing the original.
- Event identity and posting must be Tenant + Company bounded.

### Tax boundary

- No Consolidation Accounting tax filing.
- VAT, WHT, tax registers and statutory filing are Company-scoped.
- Multi-company informational reporting may aggregate but cannot create cross-company statutory posting, offsetting or filing.

### Inventory/accounting policy

- Inventory Valuation Recognition: `Periodic | Perpetual` at Product Category only.
- Costing Method: `Standard | Average | FIFO` at Product Category only.
- Product-level accounting override surface: `Income Account`, `Expense Account`, `Price Difference Account` only; blank inherits Product Category.

### Audit/data correction principle

Production business history is not cleaned by general-purpose transaction deletion. Use controlled reversal, cancellation, correction, adjustment and audit lineage. Dev/Test/UAT reset tooling is environment tooling, not a production accounting capability.

## Phase SA execution sequence

Execute the following in order. Do not jump directly to physical schema or UI.

### SA-00 — Evidence-to-Semantic Intake

For every material accounting function/domain:

- identify the source-learning facts that remain relevant;
- mark each fact as business-semantic, control, risk, edge case, user need, integration need, version-specific behavior or vendor-only implementation detail;
- explicitly exclude vendor-only schema/ORM/state/workflow artifacts from automatic inheritance;
- identify known contradictions and bounded unknowns;
- identify whether Targeted Very Deep Research is required before synthesis.

Output: `SA00_EVIDENCE_TO_SEMANTIC_REGISTER.md`

### SA-01 — SMEsPlus Accounting Capability Map

Define SMEsPlus-owned capabilities independently from source menus/modules. At minimum cover:

- General Ledger / Journal / Posting;
- Accounting Event Core;
- Accounts Receivable;
- Accounts Payable;
- Tax/VAT/WHT;
- Bank/Cash and reconciliation;
- Inventory accounting / COGS / valuation;
- Manufacturing/WIP accounting interfaces;
- Assets / depreciation / production allocation interfaces;
- Expense/employee financial interfaces;
- Period/Month/Year close;
- Reversal/correction/adjustment;
- Analytic/dimensional accounting;
- Financial statements/reporting semantics;
- Audit trail / provenance;
- Multi-tenant / multi-company boundaries.

Output: `SA01_SMEPLUS_ACCOUNTING_CAPABILITY_MAP.md`

### SA-02 — Canonical Business Event & Accounting Event Model

Design the conceptual event model before tables.

For each event type define:

- business fact;
- source ownership;
- accounting consequence;
- accounting event identity;
- company/tenant boundary;
- idempotency key semantics;
- posting eligibility;
- reversal/correction causality;
- audit/provenance requirement;
- downstream reconciliation/reporting effects.

Output: `SA02_CANONICAL_ACCOUNTING_EVENT_MODEL.md`

### SA-03 — Ownership & Boundary Matrix

Define who owns what. At minimum distinguish:

- Source Module execution;
- Approval Engine approval only;
- Accounting Core event semantics;
- Posting Engine ledger posting;
- Tax Engine statutory calculation/reporting;
- Reconciliation/settlement logic;
- Reporting/query layers;
- Audit Trail;
- Tenant/Company access control.

Output: `SA03_ACCOUNTING_OWNERSHIP_BOUNDARY_MATRIX.md`

### SA-04 — Alternative Architecture Challenge

For every material capability, document at least two defensible implementation-independent architecture alternatives where material choice exists. Reject options that merely mirror the reference system.

Each decision must state:

- what was learned;
- what is deliberately not inherited;
- alternatives considered;
- selected SMEsPlus direction;
- why it is better/safer/simpler/more auditable/more SaaS-native;
- unresolved risks;
- whether Very Deep Research is required.

Output: `SA04_ALTERNATIVE_ARCHITECTURE_CHALLENGE.md`

### SA-05 — Conceptual Information Model

Only after SA-00..SA-04 are coherent, derive the conceptual information model.

Rules:

- start from SMEsPlus concepts, not vendor tables;
- every persistent SMEsPlus business table uses `smeplus_*`;
- define identity, ownership, lifecycle, immutability and retention semantics;
- do not lock physical DB types/indexes prematurely;
- do not reproduce vendor ORM relationships by default;
- identify event/state/history records explicitly.

Output: `SA05_SMEPLUS_ACCOUNTING_CONCEPTUAL_INFORMATION_MODEL.md`

### SA-06 — Clean-Room & Nature DNA Gate

For every material function answer:

1. What did we learn?
2. What did we deliberately NOT inherit?
3. What alternatives did we consider?
4. What is the SMEsPlus-specific rationale?
5. What are the Tenant/Company/control/audit boundaries?
6. What does SMEsPlus do better or differently?
7. Is any material uncertainty still present?

Any function failing this gate is NOT READY and must return to SMT triage and, where needed, targeted Very Deep Research.

Output: `SA06_CLEAN_ROOM_NATURE_DNA_GATE.md`

### SA-07 — Cross-Domain Interface Contract

Define accounting-facing contracts with Sales, Purchase, Inventory, Manufacturing, Expense, Assets and other upstream/downstream domains using business events and capability ownership, not copied vendor calls/models.

Output: `SA07_ACCOUNTING_CROSS_DOMAIN_INTERFACE_CONTRACT.md`

### SA-08 — SMT Independent Challenge

Relevant SMT teams must independently review and attempt to break SA-00..SA-07 for:

- source-copying contamination;
- missing business semantics;
- hidden vendor assumptions;
- incomplete accounting treatment;
- SaaS tenant/company leakage;
- audit/control weakness;
- reversal/correction gaps;
- reconciliation ambiguity;
- cross-module contradiction;
- unsupported novelty;
- excessive complexity;
- places where Very Deep Research is needed.

Output: `SA08_SMT_INDEPENDENT_CHALLENGE.md`

### SA-09 — Boss Decision Pack

Only genuine Boss-only decisions may appear here. No raw questions. Each item must include evidence, alternatives, impact/risk, SMT recommendation, dissent/challenge result and exact decision requested.

If SMT can resolve an item under existing constitutional authority, do not escalate it.

Output: `SA09_BOSS_DECISION_PACK.md`

## Very Deep Research re-entry protocol

If SMT discovers a material function that is unclear, incomplete, weakly evidenced, vendor-dependent or not Clean Room:

1. mark the function `SA-HOLD-VDR`;
2. freeze only the affected dependency boundary;
3. preserve prior evidence and Boss decisions;
4. define the exact unknown / hypothesis / evidence gap;
5. execute Targeted Very Deep Research;
6. publish evidence and contradiction results;
7. re-synthesize independently;
8. re-run SA-06 and SA-08 for the affected area;
9. resume the main SA stream when cleared.

Boss retains the right to order Very Deep Research at any time. Normal quality control must not depend on Boss discovering the problem first.

## Stop conditions

Stop and hold the affected function if:

- evidence is materially insufficient;
- architecture is being inferred directly from vendor internals;
- a Boss-approved rule is contradicted;
- Tenant/Company isolation is uncertain;
- accounting event ownership or posting causality is ambiguous;
- audit/reversal/correction behavior is not defensible;
- SMT challenge finds a material gap;
- Clean Room / Nature DNA gate fails.

Do not stop unrelated functions unless dependency impact requires it.

## Current authorization boundary

This prompt authorizes Phase SA synthesis and architecture work only.

It does NOT authorize application coding, schema migration execution, production implementation, merge, release or deployment.

Terminal target for this kickoff:

`CP-SA-00 — PHASE SA CLEAN-ROOM SYNTHESIS BASELINE READY FOR SMT CHALLENGE`

Boss remains the sole Final Approver.