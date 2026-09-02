# 11 — Inventory Thai Localization, UX and Naming v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `NAMING AND LOCALIZATION CANDIDATES — NOT APPROVED UI LABELS — NO STATUTORY CLAIM MADE`
Clean-room: Layer 1. No Thai label here is a transliteration of any reference-ERP term, and no reference-ERP label set is reproduced.

> **Blanket validation status.** **Real Thai user validation has never been performed for any Inventory label, flow, reason code, document name or report title in this programme.** Every Thai name, every naming recommendation and every assumption about Thai warehouse practice in this file is therefore `UNVALIDATED - THAI USER REVIEW REQUIRED`. The label is repeated inline throughout so that no row can be quoted out of context as validated.

---

## 1. Naming Principles

| # | Principle | Rule |
|---|---|---|
| `NP-1` | Speak like a Thai storekeeper, not like an ERP | Use the verbs staff already use: รับเข้า, จ่ายออก, โอนย้าย, นับสต็อก, ตัดของเสีย |
| `NP-2` | Separate facts from summaries | รายการ… is a movement list; รายงาน… or ยอด… is a summary |
| `NP-3` | Separate the person's action from the system's proposal | เติมสินค้า (a person acts) against แผนเติมสินค้า (the system proposes) |
| `NP-4` | Make control visible in the name | Names for adjustment, scrap and valuation must carry the word that signals approval or money: ปรับปรุง, ตัด, มูลค่า |
| `NP-5` | Accountant and auditor readability | Artefacts that reach an accountant use accounting vocabulary: มูลค่าสินค้าคงเหลือ, สต็อกการ์ด |
| `NP-6` | Hide engineering vocabulary | "Rule", "route", "scheduler", "nomenclature" have no Thai SME equivalent; wrap them in a business phrase or hide them behind a template |
| `NP-7` | Never transliterate a benchmark term | A Thai label may never be a phonetic rendering of a reference-ERP label |
| `NP-8` | One concept, one word, everywhere | The same Thai word must mean the same thing on every screen, every document and every report |

---

## 2. Menu Naming Register — All 29

Every row: `UNVALIDATED - THAI USER REVIEW REQUIRED`.

