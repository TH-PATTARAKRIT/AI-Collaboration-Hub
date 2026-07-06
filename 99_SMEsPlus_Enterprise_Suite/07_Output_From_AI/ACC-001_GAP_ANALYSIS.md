# ACC-001 Gap Analysis

Version: v1.0
Status: Review Required
Owner: Functional Specification AI
Reviewer: Claude AI / PMO AI / Accounting-Legal Reviewer
Project: SMEsPlus Enterprise Suite
Control Level: L99
Created: 2026-07-07T01:31:49+07:00
Gate Impact: FDS Gate / Traceability Gate / Build Gate

---

## Purpose

This file records open gaps for ACC-001 Accounting Thailand Functional Design Specification. It converts prior draft notes into a real repository evidence artifact. It does not approve the module.

---

## L99 Rule

No Evidence = No Progress.

A gap remains open until owner, evidence location, timestamp, reviewer and verification status are complete.

---

## Gap Register

| Gap ID | Area | Gap | Impact | Owner | Evidence Required | Current Evidence | Verification Status | Gate Impact | Status | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|
| GAP-ACC-001 | Thai Tax / VAT | VAT legal handling, VAT month, output/input VAT and ภ.พ.30 rules require accounting/legal review | Compliance risk | Accounting-Legal Reviewer | Thai accounting/tax requirement confirmation and reviewed FDS comments | ACC-001 FDS Section 6, 11, 13 | Pending Review | FDS / QA / UAT | OPEN | Accounting/legal reviewer must validate VAT scope |
| GAP-ACC-002 | Withholding Tax | WHT rate, expense type mapping and certificate flow require owner validation | Compliance risk | Accounting-Legal Reviewer | WHT rule matrix and reviewed certificate requirement | ACC-001 FDS Section 6, 11, 13 | Pending Review | FDS / QA / UAT | OPEN | Define WHT categories and certificates required for Phase 1 |
| GAP-ACC-003 | e-Tax / e-Receipt | Phase 1 vs later phase is not decided | Scope risk | Boss | Decision record | ACC-001 Open Question OQ-ACC-001 | Not Verified | FDS / Integration | OPEN | Boss decision required |
| GAP-ACC-004 | Currency | THB-only or multi-currency is not decided | DB/API/reporting impact | Boss / Finance Owner | Phase scope decision | ACC-001 Open Question OQ-ACC-002 | Not Verified | DB / API / FDS | OPEN | Confirm currency scope before SDS/DB design |
| GAP-ACC-005 | Cost Center / Project Accounting | Phase inclusion is not decided | GL/reporting impact | Finance Owner / Boss | Phase scope decision and reporting requirement | ACC-001 Open Question OQ-ACC-003 | Not Verified | FDS / DB / UX | OPEN | Confirm cost center and project accounting scope |
| GAP-ACC-006 | Tax Report Export | Export format for ภ.พ.30 / ภ.ง.ด.3 / ภ.ง.ด.53 is not defined | UAT and compliance ambiguity | Accounting Owner | Export format specification | ACC-001 Open Question OQ-ACC-004 | Not Verified | FDS / QA / UAT | OPEN | Define required report formats and test cases |
| GAP-ACC-007 | Bank Integration | Real bank connection vs bank statement import is undecided | API/integration risk | Boss / Finance Owner | Integration approach decision | ACC-001 Open Question OQ-ACC-005 | Not Verified | API / Integration / Security | OPEN | Confirm Phase 1 bank method |
| GAP-ACC-008 | DB Design Evidence | DB entities are draft and not reviewed by Database Design AI | SDS/DB risk | Database Design AI | Entity model review and canonical table mapping | ACC-001 FDS Section 8 | Draft | DB Gate | OPEN | Convert data entities into reviewed DB design artifact |
| GAP-ACC-009 | API Contract Evidence | API endpoints are draft and not reviewed by Architecture/API owner | API contract risk | Enterprise Architect AI / API Owner | API contract review | ACC-001 FDS Section 9 | Draft | API Gate | OPEN | Convert API mapping into reviewed API contract |
| GAP-ACC-010 | UI/UX Evidence | Screen mapping exists but no Figma/UX evidence is linked | UX readiness risk | Figma UX/UI AI | Figma screen evidence or UX review artifact | ACC-001 FDS Section 10 | Draft | UX Gate | OPEN | Produce UX screen flow and evidence links |
| GAP-ACC-011 | QA/UAT Evidence | Acceptance criteria exist but no formal test cases are reviewed | QA readiness risk | QA/UAT AI | Test case register and UAT scenarios | ACC-001 FDS Section 11 | Draft | QA / UAT Gate | OPEN | Produce ACC-001 test case package |
| GAP-ACC-012 | Claude Review | Claude review and evidence matching are still pending | Gate cannot pass | Claude AI | Review summary, gap list, risk list, evidence decision | ACC-001 Section 15 | Pending | FDS Gate | OPEN | Send ACC-001 to Claude review |
| GAP-ACC-013 | PMO Evidence Review | Evidence register exists but has partial/pending items | Evidence Gate cannot pass | PMO AI / Liza | Verified evidence register | `07_Output_From_AI/ACC-001_EVIDENCE_REGISTER.md` | Partial | Evidence Gate | OPEN | PMO must verify each evidence row |
| GAP-ACC-014 | Build Readiness | FDS, SDS, API, DB, UX, QA and Traceability are not all passed | Build must remain HOLD | PMO AI / Boss | Build readiness decision pack | Quality Gate Standard | Not Approved | Build Gate | HOLD | Do not start feature coding |

---

## L99 Decision

```text
ACC-001 GAP status = OPEN / REVIEW REQUIRED
ACC-001 may continue to review.
ACC-001 may not proceed to Build.
```

---

## End
