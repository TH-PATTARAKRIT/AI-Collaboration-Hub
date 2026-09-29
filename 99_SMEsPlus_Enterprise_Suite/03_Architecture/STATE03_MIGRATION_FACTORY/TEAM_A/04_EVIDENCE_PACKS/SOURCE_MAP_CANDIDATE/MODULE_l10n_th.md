# Source Map (candidate) — `l10n_th`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `l10n_th` |
| Display name | Thailand - Accounting |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `060f062fa6016201` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/l10n_th/` |
| auto_install / application | ['account'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `account_qr_code_emv`, `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Localizations/Account Charts / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 1, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `account.chart.template`, `account.move`, `ir.actions.report`, `res.partner.bank`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.chart.template`, `account.move`, `ir.actions.report`, `res.partner.bank`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 49 of 50 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: `l10n_th` (Thailand - Accounting)

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, read-only). Pointers are relative to the addons root.
- Manifest: `l10n_th/__manifest__.py:1-32` — version 2.0, LGPL-3, author Almacom, category Accounting/Localizations/Account Charts, `countries: ['th']` (`:5`).
- Size: 5 Python model files (160 lines total), 4 chart CSVs, 1 tax-report XML (355 lines), 1 invoice-report view, 1 demo file, 1 test file. No security files, no groups, no record rules, no access rows, no cron (skeleton: groups/rules/crons empty).
- Evidence key: static source unless marked `(TEST)`.

## 1. Capabilities (core vs optional vs conditional)

Core (loaded whenever the module is installed):
- Thai chart-of-accounts template `th` plus Thai tax set and tax groups. `l10n_th/models/template_th.py:9-17`; data `l10n_th/data/template/*.csv`.
- Thai tax reports: VAT ("Tax Report"), PND53, PND3. `l10n_th/data/account_tax_report_data.xml:3,227,291`.
- "Tax Invoice" printed layout with buyer branch text; separate "Commercial Invoice" print action. `l10n_th/views/report_invoice.xml:3-37`.
- Thai PromptPay-style QR payment support on bank accounts (via EMV QR bridge). `l10n_th/models/res_bank.py:8-67`.
- Post-install hook keeps existing tax tags on taxes when the chart is reloaded/updated. `l10n_th/__init__.py:4-6`, `l10n_th/__manifest__.py:28`.

Automatic install: `auto_install: ['account']` — installs whenever `account` is present (`l10n_th/__manifest__.py:20`), i.e. it is not opt-in at module level. Applying the chart to a company is a separate step: the chart is chosen by the company's country via `account.chart.template` (`account/models/chart_template.py:98-134`, `:140`), and the first chart of a newly installed localization module is instantiated on the current company (`account/models/ir_module.py:62-70`). UNKNOWN — EVIDENCE INSUFFICIENT on exact auto-apply conditions for a given database without tracing `account` install flow in full.

Optional/conditional:
- Invoice layout switches to Thai only when the company's fiscal country is Thailand. `l10n_th/models/account_move.py:7-11`.
- QR behavior only for bank accounts whose country code is TH. `l10n_th/models/res_bank.py:20,30,36,41,56,64`.
- Commercial Invoice action is offered only for Thai-country sales-journal documents. `l10n_th/views/report_invoice.xml:36`.
- Demo company "TH Company" (Chiang Mai address) and demo chart load only in demo mode. `l10n_th/demo/demo_company.xml:3-36`.
- Fixed-asset model CSV is present (12 entries) but see section 8.

## 2. Business objects and lifecycle

Branch identity (partner-level, computed, display-only):
- A non-stored text "Branch <code>" shown for company-type partners in Thailand, using the partner's Company ID/registry number; "Headquarter" when that number is empty; blank for non-company or non-Thai partners. `l10n_th/models/res_partner.py:9-18`. Appears on Tax Invoice next to the customer VAT in all three address layouts (billing, same-as-shipping, no-shipping). `l10n_th/views/report_invoice.xml:4-13`. No stored branch field, no branch validation, no per-branch tax filing. UNKNOWN — EVIDENCE INSUFFICIENT for any branch-level (multi-branch VAT) accounting logic.

Chart template `th` at business level:
- Accounts: 144, all 6-digit codes (`code_digits '6'`, `l10n_th/models/template_th.py:12`; `l10n_th/data/template/account.account-th.csv`, header line 1). By class (first digit): Assets 50, Liabilities 19, Equity 3, Income 10, Direct cost 5xxxxx 7, Expense 6xxxxx 54, one technical 999999 account. By type: expense 42, fixed asset 22, current asset 15, current liability 13, depreciation expense 12, direct cost 7, non-current asset 6, other income 6, receivable 4, income 4, cash 3, payable 3, non-current liability 3, equity 3, unaffected earnings 1. 30 accounts flagged reconcilable; no account tags or account groups defined.
- Company-level defaults set on load: fiscal country Thailand; bank and cash journal code prefixes 11120 / 11110; default receivable 112100, payable 212100, stock valuation 113100, down-payment 212400; currency exchange gain/loss, early-payment discount gain/loss, cash difference gain/loss accounts; default sales tax = Output VAT 7%, default purchase tax = Input VAT 7%; default income 411100 and expense 511100; cash-basis tax option enabled on the company. `l10n_th/models/template_th.py:19-43`. POS receivable default 112101 (`:27`) is only meaningful if a POS module is installed (owner: `point_of_sale`).
- Tax groups: 5 (VAT 7%, WHT 1%, 2%, 3%, 5%), each with payable/receivable accounts. `l10n_th/data/template/account.tax.group-th.csv:2-6`.
- Taxes: 18 in total (`l10n_th/data/template/account.tax-th.csv`, 72 data rows). VAT: 6 — Input 7% / 0% / exempt and Output 7% / 0% / exempt (`:2-25`); only the 7% pair uses the VAT 7% group. Withholding (negative-rate) taxes: 12 — purchase side company (PND53) 1/2/3/5% by transportation/advertising/service/rental (`:26-41`); purchase side individual (PND3) same four rates (`:42-57`); sales side "withholding income tax" same four rates recorded to a tax-credit asset account, price-excluded (`:58-73`). Each tax has invoice and refund repartition lines; VAT taxes tag base and tax to specific report lines.
- Fixed-asset depreciation models: 12 rows, straight-line, life 3 to 20 years (land improvements 20, buildings 20, installations 10, machinery 5, spare parts 5, vehicles 5, accessories 5, furniture 5, computers 3, other 5, software 3, goodwill 20), yearly period. `l10n_th/data/template/account.asset-th.csv:2-13`.
- Not provided by the chart: fiscal positions, account groups, journals beyond core defaults (no such CSVs).

Tax reports (all root under Generic Tax Report, country-conditional):
- "Tax Report" (VAT monthly summary): numbered lines 1 to 12 — sales amount, less 0% sales, less exempt sales, taxable sales, output tax; purchase amount and input tax; tax payable vs excess; excess carried forward from prior period; net payable / net excess, with automatic carry-over. `l10n_th/data/account_tax_report_data.xml:3-224`, carry-over target `:217`. Foreign-VAT filing allowed (`:8`).
- "PND53" and "PND3" reports: Total Income, Total Remittance (withheld), Surcharge, Total. `l10n_th/data/account_tax_report_data.xml:227-289,291-354`. Surcharge lines read tags `SUR53` / `SUR3` (`:273,337`) but no tax in the template applies those tags (no match in `account.tax-th.csv`), so surcharge amounts are UNKNOWN — EVIDENCE INSUFFICIENT as to how populated (possible manual tagging).

## 3. Actions, validation, constraints, automation

- Bank QR validation (Thai bank accounts only): proxy type must be Ewallet ID, Merchant Tax ID, Mobile Number, none, or unset; Merchant Tax ID must be 13 digits; Mobile must be 10 digits. `l10n_th/models/res_bank.py:16-26`. The three Thai proxy types are added to the shared proxy list and revert to default if the module is removed. `:11-14`.
- QR eligibility: must be THB currency (message text mentions "PayNow", wording inherited, not Thai-specific) and requires a proxy type. `l10n_th/models/res_bank.py:55-67`. The QR settings block is forced visible for Thai accounts. `:34-38`. `(TEST)` THB-only, missing merchant city, and missing PromptPay info each block generation; a reference QR string is asserted. `l10n_th/tests/test_l10n_th_emv_qr.py:43-77`.
- QR payload: fixed PromptPay application identifier; account type 1 = mobile (leading 0 replaced by 66, zero-padded to 13), 2 = tax ID, 3 = e-wallet; merchant field 29. `l10n_th/models/res_bank.py:40-53`.
- Commercial Invoice printing is refused for anything that is not an invoice/receipt. `l10n_th/models/ir_actions_report.py:8-15`. `(TEST)` core report test registers this report in a generic report harness: `base/tests/test_reports.py:36`.
- Automation: none (no cron, no server action, no wizard).

## 4. Security and multi-company

- No groups, access rows or record rules defined in this module. UNKNOWN — EVIDENCE INSUFFICIENT beyond inherited rules of `account` / `base`.
- Company scoping comes from the chart-loading mechanism: template data is written per company (`l10n_th/models/template_th.py:22` uses the loading company) and taxes/accounts are company-owned in `account`. Thai behavior on invoices is decided per company by fiscal country (`l10n_th/models/account_move.py:9`), so in a multi-company database only Thai-fiscal-country companies get the Thai layout.
- Partner branch text depends on partner country, not on company (`l10n_th/models/res_partner.py:13`).

## 5. Handoffs (owner in bold)

- Chart loading, tax engine, repartition, tax closing, report engine, tag-preservation helper — owner `account` (`account/models/chart_template.py`, `account/models/ir_module.py:27-66`, hook import at `l10n_th/__init__.py:5`).
- EMV QR generation framework, proxy fields, CRC and payload assembly — owner `account_qr_code_emv` (`account_qr_code_emv/models/res_bank.py:15-16,31,51,127`). `l10n_th` supplies Thai values only.
- Stock valuation account default (113100) is consumed by inventory valuation — owner `stock_account`/`account`; only a default is set here (`l10n_th/models/template_th.py:15,40`). UNKNOWN — EVIDENCE INSUFFICIENT whether stock accounts are exercised in any way not covered by defaults.
- Down-payment account default — consumed by the sales module when down payments are used; owner `sale` (module name only; not traced).
- Fixed-asset models (`account.asset`) — no such model found in Community; consumer would be an Enterprise asset module. UNKNOWN — EVIDENCE INSUFFICIENT. The community loader only reads accounts, account groups, tax groups, taxes, fiscal positions from CSV (`account/models/chart_template.py:1129-1147`).
- Withholding-tax payment/certificate flow (PND forms, certificates, WHT on payment) — not implemented here; the separate Community module `l10n_account_withholding_tax` exists but does not reference `l10n_th`. UNKNOWN — EVIDENCE INSUFFICIENT whether the Thai WHT taxes are meant to pair with it.
- e-Tax invoice / e-invoicing for Thailand — no Thai EDI module found in this tree (grep for `l10n_th` outside itself found only a generic report test in `base`). UNKNOWN — EVIDENCE INSUFFICIENT.

## 6. Configuration/defaults/computed behavior that changes outcomes

- Fiscal country Thailand and THB (via fiscal country currency) are forced on chart load; company country filled if empty. `l10n_th/models/template_th.py:23`, `account/models/chart_template.py:489-511`.
- Cash-basis taxation is turned on for the company (`tax_exigibility` true, company setting `account/models/company.py:220`), but none of the 18 taxes in the template uses cash-basis exigibility (no exigibility column in the CSV). Effect on Thai VAT timing: UNKNOWN — EVIDENCE INSUFFICIENT.
- VAT tax base/tax lines are tagged to the numbered report lines; changing tax tags changes report results. `l10n_th/data/template/account.tax-th.csv:2-25`.
- Sales-side withholding taxes are price-excluded and post to a receivable-type tax-credit account (114300) not used in tax closing; purchase-side withholding posts to payable accounts 213301 (individual) / 213302 (company) not used in tax closing; VAT accounts are flagged for tax closing. `l10n_th/data/template/account.tax-th.csv:3-7,27,43,59`.
- Invoice title is fixed to "Tax Invoice" for the Thai layout regardless of document state. `l10n_th/views/report_invoice.xml:14-16`.
- Bank accounts with a Thai country are the only trigger for QR options; the invoice's QR method must be EMV QR. `l10n_th/models/res_bank.py:55-56`, `(TEST)` `l10n_th/tests/test_l10n_th_emv_qr.py:44`.

## 7. Effective extension path

- `l10n_th` itself extends (`_inherit`): `account.chart.template`, `res.partner`, `account.move`, `ir.actions.report`, `res.partner.bank`. `l10n_th/models/*.py`.
- Other modules extending the same key models: `account.move` and `res.partner.bank` are extended by many localizations (e.g. `l10n_sg`, `l10n_hk`, `l10n_kh`, `l10n_vn`, `l10n_br` use the same EMV QR bridge: manifest dependency on `account_qr_code_emv` found in those modules). Broader `_inherit` enumeration for `account.move` not exhaustively traced: UNKNOWN — EVIDENCE INSUFFICIENT.
- Modules depending on `l10n_th`: none in this Community tree. Only reference outside the module is a test lookup of its Commercial Invoice report `(TEST)` `base/tests/test_reports.py:36`. Note: no `product` interaction anywhere in `l10n_th` (no product models, fields or data).
- Depends on: `account`, `account_qr_code_emv` (`l10n_th/__manifest__.py:16-19`); `account_qr_code_emv` depends only on `account` (`account_qr_code_emv/__manifest__.py`).

## 8. UNKNOWN items

- Tax invoice legal numbering / sequence rules for Thai tax invoices, receipts, credit/debit notes: UNKNOWN — EVIDENCE INSUFFICIENT (only report title and branch text customized).
- Multi-branch VAT filing, per-branch reports: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the `account.asset` depreciation CSV is consumed in Community: UNKNOWN — EVIDENCE INSUFFICIENT (loader in `account` does not read it; no asset module found).
- Surcharge (SUR53 / SUR3) population; PND certificates/forms: UNKNOWN — EVIDENCE INSUFFICIENT.
- Effect of enabling cash-basis on the company without cash-basis taxes: UNKNOWN — EVIDENCE INSUFFICIENT.
- Thai-specific product behavior: none; UNKNOWN — EVIDENCE INSUFFICIENT for any product-level Thai rule (see `product.md`).

