# AI_COLLABORATION_STANDARD.md

Version: v1.0
Status: Approved
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Effective Date: 2026-07-05
Scope: `99_SMEsPlus_Enterprise_Suite/`

## Purpose

Define the standard for collaboration between all AI roles in the SMEsPlus Enterprise Suite project.

## Principles

1. Repository is the Single Source of Truth.
2. Every AI must follow the approved repository structure and governance documents.
3. AI may draft, review, analyze and support execution, but cannot approve production.
4. No Evidence = No Progress.
5. No Gate Approval = No Move Forward.
6. Work must be traceable from requirement to evidence.

## AI Collaboration Flow

```text
Functional Specification AI
→ Claude AI Review
→ Liza / PMO Gate Review
→ SDS / API / DB / UX
→ QA / UAT
→ Build Gate
→ Claude Code
```

## Role Separation

| AI Role | Main Responsibility |
|---|---|
| Functional Specification AI | Business functional specification |
| Claude AI | Evidence, repository, SaaS alignment, traceability |
| Liza / ChatGPT | Governance, roadmap, cross-AI review, gate control |
| Claude Code | Implementation after Build Gate approval |

## Rules

- Functional Specification AI must not design implementation.
- Claude AI must not invent business requirements.
- Claude Code must not build before Build Gate approval.
- Liza must not bypass Boss final approval.

## Current Gate Status

```text
AI Collaboration Standard: APPROVED
Build Gate: HOLD
Production Gate: HOLD
```
