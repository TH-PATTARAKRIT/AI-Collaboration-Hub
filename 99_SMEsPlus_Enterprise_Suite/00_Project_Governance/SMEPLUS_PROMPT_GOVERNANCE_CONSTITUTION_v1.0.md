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
9. Every prompt must declare an AI Platform, Agent Type, Capability Tier, Model Policy, and Tooling Context. Exact Model Name is required only when known or required by the applicable risk/control policy.
10. High-risk work must not silently downgrade to a lower capability tier or substitute a model. The exception and impact must be reported before execution continues.
11. Every prompt that depends on, continues, corrects, revalidates, or uses prior work context must declare Prompt Lineage and Session Traceability.

## 3. Base Prompt Standard

Every prompt must define:

- Role and single measurable objective
- Business Context: Thailand SME / Enterprise-lite; Open ERP-first; Simple UX; Enterprise-grade control
- Repository, base branch, working branch, included and excluded scope
- Evidence baseline: commit SHA, PR, and required inputs
- Session Traceability & Prompt Lineage when prior work is referenced
- AI Execution Profile: Platform, Agent Type, Capability Tier, Model, Model Policy, Tooling Context, and Execution Mode
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

### Profile E — AI Model & Capability Governance

**Use:** Every State, Gate, prompt, and AI platform.  
**Purpose:** Control model capability, cost, risk, reproducibility, and permitted fallback behavior without binding the project to one provider.

**Required fields:**

- AI Platform: Claude / ChatGPT / Figma AI / Lovable / Other
- Agent Type: Architecture Analyst / Code Executor / Independent Reviewer / UI Generator / Other
- Capability Tier: `HIGH_REASONING`, `STANDARD_EXECUTION`, `FAST_TRIAGE`, or `UI_GENERATION`
- Model: exact model name when known
- Model Policy: `REQUIRED`, `PREFERRED`, `OPTIONAL`, or `MODEL_NOT_DISCLOSED`
- Tooling Context: Desktop / Web / API / IDE / Figma / Other

**Rules:**

1. Governance, Architecture, Clean Room/IP, Independent Review, and high-risk code require `HIGH_REASONING`; exact Model Name is recorded when known.
2. Functional Design normally requires `HIGH_REASONING` or `STANDARD_EXECUTION`.
3. Bulk classification, formatting, manifests, and low-risk administrative work may use `FAST_TRIAGE`.
4. UI generation uses `UI_GENERATION` and remains subject to Profile D.
5. When a provider does not disclose the Model, record `MODEL_NOT_DISCLOSED` together with Platform, Agent Type, Capability Tier, Tooling Context, execution date, and evidence output.
6. If a required or preferred model/capability is unavailable, do not silently downgrade. Report available capability, quality/risk impact, and recommended action before continuing.
7. Any model or capability change during a work item must be recorded in the Required Final Report and YAML Result Manifest.

## 6. Prompt Lineage & Session Traceability Control

A closed prompt remains Historical Evidence and may be referenced by later prompts. Its status must never be assumed current only because the prior session was closed.

Every dependent or contextual prompt must record:

- Current Prompt ID
- Parent Prompt ID, or `NONE — NEW WORKSTREAM`
- Reference Prompt IDs
- Reference Type: `DEPENDENCY`, `HANDOFF`, `REVALIDATION`, `CORRECTION`, or `CONTEXT ONLY`
- Evidence Baseline: exact Commit SHA, PR, and required referenced artifacts
- Previous State Snapshot: prior result, State/Step position, verification status, and carried-forward gaps

Mandatory rules:

1. Revalidate referenced evidence before relying on it.
2. A closed prior Prompt is valid reference evidence unless superseded, revoked, or contradicted by a later approved record.
3. A Prompt must not assert that a prior result remains current without checking the stated Commit, PR, or artifact.
4. Any superseded reference must declare `Superseded By: STEPxxyyzz`.
5. Any changed, superseded, or unresolved reference must be recorded in the Required Final Report and YAML Result Manifest.

Required block:

```markdown
## Session Traceability & Prompt Lineage
Current Prompt ID: STEPxxyyzz
Parent Prompt ID: [STEPxxyyzz / NONE — NEW WORKSTREAM]
Reference Prompt IDs: [list / NONE]
Reference Type: [DEPENDENCY / HANDOFF / REVALIDATION / CORRECTION / CONTEXT ONLY]
Evidence Baseline: [Commit SHA / PR / required artifacts]
Previous State Snapshot: [result / State-Step status / verification / carried gaps]
```

## 7. Required Final Report

Every applicable execution or review prompt must report:

1. Result: `COMPLETED`, `BLOCKED`, or `REWORK REQUIRED`
2. Scope and files created/changed
3. Validation and evidence result
4. AI Execution Profile and any model/capability change
5. Commit SHA, PR URL, and branch status
6. Open gaps, risks, and required Boss decisions
7. Explicit confirmation of prohibited actions not performed

## 8. Standard Result Manifest

Use this YAML structure for work that produces review, evidence, Commit, or PR outputs:

```yaml
prompt_id: STEPxxyyzz
session_id: SMEPLUS-YY-MM-DD-XXX
ai_execution_profile:
  platform: Claude
  agent_type: INDEPENDENT_REVIEWER
  capability_tier: HIGH_REASONING
  model: "<exact name or not disclosed>"
  model_policy: REQUIRED
  tooling_context: Claude Code Desktop
prompt_lineage:
  parent_prompt_id: "<STEPxxyyzz or NONE — NEW WORKSTREAM>"
  reference_prompt_ids: []
  reference_type: "DEPENDENCY"
  evidence_baseline: "<commit / PR / artifacts>"
  previous_state_snapshot: "<status>"
execution_mode: READ_ONLY_REVIEW
result: COMPLETED
evidence_commit: "<sha>"
pull_request: "<url or none>"
validation:
  status: PASS
  evidence: "<report or manifest path>"
gaps: []
boss_decisions_required: []
model_or_capability_changes: []
prohibited_actions_not_performed:
  - merge
  - direct_push_to_base
  - release
  - deploy
  - production_change
```

## 9. Applicability and Change Control

This directive applies immediately to all new prompts. Its incorporation into the locked STATE02 governance baseline must be handled through a controlled Governance Change Review. No existing gate, approval authority, release control, or production restriction is changed by this document.

Boss is the Sole Final Approver.
