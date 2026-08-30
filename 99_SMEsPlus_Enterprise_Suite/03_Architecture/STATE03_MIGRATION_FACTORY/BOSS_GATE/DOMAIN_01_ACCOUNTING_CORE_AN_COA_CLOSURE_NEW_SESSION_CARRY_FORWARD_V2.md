# NEW SESSION WORK — SMEsPlus Thailand COA Closure / SaaS Architecture Carry-Forward V2

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Jira: ERPPLUS-132
Boss: Sole Final Approver
Control Level: /L99.99

## 1. Current Authority

Boss has approved the dedicated workstream:

`[STATE03][DOMAIN_01] SMEsPlus Thailand COA Architecture Closure & Boss Freeze / L99.99`

Boss subsequently approved a mandatory architecture amendment because SMEsPlus is a SaaS platform:

`COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture`

Boss authorization evidence:

- Initial COA closure authorization: `e8cc4d942d7f5c611ca3add0266c39196515b636`
- COA + SaaS mandatory Gate amendment: `c084a741b22e3352992fbeb0c212cbd1463efb92`
- Revised Evidence Index: `a3926b911c8193a5530b2dbdfbf76ba7f2351df7`

Current execution Gate remains:

`COA-G01 — Source Baseline Reconciliation`

Do NOT skip to G02 or later Gates.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

## 2. Project Identity

SMEsPlus is a NEW 100% Clean-room Node.js SaaS ERP.

Odoo / Salesforce / SAP Business One / other ERP platforms are reference / learning / benchmark only.

This is NOT an Odoo customization, clone, schema clone, ORM clone, source-code reuse project, or vendor architecture reimplementation.

Absolute rule:

`MIGRATE / LEARN BUSINESS FACTS + BUSINESS SEMANTICS, NOT LEGACY APPLICATION ARCHITECTURE.`

## 3. Approved Thailand COA Baseline

- Target localization: Thailand.
- Non-Thai localization COA: out of current COA scope unless Boss reopens it.
- Boss-approved Odoo18 workbook tab: primary business-facing source/reference, not target architecture.
- Core source Account Type universe: 19.
- SMEsPlus Local Thailand target: 19 ACTIVE Account Types.
- Off-Balance Sheet: active but excluded from ordinary Balance Sheet/P&L totals by default.
- Account Group: maintainable per Company, but must not silently redefine Account Type or canonical accounting meaning.
- Financial Statement Mapping: independent from company-specific Account Group.
- Account Code: not canonical identity.
- `389 source rows != 389 SMEsPlus target accounts`.
- Approx. `~32 Base Kernel`: working expectation only.
- Exact Base Kernel count: `TBD / EVIDENCE REQUIRED`.
- Exact final Standard Thai COA count: `TBD / EVIDENCE REQUIRED`.
- Prefer dimensions over GL-account proliferation where accounting treatment is materially equivalent.

## 4. Revised Mandatory Gate Sequence

1. COA-G01 — Source Baseline Reconciliation
2. COA-G02 — Base COA Kernel Discovery
3. COA-G03 — AI Semantic Consolidation
4. COA-G04 — Account Type & Account Group Architecture
5. COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture
6. COA-G05 — Financial Statement Taxonomy
7. COA-G06 — Thailand Tax Accounting Controls
8. COA-G07 — Multi-company & Dimension Proof
9. COA-G08 — Independent Audit + PMO Verification + Boss Final COA Freeze

`COA-G04S` is mandatory and blocks G05 and later freeze activities.

## 5. COA-G04S Mandatory Scope

When authorized to execute G04S, it must define and evidence:

- Tenant isolation
- Company isolation
- Standard Thai COA Template vs Company COA Instance separation
- COA provisioning for new Tenant / Company
- Standard COA Template versioning
- Tenant/Company customization boundary
- Controlled upgrade / delta handling
- Backward compatibility
- Canonical account identity independent from Account Code
- Company-maintainable Account Group behaviour
- Multi-company sharing / separation rules
- Role / permission boundary for COA maintenance
- Audit / change history
- Migration mapping compatibility
- Canonical reporting continuity after customization / upgrade

Conceptual target flow:

`SMEsPlus SaaS Platform`
` -> Thailand Localization Profile`
` -> Standard Thai COA Template`
` -> Template Version`
` -> Tenant`
` -> Company COA Instance`
` -> Company-maintainable Account Groups`
` -> Company Posting Accounts`
` -> Dimensions`
` -> Canonical Financial Statement Mapping`

Template upgrade principle:

`Template Version Change -> Compatibility Assessment -> Tenant Delta Analysis -> Upgrade Preview -> Controlled Apply -> Audit Evidence`

Do not design the Standard COA Template as one live record set whose modification silently changes every Tenant.

## 6. Current Gate Execution — COA-G01 Only

Build one controlled Source Baseline from:

A. Team A Deep Research / Accounting Core evidence
B. Authorized Accounting Core learning source
C. Thailand localization `l10n_th`
D. Boss-approved Odoo18 workbook tab
E. Boss-provided Thai COA business requirements
F. Boss-provided Thai financial-statement presentation evidence
G. Existing Boss rulings / PMO / ChatGPT audit evidence
H. Primary Thai regulatory sources where statutory claims are made

Do not treat any single source as target architecture.

For each significant accounting concept determine:

- Source
- Evidence
- Business Meaning
- Thailand Relevance
- Account Type
- Financial Class
- Normal Balance
- Reconciliation Behaviour
- Tax Relevance
- Financial Statement Relevance
- System/Control Dependency
- Base Kernel Candidacy
- Canonicalization Relevance
- Evidence Strength
- Conflict / Gap / Unknown
- Clean-room Status

Fact status must be one of:

`VERIFIED FACT / SUPPORTED INFERENCE / ASSUMPTION / UNKNOWN / EVIDENCE_MISSING / CONFLICTING EVIDENCE`

Do not convert UNKNOWN into FACT.

## 7. Mandatory Prohibitions

Do NOT:

- start coding
- design production database schema
- implement APIs
- start Development
- start Production
- copy vendor technical architecture
- clone source tables/classes/models
- infer missing evidence
- freeze 32 accounts arbitrarily
- freeze 389 accounts
- self-approve any Gate
- skip COA-G01
- skip COA-G04S later
- make a Standard Template change silently propagate to every Tenant

Development Authorization = NOT GRANTED.
Production Authorization = NOT GRANTED.

## 8. System of Record

Jira: `ERPPLUS-132`

GitHub: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `SMEsPlus`

Revised Evidence Index:
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md`

## 9. Start Command

`START COA-G01 — SOURCE BASELINE RECONCILIATION.`

First:

1. verify Jira/GitHub coordinates;
2. read existing COA evidence;
3. reconcile existing evidence before new research;
4. report evidence conflicts immediately;
5. execute COA-G01 only;
6. STOP at the COA-G01 Gate and report to Boss.

Do not proceed to COA-G02 without Boss authorization.
