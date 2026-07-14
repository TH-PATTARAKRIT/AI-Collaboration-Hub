# 02 — AUTHORITY CONFLICT DECISION REGISTER

Document ID: S02-FINAL-DOC-02
State: 02 — Governance / Step 02 — Authority Conflict Resolution
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Evidence Commit Reviewed: `8570187bc0f13835be154d10cdc09bfa98e1dfe9`
Prepared By: Claude AI (Responsible / analysis only)
Prepared At: 2026-07-14 (UTC)
Reused Sources (not duplicated):
- `../STATE02_AUTHORITY_CONFLICT_REGISTER_v1.0.md` (base finding set)
- `../STATE02_AUTHORITY_CONFLICT_REGISTER_v1.1.md` (tracking superset — CANONICAL tracking)
- `../STATE02_P0_AUTHORITY_CONFLICT_LIST_v1.0.md` (P0 tier)

> This register **consolidates** the prior v1.0/v1.1 conflict registers into one decision-ready
> view. It does not overwrite them. Each source blob SHA below was re-hashed at HEAD and **matches**
> the SHA recorded in v1.1, proving the source files are unchanged and the conflicts are current.

## 1. Canonical Authority Principle Applied

```text
Boss = Sole Final Approver (Boss ดำเนินการตัดสินใจและอนุมัติขั้นสุดท้ายแต่เพียงผู้เดียว)
No joint final approval. No "Boss / PMO", "PMO + Boss", "Joint Final Approval",
PMO-as-Final-Approver, or AI-as-Final-Approver.
Supporting roles: PMO prepares/coordinates/monitors/reports; Owner executes;
Reviewer reviews; Verifier verifies; AI analyzes/drafts/consolidates/executes in bounds.
```

## 2. Source Blob Evidence (re-verified at HEAD)

| File | Blob SHA at HEAD | Matches v1.1 record |
|---|---|---|
| `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md` | `ed333098c4559b91bfcedf6a05cad80e6219671c` | YES |
| `00_Project_Governance/ARCHITECTURE_GOVERNANCE_STANDARD.md` | `3a262218c3c5c5fc929680d5a5705cea424254fc` | YES |
| `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md` | `66930ae503cc6f672bf66a9c450a67ac6872d839` | YES |
| `00_Project_Governance/DOCUMENT_REGISTRY.yaml` | `2c31ee696e6d252e106e8d30e35e94235534da5d` | YES |
| `00_Project_Governance/FOLDER_REGISTRY.yaml` | `f307484a5a2b63b1d91835d66845e1a66ae9a064` | YES |

## 3. Decision Register

Correction Status legend:
- `READY — MECHANICAL`: correction is a direct application of the locked Boss-sole-approver rule; recommended for Boss authorization then RO/CAI execution.
- `READY — NEEDS DEFINITION`: correction depends on a canonical PMO role definition (a Boss decision) before source wording can be fixed.
- Correction-status values below reflect the **pre-approval** recommendation. After Boss approval
  (S02-FINAL-001 / 003) these were applied to source — see **§5 Applied Corrections** for the
  post-approval status and new blob SHAs.

### ACF-001
- Severity: **P0** | Type: AC-02 (Gate authority)
- Document: `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md` | Path blob `ed333098…` | **Line 160**
- Conflicting wording: `| Build Gate | PMO + Boss | Must pass before Claude Code implementation |`
- Governance impact: Build Gate authority is stated as a PMO+Boss joint owner, conflicting with `APPROVAL_AUTHORITY_MATRIX.md` L25 (Build Gate Final Approver = Boss) and with AI PMO = Support Only.
- Recommended canonical wording: `| Build Gate | Responsible: Repository/Technical Owner; Coordinated by PMO; Final Approver: Boss |` (PMO coordinates; Boss approves — no joint authority).
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 160 at blob `ed333098…`; corroborating GitHub Issues #5, #6, #10 (per v1.1).
- Exact Boss decision required: Confirm Build Gate final approval is **Boss only**, PMO coordinating (Support Only). → See S02-FINAL-001.

### ACF-002
- Severity: **P0** | Type: AC-02
- Document: `AI_ROLE_AND_RESPONSIBILITY.md` | blob `ed333098…` | **Line 159**
- Conflicting wording: `| QA / UAT Gate | QA AI + PMO | Must pass before Build Gate |`
- Governance impact: QA/UAT gate authority stated as QA-AI+PMO joint owner; PMO (Support Only) must not co-own gate authority.
- Recommended canonical wording: `| QA / UAT Gate | Responsible: QA AI; Coordinated by PMO; Final Approver: Boss |`
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 159 at blob `ed333098…`; Issues #5, #6.
- Exact Boss decision required: Confirm QA/UAT gate is QA-AI-Responsible, Boss-approved. → S02-FINAL-001.

