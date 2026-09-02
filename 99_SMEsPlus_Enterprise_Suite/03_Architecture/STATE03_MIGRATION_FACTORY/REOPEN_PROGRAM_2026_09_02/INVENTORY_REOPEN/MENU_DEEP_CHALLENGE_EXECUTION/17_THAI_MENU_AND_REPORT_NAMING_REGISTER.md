# 17 — Thai Menu and Report Naming Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-08 OUTPUT — THAI NAMING CANDIDATES — NOT APPROVED UI LABELS`
Clean-room boundary: benchmark labels are the input column only. Thai candidates are new SMEsPlus business-language proposals. Boss and Team B (when authorized) decide final labels. Real Thai user validation has never been performed for any Inventory label (Reopen `02` item 39); every row below is therefore `UNVALIDATED BY REAL THAI USERS`.

---

## 1. Naming Principles Applied

| Principle | Rule |
|---|---|
| P1 — Speak like a Thai storekeeper, not like an ERP | Prefer verbs Thai warehouse staff already use: รับเข้า, จ่ายออก, โอนย้าย, นับสต็อก, ตัดสินค้าเสีย. |
| P2 — Separate facts from summaries | รายการ… = movement fact list; รายงาน… / ยอด… = summary or report. |
| P3 — Separate manual action from automatic planning | เติมสินค้า (person acts) vs แผนเติมสินค้า / ระบบวางแผน (system proposes). |
| P4 — Make control visible | Adjustments, scrap and valuation names must carry the word that signals approval or accounting impact (ปรับปรุง, ตัด, มูลค่า). |
| P5 — Auditor and accountant readability | Reports that feed accounting or the Revenue Department use accounting vocabulary (มูลค่าสินค้าคงเหลือ, สต็อกการ์ด / รายงานสินค้าและวัตถุดิบ). |
| P6 — Hide engineering vocabulary | "Rules", "Routes", "Scheduler", "Nomenclature" are not Thai SME words; either wrap them in a business phrase or hide them under a template. |
| P7 — Do not transliterate the benchmark | No Thai label may be a transliteration of the benchmark label (for example "รีเพลนิชเมนต์"). |

---

## 2. Menu Naming Register

