# STATE03 — Accounting <= Inventory Backbone Execution Roadmap

Document ID: `SMEPLUS-26-08-31-STATE03-BACKBONE-ROADMAP-001`  
Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Status: `BOSS DIRECTED / CONTROLLED EXECUTION ROADMAP`  
Effective Date: `2026-08-31`  
Owner: `SMEsPlus PMO / Architecture Governance`  
Final Approval Authority: `Boss`  
Jira: `ERPPLUS-137`  
Control Level: `/L99.99`

---

## 1. Boss Direction

Boss directs STATE03 sequencing to use the system operating path as the execution roadmap so that Accounting and Inventory do not become late-stage bottlenecks.

Controlling dependency direction:

`INVENTORY / STORE -> ACCOUNTING CORE`

Interpretation:

- `Accounting Core` is the enterprise-wide **Financial Truth Center**.
- `Inventory / Store` is the **Stock Truth Center** for inventory-managed / stockable items.
- Not every financial transaction passes through Inventory.
- Every material inventory valuation effect must ultimately reconcile to Accounting.
- Sales, Purchase, Manufacturing, Expense and Employee-related financial effects may converge on Accounting according to their business facts/events.

This roadmap is sequencing and architecture-governance control. It does not itself authorize target implementation, Development, Release or Production.

---

## 2. Existing Learning Evidence Reconciled

The current canonical file:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.csv`

already places the following in **Wave 2**:

- Sales
- Purchase
- Inventory / Warehouse
- Accounting Core / COA

The matrix also explicitly records these dependencies:

- Sales: `Final posting design waits for accounting contract`.
- Purchase: `Final AP/tax posting waits for accounting contract`.
- Inventory: `Valuation design waits for COA contract`.
- Accounting Core / COA: `Blocks financial-impact design freeze`.

Wave 3 then contains Accounting-dependent financial modules including AR, AP, Cash, Bank, Payment, Reconciliation, Expense, Asset, Thailand Tax Accounting, Budget Control and Financial Reporting.

Therefore this roadmap does **not replace the Learning Priority Matrix**. It converts its dependency logic into an explicit controlled execution sequence for STATE03.

The Learning Matrix remains subject to its own catalog-reconciliation controls and must not be read as final target-module count or final scope.

---

## 3. Boss Level-0 Backbone Model

Boss-provided Level-0 operating direction is preserved as the following conceptual routing model:

```text
SALE -----------------------> ACCOUNTING CORE
  |                              ^
  +------> INVENTORY / STORE ----+

PURCHASE -------------------> ACCOUNTING CORE
  |                              ^
  +------> INVENTORY / STORE ----+

MANUFACTURING
  +------> INVENTORY / STORE ----> ACCOUNTING CORE
  +------------------------------> ACCOUNTING CORE

EXPENSE --------------------> ACCOUNTING CORE

EMPLOYEE FINANCE -----------> ACCOUNTING CORE

ACCOUNTING CORE
  |- GL
  |- AR
  |- AP
  |- Cash / Bank
  |- Tax
  |- Asset
  |- Period / Closing
  `- Financial Reporting
```

This diagram is a Boss-directed conceptual input. Exact domain boundaries, event contracts, posting semantics, valuation semantics and target model remain controlled by evidence/design Gates.

---

## 4. Product / Service Routing Direction

Boss directs the following target routing concept for controlled design verification:

| Product / Service Class | Inventory / Stock Truth | Accounting / Financial Truth |
|---|---:|---:|
| Stockable / Inventory-managed | YES | YES where financial effect applies |
| Consumable | NO stock ledger by default | YES where financial effect applies |
| Service | NO stock ledger | YES where financial effect applies |

Important control:

`Consumable / Service != Inventory-managed stock fact.`

This classification is a Boss target-design input and must be reconciled against approved business evidence and target-domain semantics. It must not be presented as a universal statutory rule or as proof of implementation.

---

## 5. Execution Objective

Avoid two failure modes:

1. **Accounting bottleneck** — downstream groups complete design assumptions before financial contracts are controlled, causing rework and conflicting posting semantics.
2. **Inventory bottleneck** — Sales / Purchase / Manufacturing design advances without a controlled stock truth, quantity, reservation, movement and valuation boundary.

The project therefore uses **parallel evidence work + controlled design dependency**, not a simple serial stop-and-wait process.

---

## 6. Controlled Execution Lanes

### LANE A — Accounting Core Closure — PRIORITY BACKBONE

Continue current DOMAIN_01 Accounting Core / Thailand COA work without interruption.

