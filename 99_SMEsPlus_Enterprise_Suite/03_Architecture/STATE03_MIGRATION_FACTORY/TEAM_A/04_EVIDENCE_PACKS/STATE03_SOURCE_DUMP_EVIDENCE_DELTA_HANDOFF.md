# STATE03 — Source / Dump Evidence Delta Handoff

| Field | Value |
|---|---|
| ผู้จัดทำ | Source / Dump Deep Research Worker (Claude) — read-only |
| ผู้รับ | STATE03 session หลัก (Integration / Architecture Knowledge Owner) |
| วันที่ | 2026-09-30 (รอบที่ 1) |
| สถานะทุกรายการในเอกสารนี้ | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`** |
| ข้อจำกัดของเอกสารนี้ | ไม่ใช่ canonical register ; ไม่มี denominator ; ไม่แก้ FDS/Target Design ; ไม่เสนอ V-level ; **source/schema proof ไม่ใช่ runtime proof** |
| การเปลี่ยนสถานะ gap | **เสนอเท่านั้น** (ช่อง "Proposed disposition") — ไม่ได้แก้ `22_UNKNOWN_AND_GAPS.md` หรือ register ใด |

---

## 1. Provenance และกติกาที่ใช้

| รายการ | ค่า |
|---|---|
| Community source | `Odoo Community/odoo-19.0.post20260921/` (`PKG-INFO` Version `19.0.post20260921`) — อ่านทั้งหมด (read-only) |
| Custom / third-party trees | `addons_Extramodule/`, `addons_smeplus/`, `Extra_Module_scgl/` — **เปิด `__manifest__.py` ก่อนเสมอ** ; อ่านโค้ดเฉพาะ license `LGPL-3`, `AGPL-3`, `GPL-*` ; ข้ามโฟลเดอร์ `Claude outputs`, zip, `MODIFY`, `VAT_BACKFILL_20260914`, `AUDIT_LOG_20260914`, `.xlsx` |
| Dump (schema-only) | ไฟล์ `iTEST02_2026-06-14_14-41-19 (1).dump` ; sha256 `d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0` ; archive จาก PostgreSQL 18.4, format custom v1.16, สร้าง 2026-06-14 |
| วิธี restore | `pg_restore --schema-only --no-owner --no-privileges` (client 18.6) เข้า cluster ส่วนตัว localhost เท่านั้น ; เมตาดาต้าจำนวนแถวรวม = 0 ; ไม่มี `SELECT` จากตารางธุรกิจ (อ่านเฉพาะ `information_schema` / `pg_catalog`) |
| Restore ครั้งที่ 1 / 2 | ทำ 2 ครั้ง (ครั้งที่ 2 เพื่อตรวจร่องรอยโมดูล custom จากชื่อคอลัมน์) ; **ทั้งสองครั้งลบ DB `state03_schema_scratch` แล้ว** (ตรวจ `pg_database` = 0), หยุด server, ลบโฟลเดอร์ cluster |
| สิ่งที่ไม่ได้ commit | dump, DDL, SQL, ซอร์สโค้ด, raw extract, credentials — (ดู §6 เรื่องข้อยกเว้นในไฟล์รอบก่อน) |
| Restricted pointer | รูปแบบ `RESTRICTED:<tree>/<path>[:line]` สัมพัทธ์กับ `SOURCE_CODE/` ; ตัวอย่าง `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_account/models/mrp_production.py:57-94` ; hash ของ manifest ใช้ 16 ตัวแรกของ sha256 |

**Legend ระดับหลักฐาน (ไม่ใช่ Gate PASS):**
`SRC-STATIC` = อ่านโค้ดโดยตรง · `SRC+TEST` = อ่านโค้ด + unit test ที่มากับ source · `SCHEMA` = โครงสร้างจาก dump · `INFER` = ข้อสรุปจากการไล่โค้ด ไม่มี test/รันยืนยัน · `ABSENCE` = ผลค้นหาแบบไม่พบ (มั่นใจต่ำกว่าเชิงบวก)

## 2. Manifest / Provenance Inventory (โมดูล custom + third-party)

**ภาพรวม:** พบ manifest 221 ไฟล์ → 158 โมดูลไม่ซ้ำ (ซ้ำเพราะมีสำเนาในหลายโฟลเดอร์/ไฟล์แตกซิป).

| ประเภท license | จำนวนโมดูลไม่ซ้ำ | การจัดการ |
|---|---|---|
| LGPL-3 / AGPL-3 / GPL-3 (อ่านโค้ดได้) | 117 | อ่านเฉพาะส่วน override โมเดลหลักของบัญชี/สต็อก/MRP |
| OPL-1 | 24 | **บันทึกชื่อ+license เท่านั้น — ไม่อ่านโค้ด** |
| ไม่ระบุ license | 15 | **ไม่อ่านโค้ด** |
| Other proprietary | 2 | **ไม่อ่านโค้ด** |

**การจัดประเภท (อนุมานจากฟิลด์ `author` ใน manifest เท่านั้น — ต้องยืนยันโดย session หลัก):**

| ประเภท | สัญญาณ | ตัวอย่างโมดูลที่เกี่ยวข้อง |
|---|---|---|
| Company Custom | author = SMEsPlus | `smesplus_account` (version ใน manifest = **17.0.1.0.0**, license LGPL-3), `smesplus_tax_period_date`, `smesplus_inventory_lot_filter`, `smesplus_account_reports` |
| Customer Custom | author = SCG Legacy / SCGL / BHPRO | `scgl_account_deferred`, `scgl_account_reconcile`, `scgl_tax_period_date`, `scgl_account_tax_return`, `scgl_stock_performance`, `scgl_inventory_lot_filter`, `bh_parent_company`, `bh_purchase_receipt_all`, `courier_type` |
| Third-party (OCA / vendor) | author = OCA, Cybrosys, Odoo Mates, Ecosoft, ForgeFlow, SuitePark ฯลฯ | `account_lock_date_update`, `account_fiscal_year`, `base_accounting_kit`, `om_fiscal_year`, `cr_effective_date_entries`, `purchase_request`, `l10n_th_withholding_tax*`, `account_asset_management` |
| Enterprise (ไม่มีโค้ดใน tree) | ตารางในฐาน + `depends` | `account_accountant` (Enterprise) เป็น dependency ของ `smesplus_account`, `smesplus_advance_expense_request`, `scgl_advance_expense_request` ; ฐาน iTEST02 มีโครงสร้างของ MPS, Quality, Assets ฯลฯ |

**โมดูลที่ license เป็น OPL-1/ไม่ระบุ แต่ depends บนโมเดลหลัก (ยังตรวจ override ไม่ได้ → เป็นเหตุของ CONDITIONAL):**
`19_bhpro_master_data` (OPL-1; depends mrp, purchase_stock, stock, stock_account), `19_bhpro_inventory` (OPL-1; stock), `import_bridge_axis` (OPL-1; account, mrp, stock), `d_tiktok_shop_connector` (OPL-1; stock_account), `d_product_brand_stock` (OPL-1; stock), `account_discount_catalog` (OPL-1; account), `product_stock_equipment` (ไม่ระบุ; stock), `bi_print_journal_entries` (ไม่ระบุ; account), `scgl_product_image`/`smesplus_product_image` (ไม่ระบุ; account, stock)
> โมดูลกลุ่มนี้เปิดถึงระดับ manifest (license/depends) เท่านั้น — ไม่มีการอ่านโค้ด

### 2.1 Override ของโมเดลหลักในโมดูลที่อ่านได้ (45 โมดูล inherit โมเดลหลัก)

ตรวจ `_inherit` ต่อโมเดล {account.move/line, stock.move/line/picking/location/quant, mrp.production/bom/workorder, res.company, product.*, account.account, stock.landed.cost, lock exception ฯลฯ} และการ override เมธอดที่เกี่ยวกับ **lock date / valuation / posting / MRP cost**.

| โมดูล | license | โมเดลหลักที่ inherit | override เมธอดอ่อนไหว | ผลต่อ finding |
|---|---|---|---|---|
| `base_accounting_kit` (Cybrosys; hash `47f87e3a576ae149`) | LGPL-3 | res.company, account.move/line/journal ฯลฯ | **`res.company._validate_locks`** — เรียก super แล้วตรวจซ้ำ (draft entries + unreconciled statement lines) → **เพิ่มความเข้ม ไม่ลดความเข้ม** | ไม่ทำให้ PCO-01 ผิด ; ทำซ้ำการตรวจเดิม |
| `account_lock_date_update` (OCA; hash `249a2c385ba3dfae`) | AGPL-3 | res.company | ไม่ override เมธอดอ่อนไหว (แก้เฉพาะ action redirect) + **wizard ตั้ง lock date** (เฉพาะ Adviser/admin, ห้ามวันอนาคต, เขียนผ่าน `company.write`) | เพิ่มช่องทาง UI ตั้ง lock ; ผ่าน validation เดิมของ core (INFER: `write` เรียก `_validate_locks`) |
| `smesplus_account` (hash `38dca86e151f7c7b`) | LGPL-3 | account.move/line/journal/account | `account.move._post` (บันทึกผู้/เวลาโพสต์ + สร้าง deferred entries) | เพิ่มพฤติกรรมหลังโพสต์ ; เรียก super ก่อน |
| `scgl_account_deferred` (hash `36b5a87126b723b7`) | LGPL-3 | account.move/line, res.company | `account.move._post` (สร้าง deferred เมื่อโหมด `on_post`), `button_draft/cancel` (ยกเลิก schedule) | เช่นเดียวกัน |
| `purchase_request` (OCA; hash `9fe183e179afa913`) | LGPL-3 | stock.move/line/picking/rule/warehouse.orderpoint | `stock.picking._action_done`, `stock.move.line._action_done` | เกี่ยวข้อง BRP-07 (เพิ่มเส้นทาง Reordering→ใบขอซื้อ) ; **ไม่ได้ตรวจเชิงลึกว่าสร้างเอกสารสถานะใด** |
| `cr_effective_date_entries` (SuitePark; hash `2026ab6dabc062d1`) | AGPL-3 | stock.picking | wizard เปลี่ยน "วันที่มีผล" ของ picking: reset-to-draft + โพสต์ใหม่รายการบัญชี, เปลี่ยนวันที่ move/move line, **อ้างโมเดล `stock.valuation.layer` และฟิลด์ `stock_move_id` ที่ไม่มีใน Odoo 19** (ตามโครงสร้างฐานและ source) | **ความเสี่ยง (SRC-STATIC):** ออกแบบสำหรับ Odoo รุ่นเก่ากว่า ; ทางที่อ้างโมเดลไม่มีอยู่จะล้มเหลวเมื่อรันบน 19 ; และเป็นช่องทาง "เปลี่ยนวันที่ย้อนหลัง" ที่ต้องพิจารณาร่วม lock date/Stock Closing |
| `scgl_tax_period_date` / `smesplus_tax_period_date` (hash `d0b42916cef1b3bf` / `c577a7002f4465df`) | LGPL-3 | account.move/line | `account.move.create` (ตั้งค่างวดภาษี) | ไม่พบการแตะ lock ; ไม่ได้ตรวจเชิงลึก |
| `bh_parent_company` (hash `18c6500d7ce8b83e`) | LGPL-3 | (multi-company / partner) | — | **มีร่องรอยในฐานทดสอบ** (ผลเป็นกลาง ไม่ระบุโครงสร้าง) ; เกี่ยวข้อง multi-company ; ยังไม่ได้ตรวจ record rule |
| `account_fiscal_year` (OCA) / `om_fiscal_year` (Odoo Mates) | AGPL-3 / LGPL-3 | res.company | — | ปีบัญชี ; ไม่แตะ lock ; ฐานทดสอบมีโครงสร้างปีบัญชี (ไม่ระบุได้ว่ามาจากโมดูลใด) |

**ไม่พบ override** (ในโมดูลที่ license เปิด) ของ: `_cal_price`, `_set_value`, `_get_value_data`, `_should_create_account_move`, `_get_account_move_line_vals`, `action_close_stock_valuation`, `_compute_bom_price`, `_check_byproducts`, `_check_fiscal_lock_dates`, `_get_lock_date_violations`, `_get_accounting_date`, และไม่พบโมดูลที่ inherit `mrp.production`, `mrp.bom`, `mrp.bom.byproduct`, `mrp.workorder`, `mrp.workcenter`, `stock.landed.cost` (`ABSENCE` — จำกัดเฉพาะโมดูลที่อ่านได้)

### 2.2 ร่องรอยการติดตั้งจาก schema (iTEST02, 2026-06-14) — SCHEMA-ONLY (data-minimized)
- **มีร่องรอยของโมดูล custom/third-party บางตัว** (ระบุได้เฉพาะระดับ: โมดูลผู้ปกครองบริษัท `bh_parent_company`, ใบขอซื้อ `purchase_request`, ภาษีหัก ณ ที่จ่าย) — ไม่ระบุชื่อตาราง/คอลัมน์
- **ไม่พบร่องรอย ณ วัน dump** ของโมดูลบัญชี `smesplus_*`, `scgl_*`, `cr_effective_date_entries`, `base_accounting_kit` — **การไม่พบไม่พิสูจน์ว่าโมดูลไม่ได้ติดตั้งหรือไม่มีผลพฤติกรรม** (โมดูลที่ไม่เพิ่มโครงสร้างตรวจไม่ได้)
- ⚠️ ชุดโมดูลที่ติดตั้งจริงอยู่ในข้อมูล (ไม่ได้ดึง) → ไม่สามารถยืนยัน effective installed extension set ; ข้อสรุปทุกข้อจึง `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`

---

## 3. รายการ Delta ต่อ Function / Gap

> ทุกรายการ: สถานะ = `SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` · Community-core finding = `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` · manifest/override status อ้างอิง §2.1 (ไม่พบ override ที่เกี่ยวข้องในโมดูล license เปิด ; OPL-1/ไม่ระบุ license ยังตรวจไม่ได้) · schema-only = ยืนยันเฉพาะที่ระบุ · ไม่ใช่ runtime proof
> Restricted evidence pointer ระดับ file+line อยู่ในไฟล์ `SRC_*` ที่ระบุ (โฟลเดอร์ pilot ที่เกี่ยวข้อง) — ไฟล์เหล่านั้นถูกสร้างก่อนกติกาใหม่ จึงต้อง **อ่านร่วมกับ §6 (relabel)**

### D-01 — GAP-BRP-09 / BRP-F08 (By-Products cost allocation)
| Field | รายละเอียด |
|---|---|
| Prior claim | `EV-BRP-13/14` (marketplace/forum, pre-19): ไม่ปันต้นทุนให้ by-product โดยปริยาย — Open/Conditional, V1 |
| Finding | Community มีฟิลด์ "Cost Share (%)" ต่อบรรทัด By-Product (ผู้ใช้ตั้งเอง) ; ตอนผลิตแต่ละรอบ: By-Product (FIFO/AVCO) = ต้นทุนรวม×%÷จำนวน, สินค้าหลัก = ต้นทุนรวม×(1−Σ%)÷จำนวน ; % = 0 ⇒ By-Product มูลค่า 0 (INFER) ; Standard-cost By-Product ใช้ราคามาตรฐานของตัวเอง ขณะสินค้าหลัก FIFO ยังถูกหัก % ; Landed cost ตัด By-Product ที่ % = 0 ; ตรวจ: ไม่ติดลบ, ผลรวม ≤ 100 (BoM/MO) |
| Classification | Community |
| Provenance / pointer | `RESTRICTED:Odoo Community/…/odoo/addons/mrp_account/models/mrp_production.py:57-94`, `mrp_account/models/product.py:63-99`, `mrp/models/mrp_bom.py:198-210,871-874`, `mrp/models/mrp_production.py:979-985`, `mrp_landed_costs/models/stock_landed_cost.py:23-28` ; ไฟล์: `MANUFACTURING_BOM_ROUTING_PILOT/SRC_GAP-BRP-09_*` |
| Manifest / override | ไม่พบ override ของ `_cal_price`/`_check_byproducts` ในโมดูล license เปิด ; OPL-1 (`19_bhpro_master_data`, `import_bridge_axis`) ตรวจไม่ได้ |
| Schema-only | ผลเป็นกลาง: โครงสร้างในฐานทดสอบสอดคล้องกับสิ่งที่ source ระบุเรื่องอัตราส่วนต้นทุนผลผลิตรอง ; **ไม่พบตัวควบคุมระดับฐานข้อมูลสำหรับกฎของอัตราส่วนนี้** ⇒ กฎอยู่ที่ชั้นแอป (ไม่ระบุชื่อตาราง/คอลัมน์ตามกติกา data-minimization) |
| Actual evidence level | `SRC+TEST` (test ของ Odoo ยืนยันตัวเลข ยกเว้นกรณี % = 0 → มูลค่า 0 เป็น `INFER`) + `SCHEMA` |
| Contradiction / limitation | ขัดกับ candidate default เดิมในแง่ "เป็นกฎของระบบ" (ผลที่ % = 0 ตรงกับข้อความเดิม) ; ไม่ได้รัน ; Unbuild/Subcontract/แก้ % หลังปิด ยังไม่ทราบ |
| Required runtime validation | AWT: MO มี By-Product (FIFO/AVCO/Standard ผสม, % = 0, Σ% < 100), backorder, unbuild |
| Proposed disposition (session หลักตัดสิน) | สถานะ gap → "มี source/schema finding รอการตรวจอิสระ" ; **ไม่ถือว่าปิด** |
| Neutral sanitized conclusion | ระบบมีตัวแปร "สัดส่วนต้นทุนของผลผลิตรอง (%)" ที่ผู้ใช้กำหนดต่อรายการ ; สินค้าหลักรับส่วนที่เหลือ ; ไม่กำหนด = ผลผลิตรองมูลค่าศูนย์ ; ไม่มีการเตือนและไม่มีข้อจำกัดระดับฐานข้อมูล → ข้อมูลย้ายเข้าต้องนำเข้าค่านี้อย่างชัดเจน |

### D-02 — GAP-MFG-02 (บัญชีการผลิตไม่ได้ตั้ง)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN: blocked / defaulted / silent |
| Finding | รายการบัญชีของ stock move สร้างเมื่อ: storable ∧ valued ∧ location ฝั่งใดฝั่งหนึ่งมีบัญชี ∧ qty≠0 ∧ valuation=real-time ; ไม่ตั้ง = **ไม่สร้างรายการ ไม่มี error/warning** ; แรงงาน (Labour) ข้ามเงียบเช่นกัน ; ไม่พบ default ในแม่แบบผังบัญชีไทยหรือ data file |
| Classification | Community |
| Pointer | `RESTRICTED:…/stock_account/models/stock_move.py:193-215,659-666` · `stock_account/models/stock_location.py:11-14` · `stock_account/views/stock_location_views.xml:10-15` · `mrp_account/models/mrp_production.py:101-105` · `l10n_th/models/template_th.py:8-45` ; ไฟล์: `MANUFACTURING_VALUATION_PILOT/SRC_GAPS_MFG-02-03-04-05_*` |
| Manifest / override | ไม่พบ override ของ `_should_create_account_move`/`_create_account_move` ในโมดูล license เปิด |
| Schema-only | ผลเป็นกลาง: มีโครงสร้างรองรับการผูกบัญชีกับพื้นที่จัดเก็บ ; ค่าตั้งจริงอยู่ในข้อมูล — ไม่ได้ตรวจ |
| Evidence level | `SRC-STATIC` + `INFER` (การแยก subledger–GL) + `SCHEMA` |
| Limitation | "ไม่มี default ใน source" ≠ "ฐานลูกค้าไม่ได้ตั้ง" ; ไม่ได้รัน |
| Runtime validation | ผลิต MO โดยไม่ตั้งบัญชี ตรวจว่ามี/ไม่มีรายการบัญชี |
| Proposed disposition | มี finding รอตรวจอิสระ |
| Neutral conclusion | การตั้งบัญชีของพื้นที่ผลิตเป็นเงื่อนไขให้เกิดรายการบัญชีการผลิต ; ถ้าไม่ตั้ง ระบบไม่ฟ้องและไม่ลงบัญชี → ต้องมี checklist การตั้งค่าก่อนใช้งาน |

### D-03 — GAP-MFG-03 (ผลิตบางส่วน / Backorder)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN |
| Finding | ต้นทุนคำนวณทุกรอบที่โพสต์ = วัตถุดิบที่ใช้จริงรอบนั้น + ต้นทุน Work Center + Extra Unit Cost×จำนวนรอบนั้น ; Extra Unit Cost คัดลอกไป Backorder ; แรงงานลงบัญชีครั้งเดียวเมื่อ MO ปิด (test ยืนยัน ไม่ซ้ำ) ; Work Order ไม่มีเวลาจริง = ใช้เวลาคาดหมาย |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp/models/mrp_production.py:1907-1955,1938-1947` · `mrp_account/models/mrp_production.py:57-99,141-144` · `mrp_account/tests/test_valuation_operation.py:13-47` · `mrp_account/tests/test_mrp_account.py:603-648` |
| Manifest / override | ไม่พบ override `_post_inventory`/`_cal_price` ในโมดูล license เปิด ; `mrp_subcontracting_account` (Community) ปรับ `_cal_price` สำหรับ subcontract |
| Schema-only | ผลเป็นกลาง: โครงสร้างสอดคล้องกับ source เรื่องต้นทุนเพิ่มต่อหน่วยระดับคำสั่งผลิต |
| Evidence level | `SRC+TEST` |
| Limitation | การแบ่งเวลา Work Order ระหว่าง MO เดิม/Backorder ยังไม่ทราบ |
| Runtime validation | ผลิตบางส่วนหลายรอบพร้อม Work Order และตรวจต้นทุนต่อรอบ |
| Proposed disposition | มี finding รอตรวจอิสระ |
| Neutral conclusion | ต้นทุนของงานผลิตบางส่วนคิดเป็นรอบตามวัตถุดิบที่ใช้จริงในรอบนั้น ; ต้นทุนแรงงานรับรู้เมื่อปิดคำสั่งผลิต |

