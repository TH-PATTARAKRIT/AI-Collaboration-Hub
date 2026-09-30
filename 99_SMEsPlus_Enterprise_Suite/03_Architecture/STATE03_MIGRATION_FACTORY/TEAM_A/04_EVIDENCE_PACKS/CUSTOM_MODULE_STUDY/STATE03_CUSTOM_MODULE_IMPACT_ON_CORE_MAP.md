# STATE03_CUSTOM_MODULE_IMPACT_ON_CORE_MAP

> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

**Scope:** maps each license-readable custom / third-party module to the Odoo Community core modules whose objects it extends (by `_inherit` text scan; not MRO analysis). Closed-license modules are listed by name + license only. The mapping is a research aid: **presence of an extension is not proof it is installed** (effective installed set unknown).

**Counts (actual):** license-readable custom/third-party modules studied = 117 (individual notes in this folder); license-gated modules (name + license only) = 41; core modules touched by at least one readable custom module = 13; modules whose note contains the phrase `ALTERS CORE CONTROL` on a line that is not clearly a negation (text heuristic — may over-count; read the note) = 70.

## A. Core module → custom / third-party modules that extend its objects
| Core module | # custom | Custom modules (license · class · `ALTERS CORE CONTROL` mark count) · core objects extended · sample of core method names overridden |
|---|---|---|
| `base` | 43 | `19_attachment_dedup_fix` (LGPL-3 · Third-party · 1) → `ir.attachment` ⟶ overrides: _get_datas_related_values<br>`account_credit_control` (AGPL-3 · Third-party · 3) → `res.company`, `res.config.settings`, `res.partner`<br>`account_financial_report` (AGPL-3 · Third-party · 0) → `ir.actions.report`, `res.config.settings` ⟶ overrides: _render_qweb_html, get_values, set_values<br>`account_fiscal_year` (AGPL-3 · Third-party · 0) → `res.company`<br>`account_lock_date_update` (AGPL-3 · Third-party · 1) → `res.company`<br>`base_accounting_kit` (LGPL-3 · Third-party · 7) → `res.company`, `res.config.settings`, `res.partner` ⟶ overrides: create, get_values, set_values, write<br>`base_location` (AGPL-3 · Third-party · 1) → `res.company`, `res.partner` ⟶ overrides: _address_fields, _get_company_address_field_names, _inverse_country, _inverse_state<br>`base_location_geonames_import` (AGPL-3 · Third-party · 1) → `res.country`<br>`bh_parent_company` (LGPL-3 · Customer-authorized · 1) → `res.partner`<br>`convert_amount_text_to_thai` (AGPL-3 · Third-party · 1) → `res.currency` ⟶ overrides: amount_to_text<br>`courier_type` (LGPL-3 · Customer-authorized · 1) → `res.partner` ⟶ overrides: write<br>`deepseek_r1` (GPL-3 · Third-party · 1) → `res.config.settings`<br>`l10n_th_amount_to_text` (AGPL-3 · Third-party · 1) → `res.currency` ⟶ overrides: amount_to_text<br>`l10n_th_base_location` (AGPL-3 · Third-party · 0) → `res.company`, `res.country.state`, `res.partner` ⟶ overrides: _inverse_street2<br>`l10n_th_partner` (AGPL-3 · Third-party · 1) → `res.company`, `res.partner`, `res.users` ⟶ overrides: create<br>`l10n_th_withholding_tax_report` (AGPL-3 · Third-party · 0) → `ir.actions.report`, `ir.ui.view`<br>`mis_builder` (AGPL-3 · Third-party · 0) → `ir.actions.report` ⟶ overrides: _render_qweb_pdf<br>`monday_odoo_connector` (AGPL-3 · Third-party · 1) → `res.partner`, `res.users`<br>`monday_smesplus_connector` (AGPL-3 · Third-party · 1) → `res.partner`, `res.users`<br>`om_account_accountant` (LGPL-3 · Third-party · 3) → `res.config.settings`<br>`om_account_followup` (LGPL-3 · Third-party · 0) → `res.config.settings`, `res.partner` ⟶ overrides: write<br>`om_data_remove` (LGPL-3 · Third-party · 1) → `res.config.settings`<br>`om_fiscal_year` (LGPL-3 · Third-party · 3) → `res.company`, `res.config.settings`<br>`partner_company_type` (AGPL-3 · Third-party · 0) → `res.partner`<br>`partner_firstname` (AGPL-3 · Third-party · 2) → `res.config.settings`, `res.partner`, `res.users` ⟶ overrides: create, default_get<br>`product_brand_sale` (AGPL-3 · Third-party · 4) → `res.company`, `res.config.settings`, `res.partner`, `res.users` ⟶ overrides: get_values, set_values<br>`purchase_request_level_approve` (LGPL-3 · Third-party · 0) → `res.config.settings`<br>`purchase_request_level_approve_po` (LGPL-3 · Third-party · 1) → `res.config.settings`<br>`report_xlsx` (AGPL-3 · Third-party · 0) → `ir.actions.report` ⟶ overrides: _get_report_from_name<br>`report_xlsx_helper` (AGPL-3 · Third-party · 1) → `ir.actions.report`<br>`scgl_account_deferred` (LGPL-3 · Customer-authorized · 2) → `res.company`, `res.config.settings`<br>`scgl_account_tax_return` (LGPL-3 · Customer-authorized · 1) → `res.company`, `res.config.settings`<br>`scgl_custom_title_and_favicon` (LGPL-3 · Customer-authorized · 0) → `ir.ui.view`, `res.company`, `res.config.settings` ⟶ overrides: _get_logo, _render_template, get_values, set_values<br>`scgl_jasper_api` (LGPL-3 · Customer-authorized · 1) → `res.users`<br>`scgl_partner_followup` (LGPL-3 · Customer-authorized · 0) → `res.partner`<br>`scgl_pos_payment_ext` (LGPL-3 · Customer-authorized · 1) → `res.company`<br>`scgl_purchase_advance_payment` (LGPL-3 · Customer-authorized · 2) → `res.config.settings`<br>`scgl_timesheet_grid` (LGPL-3 · Customer-authorized · 1) → `ir.actions.act_window.view`, `ir.ui.view`<br>`smesplus_custom_title_and_favicon` (LGPL-3 · Company · 0) → `ir.ui.view`, `res.company`, `res.config.settings` ⟶ overrides: _get_logo, _render_template, get_values, set_values<br>`smesplus_purchase_advance_payment` (LGPL-3 · Company · 1) → `res.config.settings`<br>`social_hub` (LGPL-3 · Third-party · 0) → `res.config.settings`<br>`web_responsive` (LGPL-3 · Third-party · 0) → `ir.http`, `res.users`<br>`web_window_title` (LGPL-3 · Third-party · 0) → `ir.ui.view`, `res.config.settings` ⟶ overrides: _render_template, get_values, set_values |
| `account` | 27 | `account_asset_management` (AGPL-3 · Third-party · 3) → `account.account`, `account.move`, `account.move.line` ⟶ overrides: action_post, button_draft, create, unlink, write<br>`account_credit_control` (AGPL-3 · Third-party · 3) → `account.account`, `account.move` ⟶ overrides: button_cancel<br>`account_financial_report` (AGPL-3 · Third-party · 0) → `account.account`, `account.group`, `account.move.line`<br>`account_invoice_refund_link` (AGPL-3 · Third-party · 0) → `account.move`, `account.move.line`, `account.move.reversal` ⟶ overrides: copy_data, reverse_moves<br>`account_payment_multi_deduction` (AGPL-3 · Third-party · 1) → `account.payment`, `account.payment.register` ⟶ overrides: _create_payment_vals_from_wizard, _prepare_move_line_default_vals, write<br>`accounting_pdf_reports` (LGPL-3 · Third-party · 0) → `account.move.line`<br>`base_accounting_kit` (LGPL-3 · Third-party · 7) → `account.account`, `account.bank.statement.line`, `account.journal`, `account.move`, `account.move.line`, `account.payment`, `account.payment.method`, `account.payment.register`, `report.account.report_invoice` ⟶ overrides: _create_payment_vals_from_batch, _create_payment_vals_from_wizard, _generate_move_vals, _get_payment_method_information, _get_report_values, _get_trigger_fields_to_synchronize…<br>`courier_type` (LGPL-3 · Customer-authorized · 1) → `account.move`<br>`l10n_th_withholding_tax` (AGPL-3 · Third-party · 4) → `account.account`, `account.move`, `account.move.line`, `account.payment`, `account.payment.register`, `account.tax` ⟶ overrides: _add_accounting_data_to_base_line_tax_details, _compute_amount, _compute_payment_difference_handling, _create_payment_vals_from_wizard, _prepare_base_line_grouping_key, create…<br>`l10n_th_withholding_tax_cert` (AGPL-3 · Customer-authorized · 0) → `account.account`, `account.move`, `account.payment` ⟶ overrides: create, write<br>`l10n_th_withholding_tax_multi` (AGPL-3 · Third-party · 1) → `account.move.line`, `account.payment.register` ⟶ overrides: _compute_payment_difference_handling<br>`om_account_accountant` (LGPL-3 · Third-party · 3) → `account.move` ⟶ overrides: _get_invoice_in_payment_state<br>`om_account_asset` (LGPL-3 · Third-party · 1) → `account.move`, `account.move.line` ⟶ overrides: _inverse_product_id, action_post, button_cancel, button_draft, default_get<br>`om_account_followup` (LGPL-3 · Third-party · 0) → `account.move.line`<br>`order_line_sequence` (AGPL-3 · Third-party · 1) → `account.move.line`<br>`product_brand_sale` (AGPL-3 · Third-party · 4) → `account.move`, `account.move.line` ⟶ overrides: create<br>`scgl_account_coa` (LGPL-3 · Customer-authorized · 1) → `account.account`<br>`scgl_account_deferred` (LGPL-3 · Customer-authorized · 2) → `account.move`, `account.move.line` ⟶ overrides: _post, button_cancel, button_draft<br>`scgl_account_reconcile` (LGPL-3 · Customer-authorized · 1) → `account.move.line`<br>`scgl_account_reports` (LGPL-3 · Customer-authorized · 1) → `account.move.line`<br>`scgl_account_tax_return` (LGPL-3 · Customer-authorized · 1) → `account.move`<br>`scgl_advance_expense_request` (LGPL-3 · Customer-authorized · 2) → `account.move`, `account.move.line`<br>`scgl_tax_period_date` (LGPL-3 · Customer-authorized · 1) → `account.move`, `account.move.line` ⟶ overrides: create<br>`smesplus_account` (LGPL-3 · Company · 1) → `account.account`, `account.journal`, `account.move`, `account.move.line` ⟶ overrides: _post<br>`smesplus_account_reports` (LGPL-3 · Company · 1) → `account.move.line`<br>`smesplus_advance_expense_request` (LGPL-3 · Company · 1) → `account.move`, `account.move.line`<br>`smesplus_tax_period_date` (LGPL-3 · Company · 1) → `account.move`, `account.move.line` ⟶ overrides: create |
| `mail` | 17 | `account_asset_management` (AGPL-3 · Third-party · 3) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: _compute_display_name, create, unlink, write<br>`account_credit_control` (AGPL-3 · Third-party · 3) → `mail.activity.mixin`, `mail.compose.message`, `mail.mail`, `mail.thread` ⟶ overrides: _compute_body, _message_auto_subscribe_followers, _postprocess_sent_message, _send, unlink, write<br>`agreement` (AGPL-3 · Third-party · 0) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: _compute_display_name<br>`auto_database_backup` (LGPL-3 · Third-party · 1) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: create, write<br>`base_account_budget` (LGPL-3 · Third-party · 1) → `mail.thread`<br>`base_accounting_kit` (LGPL-3 · Third-party · 7) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: copy_data, create, unlink<br>`bh_parent_company` (LGPL-3 · Customer-authorized · 1) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: create, write<br>`deepseek_r1` (GPL-3 · Third-party · 1) → `discuss.channel` ⟶ overrides: _notify_thread<br>`l10n_th_withholding_tax_cert` (AGPL-3 · Customer-authorized · 0) → `mail.activity.mixin`, `mail.thread`<br>`om_account_asset` (LGPL-3 · Third-party · 1) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: copy_data, create, unlink, write<br>`om_account_budget` (LGPL-3 · Third-party · 0) → `mail.thread`<br>`purchase_request` (LGPL-3 · Third-party · 1) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: _compute_is_editable, create, unlink, write<br>`scgl_account_tax_return` (LGPL-3 · Customer-authorized · 1) → `mail.activity.mixin`, `mail.thread`<br>`scgl_advance_expense_request` (LGPL-3 · Customer-authorized · 2) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: _compute_is_editable, create, unlink, write<br>`smesplus_advance_expense_request` (LGPL-3 · Company · 1) → `mail.activity.mixin`, `mail.thread` ⟶ overrides: _compute_is_editable, create, unlink, write<br>`social_hub` (LGPL-3 · Third-party · 0) → `mail.activity.mixin`, `mail.thread`<br>`tracking_history` (LGPL-3 · Customer-authorized · 0) → `mail.message` |
| `sale` | 16 | `auto_gen_job_type` (LGPL-3 · Customer-authorized · 2) → `sale.order` ⟶ overrides: action_cancel, action_confirm<br>`base_accounting_kit` (LGPL-3 · Third-party · 7) → `sale.order` ⟶ overrides: _action_confirm<br>`bh_parent_company` (LGPL-3 · Customer-authorized · 1) → `sale.order` ⟶ overrides: create, write<br>`courier_type` (LGPL-3 · Customer-authorized · 1) → `sale.order` ⟶ overrides: _prepare_invoice, action_confirm, create, write<br>`delivery_split` (AGPL-3 · Third-party · 3) → `sale.order`, `sale.order.line`, `sale.report` ⟶ overrides: _from_sale, _group_by_sale, _prepare_procurement_values, _select_additional_fields<br>`order_line_sequence` (AGPL-3 · Third-party · 1) → `sale.order.line`<br>`product_3d_viewer` (LGPL-3 · Customer-authorized · 0) → `sale.order.line`<br>`product_brand_sale` (AGPL-3 · Third-party · 4) → `sale.order`, `sale.order.line`, `sale.report` ⟶ overrides: _compute_user_id, _create_invoices, _get_invoiceable_lines, _group_by_sale, _prepare_procurement_values, _select_additional_fields<br>`sale_gross_profit_record` (LGPL-3 · Third-party · 0) → `sale.order`, `sale.order.line`<br>`sale_job_type` (LGPL-3 · Customer-authorized · 0) → `sale.order`<br>`sale_order_level_approve` (LGPL-3 · Company · 1) → `sale.order` ⟶ overrides: _confirmation_error_message, _prepare_confirmation_values<br>`sale_order_line_price_history` (AGPL-3 · Customer-authorized · 1) → `sale.order.line`<br>`scgl_so_section_bydivision` (LGPL-3 · Customer-authorized · 2) → `sale.order`, `sale.order.line` ⟶ overrides: create, write<br>`scgl_sol_global_discount` (LGPL-3 · Customer-authorized · 0) → `sale.order`, `sale.order.discount`, `sale.order.line` ⟶ overrides: _prepare_global_discount_so_lines<br>`smesplus_so_section_bydivision` (LGPL-3 · Company · 1) → `sale.order`, `sale.order.line` ⟶ overrides: create, write<br>`smesplus_sol_global_discount` (LGPL-3 · Company · 1) → `sale.order`, `sale.order.discount`, `sale.order.line` ⟶ overrides: _prepare_global_discount_so_lines |
| `product` | 12 | `base_accounting_kit` (LGPL-3 · Third-party · 7) → `product.template`<br>`bh_product_label_qrcode` (LGPL-3 · Customer-authorized · 1) → `product.label.layout` ⟶ overrides: _prepare_report_data<br>`l10n_th_withholding_tax` (AGPL-3 · Third-party · 4) → `product.template`<br>`om_account_asset` (LGPL-3 · Third-party · 1) → `product.template`<br>`product_3d_viewer` (LGPL-3 · Customer-authorized · 0) → `product.template`<br>`product_brand_sale` (AGPL-3 · Third-party · 4) → `product.template`<br>`product_category_filter` (AGPL-3 · Customer-authorized · 0) → `product.category`, `product.template`<br>`product_sequence` (LGPL-3 · Customer-authorized · 0) → `product.category`, `product.template` ⟶ overrides: create, write<br>`purchase_request` (LGPL-3 · Third-party · 1) → `product.template`<br>`scgl_advance_expense_request` (LGPL-3 · Customer-authorized · 2) → `product.template`<br>`smesplus_advance_expense_request` (LGPL-3 · Company · 1) → `product.template`<br>`smesplus_uom_ext` (LGPL-3 · Company · 1) → `product.supplierinfo` |
| `stock` | 9 | `courier_type` (LGPL-3 · Customer-authorized · 1) → `stock.lot`, `stock.move.line`, `stock.picking`, `stock.quant`<br>`cr_effective_date_entries` (AGPL-3 · Third-party · 5) → `stock.picking` ⟶ overrides: _set_scheduled_date<br>`delivery_split` (AGPL-3 · Third-party · 3) → `stock.move` ⟶ overrides: _key_assign_picking, _search_picking_for_assignation<br>`order_line_sequence` (AGPL-3 · Third-party · 1) → `stock.move`<br>`purchase_request` (LGPL-3 · Third-party · 1) → `stock.move`, `stock.move.line`, `stock.picking`, `stock.rule`, `stock.warehouse.orderpoint` ⟶ overrides: _action_cancel, _action_done, _merge_moves_fields, _prepare_merge_moves_distinct_fields, _quantity_in_progress<br>`sale_job_type` (LGPL-3 · Customer-authorized · 0) → `stock.picking`<br>`scgl_inventory_lot_filter` (LGPL-3 · Customer-authorized · 0) → `stock.move.line`, `stock.scrap`<br>`smesplus_inventory_lot_filter` (LGPL-3 · Company · 1) → `stock.move.line`, `stock.scrap`<br>`stock_picking_reference_no` (LGPL-3 · Third-party · 1) → `stock.picking` |
| `purchase` | 9 | `bh_purchase_receipt_all` (LGPL-3 · Customer-authorized · 1) → `purchase.order`<br>`courier_type` (LGPL-3 · Customer-authorized · 1) → `purchase.order`, `purchase.report` ⟶ overrides: _group_by, _select<br>`order_line_sequence` (AGPL-3 · Third-party · 1) → `purchase.order.line`<br>`purchase_order_lines_discount` (AGPL-3 · Third-party · 1) → `purchase.order.line` ⟶ overrides: _prepare_account_move_line<br>`purchase_request` (LGPL-3 · Third-party · 1) → `purchase.order`, `purchase.order.line` ⟶ overrides: button_confirm, write<br>`purchase_request_level_approve_po` (LGPL-3 · Third-party · 1) → `purchase.order` ⟶ overrides: button_confirm, button_draft<br>`scgl_jasper_api` (LGPL-3 · Customer-authorized · 1) → `purchase.order`<br>`scgl_purchase_advance_payment` (LGPL-3 · Customer-authorized · 2) → `purchase.order.line`<br>`smesplus_purchase_advance_payment` (LGPL-3 · Company · 1) → `purchase.order.line` |
| `hr` | 7 | `base_location` (AGPL-3 · Third-party · 1) → `hr.employee`, `hr.employee.public`<br>`product_brand_sale` (AGPL-3 · Third-party · 4) → `hr.employee`<br>`purchase_request` (LGPL-3 · Third-party · 1) → `hr.employee`, `hr.employee.public`<br>`purchase_request_level_approve` (LGPL-3 · Third-party · 0) → `hr.employee`, `hr.employee.public`<br>`scgl_advance_expense_request` (LGPL-3 · Customer-authorized · 2) → `hr.employee`<br>`scgl_timesheet_grid` (LGPL-3 · Customer-authorized · 1) → `hr.employee`<br>`smesplus_advance_expense_request` (LGPL-3 · Company · 1) → `hr.employee` |
| `analytic` | 7 | `account_asset_management` (AGPL-3 · Third-party · 3) → `analytic.mixin` ⟶ overrides: _compute_analytic_distribution, create, write<br>`account_payment_multi_deduction` (AGPL-3 · Third-party · 1) → `analytic.mixin`<br>`base_account_budget` (LGPL-3 · Third-party · 1) → `account.analytic.account`<br>`base_accounting_kit` (LGPL-3 · Third-party · 7) → `analytic.mixin`<br>`om_account_asset` (LGPL-3 · Third-party · 1) → `analytic.mixin` ⟶ overrides: create, write<br>`om_account_budget` (LGPL-3 · Third-party · 0) → `account.analytic.account`<br>`scgl_timesheet_grid` (LGPL-3 · Customer-authorized · 1) → `account.analytic.line` |
| `sales_team` | 1 | `product_brand_sale` (AGPL-3 · Third-party · 4) → `crm.team` |
| `website` | 1 | `product_brand_sale` (AGPL-3 · Third-party · 4) → `website` ⟶ overrides: _search_exact |
| `uom` | 1 | `smesplus_uom_ext` (LGPL-3 · Company · 1) → `uom.uom` |
| `base_address_extended` | 1 | `base_location` (AGPL-3 · Third-party · 1) → `res.city` |

