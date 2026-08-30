# DOMAIN_01 Accounting Core — COA-G01 Source Baseline Reconciliation / L99.99

Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Gate: COA-G01 — Source Baseline Reconciliation
Jira: ERPPLUS-132
Branch: SMEsPlus
Final Approval Authority: Boss

## 1. Gate Result

`COA-G01 EXECUTION PACKAGE = COMPLETE FOR REVIEW`

`ChatGPT Evidence Review = PASS / VERIFIED FOR COA-G01 SCOPE`

`Boss Final COA-G01 Gate Decision = PENDING`

`COA-G02 = NOT STARTED / BLOCKED PENDING BOSS AUTHORIZATION`

This is not a Development or Production authorization.

The purpose of COA-G01 is to reconcile source facts, Boss-controlled target requirements, Thai regulatory anchors and SaaS contamination controls. It does **not** freeze the exact Base Kernel, exact final Standard Thai COA, financial-statement mapping, tax-account mapping or implementation architecture.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.

---

## 2. Authority Baseline

Mandatory authority / governance inputs:

1. `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`
2. `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AG_BOSS_COA_LOCAL_TH_RULING.md`
3. `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`
4. `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`
5. `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AP_COA_CLOSURE_NEW_SESSION_CARRY_FORWARD_V3_CROSS_GATE_SAAS.md`

Controlling principles:

- SMEsPlus is a NEW 100% Clean-room Node.js SaaS ERP.
- Odoo / Salesforce / SAP Business One / legacy systems are reference / learning / benchmark only.
- Business facts and business semantics may be learned; vendor technical architecture may not be copied.
- Account Code / Name is not canonical identity.
- `389 source rows != 389 SMEsPlus target accounts`.
- Exact Base Kernel count remains `TBD / EVIDENCE REQUIRED` until COA-G02.
- SMEsPlus Local Thailand target Account Type baseline = 19 ACTIVE types by Boss ruling.

---

## 3. Controlled Source Register A–H

| Ref | Required source layer | Evidence location | Verification | Fact treatment | Gate impact |
|---|---|---|---|---|---|
| A | Team A Deep Research / Accounting Core evidence | `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/02_SOURCE_EVIDENCE.md`, `06_BUSINESS_RULE_REGISTER.md`, `09_DATA_SEMANTIC_REGISTER.md` | VERIFIED — committed read-only evidence inspected | VERIFIED FACT | No blocker |
| B | Authorized Accounting Core learning source | Team A SE-01..SE-34 direct source anchors; especially SE-17 account type, SE-18 internal group/initial balance, SE-20 reconcile, SE-15/16 company currency | VERIFIED THROUGH CONTROLLED SOURCE EVIDENCE | VERIFIED FACT | No blocker; source mechanics remain non-target |
| C | Thailand localization `l10n_th` | `COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`; controlled source result = 144 rows / 15 types | VERIFIED HISTORICAL SOURCE OBSERVATION | VERIFIED FACT | No blocker; not target count authority |
| D | Boss-approved Odoo18 workbook tab | Drive file `Account_Odoo18_19 sent 270369.xlsx`, ID `1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f`; `COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md` | DIRECTLY RE-VERIFIED 2026-08-30: first table rows 0..388, last row 388 present | VERIFIED FACT | Primary business-facing seed, not architecture |
| E | Boss Thai COA business requirements | AG/AJ/AK Boss rulings + `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md` | VERIFIED | BOSS-CONTROLLED REQUIREMENT | No blocker |
| F | Thai financial-statement presentation evidence | Boss AJ ruling establishes BS/P&L/off-balance presentation principles; TFAC TAS 1 current standards register and DBD 2566 statement-item regulatory anchor | VERIFIED AT G01 CLASSIFICATION LEVEL | VERIFIED FACT / CONTROL REQUIREMENT | Exact line mapping deferred to G05 |
| G | Existing Boss / PMO / ChatGPT audit evidence | ERPPLUS-132 + BOSS_GATE evidence index + cross-gate invariant ruling | VERIFIED | GOVERNANCE FACT | No blocker |
| H | Primary Thai regulatory sources for statutory claims | TFAC, DBD, Revenue Department URLs in §10 | VERIFIED PRIMARY/OFFICIAL SOURCE ANCHORS | VERIFIED FACT at concept level | Exact tax rules/rates/mapping deferred to G06 |

### Direct workbook re-verification note

The connected Drive source was re-opened in this execution. The first table starts with:

