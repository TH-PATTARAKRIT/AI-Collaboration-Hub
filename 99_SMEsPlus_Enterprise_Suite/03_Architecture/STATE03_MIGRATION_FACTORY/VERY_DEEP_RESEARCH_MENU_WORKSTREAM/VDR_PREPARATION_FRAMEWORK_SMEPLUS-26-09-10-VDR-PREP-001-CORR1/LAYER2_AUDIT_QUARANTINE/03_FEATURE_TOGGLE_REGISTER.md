# 03_FEATURE_TOGGLE_REGISTER.md
# Register 03 — Feature Toggle Register (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. Population

| Clause | Declaration |
|--------|-------------|
| **POPULATION** | Every field declared on the configuration-settings object by any module in the Inventory module set |
| **PATTERN** | AST parse; class whose declaration set includes the configuration-settings object; every assignment whose value is a framework field constructor |
| **PATH SET** | R1, 149 modules, 2,167 code files |
| **UNIT** | One declared settings field = one row (a field declared by two modules appears twice, deliberately — the two declarations may differ) |
| **ELIGIBILITY** | 149/149 modules processed, 0 parse failures |
| **Instrument controls** | I1 re-run agrees at 237; I2 synthetic injection raised the count by exactly 1; I3 149/149; I4 the initial zero was an instrument defect (`CORR-F-08`) and was repaired before publication |

**Total: 237 toggle declarations.**

## 2. Toggle classes

| Class | Mechanism | Count | Share | Where the state actually lives |
|-------|-----------|------:|------:|--------------------------------|
| **A** MODULE-INSTALLER | switching it on installs a separate unit of code | 41 | 17.3% | the installed-module table |
| **B** GROUP-TOGGLE | activates a security group | 21 | 8.9% | the user↔group assignment |
| **C** SYSTEM-PARAMETER | writes a system parameter read at runtime | 7 | 3.0% | the system-parameter table |
| **D** PASS-THROUGH | stores onto another business object | 138 | 58.2% | company / warehouse / product / category |
| **E** PLAIN or COMPUTED | held on the settings object, or derived | 30 | 12.7% | the settings object, or nowhere |
| | **TOTAL** | **237** | 100% | |

## 3. Register

