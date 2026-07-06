# OPEN_SOURCE_TO_SMESPLUS_GAP.md

**Document ID:** SMEPLUS-26-07-05-001-GAP
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as Repository Auditor / Enterprise Architect
**Date:** 2026-07-05

## Purpose
Classify every capability/entity identified in this consolidation pass as **Reuse**, **Adapt**, **Replace**, **New**, or **Retire**, with reasons, so Phase 3 does not re-derive decisions already made during Evidence Matching.

## Dependencies
`FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md`, `CANONICAL_DATA_MODEL.md`, `MODULE_DEPENDENCY_MATRIX.md`, `BUSINESS_CAPABILITY_MAP.md`, `01_SaaS_Foundation/FDS/Domains/*.md`.

## Source Evidence
Evidence Matching Rounds 1–3 (Purchase module) plus the SaaS Foundation FDS "Data Entities (Conceptual)" GAP markers, cross-checked in this pass.

## Confidence Level
High for the Purchase-module classifications (independently reconciled against real source code and the DB dump on 2026-07-02). Medium for SaaS Foundation platform-layer classifications (FDS Draft, not yet Boss-approved). Note the classification taxonomy used here (Reuse/Adapt/Replace/New/Retire, as specified by the Phase 2.5 instruction) maps approximately but not identically onto ADR-0003's own taxonomy (KEEP/IMPROVE/CREATE/MERGE/RETIRE) — a crosswalk is given in §5.

## Known Gaps
See §4 for gaps in the gap-analysis process itself (taxonomy conflicts, unclassified module groups).

## Recommended Next Step
Boss/PMO ruling on the three items flagged 🔴 below before Phase 3 sprint planning.

---

## ⚠️ RECLASSIFICATION NOTICE (2026-07-06, per ADR-0006 — Clean Room Policy A)

**Every "REUSE" verdict in §1 below is reclassified as "Concept Match."** Under Boss's Clean Room
Learning Directive v2.0 (Policy A) and the confirmed FastAPI/Next.js/SQLAlchemy target stack
(`00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md`), no Odoo or OCA code is installed into
SMEsPlus. "REUSE" in §1 means: *this business capability is already solved conceptually in
reference material, which informs SMEsPlus's own independent implementation in its own stack — not
that any reference-system code, schema, or module is adopted.* Full detail: `ADR-0006-CLEAN-ROOM-
LEARNING-DIRECTIVE-V2-POLICY-A.md`. §2 (Adapt) and §3 (New) already implied independent build and
are unaffected in substance, though "Adapt" now also means "adapt the *concept*," never "adapt the
*code*."

---

## 1. REUSE — Native Odoo capability, no build needed (READ AS: "Concept Match" — see notice above; no Odoo/OCA code is installed)

