# [SMEPLUS-26-09-08-ACC-PHASE-SA-KICKOFF-001]
# ACCOUNT PHASE SA — CLEAN-ROOM SYNTHESIS / ARCHITECTURE KICKOFF

Project: SMEsPlus ENTERPRISE SUITE  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `architecture/account-phase-sa-kickoff-2026-09-08-001`  
Parent control commit: `79d7027818928a1ab94cbd7c5f9b2f37233caacd`  
Boss: Sole Final Approver

## Authority

Boss explicitly authorized the start of Account Phase SA on 2026-09-08.

Phase S remains **CONDITIONALLY CLOSED**. Phase SA may proceed with architecture, synthesis and design. Any materially unclear, incomplete, weakly evidenced, source-dependent or non-clean function must be detected first by the relevant SMT team and routed to targeted Very Deep Research before Boss review.

## Phase SA purpose

Phase SA is not a translation of Source Learning into SMEsPlus structures. It is the controlled synthesis stage where accumulated learning is converted into independent SMEsPlus architecture.

Canonical direction:

- Source is evidence, not design authority.
- Learn behavior and business meaning; do not inherit vendor structure by default.
- Common ERP/accounting terminology may be reused where semantically correct.
- Similarity is allowed; dependency is not.
- SMEsPlus must have its own Nature DNA.
- Every SMEsPlus-owned persistent business table uses the `smeplus_*` namespace.
- Every material design must have an independent clean-room rationale.
- SMEsPlus target is not reference-system parity; it is a better SMEsPlus system.

## Boss-approved decisions carried into Phase SA

- `BD-ACC-01` — Accounting Core owns canonical immutable Accounting Event Identity; it is distinct from source-document number, journal number and reconciliation matching number. Source Module owns the Business Fact; Posting Engine owns Ledger Posting. Retry is idempotent; reversal is a new event referencing the original; event identity is Tenant + Company bounded.
- `BD-ACC-02` — No Consolidation Accounting tax filing. VAT/WHT/tax registers/statutory filing are Company-scoped. Multi-company informational aggregation is allowed but must not create cross-company statutory tax posting, offset or filing.
- `BD-ACC-03A` — Inventory Valuation Recognition = `Periodic | Perpetual`; policy authority is Product Category only.
- `BD-ACC-03B` — Costing Method = `Standard | Average | FIFO`; policy authority is Product Category only.
- Product > Accounting permits only `Income Account`, `Expense Account`, `Price Difference Account`; blank Product account inherits Product Category.
- Production ERP must not rely on general-purpose transaction-deletion utilities as a business capability; corrections use controlled reverse/cancel/correction/adjustment/audit mechanisms.

## SMT first-line rule

Boss must never be the first detector. SMT must detect, challenge, classify and contain functional ambiguity, evidence weakness, source-copying, Clean-room defects, SaaS-boundary defects, accounting/control/audit weaknesses and hidden cross-domain contradictions before Boss review.

A raw uncertainty is not a Boss question. Boss escalation requires a prepared decision pack with evidence, alternatives, impact/risk, SMT recommendation and the exact Boss-only decision required.

## Very Deep Research re-entry

Targeted Very Deep Research is an authorized control path, not a failure and not a reset.

Trigger it when a function is materially unclear, incomplete, insufficiently evidenced, not truly clean-room, or cannot explain what SMEsPlus does better/differently.

Re-entry rules:

- freeze only the affected function/dependency boundary;
- preserve prior learning and Boss rulings;
- reopen only the material unknown;
- research until the uncertainty is resolved or defensibly bounded;
- re-synthesize into SMEsPlus independently;
- SMT re-challenges before returning the function to Phase SA;
- do not reset unrelated Account work.

## Authority boundary

AUTHORIZED: architecture, synthesis, conceptual/domain design, alternatives analysis, Clean-room challenge, data-model design, boundary/interface definition, targeted Very Deep Research.

NOT AUTHORIZED: implementation, code merge, release, production deployment, silent reuse of vendor schema/ORM/workflow/state model, bypass of gates.

No Evidence = No Progress. Never Skip Gate. No repeated question without material delta.