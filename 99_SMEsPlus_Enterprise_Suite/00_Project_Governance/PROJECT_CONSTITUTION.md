# PROJECT_CONSTITUTION.md

Version: v1.0
Status: Approved
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Effective Date: 2026-07-05
Scope: `99_SMEsPlus_Enterprise_Suite/`

## Purpose

This document is the project constitution for SMEsPlus Enterprise Suite. It defines the operating principles, authority model, repository control model, evidence rule and gate-control discipline for all human and AI contributors.

## Core Principles

1. Repository is the Single Source of Truth.
2. No Evidence = No Progress.
3. No Gate Approval = No Move Forward.
4. AI may draft, analyze, review and support execution, but Boss holds final approval authority.
5. Build and Production are controlled gates, not automatic outcomes of documentation completion.
6. Learning, architecture, functional design, software design, testing and deployment must remain traceable.

## Authority Model

| Role | Authority |
|---|---|
| Boss | Final approval and business decision authority |
| Repository Owner | Repository structure and standards control |
| Liza / ChatGPT | Architecture governance, PMO control, cross-AI review |
| Claude AI | Repository review, evidence matching, SaaS alignment, gap analysis |
| Functional Specification AI | Business functional specification draft |
| Claude Code | Implementation only after Build Gate approval |

## Standard Execution Flow

```text
Governance
→ Learning / Knowledge Base
→ SaaS Foundation
→ Functional Specification
→ Claude Evidence Review
→ SDS / API / DB / UX
→ Traceability / QA / UAT
→ Build Readiness Review
→ Development
→ Release Review
→ Production Gate
```

## Gate Rule

A downstream phase may not proceed unless the upstream gate is explicitly approved or marked PASS WITH CONTROL.

## Current Control Status

```text
Project Constitution: APPROVED
AI Role Model: APPROVED
Functional Specification Standard: APPROVED FOR USE
Build Gate: HOLD
Production Gate: HOLD
```
