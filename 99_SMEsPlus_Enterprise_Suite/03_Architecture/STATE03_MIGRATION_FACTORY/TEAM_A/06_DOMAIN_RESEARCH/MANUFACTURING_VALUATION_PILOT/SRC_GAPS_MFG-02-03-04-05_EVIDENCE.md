> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Source-code research result | **ส่วนที่ 2 — Evidence (file + line)**
> คู่กับ: `SRC_GAPS_MFG-02-03-04-05_BUSINESS_SUMMARY.md`

# GAP-MFG-02/03/04/05 — Evidence Register

## 0. ขอบเขตและวิธีการ

| Field | Value |
|---|---|
| Source root (read-only) | `Odoo Community/odoo-19.0.post20260921/` ; path ต่อไปนี้สัมพัทธ์กับ `odoo/addons/` |
| วิธี | Static read + unit test ที่แนบมากับ source ; **ไม่ได้รัน Odoo** |
| Modules ที่อ่าน | `stock_account`, `mrp`, `mrp_account`, `l10n_th` |
| โฟลเดอร์ที่ไม่ได้แตะ | `addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus`, `VAT_BACKFILL_20260914`, `AUDIT_LOG_20260914`, `Claude outputs`, `MODIFY`, `.xlsx`/`.dump` |

---

## GAP-MFG-02 — Production Account ไม่ได้ตั้ง

### EV-SRC-MFG02-01 — เงื่อนไขสร้าง journal entry ของ stock move
`stock_account/models/stock_move.py:659-666` `_should_create_account_move` — คืน True เมื่อ **ทุกข้อ**: `product_id.is_storable` ∧ `is_valued` ∧ (`location_dest_id.valuation_account_id` ∨ `location_id.valuation_account_id`) ∧ quantity ≠ 0 ∧ `product_id.valuation == 'real_time'`.

### EV-SRC-MFG02-02 — การข้ามเป็นแบบเงียบ
`stock_account/models/stock_move.py:193-215` `_create_account_move` — วนเฉพาะ move ที่ `_should_create_account_move()` เป็นจริง ; ถ้าไม่มีบรรทัดสะสม (`if not aml_vals_list`) → `return self.env['account.move']` (ว่าง) **ไม่มี raise/warning**.
เรียกจาก `_action_done` ที่ `:177-191` (บรรทัด 187 `moves._create_account_move()`) และจาก `create` ที่ `:157-162`.

### EV-SRC-MFG02-03 — มูลค่าของ move ยังถูกตั้งแม้ไม่มี journal entry
`stock_account/models/stock_move.py:177-191` — `_set_value()` (อยู่ก่อน `_create_account_move` และไม่ขึ้นกับบัญชี) ; ฟิลด์ `value` เป็น Monetary ที่เก็บค่า (`:24-26`).
⇒ subledger (มูลค่า move) กับ GL (account.move) แยกได้ — *inference จากลำดับโค้ด ไม่ได้รัน*.

### EV-SRC-MFG02-04 — นิยามฟิลด์บัญชีของ location
`stock_account/models/stock_location.py:11-14` — `valuation_account_id` Many2one `account.account` "Stock Valuation Account", help: "Expense account used to re-qualify products removed from stock and sent to this location". ไม่มี default/required.
`stock_account/models/stock_location.py:36-41` — `_should_be_valued`: มี company ∧ `usage ∈ {internal, transit}` (Production location เป็น external → move เข้า/ออกจึงเป็น in/out ที่ valued).

### EV-SRC-MFG02-05 — Labour ข้ามเงียบด้วยเงื่อนไขเดียวกัน
`mrp_account/models/mrp_production.py:101-105` — `_post_labour`: `continue` เมื่อ `product_id.valuation != 'real_time'` หรือ `not production_location.valuation_account_id`.