| Item | Reason | Evidence |
|---|---|---|
| Base RBAC (Role-Based Access Control) | `res_groups` / `ir_model_access` / `ir_rule` fully covers base RBAC (FR-FD-002 = MATCHED) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Purchase Request | Real OCA `purchase_request` module confirmed present in the DB (FR-PUR-001 = MATCHED) — needs sourcing/verification/gating, not building | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| PO Generation (base RFQ→PO confirm flow) | Native Odoo receiving/confirm flow works (FR-PUR-006 = MATCHED, base) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Goods Receipt (base flow) | Native Odoo receiving works (FR-INV-001 = MATCHED, base) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Vendor Bill / 3-way match | Explicitly confirmed via Evidence Matching against source code and DB dump (FR-ACC-001 = MATCHED) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Company entity | `res_company` exists natively; maps directly to the SMEsPlus Company concept | `CANONICAL_DATA_MODEL.md` §1 |
| Customer/Supplier (partner) | `res_partner` natively unifies both roles | `CANONICAL_DATA_MODEL.md` §2 |
| Product, Warehouse, Stock Move | `product_template`/`product_product`, `stock_warehouse`, `stock_move` all confirmed in schema | `iTEST02_ERD_Inventory_Purchase.md` |
| Journal / Move / Payment (double-entry accounting) | `account_journal`, `account_move`, `account_move_line`, `account_payment` all confirmed in schema | `iTEST02_ERD_Accounting_Finance.md` |
| Attachment mechanism | `ir_attachment` generic model already referenced across many modules | `iTEST02_module_inventory.csv` (Manufacturing_Maintenance sample tables) |
| `l10n_th` (Thailand - Accounting), `l10n_th_reports` (Thailand - Accounting Reports) | Confirmed present in evidenced source (`02 OTHER.zip`); the correct, in-scope localization for a Thailand-only product — reuse rather than build custom | `Module_Inventory.csv`; formalized in ADR-0004, 2026-07-05 |
| VAT (7%) | Confirmed handled via Odoo's standard `account.tax` engine; `l10n_th` supplies Thai rate/configuration data only — no separate VAT module needed | Re-verified 2026-07-05, `Module_Inventory.csv`; ADR-0004 Addendum |
| PromptPay / EMV QR code on invoices | `account_qr_code_emv` confirmed present with real business methods, is a direct dependency of `l10n_th` | Re-verified 2026-07-05, `Business_Rule_Method_Inventory.csv`; ADR-0004 Addendum |
| 🆕 **Thai Withholding Tax Certificate suite** (`l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_cert_form`, `l10n_th_withholding_tax_multi`, `l10n_th_withholding_tax_report`, `l10n_th_amount_to_text`, `l10n_th_partner`, `l10n_th_base_location`) | **GAP-TH-01 RESOLVED, 2026-07-05; reclassified to Concept Match, 2026-07-06 per ADR-0006.** Boss provided the source (OCA `l10n-thailand`, by Ecosoft, v19.0.x). Field-level verification confirms 100% match against every previously-unsourced live table/field (`withholding_tax_cert`, `withholding_tax_cert_line`, `create_withholding_tax_cert`, `account_withholding_tax`, `income_tax_form`, `wt_cert_income_type`, `tax_payer`, `amount_pension_fund`, `amount_socialsecurity_fund`, `amount_provident_fund`), confirming the business rules and PND certificate concept are well-understood. Under Policy A and the FastAPI/SQLAlchemy target stack, **this code is not installed into SMEsPlus** — it is retained as labeled reference material only, informing an independent SMEsPlus implementation of the same certificate business rules. | `Archive.zip` (Boss-provided, 2026-07-05); ADR-0004 Addendum 3; ADR-0006 |

## 2. ADAPT — Base capability exists, needs an SMEsPlus-specific layer added

| Item | Reason | Evidence |
|---|---|---|
| Tenant Isolation | Company-level isolation exists; a Tenant-grouping layer above Company must be added (FR-FD-001 = PARTIAL) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Module Activation | Base module enable/disable toggle exists in Odoo; the subscription-gating layer on top of it does not (FR-FD-004 = PARTIAL) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| PO Generation — approval gate | Native flow works, but the gate requiring an Approved Vendor Selection before PO creation must be added | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Goods Receipt — over-receipt tolerance rule | Native receiving works; the business rule capping/approving over-receipt quantity is unconfirmed and likely needs adding | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Audit Trail | Odoo's native `mail.message`/tracking gives partial coverage; a dedicated cross-module Audit Service (per `FDS_AUDIT.md`) still needs to be layered on top | `FDS_AUDIT.md`, `CANONICAL_DATA_MODEL.md` §8 |
| Notification | Odoo has base notification/mail infrastructure; Tenant-scoping and archive-retention rules (BR-NTF-002/003) need to be added | `FDS_NOTIFICATION.md` |
| Generic Withholding-Tax-on-Payment engine (`l10n_account_withholding_tax`) | Present in source with real business methods, used as the base for Argentina/Cambodia/Sri Lanka/Philippines/Saudi Arabia localizations — but `l10n_th` does not depend on or extend it. The Boss-provided Thai WHT suite (see §1) already supersedes the need to wire this generic engine to Thailand — noted here only for completeness in case the Boss-provided suite is later retired. | Re-verified 2026-07-05, `Business_Rule_Method_Inventory.csv`; ADR-0004 Addendum |

## 3. NEW — Confirmed gap, no existing implementation anywhere in the 1,395-table schema

