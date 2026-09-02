# 09 — Inventory Reporting and Analytics v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED REPORTING REQUIREMENTS — NOT APPROVED LAYOUTS, NOT APPROVED STATUTORY FORMATS`
Clean-room: Layer 1. No reference-ERP report layout, column set or dashboard structure is reproduced. Thai statutory report formats are `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.

---

## 1. Reporting Principles

| # | Principle | Consequence |
|---|---|---|
| `RP-P1` | **Facts and summaries are different artefacts and must look different.** | A movement list is never presented as if it were a report; a report always states what it summarised. |
| `RP-P2` | **Physical and forecast quantities never share a column.** | A business must never ship goods it merely expects to receive. |
| `RP-P3` | **Every as-of-date report is reproducible.** | Running it twice gives the same answer, forever. |
| `RP-P4` | **Every report that leaves the system is acceptance-tested on its export path.** | A prior benchmark lesson records a reconciliation export defective in practice. |
| `RP-P5` | **Management indicators are labelled as management indicators.** | A dashboard number must never be mistaken for an accounting or statutory figure. |
| `RP-P6` | **Every figure drills through to the movements behind it.** | An unexplainable number is not evidence. |
| `RP-P7` | **Reports are audience-shaped.** | The storekeeper, the owner, the accountant and the auditor need different artefacts, not one report with more columns. |

---

## 2. Report Catalogue

All Thai names below are `UNVALIDATED - THAI USER REVIEW REQUIRED`.

| ID | Report | Thai candidate | Audience | Class | Source menu |
|---|---|---|---|---|---|
| `R-01` | On-hand / reserved / available / forecast by product | ยอดสินค้าคงเหลือ (คงเหลือจริง / จองแล้ว / พร้อมใช้ / คาดการณ์) | Warehouse, Sales | Operational | RP-01 |
| `R-02` | Stock by storage place | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | Warehouse | Operational | RP-02 |
| `R-03` | Product movement history (stock card) | สต็อกการ์ด / ประวัติการเคลื่อนไหวสินค้า | Accountant, Auditor | **Audit — statutory format `HOLD`** | RP-03 |
| `R-04` | Movement fact ledger | รายการเคลื่อนไหวสินค้า (ระดับรายการ) | Auditor, systems investigation | Audit | RP-04 |
| `R-05` | Valuation as of date | มูลค่าสินค้าคงเหลือ ณ วันที่ | Accountant, Owner | Accounting support | RP-05 |
| `R-06` | Valuation to ledger reconciliation | กระทบยอดมูลค่าสต็อกกับบัญชี | Accountant | **Accounting support — Joint ownership** | RP-05 |
| `R-07` | Adjustment register | ทะเบียนการปรับปรุงยอดสต็อก (พร้อมเหตุผลและผู้อนุมัติ) | Owner, Auditor | Control | OP-02 |
| `R-08` | Scrap and destruction register | ทะเบียนตัดสินค้าชำรุด/ทำลาย | Accountant, Auditor | **Control — statutory evidence `HOLD`** | OP-04 |
| `R-09` | Lot / serial traceability | รายงานตามรอยล็อต/ซีเรียล (รับเข้า → จ่ายออก) | Quality, Warehouse | Traceability | PR-03 |
| `R-10` | Expiry watch list | สินค้าใกล้หมดอายุ | Warehouse, Sales | Operational | PR-03 |
| `R-11` | Replenishment proposal list | สินค้าใกล้หมด / แผนเติมสินค้า | Purchasing | Operational | OP-01 |
| `R-12` | Warehouse performance | วิเคราะห์คลังสินค้า (รับ-จ่าย-ค้างส่ง) | Owner, Manager | Management | RP-06 |
| `R-13` | Landed cost allocation statement | รายงานปันส่วนต้นทุนเพิ่มเติม | Accountant | Accounting support | OP-05 |
| `R-14` | Physical count sheet | ใบตรวจนับสินค้า | Warehouse, Auditor witness | Control | OP-02 |
| `R-15` | Open transit ageing | สินค้าระหว่างขนส่งค้างนาน | Warehouse, Owner | Control | OP-03 |
| `R-16` | Negative and zero-cost stock exceptions | รายการผิดปกติ (ยอดติดลบ / ต้นทุนเป็นศูนย์) | Owner, Accountant | Control | RP-01, RP-05 |
| `R-17` | Planning run log | บันทึกการประมวลผลอัตโนมัติ | Administrator | System | OP-06 |
| `R-18` | Reservation exceptions | รายการจองที่มีปัญหา | Warehouse, Sales | Control | OP-03 |

`R-15` through `R-18` are additions of this session, driven by the control model in file 03 §8 and the reconciliation set in file 07 §5, and are `UNVALIDATED - THAI USER REVIEW REQUIRED`.

---

## 3. Report Specifications That Carry Design Weight

### 3.1 `R-03` Stock card

| Element | Requirement |
|---|---|
| Opening | Certified opening balance, or zero with the first movement stated |
| Body | One line per done movement: date, document number, document type, counterparty, in quantity, out quantity, running balance, lot where tracked, actor |
| Closing | Balance as of the requested date |
| Reproducibility | Mandatory (`RP-P3`) |
| Export | Mandatory and acceptance-tested (`RP-P4`) |
| Drill-through | To the movement and its source document |
| **Statutory** | **Whether this artefact satisfies a Thai statutory stock-report obligation, and what columns such an obligation requires, is `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.** No statutory-sounding title is claimed by this session. |

