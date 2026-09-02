# [SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001]
# Account Menu-by-Menu Process Deep Study for Thai SMEsPlus / Claude Sonnet 5 Max / L999.999

## SINGLE END-TO-END NEW SESSION PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 - Architecture`  
Domain: `ACCOUNT / Accounting Process / Reporting / Configuration / Thai Business UX`  
Jira: `ERPPLUS-138`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Target Executor: `Claude Sonnet 5 Max`  
Execution Mode: `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / MENU-BY-MENU / CHECKPOINT-CONTROLLED / L999.999`  
Boss: `Sole Final Approver at Final Gate`

This is a corrective New Session Prompt. The prior Account audit rounds were useful for evidence-gap detection, but the depth is not sufficient for a real Account process study. This session must study Account menu-by-menu, understand process handoffs, and produce a Thai SMEsPlus reference package for later design consideration.

This session is **not** a Final Solution for SMEsPlus.  
This session is **not** a development authorization.  
This session is **not** a Gate PASS.  
This session is a controlled reference study to support future Thai SMEsPlus accounting design decisions.

---

## 1. Mission

Study Open ERP / Odoo-style accounting menus as a **process benchmark only**, then rebuild the understanding into a new Thai SMEsPlus business-process reference.

The executor must identify:

1. each accounting menu or functional area;
2. what business purpose it serves;
3. what input it receives;
4. what user action or system action occurs;
5. what output it creates;
6. what downstream process receives the output;
7. whether it impacts GL, TB, Stock, P&L, BS, Cash Flow, Tax, Management Reports or Audit Reports;
8. which controls are required;
9. what evidence exists;
10. what remains unknown.

The final output must help Boss and Ai Audit SMEsPlus decide how SMEsPlus should design Thai accounting process flows later.

---

## 2. Absolute Clean-room Boundary

Open ERP / Odoo / other ERP systems may be used only as:

- `PROCESS BENCHMARK`;
- `MENU COVERAGE CHECKLIST`;
- `BUSINESS CAPABILITY REFERENCE`;
- `RISK DISCOVERY SOURCE`.

Hard prohibitions:

1. Do not copy source code.
2. Do not copy ORM models.
3. Do not copy database schema.
4. Do not copy workflow as implementation architecture.
5. Do not copy menu names as final SMEsPlus names.
6. Do not claim SMEsPlus must follow Open ERP / Odoo behavior.
7. Do not treat benchmark behavior as approved SMEsPlus design.

Required transformation:

`Benchmark Menu -> Business Meaning -> Thai User Language -> SMEsPlus Candidate Process -> Evidence / Gap / Gate Impact`

---

## 3. Thai Business UX Naming Rule

SMEsPlus is for Thai users. Menu and report names must be understandable to Thai accounting, finance, management and SME users.

The executor must produce Thai candidate names for every menu/report studied.

Examples:

| Benchmark Term | Thai Candidate Name |
|---|---|
| General Ledger | สมุดบัญชีแยกประเภท |
| Trial Balance | งบทดลอง |
| Balance Sheet | งบฐานะการเงิน |
| Profit and Loss | งบกำไรขาดทุน |
| Cash Flow Statement | งบกระแสเงินสด |
| Journal Entries | รายการสมุดรายวัน |
| Journal Items | รายการบัญชีรายบรรทัด |
| Partner Ledger | รายงานลูกหนี้/เจ้าหนี้รายตัว |
| Aged Receivable | รายงานอายุลูกหนี้ |
| Aged Payable | รายงานอายุเจ้าหนี้ |
| WT Income Tax Report | รายงานภาษีหัก ณ ที่จ่าย |
| Depreciation Schedule | ตารางค่าเสื่อมราคา |

These Thai names are candidates only. They are not final approved SMEsPlus UI labels.

---

## 4. Ai Audit SMEsPlus Structure

`Ai Audit SMEsPlus = 9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Roles Overlay.`

The executor must keep these layers separate.

| Layer | Count | Role |
|---|---:|---|
| `9 Veto Challenge Council` | 9 | Primary challenge body for Gate risk, contradiction and no-evidence control |
| `9 Special Team Challenge` | 9 | Deep-dive body for specific accounting, tax, reporting, migration and control risks |
| `4 AI Expert Roles` | 4 | Overlay review only; not a primary team and not a substitute for 9+9 |

