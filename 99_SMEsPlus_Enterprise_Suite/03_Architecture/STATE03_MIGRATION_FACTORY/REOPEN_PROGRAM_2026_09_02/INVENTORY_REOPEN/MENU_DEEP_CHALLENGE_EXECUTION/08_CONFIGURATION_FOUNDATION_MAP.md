# 08 — Configuration Foundation Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-03 OUTPUT — CONFIGURATION FOUNDATION — CANDIDATE PROCESS REFERENCE, NOT APPROVED DESIGN`
Clean-room boundary: this map describes what each configuration area *means in business terms* and what must exist before transactions can run. It does not describe or prescribe any vendor data model, field, or workflow implementation. Benchmark behaviour is cited only as `PROCESS BENCHMARK`. All SMEsPlus statements are candidates.

---

## 1. Why Configuration Comes First

In every stock system the transaction documents (receipt, delivery, transfer, count, scrap) are only valid if the master and configuration data they reference already exist. For a Thai SME the practical question is: **what is the smallest set of setup steps a new tenant must complete before the first goods receipt can be recorded, and which steps can be deferred?**

Benchmark observation (process level): a new company is usable after (1) company/tenant created, (2) one warehouse with system-generated default locations and default operation types, (3) at least one product category, (4) a base unit of measure set, (5) products. Everything else (routes, rules, storage categories, putaway, packaging, barcode formats, reordering rules, lots/serials, landed cost) is switched on by feature settings and is optional.

SMEsPlus candidate principle: **Tier 0 setup is silent and automatic; Tier 1 setup is a guided Thai-language wizard; Tier 2 setup is an opt-in "advanced warehouse" area.**

---

## 2. Setup Dependency Order (candidate)

```text
T0  Company / tenant  ->  base currency THB, fiscal year, VAT registrant flag (Accounting-owned facts, consumed by Inventory)
T0  UoM categories + base units (ชิ้น, กิโลกรัม, ลิตร, เมตร)          [MENU-CF-14]
T0  Default product category (with valuation-policy placeholder)         [MENU-CF-09]
T0  Warehouse #1 + system locations (คลังหลัก, รับเข้า, จ่ายออก, สินค้าเสีย, ปรับปรุง) [MENU-CF-02, MENU-CF-03]
T0  Default operation types per warehouse (รับเข้า / จ่ายออก / โอนภายใน) [MENU-CF-06]
T1  Settings: feature switches (lot/serial, expiry, multi-location, packaging, variants, landed cost, barcode) [MENU-CF-01]
T1  Product categories tree + valuation/costing policy per category (Accounting-dependent) [MENU-CF-09]
T1  Products (type, UoM, category, tracking, reorder policy)             [MENU-PR-01]
T2  Attributes + variants                                                 [MENU-CF-10, MENU-PR-02]
T2  Packagings                                                            [MENU-CF-11]
T2  Extra locations, storage categories, putaway rules                    [MENU-CF-03, CF-07, CF-08]
T2  Routes + rules (multi-step receipt/delivery, MTO, resupply)           [MENU-CF-04, CF-05]
T2  Reordering rules -> replenishment -> scheduler                        [MENU-CF-12, MENU-OP-01, MENU-OP-06]
T2  Barcode nomenclature                                                  [MENU-CF-13]
T2  Landed cost types (Accounting-dependent cost accounts)                [MENU-OP-05]
```

Dependency rule: a transaction may not be posted if any T0 object it references is missing; a T1/T2 feature switch may not be turned off while records depending on it exist (for example lot tracking cannot be disabled for a product that already has lot-tracked stock). This "no orphan configuration" control is a candidate SMEsPlus rule, not a benchmark copy.

---

## 3. Configuration Object Map

For each configuration area: Purpose / Input / Process / Output / Control-Accounting impact / Thai SME reading / SMEsPlus candidate / Evidence.

### 3.1 Settings — ตั้งค่าระบบคลังสินค้า (MENU-CF-01)