### EV-SRC-MFG02-06 — แม่แบบผังบัญชีไทยไม่ตั้งบัญชี location
`l10n_th/models/template_th.py:8-17` — `_get_th_template_data`: ตั้ง `property_stock_valuation_account_id = l10n_th_account_113100` เท่านั้น (ไม่มีคีย์เกี่ยวกับบัญชี Production/location) ; `:20-45` `_get_th_res_company`: `account_stock_valuation_id = l10n_th_account_113100` , `expense_account_id`, `income_account_id` ฯลฯ — ไม่มี WIP/Production.
ค้นทั้งต้นไม้ `grep valuation_account_id` พบเฉพาะไฟล์แม่แบบ `l10n_*` (ตั้งบัญชีสต็อกของหมวดสินค้า), `stock_account/models/*`, `mrp_account/*` — ไม่มี data file ที่ตั้ง `valuation_account_id` ให้ stock.location.
> ขอบเขตการอ้าง: "ไม่มี default ใน source/แม่แบบ" ≠ "ฐานข้อมูลลูกค้าไม่มีการตั้งค่า"

---

## GAP-MFG-03 — Partial completion

### EV-SRC-MFG03-01 — คำนวณราคาทุกรอบที่ post
`mrp/models/mrp_production.py:1907-1955` `_post_inventory` : 1917 consume วัตถุดิบ `_action_done`; 1919 คัดเฉพาะ move ที่เพิ่ง done ในรอบนี้ (`moves_to_do`); 1948 เรียก `_cal_price(moves_to_do_by_order[...])`; 1949-1951 finish moves `_action_done`.
`mrp_account/models/mrp_production.py:57-94` `_cal_price` — total_cost = Σ value ของ consumed_moves รอบนี้ + Work Center cost + `extra_cost × quantity` ; quantity = ผลรวมของ finished moves ที่ยังไม่ done ในรอบนี้ (64-73).

### EV-SRC-MFG03-02 — Backorder คัดลอก Extra Unit Cost
`mrp_account/models/mrp_production.py:96-99` `_get_backorder_mo_vals` → `res['extra_cost'] = self.extra_cost`.

### EV-SRC-MFG03-03 — Test FIFO + backorder
`mrp_account/tests/test_valuation_operation.py:13-47` `test_fifo_byproduct`: glass FIFO ล็อต 10 และ 20 (`_make_in_move` 20-21) ; produce 1 จาก 2 (`_produce(mo, 1)`, 24) ; backorder (25-28) ; หลังรอบ 1 `glass.total_value == 20` (29) ; หลังรอบ 2 `glass.total_value == 0` (34) ; มูลค่า FG รอบ 2 สะสมเป็น `(2·PRICE+30)·(1−share)` (35) — ยืนยันว่าแต่ละรอบใช้ต้นทุนวัตถุดิบ FIFO ของรอบนั้น.

### EV-SRC-MFG03-04 — Labour ไม่ซ้ำเมื่อ backorder
`mrp_account/models/mrp_production.py:141-144` `_post_inventory` → `self.filtered(state == 'done')._post_labour()` (ลง Labour เฉพาะ MO ที่ done) ; `:107-108` `if mo.workorder_ids.time_ids.account_move_line_id: continue` (กันซ้ำ).
Test `mrp_account/tests/test_mrp_account.py:603-648` `test_labor_move_not_duplicated_when_backorder_always` : ตั้ง `create_backorder='always'` , WO 100 ชิ้น ผลิต 50 → `len(labour_moves) == 1`.

### EV-SRC-MFG03-05 — ใช้เวลาคาดหมายเมื่อไม่มีเวลาจริง
`mrp/models/mrp_production.py:1938-1947` (ใน `_post_inventory`): WO ที่ยัง ไม่ done/cancel → `duration_expected = _get_duration_expected()` ; `duration == 0.0` → `duration = duration_expected` และ `duration_unit = round(duration / max(qty_produced,1), 2)`.
Backorder ปรับเวลาคาดหมายใหม่: `mrp/models/mrp_production.py:2194-2196`.

---

## GAP-MFG-04 (และ GAP-BRP-04) — อัตราต้นทุน Work Center

### EV-SRC-MFG04-01 — อัตราเป็นตัวเลขเดียว
`mrp/models/mrp_workcenter.py:41` — `costs_hour = fields.Float(string='Cost per hour', help='Hourly processing cost.', default=0.0, tracking=True)` ; `:42-43` `time_start` (Setup Time) / `time_stop` (Cleanup Time). ค้น `employee|shift|overtime` ใน `mrp_workcenter.py` พบเพียง comment เรื่อง extra hours (บรรทัด ~490) — **ไม่มีฟิลด์อัตราตามกะ/OT**.