| ID | Menu ID | Benchmark term | Thai candidate name (primary) | Thai alternates | Short label (mobile / button) | Naming note | Validation status |
|---|---|---|---|---|---|---|---|
| TH-01 | MENU-OP-01 | Replenishment | เติมสินค้า / แผนเติมสินค้า | รายการที่ต้องสั่งเติม, สินค้าใกล้หมด | เติมสินค้า | Must distinguish manual replenishment (คนสั่ง) from automatic planning (ระบบเสนอ). Recommend two sub-views: "สินค้าใกล้หมด" (what to order) and "แผนเติมสินค้า" (proposed orders awaiting approval). | UNVALIDATED |
| TH-02 | MENU-OP-02 | Inventory Adjustments | ปรับปรุงยอดสต็อก | นับสต็อก / ตรวจนับสินค้า (count sub-flow), ปรับยอดสินค้า | ปรับสต็อก | Must show approval and reason control. Recommend count (นับสต็อก) as the entry point and ปรับปรุงยอดสต็อก as the approved result; reason code label: เหตุผลการปรับ. | UNVALIDATED |
| TH-03 | MENU-OP-03 | Transfers | รายการเคลื่อนย้ายสินค้า (umbrella) | รับสินค้าเข้า (receipt), จ่ายสินค้าออก / ส่งสินค้า (delivery), โอนย้ายภายใน (internal), รับคืน / ส่งคืน (returns) | รับเข้า / จ่ายออก / โอนย้าย | Must support warehouse/location/source/destination. Thai users do not search for one "Transfers" list; recommend three first-level entries and one umbrella search. | UNVALIDATED |
| TH-04 | MENU-OP-04 | Scrap | ตัดสินค้าชำรุด/สูญเสีย | ตัดสินค้าเสีย, ทำลายสินค้า (destruction with witness) | ตัดของเสีย | Must connect to control and accounting impact. Recommend a reason axis: ชำรุด / หมดอายุ / สูญหาย / ทำลายตามระเบียบภาษี. | UNVALIDATED |
| TH-05 | MENU-OP-05 | Landed Costs | ต้นทุนสินค้าเพิ่มเติม | ต้นทุนนำเข้า, ค่าใช้จ่ายรวมเข้าต้นทุนสินค้า | ต้นทุนเพิ่ม | Must connect to inventory valuation and Accounting handoff; label must signal that the value of stock changes. | UNVALIDATED |
| TH-06 | MENU-OP-06 | Run Scheduler | ประมวลผลแผนสต็อก | ให้ระบบวางแผนตอนนี้, บันทึกการประมวลผลอัตโนมัติ (log) | ประมวลผล | Must explain automatic procurement/replenishment trigger. Recommend not a user menu; show as "สถานะการประมวลผลอัตโนมัติ" in admin settings with last-run time and result. | UNVALIDATED |
| TH-07 | MENU-PR-01 | Products | สินค้า | ข้อมูลสินค้า, ทะเบียนสินค้า | สินค้า | Product master must show product type in Thai: สินค้าคงคลัง / วัสดุสิ้นเปลือง / บริการ (candidate for stockable / consumable / service; see 09). | UNVALIDATED |
| TH-08 | MENU-PR-02 | Product Variants | สินค้าย่อย | ตัวเลือกสินค้า, รุ่นย่อย (สี/ไซซ์) | สินค้าย่อย | Must make clear that stock is counted per variant, not per parent. | UNVALIDATED |
| TH-09 | MENU-PR-03 | Lots/Serial Numbers | เลขล็อต / เลขซีเรียล | ล็อตการผลิต, หมายเลขเครื่อง, วันหมดอายุ (expiry attribute) | ล็อต/ซีเรียล | Must fit traceability, warranty, expiry, recall. Recommend showing วันหมดอายุ and สถานะประกัน as columns. | UNVALIDATED |
| TH-10 | MENU-RP-01 | Stock (report) | ยอดสินค้าคงเหลือ | สต็อกคงเหลือ, สินค้าคงเหลือปัจจุบัน | ยอดคงเหลือ | Must show three quantities in Thai: คงเหลือจริง (on hand), จองแล้ว (reserved), พร้อมใช้ (available). | UNVALIDATED |
| TH-11 | MENU-RP-02 | Locations (report) | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | ยอดคงเหลือรายคลัง/รายชั้นวาง | คงเหลือตามที่เก็บ | Only visible when multi-location is enabled. | UNVALIDATED |
| TH-12 | MENU-RP-03 | Moves History | ประวัติการเคลื่อนไหวสินค้า | สต็อกการ์ด, รายงานสินค้าและวัตถุดิบ (statutory-style name, evidence required) | สต็อกการ์ด | Must distinguish movement facts from summary reports; this is the per-product running history Thai accountants call สต็อกการ์ด. | UNVALIDATED |
| TH-13 | MENU-RP-04 | Stock Moves | รายการเคลื่อนไหวสินค้า | รายการเคลื่อนย้ายทั้งหมด (technical ledger) | รายการเคลื่อนไหว | Fact-level ledger; recommend advanced/audit visibility only. | UNVALIDATED |
| TH-14 | MENU-RP-05 | Valuation | มูลค่าสินค้าคงเหลือ | รายงานมูลค่าสต็อก, มูลค่าสินค้าคงเหลือตามนโยบายต้นทุน | มูลค่าสต็อก | Must connect to accounting and costing policy; label must show the valuation date (ณ วันที่). | UNVALIDATED |
| TH-15 | MENU-RP-06 | Warehouse Analysis | วิเคราะห์คลังสินค้า | ภาพรวมคลังสินค้า, แดชบอร์ดคลังสินค้า | วิเคราะห์คลัง | Management view; must not be confused with audit reports. | UNVALIDATED |
| TH-16 | MENU-CF-01 | Settings | ตั้งค่าระบบคลังสินค้า | การตั้งค่าคลังสินค้า | ตั้งค่า | Feature switches must be worded as business options (เปิดใช้ล็อต/ซีเรียล, เปิดใช้หลายตำแหน่งจัดเก็บ). | UNVALIDATED |
| TH-17 | MENU-CF-02 | Warehouses | คลังสินค้า | สาขา/คลัง (only if branch = warehouse in that tenant) | คลัง | Must not be silently equated with Thai tax branch (สาขา) — `GRPA-H8` precision note. | UNVALIDATED |
| TH-18 | MENU-CF-03 | Locations | ตำแหน่งจัดเก็บ | ที่เก็บสินค้า, ชั้นวาง/โซน | ตำแหน่ง | System locations (เช่น สินค้าระหว่างรับ) need plain Thai explanations. | UNVALIDATED |
| TH-19 | MENU-CF-04 | Routes | เส้นทางการไหลของสินค้า | ขั้นตอนรับ-จ่ายสินค้า (1 ขั้น / 2 ขั้น / 3 ขั้น), รูปแบบการจัดส่ง | เส้นทางสินค้า | Hide under templates: "รับสินค้า 1 ขั้นตอน", "รับแล้วตรวจคุณภาพก่อนเก็บ". | UNVALIDATED |
| TH-20 | MENU-CF-05 | Rules | กฎการไหลของสินค้า | เงื่อนไขการเคลื่อนย้ายอัตโนมัติ | กฎสินค้า | Advanced only; Thai SMEs should not need to edit rules directly. | UNVALIDATED |
| TH-21 | MENU-CF-06 | Operations Types | ประเภทรายการคลัง | ประเภทเอกสารคลัง (รับเข้า / จ่ายออก / โอนภายใน / ผลิต) | ประเภทรายการ | Document numbering prefix in Thai practice (ใบรับสินค้า RC-, ใบจ่ายสินค้า DO-, ใบโอน TR-) belongs here. | UNVALIDATED |
| TH-22 | MENU-CF-07 | Storage Categories | ประเภทพื้นที่จัดเก็บ | ประเภทที่เก็บ (เย็น/แห้ง/อันตราย), ความจุพื้นที่ | ประเภทที่เก็บ | Needed only for capacity or condition constrained warehouses. | UNVALIDATED |
| TH-23 | MENU-CF-08 | Putaway Rules | กฎจัดเก็บสินค้าเข้าที่ | กำหนดที่เก็บอัตโนมัติ | จัดเก็บเข้าที่ | Must be understandable to warehouse users: "สินค้านี้รับเข้าแล้วให้ไปเก็บที่ไหน". | UNVALIDATED |
| TH-24 | MENU-CF-09 | Product Categories | หมวดหมู่สินค้า | กลุ่มสินค้า, หมวดสินค้า (นโยบายต้นทุน) | หมวดสินค้า | If category owns valuation policy, the label must say so: หมวดหมู่สินค้าและนโยบายต้นทุน. | UNVALIDATED |
| TH-25 | MENU-CF-10 | Attributes | คุณลักษณะสินค้า | ตัวเลือก (สี, ขนาด), คุณสมบัติสินค้า | คุณลักษณะ | Pairs with สินค้าย่อย. | UNVALIDATED |
| TH-26 | MENU-CF-11 | Product Packagings | หน่วยบรรจุ / แพ็กสินค้า | ขนาดบรรจุ (ลัง 12 ชิ้น), หน่วยขายเป็นแพ็ก | หน่วยบรรจุ | Must not be confused with UoM: หน่วยบรรจุ is "how it is packed", หน่วยนับ is "how it is counted". | UNVALIDATED |
| TH-27 | MENU-CF-12 | Reordering Rules | จุดสั่งซื้อ / กฎสั่งเติมสินค้า | ยอดต่ำสุด-สูงสุด (min-max), ตั้งค่าสินค้าใกล้หมด | จุดสั่งซื้อ | Thai SMEs understand จุดสั่งซื้อ and ยอดต่ำสุด/สูงสุด better than "reordering rule". | UNVALIDATED |
| TH-28 | MENU-CF-13 | Barcode Nomenclatures | รูปแบบบาร์โค้ด | มาตรฐานบาร์โค้ด (EAN-13 / GS1 / ภายใน) | บาร์โค้ด | Word "nomenclature" has no Thai SME equivalent; use รูปแบบ. | UNVALIDATED |
| TH-29 | MENU-CF-14 | UoM Categories | กลุ่มหน่วยนับ | หน่วยนับและอัตราแปลง (ชิ้น / โหล / กล่อง / ลัง / กก.) | หน่วยนับ | Must show conversion in plain Thai: 1 โหล = 12 ชิ้น. | UNVALIDATED |

