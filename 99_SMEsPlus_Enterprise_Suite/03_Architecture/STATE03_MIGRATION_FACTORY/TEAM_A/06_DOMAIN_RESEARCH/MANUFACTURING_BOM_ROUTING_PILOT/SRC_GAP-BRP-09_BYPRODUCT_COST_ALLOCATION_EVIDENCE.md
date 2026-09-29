> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Source-code research result | **ส่วนที่ 2 — Evidence (file + line)**
> คู่กับ: `SRC_GAP-BRP-09_BYPRODUCT_COST_ALLOCATION_BUSINESS_SUMMARY.md`

# GAP-BRP-09 — Evidence Register

## 0. ขอบเขตและวิธีการ

| Field | Value |
|---|---|
| Source root (read-only) | `Odoo Community/odoo-19.0.post20260921/` (`PKG-INFO` Version: `19.0.post20260921`; `odoo/release.py:15` `version_info = (19, 0, 0, FINAL, 0, '')`) |
| Path ที่อ้างต่อไปนี้ | สัมพัทธ์กับ `<root>/odoo/addons/` |
| วิธี | Static read + อ่าน unit test ที่ Odoo แนบมา (ไม่รัน Odoo) |
| โฟลเดอร์ที่ **ไม่ได้แตะ** | `addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus`, `VAT_BACKFILL_20260914`, `AUDIT_LOG_20260914`, `Claude outputs`, `MODIFY`, ไฟล์ `.xlsx`/`.dump` |
| Modules ที่อ่าน | `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_subcontracting_account`, `stock_account` |
| วิธีค้นหา | `grep cost_share` ข้าม `mrp`, `mrp_account`, `stock_account`, `stock`, `mrp_subcontracting*`, `mrp_landed_costs` |

---

## EV-SRC-BRP09-01 — นิยามฟิลด์ Cost Share (%)

| ที่ | หลักฐาน |
|---|---|
| `mrp/models/mrp_bom.py:871-874` | ฟิลด์ `cost_share` บน `mrp.bom.byproduct` — Float, label "Cost Share (%)", `digits=(5, 2)` (comment ในโค้ด: "decimal = 2 is important for rounding calculations"); help text: เปอร์เซ็นต์ของต้นทุนผลิตสุดท้ายของบรรทัด by-product (แบ่งตามจำนวนที่ผลิต); ผลรวมต้อง ≤ 100 |
| `mrp/models/stock_move.py:56-58` | ฟิลด์ `cost_share` บน `stock.move` (สำเนาที่ MO) — Float `digits=0`, help text เดียวกัน |
| ค่า default | ทั้งสองฟิลด์ **ไม่มี default ระบุ** → 0. `_get_move_finished_values(..., cost_share=0)` ที่ `mrp/models/mrp_production.py:1274` |

**ข้อสรุป:** วิธีปันส่วน = เปอร์เซ็นต์ที่ผู้ใช้กำหนดต่อบรรทัด By-Product; ค่าเริ่มต้น 0.

## EV-SRC-BRP09-02 — ตรรกะคำนวณต้นทุนตอน MO ผลิต (แกนหลัก)

`mrp_account/models/mrp_production.py:57-94` — `MrpProduction._cal_price(consumed_moves)`