### D-04 — GAP-MFG-04 และ GAP-BRP-04 (อัตราต้นทุน Work Center)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN: time-based variation / rate mechanics |
| Finding | อัตราเป็นตัวเลขเดียวต่อชั่วโมงต่อ Work Center ; ไม่มีอัตรากะ/OT ใน Community ; Work Order เก็บ snapshot อัตราตอนเสร็จ (test ยืนยัน ต้นทุน MO ที่ปิดไม่เปลี่ยนเมื่อแก้อัตรา) ; เลือกคิดจากเวลาจริงหรือเวลาตามทฤษฎีต่อ Operation ; ไม่มี Overhead rate แยก (มี Extra Unit Cost ต่อ MO) ; ไม่พบฟิลด์ต้นทุนพนักงานใน Community ; แรงงานลงบัญชี Dr บัญชีผลิต / Cr บัญชีค่าใช้จ่าย |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp/models/mrp_workcenter.py:41-43` · `mrp/models/mrp_workorder.py:124-130,638-654,729,900-902` · `mrp/models/mrp_routing.py:60-64,134-136` · `mrp_account/models/mrp_production.py:110-139` · `mrp_account/tests/test_mrp_account.py:576-588` |
| Manifest / override | ไม่พบโมดูล license เปิดที่ inherit `mrp.workcenter`/`mrp.workorder` ; ฐานมีโครงสร้างต้นทุนพนักงานของโมดูลนอก Community (ตารางพนักงานต่อ Work Order) ที่ตรวจโค้ดไม่ได้ |
| Schema-only | ผลเป็นกลาง: โครงสร้างสอดคล้องกับ source เรื่องอัตราต้นทุนและโหมดคิดต้นทุน ; **ไม่พบโครงสร้างอัตราแยกตามกะ/ล่วงเวลาในฐานทดสอบ** ; พบโครงสร้างต้นทุนพนักงานจากโมดูลนอก Community |
| Evidence level | `SRC+TEST` + `SCHEMA` |
| Contradiction / limitation | ฐานทดสอบมีโครงสร้างต้นทุนพนักงานจากโมดูลนอก Community ⇒ "ไม่มีต้นทุนพนักงาน" เป็นจริงเฉพาะ Community |
| Runtime validation | ตรวจการคิดต้นทุนเมื่อมีโมดูลพนักงานร่วม |
| Proposed disposition | มี finding รอตรวจอิสระ (มีเงื่อนไขโมดูลนอก Community) |
| Neutral conclusion | อัตราต้นทุนศูนย์งานเป็นค่าเดียว ล็อกเมื่อเสร็จงาน ; ความผันแปรตามกะ/พนักงานไม่อยู่ในแกน Community |

### D-05 — GAP-MFG-05 (WIP interim entry reversal)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN: ย้อนอัตโนมัติเมื่อ MO เสร็จหรือไม่ |
| Finding | ตัวช่วย WIP สร้างรายการ WIP และรายการกลับรายการพร้อมกัน วันย้อนกลับ default = วันถัดไป (ต้องหลังวันที่ลงบัญชี) ; ไม่มีโค้ดที่ผูกการย้อนกับการปิด MO ; วัตถุดิบใน WIP ใช้ราคามาตรฐานปัจจุบัน ; แก้ไขบรรทัดได้ก่อนยืนยัน |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp_account/wizard/mrp_wip_accounting.py:46-146` · `mrp_account/tests/test_mrp_account.py:360-510` |
| Manifest / override | ไม่พบโมดูล license เปิดที่ inherit ตัวช่วย WIP |
| Schema-only | ผลเป็นกลาง: มีโครงสร้างรองรับตัวช่วย WIP และการผูก WIP กับคำสั่งผลิต ; บริษัทมีการตั้งค่าบัญชี WIP |
| Evidence level | `SRC+TEST` + `SCHEMA` |
| Contradiction | ขัดกับข้อความ "(implied) reversed once the MO actually completes" ใน `MFG-F03` |
| Runtime validation | โพสต์ WIP → ปิด MO ก่อน/หลังวันย้อน ตรวจการนับซ้ำ |
| Proposed disposition | มี finding รอตรวจอิสระ ; เสนอแก้ถ้อยคำ `MFG-F03` |
| Neutral conclusion | รายการ WIP ระหว่างงวดย้อนกลับตามวันที่ผู้ใช้กำหนด ไม่ใช่ตามสถานะคำสั่งผลิต |

