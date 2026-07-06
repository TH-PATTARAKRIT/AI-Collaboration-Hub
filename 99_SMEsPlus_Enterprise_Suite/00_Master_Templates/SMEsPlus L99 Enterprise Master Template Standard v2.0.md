# SMEsPlus L99 Enterprise Master Template Standard v2.0 — File Package

Status: READY FOR REVIEW
Gate Status: HOLD UNTIL FINAL REVIEW
Control Level: /L99
Rule: No Evidence = No Progress
GitHub Commit: HOLD
Merge / Release: HOLD
Production Use: HOLD

## FILE: README.md

# README - SMEsPlus L99 Master Templates

| Field | Value |
| --- | --- |
| Project | SMEsPlus Enterprise Suite |
| Session | [SMEPLUS-26-07-06-001] SMEsPlus L99 Enterprise Master Template Standard v2.0 |
| Document ID | SMEPLUS-README-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Rule | No Evidence = No Progress |
| Repository Target | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Branch Target | SMEsPlus |
| Base Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Requirement -> Business Rule -> Process -> Data/API -> Evidence -> Gate Result |

## Purpose

This folder contains the controlled master templates for SMEsPlus Enterprise Suite. These templates are prepared for review and must not be treated as approved production standards until final review is completed.

## Current Gate Status

Prepare: APPROVED
Review: REQUIRED
Commit: HOLD
Merge: HOLD
Production Use: HOLD
AI Coding Use: HOLD

## Required Files

README.md
00\_TEMPLATE\_INDEX.md
SMEPLUS\_MASTER\_TEMPLATE\_STANDARD\_L99\_v2.0.md
SMEPLUS\_EVIDENCE\_REGISTER\_TEMPLATE\_L99.md
SMEPLUS\_TRACEABILITY\_MATRIX\_TEMPLATE\_L99.md
SMEPLUS\_GATE\_REVIEW\_TEMPLATE\_L99.md
SMEPLUS\_AI\_EXECUTION\_TEMPLATE\_L99.md
SMEPLUS\_CLEAN\_ROOM\_LEARNING\_TEMPLATE\_L99.md
SMEPLUS\_NEXT\_STATE\_HANDOFF\_TEMPLATE\_L99.md
SMEPLUS\_DOCUMENT\_CONTROL\_STANDARD\_L99.md

## Use Restrictions

Do not commit until final review.
Do not merge until final approval.
Do not release.
Do not use for production.
Do not let AI create code from these templates until AI Coding Gate is approved.
Do not claim progress without evidence.

## Planned Commit Message After Approval

feat(L99): add SMEsPlus Enterprise Master Template Standard v2.0

## Mandatory L99 Gate Rules

No Evidence = No Progress
No Owner = No Accountability
No Reviewer = No Approval
No Criteria = No AI Execution
No Traceability = No Gate Pass
No Gate Approval = No Next State
No Clean Room = No Code Approval
No Production Evidence = Production HOLD

## FILE: 00\_TEMPLATE\_INDEX.md

# SMEsPlus Master Template Index L99

| Field | Value |
| --- | --- |
| Project | SMEsPlus Enterprise Suite |
| Document ID | SMEPLUS-IDX-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Template Index -> Template Usage -> Evidence -> Gate Review |

## Template Catalogue

