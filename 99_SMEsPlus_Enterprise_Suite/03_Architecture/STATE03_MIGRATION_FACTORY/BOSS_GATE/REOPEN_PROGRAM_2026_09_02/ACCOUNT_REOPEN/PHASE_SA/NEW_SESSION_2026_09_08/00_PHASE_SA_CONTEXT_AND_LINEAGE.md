# [SMEPLUS-26-09-08-ACC-PHASE-SA-NEWSESSION-001]
# ACCOUNT PHASE SA — NEW SESSION CONTEXT AND LINEAGE

Project: SMEsPlus ENTERPRISE SUITE  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `architecture/account-phase-sa-new-session-2026-09-08-001`  
Session scope: **PHASE SA ONLY**  
Boss: Sole Final Approver

## 1. Why this New Session exists

This New Session continues Account **Phase SA only** with complete necessary lineage carried forward so that the new execution context does not lose the decisions, Clean-room rules, control boundaries, or current checkpoint.

It is NOT a Phase S restart, NOT a new Account research programme, and NOT authorization to reopen completed learning globally.

## 2. Frozen upstream lineage

The following prior records are authoritative history and must be treated as frozen inputs unless a material delta is proven:

- Phase S final independent gate evidence commit: `be5d1595f4b96776c47399501a405b40297f3e34`
- Boss rulings / Phase S conditional closure / Phase SA entry commit: `79d7027818928a1ab94cbd7c5f9b2f37233caacd`
- Phase SA kickoff execution-frame commit: `13d11f20157f694a67ff7bbd53bbd001dc071710`

Current upstream state:

`CP-SC-15 — PHASE S CONDITIONALLY CLOSED / PHASE SA ENTRY AUTHORIZED`

Current Phase SA state:

`CP-SA-KICKOFF — PHASE SA START AUTHORIZED AND EXECUTION FRAME PUBLISHED`

## 3. Phase S closure meaning

Phase S is **conditionally closed**.

Phase S evidence and learning remain preserved. If, during Phase SA, a specific function is materially unclear, incomplete, insufficiently evidenced, not Clean-room, or too dependent on a reference implementation, that function may be routed to **Targeted Very Deep Research**.

Rules for re-entry:

- reopen only the affected material unknown;
- preserve previous evidence;
- preserve Boss rulings unless a material delta is proven;
- do not reset unrelated functions;
- do not restart Account from L1 by default;
- return the function to Phase SA only after re-synthesis and re-challenge.

Boss retains the right to order Very Deep Research at any time, but normal quality control must not depend on Boss detecting the problem first.

## 4. SMT first-line responsibility

**Boss must never be the first detector.**

Relevant SMT functional/domain teams must identify, challenge and contain before Boss review:

- functional ambiguity;
- incomplete business semantics;
- insufficient evidence;
- source-copying or reference-system dependency;
- weak Clean-room rationale;
- missing SMEsPlus Nature DNA;
- Tenant/Company boundary defects;
- accounting ownership/event/posting ambiguity;
- control/audit/reversal/correction weakness;
- cross-domain contradictions;
- hidden dependencies;
- cases requiring Targeted Very Deep Research.

Boss should receive only a genuine Boss-authority decision pack after SMT has completed analysis, alternatives, risk assessment and recommendation.

## 5. Boss-approved accounting rulings

The following decisions are CLOSED and must not be re-asked without material delta.

### BD-ACC-01 — Accounting Event Identity

- Source Module owns the Business Fact.
- Accounting Core owns canonical immutable Accounting Event Identity.
- Posting Engine owns Ledger Posting.
- Accounting Event Identity is distinct from Source Document Number, Journal Number and Reconciliation Matching Number.
- Same-event retry must be idempotent.
- Reversal creates a new event referencing the original event.
- Event identity and posting are Tenant + Company bounded.

### BD-ACC-02 — Company-scoped tax

- SMEsPlus does not perform Consolidation Accounting for statutory tax filing.
- VAT, WHT, tax registers and statutory filing are Company-scoped.
- Multi-company informational/management reporting may aggregate without creating cross-company statutory tax posting, offsetting or filing.

