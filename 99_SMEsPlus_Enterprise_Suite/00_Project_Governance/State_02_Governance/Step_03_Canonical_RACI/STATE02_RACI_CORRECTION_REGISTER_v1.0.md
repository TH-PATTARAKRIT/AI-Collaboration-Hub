# STATE02_RACI_CORRECTION_REGISTER_v1.0.md

Session: SMEPLUS-26-07-13-007
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Intake Branch: claude/state-02-step-03-04-sn0sr1
Reference Base Commit: 5454d2afb2efb4d5f2def0a744981b812b843982
Prepared By: Claude AI (Responsible role only)
Prepared At: 2026-07-13T16:16Z (UTC)
Document Status: PREPARED FOR REVIEW
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Control Rule

No source governance document is modified in this STEP. Every entry below is a
PROPOSED correction only. Execution sequencing and application procedure are
controlled in STATE02_RACI_SOURCE_DOCUMENT_UPDATE_PLAN_v0.1.md. Every correction
requires Boss approval before application.

Owner = Executive Secretary / Liza. Reviewer = Governance Reviewer (role appointed,
named identity PENDING RECORD). Verifier = Independent Evidence Verifier (role
appointed, named identity PENDING RECORD).

## 2. Correction Register

| Correction ID | Source Document | Section / Line | Existing Text | Proposed Text | Reason | Owner | Reviewer | Verifier | Approval Required | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| RC-001 | AI_ROLE_AND_RESPONSIBILITY.md | Line 160 (blob ed333098) | Build Gate Owner = `PMO + Boss` | Build Gate Approver = `Boss`; AI PMO = Support Only | ACF-001: AI PMO cannot co-own gate approval (AC-02, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-002 | AI_ROLE_AND_RESPONSIBILITY.md | Line 159 (blob ed333098) | QA/UAT Gate Owner = `QA AI + PMO` | QA/UAT Gate Approver = `Boss`; QA AI + AI PMO = Responsible execution support | ACF-002: AI roles cannot own gate approval (AC-02, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-003 | AI_ROLE_AND_RESPONSIBILITY.md | Line 95 (blob ed333098) | Production approved by `Boss and PMO Gate` | Production approved by `Boss` only | ACF-003: production approval is non-delegable (AC-07/AC-03, P1) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-004 | ARCHITECTURE_GOVERNANCE_STANDARD.md | Line 31 (blob 3a262218) | Gate movement requires `Boss / PMO authority` | Gate movement requires `Boss` approval; AI PMO provides tracking support | ACF-004: joint authority conflicts with Boss-only baseline (AC-02/AC-03, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-005 | APPROVAL_AUTHORITY_MATRIX.md | Line 23 (blob 66930ae5) | FDS Final Approver = `Boss / PMO` | FDS Final Approver = `Boss` | ACF-005: Final Approver must be Boss only (AC-03, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-006 | APPROVAL_AUTHORITY_MATRIX.md | Line 24 (blob 66930ae5) | SDS/API/DB/UX Final Approver = `Boss / PMO` | SDS/API/DB/UX Final Approver = `Boss` | ACF-006: Final Approver must be Boss only (AC-03, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-007 | APPROVAL_AUTHORITY_MATRIX.md | Line 18 (blob 66930ae5) | Project Constitution Draft Owner = `Liza / PMO AI` | Draft Owner = Executive Secretary / Liza (Accountable); AI = Responsible drafting support | ACF-007: exactly one Accountable owner required (AC-07, P1) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-008 | Standards documents vs. DOCUMENT_REGISTRY.yaml | Cross-document (blob 2c31ee69) | Standards contain joint `Boss / PMO` authority contradicting `ai_pmo_role: Support Only`, `final_approval_authority: Boss` | Align all standards to registry baseline: Boss = Final Approver, AI PMO = Support Only | ACF-008: registry/standards contradiction (AC-08, P0) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-009 | FOLDER_REGISTRY.yaml | Lines 26, 31, 36, 41, 61 (blob f307484a) | Folder Owner = `PMO` alone or joint | Named accountable owner per folder per Canonical RACI; AI PMO = Support Only | ACF-009: ownerless/ambiguous folder ownership (AC-01 cand./AC-07, P1) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |
| RC-010 | All State 02 governance documents | Cross-document glossary | `PMO` used ambiguously for AI PMO and human authority | Add canonical role glossary; replace ambiguous `PMO` with explicit role codes | ACF-010: terminology ambiguity is root cause of joint-authority drift (AC-07, P1) | ES | PENDING | PENDING | Boss | CORRECTION PROPOSED |

## 3. Sequencing

Per the Secretary review of 2026-07-13 (STATE02_RACI_SECRETARY_REVIEW_AND_CORRECTION_RECORD_v1.0),
the controlled application order is:

```text
1. RC-010 (glossary — removes ambiguity before text edits)
2. RC-008 (registry baseline alignment)
3. RC-005, RC-006, RC-007 (Approval Authority Matrix)
4. RC-001, RC-002, RC-003 (AI Role and Responsibility)
5. RC-004 (Architecture Governance Standard)
6. RC-009 (Folder Registry cleanup)
```

## 4. Control Statement

All ten corrections remain CORRECTION PROPOSED. None may be applied until Reviewer
Decision = CONFIRM or RECLASSIFY, Verifier Result = VERIFIED, and Boss source-update
authorization exist as recorded evidence.
