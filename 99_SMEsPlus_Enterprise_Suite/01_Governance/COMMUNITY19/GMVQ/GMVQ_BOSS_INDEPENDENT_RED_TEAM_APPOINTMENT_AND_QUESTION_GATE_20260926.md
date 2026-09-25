# SMEsPlus ENTERPRISE SUITE — Boss Directive
## Appointment of Independent RED TEAM for GVQ/MVQ Question Review

**Directive date:** 2026-09-26 (Asia/Bangkok)  
**Authority:** Boss, sole Final Approver  
**Scope:** Odoo 19 Community reference research, GMVQ General Verification Questions (GVQ) and Module Verification Questions (MVQ), G01–G16  
**Status:** BOSS APPROVED — effective for question handoff immediately; repository integration pending review of this record  
**Parent control:** Existing canonical VDR and GMVQ governance. This directive changes the question release gate; it does not create another VDR universe, denominator, or Constitution.

## 1. Appointment and independence

Boss appoints an **Independent RED TEAM** separate from the OVQDT/GMVQ question authors. The team has four Special Expert seats:

| Seat | Responsibility for every applicable QID |
|---|---|
| Special Expert Odoo Functional Consultant / BA | Challenge business meaning, workflow ownership, process variation, cross-module handoffs, optionality, and missing/duplicated functional questions. |
| Special Expert Odoo Technical Specialist / Architect | Challenge technical premises, Community-source scope, dependencies, security/access, configuration conditions, source/runtime distinctions, and clean-room boundaries. |
| Special Expert SaaS Architecture Consultant / Adversarial Reviewer | Attempt to disprove hypotheses; challenge tenant/company boundaries, invariants, blind assumptions, negative cases, and cross-module risks. |
| Special Expert Tester / QA | Verify unique QID, unambiguous testability, concrete disconfirming observation, negative/role/state cases, traceability, and repeatable acceptance evidence. |

These are **role appointments**, not a claim that named employees or external auditors have been hired or signed. Each review record must identify the actual reviewer/agent, role, affiliation, review time, artifact revision/hash, and conflict-of-interest declaration. A person/agent who authored or materially revised a QID may not certify that QID as its independent reviewer. Historical “RED TEAM” authorship, including any GVQ Standard questions written by an earlier RED TEAM, must be checked for reviewer separation; if it cannot be proved, that QID is **INDEPENDENCE HOLD**.

The Independent RED TEAM reports **directly and only to Boss**. OVQDT may receive defect tickets and corrected question requests; OVQDT does not approve, suppress, or alter independent conclusions. Boss is the sole Final Approver of material governance decisions. No AI recommendation is a Boss Final Approval.

## 2. Mandatory question release gate

For **every GVQ and every MVQ**, before any answering team receives the question for response:

1. OVQDT provides the exact question revision, QID, module/group, type, author/provenance, hypothesis, why it matters, risk tier, expected evidence/proof, and concrete `DISCONFIRMING_OBSERVATION`.
2. All four Independent RED TEAM seats assess the QID, or record a justified `N/A` for a seat with explicit independent acceptance by QA and a traceable reason. A blank result is never PASS.
3. Findings are returned to OVQDT for controlled correction; any material revision invalidates earlier signoffs for that QID and requires re-review.
4. RED TEAM records per-QID `PASS / CONDITIONAL / HOLD / FAIL`, reviewer identities, independent conflict check, rationale, evidence pointers, artifact SHA-256, and unresolved issues. `CONDITIONAL` cannot be dispatched while conditions remain open.
5. Only a fully cleared `INDEPENDENT QUESTION REVIEW PASS` with no open critical/material defect may advance that **exact revision** to `READY FOR ANSWER`. A new revision re-enters the gate.
6. A group/batch or standard-bank summary may be issued only from the underlying QID-level records. Missing QIDs, unverifiable roster, duplicate QIDs, missing hashes, missing reviewers, or open critical defects cause HOLD.
7. The RED TEAM sends its report and exceptions straight to Boss. Material scope/architecture decisions and disputes await Boss decision.

A prior OVQDT Functional/QA/SaaS/Adversarial check or Rolling Freeze is **author-side internal quality control**. It does not substitute for this Independent RED TEAM gate. A frozen authoring bank remains frozen as a historical revision; its release status may be `INDEPENDENT REVIEW PENDING` without rewriting history.

## 3. Existing inventory at appointment

- GVQ: 55-question standard bank; exact freeze/version labeling and provenance must be reconciled against the bank and manifest before independent disposition. Historical authorship of STD-Q01–Q35 requires recusal validation.
- G01 MVQ: reported 795 questions in 19 module banks under OVQDT rolling freezes B01–B11. Treat all 795 as `INDEPENDENT REVIEW PENDING` until individual RED TEAM records prove otherwise. Author-side QA depth differs between B01–B03 and B04–B11; no batch inherits independent PASS.
- G01 remaining module banks: `resource`, `resource_mail`, `web_hierarchy`, `web_unsplash` require authoring and the same independent gate.
- G02–G16: roster evidence must be verified before claiming module membership or issuing module-specific release; retain `EVIDENCE POINTER NOT VERIFIED / HOLD` when absent.
- Earlier valid research/source evidence may be carried forward with lineage, but no prior QID answer is newly certified by this directive. Reconcile already answered QIDs against independently approved exact question revisions before using them as governed answer/progress credit.

## 4. Required per-QID review record

`QID | GROUP | MODULE | GVQ/MVQ | QUESTION_REVISION | QUESTION_SHA256 | AUTHOR | REVIEWER_FUNCTIONAL | REVIEWER_TECHNICAL | REVIEWER_SAAS_ADVERSARIAL | REVIEWER_QA | INDEPENDENCE_CHECK | HYPOTHESIS | DISCONFIRMING_OBSERVATION | EVIDENCE_EXPECTED | FINDINGS | CORRECTION_REVISION | FOUR_SEAT_DISPOSITION | UNRESOLVED_CRITICAL | RELEASE_STATUS | REVIEW_TIMESTAMP | SOURCE_POINTER`

A review report must disclose total in scope, examined QIDs, PASS/CONDITIONAL/HOLD/FAIL counts, exclusions with reasons, duplicates, missing question records, material findings, and SHA-256 of input and output. Sampling may discover defects but cannot assert that unexamined questions passed the mandatory **every-question** gate.

## 5. Boundaries

- Odoo 19 **Community** is reference material for learning and verification only; do not study Odoo Enterprise in this scope or clone its schema, code, ORM, workflows, or UI into SMEsPlus.
- This question gate is distinct from A1 Source/Static study, A2 runtime verification, A3 adversarial evidence review, MASTER reconciliation, and later formal VDR gates. Do not answer QIDs or start prohibited answer lanes merely because a bank was internally frozen.
- No Evidence = No Progress; Unknown is not PASS; no skipped gate.
- Question counts are not Functional Coverage. No Formal Coverage before Boss freezes the canonical Function-ID denominator; applicable dimensions require at least 96%, critical/Zero-Tolerance controls 100%.
- Preserve superseded manifests and prior evidence with provenance. Never silently relabel an author-side review as independent.
- Standing user instruction to pause Jira and Slack updates remains in force until a later explicit change.

**Boss decision:** Appointment and mandatory pre-answer Independent RED TEAM question gate APPROVED on 2026-09-26. Individual QID dispositions remain PENDING REVIEW.