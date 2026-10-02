# STATE03 Progress Reporting Constitution

Document ID: `STATE03-PROGRESS-REPORTING-CONSTITUTION`  
Version: 1.0  
Effective Date: 2026-09-29  
Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture & Knowledge Acquisition  
Authority: Boss Direct Order  
Status: ACTIVE / GOVERNING UNTIL SUPERSEDED  
Boss: Sole Final Approver for changes to this constitution

## 1. Purpose

This constitution defines the mandatory progress-reporting format for STATE03.

The primary management objective is to let Boss see, at a glance, which business module/function is closest to research completion, what remains, and what should be focused next.

Progress reporting must therefore be module/function-oriented first, not Gx-number-oriented.

Gx references remain supporting traceability only.

## 2. Mandatory Dashboard

Every STATE03 progress report must use the following core columns:

| FUNCTION / MODULE | RESEARCH % | RESEARCH STATUS | RECAP | FUNCTION COMPARE % | EVIDENCE % | GAP | CURRENT STATE | NEXT STATE |
|---|---:|---|---|---:|---:|---|---|---|

Typical module rows include, as applicable:

- Sales
- Purchase
- Inventory
- Accounting
- Manufacturing
- Quality
- Maintenance
- Fixed Asset
- HRM / Payroll
- Partner
- Product
- Document
- Approval
- Event
- Tenant / Multi-company
- IAM
- Platform Foundation
- Engineering / Delivery

## 3. Research Status Values

Use only controlled status values:

- `NOT STARTED`
- `IN PROGRESS`
- `NEAR COMPLETE`
- `DONE`
- `HOLD`

`RESEARCH STATUS = DONE` means only that the defined research scope for that module/function has been completed.

It does **not** mean:

- AWT complete
- Independent Audit passed
- PMO verification complete
- Boss Gate passed
- Module Final Done
- STATE03 complete
- Functional Design authorized

## 4. Percentage Rules

No percentage may be estimated by intuition.

Each percentage must be supported by a valid denominator and evidence.

### RESEARCH %

Represents completion of the defined research population for that module/function.

### FUNCTION COMPARE %

Represents completion of function-by-function comparison / reconciliation against the approved comparison population.

### EVIDENCE %

Represents completion of the required evidence population for that module/function and must respect evidence-tier distinctions.

Documentation Evidence must not be counted as Runtime Evidence.

Source presence must not be counted as Runtime Reachability.

If the denominator is not valid/frozen enough to calculate a defensible percentage, show:

`N/A — DENOMINATOR NOT VALIDATED`

or

`PENDING DENOMINATOR`

instead of inventing a number.

## 5. Management Reading Order

Boss should be able to read the dashboard in this order:

1. `RESEARCH %`
2. `RESEARCH STATUS`
3. `RECAP`
4. `FUNCTION COMPARE %`
5. `EVIDENCE %`
6. `GAP`
7. `CURRENT STATE`
8. `NEXT STATE`

The dashboard must answer immediately:

- Which module is closest to Research DONE?
- Which module is currently being studied?
- Which module is now in Function Comparison?
- Which module is blocked by evidence?
- Which gap can be closed next?
- What should the team focus on next?

## 6. Focus Rule

STATE03 execution should preferentially close work that is nearest to a valid completion state, without stopping independent research elsewhere.

Default prioritization:

`Near DONE → Close remaining GAP → Function Compare → Evidence/Audit → Module closure candidate → Next module`

This prioritization must not override:

- Zero-Tolerance controls
- C1 critical risk
- cross-module blockers
- Clean-Room requirements
- Boss-only gates

## 7. Module-Oriented Reporting Rule

When Boss asks:

- “STATE03 ถึงไหนแล้ว”
- “เสร็จไปกี่โมดูลแล้ว”
- “Sale ถึงไหน”
- “Purchase กำลังทำอะไร”
- “ตัวไหนใกล้เสร็จที่สุด”

the first response must be the module/function progress dashboard.

Do not lead with G01–G16, Lane C scenario numbers, PR file counts, commit counts, or document counts unless Boss specifically asks for those details.

Those remain supporting detail only.

## 8. Gx Traceability Rule

Gx identifiers may be displayed as secondary traceability.

They must never replace the business module/function view.

Different Gx systems must not be mixed:

- STATE03 Lane C Gx
- OVQDT / GMVQ G01–G16
- other future Gx classifications

Each must preserve its own denominator and scope.

## 9. Current State / Next State

`CURRENT STATE` must describe the real work stage, for example:

- Deep Research
- Function Comparison
- Evidence Reconciliation
- Cross-Module Validation
- AWT Preparation
- AWT Pending
- Independent Audit
- PMO Verification
- Boss Gate

`NEXT STATE` must state the next legitimate stage based on current evidence and governance.

## 10. Gap Reporting

`GAP` must be concise enough for dashboard reading but traceable to the detailed Gap Register.

Examples:

- Runtime proof pending
- Source cross-validation pending
- Independent audit pending
- Function denominator incomplete
- Clean-Room re-audit pending
- Cross-module contradiction unresolved
- No material gap

A gap must block only the work that actually depends on it.

## 11. No False Completion

The following are prohibited:

- showing `100%` without a defensible denominator;
- calling a module `DONE` because documentation-only research finished when required source/runtime proof remains;
- using an average percentage to hide an under-threshold applicable dimension;
- treating research completion as Gate completion;
- mixing different Gx denominators;
- equating file count or question count with research completion.

## 12. Governing Threshold

Where the SMEsPlus governing threshold applies:

- each applicable coverage dimension must meet the current minimum floor;
- Critical / Zero-Tolerance controls retain their stricter requirement;
- unresolved critical gaps, contradictions, missing mandatory proof, or invalid denominator prevent final completion claims.

## 13. Progress Report Output

Each formal STATE03 progress report should contain:

### A. Executive Dashboard
The mandatory module/function table.

### B. Focus Queue
Top modules/functions closest to legitimate completion.

### C. Critical Gaps
Only gaps materially affecting progress.

### D. Audit / Gate Queue
Independent Audit, PMO, or Boss-only decisions.

### E. Delta Since Last Report
What changed since the prior report.

## 14. Change Control

This document is the governing STATE03 progress-reporting constitution until explicitly changed.

No AI agent, PMO sub-team, Claude Code session, or audit team may silently replace this reporting model.

Changes require:

1. explicit Boss instruction;
2. version increment;
3. recorded change rationale;
4. update to the applicable STATE03 governance register.

Until such change is approved:

`THIS FORMAT REMAINS MANDATORY.`

## 15. Governing Principle

`Research Progress must be visible by business module/function first.`

`Boss must be able to see what is nearly finished and what should be focused next without reading the underlying Gx machinery.`

`Evidence determines progress; activity volume does not.`
