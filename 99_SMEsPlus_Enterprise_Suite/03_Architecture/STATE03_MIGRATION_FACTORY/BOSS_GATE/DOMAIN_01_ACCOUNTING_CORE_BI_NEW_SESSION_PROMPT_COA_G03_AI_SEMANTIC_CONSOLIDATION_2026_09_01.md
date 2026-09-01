# [SMEPLUS-26-09-01-COA-G03-001]
# COA-G03 — AI Semantic Consolidation, Source-to-Canonical Meaning Reconciliation / L999.999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
STATE: STATE03 — Architecture
Domain: DOMAIN_01 Accounting Core / COA
Gate: `COA-G03 — AI Semantic Consolidation`
Execution Role: Team B independent clean-room semantic design
Boss: Sole Final Approver
Jira: `ERPPLUS-132`

Absolute rules:

- No Evidence = No Progress.
- Never Skip Gate.
- Do not convert UNKNOWN into FACT.
- Do not merge by name similarity alone.
- Preserve source provenance.
- Account Code / Name / source technical ID are not canonical identity.
- Do not self-declare G03 PASS.
- Do not start G04 or any later Gate.
- Development / Release / Deployment / Production are NOT AUTHORIZED.

## 2. EXECUTION AUTHORIZATION STATUS

This prompt is **READY / STAGED** after Five-Unit Challenge commit:

`ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`

COA-G02 is closed by Boss ruling:

`497c80887f82dfca4967ca43f83b4ecc3c01d8d8`

This prompt shall execute only when Boss explicitly authorizes COA-G03 execution in the active control session.

Until then:

`COA-G03 = NOT STARTED / PROMPT READY`

## 3. CONTROLLING AUTHORITIES / INPUTS

Read and verify before producing G03 evidence:

1. Boss COA closure authorization:
   `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`
2. Boss G02 final closure ruling:
   `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_BG_BOSS_COA_G02_FINAL_CLOSURE_RULING_2026_09_01.md`
   Commit: `497c80887f82dfca4967ca43f83b4ecc3c01d8d8`
3. G02 Base Kernel discovery register:
   `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G02_EVIDENCE/COA_G02_BASE_KERNEL_DISCOVERY_REGISTER.md`
4. G02 source-anchor disposition register:
   `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G02_EVIDENCE/COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md`
5. G02 final PMO Verification:
   `PMO_VERIFICATION/DOMAIN_01_ACCOUNTING_CORE_AK_COA_G02_FINAL_PMO_VERIFICATION_2026_09_01.md`
6. G02 fresh Independent Re-audit:
   `CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_COA_G02_CORR1_TARGETED_INDEPENDENT_REAUDIT_2026_09_01.md`
7. COA Base Kernel + AI Semantic Consolidation Standard:
   `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`
8. Boss Cross-Gate SaaS Invariants:
   `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`
9. Boss 19 ACTIVE Account Types ruling:
   `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`
10. G01/G02 verified Boss-approved ODOO18 workbook baseline and its controlled extraction/evidence.
11. Five-Unit G03 challenge:
   `ad0451e7b6b1e8962659b35056c46dc10a1b6aa6`

Authority order:

`Boss Ruling > Fresh Independent Audit / PMO verified evidence > Primary Evidence > Team B Executor Claim`

## 4. CLOSED G02 BASELINE — DO NOT REOPEN WITHOUT CONTRADICTORY PRIMARY EVIDENCE

Accepted G02 baseline:

`BASE COA KERNEL = 36 SEMANTIC CONCEPTS`

Derived and independently supported from:

`39 explicit ODOO18 anchors - 9 controlled reductions + 6 mandatory additions = 36`

Boss final state:

`COA-G02 = APPROVED / PASS / CLOSED`

G03 must preserve:

- K01..K36 semantic baseline;
- Boss 19 ACTIVE Account Types;
- Account Code / Name / source ID as provenance only;
- G02 later-Gate ownership boundaries for G04/G04S/G05/G06/G07.

If G03 discovers a genuine contradictory primary fact affecting G02, STOP and create a named conflict record. Do not silently rewrite the G02 baseline.

## 5. G03 OBJECTIVE

Classify source accounts by **business meaning and accounting treatment** and consolidate source-specific/customized rows into defensible canonical account candidates only when treatment is materially equivalent.

