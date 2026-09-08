# [SMEPLUS-26-09-08-ACC-PHASE-SA-NEWSESSION-001]
# ACCOUNT PHASE SA — NEW SESSION MASTER PROMPT

Repository:
`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:
`architecture/account-phase-sa-new-session-2026-09-08-001`

Session scope:
**PHASE SA ONLY**

Parent Phase SA kickoff commit:
`13d11f20157f694a67ff7bbd53bbd001dc071710`

Read first:
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/PHASE_SA/NEW_SESSION_2026_09_08/00_PHASE_SA_CONTEXT_AND_LINEAGE.md`

Then execute this prompt completely.

---

## 1. MISSION

Continue Account **Phase SA only** from the Boss-authorized Phase SA kickoff.

Carry forward the complete necessary history, Boss-approved rulings, Clean-room constitution, SMEsPlus Nature DNA, SMT first-line detection responsibility and controlled Very Deep Research re-entry rule.

Do NOT restart Phase S.
Do NOT restart Account research from L1.
Do NOT discard prior evidence.
Do NOT mechanically reproduce v18/v19/vendor architecture.

Your job is to transform accumulated learning into an independent SMEsPlus Accounting architecture.

The operative question is NOT:

> How does the reference system implement this?

The operative questions are:

> What business/accounting problem must be solved?
>
> What semantics, controls, risks and edge cases have we learned?
>
> What architecture should SMEsPlus choose independently today?
>
> What should SMEsPlus do better or differently?

---

## 2. ABSOLUTE CLEAN-ROOM RULES

1. SOURCE IS EVIDENCE, NOT DESIGN.
2. LEARN BEHAVIOR, NOT STRUCTURE.
3. TRANSFER BUSINESS MEANING, NOT APPLICATION ARCHITECTURE.
4. EVERY SMEPLUS DESIGN MUST HAVE AN INDEPENDENT CLEAN-ROOM RATIONALE.
5. THE TARGET IS NOT REFERENCE-SYSTEM PARITY; THE TARGET IS A BETTER SMEPLUS SYSTEM.
6. Similarity in common ERP/accounting terms is allowed; dependency on vendor architecture is not.
7. Vendor schema, ORM, workflow, state model, menu structure and UI are never inherited by default.
8. Every SMEsPlus-owned persistent business table MUST use `smeplus_*`.
9. Every material design must demonstrate SMEsPlus Nature DNA.
10. No Evidence = No Progress.
11. Never Skip Gate.
12. No repeated Boss question without material delta.

---

## 3. BOSS-APPROVED RULES — DO NOT RE-ASK

### BD-ACC-01 — Accounting Event Identity

- Source Module owns the Business Fact.
- Accounting Core owns canonical immutable Accounting Event Identity.
- Posting Engine owns Ledger Posting.
- Accounting Event Identity is distinct from Source Document Number, Journal Number and Reconciliation Matching Number.
- Same-event retry must be idempotent.
- Reversal creates a new event referencing the original.
- Event identity and posting are Tenant + Company bounded.

### BD-ACC-02 — Company-scoped Tax

- SMEsPlus does not perform Consolidation Accounting for statutory tax filing.
- VAT, WHT, tax registers and statutory filing are Company-scoped.
- Multi-company informational/management reporting may aggregate without cross-company statutory posting, offsetting or filing.

### BD-ACC-03A — Inventory Valuation Recognition

- `Periodic | Perpetual`
- Product Category only
- No Product override

### BD-ACC-03B — Costing Method

- `Standard | Average | FIFO`
- Product Category only
- No Product override

### Product Accounting Override Boundary

At Product level only:

- Income Account
- Expense Account
- Price Difference Account

Blank value inherits from Product Category.

### Production History / Data-Correction Principle

General-purpose transaction deletion is not a Production Accounting capability.
Use controlled reversal, cancellation, correction, adjustment and auditable lineage.
Dev/Test/UAT reset tools are environment tools, not production business functions.

---

## 4. SMT FIRST-LINE DETECTION RULE