- row 0: `Cash Bakery`, code `110000002`, `Bank and Cash`
- row 11: `ลูกหนี้การค้า`, code `111600010`, `Receivable`

and ends with:

- row 385: `Undistributed Profits/Losses`, `Current Year Earnings`
- row 386: `ใบเสร็จรับเงินค้างชำระ`, `Current Assets`
- row 387: `การชำระเงินค้างชำระ`, `Current Assets`
- row 388: `บัญชีพัก - ฐานภาษีมูลค่าเพิ่ม`, code `950001009`, `Expenses`

Therefore the previous controlled inventory of 389 Odoo18 source rows is independently re-supported in this Gate execution.

---

## 4. Reconciled Account Type Baseline

The evidence layers have different roles and must not be collapsed into one count:

| Evidence layer | Count | Meaning | Status |
|---|---:|---|---|
| Accounting Core source universe | 19 | Source-supported Account Type capabilities | VERIFIED FACT |
| Inspected `l10n_th` template | 15 | Types instantiated in 144 Thai source-template rows | VERIFIED FACT |
| Boss-approved Odoo18 workbook | 14 | Labels actually observed in 389 source rows | VERIFIED FACT |
| SMEsPlus Local Thailand target | 19 | Active target business capabilities mandated by Boss | BOSS APPROVED BASELINE |

Reconciliation rule:

`Source observation count != Target capability count`

`Template omission != Business prohibition`

The earlier `15 ACTIVE + 4 RESERVED` design recommendation is superseded for target design by the Boss 19-active ruling. The historical observation that `l10n_th` used 15 types remains unchanged.

### 19 Active Target Business Types

| Type | Financial class | Normal-balance principle | G01 status |
|---|---|---|---|
| Receivable | Asset | Debit | ACTIVE / VERIFIED BASELINE |
| Bank and Cash | Asset | Debit | ACTIVE / VERIFIED BASELINE |
| Current Assets | Asset | Debit | ACTIVE / VERIFIED BASELINE |
| Non-current Assets | Asset | Debit | ACTIVE / VERIFIED BASELINE |
| Prepayments | Asset | Debit | ACTIVE / Boss-required despite source-template omission |
| Fixed Assets | Asset | Debit | ACTIVE / VERIFIED BASELINE |
| Payable | Liability | Credit | ACTIVE / VERIFIED BASELINE |
| Credit Card | Liability | Credit | ACTIVE / Boss-required despite source-template omission |
| Current Liabilities | Liability | Credit | ACTIVE / VERIFIED BASELINE |
| Non-current Liabilities | Liability | Credit | ACTIVE / VERIFIED BASELINE |
| Equity | Equity | Credit | ACTIVE / VERIFIED BASELINE |
| Current Year Earnings | Equity/result carry | Normally credit for profit; may debit for loss | ACTIVE / VERIFIED BASELINE |
| Income | P&L income | Credit | ACTIVE / VERIFIED BASELINE |
| Other Income | P&L income | Credit | ACTIVE / VERIFIED BASELINE |
| Expenses | P&L expense | Debit | ACTIVE / VERIFIED BASELINE |
| Other Expenses | P&L expense | Debit | ACTIVE / Boss-required despite source-template omission |
| Depreciation | P&L expense classification in source capability | Debit | ACTIVE; source-row semantics require review |
| Cost of Revenue | P&L expense/cost | Debit | ACTIVE / VERIFIED BASELINE |
| Off-Balance Sheet | Memorandum / outside ordinary BS and P&L totals | Controlled memorandum treatment | ACTIVE / Boss-controlled special rule |

Normal-balance entries above are accounting-semantic classification for reconciliation; they are not vendor implementation mechanics.

---

## 5. Significant Accounting Concept Reconciliation