Mandatory transformation:

`Source Account -> Business Meaning -> Accounting Treatment -> Canonical Group -> SMEsPlus Target Account Candidate`

The goal is not to reduce the account count as far as possible.

The goal is to produce the smallest **defensible**, traceable, Thailand-safe, SaaS-safe canonical consolidation candidate set from the authorized source evidence.

## 6. PRIMARY ROW-LEVEL POPULATION

Primary row-level population:

`Boss-approved ODOO18 workbook = 389 source rows`

This is a source observation population, not a target-count mandate.

At minimum, all 389 ODOO18 rows must receive exactly one G03 disposition.

Other evidence sources such as `l10n_th`, Team A Deep Research and controlled G01 evidence are semantic/regulatory/control references. Do not silently blend separate source populations or double-count them as additional ODOO18 rows.

Required reconciliation:

`BASE_KERNEL + MERGE_TO_CANONICAL + KEEP_SEPARATE + RESERVED / NOT DEFAULT-TH + HOLD / EVIDENCE_REQUIRED = 389 source rows`

Exactly one row-level disposition per source row.

## 7. ALLOWED ROW-LEVEL OUTCOMES

Every ODOO18 source row must receive exactly one of:

- `BASE_KERNEL`
- `MERGE_TO_CANONICAL`
- `KEEP_SEPARATE`
- `RESERVED / NOT DEFAULT-TH`
- `HOLD / EVIDENCE_REQUIRED`

### BASE_KERNEL

Use when the source row maps to a Boss-accepted G02 kernel semantic K01..K36.
Record exact K target and evidence.

### MERGE_TO_CANONICAL

Use only when multiple source rows have materially equivalent accounting treatment.
Record:

- source row / stable evidence row key;
- source account code/name;
- source Account Type;
- source business meaning;
- accounting treatment;
- target canonical candidate;
- reason for merge;
- treatment-equivalence evidence;
- provenance retained;
- dimensions/source attributes retained outside GL identity where relevant.

### KEEP_SEPARATE

Use where accounting treatment materially differs or any Do-NOT-Merge rule applies.
State the exact material difference.

### RESERVED / NOT DEFAULT-TH

Use only where controlled evidence shows the row is not a default Thailand canonical candidate but should remain available/reserved/extension-capable.
Do not use as a dumping category for uncertainty.

### HOLD / EVIDENCE_REQUIRED

Use where evidence is insufficient to decide safely.
State:

- missing evidence;
- why the decision cannot be made safely;
- responsible later Gate if already controlled;
- whether the unresolved item blocks G03 Gate closure.

## 8. MANDATORY DO-NOT-MERGE TEST — ALL PROPOSED MERGES

Before any N-to-1 consolidation, test all 13 controls:

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

If any materially differs:

`MERGE_TO_CANONICAL = PROHIBITED`

Use `KEEP_SEPARATE` or `HOLD / EVIDENCE_REQUIRED`.

## 9. DIMENSION-OVER-ACCOUNT-PROLIFERATION CONTROL

If a distinction is operational or analytical rather than accounting-recognition driven, do not multiply GL accounts by default.

Challenge examples include:

- Sales Channel / Marketplace
- Customer
- Product
- Branch / Location
- Salesperson
- Campaign
- Source System
- Marketplace Order Source

Where recognition, tax treatment, reconciliation/control role and financial meaning are materially equivalent, preserve the distinction as a dimension/source attribute/provenance field rather than canonical GL identity.

Every dimension decision must be evidenced; do not assume all channel/company distinctions are equivalent.

## 10. HIGH-RISK SEMANTIC CLUSTERS — MANDATORY REVIEW

The G03 package must explicitly review at least:

1. Cash / Bank / Transfer / Suspense / Outstanding Receipt / Outstanding Payment
2. Trade Receivable / channel or POS receivable variants
3. Trade Payable and payable/control variants
4. Inventory / GRNI / COGS / valuation-related source rows
5. Fixed Asset / Accumulated Depreciation / Depreciation Expense
6. Operating revenue / online or channel revenue variants
7. General operating expense / salary / rent / other expense variants
8. WHT Creditable and WHT Payable source variants
9. Input VAT / Undue Input VAT
10. Output VAT / Undue Output VAT
11. Prepaid CIT / CIT Payable / CIT Expense
12. Share Capital / Retained Earnings / Current Year Earnings / distribution-related rows
13. FX Gain / FX Loss
14. Cash Difference Gain / Loss
15. Early Payment Discount Gain / Loss
16. Any source row with reconcile=True
17. Any source row carrying company-specific, channel-specific, custodian-specific or source-system-specific naming that could be mistaken for canonical identity

