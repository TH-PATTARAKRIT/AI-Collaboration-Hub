# Source Map (candidate) — `l10n_account_withholding_tax`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `l10n_account_withholding_tax` |
| Display name | Withholding Tax on Payment |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `0707a39caf1540f5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/l10n_account_withholding_tax/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (5): `l10n_account_withholding_tax_pos`, `l10n_kh`, `l10n_lk`, `l10n_ph`, `l10n_sa_withholding_tax`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Localizations / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `account.payment.withholding.line` (Payment withholding line); `account.withholding.line` (withholding line); `account.payment.register.withholding.line` (Payment register withholding line)
- Objects extended from other modules (7): `account.tax`, `product.template`, `account.payment`, `res.company`, `res.config.settings`, `analytic.mixin`, `account.payment.register`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 2 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.tax`, `product.template`, `account.payment`, `res.company`, `res.config.settings`, `analytic.mixin`, `account.payment.register`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 52 of 52 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: l10n_account_withholding_tax
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Lets a payer/payee register a tax that is withheld at payment time (not at invoice time) while registering a payment for an invoice/bill, or on a payment record directly (l10n_account_withholding_tax/__manifest__.py:`description`; wizards/account_payment_register.py:13-51; models/account_payment.py:12-26). Optional module, depends only on `account`; no auto-install (manifest `depends`).
- Tax flag "Withhold On Payment": marks a tax as withholding; only offered for sale/purchase taxes with a negative rate (models/account_tax.py:13-16; views/account_tax_views.xml:8; onchange resets flag if amount is not negative: models/account_tax.py:36-40).
- Optional withholding numbering sequence per tax (shown on purchase-side taxes only) (models/account_tax.py:17-23; views/account_tax_views.xml:10-12).
- Company setting "Withholding Tax Base" account, used as default account on base lines and hides that column when set (models/res_company.py:12-16; models/res_config_settings.py:12-15; views/res_config_settings.xml:6-18; models/account_withholding_line.py:235-242).
- Sales price hint on product now also shows "Tax Withheld" amount (models/product_template.py:13-67).
- Payment receipt template extended to show withholding (views/report_payment_receipt_templates.xml) - content not analysed: UNKNOWN — EVIDENCE INSUFFICIENT.
- Withholding section only appears when the company has at least one withholding tax matching the payment direction (sale for inbound, purchase for outbound); in the wizard it is also hidden for multi-payment batches or ungrouped multi-invoice runs (models/account_payment.py:35-52; wizards/account_payment_register.py:98-124; models/account_withholding_line.py:430-435).