| Concept | Source / Evidence | Business meaning | TH relevance | Tenant / Company relevance | Reconciliation / tax / FS relevance | Base Kernel candidacy | Fact status | G01 disposition |
|---|---|---|---|---|---|---|---|---|
| Account Type | Team A SE-17/18; l10n_th; workbook; AJ ruling | Canonical accounting class driving reporting semantics | High | Must remain canonical and not tenant-code identity | FS high; tax indirect | High | VERIFIED FACT | 19 active target baseline retained |
| Account Code / Name | Team A SE-19; workbook; AG/AO rulings | Business-facing numbering/label | High | May vary by tenant/company; cannot be canonical identity | Mapping/provenance | Low as identity | VERIFIED FACT | Source attribute only |
| Account Group | Boss AK/AG baseline | Company-maintainable organization layer | High | Company-scoped | Must not redefine Account Type/FS semantics | Not account identity | BOSS-CONTROLLED REQUIREMENT | Carry to G04/G07 |
| Reconcile flag | Team A SE-20 / BR-09; workbook `reconcile` | Determines matching/reconciliation behavior | High | Company account behavior | AR/AP/cash control | High for control accounts | VERIFIED FACT | Carry to G02/G03 |
| Current Year Earnings | Team A type semantics; workbook row 385; AJ | Year-result / equity carry semantics | High | Company/accounting-period scoped | FS/equity high | High | VERIFIED FACT | Must stay separate from ordinary income/expense |
| Off-Balance | Core type + AJ Boss ruling | Active memorandum/control capability | High by Boss requirement | Tenant/company isolated | Excluded from ordinary BS/P&L totals by default | Candidate based on control need | VERIFIED FACT + BOSS REQUIREMENT | Carry to G05/G07 |
| Debit/Credit balance | Team A SE-03/04, BR-01..03, BR-17..20 | Journal integrity | Universal | Company ledger scoped | Fundamental accounting control | System control, not COA identity | VERIFIED FACT | Do not infer DB-level entry balance from source existence |
| Company currency | Team A SE-15/16, BR-06 | Ledger monetary context | High | Company mandatory | Monetary/reporting high | System control | VERIFIED FACT | Company context mandatory |
| Lock / inalterability controls | Team A SE-13, SE-22..26, BR-11..14 | Posted-ledger integrity and period control | High | Company/user scoped | Audit/control high | System control | VERIFIED FACT | Source mechanics not copied; business control retained for later architecture |
| VAT | Workbook rows include input VAT / VAT suspense concepts; Revenue Department official source | Thai VAT accounting obligations | Thailand statutory | Tenant/company tax configuration scoped | Tax high | Candidate categories likely | VERIFIED FACT at concept level | Exact accounts/rules deferred G06 |
| WHT | Workbook row 42 + Revenue Department official WHT source | Withholding tax receivable/payable/control semantics | Thailand statutory | Tenant/company tax configuration scoped | Tax high | Candidate categories likely | VERIFIED FACT at concept level | Exact mapping deferred G06 |
| CIT | Workbook row 43 `ภาษีนิติบุคคลจ่ายล่วงหน้า` + Revenue Department CIT source | Corporate income tax current/prepaid/control concepts | Thailand statutory | Legal entity/company scoped | Tax/FS high | Candidate categories likely | VERIFIED FACT at concept level | Exact mapping deferred G06 |
| Financial statement presentation | TFAC TAS 1 register; DBD 2566 statement-item requirement; AJ off-balance ruling | Standard presentation independent from arbitrary company grouping | Thailand statutory/reporting | Company reporting; canonical mapping platform-controlled | FS critical | Not itself a posting account | VERIFIED FACT / CONTROL | Exact taxonomy deferred G05 |
| Semantic consolidation | Base Kernel + AI Consolidation Standard | N source rows may map to one canonical target when treatment is materially equivalent | High | Must preserve tenant provenance | Reporting/tax/reconcile differences block merge | G02/G03 | BOSS-CONTROLLED REQUIREMENT | Do not use name/code similarity alone |
| Dimension over GL proliferation | Base Kernel + AI Consolidation Standard | Operational distinctions should be dimensions when accounting treatment is unchanged | High | Tenant/company dimensions scoped | Must preserve reporting semantics | Reduces false kernel growth | BOSS-CONTROLLED REQUIREMENT | Carry to G03/G07 |
| Template / Instance separation | AG/AO Boss rulings | Standard Template separated from Company/Tenant instance and source mapping | SaaS critical | Tenant + Company mandatory | Reporting continuity | Architecture control | BOSS-CONTROLLED REQUIREMENT | Deep design deferred G04S |

---

## 6. Source Conflict / Ambiguity Register

These are source-quality or source-to-target interpretation issues. They are **not** silently repaired in COA-G01.

