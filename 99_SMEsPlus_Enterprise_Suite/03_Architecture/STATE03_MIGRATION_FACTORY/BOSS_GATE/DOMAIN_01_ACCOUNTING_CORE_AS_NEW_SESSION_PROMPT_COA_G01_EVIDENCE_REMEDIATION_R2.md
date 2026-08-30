# [SMEPLUS-26-08-30-COA-G01R2-001]
# COA-G01 Source Baseline Evidence Reconciliation — Controlled Remediation Round 2 / L99.99

## NEW CLAUDE CODE SESSION — CONTROLLED CARRY-FORWARD

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Current Gate: COA-G01 — Source Baseline Reconciliation
Jira: ERPPLUS-132
GitHub: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Boss: Sole Final Approver
Risk Class: HIGH
Prompt Readiness: READY FOR CONTROLLED COA-G01 REMEDIATION ONLY
Control Level: /L99.99

## 1. Session Objective

Remediate and reconcile the remaining COA-G01 evidence gaps for Thailand COA + SaaS context. Produce one controlled Source Baseline whose facts, assumptions, conflicts, Unknowns, provenance and Gate impact are inspectable.

This session executes COA-G01 only.

COA-G01 currently remains `HOLD / EVIDENCE REQUIRED`.

Do not start COA-G02.

## 2. Mandatory Start Sequence

1. Fetch and verify the latest `SMEsPlus` branch before any change.
2. Verify Jira `ERPPLUS-132` and do not change its status, assignee or due date.
3. Read the NEW PROMPT Governance Standard v1.1 completely.
4. Read the Round 2 Pre-Prompt Challenge & Readiness Record completely.
5. Read all existing COA-G01 artifacts and the archived closure before editing.
6. Reconcile existing GitHub evidence before generating new research.
7. Report any new authority conflict, Gate conflict or branch divergence immediately.

## 3. Governing Evidence

- NEW PROMPT Governance Standard v1.1: commit `a1c9395de8f2ca06803187ef81f9f860ff932064`
- Boss approval implementation record: commit `1eefea9188441de5f6da55ffb8ec69e31b90fecd`
- Initial COA closure authorization: commit `e8cc4d942d7f5c611ca3add0266c39196515b636`
- Mandatory COA-G04S amendment: commit `c084a741b22e3352992fbeb0c212cbd1463efb92`
- Cross-Gate SaaS Invariants: commit `e16b29f35d8011723a6e2593994bc226870d9fd7`
- TBRAC standard: commit `d57cca743e6dd31d7dea97486d3b48472336bb74`
- Existing COA-G01 evidence package: commit `00daa7d74478e59e9516593811b9e8fb5344bd2b`
- Existing COA-G01 session closure: commit `e2c7c64277baab52dbdad1e3377d01dc9b46866a`
- Round 2 Pre-Prompt Challenge & Prompt Readiness Record: the immediately preceding controlled GitHub artifact for this Prompt ID

GitHub is the project Source of Record. Chat-only or local-only material is not Gate closure evidence until controlled provenance and GitHub publication are complete.

## 4. Project Identity and Clean-Room Boundary

SMEsPlus is a NEW 100% Clean-room Node.js SaaS ERP.

Odoo, Salesforce, SAP Business One and other ERP systems are reference, learning and benchmark sources only.

This is not an Odoo customization, clone, ORM/schema clone, workflow clone or source-code reuse project.

Absolute rule:

`MIGRATE / LEARN BUSINESS FACTS + BUSINESS SEMANTICS, NOT LEGACY APPLICATION ARCHITECTURE.`

Do not treat absence of source evidence as proof of source architecture. Do not convert source technical structure into SMEsPlus target architecture.

## 5. Approved Accounting Baseline