---

## 3. Report Naming Register (reports split by audience, see 16)

| ID | Report candidate | Thai candidate name | Audience | Note |
|---|---|---|---|---|
| TH-R01 | On-hand / reserved / available by product | ยอดสินค้าคงเหลือ (คงเหลือจริง / จองแล้ว / พร้อมใช้) | Warehouse, Sales | Operational |
| TH-R02 | Stock by location | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | Warehouse | Operational |
| TH-R03 | Product movement history (stock card) | สต็อกการ์ด / ประวัติการเคลื่อนไหวสินค้า | Accountant, Auditor, Revenue Department (statutory format `HOLD`) | Audit |
| TH-R04 | Movement fact ledger | รายการเคลื่อนไหวสินค้า (ระดับรายการ) | Auditor, IT | Audit |
| TH-R05 | Inventory valuation as of date | มูลค่าสินค้าคงเหลือ ณ วันที่ | Accountant, Management | Accounting support |
| TH-R06 | Valuation vs GL reconciliation | กระทบยอดมูลค่าสต็อกกับบัญชี | Accountant | Accounting support (Joint Session ownership) |
| TH-R07 | Adjustment register | ทะเบียนการปรับปรุงยอดสต็อก (พร้อมเหตุผลและผู้อนุมัติ) | Management, Auditor | Control |
| TH-R08 | Scrap / destruction register | ทะเบียนตัดสินค้าชำรุด/ทำลาย | Accountant, Auditor, Tax | Control (statutory destruction evidence `HOLD`) |
| TH-R09 | Lot / serial traceability | รายงานตามรอยล็อต/ซีเรียล (รับเข้า → จ่ายออก) | QA, Warehouse | Traceability |
| TH-R10 | Expiry watch list | สินค้าใกล้หมดอายุ | Warehouse, Sales | Operational |
| TH-R11 | Reorder proposal list | สินค้าใกล้หมด / แผนเติมสินค้า | Purchasing | Operational |
| TH-R12 | Warehouse performance | วิเคราะห์คลังสินค้า (รับ-จ่าย-ค้างส่ง) | Management | Management |
| TH-R13 | Landed cost allocation statement | รายงานปันส่วนต้นทุนเพิ่มเติม | Accountant | Accounting support |
| TH-R14 | Physical count sheet | ใบตรวจนับสินค้า | Warehouse, Auditor witness | Control |