| ID | Observation | Evidence | Classification | Gate treatment |
|---|---|---|---|---|
| CF-G01-01 | 14 workbook types vs 15 l10n_th vs 19 core vs 19 target | Account Type reconciliation + AJ ruling | RECONCILED DIFFERENT EVIDENCE ROLES | CLOSED for G01; do not rewrite history |
| CF-G01-02 | Accumulated-depreciation accounts are not consistently typed in the Odoo18 table: e.g. row 71 = `Depreciation`, rows 72–73 = `Fixed Assets`, row 74 = `Depreciation`, many later accumulated-depreciation rows = `Fixed Assets` | Direct Drive workbook verification | CONFLICTING SOURCE SEMANTICS | Preserve as source fact; G03/G05 must classify by business meaning, contra-asset role and presentation |
| CF-G01-03 | Source prepayment account names (rows 32–36) are classified as `Current Assets`, while target includes active `Prepayments` capability | Direct workbook + AJ ruling | SOURCE/TARGET CLASSIFICATION DELTA | Expected transformation candidate; G03/G04 controls mapping |
| CF-G01-04 | Workbook contains tax-related concepts under generic types, including WHT, prepaid CIT, input VAT and VAT suspense | Direct workbook rows 42–46 and 388 | SOURCE CLASSIFICATION REQUIRES TH TAX SEMANTICS | G06 owns exact tax-control mapping; do not freeze from label alone |
| CF-G01-05 | Source model entry-level balance is enforced in application logic and can be bypassed; row-level DB checks do not aggregate to entry balance | Team A BR-01..03, SE-03/04/28..31 | SOURCE CONTROL RISK | Migration/ledger architecture must independently validate balance; no vendor control mechanic copied |

No unresolved conflict above prevents **source-baseline reconciliation** because each issue is explicitly classified, preserved and routed to its owning downstream Gate. None is accepted as target truth without further evidence.

---

## 7. SaaS Contamination Risk Register

| Risk | Source contamination pattern to block | G01 control | Status |
|---|---|---|---|
| CR-01 | Treat source technical ID/code/name as target identity | Provenance only; canonical identity independently owned | PASS / VERIFIED |
| CR-02 | Copy source company/tenant ownership assumptions | Every target interpretation must carry Tenant + Company context where applicable | PASS / VERIFIED |
| CR-03 | Treat one shared mutable COA record set as SaaS Standard Template | Template vs Tenant/Company Instance separation is mandatory | PASS / VERIFIED |
| CR-04 | Let tenant customization mutate published Standard Template | Explicitly prohibited | PASS / VERIFIED |
| CR-05 | Import Thailand vendor structures into SaaS Core | Thai rules belong to controlled localization semantics/profile, not copied vendor architecture | PASS / VERIFIED |
| CR-06 | Assume identical names/codes across tenants imply shared identity | Explicitly prohibited by canonical identity and isolation rules | PASS / VERIFIED |
| CR-07 | Treat source row count as target COA count | `389 != target count`; semantic consolidation required | PASS / VERIFIED |
| CR-08 | Infer financial statement mapping solely from company Account Group or mutable code | Canonical FS mapping is independent and deferred to G05 | PASS / VERIFIED |

---

## 8. SAAS INVARIANT COMPLIANCE — COA-G01

Scope note: statuses below verify **COA-G01 source-baseline compliance**. They do not claim that G04S/G07 implementation proofs are already complete.

| SI | Applicability | Evidence | Owner role | Reviewer / verifier | G01 verification | Conflict / exception | Gate impact |
|---|---|---|---|---|---|---|---|
| SI-01 Tenant context mandatory | Applicable | AO ruling; AG Template/Instance separation; this G01 matrix | Team B Architecture | ChatGPT | PASS / VERIFIED for G01 | None | No G01 block; deep architecture G04S |
| SI-02 Company context mandatory where company-scoped | Applicable | Team A company-currency/lock evidence; AG/AO rulings | Team B Architecture | ChatGPT | PASS / VERIFIED for G01 | None | No G01 block; proof G04S/G07 |
| SI-03 Standard Template is not tenant-owned mutable data | Applicable | AG/AO Boss rulings | Team B SaaS/Accounting Architecture | ChatGPT | PASS / VERIFIED guardrail | None | Deep design G04S |
| SI-04 Tenant customization cannot modify published Standard Template | Applicable | AO ruling | Team B SaaS/Accounting Architecture | ChatGPT | PASS / VERIFIED guardrail | None | Deep design G04S |
| SI-05 Account Code / Name is not canonical identity | Applicable | Team A code semantics; workbook inventory; AG/AO rulings | Team B Accounting Architecture | ChatGPT | PASS / VERIFIED | None | Required in G02/G03 mapping |
| SI-06 Published Template Version is immutable | Applicable as source-contamination guardrail | AO ruling | Team B SaaS Architecture | ChatGPT | PASS / VERIFIED for G01 guardrail | Detailed version model not yet designed | G04S required; not G01 blocker |
| SI-07 Upgrade explicit, previewable, auditable | Applicable as source-contamination guardrail | AO ruling | Team B SaaS Architecture | ChatGPT | PASS / VERIFIED for G01 guardrail | Upgrade workflow not yet designed | G04S required; not G01 blocker |
| SI-08 No cross-tenant COA access | Applicable | AO ruling; G01 source records treated only as reference/provenance | Team B SaaS Architecture | ChatGPT | PASS / VERIFIED for G01 interpretation boundary | Runtime isolation proof not yet executed | G04S/G07 required; not G01 blocker |
| SI-09 Company customization preserves canonical reporting semantics | Applicable | AG/AO rulings; canonical FS mapping independent of Account Group | Team B Accounting Architecture | ChatGPT | PASS / VERIFIED guardrail | Full proof pending | G05/G07 required; not G01 blocker |
| SI-10 SaaS Core must not hard-code Thailand-specific source architecture | Applicable | Clean-room rules; Team A read-only evidence; AG/AO rulings | Team B Architecture | ChatGPT | PASS / VERIFIED | None | Localization architecture deep proof G04S/G06 |

