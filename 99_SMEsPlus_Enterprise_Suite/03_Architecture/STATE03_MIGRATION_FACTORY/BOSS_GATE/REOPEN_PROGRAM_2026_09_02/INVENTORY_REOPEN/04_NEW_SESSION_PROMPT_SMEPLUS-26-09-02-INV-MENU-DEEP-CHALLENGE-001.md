# [SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001]
# Inventory Menu-by-Menu Deep Challenge for Thai SMEsPlus / Claude Sonnet 5 Max / L999.999

## SINGLE END-TO-END NEW SESSION PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 - Architecture`  
Domain: `INVENTORY / Stock Truth / Warehouse Operation / Reporting / Configuration / Thai Business UX`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Target Executor: `Claude Sonnet 5 Max`  
Execution Mode: `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / MENU-BY-MENU / CHECKPOINT-CONTROLLED / L999.999`  
Boss: `Sole Final Approver at Final Gate`

This is a controlled New Session Prompt after Inventory Full Reopen and Clean-Room remediation.

The prior Inventory reopen package is evidence and context. It is not enough by itself to become the final SMEsPlus Inventory solution. This session must study Inventory menu-by-menu, reconstruct every working process, challenge the flow deeply through `Ai Audit SMEsPlus`, and produce a Thai SMEsPlus reference package for later design consideration.

This session is **not** a Final Solution for SMEsPlus.  
This session is **not** a development authorization.  
This session is **not** a Gate PASS.  
This session is **not** approval for Team B, Team C or Development.  
This session is a controlled reference study to support future Thai SMEsPlus Inventory design decisions.

---

## 1. Mission

Study Open ERP / Odoo-style Inventory menus as a **process benchmark only**, then rebuild the understanding into a new Thai SMEsPlus business-process reference.

The executor must answer, for every menu and functional area:

1. `Purpose` - why the menu exists in real business operation;
2. `Input` - what data/document/event/user action enters the process;
3. `Process` - what happens operationally, including state changes and controls;
4. `Output` - what record, report, document, stock fact or exception is produced;
5. `Accounting / Control Impact` - what stock truth, valuation, audit, accounting handoff or approval effect exists.

The executor must also answer:

1. which Inventory processes have already been studied and can be carried forward;
2. which prior findings must be reopened because menu-level process detail is missing;
3. where Inventory owns truth and where Accounting/Sales/Purchase/MFG only receive handoff facts;
4. how Thai users should understand each menu in Thai business language;
5. which menus are mandatory for Thai SMEsPlus, conditional by industry, or not applicable;
6. what gaps must remain before any Gate movement.

Target condition:

`INVENTORY MENU-BY-MENU PROCESS REFERENCE PACKAGE PUBLISHED - NOT FINAL SOLUTION`

---

## 2. Absolute Clean-room Boundary

Open ERP / Odoo / other ERP systems may be used only as:

- `PROCESS BENCHMARK`;
- `MENU COVERAGE CHECKLIST`;
- `BUSINESS CAPABILITY REFERENCE`;
- `RISK DISCOVERY SOURCE`;
- `LAYER 2 AUDIT QUARANTINE SOURCE` only when needed for audit verification.

Hard prohibitions:

1. Do not copy source code.
2. Do not copy ORM models.
3. Do not copy database schema.
4. Do not copy method names, field names, file paths or implementation architecture.
5. Do not copy menu names as final SMEsPlus names.
6. Do not claim SMEsPlus must follow Open ERP / Odoo behavior.
7. Do not expose quarantined source-level evidence to Team B, Team C or Development.
8. Do not treat benchmark behavior as approved SMEsPlus design.

Required transformation:

`Benchmark Menu -> Business Meaning -> Thai User Language -> SMEsPlus Candidate Process Reference -> Evidence / Gap / Gate Impact`

If source-level inspection is unavoidable for understanding historical evidence, keep it in `Layer 2 Audit Quarantine` and produce only clean-room business learning summaries for downstream use.

---

## 3. Mandatory Prior Evidence Load

