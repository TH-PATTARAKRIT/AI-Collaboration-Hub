# State-Aware Workflow

Route every task to one primary State and apply its controls.

| State | Primary focus | Required control |
|---|---|---|
| 01 | Project Identity | naming, repository identity, ownership baseline |
| 02 | Governance | authority, RACI, gates, evidence, review, verification |
| 03 | Architecture | ADR, SaaS boundaries, security, integration, acceptance criteria |
| 04 | Functional Design | requirement, business rule, BPMN, traceability, UAT readiness |
| 05 | UX/UI Design | Figma authority, role visibility, Odoo-first simplicity |
| 06 | Development | branch, code, tests, clean-room, review, Draft PR |
| 07 | Testing & QA | test cases, expected/actual, defect evidence, UAT gate |
| 08 | AI Execution | model, prompt, tool authority, execution evidence |
| 09 | Infrastructure & Deployment | environment, security, backup, monitoring, deployment gate |
| 10 | Production Operations | production approval, incident, rollback, audit trail |
| 11 | Knowledge Base | canonical source, classification, publication evidence |
| 12 | Current Execution Context | handoff, checkpoint, open decisions, recovery |

For each State, identify allowed actions, prohibited actions, required deliverables, reviewer, verifier, evidence level, Gate impact, and Boss decisions.

Production, Release, Deployment, Merge, Final Gate, and State Closure always remain restricted until explicit Boss approval exists.