Boss must never be the first detector of an obvious functional, Clean-room, evidence, architecture, control, audit, SaaS-boundary or source-copying defect.

For each material function, relevant SMT teams must execute:

`SMT FUNCTION OWNER REVIEW`
-> `SMT CLEAN-ROOM CHALLENGE`
-> `SMT CROSS-DOMAIN / CONTROL CHECK`
-> `SMT MATERIALITY CLASSIFICATION`
-> `TARGETED VERY DEEP RESEARCH IF REQUIRED`
-> `SMT RE-CHALLENGE`
-> `BOSS PACK ONLY IF BOSS AUTHORITY IS ACTUALLY REQUIRED`

Do not send raw uncertainty to Boss.

A Boss pack must contain:

- exact issue;
- evidence;
- why SMT cannot resolve it under approved authority;
- alternatives;
- impact/risk;
- SMT recommendation;
- challenge/dissent result;
- exact Boss decision requested.

If this pack cannot be produced, the item is NOT READY FOR BOSS.

---

## 5. TARGETED VERY DEEP RESEARCH RE-ENTRY

Phase S is conditionally closed, not permanently sealed against new learning.

If Phase SA reveals a material function that is:

- unclear;
- functionally incomplete;
- insufficiently evidenced;
- internally contradictory;
- not demonstrably Clean Room;
- too dependent on a reference implementation;
- missing important control/audit semantics;
- unable to show SMEsPlus-specific rationale;

then SMT must route that function to **Targeted Very Deep Research** before Boss sees the defect.

Mandatory re-entry rules:

- freeze only the affected function;
- preserve prior evidence and Boss rulings;
- reopen only the material unknown;
- do not reset unrelated functions;
- research deeply enough to remove or defensibly bound uncertainty;
- re-synthesize as SMEsPlus;
- re-challenge under Clean Room 100%;
- return to Phase SA when ready.

Boss may independently order Very Deep Research at any time.

---

## 6. PHASE SA EXECUTION ORDER

Execute sequentially.
Do not jump to physical schema, implementation or UI.

### SA-00 — Evidence-to-Semantic Intake

For every material accounting function/domain:

- identify relevant learned facts;
- classify each as business semantic, control, risk, edge case, user need, integration need, version-specific behavior, or vendor-only implementation detail;
- explicitly prevent vendor-only implementation details from becoming SMEsPlus requirements by default;
- identify contradictions and bounded unknowns;
- determine whether Targeted Very Deep Research is needed.

Required output:
`SA00_EVIDENCE_TO_SEMANTIC_REGISTER.md`

### SA-01 — SMEsPlus Accounting Capability Map

Define SMEsPlus-owned capabilities independently from source menus/modules.
At minimum cover:

- Accounting Event Core;
- General Ledger / Journal / Posting;
- Accounts Receivable;
- Accounts Payable;
- Tax / VAT / WHT;
- Bank / Cash / Reconciliation;
- Inventory Accounting / Valuation / COGS;
- Assets / Depreciation;
- Analytic / Dimensions / Cost control;
- Period Close / Year Close;
- Reversal / Correction / Adjustment;
- Audit / Traceability;
- Inter-module accounting interfaces.

Required output:
`SA01_SMEPLUS_ACCOUNTING_CAPABILITY_MAP.md`

### SA-02 — Canonical Accounting Event Model

Define the conceptual event architecture around Boss-approved BD-ACC-01.
Do not yet lock physical technology or IDs unless required by architecture.

Required output:
`SA02_CANONICAL_ACCOUNTING_EVENT_MODEL.md`

### SA-03 — Ownership & Boundary Matrix

For each capability/object, define:

- Business owner;
- Accounting owner;
- Posting owner;
- Tenant boundary;
- Company boundary;
- approval/control owner;
- audit owner;
- authoritative source of truth.

Required output:
`SA03_OWNERSHIP_AND_BOUNDARY_MATRIX.md`

### SA-04 — Alternative Architecture Challenge

For each material design choice:

- provide at least two defensible alternatives where meaningful;
- state advantages/disadvantages;
- state reference-system influence if any;
- state why the chosen option is independently justified for SMEsPlus;
- trigger Very Deep Research where alternatives cannot yet be evaluated safely.