Every major conclusion must include:

- 9 Veto Challenge Council comments;
- 9 Special Team Challenge comments;
- 4 AI Expert Roles Overlay comments;
- unresolved objections;
- required evidence before Gate movement.

---

## 5. Mandatory Study Sequence

The executor must study in this order. Do not jump directly to financial statement conclusions.

```text
Configuration
-> Transaction
-> Posting
-> General Ledger
-> Reconciliation
-> Trial Balance
-> Period Close
-> Financial Reports
-> Tax / Audit / Management Reports
-> Thai SMEsPlus Process Reference
-> Boss Final Gate Package
```

### 5.1 First Three Mandatory Analytical Files

Before any summary, conclusion, recommendation or Boss Final Gate package, the executor must create and populate these three analytical files first:

1. `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`
2. `03_ACCOUNT_OBJECT_IMPACT_MATRIX.md`
3. `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`

Hard rule:

- If these three files are missing, the session is not deep enough.
- If any row in these files has blank evidence, owner, verifier or Gate impact, mark it `HOLD / EVIDENCE REQUIRED`.
- Do not write `21_BOSS_FINAL_GATE_PACKAGE.md` until the three files above exist and are internally consistent.
- Do not claim `Deep Study Complete` until these three files have been challenged by `Ai Audit SMEsPlus`.

---

## 6. Mandatory Menu Coverage

### 6.1 Configuration Base

Study and map:

1. Chart of Accounts
2. Account Groups
3. Account Tags
4. Taxes
5. Tax Groups
6. Tax Units
7. Fiscal Years
8. Fiscal Positions
9. Currencies
10. Journals
11. Journal Groups
12. Horizontal Groups
13. Accounting Reports
14. Sources

### 6.2 Invoicing and Partner Configuration

Study and map:

1. Payment Terms
2. Follow-up Levels
3. Incoterms
4. Withholding Tax
5. Cheque Format

### 6.3 Journal and Posting Layer

Study and map:

1. Journal Entries
2. Journal Items
3. Journal Report
4. Manual Journal Entry process
5. System-generated Journal Entry process
6. Debit/Credit balancing
7. Multi-company posting
8. Multi-currency posting
9. Period/date control
10. Reversal/correction entries

### 6.4 Bank, Cash and Reconciliation

Study and map:

1. Add a Bank Account
2. Bank transactions
3. Reconciliation Models
4. Online Synchronization
5. Cash/Bank GL impact
6. AR/AP clearing
7. Reconciliation status
8. Unreconciled item aging

### 6.5 AR/AP and Partner Ledger

Study and map:

1. Customer Invoice
2. Vendor Bill
3. Credit Note
4. Debit Note
5. Receipt
6. Payment
7. Partner Ledger
8. Aged Receivable
9. Aged Payable
10. Follow-up process
11. Bad debt / allowance / contra impact

### 6.6 Product, Stock, COGS and Account Boundary

Study and map by object:

1. Storable Product
2. Service Product
3. Consumable Product
4. Product Categories
5. Stock valuation
6. COGS
7. Inventory asset
8. Price difference
9. Account to Inventory handoff
10. Inventory to Account handoff

### 6.7 Asset, Depreciation and Deferred Recognition

Study and map:

1. Assets
2. Asset Models
3. Depreciation Schedule
4. Accumulated depreciation
5. Asset disposal
6. Deferred Revenues
7. Deferred Revenue Models
8. Deferred Expenses
9. Deferred Expense Models
10. Recognition schedule

### 6.8 Analytic Accounting and Budget

Study and map:

1. Analytic Items
2. Analytic Accounts
3. Analytic Plans
4. Analytic Distribution Models
5. Budgets
6. Budgetary Positions
7. Budget Analysis
8. Management dimension reporting

### 6.9 Financial Statement and Reporting

Study and map:

1. General Ledger
2. Trial Balance
3. Balance Sheet
4. Profit and Loss
5. Cash Flow Statement
6. Executive Summary
7. Tax Report
8. WT Income Tax Report
9. EC Sales List, only to classify as Thailand-fit / not Thailand-fit / not applicable
10. Invoice Analysis
11. Unrealized Currency Gains/Losses
12. Management Reports

### 6.10 Control Layer

Study and map:

1. Lock Dates
2. Close Period
3. Open Period
4. Year-end Close
5. Retained Earnings
6. Opening Balance
7. Audit Trail
8. Approval requirement
9. Reversal control
10. User role / segregation of duties

---

## 7. Mandatory Impact Matrix

For every menu, object, process and report, create an impact matrix with at least these columns:

| Field | Required |
|---|---|
| ID | Required |
| Benchmark menu/function | Required |
| Thai candidate name | Required |
| Business purpose | Required |
| Input | Required |
| Action | Required |
| Output | Required |
| Handoff to next process | Required |
| GL impact | Required: Y/N/Conditional |
| TB impact | Required: Y/N/Conditional |
| Stock impact | Required: Y/N/Conditional |
| P&L impact | Required: Y/N/Conditional |
| BS impact | Required: Y/N/Conditional |
| Cash Flow impact | Required: Y/N/Conditional |
| Tax impact | Required: Y/N/Conditional |
| Management report impact | Required: Y/N/Conditional |
| Audit/control impact | Required: Y/N/Conditional |
| Evidence location | Required or mark HOLD |
| Owner | Required or UNASSIGNED |
| Verifier | Required or UNVERIFIED |
| Gate impact | Required |
| Status | `COVERED / PARTIAL / GAP / HOLD / NOT APPLICABLE` |

Do not use blank cells. If unknown, write `UNKNOWN / EVIDENCE REQUIRED`.

---

## 8. Mandatory Object Impact Examples

The executor must expand this concept across all relevant accounting objects:

| Object / Transaction | GL | TB | Stock | P&L | BS | Report | Notes |
|---|---|---|---|---|---|---|---|
| Storable Product | Y | Y | Y | Y | Y | Y | Inventory valuation, COGS, inventory asset |
| Service Product | Y | Y | N | Y | Y | Y | Revenue/expense, no stock quantity movement |
| Consumable Product | Y | Y | Conditional | Y | Y | Y | Must classify expense vs inventory treatment |
| Asset | Y | Y | N | Y | Y | Y | Depreciation and accumulated depreciation |
| Deferred Revenue | Y | Y | N | Y | Y | Y | Revenue recognition |
| Deferred Expense | Y | Y | N | Y | Y | Y | Expense recognition |
| Customer Invoice | Y | Y | N | Y | Y | Y | AR, revenue, tax |
| Vendor Bill | Y | Y | Conditional | Y | Y | Y | AP, expense/stock, tax |
| Bank Transaction | Y | Y | N | Conditional | Y | Y | Cash/bank and reconciliation |

This table is a seed only. The executor must expand it from evidence and studied menu coverage.

---

## 9. Mandatory CheckPoints

Boss will wait at the Final Gate. Intermediate checkpoints may proceed autonomously only if evidence criteria are met.

### CP-00 - Repository and Branch Safety

Required:

- verify repository;
- verify branch;
- verify HEAD commit;
- verify working tree status;
- verify read-only research mode;
- verify no Inventory branch contamination;
- verify no production write.

If unsafe, stop as `FAIL / FROZEN`.

### CP-01 - Prior Evidence and Prompt Lineage

Required:

- inspect prior Account Reopen / Ai Audit SMEsPlus prompt and deliverables where available;
- record which prior findings are usable;
- record which prior findings are insufficient for deep process study;
- keep prior Account terminal state as `HOLD / EVIDENCE REQUIRED` unless Boss changes it.

### CP-02 - Benchmark Coverage Extraction

Required:

- enumerate all Account benchmark menus from provided screenshots and available evidence;
- classify each menu as `Mandatory / Conditional / Not Applicable / Unknown`;
- do not declare any item complete without evidence.

### CP-03 - Menu-by-Menu Process Study

Required:

- study each menu in sequence;
- produce input/action/output/handoff/control summary;
- identify Thai candidate name;
- identify accounting impact.

### CP-04 - Object and Transaction Impact Matrix

Required:

- produce object/transaction impact matrix;
- include product types, invoices, bills, payments, assets, deferred items, taxes, bank, journal entries and reconciliations;
- map each to GL, TB, Stock, P&L, BS, Cash Flow, Tax and Reports.

### CP-05 - Thai SMEsPlus Process Reference

Required:

- rewrite findings as Thai SMEsPlus business-process reference;
- separate benchmark facts from SMEsPlus candidate process;
- do not approve final UI, schema, workflow or architecture.

