# ACC-001 Evidence Register

Document ID: SMEPLUS-STATE04-ACC-EVD-001
Owner: Functional Specification AI
Reviewer: Not yet assigned
Approver: Boss / Final Gate Owner
Status: DRAFT
Gate Status: HOLD
Generated: 2026-07-07

## Evidence Rule
A requirement cannot be counted as progress unless evidence is inspectable and
tied to the work item. This register only records evidence that was actually
found during repository inspection this session — nothing here is inferred or
assumed.

## Evidence Register

| Evidence ID | Requirement ID | Evidence Description | GitHub Path / File | Owner | Timestamp | Verifier / Reviewer | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| EVD-04-ACC-001-DOC-20260707-001 | FR-ACC-001 through FR-ACC-020 | Primary FDS document defining all 20 Accounting FRs, 10 BRs, 4 workflows, 12 data entities, 15 APIs, 15 screens, 10 acceptance criteria | `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` | Functional Specification AI | 2026-07-01 (document date, per repo) | Not yet reviewed | Present, unreviewed | HOLD |
| EVD-04-ACC-001-DOC-20260707-002 | FR-ACC-001 (Vendor Bill / 3-way match specifically) | Cross-checked against real Odoo source (`01_ACCOUNT.zip`, `02_OTHER.zip`) and live PostgreSQL dump (`iTEST02_2026-06-14_14-41-19.dump`, read via embedded DDL since `pg_restore` could not open the v1.16 dump format) — status PARTIAL/MATCHED | `12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.2.md` | Claude (prior session, per document) | 2026-07-02 (per document's stated evidence-matching date) | Not independently reverified this session | Present, independently sourced (primary evidence) | HOLD |
| EVD-04-ACC-001-DOC-20260707-003 | FR-ACC-002 through FR-ACC-010, FR-ACC-014, FR-ACC-016, FR-ACC-017 | Internal module-level traceability (FR→BR→DB→API→UI→AC) exists inside ACC-001 itself (§12), now also extracted into a standalone matrix this batch | `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` §12; `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md` (this batch) | Functional Specification AI | 2026-07-07 (extraction date) | Not yet reviewed | Present, unreviewed | HOLD |
| EVD-04-ACC-001-DOC-20260707-004 | FR-ACC-011, FR-ACC-012, FR-ACC-013, FR-ACC-015, FR-ACC-018, FR-ACC-019, FR-ACC-020 | No traceability mapping evidence exists for these 7 FRs anywhere in the repository | — | — | — | **MISSING** | HOLD / FAIL candidate if required for this gate |
| EVD-04-ACC-001-DOC-20260707-005 | Thai VAT (ภ.พ.30) / WHT compliance detail | ACC-001 §13 records this evidence itself as "Pending Legal Review" — i.e., the source document discloses its own evidence gap | `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` §13 | Accounting Owner / Legal (not yet assigned by name) | — | Not started | Disclosed gap, not closed | HOLD |
| EVD-04-ACC-001-DOC-20260707-006 | API / DB / UI mapping (§8, §9, §10 of ACC-001) | ACC-001 §13 records these as "Draft" (Functional AI design only, no architecture review yet) | `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` §8–10, §13 | Enterprise Architect AI (not yet performed) | — | Not started | Disclosed gap, not closed | HOLD |
| EVD-04-ACC-001-DOC-20260707-007 | Duplicate folder finding D-01 | `diff -rq` confirms `02_Functional_Design/02_Functional_Design/` and `02_Functional_Design/02_Functional_Design_v2/` are byte-identical (13 files) | `07_Output_From_AI/Repository_Audit_2026-07-05/DUPLICATE_FILE_REGISTER.md` (pre-existing) + this session's `diff -rq` re-verification | Claude (this session, re-verification only) | 2026-07-07 | Not independently reviewed | Confirmed present, unresolved | HOLD |
| EVD-04-ACC-001-DOC-20260707-008 | ACC-002 through ACC-005 (standalone module FDS) | No file existed anywhere in the repository under these names prior to this batch; draft files created this batch from ACC-001 content, not from new requirements | `02_Functional_Design/ACC-002 Functional Design Specification.md` through `ACC-005 Functional Design Specification.md` (this batch) | Functional Specification AI | 2026-07-07 | Not yet reviewed | New draft, unreviewed | HOLD |

## Verification Status Legend
- **Present, unreviewed** — the artifact exists and was inspected this session, but no independent reviewer has signed off
- **Present, independently sourced** — evidence traced to a primary source (code/DB), not just another document
- **Missing** — no evidence artifact found
- **Disclosed gap, not closed** — the source document itself already states the gap; this register does not newly discover it, only surfaces it for batch review

## Gate Impact Summary
All rows carry Gate Impact = HOLD. No evidence in this register is sufficient, on its own, to move Functional Design gate to PASS.
