> **STATUS CORRECTION — The source/schema finding is CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION. It is not runtime proof, Gate PASS, final gap closure, or STATE03 completion. Refer to STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF for the current qualified disposition.**

> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Source-code research result | **ส่วนที่ 2 — Evidence (file + line)**
> คู่กับ: `SRC_GAPS_BRP-01-02-04-05-07-08-10_BUSINESS_SUMMARY.md`

# GAP-BRP-01/02/04/05/07/08/10 — Evidence Register

## 0. ขอบเขต
| Field | Value |
|---|---|
| Source root (read-only) | `Odoo Community/odoo-19.0.post20260921/` ; path สัมพัทธ์กับ `odoo/addons/` |
| วิธี | Static read + unit test ที่แนบมา ; ไม่ได้รัน Odoo |
| Modules | `mrp`, `mrp_account`, `stock`, `stock_account`, `purchase`, `purchase_stock` |
| ไม่ได้แตะ | `addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus`, `VAT_BACKFILL_20260914`, `AUDIT_LOG_20260914`, `Claude outputs`, `MODIFY`, `.xlsx`/`.dump` |

---

## GAP-BRP-01 — BoM Type change

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP01-01 ฟิลด์ `type` — Selection `normal`/`phantom` , `required=True`, default `normal` ; ไม่มี readonly/states/lock | `mrp/models/mrp_bom.py:26-29` |
| EV-SRC-BRP01-02 ไม่มี constraint บน `type` ; `write()` ตรวจฟิลด์ `['bom_line_ids','byproduct_ids','product_tmpl_id','product_id','product_qty']` เพื่อเรียก `_set_outdated_bom_in_productions` — **`type` ไม่อยู่ในรายการ** | `mrp/models/mrp_bom.py:268-275` ; `_set_outdated_bom_in_productions` `:487-515` (จำกัดที่ MO state `draft` และ `confirmed`, 498-500 ; ตั้ง `is_outdated_bom` 504) |
| EV-SRC-BRP01-03 คำเตือน UI-only : `@api.onchange` — ถ้า `type == 'phantom'` และมี `stock.move` ที่อ้าง `bom_line_id` ของ BoM นี้ → warning "editing its structure may lead to undesirable behaviours…archive…" | `mrp/models/mrp_bom.py:212-221` |
| EV-SRC-BRP01-04 การแตก Kit ณ เวลายืนยัน/ตรวจรับ : `_bom_find(..., bom_type='phantom')` → `explode` → สร้าง phantom moves → ยกเลิก+ลบ move เดิม | `mrp/models/stock_move.py:376-407` (`action_explode`; ค้นหา BoM 386, ลบ move เดิม 403-406) |
| EV-SRC-BRP01-05 Test : ใบส่งของ confirm แล้ว → `bom_1.type = 'phantom'` → `button_validate` → move กลายเป็นส่วนประกอบ ; ไม่มี AML ของตัวสินค้าเดิม (`len(product_aml)==0`), มี AML ของส่วนประกอบ (credit 50 / debit 50) | `mrp_account/tests/test_mrp_account.py:169-207` (`test_delivery_validate_after_product_converted_to_kit`) |

## GAP-BRP-02 — Kit + Operations

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP02-01 ไม่มี constraint ห้าม `operation_ids` เมื่อ `type=='phantom'` : ค้น `phantom` ใน `mrp_bom.py` พบเฉพาะบรรทัด 29 (นิยาม), 214 (onchange warning), 354, 431 (`_bom_find` bom_type) | `mrp/models/mrp_bom.py` |
| EV-SRC-BRP02-02 Test สร้าง Kit พร้อม Operations แยกตาม variant (Red/Blue) แล้วใช้เป็นส่วนประกอบของ BoM `normal` ; ผล : `mo.workorder_ids.operation_id` = Operation ของ Kit ตรงกับ variant | `mrp/tests/test_bom.py:2872-2917` (`test_bom_with_operations_for_kit_variant`) |
| EV-SRC-BRP02-03 การสร้าง Work Order : วน `production.bom_id.explode(...)` ทั้ง BoM แม่และ BoM ย่อย ; ข้ามเมื่อ Operations ของ BoM แม่กับ BoM phantom เป็นชุดเดียวกัน (`if not (bom.operation_ids and (not bom_data['parent_line'] or bom_data['parent_line'].bom_id.operation_ids != bom.operation_ids)): continue`) | `mrp/models/mrp_production.py:606-661` (`_compute_workorder_ids` ; เงื่อนไขนี้ที่ 631-632) |
| EV-SRC-BRP02-04 MO ไม่สร้าง raw move ให้ส่วนประกอบที่เป็น `child_bom_id.type == 'phantom'` (ถูกแตกเป็นระดับล่างแทน) | `mrp/models/mrp_production.py:1347-1348` |
| EV-SRC-BRP02-05 Kit มูลค่าสต็อก = 0 เพื่อกันนับซ้ำ (`_compute_value` : `total_value = 0.0`, `avg_cost = 0.0`) ; ค่าใช้จ่ายรวมอยู่ที่ส่วนประกอบ | `mrp_account/models/product.py:101-112` ; `mrp_account/models/res_company.py:7-8` (`_get_valuation_product_domain` กรอง `is_kits = False`) |
| EV-SRC-BRP02-06 ต้นทุน Kit ต่อหน่วยคำนวณจากส่วนประกอบ | `mrp_account/models/stock_move.py:33-47` (`_get_kit_price_unit`) |

