# 06 — GOVERNANCE GATE CROSSWALK

Document ID: S02-FINAL-DOC-06
State: 02 — Governance / Step 06 — Governance Gate Crosswalk
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Evidence Commit Reviewed: `8570187bc0f13835be154d10cdc09bfa98e1dfe9`
Prepared By: Claude AI (Responsible / analysis only)
Prepared At: 2026-07-14 (UTC)
Reference: Canonical RACI candidate (doc 03); `12_State_AI_Execution_Control/STATE_GATE_MATRIX.md`.

Roles: BOSS (Final Approver, sole) · ES (Accountable coordination) · CAI (Claude AI, Responsible) ·
GR (Governance Reviewer) · EV (Evidence Verifier) · RO (Repository Owner) · PMO (Support Only) ·
GTR (Gate Reviewer, recommends only).

## 1. Crosswalk Table

| Gate | Governance Requirement | Entry Criteria | Exit Criteria (verifiable) | Responsible | Accountable | Reviewer | Verifier | Boss Decision | Required Evidence | Upstream Dep. | Downstream Impact |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G0 State-01 Identity | Identity baseline fixed | Charter drafted | Closure record signed by Boss | CAI | ES | GR | EV | Yes (done) | STATE01_CLOSURE_CONFIRMATION.md | — | Enables G1 |
| G1 Governance / Authority | One authority principle; no joint final approval | Conflict register complete | All P0 conflicts corrected **or** presented for exact Boss decision; RACI confirmed | CAI | ES | GR | EV | Yes | Decision Register (doc 02) + Boss record | G0 | Enables G2 Architecture use of authority |
| G2 Architecture Gate | Boss-only gate movement | ADR / arch governance ready | ACF-004 corrected; Boss approves gate movement | RO/CAI | ES | GR | EV | Yes | ARCHITECTURE_GOVERNANCE_STANDARD.md corrected | G1 | State 03 architecture |
| G3 FDS Gate | Boss-only FDS final approval | FDS artifact ready | ACF-005 corrected; Boss approves FDS | CAI | ES | GR | EV | Yes | APPROVAL_AUTHORITY_MATRIX.md L23 corrected | G1 | State 04 functional |
| G4 SDS/API/DB/UX Gate | Boss-only technical approval | SDS artifacts ready | ACF-006 corrected; Boss approves | RO | ES | GR | EV | Yes | APPROVAL_AUTHORITY_MATRIX.md L24 corrected | G3 | Build readiness |
| G5 QA / UAT Gate | QA-AI Responsible; Boss approves | Test evidence ready | ACF-002 corrected; Boss approves | QA AI | ES | GR | EV | Yes | AI_ROLE L159 corrected | G4 | Build gate |
| G6 Build Gate | Boss-only build approval; PMO coordinates | QA/UAT passed | ACF-001 corrected; Boss approves build | RO | ES | GR | EV | Yes | AI_ROLE L160 corrected | G5 | Implementation |
| G7 Production Gate | Boss-only production approval | Build approved | ACF-003 corrected; Boss-only approval | TO | BOSS | GTR | EV | Yes (non-delegable) | AI_ROLE L95 corrected | G6 | Production (PROHIBITED this state) |

## 2. Detection Results

| Check | Result | Detail |
|---|---|---|
| Circular dependencies | **NONE** | Dependency chain G0→G1→{G2,G3}→G4→G5→G6→G7 is a DAG; no gate depends on a downstream gate. |
| Missing owners | **NONE among gates** | Every gate has one Responsible and one Accountable. Note: named **Reviewer/Verifier identities** are role-appointed but PENDING RECORD (OCP-1, OCP-2) — this is an identity-record gap, not a role-definition gap. |
| Duplicate authority | **DETECTED (source docs)** | Joint "Boss / PMO" and "PMO + Boss" wording in GI-10..12 (ACF-001..006). Crosswalk shows Boss as sole decision; correction routed to S02-FINAL-001. |
| Unverifiable exit criteria | **NONE in this crosswalk** | Every exit criterion references a corrected file + a Boss record (both inspectable). |
| Gates dependent only on percentage claims | **NONE** | No gate exit criterion above is "X% complete". Percentage-only claims are rejected per doc 07. |

## 3. Authority Duplication → Canonical Resolution Map

| Gate | Conflicting source wording | Canonical (crosswalk) | Conflict Ref |
|---|---|---|---|
| G2 | "Boss / PMO authority … for gate movement" | Boss decides; PMO coordinates | ACF-004 |
| G3 | FDS Final Approver "Boss / PMO" | Boss | ACF-005 |
| G4 | SDS/API/DB/UX Final Approver "Boss / PMO" | Boss | ACF-006 |
| G5 | "QA / UAT Gate | QA AI + PMO" | QA AI Responsible; Boss approves | ACF-002 |
| G6 | "Build Gate | PMO + Boss" | Boss approves; PMO coordinates | ACF-001 |
| G7 | "approved by Boss and PMO Gate" | Boss only | ACF-003 |

## 4. Control Statement

Boss is the Sole Final Approver. This crosswalk is a preparation artifact; gate exit criteria are
satisfied only when the referenced correction **and** the Boss record both exist as evidence. Merge,
release, deployment, and production remain PROHIBITED in State 02.
