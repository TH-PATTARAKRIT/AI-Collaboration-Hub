# SMEsPlus Prompt Governance Constitution v1.0

Status: **BOSS DIRECTIVE — EFFECTIVE IMMEDIATELY; BASELINE INCORPORATION PENDING GOVERNANCE CHANGE REVIEW**  
Effective Date: 2026-07-15  
Authority: Boss — Sole Final Approver  
Scope: All AI prompts used for SMEsPlus work, including Claude Code, AI reviewers, and UI agents.

## 1. Purpose

Establish a modular, traceable, Clean Room-safe prompt standard. The standard uses a Base Prompt plus the applicable Prompt Profile for the current State and Gate.

## 2. Mandatory Rules

1. Every prompt must include a Session ID, Step ID, and Prompt ID in the form `STEPxxyyzz`.
2. One prompt must have one measurable primary objective.
3. The prompt must declare its execution mode: `READ-ONLY REVIEW`, `WRITE ON WORKING BRANCH`, or `ANALYSIS ONLY`.
4. The preparer must not independently approve, verify, or close its own work.
5. Clean Room 100% and No Evidence = No Progress apply to every prompt.
6. Boss is the Sole Final Approver.
7. Direct push to `SMEsPlus`, merge, release, deployment, production change, and gate closure are prohibited unless explicitly authorized by Boss.
8. Prompt output must preserve traceability through evidence references, commit SHA, PR status, validation result, and open gaps.

## 3. Base Prompt Standard

Every prompt must define:

- Role and single measurable objective
- Business Context: Thailand SME / Enterprise-lite; Open ERP-first; Simple UX; Enterprise-grade control
- Repository, base branch, working branch, included and excluded scope
- Evidence baseline: commit SHA, PR, and required inputs
- Mandatory controls and forbidden actions
- Acceptance criteria
- Required Final Report

## 4. Clean Room and IP Protection

AI may learn only abstract business behavior, business rules, data concepts, process controls, and permitted evidence. AI must not copy, port, translate, reproduce, or structurally imitate third-party implementation. Every SMEsPlus design and implementation artifact must be independently authored.

## 5. Prompt Profiles

### Profile A — Logic Analysis & Architecture

**Use:** STATE03  
**Objective:** Derive abstract business rules, workflows, data models, indexes, and API boundaries from verified requirements and permitted evidence.  
**Output:** Business-rule mappings, data-schema design, required indexes, API boundaries, assumptions, and traceability.  
**Limit:** No final execution code.

### Profile B — Functional Design

**Use:** STATE04 only after STEP0401 is formally started.  
**Objective:** Module inventory, Fit-Gap, BPMN, Functional Requirements, and Acceptance Criteria.  
**Output:** Traceable Functional Requirements, BPMN, tenant-isolation requirements where applicable, and Acceptance Criteria for each business rule.

### Profile C — Backend Execution

**Use:** STATE06 only after the applicable Build Gate is passed.  
**Objective:** Original SMEsPlus code, tests, benchmarks, and security review.  
**Controls:** Define measurable performance targets by scenario; prevent N+1 and redundant queries; implement indexes, pagination, bulk processing, auditability, security, and tenant isolation where applicable. Performance claims require test evidence.

### Profile D — Frontend / UI

**Use:** STATE05 only after FDS and API Contract readiness.  
**Objective:** Components, UX flows, Thai UX, accessibility, and API-contract-ready UI.  
**Controls:** Use approved Figma Design Authority and Design Tokens only; use Mock APIs or Architecture-Gate-passed API Contracts only.  
**Forbidden:** Production API connection, deployment, and UI workflows that bypass Approval, Posting, or Audit controls.

## 6. Required Final Report

Every applicable execution or review prompt must report:

1. Result: `COMPLETED`, `BLOCKED`, or `REWORK REQUIRED`
2. Scope and files created/changed
3. Validation and evidence result
4. Commit SHA, PR URL, and branch status
5. Open gaps, risks, and required Boss decisions
6. Explicit confirmation of prohibited actions not performed

## 7. Standard Result Manifest

Use this YAML structure for work that produces review, evidence, Commit, or PR outputs:

```yaml
prompt_id: STEPxxyyzz
session_id: SMEPLUS-YY-MM-DD-XXX
execution_mode: READ_ONLY_REVIEW
result: COMPLETED
evidence_commit: "<sha>"
pull_request: "<url or none>"
validation:
  status: PASS
  evidence: "<report or manifest path>"
gaps: []
boss_decisions_required: []
prohibited_actions_not_performed:
  - merge
  - direct_push_to_base
  - release
  - deploy
  - production_change
```

## 8. Applicability and Change Control

This directive applies immediately to all new prompts. Its incorporation into the locked STATE02 governance baseline must be handled through a controlled Governance Change Review. No existing gate, approval authority, release control, or production restriction is changed by this document.

Boss is the Sole Final Approver.
