# STATE02_CANONICAL_RACI_v1.0.md

Session: SMEPLUS-26-07-13-007
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Intake Branch: claude/state-02-step-03-04-sn0sr1
Reference Base Commit: 5454d2afb2efb4d5f2def0a744981b812b843982
Prepared By: Claude AI (Authorized Governance Execution Agent — Responsible role only)
Prepared At: 2026-07-13T16:16Z (UTC)
Document Status: PREPARED FOR REVIEW — Boss Decision 1: APPROVED IN PRINCIPLE (conditions apply); Revision R1 corrections applied per Boss Approval Record 2026-07-14
Gate Status: HOLD — INDEPENDENT VERIFICATION AND BOSS CLOSURE PENDING
Revision R1 (2026-07-14, per STATE02_STEP03_BOSS_APPROVAL_RECORD_v1.0.md): added Acting Owner (AO) role to §2; added Build Gate approval and State Closure approval rows to §3; added Replacement Review escalation cross-reference to §4. No authority direction changed — Boss remains Sole Final Approver.

## 1. Purpose

This document defines the single controlled RACI model for State 02. It removes the
authority ambiguity identified in STEP 02 (ACF-001 through ACF-010) between the roles
listed in Section 2. This document is DRAFT-controlled: it becomes Canonical only after
independent Governance Review, independent Evidence Verification, and Boss approval.
No status in this document is APPROVED, PASS, FINAL, CANONICAL, CLOSED, or COMPLETE.

## 2. Controlled Roles

| Role Code | Role | Authority Baseline |
|---|---|---|
| BOSS | Boss | Sole Final Approver. Final authority for Canonical publication and for archive/supersede decisions with authority impact. Not the operational executor. |
| ES | Executive Secretary / Liza | Accountable coordination owner. Evidence and execution coordination. Closure package preparation. Cannot independently approve own work. |
| AO | Acting Owner | Holds Accountable authority for a specific assigned deliverable when standing ownership is delegated or temporarily vacant. Accountable for that deliverable only. Cannot approve the Gate, cannot act as Final Approver, and reverts to the standing owner on assignment. |
| L99 | ChatGPT L99 | Independent Governance Reviewer. Governance consistency reviewer. Repository intake reviewer. Cannot be Final Approver. Cannot verify its own repository write without separate system evidence. |
| CAI | Claude AI | Responsible execution and document preparation. May prepare RACI, matrices, registers, patches, manifests. May commit/push only when authenticated. Cannot be Accountable Owner, independent Reviewer, Evidence Verifier, or Final Approver. |
| PMO | AI PMO | Support Only. Tracking, report preparation, evidence organization. Cannot approve, verify, pass Gate, merge, release, or deploy. |
| RO | Repository Owner / Authorized GitHub Execution Agent | Responsible for repository write execution. Must provide real Commit SHA. Cannot declare Gate PASS. |
| GR | Governance Reviewer | Independent review of governance meaning, classification, severity, gate impact. Role appointed (2026-07-13 order); named identity PENDING RECORD. |
| EV | Independent Evidence Verifier | Verifies path, commit, hash, owner, approval, and evidence. Must be separate from the preparer. May be ChatGPT L99 only where evidence is system-generated and independently inspectable. Must never rely only on Claude AI self-report. Role appointed; named identity PENDING RECORD. |
| DC | Document Control | Registry maintenance, version control, classification execution, controlled publication execution after approval. |
| FO | Functional Owner | Owns functional content correctness of domain documents. |
| TO | Technical Owner | Owns technical content correctness and technical execution (build/release/deploy execution after approval). |
| GTR | Gate Reviewer | Prepares Gate recommendation from review and verification evidence. Cannot approve the Gate. |
| FA | Final Approver | Boss only. No AI may hold this role. |

## 3. Canonical RACI Table

R = Responsible, A = Accountable, C = Consulted, I = Informed.
Every activity has exactly one Accountable role. No AI is Final Approver.

