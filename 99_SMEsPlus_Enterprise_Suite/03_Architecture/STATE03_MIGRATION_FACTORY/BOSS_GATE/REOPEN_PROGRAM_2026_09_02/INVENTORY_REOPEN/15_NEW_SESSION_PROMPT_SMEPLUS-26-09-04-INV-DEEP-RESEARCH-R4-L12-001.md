# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# New Session Prompt — Inventory Deep Research R4 / L1-L12 Minimum / v2.0 Preparation / L9999.9999

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Prompt Branch: `prompt/inventory-deep-research-r4-l12-2026-09-04-001`  
Execution Branch To Create: `audit/inventory-deep-research-r4-l12-2026-09-04-001`  
Control Level: `/L9999.9999`  
Model: `Claude Opus 5 high`  
Boss: `Sole Final Approver`  
AAS+ Name: `AAS+ — AI Audit SMEsPlus`  
Status: `AUTHORIZED FOR INVENTORY L1-L12 DEEP RESEARCH — V2.0 PREPARATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 0. Executor Instruction

You are Claude Opus 5 high acting as an independent SMEsPlus Inventory Deep Research executor.

Proceed autonomously through the full L1-L12 Deep Research cycle. Do not ask Boss to click intermediate choices. Use Checkpoints, evidence logs, and explicit HOLD markers when evidence is missing.

Create a fresh isolated execution branch:

`audit/inventory-deep-research-r4-l12-2026-09-04-001`

Do not reuse dirty worktrees. Do not overwrite unrelated pending changes. Do not merge into `SMEsPlus`.

Stop only after publishing the complete Inventory R4 Deep Research evidence package and ending at:

`READY FOR BOSS REVIEW — INVENTORY R4 L1-L12 DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

If Accounting COGS Gap evidence is required but unavailable for final valuation conclusions, end the affected sections with:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

---

## 1. Mission

Perform Inventory Deep Research R4 using the new central SMEsPlus standard:

`ALL MODULE DEEP RESEARCH STANDARD = LEVEL 1 TO LEVEL 12 MINIMUM`

Inventory R4 must confirm, deepen, and gap-fill the prior Inventory evidence so it can prepare Inventory Final Solution v2.0.

This is not a reset. Preserve all prior evidence, decisions, objections, HOLD items, and lineage.

This is not a Development Final Gate.

---

## 2. Mandatory Sources To Read First

Read and cite all applicable source files before producing conclusions:

| No. | Source | Required Use |
|---:|---|---|
| 1 | `13_BOSS_RULING_ALL_MODULE_DEEP_RESEARCH_STANDARD_L1_L12_2026_09_04.md` | Central L1-L12 standard and L13+ rule |
| 2 | `14_INVENTORY_R4_MENU_EVIDENCE_INTAKE_L1_L12.md` | 29-menu Inventory scope from Boss screenshots |
| 3 | `11_BOSS_RULING_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001.md` | Inventory v2.0 authorization and COGS dependency |
| 4 | `12_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001.md` | Current v2.0 dependency lock |
| 5 | `03_SESSION_LINK_REGISTER_SMEPLUS-26-09-02-INV-REOPEN-001.md` | Inventory evidence lineage and direct links |
| 6 | Inventory v1.0 Final Solution package | Use as design baseline; do not overwrite without evidence delta |
| 7 | Inventory Menu Deep Challenge outputs | Use as menu/process/object evidence lineage |
| 8 | Inventory Clean-room containment outputs | Preserve clean-room controls |
| 9 | Accounting COGS Gap package | Required for final valuation/COGS/period-close conclusions when available |

If any mandatory source is missing, record it as `EVIDENCE GAP` and continue only where evidence remains sufficient.

---

## 3. Clean-Room Rules

Use only these terms in new design and research text:

- `OpenSource reference ERP`
- `benchmark ERP`
- `reference system`

Do not rely on or reproduce vendor-specific source code, schema, ORM, workflow, module architecture, naming, or implementation logic.

SMEsPlus is a new clean-room Node.js SaaS ERP.

Absolute rule:

`Understand deeply. Transfer accurately. Preserve verifiably.`

---

## 4. Mandatory Inventory Menu Scope

Inventory R4 must cover all 29 menus from Boss screenshot evidence.

| Group | Menus |
|---|---|
| Operations | Replenishment; Inventory Adjustments; Transfers; Scrap; Landed Costs; Run Scheduler |
| Products | Products; Product Variants; Lots/Serial Numbers |
| Reporting | Stock; Locations; Moves History; Stock Moves; Valuation; Warehouse Analysis |
| Configuration | Settings; Warehouses; Locations; Routes; Rules; Operation Types; Storage Categories; Putaway Rules; Product Categories; Attributes; Product Packagings; Reordering Rules; Barcode Nomenclatures; UoM Categories |

Every menu must be traced through L1-L12, or explicitly marked as `HOLD` with reason and owner.

---

## 5. L1-L12 Minimum Deep Research Requirements

### L1 — Domain Understanding

For every Inventory menu, define:

1. Business purpose.
2. Primary user role.
3. Thai SME operating reality.
4. Input/output business facts.
5. Relationship to Sale, Purchase, Manufacturing, Accounting, Approval, Document, and Reporting.

### L2 — UI / Field / Configuration Forensic

For every menu, identify:

1. Required fields.
2. Optional fields.
3. Configuration drivers.
4. Status/state fields.
5. Visibility rules.
6. User-facing labels and Thai naming candidates.
7. Configuration risk.

### L3 — Function Forensic

For every function, identify:

1. Trigger.
2. Preconditions.
3. Postconditions.
4. State transition.
5. Quantity impact.
6. Cost impact.
7. Document or event output.
8. Audit evidence required.

### L4 — Cross-Module Dependency

Map dependencies with at least:

1. Sale to delivery to stock movement.
2. Purchase to receipt to stock valuation.
3. Manufacturing to raw material, WIP, finished goods, capacity, and cost.
4. Accounting to valuation, interim, COGS, landed cost, return, scrap, and close.
5. Approval to controlled changes.
6. Document to evidence attachment.
7. Reporting to reconciliation.

### L5 — Whole-System Semantic

Preserve Inventory business meaning across the whole system:

1. Stock on hand.
2. Forecast stock.
3. Reserved stock.
4. Incoming stock.
5. Available stock.
6. Lot/serial traceability.
7. Ownership and location semantics.
8. Internal transfer versus valuation movement.
9. Scrap versus loss versus salvage.
10. Landed cost allocation meaning.

### L6 — Contradiction / Failure / Edge Case

Challenge at least:

1. Negative stock.
2. Backorder.
3. Partial delivery.
4. Partial receipt.
5. Return after invoice.
6. Return before invoice.
7. Scrap with salvage value.
8. Lot mismatch.
9. UoM conversion mismatch.
10. Scheduler duplication.
11. Reordering rule conflict.
12. Multi-company location leakage.
13. Cost layer timing gap.
14. Landed cost after sale.
15. Inventory adjustment after period close.

### L7 — Inventory Control / Internal Control

Adapt L7 for Inventory:

1. Stock integrity control.
2. Movement approval control.
3. Adjustment approval control.
4. Scrap approval control.
5. Location control.
6. Route/rule change control.
7. Lot/serial integrity control.
8. Count variance control.
9. Segregation of duties.
10. Audit trail requirement.

### L8 — Data / Identity / Immutability

Define canonical identity and immutability rules for:

1. Product.
2. Variant.
3. Warehouse.
4. Location.
5. Operation type.
6. Route.
7. Rule.
8. Stock movement.
9. Move line.
10. Lot/serial.
11. Package.
12. Inventory adjustment.
13. Scrap.
14. Landed cost.
15. Valuation event.

Account code, product code, names, and labels are not sufficient canonical identity by themselves.

### L9 — SaaS / Multi-Tenant / Multi-Company

Prove:

1. Tenant isolation.
2. Company isolation.
3. Branch/location isolation.
4. Shared template versus tenant-owned customization boundary.
5. No cross-tenant stock visibility.
6. No cross-company cost leakage.
7. No hard-coded Thailand-only logic in SaaS core.
8. Controlled localization extension points.

### L10 — Migration / Historical Continuity

Map:

1. Opening stock.
2. Historical movement.
3. Lot/serial history.
4. Product identity continuity.
5. Warehouse/location continuity.
6. Valuation continuity.
7. Cutover reconciliation.
8. Migration exception treatment.
9. Legacy reference quarantine.
10. Evidence lineage.

### L11 — Reconciliation / End-to-End Proof

Produce end-to-end proof scenarios for:

1. Buy to receive to stock to bill to valuation.
2. Sale to reserve to delivery to COGS dependency.
3. Manufacture to consume to WIP to finished goods.
4. Return and COGS reversal dependency.
5. Scrap and salvage dependency.
6. Inventory adjustment and approval evidence.
7. Landed cost and allocation dependency.
8. Period close and report tie-out.
9. Multi-company isolation proof.
10. Migration opening tie-out.

### L12 — Adversarial Challenge / Audit Veto

AAS+ must challenge the R4 output before closure:

1. 9 Veto Challenge Council.
2. 9 Special Team Challenge.
3. 4 AI Expert Overlay roles.
4. PMO Gate review.
5. Evidence completeness test.
6. Contradiction register.
7. HOLD register.
8. Boss decision list.

No team may self-declare PASS.

---

## 6. L13+ Conditional Auto-Escalation

Open `L13+` automatically only when the evidence requires deeper analysis.

Examples:

| Conditional Level | Trigger Example |
|---|---|
| L13 — Cost Timing Forensic | Cost is affected by receipt, delivery, invoice timing, landed cost, or return sequence. |
| L14 — Traceability Proof | Lot/serial traceability cannot be proven from L1-L12 alone. |
| L15 — Scheduler / Automation Race Condition | Replenishment or scheduler can duplicate or conflict with manual actions. |
| L16 — Close/Reopen Governance | Period close and late inventory changes conflict. |

