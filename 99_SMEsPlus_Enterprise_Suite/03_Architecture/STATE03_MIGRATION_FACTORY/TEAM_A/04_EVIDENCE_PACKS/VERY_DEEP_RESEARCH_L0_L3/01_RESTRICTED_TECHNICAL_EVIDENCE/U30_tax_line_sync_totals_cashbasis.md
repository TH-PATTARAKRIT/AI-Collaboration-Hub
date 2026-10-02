# U30 - tax_line_sync_totals_cashbasis - Restricted Technical Evidence

> **RESTRICTED - TECHNICAL EVIDENCE - NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**
> Unit: U30 `tax_line_sync_totals_cashbasis` (Thai Tax Core lane, source-level completion of what TXA1, TXA2 and TXC listed as NOT READ) - Source revision `19.0.post20260921` (Odoo 19 Community only) - Date: 2026-10-02
> Modules read in depth: `account` (account_move.py, account_move_line.py, account_tax.py, account_partial_reconcile.py, account_payment_term.py, account_cash_rounding.py, company.py, chart_template.py, views, security, report data), `base` (res_currency.py rate and conversion), and Community overrides or hooks reached: `hr_expense`, `account_edi_ubl_cii` (import path), `l10n_th` (template data and print), `sale` and `purchase` (totals consumers), `point_of_sale` (NOT installed, read only for the balance-check setter).
> Read-only on source; DB queried only for configuration (counts, flags, names of seeded configuration, ACL and rule rows). No Odoo started, no L5/AWT claims; execution-dependent items are flagged `RT`. Nothing from `Extra_Thailand`, `Extra_Module_scgl`, Enterprise or proprietary code was opened.
> SEPARATION: this file states what Community source and the restored dump DO. It asserts no Thai statutory requirement; statutory statements are linked by id only (rounding S12-08 / TXS-R1 rounding row, FX rate S12-04 and S12-03, tax point S05-01 and S05-02, credit note S07-02, foreign-currency invoices S12-02) and are not derived from Odoo behaviour. Community absence is not proof that a business requirement does not exist. No V-level, Complete, coverage percentage or Gate PASS is asserted.
> Claim IDs `VDR-U30-C###`; neutral IDs `N-U30-###` (see `02_NEUTRAL_KNOWLEDGE/U30_tax_line_sync_totals_cashbasis_NEUTRAL.md`). Claim references in the prose below are resolved claim ids; every statement is backed by a row in the Claims table.

## 0. Scope, method and Function-ID mapping

| Capability | Function-ID | Note |
|---|---|---|
| CAP-U30-01 Synchronisation of derived journal items (framework, order, protection, balance check) | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis; PCO-F01 used only on lock-date claims |
| CAP-U30-02 Payment-term items (due-date items of receivable and payable) | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-03 Tax-item generation and update from base items | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-04 Rounding allocation across lines, tax items and currencies | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-05 Cash-rounding, early-payment, discount-allocation and balancing items | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-06 Document tax totals summary (display, edit, stored versus recomputed) | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-07 Cash-basis tax exigibility, end to end | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-08 Tax items on credit note, switch, reset, cancel and fiscal-position change | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |
| CAP-U30-09 Multi-currency tax items, rate date and exchange interplay | FUNCTION MAPPING REQUIRED | no index entry for tax-item synchronisation, totals or cash basis |

Method (line ranges actually read): `account/models/account_move.py` 1000-1060, 1100-1260, 1380-1960, 2530-2610, 2655-2910, 3040-4215, 4440-4580, 5060-5335, 5420-5800, 5995-6195, 6269-6410, 7040-7090 plus targeted reads of field declarations (lines 207-292, 366-420, 533-545, 599-604, 715-725, 765) and 6991-6996; `account_move_line.py` 190-250, 330-350, 395-470, 520-540, 700-830, 905-1250, 1476-1640, 1690-2030, 2076-2098, 2236-2545, 2645-2695, 2780-3150, 3454-3500; `account_tax.py` 160-180, 262-280, 1137-1400, 1555-3165, 5365-5382; `account_partial_reconcile.py` (all 732 lines); `account_payment_term.py` 55-85, 155-260; `account_cash_rounding.py` (all); `account_report.py` 55-80; `company.py` 120-160, 214-232, 305-325; `chart_template.py` 705-775, 1175-1195; `res_config_settings.py` 265-282; `account_move_reversal.py` 88-190; views and reports (`account_move_views.xml` 880-892, 1018-1030, 1105-1145, 1358-1366, 1555; `report_invoice.xml` 365-422, 525-600); `base/models/res_currency.py` 118-320; `hr_expense/models/account_move.py` 60-130 and `account_tax.py` 20-50; `account_edi_ubl_cii/models/account_edi_common.py` 1640-1830; `l10n_th` template, move and print files; `sale` and `purchase` totals methods. Override scans over the 356 installed modules for every synchronisation, engine, cash-basis and rate method name and for the context keys that control them; DB configuration queries (company, taxes, tax groups, journals, payment terms, currencies and rates, access rows, rules, reports, crons). Earlier units were read first for their capability sections, claim lists, registers and stated limits (TXA1, TXA2, TXC, U11 with correction packets U10-R2, U11-R1 and U11-R2, U12, U13 CAP-U13-01) and were not re-verified line by line; where a line is restated here it was re-read in source and is marked as a re-read of the earlier claim.

## CAP-U30-01 Synchronisation of derived journal items (framework, order, protection, balance check)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (PCO-F01 only on the lock-date claims).

### D1 Business purpose and process semantics
Keep every derived accounting item of a document consistent with what the user typed, at every create, write, unlink and posting, so that totals, tax, receivable or payable and balance agree. Business questions covered: which derived items exist, when each is recomputed, when it is protected or editable, how the balance check and recursion guard interact, and in what order the chain recomputes. VDR-U30-C001 VDR-U30-C330

### D2 Architecture, data, objects
- Move-level manager stack VDR-U30-C001 VDR-U30-C002 VDR-U30-C003 VDR-U30-C004; generic manager VDR-U30-C052 VDR-U30-C053 VDR-U30-C055 VDR-U30-C056 VDR-U30-C057 VDR-U30-C058 VDR-U30-C059 VDR-U30-C060 VDR-U30-C061; needs merging VDR-U30-C064 VDR-U30-C065; recursion guard VDR-U30-C007 VDR-U30-C009 VDR-U30-C010; balance check VDR-U30-C011 VDR-U30-C012 VDR-U30-C013 VDR-U30-C014; item-level synchroniser VDR-U30-C066 VDR-U30-C008; protection VDR-U30-C020 VDR-U30-C021 VDR-U30-C022; write and unlink guards VDR-U30-C026 VDR-U30-C028 VDR-U30-C047 VDR-U30-C046 VDR-U30-C048.

### D3 Source/technical/workflow logic
1. create(): reject state posted VDR-U30-C017; open balance check and synchronisation with an empty container VDR-U30-C018 VDR-U30-C019; ORM create; protect supplied computed values VDR-U30-C020; container filled with the new moves VDR-U30-C019; totals value applied last VDR-U30-C023; manual flag cleared VDR-U30-C024.
2. write(): protecting, balance check, synchronisation around the ORM write VDR-U30-C025; flag set manual VDR-U30-C026; business-model synchronisation after VDR-U30-C027; lock re-checks VDR-U30-C030 VDR-U30-C031 VDR-U30-C032; totals value written last VDR-U30-C033.
3. Item create, write and unlink wrap the owning documents in the same managers VDR-U30-C038 VDR-U30-C045 VDR-U30-C049; guards VDR-U30-C040 VDR-U30-C042 VDR-U30-C043 VDR-U30-C044 VDR-U30-C046 VDR-U30-C047.
4. Order of work VDR-U30-C005 VDR-U30-C006: entering ascending 10..80 (snapshots), exiting descending 80..10 (recomputation). Payment terms therefore run last on final totals (INFERENCE).
5. Each manager: snapshot -> change -> compare -> delete or create or rewrite VDR-U30-C052 VDR-U30-C055 VDR-U30-C056 VDR-U30-C060.
6. Deletion of a document: no synchronisation, items unreconciled then deleted VDR-U30-C034 VDR-U30-C035.

State list:
- `new draft -> derived items created [create + synchronisation] VDR-U30-C018`
- `draft -> draft, derived items recomputed [write of an input] VDR-U30-C101`
- `draft -> posted [post] derived items frozen VDR-U30-C028 VDR-U30-C095`
- `posted -> draft [reset] items kept, re-derived on next input change VDR-U30-C299`
- `any -> deleted [unlink] synchronisation skipped VDR-U30-C034`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Editing a draft line re-derives tax, rounding, balancing and term items inside one save, then asserts balance VDR-U30-C001 VDR-U30-C013. |
| 2 | Reversal / negative path | Reset to draft keeps stored items VDR-U30-C299; deletion unreconciles first VDR-U30-C035; credit notes go through the same framework (CAP-U30-08). |
| 3 | Multi-company / data scope | Containers hold the moves in the write set only; item and move rules are per company (DB rules below); company currency decimals drive the balance test VDR-U30-C014. |
| 4 | Side effects and cross-module | Payment and bank-statement synchronisation after write VDR-U30-C027; expenses and e-invoice import use the same framework VDR-U30-C088 VDR-U30-C134. |
| 5 | Configuration and optionality | Balance-check suppression key and read-only bypass exist VDR-U30-C011 VDR-U30-C029; no installed module suppresses the check VDR-U30-C016; point of sale does, not installed VDR-U30-C015. |
| 6 | Validation and constraints | Cannot create posted VDR-U30-C017; tax and due-date items undeletable by users VDR-U30-C047; posted items undeletable VDR-U30-C046; hashed items undeletable VDR-U30-C048; restrictive audit trail VDR-U30-C036; sequence-chain rule VDR-U30-C037. |
| 7 | Roles and permissions | Posting needs the invoicing group (U11); lock checks apply to the user lock dates VDR-U30-C041; checks are declared on models, not on roles. Move and item ACL counts are in the DB reconciliation. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - no cron drives the framework; the auto-post cron (DB: 1 of 2 account crons) posts drafts through the same write path (U11). |
| 9 | Exception and failure behaviour | Unbalanced result raises a user error naming one or several entries VDR-U30-C013; lock violations raise user errors VDR-U30-C042; unknown combined outcomes VDR-U30-C329. |
| 10 | Accounting, audit, compliance | Item creation, change and deletion are logged to the chatter for documents posted once VDR-U30-C049 VDR-U30-C039; tax lock protects balance, taxes and tags VDR-U30-C041; manual flag marks edits VDR-U30-C026. |

### DB reconciliation (config only)
Company rules: account.move and account.move.line each have one global multi-company rule (company in allowed companies) plus group rules (invoices, personal invoices, portal, purchase user, readonly, expense approver); ACL rows in the dump: account.move 7, account.move.line 8 (the account module declares four each including portal; extra rows come from other installed modules) VDR-U30-C349 VDR-U30-C350. Crons of the account module: 2 (post draft with auto-post; send invoices automatically), both active. OBSERVATION; no document exists to exercise the framework.

### Unknown / Runtime
- RT: combined-change numeric outcome VDR-U30-C329; reverse-order recomputation confirmed only by reading, not executing VDR-U30-C006.

## CAP-U30-02 Payment-term items (due-date items of receivable and payable)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Derive the receivable or payable items (one per due date) that reflect payment terms, currency and the final document totals, including early-payment-discount data. VDR-U30-C067 VDR-U30-C332

### D2 Architecture, data, objects
- Needed values VDR-U30-C067 VDR-U30-C068 VDR-U30-C069; key VDR-U30-C077 VDR-U30-C074; computation VDR-U30-C073 VDR-U30-C080 VDR-U30-C081 VDR-U30-C082 VDR-U30-C083 VDR-U30-C084 VDR-U30-C085; due date VDR-U30-C079; synchroniser VDR-U30-C078; constraints VDR-U30-C086 VDR-U30-C087; expense override VDR-U30-C088 VDR-U30-C089.

### D3 Source/technical/workflow logic
1. Needed terms computed per move VDR-U30-C067; empty when not invoice-like or no lines VDR-U30-C069.
2. Totals source: unsaved record from fresh tax figures VDR-U30-C070; stored record from stored amounts VDR-U30-C071; sign differs between branches VDR-U30-C072.
3. With a term: instalments from the term model VDR-U30-C073; without: one signed total at due date VDR-U30-C075; discount data attached VDR-U30-C076.
4. Same-key instalments merged VDR-U30-C074.
5. Generic synchroniser compares and applies VDR-U30-C078 VDR-U30-C060; runs last in the chain VDR-U30-C006.
6. Due date follows needed terms VDR-U30-C079.

State list:
- `no items -> items created [document has lines, term or due date set] VDR-U30-C069`
- `items -> items rewritten or merged [date, term, currency or total changes] VDR-U30-C059`
- `items -> items deleted [no product lines or key not needed] VDR-U30-C057`
- `posted -> frozen by read-only rules, no explicit state test VDR-U30-C333`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | A 30-day term on a 100 percent line gives one item at invoice date plus 30 days for the total VDR-U30-C073 VDR-U30-C081. |
| 2 | Reversal / negative path | Credit notes and refunds use the same derivation with the sign applied to totals VDR-U30-C071; reverse-and-modify rebuilds items VDR-U30-C293. |
| 3 | Multi-company / data scope | Terms are per company or global (company rule on payment terms in DB); company currency drives amounts VDR-U30-C073. |
| 4 | Side effects and cross-module | Early-payment data stored on the item feeds payment registration (U12) VDR-U30-C076; expenses replace derivation VDR-U30-C088. |
| 5 | Configuration and optionality | Payment term optional VDR-U30-C334; early discount only on a single 100 percent line VDR-U30-C086. |
| 6 | Validation and constraints | Percent lines total 100 VDR-U30-C086; receivable/payable account rule VDR-U30-C087; cannot delete items VDR-U30-C047. |
| 7 | Roles and permissions | Payment term ACL: DB 4 rows for terms and 2 for instalment lines; no role gate on the derivation itself. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none. |
| 9 | Exception and failure behaviour | Zero total gives zero rate and zero company amounts for fixed lines VDR-U30-C080; preview sign question VDR-U30-C072. |
| 10 | Accounting, audit, compliance | Stored items are the ledger receivable or payable; discount fields later drive discount settlement VDR-U30-C076. |

### DB reconciliation (config only)
DB: 10 payment terms; 1 with early discount; all with early-pay computation included; payment term company rule global. OBSERVATION: no mixed-mode term, so only the stored discount fields (not mixed items) arise for Thai terms.

### Unknown / Runtime
- RT: instalment rounding with cash rounding in foreign currency; preview sign VDR-U30-C072.

## CAP-U30-03 Tax-item generation and update from base items

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Create, update and delete the tax items of a draft document from its base items, keep manual tax amounts when appropriate, and tag the base items. VDR-U30-C335 VDR-U30-C090

### D2 Architecture, data, objects
- Base and tax items VDR-U30-C090 VDR-U30-C091; tracked values VDR-U30-C092 VDR-U30-C093; decision tree VDR-U30-C094 VDR-U30-C095 VDR-U30-C096 VDR-U30-C097 VDR-U30-C098 VDR-U30-C099 VDR-U30-C100; pipeline VDR-U30-C101 VDR-U30-C106 VDR-U30-C107 VDR-U30-C108; base-line preparation VDR-U30-C109 VDR-U30-C110; sign VDR-U30-C111 VDR-U30-C112 VDR-U30-C113 VDR-U30-C114; grouping VDR-U30-C115 VDR-U30-C116 VDR-U30-C117; mapping VDR-U30-C118 VDR-U30-C119 VDR-U30-C120 VDR-U30-C121; persistence VDR-U30-C102 VDR-U30-C103 VDR-U30-C104 VDR-U30-C105; private part VDR-U30-C124 VDR-U30-C125 VDR-U30-C126 VDR-U30-C122 VDR-U30-C123 VDR-U30-C128; overrides VDR-U30-C129 VDR-U30-C130 VDR-U30-C131; e-invoice VDR-U30-C132 VDR-U30-C133 VDR-U30-C134.

### D3 Source/technical/workflow logic
1. Snapshot of base and tax item values before the change VDR-U30-C092 VDR-U30-C093; draft-only document values VDR-U30-C094.
2. After the change, per draft move choose round-from-tax-lines: type or currency change -> false VDR-U30-C096; taxed base removed -> any tax value changed VDR-U30-C097; base changed -> keep if untaxed change, tax set changed or protected VDR-U30-C098 (skip entirely when all values supplied VDR-U30-C099); rate only -> reapply rate VDR-U30-C100; otherwise nothing.
3. Compute rounded base and tax lines, accounting data and tax-item diff VDR-U30-C101.
4. Private-part tax item created, updated or deleted in the same pass VDR-U30-C122 VDR-U30-C123.
5. Persist: grouped base updates, deletions, creations VDR-U30-C104.
6. Private-part base items rebuilt in manager 60 VDR-U30-C125 VDR-U30-C126 VDR-U30-C128.

State list:
- `no tax items -> tax items created [taxed base item appears] VDR-U30-C103`
- `tax items -> tax items updated [input changed, amounts differ] VDR-U30-C120`
- `tax items -> tax items deleted [identity no longer needed or duplicate] VDR-U30-C120`
- `draft -> posted: skipped thereafter VDR-U30-C095`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | One 7 percent output tax on one line gives one base item with tag and one tax item with tag on the tax account (U13/TXA1 data) VDR-U30-C118 VDR-U30-C121. |
| 2 | Reversal / negative path | Type change recomputes fully VDR-U30-C096; credit notes use refund distribution and positive document totals VDR-U30-C112 VDR-U30-C113; removal of all taxes handled for entries VDR-U30-C201. |
| 3 | Multi-company / data scope | Distribution lines and taxes follow their company (rules in DB); taxes are filtered to the company tree on default (TXA1); documents may not keep taxes of another tax country VDR-U30-C307. |
| 4 | Side effects and cross-module | Expense and e-invoice overrides VDR-U30-C129 VDR-U30-C132; tax lock and tags feed reports (CAP-U30-07). |
| 5 | Configuration and optionality | Partial deductibility optional VDR-U30-C336; rounding method from company (CAP-U30-04). |
| 6 | Validation and constraints | No taxes on off-balance accounts VDR-U30-C337; deductibility 0 to 100 and only on vendor documents (TXA1); tax items undeletable by users VDR-U30-C047. |
| 7 | Roles and permissions | Tax model ACL: administrator full, invoicing and others read (DB: account.tax 7 rows, tax group 5, distribution line 4); derivation has no role gate. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none. |
| 9 | Exception and failure behaviour | Imbalance after sync raises VDR-U30-C013; zero rate gives zero company amounts (U11, TXA1); private-part swap RT VDR-U30-C127. |
| 10 | Accounting, audit, compliance | Tax items stored with base amount VDR-U30-C118; changes to posted items blocked VDR-U30-C040; tax lock VDR-U30-C042. |

### DB reconciliation (config only)
DB: 18 taxes (6 VAT, 12 withholding, all percent, on invoice), 5 tax groups, 72 distribution lines (TXA1 observations re-confirmed by a fresh query for group and exigibility counts). Partial deductibility group exists; purchase journal has no private-share account (TXA1). Tax model rules and ACL VDR-U30-C351. OBSERVATION.

### Unknown / Runtime
- RT: private-part item currency semantics VDR-U30-C127; whether a biggest-tax rounding item is deleted and rebuilt at each pass (its key may match a computed tax item).

## CAP-U30-04 Rounding allocation across lines, tax items and currencies

**Function-ID(s):** FUNCTION MAPPING REQUIRED (statutory link S12-08 for the rounding row).

### D1 Business purpose and process semantics
Allocate rounding differences between lines, taxes, distribution lines and currencies so that document totals equal totals computed on the whole document (global method) or per-line rounding applies (per-line method). VDR-U30-C338 VDR-U30-C135

### D2 Architecture, data, objects
- Methods VDR-U30-C135 VDR-U30-C136 VDR-U30-C137 VDR-U30-C138; raw step VDR-U30-C140 VDR-U30-C141 VDR-U30-C142; document steps VDR-U30-C143 VDR-U30-C144 VDR-U30-C145 VDR-U30-C146 VDR-U30-C147 VDR-U30-C148 VDR-U30-C149 VDR-U30-C150; alignment VDR-U30-C151 VDR-U30-C152 VDR-U30-C153 VDR-U30-C154; distribution VDR-U30-C155 VDR-U30-C156 VDR-U30-C157; repartition VDR-U30-C158 VDR-U30-C159; line figures VDR-U30-C160 VDR-U30-C161 VDR-U30-C162.

### D3 Source/technical/workflow logic
1. Per line: raw tax and base, rounded per currency only in per-line mode VDR-U30-C137 VDR-U30-C138.
2. Rounding entry rounds raw values VDR-U30-C140, applies manual amounts VDR-U30-C141, sums VDR-U30-C142.
3. Steps in order VDR-U30-C143: tax amounts per tax group VDR-U30-C144 VDR-U30-C145; base per line VDR-U30-C146 VDR-U30-C147 VDR-U30-C148 VDR-U30-C149; alignment to existing tax items VDR-U30-C151.
4. Distribution of any delta VDR-U30-C155 VDR-U30-C156; repartition lines VDR-U30-C158.
5. Item writing adds the delta to the base item balance VDR-U30-C150; line subtotal excludes it VDR-U30-C160.

