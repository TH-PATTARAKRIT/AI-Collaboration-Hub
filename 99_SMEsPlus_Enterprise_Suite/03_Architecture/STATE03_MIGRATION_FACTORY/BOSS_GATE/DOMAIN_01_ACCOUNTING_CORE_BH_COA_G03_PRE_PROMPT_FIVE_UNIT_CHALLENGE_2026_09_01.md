# [SMEPLUS-26-09-01-COA-G03-PRE-001]
# COA-G03 — Five-Unit Pre-Prompt Challenge for AI Semantic Consolidation / L999.999

Date: 2026-09-01
Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `SMEsPlus`
STATE: STATE03 — Architecture
Domain: DOMAIN_01 Accounting Core / COA
Target Gate: `COA-G03 — AI Semantic Consolidation`
Boss: Sole Final Approver
Risk Class: HIGH — Accounting Backbone / Canonical COA Gate

## 1. Controlled Prerequisite State

COA-G02 Boss closure:

`497c80887f82dfca4967ca43f83b4ecc3c01d8d8`

Accepted G02 baseline:

`36-CONCEPT BASE COA KERNEL = BOSS ACCEPTED AS COA-G02 BASELINE`

G02 status:

`COA-G02 = APPROVED / PASS / CLOSED`

The 36-concept result is a G02 Base Kernel baseline only. It is not the final Standard Thai COA.

Controlling G03 direction:

- Boss Thailand COA Closure Authorization: `DOMAIN_01_ACCOUNTING_CORE_AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`
- COA Base Kernel + AI Consolidation Standard: `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`
- Cross-Gate SaaS Invariants: `DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`

Mandatory semantic transformation:

`Source Account -> Business Meaning -> Accounting Treatment -> Canonical Group -> SMEsPlus Target Account Candidate`

Primary row-level reconciliation population for the next prompt shall be the Boss-approved `ODOO18` workbook population already verified by G01/G02:

`389 source rows`

This is a source population, not a target-count mandate.

## 2. Five-Unit Challenge

### 2.1 Audit VETO — Evidence / Governance

Status: **NO VETO — NEXT PROMPT MAY BE ISSUED; EXECUTION REQUIRES BOSS AUTHORIZATION**

Challenge requirements:

- All 389 ODOO18 source rows must receive exactly one controlled G03 disposition.
- Do not infer that `389` source rows imply 389 target accounts.
- Do not infer that the G02 36 Base Kernel is the complete final COA.
- Preserve G02 evidence and 36 concepts; do not reopen G02 unless a genuine contradictory primary fact is found.
- Every N-to-1 merge must have accounting-treatment equivalence evidence.
- Any unresolved material ambiguity must be `HOLD / EVIDENCE_REQUIRED`, not guessed.
- Do not self-declare G03 PASS; Team B evidence must route to fresh Independent Audit.

Main risk: mass consolidation by name similarity or schedule pressure rather than evidenced accounting equivalence.

### 2.2 TBRAC — Thailand Business Reality

Status: **PROCEED WITH CONTROL — THAILAND TAX / ACCOUNTING DISTINCTNESS MUST BE PRESERVED**

Challenge requirements:

- Preserve materially different VAT / Undue VAT timing positions.
- Preserve WHT credit vs WHT payable semantics.
- Do not prematurely decide final PND1/2/3/53/54 GL granularity; G06 owns statutory tax-control closure unless primary evidence forces a G03 separation.
- Preserve Prepaid CIT / CIT Payable / CIT Expense as materially different positions.
- Do not merge salary, rent, director-loan, channel, branch, customer or product distinctions merely because they appear as separate source accounts; determine whether each distinction is accounting-recognition driven or operational/analytical.
- Statutory claims require authoritative evidence; otherwise record controlled downstream dependency or HOLD.

Main risk: converting one source/company chart convention into a universal Thailand accounting rule.

### 2.3 EXPERT IBPV — Business Process / Cross-Module Semantics

Status: **PROCEED — REQUIRE DURABLE BUSINESS PURPOSE AND DO-NOT-MERGE BOUNDARIES**

Challenge requirements:

- Every canonical candidate must explain the durable business/control purpose it serves.
- Preserve AR/AP control semantics and reconciliation boundaries.
- Preserve Cash / Bank / Transfer / Suspense / Outstanding Receipt / Outstanding Payment distinctions where control behaviour differs.
- Preserve Inventory / GRNI / COGS distinctions required by Inventory and Purchase flows.
- Preserve Gross Fixed Asset / Accumulated Depreciation / Depreciation Expense separation.
- Prefer dimensions or source attributes over GL-account proliferation when accounting treatment is materially equivalent.
- Channel/Marketplace/Customer/Product/Branch/Location/Salesperson/Campaign/Source System identity shall not automatically become GL identity.

Main risk: over-consolidation that makes Sales, Purchase, Inventory, Expense, Asset or reporting processes semantically ambiguous.

### 2.4 EXPERT IDTM — Deterministic Testability / Integrity