## GAP-BRP-04 — ดู `MANUFACTURING_VALUATION_PILOT/SRC_GAPS_MFG-02-03-04-05_EVIDENCE.md` EV-SRC-MFG04-01..04

## GAP-BRP-05 — ไม่มี Work Order / ส่วนต่างเวลา

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP05-01 แท็บ/ฟีเจอร์ Operations ผูกกลุ่มสิทธิ์ `mrp.group_mrp_routings` | `mrp/views/mrp_bom_views.xml:113` (และ 25, 41, 106, 164 สำหรับฟิลด์ `operation_id`/ปุ่ม) |
| EV-SRC-BRP05-02 ไม่มี Operations → `_compute_workorder_ids` ลบ/ไม่สร้าง WO (`production.workorder_ids = [Command.delete(...)]` ในกิ่ง else) ; ต้นทุนแรงงานใน `_cal_price` = Σ `_cal_cost()` ของ `workorder_ids` (ว่าง = 0) | `mrp/models/mrp_production.py:606-661` (กิ่ง else ลบ WO ที่ 659-660) ; `mrp_account/models/mrp_production.py:67-69` |
| EV-SRC-BRP05-03 `duration_percent = 100 × (duration_expected − duration) / duration_expected` (ถ้า `duration_expected` เป็น 0 → 0) ; `duration_unit = duration / max(qty_produced,1)` | `mrp/models/mrp_workorder.py:347-355` (`_compute_duration`) |
| EV-SRC-BRP05-04 ปิด MO ที่ `duration == 0.0` → `duration = duration_expected` | `mrp/models/mrp_production.py:1944-1947` ; ปุ่ม validate ของ WO ที่ `mrp/models/mrp_workorder.py:940-945` (`duration_percent = 100` ที่ 945) |
| EV-SRC-BRP05-05 ค้นไม่พบ variance/ PPV account หรือ journal entry สำหรับส่วนต่างเวลา (ค้น `variance` ใน `mrp_account`) | `mrp_account/` — ไม่มีผล |
> EV-SRC-BRP05-05 เป็นผลการค้นหาเชิงลบ (absence) — ระดับความมั่นใจต่ำกว่าหลักฐานเชิงบวก

## GAP-BRP-07 — Reordering Rule

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP07-01 `trigger` Selection `auto`/`manual`, default `auto`, required | `stock/models/stock_orderpoint.py:31-32` |
| EV-SRC-BRP07-02 Cron "Procurement: run scheduler" — `model.run_scheduler(True)`, active, `user_id = base.user_root`, ทุก 1 วัน | `stock/data/stock_sequence_data.xml:45-56` ; `run_scheduler` ที่ `stock/models/stock_rule.py:734` (`def run_scheduler`) |
| EV-SRC-BRP07-03 `_procure_orderpoint_confirm` : สร้าง `Procurement` เมื่อ `qty_to_order > 0` แล้ว `stock.rule.run(...)` — ไม่มีขั้นตอนอนุมัติ/สิทธิ์ก่อน | `stock/models/stock_orderpoint.py:712-793` (สร้าง procurement 743 ; run 750) |
| EV-SRC-BRP07-04 กรณีล้มเหลว : จับ `ProcurementException` , ตัดออกจากชุด , สร้าง `mail.activity` (warning) บน product template ให้ `responsible_id` หรือ SUPERUSER | `stock/models/stock_orderpoint.py:751-785` (except 751 ; activity_schedule 779) |
| EV-SRC-BRP07-05 MO จาก Reordering Rule : `_should_auto_confirm_procurement_mo` — ไม่มี raw move → ยืนยันอัตโนมัติเมื่อ ไม่มี WO และ (มี orderpoint หรือ MTS) ; มี raw move → `return not p.orderpoint_id` (คือ **ไม่ยืนยัน** ถ้ามาจาก orderpoint) | `mrp/models/stock_rule.py:35-38` ; ใช้ที่ `:120` |
| EV-SRC-BRP07-06 การสร้าง MO ใช้ `SUPERUSER` + `sudo()` | `mrp/models/stock_rule.py:117-121` |
| EV-SRC-BRP07-07 PO/RFQ default `state='draft'` ; ตั้ง `po_double_validation` ที่บริษัท (`one_step`/`two_steps`) และวงเงิน `po_double_validation_amount` (default 5000) | `purchase/models/purchase_order.py:111` ; `purchase/models/res_company.py:16-22` ; `purchase/models/purchase_order.py:1255` (การตรวจ `one_step`) |
| EV-SRC-BRP07-08 `purchase_stock/models/stock_rule.py` ไม่พบการเรียก `button_confirm`/`auto_confirm` (ค้นแล้ว) | `purchase_stock/models/stock_rule.py` — ผลค้นเชิงลบ |
| EV-SRC-BRP07-09 สิทธิ์ : `stock.group_stock_user` อ่านอย่างเดียว ; `stock.group_stock_manager` CRUD เต็ม | `stock/security/ir.model.access.csv:19-20` |