Required output:
`SA04_ALTERNATIVE_ARCHITECTURE_CHALLENGE.md`

### SA-05 — Conceptual Information Model

Only after SA-00..SA-04 are stable, define conceptual SMEsPlus business objects and relationships.

Rules:

- no vendor table-copying;
- no vendor ORM-copying;
- conceptual object names must reflect SMEsPlus semantics;
- future physical persistent business tables use `smeplus_*`.

Required output:
`SA05_CONCEPTUAL_INFORMATION_MODEL.md`

### SA-06 — Clean-Room & Nature DNA Gate

Every material function must answer:

1. What did we learn?
2. What did we deliberately not inherit?
3. What alternatives were considered?
4. Why is this SMEsPlus-specific?
5. What does SMEsPlus do better or differently?
6. Are identity/ownership/lifecycle/control/audit/Tenant/Company boundaries clear?
7. Is additional Very Deep Research required?

Any material failure = NOT READY.

Required output:
`SA06_CLEAN_ROOM_NATURE_DNA_GATE.md`

### SA-07 — Cross-Domain Interface Contract

Define conceptual contracts between Accounting and source domains without moving execution ownership into Accounting improperly.

Cover at minimum Sales, Purchase, Inventory, Manufacturing, Expense, Asset, Payment/Bank and Tax interactions.

Required output:
`SA07_CROSS_DOMAIN_INTERFACE_CONTRACT.md`

### SA-08 — SMT Independent Challenge

SMT must attempt to falsify the design before Boss sees it.

Challenge at minimum:

- source-copying;
- missing functionality;
- weak control;
- audit gaps;
- idempotency/reversal gaps;
- Tenant/Company leakage;
- policy ownership ambiguity;
- over-complexity;
- missing SMEsPlus advantage;
- unsupported assumptions.

Required output:
`SA08_SMT_INDEPENDENT_CHALLENGE.md`

### SA-09 — Boss Decision Pack

Create only for genuine Boss-authority decisions that remain after SMT analysis and re-challenge.

If none remain, explicitly state:
`NO NEW BOSS DECISION REQUIRED AT THIS CHECKPOINT`.

Required output:
`SA09_BOSS_DECISION_PACK.md`

---

## 7. PROHIBITIONS

Do NOT:

- reopen all Phase S research;
- reset Account to L1;
- treat v18/v19/vendor architecture as the target;
- copy vendor schema/ORM/workflow/state/UI and rename it SMEsPlus;
- force a physical schema before conceptual architecture is stable;
- ask Boss questions that SMT should resolve;
- allow Boss to become first-line QA;
- hide unknowns;
- mark a function clean if required Very Deep Research has not been performed;
- implement application code;
- merge/release/deploy production;
- bypass Boss Final Approval.

---

## 8. EXECUTION BEHAVIOR

Proceed autonomously through Phase SA within the authorized scope.

Do not stop for routine choices that are already governed by Boss-approved rules.

At each material function:

- classify evidence;
- synthesize independently;
- challenge the design;
- trigger Targeted Very Deep Research when required;
- preserve traceability to learned facts without inheriting vendor architecture.

Escalate only genuine Boss-authority decisions after SMT completes its responsibility.

---

## 9. CURRENT START POINT

Begin now at:

`SA-00 — Evidence-to-Semantic Intake`

First required artifact:

`SA00_EVIDENCE_TO_SEMANTIC_REGISTER.md`

Do not begin SA-01 until SA-00 is evidence-complete and SMT-ready.

---

## 10. TERMINAL TARGET FOR THIS NEW SESSION

Target:

`CP-SA-00 — PHASE SA CLEAN-ROOM SYNTHESIS BASELINE READY FOR SMT CHALLENGE`

If a material function requires deeper knowledge before this checkpoint, record:

`TARGETED VERY DEEP RESEARCH REQUIRED — <FUNCTION>`

and route only that function through the controlled re-entry protocol.

Boss remains the sole Final Approver.