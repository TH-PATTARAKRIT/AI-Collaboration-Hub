# STATE02_RACI_SOURCE_DOCUMENT_UPDATE_PLAN_v0.1.md

Session: SMEPLUS-26-07-13-007
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Intake Branch: claude/state-02-step-03-04-sn0sr1
Reference Base Commit: 5454d2afb2efb4d5f2def0a744981b812b843982
Prepared By: Claude AI (Responsible role only)
Prepared At: 2026-07-13T16:16Z (UTC)
Document Status: DRAFT
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Rule

No source governance document is modified in STEP 03. This plan is the only controlled
container for proposed source changes. Application requires, per correction:

```text
1. Reviewer Decision = CONFIRM or RECLASSIFY (named Independent Governance Reviewer)
2. Verifier Result = VERIFIED (named Independent Evidence Verifier)
3. Boss source-update authorization (explicit, recorded)
4. Execution by Authorized GitHub Execution Agent with real Commit SHA
5. Post-correction verification against the new commit
```

## 2. Update Plan by Source Document

### Phase 1 — RC-010: Canonical Role Glossary (prerequisite for all text edits)

- Add a canonical role glossary (role codes and authority baselines from
  STATE02_CANONICAL_RACI_v1.0.md Section 2) to the governance standards set.
- Replace ambiguous standalone `PMO` references with explicit `AI PMO (Support Only)`
  or the correct human role.
- Affected: all State 02 governance documents flagged in ACF-010.

### Phase 2 — RC-008: DOCUMENT_REGISTRY.yaml baseline alignment

- The registry values `ai_pmo_role: Support Only` and `final_approval_authority: Boss`
  (blob 2c31ee69) are the correct baseline. Standards documents are corrected TO the
  registry; the registry itself requires no authority change in this phase.

### Phase 3 — APPROVAL_AUTHORITY_MATRIX.md (RC-005, RC-006, RC-007)

- Line 23: `Boss / PMO` → `Boss` (FDS Final Approver).
- Line 24: `Boss / PMO` → `Boss` (SDS/API/DB/UX Final Approver).
- Line 18: `Liza / PMO AI` → `Executive Secretary / Liza (Accountable), AI drafting support (Responsible)`.

### Phase 4 — AI_ROLE_AND_RESPONSIBILITY.md (RC-001, RC-002, RC-003)

- Line 160: `PMO + Boss` → `Boss` as Build Gate Approver; AI PMO = Support Only.
- Line 159: `QA AI + PMO` → `Boss` as QA/UAT Gate Approver; QA AI and AI PMO =
  Responsible execution support.
- Line 95: `Boss and PMO Gate` → `Boss` only for production approval.

### Phase 5 — ARCHITECTURE_GOVERNANCE_STANDARD.md (RC-004)

- Line 31: `Boss / PMO authority` → `Boss approval` for gate movement; AI PMO =
  tracking support.

### Phase 6 — FOLDER_REGISTRY.yaml (RC-009)

- Lines 26, 31, 36, 41, 61: replace `PMO` owner entries with the named accountable
  role per the Canonical RACI (Document Control for registry folders, Executive
  Secretary / Liza for coordination folders, Technical Owner for technical folders —
  exact per-folder assignment to be confirmed in review).

## 3. Evidence Requirements per Applied Change

Each applied change must record: original text, new text, file path, line/section,
blob SHA before and after, Commit SHA, executor identity, Boss authorization
reference, and verifier result.

## 4. Status

```text
PLAN STATUS: DRAFT
SOURCE UPDATE AUTHORIZATION: NOT GRANTED
APPLIED CHANGES: 0
```
