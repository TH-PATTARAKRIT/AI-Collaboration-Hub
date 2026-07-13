# STATE02_GOVERNANCE_FUNCTION_TO_DOCUMENT_MAP_v1.0.md

Session: [SMEPLUS-26-07-14-003] State 02 — Step 05 Blocker Resolution (refreshed from -002)
Prepared By: Claude Code (Authorized GitHub Execution Agent — mapping proposal only)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD — REVIEW, VERIFICATION, AND BOSS DECISION PENDING

Scope note: this map covers documents found under `State_02_Governance/` (State 02
scope). Several controlled functions (Project Constitution, PMO Standard,
Functional Specification / Architecture / QA-UAT / Release / Production
Governance) are governed by documents outside `State_02_Governance/` (e.g. in
`00_Project_Governance/` root) that were referenced by GOV-002/GOV-003/GOV-004 as
scan targets but are out of this Step 05 package's file-creation scope. Those
functions are recorded as GAP for State 02 Step 05 purposes — not because no
document exists anywhere in the repository, but because no State 02-scope primary
candidate exists. Boss/L99 may redirect this mapping to the repository-root
documents if that is the intended scope.

## Function Map

| Function ID | Governance Function | Primary Document Candidate | Supporting Documents | Evidence Documents | Owner | Reviewer | Verifier | Authority Conflict | Gap | Proposed Index Status |
|---|---|---|---|---|---|---|---|---|---|---|
| GF-01 | Project Constitution | None in State_02_Governance/ scope | — | GOV-005 references `APPROVAL_AUTHORITY_MATRIX.md` line 18 (root scope) | Boss (root doc, out of scope) | — | — | Referenced ACF-007 conflict (Constitution Draft Owner ambiguity) | GAP — root-scope document, not indexed by this package | GAP |
| GF-02 | Governance Principles | None in State_02_Governance/ scope | — | — | — | — | — | None found in scope | GAP — root-scope document | GAP |
| GF-03 | PMO Standard | None in State_02_Governance/ scope | GOV-002/003/004/009 (PMO ambiguity findings) | GOV-006 | — | — | — | ACF-009 (PMO folder-owner ambiguity), unresolved | GAP — root-scope document; State 02 only holds the conflict findings about it | GAP |
| GF-04 | Authority Model | GOV-020 (`STATE02_CANONICAL_RACI_v1.0.md`) | GOV-021, GOV-022, GOV-029 | GOV-023, GOV-024 | Boss (per RACI) | ChatGPT L99 (GOV-024, completed) | Claude Code (technical only — see GOV-034) | GOV-030/GOV-035 vs. PR #15 (unmerged) — see reconciliation matrix | None | PRIMARY CANDIDATE |
| GF-05 | RACI | GOV-020 | GOV-021, GOV-025, GOV-026 | GOV-023 | Boss | ChatGPT L99 | Claude Code (partial) | RC-007/RC-009 CORRECTION PROPOSED, not yet applied to source documents | None | PRIMARY CANDIDATE |
| GF-06 | Gate Control | GOV-014 (`STATE02_STEP03_STEP04_COMPLETION_CHECKLIST_v1.0.md`) | GOV-015, GOV-016, GOV-017 | GOV-018 | Executive Secretary / Liza (coordination) / Boss (decision) | ChatGPT L99 | Claude Code (partial) | None direct | Step 05 Governance Index (this package, GOV-039) is the next Gate-control artifact and is not yet finalized | PRIMARY CANDIDATE |
| GF-07 | Evidence Rule | GOV-016 (`STATE02_STEP03_STEP04_EVIDENCE_REGISTER_v1.0.md`) | GOV-023, GOV-032, this package's `STATE02_GOVERNANCE_INDEX_OPEN_ITEMS_REGISTER_v1.0.md` | GOV-004, GOV-006, GOV-008 | Executive Secretary / Liza | ChatGPT L99 (partial) | Claude Code (partial) | None | None | PRIMARY CANDIDATE |
| GF-08 | AI Governance | GOV-029 (`STATE02_AI_EXECUTION_AUTHORITY_MATRIX_v1.0.md`) | GOV-031 | GOV-032 | Boss (per RACI) | ChatGPT L99 | Claude Code (partial) | None | None | PRIMARY CANDIDATE |
| GF-09 | Ownerless Execution Control | GOV-031 (`STATE02_OWNERLESS_EXECUTION_CONTROL_STANDARD_v1.0.md`) | GOV-035, GOV-036 | GOV-032 | Explicitly "No Accountable Owner assigned" for the standard itself (by design — see Open Items OI-006) | ChatGPT L99 | Claude Code (partial) | GOV-035 disputed — see GF-04 | Accountable Owner of the standard document itself is unassigned by design; Boss decision needed on whether this is acceptable or requires assignment | CONFLICT (via GOV-035) |
| GF-10 | Escalation and Replacement | GOV-030 (`STATE02_ESCALATION_AND_REPLACEMENT_RULE_v1.0.md`) | GOV-036 | GOV-032 | Executive Secretary / Liza (repo text) / Boss (PR #15 proposed text) | ChatGPT L99 | Claude Code (partial) | **CONFLICT** — repo text vs. PR #15 (unmerged) | None | CONFLICT |
| GF-11 | Archive Control | None finalized in repository (PR #16 `STATE02_ARCHIVE_CANDIDATE_REGISTER_v1.0.md` / `STATE02_ARCHIVE_EXECUTION_REGISTER_v1.0.md` are open, not merged) | — | PR #16 archive result: 39 files inventoried, 0 qualified candidates, 0 moved, 0 deleted (see reconciliation matrix) | Claude Code (PR #16 author) | Not yet reviewed | Not yet verified | None | GAP — no merged Archive Control document exists in State_02_Governance/ yet | GAP |
| GF-12 | Document Control | This package's `STATE02_GOVERNANCE_DOCUMENT_INVENTORY_v1.0.md` | GOV-014 | — | Boss (per RACI) | Not yet reviewed | Not yet verified | None | None | PRIMARY CANDIDATE (this package) |
| GF-13 | Version Control | GOV-019, GOV-028 (SHA256 manifests) | This package's `STATE02_GOVERNANCE_INDEX_INTEGRITY_RECORD_v1.0.md` | GOV-018 | Executive Secretary / Liza | ChatGPT L99 (partial) | Claude Code (technical only) | STALE HASH on both GOV-019 (1 row) and GOV-028 (2 rows, partially fixed only in unmerged PR #17) | None | PRIMARY CANDIDATE — INTEGRITY EXCEPTION NOTED |
| GF-14 | Reviewer Control | GOV-005 (STEP 02 shell); GOV-024/GOV-033 (STEP 03/04 completed records) | GOV-007 | — | — | ChatGPT L99 (named role; STEP 03/04 completed, STEP 02 still shell) | — | None | STEP 02 Reviewer identity behind "ChatGPT L99" role still not separately named — see Open Items OI-009 | PRIMARY CANDIDATE (STEP 03/04) / GAP (STEP 02) |
| GF-15 | Verifier Control | GOV-007 (STEP 02 shell); GOV-034 (STEP 04 partial technical check) | GOV-027, GOV-038 (preparer structural checks) | — | — | — | No independent (non-preparer) Verifier has completed any State 02 verification to date | Independent Evidence Verifier identity not named anywhere in scope | GAP — this is the single largest open control gap in State 02 | GAP |
| GF-16 | Approval Control | No State-02-scope document defines this independently of GF-04 | GOV-020 (RACI approval column) | — | Boss (sole, per RACI) | ChatGPT L99 | — | None | None beyond GF-04 | SUPPORTING (folded into GF-04) |
| GF-17 | Functional Specification Governance | None in State_02_Governance/ scope | — | — | — | — | — | None found in scope | GAP — root-scope document | GAP |
| GF-18 | Architecture Governance | None in State_02_Governance/ scope | GOV-005 references `ARCHITECTURE_GOVERNANCE_STANDARD.md` line 31 (root scope) | — | — | — | — | Referenced conflict: "Boss / PMO authority required for gate movement" (root doc) | GAP — root-scope document | GAP |
| GF-19 | QA/UAT Governance | None in State_02_Governance/ scope | GOV-002 references `AI_ROLE_AND_RESPONSIBILITY.md` line 159 (root scope) | — | — | — | — | ACF-002 (QA/UAT Gate owner ambiguity), unresolved | GAP — root-scope document | GAP |
| GF-20 | Release Governance | None in State_02_Governance/ scope | — | — | — | — | — | None found in scope | GAP — root-scope document | GAP |
| GF-21 | Production Governance | None in State_02_Governance/ scope | GOV-005 references Production approval wording conflict (root scope) | — | — | — | — | Referenced conflict: Boss+PMO vs. Boss-only Production approval (root doc) | GAP — root-scope document | GAP |
| GF-22 | Jira/GitHub Traceability | GOV-008 (`STATE02_GITHUB_ISSUE_AUTHORITY_SCAN_ADDENDUM_v0.1.md`) | GOV-015 (crosswalk includes GII-006=PR #11), this package's reconciliation matrix (PR #13/#15/#16/#17) | GOV-013 | Executive Secretary / Liza | ChatGPT L99 (partial) | Claude Code (partial) | None | Jira ERPPLUS-94 update for this Step 05 package still pending (see Section 12 of the execution instruction) | PRIMARY CANDIDATE |
| GF-23 | Governance Index | This package's `STATE02_GOVERNANCE_INDEX_v1.0.md` | This package (all files) | This package's integrity record and open items register | Boss (per RACI) | Not yet reviewed | Not yet verified | None | None | PRIMARY CANDIDATE (this package — status remains PREPARED FOR INDEPENDENT REVIEW, not Canonical) |
| GF-24 | Governance Closure | PR #16's `Closure_Evidence/STATE02_CLOSURE_EVIDENCE_INDEX_v1.0.md` (open, not merged) | This package's Open Items Register and Boss Decision Pack | PR #16's Closure Evidence Pack (7 files, open) | Executive Secretary / Liza (coordination) / Boss (decision) | Not yet reviewed | Not yet verified | None | State 02 closure decision itself — PENDING BOSS DECISION | PENDING BOSS DECISION |

## Coverage Check

24 functions listed (minimum required set). Each function above has exactly one
Primary Document Candidate, or is explicitly marked GAP, CONFLICT, or PENDING BOSS
DECISION — no function is left silently unaddressed.

- PRIMARY CANDIDATE: GF-04, GF-05, GF-06, GF-07, GF-08, GF-12, GF-13, GF-14 (STEP 03/04 portion), GF-22, GF-23 (10)
- SUPPORTING: GF-16 (1)
- CONFLICT: GF-09 (via GOV-035), GF-10 (2)
- GAP: GF-01, GF-02, GF-03, GF-11, GF-14 (STEP 02 portion), GF-15, GF-17, GF-18, GF-19, GF-20, GF-21 (11)
- PENDING BOSS DECISION: GF-24 (1)
