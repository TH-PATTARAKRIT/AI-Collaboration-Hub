# Source Map (candidate) — `account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account` |
| Display name | Invoicing |
| Manifest version | 1.4 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `203c744b32681795` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `onboarding`, `product`, `analytic`, `portal`, `digest`
- Direct dependents in 300-module list (29): `account_add_gln`, `account_check_printing`, `account_debit_note`, `account_edi`, `account_edi_proxy_client`, `account_edi_ubl_cii`, `account_fleet`, `account_payment`, `account_qr_code_emv`, `account_tax_python`, `account_test`, `account_update_tax_tags` … (+17)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (129): `account_peppol_advanced_fields`, `account_qr_code_sepa`, `l10n_ae`, `l10n_ar`, `l10n_at`, `l10n_au`, `l10n_bd`, `l10n_be`, `l10n_bf`, `l10n_bg`, `l10n_bh`, `l10n_bj` … (+117)
- Custom / third-party modules that declare a dependency (name — license only) (46): `dev_print_cheque` — no-license, `scgl_product_image` — no-license, `invoice_promptpay` — no-license, `cr_effective_date_entries` — AGPL-3, `print_payment_remittance_adviec` — no-license, `l10n_th_withholding_tax` — AGPL-3, `product_brand_sale` — AGPL-3, `account_invoice_refund_link` — AGPL-3, `full_summarize_bills` — no-license, `print_voucher_request` — no-license, `bh_parent_company` — LGPL-3, `l10n_th_withholding_tax_report` — AGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Invoices & Payments
- Inventory of user-facing artifacts (counts): menu items 53, views 147, window actions 61, server actions 12, reports 6, mail templates 7, scheduled jobs 2, wizards 18, web routes 9
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (55): `validate.account.move` (Validate Account Move); `account.autopost.bills.wizard` (Autopost Bills Wizard); `account.move.reversal` (Account Move Reversal); `account.move.send.wizard` (Account Move Send Wizard); `account.automatic.entry.wizard` (Create Automatic Entries); `account.payment.register` (Pay); `account.move.send.batch.wizard` (Account Move Send Batch Wizard); `account.merge.wizard` (Account merge wizard); `account.merge.wizard.line` (Account merge wizard line); `account.secure.entries.wizard` (Secure Journal Entries); `account.financial.year.op` (Opening Balance of Financial Year); `account.setup.bank.manual.config` (Bank setup manual config); `account.resequence.wizard` (Remake the sequence of Journal Entries.); `account.accrued.orders.wizard` (Accrued Orders Wizard); `account.code.mapping` (Mapping of account codes per company); `account.payment.term` (Payment Terms); `account.payment.term.line` (Payment Terms Line); `account.tax.group` (Tax Group); `account.tax` (Tax); `account.tax.repartition.line` (Tax Repartition Line); `account.move` (Journal Entry); `account.reconcile.model.line` (Rules for the reconciliation model); `account.reconcile.model` (Preset to create journal entries during a invoices and payments matching); `account.move.send` (Account Move Send); `account.incoterms` (Incoterms) … (+30)
- Objects extended from other modules (37): `base.partner.merge.automatic.wizard`, `base.document.layout`, `mail.composer.mixin`, `digest.digest`, `res.country.group`, `onboarding.onboarding.step`, `mail.thread`, `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin`, `product.catalog.mixin`, `ir.actions.report`, `res.company`, `analytic.mixin`, `ir.http`, `ir.attachment`, `account.analytic.account`, `res.partner`, `mail.alias.mixin.optional`, `mail.template`, `res.partner.bank`, `res.currency`, `kpi.provider`, `uom.uom`, `ir.module.module` … (+12)
- Company-dependent settings introduced: 20 field(s); company-consistency auto-check declared on 23 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account.move.reversal` ← Community: `l10n_br`, `l10n_es_edi_facturae`, `l10n_es_edi_tbai`, `l10n_es_edi_verifactu`, `l10n_gr_edi`, `l10n_hu_edi`, `l10n_latam_invoice_document`, `l10n_sa`, `l10n_tw_edi_ecpay`, `l10n_vn_edi_viettel` … (+1); open-license custom/third-party scanned: `account_invoice_refund_link`
- `account.move.send.wizard` ← Community: `account_edi_ubl_cii`, `account_peppol`, `l10n_dk_nemhandel`, `l10n_es_edi_facturae`, `l10n_fr_pdp`, `l10n_ke_edi_tremol`, `l10n_ro_edi`, `l10n_rs_edi`; open-license custom/third-party scanned: —
- `account.automatic.entry.wizard` ← Community: `account_fleet`; open-license custom/third-party scanned: —
- `account.payment.register` ← Community: `account_payment`, `hr_expense`, `l10n_account_withholding_tax`, `l10n_ar_withholding`, `l10n_latam_check`, `l10n_pl_bank_verification`; open-license custom/third-party scanned: `account_payment_multi_deduction`, `base_accounting_kit`, `l10n_th_withholding_tax`, `l10n_th_withholding_tax_multi`
- `account.move.send.batch.wizard` ← Community: `account_peppol`, `l10n_dk_nemhandel`, `snailmail_account`; open-license custom/third-party scanned: —
- `account.setup.bank.manual.config` ← Community: `l10n_ch`; open-license custom/third-party scanned: —
- `account.resequence.wizard` ← Community: `account_edi`, `l10n_es_edi_sii`, `l10n_lk_invoice`; open-license custom/third-party scanned: —
- `account.accrued.orders.wizard` ← Community: `sale_stock`; open-license custom/third-party scanned: —
- `account.tax.group` ← Community: `l10n_ar`, `l10n_ec`, `point_of_sale`; open-license custom/third-party scanned: —
- `account.tax` ← Community: `account_edi_ubl_cii`, `account_tax_python`, `hr_expense`, `l10n_account_withholding_tax`, `l10n_account_withholding_tax_pos`, `l10n_ar_withholding`, `l10n_be`, `l10n_br`, `l10n_cl`, `l10n_de` … (+33); open-license custom/third-party scanned: `l10n_th_withholding_tax`
- `account.move` ← Community: `account_debit_note`, `account_edi`, `account_edi_ubl_cii`, `account_fleet`, `account_payment`, `account_payment_interco`, `account_peppol`, `account_peppol_advanced_fields`, `account_peppol_response`, `event_booth_sale` … (+105); open-license custom/third-party scanned: `account_asset_management`, `account_credit_control`, `account_invoice_refund_link`, `base_accounting_kit`, `courier_type`, `l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `om_account_accountant` … (+9)
- `account.move.send` ← Community: `account_edi`, `account_edi_ubl_cii`, `account_peppol`, `l10n_ch`, `l10n_dk_nemhandel`, `l10n_es_edi_facturae`, `l10n_es_edi_sii`, `l10n_es_edi_tbai`, `l10n_es_edi_verifactu`, `l10n_fr_pdp` … (+18); open-license custom/third-party scanned: —
- `account.fiscal.position` ← Community: `l10n_ar`, `l10n_br`, `l10n_fr_pos_cert`, `l10n_gr_edi`, `l10n_it_edi_doi`, `point_of_sale`; open-license custom/third-party scanned: —
- `account.journal` ← Community: `account_check_printing`, `account_debit_note`, `account_edi`, `account_payment`, `account_peppol`, `l10n_ar`, `l10n_at`, `l10n_be`, `l10n_bg_ledger`, `l10n_br` … (+26); open-license custom/third-party scanned: `base_accounting_kit`, `smesplus_account`
- `account.move.line` ← Community: `account_fleet`, `hr_expense`, `l10n_ar`, `l10n_cl`, `l10n_es_edi_tbai`, `l10n_gcc_invoice`, `l10n_gr_edi`, `l10n_hr_edi`, `l10n_id_efaktur_coretax`, `l10n_in` … (+30); open-license custom/third-party scanned: `account_asset_management`, `account_financial_report`, `account_invoice_refund_link`, `accounting_pdf_reports`, `base_accounting_kit`, `l10n_th_withholding_tax`, `l10n_th_withholding_tax_multi`, `om_account_asset` … (+12)
- `account.payment.method` ← Community: `account_check_printing`, `account_payment`, `l10n_latam_check`; open-license custom/third-party scanned: `base_accounting_kit`
- `account.payment.method.line` ← Community: `account_payment`, `l10n_it_edi`; open-license custom/third-party scanned: —
- `account.account` ← Community: `l10n_de`, `l10n_dk`, `l10n_in`, `l10n_mx`, `l10n_pt`, `point_of_sale`, `spreadsheet_account`, `stock_account`; open-license custom/third-party scanned: `account_asset_management`, `account_credit_control`, `account_financial_report`, `base_accounting_kit`, `l10n_th_withholding_tax`, `scgl_account_coa`, `smesplus_account`
- `account.group` ← Community: —; open-license custom/third-party scanned: `account_financial_report`
- `account.payment` ← Community: `account_check_printing`, `account_payment`, `hr_expense`, `l10n_account_withholding_tax`, `l10n_ar_withholding`, `l10n_au`, `l10n_ch`, `l10n_in`, `l10n_latam_check`, `l10n_nz` … (+5); open-license custom/third-party scanned: `account_payment_multi_deduction`, `base_accounting_kit`, `l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`
- This module's own extension of other modules' objects: `base.partner.merge.automatic.wizard`, `base.document.layout`, `mail.composer.mixin`, `digest.digest`, `res.country.group`, `onboarding.onboarding.step`, `mail.thread`, `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin`, `product.catalog.mixin`, `ir.actions.report`, `res.company`, `analytic.mixin`, `ir.http`, `ir.attachment`, `account.analytic.account`, `res.partner`, `mail.alias.mixin.optional`, `mail.template`, `res.partner.bank`, `res.currency`, `kpi.provider`, `uom.uom`, `ir.module.module` … (+12)