| No. | File | Purpose | Required Use Case | Gate Status |
| --- | --- | --- | --- | --- |
| 1 | README.md | Folder overview and usage control | Explain package and gate status | HOLD |
| 2 | 00\_TEMPLATE\_INDEX.md | Template list and usage matrix | Select correct template before execution | HOLD |
| 3 | SMEPLUS\_MASTER\_TEMPLATE\_STANDARD\_L99\_v2.0.md | Enterprise master standard | All SMEsPlus documents | HOLD |
| 4 | SMEPLUS\_EVIDENCE\_REGISTER\_TEMPLATE\_L99.md | Evidence tracking | Any workstream claiming progress | HOLD |
| 5 | SMEPLUS\_TRACEABILITY\_MATRIX\_TEMPLATE\_L99.md | Requirement-to-evidence mapping | Functional, design, development, QA, gate | HOLD |
| 6 | SMEPLUS\_GATE\_REVIEW\_TEMPLATE\_L99.md | PASS/HOLD/FAIL/FROZEN decision | Before next state or approval | HOLD |
| 7 | SMEPLUS\_AI\_EXECUTION\_TEMPLATE\_L99.md | AI agent control | ChatGPT, Claude, Copilot, Make, OpenAI API Agent | HOLD |
| 8 | SMEPLUS\_CLEAN\_ROOM\_LEARNING\_TEMPLATE\_L99.md | Legal-safe learning control | ERP Open Source, dump, source, blueprint study | HOLD |
| 9 | SMEPLUS\_NEXT\_STATE\_HANDOFF\_TEMPLATE\_L99.md | State-to-state transfer | Before moving to the next state | HOLD |
| 10 | SMEPLUS\_DOCUMENT\_CONTROL\_STANDARD\_L99.md | Document governance | Versioning, naming, status, change log | HOLD |

## Template Selection Rule

| Work Type | Required Template |
| --- | --- |
| New governance or standard document | Master Template Standard + Document Control Standard |
| Evidence collection | Evidence Register Template |
| Requirement, FDS, design, build, QA mapping | Traceability Matrix Template |
| Approval or gate decision | Gate Review Template |
| AI execution, prompt, analysis, coding support | AI Execution Template |
| Learning from ERP Open Source, dump, source code, blueprint | Clean Room Learning Template |
| Moving from one state to another | Next-State Handoff Template |

## Package Review Checklist

| Review Item | Required Result |
| --- | --- |
| All target files present | Yes |
| No shell scripts included | Yes |
| Markdown only | Yes |
| No auto-approval wording | Yes |
| Commit remains HOLD | Yes |
| Merge remains HOLD | Yes |
| Production remains HOLD | Yes |
| Clean Room rule included | Yes |

## FILE: SMEPLUS\_MASTER\_TEMPLATE\_STANDARD\_L99\_v2.0.md

# SMEsPlus Enterprise Master Template Standard L99 v2.0

| Field | Value |
| --- | --- |
| Project | SMEsPlus Enterprise Suite |
| Session | [SMEPLUS-26-07-06-001] |
| Document ID | SMEPLUS-MTS-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Rule | No Evidence = No Progress |
| Repository Target | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Branch Target | SMEsPlus |
| Base Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Requirement -> Business Rule -> Process -> Data/API -> Evidence -> Gate Result |

## Executive Control Status

| Control Item | Status | Decision |
| --- | --- | --- |
| v2.0 Preparation | PASS | Approved to prepare |
| Content Review | HOLD | Awaiting reviewer inspection |
| GitHub Commit | HOLD | Not approved until final review |
| Merge / Release | HOLD | Not approved |
| Production Use | HOLD | Not approved |
| AI Coding Usage | HOLD | Not approved for code generation |

## Enterprise Master Principle

All SMEsPlus documents must be traceable, evidence-backed, and gate-controlled. A document cannot be used as implementation authority unless it has owner, reviewer, approver, evidence path, traceability mapping, version, status, and gate decision.

Requirement
-> Business Rule
-> Business Process
-> Module / Function
-> Data Mapping
-> Screen / API Mapping
-> Jira Issue
-> AI Execution Package
-> GitHub / Figma / CI / Test Evidence
-> Gate Review Result
-> Next-State Handoff

## Mandatory Document Header Standard

| Field | Required | Rule |
| --- | --- | --- |
| Project | Yes | SMEsPlus Enterprise Suite |
| Session | Yes | Use [SMEPLUS-YY-MM-DD-XXX] format |
| Document ID | Yes | Unique and traceable |
| Version | Yes | v0.1, v1.0, v1.1, v2.0 |
| Status | Yes | DRAFT / READY FOR REVIEW / IN REVIEW / APPROVED / SUPERSEDED / ARCHIVED |
| Gate Status | Yes | PASS / HOLD / FAIL / FROZEN |
| Control Level | Yes | /L99 for enterprise-control documents |
| Owner | Yes | Accountable owner |
| Reviewer | Yes | Independent reviewer |
| Approver | Yes | Final authority |
| Evidence Path | Yes | Direct inspectable path or link |
| Traceability | Yes | Upstream and downstream links |
| Change Log | Yes | Required for every version |
| Next Action | Yes | Required when not approved |

