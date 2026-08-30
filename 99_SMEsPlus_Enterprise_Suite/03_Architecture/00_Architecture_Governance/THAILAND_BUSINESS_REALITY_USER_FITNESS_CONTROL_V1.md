# SMEsPlus Thailand Business Reality & User Fitness Control V1

Document ID: SMEPLUS-26-08-30-TBRUF-001
Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
Control Level: /L99.99
Status: BOSS APPROVED CONTROL BASELINE
Jira: ERPPLUS-134
Final Approval Authority: Boss
Independent Challenge Function: Thailand Business Reality & Adoption Council (TBRAC)

## 1. Boss Decision

**APPROVED — ESTABLISH `THAILAND BUSINESS REALITY & USER FITNESS CONTROL` AS A CROSS-DOMAIN GOVERNANCE CONTROL FOR SMEsPlus.**

This control applies across SMEsPlus product/domain work and is not limited to Accounting or COA.

The project shall not rely solely on Boss experience, AI-generated answers, vendor/reference ERP feature coverage, or textbook workflows when claiming Thailand readiness.

The project must demonstrate evidence that SMEsPlus fits real Thai business operations, users, compliance expectations, management controls, security/trust expectations, migration/replacement concerns, digital-government evolution and AI-enabled user control.

## 2. Strategic Product Intent

SMEsPlus is being designed for long-term Thailand adoption and future operating models.

Product readiness shall therefore be measured by evidence of real-world fitness, not by feature count alone.

Key principles:

- `No Thai Business Reality Evidence = No Thailand Product Readiness.`
- `No marketing claim without product evidence.`
- `AI must make users more capable and the system more controlled — not make users dependent on an AI answer.`
- `Unknown != failure; hidden or invented certainty = control failure.`
- `Real user validation cannot be replaced by AI synthesis.`
- `Reference ERP behaviour is evidence input, not target architecture by default.`

## 3. Independent Challenge Function — TBRAC

Establish `Thailand Business Reality & Adoption Council (TBRAC)` as an independent challenge/review function.

### 3.1 Purpose

TBRAC shall challenge product, architecture and workflow assumptions until material Thailand-specific uncertainty is resolved or explicitly retained as an Unknown with controlled Gate impact.

### 3.2 Independence

TBRAC must be independent from the delivery/design team for the item under review.

The same role/team shall not create a material design assumption and independently certify that same assumption without separate review evidence.

### 3.3 Responsibilities

TBRAC shall:

- ask for evidence behind Thai business assumptions;
- distinguish textbook workflow from real operating practice;
- request real-user or SME validation where AI/research evidence is insufficient;
- maintain material Unknown / Conflict / Industry Variation registers;
- challenge marketing, security and replacement claims;
- verify that AI does not silently convert uncertainty into fact;
- recommend `PASS`, `HOLD`, or `FAIL / FROZEN` to PMO/Boss based on evidence;
- identify where external accountants, auditors, tax specialists, security specialists, ISO/QMS specialists, legal/privacy specialists, industry specialists or real customers are required.

### 3.4 Authority Boundary

TBRAC does not replace Boss final authority.

TBRAC does not independently authorize Development, Production, statutory compliance claims, certification claims or marketing claims.

Named membership: `TBD / GOVERNANCE ASSIGNMENT REQUIRED`.

## 4. Mandatory Control Domains

### TB-01 — Thai Business Reality

Prove how Thai businesses actually operate, including practical workarounds and differences from textbook ERP workflows.

### TB-02 — User Persona Reality

Cover applicable personas such as owner, accountant, AR/AP, sales, purchase, warehouse, HR, approver, auditor, administrator and ordinary operating users.

### TB-03 — Happy-Path Reality

Prove normal end-to-end business workflows with evidence.

### TB-04 — Exception-Path Reality

Prove correction, reversal, missing-document, late-document, closed-period, over/under-payment, override/escalation and other non-happy-path behaviour.

### TB-05 — Thai Compliance Reality

Identify and evidence applicable Thailand accounting, tax, labour, privacy/PDPA and other regulatory dependencies by Domain.

Statutory claims require authoritative evidence.

### TB-06 — Document Reality