1. SMEsPlus COA target = Local Thailand.
2. Non-Thai localization COA is outside current COA scope.
3. Boss-approved Odoo18 workbook tab is a primary business-facing reference only.
4. Source Core Account Type universe = 19.
5. SMEsPlus Local Thailand Account Type baseline = 19 ACTIVE types.
6. Off-Balance Sheet is active but excluded from ordinary Balance Sheet/P&L totals by default.
7. Account Group is maintainable per Company but cannot redefine Account Type or canonical accounting meaning.
8. Financial Statement Mapping is independent from Company Account Group.
9. Account Code and Account Name are not canonical identity.
10. `389 source rows != 389 SMEsPlus target accounts`.
11. `~32 Base COA Kernel` is a working expectation only.
12. Exact Base Kernel count = TBD / EVIDENCE REQUIRED.
13. Exact final Standard Thai COA count = TBD / EVIDENCE REQUIRED.
14. Prefer Dimensions over GL account proliferation when accounting treatment is materially equivalent.

The approved 19 active Account Types are:

1. Receivable
2. Bank and Cash
3. Current Assets
4. Non-current Assets
5. Prepayments
6. Fixed Assets
7. Payable
8. Credit Card
9. Current Liabilities
10. Non-current Liabilities
11. Equity
12. Current Year Earnings
13. Income
14. Other Income
15. Expenses
16. Other Expenses
17. Depreciation
18. Cost of Revenue
19. Off-Balance Sheet

## 6. Mandatory Source Universe

Reconcile all authorized source classes. Do not allow one source to become the target architecture.

A. Team A Deep Research / Accounting Core evidence
B. Authorized Accounting Core learning source
C. Thailand localization `l10n_th`
D. Boss-approved Odoo18 workbook tab
E. Boss-provided Thai COA business requirements
F. Boss-provided Thai financial-statement presentation example
G. Existing Boss rulings, PMO evidence and ChatGPT audit evidence
H. Primary Thai regulatory sources where statutory facts are claimed
I. Authoritative cloud/security sources only where generic SaaS facts are claimed

If a source is unavailable, inaccessible or not controlled, retain `EVIDENCE_MISSING`. Do not infer or fabricate it.

## 7. Mandatory Cross-Gate SaaS Invariants

Reconcile SI-01 through SI-10 at G01 evidence-classification scope:

1. SI-01 Tenant context is mandatory.
2. SI-02 Company context is mandatory where company-scoped.
3. SI-03 Standard Template is not tenant-owned mutable data.
4. SI-04 Tenant customization cannot modify the Published Standard Template.
5. SI-05 Account Code / Name is not canonical identity.
6. SI-06 Published Template Version is immutable.
7. SI-07 Upgrade is explicit, previewable and auditable.
8. SI-08 No cross-tenant COA access.
9. SI-09 Company customization must preserve canonical reporting semantics.
10. SI-10 SaaS Core must not hard-code Thailand-specific source architecture.

Re-review all ten. Give special attention to SI-02, SI-05, SI-08 and SI-10. Remove internal contradictions. Do not claim runtime implementation proof at G01.

## 8. Mandatory Remediation Tasks

### 8.1 Current-State Reconciliation

- Create a dated current-state addendum linking historical pre-push/pre-Jira statements to the later published GitHub/Jira state.
- Preserve historical artifacts; do not rewrite history.
- Identify which artifact is current for each operational claim.

### 8.2 Source Class A Completeness

- Inventory substantive Team A Accounting Core evidence in GitHub, including applicable process, state/event, integration, security, edge-case, migration and data evidence.
- Record inclusion, exclusion and relevance rationale.
- Do not treat a summary reference as reconciliation of the underlying evidence.

### 8.3 Local-Only Evidence Boundary

- Identify each local-only source currently cited by GitHub artifacts.
- Port only through controlled provenance when authorized and available.
- Otherwise downgrade the claim to local/source observation, ASSUMPTION, UNKNOWN or EVIDENCE_MISSING as appropriate.
- Do not call local-only evidence Gate-level VERIFIED FACT merely because a local path was reported.

### 8.4 Unknown Register Reconciliation

- Locate the exact 11-item and 20-item registers.
- Compare their paths, definitions, domains, timestamps and denominators.
- Determine whether they are different scopes or conflicting counts.
- Do not report a count mismatch until scope equivalence is proven.

### 8.5 Source Classes E and F

