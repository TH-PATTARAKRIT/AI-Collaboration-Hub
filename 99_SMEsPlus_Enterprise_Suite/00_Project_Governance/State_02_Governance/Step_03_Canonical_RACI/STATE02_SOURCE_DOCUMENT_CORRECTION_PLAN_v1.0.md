# STATE02_SOURCE_DOCUMENT_CORRECTION_PLAN_v1.0.md

Session: SMEPLUS-26-07-13-007
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Execution Branch: claude/canonical-raci-evidence-xgk851
Prepared By: Claude Code (Responsible role only)
Execution Timestamp: 2026-07-14T04:07Z (UTC) / 2026-07-14 Asia/Bangkok
Document Status: READY FOR BOSS AUTHORIZATION — NOT YET APPLIED
Gate Status: HOLD

## 1. Scope

Controlled plan to apply RC-001 through RC-010 to source governance documents AFTER Boss
authorization. This supersedes the draft STATE02_RACI_SOURCE_DOCUMENT_UPDATE_PLAN_v0.1.md
by adding per-correction rollback and approval gating. No source file is modified until
each precondition below holds as recorded evidence.

## 2. Preconditions per Applied Correction

```text
1. Reviewer Decision = CONFIRM (named Independent Governance Reviewer)
2. Verifier Result   = VERIFIED (named Independent Evidence Verifier)
3. Boss source-update authorization (explicit, recorded)
4. Execution by Authorized GitHub Execution Agent with real Commit SHA
5. Post-correction re-verification against the new commit + updated manifest
```

## 3. Controlled Application Order

| Phase | Corrections | Source Document(s) | Rationale |
|---|---|---|---|
| 1 | RC-010 | All State 02 governance docs (glossary) | Remove terminology ambiguity before any text edit |
| 2 | RC-008 | DOCUMENT_REGISTRY.yaml (baseline reference; no change) | Fix registry baseline as the alignment target |
| 3 | RC-005, RC-006, RC-007 | APPROVAL_AUTHORITY_MATRIX.md | Final Approver + Draft Owner corrections |
| 4 | RC-001, RC-002, RC-003 | AI_ROLE_AND_RESPONSIBILITY.md | Gate approver + production approval corrections |
| 5 | RC-004 | ARCHITECTURE_GOVERNANCE_STANDARD.md | Gate movement authority correction |
| 6 | RC-009 | FOLDER_REGISTRY.yaml | Named Accountable folder owners |

## 4. Per-Correction Application & Rollback

| Correction | File | Change Class | Rollback Method |
|---|---|---|---|
| RC-001 | AI_ROLE_AND_RESPONSIBILITY.md | Material | `git revert` of the correction commit; blob-SHA-before recorded in change impact assessment |
| RC-002 | AI_ROLE_AND_RESPONSIBILITY.md | Material | As above |
| RC-003 | AI_ROLE_AND_RESPONSIBILITY.md | Material | As above |
| RC-004 | ARCHITECTURE_GOVERNANCE_STANDARD.md | Material | As above |
| RC-005 | APPROVAL_AUTHORITY_MATRIX.md | Material | As above |
| RC-006 | APPROVAL_AUTHORITY_MATRIX.md | Material | As above |
| RC-007 | APPROVAL_AUTHORITY_MATRIX.md | Material | As above |
| RC-008 | DOCUMENT_REGISTRY.yaml (no change) | Material (system) | N/A — registry unchanged; alignment achieved via other RCs |
| RC-009 | FOLDER_REGISTRY.yaml | Material | `git revert`; per-line owner-before recorded |
| RC-010 | Glossary addition (new controlled section) | Editorial | Remove added glossary block; `git revert` |

## 5. Evidence Required on Each Applied Change

```text
original text | new text | file path | line/section | blob SHA before | blob SHA after |
Commit SHA | executor identity | Boss authorization reference | verifier result
```

## 6. Status

```text
PLAN STATUS                  = READY FOR BOSS AUTHORIZATION
SOURCE UPDATE AUTHORIZATION   = NOT GRANTED
APPLIED CHANGES               = 0
PROPOSED PATCH                = STATE02_SOURCE_DOCUMENT_PROPOSED_PATCH_v1.0.diff (NOT APPLIED)
```

## 7. Control Statement

This plan does not apply any change. It defines the controlled, reversible, Boss-gated
procedure for applying approved corrections. Gate remains HOLD. Boss remains Sole Final
Approver.