## SMEsPlus State Standard

| State ID | State Name | Gate Output Required |
| --- | --- | --- |
| STATE-01 | Project Identity | Approved project baseline and index |
| STATE-02 | Governance | PMO, gate, evidence, RACI, decision rules |
| STATE-03 | Architecture | SaaS, system, integration, security, infra architecture |
| STATE-04 | Functional Design | FRD/FDS, business process, rules, traceability |
| STATE-05 | UX/UI Design | Figma, screen contract, states, design evidence |
| STATE-06 | Development | Jira, branch, PR, CI, code review evidence |
| STATE-07 | Testing & QA | Test plan, test case, defect, UAT evidence |
| STATE-08 | AI Execution | Prompt, guardrail, input, output, review evidence |
| STATE-09 | Infrastructure & Deployment | Environment, backup, monitoring, security evidence |
| STATE-10 | Production Operations | Release, rollback, monitoring, support evidence |
| STATE-11 | Knowledge Base | Decision, lesson, artifact, process knowledge evidence |
| STATE-12 | Current Execution Context | Live session, current gate, blocker, next action |

## Document Numbering Standard

SMEPLUS-{STATE}-{DOMAIN}-{DOCUMENT\_TYPE}-{SEQUENCE}\_L99\_v{VERSION}.md

Examples:

| File | Meaning |
| --- | --- |
| SMEPLUS-STATE04-ACC-FDS-001\_L99\_v1.0.md | Accounting Functional Design Specification |
| SMEPLUS-STATE05-ACC-DCC-001\_L99\_v1.0.md | Accounting Design-to-Code Contract |
| SMEPLUS-STATE08-AI-PROMPT-001\_L99\_v1.0.md | AI Execution Prompt Package |
| SMEPLUS-STATE09-INFRA-GATE-001\_L99\_v1.0.md | Infrastructure Gate Review |

## Core ID Standards

| ID Type | Format | Example |
| --- | --- | --- |
| Functional Requirement | FR-{MODULE}-{NNN} | FR-ACC-001 |
| Business Rule | BR-{MODULE}-{NNN} | BR-ACC-001 |
| Business Process | BP-{MODULE}-{NNN} | BP-ACC-001 |
| Function | {MODULE}-{FUNCTION}-{NNN} | ACC-INVOICE-001 |
| Screen | SCR-{MODULE}-{NNN} | SCR-ACC-001 |
| API | API-{MODULE}-{NNN} | API-ACC-001 |
| Data Object | DO-{MODULE}-{NNN} | DO-ACC-001 |
| Evidence | EVD-{STATE}-{MODULE}-{NNN} | EVD-04-ACC-001 |
| Gate Review | GATE-{STATE}-{MODULE}-{NNN} | GATE-04-ACC-001 |
| Traceability | TRC-{STATE}-{MODULE}-{NNN} | TRC-04-ACC-001 |
| AI Execution | AI-{STATE}-{MODULE}-{NNN} | AI-08-ACC-001 |
| Clean Room Learning | CRL-{SOURCE}-{MODULE}-{NNN} | CRL-ERP-ACC-001 |

## Data Mapping Standard

| Mapping Field | Required Detail |
| --- | --- |
| Data Object ID | DO-XXX-000 |
| Entity Name | Canonical entity name |
| Table / Collection | Target table or TBD |
| Field Name | Business and technical name |
| Data Type | Type, length, precision, nullable |
| Source | User input, calculated, imported, external, system-generated |
| Validation | Business rule ID |
| Data Scope | tenant\_id / company\_id / branch\_id / owner scope |
| Audit Fields | created\_by / updated\_by / approved\_by / posted\_by |
| Event Link | Event emitted after lifecycle change |
| Evidence | DB design, dump observation, schema review, screenshot, log |

