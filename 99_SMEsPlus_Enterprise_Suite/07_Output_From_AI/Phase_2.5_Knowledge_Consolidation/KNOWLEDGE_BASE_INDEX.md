# KNOWLEDGE_BASE_INDEX.md

**Document ID:** SMEPLUS-26-07-05-001-KBI
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Status: This document is the Entry Point for all extracted SMEsPlus knowledge.**
**Prepared by:** Claude, acting as Knowledge Engineer
**Date:** 2026-07-05

## Purpose
Single navigation point for every Phase 2.5 deliverable and the underlying repository evidence each one draws from — so the Architecture Team can go straight to Functional Design (Phase 3) without repeating any learning activity.

## Dependencies
All Phase 2.5 deliverables listed below; underlying repository evidence listed in §3.

## Source Evidence
This index does not introduce new facts — it points to facts already established in the other seven Phase 2.5 documents.

## Confidence Level
Inherits the confidence level of each linked document (see each document's own header).

## Known Gaps
Three process-level gaps are open and require Boss/PMO decision before Phase 3 begins — see §2.

## Recommended Next Step
Start Phase 3 Functional Design from `01_SaaS_Foundation/FDS/` (already Draft/In-Review) and `17_Functional_Specification_Factory/02_Purchase/` (already evidence-matched), using this index and its linked deliverables as the starting context — do not re-run Learning Source Code, Learning Database, or Learning Filestore.

---

## 1. Phase 2.5 Deliverables (This Package)

| # | Document | Answers |
|---|---|---|
| 1 | `KNOWLEDGE_CONSOLIDATION_REPORT.md` | What do we already know, from Source Code, Database, Business, and Architecture learning — and where is that knowledge weak or conflicting? |
| 2 | `BUSINESS_RULE_CATALOG.md` | What business rules already exist, organized by category, traced to Functional Requirements? |
| 3 | `CANONICAL_DATA_MODEL.md` | What are the core entities and their relationships, at a conceptual level, with no implementation detail? |
| 4 | `MODULE_DEPENDENCY_MATRIX.md` | Which module depends on which, who owns it, and what's the Input/Output/Table/API status? |
| 5 | `BUSINESS_CAPABILITY_MAP.md` | Which capabilities are Core, Supporting, Shared, or Platform? |
| 6 | `SOURCE_TO_BUSINESS_MAPPING.md` | Which real Odoo source module maps to which SMEsPlus business process and target module? |
| 7 | `OPEN_SOURCE_TO_SMESPLUS_GAP.md` | For every capability: Reuse, Adapt, Replace, New, or Retire — and why? |
| 8 | `KNOWLEDGE_BASE_INDEX.md` (this document) | Where do I start, and what's still open? |

## 2. Open Items Requiring Boss/PMO Decision Before Phase 3

| ID | Item | Where Detailed |
|---|---|---|
| 🔴 GAP-KC-01 | `16_Learning_Analysis/` conflicts with the grounded evidence base and should not be used as a Phase 3 source until Boss/PMO rules on its disposition | `KNOWLEDGE_CONSOLIDATION_REPORT.md` §4, `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §6 |
| 🔴 GAP-KC-02 | Two parallel requirement-ID taxonomies exist (FD-001–030 vs. FR-TEN/FR-CMP/...) with no published crosswalk | `KNOWLEDGE_CONSOLIDATION_REPORT.md` §5, `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §6 |
| 🔴 GAP-KC-03 | `Other_Unclassified` module group (293 tables, the largest single group in the schema) is not capability-classified | `BUSINESS_CAPABILITY_MAP.md` §5, `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §6 |
| GAP-KC-04 | `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md` lists ADR-0001–0010 with no underlying evidence files — same pattern as GAP-KC-01. **Boss decision, 2026-07-05: acknowledged, recorded as-is, original file NOT to be modified, will be corrected gradually. Closed for AI action; no further escalation needed.** | `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §7 |
| GAP-TH-01 (raised and closed same day) | Thai Withholding Tax Certificate structure was found live in the DB dump with no matching source in either original zip. **RESOLVED 2026-07-05: Boss provided the source (`Archive.zip`, OCA `l10n-thailand`), field-verified as a 100% match. Reclassified to REUSE.** | `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §1, §3a, §7a; `ADR-0004` Addendum 2 |

## 2b. Open Registry Question From GAP-TH-01 Resolution — RESOLVED/MOOT (2026-07-06)

~~The Boss-provided WHT suite is real Python module source code (AGPL-3, OCA `l10n-thailand`)...~~
**Superseded by ADR-0006 (2026-07-06):** under Clean Room Policy A and the confirmed FastAPI/
Next.js/SQLAlchemy technology stack (`TECHNOLOGY_STACK_STANDARD.md`), this code is not installed
into the SMEsPlus codebase at all — so the "which repo/path should it live in as a dependency"
question no longer applies. It may be kept only as clearly-labeled reference material. See §2c.

## 2c. ADR-0006 — Clean Room Learning Directive v2.0, Policy A Adopted (2026-07-06)

Boss issued a v2.0 Clean Room directive resolving the open question ADR-0005 had raised (does
Clean Room prohibit only Odoo-core reproduction, or also OCA-module reuse?). **Policy A adopted:**
Odoo Core and OCA may be studied for concepts only; "REUSE" is retired as a phase-ending
classification and replaced with **Concept Match** (informs independent design, no code adopted);
whether any reference-system package is ever installed as a real dependency is a separate,
later, explicitly-labeled Architecture + Licensing decision. Boss also provided
`00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` the same day, confirming SMEsPlus's real stack
is Next.js/FastAPI/PostgreSQL+SQLAlchemy — not the Odoo runtime — which makes independent
re-implementation the only technically viable path for anything below the API layer, reinforcing
Policy A as fact as well as policy.

**Documents reworded accordingly:** `ADR-0004` (Addendum 3), `OPEN_SOURCE_TO_SMESPLUS_GAP.md`
(reclassification notice + §8), `BUSINESS_RULE_CATALOG.md` (§H reworded to concept-first language
+ top-level notice), `CANONICAL_DATA_MODEL.md` (top-level notice). Full record:
`00_Architecture_Office/ADR/ADR-0006-CLEAN-ROOM-LEARNING-DIRECTIVE-V2-POLICY-A.md`. ADR-0005 (v1.0
of the directive) is marked Superseded, not deleted — its conflict-disclosure table remains the
evidence trail for why this reclassification was needed.

**Phase 2.5→4 Thai Accounting Domain FDS task status:** may now resume, under Concept Match framing
throughout — no longer held.

## 2a. Decision Recorded Since Initial Package (2026-07-05)

**ADR-0004 — Accounting Module Scope: Thailand Localization Only.** Boss approved, directly in session: standard Odoo accounting functionality (Chart of Accounts, GL, AR/AP, Journal, Vendor Bill matching) stays fully in scope; localization is restricted exclusively to Thailand (`l10n_th`, `l10n_th_reports` — confirmed present in the evidenced source). The other 521 of 523 total `l10n_*` country-localization modules are OUT OF SCOPE. Full record: `00_Architecture_Office/ADR/ADR-0004-ACCOUNTING-THAILAND-LOCALIZATION-SCOPE.md`. Reflected in `BUSINESS_CAPABILITY_MAP.md`, `SOURCE_TO_BUSINESS_MAPPING.md`, `MODULE_DEPENDENCY_MATRIX.md`, and `OPEN_SOURCE_TO_SMESPLUS_GAP.md`.

These three items do not block starting Phase 3 Functional Design on Purchase or SaaS Foundation (both already have a clean, evidence-matched or evidence-drafted baseline independent of the three gaps above), but they should be resolved before the Architecture Team relies on `16_Learning_Analysis/`, cross-references requirement IDs across documents, or scopes any module that might overlap with `Other_Unclassified`.

## 3. Underlying Repository Evidence Index (What Each Deliverable Was Built From)

### Source Code / Database Evidence (Real, Schema-Level — High Confidence)
- `V2.0/THAI/SMEPLUS-26-06-29-001_Final_AI_Handoff_Documentation_v2.0/Evidence_CSV/` — Phase B Closure Pack v1.5: `Module_Inventory.csv` (1,436 modules), `Dump_Table_Inventory.csv` (1,395 tables), `Dump_Column_Inventory.csv` (13,940 columns), `Dump_Constraint_Inventory.csv` (6,682 constraints), `Foreign_Key_Relationship_Edges.csv` (5,141 FKs), `Dump_Index_Inventory.csv` (1,714 indexes), `ORM_Field_Inventory_and_DB_Mapping.csv` (27,682 field mappings), `XML_View_Action_Menu_Inventory.csv` (6,260 UI records), `Security_Access_Inventory.csv` (473 access records), `Business_Rule_Method_Inventory.csv` (4,377 business methods), `Evidence_Gate_Register_v1.5_CLOSED.csv` (14/14 gates PASS), `Closure_Checklist_v1.5.csv`, `Closure_Evidence_Summary_v1.5.csv`.
- `02_Functional_Design/02_Functional_Design/` — iTEST02 dump-level functional analysis: module inventory, 4 module ERDs (Accounting_Finance, Sales_CRM, HR_Payroll, Inventory_Purchase), data governance controls, evidence gate report, functional design assumptions, migration readiness checklist, sensitive data risk report.

### Business / Functional Evidence (Medium-to-High Confidence)
- `01_SaaS_Foundation/FDS/Domains/` — 17 domain FDS files (Tenant, Company, Branch, Division, IAM, Role, Role/Permission, Subscription, Subscription/Module, Module, Approval, Notification, Audit, Reporting, Configuration, Integration).
- `01_SaaS_Foundation/FDS/FDS_REQUIREMENT_CATALOG.md` — 70-item FR-prefixed requirement catalog (Foundation scope).
- `17_Functional_Specification_Factory/02_Purchase/` — Purchase Module Functional Requirement Catalog v0.1, Purchase Module Business Rules v0.1 (full RFQ-centric Procure-to-Pay process, 20+ business rules).
- `12_Traceability/Requirement_Matrix/FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` — Evidence-matched verdicts for 12 Foundation/Purchase requirements.

### Architecture / Governance Evidence (High Confidence)
- `00_Architecture_Office/ADR/ADR-0002-EVIDENCE-DRIVEN-FUNCTIONAL-SPECIFICATION.md`, `ADR-0003-AS-IS-BEFORE-TO-BE-FUNCTIONAL-DESIGN.md`.
- `MODULE_EXPANSION_PLAN.md` — Foundation Reuse Rule (confirms Shared/Platform capabilities every business module must reuse).

### Flagged Low-Confidence Evidence (Do Not Build On Without Verification)
- `16_Learning_Analysis/` — generic/templated content, conflicts with the schema-level evidence above. See GAP-KC-01.

## 4. Reading Order for a New Architecture Team Member

1. `KNOWLEDGE_BASE_INDEX.md` (this document) — orientation.
2. `KNOWLEDGE_CONSOLIDATION_REPORT.md` — the full narrative, including the confidence flag on `16_Learning_Analysis/`.
3. `BUSINESS_CAPABILITY_MAP.md` — see the whole system at capability-tier altitude.
4. `SOURCE_TO_BUSINESS_MAPPING.md` — see how real Odoo modules map onto SMEsPlus target modules.
5. `MODULE_DEPENDENCY_MATRIX.md` — see who depends on whom and what's still PLACEHOLDER.
6. `CANONICAL_DATA_MODEL.md` — see the entity relationships without implementation noise.
7. `BUSINESS_RULE_CATALOG.md` — see the actual rules, traced to FRs.
8. `OPEN_SOURCE_TO_SMESPLUS_GAP.md` — see exactly what to Reuse, Adapt, or build New, and what's explicitly Retired.

## 5. Success Criteria Check (Per Phase 2.5 Instructions)

| Criterion | Met? | Evidence |
|---|---|---|
| Knowledge has been consolidated | ✅ | `KNOWLEDGE_CONSOLIDATION_REPORT.md` |
| Business Rules have been extracted | ✅ (78 rules catalogued; full universe is 4,377 method-level rules, most not yet distilled — flagged as expected/ongoing, not a Phase 2.5 failure) | `BUSINESS_RULE_CATALOG.md` |
| Canonical Data Model exists | ✅ | `CANONICAL_DATA_MODEL.md` |
| Business Capability Map exists | ✅ | `BUSINESS_CAPABILITY_MAP.md` |
| Module Dependency Matrix exists | ✅ | `MODULE_DEPENDENCY_MATRIX.md` |
| Gap Analysis is complete | ✅ (complete for Foundation + Purchase scope; three process-level gaps flagged for Boss/PMO, not left silently unresolved) | `OPEN_SOURCE_TO_SMESPLUS_GAP.md` |
| Knowledge Base Index exists | ✅ | This document |
| Architecture Team can immediately continue with Functional Design without repeating any learning activity | ✅ with 3 flagged exceptions | See §2 above |
