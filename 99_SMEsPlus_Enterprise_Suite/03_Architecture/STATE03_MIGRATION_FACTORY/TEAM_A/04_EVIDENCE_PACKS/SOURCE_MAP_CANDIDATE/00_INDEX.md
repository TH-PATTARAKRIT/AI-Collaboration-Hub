# SOURCE MAP (CANDIDATE) — INDEX

> **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION.** **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION**: module list comes from the on-disk register whose sha256 differs from the recorded baseline; it is NOT a confirmed denominator and NOT Formal Coverage. Source revision `19.0.post20260921`. Not runtime proof. Community-core findings are CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET.

## Trace levels (counts are actual, not progress percentages)
| Level | Meaning | Modules |
|---|---|---|
| S1-STATIC-EXTRACT | Automated structural extraction (manifest, dependencies, objects, extension path, security/automation counts). Behavioral meaning **not** traced. | 65 |
| S2-CANDIDATE | S1 plus a delegated read-only trace note (business meaning, lifecycle, gating, handoffs, unknowns). Sub-agent authored; pointers existence-checked automatically (7996 of 8146 resolve to an existing file and in-range line); claims only partly spot-verified by the session. | 235 |

**"Source Map Complete" is NOT declared for any module.** These are candidate records; §5.1 items 8 (module-specific schema confirmation: not performed) and 9 (V-level: not assigned) remain open for every module.

## By register group (on-disk register; unverified baseline)
| Group | Modules | S2-CANDIDATE |
|---|---|---|
| COMM-G01 | 23 | 22 |
| COMM-G02 | 51 | 48 |
| COMM-G03 | 11 | 11 |
| COMM-G04 | 26 | 26 |
| COMM-G05 | 23 | 23 |
| COMM-G06 | 15 | 14 |
| COMM-G07 | 31 | 16 |
| COMM-G08 | 58 | 38 |
| COMM-G09 | 30 | 16 |
| COMM-G10 | 32 | 21 |

## S2-CANDIDATE modules (current)
`account`, `account_add_gln`, `account_check_printing`, `account_debit_note`, `account_edi`, `account_edi_proxy_client`, `account_edi_ubl_cii`, `account_fleet`, `account_payment`, `account_payment_interco`, `account_qr_code_emv`, `account_tax_python`, `account_test`, `account_update_tax_tags`, `analytic`, `api_doc`, `attachment_indexation`, `auth_ldap`, `auth_oauth`, `auth_passkey`, `auth_passkey_portal`, `auth_password_policy`, `auth_password_policy_portal`, `auth_password_policy_signup`, `auth_signup`, `auth_timeout`, `auth_totp`, `auth_totp_mail`, `auth_totp_portal`, `barcodes`, `barcodes_gs1_nomenclature`, `base`, `base_address_extended`, `base_automation`, `base_geolocalize`, `base_iban`, `base_import`, `base_import_module`, `base_install_request`, `base_setup`, `base_sparse_field`, `base_vat`, `board`, `bus`, `calendar_sms`, `cloud_storage`, `cloud_storage_azure`, `cloud_storage_google`, `cloud_storage_migration`, `contacts`, `crm`, `crm_iap_enrich`, `crm_iap_mine`, `crm_livechat`, `crm_mail_plugin`, `crm_sms`, `delivery`, `delivery_stock_picking_batch`, `event_booth`, `event_booth_sale`, `event_crm`, `event_crm_sale`, `event_product`, `event_sale`, `event_sms`, `gamification_sale_crm`, `google_address_autocomplete`, `google_gmail`, `hr_calendar`, `hr_fleet`, `hr_gamification`, `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_homeworking_calendar`, `hr_hourly_cost`, `hr_livechat`, `hr_presence`, `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_skills_slides`, `hr_timesheet_attendance`, `hr_work_entry_holidays`, `html_builder`, `html_editor`, `iap_crm`, `iap_mail`, `l10n_account_withholding_tax`, `l10n_th`, `link_tracker`, `loyalty`, `mail_bot`, `mail_bot_hr`, `mail_plugin`, `maintenance`, `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_product_expiry`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`, `mrp_subcontracting_repair`, `onboarding`, `partnership`, `payment`, `payment_custom`, `phone_validation`, `portal`, `portal_rating`, `privacy_lookup`, `product`, `product_email_template`, `product_expiry`, `product_margin`, `product_matrix`, `project`, `project_account`, `project_hr_expense`, `project_hr_skills`, `project_mail_plugin`, `project_mrp`, `project_mrp_account`, `project_mrp_sale`, `project_mrp_stock_landed_costs`, `project_purchase`, `project_purchase_stock`, `project_sale_expense`, `project_sms`, `project_stock`, `project_stock_account`, `project_stock_landed_costs`, `project_timesheet_holidays`, `purchase`, `purchase_edi_ubl_bis3`, `purchase_mrp`, `purchase_product_matrix`, `purchase_repair`, `purchase_requisition`, `purchase_requisition_sale`, `purchase_requisition_stock`, `purchase_stock`, `rating`, `repair`, `resource`, `resource_mail`, `rpc`, `sale`, `sale_crm`, `sale_edi_ubl`, `sale_expense`, `sale_expense_margin`, `sale_gelato`, `sale_gelato_stock`, `sale_loyalty_delivery`, `sale_management`, `sale_margin`, `sale_mrp`, `sale_mrp_margin`, `sale_product_matrix`, `sale_project_stock`, `sale_project_stock_account`, `sale_purchase`, `sale_purchase_project`, `sale_purchase_stock`, `sale_service`, `sale_sms`, `sale_stock`, `sale_stock_margin`, `sale_stock_product_expiry`, `sale_timesheet`, `sale_timesheet_margin`, `sales_team`, `sms`, `sms_twilio`, `snailmail`, `snailmail_account`, `social_media`, `spreadsheet_account`, `spreadsheet_dashboard`, `spreadsheet_dashboard_account`, `spreadsheet_dashboard_im_livechat`, `spreadsheet_dashboard_sale`, `spreadsheet_dashboard_stock_account`, `stock`, `stock_account`, `stock_delivery`, `stock_dropshipping`, `stock_fleet`, `stock_landed_costs`, `stock_maintenance`, `stock_picking_batch`, `stock_sms`, `survey_crm`, `theme_anelusia`, `theme_artists`, `theme_avantgarde`, `theme_aviato`, `theme_beauty`, `theme_bewise`, `theme_bistro`, `theme_bookstore`, `theme_buzzy`, `theme_clean`, `theme_cobalt`, `theme_common`, `theme_default`, `theme_enark`, `theme_graphene`, `theme_kea`, `theme_kiddo`, `theme_loftspace`, `theme_monglia`, `theme_nano`, `theme_notes`, `theme_odoo_experts`, `theme_orchid`, `theme_paptic`, `theme_real_estate`, `theme_treehouse`, `theme_vehicle`, `theme_yes`, `theme_zap`, `uom`, `web_hierarchy`, `web_unsplash`, `website_cf_turnstile`, `website_crm_iap_reveal`, `website_links`, `website_mail`, `website_mail_group`, `website_partner`, `website_sms`

## Notes
- Raw structural extracts, sub-agent trace files and tooling are kept in a restricted local folder (not committed).
- Files: `MODULE_<technical_name>.md` (one per module).
- Sub-agent provenance and limitations: see the Delta Handoff, Round 3.
