> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: om_data_remove

## 0. Header
- Module: om_data_remove
- License (confirmed in manifest): LGPL-3 (om_data_remove/__manifest__.py:10)
- Author (manifest): Odoo Mates, Sunpop.cn (om_data_remove/__manifest__.py:4)
- Version (manifest): 19.0.1.1 (om_data_remove/__manifest__.py:3)
- Path: addons_Extramodule/addons_extra/om_data_remove
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- An administrator screen ("Remove Data") that bulk-erases business transaction data so a database can be reset for a fresh start: sales orders, purchase orders/requisitions, point-of-sale orders, expenses, manufacturing orders, BOMs, inventory moves/pickings/lots, accounting entries/payments/bank statement lines, projects/tasks, quality records, website/blog records, products, product attributes, and the chatter (messages, followers, activities) (om_data_remove/models/model.py:43-349; views/view.xml:21-140).
- A "Delete all transactions except master data" button runs a fixed sequence across most areas (models/model.py:351-365; views/view.xml:21-24). Separate buttons act per area. "Clean and reset Account Chart" removes journals, accounts, taxes and clears default account assignments on partners, product categories, products and stock locations (models/model.py:216-291).
- Also resets sequence counters for the areas cleared (models/model.py:31-40,192-212) and can recompute complete names of product categories and stock locations (models/model.py:367-385).
- The screen itself warns that data is deleted directly from database tables, is not reversible (views/view.xml:11-16). Each button asks a generic confirmation (views/view.xml, confirm attributes).

## 2. Attachment to CORE
- Depends on base only (manifest:11). Extends core res.config.settings (a transient model) with many action methods (models/model.py:7-8), so the buttons live on a settings-model form (view record view_remove_data, views/view.xml:4-8; action views/view.xml:153-161).
- No core method is overridden; all methods are new (remove_data, remove_sales, remove_product, remove_product_attribute, remove_pos, remove_purchase, remove_expense, remove_mrp, remove_mrp_bom, remove_inventory, remove_account, remove_account_chart, remove_project, remove_quality, remove_quality_setting, remove_website, remove_message, remove_all, reset_cat_loc_name).
- ALTERS CORE CONTROL (by bypass, not by override): the deletion path issues table-level removals through the database cursor and commits immediately (models/model.py:24-28), thereby bypassing the ORM unlink rules, access rules, record rules, audit chatter, locked-period / hash-chain restrictions on posted accounting entries and reconciliation integrity that core enforces. This is a data-destruction utility rather than a modification of a core method.
- The account-clearing routine looks up a model named withholding.tax.cert and deletes certificates linked to the company's payments before clearing accounting records (models/model.py:177-186). That model belongs to the Thai withholding tax certificate add-on (l10n_th_withholding_tax_cert/models/withholding_tax_cert.py, see that module's file); it is wrapped in an exception catch so it is skipped if absent.

## 3. New objects, security, automation, external calls
- No new persistent models or fields. One view and one act_window on res.config.settings (views/view.xml:4,153).
- Menu "Remove Data" under Settings > Administration (base.menu_administration), restricted to the Settings / system administrators group base.group_system (views/view.xml:163-168). The underlying methods themselves have no group check in code; access control relies on the menu/view visibility and on the caller's rights (model.py has no check). Because res.config.settings methods are callable by users who can open the settings model, this is not independently verified.
- Company scoping: mostly none - the model deletions are not filtered by company (models/model.py:24). Only the payment-linked certificate removal (models/model.py:180) and the account sequence reset (models/model.py:193) filter by the current company, and the chart clearing filters default-value clean-up by company (models/model.py:236-238). The chart routine, however, searches all partners, all product categories, all products, all stock locations and writes to them (models/model.py:250-286).
- Automation: none (manual buttons only). External calls: none.

## 4. Odoo 19 compatibility
- The routine skips models not found in the registry (models/model.py:13-17) so absent models do not raise, but they are then silently not cleaned. Model names in its lists that are absent from the Community 19 tree (checked by scanning _name declarations under core addons; some are Enterprise-only): hr.expense.sheet, hr.payslip, hr.payslip.run, mrp.production.workcenter.line, mrp.production.product.line, sale.forecast, sale.forecast.indirect, stock.package_level, stock.quant.package (core now has stock.package: core:stock/models/stock_package.py:18), stock.inventory, stock.inventory.line, stock.valuation.layer, stock.production.lot (core now stock.lot: core:stock/models/stock_lot.py:25), account.invoice, account.tax.account.tag, account.account.account.tag, project.forecast, quality.check, quality.alert, quality.point, quality.reason, quality.tag, website.redirect. Pointers to the lists: models/model.py:91-338.
- Method _end_balance called on bank statements (models/model.py:85) is not defined anywhere in core 19 (grep of core returned nothing); it is inside an exception catch that only logs.
- Field names used in clearing account defaults that were not found in core 19 (grep): property_account_creditor_price_difference_categ, property_stock_account_input_categ_id, valuation_in_account_id (models/model.py:264-266,284-285). These writes are inside catch-all handlers.
- Uses self.pool.get (models/model.py:19) - registry access still exists in core 19 (core:orm/models.py uses self.pool). Context keys force_company and company_id (models/model.py:218) are legacy; not used by core 19 (grep of core:account/models found none).
- The module sets sequence counters via the sequence model 'number_next' (models/model.py:37,207); field exists in core sequences (not re-verified).
- Core res.partner property_account_receivable_id / payable exist as company-dependent fields (core:account/models/partner.py:545-550).

## 5. Custom-to-custom dependencies
- No manifest dependency. Soft runtime coupling to the model withholding.tax.cert from l10n_th_withholding_tax_cert (models/model.py:182).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether non-administrator users can invoke the methods (RPC-level access control on res.config.settings methods not verified).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether this utility is intended to be installed in production databases; the code has no environment guard.
- UNKNOWN - EVIDENCE INSUFFICIENT: referential-integrity outcome after partial deletions (errors are logged and swallowed, models/model.py:29-30).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether statements about Enterprise-only models above hold in the target build (only Community tree compared).