Every L13+ item must record evidence, reason, checkpoint, risk/gap ID, owner, and next Gate.

---

## 7. Required Outputs

Create all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/DEEP_RESEARCH_R4_L12_EXECUTION/`

Minimum required files:

| No. | File |
|---:|---|
| 00 | `00_EXECUTION_CHECKPOINT_LOG.md` |
| 01 | `01_EVIDENCE_INTAKE_REGISTER.md` |
| 02 | `02_L1_DOMAIN_UNDERSTANDING_REGISTER.md` |
| 03 | `03_L2_UI_FIELD_CONFIGURATION_FORENSIC.md` |
| 04 | `04_L3_FUNCTION_FORENSIC_REGISTER.md` |
| 05 | `05_L4_CROSS_MODULE_DEPENDENCY_MAP.md` |
| 06 | `06_L5_WHOLE_SYSTEM_SEMANTIC_REGISTER.md` |
| 07 | `07_L6_CONTRADICTION_FAILURE_EDGE_CASE_REGISTER.md` |
| 08 | `08_L7_INVENTORY_CONTROL_INTERNAL_CONTROL_REGISTER.md` |
| 09 | `09_L8_DATA_IDENTITY_IMMUTABILITY_REGISTER.md` |
| 10 | `10_L9_SAAS_MULTI_TENANT_MULTI_COMPANY_REGISTER.md` |
| 11 | `11_L10_MIGRATION_HISTORICAL_CONTINUITY_REGISTER.md` |
| 12 | `12_L11_RECONCILIATION_END_TO_END_PROOF_REGISTER.md` |
| 13 | `13_L12_AAS_PLUS_ADVERSARIAL_CHALLENGE_AUDIT_VETO.md` |
| 14 | `14_MENU_COVERAGE_REGISTER_29_OF_29.md` |
| 15 | `15_OBJECT_IMPACT_MATRIX.md` |
| 16 | `16_PROCESS_HANDOFF_MAP.md` |
| 17 | `17_ACCOUNTING_COGS_VALUATION_DEPENDENCY_REGISTER.md` |
| 18 | `18_THAI_USER_VALIDATION_CHECKLIST.md` |
| 19 | `19_L13_PLUS_ESCALATION_REGISTER.md` |
| 20 | `20_RISK_GAP_DECISION_REGISTER.md` |
| 21 | `21_PMO_REVIEW_AND_RECOMMENDATION.md` |
| 22 | `22_BOSS_REVIEW_PACKAGE.md` |
| 23 | `23_SESSION_CLOSURE.md` |
| 24 | `24_SHA256_MANIFEST.md` |

If additional files are needed, create them and register them in `00_EXECUTION_CHECKPOINT_LOG.md` and `24_SHA256_MANIFEST.md`.

---

## 8. Accounting COGS Dependency Lock

Inventory may study valuation, COGS, landed cost, period close, returns, and scrap.

Inventory must not finalize those conclusions until Accounting COGS Gap evidence is available and cited.

Use this status where needed:

`DEPENDENCY: ACCOUNTING COGS GAP`

Known dependency areas:

1. COGS at delivery.
2. Stock input interim.
3. Stock output interim.
4. Periodic versus perpetual valuation behavior.
5. Standard, Average, FIFO cost behavior.
6. Return cost basis.
7. Scrap and salvage accounting.
8. Landed cost allocation and posting.
9. Period close and late movement handling.
10. Inventory report to GL reconciliation.

---

## 9. Checkpoint Rules

Create at least these checkpoints:

| Checkpoint | Condition |
|---|---|
| CP0 | Branch created and mandatory sources read. |
| CP1 | 29-menu scope confirmed. |
| CP2 | L1-L6 baseline completed. |
| CP3 | L7-L12 completed. |
| CP4 | COGS dependency status confirmed. |
| CP5 | AAS+ adversarial challenge completed. |
| CP6 | PMO recommendation completed. |
| CP7 | Boss Review Package and closure published. |

Do not wait for Boss during checkpoints. Record the checkpoint and continue unless a required evidence source blocks the work.

---

## 10. Publication Requirements

Before closure:

1. Commit all output files.
2. Push the execution branch.
3. Confirm file count.
4. Confirm 29/29 menu coverage.
5. Confirm L1-L12 completion or HOLD reason.
6. Confirm L13+ count if any.
7. Confirm SHA-256 manifest.
8. Provide direct GitHub links for branch, commit, output folder, Boss Review Package, and Session Closure.

---

## 11. Non-Authorization Lock

This session does not authorize:

- Team B build readiness.
- Team C development.
- Source code implementation.
- Database implementation.
- Merge to canonical branch.
- Production.
- Release.

Boss remains the sole Final Approver.

---

## 12. Final Required Statement

End with one of these statuses only:

1. `READY FOR BOSS REVIEW — INVENTORY R4 L1-L12 DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`
2. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`
3. `HOLD - MANDATORY EVIDENCE SOURCE MISSING`
4. `HOLD - CLEAN-ROOM RISK FOUND`

Do not declare PASS.
