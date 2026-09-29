> **SCHEMA-ONLY — ไม่มีข้อมูลจริง (no row data)** | ส่วนที่ 2 — Evidence | คู่กับ: `STATE03_DB_SCHEMA_SOURCE_CROSSCHECK_BUSINESS_SUMMARY.md`

# STATE03 DB Schema — Evidence (โครงสร้างเท่านั้น)

## 0. ขั้นตอนที่ทำ (ทำซ้ำได้)
1. `pg_restore --list` (PostgreSQL 18.6 client) : archive dbname `iTEST02`, created 2026-06-14 14:41:20 +07, pg_dump 18.4, format CUSTOM (dump v1.16) , TOC entries 28,648 , มีรายการ `TABLE DATA` 1,395 รายการ (**ไม่ถูก restore**)
2. `initdb` + `pg_ctl start` (PostgreSQL 18.6, `127.0.0.1:54329`, ไม่มี unix socket) ; `createdb state03_schema_scratch`
3. `pg_restore --schema-only --no-owner --no-privileges -d state03_schema_scratch <dump>` → 22 errors ทั้งหมดเกี่ยวกับ `ai_embedding` (ไม่มี extension `vector`)
4. ตรวจหลัง restore : ตารางฐาน 1,394 ; views 38 ; extensions ที่มี = `plpgsql`, `pg_stat_statements`, `pg_trgm` ; `sum(n_live_tup)` ของ `pg_stat_user_tables` = 0
5. คำสั่งที่รันทั้งหมดอ่านเฉพาะ `information_schema.tables|columns`, `pg_catalog.pg_constraint|pg_trigger|pg_views|pg_extension|pg_stat_user_tables` — **ไม่มี `SELECT` จากตารางธุรกิจ**
6. เสร็จงาน : `pg_ctl stop`, `dropdb state03_schema_scratch`, ลบโฟลเดอร์ cluster ชั่วคราว

## E1 — ตารางที่มี/ไม่มี (ตรวจเวอร์ชัน)
| ผล | รายการ |
|---|---|
| มี | `mrp_bom`, `mrp_bom_byproduct`, `mrp_production`, `mrp_workorder`, `mrp_workcenter`, `mrp_routing_workcenter`, `mrp_unbuild`, `stock_move`, `stock_location`, `stock_warehouse_orderpoint`, `stock_landed_cost`, `product_value`, `mrp_production_schedule`, `quality_check`, `quality_point`, `account_asset` |
| ไม่มี | `stock_valuation_layer`, `stock_orderpoint` (ชื่อตารางจริงของ Reordering Rule คือ `stock_warehouse_orderpoint`) |
| ไม่มี | `ir_property` (ค่า company-dependent เก็บเป็น jsonb ในคอลัมน์) |