| บรรทัด | สิ่งที่ทำ |
|---|---|
| 60 | เรียก `super()._cal_price` (base เป็น no-op ที่ `mrp/models/mrp_production.py:1903-1905`) |
| 64-66 | เลือก finished move ของสินค้าหลักที่ยังไม่ done/cancel และ quantity > 0 |
| 67-72 | รวม `work_center_cost += work_order._cal_cost()` ทุก work order |
| 73 | `extra_cost = self.extra_cost * quantity` |
| 74 | `total_cost = Σ move.value ของ consumed_moves + work_center_cost + extra_cost` |
| 76-78 | เลือก by-product moves ที่ไม่ done/cancel และ quantity > 0 |
| 79-81 | สะสม `byproduct_cost_share += byproduct.cost_share` (สะสม **ก่อน** เช็คชนิดต้นทุน → นับรวมแม้ By-Product เป็น Standard) |
| 82-86 | ถ้า By-Product เป็น `fifo`/`average`: **ถ้า cost_share ≈ 0 (2 ทศนิยม) → `continue`** (ไม่ตั้ง `price_unit`); ไม่เช่นนั้น `price_unit = total_cost × cost_share / 100 / byproduct_qty` (qty แปลงเป็น UoM ของสินค้า, ถ้า qty=0 → 0) |
| 87-88 | ถ้าไม่ใช่ fifo/average (standard): `price_unit = product.standard_price` |
| 90-91 | สินค้าหลักไม่ใช่ fifo/average: `price_unit = standard_price` |
| 92-93 | สินค้าหลัก fifo/average: `price_unit = total_cost × float_round(1 − byproduct_cost_share/100, precision_rounding=0.0001) / quantity` |

**Call site:** `mrp/models/mrp_production.py:1907` (`_post_inventory`) → เรียก `order._cal_price(moves_to_do_by_order[order.id])` ที่ **1948** *หลัง* consume วัตถุดิบ (`_action_done` ที่ 1917) และ *ก่อน* finish moves `_action_done` (1949-1951). ⇒ ราคาต่อหน่วยถูกตั้งก่อนที่ move ผลิตจะถูก valued.

**การคำนวณ `Σ move.value` มาจาก move วัตถุดิบที่ done แล้ว** (`moves_to_do`, 1919) — เป็นมูลค่าตามวิธีต้นทุนของวัตถุดิบ.

## EV-SRC-BRP09-03 — กรณี cost_share = 0 ⇒ มูลค่า 0 (ยืนยันความเสี่ยง C1)

1. `mrp_account/models/mrp_production.py:83-84` — `continue` โดยไม่ตั้ง `price_unit` (ฟิลด์ `price_unit` ของ stock.move ไม่มี default → 0: `stock_account/models/stock_move.py:38` `price_unit = fields.Float("Price Unit")`; `stock/models/stock_move.py:129`)
2. `mrp_account/models/stock_move.py:11-23` — `_get_value_from_production` (สำหรับ move ที่มี `production_id`) คืน `value = quantity × self.price_unit` และรายงาน quantity ที่ valued ครบ
3. `stock_account/models/stock_move.py:363-448` (`_get_value_data`): ขั้นตอนที่ 2 เรียก `_get_value_from_production` (บรรทัด **410**) แล้ว `remaining_qty -= production_data["quantity"]` ⇒ remaining = 0 ⇒ **ไม่ตกไปใช้ standard price (ขั้น 4)**
4. ผลรวม: By-Product ที่ cost_share = 0 (FIFO/AVCO) → `value = 0`; สินค้าหลักใช้ `(1 − 0)` = ต้นทุนเต็ม (บรรทัด 93)

> ข้อ 1-3 เป็นการ **ไล่โค้ด (inference จากการอ่าน)**, ไม่ได้รันยืนยัน. ไม่พบ test ที่ยืนยัน "By-Product ค่า 0 → value 0" ตรงๆ; test ที่ใกล้ที่สุดคือ landed cost (EV-SRC-BRP09-08).

## EV-SRC-BRP09-04 — ข้อจำกัด/Validation ของ Cost Share

| ที่ | กฎ |
|---|---|
| `mrp/models/mrp_bom.py:205-206` | `cost_share < 0` ⇒ `ValidationError` "By-products cost shares must be positive." |
| `mrp/models/mrp_bom.py:207-210` | ต่อทุก variant ของ template: ผลรวม cost_share ของบรรทัด (ไม่ skip ตาม variant และ `product_qty` ไม่เป็นศูนย์) เมื่อ `float_compare(..., 100, precision_digits=2) > 0` ⇒ `ValidationError` "The total cost share for a BoM's by-products cannot exceed 100." |
| `mrp/models/mrp_bom.py:198-204` | By-Product ห้ามเป็นสินค้าเดียวกับ BoM |
| `mrp/models/mrp_production.py:979-985` | `_check_byproducts` (`@api.constrains('move_finished_ids')`): cost_share ติดลบ ⇒ error; ผลรวม (ไม่นับ state `cancel`) > 100 ⇒ error "…cannot exceed 100." |
| `mrp/models/mrp_production.py:1305` | `UserError` ถ้าสินค้าหลักของ MO อยู่ในรายการ By-Product ของ BoM |
| ไม่พบ | กฎบังคับผลรวม = 100; warning เมื่อ cost_share = 0 |

