# 09 — Product Master / UoM / Traceability Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-04 OUTPUT — PRODUCT MASTER, UNIT, VARIANT, LOT/SERIAL REFERENCE — NOT APPROVED DESIGN`
Clean-room boundary: business identity and process learning only. Benchmark facts are cited from Layer 1 deliverables of the reopen package (`170af9ea`) and are never restated as SMEsPlus schema. Field or model names from the benchmark are not used as target names.

Menus covered: MENU-PR-01 Products, MENU-PR-02 Product Variants, MENU-PR-03 Lots/Serial Numbers, MENU-CF-10 Attributes, MENU-CF-11 Product Packagings, MENU-CF-14 UoM Categories.

---

## 1. Products — สินค้า (MENU-PR-01)

### 1.1 Purpose / Input / Process / Output / Control

| Aspect | Content |
|---|---|
| Purpose | Single master record for anything the company buys, sells, stocks, consumes, or provides. Everything downstream (stock, valuation, sales, purchase, tax) references it. |
| Input | Name (Thai/English), internal code, barcode, product type (see 1.2), category, base UoM, purchase UoM, sales/purchase flags, tracking mode (none / lot / serial), expiry policy, costing (inherits from category), reorder policy, weight/volume, tax defaults (Accounting-owned), images. |
| Process | Create → (optional) generate variants → set stock policy → activate. Changing type or tracking after stock exists is a controlled change. Archive when no open documents; never delete when history exists. |
| Output | Active product master; product appears in stock, sales, purchase, reports. |
| Control / Accounting impact | Product type decides whether stock truth applies; category decides valuation policy (Accounting-interface); tax defaults are Accounting-owned. Product identity is the primary migration key. |

### 1.2 Product Type — the routing decision (carry-forward from reopen deliverable `12`)

Benchmark fact (Layer 1, reopen `12` and `08`): classification is a **two-axis gate**, not a flat three-way type: a goods/service/combo kind plus a separate "is tracked in stock" flag that only goods may set. A service or a non-tracked good can never hold an on-hand balance. A real extract of 83,753 product rows found 989 rows violating the theoretical invariant, so migration must expect dirty data. Thai accounting concept alignment: non-tracked goods correspond to วัสดุสิ้นเปลือง (consumables expensed on purchase) under TAS 2 guidance as cited in reopen `12`.

SMEsPlus candidate reading for Thai users (three business labels over the two-axis fact):

| Thai candidate label | Business meaning | Stock truth | Valuation | Accounting handoff | Thai example |
|---|---|---|---|---|---|
| สินค้าคงคลัง (stockable) | Counted, reserved, valued | Yes | Yes | Receipt/delivery/adjustment/scrap valuation facts | สินค้าซื้อมาขายไป, วัตถุดิบ, สินค้าสำเร็จรูป |
| วัสดุสิ้นเปลือง (consumable) | Bought and used, not counted | No | No | Purchase expense only | ถุง, กล่อง, น้ำยาทำความสะอาด |
| บริการ (service) | No physical goods | No | No | Revenue/expense only | ค่าติดตั้ง, ค่าแรง |
| (conditional) ชุดสินค้า (combo/kit) | Bundle of the above | Per component | Per component | Per component | ชุดของขวัญ, แพ็กเกจซ่อม + อะไหล่ |

Open items carried: tie-break rule when the two axes disagree in migrated data (`GAP-MD-10`); whether Thai service-plus-parts businesses (ร้านซ่อม, คลินิก, สปา) need kit routing (`INV-FP-13` edge cases, reopen `04_TBRAC` §10 item 5); promotion from consumable to stockable requires a backfill of history (benchmark replays history; SMEsPlus must decide its own rule), demotion has no confirmed cleanup (reopen `06_IDTM`).

### 1.3 Mandatory Process Questions (menu-level)