State list:
- `raw amounts -> rounded amounts [round entry] VDR-U30-C140`
- `rounded -> adjusted [global steps, delta stored] VDR-U30-C150`
- `adjusted -> aligned to existing tax items [only when tax items supplied] VDR-U30-C151`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Two lines of 12.12 x 12.12 at 23 percent: line taxes 33.79 each, document tax 67.57, delta spread VDR-U30-C338 VDR-U30-C145. |
| 2 | Reversal / negative path | Refund flag is part of every group key so credit notes round on their own VDR-U30-C144; negative amounts distribute with sign VDR-U30-C155. |
| 3 | Multi-company / data scope | Method is a company setting (root company for rates only) VDR-U30-C135; currency precision per currency (DB THB 0.01). |
| 4 | Side effects and cross-module | Same engine for orders, expenses, loyalty and EDI (TXA1); delta consumed by totals VDR-U30-C210. |
| 5 | Configuration and optionality | Method default global VDR-U30-C135; caller may override for a single computation VDR-U30-C137. |
| 6 | Validation and constraints | Manual alignment skipped for zero totals VDR-U30-C153; mixed price-include handling VDR-U30-C147. |
| 7 | Roles and permissions | Company field edited through accounting settings (TXA1); no role gate in engine. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none. |
| 9 | Exception and failure behaviour | Zero rate gives zero company amounts VDR-U30-C139; client preview lacks alignment VDR-U30-C154. |
| 10 | Accounting, audit, compliance | Rounded amounts equal posted amounts; statutory rounding agreement is separate VDR-U30-C163 (S12-08, see TXS-R1 rounding row); line subtotal versus balance difference VDR-U30-C162. |

### DB reconciliation (config only)
DB: company rounding method round_globally; THB and USD both 0.01; decimal-precision records Product Price 2, Discount 2, Payment Terms 6. OBSERVATION.

### Unknown / Runtime
- UNKNOWN: statutory fit of the rounding algorithm VDR-U30-C163. RT: multi-line THB documents with VAT and withholding under global rounding; client preview versus server.

## CAP-U30-05 Cash-rounding, early-payment, discount-allocation and balancing items

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Optional derived items that change how a document is rounded, discounted or balanced: cash-rounding item, early-payment-discount items (mixed mode) and payment-time discount items (included mode), discount-allocation items and the automatic balancing item. VDR-U30-C339 VDR-U30-C199

### D2 Architecture, data, objects
- Cash rounding VDR-U30-C164 VDR-U30-C165 VDR-U30-C166 VDR-U30-C167 VDR-U30-C168 VDR-U30-C169 VDR-U30-C170 VDR-U30-C171 VDR-U30-C172 VDR-U30-C173 VDR-U30-C174 VDR-U30-C175; early payment items VDR-U30-C180 VDR-U30-C181 VDR-U30-C182 VDR-U30-C183 VDR-U30-C184 VDR-U30-C185 VDR-U30-C186 VDR-U30-C187 VDR-U30-C188; payment-time discount VDR-U30-C190 VDR-U30-C191 VDR-U30-C192 VDR-U30-C193 VDR-U30-C194 VDR-U30-C195; discount allocation VDR-U30-C196 VDR-U30-C197 VDR-U30-C198; balancing VDR-U30-C199 VDR-U30-C200 VDR-U30-C201 VDR-U30-C202 VDR-U30-C331.

### D3 Source/technical/workflow logic
1. Cash rounding after tax items in the chain (entry 30) VDR-U30-C171: total of non-term items VDR-U30-C166; difference VDR-U30-C167; strategy build VDR-U30-C169 VDR-U30-C170.
2. Early-payment items (entry 70): needs VDR-U30-C180; per group amounts VDR-U30-C183; counterpart VDR-U30-C184; distribution VDR-U30-C185.
3. Discount allocation (entry 40) VDR-U30-C198.
4. Balancing (entry 20) VDR-U30-C199.
5. Payment registration (U12) calls the included-mode helper VDR-U30-C190 VDR-U30-C192.

State list:
- `no rounding item -> rounding item [difference non-zero, draft] VDR-U30-C172`
- `rounding item -> deleted [method removed, strategy changed, zero difference] VDR-U30-C164 VDR-U30-C165 VDR-U30-C168`
- `no balancing item -> balancing item [entry with taxes unbalanced, not posted] VDR-U30-C199`
- `posted -> none of these are recomputed VDR-U30-C171 VDR-U30-C331`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | A 0.05-coin method rounds the total up by 0.03 with an extra item on the profit account VDR-U30-C170. |
| 2 | Reversal / negative path | Method removal deletes the item VDR-U30-C164; credit notes use the same method with opposite sign (sign in base lines, CAP-U30-03). |
| 3 | Multi-company / data scope | Profit and loss accounts are company-dependent VDR-U30-C170; discount accounts are company fields VDR-U30-C196. |
| 4 | Side effects and cross-module | Rounding item is a base item for taxes VDR-U30-C090; payment registration generates discount items VDR-U30-C190. |
| 5 | Configuration and optionality | Cash rounding group-gated VDR-U30-C177 VDR-U30-C178; early-payment modes per term VDR-U30-C189; discount allocation optional VDR-U30-C196. |
| 6 | Validation and constraints | Coin above zero VDR-U30-C175; early discount only on single 100 percent line VDR-U30-C086; missing profit account only warns VDR-U30-C173. |
| 7 | Roles and permissions | Cash rounding ACL VDR-U30-C176; DB: 2 rows (invoicing full, read-only read) VDR-U30-C179. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none. |
| 9 | Exception and failure behaviour | Largest-tax strategy without tax gives no item VDR-U30-C169; unknown cases VDR-U30-C340. |
| 10 | Accounting, audit, compliance | Rounding amounts post to profit, loss or tax accounts; converted at market rate on the invoice date VDR-U30-C167; discount items at payment go to gain or loss discount accounts VDR-U30-C191. |

### DB reconciliation (config only)
DB: 0 cash-rounding methods; discount allocation accounts both unset; early-payment loss and gain accounts set; 10 payment terms, all included mode; exchange journal and both exchange accounts set. OBSERVATION VDR-U30-C179 VDR-U30-C189 VDR-U30-C327.

### Unknown / Runtime
- RT: cash-rounding behaviours listed VDR-U30-C340; rounding-item rate difference VDR-U30-C217.

## CAP-U30-06 Document tax totals summary (display, edit, stored versus recomputed)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 Business purpose and process semantics
Compute and present the document tax totals (untaxed, tax per group, rounding, total) in both currencies for display and printing, allow a controlled manual edit, and distinguish stored amounts from recomputed structure. VDR-U30-C341 VDR-U30-C205

### D2 Architecture, data, objects
- Field and inverse VDR-U30-C203 VDR-U30-C204 VDR-U30-C220; computation VDR-U30-C205 VDR-U30-C206 VDR-U30-C207 VDR-U30-C208; engine VDR-U30-C209 VDR-U30-C210 VDR-U30-C211 VDR-U30-C212 VDR-U30-C213 VDR-U30-C214 VDR-U30-C215 VDR-U30-C216 VDR-U30-C218 VDR-U30-C219; stored VDR-U30-C223 VDR-U30-C224; print VDR-U30-C225 VDR-U30-C226 VDR-U30-C227; orders VDR-U30-C228 VDR-U30-C229.

### D3 Source/technical/workflow logic
1. Base lines from the document with existing tax items kept VDR-U30-C205.
2. Global totals then per tax group VDR-U30-C209 VDR-U30-C212; subtotal labels and accumulation VDR-U30-C213 VDR-U30-C215.
3. Cash rounding items read or estimated VDR-U30-C216; subtract and add back VDR-U30-C218.
4. Non-deductible subtraction (TXA1-C076); total VDR-U30-C219.
5. Edit path: widget writes the summary, inverse adjusts the first tax item VDR-U30-C220; payment-term derivation always re-run VDR-U30-C221.

State list:
- `document opened -> summary recomputed from items [dependencies change] VDR-U30-C204`
- `draft vendor document, summary edited -> first tax item of group changed VDR-U30-C220`
- `any -> printed from the summary VDR-U30-C225`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Invoice with VAT 7 percent: Untaxed Amount subtotal, VAT 7 percent row, Total VDR-U30-C213 VDR-U30-C225. |
| 2 | Reversal / negative path | Credit notes show positive amounts via direction sign VDR-U30-C113; summary absent for entries VDR-U30-C206. |
| 3 | Multi-company / data scope | Company currency block per company option VDR-U30-C208; groups are company records (rule in DB). |
| 4 | Side effects and cross-module | Orders reuse the engine VDR-U30-C228 VDR-U30-C229; prints reuse generic blocks VDR-U30-C226. |
| 5 | Configuration and optionality | Company-currency option default true VDR-U30-C208; group sequence and label drive layout VDR-U30-C214. |
| 6 | Validation and constraints | Edit allowed only in draft on vendor documents or quick encoding VDR-U30-C222. |
| 7 | Roles and permissions | No dedicated group; edit is a draft-state view rule VDR-U30-C222; cash rounding read with elevated rights VDR-U30-C205. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none. |
| 9 | Exception and failure behaviour | Summary not stored so no staleness; edit side effects VDR-U30-C221. |
| 10 | Accounting, audit, compliance | Stored amounts equal item sums VDR-U30-C223; statutory presentation VDR-U30-C230 (S12-08, S12-04 are statutory questions). |

### DB reconciliation (config only)
DB: 5 tax groups (WHT 1, 2, 3, 5 percent and VAT 7 percent) all at sequence 10, no preceding subtotal, all with a payable account; company option for taxes in company currency true. Zero-rated and exempt VAT taxes (ids 3 to 6) sit in group WHT 1% VDR-U30-C354; template leaves their group empty VDR-U30-C353; default rule VDR-U30-C352; display consequence VDR-U30-C355. OBSERVATION VDR-U30-C214 VDR-U30-C208.

### Unknown / Runtime
- UNKNOWN: statutory layout fit VDR-U30-C230; RT: printed output and the zero-rated/exempt group display VDR-U30-C355; client versus server equality.

## CAP-U30-07 Cash-basis tax exigibility, end to end

**Function-ID(s):** FUNCTION MAPPING REQUIRED (statutory context S05-01, S05-02 for the tax point; not asserted).

### D1 Business purpose and process semantics
Defer tax reporting and booking of selected taxes until payment: transition account at invoice, cash-basis entry per reconciliation, reversal on unreconcile. VDR-U30-C342

### D2 Architecture, data, objects
- Configuration VDR-U30-C231 VDR-U30-C232 VDR-U30-C233 VDR-U30-C234 VDR-U30-C235 VDR-U30-C236; Thai data VDR-U30-C237 VDR-U30-C238; invoice-time effect VDR-U30-C239 VDR-U30-C240 VDR-U30-C241 VDR-U30-C242; collection VDR-U30-C243 VDR-U30-C244 VDR-U30-C245 VDR-U30-C246 VDR-U30-C247; trigger VDR-U30-C248 VDR-U30-C249 VDR-U30-C250 VDR-U30-C251 VDR-U30-C252 VDR-U30-C253 VDR-U30-C254; per-partial values VDR-U30-C255 VDR-U30-C256 VDR-U30-C257 VDR-U30-C258 VDR-U30-C259; creation VDR-U30-C260 VDR-U30-C261 VDR-U30-C262 VDR-U30-C263 VDR-U30-C264 VDR-U30-C265 VDR-U30-C266 VDR-U30-C267 VDR-U30-C268 VDR-U30-C269 VDR-U30-C270 VDR-U30-C271 VDR-U30-C272 VDR-U30-C273 VDR-U30-C274; draft handling VDR-U30-C275; reversal VDR-U30-C276 VDR-U30-C277 VDR-U30-C278 VDR-U30-C279; UI VDR-U30-C280; reporting VDR-U30-C281 VDR-U30-C282 VDR-U30-C283 VDR-U30-C284; roles VDR-U30-C285.

### D3 Source/technical/workflow logic
1. Invoice posted: items of on-payment taxes sit on the transition account, without report tags VDR-U30-C239 VDR-U30-C240.
2. Reconcile: plan creates partials, then hook VDR-U30-C248 unless cancelling or disabled VDR-U30-C249.
3. Collect values per move VDR-U30-C243 VDR-U30-C245 VDR-U30-C246; per partial percentage VDR-U30-C257 VDR-U30-C258 and rate VDR-U30-C259.
4. Build entry: date VDR-U30-C260; amounts VDR-U30-C262 VDR-U30-C263 VDR-U30-C264; base and tax items VDR-U30-C265 VDR-U30-C267; counterparts VDR-U30-C266 VDR-U30-C268; grouping VDR-U30-C269.
5. Create without synchronisation, post if both posted VDR-U30-C271 VDR-U30-C272; reconcile transition lines VDR-U30-C270 VDR-U30-C273; store snapshot VDR-U30-C251.
6. Later: posting a draft side checks snapshot VDR-U30-C275; undoing a match reverses VDR-U30-C276 VDR-U30-C277.

State list:
- `invoice posted -> tax on transition account [on-payment tax] VDR-U30-C239`
- `partial or full reconcile -> cash-basis entry created [switch on, on-payment items] VDR-U30-C248 VDR-U30-C272`
- `draft entry -> posted [both sides posted] VDR-U30-C275`
- `matching undone -> entry reversed (posted) or deleted (draft) VDR-U30-C276`
- `cash-basis entry posted -> cannot be drafted or deleted VDR-U30-C278 VDR-U30-C279`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Invoice 107 with 7 percent on-payment VAT, payment 53.5: entry for 50 percent of base and tax dated at payment VDR-U30-C257 VDR-U30-C260. Not exercised in the Thai tax set (none on payment). |
| 2 | Reversal / negative path | Unreconcile reverses entries VDR-U30-C276; cancelling reversal creates none VDR-U30-C249; credit note against invoice uses own rates VDR-U30-C255. |
| 3 | Multi-company / data scope | Switch delegated to root VDR-U30-C234; partial company is the invoice side (U12); same-root rule on reconciliation (U12); journal from partial company VDR-U30-C253. |
| 4 | Side effects and cross-module | Expense payments request cash-basis tags VDR-U30-C131; exchange entries always exigible VDR-U30-C326; reports flag VDR-U30-C283. |
| 5 | Configuration and optionality | Tax option, company switch, journal, base account VDR-U30-C231 VDR-U30-C233; Thai template switch VDR-U30-C237. |
| 6 | Validation and constraints | Transition account reconcilable VDR-U30-C232; no mixing sharing tags VDR-U30-C242; multiple currencies skipped VDR-U30-C246; journal required VDR-U30-C253. |
| 7 | Roles and permissions | Matching ACL VDR-U30-C285; entry created under the reconciling user; settings visible to accounting user group (view). |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none; entries arise only from matching. |
| 9 | Exception and failure behaviour | Missing journal -> error VDR-U30-C253; dead branch VDR-U30-C274; base drift VDR-U30-C343. |
| 10 | Accounting, audit, compliance | Dated no earlier than day after lock VDR-U30-C260; tags on entry only VDR-U30-C240; transition lines reconciled VDR-U30-C270; statutory tax point not asserted (S05-01, S05-02). |

### DB reconciliation (config only)
DB: company switch true; CABA journal exists and is set on the company; base-tracking account not set; 18 taxes, all on invoice, none with a transition account; account partial reconcile ACL rows 6; six account reports all with only-exigible true; crons none relevant. OBSERVATION VDR-U30-C238 VDR-U30-C284 VDR-U30-C285.

### Unknown / Runtime
- UNKNOWN/RT: report-engine treatment of exigibility VDR-U30-C286; tax-account rounding branch VDR-U30-C274; base drift VDR-U30-C343; Thai VAT on payment requirement (statutory).

## CAP-U30-08 Tax items on credit note, switch, reset, cancel and fiscal-position change

**Function-ID(s):** FUNCTION MAPPING REQUIRED (PCO-F01 for lock-date interplay, see CAP-U30-01).

### D1 Business purpose and process semantics
What happens to derived tax items when an invoice is reversed into a credit note, switched in type, reset to draft, cancelled, or when its fiscal position changes after items exist. VDR-U30-C344

### D2 Architecture, data, objects
- Reversal VDR-U30-C287 VDR-U30-C288 VDR-U30-C289 VDR-U30-C290 VDR-U30-C291 VDR-U30-C292 VDR-U30-C293 VDR-U30-C294 VDR-U30-C295; switch VDR-U30-C296 VDR-U30-C297 VDR-U30-C298; reset and cancel VDR-U30-C299 VDR-U30-C300; fiscal position VDR-U30-C301 VDR-U30-C302 VDR-U30-C303 VDR-U30-C304 VDR-U30-C305 VDR-U30-C306 VDR-U30-C307; expense override VDR-U30-C348.

### D3 Source/technical/workflow logic
1. Credit note by wizard: copy with type change, items copied VDR-U30-C287 VDR-U30-C288; payment term only if mixed VDR-U30-C294.
2. Cancelling reversal: unreconcile originals, copy, negate (entries only), post, reconcile VDR-U30-C289 VDR-U30-C291 VDR-U30-C292.
3. Reverse-and-modify: only product and section lines copied VDR-U30-C293.
4. Switch type: rewrite type, currency, fiscal position VDR-U30-C296 VDR-U30-C297.
5. Reset and cancel VDR-U30-C299 VDR-U30-C300.
6. Fiscal position change: onchange flag, explicit action recomputes VDR-U30-C304 VDR-U30-C305; automatic default only on product or unit change VDR-U30-C302.

State list:
- `posted invoice -> credit note draft [reverse] VDR-U30-C287`
- `draft invoice -> draft credit note [switch type, unnumbered] VDR-U30-C296`
- `posted -> draft [reset] VDR-U30-C299`
- `draft -> cancelled [cancel] VDR-U30-C300`
- `draft with changed fiscal position -> taxes remapped [update action] VDR-U30-C305`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Reverse invoice: credit note draft with copied items, refund distribution lines; post and match later VDR-U30-C295 VDR-U30-C112. |
| 2 | Reversal / negative path | This capability is the reversal path; cash-basis entries dissolve on unreconcile (CAP-U30-07). |
| 3 | Multi-company / data scope | Tax country check per move VDR-U30-C307; fiscal position per company (finder, U13). |
| 4 | Side effects and cross-module | Expense links cleared VDR-U30-C348; payments synchronised (U11/U12). |
| 5 | Configuration and optionality | Credit-note payment term only in mixed mode VDR-U30-C294; refund sequences (U11). |
| 6 | Validation and constraints | Switch refused when numbered VDR-U30-C298; fiscal position update hidden after posting VDR-U30-C306. |
| 7 | Roles and permissions | Reset and cancel need the invoicing role (U11/TXA2); update-taxes action has no group; reversal wizard group per U11. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - none (auto-post cron only posts). |
| 9 | Exception and failure behaviour | Locks block date changes and item changes VDR-U30-C030 VDR-U30-C042; unknown copy outcome VDR-U30-C345. |
| 10 | Accounting, audit, compliance | Reversal keeps original period unless locked (U12/TXA2); statutory credit-note content S07-02 not derived from Odoo behaviour. |

### DB reconciliation (config only)
DB: no documents; fiscal position finder configuration per TXA1 (no domestic fiscal position); no purchase-receipt fiscal position. OBSERVATION (config only).

### Unknown / Runtime
- RT: credit-note tax amounts copied or recomputed VDR-U30-C345.

## CAP-U30-09 Multi-currency tax items, rate date and exchange interplay

**Function-ID(s):** FUNCTION MAPPING REQUIRED (statutory links S12-03, S12-04 for the rate row).

### D1 Business purpose and process semantics
Carry tax items in document and company currency, choose the rate and its date, and relate tax items to exchange differences. VDR-U30-C346 VDR-U30-C308

### D2 Architecture, data, objects
- Rate VDR-U30-C308 VDR-U30-C309 VDR-U30-C310 VDR-U30-C311 VDR-U30-C312 VDR-U30-C313 VDR-U30-C314 VDR-U30-C315 VDR-U30-C347; rate tables VDR-U30-C316 VDR-U30-C317 VDR-U30-C318 VDR-U30-C319; items VDR-U30-C320 VDR-U30-C321 VDR-U30-C322 VDR-U30-C323 VDR-U30-C139 VDR-U30-C140; terms VDR-U30-C324; cash basis VDR-U30-C325 VDR-U30-C326 VDR-U30-C327; unknown VDR-U30-C328.

### D3 Source/technical/workflow logic
1. Expected rate on the rate date VDR-U30-C308 VDR-U30-C309; stored on invoice-like moves, recomputed when its inputs change VDR-U30-C312.
2. Base lines carry the rate VDR-U30-C323; engine divides document amounts by it VDR-U30-C139; rounding per currency VDR-U30-C140.
3. Line synchroniser derives balance from foreign amount over rate VDR-U30-C322.
4. Payment terms and cash rounding convert separately VDR-U30-C324 VDR-U30-C167.
5. Matching posts exchange differences VDR-U30-C326; cash-basis uses payment rate VDR-U30-C325.

State list:
- `draft rate = expected -> draft rate edited [user] VDR-U30-C311`
- `rate edited -> foreign amounts kept, company amounts re-derived VDR-U30-C100`
- `currency changed -> full recomputation VDR-U30-C096`

