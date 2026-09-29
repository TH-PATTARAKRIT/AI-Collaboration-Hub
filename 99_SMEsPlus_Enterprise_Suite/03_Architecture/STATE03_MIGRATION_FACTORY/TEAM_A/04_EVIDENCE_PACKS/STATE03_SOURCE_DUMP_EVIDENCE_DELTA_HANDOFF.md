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