| Aspect | Content |
|---|---|
| Purpose | Turn on or off optional capabilities per company so that Thai SMEs see only what they use. |
| Input | Administrator decisions: use lots/serials? expiry dates? multiple locations/warehouses? packages? product variants? landed costs? barcode scanning? multi-step routes? reservation policy (reserve at confirmation vs manual)? |
| Process | Each switch reveals menus, fields and default records. Some switches create records (for example enabling multi-location exposes location menus; enabling multi-step routes generates route/rule templates per warehouse). |
| Output | Effective feature set for the tenant; generated default records. |
| Control / Accounting impact | Switches that create or restructure warehouse flow are **structural**: benchmark behaviour regenerates route/rule graphs when warehouse step settings change (Reopen `SAAS-04`). This is a tenant-provisioning risk for SaaS. Valuation-related switches are Accounting-interface facts, not Inventory-owned decisions. |
| Thai SME reading | "เปิดใช้ล็อต/วันหมดอายุ", "ใช้หลายคลัง/หลายตำแหน่ง", "รับสินค้าแบบ 1 ขั้นตอน หรือ ตรวจก่อนเก็บ". |
| SMEsPlus candidate | Settings expressed as business questions in Thai; every switch carries an "on/off allowed?" guard based on existing data; every switch change is audit-logged (who, when, before/after). No switch may silently regenerate flow rules without a preview and confirmation step. |
| Evidence | Reopen `07_IESA` (`SAAS-04`), `09_SECURITY` (`G-2` global toggle without audit). Menu-level: `PROCESS BENCHMARK` knowledge; `UNKNOWN / EVIDENCE REQUIRED` for exact benchmark switch list per version. |

### 3.2 Warehouses — คลังสินค้า (MENU-CF-02)

| Aspect | Content |
|---|---|
| Purpose | Represent a physical site where stock is kept and from which operations are run. |
| Input | Name, short code (used in document numbers), address, company; optional receipt/delivery step policy; resupply-from other warehouses. |
| Process | Creating a warehouse creates its default location tree and default operation types; changing step policy regenerates routes. |
| Output | Warehouse record + location tree + operation types + (optional) routes. |
| Control / Accounting impact | Stock truth is per location under the warehouse; valuation is normally company-wide, not warehouse-wide (Accounting-interface question). Warehouse code appears in every document number, so it is a migration key. |
| Thai SME reading | คลังหลัก, คลังสาขา, คลังหน้าร้าน. **Not** the same as Thai tax branch (สาขาภาษี) — precision note from `GRPA-H8/H3`. |
| SMEsPlus candidate | Warehouse = physical site; Branch (tax) = separate attribute on company/warehouse; a warehouse belongs to exactly one company; cross-company warehouse sharing is out of scope until Joint Session rules. Step policy changes must be previewed and versioned. |
| Evidence | Reopen `02` item 4, `07_IESA`; `GRPA-H8/H3` closure note (`15` §B). |

### 3.3 Locations — ตำแหน่งจัดเก็บ (MENU-CF-03)

| Aspect | Content |
|---|---|
| Purpose | Define *where* stock physically or logically sits: internal bins, receiving dock, shipping dock, customer/vendor virtual locations, loss/scrap, adjustment, transit. |
| Input | Name, parent, type (internal / view / vendor / customer / loss / production / transit), warehouse, optional storage category, optional scrap flag, optional return flag. |
| Process | Locations form a tree; every stock movement is from-location to to-location; quantities are held per (product, location, lot, package, owner). |
| Output | Location tree; on-hand per location. |
| Control / Accounting impact | Location type determines whether a move changes company stock truth (internal ↔ external types) and therefore whether valuation/accounting is affected. Loss/scrap and adjustment locations are the accounting-visible exception sinks. Benchmark evidence: location usage is a closed enumeration (Reopen `02` item 5, CLOSED_WITH_EVIDENCE). |
| Thai SME reading | โซน A ชั้น 1, ห้องเย็น, หน้าร้าน, ระหว่างขนส่ง, สินค้าเสีย. |
| SMEsPlus candidate | Location types as a controlled Thai-labelled enumeration; system locations cannot be deleted; a location can be archived only when empty; warehouse-level (intra-company) permissions are an open unknown (`U-01`) to be decided, not inherited. |
| Evidence | Reopen `02` item 5; `13` U-01; `09_SECURITY` §3. |

### 3.4 Routes — เส้นทางการไหลของสินค้า (MENU-CF-04) and Rules — กฎการไหลของสินค้า (MENU-CF-05)