## E2 — คอลัมน์ที่เกี่ยวกับผลวิจัยก่อนหน้า (มีอยู่ทั้งหมด)
| ตาราง | คอลัมน์ (ชนิด) | เชื่อมกับ |
|---|---|---|
| `mrp_bom_byproduct` | `cost_share` (numeric, ไม่กำหนด precision), `product_qty` (numeric), `operation_id`, `bom_id`, `product_uom_id` | `GAP-BRP-09` ; source `mrp/models/mrp_bom.py:871-874` |
| `stock_move` | `value` (numeric), `price_unit` (double precision), `cost_share` (numeric), `byproduct_id`, `production_id`, `raw_material_production_id`, `account_move_id`, `is_in`, `is_out`, `operation_id`, `bom_line_id` | `GAP-BRP-09`, valuation timing ; source `stock_account/models/stock_move.py:24-42` |
| `stock_move` | **ไม่มี** `remaining_qty`, `remaining_value`, `value_manual` (ฟิลด์ compute ไม่เก็บ) | สอดคล้อง source (compute) |
| `stock_location` | `valuation_account_id` | `GAP-MFG-02` ; `stock_account/models/stock_location.py:11-14` |
| `res_company` | `inventory_period`, `inventory_valuation`, `cost_method`, `account_stock_journal_id`, `account_stock_valuation_id`, `account_production_wip_account_id`, `account_production_wip_overhead_account_id`, `anglo_saxon_accounting`, `po_double_validation`, `po_double_validation_amount` | Stock Closing ; `stock_account/models/res_company.py:12-36` , `purchase/models/res_company.py:16-22` |
| `product_category` | `property_valuation` (**jsonb**), `property_cost_method` (**jsonb**), `property_stock_valuation_account_id`, `property_stock_account_production_cost_id` | E5 |
| `mrp_workorder` | `costs_hour`, `cost_mode`, `duration`, `duration_expected` (numeric), `duration_percent` (integer) | `GAP-MFG-04`, `GAP-BRP-05` ; `mrp/models/mrp_workorder.py:124-130,347-355` |
| `mrp_routing_workcenter` | `cost_mode`, `time_cycle_manual` | `mrp/models/mrp_routing.py:60-64` |
| `mrp_workcenter` | `costs_hour` (double precision), `expense_account_id`, `time_start`, `time_stop` — **ไม่มีคอลัมน์อัตราตามกะ/OT** | `GAP-BRP-04`/`GAP-MFG-04` |
| `mrp_production` | `extra_cost`, `bom_id`, `is_outdated_bom` | `mrp_account/models/mrp_production.py:13` |
| `stock_warehouse_orderpoint` | `trigger`, `snoozed_until`, `bom_id` (ไม่มี `qty_to_order` = compute) | `GAP-BRP-07` |
| `mrp_bom` | `type`, `enable_batch_size` | `GAP-BRP-01` |
| `account_move_line` | `cogs_origin_id` | valuation timing E3 |
| ตารางเกี่ยวกับ WIP | `mrp_account_wip_accounting*` (wizard), `wip_move_production_rel` | `GAP-MFG-05` |
> `account_move` มีคอลัมน์ `stock_move_id`/`wip_production_ids` ไม่ตรงที่คาดใน query แรก (สำรวจผิดชื่อ) — ในส่วนนี้ไม่ใช้เป็นหลักฐาน ; ความสัมพันธ์จริงคือ `stock_move.account_move_id` (มี) และตารางเชื่อม WIP ข้างต้น

## E3 — CHECK / UNIQUE constraints (ผลจาก `pg_constraint`)
| ตาราง | constraint |
|---|---|
| `account_move` | **ไม่มี CHECK** (query คืนศูนย์แถว) |
| `account_move_line` | `account_move_line_check_accountable_required_fields` : (display_type ∈ {line_section, line_subsection, line_note}) หรือ `account_id IS NOT NULL` |
| | `account_move_line_check_amount_currency_balance_sign` : ยกเว้นแถวส่วน/โน้ต ต้อง (balance ≤ 0 ∧ amount_currency ≤ 0) หรือ (balance ≥ 0 ∧ amount_currency ≥ 0) |
| | `account_move_line_check_credit_debit` : ยกเว้นแถวส่วน/โน้ต `credit * debit = 0` |
| | `account_move_line_check_non_accountable_fields_null` : แถวส่วน/โน้ต ต้อง amount_currency = debit = credit = 0 และ account_id NULL |
| `mrp_bom` | `mrp_bom_qty_positive` : `product_qty > 0` |
| `mrp_production` | `mrp_production_qty_positive` : `product_qty > 0` ; `mrp_production_name_uniq` UNIQUE(name, company_id) |
| `stock_warehouse_orderpoint` | `..._product_location_check` UNIQUE(product_id, location_id, company_id) |
| `mrp_bom_byproduct`, `stock_move` | **ไม่มี** CHECK/UNIQUE ที่เกี่ยวกับ `cost_share` |

## E4 — Trigger
`pg_trigger` (เฉพาะที่ไม่ใช่ internal) : **0 แถว** ⇒ ไม่มี trigger ระดับฐานข้อมูล (รวมถึงไม่มี trigger ตรวจ Σdebit = Σcredit)

## E5 — ค่า company-dependent เก็บเป็น jsonb
`product_category.property_valuation`, `property_cost_method` ชนิด `jsonb` ; ไม่มีตาราง `ir_property`