### BD-ACC-03A — Inventory Valuation Recognition

- Values: `Periodic | Perpetual`.
- Policy authority: Product Category only.
- Product must not override this policy.

### BD-ACC-03B — Costing Method

- Values: `Standard | Average | FIFO`.
- Policy authority: Product Category only.
- Product must not override this policy.

### Product Accounting override boundary

Product-level Accounting may contain only:

- Income Account;
- Expense Account;
- Price Difference Account.

Blank value inherits from Product Category.

## 6. SMEsPlus Clean Room 100% constitution

Reference systems, including v18/v19 and any other ERP, are:

`REFERENCE / LEARNING / EXPERIMENT / BENCHMARK ONLY`

They are NOT:

- Design Authority;
- Schema Authority;
- ORM Authority;
- Workflow Authority;
- State-model Authority;
- UI Authority.

Canonical rule:

> SOURCE IS EVIDENCE, NOT DESIGN.
>
> LEARN BEHAVIOR, NOT STRUCTURE.
>
> TRANSFER BUSINESS MEANING, NOT APPLICATION ARCHITECTURE.
>
> EVERY SMEPLUS DESIGN MUST HAVE AN INDEPENDENT CLEAN-ROOM RATIONALE.
>
> THE TARGET IS NOT REFERENCE-SYSTEM PARITY; THE TARGET IS A BETTER SMEPLUS SYSTEM.

Common ERP/accounting terminology may be reused where semantically correct. Similarity is allowed; dependency is not.

## 7. SMEsPlus Nature DNA

Every material Phase SA design must demonstrate SMEsPlus-specific:

- identity;
- ownership;
- lifecycle;
- control;
- audit lineage;
- Tenant/Company boundary;
- event semantics;
- cross-domain contract;
- explicit reason for choosing the design.

Every material function must answer:

1. What did we learn?
2. What did we deliberately NOT inherit?
3. What alternatives were considered?
4. Why is the selected design SMEsPlus-specific?
5. What does SMEsPlus do better or differently?
6. Is further Very Deep Research required?

## 8. Database namespace constitution

All SMEsPlus-owned persistent business tables MUST use the namespace:

`smeplus_*`

This is an ownership and architecture boundary, not merely a naming preference.

## 9. Production correction principle

General-purpose transaction-deletion utilities learned from reference/test environments are not Production Accounting capabilities for SMEsPlus.

Production history must be controlled through appropriate business/accounting mechanisms such as reversal, cancellation, correction, adjustment, controlled reconciliation/unreconciliation and auditable lineage.

Dev/Test/UAT reset tooling is environment tooling and must not be treated as a production business function.

## 10. Phase SA execution frame

Phase SA sequence remains:

- SA-00 — Evidence-to-Semantic Intake
- SA-01 — SMEsPlus Accounting Capability Map
- SA-02 — Canonical Accounting Event Model
- SA-03 — Ownership & Boundary Matrix
- SA-04 — Alternative Architecture Challenge
- SA-05 — Conceptual Information Model
- SA-06 — Clean-Room & Nature DNA Gate
- SA-07 — Cross-Domain Interface Contract
- SA-08 — SMT Independent Challenge
- SA-09 — Boss Decision Pack, only when genuine Boss authority is required

Do not jump directly to physical schema, implementation or UI.

## 11. Current executable target

Start this New Session at:

`SA-00 — Evidence-to-Semantic Intake`

Required initial output:

`SA00_EVIDENCE_TO_SEMANTIC_REGISTER.md`

## 12. Authority boundary

Authorized in this New Session:

- Phase SA synthesis;
- architecture;
- conceptual/domain design;
- alternatives analysis;
- Clean-room challenge;
- interface/boundary definition;
- conceptual data-model design;
- targeted Very Deep Research re-entry when triggered by SMT controls.

NOT authorized:

- reopening all of Phase S;
- global research reset;
- production implementation;
- merge/release;
- production deployment;
- silent adoption of vendor schema/workflow/ORM/UI;
- bypassing Boss Final Approval gates.

No Evidence = No Progress.  
Never Skip Gate.  
No repeated Boss question without material delta.