### D-06 — GAP-MFG-01 / MFG-F05 และห่วงโซ่ Valuation Timing (Step 1–6), GAP-PCO-02
| Field | รายละเอียด |
|---|---|
| Prior claim | `Material Finding — Independently Unverified` (Matrix Step 1–6) ; MFG-F05 (ติดลบ/revaluation) |
| Finding | (1) ค่าเริ่มต้นหมวดสินค้า/บริษัท = Periodic + Standard (2) รายการบัญชีเกิดจาก 3 เหตุการณ์: Vendor Bill (บรรทัดสินค้า storable ตั้งบัญชีสต็อกโดยตรง), Customer Invoice (บรรทัด COGS), stock move ที่ location มีบัญชี (UI แสดงฟิลด์เฉพาะ Production/Inventory) (3) การรับ/ส่งกับ Supplier/Customer ไม่สร้างรายการตอน move ในการตั้งค่า UI ปกติ (`INFER`) (4) มูลค่า move เก็บที่ stock move และปรับเมื่อบิลโพสต์; มูลค่ารวมสินค้าคำนวณสดจากจำนวนคงเหลือ (5) Stock Closing ปรับผลต่างสะสมระหว่าง subledger–GL — Manual (default) หรืออัตโนมัติรายวัน/รายเดือน (cron) ; **ไม่ใช่รายการกลับรายการ** ; Accrued Orders / WIP เป็นกลไกแยกที่มี Reversal Date (6) ไม่พบโค้ด revaluation รายการชื่อ "negative inventory" (`ABSENCE`) |
| Classification | Community (บริษัทลูกค้าอาจตั้งค่าเพิ่มเอง) |
| Pointer | `RESTRICTED:…/stock_account/data/stock_account_data.xml:4-18` · `stock_account/models/res_company.py:19-36,49-135,137-150,238-272` · `stock_account/models/account_move.py:29-44,68-161` · `stock_account/models/account_move_line.py:13-35` · `stock_account/models/stock_move.py:177-250,292-448,659-666` · `purchase_stock/models/stock_move.py:157-243` · `account/wizard/accrued_orders.py:378-389` ; ไฟล์: `MANUFACTURING_VALUATION_PILOT/SRC_GAP-MFG-01_*` |
| Manifest / override | ไม่พบ override เมธอดหลักของ valuation ในโมดูล license เปิด ; **`cr_effective_date_entries` (จัดการวันที่ picking ย้อนหลังและอ้างโมเดลรุ่นเก่า)** เป็นช่องทางที่อาจกระทบจังหวะ ; โมดูล OPL-1 ที่ depends `stock_account` (`d_tiktok_shop_connector`, `19_bhpro_master_data`) ตรวจไม่ได้ |
| Schema-only | ผลเป็นกลาง: ไม่พบโครงสร้างของแบบจำลองมูลค่ารุ่นเก่าแบบแยกชั้น ; พบโครงสร้างมูลค่าที่เก็บระดับรายการเคลื่อนไหว ; บริษัทมีการตั้งค่ารอบปิดสต็อก/โหมดมูลค่า/วิธีต้นทุน ; **ไม่พบ trigger ที่ผู้ใช้สร้าง** — **ต้อง requalify (§R) ; การไม่พบโครงสร้างไม่พิสูจน์การไม่มีอยู่** |
| Evidence level | `SRC-STATIC` + `INFER` (Step 1/3 และการแยกชั้น) + `SCHEMA` — ไม่ใช่ runtime |
| Contradiction / limitation | Step 1 ขัดกับ source (ไม่ใช่แค่ไม่ครบ) ; Step 3 มีเงื่อนไขบัญชี Loss Account ; Step 4 เรื่อง "self-reversing" ใช้กับ Accrued Orders/WIP ไม่ใช่ Stock Closing ; เอกสารนี้ **ไม่เปลี่ยนสถานะ Independently Unverified** |
| Required runtime validation | AWT: รับสินค้าจาก Supplier ก่อน/หลังบิล, ส่งสินค้าก่อน/หลัง invoice, ปรับสต็อกมี/ไม่มี Loss Account, Stock Closing ทั้ง Manual/Cron |
| Proposed disposition | ส่งเป็นหลักฐานเพิ่มให้ CHATGPT_AUDIT/Boss ; session หลักตัดสินการ reconcile |
| Neutral conclusion | มูลค่าสต็อกมีสองชั้น (รายการเคลื่อนไหวกับบัญชีแยกประเภท) ; รายการบัญชีสต็อกผูกกับเอกสารการเงินและการปิดสต็อก ไม่ใช่ทุกการเคลื่อนไหวทางกายภาพ ; ต้องกำหนดนโยบายและวินัยการปิดสต็อก |

### D-07 — GAP-PCO-01 (การแก้ไขหลัง Hard Lock) — **ถึง natural checkpoint**
| Field | รายละเอียด |
|---|---|
| Prior claim | ไม่มีกลไกแก้ไขที่มีเอกสารรองรับหลัง Hard Lock |
| Finding | Lock date 5 ชนิด: Global, Tax, Sales, Purchase (soft) และ Hard ; **Hard Lock ลดหรือลบไม่ได้ และไม่มี exception** ; ห้ามเพิ่ม/แก้รายการที่ลงวันที่ ≤ Global Lock (ข้ามได้ด้วย Lock Exception) หรือ ≤ Hard Lock (ข้ามไม่ได้) — `UserError` ; รายการใหม่ที่ลงวันที่ในช่วงล็อกถูก **เลื่อนไปวันแรกที่เปิด** ตอนสร้าง/โพสต์ ; วิธีแก้ = สร้างรายการแก้ไข/กลับรายการลงวันที่หลัง lock (ฟอร์มกลับรายการมีฟิลด์วันที่) ; Soft lock ข้ามได้ด้วย "Lock Exception" (ต่อผู้ใช้/ทั้งหมด, จำกัดเวลา, มีเหตุผล, ยกเลิกได้เฉพาะ Adviser, มี audit trail) ; ตอนตั้ง lock: ห้ามมี draft entries ใน Hard Lock และห้ามมี bank statement line ที่ยังไม่กระทบยอดถึง Global/Hard Lock  |
| Classification | Community + Third-party overlay |
| Pointer | `RESTRICTED:…/account/models/company.py:51-112,552-606,642-700` · `account/models/account_move.py:2823-2840,3826-3829,5700-5706,6714-6750` · `account/models/account_lock_exception.py:1-120,115-118` · `account/wizard/account_move_reversal.py:17,93-106` ; overlay: `RESTRICTED:Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_lock_date_update/models/res_company.py`, `…/wizards/account_update_lock_date.py:49-82` ; `RESTRICTED:addons_Extramodule/base_accounting_kit-19.0.3.3.1/base_accounting_kit/models/res_company.py:80-123` |
| Manifest / override | `account_lock_date_update` (OCA, AGPL-3, depends `account`) — wizard เท่านั้น ; `base_accounting_kit` (Cybrosys, LGPL-3) — `_validate_locks` เพิ่มการตรวจซ้ำ ไม่ลดความเข้ม ; **ไม่พบโมดูล license เปิดที่ override `_check_fiscal_lock_dates`/`_get_lock_date_violations`/`_get_accounting_date`** ; Enterprise ฐานมีตารางตัวช่วยเปลี่ยน lock date (ไม่มีโค้ดใน tree) ; OPL-1/ไม่ระบุ license ที่ depends `account` ตรวจไม่ได้ |
| Schema-only | ผลเป็นกลาง: บริษัทมีการตั้งค่า lock date ; การควบคุมความถูกต้องระดับฐานข้อมูลของหัวรายการบัญชีไม่พบ ; ไม่พบ trigger ⇒ การล็อกงวดอยู่ที่ชั้นแอป ; การนำเข้าข้ามชั้นแอปอาจข้ามการล็อก (ยังไม่ทดสอบ) |
| Evidence level | `SRC-STATIC` (ไม่มี test ที่อ่านในรอบนี้) + `SCHEMA` |
| Contradiction / limitation | ยังไม่ยืนยัน: วันที่กลับรายการที่อยู่ในช่วงล็อกถูกเลื่อนอัตโนมัติหรือถูกปฏิเสธ (มีทั้งเส้นทางเลื่อนตอนโพสต์และ `UserError` ตอนแก้) ; กลไก hash/inalterable กับ lock ; การทำงานของ wizard ของ Enterprise ; ผลต่อ subledger (Stock Closing) |
| Required runtime validation | ตั้ง Hard Lock → พยายามแก้/กลับรายการ/โพสต์ย้อนหลัง → สังเกต `UserError` หรือการเลื่อนวันที่ ; ตรวจกับโมดูลที่ติดตั้งจริง |
| Proposed disposition | มี finding รอตรวจอิสระ |
| Neutral conclusion | หลังล็อกถาวร ข้อผิดพลาดแก้ผ่านรายการใหม่ลงวันที่หลังล็อกเท่านั้น ; ล็อกแบบยืดหยุ่นมีกลไกยกเว้นที่มีผู้อนุมัติ/เวลา/เหตุผล ; การควบคุมอยู่ที่ชั้นแอป ไม่ใช่ฐานข้อมูล |

### D-08 — GAP-BRP-01 (เปลี่ยนชนิด BoM หลังถูกใช้)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN: ล็อกหรือไม่ |
| Finding | ไม่มีการล็อก/constraint ; มีเพียงคำเตือนบน UI เมื่อแก้โครงสร้าง Kit ที่เคยใช้ ; test: ใบส่งของยืนยันแล้ว → เปลี่ยนเป็น Kit → Validate = แตกเป็นส่วนประกอบและลงบัญชีที่ส่วนประกอบ ; ชนิดไม่อยู่ในรายการฟิลด์ที่ทำให้ MO ติดธง "BoM ล้าสมัย" |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp/models/mrp_bom.py:26-29,212-221,268-275,487-515` · `mrp/models/stock_move.py:376-407` · `mrp_account/tests/test_mrp_account.py:169-207` ; ไฟล์: `MANUFACTURING_BOM_ROUTING_PILOT/SRC_GAPS_BRP-01-02-04-05-07-08-10_*` |
| Manifest / override | ไม่พบโมดูล license เปิดที่ inherit `mrp.bom` |
| Schema-only | ผลเป็นกลาง: ชนิด BoM ไม่มีตัวควบคุมระดับฐานข้อมูล |
| Evidence level | `SRC+TEST` + `SCHEMA` |
| Limitation | ผลต่อ MO ที่ Confirm แล้วยังไม่ทราบ |
| Runtime validation | สลับชนิดขณะมี SO/DO/MO เปิด |
| Proposed disposition | มี finding รอตรวจอิสระ |
| Neutral conclusion | ชนิด BoM แก้ได้ตลอดโดยไม่มีตัวล็อก และกระทบวิธีรับรู้บัญชีของเอกสารที่ยังไม่ปิด → ต้องมีนโยบายห้ามสลับขณะมีเอกสารเปิด |

### D-09 — GAP-BRP-02 (Kit + Operations)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN: hybrid case |
| Finding | ไม่มี constraint ห้าม Kit มี Operations ; ขาย/ส่ง Kit = แตกเป็นส่วนประกอบ ไม่ใช้ Operations ; ใช้ Kit เป็นส่วนประกอบของสินค้าผลิต = Operations ของ Kit กลายเป็น Work Order ของ MO แม่ (test) ; Kit มูลค่าสต็อก = 0 |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp/models/mrp_production.py:606-661,1347-1348` · `mrp/tests/test_bom.py:2872-2917` · `mrp_account/models/product.py:101-112` |
| Manifest / override | ไม่พบโมดูล license เปิดที่ inherit `mrp.bom`/`mrp.production` |
| Schema-only | ผลเป็นกลาง: ไม่พบตัวควบคุมระดับฐานข้อมูลที่เชื่อมชนิด BoM กับขั้นตอนผลิต |
| Evidence level | `SRC+TEST` |
| Runtime validation | Kit ที่มี Operations ทั้งกรณีขายตรงและเป็นส่วนประกอบ |
| Proposed disposition | มี finding รอตรวจอิสระ |
| Neutral conclusion | Operations ของ Kit มีผลเฉพาะเมื่อ Kit เป็นส่วนประกอบของสินค้าที่ผลิต |

### D-10 — GAP-BRP-05 (ไม่มี Work Order / ส่วนต่างเวลา)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN |
| Finding | BoM ไม่มี Operations → ไม่มี Work Order, ไม่มีต้นทุนแรงงาน ; Work Order เก็บเวลาคาดหมาย–จริงและ % ส่วนต่าง ; ไม่พบรายการบัญชีส่วนต่างเวลา (`ABSENCE`) ; ปิด MO เวลา 0 → ใช้เวลาคาดหมาย |
| Classification | Community |
| Pointer | `RESTRICTED:…/mrp/models/mrp_workorder.py:347-355,940-945` · `mrp/models/mrp_production.py:1938-1947` |
| Manifest / override | ไม่พบ override ; **ฐานมีตารางของ Work Order ขั้นสูง (นอก Community)** |
| Schema-only | ผลเป็นกลาง: โครงสร้างสอดคล้องกับ source เรื่องเวลาคาดหมาย/จริง/ส่วนต่าง |
| Evidence level | `SRC-STATIC` + `ABSENCE` + `SCHEMA` |
| Neutral conclusion | ส่วนต่างเวลาเป็นข้อมูลรายงานระดับ Work Order ไม่ใช่รายการบัญชี ; ถ้าไม่บันทึกเวลาจริง ระบบใช้เวลาคาดหมาย |