| Item | Reason | Evidence |
|---|---|---|
| RFQ Management (multi-vendor tendering) | Confirmed real gap — biggest remaining build item (55 story points, ERPPLUS-96, top priority) | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Quote Tracking | Confirmed real gap, depends on RFQ Management | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Vendor Comparison | Confirmed real gap | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Vendor Selection (buyer decision + justification object) | Confirmed real gap — the in-scope part of FR-PUR-005 | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Tenant entity/table | No table exists above Company; purely conceptual today | `FDS_TENANT.md`, `CANONICAL_DATA_MODEL.md` |
| Branch, Division entities | Explicitly "not a stock Odoo concept" / custom table, no existing evidence | `FDS_BRANCH.md`, `FDS_DIVISION.md` |
| Subscription Plan / TenantSubscription | Zero subscription/entitlement tables exist anywhere in the schema (FR-FD-003 = GAP) | `FDS_SUBSCRIPTION.md`, `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` |
| Module Registry (Module, TenantModule) | Registry entity, no existing evidence | `FDS_MODULE.md` |
| Approval Workflow Engine (reusable, cross-module) | Explicitly designed to be new and reusable — Odoo has approval fragments but not a unified reusable engine | `FDS_APPROVAL.md` |
| Configuration key-value store | Custom key-value store, no existing evidence | `FDS_CONFIGURATION.md` |
| Integration/Webhook/API-secret layer | No dedicated integration/webhook table found anywhere in the schema | `FDS_INTEGRATION.md` |
| ReportDefinition (platform reporting object) | No existing evidence | `FDS_REPORTING.md` |
| "Close" state for the Purchase Order lifecycle | Not yet evidence-matched as an explicit terminal state | `MODULE_DEPENDENCY_MATRIX.md` §C |
| Thai e-Tax Invoice / e-Receipt (Revenue Department compliance) | Re-verified 2026-07-05 with a broader search across module names, categories, XML views, and business methods — Indonesia, India, Turkey, and Colombia all have e-invoicing modules in this source; Thailand does not. Firm GAP. | ADR-0004 Addendum, 2026-07-05 |

## 3a. GAP-TH-01 — RESOLVED (was: Found Live, Source Not Provided)

**Status: CLOSED, 2026-07-05.** Originally recorded here as the same "found live, no source" pattern
as the `efaplus` PO-approval extension. Boss provided the missing source (`Archive.zip`, OCA
`l10n-thailand` modules) the same day. Field-level verification confirmed a 100% match. See §1 (REUSE)
above and `ADR-0004-ACCOUNTING-THAILAND-LOCALIZATION-SCOPE.md` Addendum 2 for full detail. Retained here,
struck through in spirit, so the audit trail shows the gap was found, investigated, and closed rather
than silently disappearing from the register.

## 4. RETIRE (or OUT OF SCOPE) — Confirmed to be excluded from SMEsPlus scope

| Item | Reason | Evidence |
|---|---|---|
| 🔴 `level1`/`level2` two-level PO approval extension (owner role `efaplus`) | Custom add-on found live in the database but with **no source module in either uploaded zip** — outside SMEsPlus scope per explicit Boss decision, 2026-07-02 | `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` ("Boss's 2026-07-02 decision," "should be removed from ERPPLUS-99's scope entirely") |
| Non-Thailand country localizations (521 of 523 `l10n_*` modules — every country except `l10n_th`/`l10n_th_reports`) | SMEsPlus is a Thailand-only product; carrying other-country localizations (e.g. `Accounting/Localizations/Account Charts` 120 modules, `Reporting` 112 modules, `EDI` 72 modules — 304 total under Localizations) adds unused scope and maintenance surface with no evidenced business need | `Module_Inventory.csv`; Boss decision recorded in ADR-0004, 2026-07-05 |

## 5. Taxonomy Crosswalk (Phase 2.5 vs. ADR-0003)

| Phase 2.5 taxonomy (this document) | ADR-0003 taxonomy | Notes |
|---|---|---|
| Reuse | KEEP | Direct equivalent |
| Adapt | IMPROVE | Direct equivalent |
| New | CREATE | Direct equivalent |
| Retire | RETIRE | Direct equivalent |
| Replace | MERGE (closest) | ADR-0003 has no exact "Replace" category; no item in this pass required a pure Replace classification — everything found is either Reuse-as-is, Adapt, New-build, or Retire. Flagging this as a minor taxonomy gap rather than forcing a false "Replace" classification onto any item. |

## 6. Gaps in the Gap-Analysis Process Itself