**Tests ยืนยัน:** `mrp/tests/test_byproduct.py:376-` (`test_check_byproducts_cost_share`: 120 ⇒ error, −10 ⇒ error, 60+70 ⇒ error), `:427-` (`_02`: ผลรวม <100 กับ cancelled move ไม่ error), `mrp/tests/test_bom.py:3043-3134` (variant-aware constraint).

## EV-SRC-BRP09-05 — การถ่ายค่า % จาก BoM → MO

| ที่ | สิ่งที่ทำ |
|---|---|
| `mrp/models/mrp_production.py:1301-1317` | `_get_moves_finished_values`: สร้าง move By-Product จาก `bom_id.byproduct_ids` ส่ง `byproduct.cost_share` เข้า `_get_move_finished_values` (1316) และคำนวณ qty ตามสัดส่วน `qty = byproduct.product_qty × (product_uom_factor / bom.product_qty)` |
| `mrp/models/mrp_production.py:2616` (`_link_bom`), `:2750`, `:2761` | ตอนผูก/เปลี่ยน BoM ของ MO: `move_byproduct.cost_share = bom_byproduct.cost_share` และสร้าง move ใหม่ด้วย `bom_byproduct.cost_share` |
| `mrp/models/mrp_production.py:1257` | ตอน "Generate BoM from MO" ส่ง `cost_share` จาก move กลับไปยังบรรทัด By-Product ของ BoM ใหม่ |
| `mrp/tests/test_bom.py:1600-1625` | test: ตั้ง MO cost_share=50, generate BoM, แก้ BoM เป็น 10 ⇒ MO ได้ 10 (ยืนยัน sync) |

## EV-SRC-BRP09-06 — Standard cost × FIFO/AVCO (การจัดการกรณีปน)

`mrp_account/tests/test_valuation_operation.py`

| บรรทัด | Test | ผลที่ Odoo ยืนยัน |
|---|---|---|
| 13-47 | `test_fifo_byproduct` | FIFO glass, AVCO By-Product (scrap wood ×2 บรรทัด: 8 หน่วย 1%, 1 โหล 12%); สินค้าหลักมูลค่า = `(PRICE+10) × (1−0.13)`; By-Product `price_unit = (P+N)/800` และ `(P+N)/100` (`total×share%/qty_in_product_uom`, มี multi-UoM); ยืนยัน backorder รอบ 2 |
| 83-91 | `test_standard_finished_byproduct_price_unit` | ทั้งคู่ Standard ⇒ `price_unit` ของ By-Product = 30.0 (standard) "the MO has no influence" |
| 93-108 | `test_fifo_finished_standard_byproduct_price_unit` | By-Product Standard + สินค้าหลัก FIFO ⇒ By-Product `price_unit` = 30.0 (standard); docstring: "Their cost_share is still deducted from the finished product so no value disappears from inventory"; สินค้าหลัก = `total_cost × (1 − Σ cost_share/100)` |

`mrp_account/tests/common.py:250-273` — ข้อมูล test: cost_share 1 และ 12 (รวม 13).

> ข้อสังเกต: docstring ที่บรรทัด 95-96 ระบุเจตนา "ไม่ให้มูลค่าหาย" แต่ตัวเลข By-Product ที่ลงสต็อกคือ standard_price × qty (ไม่ใช่ total×share%) — ผลต่างระหว่างสองค่านี้ ไม่มีโค้ดที่นำไปปรับใน `_cal_price`. ที่ไปของส่วนต่าง = **inference** จากกฎบัญชีใน EV-SRC-BRP09-07.

