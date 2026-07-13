# STATE02_AUTHORITY_CONFLICT_DIFF_PREPARATION_v0.1.md

Session: SMEPLUS-26-07-13-002
Status: PREPARATION ONLY — no source document has been or will be modified by this file.

This file proposes correction directions and concepts for STEP 03 planning. It is not a patch, not a diff to apply, and not an authorization to edit source governance documents.

| Document | Section | Existing Authority Concept | Required Authority Concept | Conflict ID | Proposed Correction Direction | STEP 03 Action |
|---|---|---|---|---|---|---|
| AI_ROLE_AND_RESPONSIBILITY.md | Gate Control table, Build Gate row | Gate Owner = "PMO + Boss" | Gate Owner/Approver should reflect Boss-only final authority; PMO limited to Support | ACF-001 | Reword Gate Owner column to separate Support/Coordination from Final Approval | Draft replacement row for Reviewer/Verifier consideration |
| AI_ROLE_AND_RESPONSIBILITY.md | Gate Control table, QA/UAT Gate row | Gate Owner = "QA AI + PMO" | Same as above | ACF-002 | Same direction as ACF-001 | Draft replacement row |
| AI_ROLE_AND_RESPONSIBILITY.md | Core Governance Rule 9 | "approved by Boss and PMO Gate" | Boss-only explicit approval for Production | ACF-003 | Remove ambiguity and align with QUALITY_GATE_STANDARD.md line 19 | Draft replacement sentence |
| ARCHITECTURE_GOVERNANCE_STANDARD.md | Authority clause | "Boss / PMO authority is required for gate movement" | Boss authority required; PMO may support/prepare only | ACF-004 | Reword to Boss authority required; AI PMO may prepare supporting analysis | Draft replacement sentence |
| APPROVAL_AUTHORITY_MATRIX.md | FDS Domain Artifact row | Final Approver = "Boss / PMO" | Final Approver = Boss | ACF-005 | Change Final Approver cell to Boss; PMO may remain Reviewer only if independently justified | Draft replacement row |
| APPROVAL_AUTHORITY_MATRIX.md | SDS/API/DB/UX row | Final Approver = "Boss / PMO" | Final Approver = Boss | ACF-006 | Same direction as ACF-005 | Draft replacement row |
| APPROVAL_AUTHORITY_MATRIX.md | Project Constitution row | Draft Owner = "Liza / PMO AI" | Clarify whether PMO AI drafting is in scope for Support Only | ACF-007 | Await ACF-010 resolution | Hold for role-definition outcome |
| DOCUMENT_REGISTRY.yaml vs. three 2026-07-05 standards | control_notes vs. gate/authority tables | Registry states corrected position; standards not updated | Consistent current authority statement | ACF-008 | Re-issue affected standards as new versions or add explicit superseding note | Draft version-bump plan |
| FOLDER_REGISTRY.yaml | Multiple folder owner fields | Bare "PMO" used as folder owner | Disambiguate PMO and confirm AI PMO is not Accountable Owner | ACF-009 | Await ACF-010 resolution | Hold for role-definition outcome |
| Cross-document | Role terminology | "PMO" used with 3 distinct apparent referents | One canonical definition distinguishing Boss, Liza, AI PMO and human PMO | ACF-010 | Add canonical Role Definitions section or glossary | Draft glossary proposal |

## Boundary Statement

```text
This file contains proposed correction directions and draft replacement concepts only.
No source governance document has been modified, committed, or pushed.
All items require Reviewer content review and Verifier evidence/traceability verification before any STEP 03 execution.
Final Approval Authority: Boss Only.
```
