# STATE02_RACI_CONFLICT_TO_CORRECTION_MATRIX_v1.0.md

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

## 1. Scope and ID Definitions

- ACF-001 through ACF-010: authority conflict findings from
  STATE02_AUTHORITY_CONFLICT_REGISTER_v1.1.md (STEP 02).
- GII-001 through GII-006: GitHub Issue authority items. No prior register assigned GII
  identifiers, so this matrix formally defines them from
  STATE02_GITHUB_ISSUE_AUTHORITY_SCAN_ADDENDUM_v0.1.md, in listed order:

```text
GII-001 = Issue #3  — State 02 Governance Canonical Package and Closure Control
GII-002 = Issue #5  — Replace outdated AI PMO ownership with canonical RACI
GII-003 = Issue #6  — Create State Gate and Domain Gate Crosswalk
GII-004 = Issue #9  — Create Governance Evidence and Document Classification Registers
GII-005 = Issue #10 — Execute State 02 Gate Review and Boss Closure Pack
GII-006 = PR #11    — Correct document status terminology and record independent Step 01 review
```

Allowed statuses in this matrix: OPEN, CORRECTION PROPOSED, READY FOR REVIEW, HOLD.
No item is marked resolved: no approved source-document correction evidence exists yet.

## 2. Conflict-to-Correction Matrix

Owner = Executive Secretary / Liza (Accountable coordination owner).
Reviewer = Governance Reviewer (role APPOINTED 2026-07-13; named identity PENDING RECORD).
Verifier = Independent Evidence Verifier (role APPOINTED 2026-07-13; named identity PENDING RECORD).

| Conflict ID | Current Conflict | Affected Document | Current Role Statement | Correct Role Statement | Proposed Correction | Owner | Reviewer | Verifier | Status |
|---|---|---|---|---|---|---|---|---|---|
| ACF-001 | Build Gate ownership shared with PMO (AC-02, P0) | AI_ROLE_AND_RESPONSIBILITY.md line 160 | Build Gate Owner = `PMO + Boss` | Gate approval = Boss only; AI PMO = Support Only | RC-001: replace joint gate ownership with Boss-only approval, AI PMO support | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-002 | QA/UAT Gate ownership assigned to AI roles (AC-02, P0) | AI_ROLE_AND_RESPONSIBILITY.md line 159 | QA/UAT Gate Owner = `QA AI + PMO` | Gate approval = Boss only; AI = Responsible execution support | RC-002: replace AI gate ownership with Boss approval, AI responsible-support roles | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-003 | Production approval jointly delegated (AC-07/AC-03, P1) | AI_ROLE_AND_RESPONSIBILITY.md line 95 | Production approved by `Boss and PMO Gate` | Production approval = Boss only | RC-003: remove PMO from production approval statement | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-004 | Gate movement requires joint Boss/PMO authority (AC-02/AC-03, P0) | ARCHITECTURE_GOVERNANCE_STANDARD.md line 31 | `Boss / PMO authority` required for gate movement | Gate movement approval = Boss only; PMO = Support Only | RC-004: replace `Boss / PMO` with `Boss` for gate movement authority | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-005 | FDS final approval shared (AC-03, P0) | APPROVAL_AUTHORITY_MATRIX.md line 23 | FDS Final Approver = `Boss / PMO` | Final Approver = Boss only | RC-005: set FDS Final Approver = Boss | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-006 | SDS/API/DB/UX final approval shared (AC-03, P0) | APPROVAL_AUTHORITY_MATRIX.md line 24 | SDS/API/DB/UX Final Approver = `Boss / PMO` | Final Approver = Boss only | RC-006: set SDS/API/DB/UX Final Approver = Boss | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-007 | Constitution draft ownership ambiguous (AC-07, P1) | APPROVAL_AUTHORITY_MATRIX.md line 18 | Project Constitution Draft Owner = `Liza / PMO AI` | Draft Owner = Executive Secretary / Liza (Accountable); AI = Responsible drafting support | RC-007: assign single accountable draft owner (ES) with AI responsible support | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-008 | Registry contradicts 2026-07-05 standards (AC-08, P0) | DOCUMENT_REGISTRY.yaml | `ai_pmo_role: Support Only`, `final_approval_authority: Boss` vs. joint statements in standards | Registry statement is the correct baseline; standards must align to it | RC-008: align standards documents to registry baseline (Boss final, AI PMO support) | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-009 | Folder owners name PMO alone or jointly (AC-01 cand./AC-07, P1) | FOLDER_REGISTRY.yaml lines 26,31,36,41,61 | Folder Owner = `PMO` (alone or joint) | Named human Accountable owner per folder; AI PMO = Support Only | RC-009: reassign folder ownership to named accountable roles per Canonical RACI | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| ACF-010 | PMO terminology ambiguous across documents (AC-07, P1) | Cross-document | `PMO` used interchangeably for AI PMO and human authority | Single glossary: AI PMO = Support Only; no standalone `PMO` authority role | RC-010: introduce canonical role glossary and replace ambiguous `PMO` references | ES | GR (pending named) | EV (pending named) | CORRECTION PROPOSED |
| GII-001 | Issue #3 requires State 02 canonical package and closure control not yet delivered | GitHub Issue #3 | Closure control undefined in issue scope | Closure per Canonical RACI: ES prepares, GR reviews, EV verifies, Boss approves | Track against STEP 03–05 deliverables; close only after Boss approval | ES | GR (pending named) | EV (pending named) | OPEN |
| GII-002 | Issue #5 requires removal of outdated AI PMO ownership (P0) | GitHub Issue #5 | `Boss / PMO` joint approval present in governance documents | Boss sole Final Approver; AI PMO Support Only | Covered by RC-001, RC-004, RC-005, RC-006, RC-008, RC-010 | ES | GR (pending named) | EV (pending named) | READY FOR REVIEW |
| GII-003 | Issue #6 requires State/Domain Gate crosswalk | GitHub Issue #6 | Gate ownership crosswalk absent | Gate rows in Canonical RACI Section 3 provide the authority source | Derive gate crosswalk from Canonical RACI after Boss approval | ES | GR (pending named) | EV (pending named) | OPEN |
| GII-004 | Issue #9 requires evidence and classification registers | GitHub Issue #9 | Registers incomplete for State 02 | Registers per Canonical RACI: DC/CAI responsible, ES accountable | STEP 03/04 evidence registers created in this package contribute to closure | ES | GR (pending named) | EV (pending named) | READY FOR REVIEW |
| GII-005 | Issue #10 requires State 02 Gate review and Boss closure pack | GitHub Issue #10 | Gate review and closure pack pending | GTR recommends, Boss approves per Canonical RACI | Blocked until STEP 03–04 review/verification complete; tracked as STEP05-CLS-001 | ES | GR (pending named) | EV (pending named) | OPEN |
| GII-006 | PR #11 status terminology correction context | GitHub PR #11 | Status terminology previously inconsistent | Status vocabulary restricted to controlled set (no false PASS/COMPLETE) | Terminology rules embedded in all STEP 03–04 documents | ES | GR (pending named) | EV (pending named) | READY FOR REVIEW |

## 3. Control Statement

No row in this matrix is resolved. Resolution requires: Reviewer decision
(CONFIRM/RECLASSIFY), Verifier result (VERIFIED), Boss source-update authorization, an
applied and committed source correction, and post-correction verification evidence.
