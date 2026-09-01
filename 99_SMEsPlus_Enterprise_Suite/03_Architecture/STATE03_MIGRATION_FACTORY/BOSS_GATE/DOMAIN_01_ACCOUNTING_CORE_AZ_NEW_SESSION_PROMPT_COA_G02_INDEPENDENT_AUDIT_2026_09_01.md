# [SMEPLUS-26-09-01-COA-G02-AUDIT-001]
# COA-G02 Independent Audit — Base COA Kernel Discovery / L99.99

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical branch: `SMEsPlus`
Gate under review: `COA-G02 — Base COA Kernel Discovery`
Boss: Sole Final Approver

SMEsPlus is a NEW 100% Clean-room Node.js SaaS ERP.
Odoo / Salesforce / SAP Business One / legacy systems are REFERENCE / LEARNING / BENCHMARK ONLY.

Absolute controls:

- No Evidence = No Progress.
- Never Skip Gate.
- Do not convert UNKNOWN into FACT.
- Do not copy vendor source architecture, technical IDs, ORM/schema/API design, or implementation patterns into SMEsPlus target architecture.

## 2. INDEPENDENCE REQUIREMENT

Execute this review in a **fresh independent reviewer session**.

The reviewer must not be the same execution context that authored the G02 Team B evidence package.

Authority order:

`Boss Ruling > ChatGPT Independent Audit > Primary Evidence > Executor Claim`

Do not accept the Team B result merely because it is committed. Recompute and challenge it.

## 3. AUTHORITY / BASELINE TO READ FIRST

Read and verify:

1. G01 final closure record and evidence chain.
2. Boss G02 authorization:
   - commit `29eafce5bd9923d577167ecb8f9f1f63e88286df`
   - `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AY_BOSS_COA_G02_BASE_KERNEL_DISCOVERY_AUTHORIZATION_2026_09_01.md`
3. G01 Base Kernel candidate input:
   - `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`
4. Governing standard:
   - `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`
5. Account Type reconciliation:
   - `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`
6. ODOO18 source inventory and primary-source recovery evidence.
7. Team A Accounting Core evidence and business-rule registers relevant to Account Type, reconciliation, and control semantics.
8. SI-01..SI-10 cross-gate rulings.

## 4. G02 TEAM B PACKAGE TO AUDIT

Audit these four artifacts as one package:

1. `COA_G02_BASE_KERNEL_DISCOVERY_REGISTER.md`
   - commit `7bb309d9e1ef5ac0abf73dea1997296236182d49`
2. `COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md`
   - commit `d23b76226e9467b233e44c2977bcf15f6a39d505`
3. `COA_G02_SAAS_INVARIANT_COMPLIANCE.md`
   - commit `a4581d1f49ca74124ebaafa565147928a1a821a6`
4. `COA_G02_GATE_REPORT.md`
   - commit `051acf4fd3b375e977d4e65e99bf12388402a830`

Team B candidate claim to test:

`39 explicit ODOO18 default/control anchors - 9 net consolidation/extension adjustments + 6 mandatory non-anchor semantic additions = 36 Base Kernel candidates`

Do NOT target-fit the result to `~32` or accept `36` by arithmetic alone.

## 5. MANDATORY INDEPENDENT CHECKS

### A. Primary Source Integrity

Independently obtain the Boss-approved workbook if connector access permits and verify:

- filename / controlled identity;
- file size;
- SHA-256;
- ODOO18 tab identity;
- 389 non-empty data rows;
- observed Account Type distribution;
- reconcile True/False counts;
- exact count of source IDs beginning with `account.1_*`.

Known prior SHA-256 is evidence to verify, not an answer to copy:

`0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`

If primary file access fails, classify honestly as `EVIDENCE_ACCESS_BLOCKED` and determine whether the existing G01 independently verified hash chain is sufficient for G02 audit scope. Do not fabricate a fresh verification.

### B. 39-Anchor Population

Mechanically reproduce all 39 `account.1_*` rows and compare each against `COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md`.

Required result:

- missing anchor count;
- extra anchor count;
- disposition mismatch count;
- exact list of mismatches if any.

### C. Challenge the Nine Net Reductions

Independently assess whether the following are justified under the approved Base Kernel method and Do-NOT-MERGE rules:

1. `Cash Bakery` -> generic Cash on Hand.
2. Post-dated cheque -> optional extension.
3. POS receivable -> Trade Receivables / channel-specific consolidation.
4. Two accumulated-depreciation anchors -> one generic contra semantic.
5. Director short-term loan -> company-specific financing extension.
6. Dividends -> optional extension.
7. Income Summary -> optional extension rather than universal kernel.
8. Salary default -> optional extension.
9. Rent default -> optional extension.

