# [SMEPLUS-26-08-31-MIG-A-INV-BB-R01]
# Inventory Core Backbone Evidence Reconciliation / TEAM A / DELTA-FIRST / L99.99

## SINGLE END-TO-END SELF-STARTING TEAM A PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Execution Team: `TEAM A — Source Learning / Business Evidence Extraction`  
Workstream: `Inventory Core Backbone Evidence Reconciliation`  
Mode: `READ ONLY / EVIDENCE-FIRST / DELTA-FIRST / CLEAN-ROOM`  
Control Level: `/L99.99`  
Boss: `Sole Final Approver`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Jira: `ERPPLUS-137`  
Roadmap Commit: `4c3e4e8fbddb6a4231ea7704dba86f0315302072`  
Pre-Prompt Readiness Commit: `9d997ff34605ff98e9567502d6be54a77e81265f`  
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`

This is the only execution instruction for this Team A session.

`ONE SESSION = ONE END-TO-END PROMPT.`

Execute continuously. Do not ask Boss for routine START / CONTINUE / NEXT / COMMIT / PUSH instructions. Ask Boss only if a true stop condition is reached.

---

## 1. Boss Directive

Boss directs STATE03 to follow the actual ERP operating backbone so Accounting and Inventory do not become downstream bottlenecks.

Controlling direction:

`INVENTORY / STORE -> ACCOUNTING CORE`

Interpretation for this Team A session:

- Accounting is the enterprise-wide Financial Truth center.
- Inventory / Store is the Stock Truth center for inventory-managed / stockable items.
- Not every financial transaction passes through Inventory.
- Inventory Team A must build evidence for Stock Truth and the Inventory-to-Accounting interface boundary without designing Accounting internals.
- Existing GROUP A Inventory evidence must be reused. Do not restart research from zero.

Boss target routing input to preserve as a **target-design hypothesis / direction**, not source fact:

- Stockable / inventory-managed: Inventory path applies; Accounting effect may also apply.
- Consumable: no stock-ledger path by default; Accounting effect may apply.
- Service: no stock-ledger path; Accounting effect may apply.

Do not claim this is proven Thailand-wide practice merely because Boss directed it as target intent.

---

## 2. Governing Controls

Read and obey current canonical versions of:

1. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`
2. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md`
3. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/LIFECYCLE_EVIDENCE_PRESERVATION_AND_CHAIN_OF_CUSTODY_STANDARD.md`
4. `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.csv`
5. `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ACCOUNTING_INVENTORY_BACKBONE_EXECUTION_ROADMAP.md`
6. `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-MIG-A-INV-BB-R01.md`

Mandatory principles:

`No Evidence = No Progress.`  
`DELTA-FIRST.`  
`Never Skip Gate.`  
`No Cross-Team Execution.`  
`Reference ERP behavior = Evidence / Learning Input, not SMEsPlus target architecture by default.`  
`Boss = Sole Final Approver.`

---

## 3. Frozen Existing Evidence — Reuse First

### 3.1 Team A GROUP A evidence baseline

Frozen commit:

`8b0993d824cf726fa52edd687272ff54b0977c42`