### ACF-003
- Severity: **P1** | Type: AC-07 (production authority ambiguity) / AC-03 candidate
- Document: `AI_ROLE_AND_RESPONSIBILITY.md` | blob `ed333098…` | **Line 95, Rule 9**
- Conflicting wording: `9. Production remains HOLD until explicitly approved by Boss and PMO Gate.`
- Governance impact: implies PMO co-approves production; production approval is a non-delegable Boss-only authority.
- Recommended canonical wording: `9. Production remains HOLD until explicitly approved by Boss.` (remove "and PMO Gate").
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 95 at blob `ed333098…`.
- Exact Boss decision required: Confirm Production approval is **Boss only**. → S02-FINAL-001.

### ACF-004
- Severity: **P0** | Type: AC-02 / AC-03
- Document: `00_Project_Governance/ARCHITECTURE_GOVERNANCE_STANDARD.md` | blob `3a262218…` | **Line 31**
- Conflicting wording: `…but Boss / PMO authority is required for gate movement.`
- Governance impact: assigns gate-movement authority jointly to Boss/PMO.
- Recommended canonical wording: `…but Boss authority is required for gate movement (final approval). AI and PMO may propose or review only.`
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 31 at blob `3a262218…`; Issues #6, #10.
- Exact Boss decision required: Confirm gate movement final authority is **Boss only**. → S02-FINAL-001.

### ACF-005
- Severity: **P0** | Type: AC-03 (Final Approver)
- Document: `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md` | blob `66930ae5…` | **Line 23**
- Conflicting wording: `| FDS Domain Artifact | Functional Specification AI | Claude AI / Liza | Boss / PMO |`
- Governance impact: FDS Final Approver listed as `Boss / PMO`.
- Recommended canonical wording: Final Approver column → `Boss`.
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 23 at blob `66930ae5…`; Issue #5.
- Exact Boss decision required: Confirm FDS Final Approver = **Boss**. → S02-FINAL-001.

### ACF-006
- Severity: **P0** | Type: AC-03
- Document: `APPROVAL_AUTHORITY_MATRIX.md` | blob `66930ae5…` | **Line 24**
- Conflicting wording: `| SDS / API / DB / UX | Responsible technical AI | Claude AI / Architecture Office | Boss / PMO |`
- Governance impact: SDS/API/DB/UX Final Approver listed as `Boss / PMO`.
- Recommended canonical wording: Final Approver column → `Boss`.
- Correction status: **READY — MECHANICAL** | NOT YET APPLIED
- Evidence: line 24 at blob `66930ae5…`; Issue #5.
- Exact Boss decision required: Confirm SDS/API/DB/UX Final Approver = **Boss**. → S02-FINAL-001.

### ACF-007
- Severity: **P1** | Type: AC-07 (role ambiguity)
- Document: `APPROVAL_AUTHORITY_MATRIX.md` | blob `66930ae5…` | **Line 18**
- Conflicting wording: `| Project Constitution | Liza / PMO AI | Repository Owner | Boss |`
- Governance impact: Draft Owner conflates human Liza (Executive Secretary) with "PMO AI" (Support Only). Depends on canonical PMO definition.
- Recommended canonical wording (after glossary): `| Project Constitution | Liza (Executive Secretary) | Repository Owner | Boss |`; AI PMO recorded as Support-Only Consulted, not co-Draft-Owner with authority.
- Correction status: **READY — NEEDS DEFINITION** | NOT YET APPLIED
- Evidence: line 18 at blob `66930ae5…`; PR #11 contextual.
- Exact Boss decision required: Approve canonical PMO role definition. → S02-FINAL-003.

### ACF-008
- Severity: **P0** | Type: AC-08 (source-of-truth consistency)
- Document: `00_Project_Governance/DOCUMENT_REGISTRY.yaml` vs. three 2026-07-05 standards | blob `2c31ee69…`
- Conflicting wording: Registry records `ai_pmo_role: Support Only` and `final_approval_authority: Boss`; older 2026-07-05 approved standards still carry joint/PMO authority wording (ACF-001..006).
- Governance impact: latest Boss-approved baseline (via State 01 closure) not propagated to older standards → source-of-truth conflict.
- Recommended canonical action: synchronized re-issue/version correction of the older standards to match the registry baseline, executed together with ACF-001..006.
- Correction status: **READY — MECHANICAL** (bundled with ACF-001..006) | NOT YET APPLIED
- Evidence: registry blob `2c31ee69…`; Issues #5, #9, #10.
- Exact Boss decision required: Authorize synchronized propagation of the Boss-approved baseline. → S02-FINAL-001 / S02-FINAL-003.