### D-11 — GAP-BRP-07 (Reordering Rule มีเกตอนุมัติหรือไม่)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN |
| Finding | Trigger Auto รันโดย scheduler รายวันด้วยผู้ใช้ระบบ ไม่มีขั้นตอนอนุมัติก่อนสร้าง ; เอกสารที่สร้างเป็น RFQ ร่าง ; MO ที่มีส่วนประกอบจากกฎนี้ไม่ถูกยืนยันอัตโนมัติ ; ล้มเหลว → กิจกรรมเตือน ; สิทธิ์: ผู้ใช้คลังอ่านอย่างเดียว ผู้จัดการแก้ได้ |
| Classification | Community + Third-party overlay (`purchase_request` ขยายเส้นทางจัดหา) |
| Pointer | `RESTRICTED:…/stock/models/stock_orderpoint.py:31-32,712-793` · `stock/data/stock_sequence_data.xml:45-56` · `mrp/models/stock_rule.py:35-38,117-121` · `purchase/models/purchase_order.py:111` · `stock/security/ir.model.access.csv:19-20` |
| Manifest / override | `purchase_request` (OCA) inherit `stock.warehouse.orderpoint`/`stock.rule` — **ยังไม่ได้ตรวจว่าเปลี่ยนสถานะเอกสารที่สร้าง** ; ฐานมีร่องรอยการติดตั้ง |
| Schema-only | ผลเป็นกลาง: โครงสร้างรองรับโหมดทริกเกอร์และการเลื่อนของ Reordering Rule ; มีข้อจำกัดความไม่ซ้ำระดับฐานข้อมูล ; ผลนี้ **CONDITIONAL ต่อ `purchase_request`** |
| Evidence level | `SRC-STATIC` + `SCHEMA` |
| Limitation | เงื่อนไขนี้ **CONDITIONAL ต่อ `purchase_request`** ที่ติดตั้งในฐาน |
| Neutral conclusion | เกตของการจัดหาอัตโนมัติอยู่ที่การยืนยันเอกสารร่าง ไม่ใช่ก่อนสร้าง |

### D-12 — GAP-BRP-08 (MPS) และ GAP-QCP-02 (Quality) — ขอบเขตโมดูล
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN (MPS feeds ?) / Open (Quality financial impact) |
| Finding | ไม่มีโมดูล MPS และ Quality ใน source Community ; มีร่องรอยในโค้ด `mrp` ที่รองรับ origin "MPS" ; **ฐาน iTEST02 มีโครงสร้าง MPS, Quality, PLM (ECO) ติดตั้งอยู่** → พฤติกรรมอยู่นอก Community |
| Classification | ไม่ใช่ Community (Enterprise หรือแหล่งอื่น — ไม่มีโค้ดใน tree ; ไม่ได้ยืนยันที่มา) |
| Pointer | `RESTRICTED:…/mrp/models/stock_rule.py:90` ; รายการโมดูลระดับ `odoo/addons` (`ABSENCE`) |
| Manifest / override | ไม่มี manifest ใน tree |
| Schema-only | ผลเป็นกลาง: พบโครงสร้างของพื้นที่วางแผนผลิต/PLM/คุณภาพในฐานทดสอบ (ไม่ระบุชื่อ) |
| Evidence level | `ABSENCE` + `SCHEMA` |
| Neutral conclusion | ตอบไม่ได้จาก source ที่มี ; ต้องระบุแหล่งและ license ของโมดูลก่อนวิจัยต่อ |

### D-13 — GAP-BRP-10 (เปลี่ยนต้นทุนระดับล่างกระทบ MO ที่เสร็จ)
| Field | รายละเอียด |
|---|---|
| Prior claim | UNKNOWN |
| Finding | มูลค่า stock move เป็นค่าที่เก็บ ณ ตอนเสร็จ ไม่ถูกคำนวณสด ; แก้ราคามาตรฐาน (ไม่ใช่ FIFO) สร้างรายการปรับมูลค่าลงวันที่ปัจจุบัน กระทบมูลค่าคงเหลือ ไม่ใช่ move อดีต ; Landed cost เพิ่มมูลค่า move ที่เสร็จได้ ; ปุ่มคำนวณราคาจาก BoM ใช้ราคามาตรฐานปัจจุบัน |
| Classification | Community |
| Pointer | `RESTRICTED:…/stock_account/models/stock_move.py:24-26,292-357,439` · `stock_account/models/product.py:286-336` · `mrp_account/models/product.py:44-99` |
| Manifest / override | ไม่พบ override `_set_value`/`_change_standard_price` |
| Schema-only | ผลเป็นกลาง: มูลค่ารายการเคลื่อนไหวถูกเก็บเป็นค่าที่บันทึก (ไม่ใช่ค่าคำนวณสด) ตามโครงสร้าง ; มีโครงสร้างมูลค่าสินค้า — **ต้อง requalify (§R)** |
| Evidence level | `SRC-STATIC` + `SCHEMA` ; ยังไม่ตรวจกรณี vendor bill มีผลย้อน (`_set_value` ถูกเรียกซ้ำหลังบิล) |
| Neutral conclusion | ต้นทุนใหม่มีผลกับการผลิตที่จะเกิดในอนาคตและมูลค่าคงเหลือ ไม่ใช่การคำนวณย้อนคำสั่งผลิตที่เสร็จ |

### D-14 — Schema-only controls (เชื่อม GAP-D01-11, GAP-D01-13, และ Migration)
| Field | รายละเอียด |
|---|---|
| Prior claim | D01-13 `account_move` CHECK constraints ไม่ได้ enumerate ; D01-11 Σdebit=Σcredit ยังไม่ยืนยันที่ระดับข้อมูล |
| Finding | การควบคุมความถูกต้องระดับฐานข้อมูลมีเฉพาะระดับบรรทัดรายการบัญชี ไม่พบระดับหัวรายการ ; **ไม่พบ trigger ที่ผู้ใช้สร้าง** ⇒ การสมดุลของรายการไม่ได้บังคับที่ฐานข้อมูล ; ค่าตั้งตามบริษัทของหมวดสินค้าถูกเก็บภายในแถวเดียวกัน (ไม่ใช่ตารางแยก) ; ไม่พบตัวควบคุมระดับฐานข้อมูลของกฎอัตราส่วนต้นทุนผลผลิตรอง |
| Classification | Community schema (ณ ฐาน iTEST02) |
| Evidence pointer | `RESTRICTED-SCHEMA:iTEST02 dump sha256 d67fff6d…` · ผลเป็นเมตาดาต้าเท่านั้น — ไม่ commit DDL/ชื่อโครงสร้าง |
| Schema-only status | ผลเป็นกลาง (เมตาดาต้าเท่านั้น) — ข้อมูลจริงไม่ได้ตรวจ ⇒ D01-11 (data-level balance) ยังไม่ตอบ |
| Limitation | dump (2026-06-14) เก่ากว่า source (`post20260921`) ; ผลเป็นของฐานนี้ ไม่ใช่ของ Odoo ทุกฐาน |
| Neutral conclusion | การควบคุมความถูกต้องของรายการบัญชีและกฎ % ผลผลิตรองอยู่ที่ชั้นแอป ไม่ใช่ฐานข้อมูล → นำเข้าข้อมูลต้องผ่านชั้นแอปหรือมีการตรวจสมดุลแยกต่างหาก |

### D-15 — ข้อสังเกตเชิงขอบเขต (ไม่ผูก Gap-ID เดิม; ให้ session หลักพิจารณาสร้าง/ผูก)
1. **ความไม่สอดคล้องเวอร์ชันโมดูล:** `smesplus_account` ประกาศ version `17.0.1.0.0` แต่อยู่ใน tree ของ 19 และ depends `account_accountant` (Enterprise, ไม่มีโค้ดใน tree)
2. **`cr_effective_date_entries`** อ้างโมเดล/ฟิลด์ที่ไม่มีใน Odoo 19 (ดู §2.1) — ความเสี่ยงความเข้ากันได้ + ช่องทางเปลี่ยนวันที่ย้อนหลัง
3. **ฐานทดสอบมีโครงสร้างจากโมดูลนอก Community ~700 ตาราง** (จับคู่ชื่อโมเดล ประมาณการ) → ผลวิจัยแกน Community ใช้เป็นฐานได้ แต่พฤติกรรมจริงต้องอิงชุดที่ติดตั้ง
4. ไม่พบร่องรอยตารางของโมดูลบัญชี custom (`smesplus_*`/`scgl_*`) ในฐาน iTEST02 ณ 2026-06-14 → ณ วันนั้นโมดูลเหล่านั้นอาจยังไม่ติดตั้งหรือไม่เพิ่มตาราง/คอลัมน์

---

## 4. Contradictions ที่ส่งต่อ (สรุป)
| ที่ | ประเด็น |
|---|---|
| Matrix Step 1 | ขัดกับ source (รับ/ส่งกับ Supplier/Customer ไม่ลงบัญชีตอน move) |
| Matrix Step 3 | มีเงื่อนไขบัญชี Loss Account |
| Matrix Step 4 | Stock Closing ≠ self-reversing accrual |
| `MFG-F03` | "reversed once MO completes" ไม่พบกลไกนี้ |
| `BRP-F08`/`GAP-BRP-09` | candidate default เดิมเป็นผลของ % = 0 ไม่ใช่กฎหลัก |
| `GAP-BRP-08`, `GAP-QCP-02` | โมดูลอยู่นอก Community แต่ติดตั้งในฐานทดสอบ |

## 5. Required runtime validation (รวม) — รอ BGQ-04 / AWT
รายการใน D-01…D-14 ทั้งหมด ; ลำดับแนะนำ: (1) valuation timing + Stock Closing (2) lock date + การแก้หลังล็อก (3) By-Product cost share (4) ผลิตบางส่วน/Unbuild (5) Reordering→เอกสารร่าง

## 6. Relabel ผลงานรอบก่อน (ต้องอ่านร่วม — ไม่ได้แก้ไฟล์เดิมในรอบนี้)
ไฟล์ที่ commit ไปแล้วก่อนกติกาใหม่ ใช้ถ้อยคำที่ **ขัดกับกติกาปัจจุบัน** ("Resolved (source-code tier)", "ปิดได้", "เสนอ Resolved") และยังไม่ระบุ `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`:
- `MANUFACTURING_BOM_ROUTING_PILOT/SRC_GAP-BRP-09_*` (2 ไฟล์)
- `MANUFACTURING_BOM_ROUTING_PILOT/SRC_GAPS_BRP-01-02-04-05-07-08-10_*` (2 ไฟล์)
- `MANUFACTURING_VALUATION_PILOT/SRC_GAPS_MFG-02-03-04-05_*` (2 ไฟล์)
- `MANUFACTURING_VALUATION_PILOT/SRC_GAP-MFG-01_VALUATION_TIMING_SOURCE_CHECK_*` (2 ไฟล์)
- `04_EVIDENCE_PACKS/DB_SCHEMA_ONLY/STATE03_DB_SCHEMA_SOURCE_CROSSCHECK_*` (2 ไฟล์)

**ให้ถือถ้อยคำในเอกสารนี้ (§0–§5) เป็นฉบับที่ใช้แทน** ; ข้อเสนอสถานะ "Resolved/ปิด" ในไฟล์เหล่านั้นให้ถือเป็นโมฆะ.

**สถานะ remediation (2026-09-30, commit แยก):** banner `STATUS CORRECTION` ถูกเพิ่มในไฟล์ `SRC_*` และ `STATE03_DB_SCHEMA_*` ทั้ง 12 ไฟล์ (คงข้อความเดิม) ; `STATE03_DB_SCHEMA_SOURCE_CROSSCHECK_*` ถูกลดรูปเป็น data-minimized (ลบรายชื่อตารางนอก Community, นิยาม constraint, ข้อความ query และคำอธิบายตาราง/คอลัมน์ออกจาก working tree) ; รายละเอียด "Schema-only" ในเอกสารนี้ถูกทำให้เป็นผลแบบเป็นกลาง. **เนื้อหาเดิมยังอยู่ในประวัติ Git ของ branch นี้** (ไม่ได้เขียนประวัติใหม่/ไม่ force-push) และยังต้องผ่าน Independent Clean-Room review. ผลค้นรูปแบบ schema ใน working tree ส่วนอื่นที่ไม่ใช่ผลงานของ session นี้ (เอกสารของ session ก่อนหน้า เช่น DOMAIN_01 database registers) พบเป็นการกล่าวถึงวิธี/ผลระดับสรุป — **บันทึกไว้ ไม่ได้แก้** เพื่อให้ session หลักตัดสิน

## 7. คิวถัดไป (ตามที่กำหนด)
1. ✅ `GAP-PCO-01` ถึง checkpoint (D-07)
2. ✅ Manifest/provenance inventory รอบที่ 1 สำหรับ Accounting/Inventory/MRP/lock/valuation (ที่ license เปิด) — ยังค้าง: ตรวจ override เชิงลึกของ `purchase_request` (เอกสารที่สร้าง), `scgl_account_reconcile`/`scgl_account_tax_return` (reconciliation/ภาษี), `bh_parent_company` (multi-company / record rules), `stock_picking_reference_no`, `bh_purchase_receipt_all` (การรับสินค้า)
3. ต่อไป: ไล่โมดูล custom ตาม dependency/risk (ลำดับ: multi-company → reconciliation → receipts/pickings → tax period) ; ผลของ `GAP-MCT-01/02`, `GAP-RCN-01/02` จะทำหลังข้อ 2

---
---

# ROUND 2 — Append (2026-09-30) — Prompt: STATE03_ODOO19_SOURCE_DUMP_CONTINUATION_AND_REMEDIATION

**Status ของทุกรายการในส่วนนี้:** `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` · ไม่ใช่ runtime proof / Gate PASS / gap closure / STATE03 complete / FDS authorization · Community-core = `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`
**Actual V-level:** session นี้ **ไม่กำหนด V-level เอง** — หลักฐานทั้งหมดเป็น source-static/schema-only (ไม่มี runtime) จึงไม่สามารถอ้างว่าถึง floor ของ C1 (V4 จาก target V5) หรือของฟังก์ชันอื่น (V3 จาก target V4) ; การกำหนด V-level เป็นของ session หลัก

