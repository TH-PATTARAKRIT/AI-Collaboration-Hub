# COA-G02 — Base COA Kernel Discovery Register

Date: 2026-09-01
Gate: `COA-G02 — Base COA Kernel Discovery`
Authority: Boss authorization `DOMAIN_01_ACCOUNTING_CORE_AY_BOSS_COA_G02_BASE_KERNEL_DISCOVERY_AUTHORIZATION_2026_09_01.md`
Status: **TEAM B / CONTROLLED DISCOVERY RESULT — READY FOR INDEPENDENT AUDIT; NOT YET BOSS-FROZEN**

## 1. Objective

Identify the **smallest defensible Thailand Base COA Kernel** from the G01-closed evidence baseline without forcing `32`, copying `389` source rows, or starting COA-G03 semantic consolidation.

The result of this pass is an evidence-backed **36-account semantic Base Kernel candidate**.

`36` is derived mechanically from evidence; it is **not** selected to match the historical `~32` working expectation.

## 2. Evidence Baseline Used

1. `COA-G01 = APPROVED / PASS / CLOSED`.
2. `COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`.
3. `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`.
4. `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`.
5. Boss-approved workbook `Account_Odoo18_19 sent 270369.xlsx`, **ODOO18 tab only for row-level derivation in this Gate**.
6. G01-closed direct-source evidence: core Account Type universe = 19; inspected `l10n_th` source = 144 rows / 15 instantiated types; Boss target = 19 ACTIVE Account Types.
7. Team A Accounting Core evidence including `SE-17`, `SE-18`, `SE-20` and the business-rule register.
8. SI-01..SI-10 cross-gate controls.

### Primary workbook re-verification in this execution

- Drive file ID: controlled source already recorded by G01.
- File size: `307308` bytes.
- SHA-256 independently recomputed: `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`.
- Exact match to `COA_G01_PRIMARY_SOURCE_RECOVERY_REGISTER_R4.md`.
- ODOO18: 389 non-empty data rows; 14 observed Account Type labels; 33 reconcile=True / 356 False — unchanged from G01.

**Scope control:** the workbook also contains an `ODOO19` tab. It is **not used to derive the G02 count** because the G01 authority surface designated the ODOO18 tab plus separately verified `l10n_th` source evidence. This avoids silently substituting a different source population.

## 3. Mechanical Derivation

### 3.1 Source-linked starting population

The ODOO18 tab contains **39 rows whose source IDs are explicit `account.1_*` default/control anchors**. These are treated as a high-signal starting population, not as an automatic target list.

### 3.2 Controlled reductions from 39 to 30

Nine net rows are removed from the kernel starting population by evidence-backed consolidation or extension treatment:

1. `Cash Bakery` -> duplicate/company-specific cash-journal default; kernel retains generic Cash on Hand. `-1`
2. Post-dated cheque -> payment-instrument extension; no evidence it is mandatory for every tenant/company. `-1`
3. POS receivable -> channel-specific receivable; kernel retains generic Trade Receivables under dimension/subledger principle. `-1`
4. Two accumulated-depreciation default anchors -> one generic contra-asset semantic kernel concept. `-1`
5. Short-term loan — director -> company-specific financing extension. `-1`
6. Dividends -> optional distribution/equity extension, not a universal posting dependency. `-1`
7. Income Summary -> not retained as a separate universal kernel account because Current Year Earnings / retained-earnings controls already provide the evidenced year-end control surface; no hard dependency on a separate income-summary account was evidenced. `-1`
8. Salary and Rent default-expense rows -> not universal kernel accounts; they remain company/template extensions because their business/tax treatment can differ. General Office/Operating Expense is retained as the default expense kernel. `-2`

Thus: `39 - 9 = 30` source-linked kernel concepts.

### 3.3 Mandatory semantic additions from non-`account.1_*` source rows

Six additional concepts are required by the approved G02 method even though their ODOO18 rows are not explicit `account.1_*` anchors:

