# NEW SESSION WORK — SMEsPlus Thailand COA Closure / Cross-Gate SaaS Carry-Forward V3

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Jira: ERPPLUS-132
Boss: Sole Final Approver
Control Level: /L99.99

## 1. Current Authority

Boss has approved:

1. Dedicated Thailand COA Closure workstream.
2. Mandatory `COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture`.
3. Mandatory `CROSS-GATE SAAS INVARIANTS` applying to every COA Gate from G01 through G08.

Authority evidence:

- Initial COA closure authorization: `e8cc4d942d7f5c611ca3add0266c39196515b636`
- COA-G04S SaaS Architecture amendment: `c084a741b22e3352992fbeb0c212cbd1463efb92`
- Cross-Gate SaaS Invariants ruling: `e16b29f35d8011723a6e2593994bc226870d9fd7`
- Revised Evidence Index with invariant control: `79719e6866b6f9277ef8f8d99f42be1ffbdc01da`

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

## 3. Mandatory Cross-Gate SaaS Invariants

These invariants apply to **every** COA Gate: G01, G02, G03, G04, G04S, G05, G06, G07 and G08.

- `SI-01 Tenant context is mandatory.`
- `SI-02 Company context is mandatory where company-scoped.`
- `SI-03 Standard Template is not tenant-owned mutable data.`
- `SI-04 Tenant customization cannot modify the published Standard Template.`
- `SI-05 Account Code / Name is not canonical identity.`
- `SI-06 Published Template Version is immutable.`
- `SI-07 Upgrade is explicit, previewable and auditable.`
- `SI-08 No cross-tenant COA access.`
- `SI-09 Company customization must preserve canonical reporting semantics.`
- `SI-10 SaaS Core must not hard-code Thailand-specific source architecture.`

Every Gate output must include a `SAAS INVARIANT COMPLIANCE` matrix for SI-01..SI-10.

For each SI record:

- applicability;
- evidence;
- owner / owner role;
- reviewer / verifier;
- verification status;
- conflict / exception;
- Gate impact.

Allowed status:

`PASS / VERIFIED`
`HOLD / EVIDENCE REQUIRED`
`FAIL / FROZEN`
`N/A — JUSTIFICATION REQUIRED`

Enforcement:

- applicable SI violation -> Gate = `FAIL / FROZEN`;
- applicable SI evidence missing -> Gate = `HOLD`;
- no Gate may be declared PASS, FROZEN, READY FOR HANDOFF or COMPLETE while an applicable SI is unresolved;
- any exception requires an explicit Boss-controlled exception ruling.

## 4. Approved Thailand COA Baseline

- Target localization: Thailand.
- Non-Thai localization COA: out of current COA scope unless Boss reopens it.
- Boss-approved Odoo18 workbook tab: primary business-facing source/reference, not target architecture.
- Core source Account Type universe: 19.
- SMEsPlus Local Thailand target: 19 ACTIVE Account Types.
- Off-Balance Sheet: active but excluded from ordinary Balance Sheet/P&L totals by default.
- Account Group: maintainable per Company, but must not silently redefine Account Type or canonical accounting meaning.
- Financial Statement Mapping: independent from company-specific Account Group.
- Account Code / Name: not canonical identity.
- `389 source rows != 389 SMEsPlus target accounts`.
- Approx. `~32 Base Kernel`: working expectation only.
- Exact Base Kernel count: `TBD / EVIDENCE REQUIRED`.
- Exact final Standard Thai COA count: `TBD / EVIDENCE REQUIRED`.
- Prefer dimensions over GL-account proliferation where accounting treatment is materially equivalent.

## 5. Revised Mandatory Gate Sequence

1. COA-G01 — Source Baseline Reconciliation
2. COA-G02 — Base COA Kernel Discovery
3. COA-G03 — AI Semantic Consolidation
4. COA-G04 — Account Type & Account Group Architecture
5. COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture
6. COA-G05 — Financial Statement Taxonomy
7. COA-G06 — Thailand Tax Accounting Controls
8. COA-G07 — Multi-company & Dimension Proof
9. COA-G08 — Independent Audit + PMO Verification + Boss Final COA Freeze

Cross-Gate SaaS Invariants constrain every Gate from G01 onward.

`COA-G04S` remains mandatory and blocks G05 and later freeze activities.

## 6. COA-G04S Mandatory Scope

When authorized to execute G04S, it must define and evidence:

- Tenant isolation
- Company isolation
- Standard Thai COA Template vs Company COA Instance separation
- COA provisioning for new Tenant / Company
- Standard COA Template versioning
- Tenant/Company customization boundary
- Controlled upgrade / delta handling
- Backward compatibility
- Canonical account identity independent from Account Code / Name
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

## 7. Current Gate Execution — COA-G01 Only

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
- Tenant Context relevance
- Company Context relevance
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
- Cross-Gate SaaS Invariant impact

Fact status must be one of:

`VERIFIED FACT / SUPPORTED INFERENCE / ASSUMPTION / UNKNOWN / EVIDENCE_MISSING / CONFLICTING EVIDENCE`

Do not convert UNKNOWN into FACT.

### COA-G01 SaaS Control

COA-G01 must not merely collect accounting source facts. It must also flag source assumptions that could contaminate SaaS design, including:

- source tenant/company ownership assumptions;
- source account code/name identity assumptions;
- shared mutable template behaviour;
- Thailand-specific source architecture that must not be hard-coded into SaaS Core;
- source structures that could create cross-tenant coupling if copied.

COA-G01 must produce its own SI-01..SI-10 compliance matrix before Gate review.

## 8. Mandatory Prohibitions

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
- use Account Code / Name as canonical identity
- permit tenant customization to mutate a published Standard Template
- silently overwrite Tenant/Company instances from a Template version change
- permit cross-tenant COA access
- hard-code Thailand-specific source architecture into SaaS Core
- self-approve any Gate
- skip COA-G01
- skip COA-G04S later

Development Authorization = NOT GRANTED.
Production Authorization = NOT GRANTED.

## 9. System of Record

Jira: `ERPPLUS-132`

GitHub: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `SMEsPlus`

Cross-Gate SaaS Ruling:
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`

Revised Evidence Index:
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md`

## 10. Start Command

`START COA-G01 — SOURCE BASELINE RECONCILIATION WITH CROSS-GATE SAAS INVARIANTS.`

First:

1. verify Jira/GitHub coordinates;
2. read existing COA evidence;
3. read Boss Cross-Gate SaaS Invariants ruling;
4. reconcile existing evidence before new research;
5. report evidence conflicts immediately;
6. execute COA-G01 only;
7. produce SI-01..SI-10 compliance evidence for G01;
8. STOP at the COA-G01 Gate and report to Boss.

Do not proceed to COA-G02 without Boss authorization.
