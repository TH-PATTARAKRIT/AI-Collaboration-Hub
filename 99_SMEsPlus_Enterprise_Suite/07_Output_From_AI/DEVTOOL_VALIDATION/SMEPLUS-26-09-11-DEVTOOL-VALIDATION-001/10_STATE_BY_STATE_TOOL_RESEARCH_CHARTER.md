# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## STATE-by-STATE Tool Research Charter

Status: ACTIVE METHOD CORRECTION / NOT FINAL FREEZE
Owner: SSA — Software & System Architect
Co-Owner: PSPA — Principal SaaS Platform Architect
Final Approver: Boss

## Objective
Research, verify, test and challenge the tools SMEsPlus should use across the complete 12-STATE lifecycle. The goal is not to select the most feature-rich tool. The goal is to select a fit-for-purpose, economically sustainable, governable and evidence-backed toolchain for SMEsPlus ERP for Thai SMEs.

The toolchain research must go from STATE to canonical STEP where evidence exists. Do not invent STEP IDs. If a canonical STEP cannot be verified, record the gap and research at STATE capability level until the STEP map is verified.

## Economic Principle
Paid tools are allowed where measurable engineering productivity, quality, security or risk reduction justifies the cost.
Runtime/core platform components that multiply cost by tenant, company, user, server, request or storage scale require stricter TCO scrutiny. Prefer open/free licensing where it is operationally sound, but Free != Automatic Winner.

Selection basis:
Mission Fit + Constraint Fit + Runtime Evidence + Governance Fit + Sustainable TCO.
Unused Feature = 0 Selection Value.

## Research Record Required Per STATE / STEP
For every applicable STATE and canonical STEP, record:
- STATE and STEP identity
- mission / required outcome
- input and output contract
- current or historical tool
- actual usage status
- runtime/evidence status
- manual handoff and pain points
- mandatory capabilities
- optional capabilities
- prohibited capabilities/actions
- candidate supplement/replacement tools
- licensing model
- TCO model and cost multiplier
- data ownership / portability / exit cost
- API / CLI / headless / automation support
- security / permission boundary
- GitHub / Jira / Figma / CI / evidence integration where applicable
- benchmark or controlled runtime proof
- primary owner tool and supporting tools
- fallback / contingency
- recommendation: KEEP / SUPPLEMENT / REPLACE / REJECT / HOLD

## 12-STATE Research Scope

### STATE01 — Identity
Purpose: Project / AI / Role / Authority / Responsibility / Ownership.
Research focus: role identity, machine/agent identity, permission boundaries, service identities, owner/reviewer mapping, secrets/credential boundary, audit attribution.
Candidate tool families: GitHub identity/teams/rules, Jira roles/permissions, policy-as-code, secrets managers, identity providers where runtime identity is applicable.
Do not select an enterprise IAM stack merely because it is powerful; distinguish project-governance identity from customer-runtime identity.

### STATE02 — Governance
Purpose: Constitution / Standard / Policy / Gate / Evidence / Control / RACI / Tool Governance.
Research focus: policy enforcement, approval/gates, evidence traceability, change control, RACI, audit, rule-as-code, workflow governance.
Candidate tool families: GitHub rulesets/CODEOWNERS/security controls, Jira workflows, policy-as-code, evidence registers, automation controls.

### STATE03 — Architecture
Purpose: Enterprise / SaaS / Application / Data / Integration / Security / Architecture Decisions.
Research focus: architecture modeling, ADR, API/event contracts, data modeling, threat modeling, architecture validation, toolchain architecture.
Canonical STEP mapping must be recovered from repository evidence before assigning tools to each STEP.
Known historical examples include STEP0301, STEP0302, STEP0303 and STEP0304 lineage; current session must not reinterpret old STEP status without evidence.

### STATE04 — Functional
Purpose: Business Function / Process / Business Rule / Functional Specification.
Research focus: requirement intake, functional decomposition, BPMN/process flow, business rules, acceptance criteria, traceability, functional design document generation/review.
High-priority station for the current session because this output feeds UX/UI and later AI EOS learning.

### STATE05 — UX/UI
Purpose: Figma / UX Flow / Screen / Interaction / Design System / Handoff.
Research focus: UX modeling, design system, prototype, design-to-code, component mapping, visual evidence, accessibility, handoff fidelity.
Historical/current candidates such as Figma and Lovable are learning/current choices only until re-proven against SMEsPlus missions.