## R0. Remediation log (ดำเนินการแล้ว — commit `30bc0101`, แยกจากงานวิจัย)
- Banner `STATUS CORRECTION` เพิ่มใน **10 ไฟล์** (`SRC_*` 8 ไฟล์ + `STATE03_DB_SCHEMA_*` 2 ไฟล์) — **แก้ตัวเลข §6 ด้านบนที่ระบุ 12 ไฟล์ ให้เป็น 10 ไฟล์** ; ข้อความเดิมคงไว้
- `STATE03_DB_SCHEMA_SOURCE_CROSSCHECK_*` ลดรูปเป็น data-minimized (ลบ: รายชื่อตารางนอก Community, นิยาม constraint, ข้อความ query, คำอธิบายตาราง/คอลัมน์) ; แถว "Schema-only" ในเอกสารนี้ทำให้เป็นผลเป็นกลาง ; **เนื้อหาเดิมยังอยู่ใน Git history** (ไม่ได้เขียนประวัติใหม่/ไม่ force-push/ไม่อ้างว่าลบล้างได้) — ยังต้องผ่าน Independent Clean-Room review
- ผลค้นรูปแบบ schema ใน working tree ส่วนอื่น: มีการกล่าวถึงวิธี/ผลระดับสรุปในเอกสารของ session ก่อนหน้า (DOMAIN_01 database registers, source registry, session archive ฯลฯ) — **บันทึกไว้ ไม่ได้แก้** (ไม่ใช่ผลงาน session นี้ ; ให้ session หลักตัดสินว่าต้อง remediate หรือไม่)
- หมายเหตุ: ไฟล์ Handoff นี้ถูกแก้ (ไม่ใช่ append-only) **เฉพาะใน commit remediation** เพื่อลดรายละเอียด schema ; ตั้งแต่ R1 เป็นต้นไปเป็น append-only

## R1. Provenance ของ 300-module register (authorized scope)
| รายการ | ค่า |
|---|---|
| Artifact ที่อ่าน | `SMEsPlus_Odoo19_Community_Master_Register_V1.00.xlsx` — อ่านเฉพาะชีตรายการโมดูลระดับ metadata (`technical_name`, กลุ่ม, dependency) ; ไม่ได้นำเนื้อหาออกจากเครื่อง |
| **ความไม่ตรงของ hash** | sha256 ของไฟล์บนดิสก์ = `790bcd2a46a0b849…` แต่ manifest ใน repo (`…_SHA256.txt`) ระบุ `76aa648b39ccb71a…` → **ไฟล์บนดิสก์ไม่ตรงกับ baseline ที่บันทึกไว้** (แก้ไขภายหลัง? — ต้องให้ session หลักยืนยัน) ; ใช้รายการโมดูลเป็นข้อมูลอ้างอิงชั่วคราว ไม่ถือเป็น denominator |
| ผลตรวจ (นับจริง ไม่ใช่เปอร์เซ็นต์ความคืบหน้า) | CURRENT-PHASE = 300 แถว (ตรงกับ manifest) ; ทั้ง 300 โมดูล **มีอยู่ใน source Community** ; license ทั้งหมด LGPL-3 ; `direct_dependencies` ของทั้ง 300 อยู่ภายใน 300 (ไม่พบ dependency ภายนอกชุด 300) ; สถานะ mapping ในทะเบียน: MAPPED-CANDIDATE 269, BOSS-SCOPE-REVIEW-THEME 29, BOSS-DECISION-PENDING 2 |
| Restricted annex | รายการโมดูล/กลุ่มเก็บ **นอก repo** ที่ `RESTRICTED-LOCAL:~/STATE03_RESTRICTED_LOCAL/register300.json` (ไม่ commit) |

### R1.1 สถานะ Module/Function (report Module ก่อน Function — นับจริง)
| ชั้น | นับจริง | รายละเอียด |
|---|---|---|
| โมดูลใน 300 ที่ session นี้ **อ่าน source แล้วบางส่วน** (เฉพาะจุดตัดสินใจของ Function ที่ระบุ ไม่ใช่ deep-study ครบโมดูล) | 19 | `account`, `analytic`, `product`, `uom`, `stock`, `stock_account`, `stock_landed_costs`, `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_purchase`, `mrp_subcontracting_dropshipping`, `purchase`, `purchase_stock`, `sale`, `sale_stock`, `l10n_th` |
| โมดูลใน 300 ที่ **ยังไม่ได้ทำ source-map ตามมาตรฐาน §5.1** | 281 (=300−19) โดย 19 ข้างต้นก็ยัง **ไม่ครบ §5.1 เช่นกัน** | ต้องทำต่อ |
| Discovered supporting modules (นอก 300 denominator) | 0 | ทุกโมดูล Community ที่แตะอยู่ใน 300 |
| โมดูล Company Extra/Custom / Customer-authorized Custom / Third-party Source-readable ที่เปิดถึงระดับโค้ดจุดเฉพาะ | 10 | `account_lock_date_update`, `base_accounting_kit`, `smesplus_account`, `scgl_account_deferred`, `cr_effective_date_entries`, `purchase_request`, `scgl_account_reconcile`, `bh_parent_company`, `bh_purchase_receipt_all` + `smesplus_tax_period_date`/`scgl_tax_period_date` (ระดับโครงสร้าง) |
| Function/Gap ที่มีรายการ Delta | 15 ตัว (D-01…D-14 + D-15 หมายเหตุ) + R2–R6 ด้านล่าง | ไม่มีตัวใดปิดสมบูรณ์ |
> ใช้สำหรับรายงานเท่านั้น — ไม่ใช่ coverage/ความคืบหน้าเชิงเปอร์เซ็นต์

## R2. Re-qualification ของข้อสรุปเดิม (§4.3) — ถือเป็น research lead
| # | ข้อสรุปเดิม | การตรวจซ้ำ (pointer) | สถานะหลัง requalify |
|---|---|---|---|
| Q1 | GAP-PCO-01 (hard/soft lock, date-shifting) | ตรวจซ้ำโดยตรงกับ source วันนี้: `RESTRICTED:Odoo Community/…/odoo/addons/account/models/company.py:51-112,552-606,642-700`; `account/models/account_move.py:2823-2840,3826-3829,5700-5706,6714-6750`; `account/models/account_lock_exception.py` | **Lead ที่ตรวจซ้ำแล้ว (SRC-STATIC)** ; version/module set: `19.0.post20260921` + overlay ที่ระบุใน D-07 ; **UNKNOWN — EVIDENCE INSUFFICIENT**: พฤติกรรมของ Enterprise lock wizard, ผู้ override ใน OPL-1/ไม่ระบุ license, การเลื่อนวันที่ของรายการกลับรายการ ; runtime required |
| Q2 | GAP-MFG-01 / GAP-PCO-02 (valuation timing, Stock Closing) | pointers ใน D-06 (ตรวจซ้ำในรอบนี้ 3 จุด: ไม่มีรายการบัญชีตอน move ถ้าไม่มีบัญชีที่ location ; บรรทัดบิลซื้อ storable ตั้งบัญชีสต็อกโดยตรง ; Stock Closing manual/cron) | **Lead** — ข้อความ "การรับ/ส่งกับ Supplier/Customer ไม่ลงบัญชีตอน move" เป็น `INFER` เพราะขึ้นกับการตั้งค่า location/หมวดสินค้า/ส่วนขยาย ; **ห้ามสรุปเป็นกฎสากล** ; **UNKNOWN — EVIDENCE INSUFFICIENT** สำหรับพฤติกรรมเมื่อมี OPL-1 ที่ depends `stock_account` |
| Q3 | GAP-BRP-09 (By-Product cost share) | pointers ใน D-01 | **Lead** — ตัวเลขตาม unit test ของ Odoo (SRC+TEST) แต่ "% = 0 ⇒ มูลค่า 0" เป็น `INFER` ; Unbuild/Subcontract **UNKNOWN — EVIDENCE INSUFFICIENT** |
| Q4 | การมี/ไม่มี `stock.valuation.layer` ใน Odoo 19 | ค้นทั้ง `odoo/` (py/xml/csv) : **ไม่มีคำนิยามโมเดล** ; พบการกล่าวถึงเพียง 2 จุด (ความเห็นใน demo data ของ `mrp_account` และความเห็นใน test ของ `stock_account`) ; ไม่มี migration script ใน `odoo/upgrade*`/addons ที่อ้างถึง ; มีโมเดลมูลค่าสินค้าใหม่ใน `stock_account/models/product_value.py:14` | **SRC-STATIC เฉพาะ revision `19.0.post20260921`** : ไม่มีโมเดลนี้ใน revision นี้ ; **ไม่ใช่ข้อสรุปเรื่อง "Odoo 19 ทุก revision"** ; ฐานทดสอบ (2026-06-14) ไม่พบโครงสร้างชื่อเดียวกัน — แต่ผลจาก schema ไม่พิสูจน์ ; **UNKNOWN**: revision ก่อน 2026-09-21 |
| Q5 | ข้อสรุปที่อิงการ "ไม่พบตาราง/คอลัมน์" | ทุกข้อที่อิง `ABSENCE`/schema ถูกติดป้ายในแต่ละ D-xx | **ห้ามใช้เป็นหลักฐานว่าไม่มีโมดูล/ไม่มีผล** |
| Q6 | ข้อสรุปที่ว่าโมดูล custom "ไม่ override" พฤติกรรมหลัก | ขอบเขต: 117 โมดูล license เปิด (สแกนเฉพาะ `_inherit` ของโมเดลหลัก + ชื่อเมธอด) ; **สแกนด้วยรูปแบบข้อความ ไม่ใช่การวิเคราะห์ MRO** ; 41 โมดูลไม่ได้อ่านโค้ด | **Lead** — "ไม่พบ override" ≠ "ไม่มี override" |

## R3. Effective override — 4 โมดูลที่ระบุใน §7.3
| โมดูล / ประเภท / license | สิ่งที่ทำ (เป็นกลาง) | ผลต่อ core behavior | Pointer |
|---|---|---|---|
| `purchase_request` — Third-party Source-readable (OCA/ForgeFlow, LGPL-3) ; depends รวม `smesplus_widget`, `odoo19_uom_ext`, `hr`, `project` | เพิ่มโมเดลใบขอซื้อ ; **`stock.rule._run_buy` ถูก override: ถ้าสินค้ามีเครื่องหมายใช้ใบขอซื้อ ขั้นตอน "buy" จากการจัดหา (รวมจาก Reordering Rule) จะสร้าง Purchase Request แทน RFQ โดยตรง** ; ใบขอซื้อมีสถานะ draft/to_approve/approved ; `_quantity_in_progress` ของ Reordering Rule นับปริมาณในใบขอซื้อที่ยังไม่แปลงเป็น PO ; `stock.picking/_action_done` และ `stock.move.line/_action_done` จัดสรรปริมาณที่รับเข้ากับใบขอซื้อ | **มีผลต่อ GAP-BRP-07** : มี "จุดพัก/อนุมัติ" ก่อนเป็น RFQ ได้ **เมื่อเปิดใช้ต่อสินค้า** ; ไม่ได้เปลี่ยนการคำนวณมูลค่าสต็อก | `RESTRICTED:addons_Extramodule/addons/purchase_request/models/stock_rule.py:47-97` · `…/orderpoint.py` · `…/stock_picking.py:35-` · `…/stock_move_line.py:115-` (manifest hash `9fe183e179afa913`) |
| `scgl_account_reconcile` — Customer-authorized Custom (SCG Legacy, LGPL-3) ; depends `account` | เพิ่มปุ่มกระทบยอดรายการที่เลือก/อัตโนมัติ (จับคู่ยอดตรงข้ามภายใน บัญชี+คู่ค้า+สกุลเงิน เดียวกัน แล้วเรียก `reconcile()` ของ core) | **ไม่ override เมธอดของ core** ; ใช้กลไก reconcile เดิม ; ไม่ข้ามคู่ค้า | `RESTRICTED:Extra_Module_scgl/scgl_account_reconcile/models/account_move_line.py:1-60` (hash `ca6cd509b7c712ae`) |
| `bh_parent_company` — Customer-authorized Custom (BHPRO, LGPL-3) | โมเดลกลุ่มลูกค้า "บริษัทแม่/แบรนด์" ผูกกับ partner และ sale order ; **ไม่ใช่กลไก multi-company ของ Odoo** ; มี record rule แบบ multi-company มาตรฐานของตัวเอง ; ตั้งกลุ่ม Manager ให้ผู้ใช้ระบบ/admin ผ่านข้อมูลโมดูล | ไม่แตะบัญชี/สต็อก ; กระทบเฉพาะการกรองลูกค้าและรายงานขาย | `RESTRICTED:addons_Extramodule/addons/bh_parent_company/models/*.py`, `…/security/bh_parent_company_security.xml` (hash `18c6500d7ce8b83e`) |
| `bh_purchase_receipt_all` — Customer-authorized Custom (SCGL, LGPL-3) | ปุ่มแสดงใบรับสินค้าทั้งหมดของ PO รวม backorder แบบเรียกซ้ำ (อ่านอย่างเดียว) | ไม่ override พฤติกรรมของ core | `RESTRICTED:addons_Extramodule/addons/bh_purchase_receipt_all/models/purchase_order.py:1-74` |