Before asking new questions or starting menu-level conclusions, inspect and reconcile at minimum:

1. `01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`
2. `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`
3. `03_SESSION_LINK_REGISTER_SMEPLUS-26-09-02-INV-REOPEN-001.md`
4. Inventory Reopen execution branch: `audit/inventory-reopen-2026-09-02-inv-reopen-001`
5. Inventory Reopen execution commit: `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d`
6. all 20 Inventory Reopen deliverables;
7. Clean-Room remediation branch: `audit/inventory-core-corr007b-3high-closure-010`
8. Clean-Room remediation commit: `9996072aa3a353dca99de4b22e8611171e24baf4`
9. CORR-007B clean-room remediation record;
10. prior DR/CORR/IDR Inventory evidence where cited by the reopen package;
11. Accounting / Inventory boundary evidence and joint-session references;
12. New Prompt Governance v2.0, 9 Veto / 9 Special Team Charter and Global Challenge Ledger.

Rules for previously studied material:

- If already studied with evidence and no material delta exists, classify `CARRY_FORWARD_WITH_EVIDENCE`.
- If studied but not at menu/process/handoff depth, classify `REOPEN_FOR_MENU_PROCESS_DEPTH`.
- If studied but clean-room risk exists, classify `REWRITE_AS_CLEAN_ROOM_LEARNING`.
- If contradiction exists, classify `CONFLICTING - REOPEN REQUIRED`.
- If evidence is missing, classify `HOLD / EVIDENCE REQUIRED`.

Do not repeat prior work without a material reason. Complete the missing process layer instead.

---

## 4. Mandatory Menu Coverage From Boss Screenshots

Study every menu below. If evidence is insufficient, create the row anyway and mark `HOLD / EVIDENCE REQUIRED`.

### 4.1 Operations

1. Replenishment
2. Inventory Adjustments
3. Transfers
4. Scrap
5. Landed Costs
6. Run Scheduler

### 4.2 Products

1. Products
2. Product Variants
3. Lots/Serial Numbers

### 4.3 Reporting

1. Stock
2. Locations
3. Moves History
4. Stock Moves
5. Valuation
6. Warehouse Analysis

### 4.4 Configuration

1. Settings
2. Warehouses
3. Locations
4. Routes
5. Rules
6. Operations Types
7. Storage Categories
8. Putaway Rules
9. Product Categories
10. Attributes
11. Product Packagings
12. Reordering Rules
13. Barcode Nomenclatures
14. UoM Categories

---

## 5. Thai Business UX Naming Rule

SMEsPlus is for Thai users. Menu and report names must communicate clearly to Thai SME owners, warehouse staff, accountants, purchasing, sales, management and auditors.

The executor must propose Thai candidate names for every menu/report studied.

Examples:

| Benchmark Term | Thai Candidate Name | Naming Note |
|---|---|---|
| Replenishment | เติมสินค้า / แผนเติมสินค้า | Must distinguish manual replenishment vs automatic planning |
| Inventory Adjustments | ปรับปรุงยอดสต็อก | Must show approval and reason control |
| Transfers | โอนย้ายสินค้า | Must support warehouse/location/source/destination |
| Scrap | ตัดสินค้าชำรุด/สูญเสีย | Must connect to control and accounting impact |
| Landed Costs | ต้นทุนสินค้าเพิ่มเติม | Must connect to inventory valuation and Accounting handoff |
| Run Scheduler | ประมวลผลแผนสต็อก | Must explain automatic procurement/replenishment trigger |
| Lots/Serial Numbers | เลขล็อต/เลขซีเรียล | Must fit traceability, warranty, expiry, recall |
| Stock Moves | รายการเคลื่อนไหวสินค้า | Must distinguish movement facts from summary reports |
| Valuation | มูลค่าสินค้าคงเหลือ | Must connect to accounting and costing policy |
| Putaway Rules | กฎจัดเก็บสินค้าเข้าที่ | Must be understandable to warehouse users |

These names are candidates only. They are not final approved SMEsPlus UI labels.