### Ten dimensions
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | USD invoice on a date with a loaded rate: tax in USD, company amounts at that rate VDR-U30-C312 VDR-U30-C139. |
| 2 | Reversal / negative path | Credit note takes its own rate by its invoice date VDR-U30-C308; reversal wizard sets invoice date (CAP-U30-08). |
| 3 | Multi-company / data scope | Rates resolved against the root company VDR-U30-C317; rate rows rule in DB. |
| 4 | Side effects and cross-module | Cash rounding and terms convert independently VDR-U30-C324 VDR-U30-C167; cash basis uses payment rate VDR-U30-C325; exchange entries VDR-U30-C326. |
| 5 | Configuration and optionality | Multi-currency group shows currency and rate VDR-U30-C347; rates must be loaded VDR-U30-C318. |
| 6 | Validation and constraints | Rate strictly positive VDR-U30-C313. |
| 7 | Roles and permissions | Rate edit follows the draft view rule and multi-currency group VDR-U30-C347; res.currency ACL 5 rows and rate ACL 5 rows in dump. |
| 8 | Scheduled / automated behaviour | NOT APPLICABLE - rate feeds were not read (UNKNOWN whether an installed module schedules rate updates). |
| 9 | Exception and failure behaviour | No rate rows -> rate 1 VDR-U30-C316 VDR-U30-C318; zero rate -> zero company amounts VDR-U30-C139. |
| 10 | Accounting, audit, compliance | Company amounts depend on rate source; statutory rate and date rules are separate (S12-03, S12-04); supply date does not enter the rate date VDR-U30-C310. |

### DB reconciliation (config only)
DB: THB and USD active, both rounding 0.01; res.currency.rate has zero rows; exchange journal EXCH set with gain and loss accounts; CABA journal set. OBSERVATION VDR-U30-C318.

### Unknown / Runtime
- RT: VDR-U30-C328; whether any installed module schedules automatic rate loading is not read.

---

## REGISTER: Function Catalog

Cat-IDs are candidate catalogue ids, not Function-IDs. Native status vocabulary: NATIVE, PARTIAL, NATIVE GAP / EXTENSION REQUIRED, UNKNOWN. Where PARTIAL is shown, the mechanism is native but a Thai-specific configuration or statutory fit is pending TXS validation; absence in Community source is not proof that no business requirement exists.

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Entry points / triggers | Claim-IDs | Statutory link (statutory-register id or n/a) | Native status |
|---|---|---|---|---|---|---|---|
| U30-F01 | Synchronise derived journal items on create, change and delete of documents and items | 1, 7 | FUNCTION MAPPING REQUIRED | account.move create/write/unlink; account.move.line create/write/unlink; _sync_dynamic_lines stack; post | VDR-U30-C001 VDR-U30-C006 VDR-U30-C007 VDR-U30-C011 VDR-U30-C012 VDR-U30-C055 VDR-U30-C060 VDR-U30-C018 VDR-U30-C025 VDR-U30-C038 | n/a | NATIVE |
| U30-F02 | Derive due-date (payment-term) items | 6, 7 | FUNCTION MAPPING REQUIRED | _compute_needed_terms; _sync_dynamic_line(term_key) | VDR-U30-C067 VDR-U30-C073 VDR-U30-C081 VDR-U30-C074 VDR-U30-C078 | n/a | NATIVE |
| U30-F03 | Generate and update tax items from base items | 1, 2, 3 | FUNCTION MAPPING REQUIRED | _sync_tax_lines; _get_rounded_base_and_tax_lines; account.tax._prepare_tax_lines | VDR-U30-C101 VDR-U30-C096 VDR-U30-C120 VDR-U30-C118 VDR-U30-C121 | n/a | NATIVE |
| U30-F04 | Keep or recompute hand-edited tax amounts | 1, 6 | FUNCTION MAPPING REQUIRED | _sync_tax_lines branch tree; _round_tax_details_tax_amounts_from_tax_lines | VDR-U30-C098 VDR-U30-C097 VDR-U30-C099 VDR-U30-C151 VDR-U30-C152 | n/a | NATIVE |
| U30-F05 | Allocate rounding per line or globally, in both currencies | 6 | FUNCTION MAPPING REQUIRED | account.tax._round_base_lines_tax_details and helpers; company tax_calculation_rounding_method | VDR-U30-C145 VDR-U30-C146 VDR-U30-C155 VDR-U30-C150 VDR-U30-C135 VDR-U30-C163 | S12-08 | NATIVE |
| U30-F06 | Cash-rounding item | 6 | FUNCTION MAPPING REQUIRED | _recompute_cash_rounding_lines via _sync_rounding_lines | VDR-U30-C166 VDR-U30-C169 VDR-U30-C170 VDR-U30-C167 | n/a | NATIVE |
| U30-F07 | Early-payment-discount items on the document (mixed mode) | 6 | FUNCTION MAPPING REQUIRED | line epd_needed; _sync_dynamic_line(epd_key) | VDR-U30-C180 VDR-U30-C183 VDR-U30-C184 VDR-U30-C185 | n/a | NATIVE |
| U30-F08 | Early-payment-discount settlement at payment (included mode) | 6, 7 | FUNCTION MAPPING REQUIRED | _get_invoice_counterpart_amls_for_early_payment_discount* | VDR-U30-C190 VDR-U30-C192 VDR-U30-C194 VDR-U30-C191 | n/a | NATIVE |
| U30-F09 | Discount-allocation items | 6 | FUNCTION MAPPING REQUIRED | line discount_allocation_needed; company discount accounts | VDR-U30-C196 VDR-U30-C197 VDR-U30-C198 | n/a | NATIVE |
| U30-F10 | Private-part (non-deductible) items on vendor bills | 3 | FUNCTION MAPPING REQUIRED | _sync_non_deductible_base_lines; _sync_tax_lines non-deductible branch | VDR-U30-C124 VDR-U30-C126 VDR-U30-C122 VDR-U30-C127 | n/a | NATIVE |
| U30-F11 | Automatic balancing item on entries using taxes | 1, 7 | FUNCTION MAPPING REQUIRED | _sync_unbalanced_lines | VDR-U30-C199 VDR-U30-C200 VDR-U30-C201 | n/a | NATIVE |
| U30-F12 | Document tax totals summary (both currencies) | 1, 6 | FUNCTION MAPPING REQUIRED | account.move.tax_totals; account.tax._get_tax_totals_summary; invoice print | VDR-U30-C205 VDR-U30-C209 VDR-U30-C213 VDR-U30-C219 VDR-U30-C225 | n/a | NATIVE |
| U30-F13 | Edit a tax-group amount in the totals summary | 6 | FUNCTION MAPPING REQUIRED | account.move._inverse_tax_totals; form widget | VDR-U30-C220 VDR-U30-C222 VDR-U30-C221 | n/a | NATIVE |
| U30-F14 | Taxes in company currency block for foreign-currency sales | 6 | FUNCTION MAPPING REQUIRED | tax_totals display_in_company_currency; company option | VDR-U30-C207 VDR-U30-C208 VDR-U30-C227 | S12-02 | NATIVE |
| U30-F15 | Cash-basis configuration (tax option, company switch, journal, accounts) | 5, 7 | FUNCTION MAPPING REQUIRED | account.tax; res.company; settings; chart template load; l10n_th template data | VDR-U30-C231 VDR-U30-C232 VDR-U30-C233 VDR-U30-C235 VDR-U30-C236 VDR-U30-C237 | n/a | PARTIAL |
| U30-F16 | Cash-basis entry creation at reconciliation | 5, 7 | FUNCTION MAPPING REQUIRED | account.move.line._reconcile_plan_with_sync; account.partial.reconcile._create_tax_cash_basis_moves | VDR-U30-C248 VDR-U30-C257 VDR-U30-C260 VDR-U30-C267 VDR-U30-C272 | S05-01, S05-02 | PARTIAL |
| U30-F17 | Cash-basis entry reversal on unreconcile and cancel | 7 | FUNCTION MAPPING REQUIRED | account.partial.reconcile.unlink; button_cancel; _reverse_moves(cancel) | VDR-U30-C276 VDR-U30-C277 VDR-U30-C278 VDR-U30-C279 VDR-U30-C300 | n/a | NATIVE |
| U30-F18 | Credit note creation and its effect on tax items | 4, 7 | FUNCTION MAPPING REQUIRED | account.move.reversal wizard; _reverse_moves; copy_data | VDR-U30-C287 VDR-U30-C288 VDR-U30-C293 VDR-U30-C294 | S07-02 | NATIVE |
| U30-F19 | Switch a draft between invoice and credit note | 4 | FUNCTION MAPPING REQUIRED | action_switch_move_type | VDR-U30-C296 VDR-U30-C297 VDR-U30-C298 | n/a | NATIVE |
| U30-F20 | Reset to draft and cancel: effect on tax and due-date items | 7 | FUNCTION MAPPING REQUIRED | button_draft; button_cancel | VDR-U30-C299 VDR-U30-C300 | n/a | NATIVE |
| U30-F21 | Fiscal-position change after items exist (update action) | 8 | FUNCTION MAPPING REQUIRED | action_update_fpos_values; _compute_tax_ids | VDR-U30-C302 VDR-U30-C304 VDR-U30-C305 VDR-U30-C306 | n/a | PARTIAL |
| U30-F22 | Multi-currency tax conversion and rate date | 6 | FUNCTION MAPPING REQUIRED | invoice_currency_rate; res.currency._get_conversion_rate | VDR-U30-C308 VDR-U30-C312 VDR-U30-C316 VDR-U30-C318 VDR-U30-C310 | S12-03, S12-04 | PARTIAL |
| U30-F23 | Expense-originated tax items and due-date item | 12 | FUNCTION MAPPING REQUIRED | hr_expense overrides of account.move and account.tax hooks | VDR-U30-C088 VDR-U30-C129 VDR-U30-C130 VDR-U30-C131 | n/a | NATIVE |
| U30-F24 | Imported electronic invoice tax alignment | 12 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii _import_invoice_fix_taxes_amounts | VDR-U30-C132 VDR-U30-C133 VDR-U30-C134 | n/a | NATIVE |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Claim-IDs | Class |
|---|---|---|---|---|
| U30-BR01 | Derived items are re-derived by a fixed chain with numbered positions; recomputation after a change runs in reverse position order (INFERENCE) | always | VDR-U30-C001 VDR-U30-C005 VDR-U30-C006 | Calculation |
| U30-BR02 | Only the outermost create, write or unlink asserts balance; nested system operations do not (INFERENCE) | check_move_validity default True | VDR-U30-C011 VDR-U30-C012 VDR-U30-C013 | Constraint |
| U30-BR03 | Changes made by the synchronisation do not synchronise again | recursion guard on cursor cache | VDR-U30-C007 VDR-U30-C009 | Calculation |
| U30-BR04 | If needs are unchanged, or items were created by hand with no previous need, existing items are not touched | always | VDR-U30-C055 VDR-U30-C056 | Default |
| U30-BR05 | An item to delete and an item to create are merged into an in-place rewrite | always | VDR-U30-C060 | Calculation |
| U30-BR06 | Tax items are re-derived only for drafts | document state | VDR-U30-C095 VDR-U30-C331 VDR-U30-C171 | Constraint |
| U30-BR07 | Posted documents cannot write items, date, partner, term, currency, fiscal position, cash rounding | skip_readonly_check unset | VDR-U30-C028 VDR-U30-C029 | Constraint |
| U30-BR08 | Users cannot delete tax items (while taxes exist) or payment-term items; only synchronisation can | dynamic_unlink unset | VDR-U30-C047 | Constraint |
| U30-BR09 | Posted-item changes are checked against tax and fiscal locks; protected-field changes of matched items unreconcile them | posted parent / matched item | VDR-U30-C041 VDR-U30-C042 VDR-U30-C043 VDR-U30-C044 | Constraint |
| U30-BR10 | Instalments are keyed by due and discount date; the last instalment takes the remainder in both currencies | payment term | VDR-U30-C074 VDR-U30-C081 | Calculation |
| U30-BR11 | Percent instalments round independently per currency; fixed instalments convert by the totals-implied rate | payment term | VDR-U30-C083 VDR-U30-C082 VDR-U30-C080 | Calculation |
| U30-BR12 | With cash rounding every non-last instalment is rounded to the coin | cash rounding set | VDR-U30-C084 | Calculation |
| U30-BR13 | Early discount only on a single 100 percent line with positive percentage and days | always | VDR-U30-C086 | Constraint |
| U30-BR14 | A receivable account is used only by payment-term items on sales documents (mirror for purchases) | always | VDR-U30-C087 | Constraint |
| U30-BR15 | Without a payment term one item is derived at the due date | no payment term | VDR-U30-C075 VDR-U30-C334 | Default |
| U30-BR16 | Tax items are recomputed when base inputs, currency, type or rate change | draft invoice-like | VDR-U30-C092 VDR-U30-C096 VDR-U30-C100 | Calculation |
| U30-BR17 | Manual tax amounts are kept when the change does not involve taxes, when tax items changed or are protected; documents created with all amounts are not recomputed | draft | VDR-U30-C098 VDR-U30-C097 VDR-U30-C099 | Default |
| U30-BR18 | Tax items are matched by identity: first updated, duplicates deleted, zero dropped, unmatched created | always | VDR-U30-C120 VDR-U30-C119 VDR-U30-C117 | Calculation |
| U30-BR19 | Item amount = direction sign x computed amount; credit notes use refund distribution lines; entries use typed amounts as tax-excluded | always | VDR-U30-C111 VDR-U30-C113 VDR-U30-C112 VDR-U30-C109 | Calculation |
| U30-BR20 | Tax item analytic distribution is inherited only for analytic taxes or non-closing distribution lines | always | VDR-U30-C116 | Configuration |
| U30-BR21 | Private-part items are derived for draft purchase documents with deductibility below 100 | draft purchase | VDR-U30-C124 VDR-U30-C126 VDR-U30-C125 | Calculation |
| U30-BR22 | Partial deductibility is exposed through a permission group granted on posting | bill with deductibility under 100 | VDR-U30-C336 | Configuration |
| U30-BR23 | No taxes on off-balance accounts | off-balance account | VDR-U30-C337 | Constraint |
| U30-BR24 | Rounding method is a company choice, default global | company setting | VDR-U30-C135 VDR-U30-C136 | Configuration |
| U30-BR25 | Global rounding shares the document-level difference over lines in whole smallest units | round_globally | VDR-U30-C145 VDR-U30-C146 | Calculation |
| U30-BR26 | Delta distribution is proportional to size, largest first, remainder one each to the largest, equal weights if all zero | always | VDR-U30-C155 VDR-U30-C156 | Calculation |
| U30-BR27 | Line subtotal excludes the global delta, the base item balance includes it | round_globally | VDR-U30-C160 VDR-U30-C162 | Risk |
| U30-BR28 | Existing tax items become the target per tax, currency and refund flag (not per distribution line) | tax items kept | VDR-U30-C151 VDR-U30-C152 VDR-U30-C153 | Calculation |
| U30-BR29 | Client-side engine lacks alignment to existing tax items | client preview | VDR-U30-C154 | Risk |
| U30-BR30 | Cash rounding amount, strategies and removal rules | cash rounding method | VDR-U30-C166 VDR-U30-C169 VDR-U30-C170 VDR-U30-C164 VDR-U30-C168 | Calculation |
| U30-BR31 | Rounding item company amount uses market rate at invoice date; totals estimate uses implied rate | foreign currency | VDR-U30-C167 VDR-U30-C217 | Risk |
| U30-BR32 | Cash rounding is group-gated and read-only after draft | always | VDR-U30-C177 VDR-U30-C178 VDR-U30-C176 | Configuration |
| U30-BR33 | Mixed early-payment items are derived per account, analytic and tax group, excluding fixed taxes | mixed mode | VDR-U30-C180 VDR-U30-C183 VDR-U30-C182 | Calculation |
| U30-BR34 | Included early-payment discount is settled at payment by base and tax correction items | included mode | VDR-U30-C190 VDR-U30-C192 VDR-U30-C191 | Calculation |
| U30-BR35 | Discount-allocation items exist only when company discount accounts are configured | company fields | VDR-U30-C196 VDR-U30-C197 | Configuration |
| U30-BR36 | Automatic balancing item only for non-posted entries using taxes | entries | VDR-U30-C199 VDR-U30-C200 VDR-U30-C331 | Default |
| U30-BR37 | Totals summary is untaxed + tax per group + rounding = total in both currencies | invoice-like | VDR-U30-C209 VDR-U30-C219 VDR-U30-C218 | Calculation |
| U30-BR38 | Tax groups ordered by sequence then id under preceding-subtotal labels | always | VDR-U30-C212 VDR-U30-C213 VDR-U30-C214 | Configuration |
| U30-BR39 | Summary editable only in draft on vendor documents or quick encoding; edit changes the first tax item of the group | form view | VDR-U30-C222 VDR-U30-C220 | Constraint |
| U30-BR40 | Company-currency summary for foreign-currency sales documents when the company option is on | company option | VDR-U30-C207 VDR-U30-C208 | Configuration |
| U30-BR41 | Amounts stored as item amounts and document fields; summary recomputed | always | VDR-U30-C223 VDR-U30-C203 | Default |
| U30-BR42 | A tax without a group takes the first tax group of its country; Thai zero-rated and exempt VAT end up in the WHT 1% group | template leaves group empty | VDR-U30-C352 VDR-U30-C353 VDR-U30-C354 VDR-U30-C355 | Risk |
| U30-BR43 | Cash basis needs tax option, company switch, journal, reconcilable transition account; switch not removable while used | always | VDR-U30-C231 VDR-U30-C233 VDR-U30-C235 VDR-U30-C232 | Configuration |
| U30-BR44 | On-payment tax sits on the transition account without tags at invoice time | on-payment tax | VDR-U30-C239 VDR-U30-C240 | Calculation |
| U30-BR45 | Cash-basis entries triggered by reconciliation of receivable or payable when a company switch is on; skipped for cancelling reversals; skipped for multi-currency documents | reconcile | VDR-U30-C248 VDR-U30-C249 VDR-U30-C245 VDR-U30-C246 | Calculation |
| U30-BR46 | Percentage = partial over total (company or document currency); last partial of fully paid document takes tax residual | reconcile | VDR-U30-C257 VDR-U30-C258 VDR-U30-C263 | Calculation |
| U30-BR47 | Company amounts of cash-basis entries use the payment rate | reconcile | VDR-U30-C259 VDR-U30-C264 | Calculation |
| U30-BR48 | Cash-basis entry dated settlement date, not before day after fiscal lock | reconcile | VDR-U30-C260 VDR-U30-C255 VDR-U30-C256 | Calculation |
| U30-BR49 | Cash-basis lines: base on base account with base tags, tax on distribution account with tags, counterparts on original or transition account; aggregated by key | reconcile | VDR-U30-C265 VDR-U30-C267 VDR-U30-C266 VDR-U30-C268 VDR-U30-C269 | Calculation |
| U30-BR50 | Cash-basis entries posted if both documents posted, else draft; draft snapshot re-checked at posting | reconcile / post | VDR-U30-C272 VDR-U30-C275 VDR-U30-C252 | Default |
| U30-BR51 | Unreconcile reverses posted cash-basis entries and deletes draft ones; posted entries cannot be drafted or deleted | unreconcile | VDR-U30-C276 VDR-U30-C277 VDR-U30-C278 VDR-U30-C279 | Constraint |
| U30-BR52 | On-payment and on-invoice taxes may not share base tags on one item | always | VDR-U30-C242 | Constraint |
| U30-BR53 | A cash-basis journal must exist when an entry is needed | on-payment tax reconciled | VDR-U30-C253 | Constraint |
| U30-BR54 | Thai template turns the switch on while no tax is on payment | l10n_th installed | VDR-U30-C237 VDR-U30-C238 | Risk |
| U30-BR55 | Credit notes copy the items; reverse-and-modify copies only product and section lines; credit note keeps term only for mixed discount | reversal wizard | VDR-U30-C287 VDR-U30-C293 VDR-U30-C294 | Default |
| U30-BR56 | Switching type forces full recomputation and is refused when numbered | draft | VDR-U30-C296 VDR-U30-C298 | Constraint |
| U30-BR57 | Reset to draft keeps items | always | VDR-U30-C299 | Default |
| U30-BR58 | Fiscal position change does not recompute line taxes; the update action does | draft with items | VDR-U30-C302 VDR-U30-C305 VDR-U30-C306 | Risk |
| U30-BR59 | Document taxes must belong to the document tax country | always | VDR-U30-C307 | Constraint |
| U30-BR60 | Rate date is the invoice date, supply date not used | always | VDR-U30-C308 VDR-U30-C310 | Default |
| U30-BR61 | Rate lookup: latest on or before date, else earliest, else 1; no rate rows in dump | always | VDR-U30-C316 VDR-U30-C318 | Default |
| U30-BR62 | Invoice rate strictly positive | foreign currency invoice | VDR-U30-C313 | Constraint |
| U30-BR63 | Company amounts are document amounts divided by the rate; balance derived from foreign amount over rate | always | VDR-U30-C139 VDR-U30-C322 | Calculation |
| U30-BR64 | Imported e-invoice tax aligned within 0.03 tolerance | e-invoice import | VDR-U30-C132 VDR-U30-C133 | Calculation |
| U30-BR65 | Expense documents key tax items per expense and treat own-account expenses as price-included | hr_expense installed | VDR-U30-C129 VDR-U30-C130 VDR-U30-C088 | Configuration |

## REGISTER: Source and Override Map

Format `module:file:line`. Overrides are restricted to the 356 installed modules (dump list); non-installed Community add-ons are marked NOT installed. A row with none records a negative scan (method names and inheritance grepped across the installed modules).