## 11. CONTROLLED LATER-GATE BOUNDARIES

G03 shall not prematurely close later-Gate questions.

Examples:

- K14 final accumulated-depreciation Account Type / contra rule -> G04
- Account Group architecture -> G04
- Standard Template / Tenant Instance provisioning/versioning/upgrade -> G04S
- Financial-statement taxonomy -> G05
- final WHT PND form-specific statutory GL/subledger granularity -> G06
- runtime tenant/company isolation and dimension proof -> G07
- final COA independent freeze -> G08

A controlled later-Gate dependency is not automatic completion credit.

## 12. SAAS INVARIANT COMPLIANCE — MANDATORY G03 RECORD

Create a G03 SI-01..SI-10 matrix.

For every SI record all Boss-required fields:

1. Applicability to G03
2. Evidence Location
3. Owner / Owner Role
4. Reviewer / Verifier
5. Verification Status
6. Conflict / Exception
7. Gate Impact

Allowed Verification Status values only:

- `PASS / VERIFIED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`
- `N/A — JUSTIFICATION REQUIRED`

G03 minimum interpretation:

- consolidation decisions preserve tenant/company boundaries;
- source code/name/technical ID are not canonical identity;
- similar names/codes do not create shared identity by default;
- no source/vendor schema/API/ORM architecture is adopted;
- runtime G04S/G07 proof is not falsely claimed.