---

## 4. Naming Conflicts and Notes for Boss

| # | Issue | Recommendation |
|---|---|---|
| N-1 | "Transfers" as one umbrella hides the three documents Thai staff actually use (รับเข้า / จ่ายออก / โอนย้าย). | Keep the umbrella for search; expose three first-level entries. |
| N-2 | "Warehouse" (คลัง) vs Thai tax branch (สาขา) can be confused; the reopen chain already carries `GRPA-H8/H3` on two branch concepts. | Never label a warehouse "สาขา" by default; make branch an explicit attribute. |
| N-3 | "Valuation" must show the costing policy it used, or accountants will misread it. | Add ตามนโยบายต้นทุน: มาตรฐาน / ถัวเฉลี่ย / FIFO in the report header. |
| N-4 | "Consumable" has an established Thai accounting sense (วัสดุสิ้นเปลือง, Reopen `12`). | Use วัสดุสิ้นเปลือง, not "สินค้าใช้แล้วหมด". |
| N-5 | Statutory report names (รายงานสินค้าและวัตถุดิบ) must not be claimed without authoritative evidence (Council 06 rule). | Keep as alternate name marked `HOLD / EVIDENCE REQUIRED` until Accounting/Tax track confirms. |

All labels above are candidates only. They are not final approved SMEsPlus UI labels.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