### CP-06 - Ai Audit SMEsPlus Challenge

Required:

- 9 Veto Challenge Council review;
- 9 Special Team Challenge review;
- 4 AI Expert Roles Overlay review;
- list objections and unresolved gaps.

### CP-07 - Final Gate Package

Required:

- prepare Boss Final Gate package;
- state exactly what is known, unknown and blocked;
- state next recommended prompt/action;
- do not declare PASS.

---

## 10. Required Output Files

Publish all outputs under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/MENU_PROCESS_DEEP_STUDY_EXECUTION/`

Required files:

1. `00_EXECUTION_CHECKPOINT_LOG.md`
2. `01_PRIOR_EVIDENCE_AND_LINEAGE_REGISTER.md`
3. `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`
4. `03_ACCOUNT_OBJECT_IMPACT_MATRIX.md`
5. `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`
6. `05_ACCOUNT_MENU_BY_MENU_PROCESS_MAP.md`
7. `06_ACCOUNT_OBJECT_TRANSACTION_IMPACT_MATRIX_DETAILED.md`
8. `07_GL_TB_POSTING_TRACEABILITY_MATRIX.md`
9. `08_STOCK_COGS_ACCOUNT_BOUNDARY_MATRIX.md`
10. `09_FINANCIAL_STATEMENT_REPORTING_MAP.md`
11. `10_TAX_WHT_VAT_CIT_REPORTING_MAP.md`
12. `11_AR_AP_PARTNER_LEDGER_AGING_MAP.md`
13. `12_ASSET_DEFERRED_RECOGNITION_MAP.md`
14. `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md`
15. `14_CONTROL_LOCK_RECONCILIATION_AUDIT_TRAIL_MAP.md`
16. `15_THAI_MENU_AND_REPORT_NAMING_REGISTER.md`
17. `16_CLEAN_ROOM_PROCESS_TRANSFORMATION_REGISTER.md`
18. `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md`
19. `18_AI_AUDIT_SMEPLUS_9_SPECIAL_TEAM_CHALLENGE.md`
20. `19_AI_EXPERT_OVERLAY_REVIEW.md`
21. `20_GAP_OWNER_GATE_IMPACT_REGISTER.md`
22. `21_BOSS_FINAL_GATE_PACKAGE.md`
23. `22_NEXT_PROMPT_RECOMMENDATION.md`
24. `23_SHA256_MANIFEST.txt`
25. `24_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md`

If a file cannot be completed due to missing evidence, create the file anyway and mark the affected rows as `HOLD / EVIDENCE REQUIRED`.

---

## 11. Final Gate Rules

At the end of the session, stop at:

`READY FOR BOSS FINAL GATE REVIEW - PROCESS REFERENCE ONLY`

Do not state:

- `PASS`;
- `APPROVED`;
- `CLOSED`;
- `FINAL SOLUTION`;
- `READY FOR DEVELOPMENT`;
- `READY FOR PRODUCTION`.

Allowed terminal classifications:

- `PROCESS REFERENCE PACKAGE PUBLISHED`;
- `HOLD / EVIDENCE REQUIRED`;
- `GAP OWNER ROUTING REQUIRED`;
- `READY FOR BOSS FINAL GATE REVIEW - PROCESS REFERENCE ONLY`.

---

## 12. GitHub Publication Requirement

Before closing the session, publish the prompt/output evidence to GitHub and provide:

1. Repository
2. Branch
3. Commit SHA
4. Direct GitHub link to `21_BOSS_FINAL_GATE_PACKAGE.md`
5. Direct GitHub link to `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`
6. Direct GitHub link to `03_ACCOUNT_OBJECT_IMPACT_MATRIX.md`
7. Direct GitHub link to `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`
8. Direct GitHub link to `24_SESSION_CLOSURE_SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001.md`

If GitHub publication fails, do not claim the session is closed.

---

## 13. Starting Instruction for Claude

Start now.

Execute CP-00 first.

Then proceed checkpoint by checkpoint without waiting for Boss confirmation only when the checkpoint evidence criteria are met.

Boss will wait at Final Gate.

Remember:

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss is the sole Final Approver.`  
`Open ERP / Odoo = Process Benchmark Only.`  
`SMEsPlus = New Thai Business Process Design Candidate, not final solution.`  