| # | Question | Answer (candidate reference) |
|---|---|---|
| 1 | Business problem | One identity for each thing the company trades so quantities, costs and taxes agree across departments. |
| 2 | Thai SME users | เจ้าของ, ฝ่ายจัดซื้อ, ฝ่ายขาย, คลัง, บัญชี (read-only for cost). |
| 3 | Starting event | New item to buy/sell; supplier catalogue; migration load. |
| 4 | Master data first | UoM group, product category, (optional) attributes, tax codes (Accounting). |
| 5 | Manual vs automated | Manual create/edit; automatic: variant generation, code sequence, barcode validation. |
| 6 | Quantity state change | None by itself; type/tracking changes alter future stock behaviour. |
| 7 | Valuation / accounting handoff | Category policy inheritance; cost price visibility rules. |
| 8 | Approval / audit / SoD | Create by purchasing/owner; cost and type changes logged; type change after stock requires approval (candidate). |
| 9 | What goes wrong | Duplicate products (same item under two codes), wrong UoM, wrong type, unit price entered as cost, Thai/English name mismatch with tax invoice. |
| 10 | Migration data | Code, names, barcode, type (both axes), UoM, category, tracking, active flag, cost history (Accounting), external IDs. |
| 11 | Thai name | สินค้า / ข้อมูลสินค้า. |
| 12 | Must not copy | Benchmark field model, the two-field gate as literal schema, any transliterated type labels. |

---

## 2. Product Variants — สินค้าย่อย (MENU-PR-02) and Attributes — คุณลักษณะสินค้า (MENU-CF-10)

| Aspect | Content |
|---|---|
| Purpose | Sell one "model" in many colours/sizes while counting stock per exact item. |
| Input | Attributes and values (MENU-CF-10); product template; variant generation mode. |
| Process | Template + attribute combination → variant (the stock-keeping unit). Variants may carry their own barcode, code suffix, cost (optional), and image. |
| Output | Variant list; stock per variant. |
| Control / Accounting impact | Stock truth and valuation are per variant; reports may roll up to template. Migration must preserve the attribute-value identity, not the display label. |
| Thai SME reading | เสื้อรุ่น A สีแดง ไซซ์ L; รองเท้าเบอร์ 40. |
| Candidate rules | Attribute values have stable codes; a variant cannot be deleted once stocked; template-level changes (category, UoM) cascade with confirmation; variant-specific cost is Accounting-interface. |
| Evidence status | `HOLD / EVIDENCE REQUIRED` — reopen `02` item 2: no dedicated variant evidence in any round (`GAP-MD-08`). Process above is `PROCESS BENCHMARK` knowledge plus Thai retail practice, not source-verified. |

---

## 3. Lots / Serial Numbers — เลขล็อต / เลขซีเรียล (MENU-PR-03)

| Aspect | Content |
|---|---|
| Purpose | Trace which batch or which individual unit went where, for recall, expiry, warranty and QC. |
| Input | Product tracking mode; lot/serial value (typed, scanned, or generated); optional expiry / best-before / removal / alert dates; optional supplier lot reference. |
| Process | On receipt: lot/serial assigned per unit (serial) or per batch (lot). On delivery/consumption: system proposes lots by removal strategy (FIFO / FEFO by expiry) and records which lot left. Lot history = every movement of that lot across locations. |
| Output | Lot master + full movement history; expiry watch list; recall query ("which customers received lot X?"). |
| Control / Accounting impact | No direct valuation effect (valuation is per product or per cost layer). Control: serial uniqueness must be enforced at write time (benchmark evidence: uniqueness enforced only at application layer and serial duplicates detected reactively — reopen `02` items 20–21). Expiry workflow depth unread (`02` item 23). |
| Thai SME reading | อาหาร/ยา/เครื่องสำอาง: ล็อตผลิตและวันหมดอายุ; เครื่องใช้ไฟฟ้า/มือถือ: หมายเลขเครื่องเพื่อรับประกัน. |
| Candidate rules | Serial unique per product per company (hard rule); lot unique per product per company; expiry date mandatory when expiry tracking is on; FEFO default for expiry-tracked products; recall report and warranty lookup are first-class; lot cannot be edited after first movement (only merged/corrected with reason). |
| Migration | Lot/serial values, their product, current location balance per lot, expiry dates, and movement history per lot (or at least opening balance per lot at cutover with evidence). |
| Evidence status | Identity facts `CARRY_FORWARD_WITH_EVIDENCE`; expiry/removal workflow `HOLD / EVIDENCE REQUIRED` (`GAP-MD-09`); consignment/owner stock never researched (`N-A5-03`). |

