# 00_Project_Governance

Version: v1.0
Status: Governance Layer v1.0 Approved / Active
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Last Updated: 2026-07-06
Scope: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/`

## Purpose

`00_Project_Governance` is the official governance layer for SMEsPlus Enterprise Suite.

This folder stores project constitution, AI collaboration rules, role authority, document standards, traceability standards, quality gates, approval authority, roadmap and repository registries.

It is the first folder that all human teams and AI agents must read before working on SaaS Foundation, Learning, Functional Design, SDS, API, DB, UX, QA, Build or Production work.

## Governance Pack v1.0

| Document | Status | Purpose |
|---|---:|---|
| PROJECT_CONSTITUTION.md | Approved | Project operating constitution |
| AI_ROLE_AND_RESPONSIBILITY.md | Approved | AI role separation and responsibility |
| AI_COLLABORATION_STANDARD.md | Approved | Multi-AI collaboration rules |
| FUNCTIONAL_SPECIFICATION_STANDARD.md | Approved | Functional Specification standard for all domains |
| ARCHITECTURE_GOVERNANCE_STANDARD.md | Approved | Architecture governance rules |
| DOCUMENT_STANDARD.md | Approved | Document naming and status standard |
| TRACEABILITY_STANDARD.md | Approved | Requirement-to-evidence traceability standard |
| QUALITY_GATE_STANDARD.md | Approved | Gate control standard |
| APPROVAL_AUTHORITY_MATRIX.md | Approved | Decision and approval authority |
| MASTER_EXECUTION_ROADMAP.md | Approved | Project execution sequence |
| REPOSITORY_REGISTRY.yaml | Approved | Repository registry |
| FOLDER_REGISTRY.yaml | Approved | Folder registry |
| DOCUMENT_REGISTRY.yaml | Approved | Governance document registry |

## Standard Reading Order

```text
PROJECT_CONSTITUTION.md
        ↓
AI_ROLE_AND_RESPONSIBILITY.md
        ↓
AI_COLLABORATION_STANDARD.md
        ↓
FUNCTIONAL_SPECIFICATION_STANDARD.md
        ↓
ARCHITECTURE_GOVERNANCE_STANDARD.md
        ↓
TRACEABILITY_STANDARD.md
        ↓
QUALITY_GATE_STANDARD.md
        ↓
APPROVAL_AUTHORITY_MATRIX.md
        ↓
MASTER_EXECUTION_ROADMAP.md
        ↓
REPOSITORY_REGISTRY.yaml
        ↓
FOLDER_REGISTRY.yaml
        ↓
DOCUMENT_REGISTRY.yaml
```

## Access Control

Who can contribute:

- Boss
- Repository Owner
- SMEsPlus PMO
- Executive Secretary AI / Liza
- Approved AI roles under governance control

Who can view:

- All project contributors
- All approved AI agents

## Important Rules

- No Evidence = No Progress.
- No Gate Approval = No Move Forward.
- Repository is the Single Source of Truth.
- AI may draft, review and support execution, but Boss holds final approval authority.
- Build Gate remains HOLD until explicitly approved.
- Production Gate remains HOLD until explicitly approved.

## Current Control Status

```text
Governance Layer v1.0: ACTIVE
Project Constitution: ACTIVE
AI Collaboration Standard: ACTIVE
Functional Specification Standard: ACTIVE
Quality Gate Standard: ACTIVE
Build Gate: HOLD
Production Gate: HOLD
```

## Next Action

Run Governance Validation to confirm that all major folders reference Governance Layer v1.0 correctly before expanding FDP Factory Execution.