## B. Business objects, relationships, computation and posting
- Objects: shared abstract "withholding line" logic (models/account_withholding_line.py:10-15) realised as a wizard-time line (temporary, wizards/account_payment_register_withholding_line.py:5-21) and a stored payment line (models/account_payment_withholding_line.py:5-22); a payment owns many lines; deletion of payment removes them (ondelete cascade, :18-22). Lines reference tax, account, analytic distribution, base and withheld amounts, optional numbering.
- Invoice side: withholding taxes on invoice/bill lines are EXCLUDED from normal invoice tax computation unless explicitly asked, so invoice totals are unchanged (models/account_tax.py:70-79; TEST tests/test_account_withholding_amounts.py:530).
- Proposal at payment time: wizard derives lines from the taxes on the selected invoice(s) lines, grouped by name/analytic/account/tax/currency; existing lines are updated, duplicates deleted, obsolete removed (wizards/account_payment_register.py:126-152; models/account_withholding_line.py:454-538). A user can also add a line for a tax not on the invoice (TEST tests/test_account_withholding_flows.py:40, 83-115).
- Amount logic: base = original base converted to payment currency x "paid factor" (share of the invoice being paid, handles partial payment/installments/discounts) (models/account_withholding_line.py:209-220; wizards/account_payment_register_withholding_line.py:40-59); withheld amount = original withheld amount x (current base / original base) (models/account_withholding_line.py:222-233); both editable manually and manual values are kept when the entry is built (:321-341; TEST flows:1011-1042). Currency conversion uses the payment date rate (models/account_withholding_line.py:153-207).
- Net amount = payment amount minus sum of withheld amounts; must not be negative (wizards/account_payment_register.py:57-67, 204-205; TEST flows:927-950).
- Lifecycle: no new state machine. Lines are editable while the payment is draft (views/account_payment_views.xml:9,14,50) and are carried into the payment when created from wizard (wizards/account_payment_register.py:213-218).
- Posting effect (business level): the payment entry is built so that the bank/outstanding line carries only the net amount, the receivable/payable counterpart carries the gross settled amount, plus a withheld-tax line (per tax repartition, including tags), and a pair of "WH Base" and "WH Base Counterpart" lines for the tax base (models/account_withholding_line.py:345-428, docstring 348-353; account/models/account_payment.py:337-391). Withholding lines partner = payment partner (:389, 417, 425; TEST flows:1043). Tax lines use the tax's repartition lines/accounts/tags (TEST flows:426, 559).
- Withholding number: taken from the line name, else from the tax's sequence at entry-build time; if neither exists the user is asked to enter a number (models/account_withholding_line.py:363-372); placeholders show upcoming sequence numbers during editing (:125-140, 267-284; TEST flows:952).
- Refund handling: line marked as refund when tax use and payment direction are opposite, so refund repartition applies (models/account_withholding_line.py:548-556; TEST flows:1072).
- Outstanding account: if the payment method has no payment account, the user/system proposes one (latest payment's outstanding account for the same method); chosen account is set reconcilable if needed (wizards/account_payment_register.py:69-96, 208-212; TEST flows:382, 767, 890).

## C. Validations / automation / security / multi-company
- Base amount of a line must be > 0 (models/account_withholding_line.py:290-295; TEST flows:868).
- Line account may not be a liquidity account of the payment/journal/methods or the company transfer account (models/account_withholding_line.py:297-302; models/account_payment_withholding_line.py:82-94).
- Withholding tax may not use "Group of taxes" or "Percentage tax included" computation (models/account_tax.py:42-47). On tick, tax is forced to on-invoice exigibility and tax-excluded pricing (models/account_tax.py:29-34).
- Tax choices restricted by company hierarchy, tax use and flag (models/account_withholding_line.py:47-52, 430-435); line has automatic company check (models/account_withholding_line.py:15).
- Security: ACL only for group "Invoicing" (account.group_account_invoice) with full CRUD on the two line models (security/ir.model.access.csv:2-3). No record rules added; company isolation relies on company checks/company fields (models/account_withholding_line.py:105-111).
- Payment synchronisation: changes to lines or the flag trigger regeneration of the payment's journal entry (models/account_payment.py:97-100; TEST flows:792).
- No scheduled jobs.

## D. Handoffs
- Journal entry creation/synchronisation and reconciliation of payment: owned by `account` (hook `_prepare_move_withholding_lines`: account/models/account_payment.py:284-286, used at 337-391 and 1048).
- Tax computation engine (base lines, rounding, repartition, tags): owned by `account` (calls at models/account_withholding_line.py:171-181, 374-379).
- Analytic distribution: line inherits the analytic mixin (models/account_withholding_line.py:13; TEST flows:618, 680).
- Tax report grids: through tax tags of the repartition lines (TEST flows:426); reports owned by `account`/localisation.
- Point of sale variant: l10n_account_withholding_tax_pos (auto-install with this module and point_of_sale).
- Jurisdiction packages that build on it: l10n_kh, l10n_lk, l10n_ph, l10n_sa_withholding_tax (depend on this module).

## E. Configuration that changes outcomes
- Tax: flag, negative rate, computation type, sequence, repartition/tags, invoice label (label not defaulted to tax name for withholding taxes: models/account_tax.py:53-64).
- Company: withholding tax base account.
- Payment method line payment account (decides whether outstanding account must be chosen); journal default account.
- Partial payment / installment / early-discount context via paid factor (TEST flows:514).

## F. Effective extension path
- Modules with this module as manifest dependency: l10n_account_withholding_tax_pos, l10n_kh, l10n_lk, l10n_ph, l10n_sa_withholding_tax.
- Modules extending the payment object (account.payment): account_check_printing, account_payment, hr_expense, l10n_account_withholding_tax, l10n_ar_withholding, l10n_au, l10n_ch, l10n_in, l10n_latam_check, l10n_nz, l10n_ph, l10n_pl_bank_verification, point_of_sale, pos_online_payment, website_payment.
- Modules extending the payment wizard (account.payment.register): account_payment, hr_expense, l10n_account_withholding_tax, l10n_ar_withholding, l10n_latam_check, l10n_pl_bank_verification.
- Modules extending the tax object also include l10n_account_withholding_tax_pos, l10n_ar_withholding (see account_tax_python note for full list).
- Abstract withholding line model: no other module extends it.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: interplay with l10n_ar_withholding (separate Argentine mechanism; not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: reporting/certificate output beyond the receipt template.
- Source observation: payment line model declares a compute referencing a wizard field that does not exist on that model (models/account_payment_withholding_line.py:41-44); effect not verified.
- UNKNOWN — EVIDENCE INSUFFICIENT: point-of-sale flow (module l10n_account_withholding_tax_pos not read).