## Screen / API Mapping Standard

| Mapping Field | Required Detail |
| --- | --- |
| Screen ID | SCR-XXX-000 |
| Figma Frame URL | Required before Design Ready |
| Screen State | Default, Loading, Empty, Error, Permission, Submitted, Approved, Posted |
| API ID | API-XXX-000 |
| Endpoint | Method and path |
| Request DTO | Fields and validation |
| Response DTO | Fields and nullable behavior |
| Permission Rule | Role and data scope |
| Error Handling | Validation, permission, conflict, system |
| Test Mapping | Unit / integration / E2E / UAT |
| Evidence | Figma, Jira, API contract, test result |

## Evidence Naming Standard

EVD-{STATE}-{MODULE}-{TYPE}-{YYYYMMDD}-{NNN}

| Evidence Type | Code |
| --- | --- |
| Document | DOC |
| Screenshot | IMG |
| Log | LOG |
| GitHub PR | PR |
| CI Result | CI |
| Test Result | TEST |
| Approval | APR |
| Clean Room Learning | CRL |

## Gate Decision Standard

| Decision | Meaning | Minimum Evidence |
| --- | --- | --- |
| PASS | Meets criteria and evidence verified | Owner, reviewer, approver, evidence, criteria, traceability complete |
| HOLD | Work may continue but cannot advance gate | Partial evidence or pending review |
| FAIL | Claim contradicted or criteria not met | Evidence shows noncompliance |
| FROZEN | Work must stop until control issue is resolved | Missing evidence, owner, reviewer, or critical control breach |

## Clean Room Learning Standard

Observation -> Generic Concept -> SMEsPlus Decision -> New SMEsPlus Design -> Independent Implementation

Prohibited:

Direct copy
Clone
Line-by-line imitation
License bypass
Database build from external dump
Migration code without approval
Customer demo using unapproved source-derived material

## Mandatory L99 Gate Rules

No Evidence = No Progress
No Owner = No Accountability
No Reviewer = No Approval
No Criteria = No AI Execution
No Traceability = No Gate Pass
No Gate Approval = No Next State
No Clean Room = No Code Approval
No Production Evidence = Production HOLD

## FILE: SMEPLUS\_EVIDENCE\_REGISTER\_TEMPLATE\_L99.md

# SMEsPlus Evidence Register Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-EVD-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Work Item -> Evidence -> Verification -> Gate Impact |

## Evidence Rule

A task, document, module, gate, or AI output cannot be counted as progress unless evidence is inspectable and tied to the work item.

## Evidence Register Template

| Evidence ID | State | Workstream | Module | Work Item | Claim | Evidence Type | Evidence Path / Link | Owner | Reviewer | Verifier | Timestamp | Verification Status | Gate Impact | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EVD-XX-XXX-DOC-YYYYMMDD-001 | STATE-XX | TBD | TBD | TBD | TBD | DOC | TBD | TBD | TBD | TBD | TBD | Pending | HOLD | Attach evidence |

## Evidence Decision Rules

| Condition | Decision |
| --- | --- |
| Evidence exists, accessible, timestamped, tied to item, reviewed | PASS candidate |
| Evidence exists but reviewer/traceability incomplete | HOLD |
| Evidence path blank or inaccessible | FAIL or FROZEN |
| Owner missing | FROZEN |
| Evidence contradicts claim | FAIL |
| Percentage claimed without evidence | HOLD / FAIL depending criticality |
| AI output without input and criteria | HOLD |
| Clean Room learning without adaptation evidence | FAIL / FROZEN |

## Evidence Type Standards

| Type | Acceptable Evidence |
| --- | --- |
| Document | Markdown, DOCX, PDF, approved record, meeting decision |
| Jira | Issue key, status, worklog, acceptance criteria, comments |
| GitHub | Branch, commit SHA, PR, review, Actions/Checks |
| Figma | File URL, page, frame, version, reviewer note |
| CI/Test | Run ID, result log, screenshot, test report |
| Infrastructure | VM spec, config export, monitoring, backup, restore test |
| AI | Prompt, input files, output, reviewer decision, guardrail checklist |
| Clean Room | Observation, generic concept, adaptation decision, reuse risk review |