| Toggle field | Class | Declared by | Activates / stores to | Evidence |
|---|---|---|---|---|
| `module_delivery` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:33 |
| `module_delivery_bpost` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:38 |
| `module_delivery_dhl` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:34 |
| `module_delivery_easypost` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:39 |
| `module_delivery_envia` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:43 |
| `module_delivery_fedex_rest` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:35 |
| `module_delivery_sendcloud` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:40 |
| `module_delivery_shiprocket` | A MODULE-INSTALLER | delivery_shiprocket | — | delivery_shiprocket/models/res_config_settings.py:9 |
| `module_delivery_shiprocket` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:41 |
| `module_delivery_starshipit` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:42 |
| `module_delivery_ups_rest` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:36 |
| `module_delivery_usps_rest` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:37 |
| `module_mrp_mps` | A MODULE-INSTALLER | mrp | — | mrp/models/res_config_settings.py:12 |
| `module_mrp_plm` | A MODULE-INSTALLER | mrp | — | mrp/models/res_config_settings.py:13 |
| `module_mrp_subcontracting` | A MODULE-INSTALLER | mrp | — | mrp/models/res_config_settings.py:16 |
| `module_pos_adyen` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:33 |
| `module_pos_iot_ingenico` | A MODULE-INSTALLER | pos_iot | — | pos_iot/models/res_config_settings.py:10 |
| `module_pos_iot_six` | A MODULE-INSTALLER | pos_iot | — | pos_iot/models/res_config_settings.py:12 |
| `module_pos_iot_worldline` | A MODULE-INSTALLER | pos_iot | — | pos_iot/models/res_config_settings.py:11 |
| `module_pos_mercado_pago` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:37 |
| `module_pos_pine_labs` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:38 |
| `module_pos_pricer` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:40 |
| `module_pos_qfpay` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:39 |
| `module_pos_razorpay` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:36 |
| `module_pos_stripe` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:34 |
| `module_pos_tyro` | A MODULE-INSTALLER | pos_enterprise | — | pos_enterprise/models/res_config_settings.py:8 |
| `module_pos_viva_com` | A MODULE-INSTALLER | point_of_sale | — | point_of_sale/models/res_config_settings.py:35 |
| `module_product_expiry` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:11 |
| `module_quality_control` | A MODULE-INSTALLER | mrp | — | mrp/models/res_config_settings.py:14 |
| `module_quality_control` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:44 |
| `module_quality_control_worksheet` | A MODULE-INSTALLER | mrp | — | mrp/models/res_config_settings.py:15 |
| `module_quality_control_worksheet` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:45 |
| `module_stock_barcode` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:29 |
| `module_stock_barcode_barcodelookup` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:30 |
| `module_stock_dropshipping` | A MODULE-INSTALLER | purchase_stock | — | purchase_stock/models/res_config_settings.py:10 |
| `module_stock_dropshipping` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:51 |
| `module_stock_fleet` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:55 |
| `module_stock_landed_costs` | A MODULE-INSTALLER | stock_account | — | stock_account/models/res_config_settings.py:7 |
| `module_stock_picking_batch` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:28 |
| `module_stock_sms` | A MODULE-INSTALLER | stock | — | stock/models/res_config_settings.py:32 |
| `module_whatsapp_stock` | A MODULE-INSTALLER | stock_enterprise | — | stock_enterprise/models/res_config_settings.py:7 |
| `group_expiry_date_on_delivery_slip` | B GROUP-TOGGLE | product_expiry | 'product_expiry.group_expiry_date_on_delivery_slip' | product_expiry/models/res_config_settings.py:10 |
| `group_lot_on_delivery_slip` | B GROUP-TOGGLE | stock | 'stock.group_lot_on_delivery_slip' | stock/models/res_config_settings.py:17 |
| `group_lot_on_invoice` | B GROUP-TOGGLE | stock_account | 'stock_account.group_lot_on_invoice' | stock_account/models/res_config_settings.py:9 |
| `group_mrp_byproducts` | B GROUP-TOGGLE | mrp | 'mrp.group_mrp_byproducts' | mrp/models/res_config_settings.py:10 |
| `group_mrp_reception_report` | B GROUP-TOGGLE | mrp | 'mrp.group_mrp_reception_report' | mrp/models/res_config_settings.py:20 |
| `group_mrp_routings` | B GROUP-TOGGLE | mrp | 'mrp.group_mrp_routings' | mrp/models/res_config_settings.py:17 |
| `group_mrp_wo_shop_floor` | B GROUP-TOGGLE | mrp_workorder | 'mrp_workorder.group_mrp_wo_shop_floor' | mrp_workorder/models/res_config_settings.py:11 |
| `group_mrp_wo_tablet_timer` | B GROUP-TOGGLE | mrp_workorder | 'mrp_workorder.group_mrp_wo_tablet_timer' | mrp_workorder/models/res_config_settings.py:10 |
| `group_mrp_workorder_dependencies` | B GROUP-TOGGLE | mrp | 'mrp.group_mrp_workorder_dependencies' | mrp/models/res_config_settings.py:21 |
| `group_pos_preset` | B GROUP-TOGGLE | point_of_sale | 'point_of_sale.group_pos_preset' | point_of_sale/models/res_config_settings.py:120 |
| `group_rental_stock_picking` | B GROUP-TOGGLE | sale_stock_renting | 'sale_stock_renting.group_rental_stock_picking' | sale_stock_renting/models/res_config_settings.py:18 |
| `group_stock_adv_location` | B GROUP-TOGGLE | stock | 'stock.group_adv_location' | stock/models/res_config_settings.py:23 |
| `group_stock_lot_print_gs1` | B GROUP-TOGGLE | stock | 'stock.group_stock_lot_print_gs1' | stock/models/res_config_settings.py:15 |
| `group_stock_multi_locations` | B GROUP-TOGGLE | stock | 'stock.group_stock_multi_locations' | stock/models/res_config_settings.py:46 |
| `group_stock_production_lot` | B GROUP-TOGGLE | stock | 'stock.group_production_lot' | stock/models/res_config_settings.py:13 |
| `group_stock_reception_report` | B GROUP-TOGGLE | stock | 'stock.group_reception_report' | stock/models/res_config_settings.py:50 |
| `group_stock_sign_delivery` | B GROUP-TOGGLE | stock | 'stock.group_stock_sign_delivery' | stock/models/res_config_settings.py:27 |
| `group_stock_tracking_lot` | B GROUP-TOGGLE | stock | 'stock.group_tracking_lot' | stock/models/res_config_settings.py:19 |
| `group_stock_tracking_owner` | B GROUP-TOGGLE | stock | 'stock.group_tracking_owner' | stock/models/res_config_settings.py:21 |
| `group_unlocked_by_default` | B GROUP-TOGGLE | mrp | 'mrp.group_unlocked_by_default' | mrp/models/res_config_settings.py:19 |
| `group_warning_stock` | B GROUP-TOGGLE | stock | 'stock.group_warning_stock' | stock/models/res_config_settings.py:26 |
| `barcode_max_time_between_keys_in_ms` | C SYSTEM-PARAMETER | stock_barcode | 'barcode.max_time_between_keys_in_ms' | stock_barcode/models/res_config_settings.py:14 |
| `barcode_rfid_batch_time` | C SYSTEM-PARAMETER | stock_barcode | 'stock_barcode.barcode_rfid_batch_time' | stock_barcode/models/res_config_settings.py:20 |
| `barcode_separator` | C SYSTEM-PARAMETER | stock | 'stock.barcode_separator' | stock/models/res_config_settings.py:52 |
| `barcode_separator_regex` | C SYSTEM-PARAMETER | stock_barcode | 'stock_barcode.barcode_separator_regex' | stock_barcode/models/res_config_settings.py:23 |
| `stock_barcode_mute_sound_notifications` | C SYSTEM-PARAMETER | stock_barcode | 'stock_barcode.mute_sound_notifications' | stock_barcode/models/res_config_settings.py:10 |
| `use_security_lead` | C SYSTEM-PARAMETER | sale_stock | 'sale_stock.use_security_lead' | sale_stock/models/res_config_settings.py:11 |
| `wo_shop_floor_maximum_card_count` | C SYSTEM-PARAMETER | mrp_workorder | 'mrp_workorder.wo_shop_floor_maximum_card_count' | mrp_workorder/models/res_config_settings.py:12 |
| `account_default_pos_receivable_account_id` | D PASS-THROUGH | point_of_sale | 'company_id.account_default_pos_receivable_account_id' | point_of_sale/models/res_config_settings.py:42 |
| `annual_inventory_day` | D PASS-THROUGH | stock | 'company_id.annual_inventory_day' | stock/models/res_config_settings.py:49 |
| `annual_inventory_month` | D PASS-THROUGH | stock | 'company_id.annual_inventory_month' | stock/models/res_config_settings.py:48 |
| `barcode_nomenclature_id` | D PASS-THROUGH | point_of_sale | 'company_id.nomenclature_id' | point_of_sale/models/res_config_settings.py:43 |
| `barcode_nomenclature_id` | D PASS-THROUGH | stock_barcode | 'company_id.nomenclature_id' | stock_barcode/models/res_config_settings.py:7 |
| `days_to_purchase` | D PASS-THROUGH | purchase_stock | 'company_id.days_to_purchase' | purchase_stock/models/res_config_settings.py:11 |
| `horizon_days` | D PASS-THROUGH | stock | 'company_id.horizon_days' | stock/models/res_config_settings.py:59 |
| `iface_fiscal_data_module` | D PASS-THROUGH | pos_blackbox_be | 'pos_config_id.iface_fiscal_data_module' | pos_blackbox_be/models/res_config_settings.py:9 |
| `intercompany_receipt_type_id` | D PASS-THROUGH | sale_purchase_stock_inter_company_rules | 'company_id.intercompany_receipt_type_id' | sale_purchase_stock_inter_company_rules/models/res_config_settings.py:14 |
| `intercompany_sync_delivery_receipt` | D PASS-THROUGH | sale_purchase_stock_inter_company_rules | 'company_id.intercompany_sync_delivery_receipt' | sale_purchase_stock_inter_company_rules/models/res_config_settings.py:19 |
| `intercompany_warehouse_id` | D PASS-THROUGH | sale_purchase_stock_inter_company_rules | 'company_id.intercompany_warehouse_id' | sale_purchase_stock_inter_company_rules/models/res_config_settings.py:8 |
| `l10n_br_edi_csc_identifier` | D PASS-THROUGH | l10n_br_edi_pos | 'company_id.l10n_br_edi_csc_identifier' | l10n_br_edi_pos/models/res_config_settings.py:12 |
| `l10n_br_edi_csc_number` | D PASS-THROUGH | l10n_br_edi_pos | 'company_id.l10n_br_edi_csc_number' | l10n_br_edi_pos/models/res_config_settings.py:13 |
| `l10n_br_edi_qr_url_override` | D PASS-THROUGH | l10n_br_edi_pos | 'company_id.l10n_br_edi_qr_url_override' | l10n_br_edi_pos/models/res_config_settings.py:15 |
| `l10n_br_edi_url_key_override` | D PASS-THROUGH | l10n_br_edi_pos | 'company_id.l10n_br_edi_url_key_override' | l10n_br_edi_pos/models/res_config_settings.py:14 |
| `l10n_br_nfce_next_number` | D PASS-THROUGH | l10n_br_edi_pos | 'pos_config_id.order_seq_id.number_next_actual' | l10n_br_edi_pos/models/res_config_settings.py:11 |
| `l10n_pe_edi_stock_client_id` | D PASS-THROUGH | l10n_pe_edi_stock | 'company_id.l10n_pe_edi_stock_client_id' | l10n_pe_edi_stock/models/res_config_settings.py:7 |
| `l10n_pe_edi_stock_client_password` | D PASS-THROUGH | l10n_pe_edi_stock | 'company_id.l10n_pe_edi_stock_client_password' | l10n_pe_edi_stock/models/res_config_settings.py:19 |
| `l10n_pe_edi_stock_client_secret` | D PASS-THROUGH | l10n_pe_edi_stock | 'company_id.l10n_pe_edi_stock_client_secret' | l10n_pe_edi_stock/models/res_config_settings.py:11 |
| `l10n_pe_edi_stock_client_username` | D PASS-THROUGH | l10n_pe_edi_stock | 'company_id.l10n_pe_edi_stock_client_username' | l10n_pe_edi_stock/models/res_config_settings.py:15 |
| `l10n_vn_edi_pos_default_symbol` | D PASS-THROUGH | l10n_vn_edi_viettel_pos | 'company_id.l10n_vn_pos_default_symbol' | l10n_vn_edi_viettel_pos/models/res_config_settings.py:9 |
| `lc_journal_id` | D PASS-THROUGH | stock_landed_costs | 'company_id.lc_journal_id' | stock_landed_costs/models/res_config_settings.py:10 |
| `manufacturing_period` | D PASS-THROUGH | mrp_mps | 'company_id.manufacturing_period' | mrp_mps/models/res_config_settings.py:10 |
| `manufacturing_period_to_display_day` | D PASS-THROUGH | mrp_mps | 'company_id.manufacturing_period_to_display_day' | mrp_mps/models/res_config_settings.py:20 |
| `manufacturing_period_to_display_month` | D PASS-THROUGH | mrp_mps | 'company_id.manufacturing_period_to_display_month' | mrp_mps/models/res_config_settings.py:14 |
| `manufacturing_period_to_display_week` | D PASS-THROUGH | mrp_mps | 'company_id.manufacturing_period_to_display_week' | mrp_mps/models/res_config_settings.py:17 |
| `manufacturing_period_to_display_year` | D PASS-THROUGH | mrp_mps | 'company_id.manufacturing_period_to_display_year' | mrp_mps/models/res_config_settings.py:11 |
| `point_of_sale_ticket_portal_url_display_mode` | D PASS-THROUGH | point_of_sale | 'company_id.point_of_sale_ticket_portal_url_display_mode' | point_of_sale/models/res_config_settings.py:113 |
| `point_of_sale_ticket_unique_code` | D PASS-THROUGH | point_of_sale | 'company_id.point_of_sale_ticket_unique_code' | point_of_sale/models/res_config_settings.py:110 |
| `point_of_sale_use_ticket_qr_code` | D PASS-THROUGH | point_of_sale | 'company_id.point_of_sale_use_ticket_qr_code' | point_of_sale/models/res_config_settings.py:107 |
| `pos_advanced_employee_ids` | D PASS-THROUGH | pos_hr | 'pos_config_id.advanced_employee_ids' | pos_hr/models/res_config_settings.py:12 |
| `pos_amount_authorized_diff` | D PASS-THROUGH | point_of_sale | 'pos_config_id.amount_authorized_diff' | point_of_sale/models/res_config_settings.py:61 |
| `pos_appointment_type_id` | D PASS-THROUGH | pos_appointment | 'pos_config_id.appointment_type_id' | pos_appointment/models/res_config_settings.py:7 |
| `pos_auto_validate_terminal_payment` | D PASS-THROUGH | point_of_sale | 'pos_config_id.auto_validate_terminal_payment' | point_of_sale/models/res_config_settings.py:108 |
| `pos_available_preset_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.available_preset_ids' | point_of_sale/models/res_config_settings.py:51 |
| `pos_basic_employee_ids` | D PASS-THROUGH | pos_hr | 'pos_config_id.basic_employee_ids' | pos_hr/models/res_config_settings.py:10 |
| `pos_basic_receipt` | D PASS-THROUGH | point_of_sale | 'pos_config_id.basic_receipt' | point_of_sale/models/res_config_settings.py:118 |
| `pos_cash_control` | D PASS-THROUGH | point_of_sale | 'pos_config_id.cash_control' | point_of_sale/models/res_config_settings.py:63 |
| `pos_cash_rounding` | D PASS-THROUGH | point_of_sale | 'pos_config_id.cash_rounding' | point_of_sale/models/res_config_settings.py:64 |
| `pos_company_has_template` | D PASS-THROUGH | point_of_sale | 'pos_config_id.company_has_template' | point_of_sale/models/res_config_settings.py:65 |
| `pos_crm_team_id` | D PASS-THROUGH | pos_sale | 'pos_config_id.crm_team_id' | pos_sale/models/res_config_settings.py:9 |
| `pos_customer_display_bg_img` | D PASS-THROUGH | point_of_sale | 'pos_config_id.customer_display_bg_img' | point_of_sale/models/res_config_settings.py:45 |
| `pos_customer_display_bg_img_name` | D PASS-THROUGH | point_of_sale | 'pos_config_id.customer_display_bg_img_name' | point_of_sale/models/res_config_settings.py:46 |
| `pos_default_bill_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.default_bill_ids' | point_of_sale/models/res_config_settings.py:66 |
| `pos_default_preset_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.default_preset_id' | point_of_sale/models/res_config_settings.py:50 |
| `pos_default_screen` | D PASS-THROUGH | pos_restaurant | 'pos_config_id.default_screen' | pos_restaurant/models/res_config_settings.py:13 |
| `pos_down_payment_product_id` | D PASS-THROUGH | pos_sale | 'pos_config_id.down_payment_product_id' | pos_sale/models/res_config_settings.py:10 |
| `pos_epson_printer_ip` | D PASS-THROUGH | point_of_sale | 'pos_config_id.epson_printer_ip' | point_of_sale/models/res_config_settings.py:121 |
| `pos_fallback_nomenclature_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.fallback_nomenclature_id' | point_of_sale/models/res_config_settings.py:119 |
| `pos_fast_payment_method_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.fast_payment_method_ids' | point_of_sale/models/res_config_settings.py:123 |
| `pos_floor_ids` | D PASS-THROUGH | pos_restaurant | 'pos_config_id.floor_ids' | pos_restaurant/models/res_config_settings.py:9 |
| `pos_has_active_session` | D PASS-THROUGH | point_of_sale | 'pos_config_id.has_active_session' | point_of_sale/models/res_config_settings.py:69 |
| `pos_iface_big_scrollbars` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_big_scrollbars' | point_of_sale/models/res_config_settings.py:71 |
| `pos_iface_display_id` | D PASS-THROUGH | pos_iot | 'pos_config_id.iface_display_id' | pos_iot/models/res_config_settings.py:15 |
| `pos_iface_group_by_categ` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_group_by_categ' | point_of_sale/models/res_config_settings.py:72 |
| `pos_iface_print_auto` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_print_auto' | point_of_sale/models/res_config_settings.py:75 |
| `pos_iface_print_skip_screen` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_print_skip_screen' | point_of_sale/models/res_config_settings.py:76 |
| `pos_iface_printer_id` | D PASS-THROUGH | pos_iot | 'pos_config_id.iface_printer_id' | pos_iot/models/res_config_settings.py:16 |
| `pos_iface_scale_id` | D PASS-THROUGH | pos_iot | 'pos_config_id.iface_scale_id' | pos_iot/models/res_config_settings.py:17 |
| `pos_iface_scanner_ids` | D PASS-THROUGH | pos_iot | 'pos_config_id.iface_scanner_ids' | pos_iot/models/res_config_settings.py:18 |
| `pos_iface_tax_included` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_tax_included' | point_of_sale/models/res_config_settings.py:79 |
| `pos_iface_tipproduct` | D PASS-THROUGH | point_of_sale | 'pos_config_id.iface_tipproduct' | point_of_sale/models/res_config_settings.py:80 |
| `pos_invoice_journal_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.invoice_journal_id' | point_of_sale/models/res_config_settings.py:81 |
| `pos_is_closing_entry_by_product` | D PASS-THROUGH | point_of_sale | 'pos_config_id.is_closing_entry_by_product' | point_of_sale/models/res_config_settings.py:116 |
| `pos_is_company_country_germany` | D PASS-THROUGH | l10n_de_pos_cert | 'pos_config_id.is_company_country_germany' | l10n_de_pos_cert/models/res_config_settings.py:11 |
| `pos_is_header_or_footer` | D PASS-THROUGH | point_of_sale | 'pos_config_id.is_header_or_footer' | point_of_sale/models/res_config_settings.py:82 |
| `pos_is_margins_costs_accessible_to_every_user` | D PASS-THROUGH | point_of_sale | 'pos_config_id.is_margins_costs_accessible_to_every_user' | point_of_sale/models/res_config_settings.py:83 |
| `pos_is_posbox` | D PASS-THROUGH | point_of_sale | 'pos_config_id.is_posbox' | point_of_sale/models/res_config_settings.py:84 |
| `pos_journal_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.journal_id' | point_of_sale/models/res_config_settings.py:85 |
| `pos_l10n_br_invoice_serial` | D PASS-THROUGH | l10n_br_edi_pos | 'pos_config_id.l10n_br_invoice_serial' | l10n_br_edi_pos/models/res_config_settings.py:9 |
| `pos_l10n_br_is_nfce` | D PASS-THROUGH | l10n_br_edi_pos | 'pos_config_id.l10n_br_is_nfce' | l10n_br_edi_pos/models/res_config_settings.py:8 |
| `pos_l10n_de_create_tss_flag` | D PASS-THROUGH | l10n_de_pos_cert | 'pos_config_id.l10n_de_create_tss_flag' | l10n_de_pos_cert/models/res_config_settings.py:12 |
| `pos_l10n_de_fiskaly_client_id` | D PASS-THROUGH | l10n_de_pos_cert | 'pos_config_id.l10n_de_fiskaly_client_id' | l10n_de_pos_cert/models/res_config_settings.py:13 |
| `pos_l10n_de_fiskaly_tss_id` | D PASS-THROUGH | l10n_de_pos_cert | 'pos_config_id.l10n_de_fiskaly_tss_id' | l10n_de_pos_cert/models/res_config_settings.py:14 |
| `pos_l10n_gt_final_consumer_limit` | D PASS-THROUGH | l10n_gt_edi_pos | 'pos_config_id.l10n_gt_final_consumer_limit' | l10n_gt_edi_pos/models/res_config_settings.py:7 |
| `pos_l10n_vn_auto_send_to_sinvoice` | D PASS-THROUGH | l10n_vn_edi_viettel_pos | 'pos_config_id.l10n_vn_auto_send_to_sinvoice' | l10n_vn_edi_viettel_pos/models/res_config_settings.py:19 |
| `pos_l10n_vn_pos_symbol` | D PASS-THROUGH | l10n_vn_edi_viettel_pos | 'pos_config_id.l10n_vn_pos_symbol' | l10n_vn_edi_viettel_pos/models/res_config_settings.py:15 |
| `pos_limit_categories` | D PASS-THROUGH | point_of_sale | 'pos_config_id.limit_categories' | point_of_sale/models/res_config_settings.py:86 |
| `pos_manual_discount` | D PASS-THROUGH | point_of_sale | 'pos_config_id.manual_discount' | point_of_sale/models/res_config_settings.py:87 |
| `pos_minimal_employee_ids` | D PASS-THROUGH | pos_hr | 'pos_config_id.minimal_employee_ids' | pos_hr/models/res_config_settings.py:14 |
| `pos_module_pos_appointment` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_appointment' | point_of_sale/models/res_config_settings.py:55 |
| `pos_module_pos_avatax` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_avatax' | point_of_sale/models/res_config_settings.py:56 |
| `pos_module_pos_discount` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_discount' | point_of_sale/models/res_config_settings.py:52 |
| `pos_module_pos_hr` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_hr' | point_of_sale/models/res_config_settings.py:53 |
| `pos_module_pos_restaurant` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_restaurant' | point_of_sale/models/res_config_settings.py:54 |
| `pos_module_pos_sms` | D PASS-THROUGH | point_of_sale | 'pos_config_id.module_pos_sms' | point_of_sale/models/res_config_settings.py:115 |
| `pos_module_pos_urban_piper` | D PASS-THROUGH | pos_enterprise | 'pos_config_id.module_pos_urban_piper' | pos_enterprise/models/res_config_settings.py:7 |
| `pos_note_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.note_ids' | point_of_sale/models/res_config_settings.py:114 |
| `pos_only_round_cash_method` | D PASS-THROUGH | point_of_sale | 'pos_config_id.only_round_cash_method' | point_of_sale/models/res_config_settings.py:88 |
| `pos_order_edit_tracking` | D PASS-THROUGH | point_of_sale | 'pos_config_id.order_edit_tracking' | point_of_sale/models/res_config_settings.py:117 |
| `pos_other_devices` | D PASS-THROUGH | point_of_sale | 'pos_config_id.other_devices' | point_of_sale/models/res_config_settings.py:89 |
| `pos_payment_method_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.payment_method_ids' | point_of_sale/models/res_config_settings.py:90 |
| `pos_picking_policy` | D PASS-THROUGH | point_of_sale | 'pos_config_id.picking_policy' | point_of_sale/models/res_config_settings.py:91 |
| `pos_picking_type_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.picking_type_id' | point_of_sale/models/res_config_settings.py:92 |
| `pos_printer_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.printer_ids' | point_of_sale/models/res_config_settings.py:58 |
| `pos_proxy_ip` | D PASS-THROUGH | point_of_sale | 'pos_config_id.proxy_ip' | point_of_sale/models/res_config_settings.py:94 |
| `pos_restrict_price_control` | D PASS-THROUGH | point_of_sale | 'pos_config_id.restrict_price_control' | point_of_sale/models/res_config_settings.py:97 |
| `pos_rounding_method` | D PASS-THROUGH | point_of_sale | 'pos_config_id.rounding_method' | point_of_sale/models/res_config_settings.py:98 |
| `pos_route_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.route_id' | point_of_sale/models/res_config_settings.py:99 |
| `pos_self_ordering_available_language_ids` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_available_language_ids' | pos_self_order/models/res_config_settings.py:17 |
| `pos_self_ordering_default_language_id` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_default_language_id' | pos_self_order/models/res_config_settings.py:16 |
| `pos_self_ordering_default_user_id` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_default_user_id' | pos_self_order/models/res_config_settings.py:23 |
| `pos_self_ordering_image_background_ids` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_image_background_ids' | pos_self_order/models/res_config_settings.py:19 |
| `pos_self_ordering_image_brand` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_image_brand' | pos_self_order/models/res_config_settings.py:20 |
| `pos_self_ordering_image_brand_name` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_image_brand_name' | pos_self_order/models/res_config_settings.py:21 |
| `pos_self_ordering_image_home_ids` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_image_home_ids' | pos_self_order/models/res_config_settings.py:18 |
| `pos_self_ordering_mode` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_mode' | pos_self_order/models/res_config_settings.py:15 |
| `pos_self_ordering_pay_after` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_pay_after' | pos_self_order/models/res_config_settings.py:22 |
| `pos_self_ordering_service_mode` | D PASS-THROUGH | pos_self_order | 'pos_config_id.self_ordering_service_mode' | pos_self_order/models/res_config_settings.py:14 |
| `pos_set_maximum_difference` | D PASS-THROUGH | point_of_sale | 'pos_config_id.set_maximum_difference' | point_of_sale/models/res_config_settings.py:101 |
| `pos_ship_later` | D PASS-THROUGH | point_of_sale | 'pos_config_id.ship_later' | point_of_sale/models/res_config_settings.py:102 |
| `pos_show_category_images` | D PASS-THROUGH | point_of_sale | 'pos_config_id.show_category_images' | point_of_sale/models/res_config_settings.py:112 |
| `pos_show_product_images` | D PASS-THROUGH | point_of_sale | 'pos_config_id.show_product_images' | point_of_sale/models/res_config_settings.py:111 |
| `pos_tax_regime_selection` | D PASS-THROUGH | point_of_sale | 'pos_config_id.tax_regime_selection' | point_of_sale/models/res_config_settings.py:103 |
| `pos_trusted_config_ids` | D PASS-THROUGH | point_of_sale | 'pos_config_id.trusted_config_ids' | point_of_sale/models/res_config_settings.py:109 |
| `pos_urbanpiper_delivery_provider_ids` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_delivery_provider_ids' | pos_urban_piper/models/res_config_settings.py:54 |
| `pos_urbanpiper_fiscal_position_id` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_fiscal_position_id' | pos_urban_piper/models/res_config_settings.py:30 |
| `pos_urbanpiper_last_sync_date` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_last_sync_date' | pos_urban_piper/models/res_config_settings.py:43 |
| `pos_urbanpiper_minimum_preparation_time` | D PASS-THROUGH | pos_urban_piper_enhancements | 'pos_config_id.urbanpiper_minimum_preparation_time' | pos_urban_piper_enhancements/models/res_config_settings.py:7 |
| `pos_urbanpiper_payment_methods_ids` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_payment_methods_ids' | pos_urban_piper/models/res_config_settings.py:36 |
| `pos_urbanpiper_pricelist_id` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_pricelist_id' | pos_urban_piper/models/res_config_settings.py:24 |
| `pos_urbanpiper_store_identifier` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_store_identifier' | pos_urban_piper/models/res_config_settings.py:18 |
| `pos_urbanpiper_webhook_url` | D PASS-THROUGH | pos_urban_piper | 'pos_config_id.urbanpiper_webhook_url' | pos_urban_piper/models/res_config_settings.py:48 |
| `pos_use_fast_payment` | D PASS-THROUGH | point_of_sale | 'pos_config_id.use_fast_payment' | point_of_sale/models/res_config_settings.py:122 |
| `pos_use_presets` | D PASS-THROUGH | point_of_sale | 'pos_config_id.use_presets' | point_of_sale/models/res_config_settings.py:49 |
| `pos_use_pricelist` | D PASS-THROUGH | point_of_sale | 'pos_config_id.use_pricelist' | point_of_sale/models/res_config_settings.py:105 |
| `pos_warehouse_id` | D PASS-THROUGH | point_of_sale | 'pos_config_id.warehouse_id' | point_of_sale/models/res_config_settings.py:106 |
| `sale_tax_id` | D PASS-THROUGH | point_of_sale | 'company_id.account_sale_tax_id' | point_of_sale/models/res_config_settings.py:32 |
| `security_lead` | D PASS-THROUGH | sale_stock | 'company_id.security_lead' | sale_stock/models/res_config_settings.py:10 |
| `stock_confirmation_type` | D PASS-THROUGH | stock | 'company_id.stock_confirmation_type' | stock/models/res_config_settings.py:58 |
| `stock_confirmation_wa_template_id` | D PASS-THROUGH | whatsapp_stock | 'company_id.stock_confirmation_wa_template_id' | whatsapp_stock/models/res_config_settings.py:7 |
| `stock_move_email_validation` | D PASS-THROUGH | stock | 'company_id.stock_move_email_validation' | stock/models/res_config_settings.py:31 |
| `stock_sms_confirmation_template_id` | D PASS-THROUGH | stock_sms | 'company_id.stock_sms_confirmation_template_id' | stock_sms/models/res_config_settings.py:10 |
| `stock_text_confirmation` | D PASS-THROUGH | stock | 'company_id.stock_text_confirmation' | stock/models/res_config_settings.py:57 |
| `update_stock_quantities` | D PASS-THROUGH | point_of_sale | 'company_id.point_of_sale_update_stock_quantities' | point_of_sale/models/res_config_settings.py:41 |
| `urbanpiper_apikey` | D PASS-THROUGH | pos_urban_piper | 'company_id.pos_urbanpiper_apikey' | pos_urban_piper/models/res_config_settings.py:14 |
| `urbanpiper_username` | D PASS-THROUGH | pos_urban_piper | 'company_id.pos_urbanpiper_username' | pos_urban_piper/models/res_config_settings.py:10 |
| `website_warehouse_id` | D PASS-THROUGH | website_sale_stock | 'website_id.warehouse_id' | website_sale_stock/models/res_config_settings.py:25 |
| `default_allow_out_of_stock_order` | E PLAIN/COMPUTED | website_sale_stock | — | website_sale_stock/models/res_config_settings.py:10 |
| `default_available_threshold` | E PLAIN/COMPUTED | website_sale_stock | — | website_sale_stock/models/res_config_settings.py:15 |
| `default_picking_policy` | E PLAIN/COMPUTED | sale_stock | — | sale_stock/models/res_config_settings.py:15 |
| `default_show_availability` | E PLAIN/COMPUTED | website_sale_stock | — | website_sale_stock/models/res_config_settings.py:20 |
| `has_amazon_account` | E PLAIN/COMPUTED | sale_amazon | — | sale_amazon/models/res_config_settings.py:9 |
| `is_installed_sale` | E PLAIN/COMPUTED | purchase_stock | — | purchase_stock/models/res_config_settings.py:13 |
| `is_kiosk_mode` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:44 |
| `padding_time` | E PLAIN/COMPUTED | sale_stock_renting | — | sale_stock_renting/models/res_config_settings.py:11 |
| `pos_allowed_pricelist_ids` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:60 |
| `pos_available_pricelist_ids` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:62 |
| `pos_config_id` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:31 |
| `pos_default_fiscal_position_id` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:67 |
| `pos_fiscal_position_ids` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:68 |
| `pos_iface_available_categ_ids` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:70 |
| `pos_iface_cashdrawer` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:73 |
| `pos_iface_electronic_scale` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:74 |
| `pos_iface_print_via_proxy` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:77 |
| `pos_iface_printbill` | E PLAIN/COMPUTED | pos_restaurant | — | pos_restaurant/models/res_config_settings.py:10 |
| `pos_iface_scan_via_proxy` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:78 |
| `pos_iface_splitbill` | E PLAIN/COMPUTED | pos_restaurant | — | pos_restaurant/models/res_config_settings.py:11 |
| `pos_is_order_printer` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:57 |
| `pos_pricelist_id` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:93 |
| `pos_receipt_footer` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:95 |
| `pos_receipt_header` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:96 |
| `pos_selectable_categ_ids` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:100 |
| `pos_set_tip_after_payment` | E PLAIN/COMPUTED | pos_restaurant | — | pos_restaurant/models/res_config_settings.py:12 |
| `pos_tip_product_id` | E PLAIN/COMPUTED | point_of_sale | — | point_of_sale/models/res_config_settings.py:104 |
| `replenish_on_order` | E PLAIN/COMPUTED | stock | — | stock/models/res_config_settings.py:56 |
| `show_barcode_nomenclature` | E PLAIN/COMPUTED | stock_barcode | — | stock_barcode/models/res_config_settings.py:9 |
| `stock_barcode_demo_active` | E PLAIN/COMPUTED | stock_barcode | — | stock_barcode/models/res_config_settings.py:8 |
---

