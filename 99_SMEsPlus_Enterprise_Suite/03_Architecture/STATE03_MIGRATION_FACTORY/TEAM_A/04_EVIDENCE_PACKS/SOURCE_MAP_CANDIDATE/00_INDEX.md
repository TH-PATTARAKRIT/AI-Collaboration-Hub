# SOURCE MAP (CANDIDATE) — INDEX

> **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION.** **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION**: module list comes from the on-disk register whose sha256 differs from the recorded baseline; it is NOT a confirmed denominator and NOT Formal Coverage. Source revision `19.0.post20260921`. Not runtime proof. Community-core findings are CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET.

## Trace levels (counts are actual, not progress percentages)
| Level | Meaning | Modules |
|---|---|---|
| S1-STATIC-EXTRACT | Automated structural extraction (manifest, dependencies, objects, extension path, security/automation counts). Behavioral meaning **not** traced. | 234 |
| S2-CANDIDATE | S1 plus a delegated read-only trace note (business meaning, lifecycle, gating, handoffs, unknowns). Sub-agent authored; pointers existence-checked automatically (3094 of 3123 resolve to an existing file and in-range line); claims only partly spot-verified by the session. | 66 |

**"Source Map Complete" is NOT declared for any module.** These are candidate records; §5.1 items 8 (module-specific schema confirmation: not performed) and 9 (V-level: not assigned) remain open for every module.

## By register group (on-disk register; unverified baseline)
| Group | Modules | S2-CANDIDATE |
|---|---|---|
| COMM-G01 | 23 | 8 |
| COMM-G02 | 51 | 8 |
| COMM-G03 | 11 | 7 |
| COMM-G04 | 26 | 23 |
| COMM-G05 | 23 | 19 |
| COMM-G06 | 15 | 1 |
| COMM-G07 | 31 | 0 |
| COMM-G08 | 58 | 0 |
| COMM-G09 | 30 | 0 |
| COMM-G10 | 32 | 0 |

## S2-CANDIDATE modules (current)
`account`, `account_add_gln`, `account_check_printing`, `account_debit_note`, `account_edi`, `account_edi_proxy_client`, `account_edi_ubl_cii`, `account_fleet`, `account_payment`, `account_qr_code_emv`, `account_tax_python`, `account_test`, `account_update_tax_tags`, `analytic`, `auth_passkey_portal`, `auth_password_policy_portal`, `auth_password_policy_signup`, `auth_signup`, `auth_timeout`, `auth_totp_portal`, `barcodes`, `barcodes_gs1_nomenclature`, `base_geolocalize`, `base_iban`, `base_sparse_field`, `base_vat`, `contacts`, `crm_livechat`, `crm_mail_plugin`, `crm_sms`, `delivery_stock_picking_batch`, `l10n_account_withholding_tax`, `l10n_th`, `maintenance`, `mrp`, `mrp_account`, `mrp_landed_costs`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`, `mrp_subcontracting_repair`, `payment_custom`, `portal_rating`, `product`, `product_expiry`, `project_mrp_stock_landed_costs`, `project_stock_landed_costs`, `purchase`, `purchase_edi_ubl_bis3`, `purchase_product_matrix`, `purchase_repair`, `purchase_stock`, `resource_mail`, `sale`, `sale_stock`, `stock`, `stock_account`, `stock_delivery`, `stock_dropshipping`, `stock_landed_costs`, `stock_maintenance`, `stock_picking_batch`, `stock_sms`

## Notes
- Raw structural extracts, sub-agent trace files and tooling are kept in a restricted local folder (not committed).
- Files: `MODULE_<technical_name>.md` (one per module).
- Sub-agent provenance and limitations: see the Delta Handoff, Round 3.