1. Gross Fixed Assets — required to pair with contra/depreciation accounting.
2. Depreciation Expense — required to complete fixed-asset depreciation semantics.
3. Undue Input VAT — Thailand VAT timing/control distinction.
4. Prepaid CIT — Thailand corporate-income-tax asset position.
5. Undue Output VAT — Thailand VAT timing/control distinction.
6. CIT Payable — Thailand corporate-income-tax liability position.

Thus: `30 + 6 = 36`.

## 4. Evidence-Backed Base Kernel Candidate — 36 Concepts

| ID | Canonical business purpose | Account Type candidate | ODOO18 evidence anchor(s) | Why kernel / why not dimension-only |
|---|---|---|---|---|
| K01 | Cash on Hand | Bank and Cash | row 1 `เงินสด` | Physical cash control; distinct journal/liquidity behavior |
| K02 | Bank Deposit | Bank and Cash | row 5 `เงินฝากกระแสรายวัน` | Bank-journal settlement; not an analytical dimension |
| K03 | Bank Suspense | Current Assets | row 4 `Bank Suspense Account` | Unmatched bank control state |
| K04 | Liquidity Transfer | Current Assets | row 380 `Liquidity Transfer` | Inter-journal transfer clearing; system-control semantic |
| K05 | Outstanding Receipts | Current Assets | row 386 `ใบเสร็จรับเงินค้างชำระ` | Receipt clearing before bank settlement |
| K06 | Outstanding Payments | Current Assets | row 387 `การชำระเงินค้างชำระ` | Payment clearing before bank settlement |
| K07 | Trade Receivables | Receivable | row 11 `ลูกหนี้การค้า` | AR control/reconciliation semantic |
| K08 | Trade Payables | Payable | row 85 `เจ้าหนี้การค้า` | AP control/reconciliation semantic |
| K09 | Accrued Expenses | Current Liabilities | row 167 `ค่าใช้จ่ายค้างจ่าย` | Accrual recognition/control semantic |
| K10 | Inventory | Current Assets | row 25 `สินค้าคงเหลือ - สำเร็จรูป` | Inventory valuation balance |
| K11 | Uninvoiced Receipts / GRNI | Current Liabilities | row 95 `Uninvoiced Receipts` | Inventory receipt/invoice timing control |
| K12 | Cost of Goods Sold | Cost of Revenue | row 196 `ต้นทุนสินค้าเพื่อขาย - สินค้าสำเร็จรูป` | Inventory-to-P&L cost recognition |
| K13 | Fixed Assets | Fixed Assets | representative row 56 `อาคารสำนักงาน` | Gross fixed-asset recognition |
| K14 | Accumulated Depreciation | **Contra fixed-asset semantic; final Account Type rule deferred to G04** | rows 71, 74 accumulated-depreciation anchors | Contra-asset role cannot be merged with gross asset or depreciation expense; G01 source-type inconsistency is preserved, not silently rewritten |
| K15 | Depreciation Expense | Depreciation | representative row 297 `ค่าเสื่อมราคา - อาคารสำนักงาน` | P&L depreciation recognition distinct from K14 |
| K16 | Share Capital | Equity | row 173 `หุ้นสามัญ` | Core legal/equity capital semantic |
| K17 | Retained Earnings | Equity | row 174 `กำไรสะสม` | Prior-period accumulated equity |
| K18 | Current Year Earnings | Current Year Earnings | row 385 `Undistributed Profits/Losses` | Year-end/current-year earnings control |
| K19 | Operating Revenue | Income | row 177 `รายได้จากการขาย` | Default operating-income posting target; channel/customer/product remain dimensions/extensions |
| K20 | General Operating Expense | Expenses | row 207 `ค่าใช้จ่ายสำนักงานทั่วไป` (salary/rent defaults excluded as non-universal extensions) | Default operating-expense target without forcing company-specific expense taxonomy |
| K21 | Interest Expense / Finance Cost | Expenses | row 316 `ดอกเบี้ยจ่าย` | Finance-cost presentation/treatment distinct from operating expense |
| K22 | WHT Creditable | Current Assets | row 42 `ภาษีถูกหัก ณ ที่จ่าย` | Thai withholding-tax credit asset |
| K23 | Input VAT | Current Assets | row 44 `ภาษีซื้อ` | Thai VAT input tax control |
| K24 | Undue Input VAT | Current Assets | row 45 `ภาษีซื้อรอขอคืน / รอใบกำกับภาษี` | Thai VAT timing status differs materially from due input VAT |
| K25 | Prepaid CIT | Current Assets | row 43 `ภาษีนิติบุคคลจ่ายล่วงหน้า` | Thai CIT prepaid/credit asset |
| K26 | WHT Payable control | Current Liabilities | rows 154-158 PND1/2/3/53/54 source liabilities; row 157 is explicit default anchor | Kernel retains the WHT-payable control semantic. **No G02 claim that all PND forms must merge into one final GL**; form-level statutory granularity is reserved for G06 |
| K27 | Output VAT | Current Liabilities | row 160 `ภาษีขาย` | Thai VAT output tax control |
| K28 | Undue Output VAT | Current Liabilities | row 161 `ภาษีขาย-รอเรียกเก็บ` | Thai VAT timing status differs materially from due output VAT |
| K29 | CIT Payable | Current Liabilities | row 159 `ภาษีเงินได้นิติบุคคลค้างจ่าย` | Thai CIT liability |
| K30 | CIT Expense | Expenses | rows 315/320 income-tax expense source rows | P&L corporate-income-tax recognition |
| K31 | FX Gain | Other Income | row 178 `กำไรจากการแลกเปลี่ยน` | Monetary-item exchange treatment |
| K32 | FX Loss | Expenses | row 319 `ขาดทุนจากการแลกเปลี่ยน` | Monetary-item exchange treatment; distinct sign/presentation from K31 |
| K33 | Cash Difference Gain | Other Income | row 381 `Cash Difference Gain` | Cash-control generated gain |
| K34 | Cash Difference Loss | Expenses | row 382 `Cash Difference Loss` | Cash-control generated loss |
| K35 | Early Payment Discount Gain | Other Income | row 383 `Cash Discount Gain` | Journal/payment control-generated gain |
| K36 | Early Payment Discount Loss | Expenses | row 384 `Cash Discount Loss` | Journal/payment control-generated loss |