## 4. Findings

### FT-F-01 — A "feature toggle" is five different mechanisms wearing one costume (**CRITICAL**)
They differ in **where state lives**, **who can change it**, **what audit exists**, **what company or
tenant scope applies**, and **what happens when it is switched off after use**. A register — or a
SMEsPlus design — that models one mechanism models 8.9% of the surface (class B) or 58.2% (class D),
never the whole.

### FT-F-02 — 17.3% of toggles are software installation, not configuration
Class A toggles install code. On a multi-tenant platform this is not a per-tenant preference; it is a
deployment act. **Whether a tenant may flip a class-A toggle is a platform decision reserved to Boss**
and is raised as `BOSS-DEC-03`.

### FT-F-03 — The dominant class stores state off-screen
Class D (58.2%) writes to a different object. Consequences that must be designed, not inherited:
the setting's **company scope** is the storing object's scope; its **audit trail** is the storing
object's; and two settings screens can disagree if the storing objects differ.

### FT-F-04 — A system parameter can silently disable a data-mutating routine
Class C includes at least one parameter that, when set, **suppresses a routine that otherwise runs as
a side effect of opening a menu** (Register 08, `HA-F-01`). It appears on no settings screen.
**A configuration surface that is invisible to the configuration UI is a control gap**, and it is one
that would not appear in any menu-driven or settings-driven research.

### FT-F-07 — A toggle's effect surface is not the screen (**CRITICAL for method**)
Traced system-wide, 7 of the 21 group-toggles take effect **only** in printed/report templates (4) or
in runtime code branches (3); one of the latter also reaches a boundary object. See Register 02
`CD-F-03`. **"What does this switch do?" cannot be answered from screens.**

### FT-F-05 — The same toggle is declared by more than one module
Several toggle field names are declared by two different modules. The declarations are not guaranteed
identical. Recorded as an integrity hazard: a register keyed on toggle *name* would silently merge two
different declarations.

### FT-F-06 — Toggle count is generation-sensitive
R2 (series-18): **230–233** declarations across two independent comparators; R1 (series-19): **237**.
Small in magnitude, but it demonstrates the rule: **a toggle register is valid only for the generation
it was read from.**