For each, classify:

- `ACCEPT`
- `REJECT`
- `HOLD / EVIDENCE_REQUIRED`

and cite evidence/reason.

### D. Challenge the Six Mandatory Additions

Independently test whether each is genuinely required in the universal Thailand Base Kernel:

1. Gross Fixed Assets.
2. Depreciation Expense.
3. Undue Input VAT.
4. Prepaid CIT.
5. Undue Output VAT.
6. CIT Payable.

Do not add an item merely because it appears in a source COA. Require a business/control/statutory reason that meets G02's approved inclusion test.

### E. Review All 36 Candidate Concepts

For every K01..K36, verify:

- business purpose;
- Account Type candidate or controlled deferral;
- source anchor;
- Thailand relevance;
- reason the concept cannot safely be only a dimension/source attribute/company extension;
- compliance with Do-NOT-MERGE rules.

Flag any candidate that is actually optional, over-specific, source-vendor-driven, or belongs to a later Gate rather than the Base Kernel.

### F. Specific High-Risk Review Points

Pay special attention to:

1. **K14 Accumulated Depreciation** — source Account Type classifications are inconsistent. Confirm that deferring final contra/type rule to G04 is valid and that G02 does not silently settle the conflict.
2. **K26 WHT Payable** — confirm G02 has not improperly merged PND1/2/3/53/54 statutory facts into one final GL rule. Form-level treatment belongs to G06 unless G02 evidence proves otherwise.
3. **K20 General Operating Expense** — test whether excluding salary/rent from universal kernel while retaining a general operating expense is evidence-supported and does not erase materially different Thai tax/WHT treatment.
4. **K18 Current Year Earnings / Income Summary exclusion** — test whether a separate Income Summary control account is actually required by the evidenced accounting behavior.
5. **K13/K14/K15 fixed asset trio** — test gross asset, contra asset, and depreciation expense separation against the Do-NOT-MERGE rules.
6. **VAT timing accounts** — test due vs undue input/output VAT separation.
7. **CIT trio** — test Prepaid CIT, CIT Payable, CIT Expense as distinct accounting positions.

### G. Account Type and SaaS Controls

Verify:

- Boss 19 ACTIVE Account Types remain unchanged.
- G02 does not falsely require one kernel account per active type.
- Account Code/Name/source technical IDs are provenance only, not canonical identity.
- SI-01..SI-10 are correctly assessed at G02 classification/discovery scope.
- Runtime provisioning/versioning/isolation evidence is not falsely claimed as G02 proof.

### H. Scope / Gate Integrity

Confirm that the package did NOT:

- start COA-G03 semantic consolidation of the entire source population;
- freeze the final Standard Thai COA;
- design database/API/ORM/schema;
- grant Development or Production authorization;
- copy Odoo architecture;
- silently use the ODOO19 tab as the G02 derivation population.

## 6. REQUIRED AUDIT OUTPUT

Create a dedicated independent-audit artifact under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/CHATGPT_AUDIT/`

Recommended name:

`DOMAIN_01_ACCOUNTING_CORE_COA_G02_INDEPENDENT_AUDIT_2026_09_01.md`

The audit must contain:

1. evidence read list;
2. primary-source integrity result;
3. 39-anchor mechanical reconciliation;
4. reduction decision matrix (9 items);
5. addition decision matrix (6 items);
6. K01..K36 verification matrix;
7. SI-01..SI-10 matrix;
8. open findings with IDs `G02-AUD-01...`;
9. exact terminal disposition.

Allowed terminal dispositions:

- `PASS / VERIFIED — READY FOR PMO VERIFICATION`
- `HOLD / CORRECTION REQUIRED`
- `FAIL / FROZEN`

Do not invent another status.

## 7. EXIT ROUTING

If and only if audit disposition = `PASS / VERIFIED — READY FOR PMO VERIFICATION`:

- route the exact audited commit/evidence chain to PMO;
- do not self-declare PMO PASS;
- do not start G03.

If HOLD/FAIL:

- produce a precise correction register;
- preserve all evidence;
- return to Team B only for the named defects;
- do not broaden scope.

## 8. PROGRESS REPORTING

Report `% Board`, `% STATE`, `% STEP` only if an approved evidence-weighted denominator exists.

Otherwise report exactly:

- `% Board = TBD / NO APPROVED BASELINE`
- `% STATE = TBD / NO APPROVED BASELINE`
- `% STEP = TBD / NO APPROVED BASELINE`

No guessed percentages.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
