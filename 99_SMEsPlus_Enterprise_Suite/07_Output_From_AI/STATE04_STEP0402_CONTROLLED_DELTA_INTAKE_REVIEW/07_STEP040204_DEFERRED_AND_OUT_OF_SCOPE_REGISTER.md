# [STATE04][STEP0402][STEP040204] DEFERRED AND OUT-OF-SCOPE REGISTER

## Summary

**Deferred Items:** 0  
**Out-of-Scope Items:** 56  

This register documents items excluded from Thailand-scope Functional Design consideration.

## OUT-OF-SCOPE ITEMS (56)

### General Business Functions (44 Items)

Items that provide generally applicable ERP capabilities not specific to Thailand and suitable for the Open ERP baseline:

- **Data & Infrastructure:** auto_database_backup, wk_redis_session, import_bridge_axis, nthub_binary_field_preview, oi_action_file, oi_pdf_viewer, oi_jasper_report, om_data_remove, web_window_title, tracking_history
- **Sales:** order_line_sequence, sale_gross_profit_record, sale_order_line_price_history, sale_productinfo_ext, product_brand_sale
- **Purchasing:** purchase_request, purchase_order_lines_discount, purchase_discount_catalog
- **Product Management:** product_sequence, product_category_filter, product_variant_reference, product_stock_equipment
- **Accounting:** bi_print_journal_entries, dev_print_cheque, cr_effective_date_entries, print_payment_remittance_adviec, print_voucher_request, report_xlsx, report_xlsx_helper
- **Master Data:** base_location, base_location_geonames_import, contact_reference_sequence, partner_company_type, partner_firstname
- **Approvals:** multi_level_approval, multi_level_approval_configuration, multi_level_approval_hr
- **Utilities:** courier_type, date_range, deepseek_r1, equipment_sequence, full_summarize_bills, app_icon_hide

### SMEsPlus Company-Specific Customizations (11 Items)

Items that are company-specific implementations outside the authorized SMEsPlus project scope:

- hide_smesplus_menu
- monday_smesplus_connector
- smesplus_account_reports
- smesplus_advance_expense_request
- smesplus_custom_title_and_favicon
- smesplus_inventory_lot_filter
- smesplus_product_image
- smesplus_purchase_advance_payment
- smesplus_so_section_bydivision
- smesplus_sol_global_discount
- smesplus_special_access_rights
- smesplus_tax_period_date
- smesplus_uom_ext

### Disposition and Next Steps

**General Business Functions:**
- Decision Owner: Future Open ERP Baseline architecture decision
- Proposed Action: Consider for future Open ERP core functionality scoping
- Boss Decision Required: NO (architectural decision, not authorization)

**SMEsPlus Customizations:**
- Decision Owner: SMEsPlus company management
- Proposed Action: Retain as company-specific implementations; outside SMEsPlus project scope
- Boss Decision Required: NO (explicitly excluded by scope)

## DEFERRED ITEMS: NONE

All 69 Controlled Delta items have been classified with sufficient evidence. No items remain deferred pending future decision.

---

_Generated: 2026-07-17_