| Menu | Primary Thai candidate | Alternates | Short label | Note | Status |
|---|---|---|---|---|---|
| OP-01 Replenishment | เติมสินค้า / แผนเติมสินค้า | รายการที่ต้องสั่งเติม, สินค้าใกล้หมด | เติมสินค้า | Two sub-views recommended: what is running out, and what the system proposes | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| OP-02 Inventory Adjustments | ปรับปรุงยอดสต็อก | นับสต็อก / ตรวจนับสินค้า (count sub-flow) | ปรับสต็อก | Entry point should be the count; the adjustment is the approved result. Reason field label: เหตุผลการปรับ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| OP-03 Transfers | รายการเคลื่อนย้ายสินค้า (umbrella) | รับสินค้าเข้า, จ่ายสินค้าออก, โอนย้ายภายใน, รับคืน / ส่งคืน | รับเข้า / จ่ายออก / โอนย้าย | Thai staff do not look for one "transfers" list; three first-level entries plus one umbrella search | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| OP-04 Scrap | ตัดสินค้าชำรุด/สูญเสีย | ตัดสินค้าเสีย, ทำลายสินค้า | ตัดของเสีย | Reason axis candidate: ชำรุด / หมดอายุ / สูญหาย / ทำลายตามระเบียบ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| OP-05 Landed Costs | ต้นทุนสินค้าเพิ่มเติม | ต้นทุนนำเข้า, ค่าใช้จ่ายรวมเข้าต้นทุนสินค้า | ต้นทุนเพิ่ม | The label must signal that stock value changes | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| OP-06 Run Scheduler | ประมวลผลแผนสต็อก | สถานะการประมวลผลอัตโนมัติ | ประมวลผล | Not an end-user menu; an administrator status view with last-run time and result | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| PR-01 Products | สินค้า | ข้อมูลสินค้า, ทะเบียนสินค้า | สินค้า | Product kind shown in Thai: สินค้าคงคลัง / วัสดุสิ้นเปลือง / บริการ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| PR-02 Product Variants | สินค้าย่อย | ตัวเลือกสินค้า, รุ่นย่อย (สี/ไซซ์) | สินค้าย่อย | Must make clear stock is counted per variant | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| PR-03 Lots / Serials | เลขล็อต / เลขซีเรียล | ล็อตการผลิต, หมายเลขเครื่อง | ล็อต/ซีเรียล | Show วันหมดอายุ and warranty status as columns | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-01 Stock | ยอดสินค้าคงเหลือ | สต็อกคงเหลือ | ยอดคงเหลือ | Four quantities in Thai: คงเหลือจริง / จองแล้ว / พร้อมใช้ / คาดการณ์ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-02 Locations | สินค้าคงเหลือตามตำแหน่งจัดเก็บ | ยอดคงเหลือรายชั้นวาง | คงเหลือตามที่เก็บ | Visible only when multiple places are enabled | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-03 Moves History | ประวัติการเคลื่อนไหวสินค้า | สต็อกการ์ด | สต็อกการ์ด | The statutory-style alternate name is **not claimed** — see §5 | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-04 Stock Moves | รายการเคลื่อนไหวสินค้า | รายการระดับรายการ | รายการเคลื่อนไหว | Advanced and audit visibility only | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-05 Valuation | มูลค่าสินค้าคงเหลือ ณ วันที่ | รายงานมูลค่าสต็อก | มูลค่าสต็อก | Header must show the costing policy and the date | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| RP-06 Warehouse Analysis | วิเคราะห์คลังสินค้า | ภาพรวมคลังสินค้า | วิเคราะห์คลัง | Management view; must not read as an audit report | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-01 Settings | ตั้งค่าระบบคลังสินค้า | การตั้งค่าคลังสินค้า | ตั้งค่า | Switches worded as business questions: เปิดใช้ล็อต/ซีเรียล, เปิดใช้หลายตำแหน่งจัดเก็บ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-02 Warehouses | คลังสินค้า | สาขา/คลัง only where the tenant genuinely equates them | คลัง | **Never labelled สาขา by default** — see §4 `N-2` | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-03 Locations | ตำแหน่งจัดเก็บ | ที่เก็บสินค้า, ชั้นวาง/โซน | ตำแหน่ง | System counterpart places need plain Thai explanations | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-04 Routes | เส้นทางการไหลของสินค้า | ขั้นตอนรับ-จ่ายสินค้า (1/2/3 ขั้น) | เส้นทางสินค้า | Presented as named templates, e.g. รับสินค้า 1 ขั้นตอน, รับแล้วตรวจคุณภาพก่อนเก็บ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-05 Rules | กฎการไหลของสินค้า | เงื่อนไขการเคลื่อนย้ายอัตโนมัติ | กฎสินค้า | Advanced only; Thai SMEs should never need to edit this | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-06 Operation Types | ประเภทรายการคลัง | ประเภทเอกสารคลัง | ประเภทรายการ | Document numbering conventions belong here — a candidate, not a requirement | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-07 Storage Categories | ประเภทพื้นที่จัดเก็บ | ประเภทที่เก็บ (เย็น/แห้ง/อันตราย) | ประเภทที่เก็บ | Only for capacity- or condition-constrained warehouses | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-08 Putaway Rules | กฎจัดเก็บสินค้าเข้าที่ | กำหนดที่เก็บอัตโนมัติ | จัดเก็บเข้าที่ | Should read as the worker's question: รับเข้าแล้วให้ไปเก็บที่ไหน | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-09 Product Categories | หมวดหมู่สินค้า | หมวดหมู่สินค้าและนโยบายต้นทุน if it owns costing | หมวดสินค้า | If the object owns valuation policy, the label must say so | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-10 Attributes | คุณลักษณะสินค้า | ตัวเลือก (สี, ขนาด) | คุณลักษณะ | Pairs with สินค้าย่อย | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-11 Product Packagings | หน่วยบรรจุ / แพ็กสินค้า | ขนาดบรรจุ (ลัง 12 ชิ้น) | หน่วยบรรจุ | Must not be confused with หน่วยนับ — see §4 `N-6` | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-12 Reordering Rules | จุดสั่งซื้อ | ยอดต่ำสุด-สูงสุด | จุดสั่งซื้อ | Thai SMEs understand จุดสั่งซื้อ better than a rule metaphor | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-13 Barcode Nomenclatures | รูปแบบบาร์โค้ด | มาตรฐานบาร์โค้ด | บาร์โค้ด | "Nomenclature" has no Thai SME equivalent; use รูปแบบ | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| CF-14 UoM Categories | กลุ่มหน่วยนับ | หน่วยนับและอัตราแปลง | หน่วยนับ | Show the conversion in plain Thai: 1 โหล = 12 ชิ้น | `UNVALIDATED - THAI USER REVIEW REQUIRED` |