## E6 — การเทียบตารางกับโมเดลใน source Community
- วิธี : สคริปต์อ่าน source `odoo/` (ข้ามโฟลเดอร์ tests/i18n/static) เก็บ `_name` (จุด→ขีดล่าง), `_table`, และชื่อ relation ของ `Many2many` แล้วเทียบกับรายชื่อตารางจริง (ไม่ใช่การพิสูจน์ ; รูปแบบ relation ที่คำนวณอัตโนมัติอาจตกหล่น)
- ผล : ตาราง 1,394 → ตรงกับ Community ~698 ; ไม่ตรง ~696 (ตารางเชื่อม `*_rel` ~359 ; ตารางหลัก/ตัวช่วย 337)
- จำนวนตารางหลักที่ไม่ตรงตามคำนำหน้า : hr 49 , account 47 , import 19 , sign 18 , mrp 15 , documents 13 , quality 11 , helpdesk 11 , purchase 10 , appointment 10 , studio 8 , planning 8 , esg 8 , orm 7 , ai 6 , spreadsheet 5 , iot 5 , x (Studio) 4 , withholding 4 , sale 4 , product 4 , equity 4 ฯลฯ
- ชื่อตาราง mrp/stock/quality/purchase/sale ที่ไม่ตรง Community :
  - mrp : `mrp_eco`, `mrp_eco_approval`, `mrp_eco_approval_template`, `mrp_eco_bom_change`, `mrp_eco_routing_change`, `mrp_eco_stage`, `mrp_eco_tag`, `mrp_eco_type`, `mrp_mps_forecast_details`, `mrp_mps_forecast_suggestion`, `mrp_product_forecast`, `mrp_production_additional_workorder`, `mrp_production_schedule`, `mrp_workorder_additional_employee_assigned`, `mrp_workorder_employee_assigned`
  - stock : `stock_barcode_cancel_operation`
  - quality : `quality_alert`, `quality_alert_stage`, `quality_alert_team`, `quality_check`, `quality_check_spreadsheet`, `quality_check_wizard`, `quality_point`, `quality_point_test_type`, `quality_reason`, `quality_spreadsheet_template`, `quality_tag`
  - purchase : `purchase_advance_payment_bill`, `purchase_order_discount`, `purchase_order_level_reject`, `purchase_request`, `purchase_request_allocation`, `purchase_request_level_reject`, `purchase_request_line`, `purchase_request_line_make_purchase_order`, `purchase_request_line_make_purchase_order_item`, `purchase_request_rejected`
  - sale : `sale_additional_detail`, `sale_job_type`, `sale_order_reject_wizard`, `sale_order_spreadsheet`
  - account : `account_asset`, `account_asset_group`, `account_loan*`, `account_return*`, `account_report_budget*`, `account_followup_*`, `account_online_*`, `account_fiscal_year`, `account_withholding_tax`, `account_tax_unit`, `account_multicurrency_revaluation_wizard` ฯลฯ (รายการเต็มด้านล่าง)
  - ตารางที่ผู้ใช้สร้าง (Studio) : `x_master_operation`, `x_7_11_tag`, `x_res_partner_line_72662`, `x_project_task_worksheet_template_1` ; อื่นๆ : `jasper*`, `dropbox_auth_code`
- รายการเต็มของตารางหลัก/ตัวช่วยที่ไม่ตรง Community (ไม่รวมตารางเชื่อม `*_rel`) ด้านล่าง — **ชื่อตารางเท่านั้น**

## E7 — ตัวเลข 22 errors ตอน restore
ความสัมพันธ์ (FK) ของ `ai_embedding` 18 รายการ + type `vector` 1 + index vector 1 + `CREATE EXTENSION vector` 2 (extension is not available / does not exist) ; ผลต่อการวิจัย : ไม่มี (ตาราง AI)

## E8 — ข้อควรระวังในการอ้างหลักฐาน
- ผลทั้งหมดมาจากโครงสร้าง ณ วันที่ทำ dump (2026-06-14) ; source คือ `19.0.post20260921`
- การจับคู่ตาราง–โมเดลเป็นการประมาณด้วยรูปแบบข้อความ
- ไม่มีข้อมูลแถว จึงไม่สรุปเรื่องโมดูลที่ "เปิดใช้งาน" หรือค่าตั้งค่าใดๆ