## FILE: SMEPLUS\_TRACEABILITY\_MATRIX\_TEMPLATE\_L99.md

# SMEsPlus Traceability Matrix Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-TRC-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Requirement -> Evidence -> Gate Result |

## Traceability Rule

No Traceability = No Gate Pass
No Gate Approval = No Next State

## Traceability Chain

Functional Requirement
-> Business Rule
-> Business Process
-> Module / Function
-> Source / Learning Observation, if any
-> Data Object / Table / DTO
-> Screen / API
-> Jira Issue
-> AI Execution Reference
-> GitHub / Figma / CI / Test Evidence
-> UAT Case
-> Gate Result

## Matrix Template

| Trace ID | FR ID | Function | Module | BP ID | BR ID | Data Object / Table | Screen ID | API ID | Jira Key | AI Ref | GitHub / Figma / CI / Test Evidence | UAT Case | Owner | Reviewer | Gate Result | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRC-XX-XXX-001 | FR-XXX-001 | TBD | TBD | BP-XXX-001 | BR-XXX-001 | TBD | SCR-XXX-001 | API-XXX-001 | ERPPLUS-XXX | AI-XX-XXX-001 | EVD-XX-XXX-001 | UAT-XXX-001 | TBD | TBD | HOLD | Complete evidence |

## Status Values

| Status | Meaning |
| --- | --- |
| MATCHED | Requirement has sufficient evidence across required fields |
| PARTIAL | Some evidence exists but mapping is incomplete |
| GAP | Evidence or mapping not found |
| NEW | New requirement requiring design approval |
| RETIRE | Requirement should not continue |
| HOLD | Cannot move forward until missing trace is fixed |

## FILE: SMEPLUS\_GATE\_REVIEW\_TEMPLATE\_L99.md

# SMEsPlus Gate Review Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-GATE-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Criteria -> Evidence -> Review -> Gate Decision |

## Gate Decision Summary

| Gate Item | Value |
| --- | --- |
| Gate ID | GATE-XX-XXX-001 |
| Gate Name | TBD |
| State | STATE-XX |
| Module / Workstream | TBD |
| Review Date | TBD |
| Owner | TBD |
| Reviewer | TBD |
| Approver | TBD |
| Evidence Register | TBD |
| Traceability Matrix | TBD |
| Final Gate Result | HOLD |

## Decision Criteria

| Decision | Criteria |
| --- | --- |
| PASS | Criteria complete, traceability complete, evidence verified, reviewer approved, approver recorded |
| HOLD | Work may continue but next-state movement is blocked by partial evidence or pending review |
| FAIL | Required criteria are not met, evidence contradicts claim, or scope violates approved rule |
| FROZEN | No owner, no evidence, no reviewer, severe control breach, or prohibited action detected |

## Gate Checklist

| Checklist Item | Required | Status | Evidence ID | Reviewer Comment |
| --- | --- | --- | --- | --- |
| Scope confirmed | Yes | Pending | TBD | TBD |
| Out of scope confirmed | Yes | Pending | TBD | TBD |
| Owner assigned | Yes | Pending | TBD | TBD |
| Reviewer assigned | Yes | Pending | TBD | TBD |
| Approval authority identified | Yes | Pending | TBD | TBD |
| Acceptance criteria complete | Yes | Pending | TBD | TBD |
| Evidence register complete | Yes | Pending | TBD | TBD |
| Traceability matrix complete | Yes | Pending | TBD | TBD |
| Open blockers listed | Yes | Pending | TBD | TBD |
| Risks listed | Yes | Pending | TBD | TBD |
| Next action defined | Yes | Pending | TBD | TBD |

## Executive Gate Result

Gate Result: HOLD
Reason: Pending final reviewer and approver decision.
Next-State Permission: NOT APPROVED
GitHub Commit: HOLD
Merge: HOLD
Release: HOLD
Production Use: HOLD