Required controlled outcomes include, as applicable:

- canonical financial truth and ownership;
- COA / canonical classification;
- Account Type / Account Group controls;
- fiscal period / lock / correction semantics;
- posting / reversal / restatement boundary;
- AR / AP financial boundary;
- Tax interface boundary;
- Asset accounting interface;
- Financial Statement taxonomy / reporting mapping;
- SaaS tenant / company context;
- audit / traceability invariants.

Current COA Gate sequence remains controlled separately. This roadmap does not declare COA-G01..G08 complete and does not change their Gate status.

### LANE B — Inventory Core Evidence Reconciliation — START NOW

Inventory is not to wait until Accounting is fully closed.

Use DELTA-FIRST against existing approved GROUP A Team A evidence, especially the already-researched Inventory capability evidence, rather than restarting research from zero.

Inventory evidence reconciliation must isolate and strengthen the Stock Truth backbone including:

- Product / inventory-management classification evidence;
- UOM and conversion semantics;
- Warehouse / Location ownership and hierarchy;
- stock quantity facts;
- reservation / allocation;
- movement instruction vs executed physical fact;
- partial movement / backorder;
- lot / serial / traceability unit;
- handling/package unit where evidenced;
- inventory adjustment / physical count;
- returns / reversal / cancellation interaction;
- duplicate / retry / idempotency evidence relevant to stock facts;
- multi-company / tenant / warehouse boundaries;
- Manufacturing physical-stock handoff evidence;
- Sales / Purchase physical fulfillment handoffs;
- inventory valuation **interface boundary** to Accounting.

### Accounting-dependent Inventory boundary

Inventory Team A may research valuation evidence, but Team B must not silently invent final Accounting posting semantics.

Until the relevant Accounting contract is controlled, Accounting-dependent Inventory design must use explicit classifications such as:

- `ACCOUNTING INTERFACE DEPENDENCY`
- `VALUATION CONTRACT PENDING`
- `COA DEPENDENCY`
- `HOLD / EVIDENCE REQUIRED`

This allows Inventory stock-truth design to advance without fabricating financial answers.

### LANE C — Accounting x Inventory Cross-Proof — MANDATORY BACKBONE GATE

Before dependent groups may claim final canonical design readiness, the project must prove the Accounting x Inventory boundary at business-semantic level.

Minimum proof scenarios must include, where in scope and evidenced:

1. Stockable Purchase Receipt -> Stock Truth -> Valuation Handoff -> Accounting effect.
2. Stockable Sales Delivery -> Stock Truth -> Cost / Valuation Handoff -> Accounting effect.
3. Return / Reversal -> Stock reversal -> Financial correction/reversal interface.
4. Inventory Adjustment -> Quantity difference -> controlled financial interface.
5. Partial Receipt / Partial Delivery -> quantity and financial timing consistency.
6. Period / Cut-off -> Inventory physical date vs Accounting effective/recorded date.
7. Manufacturing Raw Material consumption -> WIP / production fact -> Finished Goods -> financial valuation interface.
8. Stockable vs Consumable vs Service routing proof.
9. Multi-company / Tenant isolation at Inventory-to-Accounting handoff.
10. Reconciliation identity / provenance from Stock Fact to Financial Fact.

`No Backbone Reconciliation = No Dependent Design Freeze.`

### LANE D — Dependent Group Progression

Existing GROUP A Sales + Inventory + Purchase evidence is preserved. Do not discard or restart it.

However, downstream lifecycle promotion must reconcile its design against the controlled Accounting + Inventory backbone before Development authority can be considered.

Manufacturing, Expense, Employee and later Groups are sequenced by dependency:

- Team A evidence learning may proceed in parallel when read-only and non-blocking.
- Team B may design independent business semantics where dependencies are controlled.
- Financial-impact design cannot be frozen against an unresolved Accounting contract.
- Stock-impact design cannot be frozen against an unresolved Inventory contract.
- Team C remains blocked by its normal Gate + Evidence Chain requirements.

---

## 7. Anti-Bottleneck Rules

### Rule AB-01 — Research may run ahead of design freeze

Read-only Team A research can proceed where it does not require unresolved target decisions.

### Rule AB-02 — Do not restart already-approved evidence

Existing verified evidence must be reused DELTA-FIRST. New research should close gaps, conflicts or missing coverage rather than repeat prior work.

### Rule AB-03 — Separate Stock Truth from Financial Truth

Inventory owns stock truth. Accounting owns financial truth.

