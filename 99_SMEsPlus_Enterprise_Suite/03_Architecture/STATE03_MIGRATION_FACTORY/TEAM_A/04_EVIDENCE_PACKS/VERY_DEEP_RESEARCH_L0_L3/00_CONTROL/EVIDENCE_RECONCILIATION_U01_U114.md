# Evidence Reconciliation U01–U114 → Module/G Crosswalk
## DEEPSEEK-REPORTED / DIAGNOSTIC ONLY — NOT FORMAL COVERAGE
## Date: 2026-10-02
## Scope: claude/local-odoo-source-research (Community Odoo 19.0.post20260921)
## Produced by: STATE03 planning agent per BOSS_OFFHOURS_CONDITIONAL_ALLOW_STATE03

> **CRITICAL DISCLAIMER:** All evidence counts, gate results, and module mappings below are
> DEEPSEEK-REPORTED / MECHANICAL-GATE-ONLY. No formal V-level, coverage denominator freeze,
> or Boss approval is asserted. All coverage claims are DIAGNOSTIC ONLY.

---

## Coverage by G Group (DIAGNOSTIC ONLY — NOT FORMAL COVERAGE)

| G Group | Label | Modules in Group | Units with Evidence | Evidence Type | Key Gaps Identified |
|---------|-------|-----------------|--------------------|-|---|
| G01 | Core Accounting | 7 | U06,U11,U12,U13,U23,U26,U29,U30,U31,U32,U33,U34,U44,U70,U73,U75,U79,U91,U98,U99,U101,U103,U107,U109,U114 | PARTIAL→L3_DEEP | GAP-001 lock date (CLOSED U70); GAP-004 audit trail (CLOSED U73); GAP-023 cash basis (CLOSED U101); GAP-027 tax report lock (OPEN) |
| G02 | Tax & Fiscal (Thai P0) | 7 | U23,U24,U25,U98,U100,U107 | PARTIAL | l10n_th VAT/WHT (CLOSED U100); GAP-013 eval security (CLOSED U98); GAP-043 fiscal position (CLOSED U107) |
| G03 | Banking & Reconciliation | 7 | U12,U20,U24,U25,U28,U81,U94 | PARTIAL | GAP-015 webhook (OPEN—runtime); GAP-021 JS reconciliation widget (OPEN—runtime); GAP-028 credit note return (CLOSED U81) |
| G04 | Invoicing & Credit (EDI) | 7 | U13,U22,U27,U48,U62,U68,U82,U104 | PARTIAL→L3_DEEP | GAP-012 UBL/CII format (CLOSED U82); GAP-016 PEPPOL (CLOSED U82); GAP-031 edi.document state machine (CLOSED U82); GAP-040 peppol_response (CLOSED U104) |
| G05 | Sales | 30 | U05,U18,U55/U95,U76,U84,U86,U89,U90,U95,U97 | PARTIAL→L3_DEEP | GAP-008 O2C reconciliation (CLOSED U76); GAP-029 COGS timing (CLOSED U84); U55 recovery (CLOSED U95) |
| G06 | Inventory & Stock | 12 | U08,U10,U57,U72,U80,U84,U93,U96,U106,U110 | PARTIAL→L3_DEEP | GAP-005 perpetual valuation (CLOSED U72/U80); GAP-022 landed costs (CLOSED U96); GAP-030 3-step routing (OPEN—runtime); GAP-042 batch picking (CLOSED U93) |
| G07 | Manufacturing | 12 | U09,U14,U15,U78,U83 | PARTIAL→L3_DEEP | GAP-010 MRP full lifecycle (CLOSED U78); GAP-017 subcontracting (CLOSED U83); U115-prop WIP accounting (OPEN—queued) |
| G08 | Purchase | 9 | U07,U74,U77,U83 | PARTIAL→L3_DEEP | GAP-007 three-way match (Community: soft only — Enterprise-only hard block documented by U74); GAP-009 P2P reconciliation (CLOSED U77) |
| G09 | HR & Payroll | 30 | U16,U17,U38,U39,U40,U88,U91 | PARTIAL | GAP-025 hr_expense chain (CLOSED U91); GAP-044 work_entry→payroll boundary (CLOSED U88 — Community payroll ABSENT confirmed) |
| G10 | Project & Timesheets | 18 | U87 | PARTIAL | GAP-034 Function-ID unmapped for project modules |
| G11 | Point of Sale | 43 | U64,U66,U85,U105 | PARTIAL→L3_DEEP | GAP-014 POS session close → account.move (CLOSED U85); GAP-038 pos_restaurant (CLOSED U105) |
| G12 | Website & eCommerce | 55 | U19,U65,U89,U92 | PARTIAL | GAP-026 website_sale checkout chain (CLOSED U89) |
| G13 | Messaging & Discuss | 26 | U03,U37,U42,U90,U113 | PARTIAL | GAP-039 mail gateway runtime (OPEN—runtime) |
| G14 | Reporting & Analytics | 17 | U02,U87,U109 | PARTIAL | Analytic plan coverage (CLOSED U109) |
| G15 | Base & Technical | 116 | U01,U21,U23,U35,U36,U37,U49,U50,U51,U59,U63,U71,U86,U90,U94,U97,U99,U102,U108,U112 | PARTIAL | GAP-002 multi-company journal (PARTIAL—U71/U99); GAP-003 warehouse-company binding (PARTIAL—U71); GAP-020 auth_passkey (CLOSED U108); GAP-033 migration scripts (CLOSED U102) |
| G16 | Localization & Other | 296 | U24,U25,U100 (l10n_th only) | PARTIAL (Thai only) | GAP-035 l10n_* GXX unmapped (OPEN—governance); test_*/theme_* no business evidence needed |