## 13. REQUIRED G03 DELIVERABLES

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G03_EVIDENCE/`

At minimum:

1. `COA_G03_SOURCE_SEMANTIC_CLASSIFICATION_REGISTER.md`
   - complete 389-row disposition register;
   - exactly one outcome per source row.

2. `COA_G03_CANONICAL_CONSOLIDATION_REGISTER.md`
   - every G03 canonical candidate;
   - contributing source rows;
   - business meaning;
   - accounting treatment;
   - do-not-merge check result;
   - evidence.

3. `COA_G03_SOURCE_TO_CANONICAL_PROVENANCE_MAP.md`
   - complete source-to-Kernel/canonical/keep-separate/reserved/hold traceability.

4. `COA_G03_DO_NOT_MERGE_AND_EXCEPTION_REGISTER.md`
   - material-difference findings;
   - high-risk clusters;
   - holds/conflicts.

5. `COA_G03_DIMENSION_DECISION_REGISTER.md`
   - distinctions removed from GL identity and retained as dimensions/source attributes;
   - evidence for each decision.

6. `COA_G03_SAAS_INVARIANT_COMPLIANCE.md`
   - SI-01..SI-10 with all mandatory fields/status vocabulary.

7. `COA_G03_RECONCILIATION_CHECK.md`
   - mechanical count checks;
   - 389/389 coverage;
   - zero orphan rows;
   - zero unregistered duplicate dispositions;
   - candidate arithmetic;
   - G02 K01..K36 traceability check.

8. `COA_G03_GATE_REPORT.md`
   - Team B evidence-production disposition only;
   - blocking findings;
   - explicit next independent-review route.

## 14. EVIDENCE ID RULE

G03 may use evidence-local candidate identifiers such as:

`G03-CAND-001`

for traceability inside the evidence package.

These are **audit/evidence identifiers only**.

They must not be presented as future production canonical IDs, database PKs, schema keys or implementation architecture.

## 15. MECHANICAL COMPLETION CHECKS

Before publication verify:

- ODOO18 source rows expected = 389;
- ODOO18 source rows dispositioned = 389;
- missing rows = 0;
- unregistered duplicate dispositions = 0;
- each source row has exactly one allowed outcome;
- every `BASE_KERNEL` row maps to K01..K36;
- every `MERGE_TO_CANONICAL` row has a target and equivalence evidence;
- every `KEEP_SEPARATE` row has material do-not-merge evidence;
- every `HOLD / EVIDENCE_REQUIRED` row has explicit missing evidence and Gate impact;
- all canonical candidates preserve source provenance;
- K01..K36 baseline semantics remain unchanged unless a named contradictory primary-evidence conflict is raised;
- Boss 19 ACTIVE Account Types remain unchanged;
- SI-01..SI-10 matrix has exactly 10 rows and all required fields;
- Verification Status cells use only approved vocabulary;
- no G04/G04S/G05/G06/G07/G08 execution artifacts created;
- no database/API/ORM/schema/implementation content created.

## 16. G03 GATE TREATMENT OF HOLDS

A `HOLD / EVIDENCE_REQUIRED` source row that materially changes whether a source account should merge, remain separate, or define a canonical accounting semantic is a G03 blocker unless Boss has explicitly ruled it a controlled downstream dependency.

Do not hide blocking uncertainty behind candidate counts.

If blocking Holds remain, Team B terminal state must be:

`COA-G03 = HOLD / EVIDENCE REQUIRED`

If row coverage and semantic consolidation are complete with no G03 blocking finding, Team B may state only:

`COA-G03 TEAM B SEMANTIC CONSOLIDATION = COMPLETE / READY FOR FRESH INDEPENDENT AUDIT`

This is not G03 PASS.

## 17. TEAM B TERMINAL STATUS

If no G03 blocker remains, stop with:

`COA-G03 TEAM B SEMANTIC CONSOLIDATION = COMPLETE`

`ODOO18 ROW RECONCILIATION = 389/389`

`G02 36-CONCEPT KERNEL = PRESERVED`

`G03 CANONICAL CONSOLIDATION CANDIDATE COUNT = <EVIDENCE-DERIVED COUNT> / TEAM B CANDIDATE ONLY`

`COA-G03 = READY FOR FRESH INDEPENDENT AUDIT`

`COA-G04 = NOT STARTED / NOT AUTHORIZED`

`DEVELOPMENT / PRODUCTION = NOT AUTHORIZED`

If a blocker exists, replace READY with the exact HOLD/FAIL disposition and named findings.

Do not use `BOSS APPROVED`, `G03 CLOSED`, `FINAL THAI COA`, or `READY FOR DEVELOPMENT`.

## 18. INDEPENDENT REVIEW ROUTING

After Team B publication:

`Fresh Independent Audit -> PMO Verification only if audit PASS -> Boss G03 Decision`

The Team B execution session shall not perform its own Independent Audit or PMO Verification.

A fresh reviewer must challenge at minimum:

- 389/389 row coverage;
- disposition exclusivity;
- every N-to-1 merge;
- high-risk Do-NOT-Merge clusters;
- G02 Kernel preservation;
- candidate-count arithmetic;
- source provenance;
- dimensions vs GL decisions;
- SI-01..SI-10;
- scope leakage into G04+ or implementation.

## 19. PROHIBITED ACTIONS

Do NOT:

- force a target canonical account count;
- optimize toward 32, 36, 144, 389 or any other preselected number;
- merge solely by account name/code similarity;
- change the G02 36-concept baseline silently;
- create final production account codes;
- define production database canonical IDs;
- design schema/API/ORM/tables;
- freeze Account Groups;
- freeze financial-statement taxonomy;
- make unsupported Thailand statutory claims;
- claim runtime SaaS/multi-company proof;
- start G04, G04S, G05, G06, G07 or G08;
- authorize Team C, Development, Release, Deployment or Production;
- self-approve G03.

## 20. PROGRESS REPORTING

Unless an approved evidence-weighted denominator exists, report exactly:

`% Board = TBD / NO APPROVED BASELINE`

`% STATE = TBD / NO APPROVED BASELINE`

`% STEP = TBD / NO APPROVED BASELINE`

No guessed percentages.

## 21. EXECUTION COMMAND

After explicit Boss authorization for COA-G03 execution, proceed autonomously through Team B G03 evidence publication only.

Do not ask Boss to reconfirm the already-defined semantic-consolidation method unless a genuine new authority conflict is discovered.

Stop immediately after Team B publication and report:

- publication commit;
- all G03 evidence paths;
- exact 389-row reconciliation result;
- disposition counts;
- evidence-derived Team B canonical candidate count;
- blocking findings, if any;
- fresh Independent Audit handoff requirement.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