A dependent business domain may request fulfillment or financial effects, but must not become the owner of another backbone's truth.

### Rule AB-04 — Explicit dependency beats guessed integration

When a financial or stock rule is not controlled, register the dependency rather than inventing a target behavior.

### Rule AB-05 — Parallel evidence, gated convergence

Accounting and Inventory may progress in parallel through evidence work, but must converge at the Accounting x Inventory Cross-Proof before dependent design freeze.

### Rule AB-06 — Preserve historical Group A work

GROUP A Sales + Inventory + Purchase remains valid evidence lineage. It will be reconciled, not erased.

### Rule AB-07 — No lifecycle jump

`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`Never Skip Gate.`  
`No Evidence Chain Seal = No Team C.`

---

## 8. Controlled Sequence

```text
CURRENT
  |
  +--> ACCOUNTING CORE / COA CLOSURE ---------------------+
  |                                                        |
  +--> INVENTORY CORE EVIDENCE RECONCILIATION ------------+
                                                           |
                                                           v
                                      ACCOUNTING x INVENTORY CROSS-PROOF
                                                           |
                    +--------------------------------------+--------------------------------+
                    |                                      |                                |
                    v                                      v                                v
           SALES / PURCHASE                         MANUFACTURING                    EXPENSE / EMPLOYEE
        BACKBONE RECONCILIATION                  DEPENDENCY RECONCILIATION          FINANCIAL RECONCILIATION
                    |                                      |                                |
                    +--------------------------------------+--------------------------------+
                                                           |
                                                           v
                                      OTHER GROUPS BY DEPENDENCY / EVIDENCE
                                                           |
                                                           v
                                              NORMAL PRE-DEVELOPMENT GATES
                                                           |
                                                           v
                                                 BOSS DEVELOPMENT DECISION
                                                           |
                                                           v
                                                        TEAM C
```

---

## 9. Immediate Controlled Actions

### A1 — Accounting Core

Continue existing controlled Accounting / COA Gate work. Do not reset or duplicate.

Status: `IN PROGRESS UNDER SEPARATE EVIDENCE / GATES`.

### A2 — Inventory Core

Issue a controlled Team A **Inventory Core Backbone Evidence Reconciliation** prompt using the New Prompt Governance standard.

Method:

`DELTA-FIRST / READ-ONLY / EVIDENCE-FIRST / CLEAN-ROOM`

Primary existing input:

- Boss-approved GROUP A Team A evidence lineage;
- Independent Evidence Review lineage;
- current Learning Priority Matrix;
- current project governance and SaaS / Tenant controls.

Output must identify what is already proven, what must be re-used, what remains unknown, and exactly which Accounting-interface dependencies must stay open.

### A3 — GROUP A Sales + Inventory + Purchase

Preserve current evidence and Formal IBPV lineage. Do not authorize Team C solely because prior Group A work exists.

Before Development consideration, reconcile GROUP A against the final controlled dual-backbone contracts.

### A4 — Manufacturing / Expense / Employee

Queue for evidence-first work according to dependency. Do not silently turn this roadmap into new Functional Scope.

---

## 10. Evidence / Gate Control

For every lane and Gate, evidence records must contain:

- Item / Task
- Owner
- Evidence Location / Direct Link
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact
- Preservation Status

If a required element is missing:

`HOLD / EVIDENCE REQUIRED`

Do not infer progress percentages without an approved denominator and weighting.

`% Board = TBD / BASELINE REQUIRED`  
`% STATE03 = TBD / BASELINE REQUIRED`  
`% Current Backbone Step = TBD / BASELINE REQUIRED`

---

## 11. Scope / Authority Boundary

This roadmap authorizes sequencing, evidence reconciliation and controlled research only.

It does **not** authorize:

- Team C / Development;
- physical production DB/schema design;
- Production deployment;
- Release;
- statutory claims without evidence;
- automatic conversion of Learning behavior into SMEsPlus target architecture;
- copying/reusing vendor architecture/source/schema/workflow.

SMEsPlus remains a 100% clean-room Node.js SaaS ERP.

`Reference ERP behavior = Evidence / Learning Input, not target architecture by default.`

---

## 12. Boss Control Principles

`Accounting Core = Financial Truth Center.`  
`Inventory / Store = Stock Truth Center for inventory-managed items.`  
`Consumable / Service do not enter Stock Truth by default.`  
`Parallel Evidence Work; Controlled Backbone Convergence.`  
`No Backbone Reconciliation = No Dependent Design Freeze.`  
`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
