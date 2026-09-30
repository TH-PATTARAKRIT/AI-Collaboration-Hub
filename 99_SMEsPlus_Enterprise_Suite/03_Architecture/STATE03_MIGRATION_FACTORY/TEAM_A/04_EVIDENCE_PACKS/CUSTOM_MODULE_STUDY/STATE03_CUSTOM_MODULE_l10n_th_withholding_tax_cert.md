> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: l10n_th_withholding_tax_cert

## 0. Header
- Module: l10n_th_withholding_tax_cert
- License (confirmed in manifest): AGPL-3 (l10n_th_withholding_tax_cert/__manifest__.py:8)
- Author (manifest): Ecosoft, Odoo Community Association (OCA), SMEsPlus (l10n_th_withholding_tax_cert/__manifest__.py:7)
- Version (manifest): 19.0.1.5 (l10n_th_withholding_tax_cert/__manifest__.py:6)
- Path: addons_Extramodule/addons_extra/l10n_th_withholding_tax_cert
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Produces the Thai Withholding Tax Certificate document (the certificate a payer gives a payee showing income type, base amount, tax rate and tax withheld) from a vendor payment or from a posted journal entry that carries withholding tax lines (l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:72-196,237-285; wizard/create_withholding_tax_cert.py:88-136).
- Certificate content: payer company, payee (supplier) partner, payment date, income tax form (PND3 for individuals, PND53 for companies, also PND1/PND3a available in the list), payer type (withholding or paid one time), and lines each with type of income (Thai revenue-code categories 1 to 6 including several dividend sub-types), income description, base amount, tax percent and tax amount (models/withholding_tax_cert.py:9-66,173-195,368-426).
- Line amounts are taken from the withholding tax lines of the source payment/entry: amount = absolute journal item balance, percent = tax rate on the item, base = amount divided by percent (models/withholding_tax_cert.py:291-307). A consistency check blocks lines whose base x percent does not match the tax amount within currency precision (models/withholding_tax_cert.py:407-414).
- Workflow: Draft, Done, Cancelled (models/withholding_tax_cert.py:90-97,326-342). A "Substitute" option creates a replacement certificate that, on Done, cancels the certificate it replaces and leaves a chatter note (wizard/create_withholding_tax_cert.py:21-26,120-122; models/withholding_tax_cert.py:330-338).
- Multi-certificate creation: several payments/entries can be turned into certificates in one action (wizard/create_withholding_tax_cert.py:138-188; wizard xml multi view).
- Certificates can be reached from the payment and journal-entry forms through a smart button and from Vendors > WT Certificates (views/account_payment_view.xml, views/account_move_view.xml:7-18, views/withholding_tax_cert.xml:145-155). A signature image can be captured on the certificate for users in the ERP manager group (views/withholding_tax_cert.xml:90-93).
- The certificate "Number" is not from its own numbering sequence: it takes the name of the payment or, if none, of the journal entry (models/withholding_tax_cert.py:252). See section 6.

## 2. Attachment to CORE
- Depends on l10n_th_withholding_tax (manifest:11), an add-on that is not in the Community 19 tree (it supplies the withholding tax account flag wt_account, the withholding tax tax model account.withholding.tax, and the line field wt_tax_id used here) and is outside this assignment.
- Extends core account.payment (models/account_payment.py:8-43): adds one2many of certificates, a stored flag "all certificates cancelled or none" and re-declares move_line_ids as a one2many to journal items by payment id (account_payment.py:23; core account.move.line.payment_id at core:account/models/account_move_line.py:169). ADDS after core.
- Extends core account.move (models/account_move.py:8-39): same certificate list, stored flag and smart-button action. ADDS after core.
- Extends core account.account (models/account_account.py:18-33): overrides write and create; when the field wt_account changes it clears the whole registry cache so the cached list of withholding accounts is refreshed (account_account.py:20-33). Adds after core; core registry method clear_cache exists (core:orm/registry.py:998). The clearing of all registry caches on such a change is broad (models/account_account.py:9-16 states it as intended).
- ALTERS CORE CONTROL: none directly. The certificate model restricts its payment and move links with "restrict" on delete (models/withholding_tax_cert.py:110,127), which prevents deleting a payment or entry that has a certificate (BLOCKS deletion at database-reference level).
- Views inherit account.view_move_form and account.view_account_payment_form (core:account/views/account_payment_view.xml:136); menu placed under Vendors (account.menu_finance_payables, core:account/views/account_menuitem.xml:17). Server actions are bound to the account.payment and account.move "Action" menus to launch the wizard (wizard/create_withholding_tax_cert.xml:82-107).