---

## 6. Mandatory Study Sequence

Study in this order. Do not jump directly to design conclusions.

```text
Prior Evidence Reconciliation
-> Menu Coverage Extraction
-> Configuration Foundation
-> Product Master and UoM
-> Warehouse / Location / Route / Rule Setup
-> Operation Types and Transaction Flows
-> Receiving / Delivery / Internal Transfer / Adjustment / Scrap
-> Replenishment / Scheduler / Reordering
-> Lot / Serial / Packaging / Storage / Putaway
-> Valuation / Landed Cost / Accounting Handoff
-> Reporting / Analysis / Audit Trail
-> Migration and Data Quality Implications
-> Thai SMEsPlus Process Reference
-> Ai Audit SMEsPlus Challenge
-> Boss Final Gate Package
```

---

## 7. Ai Audit SMEsPlus Structure

`Ai Audit SMEsPlus = 9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Roles Overlay.`

Keep these layers separate.

| Layer | Count | Role |
|---|---:|---|
| `9 Veto Challenge Council` | 9 | Primary challenge body for Gate risk, contradiction and no-evidence control |
| `9 Special Team Challenge` | 9 | Deep-dive body for Inventory operation, product, traceability, valuation, migration and control risks |
| `4 AI Expert Roles` | 4 | Overlay review only; not a primary team and not a substitute for 9+9 |

Every major conclusion must include:

- 9 Veto Challenge Council comments;
- 9 Special Team Challenge comments;
- 4 AI Expert Roles Overlay comments;
- unresolved objections;
- required evidence before Gate movement.

---

## 8. 9 Veto Challenge Council

Run all nine tracks separately before convergence.

| Track | Veto Role | Inventory Menu Challenge Focus |
|---|---|---|
| 01 | Audit VETO / Evidence & Governance | Evidence chain, commit/branch traceability, prior-study carry-forward, no skipped Gate |
| 02 | TBRAC / Thailand Business Reality & User Fitness | Thai warehouse practice, SME simplicity, Thai user language, approval reality |
| 03 | IBPV / Business Process & Design Integrity | End-to-end process flow, handoff, ownership boundary, exception path |
| 04 | IDTM / Data, Identity, Reconciliation & Integrity | Product identity, lot/serial, UoM, movement identity, reconciliation, migration replay |
| 05 | IESA / ERP & SaaS System Integrity | Multi-warehouse, multi-company, route/rule architecture, SaaS isolation and scale |
| 06 | Financial / Accounting / Tax / Statutory VETO | Valuation, landed cost, COGS, adjustment, scrap and accounting handoff |
| 07 | Security / Privacy / Resilience VETO | Permissions, destructive actions, audit trail, recovery, concurrent operations |
| 08 | Clean-Room / IP / Provenance VETO | No source leakage, no vendor-specific architecture, Layer 2 quarantine enforcement |
| 09 | AI Control / Automation / Human Oversight VETO | Scheduler, mapping, anomaly detection, deterministic controls, no fabricated stock facts |

Each track must return one of:

- `CONTINUE_WITH_NOTES`
- `HOLD`
- `FAIL / FROZEN`

The most conservative unresolved material verdict controls the final package.

---

## 9. 9 Special Team Challenge

Create nine special challenge tracks for menu-level depth.

| Team | Challenge Focus | Required Question |
|---|---|---|
| S1 Warehouse Operations | Transfers, adjustments, scrap, physical flow | Can a Thai warehouse user execute the process without hidden accounting or IT knowledge? |
| S2 Product Master / UoM | Products, variants, attributes, UoM, packaging | Is product identity stable enough for stock truth and migration? |
| S3 Stock Movement / Reservation | stock moves, move history, availability | Are movement facts, reservations and availability clearly separated? |
| S4 Traceability | lot, serial, package, storage category, putaway | Can the system trace recall, warranty, expiry and location history? |
| S5 Replenishment / Route / Scheduler | replenishment, reordering rules, routes, rules, scheduler | Can replenishment be explained as business logic without copying vendor architecture? |
| S6 Valuation / Landed Cost / Accounting Handoff | landed costs, valuation, product categories | Does Inventory emit enough facts for Accounting without owning Accounting truth? |
| S7 Reporting / Analytics | stock, locations, valuation, warehouse analysis | Do reports answer operational, management and audit questions separately? |
| S8 Thai UX / Localization | all menu labels and workflow language | Are Thai candidate names understandable to Thai SMEs and auditors? |
| S9 Migration / Data Quality | master data, balances, movement history, traceability | Can legacy stock be migrated, reconciled and replayed without losing truth? |