| ID | Gap | Impact | Recommended Owner |
|---|---|---|---|
| 🔴 GAP-KC-01 | `16_Learning_Analysis/` conflicts with the grounded evidence base (see `KNOWLEDGE_CONSOLIDATION_REPORT.md` §4) | Cannot be used to classify any item above; risk that a future AI role cites it by mistake | Boss / PMO AI |
| 🔴 GAP-KC-02 | Two parallel requirement-ID taxonomies exist (FD-001–030 vs. FR-TEN/FR-CMP/... 70 total) without a published crosswalk | Risk of double-counting or mis-tracing requirements in Phase 3 traceability work | PMO AI / Enterprise Architect AI |
| GAP-KC-03 | `Other_Unclassified` module group (293 tables — the single largest group in the entire schema) has not been classified into any capability tier | Unknown functional scope; could contain hidden Reuse or New items | Enterprise Architect AI (follow-up classification pass) |
| GAP-KC-04 | `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md` lists ADR-0001–0010 (generic cloud/microservices titles) with no underlying ADR file evidence anywhere in the repository — same unevidenced-content pattern as GAP-KC-01 | Risk of false confidence in architecture decisions that were never actually made/approved as described | **RESOLVED (status): Acknowledged by Boss, 2026-07-05 — recorded as-is, original file NOT to be modified, will be corrected gradually. No further AI action pending Boss.** |

---

## Summary Counts

| Classification | Count (this pass) |
|---|---:|
| Reuse | 14 |
| Adapt | 7 |
| New | 14 |
| Retire / Out of Scope | 2 |
| Found live, source not provided — now RESOLVED | 0 (was 1, closed 2026-07-05) |
| Replace | 0 (no forced classification — see §5) |
| **Process-level gaps requiring Boss/PMO decision** | **3** (GAP-KC-01, 02, 03; GAP-KC-04 and GAP-TH-01 both closed) |

## 7a. GAP-TH-01 Closure Note (2026-07-05)

Boss uploaded `Archive.zip` the same day this gap was raised, containing the OCA `l10n-thailand` Thai
Withholding Tax suite (7 modules, listed in §1 above). Field-level verification (module manifests,
model `_name` declarations, and field definitions) traced every previously-unsourced live table and
column to exact source. GAP-TH-01 is closed. One open registry question remains (not a gap in the
knowledge base, but a housekeeping item): where the actual Python module source should physically live
in version control, since `AI-Collaboration-Hub` is a governance/evidence repository, not (so far) a
code repository. See ADR-0004 Addendum 2 for the specific question raised to Boss.

## 7. Decision Log Addendum (2026-07-05)

Boss approved, directly in the AIOS session, the Accounting-module Thailand-only localization scope described above. This has been formally recorded as **ADR-0004** (`00_Architecture_Office/ADR/ADR-0004-ACCOUNTING-THAILAND-LOCALIZATION-SCOPE.md`) rather than only noted in this Gap Analysis, per ADR-0002's Evidence-Driven requirement that decisions be traceable to a real ADR file, not just a narrative mention.

**Separately flagged (not fixed in this pass):** while sourcing the next available real ADR number for ADR-0004, it was discovered that `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md` lists a decision register (ADR-0001 through ADR-0010, titles like "Kubernetes Deployment," "Redis Cache Layer," "Event Driven Integration") for which **no underlying `ADR-XXXX-*.md` file exists anywhere in the repository** — the only real ADR files on disk are `ADR-0002-EVIDENCE-DRIVEN-FUNCTIONAL-SPECIFICATION.md` and `ADR-0003-AS-IS-BEFORE-TO-BE-FUNCTIONAL-DESIGN.md` in `00_Architecture_Office/ADR/`, and even these don't match the titles the log table gives for ADR-0002/0003. This is the same pattern of unevidenced, generic-sounding content already flagged for `16_Learning_Analysis/` (GAP-KC-01) — recorded here as **GAP-KC-04**. ADR-0004 in this pass was deliberately created in the real, evidenced `00_Architecture_Office/ADR/` folder to avoid colliding with or lending false credibility to the unevidenced table.

**Boss decision on GAP-KC-04 (2026-07-05):** Acknowledged. `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md` is to remain untouched — no AI edits, corrections, or deletions to that file. Boss will address it gradually in a separate, deliberate pass. This gap analysis entry stands as the durable record of the finding; no further escalation action is needed until Boss initiates the cleanup.

## 8. ADR-0006 Reclassification Summary (2026-07-06)

Per Boss's Clean Room Learning Directive v2.0 (Policy A), every REUSE verdict in this document is
Concept Match, not code adoption. No Odoo or OCA code is installed into SMEsPlus; the confirmed
FastAPI/Next.js/SQLAlchemy technology stack (`TECHNOLOGY_STACK_STANDARD.md`) makes this a technical
fact as well as a policy choice. This closes the "physical storage" open question from ADR-0004
Addendum 2 (moot — the code isn't going into the SMEsPlus codebase) and confirms the Phase 2.5→4
Thai Accounting Domain FDS task may resume under Concept Match framing throughout.