## EV-SRC-BRP09-07 — การลงบัญชี GL ของ move ผลิต

`stock_account/models/stock_move.py:229-250` — `_get_account_move_line_vals`

- ถ้า `location_id.valuation_account_id` มี (ต้นทางเป็น location ที่มีบัญชี — เช่น Production location): **Dr `stock_valuation` (ของสินค้า) / Cr บัญชีของ location** ด้วย `_get_aml_value()` = `self.value` (บรรทัด 249-250)
- ทิศตรงข้ามสำหรับ move ออก
- ⇒ การลงบัญชีอิง `value` ของ move ตัวต่อตัว; ไม่มีการลงบัญชีระดับ MO ที่ "ปรับสมดุล" ผลต่างระหว่างต้นทุนที่บริโภคกับมูลค่าผลผลิต ⇒ ผลต่างใดๆ ระหว่างต้นทุนที่บริโภค (Dr บัญชี Production) กับมูลค่าผลผลิตที่รับเข้า (Cr บัญชี Production) จะค้างสุทธิอยู่ในบัญชีของ Production location (`property_stock_production`) — สำหรับกรณีปกติ (ต้นทุนแบ่งครบ) บัญชีนี้หักลบเป็นศูนย์ โดย Labour ก็ถูกบันทึก Dr บัญชี Production / Cr บัญชีค่าใช้จ่าย ที่ `mrp_account/models/mrp_production.py:101-139` (`_post_labour`) ดังนั้นต้นทุนแรงงานเข้าไปอยู่ในมูลค่าสินค้าสำเร็จรูป
- **สถานะ:** inference จากการอ่านโค้ด ไม่ได้รัน

## EV-SRC-BRP09-08 — Landed Cost ตัด By-Product ที่ cost_share = 0

- `mrp_landed_costs/models/stock_landed_cost.py:23-28` — `_get_targeted_move_ids`: รวม `mrp_production_ids.move_finished_ids` แล้ว **หักออก** `move_byproduct_ids.filtered(lambda move: not move.cost_share)`
- test: `mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:176-` (`test_landed_cost_on_mrp_03`): By-Product1 cost_share=100, By-Product2 cost_share=0 ⇒ `assertFalse(byproduct2 in valuation_adjustment_lines.product_id)`

## EV-SRC-BRP09-09 — รายงาน

| ที่ | ผล |
|---|---|
| `mrp/report/mrp_report_mo_overview.py:429-` (`_get_byproducts_data`, 438-442) | ต้นทุนของ By-Product ในรายงาน MO Overview = ต้นทุน MO/BoM/จริง × `cost_share/100` |
| `mrp/report/mrp_report_mo_overview.py:143-170` (`_get_cost_breakdown_data`) | เฉพาะ MO `done`; **ข้าม By-Product ที่ cost_share ≈ 0 (บรรทัด 154)**; ต้นทุนหน่วยของสินค้าหลัก = ต้นทุนจริง × `remaining_cost_share` ÷ qty |
| `mrp/tests/test_stock_report.py:44,110-118` | cost_share=1.8 ⇒ 1.8% × 400 = 7.2; ÷18 หน่วย = 0.4 |
| `mrp/report/mrp_report_bom_structure.py:322-325`, `:420-445` | โครงสร้าง BoM: `cost_share` ของสินค้าหลัก = `1 − Σ share`; ต้นทุน By-Product = `round(total × share)`; บรรทัดที่ `product_qty ≤ 0` นับ share = 0 |

## EV-SRC-BRP09-10 — "คำนวณราคาจาก BoM" (สำหรับ Standard price)

`mrp_account/models/product.py:44-99`

- `_set_price_from_bom` (51-61): มี BoM ของสินค้า ⇒ `standard_price = _compute_bom_price(bom)`; ไม่มี ⇒ หา BoM ที่สินค้านี้เป็น By-Product แล้วเรียกด้วย `byproduct_bom=True` (ตั้งราคาเมื่อ price ≠ 0)
- `_compute_bom_price` (63-99): รวม operation cost + วัตถุดิบ (recursive ตาม child BoM); โหมดสินค้าหลัก: `total *= float_round(1 − Σ share/100, 0.0001)` (95-97) แล้วหาร qty; โหมด By-Product: `total × Σ share(ของสินค้านี้) / 100 / Σ qty` (86-93)