## GAP-BRP-08 — MPS

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP08-01 รายชื่อโมดูลชื่อขึ้นต้น `mrp` ทั้งหมดใน Community : `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_product_expiry`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`, `mrp_subcontracting_repair` — **ไม่มี `mrp_mps`** | `ls odoo/addons | grep -iE "^mrp|mps|plan|quality"` |
| EV-SRC-BRP08-02 ร่องรอยในโค้ด `mrp` : ไม่ค้นหา MO เดิมมาผนวกเมื่อ `procurement.origin == 'MPS'` | `mrp/models/stock_rule.py:90` |
| EV-SRC-BRP08-03 ค้น `quality` , `planning` : ไม่พบโมดูลชื่อดังกล่าว (เกี่ยวกับ `GAP-QCP-02`) | คำสั่งเดียวกับ EV-SRC-BRP08-01 |

## GAP-BRP-10 — Re-costing

| Evidence | ที่ |
|---|---|
| EV-SRC-BRP10-01 `stock.move.value` เป็น `fields.Monetary` ที่เก็บค่า (ไม่มี `compute`) ; ตั้งค่าใน `_set_value` ตอน `_action_done` | `stock_account/models/stock_move.py:24-26` (นิยาม) ; `:292-357` (`_set_value` : ขาเข้า `move.value = move.sudo()._get_value()` 321 ; ขาออก FIFO 348 / standard 351) |
| EV-SRC-BRP10-02 ต้นทุน MO รอบนั้น = Σ `move.value` ของ raw moves ที่ done | `mrp_account/models/mrp_production.py:74` |
| EV-SRC-BRP10-03 FG move ตั้ง `price_unit` ณ รอบผลิต ; `_get_value_from_production` = `quantity × price_unit` | `mrp_account/models/mrp_production.py:86,91,93` ; `mrp_account/models/stock_move.py:11-23` |
| EV-SRC-BRP10-04 แก้ `standard_price` (ไม่ใช่ FIFO) → `_change_standard_price` สร้าง `product.value` (ปรับมูลค่า) ลงวันที่ปัจจุบัน ; FIFO ถูกข้าม (`if product.cost_method == 'fifo' or product.standard_price == old_price: continue`) ; ปิดได้ด้วย context `disable_auto_revaluation` | `stock_account/models/product.py:286-296` (write) ; `:302-326` (`_change_standard_price`) |
| EV-SRC-BRP10-05 ราคามาตรฐาน ณ วันที่ในอดีตหาได้จาก `product.value` | `stock_account/models/product.py:328-336` (`_get_standard_price_at_date`) |
| EV-SRC-BRP10-06 ปุ่ม "คำนวณราคาจาก BoM" ใช้ `standard_price` ปัจจุบันของส่วนประกอบ ; recursion ตาม `child_bom_id` เฉพาะที่อยู่ใน `boms_to_recompute` | `mrp_account/models/product.py:44-99` (`action_bom_cost`, `_set_price_from_bom`, `_compute_bom_price` : ส่วนประกอบ 76-85) |
| EV-SRC-BRP10-07 Landed cost เพิ่มมูลค่าให้ move ที่ done (`_get_value_from_extra` อยู่ในลำดับหามูลค่า) | `stock_account/models/stock_move.py:363-448` (`_get_value_from_extra` เรียกที่ 439) |
> สิ่งที่ **ไม่ได้ตรวจ** : เส้นทางที่ vendor bill/`account.move` ทำให้ `_set_value` ถูกเรียกซ้ำกับ move ของ MO ที่เสร็จแล้ว (ขึ้นกับ `purchase_stock`/`account` — R-B4/R-M4)

## ข้อควรระวังในการอ้างหลักฐาน
- เลขบรรทัดอ้างอิง tree ณ 2026-09-30 ; ช่วงบรรทัดตรวจด้วย grep แล้ว ยกเว้นช่วงกว้างของฟังก์ชันที่ระบุเป็นช่วง
- ผลค้นเชิงลบ (absence) แจ้งกำกับไว้ ระดับมั่นใจต่ำกว่าหลักฐานเชิงบวก
- ข้อเสนอเปลี่ยนสถานะเป็นการตัดสินใจของ Boss