Status: **PROCEED — REQUIRE MECHANICAL RECONCILIATION AND REPRODUCIBILITY**

Minimum deterministic controls for the next prompt:

- authoritative ODOO18 population = 389 rows;
- exactly one G03 disposition per source row;
- disposition count sum = exactly 389;
- zero orphan source rows;
- zero duplicate row dispositions unless explicitly represented as a provenance-only alias and not double-counted;
- every `MERGE_TO_CANONICAL` row has a target candidate and equivalence rationale;
- every `KEEP_SEPARATE` row has a material do-not-merge reason;
- every `HOLD / EVIDENCE_REQUIRED` row states missing evidence and Gate impact;
- all 36 G02 Kernel concepts remain traceable to G03 mapping where applicable;
- candidate-count arithmetic must be reproducible and must not be target-fitted.

Main risk: an apparently complete mapping that cannot be reconciled mechanically back to the 389-row source population.

### 2.5 EXPERT IESA — ERP / SaaS System Integrity

Status: **PROCEED — PRESERVE CANONICAL IDENTITY AND SAAS BOUNDARIES**

Challenge requirements:

- Account Code / Name / source technical ID remain provenance attributes, not canonical identity.
- Similar source names/codes across tenants or companies must not be treated as shared identity by default.
- G03 must preserve tenant/company boundaries and canonical reporting meaning.
- Evidence IDs such as `G03-CAND-###` may be used for audit traceability only and must not be presented as production database IDs.
- Do not design schema/API/ORM/tables in G03.
- Do not claim runtime template/instance/version/upgrade/isolation proof; those remain later G04S/G07 obligations.
- SI-01..SI-10 must be explicitly recorded in the G03 Gate package with the Boss-mandated evidence fields and allowed status vocabulary.

Main risk: converting source architecture or mutable company configuration into SMEsPlus SaaS Core identity.

## 3. Consolidated Do-NOT-Merge Challenge

The next prompt must challenge every proposed merge against all 13 Boss-approved material-difference rules:

1. Account Type / canonical accounting class
2. Balance Sheet vs Profit & Loss presentation
3. Thai tax/VAT/WHT/CIT treatment
4. Reconciliation requirement
5. AR/AP control-account role
6. Cash/bank/clearing/suspense behaviour
7. Inventory/valuation/cost-flow role
8. Currency restriction or monetary-item treatment
9. Statutory/regulatory reporting requirement
10. Retained earnings/current-year earnings semantics
11. Contra-account / allowance / accumulated-depreciation role
12. Multi-company consolidation meaning
13. Evidenced system-generated control dependency

If any differs materially, default outcome is `KEEP_SEPARATE` or `HOLD / EVIDENCE_REQUIRED`.

## 4. Required Row-Level Outcomes

Every source row must receive exactly one of the Boss-approved outcomes:

- `BASE_KERNEL`
- `MERGE_TO_CANONICAL`
- `KEEP_SEPARATE`
- `RESERVED / NOT DEFAULT-TH`
- `HOLD / EVIDENCE_REQUIRED`

For `MERGE_TO_CANONICAL`, evidence must include at minimum:

- source account code/name;
- source Account Type;
- source business meaning;
- target canonical account candidate;
- reason for merge;
- accounting-treatment equivalence evidence;
- retained source provenance.

## 5. Scope Boundary

The next prompt may prepare G03 Team B evidence only after Boss execution authorization.

G03 shall not:

- reopen/resize the G02 Kernel merely to optimize account count;
- freeze final Standard Thai COA;
- execute G04 Account Type & Account Group architecture;
- execute G04S SaaS provisioning/versioning architecture;
- execute G05 financial-statement taxonomy;
- execute G06 final Thailand tax-control design;
- execute G07 multi-company/runtime proof;
- execute G08 final audit/freeze;
- design database/API/ORM/schema;
- start Development, Release, Deployment or Production.

## 6. Five-Unit Consolidated Opinion

`AUDIT VETO = NO VETO`

`TBRAC = PROCEED WITH THAILAND-REALITY CONTROL`

`IBPV = PROCEED WITH CROSS-MODULE / DO-NOT-MERGE CONTROL`

`IDTM = PROCEED WITH 389/389 DETERMINISTIC RECONCILIATION`

`IESA = PROCEED WITH SAAS / CANONICAL-ID CONTROL`

`NEXT PROMPT READINESS = READY`

`COA-G03 EXECUTION = NOT STARTED / NOT AUTHORIZED BY THIS READINESS RECORD`

The fastest controlled path is:

`Boss G03 execution authorization -> Team B G03 semantic consolidation -> Fresh Independent Audit -> PMO Verification -> Boss G03 Decision -> next authorized Gate`

## 7. Progress Governance

`% Board = TBD / NO APPROVED BASELINE`

`% STATE = TBD / NO APPROVED BASELINE`

`% STEP = TBD / NO APPROVED BASELINE`

No guessed percentages.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
