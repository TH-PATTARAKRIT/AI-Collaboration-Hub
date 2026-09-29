> **STATUS CORRECTION — The source/schema finding is CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION. It is not runtime proof, Gate PASS, final gap closure, or STATE03 completion. Refer to STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF for the current qualified disposition.**

> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) / PERIOD_CUTOFF_VALIDATION_PILOT | Source-code research result | **ส่วนที่ 2 — Evidence (file + line)**
> คู่กับ: `SRC_GAP-MFG-01_VALUATION_TIMING_SOURCE_CHECK_BUSINESS_SUMMARY.md`

# Valuation Timing — Evidence Register

## 0. ขอบเขต
| Field | Value |
|---|---|
| Source root (read-only) | `Odoo Community/odoo-19.0.post20260921/` ; path สัมพัทธ์กับ `odoo/addons/` |
| วิธี | Static read ; ไม่ได้รัน Odoo |
| Modules | `stock_account`, `purchase_stock`, `account` (accrued orders), `mrp_account`, `stock` |
| ไม่ได้แตะ | `addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus`, `VAT_BACKFILL_20260914`, `AUDIT_LOG_20260914`, `Claude outputs`, `MODIFY`, `.xlsx`/`.dump` |

---

## E1 — ค่าเริ่มต้น Periodic + Standard
| ที่ | หลักฐาน |
|---|---|
| `stock_account/data/stock_account_data.xml:4-5` | `ir.default` `product.category.property_cost_method = 'standard'` ; `property_valuation = 'periodic'` |
| `stock_account/models/res_company.py:29-36,38-47` | `inventory_valuation` default `'periodic'` (label 'Periodic (at closing)' / 'Perpetual (at invoicing)') ; `cost_method` default `'standard'` |
| `stock_account/models/product.py:731-740` | help ของ `property_valuation` : "Periodic: entries suggested manually in the inventory valuation report. Perpetual: An accounting entry is automatically created to value the inventory when a product is billed or invoiced." |
| `stock_account/models/product.py:73-79` | `valuation` ของสินค้า = ค่าของหมวด หรือของบริษัท |

## E2 — ชั้น B เหตุการณ์ที่ 1 : Vendor Bill → บัญชี Stock Valuation
- `stock_account/models/account_move_line.py:13-24` `_compute_account_id` : ถ้าเป็นเอกสารซื้อ ∧ `_eligible_for_stock_account()` (storable, ไม่ใช่ dropship — `:30-35`) ∧ `product.valuation == 'real_time'` ∧ มี `stock_valuation` ⇒ `line.account_id = accounts['stock_valuation']`
- `stock_account/models/account_move.py:29-44` `_post` : หลังโพสต์ เรียก `self.line_ids._get_stock_moves().filtered(is_in or is_dropship)._set_value()` (บรรทัด **42**) ⇒ ปรับมูลค่า stock move ขาเข้าตามบิล
- มูลค่า move จากบิล : `purchase_stock/models/stock_move.py:157-215` `_get_value_from_account_move` (เฉพาะบิลสถานะ `posted` — 172-173 ; `in_invoice` บวก / `in_refund` ลบ — 175-180 ; หักจำนวนที่ move ก่อนหน้าใช้ไปแล้ว — 185-203) ; ถ้ายังไม่มีบิล : `:229-243` `_get_value_from_quotation` ใช้ราคาใน PO ("(not billed)")
- ผลต่างราคา (เฉพาะ Standard) : `purchase_stock/models/account_invoice.py:12-108` `_stock_account_prepare_anglo_saxon_in_lines_vals` (เงื่อนไข `company.anglo_saxon_accounting` , `cost_method == 'standard'` : 37, 44 ; บัญชี = `property_price_difference_account_id` 51) ; เรียกใน `_post` ที่ `:113-117`
- ส่วนต่างราคาสำหรับ standard : `purchase_stock/models/account_move_line.py:12-30`

## E3 — ชั้น B เหตุการณ์ที่ 2 : Customer Invoice → COGS
- `stock_account/models/account_move.py:68-161` `_stock_account_prepare_realtime_out_lines_vals` : เฉพาะเอกสารขาย (`is_sale_document`, 104) ; เฉพาะบรรทัด `_eligible_for_stock_account` ∧ `valuation == 'real_time'` (111) ; สร้างบรรทัด `display_type='cogs'` คู่ : บัญชี stock (สลับเครดิต) + บัญชีค่าใช้จ่าย/COGS (129-160) ; เรียกจาก `_post` ที่ `:37`
- มูลค่า COGS : `stock_account/models/account_move_line.py:51-75` `_get_cogs_value` (ใช้ `moves._get_cogs_price_unit` จาก move done — 67-68 ; ไม่มี move → standard_price/FIFO — 70-73) ; `stock_account/models/stock_move.py:266-280` `_get_cogs_price_unit`