## FILE: SMEPLUS\_AI\_EXECUTION\_TEMPLATE\_L99.md

# SMEsPlus AI Execution Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-AI-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | AI Prompt -> Input -> Output -> Review -> Evidence -> Gate Result |

## AI Execution Boundary

AI is allowed to assist with analysis, drafting, mapping, evidence register preparation, prompt preparation, and review support. AI must not approve its own output or convert a claim into progress without evidence.

## AI Work Package Header

| Field | Value |
| --- | --- |
| AI Execution ID | AI-XX-XXX-001 |
| AI Tool / Agent | ChatGPT / Claude / Copilot / Make / OpenAI API / Other |
| Workstream | TBD |
| State | STATE-XX |
| Module | TBD |
| Input Source | TBD |
| Prompt File | TBD |
| Expected Output | TBD |
| Acceptance Criteria | TBD |
| Owner | TBD |
| Reviewer | TBD |
| Approver | TBD |
| Evidence Path | TBD |
| Gate Status | HOLD |

## AI Allowed / Not Allowed Matrix

| Activity | Allowed Status | Gate Rule |
| --- | --- | --- |
| Summarize supplied notes | Allowed | Review required |
| Create Markdown template | Allowed | Review required |
| Create evidence register | Allowed | Verification required |
| Map requirement to process | Allowed | BA/SA review required |
| Analyze source/dump for learning | Allowed with Clean Room | No code, no direct reuse |
| Generate production code | HOLD | Requires Build Ready + AI Coding Ready |
| Generate migration script | HOLD | Requires Data/Migration Gate PASS |
| Merge PR | Not allowed | Human/Gate owner only |
| Release to production | Not allowed | Production Gate only |
| Approve own output | Not allowed | Independent review required |

## Prompt Control Template

Project: SMEsPlus Enterprise Suite
Control Level: /L99
Rule: No Evidence = No Progress
Task ID: AI-XX-XXX-001
State: STATE-XX
Module: TBD
Input Evidence: TBD
Allowed Output: TBD
Not Allowed: Do not invent requirements, endpoints, database schema, permissions, business rules, approval logic, posting logic, or production actions.
Review Required: Yes
Gate Status After Output: HOLD UNTIL REVIEW

## FILE: SMEPLUS\_CLEAN\_ROOM\_LEARNING\_TEMPLATE\_L99.md

# SMEsPlus Clean Room Learning Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-CRL-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Source Reference -> Observation -> Generic Concept -> SMEsPlus Decision -> Evidence -> Gate Result |

## Clean Room Purpose

This template allows learning and analysis while preventing direct copy, clone, line-by-line imitation, license bypass, or unauthorized reuse.

## Clean Room Workflow

Source Reference
-> Observation
-> Generic Concept
-> SMEsPlus Fit / Gap / Adapt / Extend / Reject Decision
-> Independent SMEsPlus Design
-> Reviewer Approval
-> Gate Result

## Learning Package Header

| Field | Value |
| --- | --- |
| Clean Room ID | CRL-XXX-001 |
| Source Type | ERP Open Source / Database Dump / Source Code / Screenshot / Export / Blueprint |
| Source Reference | TBD |
| Module / Process | TBD |
| Learning Purpose | TBD |
| Allowed Use | Observation and generic concept only |
| Prohibited Use | Copy, clone, direct reuse, line-by-line imitation |
| Owner | TBD |
| Reviewer | TBD |
| Approver | TBD |
| Evidence Path | TBD |
| Gate Status | HOLD |

## Observation Register

| Observation ID | Source Reference | What Was Observed | Generic Concept | SMEsPlus Decision | Reuse Risk | Reviewer | Gate Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OBS-001 | TBD | TBD | TBD | Adapt / Extend / Reject / Hold | Pending | TBD | HOLD |

## Prohibited Actions

Do not copy source code.
Do not clone module structure.
Do not reproduce proprietary screens.
Do not directly reuse database schema as build authority.
Do not generate migration code from external dump without approval.
Do not use source-derived material for customer demo unless approved.
Do not let AI imitate source implementation.

