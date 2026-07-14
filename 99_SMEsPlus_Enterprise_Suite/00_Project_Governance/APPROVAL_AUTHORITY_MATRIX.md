# APPROVAL_AUTHORITY_MATRIX.md

Version: v1.0
Status: Approved
Owner: SMEsPlus PMO / Boss
Approved By: Boss
Effective Date: 2026-07-05
Scope: `99_SMEsPlus_Enterprise_Suite/`

## Purpose

Define approval authority for SMEsPlus Enterprise Suite.

## Authority Matrix

| Decision Area | Draft Owner | Reviewer | Final Approver |
|---|---|---|---|
| Project Constitution | Liza (Executive Secretary) | Repository Owner | Boss |
| AI Role and Responsibility | Liza | PMO / Repository Owner | Boss |
| Functional Specification Standard | Functional Specification AI | Claude AI / Liza | Boss |
| Architecture Governance | Liza / Architecture Office | PMO | Boss |
| Repository Structure | Repository Owner | Claude AI / Liza | Boss |
| FDS Domain Artifact | Functional Specification AI | Claude AI / Liza | Boss |
| SDS / API / DB / UX | Responsible technical AI | Claude AI / Architecture Office | Boss |
| Build Gate | PMO / Liza | Architecture Office | Boss |
| Production Gate | PMO / Infrastructure Lead | Boss | Boss |

## Rule

AI can draft and review. AI cannot approve production. Boss holds final authority.

## Current Status

```text
Approval Authority Matrix: APPROVED
Build Gate: HOLD
Production Gate: HOLD
```

## Correction Record

| Date | Authority | Change | Conflict Ref |
|---|---|---|---|
| 2026-07-14 | Boss decision S02-FINAL-001 (APPROVED) | FDS and SDS/API/DB/UX Final Approver `Boss / PMO` → `Boss` (sole final approver) | ACF-005, ACF-006 |
| 2026-07-14 | Boss decision S02-FINAL-003 (APPROVED) | Project Constitution Draft Owner `Liza / PMO AI` → `Liza (Executive Secretary)`; AI PMO is Support Only, not a draft-authority owner | ACF-007 |

Basis: State 02 finalization package `STATE02_FINALIZATION/` (docs 02, 08). Canonical principle:
Boss is the sole Final Approver; AI PMO = Support Only. Applied on branch
`claude/state-02-governance-26bzvw`; no merge.
