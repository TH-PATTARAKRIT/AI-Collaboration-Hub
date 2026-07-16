# STATE02_GATE_AUTHORITY_MATRIX_v1.0.md

Session: SMEPLUS-26-07-13-GATE01
State: 02 — Governance
Step: 06 — Gate Crosswalk
Prepared By: Claude AI (Responsible role only — cannot approve, verify, or assign Gate authority)
Prepared At: 2026-07-13T17:03:12Z (UTC)
Document Status: DRAFT — NOT CANONICAL
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Authority Source Precedence Statement

Per `Step_03_Canonical_RACI/STATE02_RACI_CONFLICT_TO_CORRECTION_MATRIX_v1.0.md`
(GII-003): "Gate rows in Canonical RACI Section 3 provide the authority
source" and the gate crosswalk should be derived "from Canonical RACI after
Boss approval." As of this writing, `STATE02_CANONICAL_RACI_v1.0.md` carries
`Gate Status: HOLD — REVIEW AND VERIFICATION PENDING` — it has not been
approved by Boss. Consequently, **every owner/approver value below is marked
PENDING AUTHORITY CONFIRMATION**, even where an older document (predating the
Canonical RACI) names a specific owner. Older-document owner claims are
recorded for traceability, not asserted as current authority.

## 2. Canonical RACI Generic Gate Activities (Step 03, Section 3)

These rows apply to Gate activity in general, regardless of which specific
Gate (GATE-001 through GATE-037) is involved. Source:
`Step_03_Canonical_RACI/STATE02_CANONICAL_RACI_v1.0.md` §3.

| Activity | Responsible | Accountable | Consulted | Informed | Confirmation Status |
|---|---|---|---|---|---|
| Gate recommendation | GTR (Gate Reviewer — currently ChatGPT L99) | ES (Executive Secretary) | GR, EV | BOSS, PMO | PENDING AUTHORITY CONFIRMATION (Canonical RACI itself unapproved) |
| Gate approval | BOSS | BOSS | GTR, L99 | ES, CAI, PMO, DC | PENDING AUTHORITY CONFIRMATION |
| Merge / Release / Deployment | RO / TO | BOSS | L99 (+ FO for Release) | All roles | PROHIBITED in current execution per same table; PENDING AUTHORITY CONFIRMATION |
| Production approval | BOSS | BOSS | GTR, L99, TO | All roles | PENDING AUTHORITY CONFIRMATION |

Role key (from `STATE02_CANONICAL_RACI_v1.0.md` §2): CAI = Claude AI
(Responsible only); ES = Executive Secretary; DC = Document Custodian; RO =
Repository Owner; GR = Governance Reviewer (named identity PENDING RECORD);
EV = Independent Evidence Verifier (named identity PENDING RECORD); GTR =
Gate Reviewer; FA = Final Approver (Boss only, no AI may hold this role).

## 3. Per-Gate Owner Claims Found in Older (Pre-Canonical-RACI) Documents

These are recorded as historical/legacy claims, cross-referenced to the
generic Canonical RACI rule above. None is treated as current authority.