### 3.2 `R-05` / `R-06` Valuation and reconciliation

| Element | Requirement |
|---|---|
| Header | Costing policy name and version, as-of date, company, and the scope of places included |
| Body | Value per product and per category, with quantity and unit cost shown |
| Movement of value | Opening, receipts, issues, adjustments, scrap, landed cost, manufacturing, closing |
| Reconciliation | Computed value against the ledger balance, with every reconciling item named |
| Exceptions | Negative stock, zero-cost stock and stock in non-internal places surfaced separately |
| Blocking | Cannot be finalised until the valuation-policy ownership and close design are settled (`GAP-FS-01`) |

### 3.3 `R-07` / `R-08` Control registers

Both must show, per entry: date, document, product, quantity, value, reason code, free-text reason, requester, approver, escalation path taken, and attached evidence. Both must be filterable by reason and by approver, because a concentration of adjustments under one reason or one approver is precisely the pattern an auditor looks for. `R-08` additionally carries the destruction evidence pack, whose statutory sufficiency is `HOLD / EVIDENCE REQUIRED`.

---

## 4. Dashboard Requirements

A single Inventory dashboard, audience-selected, `UNVALIDATED - THAI USER REVIEW REQUIRED` in every element:

| Audience | Panels |
|---|---|
| Warehouse supervisor | Today's inbound and outbound work queues; open backorders; put-away exceptions; open transit; expiry within horizon |
| Owner | Stock value trend; turnover and days of stock; dead-stock value; adjustment and scrap trend by reason; on-time dispatch |
| Accountant | Valuation as of last close; reconciliation status; unposted valuation facts; period guard exceptions granted |
| Administrator | Planning run status; failed scans; feature-switch change log |

Every panel states its period and its formula, and every panel outside the accountant's view is visibly labelled as management information.

---

## 5. Analytics Requirements

| ID | Analytic | Definition to be stated on the report |
|---|---|---|
| `AN-01` | Stock turnover | Cost of goods issued in the period divided by average stock value |
| `AN-02` | Days of stock | Average stock value divided by average daily cost of goods issued |
| `AN-03` | Stock ageing | Value by age band since receipt |
| `AN-04` | Dead stock | Items with no issue movement in a stated window, with their value |
| `AN-05` | Adjustment intensity | Adjustment value as a proportion of stock value, by reason and by approver |
| `AN-06` | Scrap intensity | Scrap value as a proportion of stock value, by reason |
| `AN-07` | On-time performance | Receipts and dispatches completed on or before their planned date |
| `AN-08` | Backorder ageing | Open short-supplied lines by age |
| `AN-09` | Fill rate | Ordered quantity delivered in full at first attempt |
| `AN-10` | Capacity utilisation | Occupied against defined capacity, where storage categories are configured |

All are management indicators under `RP-P5` and never accounting figures.

---

## 6. Reporting Open Items

| ID | Item | Owner | Status |
|---|---|---|---|
| `TH-HOLD-01` | Thai statutory stock-report format. | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| `TH-HOLD-02` | Statutory sufficiency of the destruction evidence pack in `R-08`. | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| `GAP-FS-01` | Valuation policy ownership and close design, blocking `R-05` and `R-06`. | Joint | Open |
| `GAP-FS-13` | Whether Thai SME owners actually want the indicator set in §5, or a smaller one. | Thai user validation | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `GAP-FS-14` | Report retention and archive policy for closed periods. | Boss / Accounting | Open |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