## Required Output Format

Reference -> Generic Concept -> SMEsPlus Adapt / Extend / Reject -> Evidence -> Gate Result

## FILE: SMEPLUS\_NEXT\_STATE\_HANDOFF\_TEMPLATE\_L99.md

# SMEsPlus Next-State Handoff Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-HANDOFF-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Current State -> Evidence -> Gate Review -> Next State Decision |

## Handoff Rule

No state may move to the next state unless evidence, traceability, owner, reviewer, approver, open gaps, and gate decision are recorded.

## Handoff Header

| Field | Value |
| --- | --- |
| Handoff ID | HOFF-STATE-XX-TO-YY-001 |
| From State | STATE-XX |
| To State | STATE-YY |
| Workstream / Module | TBD |
| Owner | TBD |
| Reviewer | TBD |
| Approver | TBD |
| Evidence Register | TBD |
| Traceability Matrix | TBD |
| Gate Review | TBD |
| Handoff Status | HOLD |

## Deliverable Checklist

| Deliverable | Required | Status | Evidence ID | Owner | Reviewer |
| --- | --- | --- | --- | --- | --- |
| Source documents complete | Yes | Pending | TBD | TBD | TBD |
| Evidence register complete | Yes | Pending | TBD | TBD | TBD |
| Traceability matrix complete | Yes | Pending | TBD | TBD | TBD |
| Open gap list complete | Yes | Pending | TBD | TBD | TBD |
| Risk / blocker list complete | Yes | Pending | TBD | TBD | TBD |
| Gate review complete | Yes | Pending | TBD | TBD | TBD |
| Approver decision recorded | Yes | Pending | TBD | TBD | TBD |

## Final Handoff Decision

Handoff Result: HOLD
Reason: Final review and approval pending.
Next State: NOT APPROVED until gate decision is recorded.

## FILE: SMEPLUS\_DOCUMENT\_CONTROL\_STANDARD\_L99.md

# SMEsPlus Document Control Standard L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-DOCCTRL-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Document -> Version -> Review -> Approval -> Evidence -> Gate Result |

## Document Control Principle

A SMEsPlus document is not a controlled artifact unless it has document ID, version, status, owner, reviewer, approver, evidence path, change log, and gate status.

## Document Status Values

| Status | Meaning | Gate Rule |
| --- | --- | --- |
| DRAFT | Working draft | Not usable for approval |
| READY FOR REVIEW | Prepared and awaiting reviewer | HOLD |
| IN REVIEW | Reviewer is checking | HOLD |
| APPROVED | Approved by authorized approver | PASS for approved scope only |
| SUPERSEDED | Replaced by newer version | Do not use for new work |
| ARCHIVED | Retained for history | Read-only |

## Versioning Rule

| Version | Use Case |
| --- | --- |
| v0.1 | Initial draft |
| v0.2 | Draft correction |
| v1.0 | First approved baseline |
| v1.1 | Minor clarification |
| v2.0 | Major structural upgrade |

## File Naming Rule

SMEPLUS-{STATE}-{DOMAIN}-{DOCUMENT\_TYPE}-{SEQUENCE}\_L99\_v{VERSION}.md

For master templates:

SMEPLUS\_{DOCUMENT\_NAME}\_L99\_v{VERSION}.md

## Change Log Template

| Version | Date | Change Summary | Owner | Reviewer | Approver | Gate Impact |
| --- | --- | --- | --- | --- | --- | --- |
| vX.Y | YYYY-MM-DD | TBD | TBD | TBD | TBD | HOLD |

## Control Breach Result

| Control Breach | Gate Result |
| --- | --- |
| Missing owner | FROZEN |
| Missing reviewer | HOLD / FROZEN |
| Missing approver for approval claim | FAIL |
| Missing evidence path | HOLD / FAIL |
| Approved document overwritten without version | FAIL |
| AI-generated document with no review | HOLD |
| Production use without approved status | FROZEN |