### ACF-009
- Severity: **P1** | Type: AC-01 candidate / AC-07
- Document: `00_Project_Governance/FOLDER_REGISTRY.yaml` | blob `f307484a…` | **Lines 26, 31, 36, 41, 61**
- Conflicting wording: bare or joint `PMO` used as folder owner.
- Governance impact: cannot confirm one Accountable owner per folder while `PMO` is ambiguous (human vs AI). AI PMO must not be Accountable Owner.
- Recommended canonical action: after glossary, relabel owners to a single Accountable human owner; AI PMO recorded as Support Only.
- Correction status: **READY — NEEDS DEFINITION** | NOT YET APPLIED
- Evidence: lines 26/31/36/41/61 at blob `f307484a…`.
- Exact Boss decision required: Approve PMO definition, then authorize ownership relabel. → S02-FINAL-003.

### ACF-010
- Severity: **P1** | Type: AC-07 (root cause)
- Document: cross-document governance set | mixed
- Conflicting wording: `PMO` carries at least three apparent meanings (human PMO function, AI PMO Support-Only role, coordination office).
- Governance impact: root cause behind ACF-001/002/007/009. Until PMO is defined canonically, joint-authority wording keeps recurring.
- Recommended canonical action: publish a canonical Role Definitions / glossary distinguishing the meanings; AI PMO = Support Only, never Accountable Owner or Final Approver.
- Correction status: **READY — NEEDS DEFINITION** | NOT YET APPLIED
- Evidence: cross-document; Issue #5 corroborates need for canonical RACI + glossary.
- Exact Boss decision required: Approve canonical PMO glossary. → S02-FINAL-003.

## 4. Decision Roll-up

| Bucket | Conflict IDs | Count | Routed to |
|---|---|---|---|
| P0 — mechanical (locked-rule enforcement) | ACF-001, ACF-002, ACF-004, ACF-005, ACF-006, ACF-008 | 6 | S02-FINAL-001 |
| P1 — needs canonical PMO definition | ACF-003(P1 mechanical), ACF-007, ACF-009, ACF-010 | 4 | S02-FINAL-001 (003) / S02-FINAL-003 |

Note: ACF-003 is P1 by severity but mechanical by correction type; it is authorized under
S02-FINAL-001 with ACF-001/002.

## 5. Applied Corrections (post Boss approval S02-FINAL-001 / 003)

Boss approved S02-FINAL-001 and S02-FINAL-003 on 2026-07-14. The recommended corrections were then
applied to source on branch `claude/state-02-governance-26bzvw` (no merge). New blob SHAs recorded
as evidence of change:

| File | Blob SHA before | Blob SHA after | Conflicts corrected |
|---|---|---|---|
| `AI_ROLE_AND_RESPONSIBILITY.md` | `ed333098…` | `ae297c2d6f5913bc5ed4b887c6d4901d1ddf7cb0` | ACF-001, ACF-002, ACF-003 |
| `ARCHITECTURE_GOVERNANCE_STANDARD.md` | `3a262218…` | `f3abdb621466e060c3af9acae3961a230f703cbc` | ACF-004 |
| `APPROVAL_AUTHORITY_MATRIX.md` | `66930ae5…` | `07edd185ae1091ec16f59e5cd2fb858924d17a3c` | ACF-005, ACF-006, ACF-007 |
| `FOLDER_REGISTRY.yaml` | `f307484a…` | `ba56dc372c9f9ae23f9064b42613e0eb28cf6ab4` | ACF-009 |
| `DOCUMENT_REGISTRY.yaml` | `2c31ee69…` | `2c31ee69…` (unchanged) | ACF-008 resolved by propagating its baseline into the three corrected standards; registry already carried the correct baseline |

New CANONICAL glossary created (resolves ACF-010, supports ACF-007/009):
`../STATE02_CANONICAL_ROLE_DEFINITIONS_GLOSSARY_v1.0.md`.

Updated correction status per conflict:

| Conflict | Status |
|---|---|
| ACF-001, ACF-002, ACF-003, ACF-004, ACF-005, ACF-006 | **CORRECTED (applied)** — see each file's Correction Record |
| ACF-007, ACF-009 | **CORRECTED (applied)** under glossary S02-FINAL-003 |
| ACF-008 | **RESOLVED** — baseline propagated; registry unchanged |
| ACF-010 | **RESOLVED** — canonical glossary published |

Post-correction residual scan: no live authority statement contains `Boss / PMO`, `PMO + Boss`,
`Boss and PMO`, `QA AI + PMO`, or `PMO AI` (remaining matches are only inside Correction Record
tables that quote the prior wording). YAML files validate.

## 6. Control Statement

Boss is the Sole Final Approver. Corrections above were applied only after Boss decisions
S02-FINAL-001 and S02-FINAL-003. **Independent Reviewer and Verifier recording of these applied
corrections remains open under S02-FINAL-005** — the corrections are applied and evidenced, but not
yet independently verified. Claude AI does not self-verify and did not self-approve; the authorizing
decisions are Boss's.