Primary path:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/GROUP_01_SALES_INVENTORY_PURCHASE/`

Mandatory existing Inventory evidence to inspect first:

`02_INVENTORY_CAPABILITY_MODEL.md`

Also inspect supporting approved Team A artifacts from the same frozen package where needed for:

- shared Product/UOM/Warehouse/Location evidence;
- Sales handoff;
- Purchase handoff;
- E2E lifecycle;
- cross-module events/dependencies;
- business-fact ownership/handoff;
- quantity semantics;
- exception/cancel/return evidence;
- cross-module invariant candidates;
- Unknown / Conflict / Evidence Gap register;
- corrective closure report;
- final manifest.

Do not assume filenames from memory. Enumerate the frozen package and record exact resolved filenames.

### 3.2 Independent Evidence Review

Frozen commit:

`626873c3b924a0350dfd75cf52d276eff6414dd2`

Use it as independent verification evidence. Do not treat it as a substitute for primary evidence where direct re-performance is required.

### 3.3 Boss Evidence Gate

Commit:

`bd9b87f959711d502d0108d6ef4dce098a3bec1a`

Preserve all controlled carry-forwards. Boss approval did not convert Unknowns into Facts.

---

## 4. Authorized Source Inspection Boundary

Authorized source is READ ONLY.

Current known source root:

`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE`

Existing GROUP A evidence used relative source paths under:

`ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/`

Rules:

- Start from existing evidence and exact source citations.
- Re-read source only when needed to verify, close a gap, resolve a conflict, or strengthen Inventory-backbone coverage.
- Do not copy/reuse vendor source code into SMEsPlus target artifacts.
- Do not use vendor ORM/schema/workflow architecture as the target design.
- Do not write to source tree.
- Do not touch customer/Production systems.
- Do not upload proprietary raw source/dumps into GitHub.
- GitHub artifacts must contain neutral findings, provenance, hashes, evidence references and controlled summaries only.

If source path is inaccessible, register `EVIDENCE_MISSING` and stop only if the missing evidence is load-bearing.

---

## 5. Mission

Produce a standalone, traceable Inventory Core evidence package that answers:

1. What Inventory / Store business facts are already proven?
2. Which existing GROUP A evidence can be reused without re-research?
3. What is the Stock Truth concept boundary?
4. What are the exact quantity/state/event semantics supported by evidence?
5. What are Warehouse / Location / UOM / Lot / Serial / Package / Backorder / Return / Adjustment relationships?
6. What physical handoffs exist from Sales, Purchase and Manufacturing?
7. What evidence exists for stockable vs non-stock / consumable / service routing?
8. Where does Inventory end and Accounting begin?
9. Which valuation/accounting dependencies must remain open until Accounting contracts are controlled?
10. What SaaS / Tenant / Company / Warehouse isolation evidence exists?
11. What Unknowns / Conflicts / Evidence Gaps remain?
12. What minimum evidence must later be used in the Accounting x Inventory Cross-Proof?

This is Team A evidence work only.

Do not create SMEsPlus target architecture.

---

## 6. DELTA-FIRST Method

For every Inventory topic:

### Step 1 — Reuse check

Classify existing evidence as:

- `REUSE — VERIFIED`;
- `REUSE — VERIFIED WITH PRECISION NOTE`;
- `REVERIFY REQUIRED`;
- `CONFLICTING EVIDENCE`;
- `EVIDENCE MISSING`;
- `OUT OF CURRENT INVENTORY BACKBONE SCOPE`.

### Step 2 — Gap-only source re-performance

Only where needed, re-open exact source/dump evidence and record:

- source file/path;
- exact line/anchor/query;
- what it proves;
- evidence character;
- confidence/status;
- whether it changes an earlier Team A conclusion.

### Step 3 — Neutral synthesis

Express findings in business-neutral terms. Keep source-specific implementation separate.

### Step 4 — Interface dependency classification

If the evidence touches Accounting, classify it as one of:

- `INVENTORY-OWNED STOCK FACT`;
- `ACCOUNTING INTERFACE OBSERVATION`;
- `VALUATION CONTRACT PENDING`;
- `COA DEPENDENCY`;
- `ACCOUNTING INTERNAL — OUT OF TEAM A INVENTORY AUTHORITY`;
- `HOLD / EVIDENCE REQUIRED`.

Do not design final posting entries, COA, AR/AP internals, tax engine or accounting valuation internals.

---

## 7. Mandatory Inventory Evidence Domains

### 7.1 Product / Inventory-Management Classification

Determine what the source evidence actually supports for:

- stockable / storable behavior;
- consumable / non-storable behavior;
- service behavior;
- reservation bypass;
- movement creation / absence;
- effects on Inventory facts.

Explicitly separate:

`SOURCE OBSERVATION`

from

`BOSS TARGET ROUTING DIRECTION`.

Do not force source categories into the target canonical model.

### 7.2 Quantity Semantics

Evidence at minimum:

- demanded/planned quantity;
- reserved/allocated quantity;
- executed/moved quantity;
- on-hand quantity;
- available/free quantity where evidenced;
- UOM conversions;
- partial fulfillment;
- backorder;
- over/under behavior where evidenced;
- negative/return behavior.

Do not treat a source field name as a target canonical identity.

### 7.3 State / Event Lifecycle

Identify source-evidenced states/events for:

- movement instruction;
- reservation;
- execution;
- cancellation;
- return/reversal;
- backorder;
- adjustment/physical count;
- lot/serial/package traceability;
- replenishment;
- retry/duplicate implications where evidenced.

### 7.4 Ownership / Handoff

Evidence who owns each fact and where cross-domain handoffs occur for:

- Sales -> Inventory;
- Purchase -> Inventory;
- Manufacturing -> Inventory;
- Inventory -> Accounting interface.

Vendor model ownership is not automatically SMEsPlus target ownership; distinguish source observation from neutral business-semantic evidence.

### 7.5 Warehouse / Location / UOM / Traceability

Reconcile existing evidence for:

- company context;
- warehouse semantics;
- physical/logical location;
- UOM and conversion;
- lot/serial;
- package/handling unit;
- put-away;
- route/replenishment;
- branch evidence or absence.

### 7.6 Exception Paths

Include:

- partial receipt/delivery;
- backorder;
- shortage;
- cancellation before execution;
- cancellation after completed movement;
- return/reversal;
- correction;
- duplicate/retry;
- orphan / direct-SQL migration-invalid states where evidenced;
- cross-warehouse movement;
- failure/recovery evidence or gaps.

### 7.7 Accounting Boundary

Inventory may observe financial/valuation linkage but must not redesign Accounting.

Build an explicit boundary register for:

- receipt valuation handoff;
- delivery / cost handoff;
- return/reversal financial handoff;
- adjustment financial handoff;
- manufacturing valuation handoff;
- period/cutoff timing dependency;
- source accounting foreign keys / references where evidenced;
- unknown valuation algorithms or posting internals.

For each item state:

`WHAT INVENTORY KNOWS / WHAT INVENTORY EMITS / WHAT ACCOUNTING MUST OWN / WHAT REMAINS UNKNOWN`.

### 7.8 SaaS / Tenant / Company / Warehouse

Evidence source behavior and compare against approved cross-module SaaS invariants only at classification level.

Do not claim source implementation proves SMEsPlus runtime tenant isolation.

Flag any source pattern that would be unsafe in multi-tenant SaaS.

---

## 8. Accounting x Inventory Cross-Proof Candidate Inputs

Prepare candidate evidence inputs for later controlled Cross-Proof covering:

1. Purchase stock receipt.
2. Sales stock delivery.
3. Return/reversal.
4. Inventory adjustment.
5. Partial receipt/delivery.
6. Period/cutoff.
7. Manufacturing raw material -> production/WIP -> finished goods physical chain.
8. Stockable vs Consumable vs Service routing.
9. Tenant/company isolation.
10. Stock-fact to financial-fact provenance/reconciliation.

Do not execute the Accounting x Inventory Cross-Proof in this Team A session. Only prepare evidence inputs and identify missing dependencies.

---

## 9. Mandatory Deliverables

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/EXECUTION_R01/`