## ภาคผนวก — ตารางหลัก/ตัวช่วยที่ไม่ตรง Community (337 ชื่อ; ชื่อตารางเท่านั้น)
```
account_account_exclude_res_currency_provision
account_account_fiscal_rate
account_asset
account_asset_group
account_audit_account_status
account_auto_reconcile_wizard
account_bank_selection
account_bank_statement_line_transient
account_change_lock_date
account_duplicate_transaction_wizard
account_fiscal_category
account_fiscal_year
account_followup_followup_line
account_followup_manual_reminder
account_followup_missing_information_wizard
account_import_summary
account_intrastat_code
account_loan
account_loan_close_wizard
account_loan_compute_wizard
account_loan_line
account_missing_transaction_wizard
account_move__account_payment
account_move_discount
account_multicurrency_revaluation_wizard
account_online_account
account_online_link
account_payment_deduction
account_reconcile_wizard
account_report_annotation
account_report_budget
account_report_budget_item
account_report_file_download_error_wizard
account_report_horizontal_group
account_report_horizontal_group_rule
account_report_send
account_reports_export_wizard
account_reports_export_wizard_format
account_return
account_return_check
account_return_check_template
account_return_creation_wizard
account_return_payment_wizard
account_return_submission_wizard
account_return_type
account_tax_unit
account_withholding_tax
add_iot_box
ai_agent
ai_agent_source
ai_composer
ai_documents_sort
ai_prompt_button
ai_topic
appointment_answer
appointment_answer_input
appointment_booking_line
appointment_invite
appointment_manage_leaves
appointment_question
appointment_resource
appointment_resource_linked_appointment_resource
appointment_slot
appointment_type
appraisal_ask_feedback
appraisal_select_survey
asset_modify
auto_gen_job_type_cancel_wizard
auto_gen_job_type_config
auto_gen_job_type_counter
auto_gen_job_type_history
bh_brand
bh_parent_company
bh_store_type
calendar_booking
calendar_booking_line
cheque_setting
city_zip_geonames_import
conf_prefix
create_withholding_tax_cert
crm_lead_convert2ticket
custom_dashboard
date_range
date_range_generator
date_range_type
db_backup_configure
dev_print_cheque_wizard
display_device_id_select_printer
documents_access
documents_access_tracking
documents_account_folder_setting
documents_document
documents_fleet_tags_table
documents_hr_contracts_tags_table
documents_link_to_record_wizard
documents_operation
documents_redirect
documents_request_wizard
documents_sharing
documents_sharing_access
documents_tag
dropbox_auth_code
employee_commuting_emissions_wizard
employees
equity_security_class
equity_transaction
equity_ubo
equity_valuation
esg_activity_type
esg_assignation_line
esg_database
esg_emission_factor
esg_emission_factor_line
esg_emission_source
esg_gas
esg_other_emission
expense_sample_receipt
export_bom_wizard
export_purchase_order_wizard
export_sale_order_wizard
factors_auto_assignment_wizard
fleet_disallowed_expenses_rate
frontdesk_drink
frontdesk_frontdesk
frontdesk_visitor
fsm_stock_tracking
fsm_stock_tracking_line
helpdesk_create_fsm_task
helpdesk_sla
helpdesk_sla_status
helpdesk_stage
helpdesk_stage_delete_wizard
helpdesk_tag
helpdesk_tag_assignment
helpdesk_team
helpdesk_ticket
helpdesk_ticket_convert_wizard
helpdesk_ticket_to_lead
hr_appraisal
hr_appraisal_campaign_wizard
hr_appraisal_goal
hr_appraisal_goal_skill
hr_appraisal_goal_tag
hr_appraisal_note
hr_appraisal_skill
hr_appraisal_template
hr_contract_sign_document_wizard
hr_payroll_dashboard_warning
hr_payroll_edit_payslip_line
hr_payroll_edit_payslip_lines_wizard
hr_payroll_edit_payslip_worked_days_line
hr_payroll_employee_declaration
hr_payroll_headcount
hr_payroll_headcount_line
hr_payroll_headcount_working_rate
hr_payroll_index
hr_payroll_note
hr_payroll_payment_report_wizard
hr_payroll_structure
hr_payslip
hr_payslip_correction_wizard
hr_payslip_input
hr_payslip_input_type
hr_payslip_line
hr_payslip_run
hr_payslip_worked_days
hr_recruitment_sign_document_wizard
hr_referral_alert
hr_referral_alert_mail_wizard
hr_referral_campaign_wizard
hr_referral_friend
hr_referral_level
hr_referral_link_to_share
hr_referral_onboarding
hr_referral_points
hr_referral_reward
hr_referral_send_mail
hr_referral_send_sms
hr_rule_parameter
hr_rule_parameter_value
hr_salary_attachment
hr_salary_rule
hr_salary_rule_category
hr_salary_rule_section
hr_timesheet_merge_wizard
hr_timesheet_stop_timer_confirmation_wizard
hr_timesheet_tip
import_bank_statement
import_bom
import_chart_account
import_client
import_equipments
import_inventory
import_inventory_adjustment
import_invoice
import_invoice_line
import_journal_entry
import_journal_journal
import_product
import_product_pricelist
import_purchase_order
import_purchase_order_line
import_sale_order
import_sale_order_line
import_sale_pricelist
import_vendor_pricelist
iot_box
iot_device
iot_discovered_box
iot_keyboard_layout
iot_trigger
ir_ui_view_4770_backup
ir_ui_view_backup_20260508
ir_ui_view_quality_backup
jasper_report
jasper_report_run
managers
masterfile_color
masterfile_partcode
masterfile_parttype
mrp_eco
mrp_eco_approval
mrp_eco_approval_template
mrp_eco_bom_change
mrp_eco_routing_change
mrp_eco_stage
mrp_eco_tag
mrp_eco_type
mrp_mps_forecast_details
mrp_mps_forecast_suggestion
mrp_product_forecast
mrp_production_additional_workorder
mrp_production_schedule
mrp_workorder_additional_employee_assigned
mrp_workorder_employee_assigned
orm_signaling_assets
orm_signaling_default
orm_signaling_groups
orm_signaling_registry
orm_signaling_routing
orm_signaling_stable
orm_signaling_templates
payslip_tags_table
planning_calendar_resource
planning_planning
planning_preview
planning_recurrency
planning_role
planning_send
planning_slot
planning_slot_template
product_customer_info
product_fetch_image_wizard
product_tags_table
product_template_file_line
project_task_convert_wizard
project_task_stop_timers_wizard
project_task_stop_timers_wizard_line
propose_change
purchase_advance_payment_bill
purchase_order_discount
purchase_order_level_reject
purchase_request
purchase_request_allocation
purchase_request_level_reject
purchase_request_line
purchase_request_line_make_purchase_order
purchase_request_line_make_purchase_order_item
purchase_request_rejected
qr_code_payment_wizard
quality_alert
quality_alert_stage
quality_alert_team
quality_check
quality_check_spreadsheet
quality_check_wizard
quality_point
quality_point_test_type
quality_reason
quality_spreadsheet_template
quality_tag
rel_followup_manual_reminder_res_partner
rel_studio_export_wizard_data
request_appraisal
res_city_zip
res_partner_company_type
res_partner_title
sale_additional_detail
sale_job_type
sale_order_reject_wizard
sale_order_spreadsheet
save_spreadsheet_template
select_printers_wizard
sign_completed_document
sign_document
sign_import_documents
sign_item
sign_item_option
sign_item_radio_set
sign_item_role
sign_item_type
sign_log
sign_request
sign_request_item
sign_request_item_value
sign_request_share
sign_send_request
sign_send_request_signer
sign_template
sign_template_preview
sign_template_tag
spreadsheet_cell_thread
spreadsheet_contributor
spreadsheet_document_to_dashboard
spreadsheet_revision
spreadsheet_template
stock_barcode_cancel_operation
studio_approval_entry
studio_approval_request
studio_approval_rule
studio_approval_rule_approver
studio_approval_rule_delegate
studio_export_model
studio_export_wizard
studio_export_wizard_data
timer_timer
withholding_tax_cert
withholding_tax_cert_line
withholding_tax_report
withholding_tax_report_wizard
wizard_purchase_request_line_change_data
worksheet_template
worksheet_template_load_wizard
x_7_11_tag
x_master_operation
x_project_task_worksheet_template_1
x_res_partner_line_72662
```