Each team must produce objections, evidence, gaps, and recommended next action.

---

## 10. 4 AI Expert Roles Overlay

The following four overlay roles are mandatory and must challenge the Inventory menu package after the 9+9 findings are drafted.

| AI Expert Role | Primary Menu Focus | Required Challenge |
|---|---|---|
| Leader Functional Design | Replenishment, Inventory Adjustments, Transfers, Scrap, Lots/Serial Numbers, Operation Types | Are user flows, UAT scenarios, exception paths and Thai UX names sufficient for later Team B design? |
| Leadership Database Design | Products, Product Variants, Lots/Serial Numbers, Locations, Stock Moves, UoM Categories, Product Packagings | Are identities, relationships, constraints, migration keys and reconciliation facts clearly understood? |
| Lead Integration & Localization | Valuation, Landed Costs, Product Categories, Accounting handoff, Thai reporting/control | Are Thai accounting/tax/localization impacts separated from Inventory ownership and properly routed? |
| Lead Code & UI Architect | Settings, Warehouses, Routes, Rules, Putaway Rules, Scheduler, Reporting | Are future UI/process architecture risks visible without copying source code or vendor architecture? |

These four roles may not approve the final solution. They may only challenge, expose unknowns, and recommend evidence requirements for the Boss Final Gate.

---

## 11. Mandatory Menu Impact Matrix

For every menu, object, process and report, create a matrix with no blank cells.

| Field | Required |
|---|---|
| ID | Required |
| Menu group | Required |
| Benchmark menu/function | Required |
| Thai candidate name | Required |
| Business purpose | Required |
| Input | Required |
| Process | Required |
| Output | Required |
| Handoff to next process | Required |
| Stock truth impact | Required: Y/N/Conditional |
| Quantity impact | Required: Y/N/Conditional |
| Reservation impact | Required: Y/N/Conditional |
| Lot/serial impact | Required: Y/N/Conditional |
| Warehouse/location impact | Required: Y/N/Conditional |
| Valuation impact | Required: Y/N/Conditional |
| Accounting handoff impact | Required: Y/N/Conditional |
| Tax/statutory impact | Required: Y/N/Conditional |
| Management report impact | Required: Y/N/Conditional |
| Audit/control impact | Required: Y/N/Conditional |
| Migration impact | Required: Y/N/Conditional |
| SaaS/multi-company impact | Required: Y/N/Conditional |
| Clean-room transformation note | Required |
| Evidence location | Required or `HOLD / EVIDENCE REQUIRED` |
| Owner | Required or `UNASSIGNED` |
| Verifier | Required or `UNVERIFIED` |
| Gate impact | Required |
| Status | `COVERED / PARTIAL / GAP / HOLD / NOT APPLICABLE` |

Do not use blank cells. If unknown, write `UNKNOWN / EVIDENCE REQUIRED`.

---

## 12. Mandatory Process Questions Per Menu

For every menu, answer these questions:

1. What business problem does this menu solve?
2. Who uses it in a Thai SME operation?
3. What document or event normally starts the process?
4. What master data must exist first?
5. What user action is manual and what action is automated?
6. What stock quantity state changes?
7. What valuation or accounting handoff may occur?
8. What approval, audit trail or segregation of duties is required?
9. What can go wrong in real operation?
10. What migration data must be preserved?
11. What should SMEsPlus call this in Thai?
12. What must not be copied from benchmark ERP behavior?