Use real Thai business document/form patterns and evidence-backed document flows where applicable.

### TB-07 — Integration Reality

Identify practical integration dependencies such as banks, marketplaces, Excel/import-export, APIs, government services and other operating-system boundaries.

### TB-08 — Operational Usability

Prove that ordinary users can perform their work without requiring ERP-expert knowledge.

Usability must be measured/validated; it must not be assumed from UI design alone.

### TB-09 — Digital Government & e-Tax Ecosystem

SMEsPlus shall continuously track and architect for applicable Thai digital-government/e-tax capabilities, including as applicable:

- e-Filing;
- e-Tax Invoice / e-Receipt;
- e-Withholding Tax;
- other current or future Revenue Department / government e-services.

Control requirements:

- authoritative regulatory/source evidence required for statutory behaviour;
- external interfaces/formats/rules must be version-aware;
- government-interface change must not require uncontrolled changes across SaaS Core;
- connector/rule changes must be compatibility-tested and auditable;
- future e-* capabilities are tracked as evolving regulatory/integration dependencies, not assumed from current behaviour.

### TB-10 — Quality / ISO / Management System Reality

SMEsPlus shall evaluate evidence/control requirements for organizational management systems such as ISO 9001 where relevant.

Potential control areas include:

- document/version control;
- approval;
- training/competency records;
- nonconformity;
- corrective action / CAPA;
- internal audit;
- risk/opportunity;
- supplier evaluation;
- complaint/inspection evidence;
- management review;
- audit trail.

Software capability must not be represented as organizational certification.

Any certification/standards claim requires separate appropriate evidence and authority.

### TB-11 — Security & Customer Trust Evidence

Customer/security statements shall be evidence-backed rather than sales assertions.

Evidence targets, as applicable, include:

- tenant isolation;
- company/data isolation;
- IAM / MFA;
- encryption;
- access control;
- audit logging;
- backup and restore test evidence;
- DR / RTO / RPO evidence;
- secure SDLC;
- vulnerability assessment / penetration-test evidence;
- incident response;
- PDPA/privacy controls;
- availability/SLA evidence;
- customer data export/exit procedures.

Rule:

`Security claim without inspectable evidence = NOT VERIFIED / DO NOT USE AS PRODUCT PROOF.`

### TB-12 — Legacy Replacement & Adoption Confidence

SMEsPlus replacement readiness shall be measured against real Thai legacy-system workflows and migration risks.

Replacement evidence shall consider, where applicable:

- critical capability preservation;
- accounting and reconciliation accuracy;
- migration completeness/reconciliation;
- operational continuity;
- document/report continuity;
- training/adoption friction;
- closing/processing effort;
- control/auditability improvement;
- integration improvement;
- measurable business benefit.

Do not claim SMEsPlus is better than a legacy product without comparative product evidence.

Target concept:

`Legacy capability preservation + proven improvement + controlled migration + user adoption evidence = Replacement Confidence.`

### TB-13 — AI Control, Tutor & User Enablement

AI is not limited to task assistance. SMEsPlus shall evaluate AI as controlled:

- `AI Tutor` — teach users in the context of their current task;
- `AI Guard` — detect risk, inconsistency, missing evidence or abnormal behaviour;
- `AI Reviewer` — challenge work before sensitive actions/closing/filing/payment where appropriate;
- `AI Assistant` — reduce repetitive work and explain options.

AI authority boundary:

AI may `Explain / Detect / Recommend / Challenge / Teach / Escalate`.

Deterministic controls such as accounting balance rules, tenant isolation, permissions, period locks, mandatory approvals, statutory formulas and security policy enforcement must not depend solely on probabilistic AI answers.

AI outputs that affect material accounting/compliance/security decisions must preserve provenance, confidence/uncertainty and human/control escalation appropriate to the risk.

## 5. Knowledge Status & Unknown Register

Material knowledge shall be classified using one of the following:

- `VERIFIED`
- `KNOWN / NOT VERIFIED`
- `PARTIALLY UNDERSTOOD`
- `CONFLICTING PRACTICE`
- `INDUSTRY DEPENDENT`
- `COMPANY DEPENDENT`
- `UNKNOWN`
- `REQUIRES REAL USER VALIDATION`
- `REGULATORY VERIFICATION REQUIRED`