### EV-SRC-MFG04-02 — Snapshot อัตราที่ WO และเลือกมูลค่า
`mrp/models/mrp_workorder.py:124-130` — `costs_hour` (comment: "hourly cost of workcenter at time of work order completion (i.e. to keep a consistent cost)") ; `cost_mode` selection (`actual`/`estimated`) "should only be changed once at MO confirmation".
`mrp/models/mrp_workorder.py:729` — ตอนสิ้นสุด WO ตั้ง `'costs_hour': workorder.workcenter_id.costs_hour`.
`mrp/models/mrp_workorder.py:638-654` `_cal_cost(date=False)` — ถ้า `_should_estimate_cost()` ใช้ `duration_expected/60` ไม่เช่นนั้นรวม interval ของ `time_ids` ที่มี `date_end` ; คูณ `(workorder.costs_hour or workcenter.costs_hour)`.
`mrp/models/mrp_workorder.py:900-902` `_should_estimate_cost` : state ∈ {progress, done} ∧ `duration_expected` ∧ `cost_mode == 'estimated'`.
`mrp/models/mrp_workorder.py:956-959` `_set_cost_mode` "should only be called once when the MO is confirmed" (เรียกที่ `mrp/models/mrp_production.py:1659`).
`mrp/models/mrp_routing.py:60-64` — `cost_mode` ต่อ Operation ("Actual time" / "Theorical time"), help อ้างถึง "real employee costs".
`mrp/models/mrp_routing.py:134-136` `_compute_cost` — `cost = (time_total / 60.0) × workcenter.costs_hour`. `:100-118` `time_total` รวม setup+cleanup+รอบ×เวลา/ประสิทธิภาพ.
Test `mrp_account/tests/test_mrp_account.py:576-588` `test_estimated_cost_valuation` : WO `duration=60` → `_cal_cost()==600` ; ปิด MO แล้วเปลี่ยน `costs_hour` เป็น 333 → ยัง `600`.

### EV-SRC-MFG04-03 — ไม่มี Overhead rate แยก
`mrp_account/models/mrp_production.py:13` `extra_cost` "Extra Unit Cost" (ระดับ MO) ; `stock_account/models/res_company.py:16-17` `account_production_wip_account_id`, `account_production_wip_overhead_account_id` (ใช้ใน WIP wizard เท่านั้น — ดู MFG-05).

### EV-SRC-MFG04-04 — การลงบัญชีแรงงาน
`mrp_account/models/mrp_production.py:110-137` `_post_labour` : เลือกบัญชี `wo.workcenter_id.expense_account_id or product_accounts['expense']` (113-116) ; `labour_amounts[production_account] -= workcenter_cost` (124) ; ลง `'balance': -amt` (132) ⇒ บัญชี Expense **เครดิต** , บัญชี Production **เดบิต** ; `_post()` (137) ; ผูก `account_move_line_id` กลับ time entries (138-139).
`mrp_account/models/mrp_workcenter.py:12-13` `expense_account_id` help: "The expense is accounted for when the manufacturing order is marked as done. If not set, it is the expense account of the final product that will be used instead."
Analytic: `mrp_account/models/mrp_workorder.py:42-55` `_create_or_update_analytic_entry` : `value = -hours × costs_hour` ตาม `analytic_distribution` ของ Work Center.

---

## GAP-MFG-05 — WIP interim entry

### EV-SRC-MFG05-01 — สร้าง WIP + reversal พร้อมกัน
`mrp_account/wizard/mrp_wip_accounting.py:120-146` `confirm()` : ตรวจ Σcredit = Σdebit (122-123) ; ตรวจ `reversal_date > date` (124-125) ; สร้าง+`_post()` รายการ WIP (126-141) ; `move._reverse_moves(default_values_list=[{... 'date': self.reversal_date}])._post()` (142-146).
`mrp_account/wizard/mrp_wip_accounting.py:58-61,105-109` — `reversal_date` computed = `date + 1 วัน` ถ้ายังไม่ตั้งหรือ ≤ date ; แก้ไขได้ (`readonly=False`).

