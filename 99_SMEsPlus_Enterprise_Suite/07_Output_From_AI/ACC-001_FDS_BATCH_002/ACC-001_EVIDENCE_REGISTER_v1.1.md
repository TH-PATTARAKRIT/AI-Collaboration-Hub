# ACC-001 Evidence Register v1.1

Document ID: SMEPLUS-ACC001-EVD-v1.1
Previous Version: SMEPLUS-STATE04-ACC-EVD-001 (8 rows)
Version: v1.1
Batch: FDS-ACC-BATCH-002
Status: DRAFTED — REQUIRES PMO VERIFICATION
Gate Status: HOLD / REVIEW REQUIRED
Owner: Functional Specification AI
Revised By: Claude AI (/L99.99, FDS-ACC-BATCH-002)
Generated: 2026-07-08 (Asia/Bangkok)

---

## Evidence Rule

No Evidence = No Progress. A requirement cannot be counted as progress unless evidence is inspectable and tied to the work item. Status values: EVIDENCED / PARTIAL_EVIDENCE / NO_EVIDENCE / ASSUMPTION / OPEN_QUESTION / GAP / OUT_OF_SCOPE / LEGAL_TAX_REVIEW_REQUIRED.

---

## Evidence Register

### Carried Forward from v1.0 (updated status)

| Evidence ID | Requirement | Evidence Description | File / Location | Owner | Timestamp | Verifier | Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| EVD-04-ACC-001-DOC-20260707-001 | FR-ACC-001 through FR-ACC-020 | Primary FDS v1.0 document — all 20 FRs, 10 BRs, 4 WFs, 12 entities, 15 APIs, 15 screens, 10 ACs | `02_Functional_Design/ACC-001 ... Package.md` (v1.0) | Functional Specification AI | 2026-07-01 | Claude AI — State 3 review (2026-07-07) | PARTIAL_EVIDENCE — reviewed, revision required | HOLD |
| EVD-04-ACC-001-DOC-20260707-002 | FR-ACC-001 (vendor bill / 3-way match) | Cross-checked against PostgreSQL dump and Odoo source | `12_Traceability/...MATCHING-MATRIX-v0.2.md` | Claude (prior session) | 2026-07-02 | Not independently re-verified | PARTIAL_EVIDENCE | HOLD |
| EVD-04-ACC-001-DOC-20260707-003 | FR-ACC-002 to 010, 014, 016, 017 | Internal traceability §12 + standalone matrix | ACC-001 §12; ACC-001_TRACEABILITY_MATRIX.md (State 4) | Functional Specification AI | 2026-07-07 | Claude AI — State 3 confirmed matrix accurate | PARTIAL_EVIDENCE — matrix confirmed, not independently verified against source | HOLD |
| EVD-04-ACC-001-DOC-20260707-004 | FR-ACC-011/012/013/015/018/019/020 | No traceability existed for these 7 FRs in v1.0 | — | — | — | MISSING in v1.0; addressed in v1.1 (see EVD-v1.1 rows) | GAP → PARTIAL in v1.1 | HOLD |
| EVD-04-ACC-001-DOC-20260707-005 | Thai VAT/WHT compliance detail | v1.0 recorded as "Pending Legal Review" | ACC-001 §13 (v1.0) | Accounting Owner / Legal | — | Not started | GAP → PARTIAL in v1.1 (§6-B authored; legal review not done) | HOLD |
| EVD-04-ACC-001-DOC-20260707-006 | API/DB/UI mapping | v1.0 recorded as "Draft" | ACC-001 §8-10 (v1.0) | Enterprise Architect AI | — | Not done | PARTIAL_EVIDENCE — extended in v1.1; architecture review pending | HOLD |
| EVD-04-ACC-001-DOC-20260707-007 | Duplicate folder D-01 | Byte-identical duplicate verified | DUPLICATE_FILE_REGISTER.md | Claude (re-verification) | 2026-07-07 | Not resolved | PARTIAL_EVIDENCE — confirmed, unresolved | HOLD |
| EVD-04-ACC-001-DOC-20260707-008 | ACC-002 to ACC-005 standalone files | New draft split files created | `02_Functional_Design/ACC-002 to 005 ...md` | Functional Specification AI | 2026-07-07 | Not yet reviewed | PARTIAL_EVIDENCE — exist, content unreviewed | HOLD |