## 3. New objects, security, automation, external calls
- New models: withholding.tax.cert (chatter enabled), withholding.tax.cert.line, create.withholding.tax.cert (transient wizard).
- ACLs (security/ir.model.access.csv:2-4): the invoicing group (account.group_account_invoice) has full access on certificate and lines; ALL internal users have full access on the creation wizard. The wizard itself raises errors unless the source is a payment or a posted journal entry (wizard/create_withholding_tax_cert.py:41-56).
- Record rules (security/account_security.xml:2-17): certificates and lines visible when company empty or among user's companies (global rules; note core computes the global flag from groups, core:base/models/ir_rule.py:54-56). Company scoping present via company_id on certificate (models/withholding_tax_cert.py:148-155); lines take it by relation (models/withholding_tax_cert.py:403-405).
- Multi-company caveat: the line consistency check uses the current environment company's currency precision, not the certificate company (models/withholding_tax_cert.py:410).
- Cache: a per-company cached list of withholding account ids (models/withholding_tax_cert.py:219-235).
- Performance indexes on state, payment, move, supplier, company, income form, payment date and line references; a migration adds them to existing databases (models/withholding_tax_cert.py index flags; migrations/19.0.1.5/post-migrate.py:28-105, uses idempotent database statements, not reproduced).
- Automation: none scheduled. External calls: none. Data flows: read-only from accounting entries into certificate documents; no posting of journal entries by this module.

## 4. Odoo 19 compatibility
- Models/fields used that do not exist in the Community 19 tree: account.withholding.tax (wizard/create_withholding_tax_cert.py:75,80,196), account.account.wt_account (models/withholding_tax_cert.py:233; wizard :19), account.move.line.wt_tax_id (models/withholding_tax_cert.py:294; wizard :150,154). They are expected from l10n_th_withholding_tax. Note Community 19 has its own separate withholding-tax framework in module l10n_account_withholding_tax (payment withholding lines, tax flag is_withholding_tax_on_payment; core:l10n_account_withholding_tax/models/account_tax.py:13, account_payment.py:21) which this module does not use.
- payment.move_line_ids re-declared with an unusual keyword ondelete on a one2many (models/account_payment.py:23): keyword validity for core 19 field API not verified.
- Wizard hard-codes tag-name matching ("53" / "3" in tag names of withholding tax records) to choose PND53 vs PND3 (wizard/create_withholding_tax_cert.py:73-84,199-205): depends on naming of tax tags; brittle.
- Uses @tools.ormcache with company key (models/withholding_tax_cert.py:219-220; core:tools/cache.py:61 defines ormcache).
- Tests in tests/test_wt_cert.py (4 tests) not run or checked.

## 5. Custom-to-custom dependencies
- l10n_th_withholding_tax (declared; not studied here). Depended on by: l10n_th_withholding_tax_cert_form (l10n_th_withholding_tax_cert_form/__manifest__.py:11) and l10n_th_withholding_tax_report (l10n_th_withholding_tax_report/__manifest__.py:16, not studied). Soft coupling: om_data_remove (models/model.py:182) and l10n_th_withholding_tax_multi (uses payment.move_line_ids which this module declares, l10n_th_withholding_tax_multi/models/account_payment.py:45), without declaring this module.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the certificate number (payment or entry name) satisfies the statutory need for a certificate book/number and runs sequentially for the payer.
- UNKNOWN - EVIDENCE INSUFFICIENT: definitions and behaviour of account.withholding.tax, wt_account, wt_tax_id (in l10n_th_withholding_tax).
- UNKNOWN - EVIDENCE INSUFFICIENT: how certificates are filed or reported (PND3/PND53 reports live in l10n_th_withholding_tax_report, which was not in this assignment).
- UNKNOWN - EVIDENCE INSUFFICIENT: mapping of the income-type codes to the current Revenue Department certificate form.
- UNKNOWN - EVIDENCE INSUFFICIENT: handling of foreign-currency payments (amounts taken from journal item balance in company currency; conversion not examined).