| Aspect | Content |
|---|---|
| Purpose | Describe *how* a demand becomes movements: one-step receipt vs receive→inspect→store; one-step delivery vs pick→pack→ship; make-to-order; buy-on-demand; resupply from another warehouse; dropship. |
| Input | Route (a named policy applicable to a product, category, warehouse or sales line) composed of ordered rules; each rule says "when demand appears at location X, pull/push from location Y using operation type Z, or trigger buy/manufacture". |
| Process | When a demand (sales order line, manufacturing need, reorder rule) is confirmed, the applicable route is resolved and the rules generate the chain of planned movements. Benchmark: single dispatch point for run/buy/manufacture (Reopen `02` item 24). |
| Output | Planned movement chain; purchase or manufacturing requests. |
| Control / Accounting impact | No direct valuation effect; indirect through which operation types and locations are used. Duplicate/retry safety of dispatch is `PARTIALLY SUPPORTED, not proven` (Reopen `02` item 24). |
| Thai SME reading | "รับสินค้าเข้าคลังโดยตรง" vs "รับแล้วตรวจก่อนเก็บ"; "สั่งซื้อเมื่อมีออเดอร์"; "ส่งตรงจากผู้ขาย (dropship)". |
| SMEsPlus candidate | **Rules and routes hidden behind Thai business templates.** Tenants choose templates (1-step / 2-step / 3-step receipt; 1/2/3-step delivery; buy-to-order; make-to-order; resupply; dropship). Template internals are system-owned; editing raw rules is an advanced, audited action. Route resolution must be deterministic and explainable ("why did this delivery create a pick and a pack?"). `REWRITE_AS_CLEAN_ROOM_LEARNING`: SMEsPlus must not reproduce the benchmark route/rule object model; the business meaning (demand → policy → movement chain) is the learning. |
| Evidence | Reopen `02` items 24–25, `07_IESA`, `11_AI_CONTROL`, `05_IBPV` (dispatch choke point, no procurement-group model — cited as a warning against assuming benchmark model shapes). |

### 3.5 Operations Types — ประเภทรายการคลัง (MENU-CF-06)

See `11_OPERATION_TYPES_AND_STOCK_FLOW_MAP.md` for full treatment. Summary: each warehouse has receipt / delivery / internal (and manufacturing, if used) operation types; each carries its own document number sequence, default source/destination locations, allowed return type, reservation policy, and who may confirm. Thai document names (ใบรับสินค้า, ใบจ่ายสินค้า, ใบโอนย้าย) live here. Segregation of duties per operation type is a named gap (Reopen `02` item 38).

### 3.6 Storage Categories — ประเภทพื้นที่จัดเก็บ (MENU-CF-07)

| Aspect | Content |
|---|---|
| Purpose | Describe constraints of a storage place: maximum weight, maximum number of packages/products, allowed product categories, whether mixing products/lots is allowed. |
| Input | Category name, capacity limits, allowed content rules; assignment to locations. |
| Process | Putaway logic consults storage category capacity to choose a destination; a full location is skipped. |
| Output | Capacity-aware destination selection. |
| Control / Accounting impact | None on valuation. Operational control only (cold chain, hazardous, weight). |
| Thai SME reading | ห้องเย็น (เก็บได้เฉพาะสินค้าแช่เย็น), ชั้นวางหนัก (ไม่เกิน 500 กก.), พื้นที่สารเคมี. |
| SMEsPlus candidate | `CONDITIONAL`; only for warehouses that opt in to bin-level management. Capacity checks are advisory by default (warn), blocking only if the tenant chooses. |
| Evidence | `HOLD / EVIDENCE REQUIRED` — never studied in any prior round; `PROCESS BENCHMARK` knowledge only (`GAP-MD-16`). |

### 3.7 Putaway Rules — กฎจัดเก็บสินค้าเข้าที่ (MENU-CF-08)

| Aspect | Content |
|---|---|
| Purpose | Answer "when this product (or category, or package type) arrives at this location, where should it be stored?" automatically. |
| Input | Product or product category or package type; incoming location; target location or storage category; priority. |
| Process | When a receipt is validated (or an internal move is created), the destination is resolved from the most specific matching rule; storage categories filter by capacity. |
| Output | Suggested/assigned destination bin on the move line. |
| Control / Accounting impact | None on valuation. Traceability impact: the assigned bin becomes part of location history. Product Category is a rule key here **and** a valuation-policy owner candidate — dual ownership flagged by Reopen `14`/`20`. |
| Thai SME reading | "ของแช่เย็นเข้าห้องเย็นเสมอ", "สินค้า A เก็บโซน A". |
| SMEsPlus candidate | `CONDITIONAL`; rule editor in plain Thai; a rule never overrides an explicit user choice; every automatic assignment is explainable. Category dual ownership must be designed deliberately (separate "storage class" attribute from "valuation category" if needed) — Joint Session item. |
| Evidence | `HOLD / EVIDENCE REQUIRED` for benchmark mechanics; Reopen `14` §2 and `20` §3 for the category dual-ownership concern (`GAP-MD-17`). |

