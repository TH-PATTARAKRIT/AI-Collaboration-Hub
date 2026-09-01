# COA-G02 — ODOO18 Default/Control Anchor Disposition Register

Date: 2026-09-01
Purpose: provide a complete disposition of every ODOO18 source row whose source ID begins with `account.1_*`.

Primary source: Boss-approved `Account_Odoo18_19 sent 270369.xlsx`, ODOO18 tab, SHA-256 `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`.

Observed explicit default/control-anchor population = **39 rows**.

| Source row | Source observation | G02 disposition | Kernel target / reason |
|---:|---|---|---|
| 0 | `Cash Bakery` | MERGE / SOURCE-SPECIFIC | K01 Cash on Hand; source-company/journal-specific duplicate |
| 1 | `เงินสด` | BASE_KERNEL | K01 Cash on Hand |
| 4 | `Bank Suspense Account` | BASE_KERNEL | K03 Bank Suspense |
| 5 | `เงินฝากกระแสรายวัน` | BASE_KERNEL | K02 Bank Deposit |
| 11 | `ลูกหนี้การค้า` | BASE_KERNEL | K07 Trade Receivables |
| 21 | `เช็ครับลงวันที่ล่วงหน้า` | OPTIONAL EXTENSION | Payment-instrument-specific; no universal dependency evidenced |
| 24 | `ลูกหนี้การค้า (PoS)` | MERGE / CHANNEL-SPECIFIC | K07 Trade Receivables; POS identity is operational/channel context |
| 25 | `สินค้าคงเหลือ - สำเร็จรูป` | BASE_KERNEL | K10 Inventory |
| 42 | `ภาษีถูกหัก ณ ที่จ่าย` | BASE_KERNEL | K22 WHT Creditable |
| 44 | `ภาษีซื้อ` | BASE_KERNEL | K23 Input VAT |
| 71 | `ค่าเสื่อมราคาสะสม - อาคารสำนักงาน` | BASE_KERNEL / CONSOLIDATE BY CONTRA ROLE | K14 Accumulated Depreciation |
| 74 | `ค่าเสื่อมราคาสะสม - อุปกรณ์สำนักงาน` | MERGE BY CONTRA ROLE | K14 Accumulated Depreciation; asset-class detail can extend later |
| 85 | `เจ้าหนี้การค้า` | BASE_KERNEL | K08 Trade Payables |
| 91 | `เงินกู้ยืมระยะสั้น - กรรมการ` | OPTIONAL EXTENSION | Company-specific financing; not universal |
| 95 | `Uninvoiced Receipts` | BASE_KERNEL | K11 GRNI / Uninvoiced Receipts |
| 157 | `ภาษีหัก ณ ที่จ่ายค้างจ่าย ภงด.53` | BASE_KERNEL CONTROL SEMANTIC | K26 WHT Payable; no claim that G06 statutory form granularity is merged |
| 160 | `ภาษีขาย` | BASE_KERNEL | K27 Output VAT |
| 167 | `ค่าใช้จ่ายค้างจ่าย` | BASE_KERNEL | K09 Accrued Expenses |
| 173 | `หุ้นสามัญ` | BASE_KERNEL | K16 Share Capital |
| 174 | `กำไรสะสม` | BASE_KERNEL | K17 Retained Earnings |
| 175 | `เงินปันผล` | OPTIONAL EXTENSION | Distribution account; not required for every entity/period |
| 176 | `สรุปรายได้` | OPTIONAL EXTENSION | No separate hard dependency evidenced beyond Current Year Earnings / retained-earnings control |
| 177 | `รายได้จากการขาย` | BASE_KERNEL | K19 Operating Revenue |
| 178 | `กำไรจากการแลกเปลี่ยน` | BASE_KERNEL | K31 FX Gain |
| 196 | `ต้นทุนสินค้าเพื่อขาย - สินค้าสำเร็จรูป` | BASE_KERNEL | K12 Cost of Goods Sold |
| 205 | `เงินเดือนทั่วไป` | OPTIONAL EXTENSION | Personnel-cost taxonomy can differ materially by company/tax treatment |
| 206 | `ค่าเช่าทั่วไป` | OPTIONAL EXTENSION | Rent has distinct business/WHT treatment; not merged into kernel by name similarity |
| 207 | `ค่าใช้จ่ายสำนักงานทั่วไป` | BASE_KERNEL | K20 General Operating Expense default |
| 315 | `Income tax expenses` | BASE_KERNEL | K30 CIT Expense |
| 316 | `ดอกเบี้ยจ่าย` | BASE_KERNEL | K21 Interest Expense / Finance Cost |
| 319 | `ขาดทุนจากการแลกเปลี่ยน` | BASE_KERNEL | K32 FX Loss |
| 380 | `Liquidity Transfer` | BASE_KERNEL | K04 Liquidity Transfer |
| 381 | `Cash Difference Gain` | BASE_KERNEL | K33 Cash Difference Gain |
| 382 | `Cash Difference Loss` | BASE_KERNEL | K34 Cash Difference Loss |
| 383 | `Cash Discount Gain` | BASE_KERNEL | K35 Early Payment Discount Gain |
| 384 | `Cash Discount Loss` | BASE_KERNEL | K36 Early Payment Discount Loss |
| 385 | `Undistributed Profits/Losses` | BASE_KERNEL | K18 Current Year Earnings |
| 386 | `ใบเสร็จรับเงินค้างชำระ` | BASE_KERNEL | K05 Outstanding Receipts |
| 387 | `การชำระเงินค้างชำระ` | BASE_KERNEL | K06 Outstanding Payments |

## Reconciliation

- Explicit source anchors: `39`.
- Net consolidation/exclusion reduction: `9`.
- Source-linked kernel concepts after disposition: `30`.
- Mandatory non-anchor semantic additions required by G02 method: `6` (K13, K15, K24, K25, K28, K29).
- G02 Base Kernel candidate: **36**.

## Boundary

`OPTIONAL EXTENSION` does not mean prohibited. It means the source observation is not proven to be required in the universal Thailand Base Kernel. Tenant/company templates may add it later under controlled gates.

No source technical ID is reused as SMEsPlus canonical identity.