Required files:

1. `01_EXISTING_INVENTORY_EVIDENCE_REUSE_INDEX.md`
2. `02_INVENTORY_STOCK_TRUTH_CONCEPT_REGISTER.md`
3. `03_QUANTITY_STATE_EVENT_LIFECYCLE_EVIDENCE.md`
4. `04_WAREHOUSE_LOCATION_UOM_TRACEABILITY_EVIDENCE.md`
5. `05_EXCEPTION_PARTIAL_BACKORDER_RETURN_CANCEL_REGISTER.md`
6. `06_SALES_PURCHASE_MANUFACTURING_HANDOFF_EVIDENCE.md`
7. `07_STOCKABLE_CONSUMABLE_SERVICE_SOURCE_EVIDENCE_RECONCILIATION.md`
8. `08_INVENTORY_ACCOUNTING_INTERFACE_DEPENDENCY_REGISTER.md`
9. `09_SAAS_TENANT_COMPANY_WAREHOUSE_BOUNDARY_EVIDENCE.md`
10. `10_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
11. `11_CROSS_PROOF_INPUT_CANDIDATE_REGISTER.md`
12. `12_TEAM_A_INVENTORY_BACKBONE_EVIDENCE_REPORT.md`
13. `13_INVENTORY_BACKBONE_SHA256_MANIFEST.txt`
14. `14_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-R01.md`

If any required deliverable cannot be produced honestly, create the file with `HOLD / EVIDENCE REQUIRED` and explain why. Do not fabricate completion.

---

## 10. Evidence Register Fields

Every material finding must record, as applicable:

- Finding ID;
- Topic;
- Source / prior evidence location;
- exact path / line / query / artifact;
- Evidence Character;
- Fact Status;
- Owner / Team;
- Timestamp / commit where available;
- Reviewer / verifier status;
- Confidence;
- Unknown / Conflict;
- Accounting dependency;
- SaaS / Tenant implication;
- Gate impact;
- next action.

---

## 11. Required Final Status

Use one terminal status only:

### `TEAM A INVENTORY BACKBONE EVIDENCE RECONCILIATION COMPLETE — READY FOR INDEPENDENT EVIDENCE REVIEW`

only if all mandatory deliverables exist, evidence manifest is reproducible, all material claims are traceable and no load-bearing evidence gap is hidden.

Otherwise use:

### `HOLD / EVIDENCE REQUIRED`

or

### `FAIL / FROZEN — EVIDENCE OR CLEAN-ROOM CONTROL FAILURE`

as supported by evidence.

Team A must not self-declare Boss Gate PASS, Team B authorization, Development Ready or Production Ready.

---

## 12. Hard Prohibitions

Do NOT:

- restart the entire GROUP A research;
- copy/reuse vendor source into SMEsPlus;
- clone vendor ORM/schema/workflow architecture;
- design final SMEsPlus Inventory architecture;
- design Accounting internals;
- invent valuation/posting entries;
- infer Thailand-wide practice from one customer/reference source;
- modify source/customer/Production systems;
- write code;
- perform Figma/UX;
- perform Formal IBPV/IDTM/IESA;
- authorize Team B / Team C;
- merge to Production;
- hide or delete Unknowns/Conflicts merely to reach closure.

---

## 13. Lifecycle / Evidence Preservation

Before session closure:

1. Commit and push evidence to a dedicated controlled Team A branch.
2. Record exact branch and immutable commit SHA.
3. Recompute SHA-256 manifest.
4. Record session closure.
5. Preserve all superseded/corrected observations with explicit lineage.
6. Stop for Independent Evidence Review.
7. Do not merge to canonical `SMEsPlus` unless separately authorized by governance.

Expected evidence chain:

`Existing Approved Group A Evidence -> Inventory DELTA Reconciliation -> Independent Evidence Review -> Boss Evidence Gate / Controlled Handoff -> Inventory Team B only if authorized`.

---

## 14. Final Reminder

The goal is not to prove that the reference ERP is correct.

The goal is to understand the Stock Truth and cross-domain business semantics well enough that SMEsPlus can later design its own clean-room Inventory backbone without guessing and without forcing Accounting to repair missing Inventory semantics downstream.

`Accounting Core = Financial Truth Center.`  
`Inventory / Store = Stock Truth Center.`  
`Parallel Evidence Work; Controlled Backbone Convergence.`  
`No Backbone Reconciliation = No Dependent Design Freeze.`  
`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