**อัปเดต D-11 (GAP-BRP-07):** ข้อสรุปเดิม (เกตอยู่ที่การยืนยันเอกสารร่าง) ยังเป็นจริงสำหรับแกน Community ; **ถ้า `purchase_request` ติดตั้งและสินค้าเปิดใช้ ใบขอซื้อคือจุดอนุมัติเพิ่ม** (ฐานทดสอบมีร่องรอยการติดตั้งโมดูลนี้) ⇒ ผลของ BRP-07 ต้องรายงานเป็น *CONDITIONAL* ; เกี่ยวข้อง 3-dimension: Business (คำขอ→อนุมัติ→PO), Data (ใบขอซื้อเป็นออบเจกต์คั่นกลางระหว่างความต้องการกับ PO), Source (override จุดเดียวที่ขั้นตอน buy) ; **Required follow-up:** ตรวจ `purchase_request.state` flow และสิทธิ์ผู้อนุมัติ (ยังไม่ได้อ่าน)

## R4. GAP-MCT-01 (Inter-company valuation) — source-static lead
| Field | รายละเอียด |
|---|---|
| Existing ID / prior claim | `GAP-MCT-01` — ไม่มีเอกสารว่าการ sync stock move ข้ามบริษัทคำนวณมูลค่าอิสระหรือคัดลอก |
| Module / classification | `stock`, `stock_account`, `product` — Odoo Community Core (ทั้งหมดอยู่ใน 300) |
| Finding | (1) ไม่พบโมดูล inter-company rules (ที่สร้าง SO/PO/transfer คู่กันข้ามบริษัท) ใน source Community ที่มี — **กลไก "sync" เองอยู่นอก source ชุดนี้** (`ABSENCE`; ฐานทดสอบ/โมดูลนอก Community อาจมี — ไม่ทราบ) (2) มีเพียงสถานที่ "Inter-company transit" (ประเภท transit, ไม่ผูกบริษัท, ปิดใช้งานเป็นค่าเริ่มต้น) (3) การตีความ in/out ของมูลค่า: สถานที่ต้องผูกบริษัทและเป็น internal/transit จึงนับเป็นในบริษัท ; transit ที่ไม่ผูกบริษัทถือเป็นภายนอก ⇒ การส่งออก/รับเข้าของแต่ละบริษัทถูกตีค่า **ในบริบทบริษัทตนเอง** (4) ต้นทุนสินค้า (`standard_price`) เป็นค่าตามบริษัท ⇒ ไม่มีกลไกคัดลอกมูลค่าระหว่างบริษัทใน `_get_value_data` (`INFER`) |
| Pointer | `RESTRICTED:…/stock/data/stock_data.xml:34-39` · `stock/models/stock_location.py:203-205,466-476` · `stock_account/models/stock_location.py:36-41` · `stock_account/models/stock_move.py:363-448,585-595` · `product/models/product_product.py:62-66` |
| Extension / override | ไม่พบโมดูล custom (license เปิด) ที่ inherit `stock.location`/`stock.move` valuation ; OPL-1/ไม่ระบุ license ตรวจไม่ได้ |
| Schema-only | ผลเป็นกลาง: โครงสร้างต้นทุนแยกตามบริษัทเป็นแบบเก็บภายในแถว (ดู R0/F4) — ไม่ระบุรายละเอียด |
| 3-dimension | Business: การโอนขายระหว่างบริษัทในกลุ่มแต่ละฝั่งบันทึกต้นทุนของตนเอง · Data: ไม่มีออบเจกต์ "มูลค่าที่ใช้ร่วม" ข้ามบริษัทใน Community · Source: การประเมินค่าใช้ `with_company` และ `standard_price` ตามบริษัท |
| V-level | ไม่กำหนด (source-static เท่านั้น) |
| Limitation | ไม่ได้ตรวจกรณี PO/SO คู่ (ถ้ามีโมดูลที่สร้าง) ที่ทำให้ `_get_value_from_quotation` ให้ราคาข้ามบริษัท ; ไม่ได้รัน |
| Neutral outcome | ในแกน Community มูลค่าสต็อกของแต่ละบริษัทถูกคำนวณอิสระตามต้นทุนของบริษัทนั้น ; กลไกการซิงก์เอกสารข้ามบริษัทไม่อยู่ในชุด source ที่มี |
| Follow-up | runtime: ส่งของข้ามบริษัทแล้วเปรียบเทียบมูลค่าออก/เข้า ; ยืนยันโมดูลซิงก์ที่ใช้จริง |

## R5. GAP-MCT-02 (record-rule mechanics ระดับ warehouse) — ยังไม่ทำ
บันทึกเป็น **ยังไม่ได้ทำ** ในรอบนี้ (ต่อคิว).

## R6. คิวคงเหลือ (ตาม §7)
- ทำต่อ: `GAP-MCT-02`, `GAP-RCN-01/02`, `GAP-PDT-01/02`, `GAP-SDV-02/05`, `GAP-IAV-*`, `GAP-GRV-*` ตามลำดับเสี่ยง/dependency
- source-map ตาม §5.1 สำหรับโมดูลใน 300 ที่ยังไม่ได้ทำ (ทั้งหมด 300 ยังไม่ครบตามมาตรฐาน)
- ตรวจเชิงลึก: `purchase_request` state flow, `stock_picking_reference_no`, `scgl_account_tax_return`, `smesplus_tax_period_date` (record rule/IAM), โมดูล license ปิด → ระดับ manifest เท่านั้น
- ตรวจสอบ hash ของ register ที่ไม่ตรงกับ manifest (R1)

---

## R7. Corrections to R1.1 (append-only correction)
- ตัวเลข "Function/Gap ที่มีรายการ Delta 15 ตัว" ใน R1.1 **ให้แก้เป็น:** รายการ Delta แบบเต็ม D-01…D-14 = 14 รายการ (D-15 เป็นหมายเหตุ ไม่นับเป็น Function/Gap) + R3 (4 โมดูล), R4 (MCT-01), R8/R9 ด้านล่าง
- ในรายการ "โมดูลใน 300 ที่อ่านแล้วบางส่วน" ให้ **ตัด `uom` และ `analytic` ออก** (ไม่ได้อ่านโค้ดของสองโมดูลนี้จริง — อ้างถึงเพียงผ่านโมดูลอื่น) → จำนวนที่อ่านจริงเฉพาะจุดตัดสินใจ = **17**

## R8. GAP-MCT-02 — กลไก record-rule ระดับ warehouse (source-static lead)
| Field | รายละเอียด |
|---|---|
| Existing ID / prior claim | `GAP-MCT-02` (`MCT-F05`) — ไม่มีเอกสารทางการเรื่องกลไกจำกัดผู้ใช้ตาม warehouse (มีแต่หลักฐานชุมชน/marketplace) |
| Module / classification | `stock`, `stock_account` — Odoo Community Core (อยู่ใน 300) |
| Finding | กฎความปลอดภัยของ `stock` ที่พบทั้งหมดเป็นแบบ **แยกตามบริษัท** (เงื่อนไข company ∈ บริษัทที่อนุญาต ; บางโมเดลอนุญาตค่าว่าง = ใช้ร่วม) ครอบคลุม picking, operation type, warehouse, location, move, move line, quant, Reordering Rule, scrap ฯลฯ ; กลุ่ม "Manage Multiple Warehouses/Locations" เป็นตัวเปิดฟีเจอร์ **ไม่ใช่กลไกจำกัดสิทธิ์รายผู้ใช้–รายคลัง** ; **ไม่พบ** กฎที่จำกัดผู้ใช้ให้เห็นเฉพาะ warehouse ของตนใน `stock` (`ABSENCE`) ⇒ กลไกที่หลักฐานชุมชนกล่าวถึง (ถ้ามี) **ไม่อยู่ในแกน Community ของ revision นี้** — น่าจะมาจากโมดูลเสริม (ยังไม่ระบุ) |
| Pointer | `RESTRICTED:Odoo Community/…/odoo/addons/stock/security/stock_security.xml:10-70 (groups), 72-135+ (company rules)` · `stock/models/stock_warehouse.py:331` (การจัดการกลุ่ม multi-warehouse) · `stock_account/security/*.xml` (rule ของ `product.value` และรายงานต้นทุนเฉลี่ย แยกตามบริษัท) |
| Extension / override | ยังไม่ได้สแกนโมดูล custom ที่เพิ่มกฎ warehouse (สแกนก่อนหน้าดูเฉพาะ `_inherit` ของโมเดลหลัก ไม่ครอบคลุมไฟล์ security XML) → **UNKNOWN — EVIDENCE INSUFFICIENT** ว่า deployment จริงมีกฎ warehouse หรือไม่ |
| Schema-only | ไม่มีหลักฐานจาก schema ที่ตอบเรื่องนี้ได้ (กฎอยู่ในข้อมูล) — ไม่ได้ตรวจ |
| 3-dimension | Business: การแยกข้อมูลข้ามบริษัทเป็นแนวป้องกันหลัก ; การแยกภายในบริษัทตามคลังต้องพึ่งการตั้งค่า/ส่วนเสริม · Data: warehouse/location ผูก company และเป็นหน่วยแยกข้อมูล · Source: record rule แบบ company เป็นหลัก |
| V-level | ไม่กำหนด |
| Neutral outcome | แกน Community ให้การแยกข้อมูลระดับบริษัท ไม่ให้การจำกัดสิทธิ์ระดับคลังต่อผู้ใช้ ; ถ้าองค์กรต้องการ ต้องมาจากส่วนขยายหรือการออกแบบสิทธิ์ (ต้องระบุแหล่งที่มา) |
| Follow-up | สแกน security XML ของโมดูล custom ที่ license เปิด ; ตรวจ deployment จริง |

## R9. GAP-RCN-01 / GAP-RCN-02 (source-static lead)
| Field | GAP-RCN-01 | GAP-RCN-02 |
|---|---|---|
| Prior claim | ลิงก์ stock move → journal entry มีสำหรับธุรกรรมทั่วไปหรือเฉพาะกรณีย้อนหลัง? | การติดตามต้นทุนรายล็อตใช้ได้กับ AVCO ไหม (ไม่ใช่เฉพาะ FIFO)? |
| Module / classification | `stock_account`, `account` — Community Core | `stock_account` — Community Core |
| Finding | stock move มีตัวอ้างอิงไปยังรายการบัญชีที่ตนสร้าง ตั้งค่าทุกครั้งที่ระบบสร้างรายการบัญชีระดับ move (ไม่มีเงื่อนไขเฉพาะการย้อนหลัง ; บริบทวันที่บังคับ `force_period_date` เป็นเพียงตัวกำหนดวันที่) ; **จำกัดเฉพาะ move ที่เกิดรายการระดับ move** (เงื่อนไขบัญชีที่ location) — รายการที่เกิดจากบิล/ใบแจ้งหนี้เชื่อมผ่านบรรทัดคำสั่งซื้อและบรรทัด COGS (อ้างอิงต้นทางบรรทัด) ไม่ใช่ลิงก์เดียวกัน (`INFER`) | การตีมูลค่าแยกล็อต (เมื่อเปิดใช้ตามสินค้า) รองรับทั้ง Standard, Average และ FIFO ในตัวคำนวณมูลค่าล็อต ; ต้นทุนล็อตอัปเดตตามวิธีต้นทุนของสินค้า ; ขาออกของสินค้าที่ตีมูลค่าแยกล็อตใช้ต้นทุนของล็อต |
| Pointer | `RESTRICTED:…/stock_account/models/stock_move.py:51,193-216` · `stock_account/models/account_move.py:8` · `stock_account/models/account_move_line.py:7-11` | `RESTRICTED:…/stock_account/models/stock_lot.py:9-48,60-108` · `stock_account/models/stock_move.py:328-347` |
| Extension / override | ไม่พบโมดูล license เปิดที่ inherit `stock.move`/`account.move` ในส่วนนี้ (ยกเว้นตัวจัดการวันที่ picking ของ `cr_effective_date_entries` ที่ใช้โมเดลไม่ตรงรุ่น) | ไม่พบ override ; OPL-1 ตรวจไม่ได้ |
| Schema-only | ผลเป็นกลาง: มีโครงสร้างอ้างอิง move→รายการบัญชี ; มีโครงสร้างมูลค่าแยกล็อต — ไม่ระบุรายละเอียด | เช่นเดียวกัน |
| V-level | ไม่กำหนด | ไม่กำหนด |
| Limitation / UNKNOWN | ไม่ได้ตรวจข้อความ audit ที่ผู้ใช้เห็น ; ไม่ได้รัน | ไม่ได้ตรวจคุณภาพตัวเลข AVCO รายล็อตกับกรณีบิลมาทีหลัง — **UNKNOWN — EVIDENCE INSUFFICIENT** |
| Neutral outcome | ร่องรอยจากการเคลื่อนไหวสต็อกไปยังรายการบัญชีมีสำหรับรายการระดับ move ทั่วไป ไม่ผูกกับกรณีย้อนหลัง แต่ไม่ครอบคลุมรายการที่เกิดจากเอกสารการเงิน | ต้นทุนรายล็อตไม่จำกัดเฉพาะ FIFO ในแกน Community |
| Follow-up | runtime: ตรวจ audit trail ปลายทาง ; ทดสอบล็อต AVCO กับบิลมาทีหลัง | เช่นเดียวกัน |

## R10. งานที่กำลังทำ / ยังไม่ทำ (ตาม §8 contract — ใช้จำนวนจริง)
- **กำลังทำ:** ไล่คิว `GAP-PDT-01/02` → `GAP-SDV-02/05` → `GAP-IAV-*` → `GAP-GRV-*` ; ตรวจ security XML ของโมดูล custom license เปิด ; ตรวจ `purchase_request` state flow
- **ยังไม่ทำ:** source-map ตามมาตรฐาน §5.1 ครบสำหรับโมดูลใน 300 (0 จาก 300 ครบมาตรฐาน) ; ตรวจโมดูล Third-party Black-box/OEEL/ไม่ระบุ license (ระดับ manifest เท่านั้น) ; ยืนยัน hash ของ register ; Runtime validation ทุกรายการ