| Concept | Base definition (module:file:line) | Overrides in installed Community modules (module:file:line) | Effective-behaviour condition | Claim-IDs |
|---|---|---|---|---|
| Dynamic-line synchronisation stack and generic manager | account:models/account_move.py:3722 (_get_sync_stack), :3591 (_sync_dynamic_line), :3767 (_sync_dynamic_lines) | none (negative scan for the method names over the 356 installed modules); callers only: account_edi_ubl_cii:models/account_edi_common.py:1717, :1797 | Base only | VDR-U30-C001 VDR-U30-C134 VDR-U30-C055 |
| Balance check and recursion guard | account:models/account_move.py:2781 (_check_balanced), :7052 (_disable_recursion) | none installed; setter in point_of_sale:models/pos_session.py:442 (NOT installed) | Base only; suppression key never set in the installed set | VDR-U30-C011 VDR-U30-C016 VDR-U30-C015 VDR-U30-C009 |
| Tax-item synchronisation | account:models/account_move.py:3287 (_sync_tax_lines); account:models/account_tax.py:3051 (_prepare_tax_lines) | none (negative scan) | Base only | VDR-U30-C090 VDR-U30-C101 VDR-U30-C120 |
| Payment-term needs | account:models/account_move.py:1389 (_compute_needed_terms) | hr_expense:models/account_move.py:73 (company-paid expenses) | Base, replaced for documents with company-paid expenses when hr_expense installed | VDR-U30-C067 VDR-U30-C088 |
| Payment-term computation | account:models/account_payment_term.py:171 (_compute_terms) | none (negative scan) | Base only | VDR-U30-C081 VDR-U30-C080 |
| Base-line preparation | account:models/account_move.py:1591; account:models/account_tax.py:1591 | hr_expense:models/account_move.py:94 (special mode); hr_expense:models/account_tax.py:24 (expense reference) | Base + expense extension when hr_expense installed | VDR-U30-C109 VDR-U30-C130 VDR-U30-C129 |
| Tax-item grouping keys | account:models/account_tax.py:2297, :2315, :2347 | hr_expense:models/account_tax.py:36, :42 (expense id added to both keys) | Base + expense extension | VDR-U30-C115 VDR-U30-C117 VDR-U30-C129 |
| Rounding allocation and delta distribution | account:models/account_tax.py:1840, :1897, :1995, :2106, :2185 | none installed override; callers reuse: account_edi_ubl_cii:models/account_edi_common.py:1774 | Base only | VDR-U30-C155 VDR-U30-C145 VDR-U30-C133 |
| Cash-rounding items | account:models/account_move.py:3076 (_recompute_cash_rounding_lines); account:models/account_cash_rounding.py:59 | none (negative scan) | Base only; no method defined in dump | VDR-U30-C166 VDR-U30-C174 VDR-U30-C179 |
| Early-payment items and settlement | account:models/account_move_line.py:1077; account:models/account_move.py:5068 | none (negative scan) | Base only; mixed mode unused in dump | VDR-U30-C180 VDR-U30-C190 VDR-U30-C189 |
| Document tax totals summary | account:models/account_tax.py:2727; account:models/account_move.py:1836 | none override; consumers: sale:models/sale_order.py:801, purchase:models/purchase_order.py:255; print: l10n_th:views/report_invoice.xml:3 (title and branch only) | Base for invoices; same engine for orders | VDR-U30-C209 VDR-U30-C205 VDR-U30-C228 VDR-U30-C229 VDR-U30-C226 |
| Totals-summary edit | account:models/account_move.py:2548 (_inverse_tax_totals) | none (negative scan) | Base only | VDR-U30-C220 VDR-U30-C222 |
| Cash-basis entries | account:models/account_partial_reconcile.py:534 (_create_tax_cash_basis_moves), :244; account:models/account_move.py:4124 | none installed override; tag requests: hr_expense:models/hr_expense.py:1649; account_edi_ubl_cii:models/account_edi_common.py:1783 (always-exigible flag) | Base only; no on-payment tax in dump | VDR-U30-C248 VDR-U30-C271 VDR-U30-C131 VDR-U30-C238 |
| Cash-basis configuration | account:models/company.py:220; account:models/account_tax.py:164; account:models/chart_template.py:717, :763 | l10n_th:models/template_th.py:41 (switch set by template data) | Thai template sets switch; generic rule would not | VDR-U30-C233 VDR-U30-C231 VDR-U30-C236 VDR-U30-C237 |
| Exigibility helpers and report option | account:models/account_move_line.py:3456; account:models/account_move_line_tax_details.py:405; account:models/account_report.py:67 | none (the helper has no caller in any Community module) | Option set on all six reports in dump; engine outside Community | VDR-U30-C281 VDR-U30-C282 VDR-U30-C283 VDR-U30-C284 |
| Rate date and conversion | account:models/account_move.py:1130, :1143; base:models/res_currency.py:120, :273 | none (negative scan for the date and rate methods over installed modules) | Base only; supply-date stub not overridden | VDR-U30-C308 VDR-U30-C310 VDR-U30-C316 VDR-U30-C317 |
| Reversal, switch, reset, cancel | account:models/account_move.py:5495, :6058, :6269, :6384; account:wizard/account_move_reversal.py:110 | hr_expense:models/account_move.py:101 (_reverse_moves), :106 (button_cancel) | Base + expense link clearing when hr_expense installed | VDR-U30-C289 VDR-U30-C296 VDR-U30-C299 VDR-U30-C300 VDR-U30-C348 |
| Fiscal-position effect on line taxes | account:models/account_move_line.py:955, :964; account:models/account_move.py:6016 | none (negative scan) | Base only | VDR-U30-C302 VDR-U30-C305 |
| Lock re-checks at write and item changes | account:models/account_move.py:3946-4002; account:models/account_move_line.py:1526, :3485 | none (negative scan) | Base only (PCO-F01 scope) | VDR-U30-C030 VDR-U30-C041 VDR-U30-C042 |

## REGISTER: State and Reversal

| Document/entity | State or event | Trigger | Reversal / cancel / correction path | Blocked when | Claim-IDs |
|---|---|---|---|---|---|
| Draft invoice tax and due-date items | created or updated | edit of a line, term, date, currency, rate, type | edit again; reset after posting | document not draft (tax), item deletion by users | VDR-U30-C095 VDR-U30-C047 VDR-U30-C096 |
| Posted invoice items | frozen | post | credit note (reverse) or reset to draft | read-only fields, locks, hash, restrictive audit trail | VDR-U30-C028 VDR-U30-C040 VDR-U30-C036 |
| Credit note | created as draft copy | reversal wizard | post and match later (separate document) | lock dates move date | VDR-U30-C287 VDR-U30-C295 VDR-U30-C293 |
| Draft invoice type | switched invoice to credit note | switch action | switch back | document numbered or entry | VDR-U30-C296 VDR-U30-C298 |
| Posted invoice | reset to draft | button | repost; items kept | hash, cash-basis or exchange entry, cancel request | VDR-U30-C299 VDR-U30-C278 |
| Draft invoice | cancelled | button | reset to draft | only draft can be cancelled | VDR-U30-C300 |
| Cash-rounding item | created, rewritten, deleted | method set, changed, removed; difference zero | remove method | posted invoice | VDR-U30-C164 VDR-U30-C165 VDR-U30-C168 VDR-U30-C171 |
| Early-payment items (mixed) | created | payment term mixed mode | term change | posted invoice | VDR-U30-C180 |
| Matching (partial reconcile) | created | payment registration, manual reconcile | unreconcile | locks for reversal date | VDR-U30-C248 VDR-U30-C276 |
| Cash-basis entry | created, posted or draft | matching with on-payment items | unreconcile reverses (posted) or deletes (draft) | cannot reset to draft or delete once posted | VDR-U30-C272 VDR-U30-C276 VDR-U30-C278 VDR-U30-C279 |
| Draft document with matching | posted | post | matching dissolved if snapshot changed | none | VDR-U30-C275 |
| Fiscal position of a draft | changed | edit or finder | update action remaps taxes | posted or cancelled | VDR-U30-C304 VDR-U30-C305 VDR-U30-C306 |
| Document rate | edited or refreshed | draft edit, refresh button | refresh to expected rate | posted (read-only) | VDR-U30-C311 VDR-U30-C315 VDR-U30-C314 |
| Totals summary | edited | widget on vendor draft | edit again or recompute by changing an input | posted, sales invoices outside quick encoding | VDR-U30-C220 VDR-U30-C222 |

## REGISTER: Accounting Impact

Valuation context: periodic valuation as in the dump; the automated (perpetual) path is RT and not touched by this unit.

| Event | Entries created or changed (neutral) | Tax lines / tags / accounts affected | Period/lock/date effect | Reversal effect | Claim-IDs |
|---|---|---|---|---|---|
| Edit of a draft invoice | derived items rewritten in the same save; no ledger posting until posted | tax items on distribution accounts with tags; base items tagged | none for drafts; posting later moves date if locked | edit again | VDR-U30-C101 VDR-U30-C118 VDR-U30-C121 |
| Post an invoice | items frozen; analytic lines created (U11); date moved when a lock is violated | tax and base items stored with tags; on-payment tax on transition account (none in dump) | fiscal and tax lock checks; date shifted | credit note or reset | VDR-U30-C028 VDR-U30-C032 VDR-U30-C239 |
| Foreign-currency invoice | tax in both currencies at the stored rate; terms per currency | company balances = document / rate rounded | rate date = invoice date | credit note takes own rate | VDR-U30-C308 VDR-U30-C139 VDR-U30-C324 |
| Cash-rounding method applied | rounding item or enlarged tax item | profit or loss account, or largest tax distribution account with tags | only while draft | remove method deletes item | VDR-U30-C169 VDR-U30-C170 VDR-U30-C167 |
| Partly deductible bill | private-part base items, total item and private-part tax item | journal private-share account; taxes copied from the line | only while draft | rebuilt on change | VDR-U30-C126 VDR-U30-C122 |
| Payment with early discount (included) | discount base items and tax correction items at registration | inverse distribution lines; discount gain or loss account | payment date | unreconcile (U12) | VDR-U30-C190 VDR-U30-C192 VDR-U30-C191 |
| Reconcile an on-payment tax invoice | cash-basis entry in the cash-basis journal; transition lines reconciled | tax to distribution account with tags; base items tagged; transition account cleared | settlement date, not before day after fiscal lock | unreconcile reverses the entry | VDR-U30-C260 VDR-U30-C267 VDR-U30-C270 VDR-U30-C276 |
| Unreconcile or cancel an invoice with cash-basis entries | reversal entries (posted) or deletion (draft) | tags and accounts reversed | origin date or day after latest lock | n/a | VDR-U30-C276 VDR-U30-C277 VDR-U30-C300 |
| Reverse an invoice to a credit note | draft credit note with copied items; later posted and matched | refund distribution lines; positive document totals | invoice date set by wizard; auto-post if future | n/a | VDR-U30-C287 VDR-U30-C112 VDR-U30-C113 |
| Exchange difference at matching | entry in exchange journal, always exigible | no tax lines; gain or loss exchange account | later of the two item dates | unreconcile reverses | VDR-U30-C326 VDR-U30-C327 |
| Totals-summary edit | first tax item of the group changed | tax account unchanged, amount changed | draft only | recompute by editing an input | VDR-U30-C220 VDR-U30-C221 |

## Native status summary and native-gap candidates

- NATIVE mechanisms: items F01-F14, F17-F20, F23, F24 (generic synchronisation, due-date, tax-item, rounding, cash-rounding, early-payment, private-part, balancing, totals, cash-basis reversal, credit note, switch, reset, expense and e-invoice paths).
- PARTIAL: F15, F16 (cash-basis mechanism native; no on-payment tax and no base-tracking account in the Thai set), F21 (fiscal-position effect needs an explicit action), F22 (rate by invoice date only).
- NATIVE GAP / EXTENSION REQUIRED candidates (statutory need pending TXS): (NG-1) Thai taxes authored as on-payment: the switch is on but none of 18 taxes is on-payment VDR-U30-C238; (NG-2) rate date and rate source for foreign-currency VAT base (S12-03, S12-04): only an invoice-date lookup in a rate table that has no rows VDR-U30-C308 VDR-U30-C310 VDR-U30-C318; (NG-3) agreement of the rounding algorithm with S12-08 is UNKNOWN VDR-U30-C163; (NG-4) template data: zero-rated and exempt VAT taxes have no tax group in the template and fall into the WHT 1% group, so a printed or on-screen totals summary may list their base under a withholding group name VDR-U30-C352 VDR-U30-C353 VDR-U30-C354 VDR-U30-C355 (aligned with VDR-U13-C082; statutory presentation pending TXS).
- Defect or inconsistency candidates found in source (not gaps; all need execution): private-part amounts possibly swapped between balance and foreign amount VDR-U30-C127; rounding-item company amount at market rate versus totals-implied rate VDR-U30-C167 VDR-U30-C217; preview sign of fixed-amount instalments VDR-U30-C072; unreachable cash-basis rounding branch VDR-U30-C274; helper domain with no caller VDR-U30-C281.

## CONTRA register and refinements of earlier units

| Earlier claim | This unit claim | Note |
|---|---|---|
| earlier VDR-TXA1-C114 | VDR-U30-C094 | CONTRA: TXA1-C114 lists partner among the inputs that re-synchronise tax items; the document-level partner and invoice date are snapshotted (aml 3334) but no branch compares them, so only the partner on the base items (part of their grouping key), currency, type and rate trigger a recompute. Refinement, not a reversal of the earlier claim. |
| earlier VDR-U11R1-C006 / C009 | VDR-U30-C300 | refinement (not CONTRA): Consistent with correction packet U11-R1: payment_ids is the payments whose own entry is the cancelled move, so cancelling an invoice does not cancel settling payments. |
| earlier VDR-U10R2-C003 | VDR-U30-C032 | refinement (not CONTRA): Consistent with correction packet U10-R2: lock refusals arise on edits of posted documents; at posting the date is shifted (aml and move write paths re-read). |
| earlier VDR-U13-C082 | VDR-U30-C354 | refinement (not CONTRA): Consistent: zero-rated and exempt VAT taxes sit in WHT 1%; this unit adds the template cause (empty group column), the default rule and the totals-summary consequence. |
| earlier VDR-U11-C291 / C293 | VDR-U30-C006 | refinement (not CONTRA): U11 states the stack order and that managers are entered in order; this unit adds the exit (recomputation) order, reverse of the numbers (INFERENCE). |
| earlier VDR-TXA1-C104 | VDR-U30-C114 | refinement (not CONTRA): TXA1 lists untaxed items as product, rounding and non-deductible product; the source also counts the non-deductible product total item (aml 1205). |
| earlier VDR-U12-C149 / VDR-TXA2-C218 | VDR-U30-C274 | refinement (not CONTRA): Earlier units describe the cash-basis flow as complete; the rounding auto-reconciliation tail of the reconcile plan reads keys no Community code sets. |

## Runtime-required (RT) items

- VDR-U30-C072 (account/models/account_move.py:1403): INFERENCE (lines 1395, 1403, 1418-1428 and 233 of the payment-term model): the sign passed to the term computation is +1 for inbound documents in the stored branch but direction_sign (opposite polarity) in the unsaved branch; only fixed-amo
- VDR-U30-C127 (account/models/account_move.py:3561): INFERENCE (lines 3550-3562): the value rounded in the line (document) currency is written to the balance, while the value divided by the document rate and rounded in company currency is written to the foreign amount; for a document in a for
- VDR-U30-C217 (account/models/account_tax.py:2930): INFERENCE (lines 2930-2931 versus AM 3101): the estimated company amount of the rounding uses the rate implied by the document totals, whereas the stored rounding item uses the market rate at the invoice date; the two may differ for a forei
- VDR-U30-C274 (account/models/account_move_line.py:2972): INFERENCE (search of all addon sources): the full-batch keys caba_lines_to_reconcile and exchange_move are read here but no Community code sets them, so this rounding auto-reconciliation branch is never entered; behaviour of tax-account rou
- VDR-U30-C286 (account/models/account_report.py:67): UNKNOWN — EVIDENCE INSUFFICIENT: how the tax report treats exigibility and how Thai VAT and withholding reports would consume cash-basis entries needs the report engine (not in Community) or execution.
- VDR-U30-C328 (account/models/account_move.py:3101): UNKNOWN — EVIDENCE INSUFFICIENT: numeric consistency between document rate, rounding item rate and tax item balances for foreign-currency documents needs execution with loaded rates.
- VDR-U30-C329 (account/models/account_move.py:3773): UNKNOWN — EVIDENCE INSUFFICIENT: the end-to-end numeric result of the reverse-order chain for combined changes (several lines, rounding item, tax items and terms at once) was not executed; resolve with runtime documents in THB and one forei
- VDR-U30-C340 (account/models/account_move.py:3145): UNKNOWN — EVIDENCE INSUFFICIENT: no cash-rounding method is defined in the dump; the behaviour with missing profit or loss account, with the largest-tax strategy on documents with several tax groups, and the interaction of the rounding item
- VDR-U30-C343 (account/models/account_partial_reconcile.py:580): INFERENCE (lines 580-594): only tax items get the residual correction on the last partial; base items are scaled by percentage only, so over several partial payments the reported base can deviate by rounding units. Needs execution.
- VDR-U30-C345 (account/models/account_move.py:3405): INFERENCE (lines 2090-2094 of the item model, 3818-3823 and 3405-3409): a credit note produced by copy carries copied tax and term items and product items whose balance is dropped; whether its tax amounts end up copied or recomputed depends
- VDR-U30-C355 (account/models/account_tax.py:2823): INFERENCE (lines 2823-2831 and the tax-data list in the core calculation): the summary groups tax data by the tax group of each tax regardless of the amount, so a zero-rated or exempt line contributes its base to the group named WHT 1% with

## DISCOVERED SUPPORTING MODULES

- `hr_expense` (installed): overrides payment-term needs, base-line preparation, tax-item keys, reversal and cancel; requests cash-basis tags for company-paid expenses.
- `account_edi_ubl_cii` (installed): import path writes lines through the synchronisation and aligns tax amounts (tolerance 0.03); uses the smooth-delta helper.
- `base` (installed): `res.currency` rate and conversion (`_get_rates`, `_get_conversion_rate`, `_convert`).
- `sale`, `purchase` (installed): consumers of the totals summary for orders; `l10n_th` (installed): sets the cash-basis switch in template data and inherits the invoice print.
- `point_of_sale` (NOT installed): the only Community setter of the balance-check suppression key.
- Not read in depth: account report engine (Enterprise) and `account_edi_ubl_cii` export builders; the tax-details SQL view only for the exigibility column; payment registration wizard internals (U12).

## Honest limits