| Gate ID | Gate Name | Legacy Owner Claim | Source | Confirmation Status |
|---|---|---|---|---|
| GATE-001 | Governance Gate | Liza / PMO (AI PMO) | `AI_ROLE_AND_RESPONSIBILITY.md` line 154 | PENDING AUTHORITY CONFIRMATION — AI PMO is Support Only per Canonical RACI §2 |
| GATE-002 | Repository Gate | Claude AI + Liza | `AI_ROLE_AND_RESPONSIBILITY.md` line 155 | PENDING AUTHORITY CONFIRMATION — repository control is RO-responsible / ES-accountable per Canonical RACI §3 |
| GATE-003 | Architecture Gate | Liza / Architecture Office | `AI_ROLE_AND_RESPONSIBILITY.md` line 156 | PENDING AUTHORITY CONFIRMATION |
| GATE-004 | FDS Gate | Functional Specification AI + Claude Review + Liza | `AI_ROLE_AND_RESPONSIBILITY.md` line 157 | PENDING AUTHORITY CONFIRMATION |
| GATE-005 | SDS Gate | Enterprise Architect / Claude Review | `AI_ROLE_AND_RESPONSIBILITY.md` line 158 | PENDING AUTHORITY CONFIRMATION |
| GATE-010 | QA / UAT Gate | "QA AI + PMO" (legacy) | `AI_ROLE_AND_RESPONSIBILITY.md` line 159 | **PENDING AUTHORITY CONFIRMATION — under active correction.** This exact claim is flagged as authority conflict `ACF-002` in `Step_03_Canonical_RACI/STATE02_RACI_CORRECTION_REGISTER_v1.0.md` (row RC-002): proposed correction is "QA/UAT Gate Approver = Boss; QA AI + AI PMO = Responsible execution support," on the basis that AI roles cannot own gate approval (AC-02, P0). The correction itself is still status `CORRECTION PROPOSED`, not adopted. |
| GATE-011 | Build Gate | PMO + Boss (`AI_ROLE_AND_RESPONSIBILITY.md`); Draft Owner PMO/Liza, Reviewer Architecture Office, Final Approver Boss (`APPROVAL_AUTHORITY_MATRIX.md`) | `AI_ROLE_AND_RESPONSIBILITY.md` line 160; `APPROVAL_AUTHORITY_MATRIX.md` row "Build Gate" | PENDING AUTHORITY CONFIRMATION — the two source documents use different breakdowns (single joint owner vs. draft/review/approve roles) and are not reconciled with each other |
| GATE-013 | Production Gate | Boss (explicit approval only) (`AI_ROLE_AND_RESPONSIBILITY.md`); Draft Owner PMO/Infrastructure Lead, Reviewer Boss, Final Approver Boss (`APPROVAL_AUTHORITY_MATRIX.md`) | `AI_ROLE_AND_RESPONSIBILITY.md` line 161; `APPROVAL_AUTHORITY_MATRIX.md` row "Production Gate" | PENDING AUTHORITY CONFIRMATION — both sources agree Boss is Final Approver; this is the single point of strongest cross-document agreement in the whole inventory |
| GATE-030 | Architecture Gate Model (Gate A–D) | AI Owners "may prepare evidence but may not approve a gate"; ChatGPT L99 "performs independent review and issues a recommendation"; "Boss makes the final gate decision" | `03_Architecture/00_Architecture_Governance/ARCHITECTURE_GATE_MODEL.md` §"Gate Authority" | PENDING AUTHORITY CONFIRMATION — structurally consistent with Canonical RACI's Gate recommendation/Gate approval split, but not cross-referenced to it |
| GATE-031 | Architecture Review Gate (ARG) process | Architecture Office (Phase 2), Technical Team AI (Phase 3), Enterprise Architect AI (Phase 4), Boss (Phase 5, "Cannot Delegate: Approval decision") | `00_Architecture_Office/Governance/ARCHITECTURE_REVIEW_GATE.md` §Phase 1–5 | PENDING AUTHORITY CONFIRMATION |
| GATE-014, 015, 016, 017, 019, 022–028 | (all remaining PARTIAL/NOT FOUND gates) | No owner stated anywhere in the repository | — | NOT ASSIGNED |

## 4. Gates With No Owner Anywhere in the Repository

The following Gate IDs from the Inventory Register have zero owner
statement in any source document inspected: GATE-006, GATE-007, GATE-008,
GATE-009, GATE-012, GATE-014, GATE-015, GATE-016, GATE-017, GATE-018
(generic-model instance only), GATE-019, GATE-021, GATE-022, GATE-023,
GATE-024, GATE-025, GATE-026, GATE-027, GATE-028, GATE-033 through GATE-037.
These are marked **NOT ASSIGNED**. No owner is invented for them here.

## 5. Rule Applied Consistently in This Package

No AI role — Claude AI, ChatGPT L99, or any other AI — may be recorded in
this package as a Final Approver or as having Gate approval authority.
Where an older document names an AI role as sole gate "owner" (e.g., the
pre-correction `AI_ROLE_AND_RESPONSIBILITY.md` QA/UAT Gate row), this
crosswalk repeats the claim only as a quoted historical fact and marks it
PENDING AUTHORITY CONFIRMATION rather than treating it as current authority.