## 5. Why the Result Is 36, Not 32

The historical `~32` figure was explicitly a working expectation only. The evidence-driven pass produces four additional defensible kernel concepts because Thailand VAT/CIT timing and fixed-asset/depreciation semantics cannot be removed merely to hit a target number.

No account is added solely to increase the count and no account is removed solely to reduce it.

## 6. Account-Type Coverage Boundary

The Base Kernel does **not** need to instantiate one account under every one of the 19 ACTIVE Account Types. `19 ACTIVE` is a capability/taxonomy ruling, not a mandate that the default kernel contain at least one account of every type.

Types such as Prepayments, Credit Card, Non-current Liabilities, Other Expenses and Off-Balance Sheet can remain active for tenant/company extensions even when no universal Base Kernel account is proven for them at G02.

## 7. Explicit Non-Claims / Later-Gate Dependencies

1. This is **not** the final Standard Thai COA.
2. Account codes/names are not canonical identity.
3. K14 final Account Type/contra-asset rule belongs to `COA-G04`.
4. WHT form-specific statutory granularity belongs to `COA-G06`; G02 does not collapse legally distinct tax reporting facts.
5. Financial-statement taxonomy belongs to `COA-G05`.
6. Tenant/company provisioning/versioning remains `COA-G04S`.
7. No database/schema/API/implementation design is created here.
8. COA-G03 is not started by this artifact.

## 8. Team B G02 Result

`BASE COA KERNEL CANDIDATE COUNT = 36`

`TEAM B DISCOVERY RESULT = READY FOR CHATGPT INDEPENDENT AUDIT`

This is **not yet** `G02 PASS/CLOSED` and not a Boss freeze.

No Evidence = No Progress. Never Skip Gate.