## 6. Actions / states / validation / automation / security
- State fields found: `account.move` → ['draft', 'posted', 'cancel']; `account.payment` → ['draft', 'in_process', 'paid', 'canceled', 'rejected']; `account.lock_exception` → ['active', 'revoked', 'expired']; `account.invoice.report` → ['draft', 'posted', 'cancel']
- Validation: 66 declarative constraint method(s), 14 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Account: Post draft entries with auto_post enabled and accounting date up to today every 1 days; Send invoices automatically every 1 days
- Security: groups declared 11 (`base.default_user_group`, `group_delivery_invoice_address`, `group_account_readonly`, `group_account_invoice`, `group_account_basic`, `group_account_user` … (+5)); record rules 31 (of which company-scoped by text 18); access rows 125

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 57 of 58 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: `account` (Odoo 19 Community)

- Source revision: `19.0.post20260921`
- Module: `account` v1.4, LGPL-3, application=true (`account/__manifest__.py`; skeleton `/Users/admin/STATE03_RESTRICTED_LOCAL/sourcemap/account.json`).
- Declared dependencies: base_setup, onboarding, product, analytic, portal, digest (`account/__manifest__.py:17`).
- Method: source reading only, no execution. All pointers are relative to the addons root. `(TEST)` means the claim comes from a bundled test, not from production code.
- Lock-date findings were re-verified independently from `company.py`, `account_move.py`, `account_move_line.py` and `account_lock_exception.py` (pointers below are my own).

## 1. Capabilities by business area

Legend: CORE = always present once `account` is installed. COND = depends on a setting, group, journal type or company field. OPT = lives in another module or is only offered as a toggle.

