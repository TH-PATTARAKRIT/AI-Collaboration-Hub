# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

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
