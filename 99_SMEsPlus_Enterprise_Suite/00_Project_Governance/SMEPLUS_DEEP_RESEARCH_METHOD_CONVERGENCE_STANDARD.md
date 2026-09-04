# SMEsPlus Deep Research Method Convergence Standard

Standard ID: `SMEPLUS-DR-MC-001`
Status: `BOSS-DECLARED / PROJECT-WIDE RESEARCH STANDARD CANDIDATE ON RESEARCH BRANCH`
Date: `2026-09-04`
Origin: `[SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001]`

## 1. Purpose

Prevent Deep Research from entering an endless correction loop where each review round continues to discover material findings after the previous round declared the finding set complete.

This standard applies to all SMEsPlus Deep Research domains and modules using the project-wide `LEVEL 1 -> LEVEL 12` minimum standard.

Core rule:

> Deep Research is not complete merely because another review round found no veto. The enumeration method itself must demonstrate convergence.

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss is the sole Final Approver.`

## 2. Trigger Condition

Open a Method Convergence Round when any of the following occurs:

1. Two or more review/correction rounds each add material findings after the previous round claimed completeness.
2. Independent Review repeatedly discovers findings that the primary enumeration method did not surface.
3. The count of unknowns, negative-claim corrections, balanced-but-wrong cases, or cross-boundary issues continues to expand materially between rounds.
4. A Gate is blocked because the finding enumeration method has not demonstrated exhaustiveness or stable coverage.
5. A tolerance-zero control area remains affected by an unbounded search space.

Do not respond by opening another broad CORR round automatically.

## 3. Objective

Change the research objective from:

`Find more findings`

to:

`Prove that the defined enumeration universe has been bounded, systematically traversed, and has converged.`

## 4. Required Enumeration Universe

Every module/domain must explicitly define the finite or bounded population being enumerated. At minimum, where applicable:

- Menus
- Screens / views
- Fields
- Actions / buttons
- States / transitions
- Models / entities
- Source files / functions
- Database tables / columns / constraints
- Configuration items
- Security roles / access paths
- Business events
- Accounting or operational events
- Integrations
- Reports
- Scheduled jobs / automations
- Error / exception paths
- Cross-module dependencies
- Tenant/company boundaries
- Migration / historical paths
- Negative claims
- Unknowns
- Contradictions
- Balanced-but-wrong scenarios

Each universe must have a denominator where one can be verified. If no denominator can be proven, mark the population `UNBOUNDED/NOT YET ENUMERABLE` and do not invent a percentage.

## 5. Enumeration Coverage Matrix

Create a canonical matrix with at least:

`Enumeration ID | Population | Verified Denominator | Enumerated Count | Evidence Count | Gap Count | Unknown Count | Last Material Delta | Owner | Status`

Status may only be:

- `NOT STARTED`
- `IN PROGRESS`
- `BOUNDED`
- `ENUMERATED`
- `REVIEWED`
- `CONVERGED`
- `HOLD`

## 6. Convergence Test

A research method may be called `CONVERGED` only when all applicable tests pass:

### MC-01 Population Boundedness
The material research universe is explicitly defined and bounded, or the unbounded remainder is explicitly declared and proven non-gating.

### MC-02 Systematic Enumeration
Coverage comes from deterministic enumeration, not ad-hoc browsing or reviewer discovery alone.

### MC-03 Independent Delta Test
A fresh independent reviewer runs the same bounded scope and returns no new material class of finding.

### MC-04 Repeatability
A second independent pass using the same scope and method produces materially equivalent coverage and conclusions.

### MC-05 Negative Claim Compliance
All material negative claims comply with DR-NC controls. `Not found` is not promoted to `verified absent` without proportional evidence.

### MC-06 Unknown Classification
Every remaining unknown is classified as:

- `GATING`
- `NON-GATING`
- `ROUTED TO LATER WAVE`
- `OUT OF SCOPE WITH EVIDENCE`

### MC-07 Contradiction Closure
All material contradictions are dispositioned with evidence and lineage.

### MC-08 Tolerance-Zero Closure
No unresolved tolerance-zero issue remains.

### MC-09 Evidence Lineage
Every material conclusion is traceable to evidence, correction lineage, and final disposition.

### MC-10 New-Finding Delta Threshold
A fresh review adds no material finding that changes architecture, financial/operational semantics, control design, SaaS boundary, migration requirement, or Gate recommendation.

A zero count of trivial editorial deltas is not required. Material semantic/control deltas are the convergence criterion.

## 7. Review Round Rules

A review round must report separately:

- New material findings
- New non-material findings
- Corrections
- Rescoped claims
- Retracted claims
- New unknowns
- Closed unknowns
- New finding classes

If a fresh round discovers a new material finding class, convergence is `NOT ACHIEVED`.

If findings are only instances of an already enumerated class and do not change semantics/control/Gate disposition, they do not automatically break convergence; record them as instance-level delta.

## 8. Stopping Rule

Do not continue broad review indefinitely.

When convergence is not achieved, identify the exact enumeration defect and correct the method rather than opening a generic correction round.

Examples:

- Missing population denominator
- Missing source surface
- Incomplete cross-module boundary
- UI-only enumeration without source/database correlation
- Reviewer-only discovery channel
- Missing state/transition enumeration
- Missing tenant/company dimension
- Missing failure-path taxonomy

## 9. Mandatory Outputs

Every Method Convergence Round must produce:

1. `*_METHOD_CONVERGENCE_SCOPE.md`
2. `*_ENUMERATION_UNIVERSE_REGISTER`
3. `*_ENUMERATION_COVERAGE_MATRIX`
4. `*_MATERIAL_DELTA_REGISTER`
5. `*_UNKNOWN_CLASSIFICATION_REGISTER`
6. `*_CONVERGENCE_TEST_MC01_MC10.md`
7. `*_FRESH_INDEPENDENT_CONVERGENCE_REVIEW.md`
8. `*_METHOD_CONVERGENCE_GATE_REPORT.md`

## 10. Gate Rule

Allowed recommendation only:

- `RECOMMEND PASS`
- `RECOMMEND CONDITIONAL PASS`
- `RECOMMEND HOLD`
- `RECOMMEND FAIL`

For any tolerance-zero boundary, `CONDITIONAL PASS` may not be used to bypass unresolved integrity risk.

The research team may recommend a Gate status but may not declare Final Approval or Final Freeze.

## 11. Cross-Module Adoption

This standard is reusable for all SMEsPlus Deep Research modules, including Accounting, Inventory, Purchase, Sale, Manufacturing, CRM, Project, HR, Approval, Document, Payment, and future domains.

Domain-specific enumeration populations may be added, but MC-01 through MC-10 may not be weakened without Boss approval.

## 12. Practical Sequence for Other Modules

`L1-L12 Deep Research`
-> `Independent Review`
-> `Correction/Reconciliation if required`
-> `Targeted Gap Closure`
-> `Method Convergence Round if repeated material additions occur`
-> `Fresh Independent Convergence Review`
-> `Boss Final Research Gate`

Do not automatically repeat CORR rounds when the true defect is non-convergent enumeration.