---

## 13. Checkpoints

Boss will wait at the Final Gate. Intermediate checkpoints may proceed autonomously only if evidence criteria are met.

### CP-00 - Repository and Branch Safety

Required:

- verify repository;
- verify branch;
- verify HEAD commit;
- verify working tree status;
- verify read-only research mode;
- verify no production write;
- verify no Team B/Team C/Development authorization is implied.

If unsafe, stop as `FAIL / FROZEN`.

### CP-01 - Prior Evidence and Clean-Room Lineage

Required:

- inspect Inventory Reopen prompt, execution branch and 20 deliverables;
- inspect CORR-007B clean-room remediation record;
- classify what can be carried forward;
- classify what needs menu/process depth;
- preserve C-05 as Boss-visible control until independent clean-room re-audit.

### CP-02 - Screenshot Menu Coverage Register

Required:

- enumerate all menus from Boss screenshots;
- classify each menu as `Mandatory / Conditional / Not Applicable / Unknown`;
- map each to Thai candidate name;
- record evidence status.

### CP-03 - Configuration Foundation

Required:

- study settings, warehouses, locations, routes, rules, operation types, storage categories, putaway rules, product categories, attributes, product packaging, reordering rules, barcode nomenclatures and UoM categories;
- explain setup dependencies before transaction processing.

### CP-04 - Product Master and Traceability

Required:

- study products, product variants, product types, UoM, packaging, lots/serial numbers;
- distinguish stockable, consumable and service effects;
- define migration and traceability implications.

### CP-05 - Operations Process Study

Required:

- study replenishment, inventory adjustments, transfers, scrap, landed costs and run scheduler;
- produce end-to-end process maps and exception paths;
- identify stock truth and accounting handoff impact.

### CP-06 - Reporting and Analysis Study

Required:

- study stock, locations, moves history, stock moves, valuation and warehouse analysis;
- distinguish operational reports, management reports, audit reports and accounting support reports.

### CP-07 - Menu Impact Matrix and Handoff Matrix

Required:

- complete the mandatory menu impact matrix;
- complete handoff matrix to Sales, Purchase, Accounting, Manufacturing, Migration and Management Reporting;
- mark all unresolved rows clearly.

### CP-08 - Thai SMEsPlus Process Reference

Required:

- rewrite findings as clean-room Thai SMEsPlus business-process reference;
- separate benchmark facts from SMEsPlus candidate process;
- do not approve final UI, schema, workflow or architecture.

### CP-09 - Ai Audit SMEsPlus Challenge

Required:

- 9 Veto Challenge Council review;
- 9 Special Team Challenge review;
- 4 AI Expert Roles Overlay review;
- list objections and unresolved gaps;
- state conservative verdict.

### CP-10 - Boss Final Gate Package

Required:

- prepare Boss Final Gate package;
- state exactly what is known, unknown, blocked and recommended;
- report `% Board / % STATE / % STEP` only if a verified baseline exists;
- state next recommended prompt/action;
- do not declare PASS.

---

## 14. Required Output Files