- Search controlled evidence for Boss-provided Thai COA business requirements and Thai P&L/Balance Sheet presentation evidence.
- If not found, retain EVIDENCE_MISSING.
- Do not manufacture a replacement example or assert that an unrelated tax form closes the financial-statement presentation gap.

### 8.6 Workbook Provenance and Row Lineage

- Reconcile the primary Boss-approved Odoo18 workbook, workbook tab, 389-row extraction and resulting concept observations.
- Record file identity, controlled location/hash when available, extraction method, row lineage and limitations.
- Preserve `389 source rows != 389 target accounts`.

### 8.7 Account Concept Completeness

For each significant concept reconcile at minimum:

- Source
- Source Evidence
- Business Meaning
- Thailand Relevance
- Account Type
- Financial Class
- Normal Balance
- Reconciliation behavior
- Tax relevance
- Financial Statement relevance
- System/control dependency
- Base Kernel candidacy
- Canonicalization relevance
- Evidence strength
- Evidence Character
- Conflict / Gap / Unknown
- Clean-room status

Evidence Character is separate from Fact Status and must be one of:

- Source Observation
- Boss Ruling
- Regulatory Verification
- Real-User Validation
- Unclassified / Missing

Fact Status remains one of:

- VERIFIED FACT
- SUPPORTED INFERENCE
- ASSUMPTION
- UNKNOWN
- EVIDENCE_MISSING
- CONFLICTING EVIDENCE

### 8.8 Reconciliation and Process/Control Dependencies

- Reconcile source `reconcile` observations against AR/AP control roles, partial/full reconciliation, payment matching, reversal, clearing and system-generated dependencies where evidence exists.
- Reconcile posting-event origin, cross-module dependency, exception lifecycle, approval/SoD and origin-to-ledger traceability where material to canonicalization.
- Retain unproven behavior as Unknown.

### 8.9 Thailand Reality Control

- Create the Gate-appropriate TBRAC TB-01..TB-13 applicability/compliance matrix.
- Separate source observations, Boss rulings, primary regulatory facts and real-user validation.
- Do not convert Boss experience or vendor behavior into a Thailand-wide verified fact.

### 8.10 Clean-Room Provenance

- Extend provenance review to every COA_STANDARD document used by G01.
- Distinguish coverage gap from proven clean-room violation.
- Verify that source code, ORM, schema, technical IDs and vendor architecture were not copied into the target design.

### 8.11 SI Matrix Re-review

- Reassess SI-01..SI-10 using only Gate-appropriate evidence.
- For SI-08, reconcile the HOLD/not-PASS narrative against the prior PASS/VERIFIED conclusion.
- For SI-10, remove unsupported claims about source deployment architecture unless directly evidenced.
- For SI-05, distinguish canonical concept, template entry, company instance, posting account and source-row identity without designing production identifiers.

### 8.12 Evidence Integrity

- Rebuild the Evidence Manifest and SHA-256 manifest after all controlled updates.
- Record a reproducible verification command/result.
- Create a finding-closure register mapping every Pre-Prompt finding to RESOLVED / OPEN / HOLD / CARRY-FORWARD with evidence.

## 9. Required Outputs

Create or update the existing COA-G01 evidence package and add at minimum:

1. `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`
2. `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md`
3. `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md`
4. `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`
5. `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md`
6. `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md`
7. Updated Source Baseline, Conflict, Unknown, Thai Relevance, Concept Universe, Clean-Room, SI Compliance, Evidence Manifest, Gate Report and SHA-256 evidence.
8. `SESSION_CLOSURE.md` or a controlled Round 2 session closure artifact without deleting historical closure records.

Every artifact must contain:

- Item / Task
- Owner
- Evidence location
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact

## 10. Fact, Evidence and Gate Controls

- Do not convert UNKNOWN into FACT.
- Do not convert a Boss ruling into implementation proof.
- Do not convert source observation into Thai statutory fact.
- Do not merge accounts solely because names are similar.
- Do not use account code/name as canonical identity.
- Preserve material Do-Not-Merge differences in Account Type, BS/P&L treatment, VAT, WHT, CIT, reconciliation, AR/AP role, bank/cash/clearing, inventory valuation, currency/monetary treatment, statutory reporting, retained/current-year earnings, contra behavior, consolidation meaning and system dependency.

