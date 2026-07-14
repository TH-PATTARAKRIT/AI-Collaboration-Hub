# STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md

Session: SMEPLUS-26-07-14-STEP03-CORR
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Execution Branch: claude/canonical-raci-evidence-xgk851
Authorization: Boss Decision 2 — CONTROLLED SOURCE CORRECTION AUTHORIZED
Prepared By: Claude Code (Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR REVIEW
Gate Status: HOLD
Reviewer Status: PENDING
Verifier Status: PENDING

## 1. Rule

This register records exact before/after text, file path, blob SHA before the change, and
commit SHA after the change for every one of RC-001 through RC-010. All ten items were
previously mapped, verified, and gated behind Boss authorization in
`STATE02_SOURCE_GOVERNANCE_CONFLICT_REGISTER_v1.0.md`. Every correction below is scoped to
the exact line identified in that register; no unrelated content was changed.

## 2. Before/After Table

| RC ID | File | Before | After | Blob SHA Before | Commit SHA After | Reviewer Status | Verifier Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| RC-001 | `AI_ROLE_AND_RESPONSIBILITY.md` | `\| Build Gate \| PMO + Boss \| Must pass before Claude Code implementation \|` | `\| Build Gate \| Boss (approver); AI PMO (Support Only) \| Must pass before Claude Code implementation \|` | `ed333098c4559b91bfcedf6a05cad80e6219671c` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-002 | `AI_ROLE_AND_RESPONSIBILITY.md` | `\| QA / UAT Gate \| QA AI + PMO \| Must pass before Build Gate \|` | `\| QA / UAT Gate \| Boss (approver); QA AI + AI PMO (Support Only) \| Must pass before Build Gate \|` | `ed333098c4559b91bfcedf6a05cad80e6219671c` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-003 | `AI_ROLE_AND_RESPONSIBILITY.md` | `9. Production remains HOLD until explicitly approved by Boss and PMO Gate.` | `9. Production remains HOLD until explicitly approved by Boss.` | `ed333098c4559b91bfcedf6a05cad80e6219671c` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-004 | `ARCHITECTURE_GOVERNANCE_STANDARD.md` | `... AI may propose or review, but Boss / PMO authority is required for gate movement.` | `... AI may propose or review, but Boss approval is required for gate movement; AI PMO provides tracking support only.` | `3a262218c3c5c5fc929680d5a5705cea424254fc` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-005 | `APPROVAL_AUTHORITY_MATRIX.md` | `\| FDS Domain Artifact \| Functional Specification AI \| Claude AI / Liza \| Boss / PMO \|` | `\| FDS Domain Artifact \| Functional Specification AI \| Claude AI / Liza \| Boss \|` | `66930ae503cc6f672bf66a9c450a67ac6872d839` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-006 | `APPROVAL_AUTHORITY_MATRIX.md` | `\| SDS / API / DB / UX \| Responsible technical AI \| Claude AI / Architecture Office \| Boss / PMO \|` | `\| SDS / API / DB / UX \| Responsible technical AI \| Claude AI / Architecture Office \| Boss \|` | `66930ae503cc6f672bf66a9c450a67ac6872d839` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Gate decision |
| RC-007 | `APPROVAL_AUTHORITY_MATRIX.md` | `\| Project Constitution \| Liza / PMO AI \| Repository Owner \| Boss \|` | `\| Project Constitution \| Executive Secretary / Liza \| Repository Owner \| Boss \|` | `66930ae503cc6f672bf66a9c450a67ac6872d839` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Input to Gate |
| RC-008 | (alignment — no file edited; enacted via RC-001..RC-007 + RC-009/RC-010) | Standards contained `Boss / PMO` / `PMO + Boss` joint authority contradicting `DOCUMENT_REGISTRY.yaml` (`ai_pmo_role: Support Only`, `final_approval_authority: Boss`) | Standards now align to the registry baseline; `DOCUMENT_REGISTRY.yaml` unchanged (already correct) | N/A (no edit — verification only) | N/A | PENDING | PENDING | Input to Gate |
| RC-009 | `FOLDER_REGISTRY.yaml` | `owner: Functional Specification AI / PMO` (path `02_Functional_Design`); `owner: PMO / Traceability Owner` (path `12_Traceability`); `owner: PMO` (path `13_Jira_Control`); `owner: Claude AI / PMO` (path `14_Claude_Execution`); `owner: PMO / Repository Owner` (path `Archived`) | `owner: Functional Specification AI (Responsible); Document Control (Accountable)`; `owner: Traceability Owner (Accountable); AI PMO (Support Only)`; `owner: Document Control (Accountable); AI PMO (Support Only)`; `owner: Claude AI (Responsible); Document Control (Accountable)`; `owner: Repository Owner (Accountable); AI PMO (Support Only)` | `f307484a5a2b63b1d91835d66845e1a66ae9a064` | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Blocking (ownership) |
| RC-010 | `CANONICAL_ROLE_GLOSSARY.md` (new file, additive) | No canonical role glossary existed; `PMO` used ambiguously across State 02 governance documents | Added `CANONICAL_ROLE_GLOSSARY.md` defining every controlled role, with `AI PMO` explicitly marked Support Only | N/A (new file — no prior blob) | `ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc` | PENDING | PENDING | Input to Gate |

## 3. Scope Confirmation

```text
Files modified: APPROVAL_AUTHORITY_MATRIX.md, AI_ROLE_AND_RESPONSIBILITY.md,
                ARCHITECTURE_GOVERNANCE_STANDARD.md, FOLDER_REGISTRY.yaml
Files created:  CANONICAL_ROLE_GLOSSARY.md
Source code changed:            NONE
Application/infrastructure/DB/production configuration changed: NONE
Unrelated content changed:       NONE (diff-verified — only the RC-identified lines changed)
Git history rewritten:           NO
Historical evidence removed:     NO
```

## 4. Control Statement

Every correction above is reversible through `git revert ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc`.
Reviewer and Verifier statuses are PENDING and are not filled by Claude Code. Gate remains
HOLD. Boss remains Sole Final Approver.