Publish all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MENU_DEEP_CHALLENGE_EXECUTION/`

Required files:

1. `00_EXECUTION_CHECKPOINT_LOG.md`
2. `01_PRIOR_EVIDENCE_AND_CLEAN_ROOM_LINEAGE_REGISTER.md`
3. `02_INVENTORY_MENU_COVERAGE_REGISTER.md`
4. `03_INVENTORY_OBJECT_IMPACT_MATRIX.md`
5. `04_INVENTORY_PROCESS_HANDOFF_MAP.md`
6. `05_INVENTORY_SCREENSHOT_MENU_EVIDENCE_REGISTER.md`
7. `06_INVENTORY_MENU_BY_MENU_PROCESS_MAP.md`
8. `07_INVENTORY_MENU_IMPACT_MATRIX.md`
9. `08_CONFIGURATION_FOUNDATION_MAP.md`
10. `09_PRODUCT_MASTER_UOM_TRACEABILITY_MAP.md`
11. `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md`
12. `11_OPERATION_TYPES_AND_STOCK_FLOW_MAP.md`
13. `12_REPLENISHMENT_REORDERING_SCHEDULER_MAP.md`
14. `13_INVENTORY_ADJUSTMENT_SCRAP_CONTROL_MAP.md`
15. `14_TRANSFER_RECEIPT_DELIVERY_HANDOFF_MAP.md`
16. `15_LANDED_COST_VALUATION_ACCOUNTING_HANDOFF_MAP.md`
17. `16_REPORTING_STOCK_LOCATION_MOVE_VALUATION_ANALYSIS_MAP.md`
18. `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md`
19. `18_MIGRATION_DATA_QUALITY_RECONCILIATION_REGISTER.md`
20. `19_SECURITY_PERMISSION_AUDIT_TRAIL_REGISTER.md`
21. `20_CLEAN_ROOM_PROCESS_TRANSFORMATION_REGISTER.md`
22. `21_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md`
23. `22_AI_AUDIT_SMEPLUS_9_SPECIAL_TEAM_CHALLENGE.md`
24. `23_AI_EXPERT_OVERLAY_REVIEW.md`
25. `24_UNKNOWN_CONFLICT_GAP_OWNER_GATE_IMPACT_REGISTER.md`
26. `25_BOSS_FINAL_GATE_PACKAGE.md`
27. `26_NEXT_PROMPT_RECOMMENDATION.md`
28. `27_SHA256_MANIFEST.txt`
29. `28_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md`

If a file cannot be completed due to missing evidence, create the file anyway and mark the affected rows as `HOLD / EVIDENCE REQUIRED`.

---

## 15. Final Gate Rules

At the end of the session, stop at:

`READY FOR BOSS FINAL GATE REVIEW - INVENTORY PROCESS REFERENCE ONLY`

Do not state:

- `PASS`;
- `APPROVED`;
- `CLOSED`;
- `FINAL SOLUTION`;
- `READY FOR DEVELOPMENT`;
- `READY FOR PRODUCTION`;
- `TEAM B AUTHORIZED`;
- `TEAM C AUTHORIZED`.

Allowed terminal classifications:

- `PROCESS REFERENCE PACKAGE PUBLISHED`;
- `HOLD / EVIDENCE REQUIRED`;
- `GAP OWNER ROUTING REQUIRED`;
- `READY FOR BOSS FINAL GATE REVIEW - INVENTORY PROCESS REFERENCE ONLY`.

---

## 16. GitHub Publication Requirement

Before closing the session, publish the prompt/output evidence to GitHub and provide:

1. Repository
2. Branch
3. Commit SHA
4. Direct GitHub link to `25_BOSS_FINAL_GATE_PACKAGE.md`
5. Direct GitHub link to `02_INVENTORY_MENU_COVERAGE_REGISTER.md`
6. Direct GitHub link to `03_INVENTORY_OBJECT_IMPACT_MATRIX.md`
7. Direct GitHub link to `04_INVENTORY_PROCESS_HANDOFF_MAP.md`
8. Direct GitHub link to `06_INVENTORY_MENU_BY_MENU_PROCESS_MAP.md`
9. Direct GitHub link to `07_INVENTORY_MENU_IMPACT_MATRIX.md`
10. Direct GitHub link to `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md`
11. Direct GitHub link to `23_AI_EXPERT_OVERLAY_REVIEW.md`
12. Direct GitHub link to `28_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md`

If GitHub publication fails, do not claim the session is closed.

---

## 17. Starting Instruction for Claude

Start now.

Execute CP-00 first.

Then proceed checkpoint by checkpoint without waiting for Boss confirmation only when the checkpoint evidence criteria are met.

Boss will wait at Final Gate.

Remember:

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss is the sole Final Approver.`  
`Open ERP / Odoo = Process Benchmark Only.`  
`SMEsPlus = New Thai Business Process Reference Candidate, not final solution.`  
`Clean Room means business learning only; no source-code, schema or vendor architecture leakage.`
