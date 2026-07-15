# STATE04 — STEP0401 Scope and Acceptance Criteria

**Document ID:** STATE04-STEP0401-02
**Session ID:** SMEPLUS-26-07-16-002
**Current Prompt ID:** STEP040110
**Parent Prompt ID:** STEP040108
**Reference Prompt IDs:** STEP040107, STEP040102, STEP040101
**Jira Key:** ERPPLUS-97 (https://scgl.atlassian.net/browse/ERPPLUS-97)
**Evidence:** PR #35, PR #37; commits `f3bfc0a`, `cf4ef7f`, `f3a1412`, `4081709`
**Current State Status:** STATE04 — STEP0401 FORMALLY STARTED — IN PROGRESS

---

## 1. In Scope

- Evidence-source inventory
- Module inventory reconciliation
- Candidate classification controls
- Evidence ownership
- Source-of-truth mapping
- SHA-256 integrity
- Clean Room evidence control
- Gap tracking
- Controlled handoff preparation

## 2. Out of Scope

- Batch 1
- Controlled Delta Intake
- Functional Design drafting
- Source implementation
- Build / Release / Deploy / Production

## 3. Acceptance Criteria

| # | Criterion | Status at Commencement |
|---|---|---|
| 1 | 1,436 Controlled Learning Baseline reproducibly verified | PENDING — to be reconciled in Batch 1 execution; not claimed complete by this commencement |
| 2 | 808 Thailand-scope calculation verified | PENDING |
| 3 | 806 + 2 (l10n_th, l10n_th_reports) composition verified | PENDING |
| 4 | 69 Controlled Delta remains outside Active Baseline | HELD — enforced by this package (Section 8 of `01_STEP0401_FORMAL_COMMENCEMENT_RECORD.md`) |
| 5 | 1,505 not represented as Active Baseline | HELD — enforced by this package |
| 6 | Evidence Owners identified | RECORDED — role-based ownership in `01_STEP0401_FORMAL_COMMENCEMENT_RECORD.md` Section 11 |
| 7 | Sources and authority identified | RECORDED — `03_STEP0401_EVIDENCE_INPUT_REGISTER.csv` |
| 8 | SHA-256 validated | RECORDED — `04_STEP0401_PACKAGE_MANIFEST_SHA256.txt` (this package only) |
| 9 | No prohibited material | VERIFIED for this package at commencement |
| 10 | Clean Room 100% | VERIFIED for this package at commencement |
| 11 | Gaps traceable | RECORDED — GAP-005, GAP-007, GAP-008 carried forward unchanged |
| 12 | Independent Review handoff prepared | PENDING — deferred to Batch 1 |
| 13 | Boss Final Decision required before Step closure | ACKNOWLEDGED — no closure claimed by this commencement |

No acceptance criterion above is marked complete without corresponding evidence. Criteria 1–3 and 12 require the not-yet-authorized Batch 1 execution and are explicitly left PENDING by this commencement package; they are not satisfied by STEP040110.

## 4. Gate Status

| Gate | Status |
|---|---|
| PRE-STATE04 Batch 0 | CLOSED BY BOSS APPROVAL |
| STEP0401 | FORMALLY STARTED — IN PROGRESS |
| STEP0401 Completion | NOT AUTHORIZED / NOT DECLARED |
| Batch 1 | NOT STARTED |
| Controlled Delta Intake | PENDING |
| Build / Release / Deploy / Production | NOT AUTHORIZED |