### 3.8 Product Categories — หมวดหมู่สินค้า (MENU-CF-09)

| Aspect | Content |
|---|---|
| Purpose | Group products for reporting, for default routes/putaway, and (in the benchmark) as the owner of valuation timing and costing method. |
| Input | Category name, parent, removal strategy (FIFO/LIFO/FEFO preference for picking), valuation policy (manual/periodic vs automated/perpetual), costing method (standard / average / FIFO), and the accounting mapping (stock valuation account, stock input/output clearing, variance, expense) — the mapping is Accounting-owned. |
| Process | Products inherit category policy; changing category policy affects future valuation of all products in it. |
| Output | Effective valuation and costing policy per product; picking strategy per product. |
| Control / Accounting impact | **Highest accounting impact of any configuration object.** Reopen chain: Product Category confirmed as the benchmark's true valuation-policy owner (`N-A12-01` package). Clean-room Layer 1 learning is in CORR-007B file 09 (rewritten, commit `9996072a`), which lists four candidate policy owners (company / category / product / native policy object) and requires SMEsPlus to choose explicitly. `C-05` control preserved: this map uses only the rewritten Layer 1 summary. |
| Thai SME reading | หมวดสินค้าซื้อมาขายไป, วัตถุดิบ, สินค้าสำเร็จรูป, อะไหล่, วัสดุสิ้นเปลือง. Accountants will ask: "หมวดนี้ใช้ต้นทุนถัวเฉลี่ยหรือ FIFO?" |
| SMEsPlus candidate | Category tree for reporting is Inventory-owned; **valuation/costing policy ownership is a Joint Account × Inventory decision** (not decided here); policy change on a category with existing stock requires an effective date, an approval, and a valuation re-run record. |
| Evidence | CORR-007B `09` (Layer 1), `17` (remediation record); Reopen `08_FINANCIAL`, `13` C-05, `14`, `20`. Gate impact: `N-A12-01` remains `HIGH FUNCTIONAL DESIGN GAP — REOPENED`. |

### 3.9 Attributes — คุณลักษณะสินค้า (MENU-CF-10)

| Aspect | Content |
|---|---|
| Purpose | Define the axes (colour, size, material, capacity) whose value combinations create product variants. |
| Input | Attribute name, display type, values; variant creation mode (always / on demand / never). |
| Process | Assigning attributes to a product template generates (or lazily creates) variants; each variant is the stock-keeping unit. |
| Output | Variant grid. |
| Control / Accounting impact | Stock truth is per variant; valuation per variant; migration must preserve variant identity (attribute values, not display names). |
| Thai SME reading | สี, ไซซ์, ขนาดบรรจุ, รุ่น. |
| SMEsPlus candidate | `CONDITIONAL`; attribute values must be stable identities (code + Thai label); renaming a value must not change stock identity. |
| Evidence | `HOLD / EVIDENCE REQUIRED` — Reopen `02` item 2 explicitly "no dedicated variant evidence" (`GAP-MD-08`). |

### 3.10 Product Packagings — หน่วยบรรจุ / แพ็กสินค้า (MENU-CF-11)

| Aspect | Content |
|---|---|
| Purpose | Describe sellable/purchasable pack sizes (ลัง 12 ขวด, แพ็ก 6) so documents can be entered in packs while stock is counted in base units. |
| Input | Product, packaging name, quantity in base UoM, barcode, usable for sales / purchase. |
| Process | Entering "2 ลัง" on a document converts to 24 base units for stock; packaging barcode scan resolves product + quantity. |
| Output | Base-unit quantity on every movement; packaging shown on document. |
| Control / Accounting impact | None directly; valuation is per base unit. Risk: confusing packaging with UoM leads to double conversion. |
| Thai SME reading | ลัง / แพ็ก / โหล. |
| SMEsPlus candidate | `CONDITIONAL`; packaging is a display/entry convenience over base UoM; base unit is always the stock fact. Benchmark caveat: DR-002 found no dedicated packaging model in the studied source (packaging represented via unit records) — cited as a reason not to assume model shapes. |
| Evidence | Reopen `01` Part B (DR-002 summary), `05_IBPV` §3 note; `HOLD / EVIDENCE REQUIRED` for menu-level behaviour (`GAP-MD-18`). |