---

# ROUND 3 — Append (2026-09-30) — Directive: "read the 300 modules first" (module-list hash mismatch, source-map ordering)

**Status ของทุกรายการ:** `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` · source revision `19.0.post20260921` · Community-core = `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` · ไม่ใช่ runtime proof · ไม่มี V-level ที่กำหนดโดย session นี้ · ไม่ประกาศ Formal Coverage / Gate PASS / gap closure

## S0. Integrity Gap ของรายการโมดูล
`MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION` : sha256 ของไฟล์ทะเบียนบนดิสก์ (`790bcd2a…`) ≠ ค่าใน `…_SHA256.txt` (`76aa648b…`) → **Material Integrity Gap** ; 300 โมดูลนี้ **ไม่ถูกเรียกว่า "ยืนยันแล้ว"** และ **ไม่ใช้เป็น denominator / Formal Coverage** ; ใช้เป็น *candidate list* เพื่อทำ source map ต่อเท่านั้น ; ทุก record ใน `SOURCE_MAP_CANDIDATE/` ติดป้ายนี้ ; provenance การเปิดไฟล์ (อ่านเฉพาะชีตรายการโมดูล = ข้อมูลควบคุมขอบเขต ไม่ใช่ dump business data) บันทึกใน R1

## S1. R0 ส่งต่อให้ `STATE03_BUSINESS PROCESS`
รายการ R0 (ผลค้นรูปแบบ schema ในเอกสารของ session ก่อนหน้า) **ไม่ถูก remediate โดย session นี้** ตามคำสั่ง — เป็นรายการส่งต่อให้ `STATE03_BUSINESS PROCESS` ตรวจและตัดสินใจเอง

## S2. Source Map — ผลจริง (นับ ไม่ใช่เปอร์เซ็นต์ความคืบหน้า)
| รายการ | จำนวนจริง | หมายเหตุ |
|---|---|---|
| ระเบียนโครงสร้างอัตโนมัติ (S1-STATIC-EXTRACT) ของโมดูลในทะเบียน on-disk | 300 / 300 | สกัดด้วยเครื่องมืออ่าน AST/XML แบบ static ; ไม่ใช่ความหมายเชิงธุรกิจ |
| ระเบียนที่มี trace note (S2-CANDIDATE) | 300 / 300 | เขียนโดย sub-agent อ่านอย่างเดียว 37 ตัว ; ไม่ได้ตรวจอิสระ |
| Source Map **Complete** | **0** | **ไม่ประกาศ** — รายการ §5.1 ข้อ 8 (schema-only ระดับโมดูล) ยังไม่ทำและข้อ 9 (V-level) ยังไม่กำหนดในทุกโมดูล ; trace note ยังเป็น candidate |
| ชี้ตำแหน่ง (pointer) ในโน้ต | 11,364 | ตรวจอัตโนมัติ: 11,229 ชี้ไปยังไฟล์ที่มีจริงและบรรทัดอยู่ในช่วง (135 ไม่ผ่าน) — **ตรวจเพียงการมีอยู่ ไม่ใช่ว่าบรรทัดสนับสนุนข้อความ** |
| การสุ่มตรวจโดย session | 22 คู่ (ข้อความ–บรรทัดต้นทาง) สุ่ม + 9 ข้อความเชิงควบคุมตรวจเป็นรายข้อ | 22/22 สอดคล้องระดับหัวข้อ (ชี้ที่นิยามที่เกี่ยวข้อง) ; ไม่ใช่การยืนยันความหมายทุกข้อความ |
| เครื่องหมาย `UNKNOWN — EVIDENCE INSUFFICIENT` ในโน้ต | 1,155 | ส่วนใหญ่คือขอบเขตที่ไม่ได้อ่าน/ไม่ยืนยัน |
| ข้อความที่อ้างจาก test `(TEST)` | 742 | |
| โมดูลนอก 300 ที่ trace ต่อ (`DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR`) | 0 | dependency ของโมดูลที่ trace อยู่ในชุด on-disk ทั้งหมด ; มีโฟลเดอร์ `theme_test_custo` ใน tree ที่ไม่อยู่ในทะเบียน (ไม่ได้ trace) |

**ข้อจำกัดของ sub-agent notes:** ไม่ได้ทดสอบ/รัน ; การสแกนส่วนขยายใช้ `_inherit` แบบ text ไม่ใช่ MRO ; บางโน้ตอ่านเฉพาะชื่อ test ไม่ใช่เนื้อหา (ระบุในโน้ตนั้น) ; skeleton ถูกเขียนทับระหว่างที่เอเจนต์บางตัวอ่าน (เอเจนต์รายงาน 0 ไบต์ชั่วคราว — ตรวจแล้วปัจจุบันครบ 692 ไฟล์)

**ตำแหน่งไฟล์:** `SOURCE_MAP_CANDIDATE/00_INDEX.md` + `MODULE_<name>.md` (300 ไฟล์) ; ข้อมูลดิบ/ไฟล์ trace/เครื่องมือเก็บ `RESTRICTED-LOCAL:~/STATE03_RESTRICTED_LOCAL/` (ไม่ commit)

## S3. Function / Gap Deep Study (รายงานแยกจาก Source Map)
Gap-ID ที่มี delta ใน Handoff ทั้งหมด (21 ราย): BRP-01, 02, 04, 05, 07, 08, 09, 10 · MFG-01, 02, 03, 04, 05 · PCO-01, 02 · MCT-01, 02 · RCN-01, 02 · QCP-02 (ขอบเขตโมดูลเท่านั้น) · D01-13 (บางส่วน) — **ไม่มีรายการใดปิดสมบูรณ์** ; งาน Deep Study เพิ่ม **พักไว้** ตามคำสั่ง จนกว่า module map ของกลุ่มนั้นครบ

## S4. การแก้/ปรับข้อความรอบก่อน (append-only correction)
1. **R4 / GAP-MCT-01:** ข้อความ "location Inter-company transit ปิดใช้งานเป็นค่าเริ่มต้น" ต้องอ่านร่วมกับ: ตอนสร้างบริษัทใหม่ ระบบเปิดใช้ location นี้ และถ้าผู้ใช้อยู่ในกลุ่ม multi-company ระบบตั้งให้ partner ของบริษัทอื่นใช้ location นี้เป็นทั้งปลายทางลูกค้าและต้นทางผู้ขาย (`RESTRICTED:stock/models/res_company.py:181-208` — session ตรวจซ้ำเอง) ⇒ การซื้อ/ขายข้ามบริษัทในกลุ่มวิ่งผ่าน transit นี้โดยปริยายในการตั้งค่านั้น ; ข้อสรุปเรื่องมูลค่าอิสระต่อบริษัทยังเป็น `INFER`
2. **S1 record ของ `mrp_account`** : ข้อความ "ไม่มีโมดูลขยายวัตถุของโมดูลนี้" ถูกแก้ทุก record ให้ระบุ "dependency ≠ extension" (พบจากการตรวจของเอเจนต์ `stock_account`/`mrp_account`)
3. **D-06 (valuation timing) — watch-points จากเอเจนต์อิสระ (ไม่ได้รับผลเดิมของ session นี้):** (ก) การรับ/ส่งกับ Supplier/Customer ไม่สร้างรายการบัญชีตอน move ถ้าไม่มีบัญชีที่ location (ตรงกัน) (ข) รายการผลิตใช้บัญชีของ location ผลิต ไม่ใช่ "Production Account" ระดับหมวดสินค้า (ค) ต้นทุน Work Center ไม่เข้าต้นทุนสินค้าสำเร็จรูปแบบ Standard — **ข้อความ D-04/D-06 เดิมที่ขัดกับสามข้อนี้ให้ใช้ข้อความนี้แทน**

## S5. ข้อสังเกตเชิงควบคุมจาก source map (research leads — ไม่ใช่พฤติกรรม universal ของ Odoo 19)
> ทุกข้อ: revision `19.0.post20260921`, โมดูลใน on-disk register, extension/override status = "ไม่พบ override ในโมดูล license เปิดที่สแกน ; OPL-1/ไม่ระบุ license ตรวจไม่ได้ ; Enterprise ไม่มีโค้ด", limitation = static เท่านั้น
| # | ข้อสังเกต | Pointer (ตรวจซ้ำโดย session) | ข้อควรระวัง |
|---|---|---|---|
| L1 | ฝั่งขาย: ไม่มีขั้นอนุมัติ/ไม่บล็อกวงเงินเครดิตตอนยืนยัน ; mass-cancel และการปฏิเสธจาก portal เรียกการยกเลิกภายในที่ข้ามการตรวจล็อกของฟอร์ม | `RESTRICTED:sale/wizard/mass_cancel_orders.py:32`, `sale/controllers/portal.py:376`, `sale/models/sale_order.py:1326-1334` | ควบคุมบางส่วนอยู่ชั้น UI ; ผลต่อองค์กรที่ใช้ตัวช่วยเหล่านี้ |
| L2 | ฝั่งซื้อ: การอนุมัติขึ้นกับการตั้งค่าบริษัท (ขั้นเดียว/สองขั้น + วงเงิน) ; ผู้ไม่มีสิทธิ์กดอนุมัติจะไม่เกิดผลและไม่มีข้อความผิดพลาด | `RESTRICTED:purchase/models/purchase_order.py:615-619,1251-1259` | มี `purchase_request` (OCA) เป็นชั้นอนุมัติเพิ่มเมื่อติดตั้ง (R3) |
| L3 | การผลิต: การ "บล็อก" การบริโภคแบบยืดหยุ่นบังคับที่หน้าจอ ฝั่ง server ไม่ตรวจกลุ่ม | `RESTRICTED:mrp/wizard/mrp_consumption_warning.py:32-35` | |
| L4 | บัญชี: กฎผู้ตรวจทาน (`_is_user_able_to_review`) และสถานะ "in payment" เป็น hook ที่ Community คืนค่าเริ่มต้นและออกแบบให้ถูก override โดยโมดูล accountant (Enterprise) | `RESTRICTED:account/models/account_move.py:7014-7016,7367-7372` | ผลจริง **ขึ้นกับโมดูล accountant ที่ติดตั้ง** (`smesplus_account` depends `account_accountant`) → CONDITIONAL อย่างยิ่ง |
| L5 | ล็อกงวด (สรุปจาก PCO-01 + ตรวจอิสระโดยเอเจนต์ `account`): โพสต์ในช่วงล็อก = เลื่อนวัน ; แก้/ลบรายการที่โพสต์แล้วในช่วงล็อก = error ; hard lock ไม่มี exception ; ความไม่แก้ไขได้ (hash) เป็นรายสมุดรายวัน | `RESTRICTED:account/models/account_move.py:5702-5706,3947-3956`, `account/models/company.py:569-576` | ช่องทางข้าม: `account_update_tax_tags` (OCA) แก้ผ่านฐานข้อมูลตรง (ตามรายงานเอเจนต์ — ยังไม่ตรวจซ้ำ) |
| L6 | multi-company/IAM: กฎระดับแถวรวม global แบบ AND แล้วกลุ่มแบบ OR ; กฎบริษัทใน `base` ครอบคลุมเฉพาะบางออบเจกต์ (partner, ธนาคาร partner, อัตราแลกเปลี่ยน, บริษัท, ผู้ใช้) — sequence/attachment ไม่มีกฎบริษัทใน `base` | `RESTRICTED:base/models/ir_rule.py:113-172` (ตรวจซ้ำบางส่วน) | รายละเอียดการแยกข้อมูลข้ามบริษัทของเลขที่เอกสารยังเป็น `UNKNOWN — EVIDENCE INSUFFICIENT` |
| L7 | แรงงาน/ต้นทุน subcontract: BoM แบบ subcontract ห้ามมี operations/by-product ; ค่าจ้างมาจากบิล → PO → ราคาใบรับ ; กฎ portal 13 ข้อ/สิทธิ์ 17 ข้อ ไม่มี company | `RESTRICTED:mrp_subcontracting/models/mrp_bom.py:24-27` (ตรวจซ้ำ) | By-Product ที่เพิ่มด้วยมือใน production ที่รัน = UNKNOWN |
| L8 | Landed cost: เฉพาะ FIFO/average ; ยกเลิก/ลบไม่ได้หลัง post ; เพิ่มมูลค่าเข้า move ที่มีอยู่ | ตามโน้ต `stock_landed_costs` (ตรวจ pointer อัตโนมัติ) | ไม่ได้ตรวจซ้ำรายบรรทัด |
| L9 | ธีมเว็บไซต์ทั้ง 29 ไม่มีพฤติกรรมเชิงธุรกิจ (ไม่มี model/สิทธิ์/cron/ข้อมูลธุรกิจ) | `_themes_common` (ข้อมูลใน restricted) | โมดูลตัวแทน 3+ ตัวเท่านั้นที่เปิดโค้ดลึก |

## S6. Provenance ข้อสังเกตใน tree ต้นทาง (ส่งให้ session หลัก)
- มีไฟล์เอกสาร `STATE03_SMD_SOURCE_VERIFICATION_FINDINGS.md` อยู่ใน root ของ `addons` ใน tree ต้นทาง Community (ไม่ใช่โค้ด Odoo) — **ไม่ได้เปิดอ่าน** เพื่อรักษาความเป็นอิสระ ; เสนอให้ session หลักตรวจที่มา
- โฟลเดอร์ `theme_test_custo` อยู่ใน `addons` แต่ไม่อยู่ในทะเบียน 300 (ไม่ได้ trace)
- `l10n_account_withholding_tax_pos` เอเจนต์รายงานว่าไม่ได้อ่าน