## E4 — ชั้น B เหตุการณ์ที่ 3 : ตอน stock move เสร็จ (ต้องมี location valuation account)
- `stock_account/models/stock_move.py:659-666` `_should_create_account_move` ; `:177-191` `_action_done` → `moves._create_account_move()` (187) ; `:193-215` `_create_account_move` ; `:229-250` `_get_account_move_line_vals`
- ฟิลด์ location : `stock_account/models/stock_location.py:11-14`
- **UI แสดงฟิลด์นี้เฉพาะ usage `production` ("Cost of Production") และ `inventory` ("Loss Account")** : `stock_account/views/stock_location_views.xml:10-15` (`invisible="usage not in ('inventory', 'production')"`)
- **ไม่มี default** : ไม่พบไฟล์ data/chart template (`l10n_th/models/template_th.py:8-45` และ `stock_account/models/account_chart_template.py:11-54`) ที่ตั้ง `valuation_account_id` ให้ location ; `stock_account/__init__.py:10-86` post-init ตั้งเฉพาะ journal สต็อก + บัญชี stock valuation ของบริษัท/หมวด ; ค้น `valuation_account_id` ทั้ง tree — นอกจากไฟล์ทดสอบ พบเฉพาะโค้ด `stock_account`, `mrp_account`, และแม่แบบ `l10n_*` (ที่ตั้ง `property_stock_valuation_account_id` ซึ่งเป็นคนละฟิลด์)
- ทดสอบตั้งบัญชีที่ inventory locations เอง : `stock_account/tests/common.py:113` (`inventory_locations.valuation_account_id = self.account_inventory.id`)
- ⇒ การรับ/ส่งกับ Supplier/Customer ไม่ผ่านเงื่อนไข (ไม่มีบัญชีที่ location) *ในการตั้งค่า UI ปกติ* — inference จากโค้ด ไม่ได้รัน

## E5 — ชั้น C : Stock Closing
| ที่ | หลักฐาน |
|---|---|
| `stock_account/models/res_company.py:19-27` | `inventory_period` : `manual` (default) / `daily` / `monthly` |
| `stock_account/data/stock_account_data.xml:7-18` | cron "Stock Account: Inventory Valuation Closing" → `model._cron_post_stock_valuation()` , active , รันทุก 1 วัน , user root |
| `stock_account/models/res_company.py:137-150` | `_cron_post_stock_valuation` : periods = `['daily']` + `'monthly'` เมื่อวันนี้คือวันสุดท้ายของเดือน (`today == today + relativedelta(day=31)`, 140) ; เรียก `action_close_stock_valuation(auto_post=True)` , จับ `UserError` แล้วข้าม (149-150) |
| `stock_account/models/res_company.py:49-87` | `action_close_stock_valuation` : ห้ามปิดก่อน closing ล่าสุด (54-55) ; ไม่มีรายการ → error "Everything is correctly closed" หรือ (จาก cron) return เงียบ (58-63) ; ต้องมี Journal + Stock Valuation Account (64-67) ; ref "Stock Closing" ; `auto_post` จึงโพสต์ (78-79) มิฉะนั้นคง draft |
| `stock_account/models/res_company.py:119-135` | `_action_close_stock_valuation` = (1) reclassification ของ location (2) global variation ต่อบัญชี stock (3) continental realtime variation over period |
| `stock_account/models/res_company.py:238-272` | `_get_stock_valuation_account_vals` : `balance = inventory_data[account] − accounting_data[account] − extra` (258-259) ; `account_variation = account.account_stock_variation_id or company.expense_account_id` (253-255) ; ถ้าไม่มี `continue` (256-257) ; ref "Closing: Stock Variation Global…" |
| `stock_account/models/res_company.py:89-117` | `stock_value` (Σ `total_value` ของสินค้า) และ `stock_accounting_value` (ยอด `balance` ของ AML ที่ posted ในบัญชี valuation) |
| `stock_account/models/res_company.py:274-320` | `_get_continental_realtime_variation_vals` (Stock Variation Over Period) |
| `stock_account/models/res_company.py:342-359` | `_get_last_closing_date` (เก็บ id ล่าสุด 10 รายการใน `ir.config_parameter` — 361-368) |
| `stock_account/models/account_account.py:7-13` | `account_stock_variation_id` ("At closing, register the inventory variation of the period"), `account_stock_expense_id` ("Counterpart used at closing…") |
| Tests | `stock_account/tests/test_stockvaluation.py:3477-3623` (`test_cron_post_stock_valuation_domain` และการรัน cron) |
> Stock Closing ไม่ใช่รายการ reverse : สร้างรายการเดียวเป็น true-up ของผลต่างสะสม (ไม่มีการเรียก `_reverse_moves` ใน `res_company.py`)

