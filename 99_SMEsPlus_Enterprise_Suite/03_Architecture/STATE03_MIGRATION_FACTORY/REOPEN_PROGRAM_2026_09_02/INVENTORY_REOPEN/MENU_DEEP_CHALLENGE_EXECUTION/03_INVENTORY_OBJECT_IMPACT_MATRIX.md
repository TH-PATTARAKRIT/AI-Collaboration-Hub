# 03 — Inventory Object Impact Matrix

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — BUSINESS OBJECT IMPACT MATRIX — NOT A DATA MODEL, NOT APPROVED DESIGN`
Clean-room boundary: "objects" here are **business concepts** (what a Thai SME must be able to name and count), not database entities. Object names are English business terms with Thai candidates; no benchmark model or field name is used. Identity/relationship statements are candidate requirements for the Leadership Database Design overlay, not schema.

---

## 1. Object Register

| Object ID | Business object | Thai candidate | Menus that create/own | Menus that read | Identity (candidate) | Owner domain |
|---|---|---|---|---|---|---|
| OBJ-01 | Company / tenant context | บริษัท | (Platform) | all | tenant + company | SaaS Foundation |
| OBJ-02 | Warehouse | คลังสินค้า | CF-02 | all | company + code | Inventory |
| OBJ-03 | Location | ตำแหน่งจัดเก็บ | CF-03, CF-02 (defaults) | OP-*, RP-* | warehouse + path; type | Inventory |
| OBJ-04 | Operation type (document kind) | ประเภทรายการคลัง | CF-06 | OP-03, OP-02, OP-04 | warehouse + code | Inventory |
| OBJ-05 | Flow template / route | เส้นทางการไหลของสินค้า | CF-04, CF-05 | OP-01, OP-03 | company + template id + version | Inventory |
| OBJ-06 | Storage category | ประเภทพื้นที่จัดเก็บ | CF-07 | CF-08 | company + code | Inventory |
| OBJ-07 | Putaway rule | กฎจัดเก็บสินค้าเข้าที่ | CF-08 | OP-03 | company + priority + key | Inventory |
| OBJ-08 | Product category | หมวดหมู่สินค้า | CF-09 | PR-01, RP-05 | company/tenant + path | Inventory (tree) / Joint (policy) |
| OBJ-09 | Valuation policy (timing + method) | นโยบายต้นทุน | CF-09 (candidate owner) | RP-05, OP-05 | policy id + version + effective date | **Joint / Accounting** |
| OBJ-10 | Attribute and value | คุณลักษณะสินค้า | CF-10 | PR-02 | code | Inventory / Sales |
| OBJ-11 | Product (template) | สินค้า | PR-01 | all | company + code; external ID | Inventory (master) |
| OBJ-12 | Product variant (SKU) | สินค้าย่อย | PR-02 | all | product + attribute-value codes | Inventory |
| OBJ-13 | Product kind (stockable / consumable / service) | ประเภทสินค้า | PR-01 | OP-*, RP-05 | derived attribute (two-axis in benchmark) | Inventory (fact) / Accounting (WHT use) |
| OBJ-14 | UoM group and unit | หน่วยนับ | CF-14 | all | group + unit code; factor version | Inventory |
| OBJ-15 | Packaging | หน่วยบรรจุ | CF-11 | OP-03 | product + code | Inventory |
| OBJ-16 | Barcode format | รูปแบบบาร์โค้ด | CF-13 | OP-*, OP-02 | company + name | Inventory |
| OBJ-17 | Lot | ล็อต | PR-03, OP-03 | RP-03, OP-04 | product + lot value (+ company) | Inventory |
| OBJ-18 | Serial | ซีเรียล | PR-03, OP-03 | RP-03 | product + serial (+ company), unique | Inventory |
| OBJ-19 | Package / handling unit | หีบห่อ | OP-03 (if enabled) | RP-02 | package code; history snapshot | Inventory |
| OBJ-20 | Reorder rule | จุดสั่งซื้อ | CF-12 | OP-01, OP-06 | product + location | Inventory |
| OBJ-21 | Replenishment proposal | ข้อเสนอเติมสินค้า | OP-01, OP-06 | OP-01 | rule + run id | Inventory |
| OBJ-22 | Demand (planned quantity) | ความต้องการ | Sales / Purchase / MFG orders → OP-03 | OP-01 | source line + attempt (idempotency) | Source domain |
| OBJ-23 | Reservation | การจอง | OP-03, OP-06 | RP-01 | movement + bin balance | Inventory |
| OBJ-24 | Stock document (receipt / delivery / transfer / return) | ใบรับ / ใบจ่าย / ใบโอน / ใบคืน | OP-03 | RP-* | operation type + number | Inventory |
| OBJ-25 | Movement fact (done line) | รายการเคลื่อนไหว | OP-03, OP-02, OP-04, MFG | RP-03, RP-04, RP-05 | document line + attempt; immutable | Inventory |
| OBJ-26 | Stock balance (on hand per bin) | ยอดคงเหลือ | derived from OBJ-25 | RP-01, RP-02 | product × location × lot × package (× owner) | Inventory |
| OBJ-27 | Count session / count sheet | ใบตรวจนับ | OP-02 | RP-* | session id | Inventory |
| OBJ-28 | Adjustment | รายการปรับปรุงยอด | OP-02 | RP-03, TH-R07 | number; reason; approver | Inventory (fact) / Accounting (posting) |
| OBJ-29 | Scrap | รายการตัดสินค้าเสีย | OP-04 | TH-R08 | number; reason; approver | Inventory (fact) / Accounting (posting) |
| OBJ-30 | Landed cost allocation | การปันส่วนต้นทุนเพิ่ม | OP-05 | RP-05 | document + receipt line | Inventory (fact) / Accounting (posting) |
| OBJ-31 | Valuation fact (value change event) | รายการมูลค่า | OP-03, OP-02, OP-04, OP-05, MFG | RP-05 | movement + policy version | Inventory emits / Accounting owns posting |
| OBJ-32 | Period close snapshot (qty/value) | ยอดปิดงวด | RP-05 (Joint) | RP-05 | company + period | Joint |
| OBJ-33 | Opening balance at cutover | ยอดยกมา | Migration + OP-02 | RP-05 | company + cutover date; certification | Joint (`G-5`) |
| OBJ-34 | Feature switch set | การตั้งค่า | CF-01 | all | company + version | Inventory / SaaS |
| OBJ-35 | Scheduler run log | บันทึกการประมวลผล | OP-06 | admin | run id | Inventory |
| OBJ-36 | External ID / provenance map | รหัสอ้างอิงระบบเดิม | Migration | all | source system + source key → target key | Migration (to be originated) |

---

## 2. Impact Flags per Object

| Object ID | Stock truth | Quantity | Reservation | Lot/serial | Warehouse/location | Valuation | Accounting handoff | Tax/statutory | Mgmt report | Audit/control | Migration | SaaS/multi-co |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OBJ-01 | C | N | N | N | Y | Y | Y | Y | Y | Y | Y | Y |
| OBJ-02 | Y | N | N | N | Y | C | N | C | Y | Y | Y | Y |
| OBJ-03 | Y | N | N | N | Y | C | C | N | Y | Y | Y | Y |
| OBJ-04 | C | N | C | C | Y | C | C | C | Y | Y | Y | Y |
| OBJ-05 | N | N | C | N | Y | N | N | N | N | Y | C | Y |
| OBJ-06 | N | N | N | N | Y | N | N | N | N | N | N | Y |
| OBJ-07 | N | N | N | C | Y | N | N | N | N | C | N | Y |
| OBJ-08 | N | N | N | N | N | Y | Y | Y | Y | Y | Y | Y |
| OBJ-09 | N | N | N | N | N | Y | Y | Y | Y | Y | Y | Y |
| OBJ-10 | Y | N | N | N | N | N | N | N | C | C | Y | Y |
| OBJ-11 | Y | N | N | C | N | Y | C | C | Y | Y | Y | Y |
| OBJ-12 | Y | N | N | N | N | Y | N | N | Y | C | Y | Y |
| OBJ-13 | Y | N | Y (bypass when not tracked) | C | N | Y | Y | Y (WHT correlation) | Y | Y | Y | Y |
| OBJ-14 | Y | Y | N | N | N | Y | C | N | N | Y | Y | Y |
| OBJ-15 | N | C | N | N | N | N | N | N | N | C | C | Y |
| OBJ-16 | N | C | N | C | C | N | N | N | N | C | C | Y |
| OBJ-17 | Y | Y | C | Y | Y | N | N | C | Y | Y | Y | Y |
| OBJ-18 | Y | Y | C | Y | Y | N | N | C | Y | Y | Y | Y |
| OBJ-19 | Y | C | C | C | Y | N | N | N | C | Y | Y | Y |
| OBJ-20 | N | N | N | N | Y | N | N | N | Y | C | C | Y |
| OBJ-21 | N | N | N | N | Y | N | N | N | Y | C | N | Y |
| OBJ-22 | N | Y (planned) | Y | N | Y | N | N | N | Y | Y | Y | Y |
| OBJ-23 | N | N | Y | C | Y | N | N | N | Y | Y | N | Y |
| OBJ-24 | C | Y | Y | Y | Y | C | C | C | Y | Y | Y | Y |
| OBJ-25 | Y | Y | Y | Y | Y | Y | Y | C | Y | Y | Y | Y |
| OBJ-26 | Y | Y | Y | Y | Y | Y | C | N | Y | Y | Y | Y |
| OBJ-27 | C | C | C | Y | Y | N | N | C | Y | Y | N | Y |
| OBJ-28 | Y | Y | C | Y | Y | Y | Y | C | Y | Y | Y | Y |
| OBJ-29 | Y | Y | C | Y | Y | Y | Y | Y | Y | Y | C | Y |
| OBJ-30 | N | N | N | N | N | Y | Y | C | C | Y | C | Y |
| OBJ-31 | N | N | N | N | C | Y | Y | Y | Y | Y | Y | Y |
| OBJ-32 | N | Y | N | N | C | Y | Y | Y | Y | Y | Y | Y |
| OBJ-33 | Y | Y | N | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| OBJ-34 | C | N | C | C | Y | C | C | N | N | Y | Y | Y |
| OBJ-35 | N | N | Y | N | N | N | N | N | N | Y | N | Y |
| OBJ-36 | N | N | N | Y | Y | Y | Y | N | N | Y | Y | Y |

---

## 3. Candidate Invariants (for Leadership Database Design overlay; requirements, not schema)

| Inv ID | Invariant | Benchmark status (Layer 1) | SMEsPlus candidate |
|---|---|---|---|
| INV-01 | On-hand per bin = Σ done movements in − Σ done movements out | Enforced at application layer only; no DB check | DB-enforced or continuously reconciled with alarm |
| INV-02 | On-hand ≥ 0 unless tenant explicitly allows negative | Available clamped to 0; true negative can persist | Displayed, flagged, policy-controlled |
| INV-03 | One bin balance per (product, location, lot, package, owner) | No unique index; merges after the fact | Unique constraint |
| INV-04 | Serial unique per product per company | App-layer, reactive duplicate detection | DB-enforced |
| INV-05 | Done movement immutable | Confirmed (no un-done path) | Same, with reverse-movement corrections |
| INV-06 | Every movement has a unique idempotency key | None exists | Required (`C-02` severity is Boss's call) |
| INV-07 | Movement date within open period unless audited exception | Document-level guard via accounting bridge; global unaudited bypass | Native period guard + exception record |
| INV-08 | Every record scoped to one company; no cross-tenant read/write | ORM-layer rules; no DB backstop; bypass audit not done | DB-layer isolation + post-write audit |
| INV-09 | Every migrated record carries source provenance | No provenance field in source | Provenance map (OBJ-36) required |
| INV-10 | Valuation report reproducible as of date and equals GL after close | Reconciliation report export defective; closure Joint | Acceptance test |
| INV-11 | UoM factor changes never alter historical quantities | Non-retroactive by construction; rounding default up | Versioned factors, explicit rounding |
| INV-12 | Product kind change with existing stock is controlled | Promotion backfills history; demotion no cleanup | Approval + backfill/close-out rule |

---

## 4. Object Gaps

| Gap ID | Object | Gap | Owner |
|---|---|---|---|
| GAP-MD-08 | OBJ-10, OBJ-12 | No variant evidence | Track 04 / S2 |
| GAP-MD-11 | OBJ-17, OBJ-18 | DB uniqueness requirement | Track 04 / S4 |
| GAP-MD-13 | OBJ-08, OBJ-09, OBJ-32 | Policy owner; close design | Joint |
| GAP-MD-26 | OBJ-19 | Package migration disposition (live vs history vs both) undecided since DR-002 | Track 04 / S9 |
| GAP-MD-27 | OBJ-36 | Provenance/external-ID map does not exist and must be originated | Track 04, 09 / S9 |
| U-03 | OBJ-01 | Inventory-side SaaS invariant set | Track 05 / Boss |
| U-04 / G-5 | OBJ-33 | Opening balance certification | Joint / Track 09 |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
