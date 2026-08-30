# [SMEPLUS-26-08-30-COA-G01R-001]
# COA-G01 SaaS Evidence Remediation, Context Clarification & Audit Veto Re-review / L99.99

## NEW CLAUDE CODE SESSION - CONTROLLED CARRY-FORWARD

Project: SMEsPlus ENTERPRISE SUITE

STATE: STATE03 - Architecture

Domain: DOMAIN_01 - Accounting Core

Workstream: Thailand COA Architecture Closure

Current Gate: COA-G01 - Source Baseline Reconciliation

Jira: ERPPLUS-132

GitHub: TH-PATTARAKRIT/AI-Collaboration-Hub

Branch: SMEsPlus

Boss: Sole Final Approver

Control Level: /L99.99

## Artifact Control

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Create and publish controlled New Claude Code Session prompt for COA-G01 SaaS evidence remediation | ChatGPT / PMO Secretary | GitHub Branch `SMEsPlus`; this artifact path and commit history | 2026-08-30T15:34:53Z | Boss final authority / ChatGPT GitHub verification | BOSS AUTHORIZED / GITHUB PUBLISHED / VERIFIED | Authorizes G01 remediation only; G02 remains blocked |

## 1. Session Authorization

Boss authorizes a controlled COA-G01 remediation pass for COA + SaaS evidence only.

This authorization does not close COA-G01 and does not authorize COA-G02 or any later Gate.

Authorized work:

1. Record the Boss-approved SaaS Context clarification.
2. Reconcile COA-G01 against SI-01 through SI-10.
3. Remediate evidence gaps at the source-baseline level.
4. Update GitHub evidence and Jira ERPPLUS-132.
5. Stop at the COA-G01 Gate for Boss decision.

Development Authorization = NOT GRANTED.

Production Authorization = NOT GRANTED.

## 2. Project Identity

SMEsPlus is a NEW 100% Clean-room Node.js SaaS ERP.

Odoo, Salesforce, SAP Business One and other ERP platforms are reference, learning and benchmark sources only.

This is not:

- an Odoo customization project;
- an Odoo clone;
- an ORM or schema clone;
- a source-code reuse project;
- a vendor architecture reimplementation project.

Absolute rule:

`MIGRATE / LEARN BUSINESS FACTS + BUSINESS SEMANTICS, NOT LEGACY APPLICATION ARCHITECTURE.`

## 3. Authority Evidence

Verify these artifacts and commits before changing any file:

- Initial COA Closure authorization: `e8cc4d942d7f5c611ca3add0266c39196515b636`
- Mandatory COA-G04S amendment: `c084a741b22e3352992fbeb0c212cbd1463efb92`
- Cross-Gate SaaS Invariants ruling: `e16b29f35d8011723a6e2593994bc226870d9fd7`
- Revised Evidence Index: `79719e6866b6f9277ef8f8d99f42be1ffbdc01da`
- Cross-Gate SaaS Carry-Forward V3: `5c8cf97796223ec798096c5fc3014eb88ae4f608`
- Jira: `ERPPLUS-132`, including comments `10901` through `10903`

Fetch the latest `SMEsPlus` branch first. The branch may contain newer unrelated work. Preserve it and use fast-forward updates only. Never force-push.

Do not assume any prior Work-mode local commit exists in GitHub. GitHub is the project Source of Record.

## 4. Boss-Approved SaaS Context Clarification

Record this clarification as a controlled Boss ruling before using it as closure evidence:

1. `Platform Template administration = Platform Context.`
2. `Tenant-owned or tenant-access operation = Tenant Context mandatory.`
3. `Company-scoped operation = Tenant Context + Company Context mandatory.`
4. A Platform operation must not impersonate a Tenant operation.
5. A Tenant or Company operation must not access or mutate Platform-owned Published Standard Template data.

This clarification resolves the operational boundary between:

- SI-01 Tenant context is mandatory; and
- SI-03 Standard Template is not tenant-owned mutable data.