## E6 — Accrual แบบ Reversal Date (กลไกแยก)
- `account/wizard/accrued_orders.py` : wizard `account.accrued.orders.wizard` ; `reversal_date` default = `date + 1 วัน` (67-72) ; `create_entries` ตรวจ `reversal_date > date` (381) และ `move._reverse_moves(... 'date': self.reversal_date)` (386-389) ; ตรรกะ "รับแล้วยังไม่วางบิล" `qty_received_at_date − qty_invoiced_at_date` (185-222) ; "ส่งแล้วยังไม่ออกใบแจ้งหนี้" `qty_delivered_at_date − qty_invoiced_at_date` (248) ; บัญชี expense/stock variation ของสินค้า (195-196, 243, 403)
- WIP wizard (กลไกแยกอีกตัว) : `mrp_account/wizard/mrp_wip_accounting.py:120-146`

## E7 — ชั้น A : subledger = stock.move.value + total_value คำนวณสด
- `stock_account/models/stock_move.py:24-26` `value` (Monetary เก็บค่า) ; `:292-357` `_set_value` ; `:363-448` `_get_value_data` (ลำดับ : manual → บิล/Invoice → production → quotation → returns → std price → extra/landed)
- `stock_account/models/product.py:179-278` `_compute_value` : `@api.depends('cost_method','stock_move_ids.value','standard_price')` ; จำนวนคงเหลือศูนย์ → มูลค่า 0 ; Standard/Average/FIFO ใช้ `_run_standard_batch`/`_run_average_batch`/`_run_fifo_batch`
- `stock_account/models/product.py:_run_fifo` (`def _run_fifo` เริ่ม 540) : ปริมาณ ≤ 0 → `quantity × standard_price` (หรือราคา last-in ณ วัน) ; ต้องการมากกว่าที่มี → ขยายด้วยราคาล่าสุดของ move สุดท้าย หรือ `standard_price`

## E8 — GAP-MFG-01 : ติดลบระหว่างผลิต
- ขาออก (วัตถุดิบ MO) : `stock_account/models/stock_move.py:339-351` ถ้า FIFO `_run_fifo(valued_qty)` ; อื่นๆ `standard_price × qty`
- ค้น "negative inventory"/"Revaluation of" ใน `stock_account`, `mrp_account`, `stock` : **ไม่พบ** โค้ดสร้างรายการบัญชีชื่อดังกล่าว (ผลค้นเชิงลบ — ระดับมั่นใจต่ำกว่าหลักฐานเชิงบวก)
- ปรับมูลค่าภายหลัง : E2 (`_set_value` หลังบิล) + E5 (Stock Closing)

## E9 — Consumable vs Storable (Step 6)
- เงื่อนไขบัญชีสต็อกเฉพาะ `product_id.is_storable` : `stock_account/models/account_move_line.py:30-35` ; `stock_account/models/stock_move.py:664`

## ข้อควรระวังในการอ้างหลักฐาน
- เลขบรรทัดอ้างอิง tree ณ 2026-09-30 (ตรวจด้วย grep/อ่านตรง)
- E4 (⇒ ข้อสรุปเรื่อง supplier/customer location) เป็น inference จากโค้ด+UI ไม่ใช่ test ที่รัน ; การตั้งค่าฐานข้อมูลจริง/การนำเข้าอาจตั้ง location account เองได้
- เอกสารนี้ไม่เปลี่ยนสถานะ `Material Finding — Independently Unverified` ; เป็นหลักฐานเพิ่มระดับ source สำหรับ CHATGPT_AUDIT/Boss