Source-static plus configuration-only DB reconciliation of an empty-transaction restore; nothing was executed. Not read: report engine and tax return evaluation; JavaScript mirror beyond signatures; rate-feed or scheduled rate update modules; landed-cost, manufacturing and subcontracting entries (TXA2 limits unchanged); `_batch_for_taxes_computation` internals and the formula tax type (not installed). Items marked INFERENCE derive from several cited lines; items marked RT need runtime documents (THB and one foreign currency with loaded rates).

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U30-C001 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3735 | stack = [ | FACT | always | — | The synchronisation stack has eight entries keyed by sequence: 10 payment-term items, 20 automatic balancing (entries), 30 cash-rounding items, 40 discount-allocation items, 50 tax items, 60 private-part (non-deductible) base items, 70 early-payment-discount items, 80 commercial-partner propagation (re-read of VDR-U11-C291 with the generic-sync arguments). | N-U30-001 |
| VDR-U30-C002 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3727 | m.line_ids.tax_repartition_line_id | FACT | always | — | Tax-item synchronisation applies to invoice-like documents and to any entry whose items carry taxes or tax distribution lines (auto tax mode). | N-U30-002 |
| VDR-U30-C003 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3728 | invoice_container['records'] | FACT | always | — | Payment-term, rounding, discount-allocation, private-part, early-payment and partner synchronisation apply only to invoice-like documents (invoices, credit notes, receipts). | N-U30-002 |
| VDR-U30-C004 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3729 | tax_cash_basis_origin_move_id | FACT | always | — | Automatic balancing applies to ordinary entries that are not cash-basis entries generated from an origin document. | N-U30-002 |
| VDR-U30-C005 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3776 | stack_list.sort() | FACT | always | — | Entries are sorted by sequence number and their context managers entered in ascending order (before-snapshots taken 10 to 80). | N-U30-004 |
| VDR-U30-C006 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3775 | ExitStack() as stack | INFERENCE | always | — | INFERENCE (lines 3773-3778 plus ExitStack unwinding semantics): the post-change logic of each manager runs in reverse entry order, so after the stored change the chain recomputes 80 partner, 70 early-payment, 60 private-part, 50 tax, 40 discount allocation, 30 rounding, 20 balancing and finally 10 payment terms; payment terms therefore read final totals. Numeric outcome of a combined case is not executed. | N-U30-004 |
| VDR-U30-C007 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3768 | 'skip_invoice_sync' | FACT | always | — | The whole stack is skipped when the recursion guard key skip_invoice_sync is already true (stack map or context); nested writes done by the synchronisation itself therefore do not synchronise again. | N-U30-010 |
| VDR-U30-C008 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3781 | self.line_ids._sync_invoice | FACT | always | — | Inside the stack the line-level synchroniser (balance and foreign amount coherence) wraps the change; its post-change logic runs first, then the containers are refreshed (lines 3780-3784) before the move-level managers unwind. | N-U30-004 |
| VDR-U30-C009 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7067 | account_disable_recursion_stack | FACT | always | — | The recursion guard stores a stack map in the database-cursor cache (not in the record context): it is shared by every environment on the same cursor. | N-U30-010 |
| VDR-U30-C010 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7074 | stack.pushmap | FACT | always | — | Entering the guard pushes the target value for the key on the stack map and pops it on exit; the yielded flag tells the caller whether it must skip. | N-U30-010 |
| VDR-U30-C011 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2786 | 'check_move_validity' | FACT | always | — | The balance check is a context manager guarded by key check_move_validity with default True and target False: when the value is False the check is skipped. | N-U30-009 |
| VDR-U30-C012 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7073 | disabled = current_val == target | INFERENCE | always | — | INFERENCE (lines 2786, 7066-7078): entering the balance check pushes False for the key, so nested creates, writes and unlinks inside an outer operation see the check as disabled and only the outermost operation asserts balance. | N-U30-009 |
| VDR-U30-C013 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2791 | unbalanced_moves := self._get_unbalanced_moves | FACT | always | — | After the body the check raises a user error when any document is unbalanced; a single document gives a generic message and several list each document name (re-read of VDR-U11-C060, C061). | N-U30-003 |
| VDR-U30-C014 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2820 | HAVING ROUND(SUM(line.balance) | FACT | always | — | Balance is tested by direct query on rounded sum of balances in company-currency decimal places, after flushing amount fields; the query avoids computed stored fields because it runs during create. | N-U30-009 |
| VDR-U30-C015 | FUNCTION MAPPING REQUIRED | point_of_sale/models/pos_session.py:442 | check_move_validity=False | FACT | point_of_sale installed (it is not installed in the dump) | — | The only Community caller that switches the balance check off together with skip_invoice_sync is the point-of-sale session posting (module not installed here); a test in sale_timesheet also uses the key. | N-U30-013 |
| VDR-U30-C016 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2786 | 'check_move_validity' | INFERENCE | 356 installed modules | — | INFERENCE (search of installed modules): no installed module sets check_move_validity to False; in this installation the balance check is skipped only by the nested-operation effect, so any imbalance surfaces as the user error. | N-U30-013 |
| VDR-U30-C017 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3895 | You cannot create a move already | FACT | always | — | A document cannot be created directly in posted state; derived items are therefore always produced while the document is a draft. | N-U30-012 |
| VDR-U30-C018 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3899 | with ExitStack() as exit_stack | FACT | always | — | Document creation is wrapped by the balance check and by the dynamic-line synchronisation; the exit stack also holds the protection context created after the ORM create. | N-U30-009 |
| VDR-U30-C019 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3905 | stolen_moves | FACT | always | — | The container is created empty and filled with the new documents (plus documents whose items are stolen by link commands) after the ORM create, so before-snapshots on create are empty. | N-U30-007 |
| VDR-U30-C020 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3904 | self.env.protecting | FACT | always | — | After the ORM create, the fields given in the creation values that have an inverse or a writable computation are protected from recomputation for the rest of the synchronisation. | N-U30-011 |
| VDR-U30-C021 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3889 | field.inverse or (field.compute and not field.readonly) | FACT | always | — | Protection applies to supplied values of fields that have an inverse or are computed and writable, together with the fields computed from them. | N-U30-011 |
| VDR-U30-C022 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3886 | Skip protecting tax_totals | FACT | always | — | The totals summary field is excluded from protection because it is applied explicitly after the create or write. | N-U30-011 |
| VDR-U30-C023 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3907 | if 'tax_totals' in vals | FACT | always | — | A totals summary supplied at creation is written back after the synchronisation, which may adjust tax amounts through the inverse. | N-U30-087 |
| VDR-U30-C024 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3909 | moves.is_manually_modified = False | FACT | always | — | The manually-modified flag is cleared after creation and set again by any later write unless the skip context key is set (posting passes that key). | N-U30-007 |
| VDR-U30-C025 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3981 | self.env.protecting(self._get_protected_vals(vals, self)) | FACT | always | — | Document write is wrapped by protection, the balance check and the synchronisation, over the written documents and those whose items are stolen by link commands. | N-U30-009 |
| VDR-U30-C026 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3984 | vals['is_manually_modified'] = True | FACT | always | — | Every write marks the document as manually modified unless the key is given or the skip context key is set. | N-U30-007 |
| VDR-U30-C027 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3988 | skip_account_move_synchronization=True | FACT | always | — | The ORM write runs with the business-model synchronisation suppressed; the payment and bank-statement synchronisation is invoked afterwards with the changed field names. | N-U30-014 |
| VDR-U30-C028 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3960 | unmodifiable_fields = ( | FACT | always | — | On a posted document the item list, invoice date, date, partner, payment term, currency, fiscal position and cash-rounding method cannot be written (re-read of VDR-U11-C101). | N-U30-012 |
| VDR-U30-C029 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3964 | skip_readonly_check | FACT | skip_readonly_check unset | — | The posted-document read-only rule can be bypassed only by the context key skip_readonly_check. | N-U30-013 |
| VDR-U30-C030 | PCO-F01 | account/models/account_move.py:3951 | move.line_ids._check_tax_lock_date() | FACT | posted document, name or date changed | — | Changing the name or date of a posted document re-checks the fiscal lock dates and, for its items, the tax lock date. | N-U30-016 |
| VDR-U30-C031 | PCO-F01 | account/models/account_move.py:3956 | move.line_ids._check_tax_lock_date() | FACT | state leaves posted | — | Moving a document out of posted state re-checks the fiscal lock dates and the tax lock date of its items. | N-U30-016 |
| VDR-U30-C032 | PCO-F01 | account/models/account_move.py:4002 | posted_move.line_ids._check_tax_lock_date() | FACT | date or state written | — | After the write the same lock checks are made again for documents that are posted (so a new date inside a locked period is refused). | N-U30-016 |
| VDR-U30-C033 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4013 | super(AccountMove, move).write | FACT | tax_totals in vals | — | A supplied totals summary is written after synchronisation, document by document (quick-encoding rounding fix). | N-U30-087 |
| VDR-U30-C034 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4081 | no need to sync | FACT | always | — | Deleting a document disables the synchronisation and allows dynamic deletion of derived items. | N-U30-015 |
| VDR-U30-C035 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4083 | self.line_ids.remove_move_reconcile() | FACT | always | — | Deletion first removes the reconciliations of all items, then deletes the items, then the document. | N-U30-015 |
| VDR-U30-C036 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4075 | restrictive audit trail | FACT | company restrictive audit trail on | — | With the restrictive audit trail a document that has been posted once cannot be deleted (cancel instead) unless the force-delete context key is set; the Thai dump has this company option unset. | N-U30-015 |
| VDR-U30-C037 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4064 | has already consumed a sequence number | FACT | user lacks account manager group, no quick edit, no force | — | A numbered document that is not last in its sequence chain cannot be deleted by a non-manager unless quick edit mode or force-delete applies. | N-U30-015 |
| VDR-U30-C038 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1788 | moves._sync_dynamic_lines(move_container) | FACT | always | — | Creating journal items directly is wrapped by the same balance check and synchronisation of the owning documents plus the line-level synchroniser. | N-U30-009 |
| VDR-U30-C039 | PCO-F01 | account/models/account_move_line.py:1795 | lines._check_tax_lock_date() | FACT | ignore_tax_lock_date not the sentinel | — | After creation each new item on a posted document is checked against the tax lock date unless the sentinel context value is given. | N-U30-016 |
| VDR-U30-C040 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1849 | You cannot modify the taxes related | FACT | posted parent | — | Changing the taxes or originator tax of a posted item is refused with the instruction to reset the document to draft. | N-U30-012 |
| VDR-U30-C041 | PCO-F01 | account/models/account_move_line.py:3488 | tax_fnames = ['balance' | FACT | always | — | Tax lock protects balance, originator tax, taxes and tags; fiscal lock adds account, journal, foreign amount, currency and partner; reconciliation protection covers account, date, balance, foreign amount and currency. | N-U30-016 |
| VDR-U30-C042 | PCO-F01 | account/models/account_move_line.py:1857 | protected_fields['tax'] | FACT | posted parent | — | A write that changes a tax-protected field of a posted item queues the item for the tax lock check, run before and again after the write. | N-U30-016 |
| VDR-U30-C043 | PCO-F01 | account/models/account_move_line.py:1853 | protected_fields['fiscal'] | FACT | posted parent | — | A write that changes a fiscal-protected field of a posted item checks the fiscal lock dates of the document. | N-U30-016 |
| VDR-U30-C044 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1861 | Break the reconciliation | FACT | matched item | — | Writing a reconciliation-protected field of a matched item removes its reconciliation (allowing a common account change over a complete matching set); undoing a match also dissolves its cash-basis entries (see CAP-U30-07). | N-U30-016 |
| VDR-U30-C045 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1893 | self.move_id._sync_dynamic_lines(move_container) | FACT | always | — | Item write is wrapped by the balance check, protection, the move synchronisation and the line-level synchroniser. | N-U30-009 |
| VDR-U30-C046 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1966 | can't delete a posted journal item | FACT | force_delete unset | — | Items with a non-zero amount of a posted document cannot be deleted. | N-U30-015 |
| VDR-U30-C047 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1970 | if not self.env.context.get('dynamic_unlink') | FACT | dynamic_unlink unset | — | A tax item (while the document has taxed items) or a payment-term item cannot be deleted by a user; only the synchronisation, which sets the dynamic-unlink key, can delete them (re-read of VDR-U11-C296). | N-U30-015 |
| VDR-U30-C048 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1989 | locked journal entry | FACT | hashed document | — | Items of a hashed (locked) document cannot be deleted. | N-U30-015 |
| VDR-U30-C049 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1995 | self.remove_move_reconcile() | FACT | always | — | Item deletion first unreconciles the items, checks fiscal and tax locks for non-zero items of posted documents, logs the deletion in the audit trail for documents posted once, and runs under balance check and synchronisation. | N-U30-016 |
| VDR-U30-C050 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3491 | dynamic_unlink=True | FACT | always | — | Every synchroniser deletes obsolete derived items with the dynamic-unlink key (tax items at 3491, private-part items at 3588, generic items at 3687). | N-U30-015 |
| VDR-U30-C051 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3689 | clean_context(self.env.context) | FACT | always | — | Derived items are created with a cleaned context so that default-value keys of the calling screen do not leak into them. | N-U30-011 |
| VDR-U30-C052 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3622 | inv_existing_before = existing() | FACT | always | — | The generic synchroniser snapshots existing keyed items, the needed values, and the dirty flag before the change, then resets the dirty flag. | N-U30-006 |
| VDR-U30-C053 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3628 | if not dirty_recs_after | FACT | always | — | If after the change no record is marked dirty (no input of the need was touched) the synchroniser exits without recomputing. | N-U30-006 |
| VDR-U30-C054 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3634 | Filter out deleted lines | FACT | always | — | Needs that referred to items deleted during the change are dropped from the before-snapshot so they are not recreated unless still needed. | N-U30-006 |
| VDR-U30-C055 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3644 | if needed_after == needed_before | FACT | always | — | If the needed values did not change the existing items are left untouched (user edits preserved). | N-U30-007 |
| VDR-U30-C056 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3646 | do not modify user input | FACT | always | — | If there was no need before and the keyed items changed in the meantime, the items are treated as manually created and are not touched. | N-U30-007 |
| VDR-U30-C057 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3652 | to_delete = [ | FACT | always | — | Items whose key is no longer needed are deleted, both those that existed before and those that appeared during the change. | N-U30-007 |
| VDR-U30-C058 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3664 | to_create = { | FACT | always | — | Needed keys without an existing item are created. | N-U30-007 |
| VDR-U30-C059 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3669 | to_write = { | FACT | always | — | Existing items whose stored value differs from the needed value are rewritten, compared after conversion to write format. | N-U30-007 |
| VDR-U30-C060 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3680 | while to_delete and to_create | FACT | always | — | A pending deletion is paired with a pending creation and executed as an in-place rewrite of the old item with the new key and values, preserving the item identity (and any reconciliation link). | N-U30-008 |
| VDR-U30-C061 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3693 | if to_write: | FACT | always | — | Rewrites of existing items are applied one item at a time after deletions and creations. | N-U30-008 |
| VDR-U30-C062 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3615 | l.display_type != 'cogs' | FACT | item-level dirty flags | — | Cost-of-goods items are excluded when deciding whether item-level dirty flags are set. | N-U30-006 |
| VDR-U30-C063 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3593 | Keep keyless EPD lines | FACT | early-payment items | — | Early-payment items without a key (for example after an order auto-completes a bill) are kept in the map under an identity key so they can be cleaned and rebuilt. | N-U30-008 |
| VDR-U30-C064 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3271 | del res[key] | FACT | always | — | When several needs share a key their monetary values are summed; a key whose summed monetary values are all zero is dropped. | N-U30-006 |
| VDR-U30-C065 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3273 | ORM cache | FACT | always | — | Float needs are converted to the ORM cache representation so comparisons against stored items do not differ by float rounding. | N-U30-006 |
| VDR-U30-C066 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1735 | skip_invoice_line_sync | FACT | always | — | The line-level synchroniser is skipped when the skip_invoice_line_sync key is set (also set while it runs), preventing recursion. | N-U30-010 |
| VDR-U30-C067 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1388 | invoice_payment_term_id', 'invoice_date', 'currency_id' | FACT | always | — | The needed payment-term items depend on the payment term, invoice date, currency, signed total in currency and the due date field. | N-U30-033 |
| VDR-U30-C068 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1394 | invoice.needed_terms_dirty = True | FACT | always | — | Each computation resets the needed terms to empty and marks them dirty, so the generic synchroniser sees them as changed inputs. | N-U30-006 |
| VDR-U30-C069 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1396 | if invoice.is_invoice(True) and invoice.invoice_line_ids | FACT | always | — | Terms are needed only for invoice-like documents that have product, section or note lines; otherwise the needed set is empty. | N-U30-027 |
| VDR-U30-C070 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1404 | invoice._get_rounded_base_and_tax_lines(round_from_tax_lines=False) | FACT | record not yet stored (preview) | — | For a not yet stored record the term base totals come from freshly computed base and tax lines (no manual tax amounts), because accounting items do not exist yet. | N-U30-028 |
| VDR-U30-C071 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1414 | tax_amount_currency = invoice.amount_tax * sign | FACT | record stored | — | For a stored document the term base totals are read from the stored tax, untaxed and signed company-currency amounts. | N-U30-028 |
| VDR-U30-C072 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1403 | sign = invoice.direction_sign | INFERENCE | record not yet stored (preview) | RT | INFERENCE (lines 1395, 1403, 1418-1428 and 233 of the payment-term model): the sign passed to the term computation is +1 for inbound documents in the stored branch but direction_sign (opposite polarity) in the unsaved branch; only fixed-amount instalments use the sign, so the preview could show fixed instalments with the opposite sign from the stored result. Needs execution. | N-U30-034 |
| VDR-U30-C073 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1419 | date_ref=invoice.invoice_date or invoice.date | FACT | payment term set | — | Instalments are computed from the invoice date (else accounting date, else today), the document currency (else journal or company currency) and the document cash rounding. | N-U30-019 |
| VDR-U30-C074 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1445 | invoice.needed_terms[key]['balance'] += values['balance'] | FACT | payment term set | — | Instalments are keyed by document, due date and discount date; two instalments with the same key are merged by adding their amounts. | N-U30-021 |
| VDR-U30-C075 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1455 | 'balance': invoice.amount_total_signed | FACT | no payment term | — | Without a payment term a single item is needed at the invoice due date for the signed total in both currencies, with no discount data. | N-U30-019 |
| VDR-U30-C076 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1439 | 'discount_balance': invoice_payment_terms.get('discount_balance') or 0.0 | FACT | payment term set | — | Each needed term carries the discount date, the discounted company amount and the discounted amount in currency taken from the term computation. | N-U30-025 |
| VDR-U30-C077 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1228 | def _compute_term_key | FACT | payment-term items | — | An existing payment-term item is identified by document, maturity date and discount date. | N-U30-021 |
| VDR-U30-C078 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3736 | existing_key_fname='term_key' | FACT | always | — | The payment-term synchroniser uses the term key, the needed terms and their dirty flag, creating items of type payment term. | N-U30-004 |
| VDR-U30-C079 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1095 | move.needed_terms and max( | FACT | always | — | The document due date is the latest maturity among needed terms, else the existing due date, else today. | N-U30-026 |
| VDR-U30-C080 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:190 | rate = abs(total_amount_currency / total_amount) | FACT | payment term computation | — | The term computation derives its rate from the ratio of total in currency to total in company currency (zero when the total is zero), not from the stored document rate. | N-U30-023 |
| VDR-U30-C081 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:226 | The last line is always | FACT | payment term computation | — | The last instalment takes the remaining amount in both currencies, so instalments always sum exactly to the document total in each currency. | N-U30-022 |
| VDR-U30-C082 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:233 | company_currency.round(line.value_amount / rate) | FACT | fixed-amount instalment, not last | — | A fixed instalment is converted to company currency by the term rate and rounded; the amount in currency is the fixed value rounded. | N-U30-023 |
| VDR-U30-C083 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:237 | line_amount = company_currency.round | FACT | percent instalment, not last | — | A percent instalment is rounded independently in company currency and in document currency from the respective totals. | N-U30-023 |
| VDR-U30-C084 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:247 | cash_rounding_difference_currency = cash_rounding.compute_difference | FACT | cash rounding set, instalment not last | — | With cash rounding each non-last instalment is rounded to the coin in document currency and its company amount is re-derived from the rounded foreign amount divided by the rate. | N-U30-024 |
| VDR-U30-C085 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:204 | pay_term['discount_balance'] = company_currency.round | FACT | early discount, mode excluded or mixed | — | For excluded or mixed discount the discounted total is total minus discount percentage of the untaxed amount; for included mode it is total times one minus the percentage; both are rounded in each currency and cash-rounded when applicable. | N-U30-025 |
| VDR-U30-C086 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:165 | single 100% line | FACT | always | — | A payment term must have percent lines totalling 100; an early discount is allowed only on a single 100 percent line with strictly positive percentage and days. | N-U30-025 |
| VDR-U30-C087 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1514 | must have a due date | FACT | sale documents | — | On sale documents a payment-term item must sit on a receivable account and a receivable account is only allowed for payment-term items; payable accounts are refused on sale documents; the mirror rule holds for purchase documents. | N-U30-032 |
| VDR-U30-C088 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:78 | 'company_account' in move.expense_ids.mapped('payment_mode') | FACT | hr_expense installed (it is) | — | For documents created from company-paid expenses the needed terms are replaced by one item dated today, amount equal to minus the sum of all non-term items, named from the payment reference, on the expense destination account. | N-U30-031 |
| VDR-U30-C089 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:87 | "balance": -sum(term_lines.mapped("balance")) | FACT | company-paid expenses | — | The replacement term amount is computed from the other items of the document, in both currencies. | N-U30-031 |
| VDR-U30-C090 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3292 | ('product', 'epd', 'rounding', 'non_deductible_product') | FACT | always | — | Base items for the tax synchroniser are items of type product, early-payment, rounding and private-part product. | N-U30-035 |
| VDR-U30-C091 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3295 | filtered('tax_repartition_line_id') | FACT | always | — | Existing tax items are every item carrying a tax distribution line (this includes a rounding item created by the largest-tax cash-rounding strategy). | N-U30-035 |
| VDR-U30-C092 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3306 | extra_fields = ['price_unit', 'quantity', 'discount', 'deductible_amount'] | FACT | invoice-like document | — | Tracked base-item inputs are the grouping-key fields (partner, currency, analytic distribution, account, taxes) plus unit price, quantity, discount and deductibility; for ordinary entries the foreign amount. | N-U30-037 |
| VDR-U30-C093 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3301 | ('amount_currency', 'balance', 'analytic_distribution') | FACT | always | — | Tracked tax-item values are the amount in currency, the balance and the analytic distribution. | N-U30-038 |
| VDR-U30-C094 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3337 | if move.state == 'draft' | FACT | always | CONTRA | CONTRA (refinement of VDR-TXA1-C114, see CONTRA register): Document-level snapshots (currency, partner, type, rate, invoice date) are taken only for drafts; the partner and invoice date snapshots are not used by any later branch (only currency, type and rate are compared). | N-U30-037 |
| VDR-U30-C095 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3365 | if move.state != 'draft' | FACT | always | — | Any non-draft document is skipped after the change: posted or cancelled documents never have their tax items re-derived by the synchroniser. | N-U30-043 |
| VDR-U30-C096 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3375 | field_has_changed(moves_values_before, move, 'currency_id') | FACT | invoice-like draft | — | A change of document currency or of document type (invoice to credit note) forces a complete recomputation that ignores existing tax amounts (round-from-tax-lines false). | N-U30-037 |
| VDR-U30-C097 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3381 | Removed a base line affecting | FACT | a taxed base item removed | — | When a taxed base item is removed, existing tax amounts are kept only if some tax item value was itself changed in the same operation, otherwise recomputed. | N-U30-038 |
| VDR-U30-C098 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3393 | Keep the tax lines amounts | FACT | a base item changed | — | When base items change, existing tax amounts are retained if the changed items do not involve taxes, if the set of tax items changed, or if any tax-item field is protected; otherwise tax amounts are recomputed. | N-U30-038 |
| VDR-U30-C099 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3405 | we don't need to recompute anything | FACT | created with all items and amounts supplied | — | If the retained branch applies and the changed base items carry a foreign amount or balance (document created with all items), the synchroniser does nothing. | N-U30-038 |
| VDR-U30-C100 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3412 | round_from_tax_lines = 'reapply_currency_rate' | FACT | only the document rate changed | — | A change of the document rate alone keeps the foreign tax amounts and re-derives the company amounts from the new rate. | N-U30-037 |
| VDR-U30-C101 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3416 | move._get_rounded_base_and_tax_lines | FACT | always | — | Recompute pipeline: rounded base and tax lines, accounting data on base lines with cash-basis tags only for always-exigible moves, then preparation of tax-item additions, updates and deletions against existing tax items. | N-U30-035 |
| VDR-U30-C102 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3469 | grouped_update[line.currency_id.id, frozendict(to_update)] | FACT | always | — | Base-item writes are batched by currency and identical values, only for items whose stored values differ (write needed test). | N-U30-035 |
| VDR-U30-C103 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3477 | 'display_type': 'tax' | FACT | always | — | New tax items are created with type tax on the document; obsolete ones are deleted; matching ones are updated. | N-U30-039 |
| VDR-U30-C104 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3486 | if grouped_update: | FACT | always | — | Persistence order is grouped updates, then deletions (dynamic unlink), then creations. | N-U30-039 |
| VDR-U30-C105 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3487 | Need to use currency_id | FACT | always | — | Updates are grouped per currency to avoid writing items of several currencies in one write. | N-U30-039 |
| VDR-U30-C106 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1791 | if self.id or not is_invoice | FACT | always | — | For a stored document the base items are the product items plus early-payment, cash-rounding (without distribution line) and private-part items, and the tax items are those carrying distribution lines; for an unsaved invoice they are the invoice lines plus anticipated early-payment and private-part lines. | N-U30-035 |
| VDR-U30-C107 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1816 | tax_lines=tax_lines if round_from_tax_lines else [] | FACT | always | — | Existing tax items are passed to the rounding step only when the caller asks to keep them; otherwise all tax amounts are recomputed. | N-U30-038 |
| VDR-U30-C108 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1815 | tax_line['balance'] = self.company_currency_id.round( | FACT | rate-only change | — | For a rate-only change the balance of each existing tax item becomes its amount in currency divided by the new rate, rounded in company currency. | N-U30-132 |
| VDR-U30-C109 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1607 | 'special_mode': False if is_invoice else 'total_excluded' | FACT | always | — | Product item to base line: invoices use unit price, quantity, discount, document rate and direction sign with the normal price-include treatment; other entries use the foreign amount as a price-excluded unit price with quantity one. | N-U30-040 |
| VDR-U30-C110 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1612 | computation_key.startswith('global_discount') | FACT | line carries extra tax data | — | A stored computation key starting with global_discount or down_payment gives the base line the matching special type, so tax subsets are computed separately. | N-U30-035 |
| VDR-U30-C111 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1161 | invoice.direction_sign = 1 | FACT | always | — | Direction sign is +1 for ordinary entries and outbound documents (vendor bills, customer credit notes, purchase receipts) and -1 otherwise; it multiplies computed amounts into item balances. | N-U30-040 |
| VDR-U30-C112 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1207 | line.move_id.move_type in ('out_refund', 'in_refund') | FACT | always | — | An item is a refund item when its document is a credit note; for entries the flag follows the distribution line document type or the sign of the debit or credit against the tax type. | N-U30-040 |
| VDR-U30-C113 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1224 | move.amount_total = sign * total_currency | FACT | always | — | Document amounts in currency are the direction sign times the sum of item amounts, so they are positive for invoices and credit notes alike; signed company amounts use the opposite of the balance sum. | N-U30-040 |
| VDR-U30-C114 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1199 | line.display_type in ('tax', 'non_deductible_tax') | FACT | invoice-like | — | Document tax amount sums tax, private-part tax and tax-linked rounding items; untaxed amount sums product, rounding, private-part product and private-part total items. | N-U30-035 |
| VDR-U30-C115 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2327 | tax_rep = tax_rep_data | FACT | always | — | The grouping key of a tax item adds the tax distribution line, group tax, subsequent taxes (items of later taxes whose base this tax affects), tags, partner, currency, and a keep-zero flag set false (re-read of VDR-TXA1-C060 to C062 with line numbers 2327-2344). | N-U30-039 |
| VDR-U30-C116 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2335 | if tax.analytic or not tax_rep.use_in_tax_closing | FACT | always | — | Analytic distribution on a tax item is inherited only when the tax is flagged as analytic cost or its distribution line is not used for tax closing. | N-U30-039 |
| VDR-U30-C117 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2347 | def _prepare_tax_line_repartition_grouping_key | FACT | always | — | The key of an existing tax item has the same fields (distribution line, partner, currency, group tax, analytic, account, taxes, tags) so existing items can be matched to needed ones. | N-U30-039 |
| VDR-U30-C118 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3111 | tax_line['tax_base_amount'] += sign * tax_data['base_amount'] | FACT | always | — | Each tax item accumulates the signed base amount, signed amount in currency and signed balance of all base lines sharing its key, and takes the tax name unless a manual name is given. | N-U30-041 |
| VDR-U30-C119 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3120 | k['__keep_zero_line'] | FACT | always | — | A tax item whose amount is zero in both currencies is dropped; the keep-zero flag is always false for items built from base lines. | N-U30-039 |
| VDR-U30-C120 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3132 | grouping_key not in tax_lines_to_update | FACT | existing tax items supplied | — | The first existing tax item with a needed key is updated; any further existing item with the same key is queued for deletion; needed keys with no existing item become additions. | N-U30-039 |
| VDR-U30-C121 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3100 | base_line['tax_tag_ids'].ids | FACT | always | — | Base items are updated with their tax tags and with amounts equal to sign times (total excluded plus rounding delta) in both currencies. | N-U30-035 |
| VDR-U30-C122 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3457 | unused_grouping_key | FACT | partly deductible purchase | — | The single private-part tax item is updated through the same update list under a placeholder key and otherwise created, with account taken from the existing item, the journal private-part account or the journal default account (re-read of VDR-TXA1-C118). | N-U30-042 |
| VDR-U30-C123 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3428 | if not non_deductible_lines_values and non_deductible_tax_line | FACT | always | — | The private-part tax item is deleted when no private-part base line carries taxes any more. | N-U30-042 |
| VDR-U30-C124 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3501 | line.deductible_amount < 100 | FACT | draft purchase document | — | Private-part base items are generated only for draft purchase documents having a product line with deductibility below 100 percent. | N-U30-042 |
| VDR-U30-C125 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3525 | has_changed_product_lines = bool( | FACT | always | — | Private-part items are rebuilt only when the product lines changed in name, subtotal, taxes, deductibility or account (before and after counters compared). | N-U30-042 |
| VDR-U30-C126 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3550 | non_deductible_subtotal = line.currency_id.round(line.price_subtotal * percentage) | FACT | partly deductible line | — | Private share of a line = line subtotal times (100 minus deductibility) percent, rounded in the line currency; a total item carries the sum on the journal private-part account. | N-U30-042 |
| VDR-U30-C127 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3561 | 'balance': -1 * non_deductible_base | INFERENCE | partly deductible bill in a foreign currency | RT | INFERENCE (lines 3550-3562): the value rounded in the line (document) currency is written to the balance, while the value divided by the document rate and rounded in company currency is written to the foreign amount; for a document in a foreign currency the two look swapped. Not executed; for company-currency documents (rate one) there is no difference. | N-U30-049 |
| VDR-U30-C128 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3581 | while to_create and to_delete | FACT | always | — | Existing private-part items are reused by rewriting before deleting or creating the remainder. | N-U30-008 |
| VDR-U30-C129 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:39 | results['expense_id'] = base_line['expense_id'].id | FACT | hr_expense installed (it is) | — | Expense documents add the expense reference to the base-line grouping key and to the existing tax-item key so tax items are kept per expense. | N-U30-045 |
| VDR-U30-C130 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:98 | results['special_mode'] = 'total_included' | FACT | expense paid by the employee | — | For own-account expenses the product base line is computed as price-included (amount already contains the tax). | N-U30-045 |
| VDR-U30-C131 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1649 | include_caba_tags=self.payment_mode == 'company_account' | FACT | company-paid expense payment entry | — | For company-paid expenses the payment entry is built by the engine requesting cash-basis tags (re-read of VDR-TXA2-C308). | N-U30-045 |
| VDR-U30-C132 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1725 | tolerance = 0.03 | FACT | account_edi_ubl_cii installed (it is) and e-invoice imported | — | An imported e-invoice has its tax amounts aligned to the totals in the file only if the computed tax differs by no more than 0.03 in document currency and every tax is recognised. | N-U30-046 |
| VDR-U30-C133 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1774 | AccountTax._distribute_delta_amount_smoothly | FACT | e-invoice imported | — | The imported tax total per tax set is distributed over base lines by the same smooth-delta algorithm, then written on existing tax items inside the balance check and synchronisation. | N-U30-046 |
| VDR-U30-C134 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1717 | invoice._sync_dynamic_lines(container) | FACT | e-invoice imported | — | Imported lines are written inside the same balance check and dynamic-line synchronisation, so tax and payment-term items are derived exactly as for manual entry. | N-U30-046 |
| VDR-U30-C135 | FUNCTION MAPPING REQUIRED | account/models/company.py:129 | tax_calculation_rounding_method = fields.Selection | FACT | always | — | The company chooses between rounding globally (labelled round per tax) and rounding per line; the default is round globally. | N-U30-060 |
| VDR-U30-C136 | FUNCTION MAPPING REQUIRED | account/models/company.py:132 | default='round_globally' | OBSERVATION | restored database | — | OBSERVATION (company row of the dump): the single company uses the global rounding method. | N-U30-050 |
| VDR-U30-C137 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1182 | if rounding_method == 'round_per_line' | FACT | round per line | — | Per-line mode rounds each tax amount to the document currency precision inside the core calculation and also rounds the raw base (lines 1182-1183 and 1236-1237). | N-U30-050 |
| VDR-U30-C138 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1793 | if rounding_method == 'round_per_line' | FACT | round per line | — | Per-line mode additionally rounds the company-currency total and each tax and base amount per line; global mode leaves them raw until the document-level steps. | N-U30-050 |
| VDR-U30-C139 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1788 | / rate if rate else 0.0 | FACT | always | — | Company-currency raw amounts are the document-currency amounts divided by the line rate, zero when the rate is zero. | N-U30-127 |
| VDR-U30-C140 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2247 | ('', company.currency_id)) | FACT | always | — | The rounding entry first rounds, per line and independently in document and company currency, the total excluded and each tax base and tax amount. | N-U30-052 |
| VDR-U30-C141 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2272 | reverse_charge_sign = -1 if | FACT | line carries manual amounts | — | Manual total-excluded and per-tax base and tax amounts replace rounded values in document currency (reverse-charge entries take the opposite sign) and are converted to company currency by the line rate. | N-U30-055 |
| VDR-U30-C142 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2289 | tax_details[f'total_included{suffix}'] += tax_data[f'tax_amount{suffix}'] | FACT | always | — | Total included per line is its rounded total excluded plus its rounded tax amounts; the rounding delta starts at zero. | N-U30-050 |
| VDR-U30-C143 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2292 | self._round_tax_details_tax_amounts(base_lines, company) | FACT | always | — | Three document-level steps follow in order: tax amounts per tax, base amounts per line, then alignment to existing tax items. | N-U30-053 |
| VDR-U30-C144 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1925 | 'computation_key': base_line['computation_key'] | FACT | always | — | Global tax rounding groups lines by tax, currency, refund flag, reverse-charge flag, price-included flag and computation key, so down-payment and discount subsets round separately. | N-U30-053 |
| VDR-U30-C145 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1944 | delta_total_tax_amount = rounded_raw_total_tax_amount - total_tax_amount | FACT | round globally | — | Per group and per currency the delta is the rounded raw target total minus the sum of the already rounded line tax amounts; it is shared over the tax data in proportion to the raw tax amounts. | N-U30-053 |
| VDR-U30-C146 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1966 | mode == 'included' | FACT | round globally | — | For price-included groups the base delta is derived by rounding base plus tax and subtracting the tax; for price-excluded groups the base total is rounded on its own; the delta is shared over the tax data in proportion to raw base amounts. | N-U30-054 |
| VDR-U30-C147 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2041 | not tax_data | FACT | round globally | — | Base-line delta mode is included unless a line has a price-excluded tax with a non-zero amount, in which case that group rounds on total excluded (lines 2037-2050). | N-U30-054 |
| VDR-U30-C148 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2057 | if current_mode == 'excluded' | FACT | round globally | — | Excluded branch: the target is the raw total excluded; the delta versus the sum of rounded lines is shared over lines by their raw total excluded. | N-U30-054 |
| VDR-U30-C149 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2074 | Price-included rounding. | FACT | round globally | — | Included branch: the target is the raw total excluded plus raw tax, the delta versus the rounded total included is shared over lines by their raw total included. | N-U30-054 |
| VDR-U30-C150 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2103 | base_line['tax_details'][f'delta_total_excluded{delta_currency_indicator}'] += amount_to_distribute | FACT | always | — | The base delta is stored on the line as a delta of total excluded per currency and added to the item balance when base items are updated. | N-U30-059 |
| VDR-U30-C151 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2121 | total_per_tax_line_key = defaultdict | FACT | existing tax items kept | — | When existing tax items are supplied the target per tax, currency and refund flag is the sum of their signed amounts; the difference to the current computed tax is shared over the tax data in proportion to current amounts. | N-U30-055 |
| VDR-U30-C152 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2131 | tax_line_key = (tax.id, currency.id, tax_rep.document_type | INFERENCE | existing tax items kept | — | INFERENCE (lines 2131-2134): the alignment key excludes the distribution line, so a manual change to one of several distribution lines of a tax is redistributed over the tax as a whole. | N-U30-048 |
| VDR-U30-C153 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2161 | if not current_total_tax_amount | FACT | existing tax items kept | — | Alignment is skipped for a tax whose current computed total is zero (nothing to redistribute over). | N-U30-062 |
| VDR-U30-C154 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2110 | Only added python-side | FACT | always | — | Alignment to existing tax items and tax-item preparation exist only on the server; the client-side mirror of the engine has no such step, so a client preview of a document with edited tax items may differ. | N-U30-061 |
| VDR-U30-C155 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1835 | factors.sort(key=lambda x: x[1], reverse=True) | FACT | always | — | Delta distribution orders targets by absolute factor, largest first; whole smallest units are assigned by proportion, remaining units go one each to the largest targets in that order. | N-U30-053 |
| VDR-U30-C156 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1837 | 1 / len(factors) | FACT | all factors zero | — | If every factor is zero the weights are equal. | N-U30-053 |
| VDR-U30-C157 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1866 | amounts_to_distribute = [0.0] * len(target_factors) | FACT | delta below one unit | — | A delta that is zero at the currency precision distributes nothing. | N-U30-053 |
| VDR-U30-C158 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2445 | sorted_tax_reps_data = sorted( | FACT | tax with several distribution lines | — | A tax amount is split over its distribution lines by factor and rounded per line in each currency; the remaining difference is distributed over the lines, largest first. | N-U30-056 |
| VDR-U30-C159 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3059 | will not change whatever the number | FACT | always | — | Per the preparation notes the total tax amount does not change however many accounting grouping keys result; rounding is allocated before aggregation into tax items. | N-U30-057 |
| VDR-U30-C160 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:931 | line.price_subtotal = base_line['tax_details']['total_excluded_currency'] | FACT | always | — | A line subtotal and total are computed on that single line (to show on draft documents) and so exclude the document-level rounding delta, whereas the item balance includes it. | N-U30-058 |
| VDR-U30-C161 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:916 | outside of `_sync_tax_lines` | FACT | always | — | The line subtotal and total are computed outside the synchroniser so users see them before the document is saved. | N-U30-058 |
| VDR-U30-C162 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2223 | balance = 17.80 | FACT | documentation example | — | The engine documentation shows a worked case where the line subtotal is 17.79 while the accounting balance of that line is 17.80 because of the global delta. | N-U30-063 |
| VDR-U30-C163 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2185 | def _round_base_lines_tax_details | INFERENCE | always | — | INFERENCE (whole rounding entry 2185-2294): the system implements a document-level allocation of rounding, not a rule on the third decimal of the tax amount; any agreement with the statutory rounding statement S12-08 needs separate verification. | N-U30-064 |
| VDR-U30-C164 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3163 | The cash rounding has been removed | FACT | no cash rounding method | — | If the document has no cash-rounding method any rounding item is deleted. | N-U30-070 |
| VDR-U30-C165 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3171 | old_strategy = 'biggest_tax' | FACT | strategy changed | — | The previous strategy is inferred from whether the existing rounding item has an originator tax; on change the old item is deleted and a new one built. | N-U30-070 |
| VDR-U30-C166 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3177 | others_lines -= existing_cash_rounding_line | FACT | always | — | The amount rounded is the sum of foreign amounts of all items that are not receivable or payable, excluding the existing rounding item. | N-U30-070 |
| VDR-U30-C167 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3101 | self.invoice_date or self.date | FACT | foreign-currency document | — | The company-currency amount of the rounding difference is converted at the market rate on the invoice date (else the accounting date), not at the document rate stored on the invoice. | N-U30-071 |
| VDR-U30-C168 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3184 | The invoice is already rounded | FACT | always | — | If the difference is zero in both currencies the rounding item is removed; if the existing item already has the same amounts nothing is written. | N-U30-070 |
| VDR-U30-C169 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3123 | if self.invoice_cash_rounding_id.strategy == 'biggest_tax' | FACT | strategy largest tax | — | Largest-tax strategy: the item copies account, distribution line, tags and taxes of the tax item with the largest absolute balance and is named after that tax; without any tax item no rounding item is created. | N-U30-070 |
| VDR-U30-C170 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3141 | elif self.invoice_cash_rounding_id.strategy == 'add_invoice_line' | FACT | strategy add a line | — | Add-a-line strategy: the item has no taxes and sits on the loss account when the difference is positive and a loss account exists, otherwise on the profit account (both company-dependent). | N-U30-077 |
| VDR-U30-C171 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3251 | if invoice.state != 'posted' | FACT | always | — | Rounding items are recomputed only for non-posted invoices. | N-U30-074 |
| VDR-U30-C172 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3120 | 'display_type': 'rounding' | FACT | always | — | The rounding item is typed rounding, carries the commercial partner and the document currency, and is created or rewritten in place. | N-U30-070 |
| VDR-U30-C173 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2771 | invoice_cash_rounding_id.strategy == 'add_invoice_line' and not move.invoice_cash_rounding_id.profit_account_id | FACT | form edit | — | Selecting the add-a-line strategy without a profit account only raises an on-screen warning; no constraint prevents saving. | N-U30-079 |
| VDR-U30-C174 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:59 | def compute_difference | FACT | always | — | The rounding difference is the amount rounded to the coin with the chosen tie rule minus the amount, both first rounded to the currency precision. | N-U30-065 |
| VDR-U30-C175 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:48 | strictly positive rounding value | FACT | always | — | The rounding precision must be strictly positive; strategies are modify tax amount or add a rounding line; rounding methods are up, down or nearest. | N-U30-078 |
| VDR-U30-C176 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:3 | access_account_cash_rounding_uinvoice | FACT | always | — | Cash-rounding methods are editable by the invoicing group and readable by the read-only accounting group; the field on the document is shown only to the cash-rounding group and is read-only after draft. | N-U30-075 |
| VDR-U30-C177 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:86 | Allow the cash rounding management | FACT | always | — | A dedicated group controls access to cash-rounding management. | N-U30-075 |
| VDR-U30-C178 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:1555 | groups="account.group_cash_rounding" | FACT | always | — | The document field is visible only for the cash-rounding group and is read-only unless the document is a draft. | N-U30-075 |
| VDR-U30-C179 | FUNCTION MAPPING REQUIRED | account/models/account_cash_rounding.py:15 | _name = 'account.cash.rounding' | OBSERVATION | restored database | — | OBSERVATION (dump): zero cash-rounding methods are defined; the DB holds two access rows for the model (invoicing full, read-only read). | N-U30-075 |
| VDR-U30-C180 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1083 | l.move_id.invoice_payment_term_id.early_discount | FACT | early discount, mixed mode | — | Early-payment items are needed only for taxed product items on a document whose payment term has an early discount in mixed computation mode. | N-U30-066 |
| VDR-U30-C181 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1089 | def grouping_function | FACT | mixed mode | — | Early-payment amounts are grouped by account, analytic distribution and the set of taxes of the product item. | N-U30-066 |
| VDR-U30-C182 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3159 | return self.amount_type not in ('fixed', 'code') | FACT | always | — | Fixed-amount and code taxes are excluded from the early-payment computation (they are not discountable). | N-U30-066 |
| VDR-U30-C183 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1135 | epd_amount_currency = currency.round | FACT | mixed mode | — | The early-payment amount per group is the direction sign times the group total excluded times the discount percentage, rounded in each currency. | N-U30-066 |
| VDR-U30-C184 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1144 | grouping_key_counterpart = frozendict | FACT | mixed mode | — | Per group two items are needed: one with the taxes and tags of the group and an opposite counterpart with taxes cleared; both are named after the discount percentage. | N-U30-066 |
| VDR-U30-C185 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1177 | AccountTax._distribute_delta_amount_smoothly( | FACT | mixed mode | — | The group amount is distributed over the invoice lines by raw total excluded, separately for document and company currency, using the smooth-delta algorithm. | N-U30-066 |
| VDR-U30-C186 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1065 | pay_term.early_pay_discount_computation == 'mixed' | FACT | mixed mode | — | An existing early-payment item has a key (account, analytic distribution, taxes, tags, document) only in mixed mode. | N-U30-066 |
| VDR-U30-C187 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3755 | existing_key_fname='epd_key' | FACT | always | — | The early-payment synchroniser is entry 70 and uses the item-level needed and dirty fields, keyed by account, analytic distribution, taxes and tags. | N-U30-004 |
| VDR-U30-C188 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1642 | Anticipate the epd lines | FACT | unsaved document | — | For an unsaved document the early-payment items are anticipated from the base lines so the totals summary is right before saving. | N-U30-066 |
| VDR-U30-C189 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5096 | tax_lines_needed = early_pay_discount_computation == 'included' | OBSERVATION | restored database | — | OBSERVATION (dump): the ten payment terms all use the included computation and one has an early discount; no mixed-mode items therefore arise in the Thai configuration, and the included mode creates its tax correction only when the payment is registered. | N-U30-076 |
| VDR-U30-C190 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5123 | remaining_part_to_consider | FACT | included mode, payment with discount | — | At payment the base lines are recomputed at unit price times the remaining percentage as refund items, excluding fixed taxes; the difference to the original base is the discount base item. | N-U30-072 |
| VDR-U30-C191 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5131 | cash_discount_account = company.account_journal_early_pay_discount_loss_account_id | FACT | included mode | — | Discount base items go to the loss account for inbound documents and to the gain account for outbound documents (both set in the dump). | N-U30-072 |
| VDR-U30-C192 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5211 | 'name': _("Early Payment Discount (%s)", tax.name) | FACT | included mode with taxes | — | Tax correction items use the inverse distribution line of each tax and are proportional to the share paid; named after the tax. | N-U30-072 |
| VDR-U30-C193 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5082 | def inverse_tax_rep | FACT | included mode with taxes | — | The inverse distribution line is the line at the same index in the opposite document-type set of the same tax. | N-U30-072 |
| VDR-U30-C194 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5231 | biggest_base_line = max | FACT | included mode | — | Any rounding residual between the discounted term amount and the generated items is added to the largest base item in both currencies. | N-U30-072 |
| VDR-U30-C195 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5298 | Early Payment Discount (Exchange Difference) | FACT | foreign currency payment with discount | — | A residual in company currency after the discount items is posted as an exchange-difference item on the gain or loss exchange account. | N-U30-072 |
| VDR-U30-C196 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6992 | account_discount_expense_allocation_id | FACT | always | — | Discount allocation is active only when the company configures a separate discount account (expense side for sales, income side for purchases); the dump has neither set. | N-U30-067 |
| VDR-U30-C197 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1011 | (discount_allocation_account, -amount_currency | FACT | discount account set, line with discount | — | Per product item with a discount two items are needed: the discount amount on the item account and the opposite amount on the allocation account, in both currencies, with analytic shares weighted. | N-U30-067 |
| VDR-U30-C198 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3746 | existing_key_fname='discount_allocation_key' | FACT | always | — | Discount-allocation items are synchronised as entry 40, keyed by account, document and rate. | N-U30-067 |
| VDR-U30-C199 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3222 | balance_name = _('Automatic Balancing Line') | FACT | non-posted entry using taxes | — | An automatic balancing item is created or updated on non-posted entries that have or had taxes; its balance is whatever makes the entry balanced, it carries no taxes and sits on the journal default account else the suspense account. | N-U30-068 |
| VDR-U30-C200 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3213 | only manage automatically unbalanced when | FACT | always | — | Entries without taxes before and after the change are not auto-balanced; they must balance by themselves. | N-U30-068 |
| VDR-U30-C201 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3216 | taxes have been removed | FACT | entry whose taxes were all removed | — | If all taxes were removed from the entry, its tax items are deleted and the tags cleared on all items because the tax synchroniser is inactive. | N-U30-073 |
| VDR-U30-C202 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3197 | def _get_automatic_balancing_account | FACT | always | — | Balancing account is the journal default account when set, else the company suspense account. | N-U30-068 |
| VDR-U30-C203 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:599 | tax_totals = fields.Binary( | FACT | always | — | The totals summary is a computed, non-stored, non-exportable field with an inverse that lets users edit tax group amounts. | N-U30-088 |
| VDR-U30-C204 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1827 | 'invoice_line_ids.currency_rate' | FACT | always | — | The summary depends on line rates, tax base amounts, originator tax, line totals, payment term, partner, currency and the language of the context. | N-U30-088 |
| VDR-U30-C205 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1847 | cash_rounding=move.sudo().invoice_cash_rounding_id | FACT | invoice-like | — | The summary is computed from the rounded base lines of the document with existing tax items kept (default round-from-tax-lines true), the document currency and the cash-rounding method read with elevated rights. | N-U30-081 |
| VDR-U30-C206 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1857 | move.tax_totals = None | FACT | ordinary entry | — | Ordinary entries have no totals summary. | N-U30-081 |
| VDR-U30-C207 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1849 | move.tax_totals['display_in_company_currency'] = ( | FACT | always | — | A flag requests a second summary in company currency when the company option is on, the currency differs, tax groups exist and the document is a sales document (re-read of VDR-TXA1-C112). | N-U30-086 |
| VDR-U30-C208 | FUNCTION MAPPING REQUIRED | account/models/company.py:153 | display_invoice_tax_company_currency | OBSERVATION | restored database | — | OBSERVATION (default True; dump company row true): taxes in company currency are shown on foreign-currency sales documents. | N-U30-086 |
| VDR-U30-C209 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2808 | tax_totals_summary['base_amount_currency'] += values['total_excluded_currency'] | FACT | always | — | The global base is the sum of line total excluded (including the rounding delta) over all lines and the global tax is the sum of rounded tax amounts, in both currencies. | N-U30-081 |
| VDR-U30-C210 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2592 | excluded_rounded_amount = tax_details[excluded_rounded_field] + tax_details[excluded_delta_field] | FACT | always | — | Aggregated rounded base includes the stored global-rounding delta so totals equal the rounded document figures. | N-U30-058 |
| VDR-U30-C211 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2634 | for tax in tax_data | FACT | taxes affecting later taxes | — | Tax amounts of a tax that affects the base of later taxes are propagated into those taxes base when aggregating per group. | N-U30-084 |
| VDR-U30-C212 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2830 | key=lambda values: (values['grouping_key'].sequence, values['grouping_key'].id) | FACT | always | — | Tax groups are ordered by group sequence then identifier (re-read of VDR-TXA1-C072). | N-U30-083 |
| VDR-U30-C213 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2873 | preceding_subtotal = tax_group.preceding_subtotal or untaxed_amount_subtotal_label | FACT | always | — | A group appears under its preceding-subtotal label, defaulting to Untaxed Amount; each subtotal base adds the taxes of earlier subtotals. | N-U30-083 |
| VDR-U30-C214 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2814 | untaxed_amount_subtotal_label = _("Untaxed Amount") | OBSERVATION | restored database | — | OBSERVATION (dump): five tax groups (four withholding percentages and VAT 7%) all share sequence ten, none has a preceding-subtotal label, so one subtotal is shown and groups appear in identifier order with the withholding groups before VAT. | N-U30-083 |
| VDR-U30-C215 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2899 | subtotal['base_amount_currency'] = tax_totals_summary['base_amount_currency'] + accumulated_tax_amount_currency | FACT | always | — | Each subtotal base equals the untaxed base plus tax accumulated in previous subtotals. | N-U30-083 |
| VDR-U30-C216 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2909 | cash_rounding_lines = [base_line | FACT | rounding items exist | — | If rounding items already exist the cash-rounding amounts are read from them; otherwise they are estimated from the document cash-rounding method (line 2917). | N-U30-085 |
| VDR-U30-C217 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2930 | rate = abs(total_amount_currency / total_amount) | INFERENCE | estimated cash rounding | RT | INFERENCE (lines 2930-2931 versus AM 3101): the estimated company amount of the rounding uses the rate implied by the document totals, whereas the stored rounding item uses the market rate at the invoice date; the two may differ for a foreign-currency document with a manual rate. Needs execution. | N-U30-071 |
| VDR-U30-C218 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2963 | Subtract the cash rounding from | FACT | cash rounding present | — | The cash-rounding delta is subtracted from untaxed bases and added back in the total, so Rounding is displayed separately from untaxed amount. | N-U30-085 |
| VDR-U30-C219 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3002 | tax_totals_summary['total_amount_currency'] = | FACT | always | — | Total = untaxed base + tax + cash rounding, in each currency. | N-U30-081 |
| VDR-U30-C220 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2575 | first_tax_line.amount_currency -= delta_amount * sign | FACT | tax group amount edited | — | Editing a group tax amount changes the amount in currency of the first tax item of that group by the difference (non-deductible share excluded from the delta); the balance follows through the line synchroniser and document amounts are recomputed. | N-U30-092 |
| VDR-U30-C221 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2552 | with self._sync_dynamic_line( | INFERENCE | tax group amount edited | — | INFERENCE (lines 2549-2558): the recursion check exits before the payment-term synchroniser is entered, so the payment-term synchroniser always runs after a totals edit even when the recursion guard would have disabled synchronisation. | N-U30-017 |
| VDR-U30-C222 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:1362 | and not quick_edit_mode | FACT | form view | — | The totals widget is editable only in draft and only for vendor documents or in quick-encoding mode. | N-U30-091 |
| VDR-U30-C223 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1222 | move.amount_untaxed = sign * total_untaxed_currency | FACT | always | — | Untaxed, tax, total, residual and the signed company-currency amounts are stored computed fields derived from item amounts; the line subtotal and total and the tax base amount are stored; the summary structure is not. | N-U30-088 |
| VDR-U30-C224 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:222 | tax_base_amount = fields.Monetary( | FACT | always | — | A tax item stores its base amount in company currency (read-only). | N-U30-088 |
| VDR-U30-C225 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:373 | account.document_tax_totals | FACT | invoice print | — | The invoice print shows the summary in document currency and, when flagged, a second summary in company currency; a Rounding row appears only when the summary has a cash-rounding amount. | N-U30-089 |
| VDR-U30-C226 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:3 | inherit_id="account.report_invoice_document" | FACT | l10n_th installed (it is) | — | The Thai invoice print inherits the generic document and replaces only the title and branch details; its totals blocks are the generic ones. | N-U30-089 |
| VDR-U30-C227 | FUNCTION MAPPING REQUIRED | account/views/report_invoice.xml:417 | o.tax_totals.get('display_in_company_currency') | FACT | invoice print | — | The company-currency block prints only when the summary flags it. | N-U30-086 |
| VDR-U30-C228 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:801 | def _compute_tax_totals | FACT | sale installed | — | Sales orders compute the same summary from order lines (plus early-payment base lines) with the same engine and rounding, but have no journal items to keep. | N-U30-090 |
| VDR-U30-C229 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:255 | def _compute_tax_totals | FACT | purchase installed | — | Purchase orders compute the same summary from order lines with the same engine. | N-U30-090 |
| VDR-U30-C230 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2727 | def _get_tax_totals_summary | INFERENCE | always | — | INFERENCE (whole function 2727-3007): the summary arranges amounts by tax group in both currencies; whether that presentation satisfies a statutory tax-invoice layout is a TXS question, not decided here (S12-08 rounding, S12-04 rate). | N-U30-094 |
| VDR-U30-C231 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection( | FACT | always | — | A tax is exigible on invoice (default) or on payment; the on-payment option needs a cash-basis transition account (re-read of VDR-TXA1-C009). | N-U30-106 |
| VDR-U30-C232 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:267 | _constrains_cash_basis_transition_account | FACT | on-payment tax, not during chart load | — | An on-payment tax whose transition account does not allow reconciliation is refused, except while a chart template loads. | N-U30-109 |
| VDR-U30-C233 | FUNCTION MAPPING REQUIRED | account/models/company.py:220 | tax_exigibility = fields.Boolean(string='Use Cash Basis') | FACT | always | — | The company switch Use Cash Basis and the fields cash-basis journal and base-tax-received account configure the mechanism. | N-U30-106 |
| VDR-U30-C234 | FUNCTION MAPPING REQUIRED | account/models/company.py:316 | 'tax_exigibility', | FACT | company tree | — | The switch is delegated to the root company, so branches share it (re-read of VDR-TXA1-C176). | N-U30-106 |
| VDR-U30-C235 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:276 | if not self.tax_exigibility and tax: | FACT | settings screen | — | The switch cannot be turned off in settings while any tax of the company is on payment. | N-U30-106 |
| VDR-U30-C236 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:763 | if not company.parent_id and self.env | FACT | chart load | — | Loading a chart sets the switch only when an on-payment tax exists; it also assigns the Cash Basis journal to the company when none is set (line 717). | N-U30-106 |
| VDR-U30-C237 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | FACT | l10n_th installed | — | The Thai template data sets the company switch on explicitly, independent of the generic rule that requires an on-payment tax (re-read of VDR-TXA1-C186). | N-U30-107 |
| VDR-U30-C238 | FUNCTION MAPPING REQUIRED | account/models/company.py:220 | tax_exigibility = fields.Boolean(string='Use Cash Basis') | OBSERVATION | restored database | — | OBSERVATION (dump): company switch true; cash-basis journal set (journal code CABA); base-tax-received account not set; all 18 taxes are on invoice and none has a transition account. | N-U30-107 |
| VDR-U30-C239 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5379 | self.tax_id.tax_exigibility == 'on_payment' | FACT | on-payment tax | — | At invoice time the tax item account is the transition account for an on-payment tax (unless the caba_no_transition_account context key is set; no caller found). | N-U30-095 |
| VDR-U30-C240 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2412 | include_caba_tags or tax.tax_exigibility == 'on_invoice' | FACT | always | — | Report tags are put on invoice items only for on-invoice taxes unless cash-basis tags are requested; cash-basis taxes receive their tags on the cash-basis entry. | N-U30-095 |
| VDR-U30-C241 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1019 | record.always_tax_exigible = not record.is_invoice(True) | FACT | always | — | Always-exigible is stored true for a non-invoice entry that has nothing to process (no on-payment items, or no receivable or payable item); exchange-difference entries set it explicitly true (item model line 3027). | N-U30-108 |
| VDR-U30-C242 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1591 | cannot be mixed on the same | FACT | item with both kinds of taxes sharing a base tag | — | An item with an on-payment and an on-invoice tax that share base tags (or a tax affecting another of different exigibility) is refused. | N-U30-103 |
| VDR-U30-C243 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4169 | elif line.tax_line_id.tax_exigibility == 'on_payment' | FACT | always | — | Per document, tax items of on-payment taxes are processed with treatment tax and base items whose taxes include an on-payment tax (also inside a group) with treatment base. | N-U30-095 |
| VDR-U30-C244 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4173 | flatten_taxes_hierarchy() | FACT | always | — | Group taxes are flattened so an on-payment child inside a group marks the base item for cash-basis processing. | N-U30-095 |
| VDR-U30-C245 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4177 | if not values['to_process_lines'] or not has_term_lines | FACT | always | — | Nothing is collected when there is no cash-basis item or no receivable or payable item. | N-U30-097 |
| VDR-U30-C246 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4184 | multiple involved currencies | FACT | always | — | Cash-basis processing is unsupported (silently skipped) when the processed items and term items span more than one currency. | N-U30-097 |
| VDR-U30-C247 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4188 | values['is_fully_paid'] = | FACT | always | — | Fully paid means the residual is zero in company currency or in the processing currency. | N-U30-098 |
| VDR-U30-C248 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2894 | def is_cash_basis_needed(amls): | FACT | always | — | After partials are created the plan checks whether any involved company has the switch on and the account is receivable or payable (re-read of VDR-U12-C149). | N-U30-097 |
| VDR-U30-C249 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2898 | not self.env.context.get('move_reverse_cancel') | FACT | always | — | Cash-basis creation is skipped for reversals that cancel (move_reverse_cancel) and when the caller passes no_cash_basis; the automatic-entry wizard and marked reconciliation pass it. | N-U30-105 |
| VDR-U30-C250 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2901 | no_exchange_difference_no_recursive=False | FACT | always | — | The cash-basis creation is invoked with exchange differences re-enabled so exchange differences on the new entries are produced. | N-U30-131 |
| VDR-U30-C251 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2902 | plan['partials']._set_draft_caba_move_vals() | FACT | always | — | After creation the partials store a JSON snapshot of the cash-basis lines and totals of both documents for later comparison. | N-U30-104 |
| VDR-U30-C252 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:721 | 'debit_caba_lines' | FACT | always | — | The snapshot holds, for each side, the processed lines with treatment and the total balance and amount in currency. | N-U30-104 |
| VDR-U30-C253 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:276 | no tax cash basis journal | FACT | a document needs cash-basis processing | — | If a cash-basis entry is needed but the company has no cash-basis journal, reconciliation fails with a user error pointing to the settings (re-read of VDR-U12-C150). | N-U30-109 |
| VDR-U30-C254 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:260 | for field, counterpart_field in | FACT | always | — | Each partial is evaluated for both documents involved, so a payment and an invoice, or an invoice and a credit note, can each generate entries. | N-U30-097 |
| VDR-U30-C255 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:302 | reconciling a refund with an invoice | FACT | invoice with credit note | — | When two business documents are matched, each uses its own rates and the settlement date is the later of the two items. | N-U30-100 |
| VDR-U30-C256 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:311 | settlement_date = payment_date | FACT | payment against document | — | For a payment the settlement date is the date of the counterpart item. | N-U30-100 |
| VDR-U30-C257 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:319 | Percentage made on company's currency | FACT | processing currency equals company currency | — | Percentage paid is the partial amount over the document total balance in company currency; a zero partial (exchange difference only) is skipped. | N-U30-098 |
| VDR-U30-C258 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:326 | Percentage made on foreign currency | FACT | foreign processing currency | — | For a foreign-currency document the percentage is the partial amount in currency over the total in currency. | N-U30-098 |
| VDR-U30-C259 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:329 | source_line.currency_id != counterpart_line.currency_id | FACT | always | — | If the two items differ in currency the rate is taken at the payment date (or forced by the payment wizard); otherwise it is the ratio of the counterpart foreign amount to its company amount; zero when absent. | N-U30-099 |
| VDR-U30-C260 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:554 | move_date = max(partial_values | FACT | always | — | The entry is dated the settlement date but not earlier than the day after the user fiscal lock date; it references the origin document name, carries its fiscal position and links to the partial and the origin document (re-read of VDR-TXA1-C270). | N-U30-100 |
| VDR-U30-C261 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:546 | amount_residual_per_tax_line = { | FACT | always | — | The residual foreign amount of each tax item is tracked across the partials of the same run. | N-U30-098 |
| VDR-U30-C262 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:579 | amount_currency = line.currency_id.round(line.amount_currency * partial_values | FACT | always | — | Each processed item is mirrored for the paid share: foreign amount times percentage, rounded in the item currency. | N-U30-098 |
| VDR-U30-C263 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:589 | put the remaining amount to | FACT | last partial of a fully paid document or smaller residual | — | For tax items on the last partial, if the document is fully paid or the residual is smaller than the share, the remaining residual is used so the cash-basis entries add up exactly; base items have no such correction. | N-U30-098 |
| VDR-U30-C264 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:593 | balance = partial_values | FACT | always | — | The company-currency amount is the foreign amount divided by the payment rate (zero when the rate is zero); it is not rounded here and takes the company rounding when the item is created. | N-U30-099 |
| VDR-U30-C265 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:375 | account = base_line.company_id.account_cash_basis_base_account_id or base_line.account_id | FACT | always | — | A base item of the entry is on the company base-tax-received account, else on the original base account, carries the base tags of the on-payment taxes and the product tags. | N-U30-101 |
| VDR-U30-C266 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:407 | 'debit': cb_base_line_vals['credit'] | FACT | always | — | Each base item is mirrored by an opposite counterpart on the same account so base lines add tags without moving balance. | N-U30-101 |
| VDR-U30-C267 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:440 | 'account_id': tax_line.tax_repartition_line_id.account_id.id | FACT | always | — | A tax item of the entry goes to the distribution-line account, else the company base account, else the original tax item account; it carries base tags, distribution tags, product tags and the base amount. | N-U30-101 |
| VDR-U30-C268 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:462 | 'account_id': tax_line.account_id.id | FACT | always | — | The counterpart of a tax item is on the original tax item account (the transition account), so the paid share of tax moves from transition to the final account. | N-U30-101 |
| VDR-U30-C269 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:618 | if grouping_key in partial_lines_to_create | FACT | always | — | Items with the same grouping key (currency, partner, account, on-payment taxes, distribution line, analytic) are aggregated to limit the number of lines; tax base amounts add up. | N-U30-101 |
| VDR-U30-C270 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:666 | if tax_line.account_id.reconcile | FACT | tax item account reconcilable | — | When the original tax item is on a reconcilable account (the transition account) the counterpart is queued for reconciliation with it. | N-U30-102 |
| VDR-U30-C271 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:685 | skip_invoice_line_sync=True | FACT | always | — | Entries are created with the document synchronisation, line synchronisation and business-model synchronisation switched off, so no tax items are derived on them. | N-U30-104 |
| VDR-U30-C272 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:690 | moves[:len(moves_to_create_and_post)]._post(soft=False) | FACT | both documents posted | — | Entries are posted immediately only when both reconciled documents are posted; otherwise they stay draft. | N-U30-104 |
| VDR-U30-C273 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:712 | with_context(add_caba_vals=True)._reconcile_plan(reconciliation_plan) | FACT | always | — | The transition-account items of the origin and entry are then reconciled with a plan that records cash-basis values on any exchange difference. | N-U30-102 |
| VDR-U30-C274 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2972 | if not full_batch.get('caba_lines_to_reconcile') | INFERENCE | always | RT | INFERENCE (search of all addon sources): the full-batch keys caba_lines_to_reconcile and exchange_move are read here but no Community code sets them, so this rounding auto-reconciliation branch is never entered; behaviour of tax-account rounding on full reconcile is unconfirmed without execution. | N-U30-112 |
| VDR-U30-C275 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5744 | draft invoice changed since it | FACT | posting a draft with partials | — | When a draft document with partials is posted, partials whose cash-basis snapshot no longer matches are dissolved (the user must reconcile again); otherwise the related draft entries are posted. | N-U30-104 |
| VDR-U30-C276 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:117 | self.env['account.move'].search([('tax_cash_basis_rec_id', 'in', self.ids)]) | FACT | matching undone | — | Undoing a partial reverses its non-draft cash-basis entries (and exchange entries) on their own date, or the day after the latest violated lock, and deletes draft ones (re-read of VDR-U12-C154, C155). | N-U30-105 |
| VDR-U30-C277 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:148 | not_draft_moves._reverse_moves(default_values_list, cancel=True) | FACT | matching undone | — | The reversal is created with cancel semantics, i.e. posted and reconciled with the entry it reverses. | N-U30-105 |
| VDR-U30-C278 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6371 | reset to draft a tax cash | FACT | always | — | A cash-basis entry cannot be reset to draft, even after its matching was undone (re-read of VDR-TXA2-C031). | N-U30-105 |
| VDR-U30-C279 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5544 | posted_caba_entry = self.state | FACT | always | — | A posted cash-basis or exchange-difference entry is not deletable; deletion falls back to reversal (re-read of VDR-TXA2-C100). | N-U30-105 |
| VDR-U30-C280 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:886 | open_created_caba_entries | FACT | document has cash-basis entries | — | A smart button on the origin document lists the cash-basis entries it generated. | N-U30-095 |
| VDR-U30-C281 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3456 | def _get_tax_exigible_domain | FACT | always | — | A domain helper defines exigible items (always-exigible moves, items with only tags, items of cash-basis entries, items of non-cash-basis taxes); no Community module calls it. | N-U30-108 |
| VDR-U30-C282 | FUNCTION MAPPING REQUIRED | account/models/account_move_line_tax_details.py:405 | tax_exigible | FACT | always | — | The tax-details query marks an item exigible when its tax is not on-payment, or it belongs to a cash-basis entry, or the move is always exigible. | N-U30-108 |
| VDR-U30-C283 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:67 | only_tax_exigible = fields.Boolean( | FACT | always | — | Reports carry an option to include only exigible items; the evaluation of the option belongs to the report engine, not read here. | N-U30-108 |
| VDR-U30-C284 | FUNCTION MAPPING REQUIRED | account/data/account_reports_data.xml:11 | only_tax_exigible | OBSERVATION | restored database | — | OBSERVATION (dump): all six account reports, including the Thai tax report and the two withholding reports, have the only-exigible option true; since no tax is on payment the filter excludes nothing. Whether the engine honours it is outside Community. | N-U30-108 |
| VDR-U30-C285 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:98 | access_account_partial_reconcile_group_invoice | FACT | always | — | Matching records are creatable and deletable by the invoicing group (and the accounting user and administrator); read-only for the read-only accounting group; the dump has six access rows for the model. | N-U30-110 |
| VDR-U30-C286 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:67 | only_tax_exigible = fields.Boolean( | UNKNOWN | report engine outside Community | RT | UNKNOWN — EVIDENCE INSUFFICIENT: how the tax report treats exigibility and how Thai VAT and withholding reports would consume cash-basis entries needs the report engine (not in Community) or execution. | N-U30-112 |
| VDR-U30-C287 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3818 | if move.move_type in ('out_invoice', 'in_invoice'): | FACT | duplication or reversal of an invoice | — | Copying an invoice or bill keeps only create commands for its items, so tax and payment-term items are copied as items rather than relinked. | N-U30-113 |
| VDR-U30-C288 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2090 | Will be recomputed from the price_unit | FACT | copy of an invoice item | — | In a copy of an invoice the product item balance is dropped to be recomputed from the unit price and the payment-term item name is not copied; other items (tax) keep their copied values. | N-U30-113 |
| VDR-U30-C289 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5510 | lines.remove_move_reconcile() | FACT | reversal with cancel | — | A cancelling reversal first removes all reconciliations of the originals (which dissolves their cash-basis entries). | N-U30-119 |
| VDR-U30-C290 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5522 | skip_invoice_sync=move.move_type == 'entry' | FACT | always | — | Reversing an ordinary entry copies it without synchronisation; invoices copy with synchronisation active. | N-U30-113 |
| VDR-U30-C291 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5532 | or line.display_type == 'cogs' | FACT | always | — | Amounts are negated explicitly only for ordinary entries and cost items; invoices change type to the credit-note type instead. | N-U30-113 |
| VDR-U30-C292 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5537 | reverse_moves.with_context(move_reverse_cancel=cancel)._post(soft=False) | FACT | cancelling reversal | — | A cancelling reversal is posted at once and reconciled with the original, without creating cash-basis entries (move_reverse_cancel). | N-U30-119 |
| VDR-U30-C293 | FUNCTION MAPPING REQUIRED | account/wizard/account_move_reversal.py:146 | line[2]['display_type'] in ('product' | FACT | reverse and modify | — | When a replacement is created from an invoice only product, section, subsection and note items are copied, so tax and payment-term items are rebuilt by the synchroniser. | N-U30-121 |
| VDR-U30-C294 | FUNCTION MAPPING REQUIRED | account/wizard/account_move_reversal.py:94 | mixed_payment_term = move.invoice_payment_term_id.id | FACT | reversal wizard | — | A credit note keeps the payment term only when its early discount is in mixed mode; otherwise no payment term is set. | N-U30-120 |
| VDR-U30-C295 | FUNCTION MAPPING REQUIRED | account/wizard/account_move_reversal.py:128 | is_cancel_needed = not is_auto_post and | FACT | reversal wizard | — | Only reverse-and-modify and entry reversals cancel immediately; a credit note of an invoice is created as a separate draft document to be posted and matched later. | N-U30-119 |
| VDR-U30-C296 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6068 | 'fiscal_position_id': move.fiscal_position_id.id | FACT | draft never numbered | — | Switching between invoice and credit note rewrites type, currency and fiscal position, which forces a full recomputation of tax items and discards manual tax amounts (type change triggers full recompute). | N-U30-115 |
| VDR-U30-C297 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6073 | if move.amount_total < 0 | FACT | draft never numbered | — | If the total is negative after switching, product quantities and their extra tax data are negated so the resulting document has a positive total. | N-U30-115 |
| VDR-U30-C298 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6059 | switch the type of a document | FACT | always | — | Switching is refused for documents that have a sequence number and for ordinary entries. | N-U30-122 |
| VDR-U30-C299 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6280 | self.state = 'draft' | FACT | always | — | Resetting to draft changes the state only; stored tax and payment-term items are left as they are and are re-derived only when an input is next changed. | N-U30-118 |
| VDR-U30-C300 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6394 | self.line_ids.remove_move_reconcile() | FACT | always | — | Cancelling removes the reconciliations of the document (dissolving its cash-basis entries), sets the state of payments whose journal entry is this document to cancelled, and sets the document to cancelled; items are not recomputed. | N-U30-119 |
| VDR-U30-C301 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1049 | move.fiscal_position_id = self.env['account.fiscal.position'] | FACT | partner, delivery address, company or type change | — | The fiscal position is computed from partner and delivery address (purchase receipts take the company receipt position) and stays editable. | N-U30-116 |
| VDR-U30-C302 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:955 | @api.depends('product_id', 'product_uom_id') | FACT | always | — | Line taxes are recomputed (with fiscal-position mapping) only when the product or unit changes; a change of fiscal position alone does not recompute existing line taxes. | N-U30-123 |
| VDR-U30-C303 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:990 | if tax_ids and self.move_id.fiscal_position_id | FACT | always | — | When defaults are computed the document fiscal position maps the taxes after the company-tree filter. | N-U30-116 |
| VDR-U30-C304 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2680 | self.show_update_fpos = self.line_ids and | FACT | form edit | — | Changing the fiscal position on a document with items raises a flag that offers the Update Taxes and Accounts action. | N-U30-116 |
| VDR-U30-C305 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6024 | new_taxes = line._get_computed_taxes() | FACT | action on a non-posted document | — | The update action recomputes the taxes of each item from product and fiscal position, adjusts unit price when the price-included mix changes, recomputes price for zero-price items, and requeues tax and account computation inside the synchroniser so tax items follow. | N-U30-116 |
| VDR-U30-C306 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:1026 | not show_update_fpos or state | FACT | form view | — | The update action is hidden for posted and cancelled documents. | N-U30-116 |
| VDR-U30-C307 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2866 | impacted_countries = amls.tax_ids.country_id | FACT | always | — | A document may not keep taxes from a country different from its tax country (company fiscal country or foreign-VAT position country), whatever the fiscal position does. | N-U30-117 |
| VDR-U30-C308 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1132 | return self.invoice_date or fields.Date.context_today(self) | FACT | always | — | The date used for the document rate is the invoice date, else today; the supply date does not enter this date in the base implementation. | N-U30-125 |
| VDR-U30-C309 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1136 | return self.env | FACT | always | — | The expected rate is the conversion rate from company currency to document currency on the rate date. | N-U30-125 |
| VDR-U30-C310 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1108 | def _compute_taxable_supply_date | FACT | always | — | The supply-date computation is an empty stub and the rate recomputation depends on it, so a localisation could change the rate date only by overriding the date method; no installed module does. | N-U30-134 |
| VDR-U30-C311 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:537 | invoice_currency_rate = fields.Float( | FACT | always | — | The document rate is a stored computed field that users may edit in draft (readonly False), is not copied, and is shown only to the multi-currency group. | N-U30-125 |
| VDR-U30-C312 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1155 | move.invoice_currency_rate = move.expected_currency_rate | FACT | invoice-like | — | For invoice-like documents the rate is recomputed to the expected rate whenever currency, company, invoice date or supply date change. | N-U30-125 |
| VDR-U30-C313 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2881 | must be strictly positive | FACT | foreign currency invoice | — | A foreign-currency invoice must have a strictly positive rate. | N-U30-135 |
| VDR-U30-C314 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5644 | is_manual_rate = invoice.invoice_currency_rate | FACT | sale document posted without invoice date | — | When a sales document is posted without invoice date the date is set to today while a manually set rate is protected from recomputation. | N-U30-132 |
| VDR-U30-C315 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6095 | def refresh_invoice_currency_rate | FACT | draft with rate different from expected | — | A draft with a manual rate shows a button that resets the rate to the expected one for the invoice date. | N-U30-132 |
| VDR-U30-C316 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | FACT | always | — | The rate on a date is the latest rate on or before the date for the root company (or global), else the earliest available rate, else 1.0. | N-U30-128 |
| VDR-U30-C317 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:278 | company = (company or self.env.company).root_id | FACT | always | — | Rates are always resolved against the root company, so branches share company rates. | N-U30-128 |
| VDR-U30-C318 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:120 | def _get_rates | OBSERVATION | restored database | — | OBSERVATION (dump): two currencies are active (THB, USD, both 0.01 rounding) and no rate rows exist, so any conversion resolves to rate 1.0 until rates are loaded. | N-U30-136 |
| VDR-U30-C319 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:303 | return to_currency.round(to_amount) if round else to_amount | FACT | always | — | Conversion multiplies by the resolved rate and rounds in the target currency. | N-U30-128 |
| VDR-U30-C320 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:760 | line.currency_rate = line.move_id.invoice_currency_rate or 1.0 | FACT | invoice-like | — | An invoice item uses the document stored rate; other entries use the market rate at the invoice date else the entry date. | N-U30-129 |
| VDR-U30-C321 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:780 | line.amount_currency = line.currency_id.round(line.balance * line.currency_rate) | FACT | amount in currency not given | — | A missing amount in currency defaults to balance times rate, rounded in the item currency; for company-currency items of non-invoices it equals the balance. | N-U30-129 |
| VDR-U30-C322 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1771 | balance = line.company_id.currency_id.round(line.amount_currency / line.currency_rate) | FACT | amount, rate or type changed and balance not protected or changed | — | The line synchroniser derives the company balance as amount in currency divided by the rate, rounded in company currency, unless the balance itself was changed or protected (re-read of VDR-U11-C286). | N-U30-127 |
| VDR-U30-C323 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1586 | def _get_product_base_line_currency_rate | FACT | always | — | Base lines of invoices use the stored document rate; base lines of other entries use the absolute ratio of the item amount in currency to its balance, zero when the balance is zero. | N-U30-129 |
| VDR-U30-C324 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:229 | term_vals['company_amount'] = residual_amount | FACT | payment term | — | Instalments use independent rounding per currency with the last instalment carrying the remainder, so the sum in company currency equals the document total in company currency regardless of the document rate. | N-U30-130 |
| VDR-U30-C325 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:335 | payment_rate = self.env['res.currency']._get_conversion_rate( | FACT | currencies differ | — | The company-currency amounts of cash-basis entries use the payment rate, not the rate of the invoice, and no exchange difference is booked on tax accounts for the change; exchange differences are booked on the receivable and payable items by the matching. | N-U30-131 |
| VDR-U30-C326 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3027 | 'always_tax_exigible': True | FACT | exchange difference entry | — | Exchange-difference entries are created always exigible, with items on the original account and the gain or loss account (re-read of VDR-U12-C138). | N-U30-131 |
| VDR-U30-C327 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:2996 | return company.income_currency_exchange_account_id | FACT | always | — | Exchange gains go to the income exchange account and losses to the expense exchange account; the dump has the exchange journal and both accounts configured. | N-U30-131 |
| VDR-U30-C328 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3101 | diff_balance = self.currency_id._convert(diff_amount_currency | UNKNOWN | foreign-currency documents | RT | UNKNOWN — EVIDENCE INSUFFICIENT: numeric consistency between document rate, rounding item rate and tax item balances for foreign-currency documents needs execution with loaded rates. | N-U30-137 |
| VDR-U30-C329 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3773 | stack_list, update_containers = self._get_sync_stack(container) | UNKNOWN | combined edits | RT | UNKNOWN — EVIDENCE INSUFFICIENT: the end-to-end numeric result of the reverse-order chain for combined changes (several lines, rounding item, tax items and terms at once) was not executed; resolve with runtime documents in THB and one foreign currency. | N-U30-018 |
| VDR-U30-C330 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:918 | synchronized only when saving | FACT | always | — | Derived items are synchronised only when a record is saved; the line subtotal and total are therefore computed separately so users see figures on unsaved drafts. | N-U30-003 |
| VDR-U30-C331 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3211 | Skip posted moves. | FACT | always | — | Automatic balancing skips posted entries; with rounding items and tax items it is one of the synchronisers that act only before posting. | N-U30-005 |
| VDR-U30-C332 | FUNCTION MAPPING REQUIRED | account/models/account_payment_term.py:183 | does not change the totals | FACT | always | — | The term computation is designed so that the sum of all computed instalments equals the document total in both currencies even with cash rounding. | N-U30-020 |
| VDR-U30-C333 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3591 | def _sync_dynamic_line(self, existing_key_fname | INFERENCE | always | — | INFERENCE (lines 3591-3695 contain no state test): payment-term and the other generic synchronisers are not explicitly limited to drafts; on posted documents their inputs are frozen by the read-only rules and by the lock checks. | N-U30-029 |
| VDR-U30-C334 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1448 | invoice.needed_terms[frozendict({ | FACT | no payment term | — | A payment term is optional: without one the document still gets one payable or receivable item due at the document due date. | N-U30-030 |
| VDR-U30-C335 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3074 | of creating again all tax lines | FACT | always | — | Tax items are prepared as a diff against the existing ones (update, delete, add) rather than being recreated each time. | N-U30-036 |
| VDR-U30-C336 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5762 | group_partial_purchase_deductibility | FACT | posting a bill with partial deductibility | — | Partial deductibility is optional: its per-line field is exposed through a permission group which posting a partly deductible bill grants to the posting user (re-read of VDR-TXA1-C121). | N-U30-044 |
| VDR-U30-C337 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1503 | You cannot use taxes on lines | FACT | off-balance accounts | — | Taxes cannot be used on items of off-balance accounts, which must be alone on their entry. | N-U30-047 |
| VDR-U30-C338 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1903 | expected tax amount of the | FACT | always | — | The global method exists so the tax of the whole document equals the rounded tax computed on the whole document (documentation example with two equal lines: 67.57 against two rounded line taxes of 33.79). | N-U30-051 |
| VDR-U30-C339 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3079 | smallest coins do not exist | FACT | always | — | Cash rounding exists for currencies whose smallest coins are no longer in circulation, so a document paid in cash can be rounded to the smallest coin. | N-U30-069 |
| VDR-U30-C340 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3145 | cash_rounding = self.invoice_cash_rounding_id.with_company(self.company_id) | UNKNOWN | cash rounding enabled | RT | UNKNOWN — EVIDENCE INSUFFICIENT: no cash-rounding method is defined in the dump; the behaviour with missing profit or loss account, with the largest-tax strategy on documents with several tax groups, and the interaction of the rounding item with a recomputed tax item need execution. | N-U30-080 |
| VDR-U30-C341 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:603 | if you encounter rounding issues | FACT | always | — | The summary field is documented as the place where a user can edit tax amounts when rounding issues appear. | N-U30-082 |
| VDR-U30-C342 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:174 | at reconciliation, this amount cancelled | FACT | on-payment tax | — | Purpose of the transition account: it holds the tax of an unpaid document and, at reconciliation, the paid share is cancelled there and put on the regular tax account; an on-payment tax is due when payment is received. | N-U30-096 |
| VDR-U30-C343 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:580 | caba_treatment == 'tax' | INFERENCE | several partial payments | RT | INFERENCE (lines 580-594): only tax items get the residual correction on the last partial; base items are scaled by percentage only, so over several partial payments the reported base can deviate by rounding units. Needs execution. | N-U30-111 |
| VDR-U30-C344 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5498 | will be reconciled with its reverse | FACT | always | — | A cancelling reversal reconciles the receivable, payable or liquidity items of the original with its reverse so the original is neutralised. | N-U30-114 |
| VDR-U30-C345 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3405 | we don't need to recompute anything | INFERENCE | credit note created by reversal of an invoice | RT | INFERENCE (lines 2090-2094 of the item model, 3818-3823 and 3405-3409): a credit note produced by copy carries copied tax and term items and product items whose balance is dropped; whether its tax amounts end up copied or recomputed depends on the synchroniser branch taken at creation. Needs execution. | N-U30-124 |
| VDR-U30-C346 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:1644 | All computation are managing the | FACT | always | — | Every tax computation is carried in the document currency and in the company currency at the same time, using a rate carried on the base line. | N-U30-126 |
| VDR-U30-C347 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:1121 | groups="base.group_multi_currency" | FACT | form view | — | The currency and its rate are shown on the document only to the multi-currency group; the rate is read-only after draft. | N-U30-133 |
| VDR-U30-C348 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:101 | def _reverse_moves | FACT | hr_expense installed (it is) | — | Reversing a document that came from expenses first clears its expense links, then reverses through the base method; cancelling such a document also clears the links (so expenses can be reimbursed again). | N-U30-121 |
| VDR-U30-C349 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:38 | access_account_move_uinvoice | OBSERVATION | restored database | — | OBSERVATION (dump versus source): the account module declares four access rows each for documents and items (manager read, read-only read, invoicing full, portal read); the dump holds seven for documents and eight for items, the extra rows coming from other installed modules that name the models (not decomposed row by row). | N-U30-015 |
| VDR-U30-C350 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:128 | account_move_comp_rule | OBSERVATION | restored database | — | OBSERVATION (dump): documents and items each have one global company rule (company in allowed companies) plus group rules (all invoices, personal invoices, portal, purchase user, read-only, expense approver). | N-U30-015 |
| VDR-U30-C351 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:170 | tax_comp_rule | OBSERVATION | restored database | — | OBSERVATION (dump): taxes, tax groups and distribution lines are limited by a global company rule (company is a parent of an allowed company; distribution lines also allow no company); the dump holds seven access rows for taxes, five for tax groups and four for distribution lines. | N-U30-047 |
| VDR-U30-C352 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:314 | taxes.tax_group_id = self.env['account.tax.group'].search([ | FACT | tax without a group | — | A tax without a tax group (or with a group of another country or company) receives the first tax group found for its country and company tree, else the first group without country. | N-U30-093 |
| VDR-U30-C353 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:14 | tax_output_vat_0 | FACT | l10n_th template load | — | The Thai template leaves the tax group empty on the zero-rated and exempt VAT taxes (input and output, csv lines 10, 14, 18, 22), so the default rule above assigns them. | N-U30-093 |
| VDR-U30-C354 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:304 | def _compute_tax_group_id | OBSERVATION | restored database | — | OBSERVATION (dump): the four zero-rated and exempt VAT taxes (ids 3 to 6) are in the group WHT 1%, while standard VAT 7% is in VAT 7% (consistent with VDR-U13-C082). | N-U30-093 |
| VDR-U30-C355 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2823 | def tax_group_grouping_function | INFERENCE | document with a zero-rated or exempt line | RT | INFERENCE (lines 2823-2831 and the tax-data list in the core calculation): the summary groups tax data by the tax group of each tax regardless of the amount, so a zero-rated or exempt line contributes its base to the group named WHT 1% with a zero tax amount, next to any one-percent withholding on the same document. Needs execution. | N-U30-093 |
| VDR-U30-C356 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:28 | _order = 'sequence asc, id' | FACT | always | — | Tax groups are ordered by sequence then identifier, so the first group of a country is the one with the lowest sequence and identifier (in the dump the withholding one-percent group). | N-U30-093 |