---

## 3. Report, Document and Reason-Code Naming

All rows: `UNVALIDATED - THAI USER REVIEW REQUIRED`.

| Artefact | Thai candidate |
|---|---|
| On-hand report | ยอดสินค้าคงเหลือ (คงเหลือจริง / จองแล้ว / พร้อมใช้) |
| Stock by place | สินค้าคงเหลือตามตำแหน่งจัดเก็บ |
| Stock card | สต็อกการ์ด / ประวัติการเคลื่อนไหวสินค้า |
| Movement fact ledger | รายการเคลื่อนไหวสินค้า (ระดับรายการ) |
| Valuation | มูลค่าสินค้าคงเหลือ ณ วันที่ |
| Valuation reconciliation | กระทบยอดมูลค่าสต็อกกับบัญชี |
| Adjustment register | ทะเบียนการปรับปรุงยอดสต็อก |
| Scrap register | ทะเบียนตัดสินค้าชำรุด/ทำลาย |
| Traceability | รายงานตามรอยล็อต/ซีเรียล |
| Expiry watch list | สินค้าใกล้หมดอายุ |
| Reorder proposals | สินค้าใกล้หมด / แผนเติมสินค้า |
| Warehouse performance | วิเคราะห์คลังสินค้า |
| Landed cost statement | รายงานปันส่วนต้นทุนเพิ่มเติม |
| Count sheet | ใบตรวจนับสินค้า |
| Open transit ageing | สินค้าระหว่างขนส่งค้างนาน |
| Receipt document | ใบรับสินค้า |
| Delivery document | ใบจ่ายสินค้า |
| Internal transfer document | ใบโอนสินค้า |
| Return document | ใบรับคืน / ใบส่งคืน |
| Adjustment reasons | นับพบเกิน, นับพบขาด, บันทึกผิด, สูญหาย, ยอดยกมา |
| Scrap reasons | ชำรุด, หมดอายุ, สูญหาย, ทำลายตามระเบียบ |
| Return reasons | สินค้าผิดรุ่น, สินค้าชำรุด, ลูกค้าไม่รับ, ส่งเกิน |

---

## 4. Naming Conflicts and Recommendations for Boss