AI must not silently transform `UNKNOWN`, `ASSUMPTION`, conflicting practice or incomplete evidence into a verified business fact.

## 6. Gate Enforcement

For every Domain/Gate where a TB control is materially applicable, the Gate package shall include a `THAILAND BUSINESS REALITY & USER FITNESS COMPLIANCE` section or matrix.

Minimum fields:

- Control ID (TB-01..TB-13)
- Applicability
- Evidence location
- Owner / Owner Role
- Timestamp
- Reviewer / Verifier
- Verification Status
- Open Unknown / Conflict
- Gate Impact

Allowed control status:

- `PASS / VERIFIED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`
- `N/A — JUSTIFICATION REQUIRED`

Mandatory effect:

- applicable material evidence gap -> `HOLD`;
- contradictory/unsafe assumption affecting architecture or product readiness -> `FAIL / FROZEN`;
- unresolved blocking Unknown -> no Product Readiness / Replacement Readiness claim;
- exception to a blocking control -> explicit Boss-controlled exception ruling required.

Approval of this framework itself does **not** create execution progress for any STATE/STEP/Domain.

## 7. Relationship to Existing SMEsPlus Governance

This control complements, and does not replace:

- `No Evidence = No Progress`;
- `Never Skip Gate`;
- `Clean-room 100%`;
- Cross-Gate SaaS Invariants;
- Independent Review;
- PMO Verification;
- Boss Final Approval.

For DOMAIN_01 / Thailand COA, TB controls apply in addition to ERPPLUS-132 and the COA Gate sequence, including COA-G04S SaaS Architecture.

## 8. Product Claim Control

Any product claim using terms such as:

- better;
- safer;
- compliant;
- faster;
- easier;
- more reliable;
- replacement-ready;
- audit-ready;
- secure;
- certified;

must state the evidence basis, test scope and limitations.

`No marketing claim without product evidence.`

## 9. Evidence Register — Governance Establishment

| Item | Owner | Evidence Location | Timestamp | Reviewer | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Boss approval of Cross-Domain Thailand Business Reality & User Fitness Control | Boss | Jira ERPPLUS-134 + this GitHub artifact | 2026-08-30 | PMO / ChatGPT evidence check | EVIDENCE RECORDED; framework execution not yet verified | Establishes control baseline only |
| TB-01..TB-13 control scope | Project Governance | This GitHub artifact | 2026-08-30 | TBRAC / PMO review required during execution | APPROVED CONTROL BASELINE | Applies to materially relevant Domain/Gate work |
| TBRAC independent challenge function | Governance | This GitHub artifact | 2026-08-30 | Boss / PMO | APPROVED PRINCIPLE; MEMBERSHIP TBD | Independent challenge required; named assignment outstanding |
| AI Control / Tutor principle | Product + AI Governance | This GitHub artifact | 2026-08-30 | Independent Review / PMO | APPROVED CONTROL PRINCIPLE | Constrains future AI architecture/design |
| Product/marketing evidence principle | Product Governance | This GitHub artifact | 2026-08-30 | PMO / Boss | APPROVED CONTROL PRINCIPLE | Blocks unsupported product claims |

## 10. Administrative Red Flags

- Jira Assignee = `UNASSIGNED`.
- Due Date = `TBD`.
- TBRAC named membership = `TBD / GOVERNANCE ASSIGNMENT REQUIRED`.
- Domain-specific TB evidence coverage = `NOT YET BASELINED`.
- Thailand Knowledge Coverage Matrix = `NOT YET CREATED / EXECUTION REQUIRED`.
- Real-user validation panel/sample = `TBD / EVIDENCE REQUIRED`.

These red flags do not invalidate Boss approval of the governance control, but they prevent claims that the Thailand Business Reality programme itself is complete.

## 11. Authority Boundaries

This ruling authorizes governance/control establishment only.

Development Authorization = **NOT GRANTED**.
Production Authorization = **NOT GRANTED**.
No STATE, STEP, Domain, Board or Gate receives completion credit from this governance approval alone.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