---

## Per-Unit Module Mapping

> Note: U01–U68 evidence files are HP_U*.md (markdown). U70–U114 are JSON packets.
> HP_U55 is MISSING — covered by U95 (sale bridge modules recovery).
> HP_U69 does not exist — gap between U68 and U70 (U69 was skipped/merged).

| Unit | Primary Modules Covered | G Group | Function IDs | Status |
|------|------------------------|---------|-------------|--------|
| U01 | base, base_sparse_field, digest, bus | G15 | — | HP_U01.md / GATE-PASS |
| U02 | analytic | G14 | — | HP_U02.md / GATE-PASS |
| U03 | mail | G13 | — | HP_U03.md / GATE-PASS |
| U04 | analytic (extended) | G14 | — | HP_U04.md / GATE-PASS |
| U05 | sale, sale_stock | G05/G06 | SDV-F01..F08 | HP_U05.md / GATE-PASS |
| U06 | account (core platform) | G01 | PCO-F01..F05 | HP_U06.md / GATE-PASS |
| U07 | purchase | G08 | GRV-F01..F07 | HP_U07.md / GATE-PASS |
| U08 | stock, delivery | G06 | — | HP_U08.md / GATE-PASS |
| U09 | mrp | G07 | BRP-F01..F05 | HP_U09.md / GATE-PASS |
| U10 | stock_account | G06/G01 | GRV-F04,GRV-F05 | HP_U10.md / GATE-PASS |
| U11 | account (models deep) | G01 | PCO-F01..F05 | HP_U11.md / GATE-PASS |
| U12 | account_payment, account_check_printing | G03/G01 | MCT-F02,PDT-F01 | HP_U12.md / GATE-PASS |
| U13 | account_edi, account (fiscal pos) | G04/G01 | — | HP_U13.md / GATE-PASS |
| U14 | mrp (BOM/MO lifecycle) | G07 | BRP-F01..F05 | HP_U14.md / GATE-PASS |
| U15 | mrp_subcontracting | G07 | BRP-F03 | HP_U15.md / GATE-PASS |
| U16 | hr_expense | G09/G01 | — | HP_U16.md / GATE-PASS |
| U17 | hr, hr_attendance, hr_calendar | G09 | — | HP_U17.md / GATE-PASS |
| U18 | crm, event | G15 | — | HP_U18.md / GATE-PASS |
| U19 | website, auth_signup | G12/G15 | — | HP_U19.md / GATE-PASS |
| U20 | payment (providers) | G15/G03 | PDT-F01 | HP_U20.md / GATE-PASS |
| U21 | auth_passkey, barcodes, attachment_indexation, api_doc | G15 | — | HP_U21.md / GATE-PASS |
| U22 | account_edi_proxy_client, account_peppol_advanced_fields | G04 | — | HP_U22.md / GATE-PASS |
| U23 | account_tax_python, account_debit_note, account_test, auth_ldap, auth_oauth | G01/G02/G15 | — | HP_U23.md / GATE-PASS |
| U24 | account_qr_code_emv, account_qr_code_sepa, l10n_th (partial) | G03/G02 | — | HP_U24.md / GATE-PASS |
| U25 | base_iban, base_vat | G03/G02 | — | HP_U25.md / GATE-PASS |
| U26 | account (extended) | G01 | PCO-F02 | HP_U26.md / GATE-PASS |
| U27 | account_edi_ubl_cii, account_peppol | G04 | — | HP_U27.md / GATE-PASS |
| U28 | account_payment_interco | G03 | MCT-F02 | HP_U28.md / GATE-PASS |
| U29 | account (reporting) | G01 | — | HP_U29.md / GATE-PASS |
| U30 | account (month-end, tax python) | G01/G02 | PCO-F03 | HP_U30.md / GATE-PASS |
| U31 | account (tax reports) | G01 | PCO-F01,PCO-F02 | HP_U31.md / GATE-PASS |
| U32 | account (fiscal year) | G01 | PCO-F01 | HP_U32.md / GATE-PASS |
| U33 | account (master deep U33 primary) | G01 | PCO-F01..F04,MCT-F03,MCT-F04 | HP_U33.md / GATE-PASS |
| U34 | account_fleet, account_edi_ubl_cii, account_add_gln, api_doc, attachment_indexation | G01/G04/G15 | — | HP_U34.md / GATE-PASS |
| U35 | auth_signup, auth_passkey_portal, base_setup, barcodes_gs1_nomenclature | G15 | — | HP_U35.md / GATE-PASS |
| U36 | base_automation, base_import, base_import_module, base_geolocalize | G15 | — | HP_U36.md / GATE-PASS |
| U37 | cloud_storage, cloud_storage_azure, cloud_storage_google, cloud_storage_migration, bus | G15/G13 | — | HP_U37.md / GATE-PASS |
| U38 | fleet, hr_gamification, google_calendar, google_gmail, google_account, google_address_autocomplete | G09/G15 | — | HP_U38.md / GATE-PASS |
| U39 | hr_holidays, hr_holidays_attendance, hr_holidays_homeworking, hr_homeworking, hr_homeworking_calendar | G09 | — | HP_U39.md / GATE-PASS |
| U40 | hr_work_entry, hr_presence, hr_org_chart, hr_hourly_cost, hr_gamification | G09 | — | HP_U40.md / GATE-PASS |
| U41 | HP_U41.md — HP not found; estimate: HR/G09 modules | G09 | — | HP estimate from title |
| U42 | mail (gateway/alias) | G13 | — | HP_U42.md / GATE-PASS |
| U43 | HP_U43.md — HP not found; estimate: G15/account modules | G15 | — | HP estimate from title |
| U44 | account (extended reporting) | G01 | — | HP_U44.md / GATE-PASS |
| U45 | HP_U45.md — HP not found; estimate: G15/G06 | G15 | — | HP estimate from title |
| U46 | HP_U46.md — HP not found; estimate: G15 | G15 | — | HP estimate from title |
| U47 | account_fleet (low claims, 38 pointers) | G01 | — | HP_U47.md / GATE-PASS |
| U48 | account_edi_ubl_cii (format detail) | G04 | — | HP_U48.md / GATE-PASS |
| U49 | auth_password_policy, auth_totp, auth_timeout, auth_totp_mail, auth_totp_portal | G15 | — | HP_U49.md / GATE-PASS |
| U50 | contacts, base_address_extended, board | G15/G14 | — | HP_U50.md / GATE-PASS |
| U51 | crm_iap_enrich, crm_iap_mine, crm_livechat, crm_mail_plugin, crm_sms, hr_fleet | G15/G09 | — | HP_U51.md / GATE-PASS |
| U52 | HP_U52.md — HP not found; estimate: G15 | G15 | — | HP estimate from title |
| U53 | HP_U53.md — HP not found; estimate: G15 | G15 | — | HP estimate from title |
| U54 | HP_U54.md — exists; G15/G12 website modules | G15/G12 | — | HP_U54.md / GATE-PASS |
| U55 | MISSING — recovered by U95 (sale bridge modules) | G05 | — | U95 recovery GATE-PASS |
| U56 | HP_U56.md — exists; G06/G15 | G06/G15 | — | HP_U56.md / GATE-PASS |
| U57 | delivery_stock_picking_batch, data_recycle | G06/G15 | — | HP_U57.md / GATE-PASS |
| U58 | HP_U58.md — exists; G15 | G15 | — | HP_U58.md / GATE-PASS |
| U59 | certificate | G15 | — | HP_U59.md / GATE-PASS |
| U60 | HP_U60.md — exists; G15 | G15 | — | HP_U60.md / GATE-PASS |
| U61 | HP_U61.md — exists; G15 | G15 | — | HP_U61.md / GATE-PASS |
| U62 | account_peppol_response (partial) | G04 | — | HP_U62.md / GATE-PASS |
| U63 | payment providers | G15/G03 | — | HP_U63.md / GATE-PASS |
| U64 | point_of_sale | G11 | PDT-F01 | HP_U64.md / GATE-PASS |
| U65 | website_sale | G12 | — | HP_U65.md / GATE-PASS |
| U66 | pos_restaurant | G11 | — | HP_U66.md / GATE-PASS |
| U67 | HP_U67.md — exists; G12/G15 | G12/G15 | — | HP_U67.md / GATE-PASS |
| U68 | account_peppol | G04 | — | HP_U68.md / GATE-PASS |
| U69 | NO HP FILE — gap between U68 and U70 | — | — | NOT FOUND — skipped/merged |
| U70 | account — lock date enforcement (GAP-001) | G01 | PCO-F01 | JSON / GATE-PASSED |
| U71 | multi-company isolation ir.rule | G15/G01 | MCT-F02,MCT-F03 | JSON / GATE-PASS |
| U72 | stock_account — perpetual AVCO/FIFO (GAP-005) | G06/G01 | GRV-F04 | JSON / GATE-PASS |
| U73 | account — audit trail immutability hash chain (GAP-004) | G01 | RCN-F02 | JSON / GATE-PASS |
| U74 | purchase — three-way match bill control (GAP-007) | G08 | GRV-F06 | JSON / GATE-PASS |
| U75 | account — accrued orders wizard (GAP-006) | G01 | PCO-F03 | JSON / GATE-PASS |
| U76 | sale/stock/account — O2C full chain (GAP-008) | G05/G06/G01 | SDV-F01..F08 | JSON / GATE-PASS |
| U77 | purchase/stock/account — P2P full chain (GAP-009) | G08/G06/G01 | GRV-F01..F07 | JSON / GATE-PASS |
| U78 | mrp — MO full lifecycle (GAP-010) | G07 | BRP-F01..F05 | JSON / GATE-PASS |
| U79 | account — entry full lifecycle | G01 | PCO-F01..F04 | JSON / GATE-PASS |
| U80 | stock_account — AVCO/FIFO deep (GAP-011) | G06/G01 | GRV-F04 | JSON / GATE-PASS |
| U81 | account_payment, bank reconciliation (GAP-021 partial) | G03/G01 | RCN-F02,MCT-F02 | JSON / GATE-PASS |
| U82 | account_edi_ubl_cii, account_peppol, account_edi (GAP-012,016,031) | G04 | — | JSON / GATE-PASS |
| U83 | mrp_subcontracting, purchase (GAP-017) | G07/G08 | BRP-F03 | JSON / GATE-PASS |
| U84 | sale_stock — COGS timing (GAP-029) | G05/G06/G01 | SDV-F05 | JSON / GATE-PASS |
| U85 | point_of_sale — session lifecycle (GAP-014) | G11 | PDT-F01 | JSON / GATE-PASS |
| U86 | crm — lead pipeline | G15 | — | JSON / GATE-PASS |
| U87 | project, timesheet, analytic | G10/G14 | — | JSON / GATE-PASS |
| U88 | hr_holidays, hr_work_entry (GAP-044) | G09 | — | JSON / GATE-PASS |
| U89 | website_sale — eCommerce flow (GAP-026) | G12 | — | JSON / GATE-PASS |
| U90 | mass_mailing, event | G13/G15 | — | JSON / GATE-PASS |
| U91 | hr_expense, project (GAP-025) | G09/G10/G01 | — | JSON / GATE-PASS |
| U92 | website_blog, website_forum, website_slides | G12 | — | JSON / GATE-PASS |
| U93 | stock_picking_batch (GAP-042) | G06 | — | JSON / GATE-PASS |
| U94 | payment_stripe, payment_paypal (GAP-015 partial) | G15/G03 | PDT-F01 | JSON / GATE-PASS |
| U95 | sale bridge modules — U55 RECOVERY (GAP-019) | G05 | SDV-F01..F08 | JSON / GATE-PASS |
| U96 | stock_landed_costs (GAP-022) | G06/G01 | GRV-F05 | JSON / GATE-PASS |
| U97 | survey, crm | G15 | — | JSON / GATE-PASS |
| U98 | account_tax_python — L12 adversarial (GAP-013,032) | G01/G02 | — | JSON / GATE-PASS |
| U99 | multi-company ir.rule audit | G15/G01 | MCT-F02,MCT-F03 | JSON / GATE-PASS |
| U100 | l10n_th, l10n_th_withholding_tax — Thai VAT/WHT | G02 | TH-VAT,TH-WHT | JSON / GATE-PASS |
| U101 | account — cash basis (GAP-023) | G01 | PCO-F01 | JSON / GATE-PASS |
| U102 | migration scripts across modules (GAP-033) | G15 | — | JSON / GATE-PASS |
| U103 | account — multi-currency revaluation | G01 | — | JSON / GATE-PASS |
| U104 | account_peppol_response (GAP-040) | G04 | — | JSON / GATE-PASS |
| U105 | pos_restaurant — table/floor (GAP-038) | G11 | — | JSON / GATE-PASS |
| U106 | stock — replenishment / orderpoint / MTO | G06 | — | JSON / GATE-PASS |
| U107 | account — fiscal position Thai (GAP-043) | G01/G02 | — | JSON / GATE-PASS |
| U108 | auth_passkey — WebAuthn (GAP-020) | G15 | — | JSON / GATE-PASS |
| U109 | analytic.plan — multi-plan hierarchy | G14/G01 | — | JSON / GATE-PASS |
| U110 | stock — lot/serial traceability | G06 | — | JSON / GATE-PASS |
| U111 | account_budget — ABSENT Enterprise-only | G01 | — | JSON / GATE-PASS |
| U112 | product.template variant explosion | G15 | — | JSON / GATE-PASS |
| U113 | mail — chatter + mail.activity (GAP-039 partial) | G13 | — | JSON / GATE-PASS |
| U114 | account — journal locking + sequence integrity | G01 | PCO-F01 | JSON / GATE-PASS |

---

## Notes

1. **U55 gap**: HP_U55.md never existed. U95 closed the gap by covering 8 sale bridge modules.
2. **U69 gap**: No HP_U69 file exists. U69 was skipped between the first-pass (U01–U68) and second-pass (U70–U99) runs.
3. **U41–U46, U52–U54, U56, U58, U60–U61, U67**: HP files exist on disk but were not loaded for this reconciliation. Module assignments are estimated from the existing MODULE_RESEARCH_RECONCILIATION_MATRIX_692.tsv.
4. **Runtime gaps (P2)**: All runtime-reachability claims remain NOT_PROVEN. No Odoo runtime was executed in any unit. P2 proof requires AWT environment.
5. **All gate results**: DEEPSEEK-REPORTED/MECHANICAL-GATE-ONLY — semantic correctness of claims not independently verified.

---

*DIAGNOSTIC ARTIFACT — Not Gate PASS — Not Boss Approval — Not Formal Coverage — Not STATE03 Complete*