## B. Modules whose note contains the phrase `ALTERS CORE CONTROL` (heuristic; read the note before relying on it)

- `19_attachment_dedup_fix` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_19_attachment_dedup_fix.md`
- `account_asset_management` (3 mark line(s)) → `STATE03_CUSTOM_MODULE_account_asset_management.md`
- `account_credit_control` (3 mark line(s)) → `STATE03_CUSTOM_MODULE_account_credit_control.md`
- `account_lock_date_update` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_account_lock_date_update.md`
- `account_payment_multi_deduction` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_account_payment_multi_deduction.md`
- `auto_database_backup` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_auto_database_backup.md`
- `auto_gen_job_type` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_auto_gen_job_type.md`
- `base_account_budget` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_base_account_budget.md`
- `base_accounting_kit` (7 mark line(s)) → `STATE03_CUSTOM_MODULE_base_accounting_kit.md`
- `base_location` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_base_location.md`
- `base_location_geonames_import` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_base_location_geonames_import.md`
- `bh_generate_serial_lots` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_bh_generate_serial_lots.md`
- `bh_parent_company` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_bh_parent_company.md`
- `bh_product_label_qrcode` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_bh_product_label_qrcode.md`
- `bh_purchase_receipt_all` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_bh_purchase_receipt_all.md`
- `convert_amount_text_to_thai` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_convert_amount_text_to_thai.md`
- `courier_type` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_courier_type.md`
- `cr_effective_date_entries` (5 mark line(s)) → `STATE03_CUSTOM_MODULE_cr_effective_date_entries.md`
- `cybrosys_support_client` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_cybrosys_support_client.md`
- `date_range` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_date_range.md`
- `deepseek_r1` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_deepseek_r1.md`
- `delivery_split` (3 mark line(s)) → `STATE03_CUSTOM_MODULE_delivery_split.md`
- `l10n_th_amount_to_text` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_amount_to_text.md`
- `l10n_th_partner` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_partner.md`
- `l10n_th_reports_ext` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_reports_ext.md`
- `l10n_th_withholding_tax` (4 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_withholding_tax.md`
- `l10n_th_withholding_tax_cert_form` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_withholding_tax_cert_form.md`
- `l10n_th_withholding_tax_multi` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_l10n_th_withholding_tax_multi.md`
- `monday_odoo_connector` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_monday_odoo_connector.md`
- `monday_smesplus_connector` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_monday_smesplus_connector.md`
- `om_account_accountant` (3 mark line(s)) → `STATE03_CUSTOM_MODULE_om_account_accountant.md`
- `om_account_asset` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_om_account_asset.md`
- `om_data_remove` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_om_data_remove.md`
- `om_fiscal_year` (3 mark line(s)) → `STATE03_CUSTOM_MODULE_om_fiscal_year.md`
- `order_line_sequence` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_order_line_sequence.md`
- `partner_firstname` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_partner_firstname.md`
- `pr_multi_approval_bridge` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_pr_multi_approval_bridge.md`
- `product_brand_sale` (4 mark line(s)) → `STATE03_CUSTOM_MODULE_product_brand_sale.md`
- `purchase_order_lines_discount` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_purchase_order_lines_discount.md`
- `purchase_request` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_purchase_request.md`
- `purchase_request_level_approve_po` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_purchase_request_level_approve_po.md`
- `report_xlsx_helper` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_report_xlsx_helper.md`
- `sale_order_level_approve` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_sale_order_level_approve.md`
- `sale_order_line_price_history` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_sale_order_line_price_history.md`
- `scgl_account_coa` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_coa.md`
- `scgl_account_deferred` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_deferred.md`
- `scgl_account_menu` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_menu.md`
- `scgl_account_reconcile` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_reconcile.md`
- `scgl_account_reports` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_reports.md`
- `scgl_account_statements` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_statements.md`
- `scgl_account_tax_return` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_account_tax_return.md`
- `scgl_advance_expense_request` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_advance_expense_request.md`
- `scgl_jasper_api` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_jasper_api.md`
- `scgl_pos_payment_ext` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_pos_payment_ext.md`
- `scgl_purchase_advance_payment` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_purchase_advance_payment.md`
- `scgl_report_viewer` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_report_viewer.md`
- `scgl_so_section_bydivision` (2 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_so_section_bydivision.md`
- `scgl_stock_performance` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_stock_performance.md`
- `scgl_tax_period_date` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_tax_period_date.md`
- `scgl_timesheet_grid` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_scgl_timesheet_grid.md`
- `smesplus_account` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_account.md`
- `smesplus_account_reports` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_account_reports.md`
- `smesplus_advance_expense_request` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_advance_expense_request.md`
- `smesplus_inventory_lot_filter` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_inventory_lot_filter.md`
- `smesplus_purchase_advance_payment` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_purchase_advance_payment.md`
- `smesplus_so_section_bydivision` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_so_section_bydivision.md`
- `smesplus_sol_global_discount` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_sol_global_discount.md`
- `smesplus_tax_period_date` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_tax_period_date.md`
- `smesplus_uom_ext` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_smesplus_uom_ext.md`
- `stock_picking_reference_no` (1 mark line(s)) → `STATE03_CUSTOM_MODULE_stock_picking_reference_no.md`

## C. License-gated modules (code NOT read)
| Module | License found in manifest |
|---|---|
| `19_bhpro_inventory` | OPL-1 |
| `19_bhpro_master_data` | OPL-1 |
| `19_bhpro_menu_general` | OPL-1 |
| `19_bhpro_product_part` | OPL-1 |
| `19_bhpro_purchase_ext` | OPL-1 |
| `19_contact_reference_sequence` | OPL-1 |
| `19_product_variant_reference` | OPL-1 |
| `19_sale_lazada` | OPL-1 |
| `account_discount_catalog` | OPL-1 |
| `bi_print_journal_entries` | none |
| `bm_thai_rd_vat_company_search` | OPL-1 |
| `contact_reference_sequence` | OPL-1 |
| `d_product_brand` | OPL-1 |
| `d_product_brand_stock` | OPL-1 |
| `d_tiktok_shop_connector` | OPL-1 |
| `dev_print_cheque` | none |
| `equipment_sequence` | none |
| `full_summarize_bills` | none |
| `import_bridge_axis` | OPL-1 |
| `invoice_promptpay` | none |
| `multi_level_approval` | OPL-1 |
| `multi_level_approval_configuration` | OPL-1 |
| `multi_level_approval_hr` | OPL-1 |
| `odoo19_uom_ext` | none |
| `oi_action_file` | OPL-1 |
| `oi_jasper_report` | OPL-1 |
| `oi_pdf_viewer` | OPL-1 |
| `payment_2c2p` | Other proprietary |
| `print_payment_remittance_adviec` | none |
| `print_voucher_request` | none |
| `product_stock_equipment` | none |
| `product_variant_reference` | OPL-1 |
| `purchase_discount_catalog` | OPL-1 |
| `purchase_hide_line_buttons` | OPL-1 |
| `sale_productinfo_ext` | none |
| `scgl_import_product_images` | none |
| `scgl_product_image` | none |
| `scgl_special_access_rights` | none |
| `smesplus_product_image` | none |
| `smesplus_special_access_rights` | none |
| `wk_redis_session` | Other proprietary |

> Classification labels are inferred from the manifest `author` field only. `OEEL-1`: none found among the manifests inspected; Enterprise code is not present in the tree.

## D. Known limits
- Notes are sub-agent authored; the only content-check completed so far (Community `mrp` note) found, in its authoritative closing tally, about 87 claims checked: 60 supported, 16 partially supported, 2 not supported, 9 pointer-broken (the checker's own summary table says 62 claims — its two tallies disagree, so treat the numbers as approximate). Expect a similar error rate (roughly one claim in three not cleanly supported) in the other notes.
- Sensitive items (public routes without tokens, embedded shared credentials, raw-query reports that bypass record rules) are reported at business level only; values are not recorded.