## 11. Scope and Carry-Forward Boundary

The following are not G01 deliverables and must remain carry-forward unless separately authorized:

- G04S: production tenancy, provisioning, template versioning, upgrade, rollback, concurrency, idempotency, recovery and privileged-access architecture
- G05: Financial Statement Taxonomy design
- G06: Thailand tax accounting control design and statutory validation
- G07: runtime tenant isolation, multi-company and dimension proof
- Future authorized migration/deep test: row-level balance, reconciliation, concurrency and migration execution tests
- Development: production schema, API, code, build, deployment and release

`Stronger Scope Verification != Automatic Scope Expansion.`

## 12. Mandatory Prohibitions

Do not:

- start COA-G02 or any later Gate;
- freeze Base Kernel or final Standard Thai COA counts;
- design production database schema or APIs;
- code, build, deploy or release;
- copy Odoo/vendor source code, models, classes, tables, ORM or architecture;
- infer missing Thai, statutory, tenancy or security evidence;
- silently expand scope;
- let another Team co-author Team B findings;
- treat five-unit consensus as Boss approval;
- self-approve COA-G01;
- change Jira status, assignee or due date without authority;
- force-push or overwrite concurrent GitHub work.

## 13. Acceptance Criteria

This remediation session may stop for Gate review only when:

1. Every Pre-Prompt finding has a disposition and evidence link.
2. Source Classes A–I are reconciled or explicitly EVIDENCE_MISSING.
3. The 19 Account Types are reconciled with all mandatory concept fields.
4. The 11-versus-20 Unknown issue is scope-reconciled.
5. Workbook provenance and row lineage are explicit.
6. Thai claims include Evidence Character and valid Fact Status.
7. TB-01..TB-13 applicability/compliance is recorded.
8. SI-01..SI-10 are internally consistent at G01 scope.
9. Clean-room provenance covers all COA evidence used.
10. Evidence Manifest and SHA-256 verification are reproducible.
11. GitHub evidence is committed and inspectable.
12. Jira references the exact commit SHA and current Gate recommendation.
13. COA-G02 remains unstarted.

If any closure requirement remains missing, report `HOLD / EVIDENCE REQUIRED`. Do not force a PASS.

## 14. GitHub and Jira Control

GitHub:

- fetch latest branch before writing;
- preserve concurrent changes;
- fast-forward only;
- report exact changed paths and final commit SHA;
- never force-push.

Jira ERPPLUS-132:

- update only after GitHub evidence is inspectable;
- include Prompt ID, GitHub paths, final commit SHA, readiness, current Gate result, blockers, Owner, Timestamp, Verifier and Gate Impact;
- retain `To Do`, `UNASSIGNED` and Due Date `TBD` unless Boss separately authorizes changes.

## 15. Required Final Report to Boss

Report:

1. Latest branch baseline and final commit SHA.
2. All created/updated artifact paths and Direct GitHub Links.
3. Pre-Prompt finding closure summary.
4. Source Classes A–I result.
5. 19 Account Type completeness result.
6. SI-01..SI-10 matrix result.
7. Thai/TBRAC evidence result.
8. Conflicts, Unknowns and EVIDENCE_MISSING items.
9. Clean-room provenance result.
10. Jira comment/update evidence.
11. Gate recommendation requiring Boss decision.
12. Stop Line confirming COA-G02 and Development were not started.

Report `% Board`, `% STATE` and `% STEP` only when an approved denominator exists. Otherwise use `TBD / NO APPROVED BASELINE`.

## 16. Start Command

`START COA-G01 EVIDENCE REMEDIATION ROUND 2.`

Execute only the authorized COA-G01 remediation, publish evidence, update Jira, and STOP for Boss Gate decision.

`No Evidence = No Progress.`

`Never Skip Gate.`

`Boss is the sole Final Approver.`