### 1.1 Journal entries, invoices and bills (CORE)
- One document model carries all seven document kinds: general entry, customer invoice/credit note, vendor bill/credit note, sales receipt, purchase receipt (`account/models/account_move.py:143-152`). The credit-note pairing table is at `account_move.py:60-67`.
- A document type must match its journal type: purchase documents only in purchase journals, sales documents only in sales journals (`account_move.py:2849-2855`).
- Draft-to-posted checks are collected in one gate (`account_move.py:5569-5690`, see section 2).
- Reversal / credit-note wizard: creates a reversing document and, when cancel is needed (modify mode or plain entries and not auto-posted), reconciles it against the original (`account/wizard/account_move_reversal.py:110-135`; `account_move.py:5495-5540`).
- Recurring / scheduled posting: `auto_post` values no/at_date/monthly/quarterly/yearly (`account_move.py:294-303`); posting a recurring entry creates the next copy (`account_move.py:5712-5713`, `4816`).
- Quick-encode (fiduciary) mode, COND on `company.quick_edit_mode` (`account/models/company.py:246-251`): posting fails if the typed total differs from the computed total (`account_move.py:5590-5600`).
- Abnormal invoice warnings (unusual amount or date compared with the partner's history of 10-30 posted docs): computed at `account_move.py:2258-2340`. Blocking wizard on `action_post` is OFF by default (`account_move.py:6182-6197`, context flag defaults to "disabled").
- Duplicate-reference detection on bills, auto-post suppression when duplicates exist (`account_move.py:5925-5940`).
- Send & print with async cron (`account/models/account_move_send.py`, `account_move.py:6496`).
- Accrual entry wizard: builds a dated accrual on a general journal and an automatic reversal on a later date. Reversal date must be after the entry date; single company and single currency only (`account/wizard/accrued_orders.py:140-151, 378-392`). The orders come from sale/purchase via context (`accrued_orders.py:17-20, 36-42`). COND: only reachable from those apps.
- Automatic entry wizard (change period / change account) for posted, unreconciled lines of a single company (`account/wizard/account_automatic_entry_wizard.py:20, 137-161`).

### 1.2 Journals (CORE)
- Types: sale, purchase, cash, bank, credit card, general (`account/models/account_journal.py:106-112`).
- Default numbering options follow type: separate refund sequence for sale/purchase, separate payment sequence for bank/cash/credit (`account_journal.py:704-711`).
- Archive is blocked while draft entries exist (`account_journal.py:677-691`).
- Hash-secure switch per journal `restrict_mode_hash_table` (`account_journal.py:145-146`); it cannot be switched off once secured entries exist (`account_journal.py:786-793`).

### 1.3 Taxes and tax reports
- Tax computation kinds: group, fixed, percent, percent-tax-included (`account/models/account_tax.py:84-86`) (CORE).
- Tax names unique per company family, type, scope and country (`account_tax.py:232-259`).
- Repartition rules: exactly one base line each for invoice and refund; same line count and order; positive factors sum to 100 (`account_tax.py:552-594`).
- Group taxes: no nesting; child scope must match (`account_tax.py:596-611`).
- A used tax cannot be deleted, only archived (`account_tax.py:5130-5133`).
- Cash-basis tax (COND on `company.tax_exigibility`, `company.py:220`): transition account must allow reconciliation (`account_tax.py:267-275`); cash-basis entries are created when payments are matched (`account/models/account_partial_reconcile.py:534`).
- Country consistency: taxes on a document must fit the fiscal country or fiscal position country (`account_move.py:2857-2870`).
- Report definitions (`account.report`, lines, expressions) exist as data models (`account/models/account_report.py:44-46, 349-351, 579-581`). Rendering/closing screens are NOT in this module. The tax lock help text says the tax lock date is set "when the tax closing entry is posted" (`company.py:81-86`), but no closing routine exists in `account`; UNKNOWN — EVIDENCE INSUFFICIENT for who performs that step in Community.

### 1.4 Payments (CORE)
- Payment record with its own state and a linked journal entry (`account/models/account_payment.py:36-49`).
- Register-payment wizard: groups by partner/currency/bank, supports installments and early-payment discount, refuses blocked invoices and mixed inbound/outbound (`account/wizard/account_payment_register.py:266-286, 332-347, 934-990`).
- Outstanding account: in the Community configuration the payment always gets an outstanding account and a journal entry, because the "in payment" state is not offered (`account_payment.py:912-918`, `account_move.py:7367-7372`).
- Payment methods and method lines per journal (`account/models/account_payment_method.py:7-20, 95-150`).
- Outbound payments to a bank account need that bank account to be "trusted" when the method requires a bank account (`account_payment.py:1130-1142`; `account/models/res_partner_bank.py:279`; group `group_validate_bank_account`, `account/security/account_security.xml:101-104`).

### 1.5 Reconciliation (CORE engine, COND screens)
- Engine: `reconcile()` builds partial matches, creates a full-reconcile record when everything on the matched set balances, and creates exchange-difference entries when currencies differ (`account/models/account_move_line.py:2797-2999, 3088-3140, 3142-3144`).
- Eligibility rules for reconcile (`account_move_line.py:2651-2681`): not already reconciled, not from cancelled entries, same account, same company family, account must allow reconciliation (cash and credit-card types are also allowed).
- Matching numbers on lines: format rules (`account_move_line.py:1593-1610`); `I...` prefix means "pending import match" processed at post (`account_move_line.py:3157`, `account_move.py:5776`).
- Bank statement lines are entries: each line creates and immediately posts its own entry against a suspense account (`account/models/account_bank_statement_line.py:367-421`). The line is "reconciled" when the suspense residual is zero (`account_bank_statement_line.py:287-315`).
- Statement validity check: opening balance must equal the previous statement's real closing balance (`account/models/account_bank_statement.py:197-243`).
- Reconcile models (rules by label/amount/partner, trigger manual or automated) exist as data (`account/models/account_reconcile_model.py:94-165`). The interactive reconciliation widget is not found in `account/static/src/components`; UNKNOWN — EVIDENCE INSUFFICIENT for the Community screen that applies these rules.
- Undo statement-line reconciliation resets the line to its suspense form and deletes its payments (`account_bank_statement_line.py:460-478`).

### 1.6 Sequences, numbering, gaps (CORE)
- Number is assigned when the entry first needs a name after leaving draft (`account_move.py:952-969`).
- Start format by journal type: sale/bank/cash/credit use `CODE/YEAR/00000`; others `CODE/YEAR/MONTH/0000`; "R" prefix for refunds and "P" for payments when the journal has those options; staggered fiscal years use a two-year label (`account_move.py:4273-4311`).
- Reset period (never/year/year-range/month/year-range-month) is deduced from the previous number (`account/models/sequence_mixin.py:194-226`; range for fiscal year at `account_move.py:4313-4340`).
- Posted date must match the number's date pattern unless the check is skipped; error asks to clear the number or resequence (`sequence_mixin.py:156-181`; skip for non-posted and quick-edit at `account_move.py:4197-4199`).
- Journal-level override pattern for unusual formats: only accountant may change a non-conforming name (`account_move.py:3971-3974`).
- Gap tracking flag `made_sequence_gap` maintained on neighbours (`account_move.py:328, 5820-5910`).
- Resequence wizard is refused on journals with hash security (`account/wizard/account_resequence.py:155-159`).

### 1.7 Lock dates and lock exceptions (CORE)
- Five company dates: global (fiscal year), tax, sales, purchase, and hard (`account/models/company.py:57-70, 76-102`).
- Detail in sections 3.1 and 3.2.

### 1.8 Fiscal positions (CORE)
- Auto-apply by country / country group / zip / VAT-required (`account/models/partner.py:26-55, 112-140, 247-279`).
- Foreign-VAT positions require a country and, inside the home country, a state (`partner.py:118-139`); creating foreign taxes needs the accounting-manager role (`partner.py:296-300`).

### 1.9 Analytic distribution (CORE, needs `analytic` dependency)
- Distribution stored as JSON on each line (`account_move_line.py:438`).
- On posting, lines requiring 100 percent distribution (by applicability rules) block posting (`account_move_line.py:3188-3219`); analytic lines are created at post (`account_move_line.py:3221-3235`, `account_move.py:5709`).
- Posting is blocked if an archived analytic account is used (`account_move.py:5686-5691`).
- Default distribution rules: `account/models/account_analytic_distribution_model.py`; plan applicability: `account_analytic_plan.py:6-79`.
- Analytic accounting toggle in settings is COND (`account/models/res_config_settings.py:259-262`).

### 1.10 Currency (CORE)
- Per-document rate `invoice_currency_rate`, must be strictly positive for foreign-currency invoices (`account_move.py:537-543, 2872-2885`). Expected-rate fallback when invoice date empty (`account_move.py:5640-5647`).
- Decimal places of a currency cannot be reduced once used in entries (`account/models/res_currency.py:26-33`).
- Company currency cannot change once entries exist (`company.py` write, near `currency_id` check after line 750).
- Exchange gain/loss journal and accounts are company settings (`company.py:133-143`); missing accounts stop exchange-difference creation (`account_move_line.py:3110-3125`).
- Inactive currency blocks posting (`account_move.py:5665-5668`).

### 1.11 Cash rounding (COND on `group_cash_rounding`)
- Two strategies: adjust tax amount, or add a rounding line; profit/loss accounts (`account/models/account_cash_rounding.py:22-57`; setting `res_config_settings.py:80`; group `account_security.xml:86`).
- Rounding is a hash-relevant input (TEST) (`account/tests/test_account_inalterable_hash.py:290`).

### 1.12 Payment terms (CORE)
- Lines must include at least one percent line and the percent sum must be 100; early-payment discount must be positive with positive days (`account/models/account_payment_term.py:156-169`). Percent range 0-100 (`account_payment_term.py:343-347`). Terms in use cannot be deleted, only archived (`account_payment_term.py:261`).

### 1.13 Chart-of-accounts templates (CORE loader, localisation data OPT)
- Loader: `try_loading` -> `_load` (admin only) (`account/models/chart_template.py:140-257`). Only administrators can install (`chart_template.py:184`).
- Behaviour on load: if the company has no existing accounting (or demo requested) and the template differs, previous templated records and entries for that company are removed before loading (`chart_template.py:215-230`). Reloading the same template keeps existing data and only updates main configuration (`chart_template.py:265-290`).
- Community ships only the generic template (`account/models/template_generic_coa.py:8-40`; `account/data/template/`). Country templates live in `l10n_*` modules.

### 1.14 Secure / hash of entries (COND)
- See section 3.3.

### 1.15 Other
- Audit trail restriction (COND on `company.restrictive_audit_trail`): section 3.3.
- Storno accounting flag, mandatory for listed countries (`company.py:233-234, 451-458`; applied on reversal at `account_move.py:5529`).
- Partial purchase deductibility group auto-granted to the posting user when a bill has deductible below 100 (`account_move.py:5762-5764`).

## 2. Business objects and lifecycle

### 2.1 Journal entry states
States: draft, posted, cancel (`account_move.py:130-141`). Default draft. Direct creation in posted state is refused (`account_move.py:3894-3896`).

| Transition | Entry point | Gates (all must pass) |
|---|---|---|
| draft to posted | `action_post` (`account_move.py:6180-6200`); bulk with confirmation for future-dated or hash-journal docs (`account_move.py:6210-6236`); cron (`account_move.py:6460`) | Posting right: invoicing group or superuser (`5583-5584`). Per-invoice checks: quick total, active bank account, trusted own bank account, non-negative total, partner present, bill date present (`5586-5648`). Per-entry: still draft, has real lines, active journal, active currency, active accounts, accounts belong to company family (`5650-5680`). Archived analytic account (`5686-5691`). Required analytic distribution (`3188`). |
| Posting side effects | `_post` | If date is inside a violated lock, the accounting date is silently moved to the first open date (`5702-5706`, rule at `6795-6829`). Future-dated docs with soft posting become "auto-post at date" instead of posting (`5692-5698`). State set posted and `posted_before` true (`5756-5760`). Number assigned (`952-969`). Hash written when journal is secured (`4004-4006`). Customer/supplier rank raised (`5780-5795`). Zero-total invoices trigger paid hook (`5797-5799`). |
| posted to draft | `button_draft` (`6269-6283`) | Only posted/cancel source (`6270-6271`); not awaiting government cancellation request (`6272-6273`); not an exchange-difference entry, not a cash-basis entry (`6348-6371`); not hashed (`6372-6373`); global/sales/purchase/tax/hard lock check on old date (`3947-3956`) with exceptions honoured for soft locks. Next draft recurrence deleted (`6319-6342`). Analytic lines deleted (`6278`). Sale documents lose generated PDF attachment (`6296-6317`). |
| draft to cancel (or posted to cancel) | `button_cancel` (`6384-6394`) | Posted entries are first reset to draft (so all draft gates apply). Reconciliations removed, linked payments set to canceled, auto_post set to no. |
| delete | `unlink` (`4079-4090`) | Not allowed for posted lines (`account_move_line.py:1959-1966`). Non-last numbered entries need manager rights, quick-edit mode, or force flag (`4049-4066`). If company has restrictive audit trail, once-posted entries cannot be deleted, only cancelled (`4068-4077`). Hashed entries' lines cannot be deleted (`account_move_line.py:1982-1989`). Helper `_unlink_or_reverse` picks delete, cancel or reverse (`account_move.py:5551-5567`). |

Immutability of posted entries (`account_move.py:3946-3970`): date and name changes re-run lock checks; `invoice_line_ids, line_ids, invoice_date, date, partner_id, invoice_payment_term_id, currency_id, fiscal_position_id, invoice_cash_rounding_id` are blocked on posted entries unless a technical context flag is set. On lines: tax changes on posted lines blocked (`account_move_line.py:1849-1850`); balance/account/partner etc. checked against lock dates (`account_move_line.py:3485-3492`).

Balance rule: every create/write/unlink of entries or lines is wrapped by a balance check; unbalanced entry raises "The entry is not balanced" (`account_move.py:2782-2821`; wrapped at `3898`, `3981`, `account_move_line.py:1785, 1891, 2022, 2817`).

### 2.2 Payment (invoice) status
Values: not paid, in payment, paid, partial, reversed, blocked, legacy (`account_move.py:49-57`). Computed from matched lines (`account_move.py:1234-1326`).
- Community outcome: full settlement returns "paid" because the "in payment" state is a hook that only the Enterprise accounting app overrides (`account_move.py:7367-7372`; comment `account_payment.py:912-916`).
- Manual "blocked" flag is a toggle; cannot block a paid/in-payment invoice (`account_move.py:6398-6407`).
- A "paid/in payment" transition fires the paid hook, used by sale (`sale/models/account_move.py:135-146`).

### 2.3 Payment document states
States: draft, in_process, paid, canceled, rejected (`account_payment.py:36-49`).
- Post: draft to in_process; if outstanding account is a cash-type account, straight to paid (`account_payment.py:1144-1148`). Requires trusted recipient bank account for outbound bank-based methods (`account_payment.py:1130-1142`).
- In_process to paid: liquidity residual is zero or account is non-reconcilable, or all matched invoices are paid (`account_payment.py:454-470`).
- Paid back to in_process when its match is removed (`account_partial_reconcile.py:105-155`); in_process to paid when a partial matches the full amount (`account_partial_reconcile.py:157-192`).
- Validate / reject / cancel / draft actions at `account_payment.py:1150-1166`; cancel deletes draft entries or cancels posted ones (`1156-1162`).
- Guard: a state beyond draft/canceled with an outstanding account needs its entry (`account_payment.py:878-886`). Deleting a payment resets its entry to draft first (`account_payment.py:961-968`).

### 2.4 Reconciliation states
- Line level: unreconciled, partially matched (`P<n>` number), fully matched (number equals full-reconcile id), pending import match (`I...`) (`account_move_line.py:1593-1610`).
- Full reconcile is created only when the whole matched set nets to zero (`account_move_line.py:2931-2966`).
- Unreconcile (delete partials) also reverses cash-basis and exchange-difference entries; reversal date is moved after a violated lock (`account_partial_reconcile.py:105-155`, lock rule at `126-138`).
- Editing an already matched posted line's account/date/amounts breaks its reconciliation, except account change applied to all lines of the match together (`account_move_line.py:1858-1882`).
- Posted-line change refused if matched (helper `_check_reconciliation`, `account_move_line.py:1545-1550`).
- Statement line: unreconciled/reconciled flag from suspense residual (`account_bank_statement_line.py:287-315`).

## 3. Constraints, automation, security

### 3.1 Lock dates (independent verification)
- Fields: `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date` (soft) and `hard_lock_date` (`company.py:57-70, 76-102`).
- What each covers when checking an entry (`company.py:675-710`, `account_move.py:2823-2840`): global date applies to everything; sales date only to sales journals; purchase date only to purchase journals; tax date only to lines that affect the tax report (`account_move_line.py:1526-1543`); hard date always, no exceptions.
- Effective date per user: for each company in the parent chain the soft date is used, replaced by the earliest matching active exception if the user (or everyone) has one whose date is earlier than the company date (`company.py:607-640`). A date counts as violated only if it is on/before the company date AND on/before the exception-adjusted date (`company.py:656-673`).
- Hard date: max over parent companies (`company.py:442-449`); cannot be removed or moved earlier (`company.py:569-576`); setting it requires no draft entries on/before it (`company.py:578-596`). Any global or hard change requires no unreconciled bank statement lines on/before the max date (`company.py:597-605`). The docstring also mentions an "unhashed entries" check (`company.py:547-552`) but no such check exists in the function body, so it is not enforced there.
- Enforcement points: posting shifts the accounting date instead of failing (`account_move.py:5702-5706`); editing name/date of a posted entry, or leaving posted, or deleting non-zero posted lines, or changing protected line fields, raises an error (`account_move.py:3947-3956, 3998-4002`; `account_move_line.py:1852-1858, 1994-2003, 3485-3492`). Fiscal check bundle uses global+sales/purchase by journal type+hard, excludes tax date (`account_move.py:2823-2840`); tax check separate (`account_move_line.py:1526-1543`).
- Tests confirming: exception with a date not early enough is insufficient, exception on a different lock field is insufficient, hard lock ignores all exceptions and cannot be lowered/removed (TEST) (`account/tests/test_account_lock_exception.py:193-218, 274-336`).

### 3.2 Lock exceptions
- Model `account.lock_exception` (`account/models/account_lock_exception.py:8-9`). One exception changes exactly one soft field (`account_lock_exception.py:165-181`); hard lock has no exception field (selection lists four soft fields, `:57-64`).
- State computed: active / revoked (inactive) / expired (end time passed) (`account_lock_exception.py:105-113`). Exception with no end time never expires. No user means it applies to everyone (`:36-39`).
- Creation records the company's original lock date and posts a company chatter message (`account_lock_exception.py:184-216`).
- Cannot be duplicated (`:218-219`). Revoke needs accounting Administrator or superuser (`:234-244`).
- Access: everyone internal can read; Administrator can read and create; nobody can edit or delete (`account/security/ir.model.access.csv:18-19`).
- Audit view of what changed while an exception was active: `account_lock_exception.py:257-306`.

### 3.3 Hash, inalterability and audit trail
- Hash covers entry name, date, journal, company and, per line, name, debit, credit, account, partner (`account_move.py:4592-4599`; `account_move_line.py:3394-3400`). Version 4 is current (`account_move.py:43`).
- Automatic hashing on posting only for journals with `restrict_mode_hash_table` (`account_move.py:4004-4006, 4605-4623`). Retroactive: hashes all unhashed earlier posted entries of the same numbering chain back to the last hashed one (`account_move.py:4639-4718`).
- Refuses when the chain has a numbering gap or has unreconciled bank statement lines (`account_move.py:4750-4766`) (TEST: `account/tests/test_account_inalterable_hash.py:348-396`).
- Once hashed: name/date/journal/company/hash cannot be edited (`account_move.py:3924-3930`); lines' fields likewise (`account_move_line.py:1826-1836`); cannot reset to draft (`account_move.py:6372-6373`); cannot delete lines (`account_move_line.py:1982-1989`); cannot merge partners used in hashed entries (`account/models/partner.py:1121`).
- On-demand securing wizard for any journal up to a date: `account/wizard/account_secure_entries_wizard.py:24-59, 260-269`. It grants the "inalterability features" group when journals without auto-hash are secured (`account_move.py:4634-4636`; group `account_security.xml:82-84`).
- Restrictive audit trail (company flag, `company.py:258-262`): once-posted entries cannot be deleted (`account_move.py:4068-4077`); attachments on those entries cannot be removed (`account/models/ir_attachment.py:22-61`); chat/log messages and tracking on them are protected (`account/models/mail_message.py:7-30`). A localisation may force it on (`company.py:263-266, 319-323, 347-349`; l10n_de overrides `l10n_de/models/res_company.py:32`).

### 3.4 Other blocking rules
- Payable/receivable lines: sales documents may not use payable accounts, and an account of receivable type must sit on a payment-term line (and the mirror rule for purchases) (`account_move_line.py:1507-1523`).
- Off-balance accounts: cannot mix with other account types, no taxes, not reconcilable (`account_move_line.py:1496-1505`).
- Payment-term and tax lines cannot be deleted by hand (`account_move_line.py:1968-1979`).
- Bank account rules on journals (`account_journal.py:586-604`); journal company cannot change once entries exist (`:597-604`).
- Partner delete blocked when used in accounting (`partner.py:806`). Partner merge wizard: `account/wizard/account_merge_wizard.py`.

### 3.5 Automation (crons)
- "Post draft entries with auto-post enabled and accounting date up to today": daily, first run at 02:00 next day (`account/data/service_cron.xml:3-11`). Posts in batches of 100; a failing batch falls back to one-by-one; on failure the entry gets a chatter note and auto-post is turned off (`account_move.py:6460-6494`).
- "Send invoices automatically": daily, run as OdooBot (`service_cron.xml:13-21`; `account_move.py:6496-6520`). Batch send is unavailable if this cron is archived (`account/wizard/account_move_send_batch_wizard.py:89-101`).
- Bill auto-post at import: needs company flag `autopost_bills` (default true, `company.py:269`), partner value "always" (partner values always/ask/never, default ask, `partner.py:610-616`), no abnormal-amount warning, no hash journal, no duplicates (`account_move.py:5925-5940`). "Ask" mode offers the wizard after 3 unmodified validations (`account_move.py:5942-5972`; `account/wizard/account_autopost_bills_wizard.py`).
- Payment reminders / follow-up: no cron in `account` (only a `no_followup` flag, `account_move.py:344, 2443`). UNKNOWN — EVIDENCE INSUFFICIENT for any reminder cron in Community.
- Digest emails: `account/data/digest_data.xml`, `account/models/digest.py` (COND on digest module usage).

### 3.6 Security groups
- Hierarchy documented at `account/security/account_security.xml:8-38`; groups defined at `:50-84`: readonly, invoice (label "Invoicing"), basic, user (full accounting), manager (Administrator; also given to OdooBot and admin at install, `:73-80`), secured, cash rounding, partial purchase deductibility, validate bank account.
- Invoicing group can create/edit/delete entries and lines, payments and reconciliation records; sees all entries (`ir.model.access.csv:38,40,98,101,114`; rules `account_security.xml:232-243, 284-297`).
- Administrator group alone has read on move by access list but inherits invoicing rights (`ir.model.access.csv:35-36`; `account_security.xml:73-80`).
- Portal users see only own posted invoices (not draft/cancel) (`account_security.xml:247-258`).
- Configuration models (journals, accounts, taxes, fiscal positions) are writable only by Administrator; everyone internal can read (`ir.model.access.csv:20-23, 55, 68-77`).
- Community review lock: "checked" entries and the "only accountant may change validated entries" rule resolve to "anyone" because the review-permission hook returns true (`account_move.py:7014-7016`, used at `3919-3921`; statement side `account_bank_statement_line.py:465-466`). The stricter rule is expected from the Enterprise app: UNKNOWN — EVIDENCE INSUFFICIENT.

### 3.7 Multi-company and branches
- Entry, line, payment, statement, tax analysis records: visible only for the user's active companies (`account_security.xml:128-137, 182-185, 194-203, 218-221`).
- Journals, taxes, fiscal positions, account groups: `parent_of` active companies, meaning branches see parent config (`account_security.xml:140-192`); accounts use `company_ids` (`:152-155`); payment terms can be shared (`:224-227`).
- Lock dates and exceptions are evaluated up the parent chain (`company.py:607-640`), and hard lock is the max over the chain (`company.py:442-449`) (TEST branch case: `test_account_lock_exception.py:99-165`).
- Reconciliation allowed only inside one company family (`account_move_line.py:2668-2672`). Posting refuses accounts from another family (`account_move.py:5674-5679`). Payment register refuses mixed companies/branches (`account_payment_register.py:976-979`).
- Chart template loading cascades to child companies (`chart_template.py:255-256`).

## 4. Handoffs (which module owns what)

| Counterpart | Owned by `account` | Owned by the other module |
|---|---|---|
| sale | Invoice document, posting, paid hook (`account_move.py:7359`), reversal | Down-payment lines, sales team, auto-reconcile invoice with payments from online transactions on post, "invoice paid" note on the order (`sale/models/account_move.py:24-35, 83-146`); accrual wizard consumer for sale orders (`accrued_orders.py:17-42`) |
| purchase | Bill document, autopost, duplicates | Purchase-order links on bills/lines, PO matching from references, bill-to-PO reconciliation (`purchase/models/account_invoice.py:16-113, 450-520`); called from `account_move.py:5919-5923` |
| stock_account | Posting engine, anglo-saxon flag `company.py:144` | Creates cost-of-goods lines just before super-post on customer invoices, deletes them on draft/cancel (`stock_account/models/account_move.py:29-66`); stock valuation entries |
| payment (via `account_payment`) | Payment model and states | Links payment to online transaction, creates transaction on post for tokens (`account_payment/models/account_payment.py:11-14, 124-150`); invoice-to-transaction link (`account_payment/models/account_move.py:16-33`) |
| l10n_* | Generic chart and hooks (`_get_invoice_in_payment_state`, `_is_user_able_to_review`, `_get_fields_to_detach`, `button_request_cancel` for government cancellation, `account_move.py:6378-6382`) | Country charts, tax data, e-invoice formats, forced audit trail (e.g. l10n_de) |
| hr_expense, point_of_sale, mrp_account, sale_project etc. | Entry/line base | Extra fields and posting hooks (see section 6) |

Enterprise-only pieces referenced but not present: dynamic reports, bank reconciliation widget, budget, batch payments, SEPA, Peppol are listed as settings toggles that install other apps (`account/models/res_config_settings.py:79-99`). What they do is UNKNOWN — EVIDENCE INSUFFICIENT from this source.

## 5. Configuration that changes outcomes
- Lock dates (five) and exceptions: change whether posting shifts a date, or an edit is refused (section 3.1).
- Journal: type, `restrict_mode_hash_table`, refund/payment sequence flags, sequence override pattern (`account_journal.py:145, 177-200`).
- Company: `restrictive_audit_trail` (`company.py:258`), `quick_edit_mode` (`:246`), `account_storno` (`:233`), `autopost_bills` (`:269`), `tax_exigibility` (`:220`), `tax_calculation_rounding_method` (`:129`), `account_price_include` (`:270-275`), fiscal year end day/month (`:74-75`, checked `:330-345`; changes number format `account_move.py:4273-4290`), exchange gain/loss journal/accounts (`:133-143`), cash-basis journal/base account (`:221`), opening entry date (`:167-169`).
- Partner: auto-post mode; ignore abnormal amount/date flags (`partner.py:610`, `account_move.py:2266, 2323, 2337`).
- Settings: cash rounding group, sale receipts toggle, storno, analytic toggle, module toggles (`res_config_settings.py:79-99`, `:259-262`).
- Tax: `price_include_override`, `include_base_amount`, `tax_exigibility` (`account_tax.py:142-165`).
- System parameters: `sequence.mixin.constraint_start_date` (bypass date/number alignment check, `sequence_mixin.py:158-162`); `account.product_name_similarity_threshold` default 0.9 (`account/data/ir_config_parameter_data.xml:4-6`).
- Context flags that alter behaviour (technical): `skip_readonly_check`, `force_delete`, `bypass_lock_check`, `disable_abnormal_invoice_detection` (`account_move.py:3961, 4062, 2826, 6183`).

## 6. Effective extension path (Community modules that inherit)
Method: scan of `_inherit` declarations across the addons root (tests/demo excluded). Names only; a match can be any class in the module.

- `account.move`: account, account_debit_note, account_edi, account_edi_ubl_cii, account_fleet, account_payment, account_payment_interco, account_peppol, account_peppol_advanced_fields, account_peppol_response, event_booth_sale, hr_expense, mrp_account, point_of_sale, pos_sale, product_email_template, purchase, purchase_edi_ubl_bis3, purchase_stock, sale, sale_expense, sale_project, sale_stock, sale_timesheet, snailmail_account, stock_account, stock_landed_costs, website_sale, plus l10n_* modules (ae, anz_ubl_pint, ar, ar_withholding, au, be, bg_ledger, br, ch, cl, cn, cz, de, dk_fik, dk_nemhandel, dk_nemhandel_response, dk_oioubl, ec, eg_edi_eta, es, es_edi_facturae, es_edi_sii, es_edi_tbai, es_edi_verifactu, es_edi_verifactu_pos, es_pos, fi, fr_account, fr_facturx_chorus_pro, fr_pdp, fr_pdp_pos, gcc_invoice, gr_edi, gr_edi_e_invoo, hr_edi, hu, hu_edi, hu_edi_receive, id, id_efaktur_coretax, in, in_edi, in_ewaybill, in_pos, in_purchase_stock, in_sale_stock, it, it_edi, it_edi_doi, it_stock_ddt, jo_edi, jo_edi_pos, jp_ubl_pint, ke, ke_edi_tremol, latam_check, latam_invoice_document, lk_invoice, mu_account, my_edi, my_ubl_pint, no, nz, pe, ph, pl, pl_edi, pl_edi_jst, ro_edi, rs, rs_edi, sa, sa_edi, sa_edi_pos, se, sg, sg_ubl_pint, si, sk, th, tr_nilvera_einvoice, tr_nilvera_einvoice_extended, tw_edi_ecpay, uy, vn, vn_edi_viettel, vn_edi_viettel_pos, zm_account).
- `account.move.line`: account, account_fleet, hr_expense, mrp_account, mrp_subcontracting_purchase, point_of_sale, pos_discount, pos_loyalty, pos_sale, project_sale_expense, purchase, purchase_stock, repair, sale, sale_expense, sale_expense_margin, sale_loyalty, sale_mrp, sale_project, sale_stock, sale_timesheet, stock_account, stock_landed_costs, plus l10n_ar, l10n_cl, l10n_es_edi_tbai, l10n_gcc_invoice, l10n_gr_edi, l10n_hr_edi, l10n_id_efaktur_coretax, l10n_in, l10n_in_edi, l10n_in_pos, l10n_latam_check, l10n_latam_invoice_document, l10n_mx, l10n_my_edi, l10n_sa_edi, l10n_tr, l10n_tr_nilvera_einvoice_extended, l10n_tw_edi_ecpay.
- `res.company` (accounting-relevant subset; the scan also lists many non-accounting modules such as hr*, mail, web, website, stock, mrp, resource, sms, lunch): account, account_check_printing, account_edi_proxy_client, account_payment_interco, account_peppol, account_peppol_response, base_vat, hr_expense, mrp_account, payment, point_of_sale, purchase, purchase_stock, sale, sale_management, sale_stock, stock_account, stock_landed_costs, website_sale, spreadsheet_account, partner_autocomplete, plus l10n_* (account_withholding_tax, ar, ar_withholding, au, br, ca, cl, cz, de, din5008, dk_nemhandel, ec, ee, eg_edi_eta, es*, eu_oss, fr, fr_account, fr_pdp, fr_pos_cert, gcc_invoice, gr_edi, hr_edi, hu_edi, in*, it_edi*, jo_edi*, ke*, latam_base, latam_invoice_document, lk_invoice, mx, my_edi, nl, no, pe, ph, pl*, ro_edi, rs_edi, sa_edi*, se, sg, sk, tr_nilvera*, tw_edi_ecpay, uy, vn_edi_viettel*).
- Also of interest: `account.payment` (account_check_printing, account_payment, hr_expense, point_of_sale, pos_online_payment, website_payment, l10n_account_withholding_tax, l10n_latam_check and others); `account.journal` (account_check_printing, account_debit_note, account_edi, account_payment, account_peppol, point_of_sale, l10n_*); `account.tax` (account_tax_python, account_edi_ubl_cii, hr_expense, purchase, point_of_sale, pos_account_tax_python, l10n_*); `account.bank.statement.line` (account_payment, point_of_sale, pos_hr). No Community module inherits `account.partial.reconcile`.

## 7. UNKNOWN items
- Who performs the tax closing entry that sets the tax lock date in a Community-only install: UNKNOWN — EVIDENCE INSUFFICIENT.
- Interactive bank reconciliation screen and full application of reconcile models in a Community-only install: UNKNOWN — EVIDENCE INSUFFICIENT (models exist; no screen found in `account/static/src/components`).
- Behaviour of the "in payment" state, reviewer-only editing of checked entries, follow-up reminders, tax report rendering: UNKNOWN — EVIDENCE INSUFFICIENT (hooks return the simple value in `account`; the rest is outside this source).
- Whether a universal rule "hash chain blocks all late edits" applies: it applies only to entries in journals with hash mode or entries secured by the wizard; other journals: UNKNOWN — EVIDENCE INSUFFICIENT for legal-requirement claims (the code only shows the country-forced audit trail in l10n_de).
- Exact numbers of the abnormal-invoice thresholds beyond the statistical formula (mean plus/minus 2 deviations, sample 10-30 documents, `account_move.py:2279-2340`): no business rationale stated in source.