### STATE06 — Development
Purpose: Coding / Backend / Frontend / API / DB Implementation / Engineering.
Research focus: backend and frontend separately; AI coding agents, workspace/agent host, source control, package/build, database engineering, API engineering, code review, autonomous/headless execution, branch/worktree isolation.
Do not force one winner for backend and frontend.

### STATE07 — Testing
Purpose: Unit / Integration / E2E / FAT / UAT / Test Matrix / Evidence.
Research focus: unit/integration/E2E, browser evidence, performance/load, contract testing, test data, trace, screenshot/video, deterministic CI, regression, failure diagnosis.
Playwright is a current/historical candidate, not an automatic final winner.

### STATE08 — AI Execution
Purpose: AI Agent / Prompt Execution / Dispatch / Orchestration / AI EOS.
Research focus: prompt intake, dispatch, job state, retries/resume, long-running work, agent adapters, evidence lineage, human gates, cost/metering, orchestration versus integration automation.
AI EOS is the target operating layer. Make/n8n and other automation/orchestration tools are candidates/reference capabilities, not assumed baseline winners.

### STATE09 — Infrastructure
Purpose: Server / Network / DB Platform / Container / Storage / HA / DR Infrastructure.
Research focus: Linux/server OS, database platform, containers, networking, reverse proxy/gateway, queue/cache, object storage, backup/restore, HA/DR, infrastructure automation.
Economic rule is especially strict here because runtime costs can multiply with customer scale. Open/free license is preferred where technically and operationally sound.

### STATE10 — Production Operations
Purpose: Deployment / Release / Monitoring / Incident / Backup / Operations.
Research focus: deployment/release control, observability, logging, tracing, metrics, alerting, incident management, backup verification, rollback, SLO/SLA evidence, production access control.

### STATE11 — Knowledge Base
Purpose: Knowledge / Learning / Documentation / Lessons / Evidence Knowledge.
Research focus: canonical documentation, searchable knowledge, versioned knowledge, evidence retention, RAG/indexing where justified, document generation, repository navigation, learning packages for AI EOS.
Prefer portable and version-controlled knowledge over hidden vendor-only context.

### STATE12 — Current Context
Purpose: Current State / Active Session / Active Decision / Carry-forward / Working Context.
Research focus: session registry, state/step position, active decision, carry-forward, context handoff, current evidence pointers, machine-readable context package, stale-context detection.
This STATE is essential for AI EOS to know where work is now and what may or may not execute next.

## Research Priority Layers
Layer A — Foundation & Control: STATE01–STATE03
Layer B — Product Delivery Pipeline: STATE04–STATE07
Layer C — AI / Platform / Operations: STATE08–STATE10
Layer D — Knowledge & Continuity: STATE11–STATE12

STATE04–STATE07 receive deep mission-level benchmarking first because they are the immediate toolchain that produces Functional Design -> Figma/UX -> Development -> Testing/Evidence and becomes a learning/operating package for AI EOS.

## Current/Historical Tool Rule
Any existing tool such as Figma, Lovable, Claude/Claude Code, GitHub, Jira, Playwright, Make or other prior selections must be classified as CURRENT/HISTORICAL/LEARNING until current evidence proves mission fit.
Existing != Best.
Paid != Better.
Free != Better.
New != Improvement.

## Tool Economics
For every tool capture:
- one-time vs recurring
- per-seat
- per-agent
- per-run / token / execution
- per-server / core
- per-tenant / company
- per-request
- per-GB storage
- egress
- backup/DR
- support/operations
- training/skills
- migration/exit cost

Model at minimum small, medium, large and future-scale scenarios before freezing any runtime component with a material cost multiplier.

## Exit Condition
This session must produce a SMEsPlus Tool Operating Map that states for every applicable STATE/STEP:
1. what mission is being performed;
2. which tool is Primary Owner;
3. which tools are supporting/fallback;
4. why the selection fits SMEsPlus;
5. cost/TCO and scale implications;
6. input/output and handoff contract;
7. evidence and benchmark status;
8. security/governance boundary;
9. what AI EOS must learn about when/how to use the tool;
10. unresolved gaps or Boss-only strategic choices.

No tool is final until evidence is sufficient and Boss decides at Final Gate.
No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