## EV-SRC-BRP09-11 — UI visibility

| ที่ | หลักฐาน |
|---|---|
| `mrp/views/mrp_bom_views.xml:162` | `<field name="cost_share" optional="hide"/>` บนตาราง By-Product ของ BoM (ซ่อนเป็นค่าเริ่มต้น) |
| `mrp/views/mrp_production_views.xml:514` | `<field name="cost_share" optional="hide"/>` บน By-Product ของ MO (ซ่อนเป็นค่าเริ่มต้น) |
| `mrp/views/mrp_production_views.xml:403` | มี `cost_share` แบบไม่ optional ในมุมมอง list ย่อยหนึ่ง (comment "Required for test_fifo_byproduct") — ไม่ใช่มุมมองหลักของผู้ใช้ |
| `mrp/views/mrp_bom_views.xml:150` + `mrp/models/res_config_settings.py:10-11` + `mrp/security/mrp_security.xml:31` | แท็บ By-Products ถูกจำกัดด้วยกลุ่ม `mrp.group_mrp_byproducts` (setting "By-Products") |

## EV-SRC-BRP09-12 — Subcontracting (เท่าที่ตรวจ)

`mrp_subcontracting_account/models/mrp_production.py:10-22` — `_cal_price` ตั้ง `extra_cost` จากบิล/PO/ราคาบนใบรับ แล้วเรียก `super()._cal_price` ⇒ ผ่านตรรกะ EV-SRC-BRP09-02 เหมือนเดิม. **ไม่ได้ตรวจกรณี subcontract BoM ที่มี By-Product** (→ residual R2)

## EV-SRC-BRP09-13 — Unbuild (residual R1)

- `mrp/models/mrp_unbuild.py:263-267`: unbuild สร้าง move ของ By-Product จาก BoM (`_generate_move_from_bom_line(... byproduct_id=byproduct.id)`) — ไม่พบการอ้าง `cost_share`/`price_unit` ในไฟล์นี้
- `mrp_account/tests/test_valuation_operation.py:49-81` — test `test_average_cost_unbuild_with_byproducts` **ถูก comment ปิดทั้งบล็อก** ⇒ ไม่มีหลักฐาน test ที่ยืนยันมูลค่า unbuild ของ By-Product ใน 19.0.post20260921
- ไม่ได้อ่านกลไกคำนวณมูลค่า unbuild ใน `stock_account` ต่อ ⇒ ยังไม่สรุป

---

## สรุปความสัมพันธ์กับ Evidence เดิมใน `19_PROVENANCE_REGISTER.md`

| EV เดิม | สถานะหลังงานนี้ |
|---|---|
| `EV-BRP-13` (third-party listing, V12 app) | **ถูก supersede ในประเด็น 19.0** — พฤติกรรม "ไม่ปันเลย" เป็นผลเมื่อ cost_share=0; core 19.0 มีกลไก % ในตัว |
| `EV-BRP-14` (forum V12) | เช่นเดียวกัน — pre-19, ไม่ใช้เป็นฐานสำหรับ 19.0 |
| `EV-BRP-11` (official doc byproducts.html) | ไม่ขัดแย้ง — doc หน้านั้นไม่ได้พูดถึง cost allocation, source ระบุกลไกชัดเจน |

## ข้อควรระวังในการอ้างหลักฐาน

- เลขบรรทัดอ้างอิงจาก tree `odoo-19.0.post20260921` ณ วันที่อ่าน (2026-09-30); ถ้า source อัปเดตเลขอาจเลื่อน
- EV-SRC-BRP09-03 (ข้อ 1-3) และ EV-SRC-BRP09-07 เป็น **การไล่โค้ด** ไม่ใช่ test ที่รันแล้ว — เสนอให้ AWT ยืนยันตัวเลขเมื่อมี runtime
