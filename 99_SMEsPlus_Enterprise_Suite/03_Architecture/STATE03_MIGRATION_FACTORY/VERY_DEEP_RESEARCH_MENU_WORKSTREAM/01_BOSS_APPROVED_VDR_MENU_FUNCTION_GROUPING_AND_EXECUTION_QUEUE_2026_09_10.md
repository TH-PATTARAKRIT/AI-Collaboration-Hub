# [SMEPLUS-26-09-10-VDR-MENU-WORKSTREAM-001]
# BOSS APPROVED — Very Deep Research Menu/Function Grouping & Execution Queue

## Decision Status
BOSS APPROVED — EFFECTIVE IMMEDIATELY

Jira: `ERPPLUS-153`

## Purpose
Prepare a controlled, dependency-aware queue of bounded menu / master-data / function subjects for SMEsPlus Very Deep Research, so each subject can progress independently through the approved research-to-Figma pipeline without waiting for the whole ERP to complete.

This workstream applies the approved strategy:

`ONE PRIMARY DEEP BASELINE — MANY TARGETED DELTAS, NOT MANY FULL RESTARTS.`

and the approved per-subject pipeline:

`RESEARCH CONTRACT`
`-> PRIMARY VERY DEEP RESEARCH`
`-> INTERNAL MULTI-PASS RESEARCH`
`-> COMPLETENESS MATRIX`
`-> SPECIALIST REVIEW`
`-> INDEPENDENT ADVERSARIAL CHALLENGE`
`-> CORRECTION / TARGETED RESEARCH IF REQUIRED`
`-> RESEARCH SUFFICIENCY / SATURATION GATE`
`-> PHASE S`
`-> PHASE SA`
`-> PHASE PRE-MATRIX TEST`
`-> TARGETED DELTA VDR ONLY WHERE A GAP IS PROVEN`
`-> PHASE HANDOFF GATE`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> FIGMA / UX DESIGN`

## Current Timing Interpretation
The VDR menu/function grouping and Research Contract preparation MAY begin while the active Phase SA work is approaching its late assurance / pre-gate area.

However, planning readiness is not the same as declaring the active Phase SA complete. Current verified evidence shows late Phase SA correction / pre-gate closure activity, including mainline standards-claim correction and remaining controlled lineage. Therefore this workstream shall prepare the next research queue without self-declaring Phase SA PASS or skipping the future Pre-Matrix / Handoff Gates.

## Grouping Principle
Research units are not limited to broad ERP modules. The preferred unit is a `Bounded Functional Subject` that is small enough to research to practical saturation, but large enough to preserve the complete business lifecycle and cross-module handoffs.

Each subject must have:
- Research Subject ID;
- bounded scope;
- business purpose / lifecycle;
- upstream / downstream dependencies;
- menu / function / master-data mapping;
- Research Contract;
- evidence baseline;
- open gaps / unknowns;
- expected Functional Design / Figma target;
- Gate state and owner.

## Initial Execution Waves

### WAVE 0 — Shared Foundation & Master Data
Priority: HIGHEST because downstream Purchase / Inventory / Sales / Accounting depend on these identities and reference masters.

#### VDR-MD-01 — Organization / Company / Branch Context
Scope candidates:
- Tenant / Organization Root / Company / Branch business-context behavior;
- company selection / current company context;
- organization-level vs company-level master ownership;
- access / visibility boundaries;
- cross-company permitted behavior and forbidden leakage;
- Figma context indicators / selectors where required.

#### VDR-MD-02 — Customer & Vendor / Business Partner Master
Scope candidates:
- customer / vendor / both roles;
- person vs organization;
- HQ / branch / address / contact structure;
- tax identity and registration attributes;
- bank / payment information and change controls;
- payment terms / credit / commercial attributes;
- duplicate / merge / inactive / archive / historical reference behavior;
- Sales / Purchase / Accounting / Expense handoffs;
- multi-company visibility and tenant isolation;
- import/export/API/migration/audit;
- Figma menu, list, form, tabs, actions, smart actions and supporting flows.

#### VDR-MD-03 — Product / Service Master
Scope candidates:
- Goods / Service / Consumable semantics as approved by functional evidence;
- product identity / code / barcode / variants;
- category / classification;
- UOM and conversions;
- purchase / sale / inventory / accounting properties;
- routes / replenishment / tracking / lot-serial implications;
- costing / valuation / COGS attributes;
- active / inactive / archive / historical references;
- company / tenant boundaries;
- import/export/API/migration;
- Figma menu / list / form / attributes / actions.

#### VDR-MD-04 — Shared Reference Masters
Candidate subjects to split further when their lifecycle is material:
- UOM;
- Product Category / Classification;
- Currency / exchange-rate source ownership;
- Payment Terms;
- Tax / VAT / WHT reference setup;
- Incoterms / delivery terms where applicable;
- Analytic / cost dimensions where shared;
- other cross-domain reference data required by downstream phases.

### WAVE 1 — Procure-to-Pay

#### VDR-PUR-01 — Purchase Request / Requisition
Where in scope: request creation, lines, source/need, approval, change, partial approval, cancellation, traceability and conversion to sourcing/RFQ.

#### VDR-PUR-02 — RFQ / Vendor Quotation
Vendor selection, quotation lifecycle, compare, terms, price, lead time, validity, multi-vendor behavior, cancellation and audit.

#### VDR-PUR-03 — Purchase Order
Create / confirm / amend / approve / cancel, quantities, UOM, price/tax/terms, expected receipt, partial receipt, backorder, return and source-document lineage.

#### VDR-PUR-04 — Purchase Approval & Change Control
Approval authority, delegation, segregation of duties, changed-line behavior, re-approval triggers, evidence and exception handling.

#### VDR-PUR-05 — Vendor Price / Terms / Procurement Reference
Vendor-product relationship, price history, lead time, MOQ, validity, currency, company scope and effective dating.

#### VDR-PUR-06 — Receipt / Return Handoff
Purchase-to-Inventory boundary, partial receipt, over/under receipt policy, rejected receipt, return, lot/serial and accounting handoff.

#### VDR-PUR-07 — Vendor Bill / AP Handoff
PO/receipt/bill relationship, invoice/bill matching, blocked bill control, variances, tax/WHT, credit/debit adjustments and accounting evidence.

### WAVE 2 — Inventory / Warehouse

#### VDR-INV-01 — Warehouse / Location / Route Master
Warehouse, location hierarchy, route/rules, company scope, staging/transit/scrap/customer/vendor virtual concepts where applicable.

#### VDR-INV-02 — Receipt / Putaway
Inbound states, receipt validation, partial/backorder, putaway, lot/serial, QC handoff, exception and cancellation.

#### VDR-INV-03 — Internal Transfer
Source/destination, reservation, execution, partial, backorder, branch/company boundaries, transit and audit.

#### VDR-INV-04 — Delivery / Fulfillment
Reservation, picking, validation, partial delivery, backorder, customer handoff, return and COGS trigger implications.

#### VDR-INV-05 — Availability / Reservation / Forecast
On-hand vs forecast, reservation priorities, negative-stock policy, availability calculation, promise/ATP implications and exception behavior.

#### VDR-INV-06 — Lot / Serial / Tracking
Traceability, assignment, split/merge where applicable, expiry/quality attributes, historical immutability and downstream reporting.

#### VDR-INV-07 — Replenishment / Min-Max / Procurement Trigger
Reorder policy, route selection, demand/supply interaction, lead times, MTO/buy/manufacture handoff where applicable.

#### VDR-INV-08 — Inventory Count / Adjustment
Count preparation, freeze/snapshot assumptions, variance, approval, posting, audit, recount and multi-location behavior.

#### VDR-INV-09 — Return / Scrap
Return-to-stock, vendor/customer return, scrap, salvage/other-income implications where applicable, reversal and audit.

#### VDR-INV-10 — Valuation / COGS Handoff
Standard/average/FIFO behavior where approved, valuation timing, COGS-at-delivery control, interim-account handoffs, returns/reversals and reconciliation.

### WAVE 3 — Order-to-Cash

#### VDR-SAL-01 — Customer Quotation
Create/version/validity/price/discount/tax/terms/customer acceptance and conversion.

#### VDR-SAL-02 — Sales Order
Confirm/amend/cancel, quantity/UOM, pricing, commitment/delivery, source lineage and cross-module handoffs.

#### VDR-SAL-03 — Pricing / Discount / Promotion / Credit Control
Pricelist, discount authority, promotion logic, customer credit controls, overrides and audit.

#### VDR-SAL-04 — Delivery / Fulfillment Handoff
Sales-to-Inventory boundary, partial delivery, backorder, return and delivery evidence.

#### VDR-SAL-05 — Invoice Policy / AR Handoff
Order-based vs delivery-based invoicing, timing independence from COGS, invoice creation, adjustments and accounting handoff.

#### VDR-SAL-06 — Return / Refund / Cancellation
Commercial return, stock return, credit note/refund, cancellation boundary and reversal lineage.

### WAVE 4 — Expense-to-Pay

#### VDR-EXP-01 — Expense Category / Policy Master
Expense types, allowed accounts/tax, policy limits/rules, company scope and evidence requirements.

#### VDR-EXP-02 — Expense Claim
Create, line evidence, receipt attachment, allocation, analytic/cost attribution, currency and employee context.

#### VDR-EXP-03 — Expense Approval / Control
Approval, SoD, exceptions, rejection/resubmission, policy override and audit.

#### VDR-EXP-04 — Advance / Reimbursement / Payment Handoff
Employee advance and clearing where in scope, reimbursement, payment, accounting reconciliation and residual balance.

### WAVE 5 — Accounting & Finance
Accounting is to be decomposed aggressively because of complexity and control impact.

#### VDR-ACC-01 — Chart of Accounts / Account Groups / Journals
Canonical account identity, groups/control accounts, account types, posting restrictions, company scope, journal ownership and change governance.

#### VDR-ACC-02 — Customer Invoice / Credit Note / AR
Invoice lifecycle, receivable recognition, tax, payment terms, credit note, cancellation/reversal, reconciliation and audit.

#### VDR-ACC-03 — Vendor Bill / Debit-Credit Note / AP
Bill lifecycle, blocks/unblocks, three-way/two-way relationships where applicable, tax/WHT, adjustments, reconciliation and audit.

#### VDR-ACC-04 — Receipts / Payments / Bank / Cash
Payment states, allocation, bank/cash journals, transfers, unapplied amounts, reversals, payment evidence and reconciliation.

#### VDR-ACC-05 — VAT / WHT / Thai Localization Controls
Tax determination, evidence, certificates, reporting, filing-support behavior and statutory traceability without unsupported compliance claims.

#### VDR-ACC-06 — GL / Posting Engine / Journal Entries
Source-module ownership, posting boundary, immutable finalized facts, manual adjustment controls, reversals and audit.

#### VDR-ACC-07 — Reconciliation
AR/AP/bank/GL/inventory/interim-account reconciliation, exception handling, aging differences and proof.

#### VDR-ACC-08 — Inventory Accounting / COGS
COGS at delivery, valuation method impacts, interim accounts, returns, negative-stock prevention implications and period reconciliation.

#### VDR-ACC-09 — Fixed Assets / Depreciation
Asset recognition, models, depreciation, disposal, adjustments, production allocation/off-balance handling where approved and reporting.

#### VDR-ACC-10 — Analytic / Cost Dimensions
Analytic accounts/dimensions, allocation, project/cost center semantics, cross-module assignment and reporting.

#### VDR-ACC-11 — Period Close / Adjustments / Retained Earnings
Monthly close, year-end adjustments, lock/reopen controls, retained earnings and audit evidence.

#### VDR-ACC-12 — Financial / Tax / Audit / Reconciliation Reports
TB, GL, BS, P&L, AR/AP aging, tax reports, supporting schedules, drilldown, period/company context and reconciliation evidence.

### WAVE 6 — Cross-Module Controls & Supporting Subjects
These are horizontal subjects and may be invoked by other waves rather than treated as one late batch.

#### VDR-X-01 — Approval / Delegation / Segregation of Duties
#### VDR-X-02 — Documents / Attachments / Communication Evidence
#### VDR-X-03 — Import / Export / API / Integration
#### VDR-X-04 — Identity / Audit / Immutability / Effective Dating
#### VDR-X-05 — Tenant / Organization / Company / Branch Boundary
#### VDR-X-06 — Configuration / Setup / Feature Availability
#### VDR-X-07 — Exception / Reversal / Failure / Concurrency
#### VDR-X-08 — Migration / Historical Data / Cutover Behavior
#### VDR-X-09 — Search / Filter / Reporting / Traceability UX

## Recommended First Start Order
To avoid downstream redesign and maximize reuse, SMEs Core recommends the first active Research Contracts be prepared in this order:

1. `VDR-MD-02 — Customer & Vendor / Business Partner Master`
2. `VDR-MD-03 — Product / Service Master`
3. `VDR-MD-04A — UOM`
4. `VDR-MD-04B — Product Category / Classification`
5. `VDR-MD-01 — Organization / Company / Branch Context` where remaining design questions directly affect the above masters
6. `VDR-PUR-03 — Purchase Order` plus its mandatory upstream/downstream dependency checks
7. `VDR-INV-02 — Receipt / Putaway`
8. `VDR-INV-04 — Delivery / Fulfillment`
9. `VDR-SAL-01/02 — Quotation / Sales Order`
10. Accounting subjects according to the active Account Phase SA / Pre-Matrix findings, with no broad accounting reset.

This ordering is a starting recommendation, not a final frozen schedule. Dependency evidence may reorder subjects.

## Mandatory Research Contract Additions for Figma Readiness
Every subject must explicitly identify:
- which user-visible menus/screens/actions are expected;
- which behaviors should remain background/system-controlled and NOT become menus;
- list/form/detail/wizard/report/configuration view needs;
- required states and transitions visible to users;
- fields / controls whose visibility or editability changes by state/role/company;
- warning / validation / error / empty states;
- drilldown / traceability links;
- likely Figma frame groups;
- unresolved UI questions that Functional Design must answer.

The objective is not to let research directly design screens. The objective is to ensure Functional Design and Figma receive complete functional evidence and do not have to guess.

## Gate Discipline
Each bounded subject must preserve the seven approved control blocks at applicable handoffs:
1. Entrance Contract
2. Proof Obligations
3. Evidence State
4. Independent Challenge
5. Controlled Re-entry
6. Exit Contract
7. Phase Handoff Gate

`NO MENU TO FIGMA WITHOUT TRACEABLE RESEARCH + PHASE EVIDENCE.`

`CLEAR HANDOFF BEFORE NEXT PHASE.`

`NO DOWNSTREAM GUESSING.`

`NO EVIDENCE = NO PROGRESS.`

`NEVER SKIP GATE.`

`NO REPEATED QUESTION WITHOUT MATERIAL DELTA.`

Boss remains the sole Final Approver.

## Governance Boundary
This workstream authorizes research planning, Research Contract preparation, evidence collection and controlled phase progression only. It does NOT authorize source-code implementation, merge, deployment, production changes or bypass of the active Phase SA / Pre-Matrix / Handoff controls.