---

## 4. UoM Categories — กลุ่มหน่วยนับ (MENU-CF-14)

| Aspect | Content |
|---|---|
| Purpose | Let Thai SMEs buy in ลัง, count in ชิ้น, and sell in โหล without losing quantity truth. |
| Input | Group (ชิ้น-based, น้ำหนัก, ปริมาตร, ความยาว, เวลา), units in group, conversion factor to the group reference, rounding. |
| Process | Every document line quantity is converted to the product's base unit for stock; the entered unit and quantity are preserved on the document for the user. |
| Output | Stock in base unit; document in user's unit. |
| Control / Accounting impact | Conversion feeds valuation; benchmark default rounding is "up" and factor edits are non-retroactive (reopen `02` item 3) — SMEsPlus must version factors with effective dates. |
| Thai SME reading | 1 โหล = 12 ชิ้น; 1 ลัง = 24 ขวด; 1 กก. = 1,000 ก. |
| Candidate rules | Base unit immutable once stock exists; factor change creates a new version effective from a date; rounding policy explicit per unit; no cross-group conversion; product-specific pack conversions live in Packagings, not in UoM. |
| Evidence status | `CARRY_FORWARD_WITH_EVIDENCE` for conversion facts; Thai unit set is a candidate. |

---

## 5. Product Packagings — หน่วยบรรจุ (MENU-CF-11)

Covered in `08_CONFIGURATION_FOUNDATION_MAP.md` §3.10. Key distinction for Thai users: หน่วยนับ (how counted) vs หน่วยบรรจุ (how packed). Packaging never changes the base-unit stock fact. Evidence status `HOLD / EVIDENCE REQUIRED` (`GAP-MD-18`).

---

## 6. Product Identity and Migration Keys (for Leadership Database Design overlay)

| Identity | Candidate key | Stability requirement | Migration note |
|---|---|---|---|
| Product template | internal code (unique per company) + external source ID | Code immutable after first movement | Benchmark has no external-ID/provenance field (reopen `06_IDTM`) — mapping layer must be originated |
| Variant | template + ordered attribute-value codes | Value codes immutable | Display labels may change |
| Lot | product + lot value (+ company) | Immutable after first movement | Supplier lot reference kept as attribute |
| Serial | product + serial value (+ company); globally unique per product | Immutable | Must be DB-enforced in SMEsPlus (benchmark app-layer only) |
| UoM | group + unit code | Base unit immutable | Factor versions by effective date |
| Packaging | product + packaging code | Quantity immutable after use | — |
| Category | path | Rename allowed; policy change controlled | Valuation policy history needed |

Reconciliation facts Inventory must be able to emit per product: opening qty, Σ receipts, Σ issues, Σ adjustments, Σ scrap, closing qty, all in base unit, per location and per lot where tracked.

---

## 7. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-08 | Variants/attributes: no evidence | Track 04 / S2 | Team B precondition (conditional feature) |
| GAP-MD-09 | Expiry / removal workflow depth; consignment stock | Track 02, 04 / S4 | Team B precondition for food/pharma tenants |
| GAP-MD-10 | Type-axis tie-break rule and kit/combo handling for Thai service-plus-parts | Track 03 / S2 | Team B precondition |
| GAP-MD-11 | Serial/lot uniqueness must be DB-enforced in target; benchmark is app-layer only | Track 04 / S4 | Design requirement, not evidence gap |
| GAP-MD-18 | Packaging behaviour | Track 04 / S2 | Non-blocking |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
