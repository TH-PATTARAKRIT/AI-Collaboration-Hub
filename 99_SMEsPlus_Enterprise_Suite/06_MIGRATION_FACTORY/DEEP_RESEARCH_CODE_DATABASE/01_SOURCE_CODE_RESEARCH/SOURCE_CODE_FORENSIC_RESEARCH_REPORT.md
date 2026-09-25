# Source Code Forensic Research Report

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Status: `REVIEWED WITH CONTROL / CURRENT SOURCE BASELINE HOLD`  
Prepared Role: Enterprise Functional Architect & Clean-Room Systems Analyst  
Final Approver: Boss

## 1. Research Boundary

This report records source-code learning only. Odoo, third-party modules, and legacy implementations are reference artifacts. No class hierarchy, ORM pattern, module packaging, method body, workflow engine, or proprietary algorithm is authorized for transfer into SMEsPlus.

Permitted transformation:

```text
Observed source fact
-> independently interpreted business semantic
-> vendor-neutral invariant
-> independently designed SMEsPlus specification
```

Prohibited transformation:

```text
Odoo class/model/method
-> renamed SMEsPlus class/table/service
```

## 2. Source Evidence Position

### 2.1 Historical source baseline verified

The inspectable Phase B evidence package records:

- `01 ACCOUNT.zip`: 62 detected modules
- `02 OTHER.zip`: 1,374 detected modules
- Combined historical source baseline: 1,436 modules
- Detected ORM/model records: evidence exists in `Detected_ORM_Models.csv`
- Business-rule/method records: 4,377 records in `Business_Rule_Method_Inventory.csv`
- XML/view/action/menu records: 6,260
- Security/access records: 473

Primary historical artifacts:

- `Module_Inventory.csv`
- `Detected_ORM_Models.csv`
- `ORM_Field_Inventory.csv`
- `Business_Rule_Method_Inventory.csv`
- `XML_View_Action_Menu_Inventory.csv`
- `Security_Access_Inventory.csv`

### 2.2 Current source baseline not verified

The current Session states a working source manifest of 1,502 records with classification:

- CLASS-A: 19
- CLASS-B: 710
- CLASS-C: 761
- CLASS-D: 12

These figures are retained as `BOSS-PROVIDED WORKING BASELINE`, not as a verified research result. The current archive bodies, archive hashes, current manifest, classification register, and the delta from 1,436 to 1,502 have not been independently inspected in this execution environment.

Required reconciliation:

```text
1,502 current working records
- 1,436 historical verified records
= 66 records requiring explicit lineage
```

No claim is made that the 66 records are additions, replacements, duplicates, moved modules, or extra modules until an inspectable manifest and SHA-256 evidence exist.

## 3. License and Research Treatment

Historical manifest evidence shows mixed license positions, including LGPL-3 and OEEL-1. Therefore source treatment is controlled as follows:

| Class | Allowed Treatment | Prohibited Treatment |
|---|---|---|
| CLASS-A | Public-domain/general business principle research; evidence-backed source observation | Copying implementation or schema |
| CLASS-B | Semantic and behavioral learning with evidence references | Structural translation into target code |
| CLASS-C | Black-box behavior, input/output, lifecycle, and business semantic learning only | Source-body extraction into target design |
| CLASS-D | Quarantine | Any source-body research without Boss ruling |

CLASS-D remains quarantined for all 12 working-baseline modules.

## 4. Evidence-Backed Functional Observations

The source inventory proves the existence of broad accounting and operational capability surfaces. Examples from `Business_Rule_Method_Inventory.csv` include:

### 4.1 Accounting and journal control

Observed method names indicate capability areas for:

- journal posting and payment posting
- lock-date changes
- payment-term computation and validation
- tax repartition validation
- reconciliation matching
- journal resequencing
- accrual and reversal preparation
- customer follow-up and unpaid-invoice views
- trial-balance and general-ledger audit navigation
- multicurrency revaluation workflow entry points

These names prove the existence of behavior surfaces. They do not prove the exact algorithm, state transition, or target-system rule.

### 4.2 Payments and reconciliation

Observed evidence includes payment posting, refund-boundary checks, pending-refund checks, payment-provider linkage, invoice/payment references, and reconciliation matching tests. This supports the semantic conclusion that payments, refunds, allocation, and reconciliation are distinct business concerns.

### 4.3 Assets

Observed evidence includes depreciation values, depreciable value, salvage value, prorata date, disposal date, pause/resume-related fields, asset-linked moves, and gain/loss concepts. This supports a vendor-neutral asset lifecycle containing acquisition, activation, depreciation, pause, modification, disposal, and closure.

### 4.4 Tax and reporting

Observed evidence includes tax repartition checks, report-line consistency, cash-flow liquidity balance, trial-balance audit actions, tax returns, branch/company restrictions, and multicurrency revaluation entry points. This supports independent specification of tax determination, reporting periods, report snapshots, audit drill-down, and revaluation controls.

### 4.5 Intercompany behavior

Field-mapping evidence contains intercompany document state, automatic invoice references, purchase journal, responsible user, and company-level settings. This supports a semantic requirement for intercompany document linkage and reciprocal document controls. It does not authorize reuse of the legacy automation design.

## 5. Source Architecture Findings

### 5.1 What may be learned

- capability existence
- actor and document intent
- input and output business facts
- state names where corroborated by data or behavior evidence
- validations and business exceptions
- cross-domain dependency semantics
- reporting and statutory information requirements

### 5.2 What must not become target architecture

- module names and module boundaries
- ORM inheritance
- model mixins
- table naming conventions
- computed-field mechanisms
- framework decorators
- wizard/transient-model patterns
- RPC/controller conventions
- source method decomposition
- proprietary workflow or report engine structure

## 6. Source Research Verdict

| Control | Result |
|---|---|
| Historical module inventory | PASS |
| Historical business-method inventory | PASS |
| Historical XML/security inventory | PASS |
| Current 1,502-record manifest | HOLD |
| Current archive SHA-256 identity | HOLD |
| Current A/B/C/D classification register | HOLD |
| CLASS-D quarantine | PASS |
| Clean-room transfer boundary | PASS WITH CONTROL |

Source-code research may support semantic learning and an independent blueprint, but current-source completeness and all-module coverage cannot be certified.

## 7. Gate Impact

`DR2 SOURCE CODE DEEP RESEARCH = HOLD FOR CURRENT BASELINE CERTIFICATION`

Historical evidence is usable as a controlled learning baseline. Any statement that all 1,502 current records were deeply researched is prohibited until the current manifest, archive hashes, lineage, and classification are inspectable and independently reviewed.