| Activity | Responsible | Accountable | Consulted | Informed | Evidence Required | Gate Impact |
|---|---|---|---|---|---|---|
| Governance document creation | CAI | ES | L99, DC | BOSS, PMO | File path, version, commit SHA | Input to Gate |
| Document ownership assignment | DC | ES | L99, FO, TO | BOSS, PMO | Registry entry with named owner | Blocking if ownerless |
| Repository control | RO | ES | L99, DC | BOSS, PMO | Branch protection state, commit history | Blocking |
| Independent governance review | GR (L99) | ES | EV | BOSS, PMO, CAI | Signed/traceable review decision per item | Blocking |
| Evidence verification | EV | ES | GR | BOSS, PMO, CAI | Verifier result per item with direct inspection trace | Blocking |
| Document classification | DC, CAI | ES | L99 | BOSS, PMO | Classification register entry | Input to Gate |
| Conflict resolution preparation | CAI | ES | GR, L99, FO, TO | BOSS, PMO | Correction register entry (RC-xxx) | Blocking for STEP 03 |
| Archive / supersede decision preparation | CAI | ES | L99, DC | BOSS, PMO | Archive record: paths, reason, replacement, SHA256 pair | Input to Gate |
| GitHub commit and push | RO, CAI (when authenticated) | ES | — | BOSS, L99, PMO | Real Commit SHA, remote branch ref | Blocking |
| Jira update | RO, CAI (when authenticated) | ES | PMO | BOSS, L99 | Jira comment/status with Commit SHA | Input to Gate |
| Gate recommendation | GTR (L99) | ES | GR, EV | BOSS, PMO | Gate recommendation record | Blocking |
| Gate approval | BOSS | BOSS | GTR, L99 | ES, CAI, PMO, DC | Boss approval record | Gate decision |
| Canonical publication | DC | BOSS | L99, ES | All roles | Boss approval + publication commit SHA | Gate decision |
| Merge | RO | BOSS | L99 | All roles | Boss approval record + merge SHA — PROHIBITED in this execution | Gate decision |
| Release | TO | BOSS | L99, FO | All roles | Boss approval record — PROHIBITED in this execution | Gate decision |
| Deployment | TO | BOSS | L99 | All roles | Boss approval record — PROHIBITED in this execution | Gate decision |
| Production approval | BOSS | BOSS | GTR, L99, TO | All roles | Boss-only approval record — no AI participation in approval | Gate decision |
| Build Gate approval | BOSS | BOSS | GTR, L99, TO | ES, CAI, PMO, DC | Boss approval record (Build Gate); AI PMO = Support Only | Gate decision |
| State Closure approval | BOSS | BOSS | GTR, L99, EV | All roles | Boss closure approval record after full evidence verification | Gate decision |

## 4. Structural Rules Enforced

```text
Exactly one Accountable role per activity: CONFIRMED (see table).
At least one Responsible role per activity: CONFIRMED.
No AI as Final Approver: CONFIRMED (BOSS only for Gate approval, Canonical publication authority, Merge, Release, Deployment, Production approval).
No preparer as independent Verifier: CONFIRMED (CAI prepares; EV verifies; EV ≠ CAI).
No ownerless execution activity: CONFIRMED (every row has R and A).
```

Replacement Review escalation: when a Reviewer or Verifier is unavailable, conflicted,
or fails to act, escalation and role replacement are governed by
STATE02_ESCALATION_AND_REPLACEMENT_RULE_v1.0.md (Step 04). A replacement Reviewer or
Verifier must be independent of the preparer; no AI may self-review or self-verify, and
no replacement grants Final Approver authority to any role other than Boss.

## 5. Relationship to STEP 02 Findings

This RACI supersedes, upon Boss approval only, the conflicting authority statements
recorded in ACF-001 through ACF-010 (see STATE02_AUTHORITY_CONFLICT_REGISTER_v1.1.md).
The mapping is controlled in STATE02_RACI_CONFLICT_TO_CORRECTION_MATRIX_v1.0.md and
STATE02_RACI_CORRECTION_REGISTER_v1.0.md. No source governance document is modified by
this STEP; all source changes remain proposed in
STATE02_RACI_SOURCE_DOCUMENT_UPDATE_PLAN_v0.1.md.

## 6. Control Statement

Boss is the Sole Final Approver. No Evidence = No Progress. This document is
PREPARED FOR REVIEW and remains HOLD until independent review, independent
verification, and Boss approval exist as recorded evidence.