## S7. Custom / third-party — ผลกระทบที่เพิ่มขึ้นในรอบนี้
- `purchase_request` (R3) : ใบขอซื้อคั่นระหว่าง Reordering Rule กับ RFQ เมื่อสินค้าเปิดใช้ → BRP-07 = CONDITIONAL
- `smesplus_account` / OPL-1 modules ที่ depends `stock_account`/`mrp` : ยังตรวจไม่ได้ (คงสถานะ §2)
- ลำดับถัดไปตามคำสั่ง (7): (1) 17 โมดูลแรก ทำ source-map trace แล้ว (candidate) → (2) 300 โมดูล candidate แล้ว → (3) custom/third-party impact trace ตามสิทธิ์ (ต่อ: `stock_picking_reference_no`, `scgl_account_tax_return`, `smesplus_tax_period_date`, security XML ของโมดูล custom) → (4) Function/Gap deep study ตาม risk (ต่อ: `GAP-PDT-01/02`, `GAP-SDV-02/05`, `GAP-IAV-*`, `GAP-GRV-*`, `GAP-D01-04`)

## S8. สรุปรายงาน (รูปแบบที่กำหนด)
**สิ่งที่เสร็จแล้ว**
- Module/Function : ระเบียน candidate 300/300 (S1 + trace note) ; Source Map Complete = 0 ; Gap-ID ที่มี delta = 21 (ไม่มีรายการปิด)
- remediation §4 (banner 10 ไฟล์, data-minimization) ; hash mismatch บันทึกเป็น Material Integrity Gap ; R0 ส่งต่อ BUSINESS PROCESS
**สิ่งที่กำลังทำ**
- custom/third-party impact trace ตามสิทธิ์ ; ตรวจ pointer เชิงเนื้อหาของ trace note (ตรวจแล้ว 31 จาก 11,364)
**สิ่งที่ยังไม่ทำ**
- §5.1 ข้อ 8 (schema-only ระดับโมดูล) และข้อ 9 (V-level) ทุกโมดูล ; Independent verification ; runtime validation ; Deep Study ที่เหลือ ; ตรวจโมดูล custom ที่ license ปิดเกินระดับ manifest ไม่ได้

---

# ROUND 4 — Append (2026-09-30) — Prompt: STATE03_ODOO19_ULTRA_DEEP_L1_L5_CONTINUATION (first capability/status report)

**Status:** `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` · revision `19.0.post20260921` · Community-core = `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` · no Formal Coverage / Gate PASS / gap closure / STATE03 Complete / FDS authorization claimed.

## T0. Execution incident (record)
Delegated (sub-agent) work was interrupted twice by the account **monthly spend limit** (HTTP 429): 16 agents failed in the first wave and 8 more in the retry. One small probe succeeded in between, so the limit is intermittent/at the boundary. **Effect:** all L1 content-check agents (6) and all L2+L3 function agents (8) were lost; only partial files survived (below). **Decision:** no further delegated launches until the spend limit is raised/reset (a user/administrator action) — repeated retries only burn quota. Work continues directly by the main worker where cheap.

## T1. Preflight (L0) — result
| Item | Result |
|---|---|
| Source revision | `19.0.post20260921` (from package metadata; the tree is not a git checkout, so no commit hash exists) |
| Manifest / licence | Manifest sha256 (first 16 chars) recorded in every `SOURCE_MAP_CANDIDATE/MODULE_*.md`; all 300 register modules LGPL-3 per manifest |
| `OEEL-1` | No `OEEL-1` manifest found among the 158 custom/third-party manifests inspected (licences seen: LGPL-3, AGPL-3, GPL-3, OPL-1, "Other proprietary", none). Enterprise code is not in the tree. Nothing under `OEEL-1` was opened |
| Module list provenance | **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (unchanged) |
| Dump | schema-only, sha256 recorded (see §1) ; both restores cleaned up |
| Module business boundary | stated per module in the source-map records |

## T2. What is executable now / not executable (with blocker class)
| Activity | Executable now? | Constraint / blocker class |
|---|---|---|
| L1 module map (structure) | Yes — automated extraction done for 300 + 117 custom | — |
| L1 content-check | Only by direct reading by the main worker (slow) | **tooling/quota**: delegated verifiers were cut by the spend limit |
| L2 function trace | Yes, directly (limited throughput) | quota for parallel delegates |
| L3 eight-lens study | Yes, directly, function by function | quota for parallel delegates; L3 needs ≥1 function per session-hour of reading |
| L4 independent challenge | **No** | **independent review**: requires a reviewer/session other than the author; delegated agents of this session are not independent |
| L5 runtime / AWT | **No** | **runtime/configuration + rights**: no isolated Odoo runtime is provisioned or authorized; this host has Python 3.14 (Odoo 19 targets an earlier Python) and none of the Odoo Python dependencies installed; creating one means installing packages and building an environment, which is not authorized |
| Schema-only dump study | Yes (temporary local database, no row queries) | schema-only limit: cannot show installed module set or configuration values |
| Closed-licence custom modules (41) | Manifest/metadata only | **rights/provenance** |

## T3. Actual status (no inferred status)
| Scope | Status | Count (provenance = on-disk register, hash mismatch) |
|---|---|---|
| Community register modules — L1 | `L1-CANDIDATE` (automated inventory + sub-agent trace note; content-check incomplete) | 300 |
| Community register modules — `L1 COMPLETE` | — | **0** |
| Content-check of a trace note (adversarial re-verification) | done for **1** note (`mrp`) before interruption: authoritative tally ≈ 87 claims: 60 supported, 16 partially supported, 2 not supported, 9 pointer-broken (the checker's summary table says 62 — its two tallies disagree). Pointer-existence check on all notes: 11,229 of 11,364 resolve. | 1 of 17 first-batch notes |
| Function-level L2 | `L2-CANDIDATE` for the ~21 Gap-IDs already in the Handoff (source-static, by the main worker, no independent check). Three interrupted L2+L3 drafts survive as **incomplete** restricted files (lock dates PCO-F01/F04 ≈ 53 lines; sales invoicing/COGS group ≈ 58 lines; multi-company MCT group ≈ 25 lines) — not usable as L2/L3 until completed and content-checked. The other five drafts are stubs only. | 0 `L2 COMPLETE` |
| `L3 COMPLETE` / `L4 COMPLETE` / `L5 COMPLETE` | none | 0 / 0 / 0 |
| Custom / third-party (licence-readable) | study notes exist (`L1-CANDIDATE`, not content-checked) | 117 (folder `CUSTOM_MODULE_STUDY/`) ; 41 metadata-only |

**Evidence class / max V by position:** L1-CANDIDATE → at most V2 on the maps; existing function findings are V-level *not assigned by this worker* (source/schema only, no L4/L5). Floor for C1 (V4) is **not** met by any function; every C1 function remains `GAP — REQUIRED V4/V5 / ACTUAL below V4`.

## T4. First batch and first functions to advance
- **First L1 dependency/risk batch:** the 17 core modules (`account`, `stock`, `stock_account`, `stock_landed_costs`, `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_subcontracting` + 3 bridges, `purchase`, `purchase_stock`, `sale`, `sale_stock`, `product`, `l10n_th`).
- **First Function-IDs advancing L2→L3:** `PCO-F01/F04` (lock dates; partial draft), `SDV-F04/F05/F07 + RTG-F02/F03 + PDT-F01` (sales invoicing/COGS; partial draft), `MCT-F01/F02/F03/F05` (multi-company; partial draft). Not started beyond stub: `PCO-F03 + IAV-F03/F04`, `MFG-F01/F02/F04/F05`, `BRP-F08/F03/F01/F02`, `GRV-F06 + PDT-F02/F03/F04`, `GRV-F02/F03/F04/F05/F07 + IAV`.

## T5. Custom / third-party modules mapped onto the core modules studied
New folder `CUSTOM_MODULE_STUDY/` (separate from Community results; each note carries the confirmed manifest licence): per-module notes (117) and `STATE03_CUSTOM_MODULE_IMPACT_ON_CORE_MAP.md`. `DISCOVERED RELATED MODULE — RESEARCHED FOR EFFECTIVE BEHAVIOR`: these are extensions reached from core-module traces (origin: the core modules' extension-path sections), classified Company Extra/Custom, Customer-authorized Custom or Third-party; whether scope review is recommended is for `STATE03_BUSINESS PROCESS`.

Core module → custom overlays (text-scan extension; presence ≠ installed). Function-ID = the existing register ID the overlay bears on.
| Core module (function) | Overlay → effect (leads, `CLAUDE-REPORTED`) |
|---|---|
| `account` (PCO-F01 lock dates) | `account_lock_date_update`, `om_fiscal_year`, `base_accounting_kit`: extra wizards that write company lock dates with elevated rights (core validation still runs); `om_fiscal_year` carries a dead lock-check method (core 19 uses a different name); `scgl_account_deferred`, `scgl_account_tax_return`: post extra entries, do not read or set lock dates, dates are moved by core |
| `account` (posting/cancel) | `scgl_advance_expense_request`/`smesplus_advance_expense_request`: write cancel state directly on vendor bills, skipping core cancel steps; `account_asset_management`: forced deletion of posted entries via a context flag that skips sequence-gap and audit-trail guards |
| `account` (accountant hooks) | Community hooks for reviewer rights and "in payment" state are meant to be overridden by the Enterprise accountant module; `smesplus_account` depends on it but is an incomplete skeleton on disk |
| `purchase` (GRV-F06, approvals) | `purchase_request_level_approve_po`: multi-level PO approval whose last step calls core approve directly (skips core confirmation checks and amount-based double validation); `purchase_request_level_approve`: four approval settings saved but never read; `purchase_request` (OCA): request state flow, approver from the requester's employee record, no self-approval check found |
| `purchase` (advance payment) | `scgl_purchase_advance_payment`/`smesplus_purchase_advance_payment`: create a draft vendor bill for an advance (default account is an expense account), replace the core bill-matching button, run with elevated rights; older-API constructs flagged |
| `sale` (SDV-F04, confirmation) | `sale_order_level_approve`: blocks confirmation for everyone except superuser (also affects portal auto-confirmation); `base_accounting_kit`: blocks invoice posting/SO confirmation when customer balance reaches a set amount; `product_brand_sale`: replaces core invoice creation with an older copy |
| `stock`/`stock_account` (valuation dates) | `cr_effective_date_entries`: rewrites picking/move/valuation dates and re-posts entries; references models that Odoo 19 does not have |
| `base`/IAM/multi-company | `scgl_jasper_api`: public routes reading whitelisted records with no token check and a shared token embedded in source (value not recorded); `scgl_report_viewer`/`scgl_account_reports`: raw-query reports bypassing record rules; `om_recurring_payments`, `om_account_followup`, `l10n_th_withholding_tax_report`: missing/partial company scoping |
| Thai localisation (`l10n_th`) | OCA withholding-tax modules depend on a report handler module absent from Community; several Thai add-ons use constructs removed in 19 |
| Odoo 19 compatibility (general) | Many overlays use old-style uniqueness declarations that 19 ignores, removed fields/methods, or an 17/18 version string: those rules/controls silently do not run |

## T6. Process deviations to disclose
Delegates opened (via search) `MODULES.csv` (non-module file), an OCA manifest and two module folders outside their assignment; content not used. One earlier-round statement of mine ("custom agents 9 of 9 done") was wrong and was corrected at the time (one module note was missing; now 117/117 present).

## T7. Next actions (in order; pending quota unless noted)
1. (direct) Complete PCO-F01/F04 L2/L3 from the surviving draft and re-verify against source.
2. (direct) Content-check the remaining 16 first-batch notes, starting with `account`, `stock_account`, `purchase`, `sale`.
3. (delegated, after quota is restored) Re-launch the 8 L2+L3 function studies and the L1 content-checks with incremental file writes.
4. L4 and L5 remain blocked as stated in T2.


# ROUND 5 — Append (2026-10-01) — Prompt: STATE03_ODOO19_COMMUNITY_VERY_DEEP_RESEARCH (L0–L3, DEEPSEEK PRIMARY EXECUTION)

**Status:** `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION` · source revision `19.0.post20260921` · Community only · no V-level, Module/Function Complete, coverage figure, denominator freeze, Gate PASS or Clean-Room approval claimed.

## U0. B00 checkpoint reconciliation (see `VERY_DEEP_RESEARCH_L0_L3/00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md`)
- **Material delta:** DB baseline is now `iTest19C_2026-09-21` (full backup, 356 installed Community modules, near-empty transactional data) instead of the schema-only `iTEST02_2026-06-14`. `DB_SCHEMA_ONLY/` is retained as *pre-delta baseline — re-audit required*.
- **Module universe:** source 692 · register CURRENT/NEXT/EVIDENCE 300/108/284 (content-consistent with source; hash mismatch unchanged) · dump-installed 356 (279 CURRENT, 38 NEXT, 39 EVIDENCE-ONLY) · 21 CURRENT modules not installed in the dump · runtime export (6) shows 254 installed (contradiction with the dump, recorded). No denominator is frozen.
- **Restore contract:** private PostgreSQL 18.6 cluster, Unix-socket only, 0 restore errors; cleanup pending at end of DB phase.
- **Interrupted L2/L3 drafts invalidated for reuse; function studies are redone from source.**
