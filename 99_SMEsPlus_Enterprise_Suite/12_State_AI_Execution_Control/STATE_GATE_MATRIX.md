# STATE GATE MATRIX

Status: Active Control Matrix  
Project: SMEsPlus Enterprise Suite

## Gate Matrix

| State | Name | AI Allowed Scope | AI Prohibited Scope | Required Evidence | Gate Result |
|---|---|---|---|---|---|
| 01 | Project Identity | Review project name, objective, scope, principles, roles | Deep design, coding, deployment | Project charter, principle, role matrix | PASS / HOLD / FAIL |
| 02 | Governance | Review PMO rules, gate rules, evidence rules, approval rules | Approve on behalf of Boss | Governance docs, gate checklist, evidence rules | PASS / HOLD / FAIL |
| 03 | Architecture | Review SaaS, tenant, security, integration, infra direction | Coding, deployment, production change | Architecture pack, ADR, risk register | PASS / HOLD / FAIL |
| 04 | Functional Specification | Review FR, FDS, BPMN, business rules, Thai localization, traceability | Coding, DB change, build decision | FDS package, criteria, traceability matrix | PASS / HOLD / FAIL |
| 05 | UX/UI Design | Review Figma readiness, screen flow, role-based menu, usability | Change requirement without approval | Figma link, screen spec, UX review | PASS / HOLD / FAIL |
| 06 | Development | Generate or review code only from approved FDS/design | Merge, release, production change | Branch, PR, code review, test evidence | PASS / HOLD / FAIL |
| 07 | Testing & QA | Review test case, UAT, defect, screenshot evidence | Close defect without evidence | Test cases, defect log, screenshots | PASS / HOLD / FAIL |
| 08 | AI Execution | Review prompt guard, hallucination control, scope control | Execute unapproved prompt | Prompt register, AI output log, reviewer note | PASS / HOLD / FAIL |
| 09 | Infrastructure & Deployment | Review server, VM, Docker, DB, backup, monitoring, security | Production deploy without approval | Infra evidence, deployment log, security checklist | PASS / HOLD / FAIL |
| 10 | Production Operations | Review incident, backup, SLA, monitoring, change control | Hotfix production without change record | Incident log, SLA report, backup evidence | PASS / HOLD / FAIL |
| 11 | Knowledge Base | Review document completeness, version, owner, searchability | Publish unverified knowledge | KB index, version log, reviewer evidence | PASS / HOLD / FAIL |
| 12 | Current Execution Context | Review current status, blockers, next action, owner, evidence | Report unsupported progress | Status report, blocker log, next action register | PASS / HOLD / FAIL |

## Universal Gate Rule

```text
No input = HOLD
No criteria = HOLD
No evidence = No Progress
No reviewer = HOLD
Contradictory evidence = FAIL
Critical control breach = FROZEN
```