### EV-SRC-MFG05-02 — ไม่มีการผูกกับการปิด MO
ค้น `wip_move_ids|wip_production_ids` ใน `mrp_account`: ใช้เพื่อเก็บ/แสดงลิงก์เท่านั้น — `mrp_account/models/mrp_production.py:15,22-25,37-55` ; `mrp_account/models/account_move.py:11-42` ; `mrp_account/wizard/mrp_wip_accounting.py:128,144`. **ไม่มีโค้ดใน `_post_inventory` / `button_mark_done` ที่ย้อน/ยกเลิก WIP move**.

### EV-SRC-MFG05-03 — สูตรตัวเลขใน WIP
`mrp_account/wizard/mrp_wip_accounting.py:76-103` `_get_line_vals` :
- วัตถุดิบ = Σ `ml.quantity_product_uom × standard_price` (หรือ standard_price ของ lot เมื่อ lot-valuated) ของ move line ที่ `picked` ∧ `quantity` ∧ `date ≤ date` (81-84) → **ราคามาตรฐาน ไม่ใช่ `move.value`**
- Overhead = `productions.workorder_ids._cal_cost(date)` (85)
- เครดิตวัตถุดิบเข้า `property_stock_valuation_account_id` ของหมวดสินค้า **ค่า default (company-dependent fallback)** (86-92) ; เครดิต Overhead เข้า `account_production_wip_overhead_account_id` หรือ fallback `property_stock_account_production_cost_id` (69-74, 93-97) ; เดบิตรวมเข้า `account_production_wip_account_id` (98-102).
`:46-47` เลือกเฉพาะ MO state ∈ {progress, to_close, confirmed} ; `:64-66` `line_ids` computed+stored+แก้ไขได้ ; `:113-118` recompute เมื่อ `date` เปลี่ยน.
Test `mrp_account/tests/test_mrp_account.py:360-510` `test_wip_accounting_00` : ยืนยัน "2 journal entries: 1 WIP + 1 reversal" (บรรทัด 371, 388, 417), 3 บรรทัดต่อรายการ, Manual Entry สำหรับ MO ที่ไม่ใช่ WIP (367-373), ลิงก์ MO (`wip_production_count`).

---

## Evidence สำหรับหัวข้อ 5 ของ Summary (input สู่ GAP-MFG-01 — ยังไม่ปิด)

| ข้อความ | ที่ |
|---|---|
| journal entry ของ move ถูกสร้างและ post เมื่อ move done | `stock_account/models/stock_move.py:177-191` (`_action_done`), `:193-215` (`_create_account_move` → `account_move._post()`) |
| ทิศ Dr/Cr | `stock_account/models/stock_move.py:229-250` `_get_account_move_line_vals` : ถ้า `location_id.valuation_account_id` มี → Dr `stock_valuation` / Cr บัญชี location ; ไม่เช่นนั้น Dr บัญชี `location_dest_id` / Cr `stock_valuation` ; จำนวน = `_get_aml_value()` = `self.value` |
| Test ทิศ Dr/Cr ของ MO และ unbuild | `mrp_account/tests/test_mrp_account.py:120-167` `test_unbuild_account_00` (FG: Dr stock valuation / Cr production ; ส่วนประกอบ: Dr production / Cr stock valuation ; unbuild กลับทิศ) |
| ลำดับหามูลค่า move ขาเข้า | `stock_account/models/stock_move.py:363-448` `_get_value_data` : manual → `_get_value_from_account_move` (บิล/Invoice) → `_get_value_from_production` → `_get_value_from_quotation` → `_get_value_from_returns` → `_get_value_from_std_price` (+ `_get_value_from_extra` = landed cost) |
| สต็อกติดลบ ตกที่ราคามาตรฐาน | `stock_account/models/stock_move.py:500-517` `_get_value_from_std_price` |
| ยังไม่ได้ไล่ | เส้นทางที่ vendor bill ปรับมูลค่า move ที่ done แล้ว (`purchase_stock`/`account` — อยู่นอกไฟล์ที่อ่านรอบนี้) |

## ข้อควรระวังในการอ้างหลักฐาน
- เลขบรรทัดอ้างอิง tree ณ 2026-09-30
- EV-SRC-MFG02-03 เป็น inference จากลำดับโค้ด ไม่ใช่ test ที่รัน
- ข้อเสนอเปลี่ยนสถานะเป็นการตัดสินใจของ Boss