`COA-G01 SI-01..SI-10 unresolved applicable items = 0 for G01 scope.`

This does not provide execution credit for COA-G04S or COA-G07.

---

## 9. Controlled Carry-Forward — Not G01 Blockers

The following remain intentionally unresolved because they belong to later Gates:

| Item | Current status | Owning Gate |
|---|---|---|
| Exact Base COA Kernel count | TBD / EVIDENCE REQUIRED; `~32` is expectation only | COA-G02 |
| Account-by-account semantic consolidation | NOT STARTED | COA-G03 |
| Final canonical COA account count | TBD / EVIDENCE REQUIRED | COA-G03/G08 |
| Final Account Type canonical IDs / Account Group architecture | PARTIAL BASELINE | COA-G04 |
| Tenancy/provisioning/versioning/upgrade deep design | BOSS AUTHORIZED / NOT EXECUTED | COA-G04S |
| Exact financial-statement taxonomy and account-line mapping | NOT EXECUTED | COA-G05 |
| Exact VAT / Undue VAT / WHT / CIT / non-deductible mappings | NOT EXECUTED | COA-G06 |
| Multi-company / dimension / cross-tenant isolation proof | NOT EXECUTED | COA-G07 |
| Independent audit + PMO + Boss final COA freeze | NOT OPEN | COA-G08 |

These items must not be converted from UNKNOWN/TBD into fact before their evidence Gate.

---

## 10. Primary Thai Regulatory Anchors Used in G01

Used only to establish that the relevant Thai statutory/reporting concepts are real controlled requirements. Exact implementation and rate/account mapping remain downstream work.

1. TFAC — TAS/TFRS current standards register; TAS 1 `การนำเสนองบการเงิน`:
   https://acpro-std.tfac.or.th/standard/118/
2. Department of Business Development — official communication referencing `ประกาศกรมพัฒนาธุรกิจการค้า เรื่อง กำหนดรายการย่อที่ต้องมีในงบการเงิน พ.ศ. 2566`:
   https://magazine.dbd.go.th/letter/L67836
3. Revenue Department — VAT registered-operator obligations, including tax invoices, purchase/sales tax reports and VAT returns:
   https://www.rd.go.th/7051.html
4. Revenue Department — Withholding Tax concept and payer deduction/remittance obligation:
   https://www.rd.go.th/27862.html
5. Revenue Department — Corporate Income Tax overview for juristic companies/partnerships:
   https://www.rd.go.th/english/6044.html

Access / verification date for this Gate: 2026-08-30.

---

## 11. Gate Decision Record

### ChatGPT Independent Evidence Review

- Required G01 source layers A–H: RECONCILED.
- Direct Boss workbook source: RE-VERIFIED.
- Historical source-count differences: RECONCILED WITHOUT REWRITING FACTS.
- Source conflicts/ambiguities: EXPLICITLY REGISTERED; no silent correction.
- Clean-room boundary: PRESERVED.
- G01 SaaS Invariants SI-01..SI-10: PASS / VERIFIED at G01 responsibility level.
- G01 blocking evidence gaps: 0 identified.
- Development authorization: NOT GRANTED.
- Production authorization: NOT GRANTED.
- COA-G02 execution: NOT AUTHORIZED BY THIS REVIEW.

**Reviewer disposition:** `PASS / FORWARD TO BOSS FOR COA-G01 FINAL GATE DECISION`.

**Final Gate authority remains Boss.**

STOP HERE. Do not execute COA-G02 until Boss explicitly authorizes the next Gate.
