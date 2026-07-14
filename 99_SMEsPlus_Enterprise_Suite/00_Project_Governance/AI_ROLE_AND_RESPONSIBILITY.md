# AI_ROLE_AND_RESPONSIBILITY.md

Version: v1.0
Status: Approved
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Effective Date: 2026-07-05
Scope: `99_SMEsPlus_Enterprise_Suite/`

---

# Purpose

This document defines the official AI role separation and responsibility model for the SMEsPlus Enterprise Suite project.

The purpose is to ensure that multiple AI agents work under one project standard, one repository structure, one evidence rule and one gate-control model.

---

# Approved AI Working Architecture

```text
Liza / ChatGPT
        = Architecture Governance, PMO Control, Quality Gate, Cross-AI Review

Functional Specification AI
        = Business Functional Specification and Domain FDS Draft

Claude AI
        = Repository Review, Evidence Matching, SaaS Alignment, Gap Analysis, Traceability Review, Repository Writer / Reviewer

Claude Code
        = Implementation only after Gate approval
```

---

# Role Matrix

| AI / Role | Primary Responsibility | Allowed Work | Not Allowed |
|---|---|---|---|
| Liza / ChatGPT | Architecture Governance and PMO control | Roadmap, quality gate, cross-AI review, decision support, standard design | Direct build, merge, release, production approval |
| Functional Specification AI | Business Functional Specification | Business process, business rules, functional requirements, functional draft by domain | Source-code learning, database reverse engineering, technical implementation |
| Claude AI | Evidence and repository validation | Repository audit, evidence matching, SaaS alignment, gap analysis, traceability, repository writing/review | Business approval, production approval, uncontrolled coding |
| Claude Code | Development implementation | Coding only after FDS/SDS/API/DB/UX/QA gates pass | Requirement change, architecture change, merge/release without approval |
| Repository Owner | Repository standard control | Folder standard, document standard, registry control | Bypassing Boss/PMO gate |
| Boss | Final approval authority | Business decision, gate approval, scope decision | N/A |

---

# Standard Workflow

```text
Repository Review
        ↓
Learning Knowledge Base
        ↓
SaaS Foundation
        ↓
Functional Specification AI Draft
        ↓
Claude Evidence Review
        ↓
SaaS Alignment
        ↓
Traceability Review
        ↓
Liza / PMO Quality Gate
        ↓
SDS / API / DB / UX
        ↓
QA / UAT
        ↓
Build Readiness Review
        ↓
Claude Code / Development
        ↓
Release Review
        ↓
Production Gate
```

---

# Core Governance Rules

1. No Evidence = No Progress.
2. No Gate Approval = No Move Forward.
3. AI is an execution assistant, not the final approver.
4. Repository is the Single Source of Truth.
5. Functional Specification AI must not rewrite architecture.
6. Claude AI must not invent business requirements.
7. Claude Code must not start implementation before Build Gate approval.
8. Liza controls governance review but does not override Boss approval.
9. Production remains HOLD until explicitly approved by Boss.

---

# Handoff Rules

## Functional Specification AI to Claude AI

Functional Specification AI must provide:

- Business objective
- Business process
- Functional requirements
- Business rules
- User roles
- Workflow
- Acceptance criteria
- Known gaps
- Handoff notes for Claude review

Claude AI must review against:

- Repository evidence
- Learning evidence
- SaaS Foundation
- Database evidence
- Source evidence
- Traceability standard
- Reuse / Adapt / New / Retire classification

## Claude AI to Liza / PMO

Claude AI must provide:

- Evidence path
- Gap register
- Risk
- Gate impact
- Recommended action
- Build readiness status

## Liza / PMO to Boss

Liza must provide:

- Executive summary
- Current status
- Evidence checked
- Gap / risk
- Recommendation
- Gate impact
- Next action

---

# Gate Control

| Gate | Owner | Status Rule |
|---|---|---|
| Governance Gate | Liza / PMO | Must pass before changing standards |
| Repository Gate | Claude AI + Liza | Must pass before using repository as baseline |
| Architecture Gate | Liza / Architecture Office | Must pass before SDS/API/DB/UX |
| FDS Gate | Functional Specification AI + Claude Review + Liza | Must pass before SDS |
| SDS Gate | Enterprise Architect / Claude Review | Must pass before API/DB/UX finalization |
| QA / UAT Gate | Boss (approver); QA AI + AI PMO (Support Only) | Must pass before Build Gate |
| Build Gate | Boss (approver); AI PMO (Support Only) | Must pass before Claude Code implementation |
| Production Gate | Boss | Explicit approval only |

---

# Current Approved Status

```text
AI Working Architecture: APPROVED
Liza / ChatGPT: Architecture Governance
Functional Specification AI: Business FDS
Claude AI: Repository Writer / Reviewer
Claude Code: Implementation after Gate
Build Gate: HOLD
Production Gate: HOLD
```

---

# Related Documents

- `AI_COLLABORATION_STANDARD.md`
- `FUNCTIONAL_SPECIFICATION_STANDARD.md`
- `ARCHITECTURE_GOVERNANCE_STANDARD.md`
- `TRACEABILITY_STANDARD.md`
- `QUALITY_GATE_STANDARD.md`
- `MASTER_EXECUTION_ROADMAP.md`

---

# Executive Note

This document is approved as the official AI role and responsibility baseline for SMEsPlus Enterprise Suite.

All AI agents must follow this role separation to prevent duplicated work, inconsistent standards, uncontrolled implementation and gate bypass.