Recommended ruling artifact:

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AR_BOSS_SAAS_CONTEXT_CLARIFICATION_AND_G01_REMEDIATION_AUTHORIZATION.md`

If `AR` is already used in the latest branch, select the next unused controlled suffix. Do not overwrite an existing ruling.

## 5. Mandatory Cross-Gate SaaS Invariants

Apply these controls to COA-G01 and preserve them for every later Gate:

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

Audit Veto:

- applicable SI violation -> `FAIL / FROZEN`;
- applicable SI evidence missing -> `HOLD / EVIDENCE REQUIRED`;
- `N/A` requires a written Gate-specific justification;
- no Gate may be reported PASS, FROZEN, COMPLETE or READY FOR HANDOFF while an applicable SI remains unresolved.

## 6. Gate-Appropriate Evidence Boundary

COA-G01 is a Source Baseline Gate, not the G04S deep-design Gate.

For G01, determine and record:

- source Tenant/Company ownership assumptions;
- source template mutability and version assumptions;
- source upgrade/delta behavior or evidence gaps;
- source access/coupling behavior that could create cross-tenant risk;
- canonical identity contamination risks from code/name/technical IDs;
- Thailand-specific source architecture that must not enter SaaS Core;
- Company customization effects on canonical reporting semantics.

Do not require G01 to produce production tenancy architecture, physical schema, API, provisioning engine or runtime isolation test proof.

Those deep-design and runtime proofs remain mandatory at COA-G04S and COA-G07.

However, G01 must explicitly classify the source assumptions and retain every missing item as UNKNOWN or EVIDENCE_MISSING.

## 7. Approved Accounting Baseline

- Target COA localization = Local Thailand.
- Non-Thai localization COA = out of current scope.
- Boss-approved Odoo18 workbook tab = primary business-facing reference only.
- Source Core Account Type universe = 19.
- SMEsPlus Local Thailand baseline = 19 ACTIVE Account Types.
- Off-Balance Sheet = active but excluded from ordinary BS/P&L totals by default.
- Account Group may be Company-maintainable but cannot redefine Account Type or canonical meaning.
- Financial Statement Mapping is independent from Company Account Group.
- Account Code and Account Name are not canonical identity.
- `389 source rows != 389 target accounts`.
- `~32 Base Kernel` is a working expectation only.
- Exact Base Kernel count = TBD / EVIDENCE REQUIRED.
- Exact final Standard Thai COA count = TBD / EVIDENCE REQUIRED.
- Prefer Dimensions over GL-account proliferation when accounting treatment is equivalent.

## 8. Evidence Universe

Reconcile existing evidence before conducting new research:

A. Team A Deep Research / Accounting Core evidence

B. Authorized Accounting Core learning source

C. Thailand localization `l10n_th`

D. Boss-approved Odoo18 workbook tab

E. Boss-provided Thai COA business requirements

F. Boss-provided Thai financial-statement presentation evidence

G. Existing Boss rulings, PMO evidence and ChatGPT audit evidence

H. Primary Thai regulatory sources where statutory facts are claimed

I. Authoritative cloud/security sources only where generic SaaS facts are claimed

If source class F is not found, retain `EVIDENCE_MISSING`. Do not create or infer a Thai financial-statement example.

## 9. Mandatory COA-G01 Remediation Tasks

1. Verify Jira/GitHub coordinates and latest branch head.
2. Inspect whether a COA-G01 evidence package already exists in GitHub.
3. Preserve concurrent and unrelated changes.
4. Record the Boss SaaS Context clarification as GitHub evidence.
5. Reconcile every significant accounting concept with Tenant Context relevance and Company Context relevance.
6. Reconcile SI-01 through SI-10 using Gate-appropriate evidence.
7. Remediate SI-01 using the Boss clarification.
8. Investigate and register source evidence/gaps for SI-06, SI-07 and SI-08.
9. Recheck the Thai financial-statement example evidence boundary.
10. Update conflicts, unknowns, clean-room provenance and Evidence Manifest.
11. Run an independent Audit Veto review.
12. Update Jira only after GitHub evidence is committed and inspectable.
13. Stop at COA-G01 and report to Boss.

## 10. Required Artifacts

Create or reconcile these controlled outputs:

1. `COA_G01_SOURCE_BASELINE_REGISTER.md`
2. `COA_G01_SOURCE_CONFLICT_REGISTER.md`
3. `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md`
4. `COA_G01_THAI_RELEVANCE_REGISTER.md`
5. `COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`
6. `COA_G01_OPEN_UNKNOWN_REGISTER.md`
7. `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`
8. `COA_G01_EVIDENCE_MANIFEST.md`
9. `COA_G01_GATE_REPORT.md`
10. `COA_G01_SAAS_INVARIANT_COMPLIANCE.md`
11. `COA_G01_SAAS_CONTEXT_BOUNDARY_REGISTER.md`
12. `COA_G01_TEMPLATE_VERSION_UPGRADE_SOURCE_REGISTER.md`
13. `COA_G01_CROSS_TENANT_SOURCE_OBSERVATION_REGISTER.md`
14. `COA_G01_SHA256SUMS.txt`
15. `SESSION_CLOSURE.md`

Every artifact must contain:

- Item / Task
- Owner
- Evidence location
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact

## 11. Fact and SI Status Control

Fact status must be one of:

- VERIFIED FACT
- SUPPORTED INFERENCE
- ASSUMPTION
- UNKNOWN
- EVIDENCE_MISSING
- CONFLICTING EVIDENCE

SI verification status must be one of:

- PASS / VERIFIED
- HOLD / EVIDENCE REQUIRED
- FAIL / FROZEN
- N/A - JUSTIFICATION REQUIRED

Do not convert UNKNOWN into FACT.

Do not convert a Boss control rule into implementation proof.

## 12. Mandatory Prohibitions

Do not:

- start COA-G02;
- execute COA-G04S deep design;
- start coding;
- design a production database schema;
- implement APIs or provisioning services;
- start Development or Production;
- copy vendor architecture, source code, ORM, model, class or table design;
- use Account Code or Name as canonical identity;
- infer missing statutory or SaaS evidence;
- self-approve any Gate;
- force-push or overwrite concurrent GitHub work;
- mark Jira COMPLETE or PASS without committed evidence and Boss decision.

## 13. Gate Exit Assessment

At the end of this session, classify COA-G01 as one of:

- `PROPOSED PASS / BOSS DECISION REQUIRED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`

Claude must not make the final Gate decision.

COA-G01 may be proposed for PASS only when:

- all mandatory source classes are reconciled;
- every conflict and unknown is registered;
- SI-01 through SI-10 have Gate-appropriate evidence;
- no applicable SI remains HOLD or FAIL;
- clean-room provenance passes;
- Evidence Manifest and SHA-256 manifest are complete;
- GitHub evidence is inspectable;
- Jira references the exact GitHub commit;
- ChatGPT Independent Review can inspect the package.

## 14. Jira and GitHub Update Control

GitHub:

- repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- branch: `SMEsPlus`
- fetch latest before commit;
- fast-forward only;
- report exact commit SHA and changed artifact paths.

Jira:

- issue: `ERPPLUS-132`
- add evidence comment only after GitHub commit exists;
- include Gate result, SI matrix summary, open blockers, commit SHA, Owner, Timestamp, Verifier and Gate Impact;
- do not invent Assignee or Due Date;
- retain `UNASSIGNED / TBD` until Boss provides exact values.

## 15. Required Final Report to Boss

Report:

1. GitHub coordinate verification result.
2. Jira coordinate verification result.
3. Latest branch baseline commit.
4. Boss clarification artifact path and commit.
5. COA-G01 artifact list.
6. SI-01..SI-10 result matrix.
7. Conflicts, unknowns and missing evidence.
8. Thai financial-statement evidence status.
9. GitHub commit SHA.
10. Jira comment/update evidence.
11. Gate recommendation.
12. Explicit Stop Line confirming G02 was not started.

For progress percentages, report `% Board`, `% STATE` and `% STEP` only when an approved denominator and evidence baseline exist. Otherwise report `TBD / NO APPROVED BASELINE`; do not estimate.

## 16. Start Command

`START COA-G01 SAAS EVIDENCE REMEDIATION.`

Execute COA-G01 remediation end-to-end, update GitHub and Jira, then STOP at the COA-G01 Gate for Boss decision.

No Evidence = No Progress.

Never Skip Gate.

Boss is the sole Final Approver.