| # | Issue | Recommendation | Status |
|---|---|---|---|
| `N-1` | One "transfers" umbrella hides the three documents Thai staff actually use. | Keep the umbrella for search; expose รับเข้า, จ่ายออก, โอนย้าย as first-level entries. | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `N-2` | คลัง (warehouse) and สาขา (tax branch) are routinely conflated, and the tax consequence of conflating them is real. | Never label a warehouse สาขา by default; make branch an explicit, separate attribute. The statutory consequence is `HOLD / EVIDENCE REQUIRED` (`TH-HOLD-06`). | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `N-3` | A valuation figure without its costing policy will be misread by an accountant. | Print the policy and version in the report header: ตามนโยบายต้นทุน …. | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `N-4` | "Consumable" already has an established Thai accounting sense. | Use วัสดุสิ้นเปลือง, never an invented phrase. | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `N-5` | Statutory-sounding Thai report names must not be claimed without authoritative evidence. | Keep any statutory-style alternate name marked `HOLD / EVIDENCE REQUIRED` until the Accounting-Tax track confirms it. | `HOLD / EVIDENCE REQUIRED` |
| `N-6` | หน่วยบรรจุ (packaging) and หน่วยนับ (unit of measure) are easily confused, and confusing them produces double conversion. | Keep the two words rigorously distinct on every screen, and never let one screen offer both as if interchangeable. | `UNVALIDATED - THAI USER REVIEW REQUIRED` |
| `N-7` | Reason codes carry control weight; a vague list produces a useless register. | Keep the reason list short, mutually exclusive, and phrased as what actually happened rather than as an accounting category. | `UNVALIDATED - THAI USER REVIEW REQUIRED` |

---

## 5. Thai Statutory and Legal Items — All Held and Routed

**This session is not a Thai tax authority and has no legal evidence source. Nothing below is asserted.**

| ID | Item | Status | Routed to |
|---|---|---|---|
| `TH-HOLD-01` | Statutory stock-report format and title; whether the stock card satisfies it | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-02` | Scrap destruction procedure and deductibility evidence | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-03` | Import duty and import VAT treatment in landed cost | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-04` | Withholding-tax correlation with product kind | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-05` | Accepted Thai costing norms | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-06` | Warehouse against registered tax branch | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-07` | Witnessed annual physical count requirements | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |
| `TH-HOLD-08` | Sector traceability obligations (food, pharmaceutical, cosmetics) | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track, for onward legal routing |
| `TH-HOLD-09` | Delivery document to tax invoice linkage and numbering conventions | `HOLD / EVIDENCE REQUIRED` | Accounting-Tax track |

---

## 6. UX Requirements Beyond Naming

All `UNVALIDATED - THAI USER REVIEW REQUIRED`.

| # | Requirement |
|---|---|
| `UX-01` | Thai and English labels coexist; the Thai label is primary for operational users and the English label is available for reporting and support. |
| `UX-02` | Thai date presentation, including Buddhist-era year display where the tenant expects it, must be a setting rather than an assumption. |
| `UX-03` | Number and unit display follows Thai convention; the unit is always shown next to the quantity, never implied. |
| `UX-04` | Warehouse work screens must be usable on a phone or a handheld scanner, one-handed, in a warehouse with poor light and intermittent connectivity. |
| `UX-05` | Every refusal message says what was refused, why, and what the user can do next — never a bare error. |
| `UX-06` | Every automatic decision shows its reason in one readable Thai sentence. |
| `UX-07` | Advanced capabilities stay invisible until switched on; a micro-tier tenant must never see a distributor's screen. |
| `UX-08` | Printed documents follow the layout Thai staff and their customers expect; what that layout is has never been validated. |

---

## 7. Validation Plan Required Before Any of This Is Approved

| Step | What is needed |
|---|---|
| 1 | A panel of real Thai SME users — storekeeper, warehouse supervisor, purchaser, owner, external accountant — across at least the micro and growing tiers. |
| 2 | Label-by-label review of §2 and §3, recording accept, reject or replace for each row. |
| 3 | Flow walk-through of the sixteen scenarios in file 05 §5, recording where the user hesitated or misread. |
| 4 | Reason-code review with the people who will actually choose them. |
| 5 | A separate accountant and auditor review of the artefacts in §3 that reach them. |
| 6 | A per-label and per-flow acceptance record, so that "validated" is evidenced rather than asserted. |

Until that record exists, every row in this file remains `UNVALIDATED - THAI USER REVIEW REQUIRED`.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