### Added at State 3 Review (2026-07-07)

| Evidence ID | Requirement | Evidence Description | File / Location | Owner | Status | Gate Impact |
|---|---|---|---|---|---|---|
| EVD-03-ACC-001-REV-20260707-001 | Gate report action #1 | Claude State 3 review executed | `07_Output_From_AI/ACC-001_State3_Review/ACC-001_CLAUDE_STATE3_REVIEW_COMMENTS.md` | Claude AI | PARTIAL_EVIDENCE — requires PMO registration and ChatGPT L99 review | HOLD |
| EVD-03-ACC-001-REV-20260707-002 | Gap register | Confirmation of 8 existing + 7 new gaps | `07_Output_From_AI/ACC-001_State3_Review/ACC-001_REMAINING_GAPS_CONFIRMATION.md` | Claude AI | PARTIAL_EVIDENCE — requires PMO registration | HOLD |
| EVD-03-ACC-001-REV-20260707-003 | Revision planning | FDS-ACC-BATCH-002 scope proposal | `07_Output_From_AI/ACC-001_State3_Review/ACC-001_REVISION_SCOPE_PROPOSAL.md` | Claude AI | PARTIAL_EVIDENCE — requires PMO registration | HOLD |

### Added at FDS-ACC-BATCH-002 Revision (2026-07-08)

| Evidence ID | Requirement | Evidence Description | File / Location | Owner | Status | Gate Impact |
|---|---|---|---|---|---|---|
| EVD-v1.1-001 | FR-ACC-001 to 020 (all 20 FRs, traceability, API, DB, UI, AC) | ACC-001 v1.1 revised FDS — REV-01 to REV-09 addressed | `07_Output_From_AI/ACC-001_FDS_BATCH_002/ACC-001 Accounting Thailand Functional Design Specification Package v1.1.md` | Claude AI (draft) | PARTIAL_EVIDENCE — drafted, not reviewed; requires ChatGPT L99 + PMO + Accounting Owner | HOLD |
| EVD-v1.1-002 | §6-B Thai Tax Annex (TH-01 to TH-09) | Thai tax rule detail authored — all items tagged LEGAL_TAX_REVIEW_REQUIRED | §6-B of ACC-001 v1.1 | Claude AI (draft) | LEGAL_TAX_REVIEW_REQUIRED — authored, not legally reviewed; legal reviewer not yet named | HOLD |
| EVD-v1.1-003 | §6-A Posting Rules (PR-ACC-001 to PR-ACC-008) | Accounting Dr/Cr posting rules authored | §6-A of ACC-001 v1.1 | Claude AI (draft) | PARTIAL_EVIDENCE — authored, Accounting Owner review required before development | HOLD |
| EVD-v1.1-004 | Gap Analysis v1.1 | Updated gap register — 15 gaps, dispositions recorded | `ACC-001_GAP_ANALYSIS_v1.1.md` | Claude AI (draft) | PARTIAL_EVIDENCE — requires PMO verification | HOLD |
| EVD-v1.1-005 | Traceability Matrix v1.1 | All 20 FRs mapped, mis-mapping corrected | `ACC-001_TRACEABILITY_MATRIX_v1.1.md` | Claude AI (draft) | PARTIAL_EVIDENCE — requires reviewer confirmation | HOLD |
| EVD-v1.1-006 | REV-08 Boss Decision Items | OQ-ACC-007 to OQ-ACC-014 / REV-08 scope items deferred | §3 Out of Scope, §16 OQ register (ACC-001 v1.1) | Boss | NO_EVIDENCE — Boss decisions not yet made | HOLD |

---

## Gate Impact Summary

All rows carry Gate Impact = HOLD. Two new LEGAL_TAX_REVIEW_REQUIRED rows (EVD-v1.1-002, 003) and one NO_EVIDENCE row (EVD-v1.1-006) are the highest-priority gaps. No evidence row in this register is sufficient, on its own, to move any gate to PASS.

PREPARED ONLY / NOT APPROVED / REQUIRES PMO VERIFICATION AND CHATGPT L99 REVIEW