### 3.11 Reordering Rules — จุดสั่งซื้อ / กฎสั่งเติมสินค้า (MENU-CF-12)

See `12_REPLENISHMENT_REORDERING_SCHEDULER_MAP.md`. Summary: per product per location, minimum and maximum quantity (or forecast-based) plus preferred route; the scheduler proposes replenishment when forecast falls below minimum.

### 3.12 Barcode Nomenclatures — รูปแบบบาร์โค้ด (MENU-CF-13)

| Aspect | Content |
|---|---|
| Purpose | Tell the scanner how to interpret a barcode: plain product code, EAN-13, GS1 with embedded lot/expiry/quantity, weighted barcodes, internal location or package labels. |
| Input | Nomenclature name, ordered rules (pattern, type: product / lot / package / location / weight / price), GS1 application identifiers if used. |
| Process | On scan, the first matching rule parses the code into product + optional lot/qty/expiry and fills the move line. |
| Output | Parsed scan result. |
| Control / Accounting impact | None on valuation. Accuracy control: mis-parsed scans create wrong movements. |
| Thai SME reading | บาร์โค้ด EAN-13 จาก GS1 Thailand, บาร์โค้ดภายใน, บาร์โค้ดชั่งน้ำหนัก. |
| SMEsPlus candidate | `CONDITIONAL`; ship a default Thai retail nomenclature (EAN-13 + internal) and a GS1 nomenclature for lot/expiry industries; tenant edits are advanced. |
| Evidence | `HOLD / EVIDENCE REQUIRED` — never studied (`GAP-MD-19`). |

### 3.13 UoM Categories — กลุ่มหน่วยนับ (MENU-CF-14)

| Aspect | Content |
|---|---|
| Purpose | Group units that can convert to one another (unit ↔ dozen ↔ box; g ↔ kg; ml ↔ l) with one reference unit per group. |
| Input | Category, units, conversion factor to reference, rounding precision. |
| Process | Every quantity on a document is converted to the product's base unit for stock; purchase UoM may differ from stock UoM. |
| Output | Base-unit stock quantities; conversion audit. |
| Control / Accounting impact | Conversion and rounding feed valuation (Reopen `02` item 3: benchmark default rounding is "up", and factor edits are non-retroactive — historical continuity risk). |
| Thai SME reading | ชิ้น, โหล (12), กล่อง, ลัง, กิโลกรัม, ลิตร, เมตร, คู่. |
| SMEsPlus candidate | `MANDATORY`; Thai unit pack pre-loaded; conversion factors versioned with effective dates (no silent retroactive change); rounding policy explicit per unit; cross-category conversion forbidden. |
| Evidence | Reopen `02` item 3, `06_IDTM`. |

---

## 4. Configuration Gaps Carried

| Gap ID | Object | Gap | Owner | Gate impact |
|---|---|---|---|---|
| GAP-MD-14 | Settings | Feature-switch inventory and switch-off guards never mapped for SaaS provisioning (`SAAS-04`) | Track 05 / S5 | Team B precondition |
| GAP-MD-15 | Warehouses | Warehouse vs Thai tax branch labelling rule needs real-user validation (`GRPA-H8/H3` residue) | Track 02 / S8 | Team B precondition |
| GAP-MD-16 | Storage Categories | No prior evidence at all | Track 05 / S4 | Non-blocking (conditional feature) |
| GAP-MD-17 | Putaway Rules | No prior evidence; Product Category dual ownership unresolved | Track 05 / S4; Joint Session | Team B precondition |
| GAP-MD-08 | Attributes / Variants | No dedicated variant evidence | Track 04 / S2 | Team B precondition |
| GAP-MD-18 | Packagings | No menu-level evidence | Track 04 / S2 | Non-blocking |
| GAP-MD-19 | Barcode Nomenclatures | No prior evidence | Track 04 / S2 | Non-blocking |
| GAP-MD-13 | Product Categories | Valuation-policy ownership is a Joint Session decision; `N-A12-01` HIGH REOPENED; `C-05` re-audit pending | Track 06 / S6; Boss | **Blocks Joint Backbone publication** |
| U-01 | Locations | Warehouse-level authorization unknown | Track 07 | Team B precondition |

No configuration object above is approved as SMEsPlus design. This is the foundation reference for CP-03.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
